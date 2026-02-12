"""
Apply response transforms to x-stackQL-resources in generated provider specs.

Run this **after** ``npm run generate-provider`` (which creates the
``x-stackQL-resources`` block from the CSV inventory) and **before**
publishing the provider.

Reads a declarative config (``response_transforms.json``) and patches
matching operations in ``x-stackQL-resources`` with the specified
response transform configuration.

Provider specs are YAML files at::

    {spec_dir}/{provider}/v00.00.00000/services/{service}.yaml

where ``x-stackQL-resources`` lives under ``components``.

Usage::

    python -m stackql_databricks_provider.add_response_transforms [--spec-dir DIR] [--config FILE]
"""

import glob
import json
import logging
import os
import sys
from typing import Any, Dict, List, Optional

import yaml

logger = logging.getLogger(__name__)

TRANSFORMS_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "response_transforms.json"
)

SPEC_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "stackql-provider", "src"
)

# Map config scope names to provider directory names
SCOPE_TO_PROVIDER = {
    "account": "databricks_account",
    "workspace": "databricks_workspace",
}


def load_transforms(transforms_path: Optional[str] = None) -> Dict[str, Any]:
    """Load the declarative transform config.

    Args:
        transforms_path: Path to JSON config.  Defaults to
            ``response_transforms.json`` next to this module.

    Returns:
        Dict mapping ``scope/service/operationId`` to transform config.
    """
    path = transforms_path or TRANSFORMS_PATH
    if not os.path.exists(path):
        logger.warning("Transforms file not found: %s", path)
        return {}
    with open(path) as f:
        data = json.load(f)
    transforms = data.get("transforms", {})
    logger.info("Loaded %d transform entries from %s", len(transforms), path)
    return transforms


def _find_service_yaml(
    spec_dir: str,
    provider: str,
    service: str,
) -> Optional[str]:
    """Find the service YAML file, handling version directories.

    Searches ``{spec_dir}/{provider}/v*/services/{service}.yaml``.

    Returns:
        Path to the YAML file, or None.
    """
    pattern = os.path.join(spec_dir, provider, "v*", "services", f"{service}.yaml")
    matches = glob.glob(pattern)
    if matches:
        # Use the latest version if multiple exist
        matches.sort(reverse=True)
        return matches[0]
    return None


def _operation_id_to_ref(spec: Dict[str, Any], operation_id: str) -> Optional[str]:
    """Look up an operationId in the spec's paths and return the $ref string.

    Walks ``spec["paths"]`` to find the operation matching the given
    operationId, then constructs the ``$ref`` string used in
    ``x-stackQL-resources`` (e.g.
    ``#/paths/~1api~12.0~1usage~1download/get``).

    Returns:
        The ``$ref`` string, or None if not found.
    """
    for path, methods in spec.get("paths", {}).items():
        for http_method, operation in methods.items():
            if isinstance(operation, dict) and operation.get("operationId") == operation_id:
                encoded_path = path.replace("/", "~1")
                return f"#/paths/{encoded_path}/{http_method}"
    return None


def _find_method_in_resources(
    resources: Dict[str, Any],
    operation_id: str,
    spec: Optional[Dict[str, Any]] = None,
) -> Optional[Dict[str, Any]]:
    """Find a method dict in x-stackQL-resources by operationId.

    Searches all resources' methods, matching by:
    1. Direct method key match (e.g. ``billable_usage_download``)
    2. ``$ref`` match via operationId → path lookup (for cases where
       ``npm run generate-provider`` remaps the method key)

    Returns:
        The method dict (mutable reference), or None.
    """
    for resource_name, resource in resources.items():
        methods = resource.get("methods", {})
        # Direct key match
        if operation_id in methods:
            return methods[operation_id]

    # Fallback: resolve operationId to $ref and match
    if spec is not None:
        target_ref = _operation_id_to_ref(spec, operation_id)
        if target_ref:
            for resource_name, resource in resources.items():
                methods = resource.get("methods", {})
                for method_name, method in methods.items():
                    ref = method.get("operation", {}).get("$ref", "")
                    if ref == target_ref:
                        return method

    return None


def apply_transforms(
    spec_dir: Optional[str] = None,
    transforms_path: Optional[str] = None,
) -> Dict[str, int]:
    """Apply response transforms to x-stackQL-resources in provider spec files.

    For each transform entry, finds the matching YAML service spec and
    operation in ``components.x-stackQL-resources``, then merges the
    transform config into the method's ``response`` block.

    Args:
        spec_dir: Root provider spec directory (containing
            ``databricks_account/`` and ``databricks_workspace/``).
            Defaults to ``stackql-provider/src/``.
        transforms_path: Path to the transforms JSON config.

    Returns:
        Summary dict with counts per scope.
    """
    if spec_dir is None:
        spec_dir = SPEC_DIR

    transforms = load_transforms(transforms_path)
    if not transforms:
        return {"account": 0, "workspace": 0}

    summary: Dict[str, int] = {"account": 0, "workspace": 0}

    # Group transforms by scope/service for efficient file access
    by_file: Dict[str, list] = {}
    for key, config in transforms.items():
        parts = key.split("/")
        if len(parts) != 3:
            logger.warning(
                "Invalid transform key: %s (expected scope/service/operationId)",
                key,
            )
            continue
        scope, service, operation_id = parts
        file_key = f"{scope}/{service}"
        by_file.setdefault(file_key, []).append((operation_id, config, key))

    for file_key, entries in by_file.items():
        scope, service = file_key.split("/")
        provider = SCOPE_TO_PROVIDER.get(scope)
        if not provider:
            logger.warning("Unknown scope: %s", scope)
            continue

        spec_path = _find_service_yaml(spec_dir, provider, service)
        if spec_path is None:
            logger.warning(
                "Service YAML not found for %s/%s (looked in %s/%s/v*/services/%s.yaml)",
                scope, service, spec_dir, provider, service,
            )
            continue

        with open(spec_path) as f:
            spec = yaml.safe_load(f)

        resources = spec.get("components", {}).get("x-stackQL-resources", {})
        if not resources:
            logger.warning(
                "No x-stackQL-resources in %s (run npm run generate-provider first?)",
                spec_path,
            )
            continue

        modified = False
        for operation_id, config, key in entries:
            method = _find_method_in_resources(resources, operation_id, spec)
            if method is None:
                logger.warning("Operation not found in x-stackQL-resources: %s", key)
                continue

            # Merge response config
            if "response" in config:
                existing_response = method.get("response", {})
                existing_response.update(config["response"])
                method["response"] = existing_response

            modified = True
            summary[scope] += 1
            logger.info("Applied transform: %s", key)

        if modified:
            with open(spec_path, "w") as f:
                yaml.dump(spec, f, default_flow_style=False, sort_keys=False,
                          allow_unicode=True, width=120)
            logger.info("Updated %s", spec_path)

    return summary


def main():
    """CLI entry point."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s - %(message)s",
    )

    import argparse

    parser = argparse.ArgumentParser(
        description="Apply response transforms to x-stackQL-resources post provider generation"
    )
    parser.add_argument(
        "--spec-dir",
        default=None,
        help=(
            "Root provider spec directory containing databricks_account/ and "
            "databricks_workspace/ (default: stackql-provider/src/)"
        ),
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Path to response_transforms.json (default: next to this module)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable debug logging",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    spec_dir = args.spec_dir or SPEC_DIR
    print("Applying response transforms to x-stackQL-resources...")
    print(f"  Spec dir: {spec_dir}")
    print()

    summary = apply_transforms(args.spec_dir, args.config)

    print()
    print("=" * 60)
    print("Response Transform Summary")
    print("=" * 60)
    print(f"  Account transforms applied:   {summary['account']}")
    print(f"  Workspace transforms applied: {summary['workspace']}")
    print()

    if summary["account"] == 0 and summary["workspace"] == 0:
        print("  No transforms applied. Ensure x-stackQL-resources exists")
        print("  in the spec files (run npm run generate-provider first).")
        print()


if __name__ == "__main__":
    main()

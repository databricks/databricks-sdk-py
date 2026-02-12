"""
Apply response transforms to x-stackQL-resources in generated provider specs.

Run this **after** ``npm run generate-provider`` (which creates the
``x-stackQL-resources`` block from the CSV inventory) and **before**
publishing the provider.

Reads a declarative config (``response_transforms.json``) and patches
matching operations in ``x-stackQL-resources`` with the specified
response transform configuration.

Usage::

    python -m stackql_databricks_provider.add_response_transforms [--spec-dir DIR] [--config FILE]
"""

import json
import logging
import os
import sys
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

TRANSFORMS_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "response_transforms.json"
)

SPEC_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "openapi_generated"
)


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


def _find_method_in_resources(
    resources: Dict[str, Any],
    operation_id: str,
) -> Optional[Dict[str, Any]]:
    """Find a method dict in x-stackQL-resources by operationId.

    Searches all resources' methods for one whose key matches the
    given operationId.

    Returns:
        The method dict (mutable reference), or None.
    """
    for resource_name, resource in resources.items():
        methods = resource.get("methods", {})
        if operation_id in methods:
            return methods[operation_id]
    return None


def apply_transforms(
    spec_dir: Optional[str] = None,
    transforms_path: Optional[str] = None,
) -> Dict[str, int]:
    """Apply response transforms to x-stackQL-resources in spec files.

    For each transform entry, finds the matching spec file and operation
    in ``x-stackQL-resources``, then deep-merges the transform config
    into the method's ``response`` block.

    Args:
        spec_dir: Root spec directory containing ``account/`` and
            ``workspace/`` subdirectories.
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
        spec_path = os.path.join(spec_dir, scope, f"{service}.json")

        if not os.path.exists(spec_path):
            logger.warning("Spec file not found: %s", spec_path)
            continue

        with open(spec_path) as f:
            spec = json.load(f)

        resources = spec.get("x-stackQL-resources", {})
        if not resources:
            logger.warning(
                "No x-stackQL-resources in %s (run npm run generate-provider first?)",
                spec_path,
            )
            continue

        modified = False
        for operation_id, config, key in entries:
            method = _find_method_in_resources(resources, operation_id)
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
                json.dump(spec, f, indent=2, sort_keys=False)
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
        help="Directory containing account/ and workspace/ spec JSON files",
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

    print("Applying response transforms to x-stackQL-resources...")

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

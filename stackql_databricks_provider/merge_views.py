"""
Merge view definitions into generated StackQL provider service specs.

Run this as the **final** post-generation step, after
``add_response_transforms`` and all other post-processing.

Scans ``views/{account,workspace}/{service}/views.yaml`` for view
resource definitions and injects them into the corresponding
``components.x-stackQL-resources`` section of each service YAML.

Usage::

    python -m stackql_databricks_provider.merge_views [--spec-dir DIR] [--views-dir DIR]
"""

import glob
import logging
import os
from typing import Any, Dict, Optional

import yaml

logger = logging.getLogger(__name__)

VIEWS_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "views"
)

SPEC_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "stackql-provider", "src"
)

SCOPE_TO_PROVIDER = {
    "account": "databricks_account",
    "workspace": "databricks_workspace",
}


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
        matches.sort(reverse=True)
        return matches[0]
    return None


def _discover_views(views_dir: str) -> Dict[str, Dict[str, Any]]:
    """Discover all view definition files.

    Scans ``{views_dir}/{scope}/{service}/views.yaml``.

    Returns:
        Dict keyed by ``scope/service`` with parsed YAML contents.
    """
    discovered = {}
    pattern = os.path.join(views_dir, "*", "*", "views.yaml")
    for path in glob.glob(pattern):
        parts = path.replace(views_dir, "").strip(os.sep).split(os.sep)
        if len(parts) >= 3:
            scope, service = parts[0], parts[1]
            with open(path) as f:
                data = yaml.safe_load(f)
            if data:
                key = f"{scope}/{service}"
                discovered[key] = data
                logger.info("Discovered views: %s (%d view(s))", key, len(data))
    return discovered


def merge_views(
    spec_dir: Optional[str] = None,
    views_dir: Optional[str] = None,
) -> Dict[str, int]:
    """Merge view definitions into provider service YAML files.

    For each ``views.yaml`` discovered, loads the matching service spec
    and adds the view resources to ``components.x-stackQL-resources``.

    Args:
        spec_dir: Root provider spec directory containing
            ``databricks_account/`` and ``databricks_workspace/``.
            Defaults to ``stackql-provider/src/``.
        views_dir: Root views directory.
            Defaults to ``views/`` next to this module.

    Returns:
        Summary dict with counts per scope.
    """
    if spec_dir is None:
        spec_dir = SPEC_DIR
    if views_dir is None:
        views_dir = VIEWS_DIR

    all_views = _discover_views(views_dir)
    if not all_views:
        logger.info("No view definitions found in %s", views_dir)
        return {"account": 0, "workspace": 0}

    summary: Dict[str, int] = {"account": 0, "workspace": 0}

    for file_key, view_resources in all_views.items():
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

        resources = spec.get("components", {}).get("x-stackQL-resources")
        if resources is None:
            logger.warning(
                "No x-stackQL-resources in %s (run npm run generate-provider first?)",
                spec_path,
            )
            continue

        views_added = 0
        for view_name, view_def in view_resources.items():
            if view_name in resources:
                logger.info("View %s already exists in %s, replacing", view_name, file_key)
            resources[view_name] = view_def
            views_added += 1
            logger.info("Merged view: %s.%s.%s", provider, service, view_name)

        if views_added > 0:
            with open(spec_path, "w") as f:
                yaml.dump(spec, f, default_flow_style=False, sort_keys=False,
                          allow_unicode=True, width=120)
            summary[scope] += views_added
            logger.info("Updated %s (%d view(s) merged)", spec_path, views_added)

    return summary


def main():
    """CLI entry point."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s - %(message)s",
    )

    import argparse

    parser = argparse.ArgumentParser(
        description="Merge view definitions into x-stackQL-resources post provider generation"
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
        "--views-dir",
        default=None,
        help="Root views directory (default: views/ next to this module)",
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
    views_dir = args.views_dir or VIEWS_DIR
    print("Merging view definitions into x-stackQL-resources...")
    print(f"  Spec dir:  {spec_dir}")
    print(f"  Views dir: {views_dir}")
    print()

    summary = merge_views(args.spec_dir, args.views_dir)

    print()
    print("=" * 60)
    print("View Merge Summary")
    print("=" * 60)
    print(f"  Account views merged:   {summary['account']}")
    print(f"  Workspace views merged: {summary['workspace']}")
    print()

    if summary["account"] == 0 and summary["workspace"] == 0:
        print("  No views merged. Check that views/ contains")
        print("  {scope}/{service}/views.yaml files and that the")
        print("  corresponding service specs exist.")
        print()


if __name__ == "__main__":
    main()

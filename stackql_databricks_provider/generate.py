"""
Generate OpenAPI specifications for all Databricks services.

Produces one JSON file per service module, organized into account/
and workspace/ subdirectories under ``openapi_generated/``.
"""

import json
import logging
import os
import sys
from typing import Any, Dict, List, Optional, Set, Tuple

from stackql_databricks_provider.extract import (
    get_data_classes,
    get_enums,
    get_operation_details,
    get_operations,
    get_resources,
    get_schema_from_data_class,
    get_schema_from_enum,
)
from stackql_databricks_provider.registry import (
    ACCOUNT_API_CLASSES,
    SERVICE_MODULES,
    classify_api_class,
    load_service_module,
)

logger = logging.getLogger(__name__)

OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "openapi_generated"
)


def generate_spec_for_service(
    service_name: str,
    scope: str,
    api_class_names: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Generate a complete OpenAPI 3.0 spec for a service module.

    Args:
        service_name: Module name like ``"compute"``.
        scope: ``"account"`` or ``"workspace"``.
        api_class_names: If provided, only include these API classes.
            When *None*, all classes matching *scope* are included.

    Returns:
        OpenAPI spec as a dict.
    """
    module = load_service_module(service_name)
    resources = get_resources(module)

    if api_class_names is not None:
        class_set = set(api_class_names)
        resources = [(c, s) for c, s in resources if c in class_set]

    paths: Dict[str, Any] = {}
    operation_count = 0
    errors: List[str] = []

    for class_name, resource_snake in resources:
        operations = get_operations(module, class_name)
        for op_name in operations:
            try:
                details = get_operation_details(
                    module,
                    class_name,
                    op_name,
                    service_name=service_name,
                    resource_snake_name=resource_snake,
                )
                for path, methods in details.items():
                    if path not in paths:
                        paths[path] = {}
                    paths[path].update(methods)
                    operation_count += 1
            except Exception as e:
                msg = f"{class_name}.{op_name}: {e}"
                errors.append(msg)
                logger.debug("Skipped operation %s", msg)

    # Collect schemas from dataclasses and enums
    schemas: Dict[str, Any] = {}
    for dc in get_data_classes(module):
        try:
            schemas.update(get_schema_from_data_class(module, dc))
        except Exception as e:
            logger.debug("Skipped dataclass %s: %s", dc.__name__, e)

    for enum_cls in get_enums(module):
        try:
            schemas.update(get_schema_from_enum(enum_cls))
        except Exception as e:
            logger.debug("Skipped enum %s: %s", enum_cls.__name__, e)

    if scope == "account":
        server_url = "https://accounts.cloud.databricks.com"
        server_desc = "Databricks account"
    else:
        server_url = "https://{workspace}.cloud.databricks.com"
        server_desc = "Databricks workspace"

    spec: Dict[str, Any] = {
        "openapi": "3.0.0",
        "info": {
            "title": f"Databricks {service_name.replace('_', ' ').title()} API ({scope})",
            "description": (
                f"OpenAPI specification for the Databricks {service_name} "
                f"service ({scope}-level APIs), generated from the Databricks Python SDK."
            ),
            "version": "0.1.0",
        },
        "servers": [{"url": server_url, "description": server_desc}],
        "paths": paths,
        "components": {"schemas": schemas},
    }

    if server_url.startswith("https://{"):
        spec["servers"][0]["variables"] = {
            "workspace": {
                "default": "your-workspace",
                "description": "Your Databricks workspace name",
            }
        }

    logger.info(
        "Generated %s/%s: %d paths, %d operations, %d schemas (%d skipped)",
        scope,
        service_name,
        len(paths),
        operation_count,
        len(schemas),
        len(errors),
    )
    return spec


def generate_all(output_dir: Optional[str] = None) -> Dict[str, Any]:
    """Generate OpenAPI specs for every service, organized by scope.

    Writes JSON files to ``<output_dir>/account/`` and
    ``<output_dir>/workspace/``.

    Args:
        output_dir: Root directory for output.  Defaults to
            ``stackql_databricks_provider/openapi_generated/``.

    Returns:
        Summary dict with counts.
    """
    if output_dir is None:
        output_dir = OUTPUT_DIR

    account_dir = os.path.join(output_dir, "account")
    workspace_dir = os.path.join(output_dir, "workspace")
    os.makedirs(account_dir, exist_ok=True)
    os.makedirs(workspace_dir, exist_ok=True)

    summary = {
        "account_services": 0,
        "workspace_services": 0,
        "total_paths": 0,
        "total_schemas": 0,
        "errors": [],
    }

    for svc_name in SERVICE_MODULES:
        try:
            module = load_service_module(svc_name)
            resources = get_resources(module)

            account_classes = [c for c, _ in resources if classify_api_class(c) == "account"]
            workspace_classes = [c for c, _ in resources if classify_api_class(c) == "workspace"]

            if account_classes:
                spec = generate_spec_for_service(svc_name, "account", account_classes)
                if spec["paths"]:
                    _write_spec(spec, account_dir, svc_name)
                    summary["account_services"] += 1
                    summary["total_paths"] += len(spec["paths"])
                    summary["total_schemas"] += len(spec["components"]["schemas"])

            if workspace_classes:
                spec = generate_spec_for_service(svc_name, "workspace", workspace_classes)
                if spec["paths"]:
                    _write_spec(spec, workspace_dir, svc_name)
                    summary["workspace_services"] += 1
                    summary["total_paths"] += len(spec["paths"])
                    summary["total_schemas"] += len(spec["components"]["schemas"])

        except Exception as e:
            msg = f"Service {svc_name}: {e}"
            summary["errors"].append(msg)
            logger.error("Failed to generate spec for %s: %s", svc_name, e)

    return summary


def _write_spec(spec: Dict[str, Any], directory: str, service_name: str) -> str:
    """Write a spec to a JSON file and return the path."""
    filepath = os.path.join(directory, f"{service_name}.json")
    with open(filepath, "w") as f:
        json.dump(spec, f, indent=2, sort_keys=False)
    logger.info("Wrote %s", filepath)
    return filepath


def main():
    """CLI entry point for generating all OpenAPI specs."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s - %(message)s",
    )

    import argparse

    parser = argparse.ArgumentParser(
        description="Generate OpenAPI specs from the Databricks Python SDK"
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default=None,
        help="Output directory (default: stackql_databricks_provider/openapi_generated/)",
    )
    parser.add_argument(
        "-s",
        "--service",
        default=None,
        help="Generate for a single service only (e.g. 'compute')",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable debug logging",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    output_dir = args.output_dir or OUTPUT_DIR

    if args.service:
        account_dir = os.path.join(output_dir, "account")
        workspace_dir = os.path.join(output_dir, "workspace")
        os.makedirs(account_dir, exist_ok=True)
        os.makedirs(workspace_dir, exist_ok=True)

        module = load_service_module(args.service)
        resources = get_resources(module)
        account_classes = [c for c, _ in resources if classify_api_class(c) == "account"]
        workspace_classes = [c for c, _ in resources if classify_api_class(c) == "workspace"]

        if account_classes:
            spec = generate_spec_for_service(args.service, "account", account_classes)
            path = _write_spec(spec, account_dir, args.service)
            print(f"Account spec: {path}")
            print(f"  Paths: {len(spec['paths'])}, Schemas: {len(spec['components']['schemas'])}")

        if workspace_classes:
            spec = generate_spec_for_service(args.service, "workspace", workspace_classes)
            path = _write_spec(spec, workspace_dir, args.service)
            print(f"Workspace spec: {path}")
            print(f"  Paths: {len(spec['paths'])}, Schemas: {len(spec['components']['schemas'])}")

        if not account_classes and not workspace_classes:
            print(f"No API classes found for service: {args.service}")
            sys.exit(1)
    else:
        print("Generating OpenAPI specs for all Databricks services...")
        print(f"Output directory: {output_dir}")
        print()

        summary = generate_all(output_dir)

        print()
        print("=" * 60)
        print("Generation Summary")
        print("=" * 60)
        print(f"  Account services:   {summary['account_services']}")
        print(f"  Workspace services: {summary['workspace_services']}")
        print(f"  Total paths:        {summary['total_paths']}")
        print(f"  Total schemas:      {summary['total_schemas']}")

        if summary["errors"]:
            print(f"\n  Errors ({len(summary['errors'])}):")
            for err in summary["errors"][:10]:
                print(f"    - {err}")
            if len(summary["errors"]) > 10:
                print(f"    ... and {len(summary['errors']) - 10} more")

        print()


if __name__ == "__main__":
    main()

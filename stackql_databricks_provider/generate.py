"""
Generate OpenAPI specifications for all Databricks services.

Produces one JSON file per service module, organized into account/
and workspace/ subdirectories under ``openapi_generated/``.
"""

import copy
import json
import logging
import os
import shutil
import sys
from datetime import date
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


def _get_sdk_version() -> str:
    """Return the installed Databricks SDK version."""
    try:
        import importlib.metadata
        return importlib.metadata.version("databricks-sdk")
    except Exception:
        return "unknown"


OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "openapi_generated"
)

OVERRIDES_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "spec_overrides.json"
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
                    # Tag each operation with SDK source class
                    for method_detail in methods.values():
                        method_detail["x-stackql-sdk-source"] = class_name
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

    # Sanitize: replace any $ref pointing to undefined schemas with inline object
    _sanitize_orphaned_refs(paths, schemas)

    sdk_namespace = f"databricks.sdk.service.{service_name}"

    spec: Dict[str, Any] = {
        "openapi": "3.0.0",
        "info": {
            "title": f"Databricks {service_name.replace('_', ' ').title()} API ({scope})",
            "description": (
                f"OpenAPI specification for the Databricks {service_name} "
                f"service ({scope}-level APIs), generated from the Databricks Python SDK."
            ),
            "version": "0.1.0",
            "x-stackql-sdk-version": _get_sdk_version(),
            "x-stackql-date-generated": date.today().isoformat(),
            "x-stackql-sdk-namespace": sdk_namespace,
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

    # Apply post-extraction overrides from spec_overrides.json
    overrides = _load_overrides()
    overrides_applied = _apply_overrides(spec, scope, service_name, overrides)

    # Inline $ref in request body schemas so StackQL can see subfields
    _inline_request_body_refs(spec)

    logger.info(
        "Generated %s/%s: %d paths, %d operations, %d schemas (%d skipped, %d overrides)",
        scope,
        service_name,
        len(paths),
        operation_count,
        len(schemas),
        len(errors),
        overrides_applied,
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
    for d in (account_dir, workspace_dir):
        if os.path.exists(d):
            shutil.rmtree(d)
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


def _load_overrides(overrides_path: Optional[str] = None) -> Dict[str, Any]:
    """Load spec overrides from a JSON file.

    Returns:
        Dict keyed by ``scope/service`` with lists of override rules.
    """
    path = overrides_path or OVERRIDES_PATH
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        data = json.load(f)
    # Strip comment keys
    return {k: v for k, v in data.items() if not k.startswith("_")}


def _resolve_json_path(obj: Any, segments: List[str]) -> Tuple[Any, str]:
    """Walk *obj* following dot-delimited path segments.

    Supports:
    - dict keys: ``paths``, ``/api/2.0/foo``
    - array match: ``parameters[name=uid]`` finds the first element in
      a list where ``element["name"] == "uid"``

    Returns:
        ``(parent_object, final_key)`` so the caller can do
        ``parent[key] = value``.
    """
    import re as _re

    current = obj
    for i, seg in enumerate(segments[:-1]):
        # Array predicate match: key[field=value]
        m = _re.match(r"^(.+)\[(\w+)=([^\]]+)\]$", seg)
        if m:
            key, match_field, match_val = m.group(1), m.group(2), m.group(3)
            arr = current[key]
            found = False
            for item in arr:
                if isinstance(item, dict) and str(item.get(match_field)) == match_val:
                    current = item
                    found = True
                    break
            if not found:
                raise KeyError(
                    f"No element with {match_field}={match_val} in {key}"
                )
        else:
            current = current[seg]

    # Handle predicate on the last segment too
    last = segments[-1]
    m = _re.match(r"^(.+)\[(\w+)=([^\]]+)\]$", last)
    if m:
        key, match_field, match_val = m.group(1), m.group(2), m.group(3)
        arr = current[key]
        for item in arr:
            if isinstance(item, dict) and str(item.get(match_field)) == match_val:
                return item, None  # type: ignore[return-value]
        raise KeyError(f"No element with {match_field}={match_val} in {key}")

    return current, last


def _apply_overrides(spec: Dict[str, Any], scope: str, service_name: str,
                     overrides: Dict[str, Any]) -> int:
    """Apply post-extraction overrides to a spec.

    Args:
        spec: The generated OpenAPI spec (mutated in place).
        scope: ``"account"`` or ``"workspace"``.
        service_name: Service name (e.g. ``"database"``).
        overrides: Full overrides dict loaded from ``spec_overrides.json``.

    Returns:
        Number of overrides applied.
    """
    key = f"{scope}/{service_name}"
    rules = overrides.get(key, [])
    applied = 0

    for rule in rules:
        json_path = rule["json_path"]
        value = rule["value"]
        desc = rule.get("description", json_path)

        segments = _parse_json_path(json_path)
        try:
            parent, final_key = _resolve_json_path(spec, segments)
            if final_key is None:
                # Predicate matched an array element; replace the whole element
                # This shouldn't normally happen for set-value use cases
                logger.warning("Override %s: predicate on final segment, skipping", desc)
                continue
            parent[final_key] = value
            applied += 1
            logger.info("Override applied: %s -> %s = %s", key, json_path, value)
        except (KeyError, IndexError, TypeError) as e:
            logger.error("Override failed: %s -> %s: %s", key, json_path, e)

    return applied


def _parse_json_path(json_path: str) -> List[str]:
    """Split a dot-delimited JSON path, respecting dots inside path segments.

    Paths like ``paths./api/2.0/foo.get.parameters[name=uid].required``
    need to keep ``/api/2.0/foo`` as one segment.  We split on dots that
    are NOT preceded by a path-like character sequence.
    """
    segments: List[str] = []
    current = ""
    i = 0
    chars = json_path

    while i < len(chars):
        ch = chars[i]
        if ch == "." and current and not current.startswith("/"):
            # Normal dot separator
            segments.append(current)
            current = ""
        elif ch == "." and current.startswith("/"):
            # Dot inside a path segment like /api/2.0/foo - check if next
            # char continues a path or starts a new segment
            # Heuristic: if next segment starts with a letter or [, it's a
            # new segment; otherwise it's part of the path
            rest = chars[i + 1:] if i + 1 < len(chars) else ""
            if rest and (rest[0].isalpha() or rest[0] == "["):
                segments.append(current)
                current = ""
            else:
                current += ch
        elif ch == "." and not current:
            # Leading dot or consecutive dots - skip
            pass
        else:
            current += ch
        i += 1

    if current:
        segments.append(current)

    return segments


def _inline_request_body_refs(spec: Dict[str, Any]) -> None:
    """Resolve ``$ref`` in request body schemas to inline object properties.

    StackQL's manifest generator does not follow ``$ref`` for request body
    properties, so nested objects appear as opaque ``value: object``.
    This step inlines referenced component schemas so subfields are visible.
    """
    schemas = spec.get("components", {}).get("schemas", {})
    for path_data in spec.get("paths", {}).values():
        for method_data in path_data.values():
            if not isinstance(method_data, dict):
                continue
            request_body = method_data.get("requestBody", {})
            content = request_body.get("content", {})
            for media_type_data in content.values():
                schema = media_type_data.get("schema", {})
                _inline_refs_recursive(schema, schemas, set())


def _inline_refs_recursive(
    schema: Dict[str, Any],
    all_schemas: Dict[str, Any],
    seen: Set[str],
) -> None:
    """Recursively replace ``$ref`` entries with their resolved inline schemas."""
    if not isinstance(schema, dict):
        return

    properties = schema.get("properties", {})
    for prop_name in list(properties.keys()):
        prop_schema = properties[prop_name]
        if not isinstance(prop_schema, dict):
            continue

        if "$ref" in prop_schema:
            ref_name = prop_schema["$ref"].split("/")[-1]
            if ref_name in all_schemas and ref_name not in seen:
                seen.add(ref_name)
                resolved = copy.deepcopy(all_schemas[ref_name])
                # Preserve extra fields (e.g. description) from the original
                for k, v in prop_schema.items():
                    if k != "$ref":
                        resolved[k] = v
                _inline_refs_recursive(resolved, all_schemas, seen)
                properties[prop_name] = resolved
                seen.discard(ref_name)

        elif prop_schema.get("type") == "array" and isinstance(prop_schema.get("items"), dict):
            items = prop_schema["items"]
            if "$ref" in items:
                ref_name = items["$ref"].split("/")[-1]
                if ref_name in all_schemas and ref_name not in seen:
                    seen.add(ref_name)
                    resolved = copy.deepcopy(all_schemas[ref_name])
                    _inline_refs_recursive(resolved, all_schemas, seen)
                    prop_schema["items"] = resolved
                    seen.discard(ref_name)
            elif "properties" in items:
                _inline_refs_recursive(items, all_schemas, seen)

        elif "properties" in prop_schema:
            _inline_refs_recursive(prop_schema, all_schemas, seen)


def _sanitize_orphaned_refs(paths: Dict[str, Any], schemas: Dict[str, Any]) -> None:
    """Replace $ref entries that point to undefined schemas with inline types.

    Walks the entire paths tree looking for ``{"$ref": "#/components/schemas/X"}``
    where ``X`` is not present in *schemas*.  Replaces those with
    ``{"type": "object"}`` so the spec remains valid.
    """
    schema_prefix = "#/components/schemas/"

    def _walk(obj):
        if isinstance(obj, dict):
            if "$ref" in obj:
                ref = obj["$ref"]
                if isinstance(ref, str) and ref.startswith(schema_prefix):
                    schema_name = ref[len(schema_prefix):]
                    if schema_name not in schemas:
                        logger.debug("Replacing orphaned $ref %s with inline object", ref)
                        del obj["$ref"]
                        obj["type"] = "object"
                        return
            for v in obj.values():
                _walk(v)
        elif isinstance(obj, list):
            for item in obj:
                _walk(item)

    _walk(paths)


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

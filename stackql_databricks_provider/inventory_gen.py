"""
Generate CSV inventory files from OpenAPI specs.

Produces one CSV per service spec plus a consolidated ``all_services.csv``
per scope, with columns matching the format expected by
``@stackql/provider-utils``.  Respects existing CSV files so that
manually-edited mappings are preserved.
"""

import csv
import json
import logging
import os
import sys
from typing import Any, Dict, List, Optional, Set, Tuple

logger = logging.getLogger(__name__)

SPEC_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "openapi_generated"
)
INVENTORY_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "inventory"
)

# Column order matches @stackql/provider-utils analyze output
CSV_COLUMNS = [
    "filename",
    "path",
    "operationId",
    "verb",
    "response_object",
    "tags",
    "params",
    "summary",
    "description",
    "stackql_resource_name",
    "stackql_method_name",
    "stackql_verb",
    "stackql_object_key",
]

# Maps HTTP verbs to default StackQL verbs (lowercase for provider-utils)
HTTP_TO_STACKQL_VERB = {
    "get": "select",
    "post": "insert",
    "put": "replace",
    "patch": "update",
    "delete": "delete",
}


def _extract_ref_name(ref: str) -> str:
    """Extract the schema name from a $ref string.

    ``#/components/schemas/CustomLlm`` -> ``CustomLlm``
    """
    if ref and "/" in ref:
        return ref.rsplit("/", 1)[-1]
    return ref or ""


def _get_success_response_object(operation: Dict[str, Any]) -> str:
    """Get the $ref schema name from the 200 response, if any."""
    resp_200 = operation.get("responses", {}).get("200", {})
    content = resp_200.get("content", {})
    json_content = content.get("application/json", {})
    schema = json_content.get("schema", {})
    ref = schema.get("$ref", "")
    return _extract_ref_name(ref)


def _get_params_list(operation: Dict[str, Any]) -> str:
    """Comma-delimited list of parameter names."""
    params = []
    for p in operation.get("parameters", []):
        params.append(p["name"])
    # Also include requestBody properties
    rb = operation.get("requestBody", {})
    content = rb.get("content", {}).get("application/json", {})
    schema = content.get("schema", {})
    for prop_name in schema.get("properties", {}):
        params.append(prop_name)
    return ", ".join(params)


def _get_tags_str(operation: Dict[str, Any]) -> str:
    """Comma-delimited tags."""
    return ", ".join(operation.get("tags", []))


def _get_last_tag(operation: Dict[str, Any]) -> str:
    """Last tag element, used as default stackql_resource_name."""
    tags = operation.get("tags", [])
    return tags[-1] if tags else ""


def _get_stackql_verb(http_verb: str) -> str:
    """Map HTTP verb to default StackQL verb (lowercase)."""
    return HTTP_TO_STACKQL_VERB.get(http_verb.lower(), "")


def extract_operations_from_spec(
    spec: Dict[str, Any],
    service_name: str,
    filename: str = "",
) -> List[Dict[str, str]]:
    """Extract all operations from an OpenAPI spec as inventory rows.

    Args:
        spec: Parsed OpenAPI spec dict.
        service_name: Service name (spec file name without extension).
        filename: Spec filename (e.g. ``"compute.json"``).

    Returns:
        List of dicts, one per operation, with keys matching CSV_COLUMNS.
    """
    if not filename:
        filename = f"{service_name}.json"

    rows = []
    for path_str, methods in spec.get("paths", {}).items():
        for http_verb, operation in methods.items():
            verb_lower = http_verb.lower()
            stackql_verb = _get_stackql_verb(verb_lower)
            if not stackql_verb:
                # Skip unmapped HTTP methods (HEAD, OPTIONS, etc.)
                logger.debug("Skipping %s %s (unmapped HTTP verb)", http_verb, path_str)
                continue

            row = {
                "filename": filename,
                "path": path_str,
                "operationId": operation.get("operationId", ""),
                "verb": verb_lower,
                "response_object": _get_success_response_object(operation),
                "tags": _get_tags_str(operation),
                "params": _get_params_list(operation),
                "summary": operation.get("summary", ""),
                "description": operation.get("description", "").replace("\n", " ").strip(),
                "stackql_resource_name": _get_last_tag(operation),
                "stackql_method_name": operation.get("operationId", ""),
                "stackql_verb": stackql_verb,
                "stackql_object_key": "",
            }
            rows.append(row)
    return rows


def _make_row_key(row: Dict[str, str]) -> str:
    """Build the canonical lookup key for a row: ``filename::path::verb``."""
    return f"{row.get('filename', '')}::{row.get('path', '')}::{row.get('verb', '')}"


def load_existing_csv(csv_path: str) -> Dict[str, Dict[str, str]]:
    """Load an existing CSV inventory, keyed by ``filename::path::verb``.

    Args:
        csv_path: Path to the CSV file.

    Returns:
        Dict mapping canonical key to its full row dict.
    """
    existing: Dict[str, Dict[str, str]] = {}
    if not os.path.exists(csv_path):
        return existing
    with open(csv_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = _make_row_key(row)
            if key:
                existing[key] = dict(row)
    logger.info("Loaded %d existing operations from %s", len(existing), csv_path)
    return existing


def generate_inventory_for_spec(
    spec_path: str,
    output_dir: str,
    scope: str,
) -> Tuple[str, int, int]:
    """Generate or update a CSV inventory for one spec file.

    Existing rows are preserved (not overwritten). Only new operations
    are appended.

    Args:
        spec_path: Path to the OpenAPI JSON spec.
        output_dir: Root inventory directory.
        scope: ``"account"`` or ``"workspace"``.

    Returns:
        Tuple of (csv_path, new_count, existing_count).
    """
    service_name = os.path.splitext(os.path.basename(spec_path))[0]
    filename = f"{service_name}.json"

    with open(spec_path) as f:
        spec = json.load(f)

    rows = extract_operations_from_spec(spec, service_name, filename)

    scope_dir = os.path.join(output_dir, scope)
    os.makedirs(scope_dir, exist_ok=True)
    csv_path = os.path.join(scope_dir, f"{service_name}.csv")

    existing = load_existing_csv(csv_path)
    existing_count = 0
    new_count = 0

    # Build final row list: existing rows first (preserve order), then new rows
    final_rows: List[Dict[str, str]] = []
    seen_keys: Set[str] = set()

    # Keep all existing rows in their original order
    for key, row in existing.items():
        final_rows.append(row)
        seen_keys.add(key)
        existing_count += 1

    # Add new rows only
    for row in rows:
        key = _make_row_key(row)
        if key not in seen_keys:
            final_rows.append(row)
            seen_keys.add(key)
            new_count += 1

    # Write
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(final_rows)

    logger.info(
        "%s/%s: %d existing preserved, %d new added",
        scope, service_name, existing_count, new_count,
    )
    return csv_path, new_count, existing_count


def generate_all_inventories(
    spec_dir: Optional[str] = None,
    output_dir: Optional[str] = None,
) -> Dict[str, Any]:
    """Generate CSV inventories for all OpenAPI spec files.

    Produces per-service CSVs and a consolidated ``all_services.csv``
    per scope.

    Args:
        spec_dir: Root directory containing ``account/`` and ``workspace/``
            spec subdirectories. Defaults to ``openapi_generated/``.
        output_dir: Root directory for CSV output. Defaults to ``inventory/``.

    Returns:
        Summary dict with counts.
    """
    if spec_dir is None:
        spec_dir = SPEC_DIR
    if output_dir is None:
        output_dir = INVENTORY_DIR

    summary = {
        "files_generated": 0,
        "total_new": 0,
        "total_existing": 0,
    }

    for scope in ("account", "workspace"):
        scope_spec_dir = os.path.join(spec_dir, scope)
        if not os.path.isdir(scope_spec_dir):
            continue

        all_rows: List[Dict[str, str]] = []

        for fname in sorted(os.listdir(scope_spec_dir)):
            if not fname.endswith(".json"):
                continue
            spec_path = os.path.join(scope_spec_dir, fname)
            try:
                csv_path, new_count, existing_count = generate_inventory_for_spec(
                    spec_path, output_dir, scope
                )
                summary["files_generated"] += 1
                summary["total_new"] += new_count
                summary["total_existing"] += existing_count

                # Collect rows for consolidated CSV
                with open(csv_path, "r", newline="") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        all_rows.append(row)

            except Exception as e:
                logger.error("Failed to process %s: %s", spec_path, e)

        # Write consolidated all_services.csv per scope
        if all_rows:
            scope_dir = os.path.join(output_dir, scope)
            consolidated_path = os.path.join(scope_dir, "all_services.csv")
            with open(consolidated_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
                writer.writeheader()
                writer.writerows(all_rows)
            logger.info("Wrote consolidated %s/all_services.csv (%d rows)", scope, len(all_rows))

    return summary


def main():
    """CLI entry point for generating CSV inventories."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s - %(message)s",
    )

    import argparse

    parser = argparse.ArgumentParser(
        description="Generate CSV operation inventories from OpenAPI specs"
    )
    parser.add_argument(
        "--spec-dir",
        default=None,
        help="Directory containing account/ and workspace/ spec JSON files",
    )
    parser.add_argument(
        "-o", "--output-dir",
        default=None,
        help="Output directory for CSV files (default: stackql_databricks_provider/inventory/)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable debug logging",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    print("Generating CSV operation inventories...")
    print(f"  Spec dir:   {args.spec_dir or SPEC_DIR}")
    print(f"  Output dir: {args.output_dir or INVENTORY_DIR}")
    print()

    summary = generate_all_inventories(args.spec_dir, args.output_dir)

    print()
    print("=" * 60)
    print("Inventory Summary")
    print("=" * 60)
    print(f"  CSV files generated: {summary['files_generated']}")
    print(f"  New operations:      {summary['total_new']}")
    print(f"  Existing preserved:  {summary['total_existing']}")
    print()


if __name__ == "__main__":
    main()

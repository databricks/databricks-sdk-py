"""
Inject additional example tabs into generated resource documentation.

Run this **after** doc generation to add practical examples (e.g. CLI
usage, CSV export) as extra tabs alongside the auto-generated SQL
examples.

Reads a declarative config (``doc_examples.json``) and patches matching
resource ``index.md`` files, inserting new ``<TabItem>`` blocks into the
``SELECT`` examples ``<Tabs>`` section.

Usage::

    python -m stackql_databricks_provider.add_doc_examples --doc-dir website

Doc path convention::

    {doc_dir}/{provider}/docs/services/{service}/{resource}/index.md
"""

import json
import logging
import os
import re
import sys
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)

EXAMPLES_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "doc_examples.json"
)


def load_examples(examples_path: Optional[str] = None) -> List[Dict[str, Any]]:
    """Load the declarative doc examples config.

    Returns:
        List of example entries.
    """
    path = examples_path or EXAMPLES_PATH
    if not os.path.exists(path):
        logger.warning("Examples config not found: %s", path)
        return []
    with open(path) as f:
        data = json.load(f)
    examples = data.get("examples", [])
    logger.info("Loaded %d doc example entries from %s", len(examples), path)
    return examples


def _resolve_doc_path(
    doc_dir: str,
    provider: str,
    service: str,
    resource: str,
) -> str:
    """Build the path to a resource's index.md."""
    return os.path.join(
        doc_dir, provider, "docs", "services", service, resource, "index.md"
    )


def _inject_select_tabs(content: str, tabs: List[Dict[str, str]]) -> str:
    """Inject additional TabItem blocks into the SELECT examples Tabs.

    Locates the ``## `SELECT` examples`` section, finds the ``<Tabs>``
    component, appends new values to the ``values`` array, and inserts
    new ``<TabItem>`` blocks before the closing ``</Tabs>``.

    Args:
        content: The full markdown file content.
        tabs: List of tab dicts with ``label``, ``value``, ``content`` keys.

    Returns:
        Updated markdown content.
    """
    # Find the SELECT examples section
    select_header_pattern = r"## `SELECT` examples"
    header_match = re.search(select_header_pattern, content)
    if not header_match:
        logger.warning("Could not find '## `SELECT` examples' section")
        return content

    section_start = header_match.start()

    # Find the Tabs component after the SELECT header
    # Look for <Tabs with a values array
    tabs_pattern = r"(<Tabs\s*\n\s*defaultValue=\"[^\"]*\"\s*\n\s*values=\{)\[([^\]]*)\](\}\s*\n>)"
    tabs_match = re.search(tabs_pattern, content[section_start:])
    if not tabs_match:
        logger.warning("Could not find <Tabs> component in SELECT examples section")
        return content

    tabs_abs_start = section_start + tabs_match.start()

    # Find the closing </Tabs> for this section
    # Search from after the Tabs opening tag
    search_from = section_start + tabs_match.end()
    closing_match = re.search(r"</Tabs>", content[search_from:])
    if not closing_match:
        logger.warning("Could not find closing </Tabs> in SELECT examples section")
        return content

    closing_abs_pos = search_from + closing_match.start()

    # Build new value entries for the Tabs values array
    existing_values = tabs_match.group(2).rstrip()
    new_value_entries = ""
    for tab in tabs:
        new_value_entries += (
            f",\n        {{ label: '{tab['label']}', value: '{tab['value']}' }}"
        )

    # Build new TabItem blocks
    new_tab_items = ""
    for tab in tabs:
        new_tab_items += (
            f"\n<TabItem value=\"{tab['value']}\">\n\n"
            f"{tab['content']}\n\n"
            f"</TabItem>\n"
        )

    # Reconstruct the content:
    # 1. Everything before the Tabs values array
    # 2. Updated values array
    # 3. Everything between Tabs opening and closing
    # 4. New TabItems
    # 5. Closing </Tabs> and rest

    # Replace the values array
    updated_values = existing_values + new_value_entries
    new_tabs_opening = tabs_match.group(1) + "[" + updated_values + "\n    ]" + tabs_match.group(3)

    result = (
        content[:tabs_abs_start]
        + new_tabs_opening
        + content[section_start + tabs_match.end():closing_abs_pos]
        + new_tab_items
        + content[closing_abs_pos:]
    )

    return result


def apply_doc_examples(
    doc_dir: str,
    examples_path: Optional[str] = None,
) -> Dict[str, int]:
    """Apply doc examples to generated resource documentation.

    Args:
        doc_dir: Root website directory containing provider doc trees.
        examples_path: Path to the examples JSON config.

    Returns:
        Summary dict with counts.
    """
    examples = load_examples(examples_path)
    if not examples:
        return {"applied": 0, "skipped": 0}

    summary = {"applied": 0, "skipped": 0}

    for entry in examples:
        provider = entry["provider"]
        service = entry["service"]
        resource = entry["resource"]
        section = entry.get("section", "select")
        tabs = entry.get("tabs", [])

        if not tabs:
            continue

        doc_path = _resolve_doc_path(doc_dir, provider, service, resource)
        if not os.path.exists(doc_path):
            logger.warning("Doc file not found: %s", doc_path)
            summary["skipped"] += 1
            continue

        with open(doc_path, "r") as f:
            content = f.read()

        # Check if tabs are already injected (idempotency)
        already_present = all(
            f'value: \'{tab["value"]}\'' in content or
            f'value="{tab["value"]}"' in content
            for tab in tabs
        )
        if already_present:
            logger.info(
                "Tabs already present in %s/%s/%s, skipping",
                provider, service, resource,
            )
            summary["skipped"] += 1
            continue

        if section == "select":
            updated = _inject_select_tabs(content, tabs)
        else:
            logger.warning("Unsupported section: %s", section)
            summary["skipped"] += 1
            continue

        if updated != content:
            with open(doc_path, "w") as f:
                f.write(updated)
            logger.info(
                "Injected %d example tab(s) into %s/%s/%s",
                len(tabs), provider, service, resource,
            )
            summary["applied"] += 1
        else:
            logger.warning(
                "No changes made to %s/%s/%s",
                provider, service, resource,
            )
            summary["skipped"] += 1

    return summary


def main():
    """CLI entry point."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s - %(message)s",
    )

    import argparse

    parser = argparse.ArgumentParser(
        description="Inject additional example tabs into generated resource docs"
    )
    parser.add_argument(
        "--doc-dir",
        required=True,
        help="Root website directory (e.g. 'website') containing provider doc trees",
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Path to doc_examples.json (default: next to this module)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable debug logging",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    print("Injecting doc examples...")
    print(f"  Doc dir: {args.doc_dir}")
    print()

    summary = apply_doc_examples(args.doc_dir, args.config)

    print()
    print("=" * 60)
    print("Doc Examples Summary")
    print("=" * 60)
    print(f"  Resources updated: {summary['applied']}")
    print(f"  Skipped:           {summary['skipped']}")
    print()


if __name__ == "__main__":
    main()

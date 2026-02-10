"""
Example script demonstrating how to extract API information from Databricks SDK.

This script shows how to use the stackql_databricks_provider package to:
1. Extract resources (API classes) from a service module
2. Extract operations (methods) from each resource
3. Extract dataclasses from a service module
4. Generate OpenAPI schemas from dataclasses
"""

from databricks.sdk.service import agentbricks
from stackql_databricks_provider import (
    get_resources,
    get_operations,
    get_data_classes,
    get_schema_from_data_class,
)

def main():
    print("=" * 80)
    print("Extracting API Information from Databricks SDK")
    print("=" * 80)
    print()

    # 1. Get resources from the agentbricks service
    print("1. Extracting Resources from agentbricks service:")
    print("-" * 80)
    resources = get_resources(agentbricks)

    for class_name, resource_name in resources:
        print(f"  • {class_name} → {resource_name}")

    print(f"\nTotal resources found: {len(resources)}\n")

    # 2. Get operations for each resource
    print("2. Extracting Operations from each Resource:")
    print("-" * 80)

    for class_name, resource_name in resources:
        operations = get_operations(agentbricks, class_name)
        print(f"\n  {class_name} ({resource_name}):")
        for operation in operations:
            print(f"    - {operation}")
        print(f"  Total operations: {len(operations)}")

    print()

    # 3. Get dataclasses from the agentbricks service
    print("3. Extracting DataClasses from agentbricks service:")
    print("-" * 80)
    dataclasses = get_data_classes(agentbricks)

    print(f"Found {len(dataclasses)} dataclasses:\n")
    for dc in dataclasses[:5]:  # Show first 5
        print(f"  • {dc.__name__}")

    if len(dataclasses) > 5:
        print(f"  ... and {len(dataclasses) - 5} more")

    print()

    # 4. Generate schema for a sample dataclass
    print("4. Generating OpenAPI Schema for a DataClass:")
    print("-" * 80)

    # Find the CustomLlm dataclass
    custom_llm_dc = next((dc for dc in dataclasses if dc.__name__ == "CustomLlm"), None)

    if custom_llm_dc:
        schema = get_schema_from_data_class(agentbricks, custom_llm_dc)

        print(f"\nSchema for {custom_llm_dc.__name__}:")
        print(f"  Type: {schema[custom_llm_dc.__name__]['type']}")

        properties = schema[custom_llm_dc.__name__]['properties']
        print(f"  Properties ({len(properties)}):")

        for prop_name, prop_info in list(properties.items())[:5]:
            prop_type = prop_info.get('type', 'unknown')
            description = prop_info.get('description', 'No description')
            print(f"    • {prop_name}: {prop_type}")
            print(f"      Description: {description[:60]}...")

        if len(properties) > 5:
            print(f"    ... and {len(properties) - 5} more properties")

        required = schema[custom_llm_dc.__name__].get('required', [])
        print(f"\n  Required fields: {required}")

    print()
    print("=" * 80)
    print("Extraction Complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()

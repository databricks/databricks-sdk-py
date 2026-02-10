"""
Example script demonstrating how to generate OpenAPI specification from Databricks SDK.

This script shows the complete workflow:
1. Extract resources from a service
2. Extract operations from each resource
3. Generate OpenAPI path objects for each operation
4. Extract dataclasses for schemas
5. Generate component schemas
6. Assemble into OpenAPI spec structure
"""

import json
from databricks.sdk.service import agentbricks
from stackql_databricks_provider import (
    get_resources,
    get_operations,
    get_operation_details,
    get_data_classes,
    get_schema_from_data_class,
)


def generate_openapi_spec_for_service(service, service_name: str):
    """
    Generate a complete OpenAPI specification for a service.

    Args:
        service: A service module (e.g., databricks.sdk.service.agentbricks)
        service_name: Name of the service for the spec

    Returns:
        Dictionary containing OpenAPI specification
    """
    print(f"Generating OpenAPI spec for {service_name}...")
    print("=" * 80)

    # 1. Extract resources
    print("\n1. Extracting resources...")
    resources = get_resources(service)
    print(f"   Found {len(resources)} resources:")
    for class_name, resource_name in resources:
        print(f"     • {class_name} → {resource_name}")

    # 2. Generate paths from operations
    print("\n2. Generating OpenAPI paths from operations...")
    paths = {}
    operation_count = 0

    for class_name, resource_name in resources:
        operations = get_operations(service, class_name)
        print(f"\n   {class_name} ({len(operations)} operations):")

        for operation in operations:
            try:
                # Get complete OpenAPI path object
                operation_details = get_operation_details(
                    service, class_name, operation,
                    service_name=service_name,
                    resource_snake_name=resource_name
                )

                # Merge into paths (handle duplicate paths)
                for path, methods in operation_details.items():
                    if path not in paths:
                        paths[path] = {}
                    paths[path].update(methods)
                    operation_count += 1

                print(f"     ✓ {operation}")
            except Exception as e:
                print(f"     ✗ {operation}: {e}")

    print(f"\n   Total: Generated {len(paths)} paths with {operation_count} operations")

    # 3. Generate component schemas from dataclasses
    print("\n3. Generating component schemas from dataclasses...")
    dataclasses = get_data_classes(service)
    print(f"   Found {len(dataclasses)} dataclasses:")

    schemas = {}
    for dc in dataclasses:
        try:
            schema = get_schema_from_data_class(service, dc)
            schemas.update(schema)
            print(f"     ✓ {dc.__name__}")
        except Exception as e:
            print(f"     ✗ {dc.__name__}: {e}")

    print(f"\n   Total: Generated {len(schemas)} component schemas")

    # 4. Assemble OpenAPI specification
    print("\n4. Assembling OpenAPI specification...")
    openapi_spec = {
        "openapi": "3.0.0",
        "info": {
            "title": f"Databricks {service_name.title()} API",
            "description": f"API for Databricks {service_name} service",
            "version": "1.0.0"
        },
        "servers": [
            {
                "url": "https://{workspace}.databricks.com",
                "description": "Databricks workspace",
                "variables": {
                    "workspace": {
                        "default": "your-workspace",
                        "description": "Your Databricks workspace name"
                    }
                }
            }
        ],
        "paths": paths,
        "components": {
            "schemas": schemas
        }
    }

    print(f"   ✓ OpenAPI spec assembled")
    print(f"   • {len(paths)} paths")
    print(f"   • {operation_count} operations")
    print(f"   • {len(schemas)} schemas")

    return openapi_spec


def main():
    print("=" * 80)
    print("OpenAPI Specification Generator for Databricks SDK")
    print("=" * 80)

    # Generate spec for agentbricks service
    spec = generate_openapi_spec_for_service(agentbricks, "agentbricks")

    print("\n" + "=" * 80)
    print("Sample Output")
    print("=" * 80)

    # Show a sample path
    if spec["paths"]:
        sample_path = list(spec["paths"].keys())[0]
        print(f"\nSample Path: {sample_path}")
        print(json.dumps(spec["paths"][sample_path], indent=2))

    # Show a sample schema
    if spec["components"]["schemas"]:
        sample_schema_name = list(spec["components"]["schemas"].keys())[0]
        print(f"\nSample Schema: {sample_schema_name}")
        sample_schema = {sample_schema_name: spec["components"]["schemas"][sample_schema_name]}
        print(json.dumps(sample_schema, indent=2))

    # Optionally save to file
    output_file = "agentbricks_openapi.json"
    print(f"\n" + "=" * 80)
    print(f"Saving to {output_file}...")
    with open(output_file, "w") as f:
        json.dump(spec, f, indent=2)
    print(f"✓ Saved successfully!")

    print("\n" + "=" * 80)
    print("Generation Complete!")
    print("=" * 80)
    print(f"\nGenerated OpenAPI specification:")
    print(f"  • Paths: {len(spec['paths'])}")
    print(f"  • Operations: {sum(len(methods) for methods in spec['paths'].values())}")
    print(f"  • Schemas: {len(spec['components']['schemas'])}")
    print(f"  • Output: {output_file}")


if __name__ == "__main__":
    main()

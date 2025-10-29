#!/usr/bin/env python3
"""
Main script to generate OpenAPI specifications from Databricks SDK service modules.

This script processes all service modules in databricks.sdk.service and generates
standalone OpenAPI YAML specifications for each service.
"""

import os
import sys
import importlib
import inspect
from pathlib import Path
import shutil

# Add parent directory to path to import databricks module
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.sdk_parser import SDKParser
from tools.openapi_generator import OpenAPIGenerator


def get_service_modules():
    """Get all service modules from databricks.sdk.service.

    Returns:
        Dict mapping service names to module objects
    """
    from databricks.sdk import service

    modules = {}

    # Get service directory
    service_dir = Path(service.__file__).parent

    # Iterate through all .py files in the service directory
    for file_path in service_dir.glob('*.py'):
        if file_path.name.startswith('_') or file_path.name == '__init__.py':
            continue

        service_name = file_path.stem

        try:
            # Import the module
            module = importlib.import_module(f'databricks.sdk.service.{service_name}')
            modules[service_name] = module
            print(f"✓ Loaded service module: {service_name}")
        except Exception as e:
            print(f"✗ Failed to load {service_name}: {e}")

    return modules


def generate_spec_for_service(service_name: str, module) -> str:
    """Generate OpenAPI specification for a service module.

    Args:
        service_name: Name of the service
        module: The service module object

    Returns:
        YAML specification as string
    """
    print(f"\n  Parsing {service_name}...")

    # Parse the module
    parser = SDKParser(module)
    parsed_data = parser.parse()

    print(f"    - Found {len(parsed_data['schemas'])} schemas")
    print(f"    - Found {len(parsed_data['api_classes'])} API classes")

    # Count operations
    total_operations = sum(
        len(api_data['operations'])
        for api_data in parsed_data['api_classes'].values()
    )
    print(f"    - Found {total_operations} operations")

    # Get module documentation
    module_doc = inspect.getdoc(module) or ''

    # Generate OpenAPI spec
    print(f"  Generating OpenAPI spec...")
    generator = OpenAPIGenerator(service_name, parsed_data, module_doc)
    spec = generator.generate()

    # Convert to YAML
    yaml_spec = generator.to_yaml()

    return yaml_spec


def clean_output_directory(output_dir: Path):
    """Remove old OpenAPI specs from output directory.

    Args:
        output_dir: Path to output directory
    """
    if output_dir.exists():
        print(f"\nCleaning output directory: {output_dir}")
        for file_path in output_dir.glob('*.yaml'):
            file_path.unlink()
            print(f"  - Deleted: {file_path.name}")
        for file_path in output_dir.glob('*.yml'):
            file_path.unlink()
            print(f"  - Deleted: {file_path.name}")
    else:
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"\nCreated output directory: {output_dir}")


def main():
    """Main entry point for the script."""
    print("=" * 80)
    print("Databricks SDK to OpenAPI Specification Generator")
    print("=" * 80)

    # Get output directory
    repo_root = Path(__file__).parent.parent
    output_dir = repo_root / 'openapi-specs'

    # Clean output directory
    clean_output_directory(output_dir)

    # Load all service modules
    print("\nLoading service modules...")
    modules = get_service_modules()

    if not modules:
        print("\n✗ No service modules found!")
        sys.exit(1)

    print(f"\n✓ Loaded {len(modules)} service modules")

    # Generate specs for each module
    print("\n" + "=" * 80)
    print("Generating OpenAPI specifications...")
    print("=" * 80)

    success_count = 0
    failed_modules = []

    for service_name, module in sorted(modules.items()):
        try:
            print(f"\n[{service_name}]")

            # Generate spec
            yaml_spec = generate_spec_for_service(service_name, module)

            # Write to file
            output_file = output_dir / f'{service_name}.yaml'
            output_file.write_text(yaml_spec, encoding='utf-8')

            print(f"  ✓ Saved to: {output_file}")
            success_count += 1

        except Exception as e:
            print(f"  ✗ Failed to generate spec: {e}")
            import traceback
            traceback.print_exc()
            failed_modules.append(service_name)

    # Print summary
    print("\n" + "=" * 80)
    print("Summary")
    print("=" * 80)
    print(f"✓ Successfully generated: {success_count} specs")
    if failed_modules:
        print(f"✗ Failed: {len(failed_modules)} specs")
        print(f"  Failed modules: {', '.join(failed_modules)}")
    print(f"\nOutput directory: {output_dir}")
    print("=" * 80)


if __name__ == '__main__':
    main()

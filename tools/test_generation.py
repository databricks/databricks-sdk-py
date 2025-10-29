#!/usr/bin/env python3
"""
Test script to verify OpenAPI generation on a single service.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.sdk_parser import SDKParser
from tools.openapi_generator import OpenAPIGenerator


def test_tags_service():
    """Test generation on the tags service (small service)."""
    print("Testing OpenAPI generation on tags service...\n")

    # Import the tags module
    from databricks.sdk.service import tags

    # Parse the module
    print("1. Parsing SDK module...")
    parser = SDKParser(tags)
    parsed_data = parser.parse()

    print(f"   ✓ Found {len(parsed_data['schemas'])} schemas:")
    for schema_name in parsed_data['schemas'].keys():
        print(f"     - {schema_name}")

    print(f"\n   ✓ Found {len(parsed_data['api_classes'])} API classes:")
    for api_name, api_data in parsed_data['api_classes'].items():
        print(f"     - {api_name} ({len(api_data['operations'])} operations)")

    # Generate OpenAPI spec
    print("\n2. Generating OpenAPI specification...")
    generator = OpenAPIGenerator('tags', parsed_data, '')
    spec = generator.generate()

    print(f"   ✓ Generated spec with {len(spec['paths'])} paths")
    print(f"   ✓ Generated spec with {len(spec['components']['schemas'])} schemas")

    # Convert to YAML
    print("\n3. Converting to YAML...")
    yaml_output = generator.to_yaml()
    print(f"   ✓ Generated {len(yaml_output)} bytes of YAML")

    # Print sample
    print("\n4. Sample output (first 1500 chars):")
    print("-" * 80)
    print(yaml_output[:1500])
    print("-" * 80)

    # Write to file
    output_file = Path(__file__).parent.parent / 'openapi-specs' / 'tags.yaml'
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(yaml_output, encoding='utf-8')
    print(f"\n5. Saved to: {output_file}")

    print("\n✓ Test completed successfully!")


if __name__ == '__main__':
    test_tags_service()

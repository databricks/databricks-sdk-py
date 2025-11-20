"""
Demo script showing how to use the stackql_databricks_provider library.

This script demonstrates extracting dataclasses and generating OpenAPI schemas
from Databricks SDK service modules.
"""

import json
import logging
import sys

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s:%(name)s:%(message)s'
)

from stackql_databricks_provider import get_data_classes, get_schema_from_data_class


def demo_with_real_sdk():
    """Demo using the real Databricks SDK."""
    try:
        from databricks.sdk.service import iam

        print("=" * 80)
        print("DEMO: Extracting dataclasses from databricks.sdk.service.iam")
        print("=" * 80)
        print()

        # Get all dataclasses from the IAM service
        dataclasses = get_data_classes(iam)

        print(f"Found {len(dataclasses)} dataclasses")
        print()
        print("First 10 dataclasses:")
        for i, dc in enumerate(dataclasses[:10], 1):
            print(f"  {i}. {dc.__name__}")
        print()

        # Generate schema for AccessControlRequest
        from databricks.sdk.service.iam import AccessControlRequest

        print("=" * 80)
        print("DEMO: Generating schema for AccessControlRequest")
        print("=" * 80)
        print()

        schema = get_schema_from_data_class(iam, AccessControlRequest)

        print(json.dumps(schema, indent=2))
        print()

        # Generate schema for a more complex dataclass
        from databricks.sdk.service.iam import User

        print("=" * 80)
        print("DEMO: Generating schema for User (complex dataclass)")
        print("=" * 80)
        print()

        schema = get_schema_from_data_class(iam, User)

        # Show first 5 properties
        properties = schema["User"]["properties"]
        print(f"User has {len(properties)} properties")
        print()
        print("First 5 properties:")
        for i, (name, prop_schema) in enumerate(list(properties.items())[:5], 1):
            print(f"{i}. {name}:")
            print(f"   {json.dumps(prop_schema, indent=6)}")
        print()

    except ImportError as e:
        print(f"Databricks SDK not available: {e}")
        print("Install the SDK or ensure dependencies are installed.")
        return False

    return True


def demo_with_mock_data():
    """Demo using mock dataclasses (always works)."""
    from dataclasses import dataclass
    from enum import Enum
    from typing import List, Optional
    from types import ModuleType

    print("=" * 80)
    print("DEMO: Using mock dataclasses")
    print("=" * 80)
    print()

    # Create mock enum
    class Status(Enum):
        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"

    # Create mock dataclass
    @dataclass
    class MockResource:
        name: str
        """The resource name"""

        count: int
        """Number of items"""

        status: Optional[Status] = None
        """Current status"""

        tags: Optional[List[str]] = None
        """Resource tags"""

    # Create a mock module
    mock_service = ModuleType("mock_service")
    mock_service.MockResource = MockResource
    mock_service.Status = Status
    sys.modules["mock_service"] = mock_service

    # Get dataclasses
    print("Extracting dataclasses from mock_service...")
    dataclasses = get_data_classes(mock_service)
    print(f"Found {len(dataclasses)} dataclass(es): {[dc.__name__ for dc in dataclasses]}")
    print()

    # Generate schema
    print("Generating schema for MockResource...")
    schema = get_schema_from_data_class(mock_service, MockResource)

    print(json.dumps(schema, indent=2))
    print()

    # Explain the output
    print("=" * 80)
    print("Schema explanation:")
    print("=" * 80)
    properties = schema["MockResource"]["properties"]
    required = schema["MockResource"]["required"]

    print(f"- Total properties: {len(properties)}")
    print(f"- Required fields: {required}")
    print(f"- Optional fields: {[k for k in properties.keys() if k not in required]}")
    print()
    print("Field details:")
    for name, prop in properties.items():
        req_status = "REQUIRED" if name in required else "optional"
        print(f"  - {name} ({req_status}): {prop['type']}")
        if "enum" in prop:
            print(f"    Enum values: {prop['enum']}")
        if "description" in prop:
            print(f"    Description: {prop['description']}")
    print()


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("StackQL Databricks Provider - OpenAPI Schema Generator Demo")
    print("=" * 80)
    print()

    # Try demo with real SDK first
    if not demo_with_real_sdk():
        print("\nFalling back to mock data demo...\n")
        demo_with_mock_data()
    else:
        print("\n" + "=" * 80)
        print("Demo completed successfully!")
        print("=" * 80)

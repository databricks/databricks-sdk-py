"""
Unit tests for parser functions.
"""

import logging
import unittest
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from stackql_databricks_provider.parser import (
    get_data_classes,
    get_schema_from_data_class,
)

# Set up logging for tests
logging.basicConfig(level=logging.DEBUG)


# Test fixtures - mock dataclasses similar to Databricks SDK
class MockStatus(Enum):
    """Mock enum for testing enum conversion"""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"


@dataclass
class SimpleDataClass:
    name: str
    """The name of the resource"""

    count: int
    """The count value"""


@dataclass
class OptionalFieldsDataClass:
    required_field: str
    """This field is required"""

    optional_field: Optional[str] = None
    """This field is optional"""

    optional_with_default: str = "default_value"
    """This field has a default"""


@dataclass
class ComplexDataClass:
    id: str
    """Resource identifier"""

    status: Optional[MockStatus] = None
    """Current status"""

    tags: Optional[List[str]] = None
    """List of tags"""

    metadata: Optional[dict] = None
    """Additional metadata"""


@dataclass
class EmptyDataClass:
    """A dataclass with no fields"""

    pass


class TestGetDataClasses(unittest.TestCase):
    """Test the get_data_classes function"""

    def test_get_data_classes_from_module(self):
        """Test extracting dataclasses from a module"""
        import sys
        from types import ModuleType

        # Create a mock module with dataclasses
        mock_module = ModuleType("mock_service")
        mock_module.SimpleDataClass = SimpleDataClass
        mock_module.OptionalFieldsDataClass = OptionalFieldsDataClass
        mock_module.ComplexDataClass = ComplexDataClass
        mock_module.MockStatus = MockStatus  # Should not be included (not a dataclass)

        # Also add a regular class that's not a dataclass
        class RegularClass:
            pass

        mock_module.RegularClass = RegularClass

        sys.modules["mock_service"] = mock_module

        # Get dataclasses
        dataclasses = get_data_classes(mock_module)

        # Verify
        self.assertEqual(len(dataclasses), 3)
        self.assertIn(SimpleDataClass, dataclasses)
        self.assertIn(OptionalFieldsDataClass, dataclasses)
        self.assertIn(ComplexDataClass, dataclasses)
        self.assertNotIn(MockStatus, dataclasses)
        self.assertNotIn(RegularClass, dataclasses)

    def test_get_data_classes_empty_module(self):
        """Test with a module that has no dataclasses"""
        import sys
        from types import ModuleType

        mock_module = ModuleType("empty_module")
        sys.modules["empty_module"] = mock_module

        dataclasses = get_data_classes(mock_module)

        self.assertEqual(len(dataclasses), 0)


class TestGetSchemaFromDataClass(unittest.TestCase):
    """Test the get_schema_from_data_class function"""

    def test_simple_dataclass_schema(self):
        """Test schema generation for a simple dataclass"""
        import sys
        from types import ModuleType

        mock_module = ModuleType("mock_service")
        sys.modules["mock_service"] = mock_module

        schema = get_schema_from_data_class(mock_module, SimpleDataClass)

        # Verify structure
        self.assertIn("SimpleDataClass", schema)
        self.assertEqual(schema["SimpleDataClass"]["type"], "object")

        # Verify properties
        properties = schema["SimpleDataClass"]["properties"]
        self.assertIn("name", properties)
        self.assertIn("count", properties)

        # Verify types
        self.assertEqual(properties["name"]["type"], "string")
        self.assertEqual(properties["count"]["type"], "integer")

        # Verify descriptions
        self.assertEqual(properties["name"]["description"], "The name of the resource")
        self.assertEqual(properties["count"]["description"], "The count value")

        # Verify required fields (both should be required)
        required = schema["SimpleDataClass"]["required"]
        self.assertEqual(len(required), 2)
        self.assertIn("name", required)
        self.assertIn("count", required)

    def test_optional_fields_dataclass_schema(self):
        """Test schema generation with optional fields"""
        import sys
        from types import ModuleType

        mock_module = ModuleType("mock_service")
        sys.modules["mock_service"] = mock_module

        schema = get_schema_from_data_class(mock_module, OptionalFieldsDataClass)

        # Verify required field is only the one without default
        required = schema["OptionalFieldsDataClass"].get("required", [])
        self.assertEqual(len(required), 1)
        self.assertIn("required_field", required)
        self.assertNotIn("optional_field", required)
        self.assertNotIn("optional_with_default", required)

    def test_complex_dataclass_with_enum(self):
        """Test schema generation with enums and complex types"""
        import sys
        from types import ModuleType

        mock_module = ModuleType("mock_service")
        sys.modules["mock_service"] = mock_module

        schema = get_schema_from_data_class(mock_module, ComplexDataClass)

        properties = schema["ComplexDataClass"]["properties"]

        # Verify enum handling
        self.assertEqual(properties["status"]["type"], "string")
        self.assertIn("enum", properties["status"])
        self.assertEqual(
            set(properties["status"]["enum"]), {"ACTIVE", "INACTIVE", "PENDING"}
        )

        # Verify list handling
        self.assertEqual(properties["tags"]["type"], "array")
        self.assertIn("items", properties["tags"])
        self.assertEqual(properties["tags"]["items"]["type"], "string")

        # Verify dict handling
        self.assertEqual(properties["metadata"]["type"], "object")

        # Verify only id is required (others have Optional)
        required = schema["ComplexDataClass"]["required"]
        self.assertEqual(len(required), 1)
        self.assertIn("id", required)

    def test_empty_dataclass_schema(self):
        """Test schema generation for a dataclass with no fields"""
        import sys
        from types import ModuleType

        mock_module = ModuleType("mock_service")
        sys.modules["mock_service"] = mock_module

        schema = get_schema_from_data_class(mock_module, EmptyDataClass)

        # Verify structure exists but properties is empty
        self.assertIn("EmptyDataClass", schema)
        self.assertEqual(schema["EmptyDataClass"]["type"], "object")
        self.assertEqual(schema["EmptyDataClass"]["properties"], {})
        self.assertNotIn("required", schema["EmptyDataClass"])

    def test_invalid_input(self):
        """Test error handling for invalid input"""
        import sys
        from types import ModuleType

        mock_module = ModuleType("mock_service")
        sys.modules["mock_service"] = mock_module

        # Try to pass a non-dataclass
        class RegularClass:
            pass

        with self.assertRaises(ValueError):
            get_schema_from_data_class(mock_module, RegularClass)


if __name__ == "__main__":
    unittest.main()

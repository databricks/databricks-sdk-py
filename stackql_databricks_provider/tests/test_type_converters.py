"""
Unit tests for type conversion utilities.
"""

import unittest
from enum import Enum
from typing import Dict, List, Optional

from stackql_databricks_provider.type_converters import (
    flatten_description,
    python_type_to_openapi_type,
)


class TestColor(Enum):
    """Test enum"""

    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"


class TestPythonTypeToOpenAPIType(unittest.TestCase):
    """Test Python type to OpenAPI type conversion"""

    def test_basic_types(self):
        """Test basic type conversions"""
        self.assertEqual(python_type_to_openapi_type(str), {"type": "string"})
        self.assertEqual(
            python_type_to_openapi_type(int), {"type": "integer", "format": "int64"}
        )
        self.assertEqual(
            python_type_to_openapi_type(float), {"type": "number", "format": "double"}
        )
        self.assertEqual(python_type_to_openapi_type(bool), {"type": "boolean"})
        self.assertEqual(
            python_type_to_openapi_type(bytes), {"type": "string", "format": "byte"}
        )

    def test_optional_types(self):
        """Test Optional type handling"""
        result = python_type_to_openapi_type(Optional[str])
        self.assertEqual(result, {"type": "string"})

        result = python_type_to_openapi_type(Optional[int])
        self.assertEqual(result, {"type": "integer", "format": "int64"})

    def test_list_types(self):
        """Test List type handling"""
        result = python_type_to_openapi_type(List[str])
        self.assertEqual(result, {"type": "array", "items": {"type": "string"}})

        result = python_type_to_openapi_type(List[int])
        self.assertEqual(
            result, {"type": "array", "items": {"type": "integer", "format": "int64"}}
        )

        # Nested list
        result = python_type_to_openapi_type(List[List[str]])
        self.assertEqual(
            result,
            {"type": "array", "items": {"type": "array", "items": {"type": "string"}}},
        )

    def test_dict_types(self):
        """Test Dict type handling"""
        result = python_type_to_openapi_type(Dict[str, str])
        self.assertEqual(
            result, {"type": "object", "additionalProperties": {"type": "string"}}
        )

        result = python_type_to_openapi_type(Dict[str, int])
        self.assertEqual(
            result,
            {
                "type": "object",
                "additionalProperties": {"type": "integer", "format": "int64"},
            },
        )

    def test_enum_types(self):
        """Test Enum type handling"""
        result = python_type_to_openapi_type(TestColor)
        self.assertEqual(result["type"], "string")
        self.assertIn("enum", result)
        self.assertEqual(set(result["enum"]), {"RED", "GREEN", "BLUE"})

    def test_optional_list(self):
        """Test Optional[List[...]] handling"""
        result = python_type_to_openapi_type(Optional[List[str]])
        self.assertEqual(result, {"type": "array", "items": {"type": "string"}})

    def test_optional_enum(self):
        """Test Optional[Enum] handling"""
        result = python_type_to_openapi_type(Optional[TestColor])
        self.assertEqual(result["type"], "string")
        self.assertIn("enum", result)
        self.assertEqual(set(result["enum"]), {"RED", "GREEN", "BLUE"})

    def test_none_type(self):
        """Test None type handling"""
        result = python_type_to_openapi_type(type(None))
        self.assertEqual(result, {"type": "null"})


class TestFlattenDescription(unittest.TestCase):
    """Test description flattening"""

    def test_single_line_description(self):
        """Test single line description"""
        desc = "This is a simple description"
        result = flatten_description(desc)
        self.assertEqual(result, desc)

    def test_multiline_description(self):
        """Test multi-line description flattening"""
        desc = """This is a
        multi-line
        description"""
        result = flatten_description(desc)
        self.assertEqual(result, "This is a multi-line description")

    def test_description_with_extra_whitespace(self):
        """Test description with extra whitespace"""
        desc = "This  has   extra    spaces"
        result = flatten_description(desc)
        self.assertEqual(result, "This has extra spaces")

    def test_empty_description(self):
        """Test empty description"""
        result = flatten_description("")
        self.assertEqual(result, "")

        result = flatten_description(None)
        self.assertEqual(result, "")

    def test_description_with_newlines_and_tabs(self):
        """Test description with newlines and tabs"""
        desc = "Line 1\n\tLine 2\n  Line 3"
        result = flatten_description(desc)
        self.assertEqual(result, "Line 1 Line 2 Line 3")


if __name__ == "__main__":
    unittest.main()

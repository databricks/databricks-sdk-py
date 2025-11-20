"""
Type conversion utilities for converting Python types to OpenAPI types.
"""

import logging
from enum import Enum
from typing import Any, Dict, get_args, get_origin, Union

logger = logging.getLogger(__name__)


def python_type_to_openapi_type(python_type: Any) -> Dict[str, Any]:
    """
    Convert a Python type annotation to an OpenAPI type specification.

    Args:
        python_type: The Python type to convert (e.g., str, int, List[str], Optional[int])

    Returns:
        Dictionary containing OpenAPI type information (type, format, items, etc.)
    """
    logger.debug(f"Converting Python type: {python_type}")

    # Handle None type
    if python_type is type(None):
        logger.debug("Type is None, returning null")
        return {"type": "null"}

    # Get the origin for generic types (e.g., List, Optional, Dict)
    origin = get_origin(python_type)
    args = get_args(python_type)

    # Handle Optional types (Union[X, None])
    if origin is Union:
        # Filter out None from the union
        non_none_types = [arg for arg in args if arg is not type(None)]

        if len(non_none_types) == 0:
            logger.warning("Optional type with only None found")
            return {"type": "null"}

        if len(non_none_types) == 1:
            # This is Optional[X], convert X
            logger.debug(f"Optional type detected, converting inner type: {non_none_types[0]}")
            return python_type_to_openapi_type(non_none_types[0])
        else:
            # Multiple non-None types in Union
            logger.warning(f"Union type with multiple non-None types: {non_none_types}")
            # Return anyOf for multiple types
            return {
                "anyOf": [python_type_to_openapi_type(t) for t in non_none_types]
            }

    # Handle List types
    if origin is list:
        if args:
            item_type = python_type_to_openapi_type(args[0])
            logger.debug(f"List type with items: {item_type}")
            return {
                "type": "array",
                "items": item_type
            }
        else:
            logger.warning("List type without type parameter")
            return {
                "type": "array",
                "items": {}
            }

    # Handle Dict types
    if origin is dict:
        logger.debug("Dict type detected")
        if len(args) >= 2:
            # Dict[str, X] -> object with additionalProperties
            value_type = python_type_to_openapi_type(args[1])
            return {
                "type": "object",
                "additionalProperties": value_type
            }
        else:
            logger.warning("Dict type without type parameters")
            return {
                "type": "object",
                "additionalProperties": {}
            }

    # Handle basic types
    type_mapping = {
        str: {"type": "string"},
        int: {"type": "integer", "format": "int64"},
        float: {"type": "number", "format": "double"},
        bool: {"type": "boolean"},
        bytes: {"type": "string", "format": "byte"},
    }

    if python_type in type_mapping:
        logger.debug(f"Basic type mapping: {python_type} -> {type_mapping[python_type]}")
        return type_mapping[python_type]

    # Handle bare dict (without type parameters)
    if python_type is dict:
        logger.debug("Bare dict type detected")
        return {
            "type": "object",
            "additionalProperties": {}
        }

    # Handle bare list (without type parameters)
    if python_type is list:
        logger.debug("Bare list type detected")
        return {
            "type": "array",
            "items": {}
        }

    # Check if it's an Enum subclass
    try:
        if isinstance(python_type, type) and issubclass(python_type, Enum):
            logger.debug(f"Enum type detected: {python_type.__name__}")
            enum_values = [member.value for member in python_type]
            logger.info(f"Extracted enum values for {python_type.__name__}: {enum_values}")
            return {
                "type": "string",
                "enum": enum_values
            }
    except TypeError:
        # Not a class, continue to next check
        pass

    # Check if it's a dataclass (has __dataclass_fields__)
    if hasattr(python_type, "__dataclass_fields__"):
        logger.debug(f"Dataclass type detected: {python_type.__name__}")
        return {
            "type": "object",
            "description": f"Reference to {python_type.__name__} dataclass"
        }

    # Unknown type
    logger.warning(f"Unknown type encountered: {python_type}, defaulting to string")
    return {"type": "string"}


def flatten_description(description: str) -> str:
    """
    Flatten a multi-line description to a single line.

    Args:
        description: The description string (potentially multi-line)

    Returns:
        Single-line description with normalized whitespace
    """
    if not description:
        return ""

    # Replace newlines with spaces and normalize whitespace
    flattened = " ".join(description.split())
    logger.debug(f"Flattened description: {flattened[:100]}...")

    return flattened

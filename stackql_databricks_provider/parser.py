"""
Parser functions for extracting dataclasses and schemas from Databricks SDK services.
"""

import inspect
import logging
from dataclasses import fields, is_dataclass
from typing import Any, Dict, List, Type

from .type_converters import flatten_description, python_type_to_openapi_type

logger = logging.getLogger(__name__)


def get_data_classes(service: Any) -> List[Type]:
    """
    Extract all dataclass types from a service module.

    Args:
        service: A service module (e.g., databricks.sdk.service.compute)

    Returns:
        List of dataclass types found in the service module
    """
    logger.info(f"Extracting dataclasses from service: {service.__name__}")

    dataclasses = []

    # Get all members of the module
    for name, obj in inspect.getmembers(service):
        # Check if it's a class and a dataclass
        if inspect.isclass(obj) and is_dataclass(obj):
            logger.debug(f"Found dataclass: {name}")
            dataclasses.append(obj)

    logger.info(
        f"Found {len(dataclasses)} dataclasses in {service.__name__}: "
        f"{[dc.__name__ for dc in dataclasses]}"
    )

    if not dataclasses:
        logger.warning(f"No dataclasses found in service: {service.__name__}")

    return dataclasses


def get_schema_from_data_class(service: Any, dataclass_type: Type) -> Dict[str, Any]:
    """
    Generate an OpenAPI schema from a dataclass.

    Args:
        service: The service module containing the dataclass
        dataclass_type: The dataclass type to convert to a schema

    Returns:
        Dictionary containing OpenAPI schema with structure:
        {
            "DataClassName": {
                "type": "object",
                "properties": {
                    "property_name": {
                        "description": "...",
                        "type": "...",
                        "enum": [...] (if applicable)
                    }
                },
                "required": [...]
            }
        }
    """
    logger.info(f"Generating schema for dataclass: {dataclass_type.__name__}")

    if not is_dataclass(dataclass_type):
        logger.error(f"{dataclass_type.__name__} is not a dataclass")
        raise ValueError(f"{dataclass_type.__name__} is not a dataclass")

    # Get all fields from the dataclass
    dataclass_fields = fields(dataclass_type)

    logger.debug(
        f"Processing {len(dataclass_fields)} fields in {dataclass_type.__name__}"
    )

    properties = {}
    required_fields = []

    for field in dataclass_fields:
        field_name = field.name
        field_type = field.type
        field_metadata = field.metadata

        logger.debug(
            f"Processing field: {field_name} (type: {field_type}, "
            f"default: {field.default}, default_factory: {field.default_factory})"
        )

        # Extract description from docstring (field metadata or class docstring)
        # In Databricks SDK, descriptions are in the class docstring as comments above fields
        description = _extract_field_description(dataclass_type, field_name)

        if description:
            logger.debug(f"Found description for {field_name}: {description[:50]}...")
        else:
            logger.debug(f"No description found for {field_name}")

        # Convert Python type to OpenAPI type
        openapi_type_info = python_type_to_openapi_type(field_type)

        # Build property schema
        property_schema = {}

        if description:
            property_schema["description"] = flatten_description(description)

        # Merge type information
        property_schema.update(openapi_type_info)

        properties[field_name] = property_schema

        # Determine if field is required (not Optional and no default value)
        is_optional = _is_optional_field(field)

        if not is_optional:
            logger.debug(f"Field {field_name} is required")
            required_fields.append(field_name)
        else:
            logger.debug(f"Field {field_name} is optional")

    # Build the final schema
    schema = {
        dataclass_type.__name__: {
            "type": "object",
            "properties": properties if properties else {},
        }
    }

    # Only add required if there are required fields
    if required_fields:
        schema[dataclass_type.__name__]["required"] = required_fields
        logger.info(
            f"Schema for {dataclass_type.__name__}: {len(properties)} properties, "
            f"{len(required_fields)} required"
        )
    else:
        logger.info(
            f"Schema for {dataclass_type.__name__}: {len(properties)} properties, "
            f"0 required (all optional)"
        )

    # Log if no properties found
    if not properties:
        logger.warning(
            f"Dataclass {dataclass_type.__name__} has no properties (empty dataclass)"
        )

    return schema


def _extract_field_description(dataclass_type: Type, field_name: str) -> str:
    """
    Extract field description from dataclass source code or docstring.

    In the Databricks SDK, field descriptions are stored as docstring comments
    immediately following the field declaration.

    Args:
        dataclass_type: The dataclass type
        field_name: The field name to extract description for

    Returns:
        The description string, or empty string if not found
    """
    try:
        # Get the source code of the class
        source = inspect.getsource(dataclass_type)

        # Look for the field name followed by a docstring
        lines = source.split("\n")

        for i, line in enumerate(lines):
            # Check if this line contains the field definition
            if f"{field_name}:" in line or f"{field_name} =" in line:
                # Check the next line for a docstring
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()

                    # Check for docstring patterns: """...""" or '''...'''
                    if next_line.startswith('"""') or next_line.startswith("'''"):
                        quote = '"""' if next_line.startswith('"""') else "'''"

                        # Single line docstring
                        if next_line.endswith(quote) and len(next_line) > 6:
                            return next_line[3:-3].strip()

                        # Multi-line docstring
                        docstring_lines = [next_line[3:]]
                        for j in range(i + 2, len(lines)):
                            if lines[j].strip().endswith(quote):
                                docstring_lines.append(
                                    lines[j].strip()[: -len(quote)]
                                )
                                break
                            docstring_lines.append(lines[j].strip())

                        return " ".join(docstring_lines).strip()

        logger.debug(
            f"No description found for field {field_name} in {dataclass_type.__name__}"
        )
        return ""

    except (OSError, TypeError) as e:
        logger.warning(
            f"Could not extract description for {field_name} in "
            f"{dataclass_type.__name__}: {e}"
        )
        return ""


def _is_optional_field(field: Any) -> bool:
    """
    Determine if a dataclass field is optional.

    A field is considered optional if:
    1. It has a default value (including None)
    2. It has a default_factory
    3. Its type annotation includes Optional or Union with None

    Args:
        field: The dataclass field

    Returns:
        True if the field is optional, False otherwise
    """
    from dataclasses import MISSING
    from typing import Union, get_args, get_origin

    # Check if it has a default value or factory
    has_default = field.default is not MISSING or field.default_factory is not MISSING

    # Check if the type is Optional (Union[X, None])
    origin = get_origin(field.type)
    args = get_args(field.type)

    is_union_with_none = origin is Union and type(None) in args

    return has_default or is_union_with_none

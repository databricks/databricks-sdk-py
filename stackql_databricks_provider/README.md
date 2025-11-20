# StackQL Databricks Provider - OpenAPI Schema Generator

A library of modular, testable functions to parse the Databricks Python SDK and extract components for generating OpenAPI specifications.

## Features

- **Small, modular functions** - Each function has a single, well-defined responsibility
- **Comprehensive logging** - Detailed logging at INFO and DEBUG levels to track anomalies
- **Type-safe** - Full type hints throughout
- **Well-tested** - Unit tests for all core functionality
- **Incremental design** - Built to be extended without creating a monolith

## Installation

Add the package to your Python path:

```bash
export PYTHONPATH="/path/to/stackql-provider-databricks:$PYTHONPATH"
```

## Usage

### 1. Extract Dataclasses from a Service

```python
from databricks.sdk.service import iam
from stackql_databricks_provider import get_data_classes

# Get all dataclasses from the IAM service
dataclasses = get_data_classes(iam)
print(f"Found {len(dataclasses)} dataclasses")
print([dc.__name__ for dc in dataclasses])
```

### 2. Generate OpenAPI Schema from a Dataclass

```python
from databricks.sdk.service.iam import AccessControlRequest
from stackql_databricks_provider import get_schema_from_data_class

# Generate OpenAPI schema
schema = get_schema_from_data_class(iam, AccessControlRequest)

# Output:
# {
#   "AccessControlRequest": {
#     "type": "object",
#     "properties": {
#       "group_name": {
#         "description": "name of the group",
#         "type": "string"
#       },
#       "permission_level": {
#         "type": "string",
#         "enum": ["CAN_EDIT", "CAN_MANAGE", ...]
#       },
#       ...
#     },
#     "required": []  // All fields are optional in this case
#   }
# }
```

## API Reference

### `get_data_classes(service) -> List[Type]`

Extracts all dataclass types from a service module.

**Parameters:**
- `service`: A service module (e.g., `databricks.sdk.service.compute`)

**Returns:**
- List of dataclass types found in the module

**Example:**
```python
from databricks.sdk.service import compute
dataclasses = get_data_classes(compute)
```

### `get_schema_from_data_class(service, dataclass_type) -> Dict[str, Any]`

Generates an OpenAPI schema from a dataclass.

**Parameters:**
- `service`: The service module containing the dataclass
- `dataclass_type`: The dataclass type to convert

**Returns:**
- Dictionary containing OpenAPI schema with structure:
```python
{
  "DataClassName": {
    "type": "object",
    "properties": {
      "property_name": {
        "description": "...",  # Flattened to one line
        "type": "...",         # OpenAPI type
        "enum": [...]          # If property is an enum
      }
    },
    "required": [...]  # List of non-optional properties
  }
}
```

**Features:**
- Converts Python types to OpenAPI types (str → string, int → integer, etc.)
- Extracts enum values and includes them in the schema
- Identifies required vs optional fields
- Flattens multi-line descriptions to single lines
- Returns empty dict for properties if dataclass has no fields
- Handles nested types (List, Dict, Optional)

## Type Conversion

The library automatically converts Python types to OpenAPI types:

| Python Type | OpenAPI Type |
|-------------|--------------|
| `str` | `{"type": "string"}` |
| `int` | `{"type": "integer", "format": "int64"}` |
| `float` | `{"type": "number", "format": "double"}` |
| `bool` | `{"type": "boolean"}` |
| `List[T]` | `{"type": "array", "items": {...}}` |
| `Dict[str, T]` | `{"type": "object", "additionalProperties": {...}}` |
| `Enum` | `{"type": "string", "enum": [...]}` |
| `Optional[T]` | Same as `T` (optionality tracked via "required" field) |

## Logging

The library uses Python's `logging` module extensively:

```python
import logging

# Enable INFO logging to see high-level operations
logging.basicConfig(level=logging.INFO)

# Enable DEBUG logging to see detailed parsing information
logging.basicConfig(level=logging.DEBUG)
```

**Logged information includes:**
- Number of dataclasses found
- Field processing details
- Type conversion decisions
- Enum value extraction
- Warnings about anomalies (empty dataclasses, unknown types, etc.)

## Running Tests

### Unit Tests

```bash
# Run all tests
python -m unittest discover stackql_databricks_provider/tests -v

# Run specific test modules
python -m unittest stackql_databricks_provider.tests.test_parser -v
python -m unittest stackql_databricks_provider.tests.test_type_converters -v
```

### Demo Script

```bash
PYTHONPATH=/path/to/stackql-provider-databricks python stackql_databricks_provider/demo.py
```

## Project Structure

```
stackql_databricks_provider/
├── __init__.py              # Package exports
├── parser.py                # Main parsing functions
├── type_converters.py       # Type conversion utilities
├── demo.py                  # Demo script
├── README.md                # This file
└── tests/
    ├── __init__.py
    ├── test_parser.py       # Parser function tests
    ├── test_type_converters.py  # Type converter tests
    └── test_real_sdk.py     # Integration tests with real SDK
```

## Design Principles

1. **Modularity** - Each function has a single responsibility
2. **Testability** - All functions are easily testable with mock data
3. **Incrementality** - New functions can be added without modifying existing ones
4. **Observability** - Comprehensive logging at every step
5. **Type Safety** - Full type hints for better IDE support and error catching

## Future Extensions

This library is designed to be extended incrementally. Potential additions:

- `get_methods(service, api_class)` - Extract methods from API classes
- `get_method_signature(method)` - Extract method parameters and return types
- `generate_openapi_path(method)` - Generate OpenAPI path specifications
- `get_service_modules()` - List all available service modules
- And more...

Each extension should be:
- A small, focused function
- Thoroughly logged
- Well-tested
- Independent of other extensions

## License

This code is part of the StackQL Databricks Provider project.

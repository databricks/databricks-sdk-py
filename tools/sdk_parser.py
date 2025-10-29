"""
Parser for Databricks SDK service modules to extract schema and API information.
"""

import ast
import inspect
from dataclasses import fields as dataclass_fields
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, get_args, get_origin
import importlib
import sys


class SDKParser:
    """Parses SDK service modules to extract models and API operations."""

    def __init__(self, service_module):
        """Initialize parser with a service module.

        Args:
            service_module: The imported service module
        """
        self.module = service_module
        self.schemas = {}
        self.api_classes = {}

    def parse(self) -> Dict[str, Any]:
        """Parse the module and extract all relevant information.

        Returns:
            Dict containing schemas and API operations
        """
        # Extract all dataclasses and enums
        for name, obj in inspect.getmembers(self.module):
            if inspect.isclass(obj) and hasattr(obj, '__dataclass_fields__'):
                self.schemas[name] = self._parse_dataclass(obj)
            elif inspect.isclass(obj) and issubclass(obj, Enum) and obj != Enum:
                self.schemas[name] = self._parse_enum(obj)
            elif inspect.isclass(obj) and name.endswith('API') and not name.startswith('_'):
                self.api_classes[name] = self._parse_api_class(obj)

        return {
            'schemas': self.schemas,
            'api_classes': self.api_classes
        }

    def _parse_dataclass(self, cls) -> Dict[str, Any]:
        """Parse a dataclass to extract field information.

        Args:
            cls: The dataclass to parse

        Returns:
            Dict with schema information
        """
        schema = {
            'type': 'dataclass',
            'description': inspect.getdoc(cls) or '',
            'properties': {},
            'required': []
        }

        for field in dataclass_fields(cls):
            field_info = self._parse_field_type(field.type)
            field_info['description'] = self._extract_field_doc(cls, field.name)

            # Check if field is required (not Optional and no default)
            is_optional = self._is_optional_type(field.type)
            has_default = field.default is not field.default_factory if hasattr(field, 'default_factory') else field.default is not None

            if not is_optional and field.default is inspect.Parameter.empty:
                # Only mark as required if it's truly non-optional
                # But per requirements, we'll make everything optional anyway
                pass

            schema['properties'][field.name] = field_info

        return schema

    def _parse_enum(self, enum_cls) -> Dict[str, Any]:
        """Parse an Enum class.

        Args:
            enum_cls: The Enum class to parse

        Returns:
            Dict with enum information
        """
        return {
            'type': 'enum',
            'description': inspect.getdoc(enum_cls) or '',
            'values': [member.value for member in enum_cls]
        }

    def _parse_api_class(self, api_cls) -> Dict[str, Any]:
        """Parse an API class to extract operations.

        Args:
            api_cls: The API class to parse

        Returns:
            Dict with API operations
        """
        api_info = {
            'description': inspect.getdoc(api_cls) or '',
            'operations': {}
        }

        for name, method in inspect.getmembers(api_cls, predicate=inspect.isfunction):
            if name.startswith('_') or name == '__init__':
                continue

            # Skip wait methods and iterator helpers
            if 'wait' in name.lower() or name.endswith('_and_wait'):
                continue

            operation = self._parse_api_method(method, api_cls)
            if operation:
                api_info['operations'][name] = operation

        return api_info

    def _parse_api_method(self, method, api_cls) -> Optional[Dict[str, Any]]:
        """Parse an API method to extract operation details.

        Args:
            method: The method to parse
            api_cls: The parent API class

        Returns:
            Dict with operation details or None
        """
        doc = inspect.getdoc(method) or ''
        sig = inspect.signature(method)

        # Extract HTTP method and path from the method implementation
        source = inspect.getsource(method)
        http_info = self._extract_http_info_from_source(source)

        if not http_info:
            return None

        operation = {
            'description': doc.split('\n\n')[0] if doc else '',
            'full_description': doc,
            'http_method': http_info['method'],
            'path': http_info['path'],
            'parameters': [],
            'request_body': None,
            'response': None
        }

        # Get type hints to resolve string annotations
        try:
            from typing import get_type_hints
            type_hints = get_type_hints(method)
        except Exception:
            type_hints = {}

        # Parse parameters
        for param_name, param in sig.parameters.items():
            if param_name in ('self', 'timeout'):
                continue

            # Use type hint if available, otherwise use annotation
            param_type = type_hints.get(param_name, param.annotation)
            param_info = self._parse_parameter(param_name, param, doc, param_type)
            if param_info:
                operation['parameters'].append(param_info)

        # Extract return type
        return_type = type_hints.get('return', sig.return_annotation)
        if return_type != inspect.Signature.empty:
            operation['response'] = self._parse_return_type(return_type)

        return operation

    def _extract_http_info_from_source(self, source: str) -> Optional[Dict[str, Any]]:
        """Extract HTTP method and path from method source code.

        Args:
            source: The source code of the method

        Returns:
            Dict with HTTP method and path, or None
        """
        # Look for self._api.do() calls
        lines = source.split('\n')
        for line in lines:
            if 'self._api.do(' in line:
                # Extract method and path
                parts = line.split('self._api.do(')
                if len(parts) > 1:
                    args = parts[1].split(',', 2)
                    if len(args) >= 2:
                        method = args[0].strip().strip('"\'')
                        path = args[1].strip()

                        # Handle f-strings in path
                        if path.startswith('f"') or path.startswith("f'"):
                            path = self._convert_fstring_to_openapi_path(path)
                        else:
                            # Remove quotes from regular string
                            path = path.strip('"\'')

                        return {
                            'method': method,
                            'path': path
                        }

        return None

    def _convert_fstring_to_openapi_path(self, fstring: str) -> str:
        """Convert Python f-string to OpenAPI path parameter format.

        Args:
            fstring: The f-string path

        Returns:
            OpenAPI formatted path
        """
        import re
        # Remove f" or f' prefix and trailing quote
        path = fstring[2:-1]
        # Convert {variable} to {variable} (already in right format)
        # But need to handle nested expressions like {escape(var)}
        # Extract variable names from expressions
        def clean_param(match):
            content = match.group(1)
            # Handle function calls like escape(var) or _escape_multi_segment_path_parameter(var)
            if '(' in content:
                # Extract the variable name from function call
                var = content.split('(')[1].split(')')[0].strip()
                # Handle self.var or just var
                if '.' in var:
                    var = var.split('.')[-1]
                return '{' + var + '}'
            else:
                # Handle self.var or just var
                if '.' in content:
                    var = content.split('.')[-1]
                else:
                    var = content
                return '{' + var + '}'

        path = re.sub(r'\{([^}]+)\}', clean_param, path)
        return path

    def _parse_parameter(self, name: str, param: inspect.Parameter, doc: str, param_type=None) -> Optional[Dict[str, Any]]:
        """Parse a method parameter.

        Args:
            name: Parameter name
            param: Parameter object
            doc: Method docstring
            param_type: Resolved parameter type (from get_type_hints)

        Returns:
            Dict with parameter info
        """
        param_info = {
            'name': name,
            'required': param.default == inspect.Parameter.empty,
            'description': self._extract_param_doc(doc, name)
        }

        # Use provided type or fall back to annotation
        type_to_parse = param_type if param_type is not None else param.annotation

        if type_to_parse != inspect.Parameter.empty:
            type_info = self._parse_field_type(type_to_parse)
            param_info.update(type_info)

        return param_info

    def _parse_field_type(self, type_hint) -> Dict[str, Any]:
        """Parse a type hint to extract type information.

        Args:
            type_hint: The type hint to parse

        Returns:
            Dict with type information
        """
        origin = get_origin(type_hint)
        args = get_args(type_hint)

        # Handle Optional types (Union[X, None])
        if origin is not None:
            # Check if this is Union (which is how Optional is represented)
            import typing
            if hasattr(typing, 'Union') and origin is typing.Union:
                # Filter out None type and get the actual type
                non_none_args = [arg for arg in args if arg is not type(None)]
                if len(non_none_args) == 1:
                    return self._parse_field_type(non_none_args[0])

        # Handle List types
        if origin is list or origin is List:
            if args:
                item_type = self._parse_field_type(args[0])
                return {
                    'type': 'array',
                    'items': item_type
                }
            return {'type': 'array', 'items': {'type': 'string'}}

        # Handle Dict types
        if origin is dict or origin is Dict:
            return {
                'type': 'object',
                'additionalProperties': True
            }

        # Handle basic types
        if type_hint == str:
            return {'type': 'string'}
        elif type_hint == int:
            return {'type': 'integer'}
        elif type_hint == float:
            return {'type': 'number'}
        elif type_hint == bool:
            return {'type': 'boolean'}
        elif type_hint == Any:
            return {'type': 'object'}

        # Handle custom types (dataclasses, enums)
        if hasattr(type_hint, '__name__'):
            type_name = type_hint.__name__

            # Check if it's an enum
            if inspect.isclass(type_hint) and issubclass(type_hint, Enum):
                return {
                    'type': 'string',
                    'enum': [member.value for member in type_hint]
                }

            # Reference to another schema
            return {'$ref': f'#/components/schemas/{type_name}'}

        return {'type': 'string'}  # Default fallback

    def _parse_return_type(self, return_type) -> Dict[str, Any]:
        """Parse return type annotation.

        Args:
            return_type: The return type annotation

        Returns:
            Dict with return type info
        """
        # Handle Iterator types
        origin = get_origin(return_type)
        if origin is not None:
            args = get_args(return_type)
            if args:
                return self._parse_field_type(args[0])

        return self._parse_field_type(return_type)

    def _is_optional_type(self, type_hint) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: The type hint to check

        Returns:
            True if Optional, False otherwise
        """
        origin = get_origin(type_hint)
        args = get_args(type_hint)

        # Check if it's Optional (Union with None)
        if origin is Optional:
            return True

        # Check for Union[X, None]
        if hasattr(type_hint, '__origin__'):
            if str(type_hint).startswith('typing.Union'):
                return type(None) in args

        return False

    def _extract_field_doc(self, cls, field_name: str) -> str:
        """Extract documentation for a field from the source code.

        Args:
            cls: The class containing the field
            field_name: The name of the field

        Returns:
            The field documentation or empty string
        """
        try:
            source = inspect.getsource(cls)
            tree = ast.parse(source)

            for node in ast.walk(tree):
                if isinstance(node, ast.AnnAssign):
                    if hasattr(node.target, 'id') and node.target.id == field_name:
                        # Look for string literal following the assignment
                        # Check the parent to find subsequent string literals
                        pass

            # Alternative: check the actual field object for docstring
            field_obj = getattr(cls, field_name, None)
            for field in dataclass_fields(cls):
                if field.name == field_name:
                    # Look at metadata or default
                    if hasattr(field, 'metadata') and 'description' in field.metadata:
                        return field.metadata['description']

            # Parse source more carefully for inline comments
            lines = source.split('\n')
            for i, line in enumerate(lines):
                if f'{field_name}:' in line or f'{field_name} =' in line:
                    # Look for triple-quoted string on next lines
                    j = i + 1
                    doc_lines = []
                    while j < len(lines):
                        next_line = lines[j].strip()
                        if next_line.startswith('"""') or next_line.startswith("'''"):
                            # Start of docstring
                            doc_lines.append(next_line.strip('"\' '))
                            j += 1
                            while j < len(lines):
                                doc_line = lines[j].strip()
                                if doc_line.endswith('"""') or doc_line.endswith("'''"):
                                    doc_lines.append(doc_line.strip('"\' '))
                                    return ' '.join(doc_lines).strip()
                                doc_lines.append(doc_line)
                                j += 1
                            break
                        elif next_line and not next_line.startswith('#'):
                            break
                        j += 1
        except:
            pass

        return ''

    def _extract_param_doc(self, doc: str, param_name: str) -> str:
        """Extract parameter documentation from docstring.

        Args:
            doc: The full docstring
            param_name: The parameter name

        Returns:
            The parameter documentation
        """
        lines = doc.split('\n')
        for i, line in enumerate(lines):
            if f':param {param_name}:' in line:
                desc = line.split(f':param {param_name}:')[1].strip()
                # Check if description continues on next lines
                j = i + 1
                while j < len(lines):
                    next_line = lines[j].strip()
                    if next_line.startswith(':'):
                        break
                    if next_line:
                        desc += ' ' + next_line
                    j += 1
                return desc

        return ''

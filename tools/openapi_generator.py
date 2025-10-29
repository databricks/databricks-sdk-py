"""
OpenAPI specification generator from parsed SDK information.
"""

from typing import Any, Dict, List, Optional
import yaml
import re


class OpenAPIGenerator:
    """Generates OpenAPI 3.0 specifications from parsed SDK data."""

    def __init__(self, service_name: str, parsed_data: Dict[str, Any], module_doc: str = ''):
        """Initialize the generator.

        Args:
            service_name: Name of the service
            parsed_data: Parsed SDK data from SDKParser
            module_doc: Module-level documentation
        """
        self.service_name = service_name
        self.parsed_data = parsed_data
        self.module_doc = module_doc
        self.spec = self._init_spec()

    def _init_spec(self) -> Dict[str, Any]:
        """Initialize the OpenAPI specification structure.

        Returns:
            Initial OpenAPI spec dict
        """
        # Determine if this is account-level or workspace-level API
        is_account_api = self._is_account_level_api()

        servers = []
        if is_account_api:
            servers.append({
                'url': 'https://accounts.cloud.databricks.com',
                'description': 'Databricks Account API',
                'variables': {
                    'account_id': {
                        'default': 'your-account-id',
                        'description': 'Databricks account ID'
                    }
                }
            })
        else:
            servers.append({
                'url': 'https://{deployment_name}.cloud.databricks.com',
                'description': 'Databricks Workspace API',
                'variables': {
                    'deployment_name': {
                        'default': 'your-deployment',
                        'description': 'Databricks workspace deployment name'
                    }
                }
            })

        return {
            'openapi': '3.0.0',
            'info': {
                'title': f'Databricks {self.service_name.title()} API',
                'description': self.module_doc or f'API for Databricks {self.service_name} service',
                'version': '1.0.0',
                'contact': {
                    'name': 'Databricks',
                    'url': 'https://databricks.com'
                }
            },
            'servers': servers,
            'paths': {},
            'components': {
                'schemas': {},
                'securitySchemes': {
                    'bearerAuth': {
                        'type': 'http',
                        'scheme': 'bearer',
                        'bearerFormat': 'JWT',
                        'description': 'Databricks personal access token'
                    }
                }
            },
            'security': [
                {'bearerAuth': []}
            ]
        }

    def _is_account_level_api(self) -> bool:
        """Determine if this is an account-level API.

        Returns:
            True if account-level, False if workspace-level
        """
        # Check for account-level indicators
        account_indicators = ['account', 'billing', 'provisioning', 'oauth2']

        service_lower = self.service_name.lower()
        if any(indicator in service_lower for indicator in account_indicators):
            return True

        # Check API paths
        for api_name, api_data in self.parsed_data.get('api_classes', {}).items():
            for op_name, op_data in api_data.get('operations', {}).items():
                path = op_data.get('path', '')
                if '/api/2.0/accounts/' in path:
                    return True

        return False

    def generate(self) -> Dict[str, Any]:
        """Generate the complete OpenAPI specification.

        Returns:
            Complete OpenAPI spec dict
        """
        # Generate schemas
        self._generate_schemas()

        # Generate paths
        self._generate_paths()

        return self.spec

    def _generate_schemas(self):
        """Generate component schemas from parsed data."""
        for schema_name, schema_data in self.parsed_data.get('schemas', {}).items():
            if schema_data['type'] == 'enum':
                self.spec['components']['schemas'][schema_name] = {
                    'type': 'string',
                    'description': schema_data.get('description', ''),
                    'enum': schema_data['values']
                }
            elif schema_data['type'] == 'dataclass':
                self.spec['components']['schemas'][schema_name] = self._generate_object_schema(
                    schema_name, schema_data
                )

    def _generate_object_schema(self, name: str, schema_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate an object schema from dataclass information.

        Args:
            name: Schema name
            schema_data: Parsed schema data

        Returns:
            OpenAPI schema dict
        """
        schema = {
            'type': 'object',
            'description': schema_data.get('description', ''),
            'properties': {}
        }

        # Per requirements: make all properties optional (no required array)
        # This avoids polymorphism issues with cloud-specific fields

        for prop_name, prop_data in schema_data.get('properties', {}).items():
            prop_schema = self._convert_type_to_schema(prop_data)

            # Add description if available
            if 'description' in prop_data and prop_data['description']:
                prop_schema['description'] = prop_data['description']

            schema['properties'][prop_name] = prop_schema

        return schema

    def _convert_type_to_schema(self, type_data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert parsed type data to OpenAPI schema.

        Args:
            type_data: Parsed type information

        Returns:
            OpenAPI schema dict
        """
        schema = {}

        # Handle $ref
        if '$ref' in type_data:
            return {'$ref': type_data['$ref']}

        # Handle type
        if 'type' in type_data:
            schema['type'] = type_data['type']

        # Handle enum
        if 'enum' in type_data:
            schema['enum'] = type_data['enum']

        # Handle array items
        if 'items' in type_data:
            schema['items'] = self._convert_type_to_schema(type_data['items'])

        # Handle additionalProperties
        if 'additionalProperties' in type_data:
            schema['additionalProperties'] = type_data['additionalProperties']

        # Handle description
        if 'description' in type_data:
            schema['description'] = type_data['description']

        return schema

    def _generate_paths(self):
        """Generate API paths from parsed API classes."""
        for api_name, api_data in self.parsed_data.get('api_classes', {}).items():
            for op_name, op_data in api_data.get('operations', {}).items():
                path = op_data.get('path', '')
                if not path:
                    continue

                # Normalize path parameters
                path = self._normalize_path(path)

                # Initialize path if not exists
                if path not in self.spec['paths']:
                    self.spec['paths'][path] = {}

                # Get HTTP method
                http_method = op_data.get('http_method', '').lower()
                if not http_method:
                    continue

                # Generate operation
                operation = self._generate_operation(op_name, op_data, api_data)
                self.spec['paths'][path][http_method] = operation

    def _normalize_path(self, path: str) -> str:
        """Normalize path to OpenAPI format.

        Args:
            path: Raw path string

        Returns:
            Normalized path
        """
        # Ensure path parameters are in {param} format
        # Handle escape function calls
        path = re.sub(r'\{[^}]*escape[^}]*\(([^)]+)\)[^}]*\}', r'{\1}', path)
        path = re.sub(r'\{([^}]+)\}', lambda m: '{' + m.group(1).split('.')[-1].split('/')[-1] + '}', path)

        return path

    def _generate_operation(
        self, op_name: str, op_data: Dict[str, Any], api_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate an OpenAPI operation.

        Args:
            op_name: Operation name
            op_data: Operation data
            api_data: Parent API data

        Returns:
            OpenAPI operation dict
        """
        operation = {
            'operationId': op_name,
            'summary': op_data.get('description', op_name),
            'description': op_data.get('full_description', op_data.get('description', '')),
            'tags': [self.service_name]
        }

        # Add parameters
        parameters = []
        request_body_params = []

        for param in op_data.get('parameters', []):
            param_schema = self._generate_parameter(param, op_data)
            if param_schema:
                # Determine if it's a path, query, or body parameter
                if '{' + param['name'] + '}' in op_data.get('path', ''):
                    param_schema['in'] = 'path'
                    param_schema['required'] = True
                    parameters.append(param_schema)
                elif op_data.get('http_method', '').upper() in ('GET', 'DELETE'):
                    param_schema['in'] = 'query'
                    parameters.append(param_schema)
                else:
                    # Body parameter
                    request_body_params.append(param)

        if parameters:
            operation['parameters'] = parameters

        # Add request body for POST, PUT, PATCH
        if op_data.get('http_method', '').upper() in ('POST', 'PUT', 'PATCH') and request_body_params:
            operation['requestBody'] = self._generate_request_body(request_body_params)

        # Add response
        response_type = op_data.get('response')
        if response_type:
            operation['responses'] = self._generate_responses(response_type)
        else:
            operation['responses'] = {
                '200': {
                    'description': 'Success'
                }
            }

        return operation

    def _generate_parameter(self, param: Dict[str, Any], op_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate an OpenAPI parameter.

        Args:
            param: Parameter data
            op_data: Operation data

        Returns:
            OpenAPI parameter dict or None
        """
        param_schema = {
            'name': param['name'],
            'description': param.get('description', ''),
            'required': param.get('required', False),
            'schema': {}
        }

        # Get type info - don't include description in schema if $ref is used
        type_schema = self._convert_type_to_schema(param) if 'type' in param or '$ref' in param else {'type': 'string'}

        # Don't duplicate description in schema if it has a $ref
        if '$ref' in type_schema:
            param_schema['schema'] = type_schema
        else:
            param_schema['schema'] = type_schema
            # Remove duplicate description from schema
            if 'description' in param_schema['schema']:
                del param_schema['schema']['description']

        return param_schema

    def _generate_request_body(self, params: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate request body from parameters.

        Args:
            params: List of body parameters

        Returns:
            OpenAPI requestBody dict
        """
        # If there's only one parameter and it's a reference, use it directly
        if len(params) == 1 and '$ref' in params[0]:
            return {
                'required': True,
                'content': {
                    'application/json': {
                        'schema': self._convert_type_to_schema(params[0])
                    }
                }
            }

        # Otherwise, create an object with properties
        properties = {}
        for param in params:
            prop_schema = self._convert_type_to_schema(param)
            # Only add description if it's not a $ref
            if '$ref' not in prop_schema and 'description' in param:
                prop_schema['description'] = param['description']
            properties[param['name']] = prop_schema

        return {
            'required': True,
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': properties
                    }
                }
            }
        }

    def _generate_responses(self, response_type: Dict[str, Any]) -> Dict[str, Any]:
        """Generate response definitions.

        Args:
            response_type: Parsed response type info

        Returns:
            OpenAPI responses dict
        """
        responses = {
            '200': {
                'description': 'Successful response',
                'content': {
                    'application/json': {
                        'schema': self._convert_type_to_schema(response_type)
                    }
                }
            },
            '400': {
                'description': 'Bad request'
            },
            '401': {
                'description': 'Unauthorized'
            },
            '404': {
                'description': 'Not found'
            },
            '500': {
                'description': 'Internal server error'
            }
        }

        return responses

    def to_yaml(self) -> str:
        """Convert the specification to YAML format.

        Returns:
            YAML string
        """
        return yaml.dump(self.spec, sort_keys=False, default_flow_style=False, allow_unicode=True)

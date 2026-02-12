"""
Core extraction functions for parsing Databricks SDK service modules.

Each function has a single, well-defined responsibility and returns
typed, predictable results suitable for OpenAPI spec generation.
"""

import dataclasses
import inspect
import logging
import re
import textwrap
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Type

logger = logging.getLogger(__name__)


def get_resources(service_module) -> List[Tuple[str, str]]:
    """Extract API resource classes from a service module.

    Scans the module for classes whose names end with 'API' and returns
    a list of (class_name, snake_case_resource_name) tuples.

    Args:
        service_module: A ``databricks.sdk.service.*`` module.

    Returns:
        List of ``(class_name, resource_snake_name)`` tuples, sorted by
        class name.
    """
    resources = []
    for name, obj in inspect.getmembers(service_module, inspect.isclass):
        if name.endswith("API") and not name.startswith("_"):
            snake = _class_name_to_snake(name)
            resources.append((name, snake))
            logger.debug("Found resource: %s -> %s", name, snake)
    resources.sort(key=lambda x: x[0])
    logger.info("Extracted %d resources from %s", len(resources), getattr(service_module, "__name__", "?"))
    return resources


def get_operations(service_module, class_name: str) -> List[str]:
    """Extract public method names from an API class.

    Args:
        service_module: A ``databricks.sdk.service.*`` module.
        class_name: Name of the API class (e.g. ``"ClustersAPI"``).

    Returns:
        Sorted list of public method names.
    """
    cls = getattr(service_module, class_name, None)
    if cls is None:
        logger.warning("Class %s not found in module", class_name)
        return []
    operations = []
    for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
        if name.startswith("_"):
            continue
        operations.append(name)
    operations.sort()
    logger.info("Extracted %d operations from %s", len(operations), class_name)
    return operations


def get_operation_details(
    service_module,
    class_name: str,
    method_name: str,
    *,
    service_name: str = "",
    resource_snake_name: str = "",
) -> Dict[str, Any]:
    """Extract OpenAPI path object for a single API method.

    Inspects the method source to find the HTTP method and path from
    ``self._api.do(...)`` calls, then builds an OpenAPI-style path item.

    Args:
        service_module: A ``databricks.sdk.service.*`` module.
        class_name: Name of the API class.
        method_name: Name of the method.
        service_name: Service name for tags.
        resource_snake_name: Snake-case resource name for tags.

    Returns:
        Dict mapping URL path to method details, e.g.::

            {"/api/2.0/clusters/{cluster_id}": {"get": {...}}}
    """
    cls = getattr(service_module, class_name, None)
    if cls is None:
        raise ValueError(f"Class {class_name} not found")
    method = getattr(cls, method_name, None)
    if method is None:
        raise ValueError(f"Method {method_name} not found on {class_name}")

    source = _get_source_safe(method)
    if source is None:
        raise ValueError(f"Could not read source for {class_name}.{method_name}")

    http_method, url_path = _extract_http_call(source)
    if http_method is None or url_path is None:
        raise ValueError(f"No self._api.do() call found in {class_name}.{method_name}")

    sig = inspect.signature(method)
    docstring = inspect.getdoc(method) or ""

    path_params = _extract_path_params(url_path)
    body_params, query_params, positional_params = _classify_params(
        sig, path_params, http_method, source
    )

    tags = _build_tags(service_name, resource_snake_name)
    summary = _extract_summary(docstring)

    # Build a unique operationId: resource_snake_name + method_name
    if resource_snake_name:
        operation_id = f"{resource_snake_name}_{method_name}"
    else:
        operation_id = method_name

    operation: Dict[str, Any] = {
        "operationId": operation_id,
        "summary": summary,
        "tags": tags,
        "description": docstring,
    }

    parameters = _build_parameters(path_params, query_params, sig, docstring)
    if parameters:
        operation["parameters"] = parameters

    if body_params:
        operation["requestBody"] = _build_request_body(body_params, sig, docstring)

    return_type = _get_return_type(method)
    # For Iterator methods, use the list response wrapper schema instead
    # of the individual item type, since the HTTP response is the envelope.
    if _is_iterator_method(method) and return_type:
        list_response = _find_list_response_type(service_module, return_type)
        if list_response:
            logger.debug(
                "Iterator method %s.%s: using %s instead of %s",
                class_name, method_name, list_response, return_type,
            )
            return_type = list_response

    response_media_type = _detect_response_media_type(source)
    if response_media_type != "application/json":
        logger.info(
            "%s.%s: non-JSON response media type: %s",
            class_name, method_name, response_media_type,
        )
    operation["responses"] = _build_responses(return_type, response_media_type)

    openapi_path = _normalize_path(url_path)
    return {openapi_path: {http_method.lower(): operation}}


def get_data_classes(service_module) -> List[Type]:
    """Extract all dataclass types from a service module.

    Args:
        service_module: A ``databricks.sdk.service.*`` module.

    Returns:
        List of dataclass types sorted by name.
    """
    classes = []
    for name, obj in inspect.getmembers(service_module, inspect.isclass):
        if name.startswith("_"):
            continue
        if dataclasses.is_dataclass(obj) and obj.__module__ == service_module.__name__:
            classes.append(obj)
    classes.sort(key=lambda c: c.__name__)
    logger.info("Extracted %d dataclasses from %s", len(classes), getattr(service_module, "__name__", "?"))
    return classes


def get_enums(service_module) -> List[Type]:
    """Extract all Enum types from a service module.

    Args:
        service_module: A ``databricks.sdk.service.*`` module.

    Returns:
        List of Enum types sorted by name.
    """
    enums = []
    for name, obj in inspect.getmembers(service_module, inspect.isclass):
        if name.startswith("_"):
            continue
        if issubclass(obj, Enum) and obj is not Enum and obj.__module__ == service_module.__name__:
            enums.append(obj)
    enums.sort(key=lambda c: c.__name__)
    logger.info("Extracted %d enums from %s", len(enums), getattr(service_module, "__name__", "?"))
    return enums


def get_schema_from_data_class(service_module, dc: Type) -> Dict[str, Any]:
    """Generate an OpenAPI component schema from a dataclass.

    Uses the actual JSON wire field names (parsed from ``from_dict``) rather
    than the Python attribute names so the schema matches the HTTP response.

    Args:
        service_module: The service module (used to resolve type references).
        dc: A dataclass type.

    Returns:
        Dict mapping the class name to its OpenAPI schema, e.g.::

            {"CustomLlm": {"type": "object", "properties": {...}, ...}}
    """
    if not dataclasses.is_dataclass(dc):
        raise TypeError(f"{dc} is not a dataclass")

    json_mapping = _extract_json_field_mapping(dc)

    properties: Dict[str, Any] = {}
    required: List[str] = []
    field_docs = _extract_field_docs(dc)

    for field in dataclasses.fields(dc):
        prop = _field_to_property(field, service_module)
        # Add description from field docstring (inline string after the field)
        desc = field_docs.get(field.name)
        if desc:
            prop["description"] = desc
        # Use the JSON wire name (from from_dict) instead of the Python field name
        json_name = json_mapping.get(field.name, field.name)
        properties[json_name] = prop

        if _is_required_field(field):
            required.append(json_name)

    schema: Dict[str, Any] = {
        "type": "object",
        "properties": properties,
    }
    if required:
        schema["required"] = required

    # Get class docstring (not the auto-generated dataclass repr)
    doc = dc.__doc__
    if doc and not doc.startswith(dc.__name__ + "("):
        schema["description"] = doc

    return {dc.__name__: schema}


def get_schema_from_enum(enum_cls: Type) -> Dict[str, Any]:
    """Generate an OpenAPI component schema from an Enum class.

    Args:
        enum_cls: An Enum type.

    Returns:
        Dict mapping the enum name to its OpenAPI schema.
    """
    values = [e.value for e in enum_cls]
    schema: Dict[str, Any] = {
        "type": "string",
        "enum": values,
    }
    doc = inspect.getdoc(enum_cls)
    if doc:
        schema["description"] = doc
    return {enum_cls.__name__: schema}


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _class_name_to_snake(name: str) -> str:
    """Convert ``ClustersAPI`` to ``clusters``."""
    name = re.sub(r"API$", "", name)
    # Insert underscore before uppercase letters that follow lowercase
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    # Insert underscore between consecutive uppercase followed by lowercase
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return name.lower()


def _get_source_safe(method) -> Optional[str]:
    """Get source code, returning None on failure."""
    try:
        return inspect.getsource(method)
    except (OSError, TypeError):
        return None


def _extract_http_call(source: str) -> Tuple[Optional[str], Optional[str]]:
    """Parse ``self._api.do("METHOD", "path"...)`` from method source.

    Handles both plain strings and f-strings.
    """
    # Match: self._api.do("METHOD", f"..." or "...")
    pattern = r'self\._api\.do\(\s*"([A-Z]+)"\s*,\s*(?:f"([^"]+)"|"([^"]+)")'
    m = re.search(pattern, source)
    if m:
        http_method = m.group(1)
        url_path = m.group(2) or m.group(3)
        return http_method, url_path
    return None, None


def _extract_path_params(url_path: str) -> List[str]:
    """Extract ``{param}`` placeholders from a URL path.

    Handles both simple ``{id}`` and expression-based ``{some_expr}``
    placeholders.  Strips f-string expressions so only the clean
    parameter name remains.
    """
    # Find all {...} groups
    raw = re.findall(r"\{([^}]+)\}", url_path)
    params = []
    for r in raw:
        # Clean f-string expressions like {_escape_multi_segment_path_parameter(file_path)}
        clean = re.sub(r"_escape_multi_segment_path_parameter\((\w+)\)", r"\1", r)
        # Clean self._api.X expressions like {self._api.account_id} -> account_id
        clean = re.sub(r"self\._api\.(\w+)", r"\1", clean)
        params.append(clean)
    return params


def _classify_params(
    sig: inspect.Signature,
    path_params: List[str],
    http_method: str,
    source: str,
) -> Tuple[List[str], List[str], List[str]]:
    """Classify method parameters as body, query, or positional.

    Returns:
        (body_params, query_params, positional_params)
    """
    body_params: List[str] = []
    query_params: List[str] = []
    positional_params: List[str] = []

    has_body = "body = " in source or "body={" in source or "body[" in source
    has_query = "query = " in source or "query={" in source or "query[" in source

    for name, param in sig.parameters.items():
        if name in ("self", "headers"):
            continue
        if name in path_params:
            positional_params.append(name)
            continue

        if has_query and _param_in_dict(source, "query", name):
            query_params.append(name)
        elif has_body and _param_in_dict(source, "body", name):
            body_params.append(name)
        elif http_method in ("POST", "PUT", "PATCH") and has_body:
            body_params.append(name)
        elif http_method in ("GET", "DELETE", "HEAD") and has_query:
            query_params.append(name)
        else:
            # Fallback: body for write methods, query for read methods
            if http_method in ("POST", "PUT", "PATCH"):
                body_params.append(name)
            else:
                query_params.append(name)

    return body_params, query_params, positional_params


def _param_in_dict(source: str, dict_name: str, param_name: str) -> bool:
    """Check if a param is assigned into a named dict in source."""
    patterns = [
        rf'{dict_name}\["{param_name}"\]',
        rf'{dict_name}\["{param_name}"\]\s*=',
        rf'"{param_name}":\s*{param_name}',
    ]
    for p in patterns:
        if re.search(p, source):
            return True
    return False


def _build_tags(service_name: str, resource_snake_name: str) -> List[str]:
    tags = []
    if service_name:
        tags.append(service_name)
    if resource_snake_name and resource_snake_name != service_name:
        tags.append(resource_snake_name)
    return tags


def _extract_summary(docstring: str) -> str:
    """Extract first sentence from a docstring."""
    if not docstring:
        return ""
    first_line = docstring.split("\n")[0].strip()
    return first_line


def _build_parameters(
    path_params: List[str],
    query_params: List[str],
    sig: inspect.Signature,
    docstring: str,
) -> List[Dict[str, Any]]:
    """Build OpenAPI parameter objects for path and query params."""
    params = []
    param_docs = _parse_param_docs(docstring)

    for name in path_params:
        p: Dict[str, Any] = {
            "name": name,
            "in": "path",
            "required": True,
            "schema": _python_type_to_openapi(sig.parameters.get(name)),
        }
        desc = param_docs.get(name)
        if desc:
            p["description"] = desc
        params.append(p)

    for name in query_params:
        sig_param = sig.parameters.get(name)
        p = {
            "name": name,
            "in": "query",
            "required": _is_param_required(sig_param),
            "schema": _python_type_to_openapi(sig_param),
        }
        desc = param_docs.get(name)
        if desc:
            p["description"] = desc
        params.append(p)

    return params


def _build_request_body(
    body_params: List[str],
    sig: inspect.Signature,
    docstring: str,
) -> Dict[str, Any]:
    """Build an OpenAPI requestBody object."""
    param_docs = _parse_param_docs(docstring)
    properties: Dict[str, Any] = {}
    required: List[str] = []

    for name in body_params:
        sig_param = sig.parameters.get(name)
        prop = _python_type_to_openapi(sig_param)
        desc = param_docs.get(name)
        if desc:
            prop["description"] = desc
        properties[name] = prop
        if _is_param_required(sig_param):
            required.append(name)

    schema: Dict[str, Any] = {
        "type": "object",
        "properties": properties,
    }
    if required:
        schema["required"] = required

    return {
        "content": {
            "application/json": {
                "schema": schema,
            }
        }
    }


def _detect_response_media_type(source: str) -> str:
    """Detect the Accept header from method source to determine response media type.

    The SDK sets an explicit ``Accept`` header for non-JSON endpoints, e.g.::

        headers = {"Accept": "text/plain"}

    Returns:
        The media type string (defaults to ``application/json``).
    """
    m = re.search(r'"Accept"\s*:\s*"([^"]+)"', source)
    if m:
        return m.group(1)
    return "application/json"


def _build_responses(
    return_type: Optional[str],
    media_type: str = "application/json",
) -> Dict[str, Any]:
    """Build OpenAPI responses object.

    Args:
        return_type: Schema name for the response, or None.
        media_type: Response content type (e.g. ``text/plain``).
    """
    responses: Dict[str, Any] = {}

    if return_type:
        if media_type == "application/json":
            content_schema: Dict[str, Any] = {
                "$ref": f"#/components/schemas/{return_type}",
            }
        elif media_type == "application/octet-stream":
            content_schema = {"type": "string", "format": "binary"}
        elif media_type == "text/plain":
            # text/plain: wrap in object with contents property so StackQL
            # has a named column to project the raw response into.
            content_schema = {
                "type": "object",
                "properties": {
                    "contents": {"type": "string"},
                },
            }
        else:
            content_schema = {"type": "string"}

        responses["200"] = {
            "description": "Success",
            "content": {
                media_type: {
                    "schema": content_schema,
                }
            },
        }
    else:
        responses["200"] = {"description": "Success"}

    responses["default"] = {
        "description": "Error response",
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "error": {"type": "string"},
                        "message": {"type": "string"},
                    },
                }
            }
        },
    }

    return responses


def _get_return_type(method) -> Optional[str]:
    """Get the simple return type name if it's a dataclass/model reference."""
    hints = {}
    try:
        hints = method.__annotations__
    except AttributeError:
        pass
    ret = hints.get("return")
    if ret is None:
        return None

    # Handle string annotations (from __future__ import annotations)
    if isinstance(ret, str):
        name = ret.strip()
        # Skip built-in and non-schema types
        if name in ("str", "int", "float", "bool", "dict", "list", "None",
                     "NoneType", "Any", "BinaryIO", "bytes"):
            return None
        # Extract inner type from Iterator[X] -> X
        m = re.match(r"Iterator\[(\w+)\]", name)
        if m:
            return m.group(1)
        if name == "Iterator":
            return None
        # Extract inner type from Wait[X] -> X
        m = re.match(r"Wait\[(\w+)\]", name)
        if m:
            return m.group(1)
        if name == "Wait":
            return None
        # Skip other generic patterns like Optional[X] that weren't resolved
        if "[" in name:
            return None
        return name

    # Handle resolved type objects
    name = getattr(ret, "__name__", None) or getattr(ret, "_name", None)
    if name is None:
        return None
    # Filter out built-in types
    if name in ("str", "int", "float", "bool", "dict", "list", "None",
                 "NoneType", "Iterator", "Any", "BinaryIO", "bytes"):
        return None
    # Skip generic types like Iterator[X], Wait[X]
    origin = getattr(ret, "__origin__", None)
    if origin is not None:
        return None
    return name


def _is_iterator_method(method) -> bool:
    """Check if a method's return type is ``Iterator[X]``."""
    hints = {}
    try:
        hints = method.__annotations__
    except AttributeError:
        return False
    ret = hints.get("return")
    if ret is None:
        return False
    if isinstance(ret, str):
        return ret.strip().startswith("Iterator[")
    origin = getattr(ret, "__origin__", None)
    origin_name = getattr(origin, "__name__", "") or getattr(origin, "_name", "")
    return origin_name == "Iterator"


def _find_list_response_type(service_module, item_type_name: str) -> Optional[str]:
    """Find a List/Response wrapper dataclass that contains ``List[item_type_name]``.

    Searches all dataclasses in the module for one whose fields include a
    ``List[item_type_name]`` (or ``Optional[List[item_type_name]]``).  This
    corresponds to the actual HTTP response envelope that wraps a collection
    of items.

    Returns the wrapper class name or ``None`` if no match is found.
    """
    candidates = []
    for name, cls in inspect.getmembers(service_module, inspect.isclass):
        if not dataclasses.is_dataclass(cls):
            continue
        if cls.__module__ != service_module.__name__:
            continue
        for field in dataclasses.fields(cls):
            field_type = field.type
            if isinstance(field_type, str):
                if f"List[{item_type_name}]" in field_type:
                    candidates.append(name)
                    break
            else:
                # Handle resolved type annotations
                origin = getattr(field_type, "__origin__", None)
                args = getattr(field_type, "__args__", None)
                origin_name = getattr(origin, "__name__", "") or getattr(origin, "_name", "")
                if origin_name in ("List", "list") and args:
                    inner = getattr(args[0], "__name__", "")
                    if inner == item_type_name:
                        candidates.append(name)
                        break
                # Check Optional[List[X]] = Union[List[X], None]
                if origin_name == "Union" and args:
                    for a in args:
                        a_origin = getattr(a, "__origin__", None)
                        a_origin_name = getattr(a_origin, "__name__", "") or getattr(a_origin, "_name", "")
                        if a_origin_name in ("List", "list"):
                            a_args = getattr(a, "__args__", None)
                            if a_args:
                                inner = getattr(a_args[0], "__name__", "")
                                if inner == item_type_name:
                                    candidates.append(name)
                                    break

    if not candidates:
        return None
    # Prefer a class whose name contains "Response" or "List"
    for c in candidates:
        if "Response" in c or "List" in c:
            return c
    return candidates[0]


def _extract_json_field_mapping(dc: Type) -> Dict[str, str]:
    """Parse the ``from_dict`` classmethod to extract JSON-to-Python field name mapping.

    The SDK's ``from_dict`` methods contain the authoritative mapping between
    JSON wire names and Python attribute names, e.g.::

        display_name=d.get("displayName", None)
        resources=_repeated_dict(d, "Resources", AccountUser)

    Returns:
        Dict mapping Python field name to JSON wire name.  Falls back to
        identity mapping (python_name → python_name) for fields where parsing fails.
    """
    mapping: Dict[str, str] = {}
    from_dict = getattr(dc, "from_dict", None)
    if from_dict is None:
        return mapping

    try:
        source = inspect.getsource(from_dict)
    except (OSError, TypeError):
        return mapping

    # Pattern 1: field_name=d.get("json_name", ...)
    for m in re.finditer(r'(\w+)\s*=\s*d\.get\(\s*"([^"]+)"', source):
        mapping[m.group(1)] = m.group(2)

    # Pattern 2: field_name=_helper(d, "json_name", ...)
    # Covers _repeated_dict, _repeated_enum, _from_dict, _enum, etc.
    for m in re.finditer(r'(\w+)\s*=\s*_\w+\(\s*d\s*,\s*"([^"]+)"', source):
        mapping[m.group(1)] = m.group(2)

    return mapping


def _normalize_path(url_path: str) -> str:
    """Normalize f-string URL paths to OpenAPI path format.

    Converts expressions like ``{self._api.account_id}`` to
    ``{account_id}`` and strips helper function calls.
    """
    # Replace {self._api.account_id} with {account_id}
    path = re.sub(r"\{self\._api\.(\w+)\}", r"{\1}", url_path)
    # Replace {_escape_multi_segment_path_parameter(file_path)} with {file_path}
    path = re.sub(r"\{_escape_multi_segment_path_parameter\((\w+)\)\}", r"{\1}", path)
    return path


def _parse_param_docs(docstring: str) -> Dict[str, str]:
    """Parse ``:param name: description`` from a docstring."""
    result: Dict[str, str] = {}
    if not docstring:
        return result
    # Match :param name: and capture everything until next :param or :returns or end
    pattern = r":param (\w+):\s*(?:\S+\s*(?:\(optional\)\s*)?\n\s*)?(.*?)(?=\n\s*:param|\n\s*:returns|$)"
    for m in re.finditer(pattern, docstring, re.DOTALL):
        name = m.group(1)
        desc = m.group(2).strip()
        # Collapse multi-line descriptions
        desc = " ".join(desc.split())
        if desc:
            result[name] = desc
    return result


def _python_type_to_openapi(param: Optional[inspect.Parameter] = None) -> Dict[str, Any]:
    """Convert a Python parameter annotation to an OpenAPI schema snippet."""
    if param is None:
        return {"type": "string"}

    annotation = param.annotation
    if annotation is inspect.Parameter.empty:
        return {"type": "string"}

    return _annotation_to_schema(annotation)


def _annotation_to_schema(annotation) -> Dict[str, Any]:
    """Convert a Python type annotation to an OpenAPI schema."""
    if annotation is inspect.Parameter.empty or annotation is None:
        return {"type": "string"}

    # Handle string annotations
    if isinstance(annotation, str):
        if annotation == "str":
            return {"type": "string"}
        if annotation == "int":
            return {"type": "integer"}
        if annotation == "float":
            return {"type": "number"}
        if annotation == "bool":
            return {"type": "boolean"}
        return {"type": "string"}

    # Basic types
    if annotation is str:
        return {"type": "string"}
    if annotation is int:
        return {"type": "integer"}
    if annotation is float:
        return {"type": "number"}
    if annotation is bool:
        return {"type": "boolean"}

    # Check for well-known non-schema types before processing generics
    import typing
    if annotation is typing.BinaryIO:
        return {"type": "string", "format": "binary"}
    if annotation is typing.Any:
        return {"type": "object"}

    # Handle protobuf types (Timestamp, Duration)
    type_name = getattr(annotation, "__name__", None) or getattr(annotation, "DESCRIPTOR", None) and ""
    full_name = getattr(annotation, "__module__", "") + "." + (getattr(annotation, "__name__", "") or "")
    if "timestamp_pb2" in full_name or (isinstance(type_name, str) and type_name == "Timestamp"):
        return {"type": "string", "format": "date-time"}
    if "duration_pb2" in full_name or (isinstance(type_name, str) and type_name == "Duration"):
        return {"type": "string"}

    # Optional[X]
    origin = getattr(annotation, "__origin__", None)
    args = getattr(annotation, "__args__", None)

    if origin is not None:
        origin_name = getattr(origin, "__name__", "") or getattr(origin, "_name", "")
        # Optional is Union[X, None]
        if origin_name == "Union" and args and type(None) in args:
            non_none = [a for a in args if a is not type(None)]
            if len(non_none) == 1:
                return _annotation_to_schema(non_none[0])
        # List[X]
        if origin_name in ("List", "list"):
            if args:
                return {"type": "array", "items": _annotation_to_schema(args[0])}
            return {"type": "array", "items": {"type": "string"}}
        # Dict[K, V]
        if origin_name in ("Dict", "dict"):
            return {"type": "object"}
        # Iterator[X]
        if origin_name == "Iterator":
            if args:
                return _annotation_to_schema(args[0])
            return {"type": "string"}

    # Enum
    if isinstance(annotation, type) and issubclass(annotation, Enum):
        return {"$ref": f"#/components/schemas/{annotation.__name__}"}

    # Dataclass reference
    if isinstance(annotation, type) and dataclasses.is_dataclass(annotation):
        return {"$ref": f"#/components/schemas/{annotation.__name__}"}

    # Only create $ref for types that are known to be dataclasses or enums.
    # Do NOT create $ref for arbitrary Python types (BinaryIO, Any, dict, etc.)
    # as they won't have corresponding entries in components/schemas.
    name = getattr(annotation, "__name__", None)
    if name:
        logger.debug("Unmapped type annotation %s (%s), falling back to object", name, type(annotation))

    return {"type": "object"}


def _field_to_property(field: dataclasses.Field, service_module) -> Dict[str, Any]:
    """Convert a dataclass field to an OpenAPI property schema."""
    annotation = field.type
    # Resolve string annotations (from __future__ import annotations)
    if isinstance(annotation, str):
        annotation = _resolve_string_annotation(annotation, service_module)
    schema = _annotation_to_schema(annotation)
    return schema


def _extract_field_docs(dc: Type) -> Dict[str, str]:
    """Extract inline docstrings for dataclass fields from source.

    The Databricks SDK places docstrings as string literals after each field::

        name: str
        \"\"\"Name of the custom LLM\"\"\"

    Returns:
        Dict mapping field name to its description.
    """
    result: Dict[str, str] = {}
    try:
        source = inspect.getsource(dc)
    except (OSError, TypeError):
        return result

    # Match: field_name: type\n    """docstring"""
    pattern = r'(\w+):\s*[^\n]+\n\s+"""(.*?)"""'
    for m in re.finditer(pattern, source, re.DOTALL):
        field_name = m.group(1)
        doc = m.group(2).strip()
        doc = " ".join(doc.split())  # collapse whitespace
        if doc:
            result[field_name] = doc
    return result


def _resolve_string_annotation(annotation_str: str, service_module) -> Any:
    """Resolve a string-form type annotation against the service module namespace.

    Handles patterns like ``'Optional[List[Dataset]]'``, ``'str'``,
    ``'Optional[State]'``, etc.
    """
    import typing

    # Build a namespace for eval
    ns = {
        "Optional": typing.Optional,
        "List": typing.List,
        "Dict": typing.Dict,
        "Iterator": typing.Iterator,
        "Any": typing.Any,
        "str": str,
        "int": int,
        "float": float,
        "bool": bool,
        "BinaryIO": typing.BinaryIO,
    }
    # Add all classes from the service module
    for name, obj in inspect.getmembers(service_module, inspect.isclass):
        ns[name] = obj
    try:
        return eval(annotation_str, ns)
    except Exception:
        return annotation_str


def _is_required_field(field: dataclasses.Field) -> bool:
    """Check if a dataclass field is required (no default value)."""
    if field.default is not dataclasses.MISSING:
        return False
    if field.default_factory is not dataclasses.MISSING:
        return False
    return True


def _is_param_required(param: Optional[inspect.Parameter]) -> bool:
    """Check if a function parameter is required."""
    if param is None:
        return True
    if param.default is not inspect.Parameter.empty:
        return False
    if param.kind == inspect.Parameter.KEYWORD_ONLY:
        return param.default is inspect.Parameter.empty
    return True

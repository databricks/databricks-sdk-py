# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class ComplexQueryParam:
    nested_optional_query_param: Optional[str] = None

    nested_repeated_query_param: Optional[List[str]] = None

    def as_dict(self) -> dict:
        """Serializes the ComplexQueryParam into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.nested_optional_query_param is not None:
            body["nested_optional_query_param"] = self.nested_optional_query_param
        if self.nested_repeated_query_param:
            body["nested_repeated_query_param"] = [v for v in self.nested_repeated_query_param]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ComplexQueryParam into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.nested_optional_query_param is not None:
            body["nested_optional_query_param"] = self.nested_optional_query_param
        if self.nested_repeated_query_param:
            body["nested_repeated_query_param"] = self.nested_repeated_query_param
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ComplexQueryParam:
        """Deserializes the ComplexQueryParam from a dictionary."""
        return cls(
            nested_optional_query_param=d.get("nested_optional_query_param", None),
            nested_repeated_query_param=d.get("nested_repeated_query_param", None),
        )


@dataclass
class Resource:
    any_field: Optional[dict] = None

    body_field: Optional[str] = None

    nested_path_param_bool: Optional[bool] = None

    nested_path_param_int: Optional[int] = None

    nested_path_param_string: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the Resource into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.any_field:
            body["any_field"] = self.any_field
        if self.body_field is not None:
            body["body_field"] = self.body_field
        if self.nested_path_param_bool is not None:
            body["nested_path_param_bool"] = self.nested_path_param_bool
        if self.nested_path_param_int is not None:
            body["nested_path_param_int"] = self.nested_path_param_int
        if self.nested_path_param_string is not None:
            body["nested_path_param_string"] = self.nested_path_param_string
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Resource into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.any_field:
            body["any_field"] = self.any_field
        if self.body_field is not None:
            body["body_field"] = self.body_field
        if self.nested_path_param_bool is not None:
            body["nested_path_param_bool"] = self.nested_path_param_bool
        if self.nested_path_param_int is not None:
            body["nested_path_param_int"] = self.nested_path_param_int
        if self.nested_path_param_string is not None:
            body["nested_path_param_string"] = self.nested_path_param_string
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Resource:
        """Deserializes the Resource from a dictionary."""
        return cls(
            any_field=d.get("any_field", None),
            body_field=d.get("body_field", None),
            nested_path_param_bool=d.get("nested_path_param_bool", None),
            nested_path_param_int=d.get("nested_path_param_int", None),
            nested_path_param_string=d.get("nested_path_param_string", None),
        )


class HttpCallV2API:
    """Lorem Ipsum"""

    def __init__(self, api_client):
        self._api = api_client

    def create_resource(
        self, path_param_string: str, path_param_int: int, path_param_bool: bool, *, body_field: Optional[str] = None
    ) -> Resource:
        """This mimics "old" style post requests which have the resource inlined.

        :param path_param_string: str
        :param path_param_int: int
        :param path_param_bool: bool
        :param body_field: str (optional)
          Body element

        :returns: :class:`Resource`
        """
        body = {}
        if body_field is not None:
            body["body_field"] = body_field
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/http-call/{path_param_string}/{path_param_int}/{path_param_bool}",
            body=body,
            headers=headers,
        )
        return Resource.from_dict(res)

    def get_resource(
        self,
        path_param_string: str,
        path_param_int: int,
        path_param_bool: bool,
        *,
        field_mask: Optional[str] = None,
        optional_complex_query_param: Optional[ComplexQueryParam] = None,
        query_param_bool: Optional[bool] = None,
        query_param_int: Optional[int] = None,
        query_param_string: Optional[str] = None,
        repeated_complex_query_param: Optional[List[ComplexQueryParam]] = None,
        repeated_query_param: Optional[List[str]] = None,
    ) -> Resource:

        query = {}
        if field_mask is not None:
            query["field_mask"] = field_mask
        if optional_complex_query_param is not None:
            query["optional_complex_query_param"] = optional_complex_query_param.as_dict()
        if query_param_bool is not None:
            query["query_param_bool"] = query_param_bool
        if query_param_int is not None:
            query["query_param_int"] = query_param_int
        if query_param_string is not None:
            query["query_param_string"] = query_param_string
        if repeated_complex_query_param is not None:
            query["repeated_complex_query_param"] = [v.as_dict() for v in repeated_complex_query_param]
        if repeated_query_param is not None:
            query["repeated_query_param"] = [v for v in repeated_query_param]
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET",
            f"/api/2.0/http-call/{path_param_string}/{path_param_int}/{path_param_bool}",
            query=query,
            headers=headers,
        )
        return Resource.from_dict(res)

    def update_resource(
        self,
        nested_path_param_string: str,
        nested_path_param_int: int,
        nested_path_param_bool: bool,
        resource: Resource,
        *,
        field_mask: Optional[str] = None,
        optional_complex_query_param: Optional[ComplexQueryParam] = None,
        query_param_bool: Optional[bool] = None,
        query_param_int: Optional[int] = None,
        query_param_string: Optional[str] = None,
        repeated_complex_query_param: Optional[List[ComplexQueryParam]] = None,
        repeated_query_param: Optional[List[str]] = None,
    ) -> Resource:
        """This mimics "new" style post requests which have a body field.

        :param nested_path_param_string: str
        :param nested_path_param_int: int
        :param nested_path_param_bool: bool
        :param resource: :class:`Resource`
          Body element
        :param field_mask: str (optional)
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.
        :param optional_complex_query_param: :class:`ComplexQueryParam` (optional)
        :param query_param_bool: bool (optional)
        :param query_param_int: int (optional)
        :param query_param_string: str (optional)
        :param repeated_complex_query_param: List[:class:`ComplexQueryParam`] (optional)
        :param repeated_query_param: List[str] (optional)

        :returns: :class:`Resource`
        """
        body = resource.as_dict()
        query = {}
        if field_mask is not None:
            query["field_mask"] = field_mask
        if optional_complex_query_param is not None:
            query["optional_complex_query_param"] = optional_complex_query_param.as_dict()
        if query_param_bool is not None:
            query["query_param_bool"] = query_param_bool
        if query_param_int is not None:
            query["query_param_int"] = query_param_int
        if query_param_string is not None:
            query["query_param_string"] = query_param_string
        if repeated_complex_query_param is not None:
            query["repeated_complex_query_param"] = [v.as_dict() for v in repeated_complex_query_param]
        if repeated_query_param is not None:
            query["repeated_query_param"] = [v for v in repeated_query_param]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "PATCH",
            f"/api/2.0/http-call/{nested_path_param_string}/{nested_path_param_int}/{nested_path_param_bool}",
            query=query,
            body=body,
            headers=headers,
        )
        return Resource.from_dict(res)

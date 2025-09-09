# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional

from ._internal import _enum, _from_dict, _repeated_dict, _repeated_enum

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class NestedMessage:
    optional_duration: Optional[str] = None

    optional_string: Optional[str] = None

    optional_timestamp: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the NestedMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.optional_duration is not None:
            body["optional_duration"] = self.optional_duration
        if self.optional_string is not None:
            body["optional_string"] = self.optional_string
        if self.optional_timestamp is not None:
            body["optional_timestamp"] = self.optional_timestamp
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the NestedMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.optional_duration is not None:
            body["optional_duration"] = self.optional_duration
        if self.optional_string is not None:
            body["optional_string"] = self.optional_string
        if self.optional_timestamp is not None:
            body["optional_timestamp"] = self.optional_timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> NestedMessage:
        """Deserializes the NestedMessage from a dictionary."""
        return cls(
            optional_duration=d.get("optional_duration", None),
            optional_string=d.get("optional_string", None),
            optional_timestamp=d.get("optional_timestamp", None),
        )


@dataclass
class OptionalFields:
    duration: Optional[str] = None

    field_mask: Optional[str] = None
    """The field mask must be a single string, with multiple fields separated by commas (no spaces).
    The field path is relative to the resource object, using a dot (`.`) to navigate sub-fields
    (e.g., `author.given_name`). Specification of elements in sequence or map fields is not allowed,
    as only the entire collection field can be specified. Field names must exactly match the
    resource field names."""

    legacy_duration: Optional[str] = None
    """Legacy Well Known types"""

    legacy_field_mask: Optional[str] = None
    """The field mask must be a single string, with multiple fields separated by commas (no spaces).
    The field path is relative to the resource object, using a dot (`.`) to navigate sub-fields
    (e.g., `author.given_name`). Specification of elements in sequence or map fields is not allowed,
    as only the entire collection field can be specified. Field names must exactly match the
    resource field names."""

    legacy_timestamp: Optional[str] = None

    list_value: Optional[List[any]] = None

    map: Optional[Dict[str, str]] = None
    """Lint disable reason: This is a dummy field used to test SDK Generation logic."""

    optional_bool: Optional[bool] = None

    optional_int32: Optional[int] = None

    optional_int64: Optional[int] = None

    optional_message: Optional[NestedMessage] = None

    optional_string: Optional[str] = None

    struct: Optional[Dict[str, any]] = None

    test_enum: Optional[TestEnum] = None

    timestamp: Optional[str] = None

    value: Optional[any] = None

    def as_dict(self) -> dict:
        """Serializes the OptionalFields into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.duration is not None:
            body["duration"] = self.duration
        if self.field_mask is not None:
            body["field_mask"] = self.field_mask
        if self.legacy_duration is not None:
            body["legacy_duration"] = self.legacy_duration
        if self.legacy_field_mask is not None:
            body["legacy_field_mask"] = self.legacy_field_mask
        if self.legacy_timestamp is not None:
            body["legacy_timestamp"] = self.legacy_timestamp
        if self.list_value:
            body["list_value"] = [v for v in self.list_value]
        if self.map:
            body["map"] = self.map
        if self.optional_bool is not None:
            body["optional_bool"] = self.optional_bool
        if self.optional_int32 is not None:
            body["optional_int32"] = self.optional_int32
        if self.optional_int64 is not None:
            body["optional_int64"] = self.optional_int64
        if self.optional_message:
            body["optional_message"] = self.optional_message.as_dict()
        if self.optional_string is not None:
            body["optional_string"] = self.optional_string
        if self.struct:
            body["struct"] = self.struct
        if self.test_enum is not None:
            body["test_enum"] = self.test_enum.value
        if self.timestamp is not None:
            body["timestamp"] = self.timestamp
        if self.value:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the OptionalFields into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.duration is not None:
            body["duration"] = self.duration
        if self.field_mask is not None:
            body["field_mask"] = self.field_mask
        if self.legacy_duration is not None:
            body["legacy_duration"] = self.legacy_duration
        if self.legacy_field_mask is not None:
            body["legacy_field_mask"] = self.legacy_field_mask
        if self.legacy_timestamp is not None:
            body["legacy_timestamp"] = self.legacy_timestamp
        if self.list_value:
            body["list_value"] = self.list_value
        if self.map:
            body["map"] = self.map
        if self.optional_bool is not None:
            body["optional_bool"] = self.optional_bool
        if self.optional_int32 is not None:
            body["optional_int32"] = self.optional_int32
        if self.optional_int64 is not None:
            body["optional_int64"] = self.optional_int64
        if self.optional_message:
            body["optional_message"] = self.optional_message
        if self.optional_string is not None:
            body["optional_string"] = self.optional_string
        if self.struct:
            body["struct"] = self.struct
        if self.test_enum is not None:
            body["test_enum"] = self.test_enum
        if self.timestamp is not None:
            body["timestamp"] = self.timestamp
        if self.value:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> OptionalFields:
        """Deserializes the OptionalFields from a dictionary."""
        return cls(
            duration=d.get("duration", None),
            field_mask=d.get("field_mask", None),
            legacy_duration=d.get("legacy_duration", None),
            legacy_field_mask=d.get("legacy_field_mask", None),
            legacy_timestamp=d.get("legacy_timestamp", None),
            list_value=d.get("list_value", None),
            map=d.get("map", None),
            optional_bool=d.get("optional_bool", None),
            optional_int32=d.get("optional_int32", None),
            optional_int64=d.get("optional_int64", None),
            optional_message=_from_dict(d, "optional_message", NestedMessage),
            optional_string=d.get("optional_string", None),
            struct=d.get("struct", None),
            test_enum=_enum(d, "test_enum", TestEnum),
            timestamp=d.get("timestamp", None),
            value=d.get("value", None),
        )


@dataclass
class RepeatedFields:
    repeated_bool: Optional[List[bool]] = None

    repeated_duration: Optional[List[str]] = None

    repeated_field_mask: Optional[List[str]] = None

    repeated_int32: Optional[List[int]] = None

    repeated_int64: Optional[List[int]] = None

    repeated_list_value: Optional[List[List[any]]] = None

    repeated_message: Optional[List[NestedMessage]] = None

    repeated_string: Optional[List[str]] = None

    repeated_struct: Optional[List[Dict[str, any]]] = None

    repeated_timestamp: Optional[List[str]] = None

    repeated_value: Optional[List[any]] = None

    test_repeated_enum: Optional[List[TestEnum]] = None

    def as_dict(self) -> dict:
        """Serializes the RepeatedFields into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.repeated_bool:
            body["repeated_bool"] = [v for v in self.repeated_bool]
        if self.repeated_duration:
            body["repeated_duration"] = [v for v in self.repeated_duration]
        if self.repeated_field_mask:
            body["repeated_field_mask"] = [v for v in self.repeated_field_mask]
        if self.repeated_int32:
            body["repeated_int32"] = [v for v in self.repeated_int32]
        if self.repeated_int64:
            body["repeated_int64"] = [v for v in self.repeated_int64]
        if self.repeated_list_value:
            body["repeated_list_value"] = [v for v in self.repeated_list_value]
        if self.repeated_message:
            body["repeated_message"] = [v.as_dict() for v in self.repeated_message]
        if self.repeated_string:
            body["repeated_string"] = [v for v in self.repeated_string]
        if self.repeated_struct:
            body["repeated_struct"] = [v for v in self.repeated_struct]
        if self.repeated_timestamp:
            body["repeated_timestamp"] = [v for v in self.repeated_timestamp]
        if self.repeated_value:
            body["repeated_value"] = [v for v in self.repeated_value]
        if self.test_repeated_enum:
            body["test_repeated_enum"] = [v.value for v in self.test_repeated_enum]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RepeatedFields into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.repeated_bool:
            body["repeated_bool"] = self.repeated_bool
        if self.repeated_duration:
            body["repeated_duration"] = self.repeated_duration
        if self.repeated_field_mask:
            body["repeated_field_mask"] = self.repeated_field_mask
        if self.repeated_int32:
            body["repeated_int32"] = self.repeated_int32
        if self.repeated_int64:
            body["repeated_int64"] = self.repeated_int64
        if self.repeated_list_value:
            body["repeated_list_value"] = self.repeated_list_value
        if self.repeated_message:
            body["repeated_message"] = self.repeated_message
        if self.repeated_string:
            body["repeated_string"] = self.repeated_string
        if self.repeated_struct:
            body["repeated_struct"] = self.repeated_struct
        if self.repeated_timestamp:
            body["repeated_timestamp"] = self.repeated_timestamp
        if self.repeated_value:
            body["repeated_value"] = self.repeated_value
        if self.test_repeated_enum:
            body["test_repeated_enum"] = self.test_repeated_enum
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RepeatedFields:
        """Deserializes the RepeatedFields from a dictionary."""
        return cls(
            repeated_bool=d.get("repeated_bool", None),
            repeated_duration=d.get("repeated_duration", None),
            repeated_field_mask=d.get("repeated_field_mask", None),
            repeated_int32=d.get("repeated_int32", None),
            repeated_int64=d.get("repeated_int64", None),
            repeated_list_value=d.get("repeated_list_value", None),
            repeated_message=_repeated_dict(d, "repeated_message", NestedMessage),
            repeated_string=d.get("repeated_string", None),
            repeated_struct=d.get("repeated_struct", None),
            repeated_timestamp=d.get("repeated_timestamp", None),
            repeated_value=d.get("repeated_value", None),
            test_repeated_enum=_repeated_enum(d, "test_repeated_enum", TestEnum),
        )


@dataclass
class RequiredFields:
    required_string: str

    required_int32: int

    required_int64: int

    required_bool: bool

    required_message: NestedMessage

    test_required_enum: TestEnum

    required_duration: str

    required_field_mask: str
    """The field mask must be a single string, with multiple fields separated by commas (no spaces).
    The field path is relative to the resource object, using a dot (`.`) to navigate sub-fields
    (e.g., `author.given_name`). Specification of elements in sequence or map fields is not allowed,
    as only the entire collection field can be specified. Field names must exactly match the
    resource field names."""

    required_timestamp: str

    required_value: any

    required_list_value: List[any]

    required_struct: Dict[str, any]

    def as_dict(self) -> dict:
        """Serializes the RequiredFields into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.required_bool is not None:
            body["required_bool"] = self.required_bool
        if self.required_duration is not None:
            body["required_duration"] = self.required_duration
        if self.required_field_mask is not None:
            body["required_field_mask"] = self.required_field_mask
        if self.required_int32 is not None:
            body["required_int32"] = self.required_int32
        if self.required_int64 is not None:
            body["required_int64"] = self.required_int64
        if self.required_list_value:
            body["required_list_value"] = [v for v in self.required_list_value]
        if self.required_message:
            body["required_message"] = self.required_message.as_dict()
        if self.required_string is not None:
            body["required_string"] = self.required_string
        if self.required_struct:
            body["required_struct"] = self.required_struct
        if self.required_timestamp is not None:
            body["required_timestamp"] = self.required_timestamp
        if self.required_value:
            body["required_value"] = self.required_value
        if self.test_required_enum is not None:
            body["test_required_enum"] = self.test_required_enum.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RequiredFields into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.required_bool is not None:
            body["required_bool"] = self.required_bool
        if self.required_duration is not None:
            body["required_duration"] = self.required_duration
        if self.required_field_mask is not None:
            body["required_field_mask"] = self.required_field_mask
        if self.required_int32 is not None:
            body["required_int32"] = self.required_int32
        if self.required_int64 is not None:
            body["required_int64"] = self.required_int64
        if self.required_list_value:
            body["required_list_value"] = self.required_list_value
        if self.required_message:
            body["required_message"] = self.required_message
        if self.required_string is not None:
            body["required_string"] = self.required_string
        if self.required_struct:
            body["required_struct"] = self.required_struct
        if self.required_timestamp is not None:
            body["required_timestamp"] = self.required_timestamp
        if self.required_value:
            body["required_value"] = self.required_value
        if self.test_required_enum is not None:
            body["test_required_enum"] = self.test_required_enum
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RequiredFields:
        """Deserializes the RequiredFields from a dictionary."""
        return cls(
            required_bool=d.get("required_bool", None),
            required_duration=d.get("required_duration", None),
            required_field_mask=d.get("required_field_mask", None),
            required_int32=d.get("required_int32", None),
            required_int64=d.get("required_int64", None),
            required_list_value=d.get("required_list_value", None),
            required_message=_from_dict(d, "required_message", NestedMessage),
            required_string=d.get("required_string", None),
            required_struct=d.get("required_struct", None),
            required_timestamp=d.get("required_timestamp", None),
            required_value=d.get("required_value", None),
            test_required_enum=_enum(d, "test_required_enum", TestEnum),
        )


@dataclass
class Resource:
    """We separate this into 3 submessages to simplify test cases. E.g., any required top level field
    needs to be included in the expected json for each test case."""

    optional_fields: Optional[OptionalFields] = None

    repeated_fields: Optional[RepeatedFields] = None

    required_fields: Optional[RequiredFields] = None

    def as_dict(self) -> dict:
        """Serializes the Resource into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.optional_fields:
            body["optional_fields"] = self.optional_fields.as_dict()
        if self.repeated_fields:
            body["repeated_fields"] = self.repeated_fields.as_dict()
        if self.required_fields:
            body["required_fields"] = self.required_fields.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Resource into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.optional_fields:
            body["optional_fields"] = self.optional_fields
        if self.repeated_fields:
            body["repeated_fields"] = self.repeated_fields
        if self.required_fields:
            body["required_fields"] = self.required_fields
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Resource:
        """Deserializes the Resource from a dictionary."""
        return cls(
            optional_fields=_from_dict(d, "optional_fields", OptionalFields),
            repeated_fields=_from_dict(d, "repeated_fields", RepeatedFields),
            required_fields=_from_dict(d, "required_fields", RequiredFields),
        )


class TestEnum(Enum):

    TEST_ENUM_ONE = "TEST_ENUM_ONE"
    TEST_ENUM_TWO = "TEST_ENUM_TWO"


class JsonMarshallV2API:
    """Lorem Ipsum"""

    def __init__(self, api_client):
        self._api = api_client

    def get_resource(self, name: str, resource: Resource) -> Resource:

        query = {}
        if resource is not None:
            query["resource"] = resource.as_dict()
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/json-marshall/{name}", query=query, headers=headers)
        return Resource.from_dict(res)

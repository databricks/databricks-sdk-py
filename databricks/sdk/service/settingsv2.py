# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Dict, Optional

from ._internal import _from_dict

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class BooleanMessage:
    value: Optional[bool] = None

    def as_dict(self) -> dict:
        """Serializes the BooleanMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the BooleanMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> BooleanMessage:
        """Deserializes the BooleanMessage from a dictionary."""
        return cls(value=d.get("value", None))


@dataclass
class IntegerMessage:
    value: Optional[int] = None

    def as_dict(self) -> dict:
        """Serializes the IntegerMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the IntegerMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> IntegerMessage:
        """Deserializes the IntegerMessage from a dictionary."""
        return cls(value=d.get("value", None))


@dataclass
class Setting:
    boolean_val: Optional[BooleanMessage] = None

    effective_boolean_val: Optional[BooleanMessage] = None

    effective_integer_val: Optional[IntegerMessage] = None

    effective_string_val: Optional[StringMessage] = None

    integer_val: Optional[IntegerMessage] = None

    name: Optional[str] = None
    """Name of the setting."""

    string_val: Optional[StringMessage] = None

    def as_dict(self) -> dict:
        """Serializes the Setting into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.boolean_val:
            body["boolean_val"] = self.boolean_val.as_dict()
        if self.effective_boolean_val:
            body["effective_boolean_val"] = self.effective_boolean_val.as_dict()
        if self.effective_integer_val:
            body["effective_integer_val"] = self.effective_integer_val.as_dict()
        if self.effective_string_val:
            body["effective_string_val"] = self.effective_string_val.as_dict()
        if self.integer_val:
            body["integer_val"] = self.integer_val.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.string_val:
            body["string_val"] = self.string_val.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Setting into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.boolean_val:
            body["boolean_val"] = self.boolean_val
        if self.effective_boolean_val:
            body["effective_boolean_val"] = self.effective_boolean_val
        if self.effective_integer_val:
            body["effective_integer_val"] = self.effective_integer_val
        if self.effective_string_val:
            body["effective_string_val"] = self.effective_string_val
        if self.integer_val:
            body["integer_val"] = self.integer_val
        if self.name is not None:
            body["name"] = self.name
        if self.string_val:
            body["string_val"] = self.string_val
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Setting:
        """Deserializes the Setting from a dictionary."""
        return cls(
            boolean_val=_from_dict(d, "boolean_val", BooleanMessage),
            effective_boolean_val=_from_dict(d, "effective_boolean_val", BooleanMessage),
            effective_integer_val=_from_dict(d, "effective_integer_val", IntegerMessage),
            effective_string_val=_from_dict(d, "effective_string_val", StringMessage),
            integer_val=_from_dict(d, "integer_val", IntegerMessage),
            name=d.get("name", None),
            string_val=_from_dict(d, "string_val", StringMessage),
        )


@dataclass
class StringMessage:
    value: Optional[str] = None
    """Represents a generic string value."""

    def as_dict(self) -> dict:
        """Serializes the StringMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the StringMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> StringMessage:
        """Deserializes the StringMessage from a dictionary."""
        return cls(value=d.get("value", None))


class AccountSettingsV2API:
    """APIs to manage account level settings"""

    def __init__(self, api_client):
        self._api = api_client

    def get_public_account_setting(self, name: str) -> Setting:
        """Get a setting value at account level

        :param name: str

        :returns: :class:`Setting`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.1/accounts/{self._api.account_id}/settings/{name}", headers=headers)
        return Setting.from_dict(res)

    def patch_public_account_setting(self, name: str, setting: Setting) -> Setting:
        """Patch a setting value at account level

        :param name: str
        :param setting: :class:`Setting`

        :returns: :class:`Setting`
        """
        body = setting.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "PATCH", f"/api/2.1/accounts/{self._api.account_id}/settings/{name}", body=body, headers=headers
        )
        return Setting.from_dict(res)


class WorkspaceSettingsV2API:
    """APIs to manage workspace level settings"""

    def __init__(self, api_client):
        self._api = api_client

    def get_public_workspace_setting(self, name: str) -> Setting:
        """Get a setting value at workspace level

        :param name: str

        :returns: :class:`Setting`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.1/settings/{name}", headers=headers)
        return Setting.from_dict(res)

    def patch_public_workspace_setting(self, name: str, setting: Setting) -> Setting:
        """Patch a setting value at workspace level

        :param name: str
        :param setting: :class:`Setting`

        :returns: :class:`Setting`
        """
        body = setting.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.1/settings/{name}", body=body, headers=headers)
        return Setting.from_dict(res)

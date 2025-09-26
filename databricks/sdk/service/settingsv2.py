# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Dict, Iterator, List, Optional

from ._internal import _from_dict, _repeated_dict

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
class ListAccountSettingsMetadataResponse:
    next_page_token: Optional[str] = None
    """A token that can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    settings_metadata: Optional[List[SettingsMetadata]] = None
    """List of all settings available via public APIs and their metadata"""

    def as_dict(self) -> dict:
        """Serializes the ListAccountSettingsMetadataResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.settings_metadata:
            body["settings_metadata"] = [v.as_dict() for v in self.settings_metadata]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListAccountSettingsMetadataResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.settings_metadata:
            body["settings_metadata"] = self.settings_metadata
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListAccountSettingsMetadataResponse:
        """Deserializes the ListAccountSettingsMetadataResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            settings_metadata=_repeated_dict(d, "settings_metadata", SettingsMetadata),
        )


@dataclass
class ListWorkspaceSettingsMetadataResponse:
    next_page_token: Optional[str] = None
    """A token that can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    settings_metadata: Optional[List[SettingsMetadata]] = None
    """List of all settings available via public APIs and their metadata"""

    def as_dict(self) -> dict:
        """Serializes the ListWorkspaceSettingsMetadataResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.settings_metadata:
            body["settings_metadata"] = [v.as_dict() for v in self.settings_metadata]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListWorkspaceSettingsMetadataResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.settings_metadata:
            body["settings_metadata"] = self.settings_metadata
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListWorkspaceSettingsMetadataResponse:
        """Deserializes the ListWorkspaceSettingsMetadataResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            settings_metadata=_repeated_dict(d, "settings_metadata", SettingsMetadata),
        )


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
class SettingsMetadata:
    description: Optional[str] = None
    """Setting description for what this setting controls"""

    docs_link: Optional[str] = None
    """Link to databricks documentation for the setting"""

    name: Optional[str] = None
    """Name of the setting."""

    type: Optional[str] = None
    """Type of the setting. To set this setting, the value sent must match this type."""

    def as_dict(self) -> dict:
        """Serializes the SettingsMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.docs_link is not None:
            body["docs_link"] = self.docs_link
        if self.name is not None:
            body["name"] = self.name
        if self.type is not None:
            body["type"] = self.type
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SettingsMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.docs_link is not None:
            body["docs_link"] = self.docs_link
        if self.name is not None:
            body["name"] = self.name
        if self.type is not None:
            body["type"] = self.type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SettingsMetadata:
        """Deserializes the SettingsMetadata from a dictionary."""
        return cls(
            description=d.get("description", None),
            docs_link=d.get("docs_link", None),
            name=d.get("name", None),
            type=d.get("type", None),
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

    def list_account_settings_metadata(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[SettingsMetadata]:
        """List valid setting keys and metadata. These settings are available to referenced via [GET
        /api/2.1/settings/{name}](#~1api~1account~1settingsv2~1getpublicaccountsetting) and [PATCH
        /api/2.1/settings/{name}](#~1api~1account~1settingsv2~patchpublicaccountsetting) APIs

        :param page_size: int (optional)
          The maximum number of settings to return. The service may return fewer than this value. If
          unspecified, at most 200 settings will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListAccountSettingsMetadataRequest` call. Provide this to
          retrieve the subsequent page.

          When paginating, all other parameters provided to `ListAccountSettingsMetadataRequest` must match
          the call that provided the page token.

        :returns: Iterator over :class:`SettingsMetadata`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do(
                "GET", f"/api/2.1/accounts/{self._api.account_id}/settings-metadata", query=query, headers=headers
            )
            if "settings_metadata" in json:
                for v in json["settings_metadata"]:
                    yield SettingsMetadata.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

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

    def list_workspace_settings_metadata(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[SettingsMetadata]:
        """List valid setting keys and metadata. These settings are available to referenced via [GET
        /api/2.1/settings/{name}](#~1api~1workspace~1settingsv2~1getpublicworkspacesetting) and [PATCH
        /api/2.1/settings/{name}](#~1api~1workspace~1settingsv2~patchpublicworkspacesetting) APIs

        :param page_size: int (optional)
          The maximum number of settings to return. The service may return fewer than this value. If
          unspecified, at most 200 settings will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListWorkspaceSettingsMetadataRequest` call. Provide this to
          retrieve the subsequent page.

          When paginating, all other parameters provided to `ListWorkspaceSettingsMetadataRequest` must match
          the call that provided the page token.

        :returns: Iterator over :class:`SettingsMetadata`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do("GET", "/api/2.1/settings-metadata", query=query, headers=headers)
            if "settings_metadata" in json:
                for v in json["settings_metadata"]:
                    yield SettingsMetadata.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

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

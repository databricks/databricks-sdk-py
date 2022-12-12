# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class CreateIpAccessList:

    # Array of IP addresses or CIDR values to be added to the IP access list.
    ip_addresses: "List[str]"
    # Label for the IP access list. This **cannot** be empty.
    label: str
    # This describes an enum
    list_type: "ListType"

    def as_request(self) -> (dict, dict):
        createIpAccessList_query, createIpAccessList_body = {}, {}
        if self.ip_addresses:
            createIpAccessList_body["ip_addresses"] = [v for v in self.ip_addresses]
        if self.label:
            createIpAccessList_body["label"] = self.label
        if self.list_type:
            createIpAccessList_body["list_type"] = self.list_type.value

        return createIpAccessList_query, createIpAccessList_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateIpAccessList":
        return cls(
            ip_addresses=d.get("ip_addresses", None),
            label=d.get("label", None),
            list_type=ListType(d["list_type"]) if "list_type" in d else None,
        )


@dataclass
class CreateIpAccessListResponse:

    ip_access_list: "IpAccessListInfo"

    def as_request(self) -> (dict, dict):
        createIpAccessListResponse_query, createIpAccessListResponse_body = {}, {}
        if self.ip_access_list:
            createIpAccessListResponse_body[
                "ip_access_list"
            ] = self.ip_access_list.as_request()[1]

        return createIpAccessListResponse_query, createIpAccessListResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateIpAccessListResponse":
        return cls(
            ip_access_list=IpAccessListInfo.from_dict(d["ip_access_list"])
            if "ip_access_list" in d
            else None,
        )


@dataclass
class Delete:
    """Delete access list"""

    # The ID for the corresponding IP access list to modify.
    ip_access_list_id: str  # path

    def as_request(self) -> (dict, dict):
        delete_query, delete_body = {}, {}
        if self.ip_access_list_id:
            delete_body["ip_access_list_id"] = self.ip_access_list_id

        return delete_query, delete_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Delete":
        return cls(
            ip_access_list_id=d.get("ip_access_list_id", None),
        )


@dataclass
class FetchIpAccessListResponse:

    ip_access_list: "IpAccessListInfo"

    def as_request(self) -> (dict, dict):
        fetchIpAccessListResponse_query, fetchIpAccessListResponse_body = {}, {}
        if self.ip_access_list:
            fetchIpAccessListResponse_body[
                "ip_access_list"
            ] = self.ip_access_list.as_request()[1]

        return fetchIpAccessListResponse_query, fetchIpAccessListResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "FetchIpAccessListResponse":
        return cls(
            ip_access_list=IpAccessListInfo.from_dict(d["ip_access_list"])
            if "ip_access_list" in d
            else None,
        )


@dataclass
class Get:
    """Get access list"""

    # The ID for the corresponding IP access list to modify.
    ip_access_list_id: str  # path

    def as_request(self) -> (dict, dict):
        get_query, get_body = {}, {}
        if self.ip_access_list_id:
            get_body["ip_access_list_id"] = self.ip_access_list_id

        return get_query, get_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Get":
        return cls(
            ip_access_list_id=d.get("ip_access_list_id", None),
        )


@dataclass
class GetIpAccessListResponse:

    ip_access_lists: "List[IpAccessListInfo]"

    def as_request(self) -> (dict, dict):
        getIpAccessListResponse_query, getIpAccessListResponse_body = {}, {}
        if self.ip_access_lists:
            getIpAccessListResponse_body["ip_access_lists"] = [
                v.as_request()[1] for v in self.ip_access_lists
            ]

        return getIpAccessListResponse_query, getIpAccessListResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetIpAccessListResponse":
        return cls(
            ip_access_lists=[
                IpAccessListInfo.from_dict(v) for v in d["ip_access_lists"]
            ]
            if "ip_access_lists" in d
            else None,
        )


@dataclass
class IpAccessListInfo:

    # Total number of IP or CIDR values.
    address_count: int
    # Creation timestamp in milliseconds.
    created_at: int
    # User ID of the user who created this list.
    created_by: int
    # Specifies whether this IP access list is enabled.
    enabled: bool
    # Array of IP addresses or CIDR values to be added to the IP access list.
    ip_addresses: "List[str]"
    # Label for the IP access list. This **cannot** be empty.
    label: str
    # Universally unique identifier(UUID) of the IP access list.
    list_id: str
    # This describes an enum
    list_type: "ListType"
    # Update timestamp in milliseconds.
    updated_at: int
    # User ID of the user who updated this list.
    updated_by: int

    def as_request(self) -> (dict, dict):
        ipAccessListInfo_query, ipAccessListInfo_body = {}, {}
        if self.address_count:
            ipAccessListInfo_body["address_count"] = self.address_count
        if self.created_at:
            ipAccessListInfo_body["created_at"] = self.created_at
        if self.created_by:
            ipAccessListInfo_body["created_by"] = self.created_by
        if self.enabled:
            ipAccessListInfo_body["enabled"] = self.enabled
        if self.ip_addresses:
            ipAccessListInfo_body["ip_addresses"] = [v for v in self.ip_addresses]
        if self.label:
            ipAccessListInfo_body["label"] = self.label
        if self.list_id:
            ipAccessListInfo_body["list_id"] = self.list_id
        if self.list_type:
            ipAccessListInfo_body["list_type"] = self.list_type.value
        if self.updated_at:
            ipAccessListInfo_body["updated_at"] = self.updated_at
        if self.updated_by:
            ipAccessListInfo_body["updated_by"] = self.updated_by

        return ipAccessListInfo_query, ipAccessListInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "IpAccessListInfo":
        return cls(
            address_count=d.get("address_count", None),
            created_at=d.get("created_at", None),
            created_by=d.get("created_by", None),
            enabled=d.get("enabled", None),
            ip_addresses=d.get("ip_addresses", None),
            label=d.get("label", None),
            list_id=d.get("list_id", None),
            list_type=ListType(d["list_type"]) if "list_type" in d else None,
            updated_at=d.get("updated_at", None),
            updated_by=d.get("updated_by", None),
        )


class ListType(Enum):
    """This describes an enum"""

    ALLOW = "ALLOW"
    BLOCK = "BLOCK"


@dataclass
class ReplaceIpAccessList:

    # Specifies whether this IP access list is enabled.
    enabled: bool
    # The ID for the corresponding IP access list to modify.
    ip_access_list_id: str  # path
    # Array of IP addresses or CIDR values to be added to the IP access list.
    ip_addresses: "List[str]"
    # Label for the IP access list. This **cannot** be empty.
    label: str
    # Universally unique identifier(UUID) of the IP access list.
    list_id: str
    # This describes an enum
    list_type: "ListType"

    def as_request(self) -> (dict, dict):
        replaceIpAccessList_query, replaceIpAccessList_body = {}, {}
        if self.enabled:
            replaceIpAccessList_body["enabled"] = self.enabled
        if self.ip_access_list_id:
            replaceIpAccessList_body["ip_access_list_id"] = self.ip_access_list_id
        if self.ip_addresses:
            replaceIpAccessList_body["ip_addresses"] = [v for v in self.ip_addresses]
        if self.label:
            replaceIpAccessList_body["label"] = self.label
        if self.list_id:
            replaceIpAccessList_body["list_id"] = self.list_id
        if self.list_type:
            replaceIpAccessList_body["list_type"] = self.list_type.value

        return replaceIpAccessList_query, replaceIpAccessList_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ReplaceIpAccessList":
        return cls(
            enabled=d.get("enabled", None),
            ip_access_list_id=d.get("ip_access_list_id", None),
            ip_addresses=d.get("ip_addresses", None),
            label=d.get("label", None),
            list_id=d.get("list_id", None),
            list_type=ListType(d["list_type"]) if "list_type" in d else None,
        )


@dataclass
class UpdateIpAccessList:

    # Specifies whether this IP access list is enabled.
    enabled: bool
    # The ID for the corresponding IP access list to modify.
    ip_access_list_id: str  # path
    # Array of IP addresses or CIDR values to be added to the IP access list.
    ip_addresses: "List[str]"
    # Label for the IP access list. This **cannot** be empty.
    label: str
    # Universally unique identifier(UUID) of the IP access list.
    list_id: str
    # This describes an enum
    list_type: "ListType"

    def as_request(self) -> (dict, dict):
        updateIpAccessList_query, updateIpAccessList_body = {}, {}
        if self.enabled:
            updateIpAccessList_body["enabled"] = self.enabled
        if self.ip_access_list_id:
            updateIpAccessList_body["ip_access_list_id"] = self.ip_access_list_id
        if self.ip_addresses:
            updateIpAccessList_body["ip_addresses"] = [v for v in self.ip_addresses]
        if self.label:
            updateIpAccessList_body["label"] = self.label
        if self.list_id:
            updateIpAccessList_body["list_id"] = self.list_id
        if self.list_type:
            updateIpAccessList_body["list_type"] = self.list_type.value

        return updateIpAccessList_query, updateIpAccessList_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateIpAccessList":
        return cls(
            enabled=d.get("enabled", None),
            ip_access_list_id=d.get("ip_access_list_id", None),
            ip_addresses=d.get("ip_addresses", None),
            label=d.get("label", None),
            list_id=d.get("list_id", None),
            list_type=ListType(d["list_type"]) if "list_type" in d else None,
        )


class IpAccessListsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateIpAccessList) -> CreateIpAccessListResponse:
        """Create access list.

        Creates an IP access list for this workspace. A list can be an allow
        list or a block list. See the top of this file for a description of how
        the server treats allow lists and block lists at runtime.

        When creating or updating an IP access list:

        * For all allow lists and block lists combined, the API supports a
        maximum of 1000 IP/CIDR values, where one CIDR counts as a single value.
        Attempts to exceed that number return error 400 with `error_code` value
        `QUOTA_EXCEEDED`. * If the new list would block the calling user's
        current IP, error 400 is returned with `error_code` value
        `INVALID_STATE`.

        It can take a few minutes for the changes to take effect. **Note**: Your
        new IP access list has no effect until you enable the feature. See
        :method:workspaceconf/setStatus"""
        query, body = request.as_request()
        json = self._api.do("POST", "/api/2.0/ip-access-lists", query=query, body=body)
        return CreateIpAccessListResponse.from_dict(json)

    def delete(self, request: Delete):
        """Delete access list.

        Deletes an IP access list, specified by its list ID."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/ip-access-lists/{request.ip_access_list_id}",
            query=query,
            body=body,
        )

    def get(self, request: Get) -> FetchIpAccessListResponse:
        """Get access list.

        Gets an IP access list, specified by its list ID."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/ip-access-lists/{request.ip_access_list_id}",
            query=query,
            body=body,
        )
        return FetchIpAccessListResponse.from_dict(json)

    def list(self) -> GetIpAccessListResponse:
        """Get access lists.

        Gets all IP access lists for the specified workspace."""

        json = self._api.do("GET", "/api/2.0/ip-access-lists")
        return GetIpAccessListResponse.from_dict(json)

    def replace(self, request: ReplaceIpAccessList):
        """Replace access list.

        Replaces an IP access list, specified by its ID. A list can include
        allow lists and block lists. See the top of this file for a description
        of how the server treats allow lists and block lists at run time. When
        replacing an IP access list: * For all allow lists and block lists
        combined, the API supports a maximum of 1000 IP/CIDR values, where one
        CIDR counts as a single value. Attempts to exceed that number return
        error 400 with `error_code` value `QUOTA_EXCEEDED`. * If the resulting
        list would block the calling user's current IP, error 400 is returned
        with `error_code` value `INVALID_STATE`. It can take a few minutes for
        the changes to take effect. Note that your resulting IP access list has
        no effect until you enable the feature. See
        :method:workspaceconf/setStatus."""
        query, body = request.as_request()
        self._api.do(
            "PUT",
            f"/api/2.0/ip-access-lists/{request.ip_access_list_id}",
            query=query,
            body=body,
        )

    def update(self, request: UpdateIpAccessList):
        """Update access list.

        Updates an existing IP access list, specified by its ID. A list can
        include allow lists and block lists. See the top of this file for a
        description of how the server treats allow lists and block lists at run
        time.

        When updating an IP access list:

        * For all allow lists and block lists combined, the API supports a
        maximum of 1000 IP/CIDR values, where one CIDR counts as a single value.
        Attempts to exceed that number return error 400 with `error_code` value
        `QUOTA_EXCEEDED`. * If the updated list would block the calling user's
        current IP, error 400 is returned with `error_code` value
        `INVALID_STATE`.

        It can take a few minutes for the changes to take effect. Note that your
        resulting IP access list has no effect until you enable the feature. See
        :method:workspaceconf/setStatus."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.0/ip-access-lists/{request.ip_access_list_id}",
            query=query,
            body=body,
        )

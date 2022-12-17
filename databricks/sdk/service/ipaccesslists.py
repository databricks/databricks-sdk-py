# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class CreateIpAccessList:
    ip_addresses: "List[str]"
    label: str
    list_type: "ListType"

    def as_dict(self) -> dict:
        body = {}
        if self.ip_addresses:
            body["ip_addresses"] = [v for v in self.ip_addresses]
        if self.label:
            body["label"] = self.label
        if self.list_type:
            body["list_type"] = self.list_type.value

        return body

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

    def as_dict(self) -> dict:
        body = {}
        if self.ip_access_list:
            body["ip_access_list"] = self.ip_access_list.as_dict()

        return body

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

    ip_access_list_id: str  # path


@dataclass
class FetchIpAccessListResponse:
    ip_access_list: "IpAccessListInfo"

    def as_dict(self) -> dict:
        body = {}
        if self.ip_access_list:
            body["ip_access_list"] = self.ip_access_list.as_dict()

        return body

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

    ip_access_list_id: str  # path


@dataclass
class GetIpAccessListResponse:
    ip_access_lists: "List[IpAccessListInfo]"

    def as_dict(self) -> dict:
        body = {}
        if self.ip_access_lists:
            body["ip_access_lists"] = [v.as_dict() for v in self.ip_access_lists]

        return body

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
    address_count: int
    created_at: int
    created_by: int
    enabled: bool
    ip_addresses: "List[str]"
    label: str
    list_id: str
    list_type: "ListType"
    updated_at: int
    updated_by: int

    def as_dict(self) -> dict:
        body = {}
        if self.address_count:
            body["address_count"] = self.address_count
        if self.created_at:
            body["created_at"] = self.created_at
        if self.created_by:
            body["created_by"] = self.created_by
        if self.enabled:
            body["enabled"] = self.enabled
        if self.ip_addresses:
            body["ip_addresses"] = [v for v in self.ip_addresses]
        if self.label:
            body["label"] = self.label
        if self.list_id:
            body["list_id"] = self.list_id
        if self.list_type:
            body["list_type"] = self.list_type.value
        if self.updated_at:
            body["updated_at"] = self.updated_at
        if self.updated_by:
            body["updated_by"] = self.updated_by

        return body

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
    enabled: bool
    ip_access_list_id: str  # path
    ip_addresses: "List[str]"
    label: str
    list_id: str
    list_type: "ListType"

    def as_dict(self) -> dict:
        body = {}
        if self.enabled:
            body["enabled"] = self.enabled
        if self.ip_access_list_id:
            body["ip_access_list_id"] = self.ip_access_list_id
        if self.ip_addresses:
            body["ip_addresses"] = [v for v in self.ip_addresses]
        if self.label:
            body["label"] = self.label
        if self.list_id:
            body["list_id"] = self.list_id
        if self.list_type:
            body["list_type"] = self.list_type.value

        return body

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
    enabled: bool
    ip_access_list_id: str  # path
    ip_addresses: "List[str]"
    label: str
    list_id: str
    list_type: "ListType"

    def as_dict(self) -> dict:
        body = {}
        if self.enabled:
            body["enabled"] = self.enabled
        if self.ip_access_list_id:
            body["ip_access_list_id"] = self.ip_access_list_id
        if self.ip_addresses:
            body["ip_addresses"] = [v for v in self.ip_addresses]
        if self.label:
            body["label"] = self.label
        if self.list_id:
            body["list_id"] = self.list_id
        if self.list_type:
            body["list_type"] = self.list_type.value

        return body

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

    def create(
        self, label: str, list_type: ListType, ip_addresses: List[str], **kwargs
    ) -> CreateIpAccessListResponse:
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
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = CreateIpAccessList(
                ip_addresses=ip_addresses, label=label, list_type=list_type
            )
        body = request.as_dict()

        json = self._api.do("POST", "/api/2.0/ip-access-lists", body=body)
        return CreateIpAccessListResponse.from_dict(json)

    def delete(self, ip_access_list_id: str, **kwargs):
        """Delete access list.

        Deletes an IP access list, specified by its list ID."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = Delete(ip_access_list_id=ip_access_list_id)

        self._api.do("DELETE", f"/api/2.0/ip-access-lists/{request.ip_access_list_id}")

    def get(self, ip_access_list_id: str, **kwargs) -> FetchIpAccessListResponse:
        """Get access list.

        Gets an IP access list, specified by its list ID."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = Get(ip_access_list_id=ip_access_list_id)

        json = self._api.do(
            "GET", f"/api/2.0/ip-access-lists/{request.ip_access_list_id}"
        )
        return FetchIpAccessListResponse.from_dict(json)

    def list(self) -> GetIpAccessListResponse:
        """Get access lists.

        Gets all IP access lists for the specified workspace."""

        json = self._api.do("GET", "/api/2.0/ip-access-lists")
        return GetIpAccessListResponse.from_dict(json)

    def replace(
        self,
        label: str,
        list_type: ListType,
        ip_addresses: List[str],
        enabled: bool,
        ip_access_list_id: str,
        *,
        list_id: str = None,
        **kwargs,
    ):
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
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ReplaceIpAccessList(
                enabled=enabled,
                ip_access_list_id=ip_access_list_id,
                ip_addresses=ip_addresses,
                label=label,
                list_id=list_id,
                list_type=list_type,
            )
        body = request.as_dict()

        self._api.do(
            "PUT", f"/api/2.0/ip-access-lists/{request.ip_access_list_id}", body=body
        )

    def update(
        self,
        label: str,
        list_type: ListType,
        ip_addresses: List[str],
        enabled: bool,
        ip_access_list_id: str,
        *,
        list_id: str = None,
        **kwargs,
    ):
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
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = UpdateIpAccessList(
                enabled=enabled,
                ip_access_list_id=ip_access_list_id,
                ip_addresses=ip_addresses,
                label=label,
                list_id=list_id,
                list_type=list_type,
            )
        body = request.as_dict()

        self._api.do(
            "PATCH", f"/api/2.0/ip-access-lists/{request.ip_access_list_id}", body=body
        )

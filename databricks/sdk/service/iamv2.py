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
class Group:
    """The details of a Group resource."""

    account_id: Optional[str] = None
    """The parent account ID for group in Databricks."""

    external_id: Optional[str] = None
    """ExternalId of the group in the customer's IdP."""

    group_name: Optional[str] = None
    """Display name of the group."""

    internal_id: Optional[int] = None
    """Internal group ID of the group in Databricks."""

    def as_dict(self) -> dict:
        """Serializes the Group into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.internal_id is not None:
            body["internal_id"] = self.internal_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Group into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.internal_id is not None:
            body["internal_id"] = self.internal_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Group:
        """Deserializes the Group from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            external_id=d.get("external_id", None),
            group_name=d.get("group_name", None),
            internal_id=d.get("internal_id", None),
        )


@dataclass
class ListGroupsResponse:
    """TODO: Write description later when this method is implemented"""

    groups: Optional[List[Group]] = None

    next_page_token: Optional[str] = None
    """A token, which can be sent as page_token to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    def as_dict(self) -> dict:
        """Serializes the ListGroupsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.groups:
            body["groups"] = [v.as_dict() for v in self.groups]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListGroupsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.groups:
            body["groups"] = self.groups
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListGroupsResponse:
        """Deserializes the ListGroupsResponse from a dictionary."""
        return cls(groups=_repeated_dict(d, "groups", Group), next_page_token=d.get("next_page_token", None))


@dataclass
class ListServicePrincipalsResponse:
    """TODO: Write description later when this method is implemented"""

    next_page_token: Optional[str] = None
    """A token, which can be sent as page_token to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    service_principals: Optional[List[ServicePrincipal]] = None

    def as_dict(self) -> dict:
        """Serializes the ListServicePrincipalsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.service_principals:
            body["service_principals"] = [v.as_dict() for v in self.service_principals]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListServicePrincipalsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.service_principals:
            body["service_principals"] = self.service_principals
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListServicePrincipalsResponse:
        """Deserializes the ListServicePrincipalsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            service_principals=_repeated_dict(d, "service_principals", ServicePrincipal),
        )


@dataclass
class ListUsersResponse:
    """TODO: Write description later when this method is implemented"""

    next_page_token: Optional[str] = None
    """A token, which can be sent as page_token to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    users: Optional[List[User]] = None

    def as_dict(self) -> dict:
        """Serializes the ListUsersResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.users:
            body["users"] = [v.as_dict() for v in self.users]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListUsersResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.users:
            body["users"] = self.users
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListUsersResponse:
        """Deserializes the ListUsersResponse from a dictionary."""
        return cls(next_page_token=d.get("next_page_token", None), users=_repeated_dict(d, "users", User))


@dataclass
class ListWorkspaceAccessDetailsResponse:
    """TODO: Write description later when this method is implemented"""

    next_page_token: Optional[str] = None
    """A token, which can be sent as page_token to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    workspace_access_details: Optional[List[WorkspaceAccessDetail]] = None

    def as_dict(self) -> dict:
        """Serializes the ListWorkspaceAccessDetailsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.workspace_access_details:
            body["workspace_access_details"] = [v.as_dict() for v in self.workspace_access_details]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListWorkspaceAccessDetailsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.workspace_access_details:
            body["workspace_access_details"] = self.workspace_access_details
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListWorkspaceAccessDetailsResponse:
        """Deserializes the ListWorkspaceAccessDetailsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            workspace_access_details=_repeated_dict(d, "workspace_access_details", WorkspaceAccessDetail),
        )


class PrincipalType(Enum):
    """The type of the principal (user/sp/group)."""

    GROUP = "GROUP"
    SERVICE_PRINCIPAL = "SERVICE_PRINCIPAL"
    USER = "USER"


@dataclass
class ServicePrincipal:
    """The details of a ServicePrincipal resource."""

    account_id: Optional[str] = None
    """The parent account ID for the service principal in Databricks."""

    account_sp_status: Optional[State] = None
    """The activity status of a sp in a Databricks account."""

    application_id: Optional[str] = None
    """Application ID of the service principal."""

    display_name: Optional[str] = None
    """Display name of the service principal."""

    external_id: Optional[str] = None
    """ExternalId of the service principal in the customer's IdP."""

    internal_id: Optional[int] = None
    """Internal service principal ID of the service principal in Databricks."""

    def as_dict(self) -> dict:
        """Serializes the ServicePrincipal into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.account_sp_status is not None:
            body["account_sp_status"] = self.account_sp_status.value
        if self.application_id is not None:
            body["application_id"] = self.application_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.internal_id is not None:
            body["internal_id"] = self.internal_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServicePrincipal into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.account_sp_status is not None:
            body["account_sp_status"] = self.account_sp_status
        if self.application_id is not None:
            body["application_id"] = self.application_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.internal_id is not None:
            body["internal_id"] = self.internal_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ServicePrincipal:
        """Deserializes the ServicePrincipal from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            account_sp_status=_enum(d, "account_sp_status", State),
            application_id=d.get("application_id", None),
            display_name=d.get("display_name", None),
            external_id=d.get("external_id", None),
            internal_id=d.get("internal_id", None),
        )


class State(Enum):
    """The activity status of a user or service principal in a Databricks account or workspace."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


@dataclass
class SyncGroupResponse:
    group: Optional[Group] = None
    """The group that was synced."""

    def as_dict(self) -> dict:
        """Serializes the SyncGroupResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group:
            body["group"] = self.group.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncGroupResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.group:
            body["group"] = self.group
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncGroupResponse:
        """Deserializes the SyncGroupResponse from a dictionary."""
        return cls(group=_from_dict(d, "group", Group))


@dataclass
class SyncServicePrincipalResponse:
    service_principal: Optional[ServicePrincipal] = None
    """The service principal that was synced."""

    def as_dict(self) -> dict:
        """Serializes the SyncServicePrincipalResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.service_principal:
            body["service_principal"] = self.service_principal.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncServicePrincipalResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.service_principal:
            body["service_principal"] = self.service_principal
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncServicePrincipalResponse:
        """Deserializes the SyncServicePrincipalResponse from a dictionary."""
        return cls(service_principal=_from_dict(d, "service_principal", ServicePrincipal))


@dataclass
class SyncUserResponse:
    user: Optional[User] = None
    """The user that was synced."""

    def as_dict(self) -> dict:
        """Serializes the SyncUserResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.user:
            body["user"] = self.user.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncUserResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.user:
            body["user"] = self.user
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncUserResponse:
        """Deserializes the SyncUserResponse from a dictionary."""
        return cls(user=_from_dict(d, "user", User))


@dataclass
class User:
    """The details of a User resource."""

    username: str
    """Username/email of the user."""

    account_id: Optional[str] = None
    """The accountId parent of the user in Databricks."""

    account_user_status: Optional[State] = None
    """The activity status of a user in a Databricks account."""

    external_id: Optional[str] = None
    """ExternalId of the user in the customer's IdP."""

    internal_id: Optional[int] = None
    """Internal userId of the user in Databricks."""

    name: Optional[UserName] = None

    def as_dict(self) -> dict:
        """Serializes the User into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.account_user_status is not None:
            body["account_user_status"] = self.account_user_status.value
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.internal_id is not None:
            body["internal_id"] = self.internal_id
        if self.name:
            body["name"] = self.name.as_dict()
        if self.username is not None:
            body["username"] = self.username
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the User into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.account_user_status is not None:
            body["account_user_status"] = self.account_user_status
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.internal_id is not None:
            body["internal_id"] = self.internal_id
        if self.name:
            body["name"] = self.name
        if self.username is not None:
            body["username"] = self.username
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> User:
        """Deserializes the User from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            account_user_status=_enum(d, "account_user_status", State),
            external_id=d.get("external_id", None),
            internal_id=d.get("internal_id", None),
            name=_from_dict(d, "name", UserName),
            username=d.get("username", None),
        )


@dataclass
class UserName:
    family_name: Optional[str] = None

    given_name: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the UserName into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.family_name is not None:
            body["family_name"] = self.family_name
        if self.given_name is not None:
            body["given_name"] = self.given_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UserName into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.family_name is not None:
            body["family_name"] = self.family_name
        if self.given_name is not None:
            body["given_name"] = self.given_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UserName:
        """Deserializes the UserName from a dictionary."""
        return cls(family_name=d.get("family_name", None), given_name=d.get("given_name", None))


@dataclass
class WorkspaceAccessDetail:
    """The details of a principal's access to a workspace."""

    access_type: Optional[WorkspaceAccessDetailAccessType] = None

    account_id: Optional[str] = None
    """The account ID parent of the workspace where the principal has access."""

    permissions: Optional[List[WorkspacePermission]] = None
    """The permissions granted to the principal in the workspace."""

    principal_id: Optional[int] = None
    """The internal ID of the principal (user/sp/group) in Databricks."""

    principal_type: Optional[PrincipalType] = None

    status: Optional[State] = None
    """The activity status of the principal in the workspace. Not applicable for groups at the moment."""

    workspace_id: Optional[int] = None
    """The workspace ID where the principal has access."""

    def as_dict(self) -> dict:
        """Serializes the WorkspaceAccessDetail into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_type is not None:
            body["access_type"] = self.access_type.value
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.permissions:
            body["permissions"] = [v.value for v in self.permissions]
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type.value
        if self.status is not None:
            body["status"] = self.status.value
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WorkspaceAccessDetail into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.access_type is not None:
            body["access_type"] = self.access_type
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.permissions:
            body["permissions"] = self.permissions
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type
        if self.status is not None:
            body["status"] = self.status
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WorkspaceAccessDetail:
        """Deserializes the WorkspaceAccessDetail from a dictionary."""
        return cls(
            access_type=_enum(d, "access_type", WorkspaceAccessDetailAccessType),
            account_id=d.get("account_id", None),
            permissions=_repeated_enum(d, "permissions", WorkspacePermission),
            principal_id=d.get("principal_id", None),
            principal_type=_enum(d, "principal_type", PrincipalType),
            status=_enum(d, "status", State),
            workspace_id=d.get("workspace_id", None),
        )


class WorkspaceAccessDetailAccessType(Enum):
    """The type of access the principal has to the workspace."""

    DIRECT = "DIRECT"
    INDIRECT = "INDIRECT"


class WorkspaceAccessDetailView(Enum):
    """Controls what fields are returned in the GetWorkspaceAccessDetail response."""

    BASIC = "BASIC"
    FULL = "FULL"


class WorkspacePermission(Enum):
    """The type of permission a principal has to a workspace (admin/user)."""

    ADMIN_PERMISSION = "ADMIN_PERMISSION"
    USER_PERMISSION = "USER_PERMISSION"


class AccountIamV2API:
    """These APIs are used to manage identities and the workspace access of these identities in <Databricks>."""

    def __init__(self, api_client):
        self._api = api_client

    def create_group(self, group: Group) -> Group:
        """TODO: Write description later when this method is implemented

        :param group: :class:`Group`
          Required. Group to be created in <Databricks>

        :returns: :class:`Group`
        """
        body = group.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST", f"/api/2.0/identity/accounts/{self._api.account_id}/groups", body=body, headers=headers
        )
        return Group.from_dict(res)

    def create_service_principal(self, service_principal: ServicePrincipal) -> ServicePrincipal:
        """TODO: Write description later when this method is implemented

        :param service_principal: :class:`ServicePrincipal`
          Required. Service principal to be created in <Databricks>

        :returns: :class:`ServicePrincipal`
        """
        body = service_principal.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST", f"/api/2.0/identity/accounts/{self._api.account_id}/servicePrincipals", body=body, headers=headers
        )
        return ServicePrincipal.from_dict(res)

    def create_user(self, user: User) -> User:
        """TODO: Write description later when this method is implemented

        :param user: :class:`User`
          Required. User to be created in <Databricks>

        :returns: :class:`User`
        """
        body = user.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST", f"/api/2.0/identity/accounts/{self._api.account_id}/users", body=body, headers=headers
        )
        return User.from_dict(res)

    def create_workspace_access_detail(
        self, parent: str, workspace_access_detail: WorkspaceAccessDetail
    ) -> WorkspaceAccessDetail:
        """TODO: Write description later when this method is implemented

        :param parent: str
          Required. The parent path for workspace access detail.
        :param workspace_access_detail: :class:`WorkspaceAccessDetail`
          Required. Workspace access detail to be created in <Databricks>.

        :returns: :class:`WorkspaceAccessDetail`
        """
        body = workspace_access_detail.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{parent}/workspaceAccessDetails",
            body=body,
            headers=headers,
        )
        return WorkspaceAccessDetail.from_dict(res)

    def delete_group(self, internal_id: int):
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the group in Databricks.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do(
            "DELETE", f"/api/2.0/identity/accounts/{self._api.account_id}/groups/{internal_id}", headers=headers
        )

    def delete_service_principal(self, internal_id: int):
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the service principal in Databricks.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do(
            "DELETE",
            f"/api/2.0/identity/accounts/{self._api.account_id}/servicePrincipals/{internal_id}",
            headers=headers,
        )

    def delete_user(self, internal_id: int):
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the user in Databricks.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do(
            "DELETE", f"/api/2.0/identity/accounts/{self._api.account_id}/users/{internal_id}", headers=headers
        )

    def delete_workspace_access_detail(self, workspace_id: int, principal_id: int):
        """TODO: Write description later when this method is implemented

        :param workspace_id: int
          The workspace ID where the principal has access.
        :param principal_id: int
          Required. ID of the principal in Databricks to delete workspace access for.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do(
            "DELETE",
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspaceAccessDetails/{principal_id}",
            headers=headers,
        )

    def get_group(self, internal_id: int) -> Group:
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the group in Databricks.

        :returns: :class:`Group`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET", f"/api/2.0/identity/accounts/{self._api.account_id}/groups/{internal_id}", headers=headers
        )
        return Group.from_dict(res)

    def get_service_principal(self, internal_id: int) -> ServicePrincipal:
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the service principal in Databricks.

        :returns: :class:`ServicePrincipal`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET", f"/api/2.0/identity/accounts/{self._api.account_id}/servicePrincipals/{internal_id}", headers=headers
        )
        return ServicePrincipal.from_dict(res)

    def get_user(self, internal_id: int) -> User:
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the user in Databricks.

        :returns: :class:`User`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET", f"/api/2.0/identity/accounts/{self._api.account_id}/users/{internal_id}", headers=headers
        )
        return User.from_dict(res)

    def get_workspace_access_detail(
        self, workspace_id: int, principal_id: int, *, view: Optional[WorkspaceAccessDetailView] = None
    ) -> WorkspaceAccessDetail:
        """Returns the access details for a principal in a workspace. Allows for checking access details for any
        provisioned principal (user, service principal, or group) in a workspace. * Provisioned principal here
        refers to one that has been synced into Databricks from the customer's IdP or added explicitly to
        Databricks via SCIM/UI. Allows for passing in a "view" parameter to control what fields are returned
        (BASIC by default or FULL).

        :param workspace_id: int
          Required. The workspace ID for which the access details are being requested.
        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the access details are being
          requested.
        :param view: :class:`WorkspaceAccessDetailView` (optional)
          Controls what fields are returned.

        :returns: :class:`WorkspaceAccessDetail`
        """

        query = {}
        if view is not None:
            query["view"] = view.value
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET",
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspaceAccessDetails/{principal_id}",
            query=query,
            headers=headers,
        )
        return WorkspaceAccessDetail.from_dict(res)

    def list_groups(self, *, page_size: Optional[int] = None, page_token: Optional[str] = None) -> ListGroupsResponse:
        """TODO: Write description later when this method is implemented

        :param page_size: int (optional)
          The maximum number of groups to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListGroups call. Provide this to retrieve the subsequent
          page.

        :returns: :class:`ListGroupsResponse`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET", f"/api/2.0/identity/accounts/{self._api.account_id}/groups", query=query, headers=headers
        )
        return ListGroupsResponse.from_dict(res)

    def list_service_principals(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> ListServicePrincipalsResponse:
        """TODO: Write description later when this method is implemented

        :param page_size: int (optional)
          The maximum number of service principals to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListServicePrincipals call. Provide this to retrieve the
          subsequent page.

        :returns: :class:`ListServicePrincipalsResponse`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET", f"/api/2.0/identity/accounts/{self._api.account_id}/servicePrincipals", query=query, headers=headers
        )
        return ListServicePrincipalsResponse.from_dict(res)

    def list_users(self, *, page_size: Optional[int] = None, page_token: Optional[str] = None) -> ListUsersResponse:
        """TODO: Write description later when this method is implemented

        :param page_size: int (optional)
          The maximum number of users to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListUsers call. Provide this to retrieve the subsequent page.

        :returns: :class:`ListUsersResponse`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET", f"/api/2.0/identity/accounts/{self._api.account_id}/users", query=query, headers=headers
        )
        return ListUsersResponse.from_dict(res)

    def list_workspace_access_details(
        self, workspace_id: int, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> ListWorkspaceAccessDetailsResponse:
        """TODO: Write description later when this method is implemented

        :param workspace_id: int
          The workspace ID for which the workspace access details are being fetched.
        :param page_size: int (optional)
          The maximum number of workspace access details to return. The service may return fewer than this
          value.
        :param page_token: str (optional)
          A page token, received from a previous ListWorkspaceAccessDetails call. Provide this to retrieve the
          subsequent page.

        :returns: :class:`ListWorkspaceAccessDetailsResponse`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET",
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspaceAccessDetails",
            query=query,
            headers=headers,
        )
        return ListWorkspaceAccessDetailsResponse.from_dict(res)

    def sync_group(self, external_id: str) -> SyncGroupResponse:
        """Syncs a group with the given external ID from the customer's IdP. If the group does not exist, it will
        be created in the account. If the customer is not onboarded onto Automatic Identity Management (AIM),
        this will return an error. Synced information is cached for 30 minutes, so subsequent calls to this
        method will not result in a full sync unless the cache is stale. If this is triggered while the cache
        is still valid, it will return the cached group information.

        :param external_id: str
          Required. The external ID of the group in the customer's IdP.

        :returns: :class:`SyncGroupResponse`
        """
        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/identity/accounts/{self._api.account_id}/groups/syncByExternalId",
            body=body,
            headers=headers,
        )
        return SyncGroupResponse.from_dict(res)

    def sync_service_principal(self, external_id: str) -> SyncServicePrincipalResponse:
        """Syncs a sp with the given external ID from the customer's IdP. If the sp does not exist, it will be
        created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will return
        an error. Synced information is cached for 30 minutes, so subsequent calls to this method will not
        result in a full sync unless the cache is stale. If this is triggered while the cache is still valid,
        it will return the cached SP information.

        :param external_id: str
          Required. The external ID of the service principal in the customer's IdP.

        :returns: :class:`SyncServicePrincipalResponse`
        """
        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/identity/accounts/{self._api.account_id}/servicePrincipals/syncByExternalId",
            body=body,
            headers=headers,
        )
        return SyncServicePrincipalResponse.from_dict(res)

    def sync_user(self, external_id: str) -> SyncUserResponse:
        """Syncs a user with the given external ID from the customer's IdP. If the user does not exist, it will
        be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will
        return an error. Synced information is cached for 30 minutes, so subsequent calls to this method will
        not result in a full sync unless the cache is stale. If this is triggered while the cache is still
        valid, it will return the cached user information.

        :param external_id: str
          Required. The external ID of the user in the customer's IdP.

        :returns: :class:`SyncUserResponse`
        """
        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/identity/accounts/{self._api.account_id}/users/syncByExternalId",
            body=body,
            headers=headers,
        )
        return SyncUserResponse.from_dict(res)

    def update_group(self, internal_id: int, group: Group, update_mask: str) -> Group:
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the group in Databricks.
        :param group: :class:`Group`
          Required. Group to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`Group`
        """
        body = group.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "PATCH",
            f"/api/2.0/identity/accounts/{self._api.account_id}/groups/{internal_id}",
            query=query,
            body=body,
            headers=headers,
        )
        return Group.from_dict(res)

    def update_service_principal(
        self, internal_id: int, service_principal: ServicePrincipal, update_mask: str
    ) -> ServicePrincipal:
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the service principal in Databricks.
        :param service_principal: :class:`ServicePrincipal`
          Required. Service Principal to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`ServicePrincipal`
        """
        body = service_principal.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "PATCH",
            f"/api/2.0/identity/accounts/{self._api.account_id}/servicePrincipals/{internal_id}",
            query=query,
            body=body,
            headers=headers,
        )
        return ServicePrincipal.from_dict(res)

    def update_user(self, internal_id: int, user: User, update_mask: str) -> User:
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the user in Databricks.
        :param user: :class:`User`
          Required. User to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`User`
        """
        body = user.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "PATCH",
            f"/api/2.0/identity/accounts/{self._api.account_id}/users/{internal_id}",
            query=query,
            body=body,
            headers=headers,
        )
        return User.from_dict(res)

    def update_workspace_access_detail(
        self, workspace_id: int, principal_id: int, workspace_access_detail: WorkspaceAccessDetail, update_mask: str
    ) -> WorkspaceAccessDetail:
        """TODO: Write description later when this method is implemented

        :param workspace_id: int
          Required. The workspace ID for which the workspace access detail is being updated.
        :param principal_id: int
          Required. ID of the principal in Databricks.
        :param workspace_access_detail: :class:`WorkspaceAccessDetail`
          Required. Workspace access detail to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`WorkspaceAccessDetail`
        """
        body = workspace_access_detail.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "PATCH",
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspaceAccessDetails/{principal_id}",
            query=query,
            body=body,
            headers=headers,
        )
        return WorkspaceAccessDetail.from_dict(res)


class WorkspaceIamV2API:
    """These APIs are used to manage identities and the workspace access of these identities in <Databricks>."""

    def __init__(self, api_client):
        self._api = api_client

    def create_group_proxy(self, group: Group) -> Group:
        """TODO: Write description later when this method is implemented

        :param group: :class:`Group`
          Required. Group to be created in <Databricks>

        :returns: :class:`Group`
        """
        body = group.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/identity/groups", body=body, headers=headers)
        return Group.from_dict(res)

    def create_service_principal_proxy(self, service_principal: ServicePrincipal) -> ServicePrincipal:
        """TODO: Write description later when this method is implemented

        :param service_principal: :class:`ServicePrincipal`
          Required. Service principal to be created in <Databricks>

        :returns: :class:`ServicePrincipal`
        """
        body = service_principal.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/identity/servicePrincipals", body=body, headers=headers)
        return ServicePrincipal.from_dict(res)

    def create_user_proxy(self, user: User) -> User:
        """TODO: Write description later when this method is implemented

        :param user: :class:`User`
          Required. User to be created in <Databricks>

        :returns: :class:`User`
        """
        body = user.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/identity/users", body=body, headers=headers)
        return User.from_dict(res)

    def create_workspace_access_detail_local(
        self, workspace_access_detail: WorkspaceAccessDetail
    ) -> WorkspaceAccessDetail:
        """TODO: Write description later when this method is implemented

        :param workspace_access_detail: :class:`WorkspaceAccessDetail`
          Required. Workspace access detail to be created in <Databricks>.

        :returns: :class:`WorkspaceAccessDetail`
        """
        body = workspace_access_detail.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/identity/workspaceAccessDetails", body=body, headers=headers)
        return WorkspaceAccessDetail.from_dict(res)

    def delete_group_proxy(self, internal_id: int):
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the group in Databricks.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/identity/groups/{internal_id}", headers=headers)

    def delete_service_principal_proxy(self, internal_id: int):
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the service principal in Databricks.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/identity/servicePrincipals/{internal_id}", headers=headers)

    def delete_user_proxy(self, internal_id: int):
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the user in Databricks.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/identity/users/{internal_id}", headers=headers)

    def delete_workspace_access_detail_local(self, principal_id: int):
        """TODO: Write description later when this method is implemented

        :param principal_id: int
          Required. ID of the principal in Databricks.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/identity/workspaceAccessDetails/{principal_id}", headers=headers)

    def get_group_proxy(self, internal_id: int) -> Group:
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the group in Databricks.

        :returns: :class:`Group`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/groups/{internal_id}", headers=headers)
        return Group.from_dict(res)

    def get_service_principal_proxy(self, internal_id: int) -> ServicePrincipal:
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the service principal in Databricks.

        :returns: :class:`ServicePrincipal`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/servicePrincipals/{internal_id}", headers=headers)
        return ServicePrincipal.from_dict(res)

    def get_user_proxy(self, internal_id: int) -> User:
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the user in Databricks.

        :returns: :class:`User`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/users/{internal_id}", headers=headers)
        return User.from_dict(res)

    def get_workspace_access_detail_local(
        self, principal_id: int, *, view: Optional[WorkspaceAccessDetailView] = None
    ) -> WorkspaceAccessDetail:
        """Returns the access details for a principal in the current workspace. Allows for checking access
        details for any provisioned principal (user, service principal, or group) in the current workspace. *
        Provisioned principal here refers to one that has been synced into Databricks from the customer's IdP
        or added explicitly to Databricks via SCIM/UI. Allows for passing in a "view" parameter to control
        what fields are returned (BASIC by default or FULL).

        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the access details are being
          requested.
        :param view: :class:`WorkspaceAccessDetailView` (optional)
          Controls what fields are returned.

        :returns: :class:`WorkspaceAccessDetail`
        """

        query = {}
        if view is not None:
            query["view"] = view.value
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET", f"/api/2.0/identity/workspaceAccessDetails/{principal_id}", query=query, headers=headers
        )
        return WorkspaceAccessDetail.from_dict(res)

    def list_groups_proxy(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> ListGroupsResponse:
        """TODO: Write description later when this method is implemented

        :param page_size: int (optional)
          The maximum number of groups to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListGroups call. Provide this to retrieve the subsequent
          page.

        :returns: :class:`ListGroupsResponse`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", "/api/2.0/identity/groups", query=query, headers=headers)
        return ListGroupsResponse.from_dict(res)

    def list_service_principals_proxy(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> ListServicePrincipalsResponse:
        """TODO: Write description later when this method is implemented

        :param page_size: int (optional)
          The maximum number of sps to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListServicePrincipals call. Provide this to retrieve the
          subsequent page.

        :returns: :class:`ListServicePrincipalsResponse`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", "/api/2.0/identity/servicePrincipals", query=query, headers=headers)
        return ListServicePrincipalsResponse.from_dict(res)

    def list_users_proxy(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> ListUsersResponse:
        """TODO: Write description later when this method is implemented

        :param page_size: int (optional)
          The maximum number of users to return. The service may return fewer than this value.
        :param page_token: str (optional)
          A page token, received from a previous ListUsers call. Provide this to retrieve the subsequent page.

        :returns: :class:`ListUsersResponse`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", "/api/2.0/identity/users", query=query, headers=headers)
        return ListUsersResponse.from_dict(res)

    def list_workspace_access_details_local(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> ListWorkspaceAccessDetailsResponse:
        """TODO: Write description later when this method is implemented

        :param page_size: int (optional)
          The maximum number of workspace access details to return. The service may return fewer than this
          value.
        :param page_token: str (optional)
          A page token, received from a previous ListWorkspaceAccessDetails call. Provide this to retrieve the
          subsequent page.

        :returns: :class:`ListWorkspaceAccessDetailsResponse`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", "/api/2.0/identity/workspaceAccessDetails", query=query, headers=headers)
        return ListWorkspaceAccessDetailsResponse.from_dict(res)

    def sync_group_proxy(self, external_id: str) -> SyncGroupResponse:
        """Syncs a group with the given external ID from the customer's IdP. If the group does not exist, it will
        be created in the account. If the customer is not onboarded onto Automatic Identity Management (AIM),
        this will return an error. Synced information is cached for 30 minutes, so subsequent calls to this
        method will not result in a full sync unless the cache is stale. If this is triggered while the cache
        is still valid, it will return the cached group information.

        :param external_id: str
          Required. The external ID of the group in the customer's IdP.

        :returns: :class:`SyncGroupResponse`
        """
        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/identity/groups/syncByExternalId", body=body, headers=headers)
        return SyncGroupResponse.from_dict(res)

    def sync_service_principal_proxy(self, external_id: str) -> SyncServicePrincipalResponse:
        """Syncs a sp with the given external ID from the customer's IdP. If the sp does not exist, it will be
        created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will return
        an error. Synced information is cached for 30 minutes, so subsequent calls to this method will not
        result in a full sync unless the cache is stale. If this is triggered while the cache is still valid,
        it will return the cached SP information.

        :param external_id: str
          Required. The external ID of the service principal in the customer's IdP.

        :returns: :class:`SyncServicePrincipalResponse`
        """
        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/identity/servicePrincipals/syncByExternalId", body=body, headers=headers)
        return SyncServicePrincipalResponse.from_dict(res)

    def sync_user_proxy(self, external_id: str) -> SyncUserResponse:
        """Syncs a user with the given external ID from the customer's IdP. If the user does not exist, it will
        be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will
        return an error. Synced information is cached for 30 minutes, so subsequent calls to this method will
        not result in a full sync unless the cache is stale. If this is triggered while the cache is still
        valid, it will return the cached user information.

        :param external_id: str
          Required. The external ID of the user in the customer's IdP.

        :returns: :class:`SyncUserResponse`
        """
        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/identity/users/syncByExternalId", body=body, headers=headers)
        return SyncUserResponse.from_dict(res)

    def update_group_proxy(self, internal_id: int, group: Group, update_mask: str) -> Group:
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the group in Databricks.
        :param group: :class:`Group`
          Required. Group to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`Group`
        """
        body = group.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/identity/groups/{internal_id}", query=query, body=body, headers=headers)
        return Group.from_dict(res)

    def update_service_principal_proxy(
        self, internal_id: int, service_principal: ServicePrincipal, update_mask: str
    ) -> ServicePrincipal:
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the service principal in Databricks.
        :param service_principal: :class:`ServicePrincipal`
          Required. Service principal to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`ServicePrincipal`
        """
        body = service_principal.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "PATCH", f"/api/2.0/identity/servicePrincipals/{internal_id}", query=query, body=body, headers=headers
        )
        return ServicePrincipal.from_dict(res)

    def update_user_proxy(self, internal_id: int, user: User, update_mask: str) -> User:
        """TODO: Write description later when this method is implemented

        :param internal_id: int
          Required. Internal ID of the user in Databricks.
        :param user: :class:`User`
          Required. User to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`User`
        """
        body = user.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/identity/users/{internal_id}", query=query, body=body, headers=headers)
        return User.from_dict(res)

    def update_workspace_access_detail_local(
        self, principal_id: int, workspace_access_detail: WorkspaceAccessDetail, update_mask: str
    ) -> WorkspaceAccessDetail:
        """TODO: Write description later when this method is implemented

        :param principal_id: int
          Required. ID of the principal in Databricks.
        :param workspace_access_detail: :class:`WorkspaceAccessDetail`
          Required. WorkspaceAccessDetail to be updated in <Databricks>
        :param update_mask: str
          Optional. The list of fields to update.

        :returns: :class:`WorkspaceAccessDetail`
        """
        body = workspace_access_detail.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "PATCH", f"/api/2.0/identity/workspaceAccessDetails/{principal_id}", query=query, body=body, headers=headers
        )
        return WorkspaceAccessDetail.from_dict(res)

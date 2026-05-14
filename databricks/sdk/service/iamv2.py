# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional

from databricks.sdk.common.types.fieldmask import FieldMask
from databricks.sdk.service._internal import (_enum, _from_dict,
                                              _repeated_dict, _repeated_enum)

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


class Entitlement(Enum):

    ALLOW_CLUSTER_CREATE = "ALLOW_CLUSTER_CREATE"
    ALLOW_INSTANCE_POOL_CREATE = "ALLOW_INSTANCE_POOL_CREATE"
    DATABRICKS_SQL_ACCESS = "DATABRICKS_SQL_ACCESS"
    WORKSPACE_ACCESS = "WORKSPACE_ACCESS"
    WORKSPACE_ADMIN = "WORKSPACE_ADMIN"
    WORKSPACE_CONSUME = "WORKSPACE_CONSUME"


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
class ListWorkspaceAssignmentDetailsResponse:
    """Response message for listing workspace assignment details."""

    next_page_token: Optional[str] = None
    """A token, which can be sent as page_token to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    workspace_assignment_details: Optional[List[WorkspaceAssignmentDetail]] = None

    def as_dict(self) -> dict:
        """Serializes the ListWorkspaceAssignmentDetailsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.workspace_assignment_details:
            body["workspace_assignment_details"] = [v.as_dict() for v in self.workspace_assignment_details]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListWorkspaceAssignmentDetailsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.workspace_assignment_details:
            body["workspace_assignment_details"] = self.workspace_assignment_details
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListWorkspaceAssignmentDetailsResponse:
        """Deserializes the ListWorkspaceAssignmentDetailsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            workspace_assignment_details=_repeated_dict(d, "workspace_assignment_details", WorkspaceAssignmentDetail),
        )


class PrincipalType(Enum):
    """The type of the principal (user/sp/group)."""

    GROUP = "GROUP"
    SERVICE_PRINCIPAL = "SERVICE_PRINCIPAL"
    USER = "USER"


@dataclass
class ResolveGroupResponse:
    group: Optional[Group] = None
    """The group that was resolved."""

    def as_dict(self) -> dict:
        """Serializes the ResolveGroupResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group:
            body["group"] = self.group.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ResolveGroupResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.group:
            body["group"] = self.group
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResolveGroupResponse:
        """Deserializes the ResolveGroupResponse from a dictionary."""
        return cls(group=_from_dict(d, "group", Group))


@dataclass
class ResolveServicePrincipalResponse:
    service_principal: Optional[ServicePrincipal] = None
    """The service principal that was resolved."""

    def as_dict(self) -> dict:
        """Serializes the ResolveServicePrincipalResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.service_principal:
            body["service_principal"] = self.service_principal.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ResolveServicePrincipalResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.service_principal:
            body["service_principal"] = self.service_principal
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResolveServicePrincipalResponse:
        """Deserializes the ResolveServicePrincipalResponse from a dictionary."""
        return cls(service_principal=_from_dict(d, "service_principal", ServicePrincipal))


@dataclass
class ResolveUserResponse:
    user: Optional[User] = None
    """The user that was resolved."""

    def as_dict(self) -> dict:
        """Serializes the ResolveUserResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.user:
            body["user"] = self.user.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ResolveUserResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.user:
            body["user"] = self.user
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResolveUserResponse:
        """Deserializes the ResolveUserResponse from a dictionary."""
        return cls(user=_from_dict(d, "user", User))


@dataclass
class ServicePrincipal:
    """The details of a ServicePrincipal resource."""

    account_id: Optional[str] = None
    """The parent account ID for the service principal in Databricks."""

    account_sp_status: Optional[State] = None
    """The activity status of a service principal in a Databricks account."""

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
class User:
    """The details of a User resource."""

    account_id: Optional[str] = None
    """The accountId parent of the user in Databricks."""

    account_user_status: Optional[State] = None
    """The activity status of a user in a Databricks account."""

    external_id: Optional[str] = None
    """ExternalId of the user in the customer's IdP."""

    internal_id: Optional[int] = None
    """Internal userId of the user in Databricks."""

    name: Optional[UserName] = None

    username: Optional[str] = None
    """Username/email of the user."""

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


@dataclass
class WorkspaceAssignmentDetail:
    """The details of a principal's assignment to a workspace."""

    principal_id: int
    """The internal ID of the principal (user/sp/group) in Databricks."""

    account_id: Optional[str] = None
    """The account ID parent of the workspace where the principal is assigned"""

    entitlements: Optional[List[Entitlement]] = None

    principal_type: Optional[PrincipalType] = None

    workspace_id: Optional[int] = None
    """The workspace ID where the principal is assigned"""

    def as_dict(self) -> dict:
        """Serializes the WorkspaceAssignmentDetail into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.entitlements:
            body["entitlements"] = [v.value for v in self.entitlements]
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type.value
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WorkspaceAssignmentDetail into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.entitlements:
            body["entitlements"] = self.entitlements
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WorkspaceAssignmentDetail:
        """Deserializes the WorkspaceAssignmentDetail from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            entitlements=_repeated_enum(d, "entitlements", Entitlement),
            principal_id=d.get("principal_id", None),
            principal_type=_enum(d, "principal_type", PrincipalType),
            workspace_id=d.get("workspace_id", None),
        )


class WorkspacePermission(Enum):
    """The type of permission a principal has to a workspace (admin/user)."""

    ADMIN_PERMISSION = "ADMIN_PERMISSION"
    USER_PERMISSION = "USER_PERMISSION"


class AccountIamV2API:
    """These APIs are used to manage identities and the workspace access of these identities in <Databricks>."""

    def __init__(self, api_client):
        self._api = api_client

    def create_workspace_assignment_detail(
        self, workspace_id: int, workspace_assignment_detail: WorkspaceAssignmentDetail
    ) -> WorkspaceAssignmentDetail:
        """Creates a workspace assignment detail for a principal. Entitlement grants are applied individually and
        non-atomically — if a failure occurs partway through, the principal will be assigned to the
        workspace but with only a subset of the requested entitlements. Use GetWorkspaceAssignmentDetail to
        confirm which entitlements were successfully granted.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment detail is being created.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be created in <Databricks>.

        :returns: :class:`WorkspaceAssignmentDetail`
        """

        body = workspace_assignment_detail.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspaceAssignmentDetails",
            body=body,
            headers=headers,
        )
        return WorkspaceAssignmentDetail.from_dict(res)

    def delete_workspace_assignment_detail(self, workspace_id: int, principal_id: int):
        """Deletes a workspace assignment detail for a principal, revoking all associated entitlements.
        Entitlement revocations are applied individually and non-atomically — if a failure occurs partway
        through, the principal remains assigned with a subset of its original entitlements, and the operation
        is safe to retry.

        :param workspace_id: int
          The workspace ID where the principal has access.
        :param principal_id: int
          Required. ID of the principal in Databricks to delete workspace assignment for.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do(
            "DELETE",
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspaceAssignmentDetails/{principal_id}",
            headers=headers,
        )

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

    def get_workspace_assignment_detail(self, workspace_id: int, principal_id: int) -> WorkspaceAssignmentDetail:
        """Returns the assignment details for a principal in a workspace.

        :param workspace_id: int
          Required. The workspace ID for which the assignment details are being requested.
        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the assignment details are
          being requested.

        :returns: :class:`WorkspaceAssignmentDetail`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET",
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspaceAssignmentDetails/{principal_id}",
            headers=headers,
        )
        return WorkspaceAssignmentDetail.from_dict(res)

    def list_workspace_assignment_details(
        self, workspace_id: int, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> ListWorkspaceAssignmentDetailsResponse:
        """Lists workspace assignment details for a workspace.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment details are being fetched.
        :param page_size: int (optional)
          The maximum number of workspace assignment details to return. The service may return fewer than this
          value.
        :param page_token: str (optional)
          A page token, received from a previous ListWorkspaceAssignmentDetails call. Provide this to retrieve
          the subsequent page.

        :returns: :class:`ListWorkspaceAssignmentDetailsResponse`
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
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspaceAssignmentDetails",
            query=query,
            headers=headers,
        )
        return ListWorkspaceAssignmentDetailsResponse.from_dict(res)

    def resolve_group(self, external_id: str) -> ResolveGroupResponse:
        """Resolves a group with the given external ID from the customer's IdP. If the group does not exist, it
        will be created in the account. If the customer is not onboarded onto Automatic Identity Management
        (AIM), this will return an error.

        :param external_id: str
          Required. The external ID of the group in the customer's IdP.

        :returns: :class:`ResolveGroupResponse`
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
            f"/api/2.0/identity/accounts/{self._api.account_id}/groups/resolveByExternalId",
            body=body,
            headers=headers,
        )
        return ResolveGroupResponse.from_dict(res)

    def resolve_service_principal(self, external_id: str) -> ResolveServicePrincipalResponse:
        """Resolves an SP with the given external ID from the customer's IdP. If the SP does not exist, it will
        be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will
        return an error.

        :param external_id: str
          Required. The external ID of the service principal in the customer's IdP.

        :returns: :class:`ResolveServicePrincipalResponse`
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
            f"/api/2.0/identity/accounts/{self._api.account_id}/servicePrincipals/resolveByExternalId",
            body=body,
            headers=headers,
        )
        return ResolveServicePrincipalResponse.from_dict(res)

    def resolve_user(self, external_id: str) -> ResolveUserResponse:
        """Resolves a user with the given external ID from the customer's IdP. If the user does not exist, it
        will be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will
        return an error.

        :param external_id: str
          Required. The external ID of the user in the customer's IdP.

        :returns: :class:`ResolveUserResponse`
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
            f"/api/2.0/identity/accounts/{self._api.account_id}/users/resolveByExternalId",
            body=body,
            headers=headers,
        )
        return ResolveUserResponse.from_dict(res)

    def update_workspace_assignment_detail(
        self,
        workspace_id: int,
        principal_id: int,
        workspace_assignment_detail: WorkspaceAssignmentDetail,
        update_mask: FieldMask,
    ) -> WorkspaceAssignmentDetail:
        """Updates the entitlements of a directly assigned principal in a workspace. Entitlement changes are
        applied individually and non-atomically — if a failure occurs partway through, only a subset of the
        requested changes may have been applied. Use GetWorkspaceAssignmentDetail to confirm the final state.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment detail is being updated.
        :param principal_id: int
          Required. ID of the principal in Databricks.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be updated in <Databricks>.
        :param update_mask: FieldMask
          Required. The list of fields to update.

        :returns: :class:`WorkspaceAssignmentDetail`
        """

        body = workspace_assignment_detail.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "PATCH",
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspaceAssignmentDetails/{principal_id}",
            query=query,
            body=body,
            headers=headers,
        )
        return WorkspaceAssignmentDetail.from_dict(res)


class WorkspaceIamV2API:
    """These APIs are used to manage identities and the workspace access of these identities in <Databricks>."""

    def __init__(self, api_client):
        self._api = api_client

    def create_workspace_assignment_detail_proxy(
        self, workspace_assignment_detail: WorkspaceAssignmentDetail
    ) -> WorkspaceAssignmentDetail:
        """Creates a workspace assignment detail for a principal (workspace-level proxy). Entitlement grants are
        applied individually and non-atomically — if a failure occurs partway through, the principal will be
        assigned to the workspace but with only a subset of the requested entitlements. Use
        GetWorkspaceAssignmentDetail to confirm which entitlements were successfully granted.

        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be created in <Databricks>.

        :returns: :class:`WorkspaceAssignmentDetail`
        """

        body = workspace_assignment_detail.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/identity/workspaceAssignmentDetails", body=body, headers=headers)
        return WorkspaceAssignmentDetail.from_dict(res)

    def delete_workspace_assignment_detail_proxy(self, principal_id: int):
        """Deletes a workspace assignment detail for a principal (workspace-level proxy), revoking all associated
        entitlements. Entitlement revocations are applied individually and non-atomically — if a failure
        occurs partway through, the principal remains assigned with a subset of its original entitlements, and
        the operation is safe to retry.

        :param principal_id: int
          Required. ID of the principal in Databricks to delete workspace assignment for.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/identity/workspaceAssignmentDetails/{principal_id}", headers=headers)

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

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do(
            "GET", f"/api/2.0/identity/workspaceAccessDetails/{principal_id}", query=query, headers=headers
        )
        return WorkspaceAccessDetail.from_dict(res)

    def get_workspace_assignment_detail_proxy(self, principal_id: int) -> WorkspaceAssignmentDetail:
        """Returns the assignment details for a principal in a workspace (workspace-level proxy).

        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the assignment details are
          being requested.

        :returns: :class:`WorkspaceAssignmentDetail`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/identity/workspaceAssignmentDetails/{principal_id}", headers=headers)
        return WorkspaceAssignmentDetail.from_dict(res)

    def list_workspace_assignment_details_proxy(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> ListWorkspaceAssignmentDetailsResponse:
        """Lists workspace assignment details for a workspace (workspace-level proxy).

        :param page_size: int (optional)
          The maximum number of workspace assignment details to return. The service may return fewer than this
          value.
        :param page_token: str (optional)
          A page token, received from a previous ListWorkspaceAssignmentDetailsProxy call. Provide this to
          retrieve the subsequent page.

        :returns: :class:`ListWorkspaceAssignmentDetailsResponse`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("GET", "/api/2.0/identity/workspaceAssignmentDetails", query=query, headers=headers)
        return ListWorkspaceAssignmentDetailsResponse.from_dict(res)

    def resolve_group_proxy(self, external_id: str) -> ResolveGroupResponse:
        """Resolves a group with the given external ID from the customer's IdP. If the group does not exist, it
        will be created in the account. If the customer is not onboarded onto Automatic Identity Management
        (AIM), this will return an error.

        :param external_id: str
          Required. The external ID of the group in the customer's IdP.

        :returns: :class:`ResolveGroupResponse`
        """

        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/identity/groups/resolveByExternalId", body=body, headers=headers)
        return ResolveGroupResponse.from_dict(res)

    def resolve_service_principal_proxy(self, external_id: str) -> ResolveServicePrincipalResponse:
        """Resolves an SP with the given external ID from the customer's IdP. If the SP does not exist, it will
        be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will
        return an error.

        :param external_id: str
          Required. The external ID of the service principal in the customer's IdP.

        :returns: :class:`ResolveServicePrincipalResponse`
        """

        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do(
            "POST", "/api/2.0/identity/servicePrincipals/resolveByExternalId", body=body, headers=headers
        )
        return ResolveServicePrincipalResponse.from_dict(res)

    def resolve_user_proxy(self, external_id: str) -> ResolveUserResponse:
        """Resolves a user with the given external ID from the customer's IdP. If the user does not exist, it
        will be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will
        return an error.

        :param external_id: str
          Required. The external ID of the user in the customer's IdP.

        :returns: :class:`ResolveUserResponse`
        """

        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/identity/users/resolveByExternalId", body=body, headers=headers)
        return ResolveUserResponse.from_dict(res)

    def update_workspace_assignment_detail_proxy(
        self, principal_id: int, workspace_assignment_detail: WorkspaceAssignmentDetail, update_mask: FieldMask
    ) -> WorkspaceAssignmentDetail:
        """Updates the entitlements of a directly assigned principal in a workspace (workspace-level proxy).
        Entitlement changes are applied individually and non-atomically — if a failure occurs partway
        through, only a subset of the requested changes may have been applied. Use
        GetWorkspaceAssignmentDetail to confirm the final state.

        :param principal_id: int
          Required. ID of the principal in Databricks.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be updated in <Databricks>.
        :param update_mask: FieldMask
          Required. The list of fields to update.

        :returns: :class:`WorkspaceAssignmentDetail`
        """

        body = workspace_assignment_detail.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do(
            "PATCH",
            f"/api/2.0/identity/workspaceAssignmentDetails/{principal_id}",
            query=query,
            body=body,
            headers=headers,
        )
        return WorkspaceAssignmentDetail.from_dict(res)

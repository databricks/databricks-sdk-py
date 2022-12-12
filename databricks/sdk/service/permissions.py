# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class AccessControlRequest:

    # name of the group
    group_name: str
    # Permission level
    permission_level: "PermissionLevel"
    # name of the service principal
    service_principal_name: str
    # name of the user
    user_name: str

    def as_request(self) -> (dict, dict):
        accessControlRequest_query, accessControlRequest_body = {}, {}
        if self.group_name:
            accessControlRequest_body["group_name"] = self.group_name
        if self.permission_level:
            accessControlRequest_body["permission_level"] = self.permission_level.value
        if self.service_principal_name:
            accessControlRequest_body[
                "service_principal_name"
            ] = self.service_principal_name
        if self.user_name:
            accessControlRequest_body["user_name"] = self.user_name

        return accessControlRequest_query, accessControlRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "AccessControlRequest":
        return cls(
            group_name=d.get("group_name", None),
            permission_level=PermissionLevel(d["permission_level"])
            if "permission_level" in d
            else None,
            service_principal_name=d.get("service_principal_name", None),
            user_name=d.get("user_name", None),
        )


@dataclass
class AccessControlResponse:

    # All permissions.
    all_permissions: "List[Permission]"
    # name of the group
    group_name: str
    # name of the service principal
    service_principal_name: str
    # name of the user
    user_name: str

    def as_request(self) -> (dict, dict):
        accessControlResponse_query, accessControlResponse_body = {}, {}
        if self.all_permissions:
            accessControlResponse_body["all_permissions"] = [
                v.as_request()[1] for v in self.all_permissions
            ]
        if self.group_name:
            accessControlResponse_body["group_name"] = self.group_name
        if self.service_principal_name:
            accessControlResponse_body[
                "service_principal_name"
            ] = self.service_principal_name
        if self.user_name:
            accessControlResponse_body["user_name"] = self.user_name

        return accessControlResponse_query, accessControlResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "AccessControlResponse":
        return cls(
            all_permissions=[Permission.from_dict(v) for v in d["all_permissions"]]
            if "all_permissions" in d
            else None,
            group_name=d.get("group_name", None),
            service_principal_name=d.get("service_principal_name", None),
            user_name=d.get("user_name", None),
        )


@dataclass
class CreateWorkspaceAssignments:

    # Array of permissions assignments to apply to a workspace.
    permission_assignments: "List[PermissionAssignmentInput]"
    # The workspace ID for the account.
    workspace_id: int  # path

    def as_request(self) -> (dict, dict):
        createWorkspaceAssignments_query, createWorkspaceAssignments_body = {}, {}
        if self.permission_assignments:
            createWorkspaceAssignments_body["permission_assignments"] = [
                v.as_request()[1] for v in self.permission_assignments
            ]
        if self.workspace_id:
            createWorkspaceAssignments_body["workspace_id"] = self.workspace_id

        return createWorkspaceAssignments_query, createWorkspaceAssignments_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateWorkspaceAssignments":
        return cls(
            permission_assignments=[
                PermissionAssignmentInput.from_dict(v)
                for v in d["permission_assignments"]
            ]
            if "permission_assignments" in d
            else None,
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class DeleteWorkspaceAssignmentRequest:
    """Delete permissions assignment"""

    # The ID of the service principal.
    principal_id: int  # path
    # The workspace ID.
    workspace_id: int  # path

    def as_request(self) -> (dict, dict):
        (
            deleteWorkspaceAssignmentRequest_query,
            deleteWorkspaceAssignmentRequest_body,
        ) = ({}, {})
        if self.principal_id:
            deleteWorkspaceAssignmentRequest_body["principal_id"] = self.principal_id
        if self.workspace_id:
            deleteWorkspaceAssignmentRequest_body["workspace_id"] = self.workspace_id

        return (
            deleteWorkspaceAssignmentRequest_query,
            deleteWorkspaceAssignmentRequest_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteWorkspaceAssignmentRequest":
        return cls(
            principal_id=d.get("principal_id", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class Get:
    """Get object permissions"""

    request_object_id: str  # path
    # <needs content>
    request_object_type: str  # path

    def as_request(self) -> (dict, dict):
        get_query, get_body = {}, {}
        if self.request_object_id:
            get_body["request_object_id"] = self.request_object_id
        if self.request_object_type:
            get_body["request_object_type"] = self.request_object_type

        return get_query, get_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Get":
        return cls(
            request_object_id=d.get("request_object_id", None),
            request_object_type=d.get("request_object_type", None),
        )


@dataclass
class GetPermissionLevels:
    """Get permission levels"""

    # <needs content>
    request_object_id: str  # path
    # <needs content>
    request_object_type: str  # path

    def as_request(self) -> (dict, dict):
        getPermissionLevels_query, getPermissionLevels_body = {}, {}
        if self.request_object_id:
            getPermissionLevels_body["request_object_id"] = self.request_object_id
        if self.request_object_type:
            getPermissionLevels_body["request_object_type"] = self.request_object_type

        return getPermissionLevels_query, getPermissionLevels_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetPermissionLevels":
        return cls(
            request_object_id=d.get("request_object_id", None),
            request_object_type=d.get("request_object_type", None),
        )


@dataclass
class GetPermissionLevelsResponse:

    # Specific permission levels
    permission_levels: "List[PermissionsDescription]"

    def as_request(self) -> (dict, dict):
        getPermissionLevelsResponse_query, getPermissionLevelsResponse_body = {}, {}
        if self.permission_levels:
            getPermissionLevelsResponse_body["permission_levels"] = [
                v.as_request()[1] for v in self.permission_levels
            ]

        return getPermissionLevelsResponse_query, getPermissionLevelsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetPermissionLevelsResponse":
        return cls(
            permission_levels=[
                PermissionsDescription.from_dict(v) for v in d["permission_levels"]
            ]
            if "permission_levels" in d
            else None,
        )


@dataclass
class GetWorkspaceAssignmentRequest:
    """List workspace permissions"""

    # The workspace ID.
    workspace_id: int  # path

    def as_request(self) -> (dict, dict):
        getWorkspaceAssignmentRequest_query, getWorkspaceAssignmentRequest_body = {}, {}
        if self.workspace_id:
            getWorkspaceAssignmentRequest_body["workspace_id"] = self.workspace_id

        return getWorkspaceAssignmentRequest_query, getWorkspaceAssignmentRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetWorkspaceAssignmentRequest":
        return cls(
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class ListWorkspaceAssignmentRequest:
    """Get permission assignments"""

    # The workspace ID for the account.
    workspace_id: int  # path

    def as_request(self) -> (dict, dict):
        listWorkspaceAssignmentRequest_query, listWorkspaceAssignmentRequest_body = (
            {},
            {},
        )
        if self.workspace_id:
            listWorkspaceAssignmentRequest_body["workspace_id"] = self.workspace_id

        return listWorkspaceAssignmentRequest_query, listWorkspaceAssignmentRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListWorkspaceAssignmentRequest":
        return cls(
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class ObjectPermissions:

    access_control_list: "List[AccessControlResponse]"

    object_id: str

    object_type: str

    def as_request(self) -> (dict, dict):
        objectPermissions_query, objectPermissions_body = {}, {}
        if self.access_control_list:
            objectPermissions_body["access_control_list"] = [
                v.as_request()[1] for v in self.access_control_list
            ]
        if self.object_id:
            objectPermissions_body["object_id"] = self.object_id
        if self.object_type:
            objectPermissions_body["object_type"] = self.object_type

        return objectPermissions_query, objectPermissions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ObjectPermissions":
        return cls(
            access_control_list=[
                AccessControlResponse.from_dict(v) for v in d["access_control_list"]
            ]
            if "access_control_list" in d
            else None,
            object_id=d.get("object_id", None),
            object_type=d.get("object_type", None),
        )


@dataclass
class Permission:

    inherited: bool

    inherited_from_object: "List[str]"
    # Permission level
    permission_level: "PermissionLevel"

    def as_request(self) -> (dict, dict):
        permission_query, permission_body = {}, {}
        if self.inherited:
            permission_body["inherited"] = self.inherited
        if self.inherited_from_object:
            permission_body["inherited_from_object"] = [
                v for v in self.inherited_from_object
            ]
        if self.permission_level:
            permission_body["permission_level"] = self.permission_level.value

        return permission_query, permission_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Permission":
        return cls(
            inherited=d.get("inherited", None),
            inherited_from_object=d.get("inherited_from_object", None),
            permission_level=PermissionLevel(d["permission_level"])
            if "permission_level" in d
            else None,
        )


@dataclass
class PermissionAssignment:

    # Error response associated with a workspace permission assignment, if any.
    error: str
    # The permissions level of the service principal.
    permissions: "List[WorkspacePermission]"
    # Information about the service principal assigned for the workspace.
    principal: "PrincipalOutput"

    def as_request(self) -> (dict, dict):
        permissionAssignment_query, permissionAssignment_body = {}, {}
        if self.error:
            permissionAssignment_body["error"] = self.error
        if self.permissions:
            permissionAssignment_body["permissions"] = [v for v in self.permissions]
        if self.principal:
            permissionAssignment_body["principal"] = self.principal.as_request()[1]

        return permissionAssignment_query, permissionAssignment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PermissionAssignment":
        return cls(
            error=d.get("error", None),
            permissions=d.get("permissions", None),
            principal=PrincipalOutput.from_dict(d["principal"])
            if "principal" in d
            else None,
        )


@dataclass
class PermissionAssignmentInput:

    # The group name for the service principal.
    group_name: str
    # Array of permissions to apply to the workspace for the service principal.
    permissions: "List[WorkspacePermission]"
    # The name of the service principal.
    service_principal_name: str
    # The username of the owner of the service principal.
    user_name: str

    def as_request(self) -> (dict, dict):
        permissionAssignmentInput_query, permissionAssignmentInput_body = {}, {}
        if self.group_name:
            permissionAssignmentInput_body["group_name"] = self.group_name
        if self.permissions:
            permissionAssignmentInput_body["permissions"] = [
                v for v in self.permissions
            ]
        if self.service_principal_name:
            permissionAssignmentInput_body[
                "service_principal_name"
            ] = self.service_principal_name
        if self.user_name:
            permissionAssignmentInput_body["user_name"] = self.user_name

        return permissionAssignmentInput_query, permissionAssignmentInput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PermissionAssignmentInput":
        return cls(
            group_name=d.get("group_name", None),
            permissions=d.get("permissions", None),
            service_principal_name=d.get("service_principal_name", None),
            user_name=d.get("user_name", None),
        )


@dataclass
class PermissionAssignments:

    # Array of permissions assignments defined for a workspace.
    permission_assignments: "List[PermissionAssignment]"

    def as_request(self) -> (dict, dict):
        permissionAssignments_query, permissionAssignments_body = {}, {}
        if self.permission_assignments:
            permissionAssignments_body["permission_assignments"] = [
                v.as_request()[1] for v in self.permission_assignments
            ]

        return permissionAssignments_query, permissionAssignments_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PermissionAssignments":
        return cls(
            permission_assignments=[
                PermissionAssignment.from_dict(v) for v in d["permission_assignments"]
            ]
            if "permission_assignments" in d
            else None,
        )


class PermissionLevel(Enum):
    """Permission level"""

    CAN_ATTACH_TO = "CAN_ATTACH_TO"
    CAN_BIND = "CAN_BIND"
    CAN_EDIT = "CAN_EDIT"
    CAN_EDIT_METADATA = "CAN_EDIT_METADATA"
    CAN_MANAGE = "CAN_MANAGE"
    CAN_MANAGE_PRODUCTION_VERSIONS = "CAN_MANAGE_PRODUCTION_VERSIONS"
    CAN_MANAGE_RUN = "CAN_MANAGE_RUN"
    CAN_MANAGE_STAGING_VERSIONS = "CAN_MANAGE_STAGING_VERSIONS"
    CAN_READ = "CAN_READ"
    CAN_RESTART = "CAN_RESTART"
    CAN_RUN = "CAN_RUN"
    CAN_USE = "CAN_USE"
    CAN_VIEW = "CAN_VIEW"
    CAN_VIEW_METADATA = "CAN_VIEW_METADATA"
    IS_OWNER = "IS_OWNER"


@dataclass
class PermissionOutput:

    # The results of a permissions query.
    description: str

    permission_level: "WorkspacePermission"

    def as_request(self) -> (dict, dict):
        permissionOutput_query, permissionOutput_body = {}, {}
        if self.description:
            permissionOutput_body["description"] = self.description
        if self.permission_level:
            permissionOutput_body["permission_level"] = self.permission_level.value

        return permissionOutput_query, permissionOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PermissionOutput":
        return cls(
            description=d.get("description", None),
            permission_level=WorkspacePermission(d["permission_level"])
            if "permission_level" in d
            else None,
        )


@dataclass
class PermissionsDescription:

    description: str
    # Permission level
    permission_level: "PermissionLevel"

    def as_request(self) -> (dict, dict):
        permissionsDescription_query, permissionsDescription_body = {}, {}
        if self.description:
            permissionsDescription_body["description"] = self.description
        if self.permission_level:
            permissionsDescription_body[
                "permission_level"
            ] = self.permission_level.value

        return permissionsDescription_query, permissionsDescription_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PermissionsDescription":
        return cls(
            description=d.get("description", None),
            permission_level=PermissionLevel(d["permission_level"])
            if "permission_level" in d
            else None,
        )


@dataclass
class PermissionsRequest:

    access_control_list: "List[AccessControlRequest]"

    request_object_id: str  # path
    # <needs content>
    request_object_type: str  # path

    def as_request(self) -> (dict, dict):
        permissionsRequest_query, permissionsRequest_body = {}, {}
        if self.access_control_list:
            permissionsRequest_body["access_control_list"] = [
                v.as_request()[1] for v in self.access_control_list
            ]
        if self.request_object_id:
            permissionsRequest_body["request_object_id"] = self.request_object_id
        if self.request_object_type:
            permissionsRequest_body["request_object_type"] = self.request_object_type

        return permissionsRequest_query, permissionsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PermissionsRequest":
        return cls(
            access_control_list=[
                AccessControlRequest.from_dict(v) for v in d["access_control_list"]
            ]
            if "access_control_list" in d
            else None,
            request_object_id=d.get("request_object_id", None),
            request_object_type=d.get("request_object_type", None),
        )


@dataclass
class PrincipalOutput:

    # The display name of the service principal.
    display_name: str
    # The group name for the service principal.
    group_name: str
    # The unique, opaque id of the principal.
    principal_id: int
    # The name of the service principal.
    service_principal_name: str
    # The username of the owner of the service principal.
    user_name: str

    def as_request(self) -> (dict, dict):
        principalOutput_query, principalOutput_body = {}, {}
        if self.display_name:
            principalOutput_body["display_name"] = self.display_name
        if self.group_name:
            principalOutput_body["group_name"] = self.group_name
        if self.principal_id:
            principalOutput_body["principal_id"] = self.principal_id
        if self.service_principal_name:
            principalOutput_body["service_principal_name"] = self.service_principal_name
        if self.user_name:
            principalOutput_body["user_name"] = self.user_name

        return principalOutput_query, principalOutput_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PrincipalOutput":
        return cls(
            display_name=d.get("display_name", None),
            group_name=d.get("group_name", None),
            principal_id=d.get("principal_id", None),
            service_principal_name=d.get("service_principal_name", None),
            user_name=d.get("user_name", None),
        )


@dataclass
class UpdateWorkspaceAssignments:

    # Array of permissions assignments to update on the workspace.
    permissions: "List[WorkspacePermission]"
    # The ID of the service principal.
    principal_id: int  # path
    # The workspace ID.
    workspace_id: int  # path

    def as_request(self) -> (dict, dict):
        updateWorkspaceAssignments_query, updateWorkspaceAssignments_body = {}, {}
        if self.permissions:
            updateWorkspaceAssignments_body["permissions"] = [
                v for v in self.permissions
            ]
        if self.principal_id:
            updateWorkspaceAssignments_body["principal_id"] = self.principal_id
        if self.workspace_id:
            updateWorkspaceAssignments_body["workspace_id"] = self.workspace_id

        return updateWorkspaceAssignments_query, updateWorkspaceAssignments_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateWorkspaceAssignments":
        return cls(
            permissions=d.get("permissions", None),
            principal_id=d.get("principal_id", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class WorkspaceAssignmentsCreated:

    # Array of permissions assignments applied to a workspace.
    permission_assignments: "List[PermissionAssignment]"

    def as_request(self) -> (dict, dict):
        workspaceAssignmentsCreated_query, workspaceAssignmentsCreated_body = {}, {}
        if self.permission_assignments:
            workspaceAssignmentsCreated_body["permission_assignments"] = [
                v.as_request()[1] for v in self.permission_assignments
            ]

        return workspaceAssignmentsCreated_query, workspaceAssignmentsCreated_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "WorkspaceAssignmentsCreated":
        return cls(
            permission_assignments=[
                PermissionAssignment.from_dict(v) for v in d["permission_assignments"]
            ]
            if "permission_assignments" in d
            else None,
        )


class WorkspacePermission(Enum):

    ADMIN = "ADMIN"
    UNKNOWN = "UNKNOWN"
    USER = "USER"


@dataclass
class WorkspacePermissions:

    # Array of permissions defined for a workspace.
    permissions: "List[PermissionOutput]"

    def as_request(self) -> (dict, dict):
        workspacePermissions_query, workspacePermissions_body = {}, {}
        if self.permissions:
            workspacePermissions_body["permissions"] = [
                v.as_request()[1] for v in self.permissions
            ]

        return workspacePermissions_query, workspacePermissions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "WorkspacePermissions":
        return cls(
            permissions=[PermissionOutput.from_dict(v) for v in d["permissions"]]
            if "permissions" in d
            else None,
        )


class PermissionsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def get(self, request: Get) -> ObjectPermissions:
        """Get object permissions.

        Gets the permission of an object. Objects can inherit permissions from
        their parent objects or root objects."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/permissions/{request.request_object_type}/{request.request_object_id}",
            query=query,
            body=body,
        )
        return ObjectPermissions.from_dict(json)

    def get_permission_levels(
        self, request: GetPermissionLevels
    ) -> GetPermissionLevelsResponse:
        """Get permission levels.

        Gets the permission levels that a user can have on an object."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/permissions/{request.request_object_type}/{request.request_object_id}/permissionLevels",
            query=query,
            body=body,
        )
        return GetPermissionLevelsResponse.from_dict(json)

    def set(self, request: PermissionsRequest):
        """Set permissions.

        Sets permissions on object. Objects can inherit permissions from their
        parent objects and root objects."""
        query, body = request.as_request()
        self._api.do(
            "PUT",
            f"/api/2.0/permissions/{request.request_object_type}/{request.request_object_id}",
            query=query,
            body=body,
        )

    def update(self, request: PermissionsRequest):
        """Update permission.

        Updates the permissions on an object."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.0/permissions/{request.request_object_type}/{request.request_object_id}",
            query=query,
            body=body,
        )


class WorkspaceAssignmentAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self, request: CreateWorkspaceAssignments
    ) -> WorkspaceAssignmentsCreated:
        """Create permission assignments.

        Create new permission assignments for the specified account and
        workspace."""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            f"/api/2.0/preview/accounts//workspaces/{request.workspace_id}/permissionassignments",
            query=query,
            body=body,
        )
        return WorkspaceAssignmentsCreated.from_dict(json)

    def delete(self, request: DeleteWorkspaceAssignmentRequest):
        """Delete permissions assignment.

        Deletes the workspace permissions assignment for a given account and
        workspace using the specified service principal."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/preview/accounts//workspaces/{request.workspace_id}/permissionassignments/principals/{request.principal_id}",
            query=query,
            body=body,
        )

    def get(self, request: GetWorkspaceAssignmentRequest) -> WorkspacePermissions:
        """List workspace permissions.

        Get an array of workspace permissions for the specified account and
        workspace."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/preview/accounts//workspaces/{request.workspace_id}/permissionassignments/permissions",
            query=query,
            body=body,
        )
        return WorkspacePermissions.from_dict(json)

    def list(self, request: ListWorkspaceAssignmentRequest) -> PermissionAssignments:
        """Get permission assignments.

        Get the permission assignments for the specified Databricks Account and
        Databricks Workspace."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/preview/accounts//workspaces/{request.workspace_id}/permissionassignments",
            query=query,
            body=body,
        )
        return PermissionAssignments.from_dict(json)

    def update(self, request: UpdateWorkspaceAssignments):
        """Update permissions assignment.

        Updates the workspace permissions assignment for a given account and
        workspace using the specified service principal."""
        query, body = request.as_request()
        self._api.do(
            "PUT",
            f"/api/2.0/preview/accounts//workspaces/{request.workspace_id}/permissionassignments/principals/{request.principal_id}",
            query=query,
            body=body,
        )

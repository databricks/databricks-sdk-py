# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List

from ._internal import _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AccessControlRequest:
    group_name: str = None
    permission_level: 'PermissionLevel' = None
    service_principal_name: str = None
    user_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.group_name: body['group_name'] = self.group_name
        if self.permission_level: body['permission_level'] = self.permission_level.value
        if self.service_principal_name: body['service_principal_name'] = self.service_principal_name
        if self.user_name: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AccessControlRequest':
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', PermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class AccessControlResponse:
    all_permissions: 'List[Permission]' = None
    group_name: str = None
    service_principal_name: str = None
    user_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.all_permissions: body['all_permissions'] = [v.as_dict() for v in self.all_permissions]
        if self.group_name: body['group_name'] = self.group_name
        if self.service_principal_name: body['service_principal_name'] = self.service_principal_name
        if self.user_name: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AccessControlResponse':
        return cls(all_permissions=_repeated(d, 'all_permissions', Permission),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class DeleteWorkspaceAssignmentRequest:
    """Delete permissions assignment"""

    workspace_id: int
    principal_id: int


@dataclass
class Get:
    """Get object permissions"""

    request_object_type: str
    request_object_id: str


@dataclass
class GetPermissionLevels:
    """Get permission levels"""

    request_object_type: str
    request_object_id: str


@dataclass
class GetPermissionLevelsResponse:
    permission_levels: 'List[PermissionsDescription]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPermissionLevelsResponse':
        return cls(permission_levels=_repeated(d, 'permission_levels', PermissionsDescription))


@dataclass
class GetWorkspaceAssignmentRequest:
    """List workspace permissions"""

    workspace_id: int


@dataclass
class ListWorkspaceAssignmentRequest:
    """Get permission assignments"""

    workspace_id: int


@dataclass
class ObjectPermissions:
    access_control_list: 'List[AccessControlResponse]' = None
    object_id: str = None
    object_type: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id: body['object_id'] = self.object_id
        if self.object_type: body['object_type'] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ObjectPermissions':
        return cls(access_control_list=_repeated(d, 'access_control_list', AccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class Permission:
    inherited: bool = None
    inherited_from_object: 'List[str]' = None
    permission_level: 'PermissionLevel' = None

    def as_dict(self) -> dict:
        body = {}
        if self.inherited: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Permission':
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', PermissionLevel))


@dataclass
class PermissionAssignment:
    error: str = None
    permissions: 'List[WorkspacePermission]' = None
    principal: 'PrincipalOutput' = None

    def as_dict(self) -> dict:
        body = {}
        if self.error: body['error'] = self.error
        if self.permissions: body['permissions'] = [v for v in self.permissions]
        if self.principal: body['principal'] = self.principal.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermissionAssignment':
        return cls(error=d.get('error', None),
                   permissions=d.get('permissions', None),
                   principal=_from_dict(d, 'principal', PrincipalOutput))


@dataclass
class PermissionAssignments:
    permission_assignments: 'List[PermissionAssignment]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.permission_assignments:
            body['permission_assignments'] = [v.as_dict() for v in self.permission_assignments]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermissionAssignments':
        return cls(permission_assignments=_repeated(d, 'permission_assignments', PermissionAssignment))


class PermissionLevel(Enum):
    """Permission level"""

    CAN_ATTACH_TO = 'CAN_ATTACH_TO'
    CAN_BIND = 'CAN_BIND'
    CAN_EDIT = 'CAN_EDIT'
    CAN_EDIT_METADATA = 'CAN_EDIT_METADATA'
    CAN_MANAGE = 'CAN_MANAGE'
    CAN_MANAGE_PRODUCTION_VERSIONS = 'CAN_MANAGE_PRODUCTION_VERSIONS'
    CAN_MANAGE_RUN = 'CAN_MANAGE_RUN'
    CAN_MANAGE_STAGING_VERSIONS = 'CAN_MANAGE_STAGING_VERSIONS'
    CAN_READ = 'CAN_READ'
    CAN_RESTART = 'CAN_RESTART'
    CAN_RUN = 'CAN_RUN'
    CAN_USE = 'CAN_USE'
    CAN_VIEW = 'CAN_VIEW'
    CAN_VIEW_METADATA = 'CAN_VIEW_METADATA'
    IS_OWNER = 'IS_OWNER'


@dataclass
class PermissionOutput:
    description: str = None
    permission_level: 'WorkspacePermission' = None

    def as_dict(self) -> dict:
        body = {}
        if self.description: body['description'] = self.description
        if self.permission_level: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermissionOutput':
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', WorkspacePermission))


@dataclass
class PermissionsDescription:
    description: str = None
    permission_level: 'PermissionLevel' = None

    def as_dict(self) -> dict:
        body = {}
        if self.description: body['description'] = self.description
        if self.permission_level: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermissionsDescription':
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', PermissionLevel))


@dataclass
class PermissionsRequest:
    request_object_type: str
    request_object_id: str
    access_control_list: 'List[AccessControlRequest]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.request_object_id: body['request_object_id'] = self.request_object_id
        if self.request_object_type: body['request_object_type'] = self.request_object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermissionsRequest':
        return cls(access_control_list=_repeated(d, 'access_control_list', AccessControlRequest),
                   request_object_id=d.get('request_object_id', None),
                   request_object_type=d.get('request_object_type', None))


@dataclass
class PrincipalOutput:
    display_name: str = None
    group_name: str = None
    principal_id: int = None
    service_principal_name: str = None
    user_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.display_name: body['display_name'] = self.display_name
        if self.group_name: body['group_name'] = self.group_name
        if self.principal_id: body['principal_id'] = self.principal_id
        if self.service_principal_name: body['service_principal_name'] = self.service_principal_name
        if self.user_name: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PrincipalOutput':
        return cls(display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   principal_id=d.get('principal_id', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class UpdateWorkspaceAssignments:
    permissions: 'List[WorkspacePermission]'
    workspace_id: int
    principal_id: int

    def as_dict(self) -> dict:
        body = {}
        if self.permissions: body['permissions'] = [v for v in self.permissions]
        if self.principal_id: body['principal_id'] = self.principal_id
        if self.workspace_id: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateWorkspaceAssignments':
        return cls(permissions=d.get('permissions', None),
                   principal_id=d.get('principal_id', None),
                   workspace_id=d.get('workspace_id', None))


class WorkspacePermission(Enum):

    ADMIN = 'ADMIN'
    UNKNOWN = 'UNKNOWN'
    USER = 'USER'


@dataclass
class WorkspacePermissions:
    permissions: 'List[PermissionOutput]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.permissions: body['permissions'] = [v.as_dict() for v in self.permissions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WorkspacePermissions':
        return cls(permissions=_repeated(d, 'permissions', PermissionOutput))


class PermissionsAPI:
    """Permissions API are used to create read, write, edit, update and manage access for various users on
    different objects and endpoints."""

    def __init__(self, api_client):
        self._api = api_client

    def get(self, request_object_type: str, request_object_id: str, **kwargs) -> ObjectPermissions:
        """Get object permissions.
        
        Gets the permission of an object. Objects can inherit permissions from their parent objects or root
        objects."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Get(request_object_id=request_object_id, request_object_type=request_object_type)

        json = self._api.do(
            'GET', f'/api/2.0/permissions/{request.request_object_type}/{request.request_object_id}')
        return ObjectPermissions.from_dict(json)

    def get_permission_levels(self, request_object_type: str, request_object_id: str,
                              **kwargs) -> GetPermissionLevelsResponse:
        """Get permission levels.
        
        Gets the permission levels that a user can have on an object."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetPermissionLevels(request_object_id=request_object_id,
                                          request_object_type=request_object_type)

        json = self._api.do(
            'GET',
            f'/api/2.0/permissions/{request.request_object_type}/{request.request_object_id}/permissionLevels'
        )
        return GetPermissionLevelsResponse.from_dict(json)

    def set(self,
            request_object_type: str,
            request_object_id: str,
            *,
            access_control_list: List[AccessControlRequest] = None,
            **kwargs):
        """Set permissions.
        
        Sets permissions on object. Objects can inherit permissions from their parent objects and root
        objects."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PermissionsRequest(access_control_list=access_control_list,
                                         request_object_id=request_object_id,
                                         request_object_type=request_object_type)
        body = request.as_dict()
        self._api.do('PUT',
                     f'/api/2.0/permissions/{request.request_object_type}/{request.request_object_id}',
                     body=body)

    def update(self,
               request_object_type: str,
               request_object_id: str,
               *,
               access_control_list: List[AccessControlRequest] = None,
               **kwargs):
        """Update permission.
        
        Updates the permissions on an object."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PermissionsRequest(access_control_list=access_control_list,
                                         request_object_id=request_object_id,
                                         request_object_type=request_object_type)
        body = request.as_dict()
        self._api.do('PATCH',
                     f'/api/2.0/permissions/{request.request_object_type}/{request.request_object_id}',
                     body=body)


class WorkspaceAssignmentAPI:
    """The Workspace Permission Assignment API allows you to manage workspace permissions for principals in your
    account."""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, workspace_id: int, principal_id: int, **kwargs):
        """Delete permissions assignment.
        
        Deletes the workspace permissions assignment in a given account and workspace for the specified
        principal."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteWorkspaceAssignmentRequest(principal_id=principal_id, workspace_id=workspace_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{request.workspace_id}/permissionassignments/principals/{request.principal_id}'
        )

    def get(self, workspace_id: int, **kwargs) -> WorkspacePermissions:
        """List workspace permissions.
        
        Get an array of workspace permissions for the specified account and workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetWorkspaceAssignmentRequest(workspace_id=workspace_id)

        json = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{request.workspace_id}/permissionassignments/permissions'
        )
        return WorkspacePermissions.from_dict(json)

    def list(self, workspace_id: int, **kwargs) -> Iterator[PermissionAssignment]:
        """Get permission assignments.
        
        Get the permission assignments for the specified Databricks Account and Databricks Workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListWorkspaceAssignmentRequest(workspace_id=workspace_id)

        json = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{request.workspace_id}/permissionassignments'
        )
        return [PermissionAssignment.from_dict(v) for v in json.get('permission_assignments', [])]

    def update(self, permissions: List[WorkspacePermission], workspace_id: int, principal_id: int, **kwargs):
        """Create or update permissions assignment.
        
        Creates or updates the workspace permissions assignment in a given account and workspace for the
        specified principal."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateWorkspaceAssignments(permissions=permissions,
                                                 principal_id=principal_id,
                                                 workspace_id=workspace_id)
        body = request.as_dict()
        self._api.do(
            'PUT',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{request.workspace_id}/permissionassignments/principals/{request.principal_id}',
            body=body)

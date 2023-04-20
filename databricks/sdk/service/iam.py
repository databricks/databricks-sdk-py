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
class ComplexValue:
    display: str = None
    primary: bool = None
    type: str = None
    value: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.display: body['display'] = self.display
        if self.primary: body['primary'] = self.primary
        if self.type: body['type'] = self.type
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ComplexValue':
        return cls(display=d.get('display', None),
                   primary=d.get('primary', None),
                   type=d.get('type', None),
                   value=d.get('value', None))


@dataclass
class DeleteAccountGroupRequest:
    """Delete a group"""

    id: str


@dataclass
class DeleteAccountServicePrincipalRequest:
    """Delete a service principal"""

    id: str


@dataclass
class DeleteAccountUserRequest:
    """Delete a user"""

    id: str


@dataclass
class DeleteGroupRequest:
    """Delete a group"""

    id: str


@dataclass
class DeleteServicePrincipalRequest:
    """Delete a service principal"""

    id: str


@dataclass
class DeleteUserRequest:
    """Delete a user"""

    id: str


@dataclass
class DeleteWorkspaceAssignmentRequest:
    """Delete permissions assignment"""

    workspace_id: int
    principal_id: int


@dataclass
class GetAccountGroupRequest:
    """Get group details"""

    id: str


@dataclass
class GetAccountServicePrincipalRequest:
    """Get service principal details"""

    id: str


@dataclass
class GetAccountUserRequest:
    """Get user details"""

    id: str


@dataclass
class GetGroupRequest:
    """Get group details"""

    id: str


@dataclass
class GetPermissionLevelsRequest:
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
class GetPermissionRequest:
    """Get object permissions"""

    request_object_type: str
    request_object_id: str


@dataclass
class GetServicePrincipalRequest:
    """Get service principal details"""

    id: str


@dataclass
class GetUserRequest:
    """Get user details"""

    id: str


@dataclass
class GetWorkspaceAssignmentRequest:
    """List workspace permissions"""

    workspace_id: int


@dataclass
class Group:
    id: str
    display_name: str = None
    entitlements: 'List[ComplexValue]' = None
    external_id: str = None
    groups: 'List[ComplexValue]' = None
    members: 'List[ComplexValue]' = None
    roles: 'List[ComplexValue]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.display_name: body['displayName'] = self.display_name
        if self.entitlements: body['entitlements'] = [v.as_dict() for v in self.entitlements]
        if self.external_id: body['externalId'] = self.external_id
        if self.groups: body['groups'] = [v.as_dict() for v in self.groups]
        if self.id: body['id'] = self.id
        if self.members: body['members'] = [v.as_dict() for v in self.members]
        if self.roles: body['roles'] = [v.as_dict() for v in self.roles]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Group':
        return cls(display_name=d.get('displayName', None),
                   entitlements=_repeated(d, 'entitlements', ComplexValue),
                   external_id=d.get('externalId', None),
                   groups=_repeated(d, 'groups', ComplexValue),
                   id=d.get('id', None),
                   members=_repeated(d, 'members', ComplexValue),
                   roles=_repeated(d, 'roles', ComplexValue))


@dataclass
class ListAccountGroupsRequest:
    """List group details"""

    attributes: str = None
    count: int = None
    excluded_attributes: str = None
    filter: str = None
    sort_by: str = None
    sort_order: 'ListSortOrder' = None
    start_index: int = None


@dataclass
class ListAccountServicePrincipalsRequest:
    """List service principals"""

    attributes: str = None
    count: int = None
    excluded_attributes: str = None
    filter: str = None
    sort_by: str = None
    sort_order: 'ListSortOrder' = None
    start_index: int = None


@dataclass
class ListAccountUsersRequest:
    """List users"""

    attributes: str = None
    count: int = None
    excluded_attributes: str = None
    filter: str = None
    sort_by: str = None
    sort_order: 'ListSortOrder' = None
    start_index: int = None


@dataclass
class ListGroupsRequest:
    """List group details"""

    attributes: str = None
    count: int = None
    excluded_attributes: str = None
    filter: str = None
    sort_by: str = None
    sort_order: 'ListSortOrder' = None
    start_index: int = None


@dataclass
class ListGroupsResponse:
    items_per_page: int = None
    resources: 'List[Group]' = None
    start_index: int = None
    total_results: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.items_per_page: body['itemsPerPage'] = self.items_per_page
        if self.resources: body['Resources'] = [v.as_dict() for v in self.resources]
        if self.start_index: body['startIndex'] = self.start_index
        if self.total_results: body['totalResults'] = self.total_results
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListGroupsResponse':
        return cls(items_per_page=d.get('itemsPerPage', None),
                   resources=_repeated(d, 'Resources', Group),
                   start_index=d.get('startIndex', None),
                   total_results=d.get('totalResults', None))


@dataclass
class ListServicePrincipalResponse:
    items_per_page: int = None
    resources: 'List[ServicePrincipal]' = None
    start_index: int = None
    total_results: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.items_per_page: body['itemsPerPage'] = self.items_per_page
        if self.resources: body['Resources'] = [v.as_dict() for v in self.resources]
        if self.start_index: body['startIndex'] = self.start_index
        if self.total_results: body['totalResults'] = self.total_results
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListServicePrincipalResponse':
        return cls(items_per_page=d.get('itemsPerPage', None),
                   resources=_repeated(d, 'Resources', ServicePrincipal),
                   start_index=d.get('startIndex', None),
                   total_results=d.get('totalResults', None))


@dataclass
class ListServicePrincipalsRequest:
    """List service principals"""

    attributes: str = None
    count: int = None
    excluded_attributes: str = None
    filter: str = None
    sort_by: str = None
    sort_order: 'ListSortOrder' = None
    start_index: int = None


class ListSortOrder(Enum):

    ascending = 'ascending'
    descending = 'descending'


@dataclass
class ListUsersRequest:
    """List users"""

    attributes: str = None
    count: int = None
    excluded_attributes: str = None
    filter: str = None
    sort_by: str = None
    sort_order: 'ListSortOrder' = None
    start_index: int = None


@dataclass
class ListUsersResponse:
    items_per_page: int = None
    resources: 'List[User]' = None
    start_index: int = None
    total_results: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.items_per_page: body['itemsPerPage'] = self.items_per_page
        if self.resources: body['Resources'] = [v.as_dict() for v in self.resources]
        if self.start_index: body['startIndex'] = self.start_index
        if self.total_results: body['totalResults'] = self.total_results
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListUsersResponse':
        return cls(items_per_page=d.get('itemsPerPage', None),
                   resources=_repeated(d, 'Resources', User),
                   start_index=d.get('startIndex', None),
                   total_results=d.get('totalResults', None))


@dataclass
class ListWorkspaceAssignmentRequest:
    """Get permission assignments"""

    workspace_id: int


@dataclass
class Name:
    family_name: str = None
    given_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.family_name: body['familyName'] = self.family_name
        if self.given_name: body['givenName'] = self.given_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Name':
        return cls(family_name=d.get('familyName', None), given_name=d.get('givenName', None))


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
class PartialUpdate:
    id: str
    operations: 'List[Patch]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        if self.operations: body['operations'] = [v.as_dict() for v in self.operations]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PartialUpdate':
        return cls(id=d.get('id', None), operations=_repeated(d, 'operations', Patch))


@dataclass
class Patch:
    op: 'PatchOp' = None
    path: str = None
    value: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.op: body['op'] = self.op.value
        if self.path: body['path'] = self.path
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Patch':
        return cls(op=_enum(d, 'op', PatchOp), path=d.get('path', None), value=d.get('value', None))


class PatchOp(Enum):
    """Type of patch operation."""

    add = 'add'
    remove = 'remove'
    replace = 'replace'


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
class ServicePrincipal:
    id: str
    active: bool = None
    application_id: str = None
    display_name: str = None
    entitlements: 'List[ComplexValue]' = None
    external_id: str = None
    groups: 'List[ComplexValue]' = None
    roles: 'List[ComplexValue]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.active: body['active'] = self.active
        if self.application_id: body['applicationId'] = self.application_id
        if self.display_name: body['displayName'] = self.display_name
        if self.entitlements: body['entitlements'] = [v.as_dict() for v in self.entitlements]
        if self.external_id: body['externalId'] = self.external_id
        if self.groups: body['groups'] = [v.as_dict() for v in self.groups]
        if self.id: body['id'] = self.id
        if self.roles: body['roles'] = [v.as_dict() for v in self.roles]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServicePrincipal':
        return cls(active=d.get('active', None),
                   application_id=d.get('applicationId', None),
                   display_name=d.get('displayName', None),
                   entitlements=_repeated(d, 'entitlements', ComplexValue),
                   external_id=d.get('externalId', None),
                   groups=_repeated(d, 'groups', ComplexValue),
                   id=d.get('id', None),
                   roles=_repeated(d, 'roles', ComplexValue))


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


@dataclass
class User:
    id: str
    active: bool = None
    display_name: str = None
    emails: 'List[ComplexValue]' = None
    entitlements: 'List[ComplexValue]' = None
    external_id: str = None
    groups: 'List[ComplexValue]' = None
    name: 'Name' = None
    roles: 'List[ComplexValue]' = None
    user_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.active: body['active'] = self.active
        if self.display_name: body['displayName'] = self.display_name
        if self.emails: body['emails'] = [v.as_dict() for v in self.emails]
        if self.entitlements: body['entitlements'] = [v.as_dict() for v in self.entitlements]
        if self.external_id: body['externalId'] = self.external_id
        if self.groups: body['groups'] = [v.as_dict() for v in self.groups]
        if self.id: body['id'] = self.id
        if self.name: body['name'] = self.name.as_dict()
        if self.roles: body['roles'] = [v.as_dict() for v in self.roles]
        if self.user_name: body['userName'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'User':
        return cls(active=d.get('active', None),
                   display_name=d.get('displayName', None),
                   emails=_repeated(d, 'emails', ComplexValue),
                   entitlements=_repeated(d, 'entitlements', ComplexValue),
                   external_id=d.get('externalId', None),
                   groups=_repeated(d, 'groups', ComplexValue),
                   id=d.get('id', None),
                   name=_from_dict(d, 'name', Name),
                   roles=_repeated(d, 'roles', ComplexValue),
                   user_name=d.get('userName', None))


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


class AccountGroupsAPI:
    """Groups simplify identity management, making it easier to assign access to Databricks Account, data, and
    other securable objects.
    
    It is best practice to assign access to workspaces and access-control policies in Unity Catalog to groups,
    instead of to users individually. All Databricks Account identities can be assigned as members of groups,
    and members inherit permissions that are assigned to their group."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               id: str,
               *,
               display_name: str = None,
               entitlements: List[ComplexValue] = None,
               external_id: str = None,
               groups: List[ComplexValue] = None,
               members: List[ComplexValue] = None,
               roles: List[ComplexValue] = None,
               **kwargs) -> Group:
        """Create a new group.
        
        Creates a group in the Databricks Account with a unique name, using the supplied group details."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Group(display_name=display_name,
                            entitlements=entitlements,
                            external_id=external_id,
                            groups=groups,
                            id=id,
                            members=members,
                            roles=roles)
        body = request.as_dict()

        json = self._api.do('POST', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups', body=body)
        return Group.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a group.
        
        Deletes a group from the Databricks Account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteAccountGroupRequest(id=id)

        self._api.do('DELETE', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups/{request.id}')

    def get(self, id: str, **kwargs) -> Group:
        """Get group details.
        
        Gets the information for a specific group in the Databricks Account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAccountGroupRequest(id=id)

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups/{request.id}')
        return Group.from_dict(json)

    def list(self,
             *,
             attributes: str = None,
             count: int = None,
             excluded_attributes: str = None,
             filter: str = None,
             sort_by: str = None,
             sort_order: ListSortOrder = None,
             start_index: int = None,
             **kwargs) -> Iterator[Group]:
        """List group details.
        
        Gets all details of the groups associated with the Databricks Account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListAccountGroupsRequest(attributes=attributes,
                                               count=count,
                                               excluded_attributes=excluded_attributes,
                                               filter=filter,
                                               sort_by=sort_by,
                                               sort_order=sort_order,
                                               start_index=start_index)

        query = {}
        if attributes: query['attributes'] = request.attributes
        if count: query['count'] = request.count
        if excluded_attributes: query['excludedAttributes'] = request.excluded_attributes
        if filter: query['filter'] = request.filter
        if sort_by: query['sortBy'] = request.sort_by
        if sort_order: query['sortOrder'] = request.sort_order.value
        if start_index: query['startIndex'] = request.start_index

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups', query=query)
        return [Group.from_dict(v) for v in json.get('Resources', [])]

    def patch(self, id: str, *, operations: List[Patch] = None, **kwargs):
        """Update group details.
        
        Partially updates the details of a group."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations)
        body = request.as_dict()
        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups/{request.id}',
                     body=body)

    def update(self,
               id: str,
               *,
               display_name: str = None,
               entitlements: List[ComplexValue] = None,
               external_id: str = None,
               groups: List[ComplexValue] = None,
               members: List[ComplexValue] = None,
               roles: List[ComplexValue] = None,
               **kwargs):
        """Replace a group.
        
        Updates the details of a group by replacing the entire group entity."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Group(display_name=display_name,
                            entitlements=entitlements,
                            external_id=external_id,
                            groups=groups,
                            id=id,
                            members=members,
                            roles=roles)
        body = request.as_dict()
        self._api.do('PUT',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups/{request.id}',
                     body=body)


class AccountServicePrincipalsAPI:
    """Identities for use with jobs, automated tools, and systems such as scripts, apps, and CI/CD platforms.
    Databricks recommends creating service principals to run production jobs or modify production data. If all
    processes that act on production data run with service principals, interactive users do not need any
    write, delete, or modify privileges in production. This eliminates the risk of a user overwriting
    production data by accident."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               id: str,
               *,
               active: bool = None,
               application_id: str = None,
               display_name: str = None,
               entitlements: List[ComplexValue] = None,
               external_id: str = None,
               groups: List[ComplexValue] = None,
               roles: List[ComplexValue] = None,
               **kwargs) -> ServicePrincipal:
        """Create a service principal.
        
        Creates a new service principal in the Databricks Account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ServicePrincipal(active=active,
                                       application_id=application_id,
                                       display_name=display_name,
                                       entitlements=entitlements,
                                       external_id=external_id,
                                       groups=groups,
                                       id=id,
                                       roles=roles)
        body = request.as_dict()

        json = self._api.do('POST',
                            f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals',
                            body=body)
        return ServicePrincipal.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a service principal.
        
        Delete a single service principal in the Databricks Account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteAccountServicePrincipalRequest(id=id)

        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals/{request.id}')

    def get(self, id: str, **kwargs) -> ServicePrincipal:
        """Get service principal details.
        
        Gets the details for a single service principal define in the Databricks Account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAccountServicePrincipalRequest(id=id)

        json = self._api.do(
            'GET', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals/{request.id}')
        return ServicePrincipal.from_dict(json)

    def list(self,
             *,
             attributes: str = None,
             count: int = None,
             excluded_attributes: str = None,
             filter: str = None,
             sort_by: str = None,
             sort_order: ListSortOrder = None,
             start_index: int = None,
             **kwargs) -> Iterator[ServicePrincipal]:
        """List service principals.
        
        Gets the set of service principals associated with a Databricks Account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListAccountServicePrincipalsRequest(attributes=attributes,
                                                          count=count,
                                                          excluded_attributes=excluded_attributes,
                                                          filter=filter,
                                                          sort_by=sort_by,
                                                          sort_order=sort_order,
                                                          start_index=start_index)

        query = {}
        if attributes: query['attributes'] = request.attributes
        if count: query['count'] = request.count
        if excluded_attributes: query['excludedAttributes'] = request.excluded_attributes
        if filter: query['filter'] = request.filter
        if sort_by: query['sortBy'] = request.sort_by
        if sort_order: query['sortOrder'] = request.sort_order.value
        if start_index: query['startIndex'] = request.start_index

        json = self._api.do('GET',
                            f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals',
                            query=query)
        return [ServicePrincipal.from_dict(v) for v in json.get('Resources', [])]

    def patch(self, id: str, *, operations: List[Patch] = None, **kwargs):
        """Update service principal details.
        
        Partially updates the details of a single service principal in the Databricks Account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations)
        body = request.as_dict()
        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals/{request.id}',
                     body=body)

    def update(self,
               id: str,
               *,
               active: bool = None,
               application_id: str = None,
               display_name: str = None,
               entitlements: List[ComplexValue] = None,
               external_id: str = None,
               groups: List[ComplexValue] = None,
               roles: List[ComplexValue] = None,
               **kwargs):
        """Replace service principal.
        
        Updates the details of a single service principal.
        
        This action replaces the existing service principal with the same name."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ServicePrincipal(active=active,
                                       application_id=application_id,
                                       display_name=display_name,
                                       entitlements=entitlements,
                                       external_id=external_id,
                                       groups=groups,
                                       id=id,
                                       roles=roles)
        body = request.as_dict()
        self._api.do('PUT',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals/{request.id}',
                     body=body)


class AccountUsersAPI:
    """User identities recognized by Databricks and represented by email addresses.
    
    Databricks recommends using SCIM provisioning to sync users and groups automatically from your identity
    provider to your Databricks Account. SCIM streamlines onboarding a new employee or team by using your
    identity provider to create users and groups in Databricks Account and give them the proper level of
    access. When a user leaves your organization or no longer needs access to Databricks Account, admins can
    terminate the user in your identity provider and that user’s account will also be removed from
    Databricks Account. This ensures a consistent offboarding process and prevents unauthorized users from
    accessing sensitive data."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               id: str,
               *,
               active: bool = None,
               display_name: str = None,
               emails: List[ComplexValue] = None,
               entitlements: List[ComplexValue] = None,
               external_id: str = None,
               groups: List[ComplexValue] = None,
               name: Name = None,
               roles: List[ComplexValue] = None,
               user_name: str = None,
               **kwargs) -> User:
        """Create a new user.
        
        Creates a new user in the Databricks Account. This new user will also be added to the Databricks
        account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = User(active=active,
                           display_name=display_name,
                           emails=emails,
                           entitlements=entitlements,
                           external_id=external_id,
                           groups=groups,
                           id=id,
                           name=name,
                           roles=roles,
                           user_name=user_name)
        body = request.as_dict()

        json = self._api.do('POST', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users', body=body)
        return User.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a user.
        
        Deletes a user. Deleting a user from a Databricks Account also removes objects associated with the
        user."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteAccountUserRequest(id=id)

        self._api.do('DELETE', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users/{request.id}')

    def get(self, id: str, **kwargs) -> User:
        """Get user details.
        
        Gets information for a specific user in Databricks Account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAccountUserRequest(id=id)

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users/{request.id}')
        return User.from_dict(json)

    def list(self,
             *,
             attributes: str = None,
             count: int = None,
             excluded_attributes: str = None,
             filter: str = None,
             sort_by: str = None,
             sort_order: ListSortOrder = None,
             start_index: int = None,
             **kwargs) -> Iterator[User]:
        """List users.
        
        Gets details for all the users associated with a Databricks Account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListAccountUsersRequest(attributes=attributes,
                                              count=count,
                                              excluded_attributes=excluded_attributes,
                                              filter=filter,
                                              sort_by=sort_by,
                                              sort_order=sort_order,
                                              start_index=start_index)

        query = {}
        if attributes: query['attributes'] = request.attributes
        if count: query['count'] = request.count
        if excluded_attributes: query['excludedAttributes'] = request.excluded_attributes
        if filter: query['filter'] = request.filter
        if sort_by: query['sortBy'] = request.sort_by
        if sort_order: query['sortOrder'] = request.sort_order.value
        if start_index: query['startIndex'] = request.start_index

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users', query=query)
        return [User.from_dict(v) for v in json.get('Resources', [])]

    def patch(self, id: str, *, operations: List[Patch] = None, **kwargs):
        """Update user details.
        
        Partially updates a user resource by applying the supplied operations on specific user attributes."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations)
        body = request.as_dict()
        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users/{request.id}',
                     body=body)

    def update(self,
               id: str,
               *,
               active: bool = None,
               display_name: str = None,
               emails: List[ComplexValue] = None,
               entitlements: List[ComplexValue] = None,
               external_id: str = None,
               groups: List[ComplexValue] = None,
               name: Name = None,
               roles: List[ComplexValue] = None,
               user_name: str = None,
               **kwargs):
        """Replace a user.
        
        Replaces a user's information with the data supplied in request."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = User(active=active,
                           display_name=display_name,
                           emails=emails,
                           entitlements=entitlements,
                           external_id=external_id,
                           groups=groups,
                           id=id,
                           name=name,
                           roles=roles,
                           user_name=user_name)
        body = request.as_dict()
        self._api.do('PUT', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users/{request.id}', body=body)


class CurrentUserAPI:
    """This API allows retrieving information about currently authenticated user or service principal."""

    def __init__(self, api_client):
        self._api = api_client

    def me(self) -> User:
        """Get current user info.
        
        Get details about the current method caller's identity."""

        json = self._api.do('GET', '/api/2.0/preview/scim/v2/Me')
        return User.from_dict(json)


class GroupsAPI:
    """Groups simplify identity management, making it easier to assign access to Databricks Workspace, data, and
    other securable objects.
    
    It is best practice to assign access to workspaces and access-control policies in Unity Catalog to groups,
    instead of to users individually. All Databricks Workspace identities can be assigned as members of
    groups, and members inherit permissions that are assigned to their group."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               id: str,
               *,
               display_name: str = None,
               entitlements: List[ComplexValue] = None,
               external_id: str = None,
               groups: List[ComplexValue] = None,
               members: List[ComplexValue] = None,
               roles: List[ComplexValue] = None,
               **kwargs) -> Group:
        """Create a new group.
        
        Creates a group in the Databricks Workspace with a unique name, using the supplied group details."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Group(display_name=display_name,
                            entitlements=entitlements,
                            external_id=external_id,
                            groups=groups,
                            id=id,
                            members=members,
                            roles=roles)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/preview/scim/v2/Groups', body=body)
        return Group.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a group.
        
        Deletes a group from the Databricks Workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteGroupRequest(id=id)

        self._api.do('DELETE', f'/api/2.0/preview/scim/v2/Groups/{request.id}')

    def get(self, id: str, **kwargs) -> Group:
        """Get group details.
        
        Gets the information for a specific group in the Databricks Workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetGroupRequest(id=id)

        json = self._api.do('GET', f'/api/2.0/preview/scim/v2/Groups/{request.id}')
        return Group.from_dict(json)

    def list(self,
             *,
             attributes: str = None,
             count: int = None,
             excluded_attributes: str = None,
             filter: str = None,
             sort_by: str = None,
             sort_order: ListSortOrder = None,
             start_index: int = None,
             **kwargs) -> Iterator[Group]:
        """List group details.
        
        Gets all details of the groups associated with the Databricks Workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListGroupsRequest(attributes=attributes,
                                        count=count,
                                        excluded_attributes=excluded_attributes,
                                        filter=filter,
                                        sort_by=sort_by,
                                        sort_order=sort_order,
                                        start_index=start_index)

        query = {}
        if attributes: query['attributes'] = request.attributes
        if count: query['count'] = request.count
        if excluded_attributes: query['excludedAttributes'] = request.excluded_attributes
        if filter: query['filter'] = request.filter
        if sort_by: query['sortBy'] = request.sort_by
        if sort_order: query['sortOrder'] = request.sort_order.value
        if start_index: query['startIndex'] = request.start_index

        json = self._api.do('GET', '/api/2.0/preview/scim/v2/Groups', query=query)
        return [Group.from_dict(v) for v in json.get('Resources', [])]

    def patch(self, id: str, *, operations: List[Patch] = None, **kwargs):
        """Update group details.
        
        Partially updates the details of a group."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.0/preview/scim/v2/Groups/{request.id}', body=body)

    def update(self,
               id: str,
               *,
               display_name: str = None,
               entitlements: List[ComplexValue] = None,
               external_id: str = None,
               groups: List[ComplexValue] = None,
               members: List[ComplexValue] = None,
               roles: List[ComplexValue] = None,
               **kwargs):
        """Replace a group.
        
        Updates the details of a group by replacing the entire group entity."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Group(display_name=display_name,
                            entitlements=entitlements,
                            external_id=external_id,
                            groups=groups,
                            id=id,
                            members=members,
                            roles=roles)
        body = request.as_dict()
        self._api.do('PUT', f'/api/2.0/preview/scim/v2/Groups/{request.id}', body=body)


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
            request = GetPermissionRequest(request_object_id=request_object_id,
                                           request_object_type=request_object_type)

        json = self._api.do(
            'GET', f'/api/2.0/permissions/{request.request_object_type}/{request.request_object_id}')
        return ObjectPermissions.from_dict(json)

    def get_permission_levels(self, request_object_type: str, request_object_id: str,
                              **kwargs) -> GetPermissionLevelsResponse:
        """Get permission levels.
        
        Gets the permission levels that a user can have on an object."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetPermissionLevelsRequest(request_object_id=request_object_id,
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


class ServicePrincipalsAPI:
    """Identities for use with jobs, automated tools, and systems such as scripts, apps, and CI/CD platforms.
    Databricks recommends creating service principals to run production jobs or modify production data. If all
    processes that act on production data run with service principals, interactive users do not need any
    write, delete, or modify privileges in production. This eliminates the risk of a user overwriting
    production data by accident."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               id: str,
               *,
               active: bool = None,
               application_id: str = None,
               display_name: str = None,
               entitlements: List[ComplexValue] = None,
               external_id: str = None,
               groups: List[ComplexValue] = None,
               roles: List[ComplexValue] = None,
               **kwargs) -> ServicePrincipal:
        """Create a service principal.
        
        Creates a new service principal in the Databricks Workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ServicePrincipal(active=active,
                                       application_id=application_id,
                                       display_name=display_name,
                                       entitlements=entitlements,
                                       external_id=external_id,
                                       groups=groups,
                                       id=id,
                                       roles=roles)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/preview/scim/v2/ServicePrincipals', body=body)
        return ServicePrincipal.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a service principal.
        
        Delete a single service principal in the Databricks Workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteServicePrincipalRequest(id=id)

        self._api.do('DELETE', f'/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}')

    def get(self, id: str, **kwargs) -> ServicePrincipal:
        """Get service principal details.
        
        Gets the details for a single service principal define in the Databricks Workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetServicePrincipalRequest(id=id)

        json = self._api.do('GET', f'/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}')
        return ServicePrincipal.from_dict(json)

    def list(self,
             *,
             attributes: str = None,
             count: int = None,
             excluded_attributes: str = None,
             filter: str = None,
             sort_by: str = None,
             sort_order: ListSortOrder = None,
             start_index: int = None,
             **kwargs) -> Iterator[ServicePrincipal]:
        """List service principals.
        
        Gets the set of service principals associated with a Databricks Workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListServicePrincipalsRequest(attributes=attributes,
                                                   count=count,
                                                   excluded_attributes=excluded_attributes,
                                                   filter=filter,
                                                   sort_by=sort_by,
                                                   sort_order=sort_order,
                                                   start_index=start_index)

        query = {}
        if attributes: query['attributes'] = request.attributes
        if count: query['count'] = request.count
        if excluded_attributes: query['excludedAttributes'] = request.excluded_attributes
        if filter: query['filter'] = request.filter
        if sort_by: query['sortBy'] = request.sort_by
        if sort_order: query['sortOrder'] = request.sort_order.value
        if start_index: query['startIndex'] = request.start_index

        json = self._api.do('GET', '/api/2.0/preview/scim/v2/ServicePrincipals', query=query)
        return [ServicePrincipal.from_dict(v) for v in json.get('Resources', [])]

    def patch(self, id: str, *, operations: List[Patch] = None, **kwargs):
        """Update service principal details.
        
        Partially updates the details of a single service principal in the Databricks Workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}', body=body)

    def update(self,
               id: str,
               *,
               active: bool = None,
               application_id: str = None,
               display_name: str = None,
               entitlements: List[ComplexValue] = None,
               external_id: str = None,
               groups: List[ComplexValue] = None,
               roles: List[ComplexValue] = None,
               **kwargs):
        """Replace service principal.
        
        Updates the details of a single service principal.
        
        This action replaces the existing service principal with the same name."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ServicePrincipal(active=active,
                                       application_id=application_id,
                                       display_name=display_name,
                                       entitlements=entitlements,
                                       external_id=external_id,
                                       groups=groups,
                                       id=id,
                                       roles=roles)
        body = request.as_dict()
        self._api.do('PUT', f'/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}', body=body)


class UsersAPI:
    """User identities recognized by Databricks and represented by email addresses.
    
    Databricks recommends using SCIM provisioning to sync users and groups automatically from your identity
    provider to your Databricks Workspace. SCIM streamlines onboarding a new employee or team by using your
    identity provider to create users and groups in Databricks Workspace and give them the proper level of
    access. When a user leaves your organization or no longer needs access to Databricks Workspace, admins can
    terminate the user in your identity provider and that user’s account will also be removed from
    Databricks Workspace. This ensures a consistent offboarding process and prevents unauthorized users from
    accessing sensitive data."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               id: str,
               *,
               active: bool = None,
               display_name: str = None,
               emails: List[ComplexValue] = None,
               entitlements: List[ComplexValue] = None,
               external_id: str = None,
               groups: List[ComplexValue] = None,
               name: Name = None,
               roles: List[ComplexValue] = None,
               user_name: str = None,
               **kwargs) -> User:
        """Create a new user.
        
        Creates a new user in the Databricks Workspace. This new user will also be added to the Databricks
        account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = User(active=active,
                           display_name=display_name,
                           emails=emails,
                           entitlements=entitlements,
                           external_id=external_id,
                           groups=groups,
                           id=id,
                           name=name,
                           roles=roles,
                           user_name=user_name)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/preview/scim/v2/Users', body=body)
        return User.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a user.
        
        Deletes a user. Deleting a user from a Databricks Workspace also removes objects associated with the
        user."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteUserRequest(id=id)

        self._api.do('DELETE', f'/api/2.0/preview/scim/v2/Users/{request.id}')

    def get(self, id: str, **kwargs) -> User:
        """Get user details.
        
        Gets information for a specific user in Databricks Workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetUserRequest(id=id)

        json = self._api.do('GET', f'/api/2.0/preview/scim/v2/Users/{request.id}')
        return User.from_dict(json)

    def list(self,
             *,
             attributes: str = None,
             count: int = None,
             excluded_attributes: str = None,
             filter: str = None,
             sort_by: str = None,
             sort_order: ListSortOrder = None,
             start_index: int = None,
             **kwargs) -> Iterator[User]:
        """List users.
        
        Gets details for all the users associated with a Databricks Workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListUsersRequest(attributes=attributes,
                                       count=count,
                                       excluded_attributes=excluded_attributes,
                                       filter=filter,
                                       sort_by=sort_by,
                                       sort_order=sort_order,
                                       start_index=start_index)

        query = {}
        if attributes: query['attributes'] = request.attributes
        if count: query['count'] = request.count
        if excluded_attributes: query['excludedAttributes'] = request.excluded_attributes
        if filter: query['filter'] = request.filter
        if sort_by: query['sortBy'] = request.sort_by
        if sort_order: query['sortOrder'] = request.sort_order.value
        if start_index: query['startIndex'] = request.start_index

        json = self._api.do('GET', '/api/2.0/preview/scim/v2/Users', query=query)
        return [User.from_dict(v) for v in json.get('Resources', [])]

    def patch(self, id: str, *, operations: List[Patch] = None, **kwargs):
        """Update user details.
        
        Partially updates a user resource by applying the supplied operations on specific user attributes."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.0/preview/scim/v2/Users/{request.id}', body=body)

    def update(self,
               id: str,
               *,
               active: bool = None,
               display_name: str = None,
               emails: List[ComplexValue] = None,
               entitlements: List[ComplexValue] = None,
               external_id: str = None,
               groups: List[ComplexValue] = None,
               name: Name = None,
               roles: List[ComplexValue] = None,
               user_name: str = None,
               **kwargs):
        """Replace a user.
        
        Replaces a user's information with the data supplied in request."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = User(active=active,
                           display_name=display_name,
                           emails=emails,
                           entitlements=entitlements,
                           external_id=external_id,
                           groups=groups,
                           id=id,
                           name=name,
                           roles=roles,
                           user_name=user_name)
        body = request.as_dict()
        self._api.do('PUT', f'/api/2.0/preview/scim/v2/Users/{request.id}', body=body)


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

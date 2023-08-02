# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AccessControlRequest:
    group_name: Optional[str] = None
    permission_level: Optional['PermissionLevel'] = None
    service_principal_name: Optional[str] = None
    user_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AccessControlRequest':
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', PermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class AccessControlResponse:
    all_permissions: Optional['List[Permission]'] = None
    group_name: Optional[str] = None
    service_principal_name: Optional[str] = None
    user_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.all_permissions: body['all_permissions'] = [v.as_dict() for v in self.all_permissions]
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AccessControlResponse':
        return cls(all_permissions=_repeated(d, 'all_permissions', Permission),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class ComplexValue:
    display: Optional[str] = None
    primary: Optional[bool] = None
    type: Optional[str] = None
    value: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.display is not None: body['display'] = self.display
        if self.primary is not None: body['primary'] = self.primary
        if self.type is not None: body['type'] = self.type
        if self.value is not None: body['value'] = self.value
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
class GetAssignableRolesForResourceRequest:
    """Get assignable roles for a resource"""

    resource: str


@dataclass
class GetAssignableRolesForResourceResponse:
    roles: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.roles: body['roles'] = [v for v in self.roles]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetAssignableRolesForResourceResponse':
        return cls(roles=d.get('roles', None))


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
    permission_levels: Optional['List[PermissionsDescription]'] = None

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
class GetRuleSetRequest:
    """Get a rule set"""

    name: str
    etag: str


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
class GrantRule:
    role: str
    principals: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.principals: body['principals'] = [v for v in self.principals]
        if self.role is not None: body['role'] = self.role
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GrantRule':
        return cls(principals=d.get('principals', None), role=d.get('role', None))


@dataclass
class Group:
    display_name: Optional[str] = None
    entitlements: Optional['List[ComplexValue]'] = None
    external_id: Optional[str] = None
    groups: Optional['List[ComplexValue]'] = None
    id: Optional[str] = None
    members: Optional['List[ComplexValue]'] = None
    meta: Optional['ResourceMeta'] = None
    roles: Optional['List[ComplexValue]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.display_name is not None: body['displayName'] = self.display_name
        if self.entitlements: body['entitlements'] = [v.as_dict() for v in self.entitlements]
        if self.external_id is not None: body['externalId'] = self.external_id
        if self.groups: body['groups'] = [v.as_dict() for v in self.groups]
        if self.id is not None: body['id'] = self.id
        if self.members: body['members'] = [v.as_dict() for v in self.members]
        if self.meta: body['meta'] = self.meta.as_dict()
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
                   meta=_from_dict(d, 'meta', ResourceMeta),
                   roles=_repeated(d, 'roles', ComplexValue))


@dataclass
class ListAccountGroupsRequest:
    """List group details"""

    attributes: Optional[str] = None
    count: Optional[int] = None
    excluded_attributes: Optional[str] = None
    filter: Optional[str] = None
    sort_by: Optional[str] = None
    sort_order: Optional['ListSortOrder'] = None
    start_index: Optional[int] = None


@dataclass
class ListAccountServicePrincipalsRequest:
    """List service principals"""

    attributes: Optional[str] = None
    count: Optional[int] = None
    excluded_attributes: Optional[str] = None
    filter: Optional[str] = None
    sort_by: Optional[str] = None
    sort_order: Optional['ListSortOrder'] = None
    start_index: Optional[int] = None


@dataclass
class ListAccountUsersRequest:
    """List users"""

    attributes: Optional[str] = None
    count: Optional[int] = None
    excluded_attributes: Optional[str] = None
    filter: Optional[str] = None
    sort_by: Optional[str] = None
    sort_order: Optional['ListSortOrder'] = None
    start_index: Optional[int] = None


@dataclass
class ListGroupsRequest:
    """List group details"""

    attributes: Optional[str] = None
    count: Optional[int] = None
    excluded_attributes: Optional[str] = None
    filter: Optional[str] = None
    sort_by: Optional[str] = None
    sort_order: Optional['ListSortOrder'] = None
    start_index: Optional[int] = None


@dataclass
class ListGroupsResponse:
    items_per_page: Optional[int] = None
    resources: Optional['List[Group]'] = None
    start_index: Optional[int] = None
    total_results: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.items_per_page is not None: body['itemsPerPage'] = self.items_per_page
        if self.resources: body['Resources'] = [v.as_dict() for v in self.resources]
        if self.start_index is not None: body['startIndex'] = self.start_index
        if self.total_results is not None: body['totalResults'] = self.total_results
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListGroupsResponse':
        return cls(items_per_page=d.get('itemsPerPage', None),
                   resources=_repeated(d, 'Resources', Group),
                   start_index=d.get('startIndex', None),
                   total_results=d.get('totalResults', None))


@dataclass
class ListServicePrincipalResponse:
    items_per_page: Optional[int] = None
    resources: Optional['List[ServicePrincipal]'] = None
    start_index: Optional[int] = None
    total_results: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.items_per_page is not None: body['itemsPerPage'] = self.items_per_page
        if self.resources: body['Resources'] = [v.as_dict() for v in self.resources]
        if self.start_index is not None: body['startIndex'] = self.start_index
        if self.total_results is not None: body['totalResults'] = self.total_results
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

    attributes: Optional[str] = None
    count: Optional[int] = None
    excluded_attributes: Optional[str] = None
    filter: Optional[str] = None
    sort_by: Optional[str] = None
    sort_order: Optional['ListSortOrder'] = None
    start_index: Optional[int] = None


class ListSortOrder(Enum):

    ASCENDING = 'ascending'
    DESCENDING = 'descending'


@dataclass
class ListUsersRequest:
    """List users"""

    attributes: Optional[str] = None
    count: Optional[int] = None
    excluded_attributes: Optional[str] = None
    filter: Optional[str] = None
    sort_by: Optional[str] = None
    sort_order: Optional['ListSortOrder'] = None
    start_index: Optional[int] = None


@dataclass
class ListUsersResponse:
    items_per_page: Optional[int] = None
    resources: Optional['List[User]'] = None
    start_index: Optional[int] = None
    total_results: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.items_per_page is not None: body['itemsPerPage'] = self.items_per_page
        if self.resources: body['Resources'] = [v.as_dict() for v in self.resources]
        if self.start_index is not None: body['startIndex'] = self.start_index
        if self.total_results is not None: body['totalResults'] = self.total_results
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
    family_name: Optional[str] = None
    given_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.family_name is not None: body['familyName'] = self.family_name
        if self.given_name is not None: body['givenName'] = self.given_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Name':
        return cls(family_name=d.get('familyName', None), given_name=d.get('givenName', None))


@dataclass
class ObjectPermissions:
    access_control_list: Optional['List[AccessControlResponse]'] = None
    object_id: Optional[str] = None
    object_type: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None: body['object_id'] = self.object_id
        if self.object_type is not None: body['object_type'] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ObjectPermissions':
        return cls(access_control_list=_repeated(d, 'access_control_list', AccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class PartialUpdate:
    id: Optional[str] = None
    operations: Optional['List[Patch]'] = None
    schema: Optional['List[PatchSchema]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.id is not None: body['id'] = self.id
        if self.operations: body['Operations'] = [v.as_dict() for v in self.operations]
        if self.schema: body['schema'] = [v.value for v in self.schema]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PartialUpdate':
        return cls(id=d.get('id', None),
                   operations=_repeated(d, 'Operations', Patch),
                   schema=d.get('schema', None))


@dataclass
class Patch:
    op: Optional['PatchOp'] = None
    path: Optional[str] = None
    value: Optional[Any] = None

    def as_dict(self) -> dict:
        body = {}
        if self.op is not None: body['op'] = self.op.value
        if self.path is not None: body['path'] = self.path
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Patch':
        return cls(op=_enum(d, 'op', PatchOp), path=d.get('path', None), value=d.get('value', None))


class PatchOp(Enum):
    """Type of patch operation."""

    ADD = 'add'
    REMOVE = 'remove'
    REPLACE = 'replace'


class PatchSchema(Enum):

    URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_PATCH_OP = 'urn:ietf:params:scim:api:messages:2.0:PatchOp'


@dataclass
class Permission:
    inherited: Optional[bool] = None
    inherited_from_object: Optional['List[str]'] = None
    permission_level: Optional['PermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Permission':
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', PermissionLevel))


@dataclass
class PermissionAssignment:
    error: Optional[str] = None
    permissions: Optional['List[WorkspacePermission]'] = None
    principal: Optional['PrincipalOutput'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.error is not None: body['error'] = self.error
        if self.permissions: body['permissions'] = [v.value for v in self.permissions]
        if self.principal: body['principal'] = self.principal.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermissionAssignment':
        return cls(error=d.get('error', None),
                   permissions=d.get('permissions', None),
                   principal=_from_dict(d, 'principal', PrincipalOutput))


@dataclass
class PermissionAssignments:
    permission_assignments: Optional['List[PermissionAssignment]'] = None

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
    description: Optional[str] = None
    permission_level: Optional['WorkspacePermission'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermissionOutput':
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', WorkspacePermission))


@dataclass
class PermissionsDescription:
    description: Optional[str] = None
    permission_level: Optional['PermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermissionsDescription':
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', PermissionLevel))


@dataclass
class PermissionsRequest:
    access_control_list: Optional['List[AccessControlRequest]'] = None
    request_object_id: Optional[str] = None
    request_object_type: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.request_object_id is not None: body['request_object_id'] = self.request_object_id
        if self.request_object_type is not None: body['request_object_type'] = self.request_object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermissionsRequest':
        return cls(access_control_list=_repeated(d, 'access_control_list', AccessControlRequest),
                   request_object_id=d.get('request_object_id', None),
                   request_object_type=d.get('request_object_type', None))


@dataclass
class PrincipalOutput:
    display_name: Optional[str] = None
    group_name: Optional[str] = None
    principal_id: Optional[int] = None
    service_principal_name: Optional[str] = None
    user_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.principal_id is not None: body['principal_id'] = self.principal_id
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PrincipalOutput':
        return cls(display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   principal_id=d.get('principal_id', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class ResourceMeta:
    resource_type: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.resource_type is not None: body['resourceType'] = self.resource_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResourceMeta':
        return cls(resource_type=d.get('resourceType', None))


@dataclass
class RuleSetResponse:
    etag: Optional[str] = None
    grant_rules: Optional['List[GrantRule]'] = None
    name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        if self.grant_rules: body['grant_rules'] = [v.as_dict() for v in self.grant_rules]
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RuleSetResponse':
        return cls(etag=d.get('etag', None),
                   grant_rules=_repeated(d, 'grant_rules', GrantRule),
                   name=d.get('name', None))


@dataclass
class RuleSetUpdateRequest:
    name: str
    etag: str
    grant_rules: Optional['List[GrantRule]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        if self.grant_rules: body['grant_rules'] = [v.as_dict() for v in self.grant_rules]
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RuleSetUpdateRequest':
        return cls(etag=d.get('etag', None),
                   grant_rules=_repeated(d, 'grant_rules', GrantRule),
                   name=d.get('name', None))


@dataclass
class ServicePrincipal:
    active: Optional[bool] = None
    application_id: Optional[str] = None
    display_name: Optional[str] = None
    entitlements: Optional['List[ComplexValue]'] = None
    external_id: Optional[str] = None
    groups: Optional['List[ComplexValue]'] = None
    id: Optional[str] = None
    roles: Optional['List[ComplexValue]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.active is not None: body['active'] = self.active
        if self.application_id is not None: body['applicationId'] = self.application_id
        if self.display_name is not None: body['displayName'] = self.display_name
        if self.entitlements: body['entitlements'] = [v.as_dict() for v in self.entitlements]
        if self.external_id is not None: body['externalId'] = self.external_id
        if self.groups: body['groups'] = [v.as_dict() for v in self.groups]
        if self.id is not None: body['id'] = self.id
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
class UpdateRuleSetRequest:
    name: str
    rule_set: 'RuleSetUpdateRequest'

    def as_dict(self) -> dict:
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.rule_set: body['rule_set'] = self.rule_set.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateRuleSetRequest':
        return cls(name=d.get('name', None), rule_set=_from_dict(d, 'rule_set', RuleSetUpdateRequest))


@dataclass
class UpdateWorkspaceAssignments:
    permissions: 'List[WorkspacePermission]'
    principal_id: Optional[int] = None
    workspace_id: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.permissions: body['permissions'] = [v.value for v in self.permissions]
        if self.principal_id is not None: body['principal_id'] = self.principal_id
        if self.workspace_id is not None: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateWorkspaceAssignments':
        return cls(permissions=d.get('permissions', None),
                   principal_id=d.get('principal_id', None),
                   workspace_id=d.get('workspace_id', None))


@dataclass
class User:
    active: Optional[bool] = None
    display_name: Optional[str] = None
    emails: Optional['List[ComplexValue]'] = None
    entitlements: Optional['List[ComplexValue]'] = None
    external_id: Optional[str] = None
    groups: Optional['List[ComplexValue]'] = None
    id: Optional[str] = None
    name: Optional['Name'] = None
    roles: Optional['List[ComplexValue]'] = None
    user_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.active is not None: body['active'] = self.active
        if self.display_name is not None: body['displayName'] = self.display_name
        if self.emails: body['emails'] = [v.as_dict() for v in self.emails]
        if self.entitlements: body['entitlements'] = [v.as_dict() for v in self.entitlements]
        if self.external_id is not None: body['externalId'] = self.external_id
        if self.groups: body['groups'] = [v.as_dict() for v in self.groups]
        if self.id is not None: body['id'] = self.id
        if self.name: body['name'] = self.name.as_dict()
        if self.roles: body['roles'] = [v.as_dict() for v in self.roles]
        if self.user_name is not None: body['userName'] = self.user_name
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
    permissions: Optional['List[PermissionOutput]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.permissions: body['permissions'] = [v.as_dict() for v in self.permissions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WorkspacePermissions':
        return cls(permissions=_repeated(d, 'permissions', PermissionOutput))


class AccountAccessControlAPI:
    """These APIs manage access rules on resources in an account. Currently, only grant rules are supported. A
    grant rule specifies a role assigned to a set of principals. A list of rules attached to a resource is
    called a rule set."""

    def __init__(self, api_client):
        self._api = api_client

    def get_assignable_roles_for_resource(self, resource: str,
                                          **kwargs) -> GetAssignableRolesForResourceResponse:
        """Get assignable roles for a resource.
        
        Gets all the roles that can be granted on an account level resource. A role is grantable if the rule
        set on the resource can contain an access rule of the role.
        
        :param resource: str
          The resource name for which assignable roles will be listed.
        
        :returns: :class:`GetAssignableRolesForResourceResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAssignableRolesForResourceRequest(resource=resource)

        query = {}
        if resource: query['resource'] = request.resource

        json = self._api.do(
            'GET',
            f'/api/2.0/preview/accounts/{self._api.account_id}/access-control/assignable-roles',
            query=query)
        return GetAssignableRolesForResourceResponse.from_dict(json)

    def get_rule_set(self, name: str, etag: str, **kwargs) -> RuleSetResponse:
        """Get a rule set.
        
        Get a rule set by its name. A rule set is always attached to a resource and contains a list of access
        rules on the said resource. Currently only a default rule set for each resource is supported.
        
        :param name: str
          The ruleset name associated with the request.
        :param etag: str
          Etag used for versioning. The response is at least as fresh as the eTag provided. Etag is used for
          optimistic concurrency control as a way to help prevent simultaneous updates of a rule set from
          overwriting each other. It is strongly suggested that systems make use of the etag in the read ->
          modify -> write pattern to perform rule set updates in order to avoid race conditions that is get an
          etag from a GET rule set request, and pass it with the PUT update request to identify the rule set
          version you are updating.
        
        :returns: :class:`RuleSetResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetRuleSetRequest(etag=etag, name=name)

        query = {}
        if etag: query['etag'] = request.etag
        if name: query['name'] = request.name

        json = self._api.do('GET',
                            f'/api/2.0/preview/accounts/{self._api.account_id}/access-control/rule-sets',
                            query=query)
        return RuleSetResponse.from_dict(json)

    def update_rule_set(self, name: str, rule_set: RuleSetUpdateRequest, **kwargs) -> RuleSetResponse:
        """Update a rule set.
        
        Replace the rules of a rule set. First, use get to read the current version of the rule set before
        modifying it. This pattern helps prevent conflicts between concurrent updates.
        
        :param name: str
          Name of the rule set.
        :param rule_set: :class:`RuleSetUpdateRequest`
        
        :returns: :class:`RuleSetResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateRuleSetRequest(name=name, rule_set=rule_set)
        body = request.as_dict()

        json = self._api.do('PUT',
                            f'/api/2.0/preview/accounts/{self._api.account_id}/access-control/rule-sets',
                            body=body)
        return RuleSetResponse.from_dict(json)


class AccountAccessControlProxyAPI:
    """These APIs manage access rules on resources in an account. Currently, only grant rules are supported. A
    grant rule specifies a role assigned to a set of principals. A list of rules attached to a resource is
    called a rule set. A workspace must belong to an account for these APIs to work."""

    def __init__(self, api_client):
        self._api = api_client

    def get_assignable_roles_for_resource(self, resource: str,
                                          **kwargs) -> GetAssignableRolesForResourceResponse:
        """Get assignable roles for a resource.
        
        Gets all the roles that can be granted on an account-level resource. A role is grantable if the rule
        set on the resource can contain an access rule of the role.
        
        :param resource: str
          The resource name for which assignable roles will be listed.
        
        :returns: :class:`GetAssignableRolesForResourceResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAssignableRolesForResourceRequest(resource=resource)

        query = {}
        if resource: query['resource'] = request.resource

        json = self._api.do('GET', '/api/2.0/preview/accounts/access-control/assignable-roles', query=query)
        return GetAssignableRolesForResourceResponse.from_dict(json)

    def get_rule_set(self, name: str, etag: str, **kwargs) -> RuleSetResponse:
        """Get a rule set.
        
        Get a rule set by its name. A rule set is always attached to a resource and contains a list of access
        rules on the said resource. Currently only a default rule set for each resource is supported.
        
        :param name: str
          The ruleset name associated with the request.
        :param etag: str
          Etag used for versioning. The response is at least as fresh as the eTag provided. Etag is used for
          optimistic concurrency control as a way to help prevent simultaneous updates of a rule set from
          overwriting each other. It is strongly suggested that systems make use of the etag in the read ->
          modify -> write pattern to perform rule set updates in order to avoid race conditions that is get an
          etag from a GET rule set request, and pass it with the PUT update request to identify the rule set
          version you are updating.
        
        :returns: :class:`RuleSetResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetRuleSetRequest(etag=etag, name=name)

        query = {}
        if etag: query['etag'] = request.etag
        if name: query['name'] = request.name

        json = self._api.do('GET', '/api/2.0/preview/accounts/access-control/rule-sets', query=query)
        return RuleSetResponse.from_dict(json)

    def update_rule_set(self, name: str, rule_set: RuleSetUpdateRequest, **kwargs) -> RuleSetResponse:
        """Update a rule set.
        
        Replace the rules of a rule set. First, use a GET rule set request to read the current version of the
        rule set before modifying it. This pattern helps prevent conflicts between concurrent updates.
        
        :param name: str
          Name of the rule set.
        :param rule_set: :class:`RuleSetUpdateRequest`
        
        :returns: :class:`RuleSetResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateRuleSetRequest(name=name, rule_set=rule_set)
        body = request.as_dict()

        json = self._api.do('PUT', '/api/2.0/preview/accounts/access-control/rule-sets', body=body)
        return RuleSetResponse.from_dict(json)


class AccountGroupsAPI:
    """Groups simplify identity management, making it easier to assign access to Databricks account, data, and
    other securable objects.
    
    It is best practice to assign access to workspaces and access-control policies in Unity Catalog to groups,
    instead of to users individually. All Databricks account identities can be assigned as members of groups,
    and members inherit permissions that are assigned to their group."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               display_name: Optional[str] = None,
               entitlements: Optional[List[ComplexValue]] = None,
               external_id: Optional[str] = None,
               groups: Optional[List[ComplexValue]] = None,
               id: Optional[str] = None,
               members: Optional[List[ComplexValue]] = None,
               meta: Optional[ResourceMeta] = None,
               roles: Optional[List[ComplexValue]] = None,
               **kwargs) -> Group:
        """Create a new group.
        
        Creates a group in the Databricks account with a unique name, using the supplied group details.
        
        :param display_name: str (optional)
          String that represents a human-readable group name
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks group ID
        :param members: List[:class:`ComplexValue`] (optional)
        :param meta: :class:`ResourceMeta` (optional)
          Container for the group identifier. Workspace local versus account.
        :param roles: List[:class:`ComplexValue`] (optional)
        
        :returns: :class:`Group`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Group(display_name=display_name,
                            entitlements=entitlements,
                            external_id=external_id,
                            groups=groups,
                            id=id,
                            members=members,
                            meta=meta,
                            roles=roles)
        body = request.as_dict()

        json = self._api.do('POST', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups', body=body)
        return Group.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a group.
        
        Deletes a group from the Databricks account.
        
        :param id: str
          Unique ID for a group in the Databricks account.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteAccountGroupRequest(id=id)

        self._api.do('DELETE', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups/{request.id}')

    def get(self, id: str, **kwargs) -> Group:
        """Get group details.
        
        Gets the information for a specific group in the Databricks account.
        
        :param id: str
          Unique ID for a group in the Databricks account.
        
        :returns: :class:`Group`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAccountGroupRequest(id=id)

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups/{request.id}')
        return Group.from_dict(json)

    def list(self,
             *,
             attributes: Optional[str] = None,
             count: Optional[int] = None,
             excluded_attributes: Optional[str] = None,
             filter: Optional[str] = None,
             sort_by: Optional[str] = None,
             sort_order: Optional[ListSortOrder] = None,
             start_index: Optional[int] = None,
             **kwargs) -> Iterator[Group]:
        """List group details.
        
        Gets all details of the groups associated with the Databricks account.
        
        :param attributes: str (optional)
          Comma-separated list of attributes to return in response.
        :param count: int (optional)
          Desired number of results per page. Default is 10000.
        :param excluded_attributes: str (optional)
          Comma-separated list of attributes to exclude in response.
        :param filter: str (optional)
          Query by which the results have to be filtered. Supported operators are equals(`eq`),
          contains(`co`), starts with(`sw`) and not equals(`ne`). Additionally, simple expressions can be
          formed using logical operators - `and` and `or`. The [SCIM RFC] has more details but we currently
          only support simple expressions.
          
          [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
        :param sort_by: str (optional)
          Attribute to sort the results.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: Iterator over :class:`Group`
        """
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

    def patch(self,
              id: str,
              *,
              operations: Optional[List[Patch]] = None,
              schema: Optional[List[PatchSchema]] = None,
              **kwargs):
        """Update group details.
        
        Partially updates the details of a group.
        
        :param id: str
          Unique ID for a group in the Databricks account.
        :param operations: List[:class:`Patch`] (optional)
        :param schema: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations, schema=schema)
        body = request.as_dict()
        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups/{request.id}',
                     body=body)

    def update(self,
               id: str,
               *,
               display_name: Optional[str] = None,
               entitlements: Optional[List[ComplexValue]] = None,
               external_id: Optional[str] = None,
               groups: Optional[List[ComplexValue]] = None,
               members: Optional[List[ComplexValue]] = None,
               meta: Optional[ResourceMeta] = None,
               roles: Optional[List[ComplexValue]] = None,
               **kwargs):
        """Replace a group.
        
        Updates the details of a group by replacing the entire group entity.
        
        :param id: str
          Databricks group ID
        :param display_name: str (optional)
          String that represents a human-readable group name
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param members: List[:class:`ComplexValue`] (optional)
        :param meta: :class:`ResourceMeta` (optional)
          Container for the group identifier. Workspace local versus account.
        :param roles: List[:class:`ComplexValue`] (optional)
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Group(display_name=display_name,
                            entitlements=entitlements,
                            external_id=external_id,
                            groups=groups,
                            id=id,
                            members=members,
                            meta=meta,
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
               *,
               active: Optional[bool] = None,
               application_id: Optional[str] = None,
               display_name: Optional[str] = None,
               entitlements: Optional[List[ComplexValue]] = None,
               external_id: Optional[str] = None,
               groups: Optional[List[ComplexValue]] = None,
               id: Optional[str] = None,
               roles: Optional[List[ComplexValue]] = None,
               **kwargs) -> ServicePrincipal:
        """Create a service principal.
        
        Creates a new service principal in the Databricks account.
        
        :param active: bool (optional)
          If this user is active
        :param application_id: str (optional)
          UUID relating to the service principal
        :param display_name: str (optional)
          String that represents a concatenation of given and family names.
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks service principal ID.
        :param roles: List[:class:`ComplexValue`] (optional)
        
        :returns: :class:`ServicePrincipal`
        """
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
        
        Delete a single service principal in the Databricks account.
        
        :param id: str
          Unique ID for a service principal in the Databricks account.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteAccountServicePrincipalRequest(id=id)

        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals/{request.id}')

    def get(self, id: str, **kwargs) -> ServicePrincipal:
        """Get service principal details.
        
        Gets the details for a single service principal define in the Databricks account.
        
        :param id: str
          Unique ID for a service principal in the Databricks account.
        
        :returns: :class:`ServicePrincipal`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAccountServicePrincipalRequest(id=id)

        json = self._api.do(
            'GET', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals/{request.id}')
        return ServicePrincipal.from_dict(json)

    def list(self,
             *,
             attributes: Optional[str] = None,
             count: Optional[int] = None,
             excluded_attributes: Optional[str] = None,
             filter: Optional[str] = None,
             sort_by: Optional[str] = None,
             sort_order: Optional[ListSortOrder] = None,
             start_index: Optional[int] = None,
             **kwargs) -> Iterator[ServicePrincipal]:
        """List service principals.
        
        Gets the set of service principals associated with a Databricks account.
        
        :param attributes: str (optional)
          Comma-separated list of attributes to return in response.
        :param count: int (optional)
          Desired number of results per page. Default is 10000.
        :param excluded_attributes: str (optional)
          Comma-separated list of attributes to exclude in response.
        :param filter: str (optional)
          Query by which the results have to be filtered. Supported operators are equals(`eq`),
          contains(`co`), starts with(`sw`) and not equals(`ne`). Additionally, simple expressions can be
          formed using logical operators - `and` and `or`. The [SCIM RFC] has more details but we currently
          only support simple expressions.
          
          [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
        :param sort_by: str (optional)
          Attribute to sort the results.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: Iterator over :class:`ServicePrincipal`
        """
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

    def patch(self,
              id: str,
              *,
              operations: Optional[List[Patch]] = None,
              schema: Optional[List[PatchSchema]] = None,
              **kwargs):
        """Update service principal details.
        
        Partially updates the details of a single service principal in the Databricks account.
        
        :param id: str
          Unique ID for a service principal in the Databricks account.
        :param operations: List[:class:`Patch`] (optional)
        :param schema: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations, schema=schema)
        body = request.as_dict()
        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals/{request.id}',
                     body=body)

    def update(self,
               id: str,
               *,
               active: Optional[bool] = None,
               application_id: Optional[str] = None,
               display_name: Optional[str] = None,
               entitlements: Optional[List[ComplexValue]] = None,
               external_id: Optional[str] = None,
               groups: Optional[List[ComplexValue]] = None,
               roles: Optional[List[ComplexValue]] = None,
               **kwargs):
        """Replace service principal.
        
        Updates the details of a single service principal.
        
        This action replaces the existing service principal with the same name.
        
        :param id: str
          Databricks service principal ID.
        :param active: bool (optional)
          If this user is active
        :param application_id: str (optional)
          UUID relating to the service principal
        :param display_name: str (optional)
          String that represents a concatenation of given and family names.
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
        
        
        """
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
    provider to your Databricks account. SCIM streamlines onboarding a new employee or team by using your
    identity provider to create users and groups in Databricks account and give them the proper level of
    access. When a user leaves your organization or no longer needs access to Databricks account, admins can
    terminate the user in your identity provider and that user’s account will also be removed from
    Databricks account. This ensures a consistent offboarding process and prevents unauthorized users from
    accessing sensitive data."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               active: Optional[bool] = None,
               display_name: Optional[str] = None,
               emails: Optional[List[ComplexValue]] = None,
               entitlements: Optional[List[ComplexValue]] = None,
               external_id: Optional[str] = None,
               groups: Optional[List[ComplexValue]] = None,
               id: Optional[str] = None,
               name: Optional[Name] = None,
               roles: Optional[List[ComplexValue]] = None,
               user_name: Optional[str] = None,
               **kwargs) -> User:
        """Create a new user.
        
        Creates a new user in the Databricks account. This new user will also be added to the Databricks
        account.
        
        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`.
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks user ID.
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
        :param user_name: str (optional)
          Email address of the Databricks user.
        
        :returns: :class:`User`
        """
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
        
        Deletes a user. Deleting a user from a Databricks account also removes objects associated with the
        user.
        
        :param id: str
          Unique ID for a user in the Databricks account.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteAccountUserRequest(id=id)

        self._api.do('DELETE', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users/{request.id}')

    def get(self, id: str, **kwargs) -> User:
        """Get user details.
        
        Gets information for a specific user in Databricks account.
        
        :param id: str
          Unique ID for a user in the Databricks account.
        
        :returns: :class:`User`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAccountUserRequest(id=id)

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users/{request.id}')
        return User.from_dict(json)

    def list(self,
             *,
             attributes: Optional[str] = None,
             count: Optional[int] = None,
             excluded_attributes: Optional[str] = None,
             filter: Optional[str] = None,
             sort_by: Optional[str] = None,
             sort_order: Optional[ListSortOrder] = None,
             start_index: Optional[int] = None,
             **kwargs) -> Iterator[User]:
        """List users.
        
        Gets details for all the users associated with a Databricks account.
        
        :param attributes: str (optional)
          Comma-separated list of attributes to return in response.
        :param count: int (optional)
          Desired number of results per page. Default is 10000.
        :param excluded_attributes: str (optional)
          Comma-separated list of attributes to exclude in response.
        :param filter: str (optional)
          Query by which the results have to be filtered. Supported operators are equals(`eq`),
          contains(`co`), starts with(`sw`) and not equals(`ne`). Additionally, simple expressions can be
          formed using logical operators - `and` and `or`. The [SCIM RFC] has more details but we currently
          only support simple expressions.
          
          [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
        :param sort_by: str (optional)
          Attribute to sort the results. Multi-part paths are supported. For example, `userName`,
          `name.givenName`, and `emails`.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: Iterator over :class:`User`
        """
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

    def patch(self,
              id: str,
              *,
              operations: Optional[List[Patch]] = None,
              schema: Optional[List[PatchSchema]] = None,
              **kwargs):
        """Update user details.
        
        Partially updates a user resource by applying the supplied operations on specific user attributes.
        
        :param id: str
          Unique ID for a user in the Databricks account.
        :param operations: List[:class:`Patch`] (optional)
        :param schema: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations, schema=schema)
        body = request.as_dict()
        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users/{request.id}',
                     body=body)

    def update(self,
               id: str,
               *,
               active: Optional[bool] = None,
               display_name: Optional[str] = None,
               emails: Optional[List[ComplexValue]] = None,
               entitlements: Optional[List[ComplexValue]] = None,
               external_id: Optional[str] = None,
               groups: Optional[List[ComplexValue]] = None,
               name: Optional[Name] = None,
               roles: Optional[List[ComplexValue]] = None,
               user_name: Optional[str] = None,
               **kwargs):
        """Replace a user.
        
        Replaces a user's information with the data supplied in request.
        
        :param id: str
          Databricks user ID.
        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`.
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
        :param user_name: str (optional)
          Email address of the Databricks user.
        
        
        """
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
        
        Get details about the current method caller's identity.
        
        :returns: :class:`User`
        """

        json = self._api.do('GET', '/api/2.0/preview/scim/v2/Me')
        return User.from_dict(json)


class GroupsAPI:
    """Groups simplify identity management, making it easier to assign access to Databricks workspace, data, and
    other securable objects.
    
    It is best practice to assign access to workspaces and access-control policies in Unity Catalog to groups,
    instead of to users individually. All Databricks workspace identities can be assigned as members of
    groups, and members inherit permissions that are assigned to their group."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               display_name: Optional[str] = None,
               entitlements: Optional[List[ComplexValue]] = None,
               external_id: Optional[str] = None,
               groups: Optional[List[ComplexValue]] = None,
               id: Optional[str] = None,
               members: Optional[List[ComplexValue]] = None,
               meta: Optional[ResourceMeta] = None,
               roles: Optional[List[ComplexValue]] = None,
               **kwargs) -> Group:
        """Create a new group.
        
        Creates a group in the Databricks workspace with a unique name, using the supplied group details.
        
        :param display_name: str (optional)
          String that represents a human-readable group name
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks group ID
        :param members: List[:class:`ComplexValue`] (optional)
        :param meta: :class:`ResourceMeta` (optional)
          Container for the group identifier. Workspace local versus account.
        :param roles: List[:class:`ComplexValue`] (optional)
        
        :returns: :class:`Group`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Group(display_name=display_name,
                            entitlements=entitlements,
                            external_id=external_id,
                            groups=groups,
                            id=id,
                            members=members,
                            meta=meta,
                            roles=roles)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/preview/scim/v2/Groups', body=body)
        return Group.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a group.
        
        Deletes a group from the Databricks workspace.
        
        :param id: str
          Unique ID for a group in the Databricks workspace.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteGroupRequest(id=id)

        self._api.do('DELETE', f'/api/2.0/preview/scim/v2/Groups/{request.id}')

    def get(self, id: str, **kwargs) -> Group:
        """Get group details.
        
        Gets the information for a specific group in the Databricks workspace.
        
        :param id: str
          Unique ID for a group in the Databricks workspace.
        
        :returns: :class:`Group`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetGroupRequest(id=id)

        json = self._api.do('GET', f'/api/2.0/preview/scim/v2/Groups/{request.id}')
        return Group.from_dict(json)

    def list(self,
             *,
             attributes: Optional[str] = None,
             count: Optional[int] = None,
             excluded_attributes: Optional[str] = None,
             filter: Optional[str] = None,
             sort_by: Optional[str] = None,
             sort_order: Optional[ListSortOrder] = None,
             start_index: Optional[int] = None,
             **kwargs) -> Iterator[Group]:
        """List group details.
        
        Gets all details of the groups associated with the Databricks workspace.
        
        :param attributes: str (optional)
          Comma-separated list of attributes to return in response.
        :param count: int (optional)
          Desired number of results per page.
        :param excluded_attributes: str (optional)
          Comma-separated list of attributes to exclude in response.
        :param filter: str (optional)
          Query by which the results have to be filtered. Supported operators are equals(`eq`),
          contains(`co`), starts with(`sw`) and not equals(`ne`). Additionally, simple expressions can be
          formed using logical operators - `and` and `or`. The [SCIM RFC] has more details but we currently
          only support simple expressions.
          
          [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
        :param sort_by: str (optional)
          Attribute to sort the results.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: Iterator over :class:`Group`
        """
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

    def patch(self,
              id: str,
              *,
              operations: Optional[List[Patch]] = None,
              schema: Optional[List[PatchSchema]] = None,
              **kwargs):
        """Update group details.
        
        Partially updates the details of a group.
        
        :param id: str
          Unique ID for a group in the Databricks workspace.
        :param operations: List[:class:`Patch`] (optional)
        :param schema: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations, schema=schema)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.0/preview/scim/v2/Groups/{request.id}', body=body)

    def update(self,
               id: str,
               *,
               display_name: Optional[str] = None,
               entitlements: Optional[List[ComplexValue]] = None,
               external_id: Optional[str] = None,
               groups: Optional[List[ComplexValue]] = None,
               members: Optional[List[ComplexValue]] = None,
               meta: Optional[ResourceMeta] = None,
               roles: Optional[List[ComplexValue]] = None,
               **kwargs):
        """Replace a group.
        
        Updates the details of a group by replacing the entire group entity.
        
        :param id: str
          Databricks group ID
        :param display_name: str (optional)
          String that represents a human-readable group name
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param members: List[:class:`ComplexValue`] (optional)
        :param meta: :class:`ResourceMeta` (optional)
          Container for the group identifier. Workspace local versus account.
        :param roles: List[:class:`ComplexValue`] (optional)
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Group(display_name=display_name,
                            entitlements=entitlements,
                            external_id=external_id,
                            groups=groups,
                            id=id,
                            members=members,
                            meta=meta,
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
        objects.
        
        :param request_object_type: str
          <needs content>
        :param request_object_id: str
        
        :returns: :class:`ObjectPermissions`
        """
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
        
        Gets the permission levels that a user can have on an object.
        
        :param request_object_type: str
          <needs content>
        :param request_object_id: str
          <needs content>
        
        :returns: :class:`GetPermissionLevelsResponse`
        """
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
            access_control_list: Optional[List[AccessControlRequest]] = None,
            **kwargs):
        """Set permissions.
        
        Sets permissions on object. Objects can inherit permissions from their parent objects and root
        objects.
        
        :param request_object_type: str
          <needs content>
        :param request_object_id: str
        :param access_control_list: List[:class:`AccessControlRequest`] (optional)
        
        
        """
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
               access_control_list: Optional[List[AccessControlRequest]] = None,
               **kwargs):
        """Update permission.
        
        Updates the permissions on an object.
        
        :param request_object_type: str
          <needs content>
        :param request_object_id: str
        :param access_control_list: List[:class:`AccessControlRequest`] (optional)
        
        
        """
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
               *,
               active: Optional[bool] = None,
               application_id: Optional[str] = None,
               display_name: Optional[str] = None,
               entitlements: Optional[List[ComplexValue]] = None,
               external_id: Optional[str] = None,
               groups: Optional[List[ComplexValue]] = None,
               id: Optional[str] = None,
               roles: Optional[List[ComplexValue]] = None,
               **kwargs) -> ServicePrincipal:
        """Create a service principal.
        
        Creates a new service principal in the Databricks workspace.
        
        :param active: bool (optional)
          If this user is active
        :param application_id: str (optional)
          UUID relating to the service principal
        :param display_name: str (optional)
          String that represents a concatenation of given and family names.
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks service principal ID.
        :param roles: List[:class:`ComplexValue`] (optional)
        
        :returns: :class:`ServicePrincipal`
        """
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
        
        Delete a single service principal in the Databricks workspace.
        
        :param id: str
          Unique ID for a service principal in the Databricks workspace.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteServicePrincipalRequest(id=id)

        self._api.do('DELETE', f'/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}')

    def get(self, id: str, **kwargs) -> ServicePrincipal:
        """Get service principal details.
        
        Gets the details for a single service principal define in the Databricks workspace.
        
        :param id: str
          Unique ID for a service principal in the Databricks workspace.
        
        :returns: :class:`ServicePrincipal`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetServicePrincipalRequest(id=id)

        json = self._api.do('GET', f'/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}')
        return ServicePrincipal.from_dict(json)

    def list(self,
             *,
             attributes: Optional[str] = None,
             count: Optional[int] = None,
             excluded_attributes: Optional[str] = None,
             filter: Optional[str] = None,
             sort_by: Optional[str] = None,
             sort_order: Optional[ListSortOrder] = None,
             start_index: Optional[int] = None,
             **kwargs) -> Iterator[ServicePrincipal]:
        """List service principals.
        
        Gets the set of service principals associated with a Databricks workspace.
        
        :param attributes: str (optional)
          Comma-separated list of attributes to return in response.
        :param count: int (optional)
          Desired number of results per page.
        :param excluded_attributes: str (optional)
          Comma-separated list of attributes to exclude in response.
        :param filter: str (optional)
          Query by which the results have to be filtered. Supported operators are equals(`eq`),
          contains(`co`), starts with(`sw`) and not equals(`ne`). Additionally, simple expressions can be
          formed using logical operators - `and` and `or`. The [SCIM RFC] has more details but we currently
          only support simple expressions.
          
          [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
        :param sort_by: str (optional)
          Attribute to sort the results.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: Iterator over :class:`ServicePrincipal`
        """
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

    def patch(self,
              id: str,
              *,
              operations: Optional[List[Patch]] = None,
              schema: Optional[List[PatchSchema]] = None,
              **kwargs):
        """Update service principal details.
        
        Partially updates the details of a single service principal in the Databricks workspace.
        
        :param id: str
          Unique ID for a service principal in the Databricks workspace.
        :param operations: List[:class:`Patch`] (optional)
        :param schema: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations, schema=schema)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}', body=body)

    def update(self,
               id: str,
               *,
               active: Optional[bool] = None,
               application_id: Optional[str] = None,
               display_name: Optional[str] = None,
               entitlements: Optional[List[ComplexValue]] = None,
               external_id: Optional[str] = None,
               groups: Optional[List[ComplexValue]] = None,
               roles: Optional[List[ComplexValue]] = None,
               **kwargs):
        """Replace service principal.
        
        Updates the details of a single service principal.
        
        This action replaces the existing service principal with the same name.
        
        :param id: str
          Databricks service principal ID.
        :param active: bool (optional)
          If this user is active
        :param application_id: str (optional)
          UUID relating to the service principal
        :param display_name: str (optional)
          String that represents a concatenation of given and family names.
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
        
        
        """
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
    provider to your Databricks workspace. SCIM streamlines onboarding a new employee or team by using your
    identity provider to create users and groups in Databricks workspace and give them the proper level of
    access. When a user leaves your organization or no longer needs access to Databricks workspace, admins can
    terminate the user in your identity provider and that user’s account will also be removed from
    Databricks workspace. This ensures a consistent offboarding process and prevents unauthorized users from
    accessing sensitive data."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               active: Optional[bool] = None,
               display_name: Optional[str] = None,
               emails: Optional[List[ComplexValue]] = None,
               entitlements: Optional[List[ComplexValue]] = None,
               external_id: Optional[str] = None,
               groups: Optional[List[ComplexValue]] = None,
               id: Optional[str] = None,
               name: Optional[Name] = None,
               roles: Optional[List[ComplexValue]] = None,
               user_name: Optional[str] = None,
               **kwargs) -> User:
        """Create a new user.
        
        Creates a new user in the Databricks workspace. This new user will also be added to the Databricks
        account.
        
        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`.
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks user ID.
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
        :param user_name: str (optional)
          Email address of the Databricks user.
        
        :returns: :class:`User`
        """
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
        
        Deletes a user. Deleting a user from a Databricks workspace also removes objects associated with the
        user.
        
        :param id: str
          Unique ID for a user in the Databricks workspace.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteUserRequest(id=id)

        self._api.do('DELETE', f'/api/2.0/preview/scim/v2/Users/{request.id}')

    def get(self, id: str, **kwargs) -> User:
        """Get user details.
        
        Gets information for a specific user in Databricks workspace.
        
        :param id: str
          Unique ID for a user in the Databricks workspace.
        
        :returns: :class:`User`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetUserRequest(id=id)

        json = self._api.do('GET', f'/api/2.0/preview/scim/v2/Users/{request.id}')
        return User.from_dict(json)

    def list(self,
             *,
             attributes: Optional[str] = None,
             count: Optional[int] = None,
             excluded_attributes: Optional[str] = None,
             filter: Optional[str] = None,
             sort_by: Optional[str] = None,
             sort_order: Optional[ListSortOrder] = None,
             start_index: Optional[int] = None,
             **kwargs) -> Iterator[User]:
        """List users.
        
        Gets details for all the users associated with a Databricks workspace.
        
        :param attributes: str (optional)
          Comma-separated list of attributes to return in response.
        :param count: int (optional)
          Desired number of results per page.
        :param excluded_attributes: str (optional)
          Comma-separated list of attributes to exclude in response.
        :param filter: str (optional)
          Query by which the results have to be filtered. Supported operators are equals(`eq`),
          contains(`co`), starts with(`sw`) and not equals(`ne`). Additionally, simple expressions can be
          formed using logical operators - `and` and `or`. The [SCIM RFC] has more details but we currently
          only support simple expressions.
          
          [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
        :param sort_by: str (optional)
          Attribute to sort the results. Multi-part paths are supported. For example, `userName`,
          `name.givenName`, and `emails`.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: Iterator over :class:`User`
        """
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

    def patch(self,
              id: str,
              *,
              operations: Optional[List[Patch]] = None,
              schema: Optional[List[PatchSchema]] = None,
              **kwargs):
        """Update user details.
        
        Partially updates a user resource by applying the supplied operations on specific user attributes.
        
        :param id: str
          Unique ID for a user in the Databricks workspace.
        :param operations: List[:class:`Patch`] (optional)
        :param schema: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations, schema=schema)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.0/preview/scim/v2/Users/{request.id}', body=body)

    def update(self,
               id: str,
               *,
               active: Optional[bool] = None,
               display_name: Optional[str] = None,
               emails: Optional[List[ComplexValue]] = None,
               entitlements: Optional[List[ComplexValue]] = None,
               external_id: Optional[str] = None,
               groups: Optional[List[ComplexValue]] = None,
               name: Optional[Name] = None,
               roles: Optional[List[ComplexValue]] = None,
               user_name: Optional[str] = None,
               **kwargs):
        """Replace a user.
        
        Replaces a user's information with the data supplied in request.
        
        :param id: str
          Databricks user ID.
        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`.
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
        :param user_name: str (optional)
          Email address of the Databricks user.
        
        
        """
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
        principal.
        
        :param workspace_id: int
          The workspace ID.
        :param principal_id: int
          The ID of the user, service principal, or group.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteWorkspaceAssignmentRequest(principal_id=principal_id, workspace_id=workspace_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{request.workspace_id}/permissionassignments/principals/{request.principal_id}'
        )

    def get(self, workspace_id: int, **kwargs) -> WorkspacePermissions:
        """List workspace permissions.
        
        Get an array of workspace permissions for the specified account and workspace.
        
        :param workspace_id: int
          The workspace ID.
        
        :returns: :class:`WorkspacePermissions`
        """
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
        
        Get the permission assignments for the specified Databricks account and Databricks workspace.
        
        :param workspace_id: int
          The workspace ID for the account.
        
        :returns: Iterator over :class:`PermissionAssignment`
        """
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
        specified principal.
        
        :param permissions: List[:class:`WorkspacePermission`]
          Array of permissions assignments to update on the workspace.
        :param workspace_id: int
          The workspace ID.
        :param principal_id: int
          The ID of the user, service principal, or group.
        
        
        """
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

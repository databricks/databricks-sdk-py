# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated_dict, _repeated_enum

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AccessControlRequest:
    group_name: Optional[str] = None
    """name of the group"""

    permission_level: Optional[PermissionLevel] = None
    """Permission level"""

    service_principal_name: Optional[str] = None
    """Application ID of an active service principal. Setting this field requires the
    `servicePrincipal/user` role."""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the AccessControlRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AccessControlRequest:
        """Deserializes the AccessControlRequest from a dictionary."""
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', PermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class AccessControlResponse:
    all_permissions: Optional[List[Permission]] = None
    """All permissions."""

    display_name: Optional[str] = None
    """Display name of the user or service principal."""

    group_name: Optional[str] = None
    """name of the group"""

    service_principal_name: Optional[str] = None
    """Name of the service principal."""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the AccessControlResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.all_permissions: body['all_permissions'] = [v.as_dict() for v in self.all_permissions]
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AccessControlResponse:
        """Deserializes the AccessControlResponse from a dictionary."""
        return cls(all_permissions=_repeated_dict(d, 'all_permissions', Permission),
                   display_name=d.get('display_name', None),
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
        """Serializes the ComplexValue into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.display is not None: body['display'] = self.display
        if self.primary is not None: body['primary'] = self.primary
        if self.type is not None: body['type'] = self.type
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ComplexValue:
        """Deserializes the ComplexValue from a dictionary."""
        return cls(display=d.get('display', None),
                   primary=d.get('primary', None),
                   type=d.get('type', None),
                   value=d.get('value', None))


@dataclass
class GetAssignableRolesForResourceResponse:
    roles: Optional[List[Role]] = None

    def as_dict(self) -> dict:
        """Serializes the GetAssignableRolesForResourceResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.roles: body['roles'] = [v.as_dict() for v in self.roles]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetAssignableRolesForResourceResponse:
        """Deserializes the GetAssignableRolesForResourceResponse from a dictionary."""
        return cls(roles=_repeated_dict(d, 'roles', Role))


@dataclass
class GetPasswordPermissionLevelsResponse:
    permission_levels: Optional[List[PasswordPermissionsDescription]] = None
    """Specific permission levels"""

    def as_dict(self) -> dict:
        """Serializes the GetPasswordPermissionLevelsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetPasswordPermissionLevelsResponse:
        """Deserializes the GetPasswordPermissionLevelsResponse from a dictionary."""
        return cls(permission_levels=_repeated_dict(d, 'permission_levels', PasswordPermissionsDescription))


@dataclass
class GetPermissionLevelsResponse:
    permission_levels: Optional[List[PermissionsDescription]] = None
    """Specific permission levels"""

    def as_dict(self) -> dict:
        """Serializes the GetPermissionLevelsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetPermissionLevelsResponse:
        """Deserializes the GetPermissionLevelsResponse from a dictionary."""
        return cls(permission_levels=_repeated_dict(d, 'permission_levels', PermissionsDescription))


class GetSortOrder(Enum):

    ASCENDING = 'ascending'
    DESCENDING = 'descending'


@dataclass
class GrantRule:
    role: str
    """Role that is assigned to the list of principals."""

    principals: Optional[List[str]] = None
    """Principals this grant rule applies to."""

    def as_dict(self) -> dict:
        """Serializes the GrantRule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.principals: body['principals'] = [v for v in self.principals]
        if self.role is not None: body['role'] = self.role
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GrantRule:
        """Deserializes the GrantRule from a dictionary."""
        return cls(principals=d.get('principals', None), role=d.get('role', None))


@dataclass
class Group:
    display_name: Optional[str] = None
    """String that represents a human-readable group name"""

    entitlements: Optional[List[ComplexValue]] = None
    """Entitlements assigned to the group. See [assigning entitlements] for a full list of supported
    values.
    
    [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements"""

    external_id: Optional[str] = None

    groups: Optional[List[ComplexValue]] = None

    id: Optional[str] = None
    """Databricks group ID"""

    members: Optional[List[ComplexValue]] = None

    meta: Optional[ResourceMeta] = None
    """Container for the group identifier. Workspace local versus account."""

    roles: Optional[List[ComplexValue]] = None
    """Corresponds to AWS instance profile/arn role."""

    schemas: Optional[List[GroupSchema]] = None
    """The schema of the group."""

    def as_dict(self) -> dict:
        """Serializes the Group into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.display_name is not None: body['displayName'] = self.display_name
        if self.entitlements: body['entitlements'] = [v.as_dict() for v in self.entitlements]
        if self.external_id is not None: body['externalId'] = self.external_id
        if self.groups: body['groups'] = [v.as_dict() for v in self.groups]
        if self.id is not None: body['id'] = self.id
        if self.members: body['members'] = [v.as_dict() for v in self.members]
        if self.meta: body['meta'] = self.meta.as_dict()
        if self.roles: body['roles'] = [v.as_dict() for v in self.roles]
        if self.schemas: body['schemas'] = [v.value for v in self.schemas]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Group:
        """Deserializes the Group from a dictionary."""
        return cls(display_name=d.get('displayName', None),
                   entitlements=_repeated_dict(d, 'entitlements', ComplexValue),
                   external_id=d.get('externalId', None),
                   groups=_repeated_dict(d, 'groups', ComplexValue),
                   id=d.get('id', None),
                   members=_repeated_dict(d, 'members', ComplexValue),
                   meta=_from_dict(d, 'meta', ResourceMeta),
                   roles=_repeated_dict(d, 'roles', ComplexValue),
                   schemas=_repeated_enum(d, 'schemas', GroupSchema))


class GroupSchema(Enum):

    URN_IETF_PARAMS_SCIM_SCHEMAS_CORE_2_0_GROUP = 'urn:ietf:params:scim:schemas:core:2.0:Group'


@dataclass
class ListGroupsResponse:
    items_per_page: Optional[int] = None
    """Total results returned in the response."""

    resources: Optional[List[Group]] = None
    """User objects returned in the response."""

    schemas: Optional[List[ListResponseSchema]] = None
    """The schema of the service principal."""

    start_index: Optional[int] = None
    """Starting index of all the results that matched the request filters. First item is number 1."""

    total_results: Optional[int] = None
    """Total results that match the request filters."""

    def as_dict(self) -> dict:
        """Serializes the ListGroupsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.items_per_page is not None: body['itemsPerPage'] = self.items_per_page
        if self.resources: body['Resources'] = [v.as_dict() for v in self.resources]
        if self.schemas: body['schemas'] = [v.value for v in self.schemas]
        if self.start_index is not None: body['startIndex'] = self.start_index
        if self.total_results is not None: body['totalResults'] = self.total_results
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListGroupsResponse:
        """Deserializes the ListGroupsResponse from a dictionary."""
        return cls(items_per_page=d.get('itemsPerPage', None),
                   resources=_repeated_dict(d, 'Resources', Group),
                   schemas=_repeated_enum(d, 'schemas', ListResponseSchema),
                   start_index=d.get('startIndex', None),
                   total_results=d.get('totalResults', None))


class ListResponseSchema(Enum):

    URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_LIST_RESPONSE = 'urn:ietf:params:scim:api:messages:2.0:ListResponse'


@dataclass
class ListServicePrincipalResponse:
    items_per_page: Optional[int] = None
    """Total results returned in the response."""

    resources: Optional[List[ServicePrincipal]] = None
    """User objects returned in the response."""

    schemas: Optional[List[ListResponseSchema]] = None
    """The schema of the List response."""

    start_index: Optional[int] = None
    """Starting index of all the results that matched the request filters. First item is number 1."""

    total_results: Optional[int] = None
    """Total results that match the request filters."""

    def as_dict(self) -> dict:
        """Serializes the ListServicePrincipalResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.items_per_page is not None: body['itemsPerPage'] = self.items_per_page
        if self.resources: body['Resources'] = [v.as_dict() for v in self.resources]
        if self.schemas: body['schemas'] = [v.value for v in self.schemas]
        if self.start_index is not None: body['startIndex'] = self.start_index
        if self.total_results is not None: body['totalResults'] = self.total_results
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListServicePrincipalResponse:
        """Deserializes the ListServicePrincipalResponse from a dictionary."""
        return cls(items_per_page=d.get('itemsPerPage', None),
                   resources=_repeated_dict(d, 'Resources', ServicePrincipal),
                   schemas=_repeated_enum(d, 'schemas', ListResponseSchema),
                   start_index=d.get('startIndex', None),
                   total_results=d.get('totalResults', None))


class ListSortOrder(Enum):

    ASCENDING = 'ascending'
    DESCENDING = 'descending'


@dataclass
class ListUsersResponse:
    items_per_page: Optional[int] = None
    """Total results returned in the response."""

    resources: Optional[List[User]] = None
    """User objects returned in the response."""

    schemas: Optional[List[ListResponseSchema]] = None
    """The schema of the List response."""

    start_index: Optional[int] = None
    """Starting index of all the results that matched the request filters. First item is number 1."""

    total_results: Optional[int] = None
    """Total results that match the request filters."""

    def as_dict(self) -> dict:
        """Serializes the ListUsersResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.items_per_page is not None: body['itemsPerPage'] = self.items_per_page
        if self.resources: body['Resources'] = [v.as_dict() for v in self.resources]
        if self.schemas: body['schemas'] = [v.value for v in self.schemas]
        if self.start_index is not None: body['startIndex'] = self.start_index
        if self.total_results is not None: body['totalResults'] = self.total_results
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListUsersResponse:
        """Deserializes the ListUsersResponse from a dictionary."""
        return cls(items_per_page=d.get('itemsPerPage', None),
                   resources=_repeated_dict(d, 'Resources', User),
                   schemas=_repeated_enum(d, 'schemas', ListResponseSchema),
                   start_index=d.get('startIndex', None),
                   total_results=d.get('totalResults', None))


@dataclass
class Name:
    family_name: Optional[str] = None
    """Family name of the Databricks user."""

    given_name: Optional[str] = None
    """Given name of the Databricks user."""

    def as_dict(self) -> dict:
        """Serializes the Name into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.family_name is not None: body['familyName'] = self.family_name
        if self.given_name is not None: body['givenName'] = self.given_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Name:
        """Deserializes the Name from a dictionary."""
        return cls(family_name=d.get('familyName', None), given_name=d.get('givenName', None))


@dataclass
class ObjectPermissions:
    access_control_list: Optional[List[AccessControlResponse]] = None

    object_id: Optional[str] = None

    object_type: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the ObjectPermissions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None: body['object_id'] = self.object_id
        if self.object_type is not None: body['object_type'] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ObjectPermissions:
        """Deserializes the ObjectPermissions from a dictionary."""
        return cls(access_control_list=_repeated_dict(d, 'access_control_list', AccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class PartialUpdate:
    id: Optional[str] = None
    """Unique ID for a user in the Databricks workspace."""

    operations: Optional[List[Patch]] = None

    schemas: Optional[List[PatchSchema]] = None
    """The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"]."""

    def as_dict(self) -> dict:
        """Serializes the PartialUpdate into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.id is not None: body['id'] = self.id
        if self.operations: body['Operations'] = [v.as_dict() for v in self.operations]
        if self.schemas: body['schemas'] = [v.value for v in self.schemas]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PartialUpdate:
        """Deserializes the PartialUpdate from a dictionary."""
        return cls(id=d.get('id', None),
                   operations=_repeated_dict(d, 'Operations', Patch),
                   schemas=_repeated_enum(d, 'schemas', PatchSchema))


@dataclass
class PasswordAccessControlRequest:
    group_name: Optional[str] = None
    """name of the group"""

    permission_level: Optional[PasswordPermissionLevel] = None
    """Permission level"""

    service_principal_name: Optional[str] = None
    """Application ID of an active service principal. Setting this field requires the
    `servicePrincipal/user` role."""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the PasswordAccessControlRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PasswordAccessControlRequest:
        """Deserializes the PasswordAccessControlRequest from a dictionary."""
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', PasswordPermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class PasswordAccessControlResponse:
    all_permissions: Optional[List[PasswordPermission]] = None
    """All permissions."""

    display_name: Optional[str] = None
    """Display name of the user or service principal."""

    group_name: Optional[str] = None
    """name of the group"""

    service_principal_name: Optional[str] = None
    """Name of the service principal."""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the PasswordAccessControlResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.all_permissions: body['all_permissions'] = [v.as_dict() for v in self.all_permissions]
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PasswordAccessControlResponse:
        """Deserializes the PasswordAccessControlResponse from a dictionary."""
        return cls(all_permissions=_repeated_dict(d, 'all_permissions', PasswordPermission),
                   display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class PasswordPermission:
    inherited: Optional[bool] = None

    inherited_from_object: Optional[List[str]] = None

    permission_level: Optional[PasswordPermissionLevel] = None
    """Permission level"""

    def as_dict(self) -> dict:
        """Serializes the PasswordPermission into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PasswordPermission:
        """Deserializes the PasswordPermission from a dictionary."""
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', PasswordPermissionLevel))


class PasswordPermissionLevel(Enum):
    """Permission level"""

    CAN_USE = 'CAN_USE'


@dataclass
class PasswordPermissions:
    access_control_list: Optional[List[PasswordAccessControlResponse]] = None

    object_id: Optional[str] = None

    object_type: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the PasswordPermissions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None: body['object_id'] = self.object_id
        if self.object_type is not None: body['object_type'] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PasswordPermissions:
        """Deserializes the PasswordPermissions from a dictionary."""
        return cls(access_control_list=_repeated_dict(d, 'access_control_list',
                                                      PasswordAccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class PasswordPermissionsDescription:
    description: Optional[str] = None

    permission_level: Optional[PasswordPermissionLevel] = None
    """Permission level"""

    def as_dict(self) -> dict:
        """Serializes the PasswordPermissionsDescription into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PasswordPermissionsDescription:
        """Deserializes the PasswordPermissionsDescription from a dictionary."""
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', PasswordPermissionLevel))


@dataclass
class PasswordPermissionsRequest:
    access_control_list: Optional[List[PasswordAccessControlRequest]] = None

    def as_dict(self) -> dict:
        """Serializes the PasswordPermissionsRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PasswordPermissionsRequest:
        """Deserializes the PasswordPermissionsRequest from a dictionary."""
        return cls(access_control_list=_repeated_dict(d, 'access_control_list', PasswordAccessControlRequest))


@dataclass
class Patch:
    op: Optional[PatchOp] = None
    """Type of patch operation."""

    path: Optional[str] = None
    """Selection of patch operation"""

    value: Optional[Any] = None
    """Value to modify"""

    def as_dict(self) -> dict:
        """Serializes the Patch into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.op is not None: body['op'] = self.op.value
        if self.path is not None: body['path'] = self.path
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Patch:
        """Deserializes the Patch from a dictionary."""
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

    inherited_from_object: Optional[List[str]] = None

    permission_level: Optional[PermissionLevel] = None
    """Permission level"""

    def as_dict(self) -> dict:
        """Serializes the Permission into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Permission:
        """Deserializes the Permission from a dictionary."""
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', PermissionLevel))


@dataclass
class PermissionAssignment:
    error: Optional[str] = None
    """Error response associated with a workspace permission assignment, if any."""

    permissions: Optional[List[WorkspacePermission]] = None
    """The permissions level of the principal."""

    principal: Optional[PrincipalOutput] = None
    """Information about the principal assigned to the workspace."""

    def as_dict(self) -> dict:
        """Serializes the PermissionAssignment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.error is not None: body['error'] = self.error
        if self.permissions: body['permissions'] = [v.value for v in self.permissions]
        if self.principal: body['principal'] = self.principal.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PermissionAssignment:
        """Deserializes the PermissionAssignment from a dictionary."""
        return cls(error=d.get('error', None),
                   permissions=_repeated_enum(d, 'permissions', WorkspacePermission),
                   principal=_from_dict(d, 'principal', PrincipalOutput))


@dataclass
class PermissionAssignments:
    permission_assignments: Optional[List[PermissionAssignment]] = None
    """Array of permissions assignments defined for a workspace."""

    def as_dict(self) -> dict:
        """Serializes the PermissionAssignments into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission_assignments:
            body['permission_assignments'] = [v.as_dict() for v in self.permission_assignments]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PermissionAssignments:
        """Deserializes the PermissionAssignments from a dictionary."""
        return cls(permission_assignments=_repeated_dict(d, 'permission_assignments', PermissionAssignment))


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
    """The results of a permissions query."""

    permission_level: Optional[WorkspacePermission] = None

    def as_dict(self) -> dict:
        """Serializes the PermissionOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PermissionOutput:
        """Deserializes the PermissionOutput from a dictionary."""
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', WorkspacePermission))


@dataclass
class PermissionsDescription:
    description: Optional[str] = None

    permission_level: Optional[PermissionLevel] = None
    """Permission level"""

    def as_dict(self) -> dict:
        """Serializes the PermissionsDescription into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PermissionsDescription:
        """Deserializes the PermissionsDescription from a dictionary."""
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', PermissionLevel))


@dataclass
class PermissionsRequest:
    access_control_list: Optional[List[AccessControlRequest]] = None

    request_object_id: Optional[str] = None
    """The id of the request object."""

    request_object_type: Optional[str] = None
    """The type of the request object. Can be one of the following: authorization, clusters,
    cluster-policies, directories, experiments, files, instance-pools, jobs, notebooks, pipelines,
    registered-models, repos, serving-endpoints, or sql-warehouses."""

    def as_dict(self) -> dict:
        """Serializes the PermissionsRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.request_object_id is not None: body['request_object_id'] = self.request_object_id
        if self.request_object_type is not None: body['request_object_type'] = self.request_object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PermissionsRequest:
        """Deserializes the PermissionsRequest from a dictionary."""
        return cls(access_control_list=_repeated_dict(d, 'access_control_list', AccessControlRequest),
                   request_object_id=d.get('request_object_id', None),
                   request_object_type=d.get('request_object_type', None))


@dataclass
class PrincipalOutput:
    display_name: Optional[str] = None
    """The display name of the principal."""

    group_name: Optional[str] = None
    """The group name of the groupl. Present only if the principal is a group."""

    principal_id: Optional[int] = None
    """The unique, opaque id of the principal."""

    service_principal_name: Optional[str] = None
    """The name of the service principal. Present only if the principal is a service principal."""

    user_name: Optional[str] = None
    """The username of the user. Present only if the principal is a user."""

    def as_dict(self) -> dict:
        """Serializes the PrincipalOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.principal_id is not None: body['principal_id'] = self.principal_id
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PrincipalOutput:
        """Deserializes the PrincipalOutput from a dictionary."""
        return cls(display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   principal_id=d.get('principal_id', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class ResourceMeta:
    resource_type: Optional[str] = None
    """Identifier for group type. Can be local workspace group (`WorkspaceGroup`) or account group
    (`Group`)."""

    def as_dict(self) -> dict:
        """Serializes the ResourceMeta into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.resource_type is not None: body['resourceType'] = self.resource_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ResourceMeta:
        """Deserializes the ResourceMeta from a dictionary."""
        return cls(resource_type=d.get('resourceType', None))


@dataclass
class Role:
    name: str
    """Role to assign to a principal or a list of principals on a resource."""

    def as_dict(self) -> dict:
        """Serializes the Role into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Role:
        """Deserializes the Role from a dictionary."""
        return cls(name=d.get('name', None))


@dataclass
class RuleSetResponse:
    etag: Optional[str] = None
    """Identifies the version of the rule set returned."""

    grant_rules: Optional[List[GrantRule]] = None

    name: Optional[str] = None
    """Name of the rule set."""

    def as_dict(self) -> dict:
        """Serializes the RuleSetResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        if self.grant_rules: body['grant_rules'] = [v.as_dict() for v in self.grant_rules]
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> RuleSetResponse:
        """Deserializes the RuleSetResponse from a dictionary."""
        return cls(etag=d.get('etag', None),
                   grant_rules=_repeated_dict(d, 'grant_rules', GrantRule),
                   name=d.get('name', None))


@dataclass
class RuleSetUpdateRequest:
    name: str
    """Name of the rule set."""

    etag: str
    """The expected etag of the rule set to update. The update will fail if the value does not match
    the value that is stored in account access control service."""

    grant_rules: Optional[List[GrantRule]] = None

    def as_dict(self) -> dict:
        """Serializes the RuleSetUpdateRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        if self.grant_rules: body['grant_rules'] = [v.as_dict() for v in self.grant_rules]
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> RuleSetUpdateRequest:
        """Deserializes the RuleSetUpdateRequest from a dictionary."""
        return cls(etag=d.get('etag', None),
                   grant_rules=_repeated_dict(d, 'grant_rules', GrantRule),
                   name=d.get('name', None))


@dataclass
class ServicePrincipal:
    active: Optional[bool] = None
    """If this user is active"""

    application_id: Optional[str] = None
    """UUID relating to the service principal"""

    display_name: Optional[str] = None
    """String that represents a concatenation of given and family names."""

    entitlements: Optional[List[ComplexValue]] = None
    """Entitlements assigned to the service principal. See [assigning entitlements] for a full list of
    supported values.
    
    [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements"""

    external_id: Optional[str] = None

    groups: Optional[List[ComplexValue]] = None

    id: Optional[str] = None
    """Databricks service principal ID."""

    roles: Optional[List[ComplexValue]] = None
    """Corresponds to AWS instance profile/arn role."""

    schemas: Optional[List[ServicePrincipalSchema]] = None
    """The schema of the List response."""

    def as_dict(self) -> dict:
        """Serializes the ServicePrincipal into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.active is not None: body['active'] = self.active
        if self.application_id is not None: body['applicationId'] = self.application_id
        if self.display_name is not None: body['displayName'] = self.display_name
        if self.entitlements: body['entitlements'] = [v.as_dict() for v in self.entitlements]
        if self.external_id is not None: body['externalId'] = self.external_id
        if self.groups: body['groups'] = [v.as_dict() for v in self.groups]
        if self.id is not None: body['id'] = self.id
        if self.roles: body['roles'] = [v.as_dict() for v in self.roles]
        if self.schemas: body['schemas'] = [v.value for v in self.schemas]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServicePrincipal:
        """Deserializes the ServicePrincipal from a dictionary."""
        return cls(active=d.get('active', None),
                   application_id=d.get('applicationId', None),
                   display_name=d.get('displayName', None),
                   entitlements=_repeated_dict(d, 'entitlements', ComplexValue),
                   external_id=d.get('externalId', None),
                   groups=_repeated_dict(d, 'groups', ComplexValue),
                   id=d.get('id', None),
                   roles=_repeated_dict(d, 'roles', ComplexValue),
                   schemas=_repeated_enum(d, 'schemas', ServicePrincipalSchema))


class ServicePrincipalSchema(Enum):

    URN_IETF_PARAMS_SCIM_SCHEMAS_CORE_2_0_SERVICE_PRINCIPAL = 'urn:ietf:params:scim:schemas:core:2.0:ServicePrincipal'


@dataclass
class UpdateRuleSetRequest:
    name: str
    """Name of the rule set."""

    rule_set: RuleSetUpdateRequest

    def as_dict(self) -> dict:
        """Serializes the UpdateRuleSetRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.rule_set: body['rule_set'] = self.rule_set.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateRuleSetRequest:
        """Deserializes the UpdateRuleSetRequest from a dictionary."""
        return cls(name=d.get('name', None), rule_set=_from_dict(d, 'rule_set', RuleSetUpdateRequest))


@dataclass
class UpdateWorkspaceAssignments:
    permissions: List[WorkspacePermission]
    """Array of permissions assignments to update on the workspace."""

    principal_id: Optional[int] = None
    """The ID of the user, service principal, or group."""

    workspace_id: Optional[int] = None
    """The workspace ID."""

    def as_dict(self) -> dict:
        """Serializes the UpdateWorkspaceAssignments into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permissions: body['permissions'] = [v.value for v in self.permissions]
        if self.principal_id is not None: body['principal_id'] = self.principal_id
        if self.workspace_id is not None: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateWorkspaceAssignments:
        """Deserializes the UpdateWorkspaceAssignments from a dictionary."""
        return cls(permissions=_repeated_enum(d, 'permissions', WorkspacePermission),
                   principal_id=d.get('principal_id', None),
                   workspace_id=d.get('workspace_id', None))


@dataclass
class User:
    active: Optional[bool] = None
    """If this user is active"""

    display_name: Optional[str] = None
    """String that represents a concatenation of given and family names. For example `John Smith`. This
    field cannot be updated through the Workspace SCIM APIs when [identity federation is enabled].
    Use Account SCIM APIs to update `displayName`.
    
    [identity federation is enabled]: https://docs.databricks.com/administration-guide/users-groups/best-practices.html#enable-identity-federation"""

    emails: Optional[List[ComplexValue]] = None
    """All the emails associated with the Databricks user."""

    entitlements: Optional[List[ComplexValue]] = None
    """Entitlements assigned to the user. See [assigning entitlements] for a full list of supported
    values.
    
    [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements"""

    external_id: Optional[str] = None
    """External ID is not currently supported. It is reserved for future use."""

    groups: Optional[List[ComplexValue]] = None

    id: Optional[str] = None
    """Databricks user ID. This is automatically set by Databricks. Any value provided by the client
    will be ignored."""

    name: Optional[Name] = None

    roles: Optional[List[ComplexValue]] = None
    """Corresponds to AWS instance profile/arn role."""

    schemas: Optional[List[UserSchema]] = None
    """The schema of the user."""

    user_name: Optional[str] = None
    """Email address of the Databricks user."""

    def as_dict(self) -> dict:
        """Serializes the User into a dictionary suitable for use as a JSON request body."""
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
        if self.schemas: body['schemas'] = [v.value for v in self.schemas]
        if self.user_name is not None: body['userName'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> User:
        """Deserializes the User from a dictionary."""
        return cls(active=d.get('active', None),
                   display_name=d.get('displayName', None),
                   emails=_repeated_dict(d, 'emails', ComplexValue),
                   entitlements=_repeated_dict(d, 'entitlements', ComplexValue),
                   external_id=d.get('externalId', None),
                   groups=_repeated_dict(d, 'groups', ComplexValue),
                   id=d.get('id', None),
                   name=_from_dict(d, 'name', Name),
                   roles=_repeated_dict(d, 'roles', ComplexValue),
                   schemas=_repeated_enum(d, 'schemas', UserSchema),
                   user_name=d.get('userName', None))


class UserSchema(Enum):

    URN_IETF_PARAMS_SCIM_SCHEMAS_CORE_2_0_USER = 'urn:ietf:params:scim:schemas:core:2.0:User'


class WorkspacePermission(Enum):

    ADMIN = 'ADMIN'
    UNKNOWN = 'UNKNOWN'
    USER = 'USER'


@dataclass
class WorkspacePermissions:
    permissions: Optional[List[PermissionOutput]] = None
    """Array of permissions defined for a workspace."""

    def as_dict(self) -> dict:
        """Serializes the WorkspacePermissions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permissions: body['permissions'] = [v.as_dict() for v in self.permissions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> WorkspacePermissions:
        """Deserializes the WorkspacePermissions from a dictionary."""
        return cls(permissions=_repeated_dict(d, 'permissions', PermissionOutput))


class AccountAccessControlAPI:
    """These APIs manage access rules on resources in an account. Currently, only grant rules are supported. A
    grant rule specifies a role assigned to a set of principals. A list of rules attached to a resource is
    called a rule set."""

    def __init__(self, api_client):
        self._api = api_client

    def get_assignable_roles_for_resource(self, resource: str) -> GetAssignableRolesForResourceResponse:
        """Get assignable roles for a resource.
        
        Gets all the roles that can be granted on an account level resource. A role is grantable if the rule
        set on the resource can contain an access rule of the role.
        
        :param resource: str
          The resource name for which assignable roles will be listed.
        
        :returns: :class:`GetAssignableRolesForResourceResponse`
        """

        query = {}
        if resource is not None: query['resource'] = resource
        headers = {'Accept': 'application/json', }
        res = self._api.do(
            'GET',
            f'/api/2.0/preview/accounts/{self._api.account_id}/access-control/assignable-roles',
            query=query,
            headers=headers)
        return GetAssignableRolesForResourceResponse.from_dict(res)

    def get_rule_set(self, name: str, etag: str) -> RuleSetResponse:
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

        query = {}
        if etag is not None: query['etag'] = etag
        if name is not None: query['name'] = name
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/preview/accounts/{self._api.account_id}/access-control/rule-sets',
                           query=query,
                           headers=headers)
        return RuleSetResponse.from_dict(res)

    def update_rule_set(self, name: str, rule_set: RuleSetUpdateRequest) -> RuleSetResponse:
        """Update a rule set.
        
        Replace the rules of a rule set. First, use get to read the current version of the rule set before
        modifying it. This pattern helps prevent conflicts between concurrent updates.
        
        :param name: str
          Name of the rule set.
        :param rule_set: :class:`RuleSetUpdateRequest`
        
        :returns: :class:`RuleSetResponse`
        """
        body = {}
        if name is not None: body['name'] = name
        if rule_set is not None: body['rule_set'] = rule_set.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PUT',
                           f'/api/2.0/preview/accounts/{self._api.account_id}/access-control/rule-sets',
                           body=body,
                           headers=headers)
        return RuleSetResponse.from_dict(res)


class AccountAccessControlProxyAPI:
    """These APIs manage access rules on resources in an account. Currently, only grant rules are supported. A
    grant rule specifies a role assigned to a set of principals. A list of rules attached to a resource is
    called a rule set. A workspace must belong to an account for these APIs to work."""

    def __init__(self, api_client):
        self._api = api_client

    def get_assignable_roles_for_resource(self, resource: str) -> GetAssignableRolesForResourceResponse:
        """Get assignable roles for a resource.
        
        Gets all the roles that can be granted on an account-level resource. A role is grantable if the rule
        set on the resource can contain an access rule of the role.
        
        :param resource: str
          The resource name for which assignable roles will be listed.
        
        :returns: :class:`GetAssignableRolesForResourceResponse`
        """

        query = {}
        if resource is not None: query['resource'] = resource
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           '/api/2.0/preview/accounts/access-control/assignable-roles',
                           query=query,
                           headers=headers)
        return GetAssignableRolesForResourceResponse.from_dict(res)

    def get_rule_set(self, name: str, etag: str) -> RuleSetResponse:
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

        query = {}
        if etag is not None: query['etag'] = etag
        if name is not None: query['name'] = name
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           '/api/2.0/preview/accounts/access-control/rule-sets',
                           query=query,
                           headers=headers)
        return RuleSetResponse.from_dict(res)

    def update_rule_set(self, name: str, rule_set: RuleSetUpdateRequest) -> RuleSetResponse:
        """Update a rule set.
        
        Replace the rules of a rule set. First, use a GET rule set request to read the current version of the
        rule set before modifying it. This pattern helps prevent conflicts between concurrent updates.
        
        :param name: str
          Name of the rule set.
        :param rule_set: :class:`RuleSetUpdateRequest`
        
        :returns: :class:`RuleSetResponse`
        """
        body = {}
        if name is not None: body['name'] = name
        if rule_set is not None: body['rule_set'] = rule_set.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PUT',
                           '/api/2.0/preview/accounts/access-control/rule-sets',
                           body=body,
                           headers=headers)
        return RuleSetResponse.from_dict(res)


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
               schemas: Optional[List[GroupSchema]] = None) -> Group:
        """Create a new group.
        
        Creates a group in the Databricks account with a unique name, using the supplied group details.
        
        :param display_name: str (optional)
          String that represents a human-readable group name
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the group. See [assigning entitlements] for a full list of supported
          values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks group ID
        :param members: List[:class:`ComplexValue`] (optional)
        :param meta: :class:`ResourceMeta` (optional)
          Container for the group identifier. Workspace local versus account.
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`GroupSchema`] (optional)
          The schema of the group.
        
        :returns: :class:`Group`
        """
        body = {}
        if display_name is not None: body['displayName'] = display_name
        if entitlements is not None: body['entitlements'] = [v.as_dict() for v in entitlements]
        if external_id is not None: body['externalId'] = external_id
        if groups is not None: body['groups'] = [v.as_dict() for v in groups]
        if id is not None: body['id'] = id
        if members is not None: body['members'] = [v.as_dict() for v in members]
        if meta is not None: body['meta'] = meta.as_dict()
        if roles is not None: body['roles'] = [v.as_dict() for v in roles]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups',
                           body=body,
                           headers=headers)
        return Group.from_dict(res)

    def delete(self, id: str):
        """Delete a group.
        
        Deletes a group from the Databricks account.
        
        :param id: str
          Unique ID for a group in the Databricks account.
        
        
        """

        headers = {}
        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups/{id}',
                     headers=headers)

    def get(self, id: str) -> Group:
        """Get group details.
        
        Gets the information for a specific group in the Databricks account.
        
        :param id: str
          Unique ID for a group in the Databricks account.
        
        :returns: :class:`Group`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups/{id}',
                           headers=headers)
        return Group.from_dict(res)

    def list(self,
             *,
             attributes: Optional[str] = None,
             count: Optional[int] = None,
             excluded_attributes: Optional[str] = None,
             filter: Optional[str] = None,
             sort_by: Optional[str] = None,
             sort_order: Optional[ListSortOrder] = None,
             start_index: Optional[int] = None) -> Iterator[Group]:
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

        query = {}
        if attributes is not None: query['attributes'] = attributes
        if count is not None: query['count'] = count
        if excluded_attributes is not None: query['excludedAttributes'] = excluded_attributes
        if filter is not None: query['filter'] = filter
        if sort_by is not None: query['sortBy'] = sort_by
        if sort_order is not None: query['sortOrder'] = sort_order.value
        if start_index is not None: query['startIndex'] = start_index
        headers = {'Accept': 'application/json', }

        # deduplicate items that may have been added during iteration
        seen = set()
        query['startIndex'] = 1
        if "count" not in query: query['count'] = 100
        while True:
            json = self._api.do('GET',
                                f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups',
                                query=query,
                                headers=headers)
            if 'Resources' not in json or not json['Resources']:
                return
            for v in json['Resources']:
                i = v['id']
                if i in seen:
                    continue
                seen.add(i)
                yield Group.from_dict(v)
            query['startIndex'] += len(json['Resources'])

    def patch(self,
              id: str,
              *,
              operations: Optional[List[Patch]] = None,
              schemas: Optional[List[PatchSchema]] = None):
        """Update group details.
        
        Partially updates the details of a group.
        
        :param id: str
          Unique ID for a group in the Databricks account.
        :param operations: List[:class:`Patch`] (optional)
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        """
        body = {}
        if operations is not None: body['Operations'] = [v.as_dict() for v in operations]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups/{id}',
                     body=body,
                     headers=headers)

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
               schemas: Optional[List[GroupSchema]] = None):
        """Replace a group.
        
        Updates the details of a group by replacing the entire group entity.
        
        :param id: str
          Databricks group ID
        :param display_name: str (optional)
          String that represents a human-readable group name
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the group. See [assigning entitlements] for a full list of supported
          values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param members: List[:class:`ComplexValue`] (optional)
        :param meta: :class:`ResourceMeta` (optional)
          Container for the group identifier. Workspace local versus account.
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`GroupSchema`] (optional)
          The schema of the group.
        
        
        """
        body = {}
        if display_name is not None: body['displayName'] = display_name
        if entitlements is not None: body['entitlements'] = [v.as_dict() for v in entitlements]
        if external_id is not None: body['externalId'] = external_id
        if groups is not None: body['groups'] = [v.as_dict() for v in groups]
        if members is not None: body['members'] = [v.as_dict() for v in members]
        if meta is not None: body['meta'] = meta.as_dict()
        if roles is not None: body['roles'] = [v.as_dict() for v in roles]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PUT',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Groups/{id}',
                     body=body,
                     headers=headers)


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
               schemas: Optional[List[ServicePrincipalSchema]] = None) -> ServicePrincipal:
        """Create a service principal.
        
        Creates a new service principal in the Databricks account.
        
        :param active: bool (optional)
          If this user is active
        :param application_id: str (optional)
          UUID relating to the service principal
        :param display_name: str (optional)
          String that represents a concatenation of given and family names.
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the service principal. See [assigning entitlements] for a full list of
          supported values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks service principal ID.
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`ServicePrincipalSchema`] (optional)
          The schema of the List response.
        
        :returns: :class:`ServicePrincipal`
        """
        body = {}
        if active is not None: body['active'] = active
        if application_id is not None: body['applicationId'] = application_id
        if display_name is not None: body['displayName'] = display_name
        if entitlements is not None: body['entitlements'] = [v.as_dict() for v in entitlements]
        if external_id is not None: body['externalId'] = external_id
        if groups is not None: body['groups'] = [v.as_dict() for v in groups]
        if id is not None: body['id'] = id
        if roles is not None: body['roles'] = [v.as_dict() for v in roles]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals',
                           body=body,
                           headers=headers)
        return ServicePrincipal.from_dict(res)

    def delete(self, id: str):
        """Delete a service principal.
        
        Delete a single service principal in the Databricks account.
        
        :param id: str
          Unique ID for a service principal in the Databricks account.
        
        
        """

        headers = {}
        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals/{id}',
                     headers=headers)

    def get(self, id: str) -> ServicePrincipal:
        """Get service principal details.
        
        Gets the details for a single service principal define in the Databricks account.
        
        :param id: str
          Unique ID for a service principal in the Databricks account.
        
        :returns: :class:`ServicePrincipal`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals/{id}',
                           headers=headers)
        return ServicePrincipal.from_dict(res)

    def list(self,
             *,
             attributes: Optional[str] = None,
             count: Optional[int] = None,
             excluded_attributes: Optional[str] = None,
             filter: Optional[str] = None,
             sort_by: Optional[str] = None,
             sort_order: Optional[ListSortOrder] = None,
             start_index: Optional[int] = None) -> Iterator[ServicePrincipal]:
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

        query = {}
        if attributes is not None: query['attributes'] = attributes
        if count is not None: query['count'] = count
        if excluded_attributes is not None: query['excludedAttributes'] = excluded_attributes
        if filter is not None: query['filter'] = filter
        if sort_by is not None: query['sortBy'] = sort_by
        if sort_order is not None: query['sortOrder'] = sort_order.value
        if start_index is not None: query['startIndex'] = start_index
        headers = {'Accept': 'application/json', }

        # deduplicate items that may have been added during iteration
        seen = set()
        query['startIndex'] = 1
        if "count" not in query: query['count'] = 100
        while True:
            json = self._api.do('GET',
                                f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals',
                                query=query,
                                headers=headers)
            if 'Resources' not in json or not json['Resources']:
                return
            for v in json['Resources']:
                i = v['id']
                if i in seen:
                    continue
                seen.add(i)
                yield ServicePrincipal.from_dict(v)
            query['startIndex'] += len(json['Resources'])

    def patch(self,
              id: str,
              *,
              operations: Optional[List[Patch]] = None,
              schemas: Optional[List[PatchSchema]] = None):
        """Update service principal details.
        
        Partially updates the details of a single service principal in the Databricks account.
        
        :param id: str
          Unique ID for a service principal in the Databricks account.
        :param operations: List[:class:`Patch`] (optional)
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        """
        body = {}
        if operations is not None: body['Operations'] = [v.as_dict() for v in operations]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals/{id}',
                     body=body,
                     headers=headers)

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
               schemas: Optional[List[ServicePrincipalSchema]] = None):
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
          Entitlements assigned to the service principal. See [assigning entitlements] for a full list of
          supported values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`ServicePrincipalSchema`] (optional)
          The schema of the List response.
        
        
        """
        body = {}
        if active is not None: body['active'] = active
        if application_id is not None: body['applicationId'] = application_id
        if display_name is not None: body['displayName'] = display_name
        if entitlements is not None: body['entitlements'] = [v.as_dict() for v in entitlements]
        if external_id is not None: body['externalId'] = external_id
        if groups is not None: body['groups'] = [v.as_dict() for v in groups]
        if roles is not None: body['roles'] = [v.as_dict() for v in roles]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PUT',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/ServicePrincipals/{id}',
                     body=body,
                     headers=headers)


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
               schemas: Optional[List[UserSchema]] = None,
               user_name: Optional[str] = None) -> User:
        """Create a new user.
        
        Creates a new user in the Databricks account. This new user will also be added to the Databricks
        account.
        
        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`. This
          field cannot be updated through the Workspace SCIM APIs when [identity federation is enabled]. Use
          Account SCIM APIs to update `displayName`.
          
          [identity federation is enabled]: https://docs.databricks.com/administration-guide/users-groups/best-practices.html#enable-identity-federation
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the user. See [assigning entitlements] for a full list of supported values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
          External ID is not currently supported. It is reserved for future use.
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks user ID. This is automatically set by Databricks. Any value provided by the client will
          be ignored.
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`UserSchema`] (optional)
          The schema of the user.
        :param user_name: str (optional)
          Email address of the Databricks user.
        
        :returns: :class:`User`
        """
        body = {}
        if active is not None: body['active'] = active
        if display_name is not None: body['displayName'] = display_name
        if emails is not None: body['emails'] = [v.as_dict() for v in emails]
        if entitlements is not None: body['entitlements'] = [v.as_dict() for v in entitlements]
        if external_id is not None: body['externalId'] = external_id
        if groups is not None: body['groups'] = [v.as_dict() for v in groups]
        if id is not None: body['id'] = id
        if name is not None: body['name'] = name.as_dict()
        if roles is not None: body['roles'] = [v.as_dict() for v in roles]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        if user_name is not None: body['userName'] = user_name
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users',
                           body=body,
                           headers=headers)
        return User.from_dict(res)

    def delete(self, id: str):
        """Delete a user.
        
        Deletes a user. Deleting a user from a Databricks account also removes objects associated with the
        user.
        
        :param id: str
          Unique ID for a user in the Databricks account.
        
        
        """

        headers = {}
        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users/{id}',
                     headers=headers)

    def get(self,
            id: str,
            *,
            attributes: Optional[str] = None,
            count: Optional[int] = None,
            excluded_attributes: Optional[str] = None,
            filter: Optional[str] = None,
            sort_by: Optional[str] = None,
            sort_order: Optional[GetSortOrder] = None,
            start_index: Optional[int] = None) -> User:
        """Get user details.
        
        Gets information for a specific user in Databricks account.
        
        :param id: str
          Unique ID for a user in the Databricks account.
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
        :param sort_order: :class:`GetSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: :class:`User`
        """

        query = {}
        if attributes is not None: query['attributes'] = attributes
        if count is not None: query['count'] = count
        if excluded_attributes is not None: query['excludedAttributes'] = excluded_attributes
        if filter is not None: query['filter'] = filter
        if sort_by is not None: query['sortBy'] = sort_by
        if sort_order is not None: query['sortOrder'] = sort_order.value
        if start_index is not None: query['startIndex'] = start_index
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users/{id}',
                           query=query,
                           headers=headers)
        return User.from_dict(res)

    def list(self,
             *,
             attributes: Optional[str] = None,
             count: Optional[int] = None,
             excluded_attributes: Optional[str] = None,
             filter: Optional[str] = None,
             sort_by: Optional[str] = None,
             sort_order: Optional[ListSortOrder] = None,
             start_index: Optional[int] = None) -> Iterator[User]:
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

        query = {}
        if attributes is not None: query['attributes'] = attributes
        if count is not None: query['count'] = count
        if excluded_attributes is not None: query['excludedAttributes'] = excluded_attributes
        if filter is not None: query['filter'] = filter
        if sort_by is not None: query['sortBy'] = sort_by
        if sort_order is not None: query['sortOrder'] = sort_order.value
        if start_index is not None: query['startIndex'] = start_index
        headers = {'Accept': 'application/json', }

        # deduplicate items that may have been added during iteration
        seen = set()
        query['startIndex'] = 1
        if "count" not in query: query['count'] = 100
        while True:
            json = self._api.do('GET',
                                f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users',
                                query=query,
                                headers=headers)
            if 'Resources' not in json or not json['Resources']:
                return
            for v in json['Resources']:
                i = v['id']
                if i in seen:
                    continue
                seen.add(i)
                yield User.from_dict(v)
            query['startIndex'] += len(json['Resources'])

    def patch(self,
              id: str,
              *,
              operations: Optional[List[Patch]] = None,
              schemas: Optional[List[PatchSchema]] = None):
        """Update user details.
        
        Partially updates a user resource by applying the supplied operations on specific user attributes.
        
        :param id: str
          Unique ID for a user in the Databricks account.
        :param operations: List[:class:`Patch`] (optional)
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        """
        body = {}
        if operations is not None: body['Operations'] = [v.as_dict() for v in operations]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users/{id}',
                     body=body,
                     headers=headers)

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
               schemas: Optional[List[UserSchema]] = None,
               user_name: Optional[str] = None):
        """Replace a user.
        
        Replaces a user's information with the data supplied in request.
        
        :param id: str
          Databricks user ID. This is automatically set by Databricks. Any value provided by the client will
          be ignored.
        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`. This
          field cannot be updated through the Workspace SCIM APIs when [identity federation is enabled]. Use
          Account SCIM APIs to update `displayName`.
          
          [identity federation is enabled]: https://docs.databricks.com/administration-guide/users-groups/best-practices.html#enable-identity-federation
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the user. See [assigning entitlements] for a full list of supported values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
          External ID is not currently supported. It is reserved for future use.
        :param groups: List[:class:`ComplexValue`] (optional)
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`UserSchema`] (optional)
          The schema of the user.
        :param user_name: str (optional)
          Email address of the Databricks user.
        
        
        """
        body = {}
        if active is not None: body['active'] = active
        if display_name is not None: body['displayName'] = display_name
        if emails is not None: body['emails'] = [v.as_dict() for v in emails]
        if entitlements is not None: body['entitlements'] = [v.as_dict() for v in entitlements]
        if external_id is not None: body['externalId'] = external_id
        if groups is not None: body['groups'] = [v.as_dict() for v in groups]
        if name is not None: body['name'] = name.as_dict()
        if roles is not None: body['roles'] = [v.as_dict() for v in roles]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        if user_name is not None: body['userName'] = user_name
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PUT',
                     f'/api/2.0/accounts/{self._api.account_id}/scim/v2/Users/{id}',
                     body=body,
                     headers=headers)


class CurrentUserAPI:
    """This API allows retrieving information about currently authenticated user or service principal."""

    def __init__(self, api_client):
        self._api = api_client

    def me(self) -> User:
        """Get current user info.
        
        Get details about the current method caller's identity.
        
        :returns: :class:`User`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/preview/scim/v2/Me', headers=headers)
        return User.from_dict(res)


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
               schemas: Optional[List[GroupSchema]] = None) -> Group:
        """Create a new group.
        
        Creates a group in the Databricks workspace with a unique name, using the supplied group details.
        
        :param display_name: str (optional)
          String that represents a human-readable group name
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the group. See [assigning entitlements] for a full list of supported
          values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks group ID
        :param members: List[:class:`ComplexValue`] (optional)
        :param meta: :class:`ResourceMeta` (optional)
          Container for the group identifier. Workspace local versus account.
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`GroupSchema`] (optional)
          The schema of the group.
        
        :returns: :class:`Group`
        """
        body = {}
        if display_name is not None: body['displayName'] = display_name
        if entitlements is not None: body['entitlements'] = [v.as_dict() for v in entitlements]
        if external_id is not None: body['externalId'] = external_id
        if groups is not None: body['groups'] = [v.as_dict() for v in groups]
        if id is not None: body['id'] = id
        if members is not None: body['members'] = [v.as_dict() for v in members]
        if meta is not None: body['meta'] = meta.as_dict()
        if roles is not None: body['roles'] = [v.as_dict() for v in roles]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/preview/scim/v2/Groups', body=body, headers=headers)
        return Group.from_dict(res)

    def delete(self, id: str):
        """Delete a group.
        
        Deletes a group from the Databricks workspace.
        
        :param id: str
          Unique ID for a group in the Databricks workspace.
        
        
        """

        headers = {}
        self._api.do('DELETE', f'/api/2.0/preview/scim/v2/Groups/{id}', headers=headers)

    def get(self, id: str) -> Group:
        """Get group details.
        
        Gets the information for a specific group in the Databricks workspace.
        
        :param id: str
          Unique ID for a group in the Databricks workspace.
        
        :returns: :class:`Group`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/preview/scim/v2/Groups/{id}', headers=headers)
        return Group.from_dict(res)

    def list(self,
             *,
             attributes: Optional[str] = None,
             count: Optional[int] = None,
             excluded_attributes: Optional[str] = None,
             filter: Optional[str] = None,
             sort_by: Optional[str] = None,
             sort_order: Optional[ListSortOrder] = None,
             start_index: Optional[int] = None) -> Iterator[Group]:
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

        query = {}
        if attributes is not None: query['attributes'] = attributes
        if count is not None: query['count'] = count
        if excluded_attributes is not None: query['excludedAttributes'] = excluded_attributes
        if filter is not None: query['filter'] = filter
        if sort_by is not None: query['sortBy'] = sort_by
        if sort_order is not None: query['sortOrder'] = sort_order.value
        if start_index is not None: query['startIndex'] = start_index
        headers = {'Accept': 'application/json', }

        # deduplicate items that may have been added during iteration
        seen = set()
        query['startIndex'] = 1
        if "count" not in query: query['count'] = 100
        while True:
            json = self._api.do('GET', '/api/2.0/preview/scim/v2/Groups', query=query, headers=headers)
            if 'Resources' not in json or not json['Resources']:
                return
            for v in json['Resources']:
                i = v['id']
                if i in seen:
                    continue
                seen.add(i)
                yield Group.from_dict(v)
            query['startIndex'] += len(json['Resources'])

    def patch(self,
              id: str,
              *,
              operations: Optional[List[Patch]] = None,
              schemas: Optional[List[PatchSchema]] = None):
        """Update group details.
        
        Partially updates the details of a group.
        
        :param id: str
          Unique ID for a group in the Databricks workspace.
        :param operations: List[:class:`Patch`] (optional)
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        """
        body = {}
        if operations is not None: body['Operations'] = [v.as_dict() for v in operations]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PATCH', f'/api/2.0/preview/scim/v2/Groups/{id}', body=body, headers=headers)

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
               schemas: Optional[List[GroupSchema]] = None):
        """Replace a group.
        
        Updates the details of a group by replacing the entire group entity.
        
        :param id: str
          Databricks group ID
        :param display_name: str (optional)
          String that represents a human-readable group name
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the group. See [assigning entitlements] for a full list of supported
          values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param members: List[:class:`ComplexValue`] (optional)
        :param meta: :class:`ResourceMeta` (optional)
          Container for the group identifier. Workspace local versus account.
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`GroupSchema`] (optional)
          The schema of the group.
        
        
        """
        body = {}
        if display_name is not None: body['displayName'] = display_name
        if entitlements is not None: body['entitlements'] = [v.as_dict() for v in entitlements]
        if external_id is not None: body['externalId'] = external_id
        if groups is not None: body['groups'] = [v.as_dict() for v in groups]
        if members is not None: body['members'] = [v.as_dict() for v in members]
        if meta is not None: body['meta'] = meta.as_dict()
        if roles is not None: body['roles'] = [v.as_dict() for v in roles]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PUT', f'/api/2.0/preview/scim/v2/Groups/{id}', body=body, headers=headers)


class PermissionsAPI:
    """Permissions API are used to create read, write, edit, update and manage access for various users on
    different objects and endpoints.
    
    * **[Cluster permissions](:service:clusters)** — Manage which users can manage, restart, or attach to
    clusters.
    
    * **[Cluster policy permissions](:service:clusterpolicies)** — Manage which users can use cluster
    policies.
    
    * **[Delta Live Tables pipeline permissions](:service:pipelines)** — Manage which users can view,
    manage, run, cancel, or own a Delta Live Tables pipeline.
    
    * **[Job permissions](:service:jobs)** — Manage which users can view, manage, trigger, cancel, or own a
    job.
    
    * **[MLflow experiment permissions](:service:experiments)** — Manage which users can read, edit, or
    manage MLflow experiments.
    
    * **[MLflow registered model permissions](:service:modelregistry)** — Manage which users can read, edit,
    or manage MLflow registered models.
    
    * **[Password permissions](:service:users)** — Manage which users can use password login when SSO is
    enabled.
    
    * **[Instance Pool permissions](:service:instancepools)** — Manage which users can manage or attach to
    pools.
    
    * **[Repo permissions](repos)** — Manage which users can read, run, edit, or manage a repo.
    
    * **[Serving endpoint permissions](:service:servingendpoints)** — Manage which users can view, query, or
    manage a serving endpoint.
    
    * **[SQL warehouse permissions](:service:warehouses)** — Manage which users can use or manage SQL
    warehouses.
    
    * **[Token permissions](:service:tokenmanagement)** — Manage which users can create or use tokens.
    
    * **[Workspace object permissions](:service:workspace)** — Manage which users can read, run, edit, or
    manage directories, files, and notebooks.
    
    For the mapping of the required permissions for specific actions or abilities and other important
    information, see [Access Control].
    
    [Access Control]: https://docs.databricks.com/security/auth-authz/access-control/index.html"""

    def __init__(self, api_client):
        self._api = api_client

    def get(self, request_object_type: str, request_object_id: str) -> ObjectPermissions:
        """Get object permissions.
        
        Gets the permissions of an object. Objects can inherit permissions from their parent objects or root
        object.
        
        :param request_object_type: str
          The type of the request object. Can be one of the following: authorization, clusters,
          cluster-policies, directories, experiments, files, instance-pools, jobs, notebooks, pipelines,
          registered-models, repos, serving-endpoints, or sql-warehouses.
        :param request_object_id: str
          The id of the request object.
        
        :returns: :class:`ObjectPermissions`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/permissions/{request_object_type}/{request_object_id}',
                           headers=headers)
        return ObjectPermissions.from_dict(res)

    def get_permission_levels(self, request_object_type: str,
                              request_object_id: str) -> GetPermissionLevelsResponse:
        """Get object permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param request_object_type: str
          <needs content>
        :param request_object_id: str
          <needs content>
        
        :returns: :class:`GetPermissionLevelsResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/permissions/{request_object_type}/{request_object_id}/permissionLevels',
                           headers=headers)
        return GetPermissionLevelsResponse.from_dict(res)

    def set(self,
            request_object_type: str,
            request_object_id: str,
            *,
            access_control_list: Optional[List[AccessControlRequest]] = None) -> ObjectPermissions:
        """Set object permissions.
        
        Sets permissions on an object. Objects can inherit permissions from their parent objects or root
        object.
        
        :param request_object_type: str
          The type of the request object. Can be one of the following: authorization, clusters,
          cluster-policies, directories, experiments, files, instance-pools, jobs, notebooks, pipelines,
          registered-models, repos, serving-endpoints, or sql-warehouses.
        :param request_object_id: str
          The id of the request object.
        :param access_control_list: List[:class:`AccessControlRequest`] (optional)
        
        :returns: :class:`ObjectPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PUT',
                           f'/api/2.0/permissions/{request_object_type}/{request_object_id}',
                           body=body,
                           headers=headers)
        return ObjectPermissions.from_dict(res)

    def update(self,
               request_object_type: str,
               request_object_id: str,
               *,
               access_control_list: Optional[List[AccessControlRequest]] = None) -> ObjectPermissions:
        """Update object permissions.
        
        Updates the permissions on an object. Objects can inherit permissions from their parent objects or
        root object.
        
        :param request_object_type: str
          The type of the request object. Can be one of the following: authorization, clusters,
          cluster-policies, directories, experiments, files, instance-pools, jobs, notebooks, pipelines,
          registered-models, repos, serving-endpoints, or sql-warehouses.
        :param request_object_id: str
          The id of the request object.
        :param access_control_list: List[:class:`AccessControlRequest`] (optional)
        
        :returns: :class:`ObjectPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PATCH',
                           f'/api/2.0/permissions/{request_object_type}/{request_object_id}',
                           body=body,
                           headers=headers)
        return ObjectPermissions.from_dict(res)


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
               schemas: Optional[List[ServicePrincipalSchema]] = None) -> ServicePrincipal:
        """Create a service principal.
        
        Creates a new service principal in the Databricks workspace.
        
        :param active: bool (optional)
          If this user is active
        :param application_id: str (optional)
          UUID relating to the service principal
        :param display_name: str (optional)
          String that represents a concatenation of given and family names.
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the service principal. See [assigning entitlements] for a full list of
          supported values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks service principal ID.
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`ServicePrincipalSchema`] (optional)
          The schema of the List response.
        
        :returns: :class:`ServicePrincipal`
        """
        body = {}
        if active is not None: body['active'] = active
        if application_id is not None: body['applicationId'] = application_id
        if display_name is not None: body['displayName'] = display_name
        if entitlements is not None: body['entitlements'] = [v.as_dict() for v in entitlements]
        if external_id is not None: body['externalId'] = external_id
        if groups is not None: body['groups'] = [v.as_dict() for v in groups]
        if id is not None: body['id'] = id
        if roles is not None: body['roles'] = [v.as_dict() for v in roles]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/preview/scim/v2/ServicePrincipals', body=body, headers=headers)
        return ServicePrincipal.from_dict(res)

    def delete(self, id: str):
        """Delete a service principal.
        
        Delete a single service principal in the Databricks workspace.
        
        :param id: str
          Unique ID for a service principal in the Databricks workspace.
        
        
        """

        headers = {}
        self._api.do('DELETE', f'/api/2.0/preview/scim/v2/ServicePrincipals/{id}', headers=headers)

    def get(self, id: str) -> ServicePrincipal:
        """Get service principal details.
        
        Gets the details for a single service principal define in the Databricks workspace.
        
        :param id: str
          Unique ID for a service principal in the Databricks workspace.
        
        :returns: :class:`ServicePrincipal`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/preview/scim/v2/ServicePrincipals/{id}', headers=headers)
        return ServicePrincipal.from_dict(res)

    def list(self,
             *,
             attributes: Optional[str] = None,
             count: Optional[int] = None,
             excluded_attributes: Optional[str] = None,
             filter: Optional[str] = None,
             sort_by: Optional[str] = None,
             sort_order: Optional[ListSortOrder] = None,
             start_index: Optional[int] = None) -> Iterator[ServicePrincipal]:
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

        query = {}
        if attributes is not None: query['attributes'] = attributes
        if count is not None: query['count'] = count
        if excluded_attributes is not None: query['excludedAttributes'] = excluded_attributes
        if filter is not None: query['filter'] = filter
        if sort_by is not None: query['sortBy'] = sort_by
        if sort_order is not None: query['sortOrder'] = sort_order.value
        if start_index is not None: query['startIndex'] = start_index
        headers = {'Accept': 'application/json', }

        # deduplicate items that may have been added during iteration
        seen = set()
        query['startIndex'] = 1
        if "count" not in query: query['count'] = 100
        while True:
            json = self._api.do('GET',
                                '/api/2.0/preview/scim/v2/ServicePrincipals',
                                query=query,
                                headers=headers)
            if 'Resources' not in json or not json['Resources']:
                return
            for v in json['Resources']:
                i = v['id']
                if i in seen:
                    continue
                seen.add(i)
                yield ServicePrincipal.from_dict(v)
            query['startIndex'] += len(json['Resources'])

    def patch(self,
              id: str,
              *,
              operations: Optional[List[Patch]] = None,
              schemas: Optional[List[PatchSchema]] = None):
        """Update service principal details.
        
        Partially updates the details of a single service principal in the Databricks workspace.
        
        :param id: str
          Unique ID for a service principal in the Databricks workspace.
        :param operations: List[:class:`Patch`] (optional)
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        """
        body = {}
        if operations is not None: body['Operations'] = [v.as_dict() for v in operations]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PATCH', f'/api/2.0/preview/scim/v2/ServicePrincipals/{id}', body=body, headers=headers)

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
               schemas: Optional[List[ServicePrincipalSchema]] = None):
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
          Entitlements assigned to the service principal. See [assigning entitlements] for a full list of
          supported values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`ServicePrincipalSchema`] (optional)
          The schema of the List response.
        
        
        """
        body = {}
        if active is not None: body['active'] = active
        if application_id is not None: body['applicationId'] = application_id
        if display_name is not None: body['displayName'] = display_name
        if entitlements is not None: body['entitlements'] = [v.as_dict() for v in entitlements]
        if external_id is not None: body['externalId'] = external_id
        if groups is not None: body['groups'] = [v.as_dict() for v in groups]
        if roles is not None: body['roles'] = [v.as_dict() for v in roles]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PUT', f'/api/2.0/preview/scim/v2/ServicePrincipals/{id}', body=body, headers=headers)


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
               schemas: Optional[List[UserSchema]] = None,
               user_name: Optional[str] = None) -> User:
        """Create a new user.
        
        Creates a new user in the Databricks workspace. This new user will also be added to the Databricks
        account.
        
        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`. This
          field cannot be updated through the Workspace SCIM APIs when [identity federation is enabled]. Use
          Account SCIM APIs to update `displayName`.
          
          [identity federation is enabled]: https://docs.databricks.com/administration-guide/users-groups/best-practices.html#enable-identity-federation
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the user. See [assigning entitlements] for a full list of supported values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
          External ID is not currently supported. It is reserved for future use.
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks user ID. This is automatically set by Databricks. Any value provided by the client will
          be ignored.
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`UserSchema`] (optional)
          The schema of the user.
        :param user_name: str (optional)
          Email address of the Databricks user.
        
        :returns: :class:`User`
        """
        body = {}
        if active is not None: body['active'] = active
        if display_name is not None: body['displayName'] = display_name
        if emails is not None: body['emails'] = [v.as_dict() for v in emails]
        if entitlements is not None: body['entitlements'] = [v.as_dict() for v in entitlements]
        if external_id is not None: body['externalId'] = external_id
        if groups is not None: body['groups'] = [v.as_dict() for v in groups]
        if id is not None: body['id'] = id
        if name is not None: body['name'] = name.as_dict()
        if roles is not None: body['roles'] = [v.as_dict() for v in roles]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        if user_name is not None: body['userName'] = user_name
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/preview/scim/v2/Users', body=body, headers=headers)
        return User.from_dict(res)

    def delete(self, id: str):
        """Delete a user.
        
        Deletes a user. Deleting a user from a Databricks workspace also removes objects associated with the
        user.
        
        :param id: str
          Unique ID for a user in the Databricks workspace.
        
        
        """

        headers = {}
        self._api.do('DELETE', f'/api/2.0/preview/scim/v2/Users/{id}', headers=headers)

    def get(self,
            id: str,
            *,
            attributes: Optional[str] = None,
            count: Optional[int] = None,
            excluded_attributes: Optional[str] = None,
            filter: Optional[str] = None,
            sort_by: Optional[str] = None,
            sort_order: Optional[GetSortOrder] = None,
            start_index: Optional[int] = None) -> User:
        """Get user details.
        
        Gets information for a specific user in Databricks workspace.
        
        :param id: str
          Unique ID for a user in the Databricks workspace.
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
        :param sort_order: :class:`GetSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: :class:`User`
        """

        query = {}
        if attributes is not None: query['attributes'] = attributes
        if count is not None: query['count'] = count
        if excluded_attributes is not None: query['excludedAttributes'] = excluded_attributes
        if filter is not None: query['filter'] = filter
        if sort_by is not None: query['sortBy'] = sort_by
        if sort_order is not None: query['sortOrder'] = sort_order.value
        if start_index is not None: query['startIndex'] = start_index
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/preview/scim/v2/Users/{id}', query=query, headers=headers)
        return User.from_dict(res)

    def get_permission_levels(self) -> GetPasswordPermissionLevelsResponse:
        """Get password permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :returns: :class:`GetPasswordPermissionLevelsResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           '/api/2.0/permissions/authorization/passwords/permissionLevels',
                           headers=headers)
        return GetPasswordPermissionLevelsResponse.from_dict(res)

    def get_permissions(self) -> PasswordPermissions:
        """Get password permissions.
        
        Gets the permissions of all passwords. Passwords can inherit permissions from their root object.
        
        :returns: :class:`PasswordPermissions`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/permissions/authorization/passwords', headers=headers)
        return PasswordPermissions.from_dict(res)

    def list(self,
             *,
             attributes: Optional[str] = None,
             count: Optional[int] = None,
             excluded_attributes: Optional[str] = None,
             filter: Optional[str] = None,
             sort_by: Optional[str] = None,
             sort_order: Optional[ListSortOrder] = None,
             start_index: Optional[int] = None) -> Iterator[User]:
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

        query = {}
        if attributes is not None: query['attributes'] = attributes
        if count is not None: query['count'] = count
        if excluded_attributes is not None: query['excludedAttributes'] = excluded_attributes
        if filter is not None: query['filter'] = filter
        if sort_by is not None: query['sortBy'] = sort_by
        if sort_order is not None: query['sortOrder'] = sort_order.value
        if start_index is not None: query['startIndex'] = start_index
        headers = {'Accept': 'application/json', }

        # deduplicate items that may have been added during iteration
        seen = set()
        query['startIndex'] = 1
        if "count" not in query: query['count'] = 100
        while True:
            json = self._api.do('GET', '/api/2.0/preview/scim/v2/Users', query=query, headers=headers)
            if 'Resources' not in json or not json['Resources']:
                return
            for v in json['Resources']:
                i = v['id']
                if i in seen:
                    continue
                seen.add(i)
                yield User.from_dict(v)
            query['startIndex'] += len(json['Resources'])

    def patch(self,
              id: str,
              *,
              operations: Optional[List[Patch]] = None,
              schemas: Optional[List[PatchSchema]] = None):
        """Update user details.
        
        Partially updates a user resource by applying the supplied operations on specific user attributes.
        
        :param id: str
          Unique ID for a user in the Databricks workspace.
        :param operations: List[:class:`Patch`] (optional)
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        """
        body = {}
        if operations is not None: body['Operations'] = [v.as_dict() for v in operations]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PATCH', f'/api/2.0/preview/scim/v2/Users/{id}', body=body, headers=headers)

    def set_permissions(
            self,
            *,
            access_control_list: Optional[List[PasswordAccessControlRequest]] = None) -> PasswordPermissions:
        """Set password permissions.
        
        Sets permissions on all passwords. Passwords can inherit permissions from their root object.
        
        :param access_control_list: List[:class:`PasswordAccessControlRequest`] (optional)
        
        :returns: :class:`PasswordPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PUT', '/api/2.0/permissions/authorization/passwords', body=body, headers=headers)
        return PasswordPermissions.from_dict(res)

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
               schemas: Optional[List[UserSchema]] = None,
               user_name: Optional[str] = None):
        """Replace a user.
        
        Replaces a user's information with the data supplied in request.
        
        :param id: str
          Databricks user ID. This is automatically set by Databricks. Any value provided by the client will
          be ignored.
        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`. This
          field cannot be updated through the Workspace SCIM APIs when [identity federation is enabled]. Use
          Account SCIM APIs to update `displayName`.
          
          [identity federation is enabled]: https://docs.databricks.com/administration-guide/users-groups/best-practices.html#enable-identity-federation
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the user. See [assigning entitlements] for a full list of supported values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
          External ID is not currently supported. It is reserved for future use.
        :param groups: List[:class:`ComplexValue`] (optional)
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`UserSchema`] (optional)
          The schema of the user.
        :param user_name: str (optional)
          Email address of the Databricks user.
        
        
        """
        body = {}
        if active is not None: body['active'] = active
        if display_name is not None: body['displayName'] = display_name
        if emails is not None: body['emails'] = [v.as_dict() for v in emails]
        if entitlements is not None: body['entitlements'] = [v.as_dict() for v in entitlements]
        if external_id is not None: body['externalId'] = external_id
        if groups is not None: body['groups'] = [v.as_dict() for v in groups]
        if name is not None: body['name'] = name.as_dict()
        if roles is not None: body['roles'] = [v.as_dict() for v in roles]
        if schemas is not None: body['schemas'] = [v.value for v in schemas]
        if user_name is not None: body['userName'] = user_name
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PUT', f'/api/2.0/preview/scim/v2/Users/{id}', body=body, headers=headers)

    def update_permissions(
            self,
            *,
            access_control_list: Optional[List[PasswordAccessControlRequest]] = None) -> PasswordPermissions:
        """Update password permissions.
        
        Updates the permissions on all passwords. Passwords can inherit permissions from their root object.
        
        :param access_control_list: List[:class:`PasswordAccessControlRequest`] (optional)
        
        :returns: :class:`PasswordPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PATCH',
                           '/api/2.0/permissions/authorization/passwords',
                           body=body,
                           headers=headers)
        return PasswordPermissions.from_dict(res)


class WorkspaceAssignmentAPI:
    """The Workspace Permission Assignment API allows you to manage workspace permissions for principals in your
    account."""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, workspace_id: int, principal_id: int):
        """Delete permissions assignment.
        
        Deletes the workspace permissions assignment in a given account and workspace for the specified
        principal.
        
        :param workspace_id: int
          The workspace ID.
        :param principal_id: int
          The ID of the user, service principal, or group.
        
        
        """

        headers = {'Accept': 'application/json', }
        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{workspace_id}/permissionassignments/principals/{principal_id}',
            headers=headers)

    def get(self, workspace_id: int) -> WorkspacePermissions:
        """List workspace permissions.
        
        Get an array of workspace permissions for the specified account and workspace.
        
        :param workspace_id: int
          The workspace ID.
        
        :returns: :class:`WorkspacePermissions`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{workspace_id}/permissionassignments/permissions',
            headers=headers)
        return WorkspacePermissions.from_dict(res)

    def list(self, workspace_id: int) -> Iterator[PermissionAssignment]:
        """Get permission assignments.
        
        Get the permission assignments for the specified Databricks account and Databricks workspace.
        
        :param workspace_id: int
          The workspace ID for the account.
        
        :returns: Iterator over :class:`PermissionAssignment`
        """

        headers = {'Accept': 'application/json', }
        json = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{workspace_id}/permissionassignments',
            headers=headers)
        parsed = PermissionAssignments.from_dict(json).permission_assignments
        return parsed if parsed is not None else []

    def update(self, workspace_id: int, principal_id: int, permissions: List[WorkspacePermission]):
        """Create or update permissions assignment.
        
        Creates or updates the workspace permissions assignment in a given account and workspace for the
        specified principal.
        
        :param workspace_id: int
          The workspace ID.
        :param principal_id: int
          The ID of the user, service principal, or group.
        :param permissions: List[:class:`WorkspacePermission`]
          Array of permissions assignments to update on the workspace.
        
        
        """
        body = {}
        if permissions is not None: body['permissions'] = [v.value for v in permissions]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do(
            'PUT',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{workspace_id}/permissionassignments/principals/{principal_id}',
            body=body,
            headers=headers)

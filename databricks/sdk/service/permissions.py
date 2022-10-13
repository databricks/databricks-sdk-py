# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'AccessControlRequest',
    'AccessControlRequestPermissionLevel',
    'AccessControlResponse',
    'GetPermissionLevelsResponse',
    'ObjectPermissions',
    'Permission',
    'PermissionPermissionLevel',
    'PermissionsDescription',
    'PermissionsDescriptionPermissionLevel',
    'SetObjectPermissions',
    'UpdateObjectPermissions',
    'GetObjectPermissionsRequest',
    'GetPermissionLevelsRequest',
    
    'Permissions',
]

# all definitions in this file are in alphabetical order

@dataclass
class AccessControlRequest:
    
    # name of the group
    group_name: str = None
    # Permission level
    permission_level: 'AccessControlRequestPermissionLevel' = None
    # name of the service principal
    service_principal_name: str = None
    # name of the user
    user_name: str = None

    def as_request(self) -> (dict, dict):
        accessControlRequest_query, accessControlRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.group_name:
            accessControlRequest_body['group_name'] = self.group_name
        if self.permission_level:
            accessControlRequest_body['permission_level'] = self.permission_level.value
        if self.service_principal_name:
            accessControlRequest_body['service_principal_name'] = self.service_principal_name
        if self.user_name:
            accessControlRequest_body['user_name'] = self.user_name
        
        return accessControlRequest_query, accessControlRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AccessControlRequest':
        return cls(
            group_name=d.get('group_name', None),
            permission_level=AccessControlRequestPermissionLevel(d['permission_level']) if 'permission_level' in d else None,
            service_principal_name=d.get('service_principal_name', None),
            user_name=d.get('user_name', None),
        )



class AccessControlRequestPermissionLevel(Enum):
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
class AccessControlResponse:
    
    # All permissions.
    all_permissions: 'List[Permission]' = None
    # name of the group
    group_name: str = None
    # name of the service principal
    service_principal_name: str = None
    # name of the user
    user_name: str = None

    def as_request(self) -> (dict, dict):
        accessControlResponse_query, accessControlResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.all_permissions:
            accessControlResponse_body['all_permissions'] = [v.as_request()[1] for v in self.all_permissions]
        if self.group_name:
            accessControlResponse_body['group_name'] = self.group_name
        if self.service_principal_name:
            accessControlResponse_body['service_principal_name'] = self.service_principal_name
        if self.user_name:
            accessControlResponse_body['user_name'] = self.user_name
        
        return accessControlResponse_query, accessControlResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AccessControlResponse':
        return cls(
            all_permissions=[Permission.from_dict(v) for v in d['all_permissions']] if 'all_permissions' in d else None,
            group_name=d.get('group_name', None),
            service_principal_name=d.get('service_principal_name', None),
            user_name=d.get('user_name', None),
        )



@dataclass
class GetPermissionLevelsResponse:
    
    # Specific permission levels
    permission_levels: 'List[PermissionsDescription]' = None

    def as_request(self) -> (dict, dict):
        getPermissionLevelsResponse_query, getPermissionLevelsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.permission_levels:
            getPermissionLevelsResponse_body['permission_levels'] = [v.as_request()[1] for v in self.permission_levels]
        
        return getPermissionLevelsResponse_query, getPermissionLevelsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPermissionLevelsResponse':
        return cls(
            permission_levels=[PermissionsDescription.from_dict(v) for v in d['permission_levels']] if 'permission_levels' in d else None,
        )



@dataclass
class ObjectPermissions:
    
    
    access_control_list: 'List[AccessControlResponse]' = None
    
    object_id: str = None
    
    object_type: str = None

    def as_request(self) -> (dict, dict):
        objectPermissions_query, objectPermissions_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.access_control_list:
            objectPermissions_body['access_control_list'] = [v.as_request()[1] for v in self.access_control_list]
        if self.object_id:
            objectPermissions_body['object_id'] = self.object_id
        if self.object_type:
            objectPermissions_body['object_type'] = self.object_type
        
        return objectPermissions_query, objectPermissions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ObjectPermissions':
        return cls(
            access_control_list=[AccessControlResponse.from_dict(v) for v in d['access_control_list']] if 'access_control_list' in d else None,
            object_id=d.get('object_id', None),
            object_type=d.get('object_type', None),
        )



@dataclass
class Permission:
    
    
    inherited: bool = None
    
    inherited_from_object: 'List[str]' = None
    
    permission_level: 'PermissionPermissionLevel' = None

    def as_request(self) -> (dict, dict):
        permission_query, permission_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.inherited:
            permission_body['inherited'] = self.inherited
        if self.inherited_from_object:
            permission_body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level:
            permission_body['permission_level'] = self.permission_level.value
        
        return permission_query, permission_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Permission':
        return cls(
            inherited=d.get('inherited', None),
            inherited_from_object=d.get('inherited_from_object', None),
            permission_level=PermissionPermissionLevel(d['permission_level']) if 'permission_level' in d else None,
        )



class PermissionPermissionLevel(Enum):
    
    
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
class PermissionsDescription:
    
    
    description: str = None
    
    permission_level: 'PermissionsDescriptionPermissionLevel' = None

    def as_request(self) -> (dict, dict):
        permissionsDescription_query, permissionsDescription_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.description:
            permissionsDescription_body['description'] = self.description
        if self.permission_level:
            permissionsDescription_body['permission_level'] = self.permission_level.value
        
        return permissionsDescription_query, permissionsDescription_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermissionsDescription':
        return cls(
            description=d.get('description', None),
            permission_level=PermissionsDescriptionPermissionLevel(d['permission_level']) if 'permission_level' in d else None,
        )



class PermissionsDescriptionPermissionLevel(Enum):
    
    
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
class SetObjectPermissions:
    
    
    access_control_list: 'List[AccessControlRequest]' = None
    
    object_id: str = None # path
    
    object_type: str = None # path

    def as_request(self) -> (dict, dict):
        setObjectPermissions_query, setObjectPermissions_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.access_control_list:
            setObjectPermissions_body['access_control_list'] = [v.as_request()[1] for v in self.access_control_list]
        if self.object_id:
            setObjectPermissions_body['object_id'] = self.object_id
        if self.object_type:
            setObjectPermissions_body['object_type'] = self.object_type
        
        return setObjectPermissions_query, setObjectPermissions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetObjectPermissions':
        return cls(
            access_control_list=[AccessControlRequest.from_dict(v) for v in d['access_control_list']] if 'access_control_list' in d else None,
            object_id=d.get('object_id', None),
            object_type=d.get('object_type', None),
        )



@dataclass
class UpdateObjectPermissions:
    
    
    access_control_list: 'List[AccessControlRequest]' = None
    
    object_id: str = None # path
    
    object_type: str = None # path

    def as_request(self) -> (dict, dict):
        updateObjectPermissions_query, updateObjectPermissions_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.access_control_list:
            updateObjectPermissions_body['access_control_list'] = [v.as_request()[1] for v in self.access_control_list]
        if self.object_id:
            updateObjectPermissions_body['object_id'] = self.object_id
        if self.object_type:
            updateObjectPermissions_body['object_type'] = self.object_type
        
        return updateObjectPermissions_query, updateObjectPermissions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateObjectPermissions':
        return cls(
            access_control_list=[AccessControlRequest.from_dict(v) for v in d['access_control_list']] if 'access_control_list' in d else None,
            object_id=d.get('object_id', None),
            object_type=d.get('object_type', None),
        )



@dataclass
class GetObjectPermissionsRequest:
    
    
    object_id: str # path
    # <needs content>
    object_type: str # path

    def as_request(self) -> (dict, dict):
        getObjectPermissionsRequest_query, getObjectPermissionsRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.object_id:
            getObjectPermissionsRequest_body['object_id'] = self.object_id
        if self.object_type:
            getObjectPermissionsRequest_body['object_type'] = self.object_type
        
        return getObjectPermissionsRequest_query, getObjectPermissionsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetObjectPermissionsRequest':
        return cls(
            object_id=d.get('object_id', None),
            object_type=d.get('object_type', None),
        )



@dataclass
class GetPermissionLevelsRequest:
    
    # <needs content>
    request_object_id: str # path
    # <needs content>
    request_object_type: str # path

    def as_request(self) -> (dict, dict):
        getPermissionLevelsRequest_query, getPermissionLevelsRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.request_object_id:
            getPermissionLevelsRequest_body['request_object_id'] = self.request_object_id
        if self.request_object_type:
            getPermissionLevelsRequest_body['request_object_type'] = self.request_object_type
        
        return getPermissionLevelsRequest_query, getPermissionLevelsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPermissionLevelsRequest':
        return cls(
            request_object_id=d.get('request_object_id', None),
            request_object_type=d.get('request_object_type', None),
        )



class PermissionsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def getObjectPermissions(self, request: GetObjectPermissionsRequest) -> ObjectPermissions:
        """Get object permissions
        
        Get the permission of an object. Objects can inherit permissions from
        their parent objects or root objects."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/permissions/{request.object_type}/{request.object_id}', query=query, body=body)
        return ObjectPermissions.from_dict(json)
    
    def getPermissionLevels(self, request: GetPermissionLevelsRequest) -> GetPermissionLevelsResponse:
        """Get permission levels
        
        Get permission levels that a user can have."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/permissions/{request.request_object_type}/{request.request_object_id}/permissionLevels', query=query, body=body)
        return GetPermissionLevelsResponse.from_dict(json)
    
    def setObjectPermissions(self, request: SetObjectPermissions):
        """Set permissions
        
        Set permissions on object. Objects can inherit permissiond from their
        parent objects and root objects."""
        query, body = request.as_request()
        self._api.do('PUT', f'/api/2.0/permissions/{request.object_type}/{request.object_id}', query=query, body=body)
        
    
    def updateObjectPermissions(self, request: UpdateObjectPermissions):
        """Update permission
        
        Update permission on objects"""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.0/permissions/{request.object_type}/{request.object_id}', query=query, body=body)
        
    
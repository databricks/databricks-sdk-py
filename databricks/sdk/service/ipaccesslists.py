# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'CreateIPAccessListRequest',
    'DeleteIpAccessListRequest',
    'FetchIpAccessListRequest',
    'GetIPAccessListResponse',
    'IpAccessListInfo',
    'ReplaceIPAccessListRequest',
    'UpdateIPAccessListRequest',
    'AddressCount',
    'CreatedAt',
    'CreatedBy',
    'Enabled',
    'Label',
    'ListId',
    'ListType',
    'UpdatedAt',
    'UpdatedBy',
    
    'IpAccessLists',
]

# all definitions in this file are in alphabetical order

@dataclass
class CreateIPAccessListRequest:
    
    
    ip_addresses: 'List[str]'
    
    label: str
    
    list_type: 'ListType'

    def as_request(self) -> (dict, dict):
        createIPAccessListRequest_query, createIPAccessListRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.ip_addresses:
            createIPAccessListRequest_body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label:
            createIPAccessListRequest_body['label'] = self.label
        if self.list_type:
            createIPAccessListRequest_body['list_type'] = self.list_type.value
        
        return createIPAccessListRequest_query, createIPAccessListRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateIPAccessListRequest':
        return cls(
            ip_addresses=d.get('ip_addresses', None),
            label=d.get('label', None),
            list_type=ListType(d['list_type']) if 'list_type' in d else None,
        )



@dataclass
class DeleteIpAccessListRequest:
    
    # The ID for the corresponding IP access list to modify.
    ip_access_list_id: str # path

    def as_request(self) -> (dict, dict):
        deleteIpAccessListRequest_query, deleteIpAccessListRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.ip_access_list_id:
            deleteIpAccessListRequest_body['ip_access_list_id'] = self.ip_access_list_id
        
        return deleteIpAccessListRequest_query, deleteIpAccessListRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteIpAccessListRequest':
        return cls(
            ip_access_list_id=d.get('ip_access_list_id', None),
        )



@dataclass
class FetchIpAccessListRequest:
    
    # The ID for the corresponding IP access list to modify.
    ip_access_list_id: str # path

    def as_request(self) -> (dict, dict):
        fetchIpAccessListRequest_query, fetchIpAccessListRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.ip_access_list_id:
            fetchIpAccessListRequest_body['ip_access_list_id'] = self.ip_access_list_id
        
        return fetchIpAccessListRequest_query, fetchIpAccessListRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FetchIpAccessListRequest':
        return cls(
            ip_access_list_id=d.get('ip_access_list_id', None),
        )



@dataclass
class GetIPAccessListResponse:
    
    
    ip_access_lists: 'List[IpAccessListInfo]' = None

    def as_request(self) -> (dict, dict):
        getIPAccessListResponse_query, getIPAccessListResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.ip_access_lists:
            getIPAccessListResponse_body['ip_access_lists'] = [v.as_request()[1] for v in self.ip_access_lists]
        
        return getIPAccessListResponse_query, getIPAccessListResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetIPAccessListResponse':
        return cls(
            ip_access_lists=[IpAccessListInfo.from_dict(v) for v in d['ip_access_lists']] if 'ip_access_lists' in d else None,
        )



@dataclass
class IpAccessListInfo:
    
    
    address_count: int = None
    
    created_at: int = None
    
    created_by: int = None
    
    enabled: bool = None
    
    ip_addresses: 'List[str]' = None
    
    label: str = None
    
    list_id: str = None
    
    list_type: 'ListType' = None
    
    updated_at: int = None
    
    updated_by: int = None

    def as_request(self) -> (dict, dict):
        ipAccessListInfo_query, ipAccessListInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.address_count:
            ipAccessListInfo_body['address_count'] = self.address_count
        if self.created_at:
            ipAccessListInfo_body['created_at'] = self.created_at
        if self.created_by:
            ipAccessListInfo_body['created_by'] = self.created_by
        if self.enabled:
            ipAccessListInfo_body['enabled'] = self.enabled
        if self.ip_addresses:
            ipAccessListInfo_body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label:
            ipAccessListInfo_body['label'] = self.label
        if self.list_id:
            ipAccessListInfo_body['list_id'] = self.list_id
        if self.list_type:
            ipAccessListInfo_body['list_type'] = self.list_type.value
        if self.updated_at:
            ipAccessListInfo_body['updated_at'] = self.updated_at
        if self.updated_by:
            ipAccessListInfo_body['updated_by'] = self.updated_by
        
        return ipAccessListInfo_query, ipAccessListInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'IpAccessListInfo':
        return cls(
            address_count=d.get('address_count', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            enabled=d.get('enabled', None),
            ip_addresses=d.get('ip_addresses', None),
            label=d.get('label', None),
            list_id=d.get('list_id', None),
            list_type=ListType(d['list_type']) if 'list_type' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



@dataclass
class ReplaceIPAccessListRequest:
    
    
    enabled: bool
    # The ID for the corresponding IP access list to modify.
    ip_access_list_id: str # path
    
    ip_addresses: 'List[str]'
    
    label: str
    
    list_type: 'ListType'
    
    list_id: str = None

    def as_request(self) -> (dict, dict):
        replaceIPAccessListRequest_query, replaceIPAccessListRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.enabled:
            replaceIPAccessListRequest_body['enabled'] = self.enabled
        if self.ip_access_list_id:
            replaceIPAccessListRequest_body['ip_access_list_id'] = self.ip_access_list_id
        if self.ip_addresses:
            replaceIPAccessListRequest_body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label:
            replaceIPAccessListRequest_body['label'] = self.label
        if self.list_id:
            replaceIPAccessListRequest_body['list_id'] = self.list_id
        if self.list_type:
            replaceIPAccessListRequest_body['list_type'] = self.list_type.value
        
        return replaceIPAccessListRequest_query, replaceIPAccessListRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ReplaceIPAccessListRequest':
        return cls(
            enabled=d.get('enabled', None),
            ip_access_list_id=d.get('ip_access_list_id', None),
            ip_addresses=d.get('ip_addresses', None),
            label=d.get('label', None),
            list_id=d.get('list_id', None),
            list_type=ListType(d['list_type']) if 'list_type' in d else None,
        )



@dataclass
class UpdateIPAccessListRequest:
    
    # The ID for the corresponding IP access list to modify.
    ip_access_list_id: str # path
    
    enabled: bool = None
    
    ip_addresses: 'List[str]' = None
    
    label: str = None
    
    list_id: str = None
    
    list_type: 'ListType' = None

    def as_request(self) -> (dict, dict):
        updateIPAccessListRequest_query, updateIPAccessListRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.enabled:
            updateIPAccessListRequest_body['enabled'] = self.enabled
        if self.ip_access_list_id:
            updateIPAccessListRequest_body['ip_access_list_id'] = self.ip_access_list_id
        if self.ip_addresses:
            updateIPAccessListRequest_body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label:
            updateIPAccessListRequest_body['label'] = self.label
        if self.list_id:
            updateIPAccessListRequest_body['list_id'] = self.list_id
        if self.list_type:
            updateIPAccessListRequest_body['list_type'] = self.list_type.value
        
        return updateIPAccessListRequest_query, updateIPAccessListRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateIPAccessListRequest':
        return cls(
            enabled=d.get('enabled', None),
            ip_access_list_id=d.get('ip_access_list_id', None),
            ip_addresses=d.get('ip_addresses', None),
            label=d.get('label', None),
            list_id=d.get('list_id', None),
            list_type=ListType(d['list_type']) if 'list_type' in d else None,
        )















class ListType(Enum):
    """This describes an enum"""
    
    ALLOW = 'ALLOW'
    BLOCK = 'BLOCK'





class IpAccessListsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def createIpAccessList(self, request: CreateIPAccessListRequest) -> IpAccessListInfo:
        """Create access list
        
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
        [`/workspace-conf`](#operation/set-status)."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/ip-access-lists', query=query, body=body)
        return IpAccessListInfo.from_dict(json)
    
    def deleteIpAccessList(self, request: DeleteIpAccessListRequest):
        """Delete access list
        
        Deletes an IP access list, specified by its list ID."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.0/ip-access-lists/{request.ip_access_list_id}', query=query, body=body)
        
    
    def fetchIpAccessList(self, request: FetchIpAccessListRequest) -> IpAccessListInfo:
        """Get access list
        
        Gets an IP access list, specified by its list ID."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/ip-access-lists/{request.ip_access_list_id}', query=query, body=body)
        return IpAccessListInfo.from_dict(json)
    
    def getAllIpAccessLists(self) -> GetIPAccessListResponse:
        """Get access lists
        
        Gets all IP access lists for the specified workspace."""
        
        json = self._api.do('GET', '/api/2.0/ip-access-lists')
        return GetIPAccessListResponse.from_dict(json)
    
    def replaceIpAccessList(self, request: ReplaceIPAccessListRequest):
        """Replace access list
        
        Replaces an IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file
        for a description of how the server treats allow lists and block lists
        at run time.
        
        When replacing an IP access list:
        
        * For all allow lists and block lists combined, the API supports a
        maximum of 1000 IP/CIDR values, where one CIDR counts as a single value.
        Attempts to exceed that number return error 400 with `error_code` value
        `QUOTA_EXCEEDED`. * If the resulting list would block the calling user's
        current IP, error 400 is returned with `error_code` value
        `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect.
        
        Note that your resulting IP access list has no effect until you enable
        the feature. See [`/workspace-conf`](#operation/set-status)."""
        query, body = request.as_request()
        self._api.do('PUT', f'/api/2.0/ip-access-lists/{request.ip_access_list_id}', query=query, body=body)
        
    
    def updateIpAccessList(self, request: UpdateIPAccessListRequest):
        """Update access list
        
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
        [`/workspace-conf`](#operation/set-status)."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.0/ip-access-lists/{request.ip_access_list_id}', query=query, body=body)
        
    
# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List

from ._internal import _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class CreateIpAccessList:
    label: str
    list_type: 'ListType'
    ip_addresses: 'List[str]'

    def as_dict(self) -> dict:
        body = {}
        if self.ip_addresses: body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label is not None: body['label'] = self.label
        if self.list_type is not None: body['list_type'] = self.list_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateIpAccessList':
        return cls(ip_addresses=d.get('ip_addresses', None),
                   label=d.get('label', None),
                   list_type=_enum(d, 'list_type', ListType))


@dataclass
class CreateIpAccessListResponse:
    ip_access_list: 'IpAccessListInfo' = None

    def as_dict(self) -> dict:
        body = {}
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateIpAccessListResponse':
        return cls(ip_access_list=_from_dict(d, 'ip_access_list', IpAccessListInfo))


@dataclass
class CreateOboTokenRequest:
    application_id: str
    lifetime_seconds: int
    comment: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.application_id is not None: body['application_id'] = self.application_id
        if self.comment is not None: body['comment'] = self.comment
        if self.lifetime_seconds is not None: body['lifetime_seconds'] = self.lifetime_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateOboTokenRequest':
        return cls(application_id=d.get('application_id', None),
                   comment=d.get('comment', None),
                   lifetime_seconds=d.get('lifetime_seconds', None))


@dataclass
class CreateOboTokenResponse:
    token_info: 'TokenInfo' = None
    token_value: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.token_info: body['token_info'] = self.token_info.as_dict()
        if self.token_value is not None: body['token_value'] = self.token_value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateOboTokenResponse':
        return cls(token_info=_from_dict(d, 'token_info', TokenInfo), token_value=d.get('token_value', None))


@dataclass
class CreateTokenRequest:
    comment: str = None
    lifetime_seconds: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.lifetime_seconds is not None: body['lifetime_seconds'] = self.lifetime_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateTokenRequest':
        return cls(comment=d.get('comment', None), lifetime_seconds=d.get('lifetime_seconds', None))


@dataclass
class CreateTokenResponse:
    token_info: 'PublicTokenInfo' = None
    token_value: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.token_info: body['token_info'] = self.token_info.as_dict()
        if self.token_value is not None: body['token_value'] = self.token_value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateTokenResponse':
        return cls(token_info=_from_dict(d, 'token_info', PublicTokenInfo),
                   token_value=d.get('token_value', None))


@dataclass
class DeleteAccountIpAccessListRequest:
    """Delete access list"""

    ip_access_list_id: str


@dataclass
class DeleteIpAccessListRequest:
    """Delete access list"""

    ip_access_list_id: str


@dataclass
class DeleteTokenManagementRequest:
    """Delete a token"""

    token_id: str


@dataclass
class FetchIpAccessListResponse:
    ip_access_list: 'IpAccessListInfo' = None

    def as_dict(self) -> dict:
        body = {}
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FetchIpAccessListResponse':
        return cls(ip_access_list=_from_dict(d, 'ip_access_list', IpAccessListInfo))


@dataclass
class GetAccountIpAccessListRequest:
    """Get IP access list"""

    ip_access_list_id: str


@dataclass
class GetIpAccessListRequest:
    """Get access list"""

    ip_access_list_id: str


@dataclass
class GetIpAccessListResponse:
    ip_access_lists: 'List[IpAccessListInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.ip_access_lists: body['ip_access_lists'] = [v.as_dict() for v in self.ip_access_lists]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetIpAccessListResponse':
        return cls(ip_access_lists=_repeated(d, 'ip_access_lists', IpAccessListInfo))


@dataclass
class GetIpAccessListsResponse:
    ip_access_lists: 'List[IpAccessListInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.ip_access_lists: body['ip_access_lists'] = [v.as_dict() for v in self.ip_access_lists]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetIpAccessListsResponse':
        return cls(ip_access_lists=_repeated(d, 'ip_access_lists', IpAccessListInfo))


@dataclass
class GetStatusRequest:
    """Check configuration status"""

    keys: str


@dataclass
class GetTokenManagementRequest:
    """Get token info"""

    token_id: str


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

    def as_dict(self) -> dict:
        body = {}
        if self.address_count is not None: body['address_count'] = self.address_count
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.ip_addresses: body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label is not None: body['label'] = self.label
        if self.list_id is not None: body['list_id'] = self.list_id
        if self.list_type is not None: body['list_type'] = self.list_type.value
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'IpAccessListInfo':
        return cls(address_count=d.get('address_count', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   enabled=d.get('enabled', None),
                   ip_addresses=d.get('ip_addresses', None),
                   label=d.get('label', None),
                   list_id=d.get('list_id', None),
                   list_type=_enum(d, 'list_type', ListType),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


@dataclass
class ListTokenManagementRequest:
    """List all tokens"""

    created_by_id: str = None
    created_by_username: str = None


@dataclass
class ListTokensResponse:
    token_infos: 'List[TokenInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.token_infos: body['token_infos'] = [v.as_dict() for v in self.token_infos]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListTokensResponse':
        return cls(token_infos=_repeated(d, 'token_infos', TokenInfo))


class ListType(Enum):
    """This describes an enum"""

    ALLOW = 'ALLOW'
    BLOCK = 'BLOCK'


@dataclass
class PersonalComputeMessage:
    value: 'PersonalComputeMessageEnum'

    def as_dict(self) -> dict:
        body = {}
        if self.value is not None: body['value'] = self.value.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PersonalComputeMessage':
        return cls(value=_enum(d, 'value', PersonalComputeMessageEnum))


class PersonalComputeMessageEnum(Enum):
    """TBD"""

    DELEGATE = 'DELEGATE'
    ON = 'ON'


@dataclass
class PublicTokenInfo:
    comment: str = None
    creation_time: int = None
    expiry_time: int = None
    token_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.expiry_time is not None: body['expiry_time'] = self.expiry_time
        if self.token_id is not None: body['token_id'] = self.token_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PublicTokenInfo':
        return cls(comment=d.get('comment', None),
                   creation_time=d.get('creation_time', None),
                   expiry_time=d.get('expiry_time', None),
                   token_id=d.get('token_id', None))


@dataclass
class ReadPersonalComputeSettingRequest:
    """Get Personal Compute setting"""

    etag: str = None


@dataclass
class ReadPersonalComputeSettingResponse:
    setting_name: str
    personal_compute: 'PersonalComputeMessage'
    etag: str

    def as_dict(self) -> dict:
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        if self.personal_compute: body['personal_compute'] = self.personal_compute.as_dict()
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ReadPersonalComputeSettingResponse':
        return cls(etag=d.get('etag', None),
                   personal_compute=_from_dict(d, 'personal_compute', PersonalComputeMessage),
                   setting_name=d.get('setting_name', None))


@dataclass
class ReplaceIpAccessList:
    label: str
    list_type: 'ListType'
    ip_addresses: 'List[str]'
    enabled: bool
    ip_access_list_id: str = None
    list_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.ip_access_list_id is not None: body['ip_access_list_id'] = self.ip_access_list_id
        if self.ip_addresses: body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label is not None: body['label'] = self.label
        if self.list_id is not None: body['list_id'] = self.list_id
        if self.list_type is not None: body['list_type'] = self.list_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ReplaceIpAccessList':
        return cls(enabled=d.get('enabled', None),
                   ip_access_list_id=d.get('ip_access_list_id', None),
                   ip_addresses=d.get('ip_addresses', None),
                   label=d.get('label', None),
                   list_id=d.get('list_id', None),
                   list_type=_enum(d, 'list_type', ListType))


@dataclass
class RevokeTokenRequest:
    token_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.token_id is not None: body['token_id'] = self.token_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RevokeTokenRequest':
        return cls(token_id=d.get('token_id', None))


@dataclass
class TokenInfo:
    comment: str = None
    created_by_id: int = None
    created_by_username: str = None
    creation_time: int = None
    expiry_time: int = None
    owner_id: int = None
    token_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.created_by_id is not None: body['created_by_id'] = self.created_by_id
        if self.created_by_username is not None: body['created_by_username'] = self.created_by_username
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.expiry_time is not None: body['expiry_time'] = self.expiry_time
        if self.owner_id is not None: body['owner_id'] = self.owner_id
        if self.token_id is not None: body['token_id'] = self.token_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TokenInfo':
        return cls(comment=d.get('comment', None),
                   created_by_id=d.get('created_by_id', None),
                   created_by_username=d.get('created_by_username', None),
                   creation_time=d.get('creation_time', None),
                   expiry_time=d.get('expiry_time', None),
                   owner_id=d.get('owner_id', None),
                   token_id=d.get('token_id', None))


@dataclass
class UpdateIpAccessList:
    label: str
    list_type: 'ListType'
    ip_addresses: 'List[str]'
    enabled: bool
    ip_access_list_id: str = None
    list_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.ip_access_list_id is not None: body['ip_access_list_id'] = self.ip_access_list_id
        if self.ip_addresses: body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label is not None: body['label'] = self.label
        if self.list_id is not None: body['list_id'] = self.list_id
        if self.list_type is not None: body['list_type'] = self.list_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateIpAccessList':
        return cls(enabled=d.get('enabled', None),
                   ip_access_list_id=d.get('ip_access_list_id', None),
                   ip_addresses=d.get('ip_addresses', None),
                   label=d.get('label', None),
                   list_id=d.get('list_id', None),
                   list_type=_enum(d, 'list_type', ListType))


WorkspaceConf = Dict[str, str]


class AccountIpAccessListsAPI:
    """The Accounts IP Access List API enables account admins to configure IP access lists for access to the
    account console.
    
    Account IP Access Lists affect web application access and REST API access to the account console and
    account APIs. If the feature is disabled for the account, all access is allowed for this account. There is
    support for allow lists (inclusion) and block lists (exclusion).
    
    When a connection is attempted: 1. **First, all block lists are checked.** If the connection IP address
    matches any block list, the connection is rejected. 2. **If the connection was not rejected by block
    lists**, the IP address is compared with the allow lists.
    
    If there is at least one allow list for the account, the connection is allowed only if the IP address
    matches an allow list. If there are no allow lists for the account, all IP addresses are allowed.
    
    For all allow lists and block lists combined, the account supports a maximum of 1000 IP/CIDR values, where
    one CIDR counts as a single value.
    
    After changes to the account-level IP access lists, it can take a few minutes for changes to take effect."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, label: str, list_type: ListType, ip_addresses: List[str],
               **kwargs) -> CreateIpAccessListResponse:
        """Create access list.
        
        Creates an IP access list for the account.
        
        A list can be an allow list or a block list. See the top of this file for a description of how the
        server treats allow lists and block lists at runtime.
        
        When creating or updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the new list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateIpAccessList(ip_addresses=ip_addresses, label=label, list_type=list_type)
        body = request.as_dict()

        json = self._api.do('POST',
                            f'/api/2.0/preview/accounts/{self._api.account_id}/ip-access-lists',
                            body=body)
        return CreateIpAccessListResponse.from_dict(json)

    def delete(self, ip_access_list_id: str, **kwargs):
        """Delete access list.
        
        Deletes an IP access list, specified by its list ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteAccountIpAccessListRequest(ip_access_list_id=ip_access_list_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/preview/accounts/{self._api.account_id}/ip-access-lists/{request.ip_access_list_id}')

    def get(self, ip_access_list_id: str, **kwargs) -> GetIpAccessListResponse:
        """Get IP access list.
        
        Gets an IP access list, specified by its list ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAccountIpAccessListRequest(ip_access_list_id=ip_access_list_id)

        json = self._api.do(
            'GET',
            f'/api/2.0/preview/accounts/{self._api.account_id}/ip-access-lists/{request.ip_access_list_id}')
        return GetIpAccessListResponse.from_dict(json)

    def list(self) -> Iterator[IpAccessListInfo]:
        """Get access lists.
        
        Gets all IP access lists for the specified account."""

        json = self._api.do('GET', f'/api/2.0/preview/accounts/{self._api.account_id}/ip-access-lists')
        return [IpAccessListInfo.from_dict(v) for v in json.get('ip_access_lists', [])]

    def replace(self,
                label: str,
                list_type: ListType,
                ip_addresses: List[str],
                enabled: bool,
                ip_access_list_id: str,
                *,
                list_id: str = None,
                **kwargs):
        """Replace access list.
        
        Replaces an IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time. When replacing an IP access list: * For all
        allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values, where one
        CIDR counts as a single value. Attempts to exceed that number return error 400 with `error_code` value
        `QUOTA_EXCEEDED`. * If the resulting list would block the calling user's current IP, error 400 is
        returned with `error_code` value `INVALID_STATE`. It can take a few minutes for the changes to take
        effect."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ReplaceIpAccessList(enabled=enabled,
                                          ip_access_list_id=ip_access_list_id,
                                          ip_addresses=ip_addresses,
                                          label=label,
                                          list_id=list_id,
                                          list_type=list_type)
        body = request.as_dict()
        self._api.do(
            'PUT',
            f'/api/2.0/preview/accounts/{self._api.account_id}/ip-access-lists/{request.ip_access_list_id}',
            body=body)

    def update(self,
               label: str,
               list_type: ListType,
               ip_addresses: List[str],
               enabled: bool,
               ip_access_list_id: str,
               *,
               list_id: str = None,
               **kwargs):
        """Update access list.
        
        Updates an existing IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time.
        
        When updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the updated list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateIpAccessList(enabled=enabled,
                                         ip_access_list_id=ip_access_list_id,
                                         ip_addresses=ip_addresses,
                                         label=label,
                                         list_id=list_id,
                                         list_type=list_type)
        body = request.as_dict()
        self._api.do(
            'PATCH',
            f'/api/2.0/preview/accounts/{self._api.account_id}/ip-access-lists/{request.ip_access_list_id}',
            body=body)


class AccountSettingsAPI:
    """TBD"""

    def __init__(self, api_client):
        self._api = api_client

    def read_personal_compute_setting(self,
                                      *,
                                      etag: str = None,
                                      **kwargs) -> ReadPersonalComputeSettingResponse:
        """Get Personal Compute setting.
        
        TBD"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ReadPersonalComputeSettingRequest(etag=etag)

        query = {}
        if etag: query['etag'] = request.etag

        json = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/dcp_acct_enable/names/default',
            query=query)
        return ReadPersonalComputeSettingResponse.from_dict(json)


class IpAccessListsAPI:
    """IP Access List enables admins to configure IP access lists.
    
    IP access lists affect web application access and REST API access to this workspace only. If the feature
    is disabled for a workspace, all access is allowed for this workspace. There is support for allow lists
    (inclusion) and block lists (exclusion).
    
    When a connection is attempted: 1. **First, all block lists are checked.** If the connection IP address
    matches any block list, the connection is rejected. 2. **If the connection was not rejected by block
    lists**, the IP address is compared with the allow lists.
    
    If there is at least one allow list for the workspace, the connection is allowed only if the IP address
    matches an allow list. If there are no allow lists for the workspace, all IP addresses are allowed.
    
    For all allow lists and block lists combined, the workspace supports a maximum of 1000 IP/CIDR values,
    where one CIDR counts as a single value.
    
    After changes to the IP access list feature, it can take a few minutes for changes to take effect."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, label: str, list_type: ListType, ip_addresses: List[str],
               **kwargs) -> CreateIpAccessListResponse:
        """Create access list.
        
        Creates an IP access list for this workspace.
        
        A list can be an allow list or a block list. See the top of this file for a description of how the
        server treats allow lists and block lists at runtime.
        
        When creating or updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the new list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect. **Note**: Your new IP access list has no
        effect until you enable the feature. See :method:workspaceconf/setStatus"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateIpAccessList(ip_addresses=ip_addresses, label=label, list_type=list_type)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/ip-access-lists', body=body)
        return CreateIpAccessListResponse.from_dict(json)

    def delete(self, ip_access_list_id: str, **kwargs):
        """Delete access list.
        
        Deletes an IP access list, specified by its list ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteIpAccessListRequest(ip_access_list_id=ip_access_list_id)

        self._api.do('DELETE', f'/api/2.0/ip-access-lists/{request.ip_access_list_id}')

    def get(self, ip_access_list_id: str, **kwargs) -> FetchIpAccessListResponse:
        """Get access list.
        
        Gets an IP access list, specified by its list ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetIpAccessListRequest(ip_access_list_id=ip_access_list_id)

        json = self._api.do('GET', f'/api/2.0/ip-access-lists/{request.ip_access_list_id}')
        return FetchIpAccessListResponse.from_dict(json)

    def list(self) -> Iterator[IpAccessListInfo]:
        """Get access lists.
        
        Gets all IP access lists for the specified workspace."""

        json = self._api.do('GET', '/api/2.0/ip-access-lists')
        return [IpAccessListInfo.from_dict(v) for v in json.get('ip_access_lists', [])]

    def replace(self,
                label: str,
                list_type: ListType,
                ip_addresses: List[str],
                enabled: bool,
                ip_access_list_id: str,
                *,
                list_id: str = None,
                **kwargs):
        """Replace access list.
        
        Replaces an IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time. When replacing an IP access list: * For all
        allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values, where one
        CIDR counts as a single value. Attempts to exceed that number return error 400 with `error_code` value
        `QUOTA_EXCEEDED`. * If the resulting list would block the calling user's current IP, error 400 is
        returned with `error_code` value `INVALID_STATE`. It can take a few minutes for the changes to take
        effect. Note that your resulting IP access list has no effect until you enable the feature. See
        :method:workspaceconf/setStatus."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ReplaceIpAccessList(enabled=enabled,
                                          ip_access_list_id=ip_access_list_id,
                                          ip_addresses=ip_addresses,
                                          label=label,
                                          list_id=list_id,
                                          list_type=list_type)
        body = request.as_dict()
        self._api.do('PUT', f'/api/2.0/ip-access-lists/{request.ip_access_list_id}', body=body)

    def update(self,
               label: str,
               list_type: ListType,
               ip_addresses: List[str],
               enabled: bool,
               ip_access_list_id: str,
               *,
               list_id: str = None,
               **kwargs):
        """Update access list.
        
        Updates an existing IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time.
        
        When updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the updated list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect. Note that your resulting IP access list has
        no effect until you enable the feature. See :method:workspaceconf/setStatus."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateIpAccessList(enabled=enabled,
                                         ip_access_list_id=ip_access_list_id,
                                         ip_addresses=ip_addresses,
                                         label=label,
                                         list_id=list_id,
                                         list_type=list_type)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.0/ip-access-lists/{request.ip_access_list_id}', body=body)


class TokenManagementAPI:
    """Enables administrators to get all tokens and delete tokens for other users. Admins can either get every
    token, get a specific token by ID, or get all tokens for a particular user."""

    def __init__(self, api_client):
        self._api = api_client

    def create_obo_token(self,
                         application_id: str,
                         lifetime_seconds: int,
                         *,
                         comment: str = None,
                         **kwargs) -> CreateOboTokenResponse:
        """Create on-behalf token.
        
        Creates a token on behalf of a service principal."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateOboTokenRequest(application_id=application_id,
                                            comment=comment,
                                            lifetime_seconds=lifetime_seconds)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/token-management/on-behalf-of/tokens', body=body)
        return CreateOboTokenResponse.from_dict(json)

    def delete(self, token_id: str, **kwargs):
        """Delete a token.
        
        Deletes a token, specified by its ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteTokenManagementRequest(token_id=token_id)

        self._api.do('DELETE', f'/api/2.0/token-management/tokens/{request.token_id}')

    def get(self, token_id: str, **kwargs) -> TokenInfo:
        """Get token info.
        
        Gets information about a token, specified by its ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetTokenManagementRequest(token_id=token_id)

        json = self._api.do('GET', f'/api/2.0/token-management/tokens/{request.token_id}')
        return TokenInfo.from_dict(json)

    def list(self,
             *,
             created_by_id: str = None,
             created_by_username: str = None,
             **kwargs) -> Iterator[TokenInfo]:
        """List all tokens.
        
        Lists all tokens associated with the specified workspace or user."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListTokenManagementRequest(created_by_id=created_by_id,
                                                 created_by_username=created_by_username)

        query = {}
        if created_by_id: query['created_by_id'] = request.created_by_id
        if created_by_username: query['created_by_username'] = request.created_by_username

        json = self._api.do('GET', '/api/2.0/token-management/tokens', query=query)
        return [TokenInfo.from_dict(v) for v in json.get('token_infos', [])]


class TokensAPI:
    """The Token API allows you to create, list, and revoke tokens that can be used to authenticate and access
    Databricks REST APIs."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, *, comment: str = None, lifetime_seconds: int = None, **kwargs) -> CreateTokenResponse:
        """Create a user token.
        
        Creates and returns a token for a user. If this call is made through token authentication, it creates
        a token with the same client ID as the authenticated token. If the user's token quota is exceeded,
        this call returns an error **QUOTA_EXCEEDED**."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateTokenRequest(comment=comment, lifetime_seconds=lifetime_seconds)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/token/create', body=body)
        return CreateTokenResponse.from_dict(json)

    def delete(self, token_id: str, **kwargs):
        """Revoke token.
        
        Revokes an access token.
        
        If a token with the specified ID is not valid, this call returns an error **RESOURCE_DOES_NOT_EXIST**."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RevokeTokenRequest(token_id=token_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/token/delete', body=body)

    def list(self) -> Iterator[TokenInfo]:
        """List tokens.
        
        Lists all the valid tokens for a user-workspace pair."""

        json = self._api.do('GET', '/api/2.0/token/list')
        return [TokenInfo.from_dict(v) for v in json.get('token_infos', [])]


class WorkspaceConfAPI:
    """This API allows updating known workspace settings for advanced users."""

    def __init__(self, api_client):
        self._api = api_client

    def get_status(self, keys: str, **kwargs) -> WorkspaceConf:
        """Check configuration status.
        
        Gets the configuration status for a workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetStatusRequest(keys=keys)

        query = {}
        if keys: query['keys'] = request.keys

        json = self._api.do('GET', '/api/2.0/workspace-conf', query=query)
        return WorkspaceConf.from_dict(json)

    def set_status(self, **kwargs):
        """Enable/disable features.
        
        Sets the configuration status for a workspace, including enabling or disabling it."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Dict[str, str]()

        self._api.do('PATCH', '/api/2.0/workspace-conf')

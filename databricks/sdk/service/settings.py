# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AccountNetworkPolicyMessage:
    serverless_internet_access_enabled: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.serverless_internet_access_enabled is not None:
            body['serverless_internet_access_enabled'] = self.serverless_internet_access_enabled
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AccountNetworkPolicyMessage':
        return cls(serverless_internet_access_enabled=d.get('serverless_internet_access_enabled', None))


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
    ip_access_list: Optional['IpAccessListInfo'] = None

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
    comment: Optional[str] = None

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
    token_info: Optional['TokenInfo'] = None
    token_value: Optional[str] = None

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
    comment: Optional[str] = None
    lifetime_seconds: Optional[int] = None

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
    token_info: Optional['PublicTokenInfo'] = None
    token_value: Optional[str] = None

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
class DeleteAccountNetworkPolicyResponse:
    etag: str

    def as_dict(self) -> dict:
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteAccountNetworkPolicyResponse':
        return cls(etag=d.get('etag', None))


@dataclass
class DeletePersonalComputeSettingResponse:
    etag: str

    def as_dict(self) -> dict:
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeletePersonalComputeSettingResponse':
        return cls(etag=d.get('etag', None))


@dataclass
class FetchIpAccessListResponse:
    ip_access_list: Optional['IpAccessListInfo'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FetchIpAccessListResponse':
        return cls(ip_access_list=_from_dict(d, 'ip_access_list', IpAccessListInfo))


@dataclass
class GetIpAccessListResponse:
    ip_access_lists: Optional['List[IpAccessListInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.ip_access_lists: body['ip_access_lists'] = [v.as_dict() for v in self.ip_access_lists]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetIpAccessListResponse':
        return cls(ip_access_lists=_repeated(d, 'ip_access_lists', IpAccessListInfo))


@dataclass
class GetIpAccessListsResponse:
    ip_access_lists: Optional['List[IpAccessListInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.ip_access_lists: body['ip_access_lists'] = [v.as_dict() for v in self.ip_access_lists]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetIpAccessListsResponse':
        return cls(ip_access_lists=_repeated(d, 'ip_access_lists', IpAccessListInfo))


@dataclass
class GetTokenPermissionLevelsResponse:
    permission_levels: Optional['List[TokenPermissionsDescription]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetTokenPermissionLevelsResponse':
        return cls(permission_levels=_repeated(d, 'permission_levels', TokenPermissionsDescription))


@dataclass
class IpAccessListInfo:
    address_count: Optional[int] = None
    created_at: Optional[int] = None
    created_by: Optional[int] = None
    enabled: Optional[bool] = None
    ip_addresses: Optional['List[str]'] = None
    label: Optional[str] = None
    list_id: Optional[str] = None
    list_type: Optional['ListType'] = None
    updated_at: Optional[int] = None
    updated_by: Optional[int] = None

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
class ListTokensResponse:
    token_infos: Optional['List[TokenInfo]'] = None

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
    """ON: Grants all users in all workspaces access to the Personal Compute default policy, allowing
    all users to create single-machine compute resources. DELEGATE: Moves access control for the
    Personal Compute default policy to individual workspaces and requires a workspace’s users or
    groups to be added to the ACLs of that workspace’s Personal Compute default policy before they
    will be able to create compute resources through that policy."""

    DELEGATE = 'DELEGATE'
    ON = 'ON'


@dataclass
class PersonalComputeSetting:
    personal_compute: 'PersonalComputeMessage'
    etag: Optional[str] = None
    setting_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        if self.personal_compute: body['personal_compute'] = self.personal_compute.as_dict()
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PersonalComputeSetting':
        return cls(etag=d.get('etag', None),
                   personal_compute=_from_dict(d, 'personal_compute', PersonalComputeMessage),
                   setting_name=d.get('setting_name', None))


@dataclass
class PublicTokenInfo:
    comment: Optional[str] = None
    creation_time: Optional[int] = None
    expiry_time: Optional[int] = None
    token_id: Optional[str] = None

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
class ReplaceIpAccessList:
    label: str
    list_type: 'ListType'
    ip_addresses: 'List[str]'
    enabled: bool
    ip_access_list_id: Optional[str] = None
    list_id: Optional[str] = None

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
class TokenAccessControlRequest:
    group_name: Optional[str] = None
    permission_level: Optional['TokenPermissionLevel'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'TokenAccessControlRequest':
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', TokenPermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class TokenAccessControlResponse:
    all_permissions: Optional['List[TokenPermission]'] = None
    display_name: Optional[str] = None
    group_name: Optional[str] = None
    service_principal_name: Optional[str] = None
    user_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.all_permissions: body['all_permissions'] = [v.as_dict() for v in self.all_permissions]
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TokenAccessControlResponse':
        return cls(all_permissions=_repeated(d, 'all_permissions', TokenPermission),
                   display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class TokenInfo:
    comment: Optional[str] = None
    created_by_id: Optional[int] = None
    created_by_username: Optional[str] = None
    creation_time: Optional[int] = None
    expiry_time: Optional[int] = None
    owner_id: Optional[int] = None
    token_id: Optional[str] = None

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
class TokenPermission:
    inherited: Optional[bool] = None
    inherited_from_object: Optional['List[str]'] = None
    permission_level: Optional['TokenPermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TokenPermission':
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', TokenPermissionLevel))


class TokenPermissionLevel(Enum):
    """Permission level"""

    CAN_USE = 'CAN_USE'


@dataclass
class TokenPermissions:
    access_control_list: Optional['List[TokenAccessControlResponse]'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'TokenPermissions':
        return cls(access_control_list=_repeated(d, 'access_control_list', TokenAccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class TokenPermissionsDescription:
    description: Optional[str] = None
    permission_level: Optional['TokenPermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TokenPermissionsDescription':
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', TokenPermissionLevel))


@dataclass
class TokenPermissionsRequest:
    access_control_list: Optional['List[TokenAccessControlRequest]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TokenPermissionsRequest':
        return cls(access_control_list=_repeated(d, 'access_control_list', TokenAccessControlRequest))


@dataclass
class UpdateIpAccessList:
    label: str
    list_type: 'ListType'
    ip_addresses: 'List[str]'
    enabled: bool
    ip_access_list_id: Optional[str] = None
    list_id: Optional[str] = None

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

    def create(self, label: str, list_type: ListType, ip_addresses: List[str]) -> CreateIpAccessListResponse:
        """Create access list.
        
        Creates an IP access list for the account.
        
        A list can be an allow list or a block list. See the top of this file for a description of how the
        server treats allow lists and block lists at runtime.
        
        When creating or updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the new list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect.
        
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          This describes an enum
        :param ip_addresses: List[str]
          Array of IP addresses or CIDR values to be added to the IP access list.
        
        :returns: :class:`CreateIpAccessListResponse`
        """
        body = {}
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST',
                           f'/api/2.0/preview/accounts/{self._api.account_id}/ip-access-lists',
                           body=body,
                           headers=headers)
        return CreateIpAccessListResponse.from_dict(res)

    def delete(self, ip_access_list_id: str):
        """Delete access list.
        
        Deletes an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list.
        
        
        """

        headers = {}
        self._api.do('DELETE',
                     f'/api/2.0/preview/accounts/{self._api.account_id}/ip-access-lists/{ip_access_list_id}',
                     headers=headers)

    def get(self, ip_access_list_id: str) -> GetIpAccessListResponse:
        """Get IP access list.
        
        Gets an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list.
        
        :returns: :class:`GetIpAccessListResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do(
            'GET',
            f'/api/2.0/preview/accounts/{self._api.account_id}/ip-access-lists/{ip_access_list_id}',
            headers=headers)
        return GetIpAccessListResponse.from_dict(res)

    def list(self) -> Iterator[IpAccessListInfo]:
        """Get access lists.
        
        Gets all IP access lists for the specified account.
        
        :returns: Iterator over :class:`IpAccessListInfo`
        """

        headers = {'Accept': 'application/json', }
        json = self._api.do('GET',
                            f'/api/2.0/preview/accounts/{self._api.account_id}/ip-access-lists',
                            headers=headers)
        return [IpAccessListInfo.from_dict(v) for v in json.get('ip_access_lists', [])]

    def replace(self,
                label: str,
                list_type: ListType,
                ip_addresses: List[str],
                enabled: bool,
                ip_access_list_id: str,
                *,
                list_id: Optional[str] = None):
        """Replace access list.
        
        Replaces an IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time. When replacing an IP access list: * For all
        allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values, where one
        CIDR counts as a single value. Attempts to exceed that number return error 400 with `error_code` value
        `QUOTA_EXCEEDED`. * If the resulting list would block the calling user's current IP, error 400 is
        returned with `error_code` value `INVALID_STATE`. It can take a few minutes for the changes to take
        effect.
        
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          This describes an enum
        :param ip_addresses: List[str]
          Array of IP addresses or CIDR values to be added to the IP access list.
        :param enabled: bool
          Specifies whether this IP access list is enabled.
        :param ip_access_list_id: str
          The ID for the corresponding IP access list.
        :param list_id: str (optional)
          Universally unique identifier (UUID) of the IP access list.
        
        
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_id is not None: body['list_id'] = list_id
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PUT',
                     f'/api/2.0/preview/accounts/{self._api.account_id}/ip-access-lists/{ip_access_list_id}',
                     body=body,
                     headers=headers)

    def update(self,
               label: str,
               list_type: ListType,
               ip_addresses: List[str],
               enabled: bool,
               ip_access_list_id: str,
               *,
               list_id: Optional[str] = None):
        """Update access list.
        
        Updates an existing IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time.
        
        When updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the updated list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect.
        
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          This describes an enum
        :param ip_addresses: List[str]
          Array of IP addresses or CIDR values to be added to the IP access list.
        :param enabled: bool
          Specifies whether this IP access list is enabled.
        :param ip_access_list_id: str
          The ID for the corresponding IP access list.
        :param list_id: str (optional)
          Universally unique identifier (UUID) of the IP access list.
        
        
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_id is not None: body['list_id'] = list_id
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PATCH',
                     f'/api/2.0/preview/accounts/{self._api.account_id}/ip-access-lists/{ip_access_list_id}',
                     body=body,
                     headers=headers)


class AccountNetworkPolicyAPI:
    """Network policy is a set of rules that defines what can be accessed from your Databricks network. E.g.: You
    can choose to block your SQL UDF to access internet from your Databricks serverless clusters.
    
    There is only one instance of this setting per account. Since this setting has a default value, this
    setting is present on all accounts even though it's never set on a given account. Deletion reverts the
    value of the setting back to the default value."""

    def __init__(self, api_client):
        self._api = api_client

    def delete_account_network_policy(self, etag: str) -> DeleteAccountNetworkPolicyResponse:
        """Delete Account Network Policy.
        
        Reverts back all the account network policies back to default.
        
        :param etag: str
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteAccountNetworkPolicyResponse`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }
        res = self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/network_policy/names/default',
            query=query,
            headers=headers)
        return DeleteAccountNetworkPolicyResponse.from_dict(res)

    def read_account_network_policy(self, etag: str) -> AccountNetworkPolicyMessage:
        """Get Account Network Policy.
        
        Gets the value of Account level Network Policy.
        
        :param etag: str
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`AccountNetworkPolicyMessage`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }
        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/network_policy/names/default',
            query=query,
            headers=headers)
        return AccountNetworkPolicyMessage.from_dict(res)

    def update_account_network_policy(
            self,
            *,
            allow_missing: Optional[bool] = None,
            setting: Optional[AccountNetworkPolicyMessage] = None) -> AccountNetworkPolicyMessage:
        """Update Account Network Policy.
        
        Updates the policy content of Account level Network Policy.
        
        :param allow_missing: bool (optional)
          This should always be set to true for Settings RPCs. Added for AIP compliance.
        :param setting: :class:`AccountNetworkPolicyMessage` (optional)
        
        :returns: :class:`AccountNetworkPolicyMessage`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do(
            'PATCH',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/network_policy/names/default',
            body=body,
            headers=headers)
        return AccountNetworkPolicyMessage.from_dict(res)


class AccountSettingsAPI:
    """The Personal Compute enablement setting lets you control which users can use the Personal Compute default
    policy to create compute resources. By default all users in all workspaces have access (ON), but you can
    change the setting to instead let individual workspaces configure access control (DELEGATE).
    
    There is only one instance of this setting per account. Since this setting has a default value, this
    setting is present on all accounts even though it's never set on a given account. Deletion reverts the
    value of the setting back to the default value."""

    def __init__(self, api_client):
        self._api = api_client

    def delete_personal_compute_setting(self, etag: str) -> DeletePersonalComputeSettingResponse:
        """Delete Personal Compute setting.
        
        Reverts back the Personal Compute setting value to default (ON)
        
        :param etag: str
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeletePersonalComputeSettingResponse`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }
        res = self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/dcp_acct_enable/names/default',
            query=query,
            headers=headers)
        return DeletePersonalComputeSettingResponse.from_dict(res)

    def read_personal_compute_setting(self, etag: str) -> PersonalComputeSetting:
        """Get Personal Compute setting.
        
        Gets the value of the Personal Compute setting.
        
        :param etag: str
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`PersonalComputeSetting`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }
        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/dcp_acct_enable/names/default',
            query=query,
            headers=headers)
        return PersonalComputeSetting.from_dict(res)

    def update_personal_compute_setting(
            self,
            *,
            allow_missing: Optional[bool] = None,
            setting: Optional[PersonalComputeSetting] = None) -> PersonalComputeSetting:
        """Update Personal Compute setting.
        
        Updates the value of the Personal Compute setting.
        
        :param allow_missing: bool (optional)
          This should always be set to true for Settings RPCs. Added for AIP compliance.
        :param setting: :class:`PersonalComputeSetting` (optional)
        
        :returns: :class:`PersonalComputeSetting`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do(
            'PATCH',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/dcp_acct_enable/names/default',
            body=body,
            headers=headers)
        return PersonalComputeSetting.from_dict(res)


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

    def create(self, label: str, list_type: ListType, ip_addresses: List[str]) -> CreateIpAccessListResponse:
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
        effect until you enable the feature. See :method:workspaceconf/setStatus
        
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          This describes an enum
        :param ip_addresses: List[str]
          Array of IP addresses or CIDR values to be added to the IP access list.
        
        :returns: :class:`CreateIpAccessListResponse`
        """
        body = {}
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/ip-access-lists', body=body, headers=headers)
        return CreateIpAccessListResponse.from_dict(res)

    def delete(self, ip_access_list_id: str):
        """Delete access list.
        
        Deletes an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list to modify.
        
        
        """

        headers = {}
        self._api.do('DELETE', f'/api/2.0/ip-access-lists/{ip_access_list_id}', headers=headers)

    def get(self, ip_access_list_id: str) -> FetchIpAccessListResponse:
        """Get access list.
        
        Gets an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list to modify.
        
        :returns: :class:`FetchIpAccessListResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/ip-access-lists/{ip_access_list_id}', headers=headers)
        return FetchIpAccessListResponse.from_dict(res)

    def list(self) -> Iterator[IpAccessListInfo]:
        """Get access lists.
        
        Gets all IP access lists for the specified workspace.
        
        :returns: Iterator over :class:`IpAccessListInfo`
        """

        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/ip-access-lists', headers=headers)
        return [IpAccessListInfo.from_dict(v) for v in json.get('ip_access_lists', [])]

    def replace(self,
                label: str,
                list_type: ListType,
                ip_addresses: List[str],
                enabled: bool,
                ip_access_list_id: str,
                *,
                list_id: Optional[str] = None):
        """Replace access list.
        
        Replaces an IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time. When replacing an IP access list: * For all
        allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values, where one
        CIDR counts as a single value. Attempts to exceed that number return error 400 with `error_code` value
        `QUOTA_EXCEEDED`. * If the resulting list would block the calling user's current IP, error 400 is
        returned with `error_code` value `INVALID_STATE`. It can take a few minutes for the changes to take
        effect. Note that your resulting IP access list has no effect until you enable the feature. See
        :method:workspaceconf/setStatus.
        
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          This describes an enum
        :param ip_addresses: List[str]
          Array of IP addresses or CIDR values to be added to the IP access list.
        :param enabled: bool
          Specifies whether this IP access list is enabled.
        :param ip_access_list_id: str
          The ID for the corresponding IP access list to modify.
        :param list_id: str (optional)
          Universally unique identifier (UUID) of the IP access list.
        
        
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_id is not None: body['list_id'] = list_id
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PUT', f'/api/2.0/ip-access-lists/{ip_access_list_id}', body=body, headers=headers)

    def update(self,
               label: str,
               list_type: ListType,
               ip_addresses: List[str],
               enabled: bool,
               ip_access_list_id: str,
               *,
               list_id: Optional[str] = None):
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
        no effect until you enable the feature. See :method:workspaceconf/setStatus.
        
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          This describes an enum
        :param ip_addresses: List[str]
          Array of IP addresses or CIDR values to be added to the IP access list.
        :param enabled: bool
          Specifies whether this IP access list is enabled.
        :param ip_access_list_id: str
          The ID for the corresponding IP access list to modify.
        :param list_id: str (optional)
          Universally unique identifier (UUID) of the IP access list.
        
        
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_id is not None: body['list_id'] = list_id
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PATCH', f'/api/2.0/ip-access-lists/{ip_access_list_id}', body=body, headers=headers)


class TokenManagementAPI:
    """Enables administrators to get all tokens and delete tokens for other users. Admins can either get every
    token, get a specific token by ID, or get all tokens for a particular user."""

    def __init__(self, api_client):
        self._api = api_client

    def create_obo_token(self,
                         application_id: str,
                         lifetime_seconds: int,
                         *,
                         comment: Optional[str] = None) -> CreateOboTokenResponse:
        """Create on-behalf token.
        
        Creates a token on behalf of a service principal.
        
        :param application_id: str
          Application ID of the service principal.
        :param lifetime_seconds: int
          The number of seconds before the token expires.
        :param comment: str (optional)
          Comment that describes the purpose of the token.
        
        :returns: :class:`CreateOboTokenResponse`
        """
        body = {}
        if application_id is not None: body['application_id'] = application_id
        if comment is not None: body['comment'] = comment
        if lifetime_seconds is not None: body['lifetime_seconds'] = lifetime_seconds
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST',
                           '/api/2.0/token-management/on-behalf-of/tokens',
                           body=body,
                           headers=headers)
        return CreateOboTokenResponse.from_dict(res)

    def delete(self, token_id: str):
        """Delete a token.
        
        Deletes a token, specified by its ID.
        
        :param token_id: str
          The ID of the token to get.
        
        
        """

        headers = {}
        self._api.do('DELETE', f'/api/2.0/token-management/tokens/{token_id}', headers=headers)

    def get(self, token_id: str) -> TokenInfo:
        """Get token info.
        
        Gets information about a token, specified by its ID.
        
        :param token_id: str
          The ID of the token to get.
        
        :returns: :class:`TokenInfo`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/token-management/tokens/{token_id}', headers=headers)
        return TokenInfo.from_dict(res)

    def get_token_permission_levels(self) -> GetTokenPermissionLevelsResponse:
        """Get token permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :returns: :class:`GetTokenPermissionLevelsResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           '/api/2.0/permissions/authorization/tokens/permissionLevels',
                           headers=headers)
        return GetTokenPermissionLevelsResponse.from_dict(res)

    def get_token_permissions(self) -> TokenPermissions:
        """Get token permissions.
        
        Gets the permissions of all tokens. Tokens can inherit permissions from their root object.
        
        :returns: :class:`TokenPermissions`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/permissions/authorization/tokens', headers=headers)
        return TokenPermissions.from_dict(res)

    def list(self,
             *,
             created_by_id: Optional[str] = None,
             created_by_username: Optional[str] = None) -> Iterator[TokenInfo]:
        """List all tokens.
        
        Lists all tokens associated with the specified workspace or user.
        
        :param created_by_id: str (optional)
          User ID of the user that created the token.
        :param created_by_username: str (optional)
          Username of the user that created the token.
        
        :returns: Iterator over :class:`TokenInfo`
        """

        query = {}
        if created_by_id is not None: query['created_by_id'] = created_by_id
        if created_by_username is not None: query['created_by_username'] = created_by_username
        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/token-management/tokens', query=query, headers=headers)
        return [TokenInfo.from_dict(v) for v in json.get('token_infos', [])]

    def set_token_permissions(
            self,
            *,
            access_control_list: Optional[List[TokenAccessControlRequest]] = None) -> TokenPermissions:
        """Set token permissions.
        
        Sets permissions on all tokens. Tokens can inherit permissions from their root object.
        
        :param access_control_list: List[:class:`TokenAccessControlRequest`] (optional)
        
        :returns: :class:`TokenPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PUT', '/api/2.0/permissions/authorization/tokens', body=body, headers=headers)
        return TokenPermissions.from_dict(res)

    def update_token_permissions(
            self,
            *,
            access_control_list: Optional[List[TokenAccessControlRequest]] = None) -> TokenPermissions:
        """Update token permissions.
        
        Updates the permissions on all tokens. Tokens can inherit permissions from their root object.
        
        :param access_control_list: List[:class:`TokenAccessControlRequest`] (optional)
        
        :returns: :class:`TokenPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PATCH', '/api/2.0/permissions/authorization/tokens', body=body, headers=headers)
        return TokenPermissions.from_dict(res)


class TokensAPI:
    """The Token API allows you to create, list, and revoke tokens that can be used to authenticate and access
    Databricks REST APIs."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               comment: Optional[str] = None,
               lifetime_seconds: Optional[int] = None) -> CreateTokenResponse:
        """Create a user token.
        
        Creates and returns a token for a user. If this call is made through token authentication, it creates
        a token with the same client ID as the authenticated token. If the user's token quota is exceeded,
        this call returns an error **QUOTA_EXCEEDED**.
        
        :param comment: str (optional)
          Optional description to attach to the token.
        :param lifetime_seconds: int (optional)
          The lifetime of the token, in seconds.
          
          If the ifetime is not specified, this token remains valid indefinitely.
        
        :returns: :class:`CreateTokenResponse`
        """
        body = {}
        if comment is not None: body['comment'] = comment
        if lifetime_seconds is not None: body['lifetime_seconds'] = lifetime_seconds
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/token/create', body=body, headers=headers)
        return CreateTokenResponse.from_dict(res)

    def delete(self, token_id: str):
        """Revoke token.
        
        Revokes an access token.
        
        If a token with the specified ID is not valid, this call returns an error **RESOURCE_DOES_NOT_EXIST**.
        
        :param token_id: str
          The ID of the token to be revoked.
        
        
        """
        body = {}
        if token_id is not None: body['token_id'] = token_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/token/delete', body=body, headers=headers)

    def list(self) -> Iterator[TokenInfo]:
        """List tokens.
        
        Lists all the valid tokens for a user-workspace pair.
        
        :returns: Iterator over :class:`TokenInfo`
        """

        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/token/list', headers=headers)
        return [TokenInfo.from_dict(v) for v in json.get('token_infos', [])]


class WorkspaceConfAPI:
    """This API allows updating known workspace settings for advanced users."""

    def __init__(self, api_client):
        self._api = api_client

    def get_status(self, keys: str) -> WorkspaceConf:
        """Check configuration status.
        
        Gets the configuration status for a workspace.
        
        :param keys: str
        
        :returns: Dict[str,str]
        """

        query = {}
        if keys is not None: query['keys'] = keys
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/workspace-conf', query=query, headers=headers)
        return WorkspaceConf.from_dict(res)

    def set_status(self):
        """Enable/disable features.
        
        Sets the configuration status for a workspace, including enabling or disabling it.
        
        
        
        """

        headers = {'Content-Type': 'application/json', }
        self._api.do('PATCH', '/api/2.0/workspace-conf', headers=headers)

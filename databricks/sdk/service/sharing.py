# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List

from ._internal import _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

from .catalog import PermissionsChange, PermissionsList

# all definitions in this file are in alphabetical order


class AuthenticationType(Enum):
    """The delta sharing authentication type."""

    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'


@dataclass
class CreateProvider:
    name: str
    authentication_type: 'AuthenticationType'
    comment: str = None
    recipient_profile_str: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.authentication_type is not None: body['authentication_type'] = self.authentication_type.value
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        if self.recipient_profile_str is not None: body['recipient_profile_str'] = self.recipient_profile_str
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateProvider':
        return cls(authentication_type=_enum(d, 'authentication_type', AuthenticationType),
                   comment=d.get('comment', None),
                   name=d.get('name', None),
                   recipient_profile_str=d.get('recipient_profile_str', None))


@dataclass
class CreateRecipient:
    name: str
    authentication_type: 'AuthenticationType'
    comment: str = None
    data_recipient_global_metastore_id: Any = None
    ip_access_list: 'IpAccessList' = None
    owner: str = None
    properties_kvpairs: 'SecurablePropertiesKvPairs' = None
    sharing_code: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.authentication_type is not None: body['authentication_type'] = self.authentication_type.value
        if self.comment is not None: body['comment'] = self.comment
        if self.data_recipient_global_metastore_id:
            body['data_recipient_global_metastore_id'] = self.data_recipient_global_metastore_id
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.properties_kvpairs: body['properties_kvpairs'] = self.properties_kvpairs.as_dict()
        if self.sharing_code is not None: body['sharing_code'] = self.sharing_code
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRecipient':
        return cls(authentication_type=_enum(d, 'authentication_type', AuthenticationType),
                   comment=d.get('comment', None),
                   data_recipient_global_metastore_id=d.get('data_recipient_global_metastore_id', None),
                   ip_access_list=_from_dict(d, 'ip_access_list', IpAccessList),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   properties_kvpairs=_from_dict(d, 'properties_kvpairs', SecurablePropertiesKvPairs),
                   sharing_code=d.get('sharing_code', None))


@dataclass
class CreateShare:
    name: str
    comment: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateShare':
        return cls(comment=d.get('comment', None), name=d.get('name', None))


@dataclass
class DeleteProviderRequest:
    """Delete a provider"""

    name: str


@dataclass
class DeleteRecipientRequest:
    """Delete a share recipient"""

    name: str


@dataclass
class DeleteShareRequest:
    """Delete a share"""

    name: str


@dataclass
class GetActivationUrlInfoRequest:
    """Get a share activation URL"""

    activation_url: str


@dataclass
class GetProviderRequest:
    """Get a provider"""

    name: str


@dataclass
class GetRecipientRequest:
    """Get a share recipient"""

    name: str


@dataclass
class GetRecipientSharePermissionsResponse:
    permissions_out: 'List[ShareToPrivilegeAssignment]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.permissions_out: body['permissions_out'] = [v.as_dict() for v in self.permissions_out]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRecipientSharePermissionsResponse':
        return cls(permissions_out=_repeated(d, 'permissions_out', ShareToPrivilegeAssignment))


@dataclass
class GetShareRequest:
    """Get a share"""

    name: str
    include_shared_data: bool = None


@dataclass
class IpAccessList:
    allowed_ip_addresses: 'List[str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.allowed_ip_addresses: body['allowed_ip_addresses'] = [v for v in self.allowed_ip_addresses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'IpAccessList':
        return cls(allowed_ip_addresses=d.get('allowed_ip_addresses', None))


@dataclass
class ListProviderSharesResponse:
    shares: 'List[ProviderShare]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.shares: body['shares'] = [v.as_dict() for v in self.shares]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListProviderSharesResponse':
        return cls(shares=_repeated(d, 'shares', ProviderShare))


@dataclass
class ListProvidersRequest:
    """List providers"""

    data_provider_global_metastore_id: str = None


@dataclass
class ListProvidersResponse:
    providers: 'List[ProviderInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.providers: body['providers'] = [v.as_dict() for v in self.providers]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListProvidersResponse':
        return cls(providers=_repeated(d, 'providers', ProviderInfo))


@dataclass
class ListRecipientsRequest:
    """List share recipients"""

    data_recipient_global_metastore_id: str = None


@dataclass
class ListRecipientsResponse:
    recipients: 'List[RecipientInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.recipients: body['recipients'] = [v.as_dict() for v in self.recipients]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRecipientsResponse':
        return cls(recipients=_repeated(d, 'recipients', RecipientInfo))


@dataclass
class ListSharesRequest:
    """List shares by Provider"""

    name: str


@dataclass
class ListSharesResponse:
    shares: 'List[ShareInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.shares: body['shares'] = [v.as_dict() for v in self.shares]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListSharesResponse':
        return cls(shares=_repeated(d, 'shares', ShareInfo))


@dataclass
class Partition:
    values: 'List[PartitionValue]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.values: body['values'] = [v.as_dict() for v in self.values]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Partition':
        return cls(values=_repeated(d, 'values', PartitionValue))


@dataclass
class PartitionValue:
    name: str = None
    op: 'PartitionValueOp' = None
    recipient_property_key: str = None
    value: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.op is not None: body['op'] = self.op.value
        if self.recipient_property_key is not None:
            body['recipient_property_key'] = self.recipient_property_key
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PartitionValue':
        return cls(name=d.get('name', None),
                   op=_enum(d, 'op', PartitionValueOp),
                   recipient_property_key=d.get('recipient_property_key', None),
                   value=d.get('value', None))


class PartitionValueOp(Enum):
    """The operator to apply for the value."""

    EQUAL = 'EQUAL'
    LIKE = 'LIKE'


class Privilege(Enum):

    ALL_PRIVILEGES = 'ALL_PRIVILEGES'
    CREATE = 'CREATE'
    CREATE_CATALOG = 'CREATE_CATALOG'
    CREATE_EXTERNAL_LOCATION = 'CREATE_EXTERNAL_LOCATION'
    CREATE_EXTERNAL_TABLE = 'CREATE_EXTERNAL_TABLE'
    CREATE_FUNCTION = 'CREATE_FUNCTION'
    CREATE_MANAGED_STORAGE = 'CREATE_MANAGED_STORAGE'
    CREATE_MATERIALIZED_VIEW = 'CREATE_MATERIALIZED_VIEW'
    CREATE_PROVIDER = 'CREATE_PROVIDER'
    CREATE_RECIPIENT = 'CREATE_RECIPIENT'
    CREATE_SCHEMA = 'CREATE_SCHEMA'
    CREATE_SHARE = 'CREATE_SHARE'
    CREATE_STORAGE_CREDENTIAL = 'CREATE_STORAGE_CREDENTIAL'
    CREATE_TABLE = 'CREATE_TABLE'
    CREATE_VIEW = 'CREATE_VIEW'
    EXECUTE = 'EXECUTE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    READ_PRIVATE_FILES = 'READ_PRIVATE_FILES'
    REFRESH = 'REFRESH'
    SELECT = 'SELECT'
    SET_SHARE_PERMISSION = 'SET_SHARE_PERMISSION'
    USAGE = 'USAGE'
    USE_CATALOG = 'USE_CATALOG'
    USE_PROVIDER = 'USE_PROVIDER'
    USE_RECIPIENT = 'USE_RECIPIENT'
    USE_SCHEMA = 'USE_SCHEMA'
    USE_SHARE = 'USE_SHARE'
    WRITE_FILES = 'WRITE_FILES'
    WRITE_PRIVATE_FILES = 'WRITE_PRIVATE_FILES'


@dataclass
class PrivilegeAssignment:
    principal: str = None
    privileges: 'List[Privilege]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.principal is not None: body['principal'] = self.principal
        if self.privileges: body['privileges'] = [v for v in self.privileges]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PrivilegeAssignment':
        return cls(principal=d.get('principal', None), privileges=d.get('privileges', None))


@dataclass
class ProviderInfo:
    authentication_type: 'AuthenticationType' = None
    cloud: str = None
    comment: str = None
    created_at: int = None
    created_by: str = None
    data_provider_global_metastore_id: str = None
    metastore_id: str = None
    name: str = None
    owner: str = None
    recipient_profile: 'RecipientProfile' = None
    recipient_profile_str: str = None
    region: str = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.authentication_type is not None: body['authentication_type'] = self.authentication_type.value
        if self.cloud is not None: body['cloud'] = self.cloud
        if self.comment is not None: body['comment'] = self.comment
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.data_provider_global_metastore_id is not None:
            body['data_provider_global_metastore_id'] = self.data_provider_global_metastore_id
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.recipient_profile: body['recipient_profile'] = self.recipient_profile.as_dict()
        if self.recipient_profile_str is not None: body['recipient_profile_str'] = self.recipient_profile_str
        if self.region is not None: body['region'] = self.region
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ProviderInfo':
        return cls(authentication_type=_enum(d, 'authentication_type', AuthenticationType),
                   cloud=d.get('cloud', None),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   data_provider_global_metastore_id=d.get('data_provider_global_metastore_id', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   recipient_profile=_from_dict(d, 'recipient_profile', RecipientProfile),
                   recipient_profile_str=d.get('recipient_profile_str', None),
                   region=d.get('region', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


@dataclass
class ProviderShare:
    name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ProviderShare':
        return cls(name=d.get('name', None))


@dataclass
class RecipientInfo:
    activated: bool = None
    activation_url: str = None
    authentication_type: 'AuthenticationType' = None
    cloud: str = None
    comment: str = None
    created_at: int = None
    created_by: str = None
    data_recipient_global_metastore_id: Any = None
    ip_access_list: 'IpAccessList' = None
    metastore_id: str = None
    name: str = None
    owner: str = None
    properties_kvpairs: 'SecurablePropertiesKvPairs' = None
    region: str = None
    sharing_code: str = None
    tokens: 'List[RecipientTokenInfo]' = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.activated is not None: body['activated'] = self.activated
        if self.activation_url is not None: body['activation_url'] = self.activation_url
        if self.authentication_type is not None: body['authentication_type'] = self.authentication_type.value
        if self.cloud is not None: body['cloud'] = self.cloud
        if self.comment is not None: body['comment'] = self.comment
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.data_recipient_global_metastore_id:
            body['data_recipient_global_metastore_id'] = self.data_recipient_global_metastore_id
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.properties_kvpairs: body['properties_kvpairs'] = self.properties_kvpairs.as_dict()
        if self.region is not None: body['region'] = self.region
        if self.sharing_code is not None: body['sharing_code'] = self.sharing_code
        if self.tokens: body['tokens'] = [v.as_dict() for v in self.tokens]
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RecipientInfo':
        return cls(activated=d.get('activated', None),
                   activation_url=d.get('activation_url', None),
                   authentication_type=_enum(d, 'authentication_type', AuthenticationType),
                   cloud=d.get('cloud', None),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   data_recipient_global_metastore_id=d.get('data_recipient_global_metastore_id', None),
                   ip_access_list=_from_dict(d, 'ip_access_list', IpAccessList),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   properties_kvpairs=_from_dict(d, 'properties_kvpairs', SecurablePropertiesKvPairs),
                   region=d.get('region', None),
                   sharing_code=d.get('sharing_code', None),
                   tokens=_repeated(d, 'tokens', RecipientTokenInfo),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


@dataclass
class RecipientProfile:
    bearer_token: str = None
    endpoint: str = None
    share_credentials_version: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.bearer_token is not None: body['bearer_token'] = self.bearer_token
        if self.endpoint is not None: body['endpoint'] = self.endpoint
        if self.share_credentials_version is not None:
            body['share_credentials_version'] = self.share_credentials_version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RecipientProfile':
        return cls(bearer_token=d.get('bearer_token', None),
                   endpoint=d.get('endpoint', None),
                   share_credentials_version=d.get('share_credentials_version', None))


@dataclass
class RecipientTokenInfo:
    activation_url: str = None
    created_at: int = None
    created_by: str = None
    expiration_time: int = None
    id: str = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.activation_url is not None: body['activation_url'] = self.activation_url
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.expiration_time is not None: body['expiration_time'] = self.expiration_time
        if self.id is not None: body['id'] = self.id
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RecipientTokenInfo':
        return cls(activation_url=d.get('activation_url', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   expiration_time=d.get('expiration_time', None),
                   id=d.get('id', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


@dataclass
class RetrieveTokenRequest:
    """Get an access token"""

    activation_url: str


@dataclass
class RetrieveTokenResponse:
    bearer_token: str = None
    endpoint: str = None
    expiration_time: str = None
    share_credentials_version: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.bearer_token is not None: body['bearerToken'] = self.bearer_token
        if self.endpoint is not None: body['endpoint'] = self.endpoint
        if self.expiration_time is not None: body['expirationTime'] = self.expiration_time
        if self.share_credentials_version is not None:
            body['shareCredentialsVersion'] = self.share_credentials_version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RetrieveTokenResponse':
        return cls(bearer_token=d.get('bearerToken', None),
                   endpoint=d.get('endpoint', None),
                   expiration_time=d.get('expirationTime', None),
                   share_credentials_version=d.get('shareCredentialsVersion', None))


@dataclass
class RotateRecipientToken:
    existing_token_expire_in_seconds: int
    name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.existing_token_expire_in_seconds is not None:
            body['existing_token_expire_in_seconds'] = self.existing_token_expire_in_seconds
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RotateRecipientToken':
        return cls(existing_token_expire_in_seconds=d.get('existing_token_expire_in_seconds', None),
                   name=d.get('name', None))


@dataclass
class SecurablePropertiesKvPairs:
    """An object with __properties__ containing map of key-value properties attached to the securable."""

    properties: 'Dict[str,str]'

    def as_dict(self) -> dict:
        body = {}
        if self.properties: body['properties'] = self.properties
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SecurablePropertiesKvPairs':
        return cls(properties=d.get('properties', None))


SecurablePropertiesMap = Dict[str, str]


@dataclass
class ShareInfo:
    comment: str = None
    created_at: int = None
    created_by: str = None
    name: str = None
    objects: 'List[SharedDataObject]' = None
    owner: str = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.name is not None: body['name'] = self.name
        if self.objects: body['objects'] = [v.as_dict() for v in self.objects]
        if self.owner is not None: body['owner'] = self.owner
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ShareInfo':
        return cls(comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   name=d.get('name', None),
                   objects=_repeated(d, 'objects', SharedDataObject),
                   owner=d.get('owner', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


@dataclass
class SharePermissionsRequest:
    """Get recipient share permissions"""

    name: str


@dataclass
class ShareToPrivilegeAssignment:
    privilege_assignments: 'List[PrivilegeAssignment]' = None
    share_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.privilege_assignments:
            body['privilege_assignments'] = [v.as_dict() for v in self.privilege_assignments]
        if self.share_name is not None: body['share_name'] = self.share_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ShareToPrivilegeAssignment':
        return cls(privilege_assignments=_repeated(d, 'privilege_assignments', PrivilegeAssignment),
                   share_name=d.get('share_name', None))


@dataclass
class SharedDataObject:
    name: str
    added_at: int = None
    added_by: str = None
    cdf_enabled: bool = None
    comment: str = None
    data_object_type: str = None
    partitions: 'List[Partition]' = None
    shared_as: str = None
    start_version: int = None
    status: 'SharedDataObjectStatus' = None

    def as_dict(self) -> dict:
        body = {}
        if self.added_at is not None: body['added_at'] = self.added_at
        if self.added_by is not None: body['added_by'] = self.added_by
        if self.cdf_enabled is not None: body['cdf_enabled'] = self.cdf_enabled
        if self.comment is not None: body['comment'] = self.comment
        if self.data_object_type is not None: body['data_object_type'] = self.data_object_type
        if self.name is not None: body['name'] = self.name
        if self.partitions: body['partitions'] = [v.as_dict() for v in self.partitions]
        if self.shared_as is not None: body['shared_as'] = self.shared_as
        if self.start_version is not None: body['start_version'] = self.start_version
        if self.status is not None: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SharedDataObject':
        return cls(added_at=d.get('added_at', None),
                   added_by=d.get('added_by', None),
                   cdf_enabled=d.get('cdf_enabled', None),
                   comment=d.get('comment', None),
                   data_object_type=d.get('data_object_type', None),
                   name=d.get('name', None),
                   partitions=_repeated(d, 'partitions', Partition),
                   shared_as=d.get('shared_as', None),
                   start_version=d.get('start_version', None),
                   status=_enum(d, 'status', SharedDataObjectStatus))


class SharedDataObjectStatus(Enum):
    """One of: **ACTIVE**, **PERMISSION_DENIED**."""

    ACTIVE = 'ACTIVE'
    PERMISSION_DENIED = 'PERMISSION_DENIED'


@dataclass
class SharedDataObjectUpdate:
    action: 'SharedDataObjectUpdateAction' = None
    data_object: 'SharedDataObject' = None

    def as_dict(self) -> dict:
        body = {}
        if self.action is not None: body['action'] = self.action.value
        if self.data_object: body['data_object'] = self.data_object.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SharedDataObjectUpdate':
        return cls(action=_enum(d, 'action', SharedDataObjectUpdateAction),
                   data_object=_from_dict(d, 'data_object', SharedDataObject))


class SharedDataObjectUpdateAction(Enum):
    """One of: **ADD**, **REMOVE**, **UPDATE**."""

    ADD = 'ADD'
    REMOVE = 'REMOVE'
    UPDATE = 'UPDATE'


@dataclass
class UpdateProvider:
    comment: str = None
    name: str = None
    owner: str = None
    recipient_profile_str: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.recipient_profile_str is not None: body['recipient_profile_str'] = self.recipient_profile_str
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateProvider':
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   recipient_profile_str=d.get('recipient_profile_str', None))


@dataclass
class UpdateRecipient:
    comment: str = None
    ip_access_list: 'IpAccessList' = None
    name: str = None
    owner: str = None
    properties_kvpairs: 'SecurablePropertiesKvPairs' = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.properties_kvpairs: body['properties_kvpairs'] = self.properties_kvpairs.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateRecipient':
        return cls(comment=d.get('comment', None),
                   ip_access_list=_from_dict(d, 'ip_access_list', IpAccessList),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   properties_kvpairs=_from_dict(d, 'properties_kvpairs', SecurablePropertiesKvPairs))


@dataclass
class UpdateShare:
    comment: str = None
    name: str = None
    owner: str = None
    updates: 'List[SharedDataObjectUpdate]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.updates: body['updates'] = [v.as_dict() for v in self.updates]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateShare':
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   updates=_repeated(d, 'updates', SharedDataObjectUpdate))


@dataclass
class UpdateSharePermissions:
    changes: 'List[PermissionsChange]' = None
    name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.changes: body['changes'] = [v.as_dict() for v in self.changes]
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateSharePermissions':
        return cls(changes=d.get('changes', None), name=d.get('name', None))


class ProvidersAPI:
    """Databricks Providers REST API"""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               authentication_type: AuthenticationType,
               *,
               comment: str = None,
               recipient_profile_str: str = None,
               **kwargs) -> ProviderInfo:
        """Create an auth provider.
        
        Creates a new authentication provider minimally based on a name and authentication type. The caller
        must be an admin on the metastore."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateProvider(authentication_type=authentication_type,
                                     comment=comment,
                                     name=name,
                                     recipient_profile_str=recipient_profile_str)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.1/unity-catalog/providers', body=body)
        return ProviderInfo.from_dict(json)

    def delete(self, name: str, **kwargs):
        """Delete a provider.
        
        Deletes an authentication provider, if the caller is a metastore admin or is the owner of the
        provider."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteProviderRequest(name=name)

        self._api.do('DELETE', f'/api/2.1/unity-catalog/providers/{request.name}')

    def get(self, name: str, **kwargs) -> ProviderInfo:
        """Get a provider.
        
        Gets a specific authentication provider. The caller must supply the name of the provider, and must
        either be a metastore admin or the owner of the provider."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetProviderRequest(name=name)

        json = self._api.do('GET', f'/api/2.1/unity-catalog/providers/{request.name}')
        return ProviderInfo.from_dict(json)

    def list(self, *, data_provider_global_metastore_id: str = None, **kwargs) -> Iterator[ProviderInfo]:
        """List providers.
        
        Gets an array of available authentication providers. The caller must either be a metastore admin or
        the owner of the providers. Providers not owned by the caller are not included in the response. There
        is no guarantee of a specific ordering of the elements in the array."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListProvidersRequest(
                data_provider_global_metastore_id=data_provider_global_metastore_id)

        query = {}
        if data_provider_global_metastore_id:
            query['data_provider_global_metastore_id'] = request.data_provider_global_metastore_id

        json = self._api.do('GET', '/api/2.1/unity-catalog/providers', query=query)
        return [ProviderInfo.from_dict(v) for v in json.get('providers', [])]

    def list_shares(self, name: str, **kwargs) -> ListProviderSharesResponse:
        """List shares by Provider.
        
        Gets an array of a specified provider's shares within the metastore where:
        
        * the caller is a metastore admin, or * the caller is the owner."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListSharesRequest(name=name)

        json = self._api.do('GET', f'/api/2.1/unity-catalog/providers/{request.name}/shares')
        return ListProviderSharesResponse.from_dict(json)

    def update(self,
               name: str,
               *,
               comment: str = None,
               owner: str = None,
               recipient_profile_str: str = None,
               **kwargs) -> ProviderInfo:
        """Update a provider.
        
        Updates the information for an authentication provider, if the caller is a metastore admin or is the
        owner of the provider. If the update changes the provider name, the caller must be both a metastore
        admin and the owner of the provider."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateProvider(comment=comment,
                                     name=name,
                                     owner=owner,
                                     recipient_profile_str=recipient_profile_str)
        body = request.as_dict()

        json = self._api.do('PATCH', f'/api/2.1/unity-catalog/providers/{request.name}', body=body)
        return ProviderInfo.from_dict(json)


class RecipientActivationAPI:
    """Databricks Recipient Activation REST API"""

    def __init__(self, api_client):
        self._api = api_client

    def get_activation_url_info(self, activation_url: str, **kwargs):
        """Get a share activation URL.
        
        Gets an activation URL for a share."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetActivationUrlInfoRequest(activation_url=activation_url)

        self._api.do('GET',
                     f'/api/2.1/unity-catalog/public/data_sharing_activation_info/{request.activation_url}')

    def retrieve_token(self, activation_url: str, **kwargs) -> RetrieveTokenResponse:
        """Get an access token.
        
        Retrieve access token with an activation url. This is a public API without any authentication."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RetrieveTokenRequest(activation_url=activation_url)

        json = self._api.do(
            'GET', f'/api/2.1/unity-catalog/public/data_sharing_activation/{request.activation_url}')
        return RetrieveTokenResponse.from_dict(json)


class RecipientsAPI:
    """Databricks Recipients REST API"""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               authentication_type: AuthenticationType,
               *,
               comment: str = None,
               data_recipient_global_metastore_id: Any = None,
               ip_access_list: IpAccessList = None,
               owner: str = None,
               properties_kvpairs: SecurablePropertiesKvPairs = None,
               sharing_code: str = None,
               **kwargs) -> RecipientInfo:
        """Create a share recipient.
        
        Creates a new recipient with the delta sharing authentication type in the metastore. The caller must
        be a metastore admin or has the **CREATE_RECIPIENT** privilege on the metastore."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateRecipient(authentication_type=authentication_type,
                                      comment=comment,
                                      data_recipient_global_metastore_id=data_recipient_global_metastore_id,
                                      ip_access_list=ip_access_list,
                                      name=name,
                                      owner=owner,
                                      properties_kvpairs=properties_kvpairs,
                                      sharing_code=sharing_code)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.1/unity-catalog/recipients', body=body)
        return RecipientInfo.from_dict(json)

    def delete(self, name: str, **kwargs):
        """Delete a share recipient.
        
        Deletes the specified recipient from the metastore. The caller must be the owner of the recipient."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteRecipientRequest(name=name)

        self._api.do('DELETE', f'/api/2.1/unity-catalog/recipients/{request.name}')

    def get(self, name: str, **kwargs) -> RecipientInfo:
        """Get a share recipient.
        
        Gets a share recipient from the metastore if:
        
        * the caller is the owner of the share recipient, or: * is a metastore admin"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetRecipientRequest(name=name)

        json = self._api.do('GET', f'/api/2.1/unity-catalog/recipients/{request.name}')
        return RecipientInfo.from_dict(json)

    def list(self, *, data_recipient_global_metastore_id: str = None, **kwargs) -> Iterator[RecipientInfo]:
        """List share recipients.
        
        Gets an array of all share recipients within the current metastore where:
        
        * the caller is a metastore admin, or * the caller is the owner. There is no guarantee of a specific
        ordering of the elements in the array."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListRecipientsRequest(
                data_recipient_global_metastore_id=data_recipient_global_metastore_id)

        query = {}
        if data_recipient_global_metastore_id:
            query['data_recipient_global_metastore_id'] = request.data_recipient_global_metastore_id

        json = self._api.do('GET', '/api/2.1/unity-catalog/recipients', query=query)
        return [RecipientInfo.from_dict(v) for v in json.get('recipients', [])]

    def rotate_token(self, existing_token_expire_in_seconds: int, name: str, **kwargs) -> RecipientInfo:
        """Rotate a token.
        
        Refreshes the specified recipient's delta sharing authentication token with the provided token info.
        The caller must be the owner of the recipient."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RotateRecipientToken(existing_token_expire_in_seconds=existing_token_expire_in_seconds,
                                           name=name)
        body = request.as_dict()

        json = self._api.do('POST',
                            f'/api/2.1/unity-catalog/recipients/{request.name}/rotate-token',
                            body=body)
        return RecipientInfo.from_dict(json)

    def share_permissions(self, name: str, **kwargs) -> GetRecipientSharePermissionsResponse:
        """Get recipient share permissions.
        
        Gets the share permissions for the specified Recipient. The caller must be a metastore admin or the
        owner of the Recipient."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SharePermissionsRequest(name=name)

        json = self._api.do('GET', f'/api/2.1/unity-catalog/recipients/{request.name}/share-permissions')
        return GetRecipientSharePermissionsResponse.from_dict(json)

    def update(self,
               name: str,
               *,
               comment: str = None,
               ip_access_list: IpAccessList = None,
               owner: str = None,
               properties_kvpairs: SecurablePropertiesKvPairs = None,
               **kwargs):
        """Update a share recipient.
        
        Updates an existing recipient in the metastore. The caller must be a metastore admin or the owner of
        the recipient. If the recipient name will be updated, the user must be both a metastore admin and the
        owner of the recipient."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateRecipient(comment=comment,
                                      ip_access_list=ip_access_list,
                                      name=name,
                                      owner=owner,
                                      properties_kvpairs=properties_kvpairs)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/recipients/{request.name}', body=body)


class SharesAPI:
    """Databricks Shares REST API"""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, name: str, *, comment: str = None, **kwargs) -> ShareInfo:
        """Create a share.
        
        Creates a new share for data objects. Data objects can be added after creation with **update**. The
        caller must be a metastore admin or have the **CREATE_SHARE** privilege on the metastore."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateShare(comment=comment, name=name)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.1/unity-catalog/shares', body=body)
        return ShareInfo.from_dict(json)

    def delete(self, name: str, **kwargs):
        """Delete a share.
        
        Deletes a data object share from the metastore. The caller must be an owner of the share."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteShareRequest(name=name)

        self._api.do('DELETE', f'/api/2.1/unity-catalog/shares/{request.name}')

    def get(self, name: str, *, include_shared_data: bool = None, **kwargs) -> ShareInfo:
        """Get a share.
        
        Gets a data object share from the metastore. The caller must be a metastore admin or the owner of the
        share."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetShareRequest(include_shared_data=include_shared_data, name=name)

        query = {}
        if include_shared_data: query['include_shared_data'] = request.include_shared_data

        json = self._api.do('GET', f'/api/2.1/unity-catalog/shares/{request.name}', query=query)
        return ShareInfo.from_dict(json)

    def list(self) -> Iterator[ShareInfo]:
        """List shares.
        
        Gets an array of data object shares from the metastore. The caller must be a metastore admin or the
        owner of the share. There is no guarantee of a specific ordering of the elements in the array."""

        json = self._api.do('GET', '/api/2.1/unity-catalog/shares')
        return [ShareInfo.from_dict(v) for v in json.get('shares', [])]

    def share_permissions(self, name: str, **kwargs) -> PermissionsList:
        """Get permissions.
        
        Gets the permissions for a data share from the metastore. The caller must be a metastore admin or the
        owner of the share."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SharePermissionsRequest(name=name)

        json = self._api.do('GET', f'/api/2.1/unity-catalog/shares/{request.name}/permissions')
        return PermissionsList.from_dict(json)

    def update(self,
               name: str,
               *,
               comment: str = None,
               owner: str = None,
               updates: List[SharedDataObjectUpdate] = None,
               **kwargs) -> ShareInfo:
        """Update a share.
        
        Updates the share with the changes and data objects in the request. The caller must be the owner of
        the share or a metastore admin.
        
        When the caller is a metastore admin, only the __owner__ field can be updated.
        
        In the case that the share name is changed, **updateShare** requires that the caller is both the share
        owner and a metastore admin.
        
        For each table that is added through this method, the share owner must also have **SELECT** privilege
        on the table. This privilege must be maintained indefinitely for recipients to be able to access the
        table. Typically, you should use a group as the share owner.
        
        Table removals through **update** do not require additional privileges."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateShare(comment=comment, name=name, owner=owner, updates=updates)
        body = request.as_dict()

        json = self._api.do('PATCH', f'/api/2.1/unity-catalog/shares/{request.name}', body=body)
        return ShareInfo.from_dict(json)

    def update_permissions(self, name: str, *, changes: List[PermissionsChange] = None, **kwargs):
        """Update permissions.
        
        Updates the permissions for a data share in the metastore. The caller must be a metastore admin or an
        owner of the share.
        
        For new recipient grants, the user must also be the owner of the recipients. recipient revocations do
        not require additional privileges."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateSharePermissions(changes=changes, name=name)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/shares/{request.name}/permissions', body=body)

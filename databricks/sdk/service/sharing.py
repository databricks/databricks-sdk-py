# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated, _validated

_LOG = logging.getLogger('databricks.sdk')

from databricks.sdk.service import catalog

# all definitions in this file are in alphabetical order


class AuthenticationType(Enum):
    """The delta sharing authentication type."""

    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'


@dataclass
class CentralCleanRoomInfo:
    clean_room_assets: Optional['List[CleanRoomAssetInfo]'] = None
    collaborators: Optional['List[CleanRoomCollaboratorInfo]'] = None
    creator: Optional['CleanRoomCollaboratorInfo'] = None
    station_cloud: Optional[str] = None
    station_region: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.clean_room_assets:
            body['clean_room_assets'] = [
                _validated('clean_room_assets item', CleanRoomAssetInfo, v) for v in self.clean_room_assets
            ]
        if self.collaborators:
            body['collaborators'] = [
                _validated('collaborators item', CleanRoomCollaboratorInfo, v) for v in self.collaborators
            ]
        if self.creator: body['creator'] = _validated('creator', CleanRoomCollaboratorInfo, self.creator)
        if self.station_cloud is not None:
            body['station_cloud'] = _validated('station_cloud', str, self.station_cloud)
        if self.station_region is not None:
            body['station_region'] = _validated('station_region', str, self.station_region)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CentralCleanRoomInfo':
        return cls(clean_room_assets=_repeated(d, 'clean_room_assets', CleanRoomAssetInfo),
                   collaborators=_repeated(d, 'collaborators', CleanRoomCollaboratorInfo),
                   creator=_from_dict(d, 'creator', CleanRoomCollaboratorInfo),
                   station_cloud=d.get('station_cloud', None),
                   station_region=d.get('station_region', None))


@dataclass
class CleanRoomAssetInfo:
    added_at: Optional[int] = None
    notebook_info: Optional['CleanRoomNotebookInfo'] = None
    owner: Optional['CleanRoomCollaboratorInfo'] = None
    table_info: Optional['CleanRoomTableInfo'] = None
    updated_at: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.added_at is not None: body['added_at'] = _validated('added_at', int, self.added_at)
        if self.notebook_info:
            body['notebook_info'] = _validated('notebook_info', CleanRoomNotebookInfo, self.notebook_info)
        if self.owner: body['owner'] = _validated('owner', CleanRoomCollaboratorInfo, self.owner)
        if self.table_info: body['table_info'] = _validated('table_info', CleanRoomTableInfo, self.table_info)
        if self.updated_at is not None: body['updated_at'] = _validated('updated_at', int, self.updated_at)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CleanRoomAssetInfo':
        return cls(added_at=d.get('added_at', None),
                   notebook_info=_from_dict(d, 'notebook_info', CleanRoomNotebookInfo),
                   owner=_from_dict(d, 'owner', CleanRoomCollaboratorInfo),
                   table_info=_from_dict(d, 'table_info', CleanRoomTableInfo),
                   updated_at=d.get('updated_at', None))


@dataclass
class CleanRoomCatalog:
    catalog_name: Optional[str] = None
    notebook_files: Optional['List[SharedDataObject]'] = None
    tables: Optional['List[SharedDataObject]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.catalog_name is not None:
            body['catalog_name'] = _validated('catalog_name', str, self.catalog_name)
        if self.notebook_files:
            body['notebook_files'] = [
                _validated('notebook_files item', SharedDataObject, v) for v in self.notebook_files
            ]
        if self.tables: body['tables'] = [_validated('tables item', SharedDataObject, v) for v in self.tables]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CleanRoomCatalog':
        return cls(catalog_name=d.get('catalog_name', None),
                   notebook_files=_repeated(d, 'notebook_files', SharedDataObject),
                   tables=_repeated(d, 'tables', SharedDataObject))


@dataclass
class CleanRoomCatalogUpdate:
    catalog_name: Optional[str] = None
    updates: Optional['SharedDataObjectUpdate'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.catalog_name is not None:
            body['catalog_name'] = _validated('catalog_name', str, self.catalog_name)
        if self.updates: body['updates'] = _validated('updates', SharedDataObjectUpdate, self.updates)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CleanRoomCatalogUpdate':
        return cls(catalog_name=d.get('catalog_name', None),
                   updates=_from_dict(d, 'updates', SharedDataObjectUpdate))


@dataclass
class CleanRoomCollaboratorInfo:
    global_metastore_id: Optional[str] = None
    organization_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.global_metastore_id is not None:
            body['global_metastore_id'] = _validated('global_metastore_id', str, self.global_metastore_id)
        if self.organization_name is not None:
            body['organization_name'] = _validated('organization_name', str, self.organization_name)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CleanRoomCollaboratorInfo':
        return cls(global_metastore_id=d.get('global_metastore_id', None),
                   organization_name=d.get('organization_name', None))


@dataclass
class CleanRoomInfo:
    comment: Optional[str] = None
    created_at: Optional[int] = None
    created_by: Optional[str] = None
    local_catalogs: Optional['List[CleanRoomCatalog]'] = None
    name: Optional[str] = None
    owner: Optional[str] = None
    remote_detailed_info: Optional['CentralCleanRoomInfo'] = None
    updated_at: Optional[int] = None
    updated_by: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.created_at is not None: body['created_at'] = _validated('created_at', int, self.created_at)
        if self.created_by is not None: body['created_by'] = _validated('created_by', str, self.created_by)
        if self.local_catalogs:
            body['local_catalogs'] = [
                _validated('local_catalogs item', CleanRoomCatalog, v) for v in self.local_catalogs
            ]
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.owner is not None: body['owner'] = _validated('owner', str, self.owner)
        if self.remote_detailed_info:
            body['remote_detailed_info'] = _validated('remote_detailed_info', CentralCleanRoomInfo,
                                                      self.remote_detailed_info)
        if self.updated_at is not None: body['updated_at'] = _validated('updated_at', int, self.updated_at)
        if self.updated_by is not None: body['updated_by'] = _validated('updated_by', str, self.updated_by)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CleanRoomInfo':
        return cls(comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   local_catalogs=_repeated(d, 'local_catalogs', CleanRoomCatalog),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   remote_detailed_info=_from_dict(d, 'remote_detailed_info', CentralCleanRoomInfo),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


@dataclass
class CleanRoomNotebookInfo:
    notebook_content: Optional[str] = None
    notebook_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.notebook_content is not None:
            body['notebook_content'] = _validated('notebook_content', str, self.notebook_content)
        if self.notebook_name is not None:
            body['notebook_name'] = _validated('notebook_name', str, self.notebook_name)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CleanRoomNotebookInfo':
        return cls(notebook_content=d.get('notebook_content', None),
                   notebook_name=d.get('notebook_name', None))


@dataclass
class CleanRoomTableInfo:
    catalog_name: Optional[str] = None
    columns: Optional['List[ColumnInfo]'] = None
    full_name: Optional[str] = None
    name: Optional[str] = None
    schema_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.catalog_name is not None:
            body['catalog_name'] = _validated('catalog_name', str, self.catalog_name)
        if self.columns: body['columns'] = [_validated('columns item', ColumnInfo, v) for v in self.columns]
        if self.full_name is not None: body['full_name'] = _validated('full_name', str, self.full_name)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.schema_name is not None:
            body['schema_name'] = _validated('schema_name', str, self.schema_name)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CleanRoomTableInfo':
        return cls(catalog_name=d.get('catalog_name', None),
                   columns=_repeated(d, 'columns', ColumnInfo),
                   full_name=d.get('full_name', None),
                   name=d.get('name', None),
                   schema_name=d.get('schema_name', None))


@dataclass
class ColumnInfo:
    comment: Optional[str] = None
    mask: Optional['ColumnMask'] = None
    name: Optional[str] = None
    nullable: Optional[bool] = None
    partition_index: Optional[int] = None
    position: Optional[int] = None
    type_interval_type: Optional[str] = None
    type_json: Optional[str] = None
    type_name: Optional['ColumnTypeName'] = None
    type_precision: Optional[int] = None
    type_scale: Optional[int] = None
    type_text: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.mask: body['mask'] = _validated('mask', ColumnMask, self.mask)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.nullable is not None: body['nullable'] = _validated('nullable', bool, self.nullable)
        if self.partition_index is not None:
            body['partition_index'] = _validated('partition_index', int, self.partition_index)
        if self.position is not None: body['position'] = _validated('position', int, self.position)
        if self.type_interval_type is not None:
            body['type_interval_type'] = _validated('type_interval_type', str, self.type_interval_type)
        if self.type_json is not None: body['type_json'] = _validated('type_json', str, self.type_json)
        if self.type_name is not None:
            body['type_name'] = _validated('type_name', ColumnTypeName, self.type_name)
        if self.type_precision is not None:
            body['type_precision'] = _validated('type_precision', int, self.type_precision)
        if self.type_scale is not None: body['type_scale'] = _validated('type_scale', int, self.type_scale)
        if self.type_text is not None: body['type_text'] = _validated('type_text', str, self.type_text)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ColumnInfo':
        return cls(comment=d.get('comment', None),
                   mask=_from_dict(d, 'mask', ColumnMask),
                   name=d.get('name', None),
                   nullable=d.get('nullable', None),
                   partition_index=d.get('partition_index', None),
                   position=d.get('position', None),
                   type_interval_type=d.get('type_interval_type', None),
                   type_json=d.get('type_json', None),
                   type_name=_enum(d, 'type_name', ColumnTypeName),
                   type_precision=d.get('type_precision', None),
                   type_scale=d.get('type_scale', None),
                   type_text=d.get('type_text', None))


@dataclass
class ColumnMask:
    function_name: Optional[str] = None
    using_column_names: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.function_name is not None:
            body['function_name'] = _validated('function_name', str, self.function_name)
        if self.using_column_names:
            body['using_column_names'] = [
                _validated('using_column_names item', str, v) for v in self.using_column_names
            ]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ColumnMask':
        return cls(function_name=d.get('function_name', None),
                   using_column_names=d.get('using_column_names', None))


class ColumnTypeName(Enum):
    """Name of type (INT, STRUCT, MAP, etc.)."""

    ARRAY = 'ARRAY'
    BINARY = 'BINARY'
    BOOLEAN = 'BOOLEAN'
    BYTE = 'BYTE'
    CHAR = 'CHAR'
    DATE = 'DATE'
    DECIMAL = 'DECIMAL'
    DOUBLE = 'DOUBLE'
    FLOAT = 'FLOAT'
    INT = 'INT'
    INTERVAL = 'INTERVAL'
    LONG = 'LONG'
    MAP = 'MAP'
    NULL = 'NULL'
    SHORT = 'SHORT'
    STRING = 'STRING'
    STRUCT = 'STRUCT'
    TABLE_TYPE = 'TABLE_TYPE'
    TIMESTAMP = 'TIMESTAMP'
    TIMESTAMP_NTZ = 'TIMESTAMP_NTZ'
    USER_DEFINED_TYPE = 'USER_DEFINED_TYPE'


@dataclass
class CreateCleanRoom:
    name: str
    remote_detailed_info: 'CentralCleanRoomInfo'
    comment: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.remote_detailed_info:
            body['remote_detailed_info'] = _validated('remote_detailed_info', CentralCleanRoomInfo,
                                                      self.remote_detailed_info)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCleanRoom':
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   remote_detailed_info=_from_dict(d, 'remote_detailed_info', CentralCleanRoomInfo))


@dataclass
class CreateProvider:
    name: str
    authentication_type: 'AuthenticationType'
    comment: Optional[str] = None
    recipient_profile_str: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.authentication_type is not None:
            body['authentication_type'] = _validated('authentication_type', AuthenticationType,
                                                     self.authentication_type)
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.recipient_profile_str is not None:
            body['recipient_profile_str'] = _validated('recipient_profile_str', str,
                                                       self.recipient_profile_str)
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
    comment: Optional[str] = None
    data_recipient_global_metastore_id: Optional[Any] = None
    ip_access_list: Optional['IpAccessList'] = None
    owner: Optional[str] = None
    properties_kvpairs: Optional['SecurablePropertiesKvPairs'] = None
    sharing_code: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.authentication_type is not None:
            body['authentication_type'] = _validated('authentication_type', AuthenticationType,
                                                     self.authentication_type)
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.data_recipient_global_metastore_id:
            body['data_recipient_global_metastore_id'] = _validated('data_recipient_global_metastore_id', Any,
                                                                    self.data_recipient_global_metastore_id)
        if self.ip_access_list:
            body['ip_access_list'] = _validated('ip_access_list', IpAccessList, self.ip_access_list)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.owner is not None: body['owner'] = _validated('owner', str, self.owner)
        if self.properties_kvpairs:
            body['properties_kvpairs'] = _validated('properties_kvpairs', SecurablePropertiesKvPairs,
                                                    self.properties_kvpairs)
        if self.sharing_code is not None:
            body['sharing_code'] = _validated('sharing_code', str, self.sharing_code)
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
    comment: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateShare':
        return cls(comment=d.get('comment', None), name=d.get('name', None))


@dataclass
class GetRecipientSharePermissionsResponse:
    permissions_out: Optional['List[ShareToPrivilegeAssignment]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.permissions_out:
            body['permissions_out'] = [
                _validated('permissions_out item', ShareToPrivilegeAssignment, v)
                for v in self.permissions_out
            ]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRecipientSharePermissionsResponse':
        return cls(permissions_out=_repeated(d, 'permissions_out', ShareToPrivilegeAssignment))


@dataclass
class IpAccessList:
    allowed_ip_addresses: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.allowed_ip_addresses:
            body['allowed_ip_addresses'] = [
                _validated('allowed_ip_addresses item', str, v) for v in self.allowed_ip_addresses
            ]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'IpAccessList':
        return cls(allowed_ip_addresses=d.get('allowed_ip_addresses', None))


@dataclass
class ListCleanRoomsResponse:
    clean_rooms: Optional['List[CleanRoomInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.clean_rooms:
            body['clean_rooms'] = [_validated('clean_rooms item', CleanRoomInfo, v) for v in self.clean_rooms]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListCleanRoomsResponse':
        return cls(clean_rooms=_repeated(d, 'clean_rooms', CleanRoomInfo))


@dataclass
class ListProviderSharesResponse:
    shares: Optional['List[ProviderShare]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.shares: body['shares'] = [_validated('shares item', ProviderShare, v) for v in self.shares]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListProviderSharesResponse':
        return cls(shares=_repeated(d, 'shares', ProviderShare))


@dataclass
class ListProvidersResponse:
    providers: Optional['List[ProviderInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.providers:
            body['providers'] = [_validated('providers item', ProviderInfo, v) for v in self.providers]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListProvidersResponse':
        return cls(providers=_repeated(d, 'providers', ProviderInfo))


@dataclass
class ListRecipientsResponse:
    recipients: Optional['List[RecipientInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.recipients:
            body['recipients'] = [_validated('recipients item', RecipientInfo, v) for v in self.recipients]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRecipientsResponse':
        return cls(recipients=_repeated(d, 'recipients', RecipientInfo))


@dataclass
class ListSharesResponse:
    shares: Optional['List[ShareInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.shares: body['shares'] = [_validated('shares item', ShareInfo, v) for v in self.shares]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListSharesResponse':
        return cls(shares=_repeated(d, 'shares', ShareInfo))


@dataclass
class Partition:
    values: Optional['List[PartitionValue]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.values: body['values'] = [_validated('values item', PartitionValue, v) for v in self.values]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Partition':
        return cls(values=_repeated(d, 'values', PartitionValue))


@dataclass
class PartitionValue:
    name: Optional[str] = None
    op: Optional['PartitionValueOp'] = None
    recipient_property_key: Optional[str] = None
    value: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.op is not None: body['op'] = _validated('op', PartitionValueOp, self.op)
        if self.recipient_property_key is not None:
            body['recipient_property_key'] = _validated('recipient_property_key', str,
                                                        self.recipient_property_key)
        if self.value is not None: body['value'] = _validated('value', str, self.value)
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
    CREATE_CONNECTION = 'CREATE_CONNECTION'
    CREATE_EXTERNAL_LOCATION = 'CREATE_EXTERNAL_LOCATION'
    CREATE_EXTERNAL_TABLE = 'CREATE_EXTERNAL_TABLE'
    CREATE_FOREIGN_CATALOG = 'CREATE_FOREIGN_CATALOG'
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
    USE_CONNECTION = 'USE_CONNECTION'
    USE_MARKETPLACE_ASSETS = 'USE_MARKETPLACE_ASSETS'
    USE_PROVIDER = 'USE_PROVIDER'
    USE_RECIPIENT = 'USE_RECIPIENT'
    USE_SCHEMA = 'USE_SCHEMA'
    USE_SHARE = 'USE_SHARE'
    WRITE_FILES = 'WRITE_FILES'
    WRITE_PRIVATE_FILES = 'WRITE_PRIVATE_FILES'


@dataclass
class PrivilegeAssignment:
    principal: Optional[str] = None
    privileges: Optional['List[Privilege]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.principal is not None: body['principal'] = _validated('principal', str, self.principal)
        if self.privileges:
            body['privileges'] = [_validated('privileges item', Privilege, v) for v in self.privileges]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PrivilegeAssignment':
        return cls(principal=d.get('principal', None), privileges=d.get('privileges', None))


@dataclass
class ProviderInfo:
    authentication_type: Optional['AuthenticationType'] = None
    cloud: Optional[str] = None
    comment: Optional[str] = None
    created_at: Optional[int] = None
    created_by: Optional[str] = None
    data_provider_global_metastore_id: Optional[str] = None
    metastore_id: Optional[str] = None
    name: Optional[str] = None
    owner: Optional[str] = None
    recipient_profile: Optional['RecipientProfile'] = None
    recipient_profile_str: Optional[str] = None
    region: Optional[str] = None
    updated_at: Optional[int] = None
    updated_by: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.authentication_type is not None:
            body['authentication_type'] = _validated('authentication_type', AuthenticationType,
                                                     self.authentication_type)
        if self.cloud is not None: body['cloud'] = _validated('cloud', str, self.cloud)
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.created_at is not None: body['created_at'] = _validated('created_at', int, self.created_at)
        if self.created_by is not None: body['created_by'] = _validated('created_by', str, self.created_by)
        if self.data_provider_global_metastore_id is not None:
            body['data_provider_global_metastore_id'] = _validated('data_provider_global_metastore_id', str,
                                                                   self.data_provider_global_metastore_id)
        if self.metastore_id is not None:
            body['metastore_id'] = _validated('metastore_id', str, self.metastore_id)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.owner is not None: body['owner'] = _validated('owner', str, self.owner)
        if self.recipient_profile:
            body['recipient_profile'] = _validated('recipient_profile', RecipientProfile,
                                                   self.recipient_profile)
        if self.recipient_profile_str is not None:
            body['recipient_profile_str'] = _validated('recipient_profile_str', str,
                                                       self.recipient_profile_str)
        if self.region is not None: body['region'] = _validated('region', str, self.region)
        if self.updated_at is not None: body['updated_at'] = _validated('updated_at', int, self.updated_at)
        if self.updated_by is not None: body['updated_by'] = _validated('updated_by', str, self.updated_by)
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
    name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ProviderShare':
        return cls(name=d.get('name', None))


@dataclass
class RecipientInfo:
    activated: Optional[bool] = None
    activation_url: Optional[str] = None
    authentication_type: Optional['AuthenticationType'] = None
    cloud: Optional[str] = None
    comment: Optional[str] = None
    created_at: Optional[int] = None
    created_by: Optional[str] = None
    data_recipient_global_metastore_id: Optional[Any] = None
    ip_access_list: Optional['IpAccessList'] = None
    metastore_id: Optional[str] = None
    name: Optional[str] = None
    owner: Optional[str] = None
    properties_kvpairs: Optional['SecurablePropertiesKvPairs'] = None
    region: Optional[str] = None
    sharing_code: Optional[str] = None
    tokens: Optional['List[RecipientTokenInfo]'] = None
    updated_at: Optional[int] = None
    updated_by: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.activated is not None: body['activated'] = _validated('activated', bool, self.activated)
        if self.activation_url is not None:
            body['activation_url'] = _validated('activation_url', str, self.activation_url)
        if self.authentication_type is not None:
            body['authentication_type'] = _validated('authentication_type', AuthenticationType,
                                                     self.authentication_type)
        if self.cloud is not None: body['cloud'] = _validated('cloud', str, self.cloud)
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.created_at is not None: body['created_at'] = _validated('created_at', int, self.created_at)
        if self.created_by is not None: body['created_by'] = _validated('created_by', str, self.created_by)
        if self.data_recipient_global_metastore_id:
            body['data_recipient_global_metastore_id'] = _validated('data_recipient_global_metastore_id', Any,
                                                                    self.data_recipient_global_metastore_id)
        if self.ip_access_list:
            body['ip_access_list'] = _validated('ip_access_list', IpAccessList, self.ip_access_list)
        if self.metastore_id is not None:
            body['metastore_id'] = _validated('metastore_id', str, self.metastore_id)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.owner is not None: body['owner'] = _validated('owner', str, self.owner)
        if self.properties_kvpairs:
            body['properties_kvpairs'] = _validated('properties_kvpairs', SecurablePropertiesKvPairs,
                                                    self.properties_kvpairs)
        if self.region is not None: body['region'] = _validated('region', str, self.region)
        if self.sharing_code is not None:
            body['sharing_code'] = _validated('sharing_code', str, self.sharing_code)
        if self.tokens:
            body['tokens'] = [_validated('tokens item', RecipientTokenInfo, v) for v in self.tokens]
        if self.updated_at is not None: body['updated_at'] = _validated('updated_at', int, self.updated_at)
        if self.updated_by is not None: body['updated_by'] = _validated('updated_by', str, self.updated_by)
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
    bearer_token: Optional[str] = None
    endpoint: Optional[str] = None
    share_credentials_version: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.bearer_token is not None:
            body['bearer_token'] = _validated('bearer_token', str, self.bearer_token)
        if self.endpoint is not None: body['endpoint'] = _validated('endpoint', str, self.endpoint)
        if self.share_credentials_version is not None:
            body['share_credentials_version'] = _validated('share_credentials_version', int,
                                                           self.share_credentials_version)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RecipientProfile':
        return cls(bearer_token=d.get('bearer_token', None),
                   endpoint=d.get('endpoint', None),
                   share_credentials_version=d.get('share_credentials_version', None))


@dataclass
class RecipientTokenInfo:
    activation_url: Optional[str] = None
    created_at: Optional[int] = None
    created_by: Optional[str] = None
    expiration_time: Optional[int] = None
    id: Optional[str] = None
    updated_at: Optional[int] = None
    updated_by: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.activation_url is not None:
            body['activation_url'] = _validated('activation_url', str, self.activation_url)
        if self.created_at is not None: body['created_at'] = _validated('created_at', int, self.created_at)
        if self.created_by is not None: body['created_by'] = _validated('created_by', str, self.created_by)
        if self.expiration_time is not None:
            body['expiration_time'] = _validated('expiration_time', int, self.expiration_time)
        if self.id is not None: body['id'] = _validated('id', str, self.id)
        if self.updated_at is not None: body['updated_at'] = _validated('updated_at', int, self.updated_at)
        if self.updated_by is not None: body['updated_by'] = _validated('updated_by', str, self.updated_by)
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
class RetrieveTokenResponse:
    bearer_token: Optional[str] = None
    endpoint: Optional[str] = None
    expiration_time: Optional[str] = None
    share_credentials_version: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.bearer_token is not None:
            body['bearerToken'] = _validated('bearer_token', str, self.bearer_token)
        if self.endpoint is not None: body['endpoint'] = _validated('endpoint', str, self.endpoint)
        if self.expiration_time is not None:
            body['expirationTime'] = _validated('expiration_time', str, self.expiration_time)
        if self.share_credentials_version is not None:
            body['shareCredentialsVersion'] = _validated('share_credentials_version', int,
                                                         self.share_credentials_version)
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
    name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.existing_token_expire_in_seconds is not None:
            body['existing_token_expire_in_seconds'] = _validated('existing_token_expire_in_seconds', int,
                                                                  self.existing_token_expire_in_seconds)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
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
        if self.properties:
            body['properties'] = {
                k: _validated('properties item', str, v)
                for (k, v) in self.properties.items()
            }
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SecurablePropertiesKvPairs':
        return cls(properties=d.get('properties', None))


SecurablePropertiesMap = Dict[str, str]


@dataclass
class ShareInfo:
    comment: Optional[str] = None
    created_at: Optional[int] = None
    created_by: Optional[str] = None
    name: Optional[str] = None
    objects: Optional['List[SharedDataObject]'] = None
    owner: Optional[str] = None
    updated_at: Optional[int] = None
    updated_by: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.created_at is not None: body['created_at'] = _validated('created_at', int, self.created_at)
        if self.created_by is not None: body['created_by'] = _validated('created_by', str, self.created_by)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.objects:
            body['objects'] = [_validated('objects item', SharedDataObject, v) for v in self.objects]
        if self.owner is not None: body['owner'] = _validated('owner', str, self.owner)
        if self.updated_at is not None: body['updated_at'] = _validated('updated_at', int, self.updated_at)
        if self.updated_by is not None: body['updated_by'] = _validated('updated_by', str, self.updated_by)
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
class ShareToPrivilegeAssignment:
    privilege_assignments: Optional['List[PrivilegeAssignment]'] = None
    share_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.privilege_assignments:
            body['privilege_assignments'] = [
                _validated('privilege_assignments item', PrivilegeAssignment, v)
                for v in self.privilege_assignments
            ]
        if self.share_name is not None: body['share_name'] = _validated('share_name', str, self.share_name)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ShareToPrivilegeAssignment':
        return cls(privilege_assignments=_repeated(d, 'privilege_assignments', PrivilegeAssignment),
                   share_name=d.get('share_name', None))


@dataclass
class SharedDataObject:
    name: str
    added_at: Optional[int] = None
    added_by: Optional[str] = None
    cdf_enabled: Optional[bool] = None
    comment: Optional[str] = None
    data_object_type: Optional[str] = None
    history_data_sharing_status: Optional['SharedDataObjectHistoryDataSharingStatus'] = None
    partitions: Optional['List[Partition]'] = None
    shared_as: Optional[str] = None
    start_version: Optional[int] = None
    status: Optional['SharedDataObjectStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.added_at is not None: body['added_at'] = _validated('added_at', int, self.added_at)
        if self.added_by is not None: body['added_by'] = _validated('added_by', str, self.added_by)
        if self.cdf_enabled is not None:
            body['cdf_enabled'] = _validated('cdf_enabled', bool, self.cdf_enabled)
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.data_object_type is not None:
            body['data_object_type'] = _validated('data_object_type', str, self.data_object_type)
        if self.history_data_sharing_status is not None:
            body['history_data_sharing_status'] = _validated('history_data_sharing_status',
                                                             SharedDataObjectHistoryDataSharingStatus,
                                                             self.history_data_sharing_status)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.partitions:
            body['partitions'] = [_validated('partitions item', Partition, v) for v in self.partitions]
        if self.shared_as is not None: body['shared_as'] = _validated('shared_as', str, self.shared_as)
        if self.start_version is not None:
            body['start_version'] = _validated('start_version', int, self.start_version)
        if self.status is not None: body['status'] = _validated('status', SharedDataObjectStatus, self.status)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SharedDataObject':
        return cls(added_at=d.get('added_at', None),
                   added_by=d.get('added_by', None),
                   cdf_enabled=d.get('cdf_enabled', None),
                   comment=d.get('comment', None),
                   data_object_type=d.get('data_object_type', None),
                   history_data_sharing_status=_enum(d, 'history_data_sharing_status',
                                                     SharedDataObjectHistoryDataSharingStatus),
                   name=d.get('name', None),
                   partitions=_repeated(d, 'partitions', Partition),
                   shared_as=d.get('shared_as', None),
                   start_version=d.get('start_version', None),
                   status=_enum(d, 'status', SharedDataObjectStatus))


class SharedDataObjectHistoryDataSharingStatus(Enum):
    """Whether to enable or disable sharing of data history. If not specified, the default is
    **DISABLED**."""

    DISABLED = 'DISABLED'
    ENABLED = 'ENABLED'


class SharedDataObjectStatus(Enum):
    """One of: **ACTIVE**, **PERMISSION_DENIED**."""

    ACTIVE = 'ACTIVE'
    PERMISSION_DENIED = 'PERMISSION_DENIED'


@dataclass
class SharedDataObjectUpdate:
    action: Optional['SharedDataObjectUpdateAction'] = None
    data_object: Optional['SharedDataObject'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.action is not None:
            body['action'] = _validated('action', SharedDataObjectUpdateAction, self.action)
        if self.data_object:
            body['data_object'] = _validated('data_object', SharedDataObject, self.data_object)
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
class UpdateCleanRoom:
    catalog_updates: Optional['List[CleanRoomCatalogUpdate]'] = None
    comment: Optional[str] = None
    name: Optional[str] = None
    name_arg: Optional[str] = None
    owner: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.catalog_updates:
            body['catalog_updates'] = [
                _validated('catalog_updates item', CleanRoomCatalogUpdate, v) for v in self.catalog_updates
            ]
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.name_arg is not None: body['name_arg'] = _validated('name_arg', str, self.name_arg)
        if self.owner is not None: body['owner'] = _validated('owner', str, self.owner)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateCleanRoom':
        return cls(catalog_updates=_repeated(d, 'catalog_updates', CleanRoomCatalogUpdate),
                   comment=d.get('comment', None),
                   name=d.get('name', None),
                   name_arg=d.get('name_arg', None),
                   owner=d.get('owner', None))


@dataclass
class UpdateProvider:
    comment: Optional[str] = None
    name: Optional[str] = None
    owner: Optional[str] = None
    recipient_profile_str: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.owner is not None: body['owner'] = _validated('owner', str, self.owner)
        if self.recipient_profile_str is not None:
            body['recipient_profile_str'] = _validated('recipient_profile_str', str,
                                                       self.recipient_profile_str)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateProvider':
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   recipient_profile_str=d.get('recipient_profile_str', None))


@dataclass
class UpdateRecipient:
    comment: Optional[str] = None
    ip_access_list: Optional['IpAccessList'] = None
    name: Optional[str] = None
    owner: Optional[str] = None
    properties_kvpairs: Optional['SecurablePropertiesKvPairs'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.ip_access_list:
            body['ip_access_list'] = _validated('ip_access_list', IpAccessList, self.ip_access_list)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.owner is not None: body['owner'] = _validated('owner', str, self.owner)
        if self.properties_kvpairs:
            body['properties_kvpairs'] = _validated('properties_kvpairs', SecurablePropertiesKvPairs,
                                                    self.properties_kvpairs)
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
    comment: Optional[str] = None
    name: Optional[str] = None
    owner: Optional[str] = None
    updates: Optional['List[SharedDataObjectUpdate]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = _validated('comment', str, self.comment)
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        if self.owner is not None: body['owner'] = _validated('owner', str, self.owner)
        if self.updates:
            body['updates'] = [_validated('updates item', SharedDataObjectUpdate, v) for v in self.updates]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateShare':
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   updates=_repeated(d, 'updates', SharedDataObjectUpdate))


@dataclass
class UpdateSharePermissions:
    changes: Optional['List[catalog.PermissionsChange]'] = None
    name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.changes:
            body['changes'] = [_validated('changes item', catalog.PermissionsChange, v) for v in self.changes]
        if self.name is not None: body['name'] = _validated('name', str, self.name)
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateSharePermissions':
        return cls(changes=_repeated(d, 'changes', catalog.PermissionsChange), name=d.get('name', None))


class CleanRoomsAPI:
    """A clean room is a secure, privacy-protecting environment where two or more parties can share sensitive
    enterprise data, including customer data, for measurements, insights, activation and other use cases.
    
    To create clean rooms, you must be a metastore admin or a user with the **CREATE_CLEAN_ROOM** privilege."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               remote_detailed_info: CentralCleanRoomInfo,
               *,
               comment: Optional[str] = None) -> CleanRoomInfo:
        """Create a clean room.
        
        Creates a new clean room with specified colaborators. The caller must be a metastore admin or have the
        **CREATE_CLEAN_ROOM** privilege on the metastore.
        
        :param name: str
          Name of the clean room.
        :param remote_detailed_info: :class:`CentralCleanRoomInfo`
          Central clean room details.
        :param comment: str (optional)
          User-provided free-form text description.
        
        :returns: :class:`CleanRoomInfo`
        """
        body = {}
        if comment is not None: body['comment'] = _validated('comment', str, comment)
        if name is not None: body['name'] = _validated('name', str, name)
        if remote_detailed_info is not None:
            body['remote_detailed_info'] = _validated('remote_detailed_info', CentralCleanRoomInfo,
                                                      remote_detailed_info)

        json = self._api.do('POST', '/api/2.1/unity-catalog/clean-rooms', body=body)
        return CleanRoomInfo.from_dict(json)

    def delete(self, name_arg: str):
        """Delete a clean room.
        
        Deletes a data object clean room from the metastore. The caller must be an owner of the clean room.
        
        :param name_arg: str
          The name of the clean room.
        
        
        """

        self._api.do('DELETE', f'/api/2.1/unity-catalog/clean-rooms/{name_arg}')

    def get(self, name_arg: str, *, include_remote_details: Optional[bool] = None) -> CleanRoomInfo:
        """Get a clean room.
        
        Gets a data object clean room from the metastore. The caller must be a metastore admin or the owner of
        the clean room.
        
        :param name_arg: str
          The name of the clean room.
        :param include_remote_details: bool (optional)
          Whether to include remote details (central) on the clean room.
        
        :returns: :class:`CleanRoomInfo`
        """

        query = {}
        if include_remote_details is not None:
            query['include_remote_details'] = _validated('include_remote_details', bool,
                                                         include_remote_details)

        json = self._api.do('GET', f'/api/2.1/unity-catalog/clean-rooms/{name_arg}', query=query)
        return CleanRoomInfo.from_dict(json)

    def list(self) -> Iterator[CleanRoomInfo]:
        """List clean rooms.
        
        Gets an array of data object clean rooms from the metastore. The caller must be a metastore admin or
        the owner of the clean room. There is no guarantee of a specific ordering of the elements in the
        array.
        
        :returns: Iterator over :class:`CleanRoomInfo`
        """

        json = self._api.do('GET', '/api/2.1/unity-catalog/clean-rooms')
        return [CleanRoomInfo.from_dict(v) for v in json.get('clean_rooms', [])]

    def update(self,
               name_arg: str,
               *,
               catalog_updates: Optional[List[CleanRoomCatalogUpdate]] = None,
               comment: Optional[str] = None,
               name: Optional[str] = None,
               owner: Optional[str] = None) -> CleanRoomInfo:
        """Update a clean room.
        
        Updates the clean room with the changes and data objects in the request. The caller must be the owner
        of the clean room or a metastore admin.
        
        When the caller is a metastore admin, only the __owner__ field can be updated.
        
        In the case that the clean room name is changed **updateCleanRoom** requires that the caller is both
        the clean room owner and a metastore admin.
        
        For each table that is added through this method, the clean room owner must also have **SELECT**
        privilege on the table. The privilege must be maintained indefinitely for recipients to be able to
        access the table. Typically, you should use a group as the clean room owner.
        
        Table removals through **update** do not require additional privileges.
        
        :param name_arg: str
          The name of the clean room.
        :param catalog_updates: List[:class:`CleanRoomCatalogUpdate`] (optional)
          Array of shared data object updates.
        :param comment: str (optional)
          User-provided free-form text description.
        :param name: str (optional)
          Name of the clean room.
        :param owner: str (optional)
          Username of current owner of clean room.
        
        :returns: :class:`CleanRoomInfo`
        """
        body = {}
        if catalog_updates is not None:
            body['catalog_updates'] = [
                _validated('catalog_updates item', CleanRoomCatalogUpdate, v) for v in catalog_updates
            ]
        if comment is not None: body['comment'] = _validated('comment', str, comment)
        if name is not None: body['name'] = _validated('name', str, name)
        if owner is not None: body['owner'] = _validated('owner', str, owner)

        json = self._api.do('PATCH', f'/api/2.1/unity-catalog/clean-rooms/{name_arg}', body=body)
        return CleanRoomInfo.from_dict(json)


class ProvidersAPI:
    """A data provider is an object representing the organization in the real world who shares the data. A
    provider contains shares which further contain the shared data."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               authentication_type: AuthenticationType,
               *,
               comment: Optional[str] = None,
               recipient_profile_str: Optional[str] = None) -> ProviderInfo:
        """Create an auth provider.
        
        Creates a new authentication provider minimally based on a name and authentication type. The caller
        must be an admin on the metastore.
        
        :param name: str
          The name of the Provider.
        :param authentication_type: :class:`AuthenticationType`
          The delta sharing authentication type.
        :param comment: str (optional)
          Description about the provider.
        :param recipient_profile_str: str (optional)
          This field is required when the __authentication_type__ is **TOKEN** or not provided.
        
        :returns: :class:`ProviderInfo`
        """
        body = {}
        if authentication_type is not None:
            body['authentication_type'] = _validated('authentication_type', AuthenticationType,
                                                     authentication_type)
        if comment is not None: body['comment'] = _validated('comment', str, comment)
        if name is not None: body['name'] = _validated('name', str, name)
        if recipient_profile_str is not None:
            body['recipient_profile_str'] = _validated('recipient_profile_str', str, recipient_profile_str)

        json = self._api.do('POST', '/api/2.1/unity-catalog/providers', body=body)
        return ProviderInfo.from_dict(json)

    def delete(self, name: str):
        """Delete a provider.
        
        Deletes an authentication provider, if the caller is a metastore admin or is the owner of the
        provider.
        
        :param name: str
          Name of the provider.
        
        
        """

        self._api.do('DELETE', f'/api/2.1/unity-catalog/providers/{name}')

    def get(self, name: str) -> ProviderInfo:
        """Get a provider.
        
        Gets a specific authentication provider. The caller must supply the name of the provider, and must
        either be a metastore admin or the owner of the provider.
        
        :param name: str
          Name of the provider.
        
        :returns: :class:`ProviderInfo`
        """

        json = self._api.do('GET', f'/api/2.1/unity-catalog/providers/{name}')
        return ProviderInfo.from_dict(json)

    def list(self, *, data_provider_global_metastore_id: Optional[str] = None) -> Iterator[ProviderInfo]:
        """List providers.
        
        Gets an array of available authentication providers. The caller must either be a metastore admin or
        the owner of the providers. Providers not owned by the caller are not included in the response. There
        is no guarantee of a specific ordering of the elements in the array.
        
        :param data_provider_global_metastore_id: str (optional)
          If not provided, all providers will be returned. If no providers exist with this ID, no results will
          be returned.
        
        :returns: Iterator over :class:`ProviderInfo`
        """

        query = {}
        if data_provider_global_metastore_id is not None:
            query['data_provider_global_metastore_id'] = _validated('data_provider_global_metastore_id', str,
                                                                    data_provider_global_metastore_id)

        json = self._api.do('GET', '/api/2.1/unity-catalog/providers', query=query)
        return [ProviderInfo.from_dict(v) for v in json.get('providers', [])]

    def list_shares(self, name: str) -> Iterator[ProviderShare]:
        """List shares by Provider.
        
        Gets an array of a specified provider's shares within the metastore where:
        
        * the caller is a metastore admin, or * the caller is the owner.
        
        :param name: str
          Name of the provider in which to list shares.
        
        :returns: Iterator over :class:`ProviderShare`
        """

        json = self._api.do('GET', f'/api/2.1/unity-catalog/providers/{name}/shares')
        return [ProviderShare.from_dict(v) for v in json.get('shares', [])]

    def update(self,
               name: str,
               *,
               comment: Optional[str] = None,
               owner: Optional[str] = None,
               recipient_profile_str: Optional[str] = None) -> ProviderInfo:
        """Update a provider.
        
        Updates the information for an authentication provider, if the caller is a metastore admin or is the
        owner of the provider. If the update changes the provider name, the caller must be both a metastore
        admin and the owner of the provider.
        
        :param name: str
          The name of the Provider.
        :param comment: str (optional)
          Description about the provider.
        :param owner: str (optional)
          Username of Provider owner.
        :param recipient_profile_str: str (optional)
          This field is required when the __authentication_type__ is **TOKEN** or not provided.
        
        :returns: :class:`ProviderInfo`
        """
        body = {}
        if comment is not None: body['comment'] = _validated('comment', str, comment)
        if owner is not None: body['owner'] = _validated('owner', str, owner)
        if recipient_profile_str is not None:
            body['recipient_profile_str'] = _validated('recipient_profile_str', str, recipient_profile_str)

        json = self._api.do('PATCH', f'/api/2.1/unity-catalog/providers/{name}', body=body)
        return ProviderInfo.from_dict(json)


class RecipientActivationAPI:
    """The Recipient Activation API is only applicable in the open sharing model where the recipient object has
    the authentication type of `TOKEN`. The data recipient follows the activation link shared by the data
    provider to download the credential file that includes the access token. The recipient will then use the
    credential file to establish a secure connection with the provider to receive the shared data.
    
    Note that you can download the credential file only once. Recipients should treat the downloaded
    credential as a secret and must not share it outside of their organization."""

    def __init__(self, api_client):
        self._api = api_client

    def get_activation_url_info(self, activation_url: str):
        """Get a share activation URL.
        
        Gets an activation URL for a share.
        
        :param activation_url: str
          The one time activation url. It also accepts activation token.
        
        
        """

        self._api.do('GET', f'/api/2.1/unity-catalog/public/data_sharing_activation_info/{activation_url}')

    def retrieve_token(self, activation_url: str) -> RetrieveTokenResponse:
        """Get an access token.
        
        Retrieve access token with an activation url. This is a public API without any authentication.
        
        :param activation_url: str
          The one time activation url. It also accepts activation token.
        
        :returns: :class:`RetrieveTokenResponse`
        """

        json = self._api.do('GET', f'/api/2.1/unity-catalog/public/data_sharing_activation/{activation_url}')
        return RetrieveTokenResponse.from_dict(json)


class RecipientsAPI:
    """A recipient is an object you create using :method:recipients/create to represent an organization which you
    want to allow access shares. The way how sharing works differs depending on whether or not your recipient
    has access to a Databricks workspace that is enabled for Unity Catalog:
    
    - For recipients with access to a Databricks workspace that is enabled for Unity Catalog, you can create a
    recipient object along with a unique sharing identifier you get from the recipient. The sharing identifier
    is the key identifier that enables the secure connection. This sharing mode is called
    **Databricks-to-Databricks sharing**.
    
    - For recipients without access to a Databricks workspace that is enabled for Unity Catalog, when you
    create a recipient object, Databricks generates an activation link you can send to the recipient. The
    recipient follows the activation link to download the credential file, and then uses the credential file
    to establish a secure connection to receive the shared data. This sharing mode is called **open sharing**."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               authentication_type: AuthenticationType,
               *,
               comment: Optional[str] = None,
               data_recipient_global_metastore_id: Optional[Any] = None,
               ip_access_list: Optional[IpAccessList] = None,
               owner: Optional[str] = None,
               properties_kvpairs: Optional[SecurablePropertiesKvPairs] = None,
               sharing_code: Optional[str] = None) -> RecipientInfo:
        """Create a share recipient.
        
        Creates a new recipient with the delta sharing authentication type in the metastore. The caller must
        be a metastore admin or has the **CREATE_RECIPIENT** privilege on the metastore.
        
        :param name: str
          Name of Recipient.
        :param authentication_type: :class:`AuthenticationType`
          The delta sharing authentication type.
        :param comment: str (optional)
          Description about the recipient.
        :param data_recipient_global_metastore_id: Any (optional)
          The global Unity Catalog metastore id provided by the data recipient. This field is required when
          the __authentication_type__ is **DATABRICKS**. The identifier is of format
          __cloud__:__region__:__metastore-uuid__.
        :param ip_access_list: :class:`IpAccessList` (optional)
          IP Access List
        :param owner: str (optional)
          Username of the recipient owner.
        :param properties_kvpairs: :class:`SecurablePropertiesKvPairs` (optional)
          Recipient properties as map of string key-value pairs.
        :param sharing_code: str (optional)
          The one-time sharing code provided by the data recipient. This field is required when the
          __authentication_type__ is **DATABRICKS**.
        
        :returns: :class:`RecipientInfo`
        """
        body = {}
        if authentication_type is not None:
            body['authentication_type'] = _validated('authentication_type', AuthenticationType,
                                                     authentication_type)
        if comment is not None: body['comment'] = _validated('comment', str, comment)
        if data_recipient_global_metastore_id is not None:
            body['data_recipient_global_metastore_id'] = _validated('data_recipient_global_metastore_id', Any,
                                                                    data_recipient_global_metastore_id)
        if ip_access_list is not None:
            body['ip_access_list'] = _validated('ip_access_list', IpAccessList, ip_access_list)
        if name is not None: body['name'] = _validated('name', str, name)
        if owner is not None: body['owner'] = _validated('owner', str, owner)
        if properties_kvpairs is not None:
            body['properties_kvpairs'] = _validated('properties_kvpairs', SecurablePropertiesKvPairs,
                                                    properties_kvpairs)
        if sharing_code is not None: body['sharing_code'] = _validated('sharing_code', str, sharing_code)

        json = self._api.do('POST', '/api/2.1/unity-catalog/recipients', body=body)
        return RecipientInfo.from_dict(json)

    def delete(self, name: str):
        """Delete a share recipient.
        
        Deletes the specified recipient from the metastore. The caller must be the owner of the recipient.
        
        :param name: str
          Name of the recipient.
        
        
        """

        self._api.do('DELETE', f'/api/2.1/unity-catalog/recipients/{name}')

    def get(self, name: str) -> RecipientInfo:
        """Get a share recipient.
        
        Gets a share recipient from the metastore if:
        
        * the caller is the owner of the share recipient, or: * is a metastore admin
        
        :param name: str
          Name of the recipient.
        
        :returns: :class:`RecipientInfo`
        """

        json = self._api.do('GET', f'/api/2.1/unity-catalog/recipients/{name}')
        return RecipientInfo.from_dict(json)

    def list(self, *, data_recipient_global_metastore_id: Optional[str] = None) -> Iterator[RecipientInfo]:
        """List share recipients.
        
        Gets an array of all share recipients within the current metastore where:
        
        * the caller is a metastore admin, or * the caller is the owner. There is no guarantee of a specific
        ordering of the elements in the array.
        
        :param data_recipient_global_metastore_id: str (optional)
          If not provided, all recipients will be returned. If no recipients exist with this ID, no results
          will be returned.
        
        :returns: Iterator over :class:`RecipientInfo`
        """

        query = {}
        if data_recipient_global_metastore_id is not None:
            query['data_recipient_global_metastore_id'] = _validated('data_recipient_global_metastore_id',
                                                                     str, data_recipient_global_metastore_id)

        json = self._api.do('GET', '/api/2.1/unity-catalog/recipients', query=query)
        return [RecipientInfo.from_dict(v) for v in json.get('recipients', [])]

    def rotate_token(self, existing_token_expire_in_seconds: int, name: str) -> RecipientInfo:
        """Rotate a token.
        
        Refreshes the specified recipient's delta sharing authentication token with the provided token info.
        The caller must be the owner of the recipient.
        
        :param existing_token_expire_in_seconds: int
          The expiration time of the bearer token in ISO 8601 format. This will set the expiration_time of
          existing token only to a smaller timestamp, it cannot extend the expiration_time. Use 0 to expire
          the existing token immediately, negative number will return an error.
        :param name: str
          The name of the recipient.
        
        :returns: :class:`RecipientInfo`
        """
        body = {}
        if existing_token_expire_in_seconds is not None:
            body['existing_token_expire_in_seconds'] = _validated('existing_token_expire_in_seconds', int,
                                                                  existing_token_expire_in_seconds)

        json = self._api.do('POST', f'/api/2.1/unity-catalog/recipients/{name}/rotate-token', body=body)
        return RecipientInfo.from_dict(json)

    def share_permissions(self, name: str) -> GetRecipientSharePermissionsResponse:
        """Get recipient share permissions.
        
        Gets the share permissions for the specified Recipient. The caller must be a metastore admin or the
        owner of the Recipient.
        
        :param name: str
          The name of the Recipient.
        
        :returns: :class:`GetRecipientSharePermissionsResponse`
        """

        json = self._api.do('GET', f'/api/2.1/unity-catalog/recipients/{name}/share-permissions')
        return GetRecipientSharePermissionsResponse.from_dict(json)

    def update(self,
               name: str,
               *,
               comment: Optional[str] = None,
               ip_access_list: Optional[IpAccessList] = None,
               owner: Optional[str] = None,
               properties_kvpairs: Optional[SecurablePropertiesKvPairs] = None):
        """Update a share recipient.
        
        Updates an existing recipient in the metastore. The caller must be a metastore admin or the owner of
        the recipient. If the recipient name will be updated, the user must be both a metastore admin and the
        owner of the recipient.
        
        :param name: str
          Name of Recipient.
        :param comment: str (optional)
          Description about the recipient.
        :param ip_access_list: :class:`IpAccessList` (optional)
          IP Access List
        :param owner: str (optional)
          Username of the recipient owner.
        :param properties_kvpairs: :class:`SecurablePropertiesKvPairs` (optional)
          Recipient properties as map of string key-value pairs. When provided in update request, the
          specified properties will override the existing properties. To add and remove properties, one would
          need to perform a read-modify-write.
        
        
        """
        body = {}
        if comment is not None: body['comment'] = _validated('comment', str, comment)
        if ip_access_list is not None:
            body['ip_access_list'] = _validated('ip_access_list', IpAccessList, ip_access_list)
        if owner is not None: body['owner'] = _validated('owner', str, owner)
        if properties_kvpairs is not None:
            body['properties_kvpairs'] = _validated('properties_kvpairs', SecurablePropertiesKvPairs,
                                                    properties_kvpairs)
        self._api.do('PATCH', f'/api/2.1/unity-catalog/recipients/{name}', body=body)


class SharesAPI:
    """A share is a container instantiated with :method:shares/create. Once created you can iteratively register
    a collection of existing data assets defined within the metastore using :method:shares/update. You can
    register data assets under their original name, qualified by their original schema, or provide alternate
    exposed names."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, name: str, *, comment: Optional[str] = None) -> ShareInfo:
        """Create a share.
        
        Creates a new share for data objects. Data objects can be added after creation with **update**. The
        caller must be a metastore admin or have the **CREATE_SHARE** privilege on the metastore.
        
        :param name: str
          Name of the share.
        :param comment: str (optional)
          User-provided free-form text description.
        
        :returns: :class:`ShareInfo`
        """
        body = {}
        if comment is not None: body['comment'] = _validated('comment', str, comment)
        if name is not None: body['name'] = _validated('name', str, name)

        json = self._api.do('POST', '/api/2.1/unity-catalog/shares', body=body)
        return ShareInfo.from_dict(json)

    def delete(self, name: str):
        """Delete a share.
        
        Deletes a data object share from the metastore. The caller must be an owner of the share.
        
        :param name: str
          The name of the share.
        
        
        """

        self._api.do('DELETE', f'/api/2.1/unity-catalog/shares/{name}')

    def get(self, name: str, *, include_shared_data: Optional[bool] = None) -> ShareInfo:
        """Get a share.
        
        Gets a data object share from the metastore. The caller must be a metastore admin or the owner of the
        share.
        
        :param name: str
          The name of the share.
        :param include_shared_data: bool (optional)
          Query for data to include in the share.
        
        :returns: :class:`ShareInfo`
        """

        query = {}
        if include_shared_data is not None:
            query['include_shared_data'] = _validated('include_shared_data', bool, include_shared_data)

        json = self._api.do('GET', f'/api/2.1/unity-catalog/shares/{name}', query=query)
        return ShareInfo.from_dict(json)

    def list(self) -> Iterator[ShareInfo]:
        """List shares.
        
        Gets an array of data object shares from the metastore. The caller must be a metastore admin or the
        owner of the share. There is no guarantee of a specific ordering of the elements in the array.
        
        :returns: Iterator over :class:`ShareInfo`
        """

        json = self._api.do('GET', '/api/2.1/unity-catalog/shares')
        return [ShareInfo.from_dict(v) for v in json.get('shares', [])]

    def share_permissions(self, name: str) -> catalog.PermissionsList:
        """Get permissions.
        
        Gets the permissions for a data share from the metastore. The caller must be a metastore admin or the
        owner of the share.
        
        :param name: str
          The name of the share.
        
        :returns: :class:`PermissionsList`
        """

        json = self._api.do('GET', f'/api/2.1/unity-catalog/shares/{name}/permissions')
        return PermissionsList.from_dict(json)

    def update(self,
               name: str,
               *,
               comment: Optional[str] = None,
               owner: Optional[str] = None,
               updates: Optional[List[SharedDataObjectUpdate]] = None) -> ShareInfo:
        """Update a share.
        
        Updates the share with the changes and data objects in the request. The caller must be the owner of
        the share or a metastore admin.
        
        When the caller is a metastore admin, only the __owner__ field can be updated.
        
        In the case that the share name is changed, **updateShare** requires that the caller is both the share
        owner and a metastore admin.
        
        For each table that is added through this method, the share owner must also have **SELECT** privilege
        on the table. This privilege must be maintained indefinitely for recipients to be able to access the
        table. Typically, you should use a group as the share owner.
        
        Table removals through **update** do not require additional privileges.
        
        :param name: str
          Name of the share.
        :param comment: str (optional)
          User-provided free-form text description.
        :param owner: str (optional)
          Username of current owner of share.
        :param updates: List[:class:`SharedDataObjectUpdate`] (optional)
          Array of shared data object updates.
        
        :returns: :class:`ShareInfo`
        """
        body = {}
        if comment is not None: body['comment'] = _validated('comment', str, comment)
        if owner is not None: body['owner'] = _validated('owner', str, owner)
        if updates is not None:
            body['updates'] = [_validated('updates item', SharedDataObjectUpdate, v) for v in updates]

        json = self._api.do('PATCH', f'/api/2.1/unity-catalog/shares/{name}', body=body)
        return ShareInfo.from_dict(json)

    def update_permissions(self, name: str, *, changes: Optional[List[catalog.PermissionsChange]] = None):
        """Update permissions.
        
        Updates the permissions for a data share in the metastore. The caller must be a metastore admin or an
        owner of the share.
        
        For new recipient grants, the user must also be the owner of the recipients. recipient revocations do
        not require additional privileges.
        
        :param name: str
          The name of the share.
        :param changes: List[:class:`PermissionsChange`] (optional)
          Array of permission changes.
        
        
        """
        body = {}
        if changes is not None:
            body['changes'] = [_validated('changes item', catalog.PermissionsChange, v) for v in changes]
        self._api.do('PATCH', f'/api/2.1/unity-catalog/shares/{name}/permissions', body=body)

# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List

from ._internal import _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


class AuthenticationType(Enum):
    """The delta sharing authentication type."""

    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'


@dataclass
class AwsIamRole:
    role_arn: str
    external_id: str = None
    unity_catalog_iam_arn: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.external_id: body['external_id'] = self.external_id
        if self.role_arn: body['role_arn'] = self.role_arn
        if self.unity_catalog_iam_arn: body['unity_catalog_iam_arn'] = self.unity_catalog_iam_arn
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AwsIamRole':
        return cls(external_id=d.get('external_id', None),
                   role_arn=d.get('role_arn', None),
                   unity_catalog_iam_arn=d.get('unity_catalog_iam_arn', None))


@dataclass
class AzureServicePrincipal:
    directory_id: str
    application_id: str
    client_secret: str

    def as_dict(self) -> dict:
        body = {}
        if self.application_id: body['application_id'] = self.application_id
        if self.client_secret: body['client_secret'] = self.client_secret
        if self.directory_id: body['directory_id'] = self.directory_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AzureServicePrincipal':
        return cls(application_id=d.get('application_id', None),
                   client_secret=d.get('client_secret', None),
                   directory_id=d.get('directory_id', None))


@dataclass
class CatalogInfo:
    catalog_type: 'CatalogType' = None
    comment: str = None
    created_at: int = None
    created_by: str = None
    effective_auto_maintenance_flag: 'EffectiveAutoMaintenanceFlag' = None
    enable_auto_maintenance: 'EnableAutoMaintenance' = None
    metastore_id: str = None
    name: str = None
    owner: str = None
    properties: 'Dict[str,str]' = None
    provider_name: str = None
    share_name: str = None
    storage_location: str = None
    storage_root: str = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.catalog_type: body['catalog_type'] = self.catalog_type.value
        if self.comment: body['comment'] = self.comment
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.effective_auto_maintenance_flag:
            body['effective_auto_maintenance_flag'] = self.effective_auto_maintenance_flag.as_dict()
        if self.enable_auto_maintenance: body['enable_auto_maintenance'] = self.enable_auto_maintenance.value
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.properties: body['properties'] = self.properties
        if self.provider_name: body['provider_name'] = self.provider_name
        if self.share_name: body['share_name'] = self.share_name
        if self.storage_location: body['storage_location'] = self.storage_location
        if self.storage_root: body['storage_root'] = self.storage_root
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CatalogInfo':
        return cls(catalog_type=_enum(d, 'catalog_type', CatalogType),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   effective_auto_maintenance_flag=_from_dict(d, 'effective_auto_maintenance_flag',
                                                              EffectiveAutoMaintenanceFlag),
                   enable_auto_maintenance=_enum(d, 'enable_auto_maintenance', EnableAutoMaintenance),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   properties=d.get('properties', None),
                   provider_name=d.get('provider_name', None),
                   share_name=d.get('share_name', None),
                   storage_location=d.get('storage_location', None),
                   storage_root=d.get('storage_root', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


class CatalogType(Enum):
    """The type of the catalog."""

    DELTASHARING_CATALOG = 'DELTASHARING_CATALOG'
    MANAGED_CATALOG = 'MANAGED_CATALOG'
    SYSTEM_CATALOG = 'SYSTEM_CATALOG'


@dataclass
class ColumnInfo:
    comment: str = None
    mask: 'ColumnMask' = None
    name: str = None
    nullable: bool = None
    partition_index: int = None
    position: int = None
    type_interval_type: str = None
    type_json: str = None
    type_name: 'ColumnTypeName' = None
    type_precision: int = None
    type_scale: int = None
    type_text: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.mask: body['mask'] = self.mask.as_dict()
        if self.name: body['name'] = self.name
        if self.nullable: body['nullable'] = self.nullable
        if self.partition_index: body['partition_index'] = self.partition_index
        if self.position: body['position'] = self.position
        if self.type_interval_type: body['type_interval_type'] = self.type_interval_type
        if self.type_json: body['type_json'] = self.type_json
        if self.type_name: body['type_name'] = self.type_name.value
        if self.type_precision: body['type_precision'] = self.type_precision
        if self.type_scale: body['type_scale'] = self.type_scale
        if self.type_text: body['type_text'] = self.type_text
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
    function_name: str = None
    using_column_names: 'List[str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.function_name: body['function_name'] = self.function_name
        if self.using_column_names: body['using_column_names'] = [v for v in self.using_column_names]
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
class CreateCatalog:
    name: str
    comment: str = None
    properties: 'Dict[str,str]' = None
    provider_name: str = None
    share_name: str = None
    storage_root: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.name: body['name'] = self.name
        if self.properties: body['properties'] = self.properties
        if self.provider_name: body['provider_name'] = self.provider_name
        if self.share_name: body['share_name'] = self.share_name
        if self.storage_root: body['storage_root'] = self.storage_root
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCatalog':
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   properties=d.get('properties', None),
                   provider_name=d.get('provider_name', None),
                   share_name=d.get('share_name', None),
                   storage_root=d.get('storage_root', None))


@dataclass
class CreateExternalLocation:
    name: str
    url: str
    credential_name: str
    comment: str = None
    read_only: bool = None
    skip_validation: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.credential_name: body['credential_name'] = self.credential_name
        if self.name: body['name'] = self.name
        if self.read_only: body['read_only'] = self.read_only
        if self.skip_validation: body['skip_validation'] = self.skip_validation
        if self.url: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateExternalLocation':
        return cls(comment=d.get('comment', None),
                   credential_name=d.get('credential_name', None),
                   name=d.get('name', None),
                   read_only=d.get('read_only', None),
                   skip_validation=d.get('skip_validation', None),
                   url=d.get('url', None))


@dataclass
class CreateFunction:
    name: str
    catalog_name: str
    schema_name: str
    input_params: 'List[FunctionParameterInfo]'
    data_type: 'ColumnTypeName'
    full_data_type: str
    return_params: 'List[FunctionParameterInfo]'
    routine_body: 'CreateFunctionRoutineBody'
    routine_definition: str
    routine_dependencies: 'List[Dependency]'
    parameter_style: 'CreateFunctionParameterStyle'
    is_deterministic: bool
    sql_data_access: 'CreateFunctionSqlDataAccess'
    is_null_call: bool
    security_type: 'CreateFunctionSecurityType'
    specific_name: str
    comment: str = None
    external_language: str = None
    external_name: str = None
    properties: 'Dict[str,str]' = None
    sql_path: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.catalog_name: body['catalog_name'] = self.catalog_name
        if self.comment: body['comment'] = self.comment
        if self.data_type: body['data_type'] = self.data_type.value
        if self.external_language: body['external_language'] = self.external_language
        if self.external_name: body['external_name'] = self.external_name
        if self.full_data_type: body['full_data_type'] = self.full_data_type
        if self.input_params: body['input_params'] = [v.as_dict() for v in self.input_params]
        if self.is_deterministic: body['is_deterministic'] = self.is_deterministic
        if self.is_null_call: body['is_null_call'] = self.is_null_call
        if self.name: body['name'] = self.name
        if self.parameter_style: body['parameter_style'] = self.parameter_style.value
        if self.properties: body['properties'] = self.properties
        if self.return_params: body['return_params'] = [v.as_dict() for v in self.return_params]
        if self.routine_body: body['routine_body'] = self.routine_body.value
        if self.routine_definition: body['routine_definition'] = self.routine_definition
        if self.routine_dependencies:
            body['routine_dependencies'] = [v.as_dict() for v in self.routine_dependencies]
        if self.schema_name: body['schema_name'] = self.schema_name
        if self.security_type: body['security_type'] = self.security_type.value
        if self.specific_name: body['specific_name'] = self.specific_name
        if self.sql_data_access: body['sql_data_access'] = self.sql_data_access.value
        if self.sql_path: body['sql_path'] = self.sql_path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateFunction':
        return cls(catalog_name=d.get('catalog_name', None),
                   comment=d.get('comment', None),
                   data_type=_enum(d, 'data_type', ColumnTypeName),
                   external_language=d.get('external_language', None),
                   external_name=d.get('external_name', None),
                   full_data_type=d.get('full_data_type', None),
                   input_params=_repeated(d, 'input_params', FunctionParameterInfo),
                   is_deterministic=d.get('is_deterministic', None),
                   is_null_call=d.get('is_null_call', None),
                   name=d.get('name', None),
                   parameter_style=_enum(d, 'parameter_style', CreateFunctionParameterStyle),
                   properties=d.get('properties', None),
                   return_params=_repeated(d, 'return_params', FunctionParameterInfo),
                   routine_body=_enum(d, 'routine_body', CreateFunctionRoutineBody),
                   routine_definition=d.get('routine_definition', None),
                   routine_dependencies=_repeated(d, 'routine_dependencies', Dependency),
                   schema_name=d.get('schema_name', None),
                   security_type=_enum(d, 'security_type', CreateFunctionSecurityType),
                   specific_name=d.get('specific_name', None),
                   sql_data_access=_enum(d, 'sql_data_access', CreateFunctionSqlDataAccess),
                   sql_path=d.get('sql_path', None))


class CreateFunctionParameterStyle(Enum):
    """Function parameter style. **S** is the value for SQL."""

    S = 'S'


class CreateFunctionRoutineBody(Enum):
    """Function language. When **EXTERNAL** is used, the language of the routine function should be
    specified in the __external_language__ field, and the __return_params__ of the function cannot
    be used (as **TABLE** return type is not supported), and the __sql_data_access__ field must be
    **NO_SQL**."""

    EXTERNAL = 'EXTERNAL'
    SQL = 'SQL'


class CreateFunctionSecurityType(Enum):
    """Function security type."""

    DEFINER = 'DEFINER'


class CreateFunctionSqlDataAccess(Enum):
    """Function SQL data access."""

    CONTAINS_SQL = 'CONTAINS_SQL'
    NO_SQL = 'NO_SQL'
    READS_SQL_DATA = 'READS_SQL_DATA'


@dataclass
class CreateMetastore:
    name: str
    storage_root: str
    region: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.name: body['name'] = self.name
        if self.region: body['region'] = self.region
        if self.storage_root: body['storage_root'] = self.storage_root
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateMetastore':
        return cls(name=d.get('name', None),
                   region=d.get('region', None),
                   storage_root=d.get('storage_root', None))


@dataclass
class CreateMetastoreAssignment:
    metastore_id: str
    default_catalog_name: str
    workspace_id: int

    def as_dict(self) -> dict:
        body = {}
        if self.default_catalog_name: body['default_catalog_name'] = self.default_catalog_name
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.workspace_id: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateMetastoreAssignment':
        return cls(default_catalog_name=d.get('default_catalog_name', None),
                   metastore_id=d.get('metastore_id', None),
                   workspace_id=d.get('workspace_id', None))


@dataclass
class CreateProvider:
    name: str
    authentication_type: 'AuthenticationType'
    comment: str = None
    recipient_profile_str: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.authentication_type: body['authentication_type'] = self.authentication_type.value
        if self.comment: body['comment'] = self.comment
        if self.name: body['name'] = self.name
        if self.recipient_profile_str: body['recipient_profile_str'] = self.recipient_profile_str
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
    properties_kvpairs: Any = None
    sharing_code: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.authentication_type: body['authentication_type'] = self.authentication_type.value
        if self.comment: body['comment'] = self.comment
        if self.data_recipient_global_metastore_id:
            body['data_recipient_global_metastore_id'] = self.data_recipient_global_metastore_id
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.properties_kvpairs: body['properties_kvpairs'] = self.properties_kvpairs
        if self.sharing_code: body['sharing_code'] = self.sharing_code
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRecipient':
        return cls(authentication_type=_enum(d, 'authentication_type', AuthenticationType),
                   comment=d.get('comment', None),
                   data_recipient_global_metastore_id=d.get('data_recipient_global_metastore_id', None),
                   ip_access_list=_from_dict(d, 'ip_access_list', IpAccessList),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   properties_kvpairs=d.get('properties_kvpairs', None),
                   sharing_code=d.get('sharing_code', None))


@dataclass
class CreateSchema:
    name: str
    catalog_name: str
    comment: str = None
    properties: 'Dict[str,str]' = None
    storage_root: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.catalog_name: body['catalog_name'] = self.catalog_name
        if self.comment: body['comment'] = self.comment
        if self.name: body['name'] = self.name
        if self.properties: body['properties'] = self.properties
        if self.storage_root: body['storage_root'] = self.storage_root
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateSchema':
        return cls(catalog_name=d.get('catalog_name', None),
                   comment=d.get('comment', None),
                   name=d.get('name', None),
                   properties=d.get('properties', None),
                   storage_root=d.get('storage_root', None))


@dataclass
class CreateShare:
    name: str
    comment: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.name: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateShare':
        return cls(comment=d.get('comment', None), name=d.get('name', None))


@dataclass
class CreateStorageCredential:
    name: str
    metastore_id: str
    aws_iam_role: 'AwsIamRole' = None
    azure_service_principal: 'AzureServicePrincipal' = None
    comment: str = None
    gcp_service_account_key: 'GcpServiceAccountKey' = None
    read_only: bool = None
    skip_validation: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.aws_iam_role: body['aws_iam_role'] = self.aws_iam_role.as_dict()
        if self.azure_service_principal:
            body['azure_service_principal'] = self.azure_service_principal.as_dict()
        if self.comment: body['comment'] = self.comment
        if self.gcp_service_account_key:
            body['gcp_service_account_key'] = self.gcp_service_account_key.as_dict()
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.name: body['name'] = self.name
        if self.read_only: body['read_only'] = self.read_only
        if self.skip_validation: body['skip_validation'] = self.skip_validation
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateStorageCredential':
        return cls(aws_iam_role=_from_dict(d, 'aws_iam_role', AwsIamRole),
                   azure_service_principal=_from_dict(d, 'azure_service_principal', AzureServicePrincipal),
                   comment=d.get('comment', None),
                   gcp_service_account_key=_from_dict(d, 'gcp_service_account_key', GcpServiceAccountKey),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   read_only=d.get('read_only', None),
                   skip_validation=d.get('skip_validation', None))


@dataclass
class CreateTableConstraint:
    full_name_arg: str
    constraint: 'TableConstraint'

    def as_dict(self) -> dict:
        body = {}
        if self.constraint: body['constraint'] = self.constraint.as_dict()
        if self.full_name_arg: body['full_name_arg'] = self.full_name_arg
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateTableConstraint':
        return cls(constraint=_from_dict(d, 'constraint', TableConstraint),
                   full_name_arg=d.get('full_name_arg', None))


class DataSourceFormat(Enum):
    """Data source format"""

    AVRO = 'AVRO'
    CSV = 'CSV'
    DELTA = 'DELTA'
    DELTASHARING = 'DELTASHARING'
    JSON = 'JSON'
    ORC = 'ORC'
    PARQUET = 'PARQUET'
    TEXT = 'TEXT'
    UNITY_CATALOG = 'UNITY_CATALOG'


@dataclass
class DeleteAccountMetastoreAssignmentRequest:
    """Delete a metastore assignment"""

    workspace_id: int
    metastore_id: str


@dataclass
class DeleteAccountMetastoreRequest:
    """Delete a metastore"""

    metastore_id: str


@dataclass
class DeleteCatalogRequest:
    """Delete a catalog"""

    name: str
    force: bool = None


@dataclass
class DeleteExternalLocationRequest:
    """Delete an external location"""

    name: str
    force: bool = None


@dataclass
class DeleteFunctionRequest:
    """Delete a function"""

    name: str
    force: bool = None


@dataclass
class DeleteMetastoreRequest:
    """Delete a metastore"""

    id: str
    force: bool = None


@dataclass
class DeleteProviderRequest:
    """Delete a provider"""

    name: str


@dataclass
class DeleteRecipientRequest:
    """Delete a share recipient"""

    name: str


@dataclass
class DeleteSchemaRequest:
    """Delete a schema"""

    full_name: str


@dataclass
class DeleteShareRequest:
    """Delete a share"""

    name: str


@dataclass
class DeleteStorageCredentialRequest:
    """Delete a credential"""

    name: str
    force: bool = None


@dataclass
class DeleteTableConstraintRequest:
    """Delete a table constraint"""

    full_name: str
    constraint_name: str
    cascade: bool


@dataclass
class DeleteTableRequest:
    """Delete a table"""

    full_name: str


@dataclass
class Dependency:
    """A dependency of a SQL object. Either the __table__ field or the __function__ field must be
    defined."""

    function: 'FunctionDependency' = None
    table: 'TableDependency' = None

    def as_dict(self) -> dict:
        body = {}
        if self.function: body['function'] = self.function.as_dict()
        if self.table: body['table'] = self.table.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Dependency':
        return cls(function=_from_dict(d, 'function', FunctionDependency),
                   table=_from_dict(d, 'table', TableDependency))


@dataclass
class EffectiveAutoMaintenanceFlag:
    value: 'EnableAutoMaintenance'
    inherited_from_name: str = None
    inherited_from_type: 'EffectiveAutoMaintenanceFlagInheritedFromType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.inherited_from_name: body['inherited_from_name'] = self.inherited_from_name
        if self.inherited_from_type: body['inherited_from_type'] = self.inherited_from_type.value
        if self.value: body['value'] = self.value.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EffectiveAutoMaintenanceFlag':
        return cls(inherited_from_name=d.get('inherited_from_name', None),
                   inherited_from_type=_enum(d, 'inherited_from_type',
                                             EffectiveAutoMaintenanceFlagInheritedFromType),
                   value=_enum(d, 'value', EnableAutoMaintenance))


class EffectiveAutoMaintenanceFlagInheritedFromType(Enum):
    """The type of the object from which the flag was inherited. If there was no inheritance, this
    field is left blank."""

    CATALOG = 'CATALOG'
    SCHEMA = 'SCHEMA'


@dataclass
class EffectivePermissionsList:
    privilege_assignments: 'List[EffectivePrivilegeAssignment]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.privilege_assignments:
            body['privilege_assignments'] = [v.as_dict() for v in self.privilege_assignments]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EffectivePermissionsList':
        return cls(privilege_assignments=_repeated(d, 'privilege_assignments', EffectivePrivilegeAssignment))


@dataclass
class EffectivePrivilege:
    inherited_from_name: str = None
    inherited_from_type: 'SecurableType' = None
    privilege: 'Privilege' = None

    def as_dict(self) -> dict:
        body = {}
        if self.inherited_from_name: body['inherited_from_name'] = self.inherited_from_name
        if self.inherited_from_type: body['inherited_from_type'] = self.inherited_from_type.value
        if self.privilege: body['privilege'] = self.privilege.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EffectivePrivilege':
        return cls(inherited_from_name=d.get('inherited_from_name', None),
                   inherited_from_type=_enum(d, 'inherited_from_type', SecurableType),
                   privilege=_enum(d, 'privilege', Privilege))


@dataclass
class EffectivePrivilegeAssignment:
    principal: str = None
    privileges: 'List[EffectivePrivilege]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.principal: body['principal'] = self.principal
        if self.privileges: body['privileges'] = [v.as_dict() for v in self.privileges]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EffectivePrivilegeAssignment':
        return cls(principal=d.get('principal', None),
                   privileges=_repeated(d, 'privileges', EffectivePrivilege))


class EnableAutoMaintenance(Enum):
    """Whether auto maintenance should be enabled for this object and objects under it."""

    DISABLE = 'DISABLE'
    ENABLE = 'ENABLE'
    INHERIT = 'INHERIT'


@dataclass
class ExternalLocationInfo:
    comment: str = None
    created_at: int = None
    created_by: str = None
    credential_id: str = None
    credential_name: str = None
    metastore_id: str = None
    name: str = None
    owner: str = None
    read_only: bool = None
    updated_at: int = None
    updated_by: str = None
    url: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.credential_id: body['credential_id'] = self.credential_id
        if self.credential_name: body['credential_name'] = self.credential_name
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.read_only: body['read_only'] = self.read_only
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
        if self.url: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExternalLocationInfo':
        return cls(comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   credential_id=d.get('credential_id', None),
                   credential_name=d.get('credential_name', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   read_only=d.get('read_only', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None),
                   url=d.get('url', None))


@dataclass
class ForeignKeyConstraint:
    name: str
    child_columns: 'List[str]'
    parent_table: str
    parent_columns: 'List[str]'

    def as_dict(self) -> dict:
        body = {}
        if self.child_columns: body['child_columns'] = [v for v in self.child_columns]
        if self.name: body['name'] = self.name
        if self.parent_columns: body['parent_columns'] = [v for v in self.parent_columns]
        if self.parent_table: body['parent_table'] = self.parent_table
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ForeignKeyConstraint':
        return cls(child_columns=d.get('child_columns', None),
                   name=d.get('name', None),
                   parent_columns=d.get('parent_columns', None),
                   parent_table=d.get('parent_table', None))


@dataclass
class FunctionDependency:
    """A function that is dependent on a SQL object."""

    function_full_name: str

    def as_dict(self) -> dict:
        body = {}
        if self.function_full_name: body['function_full_name'] = self.function_full_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FunctionDependency':
        return cls(function_full_name=d.get('function_full_name', None))


@dataclass
class FunctionInfo:
    catalog_name: str = None
    comment: str = None
    created_at: int = None
    created_by: str = None
    data_type: 'ColumnTypeName' = None
    external_language: str = None
    external_name: str = None
    full_data_type: str = None
    full_name: str = None
    function_id: str = None
    input_params: 'List[FunctionParameterInfo]' = None
    is_deterministic: bool = None
    is_null_call: bool = None
    metastore_id: str = None
    name: str = None
    owner: str = None
    parameter_style: 'FunctionInfoParameterStyle' = None
    properties: 'Dict[str,str]' = None
    return_params: 'List[FunctionParameterInfo]' = None
    routine_body: 'FunctionInfoRoutineBody' = None
    routine_definition: str = None
    routine_dependencies: 'List[Dependency]' = None
    schema_name: str = None
    security_type: 'FunctionInfoSecurityType' = None
    specific_name: str = None
    sql_data_access: 'FunctionInfoSqlDataAccess' = None
    sql_path: str = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.catalog_name: body['catalog_name'] = self.catalog_name
        if self.comment: body['comment'] = self.comment
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.data_type: body['data_type'] = self.data_type.value
        if self.external_language: body['external_language'] = self.external_language
        if self.external_name: body['external_name'] = self.external_name
        if self.full_data_type: body['full_data_type'] = self.full_data_type
        if self.full_name: body['full_name'] = self.full_name
        if self.function_id: body['function_id'] = self.function_id
        if self.input_params: body['input_params'] = [v.as_dict() for v in self.input_params]
        if self.is_deterministic: body['is_deterministic'] = self.is_deterministic
        if self.is_null_call: body['is_null_call'] = self.is_null_call
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.parameter_style: body['parameter_style'] = self.parameter_style.value
        if self.properties: body['properties'] = self.properties
        if self.return_params: body['return_params'] = [v.as_dict() for v in self.return_params]
        if self.routine_body: body['routine_body'] = self.routine_body.value
        if self.routine_definition: body['routine_definition'] = self.routine_definition
        if self.routine_dependencies:
            body['routine_dependencies'] = [v.as_dict() for v in self.routine_dependencies]
        if self.schema_name: body['schema_name'] = self.schema_name
        if self.security_type: body['security_type'] = self.security_type.value
        if self.specific_name: body['specific_name'] = self.specific_name
        if self.sql_data_access: body['sql_data_access'] = self.sql_data_access.value
        if self.sql_path: body['sql_path'] = self.sql_path
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FunctionInfo':
        return cls(catalog_name=d.get('catalog_name', None),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   data_type=_enum(d, 'data_type', ColumnTypeName),
                   external_language=d.get('external_language', None),
                   external_name=d.get('external_name', None),
                   full_data_type=d.get('full_data_type', None),
                   full_name=d.get('full_name', None),
                   function_id=d.get('function_id', None),
                   input_params=_repeated(d, 'input_params', FunctionParameterInfo),
                   is_deterministic=d.get('is_deterministic', None),
                   is_null_call=d.get('is_null_call', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   parameter_style=_enum(d, 'parameter_style', FunctionInfoParameterStyle),
                   properties=d.get('properties', None),
                   return_params=_repeated(d, 'return_params', FunctionParameterInfo),
                   routine_body=_enum(d, 'routine_body', FunctionInfoRoutineBody),
                   routine_definition=d.get('routine_definition', None),
                   routine_dependencies=_repeated(d, 'routine_dependencies', Dependency),
                   schema_name=d.get('schema_name', None),
                   security_type=_enum(d, 'security_type', FunctionInfoSecurityType),
                   specific_name=d.get('specific_name', None),
                   sql_data_access=_enum(d, 'sql_data_access', FunctionInfoSqlDataAccess),
                   sql_path=d.get('sql_path', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


class FunctionInfoParameterStyle(Enum):
    """Function parameter style. **S** is the value for SQL."""

    S = 'S'


class FunctionInfoRoutineBody(Enum):
    """Function language. When **EXTERNAL** is used, the language of the routine function should be
    specified in the __external_language__ field, and the __return_params__ of the function cannot
    be used (as **TABLE** return type is not supported), and the __sql_data_access__ field must be
    **NO_SQL**."""

    EXTERNAL = 'EXTERNAL'
    SQL = 'SQL'


class FunctionInfoSecurityType(Enum):
    """Function security type."""

    DEFINER = 'DEFINER'


class FunctionInfoSqlDataAccess(Enum):
    """Function SQL data access."""

    CONTAINS_SQL = 'CONTAINS_SQL'
    NO_SQL = 'NO_SQL'
    READS_SQL_DATA = 'READS_SQL_DATA'


@dataclass
class FunctionParameterInfo:
    name: str
    type_text: str
    type_name: 'ColumnTypeName'
    position: int
    comment: str = None
    parameter_default: str = None
    parameter_mode: 'FunctionParameterMode' = None
    parameter_type: 'FunctionParameterType' = None
    type_interval_type: str = None
    type_json: str = None
    type_precision: int = None
    type_scale: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.name: body['name'] = self.name
        if self.parameter_default: body['parameter_default'] = self.parameter_default
        if self.parameter_mode: body['parameter_mode'] = self.parameter_mode.value
        if self.parameter_type: body['parameter_type'] = self.parameter_type.value
        if self.position: body['position'] = self.position
        if self.type_interval_type: body['type_interval_type'] = self.type_interval_type
        if self.type_json: body['type_json'] = self.type_json
        if self.type_name: body['type_name'] = self.type_name.value
        if self.type_precision: body['type_precision'] = self.type_precision
        if self.type_scale: body['type_scale'] = self.type_scale
        if self.type_text: body['type_text'] = self.type_text
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FunctionParameterInfo':
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   parameter_default=d.get('parameter_default', None),
                   parameter_mode=_enum(d, 'parameter_mode', FunctionParameterMode),
                   parameter_type=_enum(d, 'parameter_type', FunctionParameterType),
                   position=d.get('position', None),
                   type_interval_type=d.get('type_interval_type', None),
                   type_json=d.get('type_json', None),
                   type_name=_enum(d, 'type_name', ColumnTypeName),
                   type_precision=d.get('type_precision', None),
                   type_scale=d.get('type_scale', None),
                   type_text=d.get('type_text', None))


class FunctionParameterMode(Enum):
    """The mode of the function parameter."""

    IN = 'IN'


class FunctionParameterType(Enum):
    """The type of function parameter."""

    COLUMN = 'COLUMN'
    PARAM = 'PARAM'


@dataclass
class GcpServiceAccountKey:
    email: str
    private_key_id: str
    private_key: str

    def as_dict(self) -> dict:
        body = {}
        if self.email: body['email'] = self.email
        if self.private_key: body['private_key'] = self.private_key
        if self.private_key_id: body['private_key_id'] = self.private_key_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GcpServiceAccountKey':
        return cls(email=d.get('email', None),
                   private_key=d.get('private_key', None),
                   private_key_id=d.get('private_key_id', None))


@dataclass
class GetAccountMetastoreAssignmentRequest:
    """Gets the metastore assignment for a workspace"""

    workspace_id: int


@dataclass
class GetAccountMetastoreRequest:
    """Get a metastore"""

    metastore_id: str


@dataclass
class GetAccountStorageCredentialRequest:
    """Gets the named storage credential"""

    metastore_id: str
    name: str


@dataclass
class GetActivationUrlInfoRequest:
    """Get a share activation URL"""

    activation_url: str


@dataclass
class GetCatalogRequest:
    """Get a catalog"""

    name: str


@dataclass
class GetEffectiveRequest:
    """Get effective permissions"""

    securable_type: 'SecurableType'
    full_name: str
    principal: str = None


@dataclass
class GetExternalLocationRequest:
    """Get an external location"""

    name: str


@dataclass
class GetFunctionRequest:
    """Get a function"""

    name: str


@dataclass
class GetGrantRequest:
    """Get permissions"""

    securable_type: 'SecurableType'
    full_name: str
    principal: str = None


@dataclass
class GetMetastoreRequest:
    """Get a metastore"""

    id: str


@dataclass
class GetMetastoreSummaryResponse:
    cloud: str = None
    created_at: int = None
    created_by: str = None
    default_data_access_config_id: str = None
    delta_sharing_organization_name: str = None
    delta_sharing_recipient_token_lifetime_in_seconds: int = None
    delta_sharing_scope: 'GetMetastoreSummaryResponseDeltaSharingScope' = None
    global_metastore_id: str = None
    metastore_id: str = None
    name: str = None
    owner: str = None
    privilege_model_version: str = None
    region: str = None
    storage_root: str = None
    storage_root_credential_id: str = None
    storage_root_credential_name: str = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.cloud: body['cloud'] = self.cloud
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.default_data_access_config_id:
            body['default_data_access_config_id'] = self.default_data_access_config_id
        if self.delta_sharing_organization_name:
            body['delta_sharing_organization_name'] = self.delta_sharing_organization_name
        if self.delta_sharing_recipient_token_lifetime_in_seconds:
            body[
                'delta_sharing_recipient_token_lifetime_in_seconds'] = self.delta_sharing_recipient_token_lifetime_in_seconds
        if self.delta_sharing_scope: body['delta_sharing_scope'] = self.delta_sharing_scope.value
        if self.global_metastore_id: body['global_metastore_id'] = self.global_metastore_id
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.privilege_model_version: body['privilege_model_version'] = self.privilege_model_version
        if self.region: body['region'] = self.region
        if self.storage_root: body['storage_root'] = self.storage_root
        if self.storage_root_credential_id:
            body['storage_root_credential_id'] = self.storage_root_credential_id
        if self.storage_root_credential_name:
            body['storage_root_credential_name'] = self.storage_root_credential_name
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetMetastoreSummaryResponse':
        return cls(cloud=d.get('cloud', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   default_data_access_config_id=d.get('default_data_access_config_id', None),
                   delta_sharing_organization_name=d.get('delta_sharing_organization_name', None),
                   delta_sharing_recipient_token_lifetime_in_seconds=d.get(
                       'delta_sharing_recipient_token_lifetime_in_seconds', None),
                   delta_sharing_scope=_enum(d, 'delta_sharing_scope',
                                             GetMetastoreSummaryResponseDeltaSharingScope),
                   global_metastore_id=d.get('global_metastore_id', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   privilege_model_version=d.get('privilege_model_version', None),
                   region=d.get('region', None),
                   storage_root=d.get('storage_root', None),
                   storage_root_credential_id=d.get('storage_root_credential_id', None),
                   storage_root_credential_name=d.get('storage_root_credential_name', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


class GetMetastoreSummaryResponseDeltaSharingScope(Enum):
    """The scope of Delta Sharing enabled for the metastore."""

    INTERNAL = 'INTERNAL'
    INTERNAL_AND_EXTERNAL = 'INTERNAL_AND_EXTERNAL'


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
class GetSchemaRequest:
    """Get a schema"""

    full_name: str


@dataclass
class GetShareRequest:
    """Get a share"""

    name: str
    include_shared_data: bool = None


@dataclass
class GetStorageCredentialRequest:
    """Get a credential"""

    name: str


@dataclass
class GetTableRequest:
    """Get a table"""

    full_name: str
    include_delta_metadata: bool = None


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
class ListAccountMetastoreAssignmentsRequest:
    """Get all workspaces assigned to a metastore"""

    metastore_id: str


@dataclass
class ListAccountStorageCredentialsRequest:
    """Get all storage credentials assigned to a metastore"""

    metastore_id: str


@dataclass
class ListCatalogsResponse:
    catalogs: 'List[CatalogInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.catalogs: body['catalogs'] = [v.as_dict() for v in self.catalogs]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListCatalogsResponse':
        return cls(catalogs=_repeated(d, 'catalogs', CatalogInfo))


@dataclass
class ListExternalLocationsResponse:
    external_locations: 'List[ExternalLocationInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.external_locations:
            body['external_locations'] = [v.as_dict() for v in self.external_locations]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListExternalLocationsResponse':
        return cls(external_locations=_repeated(d, 'external_locations', ExternalLocationInfo))


@dataclass
class ListFunctionsRequest:
    """List functions"""

    catalog_name: str
    schema_name: str


@dataclass
class ListFunctionsResponse:
    schemas: 'List[FunctionInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.schemas: body['schemas'] = [v.as_dict() for v in self.schemas]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListFunctionsResponse':
        return cls(schemas=_repeated(d, 'schemas', FunctionInfo))


@dataclass
class ListMetastoresResponse:
    metastores: 'List[MetastoreInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.metastores: body['metastores'] = [v.as_dict() for v in self.metastores]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListMetastoresResponse':
        return cls(metastores=_repeated(d, 'metastores', MetastoreInfo))


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
class ListSchemasRequest:
    """List schemas"""

    catalog_name: str


@dataclass
class ListSchemasResponse:
    schemas: 'List[SchemaInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.schemas: body['schemas'] = [v.as_dict() for v in self.schemas]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListSchemasResponse':
        return cls(schemas=_repeated(d, 'schemas', SchemaInfo))


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
class ListSummariesRequest:
    """List table summaries"""

    catalog_name: str
    max_results: int = None
    page_token: str = None
    schema_name_pattern: str = None
    table_name_pattern: str = None


@dataclass
class ListTableSummariesResponse:
    next_page_token: str = None
    tables: 'List[TableSummary]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.tables: body['tables'] = [v.as_dict() for v in self.tables]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListTableSummariesResponse':
        return cls(next_page_token=d.get('next_page_token', None),
                   tables=_repeated(d, 'tables', TableSummary))


@dataclass
class ListTablesRequest:
    """List tables"""

    catalog_name: str
    schema_name: str
    include_delta_metadata: bool = None


@dataclass
class ListTablesResponse:
    tables: 'List[TableInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.tables: body['tables'] = [v.as_dict() for v in self.tables]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListTablesResponse':
        return cls(tables=_repeated(d, 'tables', TableInfo))


@dataclass
class MetastoreAssignment:
    metastore_id: str
    workspace_id: str
    default_catalog_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.default_catalog_name: body['default_catalog_name'] = self.default_catalog_name
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.workspace_id: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'MetastoreAssignment':
        return cls(default_catalog_name=d.get('default_catalog_name', None),
                   metastore_id=d.get('metastore_id', None),
                   workspace_id=d.get('workspace_id', None))


@dataclass
class MetastoreInfo:
    cloud: str = None
    created_at: int = None
    created_by: str = None
    default_data_access_config_id: str = None
    delta_sharing_organization_name: str = None
    delta_sharing_recipient_token_lifetime_in_seconds: int = None
    delta_sharing_scope: 'MetastoreInfoDeltaSharingScope' = None
    global_metastore_id: str = None
    metastore_id: str = None
    name: str = None
    owner: str = None
    privilege_model_version: str = None
    region: str = None
    storage_root: str = None
    storage_root_credential_id: str = None
    storage_root_credential_name: str = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.cloud: body['cloud'] = self.cloud
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.default_data_access_config_id:
            body['default_data_access_config_id'] = self.default_data_access_config_id
        if self.delta_sharing_organization_name:
            body['delta_sharing_organization_name'] = self.delta_sharing_organization_name
        if self.delta_sharing_recipient_token_lifetime_in_seconds:
            body[
                'delta_sharing_recipient_token_lifetime_in_seconds'] = self.delta_sharing_recipient_token_lifetime_in_seconds
        if self.delta_sharing_scope: body['delta_sharing_scope'] = self.delta_sharing_scope.value
        if self.global_metastore_id: body['global_metastore_id'] = self.global_metastore_id
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.privilege_model_version: body['privilege_model_version'] = self.privilege_model_version
        if self.region: body['region'] = self.region
        if self.storage_root: body['storage_root'] = self.storage_root
        if self.storage_root_credential_id:
            body['storage_root_credential_id'] = self.storage_root_credential_id
        if self.storage_root_credential_name:
            body['storage_root_credential_name'] = self.storage_root_credential_name
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'MetastoreInfo':
        return cls(cloud=d.get('cloud', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   default_data_access_config_id=d.get('default_data_access_config_id', None),
                   delta_sharing_organization_name=d.get('delta_sharing_organization_name', None),
                   delta_sharing_recipient_token_lifetime_in_seconds=d.get(
                       'delta_sharing_recipient_token_lifetime_in_seconds', None),
                   delta_sharing_scope=_enum(d, 'delta_sharing_scope', MetastoreInfoDeltaSharingScope),
                   global_metastore_id=d.get('global_metastore_id', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   privilege_model_version=d.get('privilege_model_version', None),
                   region=d.get('region', None),
                   storage_root=d.get('storage_root', None),
                   storage_root_credential_id=d.get('storage_root_credential_id', None),
                   storage_root_credential_name=d.get('storage_root_credential_name', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


class MetastoreInfoDeltaSharingScope(Enum):
    """The scope of Delta Sharing enabled for the metastore."""

    INTERNAL = 'INTERNAL'
    INTERNAL_AND_EXTERNAL = 'INTERNAL_AND_EXTERNAL'


@dataclass
class NamedTableConstraint:
    name: str

    def as_dict(self) -> dict:
        body = {}
        if self.name: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NamedTableConstraint':
        return cls(name=d.get('name', None))


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
        if self.name: body['name'] = self.name
        if self.op: body['op'] = self.op.value
        if self.recipient_property_key: body['recipient_property_key'] = self.recipient_property_key
        if self.value: body['value'] = self.value
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


@dataclass
class PermissionsChange:
    add: 'List[Privilege]' = None
    principal: str = None
    remove: 'List[Privilege]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.add: body['add'] = [v for v in self.add]
        if self.principal: body['principal'] = self.principal
        if self.remove: body['remove'] = [v for v in self.remove]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermissionsChange':
        return cls(add=d.get('add', None), principal=d.get('principal', None), remove=d.get('remove', None))


@dataclass
class PermissionsList:
    privilege_assignments: 'List[PrivilegeAssignment]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.privilege_assignments:
            body['privilege_assignments'] = [v.as_dict() for v in self.privilege_assignments]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermissionsList':
        return cls(privilege_assignments=_repeated(d, 'privilege_assignments', PrivilegeAssignment))


@dataclass
class PrimaryKeyConstraint:
    name: str
    child_columns: 'List[str]'

    def as_dict(self) -> dict:
        body = {}
        if self.child_columns: body['child_columns'] = [v for v in self.child_columns]
        if self.name: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PrimaryKeyConstraint':
        return cls(child_columns=d.get('child_columns', None), name=d.get('name', None))


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
        if self.principal: body['principal'] = self.principal
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
        if self.authentication_type: body['authentication_type'] = self.authentication_type.value
        if self.cloud: body['cloud'] = self.cloud
        if self.comment: body['comment'] = self.comment
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.data_provider_global_metastore_id:
            body['data_provider_global_metastore_id'] = self.data_provider_global_metastore_id
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.recipient_profile: body['recipient_profile'] = self.recipient_profile.as_dict()
        if self.recipient_profile_str: body['recipient_profile_str'] = self.recipient_profile_str
        if self.region: body['region'] = self.region
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
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
        if self.name: body['name'] = self.name
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
    properties_kvpairs: Any = None
    region: str = None
    sharing_code: str = None
    tokens: 'List[RecipientTokenInfo]' = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.activated: body['activated'] = self.activated
        if self.activation_url: body['activation_url'] = self.activation_url
        if self.authentication_type: body['authentication_type'] = self.authentication_type.value
        if self.cloud: body['cloud'] = self.cloud
        if self.comment: body['comment'] = self.comment
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.data_recipient_global_metastore_id:
            body['data_recipient_global_metastore_id'] = self.data_recipient_global_metastore_id
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.properties_kvpairs: body['properties_kvpairs'] = self.properties_kvpairs
        if self.region: body['region'] = self.region
        if self.sharing_code: body['sharing_code'] = self.sharing_code
        if self.tokens: body['tokens'] = [v.as_dict() for v in self.tokens]
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
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
                   properties_kvpairs=d.get('properties_kvpairs', None),
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
        if self.bearer_token: body['bearer_token'] = self.bearer_token
        if self.endpoint: body['endpoint'] = self.endpoint
        if self.share_credentials_version: body['share_credentials_version'] = self.share_credentials_version
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
        if self.activation_url: body['activation_url'] = self.activation_url
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.expiration_time: body['expiration_time'] = self.expiration_time
        if self.id: body['id'] = self.id
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
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
        if self.bearer_token: body['bearerToken'] = self.bearer_token
        if self.endpoint: body['endpoint'] = self.endpoint
        if self.expiration_time: body['expirationTime'] = self.expiration_time
        if self.share_credentials_version: body['shareCredentialsVersion'] = self.share_credentials_version
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
    name: str

    def as_dict(self) -> dict:
        body = {}
        if self.existing_token_expire_in_seconds:
            body['existing_token_expire_in_seconds'] = self.existing_token_expire_in_seconds
        if self.name: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RotateRecipientToken':
        return cls(existing_token_expire_in_seconds=d.get('existing_token_expire_in_seconds', None),
                   name=d.get('name', None))


@dataclass
class SchemaInfo:
    catalog_name: str = None
    catalog_type: str = None
    comment: str = None
    created_at: int = None
    created_by: str = None
    effective_auto_maintenance_flag: 'EffectiveAutoMaintenanceFlag' = None
    enable_auto_maintenance: 'EnableAutoMaintenance' = None
    full_name: str = None
    metastore_id: str = None
    name: str = None
    owner: str = None
    properties: 'Dict[str,str]' = None
    storage_location: str = None
    storage_root: str = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.catalog_name: body['catalog_name'] = self.catalog_name
        if self.catalog_type: body['catalog_type'] = self.catalog_type
        if self.comment: body['comment'] = self.comment
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.effective_auto_maintenance_flag:
            body['effective_auto_maintenance_flag'] = self.effective_auto_maintenance_flag.as_dict()
        if self.enable_auto_maintenance: body['enable_auto_maintenance'] = self.enable_auto_maintenance.value
        if self.full_name: body['full_name'] = self.full_name
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.properties: body['properties'] = self.properties
        if self.storage_location: body['storage_location'] = self.storage_location
        if self.storage_root: body['storage_root'] = self.storage_root
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SchemaInfo':
        return cls(catalog_name=d.get('catalog_name', None),
                   catalog_type=d.get('catalog_type', None),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   effective_auto_maintenance_flag=_from_dict(d, 'effective_auto_maintenance_flag',
                                                              EffectiveAutoMaintenanceFlag),
                   enable_auto_maintenance=_enum(d, 'enable_auto_maintenance', EnableAutoMaintenance),
                   full_name=d.get('full_name', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   properties=d.get('properties', None),
                   storage_location=d.get('storage_location', None),
                   storage_root=d.get('storage_root', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


SecurablePropertiesMap = Dict[str, str]


class SecurableType(Enum):
    """The type of Unity Catalog securable"""

    CATALOG = 'CATALOG'
    EXTERNAL_LOCATION = 'EXTERNAL_LOCATION'
    FUNCTION = 'FUNCTION'
    METASTORE = 'METASTORE'
    PROVIDER = 'PROVIDER'
    RECIPIENT = 'RECIPIENT'
    SCHEMA = 'SCHEMA'
    SHARE = 'SHARE'
    STORAGE_CREDENTIAL = 'STORAGE_CREDENTIAL'
    TABLE = 'TABLE'


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
        if self.comment: body['comment'] = self.comment
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.name: body['name'] = self.name
        if self.objects: body['objects'] = [v.as_dict() for v in self.objects]
        if self.owner: body['owner'] = self.owner
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
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
        if self.share_name: body['share_name'] = self.share_name
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
        if self.added_at: body['added_at'] = self.added_at
        if self.added_by: body['added_by'] = self.added_by
        if self.cdf_enabled: body['cdf_enabled'] = self.cdf_enabled
        if self.comment: body['comment'] = self.comment
        if self.data_object_type: body['data_object_type'] = self.data_object_type
        if self.name: body['name'] = self.name
        if self.partitions: body['partitions'] = [v.as_dict() for v in self.partitions]
        if self.shared_as: body['shared_as'] = self.shared_as
        if self.start_version: body['start_version'] = self.start_version
        if self.status: body['status'] = self.status.value
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
        if self.action: body['action'] = self.action.value
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
class StorageCredentialInfo:
    aws_iam_role: 'AwsIamRole' = None
    azure_service_principal: 'AzureServicePrincipal' = None
    comment: str = None
    created_at: int = None
    created_by: str = None
    gcp_service_account_key: 'GcpServiceAccountKey' = None
    id: str = None
    metastore_id: str = None
    name: str = None
    owner: str = None
    read_only: bool = None
    updated_at: int = None
    updated_by: str = None
    used_for_managed_storage: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.aws_iam_role: body['aws_iam_role'] = self.aws_iam_role.as_dict()
        if self.azure_service_principal:
            body['azure_service_principal'] = self.azure_service_principal.as_dict()
        if self.comment: body['comment'] = self.comment
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.gcp_service_account_key:
            body['gcp_service_account_key'] = self.gcp_service_account_key.as_dict()
        if self.id: body['id'] = self.id
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.read_only: body['read_only'] = self.read_only
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
        if self.used_for_managed_storage: body['used_for_managed_storage'] = self.used_for_managed_storage
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StorageCredentialInfo':
        return cls(aws_iam_role=_from_dict(d, 'aws_iam_role', AwsIamRole),
                   azure_service_principal=_from_dict(d, 'azure_service_principal', AzureServicePrincipal),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   gcp_service_account_key=_from_dict(d, 'gcp_service_account_key', GcpServiceAccountKey),
                   id=d.get('id', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   read_only=d.get('read_only', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None),
                   used_for_managed_storage=d.get('used_for_managed_storage', None))


@dataclass
class TableConstraint:
    """A table constraint, as defined by *one* of the following fields being set:
    __primary_key_constraint__, __foreign_key_constraint__, __named_table_constraint__."""

    foreign_key_constraint: 'ForeignKeyConstraint' = None
    named_table_constraint: 'NamedTableConstraint' = None
    primary_key_constraint: 'PrimaryKeyConstraint' = None

    def as_dict(self) -> dict:
        body = {}
        if self.foreign_key_constraint: body['foreign_key_constraint'] = self.foreign_key_constraint.as_dict()
        if self.named_table_constraint: body['named_table_constraint'] = self.named_table_constraint.as_dict()
        if self.primary_key_constraint: body['primary_key_constraint'] = self.primary_key_constraint.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TableConstraint':
        return cls(foreign_key_constraint=_from_dict(d, 'foreign_key_constraint', ForeignKeyConstraint),
                   named_table_constraint=_from_dict(d, 'named_table_constraint', NamedTableConstraint),
                   primary_key_constraint=_from_dict(d, 'primary_key_constraint', PrimaryKeyConstraint))


@dataclass
class TableConstraintList:
    table_constraints: 'List[TableConstraint]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.table_constraints: body['table_constraints'] = [v.as_dict() for v in self.table_constraints]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TableConstraintList':
        return cls(table_constraints=_repeated(d, 'table_constraints', TableConstraint))


@dataclass
class TableDependency:
    """A table that is dependent on a SQL object."""

    table_full_name: str

    def as_dict(self) -> dict:
        body = {}
        if self.table_full_name: body['table_full_name'] = self.table_full_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TableDependency':
        return cls(table_full_name=d.get('table_full_name', None))


@dataclass
class TableInfo:
    catalog_name: str = None
    columns: 'List[ColumnInfo]' = None
    comment: str = None
    created_at: int = None
    created_by: str = None
    data_access_configuration_id: str = None
    data_source_format: 'DataSourceFormat' = None
    deleted_at: int = None
    delta_runtime_properties_kvpairs: Any = None
    effective_auto_maintenance_flag: 'EffectiveAutoMaintenanceFlag' = None
    enable_auto_maintenance: 'EnableAutoMaintenance' = None
    full_name: str = None
    metastore_id: str = None
    name: str = None
    owner: str = None
    properties: 'Dict[str,str]' = None
    row_filter: 'TableRowFilter' = None
    schema_name: str = None
    sql_path: str = None
    storage_credential_name: str = None
    storage_location: str = None
    table_constraints: 'TableConstraintList' = None
    table_id: str = None
    table_type: 'TableType' = None
    updated_at: int = None
    updated_by: str = None
    view_definition: str = None
    view_dependencies: 'List[Dependency]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.catalog_name: body['catalog_name'] = self.catalog_name
        if self.columns: body['columns'] = [v.as_dict() for v in self.columns]
        if self.comment: body['comment'] = self.comment
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.data_access_configuration_id:
            body['data_access_configuration_id'] = self.data_access_configuration_id
        if self.data_source_format: body['data_source_format'] = self.data_source_format.value
        if self.deleted_at: body['deleted_at'] = self.deleted_at
        if self.delta_runtime_properties_kvpairs:
            body['delta_runtime_properties_kvpairs'] = self.delta_runtime_properties_kvpairs
        if self.effective_auto_maintenance_flag:
            body['effective_auto_maintenance_flag'] = self.effective_auto_maintenance_flag.as_dict()
        if self.enable_auto_maintenance: body['enable_auto_maintenance'] = self.enable_auto_maintenance.value
        if self.full_name: body['full_name'] = self.full_name
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.properties: body['properties'] = self.properties
        if self.row_filter: body['row_filter'] = self.row_filter.as_dict()
        if self.schema_name: body['schema_name'] = self.schema_name
        if self.sql_path: body['sql_path'] = self.sql_path
        if self.storage_credential_name: body['storage_credential_name'] = self.storage_credential_name
        if self.storage_location: body['storage_location'] = self.storage_location
        if self.table_constraints: body['table_constraints'] = self.table_constraints.as_dict()
        if self.table_id: body['table_id'] = self.table_id
        if self.table_type: body['table_type'] = self.table_type.value
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
        if self.view_definition: body['view_definition'] = self.view_definition
        if self.view_dependencies: body['view_dependencies'] = [v.as_dict() for v in self.view_dependencies]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TableInfo':
        return cls(catalog_name=d.get('catalog_name', None),
                   columns=_repeated(d, 'columns', ColumnInfo),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   data_access_configuration_id=d.get('data_access_configuration_id', None),
                   data_source_format=_enum(d, 'data_source_format', DataSourceFormat),
                   deleted_at=d.get('deleted_at', None),
                   delta_runtime_properties_kvpairs=d.get('delta_runtime_properties_kvpairs', None),
                   effective_auto_maintenance_flag=_from_dict(d, 'effective_auto_maintenance_flag',
                                                              EffectiveAutoMaintenanceFlag),
                   enable_auto_maintenance=_enum(d, 'enable_auto_maintenance', EnableAutoMaintenance),
                   full_name=d.get('full_name', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   properties=d.get('properties', None),
                   row_filter=_from_dict(d, 'row_filter', TableRowFilter),
                   schema_name=d.get('schema_name', None),
                   sql_path=d.get('sql_path', None),
                   storage_credential_name=d.get('storage_credential_name', None),
                   storage_location=d.get('storage_location', None),
                   table_constraints=_from_dict(d, 'table_constraints', TableConstraintList),
                   table_id=d.get('table_id', None),
                   table_type=_enum(d, 'table_type', TableType),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None),
                   view_definition=d.get('view_definition', None),
                   view_dependencies=_repeated(d, 'view_dependencies', Dependency))


@dataclass
class TableRowFilter:
    name: str
    input_column_names: 'List[str]'

    def as_dict(self) -> dict:
        body = {}
        if self.input_column_names: body['input_column_names'] = [v for v in self.input_column_names]
        if self.name: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TableRowFilter':
        return cls(input_column_names=d.get('input_column_names', None), name=d.get('name', None))


@dataclass
class TableSummary:
    full_name: str = None
    table_type: 'TableType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.full_name: body['full_name'] = self.full_name
        if self.table_type: body['table_type'] = self.table_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TableSummary':
        return cls(full_name=d.get('full_name', None), table_type=_enum(d, 'table_type', TableType))


class TableType(Enum):

    EXTERNAL = 'EXTERNAL'
    MANAGED = 'MANAGED'
    MATERIALIZED_VIEW = 'MATERIALIZED_VIEW'
    STREAMING_TABLE = 'STREAMING_TABLE'
    VIEW = 'VIEW'


@dataclass
class UnassignRequest:
    """Delete an assignment"""

    workspace_id: int
    metastore_id: str


@dataclass
class UpdateCatalog:
    name: str
    comment: str = None
    owner: str = None
    properties: 'Dict[str,str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.properties: body['properties'] = self.properties
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateCatalog':
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   properties=d.get('properties', None))


@dataclass
class UpdateExternalLocation:
    name: str
    comment: str = None
    credential_name: str = None
    force: bool = None
    owner: str = None
    read_only: bool = None
    url: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.credential_name: body['credential_name'] = self.credential_name
        if self.force: body['force'] = self.force
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.read_only: body['read_only'] = self.read_only
        if self.url: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateExternalLocation':
        return cls(comment=d.get('comment', None),
                   credential_name=d.get('credential_name', None),
                   force=d.get('force', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   read_only=d.get('read_only', None),
                   url=d.get('url', None))


@dataclass
class UpdateFunction:
    name: str
    owner: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateFunction':
        return cls(name=d.get('name', None), owner=d.get('owner', None))


@dataclass
class UpdateMetastore:
    metastore_id: str
    id: str
    delta_sharing_organization_name: str = None
    delta_sharing_recipient_token_lifetime_in_seconds: int = None
    delta_sharing_scope: 'UpdateMetastoreDeltaSharingScope' = None
    name: str = None
    owner: str = None
    privilege_model_version: str = None
    storage_root_credential_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.delta_sharing_organization_name:
            body['delta_sharing_organization_name'] = self.delta_sharing_organization_name
        if self.delta_sharing_recipient_token_lifetime_in_seconds:
            body[
                'delta_sharing_recipient_token_lifetime_in_seconds'] = self.delta_sharing_recipient_token_lifetime_in_seconds
        if self.delta_sharing_scope: body['delta_sharing_scope'] = self.delta_sharing_scope.value
        if self.id: body['id'] = self.id
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.privilege_model_version: body['privilege_model_version'] = self.privilege_model_version
        if self.storage_root_credential_id:
            body['storage_root_credential_id'] = self.storage_root_credential_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateMetastore':
        return cls(delta_sharing_organization_name=d.get('delta_sharing_organization_name', None),
                   delta_sharing_recipient_token_lifetime_in_seconds=d.get(
                       'delta_sharing_recipient_token_lifetime_in_seconds', None),
                   delta_sharing_scope=_enum(d, 'delta_sharing_scope', UpdateMetastoreDeltaSharingScope),
                   id=d.get('id', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   privilege_model_version=d.get('privilege_model_version', None),
                   storage_root_credential_id=d.get('storage_root_credential_id', None))


@dataclass
class UpdateMetastoreAssignment:
    workspace_id: int
    metastore_id: str
    default_catalog_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.default_catalog_name: body['default_catalog_name'] = self.default_catalog_name
        if self.metastore_id: body['metastore_id'] = self.metastore_id
        if self.workspace_id: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateMetastoreAssignment':
        return cls(default_catalog_name=d.get('default_catalog_name', None),
                   metastore_id=d.get('metastore_id', None),
                   workspace_id=d.get('workspace_id', None))


class UpdateMetastoreDeltaSharingScope(Enum):
    """The scope of Delta Sharing enabled for the metastore."""

    INTERNAL = 'INTERNAL'
    INTERNAL_AND_EXTERNAL = 'INTERNAL_AND_EXTERNAL'


@dataclass
class UpdatePermissions:
    securable_type: 'SecurableType'
    full_name: str
    changes: 'List[PermissionsChange]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.changes: body['changes'] = [v.as_dict() for v in self.changes]
        if self.full_name: body['full_name'] = self.full_name
        if self.securable_type: body['securable_type'] = self.securable_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdatePermissions':
        return cls(changes=_repeated(d, 'changes', PermissionsChange),
                   full_name=d.get('full_name', None),
                   securable_type=_enum(d, 'securable_type', SecurableType))


@dataclass
class UpdateProvider:
    name: str
    comment: str = None
    owner: str = None
    recipient_profile_str: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.recipient_profile_str: body['recipient_profile_str'] = self.recipient_profile_str
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateProvider':
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   recipient_profile_str=d.get('recipient_profile_str', None))


@dataclass
class UpdateRecipient:
    name: str
    comment: str = None
    ip_access_list: 'IpAccessList' = None
    owner: str = None
    properties_kvpairs: Any = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.properties_kvpairs: body['properties_kvpairs'] = self.properties_kvpairs
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateRecipient':
        return cls(comment=d.get('comment', None),
                   ip_access_list=_from_dict(d, 'ip_access_list', IpAccessList),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   properties_kvpairs=d.get('properties_kvpairs', None))


@dataclass
class UpdateSchema:
    full_name: str
    comment: str = None
    name: str = None
    owner: str = None
    properties: 'Dict[str,str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.full_name: body['full_name'] = self.full_name
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.properties: body['properties'] = self.properties
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateSchema':
        return cls(comment=d.get('comment', None),
                   full_name=d.get('full_name', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   properties=d.get('properties', None))


@dataclass
class UpdateShare:
    name: str
    comment: str = None
    owner: str = None
    updates: 'List[SharedDataObjectUpdate]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
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
    name: str
    changes: 'List[PermissionsChange]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.changes: body['changes'] = [v.as_dict() for v in self.changes]
        if self.name: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateSharePermissions':
        return cls(changes=_repeated(d, 'changes', PermissionsChange), name=d.get('name', None))


@dataclass
class UpdateStorageCredential:
    name: str
    aws_iam_role: 'AwsIamRole' = None
    azure_service_principal: 'AzureServicePrincipal' = None
    comment: str = None
    force: bool = None
    gcp_service_account_key: 'GcpServiceAccountKey' = None
    owner: str = None
    read_only: bool = None
    skip_validation: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.aws_iam_role: body['aws_iam_role'] = self.aws_iam_role.as_dict()
        if self.azure_service_principal:
            body['azure_service_principal'] = self.azure_service_principal.as_dict()
        if self.comment: body['comment'] = self.comment
        if self.force: body['force'] = self.force
        if self.gcp_service_account_key:
            body['gcp_service_account_key'] = self.gcp_service_account_key.as_dict()
        if self.name: body['name'] = self.name
        if self.owner: body['owner'] = self.owner
        if self.read_only: body['read_only'] = self.read_only
        if self.skip_validation: body['skip_validation'] = self.skip_validation
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateStorageCredential':
        return cls(aws_iam_role=_from_dict(d, 'aws_iam_role', AwsIamRole),
                   azure_service_principal=_from_dict(d, 'azure_service_principal', AzureServicePrincipal),
                   comment=d.get('comment', None),
                   force=d.get('force', None),
                   gcp_service_account_key=_from_dict(d, 'gcp_service_account_key', GcpServiceAccountKey),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   read_only=d.get('read_only', None),
                   skip_validation=d.get('skip_validation', None))


@dataclass
class ValidateStorageCredential:
    aws_iam_role: 'AwsIamRole' = None
    azure_service_principal: 'AzureServicePrincipal' = None
    external_location_name: str = None
    gcp_service_account_key: 'GcpServiceAccountKey' = None
    read_only: bool = None
    storage_credential_name: Any = None
    url: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.aws_iam_role: body['aws_iam_role'] = self.aws_iam_role.as_dict()
        if self.azure_service_principal:
            body['azure_service_principal'] = self.azure_service_principal.as_dict()
        if self.external_location_name: body['external_location_name'] = self.external_location_name
        if self.gcp_service_account_key:
            body['gcp_service_account_key'] = self.gcp_service_account_key.as_dict()
        if self.read_only: body['read_only'] = self.read_only
        if self.storage_credential_name: body['storage_credential_name'] = self.storage_credential_name
        if self.url: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ValidateStorageCredential':
        return cls(aws_iam_role=_from_dict(d, 'aws_iam_role', AwsIamRole),
                   azure_service_principal=_from_dict(d, 'azure_service_principal', AzureServicePrincipal),
                   external_location_name=d.get('external_location_name', None),
                   gcp_service_account_key=_from_dict(d, 'gcp_service_account_key', GcpServiceAccountKey),
                   read_only=d.get('read_only', None),
                   storage_credential_name=d.get('storage_credential_name', None),
                   url=d.get('url', None))


@dataclass
class ValidateStorageCredentialResponse:
    is_dir: bool = None
    results: 'List[ValidationResult]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.is_dir: body['isDir'] = self.is_dir
        if self.results: body['results'] = [v.as_dict() for v in self.results]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ValidateStorageCredentialResponse':
        return cls(is_dir=d.get('isDir', None), results=_repeated(d, 'results', ValidationResult))


@dataclass
class ValidationResult:
    message: str = None
    operation: 'ValidationResultOperation' = None
    result: 'ValidationResultResult' = None

    def as_dict(self) -> dict:
        body = {}
        if self.message: body['message'] = self.message
        if self.operation: body['operation'] = self.operation.value
        if self.result: body['result'] = self.result.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ValidationResult':
        return cls(message=d.get('message', None),
                   operation=_enum(d, 'operation', ValidationResultOperation),
                   result=_enum(d, 'result', ValidationResultResult))


class ValidationResultOperation(Enum):
    """The operation tested."""

    DELETE = 'DELETE'
    LIST = 'LIST'
    READ = 'READ'
    WRITE = 'WRITE'


class ValidationResultResult(Enum):
    """The results of the tested operation."""

    FAIL = 'FAIL'
    PASS = 'PASS'
    SKIP = 'SKIP'


class AccountMetastoreAssignmentsAPI:
    """These APIs manage metastore assignments to a workspace."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, metastore_id: str, default_catalog_name: str, workspace_id: int,
               **kwargs) -> MetastoreAssignment:
        """Assigns a workspace to a metastore.
        
        Creates an assignment to a metastore for a workspace"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateMetastoreAssignment(default_catalog_name=default_catalog_name,
                                                metastore_id=metastore_id,
                                                workspace_id=workspace_id)
        body = request.as_dict()

        json = self._api.do(
            'POST',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{request.workspace_id}/metastores/{request.metastore_id}',
            body=body)
        return MetastoreAssignment.from_dict(json)

    def delete(self, workspace_id: int, metastore_id: str, **kwargs):
        """Delete a metastore assignment.
        
        Deletes a metastore assignment to a workspace, leaving the workspace with no metastore."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteAccountMetastoreAssignmentRequest(metastore_id=metastore_id,
                                                              workspace_id=workspace_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{request.workspace_id}/metastores/{request.metastore_id}'
        )

    def get(self, workspace_id: int, **kwargs) -> MetastoreAssignment:
        """Gets the metastore assignment for a workspace.
        
        Gets the metastore assignment, if any, for the workspace specified by ID. If the workspace is assigned
        a metastore, the mappig will be returned. If no metastore is assigned to the workspace, the assignment
        will not be found and a 404 returned."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAccountMetastoreAssignmentRequest(workspace_id=workspace_id)

        json = self._api.do(
            'GET', f'/api/2.0/accounts/{self._api.account_id}/workspaces/{request.workspace_id}/metastore')
        return MetastoreAssignment.from_dict(json)

    def list(self, metastore_id: str, **kwargs) -> Iterator[MetastoreAssignment]:
        """Get all workspaces assigned to a metastore.
        
        Gets a list of all Databricks workspace IDs that have been assigned to given metastore."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListAccountMetastoreAssignmentsRequest(metastore_id=metastore_id)

        json = self._api.do(
            'GET', f'/api/2.0/accounts/{self._api.account_id}/metastores/{request.metastore_id}/workspaces')
        return [MetastoreAssignment.from_dict(v) for v in json]

    def update(self,
               workspace_id: int,
               metastore_id: str,
               *,
               default_catalog_name: str = None,
               **kwargs) -> MetastoreAssignment:
        """Updates a metastore assignment to a workspaces.
        
        Updates an assignment to a metastore for a workspace. Currently, only the default catalog may be
        updated"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateMetastoreAssignment(default_catalog_name=default_catalog_name,
                                                metastore_id=metastore_id,
                                                workspace_id=workspace_id)
        body = request.as_dict()

        json = self._api.do(
            'PUT',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{request.workspace_id}/metastores/{request.metastore_id}',
            body=body)
        return MetastoreAssignment.from_dict(json)


class AccountMetastoresAPI:
    """These APIs manage Unity Catalog metastores for an account. A metastore contains catalogs that can be
    associated with workspaces"""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, name: str, storage_root: str, *, region: str = None, **kwargs) -> MetastoreInfo:
        """Create metastore.
        
        Creates a Unity Catalog metastore."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateMetastore(name=name, region=region, storage_root=storage_root)
        body = request.as_dict()

        json = self._api.do('POST', f'/api/2.0/accounts/{self._api.account_id}/metastores', body=body)
        return MetastoreInfo.from_dict(json)

    def delete(self, metastore_id: str, **kwargs):
        """Delete a metastore.
        
        Deletes a Databricks Unity Catalog metastore for an account, both specified by ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteAccountMetastoreRequest(metastore_id=metastore_id)

        self._api.do('DELETE', f'/api/2.0/accounts/{self._api.account_id}/metastores/{request.metastore_id}')

    def get(self, metastore_id: str, **kwargs) -> MetastoreInfo:
        """Get a metastore.
        
        Gets a Databricks Unity Catalog metastore from an account, both specified by ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAccountMetastoreRequest(metastore_id=metastore_id)

        json = self._api.do('GET',
                            f'/api/2.0/accounts/{self._api.account_id}/metastores/{request.metastore_id}')
        return MetastoreInfo.from_dict(json)

    def list(self) -> ListMetastoresResponse:
        """Get all metastores associated with an account.
        
        Gets all Unity Catalog metastores associated with an account specified by ID."""

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/metastores')
        return ListMetastoresResponse.from_dict(json)

    def update(self,
               metastore_id: str,
               id: str,
               *,
               delta_sharing_organization_name: str = None,
               delta_sharing_recipient_token_lifetime_in_seconds: int = None,
               delta_sharing_scope: UpdateMetastoreDeltaSharingScope = None,
               name: str = None,
               owner: str = None,
               privilege_model_version: str = None,
               storage_root_credential_id: str = None,
               **kwargs) -> MetastoreInfo:
        """Update a metastore.
        
        Updates an existing Unity Catalog metastore."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateMetastore(
                delta_sharing_organization_name=delta_sharing_organization_name,
                delta_sharing_recipient_token_lifetime_in_seconds=delta_sharing_recipient_token_lifetime_in_seconds,
                delta_sharing_scope=delta_sharing_scope,
                id=id,
                metastore_id=metastore_id,
                name=name,
                owner=owner,
                privilege_model_version=privilege_model_version,
                storage_root_credential_id=storage_root_credential_id)
        body = request.as_dict()

        json = self._api.do('PUT',
                            f'/api/2.0/accounts/{self._api.account_id}/metastores/{request.metastore_id}',
                            body=body)
        return MetastoreInfo.from_dict(json)


class AccountStorageCredentialsAPI:
    """These APIs manage storage credentials for a particular metastore."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               metastore_id: str,
               *,
               aws_iam_role: AwsIamRole = None,
               azure_service_principal: AzureServicePrincipal = None,
               comment: str = None,
               gcp_service_account_key: GcpServiceAccountKey = None,
               read_only: bool = None,
               skip_validation: bool = None,
               **kwargs) -> StorageCredentialInfo:
        """Create a storage credential.
        
        Creates a new storage credential. The request object is specific to the cloud:
        
        * **AwsIamRole** for AWS credentials * **AzureServicePrincipal** for Azure credentials *
        **GcpServiceAcountKey** for GCP credentials.
        
        The caller must be a metastore admin and have the **CREATE_STORAGE_CREDENTIAL** privilege on the
        metastore."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateStorageCredential(aws_iam_role=aws_iam_role,
                                              azure_service_principal=azure_service_principal,
                                              comment=comment,
                                              gcp_service_account_key=gcp_service_account_key,
                                              metastore_id=metastore_id,
                                              name=name,
                                              read_only=read_only,
                                              skip_validation=skip_validation)
        body = request.as_dict()

        json = self._api.do(
            'POST',
            f'/api/2.0/accounts/{self._api.account_id}/metastores/{request.metastore_id}/storage-credentials',
            body=body)
        return StorageCredentialInfo.from_dict(json)

    def get(self, metastore_id: str, name: str, **kwargs) -> StorageCredentialInfo:
        """Gets the named storage credential.
        
        Gets a storage credential from the metastore. The caller must be a metastore admin, the owner of the
        storage credential, or have a level of privilege on the storage credential."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAccountStorageCredentialRequest(metastore_id=metastore_id, name=name)

        json = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/metastores/{request.metastore_id}/storage-credentials/'
        )
        return StorageCredentialInfo.from_dict(json)

    def list(self, metastore_id: str, **kwargs) -> Iterator[StorageCredentialInfo]:
        """Get all storage credentials assigned to a metastore.
        
        Gets a list of all storage credentials that have been assigned to given metastore."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListAccountStorageCredentialsRequest(metastore_id=metastore_id)

        json = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/metastores/{request.metastore_id}/storage-credentials')
        return [StorageCredentialInfo.from_dict(v) for v in json]


class CatalogsAPI:
    """A catalog is the first layer of Unity Catalog’s three-level namespace. It’s used to organize your data
    assets. Users can see all catalogs on which they have been assigned the USE_CATALOG data permission.
    
    In Unity Catalog, admins and data stewards manage users and their access to data centrally across all of
    the workspaces in a Databricks account. Users in different workspaces can share access to the same data,
    depending on privileges granted centrally in Unity Catalog."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               *,
               comment: str = None,
               properties: Dict[str, str] = None,
               provider_name: str = None,
               share_name: str = None,
               storage_root: str = None,
               **kwargs) -> CatalogInfo:
        """Create a catalog.
        
        Creates a new catalog instance in the parent metastore if the caller is a metastore admin or has the
        **CREATE_CATALOG** privilege."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateCatalog(comment=comment,
                                    name=name,
                                    properties=properties,
                                    provider_name=provider_name,
                                    share_name=share_name,
                                    storage_root=storage_root)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.1/unity-catalog/catalogs', body=body)
        return CatalogInfo.from_dict(json)

    def delete(self, name: str, *, force: bool = None, **kwargs):
        """Delete a catalog.
        
        Deletes the catalog that matches the supplied name. The caller must be a metastore admin or the owner
        of the catalog."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteCatalogRequest(force=force, name=name)

        query = {}
        if force: query['force'] = request.force

        self._api.do('DELETE', f'/api/2.1/unity-catalog/catalogs/{request.name}', query=query)

    def get(self, name: str, **kwargs) -> CatalogInfo:
        """Get a catalog.
        
        Gets the specified catalog in a metastore. The caller must be a metastore admin, the owner of the
        catalog, or a user that has the **USE_CATALOG** privilege set for their account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetCatalogRequest(name=name)

        json = self._api.do('GET', f'/api/2.1/unity-catalog/catalogs/{request.name}')
        return CatalogInfo.from_dict(json)

    def list(self) -> Iterator[CatalogInfo]:
        """List catalogs.
        
        Gets an array of catalogs in the metastore. If the caller is the metastore admin, all catalogs will be
        retrieved. Otherwise, only catalogs owned by the caller (or for which the caller has the
        **USE_CATALOG** privilege) will be retrieved. There is no guarantee of a specific ordering of the
        elements in the array."""

        json = self._api.do('GET', '/api/2.1/unity-catalog/catalogs')
        return [CatalogInfo.from_dict(v) for v in json.get('catalogs', [])]

    def update(self,
               name: str,
               *,
               comment: str = None,
               owner: str = None,
               properties: Dict[str, str] = None,
               **kwargs) -> CatalogInfo:
        """Update a catalog.
        
        Updates the catalog that matches the supplied name. The caller must be either the owner of the
        catalog, or a metastore admin (when changing the owner field of the catalog)."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateCatalog(comment=comment, name=name, owner=owner, properties=properties)
        body = request.as_dict()

        json = self._api.do('PATCH', f'/api/2.1/unity-catalog/catalogs/{request.name}', body=body)
        return CatalogInfo.from_dict(json)


class ExternalLocationsAPI:
    """An external location is an object that combines a cloud storage path with a storage credential that
    authorizes access to the cloud storage path. Each external location is subject to Unity Catalog
    access-control policies that control which users and groups can access the credential. If a user does not
    have access to an external location in Unity Catalog, the request fails and Unity Catalog does not attempt
    to authenticate to your cloud tenant on the user’s behalf.
    
    Databricks recommends using external locations rather than using storage credentials directly.
    
    To create external locations, you must be a metastore admin or a user with the
    **CREATE_EXTERNAL_LOCATION** privilege."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               url: str,
               credential_name: str,
               *,
               comment: str = None,
               read_only: bool = None,
               skip_validation: bool = None,
               **kwargs) -> ExternalLocationInfo:
        """Create an external location.
        
        Creates a new external location entry in the metastore. The caller must be a metastore admin or have
        the **CREATE_EXTERNAL_LOCATION** privilege on both the metastore and the associated storage
        credential."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateExternalLocation(comment=comment,
                                             credential_name=credential_name,
                                             name=name,
                                             read_only=read_only,
                                             skip_validation=skip_validation,
                                             url=url)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.1/unity-catalog/external-locations', body=body)
        return ExternalLocationInfo.from_dict(json)

    def delete(self, name: str, *, force: bool = None, **kwargs):
        """Delete an external location.
        
        Deletes the specified external location from the metastore. The caller must be the owner of the
        external location."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteExternalLocationRequest(force=force, name=name)

        query = {}
        if force: query['force'] = request.force

        self._api.do('DELETE', f'/api/2.1/unity-catalog/external-locations/{request.name}', query=query)

    def get(self, name: str, **kwargs) -> ExternalLocationInfo:
        """Get an external location.
        
        Gets an external location from the metastore. The caller must be either a metastore admin, the owner
        of the external location, or a user that has some privilege on the external location."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetExternalLocationRequest(name=name)

        json = self._api.do('GET', f'/api/2.1/unity-catalog/external-locations/{request.name}')
        return ExternalLocationInfo.from_dict(json)

    def list(self) -> Iterator[ExternalLocationInfo]:
        """List external locations.
        
        Gets an array of external locations (__ExternalLocationInfo__ objects) from the metastore. The caller
        must be a metastore admin, the owner of the external location, or a user that has some privilege on
        the external location. There is no guarantee of a specific ordering of the elements in the array."""

        json = self._api.do('GET', '/api/2.1/unity-catalog/external-locations')
        return [ExternalLocationInfo.from_dict(v) for v in json.get('external_locations', [])]

    def update(self,
               name: str,
               *,
               comment: str = None,
               credential_name: str = None,
               force: bool = None,
               owner: str = None,
               read_only: bool = None,
               url: str = None,
               **kwargs) -> ExternalLocationInfo:
        """Update an external location.
        
        Updates an external location in the metastore. The caller must be the owner of the external location,
        or be a metastore admin. In the second case, the admin can only update the name of the external
        location."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateExternalLocation(comment=comment,
                                             credential_name=credential_name,
                                             force=force,
                                             name=name,
                                             owner=owner,
                                             read_only=read_only,
                                             url=url)
        body = request.as_dict()

        json = self._api.do('PATCH', f'/api/2.1/unity-catalog/external-locations/{request.name}', body=body)
        return ExternalLocationInfo.from_dict(json)


class FunctionsAPI:
    """Functions implement User-Defined Functions (UDFs) in Unity Catalog.
    
    The function implementation can be any SQL expression or Query, and it can be invoked wherever a table
    reference is allowed in a query. In Unity Catalog, a function resides at the same level as a table, so it
    can be referenced with the form __catalog_name__.__schema_name__.__function_name__."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               catalog_name: str,
               schema_name: str,
               input_params: List[FunctionParameterInfo],
               data_type: ColumnTypeName,
               full_data_type: str,
               return_params: List[FunctionParameterInfo],
               routine_body: CreateFunctionRoutineBody,
               routine_definition: str,
               routine_dependencies: List[Dependency],
               parameter_style: CreateFunctionParameterStyle,
               is_deterministic: bool,
               sql_data_access: CreateFunctionSqlDataAccess,
               is_null_call: bool,
               security_type: CreateFunctionSecurityType,
               specific_name: str,
               *,
               comment: str = None,
               external_language: str = None,
               external_name: str = None,
               properties: Dict[str, str] = None,
               sql_path: str = None,
               **kwargs) -> FunctionInfo:
        """Create a function.
        
        Creates a new function
        
        The user must have the following permissions in order for the function to be created: -
        **USE_CATALOG** on the function's parent catalog - **USE_SCHEMA** and **CREATE_FUNCTION** on the
        function's parent schema"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateFunction(catalog_name=catalog_name,
                                     comment=comment,
                                     data_type=data_type,
                                     external_language=external_language,
                                     external_name=external_name,
                                     full_data_type=full_data_type,
                                     input_params=input_params,
                                     is_deterministic=is_deterministic,
                                     is_null_call=is_null_call,
                                     name=name,
                                     parameter_style=parameter_style,
                                     properties=properties,
                                     return_params=return_params,
                                     routine_body=routine_body,
                                     routine_definition=routine_definition,
                                     routine_dependencies=routine_dependencies,
                                     schema_name=schema_name,
                                     security_type=security_type,
                                     specific_name=specific_name,
                                     sql_data_access=sql_data_access,
                                     sql_path=sql_path)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.1/unity-catalog/functions', body=body)
        return FunctionInfo.from_dict(json)

    def delete(self, name: str, *, force: bool = None, **kwargs):
        """Delete a function.
        
        Deletes the function that matches the supplied name. For the deletion to succeed, the user must
        satisfy one of the following conditions: - Is the owner of the function's parent catalog - Is the
        owner of the function's parent schema and have the **USE_CATALOG** privilege on its parent catalog -
        Is the owner of the function itself and have both the **USE_CATALOG** privilege on its parent catalog
        and the **USE_SCHEMA** privilege on its parent schema"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteFunctionRequest(force=force, name=name)

        query = {}
        if force: query['force'] = request.force

        self._api.do('DELETE', f'/api/2.1/unity-catalog/functions/{request.name}', query=query)

    def get(self, name: str, **kwargs) -> FunctionInfo:
        """Get a function.
        
        Gets a function from within a parent catalog and schema. For the fetch to succeed, the user must
        satisfy one of the following requirements: - Is a metastore admin - Is an owner of the function's
        parent catalog - Have the **USE_CATALOG** privilege on the function's parent catalog and be the owner
        of the function - Have the **USE_CATALOG** privilege on the function's parent catalog, the
        **USE_SCHEMA** privilege on the function's parent schema, and the **EXECUTE** privilege on the
        function itself"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetFunctionRequest(name=name)

        json = self._api.do('GET', f'/api/2.1/unity-catalog/functions/{request.name}')
        return FunctionInfo.from_dict(json)

    def list(self, catalog_name: str, schema_name: str, **kwargs) -> ListFunctionsResponse:
        """List functions.
        
        List functions within the specified parent catalog and schema. If the user is a metastore admin, all
        functions are returned in the output list. Otherwise, the user must have the **USE_CATALOG** privilege
        on the catalog and the **USE_SCHEMA** privilege on the schema, and the output list contains only
        functions for which either the user has the **EXECUTE** privilege or the user is the owner. There is
        no guarantee of a specific ordering of the elements in the array."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListFunctionsRequest(catalog_name=catalog_name, schema_name=schema_name)

        query = {}
        if catalog_name: query['catalog_name'] = request.catalog_name
        if schema_name: query['schema_name'] = request.schema_name

        json = self._api.do('GET', '/api/2.1/unity-catalog/functions', query=query)
        return ListFunctionsResponse.from_dict(json)

    def update(self, name: str, *, owner: str = None, **kwargs) -> FunctionInfo:
        """Update a function.
        
        Updates the function that matches the supplied name. Only the owner of the function can be updated. If
        the user is not a metastore admin, the user must be a member of the group that is the new function
        owner. - Is a metastore admin - Is the owner of the function's parent catalog - Is the owner of the
        function's parent schema and has the **USE_CATALOG** privilege on its parent catalog - Is the owner of
        the function itself and has the **USE_CATALOG** privilege on its parent catalog as well as the
        **USE_SCHEMA** privilege on the function's parent schema."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateFunction(name=name, owner=owner)
        body = request.as_dict()

        json = self._api.do('PATCH', f'/api/2.1/unity-catalog/functions/{request.name}', body=body)
        return FunctionInfo.from_dict(json)


class GrantsAPI:
    """In Unity Catalog, data is secure by default. Initially, users have no access to data in a metastore.
    Access can be granted by either a metastore admin, the owner of an object, or the owner of the catalog or
    schema that contains the object. Securable objects in Unity Catalog are hierarchical and privileges are
    inherited downward.
    
    Securable objects in Unity Catalog are hierarchical and privileges are inherited downward. This means that
    granting a privilege on the catalog automatically grants the privilege to all current and future objects
    within the catalog. Similarly, privileges granted on a schema are inherited by all current and future
    objects within that schema."""

    def __init__(self, api_client):
        self._api = api_client

    def get(self,
            securable_type: SecurableType,
            full_name: str,
            *,
            principal: str = None,
            **kwargs) -> PermissionsList:
        """Get permissions.
        
        Gets the permissions for a securable."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetGrantRequest(full_name=full_name, principal=principal, securable_type=securable_type)

        query = {}
        if principal: query['principal'] = request.principal

        json = self._api.do(
            'GET',
            f'/api/2.1/unity-catalog/permissions/{request.securable_type}/{request.full_name}',
            query=query)
        return PermissionsList.from_dict(json)

    def get_effective(self,
                      securable_type: SecurableType,
                      full_name: str,
                      *,
                      principal: str = None,
                      **kwargs) -> EffectivePermissionsList:
        """Get effective permissions.
        
        Gets the effective permissions for a securable."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetEffectiveRequest(full_name=full_name,
                                          principal=principal,
                                          securable_type=securable_type)

        query = {}
        if principal: query['principal'] = request.principal

        json = self._api.do(
            'GET',
            f'/api/2.1/unity-catalog/effective-permissions/{request.securable_type}/{request.full_name}',
            query=query)
        return EffectivePermissionsList.from_dict(json)

    def update(self,
               securable_type: SecurableType,
               full_name: str,
               *,
               changes: List[PermissionsChange] = None,
               **kwargs) -> PermissionsList:
        """Update permissions.
        
        Updates the permissions for a securable."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdatePermissions(changes=changes, full_name=full_name, securable_type=securable_type)
        body = request.as_dict()

        json = self._api.do(
            'PATCH',
            f'/api/2.1/unity-catalog/permissions/{request.securable_type}/{request.full_name}',
            body=body)
        return PermissionsList.from_dict(json)


class MetastoresAPI:
    """A metastore is the top-level container of objects in Unity Catalog. It stores data assets (tables and
    views) and the permissions that govern access to them. Databricks account admins can create metastores and
    assign them to Databricks workspaces to control which workloads use each metastore. For a workspace to use
    Unity Catalog, it must have a Unity Catalog metastore attached.
    
    Each metastore is configured with a root storage location in a cloud storage account. This storage
    location is used for metadata and managed tables data.
    
    NOTE: This metastore is distinct from the metastore included in Databricks workspaces created before Unity
    Catalog was released. If your workspace includes a legacy Hive metastore, the data in that metastore is
    available in a catalog named hive_metastore."""

    def __init__(self, api_client):
        self._api = api_client

    def assign(self, metastore_id: str, default_catalog_name: str, workspace_id: int, **kwargs):
        """Create an assignment.
        
        Creates a new metastore assignment. If an assignment for the same __workspace_id__ exists, it will be
        overwritten by the new __metastore_id__ and __default_catalog_name__. The caller must be an account
        admin."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateMetastoreAssignment(default_catalog_name=default_catalog_name,
                                                metastore_id=metastore_id,
                                                workspace_id=workspace_id)
        body = request.as_dict()
        self._api.do('PUT', f'/api/2.1/unity-catalog/workspaces/{request.workspace_id}/metastore', body=body)

    def create(self, name: str, storage_root: str, *, region: str = None, **kwargs) -> MetastoreInfo:
        """Create a metastore.
        
        Creates a new metastore based on a provided name and storage root path."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateMetastore(name=name, region=region, storage_root=storage_root)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.1/unity-catalog/metastores', body=body)
        return MetastoreInfo.from_dict(json)

    def current(self) -> MetastoreAssignment:
        """Get metastore assignment for workspace.
        
        Gets the metastore assignment for the workspace being accessed."""

        json = self._api.do('GET', '/api/2.1/unity-catalog/current-metastore-assignment')
        return MetastoreAssignment.from_dict(json)

    def delete(self, id: str, *, force: bool = None, **kwargs):
        """Delete a metastore.
        
        Deletes a metastore. The caller must be a metastore admin."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteMetastoreRequest(force=force, id=id)

        query = {}
        if force: query['force'] = request.force

        self._api.do('DELETE', f'/api/2.1/unity-catalog/metastores/{request.id}', query=query)

    def get(self, id: str, **kwargs) -> MetastoreInfo:
        """Get a metastore.
        
        Gets a metastore that matches the supplied ID. The caller must be a metastore admin to retrieve this
        info."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetMetastoreRequest(id=id)

        json = self._api.do('GET', f'/api/2.1/unity-catalog/metastores/{request.id}')
        return MetastoreInfo.from_dict(json)

    def list(self) -> Iterator[MetastoreInfo]:
        """List metastores.
        
        Gets an array of the available metastores (as __MetastoreInfo__ objects). The caller must be an admin
        to retrieve this info. There is no guarantee of a specific ordering of the elements in the array."""

        json = self._api.do('GET', '/api/2.1/unity-catalog/metastores')
        return [MetastoreInfo.from_dict(v) for v in json.get('metastores', [])]

    def summary(self) -> GetMetastoreSummaryResponse:
        """Get a metastore summary.
        
        Gets information about a metastore. This summary includes the storage credential, the cloud vendor,
        the cloud region, and the global metastore ID."""

        json = self._api.do('GET', '/api/2.1/unity-catalog/metastore_summary')
        return GetMetastoreSummaryResponse.from_dict(json)

    def unassign(self, workspace_id: int, metastore_id: str, **kwargs):
        """Delete an assignment.
        
        Deletes a metastore assignment. The caller must be an account administrator."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UnassignRequest(metastore_id=metastore_id, workspace_id=workspace_id)

        query = {}
        if metastore_id: query['metastore_id'] = request.metastore_id

        self._api.do('DELETE',
                     f'/api/2.1/unity-catalog/workspaces/{request.workspace_id}/metastore',
                     query=query)

    def update(self,
               metastore_id: str,
               id: str,
               *,
               delta_sharing_organization_name: str = None,
               delta_sharing_recipient_token_lifetime_in_seconds: int = None,
               delta_sharing_scope: UpdateMetastoreDeltaSharingScope = None,
               name: str = None,
               owner: str = None,
               privilege_model_version: str = None,
               storage_root_credential_id: str = None,
               **kwargs) -> MetastoreInfo:
        """Update a metastore.
        
        Updates information for a specific metastore. The caller must be a metastore admin."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateMetastore(
                delta_sharing_organization_name=delta_sharing_organization_name,
                delta_sharing_recipient_token_lifetime_in_seconds=delta_sharing_recipient_token_lifetime_in_seconds,
                delta_sharing_scope=delta_sharing_scope,
                id=id,
                metastore_id=metastore_id,
                name=name,
                owner=owner,
                privilege_model_version=privilege_model_version,
                storage_root_credential_id=storage_root_credential_id)
        body = request.as_dict()

        json = self._api.do('PATCH', f'/api/2.1/unity-catalog/metastores/{request.id}', body=body)
        return MetastoreInfo.from_dict(json)

    def update_assignment(self,
                          workspace_id: int,
                          metastore_id: str,
                          *,
                          default_catalog_name: str = None,
                          **kwargs):
        """Update an assignment.
        
        Updates a metastore assignment. This operation can be used to update __metastore_id__ or
        __default_catalog_name__ for a specified Workspace, if the Workspace is already assigned a metastore.
        The caller must be an account admin to update __metastore_id__; otherwise, the caller can be a
        Workspace admin."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateMetastoreAssignment(default_catalog_name=default_catalog_name,
                                                metastore_id=metastore_id,
                                                workspace_id=workspace_id)
        body = request.as_dict()
        self._api.do('PATCH',
                     f'/api/2.1/unity-catalog/workspaces/{request.workspace_id}/metastore',
                     body=body)


class ProvidersAPI:
    """Databricks Delta Sharing: Providers REST API"""

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
    """Databricks Delta Sharing: Recipient Activation REST API"""

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
    """Databricks Delta Sharing: Recipients REST API"""

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
               properties_kvpairs: Any = None,
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
               properties_kvpairs: Any = None,
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


class SchemasAPI:
    """A schema (also called a database) is the second layer of Unity Catalog’s three-level namespace. A schema
    organizes tables, views and functions. To access (or list) a table or view in a schema, users must have
    the USE_SCHEMA data permission on the schema and its parent catalog, and they must have the SELECT
    permission on the table or view."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               catalog_name: str,
               *,
               comment: str = None,
               properties: Dict[str, str] = None,
               storage_root: str = None,
               **kwargs) -> SchemaInfo:
        """Create a schema.
        
        Creates a new schema for catalog in the Metatastore. The caller must be a metastore admin, or have the
        **CREATE_SCHEMA** privilege in the parent catalog."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateSchema(catalog_name=catalog_name,
                                   comment=comment,
                                   name=name,
                                   properties=properties,
                                   storage_root=storage_root)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.1/unity-catalog/schemas', body=body)
        return SchemaInfo.from_dict(json)

    def delete(self, full_name: str, **kwargs):
        """Delete a schema.
        
        Deletes the specified schema from the parent catalog. The caller must be the owner of the schema or an
        owner of the parent catalog."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteSchemaRequest(full_name=full_name)

        self._api.do('DELETE', f'/api/2.1/unity-catalog/schemas/{request.full_name}')

    def get(self, full_name: str, **kwargs) -> SchemaInfo:
        """Get a schema.
        
        Gets the specified schema within the metastore. The caller must be a metastore admin, the owner of the
        schema, or a user that has the **USE_SCHEMA** privilege on the schema."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetSchemaRequest(full_name=full_name)

        json = self._api.do('GET', f'/api/2.1/unity-catalog/schemas/{request.full_name}')
        return SchemaInfo.from_dict(json)

    def list(self, catalog_name: str, **kwargs) -> Iterator[SchemaInfo]:
        """List schemas.
        
        Gets an array of schemas for a catalog in the metastore. If the caller is the metastore admin or the
        owner of the parent catalog, all schemas for the catalog will be retrieved. Otherwise, only schemas
        owned by the caller (or for which the caller has the **USE_SCHEMA** privilege) will be retrieved.
        There is no guarantee of a specific ordering of the elements in the array."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListSchemasRequest(catalog_name=catalog_name)

        query = {}
        if catalog_name: query['catalog_name'] = request.catalog_name

        json = self._api.do('GET', '/api/2.1/unity-catalog/schemas', query=query)
        return [SchemaInfo.from_dict(v) for v in json.get('schemas', [])]

    def update(self,
               full_name: str,
               *,
               comment: str = None,
               name: str = None,
               owner: str = None,
               properties: Dict[str, str] = None,
               **kwargs) -> SchemaInfo:
        """Update a schema.
        
        Updates a schema for a catalog. The caller must be the owner of the schema or a metastore admin. If
        the caller is a metastore admin, only the __owner__ field can be changed in the update. If the
        __name__ field must be updated, the caller must be a metastore admin or have the **CREATE_SCHEMA**
        privilege on the parent catalog."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateSchema(comment=comment,
                                   full_name=full_name,
                                   name=name,
                                   owner=owner,
                                   properties=properties)
        body = request.as_dict()

        json = self._api.do('PATCH', f'/api/2.1/unity-catalog/schemas/{request.full_name}', body=body)
        return SchemaInfo.from_dict(json)


class SharesAPI:
    """Databricks Delta Sharing: Shares REST API"""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, name: str, *, comment: str = None, **kwargs) -> ShareInfo:
        """Create a share.
        
        Creates a new share for data objects. Data objects can be added at this time or after creation with
        **update**. The caller must be a metastore admin or have the **CREATE_SHARE** privilege on the
        metastore."""
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


class StorageCredentialsAPI:
    """A storage credential represents an authentication and authorization mechanism for accessing data stored on
    your cloud tenant. Each storage credential is subject to Unity Catalog access-control policies that
    control which users and groups can access the credential. If a user does not have access to a storage
    credential in Unity Catalog, the request fails and Unity Catalog does not attempt to authenticate to your
    cloud tenant on the user’s behalf.
    
    Databricks recommends using external locations rather than using storage credentials directly.
    
    To create storage credentials, you must be a Databricks account admin. The account admin who creates the
    storage credential can delegate ownership to another user or group to manage permissions on it."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               metastore_id: str,
               *,
               aws_iam_role: AwsIamRole = None,
               azure_service_principal: AzureServicePrincipal = None,
               comment: str = None,
               gcp_service_account_key: GcpServiceAccountKey = None,
               read_only: bool = None,
               skip_validation: bool = None,
               **kwargs) -> StorageCredentialInfo:
        """Create a storage credential.
        
        Creates a new storage credential. The request object is specific to the cloud:
        
        * **AwsIamRole** for AWS credentials * **AzureServicePrincipal** for Azure credentials *
        **GcpServiceAcountKey** for GCP credentials.
        
        The caller must be a metastore admin and have the **CREATE_STORAGE_CREDENTIAL** privilege on the
        metastore."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateStorageCredential(aws_iam_role=aws_iam_role,
                                              azure_service_principal=azure_service_principal,
                                              comment=comment,
                                              gcp_service_account_key=gcp_service_account_key,
                                              metastore_id=metastore_id,
                                              name=name,
                                              read_only=read_only,
                                              skip_validation=skip_validation)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.1/unity-catalog/storage-credentials', body=body)
        return StorageCredentialInfo.from_dict(json)

    def delete(self, name: str, *, force: bool = None, **kwargs):
        """Delete a credential.
        
        Deletes a storage credential from the metastore. The caller must be an owner of the storage
        credential."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteStorageCredentialRequest(force=force, name=name)

        query = {}
        if force: query['force'] = request.force

        self._api.do('DELETE', f'/api/2.1/unity-catalog/storage-credentials/{request.name}', query=query)

    def get(self, name: str, **kwargs) -> StorageCredentialInfo:
        """Get a credential.
        
        Gets a storage credential from the metastore. The caller must be a metastore admin, the owner of the
        storage credential, or have some permission on the storage credential."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetStorageCredentialRequest(name=name)

        json = self._api.do('GET', f'/api/2.1/unity-catalog/storage-credentials/{request.name}')
        return StorageCredentialInfo.from_dict(json)

    def list(self) -> Iterator[StorageCredentialInfo]:
        """List credentials.
        
        Gets an array of storage credentials (as __StorageCredentialInfo__ objects). The array is limited to
        only those storage credentials the caller has permission to access. If the caller is a metastore
        admin, all storage credentials will be retrieved. There is no guarantee of a specific ordering of the
        elements in the array."""

        json = self._api.do('GET', '/api/2.1/unity-catalog/storage-credentials')
        return [StorageCredentialInfo.from_dict(v) for v in json]

    def update(self,
               name: str,
               *,
               aws_iam_role: AwsIamRole = None,
               azure_service_principal: AzureServicePrincipal = None,
               comment: str = None,
               force: bool = None,
               gcp_service_account_key: GcpServiceAccountKey = None,
               owner: str = None,
               read_only: bool = None,
               skip_validation: bool = None,
               **kwargs) -> StorageCredentialInfo:
        """Update a credential.
        
        Updates a storage credential on the metastore. The caller must be the owner of the storage credential
        or a metastore admin. If the caller is a metastore admin, only the __owner__ credential can be
        changed."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateStorageCredential(aws_iam_role=aws_iam_role,
                                              azure_service_principal=azure_service_principal,
                                              comment=comment,
                                              force=force,
                                              gcp_service_account_key=gcp_service_account_key,
                                              name=name,
                                              owner=owner,
                                              read_only=read_only,
                                              skip_validation=skip_validation)
        body = request.as_dict()

        json = self._api.do('PATCH', f'/api/2.1/unity-catalog/storage-credentials/{request.name}', body=body)
        return StorageCredentialInfo.from_dict(json)

    def validate(self,
                 *,
                 aws_iam_role: AwsIamRole = None,
                 azure_service_principal: AzureServicePrincipal = None,
                 external_location_name: str = None,
                 gcp_service_account_key: GcpServiceAccountKey = None,
                 read_only: bool = None,
                 storage_credential_name: Any = None,
                 url: str = None,
                 **kwargs) -> ValidateStorageCredentialResponse:
        """Validate a storage credential.
        
        Validates a storage credential. At least one of __external_location_name__ and __url__ need to be
        provided. If only one of them is provided, it will be used for validation. And if both are provided,
        the __url__ will be used for validation, and __external_location_name__ will be ignored when checking
        overlapping urls.
        
        Either the __storage_credential_name__ or the cloud-specific credential must be provided.
        
        The caller must be a metastore admin or the storage credential owner or have the
        **CREATE_EXTERNAL_LOCATION** privilege on the metastore and the storage credential."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ValidateStorageCredential(aws_iam_role=aws_iam_role,
                                                azure_service_principal=azure_service_principal,
                                                external_location_name=external_location_name,
                                                gcp_service_account_key=gcp_service_account_key,
                                                read_only=read_only,
                                                storage_credential_name=storage_credential_name,
                                                url=url)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.1/unity-catalog/validate-storage-credentials', body=body)
        return ValidateStorageCredentialResponse.from_dict(json)


class TableConstraintsAPI:
    """Primary key and foreign key constraints encode relationships between fields in tables.
    
    Primary and foreign keys are informational only and are not enforced. Foreign keys must reference a
    primary key in another table. This primary key is the parent constraint of the foreign key and the table
    this primary key is on is the parent table of the foreign key. Similarly, the foreign key is the child
    constraint of its referenced primary key; the table of the foreign key is the child table of the primary
    key.
    
    You can declare primary keys and foreign keys as part of the table specification during table creation.
    You can also add or drop constraints on existing tables."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, full_name_arg: str, constraint: TableConstraint, **kwargs) -> TableConstraint:
        """Create a table constraint.
        
        Creates a new table constraint.
        
        For the table constraint creation to succeed, the user must satisfy both of these conditions: - the
        user must have the **USE_CATALOG** privilege on the table's parent catalog, the **USE_SCHEMA**
        privilege on the table's parent schema, and be the owner of the table. - if the new constraint is a
        __ForeignKeyConstraint__, the user must have the **USE_CATALOG** privilege on the referenced parent
        table's catalog, the **USE_SCHEMA** privilege on the referenced parent table's schema, and be the
        owner of the referenced parent table."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateTableConstraint(constraint=constraint, full_name_arg=full_name_arg)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.1/unity-catalog/constraints', body=body)
        return TableConstraint.from_dict(json)

    def delete(self, full_name: str, constraint_name: str, cascade: bool, **kwargs):
        """Delete a table constraint.
        
        Deletes a table constraint.
        
        For the table constraint deletion to succeed, the user must satisfy both of these conditions: - the
        user must have the **USE_CATALOG** privilege on the table's parent catalog, the **USE_SCHEMA**
        privilege on the table's parent schema, and be the owner of the table. - if __cascade__ argument is
        **true**, the user must have the following permissions on all of the child tables: the **USE_CATALOG**
        privilege on the table's catalog, the **USE_SCHEMA** privilege on the table's schema, and be the owner
        of the table."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteTableConstraintRequest(cascade=cascade,
                                                   constraint_name=constraint_name,
                                                   full_name=full_name)

        query = {}
        if cascade: query['cascade'] = request.cascade
        if constraint_name: query['constraint_name'] = request.constraint_name

        self._api.do('DELETE', f'/api/2.1/unity-catalog/constraints/{request.full_name}', query=query)


class TablesAPI:
    """A table resides in the third layer of Unity Catalog’s three-level namespace. It contains rows of data.
    To create a table, users must have CREATE_TABLE and USE_SCHEMA permissions on the schema, and they must
    have the USE_CATALOG permission on its parent catalog. To query a table, users must have the SELECT
    permission on the table, and they must have the USE_CATALOG permission on its parent catalog and the
    USE_SCHEMA permission on its parent schema.
    
    A table can be managed or external. From an API perspective, a __VIEW__ is a particular kind of table
    (rather than a managed or external table)."""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, full_name: str, **kwargs):
        """Delete a table.
        
        Deletes a table from the specified parent catalog and schema. The caller must be the owner of the
        parent catalog, have the **USE_CATALOG** privilege on the parent catalog and be the owner of the
        parent schema, or be the owner of the table and have the **USE_CATALOG** privilege on the parent
        catalog and the **USE_SCHEMA** privilege on the parent schema."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteTableRequest(full_name=full_name)

        self._api.do('DELETE', f'/api/2.1/unity-catalog/tables/{request.full_name}')

    def get(self, full_name: str, *, include_delta_metadata: bool = None, **kwargs) -> TableInfo:
        """Get a table.
        
        Gets a table from the metastore for a specific catalog and schema. The caller must be a metastore
        admin, be the owner of the table and have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema, or be the owner of the table and have the **SELECT**
        privilege on it as well."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetTableRequest(full_name=full_name, include_delta_metadata=include_delta_metadata)

        query = {}
        if include_delta_metadata: query['include_delta_metadata'] = request.include_delta_metadata

        json = self._api.do('GET', f'/api/2.1/unity-catalog/tables/{request.full_name}', query=query)
        return TableInfo.from_dict(json)

    def list(self,
             catalog_name: str,
             schema_name: str,
             *,
             include_delta_metadata: bool = None,
             **kwargs) -> Iterator[TableInfo]:
        """List tables.
        
        Gets an array of all tables for the current metastore under the parent catalog and schema. The caller
        must be a metastore admin or an owner of (or have the **SELECT** privilege on) the table. For the
        latter case, the caller must also be the owner or have the **USE_CATALOG** privilege on the parent
        catalog and the **USE_SCHEMA** privilege on the parent schema. There is no guarantee of a specific
        ordering of the elements in the array."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListTablesRequest(catalog_name=catalog_name,
                                        include_delta_metadata=include_delta_metadata,
                                        schema_name=schema_name)

        query = {}
        if catalog_name: query['catalog_name'] = request.catalog_name
        if include_delta_metadata: query['include_delta_metadata'] = request.include_delta_metadata
        if schema_name: query['schema_name'] = request.schema_name

        json = self._api.do('GET', '/api/2.1/unity-catalog/tables', query=query)
        return [TableInfo.from_dict(v) for v in json.get('tables', [])]

    def list_summaries(self,
                       catalog_name: str,
                       *,
                       max_results: int = None,
                       page_token: str = None,
                       schema_name_pattern: str = None,
                       table_name_pattern: str = None,
                       **kwargs) -> ListTableSummariesResponse:
        """List table summaries.
        
        Gets an array of summaries for tables for a schema and catalog within the metastore. The table
        summaries returned are either:
        
        * summaries for all tables (within the current metastore and parent catalog and schema), when the user
        is a metastore admin, or: * summaries for all tables and schemas (within the current metastore and
        parent catalog) for which the user has ownership or the **SELECT** privilege on the table and
        ownership or **USE_SCHEMA** privilege on the schema, provided that the user also has ownership or the
        **USE_CATALOG** privilege on the parent catalog.
        
        There is no guarantee of a specific ordering of the elements in the array."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListSummariesRequest(catalog_name=catalog_name,
                                           max_results=max_results,
                                           page_token=page_token,
                                           schema_name_pattern=schema_name_pattern,
                                           table_name_pattern=table_name_pattern)

        query = {}
        if catalog_name: query['catalog_name'] = request.catalog_name
        if max_results: query['max_results'] = request.max_results
        if page_token: query['page_token'] = request.page_token
        if schema_name_pattern: query['schema_name_pattern'] = request.schema_name_pattern
        if table_name_pattern: query['table_name_pattern'] = request.table_name_pattern

        json = self._api.do('GET', '/api/2.1/unity-catalog/table-summaries', query=query)
        return ListTableSummariesResponse.from_dict(json)

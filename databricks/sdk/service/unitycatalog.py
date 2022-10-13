# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'AwsIamRole',
    'AzureServicePrincipal',
    'CatalogInfo',
    'CatalogInfoCatalogType',
    'CatalogInfoPrivilegesItem',
    'ColumnInfo',
    'ColumnInfoTypeName',
    'CreateCatalog',
    'CreateCatalogCatalogType',
    'CreateCatalogPrivilegesItem',
    'CreateCatalogResponse',
    'CreateCatalogResponseCatalogType',
    'CreateCatalogResponsePrivilegesItem',
    'CreateExternalLocation',
    'CreateExternalLocationResponse',
    'CreateMetastore',
    'CreateMetastoreAssignment',
    'CreateMetastorePrivilegesItem',
    'CreateMetastoreResponse',
    'CreateMetastoreResponsePrivilegesItem',
    'CreateProvider',
    'CreateProviderAuthenticationType',
    'CreateProviderResponse',
    'CreateProviderResponseAuthenticationType',
    'CreateRecipient',
    'CreateRecipientAuthenticationType',
    'CreateRecipientResponse',
    'CreateRecipientResponseAuthenticationType',
    'CreateSchema',
    'CreateSchemaPrivilegesItem',
    'CreateSchemaResponse',
    'CreateSchemaResponsePrivilegesItem',
    'CreateShare',
    'CreateShareResponse',
    'CreateStagingTable',
    'CreateStagingTableResponse',
    'CreateStorageCredential',
    'CreateStorageCredentialResponse',
    'CreateTable',
    'CreateTableDataSourceFormat',
    'CreateTablePrivilegesItem',
    'CreateTableResponse',
    'CreateTableResponseDataSourceFormat',
    'CreateTableResponsePrivilegesItem',
    'CreateTableResponseTableType',
    'CreateTableTableType',
    'ExternalLocationInfo',
    'FileInfo',
    'GcpServiceAccountKey',
    'GetCatalogResponse',
    'GetCatalogResponseCatalogType',
    'GetCatalogResponsePrivilegesItem',
    'GetExternalLocationResponse',
    'GetMetastoreResponse',
    'GetMetastoreResponsePrivilegesItem',
    'GetMetastoreSummaryResponse',
    'GetPermissionsResponse',
    'GetProviderResponse',
    'GetProviderResponseAuthenticationType',
    'GetRecipientResponse',
    'GetRecipientResponseAuthenticationType',
    'GetRecipientSharePermissionsResponse',
    'GetSchemaResponse',
    'GetSchemaResponsePrivilegesItem',
    'GetSharePermissionsResponse',
    'GetShareResponse',
    'GetStorageCredentialResponse',
    'GetTableResponse',
    'GetTableResponseDataSourceFormat',
    'GetTableResponsePrivilegesItem',
    'GetTableResponseTableType',
    'IpAccessList',
    'ListCatalogsResponse',
    'ListExternalLocationsResponse',
    'ListFilesRequest',
    'ListFilesResponse',
    'ListMetastoresResponse',
    'ListProviderSharesResponse',
    'ListProvidersResponse',
    'ListRecipientsResponse',
    'ListSchemasResponse',
    'ListSharesResponse',
    'ListStorageCredentialsResponse',
    'ListTableSummariesResponse',
    'ListTablesResponse',
    'MetastoreInfo',
    'MetastoreInfoPrivilegesItem',
    'Partition',
    'PartitionValue',
    'PartitionValueOp',
    'PermissionsChange',
    'PermissionsChangeAddItem',
    'PermissionsChangeRemoveItem',
    'PrivilegeAssignment',
    'PrivilegeAssignmentPrivilegesItem',
    'ProviderInfo',
    'ProviderInfoAuthenticationType',
    'ProviderShare',
    'RecipientInfo',
    'RecipientInfoAuthenticationType',
    'RecipientProfile',
    'RecipientTokenInfo',
    'RetrieveTokenResponse',
    'RotateRecipientToken',
    'RotateRecipientTokenResponse',
    'RotateRecipientTokenResponseAuthenticationType',
    'SchemaInfo',
    'SchemaInfoPrivilegesItem',
    'ShareInfo',
    'ShareToPrivilegeAssignment',
    'SharedDataObject',
    'SharedDataObjectUpdate',
    'SharedDataObjectUpdateAction',
    'StorageCredentialInfo',
    'StringKeyValuePair',
    'TableInfo',
    'TableInfoDataSourceFormat',
    'TableInfoPrivilegesItem',
    'TableInfoTableType',
    'TableSummary',
    'TableSummaryTableType',
    'UpdateCatalog',
    'UpdateCatalogCatalogType',
    'UpdateCatalogPrivilegesItem',
    'UpdateExternalLocation',
    'UpdateMetastore',
    'UpdateMetastoreAssignment',
    'UpdateMetastorePrivilegesItem',
    'UpdatePermissions',
    'UpdateProvider',
    'UpdateProviderAuthenticationType',
    'UpdateRecipient',
    'UpdateRecipientAuthenticationType',
    'UpdateSchema',
    'UpdateSchemaPrivilegesItem',
    'UpdateShare',
    'UpdateSharePermissions',
    'UpdateStorageCredential',
    'UpdateTable',
    'UpdateTableDataSourceFormat',
    'UpdateTablePrivilegesItem',
    'UpdateTableTableType',
    'DeleteCatalogRequest',
    'DeleteExternalLocationRequest',
    'DeleteMetastoreAssignmentRequest',
    'DeleteMetastoreRequest',
    'DeleteProviderRequest',
    'DeleteRecipientRequest',
    'DeleteSchemaRequest',
    'DeleteShareRequest',
    'DeleteStorageCredentialRequest',
    'DeleteTableRequest',
    'GetActivationUrlInfoRequest',
    'GetCatalogRequest',
    'GetExternalLocationRequest',
    'GetMetastoreRequest',
    'GetPermissionsRequest',
    'GetProviderRequest',
    'GetRecipientRequest',
    'GetRecipientSharePermissionsRequest',
    'GetSchemaRequest',
    'GetSharePermissionsRequest',
    'GetShareRequest',
    'GetStorageCredentialsRequest',
    'GetTableRequest',
    'ListRequest',
    'ListSharesRequest',
    'ListTableSummariesRequest',
    'RetrieveTokenRequest',
    
    'Catalogs',
    'ExternalLocations',
    'Grants',
    'Metastores',
    'Providers',
    'RecipientActivation',
    'Recipients',
    'Schemas',
    'Shares',
    'StorageCredentials',
    'Tables',
    'UnityFiles',
]

# all definitions in this file are in alphabetical order

@dataclass
class AwsIamRole:
    
    # The external ID used in role assumption to prevent confused deputy
    # problem.
    # 
    # [Create:IGN].
    external_id: str = None
    # The Amazon Resource Name (ARN) of the AWS IAM role for S3 data access.
    # [Create:REQ].
    role_arn: str = None
    # The Amazon Resource Name (ARN) of the AWS IAM user managed by Databricks.
    # This is the identity that is going to assume the AWS IAM role.
    # 
    # [Create:IGN].
    unity_catalog_iam_arn: str = None

    def as_request(self) -> (dict, dict):
        awsIamRole_query, awsIamRole_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.external_id:
            awsIamRole_body['external_id'] = self.external_id
        if self.role_arn:
            awsIamRole_body['role_arn'] = self.role_arn
        if self.unity_catalog_iam_arn:
            awsIamRole_body['unity_catalog_iam_arn'] = self.unity_catalog_iam_arn
        
        return awsIamRole_query, awsIamRole_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AwsIamRole':
        return cls(
            external_id=d.get('external_id', None),
            role_arn=d.get('role_arn', None),
            unity_catalog_iam_arn=d.get('unity_catalog_iam_arn', None),
        )



@dataclass
class AzureServicePrincipal:
    
    # The application ID of the application registration within the referenced
    # AAD tenant. [Create:REQ]
    application_id: str = None
    # The client secret generated for the above app ID in AAD. [Create:REQ]
    client_secret: str = None
    # The directory ID corresponding to the Azure Active Directory (AAD) tenant
    # of the application. [Create:REQ].
    directory_id: str = None

    def as_request(self) -> (dict, dict):
        azureServicePrincipal_query, azureServicePrincipal_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.application_id:
            azureServicePrincipal_body['application_id'] = self.application_id
        if self.client_secret:
            azureServicePrincipal_body['client_secret'] = self.client_secret
        if self.directory_id:
            azureServicePrincipal_body['directory_id'] = self.directory_id
        
        return azureServicePrincipal_query, azureServicePrincipal_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AzureServicePrincipal':
        return cls(
            application_id=d.get('application_id', None),
            client_secret=d.get('client_secret', None),
            directory_id=d.get('directory_id', None),
        )



@dataclass
class CatalogInfo:
    
    # [Create,Update:IGN] The type of the catalog.
    catalog_type: 'CatalogInfoCatalogType' = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Catalog was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Catalog creator.
    created_by: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Catalog.
    name: str = None
    # [Create:IGN,Update:OPT] Username of current owner of Catalog.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Catalog.
    privileges: 'List[CatalogInfoPrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # Delta Sharing Catalog specific fields. A Delta Sharing Catalog is a
    # catalog that is based on a Delta share on a remote sharing server.
    # [Create:OPT,Update:IGN] The name of delta sharing provider.
    provider_name: str = None
    # [Create:OPT,Update: IGN] The name of the share under the share provider.
    share_name: str = None
    # [Create,Update:IGN] Time at which this Catalog was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Catalog.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        catalogInfo_query, catalogInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_type:
            catalogInfo_body['catalog_type'] = self.catalog_type.value
        if self.comment:
            catalogInfo_body['comment'] = self.comment
        if self.created_at:
            catalogInfo_body['created_at'] = self.created_at
        if self.created_by:
            catalogInfo_body['created_by'] = self.created_by
        if self.metastore_id:
            catalogInfo_body['metastore_id'] = self.metastore_id
        if self.name:
            catalogInfo_body['name'] = self.name
        if self.owner:
            catalogInfo_body['owner'] = self.owner
        if self.privileges:
            catalogInfo_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            catalogInfo_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.provider_name:
            catalogInfo_body['provider_name'] = self.provider_name
        if self.share_name:
            catalogInfo_body['share_name'] = self.share_name
        if self.updated_at:
            catalogInfo_body['updated_at'] = self.updated_at
        if self.updated_by:
            catalogInfo_body['updated_by'] = self.updated_by
        
        return catalogInfo_query, catalogInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CatalogInfo':
        return cls(
            catalog_type=CatalogInfoCatalogType(d['catalog_type']) if 'catalog_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            provider_name=d.get('provider_name', None),
            share_name=d.get('share_name', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class CatalogInfoCatalogType(Enum):
    """[Create,Update:IGN] The type of the catalog."""
    
    DELTASHARING_CATALOG = 'DELTASHARING_CATALOG'
    MANAGED_CATALOG = 'MANAGED_CATALOG'
    SYSTEM_CATALOG = 'SYSTEM_CATALOG'
    UNKNOWN_CATALOG_TYPE = 'UNKNOWN_CATALOG_TYPE'

class CatalogInfoPrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class ColumnInfo:
    
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create:REQ Update:OPT] Name of Column.
    name: str = None
    # [Create,Update:OPT] Whether field may be Null (default: True).
    nullable: bool = None
    # [Create,Update:OPT] Partition index for column.
    partition_index: int = None
    # [Create:REQ Update:OPT] Ordinal position of column (starting at position
    # 0).
    position: int = None
    # [Create: OPT, Update: OPT] Format of IntervalType.
    type_interval_type: str = None
    # [Create:OPT Update:OPT] Full data type spec, JSON-serialized.
    type_json: str = None
    # [Create: REQ Update: OPT] Name of type (INT, STRUCT, MAP, etc.)
    type_name: 'ColumnInfoTypeName' = None
    # [Create: OPT, Update: OPT] Digits of precision; required on Create for
    # DecimalTypes.
    type_precision: int = None
    # [Create: OPT, Update: OPT] Digits to right of decimal; Required on Create
    # for DecimalTypes.
    type_scale: int = None
    # [Create:REQ Update:OPT] Full data type spec, SQL/catalogString text.
    type_text: str = None

    def as_request(self) -> (dict, dict):
        columnInfo_query, columnInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.comment:
            columnInfo_body['comment'] = self.comment
        if self.name:
            columnInfo_body['name'] = self.name
        if self.nullable:
            columnInfo_body['nullable'] = self.nullable
        if self.partition_index:
            columnInfo_body['partition_index'] = self.partition_index
        if self.position:
            columnInfo_body['position'] = self.position
        if self.type_interval_type:
            columnInfo_body['type_interval_type'] = self.type_interval_type
        if self.type_json:
            columnInfo_body['type_json'] = self.type_json
        if self.type_name:
            columnInfo_body['type_name'] = self.type_name.value
        if self.type_precision:
            columnInfo_body['type_precision'] = self.type_precision
        if self.type_scale:
            columnInfo_body['type_scale'] = self.type_scale
        if self.type_text:
            columnInfo_body['type_text'] = self.type_text
        
        return columnInfo_query, columnInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ColumnInfo':
        return cls(
            comment=d.get('comment', None),
            name=d.get('name', None),
            nullable=d.get('nullable', None),
            partition_index=d.get('partition_index', None),
            position=d.get('position', None),
            type_interval_type=d.get('type_interval_type', None),
            type_json=d.get('type_json', None),
            type_name=ColumnInfoTypeName(d['type_name']) if 'type_name' in d else None,
            type_precision=d.get('type_precision', None),
            type_scale=d.get('type_scale', None),
            type_text=d.get('type_text', None),
        )



class ColumnInfoTypeName(Enum):
    """[Create: REQ Update: OPT] Name of type (INT, STRUCT, MAP, etc.)"""
    
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
    TIMESTAMP = 'TIMESTAMP'
    UNKNOWN_COLUMN_TYPE_NAME = 'UNKNOWN_COLUMN_TYPE_NAME'

@dataclass
class CreateCatalog:
    
    # [Create,Update:IGN] The type of the catalog.
    catalog_type: 'CreateCatalogCatalogType' = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Catalog was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Catalog creator.
    created_by: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Catalog.
    name: str = None
    # [Create:IGN,Update:OPT] Username of current owner of Catalog.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Catalog.
    privileges: 'List[CreateCatalogPrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # Delta Sharing Catalog specific fields. A Delta Sharing Catalog is a
    # catalog that is based on a Delta share on a remote sharing server.
    # [Create:OPT,Update:IGN] The name of delta sharing provider.
    provider_name: str = None
    # [Create:OPT,Update: IGN] The name of the share under the share provider.
    share_name: str = None
    # [Create,Update:IGN] Time at which this Catalog was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Catalog.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        createCatalog_query, createCatalog_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_type:
            createCatalog_body['catalog_type'] = self.catalog_type.value
        if self.comment:
            createCatalog_body['comment'] = self.comment
        if self.created_at:
            createCatalog_body['created_at'] = self.created_at
        if self.created_by:
            createCatalog_body['created_by'] = self.created_by
        if self.metastore_id:
            createCatalog_body['metastore_id'] = self.metastore_id
        if self.name:
            createCatalog_body['name'] = self.name
        if self.owner:
            createCatalog_body['owner'] = self.owner
        if self.privileges:
            createCatalog_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            createCatalog_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.provider_name:
            createCatalog_body['provider_name'] = self.provider_name
        if self.share_name:
            createCatalog_body['share_name'] = self.share_name
        if self.updated_at:
            createCatalog_body['updated_at'] = self.updated_at
        if self.updated_by:
            createCatalog_body['updated_by'] = self.updated_by
        
        return createCatalog_query, createCatalog_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCatalog':
        return cls(
            catalog_type=CreateCatalogCatalogType(d['catalog_type']) if 'catalog_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            provider_name=d.get('provider_name', None),
            share_name=d.get('share_name', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class CreateCatalogCatalogType(Enum):
    """[Create,Update:IGN] The type of the catalog."""
    
    DELTASHARING_CATALOG = 'DELTASHARING_CATALOG'
    MANAGED_CATALOG = 'MANAGED_CATALOG'
    SYSTEM_CATALOG = 'SYSTEM_CATALOG'
    UNKNOWN_CATALOG_TYPE = 'UNKNOWN_CATALOG_TYPE'

class CreateCatalogPrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class CreateCatalogResponse:
    
    # [Create,Update:IGN] The type of the catalog.
    catalog_type: 'CreateCatalogResponseCatalogType' = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Catalog was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Catalog creator.
    created_by: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Catalog.
    name: str = None
    # [Create:IGN,Update:OPT] Username of current owner of Catalog.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Catalog.
    privileges: 'List[CreateCatalogResponsePrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # Delta Sharing Catalog specific fields. A Delta Sharing Catalog is a
    # catalog that is based on a Delta share on a remote sharing server.
    # [Create:OPT,Update:IGN] The name of delta sharing provider.
    provider_name: str = None
    # [Create:OPT,Update: IGN] The name of the share under the share provider.
    share_name: str = None
    # [Create,Update:IGN] Time at which this Catalog was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Catalog.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        createCatalogResponse_query, createCatalogResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_type:
            createCatalogResponse_body['catalog_type'] = self.catalog_type.value
        if self.comment:
            createCatalogResponse_body['comment'] = self.comment
        if self.created_at:
            createCatalogResponse_body['created_at'] = self.created_at
        if self.created_by:
            createCatalogResponse_body['created_by'] = self.created_by
        if self.metastore_id:
            createCatalogResponse_body['metastore_id'] = self.metastore_id
        if self.name:
            createCatalogResponse_body['name'] = self.name
        if self.owner:
            createCatalogResponse_body['owner'] = self.owner
        if self.privileges:
            createCatalogResponse_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            createCatalogResponse_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.provider_name:
            createCatalogResponse_body['provider_name'] = self.provider_name
        if self.share_name:
            createCatalogResponse_body['share_name'] = self.share_name
        if self.updated_at:
            createCatalogResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            createCatalogResponse_body['updated_by'] = self.updated_by
        
        return createCatalogResponse_query, createCatalogResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCatalogResponse':
        return cls(
            catalog_type=CreateCatalogResponseCatalogType(d['catalog_type']) if 'catalog_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            provider_name=d.get('provider_name', None),
            share_name=d.get('share_name', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class CreateCatalogResponseCatalogType(Enum):
    """[Create,Update:IGN] The type of the catalog."""
    
    DELTASHARING_CATALOG = 'DELTASHARING_CATALOG'
    MANAGED_CATALOG = 'MANAGED_CATALOG'
    SYSTEM_CATALOG = 'SYSTEM_CATALOG'
    UNKNOWN_CATALOG_TYPE = 'UNKNOWN_CATALOG_TYPE'

class CreateCatalogResponsePrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class CreateExternalLocation:
    
    # [Create:OPT Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this External Location was created, in
    # epoch milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of External Location creator.
    created_by: str = None
    # [Create,Update:IGN] Unique ID of the location's Storage Credential.
    credential_id: str = None
    # [Create:REQ Update:OPT] Current name of the Storage Credential this
    # location uses.
    credential_name: str = None
    # [Create,Update:IGN] Unique identifier of Metastore hosting the External
    # Location.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of the External Location.
    name: str = None
    # [Create:IGN Update:OPT] The owner of the External Location.
    owner: str = None
    # [Create,Update:IGN] Time at which this was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the External
    # Location.
    updated_by: str = None
    # [Create:REQ Update:OPT] Path URL of the External Location.
    url: str = None

    def as_request(self) -> (dict, dict):
        createExternalLocation_query, createExternalLocation_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.comment:
            createExternalLocation_body['comment'] = self.comment
        if self.created_at:
            createExternalLocation_body['created_at'] = self.created_at
        if self.created_by:
            createExternalLocation_body['created_by'] = self.created_by
        if self.credential_id:
            createExternalLocation_body['credential_id'] = self.credential_id
        if self.credential_name:
            createExternalLocation_body['credential_name'] = self.credential_name
        if self.metastore_id:
            createExternalLocation_body['metastore_id'] = self.metastore_id
        if self.name:
            createExternalLocation_body['name'] = self.name
        if self.owner:
            createExternalLocation_body['owner'] = self.owner
        if self.updated_at:
            createExternalLocation_body['updated_at'] = self.updated_at
        if self.updated_by:
            createExternalLocation_body['updated_by'] = self.updated_by
        if self.url:
            createExternalLocation_body['url'] = self.url
        
        return createExternalLocation_query, createExternalLocation_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateExternalLocation':
        return cls(
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            credential_id=d.get('credential_id', None),
            credential_name=d.get('credential_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
            url=d.get('url', None),
        )



@dataclass
class CreateExternalLocationResponse:
    
    # [Create:OPT Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this External Location was created, in
    # epoch milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of External Location creator.
    created_by: str = None
    # [Create,Update:IGN] Unique ID of the location's Storage Credential.
    credential_id: str = None
    # [Create:REQ Update:OPT] Current name of the Storage Credential this
    # location uses.
    credential_name: str = None
    # [Create,Update:IGN] Unique identifier of Metastore hosting the External
    # Location.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of the External Location.
    name: str = None
    # [Create:IGN Update:OPT] The owner of the External Location.
    owner: str = None
    # [Create,Update:IGN] Time at which this was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the External
    # Location.
    updated_by: str = None
    # [Create:REQ Update:OPT] Path URL of the External Location.
    url: str = None

    def as_request(self) -> (dict, dict):
        createExternalLocationResponse_query, createExternalLocationResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.comment:
            createExternalLocationResponse_body['comment'] = self.comment
        if self.created_at:
            createExternalLocationResponse_body['created_at'] = self.created_at
        if self.created_by:
            createExternalLocationResponse_body['created_by'] = self.created_by
        if self.credential_id:
            createExternalLocationResponse_body['credential_id'] = self.credential_id
        if self.credential_name:
            createExternalLocationResponse_body['credential_name'] = self.credential_name
        if self.metastore_id:
            createExternalLocationResponse_body['metastore_id'] = self.metastore_id
        if self.name:
            createExternalLocationResponse_body['name'] = self.name
        if self.owner:
            createExternalLocationResponse_body['owner'] = self.owner
        if self.updated_at:
            createExternalLocationResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            createExternalLocationResponse_body['updated_by'] = self.updated_by
        if self.url:
            createExternalLocationResponse_body['url'] = self.url
        
        return createExternalLocationResponse_query, createExternalLocationResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateExternalLocationResponse':
        return cls(
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            credential_id=d.get('credential_id', None),
            credential_name=d.get('credential_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
            url=d.get('url', None),
        )



@dataclass
class CreateMetastore:
    
    # [Create,Update:IGN] Time at which this Metastore was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Metastore creator.
    created_by: str = None
    # [Create:IGN Update:OPT] Unique identifier of (Default) Data Access
    # Configuration
    default_data_access_config_id: str = None
    # [Create:IGN Update:OPT] Whether Delta Sharing is enabled on this
    # metastore.
    delta_sharing_enabled: bool = None
    # [Create:IGN Update:OPT] The lifetime of delta sharing recipient token in
    # seconds
    delta_sharing_recipient_token_lifetime_in_seconds: int = None
    # [Create,Update:IGN] Unique identifier of Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Metastore.
    name: str = None
    # [Create:IGN Update:OPT] The owner of the metastore.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Metastore.
    privileges: 'List[CreateMetastorePrivilegesItem]' = None
    # The region this metastore has an afinity to. This is used by
    # accounts-manager. Ignored by Unity Catalog.
    region: str = None
    # [Create:REQ Update:ERR] Storage root URL for Metastore
    storage_root: str = None
    # [Create:IGN Update:OPT] UUID of storage credential to access storage_root
    storage_root_credential_id: str = None
    # [Create,Update:IGN] Time at which the Metastore was last modified, in
    # epoch milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the Metastore.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        createMetastore_query, createMetastore_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.created_at:
            createMetastore_body['created_at'] = self.created_at
        if self.created_by:
            createMetastore_body['created_by'] = self.created_by
        if self.default_data_access_config_id:
            createMetastore_body['default_data_access_config_id'] = self.default_data_access_config_id
        if self.delta_sharing_enabled:
            createMetastore_body['delta_sharing_enabled'] = self.delta_sharing_enabled
        if self.delta_sharing_recipient_token_lifetime_in_seconds:
            createMetastore_body['delta_sharing_recipient_token_lifetime_in_seconds'] = self.delta_sharing_recipient_token_lifetime_in_seconds
        if self.metastore_id:
            createMetastore_body['metastore_id'] = self.metastore_id
        if self.name:
            createMetastore_body['name'] = self.name
        if self.owner:
            createMetastore_body['owner'] = self.owner
        if self.privileges:
            createMetastore_body['privileges'] = [v for v in self.privileges]
        if self.region:
            createMetastore_body['region'] = self.region
        if self.storage_root:
            createMetastore_body['storage_root'] = self.storage_root
        if self.storage_root_credential_id:
            createMetastore_body['storage_root_credential_id'] = self.storage_root_credential_id
        if self.updated_at:
            createMetastore_body['updated_at'] = self.updated_at
        if self.updated_by:
            createMetastore_body['updated_by'] = self.updated_by
        
        return createMetastore_query, createMetastore_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateMetastore':
        return cls(
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            default_data_access_config_id=d.get('default_data_access_config_id', None),
            delta_sharing_enabled=d.get('delta_sharing_enabled', None),
            delta_sharing_recipient_token_lifetime_in_seconds=d.get('delta_sharing_recipient_token_lifetime_in_seconds', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            region=d.get('region', None),
            storage_root=d.get('storage_root', None),
            storage_root_credential_id=d.get('storage_root_credential_id', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



@dataclass
class CreateMetastoreAssignment:
    
    # THe name of the default catalog in the Metastore.
    default_catalog_name: str
    # The ID of the Metastore.
    metastore_id: str
    # A workspace ID.
    workspace_id: int # path

    def as_request(self) -> (dict, dict):
        createMetastoreAssignment_query, createMetastoreAssignment_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.default_catalog_name:
            createMetastoreAssignment_body['default_catalog_name'] = self.default_catalog_name
        if self.metastore_id:
            createMetastoreAssignment_body['metastore_id'] = self.metastore_id
        if self.workspace_id:
            createMetastoreAssignment_body['workspace_id'] = self.workspace_id
        
        return createMetastoreAssignment_query, createMetastoreAssignment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateMetastoreAssignment':
        return cls(
            default_catalog_name=d.get('default_catalog_name', None),
            metastore_id=d.get('metastore_id', None),
            workspace_id=d.get('workspace_id', None),
        )



class CreateMetastorePrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class CreateMetastoreResponse:
    
    # [Create,Update:IGN] Time at which this Metastore was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Metastore creator.
    created_by: str = None
    # [Create:IGN Update:OPT] Unique identifier of (Default) Data Access
    # Configuration
    default_data_access_config_id: str = None
    # [Create:IGN Update:OPT] Whether Delta Sharing is enabled on this
    # metastore.
    delta_sharing_enabled: bool = None
    # [Create:IGN Update:OPT] The lifetime of delta sharing recipient token in
    # seconds
    delta_sharing_recipient_token_lifetime_in_seconds: int = None
    # [Create,Update:IGN] Unique identifier of Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Metastore.
    name: str = None
    # [Create:IGN Update:OPT] The owner of the metastore.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Metastore.
    privileges: 'List[CreateMetastoreResponsePrivilegesItem]' = None
    # The region this metastore has an afinity to. This is used by
    # accounts-manager. Ignored by Unity Catalog.
    region: str = None
    # [Create:REQ Update:ERR] Storage root URL for Metastore
    storage_root: str = None
    # [Create:IGN Update:OPT] UUID of storage credential to access storage_root
    storage_root_credential_id: str = None
    # [Create,Update:IGN] Time at which the Metastore was last modified, in
    # epoch milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the Metastore.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        createMetastoreResponse_query, createMetastoreResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.created_at:
            createMetastoreResponse_body['created_at'] = self.created_at
        if self.created_by:
            createMetastoreResponse_body['created_by'] = self.created_by
        if self.default_data_access_config_id:
            createMetastoreResponse_body['default_data_access_config_id'] = self.default_data_access_config_id
        if self.delta_sharing_enabled:
            createMetastoreResponse_body['delta_sharing_enabled'] = self.delta_sharing_enabled
        if self.delta_sharing_recipient_token_lifetime_in_seconds:
            createMetastoreResponse_body['delta_sharing_recipient_token_lifetime_in_seconds'] = self.delta_sharing_recipient_token_lifetime_in_seconds
        if self.metastore_id:
            createMetastoreResponse_body['metastore_id'] = self.metastore_id
        if self.name:
            createMetastoreResponse_body['name'] = self.name
        if self.owner:
            createMetastoreResponse_body['owner'] = self.owner
        if self.privileges:
            createMetastoreResponse_body['privileges'] = [v for v in self.privileges]
        if self.region:
            createMetastoreResponse_body['region'] = self.region
        if self.storage_root:
            createMetastoreResponse_body['storage_root'] = self.storage_root
        if self.storage_root_credential_id:
            createMetastoreResponse_body['storage_root_credential_id'] = self.storage_root_credential_id
        if self.updated_at:
            createMetastoreResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            createMetastoreResponse_body['updated_by'] = self.updated_by
        
        return createMetastoreResponse_query, createMetastoreResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateMetastoreResponse':
        return cls(
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            default_data_access_config_id=d.get('default_data_access_config_id', None),
            delta_sharing_enabled=d.get('delta_sharing_enabled', None),
            delta_sharing_recipient_token_lifetime_in_seconds=d.get('delta_sharing_recipient_token_lifetime_in_seconds', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            region=d.get('region', None),
            storage_root=d.get('storage_root', None),
            storage_root_credential_id=d.get('storage_root_credential_id', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class CreateMetastoreResponsePrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class CreateProvider:
    
    # [Create,Update:IGN] Whether this provider is successfully activated by the
    # data provider. This field is only present when the authentication type is
    # DATABRICKS.
    activated_by_provider: bool = None
    # [Create:REQ,Update:IGN] The delta sharing authentication type.
    authentication_type: 'CreateProviderAuthenticationType' = None
    # [Create,Update:OPT] Description about the provider.
    comment: str = None
    # [Create,Update:IGN] Time at which this Provider was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Provider creator.
    created_by: str = None
    # [Create,Update:REQ] The name of the Provider.
    name: str = None
    # [Create,Update:IGN] This field is only present when the authentication
    # type is TOKEN.
    recipient_profile: 'RecipientProfile' = None
    # [Create,Update:OPT] This field is only present when the authentication
    # type is TOKEN.
    recipient_profile_str: str = None
    # [Create,Update:IGN] The server-generated one-time sharing code. This field
    # is only present when the authentication type is DATABRICKS.
    sharing_code: str = None
    # [Create,Update:IGN] Time at which this Provider was created, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Share.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        createProvider_query, createProvider_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activated_by_provider:
            createProvider_body['activated_by_provider'] = self.activated_by_provider
        if self.authentication_type:
            createProvider_body['authentication_type'] = self.authentication_type.value
        if self.comment:
            createProvider_body['comment'] = self.comment
        if self.created_at:
            createProvider_body['created_at'] = self.created_at
        if self.created_by:
            createProvider_body['created_by'] = self.created_by
        if self.name:
            createProvider_body['name'] = self.name
        if self.recipient_profile:
            createProvider_body['recipient_profile'] = self.recipient_profile.as_request()[1]
        if self.recipient_profile_str:
            createProvider_body['recipient_profile_str'] = self.recipient_profile_str
        if self.sharing_code:
            createProvider_body['sharing_code'] = self.sharing_code
        if self.updated_at:
            createProvider_body['updated_at'] = self.updated_at
        if self.updated_by:
            createProvider_body['updated_by'] = self.updated_by
        
        return createProvider_query, createProvider_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateProvider':
        return cls(
            activated_by_provider=d.get('activated_by_provider', None),
            authentication_type=CreateProviderAuthenticationType(d['authentication_type']) if 'authentication_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            name=d.get('name', None),
            recipient_profile=RecipientProfile.from_dict(d['recipient_profile']) if 'recipient_profile' in d else None,
            recipient_profile_str=d.get('recipient_profile_str', None),
            sharing_code=d.get('sharing_code', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class CreateProviderAuthenticationType(Enum):
    """[Create:REQ,Update:IGN] The delta sharing authentication type."""
    
    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'
    UNKNOWN = 'UNKNOWN'

@dataclass
class CreateProviderResponse:
    
    # [Create,Update:IGN] Whether this provider is successfully activated by the
    # data provider. This field is only present when the authentication type is
    # DATABRICKS.
    activated_by_provider: bool = None
    # [Create:REQ,Update:IGN] The delta sharing authentication type.
    authentication_type: 'CreateProviderResponseAuthenticationType' = None
    # [Create,Update:OPT] Description about the provider.
    comment: str = None
    # [Create,Update:IGN] Time at which this Provider was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Provider creator.
    created_by: str = None
    # [Create,Update:REQ] The name of the Provider.
    name: str = None
    # [Create,Update:IGN] This field is only present when the authentication
    # type is TOKEN.
    recipient_profile: 'RecipientProfile' = None
    # [Create,Update:OPT] This field is only present when the authentication
    # type is TOKEN.
    recipient_profile_str: str = None
    # [Create,Update:IGN] The server-generated one-time sharing code. This field
    # is only present when the authentication type is DATABRICKS.
    sharing_code: str = None
    # [Create,Update:IGN] Time at which this Provider was created, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Share.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        createProviderResponse_query, createProviderResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activated_by_provider:
            createProviderResponse_body['activated_by_provider'] = self.activated_by_provider
        if self.authentication_type:
            createProviderResponse_body['authentication_type'] = self.authentication_type.value
        if self.comment:
            createProviderResponse_body['comment'] = self.comment
        if self.created_at:
            createProviderResponse_body['created_at'] = self.created_at
        if self.created_by:
            createProviderResponse_body['created_by'] = self.created_by
        if self.name:
            createProviderResponse_body['name'] = self.name
        if self.recipient_profile:
            createProviderResponse_body['recipient_profile'] = self.recipient_profile.as_request()[1]
        if self.recipient_profile_str:
            createProviderResponse_body['recipient_profile_str'] = self.recipient_profile_str
        if self.sharing_code:
            createProviderResponse_body['sharing_code'] = self.sharing_code
        if self.updated_at:
            createProviderResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            createProviderResponse_body['updated_by'] = self.updated_by
        
        return createProviderResponse_query, createProviderResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateProviderResponse':
        return cls(
            activated_by_provider=d.get('activated_by_provider', None),
            authentication_type=CreateProviderResponseAuthenticationType(d['authentication_type']) if 'authentication_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            name=d.get('name', None),
            recipient_profile=RecipientProfile.from_dict(d['recipient_profile']) if 'recipient_profile' in d else None,
            recipient_profile_str=d.get('recipient_profile_str', None),
            sharing_code=d.get('sharing_code', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class CreateProviderResponseAuthenticationType(Enum):
    """[Create:REQ,Update:IGN] The delta sharing authentication type."""
    
    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'
    UNKNOWN = 'UNKNOWN'

@dataclass
class CreateRecipient:
    
    # [Create:IGN,Update:IGN] A boolean status field showing whether the
    # Recipient's activation URL has been exercised or not.
    activated: bool = None
    # [Create:IGN,Update:IGN] Full activation url to retrieve the access token.
    # It will be empty if the token is already retrieved.
    activation_url: str = None
    # [Create:REQ,Update:IGN] The delta sharing authentication type.
    authentication_type: 'CreateRecipientAuthenticationType' = None
    # [Create:OPT,Update:OPT] Description about the recipient.
    comment: str = None
    # [Create:IGN,Update:IGN] Time at which this recipient was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create:IGN,Update:IGN] Username of recipient creator.
    created_by: str = None
    # [Create:OPT,Update:OPT] IP Access List
    ip_access_list: 'IpAccessList' = None
    # [Create:REQ,Update:OPT] Name of Recipient.
    name: str = None
    # [Create:OPT,Update:IGN] The one-time sharing code provided by the data
    # recipient. This field is only present when the authentication type is
    # DATABRICKS.
    sharing_code: str = None
    # [Create:IGN,Update:IGN] recipient Tokens This field is only present when
    # the authentication type is TOKEN.
    tokens: 'List[RecipientTokenInfo]' = None
    # [Create:IGN,Update:IGN] Time at which the recipient was updated, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create:IGN,Update:IGN] Username of recipient updater.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        createRecipient_query, createRecipient_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activated:
            createRecipient_body['activated'] = self.activated
        if self.activation_url:
            createRecipient_body['activation_url'] = self.activation_url
        if self.authentication_type:
            createRecipient_body['authentication_type'] = self.authentication_type.value
        if self.comment:
            createRecipient_body['comment'] = self.comment
        if self.created_at:
            createRecipient_body['created_at'] = self.created_at
        if self.created_by:
            createRecipient_body['created_by'] = self.created_by
        if self.ip_access_list:
            createRecipient_body['ip_access_list'] = self.ip_access_list.as_request()[1]
        if self.name:
            createRecipient_body['name'] = self.name
        if self.sharing_code:
            createRecipient_body['sharing_code'] = self.sharing_code
        if self.tokens:
            createRecipient_body['tokens'] = [v.as_request()[1] for v in self.tokens]
        if self.updated_at:
            createRecipient_body['updated_at'] = self.updated_at
        if self.updated_by:
            createRecipient_body['updated_by'] = self.updated_by
        
        return createRecipient_query, createRecipient_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRecipient':
        return cls(
            activated=d.get('activated', None),
            activation_url=d.get('activation_url', None),
            authentication_type=CreateRecipientAuthenticationType(d['authentication_type']) if 'authentication_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            ip_access_list=IpAccessList.from_dict(d['ip_access_list']) if 'ip_access_list' in d else None,
            name=d.get('name', None),
            sharing_code=d.get('sharing_code', None),
            tokens=[RecipientTokenInfo.from_dict(v) for v in d['tokens']] if 'tokens' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class CreateRecipientAuthenticationType(Enum):
    """[Create:REQ,Update:IGN] The delta sharing authentication type."""
    
    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'
    UNKNOWN = 'UNKNOWN'

@dataclass
class CreateRecipientResponse:
    
    # [Create:IGN,Update:IGN] A boolean status field showing whether the
    # Recipient's activation URL has been exercised or not.
    activated: bool = None
    # [Create:IGN,Update:IGN] Full activation url to retrieve the access token.
    # It will be empty if the token is already retrieved.
    activation_url: str = None
    # [Create:REQ,Update:IGN] The delta sharing authentication type.
    authentication_type: 'CreateRecipientResponseAuthenticationType' = None
    # [Create:OPT,Update:OPT] Description about the recipient.
    comment: str = None
    # [Create:IGN,Update:IGN] Time at which this recipient was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create:IGN,Update:IGN] Username of recipient creator.
    created_by: str = None
    # [Create:OPT,Update:OPT] IP Access List
    ip_access_list: 'IpAccessList' = None
    # [Create:REQ,Update:OPT] Name of Recipient.
    name: str = None
    # [Create:OPT,Update:IGN] The one-time sharing code provided by the data
    # recipient. This field is only present when the authentication type is
    # DATABRICKS.
    sharing_code: str = None
    # [Create:IGN,Update:IGN] recipient Tokens This field is only present when
    # the authentication type is TOKEN.
    tokens: 'List[RecipientTokenInfo]' = None
    # [Create:IGN,Update:IGN] Time at which the recipient was updated, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create:IGN,Update:IGN] Username of recipient updater.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        createRecipientResponse_query, createRecipientResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activated:
            createRecipientResponse_body['activated'] = self.activated
        if self.activation_url:
            createRecipientResponse_body['activation_url'] = self.activation_url
        if self.authentication_type:
            createRecipientResponse_body['authentication_type'] = self.authentication_type.value
        if self.comment:
            createRecipientResponse_body['comment'] = self.comment
        if self.created_at:
            createRecipientResponse_body['created_at'] = self.created_at
        if self.created_by:
            createRecipientResponse_body['created_by'] = self.created_by
        if self.ip_access_list:
            createRecipientResponse_body['ip_access_list'] = self.ip_access_list.as_request()[1]
        if self.name:
            createRecipientResponse_body['name'] = self.name
        if self.sharing_code:
            createRecipientResponse_body['sharing_code'] = self.sharing_code
        if self.tokens:
            createRecipientResponse_body['tokens'] = [v.as_request()[1] for v in self.tokens]
        if self.updated_at:
            createRecipientResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            createRecipientResponse_body['updated_by'] = self.updated_by
        
        return createRecipientResponse_query, createRecipientResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRecipientResponse':
        return cls(
            activated=d.get('activated', None),
            activation_url=d.get('activation_url', None),
            authentication_type=CreateRecipientResponseAuthenticationType(d['authentication_type']) if 'authentication_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            ip_access_list=IpAccessList.from_dict(d['ip_access_list']) if 'ip_access_list' in d else None,
            name=d.get('name', None),
            sharing_code=d.get('sharing_code', None),
            tokens=[RecipientTokenInfo.from_dict(v) for v in d['tokens']] if 'tokens' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class CreateRecipientResponseAuthenticationType(Enum):
    """[Create:REQ,Update:IGN] The delta sharing authentication type."""
    
    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'
    UNKNOWN = 'UNKNOWN'

@dataclass
class CreateSchema:
    
    # [Create:REQ Update:IGN] Name of parent Catalog.
    catalog_name: str = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Schema was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Schema creator.
    created_by: str = None
    # [Create,Update:IGN] Full name of Schema, in form of
    # <catalog_name>.<schema_name>.
    full_name: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Schema, relative to parent Catalog.
    name: str = None
    # [Create:IGN Update:OPT] Username of current owner of Schema.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Schema.
    privileges: 'List[CreateSchemaPrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # [Create,Update:IGN] Time at which this Schema was created, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Schema.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        createSchema_query, createSchema_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            createSchema_body['catalog_name'] = self.catalog_name
        if self.comment:
            createSchema_body['comment'] = self.comment
        if self.created_at:
            createSchema_body['created_at'] = self.created_at
        if self.created_by:
            createSchema_body['created_by'] = self.created_by
        if self.full_name:
            createSchema_body['full_name'] = self.full_name
        if self.metastore_id:
            createSchema_body['metastore_id'] = self.metastore_id
        if self.name:
            createSchema_body['name'] = self.name
        if self.owner:
            createSchema_body['owner'] = self.owner
        if self.privileges:
            createSchema_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            createSchema_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.updated_at:
            createSchema_body['updated_at'] = self.updated_at
        if self.updated_by:
            createSchema_body['updated_by'] = self.updated_by
        
        return createSchema_query, createSchema_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateSchema':
        return cls(
            catalog_name=d.get('catalog_name', None),
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            full_name=d.get('full_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class CreateSchemaPrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class CreateSchemaResponse:
    
    # [Create:REQ Update:IGN] Name of parent Catalog.
    catalog_name: str = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Schema was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Schema creator.
    created_by: str = None
    # [Create,Update:IGN] Full name of Schema, in form of
    # <catalog_name>.<schema_name>.
    full_name: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Schema, relative to parent Catalog.
    name: str = None
    # [Create:IGN Update:OPT] Username of current owner of Schema.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Schema.
    privileges: 'List[CreateSchemaResponsePrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # [Create,Update:IGN] Time at which this Schema was created, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Schema.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        createSchemaResponse_query, createSchemaResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            createSchemaResponse_body['catalog_name'] = self.catalog_name
        if self.comment:
            createSchemaResponse_body['comment'] = self.comment
        if self.created_at:
            createSchemaResponse_body['created_at'] = self.created_at
        if self.created_by:
            createSchemaResponse_body['created_by'] = self.created_by
        if self.full_name:
            createSchemaResponse_body['full_name'] = self.full_name
        if self.metastore_id:
            createSchemaResponse_body['metastore_id'] = self.metastore_id
        if self.name:
            createSchemaResponse_body['name'] = self.name
        if self.owner:
            createSchemaResponse_body['owner'] = self.owner
        if self.privileges:
            createSchemaResponse_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            createSchemaResponse_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.updated_at:
            createSchemaResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            createSchemaResponse_body['updated_by'] = self.updated_by
        
        return createSchemaResponse_query, createSchemaResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateSchemaResponse':
        return cls(
            catalog_name=d.get('catalog_name', None),
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            full_name=d.get('full_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class CreateSchemaResponsePrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class CreateShare:
    
    # [Create: OPT] comment when creating the share
    comment: str = None
    # [Create:IGN] Time at which this Share was created, in epoch milliseconds.
    created_at: int = None
    # [Create:IGN] Username of Share creator.
    created_by: str = None
    # [Create:REQ] Name of the Share.
    name: str = None
    # [Create: IGN] A list of shared data objects within the Share.
    objects: 'List[SharedDataObject]' = None

    def as_request(self) -> (dict, dict):
        createShare_query, createShare_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.comment:
            createShare_body['comment'] = self.comment
        if self.created_at:
            createShare_body['created_at'] = self.created_at
        if self.created_by:
            createShare_body['created_by'] = self.created_by
        if self.name:
            createShare_body['name'] = self.name
        if self.objects:
            createShare_body['objects'] = [v.as_request()[1] for v in self.objects]
        
        return createShare_query, createShare_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateShare':
        return cls(
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            name=d.get('name', None),
            objects=[SharedDataObject.from_dict(v) for v in d['objects']] if 'objects' in d else None,
        )



@dataclass
class CreateShareResponse:
    
    # [Create: OPT] comment when creating the share
    comment: str = None
    # [Create:IGN] Time at which this Share was created, in epoch milliseconds.
    created_at: int = None
    # [Create:IGN] Username of Share creator.
    created_by: str = None
    # [Create:REQ] Name of the Share.
    name: str = None
    # [Create: IGN] A list of shared data objects within the Share.
    objects: 'List[SharedDataObject]' = None

    def as_request(self) -> (dict, dict):
        createShareResponse_query, createShareResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.comment:
            createShareResponse_body['comment'] = self.comment
        if self.created_at:
            createShareResponse_body['created_at'] = self.created_at
        if self.created_by:
            createShareResponse_body['created_by'] = self.created_by
        if self.name:
            createShareResponse_body['name'] = self.name
        if self.objects:
            createShareResponse_body['objects'] = [v.as_request()[1] for v in self.objects]
        
        return createShareResponse_query, createShareResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateShareResponse':
        return cls(
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            name=d.get('name', None),
            objects=[SharedDataObject.from_dict(v) for v in d['objects']] if 'objects' in d else None,
        )



@dataclass
class CreateStagingTable:
    
    # [Create:REQ] Name of parent Catalog.
    catalog_name: str = None
    # [Create:IGN] Unique id generated for the staging table
    id: str = None
    # [Create:REQ] Name of Table, relative to parent Schema.
    name: str = None
    # [Create:REQ] Name of parent Schema relative to its parent Catalog.
    schema_name: str = None
    # [Create:IGN] URI generated for the staging table
    staging_location: str = None

    def as_request(self) -> (dict, dict):
        createStagingTable_query, createStagingTable_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            createStagingTable_body['catalog_name'] = self.catalog_name
        if self.id:
            createStagingTable_body['id'] = self.id
        if self.name:
            createStagingTable_body['name'] = self.name
        if self.schema_name:
            createStagingTable_body['schema_name'] = self.schema_name
        if self.staging_location:
            createStagingTable_body['staging_location'] = self.staging_location
        
        return createStagingTable_query, createStagingTable_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateStagingTable':
        return cls(
            catalog_name=d.get('catalog_name', None),
            id=d.get('id', None),
            name=d.get('name', None),
            schema_name=d.get('schema_name', None),
            staging_location=d.get('staging_location', None),
        )



@dataclass
class CreateStagingTableResponse:
    
    # [Create:REQ] Name of parent Catalog.
    catalog_name: str = None
    # [Create:IGN] Unique id generated for the staging table
    id: str = None
    # [Create:REQ] Name of Table, relative to parent Schema.
    name: str = None
    # [Create:REQ] Name of parent Schema relative to its parent Catalog.
    schema_name: str = None
    # [Create:IGN] URI generated for the staging table
    staging_location: str = None

    def as_request(self) -> (dict, dict):
        createStagingTableResponse_query, createStagingTableResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            createStagingTableResponse_body['catalog_name'] = self.catalog_name
        if self.id:
            createStagingTableResponse_body['id'] = self.id
        if self.name:
            createStagingTableResponse_body['name'] = self.name
        if self.schema_name:
            createStagingTableResponse_body['schema_name'] = self.schema_name
        if self.staging_location:
            createStagingTableResponse_body['staging_location'] = self.staging_location
        
        return createStagingTableResponse_query, createStagingTableResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateStagingTableResponse':
        return cls(
            catalog_name=d.get('catalog_name', None),
            id=d.get('id', None),
            name=d.get('name', None),
            schema_name=d.get('schema_name', None),
            staging_location=d.get('staging_location', None),
        )



@dataclass
class CreateStorageCredential:
    
    # The AWS IAM role configuration.
    aws_iam_role: 'AwsIamRole' = None
    # The Azure service principal configuration.
    azure_service_principal: 'AzureServicePrincipal' = None
    # [Create,Update:OPT] Comment associated with the credential.
    comment: str = None
    # [Create,Update:IGN] Time at which this Credential was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of credential creator.
    created_by: str = None
    # The GCP service account key configuration.
    gcp_service_account_key: 'GcpServiceAccountKey' = None
    # [Create:IGN] The unique identifier of the credential.
    id: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ, Update:OPT] The credential name. The name MUST be unique
    # within the Metastore.
    name: str = None
    # [Create:IGN Update:OPT] Username of current owner of credential.
    owner: str = None
    # Optional. Supplying true to this argument skips validation of the created
    # set of credentials.
    skip_validation: bool = None
    # [Create,Update:IGN] Time at which this credential was last modified, in
    # epoch milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the credential.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        createStorageCredential_query, createStorageCredential_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.aws_iam_role:
            createStorageCredential_body['aws_iam_role'] = self.aws_iam_role.as_request()[1]
        if self.azure_service_principal:
            createStorageCredential_body['azure_service_principal'] = self.azure_service_principal.as_request()[1]
        if self.comment:
            createStorageCredential_body['comment'] = self.comment
        if self.created_at:
            createStorageCredential_body['created_at'] = self.created_at
        if self.created_by:
            createStorageCredential_body['created_by'] = self.created_by
        if self.gcp_service_account_key:
            createStorageCredential_body['gcp_service_account_key'] = self.gcp_service_account_key.as_request()[1]
        if self.id:
            createStorageCredential_body['id'] = self.id
        if self.metastore_id:
            createStorageCredential_body['metastore_id'] = self.metastore_id
        if self.name:
            createStorageCredential_body['name'] = self.name
        if self.owner:
            createStorageCredential_body['owner'] = self.owner
        if self.skip_validation:
            createStorageCredential_body['skip_validation'] = self.skip_validation
        if self.updated_at:
            createStorageCredential_body['updated_at'] = self.updated_at
        if self.updated_by:
            createStorageCredential_body['updated_by'] = self.updated_by
        
        return createStorageCredential_query, createStorageCredential_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateStorageCredential':
        return cls(
            aws_iam_role=AwsIamRole.from_dict(d['aws_iam_role']) if 'aws_iam_role' in d else None,
            azure_service_principal=AzureServicePrincipal.from_dict(d['azure_service_principal']) if 'azure_service_principal' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            gcp_service_account_key=GcpServiceAccountKey.from_dict(d['gcp_service_account_key']) if 'gcp_service_account_key' in d else None,
            id=d.get('id', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            skip_validation=d.get('skip_validation', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



@dataclass
class CreateStorageCredentialResponse:
    
    # The AWS IAM role configuration.
    aws_iam_role: 'AwsIamRole' = None
    # The Azure service principal configuration.
    azure_service_principal: 'AzureServicePrincipal' = None
    # [Create,Update:OPT] Comment associated with the credential.
    comment: str = None
    # [Create,Update:IGN] Time at which this Credential was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of credential creator.
    created_by: str = None
    # The GCP service account key configuration.
    gcp_service_account_key: 'GcpServiceAccountKey' = None
    # [Create:IGN] The unique identifier of the credential.
    id: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ, Update:OPT] The credential name. The name MUST be unique
    # within the Metastore.
    name: str = None
    # [Create:IGN Update:OPT] Username of current owner of credential.
    owner: str = None
    # [Create,Update:IGN] Time at which this credential was last modified, in
    # epoch milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the credential.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        createStorageCredentialResponse_query, createStorageCredentialResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.aws_iam_role:
            createStorageCredentialResponse_body['aws_iam_role'] = self.aws_iam_role.as_request()[1]
        if self.azure_service_principal:
            createStorageCredentialResponse_body['azure_service_principal'] = self.azure_service_principal.as_request()[1]
        if self.comment:
            createStorageCredentialResponse_body['comment'] = self.comment
        if self.created_at:
            createStorageCredentialResponse_body['created_at'] = self.created_at
        if self.created_by:
            createStorageCredentialResponse_body['created_by'] = self.created_by
        if self.gcp_service_account_key:
            createStorageCredentialResponse_body['gcp_service_account_key'] = self.gcp_service_account_key.as_request()[1]
        if self.id:
            createStorageCredentialResponse_body['id'] = self.id
        if self.metastore_id:
            createStorageCredentialResponse_body['metastore_id'] = self.metastore_id
        if self.name:
            createStorageCredentialResponse_body['name'] = self.name
        if self.owner:
            createStorageCredentialResponse_body['owner'] = self.owner
        if self.updated_at:
            createStorageCredentialResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            createStorageCredentialResponse_body['updated_by'] = self.updated_by
        
        return createStorageCredentialResponse_query, createStorageCredentialResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateStorageCredentialResponse':
        return cls(
            aws_iam_role=AwsIamRole.from_dict(d['aws_iam_role']) if 'aws_iam_role' in d else None,
            azure_service_principal=AzureServicePrincipal.from_dict(d['azure_service_principal']) if 'azure_service_principal' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            gcp_service_account_key=GcpServiceAccountKey.from_dict(d['gcp_service_account_key']) if 'gcp_service_account_key' in d else None,
            id=d.get('id', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



@dataclass
class CreateTable:
    
    # [Create:REQ Update:IGN] Name of parent Catalog.
    catalog_name: str = None
    # This name ('columns') is what the client actually sees as the field name
    # in messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    columns: 'List[ColumnInfo]' = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Table was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Table creator.
    created_by: str = None
    # [Create,Update:IGN] Unique ID of the data_access_configuration to use.
    data_access_configuration_id: str = None
    # [Create:REQ Update:OPT] Data source format ("DELTA", "CSV", etc.).
    data_source_format: 'CreateTableDataSourceFormat' = None
    # [Create,Update:IGN] Full name of Table, in form of
    # <catalog_name>.<schema_name>.<table_name>
    full_name: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Table, relative to parent Schema.
    name: str = None
    # [Create: IGN Update:OPT] Username of current owner of Table.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Table.
    privileges: 'List[CreateTablePrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # [Create:REQ Update:IGN] Name of parent Schema relative to its parent
    # Catalog.
    schema_name: str = None
    # [Create,Update:OPT] List of schemes whose objects can be referenced
    # without qualification.
    sql_path: str = None
    # [Create:OPT Update:IGN] Name of the storage credential this table used
    storage_credential_name: str = None
    # [Create:REQ Update:OPT] Storage root URL for table (for MANAGED, EXTERNAL
    # tables)
    storage_location: str = None
    # [Create:IGN Update:IGN] Name of Table, relative to parent Schema.
    table_id: str = None
    # [Create:REQ Update:OPT] Table type ("MANAGED", "EXTERNAL", "VIEW").
    table_type: 'CreateTableTableType' = None
    # [Create,Update:IGN] Time at which this Table was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the Table.
    updated_by: str = None
    # [Create,Update:OPT] View definition SQL (when table_type == "VIEW")
    view_definition: str = None

    def as_request(self) -> (dict, dict):
        createTable_query, createTable_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            createTable_body['catalog_name'] = self.catalog_name
        if self.columns:
            createTable_body['columns'] = [v.as_request()[1] for v in self.columns]
        if self.comment:
            createTable_body['comment'] = self.comment
        if self.created_at:
            createTable_body['created_at'] = self.created_at
        if self.created_by:
            createTable_body['created_by'] = self.created_by
        if self.data_access_configuration_id:
            createTable_body['data_access_configuration_id'] = self.data_access_configuration_id
        if self.data_source_format:
            createTable_body['data_source_format'] = self.data_source_format.value
        if self.full_name:
            createTable_body['full_name'] = self.full_name
        if self.metastore_id:
            createTable_body['metastore_id'] = self.metastore_id
        if self.name:
            createTable_body['name'] = self.name
        if self.owner:
            createTable_body['owner'] = self.owner
        if self.privileges:
            createTable_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            createTable_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.schema_name:
            createTable_body['schema_name'] = self.schema_name
        if self.sql_path:
            createTable_body['sql_path'] = self.sql_path
        if self.storage_credential_name:
            createTable_body['storage_credential_name'] = self.storage_credential_name
        if self.storage_location:
            createTable_body['storage_location'] = self.storage_location
        if self.table_id:
            createTable_body['table_id'] = self.table_id
        if self.table_type:
            createTable_body['table_type'] = self.table_type.value
        if self.updated_at:
            createTable_body['updated_at'] = self.updated_at
        if self.updated_by:
            createTable_body['updated_by'] = self.updated_by
        if self.view_definition:
            createTable_body['view_definition'] = self.view_definition
        
        return createTable_query, createTable_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateTable':
        return cls(
            catalog_name=d.get('catalog_name', None),
            columns=[ColumnInfo.from_dict(v) for v in d['columns']] if 'columns' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            data_access_configuration_id=d.get('data_access_configuration_id', None),
            data_source_format=CreateTableDataSourceFormat(d['data_source_format']) if 'data_source_format' in d else None,
            full_name=d.get('full_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            schema_name=d.get('schema_name', None),
            sql_path=d.get('sql_path', None),
            storage_credential_name=d.get('storage_credential_name', None),
            storage_location=d.get('storage_location', None),
            table_id=d.get('table_id', None),
            table_type=CreateTableTableType(d['table_type']) if 'table_type' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
            view_definition=d.get('view_definition', None),
        )



class CreateTableDataSourceFormat(Enum):
    """[Create:REQ Update:OPT] Data source format ("DELTA", "CSV", etc.)."""
    
    AVRO = 'AVRO'
    CSV = 'CSV'
    DELTA = 'DELTA'
    DELTASHARING = 'DELTASHARING'
    JSON = 'JSON'
    ORC = 'ORC'
    PARQUET = 'PARQUET'
    TEXT = 'TEXT'
    UNITY_CATALOG = 'UNITY_CATALOG'
    UNKNOWN_DATA_SOURCE_FORMAT = 'UNKNOWN_DATA_SOURCE_FORMAT'

class CreateTablePrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class CreateTableResponse:
    
    # [Create:REQ Update:IGN] Name of parent Catalog.
    catalog_name: str = None
    # This name ('columns') is what the client actually sees as the field name
    # in messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    columns: 'List[ColumnInfo]' = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Table was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Table creator.
    created_by: str = None
    # [Create,Update:IGN] Unique ID of the data_access_configuration to use.
    data_access_configuration_id: str = None
    # [Create:REQ Update:OPT] Data source format ("DELTA", "CSV", etc.).
    data_source_format: 'CreateTableResponseDataSourceFormat' = None
    # [Create,Update:IGN] Full name of Table, in form of
    # <catalog_name>.<schema_name>.<table_name>
    full_name: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Table, relative to parent Schema.
    name: str = None
    # [Create: IGN Update:OPT] Username of current owner of Table.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Table.
    privileges: 'List[CreateTableResponsePrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # [Create:REQ Update:IGN] Name of parent Schema relative to its parent
    # Catalog.
    schema_name: str = None
    # [Create,Update:OPT] List of schemes whose objects can be referenced
    # without qualification.
    sql_path: str = None
    # [Create:OPT Update:IGN] Name of the storage credential this table used
    storage_credential_name: str = None
    # [Create:REQ Update:OPT] Storage root URL for table (for MANAGED, EXTERNAL
    # tables)
    storage_location: str = None
    # [Create:IGN Update:IGN] Name of Table, relative to parent Schema.
    table_id: str = None
    # [Create:REQ Update:OPT] Table type ("MANAGED", "EXTERNAL", "VIEW").
    table_type: 'CreateTableResponseTableType' = None
    # [Create,Update:IGN] Time at which this Table was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the Table.
    updated_by: str = None
    # [Create,Update:OPT] View definition SQL (when table_type == "VIEW")
    view_definition: str = None

    def as_request(self) -> (dict, dict):
        createTableResponse_query, createTableResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            createTableResponse_body['catalog_name'] = self.catalog_name
        if self.columns:
            createTableResponse_body['columns'] = [v.as_request()[1] for v in self.columns]
        if self.comment:
            createTableResponse_body['comment'] = self.comment
        if self.created_at:
            createTableResponse_body['created_at'] = self.created_at
        if self.created_by:
            createTableResponse_body['created_by'] = self.created_by
        if self.data_access_configuration_id:
            createTableResponse_body['data_access_configuration_id'] = self.data_access_configuration_id
        if self.data_source_format:
            createTableResponse_body['data_source_format'] = self.data_source_format.value
        if self.full_name:
            createTableResponse_body['full_name'] = self.full_name
        if self.metastore_id:
            createTableResponse_body['metastore_id'] = self.metastore_id
        if self.name:
            createTableResponse_body['name'] = self.name
        if self.owner:
            createTableResponse_body['owner'] = self.owner
        if self.privileges:
            createTableResponse_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            createTableResponse_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.schema_name:
            createTableResponse_body['schema_name'] = self.schema_name
        if self.sql_path:
            createTableResponse_body['sql_path'] = self.sql_path
        if self.storage_credential_name:
            createTableResponse_body['storage_credential_name'] = self.storage_credential_name
        if self.storage_location:
            createTableResponse_body['storage_location'] = self.storage_location
        if self.table_id:
            createTableResponse_body['table_id'] = self.table_id
        if self.table_type:
            createTableResponse_body['table_type'] = self.table_type.value
        if self.updated_at:
            createTableResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            createTableResponse_body['updated_by'] = self.updated_by
        if self.view_definition:
            createTableResponse_body['view_definition'] = self.view_definition
        
        return createTableResponse_query, createTableResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateTableResponse':
        return cls(
            catalog_name=d.get('catalog_name', None),
            columns=[ColumnInfo.from_dict(v) for v in d['columns']] if 'columns' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            data_access_configuration_id=d.get('data_access_configuration_id', None),
            data_source_format=CreateTableResponseDataSourceFormat(d['data_source_format']) if 'data_source_format' in d else None,
            full_name=d.get('full_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            schema_name=d.get('schema_name', None),
            sql_path=d.get('sql_path', None),
            storage_credential_name=d.get('storage_credential_name', None),
            storage_location=d.get('storage_location', None),
            table_id=d.get('table_id', None),
            table_type=CreateTableResponseTableType(d['table_type']) if 'table_type' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
            view_definition=d.get('view_definition', None),
        )



class CreateTableResponseDataSourceFormat(Enum):
    """[Create:REQ Update:OPT] Data source format ("DELTA", "CSV", etc.)."""
    
    AVRO = 'AVRO'
    CSV = 'CSV'
    DELTA = 'DELTA'
    DELTASHARING = 'DELTASHARING'
    JSON = 'JSON'
    ORC = 'ORC'
    PARQUET = 'PARQUET'
    TEXT = 'TEXT'
    UNITY_CATALOG = 'UNITY_CATALOG'
    UNKNOWN_DATA_SOURCE_FORMAT = 'UNKNOWN_DATA_SOURCE_FORMAT'

class CreateTableResponsePrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

class CreateTableResponseTableType(Enum):
    """[Create:REQ Update:OPT] Table type ("MANAGED", "EXTERNAL", "VIEW")."""
    
    EXTERNAL = 'EXTERNAL'
    MANAGED = 'MANAGED'
    UNKNOWN_TABLE_TYPE = 'UNKNOWN_TABLE_TYPE'
    VIEW = 'VIEW'

class CreateTableTableType(Enum):
    """[Create:REQ Update:OPT] Table type ("MANAGED", "EXTERNAL", "VIEW")."""
    
    EXTERNAL = 'EXTERNAL'
    MANAGED = 'MANAGED'
    UNKNOWN_TABLE_TYPE = 'UNKNOWN_TABLE_TYPE'
    VIEW = 'VIEW'

@dataclass
class ExternalLocationInfo:
    
    # [Create:OPT Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this External Location was created, in
    # epoch milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of External Location creator.
    created_by: str = None
    # [Create,Update:IGN] Unique ID of the location's Storage Credential.
    credential_id: str = None
    # [Create:REQ Update:OPT] Current name of the Storage Credential this
    # location uses.
    credential_name: str = None
    # [Create,Update:IGN] Unique identifier of Metastore hosting the External
    # Location.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of the External Location.
    name: str = None
    # [Create:IGN Update:OPT] The owner of the External Location.
    owner: str = None
    # [Create,Update:IGN] Time at which this was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the External
    # Location.
    updated_by: str = None
    # [Create:REQ Update:OPT] Path URL of the External Location.
    url: str = None

    def as_request(self) -> (dict, dict):
        externalLocationInfo_query, externalLocationInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.comment:
            externalLocationInfo_body['comment'] = self.comment
        if self.created_at:
            externalLocationInfo_body['created_at'] = self.created_at
        if self.created_by:
            externalLocationInfo_body['created_by'] = self.created_by
        if self.credential_id:
            externalLocationInfo_body['credential_id'] = self.credential_id
        if self.credential_name:
            externalLocationInfo_body['credential_name'] = self.credential_name
        if self.metastore_id:
            externalLocationInfo_body['metastore_id'] = self.metastore_id
        if self.name:
            externalLocationInfo_body['name'] = self.name
        if self.owner:
            externalLocationInfo_body['owner'] = self.owner
        if self.updated_at:
            externalLocationInfo_body['updated_at'] = self.updated_at
        if self.updated_by:
            externalLocationInfo_body['updated_by'] = self.updated_by
        if self.url:
            externalLocationInfo_body['url'] = self.url
        
        return externalLocationInfo_query, externalLocationInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExternalLocationInfo':
        return cls(
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            credential_id=d.get('credential_id', None),
            credential_name=d.get('credential_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
            url=d.get('url', None),
        )



@dataclass
class FileInfo:
    
    # Whether the object represents a directory or a file.
    is_dir: bool = None
    # Modification time, unix epoch.
    mtime: int = None
    # Name of the object.
    name: str = None
    # Path URI of the storage object.
    path: str = None
    # Size in bytes.
    size: int = None

    def as_request(self) -> (dict, dict):
        fileInfo_query, fileInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.is_dir:
            fileInfo_body['is_dir'] = self.is_dir
        if self.mtime:
            fileInfo_body['mtime'] = self.mtime
        if self.name:
            fileInfo_body['name'] = self.name
        if self.path:
            fileInfo_body['path'] = self.path
        if self.size:
            fileInfo_body['size'] = self.size
        
        return fileInfo_query, fileInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FileInfo':
        return cls(
            is_dir=d.get('is_dir', None),
            mtime=d.get('mtime', None),
            name=d.get('name', None),
            path=d.get('path', None),
            size=d.get('size', None),
        )



@dataclass
class GcpServiceAccountKey:
    
    # The email of the service account. [Create:REQ].
    email: str = None
    # The service account's RSA private key. [Create:REQ]
    private_key: str = None
    # The ID of the service account's private key. [Create:REQ]
    private_key_id: str = None

    def as_request(self) -> (dict, dict):
        gcpServiceAccountKey_query, gcpServiceAccountKey_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.email:
            gcpServiceAccountKey_body['email'] = self.email
        if self.private_key:
            gcpServiceAccountKey_body['private_key'] = self.private_key
        if self.private_key_id:
            gcpServiceAccountKey_body['private_key_id'] = self.private_key_id
        
        return gcpServiceAccountKey_query, gcpServiceAccountKey_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GcpServiceAccountKey':
        return cls(
            email=d.get('email', None),
            private_key=d.get('private_key', None),
            private_key_id=d.get('private_key_id', None),
        )



@dataclass
class GetCatalogResponse:
    
    # [Create,Update:IGN] The type of the catalog.
    catalog_type: 'GetCatalogResponseCatalogType' = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Catalog was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Catalog creator.
    created_by: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Catalog.
    name: str = None
    # [Create:IGN,Update:OPT] Username of current owner of Catalog.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Catalog.
    privileges: 'List[GetCatalogResponsePrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # Delta Sharing Catalog specific fields. A Delta Sharing Catalog is a
    # catalog that is based on a Delta share on a remote sharing server.
    # [Create:OPT,Update:IGN] The name of delta sharing provider.
    provider_name: str = None
    # [Create:OPT,Update: IGN] The name of the share under the share provider.
    share_name: str = None
    # [Create,Update:IGN] Time at which this Catalog was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Catalog.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        getCatalogResponse_query, getCatalogResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_type:
            getCatalogResponse_body['catalog_type'] = self.catalog_type.value
        if self.comment:
            getCatalogResponse_body['comment'] = self.comment
        if self.created_at:
            getCatalogResponse_body['created_at'] = self.created_at
        if self.created_by:
            getCatalogResponse_body['created_by'] = self.created_by
        if self.metastore_id:
            getCatalogResponse_body['metastore_id'] = self.metastore_id
        if self.name:
            getCatalogResponse_body['name'] = self.name
        if self.owner:
            getCatalogResponse_body['owner'] = self.owner
        if self.privileges:
            getCatalogResponse_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            getCatalogResponse_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.provider_name:
            getCatalogResponse_body['provider_name'] = self.provider_name
        if self.share_name:
            getCatalogResponse_body['share_name'] = self.share_name
        if self.updated_at:
            getCatalogResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            getCatalogResponse_body['updated_by'] = self.updated_by
        
        return getCatalogResponse_query, getCatalogResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetCatalogResponse':
        return cls(
            catalog_type=GetCatalogResponseCatalogType(d['catalog_type']) if 'catalog_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            provider_name=d.get('provider_name', None),
            share_name=d.get('share_name', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class GetCatalogResponseCatalogType(Enum):
    """[Create,Update:IGN] The type of the catalog."""
    
    DELTASHARING_CATALOG = 'DELTASHARING_CATALOG'
    MANAGED_CATALOG = 'MANAGED_CATALOG'
    SYSTEM_CATALOG = 'SYSTEM_CATALOG'
    UNKNOWN_CATALOG_TYPE = 'UNKNOWN_CATALOG_TYPE'

class GetCatalogResponsePrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class GetExternalLocationResponse:
    
    # [Create:OPT Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this External Location was created, in
    # epoch milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of External Location creator.
    created_by: str = None
    # [Create,Update:IGN] Unique ID of the location's Storage Credential.
    credential_id: str = None
    # [Create:REQ Update:OPT] Current name of the Storage Credential this
    # location uses.
    credential_name: str = None
    # [Create,Update:IGN] Unique identifier of Metastore hosting the External
    # Location.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of the External Location.
    name: str = None
    # [Create:IGN Update:OPT] The owner of the External Location.
    owner: str = None
    # [Create,Update:IGN] Time at which this was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the External
    # Location.
    updated_by: str = None
    # [Create:REQ Update:OPT] Path URL of the External Location.
    url: str = None

    def as_request(self) -> (dict, dict):
        getExternalLocationResponse_query, getExternalLocationResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.comment:
            getExternalLocationResponse_body['comment'] = self.comment
        if self.created_at:
            getExternalLocationResponse_body['created_at'] = self.created_at
        if self.created_by:
            getExternalLocationResponse_body['created_by'] = self.created_by
        if self.credential_id:
            getExternalLocationResponse_body['credential_id'] = self.credential_id
        if self.credential_name:
            getExternalLocationResponse_body['credential_name'] = self.credential_name
        if self.metastore_id:
            getExternalLocationResponse_body['metastore_id'] = self.metastore_id
        if self.name:
            getExternalLocationResponse_body['name'] = self.name
        if self.owner:
            getExternalLocationResponse_body['owner'] = self.owner
        if self.updated_at:
            getExternalLocationResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            getExternalLocationResponse_body['updated_by'] = self.updated_by
        if self.url:
            getExternalLocationResponse_body['url'] = self.url
        
        return getExternalLocationResponse_query, getExternalLocationResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetExternalLocationResponse':
        return cls(
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            credential_id=d.get('credential_id', None),
            credential_name=d.get('credential_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
            url=d.get('url', None),
        )



@dataclass
class GetMetastoreResponse:
    
    # [Create,Update:IGN] Time at which this Metastore was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Metastore creator.
    created_by: str = None
    # [Create:IGN Update:OPT] Unique identifier of (Default) Data Access
    # Configuration
    default_data_access_config_id: str = None
    # [Create:IGN Update:OPT] Whether Delta Sharing is enabled on this
    # metastore.
    delta_sharing_enabled: bool = None
    # [Create:IGN Update:OPT] The lifetime of delta sharing recipient token in
    # seconds
    delta_sharing_recipient_token_lifetime_in_seconds: int = None
    # [Create,Update:IGN] Unique identifier of Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Metastore.
    name: str = None
    # [Create:IGN Update:OPT] The owner of the metastore.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Metastore.
    privileges: 'List[GetMetastoreResponsePrivilegesItem]' = None
    # The region this metastore has an afinity to. This is used by
    # accounts-manager. Ignored by Unity Catalog.
    region: str = None
    # [Create:REQ Update:ERR] Storage root URL for Metastore
    storage_root: str = None
    # [Create:IGN Update:OPT] UUID of storage credential to access storage_root
    storage_root_credential_id: str = None
    # [Create,Update:IGN] Time at which the Metastore was last modified, in
    # epoch milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the Metastore.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        getMetastoreResponse_query, getMetastoreResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.created_at:
            getMetastoreResponse_body['created_at'] = self.created_at
        if self.created_by:
            getMetastoreResponse_body['created_by'] = self.created_by
        if self.default_data_access_config_id:
            getMetastoreResponse_body['default_data_access_config_id'] = self.default_data_access_config_id
        if self.delta_sharing_enabled:
            getMetastoreResponse_body['delta_sharing_enabled'] = self.delta_sharing_enabled
        if self.delta_sharing_recipient_token_lifetime_in_seconds:
            getMetastoreResponse_body['delta_sharing_recipient_token_lifetime_in_seconds'] = self.delta_sharing_recipient_token_lifetime_in_seconds
        if self.metastore_id:
            getMetastoreResponse_body['metastore_id'] = self.metastore_id
        if self.name:
            getMetastoreResponse_body['name'] = self.name
        if self.owner:
            getMetastoreResponse_body['owner'] = self.owner
        if self.privileges:
            getMetastoreResponse_body['privileges'] = [v for v in self.privileges]
        if self.region:
            getMetastoreResponse_body['region'] = self.region
        if self.storage_root:
            getMetastoreResponse_body['storage_root'] = self.storage_root
        if self.storage_root_credential_id:
            getMetastoreResponse_body['storage_root_credential_id'] = self.storage_root_credential_id
        if self.updated_at:
            getMetastoreResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            getMetastoreResponse_body['updated_by'] = self.updated_by
        
        return getMetastoreResponse_query, getMetastoreResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetMetastoreResponse':
        return cls(
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            default_data_access_config_id=d.get('default_data_access_config_id', None),
            delta_sharing_enabled=d.get('delta_sharing_enabled', None),
            delta_sharing_recipient_token_lifetime_in_seconds=d.get('delta_sharing_recipient_token_lifetime_in_seconds', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            region=d.get('region', None),
            storage_root=d.get('storage_root', None),
            storage_root_credential_id=d.get('storage_root_credential_id', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class GetMetastoreResponsePrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class GetMetastoreSummaryResponse:
    
    # Unique identifier of the Metastore's (Default) Data Access Configuration
    default_data_access_config_id: str = None
    # The unique ID (UUID) of the Metastore
    metastore_id: str = None
    # The user-specified name of the Metastore
    name: str = None
    # UUID of storage credential to access the metastore storage_root
    storage_root_credential_id: str = None

    def as_request(self) -> (dict, dict):
        getMetastoreSummaryResponse_query, getMetastoreSummaryResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.default_data_access_config_id:
            getMetastoreSummaryResponse_body['default_data_access_config_id'] = self.default_data_access_config_id
        if self.metastore_id:
            getMetastoreSummaryResponse_body['metastore_id'] = self.metastore_id
        if self.name:
            getMetastoreSummaryResponse_body['name'] = self.name
        if self.storage_root_credential_id:
            getMetastoreSummaryResponse_body['storage_root_credential_id'] = self.storage_root_credential_id
        
        return getMetastoreSummaryResponse_query, getMetastoreSummaryResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetMetastoreSummaryResponse':
        return cls(
            default_data_access_config_id=d.get('default_data_access_config_id', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            storage_root_credential_id=d.get('storage_root_credential_id', None),
        )



@dataclass
class GetPermissionsResponse:
    
    # Note to self (acain): Unfortunately, neither json_inline nor json_map work
    # here.
    privilege_assignments: 'List[PrivilegeAssignment]' = None

    def as_request(self) -> (dict, dict):
        getPermissionsResponse_query, getPermissionsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.privilege_assignments:
            getPermissionsResponse_body['privilege_assignments'] = [v.as_request()[1] for v in self.privilege_assignments]
        
        return getPermissionsResponse_query, getPermissionsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPermissionsResponse':
        return cls(
            privilege_assignments=[PrivilegeAssignment.from_dict(v) for v in d['privilege_assignments']] if 'privilege_assignments' in d else None,
        )



@dataclass
class GetProviderResponse:
    
    # [Create,Update:IGN] Whether this provider is successfully activated by the
    # data provider. This field is only present when the authentication type is
    # DATABRICKS.
    activated_by_provider: bool = None
    # [Create:REQ,Update:IGN] The delta sharing authentication type.
    authentication_type: 'GetProviderResponseAuthenticationType' = None
    # [Create,Update:OPT] Description about the provider.
    comment: str = None
    # [Create,Update:IGN] Time at which this Provider was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Provider creator.
    created_by: str = None
    # [Create,Update:REQ] The name of the Provider.
    name: str = None
    # [Create,Update:IGN] This field is only present when the authentication
    # type is TOKEN.
    recipient_profile: 'RecipientProfile' = None
    # [Create,Update:OPT] This field is only present when the authentication
    # type is TOKEN.
    recipient_profile_str: str = None
    # [Create,Update:IGN] The server-generated one-time sharing code. This field
    # is only present when the authentication type is DATABRICKS.
    sharing_code: str = None
    # [Create,Update:IGN] Time at which this Provider was created, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Share.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        getProviderResponse_query, getProviderResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activated_by_provider:
            getProviderResponse_body['activated_by_provider'] = self.activated_by_provider
        if self.authentication_type:
            getProviderResponse_body['authentication_type'] = self.authentication_type.value
        if self.comment:
            getProviderResponse_body['comment'] = self.comment
        if self.created_at:
            getProviderResponse_body['created_at'] = self.created_at
        if self.created_by:
            getProviderResponse_body['created_by'] = self.created_by
        if self.name:
            getProviderResponse_body['name'] = self.name
        if self.recipient_profile:
            getProviderResponse_body['recipient_profile'] = self.recipient_profile.as_request()[1]
        if self.recipient_profile_str:
            getProviderResponse_body['recipient_profile_str'] = self.recipient_profile_str
        if self.sharing_code:
            getProviderResponse_body['sharing_code'] = self.sharing_code
        if self.updated_at:
            getProviderResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            getProviderResponse_body['updated_by'] = self.updated_by
        
        return getProviderResponse_query, getProviderResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetProviderResponse':
        return cls(
            activated_by_provider=d.get('activated_by_provider', None),
            authentication_type=GetProviderResponseAuthenticationType(d['authentication_type']) if 'authentication_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            name=d.get('name', None),
            recipient_profile=RecipientProfile.from_dict(d['recipient_profile']) if 'recipient_profile' in d else None,
            recipient_profile_str=d.get('recipient_profile_str', None),
            sharing_code=d.get('sharing_code', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class GetProviderResponseAuthenticationType(Enum):
    """[Create:REQ,Update:IGN] The delta sharing authentication type."""
    
    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'
    UNKNOWN = 'UNKNOWN'

@dataclass
class GetRecipientResponse:
    
    # [Create:IGN,Update:IGN] A boolean status field showing whether the
    # Recipient's activation URL has been exercised or not.
    activated: bool = None
    # [Create:IGN,Update:IGN] Full activation url to retrieve the access token.
    # It will be empty if the token is already retrieved.
    activation_url: str = None
    # [Create:REQ,Update:IGN] The delta sharing authentication type.
    authentication_type: 'GetRecipientResponseAuthenticationType' = None
    # [Create:OPT,Update:OPT] Description about the recipient.
    comment: str = None
    # [Create:IGN,Update:IGN] Time at which this recipient was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create:IGN,Update:IGN] Username of recipient creator.
    created_by: str = None
    # [Create:OPT,Update:OPT] IP Access List
    ip_access_list: 'IpAccessList' = None
    # [Create:REQ,Update:OPT] Name of Recipient.
    name: str = None
    # [Create:OPT,Update:IGN] The one-time sharing code provided by the data
    # recipient. This field is only present when the authentication type is
    # DATABRICKS.
    sharing_code: str = None
    # [Create:IGN,Update:IGN] recipient Tokens This field is only present when
    # the authentication type is TOKEN.
    tokens: 'List[RecipientTokenInfo]' = None
    # [Create:IGN,Update:IGN] Time at which the recipient was updated, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create:IGN,Update:IGN] Username of recipient updater.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        getRecipientResponse_query, getRecipientResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activated:
            getRecipientResponse_body['activated'] = self.activated
        if self.activation_url:
            getRecipientResponse_body['activation_url'] = self.activation_url
        if self.authentication_type:
            getRecipientResponse_body['authentication_type'] = self.authentication_type.value
        if self.comment:
            getRecipientResponse_body['comment'] = self.comment
        if self.created_at:
            getRecipientResponse_body['created_at'] = self.created_at
        if self.created_by:
            getRecipientResponse_body['created_by'] = self.created_by
        if self.ip_access_list:
            getRecipientResponse_body['ip_access_list'] = self.ip_access_list.as_request()[1]
        if self.name:
            getRecipientResponse_body['name'] = self.name
        if self.sharing_code:
            getRecipientResponse_body['sharing_code'] = self.sharing_code
        if self.tokens:
            getRecipientResponse_body['tokens'] = [v.as_request()[1] for v in self.tokens]
        if self.updated_at:
            getRecipientResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            getRecipientResponse_body['updated_by'] = self.updated_by
        
        return getRecipientResponse_query, getRecipientResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRecipientResponse':
        return cls(
            activated=d.get('activated', None),
            activation_url=d.get('activation_url', None),
            authentication_type=GetRecipientResponseAuthenticationType(d['authentication_type']) if 'authentication_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            ip_access_list=IpAccessList.from_dict(d['ip_access_list']) if 'ip_access_list' in d else None,
            name=d.get('name', None),
            sharing_code=d.get('sharing_code', None),
            tokens=[RecipientTokenInfo.from_dict(v) for v in d['tokens']] if 'tokens' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class GetRecipientResponseAuthenticationType(Enum):
    """[Create:REQ,Update:IGN] The delta sharing authentication type."""
    
    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'
    UNKNOWN = 'UNKNOWN'

@dataclass
class GetRecipientSharePermissionsResponse:
    
    # An array of data share permissions for a recipient.
    permissions_out: 'List[ShareToPrivilegeAssignment]' = None

    def as_request(self) -> (dict, dict):
        getRecipientSharePermissionsResponse_query, getRecipientSharePermissionsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.permissions_out:
            getRecipientSharePermissionsResponse_body['permissions_out'] = [v.as_request()[1] for v in self.permissions_out]
        
        return getRecipientSharePermissionsResponse_query, getRecipientSharePermissionsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRecipientSharePermissionsResponse':
        return cls(
            permissions_out=[ShareToPrivilegeAssignment.from_dict(v) for v in d['permissions_out']] if 'permissions_out' in d else None,
        )



@dataclass
class GetSchemaResponse:
    
    # [Create:REQ Update:IGN] Name of parent Catalog.
    catalog_name: str = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Schema was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Schema creator.
    created_by: str = None
    # [Create,Update:IGN] Full name of Schema, in form of
    # <catalog_name>.<schema_name>.
    full_name: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Schema, relative to parent Catalog.
    name: str = None
    # [Create:IGN Update:OPT] Username of current owner of Schema.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Schema.
    privileges: 'List[GetSchemaResponsePrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # [Create,Update:IGN] Time at which this Schema was created, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Schema.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        getSchemaResponse_query, getSchemaResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            getSchemaResponse_body['catalog_name'] = self.catalog_name
        if self.comment:
            getSchemaResponse_body['comment'] = self.comment
        if self.created_at:
            getSchemaResponse_body['created_at'] = self.created_at
        if self.created_by:
            getSchemaResponse_body['created_by'] = self.created_by
        if self.full_name:
            getSchemaResponse_body['full_name'] = self.full_name
        if self.metastore_id:
            getSchemaResponse_body['metastore_id'] = self.metastore_id
        if self.name:
            getSchemaResponse_body['name'] = self.name
        if self.owner:
            getSchemaResponse_body['owner'] = self.owner
        if self.privileges:
            getSchemaResponse_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            getSchemaResponse_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.updated_at:
            getSchemaResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            getSchemaResponse_body['updated_by'] = self.updated_by
        
        return getSchemaResponse_query, getSchemaResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetSchemaResponse':
        return cls(
            catalog_name=d.get('catalog_name', None),
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            full_name=d.get('full_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class GetSchemaResponsePrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class GetSharePermissionsResponse:
    
    # Note to self (acain): Unfortunately, neither json_inline nor json_map work
    # here.
    privilege_assignments: 'List[PrivilegeAssignment]' = None

    def as_request(self) -> (dict, dict):
        getSharePermissionsResponse_query, getSharePermissionsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.privilege_assignments:
            getSharePermissionsResponse_body['privilege_assignments'] = [v.as_request()[1] for v in self.privilege_assignments]
        
        return getSharePermissionsResponse_query, getSharePermissionsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetSharePermissionsResponse':
        return cls(
            privilege_assignments=[PrivilegeAssignment.from_dict(v) for v in d['privilege_assignments']] if 'privilege_assignments' in d else None,
        )



@dataclass
class GetShareResponse:
    
    # [Create: OPT] comment when creating the share
    comment: str = None
    # [Create:IGN] Time at which this Share was created, in epoch milliseconds.
    created_at: int = None
    # [Create:IGN] Username of Share creator.
    created_by: str = None
    # [Create:REQ] Name of the Share.
    name: str = None
    # [Create: IGN] A list of shared data objects within the Share.
    objects: 'List[SharedDataObject]' = None

    def as_request(self) -> (dict, dict):
        getShareResponse_query, getShareResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.comment:
            getShareResponse_body['comment'] = self.comment
        if self.created_at:
            getShareResponse_body['created_at'] = self.created_at
        if self.created_by:
            getShareResponse_body['created_by'] = self.created_by
        if self.name:
            getShareResponse_body['name'] = self.name
        if self.objects:
            getShareResponse_body['objects'] = [v.as_request()[1] for v in self.objects]
        
        return getShareResponse_query, getShareResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetShareResponse':
        return cls(
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            name=d.get('name', None),
            objects=[SharedDataObject.from_dict(v) for v in d['objects']] if 'objects' in d else None,
        )



@dataclass
class GetStorageCredentialResponse:
    
    # The AWS IAM role configuration.
    aws_iam_role: 'AwsIamRole' = None
    # The Azure service principal configuration.
    azure_service_principal: 'AzureServicePrincipal' = None
    # [Create,Update:OPT] Comment associated with the credential.
    comment: str = None
    # [Create,Update:IGN] Time at which this Credential was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of credential creator.
    created_by: str = None
    # The GCP service account key configuration.
    gcp_service_account_key: 'GcpServiceAccountKey' = None
    # [Create:IGN] The unique identifier of the credential.
    id: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ, Update:OPT] The credential name. The name MUST be unique
    # within the Metastore.
    name: str = None
    # [Create:IGN Update:OPT] Username of current owner of credential.
    owner: str = None
    # [Create,Update:IGN] Time at which this credential was last modified, in
    # epoch milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the credential.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        getStorageCredentialResponse_query, getStorageCredentialResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.aws_iam_role:
            getStorageCredentialResponse_body['aws_iam_role'] = self.aws_iam_role.as_request()[1]
        if self.azure_service_principal:
            getStorageCredentialResponse_body['azure_service_principal'] = self.azure_service_principal.as_request()[1]
        if self.comment:
            getStorageCredentialResponse_body['comment'] = self.comment
        if self.created_at:
            getStorageCredentialResponse_body['created_at'] = self.created_at
        if self.created_by:
            getStorageCredentialResponse_body['created_by'] = self.created_by
        if self.gcp_service_account_key:
            getStorageCredentialResponse_body['gcp_service_account_key'] = self.gcp_service_account_key.as_request()[1]
        if self.id:
            getStorageCredentialResponse_body['id'] = self.id
        if self.metastore_id:
            getStorageCredentialResponse_body['metastore_id'] = self.metastore_id
        if self.name:
            getStorageCredentialResponse_body['name'] = self.name
        if self.owner:
            getStorageCredentialResponse_body['owner'] = self.owner
        if self.updated_at:
            getStorageCredentialResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            getStorageCredentialResponse_body['updated_by'] = self.updated_by
        
        return getStorageCredentialResponse_query, getStorageCredentialResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetStorageCredentialResponse':
        return cls(
            aws_iam_role=AwsIamRole.from_dict(d['aws_iam_role']) if 'aws_iam_role' in d else None,
            azure_service_principal=AzureServicePrincipal.from_dict(d['azure_service_principal']) if 'azure_service_principal' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            gcp_service_account_key=GcpServiceAccountKey.from_dict(d['gcp_service_account_key']) if 'gcp_service_account_key' in d else None,
            id=d.get('id', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



@dataclass
class GetTableResponse:
    
    # [Create:REQ Update:IGN] Name of parent Catalog.
    catalog_name: str = None
    # This name ('columns') is what the client actually sees as the field name
    # in messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    columns: 'List[ColumnInfo]' = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Table was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Table creator.
    created_by: str = None
    # [Create,Update:IGN] Unique ID of the data_access_configuration to use.
    data_access_configuration_id: str = None
    # [Create:REQ Update:OPT] Data source format ("DELTA", "CSV", etc.).
    data_source_format: 'GetTableResponseDataSourceFormat' = None
    # [Create,Update:IGN] Full name of Table, in form of
    # <catalog_name>.<schema_name>.<table_name>
    full_name: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Table, relative to parent Schema.
    name: str = None
    # [Create: IGN Update:OPT] Username of current owner of Table.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Table.
    privileges: 'List[GetTableResponsePrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # [Create:REQ Update:IGN] Name of parent Schema relative to its parent
    # Catalog.
    schema_name: str = None
    # [Create,Update:OPT] List of schemes whose objects can be referenced
    # without qualification.
    sql_path: str = None
    # [Create:OPT Update:IGN] Name of the storage credential this table used
    storage_credential_name: str = None
    # [Create:REQ Update:OPT] Storage root URL for table (for MANAGED, EXTERNAL
    # tables)
    storage_location: str = None
    # [Create:IGN Update:IGN] Name of Table, relative to parent Schema.
    table_id: str = None
    # [Create:REQ Update:OPT] Table type ("MANAGED", "EXTERNAL", "VIEW").
    table_type: 'GetTableResponseTableType' = None
    # [Create,Update:IGN] Time at which this Table was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the Table.
    updated_by: str = None
    # [Create,Update:OPT] View definition SQL (when table_type == "VIEW")
    view_definition: str = None

    def as_request(self) -> (dict, dict):
        getTableResponse_query, getTableResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            getTableResponse_body['catalog_name'] = self.catalog_name
        if self.columns:
            getTableResponse_body['columns'] = [v.as_request()[1] for v in self.columns]
        if self.comment:
            getTableResponse_body['comment'] = self.comment
        if self.created_at:
            getTableResponse_body['created_at'] = self.created_at
        if self.created_by:
            getTableResponse_body['created_by'] = self.created_by
        if self.data_access_configuration_id:
            getTableResponse_body['data_access_configuration_id'] = self.data_access_configuration_id
        if self.data_source_format:
            getTableResponse_body['data_source_format'] = self.data_source_format.value
        if self.full_name:
            getTableResponse_body['full_name'] = self.full_name
        if self.metastore_id:
            getTableResponse_body['metastore_id'] = self.metastore_id
        if self.name:
            getTableResponse_body['name'] = self.name
        if self.owner:
            getTableResponse_body['owner'] = self.owner
        if self.privileges:
            getTableResponse_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            getTableResponse_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.schema_name:
            getTableResponse_body['schema_name'] = self.schema_name
        if self.sql_path:
            getTableResponse_body['sql_path'] = self.sql_path
        if self.storage_credential_name:
            getTableResponse_body['storage_credential_name'] = self.storage_credential_name
        if self.storage_location:
            getTableResponse_body['storage_location'] = self.storage_location
        if self.table_id:
            getTableResponse_body['table_id'] = self.table_id
        if self.table_type:
            getTableResponse_body['table_type'] = self.table_type.value
        if self.updated_at:
            getTableResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            getTableResponse_body['updated_by'] = self.updated_by
        if self.view_definition:
            getTableResponse_body['view_definition'] = self.view_definition
        
        return getTableResponse_query, getTableResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetTableResponse':
        return cls(
            catalog_name=d.get('catalog_name', None),
            columns=[ColumnInfo.from_dict(v) for v in d['columns']] if 'columns' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            data_access_configuration_id=d.get('data_access_configuration_id', None),
            data_source_format=GetTableResponseDataSourceFormat(d['data_source_format']) if 'data_source_format' in d else None,
            full_name=d.get('full_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            schema_name=d.get('schema_name', None),
            sql_path=d.get('sql_path', None),
            storage_credential_name=d.get('storage_credential_name', None),
            storage_location=d.get('storage_location', None),
            table_id=d.get('table_id', None),
            table_type=GetTableResponseTableType(d['table_type']) if 'table_type' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
            view_definition=d.get('view_definition', None),
        )



class GetTableResponseDataSourceFormat(Enum):
    """[Create:REQ Update:OPT] Data source format ("DELTA", "CSV", etc.)."""
    
    AVRO = 'AVRO'
    CSV = 'CSV'
    DELTA = 'DELTA'
    DELTASHARING = 'DELTASHARING'
    JSON = 'JSON'
    ORC = 'ORC'
    PARQUET = 'PARQUET'
    TEXT = 'TEXT'
    UNITY_CATALOG = 'UNITY_CATALOG'
    UNKNOWN_DATA_SOURCE_FORMAT = 'UNKNOWN_DATA_SOURCE_FORMAT'

class GetTableResponsePrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

class GetTableResponseTableType(Enum):
    """[Create:REQ Update:OPT] Table type ("MANAGED", "EXTERNAL", "VIEW")."""
    
    EXTERNAL = 'EXTERNAL'
    MANAGED = 'MANAGED'
    UNKNOWN_TABLE_TYPE = 'UNKNOWN_TABLE_TYPE'
    VIEW = 'VIEW'

@dataclass
class IpAccessList:
    
    # Allowed IP Addresses in CIDR notation. Limit of 100.
    allowed_ip_addresses: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        ipAccessList_query, ipAccessList_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.allowed_ip_addresses:
            ipAccessList_body['allowed_ip_addresses'] = [v for v in self.allowed_ip_addresses]
        
        return ipAccessList_query, ipAccessList_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'IpAccessList':
        return cls(
            allowed_ip_addresses=d.get('allowed_ip_addresses', None),
        )



@dataclass
class ListCatalogsResponse:
    
    # AN array of catalog information objects.
    catalogs: 'List[CatalogInfo]' = None

    def as_request(self) -> (dict, dict):
        listCatalogsResponse_query, listCatalogsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalogs:
            listCatalogsResponse_body['catalogs'] = [v.as_request()[1] for v in self.catalogs]
        
        return listCatalogsResponse_query, listCatalogsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListCatalogsResponse':
        return cls(
            catalogs=[CatalogInfo.from_dict(v) for v in d['catalogs']] if 'catalogs' in d else None,
        )



@dataclass
class ListExternalLocationsResponse:
    
    # AN array of external locations.
    external_locations: 'List[ExternalLocationInfo]' = None

    def as_request(self) -> (dict, dict):
        listExternalLocationsResponse_query, listExternalLocationsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.external_locations:
            listExternalLocationsResponse_body['external_locations'] = [v.as_request()[1] for v in self.external_locations]
        
        return listExternalLocationsResponse_query, listExternalLocationsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListExternalLocationsResponse':
        return cls(
            external_locations=[ExternalLocationInfo.from_dict(v) for v in d['external_locations']] if 'external_locations' in d else None,
        )



@dataclass
class ListFilesRequest:
    
    # Required. Path URL to list files from.
    url: str # query
    # Optional. Name of a Storage Credential to use for accessing the URL.
    credential_name: str = None # query
    # Optional. Limit on number of results to return.
    max_results: int = None # query

    def as_request(self) -> (dict, dict):
        listFilesRequest_query, listFilesRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.credential_name:
            listFilesRequest_query['credential_name'] = self.credential_name
        if self.max_results:
            listFilesRequest_query['max_results'] = self.max_results
        if self.url:
            listFilesRequest_query['url'] = self.url
        
        return listFilesRequest_query, listFilesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListFilesRequest':
        return cls(
            credential_name=d.get('credential_name', None),
            max_results=d.get('max_results', None),
            url=d.get('url', None),
        )



@dataclass
class ListFilesResponse:
    
    # An array of file information objects.
    files: 'List[FileInfo]' = None

    def as_request(self) -> (dict, dict):
        listFilesResponse_query, listFilesResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.files:
            listFilesResponse_body['files'] = [v.as_request()[1] for v in self.files]
        
        return listFilesResponse_query, listFilesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListFilesResponse':
        return cls(
            files=[FileInfo.from_dict(v) for v in d['files']] if 'files' in d else None,
        )



@dataclass
class ListMetastoresResponse:
    
    # An array of Metastore information objects.
    metastores: 'List[MetastoreInfo]' = None

    def as_request(self) -> (dict, dict):
        listMetastoresResponse_query, listMetastoresResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.metastores:
            listMetastoresResponse_body['metastores'] = [v.as_request()[1] for v in self.metastores]
        
        return listMetastoresResponse_query, listMetastoresResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListMetastoresResponse':
        return cls(
            metastores=[MetastoreInfo.from_dict(v) for v in d['metastores']] if 'metastores' in d else None,
        )



@dataclass
class ListProviderSharesResponse:
    
    # An array of provider shares.
    shares: 'List[ProviderShare]' = None

    def as_request(self) -> (dict, dict):
        listProviderSharesResponse_query, listProviderSharesResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.shares:
            listProviderSharesResponse_body['shares'] = [v.as_request()[1] for v in self.shares]
        
        return listProviderSharesResponse_query, listProviderSharesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListProviderSharesResponse':
        return cls(
            shares=[ProviderShare.from_dict(v) for v in d['shares']] if 'shares' in d else None,
        )



@dataclass
class ListProvidersResponse:
    
    # An array of provider information objects.
    providers: 'List[ProviderInfo]' = None

    def as_request(self) -> (dict, dict):
        listProvidersResponse_query, listProvidersResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.providers:
            listProvidersResponse_body['providers'] = [v.as_request()[1] for v in self.providers]
        
        return listProvidersResponse_query, listProvidersResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListProvidersResponse':
        return cls(
            providers=[ProviderInfo.from_dict(v) for v in d['providers']] if 'providers' in d else None,
        )



@dataclass
class ListRecipientsResponse:
    
    # An array of recipient information objects.
    recipients: 'List[RecipientInfo]' = None

    def as_request(self) -> (dict, dict):
        listRecipientsResponse_query, listRecipientsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.recipients:
            listRecipientsResponse_body['recipients'] = [v.as_request()[1] for v in self.recipients]
        
        return listRecipientsResponse_query, listRecipientsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRecipientsResponse':
        return cls(
            recipients=[RecipientInfo.from_dict(v) for v in d['recipients']] if 'recipients' in d else None,
        )



@dataclass
class ListSchemasResponse:
    
    # An array of schema information objects.
    schemas: 'List[SchemaInfo]' = None

    def as_request(self) -> (dict, dict):
        listSchemasResponse_query, listSchemasResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.schemas:
            listSchemasResponse_body['schemas'] = [v.as_request()[1] for v in self.schemas]
        
        return listSchemasResponse_query, listSchemasResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListSchemasResponse':
        return cls(
            schemas=[SchemaInfo.from_dict(v) for v in d['schemas']] if 'schemas' in d else None,
        )



@dataclass
class ListSharesResponse:
    
    # An array of data share information objects.
    shares: 'List[ShareInfo]' = None

    def as_request(self) -> (dict, dict):
        listSharesResponse_query, listSharesResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.shares:
            listSharesResponse_body['shares'] = [v.as_request()[1] for v in self.shares]
        
        return listSharesResponse_query, listSharesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListSharesResponse':
        return cls(
            shares=[ShareInfo.from_dict(v) for v in d['shares']] if 'shares' in d else None,
        )



@dataclass
class ListStorageCredentialsResponse:
    
    # TODO: add pagination to UC list APIs.
    storage_credentials: 'List[StorageCredentialInfo]' = None

    def as_request(self) -> (dict, dict):
        listStorageCredentialsResponse_query, listStorageCredentialsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.storage_credentials:
            listStorageCredentialsResponse_body['storage_credentials'] = [v.as_request()[1] for v in self.storage_credentials]
        
        return listStorageCredentialsResponse_query, listStorageCredentialsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListStorageCredentialsResponse':
        return cls(
            storage_credentials=[StorageCredentialInfo.from_dict(v) for v in d['storage_credentials']] if 'storage_credentials' in d else None,
        )



@dataclass
class ListTableSummariesResponse:
    
    # Optional. Opaque token for pagination. Empty if there's no more page.
    next_page_token: str = None
    # Only name, catalog_name, schema_name, full_name and table_type will be
    # set.
    tables: 'List[TableSummary]' = None

    def as_request(self) -> (dict, dict):
        listTableSummariesResponse_query, listTableSummariesResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.next_page_token:
            listTableSummariesResponse_body['next_page_token'] = self.next_page_token
        if self.tables:
            listTableSummariesResponse_body['tables'] = [v.as_request()[1] for v in self.tables]
        
        return listTableSummariesResponse_query, listTableSummariesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListTableSummariesResponse':
        return cls(
            next_page_token=d.get('next_page_token', None),
            tables=[TableSummary.from_dict(v) for v in d['tables']] if 'tables' in d else None,
        )



@dataclass
class ListTablesResponse:
    
    # An array of table information objects.
    tables: 'List[TableInfo]' = None

    def as_request(self) -> (dict, dict):
        listTablesResponse_query, listTablesResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.tables:
            listTablesResponse_body['tables'] = [v.as_request()[1] for v in self.tables]
        
        return listTablesResponse_query, listTablesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListTablesResponse':
        return cls(
            tables=[TableInfo.from_dict(v) for v in d['tables']] if 'tables' in d else None,
        )



@dataclass
class MetastoreInfo:
    
    # [Create,Update:IGN] Time at which this Metastore was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Metastore creator.
    created_by: str = None
    # [Create:IGN Update:OPT] Unique identifier of (Default) Data Access
    # Configuration
    default_data_access_config_id: str = None
    # [Create:IGN Update:OPT] Whether Delta Sharing is enabled on this
    # metastore.
    delta_sharing_enabled: bool = None
    # [Create:IGN Update:OPT] The lifetime of delta sharing recipient token in
    # seconds
    delta_sharing_recipient_token_lifetime_in_seconds: int = None
    # [Create,Update:IGN] Unique identifier of Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Metastore.
    name: str = None
    # [Create:IGN Update:OPT] The owner of the metastore.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Metastore.
    privileges: 'List[MetastoreInfoPrivilegesItem]' = None
    # The region this metastore has an afinity to. This is used by
    # accounts-manager. Ignored by Unity Catalog.
    region: str = None
    # [Create:REQ Update:ERR] Storage root URL for Metastore
    storage_root: str = None
    # [Create:IGN Update:OPT] UUID of storage credential to access storage_root
    storage_root_credential_id: str = None
    # [Create,Update:IGN] Time at which the Metastore was last modified, in
    # epoch milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the Metastore.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        metastoreInfo_query, metastoreInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.created_at:
            metastoreInfo_body['created_at'] = self.created_at
        if self.created_by:
            metastoreInfo_body['created_by'] = self.created_by
        if self.default_data_access_config_id:
            metastoreInfo_body['default_data_access_config_id'] = self.default_data_access_config_id
        if self.delta_sharing_enabled:
            metastoreInfo_body['delta_sharing_enabled'] = self.delta_sharing_enabled
        if self.delta_sharing_recipient_token_lifetime_in_seconds:
            metastoreInfo_body['delta_sharing_recipient_token_lifetime_in_seconds'] = self.delta_sharing_recipient_token_lifetime_in_seconds
        if self.metastore_id:
            metastoreInfo_body['metastore_id'] = self.metastore_id
        if self.name:
            metastoreInfo_body['name'] = self.name
        if self.owner:
            metastoreInfo_body['owner'] = self.owner
        if self.privileges:
            metastoreInfo_body['privileges'] = [v for v in self.privileges]
        if self.region:
            metastoreInfo_body['region'] = self.region
        if self.storage_root:
            metastoreInfo_body['storage_root'] = self.storage_root
        if self.storage_root_credential_id:
            metastoreInfo_body['storage_root_credential_id'] = self.storage_root_credential_id
        if self.updated_at:
            metastoreInfo_body['updated_at'] = self.updated_at
        if self.updated_by:
            metastoreInfo_body['updated_by'] = self.updated_by
        
        return metastoreInfo_query, metastoreInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'MetastoreInfo':
        return cls(
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            default_data_access_config_id=d.get('default_data_access_config_id', None),
            delta_sharing_enabled=d.get('delta_sharing_enabled', None),
            delta_sharing_recipient_token_lifetime_in_seconds=d.get('delta_sharing_recipient_token_lifetime_in_seconds', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            region=d.get('region', None),
            storage_root=d.get('storage_root', None),
            storage_root_credential_id=d.get('storage_root_credential_id', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class MetastoreInfoPrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class Partition:
    
    # An array of partition values.
    values: 'List[PartitionValue]' = None

    def as_request(self) -> (dict, dict):
        partition_query, partition_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.values:
            partition_body['values'] = [v.as_request()[1] for v in self.values]
        
        return partition_query, partition_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Partition':
        return cls(
            values=[PartitionValue.from_dict(v) for v in d['values']] if 'values' in d else None,
        )



@dataclass
class PartitionValue:
    
    # The name of the partition column.
    name: str = None
    # The operator to apply for the value.
    op: 'PartitionValueOp' = None
    # The value of the partition column. When this value is not set, it means
    # `null` value.
    value: str = None

    def as_request(self) -> (dict, dict):
        partitionValue_query, partitionValue_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            partitionValue_body['name'] = self.name
        if self.op:
            partitionValue_body['op'] = self.op.value
        if self.value:
            partitionValue_body['value'] = self.value
        
        return partitionValue_query, partitionValue_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PartitionValue':
        return cls(
            name=d.get('name', None),
            op=PartitionValueOp(d['op']) if 'op' in d else None,
            value=d.get('value', None),
        )



class PartitionValueOp(Enum):
    """The operator to apply for the value."""
    
    EQUAL = 'EQUAL'
    LIKE = 'LIKE'

@dataclass
class PermissionsChange:
    
    # The set of privileges to add.
    add: 'List[PermissionsChangeAddItem]' = None
    # The principal whose privileges we are changing.
    principal: str = None
    # The set of privileges to remove.
    remove: 'List[PermissionsChangeRemoveItem]' = None

    def as_request(self) -> (dict, dict):
        permissionsChange_query, permissionsChange_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.add:
            permissionsChange_body['add'] = [v for v in self.add]
        if self.principal:
            permissionsChange_body['principal'] = self.principal
        if self.remove:
            permissionsChange_body['remove'] = [v for v in self.remove]
        
        return permissionsChange_query, permissionsChange_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermissionsChange':
        return cls(
            add=d.get('add', None),
            principal=d.get('principal', None),
            remove=d.get('remove', None),
        )



class PermissionsChangeAddItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

class PermissionsChangeRemoveItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class PrivilegeAssignment:
    
    # The principal (user email address or group name).
    principal: str = None
    # The privileges assigned to the principal.
    privileges: 'List[PrivilegeAssignmentPrivilegesItem]' = None

    def as_request(self) -> (dict, dict):
        privilegeAssignment_query, privilegeAssignment_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.principal:
            privilegeAssignment_body['principal'] = self.principal
        if self.privileges:
            privilegeAssignment_body['privileges'] = [v for v in self.privileges]
        
        return privilegeAssignment_query, privilegeAssignment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PrivilegeAssignment':
        return cls(
            principal=d.get('principal', None),
            privileges=d.get('privileges', None),
        )



class PrivilegeAssignmentPrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class ProviderInfo:
    
    # [Create,Update:IGN] Whether this provider is successfully activated by the
    # data provider. This field is only present when the authentication type is
    # DATABRICKS.
    activated_by_provider: bool = None
    # [Create:REQ,Update:IGN] The delta sharing authentication type.
    authentication_type: 'ProviderInfoAuthenticationType' = None
    # [Create,Update:OPT] Description about the provider.
    comment: str = None
    # [Create,Update:IGN] Time at which this Provider was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Provider creator.
    created_by: str = None
    # [Create,Update:REQ] The name of the Provider.
    name: str = None
    # [Create,Update:IGN] This field is only present when the authentication
    # type is TOKEN.
    recipient_profile: 'RecipientProfile' = None
    # [Create,Update:OPT] This field is only present when the authentication
    # type is TOKEN.
    recipient_profile_str: str = None
    # [Create,Update:IGN] The server-generated one-time sharing code. This field
    # is only present when the authentication type is DATABRICKS.
    sharing_code: str = None
    # [Create,Update:IGN] Time at which this Provider was created, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Share.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        providerInfo_query, providerInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activated_by_provider:
            providerInfo_body['activated_by_provider'] = self.activated_by_provider
        if self.authentication_type:
            providerInfo_body['authentication_type'] = self.authentication_type.value
        if self.comment:
            providerInfo_body['comment'] = self.comment
        if self.created_at:
            providerInfo_body['created_at'] = self.created_at
        if self.created_by:
            providerInfo_body['created_by'] = self.created_by
        if self.name:
            providerInfo_body['name'] = self.name
        if self.recipient_profile:
            providerInfo_body['recipient_profile'] = self.recipient_profile.as_request()[1]
        if self.recipient_profile_str:
            providerInfo_body['recipient_profile_str'] = self.recipient_profile_str
        if self.sharing_code:
            providerInfo_body['sharing_code'] = self.sharing_code
        if self.updated_at:
            providerInfo_body['updated_at'] = self.updated_at
        if self.updated_by:
            providerInfo_body['updated_by'] = self.updated_by
        
        return providerInfo_query, providerInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ProviderInfo':
        return cls(
            activated_by_provider=d.get('activated_by_provider', None),
            authentication_type=ProviderInfoAuthenticationType(d['authentication_type']) if 'authentication_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            name=d.get('name', None),
            recipient_profile=RecipientProfile.from_dict(d['recipient_profile']) if 'recipient_profile' in d else None,
            recipient_profile_str=d.get('recipient_profile_str', None),
            sharing_code=d.get('sharing_code', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class ProviderInfoAuthenticationType(Enum):
    """[Create:REQ,Update:IGN] The delta sharing authentication type."""
    
    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'
    UNKNOWN = 'UNKNOWN'

@dataclass
class ProviderShare:
    
    # The name of the Provider Share.
    name: str = None

    def as_request(self) -> (dict, dict):
        providerShare_query, providerShare_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            providerShare_body['name'] = self.name
        
        return providerShare_query, providerShare_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ProviderShare':
        return cls(
            name=d.get('name', None),
        )



@dataclass
class RecipientInfo:
    
    # [Create:IGN,Update:IGN] A boolean status field showing whether the
    # Recipient's activation URL has been exercised or not.
    activated: bool = None
    # [Create:IGN,Update:IGN] Full activation url to retrieve the access token.
    # It will be empty if the token is already retrieved.
    activation_url: str = None
    # [Create:REQ,Update:IGN] The delta sharing authentication type.
    authentication_type: 'RecipientInfoAuthenticationType' = None
    # [Create:OPT,Update:OPT] Description about the recipient.
    comment: str = None
    # [Create:IGN,Update:IGN] Time at which this recipient was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create:IGN,Update:IGN] Username of recipient creator.
    created_by: str = None
    # [Create:OPT,Update:OPT] IP Access List
    ip_access_list: 'IpAccessList' = None
    # [Create:REQ,Update:OPT] Name of Recipient.
    name: str = None
    # [Create:OPT,Update:IGN] The one-time sharing code provided by the data
    # recipient. This field is only present when the authentication type is
    # DATABRICKS.
    sharing_code: str = None
    # [Create:IGN,Update:IGN] Recipient Tokens. This field is only present when
    # the authentication type is TOKEN.
    tokens: 'List[RecipientTokenInfo]' = None
    # [Create:IGN,Update:IGN] Time at which this recipient was updated, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create:IGN,Update:IGN] Username of recipient updater.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        recipientInfo_query, recipientInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activated:
            recipientInfo_body['activated'] = self.activated
        if self.activation_url:
            recipientInfo_body['activation_url'] = self.activation_url
        if self.authentication_type:
            recipientInfo_body['authentication_type'] = self.authentication_type.value
        if self.comment:
            recipientInfo_body['comment'] = self.comment
        if self.created_at:
            recipientInfo_body['created_at'] = self.created_at
        if self.created_by:
            recipientInfo_body['created_by'] = self.created_by
        if self.ip_access_list:
            recipientInfo_body['ip_access_list'] = self.ip_access_list.as_request()[1]
        if self.name:
            recipientInfo_body['name'] = self.name
        if self.sharing_code:
            recipientInfo_body['sharing_code'] = self.sharing_code
        if self.tokens:
            recipientInfo_body['tokens'] = [v.as_request()[1] for v in self.tokens]
        if self.updated_at:
            recipientInfo_body['updated_at'] = self.updated_at
        if self.updated_by:
            recipientInfo_body['updated_by'] = self.updated_by
        
        return recipientInfo_query, recipientInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RecipientInfo':
        return cls(
            activated=d.get('activated', None),
            activation_url=d.get('activation_url', None),
            authentication_type=RecipientInfoAuthenticationType(d['authentication_type']) if 'authentication_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            ip_access_list=IpAccessList.from_dict(d['ip_access_list']) if 'ip_access_list' in d else None,
            name=d.get('name', None),
            sharing_code=d.get('sharing_code', None),
            tokens=[RecipientTokenInfo.from_dict(v) for v in d['tokens']] if 'tokens' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class RecipientInfoAuthenticationType(Enum):
    """[Create:REQ,Update:IGN] The delta sharing authentication type."""
    
    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'
    UNKNOWN = 'UNKNOWN'

@dataclass
class RecipientProfile:
    
    # The token used to authorize the recipient.
    bearer_token: str = None
    # The endpoint for the share to be used by the recipient.
    endpoint: str = None
    # The version number of the recipient's credentials on a share.
    share_credentials_version: int = None

    def as_request(self) -> (dict, dict):
        recipientProfile_query, recipientProfile_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.bearer_token:
            recipientProfile_body['bearer_token'] = self.bearer_token
        if self.endpoint:
            recipientProfile_body['endpoint'] = self.endpoint
        if self.share_credentials_version:
            recipientProfile_body['share_credentials_version'] = self.share_credentials_version
        
        return recipientProfile_query, recipientProfile_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RecipientProfile':
        return cls(
            bearer_token=d.get('bearer_token', None),
            endpoint=d.get('endpoint', None),
            share_credentials_version=d.get('share_credentials_version', None),
        )



@dataclass
class RecipientTokenInfo:
    
    # Full activation URL to retrieve the access token. It will be empty if the
    # token is already retrieved.
    activation_url: str = None
    # Time at which this recipient Token was created, in epoch milliseconds.
    created_at: int = None
    # Username of recipient token creator.
    created_by: str = None
    # Expiration timestamp of the token in epoch milliseconds.
    expiration_time: int = None
    # Unique ID of the recipient token.
    id: str = None
    # Time at which this recipient Token was updated, in epoch milliseconds.
    updated_at: int = None
    # Username of recipient Token updater.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        recipientTokenInfo_query, recipientTokenInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activation_url:
            recipientTokenInfo_body['activation_url'] = self.activation_url
        if self.created_at:
            recipientTokenInfo_body['created_at'] = self.created_at
        if self.created_by:
            recipientTokenInfo_body['created_by'] = self.created_by
        if self.expiration_time:
            recipientTokenInfo_body['expiration_time'] = self.expiration_time
        if self.id:
            recipientTokenInfo_body['id'] = self.id
        if self.updated_at:
            recipientTokenInfo_body['updated_at'] = self.updated_at
        if self.updated_by:
            recipientTokenInfo_body['updated_by'] = self.updated_by
        
        return recipientTokenInfo_query, recipientTokenInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RecipientTokenInfo':
        return cls(
            activation_url=d.get('activation_url', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            expiration_time=d.get('expiration_time', None),
            id=d.get('id', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



@dataclass
class RetrieveTokenResponse:
    
    # The token used to authorize the recipient.
    bearerToken: str = None
    # The endpoint for the share to be used by the recipient.
    endpoint: str = None
    # Expiration timestamp of the token in epoch milliseconds.
    expirationTime: str = None
    # These field names must follow the delta sharing protocol.
    shareCredentialsVersion: int = None

    def as_request(self) -> (dict, dict):
        retrieveTokenResponse_query, retrieveTokenResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.bearerToken:
            retrieveTokenResponse_body['bearerToken'] = self.bearerToken
        if self.endpoint:
            retrieveTokenResponse_body['endpoint'] = self.endpoint
        if self.expirationTime:
            retrieveTokenResponse_body['expirationTime'] = self.expirationTime
        if self.shareCredentialsVersion:
            retrieveTokenResponse_body['shareCredentialsVersion'] = self.shareCredentialsVersion
        
        return retrieveTokenResponse_query, retrieveTokenResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RetrieveTokenResponse':
        return cls(
            bearerToken=d.get('bearerToken', None),
            endpoint=d.get('endpoint', None),
            expirationTime=d.get('expirationTime', None),
            shareCredentialsVersion=d.get('shareCredentialsVersion', None),
        )



@dataclass
class RotateRecipientToken:
    
    # Required. The name of the recipient.
    name: str # path
    # Required. This will set the expiration_time of existing token only to a
    # smaller timestamp, it cannot extend the expiration_time. Use 0 to expire
    # the existing token immediately, negative number will return an error.
    existing_token_expire_in_seconds: int = None

    def as_request(self) -> (dict, dict):
        rotateRecipientToken_query, rotateRecipientToken_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.existing_token_expire_in_seconds:
            rotateRecipientToken_body['existing_token_expire_in_seconds'] = self.existing_token_expire_in_seconds
        if self.name:
            rotateRecipientToken_body['name'] = self.name
        
        return rotateRecipientToken_query, rotateRecipientToken_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RotateRecipientToken':
        return cls(
            existing_token_expire_in_seconds=d.get('existing_token_expire_in_seconds', None),
            name=d.get('name', None),
        )



@dataclass
class RotateRecipientTokenResponse:
    
    # [Create:IGN, Update:IGN] A boolean status field showing whether the
    # Recipient's activation URL has been exercised or not.
    activated: bool = None
    # [Create:IGN, Update:IGN] Full activation url to retrieve the access token.
    # It will be empty if the token is already retrieved.
    activation_url: str = None
    # [Create:REQ, Update:IGN] The delta sharing authentication type.
    authentication_type: 'RotateRecipientTokenResponseAuthenticationType' = None
    # [Create:OPT,Update:OPT] Description about the recipient.
    comment: str = None
    # [Create:IGN, Update:IGN] Time at which this recipient was created, in
    # epoch milliseconds.
    created_at: int = None
    # [Create:IGN, Update:IGN] Username of recipient creator.
    created_by: str = None
    # [Create:OPT,Update:OPT] IP Access List
    ip_access_list: 'IpAccessList' = None
    # [Create:REQ, Update:OPT] Name of Recipient.
    name: str = None
    # [Create:OPT,Update:IGN] The one-time sharing code provided by the data
    # recipient. This field is only present when the authentication type is
    # DATABRICKS.
    sharing_code: str = None
    # [Create:IGN,Update:IGN] recipient Tokens. This field is only present when
    # the authentication type is TOKEN.
    tokens: 'List[RecipientTokenInfo]' = None
    # [Create:IGN,Update:IGN] Time at which the recipient was updated, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create:IGN,Update:IGN] Username of recipient updater.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        rotateRecipientTokenResponse_query, rotateRecipientTokenResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activated:
            rotateRecipientTokenResponse_body['activated'] = self.activated
        if self.activation_url:
            rotateRecipientTokenResponse_body['activation_url'] = self.activation_url
        if self.authentication_type:
            rotateRecipientTokenResponse_body['authentication_type'] = self.authentication_type.value
        if self.comment:
            rotateRecipientTokenResponse_body['comment'] = self.comment
        if self.created_at:
            rotateRecipientTokenResponse_body['created_at'] = self.created_at
        if self.created_by:
            rotateRecipientTokenResponse_body['created_by'] = self.created_by
        if self.ip_access_list:
            rotateRecipientTokenResponse_body['ip_access_list'] = self.ip_access_list.as_request()[1]
        if self.name:
            rotateRecipientTokenResponse_body['name'] = self.name
        if self.sharing_code:
            rotateRecipientTokenResponse_body['sharing_code'] = self.sharing_code
        if self.tokens:
            rotateRecipientTokenResponse_body['tokens'] = [v.as_request()[1] for v in self.tokens]
        if self.updated_at:
            rotateRecipientTokenResponse_body['updated_at'] = self.updated_at
        if self.updated_by:
            rotateRecipientTokenResponse_body['updated_by'] = self.updated_by
        
        return rotateRecipientTokenResponse_query, rotateRecipientTokenResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RotateRecipientTokenResponse':
        return cls(
            activated=d.get('activated', None),
            activation_url=d.get('activation_url', None),
            authentication_type=RotateRecipientTokenResponseAuthenticationType(d['authentication_type']) if 'authentication_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            ip_access_list=IpAccessList.from_dict(d['ip_access_list']) if 'ip_access_list' in d else None,
            name=d.get('name', None),
            sharing_code=d.get('sharing_code', None),
            tokens=[RecipientTokenInfo.from_dict(v) for v in d['tokens']] if 'tokens' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class RotateRecipientTokenResponseAuthenticationType(Enum):
    """[Create:REQ, Update:IGN] The delta sharing authentication type."""
    
    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'
    UNKNOWN = 'UNKNOWN'

@dataclass
class SchemaInfo:
    
    # [Create:REQ Update:IGN] Name of parent Catalog.
    catalog_name: str = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Schema was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Schema creator.
    created_by: str = None
    # [Create,Update:IGN] Full name of Schema, in form of
    # <catalog_name>.<schema_name>.
    full_name: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Schema, relative to parent Catalog.
    name: str = None
    # [Create:IGN Update:OPT] Username of current owner of Schema.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Schema.
    privileges: 'List[SchemaInfoPrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # [Create,Update:IGN] Time at which this Schema was created, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Schema.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        schemaInfo_query, schemaInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            schemaInfo_body['catalog_name'] = self.catalog_name
        if self.comment:
            schemaInfo_body['comment'] = self.comment
        if self.created_at:
            schemaInfo_body['created_at'] = self.created_at
        if self.created_by:
            schemaInfo_body['created_by'] = self.created_by
        if self.full_name:
            schemaInfo_body['full_name'] = self.full_name
        if self.metastore_id:
            schemaInfo_body['metastore_id'] = self.metastore_id
        if self.name:
            schemaInfo_body['name'] = self.name
        if self.owner:
            schemaInfo_body['owner'] = self.owner
        if self.privileges:
            schemaInfo_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            schemaInfo_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.updated_at:
            schemaInfo_body['updated_at'] = self.updated_at
        if self.updated_by:
            schemaInfo_body['updated_by'] = self.updated_by
        
        return schemaInfo_query, schemaInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SchemaInfo':
        return cls(
            catalog_name=d.get('catalog_name', None),
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            full_name=d.get('full_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class SchemaInfoPrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class ShareInfo:
    
    # [Create: OPT] comment when creating the share
    comment: str = None
    # [Create:IGN] Time at which this Share was created, in epoch milliseconds.
    created_at: int = None
    # [Create:IGN] Username of Share creator.
    created_by: str = None
    # [Create:REQ] Name of the Share.
    name: str = None
    # [Create: IGN] A list of shared data objects within the Share.
    objects: 'List[SharedDataObject]' = None

    def as_request(self) -> (dict, dict):
        shareInfo_query, shareInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.comment:
            shareInfo_body['comment'] = self.comment
        if self.created_at:
            shareInfo_body['created_at'] = self.created_at
        if self.created_by:
            shareInfo_body['created_by'] = self.created_by
        if self.name:
            shareInfo_body['name'] = self.name
        if self.objects:
            shareInfo_body['objects'] = [v.as_request()[1] for v in self.objects]
        
        return shareInfo_query, shareInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ShareInfo':
        return cls(
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            name=d.get('name', None),
            objects=[SharedDataObject.from_dict(v) for v in d['objects']] if 'objects' in d else None,
        )



@dataclass
class ShareToPrivilegeAssignment:
    
    # The privileges assigned to the principal.
    privilege_assignments: 'List[PrivilegeAssignment]' = None
    # The share name.
    share_name: str = None

    def as_request(self) -> (dict, dict):
        shareToPrivilegeAssignment_query, shareToPrivilegeAssignment_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.privilege_assignments:
            shareToPrivilegeAssignment_body['privilege_assignments'] = [v.as_request()[1] for v in self.privilege_assignments]
        if self.share_name:
            shareToPrivilegeAssignment_body['share_name'] = self.share_name
        
        return shareToPrivilegeAssignment_query, shareToPrivilegeAssignment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ShareToPrivilegeAssignment':
        return cls(
            privilege_assignments=[PrivilegeAssignment.from_dict(v) for v in d['privilege_assignments']] if 'privilege_assignments' in d else None,
            share_name=d.get('share_name', None),
        )



@dataclass
class SharedDataObject:
    
    # The time when this data object is added to the Share, in epoch
    # milliseconds. Output only field. [Update:IGN]
    added_at: int = None
    # Username of the sharer. Output only field. [Update:IGN]
    added_by: str = None
    # A user-provided comment when adding the data object to the share.
    # [Update:OPT]
    comment: str = None
    # The type of the data object. Output only field. [Update:IGN]
    data_object_type: str = None
    # A fully qualified name that uniquely identifies a data object. For
    # example, a table's fully qualified name is in the format of
    # `<catalog>.<schema>.<table>`. [Update:REQ]
    name: str = None
    # Array of partitions for the shared data.
    partitions: 'List[Partition]' = None
    # A user-provided new name for the data object within the share. If this new
    # name is not not provided, the object's original name will be used as the
    # `shared_as` name. The `shared_as` name must be unique within a Share.
    # 
    # For tables, the new name must follow the format of `<schema>.<table>`.
    # [Update:OPT]
    shared_as: str = None

    def as_request(self) -> (dict, dict):
        sharedDataObject_query, sharedDataObject_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.added_at:
            sharedDataObject_body['added_at'] = self.added_at
        if self.added_by:
            sharedDataObject_body['added_by'] = self.added_by
        if self.comment:
            sharedDataObject_body['comment'] = self.comment
        if self.data_object_type:
            sharedDataObject_body['data_object_type'] = self.data_object_type
        if self.name:
            sharedDataObject_body['name'] = self.name
        if self.partitions:
            sharedDataObject_body['partitions'] = [v.as_request()[1] for v in self.partitions]
        if self.shared_as:
            sharedDataObject_body['shared_as'] = self.shared_as
        
        return sharedDataObject_query, sharedDataObject_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SharedDataObject':
        return cls(
            added_at=d.get('added_at', None),
            added_by=d.get('added_by', None),
            comment=d.get('comment', None),
            data_object_type=d.get('data_object_type', None),
            name=d.get('name', None),
            partitions=[Partition.from_dict(v) for v in d['partitions']] if 'partitions' in d else None,
            shared_as=d.get('shared_as', None),
        )



@dataclass
class SharedDataObjectUpdate:
    
    # One of: **ADD**, **REMOVE**.
    action: 'SharedDataObjectUpdateAction' = None
    # The data object that is being updated (added / removed).
    data_object: 'SharedDataObject' = None

    def as_request(self) -> (dict, dict):
        sharedDataObjectUpdate_query, sharedDataObjectUpdate_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.action:
            sharedDataObjectUpdate_body['action'] = self.action.value
        if self.data_object:
            sharedDataObjectUpdate_body['data_object'] = self.data_object.as_request()[1]
        
        return sharedDataObjectUpdate_query, sharedDataObjectUpdate_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SharedDataObjectUpdate':
        return cls(
            action=SharedDataObjectUpdateAction(d['action']) if 'action' in d else None,
            data_object=SharedDataObject.from_dict(d['data_object']) if 'data_object' in d else None,
        )



class SharedDataObjectUpdateAction(Enum):
    """One of: **ADD**, **REMOVE**."""
    
    ADD = 'ADD'
    REMOVE = 'REMOVE'

@dataclass
class StorageCredentialInfo:
    
    # The AWS IAM role configuration.
    aws_iam_role: 'AwsIamRole' = None
    # The Azure service principal configuration.
    azure_service_principal: 'AzureServicePrincipal' = None
    # [Create,Update:OPT] Comment associated with the credential.
    comment: str = None
    # [Create,Update:IGN] Time at which this Credential was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of credential creator.
    created_by: str = None
    # The GCP service account key configuration.
    gcp_service_account_key: 'GcpServiceAccountKey' = None
    # [Create:IGN] The unique identifier of the credential.
    id: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ, Update:OPT] The credential name. The name MUST be unique
    # within the Metastore.
    name: str = None
    # [Create:IGN Update:OPT] Username of current owner of credential.
    owner: str = None
    # [Create,Update:IGN] Time at which this credential was last modified, in
    # epoch milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the credential.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        storageCredentialInfo_query, storageCredentialInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.aws_iam_role:
            storageCredentialInfo_body['aws_iam_role'] = self.aws_iam_role.as_request()[1]
        if self.azure_service_principal:
            storageCredentialInfo_body['azure_service_principal'] = self.azure_service_principal.as_request()[1]
        if self.comment:
            storageCredentialInfo_body['comment'] = self.comment
        if self.created_at:
            storageCredentialInfo_body['created_at'] = self.created_at
        if self.created_by:
            storageCredentialInfo_body['created_by'] = self.created_by
        if self.gcp_service_account_key:
            storageCredentialInfo_body['gcp_service_account_key'] = self.gcp_service_account_key.as_request()[1]
        if self.id:
            storageCredentialInfo_body['id'] = self.id
        if self.metastore_id:
            storageCredentialInfo_body['metastore_id'] = self.metastore_id
        if self.name:
            storageCredentialInfo_body['name'] = self.name
        if self.owner:
            storageCredentialInfo_body['owner'] = self.owner
        if self.updated_at:
            storageCredentialInfo_body['updated_at'] = self.updated_at
        if self.updated_by:
            storageCredentialInfo_body['updated_by'] = self.updated_by
        
        return storageCredentialInfo_query, storageCredentialInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StorageCredentialInfo':
        return cls(
            aws_iam_role=AwsIamRole.from_dict(d['aws_iam_role']) if 'aws_iam_role' in d else None,
            azure_service_principal=AzureServicePrincipal.from_dict(d['azure_service_principal']) if 'azure_service_principal' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            gcp_service_account_key=GcpServiceAccountKey.from_dict(d['gcp_service_account_key']) if 'gcp_service_account_key' in d else None,
            id=d.get('id', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



@dataclass
class StringKeyValuePair:
    
    # The key for the tuple.
    key: str
    # The value for the tuple.
    value: str

    def as_request(self) -> (dict, dict):
        stringKeyValuePair_query, stringKeyValuePair_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.key:
            stringKeyValuePair_body['key'] = self.key
        if self.value:
            stringKeyValuePair_body['value'] = self.value
        
        return stringKeyValuePair_query, stringKeyValuePair_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StringKeyValuePair':
        return cls(
            key=d.get('key', None),
            value=d.get('value', None),
        )



@dataclass
class TableInfo:
    
    # [Create:REQ Update:IGN] Name of parent Catalog.
    catalog_name: str = None
    # This name ('columns') is what the client actually sees as the field name
    # in messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    columns: 'List[ColumnInfo]' = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Table was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Table creator.
    created_by: str = None
    # [Create,Update:IGN] Unique ID of the data_access_configuration to use.
    data_access_configuration_id: str = None
    # [Create:REQ Update:OPT] Data source format ("DELTA", "CSV", etc.).
    data_source_format: 'TableInfoDataSourceFormat' = None
    # [Create,Update:IGN] Full name of Table, in form of
    # <catalog_name>.<schema_name>.<table_name>
    full_name: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Table, relative to parent Schema.
    name: str = None
    # [Create: IGN Update:OPT] Username of current owner of Table.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Table.
    privileges: 'List[TableInfoPrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # [Create:REQ Update:IGN] Name of parent Schema relative to its parent
    # Catalog.
    schema_name: str = None
    # [Create,Update:OPT] List of schemes whose objects can be referenced
    # without qualification.
    sql_path: str = None
    # [Create:OPT Update:IGN] Name of the storage credential this table used
    storage_credential_name: str = None
    # [Create:REQ Update:OPT] Storage root URL for table (for MANAGED, EXTERNAL
    # tables)
    storage_location: str = None
    # [Create:IGN Update:IGN] Name of Table, relative to parent Schema.
    table_id: str = None
    # [Create:REQ Update:OPT] Table type ("MANAGED", "EXTERNAL", "VIEW").
    table_type: 'TableInfoTableType' = None
    # [Create,Update:IGN] Time at which this Table was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the Table.
    updated_by: str = None
    # [Create,Update:OPT] View definition SQL (when table_type == "VIEW")
    view_definition: str = None

    def as_request(self) -> (dict, dict):
        tableInfo_query, tableInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            tableInfo_body['catalog_name'] = self.catalog_name
        if self.columns:
            tableInfo_body['columns'] = [v.as_request()[1] for v in self.columns]
        if self.comment:
            tableInfo_body['comment'] = self.comment
        if self.created_at:
            tableInfo_body['created_at'] = self.created_at
        if self.created_by:
            tableInfo_body['created_by'] = self.created_by
        if self.data_access_configuration_id:
            tableInfo_body['data_access_configuration_id'] = self.data_access_configuration_id
        if self.data_source_format:
            tableInfo_body['data_source_format'] = self.data_source_format.value
        if self.full_name:
            tableInfo_body['full_name'] = self.full_name
        if self.metastore_id:
            tableInfo_body['metastore_id'] = self.metastore_id
        if self.name:
            tableInfo_body['name'] = self.name
        if self.owner:
            tableInfo_body['owner'] = self.owner
        if self.privileges:
            tableInfo_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            tableInfo_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.schema_name:
            tableInfo_body['schema_name'] = self.schema_name
        if self.sql_path:
            tableInfo_body['sql_path'] = self.sql_path
        if self.storage_credential_name:
            tableInfo_body['storage_credential_name'] = self.storage_credential_name
        if self.storage_location:
            tableInfo_body['storage_location'] = self.storage_location
        if self.table_id:
            tableInfo_body['table_id'] = self.table_id
        if self.table_type:
            tableInfo_body['table_type'] = self.table_type.value
        if self.updated_at:
            tableInfo_body['updated_at'] = self.updated_at
        if self.updated_by:
            tableInfo_body['updated_by'] = self.updated_by
        if self.view_definition:
            tableInfo_body['view_definition'] = self.view_definition
        
        return tableInfo_query, tableInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TableInfo':
        return cls(
            catalog_name=d.get('catalog_name', None),
            columns=[ColumnInfo.from_dict(v) for v in d['columns']] if 'columns' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            data_access_configuration_id=d.get('data_access_configuration_id', None),
            data_source_format=TableInfoDataSourceFormat(d['data_source_format']) if 'data_source_format' in d else None,
            full_name=d.get('full_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            schema_name=d.get('schema_name', None),
            sql_path=d.get('sql_path', None),
            storage_credential_name=d.get('storage_credential_name', None),
            storage_location=d.get('storage_location', None),
            table_id=d.get('table_id', None),
            table_type=TableInfoTableType(d['table_type']) if 'table_type' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
            view_definition=d.get('view_definition', None),
        )



class TableInfoDataSourceFormat(Enum):
    """[Create:REQ Update:OPT] Data source format ("DELTA", "CSV", etc.)."""
    
    AVRO = 'AVRO'
    CSV = 'CSV'
    DELTA = 'DELTA'
    DELTASHARING = 'DELTASHARING'
    JSON = 'JSON'
    ORC = 'ORC'
    PARQUET = 'PARQUET'
    TEXT = 'TEXT'
    UNITY_CATALOG = 'UNITY_CATALOG'
    UNKNOWN_DATA_SOURCE_FORMAT = 'UNKNOWN_DATA_SOURCE_FORMAT'

class TableInfoPrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

class TableInfoTableType(Enum):
    """[Create:REQ Update:OPT] Table type ("MANAGED", "EXTERNAL", "VIEW")."""
    
    EXTERNAL = 'EXTERNAL'
    MANAGED = 'MANAGED'
    UNKNOWN_TABLE_TYPE = 'UNKNOWN_TABLE_TYPE'
    VIEW = 'VIEW'

@dataclass
class TableSummary:
    
    # The full name of the table.
    full_name: str = None
    # One of: **UNKNOWN_TABLE_TYPE**, **MANAGED**, **EXTERNAL**, **VIEW**.
    table_type: 'TableSummaryTableType' = None

    def as_request(self) -> (dict, dict):
        tableSummary_query, tableSummary_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.full_name:
            tableSummary_body['full_name'] = self.full_name
        if self.table_type:
            tableSummary_body['table_type'] = self.table_type.value
        
        return tableSummary_query, tableSummary_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TableSummary':
        return cls(
            full_name=d.get('full_name', None),
            table_type=TableSummaryTableType(d['table_type']) if 'table_type' in d else None,
        )



class TableSummaryTableType(Enum):
    """One of: **UNKNOWN_TABLE_TYPE**, **MANAGED**, **EXTERNAL**, **VIEW**."""
    
    EXTERNAL = 'EXTERNAL'
    MANAGED = 'MANAGED'
    UNKNOWN_TABLE_TYPE = 'UNKNOWN_TABLE_TYPE'
    VIEW = 'VIEW'

@dataclass
class UpdateCatalog:
    
    # [Create,Update:IGN] The type of the catalog.
    catalog_type: 'UpdateCatalogCatalogType' = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Catalog was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Catalog creator.
    created_by: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Catalog.
    name: str = None # path
    # [Create:IGN,Update:OPT] Username of current owner of Catalog.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Catalog.
    privileges: 'List[UpdateCatalogPrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # Delta Sharing Catalog specific fields. A Delta Sharing Catalog is a
    # catalog that is based on a Delta share on a remote sharing server.
    # [Create:OPT,Update:IGN] The name of delta sharing provider.
    provider_name: str = None
    # [Create:OPT,Update: IGN] The name of the share under the share provider.
    share_name: str = None
    # [Create,Update:IGN] Time at which this Catalog was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Catalog.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        updateCatalog_query, updateCatalog_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_type:
            updateCatalog_body['catalog_type'] = self.catalog_type.value
        if self.comment:
            updateCatalog_body['comment'] = self.comment
        if self.created_at:
            updateCatalog_body['created_at'] = self.created_at
        if self.created_by:
            updateCatalog_body['created_by'] = self.created_by
        if self.metastore_id:
            updateCatalog_body['metastore_id'] = self.metastore_id
        if self.name:
            updateCatalog_body['name'] = self.name
        if self.owner:
            updateCatalog_body['owner'] = self.owner
        if self.privileges:
            updateCatalog_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            updateCatalog_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.provider_name:
            updateCatalog_body['provider_name'] = self.provider_name
        if self.share_name:
            updateCatalog_body['share_name'] = self.share_name
        if self.updated_at:
            updateCatalog_body['updated_at'] = self.updated_at
        if self.updated_by:
            updateCatalog_body['updated_by'] = self.updated_by
        
        return updateCatalog_query, updateCatalog_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateCatalog':
        return cls(
            catalog_type=UpdateCatalogCatalogType(d['catalog_type']) if 'catalog_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            provider_name=d.get('provider_name', None),
            share_name=d.get('share_name', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class UpdateCatalogCatalogType(Enum):
    """[Create,Update:IGN] The type of the catalog."""
    
    DELTASHARING_CATALOG = 'DELTASHARING_CATALOG'
    MANAGED_CATALOG = 'MANAGED_CATALOG'
    SYSTEM_CATALOG = 'SYSTEM_CATALOG'
    UNKNOWN_CATALOG_TYPE = 'UNKNOWN_CATALOG_TYPE'

class UpdateCatalogPrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class UpdateExternalLocation:
    
    # [Create:OPT Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this External Location was created, in
    # epoch milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of External Location creator.
    created_by: str = None
    # [Create,Update:IGN] Unique ID of the location's Storage Credential.
    credential_id: str = None
    # [Create:REQ Update:OPT] Current name of the Storage Credential this
    # location uses.
    credential_name: str = None
    # TODO: SC-90063 re-add 'force' parameter in backward-compatible way for DBR
    # (not removed below as it still works with CLI) Optional. Force update even
    # if changing url invalidates dependent external tables or mounts.
    force: bool = None
    # [Create,Update:IGN] Unique identifier of Metastore hosting the External
    # Location.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of the External Location.
    name: str = None # path
    # [Create:IGN Update:OPT] The owner of the External Location.
    owner: str = None
    # [Create,Update:IGN] Time at which this was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the External
    # Location.
    updated_by: str = None
    # [Create:REQ Update:OPT] Path URL of the External Location.
    url: str = None

    def as_request(self) -> (dict, dict):
        updateExternalLocation_query, updateExternalLocation_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.comment:
            updateExternalLocation_body['comment'] = self.comment
        if self.created_at:
            updateExternalLocation_body['created_at'] = self.created_at
        if self.created_by:
            updateExternalLocation_body['created_by'] = self.created_by
        if self.credential_id:
            updateExternalLocation_body['credential_id'] = self.credential_id
        if self.credential_name:
            updateExternalLocation_body['credential_name'] = self.credential_name
        if self.force:
            updateExternalLocation_body['force'] = self.force
        if self.metastore_id:
            updateExternalLocation_body['metastore_id'] = self.metastore_id
        if self.name:
            updateExternalLocation_body['name'] = self.name
        if self.owner:
            updateExternalLocation_body['owner'] = self.owner
        if self.updated_at:
            updateExternalLocation_body['updated_at'] = self.updated_at
        if self.updated_by:
            updateExternalLocation_body['updated_by'] = self.updated_by
        if self.url:
            updateExternalLocation_body['url'] = self.url
        
        return updateExternalLocation_query, updateExternalLocation_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateExternalLocation':
        return cls(
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            credential_id=d.get('credential_id', None),
            credential_name=d.get('credential_name', None),
            force=d.get('force', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
            url=d.get('url', None),
        )



@dataclass
class UpdateMetastore:
    
    # Required. Unique ID of the Metastore (from URL).
    id: str # path
    # [Create,Update:IGN] Time at which this Metastore was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Metastore creator.
    created_by: str = None
    # [Create:IGN Update:OPT] Unique identifier of (Default) Data Access
    # Configuration
    default_data_access_config_id: str = None
    # [Create:IGN Update:OPT] Whether Delta Sharing is enabled on this
    # metastore.
    delta_sharing_enabled: bool = None
    # [Create:IGN Update:OPT] The lifetime of delta sharing recipient token in
    # seconds
    delta_sharing_recipient_token_lifetime_in_seconds: int = None
    # [Create,Update:IGN] Unique identifier of Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Metastore.
    name: str = None
    # [Create:IGN Update:OPT] The owner of the metastore.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Metastore.
    privileges: 'List[UpdateMetastorePrivilegesItem]' = None
    # The region this metastore has an afinity to. This is used by
    # accounts-manager. Ignored by Unity Catalog.
    region: str = None
    # [Create:REQ Update:ERR] Storage root URL for Metastore
    storage_root: str = None
    # [Create:IGN Update:OPT] UUID of storage credential to access storage_root
    storage_root_credential_id: str = None
    # [Create,Update:IGN] Time at which the Metastore was last modified, in
    # epoch milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the Metastore.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        updateMetastore_query, updateMetastore_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.created_at:
            updateMetastore_body['created_at'] = self.created_at
        if self.created_by:
            updateMetastore_body['created_by'] = self.created_by
        if self.default_data_access_config_id:
            updateMetastore_body['default_data_access_config_id'] = self.default_data_access_config_id
        if self.delta_sharing_enabled:
            updateMetastore_body['delta_sharing_enabled'] = self.delta_sharing_enabled
        if self.delta_sharing_recipient_token_lifetime_in_seconds:
            updateMetastore_body['delta_sharing_recipient_token_lifetime_in_seconds'] = self.delta_sharing_recipient_token_lifetime_in_seconds
        if self.id:
            updateMetastore_body['id'] = self.id
        if self.metastore_id:
            updateMetastore_body['metastore_id'] = self.metastore_id
        if self.name:
            updateMetastore_body['name'] = self.name
        if self.owner:
            updateMetastore_body['owner'] = self.owner
        if self.privileges:
            updateMetastore_body['privileges'] = [v for v in self.privileges]
        if self.region:
            updateMetastore_body['region'] = self.region
        if self.storage_root:
            updateMetastore_body['storage_root'] = self.storage_root
        if self.storage_root_credential_id:
            updateMetastore_body['storage_root_credential_id'] = self.storage_root_credential_id
        if self.updated_at:
            updateMetastore_body['updated_at'] = self.updated_at
        if self.updated_by:
            updateMetastore_body['updated_by'] = self.updated_by
        
        return updateMetastore_query, updateMetastore_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateMetastore':
        return cls(
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            default_data_access_config_id=d.get('default_data_access_config_id', None),
            delta_sharing_enabled=d.get('delta_sharing_enabled', None),
            delta_sharing_recipient_token_lifetime_in_seconds=d.get('delta_sharing_recipient_token_lifetime_in_seconds', None),
            id=d.get('id', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            region=d.get('region', None),
            storage_root=d.get('storage_root', None),
            storage_root_credential_id=d.get('storage_root_credential_id', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



@dataclass
class UpdateMetastoreAssignment:
    
    # A workspace ID.
    workspace_id: int # path
    # The name of the default catalog for the Metastore.
    default_catalog_name: str = None
    # The unique ID of the Metastore.
    metastore_id: str = None

    def as_request(self) -> (dict, dict):
        updateMetastoreAssignment_query, updateMetastoreAssignment_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.default_catalog_name:
            updateMetastoreAssignment_body['default_catalog_name'] = self.default_catalog_name
        if self.metastore_id:
            updateMetastoreAssignment_body['metastore_id'] = self.metastore_id
        if self.workspace_id:
            updateMetastoreAssignment_body['workspace_id'] = self.workspace_id
        
        return updateMetastoreAssignment_query, updateMetastoreAssignment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateMetastoreAssignment':
        return cls(
            default_catalog_name=d.get('default_catalog_name', None),
            metastore_id=d.get('metastore_id', None),
            workspace_id=d.get('workspace_id', None),
        )



class UpdateMetastorePrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class UpdatePermissions:
    
    # Required. Unique identifier (full name) of Securable (from URL).
    full_name: str # path
    # Required. Type of Securable (from URL).
    securable_type: str # path
    # Array of permissions change objects.
    changes: 'List[PermissionsChange]' = None
    # Optional. List permissions granted to this principal.
    principal: str = None # query

    def as_request(self) -> (dict, dict):
        updatePermissions_query, updatePermissions_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.changes:
            updatePermissions_body['changes'] = [v.as_request()[1] for v in self.changes]
        if self.full_name:
            updatePermissions_body['full_name'] = self.full_name
        if self.principal:
            updatePermissions_query['principal'] = self.principal
        if self.securable_type:
            updatePermissions_body['securable_type'] = self.securable_type
        
        return updatePermissions_query, updatePermissions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdatePermissions':
        return cls(
            changes=[PermissionsChange.from_dict(v) for v in d['changes']] if 'changes' in d else None,
            full_name=d.get('full_name', None),
            principal=d.get('principal', None),
            securable_type=d.get('securable_type', None),
        )



@dataclass
class UpdateProvider:
    
    # [Create,Update:IGN] Whether this provider is successfully activated by the
    # data provider. This field is only present when the authentication type is
    # DATABRICKS.
    activated_by_provider: bool = None
    # [Create:REQ,Update:IGN] The delta sharing authentication type.
    authentication_type: 'UpdateProviderAuthenticationType' = None
    # [Create,Update:OPT] Description about the provider.
    comment: str = None
    # [Create,Update:IGN] Time at which this Provider was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Provider creator.
    created_by: str = None
    # [Create, Update:REQ] The name of the Provider.
    name: str = None # path
    # [Create,Update:IGN] This field is only present when the authentication
    # type is TOKEN.
    recipient_profile: 'RecipientProfile' = None
    # [Create,Update:OPT] This field is only present when the authentication
    # type is TOKEN.
    recipient_profile_str: str = None
    # [Create,Update:IGN] The server-generated one-time sharing code. This field
    # is only present when the authentication type is DATABRICKS.
    sharing_code: str = None
    # [Create,Update:IGN] Time at which this Provider was created, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Share.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        updateProvider_query, updateProvider_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activated_by_provider:
            updateProvider_body['activated_by_provider'] = self.activated_by_provider
        if self.authentication_type:
            updateProvider_body['authentication_type'] = self.authentication_type.value
        if self.comment:
            updateProvider_body['comment'] = self.comment
        if self.created_at:
            updateProvider_body['created_at'] = self.created_at
        if self.created_by:
            updateProvider_body['created_by'] = self.created_by
        if self.name:
            updateProvider_body['name'] = self.name
        if self.recipient_profile:
            updateProvider_body['recipient_profile'] = self.recipient_profile.as_request()[1]
        if self.recipient_profile_str:
            updateProvider_body['recipient_profile_str'] = self.recipient_profile_str
        if self.sharing_code:
            updateProvider_body['sharing_code'] = self.sharing_code
        if self.updated_at:
            updateProvider_body['updated_at'] = self.updated_at
        if self.updated_by:
            updateProvider_body['updated_by'] = self.updated_by
        
        return updateProvider_query, updateProvider_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateProvider':
        return cls(
            activated_by_provider=d.get('activated_by_provider', None),
            authentication_type=UpdateProviderAuthenticationType(d['authentication_type']) if 'authentication_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            name=d.get('name', None),
            recipient_profile=RecipientProfile.from_dict(d['recipient_profile']) if 'recipient_profile' in d else None,
            recipient_profile_str=d.get('recipient_profile_str', None),
            sharing_code=d.get('sharing_code', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class UpdateProviderAuthenticationType(Enum):
    """[Create:REQ,Update:IGN] The delta sharing authentication type."""
    
    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'
    UNKNOWN = 'UNKNOWN'

@dataclass
class UpdateRecipient:
    
    # [Create:IGN,Update:IGN] A boolean status field showing whether the
    # Recipient's activation URL has been exercised or not.
    activated: bool = None
    # [Create:IGN,Update:IGN] Full activation url to retrieve the access token.
    # It will be empty if the token is already retrieved.
    activation_url: str = None
    # [Create:REQ,Update:IGN] The delta sharing authentication type.
    authentication_type: 'UpdateRecipientAuthenticationType' = None
    # [Create:OPT,Update:OPT] Description about the recipient.
    comment: str = None
    # [Create:IGN,Update:IGN] Time at which this recipient was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create:IGN,Update:IGN] Username of recipient creator.
    created_by: str = None
    # [Create:OPT,Update:OPT] IP Access List
    ip_access_list: 'IpAccessList' = None
    # [Create:REQ,Update:OPT] Name of Recipient.
    name: str = None # path
    # [Create:OPT,Update:IGN] The one-time sharing code provided by the data
    # recipient. This field is only present when the authentication type is
    # DATABRICKS.
    sharing_code: str = None
    # [Create:IGN,Update:IGN] recipient Tokens This field is only present when
    # the authentication type is TOKEN.
    tokens: 'List[RecipientTokenInfo]' = None
    # [Create:IGN,Update:IGN] Time at which the recipient was updated, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create:IGN,Update:IGN] Username of recipient updater.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        updateRecipient_query, updateRecipient_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activated:
            updateRecipient_body['activated'] = self.activated
        if self.activation_url:
            updateRecipient_body['activation_url'] = self.activation_url
        if self.authentication_type:
            updateRecipient_body['authentication_type'] = self.authentication_type.value
        if self.comment:
            updateRecipient_body['comment'] = self.comment
        if self.created_at:
            updateRecipient_body['created_at'] = self.created_at
        if self.created_by:
            updateRecipient_body['created_by'] = self.created_by
        if self.ip_access_list:
            updateRecipient_body['ip_access_list'] = self.ip_access_list.as_request()[1]
        if self.name:
            updateRecipient_body['name'] = self.name
        if self.sharing_code:
            updateRecipient_body['sharing_code'] = self.sharing_code
        if self.tokens:
            updateRecipient_body['tokens'] = [v.as_request()[1] for v in self.tokens]
        if self.updated_at:
            updateRecipient_body['updated_at'] = self.updated_at
        if self.updated_by:
            updateRecipient_body['updated_by'] = self.updated_by
        
        return updateRecipient_query, updateRecipient_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateRecipient':
        return cls(
            activated=d.get('activated', None),
            activation_url=d.get('activation_url', None),
            authentication_type=UpdateRecipientAuthenticationType(d['authentication_type']) if 'authentication_type' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            ip_access_list=IpAccessList.from_dict(d['ip_access_list']) if 'ip_access_list' in d else None,
            name=d.get('name', None),
            sharing_code=d.get('sharing_code', None),
            tokens=[RecipientTokenInfo.from_dict(v) for v in d['tokens']] if 'tokens' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class UpdateRecipientAuthenticationType(Enum):
    """[Create:REQ,Update:IGN] The delta sharing authentication type."""
    
    DATABRICKS = 'DATABRICKS'
    TOKEN = 'TOKEN'
    UNKNOWN = 'UNKNOWN'

@dataclass
class UpdateSchema:
    
    # [Create:REQ Update:IGN] Name of parent Catalog.
    catalog_name: str = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Schema was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Schema creator.
    created_by: str = None
    # [Create,Update:IGN] Full name of Schema, in form of
    # <catalog_name>.<schema_name>.
    full_name: str = None # path
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Schema, relative to parent Catalog.
    name: str = None
    # [Create:IGN Update:OPT] Username of current owner of Schema.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Schema.
    privileges: 'List[UpdateSchemaPrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # [Create,Update:IGN] Time at which this Schema was created, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified Schema.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        updateSchema_query, updateSchema_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            updateSchema_body['catalog_name'] = self.catalog_name
        if self.comment:
            updateSchema_body['comment'] = self.comment
        if self.created_at:
            updateSchema_body['created_at'] = self.created_at
        if self.created_by:
            updateSchema_body['created_by'] = self.created_by
        if self.full_name:
            updateSchema_body['full_name'] = self.full_name
        if self.metastore_id:
            updateSchema_body['metastore_id'] = self.metastore_id
        if self.name:
            updateSchema_body['name'] = self.name
        if self.owner:
            updateSchema_body['owner'] = self.owner
        if self.privileges:
            updateSchema_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            updateSchema_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.updated_at:
            updateSchema_body['updated_at'] = self.updated_at
        if self.updated_by:
            updateSchema_body['updated_by'] = self.updated_by
        
        return updateSchema_query, updateSchema_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateSchema':
        return cls(
            catalog_name=d.get('catalog_name', None),
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            full_name=d.get('full_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



class UpdateSchemaPrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

@dataclass
class UpdateShare:
    
    # The name of the share.
    name: str # path
    # Array of shared data object updates.
    updates: 'List[SharedDataObjectUpdate]' = None

    def as_request(self) -> (dict, dict):
        updateShare_query, updateShare_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            updateShare_body['name'] = self.name
        if self.updates:
            updateShare_body['updates'] = [v.as_request()[1] for v in self.updates]
        
        return updateShare_query, updateShare_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateShare':
        return cls(
            name=d.get('name', None),
            updates=[SharedDataObjectUpdate.from_dict(v) for v in d['updates']] if 'updates' in d else None,
        )



@dataclass
class UpdateSharePermissions:
    
    # Required. The name of the share.
    name: str # path
    # Array of permission changes.
    changes: 'List[PermissionsChange]' = None

    def as_request(self) -> (dict, dict):
        updateSharePermissions_query, updateSharePermissions_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.changes:
            updateSharePermissions_body['changes'] = [v.as_request()[1] for v in self.changes]
        if self.name:
            updateSharePermissions_body['name'] = self.name
        
        return updateSharePermissions_query, updateSharePermissions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateSharePermissions':
        return cls(
            changes=[PermissionsChange.from_dict(v) for v in d['changes']] if 'changes' in d else None,
            name=d.get('name', None),
        )



@dataclass
class UpdateStorageCredential:
    
    # The AWS IAM role configuration.
    aws_iam_role: 'AwsIamRole' = None
    # The Azure service principal configuration.
    azure_service_principal: 'AzureServicePrincipal' = None
    # [Create,Update:OPT] Comment associated with the credential.
    comment: str = None
    # [Create,Update:IGN] Time at which this Credential was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of credential creator.
    created_by: str = None
    # The GCP service account key configuration.
    gcp_service_account_key: 'GcpServiceAccountKey' = None
    # [Create:IGN] The unique identifier of the credential.
    id: str = None
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ, Update:OPT] The credential name. The name MUST be unique
    # within the Metastore.
    name: str = None # path
    # [Create:IGN Update:OPT] Username of current owner of credential.
    owner: str = None
    # Optional. Supplying true to this argument skips validation of the updated
    # set of credentials.
    skip_validation: bool = None
    # [Create,Update:IGN] Time at which this credential was last modified, in
    # epoch milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the credential.
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        updateStorageCredential_query, updateStorageCredential_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.aws_iam_role:
            updateStorageCredential_body['aws_iam_role'] = self.aws_iam_role.as_request()[1]
        if self.azure_service_principal:
            updateStorageCredential_body['azure_service_principal'] = self.azure_service_principal.as_request()[1]
        if self.comment:
            updateStorageCredential_body['comment'] = self.comment
        if self.created_at:
            updateStorageCredential_body['created_at'] = self.created_at
        if self.created_by:
            updateStorageCredential_body['created_by'] = self.created_by
        if self.gcp_service_account_key:
            updateStorageCredential_body['gcp_service_account_key'] = self.gcp_service_account_key.as_request()[1]
        if self.id:
            updateStorageCredential_body['id'] = self.id
        if self.metastore_id:
            updateStorageCredential_body['metastore_id'] = self.metastore_id
        if self.name:
            updateStorageCredential_body['name'] = self.name
        if self.owner:
            updateStorageCredential_body['owner'] = self.owner
        if self.skip_validation:
            updateStorageCredential_body['skip_validation'] = self.skip_validation
        if self.updated_at:
            updateStorageCredential_body['updated_at'] = self.updated_at
        if self.updated_by:
            updateStorageCredential_body['updated_by'] = self.updated_by
        
        return updateStorageCredential_query, updateStorageCredential_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateStorageCredential':
        return cls(
            aws_iam_role=AwsIamRole.from_dict(d['aws_iam_role']) if 'aws_iam_role' in d else None,
            azure_service_principal=AzureServicePrincipal.from_dict(d['azure_service_principal']) if 'azure_service_principal' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            gcp_service_account_key=GcpServiceAccountKey.from_dict(d['gcp_service_account_key']) if 'gcp_service_account_key' in d else None,
            id=d.get('id', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            skip_validation=d.get('skip_validation', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



@dataclass
class UpdateTable:
    
    # [Create:REQ Update:IGN] Name of parent Catalog.
    catalog_name: str = None
    # This name ('columns') is what the client actually sees as the field name
    # in messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    columns: 'List[ColumnInfo]' = None
    # [Create,Update:OPT] User-provided free-form text description.
    comment: str = None
    # [Create,Update:IGN] Time at which this Table was created, in epoch
    # milliseconds.
    created_at: int = None
    # [Create,Update:IGN] Username of Table creator.
    created_by: str = None
    # [Create,Update:IGN] Unique ID of the data_access_configuration to use.
    data_access_configuration_id: str = None
    # [Create:REQ Update:OPT] Data source format ("DELTA", "CSV", etc.).
    data_source_format: 'UpdateTableDataSourceFormat' = None
    # [Create,Update:IGN] Full name of Table, in form of
    # <catalog_name>.<schema_name>.<table_name>
    full_name: str = None # path
    # [Create,Update:IGN] Unique identifier of parent Metastore.
    metastore_id: str = None
    # [Create:REQ Update:OPT] Name of Table, relative to parent Schema.
    name: str = None
    # [Create: IGN Update:OPT] Username of current owner of Table.
    owner: str = None
    # [Create,Update:IGN] Privileges the user has on the Table.
    privileges: 'List[UpdateTablePrivilegesItem]' = None
    # This name ('properties') is what the client sees as the field name in
    # messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    properties: 'List[StringKeyValuePair]' = None
    # [Create:REQ Update:IGN] Name of parent Schema relative to its parent
    # Catalog.
    schema_name: str = None
    # [Create,Update:OPT] List of schemes whose objects can be referenced
    # without qualification.
    sql_path: str = None
    # [Create:OPT Update:IGN] Name of the storage credential this table used
    storage_credential_name: str = None
    # [Create:REQ Update:OPT] Storage root URL for table (for MANAGED, EXTERNAL
    # tables)
    storage_location: str = None
    # [Create:IGN Update:IGN] Name of Table, relative to parent Schema.
    table_id: str = None
    # [Create:REQ Update:OPT] Table type ("MANAGED", "EXTERNAL", "VIEW").
    table_type: 'UpdateTableTableType' = None
    # [Create,Update:IGN] Time at which this Table was last modified, in epoch
    # milliseconds.
    updated_at: int = None
    # [Create,Update:IGN] Username of user who last modified the Table.
    updated_by: str = None
    # [Create,Update:OPT] View definition SQL (when table_type == "VIEW")
    view_definition: str = None

    def as_request(self) -> (dict, dict):
        updateTable_query, updateTable_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            updateTable_body['catalog_name'] = self.catalog_name
        if self.columns:
            updateTable_body['columns'] = [v.as_request()[1] for v in self.columns]
        if self.comment:
            updateTable_body['comment'] = self.comment
        if self.created_at:
            updateTable_body['created_at'] = self.created_at
        if self.created_by:
            updateTable_body['created_by'] = self.created_by
        if self.data_access_configuration_id:
            updateTable_body['data_access_configuration_id'] = self.data_access_configuration_id
        if self.data_source_format:
            updateTable_body['data_source_format'] = self.data_source_format.value
        if self.full_name:
            updateTable_body['full_name'] = self.full_name
        if self.metastore_id:
            updateTable_body['metastore_id'] = self.metastore_id
        if self.name:
            updateTable_body['name'] = self.name
        if self.owner:
            updateTable_body['owner'] = self.owner
        if self.privileges:
            updateTable_body['privileges'] = [v for v in self.privileges]
        if self.properties:
            updateTable_body['properties'] = [v.as_request()[1] for v in self.properties]
        if self.schema_name:
            updateTable_body['schema_name'] = self.schema_name
        if self.sql_path:
            updateTable_body['sql_path'] = self.sql_path
        if self.storage_credential_name:
            updateTable_body['storage_credential_name'] = self.storage_credential_name
        if self.storage_location:
            updateTable_body['storage_location'] = self.storage_location
        if self.table_id:
            updateTable_body['table_id'] = self.table_id
        if self.table_type:
            updateTable_body['table_type'] = self.table_type.value
        if self.updated_at:
            updateTable_body['updated_at'] = self.updated_at
        if self.updated_by:
            updateTable_body['updated_by'] = self.updated_by
        if self.view_definition:
            updateTable_body['view_definition'] = self.view_definition
        
        return updateTable_query, updateTable_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateTable':
        return cls(
            catalog_name=d.get('catalog_name', None),
            columns=[ColumnInfo.from_dict(v) for v in d['columns']] if 'columns' in d else None,
            comment=d.get('comment', None),
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            data_access_configuration_id=d.get('data_access_configuration_id', None),
            data_source_format=UpdateTableDataSourceFormat(d['data_source_format']) if 'data_source_format' in d else None,
            full_name=d.get('full_name', None),
            metastore_id=d.get('metastore_id', None),
            name=d.get('name', None),
            owner=d.get('owner', None),
            privileges=d.get('privileges', None),
            properties=[StringKeyValuePair.from_dict(v) for v in d['properties']] if 'properties' in d else None,
            schema_name=d.get('schema_name', None),
            sql_path=d.get('sql_path', None),
            storage_credential_name=d.get('storage_credential_name', None),
            storage_location=d.get('storage_location', None),
            table_id=d.get('table_id', None),
            table_type=UpdateTableTableType(d['table_type']) if 'table_type' in d else None,
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
            view_definition=d.get('view_definition', None),
        )



class UpdateTableDataSourceFormat(Enum):
    """[Create:REQ Update:OPT] Data source format ("DELTA", "CSV", etc.)."""
    
    AVRO = 'AVRO'
    CSV = 'CSV'
    DELTA = 'DELTA'
    DELTASHARING = 'DELTASHARING'
    JSON = 'JSON'
    ORC = 'ORC'
    PARQUET = 'PARQUET'
    TEXT = 'TEXT'
    UNITY_CATALOG = 'UNITY_CATALOG'
    UNKNOWN_DATA_SOURCE_FORMAT = 'UNKNOWN_DATA_SOURCE_FORMAT'

class UpdateTablePrivilegesItem(Enum):
    
    
    CREATE = 'CREATE'
    CREATE_MOUNT = 'CREATE_MOUNT'
    CREATE_TABLE = 'CREATE_TABLE'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    SELECT = 'SELECT'
    UNKNOWN_PRIVILEGE = 'UNKNOWN_PRIVILEGE'
    USAGE = 'USAGE'
    WRITE_FILES = 'WRITE_FILES'

class UpdateTableTableType(Enum):
    """[Create:REQ Update:OPT] Table type ("MANAGED", "EXTERNAL", "VIEW")."""
    
    EXTERNAL = 'EXTERNAL'
    MANAGED = 'MANAGED'
    UNKNOWN_TABLE_TYPE = 'UNKNOWN_TABLE_TYPE'
    VIEW = 'VIEW'

@dataclass
class DeleteCatalogRequest:
    
    # Required. The name of the catalog.
    name: str # path

    def as_request(self) -> (dict, dict):
        deleteCatalogRequest_query, deleteCatalogRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            deleteCatalogRequest_body['name'] = self.name
        
        return deleteCatalogRequest_query, deleteCatalogRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteCatalogRequest':
        return cls(
            name=d.get('name', None),
        )



@dataclass
class DeleteExternalLocationRequest:
    
    # Required. Name of the storage credential.
    name: str # path
    # Force deletion even if there are dependent external tables or mounts.
    force: bool = None # query

    def as_request(self) -> (dict, dict):
        deleteExternalLocationRequest_query, deleteExternalLocationRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.force:
            deleteExternalLocationRequest_query['force'] = self.force
        if self.name:
            deleteExternalLocationRequest_body['name'] = self.name
        
        return deleteExternalLocationRequest_query, deleteExternalLocationRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteExternalLocationRequest':
        return cls(
            force=d.get('force', None),
            name=d.get('name', None),
        )



@dataclass
class DeleteMetastoreAssignmentRequest:
    
    # Query for the ID of the Metastore to delete.
    metastore_id: str # query
    # A workspace ID.
    workspace_id: int # path

    def as_request(self) -> (dict, dict):
        deleteMetastoreAssignmentRequest_query, deleteMetastoreAssignmentRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.metastore_id:
            deleteMetastoreAssignmentRequest_query['metastore_id'] = self.metastore_id
        if self.workspace_id:
            deleteMetastoreAssignmentRequest_body['workspace_id'] = self.workspace_id
        
        return deleteMetastoreAssignmentRequest_query, deleteMetastoreAssignmentRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteMetastoreAssignmentRequest':
        return cls(
            metastore_id=d.get('metastore_id', None),
            workspace_id=d.get('workspace_id', None),
        )



@dataclass
class DeleteMetastoreRequest:
    
    # Required. Unique ID of the Metastore (from URL).
    id: str # path
    # Force deletion even if the metastore is not empty. Default is false.
    force: bool = None # query

    def as_request(self) -> (dict, dict):
        deleteMetastoreRequest_query, deleteMetastoreRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.force:
            deleteMetastoreRequest_query['force'] = self.force
        if self.id:
            deleteMetastoreRequest_body['id'] = self.id
        
        return deleteMetastoreRequest_query, deleteMetastoreRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteMetastoreRequest':
        return cls(
            force=d.get('force', None),
            id=d.get('id', None),
        )



@dataclass
class DeleteProviderRequest:
    
    # Required. Name of the provider.
    name: str # path

    def as_request(self) -> (dict, dict):
        deleteProviderRequest_query, deleteProviderRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            deleteProviderRequest_body['name'] = self.name
        
        return deleteProviderRequest_query, deleteProviderRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteProviderRequest':
        return cls(
            name=d.get('name', None),
        )



@dataclass
class DeleteRecipientRequest:
    
    # Required. Name of the recipient.
    name: str # path

    def as_request(self) -> (dict, dict):
        deleteRecipientRequest_query, deleteRecipientRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            deleteRecipientRequest_body['name'] = self.name
        
        return deleteRecipientRequest_query, deleteRecipientRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteRecipientRequest':
        return cls(
            name=d.get('name', None),
        )



@dataclass
class DeleteSchemaRequest:
    
    # Required. Full name of the schema (from URL).
    full_name: str # path

    def as_request(self) -> (dict, dict):
        deleteSchemaRequest_query, deleteSchemaRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.full_name:
            deleteSchemaRequest_body['full_name'] = self.full_name
        
        return deleteSchemaRequest_query, deleteSchemaRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteSchemaRequest':
        return cls(
            full_name=d.get('full_name', None),
        )



@dataclass
class DeleteShareRequest:
    
    # The name of the share.
    name: str # path

    def as_request(self) -> (dict, dict):
        deleteShareRequest_query, deleteShareRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            deleteShareRequest_body['name'] = self.name
        
        return deleteShareRequest_query, deleteShareRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteShareRequest':
        return cls(
            name=d.get('name', None),
        )



@dataclass
class DeleteStorageCredentialRequest:
    
    # Required. Name of the storage credential.
    name: str # path
    # Force deletion even if there are dependent external locations or external
    # tables.
    force: bool = None # query

    def as_request(self) -> (dict, dict):
        deleteStorageCredentialRequest_query, deleteStorageCredentialRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.force:
            deleteStorageCredentialRequest_query['force'] = self.force
        if self.name:
            deleteStorageCredentialRequest_body['name'] = self.name
        
        return deleteStorageCredentialRequest_query, deleteStorageCredentialRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteStorageCredentialRequest':
        return cls(
            force=d.get('force', None),
            name=d.get('name', None),
        )



@dataclass
class DeleteTableRequest:
    
    # Required. Full name of the Table (from URL).
    full_name: str # path

    def as_request(self) -> (dict, dict):
        deleteTableRequest_query, deleteTableRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.full_name:
            deleteTableRequest_body['full_name'] = self.full_name
        
        return deleteTableRequest_query, deleteTableRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteTableRequest':
        return cls(
            full_name=d.get('full_name', None),
        )



@dataclass
class GetActivationUrlInfoRequest:
    
    # Required. The one time activation url. It also accepts activation token.
    activation_url: str # path

    def as_request(self) -> (dict, dict):
        getActivationUrlInfoRequest_query, getActivationUrlInfoRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activation_url:
            getActivationUrlInfoRequest_body['activation_url'] = self.activation_url
        
        return getActivationUrlInfoRequest_query, getActivationUrlInfoRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetActivationUrlInfoRequest':
        return cls(
            activation_url=d.get('activation_url', None),
        )



@dataclass
class GetCatalogRequest:
    
    # Required. The name of the catalog.
    name: str # path

    def as_request(self) -> (dict, dict):
        getCatalogRequest_query, getCatalogRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            getCatalogRequest_body['name'] = self.name
        
        return getCatalogRequest_query, getCatalogRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetCatalogRequest':
        return cls(
            name=d.get('name', None),
        )



@dataclass
class GetExternalLocationRequest:
    
    # Required. Name of the storage credential.
    name: str # path

    def as_request(self) -> (dict, dict):
        getExternalLocationRequest_query, getExternalLocationRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            getExternalLocationRequest_body['name'] = self.name
        
        return getExternalLocationRequest_query, getExternalLocationRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetExternalLocationRequest':
        return cls(
            name=d.get('name', None),
        )



@dataclass
class GetMetastoreRequest:
    
    # Required. Unique ID of the Metastore (from URL).
    id: str # path

    def as_request(self) -> (dict, dict):
        getMetastoreRequest_query, getMetastoreRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            getMetastoreRequest_body['id'] = self.id
        
        return getMetastoreRequest_query, getMetastoreRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetMetastoreRequest':
        return cls(
            id=d.get('id', None),
        )



@dataclass
class GetPermissionsRequest:
    
    # Required. Unique identifier (full name) of Securable (from URL).
    full_name: str # path
    # Required. Type of Securable (from URL).
    securable_type: str # path
    # Optional. List permissions granted to this principal.
    principal: str = None # query

    def as_request(self) -> (dict, dict):
        getPermissionsRequest_query, getPermissionsRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.full_name:
            getPermissionsRequest_body['full_name'] = self.full_name
        if self.principal:
            getPermissionsRequest_query['principal'] = self.principal
        if self.securable_type:
            getPermissionsRequest_body['securable_type'] = self.securable_type
        
        return getPermissionsRequest_query, getPermissionsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPermissionsRequest':
        return cls(
            full_name=d.get('full_name', None),
            principal=d.get('principal', None),
            securable_type=d.get('securable_type', None),
        )



@dataclass
class GetProviderRequest:
    
    # Required. Name of the provider.
    name: str # path

    def as_request(self) -> (dict, dict):
        getProviderRequest_query, getProviderRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            getProviderRequest_body['name'] = self.name
        
        return getProviderRequest_query, getProviderRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetProviderRequest':
        return cls(
            name=d.get('name', None),
        )



@dataclass
class GetRecipientRequest:
    
    # Required. Name of the recipient.
    name: str # path

    def as_request(self) -> (dict, dict):
        getRecipientRequest_query, getRecipientRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            getRecipientRequest_body['name'] = self.name
        
        return getRecipientRequest_query, getRecipientRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRecipientRequest':
        return cls(
            name=d.get('name', None),
        )



@dataclass
class GetRecipientSharePermissionsRequest:
    
    # Required. The name of the Recipient.
    name: str # path

    def as_request(self) -> (dict, dict):
        getRecipientSharePermissionsRequest_query, getRecipientSharePermissionsRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            getRecipientSharePermissionsRequest_body['name'] = self.name
        
        return getRecipientSharePermissionsRequest_query, getRecipientSharePermissionsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRecipientSharePermissionsRequest':
        return cls(
            name=d.get('name', None),
        )



@dataclass
class GetSchemaRequest:
    
    # Required. Full name of the schema (from URL).
    full_name: str # path

    def as_request(self) -> (dict, dict):
        getSchemaRequest_query, getSchemaRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.full_name:
            getSchemaRequest_body['full_name'] = self.full_name
        
        return getSchemaRequest_query, getSchemaRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetSchemaRequest':
        return cls(
            full_name=d.get('full_name', None),
        )



@dataclass
class GetSharePermissionsRequest:
    
    # Required. The name of the share.
    name: str # path

    def as_request(self) -> (dict, dict):
        getSharePermissionsRequest_query, getSharePermissionsRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            getSharePermissionsRequest_body['name'] = self.name
        
        return getSharePermissionsRequest_query, getSharePermissionsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetSharePermissionsRequest':
        return cls(
            name=d.get('name', None),
        )



@dataclass
class GetShareRequest:
    
    # The name of the share.
    name: str # path
    # Query for data to include in the share.
    include_shared_data: bool = None # query

    def as_request(self) -> (dict, dict):
        getShareRequest_query, getShareRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.include_shared_data:
            getShareRequest_query['include_shared_data'] = self.include_shared_data
        if self.name:
            getShareRequest_body['name'] = self.name
        
        return getShareRequest_query, getShareRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetShareRequest':
        return cls(
            include_shared_data=d.get('include_shared_data', None),
            name=d.get('name', None),
        )



@dataclass
class GetStorageCredentialsRequest:
    
    # Required. Name of the storage credential.
    name: str # path

    def as_request(self) -> (dict, dict):
        getStorageCredentialsRequest_query, getStorageCredentialsRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            getStorageCredentialsRequest_body['name'] = self.name
        
        return getStorageCredentialsRequest_query, getStorageCredentialsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetStorageCredentialsRequest':
        return cls(
            name=d.get('name', None),
        )



@dataclass
class GetTableRequest:
    
    # Required. Full name of the Table (from URL).
    full_name: str # path

    def as_request(self) -> (dict, dict):
        getTableRequest_query, getTableRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.full_name:
            getTableRequest_body['full_name'] = self.full_name
        
        return getTableRequest_query, getTableRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetTableRequest':
        return cls(
            full_name=d.get('full_name', None),
        )



@dataclass
class ListRequest:
    
    # Optional. Parent catalog for schemas of interest.
    catalog_name: str = None # query

    def as_request(self) -> (dict, dict):
        listRequest_query, listRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            listRequest_query['catalog_name'] = self.catalog_name
        
        return listRequest_query, listRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRequest':
        return cls(
            catalog_name=d.get('catalog_name', None),
        )



@dataclass
class ListSharesRequest:
    
    # Required. Name of the provider in which to list shares.
    name: str # path

    def as_request(self) -> (dict, dict):
        listSharesRequest_query, listSharesRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            listSharesRequest_body['name'] = self.name
        
        return listSharesRequest_query, listSharesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListSharesRequest':
        return cls(
            name=d.get('name', None),
        )



@dataclass
class ListTableSummariesRequest:
    
    # Required. Name of parent catalog for tables of interest.
    catalog_name: str = None # query
    # Optional. Maximum number of tables to return (page length). Defaults to
    # 10000.
    max_results: int = None # query
    # Optional. Opaque token to send for the next page of results (pagination).
    page_token: str = None # query
    # Optional. A sql LIKE pattern (% and _) for schema names. All schemas will
    # be returned if not set or empty.
    schema_name_pattern: str = None # query
    # Optional. A sql LIKE pattern (% and _) for table names. All tables will be
    # returned if not set or empty.
    table_name_pattern: str = None # query

    def as_request(self) -> (dict, dict):
        listTableSummariesRequest_query, listTableSummariesRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.catalog_name:
            listTableSummariesRequest_query['catalog_name'] = self.catalog_name
        if self.max_results:
            listTableSummariesRequest_query['max_results'] = self.max_results
        if self.page_token:
            listTableSummariesRequest_query['page_token'] = self.page_token
        if self.schema_name_pattern:
            listTableSummariesRequest_query['schema_name_pattern'] = self.schema_name_pattern
        if self.table_name_pattern:
            listTableSummariesRequest_query['table_name_pattern'] = self.table_name_pattern
        
        return listTableSummariesRequest_query, listTableSummariesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListTableSummariesRequest':
        return cls(
            catalog_name=d.get('catalog_name', None),
            max_results=d.get('max_results', None),
            page_token=d.get('page_token', None),
            schema_name_pattern=d.get('schema_name_pattern', None),
            table_name_pattern=d.get('table_name_pattern', None),
        )



@dataclass
class RetrieveTokenRequest:
    
    # Required. The one time activation url. It also accepts activation token.
    activation_url: str # path

    def as_request(self) -> (dict, dict):
        retrieveTokenRequest_query, retrieveTokenRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.activation_url:
            retrieveTokenRequest_body['activation_url'] = self.activation_url
        
        return retrieveTokenRequest_query, retrieveTokenRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RetrieveTokenRequest':
        return cls(
            activation_url=d.get('activation_url', None),
        )



class CatalogsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def create(self, request: CreateCatalog) -> CreateCatalogResponse:
        """Create a catalog
        
        Creates a new catalog instance in the parent Metastore if the caller is
        a Metastore admin or has the CREATE CATALOG privilege."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/unity-catalog/catalogs', query=query, body=body)
        return CreateCatalogResponse.from_dict(json)
    
    def deleteCatalog(self, request: DeleteCatalogRequest):
        """Delete a catalog
        
        Deletes the catalog that matches the supplied name. The caller must be a
        Metastore admin or the owner of the catalog."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.1/unity-catalog/catalogs/{request.name}', query=query, body=body)
        
    
    def getCatalog(self, request: GetCatalogRequest) -> GetCatalogResponse:
        """Get a catalog
        
        Gets an array of all catalogs in the current Metastore for which the
        user is an admin or Catalog owner, or has the USAGE privilege set for
        their account."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/catalogs/{request.name}', query=query, body=body)
        return GetCatalogResponse.from_dict(json)
    
    def list(self) -> ListCatalogsResponse:
        """List catalogs
        
        Gets an array of External Locations (ExternalLocationInfo objects) from
        the Metastore. The caller must be a Metastore admin, is the owner of the
        External Location, or has privileges to access the External Location."""
        
        json = self._api.do('GET', '/api/2.1/unity-catalog/catalogs')
        return ListCatalogsResponse.from_dict(json)
    
    def update(self, request: UpdateCatalog):
        """Update a catalog
        
        Updates the catalog that matches the supplied name. The caller must be
        either the owner of the catalog, or a Metastore admin (when changing the
        owner field of the catalog)."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/catalogs/{request.name}', query=query, body=body)
        
    
class ExternalLocationsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def create(self, request: CreateExternalLocation) -> CreateExternalLocationResponse:
        """Create an external location
        
        Creates a new External Location entry in the Metastore. The caller must
        be a Metastore admin or have the CREATE EXTERNAL LOCATION privilege on
        the Metastore."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/unity-catalog/external-locations', query=query, body=body)
        return CreateExternalLocationResponse.from_dict(json)
    
    def deleteExternalLocation(self, request: DeleteExternalLocationRequest):
        """Delete an external location
        
        Deletes the specified external location from the Metastore. The caller
        must be the owner of the external location."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.1/unity-catalog/external-locations/{request.name}', query=query, body=body)
        
    
    def getExternalLocation(self, request: GetExternalLocationRequest) -> GetExternalLocationResponse:
        """Get an external location
        
        Gets an external location from the Metastore. The caller must be either
        a Metastore admin, the owner of the external location, or has an
        appropriate privilege level on the Metastore."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/external-locations/{request.name}', query=query, body=body)
        return GetExternalLocationResponse.from_dict(json)
    
    def list(self) -> ListExternalLocationsResponse:
        """List external locations
        
        Gets an array of External Locations (ExternalLocationInfo objects) from
        the Metastore. The caller must be a Metastore admin, is the owner of the
        external location, or has privileges to access the external location."""
        
        json = self._api.do('GET', '/api/2.1/unity-catalog/external-locations')
        return ListExternalLocationsResponse.from_dict(json)
    
    def update(self, request: UpdateExternalLocation):
        """Update an external location
        
        Updates an external location in the Metastore. The caller must be the
        owner of the externa location, or be a Metastore admin. In the second
        case, the admin can only update the name of the external location."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/external-locations/{request.name}', query=query, body=body)
        
    
class GrantsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def updatePermissions(self, request: UpdatePermissions):
        """Update permissions
        
        Updates the permissions for a Securable type."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/permissions/{request.securable_type}/{request.full_name}', query=query, body=body)
        
    
    def getPermissions(self, request: GetPermissionsRequest) -> GetPermissionsResponse:
        """Get permissions
        
        Gets the permissions for a Securable type."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/permissions/{request.securable_type}/{request.full_name}', query=query, body=body)
        return GetPermissionsResponse.from_dict(json)
    
class MetastoresAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def create(self, request: CreateMetastore) -> CreateMetastoreResponse:
        """Create a Metastore
        
        Creates a new Metastore based on a provided name and storage root path."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/unity-catalog/metastores', query=query, body=body)
        return CreateMetastoreResponse.from_dict(json)
    
    def createMetastoreAssignment(self, request: CreateMetastoreAssignment):
        """Create an assignment
        
        Creates a new Metastore assignment. If an assignment for the same
        __workspace_id__ exists, it will be overwritten by the new
        __metastore_id__ and __default_catalog_name__. The caller must be an
        account admin."""
        query, body = request.as_request()
        self._api.do('PUT', f'/api/2.1/unity-catalog/workspaces/{request.workspace_id}/metastore', query=query, body=body)
        
    
    def deleteMetastore(self, request: DeleteMetastoreRequest):
        """Delete a Metastore
        
        Deletes a Metastore. The caller must be a Metastore admin."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.1/unity-catalog/metastores/{request.id}', query=query, body=body)
        
    
    def deleteMetastoreAssignment(self, request: DeleteMetastoreAssignmentRequest):
        """Delete an assignment
        
        Deletes a Metastore assignment. The caller must be an account
        administrator."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.1/unity-catalog/workspaces/{request.workspace_id}/metastore', query=query, body=body)
        
    
    def getMetastore(self, request: GetMetastoreRequest) -> GetMetastoreResponse:
        """Get a Metastore
        
        Gets a Metastore that matches the supplied ID. The caller must be a
        Metastore admin to retrieve this info."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/metastores/{request.id}', query=query, body=body)
        return GetMetastoreResponse.from_dict(json)
    
    def getMetastoreSummary(self) -> GetMetastoreSummaryResponse:
        """Get a summary
        
        Gets information about a Metastore. This summary includes the storage
        credential, the cloud vendor, the cloud region, and the global Metastore
        ID."""
        
        json = self._api.do('GET', '/api/2.1/unity-catalog/metastore_summary')
        return GetMetastoreSummaryResponse.from_dict(json)
    
    def list(self) -> ListMetastoresResponse:
        """List Metastores
        
        Gets an array of the available Metastores (as MetastoreInfo objects).
        The caller must be an admin to retrieve this info."""
        
        json = self._api.do('GET', '/api/2.1/unity-catalog/metastores')
        return ListMetastoresResponse.from_dict(json)
    
    def update(self, request: UpdateMetastore):
        """Update a Metastore
        
        Updates information for a specific Metastore. The caller must be a
        Metastore admin."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/metastores/{request.id}', query=query, body=body)
        
    
    def updateMetastoreAssignment(self, request: UpdateMetastoreAssignment):
        """Update an assignment
        
        Updates a Metastore assignment. This operation can be used to update
        __metastore_id__ or __default_catalog_name__ for a specified Workspace,
        if the Workspace is already assigned a Metastore. The caller must be an
        account admin to update __metastore_id__; otherwise, the caller can be a
        Workspace admin."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/workspaces/{request.workspace_id}/metastore', query=query, body=body)
        
    
class ProvidersAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def create(self, request: CreateProvider) -> CreateProviderResponse:
        """Create an auth provider
        
        Creates a new authentication provider minimally based on a name and
        authentication type. The caller must be an admin on the Metastore."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/unity-catalog/providers', query=query, body=body)
        return CreateProviderResponse.from_dict(json)
    
    def deleteProvider(self, request: DeleteProviderRequest):
        """Delete a provider
        
        Deletes an authentication provider, if the caller is a Metastore admin
        or is the owner of the provider."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.1/unity-catalog/providers/{request.name}', query=query, body=body)
        
    
    def getProvider(self, request: GetProviderRequest) -> GetProviderResponse:
        """Get a provider
        
        Gets a specific authentication provider. The caller must supply the name
        of the provider, and must either be a Metastore admin or the owner of
        the provider."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/providers/{request.name}', query=query, body=body)
        return GetProviderResponse.from_dict(json)
    
    def list(self) -> ListProvidersResponse:
        """List providers
        
        Gets an array of available authentication providers. The caller must
        either be a Metastore admin or the owner of the providers. Providers not
        owned by the caller are not included in the response."""
        
        json = self._api.do('GET', '/api/2.1/unity-catalog/providers')
        return ListProvidersResponse.from_dict(json)
    
    def listShares(self, request: ListSharesRequest) -> ListProviderSharesResponse:
        """List shares
        
        Gets an array of all shares within the Metastore where:
        
        * the caller is a Metastore admin, or * the caller is the owner."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/providers/{request.name}/shares', query=query, body=body)
        return ListProviderSharesResponse.from_dict(json)
    
    def update(self, request: UpdateProvider):
        """Update a provider
        
        Updates the information for an authentication provider, if the caller is
        a Metastore admin or is the owner of the provider. If the update changes
        the provider name, the caller must be both a Metastore admin and the
        owner of the provider."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/providers/{request.name}', query=query, body=body)
        
    
class RecipientActivationAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def getActivationUrlInfo(self, request: GetActivationUrlInfoRequest):
        """Get a share activation URL
        
        Gets information about an Activation URL."""
        query, body = request.as_request()
        self._api.do('GET', f'/api/2.1/unity-catalog/public/data_sharing_activation_info/{request.activation_url}', query=query, body=body)
        
    
    def retrieveToken(self, request: RetrieveTokenRequest) -> RetrieveTokenResponse:
        """Get an access token
        
        RPC to retrieve access token with an activation token. This is a public
        API without any authentication."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/public/data_sharing_activation/{request.activation_url}', query=query, body=body)
        return RetrieveTokenResponse.from_dict(json)
    
class RecipientsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def create(self, request: CreateRecipient) -> CreateRecipientResponse:
        """Create a share recipient
        
        Creates a new recipient with the delta sharing authentication type in
        the Metastore. The caller must be a Metastore admin or has the CREATE
        RECIPIENT privilege on the Metastore."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/unity-catalog/recipients', query=query, body=body)
        return CreateRecipientResponse.from_dict(json)
    
    def deleteRecipient(self, request: DeleteRecipientRequest):
        """Delete a share recipient
        
        Deletes the specified recipient from the Metastore. The caller must be
        the owner of the recipient."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.1/unity-catalog/recipients/{request.name}', query=query, body=body)
        
    
    def getRecipient(self, request: GetRecipientRequest) -> GetRecipientResponse:
        """Get a share recipient
        
        Gets a share recipient from the Metastore if:
        
        * the caller is the owner of the share recipient, or: * is a Metastore
        admin"""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/recipients/{request.name}', query=query, body=body)
        return GetRecipientResponse.from_dict(json)
    
    def getRecipientSharePermissions(self, request: GetRecipientSharePermissionsRequest) -> GetRecipientSharePermissionsResponse:
        """Get share permissions
        
        Gets the share permissions for the specified Recipient. The caller must
        be a Metastore admin or the owner of the Recipient."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/recipients/{request.name}/share-permissions', query=query, body=body)
        return GetRecipientSharePermissionsResponse.from_dict(json)
    
    def list(self) -> ListRecipientsResponse:
        """List share recipients
        
        Gets an array of all share recipients within the current Metastore
        where:
        
        * the caller is a Metastore admin, or * the caller is the owner."""
        
        json = self._api.do('GET', '/api/2.1/unity-catalog/recipients')
        return ListRecipientsResponse.from_dict(json)
    
    def rotateRecipientToken(self, request: RotateRecipientToken) -> RotateRecipientTokenResponse:
        """Rotate a token
        
        Refreshes the specified recipient's delta sharing authentication token
        with the provided token info. The caller must be the owner of the
        recipient."""
        query, body = request.as_request()
        json = self._api.do('POST', f'/api/2.1/unity-catalog/recipients/{request.name}/rotate-token', query=query, body=body)
        return RotateRecipientTokenResponse.from_dict(json)
    
    def update(self, request: UpdateRecipient):
        """Update a share recipient
        
        Updates an existing recipient in the Metastore. The caller must be a
        Metastore admin or the owner of the recipient. If the recipient name
        will be updated, the user must be both a Metastore admin and the owner
        of the recipient."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/recipients/{request.name}', query=query, body=body)
        
    
class SchemasAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def create(self, request: CreateSchema) -> CreateSchemaResponse:
        """Create a schema
        
        Creates a new schema for catalog in the Metatastore. The caller must be
        a Metastore admin, or have the CREATE privilege in the parentcatalog."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/unity-catalog/schemas', query=query, body=body)
        return CreateSchemaResponse.from_dict(json)
    
    def deleteSchema(self, request: DeleteSchemaRequest):
        """Delete a schema
        
        Deletes the specified schema from the parent catalog. The caller must be
        the owner of the schema or an owner of the parent catalog."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.1/unity-catalog/schemas/{request.full_name}', query=query, body=body)
        
    
    def getSchema(self, request: GetSchemaRequest) -> GetSchemaResponse:
        """Get a schema
        
        Gets the specified schema for a catalog in the Metastore. The caller
        must be a Metastore admin, the owner of the schema, or a user that has
        the USAGE privilege on the schema."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/schemas/{request.full_name}', query=query, body=body)
        return GetSchemaResponse.from_dict(json)
    
    def list(self, request: ListRequest) -> ListSchemasResponse:
        """List schemas
        
        Gets an array of schemas for catalog in the Metastore. If the caller is
        the Metastore admin or the owner of the parent catalog, all schemas for
        the catalog will be retrieved. Otherwise, only schemas owned by the
        caller (or for which the caller has the USAGE privilege) will be
        retrieved."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.1/unity-catalog/schemas', query=query, body=body)
        return ListSchemasResponse.from_dict(json)
    
    def update(self, request: UpdateSchema):
        """Update a schema
        
        Updates a schema for a catalog. The caller must be the owner of the
        schema. If the caller is a Metastore admin, only the __owner__ field can
        be changed in the update. If the __name__ field must be updated, the
        caller must be a Metastore admin or have the CREATE privilege on the
        parent catalog."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/schemas/{request.full_name}', query=query, body=body)
        
    
class SharesAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def create(self, request: CreateShare) -> CreateShareResponse:
        """Create a share
        
        Creates a new share for data objects. Data objects can be added at this
        time or after creation with **update**. The caller must be a Metastore
        admin or have the CREATE SHARE privilege on the Metastore."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/unity-catalog/shares', query=query, body=body)
        return CreateShareResponse.from_dict(json)
    
    def deleteShare(self, request: DeleteShareRequest):
        """Delete a share
        
        Deletes a data object share from the Metastore. The caller must be an
        owner of the share."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.1/unity-catalog/shares/{request.name}', query=query, body=body)
        
    
    def getShare(self, request: GetShareRequest) -> GetShareResponse:
        """Get a share
        
        Gets a data object share from the Metastore. The caller must be a
        Metastore admin or the owner of the share."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/shares/{request.name}', query=query, body=body)
        return GetShareResponse.from_dict(json)
    
    def getSharePermissions(self, request: GetSharePermissionsRequest) -> GetSharePermissionsResponse:
        """Get permissions
        
        Gets the permissions for a data share from the Metastore. The caller
        must be a Metastore admin or the owner of the share."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/shares/{request.name}/permissions', query=query, body=body)
        return GetSharePermissionsResponse.from_dict(json)
    
    def list(self) -> ListSharesResponse:
        """List shares
        
        Gets an array of data object shares from the Metastore. The caller must
        be a Metastore admin or the owner of the share."""
        
        json = self._api.do('GET', '/api/2.1/unity-catalog/shares')
        return ListSharesResponse.from_dict(json)
    
    def update(self, request: UpdateShare):
        """Update a share
        
        Updates the share with the changes and data objects in the request. The
        caller must be the owner of the share or a Metastore admin.
        
        When the caller is a Metastore admin, only the __owner__ field can be
        updated.
        
        In the case that the Share name is changed, **updateShare** requires
        that the caller is both the share owner and a Metastore admin.
        
        For each table that is added through this method, the share owner must
        also have SELECT privilege on the table. This privilege must be
        maintained indefinitely for recipients to be able to access the table.
        Typically, you should use a group as the share owner.
        
        Table removals through **update** do not require additional privileges."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/shares/{request.name}', query=query, body=body)
        
    
    def updateSharePermissions(self, request: UpdateSharePermissions):
        """Update permissions
        
        Updates the permissions for a data share in the Metastore. The caller
        must be a Metastore admin or an owner of the share.
        
        For new recipient grants, the user must also be the owner of the
        recipients. recipient revocations do not require additional privileges."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/shares/{request.name}/permissions', query=query, body=body)
        
    
class StorageCredentialsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def create(self, request: CreateStorageCredential) -> CreateStorageCredentialResponse:
        """Create credentials
        
        Creates a new storage credential. The request object is specific to the
        cloud:
        
        * **AwsIamRole** for AWS credentials * **AzureServicePrincipal** for
        Azure credentials * **GcpServiceAcountKey** for GCP credentials.
        
        The caller must be a Metastore admin and have the CREATE STORAGE
        CREDENTIAL privilege on the Metastore."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/unity-catalog/storage-credentials', query=query, body=body)
        return CreateStorageCredentialResponse.from_dict(json)
    
    def deleteStorageCredential(self, request: DeleteStorageCredentialRequest):
        """Delete a credential
        
        Deletes a storage credential from the Metastore. The caller must be an
        owner of the storage credential."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.1/unity-catalog/storage-credentials/{request.name}', query=query, body=body)
        
    
    def getStorageCredentials(self, request: GetStorageCredentialsRequest) -> GetStorageCredentialResponse:
        """Get a credential
        
        Gets a storage credential from the Metastore. The caller must be a
        Metastore admin, the owner of the storage credential, or have a level of
        privilege on the storage credential."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/storage-credentials/{request.name}', query=query, body=body)
        return GetStorageCredentialResponse.from_dict(json)
    
    def list(self) -> ListStorageCredentialsResponse:
        """List credentials
        
        Gets an array of storage credentials (as StorageCredentialInfo objects).
        The array is limited to only those storage credentials the caller has
        the privilege level to access. If the caller is a Metastore admin, all
        storage credentials will be retrieved."""
        
        json = self._api.do('GET', '/api/2.1/unity-catalog/storage-credentials')
        return ListStorageCredentialsResponse.from_dict(json)
    
    def update(self, request: UpdateStorageCredential):
        """Update a credential
        
        Updates a storage credential on the Metastore. The caller must be the
        owner of the storage credential. If the caller is a Metastore admin,
        only the __owner__ credential can be changed."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/storage-credentials/{request.name}', query=query, body=body)
        
    
class TablesAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def create(self, request: CreateTable) -> CreateTableResponse:
        """Create a table
        
        Creates a new table in the Metastore for a specific catalog and schema.
        **WARNING**: Do not use this API at this time.
        
        The caller must be the owner of or have the USAGE privilege for both the
        parent catalog and schema, or be the owner of the parent schema (or have
        the CREATE privilege on it).
        
        If the new table has a __table_type__ of EXTERNAL specified, the user
        must be a Metastore admin or meet the permissions requirements of the
        storage credential or the external location."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/unity-catalog/tables', query=query, body=body)
        return CreateTableResponse.from_dict(json)
    
    def createStagingTable(self, request: CreateStagingTable) -> CreateStagingTableResponse:
        """Create a staging table
        
        Creates a new staging table for a schema. The caller must have both the
        USAGE privilege on the parent Catalog and the USAGE and CREATE
        privileges on the parent schema."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.1/unity-catalog/staging-tables', query=query, body=body)
        return CreateStagingTableResponse.from_dict(json)
    
    def deleteTable(self, request: DeleteTableRequest):
        """Delete a table
        
        Deletes a table from the specified parent catalog and schema. The caller
        must be the owner of the parent catalog, have the USAGE privilege on the
        parent catalog and be the owner of the parent schema, or be the owner of
        the table and have the USAGE privilege on both the parent catalog and
        schema."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.1/unity-catalog/tables/{request.full_name}', query=query, body=body)
        
    
    def getTable(self, request: GetTableRequest) -> GetTableResponse:
        """Get a table
        
        Gets a table from the Metastore for a specific catalog and schema. The
        caller must be a Metastore admin, be the owner of the table and have the
        USAGE privilege on both the parent catalog and schema, or be the owner
        of the table and have the SELECT privilege on it as well."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.1/unity-catalog/tables/{request.full_name}', query=query, body=body)
        return GetTableResponse.from_dict(json)
    
    def list(self, request: ListRequest) -> ListTablesResponse:
        """List tables
        
        Gets an array of all tables for the current Metastore under the parent
        catalog and schema. The caller must be a Metastore admin or an owner of
        (or have the SELECT privilege on) the table. For the latter case, the
        caller must also be the owner or have the USAGE privilege on the parent
        catalog and schema."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.1/unity-catalog/tables', query=query, body=body)
        return ListTablesResponse.from_dict(json)
    
    def listTableSummaries(self, request: ListTableSummariesRequest) -> ListTableSummariesResponse:
        """List table summaries
        
        Gets an array of summaries for tables for a schema and catalog within
        the Metastore. The table summaries returned are either:
        
        * summaries for all tables (within the current Metastore and parent
        catalog and schema), when the user is a Metastore admin, or: * summaries
        for all tables and schemas (within the current Metastore and parent
        catalog) for which the user has ownership or the SELECT privilege on the
        Table and ownership or USAGE privilege on the Schema, provided that the
        user also has ownership or the USAGE privilege on the parent Catalog"""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.1/unity-catalog/table-summaries', query=query, body=body)
        return ListTableSummariesResponse.from_dict(json)
    
    def update(self, request: UpdateTable):
        """Update a table
        
        Updates a table in the specified catalog and schema. The caller must be
        the owner of have the USAGE privilege on the parent catalog and schema,
        or, if changing the owner, be a Metastore admin as well."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.1/unity-catalog/tables/{request.full_name}', query=query, body=body)
        
    
class UnityFilesAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def listFiles(self, request: ListFilesRequest) -> ListFilesResponse:
        """List files
        
        List the files sound at the supplied URL."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.1/unity-catalog/files', query=query, body=body)
        return ListFilesResponse.from_dict(json)
    
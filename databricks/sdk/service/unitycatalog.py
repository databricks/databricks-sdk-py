# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


class AuthenticationType(Enum):
    """The delta sharing authentication type."""

    DATABRICKS = "DATABRICKS"
    TOKEN = "TOKEN"
    UNKNOWN = "UNKNOWN"


@dataclass
class AwsIamRole:

    # The external ID used in role assumption to prevent confused deputy
    # problem..
    external_id: str
    # The Amazon Resource Name (ARN) of the AWS IAM role for S3 data access.
    role_arn: str
    # The Amazon Resource Name (ARN) of the AWS IAM user managed by Databricks.
    # This is the identity that is going to assume the AWS IAM role.
    unity_catalog_iam_arn: str

    def as_request(self) -> (dict, dict):
        awsIamRole_query, awsIamRole_body = {}, {}
        if self.external_id:
            awsIamRole_body["external_id"] = self.external_id
        if self.role_arn:
            awsIamRole_body["role_arn"] = self.role_arn
        if self.unity_catalog_iam_arn:
            awsIamRole_body["unity_catalog_iam_arn"] = self.unity_catalog_iam_arn

        return awsIamRole_query, awsIamRole_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "AwsIamRole":
        return cls(
            external_id=d.get("external_id", None),
            role_arn=d.get("role_arn", None),
            unity_catalog_iam_arn=d.get("unity_catalog_iam_arn", None),
        )


@dataclass
class AzureServicePrincipal:

    # The application ID of the application registration within the referenced
    # AAD tenant.
    application_id: str
    # The client secret generated for the above app ID in AAD.
    client_secret: str
    # The directory ID corresponding to the Azure Active Directory (AAD) tenant
    # of the application.
    directory_id: str

    def as_request(self) -> (dict, dict):
        azureServicePrincipal_query, azureServicePrincipal_body = {}, {}
        if self.application_id:
            azureServicePrincipal_body["application_id"] = self.application_id
        if self.client_secret:
            azureServicePrincipal_body["client_secret"] = self.client_secret
        if self.directory_id:
            azureServicePrincipal_body["directory_id"] = self.directory_id

        return azureServicePrincipal_query, azureServicePrincipal_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "AzureServicePrincipal":
        return cls(
            application_id=d.get("application_id", None),
            client_secret=d.get("client_secret", None),
            directory_id=d.get("directory_id", None),
        )


@dataclass
class CatalogInfo:

    # The type of the catalog.
    catalog_type: "CatalogType"
    # User-provided free-form text description.
    comment: str
    # Time at which this Catalog was created, in epoch milliseconds.
    created_at: int
    # Username of Catalog creator.
    created_by: str
    # Unique identifier of parent Metastore.
    metastore_id: str
    # Name of Catalog.
    name: str
    # Username of current owner of Catalog.
    owner: str
    # Privileges the user has on the Catalog.
    privileges: "List[Privilege]"

    properties: "Dict[str,str]"
    # The name of delta sharing provider.
    #
    # A Delta Sharing Catalog is a catalog that is based on a Delta share on a
    # remote sharing server.
    provider_name: str
    # The name of the share under the share provider.
    share_name: str
    # Time at which this Catalog was last modified, in epoch milliseconds.
    updated_at: int
    # Username of user who last modified Catalog.
    updated_by: str

    def as_request(self) -> (dict, dict):
        catalogInfo_query, catalogInfo_body = {}, {}
        if self.catalog_type:
            catalogInfo_body["catalog_type"] = self.catalog_type.value
        if self.comment:
            catalogInfo_body["comment"] = self.comment
        if self.created_at:
            catalogInfo_body["created_at"] = self.created_at
        if self.created_by:
            catalogInfo_body["created_by"] = self.created_by
        if self.metastore_id:
            catalogInfo_body["metastore_id"] = self.metastore_id
        if self.name:
            catalogInfo_body["name"] = self.name
        if self.owner:
            catalogInfo_body["owner"] = self.owner
        if self.privileges:
            catalogInfo_body["privileges"] = [v for v in self.privileges]
        if self.properties:
            catalogInfo_body["properties"] = self.properties
        if self.provider_name:
            catalogInfo_body["provider_name"] = self.provider_name
        if self.share_name:
            catalogInfo_body["share_name"] = self.share_name
        if self.updated_at:
            catalogInfo_body["updated_at"] = self.updated_at
        if self.updated_by:
            catalogInfo_body["updated_by"] = self.updated_by

        return catalogInfo_query, catalogInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CatalogInfo":
        return cls(
            catalog_type=CatalogType(d["catalog_type"])
            if "catalog_type" in d
            else None,
            comment=d.get("comment", None),
            created_at=d.get("created_at", None),
            created_by=d.get("created_by", None),
            metastore_id=d.get("metastore_id", None),
            name=d.get("name", None),
            owner=d.get("owner", None),
            privileges=d.get("privileges", None),
            properties=d.get("properties", None),
            provider_name=d.get("provider_name", None),
            share_name=d.get("share_name", None),
            updated_at=d.get("updated_at", None),
            updated_by=d.get("updated_by", None),
        )


class CatalogType(Enum):
    """The type of the catalog."""

    DELTASHARING_CATALOG = "DELTASHARING_CATALOG"
    MANAGED_CATALOG = "MANAGED_CATALOG"
    SYSTEM_CATALOG = "SYSTEM_CATALOG"
    UNKNOWN_CATALOG_TYPE = "UNKNOWN_CATALOG_TYPE"


@dataclass
class ColumnInfo:

    # [Create,Update:OPT] User-provided free-form text description.
    comment: str
    # [Create:REQ Update:OPT] Name of Column.
    name: str
    # [Create,Update:OPT] Whether field may be Null (default: True).
    nullable: bool
    # [Create,Update:OPT] Partition index for column.
    partition_index: int
    # [Create:REQ Update:OPT] Ordinal position of column (starting at position
    # 0).
    position: int
    # [Create: OPT, Update: OPT] Format of IntervalType.
    type_interval_type: str
    # [Create:OPT Update:OPT] Full data type spec, JSON-serialized.
    type_json: str
    # [Create: REQ Update: OPT] Name of type (INT, STRUCT, MAP, etc.)
    type_name: "ColumnInfoTypeName"
    # [Create: OPT, Update: OPT] Digits of precision; required on Create for
    # DecimalTypes.
    type_precision: int
    # [Create: OPT, Update: OPT] Digits to right of decimal; Required on Create
    # for DecimalTypes.
    type_scale: int
    # [Create:REQ Update:OPT] Full data type spec, SQL/catalogString text.
    type_text: str

    def as_request(self) -> (dict, dict):
        columnInfo_query, columnInfo_body = {}, {}
        if self.comment:
            columnInfo_body["comment"] = self.comment
        if self.name:
            columnInfo_body["name"] = self.name
        if self.nullable:
            columnInfo_body["nullable"] = self.nullable
        if self.partition_index:
            columnInfo_body["partition_index"] = self.partition_index
        if self.position:
            columnInfo_body["position"] = self.position
        if self.type_interval_type:
            columnInfo_body["type_interval_type"] = self.type_interval_type
        if self.type_json:
            columnInfo_body["type_json"] = self.type_json
        if self.type_name:
            columnInfo_body["type_name"] = self.type_name.value
        if self.type_precision:
            columnInfo_body["type_precision"] = self.type_precision
        if self.type_scale:
            columnInfo_body["type_scale"] = self.type_scale
        if self.type_text:
            columnInfo_body["type_text"] = self.type_text

        return columnInfo_query, columnInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ColumnInfo":
        return cls(
            comment=d.get("comment", None),
            name=d.get("name", None),
            nullable=d.get("nullable", None),
            partition_index=d.get("partition_index", None),
            position=d.get("position", None),
            type_interval_type=d.get("type_interval_type", None),
            type_json=d.get("type_json", None),
            type_name=ColumnInfoTypeName(d["type_name"]) if "type_name" in d else None,
            type_precision=d.get("type_precision", None),
            type_scale=d.get("type_scale", None),
            type_text=d.get("type_text", None),
        )


class ColumnInfoTypeName(Enum):
    """[Create: REQ Update: OPT] Name of type (INT, STRUCT, MAP, etc.)"""

    ARRAY = "ARRAY"
    BINARY = "BINARY"
    BOOLEAN = "BOOLEAN"
    BYTE = "BYTE"
    CHAR = "CHAR"
    DATE = "DATE"
    DECIMAL = "DECIMAL"
    DOUBLE = "DOUBLE"
    FLOAT = "FLOAT"
    INT = "INT"
    INTERVAL = "INTERVAL"
    LONG = "LONG"
    MAP = "MAP"
    NULL = "NULL"
    SHORT = "SHORT"
    STRING = "STRING"
    STRUCT = "STRUCT"
    TIMESTAMP = "TIMESTAMP"
    UNKNOWN_COLUMN_TYPE_NAME = "UNKNOWN_COLUMN_TYPE_NAME"


@dataclass
class CreateCatalog:

    # User-provided free-form text description.
    comment: str
    # Name of Catalog.
    name: str

    properties: "Dict[str,str]"
    # The name of delta sharing provider.
    #
    # A Delta Sharing Catalog is a catalog that is based on a Delta share on a
    # remote sharing server.
    provider_name: str
    # The name of the share under the share provider.
    share_name: str

    def as_request(self) -> (dict, dict):
        createCatalog_query, createCatalog_body = {}, {}
        if self.comment:
            createCatalog_body["comment"] = self.comment
        if self.name:
            createCatalog_body["name"] = self.name
        if self.properties:
            createCatalog_body["properties"] = self.properties
        if self.provider_name:
            createCatalog_body["provider_name"] = self.provider_name
        if self.share_name:
            createCatalog_body["share_name"] = self.share_name

        return createCatalog_query, createCatalog_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateCatalog":
        return cls(
            comment=d.get("comment", None),
            name=d.get("name", None),
            properties=d.get("properties", None),
            provider_name=d.get("provider_name", None),
            share_name=d.get("share_name", None),
        )


@dataclass
class CreateExternalLocation:

    # User-provided free-form text description.
    comment: str
    # Current name of the Storage Credential this location uses.
    credential_name: str
    # Name of the External Location.
    name: str
    # Path URL of the External Location.
    url: str

    def as_request(self) -> (dict, dict):
        createExternalLocation_query, createExternalLocation_body = {}, {}
        if self.comment:
            createExternalLocation_body["comment"] = self.comment
        if self.credential_name:
            createExternalLocation_body["credential_name"] = self.credential_name
        if self.name:
            createExternalLocation_body["name"] = self.name
        if self.url:
            createExternalLocation_body["url"] = self.url

        return createExternalLocation_query, createExternalLocation_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateExternalLocation":
        return cls(
            comment=d.get("comment", None),
            credential_name=d.get("credential_name", None),
            name=d.get("name", None),
            url=d.get("url", None),
        )


@dataclass
class CreateMetastore:

    # Name of Metastore.
    name: str
    # Storage root URL for Metastore
    storage_root: str

    def as_request(self) -> (dict, dict):
        createMetastore_query, createMetastore_body = {}, {}
        if self.name:
            createMetastore_body["name"] = self.name
        if self.storage_root:
            createMetastore_body["storage_root"] = self.storage_root

        return createMetastore_query, createMetastore_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateMetastore":
        return cls(
            name=d.get("name", None),
            storage_root=d.get("storage_root", None),
        )


@dataclass
class CreateMetastoreAssignment:

    # THe name of the default catalog in the Metastore.
    default_catalog_name: str
    # The ID of the Metastore.
    metastore_id: str
    # A workspace ID.
    workspace_id: int  # path

    def as_request(self) -> (dict, dict):
        createMetastoreAssignment_query, createMetastoreAssignment_body = {}, {}
        if self.default_catalog_name:
            createMetastoreAssignment_body[
                "default_catalog_name"
            ] = self.default_catalog_name
        if self.metastore_id:
            createMetastoreAssignment_body["metastore_id"] = self.metastore_id
        if self.workspace_id:
            createMetastoreAssignment_body["workspace_id"] = self.workspace_id

        return createMetastoreAssignment_query, createMetastoreAssignment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateMetastoreAssignment":
        return cls(
            default_catalog_name=d.get("default_catalog_name", None),
            metastore_id=d.get("metastore_id", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class CreateProvider:

    # The delta sharing authentication type.
    authentication_type: "AuthenticationType"
    # Description about the provider.
    comment: str
    # The name of the Provider.
    name: str
    # Username of Provider owner.
    owner: str
    # This field is only present when the authentication type is TOKEN.
    recipient_profile: "RecipientProfile"
    # This field is only present when the authentication type is TOKEN.
    recipient_profile_str: str

    def as_request(self) -> (dict, dict):
        createProvider_query, createProvider_body = {}, {}
        if self.authentication_type:
            createProvider_body["authentication_type"] = self.authentication_type.value
        if self.comment:
            createProvider_body["comment"] = self.comment
        if self.name:
            createProvider_body["name"] = self.name
        if self.owner:
            createProvider_body["owner"] = self.owner
        if self.recipient_profile:
            createProvider_body[
                "recipient_profile"
            ] = self.recipient_profile.as_request()[1]
        if self.recipient_profile_str:
            createProvider_body["recipient_profile_str"] = self.recipient_profile_str

        return createProvider_query, createProvider_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateProvider":
        return cls(
            authentication_type=AuthenticationType(d["authentication_type"])
            if "authentication_type" in d
            else None,
            comment=d.get("comment", None),
            name=d.get("name", None),
            owner=d.get("owner", None),
            recipient_profile=RecipientProfile.from_dict(d["recipient_profile"])
            if "recipient_profile" in d
            else None,
            recipient_profile_str=d.get("recipient_profile_str", None),
        )


@dataclass
class CreateRecipient:

    # The delta sharing authentication type.
    authentication_type: "AuthenticationType"
    # Description about the recipient.
    comment: str
    # IP Access List
    ip_access_list: "IpAccessList"
    # Name of Recipient.
    name: str
    # The one-time sharing code provided by the data recipient. This field is
    # only present when the authentication type is `DATABRICKS`.
    sharing_code: str

    def as_request(self) -> (dict, dict):
        createRecipient_query, createRecipient_body = {}, {}
        if self.authentication_type:
            createRecipient_body["authentication_type"] = self.authentication_type.value
        if self.comment:
            createRecipient_body["comment"] = self.comment
        if self.ip_access_list:
            createRecipient_body["ip_access_list"] = self.ip_access_list.as_request()[1]
        if self.name:
            createRecipient_body["name"] = self.name
        if self.sharing_code:
            createRecipient_body["sharing_code"] = self.sharing_code

        return createRecipient_query, createRecipient_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateRecipient":
        return cls(
            authentication_type=AuthenticationType(d["authentication_type"])
            if "authentication_type" in d
            else None,
            comment=d.get("comment", None),
            ip_access_list=IpAccessList.from_dict(d["ip_access_list"])
            if "ip_access_list" in d
            else None,
            name=d.get("name", None),
            sharing_code=d.get("sharing_code", None),
        )


@dataclass
class CreateSchema:

    # Name of parent Catalog.
    catalog_name: str
    # User-provided free-form text description.
    comment: str
    # Name of Schema, relative to parent Catalog.
    name: str

    properties: "Dict[str,str]"

    def as_request(self) -> (dict, dict):
        createSchema_query, createSchema_body = {}, {}
        if self.catalog_name:
            createSchema_body["catalog_name"] = self.catalog_name
        if self.comment:
            createSchema_body["comment"] = self.comment
        if self.name:
            createSchema_body["name"] = self.name
        if self.properties:
            createSchema_body["properties"] = self.properties

        return createSchema_query, createSchema_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateSchema":
        return cls(
            catalog_name=d.get("catalog_name", None),
            comment=d.get("comment", None),
            name=d.get("name", None),
            properties=d.get("properties", None),
        )


@dataclass
class CreateShare:

    # comment when creating the share
    comment: str
    # Name of the Share.
    name: str

    def as_request(self) -> (dict, dict):
        createShare_query, createShare_body = {}, {}
        if self.comment:
            createShare_body["comment"] = self.comment
        if self.name:
            createShare_body["name"] = self.name

        return createShare_query, createShare_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateShare":
        return cls(
            comment=d.get("comment", None),
            name=d.get("name", None),
        )


@dataclass
class CreateStorageCredential:

    # The AWS IAM role configuration.
    aws_iam_role: "AwsIamRole"
    # The Azure service principal configuration.
    azure_service_principal: "AzureServicePrincipal"
    # Comment associated with the credential.
    comment: str
    # The GCP service account key configuration.
    gcp_service_account_key: "GcpServiceAccountKey"
    # The credential name. The name MUST be unique within the Metastore.
    name: str
    # Optional. Supplying true to this argument skips validation of the created
    # set of credentials.
    skip_validation: bool

    def as_request(self) -> (dict, dict):
        createStorageCredential_query, createStorageCredential_body = {}, {}
        if self.aws_iam_role:
            createStorageCredential_body[
                "aws_iam_role"
            ] = self.aws_iam_role.as_request()[1]
        if self.azure_service_principal:
            createStorageCredential_body[
                "azure_service_principal"
            ] = self.azure_service_principal.as_request()[1]
        if self.comment:
            createStorageCredential_body["comment"] = self.comment
        if self.gcp_service_account_key:
            createStorageCredential_body[
                "gcp_service_account_key"
            ] = self.gcp_service_account_key.as_request()[1]
        if self.name:
            createStorageCredential_body["name"] = self.name
        if self.skip_validation:
            createStorageCredential_body["skip_validation"] = self.skip_validation

        return createStorageCredential_query, createStorageCredential_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateStorageCredential":
        return cls(
            aws_iam_role=AwsIamRole.from_dict(d["aws_iam_role"])
            if "aws_iam_role" in d
            else None,
            azure_service_principal=AzureServicePrincipal.from_dict(
                d["azure_service_principal"]
            )
            if "azure_service_principal" in d
            else None,
            comment=d.get("comment", None),
            gcp_service_account_key=GcpServiceAccountKey.from_dict(
                d["gcp_service_account_key"]
            )
            if "gcp_service_account_key" in d
            else None,
            name=d.get("name", None),
            skip_validation=d.get("skip_validation", None),
        )


class DataSourceFormat(Enum):
    """Data source format"""

    AVRO = "AVRO"
    CSV = "CSV"
    DELTA = "DELTA"
    DELTASHARING = "DELTASHARING"
    JSON = "JSON"
    ORC = "ORC"
    PARQUET = "PARQUET"
    TEXT = "TEXT"
    UNITY_CATALOG = "UNITY_CATALOG"
    UNKNOWN_DATA_SOURCE_FORMAT = "UNKNOWN_DATA_SOURCE_FORMAT"


@dataclass
class DeleteCatalogRequest:
    """Delete a catalog"""

    # Required. The name of the catalog.
    name: str  # path

    def as_request(self) -> (dict, dict):
        deleteCatalogRequest_query, deleteCatalogRequest_body = {}, {}
        if self.name:
            deleteCatalogRequest_body["name"] = self.name

        return deleteCatalogRequest_query, deleteCatalogRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteCatalogRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class DeleteExternalLocationRequest:
    """Delete an external location"""

    # Force deletion even if there are dependent external tables or mounts.
    force: bool  # query
    # Required. Name of the storage credential.
    name: str  # path

    def as_request(self) -> (dict, dict):
        deleteExternalLocationRequest_query, deleteExternalLocationRequest_body = {}, {}
        if self.force:
            deleteExternalLocationRequest_query["force"] = self.force
        if self.name:
            deleteExternalLocationRequest_body["name"] = self.name

        return deleteExternalLocationRequest_query, deleteExternalLocationRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteExternalLocationRequest":
        return cls(
            force=d.get("force", None),
            name=d.get("name", None),
        )


@dataclass
class DeleteMetastoreRequest:
    """Delete a Metastore"""

    # Force deletion even if the metastore is not empty. Default is false.
    force: bool  # query
    # Required. Unique ID of the Metastore (from URL).
    id: str  # path

    def as_request(self) -> (dict, dict):
        deleteMetastoreRequest_query, deleteMetastoreRequest_body = {}, {}
        if self.force:
            deleteMetastoreRequest_query["force"] = self.force
        if self.id:
            deleteMetastoreRequest_body["id"] = self.id

        return deleteMetastoreRequest_query, deleteMetastoreRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteMetastoreRequest":
        return cls(
            force=d.get("force", None),
            id=d.get("id", None),
        )


@dataclass
class DeleteProviderRequest:
    """Delete a provider"""

    # Required. Name of the provider.
    name: str  # path

    def as_request(self) -> (dict, dict):
        deleteProviderRequest_query, deleteProviderRequest_body = {}, {}
        if self.name:
            deleteProviderRequest_body["name"] = self.name

        return deleteProviderRequest_query, deleteProviderRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteProviderRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class DeleteRecipientRequest:
    """Delete a share recipient"""

    # Required. Name of the recipient.
    name: str  # path

    def as_request(self) -> (dict, dict):
        deleteRecipientRequest_query, deleteRecipientRequest_body = {}, {}
        if self.name:
            deleteRecipientRequest_body["name"] = self.name

        return deleteRecipientRequest_query, deleteRecipientRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteRecipientRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class DeleteSchemaRequest:
    """Delete a schema"""

    # Required. Full name of the schema (from URL).
    full_name: str  # path

    def as_request(self) -> (dict, dict):
        deleteSchemaRequest_query, deleteSchemaRequest_body = {}, {}
        if self.full_name:
            deleteSchemaRequest_body["full_name"] = self.full_name

        return deleteSchemaRequest_query, deleteSchemaRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteSchemaRequest":
        return cls(
            full_name=d.get("full_name", None),
        )


@dataclass
class DeleteShareRequest:
    """Delete a share"""

    # The name of the share.
    name: str  # path

    def as_request(self) -> (dict, dict):
        deleteShareRequest_query, deleteShareRequest_body = {}, {}
        if self.name:
            deleteShareRequest_body["name"] = self.name

        return deleteShareRequest_query, deleteShareRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteShareRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class DeleteStorageCredentialRequest:
    """Delete a credential"""

    # Force deletion even if there are dependent external locations or external
    # tables.
    force: bool  # query
    # Required. Name of the storage credential.
    name: str  # path

    def as_request(self) -> (dict, dict):
        deleteStorageCredentialRequest_query, deleteStorageCredentialRequest_body = (
            {},
            {},
        )
        if self.force:
            deleteStorageCredentialRequest_query["force"] = self.force
        if self.name:
            deleteStorageCredentialRequest_body["name"] = self.name

        return deleteStorageCredentialRequest_query, deleteStorageCredentialRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteStorageCredentialRequest":
        return cls(
            force=d.get("force", None),
            name=d.get("name", None),
        )


@dataclass
class DeleteTableRequest:
    """Delete a table"""

    # Required. Full name of the Table (from URL).
    full_name: str  # path

    def as_request(self) -> (dict, dict):
        deleteTableRequest_query, deleteTableRequest_body = {}, {}
        if self.full_name:
            deleteTableRequest_body["full_name"] = self.full_name

        return deleteTableRequest_query, deleteTableRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteTableRequest":
        return cls(
            full_name=d.get("full_name", None),
        )


@dataclass
class ExternalLocationInfo:

    # User-provided free-form text description.
    comment: str
    # Time at which this External Location was created, in epoch milliseconds.
    created_at: int
    # Username of External Location creator.
    created_by: str
    # Unique ID of the location's Storage Credential.
    credential_id: str
    # Current name of the Storage Credential this location uses.
    credential_name: str
    # Unique identifier of Metastore hosting the External Location.
    metastore_id: str
    # Name of the External Location.
    name: str
    # The owner of the External Location.
    owner: str
    # Time at which this was last modified, in epoch milliseconds.
    updated_at: int
    # Username of user who last modified the External Location.
    updated_by: str
    # Path URL of the External Location.
    url: str

    def as_request(self) -> (dict, dict):
        externalLocationInfo_query, externalLocationInfo_body = {}, {}
        if self.comment:
            externalLocationInfo_body["comment"] = self.comment
        if self.created_at:
            externalLocationInfo_body["created_at"] = self.created_at
        if self.created_by:
            externalLocationInfo_body["created_by"] = self.created_by
        if self.credential_id:
            externalLocationInfo_body["credential_id"] = self.credential_id
        if self.credential_name:
            externalLocationInfo_body["credential_name"] = self.credential_name
        if self.metastore_id:
            externalLocationInfo_body["metastore_id"] = self.metastore_id
        if self.name:
            externalLocationInfo_body["name"] = self.name
        if self.owner:
            externalLocationInfo_body["owner"] = self.owner
        if self.updated_at:
            externalLocationInfo_body["updated_at"] = self.updated_at
        if self.updated_by:
            externalLocationInfo_body["updated_by"] = self.updated_by
        if self.url:
            externalLocationInfo_body["url"] = self.url

        return externalLocationInfo_query, externalLocationInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ExternalLocationInfo":
        return cls(
            comment=d.get("comment", None),
            created_at=d.get("created_at", None),
            created_by=d.get("created_by", None),
            credential_id=d.get("credential_id", None),
            credential_name=d.get("credential_name", None),
            metastore_id=d.get("metastore_id", None),
            name=d.get("name", None),
            owner=d.get("owner", None),
            updated_at=d.get("updated_at", None),
            updated_by=d.get("updated_by", None),
            url=d.get("url", None),
        )


@dataclass
class GcpServiceAccountKey:

    # The email of the service account.
    email: str
    # The service account's RSA private key.
    private_key: str
    # The ID of the service account's private key.
    private_key_id: str

    def as_request(self) -> (dict, dict):
        gcpServiceAccountKey_query, gcpServiceAccountKey_body = {}, {}
        if self.email:
            gcpServiceAccountKey_body["email"] = self.email
        if self.private_key:
            gcpServiceAccountKey_body["private_key"] = self.private_key
        if self.private_key_id:
            gcpServiceAccountKey_body["private_key_id"] = self.private_key_id

        return gcpServiceAccountKey_query, gcpServiceAccountKey_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GcpServiceAccountKey":
        return cls(
            email=d.get("email", None),
            private_key=d.get("private_key", None),
            private_key_id=d.get("private_key_id", None),
        )


@dataclass
class GetActivationUrlInfoRequest:
    """Get a share activation URL"""

    # Required. The one time activation url. It also accepts activation token.
    activation_url: str  # path

    def as_request(self) -> (dict, dict):
        getActivationUrlInfoRequest_query, getActivationUrlInfoRequest_body = {}, {}
        if self.activation_url:
            getActivationUrlInfoRequest_body["activation_url"] = self.activation_url

        return getActivationUrlInfoRequest_query, getActivationUrlInfoRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetActivationUrlInfoRequest":
        return cls(
            activation_url=d.get("activation_url", None),
        )


@dataclass
class GetCatalogRequest:
    """Get a catalog"""

    # Required. The name of the catalog.
    name: str  # path

    def as_request(self) -> (dict, dict):
        getCatalogRequest_query, getCatalogRequest_body = {}, {}
        if self.name:
            getCatalogRequest_body["name"] = self.name

        return getCatalogRequest_query, getCatalogRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetCatalogRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class GetExternalLocationRequest:
    """Get an external location"""

    # Required. Name of the storage credential.
    name: str  # path

    def as_request(self) -> (dict, dict):
        getExternalLocationRequest_query, getExternalLocationRequest_body = {}, {}
        if self.name:
            getExternalLocationRequest_body["name"] = self.name

        return getExternalLocationRequest_query, getExternalLocationRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetExternalLocationRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class GetGrantRequest:
    """Get permissions"""

    # Required. Unique identifier (full name) of Securable (from URL).
    full_name: str  # path
    # Optional. List permissions granted to this principal.
    principal: str  # query
    # Required. Type of Securable (from URL).
    securable_type: str  # path

    def as_request(self) -> (dict, dict):
        getGrantRequest_query, getGrantRequest_body = {}, {}
        if self.full_name:
            getGrantRequest_body["full_name"] = self.full_name
        if self.principal:
            getGrantRequest_query["principal"] = self.principal
        if self.securable_type:
            getGrantRequest_body["securable_type"] = self.securable_type

        return getGrantRequest_query, getGrantRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetGrantRequest":
        return cls(
            full_name=d.get("full_name", None),
            principal=d.get("principal", None),
            securable_type=d.get("securable_type", None),
        )


@dataclass
class GetMetastoreRequest:
    """Get a Metastore"""

    # Required. Unique ID of the Metastore (from URL).
    id: str  # path

    def as_request(self) -> (dict, dict):
        getMetastoreRequest_query, getMetastoreRequest_body = {}, {}
        if self.id:
            getMetastoreRequest_body["id"] = self.id

        return getMetastoreRequest_query, getMetastoreRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetMetastoreRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class GetMetastoreSummaryResponse:

    # Unique identifier of the Metastore's (Default) Data Access Configuration
    default_data_access_config_id: str
    # The unique ID (UUID) of the Metastore
    metastore_id: str
    # The user-specified name of the Metastore
    name: str
    # UUID of storage credential to access the metastore storage_root
    storage_root_credential_id: str

    def as_request(self) -> (dict, dict):
        getMetastoreSummaryResponse_query, getMetastoreSummaryResponse_body = {}, {}
        if self.default_data_access_config_id:
            getMetastoreSummaryResponse_body[
                "default_data_access_config_id"
            ] = self.default_data_access_config_id
        if self.metastore_id:
            getMetastoreSummaryResponse_body["metastore_id"] = self.metastore_id
        if self.name:
            getMetastoreSummaryResponse_body["name"] = self.name
        if self.storage_root_credential_id:
            getMetastoreSummaryResponse_body[
                "storage_root_credential_id"
            ] = self.storage_root_credential_id

        return getMetastoreSummaryResponse_query, getMetastoreSummaryResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetMetastoreSummaryResponse":
        return cls(
            default_data_access_config_id=d.get("default_data_access_config_id", None),
            metastore_id=d.get("metastore_id", None),
            name=d.get("name", None),
            storage_root_credential_id=d.get("storage_root_credential_id", None),
        )


@dataclass
class GetPermissionsResponse:

    privilege_assignments: "List[PrivilegeAssignment]"

    def as_request(self) -> (dict, dict):
        getPermissionsResponse_query, getPermissionsResponse_body = {}, {}
        if self.privilege_assignments:
            getPermissionsResponse_body["privilege_assignments"] = [
                v.as_request()[1] for v in self.privilege_assignments
            ]

        return getPermissionsResponse_query, getPermissionsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetPermissionsResponse":
        return cls(
            privilege_assignments=[
                PrivilegeAssignment.from_dict(v) for v in d["privilege_assignments"]
            ]
            if "privilege_assignments" in d
            else None,
        )


@dataclass
class GetProviderRequest:
    """Get a provider"""

    # Required. Name of the provider.
    name: str  # path

    def as_request(self) -> (dict, dict):
        getProviderRequest_query, getProviderRequest_body = {}, {}
        if self.name:
            getProviderRequest_body["name"] = self.name

        return getProviderRequest_query, getProviderRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetProviderRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class GetRecipientRequest:
    """Get a share recipient"""

    # Required. Name of the recipient.
    name: str  # path

    def as_request(self) -> (dict, dict):
        getRecipientRequest_query, getRecipientRequest_body = {}, {}
        if self.name:
            getRecipientRequest_body["name"] = self.name

        return getRecipientRequest_query, getRecipientRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetRecipientRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class GetRecipientSharePermissionsResponse:

    # An array of data share permissions for a recipient.
    permissions_out: "List[ShareToPrivilegeAssignment]"

    def as_request(self) -> (dict, dict):
        (
            getRecipientSharePermissionsResponse_query,
            getRecipientSharePermissionsResponse_body,
        ) = ({}, {})
        if self.permissions_out:
            getRecipientSharePermissionsResponse_body["permissions_out"] = [
                v.as_request()[1] for v in self.permissions_out
            ]

        return (
            getRecipientSharePermissionsResponse_query,
            getRecipientSharePermissionsResponse_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetRecipientSharePermissionsResponse":
        return cls(
            permissions_out=[
                ShareToPrivilegeAssignment.from_dict(v) for v in d["permissions_out"]
            ]
            if "permissions_out" in d
            else None,
        )


@dataclass
class GetSchemaRequest:
    """Get a schema"""

    # Required. Full name of the schema (from URL).
    full_name: str  # path

    def as_request(self) -> (dict, dict):
        getSchemaRequest_query, getSchemaRequest_body = {}, {}
        if self.full_name:
            getSchemaRequest_body["full_name"] = self.full_name

        return getSchemaRequest_query, getSchemaRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetSchemaRequest":
        return cls(
            full_name=d.get("full_name", None),
        )


@dataclass
class GetSharePermissionsResponse:

    # Note to self (acain): Unfortunately, neither json_inline nor json_map work
    # here.
    privilege_assignments: "List[PrivilegeAssignment]"

    def as_request(self) -> (dict, dict):
        getSharePermissionsResponse_query, getSharePermissionsResponse_body = {}, {}
        if self.privilege_assignments:
            getSharePermissionsResponse_body["privilege_assignments"] = [
                v.as_request()[1] for v in self.privilege_assignments
            ]

        return getSharePermissionsResponse_query, getSharePermissionsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetSharePermissionsResponse":
        return cls(
            privilege_assignments=[
                PrivilegeAssignment.from_dict(v) for v in d["privilege_assignments"]
            ]
            if "privilege_assignments" in d
            else None,
        )


@dataclass
class GetShareRequest:
    """Get a share"""

    # Query for data to include in the share.
    include_shared_data: bool  # query
    # The name of the share.
    name: str  # path

    def as_request(self) -> (dict, dict):
        getShareRequest_query, getShareRequest_body = {}, {}
        if self.include_shared_data:
            getShareRequest_query["include_shared_data"] = self.include_shared_data
        if self.name:
            getShareRequest_body["name"] = self.name

        return getShareRequest_query, getShareRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetShareRequest":
        return cls(
            include_shared_data=d.get("include_shared_data", None),
            name=d.get("name", None),
        )


@dataclass
class GetStorageCredentialRequest:
    """Get a credential"""

    # Required. Name of the storage credential.
    name: str  # path

    def as_request(self) -> (dict, dict):
        getStorageCredentialRequest_query, getStorageCredentialRequest_body = {}, {}
        if self.name:
            getStorageCredentialRequest_body["name"] = self.name

        return getStorageCredentialRequest_query, getStorageCredentialRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetStorageCredentialRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class GetTableRequest:
    """Get a table"""

    # Required. Full name of the Table (from URL).
    full_name: str  # path

    def as_request(self) -> (dict, dict):
        getTableRequest_query, getTableRequest_body = {}, {}
        if self.full_name:
            getTableRequest_body["full_name"] = self.full_name

        return getTableRequest_query, getTableRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetTableRequest":
        return cls(
            full_name=d.get("full_name", None),
        )


@dataclass
class IpAccessList:

    # Allowed IP Addresses in CIDR notation. Limit of 100.
    allowed_ip_addresses: "List[str]"

    def as_request(self) -> (dict, dict):
        ipAccessList_query, ipAccessList_body = {}, {}
        if self.allowed_ip_addresses:
            ipAccessList_body["allowed_ip_addresses"] = [
                v for v in self.allowed_ip_addresses
            ]

        return ipAccessList_query, ipAccessList_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "IpAccessList":
        return cls(
            allowed_ip_addresses=d.get("allowed_ip_addresses", None),
        )


@dataclass
class ListCatalogsResponse:

    # AN array of catalog information objects.
    catalogs: "List[CatalogInfo]"

    def as_request(self) -> (dict, dict):
        listCatalogsResponse_query, listCatalogsResponse_body = {}, {}
        if self.catalogs:
            listCatalogsResponse_body["catalogs"] = [
                v.as_request()[1] for v in self.catalogs
            ]

        return listCatalogsResponse_query, listCatalogsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListCatalogsResponse":
        return cls(
            catalogs=[CatalogInfo.from_dict(v) for v in d["catalogs"]]
            if "catalogs" in d
            else None,
        )


@dataclass
class ListExternalLocationsResponse:

    # AN array of external locations.
    external_locations: "List[ExternalLocationInfo]"

    def as_request(self) -> (dict, dict):
        listExternalLocationsResponse_query, listExternalLocationsResponse_body = {}, {}
        if self.external_locations:
            listExternalLocationsResponse_body["external_locations"] = [
                v.as_request()[1] for v in self.external_locations
            ]

        return listExternalLocationsResponse_query, listExternalLocationsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListExternalLocationsResponse":
        return cls(
            external_locations=[
                ExternalLocationInfo.from_dict(v) for v in d["external_locations"]
            ]
            if "external_locations" in d
            else None,
        )


@dataclass
class ListMetastoresResponse:

    # An array of Metastore information objects.
    metastores: "List[MetastoreInfo]"

    def as_request(self) -> (dict, dict):
        listMetastoresResponse_query, listMetastoresResponse_body = {}, {}
        if self.metastores:
            listMetastoresResponse_body["metastores"] = [
                v.as_request()[1] for v in self.metastores
            ]

        return listMetastoresResponse_query, listMetastoresResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListMetastoresResponse":
        return cls(
            metastores=[MetastoreInfo.from_dict(v) for v in d["metastores"]]
            if "metastores" in d
            else None,
        )


@dataclass
class ListProviderSharesResponse:

    # An array of provider shares.
    shares: "List[ProviderShare]"

    def as_request(self) -> (dict, dict):
        listProviderSharesResponse_query, listProviderSharesResponse_body = {}, {}
        if self.shares:
            listProviderSharesResponse_body["shares"] = [
                v.as_request()[1] for v in self.shares
            ]

        return listProviderSharesResponse_query, listProviderSharesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListProviderSharesResponse":
        return cls(
            shares=[ProviderShare.from_dict(v) for v in d["shares"]]
            if "shares" in d
            else None,
        )


@dataclass
class ListProvidersRequest:
    """List providers"""

    # If not provided, all providers will be returned. If no providers exist
    # with this ID, no results will be returned.
    data_provider_global_metastore_id: str  # query

    def as_request(self) -> (dict, dict):
        listProvidersRequest_query, listProvidersRequest_body = {}, {}
        if self.data_provider_global_metastore_id:
            listProvidersRequest_query[
                "data_provider_global_metastore_id"
            ] = self.data_provider_global_metastore_id

        return listProvidersRequest_query, listProvidersRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListProvidersRequest":
        return cls(
            data_provider_global_metastore_id=d.get(
                "data_provider_global_metastore_id", None
            ),
        )


@dataclass
class ListProvidersResponse:

    # An array of provider information objects.
    providers: "List[ProviderInfo]"

    def as_request(self) -> (dict, dict):
        listProvidersResponse_query, listProvidersResponse_body = {}, {}
        if self.providers:
            listProvidersResponse_body["providers"] = [
                v.as_request()[1] for v in self.providers
            ]

        return listProvidersResponse_query, listProvidersResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListProvidersResponse":
        return cls(
            providers=[ProviderInfo.from_dict(v) for v in d["providers"]]
            if "providers" in d
            else None,
        )


@dataclass
class ListRecipientsRequest:
    """List share recipients"""

    # If not provided, all recipients will be returned. If no recipients exist
    # with this ID, no results will be returned.
    data_recipient_global_metastore_id: str  # query

    def as_request(self) -> (dict, dict):
        listRecipientsRequest_query, listRecipientsRequest_body = {}, {}
        if self.data_recipient_global_metastore_id:
            listRecipientsRequest_query[
                "data_recipient_global_metastore_id"
            ] = self.data_recipient_global_metastore_id

        return listRecipientsRequest_query, listRecipientsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListRecipientsRequest":
        return cls(
            data_recipient_global_metastore_id=d.get(
                "data_recipient_global_metastore_id", None
            ),
        )


@dataclass
class ListRecipientsResponse:

    # An array of recipient information objects.
    recipients: "List[RecipientInfo]"

    def as_request(self) -> (dict, dict):
        listRecipientsResponse_query, listRecipientsResponse_body = {}, {}
        if self.recipients:
            listRecipientsResponse_body["recipients"] = [
                v.as_request()[1] for v in self.recipients
            ]

        return listRecipientsResponse_query, listRecipientsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListRecipientsResponse":
        return cls(
            recipients=[RecipientInfo.from_dict(v) for v in d["recipients"]]
            if "recipients" in d
            else None,
        )


@dataclass
class ListSchemasRequest:
    """List schemas"""

    # Optional. Parent catalog for schemas of interest.
    catalog_name: str  # query

    def as_request(self) -> (dict, dict):
        listSchemasRequest_query, listSchemasRequest_body = {}, {}
        if self.catalog_name:
            listSchemasRequest_query["catalog_name"] = self.catalog_name

        return listSchemasRequest_query, listSchemasRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListSchemasRequest":
        return cls(
            catalog_name=d.get("catalog_name", None),
        )


@dataclass
class ListSchemasResponse:

    # An array of schema information objects.
    schemas: "List[SchemaInfo]"

    def as_request(self) -> (dict, dict):
        listSchemasResponse_query, listSchemasResponse_body = {}, {}
        if self.schemas:
            listSchemasResponse_body["schemas"] = [
                v.as_request()[1] for v in self.schemas
            ]

        return listSchemasResponse_query, listSchemasResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListSchemasResponse":
        return cls(
            schemas=[SchemaInfo.from_dict(v) for v in d["schemas"]]
            if "schemas" in d
            else None,
        )


@dataclass
class ListSharesRequest:
    """List shares"""

    # Required. Name of the provider in which to list shares.
    name: str  # path

    def as_request(self) -> (dict, dict):
        listSharesRequest_query, listSharesRequest_body = {}, {}
        if self.name:
            listSharesRequest_body["name"] = self.name

        return listSharesRequest_query, listSharesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListSharesRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class ListSharesResponse:

    # An array of data share information objects.
    shares: "List[ShareInfo]"

    def as_request(self) -> (dict, dict):
        listSharesResponse_query, listSharesResponse_body = {}, {}
        if self.shares:
            listSharesResponse_body["shares"] = [v.as_request()[1] for v in self.shares]

        return listSharesResponse_query, listSharesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListSharesResponse":
        return cls(
            shares=[ShareInfo.from_dict(v) for v in d["shares"]]
            if "shares" in d
            else None,
        )


@dataclass
class ListStorageCredentialsResponse:

    storage_credentials: "List[StorageCredentialInfo]"

    def as_request(self) -> (dict, dict):
        listStorageCredentialsResponse_query, listStorageCredentialsResponse_body = (
            {},
            {},
        )
        if self.storage_credentials:
            listStorageCredentialsResponse_body["storage_credentials"] = [
                v.as_request()[1] for v in self.storage_credentials
            ]

        return listStorageCredentialsResponse_query, listStorageCredentialsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListStorageCredentialsResponse":
        return cls(
            storage_credentials=[
                StorageCredentialInfo.from_dict(v) for v in d["storage_credentials"]
            ]
            if "storage_credentials" in d
            else None,
        )


@dataclass
class ListTableSummariesResponse:

    # Optional. Opaque token for pagination. Empty if there's no more page.
    next_page_token: str
    # Only name, catalog_name, schema_name, full_name and table_type will be
    # set.
    tables: "List[TableSummary]"

    def as_request(self) -> (dict, dict):
        listTableSummariesResponse_query, listTableSummariesResponse_body = {}, {}
        if self.next_page_token:
            listTableSummariesResponse_body["next_page_token"] = self.next_page_token
        if self.tables:
            listTableSummariesResponse_body["tables"] = [
                v.as_request()[1] for v in self.tables
            ]

        return listTableSummariesResponse_query, listTableSummariesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListTableSummariesResponse":
        return cls(
            next_page_token=d.get("next_page_token", None),
            tables=[TableSummary.from_dict(v) for v in d["tables"]]
            if "tables" in d
            else None,
        )


@dataclass
class ListTablesRequest:
    """List tables"""

    # Required. Name of parent catalog for tables of interest.
    catalog_name: str  # query
    # Required (for now -- may be optional for wildcard search in future).
    # Parent schema of tables.
    schema_name: str  # query

    def as_request(self) -> (dict, dict):
        listTablesRequest_query, listTablesRequest_body = {}, {}
        if self.catalog_name:
            listTablesRequest_query["catalog_name"] = self.catalog_name
        if self.schema_name:
            listTablesRequest_query["schema_name"] = self.schema_name

        return listTablesRequest_query, listTablesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListTablesRequest":
        return cls(
            catalog_name=d.get("catalog_name", None),
            schema_name=d.get("schema_name", None),
        )


@dataclass
class ListTablesResponse:

    # An array of table information objects.
    tables: "List[TableInfo]"

    def as_request(self) -> (dict, dict):
        listTablesResponse_query, listTablesResponse_body = {}, {}
        if self.tables:
            listTablesResponse_body["tables"] = [v.as_request()[1] for v in self.tables]

        return listTablesResponse_query, listTablesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListTablesResponse":
        return cls(
            tables=[TableInfo.from_dict(v) for v in d["tables"]]
            if "tables" in d
            else None,
        )


@dataclass
class MetastoreInfo:

    # Time at which this Metastore was created, in epoch milliseconds.
    created_at: int
    # Username of Metastore creator.
    created_by: str
    # Unique identifier of (Default) Data Access Configuration
    default_data_access_config_id: str
    # Whether Delta Sharing is enabled on this metastore.
    delta_sharing_enabled: bool
    # The lifetime of delta sharing recipient token in seconds
    delta_sharing_recipient_token_lifetime_in_seconds: int
    # Unique identifier of Metastore.
    metastore_id: str
    # Name of Metastore.
    name: str
    # The owner of the metastore.
    owner: str
    # Privileges the user has on the Metastore.
    privileges: "List[Privilege]"
    # The region this metastore has an afinity to. This is used by
    # accounts-manager. Ignored by Unity Catalog.
    region: str
    # Storage root URL for Metastore
    storage_root: str
    # UUID of storage credential to access storage_root
    storage_root_credential_id: str
    # Time at which the Metastore was last modified, in epoch milliseconds.
    updated_at: int
    # Username of user who last modified the Metastore.
    updated_by: str

    def as_request(self) -> (dict, dict):
        metastoreInfo_query, metastoreInfo_body = {}, {}
        if self.created_at:
            metastoreInfo_body["created_at"] = self.created_at
        if self.created_by:
            metastoreInfo_body["created_by"] = self.created_by
        if self.default_data_access_config_id:
            metastoreInfo_body[
                "default_data_access_config_id"
            ] = self.default_data_access_config_id
        if self.delta_sharing_enabled:
            metastoreInfo_body["delta_sharing_enabled"] = self.delta_sharing_enabled
        if self.delta_sharing_recipient_token_lifetime_in_seconds:
            metastoreInfo_body[
                "delta_sharing_recipient_token_lifetime_in_seconds"
            ] = self.delta_sharing_recipient_token_lifetime_in_seconds
        if self.metastore_id:
            metastoreInfo_body["metastore_id"] = self.metastore_id
        if self.name:
            metastoreInfo_body["name"] = self.name
        if self.owner:
            metastoreInfo_body["owner"] = self.owner
        if self.privileges:
            metastoreInfo_body["privileges"] = [v for v in self.privileges]
        if self.region:
            metastoreInfo_body["region"] = self.region
        if self.storage_root:
            metastoreInfo_body["storage_root"] = self.storage_root
        if self.storage_root_credential_id:
            metastoreInfo_body[
                "storage_root_credential_id"
            ] = self.storage_root_credential_id
        if self.updated_at:
            metastoreInfo_body["updated_at"] = self.updated_at
        if self.updated_by:
            metastoreInfo_body["updated_by"] = self.updated_by

        return metastoreInfo_query, metastoreInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "MetastoreInfo":
        return cls(
            created_at=d.get("created_at", None),
            created_by=d.get("created_by", None),
            default_data_access_config_id=d.get("default_data_access_config_id", None),
            delta_sharing_enabled=d.get("delta_sharing_enabled", None),
            delta_sharing_recipient_token_lifetime_in_seconds=d.get(
                "delta_sharing_recipient_token_lifetime_in_seconds", None
            ),
            metastore_id=d.get("metastore_id", None),
            name=d.get("name", None),
            owner=d.get("owner", None),
            privileges=d.get("privileges", None),
            region=d.get("region", None),
            storage_root=d.get("storage_root", None),
            storage_root_credential_id=d.get("storage_root_credential_id", None),
            updated_at=d.get("updated_at", None),
            updated_by=d.get("updated_by", None),
        )


@dataclass
class Partition:

    # An array of partition values.
    values: "List[PartitionValue]"

    def as_request(self) -> (dict, dict):
        partition_query, partition_body = {}, {}
        if self.values:
            partition_body["values"] = [v.as_request()[1] for v in self.values]

        return partition_query, partition_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Partition":
        return cls(
            values=[PartitionValue.from_dict(v) for v in d["values"]]
            if "values" in d
            else None,
        )


@dataclass
class PartitionValue:

    # The name of the partition column.
    name: str
    # The operator to apply for the value.
    op: "PartitionValueOp"
    # The key of a Delta Sharing recipient's property. For example
    # "databricks-account-id". When this field is set, field `value` can not be
    # set.
    recipient_property_key: str
    # The value of the partition column. When this value is not set, it means
    # `null` value. When this field is set, field `recipient_property_key` can
    # not be set.
    value: str

    def as_request(self) -> (dict, dict):
        partitionValue_query, partitionValue_body = {}, {}
        if self.name:
            partitionValue_body["name"] = self.name
        if self.op:
            partitionValue_body["op"] = self.op.value
        if self.recipient_property_key:
            partitionValue_body["recipient_property_key"] = self.recipient_property_key
        if self.value:
            partitionValue_body["value"] = self.value

        return partitionValue_query, partitionValue_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PartitionValue":
        return cls(
            name=d.get("name", None),
            op=PartitionValueOp(d["op"]) if "op" in d else None,
            recipient_property_key=d.get("recipient_property_key", None),
            value=d.get("value", None),
        )


class PartitionValueOp(Enum):
    """The operator to apply for the value."""

    EQUAL = "EQUAL"
    LIKE = "LIKE"


@dataclass
class PermissionsChange:

    # The set of privileges to add.
    add: "List[Privilege]"
    # The principal whose privileges we are changing.
    principal: str
    # The set of privileges to remove.
    remove: "List[Privilege]"

    def as_request(self) -> (dict, dict):
        permissionsChange_query, permissionsChange_body = {}, {}
        if self.add:
            permissionsChange_body["add"] = [v for v in self.add]
        if self.principal:
            permissionsChange_body["principal"] = self.principal
        if self.remove:
            permissionsChange_body["remove"] = [v for v in self.remove]

        return permissionsChange_query, permissionsChange_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PermissionsChange":
        return cls(
            add=d.get("add", None),
            principal=d.get("principal", None),
            remove=d.get("remove", None),
        )


class Privilege(Enum):

    CREATE = "CREATE"
    CREATE_MOUNT = "CREATE_MOUNT"
    CREATE_TABLE = "CREATE_TABLE"
    MODIFY = "MODIFY"
    READ_FILES = "READ_FILES"
    SELECT = "SELECT"
    UNKNOWN_PRIVILEGE = "UNKNOWN_PRIVILEGE"
    USAGE = "USAGE"
    WRITE_FILES = "WRITE_FILES"


@dataclass
class PrivilegeAssignment:

    # The principal (user email address or group name).
    principal: str
    # The privileges assigned to the principal.
    privileges: "List[Privilege]"

    def as_request(self) -> (dict, dict):
        privilegeAssignment_query, privilegeAssignment_body = {}, {}
        if self.principal:
            privilegeAssignment_body["principal"] = self.principal
        if self.privileges:
            privilegeAssignment_body["privileges"] = [v for v in self.privileges]

        return privilegeAssignment_query, privilegeAssignment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PrivilegeAssignment":
        return cls(
            principal=d.get("principal", None),
            privileges=d.get("privileges", None),
        )


@dataclass
class ProviderInfo:

    # The delta sharing authentication type.
    authentication_type: "AuthenticationType"
    # Cloud vendor of the provider's UC Metastore. This field is only present
    # when the authentication type is `DATABRICKS`.
    cloud: str
    # Description about the provider.
    comment: str
    # Time at which this Provider was created, in epoch milliseconds.
    created_at: int
    # Username of Provider creator.
    created_by: str
    # The global UC metastore id of the data provider. This field is only
    # present when the authentication type is `DATABRICKS`. The identifier is of
    # format <cloud>:<region>:<metastore-uuid>.
    data_provider_global_metastore_id: str
    # UUID of the provider's UC Metastore. This field is only present when the
    # authentication type is `DATABRICKS`.
    metastore_id: str
    # The name of the Provider.
    name: str
    # Username of Provider owner.
    owner: str
    # This field is only present when the authentication type is TOKEN.
    recipient_profile: "RecipientProfile"
    # This field is only present when the authentication type is TOKEN.
    recipient_profile_str: str
    # Cloud region of the provider's UC Metastore. This field is only present
    # when the authentication type is `DATABRICKS`.
    region: str
    # Time at which this Provider was created, in epoch milliseconds.
    updated_at: int
    # Username of user who last modified Share.
    updated_by: str

    def as_request(self) -> (dict, dict):
        providerInfo_query, providerInfo_body = {}, {}
        if self.authentication_type:
            providerInfo_body["authentication_type"] = self.authentication_type.value
        if self.cloud:
            providerInfo_body["cloud"] = self.cloud
        if self.comment:
            providerInfo_body["comment"] = self.comment
        if self.created_at:
            providerInfo_body["created_at"] = self.created_at
        if self.created_by:
            providerInfo_body["created_by"] = self.created_by
        if self.data_provider_global_metastore_id:
            providerInfo_body[
                "data_provider_global_metastore_id"
            ] = self.data_provider_global_metastore_id
        if self.metastore_id:
            providerInfo_body["metastore_id"] = self.metastore_id
        if self.name:
            providerInfo_body["name"] = self.name
        if self.owner:
            providerInfo_body["owner"] = self.owner
        if self.recipient_profile:
            providerInfo_body[
                "recipient_profile"
            ] = self.recipient_profile.as_request()[1]
        if self.recipient_profile_str:
            providerInfo_body["recipient_profile_str"] = self.recipient_profile_str
        if self.region:
            providerInfo_body["region"] = self.region
        if self.updated_at:
            providerInfo_body["updated_at"] = self.updated_at
        if self.updated_by:
            providerInfo_body["updated_by"] = self.updated_by

        return providerInfo_query, providerInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ProviderInfo":
        return cls(
            authentication_type=AuthenticationType(d["authentication_type"])
            if "authentication_type" in d
            else None,
            cloud=d.get("cloud", None),
            comment=d.get("comment", None),
            created_at=d.get("created_at", None),
            created_by=d.get("created_by", None),
            data_provider_global_metastore_id=d.get(
                "data_provider_global_metastore_id", None
            ),
            metastore_id=d.get("metastore_id", None),
            name=d.get("name", None),
            owner=d.get("owner", None),
            recipient_profile=RecipientProfile.from_dict(d["recipient_profile"])
            if "recipient_profile" in d
            else None,
            recipient_profile_str=d.get("recipient_profile_str", None),
            region=d.get("region", None),
            updated_at=d.get("updated_at", None),
            updated_by=d.get("updated_by", None),
        )


@dataclass
class ProviderShare:

    # The name of the Provider Share.
    name: str

    def as_request(self) -> (dict, dict):
        providerShare_query, providerShare_body = {}, {}
        if self.name:
            providerShare_body["name"] = self.name

        return providerShare_query, providerShare_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ProviderShare":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class RecipientInfo:

    # A boolean status field showing whether the Recipient's activation URL has
    # been exercised or not.
    activated: bool
    # Full activation url to retrieve the access token. It will be empty if the
    # token is already retrieved.
    activation_url: str
    # The delta sharing authentication type.
    authentication_type: "AuthenticationType"
    # Description about the recipient.
    comment: str
    # Time at which this recipient was created, in epoch milliseconds.
    created_at: int
    # Username of recipient creator.
    created_by: str
    # IP Access List
    ip_access_list: "IpAccessList"
    # Name of Recipient.
    name: str
    # This field is only present when the authentication type is `TOKEN`.
    tokens: "List[RecipientTokenInfo]"
    # Time at which the recipient was updated, in epoch milliseconds.
    updated_at: int
    # Username of recipient updater.
    updated_by: str

    def as_request(self) -> (dict, dict):
        recipientInfo_query, recipientInfo_body = {}, {}
        if self.activated:
            recipientInfo_body["activated"] = self.activated
        if self.activation_url:
            recipientInfo_body["activation_url"] = self.activation_url
        if self.authentication_type:
            recipientInfo_body["authentication_type"] = self.authentication_type.value
        if self.comment:
            recipientInfo_body["comment"] = self.comment
        if self.created_at:
            recipientInfo_body["created_at"] = self.created_at
        if self.created_by:
            recipientInfo_body["created_by"] = self.created_by
        if self.ip_access_list:
            recipientInfo_body["ip_access_list"] = self.ip_access_list.as_request()[1]
        if self.name:
            recipientInfo_body["name"] = self.name
        if self.tokens:
            recipientInfo_body["tokens"] = [v.as_request()[1] for v in self.tokens]
        if self.updated_at:
            recipientInfo_body["updated_at"] = self.updated_at
        if self.updated_by:
            recipientInfo_body["updated_by"] = self.updated_by

        return recipientInfo_query, recipientInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RecipientInfo":
        return cls(
            activated=d.get("activated", None),
            activation_url=d.get("activation_url", None),
            authentication_type=AuthenticationType(d["authentication_type"])
            if "authentication_type" in d
            else None,
            comment=d.get("comment", None),
            created_at=d.get("created_at", None),
            created_by=d.get("created_by", None),
            ip_access_list=IpAccessList.from_dict(d["ip_access_list"])
            if "ip_access_list" in d
            else None,
            name=d.get("name", None),
            tokens=[RecipientTokenInfo.from_dict(v) for v in d["tokens"]]
            if "tokens" in d
            else None,
            updated_at=d.get("updated_at", None),
            updated_by=d.get("updated_by", None),
        )


@dataclass
class RecipientProfile:

    # The token used to authorize the recipient.
    bearer_token: str
    # The endpoint for the share to be used by the recipient.
    endpoint: str
    # The version number of the recipient's credentials on a share.
    share_credentials_version: int

    def as_request(self) -> (dict, dict):
        recipientProfile_query, recipientProfile_body = {}, {}
        if self.bearer_token:
            recipientProfile_body["bearer_token"] = self.bearer_token
        if self.endpoint:
            recipientProfile_body["endpoint"] = self.endpoint
        if self.share_credentials_version:
            recipientProfile_body[
                "share_credentials_version"
            ] = self.share_credentials_version

        return recipientProfile_query, recipientProfile_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RecipientProfile":
        return cls(
            bearer_token=d.get("bearer_token", None),
            endpoint=d.get("endpoint", None),
            share_credentials_version=d.get("share_credentials_version", None),
        )


@dataclass
class RecipientTokenInfo:

    # Full activation URL to retrieve the access token. It will be empty if the
    # token is already retrieved.
    activation_url: str
    # Time at which this recipient Token was created, in epoch milliseconds.
    created_at: int
    # Username of recipient token creator.
    created_by: str
    # Expiration timestamp of the token in epoch milliseconds.
    expiration_time: int
    # Unique ID of the recipient token.
    id: str
    # Time at which this recipient Token was updated, in epoch milliseconds.
    updated_at: int
    # Username of recipient Token updater.
    updated_by: str

    def as_request(self) -> (dict, dict):
        recipientTokenInfo_query, recipientTokenInfo_body = {}, {}
        if self.activation_url:
            recipientTokenInfo_body["activation_url"] = self.activation_url
        if self.created_at:
            recipientTokenInfo_body["created_at"] = self.created_at
        if self.created_by:
            recipientTokenInfo_body["created_by"] = self.created_by
        if self.expiration_time:
            recipientTokenInfo_body["expiration_time"] = self.expiration_time
        if self.id:
            recipientTokenInfo_body["id"] = self.id
        if self.updated_at:
            recipientTokenInfo_body["updated_at"] = self.updated_at
        if self.updated_by:
            recipientTokenInfo_body["updated_by"] = self.updated_by

        return recipientTokenInfo_query, recipientTokenInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RecipientTokenInfo":
        return cls(
            activation_url=d.get("activation_url", None),
            created_at=d.get("created_at", None),
            created_by=d.get("created_by", None),
            expiration_time=d.get("expiration_time", None),
            id=d.get("id", None),
            updated_at=d.get("updated_at", None),
            updated_by=d.get("updated_by", None),
        )


@dataclass
class RetrieveTokenRequest:
    """Get an access token"""

    # Required. The one time activation url. It also accepts activation token.
    activation_url: str  # path

    def as_request(self) -> (dict, dict):
        retrieveTokenRequest_query, retrieveTokenRequest_body = {}, {}
        if self.activation_url:
            retrieveTokenRequest_body["activation_url"] = self.activation_url

        return retrieveTokenRequest_query, retrieveTokenRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RetrieveTokenRequest":
        return cls(
            activation_url=d.get("activation_url", None),
        )


@dataclass
class RetrieveTokenResponse:

    # The token used to authorize the recipient.
    bearerToken: str
    # The endpoint for the share to be used by the recipient.
    endpoint: str
    # Expiration timestamp of the token in epoch milliseconds.
    expirationTime: str
    # These field names must follow the delta sharing protocol.
    shareCredentialsVersion: int

    def as_request(self) -> (dict, dict):
        retrieveTokenResponse_query, retrieveTokenResponse_body = {}, {}
        if self.bearerToken:
            retrieveTokenResponse_body["bearerToken"] = self.bearerToken
        if self.endpoint:
            retrieveTokenResponse_body["endpoint"] = self.endpoint
        if self.expirationTime:
            retrieveTokenResponse_body["expirationTime"] = self.expirationTime
        if self.shareCredentialsVersion:
            retrieveTokenResponse_body[
                "shareCredentialsVersion"
            ] = self.shareCredentialsVersion

        return retrieveTokenResponse_query, retrieveTokenResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RetrieveTokenResponse":
        return cls(
            bearerToken=d.get("bearerToken", None),
            endpoint=d.get("endpoint", None),
            expirationTime=d.get("expirationTime", None),
            shareCredentialsVersion=d.get("shareCredentialsVersion", None),
        )


@dataclass
class RotateRecipientToken:

    # Required. This will set the expiration_time of existing token only to a
    # smaller timestamp, it cannot extend the expiration_time. Use 0 to expire
    # the existing token immediately, negative number will return an error.
    existing_token_expire_in_seconds: int
    # Required. The name of the recipient.
    name: str  # path

    def as_request(self) -> (dict, dict):
        rotateRecipientToken_query, rotateRecipientToken_body = {}, {}
        if self.existing_token_expire_in_seconds:
            rotateRecipientToken_body[
                "existing_token_expire_in_seconds"
            ] = self.existing_token_expire_in_seconds
        if self.name:
            rotateRecipientToken_body["name"] = self.name

        return rotateRecipientToken_query, rotateRecipientToken_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RotateRecipientToken":
        return cls(
            existing_token_expire_in_seconds=d.get(
                "existing_token_expire_in_seconds", None
            ),
            name=d.get("name", None),
        )


@dataclass
class SchemaInfo:

    # Name of parent Catalog.
    catalog_name: str
    # User-provided free-form text description.
    comment: str
    # Time at which this Schema was created, in epoch milliseconds.
    created_at: int
    # Username of Schema creator.
    created_by: str
    # Full name of Schema, in form of <catalog_name>.<schema_name>.
    full_name: str
    # Unique identifier of parent Metastore.
    metastore_id: str
    # Name of Schema, relative to parent Catalog.
    name: str
    # Username of current owner of Schema.
    owner: str
    # Privileges the user has on the Schema.
    privileges: "List[Privilege]"

    properties: "Dict[str,str]"
    # Time at which this Schema was created, in epoch milliseconds.
    updated_at: int
    # Username of user who last modified Schema.
    updated_by: str

    def as_request(self) -> (dict, dict):
        schemaInfo_query, schemaInfo_body = {}, {}
        if self.catalog_name:
            schemaInfo_body["catalog_name"] = self.catalog_name
        if self.comment:
            schemaInfo_body["comment"] = self.comment
        if self.created_at:
            schemaInfo_body["created_at"] = self.created_at
        if self.created_by:
            schemaInfo_body["created_by"] = self.created_by
        if self.full_name:
            schemaInfo_body["full_name"] = self.full_name
        if self.metastore_id:
            schemaInfo_body["metastore_id"] = self.metastore_id
        if self.name:
            schemaInfo_body["name"] = self.name
        if self.owner:
            schemaInfo_body["owner"] = self.owner
        if self.privileges:
            schemaInfo_body["privileges"] = [v for v in self.privileges]
        if self.properties:
            schemaInfo_body["properties"] = self.properties
        if self.updated_at:
            schemaInfo_body["updated_at"] = self.updated_at
        if self.updated_by:
            schemaInfo_body["updated_by"] = self.updated_by

        return schemaInfo_query, schemaInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SchemaInfo":
        return cls(
            catalog_name=d.get("catalog_name", None),
            comment=d.get("comment", None),
            created_at=d.get("created_at", None),
            created_by=d.get("created_by", None),
            full_name=d.get("full_name", None),
            metastore_id=d.get("metastore_id", None),
            name=d.get("name", None),
            owner=d.get("owner", None),
            privileges=d.get("privileges", None),
            properties=d.get("properties", None),
            updated_at=d.get("updated_at", None),
            updated_by=d.get("updated_by", None),
        )


@dataclass
class ShareInfo:

    # comment when creating the share
    comment: str
    # Time at which this Share was created, in epoch milliseconds.
    created_at: int
    # Username of Share creator.
    created_by: str
    # Name of the Share.
    name: str
    # A list of shared data objects within the Share.
    objects: "List[SharedDataObject]"
    # Username of current owner of credential.
    owner: str

    def as_request(self) -> (dict, dict):
        shareInfo_query, shareInfo_body = {}, {}
        if self.comment:
            shareInfo_body["comment"] = self.comment
        if self.created_at:
            shareInfo_body["created_at"] = self.created_at
        if self.created_by:
            shareInfo_body["created_by"] = self.created_by
        if self.name:
            shareInfo_body["name"] = self.name
        if self.objects:
            shareInfo_body["objects"] = [v.as_request()[1] for v in self.objects]
        if self.owner:
            shareInfo_body["owner"] = self.owner

        return shareInfo_query, shareInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ShareInfo":
        return cls(
            comment=d.get("comment", None),
            created_at=d.get("created_at", None),
            created_by=d.get("created_by", None),
            name=d.get("name", None),
            objects=[SharedDataObject.from_dict(v) for v in d["objects"]]
            if "objects" in d
            else None,
            owner=d.get("owner", None),
        )


@dataclass
class SharePermissionsRequest:
    """Get share permissions"""

    # Required. The name of the Recipient.
    name: str  # path

    def as_request(self) -> (dict, dict):
        sharePermissionsRequest_query, sharePermissionsRequest_body = {}, {}
        if self.name:
            sharePermissionsRequest_body["name"] = self.name

        return sharePermissionsRequest_query, sharePermissionsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SharePermissionsRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class ShareToPrivilegeAssignment:

    # The privileges assigned to the principal.
    privilege_assignments: "List[PrivilegeAssignment]"
    # The share name.
    share_name: str

    def as_request(self) -> (dict, dict):
        shareToPrivilegeAssignment_query, shareToPrivilegeAssignment_body = {}, {}
        if self.privilege_assignments:
            shareToPrivilegeAssignment_body["privilege_assignments"] = [
                v.as_request()[1] for v in self.privilege_assignments
            ]
        if self.share_name:
            shareToPrivilegeAssignment_body["share_name"] = self.share_name

        return shareToPrivilegeAssignment_query, shareToPrivilegeAssignment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ShareToPrivilegeAssignment":
        return cls(
            privilege_assignments=[
                PrivilegeAssignment.from_dict(v) for v in d["privilege_assignments"]
            ]
            if "privilege_assignments" in d
            else None,
            share_name=d.get("share_name", None),
        )


@dataclass
class SharedDataObject:

    # The time when this data object is added to the Share, in epoch
    # milliseconds.
    added_at: int
    # Username of the sharer.
    added_by: str
    # Whether to enable cdf or indicate if cdf is enabled on the shared object.
    cdf_enabled: bool
    # A user-provided comment when adding the data object to the share.
    # [Update:OPT]
    comment: str
    # The type of the data object.
    data_object_type: str
    # A fully qualified name that uniquely identifies a data object.
    #
    # For example, a table's fully qualified name is in the format of
    # `<catalog>.<schema>.<table>`.
    name: str
    # Array of partitions for the shared data.
    partitions: "List[Partition]"
    # A user-provided new name for the data object within the share. If this new
    # name is not not provided, the object's original name will be used as the
    # `shared_as` name. The `shared_as` name must be unique within a Share. For
    # tables, the new name must follow the format of `<schema>.<table>`.
    shared_as: str
    # The start version associated with the object. This allows data providers
    # to control the lowest object version that is accessible by clients. If
    # specified, clients can query snapshots or changes for versions >=
    # start_version. If not specified, clients can only query starting from the
    # version of the object at the time it was added to the share.
    #
    # NOTE: The start_version should be <= the \"current\" version of the
    # object.
    start_version: int
    # One of: **ACTIVE**, **PERMISSION_DENIED**.
    status: "SharedDataObjectStatus"

    def as_request(self) -> (dict, dict):
        sharedDataObject_query, sharedDataObject_body = {}, {}
        if self.added_at:
            sharedDataObject_body["added_at"] = self.added_at
        if self.added_by:
            sharedDataObject_body["added_by"] = self.added_by
        if self.cdf_enabled:
            sharedDataObject_body["cdf_enabled"] = self.cdf_enabled
        if self.comment:
            sharedDataObject_body["comment"] = self.comment
        if self.data_object_type:
            sharedDataObject_body["data_object_type"] = self.data_object_type
        if self.name:
            sharedDataObject_body["name"] = self.name
        if self.partitions:
            sharedDataObject_body["partitions"] = [
                v.as_request()[1] for v in self.partitions
            ]
        if self.shared_as:
            sharedDataObject_body["shared_as"] = self.shared_as
        if self.start_version:
            sharedDataObject_body["start_version"] = self.start_version
        if self.status:
            sharedDataObject_body["status"] = self.status.value

        return sharedDataObject_query, sharedDataObject_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SharedDataObject":
        return cls(
            added_at=d.get("added_at", None),
            added_by=d.get("added_by", None),
            cdf_enabled=d.get("cdf_enabled", None),
            comment=d.get("comment", None),
            data_object_type=d.get("data_object_type", None),
            name=d.get("name", None),
            partitions=[Partition.from_dict(v) for v in d["partitions"]]
            if "partitions" in d
            else None,
            shared_as=d.get("shared_as", None),
            start_version=d.get("start_version", None),
            status=SharedDataObjectStatus(d["status"]) if "status" in d else None,
        )


class SharedDataObjectStatus(Enum):
    """One of: **ACTIVE**, **PERMISSION_DENIED**."""

    ACTIVE = "ACTIVE"
    PERMISSION_DENIED = "PERMISSION_DENIED"


@dataclass
class SharedDataObjectUpdate:

    # One of: **ADD**, **REMOVE**, **UPDATE**.
    action: "SharedDataObjectUpdateAction"
    # The data object that is being added, removed, or updated.
    data_object: "SharedDataObject"

    def as_request(self) -> (dict, dict):
        sharedDataObjectUpdate_query, sharedDataObjectUpdate_body = {}, {}
        if self.action:
            sharedDataObjectUpdate_body["action"] = self.action.value
        if self.data_object:
            sharedDataObjectUpdate_body["data_object"] = self.data_object.as_request()[
                1
            ]

        return sharedDataObjectUpdate_query, sharedDataObjectUpdate_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SharedDataObjectUpdate":
        return cls(
            action=SharedDataObjectUpdateAction(d["action"]) if "action" in d else None,
            data_object=SharedDataObject.from_dict(d["data_object"])
            if "data_object" in d
            else None,
        )


class SharedDataObjectUpdateAction(Enum):
    """One of: **ADD**, **REMOVE**, **UPDATE**."""

    ADD = "ADD"
    REMOVE = "REMOVE"
    UPDATE = "UPDATE"


@dataclass
class StorageCredentialInfo:

    # The AWS IAM role configuration.
    aws_iam_role: "AwsIamRole"
    # The Azure service principal configuration.
    azure_service_principal: "AzureServicePrincipal"
    # Comment associated with the credential.
    comment: str
    # Time at which this Credential was created, in epoch milliseconds.
    created_at: int
    # Username of credential creator.
    created_by: str
    # The GCP service account key configuration.
    gcp_service_account_key: "GcpServiceAccountKey"
    # The unique identifier of the credential.
    id: str
    # Unique identifier of parent Metastore.
    metastore_id: str
    # The credential name. The name MUST be unique within the Metastore.
    name: str
    # Optional. Supplying true to this argument skips validation of the created
    # set of credentials.
    skip_validation: bool
    # Time at which this credential was last modified, in epoch milliseconds.
    updated_at: int
    # Username of user who last modified the credential.
    updated_by: str

    def as_request(self) -> (dict, dict):
        storageCredentialInfo_query, storageCredentialInfo_body = {}, {}
        if self.aws_iam_role:
            storageCredentialInfo_body["aws_iam_role"] = self.aws_iam_role.as_request()[
                1
            ]
        if self.azure_service_principal:
            storageCredentialInfo_body[
                "azure_service_principal"
            ] = self.azure_service_principal.as_request()[1]
        if self.comment:
            storageCredentialInfo_body["comment"] = self.comment
        if self.created_at:
            storageCredentialInfo_body["created_at"] = self.created_at
        if self.created_by:
            storageCredentialInfo_body["created_by"] = self.created_by
        if self.gcp_service_account_key:
            storageCredentialInfo_body[
                "gcp_service_account_key"
            ] = self.gcp_service_account_key.as_request()[1]
        if self.id:
            storageCredentialInfo_body["id"] = self.id
        if self.metastore_id:
            storageCredentialInfo_body["metastore_id"] = self.metastore_id
        if self.name:
            storageCredentialInfo_body["name"] = self.name
        if self.skip_validation:
            storageCredentialInfo_body["skip_validation"] = self.skip_validation
        if self.updated_at:
            storageCredentialInfo_body["updated_at"] = self.updated_at
        if self.updated_by:
            storageCredentialInfo_body["updated_by"] = self.updated_by

        return storageCredentialInfo_query, storageCredentialInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "StorageCredentialInfo":
        return cls(
            aws_iam_role=AwsIamRole.from_dict(d["aws_iam_role"])
            if "aws_iam_role" in d
            else None,
            azure_service_principal=AzureServicePrincipal.from_dict(
                d["azure_service_principal"]
            )
            if "azure_service_principal" in d
            else None,
            comment=d.get("comment", None),
            created_at=d.get("created_at", None),
            created_by=d.get("created_by", None),
            gcp_service_account_key=GcpServiceAccountKey.from_dict(
                d["gcp_service_account_key"]
            )
            if "gcp_service_account_key" in d
            else None,
            id=d.get("id", None),
            metastore_id=d.get("metastore_id", None),
            name=d.get("name", None),
            skip_validation=d.get("skip_validation", None),
            updated_at=d.get("updated_at", None),
            updated_by=d.get("updated_by", None),
        )


@dataclass
class TableInfo:

    # Name of parent Catalog.
    catalog_name: str
    # This name ('columns') is what the client actually sees as the field name
    # in messages that include PropertiesKVPairs using 'json_inline' (e.g.,
    # TableInfo).
    columns: "List[ColumnInfo]"
    # User-provided free-form text description.
    comment: str
    # Time at which this Table was created, in epoch milliseconds.
    created_at: int
    # Username of Table creator.
    created_by: str
    # Unique ID of the data_access_configuration to use.
    data_access_configuration_id: str
    # Data source format
    data_source_format: "DataSourceFormat"
    # Full name of Table, in form of <catalog_name>.<schema_name>.<table_name>
    full_name: str
    # Unique identifier of parent Metastore.
    metastore_id: str
    # Name of Table, relative to parent Schema.
    name: str
    # Username of current owner of Table.
    owner: str
    # Privileges the user has on the Table.
    privileges: "List[Privilege]"

    properties: "Dict[str,str]"
    # Name of parent Schema relative to its parent Catalog.
    schema_name: str
    # List of schemes whose objects can be referenced without qualification.
    sql_path: str
    # Name of the storage credential this table used
    storage_credential_name: str
    # Storage root URL for table (for MANAGED, EXTERNAL tables)
    storage_location: str
    # Name of Table, relative to parent Schema.
    table_id: str

    table_type: "TableType"
    # Time at which this Table was last modified, in epoch milliseconds.
    updated_at: int
    # Username of user who last modified the Table.
    updated_by: str
    # View definition SQL (when table_type == "VIEW")
    view_definition: str

    def as_request(self) -> (dict, dict):
        tableInfo_query, tableInfo_body = {}, {}
        if self.catalog_name:
            tableInfo_body["catalog_name"] = self.catalog_name
        if self.columns:
            tableInfo_body["columns"] = [v.as_request()[1] for v in self.columns]
        if self.comment:
            tableInfo_body["comment"] = self.comment
        if self.created_at:
            tableInfo_body["created_at"] = self.created_at
        if self.created_by:
            tableInfo_body["created_by"] = self.created_by
        if self.data_access_configuration_id:
            tableInfo_body[
                "data_access_configuration_id"
            ] = self.data_access_configuration_id
        if self.data_source_format:
            tableInfo_body["data_source_format"] = self.data_source_format.value
        if self.full_name:
            tableInfo_body["full_name"] = self.full_name
        if self.metastore_id:
            tableInfo_body["metastore_id"] = self.metastore_id
        if self.name:
            tableInfo_body["name"] = self.name
        if self.owner:
            tableInfo_body["owner"] = self.owner
        if self.privileges:
            tableInfo_body["privileges"] = [v for v in self.privileges]
        if self.properties:
            tableInfo_body["properties"] = self.properties
        if self.schema_name:
            tableInfo_body["schema_name"] = self.schema_name
        if self.sql_path:
            tableInfo_body["sql_path"] = self.sql_path
        if self.storage_credential_name:
            tableInfo_body["storage_credential_name"] = self.storage_credential_name
        if self.storage_location:
            tableInfo_body["storage_location"] = self.storage_location
        if self.table_id:
            tableInfo_body["table_id"] = self.table_id
        if self.table_type:
            tableInfo_body["table_type"] = self.table_type.value
        if self.updated_at:
            tableInfo_body["updated_at"] = self.updated_at
        if self.updated_by:
            tableInfo_body["updated_by"] = self.updated_by
        if self.view_definition:
            tableInfo_body["view_definition"] = self.view_definition

        return tableInfo_query, tableInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TableInfo":
        return cls(
            catalog_name=d.get("catalog_name", None),
            columns=[ColumnInfo.from_dict(v) for v in d["columns"]]
            if "columns" in d
            else None,
            comment=d.get("comment", None),
            created_at=d.get("created_at", None),
            created_by=d.get("created_by", None),
            data_access_configuration_id=d.get("data_access_configuration_id", None),
            data_source_format=DataSourceFormat(d["data_source_format"])
            if "data_source_format" in d
            else None,
            full_name=d.get("full_name", None),
            metastore_id=d.get("metastore_id", None),
            name=d.get("name", None),
            owner=d.get("owner", None),
            privileges=d.get("privileges", None),
            properties=d.get("properties", None),
            schema_name=d.get("schema_name", None),
            sql_path=d.get("sql_path", None),
            storage_credential_name=d.get("storage_credential_name", None),
            storage_location=d.get("storage_location", None),
            table_id=d.get("table_id", None),
            table_type=TableType(d["table_type"]) if "table_type" in d else None,
            updated_at=d.get("updated_at", None),
            updated_by=d.get("updated_by", None),
            view_definition=d.get("view_definition", None),
        )


@dataclass
class TableSummariesRequest:
    """List table summaries"""

    # Required. Name of parent catalog for tables of interest.
    catalog_name: str  # query
    # Optional. Maximum number of tables to return (page length). Defaults to
    # 10000.
    max_results: int  # query
    # Optional. Opaque token to send for the next page of results (pagination).
    page_token: str  # query
    # Optional. A sql LIKE pattern (% and _) for schema names. All schemas will
    # be returned if not set or empty.
    schema_name_pattern: str  # query
    # Optional. A sql LIKE pattern (% and _) for table names. All tables will be
    # returned if not set or empty.
    table_name_pattern: str  # query

    def as_request(self) -> (dict, dict):
        tableSummariesRequest_query, tableSummariesRequest_body = {}, {}
        if self.catalog_name:
            tableSummariesRequest_query["catalog_name"] = self.catalog_name
        if self.max_results:
            tableSummariesRequest_query["max_results"] = self.max_results
        if self.page_token:
            tableSummariesRequest_query["page_token"] = self.page_token
        if self.schema_name_pattern:
            tableSummariesRequest_query[
                "schema_name_pattern"
            ] = self.schema_name_pattern
        if self.table_name_pattern:
            tableSummariesRequest_query["table_name_pattern"] = self.table_name_pattern

        return tableSummariesRequest_query, tableSummariesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TableSummariesRequest":
        return cls(
            catalog_name=d.get("catalog_name", None),
            max_results=d.get("max_results", None),
            page_token=d.get("page_token", None),
            schema_name_pattern=d.get("schema_name_pattern", None),
            table_name_pattern=d.get("table_name_pattern", None),
        )


@dataclass
class TableSummary:

    # The full name of the table.
    full_name: str

    table_type: "TableType"

    def as_request(self) -> (dict, dict):
        tableSummary_query, tableSummary_body = {}, {}
        if self.full_name:
            tableSummary_body["full_name"] = self.full_name
        if self.table_type:
            tableSummary_body["table_type"] = self.table_type.value

        return tableSummary_query, tableSummary_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TableSummary":
        return cls(
            full_name=d.get("full_name", None),
            table_type=TableType(d["table_type"]) if "table_type" in d else None,
        )


class TableType(Enum):

    EXTERNAL = "EXTERNAL"
    MANAGED = "MANAGED"
    UNKNOWN_TABLE_TYPE = "UNKNOWN_TABLE_TYPE"
    VIEW = "VIEW"


@dataclass
class UnassignRequest:
    """Delete an assignment"""

    # Query for the ID of the Metastore to delete.
    metastore_id: str  # query
    # A workspace ID.
    workspace_id: int  # path

    def as_request(self) -> (dict, dict):
        unassignRequest_query, unassignRequest_body = {}, {}
        if self.metastore_id:
            unassignRequest_query["metastore_id"] = self.metastore_id
        if self.workspace_id:
            unassignRequest_body["workspace_id"] = self.workspace_id

        return unassignRequest_query, unassignRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UnassignRequest":
        return cls(
            metastore_id=d.get("metastore_id", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class UpdateCatalog:

    # User-provided free-form text description.
    comment: str
    # Name of Catalog.
    name: str  # path
    # Username of current owner of Catalog.
    owner: str

    properties: "Dict[str,str]"

    def as_request(self) -> (dict, dict):
        updateCatalog_query, updateCatalog_body = {}, {}
        if self.comment:
            updateCatalog_body["comment"] = self.comment
        if self.name:
            updateCatalog_body["name"] = self.name
        if self.owner:
            updateCatalog_body["owner"] = self.owner
        if self.properties:
            updateCatalog_body["properties"] = self.properties

        return updateCatalog_query, updateCatalog_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateCatalog":
        return cls(
            comment=d.get("comment", None),
            name=d.get("name", None),
            owner=d.get("owner", None),
            properties=d.get("properties", None),
        )


@dataclass
class UpdateExternalLocation:

    # User-provided free-form text description.
    comment: str
    # Current name of the Storage Credential this location uses.
    credential_name: str
    # Force update even if changing url invalidates dependent external tables or
    # mounts.
    force: bool
    # Name of the External Location.
    name: str  # path
    # The owner of the External Location.
    owner: str
    # Path URL of the External Location.
    url: str

    def as_request(self) -> (dict, dict):
        updateExternalLocation_query, updateExternalLocation_body = {}, {}
        if self.comment:
            updateExternalLocation_body["comment"] = self.comment
        if self.credential_name:
            updateExternalLocation_body["credential_name"] = self.credential_name
        if self.force:
            updateExternalLocation_body["force"] = self.force
        if self.name:
            updateExternalLocation_body["name"] = self.name
        if self.owner:
            updateExternalLocation_body["owner"] = self.owner
        if self.url:
            updateExternalLocation_body["url"] = self.url

        return updateExternalLocation_query, updateExternalLocation_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateExternalLocation":
        return cls(
            comment=d.get("comment", None),
            credential_name=d.get("credential_name", None),
            force=d.get("force", None),
            name=d.get("name", None),
            owner=d.get("owner", None),
            url=d.get("url", None),
        )


@dataclass
class UpdateMetastore:

    # Unique identifier of (Default) Data Access Configuration
    default_data_access_config_id: str
    # Whether Delta Sharing is enabled on this metastore.
    delta_sharing_enabled: bool
    # The lifetime of delta sharing recipient token in seconds
    delta_sharing_recipient_token_lifetime_in_seconds: int
    # Required. Unique ID of the Metastore (from URL).
    id: str  # path
    # Name of Metastore.
    name: str
    # The owner of the metastore.
    owner: str
    # UUID of storage credential to access storage_root
    storage_root_credential_id: str

    def as_request(self) -> (dict, dict):
        updateMetastore_query, updateMetastore_body = {}, {}
        if self.default_data_access_config_id:
            updateMetastore_body[
                "default_data_access_config_id"
            ] = self.default_data_access_config_id
        if self.delta_sharing_enabled:
            updateMetastore_body["delta_sharing_enabled"] = self.delta_sharing_enabled
        if self.delta_sharing_recipient_token_lifetime_in_seconds:
            updateMetastore_body[
                "delta_sharing_recipient_token_lifetime_in_seconds"
            ] = self.delta_sharing_recipient_token_lifetime_in_seconds
        if self.id:
            updateMetastore_body["id"] = self.id
        if self.name:
            updateMetastore_body["name"] = self.name
        if self.owner:
            updateMetastore_body["owner"] = self.owner
        if self.storage_root_credential_id:
            updateMetastore_body[
                "storage_root_credential_id"
            ] = self.storage_root_credential_id

        return updateMetastore_query, updateMetastore_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateMetastore":
        return cls(
            default_data_access_config_id=d.get("default_data_access_config_id", None),
            delta_sharing_enabled=d.get("delta_sharing_enabled", None),
            delta_sharing_recipient_token_lifetime_in_seconds=d.get(
                "delta_sharing_recipient_token_lifetime_in_seconds", None
            ),
            id=d.get("id", None),
            name=d.get("name", None),
            owner=d.get("owner", None),
            storage_root_credential_id=d.get("storage_root_credential_id", None),
        )


@dataclass
class UpdateMetastoreAssignment:

    # The name of the default catalog for the Metastore.
    default_catalog_name: str
    # The unique ID of the Metastore.
    metastore_id: str
    # A workspace ID.
    workspace_id: int  # path

    def as_request(self) -> (dict, dict):
        updateMetastoreAssignment_query, updateMetastoreAssignment_body = {}, {}
        if self.default_catalog_name:
            updateMetastoreAssignment_body[
                "default_catalog_name"
            ] = self.default_catalog_name
        if self.metastore_id:
            updateMetastoreAssignment_body["metastore_id"] = self.metastore_id
        if self.workspace_id:
            updateMetastoreAssignment_body["workspace_id"] = self.workspace_id

        return updateMetastoreAssignment_query, updateMetastoreAssignment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateMetastoreAssignment":
        return cls(
            default_catalog_name=d.get("default_catalog_name", None),
            metastore_id=d.get("metastore_id", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class UpdatePermissions:

    # Array of permissions change objects.
    changes: "List[PermissionsChange]"
    # Required. Unique identifier (full name) of Securable (from URL).
    full_name: str  # path
    # Optional. List permissions granted to this principal.
    principal: str  # query
    # Required. Type of Securable (from URL).
    securable_type: str  # path

    def as_request(self) -> (dict, dict):
        updatePermissions_query, updatePermissions_body = {}, {}
        if self.changes:
            updatePermissions_body["changes"] = [
                v.as_request()[1] for v in self.changes
            ]
        if self.full_name:
            updatePermissions_body["full_name"] = self.full_name
        if self.principal:
            updatePermissions_query["principal"] = self.principal
        if self.securable_type:
            updatePermissions_body["securable_type"] = self.securable_type

        return updatePermissions_query, updatePermissions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdatePermissions":
        return cls(
            changes=[PermissionsChange.from_dict(v) for v in d["changes"]]
            if "changes" in d
            else None,
            full_name=d.get("full_name", None),
            principal=d.get("principal", None),
            securable_type=d.get("securable_type", None),
        )


@dataclass
class UpdateProvider:

    # The delta sharing authentication type.
    authentication_type: "AuthenticationType"
    # Description about the provider.
    comment: str
    # The name of the Provider.
    name: str  # path
    # Username of Provider owner.
    owner: str
    # This field is only present when the authentication type is TOKEN.
    recipient_profile: "RecipientProfile"
    # This field is only present when the authentication type is TOKEN.
    recipient_profile_str: str

    def as_request(self) -> (dict, dict):
        updateProvider_query, updateProvider_body = {}, {}
        if self.authentication_type:
            updateProvider_body["authentication_type"] = self.authentication_type.value
        if self.comment:
            updateProvider_body["comment"] = self.comment
        if self.name:
            updateProvider_body["name"] = self.name
        if self.owner:
            updateProvider_body["owner"] = self.owner
        if self.recipient_profile:
            updateProvider_body[
                "recipient_profile"
            ] = self.recipient_profile.as_request()[1]
        if self.recipient_profile_str:
            updateProvider_body["recipient_profile_str"] = self.recipient_profile_str

        return updateProvider_query, updateProvider_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateProvider":
        return cls(
            authentication_type=AuthenticationType(d["authentication_type"])
            if "authentication_type" in d
            else None,
            comment=d.get("comment", None),
            name=d.get("name", None),
            owner=d.get("owner", None),
            recipient_profile=RecipientProfile.from_dict(d["recipient_profile"])
            if "recipient_profile" in d
            else None,
            recipient_profile_str=d.get("recipient_profile_str", None),
        )


@dataclass
class UpdateRecipient:

    # The delta sharing authentication type.
    authentication_type: "AuthenticationType"
    # Description about the recipient.
    comment: str
    # IP Access List
    ip_access_list: "IpAccessList"
    # Name of Recipient.
    name: str  # path

    def as_request(self) -> (dict, dict):
        updateRecipient_query, updateRecipient_body = {}, {}
        if self.authentication_type:
            updateRecipient_body["authentication_type"] = self.authentication_type.value
        if self.comment:
            updateRecipient_body["comment"] = self.comment
        if self.ip_access_list:
            updateRecipient_body["ip_access_list"] = self.ip_access_list.as_request()[1]
        if self.name:
            updateRecipient_body["name"] = self.name

        return updateRecipient_query, updateRecipient_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateRecipient":
        return cls(
            authentication_type=AuthenticationType(d["authentication_type"])
            if "authentication_type" in d
            else None,
            comment=d.get("comment", None),
            ip_access_list=IpAccessList.from_dict(d["ip_access_list"])
            if "ip_access_list" in d
            else None,
            name=d.get("name", None),
        )


@dataclass
class UpdateSchema:

    # Name of parent Catalog.
    catalog_name: str
    # User-provided free-form text description.
    comment: str
    # Required. Full name of the schema (from URL).
    full_name: str  # path
    # Name of Schema, relative to parent Catalog.
    name: str
    # Username of current owner of Schema.
    owner: str

    properties: "Dict[str,str]"

    def as_request(self) -> (dict, dict):
        updateSchema_query, updateSchema_body = {}, {}
        if self.catalog_name:
            updateSchema_body["catalog_name"] = self.catalog_name
        if self.comment:
            updateSchema_body["comment"] = self.comment
        if self.full_name:
            updateSchema_body["full_name"] = self.full_name
        if self.name:
            updateSchema_body["name"] = self.name
        if self.owner:
            updateSchema_body["owner"] = self.owner
        if self.properties:
            updateSchema_body["properties"] = self.properties

        return updateSchema_query, updateSchema_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateSchema":
        return cls(
            catalog_name=d.get("catalog_name", None),
            comment=d.get("comment", None),
            full_name=d.get("full_name", None),
            name=d.get("name", None),
            owner=d.get("owner", None),
            properties=d.get("properties", None),
        )


@dataclass
class UpdateShare:

    # The name of the share.
    name: str  # path
    # Array of shared data object updates.
    updates: "List[SharedDataObjectUpdate]"

    def as_request(self) -> (dict, dict):
        updateShare_query, updateShare_body = {}, {}
        if self.name:
            updateShare_body["name"] = self.name
        if self.updates:
            updateShare_body["updates"] = [v.as_request()[1] for v in self.updates]

        return updateShare_query, updateShare_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateShare":
        return cls(
            name=d.get("name", None),
            updates=[SharedDataObjectUpdate.from_dict(v) for v in d["updates"]]
            if "updates" in d
            else None,
        )


@dataclass
class UpdateSharePermissions:

    # Array of permission changes.
    changes: "List[PermissionsChange]"
    # Required. The name of the share.
    name: str  # path

    def as_request(self) -> (dict, dict):
        updateSharePermissions_query, updateSharePermissions_body = {}, {}
        if self.changes:
            updateSharePermissions_body["changes"] = [
                v.as_request()[1] for v in self.changes
            ]
        if self.name:
            updateSharePermissions_body["name"] = self.name

        return updateSharePermissions_query, updateSharePermissions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateSharePermissions":
        return cls(
            changes=[PermissionsChange.from_dict(v) for v in d["changes"]]
            if "changes" in d
            else None,
            name=d.get("name", None),
        )


@dataclass
class UpdateStorageCredential:

    # The AWS IAM role configuration.
    aws_iam_role: "AwsIamRole"
    # The Azure service principal configuration.
    azure_service_principal: "AzureServicePrincipal"
    # Comment associated with the credential.
    comment: str
    # The GCP service account key configuration.
    gcp_service_account_key: "GcpServiceAccountKey"
    # The credential name. The name MUST be unique within the Metastore.
    name: str  # path
    # Username of current owner of credential.
    owner: str

    def as_request(self) -> (dict, dict):
        updateStorageCredential_query, updateStorageCredential_body = {}, {}
        if self.aws_iam_role:
            updateStorageCredential_body[
                "aws_iam_role"
            ] = self.aws_iam_role.as_request()[1]
        if self.azure_service_principal:
            updateStorageCredential_body[
                "azure_service_principal"
            ] = self.azure_service_principal.as_request()[1]
        if self.comment:
            updateStorageCredential_body["comment"] = self.comment
        if self.gcp_service_account_key:
            updateStorageCredential_body[
                "gcp_service_account_key"
            ] = self.gcp_service_account_key.as_request()[1]
        if self.name:
            updateStorageCredential_body["name"] = self.name
        if self.owner:
            updateStorageCredential_body["owner"] = self.owner

        return updateStorageCredential_query, updateStorageCredential_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateStorageCredential":
        return cls(
            aws_iam_role=AwsIamRole.from_dict(d["aws_iam_role"])
            if "aws_iam_role" in d
            else None,
            azure_service_principal=AzureServicePrincipal.from_dict(
                d["azure_service_principal"]
            )
            if "azure_service_principal" in d
            else None,
            comment=d.get("comment", None),
            gcp_service_account_key=GcpServiceAccountKey.from_dict(
                d["gcp_service_account_key"]
            )
            if "gcp_service_account_key" in d
            else None,
            name=d.get("name", None),
            owner=d.get("owner", None),
        )


class CatalogsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateCatalog) -> CatalogInfo:
        """Create a catalog.

        Creates a new catalog instance in the parent Metastore if the caller is
        a Metastore admin or has the CREATE CATALOG privilege."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.1/unity-catalog/catalogs", query=query, body=body
        )
        return CatalogInfo.from_dict(json)

    def delete(self, request: DeleteCatalogRequest):
        """Delete a catalog.

        Deletes the catalog that matches the supplied name. The caller must be a
        Metastore admin or the owner of the catalog."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.1/unity-catalog/catalogs/{request.name}",
            query=query,
            body=body,
        )

    def get(self, request: GetCatalogRequest) -> CatalogInfo:
        """Get a catalog.

        Gets an array of all catalogs in the current Metastore for which the
        user is an admin or Catalog owner, or has the USAGE privilege set for
        their account."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/catalogs/{request.name}",
            query=query,
            body=body,
        )
        return CatalogInfo.from_dict(json)

    def list(self) -> ListCatalogsResponse:
        """List catalogs.

        Gets an array of External Locations (ExternalLocationInfo objects) from
        the Metastore. The caller must be a Metastore admin, is the owner of the
        External Location, or has privileges to access the External Location."""

        json = self._api.do("GET", "/api/2.1/unity-catalog/catalogs")
        return ListCatalogsResponse.from_dict(json)

    def update(self, request: UpdateCatalog):
        """Update a catalog.

        Updates the catalog that matches the supplied name. The caller must be
        either the owner of the catalog, or a Metastore admin (when changing the
        owner field of the catalog)."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.1/unity-catalog/catalogs/{request.name}",
            query=query,
            body=body,
        )


class ExternalLocationsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateExternalLocation) -> ExternalLocationInfo:
        """Create an external location.

        Creates a new External Location entry in the Metastore. The caller must
        be a Metastore admin or have the CREATE EXTERNAL LOCATION privilege on
        the Metastore."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.1/unity-catalog/external-locations", query=query, body=body
        )
        return ExternalLocationInfo.from_dict(json)

    def delete(self, request: DeleteExternalLocationRequest):
        """Delete an external location.

        Deletes the specified external location from the Metastore. The caller
        must be the owner of the external location."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.1/unity-catalog/external-locations/{request.name}",
            query=query,
            body=body,
        )

    def get(self, request: GetExternalLocationRequest) -> ExternalLocationInfo:
        """Get an external location.

        Gets an external location from the Metastore. The caller must be either
        a Metastore admin, the owner of the external location, or has an
        appropriate privilege level on the Metastore."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/external-locations/{request.name}",
            query=query,
            body=body,
        )
        return ExternalLocationInfo.from_dict(json)

    def list(self) -> ListExternalLocationsResponse:
        """List external locations.

        Gets an array of External Locations (ExternalLocationInfo objects) from
        the Metastore. The caller must be a Metastore admin, is the owner of the
        external location, or has privileges to access the external location."""

        json = self._api.do("GET", "/api/2.1/unity-catalog/external-locations")
        return ListExternalLocationsResponse.from_dict(json)

    def update(self, request: UpdateExternalLocation):
        """Update an external location.

        Updates an external location in the Metastore. The caller must be the
        owner of the externa location, or be a Metastore admin. In the second
        case, the admin can only update the name of the external location."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.1/unity-catalog/external-locations/{request.name}",
            query=query,
            body=body,
        )


class GrantsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def get(self, request: GetGrantRequest) -> GetPermissionsResponse:
        """Get permissions.

        Gets the permissions for a Securable type."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/permissions/{request.securable_type}/{request.full_name}",
            query=query,
            body=body,
        )
        return GetPermissionsResponse.from_dict(json)

    def update(self, request: UpdatePermissions):
        """Update permissions.

        Updates the permissions for a Securable type."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.1/unity-catalog/permissions/{request.securable_type}/{request.full_name}",
            query=query,
            body=body,
        )


class MetastoresAPI:
    def __init__(self, api_client):
        self._api = api_client

    def assign(self, request: CreateMetastoreAssignment):
        """Create an assignment.

        Creates a new Metastore assignment. If an assignment for the same
        __workspace_id__ exists, it will be overwritten by the new
        __metastore_id__ and __default_catalog_name__. The caller must be an
        account admin."""
        query, body = request.as_request()
        self._api.do(
            "PUT",
            f"/api/2.1/unity-catalog/workspaces/{request.workspace_id}/metastore",
            query=query,
            body=body,
        )

    def create(self, request: CreateMetastore) -> MetastoreInfo:
        """Create a Metastore.

        Creates a new Metastore based on a provided name and storage root path."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.1/unity-catalog/metastores", query=query, body=body
        )
        return MetastoreInfo.from_dict(json)

    def delete(self, request: DeleteMetastoreRequest):
        """Delete a Metastore.

        Deletes a Metastore. The caller must be a Metastore admin."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.1/unity-catalog/metastores/{request.id}",
            query=query,
            body=body,
        )

    def get(self, request: GetMetastoreRequest) -> MetastoreInfo:
        """Get a Metastore.

        Gets a Metastore that matches the supplied ID. The caller must be a
        Metastore admin to retrieve this info."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/metastores/{request.id}",
            query=query,
            body=body,
        )
        return MetastoreInfo.from_dict(json)

    def list(self) -> ListMetastoresResponse:
        """List Metastores.

        Gets an array of the available Metastores (as MetastoreInfo objects).
        The caller must be an admin to retrieve this info."""

        json = self._api.do("GET", "/api/2.1/unity-catalog/metastores")
        return ListMetastoresResponse.from_dict(json)

    def summary(self) -> GetMetastoreSummaryResponse:
        """Get a summary.

        Gets information about a Metastore. This summary includes the storage
        credential, the cloud vendor, the cloud region, and the global Metastore
        ID."""

        json = self._api.do("GET", "/api/2.1/unity-catalog/metastore_summary")
        return GetMetastoreSummaryResponse.from_dict(json)

    def unassign(self, request: UnassignRequest):
        """Delete an assignment.

        Deletes a Metastore assignment. The caller must be an account
        administrator."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.1/unity-catalog/workspaces/{request.workspace_id}/metastore",
            query=query,
            body=body,
        )

    def update(self, request: UpdateMetastore):
        """Update a Metastore.

        Updates information for a specific Metastore. The caller must be a
        Metastore admin."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.1/unity-catalog/metastores/{request.id}",
            query=query,
            body=body,
        )

    def update_assignment(self, request: UpdateMetastoreAssignment):
        """Update an assignment.

        Updates a Metastore assignment. This operation can be used to update
        __metastore_id__ or __default_catalog_name__ for a specified Workspace,
        if the Workspace is already assigned a Metastore. The caller must be an
        account admin to update __metastore_id__; otherwise, the caller can be a
        Workspace admin."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.1/unity-catalog/workspaces/{request.workspace_id}/metastore",
            query=query,
            body=body,
        )


class ProvidersAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateProvider) -> ProviderInfo:
        """Create an auth provider.

        Creates a new authentication provider minimally based on a name and
        authentication type. The caller must be an admin on the Metastore."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.1/unity-catalog/providers", query=query, body=body
        )
        return ProviderInfo.from_dict(json)

    def delete(self, request: DeleteProviderRequest):
        """Delete a provider.

        Deletes an authentication provider, if the caller is a Metastore admin
        or is the owner of the provider."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.1/unity-catalog/providers/{request.name}",
            query=query,
            body=body,
        )

    def get(self, request: GetProviderRequest) -> ProviderInfo:
        """Get a provider.

        Gets a specific authentication provider. The caller must supply the name
        of the provider, and must either be a Metastore admin or the owner of
        the provider."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/providers/{request.name}",
            query=query,
            body=body,
        )
        return ProviderInfo.from_dict(json)

    def list(self, request: ListProvidersRequest) -> ListProvidersResponse:
        """List providers.

        Gets an array of available authentication providers. The caller must
        either be a Metastore admin or the owner of the providers. Providers not
        owned by the caller are not included in the response."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.1/unity-catalog/providers", query=query, body=body
        )
        return ListProvidersResponse.from_dict(json)

    def list_shares(self, request: ListSharesRequest) -> ListProviderSharesResponse:
        """List shares.

        Gets an array of all shares within the Metastore where:

        * the caller is a Metastore admin, or * the caller is the owner."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/providers/{request.name}/shares",
            query=query,
            body=body,
        )
        return ListProviderSharesResponse.from_dict(json)

    def update(self, request: UpdateProvider):
        """Update a provider.

        Updates the information for an authentication provider, if the caller is
        a Metastore admin or is the owner of the provider. If the update changes
        the provider name, the caller must be both a Metastore admin and the
        owner of the provider."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.1/unity-catalog/providers/{request.name}",
            query=query,
            body=body,
        )


class RecipientActivationAPI:
    def __init__(self, api_client):
        self._api = api_client

    def get_activation_url_info(self, request: GetActivationUrlInfoRequest):
        """Get a share activation URL.

        Gets information about an Activation URL."""
        query, body = request.as_request()
        self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/public/data_sharing_activation_info/{request.activation_url}",
            query=query,
            body=body,
        )

    def retrieve_token(self, request: RetrieveTokenRequest) -> RetrieveTokenResponse:
        """Get an access token.

        RPC to retrieve access token with an activation token. This is a public
        API without any authentication."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/public/data_sharing_activation/{request.activation_url}",
            query=query,
            body=body,
        )
        return RetrieveTokenResponse.from_dict(json)


class RecipientsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateRecipient) -> RecipientInfo:
        """Create a share recipient.

        Creates a new recipient with the delta sharing authentication type in
        the Metastore. The caller must be a Metastore admin or has the CREATE
        RECIPIENT privilege on the Metastore."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.1/unity-catalog/recipients", query=query, body=body
        )
        return RecipientInfo.from_dict(json)

    def delete(self, request: DeleteRecipientRequest):
        """Delete a share recipient.

        Deletes the specified recipient from the Metastore. The caller must be
        the owner of the recipient."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.1/unity-catalog/recipients/{request.name}",
            query=query,
            body=body,
        )

    def get(self, request: GetRecipientRequest) -> RecipientInfo:
        """Get a share recipient.

        Gets a share recipient from the Metastore if:

        * the caller is the owner of the share recipient, or: * is a Metastore
        admin"""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/recipients/{request.name}",
            query=query,
            body=body,
        )
        return RecipientInfo.from_dict(json)

    def list(self, request: ListRecipientsRequest) -> ListRecipientsResponse:
        """List share recipients.

        Gets an array of all share recipients within the current Metastore
        where:

        * the caller is a Metastore admin, or * the caller is the owner."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.1/unity-catalog/recipients", query=query, body=body
        )
        return ListRecipientsResponse.from_dict(json)

    def rotate_token(self, request: RotateRecipientToken) -> RecipientInfo:
        """Rotate a token.

        Refreshes the specified recipient's delta sharing authentication token
        with the provided token info. The caller must be the owner of the
        recipient."""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            f"/api/2.1/unity-catalog/recipients/{request.name}/rotate-token",
            query=query,
            body=body,
        )
        return RecipientInfo.from_dict(json)

    def share_permissions(
        self, request: SharePermissionsRequest
    ) -> GetRecipientSharePermissionsResponse:
        """Get share permissions.

        Gets the share permissions for the specified Recipient. The caller must
        be a Metastore admin or the owner of the Recipient."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/recipients/{request.name}/share-permissions",
            query=query,
            body=body,
        )
        return GetRecipientSharePermissionsResponse.from_dict(json)

    def update(self, request: UpdateRecipient):
        """Update a share recipient.

        Updates an existing recipient in the Metastore. The caller must be a
        Metastore admin or the owner of the recipient. If the recipient name
        will be updated, the user must be both a Metastore admin and the owner
        of the recipient."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.1/unity-catalog/recipients/{request.name}",
            query=query,
            body=body,
        )


class SchemasAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateSchema) -> SchemaInfo:
        """Create a schema.

        Creates a new schema for catalog in the Metatastore. The caller must be
        a Metastore admin, or have the CREATE privilege in the parentcatalog."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.1/unity-catalog/schemas", query=query, body=body
        )
        return SchemaInfo.from_dict(json)

    def delete(self, request: DeleteSchemaRequest):
        """Delete a schema.

        Deletes the specified schema from the parent catalog. The caller must be
        the owner of the schema or an owner of the parent catalog."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.1/unity-catalog/schemas/{request.full_name}",
            query=query,
            body=body,
        )

    def get(self, request: GetSchemaRequest) -> SchemaInfo:
        """Get a schema.

        Gets the specified schema for a catalog in the Metastore. The caller
        must be a Metastore admin, the owner of the schema, or a user that has
        the USAGE privilege on the schema."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/schemas/{request.full_name}",
            query=query,
            body=body,
        )
        return SchemaInfo.from_dict(json)

    def list(self, request: ListSchemasRequest) -> ListSchemasResponse:
        """List schemas.

        Gets an array of schemas for catalog in the Metastore. If the caller is
        the Metastore admin or the owner of the parent catalog, all schemas for
        the catalog will be retrieved. Otherwise, only schemas owned by the
        caller (or for which the caller has the USAGE privilege) will be
        retrieved."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.1/unity-catalog/schemas", query=query, body=body
        )
        return ListSchemasResponse.from_dict(json)

    def update(self, request: UpdateSchema):
        """Update a schema.

        Updates a schema for a catalog. The caller must be the owner of the
        schema. If the caller is a Metastore admin, only the __owner__ field can
        be changed in the update. If the __name__ field must be updated, the
        caller must be a Metastore admin or have the CREATE privilege on the
        parent catalog."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.1/unity-catalog/schemas/{request.full_name}",
            query=query,
            body=body,
        )


class SharesAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateShare) -> ShareInfo:
        """Create a share.

        Creates a new share for data objects. Data objects can be added at this
        time or after creation with **update**. The caller must be a Metastore
        admin or have the CREATE SHARE privilege on the Metastore."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.1/unity-catalog/shares", query=query, body=body
        )
        return ShareInfo.from_dict(json)

    def delete(self, request: DeleteShareRequest):
        """Delete a share.

        Deletes a data object share from the Metastore. The caller must be an
        owner of the share."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.1/unity-catalog/shares/{request.name}",
            query=query,
            body=body,
        )

    def get(self, request: GetShareRequest) -> ShareInfo:
        """Get a share.

        Gets a data object share from the Metastore. The caller must be a
        Metastore admin or the owner of the share."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/shares/{request.name}",
            query=query,
            body=body,
        )
        return ShareInfo.from_dict(json)

    def list(self) -> ListSharesResponse:
        """List shares.

        Gets an array of data object shares from the Metastore. The caller must
        be a Metastore admin or the owner of the share."""

        json = self._api.do("GET", "/api/2.1/unity-catalog/shares")
        return ListSharesResponse.from_dict(json)

    def share_permissions(
        self, request: SharePermissionsRequest
    ) -> GetSharePermissionsResponse:
        """Get permissions.

        Gets the permissions for a data share from the Metastore. The caller
        must be a Metastore admin or the owner of the share."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/shares/{request.name}/permissions",
            query=query,
            body=body,
        )
        return GetSharePermissionsResponse.from_dict(json)

    def update(self, request: UpdateShare):
        """Update a share.

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
        self._api.do(
            "PATCH",
            f"/api/2.1/unity-catalog/shares/{request.name}",
            query=query,
            body=body,
        )

    def update_permissions(self, request: UpdateSharePermissions):
        """Update permissions.

        Updates the permissions for a data share in the Metastore. The caller
        must be a Metastore admin or an owner of the share.

        For new recipient grants, the user must also be the owner of the
        recipients. recipient revocations do not require additional privileges."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.1/unity-catalog/shares/{request.name}/permissions",
            query=query,
            body=body,
        )


class StorageCredentialsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateStorageCredential) -> StorageCredentialInfo:
        """Create credentials.

        Creates a new storage credential. The request object is specific to the
        cloud:

        * **AwsIamRole** for AWS credentials * **AzureServicePrincipal** for
        Azure credentials * **GcpServiceAcountKey** for GCP credentials.

        The caller must be a Metastore admin and have the CREATE STORAGE
        CREDENTIAL privilege on the Metastore."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.1/unity-catalog/storage-credentials", query=query, body=body
        )
        return StorageCredentialInfo.from_dict(json)

    def delete(self, request: DeleteStorageCredentialRequest):
        """Delete a credential.

        Deletes a storage credential from the Metastore. The caller must be an
        owner of the storage credential."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.1/unity-catalog/storage-credentials/{request.name}",
            query=query,
            body=body,
        )

    def get(self, request: GetStorageCredentialRequest) -> StorageCredentialInfo:
        """Get a credential.

        Gets a storage credential from the Metastore. The caller must be a
        Metastore admin, the owner of the storage credential, or have a level of
        privilege on the storage credential."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/storage-credentials/{request.name}",
            query=query,
            body=body,
        )
        return StorageCredentialInfo.from_dict(json)

    def list(self) -> ListStorageCredentialsResponse:
        """List credentials.

        Gets an array of storage credentials (as StorageCredentialInfo objects).
        The array is limited to only those storage credentials the caller has
        the privilege level to access. If the caller is a Metastore admin, all
        storage credentials will be retrieved."""

        json = self._api.do("GET", "/api/2.1/unity-catalog/storage-credentials")
        return ListStorageCredentialsResponse.from_dict(json)

    def update(self, request: UpdateStorageCredential):
        """Update a credential.

        Updates a storage credential on the Metastore. The caller must be the
        owner of the storage credential. If the caller is a Metastore admin,
        only the __owner__ credential can be changed."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.1/unity-catalog/storage-credentials/{request.name}",
            query=query,
            body=body,
        )


class TablesAPI:
    def __init__(self, api_client):
        self._api = api_client

    def delete(self, request: DeleteTableRequest):
        """Delete a table.

        Deletes a table from the specified parent catalog and schema. The caller
        must be the owner of the parent catalog, have the USAGE privilege on the
        parent catalog and be the owner of the parent schema, or be the owner of
        the table and have the USAGE privilege on both the parent catalog and
        schema."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.1/unity-catalog/tables/{request.full_name}",
            query=query,
            body=body,
        )

    def get(self, request: GetTableRequest) -> TableInfo:
        """Get a table.

        Gets a table from the Metastore for a specific catalog and schema. The
        caller must be a Metastore admin, be the owner of the table and have the
        USAGE privilege on both the parent catalog and schema, or be the owner
        of the table and have the SELECT privilege on it as well."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.1/unity-catalog/tables/{request.full_name}",
            query=query,
            body=body,
        )
        return TableInfo.from_dict(json)

    def list(self, request: ListTablesRequest) -> ListTablesResponse:
        """List tables.

        Gets an array of all tables for the current Metastore under the parent
        catalog and schema. The caller must be a Metastore admin or an owner of
        (or have the SELECT privilege on) the table. For the latter case, the
        caller must also be the owner or have the USAGE privilege on the parent
        catalog and schema."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.1/unity-catalog/tables", query=query, body=body
        )
        return ListTablesResponse.from_dict(json)

    def table_summaries(
        self, request: TableSummariesRequest
    ) -> ListTableSummariesResponse:
        """List table summaries.

        Gets an array of summaries for tables for a schema and catalog within
        the Metastore. The table summaries returned are either:

        * summaries for all tables (within the current Metastore and parent
        catalog and schema), when the user is a Metastore admin, or: * summaries
        for all tables and schemas (within the current Metastore and parent
        catalog) for which the user has ownership or the SELECT privilege on the
        Table and ownership or USAGE privilege on the Schema, provided that the
        user also has ownership or the USAGE privilege on the parent Catalog"""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.1/unity-catalog/table-summaries", query=query, body=body
        )
        return ListTableSummariesResponse.from_dict(json)

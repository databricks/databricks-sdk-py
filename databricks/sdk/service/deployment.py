# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class AwsCredentials:

    sts_role: "StsRole"

    def as_request(self) -> (dict, dict):
        awsCredentials_query, awsCredentials_body = {}, {}
        if self.sts_role:
            awsCredentials_body["sts_role"] = self.sts_role.as_request()[1]

        return awsCredentials_query, awsCredentials_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "AwsCredentials":
        return cls(
            sts_role=StsRole.from_dict(d["sts_role"]) if "sts_role" in d else None,
        )


@dataclass
class AwsKeyInfo:

    # The AWS KMS key alias.
    key_alias: str
    # The AWS KMS key's Amazon Resource Name (ARN).
    key_arn: str
    # The AWS KMS key region.
    key_region: str
    # This field applies only if the `use_cases` property includes `STORAGE`. If
    # this is set to `true` or omitted, the key is also used to encrypt cluster
    # EBS volumes. If you do not want to use this key for encrypting EBS
    # volumes, set to `false`.
    reuse_key_for_cluster_volumes: bool

    def as_request(self) -> (dict, dict):
        awsKeyInfo_query, awsKeyInfo_body = {}, {}
        if self.key_alias:
            awsKeyInfo_body["key_alias"] = self.key_alias
        if self.key_arn:
            awsKeyInfo_body["key_arn"] = self.key_arn
        if self.key_region:
            awsKeyInfo_body["key_region"] = self.key_region
        if self.reuse_key_for_cluster_volumes:
            awsKeyInfo_body[
                "reuse_key_for_cluster_volumes"
            ] = self.reuse_key_for_cluster_volumes

        return awsKeyInfo_query, awsKeyInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "AwsKeyInfo":
        return cls(
            key_alias=d.get("key_alias", None),
            key_arn=d.get("key_arn", None),
            key_region=d.get("key_region", None),
            reuse_key_for_cluster_volumes=d.get("reuse_key_for_cluster_volumes", None),
        )


@dataclass
class CloudResourceBucket:
    """The general workspace configurations that are specific to cloud providers."""

    # The general workspace configurations that are specific to Google Cloud.
    gcp: "GcpProjectContainer"

    def as_request(self) -> (dict, dict):
        cloudResourceBucket_query, cloudResourceBucket_body = {}, {}
        if self.gcp:
            cloudResourceBucket_body["gcp"] = self.gcp.as_request()[1]

        return cloudResourceBucket_query, cloudResourceBucket_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CloudResourceBucket":
        return cls(
            gcp=GcpProjectContainer.from_dict(d["gcp"]) if "gcp" in d else None,
        )


@dataclass
class CreateAwsKeyInfo:

    # The AWS KMS key alias.
    key_alias: str
    # The AWS KMS key's Amazon Resource Name (ARN). Note that the key's AWS
    # region is inferred from the ARN.
    key_arn: str
    # This field applies only if the `use_cases` property includes `STORAGE`. If
    # this is set to `true` or omitted, the key is also used to encrypt cluster
    # EBS volumes. To not use this key also for encrypting EBS volumes, set this
    # to `false`.
    reuse_key_for_cluster_volumes: bool

    def as_request(self) -> (dict, dict):
        createAwsKeyInfo_query, createAwsKeyInfo_body = {}, {}
        if self.key_alias:
            createAwsKeyInfo_body["key_alias"] = self.key_alias
        if self.key_arn:
            createAwsKeyInfo_body["key_arn"] = self.key_arn
        if self.reuse_key_for_cluster_volumes:
            createAwsKeyInfo_body[
                "reuse_key_for_cluster_volumes"
            ] = self.reuse_key_for_cluster_volumes

        return createAwsKeyInfo_query, createAwsKeyInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateAwsKeyInfo":
        return cls(
            key_alias=d.get("key_alias", None),
            key_arn=d.get("key_arn", None),
            reuse_key_for_cluster_volumes=d.get("reuse_key_for_cluster_volumes", None),
        )


@dataclass
class CreateCredentialRequest:

    aws_credentials: "AwsCredentials"
    # The human-readable name of the credential configuration object.
    credentials_name: str

    def as_request(self) -> (dict, dict):
        createCredentialRequest_query, createCredentialRequest_body = {}, {}
        if self.aws_credentials:
            createCredentialRequest_body[
                "aws_credentials"
            ] = self.aws_credentials.as_request()[1]
        if self.credentials_name:
            createCredentialRequest_body["credentials_name"] = self.credentials_name

        return createCredentialRequest_query, createCredentialRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateCredentialRequest":
        return cls(
            aws_credentials=AwsCredentials.from_dict(d["aws_credentials"])
            if "aws_credentials" in d
            else None,
            credentials_name=d.get("credentials_name", None),
        )


@dataclass
class CreateCustomerManagedKeyRequest:

    aws_key_info: "CreateAwsKeyInfo"
    # The cases that the key can be used for.
    use_cases: "List[KeyUseCase]"

    def as_request(self) -> (dict, dict):
        createCustomerManagedKeyRequest_query, createCustomerManagedKeyRequest_body = (
            {},
            {},
        )
        if self.aws_key_info:
            createCustomerManagedKeyRequest_body[
                "aws_key_info"
            ] = self.aws_key_info.as_request()[1]
        if self.use_cases:
            createCustomerManagedKeyRequest_body["use_cases"] = [
                v for v in self.use_cases
            ]

        return (
            createCustomerManagedKeyRequest_query,
            createCustomerManagedKeyRequest_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateCustomerManagedKeyRequest":
        return cls(
            aws_key_info=CreateAwsKeyInfo.from_dict(d["aws_key_info"])
            if "aws_key_info" in d
            else None,
            use_cases=d.get("use_cases", None),
        )


@dataclass
class CreateGcpNetwork:
    """The network configurations for the workspace. If you provide a network
    configuration ID for a new workspace, Databricks deploys the new workspace
    into that associated customer-managed VPC. If omitted, by default Databricks
    creates a new Databricks-managed VPC for the workspace in your Google
    account and manages its lifecycle.

    All the IP range configurations must be mutually exclusive. An attempt to
    create a workspace fails if Databricks detects an IP range overlap.

    Specify custom IP ranges in CIDR format. The IP ranges for these fields must
    not overlap, and all IP addresses must be entirely within the following
    ranges: `10.0.0.0/8`, `100.64.0.0/10`, `172.16.0.0/12`, `192.168.0.0/16`,
    and `240.0.0.0/4`.

    The sizes of these IP ranges affect the maximum number of nodes for the
    workspace.

    **Important**: Confirm the IP ranges used by your Databricks workspace
    before creating the workspace. You cannot change them after your workspace
    is deployed. If the IP address ranges for your Databricks are too small, IP
    exhaustion can occur, causing your Databricks jobs to fail. To determine the
    address range sizes that you need, Databricks provides a calculator as a
    Microsoft Excel spreadsheet. See [calculate subnet sizes for a new
    workspace].

    [calculate subnet sizes for a new workspace]: https://docs.gcp.databricks.com/administration-guide/cloud-configurations/gcp/network-sizing.html"""

    # The common network configuration fields that can be used by both
    # Databricks-managed VPCs and customer-managed VPCs.
    gcp_common_network_config: "GcpCommonNetworkConfig"
    # The network settings for the workspace. The configurations are only for
    # Databricks-managed VPCs. It is ignored if you specify a customer-managed
    # VPC in the `network_id` field.
    gcp_managed_network_config: "GcpManagedNetworkConfig"
    # The network configuration ID that is attached to the workspace. If you
    # provide a network configuration ID for a new workspace, Databricks
    # validates the network resources and deploys the new workspace into your
    # associated customer-managed VPC that is specified in this network
    # configuration. If omitted, by default Databricks creates a new
    # Databricks-managed VPC for the workspace in your Google account and
    # manages its lifecycle.
    network_id: str

    def as_request(self) -> (dict, dict):
        createGcpNetwork_query, createGcpNetwork_body = {}, {}
        if self.gcp_common_network_config:
            createGcpNetwork_body[
                "gcp_common_network_config"
            ] = self.gcp_common_network_config.as_request()[1]
        if self.gcp_managed_network_config:
            createGcpNetwork_body[
                "gcp_managed_network_config"
            ] = self.gcp_managed_network_config.as_request()[1]
        if self.network_id:
            createGcpNetwork_body["network_id"] = self.network_id

        return createGcpNetwork_query, createGcpNetwork_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateGcpNetwork":
        return cls(
            gcp_common_network_config=GcpCommonNetworkConfig.from_dict(
                d["gcp_common_network_config"]
            )
            if "gcp_common_network_config" in d
            else None,
            gcp_managed_network_config=GcpManagedNetworkConfig.from_dict(
                d["gcp_managed_network_config"]
            )
            if "gcp_managed_network_config" in d
            else None,
            network_id=d.get("network_id", None),
        )


@dataclass
class CreateNetworkRequest:

    # The Google Cloud specific information for this network (for example, the
    # VPC ID, subnet ID, and secondary IP ranges).
    gcp_network_info: "GcpNetworkInfo"
    # The human-readable name of the network configuration.
    network_name: str
    # IDs of one to five security groups associated with this network. Security
    # group IDs **cannot** be used in multiple network configurations.
    security_group_ids: "List[str]"
    # IDs of at least two subnets associated with this network. Subnet IDs
    # **cannot** be used in multiple network configurations.
    subnet_ids: "List[str]"
    # If specified, contains the VPC endpoints used to allow cluster
    # communication from this VPC over [AWS PrivateLink].
    #
    # [AWS PrivateLink]: https://aws.amazon.com/privatelink/
    vpc_endpoints: "NetworkVpcEndpoints"
    # The ID of the VPC associated with this network. VPC IDs can be used in
    # multiple network configurations.
    vpc_id: str

    def as_request(self) -> (dict, dict):
        createNetworkRequest_query, createNetworkRequest_body = {}, {}
        if self.gcp_network_info:
            createNetworkRequest_body[
                "gcp_network_info"
            ] = self.gcp_network_info.as_request()[1]
        if self.network_name:
            createNetworkRequest_body["network_name"] = self.network_name
        if self.security_group_ids:
            createNetworkRequest_body["security_group_ids"] = [
                v for v in self.security_group_ids
            ]
        if self.subnet_ids:
            createNetworkRequest_body["subnet_ids"] = [v for v in self.subnet_ids]
        if self.vpc_endpoints:
            createNetworkRequest_body[
                "vpc_endpoints"
            ] = self.vpc_endpoints.as_request()[1]
        if self.vpc_id:
            createNetworkRequest_body["vpc_id"] = self.vpc_id

        return createNetworkRequest_query, createNetworkRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateNetworkRequest":
        return cls(
            gcp_network_info=GcpNetworkInfo.from_dict(d["gcp_network_info"])
            if "gcp_network_info" in d
            else None,
            network_name=d.get("network_name", None),
            security_group_ids=d.get("security_group_ids", None),
            subnet_ids=d.get("subnet_ids", None),
            vpc_endpoints=NetworkVpcEndpoints.from_dict(d["vpc_endpoints"])
            if "vpc_endpoints" in d
            else None,
            vpc_id=d.get("vpc_id", None),
        )


@dataclass
class CreateStorageConfigurationRequest:

    # Root S3 bucket information.
    root_bucket_info: "RootBucketInfo"
    # The human-readable name of the storage configuration.
    storage_configuration_name: str

    def as_request(self) -> (dict, dict):
        (
            createStorageConfigurationRequest_query,
            createStorageConfigurationRequest_body,
        ) = ({}, {})
        if self.root_bucket_info:
            createStorageConfigurationRequest_body[
                "root_bucket_info"
            ] = self.root_bucket_info.as_request()[1]
        if self.storage_configuration_name:
            createStorageConfigurationRequest_body[
                "storage_configuration_name"
            ] = self.storage_configuration_name

        return (
            createStorageConfigurationRequest_query,
            createStorageConfigurationRequest_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateStorageConfigurationRequest":
        return cls(
            root_bucket_info=RootBucketInfo.from_dict(d["root_bucket_info"])
            if "root_bucket_info" in d
            else None,
            storage_configuration_name=d.get("storage_configuration_name", None),
        )


@dataclass
class CreateVpcEndpointRequest:

    # The ID of the VPC endpoint object in AWS.
    aws_vpc_endpoint_id: str
    # The AWS region in which this VPC endpoint object exists.
    region: str
    # The human-readable name of the storage configuration.
    vpc_endpoint_name: str

    def as_request(self) -> (dict, dict):
        createVpcEndpointRequest_query, createVpcEndpointRequest_body = {}, {}
        if self.aws_vpc_endpoint_id:
            createVpcEndpointRequest_body[
                "aws_vpc_endpoint_id"
            ] = self.aws_vpc_endpoint_id
        if self.region:
            createVpcEndpointRequest_body["region"] = self.region
        if self.vpc_endpoint_name:
            createVpcEndpointRequest_body["vpc_endpoint_name"] = self.vpc_endpoint_name

        return createVpcEndpointRequest_query, createVpcEndpointRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateVpcEndpointRequest":
        return cls(
            aws_vpc_endpoint_id=d.get("aws_vpc_endpoint_id", None),
            region=d.get("region", None),
            vpc_endpoint_name=d.get("vpc_endpoint_name", None),
        )


@dataclass
class CreateWorkspaceRequest:

    # The AWS region of the workspace's data plane.
    aws_region: str
    # The cloud provider which the workspace uses. For Google Cloud workspaces,
    # always set this field to `gcp`.
    cloud: str
    # The general workspace configurations that are specific to cloud providers.
    cloud_resource_bucket: "CloudResourceBucket"
    # ID of the workspace's credential configuration object.
    credentials_id: str
    # The deployment name defines part of the subdomain for the workspace. The
    # workspace URL for web application and REST APIs is
    # `<workspace-deployment-name>.cloud.databricks.com`. For example, if the
    # deployment name is `abcsales`, your workspace URL will be
    # `https://abcsales.cloud.databricks.com`. Hyphens are allowed. This
    # property supports only the set of characters that are allowed in a
    # subdomain.
    #
    # If your account has a non-empty deployment name prefix at workspace
    # creation time, the workspace deployment name changes so that the beginning
    # has the account prefix and a hyphen. For example, if your account's
    # deployment prefix is `acme` and the workspace deployment name is
    # `workspace-1`, the `deployment_name` field becomes `acme-workspace-1` and
    # that is the value that is returned in JSON responses for the
    # `deployment_name` field. The workspace URL is
    # `acme-workspace-1.cloud.databricks.com`.
    #
    # If your account has a non-empty deployment name prefix and you set
    # `deployment_name` to the reserved keyword `EMPTY`, `deployment_name` is
    # just the account prefix only. For example, if your account's deployment
    # prefix is `acme` and the workspace deployment name is `EMPTY`,
    # `deployment_name` becomes `acme` only and the workspace URL is
    # `acme.cloud.databricks.com`.
    #
    # Contact your Databricks representatives to add an account deployment name
    # prefix to your account. If you do not have a deployment name prefix, the
    # special deployment name value `EMPTY` is invalid.
    #
    # This value must be unique across all non-deleted deployments across all
    # AWS regions.
    #
    # If a new workspace omits this property, the server generates a unique
    # deployment name for you with the pattern `dbc-xxxxxxxx-xxxx`.
    deployment_name: str
    # The Google Cloud region of the workspace data plane in your Google
    # account. For example, `us-east4`.
    location: str
    # The ID of the workspace's managed services encryption key configuration
    # object. This is used to encrypt the workspace's notebook and secret data
    # in the control plane, in addition to Databricks SQL queries and query
    # history. The provided key configuration object property `use_cases` must
    # contain `MANAGED_SERVICES`.
    managed_services_customer_managed_key_id: str
    # The network configurations for the workspace. If you provide a network
    # configuration ID for a new workspace, Databricks deploys the new workspace
    # into that associated customer-managed VPC. If omitted, by default
    # Databricks creates a new Databricks-managed VPC for the workspace in your
    # Google account and manages its lifecycle.
    #
    # All the IP range configurations must be mutually exclusive. An attempt to
    # create a workspace fails if Databricks detects an IP range overlap.
    #
    # Specify custom IP ranges in CIDR format. The IP ranges for these fields
    # must not overlap, and all IP addresses must be entirely within the
    # following ranges: `10.0.0.0/8`, `100.64.0.0/10`, `172.16.0.0/12`,
    # `192.168.0.0/16`, and `240.0.0.0/4`.
    #
    # The sizes of these IP ranges affect the maximum number of nodes for the
    # workspace.
    #
    # **Important**: Confirm the IP ranges used by your Databricks workspace
    # before creating the workspace. You cannot change them after your workspace
    # is deployed. If the IP address ranges for your Databricks are too small,
    # IP exhaustion can occur, causing your Databricks jobs to fail. To
    # determine the address range sizes that you need, Databricks provides a
    # calculator as a Microsoft Excel spreadsheet. See [calculate subnet sizes
    # for a new workspace].
    #
    # [calculate subnet sizes for a new workspace]: https://docs.gcp.databricks.com/administration-guide/cloud-configurations/gcp/network-sizing.html
    network: "CreateGcpNetwork"
    # The ID of the workspace's network configuration object. To use [AWS
    # PrivateLink] (Public Preview), this field is required.
    #
    # [AWS PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
    network_id: str
    # The pricing tier of the workspace. For pricing tier information, see [AWS
    # Pricing].
    #
    # [AWS Pricing]: https://databricks.com/product/aws-pricing
    pricing_tier: "PricingTier"
    # ID of the workspace's private access settings object. Only used for
    # PrivateLink (Public Preview). This ID must be specified for customers
    # using [AWS PrivateLink] for either front-end (user-to-workspace
    # connection), back-end (data plane to control plane connection), or both
    # connection types.
    #
    # Before configuring PrivateLink, read the [Databricks article about
    # PrivateLink].
    #
    # [AWS PrivateLink]: https://aws.amazon.com/privatelink/
    # [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
    private_access_settings_id: str
    # The ID of the workspace's storage configuration object.
    storage_configuration_id: str
    # The ID of the workspace's storage encryption key configuration object.
    # This is used to encrypt the workspace's root S3 bucket (root DBFS and
    # system data) and, optionally, cluster EBS volumes. The provided key
    # configuration object property `use_cases` must contain `STORAGE`.
    storage_customer_managed_key_id: str
    # The workspace's human-readable name.
    workspace_name: str

    def as_request(self) -> (dict, dict):
        createWorkspaceRequest_query, createWorkspaceRequest_body = {}, {}
        if self.aws_region:
            createWorkspaceRequest_body["aws_region"] = self.aws_region
        if self.cloud:
            createWorkspaceRequest_body["cloud"] = self.cloud
        if self.cloud_resource_bucket:
            createWorkspaceRequest_body[
                "cloud_resource_bucket"
            ] = self.cloud_resource_bucket.as_request()[1]
        if self.credentials_id:
            createWorkspaceRequest_body["credentials_id"] = self.credentials_id
        if self.deployment_name:
            createWorkspaceRequest_body["deployment_name"] = self.deployment_name
        if self.location:
            createWorkspaceRequest_body["location"] = self.location
        if self.managed_services_customer_managed_key_id:
            createWorkspaceRequest_body[
                "managed_services_customer_managed_key_id"
            ] = self.managed_services_customer_managed_key_id
        if self.network:
            createWorkspaceRequest_body["network"] = self.network.as_request()[1]
        if self.network_id:
            createWorkspaceRequest_body["network_id"] = self.network_id
        if self.pricing_tier:
            createWorkspaceRequest_body["pricing_tier"] = self.pricing_tier.value
        if self.private_access_settings_id:
            createWorkspaceRequest_body[
                "private_access_settings_id"
            ] = self.private_access_settings_id
        if self.storage_configuration_id:
            createWorkspaceRequest_body[
                "storage_configuration_id"
            ] = self.storage_configuration_id
        if self.storage_customer_managed_key_id:
            createWorkspaceRequest_body[
                "storage_customer_managed_key_id"
            ] = self.storage_customer_managed_key_id
        if self.workspace_name:
            createWorkspaceRequest_body["workspace_name"] = self.workspace_name

        return createWorkspaceRequest_query, createWorkspaceRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateWorkspaceRequest":
        return cls(
            aws_region=d.get("aws_region", None),
            cloud=d.get("cloud", None),
            cloud_resource_bucket=CloudResourceBucket.from_dict(
                d["cloud_resource_bucket"]
            )
            if "cloud_resource_bucket" in d
            else None,
            credentials_id=d.get("credentials_id", None),
            deployment_name=d.get("deployment_name", None),
            location=d.get("location", None),
            managed_services_customer_managed_key_id=d.get(
                "managed_services_customer_managed_key_id", None
            ),
            network=CreateGcpNetwork.from_dict(d["network"])
            if "network" in d
            else None,
            network_id=d.get("network_id", None),
            pricing_tier=PricingTier(d["pricing_tier"])
            if "pricing_tier" in d
            else None,
            private_access_settings_id=d.get("private_access_settings_id", None),
            storage_configuration_id=d.get("storage_configuration_id", None),
            storage_customer_managed_key_id=d.get(
                "storage_customer_managed_key_id", None
            ),
            workspace_name=d.get("workspace_name", None),
        )


@dataclass
class Credential:

    # The Databricks account ID that hosts the credential.
    account_id: str

    aws_credentials: "AwsCredentials"
    # Time in epoch milliseconds when the credential was created.
    creation_time: int
    # Databricks credential configuration ID.
    credentials_id: str
    # The human-readable name of the credential configuration object.
    credentials_name: str

    def as_request(self) -> (dict, dict):
        credential_query, credential_body = {}, {}
        if self.account_id:
            credential_body["account_id"] = self.account_id
        if self.aws_credentials:
            credential_body["aws_credentials"] = self.aws_credentials.as_request()[1]
        if self.creation_time:
            credential_body["creation_time"] = self.creation_time
        if self.credentials_id:
            credential_body["credentials_id"] = self.credentials_id
        if self.credentials_name:
            credential_body["credentials_name"] = self.credentials_name

        return credential_query, credential_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Credential":
        return cls(
            account_id=d.get("account_id", None),
            aws_credentials=AwsCredentials.from_dict(d["aws_credentials"])
            if "aws_credentials" in d
            else None,
            creation_time=d.get("creation_time", None),
            credentials_id=d.get("credentials_id", None),
            credentials_name=d.get("credentials_name", None),
        )


@dataclass
class CustomerManagedKey:

    # The Databricks account ID that holds the customer-managed key.
    account_id: str

    aws_key_info: "AwsKeyInfo"
    # Time in epoch milliseconds when the customer key was created.
    creation_time: int
    # ID of the encryption key configuration object.
    customer_managed_key_id: str
    # The cases that the key can be used for.
    use_cases: "List[KeyUseCase]"

    def as_request(self) -> (dict, dict):
        customerManagedKey_query, customerManagedKey_body = {}, {}
        if self.account_id:
            customerManagedKey_body["account_id"] = self.account_id
        if self.aws_key_info:
            customerManagedKey_body["aws_key_info"] = self.aws_key_info.as_request()[1]
        if self.creation_time:
            customerManagedKey_body["creation_time"] = self.creation_time
        if self.customer_managed_key_id:
            customerManagedKey_body[
                "customer_managed_key_id"
            ] = self.customer_managed_key_id
        if self.use_cases:
            customerManagedKey_body["use_cases"] = [v for v in self.use_cases]

        return customerManagedKey_query, customerManagedKey_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CustomerManagedKey":
        return cls(
            account_id=d.get("account_id", None),
            aws_key_info=AwsKeyInfo.from_dict(d["aws_key_info"])
            if "aws_key_info" in d
            else None,
            creation_time=d.get("creation_time", None),
            customer_managed_key_id=d.get("customer_managed_key_id", None),
            use_cases=d.get("use_cases", None),
        )


@dataclass
class DeleteCredentialRequest:
    """Delete credential configuration"""

    # Databricks Account API credential configuration ID
    credentials_id: str  # path

    def as_request(self) -> (dict, dict):
        deleteCredentialRequest_query, deleteCredentialRequest_body = {}, {}
        if self.credentials_id:
            deleteCredentialRequest_body["credentials_id"] = self.credentials_id

        return deleteCredentialRequest_query, deleteCredentialRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteCredentialRequest":
        return cls(
            credentials_id=d.get("credentials_id", None),
        )


@dataclass
class DeleteEncryptionKeyRequest:
    """Delete encryption key configuration"""

    # Databricks encryption key configuration ID.
    customer_managed_key_id: str  # path

    def as_request(self) -> (dict, dict):
        deleteEncryptionKeyRequest_query, deleteEncryptionKeyRequest_body = {}, {}
        if self.customer_managed_key_id:
            deleteEncryptionKeyRequest_body[
                "customer_managed_key_id"
            ] = self.customer_managed_key_id

        return deleteEncryptionKeyRequest_query, deleteEncryptionKeyRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteEncryptionKeyRequest":
        return cls(
            customer_managed_key_id=d.get("customer_managed_key_id", None),
        )


@dataclass
class DeleteNetworkRequest:
    """Delete network configuration"""

    # Databricks Account API network configuration ID.
    network_id: str  # path

    def as_request(self) -> (dict, dict):
        deleteNetworkRequest_query, deleteNetworkRequest_body = {}, {}
        if self.network_id:
            deleteNetworkRequest_body["network_id"] = self.network_id

        return deleteNetworkRequest_query, deleteNetworkRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteNetworkRequest":
        return cls(
            network_id=d.get("network_id", None),
        )


@dataclass
class DeletePrivateAccesRequest:
    """Delete a private access settings object"""

    # Databricks Account API private access settings ID.
    private_access_settings_id: str  # path

    def as_request(self) -> (dict, dict):
        deletePrivateAccesRequest_query, deletePrivateAccesRequest_body = {}, {}
        if self.private_access_settings_id:
            deletePrivateAccesRequest_body[
                "private_access_settings_id"
            ] = self.private_access_settings_id

        return deletePrivateAccesRequest_query, deletePrivateAccesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeletePrivateAccesRequest":
        return cls(
            private_access_settings_id=d.get("private_access_settings_id", None),
        )


@dataclass
class DeleteStorageRequest:
    """Delete storage configuration"""

    # Databricks Account API storage configuration ID.
    storage_configuration_id: str  # path

    def as_request(self) -> (dict, dict):
        deleteStorageRequest_query, deleteStorageRequest_body = {}, {}
        if self.storage_configuration_id:
            deleteStorageRequest_body[
                "storage_configuration_id"
            ] = self.storage_configuration_id

        return deleteStorageRequest_query, deleteStorageRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteStorageRequest":
        return cls(
            storage_configuration_id=d.get("storage_configuration_id", None),
        )


@dataclass
class DeleteVpcEndpointRequest:
    """Delete VPC endpoint configuration"""

    # Databricks VPC endpoint ID.
    vpc_endpoint_id: str  # path

    def as_request(self) -> (dict, dict):
        deleteVpcEndpointRequest_query, deleteVpcEndpointRequest_body = {}, {}
        if self.vpc_endpoint_id:
            deleteVpcEndpointRequest_body["vpc_endpoint_id"] = self.vpc_endpoint_id

        return deleteVpcEndpointRequest_query, deleteVpcEndpointRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteVpcEndpointRequest":
        return cls(
            vpc_endpoint_id=d.get("vpc_endpoint_id", None),
        )


@dataclass
class DeleteWorkspaceRequest:
    """Delete workspace"""

    # Workspace ID.
    workspace_id: int  # path

    def as_request(self) -> (dict, dict):
        deleteWorkspaceRequest_query, deleteWorkspaceRequest_body = {}, {}
        if self.workspace_id:
            deleteWorkspaceRequest_body["workspace_id"] = self.workspace_id

        return deleteWorkspaceRequest_query, deleteWorkspaceRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteWorkspaceRequest":
        return cls(
            workspace_id=d.get("workspace_id", None),
        )


class EndpointUseCase(Enum):
    """This enumeration represents the type of Databricks VPC [endpoint service]
    that was used when creating this VPC endpoint.

    If the VPC endpoint connects to the Databricks control plane for either the
    front-end connection or the back-end REST API connection, the value is
    `WORKSPACE_ACCESS`.

    If the VPC endpoint connects to the Databricks workspace for the back-end
    [secure cluster connectivity] relay, the value is `DATAPLANE_RELAY_ACCESS`.

    [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service.html
    [secure cluster connectivity]: https://docs.databricks.com/security/secure-cluster-connectivity.html"""

    DATAPLANE_RELAY_ACCESS = "DATAPLANE_RELAY_ACCESS"
    WORKSPACE_ACCESS = "WORKSPACE_ACCESS"


class ErrorType(Enum):
    """The AWS resource associated with this error: credentials, VPC, subnet,
    security group, or network ACL."""

    credentials = "credentials"
    networkAcl = "networkAcl"
    securityGroup = "securityGroup"
    subnet = "subnet"
    vpc = "vpc"


@dataclass
class GcpCommonNetworkConfig:
    """The common network configuration fields that can be used by both
    Databricks-managed VPCs and customer-managed VPCs."""

    # The IP range from which to allocate GKE cluster master resources. This
    # field will be ignored if GKE private cluster is not enabled.
    #
    # It must be exactly as big as `/28`.
    gke_cluster_master_ip_range: str
    # Specifies the network connectivity types for the GKE nodes and the GKE
    # master network. Set to `PRIVATE_NODE_PUBLIC_MASTER` for a private GKE
    # cluster for the workspace. The GKE nodes will not have public IPs. Set to
    # `PUBLIC_NODE_PUBLIC_MASTER` for a public GKE cluster. The nodes of a
    # public GKE cluster have public IP addresses.
    gke_connectivity_type: "GkeConnectivityType"

    def as_request(self) -> (dict, dict):
        gcpCommonNetworkConfig_query, gcpCommonNetworkConfig_body = {}, {}
        if self.gke_cluster_master_ip_range:
            gcpCommonNetworkConfig_body[
                "gke_cluster_master_ip_range"
            ] = self.gke_cluster_master_ip_range
        if self.gke_connectivity_type:
            gcpCommonNetworkConfig_body[
                "gke_connectivity_type"
            ] = self.gke_connectivity_type.value

        return gcpCommonNetworkConfig_query, gcpCommonNetworkConfig_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GcpCommonNetworkConfig":
        return cls(
            gke_cluster_master_ip_range=d.get("gke_cluster_master_ip_range", None),
            gke_connectivity_type=GkeConnectivityType(d["gke_connectivity_type"])
            if "gke_connectivity_type" in d
            else None,
        )


@dataclass
class GcpManagedNetworkConfig:
    """The network settings for the workspace. The configurations are only for
    Databricks-managed VPCs. It is ignored if you specify a customer-managed VPC
    in the `network_id` field."""

    # The IP range from which to allocate GKE cluster pods. No bigger than `/9`
    # and no smaller than `/21`.
    gke_cluster_pod_ip_range: str
    # The IP range from which to allocate GKE cluster services. No bigger than
    # `/16` and no smaller than `/27`.
    gke_cluster_service_ip_range: str
    # The IP range from which to allocate GKE cluster nodes. No bigger than `/9`
    # and no smaller than `/29`.
    subnet_cidr: str

    def as_request(self) -> (dict, dict):
        gcpManagedNetworkConfig_query, gcpManagedNetworkConfig_body = {}, {}
        if self.gke_cluster_pod_ip_range:
            gcpManagedNetworkConfig_body[
                "gke_cluster_pod_ip_range"
            ] = self.gke_cluster_pod_ip_range
        if self.gke_cluster_service_ip_range:
            gcpManagedNetworkConfig_body[
                "gke_cluster_service_ip_range"
            ] = self.gke_cluster_service_ip_range
        if self.subnet_cidr:
            gcpManagedNetworkConfig_body["subnet_cidr"] = self.subnet_cidr

        return gcpManagedNetworkConfig_query, gcpManagedNetworkConfig_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GcpManagedNetworkConfig":
        return cls(
            gke_cluster_pod_ip_range=d.get("gke_cluster_pod_ip_range", None),
            gke_cluster_service_ip_range=d.get("gke_cluster_service_ip_range", None),
            subnet_cidr=d.get("subnet_cidr", None),
        )


@dataclass
class GcpNetwork:

    # The network configuration ID that is attached to the workspace. This field
    # is available only if the network is a customer-managed network.
    network_id: str

    def as_request(self) -> (dict, dict):
        gcpNetwork_query, gcpNetwork_body = {}, {}
        if self.network_id:
            gcpNetwork_body["network_id"] = self.network_id

        return gcpNetwork_query, gcpNetwork_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GcpNetwork":
        return cls(
            network_id=d.get("network_id", None),
        )


@dataclass
class GcpNetworkInfo:
    """The Google Cloud specific information for this network (for example, the VPC
    ID, subnet ID, and secondary IP ranges)."""

    # The Google Cloud project ID of the VPC network.
    network_project_id: str
    # The name of the secondary IP range for pods. A Databricks-managed GKE
    # cluster uses this IP range for its pods. This secondary IP range can be
    # used by only one workspace.
    pod_ip_range_name: str
    # The name of the secondary IP range for services. A Databricks-managed GKE
    # cluster uses this IP range for its services. This secondary IP range can
    # be used by only one workspace.
    service_ip_range_name: str
    # The ID of the subnet associated with this network.
    subnet_id: str
    # The Google Cloud region of the workspace data plane (for example,
    # `us-east4`).
    subnet_region: str
    # The ID of the VPC associated with this network. VPC IDs can be used in
    # multiple network configurations.
    vpc_id: str

    def as_request(self) -> (dict, dict):
        gcpNetworkInfo_query, gcpNetworkInfo_body = {}, {}
        if self.network_project_id:
            gcpNetworkInfo_body["network_project_id"] = self.network_project_id
        if self.pod_ip_range_name:
            gcpNetworkInfo_body["pod_ip_range_name"] = self.pod_ip_range_name
        if self.service_ip_range_name:
            gcpNetworkInfo_body["service_ip_range_name"] = self.service_ip_range_name
        if self.subnet_id:
            gcpNetworkInfo_body["subnet_id"] = self.subnet_id
        if self.subnet_region:
            gcpNetworkInfo_body["subnet_region"] = self.subnet_region
        if self.vpc_id:
            gcpNetworkInfo_body["vpc_id"] = self.vpc_id

        return gcpNetworkInfo_query, gcpNetworkInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GcpNetworkInfo":
        return cls(
            network_project_id=d.get("network_project_id", None),
            pod_ip_range_name=d.get("pod_ip_range_name", None),
            service_ip_range_name=d.get("service_ip_range_name", None),
            subnet_id=d.get("subnet_id", None),
            subnet_region=d.get("subnet_region", None),
            vpc_id=d.get("vpc_id", None),
        )


@dataclass
class GcpProjectContainer:
    """The general workspace configurations that are specific to Google Cloud."""

    # The Google Cloud project ID, which the workspace uses to instantiate cloud
    # resources for your workspace.
    project_id: str

    def as_request(self) -> (dict, dict):
        gcpProjectContainer_query, gcpProjectContainer_body = {}, {}
        if self.project_id:
            gcpProjectContainer_body["project_id"] = self.project_id

        return gcpProjectContainer_query, gcpProjectContainer_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GcpProjectContainer":
        return cls(
            project_id=d.get("project_id", None),
        )


@dataclass
class GetCredentialRequest:
    """Get credential configuration"""

    # Databricks Account API credential configuration ID
    credentials_id: str  # path

    def as_request(self) -> (dict, dict):
        getCredentialRequest_query, getCredentialRequest_body = {}, {}
        if self.credentials_id:
            getCredentialRequest_body["credentials_id"] = self.credentials_id

        return getCredentialRequest_query, getCredentialRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetCredentialRequest":
        return cls(
            credentials_id=d.get("credentials_id", None),
        )


@dataclass
class GetEncryptionKeyRequest:
    """Get encryption key configuration"""

    # Databricks encryption key configuration ID.
    customer_managed_key_id: str  # path

    def as_request(self) -> (dict, dict):
        getEncryptionKeyRequest_query, getEncryptionKeyRequest_body = {}, {}
        if self.customer_managed_key_id:
            getEncryptionKeyRequest_body[
                "customer_managed_key_id"
            ] = self.customer_managed_key_id

        return getEncryptionKeyRequest_query, getEncryptionKeyRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetEncryptionKeyRequest":
        return cls(
            customer_managed_key_id=d.get("customer_managed_key_id", None),
        )


@dataclass
class GetNetworkRequest:
    """Get a network configuration"""

    # Databricks Account API network configuration ID.
    network_id: str  # path

    def as_request(self) -> (dict, dict):
        getNetworkRequest_query, getNetworkRequest_body = {}, {}
        if self.network_id:
            getNetworkRequest_body["network_id"] = self.network_id

        return getNetworkRequest_query, getNetworkRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetNetworkRequest":
        return cls(
            network_id=d.get("network_id", None),
        )


@dataclass
class GetPrivateAccesRequest:
    """Get a private access settings object"""

    # Databricks Account API private access settings ID.
    private_access_settings_id: str  # path

    def as_request(self) -> (dict, dict):
        getPrivateAccesRequest_query, getPrivateAccesRequest_body = {}, {}
        if self.private_access_settings_id:
            getPrivateAccesRequest_body[
                "private_access_settings_id"
            ] = self.private_access_settings_id

        return getPrivateAccesRequest_query, getPrivateAccesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetPrivateAccesRequest":
        return cls(
            private_access_settings_id=d.get("private_access_settings_id", None),
        )


@dataclass
class GetStorageRequest:
    """Get storage configuration"""

    # Databricks Account API storage configuration ID.
    storage_configuration_id: str  # path

    def as_request(self) -> (dict, dict):
        getStorageRequest_query, getStorageRequest_body = {}, {}
        if self.storage_configuration_id:
            getStorageRequest_body[
                "storage_configuration_id"
            ] = self.storage_configuration_id

        return getStorageRequest_query, getStorageRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetStorageRequest":
        return cls(
            storage_configuration_id=d.get("storage_configuration_id", None),
        )


@dataclass
class GetVpcEndpointRequest:
    """Get a VPC endpoint configuration"""

    # Databricks VPC endpoint ID.
    vpc_endpoint_id: str  # path

    def as_request(self) -> (dict, dict):
        getVpcEndpointRequest_query, getVpcEndpointRequest_body = {}, {}
        if self.vpc_endpoint_id:
            getVpcEndpointRequest_body["vpc_endpoint_id"] = self.vpc_endpoint_id

        return getVpcEndpointRequest_query, getVpcEndpointRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetVpcEndpointRequest":
        return cls(
            vpc_endpoint_id=d.get("vpc_endpoint_id", None),
        )


@dataclass
class GetWorkspaceRequest:
    """Get workspace"""

    # Workspace ID.
    workspace_id: int  # path

    def as_request(self) -> (dict, dict):
        getWorkspaceRequest_query, getWorkspaceRequest_body = {}, {}
        if self.workspace_id:
            getWorkspaceRequest_body["workspace_id"] = self.workspace_id

        return getWorkspaceRequest_query, getWorkspaceRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetWorkspaceRequest":
        return cls(
            workspace_id=d.get("workspace_id", None),
        )


class GkeConnectivityType(Enum):
    """Specifies the network connectivity types for the GKE nodes and the GKE
    master network. Set to `PRIVATE_NODE_PUBLIC_MASTER` for a private GKE
    cluster for the workspace. The GKE nodes will not have public IPs. Set to
    `PUBLIC_NODE_PUBLIC_MASTER` for a public GKE cluster. The nodes of a public
    GKE cluster have public IP addresses."""

    PRIVATE_NODE_PUBLIC_MASTER = "PRIVATE_NODE_PUBLIC_MASTER"
    PUBLIC_NODE_PUBLIC_MASTER = "PUBLIC_NODE_PUBLIC_MASTER"


class KeyUseCase(Enum):
    """This describes an enum"""

    MANAGED_SERVICES = "MANAGED_SERVICES"
    STORAGE = "STORAGE"


@dataclass
class Network:

    # The Databricks account ID associated with this network configuration.
    account_id: str
    # Time in epoch milliseconds when the network was created.
    creation_time: int
    # Array of error messages about the network configuration.
    error_messages: "List[NetworkHealth]"
    # The Google Cloud specific information for this network (for example, the
    # VPC ID, subnet ID, and secondary IP ranges).
    gcp_network_info: "GcpNetworkInfo"
    # The Databricks network configuration ID.
    network_id: str
    # The human-readable name of the network configuration.
    network_name: str

    security_group_ids: "List[str]"

    subnet_ids: "List[str]"
    # If specified, contains the VPC endpoints used to allow cluster
    # communication from this VPC over [AWS PrivateLink].
    #
    # [AWS PrivateLink]: https://aws.amazon.com/privatelink/
    vpc_endpoints: "NetworkVpcEndpoints"
    # The ID of the VPC associated with this network configuration. VPC IDs can
    # be used in multiple networks.
    vpc_id: str
    # This describes an enum
    vpc_status: "VpcStatus"
    # Array of warning messages about the network configuration.
    warning_messages: "List[NetworkWarning]"
    # Workspace ID associated with this network configuration.
    workspace_id: int

    def as_request(self) -> (dict, dict):
        network_query, network_body = {}, {}
        if self.account_id:
            network_body["account_id"] = self.account_id
        if self.creation_time:
            network_body["creation_time"] = self.creation_time
        if self.error_messages:
            network_body["error_messages"] = [
                v.as_request()[1] for v in self.error_messages
            ]
        if self.gcp_network_info:
            network_body["gcp_network_info"] = self.gcp_network_info.as_request()[1]
        if self.network_id:
            network_body["network_id"] = self.network_id
        if self.network_name:
            network_body["network_name"] = self.network_name
        if self.security_group_ids:
            network_body["security_group_ids"] = [v for v in self.security_group_ids]
        if self.subnet_ids:
            network_body["subnet_ids"] = [v for v in self.subnet_ids]
        if self.vpc_endpoints:
            network_body["vpc_endpoints"] = self.vpc_endpoints.as_request()[1]
        if self.vpc_id:
            network_body["vpc_id"] = self.vpc_id
        if self.vpc_status:
            network_body["vpc_status"] = self.vpc_status.value
        if self.warning_messages:
            network_body["warning_messages"] = [
                v.as_request()[1] for v in self.warning_messages
            ]
        if self.workspace_id:
            network_body["workspace_id"] = self.workspace_id

        return network_query, network_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Network":
        return cls(
            account_id=d.get("account_id", None),
            creation_time=d.get("creation_time", None),
            error_messages=[NetworkHealth.from_dict(v) for v in d["error_messages"]]
            if "error_messages" in d
            else None,
            gcp_network_info=GcpNetworkInfo.from_dict(d["gcp_network_info"])
            if "gcp_network_info" in d
            else None,
            network_id=d.get("network_id", None),
            network_name=d.get("network_name", None),
            security_group_ids=d.get("security_group_ids", None),
            subnet_ids=d.get("subnet_ids", None),
            vpc_endpoints=NetworkVpcEndpoints.from_dict(d["vpc_endpoints"])
            if "vpc_endpoints" in d
            else None,
            vpc_id=d.get("vpc_id", None),
            vpc_status=VpcStatus(d["vpc_status"]) if "vpc_status" in d else None,
            warning_messages=[
                NetworkWarning.from_dict(v) for v in d["warning_messages"]
            ]
            if "warning_messages" in d
            else None,
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class NetworkHealth:

    # Details of the error.
    error_message: str
    # The AWS resource associated with this error: credentials, VPC, subnet,
    # security group, or network ACL.
    error_type: "ErrorType"

    def as_request(self) -> (dict, dict):
        networkHealth_query, networkHealth_body = {}, {}
        if self.error_message:
            networkHealth_body["error_message"] = self.error_message
        if self.error_type:
            networkHealth_body["error_type"] = self.error_type.value

        return networkHealth_query, networkHealth_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "NetworkHealth":
        return cls(
            error_message=d.get("error_message", None),
            error_type=ErrorType(d["error_type"]) if "error_type" in d else None,
        )


@dataclass
class NetworkVpcEndpoints:
    """If specified, contains the VPC endpoints used to allow cluster communication
    from this VPC over [AWS PrivateLink].

    [AWS PrivateLink]: https://aws.amazon.com/privatelink/"""

    # The VPC endpoint ID used by this network to access the Databricks secure
    # cluster connectivity relay. See [Secure Cluster Connectivity].
    #
    # This is a list type for future compatibility, but currently only one VPC
    # endpoint ID should be supplied.
    #
    # **Note**: This is the Databricks-specific ID of the VPC endpoint object in
    # the Account API, not the AWS VPC endpoint ID that you see for your
    # endpoint in the AWS Console.
    #
    # [Secure Cluster Connectivity]: https://docs.databricks.com/security/secure-cluster-connectivity.html
    dataplane_relay: "List[str]"
    # The VPC endpoint ID used by this network to access the Databricks REST
    # API. Databricks clusters make calls to our REST API as part of cluster
    # creation, mlflow tracking, and many other features. Thus, this is required
    # even if your workspace allows public access to the REST API.
    #
    # This is a list type for future compatibility, but currently only one VPC
    # endpoint ID should be supplied.
    #
    # **Note**: This is the Databricks-specific ID of the VPC endpoint object in
    # the Account API, not the AWS VPC endpoint ID that you see for your
    # endpoint in the AWS Console.
    rest_api: "List[str]"

    def as_request(self) -> (dict, dict):
        networkVpcEndpoints_query, networkVpcEndpoints_body = {}, {}
        if self.dataplane_relay:
            networkVpcEndpoints_body["dataplane_relay"] = [
                v for v in self.dataplane_relay
            ]
        if self.rest_api:
            networkVpcEndpoints_body["rest_api"] = [v for v in self.rest_api]

        return networkVpcEndpoints_query, networkVpcEndpoints_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "NetworkVpcEndpoints":
        return cls(
            dataplane_relay=d.get("dataplane_relay", None),
            rest_api=d.get("rest_api", None),
        )


@dataclass
class NetworkWarning:

    # Details of the warning.
    warning_message: str
    # The AWS resource associated with this warning: a subnet or a security
    # group.
    warning_type: "WarningType"

    def as_request(self) -> (dict, dict):
        networkWarning_query, networkWarning_body = {}, {}
        if self.warning_message:
            networkWarning_body["warning_message"] = self.warning_message
        if self.warning_type:
            networkWarning_body["warning_type"] = self.warning_type.value

        return networkWarning_query, networkWarning_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "NetworkWarning":
        return cls(
            warning_message=d.get("warning_message", None),
            warning_type=WarningType(d["warning_type"])
            if "warning_type" in d
            else None,
        )


class PricingTier(Enum):
    """The pricing tier of the workspace. For pricing tier information, see [AWS
    Pricing].

    [AWS Pricing]: https://databricks.com/product/aws-pricing"""

    COMMUNITY_EDITION = "COMMUNITY_EDITION"
    DEDICATED = "DEDICATED"
    ENTERPRISE = "ENTERPRISE"
    PREMIUM = "PREMIUM"
    STANDARD = "STANDARD"
    UNKNOWN = "UNKNOWN"


class PrivateAccessLevel(Enum):
    """The private access level controls which VPC endpoints can connect to the UI
    or API of any workspace that attaches this private access settings object. *
    `ANY` (deprecated): Any VPC endpoint can connect to your workspace. *
    `ACCOUNT` level access (the default) allows only VPC endpoints that are
    registered in your Databricks account connect to your workspace. *
    `ENDPOINT` level access allows only specified VPC endpoints connect to your
    workspace. For details, see `allowed_vpc_endpoint_ids`."""

    ACCOUNT = "ACCOUNT"
    ANY = "ANY"
    ENDPOINT = "ENDPOINT"


@dataclass
class PrivateAccessSettings:

    # The Databricks account ID that hosts the credential.
    account_id: str
    # An array of Databricks VPC endpoint IDs. This is the Databricks ID
    # returned when registering the VPC endpoint configuration in your
    # Databricks account. This is _not_ the ID of the VPC endpoint in AWS.
    #
    # Only used when `private_access_level` is set to `ENDPOINT`. This is an
    # allow list of VPC endpoints registered in your Databricks account that can
    # connect to your workspace over AWS PrivateLink.
    #
    # **Note**: If hybrid access to your workspace is enabled by setting
    # `public_access_enabled` to `true`, this control only works for PrivateLink
    # connections. To control how your workspace is accessed via public
    # internet, see [IP access lists].
    #
    # [IP access lists]: https://docs.databricks.com/security/network/ip-access-list.html
    allowed_vpc_endpoint_ids: "List[str]"
    # The private access level controls which VPC endpoints can connect to the
    # UI or API of any workspace that attaches this private access settings
    # object. * `ANY` (deprecated): Any VPC endpoint can connect to your
    # workspace. * `ACCOUNT` level access (the default) allows only VPC
    # endpoints that are registered in your Databricks account connect to your
    # workspace. * `ENDPOINT` level access allows only specified VPC endpoints
    # connect to your workspace. For details, see `allowed_vpc_endpoint_ids`.
    private_access_level: "PrivateAccessLevel"
    # Databricks private access settings ID.
    private_access_settings_id: str
    # The human-readable name of the private access settings object.
    private_access_settings_name: str
    # Determines if the workspace can be accessed over public internet. For
    # fully private workspaces, you can optionally specify `false`, but only if
    # you implement both the front-end and the back-end PrivateLink connections.
    # Otherwise, specify `true`, which means that public access is enabled.
    public_access_enabled: bool
    # The AWS region for workspaces attached to this private access settings
    # object.
    region: str

    def as_request(self) -> (dict, dict):
        privateAccessSettings_query, privateAccessSettings_body = {}, {}
        if self.account_id:
            privateAccessSettings_body["account_id"] = self.account_id
        if self.allowed_vpc_endpoint_ids:
            privateAccessSettings_body["allowed_vpc_endpoint_ids"] = [
                v for v in self.allowed_vpc_endpoint_ids
            ]
        if self.private_access_level:
            privateAccessSettings_body[
                "private_access_level"
            ] = self.private_access_level.value
        if self.private_access_settings_id:
            privateAccessSettings_body[
                "private_access_settings_id"
            ] = self.private_access_settings_id
        if self.private_access_settings_name:
            privateAccessSettings_body[
                "private_access_settings_name"
            ] = self.private_access_settings_name
        if self.public_access_enabled:
            privateAccessSettings_body[
                "public_access_enabled"
            ] = self.public_access_enabled
        if self.region:
            privateAccessSettings_body["region"] = self.region

        return privateAccessSettings_query, privateAccessSettings_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PrivateAccessSettings":
        return cls(
            account_id=d.get("account_id", None),
            allowed_vpc_endpoint_ids=d.get("allowed_vpc_endpoint_ids", None),
            private_access_level=PrivateAccessLevel(d["private_access_level"])
            if "private_access_level" in d
            else None,
            private_access_settings_id=d.get("private_access_settings_id", None),
            private_access_settings_name=d.get("private_access_settings_name", None),
            public_access_enabled=d.get("public_access_enabled", None),
            region=d.get("region", None),
        )


@dataclass
class RootBucketInfo:
    """Root S3 bucket information."""

    # The name of the S3 bucket.
    bucket_name: str

    def as_request(self) -> (dict, dict):
        rootBucketInfo_query, rootBucketInfo_body = {}, {}
        if self.bucket_name:
            rootBucketInfo_body["bucket_name"] = self.bucket_name

        return rootBucketInfo_query, rootBucketInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RootBucketInfo":
        return cls(
            bucket_name=d.get("bucket_name", None),
        )


@dataclass
class StorageConfiguration:

    # The Databricks account ID that hosts the credential.
    account_id: str
    # Time in epoch milliseconds when the storage configuration was created.
    creation_time: int
    # Root S3 bucket information.
    root_bucket_info: "RootBucketInfo"
    # Databricks storage configuration ID.
    storage_configuration_id: str
    # The human-readable name of the storage configuration.
    storage_configuration_name: str

    def as_request(self) -> (dict, dict):
        storageConfiguration_query, storageConfiguration_body = {}, {}
        if self.account_id:
            storageConfiguration_body["account_id"] = self.account_id
        if self.creation_time:
            storageConfiguration_body["creation_time"] = self.creation_time
        if self.root_bucket_info:
            storageConfiguration_body[
                "root_bucket_info"
            ] = self.root_bucket_info.as_request()[1]
        if self.storage_configuration_id:
            storageConfiguration_body[
                "storage_configuration_id"
            ] = self.storage_configuration_id
        if self.storage_configuration_name:
            storageConfiguration_body[
                "storage_configuration_name"
            ] = self.storage_configuration_name

        return storageConfiguration_query, storageConfiguration_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "StorageConfiguration":
        return cls(
            account_id=d.get("account_id", None),
            creation_time=d.get("creation_time", None),
            root_bucket_info=RootBucketInfo.from_dict(d["root_bucket_info"])
            if "root_bucket_info" in d
            else None,
            storage_configuration_id=d.get("storage_configuration_id", None),
            storage_configuration_name=d.get("storage_configuration_name", None),
        )


@dataclass
class StsRole:

    # The external ID that needs to be trusted by the cross-account role. This
    # is always your Databricks account ID.
    external_id: str
    # The Amazon Resource Name (ARN) of the cross account role.
    role_arn: str

    def as_request(self) -> (dict, dict):
        stsRole_query, stsRole_body = {}, {}
        if self.external_id:
            stsRole_body["external_id"] = self.external_id
        if self.role_arn:
            stsRole_body["role_arn"] = self.role_arn

        return stsRole_query, stsRole_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "StsRole":
        return cls(
            external_id=d.get("external_id", None),
            role_arn=d.get("role_arn", None),
        )


@dataclass
class UpdateWorkspaceRequest:

    # The AWS region of the workspace's data plane (for example, `us-west-2`).
    # This parameter is available only for updating failed workspaces.
    aws_region: str
    # ID of the workspace's credential configuration object. This parameter is
    # available for updating both failed and running workspaces.
    credentials_id: str
    # The ID of the workspace's managed services encryption key configuration
    # object. This parameter is available only for updating failed workspaces.
    managed_services_customer_managed_key_id: str
    # The ID of the workspace's network configuration object. Used only if you
    # already use a customer-managed VPC. This change is supported only if you
    # specified a network configuration ID when the workspace was created. In
    # other words, you cannot switch from a Databricks-managed VPC to a
    # customer-managed VPC. This parameter is available for updating both failed
    # and running workspaces. **Note**: You cannot use a network configuration
    # update in this API to add support for PrivateLink (Public Preview). To add
    # PrivateLink to an existing workspace, contact your Databricks
    # representative.
    network_id: str
    # The ID of the workspace's storage configuration object. This parameter is
    # available only for updating failed workspaces.
    storage_configuration_id: str
    # The ID of the key configuration object for workspace storage. This
    # parameter is available for updating both failed and running workspaces.
    storage_customer_managed_key_id: str
    # Workspace ID.
    workspace_id: int  # path

    def as_request(self) -> (dict, dict):
        updateWorkspaceRequest_query, updateWorkspaceRequest_body = {}, {}
        if self.aws_region:
            updateWorkspaceRequest_body["aws_region"] = self.aws_region
        if self.credentials_id:
            updateWorkspaceRequest_body["credentials_id"] = self.credentials_id
        if self.managed_services_customer_managed_key_id:
            updateWorkspaceRequest_body[
                "managed_services_customer_managed_key_id"
            ] = self.managed_services_customer_managed_key_id
        if self.network_id:
            updateWorkspaceRequest_body["network_id"] = self.network_id
        if self.storage_configuration_id:
            updateWorkspaceRequest_body[
                "storage_configuration_id"
            ] = self.storage_configuration_id
        if self.storage_customer_managed_key_id:
            updateWorkspaceRequest_body[
                "storage_customer_managed_key_id"
            ] = self.storage_customer_managed_key_id
        if self.workspace_id:
            updateWorkspaceRequest_body["workspace_id"] = self.workspace_id

        return updateWorkspaceRequest_query, updateWorkspaceRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateWorkspaceRequest":
        return cls(
            aws_region=d.get("aws_region", None),
            credentials_id=d.get("credentials_id", None),
            managed_services_customer_managed_key_id=d.get(
                "managed_services_customer_managed_key_id", None
            ),
            network_id=d.get("network_id", None),
            storage_configuration_id=d.get("storage_configuration_id", None),
            storage_customer_managed_key_id=d.get(
                "storage_customer_managed_key_id", None
            ),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class UpsertPrivateAccessSettingsRequest:

    # An array of Databricks VPC endpoint IDs. This is the Databricks ID that is
    # returned when registering the VPC endpoint configuration in your
    # Databricks account. This is not the ID of the VPC endpoint in AWS.
    #
    # Only used when `private_access_level` is set to `ENDPOINT`. This is an
    # allow list of VPC endpoints that in your account that can connect to your
    # workspace over AWS PrivateLink.
    #
    # If hybrid access to your workspace is enabled by setting
    # `public_access_enabled` to `true`, this control only works for PrivateLink
    # connections. To control how your workspace is accessed via public
    # internet, see [IP access lists].
    #
    # [IP access lists]: https://docs.databricks.com/security/network/ip-access-list.html
    allowed_vpc_endpoint_ids: "List[str]"
    # The private access level controls which VPC endpoints can connect to the
    # UI or API of any workspace that attaches this private access settings
    # object. * `ANY` (deprecated): Any VPC endpoint can connect to your
    # workspace. * `ACCOUNT` level access (the default) allows only VPC
    # endpoints that are registered in your Databricks account connect to your
    # workspace. * `ENDPOINT` level access allows only specified VPC endpoints
    # connect to your workspace. For details, see `allowed_vpc_endpoint_ids`.
    private_access_level: "PrivateAccessLevel"
    # Databricks Account API private access settings ID.
    private_access_settings_id: str  # path
    # The human-readable name of the private access settings object.
    private_access_settings_name: str
    # Determines if the workspace can be accessed over public internet. For
    # fully private workspaces, you can optionally specify `false`, but only if
    # you implement both the front-end and the back-end PrivateLink connections.
    # Otherwise, specify `true`, which means that public access is enabled.
    public_access_enabled: bool
    # The AWS region for workspaces associated with this private access settings
    # object. This must be a [region that Databricks supports for PrivateLink].
    #
    # [region that Databricks supports for PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/regions.html
    region: str

    def as_request(self) -> (dict, dict):
        (
            upsertPrivateAccessSettingsRequest_query,
            upsertPrivateAccessSettingsRequest_body,
        ) = ({}, {})
        if self.allowed_vpc_endpoint_ids:
            upsertPrivateAccessSettingsRequest_body["allowed_vpc_endpoint_ids"] = [
                v for v in self.allowed_vpc_endpoint_ids
            ]
        if self.private_access_level:
            upsertPrivateAccessSettingsRequest_body[
                "private_access_level"
            ] = self.private_access_level.value
        if self.private_access_settings_id:
            upsertPrivateAccessSettingsRequest_body[
                "private_access_settings_id"
            ] = self.private_access_settings_id
        if self.private_access_settings_name:
            upsertPrivateAccessSettingsRequest_body[
                "private_access_settings_name"
            ] = self.private_access_settings_name
        if self.public_access_enabled:
            upsertPrivateAccessSettingsRequest_body[
                "public_access_enabled"
            ] = self.public_access_enabled
        if self.region:
            upsertPrivateAccessSettingsRequest_body["region"] = self.region

        return (
            upsertPrivateAccessSettingsRequest_query,
            upsertPrivateAccessSettingsRequest_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpsertPrivateAccessSettingsRequest":
        return cls(
            allowed_vpc_endpoint_ids=d.get("allowed_vpc_endpoint_ids", None),
            private_access_level=PrivateAccessLevel(d["private_access_level"])
            if "private_access_level" in d
            else None,
            private_access_settings_id=d.get("private_access_settings_id", None),
            private_access_settings_name=d.get("private_access_settings_name", None),
            public_access_enabled=d.get("public_access_enabled", None),
            region=d.get("region", None),
        )


@dataclass
class VpcEndpoint:

    # The Databricks account ID that hosts the VPC endpoint configuration.
    account_id: str
    # The AWS Account in which the VPC endpoint object exists.
    aws_account_id: str
    # The ID of the Databricks [endpoint service] that this VPC endpoint is
    # connected to. For a list of endpoint service IDs for each supported AWS
    # region, see the [Databricks PrivateLink documentation].
    #
    # [Databricks PrivateLink documentation]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
    # [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service.html
    aws_endpoint_service_id: str
    # The ID of the VPC endpoint object in AWS.
    aws_vpc_endpoint_id: str
    # The AWS region in which this VPC endpoint object exists.
    region: str
    # The current state (such as `available` or `rejected`) of the VPC endpoint.
    # Derived from AWS. For the full set of values, see [AWS DescribeVpcEndpoint
    # documentation].
    #
    # [AWS DescribeVpcEndpoint documentation]: https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html
    state: str
    # This enumeration represents the type of Databricks VPC [endpoint service]
    # that was used when creating this VPC endpoint.
    #
    # If the VPC endpoint connects to the Databricks control plane for either
    # the front-end connection or the back-end REST API connection, the value is
    # `WORKSPACE_ACCESS`.
    #
    # If the VPC endpoint connects to the Databricks workspace for the back-end
    # [secure cluster connectivity] relay, the value is
    # `DATAPLANE_RELAY_ACCESS`.
    #
    # [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service.html
    # [secure cluster connectivity]: https://docs.databricks.com/security/secure-cluster-connectivity.html
    use_case: "EndpointUseCase"
    # Databricks VPC endpoint ID. This is the Databricks-specific name of the
    # VPC endpoint. Do not confuse this with the `aws_vpc_endpoint_id`, which is
    # the ID within AWS of the VPC endpoint.
    vpc_endpoint_id: str
    # The human-readable name of the storage configuration.
    vpc_endpoint_name: str

    def as_request(self) -> (dict, dict):
        vpcEndpoint_query, vpcEndpoint_body = {}, {}
        if self.account_id:
            vpcEndpoint_body["account_id"] = self.account_id
        if self.aws_account_id:
            vpcEndpoint_body["aws_account_id"] = self.aws_account_id
        if self.aws_endpoint_service_id:
            vpcEndpoint_body["aws_endpoint_service_id"] = self.aws_endpoint_service_id
        if self.aws_vpc_endpoint_id:
            vpcEndpoint_body["aws_vpc_endpoint_id"] = self.aws_vpc_endpoint_id
        if self.region:
            vpcEndpoint_body["region"] = self.region
        if self.state:
            vpcEndpoint_body["state"] = self.state
        if self.use_case:
            vpcEndpoint_body["use_case"] = self.use_case.value
        if self.vpc_endpoint_id:
            vpcEndpoint_body["vpc_endpoint_id"] = self.vpc_endpoint_id
        if self.vpc_endpoint_name:
            vpcEndpoint_body["vpc_endpoint_name"] = self.vpc_endpoint_name

        return vpcEndpoint_query, vpcEndpoint_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "VpcEndpoint":
        return cls(
            account_id=d.get("account_id", None),
            aws_account_id=d.get("aws_account_id", None),
            aws_endpoint_service_id=d.get("aws_endpoint_service_id", None),
            aws_vpc_endpoint_id=d.get("aws_vpc_endpoint_id", None),
            region=d.get("region", None),
            state=d.get("state", None),
            use_case=EndpointUseCase(d["use_case"]) if "use_case" in d else None,
            vpc_endpoint_id=d.get("vpc_endpoint_id", None),
            vpc_endpoint_name=d.get("vpc_endpoint_name", None),
        )


class VpcStatus(Enum):
    """This describes an enum"""

    BROKEN = "BROKEN"
    UNATTACHED = "UNATTACHED"
    VALID = "VALID"
    WARNED = "WARNED"


class WarningType(Enum):
    """The AWS resource associated with this warning: a subnet or a security group."""

    securityGroup = "securityGroup"
    subnet = "subnet"


@dataclass
class Workspace:

    # Databricks account ID.
    account_id: str
    # The AWS region of the workspace data plane (for example, `us-west-2`).
    aws_region: str
    # The cloud name. This field always has the value `gcp`.
    cloud: str
    # The general workspace configurations that are specific to cloud providers.
    cloud_resource_bucket: "CloudResourceBucket"
    # Time in epoch milliseconds when the workspace was created.
    creation_time: int
    # ID of the workspace's credential configuration object.
    credentials_id: str
    # The deployment name defines part of the subdomain for the workspace. The
    # workspace URL for web application and REST APIs is
    # `<deployment-name>.cloud.databricks.com`.
    #
    # This value must be unique across all non-deleted deployments across all
    # AWS regions.
    deployment_name: str
    # The Google Cloud region of the workspace data plane in your Google account
    # (for example, `us-east4`).
    location: str
    # ID of the key configuration for encrypting managed services.
    managed_services_customer_managed_key_id: str

    network: "GcpNetwork"
    # The pricing tier of the workspace. For pricing tier information, see [AWS
    # Pricing].
    #
    # [AWS Pricing]: https://databricks.com/product/aws-pricing
    pricing_tier: "PricingTier"
    # ID of the workspace's private access settings object. Only used for
    # PrivateLink (Public Preview). You must specify this ID if you are using
    # [AWS PrivateLink] for either front-end (user-to-workspace connection),
    # back-end (data plane to control plane connection), or both connection
    # types.
    #
    # Before configuring PrivateLink, read the [Databricks article about
    # PrivateLink].
    #
    # [AWS PrivateLink]: https://aws.amazon.com/privatelink/
    # [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
    private_access_settings_id: str
    # ID of the workspace's storage configuration object.
    storage_configuration_id: str
    # ID of the key configuration for encrypting workspace storage.
    storage_customer_managed_key_id: str
    # Workspace ID.
    workspace_id: int
    # The human-readable name of the workspace.
    workspace_name: str
    # The status of the workspace. For workspace creation, usually it is set to
    # `PROVISIONING` initially. Continue to check the status until the status is
    # `RUNNING`.
    workspace_status: "WorkspaceStatus"
    # Message describing the current workspace status.
    workspace_status_message: str

    def as_request(self) -> (dict, dict):
        workspace_query, workspace_body = {}, {}
        if self.account_id:
            workspace_body["account_id"] = self.account_id
        if self.aws_region:
            workspace_body["aws_region"] = self.aws_region
        if self.cloud:
            workspace_body["cloud"] = self.cloud
        if self.cloud_resource_bucket:
            workspace_body[
                "cloud_resource_bucket"
            ] = self.cloud_resource_bucket.as_request()[1]
        if self.creation_time:
            workspace_body["creation_time"] = self.creation_time
        if self.credentials_id:
            workspace_body["credentials_id"] = self.credentials_id
        if self.deployment_name:
            workspace_body["deployment_name"] = self.deployment_name
        if self.location:
            workspace_body["location"] = self.location
        if self.managed_services_customer_managed_key_id:
            workspace_body[
                "managed_services_customer_managed_key_id"
            ] = self.managed_services_customer_managed_key_id
        if self.network:
            workspace_body["network"] = self.network.as_request()[1]
        if self.pricing_tier:
            workspace_body["pricing_tier"] = self.pricing_tier.value
        if self.private_access_settings_id:
            workspace_body[
                "private_access_settings_id"
            ] = self.private_access_settings_id
        if self.storage_configuration_id:
            workspace_body["storage_configuration_id"] = self.storage_configuration_id
        if self.storage_customer_managed_key_id:
            workspace_body[
                "storage_customer_managed_key_id"
            ] = self.storage_customer_managed_key_id
        if self.workspace_id:
            workspace_body["workspace_id"] = self.workspace_id
        if self.workspace_name:
            workspace_body["workspace_name"] = self.workspace_name
        if self.workspace_status:
            workspace_body["workspace_status"] = self.workspace_status.value
        if self.workspace_status_message:
            workspace_body["workspace_status_message"] = self.workspace_status_message

        return workspace_query, workspace_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Workspace":
        return cls(
            account_id=d.get("account_id", None),
            aws_region=d.get("aws_region", None),
            cloud=d.get("cloud", None),
            cloud_resource_bucket=CloudResourceBucket.from_dict(
                d["cloud_resource_bucket"]
            )
            if "cloud_resource_bucket" in d
            else None,
            creation_time=d.get("creation_time", None),
            credentials_id=d.get("credentials_id", None),
            deployment_name=d.get("deployment_name", None),
            location=d.get("location", None),
            managed_services_customer_managed_key_id=d.get(
                "managed_services_customer_managed_key_id", None
            ),
            network=GcpNetwork.from_dict(d["network"]) if "network" in d else None,
            pricing_tier=PricingTier(d["pricing_tier"])
            if "pricing_tier" in d
            else None,
            private_access_settings_id=d.get("private_access_settings_id", None),
            storage_configuration_id=d.get("storage_configuration_id", None),
            storage_customer_managed_key_id=d.get(
                "storage_customer_managed_key_id", None
            ),
            workspace_id=d.get("workspace_id", None),
            workspace_name=d.get("workspace_name", None),
            workspace_status=WorkspaceStatus(d["workspace_status"])
            if "workspace_status" in d
            else None,
            workspace_status_message=d.get("workspace_status_message", None),
        )


class WorkspaceStatus(Enum):
    """The status of the workspace. For workspace creation, usually it is set to
    `PROVISIONING` initially. Continue to check the status until the status is
    `RUNNING`."""

    BANNED = "BANNED"
    CANCELLING = "CANCELLING"
    FAILED = "FAILED"
    NOT_PROVISIONED = "NOT_PROVISIONED"
    PROVISIONING = "PROVISIONING"
    RUNNING = "RUNNING"


class CredentialsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateCredentialRequest) -> Credential:
        """Create credential configuration.

        Creates a Databricks credential configuration that represents cloud
        cross-account credentials for a specified account. Databricks uses this
        to set up network infrastructure properly to host Databricks clusters.
        For your AWS IAM role, you need to trust the External ID (the Databricks
        Account API account ID) in the returned credential object, and configure
        the required access policy.

        Save the response's `credentials_id` field, which is the ID for your new
        credential configuration object.

        For information about how to create a new workspace with this API, see
        [Create a new workspace using the Account API]

        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html"""
        query, body = request.as_request()
        json = self._api.do(
            "POST", f"/api/2.0/accounts//credentials", query=query, body=body
        )
        return Credential.from_dict(json)

    def delete(self, request: DeleteCredentialRequest):
        """Delete credential configuration.

        Deletes a Databricks credential configuration object for an account,
        both specified by ID. You cannot delete a credential that is associated
        with any workspace."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/accounts//credentials/{request.credentials_id}",
            query=query,
            body=body,
        )

    def get(self, request: GetCredentialRequest) -> Credential:
        """Get credential configuration.

        Gets a Databricks credential configuration object for an account, both
        specified by ID."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/accounts//credentials/{request.credentials_id}",
            query=query,
            body=body,
        )
        return Credential.from_dict(json)

    def list(self) -> CredentialList:
        """Get all credential configurations.

        Gets all Databricks credential configurations associated with an account
        specified by ID."""

        json = self._api.do("GET", f"/api/2.0/accounts//credentials")
        return CredentialList.from_dict(json)


class EncryptionKeysAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateCustomerManagedKeyRequest) -> CustomerManagedKey:
        """Create encryption key configuration.

        Creates a customer-managed key configuration object for an account,
        specified by ID. This operation uploads a reference to a
        customer-managed key to Databricks. If the key is assigned as a
        workspace's customer-managed key for managed services, Databricks uses
        the key to encrypt the workspaces notebooks and secrets in the control
        plane, in addition to Databricks SQL queries and query history. If it is
        specified as a workspace's customer-managed key for workspace storage,
        the key encrypts the workspace's root S3 bucket (which contains the
        workspace's root DBFS and system data) and, optionally, cluster EBS
        volume data.

        **Important**: Customer-managed keys are supported only for some
        deployment types, subscription types, and AWS regions.

        This operation is available only if your account is on the E2 version of
        the platform or on a select custom plan that allows multiple workspaces
        per account."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", f"/api/2.0/accounts//customer-managed-keys", query=query, body=body
        )
        return CustomerManagedKey.from_dict(json)

    def delete(self, request: DeleteEncryptionKeyRequest):
        """Delete encryption key configuration.

        Deletes a customer-managed key configuration object for an account. You
        cannot delete a configuration that is associated with a running
        workspace."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/accounts//customer-managed-keys/{request.customer_managed_key_id}",
            query=query,
            body=body,
        )

    def get(self, request: GetEncryptionKeyRequest) -> CustomerManagedKey:
        """Get encryption key configuration.

        Gets a customer-managed key configuration object for an account,
        specified by ID. This operation uploads a reference to a
        customer-managed key to Databricks. If assigned as a workspace's
        customer-managed key for managed services, Databricks uses the key to
        encrypt the workspaces notebooks and secrets in the control plane, in
        addition to Databricks SQL queries and query history. If it is specified
        as a workspace's customer-managed key for storage, the key encrypts the
        workspace's root S3 bucket (which contains the workspace's root DBFS and
        system data) and, optionally, cluster EBS volume data.

        **Important**: Customer-managed keys are supported only for some
        deployment types, subscription types, and AWS regions.

        This operation is available only if your account is on the E2 version of
        the platform."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/accounts//customer-managed-keys/{request.customer_managed_key_id}",
            query=query,
            body=body,
        )
        return CustomerManagedKey.from_dict(json)

    def list(self) -> CustomerManagedKeyList:
        """Get all encryption key configurations.

        Gets all customer-managed key configuration objects for an account. If
        the key is specified as a workspace's managed services customer-managed
        key, Databricks uses the key to encrypt the workspace's notebooks and
        secrets in the control plane, in addition to Databricks SQL queries and
        query history. If the key is specified as a workspace's storage
        customer-managed key, the key is used to encrypt the workspace's root S3
        bucket and optionally can encrypt cluster EBS volumes data in the data
        plane.

        **Important**: Customer-managed keys are supported only for some
        deployment types, subscription types, and AWS regions.

        This operation is available only if your account is on the E2 version of
        the platform."""

        json = self._api.do("GET", f"/api/2.0/accounts//customer-managed-keys")
        return CustomerManagedKeyList.from_dict(json)


class NetworksAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateNetworkRequest) -> Network:
        """Create network configuration.

        Creates a Databricks network configuration that represents an AWS VPC
        and its resources. The VPC will be used for new Databricks clusters.
        This requires a pre-existing VPC and subnets. For VPC requirements, see
        [Customer-managed VPC].

        **Important**: You can share one customer-managed VPC with multiple
        workspaces in a single account. Therefore, you can share one VPC across
        multiple Account API network configurations. However, you **cannot**
        reuse subnets or Security Groups between workspaces. Because a
        Databricks Account API network configuration encapsulates this
        information, you cannot reuse a Databricks Account API network
        configuration across workspaces. If you plan to share one VPC with
        multiple workspaces, make sure you size your VPC and subnets
        accordingly. For information about how to create a new workspace with
        this API, see [Create a new workspace using the Account API].

        This operation is available only if your account is on the E2 version of
        the platform.

        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html
        [Customer-managed VPC]: http://docs.databricks.com/administration-guide/cloud-configurations/aws/customer-managed-vpc.html"""
        query, body = request.as_request()
        json = self._api.do(
            "POST", f"/api/2.0/accounts//networks", query=query, body=body
        )
        return Network.from_dict(json)

    def delete(self, request: DeleteNetworkRequest):
        """Delete network configuration.

        Deletes a Databricks network configuration, which represents an AWS VPC
        and its resources. You cannot delete a network that is associated with a
        workspace.

        This operation is available only if your account is on the E2 version of
        the platform."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/accounts//networks/{request.network_id}",
            query=query,
            body=body,
        )

    def get(self, request: GetNetworkRequest) -> Network:
        """Get a network configuration.

        Gets a Databricks network configuration, which represents an AWS VPC and
        its resources. This requires a pre-existing VPC and subnets. For VPC
        requirements, see [Customer-managed VPC].

        This operation is available only if your account is on the E2 version of
        the platform.

        [Customer-managed VPC]: http://docs.databricks.com/administration-guide/cloud-configurations/aws/customer-managed-vpc.html"""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/accounts//networks/{request.network_id}",
            query=query,
            body=body,
        )
        return Network.from_dict(json)

    def list(self) -> NetworkList:
        """Get all network configurations.

        Gets a list of all Databricks network configurations for an account,
        specified by ID.

        This operation is available only if your account is on the E2 version of
        the platform."""

        json = self._api.do("GET", f"/api/2.0/accounts//networks")
        return NetworkList.from_dict(json)


class PrivateAccessAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self, request: UpsertPrivateAccessSettingsRequest
    ) -> PrivateAccessSettings:
        """Create private access settings.

        Creates a private access settings object, which specifies how your
        workspace is accessed over [AWS PrivateLink]. To use AWS PrivateLink, a
        workspace must have a private access settings object referenced by ID in
        the workspace's `private_access_settings_id` property.

        You can share one private access settings with multiple workspaces in a
        single account. However, private access settings are specific to AWS
        regions, so only workspaces in the same AWS region can use a given
        private access settings object.

        Before configuring PrivateLink, read the [Databricks article about
        PrivateLink].

        This operation is available only if your account is on the E2 version of
        the platform and your Databricks account is enabled for PrivateLink
        (Public Preview). Contact your Databricks representative to enable your
        account for PrivateLink.

        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            f"/api/2.0/accounts//private-access-settings",
            query=query,
            body=body,
        )
        return PrivateAccessSettings.from_dict(json)

    def delete(self, request: DeletePrivateAccesRequest):
        """Delete a private access settings object.

        Deletes a private access settings object, which determines how your
        workspace is accessed over [AWS PrivateLink].

        Before configuring PrivateLink, read the [Databricks article about
        PrivateLink].

        This operation is available only if your account is on the E2 version of
        the platform and your Databricks account is enabled for PrivateLink
        (Public Preview). Contact your Databricks representative to enable your
        account for PrivateLink.

        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/accounts//private-access-settings/{request.private_access_settings_id}",
            query=query,
            body=body,
        )

    def get(self, request: GetPrivateAccesRequest) -> PrivateAccessSettings:
        """Get a private access settings object.

        Gets a private access settings object, which specifies how your
        workspace is accessed over [AWS PrivateLink].

        Before configuring PrivateLink, read the [Databricks article about
        PrivateLink].

        This operation is available only if your account is on the E2 version of
        the platform and your Databricks account is enabled for PrivateLink
        (Public Preview). Contact your Databricks representative to enable your
        account for PrivateLink.

        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/accounts//private-access-settings/{request.private_access_settings_id}",
            query=query,
            body=body,
        )
        return PrivateAccessSettings.from_dict(json)

    def list(self) -> PrivateAccessSettingsList:
        """Get all private access settings objects.

        Gets a list of all private access settings objects for an account,
        specified by ID.

        This operation is available only if your account is on the E2 version of
        the platform and your Databricks account is enabled for AWS PrivateLink
        (Public Preview). Contact your Databricks representative to enable your
        account for PrivateLink."""

        json = self._api.do("GET", f"/api/2.0/accounts//private-access-settings")
        return PrivateAccessSettingsList.from_dict(json)

    def replace(self, request: UpsertPrivateAccessSettingsRequest):
        """Replace private access settings.

        Updates an existing private access settings object, which specifies how
        your workspace is accessed over [AWS PrivateLink]. To use AWS
        PrivateLink, a workspace must have a private access settings object
        referenced by ID in the workspace's `private_access_settings_id`
        property.

        This operation completely overwrites your existing private access
        settings object attached to your workspaces. All workspaces attached to
        the private access settings are affected by any change. If
        `public_access_enabled`, `private_access_level`, or
        `allowed_vpc_endpoint_ids` are updated, effects of these changes might
        take several minutes to propagate to the workspace API. You can share
        one private access settings object with multiple workspaces in a single
        account. However, private access settings are specific to AWS regions,
        so only workspaces in the same AWS region can use a given private access
        settings object.

        Before configuring PrivateLink, read the [Databricks article about
        PrivateLink].

        This operation is available only if your account is on the E2 version of
        the platform and your Databricks account is enabled for PrivateLink
        (Public Preview). Contact your Databricks representative to enable your
        account for PrivateLink.

        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""
        query, body = request.as_request()
        self._api.do(
            "PUT",
            f"/api/2.0/accounts//private-access-settings/{request.private_access_settings_id}",
            query=query,
            body=body,
        )


class StorageAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self, request: CreateStorageConfigurationRequest
    ) -> StorageConfiguration:
        """Create new storage configuration.

        Creates new storage configuration for an account, specified by ID.
        Uploads a storage configuration object that represents the root AWS S3
        bucket in your account. Databricks stores related workspace assets
        including DBFS, cluster logs, and job results. For the AWS S3 bucket,
        you need to configure the required bucket policy.

        For information about how to create a new workspace with this API, see
        [Create a new workspace using the Account API]

        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html"""
        query, body = request.as_request()
        json = self._api.do(
            "POST", f"/api/2.0/accounts//storage-configurations", query=query, body=body
        )
        return StorageConfiguration.from_dict(json)

    def delete(self, request: DeleteStorageRequest):
        """Delete storage configuration.

        Deletes a Databricks storage configuration. You cannot delete a storage
        configuration that is associated with any workspace."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/accounts//storage-configurations/{request.storage_configuration_id}",
            query=query,
            body=body,
        )

    def get(self, request: GetStorageRequest) -> StorageConfiguration:
        """Get storage configuration.

        Gets a Databricks storage configuration for an account, both specified
        by ID."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/accounts//storage-configurations/{request.storage_configuration_id}",
            query=query,
            body=body,
        )
        return StorageConfiguration.from_dict(json)

    def list(self) -> StorageConfigurationList:
        """Get all storage configurations.

        Gets a list of all Databricks storage configurations for your account,
        specified by ID."""

        json = self._api.do("GET", f"/api/2.0/accounts//storage-configurations")
        return StorageConfigurationList.from_dict(json)


class VpcEndpointsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateVpcEndpointRequest) -> VpcEndpoint:
        """Create VPC endpoint configuration.

        Creates a VPC endpoint configuration, which represents a [VPC endpoint]
        object in AWS used to communicate privately with Databricks over [AWS
        PrivateLink].

        **Important**: When you register a VPC endpoint to the Databricks
        workspace VPC endpoint service for any workspace, **in this release
        Databricks enables front-end (web application and REST API) access from
        the source network of the VPC endpoint to all workspaces in that AWS
        region in your Databricks account if the workspaces have any PrivateLink
        connections in their workspace configuration**. If you have questions
        about this behavior, contact your Databricks representative.

        Within AWS, your VPC endpoint stays in `pendingAcceptance` state until
        you register it in a VPC endpoint configuration through the Account API.
        After you register the VPC endpoint configuration, the Databricks
        [endpoint service] automatically accepts the VPC endpoint and it
        eventually transitions to the `available` state.

        Before configuring PrivateLink, read the [Databricks article about
        PrivateLink].

        This operation is available only if your account is on the E2 version of
        the platform and your Databricks account is enabled for PrivateLink
        (Public Preview). Contact your Databricks representative to enable your
        account for PrivateLink.

        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        [VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html
        [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html"""
        query, body = request.as_request()
        json = self._api.do(
            "POST", f"/api/2.0/accounts//vpc-endpoints", query=query, body=body
        )
        return VpcEndpoint.from_dict(json)

    def delete(self, request: DeleteVpcEndpointRequest):
        """Delete VPC endpoint configuration.

        Deletes a VPC endpoint configuration, which represents an [AWS VPC
        endpoint] that can communicate privately with Databricks over [AWS
        PrivateLink].

        Upon deleting a VPC endpoint configuration, the VPC endpoint in AWS
        changes its state from `accepted` to `rejected`, which means that it is
        no longer usable from your VPC.

        Before configuring PrivateLink, read the [Databricks article about
        PrivateLink].

        This operation is available only if your account is on the E2 version of
        the platform and your Databricks account is enabled for PrivateLink
        (Public Preview). Contact your Databricks representative to enable your
        account for PrivateLink.

        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [AWS VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/accounts//vpc-endpoints/{request.vpc_endpoint_id}",
            query=query,
            body=body,
        )

    def get(self, request: GetVpcEndpointRequest) -> VpcEndpoint:
        """Get a VPC endpoint configuration.

        Gets a VPC endpoint configuration, which represents a [VPC endpoint]
        object in AWS used to communicate privately with Databricks over [AWS
        PrivateLink].

        This operation is available only if your account is on the E2 version of
        the platform and your Databricks account is enabled for PrivateLink
        (Public Preview). Contact your Databricks representative to enable your
        account for PrivateLink.

        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html"""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/accounts//vpc-endpoints/{request.vpc_endpoint_id}",
            query=query,
            body=body,
        )
        return VpcEndpoint.from_dict(json)

    def list(self) -> VpcEndpointList:
        """Get all VPC endpoint configurations.

        Gets a list of all VPC endpoints for an account, specified by ID.

        Before configuring PrivateLink, read the [Databricks article about
        PrivateLink].

        This operation is available only if your account is on the E2 version of
        the platform and your Databricks account is enabled for PrivateLink
        (Public Preview). Contact your Databricks representative to enable your
        account for PrivateLink.

        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""

        json = self._api.do("GET", f"/api/2.0/accounts//vpc-endpoints")
        return VpcEndpointList.from_dict(json)


class WorkspacesAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateWorkspaceRequest) -> Workspace:
        """Create a new workspace.

        Creates a new workspace using a credential configuration and a storage
        configuration, an optional network configuration (if using a
        customer-managed VPC), an optional managed services key configuration
        (if using customer-managed keys for managed services), and an optional
        storage key configuration (if using customer-managed keys for storage).
        The key configurations used for managed services and storage encryption
        can be the same or different.

        **Important**: This operation is asynchronous. A response with HTTP
        status code 200 means the request has been accepted and is in progress,
        but does not mean that the workspace deployed successfully and is
        running. The initial workspace status is typically `PROVISIONING`. Use
        the workspace ID (`workspace_id`) field in the response to identify the
        new workspace and make repeated `GET` requests with the workspace ID and
        check its status. The workspace becomes available when the status
        changes to `RUNNING`.

        You can share one customer-managed VPC with multiple workspaces in a
        single account. It is not required to create a new VPC for each
        workspace. However, you **cannot** reuse subnets or Security Groups
        between workspaces. If you plan to share one VPC with multiple
        workspaces, make sure you size your VPC and subnets accordingly. Because
        a Databricks Account API network configuration encapsulates this
        information, you cannot reuse a Databricks Account API network
        configuration across workspaces.\nFor information about how to create a
        new workspace with this API **including error handling**, see [Create a
        new workspace using the Account API].

        **Important**: Customer-managed VPCs, PrivateLink, and customer-managed
        keys are supported on a limited set of deployment and subscription
        types. If you have questions about availability, contact your Databricks
        representative.\n\nThis operation is available only if your account is
        on the E2 version of the platform or on a select custom plan that allows
        multiple workspaces per account.

        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html"""
        query, body = request.as_request()
        json = self._api.do(
            "POST", f"/api/2.0/accounts//workspaces", query=query, body=body
        )
        return Workspace.from_dict(json)

    def delete(self, request: DeleteWorkspaceRequest):
        """Delete workspace.

        Terminates and deletes a Databricks workspace. From an API perspective,
        deletion is immediate. However, it might take a few minutes for all
        workspaces resources to be deleted, depending on the size and number of
        workspace resources.

        This operation is available only if your account is on the E2 version of
        the platform or on a select custom plan that allows multiple workspaces
        per account."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/accounts//workspaces/{request.workspace_id}",
            query=query,
            body=body,
        )

    def get(self, request: GetWorkspaceRequest) -> Workspace:
        """Get workspace.

        Gets information including status for a Databricks workspace, specified
        by ID. In the response, the `workspace_status` field indicates the
        current status. After initial workspace creation (which is
        asynchronous), make repeated `GET` requests with the workspace ID and
        check its status. The workspace becomes available when the status
        changes to `RUNNING`.

        For information about how to create a new workspace with this API
        **including error handling**, see [Create a new workspace using the
        Account API].

        This operation is available only if your account is on the E2 version of
        the platform or on a select custom plan that allows multiple workspaces
        per account.

        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html"""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/accounts//workspaces/{request.workspace_id}",
            query=query,
            body=body,
        )
        return Workspace.from_dict(json)

    def list(self) -> WorkspaceList:
        """Get all workspaces.

        Gets a list of all workspaces associated with an account, specified by
        ID.

        This operation is available only if your account is on the E2 version of
        the platform or on a select custom plan that allows multiple workspaces
        per account."""

        json = self._api.do("GET", f"/api/2.0/accounts//workspaces")
        return WorkspaceList.from_dict(json)

    def update(self, request: UpdateWorkspaceRequest):
        """Update workspace configuration.

        Updates a workspace configuration for either a running workspace or a
        failed workspace. The elements that can be updated varies between these
        two use cases.

        ### Update a failed workspace You can update a Databricks workspace
        configuration for failed workspace deployment for some fields, but not
        all fields. For a failed workspace, this request supports updates to the
        following fields only: - Credential configuration ID - Storage
        configuration ID - Network configuration ID. Used only if you use
        customer-managed VPC. - Key configuration ID for managed services
        (control plane storage, such as notebook source and Databricks SQL
        queries). Used only if you use customer-managed keys for managed
        services. - Key configuration ID for workspace storage (root S3 bucket
        and, optionally, EBS volumes). Used only if you use customer-managed
        keys for workspace storage. **Important**: If the workspace was ever in
        the running state, even if briefly before becoming a failed workspace,
        you cannot add a new key configuration ID for workspace storage.

        After calling the `PATCH` operation to update the workspace
        configuration, make repeated `GET` requests with the workspace ID and
        check the workspace status. The workspace is successful if the status
        changes to `RUNNING`.

        For information about how to create a new workspace with this API
        **including error handling**, see [Create a new workspace using the
        Account API].

        ### Update a running workspace You can update a Databricks workspace
        configuration for running workspaces for some fields, but not all
        fields. For a running workspace, this request supports updating the
        following fields only: - Credential configuration ID

        - Network configuration ID. Used only if you already use use
        customer-managed VPC. This change is supported only if you specified a
        network configuration ID in your original workspace creation. In other
        words, you cannot switch from a Databricks-managed VPC to a
        customer-managed VPC. **Note**: You cannot use a network configuration
        update in this API to add support for PrivateLink (in Public Preview).
        To add PrivateLink to an existing workspace, contact your Databricks
        representative.

        - Key configuration ID for managed services (control plane storage, such
        as notebook source and Databricks SQL queries). Databricks does not
        directly encrypt the data with the customer-managed key (CMK).
        Databricks uses both the CMK and the Databricks managed key (DMK) that
        is unique to your workspace to encrypt the Data Encryption Key (DEK).
        Databricks uses the DEK to encrypt your workspace's managed services
        persisted data. If the workspace does not already have a CMK for managed
        services, adding this ID enables managed services encryption for new or
        updated data. Existing managed services data that existed before adding
        the key remains not encrypted with the DEK until it is modified. If the
        workspace already has customer-managed keys for managed services, this
        request rotates (changes) the CMK keys and the DEK is re-encrypted with
        the DMK and the new CMK. - Key configuration ID for workspace storage
        (root S3 bucket and, optionally, EBS volumes). You can set this only if
        the workspace does not already have a customer-managed key configuration
        for workspace storage.

        **Important**: For updating running workspaces, this API is unavailable
        on Mondays, Tuesdays, and Thursdays from 4:30pm-7:30pm PST due to
        routine maintenance. Plan your workspace updates accordingly. For
        questions about this schedule, contact your Databricks representative.

        **Important**: To update a running workspace, your workspace must have
        no running cluster instances, which includes all-purpose clusters, job
        clusters, and pools that might have running clusters. Terminate all
        cluster instances in the workspace before calling this API.

        ### Wait until changes take effect. After calling the `PATCH` operation
        to update the workspace configuration, make repeated `GET` requests with
        the workspace ID and check the workspace status and the status of the
        fields. * For workspaces with a Databricks-managed VPC, the workspace
        status becomes `PROVISIONING` temporarily (typically under 20 minutes).
        If the workspace update is successful, the workspace status changes to
        `RUNNING`. Note that you can also check the workspace status in the
        [Account Console]. However, you cannot use or create clusters for
        another 20 minutes after that status change. This results in a total of
        up to 40 minutes in which you cannot create clusters. If you create or
        use clusters before this time interval elapses, clusters do not launch
        successfully, fail, or could cause other unexpected behavior.

        * For workspaces with a customer-managed VPC, the workspace status stays
        at status `RUNNING` and the VPC change happens immediately. A change to
        the storage customer-managed key configuration ID might take a few
        minutes to update, so continue to check the workspace until you observe
        that it has been updated. If the update fails, the workspace might
        revert silently to its original configuration. After the workspace has
        been updated, you cannot use or create clusters for another 20 minutes.
        If you create or use clusters before this time interval elapses,
        clusters do not launch successfully, fail, or could cause other
        unexpected behavior.

        If you update the _storage_ customer-managed key configurations, it
        takes 20 minutes for the changes to fully take effect. During the 20
        minute wait, it is important that you stop all REST API calls to the
        DBFS API. If you are modifying _only the managed services key
        configuration_, you can omit the 20 minute wait.

        **Important**: Customer-managed keys and customer-managed VPCs are
        supported by only some deployment types and subscription types. If you
        have questions about availability, contact your Databricks
        representative.

        This operation is available only if your account is on the E2 version of
        the platform or on a select custom plan that allows multiple workspaces
        per account.

        [Account Console]: https://docs.databricks.com/administration-guide/account-settings-e2/account-console-e2.html
        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html"""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.0/accounts//workspaces/{request.workspace_id}",
            query=query,
            body=body,
        )

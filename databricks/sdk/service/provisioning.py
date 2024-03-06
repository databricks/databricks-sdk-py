# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
import random
import time
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Callable, Dict, Iterator, List, Optional

from ..errors import OperationFailed
from ._internal import Wait, _enum, _from_dict, _repeated_dict, _repeated_enum

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AwsCredentials:
    sts_role: Optional[StsRole] = None

    def as_dict(self) -> dict:
        """Serializes the AwsCredentials into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.sts_role: body['sts_role'] = self.sts_role.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AwsCredentials:
        """Deserializes the AwsCredentials from a dictionary."""
        return cls(sts_role=_from_dict(d, 'sts_role', StsRole))


@dataclass
class AwsKeyInfo:
    key_arn: str
    """The AWS KMS key's Amazon Resource Name (ARN)."""

    key_region: str
    """The AWS KMS key region."""

    key_alias: Optional[str] = None
    """The AWS KMS key alias."""

    reuse_key_for_cluster_volumes: Optional[bool] = None
    """This field applies only if the `use_cases` property includes `STORAGE`. If this is set to `true`
    or omitted, the key is also used to encrypt cluster EBS volumes. If you do not want to use this
    key for encrypting EBS volumes, set to `false`."""

    def as_dict(self) -> dict:
        """Serializes the AwsKeyInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.key_alias is not None: body['key_alias'] = self.key_alias
        if self.key_arn is not None: body['key_arn'] = self.key_arn
        if self.key_region is not None: body['key_region'] = self.key_region
        if self.reuse_key_for_cluster_volumes is not None:
            body['reuse_key_for_cluster_volumes'] = self.reuse_key_for_cluster_volumes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AwsKeyInfo:
        """Deserializes the AwsKeyInfo from a dictionary."""
        return cls(key_alias=d.get('key_alias', None),
                   key_arn=d.get('key_arn', None),
                   key_region=d.get('key_region', None),
                   reuse_key_for_cluster_volumes=d.get('reuse_key_for_cluster_volumes', None))


@dataclass
class AzureWorkspaceInfo:
    resource_group: Optional[str] = None
    """Azure Resource Group name"""

    subscription_id: Optional[str] = None
    """Azure Subscription ID"""

    def as_dict(self) -> dict:
        """Serializes the AzureWorkspaceInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.resource_group is not None: body['resource_group'] = self.resource_group
        if self.subscription_id is not None: body['subscription_id'] = self.subscription_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AzureWorkspaceInfo:
        """Deserializes the AzureWorkspaceInfo from a dictionary."""
        return cls(resource_group=d.get('resource_group', None),
                   subscription_id=d.get('subscription_id', None))


@dataclass
class CloudResourceContainer:
    """The general workspace configurations that are specific to cloud providers."""

    gcp: Optional[CustomerFacingGcpCloudResourceContainer] = None
    """The general workspace configurations that are specific to Google Cloud."""

    def as_dict(self) -> dict:
        """Serializes the CloudResourceContainer into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.gcp: body['gcp'] = self.gcp.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CloudResourceContainer:
        """Deserializes the CloudResourceContainer from a dictionary."""
        return cls(gcp=_from_dict(d, 'gcp', CustomerFacingGcpCloudResourceContainer))


@dataclass
class CreateAwsKeyInfo:
    key_arn: str
    """The AWS KMS key's Amazon Resource Name (ARN). Note that the key's AWS region is inferred from
    the ARN."""

    key_alias: Optional[str] = None
    """The AWS KMS key alias."""

    reuse_key_for_cluster_volumes: Optional[bool] = None
    """This field applies only if the `use_cases` property includes `STORAGE`. If this is set to `true`
    or omitted, the key is also used to encrypt cluster EBS volumes. To not use this key also for
    encrypting EBS volumes, set this to `false`."""

    def as_dict(self) -> dict:
        """Serializes the CreateAwsKeyInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.key_alias is not None: body['key_alias'] = self.key_alias
        if self.key_arn is not None: body['key_arn'] = self.key_arn
        if self.reuse_key_for_cluster_volumes is not None:
            body['reuse_key_for_cluster_volumes'] = self.reuse_key_for_cluster_volumes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateAwsKeyInfo:
        """Deserializes the CreateAwsKeyInfo from a dictionary."""
        return cls(key_alias=d.get('key_alias', None),
                   key_arn=d.get('key_arn', None),
                   reuse_key_for_cluster_volumes=d.get('reuse_key_for_cluster_volumes', None))


@dataclass
class CreateCredentialAwsCredentials:
    sts_role: Optional[CreateCredentialStsRole] = None

    def as_dict(self) -> dict:
        """Serializes the CreateCredentialAwsCredentials into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.sts_role: body['sts_role'] = self.sts_role.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateCredentialAwsCredentials:
        """Deserializes the CreateCredentialAwsCredentials from a dictionary."""
        return cls(sts_role=_from_dict(d, 'sts_role', CreateCredentialStsRole))


@dataclass
class CreateCredentialRequest:
    credentials_name: str
    """The human-readable name of the credential configuration object."""

    aws_credentials: CreateCredentialAwsCredentials

    def as_dict(self) -> dict:
        """Serializes the CreateCredentialRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_credentials: body['aws_credentials'] = self.aws_credentials.as_dict()
        if self.credentials_name is not None: body['credentials_name'] = self.credentials_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateCredentialRequest:
        """Deserializes the CreateCredentialRequest from a dictionary."""
        return cls(aws_credentials=_from_dict(d, 'aws_credentials', CreateCredentialAwsCredentials),
                   credentials_name=d.get('credentials_name', None))


@dataclass
class CreateCredentialStsRole:
    role_arn: Optional[str] = None
    """The Amazon Resource Name (ARN) of the cross account role."""

    def as_dict(self) -> dict:
        """Serializes the CreateCredentialStsRole into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.role_arn is not None: body['role_arn'] = self.role_arn
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateCredentialStsRole:
        """Deserializes the CreateCredentialStsRole from a dictionary."""
        return cls(role_arn=d.get('role_arn', None))


@dataclass
class CreateCustomerManagedKeyRequest:
    use_cases: List[KeyUseCase]
    """The cases that the key can be used for."""

    aws_key_info: Optional[CreateAwsKeyInfo] = None

    gcp_key_info: Optional[CreateGcpKeyInfo] = None

    def as_dict(self) -> dict:
        """Serializes the CreateCustomerManagedKeyRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_key_info: body['aws_key_info'] = self.aws_key_info.as_dict()
        if self.gcp_key_info: body['gcp_key_info'] = self.gcp_key_info.as_dict()
        if self.use_cases: body['use_cases'] = [v.value for v in self.use_cases]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateCustomerManagedKeyRequest:
        """Deserializes the CreateCustomerManagedKeyRequest from a dictionary."""
        return cls(aws_key_info=_from_dict(d, 'aws_key_info', CreateAwsKeyInfo),
                   gcp_key_info=_from_dict(d, 'gcp_key_info', CreateGcpKeyInfo),
                   use_cases=_repeated_enum(d, 'use_cases', KeyUseCase))


@dataclass
class CreateGcpKeyInfo:
    kms_key_id: str
    """The GCP KMS key's resource name"""

    def as_dict(self) -> dict:
        """Serializes the CreateGcpKeyInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.kms_key_id is not None: body['kms_key_id'] = self.kms_key_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateGcpKeyInfo:
        """Deserializes the CreateGcpKeyInfo from a dictionary."""
        return cls(kms_key_id=d.get('kms_key_id', None))


@dataclass
class CreateNetworkRequest:
    network_name: str
    """The human-readable name of the network configuration."""

    gcp_network_info: Optional[GcpNetworkInfo] = None
    """The Google Cloud specific information for this network (for example, the VPC ID, subnet ID, and
    secondary IP ranges)."""

    security_group_ids: Optional[List[str]] = None
    """IDs of one to five security groups associated with this network. Security group IDs **cannot**
    be used in multiple network configurations."""

    subnet_ids: Optional[List[str]] = None
    """IDs of at least two subnets associated with this network. Subnet IDs **cannot** be used in
    multiple network configurations."""

    vpc_endpoints: Optional[NetworkVpcEndpoints] = None
    """If specified, contains the VPC endpoints used to allow cluster communication from this VPC over
    [AWS PrivateLink].
    
    [AWS PrivateLink]: https://aws.amazon.com/privatelink/"""

    vpc_id: Optional[str] = None
    """The ID of the VPC associated with this network. VPC IDs can be used in multiple network
    configurations."""

    def as_dict(self) -> dict:
        """Serializes the CreateNetworkRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.gcp_network_info: body['gcp_network_info'] = self.gcp_network_info.as_dict()
        if self.network_name is not None: body['network_name'] = self.network_name
        if self.security_group_ids: body['security_group_ids'] = [v for v in self.security_group_ids]
        if self.subnet_ids: body['subnet_ids'] = [v for v in self.subnet_ids]
        if self.vpc_endpoints: body['vpc_endpoints'] = self.vpc_endpoints.as_dict()
        if self.vpc_id is not None: body['vpc_id'] = self.vpc_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateNetworkRequest:
        """Deserializes the CreateNetworkRequest from a dictionary."""
        return cls(gcp_network_info=_from_dict(d, 'gcp_network_info', GcpNetworkInfo),
                   network_name=d.get('network_name', None),
                   security_group_ids=d.get('security_group_ids', None),
                   subnet_ids=d.get('subnet_ids', None),
                   vpc_endpoints=_from_dict(d, 'vpc_endpoints', NetworkVpcEndpoints),
                   vpc_id=d.get('vpc_id', None))


@dataclass
class CreateStorageConfigurationRequest:
    storage_configuration_name: str
    """The human-readable name of the storage configuration."""

    root_bucket_info: RootBucketInfo
    """Root S3 bucket information."""

    def as_dict(self) -> dict:
        """Serializes the CreateStorageConfigurationRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.root_bucket_info: body['root_bucket_info'] = self.root_bucket_info.as_dict()
        if self.storage_configuration_name is not None:
            body['storage_configuration_name'] = self.storage_configuration_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateStorageConfigurationRequest:
        """Deserializes the CreateStorageConfigurationRequest from a dictionary."""
        return cls(root_bucket_info=_from_dict(d, 'root_bucket_info', RootBucketInfo),
                   storage_configuration_name=d.get('storage_configuration_name', None))


@dataclass
class CreateVpcEndpointRequest:
    vpc_endpoint_name: str
    """The human-readable name of the storage configuration."""

    aws_vpc_endpoint_id: Optional[str] = None
    """The ID of the VPC endpoint object in AWS."""

    gcp_vpc_endpoint_info: Optional[GcpVpcEndpointInfo] = None
    """The Google Cloud specific information for this Private Service Connect endpoint."""

    region: Optional[str] = None
    """The AWS region in which this VPC endpoint object exists."""

    def as_dict(self) -> dict:
        """Serializes the CreateVpcEndpointRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_vpc_endpoint_id is not None: body['aws_vpc_endpoint_id'] = self.aws_vpc_endpoint_id
        if self.gcp_vpc_endpoint_info: body['gcp_vpc_endpoint_info'] = self.gcp_vpc_endpoint_info.as_dict()
        if self.region is not None: body['region'] = self.region
        if self.vpc_endpoint_name is not None: body['vpc_endpoint_name'] = self.vpc_endpoint_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateVpcEndpointRequest:
        """Deserializes the CreateVpcEndpointRequest from a dictionary."""
        return cls(aws_vpc_endpoint_id=d.get('aws_vpc_endpoint_id', None),
                   gcp_vpc_endpoint_info=_from_dict(d, 'gcp_vpc_endpoint_info', GcpVpcEndpointInfo),
                   region=d.get('region', None),
                   vpc_endpoint_name=d.get('vpc_endpoint_name', None))


@dataclass
class CreateWorkspaceRequest:
    workspace_name: str
    """The workspace's human-readable name."""

    aws_region: Optional[str] = None
    """The AWS region of the workspace's data plane."""

    cloud: Optional[str] = None
    """The cloud provider which the workspace uses. For Google Cloud workspaces, always set this field
    to `gcp`."""

    cloud_resource_container: Optional[CloudResourceContainer] = None
    """The general workspace configurations that are specific to cloud providers."""

    credentials_id: Optional[str] = None
    """ID of the workspace's credential configuration object."""

    custom_tags: Optional[Dict[str, str]] = None
    """The custom tags key-value pairing that is attached to this workspace. The key-value pair is a
    string of utf-8 characters. The value can be an empty string, with maximum length of 255
    characters. The key can be of maximum length of 127 characters, and cannot be empty."""

    deployment_name: Optional[str] = None
    """The deployment name defines part of the subdomain for the workspace. The workspace URL for the
    web application and REST APIs is `<workspace-deployment-name>.cloud.databricks.com`. For
    example, if the deployment name is `abcsales`, your workspace URL will be
    `https://abcsales.cloud.databricks.com`. Hyphens are allowed. This property supports only the
    set of characters that are allowed in a subdomain.
    
    To set this value, you must have a deployment name prefix. Contact your Databricks account team
    to add an account deployment name prefix to your account.
    
    Workspace deployment names follow the account prefix and a hyphen. For example, if your
    account's deployment prefix is `acme` and the workspace deployment name is `workspace-1`, the
    JSON response for the `deployment_name` field becomes `acme-workspace-1`. The workspace URL
    would be `acme-workspace-1.cloud.databricks.com`.
    
    You can also set the `deployment_name` to the reserved keyword `EMPTY` if you want the
    deployment name to only include the deployment prefix. For example, if your account's deployment
    prefix is `acme` and the workspace deployment name is `EMPTY`, the `deployment_name` becomes
    `acme` only and the workspace URL is `acme.cloud.databricks.com`.
    
    This value must be unique across all non-deleted deployments across all AWS regions.
    
    If a new workspace omits this property, the server generates a unique deployment name for you
    with the pattern `dbc-xxxxxxxx-xxxx`."""

    gcp_managed_network_config: Optional[GcpManagedNetworkConfig] = None
    """The network settings for the workspace. The configurations are only for Databricks-managed VPCs.
    It is ignored if you specify a customer-managed VPC in the `network_id` field.", All the IP
    range configurations must be mutually exclusive. An attempt to create a workspace fails if
    Databricks detects an IP range overlap.
    
    Specify custom IP ranges in CIDR format. The IP ranges for these fields must not overlap, and
    all IP addresses must be entirely within the following ranges: `10.0.0.0/8`, `100.64.0.0/10`,
    `172.16.0.0/12`, `192.168.0.0/16`, and `240.0.0.0/4`.
    
    The sizes of these IP ranges affect the maximum number of nodes for the workspace.
    
    **Important**: Confirm the IP ranges used by your Databricks workspace before creating the
    workspace. You cannot change them after your workspace is deployed. If the IP address ranges for
    your Databricks are too small, IP exhaustion can occur, causing your Databricks jobs to fail. To
    determine the address range sizes that you need, Databricks provides a calculator as a Microsoft
    Excel spreadsheet. See [calculate subnet sizes for a new workspace].
    
    [calculate subnet sizes for a new workspace]: https://docs.gcp.databricks.com/administration-guide/cloud-configurations/gcp/network-sizing.html"""

    gke_config: Optional[GkeConfig] = None
    """The configurations for the GKE cluster of a Databricks workspace."""

    location: Optional[str] = None
    """The Google Cloud region of the workspace data plane in your Google account. For example,
    `us-east4`."""

    managed_services_customer_managed_key_id: Optional[str] = None
    """The ID of the workspace's managed services encryption key configuration object. This is used to
    help protect and control access to the workspace's notebooks, secrets, Databricks SQL queries,
    and query history. The provided key configuration object property `use_cases` must contain
    `MANAGED_SERVICES`."""

    network_id: Optional[str] = None

    pricing_tier: Optional[PricingTier] = None
    """The pricing tier of the workspace. For pricing tier information, see [AWS Pricing].
    
    [AWS Pricing]: https://databricks.com/product/aws-pricing"""

    private_access_settings_id: Optional[str] = None
    """ID of the workspace's private access settings object. Only used for PrivateLink. This ID must be
    specified for customers using [AWS PrivateLink] for either front-end (user-to-workspace
    connection), back-end (data plane to control plane connection), or both connection types.
    
    Before configuring PrivateLink, read the [Databricks article about PrivateLink].",
    
    [AWS PrivateLink]: https://aws.amazon.com/privatelink/
    [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""

    storage_configuration_id: Optional[str] = None
    """The ID of the workspace's storage configuration object."""

    storage_customer_managed_key_id: Optional[str] = None
    """The ID of the workspace's storage encryption key configuration object. This is used to encrypt
    the workspace's root S3 bucket (root DBFS and system data) and, optionally, cluster EBS volumes.
    The provided key configuration object property `use_cases` must contain `STORAGE`."""

    def as_dict(self) -> dict:
        """Serializes the CreateWorkspaceRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_region is not None: body['aws_region'] = self.aws_region
        if self.cloud is not None: body['cloud'] = self.cloud
        if self.cloud_resource_container:
            body['cloud_resource_container'] = self.cloud_resource_container.as_dict()
        if self.credentials_id is not None: body['credentials_id'] = self.credentials_id
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.deployment_name is not None: body['deployment_name'] = self.deployment_name
        if self.gcp_managed_network_config:
            body['gcp_managed_network_config'] = self.gcp_managed_network_config.as_dict()
        if self.gke_config: body['gke_config'] = self.gke_config.as_dict()
        if self.location is not None: body['location'] = self.location
        if self.managed_services_customer_managed_key_id is not None:
            body['managed_services_customer_managed_key_id'] = self.managed_services_customer_managed_key_id
        if self.network_id is not None: body['network_id'] = self.network_id
        if self.pricing_tier is not None: body['pricing_tier'] = self.pricing_tier.value
        if self.private_access_settings_id is not None:
            body['private_access_settings_id'] = self.private_access_settings_id
        if self.storage_configuration_id is not None:
            body['storage_configuration_id'] = self.storage_configuration_id
        if self.storage_customer_managed_key_id is not None:
            body['storage_customer_managed_key_id'] = self.storage_customer_managed_key_id
        if self.workspace_name is not None: body['workspace_name'] = self.workspace_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateWorkspaceRequest:
        """Deserializes the CreateWorkspaceRequest from a dictionary."""
        return cls(aws_region=d.get('aws_region', None),
                   cloud=d.get('cloud', None),
                   cloud_resource_container=_from_dict(d, 'cloud_resource_container', CloudResourceContainer),
                   credentials_id=d.get('credentials_id', None),
                   custom_tags=d.get('custom_tags', None),
                   deployment_name=d.get('deployment_name', None),
                   gcp_managed_network_config=_from_dict(d, 'gcp_managed_network_config',
                                                         GcpManagedNetworkConfig),
                   gke_config=_from_dict(d, 'gke_config', GkeConfig),
                   location=d.get('location', None),
                   managed_services_customer_managed_key_id=d.get('managed_services_customer_managed_key_id',
                                                                  None),
                   network_id=d.get('network_id', None),
                   pricing_tier=_enum(d, 'pricing_tier', PricingTier),
                   private_access_settings_id=d.get('private_access_settings_id', None),
                   storage_configuration_id=d.get('storage_configuration_id', None),
                   storage_customer_managed_key_id=d.get('storage_customer_managed_key_id', None),
                   workspace_name=d.get('workspace_name', None))


@dataclass
class Credential:
    account_id: Optional[str] = None
    """The Databricks account ID that hosts the credential."""

    aws_credentials: Optional[AwsCredentials] = None

    creation_time: Optional[int] = None
    """Time in epoch milliseconds when the credential was created."""

    credentials_id: Optional[str] = None
    """Databricks credential configuration ID."""

    credentials_name: Optional[str] = None
    """The human-readable name of the credential configuration object."""

    def as_dict(self) -> dict:
        """Serializes the Credential into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None: body['account_id'] = self.account_id
        if self.aws_credentials: body['aws_credentials'] = self.aws_credentials.as_dict()
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.credentials_id is not None: body['credentials_id'] = self.credentials_id
        if self.credentials_name is not None: body['credentials_name'] = self.credentials_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Credential:
        """Deserializes the Credential from a dictionary."""
        return cls(account_id=d.get('account_id', None),
                   aws_credentials=_from_dict(d, 'aws_credentials', AwsCredentials),
                   creation_time=d.get('creation_time', None),
                   credentials_id=d.get('credentials_id', None),
                   credentials_name=d.get('credentials_name', None))


CustomTags = Dict[str, str]


@dataclass
class CustomerFacingGcpCloudResourceContainer:
    """The general workspace configurations that are specific to Google Cloud."""

    project_id: Optional[str] = None
    """The Google Cloud project ID, which the workspace uses to instantiate cloud resources for your
    workspace."""

    def as_dict(self) -> dict:
        """Serializes the CustomerFacingGcpCloudResourceContainer into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.project_id is not None: body['project_id'] = self.project_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CustomerFacingGcpCloudResourceContainer:
        """Deserializes the CustomerFacingGcpCloudResourceContainer from a dictionary."""
        return cls(project_id=d.get('project_id', None))


@dataclass
class CustomerManagedKey:
    account_id: Optional[str] = None
    """The Databricks account ID that holds the customer-managed key."""

    aws_key_info: Optional[AwsKeyInfo] = None

    creation_time: Optional[int] = None
    """Time in epoch milliseconds when the customer key was created."""

    customer_managed_key_id: Optional[str] = None
    """ID of the encryption key configuration object."""

    gcp_key_info: Optional[GcpKeyInfo] = None

    use_cases: Optional[List[KeyUseCase]] = None
    """The cases that the key can be used for."""

    def as_dict(self) -> dict:
        """Serializes the CustomerManagedKey into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None: body['account_id'] = self.account_id
        if self.aws_key_info: body['aws_key_info'] = self.aws_key_info.as_dict()
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.customer_managed_key_id is not None:
            body['customer_managed_key_id'] = self.customer_managed_key_id
        if self.gcp_key_info: body['gcp_key_info'] = self.gcp_key_info.as_dict()
        if self.use_cases: body['use_cases'] = [v.value for v in self.use_cases]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CustomerManagedKey:
        """Deserializes the CustomerManagedKey from a dictionary."""
        return cls(account_id=d.get('account_id', None),
                   aws_key_info=_from_dict(d, 'aws_key_info', AwsKeyInfo),
                   creation_time=d.get('creation_time', None),
                   customer_managed_key_id=d.get('customer_managed_key_id', None),
                   gcp_key_info=_from_dict(d, 'gcp_key_info', GcpKeyInfo),
                   use_cases=_repeated_enum(d, 'use_cases', KeyUseCase))


@dataclass
class DeleteResponse:

    def as_dict(self) -> dict:
        """Serializes the DeleteResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteResponse:
        """Deserializes the DeleteResponse from a dictionary."""
        return cls()


class EndpointUseCase(Enum):
    """This enumeration represents the type of Databricks VPC [endpoint service] that was used when
    creating this VPC endpoint.
    
    [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service.html"""

    DATAPLANE_RELAY_ACCESS = 'DATAPLANE_RELAY_ACCESS'
    WORKSPACE_ACCESS = 'WORKSPACE_ACCESS'


class ErrorType(Enum):
    """The AWS resource associated with this error: credentials, VPC, subnet, security group, or
    network ACL."""

    CREDENTIALS = 'credentials'
    NETWORK_ACL = 'networkAcl'
    SECURITY_GROUP = 'securityGroup'
    SUBNET = 'subnet'
    VPC = 'vpc'


@dataclass
class GcpKeyInfo:
    kms_key_id: str
    """The GCP KMS key's resource name"""

    def as_dict(self) -> dict:
        """Serializes the GcpKeyInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.kms_key_id is not None: body['kms_key_id'] = self.kms_key_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GcpKeyInfo:
        """Deserializes the GcpKeyInfo from a dictionary."""
        return cls(kms_key_id=d.get('kms_key_id', None))


@dataclass
class GcpManagedNetworkConfig:
    """The network settings for the workspace. The configurations are only for Databricks-managed VPCs.
    It is ignored if you specify a customer-managed VPC in the `network_id` field.", All the IP
    range configurations must be mutually exclusive. An attempt to create a workspace fails if
    Databricks detects an IP range overlap.
    
    Specify custom IP ranges in CIDR format. The IP ranges for these fields must not overlap, and
    all IP addresses must be entirely within the following ranges: `10.0.0.0/8`, `100.64.0.0/10`,
    `172.16.0.0/12`, `192.168.0.0/16`, and `240.0.0.0/4`.
    
    The sizes of these IP ranges affect the maximum number of nodes for the workspace.
    
    **Important**: Confirm the IP ranges used by your Databricks workspace before creating the
    workspace. You cannot change them after your workspace is deployed. If the IP address ranges for
    your Databricks are too small, IP exhaustion can occur, causing your Databricks jobs to fail. To
    determine the address range sizes that you need, Databricks provides a calculator as a Microsoft
    Excel spreadsheet. See [calculate subnet sizes for a new workspace].
    
    [calculate subnet sizes for a new workspace]: https://docs.gcp.databricks.com/administration-guide/cloud-configurations/gcp/network-sizing.html"""

    gke_cluster_pod_ip_range: Optional[str] = None
    """The IP range from which to allocate GKE cluster pods. No bigger than `/9` and no smaller than
    `/21`."""

    gke_cluster_service_ip_range: Optional[str] = None
    """The IP range from which to allocate GKE cluster services. No bigger than `/16` and no smaller
    than `/27`."""

    subnet_cidr: Optional[str] = None
    """The IP range from which to allocate GKE cluster nodes. No bigger than `/9` and no smaller than
    `/29`."""

    def as_dict(self) -> dict:
        """Serializes the GcpManagedNetworkConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.gke_cluster_pod_ip_range is not None:
            body['gke_cluster_pod_ip_range'] = self.gke_cluster_pod_ip_range
        if self.gke_cluster_service_ip_range is not None:
            body['gke_cluster_service_ip_range'] = self.gke_cluster_service_ip_range
        if self.subnet_cidr is not None: body['subnet_cidr'] = self.subnet_cidr
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GcpManagedNetworkConfig:
        """Deserializes the GcpManagedNetworkConfig from a dictionary."""
        return cls(gke_cluster_pod_ip_range=d.get('gke_cluster_pod_ip_range', None),
                   gke_cluster_service_ip_range=d.get('gke_cluster_service_ip_range', None),
                   subnet_cidr=d.get('subnet_cidr', None))


@dataclass
class GcpNetworkInfo:
    """The Google Cloud specific information for this network (for example, the VPC ID, subnet ID, and
    secondary IP ranges)."""

    network_project_id: str
    """The Google Cloud project ID of the VPC network."""

    vpc_id: str
    """The ID of the VPC associated with this network. VPC IDs can be used in multiple network
    configurations."""

    subnet_id: str
    """The ID of the subnet associated with this network."""

    subnet_region: str
    """The Google Cloud region of the workspace data plane (for example, `us-east4`)."""

    pod_ip_range_name: str
    """The name of the secondary IP range for pods. A Databricks-managed GKE cluster uses this IP range
    for its pods. This secondary IP range can be used by only one workspace."""

    service_ip_range_name: str
    """The name of the secondary IP range for services. A Databricks-managed GKE cluster uses this IP
    range for its services. This secondary IP range can be used by only one workspace."""

    def as_dict(self) -> dict:
        """Serializes the GcpNetworkInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.network_project_id is not None: body['network_project_id'] = self.network_project_id
        if self.pod_ip_range_name is not None: body['pod_ip_range_name'] = self.pod_ip_range_name
        if self.service_ip_range_name is not None: body['service_ip_range_name'] = self.service_ip_range_name
        if self.subnet_id is not None: body['subnet_id'] = self.subnet_id
        if self.subnet_region is not None: body['subnet_region'] = self.subnet_region
        if self.vpc_id is not None: body['vpc_id'] = self.vpc_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GcpNetworkInfo:
        """Deserializes the GcpNetworkInfo from a dictionary."""
        return cls(network_project_id=d.get('network_project_id', None),
                   pod_ip_range_name=d.get('pod_ip_range_name', None),
                   service_ip_range_name=d.get('service_ip_range_name', None),
                   subnet_id=d.get('subnet_id', None),
                   subnet_region=d.get('subnet_region', None),
                   vpc_id=d.get('vpc_id', None))


@dataclass
class GcpVpcEndpointInfo:
    """The Google Cloud specific information for this Private Service Connect endpoint."""

    project_id: str
    """The Google Cloud project ID of the VPC network where the PSC connection resides."""

    psc_endpoint_name: str
    """The name of the PSC endpoint in the Google Cloud project."""

    endpoint_region: str
    """Region of the PSC endpoint."""

    psc_connection_id: Optional[str] = None
    """The unique ID of this PSC connection."""

    service_attachment_id: Optional[str] = None
    """The service attachment this PSC connection connects to."""

    def as_dict(self) -> dict:
        """Serializes the GcpVpcEndpointInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.endpoint_region is not None: body['endpoint_region'] = self.endpoint_region
        if self.project_id is not None: body['project_id'] = self.project_id
        if self.psc_connection_id is not None: body['psc_connection_id'] = self.psc_connection_id
        if self.psc_endpoint_name is not None: body['psc_endpoint_name'] = self.psc_endpoint_name
        if self.service_attachment_id is not None: body['service_attachment_id'] = self.service_attachment_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GcpVpcEndpointInfo:
        """Deserializes the GcpVpcEndpointInfo from a dictionary."""
        return cls(endpoint_region=d.get('endpoint_region', None),
                   project_id=d.get('project_id', None),
                   psc_connection_id=d.get('psc_connection_id', None),
                   psc_endpoint_name=d.get('psc_endpoint_name', None),
                   service_attachment_id=d.get('service_attachment_id', None))


@dataclass
class GkeConfig:
    """The configurations for the GKE cluster of a Databricks workspace."""

    connectivity_type: Optional[GkeConfigConnectivityType] = None
    """Specifies the network connectivity types for the GKE nodes and the GKE master network.
    
    Set to `PRIVATE_NODE_PUBLIC_MASTER` for a private GKE cluster for the workspace. The GKE nodes
    will not have public IPs.
    
    Set to `PUBLIC_NODE_PUBLIC_MASTER` for a public GKE cluster. The nodes of a public GKE cluster
    have public IP addresses."""

    master_ip_range: Optional[str] = None
    """The IP range from which to allocate GKE cluster master resources. This field will be ignored if
    GKE private cluster is not enabled.
    
    It must be exactly as big as `/28`."""

    def as_dict(self) -> dict:
        """Serializes the GkeConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.connectivity_type is not None: body['connectivity_type'] = self.connectivity_type.value
        if self.master_ip_range is not None: body['master_ip_range'] = self.master_ip_range
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GkeConfig:
        """Deserializes the GkeConfig from a dictionary."""
        return cls(connectivity_type=_enum(d, 'connectivity_type', GkeConfigConnectivityType),
                   master_ip_range=d.get('master_ip_range', None))


class GkeConfigConnectivityType(Enum):
    """Specifies the network connectivity types for the GKE nodes and the GKE master network.
    
    Set to `PRIVATE_NODE_PUBLIC_MASTER` for a private GKE cluster for the workspace. The GKE nodes
    will not have public IPs.
    
    Set to `PUBLIC_NODE_PUBLIC_MASTER` for a public GKE cluster. The nodes of a public GKE cluster
    have public IP addresses."""

    PRIVATE_NODE_PUBLIC_MASTER = 'PRIVATE_NODE_PUBLIC_MASTER'
    PUBLIC_NODE_PUBLIC_MASTER = 'PUBLIC_NODE_PUBLIC_MASTER'


class KeyUseCase(Enum):
    """Possible values are: * `MANAGED_SERVICES`: Encrypts notebook and secret data in the control
    plane * `STORAGE`: Encrypts the workspace's root S3 bucket (root DBFS and system data) and,
    optionally, cluster EBS volumes."""

    MANAGED_SERVICES = 'MANAGED_SERVICES'
    STORAGE = 'STORAGE'


@dataclass
class Network:
    account_id: Optional[str] = None
    """The Databricks account ID associated with this network configuration."""

    creation_time: Optional[int] = None
    """Time in epoch milliseconds when the network was created."""

    error_messages: Optional[List[NetworkHealth]] = None
    """Array of error messages about the network configuration."""

    gcp_network_info: Optional[GcpNetworkInfo] = None
    """The Google Cloud specific information for this network (for example, the VPC ID, subnet ID, and
    secondary IP ranges)."""

    network_id: Optional[str] = None
    """The Databricks network configuration ID."""

    network_name: Optional[str] = None
    """The human-readable name of the network configuration."""

    security_group_ids: Optional[List[str]] = None

    subnet_ids: Optional[List[str]] = None

    vpc_endpoints: Optional[NetworkVpcEndpoints] = None
    """If specified, contains the VPC endpoints used to allow cluster communication from this VPC over
    [AWS PrivateLink].
    
    [AWS PrivateLink]: https://aws.amazon.com/privatelink/"""

    vpc_id: Optional[str] = None
    """The ID of the VPC associated with this network configuration. VPC IDs can be used in multiple
    networks."""

    vpc_status: Optional[VpcStatus] = None
    """The status of this network configuration object in terms of its use in a workspace: *
    `UNATTACHED`: Unattached. * `VALID`: Valid. * `BROKEN`: Broken. * `WARNED`: Warned."""

    warning_messages: Optional[List[NetworkWarning]] = None
    """Array of warning messages about the network configuration."""

    workspace_id: Optional[int] = None
    """Workspace ID associated with this network configuration."""

    def as_dict(self) -> dict:
        """Serializes the Network into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None: body['account_id'] = self.account_id
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.error_messages: body['error_messages'] = [v.as_dict() for v in self.error_messages]
        if self.gcp_network_info: body['gcp_network_info'] = self.gcp_network_info.as_dict()
        if self.network_id is not None: body['network_id'] = self.network_id
        if self.network_name is not None: body['network_name'] = self.network_name
        if self.security_group_ids: body['security_group_ids'] = [v for v in self.security_group_ids]
        if self.subnet_ids: body['subnet_ids'] = [v for v in self.subnet_ids]
        if self.vpc_endpoints: body['vpc_endpoints'] = self.vpc_endpoints.as_dict()
        if self.vpc_id is not None: body['vpc_id'] = self.vpc_id
        if self.vpc_status is not None: body['vpc_status'] = self.vpc_status.value
        if self.warning_messages: body['warning_messages'] = [v.as_dict() for v in self.warning_messages]
        if self.workspace_id is not None: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Network:
        """Deserializes the Network from a dictionary."""
        return cls(account_id=d.get('account_id', None),
                   creation_time=d.get('creation_time', None),
                   error_messages=_repeated_dict(d, 'error_messages', NetworkHealth),
                   gcp_network_info=_from_dict(d, 'gcp_network_info', GcpNetworkInfo),
                   network_id=d.get('network_id', None),
                   network_name=d.get('network_name', None),
                   security_group_ids=d.get('security_group_ids', None),
                   subnet_ids=d.get('subnet_ids', None),
                   vpc_endpoints=_from_dict(d, 'vpc_endpoints', NetworkVpcEndpoints),
                   vpc_id=d.get('vpc_id', None),
                   vpc_status=_enum(d, 'vpc_status', VpcStatus),
                   warning_messages=_repeated_dict(d, 'warning_messages', NetworkWarning),
                   workspace_id=d.get('workspace_id', None))


@dataclass
class NetworkHealth:
    error_message: Optional[str] = None
    """Details of the error."""

    error_type: Optional[ErrorType] = None
    """The AWS resource associated with this error: credentials, VPC, subnet, security group, or
    network ACL."""

    def as_dict(self) -> dict:
        """Serializes the NetworkHealth into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.error_message is not None: body['error_message'] = self.error_message
        if self.error_type is not None: body['error_type'] = self.error_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NetworkHealth:
        """Deserializes the NetworkHealth from a dictionary."""
        return cls(error_message=d.get('error_message', None), error_type=_enum(d, 'error_type', ErrorType))


@dataclass
class NetworkVpcEndpoints:
    """If specified, contains the VPC endpoints used to allow cluster communication from this VPC over
    [AWS PrivateLink].
    
    [AWS PrivateLink]: https://aws.amazon.com/privatelink/"""

    rest_api: List[str]
    """The VPC endpoint ID used by this network to access the Databricks REST API."""

    dataplane_relay: List[str]
    """The VPC endpoint ID used by this network to access the Databricks secure cluster connectivity
    relay."""

    def as_dict(self) -> dict:
        """Serializes the NetworkVpcEndpoints into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.dataplane_relay: body['dataplane_relay'] = [v for v in self.dataplane_relay]
        if self.rest_api: body['rest_api'] = [v for v in self.rest_api]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NetworkVpcEndpoints:
        """Deserializes the NetworkVpcEndpoints from a dictionary."""
        return cls(dataplane_relay=d.get('dataplane_relay', None), rest_api=d.get('rest_api', None))


@dataclass
class NetworkWarning:
    warning_message: Optional[str] = None
    """Details of the warning."""

    warning_type: Optional[WarningType] = None
    """The AWS resource associated with this warning: a subnet or a security group."""

    def as_dict(self) -> dict:
        """Serializes the NetworkWarning into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.warning_message is not None: body['warning_message'] = self.warning_message
        if self.warning_type is not None: body['warning_type'] = self.warning_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NetworkWarning:
        """Deserializes the NetworkWarning from a dictionary."""
        return cls(warning_message=d.get('warning_message', None),
                   warning_type=_enum(d, 'warning_type', WarningType))


class PricingTier(Enum):
    """The pricing tier of the workspace. For pricing tier information, see [AWS Pricing].
    
    [AWS Pricing]: https://databricks.com/product/aws-pricing"""

    COMMUNITY_EDITION = 'COMMUNITY_EDITION'
    DEDICATED = 'DEDICATED'
    ENTERPRISE = 'ENTERPRISE'
    PREMIUM = 'PREMIUM'
    STANDARD = 'STANDARD'
    UNKNOWN = 'UNKNOWN'


class PrivateAccessLevel(Enum):
    """The private access level controls which VPC endpoints can connect to the UI or API of any
    workspace that attaches this private access settings object. * `ACCOUNT` level access (the
    default) allows only VPC endpoints that are registered in your Databricks account connect to
    your workspace. * `ENDPOINT` level access allows only specified VPC endpoints connect to your
    workspace. For details, see `allowed_vpc_endpoint_ids`."""

    ACCOUNT = 'ACCOUNT'
    ENDPOINT = 'ENDPOINT'


@dataclass
class PrivateAccessSettings:
    account_id: Optional[str] = None
    """The Databricks account ID that hosts the credential."""

    allowed_vpc_endpoint_ids: Optional[List[str]] = None
    """An array of Databricks VPC endpoint IDs."""

    private_access_level: Optional[PrivateAccessLevel] = None
    """The private access level controls which VPC endpoints can connect to the UI or API of any
    workspace that attaches this private access settings object. * `ACCOUNT` level access (the
    default) allows only VPC endpoints that are registered in your Databricks account connect to
    your workspace. * `ENDPOINT` level access allows only specified VPC endpoints connect to your
    workspace. For details, see `allowed_vpc_endpoint_ids`."""

    private_access_settings_id: Optional[str] = None
    """Databricks private access settings ID."""

    private_access_settings_name: Optional[str] = None
    """The human-readable name of the private access settings object."""

    public_access_enabled: Optional[bool] = None
    """Determines if the workspace can be accessed over public internet. For fully private workspaces,
    you can optionally specify `false`, but only if you implement both the front-end and the
    back-end PrivateLink connections. Otherwise, specify `true`, which means that public access is
    enabled."""

    region: Optional[str] = None
    """The cloud region for workspaces attached to this private access settings object."""

    def as_dict(self) -> dict:
        """Serializes the PrivateAccessSettings into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None: body['account_id'] = self.account_id
        if self.allowed_vpc_endpoint_ids:
            body['allowed_vpc_endpoint_ids'] = [v for v in self.allowed_vpc_endpoint_ids]
        if self.private_access_level is not None:
            body['private_access_level'] = self.private_access_level.value
        if self.private_access_settings_id is not None:
            body['private_access_settings_id'] = self.private_access_settings_id
        if self.private_access_settings_name is not None:
            body['private_access_settings_name'] = self.private_access_settings_name
        if self.public_access_enabled is not None: body['public_access_enabled'] = self.public_access_enabled
        if self.region is not None: body['region'] = self.region
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PrivateAccessSettings:
        """Deserializes the PrivateAccessSettings from a dictionary."""
        return cls(account_id=d.get('account_id', None),
                   allowed_vpc_endpoint_ids=d.get('allowed_vpc_endpoint_ids', None),
                   private_access_level=_enum(d, 'private_access_level', PrivateAccessLevel),
                   private_access_settings_id=d.get('private_access_settings_id', None),
                   private_access_settings_name=d.get('private_access_settings_name', None),
                   public_access_enabled=d.get('public_access_enabled', None),
                   region=d.get('region', None))


@dataclass
class ReplaceResponse:

    def as_dict(self) -> dict:
        """Serializes the ReplaceResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ReplaceResponse:
        """Deserializes the ReplaceResponse from a dictionary."""
        return cls()


@dataclass
class RootBucketInfo:
    """Root S3 bucket information."""

    bucket_name: Optional[str] = None
    """The name of the S3 bucket."""

    def as_dict(self) -> dict:
        """Serializes the RootBucketInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.bucket_name is not None: body['bucket_name'] = self.bucket_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> RootBucketInfo:
        """Deserializes the RootBucketInfo from a dictionary."""
        return cls(bucket_name=d.get('bucket_name', None))


@dataclass
class StorageConfiguration:
    account_id: Optional[str] = None
    """The Databricks account ID that hosts the credential."""

    creation_time: Optional[int] = None
    """Time in epoch milliseconds when the storage configuration was created."""

    root_bucket_info: Optional[RootBucketInfo] = None
    """Root S3 bucket information."""

    storage_configuration_id: Optional[str] = None
    """Databricks storage configuration ID."""

    storage_configuration_name: Optional[str] = None
    """The human-readable name of the storage configuration."""

    def as_dict(self) -> dict:
        """Serializes the StorageConfiguration into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None: body['account_id'] = self.account_id
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.root_bucket_info: body['root_bucket_info'] = self.root_bucket_info.as_dict()
        if self.storage_configuration_id is not None:
            body['storage_configuration_id'] = self.storage_configuration_id
        if self.storage_configuration_name is not None:
            body['storage_configuration_name'] = self.storage_configuration_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> StorageConfiguration:
        """Deserializes the StorageConfiguration from a dictionary."""
        return cls(account_id=d.get('account_id', None),
                   creation_time=d.get('creation_time', None),
                   root_bucket_info=_from_dict(d, 'root_bucket_info', RootBucketInfo),
                   storage_configuration_id=d.get('storage_configuration_id', None),
                   storage_configuration_name=d.get('storage_configuration_name', None))


@dataclass
class StsRole:
    external_id: Optional[str] = None
    """The external ID that needs to be trusted by the cross-account role. This is always your
    Databricks account ID."""

    role_arn: Optional[str] = None
    """The Amazon Resource Name (ARN) of the cross account role."""

    def as_dict(self) -> dict:
        """Serializes the StsRole into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.external_id is not None: body['external_id'] = self.external_id
        if self.role_arn is not None: body['role_arn'] = self.role_arn
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> StsRole:
        """Deserializes the StsRole from a dictionary."""
        return cls(external_id=d.get('external_id', None), role_arn=d.get('role_arn', None))


@dataclass
class UpdateResponse:

    def as_dict(self) -> dict:
        """Serializes the UpdateResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateResponse:
        """Deserializes the UpdateResponse from a dictionary."""
        return cls()


@dataclass
class UpdateWorkspaceRequest:
    aws_region: Optional[str] = None
    """The AWS region of the workspace's data plane (for example, `us-west-2`). This parameter is
    available only for updating failed workspaces."""

    credentials_id: Optional[str] = None
    """ID of the workspace's credential configuration object. This parameter is available for updating
    both failed and running workspaces."""

    custom_tags: Optional[Dict[str, str]] = None
    """The custom tags key-value pairing that is attached to this workspace. The key-value pair is a
    string of utf-8 characters. The value can be an empty string, with maximum length of 255
    characters. The key can be of maximum length of 127 characters, and cannot be empty."""

    managed_services_customer_managed_key_id: Optional[str] = None
    """The ID of the workspace's managed services encryption key configuration object. This parameter
    is available only for updating failed workspaces."""

    network_connectivity_config_id: Optional[str] = None

    network_id: Optional[str] = None
    """The ID of the workspace's network configuration object. Used only if you already use a
    customer-managed VPC. For failed workspaces only, you can switch from a Databricks-managed VPC
    to a customer-managed VPC by updating the workspace to add a network configuration ID."""

    storage_configuration_id: Optional[str] = None
    """The ID of the workspace's storage configuration object. This parameter is available only for
    updating failed workspaces."""

    storage_customer_managed_key_id: Optional[str] = None
    """The ID of the key configuration object for workspace storage. This parameter is available for
    updating both failed and running workspaces."""

    workspace_id: Optional[int] = None
    """Workspace ID."""

    def as_dict(self) -> dict:
        """Serializes the UpdateWorkspaceRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_region is not None: body['aws_region'] = self.aws_region
        if self.credentials_id is not None: body['credentials_id'] = self.credentials_id
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.managed_services_customer_managed_key_id is not None:
            body['managed_services_customer_managed_key_id'] = self.managed_services_customer_managed_key_id
        if self.network_connectivity_config_id is not None:
            body['network_connectivity_config_id'] = self.network_connectivity_config_id
        if self.network_id is not None: body['network_id'] = self.network_id
        if self.storage_configuration_id is not None:
            body['storage_configuration_id'] = self.storage_configuration_id
        if self.storage_customer_managed_key_id is not None:
            body['storage_customer_managed_key_id'] = self.storage_customer_managed_key_id
        if self.workspace_id is not None: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateWorkspaceRequest:
        """Deserializes the UpdateWorkspaceRequest from a dictionary."""
        return cls(aws_region=d.get('aws_region', None),
                   credentials_id=d.get('credentials_id', None),
                   custom_tags=d.get('custom_tags', None),
                   managed_services_customer_managed_key_id=d.get('managed_services_customer_managed_key_id',
                                                                  None),
                   network_connectivity_config_id=d.get('network_connectivity_config_id', None),
                   network_id=d.get('network_id', None),
                   storage_configuration_id=d.get('storage_configuration_id', None),
                   storage_customer_managed_key_id=d.get('storage_customer_managed_key_id', None),
                   workspace_id=d.get('workspace_id', None))


@dataclass
class UpsertPrivateAccessSettingsRequest:
    private_access_settings_name: str
    """The human-readable name of the private access settings object."""

    region: str
    """The cloud region for workspaces associated with this private access settings object."""

    allowed_vpc_endpoint_ids: Optional[List[str]] = None
    """An array of Databricks VPC endpoint IDs. This is the Databricks ID that is returned when
    registering the VPC endpoint configuration in your Databricks account. This is not the ID of the
    VPC endpoint in AWS.
    
    Only used when `private_access_level` is set to `ENDPOINT`. This is an allow list of VPC
    endpoints that in your account that can connect to your workspace over AWS PrivateLink.
    
    If hybrid access to your workspace is enabled by setting `public_access_enabled` to `true`, this
    control only works for PrivateLink connections. To control how your workspace is accessed via
    public internet, see [IP access lists].
    
    [IP access lists]: https://docs.databricks.com/security/network/ip-access-list.html"""

    private_access_level: Optional[PrivateAccessLevel] = None
    """The private access level controls which VPC endpoints can connect to the UI or API of any
    workspace that attaches this private access settings object. * `ACCOUNT` level access (the
    default) allows only VPC endpoints that are registered in your Databricks account connect to
    your workspace. * `ENDPOINT` level access allows only specified VPC endpoints connect to your
    workspace. For details, see `allowed_vpc_endpoint_ids`."""

    private_access_settings_id: Optional[str] = None
    """Databricks Account API private access settings ID."""

    public_access_enabled: Optional[bool] = None
    """Determines if the workspace can be accessed over public internet. For fully private workspaces,
    you can optionally specify `false`, but only if you implement both the front-end and the
    back-end PrivateLink connections. Otherwise, specify `true`, which means that public access is
    enabled."""

    def as_dict(self) -> dict:
        """Serializes the UpsertPrivateAccessSettingsRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.allowed_vpc_endpoint_ids:
            body['allowed_vpc_endpoint_ids'] = [v for v in self.allowed_vpc_endpoint_ids]
        if self.private_access_level is not None:
            body['private_access_level'] = self.private_access_level.value
        if self.private_access_settings_id is not None:
            body['private_access_settings_id'] = self.private_access_settings_id
        if self.private_access_settings_name is not None:
            body['private_access_settings_name'] = self.private_access_settings_name
        if self.public_access_enabled is not None: body['public_access_enabled'] = self.public_access_enabled
        if self.region is not None: body['region'] = self.region
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpsertPrivateAccessSettingsRequest:
        """Deserializes the UpsertPrivateAccessSettingsRequest from a dictionary."""
        return cls(allowed_vpc_endpoint_ids=d.get('allowed_vpc_endpoint_ids', None),
                   private_access_level=_enum(d, 'private_access_level', PrivateAccessLevel),
                   private_access_settings_id=d.get('private_access_settings_id', None),
                   private_access_settings_name=d.get('private_access_settings_name', None),
                   public_access_enabled=d.get('public_access_enabled', None),
                   region=d.get('region', None))


@dataclass
class VpcEndpoint:
    account_id: Optional[str] = None
    """The Databricks account ID that hosts the VPC endpoint configuration."""

    aws_account_id: Optional[str] = None
    """The AWS Account in which the VPC endpoint object exists."""

    aws_endpoint_service_id: Optional[str] = None
    """The ID of the Databricks [endpoint service] that this VPC endpoint is connected to. For a list
    of endpoint service IDs for each supported AWS region, see the [Databricks PrivateLink
    documentation].
    
    [Databricks PrivateLink documentation]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
    [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service.html"""

    aws_vpc_endpoint_id: Optional[str] = None
    """The ID of the VPC endpoint object in AWS."""

    gcp_vpc_endpoint_info: Optional[GcpVpcEndpointInfo] = None
    """The Google Cloud specific information for this Private Service Connect endpoint."""

    region: Optional[str] = None
    """The AWS region in which this VPC endpoint object exists."""

    state: Optional[str] = None
    """The current state (such as `available` or `rejected`) of the VPC endpoint. Derived from AWS. For
    the full set of values, see [AWS DescribeVpcEndpoint documentation].
    
    [AWS DescribeVpcEndpoint documentation]: https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html"""

    use_case: Optional[EndpointUseCase] = None
    """This enumeration represents the type of Databricks VPC [endpoint service] that was used when
    creating this VPC endpoint.
    
    [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service.html"""

    vpc_endpoint_id: Optional[str] = None
    """Databricks VPC endpoint ID. This is the Databricks-specific name of the VPC endpoint. Do not
    confuse this with the `aws_vpc_endpoint_id`, which is the ID within AWS of the VPC endpoint."""

    vpc_endpoint_name: Optional[str] = None
    """The human-readable name of the storage configuration."""

    def as_dict(self) -> dict:
        """Serializes the VpcEndpoint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None: body['account_id'] = self.account_id
        if self.aws_account_id is not None: body['aws_account_id'] = self.aws_account_id
        if self.aws_endpoint_service_id is not None:
            body['aws_endpoint_service_id'] = self.aws_endpoint_service_id
        if self.aws_vpc_endpoint_id is not None: body['aws_vpc_endpoint_id'] = self.aws_vpc_endpoint_id
        if self.gcp_vpc_endpoint_info: body['gcp_vpc_endpoint_info'] = self.gcp_vpc_endpoint_info.as_dict()
        if self.region is not None: body['region'] = self.region
        if self.state is not None: body['state'] = self.state
        if self.use_case is not None: body['use_case'] = self.use_case.value
        if self.vpc_endpoint_id is not None: body['vpc_endpoint_id'] = self.vpc_endpoint_id
        if self.vpc_endpoint_name is not None: body['vpc_endpoint_name'] = self.vpc_endpoint_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> VpcEndpoint:
        """Deserializes the VpcEndpoint from a dictionary."""
        return cls(account_id=d.get('account_id', None),
                   aws_account_id=d.get('aws_account_id', None),
                   aws_endpoint_service_id=d.get('aws_endpoint_service_id', None),
                   aws_vpc_endpoint_id=d.get('aws_vpc_endpoint_id', None),
                   gcp_vpc_endpoint_info=_from_dict(d, 'gcp_vpc_endpoint_info', GcpVpcEndpointInfo),
                   region=d.get('region', None),
                   state=d.get('state', None),
                   use_case=_enum(d, 'use_case', EndpointUseCase),
                   vpc_endpoint_id=d.get('vpc_endpoint_id', None),
                   vpc_endpoint_name=d.get('vpc_endpoint_name', None))


class VpcStatus(Enum):
    """The status of this network configuration object in terms of its use in a workspace: *
    `UNATTACHED`: Unattached. * `VALID`: Valid. * `BROKEN`: Broken. * `WARNED`: Warned."""

    BROKEN = 'BROKEN'
    UNATTACHED = 'UNATTACHED'
    VALID = 'VALID'
    WARNED = 'WARNED'


class WarningType(Enum):
    """The AWS resource associated with this warning: a subnet or a security group."""

    SECURITY_GROUP = 'securityGroup'
    SUBNET = 'subnet'


@dataclass
class Workspace:
    account_id: Optional[str] = None
    """Databricks account ID."""

    aws_region: Optional[str] = None
    """The AWS region of the workspace data plane (for example, `us-west-2`)."""

    azure_workspace_info: Optional[AzureWorkspaceInfo] = None

    cloud: Optional[str] = None
    """The cloud name. This field always has the value `gcp`."""

    cloud_resource_container: Optional[CloudResourceContainer] = None
    """The general workspace configurations that are specific to cloud providers."""

    creation_time: Optional[int] = None
    """Time in epoch milliseconds when the workspace was created."""

    credentials_id: Optional[str] = None
    """ID of the workspace's credential configuration object."""

    custom_tags: Optional[Dict[str, str]] = None
    """The custom tags key-value pairing that is attached to this workspace. The key-value pair is a
    string of utf-8 characters. The value can be an empty string, with maximum length of 255
    characters. The key can be of maximum length of 127 characters, and cannot be empty."""

    deployment_name: Optional[str] = None
    """The deployment name defines part of the subdomain for the workspace. The workspace URL for web
    application and REST APIs is `<deployment-name>.cloud.databricks.com`.
    
    This value must be unique across all non-deleted deployments across all AWS regions."""

    gcp_managed_network_config: Optional[GcpManagedNetworkConfig] = None
    """The network settings for the workspace. The configurations are only for Databricks-managed VPCs.
    It is ignored if you specify a customer-managed VPC in the `network_id` field.", All the IP
    range configurations must be mutually exclusive. An attempt to create a workspace fails if
    Databricks detects an IP range overlap.
    
    Specify custom IP ranges in CIDR format. The IP ranges for these fields must not overlap, and
    all IP addresses must be entirely within the following ranges: `10.0.0.0/8`, `100.64.0.0/10`,
    `172.16.0.0/12`, `192.168.0.0/16`, and `240.0.0.0/4`.
    
    The sizes of these IP ranges affect the maximum number of nodes for the workspace.
    
    **Important**: Confirm the IP ranges used by your Databricks workspace before creating the
    workspace. You cannot change them after your workspace is deployed. If the IP address ranges for
    your Databricks are too small, IP exhaustion can occur, causing your Databricks jobs to fail. To
    determine the address range sizes that you need, Databricks provides a calculator as a Microsoft
    Excel spreadsheet. See [calculate subnet sizes for a new workspace].
    
    [calculate subnet sizes for a new workspace]: https://docs.gcp.databricks.com/administration-guide/cloud-configurations/gcp/network-sizing.html"""

    gke_config: Optional[GkeConfig] = None
    """The configurations for the GKE cluster of a Databricks workspace."""

    location: Optional[str] = None
    """The Google Cloud region of the workspace data plane in your Google account (for example,
    `us-east4`)."""

    managed_services_customer_managed_key_id: Optional[str] = None
    """ID of the key configuration for encrypting managed services."""

    network_id: Optional[str] = None
    """The network configuration ID that is attached to the workspace. This field is available only if
    the network is a customer-managed network."""

    pricing_tier: Optional[PricingTier] = None
    """The pricing tier of the workspace. For pricing tier information, see [AWS Pricing].
    
    [AWS Pricing]: https://databricks.com/product/aws-pricing"""

    private_access_settings_id: Optional[str] = None
    """ID of the workspace's private access settings object. Only used for PrivateLink. You must
    specify this ID if you are using [AWS PrivateLink] for either front-end (user-to-workspace
    connection), back-end (data plane to control plane connection), or both connection types.
    
    Before configuring PrivateLink, read the [Databricks article about PrivateLink].",
    
    [AWS PrivateLink]: https://aws.amazon.com/privatelink/
    [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""

    storage_configuration_id: Optional[str] = None
    """ID of the workspace's storage configuration object."""

    storage_customer_managed_key_id: Optional[str] = None
    """ID of the key configuration for encrypting workspace storage."""

    workspace_id: Optional[int] = None
    """A unique integer ID for the workspace"""

    workspace_name: Optional[str] = None
    """The human-readable name of the workspace."""

    workspace_status: Optional[WorkspaceStatus] = None
    """The status of the workspace. For workspace creation, usually it is set to `PROVISIONING`
    initially. Continue to check the status until the status is `RUNNING`."""

    workspace_status_message: Optional[str] = None
    """Message describing the current workspace status."""

    def as_dict(self) -> dict:
        """Serializes the Workspace into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None: body['account_id'] = self.account_id
        if self.aws_region is not None: body['aws_region'] = self.aws_region
        if self.azure_workspace_info: body['azure_workspace_info'] = self.azure_workspace_info.as_dict()
        if self.cloud is not None: body['cloud'] = self.cloud
        if self.cloud_resource_container:
            body['cloud_resource_container'] = self.cloud_resource_container.as_dict()
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.credentials_id is not None: body['credentials_id'] = self.credentials_id
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.deployment_name is not None: body['deployment_name'] = self.deployment_name
        if self.gcp_managed_network_config:
            body['gcp_managed_network_config'] = self.gcp_managed_network_config.as_dict()
        if self.gke_config: body['gke_config'] = self.gke_config.as_dict()
        if self.location is not None: body['location'] = self.location
        if self.managed_services_customer_managed_key_id is not None:
            body['managed_services_customer_managed_key_id'] = self.managed_services_customer_managed_key_id
        if self.network_id is not None: body['network_id'] = self.network_id
        if self.pricing_tier is not None: body['pricing_tier'] = self.pricing_tier.value
        if self.private_access_settings_id is not None:
            body['private_access_settings_id'] = self.private_access_settings_id
        if self.storage_configuration_id is not None:
            body['storage_configuration_id'] = self.storage_configuration_id
        if self.storage_customer_managed_key_id is not None:
            body['storage_customer_managed_key_id'] = self.storage_customer_managed_key_id
        if self.workspace_id is not None: body['workspace_id'] = self.workspace_id
        if self.workspace_name is not None: body['workspace_name'] = self.workspace_name
        if self.workspace_status is not None: body['workspace_status'] = self.workspace_status.value
        if self.workspace_status_message is not None:
            body['workspace_status_message'] = self.workspace_status_message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Workspace:
        """Deserializes the Workspace from a dictionary."""
        return cls(account_id=d.get('account_id', None),
                   aws_region=d.get('aws_region', None),
                   azure_workspace_info=_from_dict(d, 'azure_workspace_info', AzureWorkspaceInfo),
                   cloud=d.get('cloud', None),
                   cloud_resource_container=_from_dict(d, 'cloud_resource_container', CloudResourceContainer),
                   creation_time=d.get('creation_time', None),
                   credentials_id=d.get('credentials_id', None),
                   custom_tags=d.get('custom_tags', None),
                   deployment_name=d.get('deployment_name', None),
                   gcp_managed_network_config=_from_dict(d, 'gcp_managed_network_config',
                                                         GcpManagedNetworkConfig),
                   gke_config=_from_dict(d, 'gke_config', GkeConfig),
                   location=d.get('location', None),
                   managed_services_customer_managed_key_id=d.get('managed_services_customer_managed_key_id',
                                                                  None),
                   network_id=d.get('network_id', None),
                   pricing_tier=_enum(d, 'pricing_tier', PricingTier),
                   private_access_settings_id=d.get('private_access_settings_id', None),
                   storage_configuration_id=d.get('storage_configuration_id', None),
                   storage_customer_managed_key_id=d.get('storage_customer_managed_key_id', None),
                   workspace_id=d.get('workspace_id', None),
                   workspace_name=d.get('workspace_name', None),
                   workspace_status=_enum(d, 'workspace_status', WorkspaceStatus),
                   workspace_status_message=d.get('workspace_status_message', None))


class WorkspaceStatus(Enum):
    """The status of the workspace. For workspace creation, usually it is set to `PROVISIONING`
    initially. Continue to check the status until the status is `RUNNING`."""

    BANNED = 'BANNED'
    CANCELLING = 'CANCELLING'
    FAILED = 'FAILED'
    NOT_PROVISIONED = 'NOT_PROVISIONED'
    PROVISIONING = 'PROVISIONING'
    RUNNING = 'RUNNING'


class CredentialsAPI:
    """These APIs manage credential configurations for this workspace. Databricks needs access to a cross-account
    service IAM role in your AWS account so that Databricks can deploy clusters in the appropriate VPC for the
    new workspace. A credential configuration encapsulates this role information, and its ID is used when
    creating a new workspace."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, credentials_name: str, aws_credentials: CreateCredentialAwsCredentials) -> Credential:
        """Create credential configuration.
        
        Creates a Databricks credential configuration that represents cloud cross-account credentials for a
        specified account. Databricks uses this to set up network infrastructure properly to host Databricks
        clusters. For your AWS IAM role, you need to trust the External ID (the Databricks Account API account
        ID) in the returned credential object, and configure the required access policy.
        
        Save the response's `credentials_id` field, which is the ID for your new credential configuration
        object.
        
        For information about how to create a new workspace with this API, see [Create a new workspace using
        the Account API]
        
        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html
        
        :param credentials_name: str
          The human-readable name of the credential configuration object.
        :param aws_credentials: :class:`CreateCredentialAwsCredentials`
        
        :returns: :class:`Credential`
        """
        body = {}
        if aws_credentials is not None: body['aws_credentials'] = aws_credentials.as_dict()
        if credentials_name is not None: body['credentials_name'] = credentials_name
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/credentials',
                           body=body,
                           headers=headers)
        return Credential.from_dict(res)

    def delete(self, credentials_id: str):
        """Delete credential configuration.
        
        Deletes a Databricks credential configuration object for an account, both specified by ID. You cannot
        delete a credential that is associated with any workspace.
        
        :param credentials_id: str
          Databricks Account API credential configuration ID
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/credentials/{credentials_id}',
                     headers=headers)

    def get(self, credentials_id: str) -> Credential:
        """Get credential configuration.
        
        Gets a Databricks credential configuration object for an account, both specified by ID.
        
        :param credentials_id: str
          Databricks Account API credential configuration ID
        
        :returns: :class:`Credential`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/credentials/{credentials_id}',
                           headers=headers)
        return Credential.from_dict(res)

    def list(self) -> Iterator[Credential]:
        """Get all credential configurations.
        
        Gets all Databricks credential configurations associated with an account specified by ID.
        
        :returns: Iterator over :class:`Credential`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/credentials', headers=headers)
        return [Credential.from_dict(v) for v in res]


class EncryptionKeysAPI:
    """These APIs manage encryption key configurations for this workspace (optional). A key configuration
    encapsulates the AWS KMS key information and some information about how the key configuration can be used.
    There are two possible uses for key configurations:
    
    * Managed services: A key configuration can be used to encrypt a workspace's notebook and secret data in
    the control plane, as well as Databricks SQL queries and query history. * Storage: A key configuration can
    be used to encrypt a workspace's DBFS and EBS data in the data plane.
    
    In both of these cases, the key configuration's ID is used when creating a new workspace. This Preview
    feature is available if your account is on the E2 version of the platform. Updating a running workspace
    with workspace storage encryption requires that the workspace is on the E2 version of the platform. If you
    have an older workspace, it might not be on the E2 version of the platform. If you are not sure, contact
    your Databricks representative."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               use_cases: List[KeyUseCase],
               *,
               aws_key_info: Optional[CreateAwsKeyInfo] = None,
               gcp_key_info: Optional[CreateGcpKeyInfo] = None) -> CustomerManagedKey:
        """Create encryption key configuration.
        
        Creates a customer-managed key configuration object for an account, specified by ID. This operation
        uploads a reference to a customer-managed key to Databricks. If the key is assigned as a workspace's
        customer-managed key for managed services, Databricks uses the key to encrypt the workspaces notebooks
        and secrets in the control plane, in addition to Databricks SQL queries and query history. If it is
        specified as a workspace's customer-managed key for workspace storage, the key encrypts the
        workspace's root S3 bucket (which contains the workspace's root DBFS and system data) and, optionally,
        cluster EBS volume data.
        
        **Important**: Customer-managed keys are supported only for some deployment types, subscription types,
        and AWS regions that currently support creation of Databricks workspaces.
        
        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account.
        
        :param use_cases: List[:class:`KeyUseCase`]
          The cases that the key can be used for.
        :param aws_key_info: :class:`CreateAwsKeyInfo` (optional)
        :param gcp_key_info: :class:`CreateGcpKeyInfo` (optional)
        
        :returns: :class:`CustomerManagedKey`
        """
        body = {}
        if aws_key_info is not None: body['aws_key_info'] = aws_key_info.as_dict()
        if gcp_key_info is not None: body['gcp_key_info'] = gcp_key_info.as_dict()
        if use_cases is not None: body['use_cases'] = [v.value for v in use_cases]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/customer-managed-keys',
                           body=body,
                           headers=headers)
        return CustomerManagedKey.from_dict(res)

    def delete(self, customer_managed_key_id: str):
        """Delete encryption key configuration.
        
        Deletes a customer-managed key configuration object for an account. You cannot delete a configuration
        that is associated with a running workspace.
        
        :param customer_managed_key_id: str
          Databricks encryption key configuration ID.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/customer-managed-keys/{customer_managed_key_id}',
            headers=headers)

    def get(self, customer_managed_key_id: str) -> CustomerManagedKey:
        """Get encryption key configuration.
        
        Gets a customer-managed key configuration object for an account, specified by ID. This operation
        uploads a reference to a customer-managed key to Databricks. If assigned as a workspace's
        customer-managed key for managed services, Databricks uses the key to encrypt the workspaces notebooks
        and secrets in the control plane, in addition to Databricks SQL queries and query history. If it is
        specified as a workspace's customer-managed key for storage, the key encrypts the workspace's root S3
        bucket (which contains the workspace's root DBFS and system data) and, optionally, cluster EBS volume
        data.
        
        **Important**: Customer-managed keys are supported only for some deployment types, subscription types,
        and AWS regions.
        
        This operation is available only if your account is on the E2 version of the platform.",
        
        :param customer_managed_key_id: str
          Databricks encryption key configuration ID.
        
        :returns: :class:`CustomerManagedKey`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/customer-managed-keys/{customer_managed_key_id}',
            headers=headers)
        return CustomerManagedKey.from_dict(res)

    def list(self) -> Iterator[CustomerManagedKey]:
        """Get all encryption key configurations.
        
        Gets all customer-managed key configuration objects for an account. If the key is specified as a
        workspace's managed services customer-managed key, Databricks uses the key to encrypt the workspace's
        notebooks and secrets in the control plane, in addition to Databricks SQL queries and query history.
        If the key is specified as a workspace's storage customer-managed key, the key is used to encrypt the
        workspace's root S3 bucket and optionally can encrypt cluster EBS volumes data in the data plane.
        
        **Important**: Customer-managed keys are supported only for some deployment types, subscription types,
        and AWS regions.
        
        This operation is available only if your account is on the E2 version of the platform.
        
        :returns: Iterator over :class:`CustomerManagedKey`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/customer-managed-keys',
                           headers=headers)
        return [CustomerManagedKey.from_dict(v) for v in res]


class NetworksAPI:
    """These APIs manage network configurations for customer-managed VPCs (optional). Its ID is used when
    creating a new workspace if you use customer-managed VPCs."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               network_name: str,
               *,
               gcp_network_info: Optional[GcpNetworkInfo] = None,
               security_group_ids: Optional[List[str]] = None,
               subnet_ids: Optional[List[str]] = None,
               vpc_endpoints: Optional[NetworkVpcEndpoints] = None,
               vpc_id: Optional[str] = None) -> Network:
        """Create network configuration.
        
        Creates a Databricks network configuration that represents an VPC and its resources. The VPC will be
        used for new Databricks clusters. This requires a pre-existing VPC and subnets.
        
        :param network_name: str
          The human-readable name of the network configuration.
        :param gcp_network_info: :class:`GcpNetworkInfo` (optional)
          The Google Cloud specific information for this network (for example, the VPC ID, subnet ID, and
          secondary IP ranges).
        :param security_group_ids: List[str] (optional)
          IDs of one to five security groups associated with this network. Security group IDs **cannot** be
          used in multiple network configurations.
        :param subnet_ids: List[str] (optional)
          IDs of at least two subnets associated with this network. Subnet IDs **cannot** be used in multiple
          network configurations.
        :param vpc_endpoints: :class:`NetworkVpcEndpoints` (optional)
          If specified, contains the VPC endpoints used to allow cluster communication from this VPC over [AWS
          PrivateLink].
          
          [AWS PrivateLink]: https://aws.amazon.com/privatelink/
        :param vpc_id: str (optional)
          The ID of the VPC associated with this network. VPC IDs can be used in multiple network
          configurations.
        
        :returns: :class:`Network`
        """
        body = {}
        if gcp_network_info is not None: body['gcp_network_info'] = gcp_network_info.as_dict()
        if network_name is not None: body['network_name'] = network_name
        if security_group_ids is not None: body['security_group_ids'] = [v for v in security_group_ids]
        if subnet_ids is not None: body['subnet_ids'] = [v for v in subnet_ids]
        if vpc_endpoints is not None: body['vpc_endpoints'] = vpc_endpoints.as_dict()
        if vpc_id is not None: body['vpc_id'] = vpc_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/networks',
                           body=body,
                           headers=headers)
        return Network.from_dict(res)

    def delete(self, network_id: str):
        """Delete a network configuration.
        
        Deletes a Databricks network configuration, which represents a cloud VPC and its resources. You cannot
        delete a network that is associated with a workspace.
        
        This operation is available only if your account is on the E2 version of the platform.
        
        :param network_id: str
          Databricks Account API network configuration ID.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/networks/{network_id}',
                     headers=headers)

    def get(self, network_id: str) -> Network:
        """Get a network configuration.
        
        Gets a Databricks network configuration, which represents a cloud VPC and its resources.
        
        :param network_id: str
          Databricks Account API network configuration ID.
        
        :returns: :class:`Network`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/networks/{network_id}',
                           headers=headers)
        return Network.from_dict(res)

    def list(self) -> Iterator[Network]:
        """Get all network configurations.
        
        Gets a list of all Databricks network configurations for an account, specified by ID.
        
        This operation is available only if your account is on the E2 version of the platform.
        
        :returns: Iterator over :class:`Network`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/networks', headers=headers)
        return [Network.from_dict(v) for v in res]


class PrivateAccessAPI:
    """These APIs manage private access settings for this account."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               private_access_settings_name: str,
               region: str,
               *,
               allowed_vpc_endpoint_ids: Optional[List[str]] = None,
               private_access_level: Optional[PrivateAccessLevel] = None,
               public_access_enabled: Optional[bool] = None) -> PrivateAccessSettings:
        """Create private access settings.
        
        Creates a private access settings object, which specifies how your workspace is accessed over [AWS
        PrivateLink]. To use AWS PrivateLink, a workspace must have a private access settings object
        referenced by ID in the workspace's `private_access_settings_id` property.
        
        You can share one private access settings with multiple workspaces in a single account. However,
        private access settings are specific to AWS regions, so only workspaces in the same AWS region can use
        a given private access settings object.
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        
        :param private_access_settings_name: str
          The human-readable name of the private access settings object.
        :param region: str
          The cloud region for workspaces associated with this private access settings object.
        :param allowed_vpc_endpoint_ids: List[str] (optional)
          An array of Databricks VPC endpoint IDs. This is the Databricks ID that is returned when registering
          the VPC endpoint configuration in your Databricks account. This is not the ID of the VPC endpoint in
          AWS.
          
          Only used when `private_access_level` is set to `ENDPOINT`. This is an allow list of VPC endpoints
          that in your account that can connect to your workspace over AWS PrivateLink.
          
          If hybrid access to your workspace is enabled by setting `public_access_enabled` to `true`, this
          control only works for PrivateLink connections. To control how your workspace is accessed via public
          internet, see [IP access lists].
          
          [IP access lists]: https://docs.databricks.com/security/network/ip-access-list.html
        :param private_access_level: :class:`PrivateAccessLevel` (optional)
          The private access level controls which VPC endpoints can connect to the UI or API of any workspace
          that attaches this private access settings object. * `ACCOUNT` level access (the default) allows
          only VPC endpoints that are registered in your Databricks account connect to your workspace. *
          `ENDPOINT` level access allows only specified VPC endpoints connect to your workspace. For details,
          see `allowed_vpc_endpoint_ids`.
        :param public_access_enabled: bool (optional)
          Determines if the workspace can be accessed over public internet. For fully private workspaces, you
          can optionally specify `false`, but only if you implement both the front-end and the back-end
          PrivateLink connections. Otherwise, specify `true`, which means that public access is enabled.
        
        :returns: :class:`PrivateAccessSettings`
        """
        body = {}
        if allowed_vpc_endpoint_ids is not None:
            body['allowed_vpc_endpoint_ids'] = [v for v in allowed_vpc_endpoint_ids]
        if private_access_level is not None: body['private_access_level'] = private_access_level.value
        if private_access_settings_name is not None:
            body['private_access_settings_name'] = private_access_settings_name
        if public_access_enabled is not None: body['public_access_enabled'] = public_access_enabled
        if region is not None: body['region'] = region
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/private-access-settings',
                           body=body,
                           headers=headers)
        return PrivateAccessSettings.from_dict(res)

    def delete(self, private_access_settings_id: str):
        """Delete a private access settings object.
        
        Deletes a private access settings object, which determines how your workspace is accessed over [AWS
        PrivateLink].
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].",
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        
        :param private_access_settings_id: str
          Databricks Account API private access settings ID.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/private-access-settings/{private_access_settings_id}',
            headers=headers)

    def get(self, private_access_settings_id: str) -> PrivateAccessSettings:
        """Get a private access settings object.
        
        Gets a private access settings object, which specifies how your workspace is accessed over [AWS
        PrivateLink].
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].",
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        
        :param private_access_settings_id: str
          Databricks Account API private access settings ID.
        
        :returns: :class:`PrivateAccessSettings`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/private-access-settings/{private_access_settings_id}',
            headers=headers)
        return PrivateAccessSettings.from_dict(res)

    def list(self) -> Iterator[PrivateAccessSettings]:
        """Get all private access settings objects.
        
        Gets a list of all private access settings objects for an account, specified by ID.
        
        :returns: Iterator over :class:`PrivateAccessSettings`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/private-access-settings',
                           headers=headers)
        return [PrivateAccessSettings.from_dict(v) for v in res]

    def replace(self,
                private_access_settings_id: str,
                private_access_settings_name: str,
                region: str,
                *,
                allowed_vpc_endpoint_ids: Optional[List[str]] = None,
                private_access_level: Optional[PrivateAccessLevel] = None,
                public_access_enabled: Optional[bool] = None):
        """Replace private access settings.
        
        Updates an existing private access settings object, which specifies how your workspace is accessed
        over [AWS PrivateLink]. To use AWS PrivateLink, a workspace must have a private access settings object
        referenced by ID in the workspace's `private_access_settings_id` property.
        
        This operation completely overwrites your existing private access settings object attached to your
        workspaces. All workspaces attached to the private access settings are affected by any change. If
        `public_access_enabled`, `private_access_level`, or `allowed_vpc_endpoint_ids` are updated, effects of
        these changes might take several minutes to propagate to the workspace API.
        
        You can share one private access settings object with multiple workspaces in a single account.
        However, private access settings are specific to AWS regions, so only workspaces in the same AWS
        region can use a given private access settings object.
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        
        :param private_access_settings_id: str
          Databricks Account API private access settings ID.
        :param private_access_settings_name: str
          The human-readable name of the private access settings object.
        :param region: str
          The cloud region for workspaces associated with this private access settings object.
        :param allowed_vpc_endpoint_ids: List[str] (optional)
          An array of Databricks VPC endpoint IDs. This is the Databricks ID that is returned when registering
          the VPC endpoint configuration in your Databricks account. This is not the ID of the VPC endpoint in
          AWS.
          
          Only used when `private_access_level` is set to `ENDPOINT`. This is an allow list of VPC endpoints
          that in your account that can connect to your workspace over AWS PrivateLink.
          
          If hybrid access to your workspace is enabled by setting `public_access_enabled` to `true`, this
          control only works for PrivateLink connections. To control how your workspace is accessed via public
          internet, see [IP access lists].
          
          [IP access lists]: https://docs.databricks.com/security/network/ip-access-list.html
        :param private_access_level: :class:`PrivateAccessLevel` (optional)
          The private access level controls which VPC endpoints can connect to the UI or API of any workspace
          that attaches this private access settings object. * `ACCOUNT` level access (the default) allows
          only VPC endpoints that are registered in your Databricks account connect to your workspace. *
          `ENDPOINT` level access allows only specified VPC endpoints connect to your workspace. For details,
          see `allowed_vpc_endpoint_ids`.
        :param public_access_enabled: bool (optional)
          Determines if the workspace can be accessed over public internet. For fully private workspaces, you
          can optionally specify `false`, but only if you implement both the front-end and the back-end
          PrivateLink connections. Otherwise, specify `true`, which means that public access is enabled.
        
        
        """
        body = {}
        if allowed_vpc_endpoint_ids is not None:
            body['allowed_vpc_endpoint_ids'] = [v for v in allowed_vpc_endpoint_ids]
        if private_access_level is not None: body['private_access_level'] = private_access_level.value
        if private_access_settings_name is not None:
            body['private_access_settings_name'] = private_access_settings_name
        if public_access_enabled is not None: body['public_access_enabled'] = public_access_enabled
        if region is not None: body['region'] = region
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        self._api.do(
            'PUT',
            f'/api/2.0/accounts/{self._api.account_id}/private-access-settings/{private_access_settings_id}',
            body=body,
            headers=headers)


class StorageAPI:
    """These APIs manage storage configurations for this workspace. A root storage S3 bucket in your account is
    required to store objects like cluster logs, notebook revisions, and job results. You can also use the
    root storage S3 bucket for storage of non-production DBFS data. A storage configuration encapsulates this
    bucket information, and its ID is used when creating a new workspace."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, storage_configuration_name: str,
               root_bucket_info: RootBucketInfo) -> StorageConfiguration:
        """Create new storage configuration.
        
        Creates new storage configuration for an account, specified by ID. Uploads a storage configuration
        object that represents the root AWS S3 bucket in your account. Databricks stores related workspace
        assets including DBFS, cluster logs, and job results. For the AWS S3 bucket, you need to configure the
        required bucket policy.
        
        For information about how to create a new workspace with this API, see [Create a new workspace using
        the Account API]
        
        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html
        
        :param storage_configuration_name: str
          The human-readable name of the storage configuration.
        :param root_bucket_info: :class:`RootBucketInfo`
          Root S3 bucket information.
        
        :returns: :class:`StorageConfiguration`
        """
        body = {}
        if root_bucket_info is not None: body['root_bucket_info'] = root_bucket_info.as_dict()
        if storage_configuration_name is not None:
            body['storage_configuration_name'] = storage_configuration_name
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/storage-configurations',
                           body=body,
                           headers=headers)
        return StorageConfiguration.from_dict(res)

    def delete(self, storage_configuration_id: str):
        """Delete storage configuration.
        
        Deletes a Databricks storage configuration. You cannot delete a storage configuration that is
        associated with any workspace.
        
        :param storage_configuration_id: str
          Databricks Account API storage configuration ID.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/storage-configurations/{storage_configuration_id}',
            headers=headers)

    def get(self, storage_configuration_id: str) -> StorageConfiguration:
        """Get storage configuration.
        
        Gets a Databricks storage configuration for an account, both specified by ID.
        
        :param storage_configuration_id: str
          Databricks Account API storage configuration ID.
        
        :returns: :class:`StorageConfiguration`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/storage-configurations/{storage_configuration_id}',
            headers=headers)
        return StorageConfiguration.from_dict(res)

    def list(self) -> Iterator[StorageConfiguration]:
        """Get all storage configurations.
        
        Gets a list of all Databricks storage configurations for your account, specified by ID.
        
        :returns: Iterator over :class:`StorageConfiguration`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/storage-configurations',
                           headers=headers)
        return [StorageConfiguration.from_dict(v) for v in res]


class VpcEndpointsAPI:
    """These APIs manage VPC endpoint configurations for this account."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               vpc_endpoint_name: str,
               *,
               aws_vpc_endpoint_id: Optional[str] = None,
               gcp_vpc_endpoint_info: Optional[GcpVpcEndpointInfo] = None,
               region: Optional[str] = None) -> VpcEndpoint:
        """Create VPC endpoint configuration.
        
        Creates a VPC endpoint configuration, which represents a [VPC endpoint] object in AWS used to
        communicate privately with Databricks over [AWS PrivateLink].
        
        After you create the VPC endpoint configuration, the Databricks [endpoint service] automatically
        accepts the VPC endpoint.
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        [VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html
        [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html
        
        :param vpc_endpoint_name: str
          The human-readable name of the storage configuration.
        :param aws_vpc_endpoint_id: str (optional)
          The ID of the VPC endpoint object in AWS.
        :param gcp_vpc_endpoint_info: :class:`GcpVpcEndpointInfo` (optional)
          The Google Cloud specific information for this Private Service Connect endpoint.
        :param region: str (optional)
          The AWS region in which this VPC endpoint object exists.
        
        :returns: :class:`VpcEndpoint`
        """
        body = {}
        if aws_vpc_endpoint_id is not None: body['aws_vpc_endpoint_id'] = aws_vpc_endpoint_id
        if gcp_vpc_endpoint_info is not None: body['gcp_vpc_endpoint_info'] = gcp_vpc_endpoint_info.as_dict()
        if region is not None: body['region'] = region
        if vpc_endpoint_name is not None: body['vpc_endpoint_name'] = vpc_endpoint_name
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/vpc-endpoints',
                           body=body,
                           headers=headers)
        return VpcEndpoint.from_dict(res)

    def delete(self, vpc_endpoint_id: str):
        """Delete VPC endpoint configuration.
        
        Deletes a VPC endpoint configuration, which represents an [AWS VPC endpoint] that can communicate
        privately with Databricks over [AWS PrivateLink].
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [AWS VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        
        :param vpc_endpoint_id: str
          Databricks VPC endpoint ID.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/vpc-endpoints/{vpc_endpoint_id}',
                     headers=headers)

    def get(self, vpc_endpoint_id: str) -> VpcEndpoint:
        """Get a VPC endpoint configuration.
        
        Gets a VPC endpoint configuration, which represents a [VPC endpoint] object in AWS used to communicate
        privately with Databricks over [AWS PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html
        
        :param vpc_endpoint_id: str
          Databricks VPC endpoint ID.
        
        :returns: :class:`VpcEndpoint`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/vpc-endpoints/{vpc_endpoint_id}',
                           headers=headers)
        return VpcEndpoint.from_dict(res)

    def list(self) -> Iterator[VpcEndpoint]:
        """Get all VPC endpoint configurations.
        
        Gets a list of all VPC endpoints for an account, specified by ID.
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        
        :returns: Iterator over :class:`VpcEndpoint`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/vpc-endpoints', headers=headers)
        return [VpcEndpoint.from_dict(v) for v in res]


class WorkspacesAPI:
    """These APIs manage workspaces for this account. A Databricks workspace is an environment for accessing all
    of your Databricks assets. The workspace organizes objects (notebooks, libraries, and experiments) into
    folders, and provides access to data and computational resources such as clusters and jobs.
    
    These endpoints are available if your account is on the E2 version of the platform or on a select custom
    plan that allows multiple workspaces per account."""

    def __init__(self, api_client):
        self._api = api_client

    def wait_get_workspace_running(self,
                                   workspace_id: int,
                                   timeout=timedelta(minutes=20),
                                   callback: Optional[Callable[[Workspace], None]] = None) -> Workspace:
        deadline = time.time() + timeout.total_seconds()
        target_states = (WorkspaceStatus.RUNNING, )
        failure_states = (WorkspaceStatus.BANNED, WorkspaceStatus.FAILED, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get(workspace_id=workspace_id)
            status = poll.workspace_status
            status_message = poll.workspace_status_message
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach RUNNING, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"workspace_id={workspace_id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def create(self,
               workspace_name: str,
               *,
               aws_region: Optional[str] = None,
               cloud: Optional[str] = None,
               cloud_resource_container: Optional[CloudResourceContainer] = None,
               credentials_id: Optional[str] = None,
               custom_tags: Optional[Dict[str, str]] = None,
               deployment_name: Optional[str] = None,
               gcp_managed_network_config: Optional[GcpManagedNetworkConfig] = None,
               gke_config: Optional[GkeConfig] = None,
               location: Optional[str] = None,
               managed_services_customer_managed_key_id: Optional[str] = None,
               network_id: Optional[str] = None,
               pricing_tier: Optional[PricingTier] = None,
               private_access_settings_id: Optional[str] = None,
               storage_configuration_id: Optional[str] = None,
               storage_customer_managed_key_id: Optional[str] = None) -> Wait[Workspace]:
        """Create a new workspace.
        
        Creates a new workspace.
        
        **Important**: This operation is asynchronous. A response with HTTP status code 200 means the request
        has been accepted and is in progress, but does not mean that the workspace deployed successfully and
        is running. The initial workspace status is typically `PROVISIONING`. Use the workspace ID
        (`workspace_id`) field in the response to identify the new workspace and make repeated `GET` requests
        with the workspace ID and check its status. The workspace becomes available when the status changes to
        `RUNNING`.
        
        :param workspace_name: str
          The workspace's human-readable name.
        :param aws_region: str (optional)
          The AWS region of the workspace's data plane.
        :param cloud: str (optional)
          The cloud provider which the workspace uses. For Google Cloud workspaces, always set this field to
          `gcp`.
        :param cloud_resource_container: :class:`CloudResourceContainer` (optional)
          The general workspace configurations that are specific to cloud providers.
        :param credentials_id: str (optional)
          ID of the workspace's credential configuration object.
        :param custom_tags: Dict[str,str] (optional)
          The custom tags key-value pairing that is attached to this workspace. The key-value pair is a string
          of utf-8 characters. The value can be an empty string, with maximum length of 255 characters. The
          key can be of maximum length of 127 characters, and cannot be empty.
        :param deployment_name: str (optional)
          The deployment name defines part of the subdomain for the workspace. The workspace URL for the web
          application and REST APIs is `<workspace-deployment-name>.cloud.databricks.com`. For example, if the
          deployment name is `abcsales`, your workspace URL will be `https://abcsales.cloud.databricks.com`.
          Hyphens are allowed. This property supports only the set of characters that are allowed in a
          subdomain.
          
          To set this value, you must have a deployment name prefix. Contact your Databricks account team to
          add an account deployment name prefix to your account.
          
          Workspace deployment names follow the account prefix and a hyphen. For example, if your account's
          deployment prefix is `acme` and the workspace deployment name is `workspace-1`, the JSON response
          for the `deployment_name` field becomes `acme-workspace-1`. The workspace URL would be
          `acme-workspace-1.cloud.databricks.com`.
          
          You can also set the `deployment_name` to the reserved keyword `EMPTY` if you want the deployment
          name to only include the deployment prefix. For example, if your account's deployment prefix is
          `acme` and the workspace deployment name is `EMPTY`, the `deployment_name` becomes `acme` only and
          the workspace URL is `acme.cloud.databricks.com`.
          
          This value must be unique across all non-deleted deployments across all AWS regions.
          
          If a new workspace omits this property, the server generates a unique deployment name for you with
          the pattern `dbc-xxxxxxxx-xxxx`.
        :param gcp_managed_network_config: :class:`GcpManagedNetworkConfig` (optional)
          The network settings for the workspace. The configurations are only for Databricks-managed VPCs. It
          is ignored if you specify a customer-managed VPC in the `network_id` field.", All the IP range
          configurations must be mutually exclusive. An attempt to create a workspace fails if Databricks
          detects an IP range overlap.
          
          Specify custom IP ranges in CIDR format. The IP ranges for these fields must not overlap, and all IP
          addresses must be entirely within the following ranges: `10.0.0.0/8`, `100.64.0.0/10`,
          `172.16.0.0/12`, `192.168.0.0/16`, and `240.0.0.0/4`.
          
          The sizes of these IP ranges affect the maximum number of nodes for the workspace.
          
          **Important**: Confirm the IP ranges used by your Databricks workspace before creating the
          workspace. You cannot change them after your workspace is deployed. If the IP address ranges for
          your Databricks are too small, IP exhaustion can occur, causing your Databricks jobs to fail. To
          determine the address range sizes that you need, Databricks provides a calculator as a Microsoft
          Excel spreadsheet. See [calculate subnet sizes for a new workspace].
          
          [calculate subnet sizes for a new workspace]: https://docs.gcp.databricks.com/administration-guide/cloud-configurations/gcp/network-sizing.html
        :param gke_config: :class:`GkeConfig` (optional)
          The configurations for the GKE cluster of a Databricks workspace.
        :param location: str (optional)
          The Google Cloud region of the workspace data plane in your Google account. For example, `us-east4`.
        :param managed_services_customer_managed_key_id: str (optional)
          The ID of the workspace's managed services encryption key configuration object. This is used to help
          protect and control access to the workspace's notebooks, secrets, Databricks SQL queries, and query
          history. The provided key configuration object property `use_cases` must contain `MANAGED_SERVICES`.
        :param network_id: str (optional)
        :param pricing_tier: :class:`PricingTier` (optional)
          The pricing tier of the workspace. For pricing tier information, see [AWS Pricing].
          
          [AWS Pricing]: https://databricks.com/product/aws-pricing
        :param private_access_settings_id: str (optional)
          ID of the workspace's private access settings object. Only used for PrivateLink. This ID must be
          specified for customers using [AWS PrivateLink] for either front-end (user-to-workspace connection),
          back-end (data plane to control plane connection), or both connection types.
          
          Before configuring PrivateLink, read the [Databricks article about PrivateLink].",
          
          [AWS PrivateLink]: https://aws.amazon.com/privatelink/
          [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        :param storage_configuration_id: str (optional)
          The ID of the workspace's storage configuration object.
        :param storage_customer_managed_key_id: str (optional)
          The ID of the workspace's storage encryption key configuration object. This is used to encrypt the
          workspace's root S3 bucket (root DBFS and system data) and, optionally, cluster EBS volumes. The
          provided key configuration object property `use_cases` must contain `STORAGE`.
        
        :returns:
          Long-running operation waiter for :class:`Workspace`.
          See :method:wait_get_workspace_running for more details.
        """
        body = {}
        if aws_region is not None: body['aws_region'] = aws_region
        if cloud is not None: body['cloud'] = cloud
        if cloud_resource_container is not None:
            body['cloud_resource_container'] = cloud_resource_container.as_dict()
        if credentials_id is not None: body['credentials_id'] = credentials_id
        if custom_tags is not None: body['custom_tags'] = custom_tags
        if deployment_name is not None: body['deployment_name'] = deployment_name
        if gcp_managed_network_config is not None:
            body['gcp_managed_network_config'] = gcp_managed_network_config.as_dict()
        if gke_config is not None: body['gke_config'] = gke_config.as_dict()
        if location is not None: body['location'] = location
        if managed_services_customer_managed_key_id is not None:
            body['managed_services_customer_managed_key_id'] = managed_services_customer_managed_key_id
        if network_id is not None: body['network_id'] = network_id
        if pricing_tier is not None: body['pricing_tier'] = pricing_tier.value
        if private_access_settings_id is not None:
            body['private_access_settings_id'] = private_access_settings_id
        if storage_configuration_id is not None: body['storage_configuration_id'] = storage_configuration_id
        if storage_customer_managed_key_id is not None:
            body['storage_customer_managed_key_id'] = storage_customer_managed_key_id
        if workspace_name is not None: body['workspace_name'] = workspace_name
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        op_response = self._api.do('POST',
                                   f'/api/2.0/accounts/{self._api.account_id}/workspaces',
                                   body=body,
                                   headers=headers)
        return Wait(self.wait_get_workspace_running,
                    response=Workspace.from_dict(op_response),
                    workspace_id=op_response['workspace_id'])

    def create_and_wait(
        self,
        workspace_name: str,
        *,
        aws_region: Optional[str] = None,
        cloud: Optional[str] = None,
        cloud_resource_container: Optional[CloudResourceContainer] = None,
        credentials_id: Optional[str] = None,
        custom_tags: Optional[Dict[str, str]] = None,
        deployment_name: Optional[str] = None,
        gcp_managed_network_config: Optional[GcpManagedNetworkConfig] = None,
        gke_config: Optional[GkeConfig] = None,
        location: Optional[str] = None,
        managed_services_customer_managed_key_id: Optional[str] = None,
        network_id: Optional[str] = None,
        pricing_tier: Optional[PricingTier] = None,
        private_access_settings_id: Optional[str] = None,
        storage_configuration_id: Optional[str] = None,
        storage_customer_managed_key_id: Optional[str] = None,
        timeout=timedelta(minutes=20)) -> Workspace:
        return self.create(aws_region=aws_region,
                           cloud=cloud,
                           cloud_resource_container=cloud_resource_container,
                           credentials_id=credentials_id,
                           custom_tags=custom_tags,
                           deployment_name=deployment_name,
                           gcp_managed_network_config=gcp_managed_network_config,
                           gke_config=gke_config,
                           location=location,
                           managed_services_customer_managed_key_id=managed_services_customer_managed_key_id,
                           network_id=network_id,
                           pricing_tier=pricing_tier,
                           private_access_settings_id=private_access_settings_id,
                           storage_configuration_id=storage_configuration_id,
                           storage_customer_managed_key_id=storage_customer_managed_key_id,
                           workspace_name=workspace_name).result(timeout=timeout)

    def delete(self, workspace_id: int):
        """Delete a workspace.
        
        Terminates and deletes a Databricks workspace. From an API perspective, deletion is immediate.
        However, it might take a few minutes for all workspaces resources to be deleted, depending on the size
        and number of workspace resources.
        
        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account.
        
        :param workspace_id: int
          Workspace ID.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/workspaces/{workspace_id}',
                     headers=headers)

    def get(self, workspace_id: int) -> Workspace:
        """Get a workspace.
        
        Gets information including status for a Databricks workspace, specified by ID. In the response, the
        `workspace_status` field indicates the current status. After initial workspace creation (which is
        asynchronous), make repeated `GET` requests with the workspace ID and check its status. The workspace
        becomes available when the status changes to `RUNNING`.
        
        For information about how to create a new workspace with this API **including error handling**, see
        [Create a new workspace using the Account API].
        
        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account.
        
        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html
        
        :param workspace_id: int
          Workspace ID.
        
        :returns: :class:`Workspace`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/workspaces/{workspace_id}',
                           headers=headers)
        return Workspace.from_dict(res)

    def list(self) -> Iterator[Workspace]:
        """Get all workspaces.
        
        Gets a list of all workspaces associated with an account, specified by ID.
        
        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account.
        
        :returns: Iterator over :class:`Workspace`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/workspaces', headers=headers)
        return [Workspace.from_dict(v) for v in res]

    def update(self,
               workspace_id: int,
               *,
               aws_region: Optional[str] = None,
               credentials_id: Optional[str] = None,
               custom_tags: Optional[Dict[str, str]] = None,
               managed_services_customer_managed_key_id: Optional[str] = None,
               network_connectivity_config_id: Optional[str] = None,
               network_id: Optional[str] = None,
               storage_configuration_id: Optional[str] = None,
               storage_customer_managed_key_id: Optional[str] = None) -> Wait[Workspace]:
        """Update workspace configuration.
        
        Updates a workspace configuration for either a running workspace or a failed workspace. The elements
        that can be updated varies between these two use cases.
        
        ### Update a failed workspace You can update a Databricks workspace configuration for failed workspace
        deployment for some fields, but not all fields. For a failed workspace, this request supports updates
        to the following fields only: - Credential configuration ID - Storage configuration ID - Network
        configuration ID. Used only to add or change a network configuration for a customer-managed VPC. For a
        failed workspace only, you can convert a workspace with Databricks-managed VPC to use a
        customer-managed VPC by adding this ID. You cannot downgrade a workspace with a customer-managed VPC
        to be a Databricks-managed VPC. You can update the network configuration for a failed or running
        workspace to add PrivateLink support, though you must also add a private access settings object. - Key
        configuration ID for managed services (control plane storage, such as notebook source and Databricks
        SQL queries). Used only if you use customer-managed keys for managed services. - Key configuration ID
        for workspace storage (root S3 bucket and, optionally, EBS volumes). Used only if you use
        customer-managed keys for workspace storage. **Important**: If the workspace was ever in the running
        state, even if briefly before becoming a failed workspace, you cannot add a new key configuration ID
        for workspace storage. - Private access settings ID to add PrivateLink support. You can add or update
        the private access settings ID to upgrade a workspace to add support for front-end, back-end, or both
        types of connectivity. You cannot remove (downgrade) any existing front-end or back-end PrivateLink
        support on a workspace. - Custom tags. Given you provide an empty custom tags, the update would not be
        applied. - Network connectivity configuration ID to add serverless stable IP support. You can add or
        update the network connectivity configuration ID to ensure the workspace uses the same set of stable
        IP CIDR blocks to access your resources. You cannot remove a network connectivity configuration from
        the workspace once attached, you can only switch to another one.
        
        After calling the `PATCH` operation to update the workspace configuration, make repeated `GET`
        requests with the workspace ID and check the workspace status. The workspace is successful if the
        status changes to `RUNNING`.
        
        For information about how to create a new workspace with this API **including error handling**, see
        [Create a new workspace using the Account API].
        
        ### Update a running workspace You can update a Databricks workspace configuration for running
        workspaces for some fields, but not all fields. For a running workspace, this request supports
        updating the following fields only: - Credential configuration ID - Network configuration ID. Used
        only if you already use a customer-managed VPC. You cannot convert a running workspace from a
        Databricks-managed VPC to a customer-managed VPC. You can use a network configuration update in this
        API for a failed or running workspace to add support for PrivateLink, although you also need to add a
        private access settings object. - Key configuration ID for managed services (control plane storage,
        such as notebook source and Databricks SQL queries). Databricks does not directly encrypt the data
        with the customer-managed key (CMK). Databricks uses both the CMK and the Databricks managed key (DMK)
        that is unique to your workspace to encrypt the Data Encryption Key (DEK). Databricks uses the DEK to
        encrypt your workspace's managed services persisted data. If the workspace does not already have a CMK
        for managed services, adding this ID enables managed services encryption for new or updated data.
        Existing managed services data that existed before adding the key remains not encrypted with the DEK
        until it is modified. If the workspace already has customer-managed keys for managed services, this
        request rotates (changes) the CMK keys and the DEK is re-encrypted with the DMK and the new CMK. - Key
        configuration ID for workspace storage (root S3 bucket and, optionally, EBS volumes). You can set this
        only if the workspace does not already have a customer-managed key configuration for workspace
        storage. - Private access settings ID to add PrivateLink support. You can add or update the private
        access settings ID to upgrade a workspace to add support for front-end, back-end, or both types of
        connectivity. You cannot remove (downgrade) any existing front-end or back-end PrivateLink support on
        a workspace. - Custom tags. Given you provide an empty custom tags, the update would not be applied. -
        Network connectivity configuration ID to add serverless stable IP support. You can add or update the
        network connectivity configuration ID to ensure the workspace uses the same set of stable IP CIDR
        blocks to access your resources. You cannot remove a network connectivity configuration from the
        workspace once attached, you can only switch to another one.
        
        **Important**: To update a running workspace, your workspace must have no running compute resources
        that run in your workspace's VPC in the Classic data plane. For example, stop all all-purpose
        clusters, job clusters, pools with running clusters, and Classic SQL warehouses. If you do not
        terminate all cluster instances in the workspace before calling this API, the request will fail.
        
        ### Wait until changes take effect. After calling the `PATCH` operation to update the workspace
        configuration, make repeated `GET` requests with the workspace ID and check the workspace status and
        the status of the fields. * For workspaces with a Databricks-managed VPC, the workspace status becomes
        `PROVISIONING` temporarily (typically under 20 minutes). If the workspace update is successful, the
        workspace status changes to `RUNNING`. Note that you can also check the workspace status in the
        [Account Console]. However, you cannot use or create clusters for another 20 minutes after that status
        change. This results in a total of up to 40 minutes in which you cannot create clusters. If you create
        or use clusters before this time interval elapses, clusters do not launch successfully, fail, or could
        cause other unexpected behavior. * For workspaces with a customer-managed VPC, the workspace status
        stays at status `RUNNING` and the VPC change happens immediately. A change to the storage
        customer-managed key configuration ID might take a few minutes to update, so continue to check the
        workspace until you observe that it has been updated. If the update fails, the workspace might revert
        silently to its original configuration. After the workspace has been updated, you cannot use or create
        clusters for another 20 minutes. If you create or use clusters before this time interval elapses,
        clusters do not launch successfully, fail, or could cause other unexpected behavior.
        
        If you update the _storage_ customer-managed key configurations, it takes 20 minutes for the changes
        to fully take effect. During the 20 minute wait, it is important that you stop all REST API calls to
        the DBFS API. If you are modifying _only the managed services key configuration_, you can omit the 20
        minute wait.
        
        **Important**: Customer-managed keys and customer-managed VPCs are supported by only some deployment
        types and subscription types. If you have questions about availability, contact your Databricks
        representative.
        
        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account.
        
        [Account Console]: https://docs.databricks.com/administration-guide/account-settings-e2/account-console-e2.html
        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html
        
        :param workspace_id: int
          Workspace ID.
        :param aws_region: str (optional)
          The AWS region of the workspace's data plane (for example, `us-west-2`). This parameter is available
          only for updating failed workspaces.
        :param credentials_id: str (optional)
          ID of the workspace's credential configuration object. This parameter is available for updating both
          failed and running workspaces.
        :param custom_tags: Dict[str,str] (optional)
          The custom tags key-value pairing that is attached to this workspace. The key-value pair is a string
          of utf-8 characters. The value can be an empty string, with maximum length of 255 characters. The
          key can be of maximum length of 127 characters, and cannot be empty.
        :param managed_services_customer_managed_key_id: str (optional)
          The ID of the workspace's managed services encryption key configuration object. This parameter is
          available only for updating failed workspaces.
        :param network_connectivity_config_id: str (optional)
        :param network_id: str (optional)
          The ID of the workspace's network configuration object. Used only if you already use a
          customer-managed VPC. For failed workspaces only, you can switch from a Databricks-managed VPC to a
          customer-managed VPC by updating the workspace to add a network configuration ID.
        :param storage_configuration_id: str (optional)
          The ID of the workspace's storage configuration object. This parameter is available only for
          updating failed workspaces.
        :param storage_customer_managed_key_id: str (optional)
          The ID of the key configuration object for workspace storage. This parameter is available for
          updating both failed and running workspaces.
        
        :returns:
          Long-running operation waiter for :class:`Workspace`.
          See :method:wait_get_workspace_running for more details.
        """
        body = {}
        if aws_region is not None: body['aws_region'] = aws_region
        if credentials_id is not None: body['credentials_id'] = credentials_id
        if custom_tags is not None: body['custom_tags'] = custom_tags
        if managed_services_customer_managed_key_id is not None:
            body['managed_services_customer_managed_key_id'] = managed_services_customer_managed_key_id
        if network_connectivity_config_id is not None:
            body['network_connectivity_config_id'] = network_connectivity_config_id
        if network_id is not None: body['network_id'] = network_id
        if storage_configuration_id is not None: body['storage_configuration_id'] = storage_configuration_id
        if storage_customer_managed_key_id is not None:
            body['storage_customer_managed_key_id'] = storage_customer_managed_key_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        op_response = self._api.do('PATCH',
                                   f'/api/2.0/accounts/{self._api.account_id}/workspaces/{workspace_id}',
                                   body=body,
                                   headers=headers)
        return Wait(self.wait_get_workspace_running,
                    response=UpdateResponse.from_dict(op_response),
                    workspace_id=workspace_id)

    def update_and_wait(
        self,
        workspace_id: int,
        *,
        aws_region: Optional[str] = None,
        credentials_id: Optional[str] = None,
        custom_tags: Optional[Dict[str, str]] = None,
        managed_services_customer_managed_key_id: Optional[str] = None,
        network_connectivity_config_id: Optional[str] = None,
        network_id: Optional[str] = None,
        storage_configuration_id: Optional[str] = None,
        storage_customer_managed_key_id: Optional[str] = None,
        timeout=timedelta(minutes=20)) -> Workspace:
        return self.update(aws_region=aws_region,
                           credentials_id=credentials_id,
                           custom_tags=custom_tags,
                           managed_services_customer_managed_key_id=managed_services_customer_managed_key_id,
                           network_connectivity_config_id=network_connectivity_config_id,
                           network_id=network_id,
                           storage_configuration_id=storage_configuration_id,
                           storage_customer_managed_key_id=storage_customer_managed_key_id,
                           workspace_id=workspace_id).result(timeout=timeout)

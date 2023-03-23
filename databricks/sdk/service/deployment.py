# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
import random
import time
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Dict, Iterator, List

from ..errors import OperationFailed
from ._internal import Wait, _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AwsCredentials:
    sts_role: 'StsRole' = None

    def as_dict(self) -> dict:
        body = {}
        if self.sts_role: body['sts_role'] = self.sts_role.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AwsCredentials':
        return cls(sts_role=_from_dict(d, 'sts_role', StsRole))


@dataclass
class AwsKeyInfo:
    key_arn: str
    key_region: str
    key_alias: str = None
    reuse_key_for_cluster_volumes: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.key_alias: body['key_alias'] = self.key_alias
        if self.key_arn: body['key_arn'] = self.key_arn
        if self.key_region: body['key_region'] = self.key_region
        if self.reuse_key_for_cluster_volumes:
            body['reuse_key_for_cluster_volumes'] = self.reuse_key_for_cluster_volumes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AwsKeyInfo':
        return cls(key_alias=d.get('key_alias', None),
                   key_arn=d.get('key_arn', None),
                   key_region=d.get('key_region', None),
                   reuse_key_for_cluster_volumes=d.get('reuse_key_for_cluster_volumes', None))


@dataclass
class CloudResourceContainer:
    """The general workspace configurations that are specific to cloud providers."""

    gcp: 'CustomerFacingGcpCloudResourceContainer' = None

    def as_dict(self) -> dict:
        body = {}
        if self.gcp: body['gcp'] = self.gcp.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CloudResourceContainer':
        return cls(gcp=_from_dict(d, 'gcp', CustomerFacingGcpCloudResourceContainer))


@dataclass
class CreateAwsKeyInfo:
    key_arn: str
    key_alias: str = None
    reuse_key_for_cluster_volumes: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.key_alias: body['key_alias'] = self.key_alias
        if self.key_arn: body['key_arn'] = self.key_arn
        if self.reuse_key_for_cluster_volumes:
            body['reuse_key_for_cluster_volumes'] = self.reuse_key_for_cluster_volumes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateAwsKeyInfo':
        return cls(key_alias=d.get('key_alias', None),
                   key_arn=d.get('key_arn', None),
                   reuse_key_for_cluster_volumes=d.get('reuse_key_for_cluster_volumes', None))


@dataclass
class CreateCredentialAwsCredentials:
    sts_role: 'CreateCredentialStsRole' = None

    def as_dict(self) -> dict:
        body = {}
        if self.sts_role: body['sts_role'] = self.sts_role.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCredentialAwsCredentials':
        return cls(sts_role=_from_dict(d, 'sts_role', CreateCredentialStsRole))


@dataclass
class CreateCredentialRequest:
    credentials_name: str
    aws_credentials: 'CreateCredentialAwsCredentials'

    def as_dict(self) -> dict:
        body = {}
        if self.aws_credentials: body['aws_credentials'] = self.aws_credentials.as_dict()
        if self.credentials_name: body['credentials_name'] = self.credentials_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCredentialRequest':
        return cls(aws_credentials=_from_dict(d, 'aws_credentials', CreateCredentialAwsCredentials),
                   credentials_name=d.get('credentials_name', None))


@dataclass
class CreateCredentialStsRole:
    role_arn: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.role_arn: body['role_arn'] = self.role_arn
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCredentialStsRole':
        return cls(role_arn=d.get('role_arn', None))


@dataclass
class CreateCustomerManagedKeyRequest:
    aws_key_info: 'CreateAwsKeyInfo'
    use_cases: 'List[KeyUseCase]'

    def as_dict(self) -> dict:
        body = {}
        if self.aws_key_info: body['aws_key_info'] = self.aws_key_info.as_dict()
        if self.use_cases: body['use_cases'] = [v for v in self.use_cases]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCustomerManagedKeyRequest':
        return cls(aws_key_info=_from_dict(d, 'aws_key_info', CreateAwsKeyInfo),
                   use_cases=d.get('use_cases', None))


@dataclass
class CreateNetworkRequest:
    network_name: str
    gcp_network_info: 'GcpNetworkInfo' = None
    security_group_ids: 'List[str]' = None
    subnet_ids: 'List[str]' = None
    vpc_endpoints: 'NetworkVpcEndpoints' = None
    vpc_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.gcp_network_info: body['gcp_network_info'] = self.gcp_network_info.as_dict()
        if self.network_name: body['network_name'] = self.network_name
        if self.security_group_ids: body['security_group_ids'] = [v for v in self.security_group_ids]
        if self.subnet_ids: body['subnet_ids'] = [v for v in self.subnet_ids]
        if self.vpc_endpoints: body['vpc_endpoints'] = self.vpc_endpoints.as_dict()
        if self.vpc_id: body['vpc_id'] = self.vpc_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateNetworkRequest':
        return cls(gcp_network_info=_from_dict(d, 'gcp_network_info', GcpNetworkInfo),
                   network_name=d.get('network_name', None),
                   security_group_ids=d.get('security_group_ids', None),
                   subnet_ids=d.get('subnet_ids', None),
                   vpc_endpoints=_from_dict(d, 'vpc_endpoints', NetworkVpcEndpoints),
                   vpc_id=d.get('vpc_id', None))


@dataclass
class CreateStorageConfigurationRequest:
    storage_configuration_name: str
    root_bucket_info: 'RootBucketInfo'

    def as_dict(self) -> dict:
        body = {}
        if self.root_bucket_info: body['root_bucket_info'] = self.root_bucket_info.as_dict()
        if self.storage_configuration_name:
            body['storage_configuration_name'] = self.storage_configuration_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateStorageConfigurationRequest':
        return cls(root_bucket_info=_from_dict(d, 'root_bucket_info', RootBucketInfo),
                   storage_configuration_name=d.get('storage_configuration_name', None))


@dataclass
class CreateVpcEndpointRequest:
    vpc_endpoint_name: str
    aws_vpc_endpoint_id: str
    region: str

    def as_dict(self) -> dict:
        body = {}
        if self.aws_vpc_endpoint_id: body['aws_vpc_endpoint_id'] = self.aws_vpc_endpoint_id
        if self.region: body['region'] = self.region
        if self.vpc_endpoint_name: body['vpc_endpoint_name'] = self.vpc_endpoint_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateVpcEndpointRequest':
        return cls(aws_vpc_endpoint_id=d.get('aws_vpc_endpoint_id', None),
                   region=d.get('region', None),
                   vpc_endpoint_name=d.get('vpc_endpoint_name', None))


@dataclass
class CreateWorkspaceRequest:
    workspace_name: str
    aws_region: str = None
    cloud: str = None
    cloud_resource_container: 'CloudResourceContainer' = None
    credentials_id: str = None
    deployment_name: str = None
    location: str = None
    managed_services_customer_managed_key_id: str = None
    network_id: str = None
    pricing_tier: 'PricingTier' = None
    private_access_settings_id: str = None
    storage_configuration_id: str = None
    storage_customer_managed_key_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.aws_region: body['aws_region'] = self.aws_region
        if self.cloud: body['cloud'] = self.cloud
        if self.cloud_resource_container:
            body['cloud_resource_container'] = self.cloud_resource_container.as_dict()
        if self.credentials_id: body['credentials_id'] = self.credentials_id
        if self.deployment_name: body['deployment_name'] = self.deployment_name
        if self.location: body['location'] = self.location
        if self.managed_services_customer_managed_key_id:
            body['managed_services_customer_managed_key_id'] = self.managed_services_customer_managed_key_id
        if self.network_id: body['network_id'] = self.network_id
        if self.pricing_tier: body['pricing_tier'] = self.pricing_tier.value
        if self.private_access_settings_id:
            body['private_access_settings_id'] = self.private_access_settings_id
        if self.storage_configuration_id: body['storage_configuration_id'] = self.storage_configuration_id
        if self.storage_customer_managed_key_id:
            body['storage_customer_managed_key_id'] = self.storage_customer_managed_key_id
        if self.workspace_name: body['workspace_name'] = self.workspace_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateWorkspaceRequest':
        return cls(aws_region=d.get('aws_region', None),
                   cloud=d.get('cloud', None),
                   cloud_resource_container=_from_dict(d, 'cloud_resource_container', CloudResourceContainer),
                   credentials_id=d.get('credentials_id', None),
                   deployment_name=d.get('deployment_name', None),
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
    account_id: str = None
    aws_credentials: 'AwsCredentials' = None
    creation_time: int = None
    credentials_id: str = None
    credentials_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.account_id: body['account_id'] = self.account_id
        if self.aws_credentials: body['aws_credentials'] = self.aws_credentials.as_dict()
        if self.creation_time: body['creation_time'] = self.creation_time
        if self.credentials_id: body['credentials_id'] = self.credentials_id
        if self.credentials_name: body['credentials_name'] = self.credentials_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Credential':
        return cls(account_id=d.get('account_id', None),
                   aws_credentials=_from_dict(d, 'aws_credentials', AwsCredentials),
                   creation_time=d.get('creation_time', None),
                   credentials_id=d.get('credentials_id', None),
                   credentials_name=d.get('credentials_name', None))


@dataclass
class CustomerFacingGcpCloudResourceContainer:
    """The general workspace configurations that are specific to Google Cloud."""

    project_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.project_id: body['project_id'] = self.project_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CustomerFacingGcpCloudResourceContainer':
        return cls(project_id=d.get('project_id', None))


@dataclass
class CustomerManagedKey:
    account_id: str = None
    aws_key_info: 'AwsKeyInfo' = None
    creation_time: int = None
    customer_managed_key_id: str = None
    use_cases: 'List[KeyUseCase]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.account_id: body['account_id'] = self.account_id
        if self.aws_key_info: body['aws_key_info'] = self.aws_key_info.as_dict()
        if self.creation_time: body['creation_time'] = self.creation_time
        if self.customer_managed_key_id: body['customer_managed_key_id'] = self.customer_managed_key_id
        if self.use_cases: body['use_cases'] = [v for v in self.use_cases]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CustomerManagedKey':
        return cls(account_id=d.get('account_id', None),
                   aws_key_info=_from_dict(d, 'aws_key_info', AwsKeyInfo),
                   creation_time=d.get('creation_time', None),
                   customer_managed_key_id=d.get('customer_managed_key_id', None),
                   use_cases=d.get('use_cases', None))


@dataclass
class DeleteCredentialRequest:
    """Delete credential configuration"""

    credentials_id: str


@dataclass
class DeleteEncryptionKeyRequest:
    """Delete encryption key configuration"""

    customer_managed_key_id: str


@dataclass
class DeleteNetworkRequest:
    """Delete a network configuration"""

    network_id: str


@dataclass
class DeletePrivateAccesRequest:
    """Delete a private access settings object"""

    private_access_settings_id: str


@dataclass
class DeleteStorageRequest:
    """Delete storage configuration"""

    storage_configuration_id: str


@dataclass
class DeleteVpcEndpointRequest:
    """Delete VPC endpoint configuration"""

    vpc_endpoint_id: str


@dataclass
class DeleteWorkspaceRequest:
    """Delete a workspace"""

    workspace_id: int


class EndpointUseCase(Enum):
    """This enumeration represents the type of Databricks VPC [endpoint service] that was used when
    creating this VPC endpoint.
    
    If the VPC endpoint connects to the Databricks control plane for either the front-end connection
    or the back-end REST API connection, the value is `WORKSPACE_ACCESS`.
    
    If the VPC endpoint connects to the Databricks workspace for the back-end [secure cluster
    connectivity] relay, the value is `DATAPLANE_RELAY_ACCESS`.
    
    [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service.html
    [secure cluster connectivity]: https://docs.databricks.com/security/secure-cluster-connectivity.html"""

    DATAPLANE_RELAY_ACCESS = 'DATAPLANE_RELAY_ACCESS'
    WORKSPACE_ACCESS = 'WORKSPACE_ACCESS'


class ErrorType(Enum):
    """The AWS resource associated with this error: credentials, VPC, subnet, security group, or
    network ACL."""

    credentials = 'credentials'
    networkAcl = 'networkAcl'
    securityGroup = 'securityGroup'
    subnet = 'subnet'
    vpc = 'vpc'


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

    gke_cluster_pod_ip_range: str = None
    gke_cluster_service_ip_range: str = None
    subnet_cidr: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.gke_cluster_pod_ip_range: body['gke_cluster_pod_ip_range'] = self.gke_cluster_pod_ip_range
        if self.gke_cluster_service_ip_range:
            body['gke_cluster_service_ip_range'] = self.gke_cluster_service_ip_range
        if self.subnet_cidr: body['subnet_cidr'] = self.subnet_cidr
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GcpManagedNetworkConfig':
        return cls(gke_cluster_pod_ip_range=d.get('gke_cluster_pod_ip_range', None),
                   gke_cluster_service_ip_range=d.get('gke_cluster_service_ip_range', None),
                   subnet_cidr=d.get('subnet_cidr', None))


@dataclass
class GcpNetworkInfo:
    """The Google Cloud specific information for this network (for example, the VPC ID, subnet ID, and
    secondary IP ranges)."""

    network_project_id: str
    vpc_id: str
    subnet_id: str
    subnet_region: str
    pod_ip_range_name: str
    service_ip_range_name: str

    def as_dict(self) -> dict:
        body = {}
        if self.network_project_id: body['network_project_id'] = self.network_project_id
        if self.pod_ip_range_name: body['pod_ip_range_name'] = self.pod_ip_range_name
        if self.service_ip_range_name: body['service_ip_range_name'] = self.service_ip_range_name
        if self.subnet_id: body['subnet_id'] = self.subnet_id
        if self.subnet_region: body['subnet_region'] = self.subnet_region
        if self.vpc_id: body['vpc_id'] = self.vpc_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GcpNetworkInfo':
        return cls(network_project_id=d.get('network_project_id', None),
                   pod_ip_range_name=d.get('pod_ip_range_name', None),
                   service_ip_range_name=d.get('service_ip_range_name', None),
                   subnet_id=d.get('subnet_id', None),
                   subnet_region=d.get('subnet_region', None),
                   vpc_id=d.get('vpc_id', None))


@dataclass
class GetCredentialRequest:
    """Get credential configuration"""

    credentials_id: str


@dataclass
class GetEncryptionKeyRequest:
    """Get encryption key configuration"""

    customer_managed_key_id: str


@dataclass
class GetNetworkRequest:
    """Get a network configuration"""

    network_id: str


@dataclass
class GetPrivateAccesRequest:
    """Get a private access settings object"""

    private_access_settings_id: str


@dataclass
class GetStorageRequest:
    """Get storage configuration"""

    storage_configuration_id: str


@dataclass
class GetVpcEndpointRequest:
    """Get a VPC endpoint configuration"""

    vpc_endpoint_id: str


@dataclass
class GetWorkspaceRequest:
    """Get a workspace"""

    workspace_id: int


@dataclass
class GkeConfig:
    """The configurations for the GKE cluster of a Databricks workspace."""

    connectivity_type: 'GkeConfigConnectivityType' = None
    master_ip_range: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.connectivity_type: body['connectivity_type'] = self.connectivity_type.value
        if self.master_ip_range: body['master_ip_range'] = self.master_ip_range
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GkeConfig':
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
    """This describes an enum"""

    MANAGED_SERVICES = 'MANAGED_SERVICES'
    STORAGE = 'STORAGE'


@dataclass
class Network:
    account_id: str = None
    creation_time: int = None
    error_messages: 'List[NetworkHealth]' = None
    gcp_network_info: 'GcpNetworkInfo' = None
    network_id: str = None
    network_name: str = None
    security_group_ids: 'List[str]' = None
    subnet_ids: 'List[str]' = None
    vpc_endpoints: 'NetworkVpcEndpoints' = None
    vpc_id: str = None
    vpc_status: 'VpcStatus' = None
    warning_messages: 'List[NetworkWarning]' = None
    workspace_id: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.account_id: body['account_id'] = self.account_id
        if self.creation_time: body['creation_time'] = self.creation_time
        if self.error_messages: body['error_messages'] = [v.as_dict() for v in self.error_messages]
        if self.gcp_network_info: body['gcp_network_info'] = self.gcp_network_info.as_dict()
        if self.network_id: body['network_id'] = self.network_id
        if self.network_name: body['network_name'] = self.network_name
        if self.security_group_ids: body['security_group_ids'] = [v for v in self.security_group_ids]
        if self.subnet_ids: body['subnet_ids'] = [v for v in self.subnet_ids]
        if self.vpc_endpoints: body['vpc_endpoints'] = self.vpc_endpoints.as_dict()
        if self.vpc_id: body['vpc_id'] = self.vpc_id
        if self.vpc_status: body['vpc_status'] = self.vpc_status.value
        if self.warning_messages: body['warning_messages'] = [v.as_dict() for v in self.warning_messages]
        if self.workspace_id: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Network':
        return cls(account_id=d.get('account_id', None),
                   creation_time=d.get('creation_time', None),
                   error_messages=_repeated(d, 'error_messages', NetworkHealth),
                   gcp_network_info=_from_dict(d, 'gcp_network_info', GcpNetworkInfo),
                   network_id=d.get('network_id', None),
                   network_name=d.get('network_name', None),
                   security_group_ids=d.get('security_group_ids', None),
                   subnet_ids=d.get('subnet_ids', None),
                   vpc_endpoints=_from_dict(d, 'vpc_endpoints', NetworkVpcEndpoints),
                   vpc_id=d.get('vpc_id', None),
                   vpc_status=_enum(d, 'vpc_status', VpcStatus),
                   warning_messages=_repeated(d, 'warning_messages', NetworkWarning),
                   workspace_id=d.get('workspace_id', None))


@dataclass
class NetworkHealth:
    error_message: str = None
    error_type: 'ErrorType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.error_message: body['error_message'] = self.error_message
        if self.error_type: body['error_type'] = self.error_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NetworkHealth':
        return cls(error_message=d.get('error_message', None), error_type=_enum(d, 'error_type', ErrorType))


@dataclass
class NetworkVpcEndpoints:
    """If specified, contains the VPC endpoints used to allow cluster communication from this VPC over
    [AWS PrivateLink].
    
    [AWS PrivateLink]: https://aws.amazon.com/privatelink/"""

    rest_api: 'List[str]'
    dataplane_relay: 'List[str]'

    def as_dict(self) -> dict:
        body = {}
        if self.dataplane_relay: body['dataplane_relay'] = [v for v in self.dataplane_relay]
        if self.rest_api: body['rest_api'] = [v for v in self.rest_api]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NetworkVpcEndpoints':
        return cls(dataplane_relay=d.get('dataplane_relay', None), rest_api=d.get('rest_api', None))


@dataclass
class NetworkWarning:
    warning_message: str = None
    warning_type: 'WarningType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.warning_message: body['warning_message'] = self.warning_message
        if self.warning_type: body['warning_type'] = self.warning_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NetworkWarning':
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
    account_id: str = None
    allowed_vpc_endpoint_ids: 'List[str]' = None
    private_access_level: 'PrivateAccessLevel' = None
    private_access_settings_id: str = None
    private_access_settings_name: str = None
    public_access_enabled: bool = None
    region: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.account_id: body['account_id'] = self.account_id
        if self.allowed_vpc_endpoint_ids:
            body['allowed_vpc_endpoint_ids'] = [v for v in self.allowed_vpc_endpoint_ids]
        if self.private_access_level: body['private_access_level'] = self.private_access_level.value
        if self.private_access_settings_id:
            body['private_access_settings_id'] = self.private_access_settings_id
        if self.private_access_settings_name:
            body['private_access_settings_name'] = self.private_access_settings_name
        if self.public_access_enabled: body['public_access_enabled'] = self.public_access_enabled
        if self.region: body['region'] = self.region
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PrivateAccessSettings':
        return cls(account_id=d.get('account_id', None),
                   allowed_vpc_endpoint_ids=d.get('allowed_vpc_endpoint_ids', None),
                   private_access_level=_enum(d, 'private_access_level', PrivateAccessLevel),
                   private_access_settings_id=d.get('private_access_settings_id', None),
                   private_access_settings_name=d.get('private_access_settings_name', None),
                   public_access_enabled=d.get('public_access_enabled', None),
                   region=d.get('region', None))


@dataclass
class RootBucketInfo:
    """Root S3 bucket information."""

    bucket_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.bucket_name: body['bucket_name'] = self.bucket_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RootBucketInfo':
        return cls(bucket_name=d.get('bucket_name', None))


@dataclass
class StorageConfiguration:
    account_id: str = None
    creation_time: int = None
    root_bucket_info: 'RootBucketInfo' = None
    storage_configuration_id: str = None
    storage_configuration_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.account_id: body['account_id'] = self.account_id
        if self.creation_time: body['creation_time'] = self.creation_time
        if self.root_bucket_info: body['root_bucket_info'] = self.root_bucket_info.as_dict()
        if self.storage_configuration_id: body['storage_configuration_id'] = self.storage_configuration_id
        if self.storage_configuration_name:
            body['storage_configuration_name'] = self.storage_configuration_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StorageConfiguration':
        return cls(account_id=d.get('account_id', None),
                   creation_time=d.get('creation_time', None),
                   root_bucket_info=_from_dict(d, 'root_bucket_info', RootBucketInfo),
                   storage_configuration_id=d.get('storage_configuration_id', None),
                   storage_configuration_name=d.get('storage_configuration_name', None))


@dataclass
class StsRole:
    external_id: str = None
    role_arn: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.external_id: body['external_id'] = self.external_id
        if self.role_arn: body['role_arn'] = self.role_arn
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StsRole':
        return cls(external_id=d.get('external_id', None), role_arn=d.get('role_arn', None))


@dataclass
class UpdateWorkspaceRequest:
    workspace_id: int
    aws_region: str = None
    credentials_id: str = None
    managed_services_customer_managed_key_id: str = None
    network_id: str = None
    storage_configuration_id: str = None
    storage_customer_managed_key_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.aws_region: body['aws_region'] = self.aws_region
        if self.credentials_id: body['credentials_id'] = self.credentials_id
        if self.managed_services_customer_managed_key_id:
            body['managed_services_customer_managed_key_id'] = self.managed_services_customer_managed_key_id
        if self.network_id: body['network_id'] = self.network_id
        if self.storage_configuration_id: body['storage_configuration_id'] = self.storage_configuration_id
        if self.storage_customer_managed_key_id:
            body['storage_customer_managed_key_id'] = self.storage_customer_managed_key_id
        if self.workspace_id: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateWorkspaceRequest':
        return cls(aws_region=d.get('aws_region', None),
                   credentials_id=d.get('credentials_id', None),
                   managed_services_customer_managed_key_id=d.get('managed_services_customer_managed_key_id',
                                                                  None),
                   network_id=d.get('network_id', None),
                   storage_configuration_id=d.get('storage_configuration_id', None),
                   storage_customer_managed_key_id=d.get('storage_customer_managed_key_id', None),
                   workspace_id=d.get('workspace_id', None))


@dataclass
class UpsertPrivateAccessSettingsRequest:
    private_access_settings_name: str
    region: str
    private_access_settings_id: str
    allowed_vpc_endpoint_ids: 'List[str]' = None
    private_access_level: 'PrivateAccessLevel' = None
    public_access_enabled: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.allowed_vpc_endpoint_ids:
            body['allowed_vpc_endpoint_ids'] = [v for v in self.allowed_vpc_endpoint_ids]
        if self.private_access_level: body['private_access_level'] = self.private_access_level.value
        if self.private_access_settings_id:
            body['private_access_settings_id'] = self.private_access_settings_id
        if self.private_access_settings_name:
            body['private_access_settings_name'] = self.private_access_settings_name
        if self.public_access_enabled: body['public_access_enabled'] = self.public_access_enabled
        if self.region: body['region'] = self.region
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpsertPrivateAccessSettingsRequest':
        return cls(allowed_vpc_endpoint_ids=d.get('allowed_vpc_endpoint_ids', None),
                   private_access_level=_enum(d, 'private_access_level', PrivateAccessLevel),
                   private_access_settings_id=d.get('private_access_settings_id', None),
                   private_access_settings_name=d.get('private_access_settings_name', None),
                   public_access_enabled=d.get('public_access_enabled', None),
                   region=d.get('region', None))


@dataclass
class VpcEndpoint:
    account_id: str = None
    aws_account_id: str = None
    aws_endpoint_service_id: str = None
    aws_vpc_endpoint_id: str = None
    region: str = None
    state: str = None
    use_case: 'EndpointUseCase' = None
    vpc_endpoint_id: str = None
    vpc_endpoint_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.account_id: body['account_id'] = self.account_id
        if self.aws_account_id: body['aws_account_id'] = self.aws_account_id
        if self.aws_endpoint_service_id: body['aws_endpoint_service_id'] = self.aws_endpoint_service_id
        if self.aws_vpc_endpoint_id: body['aws_vpc_endpoint_id'] = self.aws_vpc_endpoint_id
        if self.region: body['region'] = self.region
        if self.state: body['state'] = self.state
        if self.use_case: body['use_case'] = self.use_case.value
        if self.vpc_endpoint_id: body['vpc_endpoint_id'] = self.vpc_endpoint_id
        if self.vpc_endpoint_name: body['vpc_endpoint_name'] = self.vpc_endpoint_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'VpcEndpoint':
        return cls(account_id=d.get('account_id', None),
                   aws_account_id=d.get('aws_account_id', None),
                   aws_endpoint_service_id=d.get('aws_endpoint_service_id', None),
                   aws_vpc_endpoint_id=d.get('aws_vpc_endpoint_id', None),
                   region=d.get('region', None),
                   state=d.get('state', None),
                   use_case=_enum(d, 'use_case', EndpointUseCase),
                   vpc_endpoint_id=d.get('vpc_endpoint_id', None),
                   vpc_endpoint_name=d.get('vpc_endpoint_name', None))


class VpcStatus(Enum):
    """This describes an enum"""

    BROKEN = 'BROKEN'
    UNATTACHED = 'UNATTACHED'
    VALID = 'VALID'
    WARNED = 'WARNED'


class WarningType(Enum):
    """The AWS resource associated with this warning: a subnet or a security group."""

    securityGroup = 'securityGroup'
    subnet = 'subnet'


@dataclass
class Workspace:
    account_id: str = None
    aws_region: str = None
    cloud: str = None
    cloud_resource_container: 'CloudResourceContainer' = None
    creation_time: int = None
    credentials_id: str = None
    deployment_name: str = None
    gcp_managed_network_config: 'GcpManagedNetworkConfig' = None
    gke_config: 'GkeConfig' = None
    location: str = None
    managed_services_customer_managed_key_id: str = None
    network_id: str = None
    pricing_tier: 'PricingTier' = None
    private_access_settings_id: str = None
    storage_configuration_id: str = None
    storage_customer_managed_key_id: str = None
    workspace_id: int = None
    workspace_name: str = None
    workspace_status: 'WorkspaceStatus' = None
    workspace_status_message: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.account_id: body['account_id'] = self.account_id
        if self.aws_region: body['aws_region'] = self.aws_region
        if self.cloud: body['cloud'] = self.cloud
        if self.cloud_resource_container:
            body['cloud_resource_container'] = self.cloud_resource_container.as_dict()
        if self.creation_time: body['creation_time'] = self.creation_time
        if self.credentials_id: body['credentials_id'] = self.credentials_id
        if self.deployment_name: body['deployment_name'] = self.deployment_name
        if self.gcp_managed_network_config:
            body['gcp_managed_network_config'] = self.gcp_managed_network_config.as_dict()
        if self.gke_config: body['gke_config'] = self.gke_config.as_dict()
        if self.location: body['location'] = self.location
        if self.managed_services_customer_managed_key_id:
            body['managed_services_customer_managed_key_id'] = self.managed_services_customer_managed_key_id
        if self.network_id: body['network_id'] = self.network_id
        if self.pricing_tier: body['pricing_tier'] = self.pricing_tier.value
        if self.private_access_settings_id:
            body['private_access_settings_id'] = self.private_access_settings_id
        if self.storage_configuration_id: body['storage_configuration_id'] = self.storage_configuration_id
        if self.storage_customer_managed_key_id:
            body['storage_customer_managed_key_id'] = self.storage_customer_managed_key_id
        if self.workspace_id: body['workspace_id'] = self.workspace_id
        if self.workspace_name: body['workspace_name'] = self.workspace_name
        if self.workspace_status: body['workspace_status'] = self.workspace_status.value
        if self.workspace_status_message: body['workspace_status_message'] = self.workspace_status_message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Workspace':
        return cls(account_id=d.get('account_id', None),
                   aws_region=d.get('aws_region', None),
                   cloud=d.get('cloud', None),
                   cloud_resource_container=_from_dict(d, 'cloud_resource_container', CloudResourceContainer),
                   creation_time=d.get('creation_time', None),
                   credentials_id=d.get('credentials_id', None),
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

    def create(self, credentials_name: str, aws_credentials: CreateCredentialAwsCredentials,
               **kwargs) -> Credential:
        """Create credential configuration.
        
        Creates a Databricks credential configuration that represents cloud cross-account credentials for a
        specified account. Databricks uses this to set up network infrastructure properly to host Databricks
        clusters. For your AWS IAM role, you need to trust the External ID (the Databricks Account API account
        ID) in the returned credential object, and configure the required access policy.
        
        Save the response's `credentials_id` field, which is the ID for your new credential configuration
        object.
        
        For information about how to create a new workspace with this API, see [Create a new workspace using
        the Account API]
        
        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateCredentialRequest(aws_credentials=aws_credentials,
                                              credentials_name=credentials_name)
        body = request.as_dict()

        json = self._api.do('POST', f'/api/2.0/accounts/{self._api.account_id}/credentials', body=body)
        return Credential.from_dict(json)

    def delete(self, credentials_id: str, **kwargs):
        """Delete credential configuration.
        
        Deletes a Databricks credential configuration object for an account, both specified by ID. You cannot
        delete a credential that is associated with any workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteCredentialRequest(credentials_id=credentials_id)

        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/credentials/{request.credentials_id}')

    def get(self, credentials_id: str, **kwargs) -> Credential:
        """Get credential configuration.
        
        Gets a Databricks credential configuration object for an account, both specified by ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetCredentialRequest(credentials_id=credentials_id)

        json = self._api.do('GET',
                            f'/api/2.0/accounts/{self._api.account_id}/credentials/{request.credentials_id}')
        return Credential.from_dict(json)

    def list(self) -> Iterator[Credential]:
        """Get all credential configurations.
        
        Gets all Databricks credential configurations associated with an account specified by ID."""

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/credentials')
        return [Credential.from_dict(v) for v in json]


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

    def create(self, aws_key_info: CreateAwsKeyInfo, use_cases: List[KeyUseCase],
               **kwargs) -> CustomerManagedKey:
        """Create encryption key configuration.
        
        Creates a customer-managed key configuration object for an account, specified by ID. This operation
        uploads a reference to a customer-managed key to Databricks. If the key is assigned as a workspace's
        customer-managed key for managed services, Databricks uses the key to encrypt the workspaces notebooks
        and secrets in the control plane, in addition to Databricks SQL queries and query history. If it is
        specified as a workspace's customer-managed key for workspace storage, the key encrypts the
        workspace's root S3 bucket (which contains the workspace's root DBFS and system data) and, optionally,
        cluster EBS volume data.
        
        **Important**: Customer-managed keys are supported only for some deployment types, subscription types,
        and AWS regions.
        
        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateCustomerManagedKeyRequest(aws_key_info=aws_key_info, use_cases=use_cases)
        body = request.as_dict()

        json = self._api.do('POST',
                            f'/api/2.0/accounts/{self._api.account_id}/customer-managed-keys',
                            body=body)
        return CustomerManagedKey.from_dict(json)

    def delete(self, customer_managed_key_id: str, **kwargs):
        """Delete encryption key configuration.
        
        Deletes a customer-managed key configuration object for an account. You cannot delete a configuration
        that is associated with a running workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteEncryptionKeyRequest(customer_managed_key_id=customer_managed_key_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/customer-managed-keys/{request.customer_managed_key_id}'
        )

    def get(self, customer_managed_key_id: str, **kwargs) -> CustomerManagedKey:
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
        
        This operation is available only if your account is on the E2 version of the platform."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetEncryptionKeyRequest(customer_managed_key_id=customer_managed_key_id)

        json = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/customer-managed-keys/{request.customer_managed_key_id}'
        )
        return CustomerManagedKey.from_dict(json)

    def list(self) -> Iterator[CustomerManagedKey]:
        """Get all encryption key configurations.
        
        Gets all customer-managed key configuration objects for an account. If the key is specified as a
        workspace's managed services customer-managed key, Databricks uses the key to encrypt the workspace's
        notebooks and secrets in the control plane, in addition to Databricks SQL queries and query history.
        If the key is specified as a workspace's storage customer-managed key, the key is used to encrypt the
        workspace's root S3 bucket and optionally can encrypt cluster EBS volumes data in the data plane.
        
        **Important**: Customer-managed keys are supported only for some deployment types, subscription types,
        and AWS regions.
        
        This operation is available only if your account is on the E2 version of the platform."""

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/customer-managed-keys')
        return [CustomerManagedKey.from_dict(v) for v in json]


class NetworksAPI:
    """These APIs manage network configurations for customer-managed VPCs (optional). Its ID is used when
    creating a new workspace if you use customer-managed VPCs."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               network_name: str,
               *,
               gcp_network_info: GcpNetworkInfo = None,
               security_group_ids: List[str] = None,
               subnet_ids: List[str] = None,
               vpc_endpoints: NetworkVpcEndpoints = None,
               vpc_id: str = None,
               **kwargs) -> Network:
        """Create network configuration.
        
        Creates a Databricks network configuration that represents an VPC and its resources. The VPC will be
        used for new Databricks clusters. This requires a pre-existing VPC and subnets."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateNetworkRequest(gcp_network_info=gcp_network_info,
                                           network_name=network_name,
                                           security_group_ids=security_group_ids,
                                           subnet_ids=subnet_ids,
                                           vpc_endpoints=vpc_endpoints,
                                           vpc_id=vpc_id)
        body = request.as_dict()

        json = self._api.do('POST', f'/api/2.0/accounts/{self._api.account_id}/networks', body=body)
        return Network.from_dict(json)

    def delete(self, network_id: str, **kwargs):
        """Delete a network configuration.
        
        Deletes a Databricks network configuration, which represents a cloud VPC and its resources. You cannot
        delete a network that is associated with a workspace.
        
        This operation is available only if your account is on the E2 version of the platform."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteNetworkRequest(network_id=network_id)

        self._api.do('DELETE', f'/api/2.0/accounts/{self._api.account_id}/networks/{request.network_id}')

    def get(self, network_id: str, **kwargs) -> Network:
        """Get a network configuration.
        
        Gets a Databricks network configuration, which represents a cloud VPC and its resources."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetNetworkRequest(network_id=network_id)

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/networks/{request.network_id}')
        return Network.from_dict(json)

    def list(self) -> Iterator[Network]:
        """Get all network configurations.
        
        Gets a list of all Databricks network configurations for an account, specified by ID.
        
        This operation is available only if your account is on the E2 version of the platform."""

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/networks')
        return [Network.from_dict(v) for v in json]


class PrivateAccessAPI:
    """These APIs manage private access settings for this account. A private access settings object specifies how
    your workspace is accessed using AWS PrivateLink. Each workspace that has any PrivateLink connections must
    include the ID for a private access settings object is in its workspace configuration object. Your account
    must be enabled for PrivateLink to use these APIs. Before configuring PrivateLink, it is important to read
    the [Databricks article about PrivateLink].
    
    [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               private_access_settings_name: str,
               region: str,
               private_access_settings_id: str,
               *,
               allowed_vpc_endpoint_ids: List[str] = None,
               private_access_level: PrivateAccessLevel = None,
               public_access_enabled: bool = None,
               **kwargs) -> PrivateAccessSettings:
        """Create private access settings.
        
        Creates a private access settings object, which specifies how your workspace is accessed over [AWS
        PrivateLink]. To use AWS PrivateLink, a workspace must have a private access settings object
        referenced by ID in the workspace's `private_access_settings_id` property.
        
        You can share one private access settings with multiple workspaces in a single account. However,
        private access settings are specific to AWS regions, so only workspaces in the same AWS region can use
        a given private access settings object.
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpsertPrivateAccessSettingsRequest(
                allowed_vpc_endpoint_ids=allowed_vpc_endpoint_ids,
                private_access_level=private_access_level,
                private_access_settings_id=private_access_settings_id,
                private_access_settings_name=private_access_settings_name,
                public_access_enabled=public_access_enabled,
                region=region)
        body = request.as_dict()

        json = self._api.do('POST',
                            f'/api/2.0/accounts/{self._api.account_id}/private-access-settings',
                            body=body)
        return PrivateAccessSettings.from_dict(json)

    def delete(self, private_access_settings_id: str, **kwargs):
        """Delete a private access settings object.
        
        Deletes a private access settings object, which determines how your workspace is accessed over [AWS
        PrivateLink].
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeletePrivateAccesRequest(private_access_settings_id=private_access_settings_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/private-access-settings/{request.private_access_settings_id}'
        )

    def get(self, private_access_settings_id: str, **kwargs) -> PrivateAccessSettings:
        """Get a private access settings object.
        
        Gets a private access settings object, which specifies how your workspace is accessed over [AWS
        PrivateLink].
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetPrivateAccesRequest(private_access_settings_id=private_access_settings_id)

        json = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/private-access-settings/{request.private_access_settings_id}'
        )
        return PrivateAccessSettings.from_dict(json)

    def list(self) -> Iterator[PrivateAccessSettings]:
        """Get all private access settings objects.
        
        Gets a list of all private access settings objects for an account, specified by ID."""

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/private-access-settings')
        return [PrivateAccessSettings.from_dict(v) for v in json]

    def replace(self,
                private_access_settings_name: str,
                region: str,
                private_access_settings_id: str,
                *,
                allowed_vpc_endpoint_ids: List[str] = None,
                private_access_level: PrivateAccessLevel = None,
                public_access_enabled: bool = None,
                **kwargs):
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
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpsertPrivateAccessSettingsRequest(
                allowed_vpc_endpoint_ids=allowed_vpc_endpoint_ids,
                private_access_level=private_access_level,
                private_access_settings_id=private_access_settings_id,
                private_access_settings_name=private_access_settings_name,
                public_access_enabled=public_access_enabled,
                region=region)
        body = request.as_dict()
        self._api.do(
            'PUT',
            f'/api/2.0/accounts/{self._api.account_id}/private-access-settings/{request.private_access_settings_id}',
            body=body)


class StorageAPI:
    """These APIs manage storage configurations for this workspace. A root storage S3 bucket in your account is
    required to store objects like cluster logs, notebook revisions, and job results. You can also use the
    root storage S3 bucket for storage of non-production DBFS data. A storage configuration encapsulates this
    bucket information, and its ID is used when creating a new workspace."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, storage_configuration_name: str, root_bucket_info: RootBucketInfo,
               **kwargs) -> StorageConfiguration:
        """Create new storage configuration.
        
        Creates new storage configuration for an account, specified by ID. Uploads a storage configuration
        object that represents the root AWS S3 bucket in your account. Databricks stores related workspace
        assets including DBFS, cluster logs, and job results. For the AWS S3 bucket, you need to configure the
        required bucket policy.
        
        For information about how to create a new workspace with this API, see [Create a new workspace using
        the Account API]
        
        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateStorageConfigurationRequest(root_bucket_info=root_bucket_info,
                                                        storage_configuration_name=storage_configuration_name)
        body = request.as_dict()

        json = self._api.do('POST',
                            f'/api/2.0/accounts/{self._api.account_id}/storage-configurations',
                            body=body)
        return StorageConfiguration.from_dict(json)

    def delete(self, storage_configuration_id: str, **kwargs):
        """Delete storage configuration.
        
        Deletes a Databricks storage configuration. You cannot delete a storage configuration that is
        associated with any workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteStorageRequest(storage_configuration_id=storage_configuration_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/storage-configurations/{request.storage_configuration_id}'
        )

    def get(self, storage_configuration_id: str, **kwargs) -> StorageConfiguration:
        """Get storage configuration.
        
        Gets a Databricks storage configuration for an account, both specified by ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetStorageRequest(storage_configuration_id=storage_configuration_id)

        json = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/storage-configurations/{request.storage_configuration_id}'
        )
        return StorageConfiguration.from_dict(json)

    def list(self) -> Iterator[StorageConfiguration]:
        """Get all storage configurations.
        
        Gets a list of all Databricks storage configurations for your account, specified by ID."""

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/storage-configurations')
        return [StorageConfiguration.from_dict(v) for v in json]


class VpcEndpointsAPI:
    """These APIs manage VPC endpoint configurations for this account. This object registers an AWS VPC endpoint
    in your Databricks account so your workspace can use it with AWS PrivateLink. Your VPC endpoint connects
    to one of two VPC endpoint services -- one for workspace (both for front-end connection and for back-end
    connection to REST APIs) and one for the back-end secure cluster connectivity relay from the data plane.
    Your account must be enabled for PrivateLink to use these APIs. Before configuring PrivateLink, it is
    important to read the [Databricks article about PrivateLink].
    
    [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, vpc_endpoint_name: str, aws_vpc_endpoint_id: str, region: str, **kwargs) -> VpcEndpoint:
        """Create VPC endpoint configuration.
        
        Creates a VPC endpoint configuration, which represents a [VPC endpoint] object in AWS used to
        communicate privately with Databricks over [AWS PrivateLink].
        
        After you create the VPC endpoint configuration, the Databricks [endpoint service] automatically
        accepts the VPC endpoint.
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        [VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html
        [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateVpcEndpointRequest(aws_vpc_endpoint_id=aws_vpc_endpoint_id,
                                               region=region,
                                               vpc_endpoint_name=vpc_endpoint_name)
        body = request.as_dict()

        json = self._api.do('POST', f'/api/2.0/accounts/{self._api.account_id}/vpc-endpoints', body=body)
        return VpcEndpoint.from_dict(json)

    def delete(self, vpc_endpoint_id: str, **kwargs):
        """Delete VPC endpoint configuration.
        
        Deletes a VPC endpoint configuration, which represents an [AWS VPC endpoint] that can communicate
        privately with Databricks over [AWS PrivateLink].
        
        Upon deleting a VPC endpoint configuration, the VPC endpoint in AWS changes its state from `accepted`
        to `rejected`, which means that it is no longer usable from your VPC.
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [AWS VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteVpcEndpointRequest(vpc_endpoint_id=vpc_endpoint_id)

        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/vpc-endpoints/{request.vpc_endpoint_id}')

    def get(self, vpc_endpoint_id: str, **kwargs) -> VpcEndpoint:
        """Get a VPC endpoint configuration.
        
        Gets a VPC endpoint configuration, which represents a [VPC endpoint] object in AWS used to communicate
        privately with Databricks over [AWS PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetVpcEndpointRequest(vpc_endpoint_id=vpc_endpoint_id)

        json = self._api.do(
            'GET', f'/api/2.0/accounts/{self._api.account_id}/vpc-endpoints/{request.vpc_endpoint_id}')
        return VpcEndpoint.from_dict(json)

    def list(self) -> Iterator[VpcEndpoint]:
        """Get all VPC endpoint configurations.
        
        Gets a list of all VPC endpoints for an account, specified by ID.
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"""

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/vpc-endpoints')
        return [VpcEndpoint.from_dict(v) for v in json]


class WorkspacesAPI:
    """These APIs manage workspaces for this account. A Databricks workspace is an environment for accessing all
    of your Databricks assets. The workspace organizes objects (notebooks, libraries, and experiments) into
    folders, and provides access to data and computational resources such as clusters and jobs.
    
    These endpoints are available if your account is on the E2 version of the platform or on a select custom
    plan that allows multiple workspaces per account."""

    def __init__(self, api_client):
        self._api = api_client

    def wait_get_workspace_running(self, workspace_id: int, timeout=timedelta(minutes=20)) -> Workspace:
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
               aws_region: str = None,
               cloud: str = None,
               cloud_resource_container: CloudResourceContainer = None,
               credentials_id: str = None,
               deployment_name: str = None,
               location: str = None,
               managed_services_customer_managed_key_id: str = None,
               network_id: str = None,
               pricing_tier: PricingTier = None,
               private_access_settings_id: str = None,
               storage_configuration_id: str = None,
               storage_customer_managed_key_id: str = None,
               **kwargs) -> Wait[Workspace]:
        """Create a new workspace.
        
        Creates a new workspace.
        
        **Important**: This operation is asynchronous. A response with HTTP status code 200 means the request
        has been accepted and is in progress, but does not mean that the workspace deployed successfully and
        is running. The initial workspace status is typically `PROVISIONING`. Use the workspace ID
        (`workspace_id`) field in the response to identify the new workspace and make repeated `GET` requests
        with the workspace ID and check its status. The workspace becomes available when the status changes to
        `RUNNING`."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateWorkspaceRequest(
                aws_region=aws_region,
                cloud=cloud,
                cloud_resource_container=cloud_resource_container,
                credentials_id=credentials_id,
                deployment_name=deployment_name,
                location=location,
                managed_services_customer_managed_key_id=managed_services_customer_managed_key_id,
                network_id=network_id,
                pricing_tier=pricing_tier,
                private_access_settings_id=private_access_settings_id,
                storage_configuration_id=storage_configuration_id,
                storage_customer_managed_key_id=storage_customer_managed_key_id,
                workspace_name=workspace_name)
        body = request.as_dict()
        op_response = self._api.do('POST', f'/api/2.0/accounts/{self._api.account_id}/workspaces', body=body)
        return Wait(self.wait_get_workspace_running, workspace_id=op_response['workspace_id'])

    def create_and_wait(
        self,
        workspace_name: str,
        *,
        aws_region: str = None,
        cloud: str = None,
        cloud_resource_container: CloudResourceContainer = None,
        credentials_id: str = None,
        deployment_name: str = None,
        location: str = None,
        managed_services_customer_managed_key_id: str = None,
        network_id: str = None,
        pricing_tier: PricingTier = None,
        private_access_settings_id: str = None,
        storage_configuration_id: str = None,
        storage_customer_managed_key_id: str = None,
        timeout=timedelta(minutes=20)) -> Workspace:
        return self.create(aws_region=aws_region,
                           cloud=cloud,
                           cloud_resource_container=cloud_resource_container,
                           credentials_id=credentials_id,
                           deployment_name=deployment_name,
                           location=location,
                           managed_services_customer_managed_key_id=managed_services_customer_managed_key_id,
                           network_id=network_id,
                           pricing_tier=pricing_tier,
                           private_access_settings_id=private_access_settings_id,
                           storage_configuration_id=storage_configuration_id,
                           storage_customer_managed_key_id=storage_customer_managed_key_id,
                           workspace_name=workspace_name).result(timeout=timeout)

    def delete(self, workspace_id: int, **kwargs):
        """Delete a workspace.
        
        Terminates and deletes a Databricks workspace. From an API perspective, deletion is immediate.
        However, it might take a few minutes for all workspaces resources to be deleted, depending on the size
        and number of workspace resources.
        
        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteWorkspaceRequest(workspace_id=workspace_id)

        self._api.do('DELETE', f'/api/2.0/accounts/{self._api.account_id}/workspaces/{request.workspace_id}')

    def get(self, workspace_id: int, **kwargs) -> Workspace:
        """Get a workspace.
        
        Gets information including status for a Databricks workspace, specified by ID. In the response, the
        `workspace_status` field indicates the current status. After initial workspace creation (which is
        asynchronous), make repeated `GET` requests with the workspace ID and check its status. The workspace
        becomes available when the status changes to `RUNNING`.
        
        For information about how to create a new workspace with this API **including error handling**, see
        [Create a new workspace using the Account API].
        
        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account.
        
        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetWorkspaceRequest(workspace_id=workspace_id)

        json = self._api.do('GET',
                            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{request.workspace_id}')
        return Workspace.from_dict(json)

    def list(self) -> Iterator[Workspace]:
        """Get all workspaces.
        
        Gets a list of all workspaces associated with an account, specified by ID.
        
        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account."""

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/workspaces')
        return [Workspace.from_dict(v) for v in json]

    def update(self,
               workspace_id: int,
               *,
               aws_region: str = None,
               credentials_id: str = None,
               managed_services_customer_managed_key_id: str = None,
               network_id: str = None,
               storage_configuration_id: str = None,
               storage_customer_managed_key_id: str = None,
               **kwargs) -> Wait[Workspace]:
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
        support on a workspace.
        
        After calling the `PATCH` operation to update the workspace configuration, make repeated `GET`
        requests with the workspace ID and check the workspace status. The workspace is successful if the
        status changes to `RUNNING`.
        
        For information about how to create a new workspace with this API **including error handling**, see
        [Create a new workspace using the Account API].
        
        ### Update a running workspace You can update a Databricks workspace configuration for running
        workspaces for some fields, but not all fields. For a running workspace, this request supports
        updating the following fields only: - Credential configuration ID
        
        - Network configuration ID. Used only if you already use a customer-managed VPC. You cannot convert a
        running workspace from a Databricks-managed VPC to a customer-managed VPC. You can use a network
        configuration update in this API for a failed or running workspace to add support for PrivateLink,
        although you also need to add a private access settings object.
        
        - Key configuration ID for managed services (control plane storage, such as notebook source and
        Databricks SQL queries). Databricks does not directly encrypt the data with the customer-managed key
        (CMK). Databricks uses both the CMK and the Databricks managed key (DMK) that is unique to your
        workspace to encrypt the Data Encryption Key (DEK). Databricks uses the DEK to encrypt your
        workspace's managed services persisted data. If the workspace does not already have a CMK for managed
        services, adding this ID enables managed services encryption for new or updated data. Existing managed
        services data that existed before adding the key remains not encrypted with the DEK until it is
        modified. If the workspace already has customer-managed keys for managed services, this request
        rotates (changes) the CMK keys and the DEK is re-encrypted with the DMK and the new CMK. - Key
        configuration ID for workspace storage (root S3 bucket and, optionally, EBS volumes). You can set this
        only if the workspace does not already have a customer-managed key configuration for workspace
        storage. - Private access settings ID to add PrivateLink support. You can add or update the private
        access settings ID to upgrade a workspace to add support for front-end, back-end, or both types of
        connectivity. You cannot remove (downgrade) any existing front-end or back-end PrivateLink support on
        a workspace.
        
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
        cause other unexpected behavior.
        
        * For workspaces with a customer-managed VPC, the workspace status stays at status `RUNNING` and the
        VPC change happens immediately. A change to the storage customer-managed key configuration ID might
        take a few minutes to update, so continue to check the workspace until you observe that it has been
        updated. If the update fails, the workspace might revert silently to its original configuration. After
        the workspace has been updated, you cannot use or create clusters for another 20 minutes. If you
        create or use clusters before this time interval elapses, clusters do not launch successfully, fail,
        or could cause other unexpected behavior.
        
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
        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateWorkspaceRequest(
                aws_region=aws_region,
                credentials_id=credentials_id,
                managed_services_customer_managed_key_id=managed_services_customer_managed_key_id,
                network_id=network_id,
                storage_configuration_id=storage_configuration_id,
                storage_customer_managed_key_id=storage_customer_managed_key_id,
                workspace_id=workspace_id)
        body = request.as_dict()
        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/workspaces/{request.workspace_id}',
                     body=body)
        return Wait(self.wait_get_workspace_running, workspace_id=request.workspace_id)

    def update_and_wait(
        self,
        workspace_id: int,
        *,
        aws_region: str = None,
        credentials_id: str = None,
        managed_services_customer_managed_key_id: str = None,
        network_id: str = None,
        storage_configuration_id: str = None,
        storage_customer_managed_key_id: str = None,
        timeout=timedelta(minutes=20)) -> Workspace:
        return self.update(aws_region=aws_region,
                           credentials_id=credentials_id,
                           managed_services_customer_managed_key_id=managed_services_customer_managed_key_id,
                           network_id=network_id,
                           storage_configuration_id=storage_configuration_id,
                           storage_customer_managed_key_id=storage_customer_managed_key_id,
                           workspace_id=workspace_id).result(timeout=timeout)

# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.
# ruff: noqa: F811, F841
# F401 is intentionally NOT covered: `make fmt` uses `ruff check --fix-only`
# to strip the fat-import header below; ignoring F401 would defeat that.

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any, Iterator, Optional

from google.protobuf.timestamp_pb2 import Timestamp

import logging
import uuid

from databricks.sdk.service._internal import (
    _enum,
    _from_dict,
    _repeated_dict,
    _timestamp,
)
from databricks.sdk.common.types.fieldmask import FieldMask
from databricks.sdk.common import lro
from databricks.sdk.retries import RetryError, poll


_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class AwsVpcEndpointInfo:
    aws_vpc_endpoint_id: str
    """The ID of the underlying VPC endpoint in AWS. Provided by the customer when registering an
    existing AWS VPC endpoint."""

    aws_account_id: Optional[str] = None
    """The AWS account ID in which this VPC endpoint lives."""

    aws_endpoint_service_id: Optional[str] = None
    """The ID of the Databricks VPC endpoint service that this endpoint connects to."""

    def as_dict(self) -> dict:
        """Serializes the AwsVpcEndpointInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_account_id is not None:
            body["aws_account_id"] = self.aws_account_id
        if self.aws_endpoint_service_id is not None:
            body["aws_endpoint_service_id"] = self.aws_endpoint_service_id
        if self.aws_vpc_endpoint_id is not None:
            body["aws_vpc_endpoint_id"] = self.aws_vpc_endpoint_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AwsVpcEndpointInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.aws_account_id is not None:
            body["aws_account_id"] = self.aws_account_id
        if self.aws_endpoint_service_id is not None:
            body["aws_endpoint_service_id"] = self.aws_endpoint_service_id
        if self.aws_vpc_endpoint_id is not None:
            body["aws_vpc_endpoint_id"] = self.aws_vpc_endpoint_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AwsVpcEndpointInfo:
        """Deserializes the AwsVpcEndpointInfo from a dictionary."""
        return cls(
            aws_account_id=d.get("aws_account_id", None),
            aws_endpoint_service_id=d.get("aws_endpoint_service_id", None),
            aws_vpc_endpoint_id=d.get("aws_vpc_endpoint_id", None),
        )


@dataclass
class AzurePrivateEndpointInfo:
    private_endpoint_name: str
    """The name of the Private Endpoint in the Azure subscription."""

    private_endpoint_resource_guid: str
    """The GUID of the Private Endpoint resource in the Azure subscription. This is assigned by Azure
    when the user sets up the Private Endpoint."""

    private_endpoint_resource_id: Optional[str] = None
    """The full resource ID of the Private Endpoint."""

    private_link_service_id: Optional[str] = None
    """The resource ID of the Databricks Private Link Service that this Private Endpoint connects to."""

    def as_dict(self) -> dict:
        """Serializes the AzurePrivateEndpointInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.private_endpoint_name is not None:
            body["private_endpoint_name"] = self.private_endpoint_name
        if self.private_endpoint_resource_guid is not None:
            body["private_endpoint_resource_guid"] = self.private_endpoint_resource_guid
        if self.private_endpoint_resource_id is not None:
            body["private_endpoint_resource_id"] = self.private_endpoint_resource_id
        if self.private_link_service_id is not None:
            body["private_link_service_id"] = self.private_link_service_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AzurePrivateEndpointInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.private_endpoint_name is not None:
            body["private_endpoint_name"] = self.private_endpoint_name
        if self.private_endpoint_resource_guid is not None:
            body["private_endpoint_resource_guid"] = self.private_endpoint_resource_guid
        if self.private_endpoint_resource_id is not None:
            body["private_endpoint_resource_id"] = self.private_endpoint_resource_id
        if self.private_link_service_id is not None:
            body["private_link_service_id"] = self.private_link_service_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AzurePrivateEndpointInfo:
        """Deserializes the AzurePrivateEndpointInfo from a dictionary."""
        return cls(
            private_endpoint_name=d.get("private_endpoint_name", None),
            private_endpoint_resource_guid=d.get("private_endpoint_resource_guid", None),
            private_endpoint_resource_id=d.get("private_endpoint_resource_id", None),
            private_link_service_id=d.get("private_link_service_id", None),
        )


@dataclass
class DatabricksServiceExceptionWithDetailsProto:
    """Databricks Error that is returned by all Databricks APIs."""

    details: Optional[List[dict]] = None

    error_code: Optional[ErrorCode] = None

    message: Optional[str] = None

    stack_trace: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the DatabricksServiceExceptionWithDetailsProto into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.details:
            body["details"] = [v for v in self.details]
        if self.error_code is not None:
            body["error_code"] = self.error_code.value
        if self.message is not None:
            body["message"] = self.message
        if self.stack_trace is not None:
            body["stack_trace"] = self.stack_trace
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabricksServiceExceptionWithDetailsProto into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.details:
            body["details"] = self.details
        if self.error_code is not None:
            body["error_code"] = self.error_code
        if self.message is not None:
            body["message"] = self.message
        if self.stack_trace is not None:
            body["stack_trace"] = self.stack_trace
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabricksServiceExceptionWithDetailsProto:
        """Deserializes the DatabricksServiceExceptionWithDetailsProto from a dictionary."""
        return cls(
            details=d.get("details", None),
            error_code=_enum(d, "error_code", ErrorCode),
            message=d.get("message", None),
            stack_trace=d.get("stack_trace", None),
        )


@dataclass
class Endpoint:
    """Endpoint represents a cloud networking resource in a user's cloud account and binds it to the
    Databricks account."""

    display_name: str
    """The human-readable display name of this endpoint. The input should conform to RFC-1034, which
    restricts to letters, numbers, and hyphens, with the first character a letter, the last a letter
    or a number, and a 63 character maximum."""

    region: str
    """The cloud provider region where this endpoint is located."""

    account_id: Optional[str] = None
    """The Databricks Account in which the endpoint object exists."""

    aws_vpc_endpoint_info: Optional[AwsVpcEndpointInfo] = None
    """Info for an AWS VPC endpoint."""

    azure_private_endpoint_info: Optional[AzurePrivateEndpointInfo] = None
    """Info for an Azure private endpoint."""

    create_time: Optional[Timestamp] = None
    """The timestamp when the endpoint was created. The timestamp is in RFC 3339 format in UTC
    timezone."""

    endpoint_id: Optional[str] = None
    """The unique identifier for this endpoint under the account. This field is a UUID generated by
    Databricks."""

    gcp_psc_endpoint_info: Optional[GcpPscEndpointInfo] = None
    """Info for a GCP Private Service Connect endpoint."""

    name: Optional[str] = None
    """The resource name of the endpoint, which uniquely identifies the endpoint."""

    state: Optional[EndpointState] = None
    """The state of the endpoint. The endpoint can only be used if the state is ``APPROVED``."""

    use_case: Optional[EndpointUseCase] = None
    """The use case that determines the type of network connectivity this endpoint provides. This field
    is automatically determined based on the endpoint configuration and cloud-specific settings."""

    def as_dict(self) -> dict:
        """Serializes the Endpoint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.aws_vpc_endpoint_info:
            body["aws_vpc_endpoint_info"] = self.aws_vpc_endpoint_info.as_dict()
        if self.azure_private_endpoint_info:
            body["azure_private_endpoint_info"] = self.azure_private_endpoint_info.as_dict()
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.endpoint_id is not None:
            body["endpoint_id"] = self.endpoint_id
        if self.gcp_psc_endpoint_info:
            body["gcp_psc_endpoint_info"] = self.gcp_psc_endpoint_info.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.region is not None:
            body["region"] = self.region
        if self.state is not None:
            body["state"] = self.state.value
        if self.use_case is not None:
            body["use_case"] = self.use_case.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Endpoint into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.aws_vpc_endpoint_info:
            body["aws_vpc_endpoint_info"] = self.aws_vpc_endpoint_info
        if self.azure_private_endpoint_info:
            body["azure_private_endpoint_info"] = self.azure_private_endpoint_info
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.endpoint_id is not None:
            body["endpoint_id"] = self.endpoint_id
        if self.gcp_psc_endpoint_info:
            body["gcp_psc_endpoint_info"] = self.gcp_psc_endpoint_info
        if self.name is not None:
            body["name"] = self.name
        if self.region is not None:
            body["region"] = self.region
        if self.state is not None:
            body["state"] = self.state
        if self.use_case is not None:
            body["use_case"] = self.use_case
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Endpoint:
        """Deserializes the Endpoint from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            aws_vpc_endpoint_info=_from_dict(d, "aws_vpc_endpoint_info", AwsVpcEndpointInfo),
            azure_private_endpoint_info=_from_dict(d, "azure_private_endpoint_info", AzurePrivateEndpointInfo),
            create_time=_timestamp(d, "create_time"),
            display_name=d.get("display_name", None),
            endpoint_id=d.get("endpoint_id", None),
            gcp_psc_endpoint_info=_from_dict(d, "gcp_psc_endpoint_info", GcpPscEndpointInfo),
            name=d.get("name", None),
            region=d.get("region", None),
            state=_enum(d, "state", EndpointState),
            use_case=_enum(d, "use_case", EndpointUseCase),
        )


class EndpointState(Enum):
    APPROVED = "APPROVED"
    DISCONNECTED = "DISCONNECTED"
    FAILED = "FAILED"
    PENDING = "PENDING"


class EndpointUseCase(Enum):
    SERVICE_DIRECT = "SERVICE_DIRECT"


class ErrorCode(Enum):
    """Error codes returned by Databricks APIs to indicate specific failure conditions."""

    ABORTED = "ABORTED"
    ALREADY_EXISTS = "ALREADY_EXISTS"
    BAD_REQUEST = "BAD_REQUEST"
    CANCELLED = "CANCELLED"
    CATALOG_ALREADY_EXISTS = "CATALOG_ALREADY_EXISTS"
    CATALOG_DOES_NOT_EXIST = "CATALOG_DOES_NOT_EXIST"
    CATALOG_NOT_EMPTY = "CATALOG_NOT_EMPTY"
    COULD_NOT_ACQUIRE_LOCK = "COULD_NOT_ACQUIRE_LOCK"
    CUSTOMER_UNAUTHORIZED = "CUSTOMER_UNAUTHORIZED"
    DAC_ALREADY_EXISTS = "DAC_ALREADY_EXISTS"
    DAC_DOES_NOT_EXIST = "DAC_DOES_NOT_EXIST"
    DATA_LOSS = "DATA_LOSS"
    DEADLINE_EXCEEDED = "DEADLINE_EXCEEDED"
    DEPLOYMENT_TIMEOUT = "DEPLOYMENT_TIMEOUT"
    DIRECTORY_NOT_EMPTY = "DIRECTORY_NOT_EMPTY"
    DIRECTORY_PROTECTED = "DIRECTORY_PROTECTED"
    DRY_RUN_FAILED = "DRY_RUN_FAILED"
    ENDPOINT_NOT_FOUND = "ENDPOINT_NOT_FOUND"
    EXTERNAL_LOCATION_ALREADY_EXISTS = "EXTERNAL_LOCATION_ALREADY_EXISTS"
    EXTERNAL_LOCATION_DOES_NOT_EXIST = "EXTERNAL_LOCATION_DOES_NOT_EXIST"
    FEATURE_DISABLED = "FEATURE_DISABLED"
    GIT_CONFLICT = "GIT_CONFLICT"
    GIT_REMOTE_ERROR = "GIT_REMOTE_ERROR"
    GIT_SENSITIVE_TOKEN_DETECTED = "GIT_SENSITIVE_TOKEN_DETECTED"
    GIT_UNKNOWN_REF = "GIT_UNKNOWN_REF"
    GIT_URL_NOT_ON_ALLOW_LIST = "GIT_URL_NOT_ON_ALLOW_LIST"
    INSECURE_PARTNER_RESPONSE = "INSECURE_PARTNER_RESPONSE"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_PARAMETER_VALUE = "INVALID_PARAMETER_VALUE"
    INVALID_STATE = "INVALID_STATE"
    INVALID_STATE_TRANSITION = "INVALID_STATE_TRANSITION"
    IO_ERROR = "IO_ERROR"
    IPYNB_FILE_IN_REPO = "IPYNB_FILE_IN_REPO"
    MALFORMED_PARTNER_RESPONSE = "MALFORMED_PARTNER_RESPONSE"
    MALFORMED_REQUEST = "MALFORMED_REQUEST"
    MANAGED_RESOURCE_GROUP_DOES_NOT_EXIST = "MANAGED_RESOURCE_GROUP_DOES_NOT_EXIST"
    MAX_BLOCK_SIZE_EXCEEDED = "MAX_BLOCK_SIZE_EXCEEDED"
    MAX_CHILD_NODE_SIZE_EXCEEDED = "MAX_CHILD_NODE_SIZE_EXCEEDED"
    MAX_LIST_SIZE_EXCEEDED = "MAX_LIST_SIZE_EXCEEDED"
    MAX_NOTEBOOK_SIZE_EXCEEDED = "MAX_NOTEBOOK_SIZE_EXCEEDED"
    MAX_READ_SIZE_EXCEEDED = "MAX_READ_SIZE_EXCEEDED"
    METASTORE_ALREADY_EXISTS = "METASTORE_ALREADY_EXISTS"
    METASTORE_DOES_NOT_EXIST = "METASTORE_DOES_NOT_EXIST"
    METASTORE_NOT_EMPTY = "METASTORE_NOT_EMPTY"
    NOT_FOUND = "NOT_FOUND"
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    PARTIAL_DELETE = "PARTIAL_DELETE"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    PERMISSION_NOT_PROPAGATED = "PERMISSION_NOT_PROPAGATED"
    PRINCIPAL_DOES_NOT_EXIST = "PRINCIPAL_DOES_NOT_EXIST"
    PROJECTS_OPERATION_TIMEOUT = "PROJECTS_OPERATION_TIMEOUT"
    PROVIDER_ALREADY_EXISTS = "PROVIDER_ALREADY_EXISTS"
    PROVIDER_DOES_NOT_EXIST = "PROVIDER_DOES_NOT_EXIST"
    PROVIDER_SHARE_NOT_ACCESSIBLE = "PROVIDER_SHARE_NOT_ACCESSIBLE"
    QUOTA_EXCEEDED = "QUOTA_EXCEEDED"
    RECIPIENT_ALREADY_EXISTS = "RECIPIENT_ALREADY_EXISTS"
    RECIPIENT_DOES_NOT_EXIST = "RECIPIENT_DOES_NOT_EXIST"
    REQUEST_LIMIT_EXCEEDED = "REQUEST_LIMIT_EXCEEDED"
    RESOURCE_ALREADY_EXISTS = "RESOURCE_ALREADY_EXISTS"
    RESOURCE_CONFLICT = "RESOURCE_CONFLICT"
    RESOURCE_DOES_NOT_EXIST = "RESOURCE_DOES_NOT_EXIST"
    RESOURCE_EXHAUSTED = "RESOURCE_EXHAUSTED"
    RESOURCE_LIMIT_EXCEEDED = "RESOURCE_LIMIT_EXCEEDED"
    SCHEMA_ALREADY_EXISTS = "SCHEMA_ALREADY_EXISTS"
    SCHEMA_DOES_NOT_EXIST = "SCHEMA_DOES_NOT_EXIST"
    SCHEMA_NOT_EMPTY = "SCHEMA_NOT_EMPTY"
    SEARCH_QUERY_TOO_LONG = "SEARCH_QUERY_TOO_LONG"
    SEARCH_QUERY_TOO_SHORT = "SEARCH_QUERY_TOO_SHORT"
    SERVICE_UNDER_MAINTENANCE = "SERVICE_UNDER_MAINTENANCE"
    SHARE_ALREADY_EXISTS = "SHARE_ALREADY_EXISTS"
    SHARE_DOES_NOT_EXIST = "SHARE_DOES_NOT_EXIST"
    STORAGE_CREDENTIAL_ALREADY_EXISTS = "STORAGE_CREDENTIAL_ALREADY_EXISTS"
    STORAGE_CREDENTIAL_DOES_NOT_EXIST = "STORAGE_CREDENTIAL_DOES_NOT_EXIST"
    TABLE_ALREADY_EXISTS = "TABLE_ALREADY_EXISTS"
    TABLE_DOES_NOT_EXIST = "TABLE_DOES_NOT_EXIST"
    TEMPORARILY_UNAVAILABLE = "TEMPORARILY_UNAVAILABLE"
    UNAUTHENTICATED = "UNAUTHENTICATED"
    UNAVAILABLE = "UNAVAILABLE"
    UNKNOWN = "UNKNOWN"
    UNPARSEABLE_HTTP_ERROR = "UNPARSEABLE_HTTP_ERROR"
    WORKSPACE_TEMPORARILY_UNAVAILABLE = "WORKSPACE_TEMPORARILY_UNAVAILABLE"


@dataclass
class GcpPscEndpointInfo:
    project_id: str
    """The GCP consumer project ID in which this PSC endpoint is created. Provided by the customer when
    registering an existing PSC endpoint."""

    psc_endpoint: str
    """The name of this PSC connection in the GCP consumer project. Provided by the customer when
    registering an existing PSC endpoint."""

    endpoint_region: str
    """The GCP region of the PSC connection endpoint. Provided by the customer when registering an
    existing PSC endpoint. GCP supports only same-region PSC, so this must match the workspace
    region."""

    psc_connection_id: Optional[str] = None
    """The ID of the underlying Private Service Connect connection in the GCP consumer project,
    assigned by GCP when the PSC connection is created."""

    service_attachment_id: Optional[str] = None
    """The ID of the Databricks service attachment this PSC endpoint connects to."""

    def as_dict(self) -> dict:
        """Serializes the GcpPscEndpointInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.endpoint_region is not None:
            body["endpoint_region"] = self.endpoint_region
        if self.project_id is not None:
            body["project_id"] = self.project_id
        if self.psc_connection_id is not None:
            body["psc_connection_id"] = self.psc_connection_id
        if self.psc_endpoint is not None:
            body["psc_endpoint"] = self.psc_endpoint
        if self.service_attachment_id is not None:
            body["service_attachment_id"] = self.service_attachment_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GcpPscEndpointInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.endpoint_region is not None:
            body["endpoint_region"] = self.endpoint_region
        if self.project_id is not None:
            body["project_id"] = self.project_id
        if self.psc_connection_id is not None:
            body["psc_connection_id"] = self.psc_connection_id
        if self.psc_endpoint is not None:
            body["psc_endpoint"] = self.psc_endpoint
        if self.service_attachment_id is not None:
            body["service_attachment_id"] = self.service_attachment_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GcpPscEndpointInfo:
        """Deserializes the GcpPscEndpointInfo from a dictionary."""
        return cls(
            endpoint_region=d.get("endpoint_region", None),
            project_id=d.get("project_id", None),
            psc_connection_id=d.get("psc_connection_id", None),
            psc_endpoint=d.get("psc_endpoint", None),
            service_attachment_id=d.get("service_attachment_id", None),
        )


@dataclass
class ListEndpointsResponse:
    items: Optional[List[Endpoint]] = None

    next_page_token: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the ListEndpointsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.items:
            body["items"] = [v.as_dict() for v in self.items]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListEndpointsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.items:
            body["items"] = self.items
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListEndpointsResponse:
        """Deserializes the ListEndpointsResponse from a dictionary."""
        return cls(items=_repeated_dict(d, "items", Endpoint), next_page_token=d.get("next_page_token", None))


@dataclass
class ListPrivateNetworkGatewaysResponse:
    next_page_token: Optional[str] = None
    """An opaque token for the next page, or empty when there are no more results."""

    private_network_gateways: Optional[List[PrivateNetworkGateway]] = None

    def as_dict(self) -> dict:
        """Serializes the ListPrivateNetworkGatewaysResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.private_network_gateways:
            body["private_network_gateways"] = [v.as_dict() for v in self.private_network_gateways]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListPrivateNetworkGatewaysResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.private_network_gateways:
            body["private_network_gateways"] = self.private_network_gateways
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListPrivateNetworkGatewaysResponse:
        """Deserializes the ListPrivateNetworkGatewaysResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            private_network_gateways=_repeated_dict(d, "private_network_gateways", PrivateNetworkGateway),
        )


@dataclass
class Operation:
    """This resource represents a long-running operation that is the result of a network API call."""

    done: Optional[bool] = None
    """If the value is ``false``, it means the operation is still in progress. If ``true``, the
    operation is completed, and either ``error`` or ``response`` is available."""

    error: Optional[DatabricksServiceExceptionWithDetailsProto] = None
    """The error result of the operation in case of failure or cancellation."""

    metadata: Optional[dict] = None
    """Service-specific metadata associated with the operation. It typically contains progress
    information and common metadata such as create time. Some services might not provide such
    metadata."""

    name: Optional[str] = None
    """The server-assigned name, which is only unique within the same service that originally returns
    it. If you use the default HTTP mapping, the ``name`` should be a resource name ending with
    ``operations/{unique_id}``."""

    response: Optional[dict] = None
    """The normal, successful response of the operation."""

    def as_dict(self) -> dict:
        """Serializes the Operation into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.done is not None:
            body["done"] = self.done
        if self.error:
            body["error"] = self.error.as_dict()
        if self.metadata:
            body["metadata"] = self.metadata
        if self.name is not None:
            body["name"] = self.name
        if self.response:
            body["response"] = self.response
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Operation into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.done is not None:
            body["done"] = self.done
        if self.error:
            body["error"] = self.error
        if self.metadata:
            body["metadata"] = self.metadata
        if self.name is not None:
            body["name"] = self.name
        if self.response:
            body["response"] = self.response
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Operation:
        """Deserializes the Operation from a dictionary."""
        return cls(
            done=d.get("done", None),
            error=_from_dict(d, "error", DatabricksServiceExceptionWithDetailsProto),
            metadata=d.get("metadata", None),
            name=d.get("name", None),
            response=d.get("response", None),
        )


@dataclass
class PrivateNetworkGateway:
    """A private network gateway connects serverless compute to destinations in a customer-managed VPC
    or VNet."""

    display_name: str
    """The human-readable name of the gateway."""

    traffic_mode: PrivateNetworkGatewayTrafficMode
    """The traffic routed through this gateway."""

    aws_cloud_connection: Optional[PrivateNetworkGatewayAwsCloudConnection] = None
    """The AWS connection used by the gateway."""

    azure_cloud_connection: Optional[PrivateNetworkGatewayAzureCloudConnection] = None
    """The Azure connection used by the gateway."""

    bandwidth_tier_gigabits_per_second: Optional[int] = None
    """The provisioned bandwidth tier for an Azure gateway, in gigabits per second. Required when
    creating an Azure gateway."""

    create_time: Optional[Timestamp] = None
    """The time when the gateway was created."""

    destinations: Optional[List[PrivateNetworkGatewayDestination]] = None
    """The destinations routed through this gateway."""

    error_message: Optional[str] = None
    """The failure reason when the gateway is in the FAILED state."""

    name: Optional[str] = None
    """The canonical resource name of the gateway, in the form
    ``accounts/{account_id}/network-connectivity-configs/{ncc_id}/private-network-gateways/{gateway_id}``."""

    private_dns_resolvers: Optional[List[PrivateNetworkGatewayPrivateDnsResolver]] = None
    """The DNS resolvers used for private name resolution."""

    state: Optional[PrivateNetworkGatewayGatewayState] = None
    """The current lifecycle state of the gateway."""

    update_time: Optional[Timestamp] = None
    """The time when the gateway was last updated."""

    def as_dict(self) -> dict:
        """Serializes the PrivateNetworkGateway into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_cloud_connection:
            body["aws_cloud_connection"] = self.aws_cloud_connection.as_dict()
        if self.azure_cloud_connection:
            body["azure_cloud_connection"] = self.azure_cloud_connection.as_dict()
        if self.bandwidth_tier_gigabits_per_second is not None:
            body["bandwidth_tier_gigabits_per_second"] = self.bandwidth_tier_gigabits_per_second
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.destinations:
            body["destinations"] = [v.as_dict() for v in self.destinations]
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.error_message is not None:
            body["error_message"] = self.error_message
        if self.name is not None:
            body["name"] = self.name
        if self.private_dns_resolvers:
            body["private_dns_resolvers"] = [v.as_dict() for v in self.private_dns_resolvers]
        if self.state is not None:
            body["state"] = self.state.value
        if self.traffic_mode is not None:
            body["traffic_mode"] = self.traffic_mode.value
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PrivateNetworkGateway into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.aws_cloud_connection:
            body["aws_cloud_connection"] = self.aws_cloud_connection
        if self.azure_cloud_connection:
            body["azure_cloud_connection"] = self.azure_cloud_connection
        if self.bandwidth_tier_gigabits_per_second is not None:
            body["bandwidth_tier_gigabits_per_second"] = self.bandwidth_tier_gigabits_per_second
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.destinations:
            body["destinations"] = self.destinations
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.error_message is not None:
            body["error_message"] = self.error_message
        if self.name is not None:
            body["name"] = self.name
        if self.private_dns_resolvers:
            body["private_dns_resolvers"] = self.private_dns_resolvers
        if self.state is not None:
            body["state"] = self.state
        if self.traffic_mode is not None:
            body["traffic_mode"] = self.traffic_mode
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PrivateNetworkGateway:
        """Deserializes the PrivateNetworkGateway from a dictionary."""
        return cls(
            aws_cloud_connection=_from_dict(d, "aws_cloud_connection", PrivateNetworkGatewayAwsCloudConnection),
            azure_cloud_connection=_from_dict(d, "azure_cloud_connection", PrivateNetworkGatewayAzureCloudConnection),
            bandwidth_tier_gigabits_per_second=d.get("bandwidth_tier_gigabits_per_second", None),
            create_time=_timestamp(d, "create_time"),
            destinations=_repeated_dict(d, "destinations", PrivateNetworkGatewayDestination),
            display_name=d.get("display_name", None),
            error_message=d.get("error_message", None),
            name=d.get("name", None),
            private_dns_resolvers=_repeated_dict(d, "private_dns_resolvers", PrivateNetworkGatewayPrivateDnsResolver),
            state=_enum(d, "state", PrivateNetworkGatewayGatewayState),
            traffic_mode=_enum(d, "traffic_mode", PrivateNetworkGatewayTrafficMode),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class PrivateNetworkGatewayAwsCloudConnection:
    """AWS connection configuration."""

    gateway_subnets: List[PrivateNetworkGatewayAwsCloudConnectionAwsGatewaySubnet]
    """The subnets where the gateway establishes connectivity."""

    cross_account_role: PrivateNetworkGatewayAwsCloudConnectionCrossAccountRole
    """The IAM role that Databricks assumes to manage gateway resources."""

    security_group_ids: List[str]
    """The security groups attached to the gateway network interface."""

    def as_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayAwsCloudConnection into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.cross_account_role:
            body["cross_account_role"] = self.cross_account_role.as_dict()
        if self.gateway_subnets:
            body["gateway_subnets"] = [v.as_dict() for v in self.gateway_subnets]
        if self.security_group_ids:
            body["security_group_ids"] = [v for v in self.security_group_ids]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayAwsCloudConnection into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.cross_account_role:
            body["cross_account_role"] = self.cross_account_role
        if self.gateway_subnets:
            body["gateway_subnets"] = self.gateway_subnets
        if self.security_group_ids:
            body["security_group_ids"] = self.security_group_ids
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PrivateNetworkGatewayAwsCloudConnection:
        """Deserializes the PrivateNetworkGatewayAwsCloudConnection from a dictionary."""
        return cls(
            cross_account_role=_from_dict(
                d, "cross_account_role", PrivateNetworkGatewayAwsCloudConnectionCrossAccountRole
            ),
            gateway_subnets=_repeated_dict(
                d, "gateway_subnets", PrivateNetworkGatewayAwsCloudConnectionAwsGatewaySubnet
            ),
            security_group_ids=d.get("security_group_ids", None),
        )


@dataclass
class PrivateNetworkGatewayAwsCloudConnectionAwsGatewaySubnet:
    """An AWS subnet used by the gateway."""

    subnet_id: str
    """The AWS subnet ID."""

    def as_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayAwsCloudConnectionAwsGatewaySubnet into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.subnet_id is not None:
            body["subnet_id"] = self.subnet_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayAwsCloudConnectionAwsGatewaySubnet into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.subnet_id is not None:
            body["subnet_id"] = self.subnet_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PrivateNetworkGatewayAwsCloudConnectionAwsGatewaySubnet:
        """Deserializes the PrivateNetworkGatewayAwsCloudConnectionAwsGatewaySubnet from a dictionary."""
        return cls(subnet_id=d.get("subnet_id", None))


@dataclass
class PrivateNetworkGatewayAwsCloudConnectionCrossAccountRole:
    """A cross-account IAM role used to manage gateway resources."""

    role_arn: str
    """The ARN of the IAM role."""

    def as_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayAwsCloudConnectionCrossAccountRole into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.role_arn is not None:
            body["role_arn"] = self.role_arn
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayAwsCloudConnectionCrossAccountRole into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.role_arn is not None:
            body["role_arn"] = self.role_arn
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PrivateNetworkGatewayAwsCloudConnectionCrossAccountRole:
        """Deserializes the PrivateNetworkGatewayAwsCloudConnectionCrossAccountRole from a dictionary."""
        return cls(role_arn=d.get("role_arn", None))


@dataclass
class PrivateNetworkGatewayAzureCloudConnection:
    """Azure connection configuration."""

    gateway_subnet: PrivateNetworkGatewayAzureCloudConnectionAzureGatewaySubnet
    """The subnet where the gateway establishes connectivity."""

    def as_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayAzureCloudConnection into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.gateway_subnet:
            body["gateway_subnet"] = self.gateway_subnet.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayAzureCloudConnection into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.gateway_subnet:
            body["gateway_subnet"] = self.gateway_subnet
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PrivateNetworkGatewayAzureCloudConnection:
        """Deserializes the PrivateNetworkGatewayAzureCloudConnection from a dictionary."""
        return cls(
            gateway_subnet=_from_dict(d, "gateway_subnet", PrivateNetworkGatewayAzureCloudConnectionAzureGatewaySubnet)
        )


@dataclass
class PrivateNetworkGatewayAzureCloudConnectionAzureGatewaySubnet:
    """An Azure subnet used by the gateway."""

    resource_id: str
    """The full Azure resource ID of the subnet."""

    def as_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayAzureCloudConnectionAzureGatewaySubnet into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.resource_id is not None:
            body["resource_id"] = self.resource_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayAzureCloudConnectionAzureGatewaySubnet into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.resource_id is not None:
            body["resource_id"] = self.resource_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PrivateNetworkGatewayAzureCloudConnectionAzureGatewaySubnet:
        """Deserializes the PrivateNetworkGatewayAzureCloudConnectionAzureGatewaySubnet from a dictionary."""
        return cls(resource_id=d.get("resource_id", None))


@dataclass
class PrivateNetworkGatewayDestination:
    """A destination routed through the gateway."""

    destination_type: PrivateNetworkGatewayDestinationDestinationType
    """The destination type."""

    value: str
    """The destination value."""

    def as_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayDestination into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.destination_type is not None:
            body["destination_type"] = self.destination_type.value
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayDestination into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.destination_type is not None:
            body["destination_type"] = self.destination_type
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PrivateNetworkGatewayDestination:
        """Deserializes the PrivateNetworkGatewayDestination from a dictionary."""
        return cls(
            destination_type=_enum(d, "destination_type", PrivateNetworkGatewayDestinationDestinationType),
            value=d.get("value", None),
        )


class PrivateNetworkGatewayDestinationDestinationType(Enum):
    """The supported destination types."""

    DNS_NAME = "DNS_NAME"


class PrivateNetworkGatewayGatewayState(Enum):
    """The lifecycle state of the gateway."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    ESTABLISHED = "ESTABLISHED"
    FAILED = "FAILED"


@dataclass
class PrivateNetworkGatewayOperationMetadata:
    operation_type: Optional[PrivateNetworkGatewayOperationMetadataOperationType] = None
    """The operation performed on the gateway."""

    def as_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.operation_type is not None:
            body["operation_type"] = self.operation_type.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.operation_type is not None:
            body["operation_type"] = self.operation_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PrivateNetworkGatewayOperationMetadata:
        """Deserializes the PrivateNetworkGatewayOperationMetadata from a dictionary."""
        return cls(operation_type=_enum(d, "operation_type", PrivateNetworkGatewayOperationMetadataOperationType))


class PrivateNetworkGatewayOperationMetadataOperationType(Enum):
    CREATE = "CREATE"


@dataclass
class PrivateNetworkGatewayPrivateDnsResolver:
    """A private DNS resolver used by the gateway."""

    resolver_type: PrivateNetworkGatewayPrivateDnsResolverResolverType
    """The resolver type."""

    value: str
    """The resolver value."""

    def as_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayPrivateDnsResolver into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.resolver_type is not None:
            body["resolver_type"] = self.resolver_type.value
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PrivateNetworkGatewayPrivateDnsResolver into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.resolver_type is not None:
            body["resolver_type"] = self.resolver_type
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PrivateNetworkGatewayPrivateDnsResolver:
        """Deserializes the PrivateNetworkGatewayPrivateDnsResolver from a dictionary."""
        return cls(
            resolver_type=_enum(d, "resolver_type", PrivateNetworkGatewayPrivateDnsResolverResolverType),
            value=d.get("value", None),
        )


class PrivateNetworkGatewayPrivateDnsResolverResolverType(Enum):
    """The supported resolver types."""

    IP_ADDRESS = "IP_ADDRESS"


class PrivateNetworkGatewayTrafficMode(Enum):
    """The traffic routed through the gateway."""

    ALL_TRAFFIC = "ALL_TRAFFIC"
    SPECIFIC_DESTINATIONS = "SPECIFIC_DESTINATIONS"


class EndpointsAPI:
    """These APIs manage endpoint configurations for this account."""

    def __init__(self, api_client):
        self._api = api_client

    def create_endpoint(self, parent: str, endpoint: Endpoint) -> Endpoint:
        """Creates a new network connectivity endpoint that enables private connectivity between your network
        resources and Databricks services.

        After creation, the endpoint is initially in the PENDING state. The Databricks endpoint service
        automatically reviews and approves the endpoint within a few minutes. Use the GET method to retrieve
        the latest endpoint state.

        An endpoint can be used only after it reaches the APPROVED state.

        :param parent: str
          The parent resource name of the account under which the endpoint is created. Format:
          ``accounts/{account_id}``.
        :param endpoint: :class:`Endpoint`

        :returns: :class:`Endpoint`
        """

        body = endpoint.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/networking/v1/{parent}/endpoints", body=body, headers=headers)
        return Endpoint.from_dict(res)

    def delete_endpoint(self, name: str):
        """Deletes a network endpoint. This will remove the endpoint configuration from Databricks. Depending on
        the endpoint type and use case, you may also need to delete corresponding network resources in your
        cloud provider account.

        :param name: str


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/networking/v1/{name}", headers=headers)

    def get_endpoint(self, name: str) -> Endpoint:
        """Gets details of a specific network endpoint.

        :param name: str

        :returns: :class:`Endpoint`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/networking/v1/{name}", headers=headers)
        return Endpoint.from_dict(res)

    def list_endpoints(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Endpoint]:
        """Lists all network connectivity endpoints for the account.

        :param parent: str
          The parent resource name of the account to list endpoints for. Format: ``accounts/{account_id}``.
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Endpoint`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do("GET", f"/api/networking/v1/{parent}/endpoints", query=query, headers=headers)
            if "items" in json:
                for v in json["items"]:
                    yield Endpoint.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]


class PrivateNetworkGatewaysAPI:
    """These APIs manage private network gateways under network connectivity configurations."""

    def __init__(self, api_client):
        self._api = api_client

    def create_private_network_gateway(
        self, parent: str, private_network_gateway: PrivateNetworkGateway, *, request_id: Optional[str] = None
    ) -> CreatePrivateNetworkGatewayOperation:
        """Creates a private network gateway.

        :param parent: str
          The network connectivity configuration that will contain the gateway.
        :param private_network_gateway: :class:`PrivateNetworkGateway`
          The gateway to create.
        :param request_id: str (optional)
          A unique identifier for this request. The request is idempotent when this is provided.

        :returns: :class:`Operation`
        """

        if request_id is None or request_id == "":
            request_id = str(uuid.uuid4())
        body = private_network_gateway.as_dict()
        query = {}
        if request_id is not None:
            query["request_id"] = request_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST", f"/api/networking/v1/{parent}/private-network-gateways", query=query, body=body, headers=headers
        )
        operation = Operation.from_dict(res)
        return CreatePrivateNetworkGatewayOperation(self, operation)

    def delete_private_network_gateway(self, name: str):
        """Permanently deletes a private network gateway.

        :param name: str
          The canonical resource name of the gateway.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/networking/v1/{name}", headers=headers)

    def get_private_network_gateway(self, name: str) -> PrivateNetworkGateway:
        """Gets a private network gateway.

        :param name: str
          The canonical resource name of the gateway.

        :returns: :class:`PrivateNetworkGateway`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/networking/v1/{name}", headers=headers)
        return PrivateNetworkGateway.from_dict(res)

    def get_private_network_gateway_operation(self, name: str) -> Operation:
        """Gets the status of a private network gateway create operation.

        :param name: str
          The name of the operation resource.

        :returns: :class:`Operation`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/networking/v1/{name}", headers=headers)
        return Operation.from_dict(res)

    def list_private_network_gateways(
        self, parent: str, *, page_token: Optional[str] = None
    ) -> Iterator[PrivateNetworkGateway]:
        """Lists private network gateways under a network connectivity configuration.

        :param parent: str
          The network connectivity configuration containing the gateways.
        :param page_token: str (optional)
          An opaque token returned by a previous list request.

        :returns: Iterator over :class:`PrivateNetworkGateway`
        """

        query = {}
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do(
                "GET", f"/api/networking/v1/{parent}/private-network-gateways", query=query, headers=headers
            )
            if "private_network_gateways" in json:
                for v in json["private_network_gateways"]:
                    yield PrivateNetworkGateway.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def update_private_network_gateway(
        self, name: str, private_network_gateway: PrivateNetworkGateway, update_mask: FieldMask
    ) -> PrivateNetworkGateway:
        """Updates a private network gateway.

        :param name: str
          The canonical resource name of the gateway, in the form
          ``accounts/{account_id}/network-connectivity-configs/{ncc_id}/private-network-gateways/{gateway_id}``.
        :param private_network_gateway: :class:`PrivateNetworkGateway`
          The gateway containing the desired mutable field values.
        :param update_mask: FieldMask
          The fields to update.

        :returns: :class:`PrivateNetworkGateway`
        """

        body = private_network_gateway.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/networking/v1/{name}", query=query, body=body, headers=headers)
        return PrivateNetworkGateway.from_dict(res)


class CreatePrivateNetworkGatewayOperation:
    """Long-running operation for create_private_network_gateway"""

    def __init__(self, impl: PrivateNetworkGatewaysAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> PrivateNetworkGateway:
        """Wait blocks until the long-running operation is completed. If no timeout is
        specified, this will poll indefinitely. If a timeout is provided and the operation
        didn't finish within the timeout, this function will raise an error of type
        TimeoutError, otherwise returns successful response and any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: polls indefinitely)

        :returns: :class:`PrivateNetworkGateway`
        """

        def poll_operation():
            operation = self._impl.get_private_network_gateway_operation(name=self._operation.name)

            # Update local operation state
            self._operation = operation

            if not operation.done:
                return None, RetryError.continues("operation still in progress")

            if operation.error:
                error_msg = operation.error.message if operation.error.message else "unknown error"
                if operation.error.error_code:
                    error_msg = f"[{operation.error.error_code}] {error_msg}"
                return None, RetryError.halt(Exception(f"operation failed: {error_msg}"))

            # Operation completed successfully, unmarshal response.
            if operation.response is None:
                return None, RetryError.halt(Exception("operation completed but no response available"))

            private_network_gateway = PrivateNetworkGateway.from_dict(operation.response)

            return private_network_gateway, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else None)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> PrivateNetworkGatewayOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`PrivateNetworkGatewayOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return PrivateNetworkGatewayOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_private_network_gateway_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done

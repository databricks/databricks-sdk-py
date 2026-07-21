# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.
# ruff: noqa: F811, F841
# F401 is intentionally NOT covered: `make fmt` uses `ruff check --fix-only`
# to strip the fat-import header below; ignoring F401 would defeat that.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from google.protobuf.timestamp_pb2 import Timestamp

from databricks.sdk.service._internal import (
    _enum,
    _from_dict,
    _repeated_dict,
    _timestamp,
)

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

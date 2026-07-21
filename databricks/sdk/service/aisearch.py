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

from databricks.sdk.common.types.fieldmask import FieldMask
from databricks.sdk.service._internal import (
    _enum,
    _from_dict,
    _repeated_dict,
    _timestamp,
)

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class ColumnInfo:
    """Column information (name and data type) for an index column. Surfaced on ``Index.column_info``."""

    name: Optional[str] = None
    """Name of the column."""

    type_text: Optional[str] = None
    """Data type of the column (e.g., "string", "int", "array<float>")."""

    def as_dict(self) -> dict:
        """Serializes the ColumnInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.type_text is not None:
            body["type_text"] = self.type_text
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ColumnInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.type_text is not None:
            body["type_text"] = self.type_text
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ColumnInfo:
        """Deserializes the ColumnInfo from a dictionary."""
        return cls(name=d.get("name", None), type_text=d.get("type_text", None))


@dataclass
class CustomTag:
    """User-defined key/value tag attached to an AI Search endpoint for cost attribution and access
    control."""

    key: str
    """Key field for an AI Search endpoint tag."""

    value: Optional[str] = None
    """[Optional] Value field for an AI Search endpoint tag."""

    def as_dict(self) -> dict:
        """Serializes the CustomTag into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.key is not None:
            body["key"] = self.key
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CustomTag into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.key is not None:
            body["key"] = self.key
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CustomTag:
        """Deserializes the CustomTag from a dictionary."""
        return cls(key=d.get("key", None), value=d.get("value", None))


@dataclass
class DataModificationResult:
    """Per-row outcome of a data-plane upsert or delete operation."""

    failed_primary_keys: Optional[List[str]] = None
    """Primary keys of rows that failed to process."""

    success_row_count: Optional[int] = None
    """Count of rows processed successfully."""

    def as_dict(self) -> dict:
        """Serializes the DataModificationResult into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.failed_primary_keys:
            body["failed_primary_keys"] = [v for v in self.failed_primary_keys]
        if self.success_row_count is not None:
            body["success_row_count"] = self.success_row_count
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DataModificationResult into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.failed_primary_keys:
            body["failed_primary_keys"] = self.failed_primary_keys
        if self.success_row_count is not None:
            body["success_row_count"] = self.success_row_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DataModificationResult:
        """Deserializes the DataModificationResult from a dictionary."""
        return cls(
            failed_primary_keys=d.get("failed_primary_keys", None), success_row_count=d.get("success_row_count", None)
        )


class DataModificationStatus(Enum):
    """Overall outcome of a data-plane upsert or delete. Mirrors the legacy
    ``databricks.brickindexscheduler.UpsertDeleteDataStatus`` value-for-value."""

    FAILURE = "FAILURE"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    SUCCESS = "SUCCESS"


@dataclass
class DeltaSyncIndexSpec:
    """Specification for a Delta Sync index — the index is kept in sync with a source Delta table."""

    pipeline_type: PipelineType
    """Pipeline execution mode. Required on create — the backend rejects an unset value. Storage
    Optimized endpoints accept only ``TRIGGERED``; Standard endpoints accept both. No explicit
    ``stage`` — a REQUIRED field staged below its service would be dropped from combined specs
    while remaining in ``required``, tripping the OpenAPI required-vs-properties consistency check.
    The field inherits the service's launch stage."""

    columns_to_sync: Optional[List[str]] = None
    """[Optional] Select the columns to sync with the index. If left blank, all columns from the source
    table are synced. The primary key column and embedding source or vector column are always
    synced."""

    embedding_source_columns: Optional[List[EmbeddingSourceColumn]] = None
    """The columns that contain the embedding source."""

    embedding_vector_columns: Optional[List[EmbeddingVectorColumn]] = None
    """The columns that contain the embedding vectors."""

    embedding_writeback_table: Optional[str] = None
    """[Optional] Name of the Delta table to sync the index contents and computed embeddings to."""

    pipeline_id: Optional[str] = None
    """The ID of the pipeline that is used to sync the index."""

    source_table: Optional[str] = None
    """The full name of the source Delta table."""

    def as_dict(self) -> dict:
        """Serializes the DeltaSyncIndexSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.columns_to_sync:
            body["columns_to_sync"] = [v for v in self.columns_to_sync]
        if self.embedding_source_columns:
            body["embedding_source_columns"] = [v.as_dict() for v in self.embedding_source_columns]
        if self.embedding_vector_columns:
            body["embedding_vector_columns"] = [v.as_dict() for v in self.embedding_vector_columns]
        if self.embedding_writeback_table is not None:
            body["embedding_writeback_table"] = self.embedding_writeback_table
        if self.pipeline_id is not None:
            body["pipeline_id"] = self.pipeline_id
        if self.pipeline_type is not None:
            body["pipeline_type"] = self.pipeline_type.value
        if self.source_table is not None:
            body["source_table"] = self.source_table
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeltaSyncIndexSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.columns_to_sync:
            body["columns_to_sync"] = self.columns_to_sync
        if self.embedding_source_columns:
            body["embedding_source_columns"] = self.embedding_source_columns
        if self.embedding_vector_columns:
            body["embedding_vector_columns"] = self.embedding_vector_columns
        if self.embedding_writeback_table is not None:
            body["embedding_writeback_table"] = self.embedding_writeback_table
        if self.pipeline_id is not None:
            body["pipeline_id"] = self.pipeline_id
        if self.pipeline_type is not None:
            body["pipeline_type"] = self.pipeline_type
        if self.source_table is not None:
            body["source_table"] = self.source_table
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeltaSyncIndexSpec:
        """Deserializes the DeltaSyncIndexSpec from a dictionary."""
        return cls(
            columns_to_sync=d.get("columns_to_sync", None),
            embedding_source_columns=_repeated_dict(d, "embedding_source_columns", EmbeddingSourceColumn),
            embedding_vector_columns=_repeated_dict(d, "embedding_vector_columns", EmbeddingVectorColumn),
            embedding_writeback_table=d.get("embedding_writeback_table", None),
            pipeline_id=d.get("pipeline_id", None),
            pipeline_type=_enum(d, "pipeline_type", PipelineType),
            source_table=d.get("source_table", None),
        )


@dataclass
class DirectAccessIndexSpec:
    """Specification for a Direct Access index — the customer manages vectors and metadata directly."""

    embedding_source_columns: Optional[List[EmbeddingSourceColumn]] = None
    """The columns that contain the embedding source."""

    embedding_vector_columns: Optional[List[EmbeddingVectorColumn]] = None
    """The columns that contain the embedding vectors."""

    schema_json: Optional[str] = None
    """The schema of the index in JSON format. Supported types are ``integer``, ``long``, ``float``,
    ``double``, ``boolean``, ``string``, ``date``, ``timestamp``. Supported types for vector
    columns: ``array<float>``, ``array<double>``."""

    def as_dict(self) -> dict:
        """Serializes the DirectAccessIndexSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.embedding_source_columns:
            body["embedding_source_columns"] = [v.as_dict() for v in self.embedding_source_columns]
        if self.embedding_vector_columns:
            body["embedding_vector_columns"] = [v.as_dict() for v in self.embedding_vector_columns]
        if self.schema_json is not None:
            body["schema_json"] = self.schema_json
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DirectAccessIndexSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.embedding_source_columns:
            body["embedding_source_columns"] = self.embedding_source_columns
        if self.embedding_vector_columns:
            body["embedding_vector_columns"] = self.embedding_vector_columns
        if self.schema_json is not None:
            body["schema_json"] = self.schema_json
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DirectAccessIndexSpec:
        """Deserializes the DirectAccessIndexSpec from a dictionary."""
        return cls(
            embedding_source_columns=_repeated_dict(d, "embedding_source_columns", EmbeddingSourceColumn),
            embedding_vector_columns=_repeated_dict(d, "embedding_vector_columns", EmbeddingVectorColumn),
            schema_json=d.get("schema_json", None),
        )


@dataclass
class EmbeddingSourceColumn:
    """Name of an embedding source column and its associated embedding model endpoint."""

    embedding_model_endpoint: Optional[str] = None
    """Name of the embedding model endpoint, used by default for both ingestion and querying."""

    model_endpoint_name_for_query: Optional[str] = None
    """Name of the embedding model endpoint which, if specified, is used for querying (not ingestion)."""

    name: Optional[str] = None
    """Name of the source column."""

    def as_dict(self) -> dict:
        """Serializes the EmbeddingSourceColumn into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.embedding_model_endpoint is not None:
            body["embedding_model_endpoint"] = self.embedding_model_endpoint
        if self.model_endpoint_name_for_query is not None:
            body["model_endpoint_name_for_query"] = self.model_endpoint_name_for_query
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EmbeddingSourceColumn into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.embedding_model_endpoint is not None:
            body["embedding_model_endpoint"] = self.embedding_model_endpoint
        if self.model_endpoint_name_for_query is not None:
            body["model_endpoint_name_for_query"] = self.model_endpoint_name_for_query
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EmbeddingSourceColumn:
        """Deserializes the EmbeddingSourceColumn from a dictionary."""
        return cls(
            embedding_model_endpoint=d.get("embedding_model_endpoint", None),
            model_endpoint_name_for_query=d.get("model_endpoint_name_for_query", None),
            name=d.get("name", None),
        )


@dataclass
class EmbeddingVectorColumn:
    """Name and dimension of an embedding vector column."""

    embedding_dimension: Optional[int] = None
    """Dimension of the embedding vector."""

    name: Optional[str] = None
    """Name of the column."""

    def as_dict(self) -> dict:
        """Serializes the EmbeddingVectorColumn into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.embedding_dimension is not None:
            body["embedding_dimension"] = self.embedding_dimension
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EmbeddingVectorColumn into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.embedding_dimension is not None:
            body["embedding_dimension"] = self.embedding_dimension
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EmbeddingVectorColumn:
        """Deserializes the EmbeddingVectorColumn from a dictionary."""
        return cls(embedding_dimension=d.get("embedding_dimension", None), name=d.get("name", None))


@dataclass
class Endpoint:
    """An AI Search endpoint — compute infrastructure that hosts AI Search indexes and serves queries
    against them. Customers create, query, and delete endpoints; the system manages provisioning,
    scaling, and health status."""

    endpoint_type: EndpointType
    """Type of endpoint. Required on create and immutable thereafter."""

    budget_policy_id: Optional[str] = None
    """The user-selected budget policy id for the endpoint."""

    create_time: Optional[Timestamp] = None
    """Time the endpoint was created."""

    creator: Optional[str] = None
    """Creator of the endpoint"""

    custom_tags: Optional[List[CustomTag]] = None
    """The custom tags assigned to the endpoint"""

    effective_budget_policy_id: Optional[str] = None
    """The budget policy id applied to the endpoint"""

    endpoint_status: Optional[EndpointStatus] = None
    """Current status of the endpoint"""

    id: Optional[str] = None
    """Unique identifier of the endpoint"""

    index_count: Optional[int] = None
    """Number of indexes on the endpoint"""

    last_updated_user: Optional[str] = None
    """User who last updated the endpoint"""

    name: Optional[str] = None
    """Name of the AI Search endpoint. Server-assigned full resource path
    (``workspaces/{workspace}/endpoints/{endpoint}``) on output. On create, the user-supplied short
    name is conveyed via ``CreateEndpointRequest.endpoint_id``; the server composes the full
    ``name`` and returns it on the response."""

    replica_count: Optional[int] = None
    """The client-supplied desired number of replicas for the endpoint, applied at create/update time.
    Mutually exclusive with ``target_qps``."""

    scaling_info: Optional[EndpointScalingInfo] = None
    """Scaling information for the endpoint"""

    target_qps: Optional[int] = None
    """Target QPS for the endpoint. Mutually exclusive with ``replica_count``. Best-effort; the system
    does not guarantee this QPS will be achieved."""

    throughput_info: Optional[EndpointThroughputInfo] = None
    """Throughput information for the endpoint"""

    update_time: Optional[Timestamp] = None
    """Time the endpoint was last updated."""

    usage_policy_id: Optional[str] = None
    """The usage policy id applied to the endpoint."""

    def as_dict(self) -> dict:
        """Serializes the Endpoint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.creator is not None:
            body["creator"] = self.creator
        if self.custom_tags:
            body["custom_tags"] = [v.as_dict() for v in self.custom_tags]
        if self.effective_budget_policy_id is not None:
            body["effective_budget_policy_id"] = self.effective_budget_policy_id
        if self.endpoint_status:
            body["endpoint_status"] = self.endpoint_status.as_dict()
        if self.endpoint_type is not None:
            body["endpoint_type"] = self.endpoint_type.value
        if self.id is not None:
            body["id"] = self.id
        if self.index_count is not None:
            body["index_count"] = self.index_count
        if self.last_updated_user is not None:
            body["last_updated_user"] = self.last_updated_user
        if self.name is not None:
            body["name"] = self.name
        if self.replica_count is not None:
            body["replica_count"] = self.replica_count
        if self.scaling_info:
            body["scaling_info"] = self.scaling_info.as_dict()
        if self.target_qps is not None:
            body["target_qps"] = self.target_qps
        if self.throughput_info:
            body["throughput_info"] = self.throughput_info.as_dict()
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        if self.usage_policy_id is not None:
            body["usage_policy_id"] = self.usage_policy_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Endpoint into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.creator is not None:
            body["creator"] = self.creator
        if self.custom_tags:
            body["custom_tags"] = self.custom_tags
        if self.effective_budget_policy_id is not None:
            body["effective_budget_policy_id"] = self.effective_budget_policy_id
        if self.endpoint_status:
            body["endpoint_status"] = self.endpoint_status
        if self.endpoint_type is not None:
            body["endpoint_type"] = self.endpoint_type
        if self.id is not None:
            body["id"] = self.id
        if self.index_count is not None:
            body["index_count"] = self.index_count
        if self.last_updated_user is not None:
            body["last_updated_user"] = self.last_updated_user
        if self.name is not None:
            body["name"] = self.name
        if self.replica_count is not None:
            body["replica_count"] = self.replica_count
        if self.scaling_info:
            body["scaling_info"] = self.scaling_info
        if self.target_qps is not None:
            body["target_qps"] = self.target_qps
        if self.throughput_info:
            body["throughput_info"] = self.throughput_info
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.usage_policy_id is not None:
            body["usage_policy_id"] = self.usage_policy_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Endpoint:
        """Deserializes the Endpoint from a dictionary."""
        return cls(
            budget_policy_id=d.get("budget_policy_id", None),
            create_time=_timestamp(d, "create_time"),
            creator=d.get("creator", None),
            custom_tags=_repeated_dict(d, "custom_tags", CustomTag),
            effective_budget_policy_id=d.get("effective_budget_policy_id", None),
            endpoint_status=_from_dict(d, "endpoint_status", EndpointStatus),
            endpoint_type=_enum(d, "endpoint_type", EndpointType),
            id=d.get("id", None),
            index_count=d.get("index_count", None),
            last_updated_user=d.get("last_updated_user", None),
            name=d.get("name", None),
            replica_count=d.get("replica_count", None),
            scaling_info=_from_dict(d, "scaling_info", EndpointScalingInfo),
            target_qps=d.get("target_qps", None),
            throughput_info=_from_dict(d, "throughput_info", EndpointThroughputInfo),
            update_time=_timestamp(d, "update_time"),
            usage_policy_id=d.get("usage_policy_id", None),
        )


@dataclass
class EndpointScalingInfo:
    """Scaling information for a Storage Optimized endpoint — current scaling state and the requested
    QPS target the system is scaling toward."""

    requested_target_qps: Optional[int] = None
    """The requested QPS target for the endpoint. Best-effort; the system does not guarantee this QPS
    will be achieved."""

    state: Optional[ScalingChangeState] = None
    """The current state of the scaling change request."""

    def as_dict(self) -> dict:
        """Serializes the EndpointScalingInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.requested_target_qps is not None:
            body["requested_target_qps"] = self.requested_target_qps
        if self.state is not None:
            body["state"] = self.state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointScalingInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.requested_target_qps is not None:
            body["requested_target_qps"] = self.requested_target_qps
        if self.state is not None:
            body["state"] = self.state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointScalingInfo:
        """Deserializes the EndpointScalingInfo from a dictionary."""
        return cls(
            requested_target_qps=d.get("requested_target_qps", None), state=_enum(d, "state", ScalingChangeState)
        )


@dataclass
class EndpointStatus:
    """Lifecycle and health state of an AI Search endpoint, along with any human-readable detail about
    that state."""

    message: Optional[str] = None
    """Human-readable detail about the endpoint's current state or the reason for a state transition."""

    state: Optional[EndpointStatusState] = None
    """Current lifecycle state of the endpoint. See ``State`` for the meaning of each value."""

    def as_dict(self) -> dict:
        """Serializes the EndpointStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.message is not None:
            body["message"] = self.message
        if self.state is not None:
            body["state"] = self.state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.message is not None:
            body["message"] = self.message
        if self.state is not None:
            body["state"] = self.state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointStatus:
        """Deserializes the EndpointStatus from a dictionary."""
        return cls(message=d.get("message", None), state=_enum(d, "state", EndpointStatusState))


class EndpointStatusState(Enum):
    """Lifecycle state of an AI Search endpoint, used by both Standard and Storage Optimized SKUs."""

    DELETED = "DELETED"
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    PROVISIONING = "PROVISIONING"
    RED_STATE = "RED_STATE"
    YELLOW_STATE = "YELLOW_STATE"


@dataclass
class EndpointThroughputInfo:
    """Throughput information for an AI Search endpoint, including requested and current concurrency
    settings."""

    change_request_message: Optional[str] = None
    """Additional information about the throughput change request"""

    change_request_state: Optional[ThroughputChangeRequestState] = None
    """The state of the most recent throughput change request"""

    current_concurrency: Optional[float] = None
    """The current concurrency (total CPU) allocated to the endpoint"""

    current_concurrency_utilization_percentage: Optional[float] = None
    """The current utilization of concurrency as a percentage (0-100)"""

    current_num_replicas: Optional[int] = None
    """The current number of replicas allocated to the endpoint"""

    maximum_concurrency_allowed: Optional[float] = None
    """The maximum concurrency allowed for this endpoint"""

    minimal_concurrency_allowed: Optional[float] = None
    """The minimum concurrency allowed for this endpoint"""

    requested_concurrency: Optional[float] = None
    """The requested concurrency (total CPU) for the endpoint"""

    requested_num_replicas: Optional[int] = None
    """The requested number of replicas for the endpoint"""

    def as_dict(self) -> dict:
        """Serializes the EndpointThroughputInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.change_request_message is not None:
            body["change_request_message"] = self.change_request_message
        if self.change_request_state is not None:
            body["change_request_state"] = self.change_request_state.value
        if self.current_concurrency is not None:
            body["current_concurrency"] = self.current_concurrency
        if self.current_concurrency_utilization_percentage is not None:
            body["current_concurrency_utilization_percentage"] = self.current_concurrency_utilization_percentage
        if self.current_num_replicas is not None:
            body["current_num_replicas"] = self.current_num_replicas
        if self.maximum_concurrency_allowed is not None:
            body["maximum_concurrency_allowed"] = self.maximum_concurrency_allowed
        if self.minimal_concurrency_allowed is not None:
            body["minimal_concurrency_allowed"] = self.minimal_concurrency_allowed
        if self.requested_concurrency is not None:
            body["requested_concurrency"] = self.requested_concurrency
        if self.requested_num_replicas is not None:
            body["requested_num_replicas"] = self.requested_num_replicas
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointThroughputInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.change_request_message is not None:
            body["change_request_message"] = self.change_request_message
        if self.change_request_state is not None:
            body["change_request_state"] = self.change_request_state
        if self.current_concurrency is not None:
            body["current_concurrency"] = self.current_concurrency
        if self.current_concurrency_utilization_percentage is not None:
            body["current_concurrency_utilization_percentage"] = self.current_concurrency_utilization_percentage
        if self.current_num_replicas is not None:
            body["current_num_replicas"] = self.current_num_replicas
        if self.maximum_concurrency_allowed is not None:
            body["maximum_concurrency_allowed"] = self.maximum_concurrency_allowed
        if self.minimal_concurrency_allowed is not None:
            body["minimal_concurrency_allowed"] = self.minimal_concurrency_allowed
        if self.requested_concurrency is not None:
            body["requested_concurrency"] = self.requested_concurrency
        if self.requested_num_replicas is not None:
            body["requested_num_replicas"] = self.requested_num_replicas
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointThroughputInfo:
        """Deserializes the EndpointThroughputInfo from a dictionary."""
        return cls(
            change_request_message=d.get("change_request_message", None),
            change_request_state=_enum(d, "change_request_state", ThroughputChangeRequestState),
            current_concurrency=d.get("current_concurrency", None),
            current_concurrency_utilization_percentage=d.get("current_concurrency_utilization_percentage", None),
            current_num_replicas=d.get("current_num_replicas", None),
            maximum_concurrency_allowed=d.get("maximum_concurrency_allowed", None),
            minimal_concurrency_allowed=d.get("minimal_concurrency_allowed", None),
            requested_concurrency=d.get("requested_concurrency", None),
            requested_num_replicas=d.get("requested_num_replicas", None),
        )


class EndpointType(Enum):
    """Type of endpoint."""

    STANDARD = "STANDARD"
    STORAGE_OPTIMIZED = "STORAGE_OPTIMIZED"


@dataclass
class FacetResultData:
    """Facet aggregation rows returned by a query."""

    facet_array: Optional[List[List[any]]] = None
    """Facet rows; each row is ``[facet_column_name, value_or_range, count]``."""

    facet_row_count: Optional[int] = None
    """Number of facet rows returned."""

    def as_dict(self) -> dict:
        """Serializes the FacetResultData into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.facet_array:
            body["facet_array"] = [v for v in self.facet_array]
        if self.facet_row_count is not None:
            body["facet_row_count"] = self.facet_row_count
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the FacetResultData into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.facet_array:
            body["facet_array"] = self.facet_array
        if self.facet_row_count is not None:
            body["facet_row_count"] = self.facet_row_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> FacetResultData:
        """Deserializes the FacetResultData from a dictionary."""
        return cls(facet_array=d.get("facet_array", None), facet_row_count=d.get("facet_row_count", None))


@dataclass
class Index:
    """An AI Search index — a searchable collection of vectors and metadata hosted on an AI Search
    endpoint. Indexes are children of endpoints; customers create, get, list, and delete them. The
    ``{index}`` segment of the resource name is the index's Unity Catalog table name."""

    primary_key: str
    """Primary key of the index. Set on create and immutable thereafter."""

    index_type: IndexType
    """Type of index. Required on create and immutable thereafter."""

    creator: Optional[str] = None
    """Creator of the index."""

    delta_sync_index_spec: Optional[DeltaSyncIndexSpec] = None
    """Specification for a Delta Sync index. Set when ``index_type`` is ``DELTA_SYNC``."""

    direct_access_index_spec: Optional[DirectAccessIndexSpec] = None
    """Specification for a Direct Access index. Set when ``index_type`` is ``DIRECT_ACCESS``."""

    endpoint: Optional[str] = None
    """Name of the endpoint associated with the index. Ignored on create — the endpoint is taken from
    ``CreateIndexRequest.parent``; populated only on output."""

    index_subtype: Optional[IndexSubtype] = None
    """The subtype of the index. Set on create and immutable thereafter."""

    name: Optional[str] = None
    """Name of the AI Search index. Server-assigned full resource path
    (``workspaces/{workspace}/endpoints/{endpoint}/indexes/{index}``) on output, where ``{index}``
    is the index's Unity Catalog table name. On create, the user-supplied UC table name is conveyed
    via ``CreateIndexRequest.index_id``; the server composes the full ``name`` and returns it on the
    response."""

    status: Optional[IndexStatus] = None
    """Current status of the index."""

    def as_dict(self) -> dict:
        """Serializes the Index into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.creator is not None:
            body["creator"] = self.creator
        if self.delta_sync_index_spec:
            body["delta_sync_index_spec"] = self.delta_sync_index_spec.as_dict()
        if self.direct_access_index_spec:
            body["direct_access_index_spec"] = self.direct_access_index_spec.as_dict()
        if self.endpoint is not None:
            body["endpoint"] = self.endpoint
        if self.index_subtype is not None:
            body["index_subtype"] = self.index_subtype.value
        if self.index_type is not None:
            body["index_type"] = self.index_type.value
        if self.name is not None:
            body["name"] = self.name
        if self.primary_key is not None:
            body["primary_key"] = self.primary_key
        if self.status:
            body["status"] = self.status.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Index into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.creator is not None:
            body["creator"] = self.creator
        if self.delta_sync_index_spec:
            body["delta_sync_index_spec"] = self.delta_sync_index_spec
        if self.direct_access_index_spec:
            body["direct_access_index_spec"] = self.direct_access_index_spec
        if self.endpoint is not None:
            body["endpoint"] = self.endpoint
        if self.index_subtype is not None:
            body["index_subtype"] = self.index_subtype
        if self.index_type is not None:
            body["index_type"] = self.index_type
        if self.name is not None:
            body["name"] = self.name
        if self.primary_key is not None:
            body["primary_key"] = self.primary_key
        if self.status:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Index:
        """Deserializes the Index from a dictionary."""
        return cls(
            creator=d.get("creator", None),
            delta_sync_index_spec=_from_dict(d, "delta_sync_index_spec", DeltaSyncIndexSpec),
            direct_access_index_spec=_from_dict(d, "direct_access_index_spec", DirectAccessIndexSpec),
            endpoint=d.get("endpoint", None),
            index_subtype=_enum(d, "index_subtype", IndexSubtype),
            index_type=_enum(d, "index_type", IndexType),
            name=d.get("name", None),
            primary_key=d.get("primary_key", None),
            status=_from_dict(d, "status", IndexStatus),
        )


@dataclass
class IndexStatus:
    """Lifecycle and health state of an AI Search index, along with human-readable detail about that
    state and basic indexing progress."""

    index_url: Optional[str] = None
    """Index API URL used to perform operations on the index."""

    indexed_row_count: Optional[int] = None
    """Number of rows indexed."""

    message: Optional[str] = None
    """Human-readable detail about the index's current state."""

    ready: Optional[bool] = None
    """Whether the index is ready for search."""

    def as_dict(self) -> dict:
        """Serializes the IndexStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.index_url is not None:
            body["index_url"] = self.index_url
        if self.indexed_row_count is not None:
            body["indexed_row_count"] = self.indexed_row_count
        if self.message is not None:
            body["message"] = self.message
        if self.ready is not None:
            body["ready"] = self.ready
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the IndexStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.index_url is not None:
            body["index_url"] = self.index_url
        if self.indexed_row_count is not None:
            body["indexed_row_count"] = self.indexed_row_count
        if self.message is not None:
            body["message"] = self.message
        if self.ready is not None:
            body["ready"] = self.ready
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> IndexStatus:
        """Deserializes the IndexStatus from a dictionary."""
        return cls(
            index_url=d.get("index_url", None),
            indexed_row_count=d.get("indexed_row_count", None),
            message=d.get("message", None),
            ready=d.get("ready", None),
        )


class IndexSubtype(Enum):
    """The subtype of the AI Search index, determining the indexing and retrieval strategy.

    - ``VECTOR``: Not a supported create value — do not select it. Use ``HYBRID`` (vector + hybrid
      search) or ``FULL_TEXT`` (full-text only). It is the proto2 default (``= 0``) solely to mirror
      the legacy ``index_v2.proto`` enum value-for-value; it is not an offered index subtype.
    - ``FULL_TEXT``: An index that uses full-text search without vector embeddings.
    - ``HYBRID``: An index that uses vector embeddings for similarity search and hybrid search."""

    FULL_TEXT = "FULL_TEXT"
    HYBRID = "HYBRID"
    VECTOR = "VECTOR"


class IndexType(Enum):
    """There are 2 types of AI Search indexes:

    - ``DELTA_SYNC``: An index that automatically syncs with a source Delta Table, automatically and
      incrementally updating the index as the underlying data in the Delta Table changes.
    - ``DIRECT_ACCESS``: An index that supports direct read and write of vectors and metadata
      through our REST and SDK APIs. With this model, the user manages index updates."""

    DELTA_SYNC = "DELTA_SYNC"
    DIRECT_ACCESS = "DIRECT_ACCESS"


@dataclass
class ListEndpointsResponse:
    """Response for ListEndpoints carrying the page of endpoints and an optional continuation token."""

    endpoints: Optional[List[Endpoint]] = None
    """The endpoints in the workspace."""

    next_page_token: Optional[str] = None
    """A token that can be used to get the next page of results. Empty when there are no more results."""

    def as_dict(self) -> dict:
        """Serializes the ListEndpointsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.endpoints:
            body["endpoints"] = [v.as_dict() for v in self.endpoints]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListEndpointsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.endpoints:
            body["endpoints"] = self.endpoints
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListEndpointsResponse:
        """Deserializes the ListEndpointsResponse from a dictionary."""
        return cls(endpoints=_repeated_dict(d, "endpoints", Endpoint), next_page_token=d.get("next_page_token", None))


@dataclass
class ListIndexesResponse:
    """Response for ListIndexes carrying the page of indexes and an optional continuation token."""

    indexes: Optional[List[Index]] = None
    """The indexes on the endpoint. The field is named ``indexes`` (not the irregular plural
    ``indices``) to satisfy core::0132, which derives the response field name from the ListIndexes
    method. core::0158::response-plural-first-field independently computes the resource plural as
    ``indices`` and is satisfied via a scoped field exception below."""

    next_page_token: Optional[str] = None
    """A token that can be used to get the next page of results. Empty when there are no more results."""

    def as_dict(self) -> dict:
        """Serializes the ListIndexesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.indexes:
            body["indexes"] = [v.as_dict() for v in self.indexes]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListIndexesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.indexes:
            body["indexes"] = self.indexes
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListIndexesResponse:
        """Deserializes the ListIndexesResponse from a dictionary."""
        return cls(indexes=_repeated_dict(d, "indexes", Index), next_page_token=d.get("next_page_token", None))


class PipelineType(Enum):
    """Pipeline execution mode for a Delta Sync index. Required on create for Delta Sync indexes; the
    legacy backend rejects an unset value with INVALID_PARAMETER_VALUE.

    - ``TRIGGERED``: the pipeline stops after refreshing the source table once, using the data
      available when the update started.
    - ``CONTINUOUS``: the pipeline processes new data as it arrives in the source table to keep the
      index fresh."""

    CONTINUOUS = "CONTINUOUS"
    TRIGGERED = "TRIGGERED"


@dataclass
class QueryIndexResponse:
    """Response for QueryIndex carrying the matched rows and their column metadata."""

    facet_result: Optional[FacetResultData] = None
    """Facet aggregation rows, when facets were requested."""

    manifest: Optional[ResultManifest] = None
    """Metadata describing the result columns."""

    result: Optional[ResultData] = None
    """The matched result rows."""

    def as_dict(self) -> dict:
        """Serializes the QueryIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.facet_result:
            body["facet_result"] = self.facet_result.as_dict()
        if self.manifest:
            body["manifest"] = self.manifest.as_dict()
        if self.result:
            body["result"] = self.result.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the QueryIndexResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.facet_result:
            body["facet_result"] = self.facet_result
        if self.manifest:
            body["manifest"] = self.manifest
        if self.result:
            body["result"] = self.result
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> QueryIndexResponse:
        """Deserializes the QueryIndexResponse from a dictionary."""
        return cls(
            facet_result=_from_dict(d, "facet_result", FacetResultData),
            manifest=_from_dict(d, "manifest", ResultManifest),
            result=_from_dict(d, "result", ResultData),
        )


@dataclass
class RemoveDataResponse:
    """Response for RemoveData."""

    result: Optional[DataModificationResult] = None
    """Per-row outcome of the delete."""

    status: Optional[DataModificationStatus] = None
    """Overall status of the delete."""

    def as_dict(self) -> dict:
        """Serializes the RemoveDataResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.result:
            body["result"] = self.result.as_dict()
        if self.status is not None:
            body["status"] = self.status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RemoveDataResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.result:
            body["result"] = self.result
        if self.status is not None:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RemoveDataResponse:
        """Deserializes the RemoveDataResponse from a dictionary."""
        return cls(
            result=_from_dict(d, "result", DataModificationResult), status=_enum(d, "status", DataModificationStatus)
        )


@dataclass
class RerankerConfig:
    """Configuration for reranking query results with a reranker model."""

    model: Optional[str] = None
    """Reranker identifier: "databricks_reranker" for the base model, or a Model Serving endpoint name
    when ``model_type`` is MODEL_TYPE_FINETUNED."""

    model_type: Optional[RerankerConfigModelType] = None
    """Discriminator for how ``model`` is interpreted."""

    parameters: Optional[RerankerConfigRerankerParameters] = None
    """Parameters controlling reranking."""

    def as_dict(self) -> dict:
        """Serializes the RerankerConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.model is not None:
            body["model"] = self.model
        if self.model_type is not None:
            body["model_type"] = self.model_type.value
        if self.parameters:
            body["parameters"] = self.parameters.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RerankerConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.model is not None:
            body["model"] = self.model
        if self.model_type is not None:
            body["model_type"] = self.model_type
        if self.parameters:
            body["parameters"] = self.parameters
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RerankerConfig:
        """Deserializes the RerankerConfig from a dictionary."""
        return cls(
            model=d.get("model", None),
            model_type=_enum(d, "model_type", RerankerConfigModelType),
            parameters=_from_dict(d, "parameters", RerankerConfigRerankerParameters),
        )


class RerankerConfigModelType(Enum):
    """How the ``model`` field is interpreted."""

    MODEL_TYPE_BASE = "MODEL_TYPE_BASE"
    MODEL_TYPE_FINETUNED = "MODEL_TYPE_FINETUNED"


@dataclass
class RerankerConfigRerankerParameters:
    """Parameters controlling how the reranker processes results."""

    columns_to_rerank: Optional[List[str]] = None
    """Columns whose values are concatenated and sent to the reranker."""

    def as_dict(self) -> dict:
        """Serializes the RerankerConfigRerankerParameters into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.columns_to_rerank:
            body["columns_to_rerank"] = [v for v in self.columns_to_rerank]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RerankerConfigRerankerParameters into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.columns_to_rerank:
            body["columns_to_rerank"] = self.columns_to_rerank
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RerankerConfigRerankerParameters:
        """Deserializes the RerankerConfigRerankerParameters from a dictionary."""
        return cls(columns_to_rerank=d.get("columns_to_rerank", None))


@dataclass
class ResultData:
    """The rows of a query result set."""

    data_array: Optional[List[List[any]]] = None
    """Result rows; each row is a list of column values aligned with the manifest columns."""

    row_count: Optional[int] = None
    """Number of rows in the result set."""

    def as_dict(self) -> dict:
        """Serializes the ResultData into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.data_array:
            body["data_array"] = [v for v in self.data_array]
        if self.row_count is not None:
            body["row_count"] = self.row_count
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ResultData into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.data_array:
            body["data_array"] = self.data_array
        if self.row_count is not None:
            body["row_count"] = self.row_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResultData:
        """Deserializes the ResultData from a dictionary."""
        return cls(data_array=d.get("data_array", None), row_count=d.get("row_count", None))


@dataclass
class ResultManifest:
    """Metadata describing the columns of a query result set."""

    column_count: Optional[int] = None
    """Number of columns in the result set."""

    columns: Optional[List[ColumnInfo]] = None
    """Information about each column in the result set."""

    facet_column_count: Optional[int] = None
    """Number of columns in the facet result."""

    facet_columns: Optional[List[ColumnInfo]] = None
    """Information about each facet column."""

    def as_dict(self) -> dict:
        """Serializes the ResultManifest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.column_count is not None:
            body["column_count"] = self.column_count
        if self.columns:
            body["columns"] = [v.as_dict() for v in self.columns]
        if self.facet_column_count is not None:
            body["facet_column_count"] = self.facet_column_count
        if self.facet_columns:
            body["facet_columns"] = [v.as_dict() for v in self.facet_columns]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ResultManifest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.column_count is not None:
            body["column_count"] = self.column_count
        if self.columns:
            body["columns"] = self.columns
        if self.facet_column_count is not None:
            body["facet_column_count"] = self.facet_column_count
        if self.facet_columns:
            body["facet_columns"] = self.facet_columns
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResultManifest:
        """Deserializes the ResultManifest from a dictionary."""
        return cls(
            column_count=d.get("column_count", None),
            columns=_repeated_dict(d, "columns", ColumnInfo),
            facet_column_count=d.get("facet_column_count", None),
            facet_columns=_repeated_dict(d, "facet_columns", ColumnInfo),
        )


class ScalingChangeState(Enum):
    """State of the most recent scaling change request for a Storage Optimized endpoint."""

    SCALING_CHANGE_APPLIED = "SCALING_CHANGE_APPLIED"
    SCALING_CHANGE_IN_PROGRESS = "SCALING_CHANGE_IN_PROGRESS"
    SCALING_CHANGE_UNSPECIFIED = "SCALING_CHANGE_UNSPECIFIED"


@dataclass
class ScanIndexResponse:
    """Response for ScanIndex carrying a page of rows and an optional continuation token."""

    data: Optional[List[Dict[str, any]]] = None
    """The rows in this page, each a struct of column name to value."""

    next_page_token: Optional[str] = None
    """Token for the next page; empty when the scan is exhausted."""

    def as_dict(self) -> dict:
        """Serializes the ScanIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.data:
            body["data"] = [v for v in self.data]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ScanIndexResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.data:
            body["data"] = self.data
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ScanIndexResponse:
        """Deserializes the ScanIndexResponse from a dictionary."""
        return cls(data=d.get("data", None), next_page_token=d.get("next_page_token", None))


@dataclass
class SyncIndexResponse:
    """Response for SyncIndex. Empty today; reserved so future sync metadata (e.g. an operation handle)
    can be added without breaking the wire contract."""

    def as_dict(self) -> dict:
        """Serializes the SyncIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SyncIndexResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SyncIndexResponse:
        """Deserializes the SyncIndexResponse from a dictionary."""
        return cls()


class ThroughputChangeRequestState(Enum):
    """State of the most recent throughput change request issued against a Storage Optimized endpoint.
    Surfaced on ``EndpointThroughputInfo.change_request_state``."""

    CHANGE_ADJUSTED = "CHANGE_ADJUSTED"
    CHANGE_FAILED = "CHANGE_FAILED"
    CHANGE_IN_PROGRESS = "CHANGE_IN_PROGRESS"
    CHANGE_REACHED_MAXIMUM = "CHANGE_REACHED_MAXIMUM"
    CHANGE_REACHED_MINIMUM = "CHANGE_REACHED_MINIMUM"
    CHANGE_SUCCESS = "CHANGE_SUCCESS"


@dataclass
class UpsertDataResponse:
    """Response for UpsertData."""

    result: Optional[DataModificationResult] = None
    """Per-row outcome of the upsert."""

    status: Optional[DataModificationStatus] = None
    """Overall status of the upsert."""

    def as_dict(self) -> dict:
        """Serializes the UpsertDataResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.result:
            body["result"] = self.result.as_dict()
        if self.status is not None:
            body["status"] = self.status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UpsertDataResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.result:
            body["result"] = self.result
        if self.status is not None:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UpsertDataResponse:
        """Deserializes the UpsertDataResponse from a dictionary."""
        return cls(
            result=_from_dict(d, "result", DataModificationResult), status=_enum(d, "status", DataModificationStatus)
        )


class AiSearchAPI:
    """**AI Search Endpoint**: Represents the compute resources to host AI Search indexes. AIP-conformant
    replacement for the legacy VectorSearchEndpoints API; functionally equivalent."""

    def __init__(self, api_client):
        self._api = api_client

    def create_endpoint(self, parent: str, endpoint: Endpoint, *, endpoint_id: Optional[str] = None) -> Endpoint:
        """Create a new AI Search endpoint.

        :param parent: str
          The Workspace where this Endpoint will be created. Format: ``workspaces/{workspace_id}``
        :param endpoint: :class:`Endpoint`
          The Endpoint resource to create. Fields other than ``endpoint.name`` carry the desired
          configuration; ``endpoint.name`` is server-assigned from ``parent`` and ``endpoint_id``.
        :param endpoint_id: str (optional)
          The user-supplied short name for the Endpoint, per AIP-133. The server composes the full
          ``Endpoint.name`` as ``{parent}/endpoints/{endpoint_id}``. AIP-133 does not list ``endpoint_id`` as
          a fields-may-be-required entry, so we annotate it OPTIONAL on the wire; the server still rejects
          empty values with INVALID_PARAMETER_VALUE.

        :returns: :class:`Endpoint`
        """

        body = endpoint.as_dict()
        query = {}
        if endpoint_id is not None:
            query["endpoint_id"] = endpoint_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/ai-search/{parent}/endpoints", query=query, body=body, headers=headers)
        return Endpoint.from_dict(res)

    def create_index(self, parent: str, index: Index, *, index_id: Optional[str] = None) -> Index:
        """Create a new AI Search index.

        :param parent: str
          The Endpoint where this Index will be created. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}``
        :param index: :class:`Index`
          The Index resource to create. Fields other than ``index.name`` carry the desired configuration;
          ``index.name`` is server-assigned from ``parent`` and ``index_id``.
        :param index_id: str (optional)
          The user-supplied Unity Catalog table name for the Index, per AIP-133. The server composes the full
          ``Index.name`` as ``{parent}/indexes/{index_id}``. AIP-133 does not list ``index_id`` as a
          fields-may-be-required entry, so we annotate it OPTIONAL on the wire; the server still rejects empty
          values with INVALID_PARAMETER_VALUE.

        :returns: :class:`Index`
        """

        body = index.as_dict()
        query = {}
        if index_id is not None:
            query["index_id"] = index_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/ai-search/{parent}/indexes", query=query, body=body, headers=headers)
        return Index.from_dict(res)

    def delete_endpoint(self, name: str):
        """Delete an AI Search endpoint.

        :param name: str
          Full resource name of the endpoint to delete. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}``


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/ai-search/{name}", headers=headers)

    def delete_index(self, name: str):
        """Delete an AI Search index.

        :param name: str
          Full resource name of the index to delete. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/ai-search/{name}", headers=headers)

    def get_endpoint(self, name: str) -> Endpoint:
        """Get details for a single AI Search endpoint.

        :param name: str
          Full resource name of the endpoint. Format: ``workspaces/{workspace_id}/endpoints/{endpoint_id}``

        :returns: :class:`Endpoint`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/ai-search/{name}", headers=headers)
        return Endpoint.from_dict(res)

    def get_index(self, name: str) -> Index:
        """Get details for a single AI Search index.

        :param name: str
          Full resource name of the index. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``

        :returns: :class:`Index`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/ai-search/{name}", headers=headers)
        return Index.from_dict(res)

    def list_endpoints(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Endpoint]:
        """List AI Search endpoints in a workspace.

        :param parent: str
          The Workspace that owns this collection of endpoints. Format: ``workspaces/{workspace_id}``
        :param page_size: int (optional)
          Best-effort upper bound on the number of results to return. Honored as an upper bound by the shim:
          ``page_size`` only narrows the legacy backend's response, never widens it, so the practical cap is
          ``min(page_size, legacy_fixed_page_size)``.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.

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

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", f"/api/2.0/ai-search/{parent}/endpoints", query=query, headers=headers)
            if "endpoints" in json:
                for v in json["endpoints"]:
                    yield Endpoint.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_indexes(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Index]:
        """List AI Search indexes on an endpoint.

        :param parent: str
          The Endpoint that owns this collection of indexes. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}``
        :param page_size: int (optional)
          Best-effort upper bound on the number of results to return. Honored as an upper bound by the shim:
          ``page_size`` only narrows the legacy backend's response, never widens it, so the practical cap is
          ``min(page_size, legacy_fixed_page_size)``.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.

        :returns: Iterator over :class:`Index`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", f"/api/2.0/ai-search/{parent}/indexes", query=query, headers=headers)
            if "indexes" in json:
                for v in json["indexes"]:
                    yield Index.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def query_index(
        self,
        name: str,
        columns: List[str],
        *,
        columns_to_rerank: Optional[List[str]] = None,
        facets: Optional[List[str]] = None,
        filters_json: Optional[str] = None,
        max_results: Optional[int] = None,
        query_columns: Optional[List[str]] = None,
        query_text: Optional[str] = None,
        query_type: Optional[str] = None,
        query_vector: Optional[List[float]] = None,
        reranker: Optional[RerankerConfig] = None,
        score_threshold: Optional[float] = None,
        sort_columns: Optional[List[str]] = None,
    ) -> QueryIndexResponse:
        """Query (search) an AI Search index. Read-only, so a read-scoped token may invoke it.

        :param name: str
          Full resource name of the index to query. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``
        :param columns: List[str]
          Column names to include in each result row.
        :param columns_to_rerank: List[str] (optional)
          Columns whose values are sent to the reranker.
        :param facets: List[str] (optional)
          Facets to compute over the matched results (e.g. ``"category TOP 5"``).
        :param filters_json: str (optional)
          JSON string describing query filters (e.g. ``{"id >": 5}``).
        :param max_results: int (optional)
          Maximum number of results to return (the legacy ``num_results``). Defaults to 10.
        :param query_columns: List[str] (optional)
          Text columns to search for ``query_text``. When empty, all text columns are searched.
        :param query_text: str (optional)
          Query text. Required for Delta Sync indexes that compute embeddings from a model endpoint.
        :param query_type: str (optional)
          Query type: ``ANN``, ``HYBRID``, or ``FULL_TEXT``. Defaults to ``ANN``.
        :param query_vector: List[float] (optional)
          Query vector. Required for Direct Access indexes and Delta Sync indexes with self-managed vectors.
        :param reranker: :class:`RerankerConfig` (optional)
          If set, results are reranked before being returned.
        :param score_threshold: float (optional)
          Score threshold for the approximate nearest-neighbor search. Defaults to 0.0.
        :param sort_columns: List[str] (optional)
          Sort clauses, e.g. ``["rating DESC", "price ASC"]``. Overrides relevance ordering.

        :returns: :class:`QueryIndexResponse`
        """

        body = {}
        if columns is not None:
            body["columns"] = [v for v in columns]
        if columns_to_rerank is not None:
            body["columns_to_rerank"] = [v for v in columns_to_rerank]
        if facets is not None:
            body["facets"] = [v for v in facets]
        if filters_json is not None:
            body["filters_json"] = filters_json
        if max_results is not None:
            body["max_results"] = max_results
        if query_columns is not None:
            body["query_columns"] = [v for v in query_columns]
        if query_text is not None:
            body["query_text"] = query_text
        if query_type is not None:
            body["query_type"] = query_type
        if query_vector is not None:
            body["query_vector"] = [v for v in query_vector]
        if reranker is not None:
            body["reranker"] = reranker.as_dict()
        if score_threshold is not None:
            body["score_threshold"] = score_threshold
        if sort_columns is not None:
            body["sort_columns"] = [v for v in sort_columns]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/ai-search/{name}:query", body=body, headers=headers)
        return QueryIndexResponse.from_dict(res)

    def remove_data(self, name: str, primary_keys: List[str]) -> RemoveDataResponse:
        """Remove rows by primary key from a Direct Access AI Search index.

        :param name: str
          Full resource name of the index. Must be a Direct Access index. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``
        :param primary_keys: List[str]
          Primary keys of the rows to remove.

        :returns: :class:`RemoveDataResponse`
        """

        body = {}
        if primary_keys is not None:
            body["primary_keys"] = [v for v in primary_keys]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/ai-search/{name}:removeData", body=body, headers=headers)
        return RemoveDataResponse.from_dict(res)

    def scan_index(
        self, name: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> ScanIndexResponse:
        """Scan (paginate over) the rows of an AI Search index.

        :param name: str
          Full resource name of the index to scan. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``
        :param page_size: int (optional)
          Maximum number of rows to return in this page.
        :param page_token: str (optional)
          Page token from a previous response; if unset, scanning starts from the beginning.

        :returns: :class:`ScanIndexResponse`
        """

        body = {}
        if page_size is not None:
            body["page_size"] = page_size
        if page_token is not None:
            body["page_token"] = page_token
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/ai-search/{name}:scan", body=body, headers=headers)
        return ScanIndexResponse.from_dict(res)

    def sync_index(self, name: str) -> SyncIndexResponse:
        """Synchronize a Delta Sync AI Search index with its source Delta table. Applies only to Delta Sync
        indexes; Direct Access indexes are written via the data-plane upsert path.

        :param name: str
          Full resource name of the index to synchronize. Must be a Delta Sync index. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``

        :returns: :class:`SyncIndexResponse`
        """

        body = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/ai-search/{name}:sync", body=body, headers=headers)
        return SyncIndexResponse.from_dict(res)

    def update_endpoint(self, name: str, endpoint: Endpoint, update_mask: FieldMask) -> Endpoint:
        """Update an existing AI Search endpoint. Multi-bucket masks are supported and dispatched in
        deterministic bucket order: budget policy, custom tags, throughput, then scaling/replicas. Per-bucket
        dispatch is not atomic across buckets — if a later bucket fails, earlier buckets may already have
        been applied.

        :param name: str
          Name of the AI Search endpoint. Server-assigned full resource path
          (``workspaces/{workspace}/endpoints/{endpoint}``) on output. On create, the user-supplied short name
          is conveyed via ``CreateEndpointRequest.endpoint_id``; the server composes the full ``name`` and
          returns it on the response.
        :param endpoint: :class:`Endpoint`
          The Endpoint resource to update. ``endpoint.name`` carries the full resource path.
        :param update_mask: FieldMask
          The list of fields to update.

        :returns: :class:`Endpoint`
        """

        body = endpoint.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/ai-search/{name}", query=query, body=body, headers=headers)
        return Endpoint.from_dict(res)

    def upsert_data(self, name: str, inputs_json: str) -> UpsertDataResponse:
        """Upsert rows into a Direct Access AI Search index.

        :param name: str
          Full resource name of the index. Must be a Direct Access index. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``
        :param inputs_json: str
          JSON document describing the rows to upsert.

        :returns: :class:`UpsertDataResponse`
        """

        body = {}
        if inputs_json is not None:
            body["inputs_json"] = inputs_json
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/ai-search/{name}:upsertData", body=body, headers=headers)
        return UpsertDataResponse.from_dict(res)

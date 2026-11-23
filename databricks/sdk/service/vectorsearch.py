# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.
# ruff: noqa: F811, F841
# F401 is intentionally NOT covered: `make fmt` uses `ruff check --fix-only`
# to strip the fat-import header below; ignoring F401 would defeat that.

from __future__ import annotations
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Dict, List, Any, Iterator, Callable, Optional

from google.protobuf.timestamp_pb2 import Timestamp

import time
import random
import logging

from ..errors import OperationFailed
from databricks.sdk.service._internal import (
    _enum,
    _from_dict,
    _int64,
    _repeated_dict,
    _timestamp,
    Wait,
)


_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class ColumnInfo:
    name: Optional[str] = None
    """Name of the column."""

    type_text: Optional[str] = None
    """Data type of the column (e.g., "string", "int", "array<float>")"""

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
class DeleteDataResult:
    failed_primary_keys: Optional[List[str]] = None
    """List of primary keys for rows that failed to process."""

    success_row_count: Optional[int] = None
    """Count of successfully processed rows."""

    def as_dict(self) -> dict:
        """Serializes the DeleteDataResult into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.failed_primary_keys:
            body["failed_primary_keys"] = [v for v in self.failed_primary_keys]
        if self.success_row_count is not None:
            body["success_row_count"] = self.success_row_count
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteDataResult into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.failed_primary_keys:
            body["failed_primary_keys"] = self.failed_primary_keys
        if self.success_row_count is not None:
            body["success_row_count"] = self.success_row_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeleteDataResult:
        """Deserializes the DeleteDataResult from a dictionary."""
        return cls(
            failed_primary_keys=d.get("failed_primary_keys", None), success_row_count=_int64(d, "success_row_count")
        )


class DeleteDataStatus(Enum):
    FAILURE = "FAILURE"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    SUCCESS = "SUCCESS"


@dataclass
class DeleteDataVectorIndexResponse:
    result: Optional[DeleteDataResult] = None
    """Result of the upsert or delete operation."""

    status: Optional[DeleteDataStatus] = None
    """Status of the delete operation."""

    def as_dict(self) -> dict:
        """Serializes the DeleteDataVectorIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.result:
            body["result"] = self.result.as_dict()
        if self.status is not None:
            body["status"] = self.status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteDataVectorIndexResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.result:
            body["result"] = self.result
        if self.status is not None:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeleteDataVectorIndexResponse:
        """Deserializes the DeleteDataVectorIndexResponse from a dictionary."""
        return cls(result=_from_dict(d, "result", DeleteDataResult), status=_enum(d, "status", DeleteDataStatus))


@dataclass
class DeleteEndpointResponse:
    def as_dict(self) -> dict:
        """Serializes the DeleteEndpointResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteEndpointResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeleteEndpointResponse:
        """Deserializes the DeleteEndpointResponse from a dictionary."""
        return cls()


@dataclass
class DeleteIndexResponse:
    def as_dict(self) -> dict:
        """Serializes the DeleteIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteIndexResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeleteIndexResponse:
        """Deserializes the DeleteIndexResponse from a dictionary."""
        return cls()


@dataclass
class DeltaSyncVectorIndexSpecRequest:
    columns_to_index: Optional[List[str]] = None
    """[Optional] Alias for columns_to_sync. Select the columns to include in the vector index. If you
    leave this field blank, all columns from the source table are included. The primary key column
    and embedding source column or embedding vector column are always included. Only one of
    columns_to_sync or columns_to_index may be specified."""

    columns_to_sync: Optional[List[str]] = None
    """[Optional] Select the columns to sync with the vector index. If you leave this field blank, all
    columns from the source table are synced with the index. The primary key column and embedding
    source column or embedding vector column are always synced."""

    embedding_source_columns: Optional[List[EmbeddingSourceColumn]] = None
    """The source table column whose text Databricks embeds, together with the embedding model endpoint
    to use. Set this for an index with Databricks-managed embeddings. Exactly one of
    ``embedding_source_columns`` or ``embedding_vector_columns`` must be specified unless the index
    subtype is ``FULL_TEXT``, and only one column is supported."""

    embedding_vector_columns: Optional[List[EmbeddingVectorColumn]] = None
    """The source table column that contains precomputed embedding vectors. Set this instead of
    ``embedding_source_columns`` for an index with self-managed embeddings."""

    embedding_writeback_table: Optional[str] = None
    """[Optional] Name of the Delta table to sync the vector index contents and computed embeddings to."""

    pipeline_type: Optional[PipelineType] = None
    """Pipeline execution mode.
    
    - ``TRIGGERED``: If the pipeline uses the triggered execution mode, the system stops processing
      after successfully refreshing the source table in the pipeline once, ensuring the table is
      updated based on the data available when the update started.
    - ``CONTINUOUS``: If the pipeline uses continuous execution, the pipeline processes new data as
      it arrives in the source table to keep vector index fresh."""

    source_table: Optional[str] = None
    """Three-level Unity Catalog name of the source table that the index is synced from."""

    def as_dict(self) -> dict:
        """Serializes the DeltaSyncVectorIndexSpecRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.columns_to_index:
            body["columns_to_index"] = [v for v in self.columns_to_index]
        if self.columns_to_sync:
            body["columns_to_sync"] = [v for v in self.columns_to_sync]
        if self.embedding_source_columns:
            body["embedding_source_columns"] = [v.as_dict() for v in self.embedding_source_columns]
        if self.embedding_vector_columns:
            body["embedding_vector_columns"] = [v.as_dict() for v in self.embedding_vector_columns]
        if self.embedding_writeback_table is not None:
            body["embedding_writeback_table"] = self.embedding_writeback_table
        if self.pipeline_type is not None:
            body["pipeline_type"] = self.pipeline_type.value
        if self.source_table is not None:
            body["source_table"] = self.source_table
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeltaSyncVectorIndexSpecRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.columns_to_index:
            body["columns_to_index"] = self.columns_to_index
        if self.columns_to_sync:
            body["columns_to_sync"] = self.columns_to_sync
        if self.embedding_source_columns:
            body["embedding_source_columns"] = self.embedding_source_columns
        if self.embedding_vector_columns:
            body["embedding_vector_columns"] = self.embedding_vector_columns
        if self.embedding_writeback_table is not None:
            body["embedding_writeback_table"] = self.embedding_writeback_table
        if self.pipeline_type is not None:
            body["pipeline_type"] = self.pipeline_type
        if self.source_table is not None:
            body["source_table"] = self.source_table
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeltaSyncVectorIndexSpecRequest:
        """Deserializes the DeltaSyncVectorIndexSpecRequest from a dictionary."""
        return cls(
            columns_to_index=d.get("columns_to_index", None),
            columns_to_sync=d.get("columns_to_sync", None),
            embedding_source_columns=_repeated_dict(d, "embedding_source_columns", EmbeddingSourceColumn),
            embedding_vector_columns=_repeated_dict(d, "embedding_vector_columns", EmbeddingVectorColumn),
            embedding_writeback_table=d.get("embedding_writeback_table", None),
            pipeline_type=_enum(d, "pipeline_type", PipelineType),
            source_table=d.get("source_table", None),
        )


@dataclass
class DeltaSyncVectorIndexSpecResponse:
    columns_to_index: Optional[List[str]] = None
    """[Optional] Alias for columns_to_sync. Select the columns to include in the vector index. If you
    leave this field blank, all columns from the source table are included. The primary key column
    and embedding source column or embedding vector column are always included. Only one of
    columns_to_sync or columns_to_index may be specified."""

    columns_to_sync: Optional[List[str]] = None
    """[Optional] Select the columns to sync with the vector index. If you leave this field blank, all
    columns from the source table are synced with the index. The primary key column and embedding
    source column or embedding vector column are always synced."""

    embedding_source_columns: Optional[List[EmbeddingSourceColumn]] = None
    """The source table column whose text Databricks embeds, together with the embedding model endpoint
    to use. Set this for an index with Databricks-managed embeddings. Exactly one of
    ``embedding_source_columns`` or ``embedding_vector_columns`` must be specified unless the index
    subtype is ``FULL_TEXT``, and only one column is supported."""

    embedding_vector_columns: Optional[List[EmbeddingVectorColumn]] = None
    """The source table column that contains precomputed embedding vectors. Set this instead of
    ``embedding_source_columns`` for an index with self-managed embeddings."""

    embedding_writeback_table: Optional[str] = None
    """[Optional] Name of the Delta table to sync the vector index contents and computed embeddings to."""

    pipeline_id: Optional[str] = None
    """The ID of the pipeline that is used to sync the index."""

    pipeline_type: Optional[PipelineType] = None
    """Pipeline execution mode.
    
    - ``TRIGGERED``: If the pipeline uses the triggered execution mode, the system stops processing
      after successfully refreshing the source table in the pipeline once, ensuring the table is
      updated based on the data available when the update started.
    - ``CONTINUOUS``: If the pipeline uses continuous execution, the pipeline processes new data as
      it arrives in the source table to keep vector index fresh."""

    source_table: Optional[str] = None
    """Three-level Unity Catalog name of the source table that the index is synced from."""

    def as_dict(self) -> dict:
        """Serializes the DeltaSyncVectorIndexSpecResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.columns_to_index:
            body["columns_to_index"] = [v for v in self.columns_to_index]
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
        """Serializes the DeltaSyncVectorIndexSpecResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.columns_to_index:
            body["columns_to_index"] = self.columns_to_index
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
    def from_dict(cls, d: Dict[str, Any]) -> DeltaSyncVectorIndexSpecResponse:
        """Deserializes the DeltaSyncVectorIndexSpecResponse from a dictionary."""
        return cls(
            columns_to_index=d.get("columns_to_index", None),
            columns_to_sync=d.get("columns_to_sync", None),
            embedding_source_columns=_repeated_dict(d, "embedding_source_columns", EmbeddingSourceColumn),
            embedding_vector_columns=_repeated_dict(d, "embedding_vector_columns", EmbeddingVectorColumn),
            embedding_writeback_table=d.get("embedding_writeback_table", None),
            pipeline_id=d.get("pipeline_id", None),
            pipeline_type=_enum(d, "pipeline_type", PipelineType),
            source_table=d.get("source_table", None),
        )


@dataclass
class DirectAccessVectorIndexSpec:
    embedding_source_columns: Optional[List[EmbeddingSourceColumn]] = None
    """Embedding source configuration used to embed ``query_text`` when the index is queried with text,
    naming the embedding model endpoint to use. The index stores the vectors you supply through
    upsert; this setting never computes embeddings for them."""

    embedding_vector_columns: Optional[List[EmbeddingVectorColumn]] = None
    """The column that holds the embedding vectors you write to the index. Exactly one column must be
    specified, and ``schema_json`` must declare it as ``array<float>`` or ``array<double>``."""

    schema_json: Optional[str] = None
    """JSON object that maps each column name of the index to its type, serialized to a string. The
    primary key and the embedding vector column must be present. Supported types are ``integer``,
    ``long``, ``float``, ``double``, ``boolean``, ``string``, ``date``, ``timestamp``. Supported
    types for vector column: ``array<float>``, ``array<double>``."""

    def as_dict(self) -> dict:
        """Serializes the DirectAccessVectorIndexSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.embedding_source_columns:
            body["embedding_source_columns"] = [v.as_dict() for v in self.embedding_source_columns]
        if self.embedding_vector_columns:
            body["embedding_vector_columns"] = [v.as_dict() for v in self.embedding_vector_columns]
        if self.schema_json is not None:
            body["schema_json"] = self.schema_json
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DirectAccessVectorIndexSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.embedding_source_columns:
            body["embedding_source_columns"] = self.embedding_source_columns
        if self.embedding_vector_columns:
            body["embedding_vector_columns"] = self.embedding_vector_columns
        if self.schema_json is not None:
            body["schema_json"] = self.schema_json
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DirectAccessVectorIndexSpec:
        """Deserializes the DirectAccessVectorIndexSpec from a dictionary."""
        return cls(
            embedding_source_columns=_repeated_dict(d, "embedding_source_columns", EmbeddingSourceColumn),
            embedding_vector_columns=_repeated_dict(d, "embedding_vector_columns", EmbeddingVectorColumn),
            schema_json=d.get("schema_json", None),
        )


@dataclass
class EmbeddingSourceColumn:
    embedding_model_endpoint_name: Optional[str] = None
    """Name of the embedding model endpoint, used by default for both ingestion and querying."""

    model_endpoint_name_for_query: Optional[str] = None
    """Name of the embedding model endpoint which, if specified, is used for querying (not ingestion)."""

    name: Optional[str] = None
    """Name of the column that contains the text to embed."""

    def as_dict(self) -> dict:
        """Serializes the EmbeddingSourceColumn into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.embedding_model_endpoint_name is not None:
            body["embedding_model_endpoint_name"] = self.embedding_model_endpoint_name
        if self.model_endpoint_name_for_query is not None:
            body["model_endpoint_name_for_query"] = self.model_endpoint_name_for_query
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EmbeddingSourceColumn into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.embedding_model_endpoint_name is not None:
            body["embedding_model_endpoint_name"] = self.embedding_model_endpoint_name
        if self.model_endpoint_name_for_query is not None:
            body["model_endpoint_name_for_query"] = self.model_endpoint_name_for_query
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EmbeddingSourceColumn:
        """Deserializes the EmbeddingSourceColumn from a dictionary."""
        return cls(
            embedding_model_endpoint_name=d.get("embedding_model_endpoint_name", None),
            model_endpoint_name_for_query=d.get("model_endpoint_name_for_query", None),
            name=d.get("name", None),
        )


@dataclass
class EmbeddingVectorColumn:
    embedding_dimension: Optional[int] = None
    """Dimension of the embedding vector"""

    name: Optional[str] = None
    """Name of the column that contains the embedding vectors."""

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
class EndpointInfo:
    budget_policy_id: Optional[str] = None
    """The user-selected budget policy id for the endpoint."""

    creation_timestamp: Optional[int] = None
    """Time at which the endpoint was created, in milliseconds since the Unix epoch."""

    creator: Optional[str] = None
    """User or service principal that created the endpoint. Users are identified by username and
    service principals by application ID."""

    custom_tags: Optional[List[CustomTag]] = None
    """The custom tags assigned to the endpoint"""

    effective_budget_policy_id: Optional[str] = None
    """Budget policy ID in effect for the endpoint. This is the policy set on the endpoint when one was
    set, and otherwise the default budget policy."""

    endpoint_status: Optional[EndpointStatus] = None
    """Current status of the endpoint"""

    endpoint_type: Optional[EndpointType] = None
    """Type of the endpoint. See
    https://docs.databricks.com/aws/en/ai-search/ai-search#endpoint-options for how the types
    differ."""

    id: Optional[str] = None
    """Unique identifier of the endpoint"""

    last_updated_timestamp: Optional[int] = None
    """Time at which the endpoint was last updated, in milliseconds since the Unix epoch."""

    last_updated_user: Optional[str] = None
    """User or service principal that last updated the endpoint, in the same form as creator."""

    name: Optional[str] = None
    """Name of the AI Search endpoint"""

    num_indexes: Optional[int] = None
    """Number of indexes on the endpoint"""

    scaling_info: Optional[EndpointScalingInfo] = None
    """Scaling information for the endpoint. Present only for STANDARD endpoints that have a Target QPS
    set."""

    def as_dict(self) -> dict:
        """Serializes the EndpointInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.creation_timestamp is not None:
            body["creation_timestamp"] = self.creation_timestamp
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
        if self.last_updated_timestamp is not None:
            body["last_updated_timestamp"] = self.last_updated_timestamp
        if self.last_updated_user is not None:
            body["last_updated_user"] = self.last_updated_user
        if self.name is not None:
            body["name"] = self.name
        if self.num_indexes is not None:
            body["num_indexes"] = self.num_indexes
        if self.scaling_info:
            body["scaling_info"] = self.scaling_info.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.creation_timestamp is not None:
            body["creation_timestamp"] = self.creation_timestamp
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
        if self.last_updated_timestamp is not None:
            body["last_updated_timestamp"] = self.last_updated_timestamp
        if self.last_updated_user is not None:
            body["last_updated_user"] = self.last_updated_user
        if self.name is not None:
            body["name"] = self.name
        if self.num_indexes is not None:
            body["num_indexes"] = self.num_indexes
        if self.scaling_info:
            body["scaling_info"] = self.scaling_info
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointInfo:
        """Deserializes the EndpointInfo from a dictionary."""
        return cls(
            budget_policy_id=d.get("budget_policy_id", None),
            creation_timestamp=_int64(d, "creation_timestamp"),
            creator=d.get("creator", None),
            custom_tags=_repeated_dict(d, "custom_tags", CustomTag),
            effective_budget_policy_id=d.get("effective_budget_policy_id", None),
            endpoint_status=_from_dict(d, "endpoint_status", EndpointStatus),
            endpoint_type=_enum(d, "endpoint_type", EndpointType),
            id=d.get("id", None),
            last_updated_timestamp=_int64(d, "last_updated_timestamp"),
            last_updated_user=d.get("last_updated_user", None),
            name=d.get("name", None),
            num_indexes=d.get("num_indexes", None),
            scaling_info=_from_dict(d, "scaling_info", EndpointScalingInfo),
        )


@dataclass
class EndpointScalingInfo:
    """Scaling information for a Standard endpoint: the current scaling state, the requested QPS
    target, and the progress of an in-progress scaling change."""

    delayed_reason: Optional[EndpointScalingInfoScalingDelayReason] = None
    """Reason the in-progress scaling change is delayed. When set, ``estimated_completion_timestamp``
    is unset. Unset when the change is not delayed or no scaling change is in progress."""

    estimated_completion_timestamp: Optional[int] = None
    """Estimated time at which the in-progress scaling change will complete, in milliseconds since the
    Unix epoch. The estimate may change as the scaling change progresses. Unset when no scaling
    change is in progress, when no estimate is available, or when the change is delayed (see
    ``delayed_reason``)."""

    index_initialization_percentage: Optional[int] = None
    """Percentage of index initialization completed, from 0 to 100. Set only during the
    ``INITIALIZING_INDEX`` phase; unset in other phases or when progress is not available."""

    phase: Optional[EndpointScalingInfoScalingPhase] = None
    """Current phase of the in-progress scaling change. Unset when no scaling change is in progress or
    the phase is not available."""

    requested_target_qps: Optional[int] = None
    """The requested QPS target for the endpoint. Best-effort; the system does not guarantee this QPS
    will be achieved."""

    state: Optional[ScalingChangeState] = None
    """The current state of the scaling change request."""

    target_qps_change_allowed_after_timestamp: Optional[int] = None
    """Earliest time a new Target QPS change is accepted, in milliseconds since the Unix epoch. Set
    only while a scaling change is in progress, the change lock is on, and the endpoint has a
    recorded last throughput change; may be in the past once the lock has expired."""

    def as_dict(self) -> dict:
        """Serializes the EndpointScalingInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.delayed_reason is not None:
            body["delayed_reason"] = self.delayed_reason.value
        if self.estimated_completion_timestamp is not None:
            body["estimated_completion_timestamp"] = self.estimated_completion_timestamp
        if self.index_initialization_percentage is not None:
            body["index_initialization_percentage"] = self.index_initialization_percentage
        if self.phase is not None:
            body["phase"] = self.phase.value
        if self.requested_target_qps is not None:
            body["requested_target_qps"] = self.requested_target_qps
        if self.state is not None:
            body["state"] = self.state.value
        if self.target_qps_change_allowed_after_timestamp is not None:
            body["target_qps_change_allowed_after_timestamp"] = self.target_qps_change_allowed_after_timestamp
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointScalingInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.delayed_reason is not None:
            body["delayed_reason"] = self.delayed_reason
        if self.estimated_completion_timestamp is not None:
            body["estimated_completion_timestamp"] = self.estimated_completion_timestamp
        if self.index_initialization_percentage is not None:
            body["index_initialization_percentage"] = self.index_initialization_percentage
        if self.phase is not None:
            body["phase"] = self.phase
        if self.requested_target_qps is not None:
            body["requested_target_qps"] = self.requested_target_qps
        if self.state is not None:
            body["state"] = self.state
        if self.target_qps_change_allowed_after_timestamp is not None:
            body["target_qps_change_allowed_after_timestamp"] = self.target_qps_change_allowed_after_timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointScalingInfo:
        """Deserializes the EndpointScalingInfo from a dictionary."""
        return cls(
            delayed_reason=_enum(d, "delayed_reason", EndpointScalingInfoScalingDelayReason),
            estimated_completion_timestamp=_int64(d, "estimated_completion_timestamp"),
            index_initialization_percentage=d.get("index_initialization_percentage", None),
            phase=_enum(d, "phase", EndpointScalingInfoScalingPhase),
            requested_target_qps=_int64(d, "requested_target_qps"),
            state=_enum(d, "state", ScalingChangeState),
            target_qps_change_allowed_after_timestamp=_int64(d, "target_qps_change_allowed_after_timestamp"),
        )


class EndpointScalingInfoScalingDelayReason(Enum):
    """Reason an in-progress scaling change is delayed."""

    CAPACITY_UNAVAILABLE = "CAPACITY_UNAVAILABLE"
    SCALE_DOWN_BLOCKED = "SCALE_DOWN_BLOCKED"
    TAKING_LONGER_THAN_EXPECTED = "TAKING_LONGER_THAN_EXPECTED"


class EndpointScalingInfoScalingPhase(Enum):
    """Phase of an in-progress scaling change."""

    ADJUSTING_CAPACITY = "ADJUSTING_CAPACITY"
    ESTIMATING = "ESTIMATING"
    FINALIZING = "FINALIZING"
    INITIALIZING_INDEX = "INITIALIZING_INDEX"


@dataclass
class EndpointStatus:
    """Status information of an endpoint"""

    message: Optional[str] = None
    """Additional detail about the state, such as the reason the endpoint is OFFLINE. Absent when there
    is nothing to report."""

    state: Optional[EndpointStatusState] = None
    """Current state of the endpoint"""

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
    """Current state of the endpoint"""

    DELETED = "DELETED"
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    PROVISIONING = "PROVISIONING"
    RED_STATE = "RED_STATE"
    STARTING = "STARTING"
    STOPPED = "STOPPED"
    STOPPING = "STOPPING"
    YELLOW_STATE = "YELLOW_STATE"


class EndpointType(Enum):
    """Type of endpoint."""

    STANDARD = "STANDARD"
    STORAGE_OPTIMIZED = "STORAGE_OPTIMIZED"


@dataclass
class FacetResultData:
    """Facet aggregation rows returned by a query."""

    facet_array: Optional[List[List[str]]] = None
    """Facet rows. Each row is ``[facet_column_name, value_or_range, count]``."""

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
class FailedStatus:
    """Failure details for an index or its latest ingestion update."""

    error_code: Optional[str] = None
    """Error code associated with the error message, when available."""

    error_message: Optional[str] = None
    """Error message, when available."""

    last_processed_commit_timestamp: Optional[Timestamp] = None
    """[Standard endpoint] timestamp when the last processed commit was committed to the source table.
    [Storage Optimized endpoint] timestamp when the last processed commit was processed by the
    pipeline."""

    last_processed_commit_version: Optional[int] = None
    """Last source Delta table version fully processed while the index is still queryable."""

    def as_dict(self) -> dict:
        """Serializes the FailedStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.error_code is not None:
            body["error_code"] = self.error_code
        if self.error_message is not None:
            body["error_message"] = self.error_message
        if self.last_processed_commit_timestamp is not None:
            body["last_processed_commit_timestamp"] = self.last_processed_commit_timestamp.ToJsonString()
        if self.last_processed_commit_version is not None:
            body["last_processed_commit_version"] = self.last_processed_commit_version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the FailedStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.error_code is not None:
            body["error_code"] = self.error_code
        if self.error_message is not None:
            body["error_message"] = self.error_message
        if self.last_processed_commit_timestamp is not None:
            body["last_processed_commit_timestamp"] = self.last_processed_commit_timestamp
        if self.last_processed_commit_version is not None:
            body["last_processed_commit_version"] = self.last_processed_commit_version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> FailedStatus:
        """Deserializes the FailedStatus from a dictionary."""
        return cls(
            error_code=d.get("error_code", None),
            error_message=d.get("error_message", None),
            last_processed_commit_timestamp=_timestamp(d, "last_processed_commit_timestamp"),
            last_processed_commit_version=_int64(d, "last_processed_commit_version"),
        )


@dataclass
class GetVectorSearchEndpointPermissionLevelsResponse:
    permission_levels: Optional[List[VectorSearchEndpointPermissionsDescription]] = None
    """Specific permission levels"""

    def as_dict(self) -> dict:
        """Serializes the GetVectorSearchEndpointPermissionLevelsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission_levels:
            body["permission_levels"] = [v.as_dict() for v in self.permission_levels]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GetVectorSearchEndpointPermissionLevelsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.permission_levels:
            body["permission_levels"] = self.permission_levels
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GetVectorSearchEndpointPermissionLevelsResponse:
        """Deserializes the GetVectorSearchEndpointPermissionLevelsResponse from a dictionary."""
        return cls(permission_levels=_repeated_dict(d, "permission_levels", VectorSearchEndpointPermissionsDescription))


class IndexStatus(Enum):
    """Lifecycle and ingestion state of an index."""

    DOWNLOADING = "DOWNLOADING"
    OFFLINE = "OFFLINE"
    OFFLINE_FAILED = "OFFLINE_FAILED"
    ONLINE = "ONLINE"
    ONLINE_CONTINUOUS_UPDATE = "ONLINE_CONTINUOUS_UPDATE"
    ONLINE_DIRECT_ACCESS = "ONLINE_DIRECT_ACCESS"
    ONLINE_NO_PENDING_UPDATE = "ONLINE_NO_PENDING_UPDATE"
    ONLINE_PIPELINE_FAILED = "ONLINE_PIPELINE_FAILED"
    ONLINE_TRIGGERED_UPDATE = "ONLINE_TRIGGERED_UPDATE"
    ONLINE_UPDATING_PIPELINE_RESOURCES = "ONLINE_UPDATING_PIPELINE_RESOURCES"
    PROVISIONING = "PROVISIONING"
    PROVISIONING_ENDPOINT = "PROVISIONING_ENDPOINT"
    PROVISIONING_INDEX = "PROVISIONING_INDEX"
    PROVISIONING_INITIAL_SNAPSHOT = "PROVISIONING_INITIAL_SNAPSHOT"
    PROVISIONING_PIPELINE_RESOURCES = "PROVISIONING_PIPELINE_RESOURCES"


class IndexSubtype(Enum):
    """The subtype of the AI Search index, determining the indexing and retrieval strategy.

    - ``VECTOR``: Not supported. Use ``HYBRID`` instead.
    - ``FULL_TEXT``: An index that uses full-text search without vector embeddings.
    - ``HYBRID``: An index that uses vector embeddings for similarity search and hybrid search."""

    FULL_TEXT = "FULL_TEXT"
    HYBRID = "HYBRID"
    VECTOR = "VECTOR"


@dataclass
class ListEndpointResponse:
    endpoints: Optional[List[EndpointInfo]] = None
    """An array of Endpoint objects"""

    next_page_token: Optional[str] = None
    """A token that can be used to get the next page of results. If not present, there are no more
    results to show."""

    def as_dict(self) -> dict:
        """Serializes the ListEndpointResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.endpoints:
            body["endpoints"] = [v.as_dict() for v in self.endpoints]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListEndpointResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.endpoints:
            body["endpoints"] = self.endpoints
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListEndpointResponse:
        """Deserializes the ListEndpointResponse from a dictionary."""
        return cls(
            endpoints=_repeated_dict(d, "endpoints", EndpointInfo), next_page_token=d.get("next_page_token", None)
        )


@dataclass
class ListValue:
    values: Optional[List[Value]] = None
    """Repeated field of dynamically typed values."""

    def as_dict(self) -> dict:
        """Serializes the ListValue into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.values:
            body["values"] = [v.as_dict() for v in self.values]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListValue into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.values:
            body["values"] = self.values
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListValue:
        """Deserializes the ListValue from a dictionary."""
        return cls(values=_repeated_dict(d, "values", Value))


@dataclass
class ListVectorIndexesResponse:
    next_page_token: Optional[str] = None
    """A token that can be used to get the next page of results. If not present, there are no more
    results to show."""

    vector_indexes: Optional[List[MiniVectorIndex]] = None
    """Indexes served by the endpoint. Each entry is a summary without the index specification and
    status; use Get an index to retrieve them."""

    def as_dict(self) -> dict:
        """Serializes the ListVectorIndexesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.vector_indexes:
            body["vector_indexes"] = [v.as_dict() for v in self.vector_indexes]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListVectorIndexesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.vector_indexes:
            body["vector_indexes"] = self.vector_indexes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListVectorIndexesResponse:
        """Deserializes the ListVectorIndexesResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            vector_indexes=_repeated_dict(d, "vector_indexes", MiniVectorIndex),
        )


@dataclass
class MapStringValueEntry:
    """Key-value pair."""

    key: Optional[str] = None
    """Column name."""

    value: Optional[Value] = None
    """Column value, nullable."""

    def as_dict(self) -> dict:
        """Serializes the MapStringValueEntry into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.key is not None:
            body["key"] = self.key
        if self.value:
            body["value"] = self.value.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MapStringValueEntry into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.key is not None:
            body["key"] = self.key
        if self.value:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> MapStringValueEntry:
        """Deserializes the MapStringValueEntry from a dictionary."""
        return cls(key=d.get("key", None), value=_from_dict(d, "value", Value))


@dataclass
class Metric:
    """Metric specification"""

    labels: Optional[List[MetricLabel]] = None
    """Labels that restrict the metric to matching series, for example to a single index.
    Endpoint-level metrics do not accept labels."""

    name: Optional[str] = None
    """Metric name. Supported metrics include: ``EndpointHealthStatus``, ``EndpointConcurrency``,
    ``IndexRequestCount``, ``IndexRequestLatency``, ``IndexRequestErrorSourceCount``,
    ``IndexRequestGuidanceCount``, ``IndexRequestGuidancePeakRate``, ``IndexIngestedRows``, and
    ``IndexEmbeddedRows``. An unknown name is rejected with an error that lists the available metric
    names."""

    percentile: Optional[float] = None
    """Percentile for latency metrics, such as ``IndexRequestLatency``, which require it. One of 0.5,
    0.75, 0.9, 0.95, or 0.99."""

    def as_dict(self) -> dict:
        """Serializes the Metric into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.labels:
            body["labels"] = [v.as_dict() for v in self.labels]
        if self.name is not None:
            body["name"] = self.name
        if self.percentile is not None:
            body["percentile"] = self.percentile
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Metric into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.labels:
            body["labels"] = self.labels
        if self.name is not None:
            body["name"] = self.name
        if self.percentile is not None:
            body["percentile"] = self.percentile
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Metric:
        """Deserializes the Metric from a dictionary."""
        return cls(
            labels=_repeated_dict(d, "labels", MetricLabel),
            name=d.get("name", None),
            percentile=d.get("percentile", None),
        )


@dataclass
class MetricLabel:
    """Label for a metric"""

    name: Optional[str] = None
    """Label name, such as ``error_source``, ``failure_cause``, ``operation``, ``request_path``,
    ``query_type``, ``response_code``, or ``index_name``. Supported labels depend on the metric."""

    value: Optional[str] = None
    """Label value, as an RE2 regular expression. The label also splits the result by its values, so
    ``.+`` returns one series per value. Some labels, such as ``operation``, accept only ``.+``,
    ``.*``, or listed values joined by ``|``."""

    def as_dict(self) -> dict:
        """Serializes the MetricLabel into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MetricLabel into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> MetricLabel:
        """Deserializes the MetricLabel from a dictionary."""
        return cls(name=d.get("name", None), value=d.get("value", None))


@dataclass
class MetricValue:
    """Single metric value at a specific timestamp"""

    timestamp: Optional[int] = None
    """Timestamp of the metric value, in seconds since the Unix epoch."""

    value: Optional[float] = None
    """Value of the metric at ``timestamp``."""

    def as_dict(self) -> dict:
        """Serializes the MetricValue into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.timestamp is not None:
            body["timestamp"] = self.timestamp
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MetricValue into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.timestamp is not None:
            body["timestamp"] = self.timestamp
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> MetricValue:
        """Deserializes the MetricValue from a dictionary."""
        return cls(timestamp=_int64(d, "timestamp"), value=d.get("value", None))


@dataclass
class MetricValues:
    """Collection of metric values for a specific metric"""

    metric: Optional[Metric] = None
    """The metric this time series was computed for, including the labels that identify the series."""

    values: Optional[List[MetricValue]] = None
    """Each entry is one data point of the time series."""

    def as_dict(self) -> dict:
        """Serializes the MetricValues into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.metric:
            body["metric"] = self.metric.as_dict()
        if self.values:
            body["values"] = [v.as_dict() for v in self.values]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MetricValues into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.metric:
            body["metric"] = self.metric
        if self.values:
            body["values"] = self.values
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> MetricValues:
        """Deserializes the MetricValues from a dictionary."""
        return cls(metric=_from_dict(d, "metric", Metric), values=_repeated_dict(d, "values", MetricValue))


@dataclass
class MiniVectorIndex:
    """An AI Search index stores vectors and metadata on an endpoint and serves vector similarity,
    full-text and hybrid search queries over them. A Delta Sync index is kept in sync with a source
    table, with embeddings either computed by Databricks from a text column or supplied by you in a
    vector column; a Direct Vector Access index holds rows that you write through the upsert and
    delete data APIs. See https://docs.databricks.com/aws/en/ai-search/create-ai-search for how to
    choose between them."""

    creator: Optional[str] = None
    """The user who created the index."""

    endpoint_id: Optional[str] = None
    """ID of the endpoint associated with the index."""

    endpoint_name: Optional[str] = None
    """Name of the endpoint that serves the index."""

    index_subtype: Optional[IndexSubtype] = None
    """Subtype of the index. A ``HYBRID`` index supports vector similarity, full-text and hybrid
    queries; a ``FULL_TEXT`` index has no embeddings and supports only full-text queries."""

    index_type: Optional[VectorIndexType] = None
    """Type of the index, which determines whether ``delta_sync_index_spec`` or
    ``direct_access_index_spec`` describes it."""

    name: Optional[str] = None
    """Three-level Unity Catalog name of the index."""

    primary_key: Optional[str] = None
    """Name of the column that uniquely identifies each row of the index."""

    def as_dict(self) -> dict:
        """Serializes the MiniVectorIndex into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.creator is not None:
            body["creator"] = self.creator
        if self.endpoint_id is not None:
            body["endpoint_id"] = self.endpoint_id
        if self.endpoint_name is not None:
            body["endpoint_name"] = self.endpoint_name
        if self.index_subtype is not None:
            body["index_subtype"] = self.index_subtype.value
        if self.index_type is not None:
            body["index_type"] = self.index_type.value
        if self.name is not None:
            body["name"] = self.name
        if self.primary_key is not None:
            body["primary_key"] = self.primary_key
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MiniVectorIndex into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.creator is not None:
            body["creator"] = self.creator
        if self.endpoint_id is not None:
            body["endpoint_id"] = self.endpoint_id
        if self.endpoint_name is not None:
            body["endpoint_name"] = self.endpoint_name
        if self.index_subtype is not None:
            body["index_subtype"] = self.index_subtype
        if self.index_type is not None:
            body["index_type"] = self.index_type
        if self.name is not None:
            body["name"] = self.name
        if self.primary_key is not None:
            body["primary_key"] = self.primary_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> MiniVectorIndex:
        """Deserializes the MiniVectorIndex from a dictionary."""
        return cls(
            creator=d.get("creator", None),
            endpoint_id=d.get("endpoint_id", None),
            endpoint_name=d.get("endpoint_name", None),
            index_subtype=_enum(d, "index_subtype", IndexSubtype),
            index_type=_enum(d, "index_type", VectorIndexType),
            name=d.get("name", None),
            primary_key=d.get("primary_key", None),
        )


@dataclass
class PatchEndpointBudgetPolicyResponse:
    budget_policy_id: Optional[str] = None
    """The requested budget policy ID, returned when the endpoint was already using it."""

    effective_budget_policy_id: Optional[str] = None
    """The budget policy applied to the AI Search endpoint."""

    def as_dict(self) -> dict:
        """Serializes the PatchEndpointBudgetPolicyResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.effective_budget_policy_id is not None:
            body["effective_budget_policy_id"] = self.effective_budget_policy_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PatchEndpointBudgetPolicyResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.budget_policy_id is not None:
            body["budget_policy_id"] = self.budget_policy_id
        if self.effective_budget_policy_id is not None:
            body["effective_budget_policy_id"] = self.effective_budget_policy_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PatchEndpointBudgetPolicyResponse:
        """Deserializes the PatchEndpointBudgetPolicyResponse from a dictionary."""
        return cls(
            budget_policy_id=d.get("budget_policy_id", None),
            effective_budget_policy_id=d.get("effective_budget_policy_id", None),
        )


class PipelineType(Enum):
    """Pipeline execution mode.

    - ``TRIGGERED``: If the pipeline uses the triggered execution mode, the system stops processing
      after successfully refreshing the source table in the pipeline once, ensuring the table is
      updated based on the data available when the update started.
    - ``CONTINUOUS``: If the pipeline uses continuous execution, the pipeline processes new data as
      it arrives in the source table to keep vector index fresh."""

    CONTINUOUS = "CONTINUOUS"
    TRIGGERED = "TRIGGERED"


@dataclass
class QueryVectorIndexResponse:
    facet_result: Optional[FacetResultData] = None
    """Facet aggregation rows returned by a query."""

    manifest: Optional[ResultManifest] = None
    """Metadata about the result set."""

    next_page_token: Optional[str] = None
    """[Optional] Token that can be used in ``QueryVectorIndexNextPage`` API to get next page of
    results. If more than 1000 results satisfy the query, they are returned in groups of 1000. Empty
    value means no more results. The maximum number of results that can be returned is 10,000."""

    result: Optional[ResultData] = None
    """Data returned in the query result."""

    def as_dict(self) -> dict:
        """Serializes the QueryVectorIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.facet_result:
            body["facet_result"] = self.facet_result.as_dict()
        if self.manifest:
            body["manifest"] = self.manifest.as_dict()
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.result:
            body["result"] = self.result.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the QueryVectorIndexResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.facet_result:
            body["facet_result"] = self.facet_result
        if self.manifest:
            body["manifest"] = self.manifest
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.result:
            body["result"] = self.result
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> QueryVectorIndexResponse:
        """Deserializes the QueryVectorIndexResponse from a dictionary."""
        return cls(
            facet_result=_from_dict(d, "facet_result", FacetResultData),
            manifest=_from_dict(d, "manifest", ResultManifest),
            next_page_token=d.get("next_page_token", None),
            result=_from_dict(d, "result", ResultData),
        )


@dataclass
class RerankerConfig:
    model: Optional[str] = None
    """Reranker identifier:
    
    - When model_type=BASE/UNSPECIFIED: must be "databricks_reranker".
    - When model_type=FINETUNED: the Model Serving endpoint name hosting a finetuned reranker."""

    parameters: Optional[RerankerConfigRerankerParameters] = None
    """Parameters that control how the reranker processes the query results."""

    def as_dict(self) -> dict:
        """Serializes the RerankerConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.model is not None:
            body["model"] = self.model
        if self.parameters:
            body["parameters"] = self.parameters.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RerankerConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.model is not None:
            body["model"] = self.model
        if self.parameters:
            body["parameters"] = self.parameters
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RerankerConfig:
        """Deserializes the RerankerConfig from a dictionary."""
        return cls(model=d.get("model", None), parameters=_from_dict(d, "parameters", RerankerConfigRerankerParameters))


@dataclass
class RerankerConfigRerankerParameters:
    columns_to_rerank: Optional[List[str]] = None
    """Names of the columns whose values are sent to the reranker. List the most relevant column first,
    since the order affects the ranking."""

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
    """Data returned in the query result."""

    data_array: Optional[List[List[str]]] = None
    """Data rows returned in the query."""

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
    """Metadata about the result set."""

    column_count: Optional[int] = None
    """Number of columns in the result set."""

    columns: Optional[List[ColumnInfo]] = None
    """Information about each column in the result set."""

    facet_column_count: Optional[int] = None
    """Number of columns in ``facet_result``."""

    facet_columns: Optional[List[ColumnInfo]] = None
    """Information about each column in ``facet_result``."""

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


@dataclass
class RetrieveUserVisibleMetricsResponse:
    """Response containing user-visible metrics"""

    metric_values: Optional[List[MetricValues]] = None
    """One time series for each requested metric and each combination of label values it was broken
    down by."""

    next_page_token: Optional[str] = None
    """Not set. The response returns all data points in one page."""

    def as_dict(self) -> dict:
        """Serializes the RetrieveUserVisibleMetricsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.metric_values:
            body["metric_values"] = [v.as_dict() for v in self.metric_values]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RetrieveUserVisibleMetricsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.metric_values:
            body["metric_values"] = self.metric_values
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RetrieveUserVisibleMetricsResponse:
        """Deserializes the RetrieveUserVisibleMetricsResponse from a dictionary."""
        return cls(
            metric_values=_repeated_dict(d, "metric_values", MetricValues),
            next_page_token=d.get("next_page_token", None),
        )


class ScalingChangeState(Enum):
    SCALING_CHANGE_APPLIED = "SCALING_CHANGE_APPLIED"
    SCALING_CHANGE_IN_PROGRESS = "SCALING_CHANGE_IN_PROGRESS"
    SCALING_CHANGE_UNSPECIFIED = "SCALING_CHANGE_UNSPECIFIED"


@dataclass
class ScanVectorIndexResponse:
    """Response to a scan vector index request."""

    data: Optional[List[Struct]] = None
    """List of data entries"""

    last_primary_key: Optional[str] = None
    """Primary key of the last entry."""

    def as_dict(self) -> dict:
        """Serializes the ScanVectorIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.data:
            body["data"] = [v.as_dict() for v in self.data]
        if self.last_primary_key is not None:
            body["last_primary_key"] = self.last_primary_key
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ScanVectorIndexResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.data:
            body["data"] = self.data
        if self.last_primary_key is not None:
            body["last_primary_key"] = self.last_primary_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ScanVectorIndexResponse:
        """Deserializes the ScanVectorIndexResponse from a dictionary."""
        return cls(data=_repeated_dict(d, "data", Struct), last_primary_key=d.get("last_primary_key", None))


@dataclass
class Struct:
    fields: Optional[List[MapStringValueEntry]] = None
    """Data entry, corresponding to a row in a vector index."""

    def as_dict(self) -> dict:
        """Serializes the Struct into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.fields:
            body["fields"] = [v.as_dict() for v in self.fields]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Struct into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.fields:
            body["fields"] = self.fields
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Struct:
        """Deserializes the Struct from a dictionary."""
        return cls(fields=_repeated_dict(d, "fields", MapStringValueEntry))


@dataclass
class SyncIndexResponse:
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


@dataclass
class UpdateEndpointCustomTagsResponse:
    custom_tags: Optional[List[CustomTag]] = None
    """All the custom tags that are applied to the AI Search endpoint."""

    name: Optional[str] = None
    """The name of the AI Search endpoint whose custom tags were updated."""

    def as_dict(self) -> dict:
        """Serializes the UpdateEndpointCustomTagsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.custom_tags:
            body["custom_tags"] = [v.as_dict() for v in self.custom_tags]
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UpdateEndpointCustomTagsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.custom_tags:
            body["custom_tags"] = self.custom_tags
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UpdateEndpointCustomTagsResponse:
        """Deserializes the UpdateEndpointCustomTagsResponse from a dictionary."""
        return cls(custom_tags=_repeated_dict(d, "custom_tags", CustomTag), name=d.get("name", None))


@dataclass
class UpsertDataResult:
    failed_primary_keys: Optional[List[str]] = None
    """List of primary keys for rows that failed to process."""

    success_row_count: Optional[int] = None
    """Count of successfully processed rows."""

    def as_dict(self) -> dict:
        """Serializes the UpsertDataResult into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.failed_primary_keys:
            body["failed_primary_keys"] = [v for v in self.failed_primary_keys]
        if self.success_row_count is not None:
            body["success_row_count"] = self.success_row_count
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UpsertDataResult into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.failed_primary_keys:
            body["failed_primary_keys"] = self.failed_primary_keys
        if self.success_row_count is not None:
            body["success_row_count"] = self.success_row_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UpsertDataResult:
        """Deserializes the UpsertDataResult from a dictionary."""
        return cls(
            failed_primary_keys=d.get("failed_primary_keys", None), success_row_count=_int64(d, "success_row_count")
        )


class UpsertDataStatus(Enum):
    FAILURE = "FAILURE"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    SUCCESS = "SUCCESS"


@dataclass
class UpsertDataVectorIndexResponse:
    result: Optional[UpsertDataResult] = None
    """Result of the upsert or delete operation."""

    status: Optional[UpsertDataStatus] = None
    """Status of the upsert operation."""

    def as_dict(self) -> dict:
        """Serializes the UpsertDataVectorIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.result:
            body["result"] = self.result.as_dict()
        if self.status is not None:
            body["status"] = self.status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UpsertDataVectorIndexResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.result:
            body["result"] = self.result
        if self.status is not None:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UpsertDataVectorIndexResponse:
        """Deserializes the UpsertDataVectorIndexResponse from a dictionary."""
        return cls(result=_from_dict(d, "result", UpsertDataResult), status=_enum(d, "status", UpsertDataStatus))


@dataclass
class Value:
    bool_value: Optional[bool] = None

    list_value: Optional[ListValue] = None

    number_value: Optional[float] = None

    string_value: Optional[str] = None

    struct_value: Optional[Struct] = None

    def as_dict(self) -> dict:
        """Serializes the Value into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.bool_value is not None:
            body["bool_value"] = self.bool_value
        if self.list_value:
            body["list_value"] = self.list_value.as_dict()
        if self.number_value is not None:
            body["number_value"] = self.number_value
        if self.string_value is not None:
            body["string_value"] = self.string_value
        if self.struct_value:
            body["struct_value"] = self.struct_value.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Value into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.bool_value is not None:
            body["bool_value"] = self.bool_value
        if self.list_value:
            body["list_value"] = self.list_value
        if self.number_value is not None:
            body["number_value"] = self.number_value
        if self.string_value is not None:
            body["string_value"] = self.string_value
        if self.struct_value:
            body["struct_value"] = self.struct_value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Value:
        """Deserializes the Value from a dictionary."""
        return cls(
            bool_value=d.get("bool_value", None),
            list_value=_from_dict(d, "list_value", ListValue),
            number_value=d.get("number_value", None),
            string_value=d.get("string_value", None),
            struct_value=_from_dict(d, "struct_value", Struct),
        )


@dataclass
class VectorIndex:
    """An AI Search index stores vectors and metadata on an endpoint and serves vector similarity,
    full-text and hybrid search queries over them. A Delta Sync index is kept in sync with a source
    table, with embeddings either computed by Databricks from a text column or supplied by you in a
    vector column; a Direct Vector Access index holds rows that you write through the upsert and
    delete data APIs. See https://docs.databricks.com/aws/en/ai-search/create-ai-search for how to
    choose between them."""

    creator: Optional[str] = None
    """The user who created the index."""

    delta_sync_index_spec: Optional[DeltaSyncVectorIndexSpecResponse] = None
    """Specification of a Delta Sync index. Present only when ``index_type`` is ``DELTA_SYNC``."""

    direct_access_index_spec: Optional[DirectAccessVectorIndexSpec] = None
    """Specification of a Direct Vector Access index. Present only when ``index_type`` is
    ``DIRECT_ACCESS``."""

    endpoint_id: Optional[str] = None
    """ID of the endpoint associated with the index."""

    endpoint_name: Optional[str] = None
    """Name of the endpoint that serves the index."""

    index_subtype: Optional[IndexSubtype] = None
    """Subtype of the index. A ``HYBRID`` index supports vector similarity, full-text and hybrid
    queries; a ``FULL_TEXT`` index has no embeddings and supports only full-text queries."""

    index_type: Optional[VectorIndexType] = None
    """Type of the index, which determines whether ``delta_sync_index_spec`` or
    ``direct_access_index_spec`` describes it."""

    name: Optional[str] = None
    """Three-level Unity Catalog name of the index."""

    primary_key: Optional[str] = None
    """Name of the column that uniquely identifies each row of the index."""

    status: Optional[VectorIndexStatus] = None
    """Current status of the index, including whether it is ready to serve queries and how many rows it
    holds."""

    def as_dict(self) -> dict:
        """Serializes the VectorIndex into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.creator is not None:
            body["creator"] = self.creator
        if self.delta_sync_index_spec:
            body["delta_sync_index_spec"] = self.delta_sync_index_spec.as_dict()
        if self.direct_access_index_spec:
            body["direct_access_index_spec"] = self.direct_access_index_spec.as_dict()
        if self.endpoint_id is not None:
            body["endpoint_id"] = self.endpoint_id
        if self.endpoint_name is not None:
            body["endpoint_name"] = self.endpoint_name
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
        """Serializes the VectorIndex into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.creator is not None:
            body["creator"] = self.creator
        if self.delta_sync_index_spec:
            body["delta_sync_index_spec"] = self.delta_sync_index_spec
        if self.direct_access_index_spec:
            body["direct_access_index_spec"] = self.direct_access_index_spec
        if self.endpoint_id is not None:
            body["endpoint_id"] = self.endpoint_id
        if self.endpoint_name is not None:
            body["endpoint_name"] = self.endpoint_name
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
    def from_dict(cls, d: Dict[str, Any]) -> VectorIndex:
        """Deserializes the VectorIndex from a dictionary."""
        return cls(
            creator=d.get("creator", None),
            delta_sync_index_spec=_from_dict(d, "delta_sync_index_spec", DeltaSyncVectorIndexSpecResponse),
            direct_access_index_spec=_from_dict(d, "direct_access_index_spec", DirectAccessVectorIndexSpec),
            endpoint_id=d.get("endpoint_id", None),
            endpoint_name=d.get("endpoint_name", None),
            index_subtype=_enum(d, "index_subtype", IndexSubtype),
            index_type=_enum(d, "index_type", VectorIndexType),
            name=d.get("name", None),
            primary_key=d.get("primary_key", None),
            status=_from_dict(d, "status", VectorIndexStatus),
        )


@dataclass
class VectorIndexStatus:
    detailed_state: Optional[IndexStatus] = None
    """Lifecycle and ingestion state. An online index can still have a failed update."""

    failed_status: Optional[FailedStatus] = None
    """Failure details, when available, for OFFLINE_FAILED or ONLINE_PIPELINE_FAILED."""

    index_url: Optional[str] = None
    """Index API Url to be used to perform operations on the index"""

    indexed_row_count: Optional[int] = None
    """Number of rows indexed"""

    message: Optional[str] = None
    """Human-readable description of the current status."""

    ready: Optional[bool] = None
    """Whether the index can serve queries. This does not mean the latest update succeeded or that all
    source-table changes have been indexed; check detailed_state for update failures."""

    def as_dict(self) -> dict:
        """Serializes the VectorIndexStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.detailed_state is not None:
            body["detailed_state"] = self.detailed_state.value
        if self.failed_status:
            body["failed_status"] = self.failed_status.as_dict()
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
        """Serializes the VectorIndexStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.detailed_state is not None:
            body["detailed_state"] = self.detailed_state
        if self.failed_status:
            body["failed_status"] = self.failed_status
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
    def from_dict(cls, d: Dict[str, Any]) -> VectorIndexStatus:
        """Deserializes the VectorIndexStatus from a dictionary."""
        return cls(
            detailed_state=_enum(d, "detailed_state", IndexStatus),
            failed_status=_from_dict(d, "failed_status", FailedStatus),
            index_url=d.get("index_url", None),
            indexed_row_count=_int64(d, "indexed_row_count"),
            message=d.get("message", None),
            ready=d.get("ready", None),
        )


class VectorIndexType(Enum):
    """There are 2 types of AI Search indexes:

    - ``DELTA_SYNC``: An index that automatically syncs with a source Delta Table, automatically and
      incrementally updating the index as the underlying data in the Delta Table changes.
    - ``DIRECT_ACCESS``: An index that supports direct read and write of vectors and metadata
      through our REST and SDK APIs. With this model, the user manages index updates."""

    DELTA_SYNC = "DELTA_SYNC"
    DIRECT_ACCESS = "DIRECT_ACCESS"


@dataclass
class VectorSearchEndpointAccessControlRequest:
    group_name: Optional[str] = None
    """name of the group"""

    permission_level: Optional[VectorSearchEndpointPermissionLevel] = None

    service_principal_name: Optional[str] = None
    """application ID of a service principal"""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the VectorSearchEndpointAccessControlRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level.value
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.user_name is not None:
            body["user_name"] = self.user_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the VectorSearchEndpointAccessControlRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.user_name is not None:
            body["user_name"] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> VectorSearchEndpointAccessControlRequest:
        """Deserializes the VectorSearchEndpointAccessControlRequest from a dictionary."""
        return cls(
            group_name=d.get("group_name", None),
            permission_level=_enum(d, "permission_level", VectorSearchEndpointPermissionLevel),
            service_principal_name=d.get("service_principal_name", None),
            user_name=d.get("user_name", None),
        )


@dataclass
class VectorSearchEndpointAccessControlResponse:
    all_permissions: Optional[List[VectorSearchEndpointPermission]] = None
    """All permissions."""

    display_name: Optional[str] = None
    """Display name of the user or service principal."""

    group_name: Optional[str] = None
    """name of the group"""

    service_principal_name: Optional[str] = None
    """Name of the service principal."""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the VectorSearchEndpointAccessControlResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.all_permissions:
            body["all_permissions"] = [v.as_dict() for v in self.all_permissions]
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.user_name is not None:
            body["user_name"] = self.user_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the VectorSearchEndpointAccessControlResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.all_permissions:
            body["all_permissions"] = self.all_permissions
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.user_name is not None:
            body["user_name"] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> VectorSearchEndpointAccessControlResponse:
        """Deserializes the VectorSearchEndpointAccessControlResponse from a dictionary."""
        return cls(
            all_permissions=_repeated_dict(d, "all_permissions", VectorSearchEndpointPermission),
            display_name=d.get("display_name", None),
            group_name=d.get("group_name", None),
            service_principal_name=d.get("service_principal_name", None),
            user_name=d.get("user_name", None),
        )


@dataclass
class VectorSearchEndpointPermission:
    inherited: Optional[bool] = None

    inherited_from_object: Optional[List[str]] = None

    permission_level: Optional[VectorSearchEndpointPermissionLevel] = None

    def as_dict(self) -> dict:
        """Serializes the VectorSearchEndpointPermission into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.inherited is not None:
            body["inherited"] = self.inherited
        if self.inherited_from_object:
            body["inherited_from_object"] = [v for v in self.inherited_from_object]
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the VectorSearchEndpointPermission into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.inherited is not None:
            body["inherited"] = self.inherited
        if self.inherited_from_object:
            body["inherited_from_object"] = self.inherited_from_object
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> VectorSearchEndpointPermission:
        """Deserializes the VectorSearchEndpointPermission from a dictionary."""
        return cls(
            inherited=d.get("inherited", None),
            inherited_from_object=d.get("inherited_from_object", None),
            permission_level=_enum(d, "permission_level", VectorSearchEndpointPermissionLevel),
        )


class VectorSearchEndpointPermissionLevel(Enum):
    """Permission level"""

    CAN_CREATE = "CAN_CREATE"
    CAN_MANAGE = "CAN_MANAGE"
    CAN_USE = "CAN_USE"


@dataclass
class VectorSearchEndpointPermissions:
    access_control_list: Optional[List[VectorSearchEndpointAccessControlResponse]] = None

    object_id: Optional[str] = None

    object_type: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the VectorSearchEndpointPermissions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body["access_control_list"] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None:
            body["object_id"] = self.object_id
        if self.object_type is not None:
            body["object_type"] = self.object_type
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the VectorSearchEndpointPermissions into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.access_control_list:
            body["access_control_list"] = self.access_control_list
        if self.object_id is not None:
            body["object_id"] = self.object_id
        if self.object_type is not None:
            body["object_type"] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> VectorSearchEndpointPermissions:
        """Deserializes the VectorSearchEndpointPermissions from a dictionary."""
        return cls(
            access_control_list=_repeated_dict(d, "access_control_list", VectorSearchEndpointAccessControlResponse),
            object_id=d.get("object_id", None),
            object_type=d.get("object_type", None),
        )


@dataclass
class VectorSearchEndpointPermissionsDescription:
    description: Optional[str] = None

    permission_level: Optional[VectorSearchEndpointPermissionLevel] = None

    def as_dict(self) -> dict:
        """Serializes the VectorSearchEndpointPermissionsDescription into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the VectorSearchEndpointPermissionsDescription into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> VectorSearchEndpointPermissionsDescription:
        """Deserializes the VectorSearchEndpointPermissionsDescription from a dictionary."""
        return cls(
            description=d.get("description", None),
            permission_level=_enum(d, "permission_level", VectorSearchEndpointPermissionLevel),
        )


class VectorSearchEndpointsAPI:
    """**Endpoint**: Represents the compute resources to host AI Search indexes."""

    def __init__(self, api_client):
        self._api = api_client

    def wait_get_endpoint_vector_search_endpoint_online(
        self,
        endpoint_name: str,
        timeout=timedelta(minutes=20),
        callback: Optional[Callable[[EndpointInfo], None]] = None,
    ) -> EndpointInfo:
        deadline = time.time() + timeout.total_seconds()
        target_states = (EndpointStatusState.ONLINE,)
        failure_states = (EndpointStatusState.OFFLINE,)
        status_message = "polling..."
        attempt = 1
        while time.time() < deadline:
            poll = self.get_endpoint(endpoint_name=endpoint_name)
            status = poll.endpoint_status.state
            status_message = f"current status: {status}"
            if poll.endpoint_status:
                status_message = poll.endpoint_status.message
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f"failed to reach ONLINE, got {status}: {status_message}"
                raise OperationFailed(msg)
            prefix = f"endpoint_name={endpoint_name}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f"{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)")
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f"timed out after {timeout}: {status_message}")

    def create_endpoint(
        self,
        name: str,
        endpoint_type: EndpointType,
        *,
        budget_policy_id: Optional[str] = None,
        target_qps: Optional[int] = None,
        usage_policy_id: Optional[str] = None,
    ) -> Wait[EndpointInfo]:
        """Create a new endpoint.

        :param name: str
          Name of the AI Search endpoint. The name must be unique within the workspace, have at most 50
          characters, contain only lowercase letters, digits, hyphens, underscores and periods, and start and
          end with a letter or digit.
        :param endpoint_type: :class:`EndpointType`
          Type of endpoint to create. STANDARD endpoints are optimized for low-latency queries and support
          Target QPS scaling. STORAGE_OPTIMIZED endpoints hold much larger indexes and index faster, with
          higher query latency. See https://docs.databricks.com/aws/en/ai-search/ai-search#endpoint-options.
        :param budget_policy_id: str (optional)
          Budget policy to attribute the endpoint's usage to. If omitted, the default budget policy applies.
        :param target_qps: int (optional)
          Target queries per second (QPS) for the endpoint. Supported for STANDARD endpoints only. The actual
          replica count is calculated at index creation/sync time based on this value. Best-effort target; the
          system does not guarantee this QPS will be achieved.
        :param usage_policy_id: str (optional)
          The usage policy id to be applied once we've migrated to usage policies

        :returns:
          Long-running operation waiter for :class:`EndpointInfo`.
          See :method:wait_get_endpoint_vector_search_endpoint_online for more details.
        """

        body = {}
        if budget_policy_id is not None:
            body["budget_policy_id"] = budget_policy_id
        if endpoint_type is not None:
            body["endpoint_type"] = endpoint_type.value
        if name is not None:
            body["name"] = name
        if target_qps is not None:
            body["target_qps"] = target_qps
        if usage_policy_id is not None:
            body["usage_policy_id"] = usage_policy_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        op_response = self._api.do("POST", "/api/2.0/vector-search/endpoints", body=body, headers=headers)
        return Wait(
            self.wait_get_endpoint_vector_search_endpoint_online,
            response=EndpointInfo.from_dict(op_response),
            endpoint_name=op_response["name"],
        )

    def create_endpoint_and_wait(
        self,
        name: str,
        endpoint_type: EndpointType,
        *,
        budget_policy_id: Optional[str] = None,
        target_qps: Optional[int] = None,
        usage_policy_id: Optional[str] = None,
        timeout=timedelta(minutes=20),
    ) -> EndpointInfo:
        return self.create_endpoint(
            budget_policy_id=budget_policy_id,
            endpoint_type=endpoint_type,
            name=name,
            target_qps=target_qps,
            usage_policy_id=usage_policy_id,
        ).result(timeout=timeout)

    def delete_endpoint(self, endpoint_name: str):
        """Delete an AI Search endpoint.

        :param endpoint_name: str
          Name of the AI Search endpoint


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/vector-search/endpoints/{endpoint_name}", headers=headers)

    def get_endpoint(self, endpoint_name: str) -> EndpointInfo:
        """Get details for a single AI Search endpoint.

        :param endpoint_name: str
          Name of the endpoint

        :returns: :class:`EndpointInfo`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/vector-search/endpoints/{endpoint_name}", headers=headers)
        return EndpointInfo.from_dict(res)

    def get_permission_levels(self, endpoint_id: str) -> GetVectorSearchEndpointPermissionLevelsResponse:
        """Gets the permission levels that a user can have on an object.

        :param endpoint_id: str
          The vector search endpoint for which to get or manage permissions.

        :returns: :class:`GetVectorSearchEndpointPermissionLevelsResponse`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "GET", f"/api/2.0/permissions/vector-search-endpoints/{endpoint_id}/permissionLevels", headers=headers
        )
        return GetVectorSearchEndpointPermissionLevelsResponse.from_dict(res)

    def get_permissions(self, endpoint_id: str) -> VectorSearchEndpointPermissions:
        """Gets the permissions of a vector search endpoint. Vector search endpoints can inherit permissions from
        their root object.

        :param endpoint_id: str
          The vector search endpoint for which to get or manage permissions.

        :returns: :class:`VectorSearchEndpointPermissions`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/permissions/vector-search-endpoints/{endpoint_id}", headers=headers)
        return VectorSearchEndpointPermissions.from_dict(res)

    def list_endpoints(self, *, page_token: Optional[str] = None) -> Iterator[EndpointInfo]:
        """List all AI Search endpoints in the workspace.

        :param page_token: str (optional)
          Token for pagination

        :returns: Iterator over :class:`EndpointInfo`
        """

        query = {}
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.0/vector-search/endpoints", query=query, headers=headers)
            if "endpoints" in json:
                for v in json["endpoints"]:
                    yield EndpointInfo.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def patch_endpoint(self, endpoint_name: str, *, target_qps: Optional[int] = None) -> EndpointInfo:
        """Update the Target QPS of a STANDARD endpoint. The response is the updated endpoint; its scaling_info
        shows whether the resulting scaling change is applied or still in progress.

        :param endpoint_name: str
          Name of the AI Search endpoint
        :param target_qps: int (optional)
          Target QPS for the endpoint. Best-effort; the system does not guarantee this QPS will be achieved.
          Set to -1 to clear the Target QPS, as if it had never been set.

        :returns: :class:`EndpointInfo`
        """

        body = {}
        if target_qps is not None:
            body["target_qps"] = target_qps
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/vector-search/endpoints/{endpoint_name}", body=body, headers=headers)
        return EndpointInfo.from_dict(res)

    def retrieve_user_visible_metrics(
        self,
        name: str,
        *,
        end_time: Optional[str] = None,
        granularity_in_seconds: Optional[int] = None,
        metrics: Optional[List[Metric]] = None,
        page_token: Optional[str] = None,
        start_time: Optional[str] = None,
    ) -> RetrieveUserVisibleMetricsResponse:
        """Retrieve time series of usage and health metrics for an endpoint and its indexes, such as request
        counts, request latency percentiles and endpoint utilization.

        :param name: str
          Name of the endpoint whose metrics to retrieve.
        :param end_time: str (optional)
          End of the time range. Defaults to the current time. Must be later than ``start_time``.
        :param granularity_in_seconds: int (optional)
          Requested interval between data points, in seconds. Defaults to 60, which is also the minimum. The
          server may return a finer or coarser interval: 60 seconds only for time ranges of 1 hour or less,
          otherwise 300 seconds or more. Read the interval from the returned timestamps.
        :param metrics: List[:class:`Metric`] (optional)
          Metrics to retrieve. Each entry names a metric and optionally narrows it with labels or a
          percentile. An unknown metric name fails the whole request, and an empty list returns no series.
        :param page_token: str (optional)
          Not used. The response returns all data points in one page.
        :param start_time: str (optional)
          Start of the time range. Required. Must be within the last 169 hours.

        :returns: :class:`RetrieveUserVisibleMetricsResponse`
        """

        body = {}
        if end_time is not None:
            body["end_time"] = end_time
        if granularity_in_seconds is not None:
            body["granularity_in_seconds"] = granularity_in_seconds
        if metrics is not None:
            body["metrics"] = [v.as_dict() for v in metrics]
        if page_token is not None:
            body["page_token"] = page_token
        if start_time is not None:
            body["start_time"] = start_time
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/vector-search/endpoints/{name}/metrics", body=body, headers=headers)
        return RetrieveUserVisibleMetricsResponse.from_dict(res)

    def set_permissions(
        self, endpoint_id: str, *, access_control_list: Optional[List[VectorSearchEndpointAccessControlRequest]] = None
    ) -> VectorSearchEndpointPermissions:
        """Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct
        permissions if none are specified. Objects can inherit permissions from their root object.

        :param endpoint_id: str
          The vector search endpoint for which to get or manage permissions.
        :param access_control_list: List[:class:`VectorSearchEndpointAccessControlRequest`] (optional)

        :returns: :class:`VectorSearchEndpointPermissions`
        """

        body = {}
        if access_control_list is not None:
            body["access_control_list"] = [v.as_dict() for v in access_control_list]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "PUT", f"/api/2.0/permissions/vector-search-endpoints/{endpoint_id}", body=body, headers=headers
        )
        return VectorSearchEndpointPermissions.from_dict(res)

    def start_endpoint(self, endpoint_name: str) -> EndpointInfo:
        """Start a stopped endpoint. The endpoint serves the same indexes it had when it stopped.

        :param endpoint_name: str
          Name of the AI Search endpoint

        :returns: :class:`EndpointInfo`
        """

        body = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "POST", f"/api/2.0/vector-search/endpoints/{endpoint_name}/start", body=body, headers=headers
        )
        return EndpointInfo.from_dict(res)

    def stop_endpoint(self, endpoint_name: str) -> EndpointInfo:
        """Stop an endpoint. Stopping removes the endpoint's serving compute and retains its indexes. A stopped
        endpoint can't serve queries or sync indexes until it is started.

        :param endpoint_name: str
          Name of the AI Search endpoint

        :returns: :class:`EndpointInfo`
        """

        body = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/vector-search/endpoints/{endpoint_name}/stop", body=body, headers=headers)
        return EndpointInfo.from_dict(res)

    def update_endpoint_budget_policy(
        self, endpoint_name: str, budget_policy_id: str
    ) -> PatchEndpointBudgetPolicyResponse:
        """Update the budget policy that the endpoint's usage is attributed to.

        :param endpoint_name: str
          Name of the AI Search endpoint
        :param budget_policy_id: str
          The budget policy id to be applied

        :returns: :class:`PatchEndpointBudgetPolicyResponse`
        """

        body = {}
        if budget_policy_id is not None:
            body["budget_policy_id"] = budget_policy_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "PATCH", f"/api/2.0/vector-search/endpoints/{endpoint_name}/budget-policy", body=body, headers=headers
        )
        return PatchEndpointBudgetPolicyResponse.from_dict(res)

    def update_endpoint_custom_tags(
        self, endpoint_name: str, custom_tags: List[CustomTag]
    ) -> UpdateEndpointCustomTagsResponse:
        """Update the custom tags of an endpoint.

        :param endpoint_name: str
          Name of the AI Search endpoint
        :param custom_tags: List[:class:`CustomTag`]
          The new custom tags for the AI Search endpoint

        :returns: :class:`UpdateEndpointCustomTagsResponse`
        """

        body = {}
        if custom_tags is not None:
            body["custom_tags"] = [v.as_dict() for v in custom_tags]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "PATCH", f"/api/2.0/vector-search/endpoints/{endpoint_name}/tags", body=body, headers=headers
        )
        return UpdateEndpointCustomTagsResponse.from_dict(res)

    def update_permissions(
        self, endpoint_id: str, *, access_control_list: Optional[List[VectorSearchEndpointAccessControlRequest]] = None
    ) -> VectorSearchEndpointPermissions:
        """Updates the permissions on a vector search endpoint. Vector search endpoints can inherit permissions
        from their root object.

        :param endpoint_id: str
          The vector search endpoint for which to get or manage permissions.
        :param access_control_list: List[:class:`VectorSearchEndpointAccessControlRequest`] (optional)

        :returns: :class:`VectorSearchEndpointPermissions`
        """

        body = {}
        if access_control_list is not None:
            body["access_control_list"] = [v.as_dict() for v in access_control_list]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "PATCH", f"/api/2.0/permissions/vector-search-endpoints/{endpoint_id}", body=body, headers=headers
        )
        return VectorSearchEndpointPermissions.from_dict(res)


class VectorSearchIndexesAPI:
    """**Index**: An efficient representation of your embedding vectors that supports real-time and efficient
    approximate nearest neighbor (ANN) search queries.

    There are 2 types of AI Search indexes:

    - **Delta Sync Index**: An index that automatically syncs with a source Delta Table, automatically and
      incrementally updating the index as the underlying data in the Delta Table changes.
    - **Direct Vector Access Index**: An index that supports direct read and write of vectors and metadata
      through our REST and SDK APIs. With this model, the user manages index updates."""

    def __init__(self, api_client):
        self._api = api_client

    def create_index(
        self,
        name: str,
        endpoint_name: str,
        primary_key: str,
        index_type: VectorIndexType,
        *,
        delta_sync_index_spec: Optional[DeltaSyncVectorIndexSpecRequest] = None,
        direct_access_index_spec: Optional[DirectAccessVectorIndexSpec] = None,
        index_subtype: Optional[IndexSubtype] = None,
    ) -> VectorIndex:
        """Create a new index on an endpoint. Creating a Delta Sync index also creates the pipeline that
        populates it from the source table; a Direct Vector Access index starts empty and is populated through
        Upsert data into an index.

        :param name: str
          Three-level Unity Catalog name of the index to create.
        :param endpoint_name: str
          Name of the endpoint to be used for serving the index
        :param primary_key: str
          Name of the column that uniquely identifies each row. For a Delta Sync index it is a column of the
          source table; for a Direct Vector Access index it must be declared in ``schema_json``. It cannot be
          the embedding source or embedding vector column.
        :param index_type: :class:`VectorIndexType`
          Type of index to create, which determines which spec field is required.
        :param delta_sync_index_spec: :class:`DeltaSyncVectorIndexSpecRequest` (optional)
          Specification for Delta Sync Index. Required if ``index_type`` is ``DELTA_SYNC``.
        :param direct_access_index_spec: :class:`DirectAccessVectorIndexSpec` (optional)
          Specification for Direct Vector Access Index. Required if ``index_type`` is ``DIRECT_ACCESS``.
        :param index_subtype: :class:`IndexSubtype` (optional)
          The subtype of the index. Use ``HYBRID`` or ``FULL_TEXT``. ``VECTOR`` is not supported.

        :returns: :class:`VectorIndex`
        """

        body = {}
        if delta_sync_index_spec is not None:
            body["delta_sync_index_spec"] = delta_sync_index_spec.as_dict()
        if direct_access_index_spec is not None:
            body["direct_access_index_spec"] = direct_access_index_spec.as_dict()
        if endpoint_name is not None:
            body["endpoint_name"] = endpoint_name
        if index_subtype is not None:
            body["index_subtype"] = index_subtype.value
        if index_type is not None:
            body["index_type"] = index_type.value
        if name is not None:
            body["name"] = name
        if primary_key is not None:
            body["primary_key"] = primary_key
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/vector-search/indexes", body=body, headers=headers)
        return VectorIndex.from_dict(res)

    def delete_data_vector_index(self, index_name: str, primary_keys: List[str]) -> DeleteDataVectorIndexResponse:
        """Delete rows from a Direct Vector Access index by primary key. The response reports how many rows were
        deleted and the primary keys of the rows that failed.

        :param index_name: str
          Name of the vector index where data is to be deleted. Must be a Direct Vector Access Index.
        :param primary_keys: List[str]
          Primary keys of the rows to delete. At least one key is required.

        :returns: :class:`DeleteDataVectorIndexResponse`
        """

        query = {}
        if primary_keys is not None:
            query["primary_keys"] = [v for v in primary_keys]
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "DELETE", f"/api/2.0/vector-search/indexes/{index_name}/delete-data", query=query, headers=headers
        )
        return DeleteDataVectorIndexResponse.from_dict(res)

    def delete_index(self, index_name: str):
        """Delete an index and the data it holds. The source table of a Delta Sync index is not affected.

        :param index_name: str
          Three-level Unity Catalog name of the index.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/vector-search/indexes/{index_name}", headers=headers)

    def get_index(self, index_name: str, *, ensure_reranker_compatible: Optional[bool] = None) -> VectorIndex:
        """Get an index.

        :param index_name: str
          Three-level Unity Catalog name of the index.
        :param ensure_reranker_compatible: bool (optional)
          If true, the URL returned for the index is guaranteed to be compatible with the reranker. Currently
          this means we return the CP URL regardless of how the index is being accessed. If not set or set to
          false, the URL may still be compatible with the reranker depending on what URL we return.

        :returns: :class:`VectorIndex`
        """

        query = {}
        if ensure_reranker_compatible is not None:
            query["ensure_reranker_compatible"] = ensure_reranker_compatible
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/vector-search/indexes/{index_name}", query=query, headers=headers)
        return VectorIndex.from_dict(res)

    def list_indexes(self, endpoint_name: str, *, page_token: Optional[str] = None) -> Iterator[MiniVectorIndex]:
        """List all indexes in the given endpoint.

        :param endpoint_name: str
          Name of the endpoint whose indexes to list.
        :param page_token: str (optional)
          Page token returned by a previous call, used to get the next page of results.

        :returns: Iterator over :class:`MiniVectorIndex`
        """

        query = {}
        if endpoint_name is not None:
            query["endpoint_name"] = endpoint_name
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.0/vector-search/indexes", query=query, headers=headers)
            if "vector_indexes" in json:
                for v in json["vector_indexes"]:
                    yield MiniVectorIndex.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def query_index(
        self,
        index_name: str,
        columns: List[str],
        *,
        columns_to_rerank: Optional[List[str]] = None,
        facets: Optional[List[str]] = None,
        filters_json: Optional[str] = None,
        num_results: Optional[int] = None,
        query_columns: Optional[List[str]] = None,
        query_text: Optional[str] = None,
        query_type: Optional[str] = None,
        query_vector: Optional[List[float]] = None,
        reranker: Optional[RerankerConfig] = None,
        score_threshold: Optional[float] = None,
        sort_columns: Optional[List[str]] = None,
    ) -> QueryVectorIndexResponse:
        """Query an index with a vector, text, or both, and return the requested columns of the best-matching
        rows.

        :param index_name: str
          Name of the vector index to query.
        :param columns: List[str]
          Names of the columns to return for each result. At least one column is required, and only columns
          that are part of the index can be returned.
        :param columns_to_rerank: List[str] (optional)
          Column names used to retrieve data to send to the reranker.
        :param facets: List[str] (optional)
          Facets to compute over the matched results. Each entry has one of these forms: ``"<column>"`` - top
          10 distinct values by count ``"<column> TOP <n>"`` - top n distinct values, where n > 0 ``"<column>
          BUCKETS [[from,to],...]"`` - inclusive numeric ranges ``TOP`` and ``BUCKETS`` are case-insensitive.
          A column may appear at most once.
        :param filters_json: str (optional)
          Filters to apply to the results, as a JSON object serialized to a string. Each key is a column name,
          optionally followed by a space and an operator, and each value is the value or list of values to
          compare the column against. A key without an operator matches the value exactly, or any of the
          listed values. Supported operators are ``NOT``, ``<``, ``<=``, ``>``, ``>=``, ``OR`` and ``LIKE``;
          see https://docs.databricks.com/aws/en/ai-search/query-ai-search for their semantics. This field is
          not supported on storage-optimized endpoints.
        :param num_results: int (optional)
          Maximum number of results to return. It must be greater than 0 and defaults to 10. By default, a
          ``HYBRID`` query can return at most 200 results.
        :param query_columns: List[str] (optional)
          Text columns to search for ``query_text``. When empty, all text columns are searched.
        :param query_text: str (optional)
          Text to search for. Use it for an index with Databricks-managed embeddings, which embeds the text
          with the index's embedding model endpoint, and for ``FULL_TEXT`` queries on any index. A ``HYBRID``
          query on an index with managed embeddings requires only ``query_text``.
        :param query_type: str (optional)
          The query type to use. Choices are ``ANN`` and ``HYBRID`` and ``FULL_TEXT``. Defaults to ``ANN``.
        :param query_vector: List[float] (optional)
          Embedding vector to search for. Use it for an index whose embeddings you compute yourself: a Direct
          Vector Access index or a Delta Sync index with ``embedding_vector_columns``. A ``HYBRID`` query on a
          Delta Sync index with ``embedding_vector_columns``, or on a Direct Vector Access index without
          ``embedding_source_columns``, requires both ``query_vector`` and ``query_text``. A Direct Vector
          Access index with ``embedding_source_columns`` can be queried with ``query_text`` alone.
        :param reranker: :class:`RerankerConfig` (optional)
          If set, the top 50 results are reranked with the Databricks Reranker model before returning the
          ``num_results`` results to the user. The setting ``columns_to_rerank`` selects which columns are
          used for reranking. For each datapoint, the columns selected are concatenated before being sent to
          the reranking model. See https://docs.databricks.com/aws/en/vector-search/query-vector-search#rerank
          for more information.
        :param score_threshold: float (optional)
          Threshold for the approximate nearest neighbor search. Defaults to 0.0.
        :param sort_columns: List[str] (optional)
          Sort results by column values instead of the default relevance ordering. Each clause has the form
          ``"<column> ASC"`` or ``"<column> DESC"``, for example ``["rating DESC", "price ASC"]``.

        :returns: :class:`QueryVectorIndexResponse`
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
        if num_results is not None:
            body["num_results"] = num_results
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

        res = self._api.do("POST", f"/api/2.0/vector-search/indexes/{index_name}/query", body=body, headers=headers)
        return QueryVectorIndexResponse.from_dict(res)

    def query_next_page(
        self, index_name: str, *, endpoint_name: Optional[str] = None, page_token: Optional[str] = None
    ) -> QueryVectorIndexResponse:
        """Use ``next_page_token`` returned from previous ``QueryVectorIndex`` or ``QueryVectorIndexNextPage``
        request to fetch next page of results.

        :param index_name: str
          Name of the vector index to query.
        :param endpoint_name: str (optional)
          Name of the endpoint that serves the index.
        :param page_token: str (optional)
          Page token returned from previous ``QueryVectorIndex`` or ``QueryVectorIndexNextPage`` API.

        :returns: :class:`QueryVectorIndexResponse`
        """

        body = {}
        if endpoint_name is not None:
            body["endpoint_name"] = endpoint_name
        if page_token is not None:
            body["page_token"] = page_token
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "POST", f"/api/2.0/vector-search/indexes/{index_name}/query-next-page", body=body, headers=headers
        )
        return QueryVectorIndexResponse.from_dict(res)

    def scan_index(
        self, index_name: str, *, last_primary_key: Optional[str] = None, num_results: Optional[int] = None
    ) -> ScanVectorIndexResponse:
        """Scan an index and return the first ``num_results`` rows after the exclusive ``last_primary_key``.
        Repeat the call with the returned ``last_primary_key`` to read the whole index.

        :param index_name: str
          Name of the vector index to scan.
        :param last_primary_key: str (optional)
          Primary key of the last entry returned in the previous scan.
        :param num_results: int (optional)
          Number of results to return. Defaults to 10.

        :returns: :class:`ScanVectorIndexResponse`
        """

        body = {}
        if last_primary_key is not None:
            body["last_primary_key"] = last_primary_key
        if num_results is not None:
            body["num_results"] = num_results
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/vector-search/indexes/{index_name}/scan", body=body, headers=headers)
        return ScanVectorIndexResponse.from_dict(res)

    def sync_index(self, index_name: str):
        """Start a sync of a Delta Sync index with a ``TRIGGERED`` pipeline from its source table. An index with
        a ``CONTINUOUS`` pipeline syncs automatically and rejects manual syncs.

        :param index_name: str
          Name of the vector index to synchronize. Must be a Delta Sync Index.


        """

        body = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("POST", f"/api/2.0/vector-search/indexes/{index_name}/sync", body=body, headers=headers)

    def upsert_data_vector_index(self, index_name: str, inputs_json: str) -> UpsertDataVectorIndexResponse:
        """Insert rows into a Direct Vector Access index, replacing existing rows that have the same primary key.
        The response reports how many rows succeeded and the primary keys of the rows that failed.

        :param index_name: str
          Name of the vector index where data is to be upserted. Must be a Direct Vector Access Index.
        :param inputs_json: str
          Rows to upsert, as a JSON array of objects serialized to a string. Each object maps column names
          from ``schema_json`` to values and must include the primary key. A row whose primary key already
          exists in the index is replaced.

        :returns: :class:`UpsertDataVectorIndexResponse`
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

        res = self._api.do(
            "POST", f"/api/2.0/vector-search/indexes/{index_name}/upsert-data", body=body, headers=headers
        )
        return UpsertDataVectorIndexResponse.from_dict(res)

# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.
# ruff: noqa: F811, F841
# F401 is intentionally NOT covered: `make fmt` uses `ruff check --fix-only`
# to strip the fat-import header below; ignoring F401 would defeat that.

from __future__ import annotations
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Dict, List, Any, Iterator, Callable, Optional


import time
import random
import logging

from ..errors import OperationFailed
from databricks.sdk.service._internal import (
    _enum,
    _from_dict,
    _repeated_dict,
    Wait,
)


_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class AdjustedThroughputRequest:
    """Adjusted throughput request parameters"""

    concurrency: Optional[float] = None
    """Adjusted concurrency (total CPU) for the endpoint"""

    maximum_concurrency_allowed: Optional[float] = None
    """Adjusted maximum concurrency allowed for the endpoint"""

    minimal_concurrency_allowed: Optional[float] = None
    """Adjusted minimum concurrency allowed for the endpoint"""

    def as_dict(self) -> dict:
        """Serializes the AdjustedThroughputRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.concurrency is not None:
            body["concurrency"] = self.concurrency
        if self.maximum_concurrency_allowed is not None:
            body["maximum_concurrency_allowed"] = self.maximum_concurrency_allowed
        if self.minimal_concurrency_allowed is not None:
            body["minimal_concurrency_allowed"] = self.minimal_concurrency_allowed
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AdjustedThroughputRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.concurrency is not None:
            body["concurrency"] = self.concurrency
        if self.maximum_concurrency_allowed is not None:
            body["maximum_concurrency_allowed"] = self.maximum_concurrency_allowed
        if self.minimal_concurrency_allowed is not None:
            body["minimal_concurrency_allowed"] = self.minimal_concurrency_allowed
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AdjustedThroughputRequest:
        """Deserializes the AdjustedThroughputRequest from a dictionary."""
        return cls(
            concurrency=d.get("concurrency", None),
            maximum_concurrency_allowed=d.get("maximum_concurrency_allowed", None),
            minimal_concurrency_allowed=d.get("minimal_concurrency_allowed", None),
        )


class AutoEvalDisplayStatus(Enum):
    AUTO_EVAL_DISPLAY_STATUS_FAILED = "AUTO_EVAL_DISPLAY_STATUS_FAILED"
    AUTO_EVAL_DISPLAY_STATUS_PENDING = "AUTO_EVAL_DISPLAY_STATUS_PENDING"
    AUTO_EVAL_DISPLAY_STATUS_RUNNING = "AUTO_EVAL_DISPLAY_STATUS_RUNNING"
    AUTO_EVAL_DISPLAY_STATUS_SUCCEEDED = "AUTO_EVAL_DISPLAY_STATUS_SUCCEEDED"


@dataclass
class AutoEvalJob:
    """State of the most recent autoeval Databricks Jobs background-compute run for an index. The UI
    uses this to render the staged progress bar."""

    current_stage: Optional[AutoEvalStage] = None
    """Pipeline stage currently in progress."""

    dashboard_url: Optional[str] = None
    """Lakeview dashboard URL for the latest run's results."""

    metrics_table_full_name: Optional[str] = None
    """Fully qualified Delta table name where per-run metrics are persisted
    (``autoeval_metrics_<index>``)."""

    mlflow_experiment_id: Optional[str] = None
    """MLflow experiment_id used by the autoeval wheel. Stable per index. The UI uses this to construct
    an "Open in MLflow" deep link without an additional MLflow tag fetch."""

    mlflow_run_id: Optional[str] = None
    """MLflow run_id of the latest autoeval run. Per-run, latest only."""

    overall_progress: Optional[float] = None
    """Overall progress across all stages, in the range [0.0, 1.0]. Capped at 0.99 while the run is
    RUNNING — the bar only reaches 1.0 when status flips to AUTO_EVAL_DISPLAY_STATUS_SUCCEEDED."""

    progress_on_current_stage: Optional[int] = None
    """Items completed within the current stage (e.g., queries generated, (query_type, reranker, phase)
    tuples evaluated, results saved)."""

    results_table_full_name: Optional[str] = None
    """Fully qualified Delta table name where per-query results are persisted
    (``autoeval_results_<index>``)."""

    total_for_current_stage: Optional[int] = None
    """Total items expected within the current stage."""

    def as_dict(self) -> dict:
        """Serializes the AutoEvalJob into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.current_stage is not None:
            body["current_stage"] = self.current_stage.value
        if self.dashboard_url is not None:
            body["dashboard_url"] = self.dashboard_url
        if self.metrics_table_full_name is not None:
            body["metrics_table_full_name"] = self.metrics_table_full_name
        if self.mlflow_experiment_id is not None:
            body["mlflow_experiment_id"] = self.mlflow_experiment_id
        if self.mlflow_run_id is not None:
            body["mlflow_run_id"] = self.mlflow_run_id
        if self.overall_progress is not None:
            body["overall_progress"] = self.overall_progress
        if self.progress_on_current_stage is not None:
            body["progress_on_current_stage"] = self.progress_on_current_stage
        if self.results_table_full_name is not None:
            body["results_table_full_name"] = self.results_table_full_name
        if self.total_for_current_stage is not None:
            body["total_for_current_stage"] = self.total_for_current_stage
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AutoEvalJob into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.current_stage is not None:
            body["current_stage"] = self.current_stage
        if self.dashboard_url is not None:
            body["dashboard_url"] = self.dashboard_url
        if self.metrics_table_full_name is not None:
            body["metrics_table_full_name"] = self.metrics_table_full_name
        if self.mlflow_experiment_id is not None:
            body["mlflow_experiment_id"] = self.mlflow_experiment_id
        if self.mlflow_run_id is not None:
            body["mlflow_run_id"] = self.mlflow_run_id
        if self.overall_progress is not None:
            body["overall_progress"] = self.overall_progress
        if self.progress_on_current_stage is not None:
            body["progress_on_current_stage"] = self.progress_on_current_stage
        if self.results_table_full_name is not None:
            body["results_table_full_name"] = self.results_table_full_name
        if self.total_for_current_stage is not None:
            body["total_for_current_stage"] = self.total_for_current_stage
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AutoEvalJob:
        """Deserializes the AutoEvalJob from a dictionary."""
        return cls(
            current_stage=_enum(d, "current_stage", AutoEvalStage),
            dashboard_url=d.get("dashboard_url", None),
            metrics_table_full_name=d.get("metrics_table_full_name", None),
            mlflow_experiment_id=d.get("mlflow_experiment_id", None),
            mlflow_run_id=d.get("mlflow_run_id", None),
            overall_progress=d.get("overall_progress", None),
            progress_on_current_stage=d.get("progress_on_current_stage", None),
            results_table_full_name=d.get("results_table_full_name", None),
            total_for_current_stage=d.get("total_for_current_stage", None),
        )


class AutoEvalStage(Enum):
    """Pipeline stages within a single autoeval run, in execution order. Used together with AutoEvalJob
    to drive a staged progress bar in the UI."""

    AUTO_EVAL_STAGE_FEW_SHOT_QUERIES = "AUTO_EVAL_STAGE_FEW_SHOT_QUERIES"
    AUTO_EVAL_STAGE_GENERATE_QUERIES = "AUTO_EVAL_STAGE_GENERATE_QUERIES"
    AUTO_EVAL_STAGE_GENERATE_RESULTS = "AUTO_EVAL_STAGE_GENERATE_RESULTS"
    AUTO_EVAL_STAGE_METRICS_COMPUTATION = "AUTO_EVAL_STAGE_METRICS_COMPUTATION"


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
            failed_primary_keys=d.get("failed_primary_keys", None), success_row_count=d.get("success_row_count", None)
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

    effective_budget_policy_id: Optional[str] = None
    """The budget policy id applied to the AI Search index"""

    effective_usage_policy_id: Optional[str] = None

    embedding_source_columns: Optional[List[EmbeddingSourceColumn]] = None
    """The columns that contain the embedding source."""

    embedding_vector_columns: Optional[List[EmbeddingVectorColumn]] = None
    """The columns that contain the embedding vectors."""

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
    """The name of the source table."""

    def as_dict(self) -> dict:
        """Serializes the DeltaSyncVectorIndexSpecRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.columns_to_index:
            body["columns_to_index"] = [v for v in self.columns_to_index]
        if self.columns_to_sync:
            body["columns_to_sync"] = [v for v in self.columns_to_sync]
        if self.effective_budget_policy_id is not None:
            body["effective_budget_policy_id"] = self.effective_budget_policy_id
        if self.effective_usage_policy_id is not None:
            body["effective_usage_policy_id"] = self.effective_usage_policy_id
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
        if self.effective_budget_policy_id is not None:
            body["effective_budget_policy_id"] = self.effective_budget_policy_id
        if self.effective_usage_policy_id is not None:
            body["effective_usage_policy_id"] = self.effective_usage_policy_id
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
            effective_budget_policy_id=d.get("effective_budget_policy_id", None),
            effective_usage_policy_id=d.get("effective_usage_policy_id", None),
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

    effective_budget_policy_id: Optional[str] = None
    """The budget policy id applied to the AI Search index"""

    effective_usage_policy_id: Optional[str] = None

    embedding_source_columns: Optional[List[EmbeddingSourceColumn]] = None
    """The columns that contain the embedding source."""

    embedding_vector_columns: Optional[List[EmbeddingVectorColumn]] = None
    """The columns that contain the embedding vectors."""

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
    """The name of the source table."""

    def as_dict(self) -> dict:
        """Serializes the DeltaSyncVectorIndexSpecResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.columns_to_index:
            body["columns_to_index"] = [v for v in self.columns_to_index]
        if self.columns_to_sync:
            body["columns_to_sync"] = [v for v in self.columns_to_sync]
        if self.effective_budget_policy_id is not None:
            body["effective_budget_policy_id"] = self.effective_budget_policy_id
        if self.effective_usage_policy_id is not None:
            body["effective_usage_policy_id"] = self.effective_usage_policy_id
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
        if self.effective_budget_policy_id is not None:
            body["effective_budget_policy_id"] = self.effective_budget_policy_id
        if self.effective_usage_policy_id is not None:
            body["effective_usage_policy_id"] = self.effective_usage_policy_id
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
            effective_budget_policy_id=d.get("effective_budget_policy_id", None),
            effective_usage_policy_id=d.get("effective_usage_policy_id", None),
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
    """The columns that contain the embedding source. The format should be array[double]."""

    embedding_vector_columns: Optional[List[EmbeddingVectorColumn]] = None
    """The columns that contain the embedding vectors. The format should be array[double]."""

    requested_schema_json: Optional[str] = None
    """The index schema exactly as the user supplied it on create, preserving the original type
    spellings (e.g. ``integer``) rather than Unity Catalog's canonical names (e.g. ``int``) that
    ``schema_json`` returns."""

    schema_json: Optional[str] = None
    """The schema of the index in JSON format. Supported types are ``integer``, ``long``, ``float``,
    ``double``, ``boolean``, ``string``, ``date``, ``timestamp``. Supported types for vector column:
    ``array<float>``, ``array<double>``,`."""

    def as_dict(self) -> dict:
        """Serializes the DirectAccessVectorIndexSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.embedding_source_columns:
            body["embedding_source_columns"] = [v.as_dict() for v in self.embedding_source_columns]
        if self.embedding_vector_columns:
            body["embedding_vector_columns"] = [v.as_dict() for v in self.embedding_vector_columns]
        if self.requested_schema_json is not None:
            body["requested_schema_json"] = self.requested_schema_json
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
        if self.requested_schema_json is not None:
            body["requested_schema_json"] = self.requested_schema_json
        if self.schema_json is not None:
            body["schema_json"] = self.schema_json
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DirectAccessVectorIndexSpec:
        """Deserializes the DirectAccessVectorIndexSpec from a dictionary."""
        return cls(
            embedding_source_columns=_repeated_dict(d, "embedding_source_columns", EmbeddingSourceColumn),
            embedding_vector_columns=_repeated_dict(d, "embedding_vector_columns", EmbeddingVectorColumn),
            requested_schema_json=d.get("requested_schema_json", None),
            schema_json=d.get("schema_json", None),
        )


@dataclass
class EmbeddingSourceColumn:
    embedding_model_endpoint_name: Optional[str] = None
    """Name of the embedding model endpoint, used by default for both ingestion and querying."""

    model_endpoint_name_for_query: Optional[str] = None
    """Name of the embedding model endpoint which, if specified, is used for querying (not ingestion)."""

    name: Optional[str] = None
    """Name of the column"""

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
    """Name of the column"""

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
    """Timestamp of endpoint creation"""

    creator: Optional[str] = None
    """Creator of the endpoint"""

    custom_tags: Optional[List[CustomTag]] = None
    """The custom tags assigned to the endpoint"""

    effective_budget_policy_id: Optional[str] = None
    """The budget policy id applied to the endpoint"""

    endpoint_status: Optional[EndpointStatus] = None
    """Current status of the endpoint"""

    endpoint_type: Optional[EndpointType] = None
    """Type of endpoint"""

    id: Optional[str] = None
    """Unique identifier of the endpoint"""

    last_updated_timestamp: Optional[int] = None
    """Timestamp of last update to the endpoint"""

    last_updated_user: Optional[str] = None
    """User who last updated the endpoint"""

    name: Optional[str] = None
    """Name of the AI Search endpoint"""

    num_indexes: Optional[int] = None
    """Number of indexes on the endpoint"""

    scaling_info: Optional[EndpointScalingInfo] = None
    """Scaling information for the endpoint"""

    throughput_info: Optional[EndpointThroughputInfo] = None
    """Throughput information for the endpoint"""

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
        if self.throughput_info:
            body["throughput_info"] = self.throughput_info.as_dict()
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
        if self.throughput_info:
            body["throughput_info"] = self.throughput_info
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> EndpointInfo:
        """Deserializes the EndpointInfo from a dictionary."""
        return cls(
            budget_policy_id=d.get("budget_policy_id", None),
            creation_timestamp=d.get("creation_timestamp", None),
            creator=d.get("creator", None),
            custom_tags=_repeated_dict(d, "custom_tags", CustomTag),
            effective_budget_policy_id=d.get("effective_budget_policy_id", None),
            endpoint_status=_from_dict(d, "endpoint_status", EndpointStatus),
            endpoint_type=_enum(d, "endpoint_type", EndpointType),
            id=d.get("id", None),
            last_updated_timestamp=d.get("last_updated_timestamp", None),
            last_updated_user=d.get("last_updated_user", None),
            name=d.get("name", None),
            num_indexes=d.get("num_indexes", None),
            scaling_info=_from_dict(d, "scaling_info", EndpointScalingInfo),
            throughput_info=_from_dict(d, "throughput_info", EndpointThroughputInfo),
        )


@dataclass
class EndpointScalingInfo:
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
    """Status information of an endpoint"""

    message: Optional[str] = None
    """Additional status message"""

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
    YELLOW_STATE = "YELLOW_STATE"


@dataclass
class EndpointThroughputInfo:
    """Throughput information for an endpoint"""

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
class GetAutoEvalStatusResponse:
    end_time_ms: Optional[int] = None
    """Wall-clock end time of the latest run, in milliseconds since epoch. Unset until the run reaches
    a terminal state."""

    job_id: Optional[str] = None
    """Databricks Jobs job_id of the autoeval background-compute job for this index, so the UI can
    surface a link to the job. Unset when no autoeval job exists for the index yet."""

    latest_run: Optional[AutoEvalJob] = None
    """State of the latest autoeval run, including stage progress. Populated only while status is
    AUTO_EVAL_DISPLAY_STATUS_RUNNING and the running wheel has reported at least one stage update.
    Absent for terminal states."""

    run_as_user: Optional[str] = None
    """The user the latest job run was created as. Used by the UI to construct the per-run MLflow
    dashboard URL."""

    state_message: Optional[str] = None
    """Free-form failure copy from the underlying job. Populated only when status is
    AUTO_EVAL_DISPLAY_STATUS_FAILED. Capped server-side to bound payload size when the job emits
    long stack traces."""

    status: Optional[AutoEvalDisplayStatus] = None
    """Current display status of the latest autoeval run."""

    def as_dict(self) -> dict:
        """Serializes the GetAutoEvalStatusResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.end_time_ms is not None:
            body["end_time_ms"] = self.end_time_ms
        if self.job_id is not None:
            body["job_id"] = self.job_id
        if self.latest_run:
            body["latest_run"] = self.latest_run.as_dict()
        if self.run_as_user is not None:
            body["run_as_user"] = self.run_as_user
        if self.state_message is not None:
            body["state_message"] = self.state_message
        if self.status is not None:
            body["status"] = self.status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GetAutoEvalStatusResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.end_time_ms is not None:
            body["end_time_ms"] = self.end_time_ms
        if self.job_id is not None:
            body["job_id"] = self.job_id
        if self.latest_run:
            body["latest_run"] = self.latest_run
        if self.run_as_user is not None:
            body["run_as_user"] = self.run_as_user
        if self.state_message is not None:
            body["state_message"] = self.state_message
        if self.status is not None:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GetAutoEvalStatusResponse:
        """Deserializes the GetAutoEvalStatusResponse from a dictionary."""
        return cls(
            end_time_ms=d.get("end_time_ms", None),
            job_id=d.get("job_id", None),
            latest_run=_from_dict(d, "latest_run", AutoEvalJob),
            run_as_user=d.get("run_as_user", None),
            state_message=d.get("state_message", None),
            status=_enum(d, "status", AutoEvalDisplayStatus),
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
    """Metric labels"""

    name: Optional[str] = None
    """Metric name"""

    percentile: Optional[float] = None
    """Percentile for the metric"""

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
    """Label name"""

    value: Optional[str] = None
    """Label value"""

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
    """Timestamp of the metric value (milliseconds since epoch)"""

    value: Optional[float] = None
    """Metric value"""

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
        return cls(timestamp=d.get("timestamp", None), value=d.get("value", None))


@dataclass
class MetricValues:
    """Collection of metric values for a specific metric"""

    metric: Optional[Metric] = None
    """Metric specification"""

    values: Optional[List[MetricValue]] = None
    """Time series of metric values"""

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
    creator: Optional[str] = None
    """The user who created the index."""

    endpoint_id: Optional[str] = None
    """ID of the endpoint associated with the index."""

    endpoint_name: Optional[str] = None
    """Name of the endpoint associated with the index"""

    index_subtype: Optional[IndexSubtype] = None
    """The subtype of the index."""

    index_type: Optional[VectorIndexType] = None

    name: Optional[str] = None
    """Name of the index"""

    primary_key: Optional[str] = None
    """Primary key of the index"""

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


@dataclass
class PatchEndpointThroughputResponse:
    adjusted_request: Optional[AdjustedThroughputRequest] = None
    """The adjusted request if the original request could not be fully fulfilled. This is only
    populated when the request was adjusted."""

    message: Optional[str] = None
    """Message explaining the status or any adjustments made"""

    status: Optional[ThroughputPatchStatus] = None
    """The status of the throughput change request"""

    def as_dict(self) -> dict:
        """Serializes the PatchEndpointThroughputResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.adjusted_request:
            body["adjusted_request"] = self.adjusted_request.as_dict()
        if self.message is not None:
            body["message"] = self.message
        if self.status is not None:
            body["status"] = self.status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PatchEndpointThroughputResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.adjusted_request:
            body["adjusted_request"] = self.adjusted_request
        if self.message is not None:
            body["message"] = self.message
        if self.status is not None:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PatchEndpointThroughputResponse:
        """Deserializes the PatchEndpointThroughputResponse from a dictionary."""
        return cls(
            adjusted_request=_from_dict(d, "adjusted_request", AdjustedThroughputRequest),
            message=d.get("message", None),
            status=_enum(d, "status", ThroughputPatchStatus),
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

    model_type: Optional[RerankerConfigModelType] = None
    """EXPERIMENTAL. Discriminator for how the ``model`` field is interpreted: BASE/UNSPECIFIED expects
    the literal "databricks_reranker"; FINETUNED treats ``model`` as a Model Serving endpoint name
    in the caller's workspace. See the doc comment on ``model`` for the per-case contract."""

    parameters: Optional[RerankerConfigRerankerParameters] = None
    """Parameters that control how the reranker processes the query results."""

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
    """EXPERIMENTAL. Selects how ``model`` is interpreted."""

    MODEL_TYPE_BASE = "MODEL_TYPE_BASE"
    MODEL_TYPE_FINETUNED = "MODEL_TYPE_FINETUNED"


@dataclass
class RerankerConfigRerankerParameters:
    columns_to_rerank: Optional[List[str]] = None

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

    total_hit_count: Optional[int] = None
    """Documents matching the query, independent of num_results (which bounds ``row_count``). A lower
    bound once matches exceed the per-shard counting threshold. Unset unless doc count is enabled."""

    total_hit_count_lower_bound: Optional[bool] = None
    """True when total_hit_count is a lower bound (the match count exceeded the counting threshold)
    rather than the exact total. Unset unless doc count is enabled."""

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
        if self.total_hit_count is not None:
            body["total_hit_count"] = self.total_hit_count
        if self.total_hit_count_lower_bound is not None:
            body["total_hit_count_lower_bound"] = self.total_hit_count_lower_bound
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
        if self.total_hit_count is not None:
            body["total_hit_count"] = self.total_hit_count
        if self.total_hit_count_lower_bound is not None:
            body["total_hit_count_lower_bound"] = self.total_hit_count_lower_bound
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResultManifest:
        """Deserializes the ResultManifest from a dictionary."""
        return cls(
            column_count=d.get("column_count", None),
            columns=_repeated_dict(d, "columns", ColumnInfo),
            facet_column_count=d.get("facet_column_count", None),
            facet_columns=_repeated_dict(d, "facet_columns", ColumnInfo),
            total_hit_count=d.get("total_hit_count", None),
            total_hit_count_lower_bound=d.get("total_hit_count_lower_bound", None),
        )


@dataclass
class RetrieveUserVisibleMetricsResponse:
    """Response containing user-visible metrics"""

    metric_values: Optional[List[MetricValues]] = None
    """Collection of metric values"""

    next_page_token: Optional[str] = None
    """A token that can be used to get the next page of results. If not present, there are no more
    results to show."""

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


@dataclass
class RunAutoEvalResponse:
    def as_dict(self) -> dict:
        """Serializes the RunAutoEvalResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RunAutoEvalResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RunAutoEvalResponse:
        """Deserializes the RunAutoEvalResponse from a dictionary."""
        return cls()


@dataclass
class RunRerankerFinetuningResponse:
    def as_dict(self) -> dict:
        """Serializes the RunRerankerFinetuningResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RunRerankerFinetuningResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RunRerankerFinetuningResponse:
        """Deserializes the RunRerankerFinetuningResponse from a dictionary."""
        return cls()


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


class ThroughputChangeRequestState(Enum):
    """Throughput change request state"""

    CHANGE_ADJUSTED = "CHANGE_ADJUSTED"
    CHANGE_FAILED = "CHANGE_FAILED"
    CHANGE_IN_PROGRESS = "CHANGE_IN_PROGRESS"
    CHANGE_REACHED_MAXIMUM = "CHANGE_REACHED_MAXIMUM"
    CHANGE_REACHED_MINIMUM = "CHANGE_REACHED_MINIMUM"
    CHANGE_SUCCESS = "CHANGE_SUCCESS"


class ThroughputPatchStatus(Enum):
    """Response status for throughput change requests"""

    PATCH_ACCEPTED = "PATCH_ACCEPTED"
    PATCH_FAILED = "PATCH_FAILED"
    PATCH_REJECTED = "PATCH_REJECTED"


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
class UpdateVectorIndexUsagePolicyResponse:
    effective_usage_policy_id: Optional[str] = None
    """The effective usage policy id applied to the AI Search index"""

    usage_policy_id: Optional[str] = None
    """The updated usage policy id"""

    def as_dict(self) -> dict:
        """Serializes the UpdateVectorIndexUsagePolicyResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.effective_usage_policy_id is not None:
            body["effective_usage_policy_id"] = self.effective_usage_policy_id
        if self.usage_policy_id is not None:
            body["usage_policy_id"] = self.usage_policy_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UpdateVectorIndexUsagePolicyResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.effective_usage_policy_id is not None:
            body["effective_usage_policy_id"] = self.effective_usage_policy_id
        if self.usage_policy_id is not None:
            body["usage_policy_id"] = self.usage_policy_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UpdateVectorIndexUsagePolicyResponse:
        """Deserializes the UpdateVectorIndexUsagePolicyResponse from a dictionary."""
        return cls(
            effective_usage_policy_id=d.get("effective_usage_policy_id", None),
            usage_policy_id=d.get("usage_policy_id", None),
        )


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
            failed_primary_keys=d.get("failed_primary_keys", None), success_row_count=d.get("success_row_count", None)
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
    creator: Optional[str] = None
    """The user who created the index."""

    delta_sync_index_spec: Optional[DeltaSyncVectorIndexSpecResponse] = None

    direct_access_index_spec: Optional[DirectAccessVectorIndexSpec] = None

    endpoint_id: Optional[str] = None
    """ID of the endpoint associated with the index."""

    endpoint_name: Optional[str] = None
    """Name of the endpoint associated with the index"""

    index_subtype: Optional[IndexSubtype] = None
    """The subtype of the index."""

    index_type: Optional[VectorIndexType] = None

    name: Optional[str] = None
    """Name of the index"""

    primary_key: Optional[str] = None
    """Primary key of the index"""

    status: Optional[VectorIndexStatus] = None

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
    index_url: Optional[str] = None
    """Index API Url to be used to perform operations on the index"""

    indexed_row_count: Optional[int] = None
    """Number of rows indexed"""

    message: Optional[str] = None
    """Message associated with the index status"""

    ready: Optional[bool] = None
    """Whether the index is ready for search"""

    def as_dict(self) -> dict:
        """Serializes the VectorIndexStatus into a dictionary suitable for use as a JSON request body."""
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
        """Serializes the VectorIndexStatus into a shallow dictionary of its immediate attributes."""
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
    def from_dict(cls, d: Dict[str, Any]) -> VectorIndexStatus:
        """Deserializes the VectorIndexStatus from a dictionary."""
        return cls(
            index_url=d.get("index_url", None),
            indexed_row_count=d.get("indexed_row_count", None),
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
        num_replicas: Optional[int] = None,
        target_qps: Optional[int] = None,
        usage_policy_id: Optional[str] = None,
    ) -> Wait[EndpointInfo]:
        """Create a new endpoint.

        :param name: str
          Name of the AI Search endpoint
        :param endpoint_type: :class:`EndpointType`
          Type of endpoint
        :param budget_policy_id: str (optional)
          The budget policy id to be applied
        :param num_replicas: int (optional)
          Initial number of replicas for the endpoint. If not specified, defaults to 1.
        :param target_qps: int (optional)
          Target QPS for the endpoint. Mutually exclusive with num_replicas. The actual replica count is
          calculated at index creation/sync time based on this value. Best-effort target; the system does not
          guarantee this QPS will be achieved.
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
        if num_replicas is not None:
            body["num_replicas"] = num_replicas
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
        num_replicas: Optional[int] = None,
        target_qps: Optional[int] = None,
        usage_policy_id: Optional[str] = None,
        timeout=timedelta(minutes=20),
    ) -> EndpointInfo:
        return self.create_endpoint(
            budget_policy_id=budget_policy_id,
            endpoint_type=endpoint_type,
            name=name,
            num_replicas=num_replicas,
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

    def patch_endpoint(
        self, endpoint_name: str, *, replication_factor: Optional[int] = None, target_qps: Optional[int] = None
    ) -> EndpointInfo:
        """Update an endpoint

        :param endpoint_name: str
          Name of the AI Search endpoint
        :param replication_factor: int (optional)
          OpenSearch replication factor. Directly sets userThroughputSettings.replicationFactor. Mutually
          exclusive with target_qps (and the deprecated min_qps alias). Must be non-negative (0 = no
          replication). The autoscaler caps the effective value based on endpoint scaling settings. Note: This
          is the raw replication factor, not "total data copies". For the user-facing replica count (which
          uses total-copies semantics), see PatchEndpointThroughputRequest.num_replicas.
        :param target_qps: int (optional)
          Target QPS for the endpoint. Best-effort; the system does not guarantee this QPS will be achieved.

        :returns: :class:`EndpointInfo`
        """

        body = {}
        if replication_factor is not None:
            body["replication_factor"] = replication_factor
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

    def patch_endpoint_throughput(
        self,
        endpoint_name: str,
        *,
        all_or_nothing: Optional[bool] = None,
        concurrency: Optional[float] = None,
        maximum_concurrency_allowed: Optional[float] = None,
        minimal_concurrency_allowed: Optional[float] = None,
        num_replicas: Optional[int] = None,
    ) -> PatchEndpointThroughputResponse:
        """Update the throughput (concurrency) of an endpoint

        :param endpoint_name: str
          Name of the AI Search endpoint
        :param all_or_nothing: bool (optional)
          If true, the request will fail if the requested concurrency or limits cannot be exactly met. If
          false, the request will be adjusted to the closest possible value.
        :param concurrency: float (optional)
          Requested concurrency (total CPU) for the endpoint. If not specified, the current concurrency is
          maintained.
        :param maximum_concurrency_allowed: float (optional)
          Maximum concurrency allowed for the endpoint. If not specified, the current maximum is maintained.
        :param minimal_concurrency_allowed: float (optional)
          Minimum concurrency allowed for the endpoint. If not specified, the current minimum is maintained.
        :param num_replicas: int (optional)
          Requested number of data copies for the endpoint (including primary). For example: num_replicas=2
          means 2 total copies of the data (1 primary + 1 replica). If not specified, the current replication
          factor is maintained. Valid range: 1-6 (where 1 = no replication, 6 = 1 primary + 5 replicas).

        :returns: :class:`PatchEndpointThroughputResponse`
        """

        body = {}
        if all_or_nothing is not None:
            body["all_or_nothing"] = all_or_nothing
        if concurrency is not None:
            body["concurrency"] = concurrency
        if maximum_concurrency_allowed is not None:
            body["maximum_concurrency_allowed"] = maximum_concurrency_allowed
        if minimal_concurrency_allowed is not None:
            body["minimal_concurrency_allowed"] = minimal_concurrency_allowed
        if num_replicas is not None:
            body["num_replicas"] = num_replicas
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "PATCH", f"/api/2.0/vector-search/endpoints/{endpoint_name}/throughput", body=body, headers=headers
        )
        return PatchEndpointThroughputResponse.from_dict(res)

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
        """Retrieve user-visible metrics for an endpoint

        :param name: str
          AI Search endpoint name
        :param end_time: str (optional)
          End time for metrics query
        :param granularity_in_seconds: int (optional)
          Granularity in seconds
        :param metrics: List[:class:`Metric`] (optional)
          List of metrics to retrieve
        :param page_token: str (optional)
          Token for pagination
        :param start_time: str (optional)
          Start time for metrics query

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

    def update_endpoint_budget_policy(
        self, endpoint_name: str, budget_policy_id: str
    ) -> PatchEndpointBudgetPolicyResponse:
        """Update the budget policy of an endpoint

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
        """Create a new index.

        :param name: str
          Name of the index
        :param endpoint_name: str
          Name of the endpoint to be used for serving the index
        :param primary_key: str
          Primary key of the index
        :param index_type: :class:`VectorIndexType`
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
        """Handles the deletion of data from a specified vector index.

        :param index_name: str
          Name of the vector index where data is to be deleted. Must be a Direct Vector Access Index.
        :param primary_keys: List[str]
          List of primary keys for the data to be deleted.

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
        """Delete an index.

        :param index_name: str
          Name of the index


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/vector-search/indexes/{index_name}", headers=headers)

    def get_auto_eval_status(self, name: str) -> GetAutoEvalStatusResponse:
        """Returns the status of the latest autoeval run for a vector index.

        :param name: str
          Fully qualified index name (catalog.schema.index).

        :returns: :class:`GetAutoEvalStatusResponse`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/vector-search/indexes/{name}/autoeval", headers=headers)
        return GetAutoEvalStatusResponse.from_dict(res)

    def get_index(self, index_name: str, *, ensure_reranker_compatible: Optional[bool] = None) -> VectorIndex:
        """Get an index.

        :param index_name: str
          Name of the index
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
          Name of the endpoint
        :param page_token: str (optional)
          Token for pagination

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
        """Query the specified vector index.

        :param index_name: str
          Name of the vector index to query.
        :param columns: List[str]
          List of column names to include in the response.
        :param columns_to_rerank: List[str] (optional)
          Column names used to retrieve data to send to the reranker.
        :param facets: List[str] (optional)
          Facets to compute over the matched results. Each entry has one of these forms: ``"<column>"`` - top
          10 distinct values by count ``"<column> TOP <n>"`` - top n distinct values, where n > 0 ``"<column>
          BUCKETS [[from,to],...]"`` - inclusive numeric ranges ``TOP`` and ``BUCKETS`` are case-insensitive.
          A column may appear at most once.
        :param filters_json: str (optional)
          JSON string representing query filters.

          Example filters:

          - ``{"id <": 5}``: Filter for id less than 5.
          - ``{"id >": 5}``: Filter for id greater than 5.
          - ``{"id <=": 5}``: Filter for id less than equal to 5.
          - ``{"id >=": 5}``: Filter for id greater than equal to 5.
          - ``{"id": 5}``: Filter for id equal to 5.
        :param num_results: int (optional)
          Number of results to return. Defaults to 10.
        :param query_columns: List[str] (optional)
          Text columns to search for ``query_text``. When empty, all text columns are searched.
        :param query_text: str (optional)
          Query text. Required for Delta Sync Index using model endpoint.
        :param query_type: str (optional)
          The query type to use. Choices are ``ANN`` and ``HYBRID`` and ``FULL_TEXT``. Defaults to ``ANN``.
        :param query_vector: List[float] (optional)
          Query vector. Required for Direct Vector Access Index and Delta Sync Index using self-managed
          vectors.
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
          Name of the endpoint.
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

    def run_auto_eval(
        self,
        name: str,
        *,
        num_queries: Optional[int] = None,
        num_results: Optional[int] = None,
        query_types: Optional[List[str]] = None,
        queryset_query_column: Optional[str] = None,
        queryset_relevant_docs_column: Optional[str] = None,
        queryset_table: Optional[str] = None,
    ) -> RunAutoEvalResponse:
        """Triggers an autoeval quality evaluation for a vector index.

        :param name: str
          Fully qualified index name (catalog.schema.index).
        :param num_queries: int (optional)
          Number of queries to generate for evaluation (default: 50).
        :param num_results: int (optional)
          Number of results to fetch per query (default: 10).
        :param query_types: List[str] (optional)
          Query types to evaluate (default: FULL_TEXT, ANN, HYBRID).
        :param queryset_query_column: str (optional)
          Column in ``queryset_table`` holding the query text. Required when ``queryset_table`` is set;
          ignored otherwise.
        :param queryset_relevant_docs_column: str (optional)
          Optional column in ``queryset_table`` holding the ground-truth relevant document IDs for each query
          (STRING or ARRAY<STRING>). When set, recall@k is reported against these labels; when unset,
          evaluation falls back to LLM-judged metrics only. Ignored when ``queryset_table`` is unset.
        :param queryset_table: str (optional)
          Fully qualified Unity Catalog table (catalog.schema.table) of evaluation queries to run against the
          index. When set, queries are read from this table and synthetic query generation is skipped. The
          table takes precedence over any automatically detected query source.

        :returns: :class:`RunAutoEvalResponse`
        """

        body = {}
        if num_queries is not None:
            body["num_queries"] = num_queries
        if num_results is not None:
            body["num_results"] = num_results
        if query_types is not None:
            body["query_types"] = [v for v in query_types]
        if queryset_query_column is not None:
            body["queryset_query_column"] = queryset_query_column
        if queryset_relevant_docs_column is not None:
            body["queryset_relevant_docs_column"] = queryset_relevant_docs_column
        if queryset_table is not None:
            body["queryset_table"] = queryset_table
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/vector-search/indexes/{name}/autoeval", body=body, headers=headers)
        return RunAutoEvalResponse.from_dict(res)

    def run_reranker_finetuning(
        self,
        name: str,
        *,
        embedding_model: Optional[str] = None,
        model_name: Optional[str] = None,
        num_queries: Optional[int] = None,
        query_column: Optional[str] = None,
        query_table: Optional[str] = None,
    ) -> RunRerankerFinetuningResponse:
        """Triggers reranker finetuning for a vector index.

        :param name: str
          Fully qualified index name (catalog.schema.index).
        :param embedding_model: str (optional)
          Model-serving endpoint name. Reranker finetuning only supports managed Delta Sync indices
          (Databricks-computed embeddings), so this field is informational — it is auto-derived from the
          index and not used to embed training queries locally.
        :param model_name: str (optional)
          Fully qualified UC name for the registered finetuned model (catalog.schema.model). When unset, the
          handler derives a default of ``<catalog>.<schema>.reranker_<index_short_name>`` from ``name``.
        :param num_queries: int (optional)
          Cap on the number of queries sampled from ``query_table`` (or generated when ``query_table`` is
          unset). Use -1 to process all queries (the data-gen default). Lower values cut LLM-judge cost and
          run time.
        :param query_column: str (optional)
          Column in ``query_table`` containing the query text. Ignored when ``query_table`` is unset. Defaults
          to "query_text" when omitted.
        :param query_table: str (optional)
          Optional fully qualified UC Delta table holding training queries (catalog.schema.table). When unset,
          the data-gen job synthesises queries from the index corpus via an LLM.

        :returns: :class:`RunRerankerFinetuningResponse`
        """

        body = {}
        if embedding_model is not None:
            body["embedding_model"] = embedding_model
        if model_name is not None:
            body["model_name"] = model_name
        if num_queries is not None:
            body["num_queries"] = num_queries
        if query_column is not None:
            body["query_column"] = query_column
        if query_table is not None:
            body["query_table"] = query_table
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "POST", f"/api/2.0/vector-search/indexes/{name}/reranker-finetuning", body=body, headers=headers
        )
        return RunRerankerFinetuningResponse.from_dict(res)

    def scan_index(
        self, index_name: str, *, last_primary_key: Optional[str] = None, num_results: Optional[int] = None
    ) -> ScanVectorIndexResponse:
        """Scan the specified vector index and return the first ``num_results`` entries after the exclusive
        ``primary_key``.

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
        """Triggers a synchronization process for a specified vector index.

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

    def update_index_budget_policy(
        self, index_name: str, *, usage_policy_id: Optional[str] = None
    ) -> UpdateVectorIndexUsagePolicyResponse:
        """Update the budget policy of an index

        :param index_name: str
          Name of the AI Search index
        :param usage_policy_id: str (optional)
          The usage policy id to be applied

        :returns: :class:`UpdateVectorIndexUsagePolicyResponse`
        """

        body = {}
        if usage_policy_id is not None:
            body["usage_policy_id"] = usage_policy_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "PATCH", f"/api/2.0/vector-search/indexes/{index_name}/usage-policy", body=body, headers=headers
        )
        return UpdateVectorIndexUsagePolicyResponse.from_dict(res)

    def upsert_data_vector_index(self, index_name: str, inputs_json: str) -> UpsertDataVectorIndexResponse:
        """Handles the upserting of data into a specified vector index.

        :param index_name: str
          Name of the vector index where data is to be upserted. Must be a Direct Vector Access Index.
        :param inputs_json: str
          JSON string representing the data to be upserted.

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

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
from ._internal import Wait, _enum, _from_dict, _repeated_dict

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class ColumnInfo:
    name: Optional[str] = None
    """Name of the column."""

    def as_dict(self) -> dict:
        """Serializes the ColumnInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ColumnInfo:
        """Deserializes the ColumnInfo from a dictionary."""
        return cls(name=d.get('name', None))


@dataclass
class CreateEndpoint:
    name: str
    """Name of endpoint"""

    endpoint_type: EndpointType
    """Type of endpoint."""

    def as_dict(self) -> dict:
        """Serializes the CreateEndpoint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.endpoint_type is not None: body['endpoint_type'] = self.endpoint_type.value
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateEndpoint:
        """Deserializes the CreateEndpoint from a dictionary."""
        return cls(endpoint_type=_enum(d, 'endpoint_type', EndpointType), name=d.get('name', None))


@dataclass
class CreateVectorIndexRequest:
    name: str
    """Name of the index"""

    endpoint_name: str
    """Name of the endpoint to be used for serving the index"""

    primary_key: str
    """Primary key of the index"""

    index_type: VectorIndexType
    """There are 2 types of Vector Search indexes:
    
    - `DELTA_SYNC`: An index that automatically syncs with a source Delta Table, automatically and
    incrementally updating the index as the underlying data in the Delta Table changes. -
    `DIRECT_ACCESS`: An index that supports direct read and write of vectors and metadata through
    our REST and SDK APIs. With this model, the user manages index updates."""

    delta_sync_index_spec: Optional[DeltaSyncVectorIndexSpecRequest] = None
    """Specification for Delta Sync Index. Required if `index_type` is `DELTA_SYNC`."""

    direct_access_index_spec: Optional[DirectAccessVectorIndexSpec] = None
    """Specification for Direct Vector Access Index. Required if `index_type` is `DIRECT_ACCESS`."""

    def as_dict(self) -> dict:
        """Serializes the CreateVectorIndexRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.delta_sync_index_spec: body['delta_sync_index_spec'] = self.delta_sync_index_spec.as_dict()
        if self.direct_access_index_spec:
            body['direct_access_index_spec'] = self.direct_access_index_spec.as_dict()
        if self.endpoint_name is not None: body['endpoint_name'] = self.endpoint_name
        if self.index_type is not None: body['index_type'] = self.index_type.value
        if self.name is not None: body['name'] = self.name
        if self.primary_key is not None: body['primary_key'] = self.primary_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateVectorIndexRequest:
        """Deserializes the CreateVectorIndexRequest from a dictionary."""
        return cls(delta_sync_index_spec=_from_dict(d, 'delta_sync_index_spec',
                                                    DeltaSyncVectorIndexSpecRequest),
                   direct_access_index_spec=_from_dict(d, 'direct_access_index_spec',
                                                       DirectAccessVectorIndexSpec),
                   endpoint_name=d.get('endpoint_name', None),
                   index_type=_enum(d, 'index_type', VectorIndexType),
                   name=d.get('name', None),
                   primary_key=d.get('primary_key', None))


@dataclass
class CreateVectorIndexResponse:
    vector_index: Optional[VectorIndex] = None

    def as_dict(self) -> dict:
        """Serializes the CreateVectorIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.vector_index: body['vector_index'] = self.vector_index.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateVectorIndexResponse:
        """Deserializes the CreateVectorIndexResponse from a dictionary."""
        return cls(vector_index=_from_dict(d, 'vector_index', VectorIndex))


@dataclass
class DeleteDataResult:
    """Result of the upsert or delete operation."""

    failed_primary_keys: Optional[List[str]] = None
    """List of primary keys for rows that failed to process."""

    success_row_count: Optional[int] = None
    """Count of successfully processed rows."""

    def as_dict(self) -> dict:
        """Serializes the DeleteDataResult into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.failed_primary_keys: body['failed_primary_keys'] = [v for v in self.failed_primary_keys]
        if self.success_row_count is not None: body['success_row_count'] = self.success_row_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteDataResult:
        """Deserializes the DeleteDataResult from a dictionary."""
        return cls(failed_primary_keys=d.get('failed_primary_keys', None),
                   success_row_count=d.get('success_row_count', None))


class DeleteDataStatus(Enum):
    """Status of the delete operation."""

    FAILURE = 'FAILURE'
    PARTIAL_SUCCESS = 'PARTIAL_SUCCESS'
    SUCCESS = 'SUCCESS'


@dataclass
class DeleteDataVectorIndexRequest:
    """Request payload for deleting data from a vector index."""

    primary_keys: List[str]
    """List of primary keys for the data to be deleted."""

    index_name: Optional[str] = None
    """Name of the vector index where data is to be deleted. Must be a Direct Vector Access Index."""

    def as_dict(self) -> dict:
        """Serializes the DeleteDataVectorIndexRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.index_name is not None: body['index_name'] = self.index_name
        if self.primary_keys: body['primary_keys'] = [v for v in self.primary_keys]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteDataVectorIndexRequest:
        """Deserializes the DeleteDataVectorIndexRequest from a dictionary."""
        return cls(index_name=d.get('index_name', None), primary_keys=d.get('primary_keys', None))


@dataclass
class DeleteDataVectorIndexResponse:
    """Response to a delete data vector index request."""

    result: Optional[DeleteDataResult] = None
    """Result of the upsert or delete operation."""

    status: Optional[DeleteDataStatus] = None
    """Status of the delete operation."""

    def as_dict(self) -> dict:
        """Serializes the DeleteDataVectorIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.result: body['result'] = self.result.as_dict()
        if self.status is not None: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteDataVectorIndexResponse:
        """Deserializes the DeleteDataVectorIndexResponse from a dictionary."""
        return cls(result=_from_dict(d, 'result', DeleteDataResult),
                   status=_enum(d, 'status', DeleteDataStatus))


@dataclass
class DeleteEndpointResponse:

    def as_dict(self) -> dict:
        """Serializes the DeleteEndpointResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteEndpointResponse:
        """Deserializes the DeleteEndpointResponse from a dictionary."""
        return cls()


@dataclass
class DeleteIndexResponse:

    def as_dict(self) -> dict:
        """Serializes the DeleteIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteIndexResponse:
        """Deserializes the DeleteIndexResponse from a dictionary."""
        return cls()


@dataclass
class DeltaSyncVectorIndexSpecRequest:
    embedding_source_columns: Optional[List[EmbeddingSourceColumn]] = None
    """The columns that contain the embedding source."""

    embedding_vector_columns: Optional[List[EmbeddingVectorColumn]] = None
    """The columns that contain the embedding vectors. The format should be array[double]."""

    embedding_writeback_table: Optional[str] = None
    """[Optional] Automatically sync the vector index contents and computed embeddings to the specified
    Delta table. The only supported table name is the index name with the suffix `_writeback_table`."""

    pipeline_type: Optional[PipelineType] = None
    """Pipeline execution mode.
    
    - `TRIGGERED`: If the pipeline uses the triggered execution mode, the system stops processing
    after successfully refreshing the source table in the pipeline once, ensuring the table is
    updated based on the data available when the update started. - `CONTINUOUS`: If the pipeline
    uses continuous execution, the pipeline processes new data as it arrives in the source table to
    keep vector index fresh."""

    source_table: Optional[str] = None
    """The name of the source table."""

    def as_dict(self) -> dict:
        """Serializes the DeltaSyncVectorIndexSpecRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.embedding_source_columns:
            body['embedding_source_columns'] = [v.as_dict() for v in self.embedding_source_columns]
        if self.embedding_vector_columns:
            body['embedding_vector_columns'] = [v.as_dict() for v in self.embedding_vector_columns]
        if self.embedding_writeback_table is not None:
            body['embedding_writeback_table'] = self.embedding_writeback_table
        if self.pipeline_type is not None: body['pipeline_type'] = self.pipeline_type.value
        if self.source_table is not None: body['source_table'] = self.source_table
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeltaSyncVectorIndexSpecRequest:
        """Deserializes the DeltaSyncVectorIndexSpecRequest from a dictionary."""
        return cls(embedding_source_columns=_repeated_dict(d, 'embedding_source_columns',
                                                           EmbeddingSourceColumn),
                   embedding_vector_columns=_repeated_dict(d, 'embedding_vector_columns',
                                                           EmbeddingVectorColumn),
                   embedding_writeback_table=d.get('embedding_writeback_table', None),
                   pipeline_type=_enum(d, 'pipeline_type', PipelineType),
                   source_table=d.get('source_table', None))


@dataclass
class DeltaSyncVectorIndexSpecResponse:
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
    
    - `TRIGGERED`: If the pipeline uses the triggered execution mode, the system stops processing
    after successfully refreshing the source table in the pipeline once, ensuring the table is
    updated based on the data available when the update started. - `CONTINUOUS`: If the pipeline
    uses continuous execution, the pipeline processes new data as it arrives in the source table to
    keep vector index fresh."""

    source_table: Optional[str] = None
    """The name of the source table."""

    def as_dict(self) -> dict:
        """Serializes the DeltaSyncVectorIndexSpecResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.embedding_source_columns:
            body['embedding_source_columns'] = [v.as_dict() for v in self.embedding_source_columns]
        if self.embedding_vector_columns:
            body['embedding_vector_columns'] = [v.as_dict() for v in self.embedding_vector_columns]
        if self.embedding_writeback_table is not None:
            body['embedding_writeback_table'] = self.embedding_writeback_table
        if self.pipeline_id is not None: body['pipeline_id'] = self.pipeline_id
        if self.pipeline_type is not None: body['pipeline_type'] = self.pipeline_type.value
        if self.source_table is not None: body['source_table'] = self.source_table
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeltaSyncVectorIndexSpecResponse:
        """Deserializes the DeltaSyncVectorIndexSpecResponse from a dictionary."""
        return cls(embedding_source_columns=_repeated_dict(d, 'embedding_source_columns',
                                                           EmbeddingSourceColumn),
                   embedding_vector_columns=_repeated_dict(d, 'embedding_vector_columns',
                                                           EmbeddingVectorColumn),
                   embedding_writeback_table=d.get('embedding_writeback_table', None),
                   pipeline_id=d.get('pipeline_id', None),
                   pipeline_type=_enum(d, 'pipeline_type', PipelineType),
                   source_table=d.get('source_table', None))


@dataclass
class DirectAccessVectorIndexSpec:
    embedding_source_columns: Optional[List[EmbeddingSourceColumn]] = None
    """Contains the optional model endpoint to use during query time."""

    embedding_vector_columns: Optional[List[EmbeddingVectorColumn]] = None

    schema_json: Optional[str] = None
    """The schema of the index in JSON format.
    
    Supported types are `integer`, `long`, `float`, `double`, `boolean`, `string`, `date`,
    `timestamp`.
    
    Supported types for vector column: `array<float>`, `array<double>`,`."""

    def as_dict(self) -> dict:
        """Serializes the DirectAccessVectorIndexSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.embedding_source_columns:
            body['embedding_source_columns'] = [v.as_dict() for v in self.embedding_source_columns]
        if self.embedding_vector_columns:
            body['embedding_vector_columns'] = [v.as_dict() for v in self.embedding_vector_columns]
        if self.schema_json is not None: body['schema_json'] = self.schema_json
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DirectAccessVectorIndexSpec:
        """Deserializes the DirectAccessVectorIndexSpec from a dictionary."""
        return cls(embedding_source_columns=_repeated_dict(d, 'embedding_source_columns',
                                                           EmbeddingSourceColumn),
                   embedding_vector_columns=_repeated_dict(d, 'embedding_vector_columns',
                                                           EmbeddingVectorColumn),
                   schema_json=d.get('schema_json', None))


@dataclass
class EmbeddingSourceColumn:
    embedding_model_endpoint_name: Optional[str] = None
    """Name of the embedding model endpoint"""

    name: Optional[str] = None
    """Name of the column"""

    def as_dict(self) -> dict:
        """Serializes the EmbeddingSourceColumn into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.embedding_model_endpoint_name is not None:
            body['embedding_model_endpoint_name'] = self.embedding_model_endpoint_name
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EmbeddingSourceColumn:
        """Deserializes the EmbeddingSourceColumn from a dictionary."""
        return cls(embedding_model_endpoint_name=d.get('embedding_model_endpoint_name', None),
                   name=d.get('name', None))


@dataclass
class EmbeddingVectorColumn:
    embedding_dimension: Optional[int] = None
    """Dimension of the embedding vector"""

    name: Optional[str] = None
    """Name of the column"""

    def as_dict(self) -> dict:
        """Serializes the EmbeddingVectorColumn into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.embedding_dimension is not None: body['embedding_dimension'] = self.embedding_dimension
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EmbeddingVectorColumn:
        """Deserializes the EmbeddingVectorColumn from a dictionary."""
        return cls(embedding_dimension=d.get('embedding_dimension', None), name=d.get('name', None))


@dataclass
class EndpointInfo:
    creation_timestamp: Optional[int] = None
    """Timestamp of endpoint creation"""

    creator: Optional[str] = None
    """Creator of the endpoint"""

    endpoint_status: Optional[EndpointStatus] = None
    """Current status of the endpoint"""

    endpoint_type: Optional[EndpointType] = None
    """Type of endpoint."""

    id: Optional[str] = None
    """Unique identifier of the endpoint"""

    last_updated_timestamp: Optional[int] = None
    """Timestamp of last update to the endpoint"""

    last_updated_user: Optional[str] = None
    """User who last updated the endpoint"""

    name: Optional[str] = None
    """Name of endpoint"""

    num_indexes: Optional[int] = None
    """Number of indexes on the endpoint"""

    def as_dict(self) -> dict:
        """Serializes the EndpointInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.creator is not None: body['creator'] = self.creator
        if self.endpoint_status: body['endpoint_status'] = self.endpoint_status.as_dict()
        if self.endpoint_type is not None: body['endpoint_type'] = self.endpoint_type.value
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.last_updated_user is not None: body['last_updated_user'] = self.last_updated_user
        if self.name is not None: body['name'] = self.name
        if self.num_indexes is not None: body['num_indexes'] = self.num_indexes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EndpointInfo:
        """Deserializes the EndpointInfo from a dictionary."""
        return cls(creation_timestamp=d.get('creation_timestamp', None),
                   creator=d.get('creator', None),
                   endpoint_status=_from_dict(d, 'endpoint_status', EndpointStatus),
                   endpoint_type=_enum(d, 'endpoint_type', EndpointType),
                   id=d.get('id', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   last_updated_user=d.get('last_updated_user', None),
                   name=d.get('name', None),
                   num_indexes=d.get('num_indexes', None))


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
        if self.message is not None: body['message'] = self.message
        if self.state is not None: body['state'] = self.state.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EndpointStatus:
        """Deserializes the EndpointStatus from a dictionary."""
        return cls(message=d.get('message', None), state=_enum(d, 'state', EndpointStatusState))


class EndpointStatusState(Enum):
    """Current state of the endpoint"""

    OFFLINE = 'OFFLINE'
    ONLINE = 'ONLINE'
    PROVISIONING = 'PROVISIONING'


class EndpointType(Enum):
    """Type of endpoint."""

    STANDARD = 'STANDARD'


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
        if self.endpoints: body['endpoints'] = [v.as_dict() for v in self.endpoints]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListEndpointResponse:
        """Deserializes the ListEndpointResponse from a dictionary."""
        return cls(endpoints=_repeated_dict(d, 'endpoints', EndpointInfo),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListValue:
    values: Optional[List[Value]] = None

    def as_dict(self) -> dict:
        """Serializes the ListValue into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.values: body['values'] = [v.as_dict() for v in self.values]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListValue:
        """Deserializes the ListValue from a dictionary."""
        return cls(values=_repeated_dict(d, 'values', Value))


@dataclass
class ListVectorIndexesResponse:
    next_page_token: Optional[str] = None
    """A token that can be used to get the next page of results. If not present, there are no more
    results to show."""

    vector_indexes: Optional[List[MiniVectorIndex]] = None

    def as_dict(self) -> dict:
        """Serializes the ListVectorIndexesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.vector_indexes: body['vector_indexes'] = [v.as_dict() for v in self.vector_indexes]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListVectorIndexesResponse:
        """Deserializes the ListVectorIndexesResponse from a dictionary."""
        return cls(next_page_token=d.get('next_page_token', None),
                   vector_indexes=_repeated_dict(d, 'vector_indexes', MiniVectorIndex))


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
        if self.key is not None: body['key'] = self.key
        if self.value: body['value'] = self.value.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MapStringValueEntry:
        """Deserializes the MapStringValueEntry from a dictionary."""
        return cls(key=d.get('key', None), value=_from_dict(d, 'value', Value))


@dataclass
class MiniVectorIndex:
    creator: Optional[str] = None
    """The user who created the index."""

    endpoint_name: Optional[str] = None
    """Name of the endpoint associated with the index"""

    index_type: Optional[VectorIndexType] = None
    """There are 2 types of Vector Search indexes:
    
    - `DELTA_SYNC`: An index that automatically syncs with a source Delta Table, automatically and
    incrementally updating the index as the underlying data in the Delta Table changes. -
    `DIRECT_ACCESS`: An index that supports direct read and write of vectors and metadata through
    our REST and SDK APIs. With this model, the user manages index updates."""

    name: Optional[str] = None
    """Name of the index"""

    primary_key: Optional[str] = None
    """Primary key of the index"""

    def as_dict(self) -> dict:
        """Serializes the MiniVectorIndex into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.creator is not None: body['creator'] = self.creator
        if self.endpoint_name is not None: body['endpoint_name'] = self.endpoint_name
        if self.index_type is not None: body['index_type'] = self.index_type.value
        if self.name is not None: body['name'] = self.name
        if self.primary_key is not None: body['primary_key'] = self.primary_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MiniVectorIndex:
        """Deserializes the MiniVectorIndex from a dictionary."""
        return cls(creator=d.get('creator', None),
                   endpoint_name=d.get('endpoint_name', None),
                   index_type=_enum(d, 'index_type', VectorIndexType),
                   name=d.get('name', None),
                   primary_key=d.get('primary_key', None))


class PipelineType(Enum):
    """Pipeline execution mode.
    
    - `TRIGGERED`: If the pipeline uses the triggered execution mode, the system stops processing
    after successfully refreshing the source table in the pipeline once, ensuring the table is
    updated based on the data available when the update started. - `CONTINUOUS`: If the pipeline
    uses continuous execution, the pipeline processes new data as it arrives in the source table to
    keep vector index fresh."""

    CONTINUOUS = 'CONTINUOUS'
    TRIGGERED = 'TRIGGERED'


@dataclass
class QueryVectorIndexNextPageRequest:
    """Request payload for getting next page of results."""

    endpoint_name: Optional[str] = None
    """Name of the endpoint."""

    index_name: Optional[str] = None
    """Name of the vector index to query."""

    page_token: Optional[str] = None
    """Page token returned from previous `QueryVectorIndex` or `QueryVectorIndexNextPage` API."""

    def as_dict(self) -> dict:
        """Serializes the QueryVectorIndexNextPageRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.endpoint_name is not None: body['endpoint_name'] = self.endpoint_name
        if self.index_name is not None: body['index_name'] = self.index_name
        if self.page_token is not None: body['page_token'] = self.page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> QueryVectorIndexNextPageRequest:
        """Deserializes the QueryVectorIndexNextPageRequest from a dictionary."""
        return cls(endpoint_name=d.get('endpoint_name', None),
                   index_name=d.get('index_name', None),
                   page_token=d.get('page_token', None))


@dataclass
class QueryVectorIndexRequest:
    columns: List[str]
    """List of column names to include in the response."""

    filters_json: Optional[str] = None
    """JSON string representing query filters.
    
    Example filters: - `{"id <": 5}`: Filter for id less than 5. - `{"id >": 5}`: Filter for id
    greater than 5. - `{"id <=": 5}`: Filter for id less than equal to 5. - `{"id >=": 5}`: Filter
    for id greater than equal to 5. - `{"id": 5}`: Filter for id equal to 5."""

    index_name: Optional[str] = None
    """Name of the vector index to query."""

    num_results: Optional[int] = None
    """Number of results to return. Defaults to 10."""

    query_text: Optional[str] = None
    """Query text. Required for Delta Sync Index using model endpoint."""

    query_type: Optional[str] = None
    """The query type to use. Choices are `ANN` and `HYBRID`. Defaults to `ANN`."""

    query_vector: Optional[List[float]] = None
    """Query vector. Required for Direct Vector Access Index and Delta Sync Index using self-managed
    vectors."""

    score_threshold: Optional[float] = None
    """Threshold for the approximate nearest neighbor search. Defaults to 0.0."""

    def as_dict(self) -> dict:
        """Serializes the QueryVectorIndexRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.columns: body['columns'] = [v for v in self.columns]
        if self.filters_json is not None: body['filters_json'] = self.filters_json
        if self.index_name is not None: body['index_name'] = self.index_name
        if self.num_results is not None: body['num_results'] = self.num_results
        if self.query_text is not None: body['query_text'] = self.query_text
        if self.query_type is not None: body['query_type'] = self.query_type
        if self.query_vector: body['query_vector'] = [v for v in self.query_vector]
        if self.score_threshold is not None: body['score_threshold'] = self.score_threshold
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> QueryVectorIndexRequest:
        """Deserializes the QueryVectorIndexRequest from a dictionary."""
        return cls(columns=d.get('columns', None),
                   filters_json=d.get('filters_json', None),
                   index_name=d.get('index_name', None),
                   num_results=d.get('num_results', None),
                   query_text=d.get('query_text', None),
                   query_type=d.get('query_type', None),
                   query_vector=d.get('query_vector', None),
                   score_threshold=d.get('score_threshold', None))


@dataclass
class QueryVectorIndexResponse:
    manifest: Optional[ResultManifest] = None
    """Metadata about the result set."""

    next_page_token: Optional[str] = None
    """[Optional] Token that can be used in `QueryVectorIndexNextPage` API to get next page of results.
    If more than 1000 results satisfy the query, they are returned in groups of 1000. Empty value
    means no more results."""

    result: Optional[ResultData] = None
    """Data returned in the query result."""

    def as_dict(self) -> dict:
        """Serializes the QueryVectorIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.manifest: body['manifest'] = self.manifest.as_dict()
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.result: body['result'] = self.result.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> QueryVectorIndexResponse:
        """Deserializes the QueryVectorIndexResponse from a dictionary."""
        return cls(manifest=_from_dict(d, 'manifest', ResultManifest),
                   next_page_token=d.get('next_page_token', None),
                   result=_from_dict(d, 'result', ResultData))


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
        if self.data_array: body['data_array'] = [v for v in self.data_array]
        if self.row_count is not None: body['row_count'] = self.row_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ResultData:
        """Deserializes the ResultData from a dictionary."""
        return cls(data_array=d.get('data_array', None), row_count=d.get('row_count', None))


@dataclass
class ResultManifest:
    """Metadata about the result set."""

    column_count: Optional[int] = None
    """Number of columns in the result set."""

    columns: Optional[List[ColumnInfo]] = None
    """Information about each column in the result set."""

    def as_dict(self) -> dict:
        """Serializes the ResultManifest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.column_count is not None: body['column_count'] = self.column_count
        if self.columns: body['columns'] = [v.as_dict() for v in self.columns]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ResultManifest:
        """Deserializes the ResultManifest from a dictionary."""
        return cls(column_count=d.get('column_count', None), columns=_repeated_dict(d, 'columns', ColumnInfo))


@dataclass
class ScanVectorIndexRequest:
    """Request payload for scanning data from a vector index."""

    index_name: Optional[str] = None
    """Name of the vector index to scan."""

    last_primary_key: Optional[str] = None
    """Primary key of the last entry returned in the previous scan."""

    num_results: Optional[int] = None
    """Number of results to return. Defaults to 10."""

    def as_dict(self) -> dict:
        """Serializes the ScanVectorIndexRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.index_name is not None: body['index_name'] = self.index_name
        if self.last_primary_key is not None: body['last_primary_key'] = self.last_primary_key
        if self.num_results is not None: body['num_results'] = self.num_results
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ScanVectorIndexRequest:
        """Deserializes the ScanVectorIndexRequest from a dictionary."""
        return cls(index_name=d.get('index_name', None),
                   last_primary_key=d.get('last_primary_key', None),
                   num_results=d.get('num_results', None))


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
        if self.data: body['data'] = [v.as_dict() for v in self.data]
        if self.last_primary_key is not None: body['last_primary_key'] = self.last_primary_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ScanVectorIndexResponse:
        """Deserializes the ScanVectorIndexResponse from a dictionary."""
        return cls(data=_repeated_dict(d, 'data', Struct), last_primary_key=d.get('last_primary_key', None))


@dataclass
class Struct:
    fields: Optional[List[MapStringValueEntry]] = None
    """Data entry, corresponding to a row in a vector index."""

    def as_dict(self) -> dict:
        """Serializes the Struct into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.fields: body['fields'] = [v.as_dict() for v in self.fields]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Struct:
        """Deserializes the Struct from a dictionary."""
        return cls(fields=_repeated_dict(d, 'fields', MapStringValueEntry))


@dataclass
class SyncIndexResponse:

    def as_dict(self) -> dict:
        """Serializes the SyncIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> SyncIndexResponse:
        """Deserializes the SyncIndexResponse from a dictionary."""
        return cls()


@dataclass
class UpsertDataResult:
    """Result of the upsert or delete operation."""

    failed_primary_keys: Optional[List[str]] = None
    """List of primary keys for rows that failed to process."""

    success_row_count: Optional[int] = None
    """Count of successfully processed rows."""

    def as_dict(self) -> dict:
        """Serializes the UpsertDataResult into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.failed_primary_keys: body['failed_primary_keys'] = [v for v in self.failed_primary_keys]
        if self.success_row_count is not None: body['success_row_count'] = self.success_row_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpsertDataResult:
        """Deserializes the UpsertDataResult from a dictionary."""
        return cls(failed_primary_keys=d.get('failed_primary_keys', None),
                   success_row_count=d.get('success_row_count', None))


class UpsertDataStatus(Enum):
    """Status of the upsert operation."""

    FAILURE = 'FAILURE'
    PARTIAL_SUCCESS = 'PARTIAL_SUCCESS'
    SUCCESS = 'SUCCESS'


@dataclass
class UpsertDataVectorIndexRequest:
    """Request payload for upserting data into a vector index."""

    inputs_json: str
    """JSON string representing the data to be upserted."""

    index_name: Optional[str] = None
    """Name of the vector index where data is to be upserted. Must be a Direct Vector Access Index."""

    def as_dict(self) -> dict:
        """Serializes the UpsertDataVectorIndexRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.index_name is not None: body['index_name'] = self.index_name
        if self.inputs_json is not None: body['inputs_json'] = self.inputs_json
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpsertDataVectorIndexRequest:
        """Deserializes the UpsertDataVectorIndexRequest from a dictionary."""
        return cls(index_name=d.get('index_name', None), inputs_json=d.get('inputs_json', None))


@dataclass
class UpsertDataVectorIndexResponse:
    """Response to an upsert data vector index request."""

    result: Optional[UpsertDataResult] = None
    """Result of the upsert or delete operation."""

    status: Optional[UpsertDataStatus] = None
    """Status of the upsert operation."""

    def as_dict(self) -> dict:
        """Serializes the UpsertDataVectorIndexResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.result: body['result'] = self.result.as_dict()
        if self.status is not None: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpsertDataVectorIndexResponse:
        """Deserializes the UpsertDataVectorIndexResponse from a dictionary."""
        return cls(result=_from_dict(d, 'result', UpsertDataResult),
                   status=_enum(d, 'status', UpsertDataStatus))


@dataclass
class Value:
    bool_value: Optional[bool] = None

    list_value: Optional[ListValue] = None

    null_value: Optional[str] = None

    number_value: Optional[float] = None

    string_value: Optional[str] = None

    struct_value: Optional[Struct] = None

    def as_dict(self) -> dict:
        """Serializes the Value into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.bool_value is not None: body['bool_value'] = self.bool_value
        if self.list_value: body['list_value'] = self.list_value.as_dict()
        if self.null_value is not None: body['null_value'] = self.null_value
        if self.number_value is not None: body['number_value'] = self.number_value
        if self.string_value is not None: body['string_value'] = self.string_value
        if self.struct_value: body['struct_value'] = self.struct_value.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Value:
        """Deserializes the Value from a dictionary."""
        return cls(bool_value=d.get('bool_value', None),
                   list_value=_from_dict(d, 'list_value', ListValue),
                   null_value=d.get('null_value', None),
                   number_value=d.get('number_value', None),
                   string_value=d.get('string_value', None),
                   struct_value=_from_dict(d, 'struct_value', Struct))


@dataclass
class VectorIndex:
    creator: Optional[str] = None
    """The user who created the index."""

    delta_sync_index_spec: Optional[DeltaSyncVectorIndexSpecResponse] = None

    direct_access_index_spec: Optional[DirectAccessVectorIndexSpec] = None

    endpoint_name: Optional[str] = None
    """Name of the endpoint associated with the index"""

    index_type: Optional[VectorIndexType] = None
    """There are 2 types of Vector Search indexes:
    
    - `DELTA_SYNC`: An index that automatically syncs with a source Delta Table, automatically and
    incrementally updating the index as the underlying data in the Delta Table changes. -
    `DIRECT_ACCESS`: An index that supports direct read and write of vectors and metadata through
    our REST and SDK APIs. With this model, the user manages index updates."""

    name: Optional[str] = None
    """Name of the index"""

    primary_key: Optional[str] = None
    """Primary key of the index"""

    status: Optional[VectorIndexStatus] = None

    def as_dict(self) -> dict:
        """Serializes the VectorIndex into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.creator is not None: body['creator'] = self.creator
        if self.delta_sync_index_spec: body['delta_sync_index_spec'] = self.delta_sync_index_spec.as_dict()
        if self.direct_access_index_spec:
            body['direct_access_index_spec'] = self.direct_access_index_spec.as_dict()
        if self.endpoint_name is not None: body['endpoint_name'] = self.endpoint_name
        if self.index_type is not None: body['index_type'] = self.index_type.value
        if self.name is not None: body['name'] = self.name
        if self.primary_key is not None: body['primary_key'] = self.primary_key
        if self.status: body['status'] = self.status.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> VectorIndex:
        """Deserializes the VectorIndex from a dictionary."""
        return cls(creator=d.get('creator', None),
                   delta_sync_index_spec=_from_dict(d, 'delta_sync_index_spec',
                                                    DeltaSyncVectorIndexSpecResponse),
                   direct_access_index_spec=_from_dict(d, 'direct_access_index_spec',
                                                       DirectAccessVectorIndexSpec),
                   endpoint_name=d.get('endpoint_name', None),
                   index_type=_enum(d, 'index_type', VectorIndexType),
                   name=d.get('name', None),
                   primary_key=d.get('primary_key', None),
                   status=_from_dict(d, 'status', VectorIndexStatus))


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
        if self.index_url is not None: body['index_url'] = self.index_url
        if self.indexed_row_count is not None: body['indexed_row_count'] = self.indexed_row_count
        if self.message is not None: body['message'] = self.message
        if self.ready is not None: body['ready'] = self.ready
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> VectorIndexStatus:
        """Deserializes the VectorIndexStatus from a dictionary."""
        return cls(index_url=d.get('index_url', None),
                   indexed_row_count=d.get('indexed_row_count', None),
                   message=d.get('message', None),
                   ready=d.get('ready', None))


class VectorIndexType(Enum):
    """There are 2 types of Vector Search indexes:
    
    - `DELTA_SYNC`: An index that automatically syncs with a source Delta Table, automatically and
    incrementally updating the index as the underlying data in the Delta Table changes. -
    `DIRECT_ACCESS`: An index that supports direct read and write of vectors and metadata through
    our REST and SDK APIs. With this model, the user manages index updates."""

    DELTA_SYNC = 'DELTA_SYNC'
    DIRECT_ACCESS = 'DIRECT_ACCESS'


class VectorSearchEndpointsAPI:
    """**Endpoint**: Represents the compute resources to host vector search indexes."""

    def __init__(self, api_client):
        self._api = api_client

    def wait_get_endpoint_vector_search_endpoint_online(
            self,
            endpoint_name: str,
            timeout=timedelta(minutes=20),
            callback: Optional[Callable[[EndpointInfo], None]] = None) -> EndpointInfo:
        deadline = time.time() + timeout.total_seconds()
        target_states = (EndpointStatusState.ONLINE, )
        failure_states = (EndpointStatusState.OFFLINE, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get_endpoint(endpoint_name=endpoint_name)
            status = poll.endpoint_status.state
            status_message = f'current status: {status}'
            if poll.endpoint_status:
                status_message = poll.endpoint_status.message
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach ONLINE, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"endpoint_name={endpoint_name}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def create_endpoint(self, name: str, endpoint_type: EndpointType) -> Wait[EndpointInfo]:
        """Create an endpoint.
        
        Create a new endpoint.
        
        :param name: str
          Name of endpoint
        :param endpoint_type: :class:`EndpointType`
          Type of endpoint.
        
        :returns:
          Long-running operation waiter for :class:`EndpointInfo`.
          See :method:wait_get_endpoint_vector_search_endpoint_online for more details.
        """
        body = {}
        if endpoint_type is not None: body['endpoint_type'] = endpoint_type.value
        if name is not None: body['name'] = name
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        op_response = self._api.do('POST', '/api/2.0/vector-search/endpoints', body=body, headers=headers)
        return Wait(self.wait_get_endpoint_vector_search_endpoint_online,
                    response=EndpointInfo.from_dict(op_response),
                    endpoint_name=op_response['name'])

    def create_endpoint_and_wait(self, name: str, endpoint_type: EndpointType,
                                 timeout=timedelta(minutes=20)) -> EndpointInfo:
        return self.create_endpoint(endpoint_type=endpoint_type, name=name).result(timeout=timeout)

    def delete_endpoint(self, endpoint_name: str):
        """Delete an endpoint.
        
        :param endpoint_name: str
          Name of the endpoint
        
        
        """

        headers = {}

        self._api.do('DELETE', f'/api/2.0/vector-search/endpoints/{endpoint_name}', headers=headers)

    def get_endpoint(self, endpoint_name: str) -> EndpointInfo:
        """Get an endpoint.
        
        :param endpoint_name: str
          Name of the endpoint
        
        :returns: :class:`EndpointInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/vector-search/endpoints/{endpoint_name}', headers=headers)
        return EndpointInfo.from_dict(res)

    def list_endpoints(self, *, page_token: Optional[str] = None) -> Iterator[EndpointInfo]:
        """List all endpoints.
        
        :param page_token: str (optional)
          Token for pagination
        
        :returns: Iterator over :class:`EndpointInfo`
        """

        query = {}
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.0/vector-search/endpoints', query=query, headers=headers)
            if 'endpoints' in json:
                for v in json['endpoints']:
                    yield EndpointInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']


class VectorSearchIndexesAPI:
    """**Index**: An efficient representation of your embedding vectors that supports real-time and efficient
    approximate nearest neighbor (ANN) search queries.
    
    There are 2 types of Vector Search indexes: * **Delta Sync Index**: An index that automatically syncs with
    a source Delta Table, automatically and incrementally updating the index as the underlying data in the
    Delta Table changes. * **Direct Vector Access Index**: An index that supports direct read and write of
    vectors and metadata through our REST and SDK APIs. With this model, the user manages index updates."""

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
            direct_access_index_spec: Optional[DirectAccessVectorIndexSpec] = None
    ) -> CreateVectorIndexResponse:
        """Create an index.
        
        Create a new index.
        
        :param name: str
          Name of the index
        :param endpoint_name: str
          Name of the endpoint to be used for serving the index
        :param primary_key: str
          Primary key of the index
        :param index_type: :class:`VectorIndexType`
          There are 2 types of Vector Search indexes:
          
          - `DELTA_SYNC`: An index that automatically syncs with a source Delta Table, automatically and
          incrementally updating the index as the underlying data in the Delta Table changes. -
          `DIRECT_ACCESS`: An index that supports direct read and write of vectors and metadata through our
          REST and SDK APIs. With this model, the user manages index updates.
        :param delta_sync_index_spec: :class:`DeltaSyncVectorIndexSpecRequest` (optional)
          Specification for Delta Sync Index. Required if `index_type` is `DELTA_SYNC`.
        :param direct_access_index_spec: :class:`DirectAccessVectorIndexSpec` (optional)
          Specification for Direct Vector Access Index. Required if `index_type` is `DIRECT_ACCESS`.
        
        :returns: :class:`CreateVectorIndexResponse`
        """
        body = {}
        if delta_sync_index_spec is not None: body['delta_sync_index_spec'] = delta_sync_index_spec.as_dict()
        if direct_access_index_spec is not None:
            body['direct_access_index_spec'] = direct_access_index_spec.as_dict()
        if endpoint_name is not None: body['endpoint_name'] = endpoint_name
        if index_type is not None: body['index_type'] = index_type.value
        if name is not None: body['name'] = name
        if primary_key is not None: body['primary_key'] = primary_key
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.0/vector-search/indexes', body=body, headers=headers)
        return CreateVectorIndexResponse.from_dict(res)

    def delete_data_vector_index(self, index_name: str,
                                 primary_keys: List[str]) -> DeleteDataVectorIndexResponse:
        """Delete data from index.
        
        Handles the deletion of data from a specified vector index.
        
        :param index_name: str
          Name of the vector index where data is to be deleted. Must be a Direct Vector Access Index.
        :param primary_keys: List[str]
          List of primary keys for the data to be deleted.
        
        :returns: :class:`DeleteDataVectorIndexResponse`
        """
        body = {}
        if primary_keys is not None: body['primary_keys'] = [v for v in primary_keys]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/vector-search/indexes/{index_name}/delete-data',
                           body=body,
                           headers=headers)
        return DeleteDataVectorIndexResponse.from_dict(res)

    def delete_index(self, index_name: str):
        """Delete an index.
        
        Delete an index.
        
        :param index_name: str
          Name of the index
        
        
        """

        headers = {}

        self._api.do('DELETE', f'/api/2.0/vector-search/indexes/{index_name}', headers=headers)

    def get_index(self, index_name: str) -> VectorIndex:
        """Get an index.
        
        Get an index.
        
        :param index_name: str
          Name of the index
        
        :returns: :class:`VectorIndex`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/vector-search/indexes/{index_name}', headers=headers)
        return VectorIndex.from_dict(res)

    def list_indexes(self,
                     endpoint_name: str,
                     *,
                     page_token: Optional[str] = None) -> Iterator[MiniVectorIndex]:
        """List indexes.
        
        List all indexes in the given endpoint.
        
        :param endpoint_name: str
          Name of the endpoint
        :param page_token: str (optional)
          Token for pagination
        
        :returns: Iterator over :class:`MiniVectorIndex`
        """

        query = {}
        if endpoint_name is not None: query['endpoint_name'] = endpoint_name
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.0/vector-search/indexes', query=query, headers=headers)
            if 'vector_indexes' in json:
                for v in json['vector_indexes']:
                    yield MiniVectorIndex.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def query_index(self,
                    index_name: str,
                    columns: List[str],
                    *,
                    filters_json: Optional[str] = None,
                    num_results: Optional[int] = None,
                    query_text: Optional[str] = None,
                    query_type: Optional[str] = None,
                    query_vector: Optional[List[float]] = None,
                    score_threshold: Optional[float] = None) -> QueryVectorIndexResponse:
        """Query an index.
        
        Query the specified vector index.
        
        :param index_name: str
          Name of the vector index to query.
        :param columns: List[str]
          List of column names to include in the response.
        :param filters_json: str (optional)
          JSON string representing query filters.
          
          Example filters: - `{"id <": 5}`: Filter for id less than 5. - `{"id >": 5}`: Filter for id greater
          than 5. - `{"id <=": 5}`: Filter for id less than equal to 5. - `{"id >=": 5}`: Filter for id
          greater than equal to 5. - `{"id": 5}`: Filter for id equal to 5.
        :param num_results: int (optional)
          Number of results to return. Defaults to 10.
        :param query_text: str (optional)
          Query text. Required for Delta Sync Index using model endpoint.
        :param query_type: str (optional)
          The query type to use. Choices are `ANN` and `HYBRID`. Defaults to `ANN`.
        :param query_vector: List[float] (optional)
          Query vector. Required for Direct Vector Access Index and Delta Sync Index using self-managed
          vectors.
        :param score_threshold: float (optional)
          Threshold for the approximate nearest neighbor search. Defaults to 0.0.
        
        :returns: :class:`QueryVectorIndexResponse`
        """
        body = {}
        if columns is not None: body['columns'] = [v for v in columns]
        if filters_json is not None: body['filters_json'] = filters_json
        if num_results is not None: body['num_results'] = num_results
        if query_text is not None: body['query_text'] = query_text
        if query_type is not None: body['query_type'] = query_type
        if query_vector is not None: body['query_vector'] = [v for v in query_vector]
        if score_threshold is not None: body['score_threshold'] = score_threshold
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/vector-search/indexes/{index_name}/query',
                           body=body,
                           headers=headers)
        return QueryVectorIndexResponse.from_dict(res)

    def query_next_page(self,
                        index_name: str,
                        *,
                        endpoint_name: Optional[str] = None,
                        page_token: Optional[str] = None) -> QueryVectorIndexResponse:
        """Query next page.
        
        Use `next_page_token` returned from previous `QueryVectorIndex` or `QueryVectorIndexNextPage` request
        to fetch next page of results.
        
        :param index_name: str
          Name of the vector index to query.
        :param endpoint_name: str (optional)
          Name of the endpoint.
        :param page_token: str (optional)
          Page token returned from previous `QueryVectorIndex` or `QueryVectorIndexNextPage` API.
        
        :returns: :class:`QueryVectorIndexResponse`
        """
        body = {}
        if endpoint_name is not None: body['endpoint_name'] = endpoint_name
        if page_token is not None: body['page_token'] = page_token
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/vector-search/indexes/{index_name}/query-next-page',
                           body=body,
                           headers=headers)
        return QueryVectorIndexResponse.from_dict(res)

    def scan_index(self,
                   index_name: str,
                   *,
                   last_primary_key: Optional[str] = None,
                   num_results: Optional[int] = None) -> ScanVectorIndexResponse:
        """Scan an index.
        
        Scan the specified vector index and return the first `num_results` entries after the exclusive
        `primary_key`.
        
        :param index_name: str
          Name of the vector index to scan.
        :param last_primary_key: str (optional)
          Primary key of the last entry returned in the previous scan.
        :param num_results: int (optional)
          Number of results to return. Defaults to 10.
        
        :returns: :class:`ScanVectorIndexResponse`
        """
        body = {}
        if last_primary_key is not None: body['last_primary_key'] = last_primary_key
        if num_results is not None: body['num_results'] = num_results
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/vector-search/indexes/{index_name}/scan',
                           body=body,
                           headers=headers)
        return ScanVectorIndexResponse.from_dict(res)

    def sync_index(self, index_name: str):
        """Synchronize an index.
        
        Triggers a synchronization process for a specified vector index.
        
        :param index_name: str
          Name of the vector index to synchronize. Must be a Delta Sync Index.
        
        
        """

        headers = {}

        self._api.do('POST', f'/api/2.0/vector-search/indexes/{index_name}/sync', headers=headers)

    def upsert_data_vector_index(self, index_name: str, inputs_json: str) -> UpsertDataVectorIndexResponse:
        """Upsert data into an index.
        
        Handles the upserting of data into a specified vector index.
        
        :param index_name: str
          Name of the vector index where data is to be upserted. Must be a Direct Vector Access Index.
        :param inputs_json: str
          JSON string representing the data to be upserted.
        
        :returns: :class:`UpsertDataVectorIndexResponse`
        """
        body = {}
        if inputs_json is not None: body['inputs_json'] = inputs_json
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/vector-search/indexes/{index_name}/upsert-data',
                           body=body,
                           headers=headers)
        return UpsertDataVectorIndexResponse.from_dict(res)

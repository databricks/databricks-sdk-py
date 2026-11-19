# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.
# ruff: noqa: F811, F841
# F401 is intentionally NOT covered: `make fmt` uses `ruff check --fix-only`
# to strip the fat-import header below; ignoring F401 would defeat that.

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any, Optional


import logging

from databricks.sdk.service._internal import (
    _enum,
    _from_dict,
    _int64,
    _repeated_dict,
)


_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class BaseChunkInfo:
    """Metadata of one result set chunk, as listed in the result manifest."""

    byte_count: Optional[int] = None
    """The number of bytes in the result chunk. This field is not available when using ``INLINE``
    disposition."""

    chunk_index: Optional[int] = None
    """The position within the sequence of result set chunks."""

    row_count: Optional[int] = None
    """The number of rows within the result chunk."""

    row_offset: Optional[int] = None
    """The starting row offset within the result set."""

    def as_dict(self) -> dict:
        """Serializes the BaseChunkInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.byte_count is not None:
            body["byte_count"] = self.byte_count
        if self.chunk_index is not None:
            body["chunk_index"] = self.chunk_index
        if self.row_count is not None:
            body["row_count"] = self.row_count
        if self.row_offset is not None:
            body["row_offset"] = self.row_offset
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the BaseChunkInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.byte_count is not None:
            body["byte_count"] = self.byte_count
        if self.chunk_index is not None:
            body["chunk_index"] = self.chunk_index
        if self.row_count is not None:
            body["row_count"] = self.row_count
        if self.row_offset is not None:
            body["row_offset"] = self.row_offset
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> BaseChunkInfo:
        """Deserializes the BaseChunkInfo from a dictionary."""
        return cls(
            byte_count=_int64(d, "byte_count"),
            chunk_index=d.get("chunk_index", None),
            row_count=_int64(d, "row_count"),
            row_offset=_int64(d, "row_offset"),
        )


@dataclass
class CancelStatementResponse:
    """Empty response to a cancel request. Receiving it means the cancel request was accepted."""

    def as_dict(self) -> dict:
        """Serializes the CancelStatementResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CancelStatementResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CancelStatementResponse:
        """Deserializes the CancelStatementResponse from a dictionary."""
        return cls()


@dataclass
class ColumnInfo:
    """Describes one column of the result set: its name, SQL type, and position."""

    name: Optional[str] = None
    """The name of the column."""

    position: Optional[int] = None
    """The ordinal position of the column (starting at position 0)."""

    type_interval_type: Optional[str] = None
    """The format of the interval type."""

    type_name: Optional[ColumnTypeName] = None
    """The name of the base data type. This doesn't include details for complex types such as STRUCT,
    MAP or ARRAY."""

    type_precision: Optional[int] = None
    """Specifies the number of digits in a number. This applies to the DECIMAL type."""

    type_scale: Optional[int] = None
    """Specifies the number of digits to the right of the decimal point in a number. This applies to
    the DECIMAL type."""

    type_text: Optional[str] = None
    """The full SQL type specification."""

    def as_dict(self) -> dict:
        """Serializes the ColumnInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.position is not None:
            body["position"] = self.position
        if self.type_interval_type is not None:
            body["type_interval_type"] = self.type_interval_type
        if self.type_name is not None:
            body["type_name"] = self.type_name.value
        if self.type_precision is not None:
            body["type_precision"] = self.type_precision
        if self.type_scale is not None:
            body["type_scale"] = self.type_scale
        if self.type_text is not None:
            body["type_text"] = self.type_text
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ColumnInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.position is not None:
            body["position"] = self.position
        if self.type_interval_type is not None:
            body["type_interval_type"] = self.type_interval_type
        if self.type_name is not None:
            body["type_name"] = self.type_name
        if self.type_precision is not None:
            body["type_precision"] = self.type_precision
        if self.type_scale is not None:
            body["type_scale"] = self.type_scale
        if self.type_text is not None:
            body["type_text"] = self.type_text
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ColumnInfo:
        """Deserializes the ColumnInfo from a dictionary."""
        return cls(
            name=d.get("name", None),
            position=d.get("position", None),
            type_interval_type=d.get("type_interval_type", None),
            type_name=_enum(d, "type_name", ColumnTypeName),
            type_precision=d.get("type_precision", None),
            type_scale=d.get("type_scale", None),
            type_text=d.get("type_text", None),
        )


class ColumnTypeName(Enum):
    """The name of the base data type. This doesn't include details for complex types such as STRUCT,
    MAP or ARRAY."""

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
    USER_DEFINED_TYPE = "USER_DEFINED_TYPE"


@dataclass
class ExternalLink:
    """A short-lived cloud-storage link to one chunk of result data."""

    byte_count: Optional[int] = None
    """The number of bytes in the result chunk. This field is not available when using ``INLINE``
    disposition."""

    chunk_index: Optional[int] = None
    """The position within the sequence of result set chunks."""

    expiration: Optional[str] = None
    """Indicates the date-time that the given external link will expire and become invalid, after which
    point a new ``external_link`` must be requested."""

    external_link: Optional[str] = None
    """A short-lived cloud-storage URL pointing to a chunk of result data, hosted by an external
    service, with a short expiration time (<= 15 minutes). As this URL contains a temporary
    credential, it should be considered sensitive and the client should not expose this URL in a
    log."""

    http_headers: Optional[Dict[str, str]] = None
    """HTTP headers that must be included with a GET request to the ``external_link``. Each header is
    provided as a key-value pair. Headers are typically used to pass a decryption key to the
    external service. The values of these headers should be considered sensitive and the client
    should not expose these values in a log."""

    next_chunk_index: Optional[int] = None
    """When fetching, provides the ``chunk_index`` for the *next* chunk. If absent, indicates there are
    no more chunks. The next chunk can be fetched with a get-result-chunk request for that index."""

    next_chunk_internal_link: Optional[str] = None
    """When fetching, provides a link to fetch the *next* chunk. If absent, indicates there are no more
    chunks. This link is an absolute ``path`` to be joined with your ``$DATABRICKS_HOST``, and
    should be treated as an opaque link. This is an alternative to using ``next_chunk_index``.
    Lakehouse//RT warehouses currently don't return this field; use ``next_chunk_index`` instead."""

    row_count: Optional[int] = None
    """The number of rows within the result chunk."""

    row_offset: Optional[int] = None
    """The starting row offset within the result set."""

    def as_dict(self) -> dict:
        """Serializes the ExternalLink into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.byte_count is not None:
            body["byte_count"] = self.byte_count
        if self.chunk_index is not None:
            body["chunk_index"] = self.chunk_index
        if self.expiration is not None:
            body["expiration"] = self.expiration
        if self.external_link is not None:
            body["external_link"] = self.external_link
        if self.http_headers:
            body["http_headers"] = self.http_headers
        if self.next_chunk_index is not None:
            body["next_chunk_index"] = self.next_chunk_index
        if self.next_chunk_internal_link is not None:
            body["next_chunk_internal_link"] = self.next_chunk_internal_link
        if self.row_count is not None:
            body["row_count"] = self.row_count
        if self.row_offset is not None:
            body["row_offset"] = self.row_offset
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExternalLink into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.byte_count is not None:
            body["byte_count"] = self.byte_count
        if self.chunk_index is not None:
            body["chunk_index"] = self.chunk_index
        if self.expiration is not None:
            body["expiration"] = self.expiration
        if self.external_link is not None:
            body["external_link"] = self.external_link
        if self.http_headers:
            body["http_headers"] = self.http_headers
        if self.next_chunk_index is not None:
            body["next_chunk_index"] = self.next_chunk_index
        if self.next_chunk_internal_link is not None:
            body["next_chunk_internal_link"] = self.next_chunk_internal_link
        if self.row_count is not None:
            body["row_count"] = self.row_count
        if self.row_offset is not None:
            body["row_offset"] = self.row_offset
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ExternalLink:
        """Deserializes the ExternalLink from a dictionary."""
        return cls(
            byte_count=_int64(d, "byte_count"),
            chunk_index=d.get("chunk_index", None),
            expiration=d.get("expiration", None),
            external_link=d.get("external_link", None),
            http_headers=d.get("http_headers", None),
            next_chunk_index=d.get("next_chunk_index", None),
            next_chunk_internal_link=d.get("next_chunk_internal_link", None),
            row_count=_int64(d, "row_count"),
            row_offset=_int64(d, "row_offset"),
        )


class FetchDisposition(Enum):
    EXTERNAL_LINKS = "EXTERNAL_LINKS"
    INLINE = "INLINE"


class Format(Enum):
    """The format of the result data."""

    ARROW_STREAM = "ARROW_STREAM"
    CSV = "CSV"
    JSON_ARRAY = "JSON_ARRAY"


@dataclass
class QueryTag:
    """- A query execution can be annotated with an optional key-value pair to allow users to attribute
    the executions by key and optional value to filter by. QueryTag is the user-facing
    representation."""

    key: str
    """The key of the tag."""

    value: Optional[str] = None
    """The value of the tag. Key-only tags have no value."""

    def as_dict(self) -> dict:
        """Serializes the QueryTag into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.key is not None:
            body["key"] = self.key
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the QueryTag into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.key is not None:
            body["key"] = self.key
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> QueryTag:
        """Deserializes the QueryTag from a dictionary."""
        return cls(key=d.get("key", None), value=d.get("value", None))


@dataclass
class ResultData:
    """Contains the result data of a single chunk when using ``INLINE`` disposition. When using
    ``EXTERNAL_LINKS`` disposition, the array ``external_links`` is used instead to provide
    short-lived cloud-storage URLs to the result data in cloud storage. Exactly one of these
    alternatives is used. (While the ``external_links`` array prepares the API to return multiple
    links in a single response, currently only a single link is returned.)"""

    byte_count: Optional[int] = None
    """The number of bytes in the result chunk. This field is not available when using ``INLINE``
    disposition."""

    chunk_index: Optional[int] = None
    """The position within the sequence of result set chunks."""

    data_array: Optional[List[List[any]]] = None
    """The ``JSON_ARRAY`` format is an array of arrays of values, where each non-null value is
    formatted as a string. Null values are encoded as JSON ``null``."""

    external_links: Optional[List[ExternalLink]] = None
    """Short-lived cloud-storage links to the result data, used with the ``EXTERNAL_LINKS``
    disposition."""

    next_chunk_index: Optional[int] = None
    """When fetching, provides the ``chunk_index`` for the *next* chunk. If absent, indicates there are
    no more chunks. The next chunk can be fetched with a get-result-chunk request for that index."""

    next_chunk_internal_link: Optional[str] = None
    """When fetching, provides a link to fetch the *next* chunk. If absent, indicates there are no more
    chunks. This link is an absolute ``path`` to be joined with your ``$DATABRICKS_HOST``, and
    should be treated as an opaque link. This is an alternative to using ``next_chunk_index``.
    Lakehouse//RT warehouses currently don't return this field; use ``next_chunk_index`` instead."""

    row_count: Optional[int] = None
    """The number of rows within the result chunk."""

    row_offset: Optional[int] = None
    """The starting row offset within the result set."""

    def as_dict(self) -> dict:
        """Serializes the ResultData into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.byte_count is not None:
            body["byte_count"] = self.byte_count
        if self.chunk_index is not None:
            body["chunk_index"] = self.chunk_index
        if self.data_array:
            body["data_array"] = [v for v in self.data_array]
        if self.external_links:
            body["external_links"] = [v.as_dict() for v in self.external_links]
        if self.next_chunk_index is not None:
            body["next_chunk_index"] = self.next_chunk_index
        if self.next_chunk_internal_link is not None:
            body["next_chunk_internal_link"] = self.next_chunk_internal_link
        if self.row_count is not None:
            body["row_count"] = self.row_count
        if self.row_offset is not None:
            body["row_offset"] = self.row_offset
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ResultData into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.byte_count is not None:
            body["byte_count"] = self.byte_count
        if self.chunk_index is not None:
            body["chunk_index"] = self.chunk_index
        if self.data_array:
            body["data_array"] = self.data_array
        if self.external_links:
            body["external_links"] = self.external_links
        if self.next_chunk_index is not None:
            body["next_chunk_index"] = self.next_chunk_index
        if self.next_chunk_internal_link is not None:
            body["next_chunk_internal_link"] = self.next_chunk_internal_link
        if self.row_count is not None:
            body["row_count"] = self.row_count
        if self.row_offset is not None:
            body["row_offset"] = self.row_offset
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResultData:
        """Deserializes the ResultData from a dictionary."""
        return cls(
            byte_count=_int64(d, "byte_count"),
            chunk_index=d.get("chunk_index", None),
            data_array=d.get("data_array", None),
            external_links=_repeated_dict(d, "external_links", ExternalLink),
            next_chunk_index=d.get("next_chunk_index", None),
            next_chunk_internal_link=d.get("next_chunk_internal_link", None),
            row_count=_int64(d, "row_count"),
            row_offset=_int64(d, "row_offset"),
        )


@dataclass
class ResultManifest:
    """The result manifest provides schema and metadata for the result set."""

    chunks: Optional[List[BaseChunkInfo]] = None
    """Array of result set chunk metadata."""

    format: Optional[Format] = None
    """The format of the result data, as requested with ``format``."""

    schema: Optional[Schema] = None
    """The schema of the result set: the ordered list of column descriptions."""

    total_byte_count: Optional[int] = None
    """The total number of bytes in the result set. This field is not available when using ``INLINE``
    disposition."""

    total_chunk_count: Optional[int] = None
    """The total number of chunks that the result set has been divided into."""

    total_row_count: Optional[int] = None
    """The total number of rows in the result set."""

    truncated: Optional[bool] = None
    """Indicates whether the result is truncated due to ``row_limit`` or ``byte_limit``."""

    def as_dict(self) -> dict:
        """Serializes the ResultManifest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.chunks:
            body["chunks"] = [v.as_dict() for v in self.chunks]
        if self.format is not None:
            body["format"] = self.format.value
        if self.schema:
            body["schema"] = self.schema.as_dict()
        if self.total_byte_count is not None:
            body["total_byte_count"] = self.total_byte_count
        if self.total_chunk_count is not None:
            body["total_chunk_count"] = self.total_chunk_count
        if self.total_row_count is not None:
            body["total_row_count"] = self.total_row_count
        if self.truncated is not None:
            body["truncated"] = self.truncated
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ResultManifest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.chunks:
            body["chunks"] = self.chunks
        if self.format is not None:
            body["format"] = self.format
        if self.schema:
            body["schema"] = self.schema
        if self.total_byte_count is not None:
            body["total_byte_count"] = self.total_byte_count
        if self.total_chunk_count is not None:
            body["total_chunk_count"] = self.total_chunk_count
        if self.total_row_count is not None:
            body["total_row_count"] = self.total_row_count
        if self.truncated is not None:
            body["truncated"] = self.truncated
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResultManifest:
        """Deserializes the ResultManifest from a dictionary."""
        return cls(
            chunks=_repeated_dict(d, "chunks", BaseChunkInfo),
            format=_enum(d, "format", Format),
            schema=_from_dict(d, "schema", Schema),
            total_byte_count=_int64(d, "total_byte_count"),
            total_chunk_count=d.get("total_chunk_count", None),
            total_row_count=_int64(d, "total_row_count"),
            truncated=d.get("truncated", None),
        )


@dataclass
class Schema:
    """The schema is an ordered list of column descriptions."""

    column_count: Optional[int] = None
    """The number of columns in the result set."""

    columns: Optional[List[ColumnInfo]] = None
    """The column descriptions, in result set order."""

    def as_dict(self) -> dict:
        """Serializes the Schema into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.column_count is not None:
            body["column_count"] = self.column_count
        if self.columns:
            body["columns"] = [v.as_dict() for v in self.columns]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Schema into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.column_count is not None:
            body["column_count"] = self.column_count
        if self.columns:
            body["columns"] = self.columns
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Schema:
        """Deserializes the Schema from a dictionary."""
        return cls(column_count=d.get("column_count", None), columns=_repeated_dict(d, "columns", ColumnInfo))


@dataclass
class ServiceError:
    """The error that caused a statement execution to fail."""

    error_code: Optional[ServiceErrorCode] = None
    """The error code that classifies the failure."""

    message: Optional[str] = None
    """A brief summary of the error condition."""

    def as_dict(self) -> dict:
        """Serializes the ServiceError into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.error_code is not None:
            body["error_code"] = self.error_code.value
        if self.message is not None:
            body["message"] = self.message
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServiceError into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.error_code is not None:
            body["error_code"] = self.error_code
        if self.message is not None:
            body["message"] = self.message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ServiceError:
        """Deserializes the ServiceError from a dictionary."""
        return cls(error_code=_enum(d, "error_code", ServiceErrorCode), message=d.get("message", None))


class ServiceErrorCode(Enum):
    """Error codes that classify a failed statement execution."""

    ABORTED = "ABORTED"
    ALREADY_EXISTS = "ALREADY_EXISTS"
    BAD_REQUEST = "BAD_REQUEST"
    CANCELLED = "CANCELLED"
    DEADLINE_EXCEEDED = "DEADLINE_EXCEEDED"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    IO_ERROR = "IO_ERROR"
    NOT_FOUND = "NOT_FOUND"
    RESOURCE_EXHAUSTED = "RESOURCE_EXHAUSTED"
    SERVICE_UNDER_MAINTENANCE = "SERVICE_UNDER_MAINTENANCE"
    TEMPORARILY_UNAVAILABLE = "TEMPORARILY_UNAVAILABLE"
    UNAUTHENTICATED = "UNAUTHENTICATED"
    UNKNOWN = "UNKNOWN"
    WORKSPACE_TEMPORARILY_UNAVAILABLE = "WORKSPACE_TEMPORARILY_UNAVAILABLE"


@dataclass
class StatementParameter:
    """A named parameter to substitute for a parameter marker in the statement."""

    name: str
    """The name of a parameter marker to be substituted in the statement."""

    type: Optional[str] = None
    """The data type, given as a string. For example: ``INT``, ``STRING``, ``DECIMAL(10,2)``. If no
    type is given the type is assumed to be ``STRING``. Complex types, such as ``ARRAY``, ``MAP``,
    and ``STRUCT`` are not supported. For valid types, refer to the section `Data types
    <https://docs.databricks.com/sql/language-manual/functions/cast.html>`__ of the SQL language
    reference."""

    value: Optional[str] = None
    """The value to substitute, represented as a string. If omitted, the value is interpreted as NULL."""

    def as_dict(self) -> dict:
        """Serializes the StatementParameter into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.type is not None:
            body["type"] = self.type
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the StatementParameter into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        if self.type is not None:
            body["type"] = self.type
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> StatementParameter:
        """Deserializes the StatementParameter from a dictionary."""
        return cls(name=d.get("name", None), type=d.get("type", None), value=d.get("value", None))


@dataclass
class StatementResponse:
    """Statement Execution (Lakehouse//RT) is version 2 of the Statement Execution API. It is optimized
    for Lakehouse//RT warehouses, with lower latency and higher concurrency, and takes
    ``warehouse_id`` as a path parameter on every call. It currently supports Lakehouse//RT
    warehouses only. The Statement Execution API (version 1) works with all SQL warehouse types,
    including Lakehouse//RT."""

    manifest: Optional[ResultManifest] = None
    """The schema and metadata of the result set. Present when ``status.state`` is ``SUCCEEDED``."""

    result: Optional[ResultData] = None
    """The first chunk of result data. Present when ``status.state`` is ``SUCCEEDED``."""

    statement_id: Optional[str] = None
    """The statement ID is returned upon successfully submitting a SQL statement, and is a required
    reference for all subsequent calls."""

    status: Optional[StatementStatus] = None
    """The execution state of the statement and, if it failed, the error details."""

    def as_dict(self) -> dict:
        """Serializes the StatementResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.manifest:
            body["manifest"] = self.manifest.as_dict()
        if self.result:
            body["result"] = self.result.as_dict()
        if self.statement_id is not None:
            body["statement_id"] = self.statement_id
        if self.status:
            body["status"] = self.status.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the StatementResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.manifest:
            body["manifest"] = self.manifest
        if self.result:
            body["result"] = self.result
        if self.statement_id is not None:
            body["statement_id"] = self.statement_id
        if self.status:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> StatementResponse:
        """Deserializes the StatementResponse from a dictionary."""
        return cls(
            manifest=_from_dict(d, "manifest", ResultManifest),
            result=_from_dict(d, "result", ResultData),
            statement_id=d.get("statement_id", None),
            status=_from_dict(d, "status", StatementStatus),
        )


@dataclass
class StatementStatus:
    """The status response includes execution state and if relevant, error information."""

    error: Optional[ServiceError] = None
    """The error details. Only populated when ``state`` is ``FAILED``."""

    sql_state: Optional[str] = None
    """SQLSTATE error code returned when the statement execution fails. Only populated when the
    statement status is ``FAILED``."""

    state: Optional[StatementStatusState] = None
    """Statement execution state:
    
    - ``PENDING``: waiting for warehouse
    - ``RUNNING``: running
    - ``SUCCEEDED``: execution was successful, result data available for fetch
    - ``FAILED``: execution failed; reason for failure described in accompanying error message
    - ``CANCELED``: user canceled; can come from explicit cancel call, or timeout with
      ``on_wait_timeout=CANCEL``
    - ``CLOSED``: execution successful, and statement closed; result no longer available for fetch"""

    def as_dict(self) -> dict:
        """Serializes the StatementStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.error:
            body["error"] = self.error.as_dict()
        if self.sql_state is not None:
            body["sql_state"] = self.sql_state
        if self.state is not None:
            body["state"] = self.state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the StatementStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.error:
            body["error"] = self.error
        if self.sql_state is not None:
            body["sql_state"] = self.sql_state
        if self.state is not None:
            body["state"] = self.state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> StatementStatus:
        """Deserializes the StatementStatus from a dictionary."""
        return cls(
            error=_from_dict(d, "error", ServiceError),
            sql_state=d.get("sql_state", None),
            state=_enum(d, "state", StatementStatusState),
        )


class StatementStatusState(Enum):
    """Statement execution state."""

    CANCELED = "CANCELED"
    CLOSED = "CLOSED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"


class TimeoutAction(Enum):
    """What happens when the statement execution outlives ``wait_timeout``."""

    CANCEL = "CANCEL"
    CONTINUE = "CONTINUE"


class StatementExecutionV2API:
    """The Statement Execution API v2 can be used to execute SQL statements on a SQL warehouse and fetch the
    result. It works the same as the Statement Execution API (v1), except that ``warehouse_id`` is a path
    parameter on every call, including polling, fetching result chunks, and canceling. Routing on the
    warehouse ID gives lower latency and higher concurrency.

    Version 2 currently supports `Lakehouse//RT
    <https://docs.databricks.com/compute/sql-warehouse/real-time.html>`__ warehouses only. For other warehouse
    types, use the Statement Execution API (v1). You can also run statements on Lakehouse//RT warehouses with
    version 1, but version 2 is optimized for them."""

    def __init__(self, api_client):
        self._api = api_client

    def cancel_statement(self, warehouse_id: str, statement_id: str) -> CancelStatementResponse:
        """Requests that an executing statement be canceled. Callers must poll for status to see the terminal
        state. The cancel response is empty; receiving a response indicates successful receipt.

        :param warehouse_id: str
          The ID of the SQL warehouse that ran the statement.
        :param statement_id: str
          The statement ID is returned upon successfully submitting a SQL statement, and is a required
          reference for all subsequent calls.

        :returns: :class:`CancelStatementResponse`
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
            "POST",
            f"/api/2.0/sql/warehouses/{warehouse_id}/statements/{statement_id}/cancel",
            body=body,
            headers=headers,
        )
        return CancelStatementResponse.from_dict(res)

    def execute_statement(
        self,
        warehouse_id: str,
        statement: str,
        *,
        byte_limit: Optional[int] = None,
        catalog: Optional[str] = None,
        disposition: Optional[FetchDisposition] = None,
        format: Optional[Format] = None,
        on_wait_timeout: Optional[TimeoutAction] = None,
        parameters: Optional[List[StatementParameter]] = None,
        query_tags: Optional[List[QueryTag]] = None,
        row_limit: Optional[int] = None,
        schema: Optional[str] = None,
        wait_timeout: Optional[str] = None,
    ) -> StatementResponse:
        """Execute a SQL statement and optionally await its results for a specified time.

        **Use case: small result sets with INLINE + JSON_ARRAY**

        For flows that generate small and predictable result sets (<= 25 MiB), ``INLINE`` responses of
        ``JSON_ARRAY`` result data are typically the simplest way to execute and fetch result data.

        **Use case: large result sets with EXTERNAL_LINKS**

        Using ``EXTERNAL_LINKS`` to fetch result data allows you to fetch large result sets efficiently. The
        main differences from using ``INLINE`` disposition are that the result data is accessed with
        short-lived cloud-storage URLs, and that there are 3 supported formats: ``JSON_ARRAY``,
        ``ARROW_STREAM`` and ``CSV`` compared to only ``JSON_ARRAY`` with ``INLINE``.

        **External-link URLs**

        External links point to data stored within your workspace's internal cloud storage. The URLs are valid
        for only a short period, <= 15 minutes. Alongside each ``external_link`` is an expiration field
        indicating the time at which the URL is no longer valid. In ``EXTERNAL_LINKS`` mode, chunks can be
        resolved and fetched multiple times and in parallel.

        **Warning: Databricks strongly recommends that you protect the URLs that are returned by the
        ``EXTERNAL_LINKS`` disposition.**

        When you use the ``EXTERNAL_LINKS`` disposition, a short-lived cloud-storage URL is generated to
        download the results. The URL contains temporary access credentials, so protect it and do not set an
        ``Authorization`` header in the download request.

        The ``EXTERNAL_LINKS`` disposition can be disabled upon request by creating a `support case
        <https://docs.databricks.com/resources/support.html>`__.

        See also `Security best practices
        <https://docs.databricks.com/sql/admin/sql-execution-tutorial.html#security-best-practices>`__.

        StatementResponse contains ``statement_id`` and ``status``; other fields might be absent or present
        depending on context. If the SQL warehouse fails to execute the provided statement, a 200 response is
        returned with ``status.state`` set to ``FAILED`` (in contrast to a failure when accepting the request,
        which results in a non-200 response). Details of the error can be found at ``status.error`` in case of
        execution failures.

        :param warehouse_id: str
          The ID of the SQL warehouse to run the statement on. Currently, only `Lakehouse//RT
          <https://docs.databricks.com/compute/sql-warehouse/real-time.html>`__ warehouses are supported. See
          also `What are SQL warehouses? <https://docs.databricks.com/sql/admin/warehouse-type.html>`__.
        :param statement: str
          The SQL statement to execute. The statement can optionally be parameterized, see ``parameters``. The
          maximum query text size is 16 MiB.
        :param byte_limit: int (optional)
          Applies the given byte limit to the statement's result size. Byte counts are based on internal data
          representations and might not match the final size in the requested ``format``. If the result was
          truncated due to the byte limit, then ``truncated`` in the response is set to ``true``. When using
          ``EXTERNAL_LINKS`` disposition, a default ``byte_limit`` of 100 GiB is applied if ``byte_limit`` is
          not explicitly set.
        :param catalog: str (optional)
          Sets default catalog for statement execution, similar to `USE CATALOG
          <https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-catalog.html>`__ in SQL.
        :param disposition: :class:`FetchDisposition` (optional)
          The fetch disposition provides two modes of fetching results: ``INLINE`` and ``EXTERNAL_LINKS``.

          Statements executed with ``INLINE`` disposition will return result data inline, in ``JSON_ARRAY``
          format, in a series of chunks. If a given statement produces a result set with a size larger than 25
          MiB, that statement execution is aborted, and no result set will be available.

          **NOTE** Byte limits are computed based upon internal representations of the result set data, and
          might not match the sizes visible in JSON responses.

          Statements executed with ``EXTERNAL_LINKS`` disposition will return result data as external links:
          URLs that point to cloud storage internal to the workspace. Using ``EXTERNAL_LINKS`` disposition
          allows statements to generate arbitrarily sized result sets for fetching up to 100 GiB. The
          resulting links have two important properties:

          1. They point to resources *external* to the Databricks compute; therefore any associated
             authentication information (typically a personal access token, OAuth token, or similar) *must be
             removed* when fetching from these links.
          2. These are short-lived cloud-storage URLs with a specific expiration, indicated in the response.
             The behavior when attempting to use an expired link is cloud specific.
        :param format: :class:`Format` (optional)
          Statement execution supports three result formats: ``JSON_ARRAY``, ``ARROW_STREAM``, and ``CSV``.
          Set ``format`` explicitly: on Lakehouse//RT warehouses, an omitted ``format`` with the ``INLINE``
          disposition currently returns Arrow data rather than ``JSON_ARRAY``.

          Important: The formats ``ARROW_STREAM`` and ``CSV`` are supported only with ``EXTERNAL_LINKS``
          disposition. ``JSON_ARRAY`` is supported in ``INLINE`` and ``EXTERNAL_LINKS`` disposition.

          When specifying ``format=JSON_ARRAY``, result data will be formatted as an array of arrays of
          values, where each value is either the *string representation* of a value, or ``null``. For example,
          the output of ``SELECT concat('id-', id) AS strCol, id AS intCol, null AS nullCol FROM range(3)``
          would look like this:

          .. code-block::

             [
             [ "id-1", "1", null ],
             [ "id-2", "2", null ],
             [ "id-3", "3", null ],
             ]

          When specifying ``format=JSON_ARRAY`` and ``disposition=EXTERNAL_LINKS``, each chunk in the result
          contains compact JSON with no indentation or extra whitespace.

          When specifying ``format=ARROW_STREAM`` and ``disposition=EXTERNAL_LINKS``, each chunk in the result
          will be formatted as Apache Arrow Stream. See the `Apache Arrow streaming format
          <https://arrow.apache.org/docs/format/Columnar.html#ipc-streaming-format>`__.

          When specifying ``format=CSV`` and ``disposition=EXTERNAL_LINKS``, each chunk in the result will be
          a CSV according to `RFC 4180 <https://www.rfc-editor.org/rfc/rfc4180>`__ standard. All column values
          will have *string representation* similar to the ``JSON_ARRAY`` format, and ``null`` values will be
          encoded as “null”. Only the first chunk in the result would contain a header row with column
          names. For example, the output of ``SELECT concat('id-', id) AS strCol, id AS intCol, null as
          nullCol FROM range(3)`` would look like this:

          .. code-block::

             strCol,intCol,nullCol
             id-1,1,null
             id-2,2,null
             id-3,3,null
        :param on_wait_timeout: :class:`TimeoutAction` (optional)
          When ``wait_timeout > 0s``, the call will block up to the specified time. If the statement execution
          doesn't finish within this time, ``on_wait_timeout`` determines whether the execution should
          continue or be canceled. When set to ``CONTINUE``, the statement execution continues asynchronously
          and the call returns a statement ID which can be used for polling the statement status. When set to
          ``CANCEL``, the statement execution is canceled and the call returns with a ``CANCELED`` state.
          Lakehouse//RT warehouses currently don't support ``CANCEL``: the statement keeps running as with
          ``CONTINUE``.
        :param parameters: List[:class:`StatementParameter`] (optional)
          A list of parameters to pass into a SQL statement containing parameter markers. A parameter consists
          of a name, a value, and optionally a type. To represent a NULL value, the ``value`` field may be
          omitted or set to ``null`` explicitly. If the ``type`` field is omitted, the value is interpreted as
          a string.

          If the type is given, parameters will be checked for type correctness according to the given type. A
          value is correct if the provided string can be converted to the requested type using the ``cast``
          function. The exact semantics are described in the section `cast function
          <https://docs.databricks.com/sql/language-manual/functions/cast.html>`__ of the SQL language
          reference.

          For example, the following statement contains two parameters, ``my_name`` and ``my_date``:

          .. code-block::

             SELECT * FROM my_table WHERE name = :my_name AND date = :my_date

          The parameters can be passed in the request body as follows:

          .. code-block::

             {
             ...,
             "statement": "SELECT * FROM my_table WHERE name = :my_name AND date = :my_date",
             "parameters": [
             { "name": "my_name", "value": "the name" },
             { "name": "my_date", "value": "2020-01-01", "type": "DATE" }
             ]
             }

          Currently, positional parameters denoted by a ``?`` marker are not supported by the Databricks SQL
          Statement Execution API.

          Also see the section `Parameter markers
          <https://docs.databricks.com/sql/language-manual/sql-ref-parameter-marker.html>`__ of the SQL
          language reference.
        :param query_tags: List[:class:`QueryTag`] (optional)
          An array of query tags to annotate a SQL statement. A query tag consists of a non-empty key and,
          optionally, a value. To represent a NULL value, either omit the ``value`` field or manually set it
          to ``null`` or white space. Refer to the SQL language reference for the format specification of
          query tags. There's no significance to the order of tags. Only one value per key will be recorded. A
          sequence in excess of 20 query tags will be coerced to 20. Example:

          { ..., "query_tags": [ { "key": "team", "value": "eng" }, { "key": "some key only tag" } ] }
        :param row_limit: int (optional)
          Applies the given row limit to the statement's result set, but unlike the ``LIMIT`` clause in SQL,
          it also sets the ``truncated`` field in the response to indicate whether the result was trimmed due
          to the limit or not.
        :param schema: str (optional)
          Sets default schema for statement execution, similar to `USE SCHEMA
          <https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-schema.html>`__ in SQL.
        :param wait_timeout: str (optional)
          The time in seconds the call will wait for the statement's result set as ``Ns``, where ``N`` can be
          set to 0 or to a value between 5 and 50.

          When set to ``0s``, the statement will execute in asynchronous mode and the call will not wait for
          the execution to finish. In this case, the call returns directly with ``PENDING`` state and a
          statement ID which can be used for polling the statement status.

          When set between 5 and 50 seconds, the call will behave synchronously up to this timeout and wait
          for the statement execution to finish. If the execution finishes within this time, the call returns
          immediately with a manifest and result data (or a ``FAILED`` state in case of an execution error).
          If the statement takes longer to execute, ``on_wait_timeout`` determines what should happen after
          the timeout is reached.

        :returns: :class:`StatementResponse`
        """

        body = {}
        if byte_limit is not None:
            body["byte_limit"] = byte_limit
        if catalog is not None:
            body["catalog"] = catalog
        if disposition is not None:
            body["disposition"] = disposition.value
        if format is not None:
            body["format"] = format.value
        if on_wait_timeout is not None:
            body["on_wait_timeout"] = on_wait_timeout.value
        if parameters is not None:
            body["parameters"] = [v.as_dict() for v in parameters]
        if query_tags is not None:
            body["query_tags"] = [v.as_dict() for v in query_tags]
        if row_limit is not None:
            body["row_limit"] = row_limit
        if schema is not None:
            body["schema"] = schema
        if statement is not None:
            body["statement"] = statement
        if wait_timeout is not None:
            body["wait_timeout"] = wait_timeout
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/sql/warehouses/{warehouse_id}/statements", body=body, headers=headers)
        return StatementResponse.from_dict(res)

    def get_result_data(self, warehouse_id: str, statement_id: str, chunk_index: int) -> ResultData:
        """After the statement execution has ``SUCCEEDED``, this request can be used to fetch any chunk by index.
        Whereas the first chunk with ``chunk_index=0`` is typically fetched with the execute or the get-status
        request, this request can be used to fetch subsequent chunks. The response structure is identical to
        the nested ``result`` element of those responses, and similarly includes the ``next_chunk_index``
        field for simple iteration through the result set. Depending on ``disposition``, the response returns
        chunks of data either inline, or as links.

        :param warehouse_id: str
          The ID of the SQL warehouse that ran the statement.
        :param statement_id: str
          The statement ID is returned upon successfully submitting a SQL statement, and is a required
          reference for all subsequent calls.
        :param chunk_index: int
          The zero-based index of the result chunk to fetch.

        :returns: :class:`ResultData`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "GET",
            f"/api/2.0/sql/warehouses/{warehouse_id}/statements/{statement_id}/result/chunks/{chunk_index}",
            headers=headers,
        )
        return ResultData.from_dict(res)

    def get_statement_result(self, warehouse_id: str, statement_id: str) -> StatementResponse:
        """This request can be used to poll for the statement's status. StatementResponse contains
        ``statement_id`` and ``status``; other fields might be absent or present depending on context. When
        the ``status.state`` field is ``SUCCEEDED`` it will also return the result manifest and the first
        chunk of the result data. When the statement is in the terminal states ``CANCELED``, ``CLOSED`` or
        ``FAILED``, it returns HTTP 200 with the state set. After at least 12 hours in a terminal state, the
        statement is removed from the warehouse and further calls will receive an HTTP 404 response.

        **NOTE** This call currently might take up to 5 seconds to get the latest status and result.

        :param warehouse_id: str
          The ID of the SQL warehouse that ran the statement.
        :param statement_id: str
          The statement ID is returned upon successfully submitting a SQL statement, and is a required
          reference for all subsequent calls.

        :returns: :class:`StatementResponse`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/sql/warehouses/{warehouse_id}/statements/{statement_id}", headers=headers)
        return StatementResponse.from_dict(res)

# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from ...service._internal import _enum, _from_dict, _repeated_dict

_LOG = logging.getLogger("databricks.sdk")

# all definitions in this file are in alphabetical order


@dataclass
class BaseChunkInfo:
    """Describes metadata for a particular chunk, within a result set; this structure is used both
    within a manifest, and when fetching individual chunk data or links."""

    byte_count: Optional[int] = None
    """The number of bytes in the result chunk. This field is not available when using `INLINE`
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
            byte_count=d.get("byte_count", None),
            chunk_index=d.get("chunk_index", None),
            row_count=d.get("row_count", None),
            row_offset=d.get("row_offset", None),
        )


@dataclass
class CancelQueryExecutionResponse:
    status: Optional[List[CancelQueryExecutionResponseStatus]] = None

    def as_dict(self) -> dict:
        """Serializes the CancelQueryExecutionResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.status:
            body["status"] = [v.as_dict() for v in self.status]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CancelQueryExecutionResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.status:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CancelQueryExecutionResponse:
        """Deserializes the CancelQueryExecutionResponse from a dictionary."""
        return cls(status=_repeated_dict(d, "status", CancelQueryExecutionResponseStatus))


@dataclass
class CancelQueryExecutionResponseStatus:
    data_token: str
    """The token to poll for result asynchronously Example:
    EC0A..ChAB7WCEn_4Qo4vkLqEbXsxxEgh3Y2pbWw45WhoQXgZSQo9aS5q2ZvFcbvbx9CgA-PAEAQ"""

    pending: Optional[Empty] = None
    """Represents an empty message, similar to google.protobuf.Empty, which is not available in the
    firm right now."""

    success: Optional[Empty] = None
    """Represents an empty message, similar to google.protobuf.Empty, which is not available in the
    firm right now."""

    def as_dict(self) -> dict:
        """Serializes the CancelQueryExecutionResponseStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.data_token is not None:
            body["data_token"] = self.data_token
        if self.pending:
            body["pending"] = self.pending.as_dict()
        if self.success:
            body["success"] = self.success.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CancelQueryExecutionResponseStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.data_token is not None:
            body["data_token"] = self.data_token
        if self.pending:
            body["pending"] = self.pending
        if self.success:
            body["success"] = self.success
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CancelQueryExecutionResponseStatus:
        """Deserializes the CancelQueryExecutionResponseStatus from a dictionary."""
        return cls(
            data_token=d.get("data_token", None),
            pending=_from_dict(d, "pending", Empty),
            success=_from_dict(d, "success", Empty),
        )


@dataclass
class ColumnInfo:
    name: Optional[str] = None
    """The name of the column."""

    position: Optional[int] = None
    """The ordinal position of the column (starting at position 0)."""

    type_interval_type: Optional[str] = None
    """The format of the interval type."""

    type_name: Optional[ColumnInfoTypeName] = None
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
            type_name=_enum(d, "type_name", ColumnInfoTypeName),
            type_precision=d.get("type_precision", None),
            type_scale=d.get("type_scale", None),
            type_text=d.get("type_text", None),
        )


class ColumnInfoTypeName(Enum):
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
class CronSchedule:
    quartz_cron_expression: str
    """A cron expression using quartz syntax. EX: `0 0 8 * * ?` represents everyday at 8am. See [Cron
    Trigger] for details.
    
    [Cron Trigger]: http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html"""

    timezone_id: str
    """A Java timezone id. The schedule will be resolved with respect to this timezone. See [Java
    TimeZone] for details.
    
    [Java TimeZone]: https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html"""

    def as_dict(self) -> dict:
        """Serializes the CronSchedule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.quartz_cron_expression is not None:
            body["quartz_cron_expression"] = self.quartz_cron_expression
        if self.timezone_id is not None:
            body["timezone_id"] = self.timezone_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CronSchedule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.quartz_cron_expression is not None:
            body["quartz_cron_expression"] = self.quartz_cron_expression
        if self.timezone_id is not None:
            body["timezone_id"] = self.timezone_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CronSchedule:
        """Deserializes the CronSchedule from a dictionary."""
        return cls(quartz_cron_expression=d.get("quartz_cron_expression", None), timezone_id=d.get("timezone_id", None))


@dataclass
class Dashboard:
    create_time: Optional[str] = None
    """The timestamp of when the dashboard was created."""

    dashboard_id: Optional[str] = None
    """UUID identifying the dashboard."""

    display_name: Optional[str] = None
    """The display name of the dashboard."""

    etag: Optional[str] = None
    """The etag for the dashboard. Can be optionally provided on updates to ensure that the dashboard
    has not been modified since the last read. This field is excluded in List Dashboards responses."""

    lifecycle_state: Optional[LifecycleState] = None
    """The state of the dashboard resource. Used for tracking trashed status."""

    parent_path: Optional[str] = None
    """The workspace path of the folder containing the dashboard. Includes leading slash and no
    trailing slash. This field is excluded in List Dashboards responses."""

    path: Optional[str] = None
    """The workspace path of the dashboard asset, including the file name. Exported dashboards always
    have the file extension `.lvdash.json`. This field is excluded in List Dashboards responses."""

    serialized_dashboard: Optional[str] = None
    """The contents of the dashboard in serialized string form. This field is excluded in List
    Dashboards responses. Use the [get dashboard API] to retrieve an example response, which
    includes the `serialized_dashboard` field. This field provides the structure of the JSON string
    that represents the dashboard's layout and components.
    
    [get dashboard API]: https://docs.databricks.com/api/workspace/lakeview/get"""

    update_time: Optional[str] = None
    """The timestamp of when the dashboard was last updated by the user. This field is excluded in List
    Dashboards responses."""

    warehouse_id: Optional[str] = None
    """The warehouse ID used to run the dashboard."""

    def as_dict(self) -> dict:
        """Serializes the Dashboard into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.dashboard_id is not None:
            body["dashboard_id"] = self.dashboard_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.etag is not None:
            body["etag"] = self.etag
        if self.lifecycle_state is not None:
            body["lifecycle_state"] = self.lifecycle_state.value
        if self.parent_path is not None:
            body["parent_path"] = self.parent_path
        if self.path is not None:
            body["path"] = self.path
        if self.serialized_dashboard is not None:
            body["serialized_dashboard"] = self.serialized_dashboard
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Dashboard into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.dashboard_id is not None:
            body["dashboard_id"] = self.dashboard_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.etag is not None:
            body["etag"] = self.etag
        if self.lifecycle_state is not None:
            body["lifecycle_state"] = self.lifecycle_state
        if self.parent_path is not None:
            body["parent_path"] = self.parent_path
        if self.path is not None:
            body["path"] = self.path
        if self.serialized_dashboard is not None:
            body["serialized_dashboard"] = self.serialized_dashboard
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Dashboard:
        """Deserializes the Dashboard from a dictionary."""
        return cls(
            create_time=d.get("create_time", None),
            dashboard_id=d.get("dashboard_id", None),
            display_name=d.get("display_name", None),
            etag=d.get("etag", None),
            lifecycle_state=_enum(d, "lifecycle_state", LifecycleState),
            parent_path=d.get("parent_path", None),
            path=d.get("path", None),
            serialized_dashboard=d.get("serialized_dashboard", None),
            update_time=d.get("update_time", None),
            warehouse_id=d.get("warehouse_id", None),
        )


class DashboardView(Enum):

    DASHBOARD_VIEW_BASIC = "DASHBOARD_VIEW_BASIC"


@dataclass
class DeleteScheduleResponse:
    def as_dict(self) -> dict:
        """Serializes the DeleteScheduleResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteScheduleResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeleteScheduleResponse:
        """Deserializes the DeleteScheduleResponse from a dictionary."""
        return cls()


@dataclass
class DeleteSubscriptionResponse:
    def as_dict(self) -> dict:
        """Serializes the DeleteSubscriptionResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteSubscriptionResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DeleteSubscriptionResponse:
        """Deserializes the DeleteSubscriptionResponse from a dictionary."""
        return cls()


@dataclass
class Empty:
    """Represents an empty message, similar to google.protobuf.Empty, which is not available in the
    firm right now."""

    def as_dict(self) -> dict:
        """Serializes the Empty into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Empty into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Empty:
        """Deserializes the Empty from a dictionary."""
        return cls()


@dataclass
class ExecutePublishedDashboardQueryRequest:
    """Execute query request for published Dashboards. Since published dashboards have the option of
    running as the publisher, the datasets, warehouse_id are excluded from the request and instead
    read from the source (lakeview-config) via the additional parameters (dashboardName and
    dashboardRevisionId)"""

    dashboard_name: str
    """Dashboard name and revision_id is required to retrieve PublishedDatasetDataModel which contains
    the list of datasets, warehouse_id, and embedded_credentials"""

    dashboard_revision_id: str

    override_warehouse_id: Optional[str] = None
    """A dashboard schedule can override the warehouse used as compute for processing the published
    dashboard queries"""

    def as_dict(self) -> dict:
        """Serializes the ExecutePublishedDashboardQueryRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.dashboard_name is not None:
            body["dashboard_name"] = self.dashboard_name
        if self.dashboard_revision_id is not None:
            body["dashboard_revision_id"] = self.dashboard_revision_id
        if self.override_warehouse_id is not None:
            body["override_warehouse_id"] = self.override_warehouse_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExecutePublishedDashboardQueryRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.dashboard_name is not None:
            body["dashboard_name"] = self.dashboard_name
        if self.dashboard_revision_id is not None:
            body["dashboard_revision_id"] = self.dashboard_revision_id
        if self.override_warehouse_id is not None:
            body["override_warehouse_id"] = self.override_warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ExecutePublishedDashboardQueryRequest:
        """Deserializes the ExecutePublishedDashboardQueryRequest from a dictionary."""
        return cls(
            dashboard_name=d.get("dashboard_name", None),
            dashboard_revision_id=d.get("dashboard_revision_id", None),
            override_warehouse_id=d.get("override_warehouse_id", None),
        )


@dataclass
class ExecuteQueryResponse:
    def as_dict(self) -> dict:
        """Serializes the ExecuteQueryResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExecuteQueryResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ExecuteQueryResponse:
        """Deserializes the ExecuteQueryResponse from a dictionary."""
        return cls()


@dataclass
class ExternalLink:
    byte_count: Optional[int] = None
    """The number of bytes in the result chunk. This field is not available when using `INLINE`
    disposition."""

    chunk_index: Optional[int] = None
    """The position within the sequence of result set chunks."""

    expiration: Optional[str] = None
    """Indicates the date-time that the given external link will expire and becomes invalid, after
    which point a new `external_link` must be requested."""

    external_link: Optional[str] = None

    http_headers: Optional[Dict[str, str]] = None
    """HTTP headers that must be included with a GET request to the `external_link`. Each header is
    provided as a key-value pair. Headers are typically used to pass a decryption key to the
    external service. The values of these headers should be considered sensitive and the client
    should not expose these values in a log."""

    next_chunk_index: Optional[int] = None
    """When fetching, provides the `chunk_index` for the _next_ chunk. If absent, indicates there are
    no more chunks. The next chunk can be fetched with a
    :method:statementexecution/getStatementResultChunkN request."""

    next_chunk_internal_link: Optional[str] = None
    """When fetching, provides a link to fetch the _next_ chunk. If absent, indicates there are no more
    chunks. This link is an absolute `path` to be joined with your `$DATABRICKS_HOST`, and should be
    treated as an opaque link. This is an alternative to using `next_chunk_index`."""

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
            byte_count=d.get("byte_count", None),
            chunk_index=d.get("chunk_index", None),
            expiration=d.get("expiration", None),
            external_link=d.get("external_link", None),
            http_headers=d.get("http_headers", None),
            next_chunk_index=d.get("next_chunk_index", None),
            next_chunk_internal_link=d.get("next_chunk_internal_link", None),
            row_count=d.get("row_count", None),
            row_offset=d.get("row_offset", None),
        )


class Format(Enum):

    ARROW_STREAM = "ARROW_STREAM"
    CSV = "CSV"
    JSON_ARRAY = "JSON_ARRAY"


@dataclass
class GenieAttachment:
    """Genie AI Response"""

    attachment_id: Optional[str] = None
    """Attachment ID"""

    query: Optional[GenieQueryAttachment] = None
    """Query Attachment if Genie responds with a SQL query"""

    text: Optional[TextAttachment] = None
    """Text Attachment if Genie responds with text"""

    def as_dict(self) -> dict:
        """Serializes the GenieAttachment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.attachment_id is not None:
            body["attachment_id"] = self.attachment_id
        if self.query:
            body["query"] = self.query.as_dict()
        if self.text:
            body["text"] = self.text.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAttachment into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.attachment_id is not None:
            body["attachment_id"] = self.attachment_id
        if self.query:
            body["query"] = self.query
        if self.text:
            body["text"] = self.text
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAttachment:
        """Deserializes the GenieAttachment from a dictionary."""
        return cls(
            attachment_id=d.get("attachment_id", None),
            query=_from_dict(d, "query", GenieQueryAttachment),
            text=_from_dict(d, "text", TextAttachment),
        )


@dataclass
class GenieConversation:
    id: str
    """Conversation ID. Legacy identifier, use conversation_id instead"""

    space_id: str
    """Genie space ID"""

    user_id: int
    """ID of the user who created the conversation"""

    title: str
    """Conversation title"""

    conversation_id: str
    """Conversation ID"""

    created_timestamp: Optional[int] = None
    """Timestamp when the message was created"""

    last_updated_timestamp: Optional[int] = None
    """Timestamp when the message was last updated"""

    def as_dict(self) -> dict:
        """Serializes the GenieConversation into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.conversation_id is not None:
            body["conversation_id"] = self.conversation_id
        if self.created_timestamp is not None:
            body["created_timestamp"] = self.created_timestamp
        if self.id is not None:
            body["id"] = self.id
        if self.last_updated_timestamp is not None:
            body["last_updated_timestamp"] = self.last_updated_timestamp
        if self.space_id is not None:
            body["space_id"] = self.space_id
        if self.title is not None:
            body["title"] = self.title
        if self.user_id is not None:
            body["user_id"] = self.user_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieConversation into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.conversation_id is not None:
            body["conversation_id"] = self.conversation_id
        if self.created_timestamp is not None:
            body["created_timestamp"] = self.created_timestamp
        if self.id is not None:
            body["id"] = self.id
        if self.last_updated_timestamp is not None:
            body["last_updated_timestamp"] = self.last_updated_timestamp
        if self.space_id is not None:
            body["space_id"] = self.space_id
        if self.title is not None:
            body["title"] = self.title
        if self.user_id is not None:
            body["user_id"] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieConversation:
        """Deserializes the GenieConversation from a dictionary."""
        return cls(
            conversation_id=d.get("conversation_id", None),
            created_timestamp=d.get("created_timestamp", None),
            id=d.get("id", None),
            last_updated_timestamp=d.get("last_updated_timestamp", None),
            space_id=d.get("space_id", None),
            title=d.get("title", None),
            user_id=d.get("user_id", None),
        )


@dataclass
class GenieCreateConversationMessageRequest:
    content: str
    """User message content."""

    conversation_id: Optional[str] = None
    """The ID associated with the conversation."""

    space_id: Optional[str] = None
    """The ID associated with the Genie space where the conversation is started."""

    def as_dict(self) -> dict:
        """Serializes the GenieCreateConversationMessageRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.content is not None:
            body["content"] = self.content
        if self.conversation_id is not None:
            body["conversation_id"] = self.conversation_id
        if self.space_id is not None:
            body["space_id"] = self.space_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieCreateConversationMessageRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.content is not None:
            body["content"] = self.content
        if self.conversation_id is not None:
            body["conversation_id"] = self.conversation_id
        if self.space_id is not None:
            body["space_id"] = self.space_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieCreateConversationMessageRequest:
        """Deserializes the GenieCreateConversationMessageRequest from a dictionary."""
        return cls(
            content=d.get("content", None),
            conversation_id=d.get("conversation_id", None),
            space_id=d.get("space_id", None),
        )


@dataclass
class GenieGenerateDownloadFullQueryResultResponse:
    error: Optional[str] = None
    """Error message if Genie failed to download the result"""

    status: Optional[MessageStatus] = None
    """Download result status"""

    transient_statement_id: Optional[str] = None
    """Transient Statement ID. Use this ID to track the download request in subsequent polling calls"""

    def as_dict(self) -> dict:
        """Serializes the GenieGenerateDownloadFullQueryResultResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.error is not None:
            body["error"] = self.error
        if self.status is not None:
            body["status"] = self.status.value
        if self.transient_statement_id is not None:
            body["transient_statement_id"] = self.transient_statement_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieGenerateDownloadFullQueryResultResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.error is not None:
            body["error"] = self.error
        if self.status is not None:
            body["status"] = self.status
        if self.transient_statement_id is not None:
            body["transient_statement_id"] = self.transient_statement_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieGenerateDownloadFullQueryResultResponse:
        """Deserializes the GenieGenerateDownloadFullQueryResultResponse from a dictionary."""
        return cls(
            error=d.get("error", None),
            status=_enum(d, "status", MessageStatus),
            transient_statement_id=d.get("transient_statement_id", None),
        )


@dataclass
class GenieGetDownloadFullQueryResultResponse:
    statement_response: Optional[StatementResponse] = None
    """SQL Statement Execution response. See [Get status, manifest, and result first
    chunk](:method:statementexecution/getstatement) for more details."""

    transient_statement_id: Optional[str] = None
    """Transient Statement ID"""

    def as_dict(self) -> dict:
        """Serializes the GenieGetDownloadFullQueryResultResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.statement_response:
            body["statement_response"] = self.statement_response.as_dict()
        if self.transient_statement_id is not None:
            body["transient_statement_id"] = self.transient_statement_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieGetDownloadFullQueryResultResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.statement_response:
            body["statement_response"] = self.statement_response
        if self.transient_statement_id is not None:
            body["transient_statement_id"] = self.transient_statement_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieGetDownloadFullQueryResultResponse:
        """Deserializes the GenieGetDownloadFullQueryResultResponse from a dictionary."""
        return cls(
            statement_response=_from_dict(d, "statement_response", StatementResponse),
            transient_statement_id=d.get("transient_statement_id", None),
        )


@dataclass
class GenieGetMessageQueryResultResponse:
    statement_response: Optional[StatementResponse] = None
    """SQL Statement Execution response. See [Get status, manifest, and result first
    chunk](:method:statementexecution/getstatement) for more details."""

    def as_dict(self) -> dict:
        """Serializes the GenieGetMessageQueryResultResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.statement_response:
            body["statement_response"] = self.statement_response.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieGetMessageQueryResultResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.statement_response:
            body["statement_response"] = self.statement_response
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieGetMessageQueryResultResponse:
        """Deserializes the GenieGetMessageQueryResultResponse from a dictionary."""
        return cls(statement_response=_from_dict(d, "statement_response", StatementResponse))


@dataclass
class GenieMessage:
    id: str
    """Message ID. Legacy identifier, use message_id instead"""

    space_id: str
    """Genie space ID"""

    conversation_id: str
    """Conversation ID"""

    content: str
    """User message content"""

    message_id: str
    """Message ID"""

    attachments: Optional[List[GenieAttachment]] = None
    """AI-generated response to the message"""

    created_timestamp: Optional[int] = None
    """Timestamp when the message was created"""

    error: Optional[MessageError] = None
    """Error message if Genie failed to respond to the message"""

    last_updated_timestamp: Optional[int] = None
    """Timestamp when the message was last updated"""

    query_result: Optional[Result] = None
    """The result of SQL query if the message includes a query attachment. Deprecated. Use
    `query_result_metadata` in `GenieQueryAttachment` instead."""

    status: Optional[MessageStatus] = None
    """MessageStatus. The possible values are: * `FETCHING_METADATA`: Fetching metadata from the data
    sources. * `FILTERING_CONTEXT`: Running smart context step to determine relevant context. *
    `ASKING_AI`: Waiting for the LLM to respond to the user's question. * `PENDING_WAREHOUSE`:
    Waiting for warehouse before the SQL query can start executing. * `EXECUTING_QUERY`: Executing a
    generated SQL query. Get the SQL query result by calling
    [getMessageAttachmentQueryResult](:method:genie/getMessageAttachmentQueryResult) API. *
    `FAILED`: The response generation or query execution failed. See `error` field. * `COMPLETED`:
    Message processing is completed. Results are in the `attachments` field. Get the SQL query
    result by calling
    [getMessageAttachmentQueryResult](:method:genie/getMessageAttachmentQueryResult) API. *
    `SUBMITTED`: Message has been submitted. * `QUERY_RESULT_EXPIRED`: SQL result is not available
    anymore. The user needs to rerun the query. Rerun the SQL query result by calling
    [executeMessageAttachmentQuery](:method:genie/executeMessageAttachmentQuery) API. * `CANCELLED`:
    Message has been cancelled."""

    user_id: Optional[int] = None
    """ID of the user who created the message"""

    def as_dict(self) -> dict:
        """Serializes the GenieMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.attachments:
            body["attachments"] = [v.as_dict() for v in self.attachments]
        if self.content is not None:
            body["content"] = self.content
        if self.conversation_id is not None:
            body["conversation_id"] = self.conversation_id
        if self.created_timestamp is not None:
            body["created_timestamp"] = self.created_timestamp
        if self.error:
            body["error"] = self.error.as_dict()
        if self.id is not None:
            body["id"] = self.id
        if self.last_updated_timestamp is not None:
            body["last_updated_timestamp"] = self.last_updated_timestamp
        if self.message_id is not None:
            body["message_id"] = self.message_id
        if self.query_result:
            body["query_result"] = self.query_result.as_dict()
        if self.space_id is not None:
            body["space_id"] = self.space_id
        if self.status is not None:
            body["status"] = self.status.value
        if self.user_id is not None:
            body["user_id"] = self.user_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.attachments:
            body["attachments"] = self.attachments
        if self.content is not None:
            body["content"] = self.content
        if self.conversation_id is not None:
            body["conversation_id"] = self.conversation_id
        if self.created_timestamp is not None:
            body["created_timestamp"] = self.created_timestamp
        if self.error:
            body["error"] = self.error
        if self.id is not None:
            body["id"] = self.id
        if self.last_updated_timestamp is not None:
            body["last_updated_timestamp"] = self.last_updated_timestamp
        if self.message_id is not None:
            body["message_id"] = self.message_id
        if self.query_result:
            body["query_result"] = self.query_result
        if self.space_id is not None:
            body["space_id"] = self.space_id
        if self.status is not None:
            body["status"] = self.status
        if self.user_id is not None:
            body["user_id"] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieMessage:
        """Deserializes the GenieMessage from a dictionary."""
        return cls(
            attachments=_repeated_dict(d, "attachments", GenieAttachment),
            content=d.get("content", None),
            conversation_id=d.get("conversation_id", None),
            created_timestamp=d.get("created_timestamp", None),
            error=_from_dict(d, "error", MessageError),
            id=d.get("id", None),
            last_updated_timestamp=d.get("last_updated_timestamp", None),
            message_id=d.get("message_id", None),
            query_result=_from_dict(d, "query_result", Result),
            space_id=d.get("space_id", None),
            status=_enum(d, "status", MessageStatus),
            user_id=d.get("user_id", None),
        )


@dataclass
class GenieQueryAttachment:
    description: Optional[str] = None
    """Description of the query"""

    id: Optional[str] = None

    last_updated_timestamp: Optional[int] = None
    """Time when the user updated the query last"""

    query: Optional[str] = None
    """AI generated SQL query"""

    query_result_metadata: Optional[GenieResultMetadata] = None
    """Metadata associated with the query result."""

    statement_id: Optional[str] = None
    """Statement Execution API statement id. Use [Get status, manifest, and result first
    chunk](:method:statementexecution/getstatement) to get the full result data."""

    title: Optional[str] = None
    """Name of the query"""

    def as_dict(self) -> dict:
        """Serializes the GenieQueryAttachment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.id is not None:
            body["id"] = self.id
        if self.last_updated_timestamp is not None:
            body["last_updated_timestamp"] = self.last_updated_timestamp
        if self.query is not None:
            body["query"] = self.query
        if self.query_result_metadata:
            body["query_result_metadata"] = self.query_result_metadata.as_dict()
        if self.statement_id is not None:
            body["statement_id"] = self.statement_id
        if self.title is not None:
            body["title"] = self.title
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieQueryAttachment into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.id is not None:
            body["id"] = self.id
        if self.last_updated_timestamp is not None:
            body["last_updated_timestamp"] = self.last_updated_timestamp
        if self.query is not None:
            body["query"] = self.query
        if self.query_result_metadata:
            body["query_result_metadata"] = self.query_result_metadata
        if self.statement_id is not None:
            body["statement_id"] = self.statement_id
        if self.title is not None:
            body["title"] = self.title
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieQueryAttachment:
        """Deserializes the GenieQueryAttachment from a dictionary."""
        return cls(
            description=d.get("description", None),
            id=d.get("id", None),
            last_updated_timestamp=d.get("last_updated_timestamp", None),
            query=d.get("query", None),
            query_result_metadata=_from_dict(d, "query_result_metadata", GenieResultMetadata),
            statement_id=d.get("statement_id", None),
            title=d.get("title", None),
        )


@dataclass
class GenieResultMetadata:
    is_truncated: Optional[bool] = None
    """Indicates whether the result set is truncated."""

    row_count: Optional[int] = None
    """The number of rows in the result set."""

    def as_dict(self) -> dict:
        """Serializes the GenieResultMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.is_truncated is not None:
            body["is_truncated"] = self.is_truncated
        if self.row_count is not None:
            body["row_count"] = self.row_count
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieResultMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.is_truncated is not None:
            body["is_truncated"] = self.is_truncated
        if self.row_count is not None:
            body["row_count"] = self.row_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieResultMetadata:
        """Deserializes the GenieResultMetadata from a dictionary."""
        return cls(is_truncated=d.get("is_truncated", None), row_count=d.get("row_count", None))


@dataclass
class GenieSpace:
    space_id: str
    """Space ID"""

    title: str
    """Title of the Genie Space"""

    description: Optional[str] = None
    """Description of the Genie Space"""

    def as_dict(self) -> dict:
        """Serializes the GenieSpace into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.space_id is not None:
            body["space_id"] = self.space_id
        if self.title is not None:
            body["title"] = self.title
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieSpace into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.space_id is not None:
            body["space_id"] = self.space_id
        if self.title is not None:
            body["title"] = self.title
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieSpace:
        """Deserializes the GenieSpace from a dictionary."""
        return cls(description=d.get("description", None), space_id=d.get("space_id", None), title=d.get("title", None))


@dataclass
class GenieStartConversationMessageRequest:
    content: str
    """The text of the message that starts the conversation."""

    space_id: Optional[str] = None
    """The ID associated with the Genie space where you want to start a conversation."""

    def as_dict(self) -> dict:
        """Serializes the GenieStartConversationMessageRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.content is not None:
            body["content"] = self.content
        if self.space_id is not None:
            body["space_id"] = self.space_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieStartConversationMessageRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.content is not None:
            body["content"] = self.content
        if self.space_id is not None:
            body["space_id"] = self.space_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieStartConversationMessageRequest:
        """Deserializes the GenieStartConversationMessageRequest from a dictionary."""
        return cls(content=d.get("content", None), space_id=d.get("space_id", None))


@dataclass
class GenieStartConversationResponse:
    message_id: str
    """Message ID"""

    conversation_id: str
    """Conversation ID"""

    conversation: Optional[GenieConversation] = None

    message: Optional[GenieMessage] = None

    def as_dict(self) -> dict:
        """Serializes the GenieStartConversationResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.conversation:
            body["conversation"] = self.conversation.as_dict()
        if self.conversation_id is not None:
            body["conversation_id"] = self.conversation_id
        if self.message:
            body["message"] = self.message.as_dict()
        if self.message_id is not None:
            body["message_id"] = self.message_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieStartConversationResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.conversation:
            body["conversation"] = self.conversation
        if self.conversation_id is not None:
            body["conversation_id"] = self.conversation_id
        if self.message:
            body["message"] = self.message
        if self.message_id is not None:
            body["message_id"] = self.message_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieStartConversationResponse:
        """Deserializes the GenieStartConversationResponse from a dictionary."""
        return cls(
            conversation=_from_dict(d, "conversation", GenieConversation),
            conversation_id=d.get("conversation_id", None),
            message=_from_dict(d, "message", GenieMessage),
            message_id=d.get("message_id", None),
        )


@dataclass
class GetPublishedDashboardEmbeddedResponse:
    def as_dict(self) -> dict:
        """Serializes the GetPublishedDashboardEmbeddedResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GetPublishedDashboardEmbeddedResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GetPublishedDashboardEmbeddedResponse:
        """Deserializes the GetPublishedDashboardEmbeddedResponse from a dictionary."""
        return cls()


class LifecycleState(Enum):

    ACTIVE = "ACTIVE"
    TRASHED = "TRASHED"


@dataclass
class ListDashboardsResponse:
    dashboards: Optional[List[Dashboard]] = None

    next_page_token: Optional[str] = None
    """A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent dashboards."""

    def as_dict(self) -> dict:
        """Serializes the ListDashboardsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.dashboards:
            body["dashboards"] = [v.as_dict() for v in self.dashboards]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListDashboardsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.dashboards:
            body["dashboards"] = self.dashboards
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListDashboardsResponse:
        """Deserializes the ListDashboardsResponse from a dictionary."""
        return cls(
            dashboards=_repeated_dict(d, "dashboards", Dashboard), next_page_token=d.get("next_page_token", None)
        )


@dataclass
class ListSchedulesResponse:
    next_page_token: Optional[str] = None
    """A token that can be used as a `page_token` in subsequent requests to retrieve the next page of
    results. If this field is omitted, there are no subsequent schedules."""

    schedules: Optional[List[Schedule]] = None

    def as_dict(self) -> dict:
        """Serializes the ListSchedulesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.schedules:
            body["schedules"] = [v.as_dict() for v in self.schedules]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListSchedulesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.schedules:
            body["schedules"] = self.schedules
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListSchedulesResponse:
        """Deserializes the ListSchedulesResponse from a dictionary."""
        return cls(next_page_token=d.get("next_page_token", None), schedules=_repeated_dict(d, "schedules", Schedule))


@dataclass
class ListSubscriptionsResponse:
    next_page_token: Optional[str] = None
    """A token that can be used as a `page_token` in subsequent requests to retrieve the next page of
    results. If this field is omitted, there are no subsequent subscriptions."""

    subscriptions: Optional[List[Subscription]] = None

    def as_dict(self) -> dict:
        """Serializes the ListSubscriptionsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.subscriptions:
            body["subscriptions"] = [v.as_dict() for v in self.subscriptions]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListSubscriptionsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.subscriptions:
            body["subscriptions"] = self.subscriptions
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListSubscriptionsResponse:
        """Deserializes the ListSubscriptionsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            subscriptions=_repeated_dict(d, "subscriptions", Subscription),
        )


@dataclass
class MessageError:
    error: Optional[str] = None

    type: Optional[MessageErrorType] = None

    def as_dict(self) -> dict:
        """Serializes the MessageError into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.error is not None:
            body["error"] = self.error
        if self.type is not None:
            body["type"] = self.type.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MessageError into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.error is not None:
            body["error"] = self.error
        if self.type is not None:
            body["type"] = self.type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> MessageError:
        """Deserializes the MessageError from a dictionary."""
        return cls(error=d.get("error", None), type=_enum(d, "type", MessageErrorType))


class MessageErrorType(Enum):

    BLOCK_MULTIPLE_EXECUTIONS_EXCEPTION = "BLOCK_MULTIPLE_EXECUTIONS_EXCEPTION"
    CHAT_COMPLETION_CLIENT_EXCEPTION = "CHAT_COMPLETION_CLIENT_EXCEPTION"
    CHAT_COMPLETION_CLIENT_TIMEOUT_EXCEPTION = "CHAT_COMPLETION_CLIENT_TIMEOUT_EXCEPTION"
    CHAT_COMPLETION_NETWORK_EXCEPTION = "CHAT_COMPLETION_NETWORK_EXCEPTION"
    CONTENT_FILTER_EXCEPTION = "CONTENT_FILTER_EXCEPTION"
    CONTEXT_EXCEEDED_EXCEPTION = "CONTEXT_EXCEEDED_EXCEPTION"
    COULD_NOT_GET_MODEL_DEPLOYMENTS_EXCEPTION = "COULD_NOT_GET_MODEL_DEPLOYMENTS_EXCEPTION"
    COULD_NOT_GET_UC_SCHEMA_EXCEPTION = "COULD_NOT_GET_UC_SCHEMA_EXCEPTION"
    DEPLOYMENT_NOT_FOUND_EXCEPTION = "DEPLOYMENT_NOT_FOUND_EXCEPTION"
    FUNCTIONS_NOT_AVAILABLE_EXCEPTION = "FUNCTIONS_NOT_AVAILABLE_EXCEPTION"
    FUNCTION_ARGUMENTS_INVALID_EXCEPTION = "FUNCTION_ARGUMENTS_INVALID_EXCEPTION"
    FUNCTION_ARGUMENTS_INVALID_JSON_EXCEPTION = "FUNCTION_ARGUMENTS_INVALID_JSON_EXCEPTION"
    FUNCTION_ARGUMENTS_INVALID_TYPE_EXCEPTION = "FUNCTION_ARGUMENTS_INVALID_TYPE_EXCEPTION"
    FUNCTION_CALL_MISSING_PARAMETER_EXCEPTION = "FUNCTION_CALL_MISSING_PARAMETER_EXCEPTION"
    GENERATED_SQL_QUERY_TOO_LONG_EXCEPTION = "GENERATED_SQL_QUERY_TOO_LONG_EXCEPTION"
    GENERIC_CHAT_COMPLETION_EXCEPTION = "GENERIC_CHAT_COMPLETION_EXCEPTION"
    GENERIC_CHAT_COMPLETION_SERVICE_EXCEPTION = "GENERIC_CHAT_COMPLETION_SERVICE_EXCEPTION"
    GENERIC_SQL_EXEC_API_CALL_EXCEPTION = "GENERIC_SQL_EXEC_API_CALL_EXCEPTION"
    ILLEGAL_PARAMETER_DEFINITION_EXCEPTION = "ILLEGAL_PARAMETER_DEFINITION_EXCEPTION"
    INVALID_CERTIFIED_ANSWER_FUNCTION_EXCEPTION = "INVALID_CERTIFIED_ANSWER_FUNCTION_EXCEPTION"
    INVALID_CERTIFIED_ANSWER_IDENTIFIER_EXCEPTION = "INVALID_CERTIFIED_ANSWER_IDENTIFIER_EXCEPTION"
    INVALID_CHAT_COMPLETION_JSON_EXCEPTION = "INVALID_CHAT_COMPLETION_JSON_EXCEPTION"
    INVALID_COMPLETION_REQUEST_EXCEPTION = "INVALID_COMPLETION_REQUEST_EXCEPTION"
    INVALID_FUNCTION_CALL_EXCEPTION = "INVALID_FUNCTION_CALL_EXCEPTION"
    INVALID_TABLE_IDENTIFIER_EXCEPTION = "INVALID_TABLE_IDENTIFIER_EXCEPTION"
    LOCAL_CONTEXT_EXCEEDED_EXCEPTION = "LOCAL_CONTEXT_EXCEEDED_EXCEPTION"
    MESSAGE_CANCELLED_WHILE_EXECUTING_EXCEPTION = "MESSAGE_CANCELLED_WHILE_EXECUTING_EXCEPTION"
    MESSAGE_DELETED_WHILE_EXECUTING_EXCEPTION = "MESSAGE_DELETED_WHILE_EXECUTING_EXCEPTION"
    MESSAGE_UPDATED_WHILE_EXECUTING_EXCEPTION = "MESSAGE_UPDATED_WHILE_EXECUTING_EXCEPTION"
    MISSING_SQL_QUERY_EXCEPTION = "MISSING_SQL_QUERY_EXCEPTION"
    NO_DEPLOYMENTS_AVAILABLE_TO_WORKSPACE = "NO_DEPLOYMENTS_AVAILABLE_TO_WORKSPACE"
    NO_QUERY_TO_VISUALIZE_EXCEPTION = "NO_QUERY_TO_VISUALIZE_EXCEPTION"
    NO_TABLES_TO_QUERY_EXCEPTION = "NO_TABLES_TO_QUERY_EXCEPTION"
    RATE_LIMIT_EXCEEDED_GENERIC_EXCEPTION = "RATE_LIMIT_EXCEEDED_GENERIC_EXCEPTION"
    RATE_LIMIT_EXCEEDED_SPECIFIED_WAIT_EXCEPTION = "RATE_LIMIT_EXCEEDED_SPECIFIED_WAIT_EXCEPTION"
    REPLY_PROCESS_TIMEOUT_EXCEPTION = "REPLY_PROCESS_TIMEOUT_EXCEPTION"
    RETRYABLE_PROCESSING_EXCEPTION = "RETRYABLE_PROCESSING_EXCEPTION"
    SQL_EXECUTION_EXCEPTION = "SQL_EXECUTION_EXCEPTION"
    STOP_PROCESS_DUE_TO_AUTO_REGENERATE = "STOP_PROCESS_DUE_TO_AUTO_REGENERATE"
    TABLES_MISSING_EXCEPTION = "TABLES_MISSING_EXCEPTION"
    TOO_MANY_CERTIFIED_ANSWERS_EXCEPTION = "TOO_MANY_CERTIFIED_ANSWERS_EXCEPTION"
    TOO_MANY_TABLES_EXCEPTION = "TOO_MANY_TABLES_EXCEPTION"
    UNEXPECTED_REPLY_PROCESS_EXCEPTION = "UNEXPECTED_REPLY_PROCESS_EXCEPTION"
    UNKNOWN_AI_MODEL = "UNKNOWN_AI_MODEL"
    WAREHOUSE_ACCESS_MISSING_EXCEPTION = "WAREHOUSE_ACCESS_MISSING_EXCEPTION"
    WAREHOUSE_NOT_FOUND_EXCEPTION = "WAREHOUSE_NOT_FOUND_EXCEPTION"


class MessageStatus(Enum):
    """MessageStatus. The possible values are: * `FETCHING_METADATA`: Fetching metadata from the data
    sources. * `FILTERING_CONTEXT`: Running smart context step to determine relevant context. *
    `ASKING_AI`: Waiting for the LLM to respond to the user's question. * `PENDING_WAREHOUSE`:
    Waiting for warehouse before the SQL query can start executing. * `EXECUTING_QUERY`: Executing a
    generated SQL query. Get the SQL query result by calling
    [getMessageAttachmentQueryResult](:method:genie/getMessageAttachmentQueryResult) API. *
    `FAILED`: The response generation or query execution failed. See `error` field. * `COMPLETED`:
    Message processing is completed. Results are in the `attachments` field. Get the SQL query
    result by calling
    [getMessageAttachmentQueryResult](:method:genie/getMessageAttachmentQueryResult) API. *
    `SUBMITTED`: Message has been submitted. * `QUERY_RESULT_EXPIRED`: SQL result is not available
    anymore. The user needs to rerun the query. Rerun the SQL query result by calling
    [executeMessageAttachmentQuery](:method:genie/executeMessageAttachmentQuery) API. * `CANCELLED`:
    Message has been cancelled."""

    ASKING_AI = "ASKING_AI"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    EXECUTING_QUERY = "EXECUTING_QUERY"
    FAILED = "FAILED"
    FETCHING_METADATA = "FETCHING_METADATA"
    FILTERING_CONTEXT = "FILTERING_CONTEXT"
    PENDING_WAREHOUSE = "PENDING_WAREHOUSE"
    QUERY_RESULT_EXPIRED = "QUERY_RESULT_EXPIRED"
    SUBMITTED = "SUBMITTED"


@dataclass
class MigrateDashboardRequest:
    source_dashboard_id: str
    """UUID of the dashboard to be migrated."""

    display_name: Optional[str] = None
    """Display name for the new Lakeview dashboard."""

    parent_path: Optional[str] = None
    """The workspace path of the folder to contain the migrated Lakeview dashboard."""

    update_parameter_syntax: Optional[bool] = None
    """Flag to indicate if mustache parameter syntax ({{ param }}) should be auto-updated to named
    syntax (:param) when converting datasets in the dashboard."""

    def as_dict(self) -> dict:
        """Serializes the MigrateDashboardRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.parent_path is not None:
            body["parent_path"] = self.parent_path
        if self.source_dashboard_id is not None:
            body["source_dashboard_id"] = self.source_dashboard_id
        if self.update_parameter_syntax is not None:
            body["update_parameter_syntax"] = self.update_parameter_syntax
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MigrateDashboardRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.parent_path is not None:
            body["parent_path"] = self.parent_path
        if self.source_dashboard_id is not None:
            body["source_dashboard_id"] = self.source_dashboard_id
        if self.update_parameter_syntax is not None:
            body["update_parameter_syntax"] = self.update_parameter_syntax
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> MigrateDashboardRequest:
        """Deserializes the MigrateDashboardRequest from a dictionary."""
        return cls(
            display_name=d.get("display_name", None),
            parent_path=d.get("parent_path", None),
            source_dashboard_id=d.get("source_dashboard_id", None),
            update_parameter_syntax=d.get("update_parameter_syntax", None),
        )


@dataclass
class PendingStatus:
    data_token: str
    """The token to poll for result asynchronously Example:
    EC0A..ChAB7WCEn_4Qo4vkLqEbXsxxEgh3Y2pbWw45WhoQXgZSQo9aS5q2ZvFcbvbx9CgA-PAEAQ"""

    def as_dict(self) -> dict:
        """Serializes the PendingStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.data_token is not None:
            body["data_token"] = self.data_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PendingStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.data_token is not None:
            body["data_token"] = self.data_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PendingStatus:
        """Deserializes the PendingStatus from a dictionary."""
        return cls(data_token=d.get("data_token", None))


@dataclass
class PollQueryStatusResponse:
    data: Optional[List[PollQueryStatusResponseData]] = None

    def as_dict(self) -> dict:
        """Serializes the PollQueryStatusResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.data:
            body["data"] = [v.as_dict() for v in self.data]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PollQueryStatusResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.data:
            body["data"] = self.data
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PollQueryStatusResponse:
        """Deserializes the PollQueryStatusResponse from a dictionary."""
        return cls(data=_repeated_dict(d, "data", PollQueryStatusResponseData))


@dataclass
class PollQueryStatusResponseData:
    status: QueryResponseStatus

    def as_dict(self) -> dict:
        """Serializes the PollQueryStatusResponseData into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.status:
            body["status"] = self.status.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PollQueryStatusResponseData into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.status:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PollQueryStatusResponseData:
        """Deserializes the PollQueryStatusResponseData from a dictionary."""
        return cls(status=_from_dict(d, "status", QueryResponseStatus))


@dataclass
class PublishRequest:
    dashboard_id: Optional[str] = None
    """UUID identifying the dashboard to be published."""

    embed_credentials: Optional[bool] = None
    """Flag to indicate if the publisher's credentials should be embedded in the published dashboard.
    These embedded credentials will be used to execute the published dashboard's queries."""

    warehouse_id: Optional[str] = None
    """The ID of the warehouse that can be used to override the warehouse which was set in the draft."""

    def as_dict(self) -> dict:
        """Serializes the PublishRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.dashboard_id is not None:
            body["dashboard_id"] = self.dashboard_id
        if self.embed_credentials is not None:
            body["embed_credentials"] = self.embed_credentials
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PublishRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.dashboard_id is not None:
            body["dashboard_id"] = self.dashboard_id
        if self.embed_credentials is not None:
            body["embed_credentials"] = self.embed_credentials
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PublishRequest:
        """Deserializes the PublishRequest from a dictionary."""
        return cls(
            dashboard_id=d.get("dashboard_id", None),
            embed_credentials=d.get("embed_credentials", None),
            warehouse_id=d.get("warehouse_id", None),
        )


@dataclass
class PublishedDashboard:
    display_name: Optional[str] = None
    """The display name of the published dashboard."""

    embed_credentials: Optional[bool] = None
    """Indicates whether credentials are embedded in the published dashboard."""

    revision_create_time: Optional[str] = None
    """The timestamp of when the published dashboard was last revised."""

    warehouse_id: Optional[str] = None
    """The warehouse ID used to run the published dashboard."""

    def as_dict(self) -> dict:
        """Serializes the PublishedDashboard into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.embed_credentials is not None:
            body["embed_credentials"] = self.embed_credentials
        if self.revision_create_time is not None:
            body["revision_create_time"] = self.revision_create_time
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PublishedDashboard into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.embed_credentials is not None:
            body["embed_credentials"] = self.embed_credentials
        if self.revision_create_time is not None:
            body["revision_create_time"] = self.revision_create_time
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PublishedDashboard:
        """Deserializes the PublishedDashboard from a dictionary."""
        return cls(
            display_name=d.get("display_name", None),
            embed_credentials=d.get("embed_credentials", None),
            revision_create_time=d.get("revision_create_time", None),
            warehouse_id=d.get("warehouse_id", None),
        )


@dataclass
class QueryResponseStatus:
    canceled: Optional[Empty] = None
    """Represents an empty message, similar to google.protobuf.Empty, which is not available in the
    firm right now."""

    closed: Optional[Empty] = None
    """Represents an empty message, similar to google.protobuf.Empty, which is not available in the
    firm right now."""

    pending: Optional[PendingStatus] = None

    statement_id: Optional[str] = None
    """The statement id in format(01eef5da-c56e-1f36-bafa-21906587d6ba) The statement_id should be
    identical to data_token in SuccessStatus and PendingStatus. This field is created for audit
    logging purpose to record the statement_id of all QueryResponseStatus."""

    success: Optional[SuccessStatus] = None

    def as_dict(self) -> dict:
        """Serializes the QueryResponseStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.canceled:
            body["canceled"] = self.canceled.as_dict()
        if self.closed:
            body["closed"] = self.closed.as_dict()
        if self.pending:
            body["pending"] = self.pending.as_dict()
        if self.statement_id is not None:
            body["statement_id"] = self.statement_id
        if self.success:
            body["success"] = self.success.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the QueryResponseStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.canceled:
            body["canceled"] = self.canceled
        if self.closed:
            body["closed"] = self.closed
        if self.pending:
            body["pending"] = self.pending
        if self.statement_id is not None:
            body["statement_id"] = self.statement_id
        if self.success:
            body["success"] = self.success
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> QueryResponseStatus:
        """Deserializes the QueryResponseStatus from a dictionary."""
        return cls(
            canceled=_from_dict(d, "canceled", Empty),
            closed=_from_dict(d, "closed", Empty),
            pending=_from_dict(d, "pending", PendingStatus),
            statement_id=d.get("statement_id", None),
            success=_from_dict(d, "success", SuccessStatus),
        )


@dataclass
class Result:
    is_truncated: Optional[bool] = None
    """If result is truncated"""

    row_count: Optional[int] = None
    """Row count of the result"""

    statement_id: Optional[str] = None
    """Statement Execution API statement id. Use [Get status, manifest, and result first
    chunk](:method:statementexecution/getstatement) to get the full result data."""

    def as_dict(self) -> dict:
        """Serializes the Result into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.is_truncated is not None:
            body["is_truncated"] = self.is_truncated
        if self.row_count is not None:
            body["row_count"] = self.row_count
        if self.statement_id is not None:
            body["statement_id"] = self.statement_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Result into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.is_truncated is not None:
            body["is_truncated"] = self.is_truncated
        if self.row_count is not None:
            body["row_count"] = self.row_count
        if self.statement_id is not None:
            body["statement_id"] = self.statement_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Result:
        """Deserializes the Result from a dictionary."""
        return cls(
            is_truncated=d.get("is_truncated", None),
            row_count=d.get("row_count", None),
            statement_id=d.get("statement_id", None),
        )


@dataclass
class ResultData:
    byte_count: Optional[int] = None
    """The number of bytes in the result chunk. This field is not available when using `INLINE`
    disposition."""

    chunk_index: Optional[int] = None
    """The position within the sequence of result set chunks."""

    data_array: Optional[List[List[str]]] = None
    """The `JSON_ARRAY` format is an array of arrays of values, where each non-null value is formatted
    as a string. Null values are encoded as JSON `null`."""

    external_links: Optional[List[ExternalLink]] = None

    next_chunk_index: Optional[int] = None
    """When fetching, provides the `chunk_index` for the _next_ chunk. If absent, indicates there are
    no more chunks. The next chunk can be fetched with a
    :method:statementexecution/getStatementResultChunkN request."""

    next_chunk_internal_link: Optional[str] = None
    """When fetching, provides a link to fetch the _next_ chunk. If absent, indicates there are no more
    chunks. This link is an absolute `path` to be joined with your `$DATABRICKS_HOST`, and should be
    treated as an opaque link. This is an alternative to using `next_chunk_index`."""

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
            byte_count=d.get("byte_count", None),
            chunk_index=d.get("chunk_index", None),
            data_array=d.get("data_array", None),
            external_links=_repeated_dict(d, "external_links", ExternalLink),
            next_chunk_index=d.get("next_chunk_index", None),
            next_chunk_internal_link=d.get("next_chunk_internal_link", None),
            row_count=d.get("row_count", None),
            row_offset=d.get("row_offset", None),
        )


@dataclass
class ResultManifest:
    """The result manifest provides schema and metadata for the result set."""

    chunks: Optional[List[BaseChunkInfo]] = None
    """Array of result set chunk metadata."""

    format: Optional[Format] = None

    schema: Optional[ResultSchema] = None
    """The schema is an ordered list of column descriptions."""

    total_byte_count: Optional[int] = None
    """The total number of bytes in the result set. This field is not available when using `INLINE`
    disposition."""

    total_chunk_count: Optional[int] = None
    """The total number of chunks that the result set has been divided into."""

    total_row_count: Optional[int] = None
    """The total number of rows in the result set."""

    truncated: Optional[bool] = None
    """Indicates whether the result is truncated due to `row_limit` or `byte_limit`."""

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
            schema=_from_dict(d, "schema", ResultSchema),
            total_byte_count=d.get("total_byte_count", None),
            total_chunk_count=d.get("total_chunk_count", None),
            total_row_count=d.get("total_row_count", None),
            truncated=d.get("truncated", None),
        )


@dataclass
class ResultSchema:
    """The schema is an ordered list of column descriptions."""

    column_count: Optional[int] = None

    columns: Optional[List[ColumnInfo]] = None

    def as_dict(self) -> dict:
        """Serializes the ResultSchema into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.column_count is not None:
            body["column_count"] = self.column_count
        if self.columns:
            body["columns"] = [v.as_dict() for v in self.columns]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ResultSchema into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.column_count is not None:
            body["column_count"] = self.column_count
        if self.columns:
            body["columns"] = self.columns
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResultSchema:
        """Deserializes the ResultSchema from a dictionary."""
        return cls(column_count=d.get("column_count", None), columns=_repeated_dict(d, "columns", ColumnInfo))


@dataclass
class Schedule:
    cron_schedule: CronSchedule
    """The cron expression describing the frequency of the periodic refresh for this schedule."""

    create_time: Optional[str] = None
    """A timestamp indicating when the schedule was created."""

    dashboard_id: Optional[str] = None
    """UUID identifying the dashboard to which the schedule belongs."""

    display_name: Optional[str] = None
    """The display name for schedule."""

    etag: Optional[str] = None
    """The etag for the schedule. Must be left empty on create, must be provided on updates to ensure
    that the schedule has not been modified since the last read, and can be optionally provided on
    delete."""

    pause_status: Optional[SchedulePauseStatus] = None
    """The status indicates whether this schedule is paused or not."""

    schedule_id: Optional[str] = None
    """UUID identifying the schedule."""

    update_time: Optional[str] = None
    """A timestamp indicating when the schedule was last updated."""

    warehouse_id: Optional[str] = None
    """The warehouse id to run the dashboard with for the schedule."""

    def as_dict(self) -> dict:
        """Serializes the Schedule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.cron_schedule:
            body["cron_schedule"] = self.cron_schedule.as_dict()
        if self.dashboard_id is not None:
            body["dashboard_id"] = self.dashboard_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.etag is not None:
            body["etag"] = self.etag
        if self.pause_status is not None:
            body["pause_status"] = self.pause_status.value
        if self.schedule_id is not None:
            body["schedule_id"] = self.schedule_id
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Schedule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.cron_schedule:
            body["cron_schedule"] = self.cron_schedule
        if self.dashboard_id is not None:
            body["dashboard_id"] = self.dashboard_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.etag is not None:
            body["etag"] = self.etag
        if self.pause_status is not None:
            body["pause_status"] = self.pause_status
        if self.schedule_id is not None:
            body["schedule_id"] = self.schedule_id
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Schedule:
        """Deserializes the Schedule from a dictionary."""
        return cls(
            create_time=d.get("create_time", None),
            cron_schedule=_from_dict(d, "cron_schedule", CronSchedule),
            dashboard_id=d.get("dashboard_id", None),
            display_name=d.get("display_name", None),
            etag=d.get("etag", None),
            pause_status=_enum(d, "pause_status", SchedulePauseStatus),
            schedule_id=d.get("schedule_id", None),
            update_time=d.get("update_time", None),
            warehouse_id=d.get("warehouse_id", None),
        )


class SchedulePauseStatus(Enum):

    PAUSED = "PAUSED"
    UNPAUSED = "UNPAUSED"


@dataclass
class ServiceError:
    error_code: Optional[ServiceErrorCode] = None

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
class StatementResponse:
    manifest: Optional[ResultManifest] = None
    """The result manifest provides schema and metadata for the result set."""

    result: Optional[ResultData] = None

    statement_id: Optional[str] = None
    """The statement ID is returned upon successfully submitting a SQL statement, and is a required
    reference for all subsequent calls."""

    status: Optional[StatementStatus] = None
    """The status response includes execution state and if relevant, error information."""

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


class StatementState(Enum):
    """Statement execution state: - `PENDING`: waiting for warehouse - `RUNNING`: running -
    `SUCCEEDED`: execution was successful, result data available for fetch - `FAILED`: execution
    failed; reason for failure described in accomanying error message - `CANCELED`: user canceled;
    can come from explicit cancel call, or timeout with `on_wait_timeout=CANCEL` - `CLOSED`:
    execution successful, and statement closed; result no longer available for fetch"""

    CANCELED = "CANCELED"
    CLOSED = "CLOSED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"


@dataclass
class StatementStatus:
    """The status response includes execution state and if relevant, error information."""

    error: Optional[ServiceError] = None

    state: Optional[StatementState] = None
    """Statement execution state: - `PENDING`: waiting for warehouse - `RUNNING`: running -
    `SUCCEEDED`: execution was successful, result data available for fetch - `FAILED`: execution
    failed; reason for failure described in accomanying error message - `CANCELED`: user canceled;
    can come from explicit cancel call, or timeout with `on_wait_timeout=CANCEL` - `CLOSED`:
    execution successful, and statement closed; result no longer available for fetch"""

    def as_dict(self) -> dict:
        """Serializes the StatementStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.error:
            body["error"] = self.error.as_dict()
        if self.state is not None:
            body["state"] = self.state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the StatementStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.error:
            body["error"] = self.error
        if self.state is not None:
            body["state"] = self.state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> StatementStatus:
        """Deserializes the StatementStatus from a dictionary."""
        return cls(error=_from_dict(d, "error", ServiceError), state=_enum(d, "state", StatementState))


@dataclass
class Subscriber:
    destination_subscriber: Optional[SubscriptionSubscriberDestination] = None
    """The destination to receive the subscription email. This parameter is mutually exclusive with
    `user_subscriber`."""

    user_subscriber: Optional[SubscriptionSubscriberUser] = None
    """The user to receive the subscription email. This parameter is mutually exclusive with
    `destination_subscriber`."""

    def as_dict(self) -> dict:
        """Serializes the Subscriber into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.destination_subscriber:
            body["destination_subscriber"] = self.destination_subscriber.as_dict()
        if self.user_subscriber:
            body["user_subscriber"] = self.user_subscriber.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Subscriber into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.destination_subscriber:
            body["destination_subscriber"] = self.destination_subscriber
        if self.user_subscriber:
            body["user_subscriber"] = self.user_subscriber
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Subscriber:
        """Deserializes the Subscriber from a dictionary."""
        return cls(
            destination_subscriber=_from_dict(d, "destination_subscriber", SubscriptionSubscriberDestination),
            user_subscriber=_from_dict(d, "user_subscriber", SubscriptionSubscriberUser),
        )


@dataclass
class Subscription:
    subscriber: Subscriber
    """Subscriber details for users and destinations to be added as subscribers to the schedule."""

    create_time: Optional[str] = None
    """A timestamp indicating when the subscription was created."""

    created_by_user_id: Optional[int] = None
    """UserId of the user who adds subscribers (users or notification destinations) to the dashboard's
    schedule."""

    dashboard_id: Optional[str] = None
    """UUID identifying the dashboard to which the subscription belongs."""

    etag: Optional[str] = None
    """The etag for the subscription. Must be left empty on create, can be optionally provided on
    delete to ensure that the subscription has not been deleted since the last read."""

    schedule_id: Optional[str] = None
    """UUID identifying the schedule to which the subscription belongs."""

    subscription_id: Optional[str] = None
    """UUID identifying the subscription."""

    update_time: Optional[str] = None
    """A timestamp indicating when the subscription was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Subscription into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.created_by_user_id is not None:
            body["created_by_user_id"] = self.created_by_user_id
        if self.dashboard_id is not None:
            body["dashboard_id"] = self.dashboard_id
        if self.etag is not None:
            body["etag"] = self.etag
        if self.schedule_id is not None:
            body["schedule_id"] = self.schedule_id
        if self.subscriber:
            body["subscriber"] = self.subscriber.as_dict()
        if self.subscription_id is not None:
            body["subscription_id"] = self.subscription_id
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Subscription into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.created_by_user_id is not None:
            body["created_by_user_id"] = self.created_by_user_id
        if self.dashboard_id is not None:
            body["dashboard_id"] = self.dashboard_id
        if self.etag is not None:
            body["etag"] = self.etag
        if self.schedule_id is not None:
            body["schedule_id"] = self.schedule_id
        if self.subscriber:
            body["subscriber"] = self.subscriber
        if self.subscription_id is not None:
            body["subscription_id"] = self.subscription_id
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Subscription:
        """Deserializes the Subscription from a dictionary."""
        return cls(
            create_time=d.get("create_time", None),
            created_by_user_id=d.get("created_by_user_id", None),
            dashboard_id=d.get("dashboard_id", None),
            etag=d.get("etag", None),
            schedule_id=d.get("schedule_id", None),
            subscriber=_from_dict(d, "subscriber", Subscriber),
            subscription_id=d.get("subscription_id", None),
            update_time=d.get("update_time", None),
        )


@dataclass
class SubscriptionSubscriberDestination:
    destination_id: str
    """The canonical identifier of the destination to receive email notification."""

    def as_dict(self) -> dict:
        """Serializes the SubscriptionSubscriberDestination into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.destination_id is not None:
            body["destination_id"] = self.destination_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SubscriptionSubscriberDestination into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.destination_id is not None:
            body["destination_id"] = self.destination_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SubscriptionSubscriberDestination:
        """Deserializes the SubscriptionSubscriberDestination from a dictionary."""
        return cls(destination_id=d.get("destination_id", None))


@dataclass
class SubscriptionSubscriberUser:
    user_id: int
    """UserId of the subscriber."""

    def as_dict(self) -> dict:
        """Serializes the SubscriptionSubscriberUser into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.user_id is not None:
            body["user_id"] = self.user_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SubscriptionSubscriberUser into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.user_id is not None:
            body["user_id"] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SubscriptionSubscriberUser:
        """Deserializes the SubscriptionSubscriberUser from a dictionary."""
        return cls(user_id=d.get("user_id", None))


@dataclass
class SuccessStatus:
    data_token: str
    """The token to poll for result asynchronously Example:
    EC0A..ChAB7WCEn_4Qo4vkLqEbXsxxEgh3Y2pbWw45WhoQXgZSQo9aS5q2ZvFcbvbx9CgA-PAEAQ"""

    truncated: Optional[bool] = None
    """Whether the query result is truncated (either by byte limit or row limit)"""

    def as_dict(self) -> dict:
        """Serializes the SuccessStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.data_token is not None:
            body["data_token"] = self.data_token
        if self.truncated is not None:
            body["truncated"] = self.truncated
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SuccessStatus into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.data_token is not None:
            body["data_token"] = self.data_token
        if self.truncated is not None:
            body["truncated"] = self.truncated
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SuccessStatus:
        """Deserializes the SuccessStatus from a dictionary."""
        return cls(data_token=d.get("data_token", None), truncated=d.get("truncated", None))


@dataclass
class TextAttachment:
    content: Optional[str] = None
    """AI generated message"""

    id: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the TextAttachment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.content is not None:
            body["content"] = self.content
        if self.id is not None:
            body["id"] = self.id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the TextAttachment into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.content is not None:
            body["content"] = self.content
        if self.id is not None:
            body["id"] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> TextAttachment:
        """Deserializes the TextAttachment from a dictionary."""
        return cls(content=d.get("content", None), id=d.get("id", None))


@dataclass
class TrashDashboardResponse:
    def as_dict(self) -> dict:
        """Serializes the TrashDashboardResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the TrashDashboardResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> TrashDashboardResponse:
        """Deserializes the TrashDashboardResponse from a dictionary."""
        return cls()


@dataclass
class UnpublishDashboardResponse:
    def as_dict(self) -> dict:
        """Serializes the UnpublishDashboardResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UnpublishDashboardResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UnpublishDashboardResponse:
        """Deserializes the UnpublishDashboardResponse from a dictionary."""
        return cls()


class GenieAPI:
    """Genie provides a no-code experience for business users, powered by AI/BI. Analysts set up spaces that
    business users can use to ask questions using natural language. Genie uses data registered to Unity
    Catalog and requires at least CAN USE permission on a Pro or Serverless SQL warehouse. Also, Databricks
    Assistant must be enabled."""

    def __init__(self, api_client):
        self._api = api_client

    def create_message(self, space_id: str, conversation_id: str, content: str) -> GenieMessage:
        """Create conversation message.

        Create new message in a [conversation](:method:genie/startconversation). The AI response uses all
        previously created messages in the conversation to respond.

        :param space_id: str
          The ID associated with the Genie space where the conversation is started.
        :param conversation_id: str
          The ID associated with the conversation.
        :param content: str
          User message content.

        :returns:
          Long-running operation waiter for :class:`GenieMessage`.
          See :method:WaitGetMessageGenieCompleted for more details.
        """
        body = {}
        if content is not None:
            body["content"] = content
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages",
            body=body,
            headers=headers,
        )
        return GenieMessage.from_dict(res)

    def execute_message_attachment_query(
        self, space_id: str, conversation_id: str, message_id: str, attachment_id: str
    ) -> GenieGetMessageQueryResultResponse:
        """Execute message attachment SQL query.

        Execute the SQL for a message query attachment. Use this API when the query attachment has expired and
        needs to be re-executed.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        :param attachment_id: str
          Attachment ID

        :returns: :class:`GenieGetMessageQueryResultResponse`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}/attachments/{attachment_id}/execute-query",
            headers=headers,
        )
        return GenieGetMessageQueryResultResponse.from_dict(res)

    def execute_message_query(
        self, space_id: str, conversation_id: str, message_id: str
    ) -> GenieGetMessageQueryResultResponse:
        """[Deprecated] Execute SQL query in a conversation message.

        Execute the SQL query in the message.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID

        :returns: :class:`GenieGetMessageQueryResultResponse`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}/execute-query",
            headers=headers,
        )
        return GenieGetMessageQueryResultResponse.from_dict(res)

    def generate_download_full_query_result(
        self, space_id: str, conversation_id: str, message_id: str, attachment_id: str
    ) -> GenieGenerateDownloadFullQueryResultResponse:
        """Generate full query result download.

        Initiate full SQL query result download and obtain a transient ID for tracking the download progress.
        This call initiates a new SQL execution to generate the query result. The result is stored in an
        external link can be retrieved using the [Get Download Full Query
        Result](:method:genie/getdownloadfullqueryresult) API. Warning: Databricks strongly recommends that
        you protect the URLs that are returned by the `EXTERNAL_LINKS` disposition. See [Execute
        Statement](:method:statementexecution/executestatement) for more details.

        :param space_id: str
          Space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        :param attachment_id: str
          Attachment ID

        :returns: :class:`GenieGenerateDownloadFullQueryResultResponse`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}/attachments/{attachment_id}/generate-download",
            headers=headers,
        )
        return GenieGenerateDownloadFullQueryResultResponse.from_dict(res)

    def get_download_full_query_result(
        self, space_id: str, conversation_id: str, message_id: str, attachment_id: str, transient_statement_id: str
    ) -> GenieGetDownloadFullQueryResultResponse:
        """Get download full query result status.

        Poll download progress and retrieve the SQL query result external link(s) upon completion. Warning:
        Databricks strongly recommends that you protect the URLs that are returned by the `EXTERNAL_LINKS`
        disposition. When you use the `EXTERNAL_LINKS` disposition, a short-lived, presigned URL is generated,
        which can be used to download the results directly from Amazon S3. As a short-lived access credential
        is embedded in this presigned URL, you should protect the URL. Because presigned URLs are already
        generated with embedded temporary access credentials, you must not set an Authorization header in the
        download requests. See [Execute Statement](:method:statementexecution/executestatement) for more
        details.

        :param space_id: str
          Space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        :param attachment_id: str
          Attachment ID
        :param transient_statement_id: str
          Transient Statement ID. This ID is provided by the [Start Download
          endpoint](:method:genie/startdownloadfullqueryresult)

        :returns: :class:`GenieGetDownloadFullQueryResultResponse`
        """

        query = {}
        if transient_statement_id is not None:
            query["transient_statement_id"] = transient_statement_id
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET",
            f"/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}/attachments/{attachment_id}/get-download",
            query=query,
            headers=headers,
        )
        return GenieGetDownloadFullQueryResultResponse.from_dict(res)

    def get_message(self, space_id: str, conversation_id: str, message_id: str) -> GenieMessage:
        """Get conversation message.

        Get message from conversation.

        :param space_id: str
          The ID associated with the Genie space where the target conversation is located.
        :param conversation_id: str
          The ID associated with the target conversation.
        :param message_id: str
          The ID associated with the target message from the identified conversation.

        :returns: :class:`GenieMessage`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET",
            f"/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}",
            headers=headers,
        )
        return GenieMessage.from_dict(res)

    def get_message_attachment_query_result(
        self, space_id: str, conversation_id: str, message_id: str, attachment_id: str
    ) -> GenieGetMessageQueryResultResponse:
        """Get message attachment SQL query result.

        Get the result of SQL query if the message has a query attachment. This is only available if a message
        has a query attachment and the message status is `EXECUTING_QUERY` OR `COMPLETED`.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        :param attachment_id: str
          Attachment ID

        :returns: :class:`GenieGetMessageQueryResultResponse`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET",
            f"/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}/attachments/{attachment_id}/query-result",
            headers=headers,
        )
        return GenieGetMessageQueryResultResponse.from_dict(res)

    def get_message_query_result(
        self, space_id: str, conversation_id: str, message_id: str
    ) -> GenieGetMessageQueryResultResponse:
        """[Deprecated] Get conversation message SQL query result.

        Get the result of SQL query if the message has a query attachment. This is only available if a message
        has a query attachment and the message status is `EXECUTING_QUERY`.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID

        :returns: :class:`GenieGetMessageQueryResultResponse`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET",
            f"/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}/query-result",
            headers=headers,
        )
        return GenieGetMessageQueryResultResponse.from_dict(res)

    def get_message_query_result_by_attachment(
        self, space_id: str, conversation_id: str, message_id: str, attachment_id: str
    ) -> GenieGetMessageQueryResultResponse:
        """[Deprecated] Get conversation message SQL query result.

        Get the result of SQL query if the message has a query attachment. This is only available if a message
        has a query attachment and the message status is `EXECUTING_QUERY` OR `COMPLETED`.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        :param attachment_id: str
          Attachment ID

        :returns: :class:`GenieGetMessageQueryResultResponse`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET",
            f"/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}/query-result/{attachment_id}",
            headers=headers,
        )
        return GenieGetMessageQueryResultResponse.from_dict(res)

    def get_space(self, space_id: str) -> GenieSpace:
        """Get Genie Space.

        Get details of a Genie Space.

        :param space_id: str
          The ID associated with the Genie space

        :returns: :class:`GenieSpace`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/genie/spaces/{space_id}", headers=headers)
        return GenieSpace.from_dict(res)

    def start_conversation(self, space_id: str, content: str) -> GenieStartConversationResponse:
        """Start conversation.

        Start a new conversation.

        :param space_id: str
          The ID associated with the Genie space where you want to start a conversation.
        :param content: str
          The text of the message that starts the conversation.

        :returns:
          Long-running operation waiter for :class:`GenieMessage`.
          See :method:WaitGetMessageGenieCompleted for more details.
        """
        body = {}
        if content is not None:
            body["content"] = content
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/genie/spaces/{space_id}/start-conversation", body=body, headers=headers)
        return GenieStartConversationResponse.from_dict(res)


class LakeviewAPI:
    """These APIs provide specific management operations for Lakeview dashboards. Generic resource management can
    be done with Workspace API (import, export, get-status, list, delete)."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, *, dashboard: Optional[Dashboard] = None) -> Dashboard:
        """Create dashboard.

        Create a draft dashboard.

        :param dashboard: :class:`Dashboard` (optional)

        :returns: :class:`Dashboard`
        """
        body = dashboard.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/lakeview/dashboards", body=body, headers=headers)
        return Dashboard.from_dict(res)

    def create_schedule(self, dashboard_id: str, *, schedule: Optional[Schedule] = None) -> Schedule:
        """Create dashboard schedule.

        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param schedule: :class:`Schedule` (optional)

        :returns: :class:`Schedule`
        """
        body = schedule.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/lakeview/dashboards/{dashboard_id}/schedules", body=body, headers=headers)
        return Schedule.from_dict(res)

    def create_subscription(
        self, dashboard_id: str, schedule_id: str, *, subscription: Optional[Subscription] = None
    ) -> Subscription:
        """Create schedule subscription.

        :param dashboard_id: str
          UUID identifying the dashboard to which the subscription belongs.
        :param schedule_id: str
          UUID identifying the schedule to which the subscription belongs.
        :param subscription: :class:`Subscription` (optional)

        :returns: :class:`Subscription`
        """
        body = subscription.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}/subscriptions",
            body=body,
            headers=headers,
        )
        return Subscription.from_dict(res)

    def delete_schedule(self, dashboard_id: str, schedule_id: str, *, etag: Optional[str] = None):
        """Delete dashboard schedule.

        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param schedule_id: str
          UUID identifying the schedule.
        :param etag: str (optional)
          The etag for the schedule. Optionally, it can be provided to verify that the schedule has not been
          modified from its last retrieval.


        """

        query = {}
        if etag is not None:
            query["etag"] = etag
        headers = {
            "Accept": "application/json",
        }

        self._api.do(
            "DELETE",
            f"/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}",
            query=query,
            headers=headers,
        )

    def delete_subscription(
        self, dashboard_id: str, schedule_id: str, subscription_id: str, *, etag: Optional[str] = None
    ):
        """Delete schedule subscription.

        :param dashboard_id: str
          UUID identifying the dashboard which the subscription belongs.
        :param schedule_id: str
          UUID identifying the schedule which the subscription belongs.
        :param subscription_id: str
          UUID identifying the subscription.
        :param etag: str (optional)
          The etag for the subscription. Can be optionally provided to ensure that the subscription has not
          been modified since the last read.


        """

        query = {}
        if etag is not None:
            query["etag"] = etag
        headers = {
            "Accept": "application/json",
        }

        self._api.do(
            "DELETE",
            f"/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}/subscriptions/{subscription_id}",
            query=query,
            headers=headers,
        )

    def get(self, dashboard_id: str) -> Dashboard:
        """Get dashboard.

        Get a draft dashboard.

        :param dashboard_id: str
          UUID identifying the dashboard.

        :returns: :class:`Dashboard`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/lakeview/dashboards/{dashboard_id}", headers=headers)
        return Dashboard.from_dict(res)

    def get_published(self, dashboard_id: str) -> PublishedDashboard:
        """Get published dashboard.

        Get the current published dashboard.

        :param dashboard_id: str
          UUID identifying the published dashboard.

        :returns: :class:`PublishedDashboard`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/lakeview/dashboards/{dashboard_id}/published", headers=headers)
        return PublishedDashboard.from_dict(res)

    def get_schedule(self, dashboard_id: str, schedule_id: str) -> Schedule:
        """Get dashboard schedule.

        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param schedule_id: str
          UUID identifying the schedule.

        :returns: :class:`Schedule`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET", f"/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}", headers=headers
        )
        return Schedule.from_dict(res)

    def get_subscription(self, dashboard_id: str, schedule_id: str, subscription_id: str) -> Subscription:
        """Get schedule subscription.

        :param dashboard_id: str
          UUID identifying the dashboard which the subscription belongs.
        :param schedule_id: str
          UUID identifying the schedule which the subscription belongs.
        :param subscription_id: str
          UUID identifying the subscription.

        :returns: :class:`Subscription`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET",
            f"/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}/subscriptions/{subscription_id}",
            headers=headers,
        )
        return Subscription.from_dict(res)

    def list(
        self,
        *,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        show_trashed: Optional[bool] = None,
        view: Optional[DashboardView] = None,
    ) -> Iterator[Dashboard]:
        """List dashboards.

        :param page_size: int (optional)
          The number of dashboards to return per page.
        :param page_token: str (optional)
          A page token, received from a previous `ListDashboards` call. This token can be used to retrieve the
          subsequent page.
        :param show_trashed: bool (optional)
          The flag to include dashboards located in the trash. If unspecified, only active dashboards will be
          returned.
        :param view: :class:`DashboardView` (optional)
          `DASHBOARD_VIEW_BASIC`only includes summary metadata from the dashboard.

        :returns: Iterator over :class:`Dashboard`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if show_trashed is not None:
            query["show_trashed"] = show_trashed
        if view is not None:
            query["view"] = view.value
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do("GET", "/api/2.0/lakeview/dashboards", query=query, headers=headers)
            if "dashboards" in json:
                for v in json["dashboards"]:
                    yield Dashboard.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_schedules(
        self, dashboard_id: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Schedule]:
        """List dashboard schedules.

        :param dashboard_id: str
          UUID identifying the dashboard to which the schedules belongs.
        :param page_size: int (optional)
          The number of schedules to return per page.
        :param page_token: str (optional)
          A page token, received from a previous `ListSchedules` call. Use this to retrieve the subsequent
          page.

        :returns: Iterator over :class:`Schedule`
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
            json = self._api.do(
                "GET", f"/api/2.0/lakeview/dashboards/{dashboard_id}/schedules", query=query, headers=headers
            )
            if "schedules" in json:
                for v in json["schedules"]:
                    yield Schedule.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_subscriptions(
        self, dashboard_id: str, schedule_id: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Subscription]:
        """List schedule subscriptions.

        :param dashboard_id: str
          UUID identifying the dashboard which the subscriptions belongs.
        :param schedule_id: str
          UUID identifying the schedule which the subscriptions belongs.
        :param page_size: int (optional)
          The number of subscriptions to return per page.
        :param page_token: str (optional)
          A page token, received from a previous `ListSubscriptions` call. Use this to retrieve the subsequent
          page.

        :returns: Iterator over :class:`Subscription`
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
            json = self._api.do(
                "GET",
                f"/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}/subscriptions",
                query=query,
                headers=headers,
            )
            if "subscriptions" in json:
                for v in json["subscriptions"]:
                    yield Subscription.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def migrate(
        self,
        source_dashboard_id: str,
        *,
        display_name: Optional[str] = None,
        parent_path: Optional[str] = None,
        update_parameter_syntax: Optional[bool] = None,
    ) -> Dashboard:
        """Migrate dashboard.

        Migrates a classic SQL dashboard to Lakeview.

        :param source_dashboard_id: str
          UUID of the dashboard to be migrated.
        :param display_name: str (optional)
          Display name for the new Lakeview dashboard.
        :param parent_path: str (optional)
          The workspace path of the folder to contain the migrated Lakeview dashboard.
        :param update_parameter_syntax: bool (optional)
          Flag to indicate if mustache parameter syntax ({{ param }}) should be auto-updated to named syntax
          (:param) when converting datasets in the dashboard.

        :returns: :class:`Dashboard`
        """
        body = {}
        if display_name is not None:
            body["display_name"] = display_name
        if parent_path is not None:
            body["parent_path"] = parent_path
        if source_dashboard_id is not None:
            body["source_dashboard_id"] = source_dashboard_id
        if update_parameter_syntax is not None:
            body["update_parameter_syntax"] = update_parameter_syntax
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/lakeview/dashboards/migrate", body=body, headers=headers)
        return Dashboard.from_dict(res)

    def publish(
        self, dashboard_id: str, *, embed_credentials: Optional[bool] = None, warehouse_id: Optional[str] = None
    ) -> PublishedDashboard:
        """Publish dashboard.

        Publish the current draft dashboard.

        :param dashboard_id: str
          UUID identifying the dashboard to be published.
        :param embed_credentials: bool (optional)
          Flag to indicate if the publisher's credentials should be embedded in the published dashboard. These
          embedded credentials will be used to execute the published dashboard's queries.
        :param warehouse_id: str (optional)
          The ID of the warehouse that can be used to override the warehouse which was set in the draft.

        :returns: :class:`PublishedDashboard`
        """
        body = {}
        if embed_credentials is not None:
            body["embed_credentials"] = embed_credentials
        if warehouse_id is not None:
            body["warehouse_id"] = warehouse_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/lakeview/dashboards/{dashboard_id}/published", body=body, headers=headers)
        return PublishedDashboard.from_dict(res)

    def trash(self, dashboard_id: str):
        """Trash dashboard.

        Trash a dashboard.

        :param dashboard_id: str
          UUID identifying the dashboard.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/lakeview/dashboards/{dashboard_id}", headers=headers)

    def unpublish(self, dashboard_id: str):
        """Unpublish dashboard.

        Unpublish the dashboard.

        :param dashboard_id: str
          UUID identifying the published dashboard.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/lakeview/dashboards/{dashboard_id}/published", headers=headers)

    def update(self, dashboard_id: str, *, dashboard: Optional[Dashboard] = None) -> Dashboard:
        """Update dashboard.

        Update a draft dashboard.

        :param dashboard_id: str
          UUID identifying the dashboard.
        :param dashboard: :class:`Dashboard` (optional)

        :returns: :class:`Dashboard`
        """
        body = dashboard.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/lakeview/dashboards/{dashboard_id}", body=body, headers=headers)
        return Dashboard.from_dict(res)

    def update_schedule(self, dashboard_id: str, schedule_id: str, *, schedule: Optional[Schedule] = None) -> Schedule:
        """Update dashboard schedule.

        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param schedule_id: str
          UUID identifying the schedule.
        :param schedule: :class:`Schedule` (optional)

        :returns: :class:`Schedule`
        """
        body = schedule.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "PUT", f"/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}", body=body, headers=headers
        )
        return Schedule.from_dict(res)


class LakeviewEmbeddedAPI:
    """Token-based Lakeview APIs for embedding dashboards in external applications."""

    def __init__(self, api_client):
        self._api = api_client

    def get_published_dashboard_embedded(self, dashboard_id: str):
        """Read a published dashboard in an embedded ui.

        Get the current published dashboard within an embedded context.

        :param dashboard_id: str
          UUID identifying the published dashboard.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("GET", f"/api/2.0/lakeview/dashboards/{dashboard_id}/published/embedded", headers=headers)


class QueryExecutionAPI:
    """Query execution APIs for AI / BI Dashboards"""

    def __init__(self, api_client):
        self._api = api_client

    def cancel_published_query_execution(
        self, dashboard_name: str, dashboard_revision_id: str, *, tokens: Optional[List[str]] = None
    ) -> CancelQueryExecutionResponse:
        """Cancel the results for the a query for a published, embedded dashboard.

        :param dashboard_name: str
        :param dashboard_revision_id: str
        :param tokens: List[str] (optional)
          Example: EC0A..ChAB7WCEn_4Qo4vkLqEbXsxxEgh3Y2pbWw45WhoQXgZSQo9aS5q2ZvFcbvbx9CgA-PAEAQ

        :returns: :class:`CancelQueryExecutionResponse`
        """

        query = {}
        if dashboard_name is not None:
            query["dashboard_name"] = dashboard_name
        if dashboard_revision_id is not None:
            query["dashboard_revision_id"] = dashboard_revision_id
        if tokens is not None:
            query["tokens"] = [v for v in tokens]
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("DELETE", "/api/2.0/lakeview-query/query/published", query=query, headers=headers)
        return CancelQueryExecutionResponse.from_dict(res)

    def execute_published_dashboard_query(
        self, dashboard_name: str, dashboard_revision_id: str, *, override_warehouse_id: Optional[str] = None
    ):
        """Execute a query for a published dashboard.

        :param dashboard_name: str
          Dashboard name and revision_id is required to retrieve PublishedDatasetDataModel which contains the
          list of datasets, warehouse_id, and embedded_credentials
        :param dashboard_revision_id: str
        :param override_warehouse_id: str (optional)
          A dashboard schedule can override the warehouse used as compute for processing the published
          dashboard queries


        """
        body = {}
        if dashboard_name is not None:
            body["dashboard_name"] = dashboard_name
        if dashboard_revision_id is not None:
            body["dashboard_revision_id"] = dashboard_revision_id
        if override_warehouse_id is not None:
            body["override_warehouse_id"] = override_warehouse_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        self._api.do("POST", "/api/2.0/lakeview-query/query/published", body=body, headers=headers)

    def poll_published_query_status(
        self, dashboard_name: str, dashboard_revision_id: str, *, tokens: Optional[List[str]] = None
    ) -> PollQueryStatusResponse:
        """Poll the results for the a query for a published, embedded dashboard.

        :param dashboard_name: str
        :param dashboard_revision_id: str
        :param tokens: List[str] (optional)
          Example: EC0A..ChAB7WCEn_4Qo4vkLqEbXsxxEgh3Y2pbWw45WhoQXgZSQo9aS5q2ZvFcbvbx9CgA-PAEAQ

        :returns: :class:`PollQueryStatusResponse`
        """

        query = {}
        if dashboard_name is not None:
            query["dashboard_name"] = dashboard_name
        if dashboard_revision_id is not None:
            query["dashboard_revision_id"] = dashboard_revision_id
        if tokens is not None:
            query["tokens"] = [v for v in tokens]
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", "/api/2.0/lakeview-query/query/published", query=query, headers=headers)
        return PollQueryStatusResponse.from_dict(res)

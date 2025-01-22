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

from databricks.sdk.service import sql

# all definitions in this file are in alphabetical order


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
            body['quartz_cron_expression'] = self.quartz_cron_expression
        if self.timezone_id is not None: body['timezone_id'] = self.timezone_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CronSchedule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.quartz_cron_expression is not None:
            body['quartz_cron_expression'] = self.quartz_cron_expression
        if self.timezone_id is not None: body['timezone_id'] = self.timezone_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CronSchedule:
        """Deserializes the CronSchedule from a dictionary."""
        return cls(quartz_cron_expression=d.get('quartz_cron_expression', None),
                   timezone_id=d.get('timezone_id', None))


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
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.etag is not None: body['etag'] = self.etag
        if self.lifecycle_state is not None: body['lifecycle_state'] = self.lifecycle_state.value
        if self.parent_path is not None: body['parent_path'] = self.parent_path
        if self.path is not None: body['path'] = self.path
        if self.serialized_dashboard is not None: body['serialized_dashboard'] = self.serialized_dashboard
        if self.update_time is not None: body['update_time'] = self.update_time
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Dashboard into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.etag is not None: body['etag'] = self.etag
        if self.lifecycle_state is not None: body['lifecycle_state'] = self.lifecycle_state
        if self.parent_path is not None: body['parent_path'] = self.parent_path
        if self.path is not None: body['path'] = self.path
        if self.serialized_dashboard is not None: body['serialized_dashboard'] = self.serialized_dashboard
        if self.update_time is not None: body['update_time'] = self.update_time
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Dashboard:
        """Deserializes the Dashboard from a dictionary."""
        return cls(create_time=d.get('create_time', None),
                   dashboard_id=d.get('dashboard_id', None),
                   display_name=d.get('display_name', None),
                   etag=d.get('etag', None),
                   lifecycle_state=_enum(d, 'lifecycle_state', LifecycleState),
                   parent_path=d.get('parent_path', None),
                   path=d.get('path', None),
                   serialized_dashboard=d.get('serialized_dashboard', None),
                   update_time=d.get('update_time', None),
                   warehouse_id=d.get('warehouse_id', None))


class DashboardView(Enum):

    DASHBOARD_VIEW_BASIC = 'DASHBOARD_VIEW_BASIC'


class DataType(Enum):

    DATA_TYPE_ARRAY = 'DATA_TYPE_ARRAY'
    DATA_TYPE_BIG_INT = 'DATA_TYPE_BIG_INT'
    DATA_TYPE_BINARY = 'DATA_TYPE_BINARY'
    DATA_TYPE_BOOLEAN = 'DATA_TYPE_BOOLEAN'
    DATA_TYPE_DATE = 'DATA_TYPE_DATE'
    DATA_TYPE_DECIMAL = 'DATA_TYPE_DECIMAL'
    DATA_TYPE_DOUBLE = 'DATA_TYPE_DOUBLE'
    DATA_TYPE_FLOAT = 'DATA_TYPE_FLOAT'
    DATA_TYPE_INT = 'DATA_TYPE_INT'
    DATA_TYPE_INTERVAL = 'DATA_TYPE_INTERVAL'
    DATA_TYPE_MAP = 'DATA_TYPE_MAP'
    DATA_TYPE_SMALL_INT = 'DATA_TYPE_SMALL_INT'
    DATA_TYPE_STRING = 'DATA_TYPE_STRING'
    DATA_TYPE_STRUCT = 'DATA_TYPE_STRUCT'
    DATA_TYPE_TIMESTAMP = 'DATA_TYPE_TIMESTAMP'
    DATA_TYPE_TINY_INT = 'DATA_TYPE_TINY_INT'
    DATA_TYPE_VOID = 'DATA_TYPE_VOID'


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
    def from_dict(cls, d: Dict[str, any]) -> DeleteScheduleResponse:
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
    def from_dict(cls, d: Dict[str, any]) -> DeleteSubscriptionResponse:
        """Deserializes the DeleteSubscriptionResponse from a dictionary."""
        return cls()


@dataclass
class GenieAttachment:
    """Genie AI Response"""

    query: Optional[QueryAttachment] = None

    text: Optional[TextAttachment] = None

    def as_dict(self) -> dict:
        """Serializes the GenieAttachment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.query: body['query'] = self.query.as_dict()
        if self.text: body['text'] = self.text.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAttachment into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.query: body['query'] = self.query
        if self.text: body['text'] = self.text
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GenieAttachment:
        """Deserializes the GenieAttachment from a dictionary."""
        return cls(query=_from_dict(d, 'query', QueryAttachment), text=_from_dict(d, 'text', TextAttachment))


@dataclass
class GenieConversation:
    id: str
    """Conversation ID"""

    space_id: str
    """Genie space ID"""

    user_id: int
    """ID of the user who created the conversation"""

    title: str
    """Conversation title"""

    created_timestamp: Optional[int] = None
    """Timestamp when the message was created"""

    last_updated_timestamp: Optional[int] = None
    """Timestamp when the message was last updated"""

    def as_dict(self) -> dict:
        """Serializes the GenieConversation into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.created_timestamp is not None: body['created_timestamp'] = self.created_timestamp
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.space_id is not None: body['space_id'] = self.space_id
        if self.title is not None: body['title'] = self.title
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieConversation into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.created_timestamp is not None: body['created_timestamp'] = self.created_timestamp
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.space_id is not None: body['space_id'] = self.space_id
        if self.title is not None: body['title'] = self.title
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GenieConversation:
        """Deserializes the GenieConversation from a dictionary."""
        return cls(created_timestamp=d.get('created_timestamp', None),
                   id=d.get('id', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   space_id=d.get('space_id', None),
                   title=d.get('title', None),
                   user_id=d.get('user_id', None))


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
        if self.content is not None: body['content'] = self.content
        if self.conversation_id is not None: body['conversation_id'] = self.conversation_id
        if self.space_id is not None: body['space_id'] = self.space_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieCreateConversationMessageRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.content is not None: body['content'] = self.content
        if self.conversation_id is not None: body['conversation_id'] = self.conversation_id
        if self.space_id is not None: body['space_id'] = self.space_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GenieCreateConversationMessageRequest:
        """Deserializes the GenieCreateConversationMessageRequest from a dictionary."""
        return cls(content=d.get('content', None),
                   conversation_id=d.get('conversation_id', None),
                   space_id=d.get('space_id', None))


@dataclass
class GenieGetMessageQueryResultResponse:
    statement_response: Optional[sql.StatementResponse] = None
    """SQL Statement Execution response. See [Get status, manifest, and result first
    chunk](:method:statementexecution/getstatement) for more details."""

    def as_dict(self) -> dict:
        """Serializes the GenieGetMessageQueryResultResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.statement_response: body['statement_response'] = self.statement_response.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieGetMessageQueryResultResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.statement_response: body['statement_response'] = self.statement_response
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GenieGetMessageQueryResultResponse:
        """Deserializes the GenieGetMessageQueryResultResponse from a dictionary."""
        return cls(statement_response=_from_dict(d, 'statement_response', sql.StatementResponse))


@dataclass
class GenieMessage:
    id: str
    """Message ID"""

    space_id: str
    """Genie space ID"""

    conversation_id: str
    """Conversation ID"""

    content: str
    """User message content"""

    attachments: Optional[List[GenieAttachment]] = None
    """AI produced response to the message"""

    created_timestamp: Optional[int] = None
    """Timestamp when the message was created"""

    error: Optional[MessageError] = None
    """Error message if AI failed to respond to the message"""

    last_updated_timestamp: Optional[int] = None
    """Timestamp when the message was last updated"""

    query_result: Optional[Result] = None
    """The result of SQL query if the message has a query attachment"""

    status: Optional[MessageStatus] = None
    """MesssageStatus. The possible values are: * `FETCHING_METADATA`: Fetching metadata from the data
    sources. * `FILTERING_CONTEXT`: Running smart context step to determine relevant context. *
    `ASKING_AI`: Waiting for the LLM to respond to the users question. * `PENDING_WAREHOUSE`:
    Waiting for warehouse before the SQL query can start executing. * `EXECUTING_QUERY`: Executing
    AI provided SQL query. Get the SQL query result by calling
    [getMessageQueryResult](:method:genie/getMessageQueryResult) API. **Important: The message
    status will stay in the `EXECUTING_QUERY` until a client calls
    [getMessageQueryResult](:method:genie/getMessageQueryResult)**. * `FAILED`: Generating a
    response or the executing the query failed. Please see `error` field. * `COMPLETED`: Message
    processing is completed. Results are in the `attachments` field. Get the SQL query result by
    calling [getMessageQueryResult](:method:genie/getMessageQueryResult) API. * `SUBMITTED`: Message
    has been submitted. * `QUERY_RESULT_EXPIRED`: SQL result is not available anymore. The user
    needs to execute the query again. * `CANCELLED`: Message has been cancelled."""

    user_id: Optional[int] = None
    """ID of the user who created the message"""

    def as_dict(self) -> dict:
        """Serializes the GenieMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.attachments: body['attachments'] = [v.as_dict() for v in self.attachments]
        if self.content is not None: body['content'] = self.content
        if self.conversation_id is not None: body['conversation_id'] = self.conversation_id
        if self.created_timestamp is not None: body['created_timestamp'] = self.created_timestamp
        if self.error: body['error'] = self.error.as_dict()
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.query_result: body['query_result'] = self.query_result.as_dict()
        if self.space_id is not None: body['space_id'] = self.space_id
        if self.status is not None: body['status'] = self.status.value
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.attachments: body['attachments'] = self.attachments
        if self.content is not None: body['content'] = self.content
        if self.conversation_id is not None: body['conversation_id'] = self.conversation_id
        if self.created_timestamp is not None: body['created_timestamp'] = self.created_timestamp
        if self.error: body['error'] = self.error
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.query_result: body['query_result'] = self.query_result
        if self.space_id is not None: body['space_id'] = self.space_id
        if self.status is not None: body['status'] = self.status
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GenieMessage:
        """Deserializes the GenieMessage from a dictionary."""
        return cls(attachments=_repeated_dict(d, 'attachments', GenieAttachment),
                   content=d.get('content', None),
                   conversation_id=d.get('conversation_id', None),
                   created_timestamp=d.get('created_timestamp', None),
                   error=_from_dict(d, 'error', MessageError),
                   id=d.get('id', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   query_result=_from_dict(d, 'query_result', Result),
                   space_id=d.get('space_id', None),
                   status=_enum(d, 'status', MessageStatus),
                   user_id=d.get('user_id', None))


@dataclass
class GenieStartConversationMessageRequest:
    content: str
    """The text of the message that starts the conversation."""

    space_id: Optional[str] = None
    """The ID associated with the Genie space where you want to start a conversation."""

    def as_dict(self) -> dict:
        """Serializes the GenieStartConversationMessageRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.content is not None: body['content'] = self.content
        if self.space_id is not None: body['space_id'] = self.space_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieStartConversationMessageRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.content is not None: body['content'] = self.content
        if self.space_id is not None: body['space_id'] = self.space_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GenieStartConversationMessageRequest:
        """Deserializes the GenieStartConversationMessageRequest from a dictionary."""
        return cls(content=d.get('content', None), space_id=d.get('space_id', None))


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
        if self.conversation: body['conversation'] = self.conversation.as_dict()
        if self.conversation_id is not None: body['conversation_id'] = self.conversation_id
        if self.message: body['message'] = self.message.as_dict()
        if self.message_id is not None: body['message_id'] = self.message_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieStartConversationResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.conversation: body['conversation'] = self.conversation
        if self.conversation_id is not None: body['conversation_id'] = self.conversation_id
        if self.message: body['message'] = self.message
        if self.message_id is not None: body['message_id'] = self.message_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GenieStartConversationResponse:
        """Deserializes the GenieStartConversationResponse from a dictionary."""
        return cls(conversation=_from_dict(d, 'conversation', GenieConversation),
                   conversation_id=d.get('conversation_id', None),
                   message=_from_dict(d, 'message', GenieMessage),
                   message_id=d.get('message_id', None))


class LifecycleState(Enum):

    ACTIVE = 'ACTIVE'
    TRASHED = 'TRASHED'


@dataclass
class ListDashboardsResponse:
    dashboards: Optional[List[Dashboard]] = None

    next_page_token: Optional[str] = None
    """A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent dashboards."""

    def as_dict(self) -> dict:
        """Serializes the ListDashboardsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.dashboards: body['dashboards'] = [v.as_dict() for v in self.dashboards]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListDashboardsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.dashboards: body['dashboards'] = self.dashboards
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListDashboardsResponse:
        """Deserializes the ListDashboardsResponse from a dictionary."""
        return cls(dashboards=_repeated_dict(d, 'dashboards', Dashboard),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListSchedulesResponse:
    next_page_token: Optional[str] = None
    """A token that can be used as a `page_token` in subsequent requests to retrieve the next page of
    results. If this field is omitted, there are no subsequent schedules."""

    schedules: Optional[List[Schedule]] = None

    def as_dict(self) -> dict:
        """Serializes the ListSchedulesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.schedules: body['schedules'] = [v.as_dict() for v in self.schedules]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListSchedulesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.schedules: body['schedules'] = self.schedules
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListSchedulesResponse:
        """Deserializes the ListSchedulesResponse from a dictionary."""
        return cls(next_page_token=d.get('next_page_token', None),
                   schedules=_repeated_dict(d, 'schedules', Schedule))


@dataclass
class ListSubscriptionsResponse:
    next_page_token: Optional[str] = None
    """A token that can be used as a `page_token` in subsequent requests to retrieve the next page of
    results. If this field is omitted, there are no subsequent subscriptions."""

    subscriptions: Optional[List[Subscription]] = None

    def as_dict(self) -> dict:
        """Serializes the ListSubscriptionsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.subscriptions: body['subscriptions'] = [v.as_dict() for v in self.subscriptions]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListSubscriptionsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.subscriptions: body['subscriptions'] = self.subscriptions
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListSubscriptionsResponse:
        """Deserializes the ListSubscriptionsResponse from a dictionary."""
        return cls(next_page_token=d.get('next_page_token', None),
                   subscriptions=_repeated_dict(d, 'subscriptions', Subscription))


@dataclass
class MessageError:
    error: Optional[str] = None

    type: Optional[MessageErrorType] = None

    def as_dict(self) -> dict:
        """Serializes the MessageError into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.error is not None: body['error'] = self.error
        if self.type is not None: body['type'] = self.type.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MessageError into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.error is not None: body['error'] = self.error
        if self.type is not None: body['type'] = self.type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MessageError:
        """Deserializes the MessageError from a dictionary."""
        return cls(error=d.get('error', None), type=_enum(d, 'type', MessageErrorType))


class MessageErrorType(Enum):

    BLOCK_MULTIPLE_EXECUTIONS_EXCEPTION = 'BLOCK_MULTIPLE_EXECUTIONS_EXCEPTION'
    CHAT_COMPLETION_CLIENT_EXCEPTION = 'CHAT_COMPLETION_CLIENT_EXCEPTION'
    CHAT_COMPLETION_CLIENT_TIMEOUT_EXCEPTION = 'CHAT_COMPLETION_CLIENT_TIMEOUT_EXCEPTION'
    CHAT_COMPLETION_NETWORK_EXCEPTION = 'CHAT_COMPLETION_NETWORK_EXCEPTION'
    CONTENT_FILTER_EXCEPTION = 'CONTENT_FILTER_EXCEPTION'
    CONTEXT_EXCEEDED_EXCEPTION = 'CONTEXT_EXCEEDED_EXCEPTION'
    COULD_NOT_GET_UC_SCHEMA_EXCEPTION = 'COULD_NOT_GET_UC_SCHEMA_EXCEPTION'
    DEPLOYMENT_NOT_FOUND_EXCEPTION = 'DEPLOYMENT_NOT_FOUND_EXCEPTION'
    FUNCTIONS_NOT_AVAILABLE_EXCEPTION = 'FUNCTIONS_NOT_AVAILABLE_EXCEPTION'
    FUNCTION_ARGUMENTS_INVALID_EXCEPTION = 'FUNCTION_ARGUMENTS_INVALID_EXCEPTION'
    FUNCTION_ARGUMENTS_INVALID_JSON_EXCEPTION = 'FUNCTION_ARGUMENTS_INVALID_JSON_EXCEPTION'
    FUNCTION_CALL_MISSING_PARAMETER_EXCEPTION = 'FUNCTION_CALL_MISSING_PARAMETER_EXCEPTION'
    GENERIC_CHAT_COMPLETION_EXCEPTION = 'GENERIC_CHAT_COMPLETION_EXCEPTION'
    GENERIC_CHAT_COMPLETION_SERVICE_EXCEPTION = 'GENERIC_CHAT_COMPLETION_SERVICE_EXCEPTION'
    GENERIC_SQL_EXEC_API_CALL_EXCEPTION = 'GENERIC_SQL_EXEC_API_CALL_EXCEPTION'
    ILLEGAL_PARAMETER_DEFINITION_EXCEPTION = 'ILLEGAL_PARAMETER_DEFINITION_EXCEPTION'
    INVALID_CERTIFIED_ANSWER_FUNCTION_EXCEPTION = 'INVALID_CERTIFIED_ANSWER_FUNCTION_EXCEPTION'
    INVALID_CERTIFIED_ANSWER_IDENTIFIER_EXCEPTION = 'INVALID_CERTIFIED_ANSWER_IDENTIFIER_EXCEPTION'
    INVALID_CHAT_COMPLETION_JSON_EXCEPTION = 'INVALID_CHAT_COMPLETION_JSON_EXCEPTION'
    INVALID_COMPLETION_REQUEST_EXCEPTION = 'INVALID_COMPLETION_REQUEST_EXCEPTION'
    INVALID_FUNCTION_CALL_EXCEPTION = 'INVALID_FUNCTION_CALL_EXCEPTION'
    INVALID_TABLE_IDENTIFIER_EXCEPTION = 'INVALID_TABLE_IDENTIFIER_EXCEPTION'
    LOCAL_CONTEXT_EXCEEDED_EXCEPTION = 'LOCAL_CONTEXT_EXCEEDED_EXCEPTION'
    MESSAGE_DELETED_WHILE_EXECUTING_EXCEPTION = 'MESSAGE_DELETED_WHILE_EXECUTING_EXCEPTION'
    MESSAGE_UPDATED_WHILE_EXECUTING_EXCEPTION = 'MESSAGE_UPDATED_WHILE_EXECUTING_EXCEPTION'
    NO_DEPLOYMENTS_AVAILABLE_TO_WORKSPACE = 'NO_DEPLOYMENTS_AVAILABLE_TO_WORKSPACE'
    NO_QUERY_TO_VISUALIZE_EXCEPTION = 'NO_QUERY_TO_VISUALIZE_EXCEPTION'
    NO_TABLES_TO_QUERY_EXCEPTION = 'NO_TABLES_TO_QUERY_EXCEPTION'
    RATE_LIMIT_EXCEEDED_GENERIC_EXCEPTION = 'RATE_LIMIT_EXCEEDED_GENERIC_EXCEPTION'
    RATE_LIMIT_EXCEEDED_SPECIFIED_WAIT_EXCEPTION = 'RATE_LIMIT_EXCEEDED_SPECIFIED_WAIT_EXCEPTION'
    REPLY_PROCESS_TIMEOUT_EXCEPTION = 'REPLY_PROCESS_TIMEOUT_EXCEPTION'
    RETRYABLE_PROCESSING_EXCEPTION = 'RETRYABLE_PROCESSING_EXCEPTION'
    SQL_EXECUTION_EXCEPTION = 'SQL_EXECUTION_EXCEPTION'
    TABLES_MISSING_EXCEPTION = 'TABLES_MISSING_EXCEPTION'
    TOO_MANY_CERTIFIED_ANSWERS_EXCEPTION = 'TOO_MANY_CERTIFIED_ANSWERS_EXCEPTION'
    TOO_MANY_TABLES_EXCEPTION = 'TOO_MANY_TABLES_EXCEPTION'
    UNEXPECTED_REPLY_PROCESS_EXCEPTION = 'UNEXPECTED_REPLY_PROCESS_EXCEPTION'
    UNKNOWN_AI_MODEL = 'UNKNOWN_AI_MODEL'
    WAREHOUSE_ACCESS_MISSING_EXCEPTION = 'WAREHOUSE_ACCESS_MISSING_EXCEPTION'
    WAREHOUSE_NOT_FOUND_EXCEPTION = 'WAREHOUSE_NOT_FOUND_EXCEPTION'


class MessageStatus(Enum):
    """MesssageStatus. The possible values are: * `FETCHING_METADATA`: Fetching metadata from the data
    sources. * `FILTERING_CONTEXT`: Running smart context step to determine relevant context. *
    `ASKING_AI`: Waiting for the LLM to respond to the users question. * `PENDING_WAREHOUSE`:
    Waiting for warehouse before the SQL query can start executing. * `EXECUTING_QUERY`: Executing
    AI provided SQL query. Get the SQL query result by calling
    [getMessageQueryResult](:method:genie/getMessageQueryResult) API. **Important: The message
    status will stay in the `EXECUTING_QUERY` until a client calls
    [getMessageQueryResult](:method:genie/getMessageQueryResult)**. * `FAILED`: Generating a
    response or the executing the query failed. Please see `error` field. * `COMPLETED`: Message
    processing is completed. Results are in the `attachments` field. Get the SQL query result by
    calling [getMessageQueryResult](:method:genie/getMessageQueryResult) API. * `SUBMITTED`: Message
    has been submitted. * `QUERY_RESULT_EXPIRED`: SQL result is not available anymore. The user
    needs to execute the query again. * `CANCELLED`: Message has been cancelled."""

    ASKING_AI = 'ASKING_AI'
    CANCELLED = 'CANCELLED'
    COMPLETED = 'COMPLETED'
    EXECUTING_QUERY = 'EXECUTING_QUERY'
    FAILED = 'FAILED'
    FETCHING_METADATA = 'FETCHING_METADATA'
    FILTERING_CONTEXT = 'FILTERING_CONTEXT'
    PENDING_WAREHOUSE = 'PENDING_WAREHOUSE'
    QUERY_RESULT_EXPIRED = 'QUERY_RESULT_EXPIRED'
    SUBMITTED = 'SUBMITTED'


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
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.parent_path is not None: body['parent_path'] = self.parent_path
        if self.source_dashboard_id is not None: body['source_dashboard_id'] = self.source_dashboard_id
        if self.update_parameter_syntax is not None:
            body['update_parameter_syntax'] = self.update_parameter_syntax
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MigrateDashboardRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.parent_path is not None: body['parent_path'] = self.parent_path
        if self.source_dashboard_id is not None: body['source_dashboard_id'] = self.source_dashboard_id
        if self.update_parameter_syntax is not None:
            body['update_parameter_syntax'] = self.update_parameter_syntax
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MigrateDashboardRequest:
        """Deserializes the MigrateDashboardRequest from a dictionary."""
        return cls(display_name=d.get('display_name', None),
                   parent_path=d.get('parent_path', None),
                   source_dashboard_id=d.get('source_dashboard_id', None),
                   update_parameter_syntax=d.get('update_parameter_syntax', None))


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
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.embed_credentials is not None: body['embed_credentials'] = self.embed_credentials
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PublishRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.embed_credentials is not None: body['embed_credentials'] = self.embed_credentials
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PublishRequest:
        """Deserializes the PublishRequest from a dictionary."""
        return cls(dashboard_id=d.get('dashboard_id', None),
                   embed_credentials=d.get('embed_credentials', None),
                   warehouse_id=d.get('warehouse_id', None))


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
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.embed_credentials is not None: body['embed_credentials'] = self.embed_credentials
        if self.revision_create_time is not None: body['revision_create_time'] = self.revision_create_time
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PublishedDashboard into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.embed_credentials is not None: body['embed_credentials'] = self.embed_credentials
        if self.revision_create_time is not None: body['revision_create_time'] = self.revision_create_time
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PublishedDashboard:
        """Deserializes the PublishedDashboard from a dictionary."""
        return cls(display_name=d.get('display_name', None),
                   embed_credentials=d.get('embed_credentials', None),
                   revision_create_time=d.get('revision_create_time', None),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class QueryAttachment:
    cached_query_schema: Optional[QuerySchema] = None

    description: Optional[str] = None
    """Description of the query"""

    id: Optional[str] = None

    instruction_id: Optional[str] = None
    """If the query was created on an instruction (trusted asset) we link to the id"""

    instruction_title: Optional[str] = None
    """Always store the title next to the id in case the original instruction title changes or the
    instruction is deleted."""

    last_updated_timestamp: Optional[int] = None
    """Time when the user updated the query last"""

    query: Optional[str] = None
    """AI generated SQL query"""

    title: Optional[str] = None
    """Name of the query"""

    def as_dict(self) -> dict:
        """Serializes the QueryAttachment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.cached_query_schema: body['cached_query_schema'] = self.cached_query_schema.as_dict()
        if self.description is not None: body['description'] = self.description
        if self.id is not None: body['id'] = self.id
        if self.instruction_id is not None: body['instruction_id'] = self.instruction_id
        if self.instruction_title is not None: body['instruction_title'] = self.instruction_title
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.query is not None: body['query'] = self.query
        if self.title is not None: body['title'] = self.title
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the QueryAttachment into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.cached_query_schema: body['cached_query_schema'] = self.cached_query_schema
        if self.description is not None: body['description'] = self.description
        if self.id is not None: body['id'] = self.id
        if self.instruction_id is not None: body['instruction_id'] = self.instruction_id
        if self.instruction_title is not None: body['instruction_title'] = self.instruction_title
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.query is not None: body['query'] = self.query
        if self.title is not None: body['title'] = self.title
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> QueryAttachment:
        """Deserializes the QueryAttachment from a dictionary."""
        return cls(cached_query_schema=_from_dict(d, 'cached_query_schema', QuerySchema),
                   description=d.get('description', None),
                   id=d.get('id', None),
                   instruction_id=d.get('instruction_id', None),
                   instruction_title=d.get('instruction_title', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   query=d.get('query', None),
                   title=d.get('title', None))


@dataclass
class QuerySchema:
    columns: Optional[List[QuerySchemaColumn]] = None

    statement_id: Optional[str] = None
    """Used to determine if the stored query schema is compatible with the latest run. The service
    should always clear the schema when the query is re-executed."""

    def as_dict(self) -> dict:
        """Serializes the QuerySchema into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.columns: body['columns'] = [v.as_dict() for v in self.columns]
        if self.statement_id is not None: body['statement_id'] = self.statement_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the QuerySchema into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.columns: body['columns'] = self.columns
        if self.statement_id is not None: body['statement_id'] = self.statement_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> QuerySchema:
        """Deserializes the QuerySchema from a dictionary."""
        return cls(columns=_repeated_dict(d, 'columns', QuerySchemaColumn),
                   statement_id=d.get('statement_id', None))


@dataclass
class QuerySchemaColumn:
    name: str

    type_text: str
    """Corresponds to type desc"""

    data_type: DataType
    """Populated from https://docs.databricks.com/sql/language-manual/sql-ref-datatypes.html"""

    def as_dict(self) -> dict:
        """Serializes the QuerySchemaColumn into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.data_type is not None: body['data_type'] = self.data_type.value
        if self.name is not None: body['name'] = self.name
        if self.type_text is not None: body['type_text'] = self.type_text
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the QuerySchemaColumn into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.data_type is not None: body['data_type'] = self.data_type
        if self.name is not None: body['name'] = self.name
        if self.type_text is not None: body['type_text'] = self.type_text
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> QuerySchemaColumn:
        """Deserializes the QuerySchemaColumn from a dictionary."""
        return cls(data_type=_enum(d, 'data_type', DataType),
                   name=d.get('name', None),
                   type_text=d.get('type_text', None))


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
        if self.is_truncated is not None: body['is_truncated'] = self.is_truncated
        if self.row_count is not None: body['row_count'] = self.row_count
        if self.statement_id is not None: body['statement_id'] = self.statement_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Result into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.is_truncated is not None: body['is_truncated'] = self.is_truncated
        if self.row_count is not None: body['row_count'] = self.row_count
        if self.statement_id is not None: body['statement_id'] = self.statement_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Result:
        """Deserializes the Result from a dictionary."""
        return cls(is_truncated=d.get('is_truncated', None),
                   row_count=d.get('row_count', None),
                   statement_id=d.get('statement_id', None))


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
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.cron_schedule: body['cron_schedule'] = self.cron_schedule.as_dict()
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.etag is not None: body['etag'] = self.etag
        if self.pause_status is not None: body['pause_status'] = self.pause_status.value
        if self.schedule_id is not None: body['schedule_id'] = self.schedule_id
        if self.update_time is not None: body['update_time'] = self.update_time
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Schedule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.cron_schedule: body['cron_schedule'] = self.cron_schedule
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.etag is not None: body['etag'] = self.etag
        if self.pause_status is not None: body['pause_status'] = self.pause_status
        if self.schedule_id is not None: body['schedule_id'] = self.schedule_id
        if self.update_time is not None: body['update_time'] = self.update_time
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Schedule:
        """Deserializes the Schedule from a dictionary."""
        return cls(create_time=d.get('create_time', None),
                   cron_schedule=_from_dict(d, 'cron_schedule', CronSchedule),
                   dashboard_id=d.get('dashboard_id', None),
                   display_name=d.get('display_name', None),
                   etag=d.get('etag', None),
                   pause_status=_enum(d, 'pause_status', SchedulePauseStatus),
                   schedule_id=d.get('schedule_id', None),
                   update_time=d.get('update_time', None),
                   warehouse_id=d.get('warehouse_id', None))


class SchedulePauseStatus(Enum):

    PAUSED = 'PAUSED'
    UNPAUSED = 'UNPAUSED'


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
        if self.destination_subscriber: body['destination_subscriber'] = self.destination_subscriber.as_dict()
        if self.user_subscriber: body['user_subscriber'] = self.user_subscriber.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Subscriber into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.destination_subscriber: body['destination_subscriber'] = self.destination_subscriber
        if self.user_subscriber: body['user_subscriber'] = self.user_subscriber
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Subscriber:
        """Deserializes the Subscriber from a dictionary."""
        return cls(destination_subscriber=_from_dict(d, 'destination_subscriber',
                                                     SubscriptionSubscriberDestination),
                   user_subscriber=_from_dict(d, 'user_subscriber', SubscriptionSubscriberUser))


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
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.created_by_user_id is not None: body['created_by_user_id'] = self.created_by_user_id
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.etag is not None: body['etag'] = self.etag
        if self.schedule_id is not None: body['schedule_id'] = self.schedule_id
        if self.subscriber: body['subscriber'] = self.subscriber.as_dict()
        if self.subscription_id is not None: body['subscription_id'] = self.subscription_id
        if self.update_time is not None: body['update_time'] = self.update_time
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Subscription into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.created_by_user_id is not None: body['created_by_user_id'] = self.created_by_user_id
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.etag is not None: body['etag'] = self.etag
        if self.schedule_id is not None: body['schedule_id'] = self.schedule_id
        if self.subscriber: body['subscriber'] = self.subscriber
        if self.subscription_id is not None: body['subscription_id'] = self.subscription_id
        if self.update_time is not None: body['update_time'] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Subscription:
        """Deserializes the Subscription from a dictionary."""
        return cls(create_time=d.get('create_time', None),
                   created_by_user_id=d.get('created_by_user_id', None),
                   dashboard_id=d.get('dashboard_id', None),
                   etag=d.get('etag', None),
                   schedule_id=d.get('schedule_id', None),
                   subscriber=_from_dict(d, 'subscriber', Subscriber),
                   subscription_id=d.get('subscription_id', None),
                   update_time=d.get('update_time', None))


@dataclass
class SubscriptionSubscriberDestination:
    destination_id: str
    """The canonical identifier of the destination to receive email notification."""

    def as_dict(self) -> dict:
        """Serializes the SubscriptionSubscriberDestination into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.destination_id is not None: body['destination_id'] = self.destination_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SubscriptionSubscriberDestination into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.destination_id is not None: body['destination_id'] = self.destination_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> SubscriptionSubscriberDestination:
        """Deserializes the SubscriptionSubscriberDestination from a dictionary."""
        return cls(destination_id=d.get('destination_id', None))


@dataclass
class SubscriptionSubscriberUser:
    user_id: int
    """UserId of the subscriber."""

    def as_dict(self) -> dict:
        """Serializes the SubscriptionSubscriberUser into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SubscriptionSubscriberUser into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> SubscriptionSubscriberUser:
        """Deserializes the SubscriptionSubscriberUser from a dictionary."""
        return cls(user_id=d.get('user_id', None))


@dataclass
class TextAttachment:
    content: Optional[str] = None
    """AI generated message"""

    id: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the TextAttachment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.content is not None: body['content'] = self.content
        if self.id is not None: body['id'] = self.id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the TextAttachment into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.content is not None: body['content'] = self.content
        if self.id is not None: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TextAttachment:
        """Deserializes the TextAttachment from a dictionary."""
        return cls(content=d.get('content', None), id=d.get('id', None))


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
    def from_dict(cls, d: Dict[str, any]) -> TrashDashboardResponse:
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
    def from_dict(cls, d: Dict[str, any]) -> UnpublishDashboardResponse:
        """Deserializes the UnpublishDashboardResponse from a dictionary."""
        return cls()


class GenieAPI:
    """Genie provides a no-code experience for business users, powered by AI/BI. Analysts set up spaces that
    business users can use to ask questions using natural language. Genie uses data registered to Unity
    Catalog and requires at least CAN USE permission on a Pro or Serverless SQL warehouse. Also, Databricks
    Assistant must be enabled."""

    def __init__(self, api_client):
        self._api = api_client

    def wait_get_message_genie_completed(
            self,
            conversation_id: str,
            message_id: str,
            space_id: str,
            timeout=timedelta(minutes=20),
            callback: Optional[Callable[[GenieMessage], None]] = None) -> GenieMessage:
        deadline = time.time() + timeout.total_seconds()
        target_states = (MessageStatus.COMPLETED, )
        failure_states = (MessageStatus.FAILED, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get_message(conversation_id=conversation_id, message_id=message_id, space_id=space_id)
            status = poll.status
            status_message = f'current status: {status}'
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach COMPLETED, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"conversation_id={conversation_id}, message_id={message_id}, space_id={space_id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def create_message(self, space_id: str, conversation_id: str, content: str) -> Wait[GenieMessage]:
        """Create conversation message.
        
        Create new message in [conversation](:method:genie/startconversation). The AI response uses all
        previously created messages in the conversation to respond.
        
        :param space_id: str
          The ID associated with the Genie space where the conversation is started.
        :param conversation_id: str
          The ID associated with the conversation.
        :param content: str
          User message content.
        
        :returns:
          Long-running operation waiter for :class:`GenieMessage`.
          See :method:wait_get_message_genie_completed for more details.
        """
        body = {}
        if content is not None: body['content'] = content
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        op_response = self._api.do(
            'POST',
            f'/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages',
            body=body,
            headers=headers)
        return Wait(self.wait_get_message_genie_completed,
                    response=GenieMessage.from_dict(op_response),
                    conversation_id=conversation_id,
                    message_id=op_response['id'],
                    space_id=space_id)

    def create_message_and_wait(self,
                                space_id: str,
                                conversation_id: str,
                                content: str,
                                timeout=timedelta(minutes=20)) -> GenieMessage:
        return self.create_message(content=content, conversation_id=conversation_id,
                                   space_id=space_id).result(timeout=timeout)

    def execute_message_query(self, space_id: str, conversation_id: str,
                              message_id: str) -> GenieGetMessageQueryResultResponse:
        """Execute SQL query in a conversation message.
        
        Execute the SQL query in the message.
        
        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        
        :returns: :class:`GenieGetMessageQueryResultResponse`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'POST',
            f'/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}/execute-query',
            headers=headers)
        return GenieGetMessageQueryResultResponse.from_dict(res)

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

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}',
            headers=headers)
        return GenieMessage.from_dict(res)

    def get_message_query_result(self, space_id: str, conversation_id: str,
                                 message_id: str) -> GenieGetMessageQueryResultResponse:
        """Get conversation message SQL query result.
        
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

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}/query-result',
            headers=headers)
        return GenieGetMessageQueryResultResponse.from_dict(res)

    def start_conversation(self, space_id: str, content: str) -> Wait[GenieMessage]:
        """Start conversation.
        
        Start a new conversation.
        
        :param space_id: str
          The ID associated with the Genie space where you want to start a conversation.
        :param content: str
          The text of the message that starts the conversation.
        
        :returns:
          Long-running operation waiter for :class:`GenieMessage`.
          See :method:wait_get_message_genie_completed for more details.
        """
        body = {}
        if content is not None: body['content'] = content
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        op_response = self._api.do('POST',
                                   f'/api/2.0/genie/spaces/{space_id}/start-conversation',
                                   body=body,
                                   headers=headers)
        return Wait(self.wait_get_message_genie_completed,
                    response=GenieStartConversationResponse.from_dict(op_response),
                    conversation_id=op_response['conversation_id'],
                    message_id=op_response['message_id'],
                    space_id=space_id)

    def start_conversation_and_wait(self, space_id: str, content: str,
                                    timeout=timedelta(minutes=20)) -> GenieMessage:
        return self.start_conversation(content=content, space_id=space_id).result(timeout=timeout)


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
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.0/lakeview/dashboards', body=body, headers=headers)
        return Dashboard.from_dict(res)

    def create_schedule(self, dashboard_id: str, *, schedule: Optional[Schedule] = None) -> Schedule:
        """Create dashboard schedule.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param schedule: :class:`Schedule` (optional)
        
        :returns: :class:`Schedule`
        """
        body = schedule.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules',
                           body=body,
                           headers=headers)
        return Schedule.from_dict(res)

    def create_subscription(self,
                            dashboard_id: str,
                            schedule_id: str,
                            *,
                            subscription: Optional[Subscription] = None) -> Subscription:
        """Create schedule subscription.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the subscription belongs.
        :param schedule_id: str
          UUID identifying the schedule to which the subscription belongs.
        :param subscription: :class:`Subscription` (optional)
        
        :returns: :class:`Subscription`
        """
        body = subscription.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do(
            'POST',
            f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}/subscriptions',
            body=body,
            headers=headers)
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
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}',
                     query=query,
                     headers=headers)

    def delete_subscription(self,
                            dashboard_id: str,
                            schedule_id: str,
                            subscription_id: str,
                            *,
                            etag: Optional[str] = None):
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
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        self._api.do(
            'DELETE',
            f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}/subscriptions/{subscription_id}',
            query=query,
            headers=headers)

    def get(self, dashboard_id: str) -> Dashboard:
        """Get dashboard.
        
        Get a draft dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard.
        
        :returns: :class:`Dashboard`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/lakeview/dashboards/{dashboard_id}', headers=headers)
        return Dashboard.from_dict(res)

    def get_published(self, dashboard_id: str) -> PublishedDashboard:
        """Get published dashboard.
        
        Get the current published dashboard.
        
        :param dashboard_id: str
          UUID identifying the published dashboard.
        
        :returns: :class:`PublishedDashboard`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/lakeview/dashboards/{dashboard_id}/published', headers=headers)
        return PublishedDashboard.from_dict(res)

    def get_schedule(self, dashboard_id: str, schedule_id: str) -> Schedule:
        """Get dashboard schedule.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param schedule_id: str
          UUID identifying the schedule.
        
        :returns: :class:`Schedule`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}',
                           headers=headers)
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

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}/subscriptions/{subscription_id}',
            headers=headers)
        return Subscription.from_dict(res)

    def list(self,
             *,
             page_size: Optional[int] = None,
             page_token: Optional[str] = None,
             show_trashed: Optional[bool] = None,
             view: Optional[DashboardView] = None) -> Iterator[Dashboard]:
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
        if page_size is not None: query['page_size'] = page_size
        if page_token is not None: query['page_token'] = page_token
        if show_trashed is not None: query['show_trashed'] = show_trashed
        if view is not None: query['view'] = view.value
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.0/lakeview/dashboards', query=query, headers=headers)
            if 'dashboards' in json:
                for v in json['dashboards']:
                    yield Dashboard.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def list_schedules(self,
                       dashboard_id: str,
                       *,
                       page_size: Optional[int] = None,
                       page_token: Optional[str] = None) -> Iterator[Schedule]:
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
        if page_size is not None: query['page_size'] = page_size
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET',
                                f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules',
                                query=query,
                                headers=headers)
            if 'schedules' in json:
                for v in json['schedules']:
                    yield Schedule.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def list_subscriptions(self,
                           dashboard_id: str,
                           schedule_id: str,
                           *,
                           page_size: Optional[int] = None,
                           page_token: Optional[str] = None) -> Iterator[Subscription]:
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
        if page_size is not None: query['page_size'] = page_size
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do(
                'GET',
                f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}/subscriptions',
                query=query,
                headers=headers)
            if 'subscriptions' in json:
                for v in json['subscriptions']:
                    yield Subscription.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def migrate(self,
                source_dashboard_id: str,
                *,
                display_name: Optional[str] = None,
                parent_path: Optional[str] = None,
                update_parameter_syntax: Optional[bool] = None) -> Dashboard:
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
        if display_name is not None: body['display_name'] = display_name
        if parent_path is not None: body['parent_path'] = parent_path
        if source_dashboard_id is not None: body['source_dashboard_id'] = source_dashboard_id
        if update_parameter_syntax is not None: body['update_parameter_syntax'] = update_parameter_syntax
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.0/lakeview/dashboards/migrate', body=body, headers=headers)
        return Dashboard.from_dict(res)

    def publish(self,
                dashboard_id: str,
                *,
                embed_credentials: Optional[bool] = None,
                warehouse_id: Optional[str] = None) -> PublishedDashboard:
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
        if embed_credentials is not None: body['embed_credentials'] = embed_credentials
        if warehouse_id is not None: body['warehouse_id'] = warehouse_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/lakeview/dashboards/{dashboard_id}/published',
                           body=body,
                           headers=headers)
        return PublishedDashboard.from_dict(res)

    def trash(self, dashboard_id: str):
        """Trash dashboard.
        
        Trash a dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.0/lakeview/dashboards/{dashboard_id}', headers=headers)

    def unpublish(self, dashboard_id: str):
        """Unpublish dashboard.
        
        Unpublish the dashboard.
        
        :param dashboard_id: str
          UUID identifying the published dashboard.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.0/lakeview/dashboards/{dashboard_id}/published', headers=headers)

    def update(self, dashboard_id: str, *, dashboard: Optional[Dashboard] = None) -> Dashboard:
        """Update dashboard.
        
        Update a draft dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard.
        :param dashboard: :class:`Dashboard` (optional)
        
        :returns: :class:`Dashboard`
        """
        body = dashboard.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           f'/api/2.0/lakeview/dashboards/{dashboard_id}',
                           body=body,
                           headers=headers)
        return Dashboard.from_dict(res)

    def update_schedule(self,
                        dashboard_id: str,
                        schedule_id: str,
                        *,
                        schedule: Optional[Schedule] = None) -> Schedule:
        """Update dashboard schedule.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param schedule_id: str
          UUID identifying the schedule.
        :param schedule: :class:`Schedule` (optional)
        
        :returns: :class:`Schedule`
        """
        body = schedule.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PUT',
                           f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}',
                           body=body,
                           headers=headers)
        return Schedule.from_dict(res)

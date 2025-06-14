Dashboards
==========

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.dashboards`` module.

.. py:currentmodule:: databricks.sdk.service.dashboards
.. autoclass:: AuthorizationDetails
   :members:
   :undoc-members:

.. autoclass:: AuthorizationDetailsGrantRule
   :members:
   :undoc-members:

.. autoclass:: CronSchedule
   :members:
   :undoc-members:

.. autoclass:: Dashboard
   :members:
   :undoc-members:

.. py:class:: DashboardView

   .. py:attribute:: DASHBOARD_VIEW_BASIC
      :value: "DASHBOARD_VIEW_BASIC"

.. autoclass:: DeleteScheduleResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteSubscriptionResponse
   :members:
   :undoc-members:

.. autoclass:: GenieAttachment
   :members:
   :undoc-members:

.. autoclass:: GenieConversation
   :members:
   :undoc-members:

.. autoclass:: GenieGenerateDownloadFullQueryResultResponse
   :members:
   :undoc-members:

.. autoclass:: GenieGetDownloadFullQueryResultResponse
   :members:
   :undoc-members:

.. autoclass:: GenieGetMessageQueryResultResponse
   :members:
   :undoc-members:

.. autoclass:: GenieListSpacesResponse
   :members:
   :undoc-members:

.. autoclass:: GenieMessage
   :members:
   :undoc-members:

.. autoclass:: GenieQueryAttachment
   :members:
   :undoc-members:

.. autoclass:: GenieResultMetadata
   :members:
   :undoc-members:

.. autoclass:: GenieSpace
   :members:
   :undoc-members:

.. autoclass:: GenieStartConversationResponse
   :members:
   :undoc-members:

.. autoclass:: GetPublishedDashboardTokenInfoResponse
   :members:
   :undoc-members:

.. py:class:: LifecycleState

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: TRASHED
      :value: "TRASHED"

.. autoclass:: ListDashboardsResponse
   :members:
   :undoc-members:

.. autoclass:: ListSchedulesResponse
   :members:
   :undoc-members:

.. autoclass:: ListSubscriptionsResponse
   :members:
   :undoc-members:

.. autoclass:: MessageError
   :members:
   :undoc-members:

.. py:class:: MessageErrorType

   .. py:attribute:: BLOCK_MULTIPLE_EXECUTIONS_EXCEPTION
      :value: "BLOCK_MULTIPLE_EXECUTIONS_EXCEPTION"

   .. py:attribute:: CHAT_COMPLETION_CLIENT_EXCEPTION
      :value: "CHAT_COMPLETION_CLIENT_EXCEPTION"

   .. py:attribute:: CHAT_COMPLETION_CLIENT_TIMEOUT_EXCEPTION
      :value: "CHAT_COMPLETION_CLIENT_TIMEOUT_EXCEPTION"

   .. py:attribute:: CHAT_COMPLETION_NETWORK_EXCEPTION
      :value: "CHAT_COMPLETION_NETWORK_EXCEPTION"

   .. py:attribute:: CONTENT_FILTER_EXCEPTION
      :value: "CONTENT_FILTER_EXCEPTION"

   .. py:attribute:: CONTEXT_EXCEEDED_EXCEPTION
      :value: "CONTEXT_EXCEEDED_EXCEPTION"

   .. py:attribute:: COULD_NOT_GET_MODEL_DEPLOYMENTS_EXCEPTION
      :value: "COULD_NOT_GET_MODEL_DEPLOYMENTS_EXCEPTION"

   .. py:attribute:: COULD_NOT_GET_UC_SCHEMA_EXCEPTION
      :value: "COULD_NOT_GET_UC_SCHEMA_EXCEPTION"

   .. py:attribute:: DEPLOYMENT_NOT_FOUND_EXCEPTION
      :value: "DEPLOYMENT_NOT_FOUND_EXCEPTION"

   .. py:attribute:: DESCRIBE_QUERY_INVALID_SQL_ERROR
      :value: "DESCRIBE_QUERY_INVALID_SQL_ERROR"

   .. py:attribute:: DESCRIBE_QUERY_TIMEOUT
      :value: "DESCRIBE_QUERY_TIMEOUT"

   .. py:attribute:: DESCRIBE_QUERY_UNEXPECTED_FAILURE
      :value: "DESCRIBE_QUERY_UNEXPECTED_FAILURE"

   .. py:attribute:: FUNCTIONS_NOT_AVAILABLE_EXCEPTION
      :value: "FUNCTIONS_NOT_AVAILABLE_EXCEPTION"

   .. py:attribute:: FUNCTION_ARGUMENTS_INVALID_EXCEPTION
      :value: "FUNCTION_ARGUMENTS_INVALID_EXCEPTION"

   .. py:attribute:: FUNCTION_ARGUMENTS_INVALID_JSON_EXCEPTION
      :value: "FUNCTION_ARGUMENTS_INVALID_JSON_EXCEPTION"

   .. py:attribute:: FUNCTION_ARGUMENTS_INVALID_TYPE_EXCEPTION
      :value: "FUNCTION_ARGUMENTS_INVALID_TYPE_EXCEPTION"

   .. py:attribute:: FUNCTION_CALL_MISSING_PARAMETER_EXCEPTION
      :value: "FUNCTION_CALL_MISSING_PARAMETER_EXCEPTION"

   .. py:attribute:: GENERATED_SQL_QUERY_TOO_LONG_EXCEPTION
      :value: "GENERATED_SQL_QUERY_TOO_LONG_EXCEPTION"

   .. py:attribute:: GENERIC_CHAT_COMPLETION_EXCEPTION
      :value: "GENERIC_CHAT_COMPLETION_EXCEPTION"

   .. py:attribute:: GENERIC_CHAT_COMPLETION_SERVICE_EXCEPTION
      :value: "GENERIC_CHAT_COMPLETION_SERVICE_EXCEPTION"

   .. py:attribute:: GENERIC_SQL_EXEC_API_CALL_EXCEPTION
      :value: "GENERIC_SQL_EXEC_API_CALL_EXCEPTION"

   .. py:attribute:: ILLEGAL_PARAMETER_DEFINITION_EXCEPTION
      :value: "ILLEGAL_PARAMETER_DEFINITION_EXCEPTION"

   .. py:attribute:: INVALID_CERTIFIED_ANSWER_FUNCTION_EXCEPTION
      :value: "INVALID_CERTIFIED_ANSWER_FUNCTION_EXCEPTION"

   .. py:attribute:: INVALID_CERTIFIED_ANSWER_IDENTIFIER_EXCEPTION
      :value: "INVALID_CERTIFIED_ANSWER_IDENTIFIER_EXCEPTION"

   .. py:attribute:: INVALID_CHAT_COMPLETION_ARGUMENTS_JSON_EXCEPTION
      :value: "INVALID_CHAT_COMPLETION_ARGUMENTS_JSON_EXCEPTION"

   .. py:attribute:: INVALID_CHAT_COMPLETION_JSON_EXCEPTION
      :value: "INVALID_CHAT_COMPLETION_JSON_EXCEPTION"

   .. py:attribute:: INVALID_COMPLETION_REQUEST_EXCEPTION
      :value: "INVALID_COMPLETION_REQUEST_EXCEPTION"

   .. py:attribute:: INVALID_FUNCTION_CALL_EXCEPTION
      :value: "INVALID_FUNCTION_CALL_EXCEPTION"

   .. py:attribute:: INVALID_SQL_MULTIPLE_DATASET_REFERENCES_EXCEPTION
      :value: "INVALID_SQL_MULTIPLE_DATASET_REFERENCES_EXCEPTION"

   .. py:attribute:: INVALID_SQL_MULTIPLE_STATEMENTS_EXCEPTION
      :value: "INVALID_SQL_MULTIPLE_STATEMENTS_EXCEPTION"

   .. py:attribute:: INVALID_SQL_UNKNOWN_TABLE_EXCEPTION
      :value: "INVALID_SQL_UNKNOWN_TABLE_EXCEPTION"

   .. py:attribute:: INVALID_TABLE_IDENTIFIER_EXCEPTION
      :value: "INVALID_TABLE_IDENTIFIER_EXCEPTION"

   .. py:attribute:: LOCAL_CONTEXT_EXCEEDED_EXCEPTION
      :value: "LOCAL_CONTEXT_EXCEEDED_EXCEPTION"

   .. py:attribute:: MESSAGE_CANCELLED_WHILE_EXECUTING_EXCEPTION
      :value: "MESSAGE_CANCELLED_WHILE_EXECUTING_EXCEPTION"

   .. py:attribute:: MESSAGE_DELETED_WHILE_EXECUTING_EXCEPTION
      :value: "MESSAGE_DELETED_WHILE_EXECUTING_EXCEPTION"

   .. py:attribute:: MESSAGE_UPDATED_WHILE_EXECUTING_EXCEPTION
      :value: "MESSAGE_UPDATED_WHILE_EXECUTING_EXCEPTION"

   .. py:attribute:: MISSING_SQL_QUERY_EXCEPTION
      :value: "MISSING_SQL_QUERY_EXCEPTION"

   .. py:attribute:: NO_DEPLOYMENTS_AVAILABLE_TO_WORKSPACE
      :value: "NO_DEPLOYMENTS_AVAILABLE_TO_WORKSPACE"

   .. py:attribute:: NO_QUERY_TO_VISUALIZE_EXCEPTION
      :value: "NO_QUERY_TO_VISUALIZE_EXCEPTION"

   .. py:attribute:: NO_TABLES_TO_QUERY_EXCEPTION
      :value: "NO_TABLES_TO_QUERY_EXCEPTION"

   .. py:attribute:: RATE_LIMIT_EXCEEDED_GENERIC_EXCEPTION
      :value: "RATE_LIMIT_EXCEEDED_GENERIC_EXCEPTION"

   .. py:attribute:: RATE_LIMIT_EXCEEDED_SPECIFIED_WAIT_EXCEPTION
      :value: "RATE_LIMIT_EXCEEDED_SPECIFIED_WAIT_EXCEPTION"

   .. py:attribute:: REPLY_PROCESS_TIMEOUT_EXCEPTION
      :value: "REPLY_PROCESS_TIMEOUT_EXCEPTION"

   .. py:attribute:: RETRYABLE_PROCESSING_EXCEPTION
      :value: "RETRYABLE_PROCESSING_EXCEPTION"

   .. py:attribute:: SQL_EXECUTION_EXCEPTION
      :value: "SQL_EXECUTION_EXCEPTION"

   .. py:attribute:: STOP_PROCESS_DUE_TO_AUTO_REGENERATE
      :value: "STOP_PROCESS_DUE_TO_AUTO_REGENERATE"

   .. py:attribute:: TABLES_MISSING_EXCEPTION
      :value: "TABLES_MISSING_EXCEPTION"

   .. py:attribute:: TOO_MANY_CERTIFIED_ANSWERS_EXCEPTION
      :value: "TOO_MANY_CERTIFIED_ANSWERS_EXCEPTION"

   .. py:attribute:: TOO_MANY_TABLES_EXCEPTION
      :value: "TOO_MANY_TABLES_EXCEPTION"

   .. py:attribute:: UNEXPECTED_REPLY_PROCESS_EXCEPTION
      :value: "UNEXPECTED_REPLY_PROCESS_EXCEPTION"

   .. py:attribute:: UNKNOWN_AI_MODEL
      :value: "UNKNOWN_AI_MODEL"

   .. py:attribute:: WAREHOUSE_ACCESS_MISSING_EXCEPTION
      :value: "WAREHOUSE_ACCESS_MISSING_EXCEPTION"

   .. py:attribute:: WAREHOUSE_NOT_FOUND_EXCEPTION
      :value: "WAREHOUSE_NOT_FOUND_EXCEPTION"

.. py:class:: MessageStatus

   MessageStatus. The possible values are: * `FETCHING_METADATA`: Fetching metadata from the data sources. * `FILTERING_CONTEXT`: Running smart context step to determine relevant context. * `ASKING_AI`: Waiting for the LLM to respond to the user's question. * `PENDING_WAREHOUSE`: Waiting for warehouse before the SQL query can start executing. * `EXECUTING_QUERY`: Executing a generated SQL query. Get the SQL query result by calling [getMessageAttachmentQueryResult](:method:genie/getMessageAttachmentQueryResult) API. * `FAILED`: The response generation or query execution failed. See `error` field. * `COMPLETED`: Message processing is completed. Results are in the `attachments` field. Get the SQL query result by calling [getMessageAttachmentQueryResult](:method:genie/getMessageAttachmentQueryResult) API. * `SUBMITTED`: Message has been submitted. * `QUERY_RESULT_EXPIRED`: SQL result is not available anymore. The user needs to rerun the query. Rerun the SQL query result by calling [executeMessageAttachmentQuery](:method:genie/executeMessageAttachmentQuery) API. * `CANCELLED`: Message has been cancelled.

   .. py:attribute:: ASKING_AI
      :value: "ASKING_AI"

   .. py:attribute:: CANCELLED
      :value: "CANCELLED"

   .. py:attribute:: COMPLETED
      :value: "COMPLETED"

   .. py:attribute:: EXECUTING_QUERY
      :value: "EXECUTING_QUERY"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: FETCHING_METADATA
      :value: "FETCHING_METADATA"

   .. py:attribute:: FILTERING_CONTEXT
      :value: "FILTERING_CONTEXT"

   .. py:attribute:: PENDING_WAREHOUSE
      :value: "PENDING_WAREHOUSE"

   .. py:attribute:: QUERY_RESULT_EXPIRED
      :value: "QUERY_RESULT_EXPIRED"

   .. py:attribute:: SUBMITTED
      :value: "SUBMITTED"

.. autoclass:: PublishedDashboard
   :members:
   :undoc-members:

.. autoclass:: Result
   :members:
   :undoc-members:

.. autoclass:: Schedule
   :members:
   :undoc-members:

.. py:class:: SchedulePauseStatus

   .. py:attribute:: PAUSED
      :value: "PAUSED"

   .. py:attribute:: UNPAUSED
      :value: "UNPAUSED"

.. autoclass:: Subscriber
   :members:
   :undoc-members:

.. autoclass:: Subscription
   :members:
   :undoc-members:

.. autoclass:: SubscriptionSubscriberDestination
   :members:
   :undoc-members:

.. autoclass:: SubscriptionSubscriberUser
   :members:
   :undoc-members:

.. autoclass:: TextAttachment
   :members:
   :undoc-members:

.. autoclass:: TrashDashboardResponse
   :members:
   :undoc-members:

.. autoclass:: UnpublishDashboardResponse
   :members:
   :undoc-members:

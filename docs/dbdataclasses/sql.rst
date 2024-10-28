Databricks SQL
==============

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.sql`` module.

.. py:currentmodule:: databricks.sdk.service.sql
.. autoclass:: AccessControl
   :members:
   :undoc-members:

.. autoclass:: Alert
   :members:
   :undoc-members:

.. autoclass:: AlertCondition
   :members:
   :undoc-members:

.. autoclass:: AlertConditionOperand
   :members:
   :undoc-members:

.. autoclass:: AlertConditionThreshold
   :members:
   :undoc-members:

.. autoclass:: AlertOperandColumn
   :members:
   :undoc-members:

.. autoclass:: AlertOperandValue
   :members:
   :undoc-members:

.. py:class:: AlertOperator

   .. py:attribute:: EQUAL
      :value: "EQUAL"

   .. py:attribute:: GREATER_THAN
      :value: "GREATER_THAN"

   .. py:attribute:: GREATER_THAN_OR_EQUAL
      :value: "GREATER_THAN_OR_EQUAL"

   .. py:attribute:: IS_NULL
      :value: "IS_NULL"

   .. py:attribute:: LESS_THAN
      :value: "LESS_THAN"

   .. py:attribute:: LESS_THAN_OR_EQUAL
      :value: "LESS_THAN_OR_EQUAL"

   .. py:attribute:: NOT_EQUAL
      :value: "NOT_EQUAL"

.. autoclass:: AlertOptions
   :members:
   :undoc-members:

.. py:class:: AlertOptionsEmptyResultState

   State that alert evaluates to when query result is empty.

   .. py:attribute:: OK
      :value: "OK"

   .. py:attribute:: TRIGGERED
      :value: "TRIGGERED"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

.. autoclass:: AlertQuery
   :members:
   :undoc-members:

.. py:class:: AlertState

   .. py:attribute:: OK
      :value: "OK"

   .. py:attribute:: TRIGGERED
      :value: "TRIGGERED"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

.. autoclass:: BaseChunkInfo
   :members:
   :undoc-members:

.. autoclass:: CancelExecutionResponse
   :members:
   :undoc-members:

.. autoclass:: Channel
   :members:
   :undoc-members:

.. autoclass:: ChannelInfo
   :members:
   :undoc-members:

.. py:class:: ChannelName

   .. py:attribute:: CHANNEL_NAME_CURRENT
      :value: "CHANNEL_NAME_CURRENT"

   .. py:attribute:: CHANNEL_NAME_CUSTOM
      :value: "CHANNEL_NAME_CUSTOM"

   .. py:attribute:: CHANNEL_NAME_PREVIEW
      :value: "CHANNEL_NAME_PREVIEW"

   .. py:attribute:: CHANNEL_NAME_UNSPECIFIED
      :value: "CHANNEL_NAME_UNSPECIFIED"

.. autoclass:: ColumnInfo
   :members:
   :undoc-members:

.. py:class:: ColumnInfoTypeName

   The name of the base data type. This doesn't include details for complex types such as STRUCT, MAP or ARRAY.

   .. py:attribute:: ARRAY
      :value: "ARRAY"

   .. py:attribute:: BINARY
      :value: "BINARY"

   .. py:attribute:: BOOLEAN
      :value: "BOOLEAN"

   .. py:attribute:: BYTE
      :value: "BYTE"

   .. py:attribute:: CHAR
      :value: "CHAR"

   .. py:attribute:: DATE
      :value: "DATE"

   .. py:attribute:: DECIMAL
      :value: "DECIMAL"

   .. py:attribute:: DOUBLE
      :value: "DOUBLE"

   .. py:attribute:: FLOAT
      :value: "FLOAT"

   .. py:attribute:: INT
      :value: "INT"

   .. py:attribute:: INTERVAL
      :value: "INTERVAL"

   .. py:attribute:: LONG
      :value: "LONG"

   .. py:attribute:: MAP
      :value: "MAP"

   .. py:attribute:: NULL
      :value: "NULL"

   .. py:attribute:: SHORT
      :value: "SHORT"

   .. py:attribute:: STRING
      :value: "STRING"

   .. py:attribute:: STRUCT
      :value: "STRUCT"

   .. py:attribute:: TIMESTAMP
      :value: "TIMESTAMP"

   .. py:attribute:: USER_DEFINED_TYPE
      :value: "USER_DEFINED_TYPE"

.. autoclass:: CreateAlert
   :members:
   :undoc-members:

.. autoclass:: CreateAlertRequest
   :members:
   :undoc-members:

.. autoclass:: CreateAlertRequestAlert
   :members:
   :undoc-members:

.. autoclass:: CreateQueryRequest
   :members:
   :undoc-members:

.. autoclass:: CreateQueryRequestQuery
   :members:
   :undoc-members:

.. autoclass:: CreateVisualizationRequest
   :members:
   :undoc-members:

.. autoclass:: CreateVisualizationRequestVisualization
   :members:
   :undoc-members:

.. autoclass:: CreateWarehouseRequest
   :members:
   :undoc-members:

.. py:class:: CreateWarehouseRequestWarehouseType

   Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and also set the field `enable_serverless_compute` to `true`.

   .. py:attribute:: CLASSIC
      :value: "CLASSIC"

   .. py:attribute:: PRO
      :value: "PRO"

   .. py:attribute:: TYPE_UNSPECIFIED
      :value: "TYPE_UNSPECIFIED"

.. autoclass:: CreateWarehouseResponse
   :members:
   :undoc-members:

.. autoclass:: CreateWidget
   :members:
   :undoc-members:

.. autoclass:: Dashboard
   :members:
   :undoc-members:

.. autoclass:: DashboardEditContent
   :members:
   :undoc-members:

.. autoclass:: DashboardOptions
   :members:
   :undoc-members:

.. autoclass:: DashboardPostContent
   :members:
   :undoc-members:

.. autoclass:: DataSource
   :members:
   :undoc-members:

.. py:class:: DatePrecision

   .. py:attribute:: DAY_PRECISION
      :value: "DAY_PRECISION"

   .. py:attribute:: MINUTE_PRECISION
      :value: "MINUTE_PRECISION"

   .. py:attribute:: SECOND_PRECISION
      :value: "SECOND_PRECISION"

.. autoclass:: DateRange
   :members:
   :undoc-members:

.. autoclass:: DateRangeValue
   :members:
   :undoc-members:

.. py:class:: DateRangeValueDynamicDateRange

   .. py:attribute:: LAST_12_MONTHS
      :value: "LAST_12_MONTHS"

   .. py:attribute:: LAST_14_DAYS
      :value: "LAST_14_DAYS"

   .. py:attribute:: LAST_24_HOURS
      :value: "LAST_24_HOURS"

   .. py:attribute:: LAST_30_DAYS
      :value: "LAST_30_DAYS"

   .. py:attribute:: LAST_60_DAYS
      :value: "LAST_60_DAYS"

   .. py:attribute:: LAST_7_DAYS
      :value: "LAST_7_DAYS"

   .. py:attribute:: LAST_8_HOURS
      :value: "LAST_8_HOURS"

   .. py:attribute:: LAST_90_DAYS
      :value: "LAST_90_DAYS"

   .. py:attribute:: LAST_HOUR
      :value: "LAST_HOUR"

   .. py:attribute:: LAST_MONTH
      :value: "LAST_MONTH"

   .. py:attribute:: LAST_WEEK
      :value: "LAST_WEEK"

   .. py:attribute:: LAST_YEAR
      :value: "LAST_YEAR"

   .. py:attribute:: THIS_MONTH
      :value: "THIS_MONTH"

   .. py:attribute:: THIS_WEEK
      :value: "THIS_WEEK"

   .. py:attribute:: THIS_YEAR
      :value: "THIS_YEAR"

   .. py:attribute:: TODAY
      :value: "TODAY"

   .. py:attribute:: YESTERDAY
      :value: "YESTERDAY"

.. autoclass:: DateValue
   :members:
   :undoc-members:

.. py:class:: DateValueDynamicDate

   .. py:attribute:: NOW
      :value: "NOW"

   .. py:attribute:: YESTERDAY
      :value: "YESTERDAY"

.. autoclass:: DeleteResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteWarehouseResponse
   :members:
   :undoc-members:

.. py:class:: Disposition

   .. py:attribute:: EXTERNAL_LINKS
      :value: "EXTERNAL_LINKS"

   .. py:attribute:: INLINE
      :value: "INLINE"

.. autoclass:: EditAlert
   :members:
   :undoc-members:

.. autoclass:: EditWarehouseRequest
   :members:
   :undoc-members:

.. py:class:: EditWarehouseRequestWarehouseType

   Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and also set the field `enable_serverless_compute` to `true`.

   .. py:attribute:: CLASSIC
      :value: "CLASSIC"

   .. py:attribute:: PRO
      :value: "PRO"

   .. py:attribute:: TYPE_UNSPECIFIED
      :value: "TYPE_UNSPECIFIED"

.. autoclass:: EditWarehouseResponse
   :members:
   :undoc-members:

.. autoclass:: Empty
   :members:
   :undoc-members:

.. autoclass:: EndpointConfPair
   :members:
   :undoc-members:

.. autoclass:: EndpointHealth
   :members:
   :undoc-members:

.. autoclass:: EndpointInfo
   :members:
   :undoc-members:

.. py:class:: EndpointInfoWarehouseType

   Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and also set the field `enable_serverless_compute` to `true`.

   .. py:attribute:: CLASSIC
      :value: "CLASSIC"

   .. py:attribute:: PRO
      :value: "PRO"

   .. py:attribute:: TYPE_UNSPECIFIED
      :value: "TYPE_UNSPECIFIED"

.. autoclass:: EndpointTagPair
   :members:
   :undoc-members:

.. autoclass:: EndpointTags
   :members:
   :undoc-members:

.. autoclass:: EnumValue
   :members:
   :undoc-members:

.. autoclass:: ExecuteStatementRequest
   :members:
   :undoc-members:

.. py:class:: ExecuteStatementRequestOnWaitTimeout

   When `wait_timeout > 0s`, the call will block up to the specified time. If the statement execution doesn't finish within this time, `on_wait_timeout` determines whether the execution should continue or be canceled. When set to `CONTINUE`, the statement execution continues asynchronously and the call returns a statement ID which can be used for polling with :method:statementexecution/getStatement. When set to `CANCEL`, the statement execution is canceled and the call returns with a `CANCELED` state.

   .. py:attribute:: CANCEL
      :value: "CANCEL"

   .. py:attribute:: CONTINUE
      :value: "CONTINUE"

.. autoclass:: ExternalLink
   :members:
   :undoc-members:

.. py:class:: Format

   .. py:attribute:: ARROW_STREAM
      :value: "ARROW_STREAM"

   .. py:attribute:: CSV
      :value: "CSV"

   .. py:attribute:: JSON_ARRAY
      :value: "JSON_ARRAY"

.. autoclass:: GetResponse
   :members:
   :undoc-members:

.. autoclass:: GetWarehousePermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GetWarehouseResponse
   :members:
   :undoc-members:

.. py:class:: GetWarehouseResponseWarehouseType

   Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and also set the field `enable_serverless_compute` to `true`.

   .. py:attribute:: CLASSIC
      :value: "CLASSIC"

   .. py:attribute:: PRO
      :value: "PRO"

   .. py:attribute:: TYPE_UNSPECIFIED
      :value: "TYPE_UNSPECIFIED"

.. autoclass:: GetWorkspaceWarehouseConfigResponse
   :members:
   :undoc-members:

.. py:class:: GetWorkspaceWarehouseConfigResponseSecurityPolicy

   Security policy for warehouses

   .. py:attribute:: DATA_ACCESS_CONTROL
      :value: "DATA_ACCESS_CONTROL"

   .. py:attribute:: NONE
      :value: "NONE"

   .. py:attribute:: PASSTHROUGH
      :value: "PASSTHROUGH"

.. autoclass:: LegacyAlert
   :members:
   :undoc-members:

.. py:class:: LegacyAlertState

   State of the alert. Possible values are: `unknown` (yet to be evaluated), `triggered` (evaluated and fulfilled trigger conditions), or `ok` (evaluated and did not fulfill trigger conditions).

   .. py:attribute:: OK
      :value: "OK"

   .. py:attribute:: TRIGGERED
      :value: "TRIGGERED"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

.. autoclass:: LegacyQuery
   :members:
   :undoc-members:

.. autoclass:: LegacyVisualization
   :members:
   :undoc-members:

.. py:class:: LifecycleState

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: TRASHED
      :value: "TRASHED"

.. autoclass:: ListAlertsResponse
   :members:
   :undoc-members:

.. autoclass:: ListAlertsResponseAlert
   :members:
   :undoc-members:

.. py:class:: ListOrder

   .. py:attribute:: CREATED_AT
      :value: "CREATED_AT"

   .. py:attribute:: NAME
      :value: "NAME"

.. autoclass:: ListQueriesResponse
   :members:
   :undoc-members:

.. autoclass:: ListQueryObjectsResponse
   :members:
   :undoc-members:

.. autoclass:: ListQueryObjectsResponseQuery
   :members:
   :undoc-members:

.. autoclass:: ListResponse
   :members:
   :undoc-members:

.. autoclass:: ListVisualizationsForQueryResponse
   :members:
   :undoc-members:

.. autoclass:: ListWarehousesResponse
   :members:
   :undoc-members:

.. autoclass:: MultiValuesOptions
   :members:
   :undoc-members:

.. autoclass:: NumericValue
   :members:
   :undoc-members:

.. py:class:: ObjectType

   A singular noun object type.

   .. py:attribute:: ALERT
      :value: "ALERT"

   .. py:attribute:: DASHBOARD
      :value: "DASHBOARD"

   .. py:attribute:: DATA_SOURCE
      :value: "DATA_SOURCE"

   .. py:attribute:: QUERY
      :value: "QUERY"

.. py:class:: ObjectTypePlural

   Always a plural of the object type.

   .. py:attribute:: ALERTS
      :value: "ALERTS"

   .. py:attribute:: DASHBOARDS
      :value: "DASHBOARDS"

   .. py:attribute:: DATA_SOURCES
      :value: "DATA_SOURCES"

   .. py:attribute:: QUERIES
      :value: "QUERIES"

.. autoclass:: OdbcParams
   :members:
   :undoc-members:

.. py:class:: OwnableObjectType

   The singular form of the type of object which can be owned.

   .. py:attribute:: ALERT
      :value: "ALERT"

   .. py:attribute:: DASHBOARD
      :value: "DASHBOARD"

   .. py:attribute:: QUERY
      :value: "QUERY"

.. autoclass:: Parameter
   :members:
   :undoc-members:

.. py:class:: ParameterType

   Parameters can have several different types.

   .. py:attribute:: DATETIME
      :value: "DATETIME"

   .. py:attribute:: ENUM
      :value: "ENUM"

   .. py:attribute:: NUMBER
      :value: "NUMBER"

   .. py:attribute:: QUERY
      :value: "QUERY"

   .. py:attribute:: TEXT
      :value: "TEXT"

.. py:class:: PermissionLevel

   * `CAN_VIEW`: Can view the query * `CAN_RUN`: Can run the query * `CAN_EDIT`: Can edit the query * `CAN_MANAGE`: Can manage the query

   .. py:attribute:: CAN_EDIT
      :value: "CAN_EDIT"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_RUN
      :value: "CAN_RUN"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

.. py:class:: PlansState

   Possible Reasons for which we have not saved plans in the database

   .. py:attribute:: EMPTY
      :value: "EMPTY"

   .. py:attribute:: EXISTS
      :value: "EXISTS"

   .. py:attribute:: IGNORED_LARGE_PLANS_SIZE
      :value: "IGNORED_LARGE_PLANS_SIZE"

   .. py:attribute:: IGNORED_SMALL_DURATION
      :value: "IGNORED_SMALL_DURATION"

   .. py:attribute:: IGNORED_SPARK_PLAN_TYPE
      :value: "IGNORED_SPARK_PLAN_TYPE"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

.. autoclass:: Query
   :members:
   :undoc-members:

.. autoclass:: QueryBackedValue
   :members:
   :undoc-members:

.. autoclass:: QueryEditContent
   :members:
   :undoc-members:

.. autoclass:: QueryFilter
   :members:
   :undoc-members:

.. autoclass:: QueryInfo
   :members:
   :undoc-members:

.. autoclass:: QueryList
   :members:
   :undoc-members:

.. autoclass:: QueryMetrics
   :members:
   :undoc-members:

.. autoclass:: QueryOptions
   :members:
   :undoc-members:

.. autoclass:: QueryParameter
   :members:
   :undoc-members:

.. autoclass:: QueryPostContent
   :members:
   :undoc-members:

.. py:class:: QueryStatementType

   .. py:attribute:: ALTER
      :value: "ALTER"

   .. py:attribute:: ANALYZE
      :value: "ANALYZE"

   .. py:attribute:: COPY
      :value: "COPY"

   .. py:attribute:: CREATE
      :value: "CREATE"

   .. py:attribute:: DELETE
      :value: "DELETE"

   .. py:attribute:: DESCRIBE
      :value: "DESCRIBE"

   .. py:attribute:: DROP
      :value: "DROP"

   .. py:attribute:: EXPLAIN
      :value: "EXPLAIN"

   .. py:attribute:: GRANT
      :value: "GRANT"

   .. py:attribute:: INSERT
      :value: "INSERT"

   .. py:attribute:: MERGE
      :value: "MERGE"

   .. py:attribute:: OPTIMIZE
      :value: "OPTIMIZE"

   .. py:attribute:: OTHER
      :value: "OTHER"

   .. py:attribute:: REFRESH
      :value: "REFRESH"

   .. py:attribute:: REPLACE
      :value: "REPLACE"

   .. py:attribute:: REVOKE
      :value: "REVOKE"

   .. py:attribute:: SELECT
      :value: "SELECT"

   .. py:attribute:: SET
      :value: "SET"

   .. py:attribute:: SHOW
      :value: "SHOW"

   .. py:attribute:: TRUNCATE
      :value: "TRUNCATE"

   .. py:attribute:: UPDATE
      :value: "UPDATE"

   .. py:attribute:: USE
      :value: "USE"

.. py:class:: QueryStatus

   Statuses which are also used by OperationStatus in runtime

   .. py:attribute:: CANCELED
      :value: "CANCELED"

   .. py:attribute:: COMPILED
      :value: "COMPILED"

   .. py:attribute:: COMPILING
      :value: "COMPILING"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: FINISHED
      :value: "FINISHED"

   .. py:attribute:: QUEUED
      :value: "QUEUED"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: STARTED
      :value: "STARTED"

.. autoclass:: RepeatedEndpointConfPairs
   :members:
   :undoc-members:

.. autoclass:: RestoreResponse
   :members:
   :undoc-members:

.. autoclass:: ResultData
   :members:
   :undoc-members:

.. autoclass:: ResultManifest
   :members:
   :undoc-members:

.. autoclass:: ResultSchema
   :members:
   :undoc-members:

.. py:class:: RunAsMode

   .. py:attribute:: OWNER
      :value: "OWNER"

   .. py:attribute:: VIEWER
      :value: "VIEWER"

.. py:class:: RunAsRole

   Sets the **Run as** role for the object. Must be set to one of `"viewer"` (signifying "run as viewer" behavior) or `"owner"` (signifying "run as owner" behavior)

   .. py:attribute:: OWNER
      :value: "OWNER"

   .. py:attribute:: VIEWER
      :value: "VIEWER"

.. autoclass:: ServiceError
   :members:
   :undoc-members:

.. py:class:: ServiceErrorCode

   .. py:attribute:: ABORTED
      :value: "ABORTED"

   .. py:attribute:: ALREADY_EXISTS
      :value: "ALREADY_EXISTS"

   .. py:attribute:: BAD_REQUEST
      :value: "BAD_REQUEST"

   .. py:attribute:: CANCELLED
      :value: "CANCELLED"

   .. py:attribute:: DEADLINE_EXCEEDED
      :value: "DEADLINE_EXCEEDED"

   .. py:attribute:: INTERNAL_ERROR
      :value: "INTERNAL_ERROR"

   .. py:attribute:: IO_ERROR
      :value: "IO_ERROR"

   .. py:attribute:: NOT_FOUND
      :value: "NOT_FOUND"

   .. py:attribute:: RESOURCE_EXHAUSTED
      :value: "RESOURCE_EXHAUSTED"

   .. py:attribute:: SERVICE_UNDER_MAINTENANCE
      :value: "SERVICE_UNDER_MAINTENANCE"

   .. py:attribute:: TEMPORARILY_UNAVAILABLE
      :value: "TEMPORARILY_UNAVAILABLE"

   .. py:attribute:: UNAUTHENTICATED
      :value: "UNAUTHENTICATED"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

   .. py:attribute:: WORKSPACE_TEMPORARILY_UNAVAILABLE
      :value: "WORKSPACE_TEMPORARILY_UNAVAILABLE"

.. autoclass:: SetResponse
   :members:
   :undoc-members:

.. autoclass:: SetWorkspaceWarehouseConfigRequest
   :members:
   :undoc-members:

.. py:class:: SetWorkspaceWarehouseConfigRequestSecurityPolicy

   Security policy for warehouses

   .. py:attribute:: DATA_ACCESS_CONTROL
      :value: "DATA_ACCESS_CONTROL"

   .. py:attribute:: NONE
      :value: "NONE"

   .. py:attribute:: PASSTHROUGH
      :value: "PASSTHROUGH"

.. autoclass:: SetWorkspaceWarehouseConfigResponse
   :members:
   :undoc-members:

.. py:class:: SpotInstancePolicy

   Configurations whether the warehouse should use spot instances.

   .. py:attribute:: COST_OPTIMIZED
      :value: "COST_OPTIMIZED"

   .. py:attribute:: POLICY_UNSPECIFIED
      :value: "POLICY_UNSPECIFIED"

   .. py:attribute:: RELIABILITY_OPTIMIZED
      :value: "RELIABILITY_OPTIMIZED"

.. autoclass:: StartWarehouseResponse
   :members:
   :undoc-members:

.. py:class:: State

   State of the warehouse

   .. py:attribute:: DELETED
      :value: "DELETED"

   .. py:attribute:: DELETING
      :value: "DELETING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: STARTING
      :value: "STARTING"

   .. py:attribute:: STOPPED
      :value: "STOPPED"

   .. py:attribute:: STOPPING
      :value: "STOPPING"

.. autoclass:: StatementParameterListItem
   :members:
   :undoc-members:

.. autoclass:: StatementResponse
   :members:
   :undoc-members:

.. py:class:: StatementState

   Statement execution state: - `PENDING`: waiting for warehouse - `RUNNING`: running - `SUCCEEDED`: execution was successful, result data available for fetch - `FAILED`: execution failed; reason for failure described in accomanying error message - `CANCELED`: user canceled; can come from explicit cancel call, or timeout with `on_wait_timeout=CANCEL` - `CLOSED`: execution successful, and statement closed; result no longer available for fetch

   .. py:attribute:: CANCELED
      :value: "CANCELED"

   .. py:attribute:: CLOSED
      :value: "CLOSED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SUCCEEDED
      :value: "SUCCEEDED"

.. autoclass:: StatementStatus
   :members:
   :undoc-members:

.. py:class:: Status

   Health status of the warehouse.

   .. py:attribute:: DEGRADED
      :value: "DEGRADED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: HEALTHY
      :value: "HEALTHY"

   .. py:attribute:: STATUS_UNSPECIFIED
      :value: "STATUS_UNSPECIFIED"

.. autoclass:: StopWarehouseResponse
   :members:
   :undoc-members:

.. autoclass:: Success
   :members:
   :undoc-members:

.. py:class:: SuccessMessage

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

.. autoclass:: TerminationReason
   :members:
   :undoc-members:

.. py:class:: TerminationReasonCode

   status code indicating why the cluster was terminated

   .. py:attribute:: ABUSE_DETECTED
      :value: "ABUSE_DETECTED"

   .. py:attribute:: ATTACH_PROJECT_FAILURE
      :value: "ATTACH_PROJECT_FAILURE"

   .. py:attribute:: AWS_AUTHORIZATION_FAILURE
      :value: "AWS_AUTHORIZATION_FAILURE"

   .. py:attribute:: AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE
      :value: "AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE"

   .. py:attribute:: AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE
      :value: "AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE"

   .. py:attribute:: AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE
      :value: "AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE"

   .. py:attribute:: AWS_REQUEST_LIMIT_EXCEEDED
      :value: "AWS_REQUEST_LIMIT_EXCEEDED"

   .. py:attribute:: AWS_UNSUPPORTED_FAILURE
      :value: "AWS_UNSUPPORTED_FAILURE"

   .. py:attribute:: AZURE_BYOK_KEY_PERMISSION_FAILURE
      :value: "AZURE_BYOK_KEY_PERMISSION_FAILURE"

   .. py:attribute:: AZURE_EPHEMERAL_DISK_FAILURE
      :value: "AZURE_EPHEMERAL_DISK_FAILURE"

   .. py:attribute:: AZURE_INVALID_DEPLOYMENT_TEMPLATE
      :value: "AZURE_INVALID_DEPLOYMENT_TEMPLATE"

   .. py:attribute:: AZURE_OPERATION_NOT_ALLOWED_EXCEPTION
      :value: "AZURE_OPERATION_NOT_ALLOWED_EXCEPTION"

   .. py:attribute:: AZURE_QUOTA_EXCEEDED_EXCEPTION
      :value: "AZURE_QUOTA_EXCEEDED_EXCEPTION"

   .. py:attribute:: AZURE_RESOURCE_MANAGER_THROTTLING
      :value: "AZURE_RESOURCE_MANAGER_THROTTLING"

   .. py:attribute:: AZURE_RESOURCE_PROVIDER_THROTTLING
      :value: "AZURE_RESOURCE_PROVIDER_THROTTLING"

   .. py:attribute:: AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE
      :value: "AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE"

   .. py:attribute:: AZURE_VM_EXTENSION_FAILURE
      :value: "AZURE_VM_EXTENSION_FAILURE"

   .. py:attribute:: AZURE_VNET_CONFIGURATION_FAILURE
      :value: "AZURE_VNET_CONFIGURATION_FAILURE"

   .. py:attribute:: BOOTSTRAP_TIMEOUT
      :value: "BOOTSTRAP_TIMEOUT"

   .. py:attribute:: BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION
      :value: "BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION"

   .. py:attribute:: CLOUD_PROVIDER_DISK_SETUP_FAILURE
      :value: "CLOUD_PROVIDER_DISK_SETUP_FAILURE"

   .. py:attribute:: CLOUD_PROVIDER_LAUNCH_FAILURE
      :value: "CLOUD_PROVIDER_LAUNCH_FAILURE"

   .. py:attribute:: CLOUD_PROVIDER_RESOURCE_STOCKOUT
      :value: "CLOUD_PROVIDER_RESOURCE_STOCKOUT"

   .. py:attribute:: CLOUD_PROVIDER_SHUTDOWN
      :value: "CLOUD_PROVIDER_SHUTDOWN"

   .. py:attribute:: COMMUNICATION_LOST
      :value: "COMMUNICATION_LOST"

   .. py:attribute:: CONTAINER_LAUNCH_FAILURE
      :value: "CONTAINER_LAUNCH_FAILURE"

   .. py:attribute:: CONTROL_PLANE_REQUEST_FAILURE
      :value: "CONTROL_PLANE_REQUEST_FAILURE"

   .. py:attribute:: DATABASE_CONNECTION_FAILURE
      :value: "DATABASE_CONNECTION_FAILURE"

   .. py:attribute:: DBFS_COMPONENT_UNHEALTHY
      :value: "DBFS_COMPONENT_UNHEALTHY"

   .. py:attribute:: DOCKER_IMAGE_PULL_FAILURE
      :value: "DOCKER_IMAGE_PULL_FAILURE"

   .. py:attribute:: DRIVER_UNREACHABLE
      :value: "DRIVER_UNREACHABLE"

   .. py:attribute:: DRIVER_UNRESPONSIVE
      :value: "DRIVER_UNRESPONSIVE"

   .. py:attribute:: EXECUTION_COMPONENT_UNHEALTHY
      :value: "EXECUTION_COMPONENT_UNHEALTHY"

   .. py:attribute:: GCP_QUOTA_EXCEEDED
      :value: "GCP_QUOTA_EXCEEDED"

   .. py:attribute:: GCP_SERVICE_ACCOUNT_DELETED
      :value: "GCP_SERVICE_ACCOUNT_DELETED"

   .. py:attribute:: GLOBAL_INIT_SCRIPT_FAILURE
      :value: "GLOBAL_INIT_SCRIPT_FAILURE"

   .. py:attribute:: HIVE_METASTORE_PROVISIONING_FAILURE
      :value: "HIVE_METASTORE_PROVISIONING_FAILURE"

   .. py:attribute:: IMAGE_PULL_PERMISSION_DENIED
      :value: "IMAGE_PULL_PERMISSION_DENIED"

   .. py:attribute:: INACTIVITY
      :value: "INACTIVITY"

   .. py:attribute:: INIT_SCRIPT_FAILURE
      :value: "INIT_SCRIPT_FAILURE"

   .. py:attribute:: INSTANCE_POOL_CLUSTER_FAILURE
      :value: "INSTANCE_POOL_CLUSTER_FAILURE"

   .. py:attribute:: INSTANCE_UNREACHABLE
      :value: "INSTANCE_UNREACHABLE"

   .. py:attribute:: INTERNAL_ERROR
      :value: "INTERNAL_ERROR"

   .. py:attribute:: INVALID_ARGUMENT
      :value: "INVALID_ARGUMENT"

   .. py:attribute:: INVALID_SPARK_IMAGE
      :value: "INVALID_SPARK_IMAGE"

   .. py:attribute:: IP_EXHAUSTION_FAILURE
      :value: "IP_EXHAUSTION_FAILURE"

   .. py:attribute:: JOB_FINISHED
      :value: "JOB_FINISHED"

   .. py:attribute:: K8S_AUTOSCALING_FAILURE
      :value: "K8S_AUTOSCALING_FAILURE"

   .. py:attribute:: K8S_DBR_CLUSTER_LAUNCH_TIMEOUT
      :value: "K8S_DBR_CLUSTER_LAUNCH_TIMEOUT"

   .. py:attribute:: METASTORE_COMPONENT_UNHEALTHY
      :value: "METASTORE_COMPONENT_UNHEALTHY"

   .. py:attribute:: NEPHOS_RESOURCE_MANAGEMENT
      :value: "NEPHOS_RESOURCE_MANAGEMENT"

   .. py:attribute:: NETWORK_CONFIGURATION_FAILURE
      :value: "NETWORK_CONFIGURATION_FAILURE"

   .. py:attribute:: NFS_MOUNT_FAILURE
      :value: "NFS_MOUNT_FAILURE"

   .. py:attribute:: NPIP_TUNNEL_SETUP_FAILURE
      :value: "NPIP_TUNNEL_SETUP_FAILURE"

   .. py:attribute:: NPIP_TUNNEL_TOKEN_FAILURE
      :value: "NPIP_TUNNEL_TOKEN_FAILURE"

   .. py:attribute:: REQUEST_REJECTED
      :value: "REQUEST_REJECTED"

   .. py:attribute:: REQUEST_THROTTLED
      :value: "REQUEST_THROTTLED"

   .. py:attribute:: SECRET_RESOLUTION_ERROR
      :value: "SECRET_RESOLUTION_ERROR"

   .. py:attribute:: SECURITY_DAEMON_REGISTRATION_EXCEPTION
      :value: "SECURITY_DAEMON_REGISTRATION_EXCEPTION"

   .. py:attribute:: SELF_BOOTSTRAP_FAILURE
      :value: "SELF_BOOTSTRAP_FAILURE"

   .. py:attribute:: SKIPPED_SLOW_NODES
      :value: "SKIPPED_SLOW_NODES"

   .. py:attribute:: SLOW_IMAGE_DOWNLOAD
      :value: "SLOW_IMAGE_DOWNLOAD"

   .. py:attribute:: SPARK_ERROR
      :value: "SPARK_ERROR"

   .. py:attribute:: SPARK_IMAGE_DOWNLOAD_FAILURE
      :value: "SPARK_IMAGE_DOWNLOAD_FAILURE"

   .. py:attribute:: SPARK_STARTUP_FAILURE
      :value: "SPARK_STARTUP_FAILURE"

   .. py:attribute:: SPOT_INSTANCE_TERMINATION
      :value: "SPOT_INSTANCE_TERMINATION"

   .. py:attribute:: STORAGE_DOWNLOAD_FAILURE
      :value: "STORAGE_DOWNLOAD_FAILURE"

   .. py:attribute:: STS_CLIENT_SETUP_FAILURE
      :value: "STS_CLIENT_SETUP_FAILURE"

   .. py:attribute:: SUBNET_EXHAUSTED_FAILURE
      :value: "SUBNET_EXHAUSTED_FAILURE"

   .. py:attribute:: TEMPORARILY_UNAVAILABLE
      :value: "TEMPORARILY_UNAVAILABLE"

   .. py:attribute:: TRIAL_EXPIRED
      :value: "TRIAL_EXPIRED"

   .. py:attribute:: UNEXPECTED_LAUNCH_FAILURE
      :value: "UNEXPECTED_LAUNCH_FAILURE"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

   .. py:attribute:: UNSUPPORTED_INSTANCE_TYPE
      :value: "UNSUPPORTED_INSTANCE_TYPE"

   .. py:attribute:: UPDATE_INSTANCE_PROFILE_FAILURE
      :value: "UPDATE_INSTANCE_PROFILE_FAILURE"

   .. py:attribute:: USER_REQUEST
      :value: "USER_REQUEST"

   .. py:attribute:: WORKER_SETUP_FAILURE
      :value: "WORKER_SETUP_FAILURE"

   .. py:attribute:: WORKSPACE_CANCELLED_ERROR
      :value: "WORKSPACE_CANCELLED_ERROR"

   .. py:attribute:: WORKSPACE_CONFIGURATION_ERROR
      :value: "WORKSPACE_CONFIGURATION_ERROR"

.. py:class:: TerminationReasonType

   type of the termination

   .. py:attribute:: CLIENT_ERROR
      :value: "CLIENT_ERROR"

   .. py:attribute:: CLOUD_FAILURE
      :value: "CLOUD_FAILURE"

   .. py:attribute:: SERVICE_FAULT
      :value: "SERVICE_FAULT"

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

.. autoclass:: TextValue
   :members:
   :undoc-members:

.. autoclass:: TimeRange
   :members:
   :undoc-members:

.. autoclass:: TransferOwnershipObjectId
   :members:
   :undoc-members:

.. autoclass:: UpdateAlertRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateAlertRequestAlert
   :members:
   :undoc-members:

.. autoclass:: UpdateQueryRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateQueryRequestQuery
   :members:
   :undoc-members:

.. autoclass:: UpdateResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateVisualizationRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateVisualizationRequestVisualization
   :members:
   :undoc-members:

.. autoclass:: User
   :members:
   :undoc-members:

.. autoclass:: Visualization
   :members:
   :undoc-members:

.. autoclass:: WarehouseAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: WarehouseAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: WarehousePermission
   :members:
   :undoc-members:

.. py:class:: WarehousePermissionLevel

   Permission level

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_MONITOR
      :value: "CAN_MONITOR"

   .. py:attribute:: CAN_USE
      :value: "CAN_USE"

   .. py:attribute:: IS_OWNER
      :value: "IS_OWNER"

.. autoclass:: WarehousePermissions
   :members:
   :undoc-members:

.. autoclass:: WarehousePermissionsDescription
   :members:
   :undoc-members:

.. autoclass:: WarehousePermissionsRequest
   :members:
   :undoc-members:

.. autoclass:: WarehouseTypePair
   :members:
   :undoc-members:

.. py:class:: WarehouseTypePairWarehouseType

   Warehouse type: `PRO` or `CLASSIC`.

   .. py:attribute:: CLASSIC
      :value: "CLASSIC"

   .. py:attribute:: PRO
      :value: "PRO"

   .. py:attribute:: TYPE_UNSPECIFIED
      :value: "TYPE_UNSPECIFIED"

.. autoclass:: Widget
   :members:
   :undoc-members:

.. autoclass:: WidgetOptions
   :members:
   :undoc-members:

.. autoclass:: WidgetPosition
   :members:
   :undoc-members:

Delta Live Tables
=================

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.pipelines`` module.

.. py:currentmodule:: databricks.sdk.service.pipelines
.. autoclass:: AutoFullRefreshPolicy
   :members:
   :undoc-members:

.. autoclass:: ClonePipelineResponse
   :members:
   :undoc-members:

.. autoclass:: ConnectionParameters
   :members:
   :undoc-members:

.. autoclass:: CreatePipelineResponse
   :members:
   :undoc-members:

.. autoclass:: CronTrigger
   :members:
   :undoc-members:

.. autoclass:: DataPlaneId
   :members:
   :undoc-members:

.. py:class:: DayOfWeek

   Days of week in which the window is allowed to happen. If not specified all days of the week will be used.

   .. py:attribute:: FRIDAY
      :value: "FRIDAY"

   .. py:attribute:: MONDAY
      :value: "MONDAY"

   .. py:attribute:: SATURDAY
      :value: "SATURDAY"

   .. py:attribute:: SUNDAY
      :value: "SUNDAY"

   .. py:attribute:: THURSDAY
      :value: "THURSDAY"

   .. py:attribute:: TUESDAY
      :value: "TUESDAY"

   .. py:attribute:: WEDNESDAY
      :value: "WEDNESDAY"

.. autoclass:: DeletePipelineResponse
   :members:
   :undoc-members:

.. py:class:: DeploymentKind

   The deployment method that manages the pipeline: - BUNDLE: The pipeline is managed by a Databricks Asset Bundle.

   .. py:attribute:: BUNDLE
      :value: "BUNDLE"

.. autoclass:: EditPipelineResponse
   :members:
   :undoc-members:

.. autoclass:: ErrorDetail
   :members:
   :undoc-members:

.. py:class:: EventLevel

   The severity level of the event.

   .. py:attribute:: ERROR
      :value: "ERROR"

   .. py:attribute:: INFO
      :value: "INFO"

   .. py:attribute:: METRICS
      :value: "METRICS"

   .. py:attribute:: WARN
      :value: "WARN"

.. autoclass:: EventLogSpec
   :members:
   :undoc-members:

.. autoclass:: FileLibrary
   :members:
   :undoc-members:

.. autoclass:: Filters
   :members:
   :undoc-members:

.. autoclass:: GetPipelinePermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GetPipelineResponse
   :members:
   :undoc-members:

.. py:class:: GetPipelineResponseHealth

   The health of a pipeline.

   .. py:attribute:: HEALTHY
      :value: "HEALTHY"

   .. py:attribute:: UNHEALTHY
      :value: "UNHEALTHY"

.. autoclass:: GetUpdateResponse
   :members:
   :undoc-members:

.. autoclass:: IngestionConfig
   :members:
   :undoc-members:

.. autoclass:: IngestionGatewayPipelineDefinition
   :members:
   :undoc-members:

.. autoclass:: IngestionPipelineDefinition
   :members:
   :undoc-members:

.. autoclass:: IngestionPipelineDefinitionTableSpecificConfigQueryBasedConnectorConfig
   :members:
   :undoc-members:

.. autoclass:: IngestionPipelineDefinitionWorkdayReportParameters
   :members:
   :undoc-members:

.. autoclass:: IngestionPipelineDefinitionWorkdayReportParametersQueryKeyValue
   :members:
   :undoc-members:

.. py:class:: IngestionSourceType

   .. py:attribute:: BIGQUERY
      :value: "BIGQUERY"

   .. py:attribute:: DYNAMICS365
      :value: "DYNAMICS365"

   .. py:attribute:: FOREIGN_CATALOG
      :value: "FOREIGN_CATALOG"

   .. py:attribute:: GA4_RAW_DATA
      :value: "GA4_RAW_DATA"

   .. py:attribute:: MANAGED_POSTGRESQL
      :value: "MANAGED_POSTGRESQL"

   .. py:attribute:: MYSQL
      :value: "MYSQL"

   .. py:attribute:: NETSUITE
      :value: "NETSUITE"

   .. py:attribute:: ORACLE
      :value: "ORACLE"

   .. py:attribute:: POSTGRESQL
      :value: "POSTGRESQL"

   .. py:attribute:: SALESFORCE
      :value: "SALESFORCE"

   .. py:attribute:: SERVICENOW
      :value: "SERVICENOW"

   .. py:attribute:: SHAREPOINT
      :value: "SHAREPOINT"

   .. py:attribute:: SQLSERVER
      :value: "SQLSERVER"

   .. py:attribute:: TERADATA
      :value: "TERADATA"

   .. py:attribute:: WORKDAY_RAAS
      :value: "WORKDAY_RAAS"

.. autoclass:: ListPipelineEventsResponse
   :members:
   :undoc-members:

.. autoclass:: ListPipelinesResponse
   :members:
   :undoc-members:

.. autoclass:: ListUpdatesResponse
   :members:
   :undoc-members:

.. autoclass:: ManualTrigger
   :members:
   :undoc-members:

.. py:class:: MaturityLevel

   Maturity level for EventDetails.

   .. py:attribute:: DEPRECATED
      :value: "DEPRECATED"

   .. py:attribute:: EVOLVING
      :value: "EVOLVING"

   .. py:attribute:: STABLE
      :value: "STABLE"

.. autoclass:: NotebookLibrary
   :members:
   :undoc-members:

.. autoclass:: Notifications
   :members:
   :undoc-members:

.. autoclass:: OperationTimeWindow
   :members:
   :undoc-members:

.. autoclass:: Origin
   :members:
   :undoc-members:

.. autoclass:: PathPattern
   :members:
   :undoc-members:

.. autoclass:: PipelineAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: PipelineAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: PipelineCluster
   :members:
   :undoc-members:

.. autoclass:: PipelineClusterAutoscale
   :members:
   :undoc-members:

.. py:class:: PipelineClusterAutoscaleMode

   Databricks Enhanced Autoscaling optimizes cluster utilization by automatically allocating cluster resources based on workload volume, with minimal impact to the data processing latency of your pipelines. Enhanced Autoscaling is available for `updates` clusters only. The legacy autoscaling feature is used for `maintenance` clusters.

   .. py:attribute:: ENHANCED
      :value: "ENHANCED"

   .. py:attribute:: LEGACY
      :value: "LEGACY"

.. autoclass:: PipelineDeployment
   :members:
   :undoc-members:

.. autoclass:: PipelineEvent
   :members:
   :undoc-members:

.. autoclass:: PipelineLibrary
   :members:
   :undoc-members:

.. autoclass:: PipelinePermission
   :members:
   :undoc-members:

.. py:class:: PipelinePermissionLevel

   Permission level

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_RUN
      :value: "CAN_RUN"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

   .. py:attribute:: IS_OWNER
      :value: "IS_OWNER"

.. autoclass:: PipelinePermissions
   :members:
   :undoc-members:

.. autoclass:: PipelinePermissionsDescription
   :members:
   :undoc-members:

.. autoclass:: PipelineSpec
   :members:
   :undoc-members:

.. py:class:: PipelineState

   The pipeline state.

   .. py:attribute:: DELETED
      :value: "DELETED"

   .. py:attribute:: DEPLOYING
      :value: "DEPLOYING"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: IDLE
      :value: "IDLE"

   .. py:attribute:: RECOVERING
      :value: "RECOVERING"

   .. py:attribute:: RESETTING
      :value: "RESETTING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: STARTING
      :value: "STARTING"

   .. py:attribute:: STOPPING
      :value: "STOPPING"

.. autoclass:: PipelineStateInfo
   :members:
   :undoc-members:

.. py:class:: PipelineStateInfoHealth

   The health of a pipeline.

   .. py:attribute:: HEALTHY
      :value: "HEALTHY"

   .. py:attribute:: UNHEALTHY
      :value: "UNHEALTHY"

.. autoclass:: PipelineTrigger
   :members:
   :undoc-members:

.. autoclass:: PipelinesEnvironment
   :members:
   :undoc-members:

.. autoclass:: PostgresCatalogConfig
   :members:
   :undoc-members:

.. autoclass:: PostgresSlotConfig
   :members:
   :undoc-members:

.. autoclass:: ReportSpec
   :members:
   :undoc-members:

.. autoclass:: RestartWindow
   :members:
   :undoc-members:

.. autoclass:: RewindDatasetSpec
   :members:
   :undoc-members:

.. autoclass:: RewindSpec
   :members:
   :undoc-members:

.. autoclass:: RunAs
   :members:
   :undoc-members:

.. autoclass:: SchemaSpec
   :members:
   :undoc-members:

.. autoclass:: Sequencing
   :members:
   :undoc-members:

.. autoclass:: SerializedException
   :members:
   :undoc-members:

.. autoclass:: SourceCatalogConfig
   :members:
   :undoc-members:

.. autoclass:: SourceConfig
   :members:
   :undoc-members:

.. autoclass:: StackFrame
   :members:
   :undoc-members:

.. py:class:: StartUpdateCause

   What triggered this update.

   .. py:attribute:: API_CALL
      :value: "API_CALL"

   .. py:attribute:: INFRASTRUCTURE_MAINTENANCE
      :value: "INFRASTRUCTURE_MAINTENANCE"

   .. py:attribute:: JOB_TASK
      :value: "JOB_TASK"

   .. py:attribute:: RETRY_ON_FAILURE
      :value: "RETRY_ON_FAILURE"

   .. py:attribute:: SCHEMA_CHANGE
      :value: "SCHEMA_CHANGE"

   .. py:attribute:: SERVICE_UPGRADE
      :value: "SERVICE_UPGRADE"

   .. py:attribute:: USER_ACTION
      :value: "USER_ACTION"

.. autoclass:: StartUpdateResponse
   :members:
   :undoc-members:

.. autoclass:: StopPipelineResponse
   :members:
   :undoc-members:

.. autoclass:: TableSpec
   :members:
   :undoc-members:

.. autoclass:: TableSpecificConfig
   :members:
   :undoc-members:

.. py:class:: TableSpecificConfigScdType

   The SCD type to use to ingest the table.

   .. py:attribute:: APPEND_ONLY
      :value: "APPEND_ONLY"

   .. py:attribute:: SCD_TYPE_1
      :value: "SCD_TYPE_1"

   .. py:attribute:: SCD_TYPE_2
      :value: "SCD_TYPE_2"

.. autoclass:: Truncation
   :members:
   :undoc-members:

.. autoclass:: TruncationTruncationDetail
   :members:
   :undoc-members:

.. autoclass:: UpdateInfo
   :members:
   :undoc-members:

.. py:class:: UpdateInfoCause

   What triggered this update.

   .. py:attribute:: API_CALL
      :value: "API_CALL"

   .. py:attribute:: INFRASTRUCTURE_MAINTENANCE
      :value: "INFRASTRUCTURE_MAINTENANCE"

   .. py:attribute:: JOB_TASK
      :value: "JOB_TASK"

   .. py:attribute:: RETRY_ON_FAILURE
      :value: "RETRY_ON_FAILURE"

   .. py:attribute:: SCHEMA_CHANGE
      :value: "SCHEMA_CHANGE"

   .. py:attribute:: SERVICE_UPGRADE
      :value: "SERVICE_UPGRADE"

   .. py:attribute:: USER_ACTION
      :value: "USER_ACTION"

.. py:class:: UpdateInfoState

   The update state.

   .. py:attribute:: CANCELED
      :value: "CANCELED"

   .. py:attribute:: COMPLETED
      :value: "COMPLETED"

   .. py:attribute:: CREATED
      :value: "CREATED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: INITIALIZING
      :value: "INITIALIZING"

   .. py:attribute:: QUEUED
      :value: "QUEUED"

   .. py:attribute:: RESETTING
      :value: "RESETTING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SETTING_UP_TABLES
      :value: "SETTING_UP_TABLES"

   .. py:attribute:: STOPPING
      :value: "STOPPING"

   .. py:attribute:: WAITING_FOR_RESOURCES
      :value: "WAITING_FOR_RESOURCES"

.. autoclass:: UpdateStateInfo
   :members:
   :undoc-members:

.. py:class:: UpdateStateInfoState

   The update state.

   .. py:attribute:: CANCELED
      :value: "CANCELED"

   .. py:attribute:: COMPLETED
      :value: "COMPLETED"

   .. py:attribute:: CREATED
      :value: "CREATED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: INITIALIZING
      :value: "INITIALIZING"

   .. py:attribute:: QUEUED
      :value: "QUEUED"

   .. py:attribute:: RESETTING
      :value: "RESETTING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SETTING_UP_TABLES
      :value: "SETTING_UP_TABLES"

   .. py:attribute:: STOPPING
      :value: "STOPPING"

   .. py:attribute:: WAITING_FOR_RESOURCES
      :value: "WAITING_FOR_RESOURCES"

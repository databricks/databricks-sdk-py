Jobs
====

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.jobs`` module.

.. py:currentmodule:: databricks.sdk.service.jobs
.. autoclass:: BaseJob
   :members:
   :undoc-members:

.. autoclass:: BaseRun
   :members:
   :undoc-members:

.. autoclass:: CancelAllRuns
   :members:
   :undoc-members:

.. autoclass:: CancelAllRunsResponse
   :members:
   :undoc-members:

.. autoclass:: CancelRun
   :members:
   :undoc-members:

.. autoclass:: CancelRunResponse
   :members:
   :undoc-members:

.. autoclass:: ClusterInstance
   :members:
   :undoc-members:

.. autoclass:: ClusterSpec
   :members:
   :undoc-members:

.. py:class:: Condition

   .. py:attribute:: ALL_UPDATED
      :value: "ALL_UPDATED"

   .. py:attribute:: ANY_UPDATED
      :value: "ANY_UPDATED"

.. autoclass:: ConditionTask
   :members:
   :undoc-members:

.. py:class:: ConditionTaskOp

   * `EQUAL_TO`, `NOT_EQUAL` operators perform string comparison of their operands. This means that `“12.0” == “12”` will evaluate to `false`. * `GREATER_THAN`, `GREATER_THAN_OR_EQUAL`, `LESS_THAN`, `LESS_THAN_OR_EQUAL` operators perform numeric comparison of their operands. `“12.0” >= “12”` will evaluate to `true`, `“10.0” >= “12”` will evaluate to `false`.
   The boolean comparison to task values can be implemented with operators `EQUAL_TO`, `NOT_EQUAL`. If a task value was set to a boolean value, it will be serialized to `“true”` or `“false”` for the comparison.

   .. py:attribute:: EQUAL_TO
      :value: "EQUAL_TO"

   .. py:attribute:: GREATER_THAN
      :value: "GREATER_THAN"

   .. py:attribute:: GREATER_THAN_OR_EQUAL
      :value: "GREATER_THAN_OR_EQUAL"

   .. py:attribute:: LESS_THAN
      :value: "LESS_THAN"

   .. py:attribute:: LESS_THAN_OR_EQUAL
      :value: "LESS_THAN_OR_EQUAL"

   .. py:attribute:: NOT_EQUAL
      :value: "NOT_EQUAL"

.. autoclass:: Continuous
   :members:
   :undoc-members:

.. autoclass:: CreateJob
   :members:
   :undoc-members:

.. autoclass:: CreateResponse
   :members:
   :undoc-members:

.. autoclass:: CronSchedule
   :members:
   :undoc-members:

.. autoclass:: DbtOutput
   :members:
   :undoc-members:

.. autoclass:: DbtTask
   :members:
   :undoc-members:

.. autoclass:: DeleteJob
   :members:
   :undoc-members:

.. autoclass:: DeleteResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteRun
   :members:
   :undoc-members:

.. autoclass:: DeleteRunResponse
   :members:
   :undoc-members:

.. autoclass:: EnforcePolicyComplianceForJobResponseJobClusterSettingsChange
   :members:
   :undoc-members:

.. autoclass:: EnforcePolicyComplianceRequest
   :members:
   :undoc-members:

.. autoclass:: EnforcePolicyComplianceResponse
   :members:
   :undoc-members:

.. autoclass:: ExportRunOutput
   :members:
   :undoc-members:

.. autoclass:: FileArrivalTriggerConfiguration
   :members:
   :undoc-members:

.. autoclass:: ForEachStats
   :members:
   :undoc-members:

.. autoclass:: ForEachTask
   :members:
   :undoc-members:

.. autoclass:: ForEachTaskErrorMessageStats
   :members:
   :undoc-members:

.. autoclass:: ForEachTaskTaskRunStats
   :members:
   :undoc-members:

.. py:class:: Format

   .. py:attribute:: MULTI_TASK
      :value: "MULTI_TASK"

   .. py:attribute:: SINGLE_TASK
      :value: "SINGLE_TASK"

.. autoclass:: GetJobPermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GetPolicyComplianceResponse
   :members:
   :undoc-members:

.. py:class:: GitProvider

   .. py:attribute:: AWS_CODE_COMMIT
      :value: "AWS_CODE_COMMIT"

   .. py:attribute:: AZURE_DEV_OPS_SERVICES
      :value: "AZURE_DEV_OPS_SERVICES"

   .. py:attribute:: BITBUCKET_CLOUD
      :value: "BITBUCKET_CLOUD"

   .. py:attribute:: BITBUCKET_SERVER
      :value: "BITBUCKET_SERVER"

   .. py:attribute:: GIT_HUB
      :value: "GIT_HUB"

   .. py:attribute:: GIT_HUB_ENTERPRISE
      :value: "GIT_HUB_ENTERPRISE"

   .. py:attribute:: GIT_LAB
      :value: "GIT_LAB"

   .. py:attribute:: GIT_LAB_ENTERPRISE_EDITION
      :value: "GIT_LAB_ENTERPRISE_EDITION"

.. autoclass:: GitSnapshot
   :members:
   :undoc-members:

.. autoclass:: GitSource
   :members:
   :undoc-members:

.. autoclass:: Job
   :members:
   :undoc-members:

.. autoclass:: JobAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: JobAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: JobCluster
   :members:
   :undoc-members:

.. autoclass:: JobCompliance
   :members:
   :undoc-members:

.. autoclass:: JobDeployment
   :members:
   :undoc-members:

.. py:class:: JobDeploymentKind

   * `BUNDLE`: The job is managed by Databricks Asset Bundle.

   .. py:attribute:: BUNDLE
      :value: "BUNDLE"

.. py:class:: JobEditMode

   Edit mode of the job.
   * `UI_LOCKED`: The job is in a locked UI state and cannot be modified. * `EDITABLE`: The job is in an editable state and can be modified.

   .. py:attribute:: EDITABLE
      :value: "EDITABLE"

   .. py:attribute:: UI_LOCKED
      :value: "UI_LOCKED"

.. autoclass:: JobEmailNotifications
   :members:
   :undoc-members:

.. autoclass:: JobEnvironment
   :members:
   :undoc-members:

.. autoclass:: JobNotificationSettings
   :members:
   :undoc-members:

.. autoclass:: JobParameter
   :members:
   :undoc-members:

.. autoclass:: JobParameterDefinition
   :members:
   :undoc-members:

.. autoclass:: JobPermission
   :members:
   :undoc-members:

.. py:class:: JobPermissionLevel

   Permission level

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_MANAGE_RUN
      :value: "CAN_MANAGE_RUN"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

   .. py:attribute:: IS_OWNER
      :value: "IS_OWNER"

.. autoclass:: JobPermissions
   :members:
   :undoc-members:

.. autoclass:: JobPermissionsDescription
   :members:
   :undoc-members:

.. autoclass:: JobPermissionsRequest
   :members:
   :undoc-members:

.. autoclass:: JobRunAs
   :members:
   :undoc-members:

.. autoclass:: JobSettings
   :members:
   :undoc-members:

.. autoclass:: JobSource
   :members:
   :undoc-members:

.. py:class:: JobSourceDirtyState

   Dirty state indicates the job is not fully synced with the job specification in the remote repository.
   Possible values are: * `NOT_SYNCED`: The job is not yet synced with the remote job specification. Import the remote job specification from UI to make the job fully synced. * `DISCONNECTED`: The job is temporary disconnected from the remote job specification and is allowed for live edit. Import the remote job specification again from UI to make the job fully synced.

   .. py:attribute:: DISCONNECTED
      :value: "DISCONNECTED"

   .. py:attribute:: NOT_SYNCED
      :value: "NOT_SYNCED"

.. py:class:: JobsHealthMetric

   Specifies the health metric that is being evaluated for a particular health rule.
   * `RUN_DURATION_SECONDS`: Expected total time for a run in seconds. * `STREAMING_BACKLOG_BYTES`: An estimate of the maximum bytes of data waiting to be consumed across all streams. This metric is in Private Preview. * `STREAMING_BACKLOG_RECORDS`: An estimate of the maximum offset lag across all streams. This metric is in Private Preview. * `STREAMING_BACKLOG_SECONDS`: An estimate of the maximum consumer delay across all streams. This metric is in Private Preview. * `STREAMING_BACKLOG_FILES`: An estimate of the maximum number of outstanding files across all streams. This metric is in Private Preview.

   .. py:attribute:: RUN_DURATION_SECONDS
      :value: "RUN_DURATION_SECONDS"

   .. py:attribute:: STREAMING_BACKLOG_BYTES
      :value: "STREAMING_BACKLOG_BYTES"

   .. py:attribute:: STREAMING_BACKLOG_FILES
      :value: "STREAMING_BACKLOG_FILES"

   .. py:attribute:: STREAMING_BACKLOG_RECORDS
      :value: "STREAMING_BACKLOG_RECORDS"

   .. py:attribute:: STREAMING_BACKLOG_SECONDS
      :value: "STREAMING_BACKLOG_SECONDS"

.. py:class:: JobsHealthOperator

   Specifies the operator used to compare the health metric value with the specified threshold.

   .. py:attribute:: GREATER_THAN
      :value: "GREATER_THAN"

.. autoclass:: JobsHealthRule
   :members:
   :undoc-members:

.. autoclass:: JobsHealthRules
   :members:
   :undoc-members:

.. autoclass:: ListJobComplianceForPolicyResponse
   :members:
   :undoc-members:

.. autoclass:: ListJobsResponse
   :members:
   :undoc-members:

.. autoclass:: ListRunsResponse
   :members:
   :undoc-members:

.. autoclass:: NotebookOutput
   :members:
   :undoc-members:

.. autoclass:: NotebookTask
   :members:
   :undoc-members:

.. py:class:: PauseStatus

   .. py:attribute:: PAUSED
      :value: "PAUSED"

   .. py:attribute:: UNPAUSED
      :value: "UNPAUSED"

.. autoclass:: PeriodicTriggerConfiguration
   :members:
   :undoc-members:

.. py:class:: PeriodicTriggerConfigurationTimeUnit

   .. py:attribute:: DAYS
      :value: "DAYS"

   .. py:attribute:: HOURS
      :value: "HOURS"

   .. py:attribute:: WEEKS
      :value: "WEEKS"

.. autoclass:: PipelineParams
   :members:
   :undoc-members:

.. autoclass:: PipelineTask
   :members:
   :undoc-members:

.. autoclass:: PythonWheelTask
   :members:
   :undoc-members:

.. autoclass:: QueueDetails
   :members:
   :undoc-members:

.. py:class:: QueueDetailsCodeCode

   The reason for queuing the run. * `ACTIVE_RUNS_LIMIT_REACHED`: The run was queued due to reaching the workspace limit of active task runs. * `MAX_CONCURRENT_RUNS_REACHED`: The run was queued due to reaching the per-job limit of concurrent job runs. * `ACTIVE_RUN_JOB_TASKS_LIMIT_REACHED`: The run was queued due to reaching the workspace limit of active run job tasks.

   .. py:attribute:: ACTIVE_RUNS_LIMIT_REACHED
      :value: "ACTIVE_RUNS_LIMIT_REACHED"

   .. py:attribute:: ACTIVE_RUN_JOB_TASKS_LIMIT_REACHED
      :value: "ACTIVE_RUN_JOB_TASKS_LIMIT_REACHED"

   .. py:attribute:: MAX_CONCURRENT_RUNS_REACHED
      :value: "MAX_CONCURRENT_RUNS_REACHED"

.. autoclass:: QueueSettings
   :members:
   :undoc-members:

.. autoclass:: RepairHistoryItem
   :members:
   :undoc-members:

.. py:class:: RepairHistoryItemType

   The repair history item type. Indicates whether a run is the original run or a repair run.

   .. py:attribute:: ORIGINAL
      :value: "ORIGINAL"

   .. py:attribute:: REPAIR
      :value: "REPAIR"

.. autoclass:: RepairRun
   :members:
   :undoc-members:

.. autoclass:: RepairRunResponse
   :members:
   :undoc-members:

.. autoclass:: ResetJob
   :members:
   :undoc-members:

.. autoclass:: ResetResponse
   :members:
   :undoc-members:

.. autoclass:: ResolvedConditionTaskValues
   :members:
   :undoc-members:

.. autoclass:: ResolvedDbtTaskValues
   :members:
   :undoc-members:

.. autoclass:: ResolvedNotebookTaskValues
   :members:
   :undoc-members:

.. autoclass:: ResolvedParamPairValues
   :members:
   :undoc-members:

.. autoclass:: ResolvedPythonWheelTaskValues
   :members:
   :undoc-members:

.. autoclass:: ResolvedRunJobTaskValues
   :members:
   :undoc-members:

.. autoclass:: ResolvedStringParamsValues
   :members:
   :undoc-members:

.. autoclass:: ResolvedValues
   :members:
   :undoc-members:

.. autoclass:: Run
   :members:
   :undoc-members:

.. autoclass:: RunConditionTask
   :members:
   :undoc-members:

.. autoclass:: RunForEachTask
   :members:
   :undoc-members:

.. py:class:: RunIf

   An optional value indicating the condition that determines whether the task should be run once its dependencies have been completed. When omitted, defaults to `ALL_SUCCESS`.
   Possible values are: * `ALL_SUCCESS`: All dependencies have executed and succeeded * `AT_LEAST_ONE_SUCCESS`: At least one dependency has succeeded * `NONE_FAILED`: None of the dependencies have failed and at least one was executed * `ALL_DONE`: All dependencies have been completed * `AT_LEAST_ONE_FAILED`: At least one dependency failed * `ALL_FAILED`: ALl dependencies have failed

   .. py:attribute:: ALL_DONE
      :value: "ALL_DONE"

   .. py:attribute:: ALL_FAILED
      :value: "ALL_FAILED"

   .. py:attribute:: ALL_SUCCESS
      :value: "ALL_SUCCESS"

   .. py:attribute:: AT_LEAST_ONE_FAILED
      :value: "AT_LEAST_ONE_FAILED"

   .. py:attribute:: AT_LEAST_ONE_SUCCESS
      :value: "AT_LEAST_ONE_SUCCESS"

   .. py:attribute:: NONE_FAILED
      :value: "NONE_FAILED"

.. autoclass:: RunJobOutput
   :members:
   :undoc-members:

.. autoclass:: RunJobTask
   :members:
   :undoc-members:

.. py:class:: RunLifeCycleState

   A value indicating the run's lifecycle state. The possible values are: * `QUEUED`: The run is queued. * `PENDING`: The run is waiting to be executed while the cluster and execution context are being prepared. * `RUNNING`: The task of this run is being executed. * `TERMINATING`: The task of this run has completed, and the cluster and execution context are being cleaned up. * `TERMINATED`: The task of this run has completed, and the cluster and execution context have been cleaned up. This state is terminal. * `SKIPPED`: This run was aborted because a previous run of the same job was already active. This state is terminal. * `INTERNAL_ERROR`: An exceptional state that indicates a failure in the Jobs service, such as network failure over a long period. If a run on a new cluster ends in the `INTERNAL_ERROR` state, the Jobs service terminates the cluster as soon as possible. This state is terminal. * `BLOCKED`: The run is blocked on an upstream dependency. * `WAITING_FOR_RETRY`: The run is waiting for a retry.

   .. py:attribute:: BLOCKED
      :value: "BLOCKED"

   .. py:attribute:: INTERNAL_ERROR
      :value: "INTERNAL_ERROR"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: QUEUED
      :value: "QUEUED"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SKIPPED
      :value: "SKIPPED"

   .. py:attribute:: TERMINATED
      :value: "TERMINATED"

   .. py:attribute:: TERMINATING
      :value: "TERMINATING"

   .. py:attribute:: WAITING_FOR_RETRY
      :value: "WAITING_FOR_RETRY"

.. py:class:: RunLifecycleStateV2State

   The current state of the run.

   .. py:attribute:: BLOCKED
      :value: "BLOCKED"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: QUEUED
      :value: "QUEUED"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: TERMINATED
      :value: "TERMINATED"

   .. py:attribute:: TERMINATING
      :value: "TERMINATING"

.. autoclass:: RunNow
   :members:
   :undoc-members:

.. autoclass:: RunNowResponse
   :members:
   :undoc-members:

.. autoclass:: RunOutput
   :members:
   :undoc-members:

.. autoclass:: RunParameters
   :members:
   :undoc-members:

.. py:class:: RunResultState

   A value indicating the run's result. The possible values are: * `SUCCESS`: The task completed successfully. * `FAILED`: The task completed with an error. * `TIMEDOUT`: The run was stopped after reaching the timeout. * `CANCELED`: The run was canceled at user request. * `MAXIMUM_CONCURRENT_RUNS_REACHED`: The run was skipped because the maximum concurrent runs were reached. * `EXCLUDED`: The run was skipped because the necessary conditions were not met. * `SUCCESS_WITH_FAILURES`: The job run completed successfully with some failures; leaf tasks were successful. * `UPSTREAM_FAILED`: The run was skipped because of an upstream failure. * `UPSTREAM_CANCELED`: The run was skipped because an upstream task was canceled. * `DISABLED`: The run was skipped because it was disabled explicitly by the user.

   .. py:attribute:: CANCELED
      :value: "CANCELED"

   .. py:attribute:: DISABLED
      :value: "DISABLED"

   .. py:attribute:: EXCLUDED
      :value: "EXCLUDED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: MAXIMUM_CONCURRENT_RUNS_REACHED
      :value: "MAXIMUM_CONCURRENT_RUNS_REACHED"

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

   .. py:attribute:: SUCCESS_WITH_FAILURES
      :value: "SUCCESS_WITH_FAILURES"

   .. py:attribute:: TIMEDOUT
      :value: "TIMEDOUT"

   .. py:attribute:: UPSTREAM_CANCELED
      :value: "UPSTREAM_CANCELED"

   .. py:attribute:: UPSTREAM_FAILED
      :value: "UPSTREAM_FAILED"

.. autoclass:: RunState
   :members:
   :undoc-members:

.. autoclass:: RunStatus
   :members:
   :undoc-members:

.. autoclass:: RunTask
   :members:
   :undoc-members:

.. py:class:: RunType

   The type of a run. * `JOB_RUN`: Normal job run. A run created with :method:jobs/runNow. * `WORKFLOW_RUN`: Workflow run. A run created with [dbutils.notebook.run]. * `SUBMIT_RUN`: Submit run. A run created with :method:jobs/submit.
   [dbutils.notebook.run]: https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-workflow

   .. py:attribute:: JOB_RUN
      :value: "JOB_RUN"

   .. py:attribute:: SUBMIT_RUN
      :value: "SUBMIT_RUN"

   .. py:attribute:: WORKFLOW_RUN
      :value: "WORKFLOW_RUN"

.. py:class:: Source

   Optional location type of the SQL file. When set to `WORKSPACE`, the SQL file will be retrieved    from the local Databricks workspace. When set to `GIT`, the SQL file will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise.
   * `WORKSPACE`: SQL file is located in Databricks workspace. * `GIT`: SQL file is located in cloud Git provider.

   .. py:attribute:: GIT
      :value: "GIT"

   .. py:attribute:: WORKSPACE
      :value: "WORKSPACE"

.. autoclass:: SparkJarTask
   :members:
   :undoc-members:

.. autoclass:: SparkPythonTask
   :members:
   :undoc-members:

.. autoclass:: SparkSubmitTask
   :members:
   :undoc-members:

.. autoclass:: SqlAlertOutput
   :members:
   :undoc-members:

.. py:class:: SqlAlertState

   The state of the SQL alert.
   * UNKNOWN: alert yet to be evaluated * OK: alert evaluated and did not fulfill trigger conditions * TRIGGERED: alert evaluated and fulfilled trigger conditions

   .. py:attribute:: OK
      :value: "OK"

   .. py:attribute:: TRIGGERED
      :value: "TRIGGERED"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

.. autoclass:: SqlDashboardOutput
   :members:
   :undoc-members:

.. autoclass:: SqlDashboardWidgetOutput
   :members:
   :undoc-members:

.. py:class:: SqlDashboardWidgetOutputStatus

   .. py:attribute:: CANCELLED
      :value: "CANCELLED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

.. autoclass:: SqlOutput
   :members:
   :undoc-members:

.. autoclass:: SqlOutputError
   :members:
   :undoc-members:

.. autoclass:: SqlQueryOutput
   :members:
   :undoc-members:

.. autoclass:: SqlStatementOutput
   :members:
   :undoc-members:

.. autoclass:: SqlTask
   :members:
   :undoc-members:

.. autoclass:: SqlTaskAlert
   :members:
   :undoc-members:

.. autoclass:: SqlTaskDashboard
   :members:
   :undoc-members:

.. autoclass:: SqlTaskFile
   :members:
   :undoc-members:

.. autoclass:: SqlTaskQuery
   :members:
   :undoc-members:

.. autoclass:: SqlTaskSubscription
   :members:
   :undoc-members:

.. autoclass:: SubmitRun
   :members:
   :undoc-members:

.. autoclass:: SubmitRunResponse
   :members:
   :undoc-members:

.. autoclass:: SubmitTask
   :members:
   :undoc-members:

.. autoclass:: TableUpdateTriggerConfiguration
   :members:
   :undoc-members:

.. autoclass:: Task
   :members:
   :undoc-members:

.. autoclass:: TaskDependency
   :members:
   :undoc-members:

.. autoclass:: TaskEmailNotifications
   :members:
   :undoc-members:

.. autoclass:: TaskNotificationSettings
   :members:
   :undoc-members:

.. py:class:: TerminationCodeCode

   The code indicates why the run was terminated. Additional codes might be introduced in future releases. * `SUCCESS`: The run was completed successfully. * `USER_CANCELED`: The run was successfully canceled during execution by a user. * `CANCELED`: The run was canceled during execution by the Databricks platform; for example, if the maximum run duration was exceeded. * `SKIPPED`: Run was never executed, for example, if the upstream task run failed, the dependency type condition was not met, or there were no material tasks to execute. * `INTERNAL_ERROR`: The run encountered an unexpected error. Refer to the state message for further details. * `DRIVER_ERROR`: The run encountered an error while communicating with the Spark Driver. * `CLUSTER_ERROR`: The run failed due to a cluster error. Refer to the state message for further details. * `REPOSITORY_CHECKOUT_FAILED`: Failed to complete the checkout due to an error when communicating with the third party service. * `INVALID_CLUSTER_REQUEST`: The run failed because it issued an invalid request to start the cluster. * `WORKSPACE_RUN_LIMIT_EXCEEDED`: The workspace has reached the quota for the maximum number of concurrent active runs. Consider scheduling the runs over a larger time frame. * `FEATURE_DISABLED`: The run failed because it tried to access a feature unavailable for the workspace. * `CLUSTER_REQUEST_LIMIT_EXCEEDED`: The number of cluster creation, start, and upsize requests have exceeded the allotted rate limit. Consider spreading the run execution over a larger time frame. * `STORAGE_ACCESS_ERROR`: The run failed due to an error when accessing the customer blob storage. Refer to the state message for further details. * `RUN_EXECUTION_ERROR`: The run was completed with task failures. For more details, refer to the state message or run output. * `UNAUTHORIZED_ERROR`: The run failed due to a permission issue while accessing a resource. Refer to the state message for further details. * `LIBRARY_INSTALLATION_ERROR`: The run failed while installing the user-requested library. Refer to the state message for further details. The causes might include, but are not limited to: The provided library is invalid, there are insufficient permissions to install the library, and so forth. * `MAX_CONCURRENT_RUNS_EXCEEDED`: The scheduled run exceeds the limit of maximum concurrent runs set for the job. * `MAX_SPARK_CONTEXTS_EXCEEDED`: The run is scheduled on a cluster that has already reached the maximum number of contexts it is configured to create. See: [Link]. * `RESOURCE_NOT_FOUND`: A resource necessary for run execution does not exist. Refer to the state message for further details. * `INVALID_RUN_CONFIGURATION`: The run failed due to an invalid configuration. Refer to the state message for further details. * `CLOUD_FAILURE`: The run failed due to a cloud provider issue. Refer to the state message for further details. * `MAX_JOB_QUEUE_SIZE_EXCEEDED`: The run was skipped due to reaching the job level queue size limit.
   [Link]: https://kb.databricks.com/en_US/notebooks/too-many-execution-contexts-are-open-right-now

   .. py:attribute:: CANCELED
      :value: "CANCELED"

   .. py:attribute:: CLOUD_FAILURE
      :value: "CLOUD_FAILURE"

   .. py:attribute:: CLUSTER_ERROR
      :value: "CLUSTER_ERROR"

   .. py:attribute:: CLUSTER_REQUEST_LIMIT_EXCEEDED
      :value: "CLUSTER_REQUEST_LIMIT_EXCEEDED"

   .. py:attribute:: DRIVER_ERROR
      :value: "DRIVER_ERROR"

   .. py:attribute:: FEATURE_DISABLED
      :value: "FEATURE_DISABLED"

   .. py:attribute:: INTERNAL_ERROR
      :value: "INTERNAL_ERROR"

   .. py:attribute:: INVALID_CLUSTER_REQUEST
      :value: "INVALID_CLUSTER_REQUEST"

   .. py:attribute:: INVALID_RUN_CONFIGURATION
      :value: "INVALID_RUN_CONFIGURATION"

   .. py:attribute:: LIBRARY_INSTALLATION_ERROR
      :value: "LIBRARY_INSTALLATION_ERROR"

   .. py:attribute:: MAX_CONCURRENT_RUNS_EXCEEDED
      :value: "MAX_CONCURRENT_RUNS_EXCEEDED"

   .. py:attribute:: MAX_JOB_QUEUE_SIZE_EXCEEDED
      :value: "MAX_JOB_QUEUE_SIZE_EXCEEDED"

   .. py:attribute:: MAX_SPARK_CONTEXTS_EXCEEDED
      :value: "MAX_SPARK_CONTEXTS_EXCEEDED"

   .. py:attribute:: REPOSITORY_CHECKOUT_FAILED
      :value: "REPOSITORY_CHECKOUT_FAILED"

   .. py:attribute:: RESOURCE_NOT_FOUND
      :value: "RESOURCE_NOT_FOUND"

   .. py:attribute:: RUN_EXECUTION_ERROR
      :value: "RUN_EXECUTION_ERROR"

   .. py:attribute:: SKIPPED
      :value: "SKIPPED"

   .. py:attribute:: STORAGE_ACCESS_ERROR
      :value: "STORAGE_ACCESS_ERROR"

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

   .. py:attribute:: UNAUTHORIZED_ERROR
      :value: "UNAUTHORIZED_ERROR"

   .. py:attribute:: USER_CANCELED
      :value: "USER_CANCELED"

   .. py:attribute:: WORKSPACE_RUN_LIMIT_EXCEEDED
      :value: "WORKSPACE_RUN_LIMIT_EXCEEDED"

.. autoclass:: TerminationDetails
   :members:
   :undoc-members:

.. py:class:: TerminationTypeType

   * `SUCCESS`: The run terminated without any issues * `INTERNAL_ERROR`: An error occurred in the Databricks platform. Please look at the [status page] or contact support if the issue persists. * `CLIENT_ERROR`: The run was terminated because of an error caused by user input or the job configuration. * `CLOUD_FAILURE`: The run was terminated because of an issue with your cloud provider.
   [status page]: https://status.databricks.com/

   .. py:attribute:: CLIENT_ERROR
      :value: "CLIENT_ERROR"

   .. py:attribute:: CLOUD_FAILURE
      :value: "CLOUD_FAILURE"

   .. py:attribute:: INTERNAL_ERROR
      :value: "INTERNAL_ERROR"

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

.. autoclass:: TriggerInfo
   :members:
   :undoc-members:

.. autoclass:: TriggerSettings
   :members:
   :undoc-members:

.. py:class:: TriggerType

   The type of trigger that fired this run.
   * `PERIODIC`: Schedules that periodically trigger runs, such as a cron scheduler. * `ONE_TIME`: One time triggers that fire a single run. This occurs you triggered a single run on demand through the UI or the API. * `RETRY`: Indicates a run that is triggered as a retry of a previously failed run. This occurs when you request to re-run the job in case of failures. * `RUN_JOB_TASK`: Indicates a run that is triggered using a Run Job task. * `FILE_ARRIVAL`: Indicates a run that is triggered by a file arrival. * `TABLE`: Indicates a run that is triggered by a table update.

   .. py:attribute:: FILE_ARRIVAL
      :value: "FILE_ARRIVAL"

   .. py:attribute:: ONE_TIME
      :value: "ONE_TIME"

   .. py:attribute:: PERIODIC
      :value: "PERIODIC"

   .. py:attribute:: RETRY
      :value: "RETRY"

   .. py:attribute:: RUN_JOB_TASK
      :value: "RUN_JOB_TASK"

   .. py:attribute:: TABLE
      :value: "TABLE"

.. autoclass:: UpdateJob
   :members:
   :undoc-members:

.. autoclass:: UpdateResponse
   :members:
   :undoc-members:

.. autoclass:: ViewItem
   :members:
   :undoc-members:

.. py:class:: ViewType

   * `NOTEBOOK`: Notebook view item. * `DASHBOARD`: Dashboard view item.

   .. py:attribute:: DASHBOARD
      :value: "DASHBOARD"

   .. py:attribute:: NOTEBOOK
      :value: "NOTEBOOK"

.. py:class:: ViewsToExport

   * `CODE`: Code view of the notebook. * `DASHBOARDS`: All dashboard views of the notebook. * `ALL`: All views of the notebook.

   .. py:attribute:: ALL
      :value: "ALL"

   .. py:attribute:: CODE
      :value: "CODE"

   .. py:attribute:: DASHBOARDS
      :value: "DASHBOARDS"

.. autoclass:: Webhook
   :members:
   :undoc-members:

.. autoclass:: WebhookNotifications
   :members:
   :undoc-members:

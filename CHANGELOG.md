# Version changelog

## 0.26.0

* Increase cluster creation test timeout ([#617](https://github.com/databricks/databricks-sdk-py/pull/617)).
* Added code example for adding a user to a group using group patch API ([#625](https://github.com/databricks/databricks-sdk-py/pull/625)).
* Updated SDK to OpenAPI spec ([#624](https://github.com/databricks/databricks-sdk-py/pull/624)).

Note: This release contains breaking changes, please see the API changes below for more details.

API Changes:

 * Added `deployment` field for `databricks.sdk.service.pipelines.CreatePipeline`, `databricks.sdk.service.pipelines.EditPipeline` and `databricks.sdk.service.pipelines.PipelineSpec`.
 * Added `schema_id` field for `databricks.sdk.service.catalog.SchemaInfo`.
 * Added `operation` field for `databricks.sdk.service.catalog.ValidationResult`.
 * Added `requirements` field for `databricks.sdk.service.compute.Library`.
 * Added `warehouse_id` field for `databricks.sdk.service.jobs.NotebookTask`.
 * Added `run_as` field for `databricks.sdk.service.jobs.SubmitRun`.
 * Added `databricks.sdk.service.catalog.ValidationResultOperation` dataclass.
 * Added `databricks.sdk.service.compute.ClusterStatus` dataclass.
 * Added `databricks.sdk.service.compute.ClusterStatusResponse` dataclass.
 * Added `databricks.sdk.service.compute.LibraryInstallStatus` dataclass.
 * Added `databricks.sdk.service.pipelines.DeploymentKind` dataclass.
 * Added `databricks.sdk.service.pipelines.PipelineDeployment` dataclass.
 * Removed `aws_operation` field for `databricks.sdk.service.catalog.ValidationResult`.
 * Removed `azure_operation` field for `databricks.sdk.service.catalog.ValidationResult`.
 * Removed `gcp_operation` field for `databricks.sdk.service.catalog.ValidationResult`.
 * Removed `databricks.sdk.service.catalog.ValidationResultAwsOperation` dataclass.
 * Removed `databricks.sdk.service.catalog.ValidationResultAzureOperation` dataclass.
 * Removed `databricks.sdk.service.catalog.ValidationResultGcpOperation` dataclass.
 * Removed `databricks.sdk.service.compute.LibraryFullStatusStatus` dataclass.
 * Removed `databricks.sdk.service.compute.ClusterStatusRequest` dataclass.
 * Changed `cluster_status()` method for [w.libraries](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/libraries.html) workspace-level service . New request type is `databricks.sdk.service.compute.ClusterStatus` dataclass.
 * Changed `cluster_status()` method for [w.libraries](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/libraries.html) workspace-level service to return `databricks.sdk.service.compute.ClusterStatusResponse` dataclass.
 * Changed `status` field for `databricks.sdk.service.compute.LibraryFullStatus` to `databricks.sdk.service.compute.LibraryInstallStatus` dataclass.

OpenAPI SHA: 06d330f43d92c1be864d4638c672cd0723e20a51, Date: 2024-04-22

## 0.25.1

Bug fixes:
* Fixed `select_node_type` error ([#614](https://github.com/databricks/databricks-sdk-py/pull/614)).


## 0.25.0

### Behavior Changes

* Override INVALID_PARAMETER_VALUE on fetching non-existent job/cluster ([#591](https://github.com/databricks/databricks-sdk-py/pull/591)). When getting a job or cluster by ID that doesn't exist, the API currently returns a 400, corresponding to the InvalidParameterValue exception. This change throws a ResourceNotFoundException instead in this circumstance. To handle this change, modify error handling by updating your `except` blocks from:
```py
try:
    w.jobs.get_by_id("123")
except e as InvalidParameterValue:
    ...
```
to
```py
try:
    w.jobs.get_by_id("123")
except e as ResourceDoesNotExist:
    ...
```

### Internal Changes
* Check downstream backwards compatibility ([#600](https://github.com/databricks/databricks-sdk-py/pull/600)).
* Add support for upcoming Marketplace package ([#608](https://github.com/databricks/databricks-sdk-py/pull/608)).

API Changes:

 * Changed `cancel_refresh()` method for [w.lakehouse_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakehouse_monitors.html) workspace-level service with new required argument order.
 * Changed `create()` method for [w.lakehouse_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakehouse_monitors.html) workspace-level service with new required argument order.
 * Changed `delete()` method for [w.lakehouse_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakehouse_monitors.html) workspace-level service with new required argument order.
 * Changed `get()` method for [w.lakehouse_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakehouse_monitors.html) workspace-level service with new required argument order.
 * Changed `get_refresh()` method for [w.lakehouse_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakehouse_monitors.html) workspace-level service with new required argument order.
 * Changed `list_refreshes()` method for [w.lakehouse_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakehouse_monitors.html) workspace-level service with new required argument order.
 * Changed `run_refresh()` method for [w.lakehouse_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakehouse_monitors.html) workspace-level service with new required argument order.
 * Changed `update()` method for [w.lakehouse_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakehouse_monitors.html) workspace-level service with new required argument order.
 * Removed `databricks.sdk.service.catalog.AzureManagedIdentity` dataclass.
 * Removed `full_name` field for `databricks.sdk.service.catalog.CancelRefreshRequest`.
 * Added `table_name` field for `databricks.sdk.service.catalog.CancelRefreshRequest`.
 * Changed `custom_metrics` field for `databricks.sdk.service.catalog.CreateMonitor` to `databricks.sdk.service.catalog.MonitorMetricList` dataclass.
 * Removed `full_name` field for `databricks.sdk.service.catalog.CreateMonitor`.
 * Changed `inference_log` field for `databricks.sdk.service.catalog.CreateMonitor` to `databricks.sdk.service.catalog.MonitorInferenceLog` dataclass.
 * Changed `notifications` field for `databricks.sdk.service.catalog.CreateMonitor` to `databricks.sdk.service.catalog.MonitorNotifications` dataclass.
 * Changed `snapshot` field for `databricks.sdk.service.catalog.CreateMonitor` to `any` dataclass.
 * Changed `time_series` field for `databricks.sdk.service.catalog.CreateMonitor` to `databricks.sdk.service.catalog.MonitorTimeSeries` dataclass.
 * Added `table_name` field for `databricks.sdk.service.catalog.CreateMonitor`.
 * Changed `azure_managed_identity` field for `databricks.sdk.service.catalog.CreateStorageCredential` to `databricks.sdk.service.catalog.AzureManagedIdentityRequest` dataclass.
 * Removed `full_name` field for `databricks.sdk.service.catalog.DeleteLakehouseMonitorRequest`.
 * Added `table_name` field for `databricks.sdk.service.catalog.DeleteLakehouseMonitorRequest`.
 * Removed `full_name` field for `databricks.sdk.service.catalog.GetLakehouseMonitorRequest`.
 * Added `table_name` field for `databricks.sdk.service.catalog.GetLakehouseMonitorRequest`.
 * Removed `full_name` field for `databricks.sdk.service.catalog.GetRefreshRequest`.
 * Added `table_name` field for `databricks.sdk.service.catalog.GetRefreshRequest`.
 * Removed `full_name` field for `databricks.sdk.service.catalog.ListRefreshesRequest`.
 * Added `table_name` field for `databricks.sdk.service.catalog.ListRefreshesRequest`.
 * Changed `quartz_cron_expression` field for `databricks.sdk.service.catalog.MonitorCronSchedule` to be required.
 * Changed `timezone_id` field for `databricks.sdk.service.catalog.MonitorCronSchedule` to be required.
 * Removed `databricks.sdk.service.catalog.MonitorCustomMetric` dataclass.
 * Removed `databricks.sdk.service.catalog.MonitorCustomMetricType` dataclass.
 * Removed `databricks.sdk.service.catalog.MonitorDestinations` dataclass.
 * Removed `databricks.sdk.service.catalog.MonitorInferenceLogProfileType` dataclass.
 * Removed `databricks.sdk.service.catalog.MonitorInferenceLogProfileTypeProblemType` dataclass.
 * Changed `custom_metrics` field for `databricks.sdk.service.catalog.MonitorInfo` to `databricks.sdk.service.catalog.MonitorMetricList` dataclass.
 * Changed `drift_metrics_table_name` field for `databricks.sdk.service.catalog.MonitorInfo` to be required.
 * Changed `inference_log` field for `databricks.sdk.service.catalog.MonitorInfo` to `databricks.sdk.service.catalog.MonitorInferenceLog` dataclass.
 * Changed `monitor_version` field for `databricks.sdk.service.catalog.MonitorInfo` to be required.
 * Changed `notifications` field for `databricks.sdk.service.catalog.MonitorInfo` to `databricks.sdk.service.catalog.MonitorNotifications` dataclass.
 * Changed `profile_metrics_table_name` field for `databricks.sdk.service.catalog.MonitorInfo` to be required.
 * Changed `snapshot` field for `databricks.sdk.service.catalog.MonitorInfo` to `any` dataclass.
 * Changed `status` field for `databricks.sdk.service.catalog.MonitorInfo` to be required.
 * Changed `table_name` field for `databricks.sdk.service.catalog.MonitorInfo` to be required.
 * Changed `time_series` field for `databricks.sdk.service.catalog.MonitorInfo` to `databricks.sdk.service.catalog.MonitorTimeSeries` dataclass.
 * Removed `databricks.sdk.service.catalog.MonitorNotificationsConfig` dataclass.
 * Changed `refresh_id` field for `databricks.sdk.service.catalog.MonitorRefreshInfo` to be required.
 * Changed `start_time_ms` field for `databricks.sdk.service.catalog.MonitorRefreshInfo` to be required.
 * Changed `state` field for `databricks.sdk.service.catalog.MonitorRefreshInfo` to be required.
 * Added `trigger` field for `databricks.sdk.service.catalog.MonitorRefreshInfo`.
 * Removed `any` dataclass.
 * Removed `databricks.sdk.service.catalog.MonitorTimeSeriesProfileType` dataclass.
 * Removed `full_name` field for `databricks.sdk.service.catalog.RunRefreshRequest`.
 * Added `table_name` field for `databricks.sdk.service.catalog.RunRefreshRequest`.
 * Changed `azure_managed_identity` field for `databricks.sdk.service.catalog.StorageCredentialInfo` to `databricks.sdk.service.catalog.AzureManagedIdentityResponse` dataclass.
 * Removed `name` field for `databricks.sdk.service.catalog.TableRowFilter`.
 * Added `function_name` field for `databricks.sdk.service.catalog.TableRowFilter`.
 * Changed `custom_metrics` field for `databricks.sdk.service.catalog.UpdateMonitor` to `databricks.sdk.service.catalog.MonitorMetricList` dataclass.
 * Removed `full_name` field for `databricks.sdk.service.catalog.UpdateMonitor`.
 * Changed `inference_log` field for `databricks.sdk.service.catalog.UpdateMonitor` to `databricks.sdk.service.catalog.MonitorInferenceLog` dataclass.
 * Changed `notifications` field for `databricks.sdk.service.catalog.UpdateMonitor` to `databricks.sdk.service.catalog.MonitorNotifications` dataclass.
 * Changed `snapshot` field for `databricks.sdk.service.catalog.UpdateMonitor` to `any` dataclass.
 * Changed `time_series` field for `databricks.sdk.service.catalog.UpdateMonitor` to `databricks.sdk.service.catalog.MonitorTimeSeries` dataclass.
 * Added `table_name` field for `databricks.sdk.service.catalog.UpdateMonitor`.
 * Changed `azure_managed_identity` field for `databricks.sdk.service.catalog.UpdateStorageCredential` to `databricks.sdk.service.catalog.AzureManagedIdentityResponse` dataclass.
 * Changed `azure_managed_identity` field for `databricks.sdk.service.catalog.ValidateStorageCredential` to `databricks.sdk.service.catalog.AzureManagedIdentityRequest` dataclass.
 * Removed `operation` field for `databricks.sdk.service.catalog.ValidationResult`.
 * Added `aws_operation` field for `databricks.sdk.service.catalog.ValidationResult`.
 * Added `azure_operation` field for `databricks.sdk.service.catalog.ValidationResult`.
 * Added `gcp_operation` field for `databricks.sdk.service.catalog.ValidationResult`.
 * Removed `databricks.sdk.service.catalog.ValidationResultOperation` dataclass.
 * Added `databricks.sdk.service.catalog.AzureManagedIdentityRequest` dataclass.
 * Added `databricks.sdk.service.catalog.AzureManagedIdentityResponse` dataclass.
 * Added `databricks.sdk.service.catalog.MonitorDestination` dataclass.
 * Added `databricks.sdk.service.catalog.MonitorInferenceLog` dataclass.
 * Added `databricks.sdk.service.catalog.MonitorInferenceLogProblemType` dataclass.
 * Added `databricks.sdk.service.catalog.MonitorMetric` dataclass.
 * Added `databricks.sdk.service.catalog.MonitorMetricType` dataclass.
 * Added `databricks.sdk.service.catalog.MonitorNotifications` dataclass.
 * Added `databricks.sdk.service.catalog.MonitorRefreshInfoTrigger` dataclass.
 * Added `any` dataclass.
 * Added `databricks.sdk.service.catalog.MonitorTimeSeries` dataclass.
 * Added `databricks.sdk.service.catalog.ValidationResultAwsOperation` dataclass.
 * Added `databricks.sdk.service.catalog.ValidationResultAzureOperation` dataclass.
 * Added `databricks.sdk.service.catalog.ValidationResultGcpOperation` dataclass.
 * Added `clone_from` field for `databricks.sdk.service.compute.ClusterSpec`.
 * Removed `databricks.sdk.service.compute.ComputeSpec` dataclass.
 * Removed `databricks.sdk.service.compute.ComputeSpecKind` dataclass.
 * Added `clone_from` field for `databricks.sdk.service.compute.CreateCluster`.
 * Added `clone_from` field for `databricks.sdk.service.compute.EditCluster`.
 * Added `databricks.sdk.service.compute.CloneCluster` dataclass.
 * Added `databricks.sdk.service.compute.Environment` dataclass.
 * Changed `update()` method for [a.workspace_assignment](https://databricks-sdk-py.readthedocs.io/en/latest/account/workspace_assignment.html) account-level service to return `databricks.sdk.service.iam.PermissionAssignment` dataclass.
 * Removed `any` dataclass.
 * Removed `compute_key` field for `databricks.sdk.service.jobs.ClusterSpec`.
 * Removed `compute` field for `databricks.sdk.service.jobs.CreateJob`.
 * Added `environments` field for `databricks.sdk.service.jobs.CreateJob`.
 * Removed `databricks.sdk.service.jobs.JobCompute` dataclass.
 * Removed `compute` field for `databricks.sdk.service.jobs.JobSettings`.
 * Added `environments` field for `databricks.sdk.service.jobs.JobSettings`.
 * Removed `compute_key` field for `databricks.sdk.service.jobs.RunTask`.
 * Removed `databricks.sdk.service.jobs.TableTriggerConfiguration` dataclass.
 * Removed `compute_key` field for `databricks.sdk.service.jobs.Task`.
 * Added `environment_key` field for `databricks.sdk.service.jobs.Task`.
 * Changed `table` field for `databricks.sdk.service.jobs.TriggerSettings` to `databricks.sdk.service.jobs.TableUpdateTriggerConfiguration` dataclass.
 * Changed `table_update` field for `databricks.sdk.service.jobs.TriggerSettings` to `databricks.sdk.service.jobs.TableUpdateTriggerConfiguration` dataclass.
 * Added `databricks.sdk.service.jobs.JobEnvironment` dataclass.
 * Added `databricks.sdk.service.jobs.TableUpdateTriggerConfiguration` dataclass.
 * Added `databricks.sdk.service.marketplace` package.

OpenAPI SHA: 94684175b8bd65f8701f89729351f8069e8309c9, Date: 2024-04-11

## 0.24.0

### Improvements and Bug Fixes
* Properly escape multi-segment path parameters ([#596](https://github.com/databricks/databricks-sdk-py/pull/596)).

### Internal Changes
* Revert changelog template changes for better diffs ([#590](https://github.com/databricks/databricks-sdk-py/pull/590)).

### API Changes
* Added `migrate()` and `unpublish()` method fors [w.lakeview](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakeview.html) workspace-level service.
* Added `databricks.sdk.service.dashboards.MigrateDashboardRequest` and `databricks.sdk.service.dashboards.UnpublishDashboardRequest` dataclasses.
* Added `description`, `queue_duration` and `repair_history` fields for `databricks.sdk.service.jobs.BaseRun`.
* Added `compute_key` and `job_cluster_key` fields for `databricks.sdk.service.jobs.ClusterSpec`.
* Changed `left`, `op` and `right` fields for `databricks.sdk.service.jobs.ConditionTask` to be required.
* Changed `edit_mode` field for `databricks.sdk.service.jobs.CreateJob` to `databricks.sdk.service.jobs.JobEditMode` dataclass.
* Replaced `databricks.sdk.service.jobs.CreateJobEditMode` dataclass by `databricks.sdk.service.jobs.JobEditMode`.
* Changed `url` field for `databricks.sdk.service.jobs.FileArrivalTriggerConfiguration` to be required.
* Changed `error_message_stats` field for `databricks.sdk.service.jobs.ForEachStats` to `databricks.sdk.service.jobs.ForEachTaskErrorMessageStatsList` dataclass.
* Changed `new_cluster` field for `databricks.sdk.service.jobs.JobCluster` to be required.
* Changed `edit_mode` field for `databricks.sdk.service.jobs.JobSettings` to `databricks.sdk.service.jobs.JobEditMode` dataclass.
* Replaced `databricks.sdk.service.jobs.JobsSettingsEditMode` dataclass by `databricks.sdk.service.jobs.JobEditMode`.
* Changed `metric`, `op` and `value` fields for `databricks.sdk.service.jobs.JobsHealthRule` to be required.
* Changed `run_type` field for `databricks.sdk.service.jobs.ListRunsRequest` to `databricks.sdk.service.jobs.RunType` dataclass.
* Repplaced `databricks.sdk.service.jobs.ListRunsRunType` dataclass by `databricks.sdk.service.jobs.RunType` dataclass.
* Changed `pipeline_id` field for `databricks.sdk.service.jobs.PipelineTask` to be required.
* Changed `entry_point` and `package_name` fields for `databricks.sdk.service.jobs.PythonWheelTask` to be required.
* Changed `job_parameters` field for `databricks.sdk.service.jobs.RepairRun` to dict[str,`str`] dataclass.
* Changed `base_parameters` field for `databricks.sdk.service.jobs.ResolvedNotebookTaskValues` to dict[str,`str`] dataclass.
* Changed `parameters` field for `databricks.sdk.service.jobs.ResolvedParamPairValues` to dict[str,`str`] dataclass.
* Changed `named_parameters` field for `databricks.sdk.service.jobs.ResolvedPythonWheelTaskValues` to dict[str,`str`] dataclass.
* Removed `named_parameters` field for `databricks.sdk.service.jobs.ResolvedRunJobTaskValues`.
* Changed `parameters` field for `databricks.sdk.service.jobs.ResolvedRunJobTaskValues` to dict[str,`str`] dataclass.
* Added `job_parameters` field for `databricks.sdk.service.jobs.ResolvedRunJobTaskValues`.
* Added `description` and `queue_duration` fields for `databricks.sdk.service.jobs.Run`.
* Changed `op` field for `databricks.sdk.service.jobs.RunConditionTask` to `databricks.sdk.service.jobs.ConditionTaskOp` dataclass.
* Replaced `databricks.sdk.service.jobs.RunConditionTaskOp` dataclass by `databricks.sdk.service.jobs.ConditionTaskOp` dataclass.
* Changed `inputs` and `task` fields for `databricks.sdk.service.jobs.RunForEachTask` to be required.
* Changed `job_parameters` field for `databricks.sdk.service.jobs.RunJobTask` to dict[str,`str`] dataclass.
* Added `dbt_commands`, `jar_params`, `notebook_params`, `pipeline_params`, `python_named_params`, `python_params`, `spark_submit_params` and `sql_params` fields for `databricks.sdk.service.jobs.RunJobTask`.
* Changed `job_parameters` field for `databricks.sdk.service.jobs.RunNow` to dict[str,`str`] dataclass.
* Added `info` field for `databricks.sdk.service.jobs.RunOutput`.
* Removed `job_parameters` field for `databricks.sdk.service.jobs.RunParameters`.
* Changed `task_key` field for `databricks.sdk.service.jobs.RunTask` to be required.
* Added `compute_key`, `email_notifications`, `job_cluster_key`, `notification_settings`, `run_duration`, `run_page_url`, `timeout_seconds` and `webhook_notifications` fields for `databricks.sdk.service.jobs.RunTask`.
* Added `endpoint_id` field for `databricks.sdk.service.jobs.SqlQueryOutput`.
* Added `condition_task`, `dbt_task`, `notebook_task`, `pipeline_task`, `python_wheel_task`, `run_job_task`, `spark_jar_task`, `spark_python_task`, `spark_submit_task` and `sql_task` fields for `databricks.sdk.service.jobs.SubmitRun`.
* Added `description` field for `databricks.sdk.service.jobs.SubmitTask`.
* Added `disable_auto_optimization` field for `databricks.sdk.service.jobs.Task`.
* Added `no_alert_for_skipped_runs` field for `databricks.sdk.service.jobs.TaskEmailNotifications`.
* Added `table_update` field for `databricks.sdk.service.jobs.TriggerSettings`.
* Changed `id` field for `databricks.sdk.service.jobs.Webhook` to be required.
* Changed `on_duration_warning_threshold_exceeded` field for `databricks.sdk.service.jobs.WebhookNotifications` to `databricks.sdk.service.jobs.WebhookList` dataclass.
* Removed `databricks.sdk.service.jobs.WebhookNotificationsOnDurationWarningThresholdExceededItem` dataclass.
* Added `databricks.sdk.service.jobs.JobEditMode` dataclass.
* Replaced `databricks.sdk.service.serving.AwsBedrockConfig` dataclass by `databricks.sdk.service.serving.AmazonBedrockConfig` dataclass.
* Replaced `databricks.sdk.service.serving.AwsBedrockConfigBedrockProvider` dataclass by `databricks.sdk.service.serving.AmazonBedrockConfigBedrockProvider` dataclass.
* Renamed `aws_bedrock_config` field for `databricks.sdk.service.serving.ExternalModel` to `amazon_bedrock_config`.
* Changed `get()` method for [w.ip_access_lists](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ip_access_lists.html) workspace-level service . New request type is `databricks.sdk.service.settings.GetIpAccessListRequest` dataclass.
* Replaced `databricks.sdk.service.settings.GetIpAccessList` dataclass by `databricks.sdk.service.settings.GetIpAccessListRequest` dataclass.
  
OpenAPI SHA: d38528c3e47dd81c9bdbd918272a3e49d36e09ce, Date: 2024-03-27

## 0.23.0

* Add CONTRIBUTING.md ([#585](https://github.com/databricks/databricks-sdk-py/pull/585)).

API Changes:

 * Added `databricks.sdk.service.catalog.AwsIamRoleResponse` dataclass.
 * Added `databricks.sdk.service.catalog.AwsIamRoleRequest` dataclass.
 * Removed `databricks.sdk.service.catalog.AwsIamRole` dataclass.
 * Changed `aws_iam_role` field for `databricks.sdk.service.catalog.CreateStorageCredential` to `databricks.sdk.service.catalog.AwsIamRoleRequest` dataclass.
 * Changed `aws_iam_role` field for `databricks.sdk.service.catalog.StorageCredentialInfo` to `databricks.sdk.service.catalog.AwsIamRoleResponse` dataclass.
 * Changed `aws_iam_role` field for `databricks.sdk.service.catalog.UpdateStorageCredential` to `databricks.sdk.service.catalog.AwsIamRoleRequest` dataclass.
 * Changed `aws_iam_role` field for `databricks.sdk.service.catalog.ValidateStorageCredential` to `databricks.sdk.service.catalog.AwsIamRoleRequest` dataclass.
 * Added `auto_capture_config` field for `databricks.sdk.service.serving.EndpointPendingConfig`.
 * Added `databricks.sdk.service.sharing.SharedDataObjectDataObjectType` dataclass.
 * Changed `data_object_type` field for `databricks.sdk.service.sharing.SharedDataObject` to `databricks.sdk.service.sharing.SharedDataObjectDataObjectType` dataclass.
 * Added `content` field for `databricks.sdk.service.sharing.SharedDataObject`.
 * Added `embedding_source_columns` field for `databricks.sdk.service.vectorsearch.DirectAccessVectorIndexSpec`.

OpenAPI SHA: 93763b0d7ae908520c229c786fff28b8fd623261, Date: 2024-03-20

## 0.22.0

* Fix typos in doc string for select_spark_version ([#575](https://github.com/databricks/databricks-sdk-py/pull/575)).

API Changes:

 * Changed `notifications` field for `databricks.sdk.service.catalog.CreateMonitor`, `databricks.sdk.service.catalog.MonitorInfo`, and `databricks.sdk.service.catalog.UpdateMonitor` to `databricks.sdk.service.catalog.MonitorNotificationsConfig` dataclass.
 * Added `browse_only` field for `databricks.sdk.service.catalog.ExternalLocationInfo`, `databricks.sdk.service.catalog.FunctionInfo`, `databricks.sdk.service.catalog.ModelVersionInfo`, `databricks.sdk.service.catalog.RegisteredModelInfo`, `databricks.sdk.service.catalog.SchemaInfo`, `databricks.sdk.service.catalog.TableInfo`, and `databricks.sdk.service.catalog.VolumeInfo`.
 * Added `include_browse` field for `databricks.sdk.service.catalog.GetCatalogRequest`,  `databricks.sdk.service.catalog.GetExternalLocationRequest`,  `databricks.sdk.service.catalog.GetFunctionRequest`,  `databricks.sdk.service.catalog.GetModelVersionRequest`,  `databricks.sdk.service.catalog.GetRegisteredModelRequest`,  `databricks.sdk.service.catalog.GetSchemaRequest`,  `databricks.sdk.service.catalog.GetTableRequest`,  `databricks.sdk.service.catalog.ListExternalLocationsRequest`,  `databricks.sdk.service.catalog.ListFunctionsRequest`,  `databricks.sdk.service.catalog.ListModelVersionsRequest`,  `databricks.sdk.service.catalog.ListRegisteredModelsRequest`,  `databricks.sdk.service.catalog.ListSchemasRequest`,  `databricks.sdk.service.catalog.ListTablesRequest`, `databricks.sdk.service.catalog.ListVolumesRequest`, and `databricks.sdk.service.catalog.ReadVolumeRequest`.
 * Changed `publish()` method for [w.lakeview](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakeview.html) workspace-level service to return `databricks.sdk.service.dashboards.PublishedDashboard` dataclass.
 * Added `create()`, `get()`, `get_published()`, `trash()`, and `update()` methods for [w.lakeview](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakeview.html) workspace-level service.
 * Added `databricks.sdk.service.dashboards.CreateDashboardRequest`, `databricks.sdk.service.dashboards.Dashboard`, `databricks.sdk.service.dashboards.GetLakeviewRequest`, `databricks.sdk.service.dashboards.GetPublishedRequest`, `databricks.sdk.service.dashboards.LifecycleState`, `databricks.sdk.service.dashboards.PublishedDashboard`, `databricks.sdk.service.dashboards.TrashRequest`, and `databricks.sdk.service.dashboards.UpdateDashboardRequest` dataclasses.

OpenAPI SHA: c84caf9e5ef531cc0b1ddd0a76970d9a8b664e32, Date: 2024-03-15

## 0.21.0

### New Features and Improvements
* Fixed get_workspace_client in GCP ([#532](https://github.com/databricks/databricks-sdk-py/pull/532)).
* Use all-apis scope with external-browser ([#563](https://github.com/databricks/databricks-sdk-py/pull/563)).
* Make a best effort attempt to initialise all Databricks globals ([#562](https://github.com/databricks/databricks-sdk-py/pull/562)).
* Fixed type issue with widgets.getArgument ([#581](https://github.com/databricks/databricks-sdk-py/pull/581))
* Note: Backwards incompatible changes - Settings are now nested, please see the API changes below.

### Documentation
* Added Files API docs to the SDK Documentation ([#556](https://github.com/databricks/databricks-sdk-py/pull/556)).
* Added new example to list compute resource for SUBMIT_RUN job runs ([#572](https://github.com/databricks/databricks-sdk-py/pull/572)).
* Sorted index pages by name in docs ([#560](https://github.com/databricks/databricks-sdk-py/pull/560)).
* Added back enums to docs ([#557](https://github.com/databricks/databricks-sdk-py/pull/557)).

### API Changes
#### Added
Services:
- [w.permission_migration](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/permission_migration.html) workspace-level service.
- [w.settings.automatic_cluster_update](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/automatic_cluster_update.html) workspace-level service.
- [w.settings.csp_enablement](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/csp_enablement.html) workspace-level service.
- [a.settings.csp_enablement_account](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/csp_enablement_account.html) account-level service.
- [w.settings.default_namespace](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/default_namespace.html) workspace-level service.
- [w.settings.esm_enablement](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/esm_enablement.html) workspace-level service.
- [a.settings.esm_enablement_account](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/esm_enablement_account.html) account-level service.
- [a.settings.personal_compute](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/personal_compute.html) account-level service.
- [w.settings.restrict_workspace_admins](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/restrict_workspace_admins.html) workspace-level service.

Dataclasses:
- `databricks.sdk.service.settings.AutomaticClusterUpdateSetting`
- `databricks.sdk.service.settings.ClusterAutoRestartMessage`
- `databricks.sdk.service.settings.ClusterAutoRestartMessageEnablementDetails`
- `databricks.sdk.service.settings.ClusterAutoRestartMessageMaintenanceWindow`
- `databricks.sdk.service.settings.ClusterAutoRestartMessageMaintenanceWindowDayOfWeek`
- `databricks.sdk.service.settings.ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule`
- `databricks.sdk.service.settings.ClusterAutoRestartMessageMaintenanceWindowWeekDayFrequency`
- `databricks.sdk.service.settings.ClusterAutoRestartMessageMaintenanceWindowWindowStartTime`
- `databricks.sdk.service.settings.ComplianceStandard`
- `databricks.sdk.service.settings.CspEnablement`
- `databricks.sdk.service.settings.CspEnablementAccount`
- `databricks.sdk.service.settings.CspEnablementAccountSetting`
- `databricks.sdk.service.settings.CspEnablementSetting`
- `databricks.sdk.service.settings.DeleteDefaultNamespaceRequest`
- `databricks.sdk.service.settings.DeletePersonalComputeRequest`
- `databricks.sdk.service.settings.DeleteRestrictWorkspaceAdminRequest`
- `databricks.sdk.service.settings.EsmEnablement`
- `databricks.sdk.service.settings.EsmEnablementAccount`
- `databricks.sdk.service.settings.EsmEnablementAccountSetting`
- `databricks.sdk.service.settings.EsmEnablementSetting`
- `databricks.sdk.service.settings.GetAutomaticClusterUpdateRequest`
- `databricks.sdk.service.settings.GetCspEnablementAccountRequest`
- `databricks.sdk.service.settings.GetCspEnablementRequest`
- `databricks.sdk.service.settings.GetDefaultNamespaceRequest`
- `databricks.sdk.service.settings.GetEsmEnablementAccountRequest`
- `databricks.sdk.service.settings.GetEsmEnablementRequest`
- `databricks.sdk.service.settings.GetPersonalComputeRequest`
- `databricks.sdk.service.settings.GetRestrictWorkspaceAdminRequest`
- `databricks.sdk.service.settings.NccAwsStableIpRule`
- `databricks.sdk.service.settings.UpdateAutomaticClusterUpdateSettingRequest`
- `databricks.sdk.service.settings.UpdateCspEnablementAccountSettingRequest`
- `databricks.sdk.service.settings.UpdateCspEnablementSettingRequest`
- `databricks.sdk.service.settings.UpdateEsmEnablementAccountSettingRequest`
- `databricks.sdk.service.settings.UpdateEsmEnablementSettingRequest`
- `databricks.sdk.service.vectorsearch.ClusterAutoRestartMessageMaintenanceWindow`
- `databricks.sdk.service.vectorsearch.ClusterAutoRestartMessageMaintenanceWindowDayOfWeek`
- `databricks.sdk.service.vectorsearch.ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule`
- `databricks.sdk.service.vectorsearch.ClusterAutoRestartMessageMaintenanceWindowWeekDayFrequency`
- `databricks.sdk.service.vectorsearch.ClusterAutoRestartMessageMaintenanceWindowWindowStartTime`
- `databricks.sdk.service.vectorsearch.ComplianceStandard`
- `databricks.sdk.service.vectorsearch.CspEnablement`
- `databricks.sdk.service.vectorsearch.CspEnablementAccount`
- `databricks.sdk.service.vectorsearch.CspEnablementAccountSetting`
- `databricks.sdk.service.vectorsearch.CspEnablementSetting`
- `databricks.sdk.service.vectorsearch.DeleteDefaultNamespaceRequest`
- `databricks.sdk.service.vectorsearch.DeletePersonalComputeRequest`
- `databricks.sdk.service.vectorsearch.DeleteRestrictWorkspaceAdminRequest`
- `databricks.sdk.service.vectorsearch.EsmEnablement`
- `databricks.sdk.service.vectorsearch.EsmEnablementAccount`
- `databricks.sdk.service.vectorsearch.EsmEnablementAccountSetting`
- `databricks.sdk.service.vectorsearch.EsmEnablementSetting`
- `databricks.sdk.service.vectorsearch.GetAutomaticClusterUpdateRequest`
- `databricks.sdk.service.vectorsearch.GetCspEnablementAccountRequest`
- `databricks.sdk.service.vectorsearch.GetCspEnablementRequest`
- `databricks.sdk.service.vectorsearch.GetDefaultNamespaceRequest`
- `databricks.sdk.service.vectorsearch.GetEsmEnablementAccountRequest`
- `databricks.sdk.service.vectorsearch.GetEsmEnablementRequest`
- `databricks.sdk.service.vectorsearch.GetPersonalComputeRequest`
- `databricks.sdk.service.vectorsearch.GetRestrictWorkspaceAdminRequest`
- `databricks.sdk.service.vectorsearch.NccAwsStableIpRule`
- `databricks.sdk.service.vectorsearch.UpdateAutomaticClusterUpdateSettingRequest`
- `databricks.sdk.service.vectorsearch.UpdateCspEnablementAccountSettingRequest`
- `databricks.sdk.service.vectorsearch.UpdateCspEnablementSettingRequest`
- `databricks.sdk.service.vectorsearch.UpdateEsmEnablementAccountSettingRequest`
- `databricks.sdk.service.vectorsearch.UpdateEsmEnablementSettingRequest`
- `databricks.sdk.service.iam.PermissionMigrationRequest`
- `databricks.sdk.service.iam.PermissionMigrationResponse` 

#### Changed
- `version` field for `databricks.sdk.service.serving.AppManifest` to `databricks.sdk.service.serving.AnyValue` dataclass.
- `delete_endpoint()` method for [w.vector_search_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/vector_search_endpoints.html) workspace-level service with new required argument order.
- `create_index()` method for [w.vector_search_indexes](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/vector_search_indexes.html) workspace-level service with new required argument order.
- `delete_data_vector_index()` method for [w.vector_search_indexes](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/vector_search_indexes.html) workspace-level service with new required argument order.
- `upsert_data_vector_index()` method for [w.vector_search_indexes](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/vector_search_indexes.html) workspace-level service with new required argument order.
- `endpoint_name` field for `databricks.sdk.service.vectorsearch.CreateVectorIndexRequest` to be required.

#### Removed
- `delete_personal_compute_setting()` method for [a.account_settings](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_settings.html) account-level service.
- `get_personal_compute_setting()` method for [a.account_settings](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_settings.html) account-level service.
- `update_personal_compute_setting()` method for [a.account_settings](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_settings.html) account-level service.
- `delete_default_namespace_setting()` method for [w.settings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings.html) workspace-level service.
- `delete_restrict_workspace_admins_setting()` method for [w.settings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings.html) workspace-level service.
- `get_default_namespace_setting()` method for [w.settings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings.html) workspace-level service.
- `get_restrict_workspace_admins_setting()` method for [w.settings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings.html) workspace-level service.
- `update_default_namespace_setting()` method for [w.settings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings.html) workspace-level service.
- `update_restrict_workspace_admins_setting()` method for [w.settings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings.html) workspace-level service.
- `databricks.sdk.service.settings.DeleteDefaultNamespaceSettingRequest` dataclass.
- `databricks.sdk.service.settings.DeletePersonalComputeSettingRequest` dataclass.
- `databricks.sdk.service.settings.DeleteRestrictWorkspaceAdminsSettingRequest` dataclass.
- `databricks.sdk.service.settings.GetDefaultNamespaceSettingRequest` dataclass.
- `databricks.sdk.service.settings.GetPersonalComputeSettingRequest` dataclass.
- `databricks.sdk.service.settings.GetRestrictWorkspaceAdminsSettingRequest` dataclass.
- `databricks.sdk.service.vectorsearch.EmbeddingConfig` dataclass.
- `embedding_config` field for `databricks.sdk.service.vectorsearch.EmbeddingSourceColumn`.
- `name` field for `databricks.sdk.service.vectorsearch.DeleteDataVectorIndexRequest`.
- `name` field for `databricks.sdk.service.vectorsearch.DeleteEndpointRequest`.
- `planning_phases` field for `databricks.sdk.service.sql.QueryMetrics`.
- `delta_sync_vector_index_spec` field for `databricks.sdk.service.vectorsearch.VectorIndex`.
- `direct_access_vector_index_spec` field for `databricks.sdk.service.vectorsearch.VectorIndex`.

### Internal Changes
* Added tokei.rs badge ([#567](https://github.com/databricks/databricks-sdk-py/pull/567)).
* Update SDK to latest OpenAPI spec ([#576](https://github.com/databricks/databricks-sdk-py/pull/576)).
* Add integration tests for Files API ([#552](https://github.com/databricks/databricks-sdk-py/pull/552)).
* Fix integer deserialization for headers ([#553](https://github.com/databricks/databricks-sdk-py/pull/553)).
* Support subservices ([#559](https://github.com/databricks/databricks-sdk-py/pull/559)).
* Distinguish between empty types and fields that can take any value ([#561](https://github.com/databricks/databricks-sdk-py/pull/561)).

OpenAPI SHA: 1026b998b14fba1b8317528f47778240dc4e9a5d, Date: 2024-03-06


## 0.20.0

Major Changes:

* Updated behaviour for raw parameter in `ApiClient.do()` method. The raw data is not returned directly anymore, but as part of a dict with the `contents` key. This dict will also contain response headers if returned by the API.

Internal Changes:
 
* Add get_workspace_id to docgen blocklist ([#549](https://github.com/databricks/databricks-sdk-py/pull/549)).
* Support HEAD operation and response Headers ([#547](https://github.com/databricks/databricks-sdk-py/pull/547)).

API Changes:

 * Changed `delete()`, `get()` and `update()` methods for [w.connections](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/connections.html) workspace-level service with new required argument order.
 * Changed `update()` method for [w.lakehouse_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakehouse_monitors.html) workspace-level service with new required argument order.
 * Changed `delete()`, `get()` and `update()` methods for [w.volumes](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/volumes.html) workspace-level service with new required argument order.
 * Added [w.online_tables](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/online_tables.html) workspace-level service.
 * Renamed `name_arg` field to `name` for the following dataclasses: `databricks.sdk.service.catalog.DeleteConnectionRequest`,
   `databricks.sdk.service.catalog.GetConnectionRequest`,
   `databricks.sdk.service.catalog.UpdateConnection`,
   `databricks.sdk.service.sharing.DeleteCleanRoomRequest`, 
   `databricks.sdk.service.sharing.GetCleanRoomRequest` and
   `databricks.sdk.service.sharing.UpdateCleanRoom`.
 * Removed `full_name_arg` field for `databricks.sdk.service.catalog.DeleteVolumeRequest`.
 * Added `name` field for `databricks.sdk.service.catalog.DeleteVolumeRequest`.
 * Added `max_results` field for `databricks.sdk.service.catalog.ListVolumesRequest`.
 * Added `page_token` field for `databricks.sdk.service.catalog.ListVolumesRequest`.
 * Added `next_page_token` field for `databricks.sdk.service.catalog.ListVolumesResponseContent`.
 * Removed `full_name_arg` field for `databricks.sdk.service.catalog.ReadVolumeRequest`.
 * Added `name` field for `databricks.sdk.service.catalog.ReadVolumeRequest`.
 * Removed `assets_dir` field for `databricks.sdk.service.catalog.UpdateMonitor`.
 * Removed `full_name_arg` field for `databricks.sdk.service.catalog.UpdateVolumeRequestContent`.
 * Added `name` field for `databricks.sdk.service.catalog.UpdateVolumeRequestContent`.
 * Added the following catalog dataclasses: `ContinuousUpdateStatus`, `DeleteOnlineTableRequest`, `FailedStatus`,
   `GetOnlineTableRequest`, `OnlineTable`, `OnlineTableSpec`, `OnlineTableState`, `OnlineTableStatus`,
   `PipelineProgress`, `ProvisioningStatus`, `TriggeredUpdateStatus` and `ViewData`.
 * Added `get_directory_metadata()` method for [w.files](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/files.html) workspace-level service.
 * Added `get_metadata()` method for [w.files](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/files.html) workspace-level service.
 * Added `content_length`, `content_type` and `last_modified` fields for `databricks.sdk.service.files.DownloadResponse`.
 * Added the following files dataclasses: `FileSize`, `GetDirectoryMetadataRequest`, `GetMetadataRequest`,
   `GetMetadataResponse` and `LastModifiedHttpDate`.
 * Removed `trigger_history` field for `databricks.sdk.service.jobs.Job`.
 * Removed `databricks.sdk.service.jobs.TriggerEvaluation` dataclass.
 * Removed `databricks.sdk.service.jobs.TriggerHistory` dataclass.
 * Added `table` field for `databricks.sdk.service.jobs.TriggerSettings`.
 * Added `databricks.sdk.service.jobs.Condition` dataclass.
 * Added `databricks.sdk.service.jobs.TableTriggerConfiguration` dataclass.
 * Removed `config` field for `databricks.sdk.service.serving.ExternalModel`.
 * Removed `databricks.sdk.service.serving.ExternalModelConfig` dataclass. Fields moved to `databricks.sdk.service.serving.ExternalModel`.
 * Added `max_provisioned_throughput` and `min_provisioned_throughput` fields for `databricks.sdk.service.serving.ServedEntityInput`.
 * Added `max_provisioned_throughput` and `min_provisioned_throughput` fields for `databricks.sdk.service.serving.ServedEntityOutput`.
 * Changed `delete()` method for [w.clean_rooms](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/clean_rooms.html) workspace-level service with new required argument order.
 * Changed `get()` method for [w.clean_rooms](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/clean_rooms.html) workspace-level service with new required argument order.
 * Changed `update()` method for [w.clean_rooms](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/clean_rooms.html) workspace-level service with new required argument order.
 * Added `enum_options` field for `databricks.sdk.service.sql.Parameter`.
 * Added `multi_values_options` field for `databricks.sdk.service.sql.Parameter`.
 * Added `query_id` field for `databricks.sdk.service.sql.Parameter`.
 * Added `databricks.sdk.service.sql.MultiValuesOptions` dataclass.

OpenAPI SHA: cdd76a98a4fca7008572b3a94427566dd286c63b, Date: 2024-02-19

## 0.19.1

New features:

* Add `get_workspace_id()` to WorkspaceClient ([#537](https://github.com/databricks/databricks-sdk-py/pull/537)).

Bugfix:

* Create a deepcopy of config when creating workspace client from account client ([#542](https://github.com/databricks/databricks-sdk-py/pull/542)). This fixes an issue where `AccountClient` instances would stop working after calling `get_workspace_client()`.
## 0.19.0

### Improvements and Bug Fixes
* Construct workspace client from account client ([#527](https://github.com/databricks/databricks-sdk-py/pull/527)).
* Enabled Databricks OAuth also for Azure and GCP ([#526](https://github.com/databricks/databricks-sdk-py/pull/526)).
* Do not terminate listing for token-based pagination resources on empty response ([#530](https://github.com/databricks/databricks-sdk-py/pull/530)).
* Renamed `databricks.sdk.errors.mapping` to `databricks.sdk.errors.platform` ([#522](https://github.com/databricks/databricks-sdk-py/pull/522)).
* Added Union to content (2nd) parameter in upload function ([#493](https://github.com/databricks/databricks-sdk-py/pull/493)).
* Fixed WorkspaceConf.get_status and WorkspaceConf.set_status ([#525](https://github.com/databricks/databricks-sdk-py/pull/525)).

### Documentation
* Make docs useful again ([#519](https://github.com/databricks/databricks-sdk-py/pull/519)).
* Show undocumented fields in dataclasses ([#520](https://github.com/databricks/databricks-sdk-py/pull/520)). 


### API Changes

Additions:
 * Added the following dataclasses:
    - `databricks.sdk.service.catalog.CancelRefreshRequest`
    - `databricks.sdk.service.catalog.GetRefreshRequest` 
    - `databricks.sdk.service.catalog.ListRefreshesRequest`
    - `databricks.sdk.service.catalog.MonitorRefreshInfo`
    - `databricks.sdk.service.catalog.MonitorRefreshInfoState`
    - `databricks.sdk.service.catalog.RunRefreshRequest`
    - `databricks.sdk.service.compute.Adlsgen2Info`
    - `databricks.sdk.service.compute.GcsStorageInfo`
    - `databricks.sdk.service.files.CreateDirectoryRequest`
    - `databricks.sdk.service.files.DeleteDirectoryRequest`
    - `databricks.sdk.service.files.DirectoryEntry`
    - `databricks.sdk.service.files.ListDirectoryContentsRequest`
    - `databricks.sdk.service.files.ListDirectoryResponse`
    -  `databricks.sdk.service.files.PageToken`
    - `databricks.sdk.service.jobs.ForEachStats`
    - `databricks.sdk.service.jobs.ForEachTask`
    - `databricks.sdk.service.jobs.ForEachTaskErrorMessageStats`
    - `databricks.sdk.service.jobs.ForEachTaskTaskRunStats`
    - `databricks.sdk.service.jobs.RunForEachTask`
    - `databricks.sdk.service.pipelines.PipelineClusterAutoscale`
    - `databricks.sdk.service.pipelines.PipelineClusterAutoscaleMode`
    - `databricks.sdk.service.settings.DeleteDefaultNamespaceSettingRequest`
    - `databricks.sdk.service.settings.DeleteDefaultNamespaceSettingResponse`
    - `databricks.sdk.service.settings.DeleteRestrictWorkspaceAdminsSettingRequest`
    - `databricks.sdk.service.settings.DeleteRestrictWorkspaceAdminsSettingResponse`
    - `databricks.sdk.service.settings.GetDefaultNamespaceSettingRequest`
    - `databricks.sdk.service.settings.GetPersonalComputeSettingRequest`
    - `databricks.sdk.service.settings.GetRestrictWorkspaceAdminsSettingRequest`
    - `databricks.sdk.service.settings.RestrictWorkspaceAdminsMessage`
    - `databricks.sdk.service.settings.RestrictWorkspaceAdminsMessageStatus`
    - `databricks.sdk.service.settings.RestrictWorkspaceAdminsSetting`
    - `databricks.sdk.service.settings.UpdateDefaultNamespaceSettingRequest`
    - `databricks.sdk.service.settings.UpdateRestrictWorkspaceAdminsSettingRequest`
 * Added `cancel_refresh()`, `get_refresh()`, `list_refreshes()` and `run_refresh()` method for [w.lakehouse_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakehouse_monitors.html) workspace-level service.
 * Added `use_preemptible_executors` field for `databricks.sdk.service.compute.GcpAttributes`.
 * Added `zone_id` field for `databricks.sdk.service.compute.GcpAttributes`.
 * Added `abfss` and `gcs` field for `databricks.sdk.service.compute.InitScriptInfo`.
 * Added `create_directory()`, `delete_directory()` and `list_directory_contents()` method for [w.files](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/files.html) workspace-level service.
 * Added `source` field for `databricks.sdk.service.jobs.DbtTask` and `databricks.sdk.service.jobs.SqlTaskFile`.
 * Added `for_each_task` field for `databricks.sdk.service.jobs.RunTask`, `databricks.sdk.service.jobs.SubmitTask` and `databricks.sdk.service.jobs.Task`.
 * Added `field_mask` field for `databricks.sdk.service.settings.UpdatePersonalComputeSettingRequest`.
 * Added `delta_sync_index_spec` field for `databricks.sdk.service.vectorsearch.CreateVectorIndexRequest`.
 * Added `file_type` field for `databricks.sdk.service.workspace.ExportResponse`.
 * Added `resource_id` field for `databricks.sdk.service.workspace.ObjectInfo`.
 * Added `delete_default_namespace_setting()`, `delete_restrict_workspace_admins_setting()`, `get_default_namespace_setting()`, `get_restrict_workspace_admins_setting()`, `update_default_namespace_setting()` and `update_restrict_workspace_admins_setting()` method for [w.settings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings.html) workspace-level service.
 * Added `get_personal_compute_setting()` method for [a.account_settings](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_settings.html) account-level service.

Removals:
 * Removed the following dataclasses:
    - `databricks.sdk.service.settings.ReadDefaultWorkspaceNamespaceRequest`
    - `databricks.sdk.service.settings.ReadPersonalComputeSettingRequest`
    - `databricks.sdk.service.settings.UpdateDefaultWorkspaceNamespaceRequest`
    - `databricks.sdk.service.settings.DeleteDefaultWorkspaceNamespaceRequest`
    - `databricks.sdk.service.settings.DeleteDefaultWorkspaceNamespaceResponse`
    - `databricks.sdk.service.pipelines.ResetRequest`
 * Removed the following methods:
    - `get_status()` for [w.files](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/files.html) workspace-level service.
    - `reset()` for [w.pipelines](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/pipelines.html) workspace-level service.
    - `delete_default_workspace_namespace()` for [w.settings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings.html) workspace-level service.
    - `read_default_workspace_namespace()` for [w.settings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings.html) workspace-level service.
    - `update_default_workspace_namespace()` for [w.settings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings.html) workspace-level service.
    - `read_personal_compute_setting()` for [a.account_settings](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_settings.html) account-level service.
 * Removed `name` field for `databricks.sdk.service.catalog.UpdateConnection`, `databricks.sdk.service.catalog.UpdateMetastore`, `databricks.sdk.service.catalog.UpdateRegisteredModelRequest`. `databricks.sdk.service.catalog.UpdateSchema`and `databricks.sdk.service.catalog.UpdateVolumeRequestContent`.
 * Removed `delta_sync_vector_index_spec` field for `databricks.sdk.service.vectorsearch.CreateVectorIndexRequest`.

Changes:
 * Changed `max_workers` and `min_workers` field for `databricks.sdk.service.compute.AutoScale` to no longer be required.
 * Changed `destination` field for `databricks.sdk.service.compute.DbfsStorageInfo`, `databricks.sdk.service.compute.LocalFileInfo`, `databricks.sdk.service.compute.S3StorageInfo`, `databricks.sdk.service.compute.VolumesStorageInfo` and `databricks.sdk.service.compute.WorkspaceStorageInfo` to be required.
 * Changed `clients` field for `databricks.sdk.service.compute.WorkloadType` to be required.
 * Changed `allow_missing` and `setting` field for `databricks.sdk.service.settings.UpdatePersonalComputeSettingRequest` to be required.
 * Changed `etag` field for `databricks.sdk.service.settings.DeletePersonalComputeSettingRequest` to no longer be required.
 * Changed `autoscale` field for `databricks.sdk.service.pipelines.PipelineCluster` to `databricks.sdk.service.pipelines.PipelineClusterAutoscale` dataclass.
 * Changed `delete_personal_compute_setting()` and `update_personal_compute_setting()` method for [a.account_settings](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_settings.html) account-level service with new required argument order.

### Internal Changes
* Generate SDK ([#536](https://github.com/databricks/databricks-sdk-py/pull/536)).
* Use fake clock for faster unit tests ([#533](https://github.com/databricks/databricks-sdk-py/pull/533)).
* Skip test_get_workspace_client in Azure and GCP ([#531](https://github.com/databricks/databricks-sdk-py/pull/531)).
* Regenerate from the tip of main ([#524](https://github.com/databricks/databricks-sdk-py/pull/524)).
* Search for both databricks.exe and databricks binaries in windows ([#517](https://github.com/databricks/databricks-sdk-py/pull/517)).

OpenAPI SHA: 6b897bc95b23abed8b9f5eff0e6b8ec034046180, Date: 2024-02-08

## 0.18.0

Bugfixes:

* Fix Databricks OAuth M2M on Azure ([#513](https://github.com/databricks/databricks-sdk-py/pull/513)).

Other noteworthy changes:

* Use `[]` instead of `None` as default list value for deserialising responses ([#361](https://github.com/databricks/databricks-sdk-py/pull/361)).
* Support dev and staging workspaces ([#514](https://github.com/databricks/databricks-sdk-py/pull/514)).

API Changes:

 * Added `exists()` method for [w.tables](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/tables.html) workspace-level service.
 * Added [w.lakehouse_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/lakehouse_monitors.html) workspace-level service.
 * Added the following dataclasses: 
  `databricks.sdk.service.catalog.CreateMonitor`, 
  `databricks.sdk.service.catalog.DeleteLakehouseMonitorRequest`, 
  `databricks.sdk.service.catalog.ExistsRequest`, 
  `databricks.sdk.service.catalog.GetLakehouseMonitorRequest`, 
  `databricks.sdk.service.catalog.MonitorCronSchedule`, 
  `databricks.sdk.service.catalog.MonitorCronSchedulePauseStatus`, 
  `databricks.sdk.service.catalog.MonitorCustomMetric`, 
  `databricks.sdk.service.catalog.MonitorCustomMetricType`, 
  `databricks.sdk.service.catalog.MonitorDataClassificationConfig`, 
  `databricks.sdk.service.catalog.MonitorDestinations`, 
  `databricks.sdk.service.catalog.MonitorInferenceLogProfileType`, 
  `databricks.sdk.service.catalog.MonitorInferenceLogProfileTypeProblemType`, 
  `databricks.sdk.service.catalog.MonitorInfo`, 
  `databricks.sdk.service.catalog.MonitorInfoStatus`, 
  `databricks.sdk.service.catalog.MonitorNotificationsConfig`, 
  `databricks.sdk.service.catalog.MonitorTimeSeriesProfileType`, 
  `databricks.sdk.service.catalog.TableExistsResponse` and
  `databricks.sdk.service.catalog.UpdateMonitor`.
 * Changed `create_obo_token()` method for [w.token_management](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/token_management.html) workspace-level service with new required argument order.
 * Changed `get()` method for [w.token_management](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/token_management.html) workspace-level service to return `databricks.sdk.service.settings.GetTokenResponse` dataclass.
 * Changed `lifetime_seconds` field for `databricks.sdk.service.settings.CreateOboTokenRequest` to no longer be required.
 * Added `databricks.sdk.service.settings.GetTokenResponse` dataclass.

OpenAPI SHA: e05401ed5dd4974c5333d737ec308a7d451f749f, Date: 2024-01-23

## 0.17.0

* Use covariant type for `@retried(on=[...])` ([#486](https://github.com/databricks/databricks-sdk-py/pull/486)).
* Configure request timeout using existing parameter from Config ([#489](https://github.com/databricks/databricks-sdk-py/pull/489)).
* Make contents of `__init__.py` equal across projects ([#488](https://github.com/databricks/databricks-sdk-py/pull/488)).
* Update SDK to Latest OpenAPI Specification ([#501](https://github.com/databricks/databricks-sdk-py/pull/501)).

Note: This release contains breaking changes, please see below for more details.

API Changes:

 * [Breaking] Changed `list()` method for [w.tokens](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/tokens.html) workspace-level service to return `databricks.sdk.service.settings.ListPublicTokensResponse` dataclass.
 * Changed `list()` method for [w.external_locations](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/external_locations.html) workspace-level service to require request of `databricks.sdk.service.catalog.ListExternalLocationsRequest` dataclass and [w.storage_credentials](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/storage_credentials.html) workspace-level service to require request of `databricks.sdk.service.catalog.ListStorageCredentialsRequest` dataclass. 
 * Added `next_page_token` field for `databricks.sdk.service.catalog.ListExternalLocationsResponse`, `databricks.sdk.service.catalog.ListFunctionsResponse`, `databricks.sdk.service.catalog.ListSchemasResponse` and `databricks.sdk.service.catalog.ListStorageCredentialsResponse`.
 * Added `max_results` field for `databricks.sdk.service.catalog.ListFunctionsRequest` and `databricks.sdk.service.catalog.ListSchemasRequest`.
 * Added `page_token` field for `databricks.sdk.service.catalog.ListFunctionsRequest` and `databricks.sdk.service.catalog.ListSchemasRequest`.
 * Added `omit_columns` field for `databricks.sdk.service.catalog.ListTablesRequest`.
 * Added `omit_properties` field for `databricks.sdk.service.catalog.ListTablesRequest`.
 * Added `init_scripts` field for `databricks.sdk.service.pipelines.PipelineCluster`.
 * Added `validate_only` field for `databricks.sdk.service.pipelines.StartUpdate` and `databricks.sdk.service.pipelines.UpdateInfo`.
 * Changed `create()` method for [w.dashboards](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards.html) workspace-level service . New request type is `databricks.sdk.service.sql.DashboardPostContent` dataclass.
 * Added `update()` method for [w.dashboards](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards.html) workspace-level service.
 * Added `http_headers` field for `databricks.sdk.service.sql.ExternalLink`.
 * Added `run_as_role` field for `databricks.sdk.service.sql.QueryEditContent`.
 * Added package: `databricks.sdk.service.dashboards` and `databricks.sdk.service.vectorsearch`.
 * Added dataclass: `databricks.sdk.service.catalog.ListExternalLocationsRequest`, `databricks.sdk.service.catalog.ListStorageCredentialsRequest`, `databricks.sdk.service.settings.ListPublicTokensResponse`, `databricks.sdk.service.sql.DashboardEditContent` and `databricks.sdk.service.sql.DashboardPostContent`.
 * Removed dataclass: `databricks.sdk.service.catalog.TableConstraintList` and `databricks.sdk.service.sql.CreateDashboardRequest`.

OpenAPI SHA: 0e0d4cbe87193e36c73b8b2be3b0dd0f1b013e00, Date: 2024-01-10

## 0.16.0

* Sort imports in service template ([#479](https://github.com/databricks/databricks-sdk-py/pull/479)).
* Add `py.typed` to support PEP-561 ([#483](https://github.com/databricks/databricks-sdk-py/pull/483)).
* Fixed bug in `@retried` when exception subtypes were not respected ([#484](https://github.com/databricks/databricks-sdk-py/pull/484)).
* Make `WorkspaceClient` and `AccountClient` more friendly with autospeccing ([#480](https://github.com/databricks/databricks-sdk-py/pull/480)).

API Changes:

 * Added `azure_workspace_info` field for `databricks.sdk.service.provisioning.Workspace`.
 * Added `databricks.sdk.service.provisioning.AzureWorkspaceInfo` dataclass.
 * Changed `update_config()` method for [w.serving_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/serving_endpoints.html) workspace-level service with new required argument order.
 * Changed `served_entities` field for `databricks.sdk.service.serving.EndpointCoreConfigInput` to no longer be required.
 * Changed `create()` method for [a.account_ip_access_lists](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_ip_access_lists.html) account-level service with new required argument order.
 * Changed `replace()` method for [a.account_ip_access_lists](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_ip_access_lists.html) account-level service with new required argument order.
 * Changed `update()` method for [a.account_ip_access_lists](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_ip_access_lists.html) account-level service with new required argument order.
 * Changed `create()` method for [w.ip_access_lists](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ip_access_lists.html) workspace-level service with new required argument order.
 * Changed `replace()` method for [w.ip_access_lists](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ip_access_lists.html) workspace-level service with new required argument order.
 * Changed `update()` method for [w.ip_access_lists](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ip_access_lists.html) workspace-level service with new required argument order.
 * Changed `ip_addresses` field for `databricks.sdk.service.settings.CreateIpAccessList` to no longer be required.
 * Changed `ip_addresses` field for `databricks.sdk.service.settings.ReplaceIpAccessList` to no longer be required.
 * Removed `list_id` field for `databricks.sdk.service.settings.ReplaceIpAccessList`.
 * Changed `enabled` field for `databricks.sdk.service.settings.UpdateIpAccessList` to no longer be required.
 * Changed `ip_addresses` field for `databricks.sdk.service.settings.UpdateIpAccessList` to no longer be required.
 * Changed `label` field for `databricks.sdk.service.settings.UpdateIpAccessList` to no longer be required.
 * Removed `list_id` field for `databricks.sdk.service.settings.UpdateIpAccessList`.
 * Changed `list_type` field for `databricks.sdk.service.settings.UpdateIpAccessList` to no longer be required.

OpenAPI SHA: d3853c8dee5806d04da2ae8910f273ffb35719a5, Date: 2023-12-14

## 0.15.0

Bugfixes:

* Fixed accidental rename ([#471](https://github.com/databricks/databricks-sdk-py/pull/471)).
* Fixed parsing of ISO date strings ([#473](https://github.com/databricks/databricks-sdk-py/pull/473)).


Other changes:

* Updated GCP OAuth Readme ([#464](https://github.com/databricks/databricks-sdk-py/pull/464)).
* Reference Documentation Refactoring ([#467](https://github.com/databricks/databricks-sdk-py/pull/467)).
* Installed local library when generating docs ([#469](https://github.com/databricks/databricks-sdk-py/pull/469)).
* Fixed readme links in pypi ([#472](https://github.com/databricks/databricks-sdk-py/pull/472)).
* Updated a note for installing Python SDK on Databricks Runtime 13.1+ ([#474](https://github.com/databricks/databricks-sdk-py/pull/474)).
* Updated GCP auth readme ([#470](https://github.com/databricks/databricks-sdk-py/pull/470)).


API Changes:

 * Changed `update()` method for [w.connections](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/connections.html) workspace-level service with new required argument order.
 * Added `cloudflare_api_token` field for `databricks.sdk.service.catalog.CreateStorageCredential`.
 * Added `cloudflare_api_token` field for `databricks.sdk.service.catalog.StorageCredentialInfo`.
 * Changed `name` field for `databricks.sdk.service.catalog.UpdateCatalog` to be required.
 * Added `new_name` field for `databricks.sdk.service.catalog.UpdateCatalog`.
 * Changed `name` field for `databricks.sdk.service.catalog.UpdateConnection` to no longer be required.
 * Added `new_name` field for `databricks.sdk.service.catalog.UpdateConnection`.
 * Changed `name` field for `databricks.sdk.service.catalog.UpdateExternalLocation` to be required.
 * Added `new_name` field for `databricks.sdk.service.catalog.UpdateExternalLocation`.
 * Added `new_name` field for `databricks.sdk.service.catalog.UpdateMetastore`.
 * Added `new_name` field for `databricks.sdk.service.catalog.UpdateRegisteredModelRequest`.
 * Added `new_name` field for `databricks.sdk.service.catalog.UpdateSchema`.
 * Changed `name` field for `databricks.sdk.service.catalog.UpdateStorageCredential` to be required.
 * Added `cloudflare_api_token` field for `databricks.sdk.service.catalog.UpdateStorageCredential`.
 * Added `new_name` field for `databricks.sdk.service.catalog.UpdateStorageCredential`.
 * Added `new_name` field for `databricks.sdk.service.catalog.UpdateVolumeRequestContent`.
 * Added `cloudflare_api_token` field for `databricks.sdk.service.catalog.ValidateStorageCredential`.
 * Added `databricks.sdk.service.catalog.CloudflareApiToken` dataclass.
 * Removed `continuous` field for `databricks.sdk.service.jobs.BaseRun`.
 * Removed `continuous` field for `databricks.sdk.service.jobs.Run`.
 * Changed `job_parameters` field for `databricks.sdk.service.jobs.RunJobTask` to `databricks.sdk.service.jobs.ParamPairs` dataclass.
 * Added `run_if` field for `databricks.sdk.service.jobs.SubmitTask`.
 * Added `run_job_task` field for `databricks.sdk.service.jobs.SubmitTask`.
 * Changed `update_config()` method for [w.serving_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/serving_endpoints.html) workspace-level service with new required argument order.
 * Added `put()` method for [w.serving_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/serving_endpoints.html) workspace-level service.
 * Added `rate_limits` field for `databricks.sdk.service.serving.CreateServingEndpoint`.
 * Changed `served_models` field for `databricks.sdk.service.serving.EndpointCoreConfigInput` to no longer be required.
 * Added `auto_capture_config` field for `databricks.sdk.service.serving.EndpointCoreConfigInput`.
 * Added `served_entities` field for `databricks.sdk.service.serving.EndpointCoreConfigInput`.
 * Added `auto_capture_config` field for `databricks.sdk.service.serving.EndpointCoreConfigOutput`.
 * Added `served_entities` field for `databricks.sdk.service.serving.EndpointCoreConfigOutput`.
 * Added `served_entities` field for `databricks.sdk.service.serving.EndpointCoreConfigSummary`.
 * Added `served_entities` field for `databricks.sdk.service.serving.EndpointPendingConfig`.
 * Added `extra_params` field for `databricks.sdk.service.serving.QueryEndpointInput`.
 * Added `input` field for `databricks.sdk.service.serving.QueryEndpointInput`.
 * Added `max_tokens` field for `databricks.sdk.service.serving.QueryEndpointInput`.
 * Added `messages` field for `databricks.sdk.service.serving.QueryEndpointInput`.
 * Added `n` field for `databricks.sdk.service.serving.QueryEndpointInput`.
 * Added `prompt` field for `databricks.sdk.service.serving.QueryEndpointInput`.
 * Added `stop` field for `databricks.sdk.service.serving.QueryEndpointInput`.
 * Added `stream` field for `databricks.sdk.service.serving.QueryEndpointInput`.
 * Added `temperature` field for `databricks.sdk.service.serving.QueryEndpointInput`.
 * Changed `predictions` field for `databricks.sdk.service.serving.QueryEndpointResponse` to no longer be required.
 * Added `choices` field for `databricks.sdk.service.serving.QueryEndpointResponse`.
 * Added `created` field for `databricks.sdk.service.serving.QueryEndpointResponse`.
 * Added `data` field for `databricks.sdk.service.serving.QueryEndpointResponse`.
 * Added `id` field for `databricks.sdk.service.serving.QueryEndpointResponse`.
 * Added `model` field for `databricks.sdk.service.serving.QueryEndpointResponse`.
 * Added `object` field for `databricks.sdk.service.serving.QueryEndpointResponse`.
 * Added `usage` field for `databricks.sdk.service.serving.QueryEndpointResponse`.
 * Changed `workload_size` field for `databricks.sdk.service.serving.ServedModelInput` to `databricks.sdk.service.serving.ServedModelInputWorkloadSize` dataclass.
 * Changed `workload_type` field for `databricks.sdk.service.serving.ServedModelInput` to `databricks.sdk.service.serving.ServedModelInputWorkloadType` dataclass.
 * Added `task` field for `databricks.sdk.service.serving.ServingEndpoint`.
 * Added `task` field for `databricks.sdk.service.serving.ServingEndpointDetailed`.
 * Added `databricks.sdk.service.serving.Ai21LabsConfig` dataclass.
 * Added `databricks.sdk.service.serving.AnthropicConfig` dataclass.
 * Added `databricks.sdk.service.serving.AutoCaptureConfigInput` dataclass.
 * Added `databricks.sdk.service.serving.AutoCaptureConfigOutput` dataclass.
 * Added `databricks.sdk.service.serving.AutoCaptureState` dataclass.
 * Added `databricks.sdk.service.serving.AwsBedrockConfig` dataclass.
 * Added `databricks.sdk.service.serving.AwsBedrockConfigBedrockProvider` dataclass.
 * Added `databricks.sdk.service.serving.ChatMessage` dataclass.
 * Added `databricks.sdk.service.serving.ChatMessageRole` dataclass.
 * Added `databricks.sdk.service.serving.CohereConfig` dataclass.
 * Added `databricks.sdk.service.serving.DatabricksModelServingConfig` dataclass.
 * Added `databricks.sdk.service.serving.EmbeddingsV1ResponseEmbeddingElement` dataclass.
 * Added `databricks.sdk.service.serving.EmbeddingsV1ResponseEmbeddingElementObject` dataclass.
 * Added `databricks.sdk.service.serving.ExternalModel` dataclass.
 * Added `databricks.sdk.service.serving.ExternalModelConfig` dataclass.
 * Added `databricks.sdk.service.serving.ExternalModelProvider` dataclass.
 * Added `databricks.sdk.service.serving.ExternalModelUsageElement` dataclass.
 * Added `databricks.sdk.service.serving.FoundationModel` dataclass.
 * Added `databricks.sdk.service.serving.OpenAiConfig` dataclass.
 * Added `databricks.sdk.service.serving.PaLmConfig` dataclass.
 * Added `databricks.sdk.service.serving.PayloadTable` dataclass.
 * Added `databricks.sdk.service.serving.PutRequest` dataclass.
 * Added `databricks.sdk.service.serving.PutResponse` dataclass.
 * Added `databricks.sdk.service.serving.QueryEndpointResponseObject` dataclass.
 * Added `databricks.sdk.service.serving.RateLimit` dataclass.
 * Added `databricks.sdk.service.serving.RateLimitKey` dataclass.
 * Added `databricks.sdk.service.serving.RateLimitRenewalPeriod` dataclass.
 * Added `databricks.sdk.service.serving.ServedEntityInput` dataclass.
 * Added `databricks.sdk.service.serving.ServedEntityOutput` dataclass.
 * Added `databricks.sdk.service.serving.ServedEntitySpec` dataclass.
 * Added `databricks.sdk.service.serving.ServedModelInputWorkloadSize` dataclass.
 * Added `databricks.sdk.service.serving.ServedModelInputWorkloadType` dataclass.
 * Added `databricks.sdk.service.serving.V1ResponseChoiceElement` dataclass.
 * Removed [a.account_network_policy](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_network_policy.html) account-level service.
 * Removed `databricks.sdk.service.settings.AccountNetworkPolicyMessage` dataclass.
 * Removed `databricks.sdk.service.settings.DeleteAccountNetworkPolicyRequest` dataclass.
 * Removed `databricks.sdk.service.settings.DeleteAccountNetworkPolicyResponse` dataclass.
 * Removed `databricks.sdk.service.settings.ReadAccountNetworkPolicyRequest` dataclass.
 * Removed `databricks.sdk.service.settings.UpdateAccountNetworkPolicyRequest` dataclass.
 * Removed `name` field for `databricks.sdk.service.sharing.UpdateCleanRoom`.
 * Changed `name` field for `databricks.sdk.service.sharing.UpdateProvider` to be required.
 * Added `new_name` field for `databricks.sdk.service.sharing.UpdateProvider`.
 * Changed `name` field for `databricks.sdk.service.sharing.UpdateRecipient` to be required.
 * Added `new_name` field for `databricks.sdk.service.sharing.UpdateRecipient`.
 * Changed `name` field for `databricks.sdk.service.sharing.UpdateShare` to be required.
 * Added `new_name` field for `databricks.sdk.service.sharing.UpdateShare`.
 * Added `statement_ids` field for `databricks.sdk.service.sql.QueryFilter`.
 * Added `databricks.sdk.service.sql.StatementId` dataclass.

OpenAPI SHA: 63caa3cb0c05045e81d3dcf2451fa990d8670f36, Date: 2023-12-12

## 0.14.0

Major changes:
* GCP Auth is now supported in the Python SDK. To use Google credentials-based authentication, specify your Default Application Credentials in the `GOOGLE_CREDENTIALS` environment variable or corresponding `google_credentials` parameter in `Config` or the client constructors. You may provide either the path to the file containing your credentials or the credentials themselves serialized as JSON. To use Google impersonation, specify the service principal to impersonate in the `DATABRICKS_GOOGLE_SERVICE_ACCOUNT` environment variable or the corresponding `google_service_account` parameter in `Config` or the client constructors. See [#444](https://github.com/databricks/databricks-sdk-py/pull/444) for the changes.

Bug fixes:
* Fix flask app example ([#445](https://github.com/databricks/databricks-sdk-py/pull/445)).
* Fix deserialization of repeated enums ([#450](https://github.com/databricks/databricks-sdk-py/pull/450), [#452](https://github.com/databricks/databricks-sdk-py/pull/452)).
* Capture stdout and stderr separately when calling Azure CLI ([#460](https://github.com/databricks/databricks-sdk-py/pull/460)).

Other changes:
* Change the name of retries logger to `databricks.sdk.retries` ([#453](https://github.com/databricks/databricks-sdk-py/pull/453)).

API Changes:

 * Added `pipeline_id` field for `databricks.sdk.service.catalog.TableInfo`.
 * Added `enable_predictive_optimization` field for `databricks.sdk.service.catalog.UpdateCatalog` and `databricks.sdk.service.catalog.UpdateSchema`.
 * Removed `databricks.sdk.service.catalog.UpdatePredictiveOptimization` and `databricks.sdk.service.catalog.UpdatePredictiveOptimizationResponse` dataclasses.
 * Removed `enable_optimization()` method for [w.metastores](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/metastores.html) workspace-level service.
 * Added `description` field for `databricks.sdk.service.jobs.CreateJob`  and `databricks.sdk.service.jobs.JobSettings`.
 * Added `list_network_connectivity_configurations()` and `list_private_endpoint_rules()` methods for [a.network_connectivity](https://databricks-sdk-py.readthedocs.io/en/latest/account/network_connectivity.html) account-level service.
 * Added `databricks.sdk.service.settings.ListNccAzurePrivateEndpointRulesResponse`, `databricks.sdk.service.settings.ListNetworkConnectivityConfigurationsRequest`, `databricks.sdk.service.settings.ListNetworkConnectivityConfigurationsResponse`, and `databricks.sdk.service.settings.ListPrivateEndpointRulesRequest` dataclasses.

Internal changes:

* Make ucws tests skipped when DATABRICKS_ACCOUNT_ID is present ([#448](https://github.com/databricks/databricks-sdk-py/pull/448)).

OpenAPI SHA: 22f09783eb8a84d52026f856be3b2068f9498db3, Date: 2023-11-23
Dependency updates:

 * Introduced "google-auth" dependency to support Google authentication.


## 0.13.0

* Introduce more specific exceptions, like `NotFound`, `AlreadyExists`, `BadRequest`, `PermissionDenied`, `InternalError`, and others ([#376](https://github.com/databricks/databricks-sdk-py/pull/376)). This makes it easier to handle errors thrown by the Databricks API. Instead of catching `DatabricksError` and checking the error_code field, you can catch one of these subtypes of `DatabricksError`, which is more ergonomic and removes the need to rethrow exceptions that you don't want to catch. For example:
```python
try:
  return (self._ws
    .permissions
    .get(object_type, object_id))
except DatabricksError as e:
  if e.error_code in [
    "RESOURCE_DOES_NOT_EXIST",
    "RESOURCE_NOT_FOUND",
    "PERMISSION_DENIED",
    "FEATURE_DISABLED",
    "BAD_REQUEST"]:
    logger.warning(...)
    return None
  raise RetryableError(...) from e
```
can be replaced with
```python
try:
  return (self._ws
    .permissions
    .get(object_type, object_id))
except PermissionDenied, FeatureDisabled:
  logger.warning(...)
  return None
except NotFound:
  raise RetryableError(...)
```
* Paginate all SCIM list requests in the SDK ([#440](https://github.com/databricks/databricks-sdk-py/pull/440)). This change ensures that SCIM list() APIs use a default limit of 100 resources, leveraging SCIM's offset + limit pagination to batch requests to the Databricks API.
* Added taskValues support in remoteDbUtils ([#406](https://github.com/databricks/databricks-sdk-py/pull/406)).
* Added more detailed error message on default credentials not found error ([#419](https://github.com/databricks/databricks-sdk-py/pull/419)).
* Request management token via Azure CLI only for Service Principals and not human users ([#408](https://github.com/databricks/databricks-sdk-py/pull/408)).

API Changes:

 * Fixed `create()` method for [w.functions](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/functions.html) workspace-level service and corresponding `databricks.sdk.service.catalog.CreateFunction` and `databricks.sdk.service.catalog.FunctionInfo` dataclasses.
 * Changed `create()` method for [w.metastores](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/metastores.html) workspace-level service with new required argument order.
 * Changed `storage_root` field for `databricks.sdk.service.catalog.CreateMetastore` to be optional.
 * Added `skip_validation` field for `databricks.sdk.service.catalog.UpdateExternalLocation`.
 * Added `libraries` field for `databricks.sdk.service.compute.CreatePolicy`, `databricks.sdk.service.compute.EditPolicy` and `databricks.sdk.service.compute.Policy`.
 * Added `init_scripts` field for `databricks.sdk.service.compute.EventDetails`.
 * Added `file` field for `databricks.sdk.service.compute.InitScriptInfo`.
 * Added `zone_id` field for `databricks.sdk.service.compute.InstancePoolGcpAttributes`.
 * Added several dataclasses related to init scripts.
 * Added `databricks.sdk.service.compute.LocalFileInfo` dataclass.
 * Replaced `ui_state` field with `edit_mode` for `databricks.sdk.service.jobs.CreateJob` and `databricks.sdk.service.jobs.JobSettings`.
 * Replaced `databricks.sdk.service.jobs.CreateJobUiState` dataclass with `databricks.sdk.service.jobs.CreateJobEditMode`.
 * Added `include_resolved_values` field for `databricks.sdk.service.jobs.GetRunRequest`.
 * Replaced `databricks.sdk.service.jobs.JobSettingsUiState` dataclass with `databricks.sdk.service.jobs.JobSettingsEditMode`.
 * Removed [a.o_auth_enrollment](https://databricks-sdk-py.readthedocs.io/en/latest/account/o_auth_enrollment.html) account-level service. This was only used to aid in OAuth enablement during the public preview of OAuth. OAuth is now enabled for all AWS E2 accounts, so usage of this API is no longer needed.
 * Added `network_connectivity_config_id` field for `databricks.sdk.service.provisioning.UpdateWorkspaceRequest`.
 * Added [a.network_connectivity](https://databricks-sdk-py.readthedocs.io/en/latest/account/network_connectivity.html) account-level service.
 * Added `string_shared_as` field for `databricks.sdk.service.sharing.SharedDataObject`.

Internal changes:

* Added regression question to issue template ([#414](https://github.com/databricks/databricks-sdk-py/pull/414)).
* Made test_auth no longer fail if you have a default profile setup ([#426](https://github.com/databricks/databricks-sdk-py/pull/426)).

OpenAPI SHA: d136ad0541f036372601bad9a4382db06c3c912d, Date: 2023-11-14

## 0.12.0

* Retry on all 429 and 503, even when missing Retry-After header ([#402](https://github.com/databricks/databricks-sdk-py/pull/402)).
* Add support for tokenless authentication for GitHub Actions configured with OpenID Connect with Azure User Managed Identity (or Service Principal) ([#385](https://github.com/databricks/databricks-sdk-py/pull/385)).
* Reduce redundant warning messages in azure-cli credential provider ([#410](https://github.com/databricks/databricks-sdk-py/pull/410)).

API Changes:

 * Added `attributes`, `count`, `excluded_attributes`, `filter`, `sort_by`, `sort_order`, and `start_index` fields for `databricks.sdk.service.iam.GetAccountUserRequest` and `databricks.sdk.service.iam.GetUserRequest`.
 * Added `schemas` field for `databricks.sdk.service.iam.Group`, `databricks.sdk.service.iam.ListGroupsResponse`, `databricks.sdk.service.iam.ListServicePrincipalResponse`, `databricks.sdk.service.iam.ListUsersResponse`, `databricks.sdk.service.iam.ServicePrincipal`, and `databricks.sdk.service.iam.User`.
 * Added `databricks.sdk.service.iam.GetSortOrder`, `databricks.sdk.service.iam.GroupSchema`, `databricks.sdk.service.iam.ListResponseSchema`, `databricks.sdk.service.iam.ServicePrincipalSchema`, and `databricks.sdk.service.iam.UserSchema` dataclasses.
 * Added `webhook_notifications` field for `databricks.sdk.service.jobs.SubmitTask`.
 * Added [w.apps](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/apps.html) workspace-level service and related dataclasses
 * Added [a.account_network_policy](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_network_policy.html) account-level service and related dataclasses.

OpenAPI SHA: 5903bb39137fd76ac384b2044e425f9c56840e00, Date: 2023-10-23

## 0.11.0

* Added Python 3.12 to project classifiers ([#381](https://github.com/databricks/databricks-sdk-py/pull/381)).
* Fix serialization issues for generated resources ([#382](https://github.com/databricks/databricks-sdk-py/pull/382)).
* Fix select spark version in staging ([#388](https://github.com/databricks/databricks-sdk-py/pull/388)).
* Adjust token expiry window to 40 seconds because of Azure ([#392](https://github.com/databricks/databricks-sdk-py/pull/392)).
* Add retries on `RPC token bucket limit has been exceeded` ([#395](https://github.com/databricks/databricks-sdk-py/pull/395)).
* Regenerate to fix template drift ([#398](https://github.com/databricks/databricks-sdk-py/pull/398)).
* Update OpenAPI spec to 12 Oct 2023 ([#399](https://github.com/databricks/databricks-sdk-py/pull/399)).

Internal:

* GitHub OIDC publishing ([#386](https://github.com/databricks/databricks-sdk-py/pull/386)).
* Move Release Pipeline to OIDC ([#387](https://github.com/databricks/databricks-sdk-py/pull/387)).

API Changes:

 * Changed `download()` method for [a.billable_usage](https://databricks-sdk-py.readthedocs.io/en/latest/account/billable_usage.html) account-level service to start returning `databricks.sdk.service.billing.DownloadResponse` dataclass.
 * Added `databricks.sdk.service.billing.DownloadResponse` dataclass.
 * Changed `delete()` method for [a.account_storage_credentials](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_storage_credentials.html) account-level service with new required argument order.
 * Changed `get()` method for [a.account_storage_credentials](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_storage_credentials.html) account-level service with new required argument order.
 * Changed `update()` method for [a.account_storage_credentials](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_storage_credentials.html) account-level service with new required argument order.
 * Added `get_bindings()` method for [w.workspace_bindings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/workspace_bindings.html) workspace-level service.
 * Added `update_bindings()` method for [w.workspace_bindings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/workspace_bindings.html) workspace-level service.
 * Removed `name` field for `databricks.sdk.service.catalog.AccountsUpdateStorageCredential`.
 * Added `storage_credential_name` field for `databricks.sdk.service.catalog.AccountsUpdateStorageCredential`.
 * Removed `name` field for `databricks.sdk.service.catalog.DeleteAccountStorageCredentialRequest`.
 * Added `storage_credential_name` field for `databricks.sdk.service.catalog.DeleteAccountStorageCredentialRequest`.
 * Removed `name` field for `databricks.sdk.service.catalog.GetAccountStorageCredentialRequest`.
 * Added `storage_credential_name` field for `databricks.sdk.service.catalog.GetAccountStorageCredentialRequest`.
 * Added `owner` field for `databricks.sdk.service.catalog.UpdateConnection`.
 * Added `databricks.sdk.service.catalog.GetBindingsRequest` dataclass.
 * Added `databricks.sdk.service.catalog.UpdateWorkspaceBindingsParameters` dataclass.
 * Added `databricks.sdk.service.catalog.WorkspaceBinding` dataclass.
 * Added `databricks.sdk.service.catalog.WorkspaceBindingBindingType` dataclass.
 * Added `databricks.sdk.service.catalog.WorkspaceBindingsResponse` dataclass.
 * Added `spec` field for `databricks.sdk.service.compute.ClusterDetails`.
 * Added `apply_policy_default_values` field for `databricks.sdk.service.compute.ClusterSpec`.
 * Removed `aws_attributes` field for `databricks.sdk.service.compute.EditInstancePool`.
 * Removed `azure_attributes` field for `databricks.sdk.service.compute.EditInstancePool`.
 * Removed `disk_spec` field for `databricks.sdk.service.compute.EditInstancePool`.
 * Removed `enable_elastic_disk` field for `databricks.sdk.service.compute.EditInstancePool`.
 * Removed `gcp_attributes` field for `databricks.sdk.service.compute.EditInstancePool`.
 * Removed `preloaded_docker_images` field for `databricks.sdk.service.compute.EditInstancePool`.
 * Removed `preloaded_spark_versions` field for `databricks.sdk.service.compute.EditInstancePool`.
 * Added `deployment` field for `databricks.sdk.service.jobs.CreateJob`.
 * Added `ui_state` field for `databricks.sdk.service.jobs.CreateJob`.
 * Added `deployment` field for `databricks.sdk.service.jobs.JobSettings`.
 * Added `ui_state` field for `databricks.sdk.service.jobs.JobSettings`.
 * Removed `condition_task` field for `databricks.sdk.service.jobs.RunOutput`.
 * Added `webhook_notifications` field for `databricks.sdk.service.jobs.Task`.
 * Added `databricks.sdk.service.jobs.CreateJobUiState` dataclass.
 * Added `databricks.sdk.service.jobs.JobDeployment` dataclass.
 * Added `databricks.sdk.service.jobs.JobDeploymentKind` dataclass.
 * Added `databricks.sdk.service.jobs.JobSettingsUiState` dataclass.
 * Added `workload_type` field for `databricks.sdk.service.serving.ServedModelInput`.
 * Added `workload_type` field for `databricks.sdk.service.serving.ServedModelOutput`.
 * Removed [a.account_network_policy](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_network_policy.html) account-level service.
 * Changed `list()` method for [w.ip_access_lists](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ip_access_lists.html) workspace-level service to return `databricks.sdk.service.settings.ListIpAccessListResponse` dataclass.
 * Removed `databricks.sdk.service.settings.AccountNetworkPolicyMessage` dataclass.
 * Removed `databricks.sdk.service.settings.DeleteAccountNetworkPolicyRequest` dataclass.
 * Removed `databricks.sdk.service.settings.DeleteAccountNetworkPolicyResponse` dataclass.
 * Removed `ip_access_lists` field for `databricks.sdk.service.settings.GetIpAccessListResponse`.
 * Added `ip_access_list` field for `databricks.sdk.service.settings.GetIpAccessListResponse`.
 * Removed `databricks.sdk.service.settings.ReadAccountNetworkPolicyRequest` dataclass.
 * Removed `databricks.sdk.service.settings.UpdateAccountNetworkPolicyRequest` dataclass.
 * Added `databricks.sdk.service.settings.ListIpAccessListResponse` dataclass.

OpenAPI SHA: 493a76554afd3afdd15dc858773d01643f80352a, Date: 2023-10-12

## 0.10.0

* Respect `retry_timeout_seconds` config setting and align retry implementation with Go SDK ([#337](https://github.com/databricks/databricks-sdk-py/pull/337)).

Breaking API Changes:

 * Changed `list()` method for [a.account_metastore_assignments](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_metastore_assignments.html) account-level service to return `databricks.sdk.service.catalog.ListAccountMetastoreAssignmentsResponse` dataclass.
 * Removed `owner` field for `databricks.sdk.service.catalog.CreateConnection`. Instead, use the `owner` field of `UpdateConnection`.
 * Removed `options` field for `databricks.sdk.service.catalog.UpdateCatalog`.
 * Changed `job_parameters` field for `databricks.sdk.service.jobs.RunNow` to `databricks.sdk.service.jobs.ParamPairs` dataclass.
 * Changed `query()` method for [w.serving_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/serving_endpoints.html) workspace-level service . New request type is `databricks.sdk.service.serving.QueryEndpointInput` dataclass.
 * Renamed `databricks.sdk.service.serving.QueryRequest` dataclass to `QueryEndpointInput`.
 * Changed `list()` method for [w.clean_rooms](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/clean_rooms.html) workspace-level service to require request of `databricks.sdk.service.sharing.ListCleanRoomsRequest` dataclass.

API Changes:

 * Added `databricks.sdk.service.catalog.ListAccountMetastoreAssignmentsResponse` dataclass.
 * Added `job_parameters` field for `databricks.sdk.service.jobs.RepairRun`.
 * Added `job_parameters` field for `databricks.sdk.service.jobs.RunParameters`.
 * Added `notifications` field for `databricks.sdk.service.pipelines.CreatePipeline`.
 * Added `notifications` field for `databricks.sdk.service.pipelines.EditPipeline`.
 * Added `notifications` field for `databricks.sdk.service.pipelines.PipelineSpec`.
 * Added `databricks.sdk.service.pipelines.Notifications` dataclass.
 * Added `databricks.sdk.service.serving.DataframeSplitInput` dataclass.
 * Added [w.settings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings.html) workspace-level service.
 * Added `databricks.sdk.service.settings.DefaultNamespaceSetting` dataclass.
 * Added `databricks.sdk.service.settings.DeleteDefaultWorkspaceNamespaceRequest` dataclass.
 * Added `databricks.sdk.service.settings.DeleteDefaultWorkspaceNamespaceResponse` dataclass.
 * Added `databricks.sdk.service.settings.ReadDefaultWorkspaceNamespaceRequest` dataclass.
 * Added `databricks.sdk.service.settings.StringMessage` dataclass.
 * Added `databricks.sdk.service.settings.UpdateDefaultWorkspaceNamespaceRequest` dataclass.
 * Added `next_page_token` field for `databricks.sdk.service.sharing.ListCleanRoomsResponse`.
 * Added `databricks.sdk.service.sharing.ListCleanRoomsRequest` dataclass.

OpenAPI SHA: bcbf6e851e3d82fd910940910dd31c10c059746c, Date: 2023-10-02

## 0.9.0

* Don't try to import runtime_auth when not in runtime ([#327](https://github.com/databricks/databricks-sdk-py/pull/327)).
* Handled Azure authentication when WorkspaceResourceID is provided ([#328](https://github.com/databricks/databricks-sdk-py/pull/328)).
* Added ErrorInfo to API errors ([#347](https://github.com/databricks/databricks-sdk-py/pull/347)).
* Fixed eager default argument evaluation in `DatabricksError` ([#353](https://github.com/databricks/databricks-sdk-py/pull/353)).
* Fixed code generation of primitive types ([#354](https://github.com/databricks/databricks-sdk-py/pull/354)).
* Updated SDK to changes in OpenAPI specification ([#355](https://github.com/databricks/databricks-sdk-py/pull/355)).

API Changes:

 * Changed `list()` method for [a.account_metastore_assignments](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_metastore_assignments.html) account-level service to return `databricks.sdk.service.catalog.WorkspaceIdList` dataclass.
 * Changed `artifact_matchers` field for `databricks.sdk.service.catalog.ArtifactAllowlistInfo` to `databricks.sdk.service.catalog.ArtifactMatcherList` dataclass.
 * Changed `artifact_matchers` field for `databricks.sdk.service.catalog.SetArtifactAllowlist` to `databricks.sdk.service.catalog.ArtifactMatcherList` dataclass.
 * Added `databricks.sdk.service.catalog.WorkspaceId` dataclass.
 * Changed `cancel_all_runs()` method for [w.jobs](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/jobs.html) workspace-level service with new required argument order.
 * Changed `job_id` field for `databricks.sdk.service.jobs.CancelAllRuns` to no longer be required.
 * Added `all_queued_runs` field for `databricks.sdk.service.jobs.CancelAllRuns`.
 * Added `queue` field for `databricks.sdk.service.jobs.CreateJob`.
 * Added `queue` field for `databricks.sdk.service.jobs.JobSettings`.
 * Added `queue` field for `databricks.sdk.service.jobs.RunNow`.
 * Added `queue_reason` field for `databricks.sdk.service.jobs.RunState`.
 * Added `queue_duration` field for `databricks.sdk.service.jobs.RunTask`.
 * Added `queue` field for `databricks.sdk.service.jobs.SubmitRun`.
 * Added `databricks.sdk.service.jobs.QueueSettings` dataclass.
 * Added [a.o_auth_published_apps](https://databricks-sdk-py.readthedocs.io/en/latest/account/o_auth_published_apps.html) account-level service.
 * Added `databricks.sdk.service.oauth2.GetPublishedAppsOutput` dataclass.
 * Added `databricks.sdk.service.oauth2.ListOAuthPublishedAppsRequest` dataclass.
 * Added `databricks.sdk.service.oauth2.PublishedAppOutput` dataclass.
 * Added `patch()` method for [w.serving_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/serving_endpoints.html) workspace-level service.
 * Added `tags` field for `databricks.sdk.service.serving.CreateServingEndpoint`.
 * Added `tags` field for `databricks.sdk.service.serving.ServingEndpoint`.
 * Added `tags` field for `databricks.sdk.service.serving.ServingEndpointDetailed`.
 * Added `databricks.sdk.service.serving.EndpointTag` dataclass.
 * Added `databricks.sdk.service.serving.PatchServingEndpointTags` dataclass.
 * Added [w.credentials_manager](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/credentials_manager.html) workspace-level service.
 * Added `databricks.sdk.service.settings.ExchangeToken` dataclass.
 * Added `databricks.sdk.service.settings.ExchangeTokenRequest` dataclass.
 * Added `databricks.sdk.service.settings.ExchangeTokenResponse` dataclass.
 * Added `databricks.sdk.service.settings.PartitionId` dataclass.
 * Added `databricks.sdk.service.settings.TokenType` dataclass.
 * Changed `execute_statement()` method for [w.statement_execution](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/statement_execution.html) workspace-level service with new required argument order.
 * Added `empty_result_state` field for `databricks.sdk.service.sql.AlertOptions`.
 * Removed `databricks.sdk.service.sql.ChunkInfo` dataclass.
 * Changed `on_wait_timeout` field for `databricks.sdk.service.sql.ExecuteStatementRequest` to `databricks.sdk.service.sql.ExecuteStatementRequestOnWaitTimeout` dataclass.
 * Changed `statement` field for `databricks.sdk.service.sql.ExecuteStatementRequest` to be required.
 * Changed `warehouse_id` field for `databricks.sdk.service.sql.ExecuteStatementRequest` to be required.
 * Changed `chunks` field for `databricks.sdk.service.sql.ResultManifest` to `databricks.sdk.service.sql.BaseChunkInfoList` dataclass.
 * Added `truncated` field for `databricks.sdk.service.sql.ResultManifest`.
 * Removed `databricks.sdk.service.sql.TimeoutAction` dataclass.
 * Added `databricks.sdk.service.sql.AlertOptionsEmptyResultState` dataclass.
 * Added `databricks.sdk.service.sql.BaseChunkInfo` dataclass.
 * Added `databricks.sdk.service.sql.ExecuteStatementRequestOnWaitTimeout` dataclass.

OpenAPI SHA: b52a3b410976501f08f76ca0b355fb2dca876953, Date: 2023-09-15

## 0.8.0

* Fixed redeclared `test_streaming_response_read_partial` test ([#335](https://github.com/databricks/databricks-sdk-py/pull/335)).
* Fixed `Incorrect type` warning ([#336](https://github.com/databricks/databricks-sdk-py/pull/336)).
* Add notebook installation instructions ([#334](https://github.com/databricks/databricks-sdk-py/pull/334)).

API Changes:

* Renamed permissions APIs to no longer include the service name, for example:
  * `get_job_permission_levels` -> `get_permission_levels`
  * `get_job_permissions` -> `get_permissions`
  * `set_job_permissions` -> `set_permissions`
  * `update_job_permissions` -> `update_permissions`
* Changed `create()` method for [w.volumes](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/volumes.html) workspace-level service with new required argument order.
* Added `supports_elastic_disk` field for `databricks.sdk.service.compute.NodeType`.
* Changed `create()` method for [w.dashboards](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards.html) workspace-level service with new required argument order.
* Added [w.dashboard_widgets](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboard_widgets.html) workspace-level service.
* Added [w.query_visualizations](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/query_visualizations.html) workspace-level service.
* Changed `name` field for `databricks.sdk.service.sql.CreateDashboardRequest` to be required.
* Added `dashboard_filters_enabled` field for `databricks.sdk.service.sql.CreateDashboardRequest`.
* Added `run_as_role` field for `databricks.sdk.service.sql.CreateDashboardRequest`.
* Added `run_as_role` field for `databricks.sdk.service.sql.Query`.
* Added `run_as_role` field for `databricks.sdk.service.sql.QueryPostContent`.
* Removed `dashboard_id` field for `databricks.sdk.service.sql.WidgetOptions`.
* Changed `position` field for `databricks.sdk.service.sql.WidgetOptions` to `databricks.sdk.service.sql.WidgetPosition` dataclass.
* Removed `text` field for `databricks.sdk.service.sql.WidgetOptions`.
* Added `description` field for `databricks.sdk.service.sql.WidgetOptions`.
* Added `title` field for `databricks.sdk.service.sql.WidgetOptions`.
* Added `databricks.sdk.service.sql.CreateQueryVisualizationRequest` dataclass.
* Added `databricks.sdk.service.sql.CreateWidget` dataclass.
* Added `databricks.sdk.service.sql.DeleteDashboardWidgetRequest` dataclass.
* Added `databricks.sdk.service.sql.DeleteQueryVisualizationRequest` dataclass.
* Added `databricks.sdk.service.sql.RunAsRole` dataclass.
* Added `databricks.sdk.service.sql.WidgetPosition` dataclass.

OpenAPI SHA: 09a7fa63d9ae243e5407941f200960ca14d48b07, Date: 2023-09-04
## 0.7.1

* Improve file download performance ([#319](https://github.com/databricks/databricks-sdk-py/pull/319)).


## 0.7.0

* Added support for GZIP'ed streaming responses ([#306](https://github.com/databricks/databricks-sdk-py/pull/306)).
* Added support for per-method request headers to ApiClient ([#302](https://github.com/databricks/databricks-sdk-py/pull/302)).
* Added support for BinaryIO for streaming request and response bodies ([#303](https://github.com/databricks/databricks-sdk-py/pull/303)).
* Added a link to the API reference ([#311](https://github.com/databricks/databricks-sdk-py/pull/311)).
* Check workspaceUrl explicitly in runtime repl auth ([#312](https://github.com/databricks/databricks-sdk-py/pull/312)).

Breaking Changes:
 * Added support for the Files API (using application/octet-stream) in OpenAPI. The names of parameters have changed from `src` to `contents`, and `w.files.download()` now returns a `files.DownloadResponse`, whose `contents` field is a `BinaryIO` object. When reading a download, the user must explicitly close this object to allow the connection to return to the connection pool.

Breaking API Changes:
 * Changed `list()` method for [a.account_storage_credentials](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_storage_credentials.html) account-level service to return `databricks.sdk.service.catalog.StorageCredentialInfoList` dataclass.
 * Removed [w.securable_tags](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/securable_tags.html) workspace-level service and all associated classes.
 * Removed [w.subentity_tags](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/subentity_tags.html) workspace-level service and all associated classes.
 * Removed `instance_pool_fleet_attributes` field for `databricks.sdk.service.compute.CreateInstancePool`.
 * Removed `instance_pool_fleet_attributes` field for `databricks.sdk.service.compute.EditInstancePool`.
 * Removed `databricks.sdk.service.compute.FleetLaunchTemplateOverride` dataclass.
 * Removed `databricks.sdk.service.compute.FleetOnDemandOption` dataclass.
 * Removed `databricks.sdk.service.compute.FleetOnDemandOptionAllocationStrategy` dataclass.
 * Removed `databricks.sdk.service.compute.FleetSpotOption` dataclass.
 * Removed `databricks.sdk.service.compute.FleetSpotOptionAllocationStrategy` dataclass.
 * Removed `instance_pool_fleet_attributes` field for `databricks.sdk.service.compute.GetInstancePool`.
 * Removed `instance_pool_fleet_attributes` field for `databricks.sdk.service.compute.InstancePoolAndStats`.
 * Removed `databricks.sdk.service.compute.InstancePoolFleetAttributes` dataclass.
 * Changed `get_by_name()` method for [w.experiments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/experiments.html) workspace-level service to return `databricks.sdk.service.ml.GetExperimentResponse` dataclass.
 * Changed `get_experiment()` method for [w.experiments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/experiments.html) workspace-level service to return `databricks.sdk.service.ml.GetExperimentResponse` dataclass.
 * Renamed `databricks.sdk.service.ml.GetExperimentByNameResponse` dataclass to `databricks.sdk.service.ml.GetExperimentResponse`.
 * Renamed `databricks.sdk.service.catalog.ProvisioningState` to `databricks.sdk.service.catalog.ProvisioningInfoState` dataclass.

API Changes:
 * Added [w.model_versions](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/model_versions.html) workspace-level service.
 * Added [w.registered_models](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/registered_models.html) workspace-level service.
 * Added `browse_only` field for `databricks.sdk.service.catalog.CatalogInfo`.
 * Added `full_name` field for `databricks.sdk.service.catalog.CatalogInfo`.
 * Added `provisioning_info` field for `databricks.sdk.service.catalog.CatalogInfo`.
 * Added `securable_kind` field for `databricks.sdk.service.catalog.CatalogInfo`.
 * Added `securable_type` field for `databricks.sdk.service.catalog.CatalogInfo`.
 * Added `provisioning_info` field for `databricks.sdk.service.catalog.ConnectionInfo`.
 * Added `options` field for `databricks.sdk.service.catalog.CreateCatalog`.
 * Added `options` field for `databricks.sdk.service.catalog.UpdateCatalog`.
 * Added `databricks.sdk.service.catalog.CatalogInfoSecurableKind` dataclass.
 * Added `databricks.sdk.service.catalog.CreateRegisteredModelRequest` dataclass.
 * Added `databricks.sdk.service.catalog.DeleteAliasRequest` dataclass.
 * Added `databricks.sdk.service.catalog.DeleteModelVersionRequest` dataclass.
 * Added `databricks.sdk.service.catalog.DeleteRegisteredModelRequest` dataclass.
 * Added `databricks.sdk.service.catalog.GetByAliasRequest` dataclass.
 * Added `databricks.sdk.service.catalog.GetModelVersionRequest` dataclass.
 * Added `databricks.sdk.service.catalog.GetRegisteredModelRequest` dataclass.
 * Added `databricks.sdk.service.catalog.ListModelVersionsRequest` dataclass.
 * Added `databricks.sdk.service.catalog.ListModelVersionsResponse` dataclass.
 * Added `databricks.sdk.service.catalog.ListRegisteredModelsRequest` dataclass.
 * Added `databricks.sdk.service.catalog.ListRegisteredModelsResponse` dataclass.
 * Added `databricks.sdk.service.catalog.ModelVersionInfo` dataclass.
 * Added `databricks.sdk.service.catalog.ModelVersionInfoStatus` dataclass.
 * Added `databricks.sdk.service.catalog.ProvisioningInfo` dataclass.
 * Added `databricks.sdk.service.catalog.RegisteredModelAlias` dataclass.
 * Added `databricks.sdk.service.catalog.RegisteredModelInfo` dataclass.
 * Added `databricks.sdk.service.catalog.SetRegisteredModelAliasRequest` dataclass.
 * Added `databricks.sdk.service.catalog.UpdateModelVersionRequest` dataclass.
 * Added `databricks.sdk.service.catalog.UpdateRegisteredModelRequest` dataclass.
 * Added `volumes` field for `databricks.sdk.service.compute.InitScriptInfo`.
 * Added `databricks.sdk.service.compute.VolumesStorageInfo` dataclass.
 * Added [w.files](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/files.html) workspace-level service.
 * Added `databricks.sdk.service.files.DeleteFileRequest` dataclass.
 * Added `databricks.sdk.service.files.DownloadRequest` dataclass.
 * Added `databricks.sdk.service.files.DownloadResponse` dataclass.
 * Added `databricks.sdk.service.files.UploadRequest` dataclass.
 * Added `custom_tags` field for `databricks.sdk.service.provisioning.CreateWorkspaceRequest`.
 * Added `custom_tags` field for `databricks.sdk.service.provisioning.UpdateWorkspaceRequest`.
 * Added `custom_tags` field for `databricks.sdk.service.provisioning.Workspace`.
 * Added `databricks.sdk.service.provisioning.CustomTags` dataclass.
 * Added `parameters` field for `databricks.sdk.service.sql.ExecuteStatementRequest`.
 * Added `row_limit` field for `databricks.sdk.service.sql.ExecuteStatementRequest`.
 * Added `databricks.sdk.service.sql.StatementParameterListItem` dataclass.

SDK Internal Changes:
 * Skip Graviton runtimes for testing notebook native auth ([#294](https://github.com/databricks/databricks-sdk-py/pull/294)).
 * Fixed integration tests to not use beta DBR ([#309](https://github.com/databricks/databricks-sdk-py/pull/309)).

OpenAPI SHA: 5d0ccbb790d341eae8e85321a685a9e9e2d5bf24, Date: 2023-08-29

## 0.6.0

* Added collection of Databricks Runtime versions used together with Python SDK ([#287](https://github.com/databricks/databricks-sdk-py/pull/287)).
* Applied attribute transformer when reading in attributes from the environment ([#293](https://github.com/databricks/databricks-sdk-py/pull/293)).
* Made notebook-native auth work with more configurations of the Databricks Runtime ([#285](https://github.com/databricks/databricks-sdk-py/pull/285)).
* Added retry in `w.clusters.ensure_cluster_is_running(id)` when cluster is simultaneously started by two different processes. ([#283](https://github.com/databricks/databricks-sdk-py/pull/283)).
* Set necessary headers when authenticating via Azure CLI ([#290](https://github.com/databricks/databricks-sdk-py/pull/290)).
* Updated classifier to `Development Status :: 4 - Beta` ([#291](https://github.com/databricks/databricks-sdk-py/pull/291)).
* Introduced Artifact Allowlist, Securable Tags, and Subentity Tags services.
* Introduced DeleteRuns and RestoreRuns methods in the Experiments API.
* Introduced the GetSecret method in the Secrets API.
* Renamed Auto Maintenance to Predictive Optimization.

New Services:

 * Added [w.artifact_allowlists](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/artifact_allowlists.html) workspace-level service.
 * Added [w.securable_tags](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/securable_tags.html) workspace-level service.
 * Added [w.subentity_tags](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/subentity_tags.html) workspace-level service.
 * Added `databricks.sdk.service.catalog.ArtifactAllowlistInfo` dataclass.
 * Added `databricks.sdk.service.catalog.ArtifactMatcher` dataclass.
 * Added `databricks.sdk.service.catalog.ArtifactType` dataclass.
 * Added `databricks.sdk.service.catalog.GetArtifactAllowlistRequest` dataclass.
 * Added `databricks.sdk.service.catalog.ListSecurableTagsRequest` dataclass.
 * Added `databricks.sdk.service.catalog.ListSecurableType` dataclass.
 * Added `databricks.sdk.service.catalog.ListSubentityTagsRequest` dataclass.
 * Added `databricks.sdk.service.catalog.MatchType` dataclass.
 * Added `databricks.sdk.service.catalog.SetArtifactAllowlist` dataclass.
 * Added `databricks.sdk.service.catalog.TagChanges` dataclass.
 * Added `databricks.sdk.service.catalog.TagKeyValuePair` dataclass.
 * Added `databricks.sdk.service.catalog.TagSecurable` dataclass.
 * Added `databricks.sdk.service.catalog.TagSecurableAssignment` dataclass.
 * Added `databricks.sdk.service.catalog.TagSecurableAssignmentsList` dataclass.
 * Added `databricks.sdk.service.catalog.TagSubentity` dataclass.
 * Added `databricks.sdk.service.catalog.TagSubentityAssignmentsList` dataclass.
 * Added `databricks.sdk.service.catalog.TagsSubentityAssignment` dataclass.
 * Added `databricks.sdk.service.catalog.UpdateSecurableType` dataclass.
 * Added `databricks.sdk.service.catalog.UpdateTags` dataclass.

New APIs:

 * Added `delete_runs()` method for [w.experiments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/experiments.html) workspace-level service.
 * Added `restore_runs()` method for [w.experiments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/experiments.html) workspace-level service.
 * Added `databricks.sdk.service.ml.DeleteRuns` dataclass.
 * Added `databricks.sdk.service.ml.DeleteRunsResponse` dataclass.
 * Added `databricks.sdk.service.ml.RestoreRuns` dataclass.
 * Added `databricks.sdk.service.ml.RestoreRunsResponse` dataclass.
 * Added `get_secret()` method for [w.secrets](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/secrets.html) workspace-level service.
 * Added `databricks.sdk.service.workspace.GetSecretRequest` dataclass.
 * Added `databricks.sdk.service.workspace.GetSecretResponse` dataclass.

Service Renames:

 * Removed `effective_auto_maintenance_flag` field for `databricks.sdk.service.catalog.CatalogInfo`.
 * Removed `enable_auto_maintenance` field for `databricks.sdk.service.catalog.CatalogInfo`.
 * Added `effective_predictive_optimization_flag` field for `databricks.sdk.service.catalog.CatalogInfo`.
 * Added `enable_predictive_optimization` field for `databricks.sdk.service.catalog.CatalogInfo`.
 * Removed `databricks.sdk.service.catalog.EffectiveAutoMaintenanceFlag` dataclass.
 * Removed `databricks.sdk.service.catalog.EffectiveAutoMaintenanceFlagInheritedFromType` dataclass.
 * Removed `databricks.sdk.service.catalog.EnableAutoMaintenance` dataclass.
 * Removed `effective_auto_maintenance_flag` field for `databricks.sdk.service.catalog.SchemaInfo`.
 * Removed `enable_auto_maintenance` field for `databricks.sdk.service.catalog.SchemaInfo`.
 * Added `effective_predictive_optimization_flag` field for `databricks.sdk.service.catalog.SchemaInfo`.
 * Added `enable_predictive_optimization` field for `databricks.sdk.service.catalog.SchemaInfo`.
 * Removed `effective_auto_maintenance_flag` field for `databricks.sdk.service.catalog.TableInfo`.
 * Removed `enable_auto_maintenance` field for `databricks.sdk.service.catalog.TableInfo`.
 * Added `effective_predictive_optimization_flag` field for `databricks.sdk.service.catalog.TableInfo`.
 * Added `enable_predictive_optimization` field for `databricks.sdk.service.catalog.TableInfo`.
 * Added `databricks.sdk.service.catalog.EffectivePredictiveOptimizationFlag` dataclass.
 * Added `databricks.sdk.service.catalog.EffectivePredictiveOptimizationFlagInheritedFromType` dataclass.
 * Added `databricks.sdk.service.catalog.EnablePredictiveOptimization` dataclass.

OpenAPI SHA: beff621d7b3e1d59244e2e34fc53a496f310e130, Date: 2023-08-17

## 0.5.0

* Added `connection_pool_size` configuration property (preview) ([#276](https://github.com/databricks/databricks-sdk-py/pull/276)).
* Fixed OAuth M2M corner case in `WorkspaceClient` where `DATABRICKS_ACCOUNT_ID` is present in the environment ([#273](https://github.com/databricks/databricks-sdk-py/pull/273)).

API Changes:

 * Changed `create()` method for [a.account_storage_credentials](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_storage_credentials.html) account-level service to return `databricks.sdk.service.catalog.AccountsStorageCredentialInfo` dataclass.
 * Changed `get()` method for [a.account_storage_credentials](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_storage_credentials.html) account-level service to return `databricks.sdk.service.catalog.AccountsStorageCredentialInfo` dataclass.
 * Changed `update()` method for [a.account_storage_credentials](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_storage_credentials.html) account-level service to return `databricks.sdk.service.catalog.AccountsStorageCredentialInfo` dataclass.
 * Changed `create()` method for [w.connections](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/connections.html) workspace-level service with new required argument order.
 * Changed `update()` method for [w.connections](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/connections.html) workspace-level service with new required argument order.
 * Removed `options_kvpairs` field for `databricks.sdk.service.catalog.ConnectionInfo`.
 * Removed `properties_kvpairs` field for `databricks.sdk.service.catalog.ConnectionInfo`.
 * Added `options` field for `databricks.sdk.service.catalog.ConnectionInfo`.
 * Added `properties` field for `databricks.sdk.service.catalog.ConnectionInfo`.
 * Added `provisioning_state` field for `databricks.sdk.service.catalog.ConnectionInfo`.
 * Added `securable_kind` field for `databricks.sdk.service.catalog.ConnectionInfo`.
 * Added `securable_type` field for `databricks.sdk.service.catalog.ConnectionInfo`.
 * Removed `options_kvpairs` field for `databricks.sdk.service.catalog.CreateConnection`.
 * Removed `properties_kvpairs` field for `databricks.sdk.service.catalog.CreateConnection`.
 * Added `options` field for `databricks.sdk.service.catalog.CreateConnection`.
 * Added `properties` field for `databricks.sdk.service.catalog.CreateConnection`.
 * Changed `algorithm` field for `databricks.sdk.service.catalog.SseEncryptionDetails` to no longer be required.
 * Removed `options_kvpairs` field for `databricks.sdk.service.catalog.UpdateConnection`.
 * Added `options` field for `databricks.sdk.service.catalog.UpdateConnection`.
 * Added `databricks.sdk.service.catalog.AccountsStorageCredentialInfo` dataclass.
 * Added `databricks.sdk.service.catalog.ConnectionInfoSecurableKind` dataclass.
 * Added `databricks.sdk.service.catalog.ProvisioningState` dataclass.
 * Added `data_security_mode` field for `databricks.sdk.service.compute.CreateCluster`.
 * Added `docker_image` field for `databricks.sdk.service.compute.CreateCluster`.
 * Added `single_user_name` field for `databricks.sdk.service.compute.CreateCluster`.
 * Removed `schema` field for `databricks.sdk.service.iam.PartialUpdate`.
 * Added `schemas` field for `databricks.sdk.service.iam.PartialUpdate`.

OpenAPI SHA: 1e3533f94335f0e6c5d9262bc1fea95b3ddcb0e1, Date: 2023-08-11

## 0.4.0

To simplify documentation and management of object permissions, this release features a major reorganization of how permissions APIs are structured in the SDK. Rather than using a single permissions.get() API for all services, each service supporting permissions has its own permissions APIs. Follow these steps to migrate to the current SDK:

 * Change `w.permissions.get()` and `w.permissions.get_by_request_object_id_and_request_object_type()` to `w.<Service>.get_<Service>_permissions()`
 * Change `w.permissions.get_permission_levels()` to `w.<Service>.get_<Service>_permission_levels()`
 * Change `w.permissions.set()` to `w.<Service>.set_<Service>_permissions()`
 * Change `w.permissions.update()` to `w.<Service>.update_<Service>_permissions()`

API Changes:

 * Added `get_cluster_policy_permission_levels()` method for [w.cluster_policies](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/cluster_policies.html) workspace-level service.
 * Added `get_cluster_policy_permissions()` method for [w.cluster_policies](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/cluster_policies.html) workspace-level service.
 * Added `set_cluster_policy_permissions()` method for [w.cluster_policies](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/cluster_policies.html) workspace-level service.
 * Added `update_cluster_policy_permissions()` method for [w.cluster_policies](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/cluster_policies.html) workspace-level service.
 * Added `get_cluster_permission_levels()` method for [w.clusters](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/clusters.html) workspace-level service.
 * Added `get_cluster_permissions()` method for [w.clusters](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/clusters.html) workspace-level service.
 * Added `set_cluster_permissions()` method for [w.clusters](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/clusters.html) workspace-level service.
 * Added `update_cluster_permissions()` method for [w.clusters](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/clusters.html) workspace-level service.
 * Added `get_instance_pool_permission_levels()` method for [w.instance_pools](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/instance_pools.html) workspace-level service.
 * Added `get_instance_pool_permissions()` method for [w.instance_pools](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/instance_pools.html) workspace-level service.
 * Added `set_instance_pool_permissions()` method for [w.instance_pools](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/instance_pools.html) workspace-level service.
 * Added `update_instance_pool_permissions()` method for [w.instance_pools](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/instance_pools.html) workspace-level service.
 * Added `databricks.sdk.service.compute.ClusterAccessControlRequest` dataclass.
 * Added `databricks.sdk.service.compute.ClusterAccessControlResponse` dataclass.
 * Added `databricks.sdk.service.compute.ClusterPermission` dataclass.
 * Added `databricks.sdk.service.compute.ClusterPermissionLevel` dataclass.
 * Added `databricks.sdk.service.compute.ClusterPermissions` dataclass.
 * Added `databricks.sdk.service.compute.ClusterPermissionsDescription` dataclass.
 * Added `databricks.sdk.service.compute.ClusterPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.compute.ClusterPolicyAccessControlRequest` dataclass.
 * Added `databricks.sdk.service.compute.ClusterPolicyAccessControlResponse` dataclass.
 * Added `databricks.sdk.service.compute.ClusterPolicyPermission` dataclass.
 * Added `databricks.sdk.service.compute.ClusterPolicyPermissionLevel` dataclass.
 * Added `databricks.sdk.service.compute.ClusterPolicyPermissions` dataclass.
 * Added `databricks.sdk.service.compute.ClusterPolicyPermissionsDescription` dataclass.
 * Added `databricks.sdk.service.compute.ClusterPolicyPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.compute.GetClusterPermissionLevelsRequest` dataclass.
 * Added `databricks.sdk.service.compute.GetClusterPermissionLevelsResponse` dataclass.
 * Added `databricks.sdk.service.compute.GetClusterPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.compute.GetClusterPolicyPermissionLevelsRequest` dataclass.
 * Added `databricks.sdk.service.compute.GetClusterPolicyPermissionLevelsResponse` dataclass.
 * Added `databricks.sdk.service.compute.GetClusterPolicyPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.compute.GetInstancePoolPermissionLevelsRequest` dataclass.
 * Added `databricks.sdk.service.compute.GetInstancePoolPermissionLevelsResponse` dataclass.
 * Added `databricks.sdk.service.compute.GetInstancePoolPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.compute.InstancePoolAccessControlRequest` dataclass.
 * Added `databricks.sdk.service.compute.InstancePoolAccessControlResponse` dataclass.
 * Added `databricks.sdk.service.compute.InstancePoolPermission` dataclass.
 * Added `databricks.sdk.service.compute.InstancePoolPermissionLevel` dataclass.
 * Added `databricks.sdk.service.compute.InstancePoolPermissions` dataclass.
 * Added `databricks.sdk.service.compute.InstancePoolPermissionsDescription` dataclass.
 * Added `databricks.sdk.service.compute.InstancePoolPermissionsRequest` dataclass.
 * Changed `set()` method for [w.permissions](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/permissions.html) workspace-level service to start returning `databricks.sdk.service.iam.ObjectPermissions` dataclass.
 * Changed `update()` method for [w.permissions](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/permissions.html) workspace-level service to start returning `databricks.sdk.service.iam.ObjectPermissions` dataclass.
 * Added `get_password_permission_levels()` method for [w.users](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/users.html) workspace-level service.
 * Added `get_password_permissions()` method for [w.users](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/users.html) workspace-level service.
 * Added `set_password_permissions()` method for [w.users](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/users.html) workspace-level service.
 * Added `update_password_permissions()` method for [w.users](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/users.html) workspace-level service.
 * Added `display_name` field for `databricks.sdk.service.iam.AccessControlResponse`.
 * Changed `roles` field for `databricks.sdk.service.iam.GetAssignableRolesForResourceResponse` to `databricks.sdk.service.iam.RoleList` dataclass.
 * Added `databricks.sdk.service.iam.GetPasswordPermissionLevelsResponse` dataclass.
 * Added `databricks.sdk.service.iam.PasswordAccessControlRequest` dataclass.
 * Added `databricks.sdk.service.iam.PasswordAccessControlResponse` dataclass.
 * Added `databricks.sdk.service.iam.PasswordPermission` dataclass.
 * Added `databricks.sdk.service.iam.PasswordPermissionLevel` dataclass.
 * Added `databricks.sdk.service.iam.PasswordPermissions` dataclass.
 * Added `databricks.sdk.service.iam.PasswordPermissionsDescription` dataclass.
 * Added `databricks.sdk.service.iam.PasswordPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.iam.Role` dataclass.
 * Added `get_job_permission_levels()` method for [w.jobs](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/jobs.html) workspace-level service.
 * Added `get_job_permissions()` method for [w.jobs](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/jobs.html) workspace-level service.
 * Added `set_job_permissions()` method for [w.jobs](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/jobs.html) workspace-level service.
 * Added `update_job_permissions()` method for [w.jobs](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/jobs.html) workspace-level service.
 * Added `databricks.sdk.service.jobs.GetJobPermissionLevelsRequest` dataclass.
 * Added `databricks.sdk.service.jobs.GetJobPermissionLevelsResponse` dataclass.
 * Added `databricks.sdk.service.jobs.GetJobPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.jobs.JobAccessControlRequest` dataclass.
 * Added `databricks.sdk.service.jobs.JobAccessControlResponse` dataclass.
 * Added `databricks.sdk.service.jobs.JobPermission` dataclass.
 * Added `databricks.sdk.service.jobs.JobPermissionLevel` dataclass.
 * Added `databricks.sdk.service.jobs.JobPermissions` dataclass.
 * Added `databricks.sdk.service.jobs.JobPermissionsDescription` dataclass.
 * Added `databricks.sdk.service.jobs.JobPermissionsRequest` dataclass.
 * Added `get_experiment_permission_levels()` method for [w.experiments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/experiments.html) workspace-level service.
 * Added `get_experiment_permissions()` method for [w.experiments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/experiments.html) workspace-level service.
 * Added `set_experiment_permissions()` method for [w.experiments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/experiments.html) workspace-level service.
 * Added `update_experiment_permissions()` method for [w.experiments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/experiments.html) workspace-level service.
 * Added `get_registered_model_permission_levels()` method for [w.model_registry](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/model_registry.html) workspace-level service.
 * Added `get_registered_model_permissions()` method for [w.model_registry](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/model_registry.html) workspace-level service.
 * Added `set_registered_model_permissions()` method for [w.model_registry](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/model_registry.html) workspace-level service.
 * Added `update_registered_model_permissions()` method for [w.model_registry](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/model_registry.html) workspace-level service.
 * Added `databricks.sdk.service.ml.ExperimentAccessControlRequest` dataclass.
 * Added `databricks.sdk.service.ml.ExperimentAccessControlResponse` dataclass.
 * Added `databricks.sdk.service.ml.ExperimentPermission` dataclass.
 * Added `databricks.sdk.service.ml.ExperimentPermissionLevel` dataclass.
 * Added `databricks.sdk.service.ml.ExperimentPermissions` dataclass.
 * Added `databricks.sdk.service.ml.ExperimentPermissionsDescription` dataclass.
 * Added `databricks.sdk.service.ml.ExperimentPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.ml.GetExperimentPermissionLevelsRequest` dataclass.
 * Added `databricks.sdk.service.ml.GetExperimentPermissionLevelsResponse` dataclass.
 * Added `databricks.sdk.service.ml.GetExperimentPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.ml.GetRegisteredModelPermissionLevelsRequest` dataclass.
 * Added `databricks.sdk.service.ml.GetRegisteredModelPermissionLevelsResponse` dataclass.
 * Added `databricks.sdk.service.ml.GetRegisteredModelPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.ml.RegisteredModelAccessControlRequest` dataclass.
 * Added `databricks.sdk.service.ml.RegisteredModelAccessControlResponse` dataclass.
 * Added `databricks.sdk.service.ml.RegisteredModelPermission` dataclass.
 * Added `databricks.sdk.service.ml.RegisteredModelPermissionLevel` dataclass.
 * Added `databricks.sdk.service.ml.RegisteredModelPermissions` dataclass.
 * Added `databricks.sdk.service.ml.RegisteredModelPermissionsDescription` dataclass.
 * Added `databricks.sdk.service.ml.RegisteredModelPermissionsRequest` dataclass.
 * Added `scopes` field for `databricks.sdk.service.oauth2.CreateCustomAppIntegration`.
 * Added `get_pipeline_permission_levels()` method for [w.pipelines](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/pipelines.html) workspace-level service.
 * Added `get_pipeline_permissions()` method for [w.pipelines](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/pipelines.html) workspace-level service.
 * Added `set_pipeline_permissions()` method for [w.pipelines](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/pipelines.html) workspace-level service.
 * Added `update_pipeline_permissions()` method for [w.pipelines](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/pipelines.html) workspace-level service.
 * Added `databricks.sdk.service.pipelines.GetPipelinePermissionLevelsRequest` dataclass.
 * Added `databricks.sdk.service.pipelines.GetPipelinePermissionLevelsResponse` dataclass.
 * Added `databricks.sdk.service.pipelines.GetPipelinePermissionsRequest` dataclass.
 * Added `databricks.sdk.service.pipelines.PipelineAccessControlRequest` dataclass.
 * Added `databricks.sdk.service.pipelines.PipelineAccessControlResponse` dataclass.
 * Added `databricks.sdk.service.pipelines.PipelinePermission` dataclass.
 * Added `databricks.sdk.service.pipelines.PipelinePermissionLevel` dataclass.
 * Added `databricks.sdk.service.pipelines.PipelinePermissions` dataclass.
 * Added `databricks.sdk.service.pipelines.PipelinePermissionsDescription` dataclass.
 * Added `databricks.sdk.service.pipelines.PipelinePermissionsRequest` dataclass.
 * Added `gcp_managed_network_config` field for `databricks.sdk.service.provisioning.CreateWorkspaceRequest`.
 * Added `gke_config` field for `databricks.sdk.service.provisioning.CreateWorkspaceRequest`.
 * Added `get_serving_endpoint_permission_levels()` method for [w.serving_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/serving_endpoints.html) workspace-level service.
 * Added `get_serving_endpoint_permissions()` method for [w.serving_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/serving_endpoints.html) workspace-level service.
 * Added `set_serving_endpoint_permissions()` method for [w.serving_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/serving_endpoints.html) workspace-level service.
 * Added `update_serving_endpoint_permissions()` method for [w.serving_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/serving_endpoints.html) workspace-level service.
 * Added `instance_profile_arn` field for `databricks.sdk.service.serving.ServedModelInput`.
 * Added `instance_profile_arn` field for `databricks.sdk.service.serving.ServedModelOutput`.
 * Added `databricks.sdk.service.serving.GetServingEndpointPermissionLevelsRequest` dataclass.
 * Added `databricks.sdk.service.serving.GetServingEndpointPermissionLevelsResponse` dataclass.
 * Added `databricks.sdk.service.serving.GetServingEndpointPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.serving.ServingEndpointAccessControlRequest` dataclass.
 * Added `databricks.sdk.service.serving.ServingEndpointAccessControlResponse` dataclass.
 * Added `databricks.sdk.service.serving.ServingEndpointPermission` dataclass.
 * Added `databricks.sdk.service.serving.ServingEndpointPermissionLevel` dataclass.
 * Added `databricks.sdk.service.serving.ServingEndpointPermissions` dataclass.
 * Added `databricks.sdk.service.serving.ServingEndpointPermissionsDescription` dataclass.
 * Added `databricks.sdk.service.serving.ServingEndpointPermissionsRequest` dataclass.
 * Added `get_token_permission_levels()` method for [w.token_management](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/token_management.html) workspace-level service.
 * Added `get_token_permissions()` method for [w.token_management](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/token_management.html) workspace-level service.
 * Added `set_token_permissions()` method for [w.token_management](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/token_management.html) workspace-level service.
 * Added `update_token_permissions()` method for [w.token_management](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/token_management.html) workspace-level service.
 * Added `databricks.sdk.service.settings.GetTokenPermissionLevelsResponse` dataclass.
 * Added `databricks.sdk.service.settings.TokenAccessControlRequest` dataclass.
 * Added `databricks.sdk.service.settings.TokenAccessControlResponse` dataclass.
 * Added `databricks.sdk.service.settings.TokenPermission` dataclass.
 * Added `databricks.sdk.service.settings.TokenPermissionLevel` dataclass.
 * Added `databricks.sdk.service.settings.TokenPermissions` dataclass.
 * Added `databricks.sdk.service.settings.TokenPermissionsDescription` dataclass.
 * Added `databricks.sdk.service.settings.TokenPermissionsRequest` dataclass.
 * Added `get_warehouse_permission_levels()` method for [w.warehouses](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/warehouses.html) workspace-level service.
 * Added `get_warehouse_permissions()` method for [w.warehouses](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/warehouses.html) workspace-level service.
 * Added `set_warehouse_permissions()` method for [w.warehouses](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/warehouses.html) workspace-level service.
 * Added `update_warehouse_permissions()` method for [w.warehouses](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/warehouses.html) workspace-level service.
 * Added `can_subscribe_to_live_query` field for `databricks.sdk.service.sql.QueryInfo`.
 * Removed `queued_overload_time_ms` field for `databricks.sdk.service.sql.QueryMetrics`.
 * Removed `queued_provisioning_time_ms` field for `databricks.sdk.service.sql.QueryMetrics`.
 * Removed `total_files_count` field for `databricks.sdk.service.sql.QueryMetrics`.
 * Removed `total_partitions_count` field for `databricks.sdk.service.sql.QueryMetrics`.
 * Added `metadata_time_ms` field for `databricks.sdk.service.sql.QueryMetrics`.
 * Added `overloading_queue_start_timestamp` field for `databricks.sdk.service.sql.QueryMetrics`.
 * Added `planning_phases` field for `databricks.sdk.service.sql.QueryMetrics`.
 * Added `planning_time_ms` field for `databricks.sdk.service.sql.QueryMetrics`.
 * Added `provisioning_queue_start_timestamp` field for `databricks.sdk.service.sql.QueryMetrics`.
 * Added `pruned_bytes` field for `databricks.sdk.service.sql.QueryMetrics`.
 * Added `pruned_files_count` field for `databricks.sdk.service.sql.QueryMetrics`.
 * Added `query_compilation_start_timestamp` field for `databricks.sdk.service.sql.QueryMetrics`.
 * Added `query_execution_time_ms` field for `databricks.sdk.service.sql.QueryMetrics`.
 * Added `databricks.sdk.service.sql.GetWarehousePermissionLevelsRequest` dataclass.
 * Added `databricks.sdk.service.sql.GetWarehousePermissionLevelsResponse` dataclass.
 * Added `databricks.sdk.service.sql.GetWarehousePermissionsRequest` dataclass.
 * Added `databricks.sdk.service.sql.WarehouseAccessControlRequest` dataclass.
 * Added `databricks.sdk.service.sql.WarehouseAccessControlResponse` dataclass.
 * Added `databricks.sdk.service.sql.WarehousePermission` dataclass.
 * Added `databricks.sdk.service.sql.WarehousePermissionLevel` dataclass.
 * Added `databricks.sdk.service.sql.WarehousePermissions` dataclass.
 * Added `databricks.sdk.service.sql.WarehousePermissionsDescription` dataclass.
 * Added `databricks.sdk.service.sql.WarehousePermissionsRequest` dataclass.
 * Added `get_repo_permission_levels()` method for [w.repos](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/repos.html) workspace-level service.
 * Added `get_repo_permissions()` method for [w.repos](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/repos.html) workspace-level service.
 * Added `set_repo_permissions()` method for [w.repos](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/repos.html) workspace-level service.
 * Added `update_repo_permissions()` method for [w.repos](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/repos.html) workspace-level service.
 * Added `get_workspace_object_permission_levels()` method for [w.workspace](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/workspace.html) workspace-level service.
 * Added `get_workspace_object_permissions()` method for [w.workspace](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/workspace.html) workspace-level service.
 * Added `set_workspace_object_permissions()` method for [w.workspace](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/workspace.html) workspace-level service.
 * Added `update_workspace_object_permissions()` method for [w.workspace](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/workspace.html) workspace-level service.
 * Added `databricks.sdk.service.workspace.GetRepoPermissionLevelsRequest` dataclass.
 * Added `databricks.sdk.service.workspace.GetRepoPermissionLevelsResponse` dataclass.
 * Added `databricks.sdk.service.workspace.GetRepoPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.workspace.GetWorkspaceObjectPermissionLevelsRequest` dataclass.
 * Added `databricks.sdk.service.workspace.GetWorkspaceObjectPermissionLevelsResponse` dataclass.
 * Added `databricks.sdk.service.workspace.GetWorkspaceObjectPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.workspace.RepoAccessControlRequest` dataclass.
 * Added `databricks.sdk.service.workspace.RepoAccessControlResponse` dataclass.
 * Added `databricks.sdk.service.workspace.RepoPermission` dataclass.
 * Added `databricks.sdk.service.workspace.RepoPermissionLevel` dataclass.
 * Added `databricks.sdk.service.workspace.RepoPermissions` dataclass.
 * Added `databricks.sdk.service.workspace.RepoPermissionsDescription` dataclass.
 * Added `databricks.sdk.service.workspace.RepoPermissionsRequest` dataclass.
 * Added `databricks.sdk.service.workspace.WorkspaceObjectAccessControlRequest` dataclass.
 * Added `databricks.sdk.service.workspace.WorkspaceObjectAccessControlResponse` dataclass.
 * Added `databricks.sdk.service.workspace.WorkspaceObjectPermission` dataclass.
 * Added `databricks.sdk.service.workspace.WorkspaceObjectPermissionLevel` dataclass.
 * Added `databricks.sdk.service.workspace.WorkspaceObjectPermissions` dataclass.
 * Added `databricks.sdk.service.workspace.WorkspaceObjectPermissionsDescription` dataclass.
 * Added `databricks.sdk.service.workspace.WorkspaceObjectPermissionsRequest` dataclass.

OpenAPI SHA: 386b65ecdc825b9c3ed4aa7ca88e2e5baf9d87df, Date: 2023-08-07

## 0.3.1

* Added timeout to `w.clusters.ensure_cluster_running()` ([#227](https://github.com/databricks/databricks-sdk-py/pull/227)).
* Fixed `debug_headers` type hints for `WorkspaceClient` and `AccountClient` ([#258](https://github.com/databricks/databricks-sdk-py/pull/258)).
* Made dbutils typecast use a valid type variable ([#259](https://github.com/databricks/databricks-sdk-py/pull/259)).


## 0.3.0

* Fixed serialization of lists of enum values ([#248](https://github.com/databricks/databricks-sdk-py/pull/248)).
* Fixed examples that used incorrect keyword argument names. (https://github.com/databricks/databricks-sdk-go/pull/560)
* Handled nested query parameters in ApiClient.do() ([#249](https://github.com/databricks/databricks-sdk-py/pull/249)).
* Improved access of `__annotations__` ([#239](https://github.com/databricks/databricks-sdk-py/pull/239)).

API Changes:

 * Changed `create()` method for [a.account_metastore_assignments](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_metastore_assignments.html) account-level service to no longer return `databricks.sdk.service.catalog.CreateMetastoreAssignmentsResponseItemList` dataclass.
 * Added `connection_name` field for `databricks.sdk.service.catalog.CreateCatalog`.
 * Added `access_point` field for `databricks.sdk.service.catalog.CreateExternalLocation`.
 * Added `encryption_details` field for `databricks.sdk.service.catalog.CreateExternalLocation`.
 * Removed `databricks.sdk.service.catalog.CreateMetastoreAssignmentsResponseItem` dataclass.
 * Added `access_point` field for `databricks.sdk.service.catalog.ExternalLocationInfo`.
 * Added `encryption_details` field for `databricks.sdk.service.catalog.ExternalLocationInfo`.
 * Added `access_point` field for `databricks.sdk.service.catalog.TableInfo`.
 * Added `encryption_details` field for `databricks.sdk.service.catalog.TableInfo`.
 * Added `access_point` field for `databricks.sdk.service.catalog.UpdateExternalLocation`.
 * Added `encryption_details` field for `databricks.sdk.service.catalog.UpdateExternalLocation`.
 * Added `access_point` field for `databricks.sdk.service.catalog.VolumeInfo`.
 * Added `encryption_details` field for `databricks.sdk.service.catalog.VolumeInfo`.
 * Added `databricks.sdk.service.catalog.EncryptionDetails` dataclass.
 * Added `databricks.sdk.service.catalog.SseEncryptionDetails` dataclass.
 * Added `databricks.sdk.service.catalog.SseEncryptionDetailsAlgorithm` dataclass.
 * Added [a.account_network_policy](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_network_policy.html) account-level service.
 * Added `databricks.sdk.service.settings.AccountNetworkPolicyMessage` dataclass.
 * Added `databricks.sdk.service.settings.DeleteAccountNetworkPolicyRequest` dataclass.
 * Added `databricks.sdk.service.settings.DeleteAccountNetworkPolicyResponse` dataclass.
 * Added `databricks.sdk.service.settings.ReadAccountNetworkPolicyRequest` dataclass.
 * Added `databricks.sdk.service.settings.UpdateAccountNetworkPolicyRequest` dataclass.

OpenAPI SHA: a1b6c1ecfaab6635911d3c060a8dd797ac6b2d4d, Date: 2023-07-27

## 0.2.1

* Support older versions of `urllib3` and Databricks Runtime with regards to `DEFAULT_METHOD_WHITELIST` change to `DEFAULT_ALLOWED_METHODS` ([#240](https://github.com/databricks/databricks-sdk-py/pull/240)).


## 0.2.0

* Add Issue Templates ([#208](https://github.com/databricks/databricks-sdk-py/pull/208)).
* Fixed notebook native auth for jobs ([#209](https://github.com/databricks/databricks-sdk-py/pull/209)).
* Replace `datatime.timedelta()` with `datetime.timedelta()` in codebase ([#207](https://github.com/databricks/databricks-sdk-py/pull/207)).
* Support dod in python sdk ([#212](https://github.com/databricks/databricks-sdk-py/pull/212)).
* [DECO-1115] Add local implementation for `dbutils.widgets` ([#93](https://github.com/databricks/databricks-sdk-py/pull/93)).
* Fix error message, ExportFormat -> ImportFormat ([#220](https://github.com/databricks/databricks-sdk-py/pull/220)).
* Regenerate Python SDK using recent OpenAPI Specification ([#229](https://github.com/databricks/databricks-sdk-py/pull/229)).
* Make workspace client also return runtime dbutils when in dbr ([#210](https://github.com/databricks/databricks-sdk-py/pull/210)).
* Use .ConstantName defining target enum states for waiters ([#230](https://github.com/databricks/databricks-sdk-py/pull/230)).
* Fix enum deserialization ([#234](https://github.com/databricks/databricks-sdk-py/pull/234)).
* Fix enum deserialization, take 2 ([#235](https://github.com/databricks/databricks-sdk-py/pull/235)).
* Added toolchain configuration to `.codegen.json` ([#236](https://github.com/databricks/databricks-sdk-py/pull/236)).
* Make OpenAPI spec location configurable ([#237](https://github.com/databricks/databricks-sdk-py/pull/237)).
* Rearrange imports in `databricks.sdk.runtime` to improve local editor experience ([#219](https://github.com/databricks/databricks-sdk-py/pull/219)).
* Updated account-level and workspace-level user management examples ([#241](https://github.com/databricks/databricks-sdk-py/pull/241)).

API Changes:

 * Removed `maintenance()` method for [w.metastores](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/metastores.html) workspace-level service.
 * Added `enable_optimization()` method for [w.metastores](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/metastores.html) workspace-level service.
 * Added `update()` method for [w.tables](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/tables.html) workspace-level service.
 * Added `force` field for `databricks.sdk.service.catalog.DeleteAccountMetastoreRequest`.
 * Added `force` field for `databricks.sdk.service.catalog.DeleteAccountStorageCredentialRequest`.
 * Removed `databricks.sdk.service.catalog.UpdateAutoMaintenance` dataclass.
 * Removed `databricks.sdk.service.catalog.UpdateAutoMaintenanceResponse` dataclass.
 * Added `databricks.sdk.service.catalog.UpdatePredictiveOptimization` dataclass.
 * Added `databricks.sdk.service.catalog.UpdatePredictiveOptimizationResponse` dataclass.
 * Added `databricks.sdk.service.catalog.UpdateTableRequest` dataclass.
 * Added `schema` field for `databricks.sdk.service.iam.PartialUpdate`.
 * Added `databricks.sdk.service.iam.PatchSchema` dataclass.
 * Added `trigger_info` field for `databricks.sdk.service.jobs.BaseRun`.
 * Added `health` field for `databricks.sdk.service.jobs.CreateJob`.
 * Added `job_source` field for `databricks.sdk.service.jobs.GitSource`.
 * Added `on_duration_warning_threshold_exceeded` field for `databricks.sdk.service.jobs.JobEmailNotifications`.
 * Added `health` field for `databricks.sdk.service.jobs.JobSettings`.
 * Added `trigger_info` field for `databricks.sdk.service.jobs.Run`.
 * Added `run_job_output` field for `databricks.sdk.service.jobs.RunOutput`.
 * Added `run_job_task` field for `databricks.sdk.service.jobs.RunTask`.
 * Added `email_notifications` field for `databricks.sdk.service.jobs.SubmitRun`.
 * Added `health` field for `databricks.sdk.service.jobs.SubmitRun`.
 * Added `email_notifications` field for `databricks.sdk.service.jobs.SubmitTask`.
 * Added `health` field for `databricks.sdk.service.jobs.SubmitTask`.
 * Added `notification_settings` field for `databricks.sdk.service.jobs.SubmitTask`.
 * Added `health` field for `databricks.sdk.service.jobs.Task`.
 * Added `run_job_task` field for `databricks.sdk.service.jobs.Task`.
 * Added `on_duration_warning_threshold_exceeded` field for `databricks.sdk.service.jobs.TaskEmailNotifications`.
 * Added `on_duration_warning_threshold_exceeded` field for `databricks.sdk.service.jobs.WebhookNotifications`.
 * Added `databricks.sdk.service.jobs.JobSource` dataclass.
 * Added `databricks.sdk.service.jobs.JobSourceDirtyState` dataclass.
 * Added `databricks.sdk.service.jobs.JobsHealthMetric` dataclass.
 * Added `databricks.sdk.service.jobs.JobsHealthOperator` dataclass.
 * Added `databricks.sdk.service.jobs.JobsHealthRule` dataclass.
 * Added `databricks.sdk.service.jobs.JobsHealthRules` dataclass.
 * Added `databricks.sdk.service.jobs.RunJobOutput` dataclass.
 * Added `databricks.sdk.service.jobs.RunJobTask` dataclass.
 * Added `databricks.sdk.service.jobs.TriggerInfo` dataclass.
 * Added `databricks.sdk.service.jobs.WebhookNotificationsOnDurationWarningThresholdExceededItem` dataclass.
 * Removed `whl` field for `databricks.sdk.service.pipelines.PipelineLibrary`.
 * Changed `delete_personal_compute_setting()` method for [a.account_settings](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_settings.html) account-level service with new required argument order.
 * Changed `read_personal_compute_setting()` method for [a.account_settings](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_settings.html) account-level service with new required argument order.
 * Changed `etag` field for `databricks.sdk.service.settings.DeletePersonalComputeSettingRequest` to be required.
 * Changed `etag` field for `databricks.sdk.service.settings.ReadPersonalComputeSettingRequest` to be required.
 * Added [w.clean_rooms](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/clean_rooms.html) workspace-level service.
 * Added `databricks.sdk.service.sharing.CentralCleanRoomInfo` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomAssetInfo` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomCatalog` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomCatalogUpdate` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomCollaboratorInfo` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomInfo` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomNotebookInfo` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomTableInfo` dataclass.
 * Added `databricks.sdk.service.sharing.ColumnInfo` dataclass.
 * Added `databricks.sdk.service.sharing.ColumnMask` dataclass.
 * Added `databricks.sdk.service.sharing.ColumnTypeName` dataclass.
 * Added `databricks.sdk.service.sharing.CreateCleanRoom` dataclass.
 * Added `databricks.sdk.service.sharing.DeleteCleanRoomRequest` dataclass.
 * Added `databricks.sdk.service.sharing.GetCleanRoomRequest` dataclass.
 * Added `databricks.sdk.service.sharing.ListCleanRoomsResponse` dataclass.
 * Added `databricks.sdk.service.sharing.UpdateCleanRoom` dataclass.
 * Changed `query` field for `databricks.sdk.service.sql.Alert` to `databricks.sdk.service.sql.AlertQuery` dataclass.
 * Changed `value` field for `databricks.sdk.service.sql.AlertOptions` to `any` dataclass.
 * Removed `is_db_admin` field for `databricks.sdk.service.sql.User`.
 * Removed `profile_image_url` field for `databricks.sdk.service.sql.User`.
 * Added `databricks.sdk.service.sql.AlertQuery` dataclass.

OpenAPI SHA: 0a1949ba96f71680dad30e06973eaae85b1307bb, Date: 2023-07-18

## 0.1.12

* Beta release ([#198](https://github.com/databricks/databricks-sdk-py/pull/198)).
* Documentation improvements ([#197](https://github.com/databricks/databricks-sdk-py/pull/197)).
* Make `dbutils` type stubs consistent with runtime implementation ([#196](https://github.com/databricks/databricks-sdk-py/pull/196)).
* Regenerated from OpenAPI spec ([#199](https://github.com/databricks/databricks-sdk-py/pull/199)).

API changes:

* Renamed `compute.BaseClusterInfo` to `compute.ClusterSpec`
* Renamed `compute.ClusterInfo` to `compute.ClusterDetails`
* Renamed `jobs.JobTaskSettings` to `jobs.Task`
* Renamed `jobs.RunSubmitTaskSettings` to `jobs.SubmitTask`
* Renamed `jobs.JobWebhookNotifications` to `jobs.WebhookNotifications`
* Renamed `jobs.CreateJobFormat` to `jobs.Format`
* Renamed `jobs.GitSourceGitProvider` to `jobs.GitProvider`
* Renamed `jobs.FileArrivalTriggerSettings` to `jobs.FileArrivalTriggerConfiguration`

## 0.1.11

* Added Sphinx documentation ([#184](https://github.com/databricks/databricks-sdk-py/pull/184), [#191](https://github.com/databricks/databricks-sdk-py/pull/191), [#183](https://github.com/databricks/databricks-sdk-py/pull/183), [#193](https://github.com/databricks/databricks-sdk-py/pull/193)).
* Integrated with ReadTheDocs service ([#188](https://github.com/databricks/databricks-sdk-py/pull/188), [#189](https://github.com/databricks/databricks-sdk-py/pull/189), [#190](https://github.com/databricks/databricks-sdk-py/pull/190)).
* Create a deepcopy of config in api client ([#172](https://github.com/databricks/databricks-sdk-py/pull/172)).
* Fix client/secret auth ([#186](https://github.com/databricks/databricks-sdk-py/pull/186)).
* Increase DBFS copy buffer size ([#185](https://github.com/databricks/databricks-sdk-py/pull/185)).
* Move classes to other repository ([#192](https://github.com/databricks/databricks-sdk-py/pull/192)).
* Relax `requests` version upper bound to <3 ([#138](https://github.com/databricks/databricks-sdk-py/pull/138)).

## 0.1.10

* Regenerate from OpenAPI spec ([#176](https://github.com/databricks/databricks-sdk-py/pull/176)).
* Added improved notebook-native authentication ([#152](https://github.com/databricks/databricks-sdk-py/pull/152)).
* Added methods to provide extra user agent and upstream user agent to SDK config ([#163](https://github.com/databricks/databricks-sdk-py/pull/163)).
* Added more missing `Optional` type hints ([#171](https://github.com/databricks/databricks-sdk-py/pull/171), [#177](https://github.com/databricks/databricks-sdk-py/pull/177)).
* Correctly serialize external entities ([#178](https://github.com/databricks/databricks-sdk-py/pull/178)).
* Correctly serialize external enum values in paths ([#179](https://github.com/databricks/databricks-sdk-py/pull/179)).
* Mark non-required fields as `Optional` ([#170](https://github.com/databricks/databricks-sdk-py/pull/170)).
* Synchronize auth permutation tests with Go SDK ([#165](https://github.com/databricks/databricks-sdk-py/pull/165)).

## 0.1.9

* Added new services from OpenAPI spec ([#145](https://github.com/databricks/databricks-sdk-py/pull/145), [#159](https://github.com/databricks/databricks-sdk-py/pull/159)).
* Added consistent usage of the `upload(path, IO)` and `download(path) -> IO` across file-related operations ([#148](https://github.com/databricks/databricks-sdk-py/pull/148)).
* Added Databricks Metadata Service credential provider ([#139](https://github.com/databricks/databricks-sdk-py/pull/139), [#130](https://github.com/databricks/databricks-sdk-py/pull/130)).
* Added exposing runtime credential provider without changing user namespace ([#140](https://github.com/databricks/databricks-sdk-py/pull/140)).
* Added a check for `is not None` for primitive fields in `as_dict()` ([#147](https://github.com/databricks/databricks-sdk-py/pull/147)).
* Fixed bug related to boolean flags and convert `True` to `true` in query strings ([#156](https://github.com/databricks/databricks-sdk-py/pull/156)).
* Fixed generation of external entities ([#146](https://github.com/databricks/databricks-sdk-py/pull/146)).
* Make u2m authentication work with new CLI ([#150](https://github.com/databricks/databricks-sdk-py/pull/150)).

## 0.1.8

 * Regenerated from OpenAPI spec ([#124](https://github.com/databricks/databricks-sdk-py/pull/124)).
 * Added `codecov.io` badge ([#126](https://github.com/databricks/databricks-sdk-py/pull/126)).
 * Improved readme with links to examples ([#125](https://github.com/databricks/databricks-sdk-py/pull/125)).
 * Fixed `AttributeError: 'NoneType' object has no attribute 'debug_truncate_bytes' when instantiating an ApiClient` with empty config ([#123](https://github.com/databricks/databricks-sdk-py/pull/123)).

## 0.1.7

* Added an extensive set of examples ([#113](https://github.com/databricks/databricks-sdk-py/pull/113)).
* Fixed broken `dbutils.fs.mount` and `dbutils.fs.updateMount` ([#119](https://github.com/databricks/databricks-sdk-py/pull/119)).
* Ignore `.netrc` when sending unauthenticated requests for OAuth handshake ([#108](https://github.com/databricks/databricks-sdk-py/pull/108)).
* Make ApiClient more `pyodide` friendly ([#114](https://github.com/databricks/databricks-sdk-py/pull/114)).
* Persist token acquired through `external-browser` auth type ([#110](https://github.com/databricks/databricks-sdk-py/pull/110)).
* Prototype for notebook-native auth ([#115](https://github.com/databricks/databricks-sdk-py/pull/115)).
* Rename `RefreshableCredentials` to `SessionCredentials` ([#116](https://github.com/databricks/databricks-sdk-py/pull/116)).
* Use shell for opening `az` cli on Windows ([#117](https://github.com/databricks/databricks-sdk-py/pull/117)).

## 0.1.6

* Preserve original `databricks.sdk.runtime` for internal purposes ([#96](https://github.com/databricks/databricks-sdk-py/pull/96)).

## 0.1.5

* Pin version of `requests` to `>=2.28.1,<2.29.0`, so that we don't get `ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with LibreSSL 2.8.3`. See [this issue](https://github.com/psf/requests/issues/6432) for more information.

## 0.1.4

* Removed experimental redacting logger filter for `dbutils.secrets.get('scope', 'key')`, that was causing Jupyter Kernels to hang ([#92](https://github.com/databricks/databricks-sdk-py/pull/92)).
* Fixed error handling for SCIM and CommandExecution APIs ([#94](https://github.com/databricks/databricks-sdk-py/pull/94)).
* Created `dependabot.yml` ([#89](https://github.com/databricks/databricks-sdk-py/pull/89)).

## 0.1.3

* Added support for sdist ([#86](https://github.com/databricks/databricks-sdk-py/pull/86)).
* Removed redundant newlines from AAD OAuth responses ([#85](https://github.com/databricks/databricks-sdk-py/pull/85)).
* Update README.md with doc links ([#83](https://github.com/databricks/databricks-sdk-py/pull/83)).

## 0.1.2

* Fix `dbutils.fs.put()` utility ([#82](https://github.com/databricks/databricks-sdk-py/pull/82)).

## 0.1.1

* Improve Azure AD auth ([#80](https://github.com/databricks/databricks-sdk-py/pull/80)).

## 0.1.0

* Make code working with new OpenAPI packaging ([#78](https://github.com/databricks/databricks-sdk-py/pull/78)).
* Added `bricks` CLI authentication ([#66](https://github.com/databricks/databricks-sdk-py/pull/66)).
* Use `databricks.sdk.oauth` logger for single-request server ([#74](https://github.com/databricks/databricks-sdk-py/pull/74)).
* Support more Azure environments ([#73](https://github.com/databricks/databricks-sdk-py/pull/73)).
* Added SECURITY.md ([#64](https://github.com/databricks/databricks-sdk-py/pull/64)).

API changes:

* Moved `clusterpolicies` APIs to `compute` package.
* Moved `clusters` APIs to `compute` package.
* Moved `commands` APIs to `compute` package.
* Moved `globalinitscripts` APIs to `compute` package.
* Moved `instancepools` APIs to `compute` package.
* Moved `scim` APIs to `iam` package.
* Moved `permissions` APIs to `iam` package.
* Moved `ipaccesslists` APIs to `settings` package.
* Moved `tokenmanagement` APIs to `settings` package.
* Moved `tokens` APIs to `settings` package.
* Moved `workspaceconf` APIs to `settings` package.
* Moved `gitcredentials` APIs to `workspace` package.
* Moved `repos` APIs to `workspace` package.
* Moved `secrets` APIs to `workspace` package.
* Split `unitcatalog` package to `catalog` and `sharing`.
* Renamed `mlflow` package to `ml`.
* Renamed `dbfs` package to `files`.
* Renamed `deployment` package to `provisioning`.
* Renamed `endpoints` package to `serving`.
* Renamed `clusters.List` type to `compute.ListClustersRequest`.
* Renamed `jobs.ListRuns` type to `jobs.ListRunsRequest`.
* Renamed `jobs.ExportRun` type to `jobs.ExportRunRequest`.
* Renamed `clusterpolicies.List` type to `compute.ListClusterPoliciesRequest`.
* Renamed `jobs.List` type to `jobs.ListJobsRequest`.
* Renamed `permissions.GetPermissionLevels` type to `iam.GetPermissionLevelsRequest`.
* Renamed `pipelines.ListPipelineEvents` type to `pipelines.ListPipelineEventsRequest`.
* Renamed `pipelines.ListPipelines` type to `pipelines.ListPipelinesRequest`.
* Renamed `workspaceconf.GetStatus` type to `settings.GetStatusRequest`.
* Renamed `repos.List` type to `workspace.ListReposRequest`.
* Renamed `tokenmanagement.List` type to `settings.ListTokenManagementRequest`.
* Renamed `workspace.Export` type to `workspace.ExportRequest`.
* Renamed `workspace.List` type to `workspace.ListWorkspaceRequest`.

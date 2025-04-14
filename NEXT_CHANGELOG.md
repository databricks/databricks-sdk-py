# NEXT CHANGELOG

## Release v0.50.0

### New Features and Improvements

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added [w.enable_export_notebook](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/settings/enable_export_notebook.html) workspace-level service, [w.enable_notebook_table_clipboard](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/settings/enable_notebook_table_clipboard.html) workspace-level service and [w.enable_results_downloading](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/settings/enable_results_downloading.html) workspace-level service.
* Added `get_credentials_for_trace_data_download()` and `get_credentials_for_trace_data_upload()` methods for [w.experiments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/experiments.html) workspace-level service.
* Added `get_download_full_query_result()` method for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service.
* Added `get_published_dashboard_token_info()` method for [w.lakeview_embedded](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/lakeview_embedded.html) workspace-level service.
* Added `binding_workspace_ids` field for `databricks.sdk.service.billing.BudgetPolicy`.
* Added `download_id` field for `databricks.sdk.service.dashboards.GenieGenerateDownloadFullQueryResultResponse`.
* Added `dashboard_output` field for `databricks.sdk.service.jobs.RunOutput`.
* Added `dashboard_task` and `power_bi_task` fields for `databricks.sdk.service.jobs.RunTask`.
* Added `dashboard_task` and `power_bi_task` fields for `databricks.sdk.service.jobs.SubmitTask`.
* Added `dashboard_task` and `power_bi_task` fields for `databricks.sdk.service.jobs.Task`.
* Added `include_features` field for `databricks.sdk.service.ml.CreateForecastingExperimentRequest`.
* Added `models` field for `databricks.sdk.service.ml.LogInputs`.
* Added `dataset_digest`, `dataset_name` and `model_id` fields for `databricks.sdk.service.ml.LogMetric`.
* Added `dataset_digest`, `dataset_name`, `model_id` and `run_id` fields for `databricks.sdk.service.ml.Metric`.
* Added `model_inputs` field for `databricks.sdk.service.ml.RunInputs`.
* Added `client_application` field for `databricks.sdk.service.sql.QueryInfo`.
* Added `geography` and `geometry` enum values for `databricks.sdk.service.catalog.ColumnTypeName`.
* Added `allocation_timeout_no_healthy_and_warmed_up_clusters`, `docker_container_creation_exception`, `docker_image_too_large_for_instance_exception` and `docker_invalid_os_exception` enum values for `databricks.sdk.service.compute.TerminationReasonCode`.
* Added `standard` enum value for `databricks.sdk.service.jobs.PerformanceTarget`.
* Added `can_view` enum value for `databricks.sdk.service.sql.WarehousePermissionLevel`.
* [Breaking] Changed `generate_download_full_query_result()` method for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service . Method path has changed.
* [Breaking] Changed waiter for [CommandExecutionAPI.create](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/compute/command_execution.html#databricks.sdk.service.compute.CommandExecutionAPI.create) method.
* [Breaking] Changed waiter for [CommandExecutionAPI.execute](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/compute/command_execution.html#databricks.sdk.service.compute.CommandExecutionAPI.execute) method.
* [Breaking] Removed `error`, `status` and `transient_statement_id` fields for `databricks.sdk.service.dashboards.GenieGenerateDownloadFullQueryResultResponse`.
* [Breaking] Removed `balanced` and `cost_optimized` enum values for `databricks.sdk.service.jobs.PerformanceTarget`.
* [Breaking] Removed [PipelinesAPI.wait_get_pipeline_running](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/pipelines/pipelines.html#databricks.sdk.service.pipelines.PipelinesAPI.wait_get_pipeline_running) method.

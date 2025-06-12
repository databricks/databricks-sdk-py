# NEXT CHANGELOG

## Release v0.57.0

### New Features and Improvements

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added [w.ai_builder](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/aibuilder/ai_builder.html) workspace-level service.
* Added [w.feature_store](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/feature_store.html) workspace-level service.
* Added `expiration_time` field for `databricks.sdk.service.database.DatabaseCredential`.
* Added `effective_stopped` field for `databricks.sdk.service.database.DatabaseInstance`.
* Added `existing_pipeline_id` field for `databricks.sdk.service.database.SyncedTableSpec`.
* Added `pipeline_id` field for `databricks.sdk.service.database.SyncedTableStatus`.
* Added `dbt_platform_output` field for `databricks.sdk.service.jobs.RunOutput`.
* Added `dbt_platform_task` field for `databricks.sdk.service.jobs.RunTask`.
* Added `dbt_platform_task` field for `databricks.sdk.service.jobs.SubmitTask`.
* Added `dbt_platform_task` field for `databricks.sdk.service.jobs.Task`.
* Added `environment` field for `databricks.sdk.service.pipelines.CreatePipeline`.
* Added `environment` field for `databricks.sdk.service.pipelines.EditPipeline`.
* Added `environment` field for `databricks.sdk.service.pipelines.PipelineSpec`.
* Added `description` field for `databricks.sdk.service.serving.ServingEndpoint`.
* Added `description` field for `databricks.sdk.service.serving.ServingEndpointDetailed`.
* Added `cancelled`, `error`, `queued`, `running`, `starting` and `success` enum values for `databricks.sdk.service.jobs.DbtPlatformRunStatus`.
* [Breaking] Changed `status` field for `databricks.sdk.service.jobs.DbtCloudJobRunStep` to type `databricks.sdk.service.jobs.DbtPlatformRunStatus` dataclass.
* [Breaking] Removed [w.custom_llms](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/aibuilder/custom_llms.html) workspace-level service.
* [Breaking] Removed `table_serving_url` field for `databricks.sdk.service.database.DatabaseTable`.
* [Breaking] Removed `table_serving_url` field for `databricks.sdk.service.database.SyncedDatabaseTable`.
* [Breaking] Removed `pipeline_id` field for `databricks.sdk.service.database.SyncedTableSpec`.
* [Breaking] Removed `cancelled`, `error`, `queued`, `running`, `starting` and `success` enum values for `databricks.sdk.service.jobs.DbtCloudRunStatus`.

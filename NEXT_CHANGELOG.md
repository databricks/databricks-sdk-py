# NEXT CHANGELOG

## Release v0.77.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `git_repository` field for `databricks.sdk.service.apps.App`.
* Add `git_source` field for `databricks.sdk.service.apps.AppDeployment`.
* Add `experiment_spec` field for `databricks.sdk.service.apps.AppManifestAppResourceSpec`.
* Add `experiment` field for `databricks.sdk.service.apps.AppResource`.
* Add `git_repository` field for `databricks.sdk.service.apps.AppUpdate`.
* Add `excluded_table_full_names` field for `databricks.sdk.service.dataquality.AnomalyDetectionConfig`.
* Add `group_name` field for `databricks.sdk.service.jobs.JobRunAs`.
* Add `row_filter` field for `databricks.sdk.service.pipelines.TableSpecificConfig`.
* Add `spec` and `status` fields for `databricks.sdk.service.postgres.Endpoint`.
* Add `excluded_table_full_names` field for `databricks.sdk.service.qualitymonitorv2.AnomalyDetectionConfig`.
* Add `execute` and `use_connection` enum values for `databricks.sdk.service.apps.AppManifestAppResourceUcSecurableSpecUcSecurablePermission`.
* Add `function` and `connection` enum values for `databricks.sdk.service.apps.AppManifestAppResourceUcSecurableSpecUcSecurableType`.
* Add `select`, `execute` and `use_connection` enum values for `databricks.sdk.service.apps.AppResourceUcSecurableUcSecurablePermission`.
* Add `table`, `function` and `connection` enum values for `databricks.sdk.service.apps.AppResourceUcSecurableUcSecurableType`.
* [Breaking] Remove `apply_environment()` method for [w.pipelines](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/pipelines/pipelines.html) workspace-level service.
* [Breaking] Remove `autoscaling_limit_max_cu`, `autoscaling_limit_min_cu`, `current_state`, `disabled`, `effective_autoscaling_limit_max_cu`, `effective_autoscaling_limit_min_cu`, `effective_disabled`, `effective_pooler_mode`, `effective_settings`, `effective_suspend_timeout_duration`, `endpoint_type`, `host`, `last_active_time`, `pending_state`, `pooler_mode`, `settings`, `start_time`, `suspend_time` and `suspend_timeout_duration` fields for `databricks.sdk.service.postgres.Endpoint`.
* Add `spec` and `status` fields for `databricks.sdk.service.postgres.Branch`.
* Add `spec` and `status` fields for `databricks.sdk.service.postgres.Project`.
* [Breaking] Remove `current_state`, `default`, `effective_default`, `effective_is_protected`, `effective_source_branch`, `effective_source_branch_lsn`, `effective_source_branch_time`, `is_protected`, `logical_size_bytes`, `pending_state`, `source_branch`, `source_branch_lsn`, `source_branch_time` and `state_change_time` fields for `databricks.sdk.service.postgres.Branch`.
* [Breaking] Remove `branch_logical_size_limit_bytes`, `compute_last_active_time`, `default_endpoint_settings`, `display_name`, `effective_default_endpoint_settings`, `effective_display_name`, `effective_history_retention_duration`, `effective_pg_version`, `effective_settings`, `history_retention_duration`, `pg_version`, `settings` and `synthetic_storage_size_bytes` fields for `databricks.sdk.service.postgres.Project`.
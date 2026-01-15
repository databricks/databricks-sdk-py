# NEXT CHANGELOG

## Release v0.79.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `full_refresh_window` field for `databricks.sdk.service.pipelines.IngestionPipelineDefinition`.
* Add `auto_full_refresh_policy` field for `databricks.sdk.service.pipelines.TableSpecificConfig`.
* Add `hosts` field for `databricks.sdk.service.postgres.EndpointStatus`.
* Add `owner` field for `databricks.sdk.service.postgres.ProjectStatus`.
* Add `validity_check_configurations` field for `databricks.sdk.service.qualitymonitorv2.QualityMonitor`.
* Add `burst_scaling_enabled` field for `databricks.sdk.service.serving.PtServedModel`.
* Add `system_managed` enum value for `databricks.sdk.service.jobs.JobDeploymentKind`.
* Add `endpoint_type_read_write` and `endpoint_type_read_only` enum values for `databricks.sdk.service.postgres.EndpointType`.
* Add `deleted` enum value for `databricks.sdk.service.vectorsearch.EndpointStatusState`.
* [Breaking] Remove `host`, `last_active_time`, `start_time` and `suspend_time` fields for `databricks.sdk.service.postgres.EndpointStatus`.
* [Breaking] Remove `compute_last_active_time` field for `databricks.sdk.service.postgres.ProjectStatus`.
* [Breaking] Remove `read_write` and `read_only` enum values for `databricks.sdk.service.postgres.EndpointType`.
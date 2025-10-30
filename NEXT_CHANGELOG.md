# NEXT CHANGELOG

## Release v0.71.0

### New Features and Improvements

### Bug Fixes

- Fix the issue where `FilesExt.upload`'s second parameter was changed from `contents` to `content` unintentionally. Now the interface is backward compatible to versions previous than 0.69.0.

### Documentation

### Internal Changes

### API Changes
* Add `instance_profile_arn` field for `databricks.sdk.service.compute.InstancePoolAwsAttributes`.
* Add `continuous`, `sliding` and `tumbling` fields for `databricks.sdk.service.ml.TimeWindow`.
* Add `usage_policy_id` field for `databricks.sdk.service.pipelines.CreatePipeline`.
* Add `usage_policy_id` field for `databricks.sdk.service.pipelines.EditPipeline`.
* Add `usage_policy_id` field for `databricks.sdk.service.pipelines.PipelineSpec`.
* Add `read_files_bytes` field for `databricks.sdk.service.sql.QueryMetrics`.
* Add `select` enum value for `databricks.sdk.service.apps.AppManifestAppResourceUcSecurableSpecUcSecurablePermission`.
* Add `table` enum value for `databricks.sdk.service.apps.AppManifestAppResourceUcSecurableSpecUcSecurableType`.
* Add `decommission_started` and `decommission_ended` enum values for `databricks.sdk.service.compute.EventType`.
* Add `dbr_image_resolution_failure` enum value for `databricks.sdk.service.compute.TerminationReasonCode`.
* Add `dbr_image_resolution_failure` enum value for `databricks.sdk.service.sql.TerminationReasonCode`.
* [Breaking] Change `offline_store_config` and `online_store_config` fields for `databricks.sdk.service.ml.MaterializedFeature` to no longer be required.
* Change `offline_store_config` and `online_store_config` fields for `databricks.sdk.service.ml.MaterializedFeature` to no longer be required.
* [Breaking] Change `lifecycle_state` field for `databricks.sdk.service.sql.AlertV2` to type `databricks.sdk.service.sql.AlertLifecycleState` dataclass.
* [Breaking] Remove `table` field for `databricks.sdk.service.jobs.TriggerSettings`.
* [Breaking] Remove `duration` and `offset` fields for `databricks.sdk.service.ml.TimeWindow`.
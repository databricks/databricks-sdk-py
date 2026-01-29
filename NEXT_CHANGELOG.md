# NEXT CHANGELOG

## Release v0.82.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `backfill_source` field for `databricks.sdk.service.ml.KafkaConfig`.
* Add `clone_mode` field for `databricks.sdk.service.pipelines.ClonePipelineRequest`.
* Add `burst_scaling_enabled` field for `databricks.sdk.service.serving.ServedEntityInput`.
* Add `burst_scaling_enabled` field for `databricks.sdk.service.serving.ServedEntityOutput`.
* Add `burst_scaling_enabled` field for `databricks.sdk.service.serving.ServedModelInput`.
* Add `burst_scaling_enabled` field for `databricks.sdk.service.serving.ServedModelOutput`.
* [Breaking] Change `create_role()` method for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service with new required argument order.
* Change `role_id` field for `databricks.sdk.service.postgres.CreateRoleRequest` to no longer be required.
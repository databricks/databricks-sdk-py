# NEXT CHANGELOG

## Release v0.67.0

### New Features and Improvements

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `update_notifications()` method for [w.serving_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/serving/serving_endpoints.html) workspace-level service.
* Add `parameters` field for `databricks.sdk.service.dashboards.GenieQueryAttachment`.
* Add `database_instance_name` field for `databricks.sdk.service.database.CreateDatabaseInstanceRoleRequest`.
* Add `custom_tags`, `effective_custom_tags`, `effective_usage_policy_id` and `usage_policy_id` fields for `databricks.sdk.service.database.DatabaseInstance`.
* Add `effective_attributes` and `instance_name` fields for `databricks.sdk.service.database.DatabaseInstanceRole`.
* Add `external_use_schema` enum value for `databricks.sdk.service.catalog.Privilege`.
* Add `stream_native` enum value for `databricks.sdk.service.catalog.SystemType`.
* Add `exceeded_max_token_length_exception` enum value for `databricks.sdk.service.dashboards.MessageErrorType`.
* Change `name` field for `databricks.sdk.service.database.DatabaseInstanceRole` to be required.
* [Breaking] Change `name` field for `databricks.sdk.service.database.DatabaseInstanceRole` to be required.
# NEXT CHANGELOG

## Release v0.63.0

### New Features and Improvements

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added [w.policies](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/policies.html) workspace-level service and [w.temporary_path_credentials](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/temporary_path_credentials.html) workspace-level service.
* Added `create()` method for [w.tables](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/tables.html) workspace-level service.
* Added `list_database_catalogs()`, `list_synced_database_tables()`, `update_database_catalog()` and `update_synced_database_table()` methods for [w.database](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/database/database.html) workspace-level service.
* Added `first_on_demand` field for `databricks.sdk.service.compute.GcpAttributes`.
* Added `usage_policy_id` field for `databricks.sdk.service.jobs.CreateJob`.
* Added `usage_policy_id` field for `databricks.sdk.service.jobs.JobSettings`.
* Added `usage_policy_id` field for `databricks.sdk.service.jobs.SubmitRun`.
* Added `client_request_id` and `usage_context` fields for `databricks.sdk.service.serving.QueryEndpointInput`.
* Added `channel_id`, `channel_id_set`, `oauth_token` and `oauth_token_set` fields for `databricks.sdk.service.settings.SlackConfig`.
* Added `snapshot` enum value for `databricks.sdk.service.ml.PublishSpecPublishMode`.
* [Breaking] Changed `publish_mode` field for `databricks.sdk.service.ml.PublishSpec` to be required.
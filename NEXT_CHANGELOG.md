# NEXT CHANGELOG

## Release v0.95.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `dataframe_schema`, `filter_condition` and `transformation_sql` fields for `databricks.sdk.service.ml.DeltaTableSource`.
* Add `environment_version` field for `databricks.sdk.service.pipelines.PipelinesEnvironment`.
* Add `reset_checkpoint_selection` field for `databricks.sdk.service.pipelines.StartUpdate`.
* [Breaking] Remove `oauth2_app_client_id` and `oauth2_app_integration_id` fields for `databricks.sdk.service.apps.Space`.
* Add `create_database()`, `delete_database()`, `get_database()`, `list_databases()` and `update_database()` methods for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service.
* Add `postgres` field for `databricks.sdk.service.apps.AppResource`.
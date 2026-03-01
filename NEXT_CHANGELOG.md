# NEXT CHANGELOG

## Release v0.95.0

### New Features and Improvements
* Added `Config.discovery_url` config field (`DATABRICKS_DISCOVERY_URL` env var). When set, OIDC endpoints are fetched directly from this URL instead of the default host-type-based logic. Mirrors `discoveryUrl` in the Java SDK.
* The OAuth token cache filename now includes the config profile name (if set) and uses a serialized map to prevent hash collisions. All users will need to reauthenticate once after upgrading.

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
* Add `enable_pg_native_login` field for `databricks.sdk.service.postgres.ProjectSpec`.
* Add `enable_pg_native_login` field for `databricks.sdk.service.postgres.ProjectStatus`.
* [Breaking] Remove `node_type_flexibility` field for `databricks.sdk.service.compute.EditInstancePool`.

# NEXT CHANGELOG

## Release v0.95.0

### New Features and Improvements
* Added `Config.discovery_url` config field (`DATABRICKS_DISCOVERY_URL` env var). When set, OIDC endpoints are fetched directly from this URL instead of the default host-type-based logic. Mirrors `discoveryUrl` in the Java SDK.
* The OAuth token cache filename now includes the config profile name (if set) and uses a serialized map to prevent hash collisions. All users will need to reauthenticate once after upgrading.

### Security

### Bug Fixes

### Documentation

### Internal Changes
* Implement dynamic auth token stale period based on initial token lifetime. Increased up to 20 mins for standard OAuth with proportionally shorter periods for short-lived tokens. Providing a stale_duration in the constructor of the Refreshable class will use that fixed value instead. To match the previous default, pass stale_duration=timedelta(minutes=5).

### API Changes
* Add `dataframe_schema`, `filter_condition` and `transformation_sql` fields for `databricks.sdk.service.ml.DeltaTableSource`.
* Add `environment_version` field for `databricks.sdk.service.pipelines.PipelinesEnvironment`.
* Add `reset_checkpoint_selection` field for `databricks.sdk.service.pipelines.StartUpdate`.
* [Breaking] Remove `oauth2_app_client_id` and `oauth2_app_integration_id` fields for `databricks.sdk.service.apps.Space`.
* Add `create_database()`, `delete_database()`, `get_database()`, `list_databases()` and `update_database()` methods for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service.
* Add `postgres` field for `databricks.sdk.service.apps.AppResource`.

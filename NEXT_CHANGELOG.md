# NEXT CHANGELOG

## Release v0.61.0

### New Features and Improvements

### Bug Fixes

* Fix `Config.oauth_token()` to avoid re-creating a new `CredentialsProvider` at each call. This fix indirectly makes `oauth_token()` benefit from the internal caching mechanism of some providers. 

### Documentation

### Internal Changes

### API Changes
* Added [w.clean_room_asset_revisions](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/cleanrooms/clean_room_asset_revisions.html) workspace-level service and [w.clean_room_auto_approval_rules](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/cleanrooms/clean_room_auto_approval_rules.html) workspace-level service.
* Added `create_clean_room_asset_review()` method for [w.clean_room_assets](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/cleanrooms/clean_room_assets.html) workspace-level service.
* Added `latest_monitor_failure_msg` field for `databricks.sdk.service.catalog.CreateMonitor`.
* Added `latest_monitor_failure_msg` field for `databricks.sdk.service.catalog.UpdateMonitor`.
* Added `share` field for `databricks.sdk.service.sharing.ListProviderShareAssetsResponse`.
* Added `projected_remaining_wallclock_time_ms` field for `databricks.sdk.service.sql.QueryMetrics`.
* Added `unspecified` enum value for `databricks.sdk.service.catalog.MonitorCronSchedulePauseStatus`.
* Added `unknown` enum value for `databricks.sdk.service.catalog.MonitorRefreshInfoState`.
* Added `unknown_trigger` enum value for `databricks.sdk.service.catalog.MonitorRefreshInfoTrigger`.
* Added `message_attachment_too_long_error` enum value for `databricks.sdk.service.dashboards.MessageErrorType`.
* Added `mask` enum value for `databricks.sdk.service.serving.AiGatewayGuardrailPiiBehaviorBehavior`.
* [Breaking] Added waiter for [CleanRoomsAPI.create](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/cleanrooms/clean_rooms.html#databricks.sdk.service.cleanrooms.CleanRoomsAPI.create) method.
* [Breaking] Added waiter for [DatabaseAPI.create_database_instance](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/database/database.html#databricks.sdk.service.database.DatabaseAPI.create_database_instance) method.
* [Breaking] Changed `cancel_refresh()` method for [w.quality_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/quality_monitors.html) workspace-level service to start returning `databricks.sdk.service.catalog.CancelRefreshResponse` dataclass.
* [Breaking] Changed `create()` method for [w.quality_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/quality_monitors.html) workspace-level service with new required argument order.
* [Breaking] Changed `delete()` method for [w.quality_monitors](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/quality_monitors.html) workspace-level service to start returning `databricks.sdk.service.catalog.DeleteMonitorResponse` dataclass.
* [Breaking] Changed `refresh_id` field for `databricks.sdk.service.catalog.CancelRefreshRequest` to type `int` dataclass.
* [Breaking] Changed `refresh_id` field for `databricks.sdk.service.catalog.GetRefreshRequest` to type `int` dataclass.
* [Breaking] Changed `monitor_version` field for `databricks.sdk.service.catalog.MonitorInfo` to type `int` dataclass.
* Changed `output_schema_name` field for `databricks.sdk.service.catalog.MonitorInfo` to be required.
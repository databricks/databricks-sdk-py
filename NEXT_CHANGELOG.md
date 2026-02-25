# NEXT CHANGELOG

## Release v0.93.0

### New Features and Improvements

### Security

### Bug Fixes
* Fixed Databricks CLI authentication to detect when the cached token's scopes don't match the SDK's configured scopes. Previously, a scope mismatch was silently ignored, causing requests to use wrong permissions. The SDK now raises an error with instructions to re-authenticate.


### Documentation

### Internal Changes

### API Changes
* Add `parameters` field for `databricks.sdk.service.pipelines.StartUpdate`.
* Add `parameters` field for `databricks.sdk.service.pipelines.UpdateInfo`.
* [Breaking] Change `get_download_full_query_result()` method for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service with new required argument order.
* [Breaking] Change `name` field for `databricks.sdk.service.apps.Space` to be required.
* Change `name` field for `databricks.sdk.service.apps.Space` to be required.
* [Breaking] Change `id` and `user_id` fields for `databricks.sdk.service.dashboards.GenieConversation` to no longer be required.
* [Breaking] Change `created_timestamp` and `title` fields for `databricks.sdk.service.dashboards.GenieConversationSummary` to no longer be required.
* [Breaking] Change `download_id_signature` field for `databricks.sdk.service.dashboards.GenieGetDownloadFullQueryResultRequest` to be required.
* [Breaking] Change `id` field for `databricks.sdk.service.dashboards.GenieMessage` to no longer be required.
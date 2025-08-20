# NEXT CHANGELOG

## Release v0.64.0

### New Features and Improvements

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added `databricks.sdk.service.settingsv2` and `databricks.sdk.service.tags` packages.
* Added [w.apps_settings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/apps/apps_settings.html) workspace-level service.
* Added [w.entity_tag_assignments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/entity_tag_assignments.html) workspace-level service and [w.rfa](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/rfa.html) workspace-level service.
* Added [a.account_settings_v2](https://databricks-sdk-py.readthedocs.io/en/latest/account/settingsv2/account_settings_v2.html) account-level service and [w.workspace_settings_v2](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settingsv2/workspace_settings_v2.html) workspace-level service.
* Added [w.tag_policies](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/tags/tag_policies.html) workspace-level service.
* Added `delete_conversation_message()`, `list_conversation_messages()` and `send_message_feedback()` methods for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service.
* Added `include_all` field for `databricks.sdk.service.dashboards.GenieListConversationsRequest`.
* Added `effective_usage_policy_id` field for `databricks.sdk.service.jobs.BaseJob`.
* Added `effective_usage_policy_id` field for `databricks.sdk.service.jobs.BaseRun`.
* Added `effective_usage_policy_id` field for `databricks.sdk.service.jobs.Job`.
* Added `effective_usage_policy_id` field for `databricks.sdk.service.jobs.Run`.
* Added `tokens` field for `databricks.sdk.service.serving.AiGatewayRateLimit`.
* Added `usage_policy_id` field for `databricks.sdk.service.serving.ServingEndpoint`.
* Added `effective_run_as` and `run_as` fields for `databricks.sdk.service.sql.AlertV2`.
* Added `cache_query_id` field for `databricks.sdk.service.sql.QueryInfo`.
* Added `model_endpoint_name_for_query` field for `databricks.sdk.service.vectorsearch.EmbeddingSourceColumn`.
* [Breaking] Removed `environment_settings` field for `databricks.sdk.service.catalog.ConnectionInfo`.
* [Breaking] Removed `environment_settings` field for `databricks.sdk.service.catalog.CreateConnection`.
* [Breaking] Removed `environment_settings` field for `databricks.sdk.service.catalog.UpdateConnection`.
* [Breaking] Removed `comment`, `display_name` and `tags` fields for `databricks.sdk.service.sharing.Share`.
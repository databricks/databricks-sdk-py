# NEXT CHANGELOG

## Release v0.51.0

### New Features and Improvements
* Enabled asynchronous token refreshes by default. A new `disable_async_token_refresh` configuration option has been added to allow disabling this feature if necessary ([#952](https://github.com/databricks/databricks-sdk-py/pull/952)).
  To disable asynchronous token refresh, set the environment variable `DATABRICKS_DISABLE_ASYNC_TOKEN_REFRESH=true` or configure it within your configuration object.
  The previous `enable_experimental_async_token_refresh` option has been removed as asynchronous refresh is now the default behavior.
* Introduce support for Databricks Workload Identity Federation in GitHub workflows ([933](https://github.com/databricks/databricks-sdk-py/pull/933)).
  See README.md for instructions.
* [Breaking] Users running their workflows in GitHub Actions, which use Cloud native authentication and also have a `DATABRICKS_CLIENT_ID` and `DATABRICKS_HOST`
  environment variables set may see their authentication start failing due to the order in which the SDK tries different authentication methods.

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added [w.alerts_v2](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sql/alerts_v2.html) workspace-level service.
* Added `update_ncc_azure_private_endpoint_rule_public()` method for [a.network_connectivity](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/network_connectivity.html) account-level service.
* Added `update_endpoint_budget_policy()` and `update_endpoint_custom_tags()` methods for [w.vector_search_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/vectorsearch/vector_search_endpoints.html) workspace-level service.
* Added `created_at`, `created_by` and `metastore_id` fields for `databricks.sdk.service.catalog.SetArtifactAllowlist`.
* Added `node_type_flexibility` field for `databricks.sdk.service.compute.EditInstancePool`.
* Added `page_size` and `page_token` fields for `databricks.sdk.service.compute.GetEvents`.
* Added `next_page_token` and `prev_page_token` fields for `databricks.sdk.service.compute.GetEventsResponse`.
* Added `node_type_flexibility` field for `databricks.sdk.service.compute.GetInstancePool`.
* Added `node_type_flexibility` field for `databricks.sdk.service.compute.InstancePoolAndStats`.
* Added `effective_performance_target` field for `databricks.sdk.service.jobs.RepairHistoryItem`.
* Added `performance_target` field for `databricks.sdk.service.jobs.RepairRun`.
* [Breaking] Added `network_connectivity_config` field for `databricks.sdk.service.settings.CreateNetworkConnectivityConfigRequest`.
* [Breaking] Added `private_endpoint_rule` field for `databricks.sdk.service.settings.CreatePrivateEndpointRuleRequest`.
* Added `domain_names` field for `databricks.sdk.service.settings.NccAzurePrivateEndpointRule`.
* Added `auto_resolve_display_name` field for `databricks.sdk.service.sql.CreateAlertRequest`.
* Added `auto_resolve_display_name` field for `databricks.sdk.service.sql.CreateQueryRequest`.
* Added `budget_policy_id` field for `databricks.sdk.service.vectorsearch.CreateEndpoint`.
* Added `custom_tags` and `effective_budget_policy_id` fields for `databricks.sdk.service.vectorsearch.EndpointInfo`.
* Added `create_clean_room`, `execute_clean_room_task` and `modify_clean_room` enum values for `databricks.sdk.service.catalog.Privilege`.
* Added `dns_resolution_error` and `gcp_denied_by_org_policy` enum values for `databricks.sdk.service.compute.TerminationReasonCode`.
* Added `disabled` enum value for `databricks.sdk.service.jobs.TerminationCodeCode`.
* Added `expired` enum value for `databricks.sdk.service.settings.NccAzurePrivateEndpointRuleConnectionState`.
* [Breaking] Changed `create_network_connectivity_configuration()` and `create_private_endpoint_rule()` methods for [a.network_connectivity](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/network_connectivity.html) account-level service with new required argument order.
* [Breaking] Changed `create_index()` method for [w.vector_search_indexes](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/vectorsearch/vector_search_indexes.html) workspace-level service to return `databricks.sdk.service.vectorsearch.VectorIndex` dataclass.
* [Breaking] Changed `delete_data_vector_index()` method for [w.vector_search_indexes](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/vectorsearch/vector_search_indexes.html) workspace-level service . HTTP method/verb has changed.
* [Breaking] Changed `delete_data_vector_index()` method for [w.vector_search_indexes](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/vectorsearch/vector_search_indexes.html) workspace-level service with new required argument order.
* [Breaking] Changed `databricks.sdk.service.vectorsearch.List` dataclass to.
* [Breaking] Changed `workload_size` field for `databricks.sdk.service.serving.ServedModelInput` to type `str` dataclass.
* [Breaking] Changed `group_id` field for `databricks.sdk.service.settings.NccAzurePrivateEndpointRule` to type `str` dataclass.
* [Breaking] Changed `target_services` field for `databricks.sdk.service.settings.NccAzureServiceEndpointRule` to type `databricks.sdk.service.settings.EgressResourceTypeList` dataclass.
* [Breaking] Changed `data_array` field for `databricks.sdk.service.vectorsearch.ResultData` to type `databricks.sdk.service.vectorsearch.ListValueList` dataclass.
* [Breaking] Changed waiter for [VectorSearchEndpointsAPI.create_endpoint](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/vectorsearch/vector_search_endpoints.html#databricks.sdk.service.vectorsearch.VectorSearchEndpointsAPI.create_endpoint) method.
* [Breaking] Removed `name` and `region` fields for `databricks.sdk.service.settings.CreateNetworkConnectivityConfigRequest`.
* [Breaking] Removed `group_id` and `resource_id` fields for `databricks.sdk.service.settings.CreatePrivateEndpointRuleRequest`.
* [Breaking] Removed `null_value` field for `databricks.sdk.service.vectorsearch.Value`.
* [Breaking] Removed `large`, `medium` and `small` enum values for `databricks.sdk.service.serving.ServedModelInputWorkloadSize`.
* [Breaking] Removed `blob`, `dfs`, `mysql_server` and `sql_server` enum values for `databricks.sdk.service.settings.NccAzurePrivateEndpointRuleGroupId`.

# NEXT CHANGELOG

## Release v0.107.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Breaking Changes

### Internal Changes
* Pass `--force-refresh` to Databricks CLI `auth token` command so the SDK always receives a freshly minted token instead of a potentially stale one from the CLI's internal cache.

### API Changes
* Add `create_example()`, `delete_example()`, `get_example()`, `get_permission_levels()`, `get_permissions()`, `list_examples()`, `set_permissions()`, `update_example()` and `update_permissions()` methods for [w.supervisor_agents](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/supervisoragents/supervisor_agents.html) workspace-level service.
* Add `meta_ads_options` field for `databricks.sdk.service.pipelines.ConnectorOptions`.
* Add `meta_marketing` and `zendesk` enum values for `databricks.sdk.service.catalog.ConnectionType`.
* Add `meta_marketing` enum value for `databricks.sdk.service.pipelines.IngestionSourceType`.
* Change `guidelines` field for `databricks.sdk.service.knowledgeassistants.Example` to no longer be required.
* [Breaking] Change `guidelines` field for `databricks.sdk.service.knowledgeassistants.Example` to no longer be required.
* Change `description` field for `databricks.sdk.service.supervisoragents.Tool` to no longer be required.
* [Breaking] Change `description` field for `databricks.sdk.service.supervisoragents.Tool` to no longer be required.
* Add `r2_temp_credentials` field for `databricks.sdk.service.catalog.TemporaryCredentials`.
* Add `zendesk_support_options` field for `databricks.sdk.service.pipelines.ConnectorOptions`.
* Add `azure_key_info` field for `databricks.sdk.service.provisioning.CreateCustomerManagedKeyRequest`.
* Add `target_qps` field for `databricks.sdk.service.vectorsearch.CreateEndpoint`.
* Add `requested_target_qps` field for `databricks.sdk.service.vectorsearch.EndpointScalingInfo`.
* Add `target_qps` field for `databricks.sdk.service.vectorsearch.PatchEndpointRequest`.
* Add `jira` and `zendesk` enum values for `databricks.sdk.service.pipelines.IngestionSourceType`.
* [Breaking] Remove `min_qps` field for `databricks.sdk.service.vectorsearch.CreateEndpoint`.
* [Breaking] Remove `requested_min_qps` field for `databricks.sdk.service.vectorsearch.EndpointScalingInfo`.
* [Breaking] Remove `min_qps` field for `databricks.sdk.service.vectorsearch.PatchEndpointRequest`.
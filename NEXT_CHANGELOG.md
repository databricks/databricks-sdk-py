# NEXT CHANGELOG

## Release v0.103.0

### New Features and Improvements
* Add support for unified hosts. A single configuration profile can now be used for both account-level and workspace-level operations when the host supports it and both `account_id` and `workspace_id` are available. The `experimental_is_unified_host` flag has been removed; unified host detection is now automatic.
* Accept `DATABRICKS_OIDC_TOKEN_FILEPATH` environment variable for consistency with other Databricks SDKs (Go, CLI, Terraform). The previous `DATABRICKS_OIDC_TOKEN_FILE` is still supported as an alias.

### Security

### Bug Fixes

### Documentation

### Breaking Changes
* Drop support for Python 3.8 and 3.9. The minimum supported Python version is now 3.10, in line with the oldest supported Databricks Runtime LTS (DBR 13.3).

### Internal Changes
* Replace the async-disabling mechanism on token refresh failure with a 1-minute retry backoff. Previously, a single failed async refresh would disable proactive token renewal until the token expired. Now, the SDK waits a short cooldown period and retries, improving resilience to transient errors.
* Extract `_resolve_profile` to simplify config file loading and improve `__settings__` error messages.
* Resolve `token_audience` from the `token_federation_default_oidc_audiences` field in the host metadata discovery endpoint, removing the need for explicit audience configuration.

### API Changes
* Add `create_catalog()`, `create_synced_table()`, `delete_catalog()`, `delete_synced_table()`, `get_catalog()` and `get_synced_table()` methods for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service.
* Add `effective_file_event_queue` field for `databricks.sdk.service.catalog.CreateExternalLocation`.
* Add `effective_file_event_queue` field for `databricks.sdk.service.catalog.ExternalLocationInfo`.
* Add `effective_file_event_queue` field for `databricks.sdk.service.catalog.UpdateExternalLocation`.
* Add `column_selection` field for `databricks.sdk.service.ml.Function`.
* Add `cascade` field for `databricks.sdk.service.pipelines.DeletePipelineRequest`.
* Add `default_branch` field for `databricks.sdk.service.postgres.ProjectSpec`.
* Add `default_branch` field for `databricks.sdk.service.postgres.ProjectStatus`.
* Add `ingress` and `ingress_dry_run` fields for `databricks.sdk.service.settings.AccountNetworkPolicy`.
* Add `delete_app_thumbnail()` and `update_app_thumbnail()` methods for [w.apps](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/apps/apps.html) workspace-level service.
* Add `create_message_comment()`, `list_conversation_comments()` and `list_message_comments()` methods for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service.
* Add `apply_environment()` method for [w.pipelines](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/pipelines/pipelines.html) workspace-level service.
* Add `name` and `permission` fields for `databricks.sdk.service.apps.AppResourceApp`.
* Add `managed_encryption_settings` field for `databricks.sdk.service.catalog.CatalogInfo`.
* Add `managed_encryption_settings` field for `databricks.sdk.service.catalog.CreateCatalog`.
* Add `managed_encryption_settings` field for `databricks.sdk.service.catalog.UpdateCatalog`.
* Add `comment` field for `databricks.sdk.service.dashboards.GenieFeedback`.
* Add `thoughts` field for `databricks.sdk.service.dashboards.GenieQueryAttachment`.
* Add `comment` field for `databricks.sdk.service.dashboards.GenieSendMessageFeedbackRequest`.
* Add `request_source` field for `databricks.sdk.service.ml.DataSource`.
* Add `is_online` field for `databricks.sdk.service.ml.MaterializedFeature`.
* Add `connector_options` field for `databricks.sdk.service.pipelines.SchemaSpec`.
* Add `connector_options` field for `databricks.sdk.service.pipelines.TableSpec`.
* Add `scopes` field for `databricks.sdk.service.settings.CreateOboTokenRequest`.
* Add `gcp_endpoint` field for `databricks.sdk.service.settings.CreatePrivateEndpointRule`.
* Add `scopes` field for `databricks.sdk.service.settings.CreateTokenRequest`.
* Add `gcp_endpoint` field for `databricks.sdk.service.settings.NccPrivateEndpointRule`.
* Add `gcp_endpoint` field for `databricks.sdk.service.settings.UpdatePrivateEndpointRule`.
* Add `sql_state` field for `databricks.sdk.service.sql.StatementStatus`.
* Add `usage_policy_id` field for `databricks.sdk.service.vectorsearch.CreateEndpoint`.
* Add `index_subtype` field for `databricks.sdk.service.vectorsearch.CreateVectorIndexRequest`.
* Add `budget_policy_id` field for `databricks.sdk.service.vectorsearch.EndpointInfo`.
* Add `index_subtype` field for `databricks.sdk.service.vectorsearch.MiniVectorIndex`.
* Add `budget_policy_id` field for `databricks.sdk.service.vectorsearch.PatchEndpointBudgetPolicyResponse`.
* Add `index_subtype` field for `databricks.sdk.service.vectorsearch.VectorIndex`.
* Add `table_delta_uniform_iceberg_external_deltasharing` enum value for `databricks.sdk.service.catalog.SecurableKind`.
* Add `google_drive` enum value for `databricks.sdk.service.pipelines.IngestionSourceType`.
* Add `storage_optimized` enum value for `databricks.sdk.service.vectorsearch.EndpointType`.
* [Breaking] Remove `project` field for `databricks.sdk.service.postgres.SyncedTableSyncedTableSpec`.
* [Breaking] Remove `apps` and `lakebase` fields for `databricks.sdk.service.settings.CustomerFacingIngressNetworkPolicyRequestDestination`.
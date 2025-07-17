# NEXT CHANGELOG

## Release v0.59.0

### New Features and Improvements

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added [w.service_principal_secrets_proxy](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/oauth2/service_principal_secrets_proxy.html) workspace-level service.
* Added [w.default_warehouse_id](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/default_warehouse_id.html) workspace-level service.
* Added `database` field for `databricks.sdk.service.apps.AppResource`.
* Added `environment_settings` field for `databricks.sdk.service.catalog.ConnectionInfo`.
* Added `environment_settings` field for `databricks.sdk.service.catalog.CreateConnection`.
* Added `environment_settings` field for `databricks.sdk.service.catalog.UpdateConnection`.
* Added `read_replica_count` field for `databricks.sdk.service.ml.OnlineStore`.
* Added `page_size` field for `databricks.sdk.service.oauth2.ListServicePrincipalSecretsRequest`.
* Added `query_based_connector_config` field for `databricks.sdk.service.pipelines.TableSpecificConfig`.
* Added `projected_remaining_task_total_time_ms`, `remaining_task_count`, `runnable_tasks` and `work_to_be_done` fields for `databricks.sdk.service.sql.QueryMetrics`.
* Added `is_default_for_provider` and `name` fields for `databricks.sdk.service.workspace.CreateCredentialsRequest`.
* Added `is_default_for_provider` and `name` fields for `databricks.sdk.service.workspace.CreateCredentialsResponse`.
* Added `is_default_for_provider` and `name` fields for `databricks.sdk.service.workspace.CredentialInfo`.
* Added `is_default_for_provider` and `name` fields for `databricks.sdk.service.workspace.GetCredentialsResponse`.
* Added `is_default_for_provider` and `name` fields for `databricks.sdk.service.workspace.UpdateCredentialsRequest`.
* Added `databricks` enum value for `databricks.sdk.service.catalog.SystemType`.
* Added `driver_dns_resolution_failure` enum value for `databricks.sdk.service.compute.TerminationReasonCode`.
* Added `confluence` and `meta_marketing` enum values for `databricks.sdk.service.pipelines.IngestionSourceType`.
* Added `delta_iceberg_table` enum value for `databricks.sdk.service.sharing.TableInternalAttributesSharedTableType`.
* [Breaking] Changed `delete()` method for [w.table_constraints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/table_constraints.html) workspace-level service to start returning `databricks.sdk.service.catalog.DeleteTableConstraintResponse` dataclass.
* [Breaking] Changed `service_principal_id` field for `databricks.sdk.service.oauth2.CreateServicePrincipalSecretRequest` to type `str` dataclass.
* [Breaking] Changed `service_principal_id` field for `databricks.sdk.service.oauth2.DeleteServicePrincipalSecretRequest` to type `str` dataclass.
* [Breaking] Changed `service_principal_id` field for `databricks.sdk.service.oauth2.ListServicePrincipalSecretsRequest` to type `str` dataclass.
* [Breaking] Changed `calls` field for `databricks.sdk.service.serving.AiGatewayRateLimit` to no longer be required.
* Changed `calls` field for `databricks.sdk.service.serving.AiGatewayRateLimit` to no longer be required.
* [Breaking] Removed `create()` method for [w.dashboards](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sql/dashboards.html) workspace-level service.
* [Breaking] Removed `range` and `if_unmodified_since` fields for `databricks.sdk.service.files.DownloadRequest`.
* [Breaking] Removed `range` and `if_unmodified_since` fields for `databricks.sdk.service.files.GetMetadataRequest`.
# NEXT CHANGELOG

## Release v0.74.0

### New Features and Improvements
* Add new auth type (`runtime-oauth`) for notebooks: Introduce a new authentication mechanism that allows notebooks to authenticate using OAuth tokens

### Security

### Bug Fixes

- Fixed an issue where download from Shared Volumes could fail by falling back to Files API whenever Presigned URLs are not available.

### Documentation

### Internal Changes

### API Changes
* Add `create_space()` and `update_space()` methods for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service.
* Add `create_kafka_config()`, `delete_kafka_config()`, `get_kafka_config()`, `list_kafka_configs()` and `update_kafka_config()` methods for [w.feature_engineering](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/feature_engineering.html) workspace-level service.
* Add `delete_online_table()` method for [w.feature_store](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/feature_store.html) workspace-level service.
* Add `retrieve_user_visible_metrics()` method for [w.vector_search_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/vectorsearch/vector_search_endpoints.html) workspace-level service.
* Add `major_version` field for `databricks.sdk.service.billing.CreateBillingUsageDashboardRequest`.
* Add `include_serialized_space` field for `databricks.sdk.service.dashboards.GenieGetSpaceRequest`.
* Add `serialized_space` field for `databricks.sdk.service.dashboards.GenieSpace`.
* Add `purpose` field for `databricks.sdk.service.dashboards.TextAttachment`.
* Add `budget_policy_id` field for `databricks.sdk.service.database.NewPipelineSpec`.
* Add `model` field for `databricks.sdk.service.jobs.TriggerSettings`.
* Add `kafka_source` field for `databricks.sdk.service.ml.DataSource`.
* Add `connection_parameters` field for `databricks.sdk.service.pipelines.IngestionGatewayPipelineDefinition`.
* Add `ingest_from_uc_foreign_catalog` field for `databricks.sdk.service.pipelines.IngestionPipelineDefinition`.
* Add `rewind_spec` field for `databricks.sdk.service.pipelines.StartUpdate`.
* Add `type_text` field for `databricks.sdk.service.vectorsearch.ColumnInfo`.
* Add `foreign_catalog` enum value for `databricks.sdk.service.pipelines.IngestionSourceType`.
* Add `creating` and `create_failed` enum values for `databricks.sdk.service.settings.CustomerFacingNetworkConnectivityConfigAwsPrivateEndpointRulePrivateLinkConnectionState`.
* Add `creating` and `create_failed` enum values for `databricks.sdk.service.settings.NccAzurePrivateEndpointRuleConnectionState`.
* [Breaking] Change `destinations` field for `databricks.sdk.service.catalog.AccessRequestDestinations` to no longer be required.
* Change `destinations` field for `databricks.sdk.service.catalog.AccessRequestDestinations` to no longer be required.
* [Breaking] Change `online_store_config` field for `databricks.sdk.service.ml.MaterializedFeature` to type `databricks.sdk.service.ml.OnlineStoreConfig` dataclass.
* Add [w.workspace_entity_tag_assignments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/tags/workspace_entity_tag_assignments.html) workspace-level service.
* Add `clone()` method for [w.pipelines](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/pipelines/pipelines.html) workspace-level service.
* Add `dataset_catalog` and `dataset_schema` fields for `databricks.sdk.service.dashboards.CreateDashboardRequest`.
* Add `dataset_catalog` and `dataset_schema` fields for `databricks.sdk.service.dashboards.UpdateDashboardRequest`.
* Add `purge_data` field for `databricks.sdk.service.database.DeleteSyncedDatabaseTableRequest`.
* Add `cron_schedule` field for `databricks.sdk.service.ml.MaterializedFeature`.
* Add `truncation` field for `databricks.sdk.service.pipelines.PipelineEvent`.
* Add `gcp_service_account` field for `databricks.sdk.service.provisioning.CreateGcpKeyInfo`.
* Add `gcp_service_account` field for `databricks.sdk.service.provisioning.GcpKeyInfo`.
* Add `foreign_table` and `volume` enum values for `databricks.sdk.service.sharing.SharedDataObjectDataObjectType`.
* [Breaking] Change `time_window` field for `databricks.sdk.service.ml.Feature` to no longer be required.
* Change `time_window` field for `databricks.sdk.service.ml.Feature` to no longer be required.
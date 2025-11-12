# NEXT CHANGELOG

## Release v0.74.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `retrieve_user_visible_metrics()` method for [w.vector_search_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/vectorsearch/vector_search_endpoints.html) workspace-level service.
* Add `purpose` field for `databricks.sdk.service.dashboards.TextAttachment`.
* Add `connection_parameters` field for `databricks.sdk.service.pipelines.IngestionGatewayPipelineDefinition`.
* Add `ingest_from_uc_foreign_catalog` field for `databricks.sdk.service.pipelines.IngestionPipelineDefinition`.
* Add `type_text` field for `databricks.sdk.service.vectorsearch.ColumnInfo`.
* Add `foreign_catalog` enum value for `databricks.sdk.service.pipelines.IngestionSourceType`.
* Add `creating` and `create_failed` enum values for `databricks.sdk.service.settings.CustomerFacingNetworkConnectivityConfigAwsPrivateEndpointRulePrivateLinkConnectionState`.
* Add `creating` and `create_failed` enum values for `databricks.sdk.service.settings.NccAzurePrivateEndpointRuleConnectionState`.
* Change `destinations` field for `databricks.sdk.service.catalog.AccessRequestDestinations` to no longer be required.
* [Breaking] Change `destinations` field for `databricks.sdk.service.catalog.AccessRequestDestinations` to no longer be required.
* [Breaking] Change `online_store_config` field for `databricks.sdk.service.ml.MaterializedFeature` to type `databricks.sdk.service.ml.OnlineStoreConfig` dataclass.
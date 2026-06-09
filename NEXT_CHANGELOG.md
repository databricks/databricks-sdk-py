# NEXT CHANGELOG

## Release v0.116.0

### New Features and Improvements

### Security

### Bug Fixes

* Fall back to the remote runtime implementation when the legacy user namespace cannot be materialized. On Spark Connect runtimes (e.g. shared-access-mode clusters), importing `databricks.sdk.runtime` — which happens when constructing a `WorkspaceClient` on such a cluster — tried to build a legacy `SparkContext` and raised `CONTEXT_UNAVAILABLE_FOR_REMOTE_CLIENT` at import time. It now logs a warning and falls back to the Spark Connect-compatible remote implementation instead of crashing.

### Documentation

### Breaking Changes

### Internal Changes

### API Changes
* Add `databricks.sdk.service.aisearch` and `databricks.sdk.service.bundledeployments` packages.
* Add [w.ai_search](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/aisearch/ai_search.html) workspace-level service.
* Add [w.bundle_deployments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/bundledeployments/bundle_deployments.html) workspace-level service.
* Add `running_instances` field for `databricks.sdk.service.apps.ApplicationStatus`.
* Add `custom_max_retention_hours` field for `databricks.sdk.service.catalog.CatalogInfo`.
* Add `environment_settings` field for `databricks.sdk.service.catalog.ConnectionInfo`.
* Add `custom_max_retention_hours` field for `databricks.sdk.service.catalog.CreateCatalog`.
* Add `environment_settings` field for `databricks.sdk.service.catalog.CreateConnection`.
* Add `custom_max_retention_hours` field for `databricks.sdk.service.catalog.CreateSchema`.
* Add `custom_max_retention_hours` field for `databricks.sdk.service.catalog.SchemaInfo`.
* Add `custom_max_retention_hours` field for `databricks.sdk.service.catalog.UpdateCatalog`.
* Add `environment_settings` field for `databricks.sdk.service.catalog.UpdateConnection`.
* Add `custom_max_retention_hours` field for `databricks.sdk.service.catalog.UpdateSchema`.
* Add `stream_source` field for `databricks.sdk.service.ml.DataSource`.
* Add `ingestion_config` field for `databricks.sdk.service.ml.KafkaConfig`.
* Add `clustering_columns`, `enable_auto_clustering` and `table_properties` fields for `databricks.sdk.service.pipelines.TableSpecificConfig`.
* Add `branch_id` field for `databricks.sdk.service.postgres.Branch`.
* Add `catalog_id` field for `databricks.sdk.service.postgres.Catalog`.
* Add `database_id` field for `databricks.sdk.service.postgres.Database`.
* Add `endpoint_id` field for `databricks.sdk.service.postgres.Endpoint`.
* Add `project_id` field for `databricks.sdk.service.postgres.Project`.
* Add `role_id` field for `databricks.sdk.service.postgres.Role`.
* Add `synced_table_id` field for `databricks.sdk.service.postgres.SyncedTable`.
* Add `allowed_databricks_destinations` field for `databricks.sdk.service.settings.EgressNetworkPolicyNetworkAccessPolicy`.
* Add `facets`, `query_columns` and `sort_columns` fields for `databricks.sdk.service.vectorsearch.QueryVectorIndexRequest`.
* Add `facet_result` field for `databricks.sdk.service.vectorsearch.QueryVectorIndexResponse`.
* Add `facet_column_count` and `facet_columns` fields for `databricks.sdk.service.vectorsearch.ResultManifest`.
* Add `dangerously_force_discard_all` field for `databricks.sdk.service.workspace.UpdateRepoRequest`.
* [Breaking] Remove `databricks.sdk.service.bundle` package.
* [Breaking] Remove [w.bundle](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/bundle/bundle.html) workspace-level service.
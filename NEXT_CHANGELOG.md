# NEXT CHANGELOG

## Release v0.113.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Breaking Changes

### Internal Changes

* Switch workspace addressing header on workspace-scoped API calls from `X-Databricks-Org-Id` to `X-Databricks-Workspace-Id`. The value continues to come from `Config.workspace_id` (`DATABRICKS_WORKSPACE_ID`), and now accepts either a classic numeric workspace ID or another workspace identifier format (server disambiguates).

### API Changes
* Add `create_stream()`, `delete_stream()`, `get_stream()`, `list_streams()` and `update_stream()` methods for [w.feature_engineering](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/feature_engineering.html) workspace-level service.
* Add `update_token_management()` method for [w.token_management](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/token_management.html) workspace-level service.
* Add `deployment_id` and `version_id` fields for `databricks.sdk.service.jobs.JobDeployment`.
* Add `parameters` field for `databricks.sdk.service.jobs.PipelineTask`.
* Add `pipeline_task` field for `databricks.sdk.service.jobs.ResolvedValues`.
* Add `parameters` field for `databricks.sdk.service.pipelines.CreatePipeline`.
* Add `parameters` field for `databricks.sdk.service.pipelines.EditPipeline`.
* Add `parameters` field for `databricks.sdk.service.pipelines.GetPipelineResponse`.
* Add `deployment_id` and `version_id` fields for `databricks.sdk.service.pipelines.PipelineDeployment`.
* Add `autoscope_enabled` field for `databricks.sdk.service.settings.CreateOboTokenRequest`.
* Add `autoscope_enabled` field for `databricks.sdk.service.settings.CreateTokenRequest`.
* Add `autoscope_state`, `backfill_scopes`, `inferred_scopes` and `scopes` fields for `databricks.sdk.service.settings.PublicTokenInfo`.
* Add `autoscope_state`, `backfill_scopes`, `inferred_scopes` and `scopes` fields for `databricks.sdk.service.settings.TokenInfo`.
* [Breaking] Remove `catalog_id` field for `databricks.sdk.service.postgres.CatalogCatalogStatus`.
* [Breaking] Remove `synced_table_id` field for `databricks.sdk.service.postgres.SyncedTableSyncedTableStatus`.
* Add `resource_type` field for `databricks.sdk.service.bundle.Operation`.

# NEXT CHANGELOG

## Release v0.113.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Breaking Changes

### Internal Changes

### API Changes
* Add `create_stream()`, `delete_stream()`, `get_stream()`, `list_streams()` and `update_stream()` methods for [w.feature_engineering](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/feature_engineering.html) workspace-level service.
* Add `parameters` field for `databricks.sdk.service.jobs.PipelineTask`.
* Add `pipeline_task` field for `databricks.sdk.service.jobs.ResolvedValues`.
* Add `parameters` field for `databricks.sdk.service.pipelines.CreatePipeline`.
* Add `parameters` field for `databricks.sdk.service.pipelines.EditPipeline`.
* Add `parameters` field for `databricks.sdk.service.pipelines.GetPipelineResponse`.
* [Breaking] Remove `catalog_id` field for `databricks.sdk.service.postgres.CatalogCatalogStatus`.
* [Breaking] Remove `synced_table_id` field for `databricks.sdk.service.postgres.SyncedTableSyncedTableStatus`.
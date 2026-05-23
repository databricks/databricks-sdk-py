# NEXT CHANGELOG

## Release v0.111.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Breaking Changes

### Internal Changes

### API Changes
* Add `databricks.sdk.service.bundle` package.
* Add [w.bundle](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/bundle/bundle.html) workspace-level service.
* Add `revert()` method for [w.lakeview](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/lakeview.html) workspace-level service.
* Add `undelete_branch()` method for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service.
* Add `parent_path` field for `databricks.sdk.service.dashboards.GenieUpdateSpaceRequest`.
* Add `attributes` and `excluded_attributes` fields for `databricks.sdk.service.iam.MeRequest`.
* Add `include_trigger_state` field for `databricks.sdk.service.jobs.GetJobRequest`.
* Add `mtls_config` field for `databricks.sdk.service.ml.AuthConfig`.
* Add `delete_time` and `purge_time` fields for `databricks.sdk.service.postgres.BranchStatus`.
* Add `purge` field for `databricks.sdk.service.postgres.DeleteBranchRequest`.
* Add `show_deleted` field for `databricks.sdk.service.postgres.ListBranchesRequest`.
* Add `deleted` enum value for `databricks.sdk.service.postgres.BranchStatusState`.
* [Breaking] Change `tags` field for `databricks.sdk.service.marketplace.ListListingsRequest` to type `databricks.sdk.service.marketplace.ListingTag` dataclass.
* [Breaking] Change pagination for [ClustersAPI.events](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/compute/clusters.html#databricks.sdk.service.compute.ClustersAPI.events) method.
* Add `cron_schedule_trigger`, `streaming_mode` and `table_trigger` fields for `databricks.sdk.service.ml.MaterializedFeature`.
* Add `synced_table_id` field for `databricks.sdk.service.postgres.SyncedTableSyncedTableStatus`.
# NEXT CHANGELOG

## Release v0.113.0

### New Features and Improvements

### Security

### Bug Fixes

* Fixed recursive file lising in `WorkspaceClient.dbfs.list` on volumes. ([#1260](https://github.com/databricks/databricks-sdk-py/pull/1260))

### Documentation

### Breaking Changes

### Internal Changes

* Switch workspace addressing header on workspace-scoped API calls from `X-Databricks-Org-Id` to `X-Databricks-Workspace-Id`. The value continues to come from `Config.workspace_id` (`DATABRICKS_WORKSPACE_ID`), and now accepts either a classic numeric workspace ID or another workspace identifier format (server disambiguates).

### API Changes

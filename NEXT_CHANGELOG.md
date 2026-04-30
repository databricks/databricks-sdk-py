# NEXT CHANGELOG

## Release v0.106.0

### New Features and Improvements

### Security

### Bug Fixes
* Fixed Databricks CLI `--profile` fallback by detecting the CLI version at init time. The previous error-based detection was broken because `--profile` is a global Cobra flag silently accepted by old CLIs.

### Documentation

### Breaking Changes

### Internal Changes
* Detect Databricks CLI version at init time via `databricks version`, enabling version-gated flag support without additional subprocess calls.
* Validate Databricks CLI configuration at `DatabricksCliTokenSource.__init__` time. Misconfiguration (missing profile and host, or `--profile`-unsupported CLI without a host fallback) now surfaces as `IOError` synchronously from construction rather than lazily from the first `refresh()` call. The exception type matches the previous `refresh()`-time behaviour, so callers who already catch `IOError` are unaffected.

### API Changes
* Add [w.temporary_volume_credentials](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/temporary_volume_credentials.html) workspace-level service.
* Add `get_permission_levels()`, `get_permissions()`, `set_permissions()` and `update_permissions()` methods for [w.knowledge_assistants](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/knowledgeassistants/knowledge_assistants.html) workspace-level service.
* Add `undelete_project()` method for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service.
* Add `thumbnail_url` field for `databricks.sdk.service.apps.App`.
* Add `confidential_compute_type` field for `databricks.sdk.service.compute.GcpAttributes`.
* Add `jira_options`, `outlook_options` and `smartsheet_options` fields for `databricks.sdk.service.pipelines.ConnectorOptions`.
* Add `google_ads_config` field for `databricks.sdk.service.pipelines.SourceConfig`.
* Add `replace_existing` field for `databricks.sdk.service.postgres.CreateBranchRequest`.
* Add `replace_existing` field for `databricks.sdk.service.postgres.CreateEndpointRequest`.
* Add `purge` field for `databricks.sdk.service.postgres.DeleteProjectRequest`.
* Add `show_deleted` field for `databricks.sdk.service.postgres.ListProjectsRequest`.
* Add `delete_time` and `purge_time` fields for `databricks.sdk.service.postgres.Project`.
* Add `uc_connection` field for `databricks.sdk.service.supervisoragents.Tool`.
* Change `name` field for `databricks.sdk.service.supervisoragents.Connection` to no longer be required.
* [Breaking] Change `name` field for `databricks.sdk.service.supervisoragents.Connection` to no longer be required.
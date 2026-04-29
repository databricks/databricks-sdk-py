# NEXT CHANGELOG

## Release v0.106.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Breaking Changes

### Internal Changes

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
* Add `databricks.sdk.service.disasterrecovery` package.
* Add [a.disaster_recovery](https://databricks-sdk-py.readthedocs.io/en/latest/account/disasterrecovery/disaster_recovery.html) account-level service.
* Add `create_example()`, `delete_example()`, `get_example()`, `list_examples()` and `update_example()` methods for [w.knowledge_assistants](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/knowledgeassistants/knowledge_assistants.html) workspace-level service.
* Add `delta_table_name` field for `databricks.sdk.service.ml.BackfillSource`.
* Add `confluence_options` field for `databricks.sdk.service.pipelines.ConnectorOptions`.
* Add `confluence` enum value for `databricks.sdk.service.catalog.ConnectionType`.
* Add `confluence` enum value for `databricks.sdk.service.pipelines.IngestionSourceType`.
* Change `description` field for `databricks.sdk.service.supervisoragents.SupervisorAgent` to no longer be required.
* [Breaking] Change `description` field for `databricks.sdk.service.supervisoragents.SupervisorAgent` to no longer be required.
* [Breaking] Remove `connection` field for `databricks.sdk.service.supervisoragents.Tool`.
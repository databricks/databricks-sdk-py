# NEXT CHANGELOG

## Release v0.105.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Breaking Changes

### Internal Changes

### API Changes
* Add `databricks.sdk.service.supervisoragents` package.
* Add [w.secrets_uc](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/secrets_uc.html) workspace-level service.
* Add [w.supervisor_agents](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/supervisoragents/supervisor_agents.html) workspace-level service.
* Add `update()` method for [w.tokens](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/tokens.html) workspace-level service.
* Add `etag` field for `databricks.sdk.service.dashboards.GenieSpace`.
* Add `etag` field for `databricks.sdk.service.dashboards.GenieUpdateSpaceRequest`.
* Add `branch_id` field for `databricks.sdk.service.postgres.BranchStatus`.
* Add `catalog_id` field for `databricks.sdk.service.postgres.CatalogCatalogStatus`.
* Add `database_id` field for `databricks.sdk.service.postgres.DatabaseDatabaseStatus`.
* Add `endpoint_id` field for `databricks.sdk.service.postgres.EndpointStatus`.
* Add `project_id` field for `databricks.sdk.service.postgres.ProjectStatus`.
* Add `role_id` field for `databricks.sdk.service.postgres.RoleRoleStatus`.
* Add `project` field for `databricks.sdk.service.postgres.SyncedTableSyncedTableStatus`.
* Add `manual` field for `databricks.sdk.service.provisioning.CreateGcpKeyInfo`.
* Add `manual` field for `databricks.sdk.service.provisioning.GcpKeyInfo`.
* Add `apps_runtime` and `lakebase_runtime` fields for `databricks.sdk.service.settings.CustomerFacingIngressNetworkPolicyRequestDestination`.
* Add `blocked_internet_destinations` field for `databricks.sdk.service.settings.EgressNetworkPolicyNetworkAccessPolicy`.
* Add `columns_to_sync` field for `databricks.sdk.service.vectorsearch.DeltaSyncVectorIndexSpecResponse`.
* Add `breaking_change` enum value for `databricks.sdk.service.jobs.TerminationCodeCode`.
* [Breaking] Change `update_catalog_config()` method for [w.data_classification](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dataclassification/data_classification.html) workspace-level service. Method path has changed.
* [Breaking] Change `update_default_workspace_base_environment()` method for [w.environments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/environments/environments.html) workspace-level service. Method path has changed.
* [Breaking] Change `update_knowledge_assistant()` method for [w.knowledge_assistants](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/knowledgeassistants/knowledge_assistants.html) workspace-level service. Method path has changed.
* [Breaking] Change `update_branch()`, `update_database()`, `update_endpoint()`, `update_project()` and `update_role()` methods for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service. Method path has changed.
* [Breaking] Change `update_default_warehouse_override()` method for [w.warehouses](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sql/warehouses.html) workspace-level service. Method path has changed.

# NEXT CHANGELOG

## Release v0.103.0

### New Features and Improvements
* Accept `DATABRICKS_OIDC_TOKEN_FILEPATH` environment variable for consistency with other Databricks SDKs (Go, CLI, Terraform). The previous `DATABRICKS_OIDC_TOKEN_FILE` is still supported as an alias.

### Security

### Bug Fixes
* Fixes TypeError in _unknown_error() when API returns unparseable error on streaming request (#1264) 

### Documentation

### Internal Changes
* Replace the async-disabling mechanism on token refresh failure with a 1-minute retry backoff. Previously, a single failed async refresh would disable proactive token renewal until the token expired. Now, the SDK waits a short cooldown period and retries, improving resilience to transient errors.
* Extract `_resolve_profile` to simplify config file loading and improve `__settings__` error messages.

### API Changes
* Add `create_catalog()`, `create_synced_table()`, `delete_catalog()`, `delete_synced_table()`, `get_catalog()` and `get_synced_table()` methods for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service.
* Add `effective_file_event_queue` field for `databricks.sdk.service.catalog.CreateExternalLocation`.
* Add `effective_file_event_queue` field for `databricks.sdk.service.catalog.ExternalLocationInfo`.
* Add `effective_file_event_queue` field for `databricks.sdk.service.catalog.UpdateExternalLocation`.
* Add `column_selection` field for `databricks.sdk.service.ml.Function`.
* Add `cascade` field for `databricks.sdk.service.pipelines.DeletePipelineRequest`.
* Add `default_branch` field for `databricks.sdk.service.postgres.ProjectSpec`.
* Add `default_branch` field for `databricks.sdk.service.postgres.ProjectStatus`.
* Add `ingress` and `ingress_dry_run` fields for `databricks.sdk.service.settings.AccountNetworkPolicy`.
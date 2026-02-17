# NEXT CHANGELOG

## Release v0.90.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `databricks.sdk.service.networking` package.
* Add [a.endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/account/networking/endpoints.html) account-level service.
* Add `create_space()`, `delete_space()`, `get_space()`, `get_space_operation()`, `list_spaces()` and `update_space()` methods for [w.apps](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/apps/apps.html) workspace-level service.
* Add `space` field for `databricks.sdk.service.apps.App`.
* Add `space` field for `databricks.sdk.service.apps.ListAppsRequest`.
* Add `source_type`, `update_time` and `updated_by` fields for `databricks.sdk.service.catalog.EntityTagAssignment`.
* Add `skip_notify` field for `databricks.sdk.service.dashboards.Subscription`.
* Add `sparse_checkout` field for `databricks.sdk.service.jobs.GitSource`.
* Add `disable_auto_optimization`, `max_retries`, `min_retry_interval_millis` and `retry_on_timeout` fields for `databricks.sdk.service.jobs.RunTask`.
* Add `disable_auto_optimization`, `max_retries`, `min_retry_interval_millis` and `retry_on_timeout` fields for `databricks.sdk.service.jobs.SubmitTask`.
* Add `budget_policy_id` and `custom_tags` fields for `databricks.sdk.service.postgres.ProjectSpec`.
* Add `budget_policy_id` and `custom_tags` fields for `databricks.sdk.service.postgres.ProjectStatus`.
* Add `edgegrid_akamai` enum value for `databricks.sdk.service.catalog.CredentialType`.

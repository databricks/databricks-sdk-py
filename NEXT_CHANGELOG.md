# NEXT CHANGELOG

## Release v0.86.0

### New Features and Improvements
* Added `custom_headers` parameter to `WorkspaceClient` and `AccountClient` to support custom HTTP headers in all API requests ([#1245](https://github.com/databricks/databricks-sdk-py/pull/1245)).

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `id` field for `databricks.sdk.service.sharing.CreateRecipient`.
* Add `id` field for `databricks.sdk.service.sharing.RecipientInfo`.
* Add `id` field for `databricks.sdk.service.sharing.UpdateRecipient`.
* Add `query_tags` field for `databricks.sdk.service.sql.ExecuteStatementRequest`.
* Add `query_tags` field for `databricks.sdk.service.sql.QueryInfo`.
* Add `uc_volume_misconfigured` enum value for `databricks.sdk.service.compute.EventType`.
* Add `filters` field for `databricks.sdk.service.jobs.DashboardTask`.
* Add `ssws_token` enum value for `databricks.sdk.service.catalog.CredentialType`.
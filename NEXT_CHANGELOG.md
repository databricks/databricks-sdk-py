# NEXT CHANGELOG

## Release v0.75.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `databricks.sdk.service.postgres` package.
* Add [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service.
* Add `apply_environment()` method for [w.pipelines](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/pipelines/pipelines.html) workspace-level service.
* Add `effective_usage_policy_id` and `usage_policy_id` fields for `databricks.sdk.service.apps.App`.
* Add `external_access_enabled` field for `databricks.sdk.service.catalog.CreateAccountsMetastore`.
* Add `external_access_enabled` field for `databricks.sdk.service.catalog.CreateMetastore`.
* Add `external_access_enabled` field for `databricks.sdk.service.catalog.UpdateAccountsMetastore`.
* Add `external_access_enabled` field for `databricks.sdk.service.catalog.UpdateMetastore`.
* Add `usage_policy_id` field for `databricks.sdk.service.ml.OnlineStore`.
* Add `error_message` field for `databricks.sdk.service.settings.CustomerFacingNetworkConnectivityConfigAwsPrivateEndpointRule`.
* Add `error_message` field for `databricks.sdk.service.settings.NccAzurePrivateEndpointRule`.
* Add `control_plane_connection_failure` and `control_plane_connection_failure_due_to_misconfig` enum values for `databricks.sdk.service.compute.TerminationReasonCode`.
* Add `control_plane_connection_failure` and `control_plane_connection_failure_due_to_misconfig` enum values for `databricks.sdk.service.sql.TerminationReasonCode`.
# NEXT CHANGELOG

## Release v0.66.0

### New Features and Improvements

* Add a public helper function to build a `CredentialsProvider` directly from an `IdTokenSource`.

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added `databricks.sdk.service.iamv2` package.
* Added `feedback` field for `databricks.sdk.service.dashboards.GenieMessage`.
* Added `disabled` field for `databricks.sdk.service.jobs.Task`.
* Added `auxiliary_managed_location` field for `databricks.sdk.service.sharing.TableInternalAttributes`.
* Added `alerts` field for `databricks.sdk.service.sql.ListAlertsV2Response`.
* Added `no_activated_k8s` and `usage_policy_entitlement_denied` enum values for `databricks.sdk.service.compute.TerminationReasonCode`.
* Added `foreign_catalog` enum value for `databricks.sdk.service.pipelines.IngestionSourceType`.
* Added `foreign_iceberg_table` enum value for `databricks.sdk.service.sharing.TableInternalAttributesSharedTableType`.
* [Breaking] Removed `disabled` field for `databricks.sdk.service.jobs.RunTask`.

# NEXT CHANGELOG

## Release v0.78.0

### New Features and Improvements

* Increase async cache stale period from 3 to 5 minutes to cover the maximum monthly downtime of a 99.99% uptime SLA.

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `table_deltasharing_open_dir_based` enum value for `databricks.sdk.service.catalog.SecurableKind`.
* Add `creating` and `create_failed` enum values for `databricks.sdk.service.settings.NccPrivateEndpointRulePrivateLinkConnectionState`.
* [Breaking] Remove `access_modes` and `storage_location` fields for `databricks.sdk.service.sharing.Table`.
* Add `error_message` field for `databricks.sdk.service.settings.CreatePrivateEndpointRule`.
* Add `error_message` field for `databricks.sdk.service.settings.NccPrivateEndpointRule`.
* Add `error_message` field for `databricks.sdk.service.settings.UpdatePrivateEndpointRule`.
* Add `rate_limited` enum value for `databricks.sdk.service.compute.TerminationReasonCode`.
* Add `rate_limited` enum value for `databricks.sdk.service.sql.TerminationReasonCode`.
* [Breaking] Add long-running operation configuration for [PostgresAPI.delete_branch](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html#databricks.sdk.service.postgres.PostgresAPI.delete_branch) method.
* [Breaking] Add long-running operation configuration for [PostgresAPI.delete_endpoint](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html#databricks.sdk.service.postgres.PostgresAPI.delete_endpoint) method.
* [Breaking] Add long-running operation configuration for [PostgresAPI.delete_project](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html#databricks.sdk.service.postgres.PostgresAPI.delete_project) method.
* [Breaking] Change `delete_branch()`, `delete_endpoint()` and `delete_project()` methods for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service to return `databricks.sdk.service.postgres.Operation` dataclass.
* [Breaking] Remove `pgbouncer_settings` field for `databricks.sdk.service.postgres.EndpointSettings`.
* [Breaking] Remove `pooler_mode` field for `databricks.sdk.service.postgres.EndpointSpec`.
* [Breaking] Remove `pooler_mode` field for `databricks.sdk.service.postgres.EndpointStatus`.
* [Breaking] Remove `pgbouncer_settings` field for `databricks.sdk.service.postgres.ProjectDefaultEndpointSettings`.
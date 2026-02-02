# NEXT CHANGELOG

## Release v0.83.0

### New Features and Improvements
* Add support for single Profile for Account and Workspace operations in Unified Mode.

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `generate_download_full_query_result()` and `get_download_full_query_result()` methods for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service.
* Add `active_instances` field for `databricks.sdk.service.apps.ComputeStatus`.
* [Breaking] Change `create_role()` method for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service. HTTP method/verb has changed.
* Add `compute` field for `databricks.sdk.service.jobs.RunTask`.
* Add `compute` field for `databricks.sdk.service.jobs.SubmitTask`.
* Add `compute` field for `databricks.sdk.service.jobs.Task`.
* Add `mtls_port_connectivity_failure` enum value for `databricks.sdk.service.compute.TerminationReasonCode`.
* Add `mtls_port_connectivity_failure` enum value for `databricks.sdk.service.sql.TerminationReasonCode`.
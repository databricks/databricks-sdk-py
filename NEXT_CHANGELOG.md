# NEXT CHANGELOG

## Release v0.83.0

### New Features and Improvements
* Add support for single Profile for Account and Workspace operations in Unified Mode.

* FilesExt retry logic now respects a retry count limit in addition to the time-based timeout. Operations will stop retrying when either the retry count (`experimental_files_ext_cloud_api_max_retries`, default: 3) or timeout (`retry_timeout_seconds`) is exceeded, whichever comes first. This provides faster feedback when APIs are consistently unavailable.

### Security

### Bug Fixes

* FilesExt no longer retries on 500 (Internal Server Error) responses. These errors now fail immediately or fallback to alternative upload methods as appropriate.

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
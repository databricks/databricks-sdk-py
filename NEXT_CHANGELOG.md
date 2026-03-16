# NEXT CHANGELOG

## Release v0.100.0

### New Features and Improvements
* Support `default_profile` in `[__settings__]` section of `.databrickscfg` for consistent default profile resolution across CLI and SDKs.

### Security

### Bug Fixes

* Always create a new logger instance, rather than using Python's default global logger instance ([#988](https://github.com/databricks/databricks-sdk-py/pull/988)).

### Documentation

### Internal Changes

### API Changes
* Add `alert_output` field for `databricks.sdk.service.jobs.RunOutput`.
* Add `alert_task` field for `databricks.sdk.service.jobs.RunTask`.
* Add `alert_task` field for `databricks.sdk.service.jobs.SubmitTask`.
* Add `alert_task` field for `databricks.sdk.service.jobs.Task`.
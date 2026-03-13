# NEXT CHANGELOG

## Release v0.100.0

### New Features and Improvements
* Support `default_profile` in `[__settings__]` section of `.databrickscfg` for consistent default profile resolution across CLI and SDKs.

### Security

### Bug Fixes

### Documentation

### Internal Changes
* Replace the async-disabling mechanism on token refresh failure with a 1-minute retry backoff. Previously, a single failed async refresh would disable proactive token renewal until the token expired. Now, the SDK waits a short cooldown period and retries, improving resilience to transient errors.

### API Changes
* Add `alert_output` field for `databricks.sdk.service.jobs.RunOutput`.
* Add `alert_task` field for `databricks.sdk.service.jobs.RunTask`.
* Add `alert_task` field for `databricks.sdk.service.jobs.SubmitTask`.
* Add `alert_task` field for `databricks.sdk.service.jobs.Task`.
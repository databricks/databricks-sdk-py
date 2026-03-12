# NEXT CHANGELOG

## Release v0.100.0

### New Features and Improvements

* Added automatic detection of AI coding agents (Claude Code, Cursor, Cline, Codex, Gemini CLI, OpenCode, Antigravity) in the user-agent string. The SDK now appends `agent/<name>` to HTTP request headers when running inside a known AI agent environment.

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `alert_output` field for `databricks.sdk.service.jobs.RunOutput`.
* Add `alert_task` field for `databricks.sdk.service.jobs.RunTask`.
* Add `alert_task` field for `databricks.sdk.service.jobs.SubmitTask`.
* Add `alert_task` field for `databricks.sdk.service.jobs.Task`.
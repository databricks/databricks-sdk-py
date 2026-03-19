# NEXT CHANGELOG

## Release v0.102.0

### New Features and Improvements

* Added automatic detection of AI coding agents (Antigravity, Claude Code, Cline, Codex, Copilot CLI, Cursor, Gemini CLI, OpenCode) in the user-agent string. The SDK now appends `agent/<name>` to HTTP request headers when running inside a known AI agent environment.

### Security

### Bug Fixes

* Added `timeout` to `requests.post()`/`requests.get()` calls in `oauth.py` that previously had no timeout, which could cause indefinite hangs when the OAuth endpoint is unreachable during token refresh ([#1338](https://github.com/databricks/databricks-sdk-py/issues/1338)).

### Documentation

### Internal Changes

### API Changes
* Add `disable_gov_tag_creation` field for `databricks.sdk.service.settings.RestrictWorkspaceAdminsMessage`.
* Add `disable_gov_tag_creation` field for `databricks.sdk.service.settingsv2.RestrictWorkspaceAdminsMessage`.
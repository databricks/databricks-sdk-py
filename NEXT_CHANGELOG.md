# NEXT CHANGELOG

## Release v0.102.0

### New Features and Improvements

* Added automatic detection of AI coding agents (Claude Code, Cursor, Cline, Codex, Gemini CLI, OpenCode, Antigravity) in the user-agent string. The SDK now appends `agent/<name>` to HTTP request headers when running inside a known AI agent environment.

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `disable_gov_tag_creation` field for `databricks.sdk.service.settings.RestrictWorkspaceAdminsMessage`.
* Add `disable_gov_tag_creation` field for `databricks.sdk.service.settingsv2.RestrictWorkspaceAdminsMessage`.
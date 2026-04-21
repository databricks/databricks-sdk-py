# NEXT CHANGELOG

## Release v0.104.0

### New Features and Improvements

### Security

### Bug Fixes

* Add `X-Databricks-Org-Id` header to `WorkspaceExt.upload()` and `WorkspaceExt.download()` for SPOG host compatibility.
* `WorkspaceClient.get_workspace_id()` now returns `Config.workspace_id` directly when set, instead of calling `/api/2.0/preview/scim/v2/Me`. This removes an API round-trip on every call where the workspace ID is already known (profile, `?o=` query param, env var, or host metadata) and fixes a failure on SPOG hosts where the unauthenticated probe request was rejected with `Unable to load OAuth Config`.
* Add `X-Databricks-Org-Id` header to `SharesExt.list()` for SPOG host compatibility.

### Documentation

### Breaking Changes

### Internal Changes

* Expanded AI agent detection: added Goose, Amp, Augment, Copilot (VS Code), Kiro, Windsurf. Honors the `AGENT=<name>` standard (resolves to a known product if the value matches one, otherwise `unknown`). Presence-only env var matchers now treat an empty string as "set" for parity with the Go and Java SDKs. Explicit agent env vars (e.g. `CLAUDECODE`, `GOOSE_TERMINAL`) always take precedence over the generic `AGENT=<name>` signal. When multiple agent env vars are present (e.g. a Cursor CLI subagent invoked from Claude Code), the user-agent reports `agent/multiple`.

### API Changes

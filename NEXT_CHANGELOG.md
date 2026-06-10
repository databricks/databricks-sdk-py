# NEXT CHANGELOG

## Release v0.117.0

### New Features and Improvements

* Add `databricks.apps` module with `get_workspace_client()` and `get_user_workspace_client()` helpers for code running inside Databricks Apps. Both pin `auth_type` explicitly so the SDK's auth validator does not raise `more than one authorization method configured` when both the app's SP env vars and a user OBO token are available in the same process. `get_user_workspace_client()` reads the user token from `X-Forwarded-Access-Token` without mutating process env vars, making it safe for concurrent request handlers. A `get_mcp_client()` placeholder is exposed; the real implementation will land alongside the mcp_server resource type (tracked separately).

### Security

### Bug Fixes

* Cache tokens minted by `DatabricksOidcTokenSource` (Workload Identity Federation / account-wide token federation). Previously a fresh `/oidc/v1/token` exchange was performed on every authenticated API call, adding latency, amplifying transient federation-policy errors, and hitting OIDC token-endpoint rate limits. The token source now reuses the cached token until it is stale or expired, fetching a fresh ID token on each refresh to support rotation.

### Documentation

### Breaking Changes

### Internal Changes

### API Changes

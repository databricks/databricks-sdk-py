# NEXT CHANGELOG

## Release v0.117.0

### New Features and Improvements

### Security

### Bug Fixes

* Fall back to the remote runtime implementation when the legacy user namespace cannot be materialized. On Spark Connect runtimes (e.g. shared-access-mode clusters), importing `databricks.sdk.runtime` — which happens when constructing a `WorkspaceClient` on such a cluster — tried to build a legacy `SparkContext` and raised `CONTEXT_UNAVAILABLE_FOR_REMOTE_CLIENT` at import time. It now logs a warning and falls back to the Spark Connect-compatible remote implementation instead of crashing.
* Cache tokens minted by `DatabricksOidcTokenSource` (Workload Identity Federation / account-wide token federation). Previously a fresh `/oidc/v1/token` exchange was performed on every authenticated API call, adding latency, amplifying transient federation-policy errors, and hitting OIDC token-endpoint rate limits. The token source now reuses the cached token until it is stale or expired, fetching a fresh ID token on each refresh to support rotation.

### Documentation

### Breaking Changes

### Internal Changes

### API Changes

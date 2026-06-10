# NEXT CHANGELOG

## Release v0.117.0

### New Features and Improvements

* Add `include_shared_data` param to `databricks.sdk.service.sharing.SharesAPI.list_shares` so that it's possible to fetch shared_data when listing all shares.

### Security

### Bug Fixes

* Cache tokens minted by `DatabricksOidcTokenSource` (Workload Identity Federation / account-wide token federation). Previously a fresh `/oidc/v1/token` exchange was performed on every authenticated API call, adding latency, amplifying transient federation-policy errors, and hitting OIDC token-endpoint rate limits. The token source now reuses the cached token until it is stale or expired, fetching a fresh ID token on each refresh to support rotation.

### Documentation

### Breaking Changes

### Internal Changes

### API Changes

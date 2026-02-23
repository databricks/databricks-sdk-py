# NEXT CHANGELOG

## Release v0.94.0

### New Features and Improvements
* Added `Config.discovery_url` config field (`DATABRICKS_DISCOVERY_URL` env var) and `Config._resolve_host_metadata()` to auto-populate `account_id`, `workspace_id`, and the OIDC discovery URL from `/.well-known/databricks-config`. Mirrors `discoveryUrl` in the Java SDK.

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes

# NEXT CHANGELOG

## Release v0.97.0

### New Features and Improvements

### Security

### Bug Fixes
* Fixed Databricks CLI authentication to detect when the cached token's scopes don't match the SDK's configured scopes. Previously, a scope mismatch was silently ignored, causing requests to use wrong permissions. The SDK now raises an error with instructions to re-authenticate.


### Documentation

### Internal Changes

### API Changes

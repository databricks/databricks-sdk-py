# NEXT CHANGELOG

## Release v0.62.0

### New Features and Improvements

### Bug Fixes

* Fix `Config.oauth_token()` to avoid re-creating a new `CredentialsProvider` at each call. This fix indirectly makes `oauth_token()` benefit from the internal caching mechanism of some providers. 

### Documentation

### Internal Changes

### API Changes

# NEXT CHANGELOG

## Release v0.68.0

### New Features and Improvements

* Add native support for authentication through Azure DevOps OIDC.

### Bug Fixes
* Fix a security issue that resulted in bearer tokens being logged in exception messages.

* Always create a new logger instance, rather than using Python's default global logger instance ([#988](https://github.com/databricks/databricks-sdk-py/pull/988)).

### Documentation

### Internal Changes

### API Changes

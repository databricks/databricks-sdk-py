# NEXT CHANGELOG

## Release v0.51.0

### New Features and Improvements
* Enabled asynchronous token refreshes by default. A new `disable_async_token_refresh` configuration option has been added to allow disabling this feature if necessary ([#952](https://github.com/databricks/databricks-sdk-py/pull/952)).
  To disable asynchronous token refresh, set the environment variable `DATABRICKS_DISABLE_ASYNC_TOKEN_REFRESH=true` or configure it within your configuration object.
  The previous `enable_experimental_async_token_refresh` option has been removed as asynchronous refresh is now the default behavior.

### Bug Fixes

### Documentation

### Internal Changes

### API Changes

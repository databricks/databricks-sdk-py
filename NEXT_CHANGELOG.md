# NEXT CHANGELOG

## Release v0.51.0

### New Features and Improvements
* Made async token refresh the default behavior. Added `disable_async_token_refresh` configuration option to disable it if needed ([#952](https://github.com/databricks/databricks-sdk-py/pull/952)).
  To disable async token refresh, set environment variable `DATABRICKS_DISABLE_ASYNC_TOKEN_REFRESH=true` or configure it in your config object.
  The previous `enable_experimental_async_token_refresh` option has been removed as async refresh is now the default.

### Bug Fixes

### Documentation

### Internal Changes

### API Changes

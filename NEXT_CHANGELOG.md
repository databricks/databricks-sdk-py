# NEXT CHANGELOG

## Release v0.45.0

### New Features and Improvements
* Update Jobs service to use API 2.2 ([#913](https://github.com/databricks/databricks-sdk-py/pull/913)).
* [Experimental] Add support for async token refresh ([#916](https://github.com/databricks/databricks-sdk-py/pull/916)).
  This can be enabled with by setting the following setting:
  ```
  export DATABRICKS_ENABLE_EXPERIMENTAL_ASYNC_TOKEN_REFRESH=1.
  ```
  This feature and its setting are experimental and may be removed in future releases.

### Bug Fixes

### Documentation

### Internal Changes

* Refactor `DatabricksError` to expose different types of error details ([#912](https://github.com/databricks/databricks-sdk-py/pull/912)). 
* Update Jobs ListJobs API to support paginated responses ([#896](https://github.com/databricks/databricks-sdk-py/pull/896))
* Update Jobs ListRuns API to support paginated responses ([#890](https://github.com/databricks/databricks-sdk-py/pull/890))
* Introduce automated tagging ([#888](https://github.com/databricks/databricks-sdk-py/pull/888))
* Update Jobs GetJob API to support paginated responses ([#869](https://github.com/databricks/databricks-sdk-py/pull/869)).
* Update On Behalf Of User Authentication in Multithreaded applications ([#907](https://github.com/databricks/databricks-sdk-py/pull/907))

### API Changes

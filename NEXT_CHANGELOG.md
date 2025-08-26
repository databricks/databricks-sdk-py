# NEXT CHANGELOG

## Release v0.65.0

### New Features and Improvements

* Added support for passing additional kwargs to `WorkspaceClient().serving_endpoints.get_open_ai_client()` ([#1025](https://github.com/databricks/databricks-sdk-py/pull/1025)). Users can now pass standard OpenAI client parameters like `timeout` and `max_retries` when creating an OpenAI client for Databricks Model Serving.
* Enable remove DBUtils in Shared Clusters ([#1033](https://github.com/databricks/databricks-sdk-py/pull/1033)).

### Bug Fixes

### Documentation

### Internal Changes

### API Changes

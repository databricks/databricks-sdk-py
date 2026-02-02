# NEXT CHANGELOG

## Release v0.82.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes

 * Deprecated `WorkspaceClient.serving_endpoints.get_open_ai_client()` and `WorkspaceClient.serving_endpoints.get_langchain_chat_open_ai_client()` methods in favor of dedicated packages. Users should migrate to `databricks-openai` (using `DatabricksOpenAI`) and `databricks-langchain` (using `ChatDatabricks`) respectively ([#1238](https://github.com/databricks/databricks-sdk-py/pull/1238)).

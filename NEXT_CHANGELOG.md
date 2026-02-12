# NEXT CHANGELOG

## Release v0.88.0

### New Features and Improvements

* FilesExt retry logic now respects a retry count limit in addition to the time-based timeout. Operations will stop retrying when either the retry count (`experimental_files_ext_cloud_api_max_retries`, default: 3) or timeout (`retry_timeout_seconds`) is exceeded, whichever comes first. This provides faster feedback when APIs are consistently unavailable.

### Security

### Bug Fixes

* FilesExt no longer retries on 500 (Internal Server Error) responses. These errors now fail immediately or fallback to alternative upload methods as appropriate.

### Documentation

### Internal Changes

### API Changes
* Deprecated `WorkspaceClient.serving_endpoints.get_open_ai_client()` and `WorkspaceClient.serving_endpoints.get_langchain_chat_open_ai_client()` methods in favor of dedicated packages. Users should migrate to `databricks-openai` (using `DatabricksOpenAI`) and `databricks-langchain` (using `ChatDatabricks`) respectively ([#1238](https://github.com/databricks/databricks-sdk-py/pull/1238)).

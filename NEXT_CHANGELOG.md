# NEXT CHANGELOG

## Release v0.88.0

### New Features and Improvements
* Add `get_async_open_ai_client()` method to `ServingEndpointsAPI` for native `AsyncOpenAI` client support ([#847](https://github.com/databricks/databricks-sdk-py/issues/847)).

### Security

### Bug Fixes
* Fix `get_langchain_chat_open_ai_client()` returning 401 on async operations by adding `http_async_client` ([#1173](https://github.com/databricks/databricks-sdk-py/issues/1173)).

### Documentation

### Internal Changes

### API Changes

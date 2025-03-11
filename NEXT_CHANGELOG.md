# NEXT CHANGELOG

## Release v0.46.0

### New Features and Improvements
* [Experimental] Add support for async token refresh ([#916](https://github.com/databricks/databricks-sdk-py/pull/916)).
  This can be enabled with by setting the following setting:
  ```
  export DATABRICKS_ENABLE_EXPERIMENTAL_ASYNC_TOKEN_REFRESH=1.
  ```
  This feature and its setting are experimental and may be removed in future releases.

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added [w.forecasting](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/forecasting.html) workspace-level service.
* Added `statement_id` field for `databricks.sdk.service.dashboards.GenieQueryAttachment`.
* Added `could_not_get_model_deployments_exception` enum value for `databricks.sdk.service.dashboards.MessageErrorType`.
* [Breaking] Removed `jwks_uri` field for `databricks.sdk.service.oauth2.OidcFederationPolicy`.

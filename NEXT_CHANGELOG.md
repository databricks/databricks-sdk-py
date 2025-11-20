# NEXT CHANGELOG

## Release v0.74.0

### New Features and Improvements
* Add new auth type (`runtime-oauth`) for notebooks: Introduce a new authentication mechanism that allows notebooks to authenticate using OAuth tokens

### Security

### Bug Fixes

- Fixed an issue where download from Shared Volumes could fail by falling back to Files API whenever Presigned URLs are not available.

### Documentation

### Internal Changes

### API Changes
* Change `table_names` field for `databricks.sdk.service.jobs.TableUpdateTriggerConfiguration` to no longer be required.
* [Breaking] Change `table_names` field for `databricks.sdk.service.jobs.TableUpdateTriggerConfiguration` to no longer be required.
* [Breaking] Remove `batch_create_materialized_features()` method for [w.feature_engineering](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/feature_engineering.html) workspace-level service.
* [Breaking] Remove `lineage_context` field for `databricks.sdk.service.ml.Feature`.
* [Breaking] Remove `autoscale_v2` enum value for `databricks.sdk.service.compute.EventDetailsCause`.
* [Breaking] Remove `unsupported_conversation_type_exception` enum value for `databricks.sdk.service.dashboards.MessageErrorType`.
* [Breaking] Remove `red_state` and `yellow_state` enum values for `databricks.sdk.service.vectorsearch.EndpointStatusState`.
# NEXT CHANGELOG

## Release v0.72.0

### New Features and Improvements

### Bug Fixes
- Fix `FilesExt` can fail to upload and download data when Presigned URLs are not available in certain environments (e.g. Serverless GPU clusters).

- Fix `FilesExt.upload` and `FilesExt.upload_from` would fail when the source content is empty and `use_parallel=True`.

### Documentation

### Internal Changes

### API Changes
* Add `google_ads`, `tiktok_ads`, `salesforce_marketing_cloud`, `hubspot`, `workday_hcm`, `guidewire` and `zendesk` enum values for `databricks.sdk.service.pipelines.IngestionSourceType`.
* Add `batch_create_materialized_features()` method for [w.feature_engineering](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/feature_engineering.html) workspace-level service.
* Add `lineage_context` field for `databricks.sdk.service.ml.Feature`.
* Add `autoscale_v2` enum value for `databricks.sdk.service.compute.EventDetailsCause`.
* Add `unsupported_conversation_type_exception` enum value for `databricks.sdk.service.dashboards.MessageErrorType`.
* Add `red_state` and `yellow_state` enum values for `databricks.sdk.service.vectorsearch.EndpointStatusState`.
* [Breaking] Change `table_names` field for `databricks.sdk.service.jobs.TableUpdateTriggerConfiguration` to be required.
* Change `table_names` field for `databricks.sdk.service.jobs.TableUpdateTriggerConfiguration` to be required.
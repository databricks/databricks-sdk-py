# NEXT CHANGELOG

## Release v0.65.0

### New Features and Improvements

* Added support for passing additional kwargs to `WorkspaceClient().serving_endpoints.get_open_ai_client()` ([#1025](https://github.com/databricks/databricks-sdk-py/pull/1025)). Users can now pass standard OpenAI client parameters like `timeout` and `max_retries` when creating an OpenAI client for Databricks Model Serving.

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added `comment` field for `databricks.sdk.service.dashboards.GenieSendMessageFeedbackRequest`.
* [Breaking] Added `rating` field for `databricks.sdk.service.dashboards.GenieSendMessageFeedbackRequest`.
* Added `effective_enable_pg_native_login` and `enable_pg_native_login` fields for `databricks.sdk.service.database.DatabaseInstance`.
* Added `task_retry_mode` field for `databricks.sdk.service.jobs.Continuous`.
* Added `source_configurations` field for `databricks.sdk.service.pipelines.IngestionPipelineDefinition`.
* Added `app_id`, `app_id_set`, `auth_secret`, `auth_secret_set`, `channel_url`, `channel_url_set`, `tenant_id` and `tenant_id_set` fields for `databricks.sdk.service.settings.MicrosoftTeamsConfig`.
* Added `ensure_reranker_compatible` field for `databricks.sdk.service.vectorsearch.GetIndexRequest`.
* Added `reranker` field for `databricks.sdk.service.vectorsearch.QueryVectorIndexRequest`.
* [Breaking] Changed `create_clean_room_asset_review()` method for [w.clean_room_assets](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/cleanrooms/clean_room_assets.html) workspace-level service with new required argument order.
* [Breaking] Changed `send_message_feedback()` method for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service with new required argument order.
* Changed `notebook_review` field for `databricks.sdk.service.cleanrooms.CreateCleanRoomAssetReviewRequest` to no longer be required.
* [Breaking] Changed `features` field for `databricks.sdk.service.ml.FeatureList` to type list[`databricks.sdk.service.ml.LinkedFeature`] dataclass.
* [Breaking] Removed `feedback_rating` and `feedback_text` fields for `databricks.sdk.service.dashboards.GenieSendMessageFeedbackRequest`.

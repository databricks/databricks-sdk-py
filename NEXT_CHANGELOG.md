# NEXT CHANGELOG

## Release v0.109.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Breaking Changes

### Internal Changes

### API Changes
* Add `create_workspace_assignment_detail()`, `delete_workspace_assignment_detail()`, `get_workspace_assignment_detail()`, `list_workspace_assignment_details()` and `update_workspace_assignment_detail()` methods for [a.account_iam_v2](https://databricks-sdk-py.readthedocs.io/en/latest/account/iamv2/account_iam_v2.html) account-level service.
* Add `create_workspace_assignment_detail_proxy()`, `delete_workspace_assignment_detail_proxy()`, `get_workspace_assignment_detail_proxy()`, `list_workspace_assignment_details_proxy()` and `update_workspace_assignment_detail_proxy()` methods for [w.workspace_iam_v2](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/iamv2/workspace_iam_v2.html) workspace-level service.
* Add `failover_group_name` field for `databricks.sdk.service.disasterrecovery.StableUrl`.
* Add `catalog_name`, `created_at`, `created_by`, `name` and `schema_name` fields for `databricks.sdk.service.ml.Feature`.
* [Breaking] Add `catalog_name` and `schema_name` fields for `databricks.sdk.service.ml.ListFeaturesRequest`.
* Add `cross_workspace_access` field for `databricks.sdk.service.settings.CustomerFacingIngressNetworkPolicy`.
* Add `allowed_apps_user_api_scopes` and `effective_allowed_apps_user_api_scopes` fields for `databricks.sdk.service.settingsv2.Setting`.
* Add `gpu_xlarge` enum value for `databricks.sdk.service.serving.ServedModelInputWorkloadType`.
* Add `gpu_xlarge` enum value for `databricks.sdk.service.serving.ServingModelWorkloadType`.
* [Breaking] Change `list_features()` method for [w.feature_engineering](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/feature_engineering.html) workspace-level service with new required argument order.
* Add `python_operator_task` field for `databricks.sdk.service.jobs.RunTask`.
* Add `python_operator_task` field for `databricks.sdk.service.jobs.SubmitTask`.
* Add `python_operator_task` field for `databricks.sdk.service.jobs.Task`.
* Add `rolling` field for `databricks.sdk.service.ml.TimeWindow`.
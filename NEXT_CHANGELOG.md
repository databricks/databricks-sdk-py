# NEXT CHANGELOG

## Release v0.77.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `git_repository` field for `databricks.sdk.service.apps.App`.
* Add `git_source` field for `databricks.sdk.service.apps.AppDeployment`.
* Add `experiment_spec` field for `databricks.sdk.service.apps.AppManifestAppResourceSpec`.
* Add `experiment` field for `databricks.sdk.service.apps.AppResource`.
* Add `git_repository` field for `databricks.sdk.service.apps.AppUpdate`.
* Add `excluded_table_full_names` field for `databricks.sdk.service.dataquality.AnomalyDetectionConfig`.
* Add `excluded_table_full_names` field for `databricks.sdk.service.qualitymonitorv2.AnomalyDetectionConfig`.
* Add `execute` and `use_connection` enum values for `databricks.sdk.service.apps.AppManifestAppResourceUcSecurableSpecUcSecurablePermission`.
* Add `function` and `connection` enum values for `databricks.sdk.service.apps.AppManifestAppResourceUcSecurableSpecUcSecurableType`.
* Add `select`, `execute` and `use_connection` enum values for `databricks.sdk.service.apps.AppResourceUcSecurableUcSecurablePermission`.
* Add `table`, `function` and `connection` enum values for `databricks.sdk.service.apps.AppResourceUcSecurableUcSecurableType`.
* [Breaking] Remove `apply_environment()` method for [w.pipelines](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/pipelines/pipelines.html) workspace-level service.
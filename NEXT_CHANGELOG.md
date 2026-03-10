# NEXT CHANGELOG

## Release v0.98.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `genie_create_eval_run()`, `genie_get_eval_result_details()`, `genie_get_eval_run()`, `genie_list_eval_results()` and `genie_list_eval_runs()` methods for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service.
* Add `update_role()` method for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service.
* Add `telemetry_export_destinations` field for `databricks.sdk.service.apps.App`.
* Add `entities` and `timeseries_column` fields for `databricks.sdk.service.ml.Feature`.
* Add `aggregation_function` field for `databricks.sdk.service.ml.Function`.
* Add `filter_condition` field for `databricks.sdk.service.ml.KafkaSource`.
* Add `attributes` field for `databricks.sdk.service.postgres.RoleRoleStatus`.
* [Breaking] Change `entity_columns` and `timeseries_column` fields for `databricks.sdk.service.ml.DeltaTableSource` to no longer be required.
* Change `entity_columns` and `timeseries_column` fields for `databricks.sdk.service.ml.DeltaTableSource` to no longer be required.
* Change `inputs` field for `databricks.sdk.service.ml.Feature` to no longer be required.
* [Breaking] Change `inputs` field for `databricks.sdk.service.ml.Feature` to no longer be required.
* [Breaking] Change `function_type` field for `databricks.sdk.service.ml.Function` to no longer be required.
* Change `function_type` field for `databricks.sdk.service.ml.Function` to no longer be required.
* Change `entity_column_identifiers` and `timeseries_column_identifier` fields for `databricks.sdk.service.ml.KafkaSource` to no longer be required.
* [Breaking] Change `entity_column_identifiers` and `timeseries_column_identifier` fields for `databricks.sdk.service.ml.KafkaSource` to no longer be required.
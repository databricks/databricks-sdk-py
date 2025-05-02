# NEXT CHANGELOG

## Release v0.52.0

### New Features and Improvements

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added `future_feature_data_path` field for `databricks.sdk.service.ml.CreateForecastingExperimentRequest`.
* Added `exclude_columns` and `include_columns` fields for `databricks.sdk.service.pipelines.TableSpecificConfig`.
* Added `network_check_control_plane_failure`, `network_check_dns_server_failure`, `network_check_metadata_endpoint_failure`, `network_check_multiple_components_failure`, `network_check_nic_failure`, `network_check_storage_failure` and `secret_permission_denied` enum values for `databricks.sdk.service.compute.TerminationReasonCode`.
* [Breaking] Changed `pipeline_id` field for `databricks.sdk.service.pipelines.EditPipeline` to be required.
* Changed `connection_name`, `gateway_storage_catalog` and `gateway_storage_schema` fields for `databricks.sdk.service.pipelines.IngestionGatewayPipelineDefinition` to be required.
* [Breaking] Changed `connection_name`, `gateway_storage_catalog` and `gateway_storage_schema` fields for `databricks.sdk.service.pipelines.IngestionGatewayPipelineDefinition` to be required.
* Changed `kind` field for `databricks.sdk.service.pipelines.PipelineDeployment` to be required.
* [Breaking] Changed `kind` field for `databricks.sdk.service.pipelines.PipelineDeployment` to be required.
* Changed `destination_catalog`, `destination_schema` and `source_url` fields for `databricks.sdk.service.pipelines.ReportSpec` to be required.
* [Breaking] Changed `destination_catalog`, `destination_schema` and `source_url` fields for `databricks.sdk.service.pipelines.ReportSpec` to be required.
* Changed `destination_catalog`, `destination_schema` and `source_schema` fields for `databricks.sdk.service.pipelines.SchemaSpec` to be required.
* [Breaking] Changed `destination_catalog`, `destination_schema` and `source_schema` fields for `databricks.sdk.service.pipelines.SchemaSpec` to be required.
* [Breaking] Changed `destination_catalog`, `destination_schema` and `source_table` fields for `databricks.sdk.service.pipelines.TableSpec` to be required.
* Changed `destination_catalog`, `destination_schema` and `source_table` fields for `databricks.sdk.service.pipelines.TableSpec` to be required.
* [Breaking] Changed `results` field for `databricks.sdk.service.sql.ListAlertsV2Response` to type `databricks.sdk.service.sql.AlertV2List` dataclass.
* [Breaking] Changed pagination for [AlertsV2API.list_alerts](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sql/alerts_v2.html#databricks.sdk.service.sql.AlertsV2API.list_alerts) method.
* Fixed waiter for [GenieAPI.create_message](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html#databricks.sdk.service.dashboards.GenieAPI.create_message) method.

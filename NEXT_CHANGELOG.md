# NEXT CHANGELOG

## Release v0.99.0

### New Features and Improvements

### Security

### Bug Fixes

* Fixed recursive file lising in `WorkspaceClient.dbfs.list` on volumes. ([#1260](https://github.com/databricks/databricks-sdk-py/pull/1260))

### Documentation

### Internal Changes

### API Changes
* Add `connector_type` and `data_staging_options` fields for `databricks.sdk.service.pipelines.IngestionPipelineDefinition`.
* Add `ingestion_source_catalog_name`, `ingestion_source_connection_name`, `ingestion_source_schema_name`, `ingestion_source_table_name` and `ingestion_source_table_version` fields for `databricks.sdk.service.pipelines.Origin`.
* Add `sub_domain` field for `databricks.sdk.service.serving.ExternalFunctionRequest`.
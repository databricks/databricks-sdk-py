# NEXT CHANGELOG

## Release v0.92.0

### New Features and Improvements
* Add a new `_ProtobufErrorDeserializer` for handling Protobuf response errors.

### Security

### Bug Fixes

### Documentation
* Added "Retries" section to README.

### Internal Changes

### API Changes
* Add `read_only_host` field for `databricks.sdk.service.postgres.EndpointHosts`.
* Add `group` field for `databricks.sdk.service.postgres.EndpointSpec`.
* Add `group` field for `databricks.sdk.service.postgres.EndpointStatus`.
* Add `initial_endpoint_spec` field for `databricks.sdk.service.postgres.Project`.
* Add `degraded` enum value for `databricks.sdk.service.postgres.EndpointStatusState`.
* Add `patch_endpoint()` method for [w.vector_search_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/vectorsearch/vector_search_endpoints.html) workspace-level service.
* Add `app` field for `databricks.sdk.service.apps.AppResource`.
* Add `securable_kind` field for `databricks.sdk.service.apps.AppResourceUcSecurable`.
* Add `min_qps` field for `databricks.sdk.service.vectorsearch.CreateEndpoint`.
* Add `scaling_info` field for `databricks.sdk.service.vectorsearch.EndpointInfo`.
* Add `modify` enum value for `databricks.sdk.service.apps.AppResourceUcSecurableUcSecurablePermission`.
* Add `could_not_get_dashboard_schema_exception` enum value for `databricks.sdk.service.dashboards.MessageErrorType`.
* Add `replace_where_overrides` field for `databricks.sdk.service.pipelines.StartUpdate`.
* Add `hivemetastore_connectivity_failure` enum value for `databricks.sdk.service.compute.TerminationReasonCode`.
* Add `hivemetastore_connectivity_failure` enum value for `databricks.sdk.service.sql.TerminationReasonCode`.

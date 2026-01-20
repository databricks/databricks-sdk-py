# NEXT CHANGELOG

## Release v0.79.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `full_refresh_window` field for `databricks.sdk.service.pipelines.IngestionPipelineDefinition`.
* Add `auto_full_refresh_policy` field for `databricks.sdk.service.pipelines.TableSpecificConfig`.
* Add `hosts` field for `databricks.sdk.service.postgres.EndpointStatus`.
* Add `owner` field for `databricks.sdk.service.postgres.ProjectStatus`.
* Add `validity_check_configurations` field for `databricks.sdk.service.qualitymonitorv2.QualityMonitor`.
* Add `burst_scaling_enabled` field for `databricks.sdk.service.serving.PtServedModel`.
* Add `system_managed` enum value for `databricks.sdk.service.jobs.JobDeploymentKind`.
* Add `endpoint_type_read_write` and `endpoint_type_read_only` enum values for `databricks.sdk.service.postgres.EndpointType`.
* Add `deleted` enum value for `databricks.sdk.service.vectorsearch.EndpointStatusState`.
* [Breaking] Remove `host`, `last_active_time`, `start_time` and `suspend_time` fields for `databricks.sdk.service.postgres.EndpointStatus`.
* [Breaking] Remove `compute_last_active_time` field for `databricks.sdk.service.postgres.ProjectStatus`.
* [Breaking] Remove `read_write` and `read_only` enum values for `databricks.sdk.service.postgres.EndpointType`.
* Add `create_default_warehouse_override()`, `delete_default_warehouse_override()`, `get_default_warehouse_override()`, `list_default_warehouse_overrides()` and `update_default_warehouse_override()` methods for [w.warehouses](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sql/warehouses.html) workspace-level service.
* Add `driver_node_type_flexibility` and `worker_node_type_flexibility` fields for `databricks.sdk.service.compute.ClusterAttributes`.
* Add `driver_node_type_flexibility` and `worker_node_type_flexibility` fields for `databricks.sdk.service.compute.ClusterDetails`.
* Add `driver_node_type_flexibility` and `worker_node_type_flexibility` fields for `databricks.sdk.service.compute.ClusterSpec`.
* Add `driver_node_type_flexibility` and `worker_node_type_flexibility` fields for `databricks.sdk.service.compute.CreateCluster`.
* Add `node_type_flexibility` field for `databricks.sdk.service.compute.CreateInstancePool`.
* Add `driver_node_type_flexibility` and `worker_node_type_flexibility` fields for `databricks.sdk.service.compute.EditCluster`.
* Add `node_type_flexibility` field for `databricks.sdk.service.compute.EditInstancePool`.
* Add `node_type_flexibility` field for `databricks.sdk.service.compute.GetInstancePool`.
* Add `node_type_flexibility` field for `databricks.sdk.service.compute.InstancePoolAndStats`.
* Add `driver_node_type_flexibility` and `worker_node_type_flexibility` fields for `databricks.sdk.service.compute.UpdateClusterResource`.
* Add `expire_time` and `ttl` fields for `databricks.sdk.service.postgres.BranchSpec`.
* Add `expire_time` field for `databricks.sdk.service.postgres.BranchStatus`.
* [Breaking] Change `create_branch()`, `create_endpoint()` and `create_project()` methods for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service with new required argument order.
* [Breaking] Change `branch_id` field for `databricks.sdk.service.postgres.CreateBranchRequest` to be required.
* [Breaking] Change `endpoint_id` field for `databricks.sdk.service.postgres.CreateEndpointRequest` to be required.
* [Breaking] Change `project_id` field for `databricks.sdk.service.postgres.CreateProjectRequest` to be required.
* [Breaking] Remove `default` field for `databricks.sdk.service.postgres.BranchSpec`.
* [Breaking] Remove `settings` field for `databricks.sdk.service.postgres.ProjectSpec`.
* [Breaking] Remove `settings` field for `databricks.sdk.service.postgres.ProjectStatus`.
* Add `generate_database_credential()` method for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service.
* Add `get_public_account_user_preference()`, `list_account_user_preferences_metadata()` and `patch_public_account_user_preference()` methods for [a.account_settings_v2](https://databricks-sdk-py.readthedocs.io/en/latest/account/settingsv2/account_settings_v2.html) account-level service.
* Add `stderr` field for `databricks.sdk.service.compute.InitScriptInfoAndExecutionDetails`.
* Add `no_expiry` field for `databricks.sdk.service.postgres.BranchSpec`.
* Add `outputs` field for `databricks.sdk.service.serving.QueryEndpointResponse`.
* Add `principal_id` field for `databricks.sdk.service.workspace.CreateCredentialsRequest`.
* Add `principal_id` field for `databricks.sdk.service.workspace.DeleteCredentialsRequest`.
* Add `principal_id` field for `databricks.sdk.service.workspace.GetCredentialsRequest`.
* Add `principal_id` field for `databricks.sdk.service.workspace.ListCredentialsRequest`.
* Add `principal_id` field for `databricks.sdk.service.workspace.UpdateCredentialsRequest`.
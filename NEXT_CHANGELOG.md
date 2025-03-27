# NEXT CHANGELOG

## Release v0.48.0

### New Features and Improvements

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added `execution_details` and `script` fields for `databricks.sdk.service.compute.InitScriptInfoAndExecutionDetails`.
* Added `supports_elastic_disk` field for `databricks.sdk.service.compute.NodeType`.
* Added `data_granularity_quantity` field for `databricks.sdk.service.ml.CreateForecastingExperimentRequest`.
* [Breaking] Added `data_granularity_unit` field for `databricks.sdk.service.ml.CreateForecastingExperimentRequest`.
* Added `aliases`, `comment`, `data_type`, `dependency_list`, `full_data_type`, `id`, `input_params`, `name`, `properties`, `routine_definition`, `schema`, `securable_kind`, `share`, `share_id`, `storage_location` and `tags` fields for `databricks.sdk.service.sharing.Function`.
* [Breaking] Changed `create_experiment()` method for [w.forecasting](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/forecasting.html) workspace-level service with new required argument order.
* [Breaking] Changed `instance_type_id` field for `databricks.sdk.service.compute.NodeInstanceType` to no longer be required.
* [Breaking] Changed `category` field for `databricks.sdk.service.compute.NodeType` to no longer be required.
* [Breaking] Changed `functions` field for `databricks.sdk.service.sharing.ListProviderShareAssetsResponse` to type `databricks.sdk.service.sharing.FunctionList` dataclass.
* [Breaking] Removed `abfss`, `dbfs`, `error_message`, `execution_duration_seconds`, `file`, `gcs`, `s3`, `status`, `volumes` and `workspace` fields for `databricks.sdk.service.compute.InitScriptInfoAndExecutionDetails`.
* [Breaking] Removed `forecast_granularity` field for `databricks.sdk.service.ml.CreateForecastingExperimentRequest`.
* [Breaking] Removed `jwks_uri` field for `databricks.sdk.service.oauth2.OidcFederationPolicy`.
* [Breaking] Removed `fallback_config` field for `databricks.sdk.service.serving.AiGatewayConfig`.
* [Breaking] Removed `custom_provider_config` field for `databricks.sdk.service.serving.ExternalModel`.
* [Breaking] Removed `fallback_config` field for `databricks.sdk.service.serving.PutAiGatewayRequest`.
* [Breaking] Removed `fallback_config` field for `databricks.sdk.service.serving.PutAiGatewayResponse`.
* [Breaking] Removed `aliases`, `comment`, `data_type`, `dependency_list`, `full_data_type`, `id`, `input_params`, `name`, `properties`, `routine_definition`, `schema`, `securable_kind`, `share`, `share_id`, `storage_location` and `tags` fields for `databricks.sdk.service.sharing.DeltaSharingFunction`.
* [Breaking] Removed `access_token_failure`, `allocation_timeout`, `allocation_timeout_node_daemon_not_ready`, `allocation_timeout_no_healthy_clusters`, `allocation_timeout_no_matched_clusters`, `allocation_timeout_no_ready_clusters`, `allocation_timeout_no_unallocated_clusters`, `allocation_timeout_no_warmed_up_clusters`, `aws_inaccessible_kms_key_failure`, `aws_instance_profile_update_failure`, `aws_invalid_key_pair`, `aws_invalid_kms_key_state`, `aws_resource_quota_exceeded`, `azure_packed_deployment_partial_failure`, `bootstrap_timeout_due_to_misconfig`, `budget_policy_limit_enforcement_activated`, `budget_policy_resolution_failure`, `cloud_account_setup_failure`, `cloud_operation_cancelled`, `cloud_provider_instance_not_launched`, `cloud_provider_launch_failure_due_to_misconfig`, `cloud_provider_resource_stockout_due_to_misconfig`, `cluster_operation_throttled`, `cluster_operation_timeout`, `control_plane_request_failure_due_to_misconfig`, `data_access_config_changed`, `disaster_recovery_replication`, `driver_eviction`, `driver_launch_timeout`, `driver_node_unreachable`, `driver_out_of_disk`, `driver_out_of_memory`, `driver_pod_creation_failure`, `driver_unexpected_failure`, `dynamic_spark_conf_size_exceeded`, `eos_spark_image`, `executor_pod_unscheduled`, `gcp_api_rate_quota_exceeded`, `gcp_forbidden`, `gcp_iam_timeout`, `gcp_inaccessible_kms_key_failure`, `gcp_insufficient_capacity`, `gcp_ip_space_exhausted`, `gcp_kms_key_permission_denied`, `gcp_not_found`, `gcp_resource_quota_exceeded`, `gcp_service_account_access_denied`, `gcp_service_account_not_found`, `gcp_subnet_not_ready`, `gcp_trusted_image_projects_violated`, `gke_based_cluster_termination`, `init_container_not_finished`, `instance_pool_max_capacity_reached`, `instance_pool_not_found`, `instance_unreachable_due_to_misconfig`, `internal_capacity_failure`, `invalid_aws_parameter`, `invalid_instance_placement_protocol`, `invalid_worker_image_failure`, `in_penalty_box`, `lazy_allocation_timeout`, `maintenance_mode`, `netvisor_setup_timeout`, `no_matched_k8s`, `no_matched_k8s_testing_tag`, `pod_assignment_failure`, `pod_scheduling_failure`, `resource_usage_blocked`, `secret_creation_failure`, `serverless_long_running_terminated`, `spark_image_download_throttled`, `spark_image_not_found`, `ssh_bootstrap_failure`, `storage_download_failure_due_to_misconfig`, `storage_download_failure_slow`, `storage_download_failure_throttled`, `unexpected_pod_recreation`, `user_initiated_vm_termination` and `workspace_update` enum values for `databricks.sdk.service.compute.TerminationReasonCode`.
* [Breaking] Removed `generated_sql_query_too_long_exception` and `missing_sql_query_exception` enum values for `databricks.sdk.service.dashboards.MessageErrorType`.
* [Breaking] Removed `balanced` enum value for `databricks.sdk.service.jobs.PerformanceTarget`.
* [Breaking] Removed `listing_resource` enum value for `databricks.sdk.service.marketplace.FileParentType`.
* [Breaking] Removed `app` enum value for `databricks.sdk.service.marketplace.MarketplaceFileType`.
* [Breaking] Removed `custom` enum value for `databricks.sdk.service.serving.ExternalModelProvider`.

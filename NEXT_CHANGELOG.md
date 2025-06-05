# NEXT CHANGELOG

## Release v0.56.0

### New Features and Improvements

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added `databricks.sdk.service.aibuilder`, `databricks.sdk.service.database` and `databricks.sdk.service.qualitymonitorv2` packages.
* Added [w.custom_llms](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/aibuilder/custom_llms.html) workspace-level service.
* Added [w.dashboard_email_subscriptions](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/settings/dashboard_email_subscriptions.html) workspace-level service and [w.sql_results_download](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/settings/sql_results_download.html) workspace-level service.
* Added [w.database](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/database/database.html) workspace-level service.
* Added [w.quality_monitor_v2](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/qualitymonitorv2/quality_monitor_v2.html) workspace-level service.
* Added `update_private_endpoint_rule()` method for [a.network_connectivity](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/network_connectivity.html) account-level service.
* Added `list_spaces()` method for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service.
* Added `page_token` field for `databricks.sdk.service.billing.ListLogDeliveryRequest`.
* Added `next_page_token` field for `databricks.sdk.service.billing.WrappedLogDeliveryConfigurations`.
* Added `next_page_token` field for `databricks.sdk.service.catalog.EffectivePermissionsList`.
* Added `max_results` and `page_token` fields for `databricks.sdk.service.catalog.GetEffectiveRequest`.
* Added `max_results` and `page_token` fields for `databricks.sdk.service.catalog.GetGrantRequest`.
* Added `next_page_token` field for `databricks.sdk.service.catalog.ListMetastoresResponse`.
* Added `clean_room_name` field for `databricks.sdk.service.cleanrooms.CleanRoomAsset`.
* [Breaking] Added `name` field for `databricks.sdk.service.cleanrooms.DeleteCleanRoomAssetRequest`.
* [Breaking] Added `name` field for `databricks.sdk.service.cleanrooms.GetCleanRoomAssetRequest`.
* Added `trigger_state` field for `databricks.sdk.service.jobs.BaseJob`.
* Added `trigger_state` field for `databricks.sdk.service.jobs.Job`.
* Added `dbt_cloud_output` field for `databricks.sdk.service.jobs.RunOutput`.
* Added `dbt_cloud_task` field for `databricks.sdk.service.jobs.RunTask`.
* Added `dbt_cloud_task` field for `databricks.sdk.service.jobs.SubmitTask`.
* Added `dbt_cloud_task` field for `databricks.sdk.service.jobs.Task`.
* Added `tags` field for `databricks.sdk.service.pipelines.CreatePipeline`.
* Added `tags` field for `databricks.sdk.service.pipelines.EditPipeline`.
* Added `tags` field for `databricks.sdk.service.pipelines.PipelineSpec`.
* Added `max_provisioned_concurrency` and `min_provisioned_concurrency` fields for `databricks.sdk.service.serving.ServedEntityInput`.
* Added `max_provisioned_concurrency` and `min_provisioned_concurrency` fields for `databricks.sdk.service.serving.ServedEntityOutput`.
* Added `max_provisioned_concurrency` and `min_provisioned_concurrency` fields for `databricks.sdk.service.serving.ServedModelInput`.
* Added `max_provisioned_concurrency` and `min_provisioned_concurrency` fields for `databricks.sdk.service.serving.ServedModelOutput`.
* Added `endpoint_service` and `resource_names` fields for `databricks.sdk.service.settings.CreatePrivateEndpointRule`.
* Added `aws_private_endpoint_rules` field for `databricks.sdk.service.settings.NccEgressTargetRules`.
* Added `task_time_over_time_range` field for `databricks.sdk.service.sql.QueryMetrics`.
* Added `deltasharing_catalog`, `foreign_catalog`, `internal_catalog`, `managed_catalog`, `managed_online_catalog`, `system_catalog` and `unknown_catalog_type` enum values for `databricks.sdk.service.catalog.CatalogType`.
* Added `ga4_raw_data`, `power_bi`, `salesforce`, `salesforce_data_cloud`, `servicenow`, `unknown_connection_type` and `workday_raas` enum values for `databricks.sdk.service.catalog.ConnectionType`.
* Added `oauth_access_token`, `oauth_m2m`, `oauth_refresh_token`, `oauth_resource_owner_password`, `oauth_u2m`, `oauth_u2m_mapping`, `oidc_token`, `pem_private_key`, `service_credential` and `unknown_credential_type` enum values for `databricks.sdk.service.catalog.CredentialType`.
* Added `internal` and `internal_and_external` enum values for `databricks.sdk.service.catalog.DeltaSharingScopeEnum`.
* Added `catalog`, `clean_room`, `connection`, `credential`, `external_location`, `external_metadata`, `function`, `metastore`, `pipeline`, `provider`, `recipient`, `schema`, `share`, `staging_table`, `storage_credential`, `table`, `unknown_securable_type` and `volume` enum values for `databricks.sdk.service.catalog.SecurableType`.
* Added `cluster_migrated` enum value for `databricks.sdk.service.compute.EventType`.
* Added `driver_unhealthy` enum value for `databricks.sdk.service.compute.TerminationReasonCode`.
* Added `teradata` enum value for `databricks.sdk.service.pipelines.IngestionSourceType`.
* Added `oidc_federation` enum value for `databricks.sdk.service.sharing.AuthenticationType`.
* [Breaking] Changed `create()` method for [a.log_delivery](https://databricks-sdk-py.readthedocs.io/en/latest/account/billing/log_delivery.html) account-level service with new required argument order.
* [Breaking] Changed `get()` method for [a.log_delivery](https://databricks-sdk-py.readthedocs.io/en/latest/account/billing/log_delivery.html) account-level service to return `databricks.sdk.service.billing.GetLogDeliveryConfigurationResponse` dataclass.
* [Breaking] Changed `create_private_endpoint_rule()`, `delete_private_endpoint_rule()` and `get_private_endpoint_rule()` methods for [a.network_connectivity](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/network_connectivity.html) account-level service to return `databricks.sdk.service.settings.NccPrivateEndpointRule` dataclass.
* [Breaking] Changed `list_private_endpoint_rules()` method for [a.network_connectivity](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/network_connectivity.html) account-level service to return `databricks.sdk.service.settings.ListPrivateEndpointRulesResponse` dataclass.
* [Breaking] Changed `delete()` and `get()` methods for [w.clean_room_assets](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/cleanrooms/clean_room_assets.html) workspace-level service . Method path has changed.
* [Breaking] Changed `delete()` and `get()` methods for [w.clean_room_assets](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/cleanrooms/clean_room_assets.html) workspace-level service with new required argument order.
* [Breaking] Changed `get()` method for [w.grants](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/grants.html) workspace-level service to return `databricks.sdk.service.catalog.GetPermissionsResponse` dataclass.
* [Breaking] Changed `update()` method for [w.grants](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/grants.html) workspace-level service to return `databricks.sdk.service.catalog.UpdatePermissionsResponse` dataclass.
* [Breaking] Changed `list()` method for [w.metastores](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/metastores.html) workspace-level service to require request of `databricks.sdk.service.catalog.ListMetastoresRequest` dataclass.
* Changed `account_id`, `credentials_id`, `log_type`, `output_format` and `storage_configuration_id` fields for `databricks.sdk.service.billing.LogDeliveryConfiguration` to be required.
* Changed `message` and `status` fields for `databricks.sdk.service.billing.LogDeliveryStatus` to be required.
* [Breaking] Changed `log_delivery_configuration` field for `databricks.sdk.service.billing.WrappedCreateLogDeliveryConfiguration` to be required.
* [Breaking] Changed `securable_type` field for `databricks.sdk.service.catalog.ConnectionInfo` to type `databricks.sdk.service.catalog.SecurableType` dataclass.
* [Breaking] Changed `securable_type` field for `databricks.sdk.service.catalog.GetEffectiveRequest` to type `str` dataclass.
* [Breaking] Changed `securable_type` field for `databricks.sdk.service.catalog.GetGrantRequest` to type `str` dataclass.
* [Breaking] Changed `delta_sharing_scope` field for `databricks.sdk.service.catalog.GetMetastoreSummaryResponse` to type `databricks.sdk.service.catalog.DeltaSharingScopeEnum` dataclass.
* [Breaking] Changed `delta_sharing_scope` field for `databricks.sdk.service.catalog.MetastoreInfo` to type `databricks.sdk.service.catalog.DeltaSharingScopeEnum` dataclass.
* [Breaking] Changed `catalog_type` field for `databricks.sdk.service.catalog.SchemaInfo` to type `databricks.sdk.service.catalog.CatalogType` dataclass.
* [Breaking] Changed `delta_sharing_scope` field for `databricks.sdk.service.catalog.UpdateMetastore` to type `databricks.sdk.service.catalog.DeltaSharingScopeEnum` dataclass.
* [Breaking] Changed `securable_type` field for `databricks.sdk.service.catalog.UpdatePermissions` to type `str` dataclass.
* Changed `resource_id` field for `databricks.sdk.service.settings.CreatePrivateEndpointRule` to no longer be required.
* [Breaking] Changed pagination for [NetworkConnectivityAPI.list_private_endpoint_rules](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/network_connectivity.html#databricks.sdk.service.settings.NetworkConnectivityAPI.list_private_endpoint_rules) method.
* [Breaking] Removed [w.database_instances](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/database_instances.html) workspace-level service.
* [Breaking] Removed [w.query_execution](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/query_execution.html) workspace-level service.
* [Breaking] Removed `update_ncc_azure_private_endpoint_rule_public()` method for [a.network_connectivity](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/network_connectivity.html) account-level service.
* [Breaking] Removed `get_credentials_for_trace_data_download()`, `get_credentials_for_trace_data_upload()` and `list_logged_model_artifacts()` methods for [w.experiments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/experiments.html) workspace-level service.
* [Breaking] Removed `get_published_dashboard_embedded()` method for [w.lakeview_embedded](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/lakeview_embedded.html) workspace-level service.
* [Breaking] Removed `asset_full_name` field for `databricks.sdk.service.cleanrooms.DeleteCleanRoomAssetRequest`.
* [Breaking] Removed `asset_full_name` field for `databricks.sdk.service.cleanrooms.GetCleanRoomAssetRequest`.
* [Breaking] Removed `internal` and `internal_and_external` enum values for `databricks.sdk.service.catalog.GetMetastoreSummaryResponseDeltaSharingScope`.
* [Breaking] Removed `internal` and `internal_and_external` enum values for `databricks.sdk.service.catalog.MetastoreInfoDeltaSharingScope`.
* [Breaking] Removed `catalog`, `clean_room`, `connection`, `credential`, `external_location`, `external_metadata`, `function`, `metastore`, `pipeline`, `provider`, `recipient`, `schema`, `share`, `staging_table`, `storage_credential`, `table`, `unknown_securable_type` and `volume` enum values for `databricks.sdk.service.catalog.SecurableType`.
* [Breaking] Removed `internal` and `internal_and_external` enum values for `databricks.sdk.service.catalog.UpdateMetastoreDeltaSharingScope`.

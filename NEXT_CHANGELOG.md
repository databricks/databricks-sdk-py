# NEXT CHANGELOG

## Release v0.58.0

### New Features and Improvements

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.ClusterAttributes`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.ClusterDetails`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.ClusterSpec`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.CreateCluster`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.CreateInstancePool`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.EditCluster`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.EditInstancePool`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.GetInstancePool`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.InstancePoolAndStats`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.UpdateClusterResource`.
* Added `r` enum value for `databricks.sdk.service.compute.Language`.
* Added `continuous` and `continuous_restart` enum values for `databricks.sdk.service.jobs.TriggerType`.
* Added [w.external_lineage](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/external_lineage.html) workspace-level service and [w.external_metadata](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/external_metadata.html) workspace-level service.
* Added [w.materialized_features](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/materialized_features.html) workspace-level service.
* Added `delete_conversation()`, `list_conversations()` and `trash_space()` methods for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service.
* Added `create_database_instance_role()`, `delete_database_instance_role()`, `get_database_instance_role()` and `list_database_instance_roles()` methods for [w.database](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/database/database.html) workspace-level service.
* Added `connection` and `credential` fields for `databricks.sdk.service.catalog.Dependency`.
* Added `rely` field for `databricks.sdk.service.catalog.ForeignKeyConstraint`.
* Added `rely` field for `databricks.sdk.service.catalog.PrimaryKeyConstraint`.
* Added `securable_kind_manifest` field for `databricks.sdk.service.catalog.TableInfo`.
* Added `securable_kind_manifest` field for `databricks.sdk.service.catalog.TableSummary`.
* Added `child_instance_refs`, `effective_enable_readable_secondaries`, `effective_node_count`, `effective_retention_window_in_days`, `enable_readable_secondaries`, `node_count`, `parent_instance_ref`, `read_only_dns` and `retention_window_in_days` fields for `databricks.sdk.service.database.DatabaseInstance`.
* Added `claims` field for `databricks.sdk.service.database.GenerateDatabaseCredentialRequest`.
* Added `last_sync` field for `databricks.sdk.service.database.SyncedTableStatus`.
* Added `activity` field for `databricks.sdk.service.ml.DeleteTransitionRequestResponse`.
* Added `max_results` field for `databricks.sdk.service.ml.ListWebhooksRequest`.
* Added `body` and `status_code` fields for `databricks.sdk.service.ml.TestRegistryWebhookResponse`.
* Added `model_version_databricks` field for `databricks.sdk.service.ml.TransitionStageResponse`.
* Added `registered_model` field for `databricks.sdk.service.ml.UpdateModelResponse`.
* Added `model_version` field for `databricks.sdk.service.ml.UpdateModelVersionResponse`.
* Added `webhook` field for `databricks.sdk.service.ml.UpdateWebhookResponse`.
* Added `run_as` field for `databricks.sdk.service.pipelines.GetPipelineResponse`.
* Added `principal` field for `databricks.sdk.service.serving.AiGatewayRateLimit`.
* Added `description` field for `databricks.sdk.service.serving.CreateServingEndpoint`.
* Added `served_entity_name` field for `databricks.sdk.service.serving.Route`.
* Added `any_static_credential` enum value for `databricks.sdk.service.catalog.CredentialType`.
* Added `databricks_row_store_format`, `delta_uniform_hudi`, `delta_uniform_iceberg`, `hive`, `iceberg`, `mongodb_format`, `oracle_format`, `salesforce_data_cloud_format` and `teradata_format` enum values for `databricks.sdk.service.catalog.DataSourceFormat`.
* Added `metric_view` enum value for `databricks.sdk.service.catalog.TableType`.
* Added `security_agents_failed_initial_verification` enum value for `databricks.sdk.service.compute.TerminationReasonCode`.
* Added `can_create_registered_model` enum value for `databricks.sdk.service.ml.PermissionLevel`.
* Added `bigquery` enum value for `databricks.sdk.service.pipelines.IngestionSourceType`.
* Added `append_only` enum value for `databricks.sdk.service.pipelines.TableSpecificConfigScdType`.
* Added `service_principal` and `user_group` enum values for `databricks.sdk.service.serving.AiGatewayRateLimitKey`.
* [Breaking] Changed `cancel_optimize()` and `delete_custom_llm()` methods for [w.ai_builder](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/aibuilder/ai_builder.html) workspace-level service to return `any` dataclass.
* [Breaking] Changed `delete()` method for [a.budget_policy](https://databricks-sdk-py.readthedocs.io/en/latest/account/billing/budget_policy.html) account-level service to return `any` dataclass.
* [Breaking] Changed `delete()` method for [w.online_tables](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/online_tables.html) workspace-level service to return `any` dataclass.
* [Breaking] Changed `delete()` method for [w.clean_rooms](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/cleanrooms/clean_rooms.html) workspace-level service to return `any` dataclass.
* [Breaking] Changed `delete_schedule()` and `delete_subscription()` methods for [w.lakeview](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/lakeview.html) workspace-level service to return `any` dataclass.
* [Breaking] Changed `delete_database_catalog()`, `delete_database_instance()`, `delete_database_table()` and `delete_synced_database_table()` methods for [w.database](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/database/database.html) workspace-level service to return `any` dataclass.
* [Breaking] Changed `delete_online_store()` method for [w.feature_store](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/feature_store.html) workspace-level service to return `any` dataclass.
* [Breaking] Changed `delete_transition_request()`, `update_model()`, `update_model_version()` and `update_webhook()` methods for [w.model_registry](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/model_registry.html) workspace-level service return type to become non-empty.
* [Breaking] Changed `delete_webhook()` method for [w.model_registry](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/model_registry.html) workspace-level service with new required argument order.
* [Breaking] Changed `delete()` method for [a.account_federation_policy](https://databricks-sdk-py.readthedocs.io/en/latest/account/oauth2/federation_policy.html) account-level service to return `any` dataclass.
* [Breaking] Changed `delete()` method for [a.service_principal_federation_policy](https://databricks-sdk-py.readthedocs.io/en/latest/account/oauth2/service_principal_federation_policy.html) account-level service to return `any` dataclass.
* [Breaking] Changed `delete_quality_monitor()` method for [w.quality_monitor_v2](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/qualitymonitorv2/quality_monitor_v2.html) workspace-level service to return `any` dataclass.
* [Breaking] Changed `delete_network_connectivity_configuration()` method for [a.network_connectivity](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/network_connectivity.html) account-level service to return `any` dataclass.
* [Breaking] Changed `delete_network_policy_rpc()` method for [a.network_policies](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/network_policies.html) account-level service to return `any` dataclass.
* [Breaking] Changed `delete()` method for [w.recipient_federation_policies](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sharing/recipient_federation_policies.html) workspace-level service to return `any` dataclass.
* [Breaking] Changed `list()` method for [w.alerts_legacy](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sql/alerts_legacy.html) workspace-level service . New request type is `any` dataclass.
* [Breaking] Changed `update()` method for [w.dashboard_widgets](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sql/dashboard_widgets.html) workspace-level service . New request type is `databricks.sdk.service.sql.UpdateWidgetRequest` dataclass.
* [Breaking] Changed `list()` method for [w.data_sources](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sql/data_sources.html) workspace-level service . New request type is `any` dataclass.
* [Breaking] Changed `create()` method for [w.query_visualizations_legacy](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sql/query_visualizations_legacy.html) workspace-level service with new required argument order.
* [Breaking] Changed `from_stage` and `to_stage` fields for `databricks.sdk.service.ml.Activity` to type `str` dataclass.
* [Breaking] Changed `stage` field for `databricks.sdk.service.ml.ApproveTransitionRequest` to type `str` dataclass.
* [Breaking] Changed `stage` field for `databricks.sdk.service.ml.CreateTransitionRequest` to type `str` dataclass.
* [Breaking] Changed `stage` field for `databricks.sdk.service.ml.DeleteTransitionRequestRequest` to type `str` dataclass.
* [Breaking] Changed `id` field for `databricks.sdk.service.ml.DeleteWebhookRequest` to be required.
* [Breaking] Changed `capacity` field for `databricks.sdk.service.ml.OnlineStore` to be required.
* Changed `capacity` field for `databricks.sdk.service.ml.OnlineStore` to be required.
* [Breaking] Changed `online_table_name` field for `databricks.sdk.service.ml.PublishSpec` to be required.
* [Breaking] Changed `stage` field for `databricks.sdk.service.ml.RejectTransitionRequest` to type `str` dataclass.
* [Breaking] Changed `stage` field for `databricks.sdk.service.ml.TransitionModelVersionStageDatabricks` to type `str` dataclass.
* [Breaking] Changed `to_stage` field for `databricks.sdk.service.ml.TransitionRequest` to type `str` dataclass.
* Changed `served_model_name` field for `databricks.sdk.service.serving.Route` to no longer be required.
* [Breaking] Changed `served_model_name` field for `databricks.sdk.service.serving.Route` to no longer be required.
* Changed pagination for [TablesAPI.list](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/tables.html#databricks.sdk.service.catalog.TablesAPI.list) method.
* Changed pagination for [TablesAPI.list_summaries](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/tables.html#databricks.sdk.service.catalog.TablesAPI.list_summaries) method.
* [Breaking] Removed `generate_download_full_query_result()` and `get_download_full_query_result()` methods for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service.
* [Breaking] Removed `include_delta_metadata` field for `databricks.sdk.service.catalog.ListTablesRequest`.
* [Breaking] Removed `webhook` field for `databricks.sdk.service.ml.TestRegistryWebhookResponse`.
* [Breaking] Removed `model_version` field for `databricks.sdk.service.ml.TransitionStageResponse`.
* [Breaking] Removed `unknown_catalog_type` enum value for `databricks.sdk.service.catalog.CatalogType`.
* [Breaking] Removed `hive_custom` and `hive_serde` enum values for `databricks.sdk.service.catalog.DataSourceFormat`.
* [Breaking] Removed `unknown_securable_type` enum value for `databricks.sdk.service.catalog.SecurableType`.
* [Breaking] Removed `archived`, `none`, `production` and `staging` enum values for `databricks.sdk.service.ml.DeleteTransitionRequestStage`.
* [Breaking] Removed `archived`, `none`, `production` and `staging` enum values for `databricks.sdk.service.ml.Stage`.

# NEXT CHANGELOG

## Release v0.54.0

### New Features and Improvements

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added [a.llm_proxy_partner_powered_account](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/settings/llm_proxy_partner_powered_account.html) account-level service, [a.llm_proxy_partner_powered_enforce](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/settings/llm_proxy_partner_powered_enforce.html) account-level service, [w.llm_proxy_partner_powered_workspace](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/settings/settings/llm_proxy_partner_powered_workspace.html) workspace-level service, [a.network_policies](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/network_policies.html) account-level service and [a.workspace_network_configuration](https://databricks-sdk-py.readthedocs.io/en/latest/account/settings/workspace_network_configuration.html) account-level service.
* Added [w.database_instances](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/database_instances.html) workspace-level service.
* Added [w.recipient_federation_policies](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sharing/recipient_federation_policies.html) workspace-level service.
* Added `create_logged_model()`, `delete_logged_model()`, `delete_logged_model_tag()`, `finalize_logged_model()`, `get_logged_model()`, `list_logged_model_artifacts()`, `log_logged_model_params()`, `log_outputs()`, `search_logged_models()` and `set_logged_model_tags()` methods for [w.experiments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/experiments.html) workspace-level service.
* Added `create_provisioned_throughput_endpoint()` and `update_provisioned_throughput_endpoint_config()` methods for [w.serving_endpoints](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/serving/serving_endpoints.html) workspace-level service.
* Added `uc_securable` field for `databricks.sdk.service.apps.AppResource`.
* Added `enable_file_events` and `file_event_queue` fields for `databricks.sdk.service.catalog.CreateExternalLocation`.
* Added `catalog_name` field for `databricks.sdk.service.catalog.EnableRequest`.
* Added `enable_file_events` and `file_event_queue` fields for `databricks.sdk.service.catalog.ExternalLocationInfo`.
* Added `timeseries_columns` field for `databricks.sdk.service.catalog.PrimaryKeyConstraint`.
* Added `enable_file_events` and `file_event_queue` fields for `databricks.sdk.service.catalog.UpdateExternalLocation`.
* Added `review_state`, `reviews` and `runner_collaborator_aliases` fields for `databricks.sdk.service.cleanrooms.CleanRoomAssetNotebook`.
* Added `notebook_etag` and `notebook_updated_at` fields for `databricks.sdk.service.cleanrooms.CleanRoomNotebookTaskRun`.
* Added `policy_id` and `service_principal_id` fields for `databricks.sdk.service.oauth2.FederationPolicy`.
* Added `root_path` field for `databricks.sdk.service.pipelines.CreatePipeline`.
* Added `root_path` field for `databricks.sdk.service.pipelines.EditPipeline`.
* Added `source_type` field for `databricks.sdk.service.pipelines.IngestionPipelineDefinition`.
* Added `glob` field for `databricks.sdk.service.pipelines.PipelineLibrary`.
* Added `root_path` field for `databricks.sdk.service.pipelines.PipelineSpec`.
* Added `provisioned_model_units` field for `databricks.sdk.service.serving.ServedEntityInput`.
* Added `provisioned_model_units` field for `databricks.sdk.service.serving.ServedEntityOutput`.
* Added `provisioned_model_units` field for `databricks.sdk.service.serving.ServedModelInput`.
* Added `provisioned_model_units` field for `databricks.sdk.service.serving.ServedModelOutput`.
* Added `materialization_namespace` field for `databricks.sdk.service.sharing.Table`.
* Added `omit_permissions_list` field for `databricks.sdk.service.sharing.UpdateSharePermissions`.
* Added `auto_resolve_display_name` field for `databricks.sdk.service.sql.UpdateAlertRequest`.
* Added `auto_resolve_display_name` field for `databricks.sdk.service.sql.UpdateQueryRequest`.
* Added `internal_catalog`, `managed_online_catalog` and `unknown_catalog_type` enum values for `databricks.sdk.service.catalog.CatalogType`.
* Added `catalog`, `clean_room`, `connection`, `credential`, `external_location`, `external_metadata`, `function`, `metastore`, `pipeline`, `provider`, `recipient`, `schema`, `share`, `staging_table`, `storage_credential`, `table`, `unknown_securable_type` and `volume` enum values for `databricks.sdk.service.catalog.SecurableType`.
* Added `describe_query_invalid_sql_error`, `describe_query_timeout`, `describe_query_unexpected_failure`, `invalid_chat_completion_arguments_json_exception`, `invalid_sql_multiple_dataset_references_exception`, `invalid_sql_multiple_statements_exception` and `invalid_sql_unknown_table_exception` enum values for `databricks.sdk.service.dashboards.MessageErrorType`.
* Added `can_create` and `can_monitor_only` enum values for `databricks.sdk.service.iam.PermissionLevel`.
* Added `success_with_failures` enum value for `databricks.sdk.service.jobs.TerminationCodeCode`.
* Added `infrastructure_maintenance` enum value for `databricks.sdk.service.pipelines.StartUpdateCause`.
* Added `infrastructure_maintenance` enum value for `databricks.sdk.service.pipelines.UpdateInfoCause`.
* [Breaking] Changed `create_alert()` and `update_alert()` methods for [w.alerts_v2](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sql/alerts_v2.html) workspace-level service with new required argument order.
* [Breaking] Changed `set()` method for [w.permissions](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/iam/permissions.html) workspace-level service . New request type is `databricks.sdk.service.iam.SetObjectPermissions` dataclass.
* [Breaking] Changed `update()` method for [w.permissions](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/iam/permissions.html) workspace-level service . New request type is `databricks.sdk.service.iam.UpdateObjectPermissions` dataclass.
* [Breaking] Changed `get()` method for [w.workspace_bindings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/workspace_bindings.html) workspace-level service to return `databricks.sdk.service.catalog.GetCatalogWorkspaceBindingsResponse` dataclass.
* [Breaking] Changed `get_bindings()` method for [w.workspace_bindings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/workspace_bindings.html) workspace-level service to return `databricks.sdk.service.catalog.GetWorkspaceBindingsResponse` dataclass.
* [Breaking] Changed `update()` method for [w.workspace_bindings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/workspace_bindings.html) workspace-level service to return `databricks.sdk.service.catalog.UpdateCatalogWorkspaceBindingsResponse` dataclass.
* [Breaking] Changed `update_bindings()` method for [w.workspace_bindings](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/workspace_bindings.html) workspace-level service to return `databricks.sdk.service.catalog.UpdateWorkspaceBindingsResponse` dataclass.
* [Breaking] Changed `securable_type` field for `databricks.sdk.service.catalog.CatalogInfo` to type `databricks.sdk.service.catalog.SecurableType` dataclass.
* [Breaking] Changed `securable_type` field for `databricks.sdk.service.catalog.GetBindingsRequest` to type `str` dataclass.
* Changed `schema` and `state` fields for `databricks.sdk.service.catalog.SystemSchemaInfo` to be required.
* [Breaking] Changed `state` field for `databricks.sdk.service.catalog.SystemSchemaInfo` to type `str` dataclass.
* [Breaking] Changed `securable_type` field for `databricks.sdk.service.catalog.UpdateWorkspaceBindingsParameters` to type `str` dataclass.
* [Breaking] Changed `workspace_id` field for `databricks.sdk.service.catalog.WorkspaceBinding` to be required.
* Changed `etag` and `name` fields for `databricks.sdk.service.iam.RuleSetResponse` to be required.
* Changed `gpu_node_pool_id` field for `databricks.sdk.service.jobs.ComputeConfig` to no longer be required.
* [Breaking] Changed `gpu_node_pool_id` field for `databricks.sdk.service.jobs.ComputeConfig` to no longer be required.
* [Breaking] Changed `alert` field for `databricks.sdk.service.sql.CreateAlertV2Request` to be required.
* [Breaking] Changed `alert` field for `databricks.sdk.service.sql.UpdateAlertV2Request` to be required.
* [Breaking] Removed `access_point` field for `databricks.sdk.service.catalog.CreateExternalLocation`.
* [Breaking] Removed `access_point` field for `databricks.sdk.service.catalog.ExternalLocationInfo`.
* [Breaking] Removed `access_point` field for `databricks.sdk.service.catalog.UpdateExternalLocation`.
* [Breaking] Removed `node_type_flexibility` field for `databricks.sdk.service.compute.EditInstancePool`.
* [Breaking] Removed `node_type_flexibility` field for `databricks.sdk.service.compute.GetInstancePool`.
* [Breaking] Removed `node_type_flexibility` field for `databricks.sdk.service.compute.InstancePoolAndStats`.
* [Breaking] Removed `catalog`, `credential`, `external_location` and `storage_credential` enum values for `databricks.sdk.service.catalog.GetBindingsSecurableType`.
* [Breaking] Removed `available`, `disable_initialized`, `enable_completed`, `enable_initialized` and `unavailable` enum values for `databricks.sdk.service.catalog.SystemSchemaInfoState`.
* [Breaking] Removed `catalog`, `credential`, `external_location` and `storage_credential` enum values for `databricks.sdk.service.catalog.UpdateBindingsSecurableType`.

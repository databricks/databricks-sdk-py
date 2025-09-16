# NEXT CHANGELOG

## Release v0.66.0

### New Features and Improvements

* Add a public helper function to build a `CredentialsProvider` directly from an `IdTokenSource`.

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Added `databricks.sdk.service.iamv2` package.
* Added [a.account_groups_v2](https://databricks-sdk-py.readthedocs.io/en/latest/account/iam/account_groups_v2.html) account-level service, [a.account_service_principals_v2](https://databricks-sdk-py.readthedocs.io/en/latest/account/iam/account_service_principals_v2.html) account-level service, [a.account_users_v2](https://databricks-sdk-py.readthedocs.io/en/latest/account/iam/account_users_v2.html) account-level service, [w.groups_v2](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/iam/groups_v2.html) workspace-level service, [w.service_principals_v2](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/iam/service_principals_v2.html) workspace-level service and [w.users_v2](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/iam/users_v2.html) workspace-level service.
* Added [a.account_iam_v2](https://databricks-sdk-py.readthedocs.io/en/latest/account/iamv2/account_iam_v2.html) account-level service and [w.workspace_iam_v2](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/iamv2/workspace_iam_v2.html) workspace-level service.
* Added [w.feature_engineering](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/feature_engineering.html) workspace-level service.
* Added `java_dependencies` field for `databricks.sdk.service.compute.Environment`.
* Added `followup_questions` field for `databricks.sdk.service.dashboards.GenieAttachment`.
* Added `feedback` field for `databricks.sdk.service.dashboards.GenieMessage`.
* Added `effective_capacity` field for `databricks.sdk.service.database.DatabaseInstance`.
* Added `disabled` field for `databricks.sdk.service.jobs.Task`.
* Added `netsuite_jar_path` field for `databricks.sdk.service.pipelines.IngestionPipelineDefinition`.
* Added `workday_report_parameters` field for `databricks.sdk.service.pipelines.TableSpecificConfig`.
* Added `auxiliary_managed_location` field for `databricks.sdk.service.sharing.TableInternalAttributes`.
* Added `alerts` field for `databricks.sdk.service.sql.ListAlertsV2Response`.
* Added `create_time` and `update_time` fields for `databricks.sdk.service.tags.TagPolicy`.
* Added `table_delta_uniform_iceberg_foreign_deltasharing` enum value for `databricks.sdk.service.catalog.SecurableKind`.
* Added `no_activated_k8s` and `usage_policy_entitlement_denied` enum values for `databricks.sdk.service.compute.TerminationReasonCode`.
* Added `internal_catalog_path_overlap_exception` and `internal_catalog_missing_uc_path_exception` enum values for `databricks.sdk.service.dashboards.MessageErrorType`.
* Added `foreign_catalog` enum value for `databricks.sdk.service.pipelines.IngestionSourceType`.
* Added `foreign_iceberg_table` enum value for `databricks.sdk.service.sharing.TableInternalAttributesSharedTableType`.
* [Breaking] Changed `creation_time` field for `databricks.sdk.service.agentbricks.CustomLlm` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.agentbricks.UpdateCustomLlmRequest` to type `str` dataclass.
* [Breaking] Changed `create_time` and `update_time` fields for `databricks.sdk.service.apps.App` to type `str` dataclass.
* [Breaking] Changed `create_time` and `update_time` fields for `databricks.sdk.service.apps.AppDeployment` to type `str` dataclass.
* [Breaking] Changed `timestamp` field for `databricks.sdk.service.catalog.ContinuousUpdateStatus` to type `str` dataclass.
* [Breaking] Changed `event_time` field for `databricks.sdk.service.catalog.ExternalLineageExternalMetadataInfo` to type `str` dataclass.
* [Breaking] Changed `event_time` field for `databricks.sdk.service.catalog.ExternalLineageFileInfo` to type `str` dataclass.
* [Breaking] Changed `event_time` field for `databricks.sdk.service.catalog.ExternalLineageModelVersionInfo` to type `str` dataclass.
* [Breaking] Changed `event_time` field for `databricks.sdk.service.catalog.ExternalLineageTableInfo` to type `str` dataclass.
* [Breaking] Changed `create_time` and `update_time` fields for `databricks.sdk.service.catalog.ExternalMetadata` to type `str` dataclass.
* [Breaking] Changed `timestamp` field for `databricks.sdk.service.catalog.FailedStatus` to type `str` dataclass.
* [Breaking] Changed `timestamp` field for `databricks.sdk.service.catalog.TriggeredUpdateStatus` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.catalog.UpdateAccessRequestDestinationsRequest` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.catalog.UpdateEntityTagAssignmentRequest` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.catalog.UpdateExternalLineageRelationshipRequest` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.catalog.UpdateExternalMetadataRequest` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.catalog.UpdatePolicyRequest` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.compute.UpdateCluster` to type `str` dataclass.
* [Breaking] Changed `create_time` and `update_time` fields for `databricks.sdk.service.dashboards.Dashboard` to type `str` dataclass.
* [Breaking] Changed `revision_create_time` field for `databricks.sdk.service.dashboards.PublishedDashboard` to type `str` dataclass.
* [Breaking] Changed `create_time` and `update_time` fields for `databricks.sdk.service.dashboards.Schedule` to type `str` dataclass.
* [Breaking] Changed `create_time` and `update_time` fields for `databricks.sdk.service.dashboards.Subscription` to type `str` dataclass.
* [Breaking] Changed `expiration_time` field for `databricks.sdk.service.database.DatabaseCredential` to type `str` dataclass.
* [Breaking] Changed `creation_time` field for `databricks.sdk.service.database.DatabaseInstance` to type `str` dataclass.
* [Breaking] Changed `branch_time` field for `databricks.sdk.service.database.DatabaseInstanceRef` to type `str` dataclass.
* [Breaking] Changed `delta_commit_timestamp` field for `databricks.sdk.service.database.DeltaTableSyncInfo` to type `str` dataclass.
* [Breaking] Changed `timestamp` field for `databricks.sdk.service.database.SyncedTableContinuousUpdateStatus` to type `str` dataclass.
* [Breaking] Changed `timestamp` field for `databricks.sdk.service.database.SyncedTableFailedStatus` to type `str` dataclass.
* [Breaking] Changed `sync_end_timestamp` and `sync_start_timestamp` fields for `databricks.sdk.service.database.SyncedTablePosition` to type `str` dataclass.
* [Breaking] Changed `timestamp` field for `databricks.sdk.service.database.SyncedTableTriggeredUpdateStatus` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.database.UpdateDatabaseCatalogRequest` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.database.UpdateDatabaseInstanceRequest` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.database.UpdateSyncedDatabaseTableRequest` to type `str` dataclass.
* [Breaking] Changed `creation_time` field for `databricks.sdk.service.ml.OnlineStore` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.ml.UpdateFeatureTagRequest` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.ml.UpdateOnlineStoreRequest` to type `str` dataclass.
* [Breaking] Changed `lifetime` field for `databricks.sdk.service.oauth2.CreateServicePrincipalSecretRequest` to type `str` dataclass.
* [Breaking] Changed `expire_time` field for `databricks.sdk.service.oauth2.CreateServicePrincipalSecretResponse` to type `str` dataclass.
* [Breaking] Changed `create_time` and `update_time` fields for `databricks.sdk.service.oauth2.FederationPolicy` to type `str` dataclass.
* [Breaking] Changed `expire_time` field for `databricks.sdk.service.oauth2.SecretInfo` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.oauth2.UpdateAccountFederationPolicyRequest` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.oauth2.UpdateServicePrincipalFederationPolicyRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateAccountIpAccessEnableRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateAibiDashboardEmbeddingAccessPolicySettingRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateAibiDashboardEmbeddingApprovedDomainsSettingRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateAutomaticClusterUpdateSettingRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateComplianceSecurityProfileSettingRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateCspEnablementAccountSettingRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateDashboardEmailSubscriptionsRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateDefaultNamespaceSettingRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateDefaultWarehouseIdRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateDisableLegacyAccessRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateDisableLegacyDbfsRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateDisableLegacyFeaturesRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateEnableExportNotebookRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateEnableNotebookTableClipboardRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateEnableResultsDownloadingRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateEnhancedSecurityMonitoringSettingRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateEsmEnablementAccountSettingRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateLlmProxyPartnerPoweredAccountRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateLlmProxyPartnerPoweredEnforceRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateLlmProxyPartnerPoweredWorkspaceRequest` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.settings.UpdateNccPrivateEndpointRuleRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdatePersonalComputeSettingRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateRestrictWorkspaceAdminsSettingRequest` to type `str` dataclass.
* [Breaking] Changed `field_mask` field for `databricks.sdk.service.settings.UpdateSqlResultsDownloadRequest` to type `str` dataclass.
* [Breaking] Changed `create_time` and `update_time` fields for `databricks.sdk.service.sharing.FederationPolicy` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.sharing.UpdateFederationPolicyRequest` to type `str` dataclass.
* [Breaking] Changed `create_time`, `trigger_time` and `update_time` fields for `databricks.sdk.service.sql.Alert` to type `str` dataclass.
* [Breaking] Changed `create_time` and `update_time` fields for `databricks.sdk.service.sql.AlertV2` to type `str` dataclass.
* [Breaking] Changed `last_evaluated_at` field for `databricks.sdk.service.sql.AlertV2Evaluation` to type `str` dataclass.
* [Breaking] Changed `create_time`, `trigger_time` and `update_time` fields for `databricks.sdk.service.sql.ListAlertsResponseAlert` to type `str` dataclass.
* [Breaking] Changed `create_time` and `update_time` fields for `databricks.sdk.service.sql.ListQueryObjectsResponseQuery` to type `str` dataclass.
* [Breaking] Changed `create_time` and `update_time` fields for `databricks.sdk.service.sql.Query` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.sql.UpdateAlertRequest` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.sql.UpdateAlertV2Request` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.sql.UpdateQueryRequest` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.sql.UpdateVisualizationRequest` to type `str` dataclass.
* [Breaking] Changed `create_time` and `update_time` fields for `databricks.sdk.service.sql.Visualization` to type `str` dataclass.
* [Breaking] Changed `update_mask` field for `databricks.sdk.service.tags.UpdateTagPolicyRequest` to type `str` dataclass.
* [Breaking] Removed `disabled` field for `databricks.sdk.service.jobs.RunTask`.
* [Breaking] Removed `default_data_security_mode` and `effective_default_data_security_mode` fields for `databricks.sdk.service.settingsv2.Setting`.

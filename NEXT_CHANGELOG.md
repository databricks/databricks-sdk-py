# NEXT CHANGELOG

## Release v0.66.0

### New Features and Improvements

* Add a public helper function to build a `CredentialsProvider` directly from an `IdTokenSource`.

* Add native support for authentication through Azure DevOps OIDC

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
* [Breaking] Removed `disabled` field for `databricks.sdk.service.jobs.RunTask`.
* [Breaking] Removed `default_data_security_mode` and `effective_default_data_security_mode` fields for `databricks.sdk.service.settingsv2.Setting`.
* Added `list_shares()` method for [w.shares](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sharing/shares.html) workspace-level service.
* Added `suggested_questions` field for `databricks.sdk.service.dashboards.GenieAttachment`.
* Added `warehouse_id` field for `databricks.sdk.service.dashboards.GenieSpace`.
* Added `palantir` enum value for `databricks.sdk.service.catalog.ConnectionType`.
* Added `table_metric_view_deltasharing` and `table_foreign_palantir` enum values for `databricks.sdk.service.catalog.SecurableKind`.
* Added `no_activated_k8s_testing_tag` enum value for `databricks.sdk.service.compute.TerminationReasonCode`.
* Added `metric_view` enum value for `databricks.sdk.service.sharing.TableInternalAttributesSharedTableType`.
* [Breaking] Removed `followup_questions` field for `databricks.sdk.service.dashboards.GenieAttachment`.
* [Breaking] Removed `comment` field for `databricks.sdk.service.dashboards.GenieFeedback`.
* [Breaking] Removed `comment` field for `databricks.sdk.service.dashboards.GenieSendMessageFeedbackRequest`.
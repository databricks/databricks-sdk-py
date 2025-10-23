# NEXT CHANGELOG

## Release v0.70.0

### New Features and Improvements

### Bug Fixes
- Improving the error message that is shown when the unsupported `dbutils.credentials.getServiceCredentialsProvider` method is used. This method can only be used inside of a notebook.

### Documentation

### Internal Changes

### API Changes
* Add `create_materialized_feature()`, `delete_materialized_feature()`, `get_materialized_feature()`, `list_materialized_features()` and `update_materialized_feature()` methods for [w.feature_engineering](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/feature_engineering.html) workspace-level service.
* Add `filter_condition` field for `databricks.sdk.service.ml.Feature`.
* Add `absolute_session_lifetime_in_minutes` and `enable_single_use_refresh_tokens` fields for `databricks.sdk.service.oauth2.TokenAccessPolicy`.
* Add `network_connectivity_config_id` field for `databricks.sdk.service.provisioning.CreateWorkspaceRequest`.
* Add `oauth_mtls` enum value for `databricks.sdk.service.catalog.CredentialType`.
* Add `network_check_nic_failure_due_to_misconfig`, `network_check_dns_server_failure_due_to_misconfig`, `network_check_storage_failure_due_to_misconfig`, `network_check_metadata_endpoint_failure_due_to_misconfig`, `network_check_control_plane_failure_due_to_misconfig` and `network_check_multiple_components_failure_due_to_misconfig` enum values for `databricks.sdk.service.compute.TerminationReasonCode`.
* Add `creating` and `create_failed` enum values for `databricks.sdk.service.settings.NccPrivateEndpointRulePrivateLinkConnectionState`.
* Add `network_check_nic_failure_due_to_misconfig`, `network_check_dns_server_failure_due_to_misconfig`, `network_check_storage_failure_due_to_misconfig`, `network_check_metadata_endpoint_failure_due_to_misconfig`, `network_check_control_plane_failure_due_to_misconfig` and `network_check_multiple_components_failure_due_to_misconfig` enum values for `databricks.sdk.service.sql.TerminationReasonCode`.
* [Breaking] Change `display_name`, `evaluation`, `query_text`, `schedule` and `warehouse_id` fields for `databricks.sdk.service.sql.AlertV2` to be required.
* Change `display_name`, `evaluation`, `query_text`, `schedule` and `warehouse_id` fields for `databricks.sdk.service.sql.AlertV2` to be required.
* Change `comparison_operator` and `source` fields for `databricks.sdk.service.sql.AlertV2Evaluation` to be required.
* [Breaking] Change `comparison_operator` and `source` fields for `databricks.sdk.service.sql.AlertV2Evaluation` to be required.
* Change `name` field for `databricks.sdk.service.sql.AlertV2OperandColumn` to be required.
* [Breaking] Change `name` field for `databricks.sdk.service.sql.AlertV2OperandColumn` to be required.
* [Breaking] Change `quartz_cron_schedule` and `timezone_id` fields for `databricks.sdk.service.sql.CronSchedule` to be required.
* Change `quartz_cron_schedule` and `timezone_id` fields for `databricks.sdk.service.sql.CronSchedule` to be required.
* [Breaking] Remove `update()` method for [w.recipient_federation_policies](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sharing/recipient_federation_policies.html) workspace-level service.
* [Breaking] Remove `results` field for `databricks.sdk.service.sql.ListAlertsV2Response`.
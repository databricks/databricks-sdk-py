# NEXT CHANGELOG

## Release v0.45.0

### New Features and Improvements
* Update Jobs service to use API 2.2 ([#913](https://github.com/databricks/databricks-sdk-py/pull/913)).

### Bug Fixes

### Documentation

### Internal Changes

* Refactor `DatabricksError` to expose different types of error details ([#912](https://github.com/databricks/databricks-sdk-py/pull/912)). 
* Update Jobs ListJobs API to support paginated responses ([#896](https://github.com/databricks/databricks-sdk-py/pull/896))
* Update Jobs ListRuns API to support paginated responses ([#890](https://github.com/databricks/databricks-sdk-py/pull/890))
* Introduce automated tagging ([#888](https://github.com/databricks/databricks-sdk-py/pull/888))
* Update Jobs GetJob API to support paginated responses ([#869](https://github.com/databricks/databricks-sdk-py/pull/869)).
* Update On Behalf Of User Authentication in Multithreaded applications ([#907](https://github.com/databricks/databricks-sdk-py/pull/907))

### API Changes
* Added `execute_message_attachment_query()`, `get_message_attachment_query_result()` and `get_space()` methods for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service.
* Added `list_provider_share_assets()` method for [w.providers](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sharing/providers.html) workspace-level service.
* Added `budget_policy_id` and `effective_budget_policy_id` fields for `databricks.sdk.service.apps.App`.
* Added `policy` field for `databricks.sdk.service.billing.CreateBudgetPolicyRequest`.
* Added `databricks_gcp_service_account` field for `databricks.sdk.service.catalog.ValidateCredentialRequest`.
* Added `attachment_id` field for `databricks.sdk.service.dashboards.GenieAttachment`.
* Added `conversation_id` field for `databricks.sdk.service.dashboards.GenieConversation`.
* Added `message_id` field for `databricks.sdk.service.dashboards.GenieMessage`.
* Added `description`, `id`, `last_updated_timestamp`, `query`, `query_result_metadata` and `title` fields for `databricks.sdk.service.dashboards.GenieQueryAttachment`.
* Added `gen_ai_compute_task` field for `databricks.sdk.service.jobs.RunTask`.
* Added `gen_ai_compute_task` field for `databricks.sdk.service.jobs.SubmitTask`.
* Added `gen_ai_compute_task` field for `databricks.sdk.service.jobs.Task`.
* Added `run_name` field for `databricks.sdk.service.ml.CreateRun`.
* Added `run_name` field for `databricks.sdk.service.ml.RunInfo`.
* Added `run_name` field for `databricks.sdk.service.ml.UpdateRun`.
* Added `lifetime` field for `databricks.sdk.service.oauth2.CreateServicePrincipalSecretRequest`.
* Added `expire_time` field for `databricks.sdk.service.oauth2.CreateServicePrincipalSecretResponse`.
* Added `jwks_uri` field for `databricks.sdk.service.oauth2.OidcFederationPolicy`.
* Added `expire_time` field for `databricks.sdk.service.oauth2.SecretInfo`.
* Added `instance_profile_arn` field for `databricks.sdk.service.serving.AmazonBedrockConfig`.
* Added `budget_policy_id` field for `databricks.sdk.service.serving.CreateServingEndpoint`.
* Added `budget_policy_id` field for `databricks.sdk.service.serving.ServingEndpoint`.
* Added `budget_policy_id` field for `databricks.sdk.service.serving.ServingEndpointDetailed`.
* Added `add`, `principal` and `remove` fields for `databricks.sdk.service.sharing.PermissionsChange`.
* Added `columns_to_rerank` field for `databricks.sdk.service.vectorsearch.QueryVectorIndexRequest`.
* Added `oracle` and `teradata` enum values for `databricks.sdk.service.catalog.ConnectionType`.
* Added `function_arguments_invalid_type_exception` and `message_cancelled_while_executing_exception` enum values for `databricks.sdk.service.dashboards.MessageErrorType`.
* Added `waiting` enum value for `databricks.sdk.service.jobs.RunLifecycleStateV2State`.
* Added `active_only`, `all` and `deleted_only` enum values for `databricks.sdk.service.ml.ViewType`.
* Added `oauth_client_credentials` enum value for `databricks.sdk.service.sharing.AuthenticationType`.
* Added `raw` enum value for `databricks.sdk.service.workspace.ExportFormat`.
* [Breaking] Changed `get_by_name()` method for [w.experiments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/experiments.html) workspace-level service to return `databricks.sdk.service.ml.GetExperimentByNameResponse` dataclass.
* [Breaking] Changed `log_inputs()` method for [w.experiments](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/ml/experiments.html) workspace-level service with new required argument order.
* [Breaking] Changed `share_permissions()` method for [w.shares](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sharing/shares.html) workspace-level service to return `databricks.sdk.service.sharing.GetSharePermissionsResponse` dataclass.
* [Breaking] Changed `share_permissions()` and `update_permissions()` methods for [w.shares](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sharing/shares.html) workspace-level service return type to become non-empty.
* [Breaking] Changed `update_permissions()` method for [w.shares](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sharing/shares.html) workspace-level service to return `databricks.sdk.service.sharing.UpdateSharePermissionsResponse` dataclass.
* [Breaking] Changed `policy_id` field for `databricks.sdk.service.billing.BudgetPolicy` to no longer be required.
* Changed `policy_id` field for `databricks.sdk.service.billing.BudgetPolicy` to no longer be required.
* [Breaking] Changed `partitions` field for `databricks.sdk.service.cleanrooms.CleanRoomAssetTableLocalDetails` to type `databricks.sdk.service.cleanrooms.PartitionList` dataclass.
* [Breaking] Changed `query` field for `databricks.sdk.service.dashboards.GenieAttachment` to type `databricks.sdk.service.dashboards.GenieQueryAttachment` dataclass.
* [Breaking] Changed `digest`, `name`, `source` and `source_type` fields for `databricks.sdk.service.ml.Dataset` to be required.
* Changed `digest`, `name`, `source` and `source_type` fields for `databricks.sdk.service.ml.Dataset` to be required.
* [Breaking] Changed `dataset` field for `databricks.sdk.service.ml.DatasetInput` to be required.
* Changed `dataset` field for `databricks.sdk.service.ml.DatasetInput` to be required.
* Changed `key` and `value` fields for `databricks.sdk.service.ml.InputTag` to be required.
* [Breaking] Changed `key` and `value` fields for `databricks.sdk.service.ml.InputTag` to be required.
* [Breaking] Changed `view_type` field for `databricks.sdk.service.ml.ListExperimentsRequest` to type `databricks.sdk.service.ml.ViewType` dataclass.
* [Breaking] Changed `run_id` field for `databricks.sdk.service.ml.LogInputs` to be required.
* [Breaking] Changed `view_type` field for `databricks.sdk.service.ml.SearchExperiments` to type `databricks.sdk.service.ml.ViewType` dataclass.
* [Breaking] Changed `run_view_type` field for `databricks.sdk.service.ml.SearchRuns` to type `databricks.sdk.service.ml.ViewType` dataclass.
* [Breaking] Removed `custom_tags` and `policy_name` fields for `databricks.sdk.service.billing.CreateBudgetPolicyRequest`.
* [Breaking] Removed `cached_query_schema`, `description`, `id`, `instruction_id`, `instruction_title`, `last_updated_timestamp`, `query`, `statement_id` and `title` fields for `databricks.sdk.service.dashboards.QueryAttachment`.
* [Breaking] Removed `max_results` and `page_token` fields for `databricks.sdk.service.sharing.UpdateSharePermissions`.
* [Breaking] Removed `active_only`, `all` and `deleted_only` enum values for `databricks.sdk.service.ml.SearchExperimentsViewType`.
* [Breaking] Removed `active_only`, `all` and `deleted_only` enum values for `databricks.sdk.service.ml.SearchRunsRunViewType`.

# Version changelog

## 0.3.0

* Fixed serialization of lists of enum values ([#248](https://github.com/databricks/databricks-sdk-py/pull/248)).
* Fixed examples that used incorrect keyword argument names. (https://github.com/databricks/databricks-sdk-go/pull/560)
* Handled nested query parameters in ApiClient.do() ([#249](https://github.com/databricks/databricks-sdk-py/pull/249)).
* Improved access of `__annotations__` ([#239](https://github.com/databricks/databricks-sdk-py/pull/239)).

API Changes:

 * Changed `create()` method for [a.account_metastore_assignments](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_metastore_assignments.html) account-level service to no longer return `databricks.sdk.service.catalog.CreateMetastoreAssignmentsResponseItemList` dataclass.
 * Added `connection_name` field for `databricks.sdk.service.catalog.CreateCatalog`.
 * Added `access_point` field for `databricks.sdk.service.catalog.CreateExternalLocation`.
 * Added `encryption_details` field for `databricks.sdk.service.catalog.CreateExternalLocation`.
 * Removed `databricks.sdk.service.catalog.CreateMetastoreAssignmentsResponseItem` dataclass.
 * Added `access_point` field for `databricks.sdk.service.catalog.ExternalLocationInfo`.
 * Added `encryption_details` field for `databricks.sdk.service.catalog.ExternalLocationInfo`.
 * Added `access_point` field for `databricks.sdk.service.catalog.TableInfo`.
 * Added `encryption_details` field for `databricks.sdk.service.catalog.TableInfo`.
 * Added `access_point` field for `databricks.sdk.service.catalog.UpdateExternalLocation`.
 * Added `encryption_details` field for `databricks.sdk.service.catalog.UpdateExternalLocation`.
 * Added `access_point` field for `databricks.sdk.service.catalog.VolumeInfo`.
 * Added `encryption_details` field for `databricks.sdk.service.catalog.VolumeInfo`.
 * Added `databricks.sdk.service.catalog.EncryptionDetails` dataclass.
 * Added `databricks.sdk.service.catalog.SseEncryptionDetails` dataclass.
 * Added `databricks.sdk.service.catalog.SseEncryptionDetailsAlgorithm` dataclass.
 * Added [a.account_network_policy](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_network_policy.html) account-level service.
 * Added `databricks.sdk.service.settings.AccountNetworkPolicyMessage` dataclass.
 * Added `databricks.sdk.service.settings.DeleteAccountNetworkPolicyRequest` dataclass.
 * Added `databricks.sdk.service.settings.DeleteAccountNetworkPolicyResponse` dataclass.
 * Added `databricks.sdk.service.settings.ReadAccountNetworkPolicyRequest` dataclass.
 * Added `databricks.sdk.service.settings.UpdateAccountNetworkPolicyRequest` dataclass.

OpenAPI SHA: a1b6c1ecfaab6635911d3c060a8dd797ac6b2d4d, Date: 2023-07-27

## 0.2.1

* Support older versions of `urllib3` and Databricks Runtime with regards to `DEFAULT_METHOD_WHITELIST` change to `DEFAULT_ALLOWED_METHODS` ([#240](https://github.com/databricks/databricks-sdk-py/pull/240)).


## 0.2.0

* Add Issue Templates ([#208](https://github.com/databricks/databricks-sdk-py/pull/208)).
* Fixed notebook native auth for jobs ([#209](https://github.com/databricks/databricks-sdk-py/pull/209)).
* Replace `datatime.timedelta()` with `datetime.timedelta()` in codebase ([#207](https://github.com/databricks/databricks-sdk-py/pull/207)).
* Support dod in python sdk ([#212](https://github.com/databricks/databricks-sdk-py/pull/212)).
* [DECO-1115] Add local implementation for `dbutils.widgets` ([#93](https://github.com/databricks/databricks-sdk-py/pull/93)).
* Fix error message, ExportFormat -> ImportFormat ([#220](https://github.com/databricks/databricks-sdk-py/pull/220)).
* Regenerate Python SDK using recent OpenAPI Specification ([#229](https://github.com/databricks/databricks-sdk-py/pull/229)).
* Make workspace client also return runtime dbutils when in dbr ([#210](https://github.com/databricks/databricks-sdk-py/pull/210)).
* Use .ConstantName defining target enum states for waiters ([#230](https://github.com/databricks/databricks-sdk-py/pull/230)).
* Fix enum deserialization ([#234](https://github.com/databricks/databricks-sdk-py/pull/234)).
* Fix enum deserialization, take 2 ([#235](https://github.com/databricks/databricks-sdk-py/pull/235)).
* Added toolchain configuration to `.codegen.json` ([#236](https://github.com/databricks/databricks-sdk-py/pull/236)).
* Make OpenAPI spec location configurable ([#237](https://github.com/databricks/databricks-sdk-py/pull/237)).
* Rearrange imports in `databricks.sdk.runtime` to improve local editor experience ([#219](https://github.com/databricks/databricks-sdk-py/pull/219)).
* Updated account-level and workspace-level user management examples ([#241](https://github.com/databricks/databricks-sdk-py/pull/241)).

API Changes:

 * Removed `maintenance()` method for [w.metastores](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/metastores.html) workspace-level service.
 * Added `enable_optimization()` method for [w.metastores](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/metastores.html) workspace-level service.
 * Added `update()` method for [w.tables](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/tables.html) workspace-level service.
 * Added `force` field for `databricks.sdk.service.catalog.DeleteAccountMetastoreRequest`.
 * Added `force` field for `databricks.sdk.service.catalog.DeleteAccountStorageCredentialRequest`.
 * Removed `databricks.sdk.service.catalog.UpdateAutoMaintenance` dataclass.
 * Removed `databricks.sdk.service.catalog.UpdateAutoMaintenanceResponse` dataclass.
 * Added `databricks.sdk.service.catalog.UpdatePredictiveOptimization` dataclass.
 * Added `databricks.sdk.service.catalog.UpdatePredictiveOptimizationResponse` dataclass.
 * Added `databricks.sdk.service.catalog.UpdateTableRequest` dataclass.
 * Added `schema` field for `databricks.sdk.service.iam.PartialUpdate`.
 * Added `databricks.sdk.service.iam.PatchSchema` dataclass.
 * Added `trigger_info` field for `databricks.sdk.service.jobs.BaseRun`.
 * Added `health` field for `databricks.sdk.service.jobs.CreateJob`.
 * Added `job_source` field for `databricks.sdk.service.jobs.GitSource`.
 * Added `on_duration_warning_threshold_exceeded` field for `databricks.sdk.service.jobs.JobEmailNotifications`.
 * Added `health` field for `databricks.sdk.service.jobs.JobSettings`.
 * Added `trigger_info` field for `databricks.sdk.service.jobs.Run`.
 * Added `run_job_output` field for `databricks.sdk.service.jobs.RunOutput`.
 * Added `run_job_task` field for `databricks.sdk.service.jobs.RunTask`.
 * Added `email_notifications` field for `databricks.sdk.service.jobs.SubmitRun`.
 * Added `health` field for `databricks.sdk.service.jobs.SubmitRun`.
 * Added `email_notifications` field for `databricks.sdk.service.jobs.SubmitTask`.
 * Added `health` field for `databricks.sdk.service.jobs.SubmitTask`.
 * Added `notification_settings` field for `databricks.sdk.service.jobs.SubmitTask`.
 * Added `health` field for `databricks.sdk.service.jobs.Task`.
 * Added `run_job_task` field for `databricks.sdk.service.jobs.Task`.
 * Added `on_duration_warning_threshold_exceeded` field for `databricks.sdk.service.jobs.TaskEmailNotifications`.
 * Added `on_duration_warning_threshold_exceeded` field for `databricks.sdk.service.jobs.WebhookNotifications`.
 * Added `databricks.sdk.service.jobs.JobSource` dataclass.
 * Added `databricks.sdk.service.jobs.JobSourceDirtyState` dataclass.
 * Added `databricks.sdk.service.jobs.JobsHealthMetric` dataclass.
 * Added `databricks.sdk.service.jobs.JobsHealthOperator` dataclass.
 * Added `databricks.sdk.service.jobs.JobsHealthRule` dataclass.
 * Added `databricks.sdk.service.jobs.JobsHealthRules` dataclass.
 * Added `databricks.sdk.service.jobs.RunJobOutput` dataclass.
 * Added `databricks.sdk.service.jobs.RunJobTask` dataclass.
 * Added `databricks.sdk.service.jobs.TriggerInfo` dataclass.
 * Added `databricks.sdk.service.jobs.WebhookNotificationsOnDurationWarningThresholdExceededItem` dataclass.
 * Removed `whl` field for `databricks.sdk.service.pipelines.PipelineLibrary`.
 * Changed `delete_personal_compute_setting()` method for [a.account_settings](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_settings.html) account-level service with new required argument order.
 * Changed `read_personal_compute_setting()` method for [a.account_settings](https://databricks-sdk-py.readthedocs.io/en/latest/account/account_settings.html) account-level service with new required argument order.
 * Changed `etag` field for `databricks.sdk.service.settings.DeletePersonalComputeSettingRequest` to be required.
 * Changed `etag` field for `databricks.sdk.service.settings.ReadPersonalComputeSettingRequest` to be required.
 * Added [w.clean_rooms](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/clean_rooms.html) workspace-level service.
 * Added `databricks.sdk.service.sharing.CentralCleanRoomInfo` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomAssetInfo` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomCatalog` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomCatalogUpdate` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomCollaboratorInfo` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomInfo` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomNotebookInfo` dataclass.
 * Added `databricks.sdk.service.sharing.CleanRoomTableInfo` dataclass.
 * Added `databricks.sdk.service.sharing.ColumnInfo` dataclass.
 * Added `databricks.sdk.service.sharing.ColumnMask` dataclass.
 * Added `databricks.sdk.service.sharing.ColumnTypeName` dataclass.
 * Added `databricks.sdk.service.sharing.CreateCleanRoom` dataclass.
 * Added `databricks.sdk.service.sharing.DeleteCleanRoomRequest` dataclass.
 * Added `databricks.sdk.service.sharing.GetCleanRoomRequest` dataclass.
 * Added `databricks.sdk.service.sharing.ListCleanRoomsResponse` dataclass.
 * Added `databricks.sdk.service.sharing.UpdateCleanRoom` dataclass.
 * Changed `query` field for `databricks.sdk.service.sql.Alert` to `databricks.sdk.service.sql.AlertQuery` dataclass.
 * Changed `value` field for `databricks.sdk.service.sql.AlertOptions` to `any` dataclass.
 * Removed `is_db_admin` field for `databricks.sdk.service.sql.User`.
 * Removed `profile_image_url` field for `databricks.sdk.service.sql.User`.
 * Added `databricks.sdk.service.sql.AlertQuery` dataclass.

OpenAPI SHA: 0a1949ba96f71680dad30e06973eaae85b1307bb, Date: 2023-07-18

## 0.1.12

* Beta release ([#198](https://github.com/databricks/databricks-sdk-py/pull/198)).
* Documentation improvements ([#197](https://github.com/databricks/databricks-sdk-py/pull/197)).
* Make `dbutils` type stubs consistent with runtime implementation ([#196](https://github.com/databricks/databricks-sdk-py/pull/196)).
* Regenerated from OpenAPI spec ([#199](https://github.com/databricks/databricks-sdk-py/pull/199)).

API changes:

* Renamed `compute.BaseClusterInfo` to `compute.ClusterSpec`
* Renamed `compute.ClusterInfo` to `compute.ClusterDetails`
* Renamed `jobs.JobTaskSettings` to `jobs.Task`
* Renamed `jobs.RunSubmitTaskSettings` to `jobs.SubmitTask`
* Renamed `jobs.JobWebhookNotifications` to `jobs.WebhookNotifications`
* Renamed `jobs.CreateJobFormat` to `jobs.Format`
* Renamed `jobs.GitSourceGitProvider` to `jobs.GitProvider`
* Renamed `jobs.FileArrivalTriggerSettings` to `jobs.FileArrivalTriggerConfiguration`

## 0.1.11

* Added Sphinx documentation ([#184](https://github.com/databricks/databricks-sdk-py/pull/184), [#191](https://github.com/databricks/databricks-sdk-py/pull/191), [#183](https://github.com/databricks/databricks-sdk-py/pull/183), [#193](https://github.com/databricks/databricks-sdk-py/pull/193)).
* Integrated with ReadTheDocs service ([#188](https://github.com/databricks/databricks-sdk-py/pull/188), [#189](https://github.com/databricks/databricks-sdk-py/pull/189), [#190](https://github.com/databricks/databricks-sdk-py/pull/190)).
* Create a deepcopy of config in api client ([#172](https://github.com/databricks/databricks-sdk-py/pull/172)).
* Fix client/secret auth ([#186](https://github.com/databricks/databricks-sdk-py/pull/186)).
* Increase DBFS copy buffer size ([#185](https://github.com/databricks/databricks-sdk-py/pull/185)).
* Move classes to other repository ([#192](https://github.com/databricks/databricks-sdk-py/pull/192)).
* Relax `requests` version upper bound to <3 ([#138](https://github.com/databricks/databricks-sdk-py/pull/138)).

## 0.1.10

* Regenerate from OpenAPI spec ([#176](https://github.com/databricks/databricks-sdk-py/pull/176)).
* Added improved notebook-native authentication ([#152](https://github.com/databricks/databricks-sdk-py/pull/152)).
* Added methods to provide extra user agent and upstream user agent to SDK config ([#163](https://github.com/databricks/databricks-sdk-py/pull/163)).
* Added more missing `Optional` type hints ([#171](https://github.com/databricks/databricks-sdk-py/pull/171), [#177](https://github.com/databricks/databricks-sdk-py/pull/177)).
* Correctly serialize external entities ([#178](https://github.com/databricks/databricks-sdk-py/pull/178)).
* Correctly serialize external enum values in paths ([#179](https://github.com/databricks/databricks-sdk-py/pull/179)).
* Mark non-required fields as `Optional` ([#170](https://github.com/databricks/databricks-sdk-py/pull/170)).
* Synchronize auth permutation tests with Go SDK ([#165](https://github.com/databricks/databricks-sdk-py/pull/165)).

## 0.1.9

* Added new services from OpenAPI spec ([#145](https://github.com/databricks/databricks-sdk-py/pull/145), [#159](https://github.com/databricks/databricks-sdk-py/pull/159)).
* Added consistent usage of the `upload(path, IO)` and `download(path) -> IO` across file-related operations ([#148](https://github.com/databricks/databricks-sdk-py/pull/148)).
* Added Databricks Metadata Service credential provider ([#139](https://github.com/databricks/databricks-sdk-py/pull/139), [#130](https://github.com/databricks/databricks-sdk-py/pull/130)).
* Added exposing runtime credential provider without changing user namespace ([#140](https://github.com/databricks/databricks-sdk-py/pull/140)).
* Added a check for `is not None` for primitive fields in `as_dict()` ([#147](https://github.com/databricks/databricks-sdk-py/pull/147)).
* Fixed bug related to boolean flags and convert `True` to `true` in query strings ([#156](https://github.com/databricks/databricks-sdk-py/pull/156)).
* Fixed generation of external entities ([#146](https://github.com/databricks/databricks-sdk-py/pull/146)).
* Make u2m authentication work with new CLI ([#150](https://github.com/databricks/databricks-sdk-py/pull/150)).

## 0.1.8

 * Regenerated from OpenAPI spec ([#124](https://github.com/databricks/databricks-sdk-py/pull/124)).
 * Added `codecov.io` badge ([#126](https://github.com/databricks/databricks-sdk-py/pull/126)).
 * Improved readme with links to examples ([#125](https://github.com/databricks/databricks-sdk-py/pull/125)).
 * Fixed `AttributeError: 'NoneType' object has no attribute 'debug_truncate_bytes' when instantiating an ApiClient` with empty config ([#123](https://github.com/databricks/databricks-sdk-py/pull/123)).

## 0.1.7

* Added an extensive set of examples ([#113](https://github.com/databricks/databricks-sdk-py/pull/113)).
* Fixed broken `dbutils.fs.mount` and `dbutils.fs.updateMount` ([#119](https://github.com/databricks/databricks-sdk-py/pull/119)).
* Ignore `.netrc` when sending unauthenticated requests for OAuth handshake ([#108](https://github.com/databricks/databricks-sdk-py/pull/108)).
* Make ApiClient more `pyodide` friendly ([#114](https://github.com/databricks/databricks-sdk-py/pull/114)).
* Persist token acquired through `external-browser` auth type ([#110](https://github.com/databricks/databricks-sdk-py/pull/110)).
* Prototype for notebook-native auth ([#115](https://github.com/databricks/databricks-sdk-py/pull/115)).
* Rename `RefreshableCredentials` to `SessionCredentials` ([#116](https://github.com/databricks/databricks-sdk-py/pull/116)).
* Use shell for opening `az` cli on Windows ([#117](https://github.com/databricks/databricks-sdk-py/pull/117)).

## 0.1.6

* Preserve original `databricks.sdk.runtime` for internal purposes ([#96](https://github.com/databricks/databricks-sdk-py/pull/96)).

## 0.1.5

* Pin version of `requests` to `>=2.28.1,<2.29.0`, so that we don't get `ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with LibreSSL 2.8.3`. See [this issue](https://github.com/psf/requests/issues/6432) for more information.

## 0.1.4

* Removed experimental redacting logger filter for `dbutils.secrets.get('scope', 'key')`, that was causing Jupyter Kernels to hang ([#92](https://github.com/databricks/databricks-sdk-py/pull/92)).
* Fixed error handling for SCIM and CommandExecution APIs ([#94](https://github.com/databricks/databricks-sdk-py/pull/94)).
* Created `dependabot.yml` ([#89](https://github.com/databricks/databricks-sdk-py/pull/89)).

## 0.1.3

* Added support for sdist ([#86](https://github.com/databricks/databricks-sdk-py/pull/86)).
* Removed redundant newlines from AAD OAuth responses ([#85](https://github.com/databricks/databricks-sdk-py/pull/85)).
* Update README.md with doc links ([#83](https://github.com/databricks/databricks-sdk-py/pull/83)).

## 0.1.2

* Fix `dbutils.fs.put()` utility ([#82](https://github.com/databricks/databricks-sdk-py/pull/82)).

## 0.1.1

* Improve Azure AD auth ([#80](https://github.com/databricks/databricks-sdk-py/pull/80)).

## 0.1.0

* Make code working with new OpenAPI packaging ([#78](https://github.com/databricks/databricks-sdk-py/pull/78)).
* Added `bricks` CLI authentication ([#66](https://github.com/databricks/databricks-sdk-py/pull/66)).
* Use `databricks.sdk.oauth` logger for single-request server ([#74](https://github.com/databricks/databricks-sdk-py/pull/74)).
* Support more Azure environments ([#73](https://github.com/databricks/databricks-sdk-py/pull/73)).
* Added SECURITY.md ([#64](https://github.com/databricks/databricks-sdk-py/pull/64)).

API changes:

* Moved `clusterpolicies` APIs to `compute` package.
* Moved `clusters` APIs to `compute` package.
* Moved `commands` APIs to `compute` package.
* Moved `globalinitscripts` APIs to `compute` package.
* Moved `instancepools` APIs to `compute` package.
* Moved `scim` APIs to `iam` package.
* Moved `permissions` APIs to `iam` package.
* Moved `ipaccesslists` APIs to `settings` package.
* Moved `tokenmanagement` APIs to `settings` package.
* Moved `tokens` APIs to `settings` package.
* Moved `workspaceconf` APIs to `settings` package.
* Moved `gitcredentials` APIs to `workspace` package.
* Moved `repos` APIs to `workspace` package.
* Moved `secrets` APIs to `workspace` package.
* Split `unitcatalog` package to `catalog` and `sharing`.
* Renamed `mlflow` package to `ml`.
* Renamed `dbfs` package to `files`.
* Renamed `deployment` package to `provisioning`.
* Renamed `endpoints` package to `serving`.
* Renamed `clusters.List` type to `compute.ListClustersRequest`.
* Renamed `jobs.ListRuns` type to `jobs.ListRunsRequest`.
* Renamed `jobs.ExportRun` type to `jobs.ExportRunRequest`.
* Renamed `clusterpolicies.List` type to `compute.ListClusterPoliciesRequest`.
* Renamed `jobs.List` type to `jobs.ListJobsRequest`.
* Renamed `permissions.GetPermissionLevels` type to `iam.GetPermissionLevelsRequest`.
* Renamed `pipelines.ListPipelineEvents` type to `pipelines.ListPipelineEventsRequest`.
* Renamed `pipelines.ListPipelines` type to `pipelines.ListPipelinesRequest`.
* Renamed `workspaceconf.GetStatus` type to `settings.GetStatusRequest`.
* Renamed `repos.List` type to `workspace.ListReposRequest`.
* Renamed `tokenmanagement.List` type to `settings.ListTokenManagementRequest`.
* Renamed `workspace.Export` type to `workspace.ExportRequest`.
* Renamed `workspace.List` type to `workspace.ListWorkspaceRequest`.

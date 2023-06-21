# Version changelog

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

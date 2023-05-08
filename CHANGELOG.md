# Version changelog

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

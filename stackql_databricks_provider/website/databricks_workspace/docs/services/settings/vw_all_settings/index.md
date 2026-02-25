---
title: vw_all_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_all_settings
  - settings
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>vw_all_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_all_settings" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settings.vw_all_settings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="property" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The name of the workspace setting (only non-null values are included).</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The value of the workspace setting (only non-null values are included).</td>
</tr>
</tbody>
</table>

## Required Parameters

The following parameters are required by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="deployment_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Workspace deployment name used to scope the query.</td>
</tr>
</tbody>
</table>

## `SELECT` Examples

```sql
SELECT
  property,
  value
FROM databricks_workspace.settings.vw_all_settings
WHERE deployment_name = '{{ deployment_name }}';
```

## SQL Definition

<Tabs
defaultValue="Sqlite3"
values={[
{ label: 'Sqlite3', value: 'Sqlite3' },
{ label: 'Postgres', value: 'Postgres' }
]}
>
<TabItem value="Sqlite3">

```sql
SELECT key, value
FROM (
  SELECT
    json_object(
    'enableWebTerminal', enableWebTerminal,
      'enableTokensConfig', enableTokensConfig,
      'maxTokenLifetimeDays', maxTokenLifetimeDays,
      'enableWorkspaceFilesystem', enableWorkspaceFilesystem,
      'enableExportNotebook', enableExportNotebook,
      'enableNotebookTableClipboard', enableNotebookTableClipboard,
      'enableResultsDownloading', enableResultsDownloading,
      'enableDcs', enableDcs,
      'enableGp3', enableGp3,
      'mlflowRunArtifactDownloadEnabled', mlflowRunArtifactDownloadEnabled,
      'enableUploadDataUis', enableUploadDataUis,
      'storeInteractiveNotebookResultsInCustomerAccount', storeInteractiveNotebookResultsInCustomerAccount,
      'enableDeprecatedGlobalInitScripts', enableDeprecatedGlobalInitScripts,
      'rStudioUserDefaultHomeBase', rStudioUserDefaultHomeBase,
      'enforceUserIsolation', enforceUserIsolation,
      'enableProjectsAllowList', enableProjectsAllowList,
      'projectsAllowListPermissions', projectsAllowListPermissions,
      'projectsAllowList', projectsAllowList,
      'reposIpynbResultsExportPermissions', reposIpynbResultsExportPermissions,
      'enableDbfsFileBrowser', enableDbfsFileBrowser,
      'enableDatabricksAutologgingAdminConf', enableDatabricksAutologgingAdminConf,
      'mlflowModelServingEndpointCreationEnabled', mlflowModelServingEndpointCreationEnabled,
      'enableVerboseAuditLogs', enableVerboseAuditLogs,
      'enableFileStoreEndpoint', enableFileStoreEndpoint,
      'loginLogo', loginLogo,
      'productName', productName,
      'homePageLogo', homePageLogo,
      'homePageLogoWidth', homePageLogoWidth,
      'homePageWelcomeMessage', homePageWelcomeMessage,
      'sidebarLogoText', sidebarLogoText,
      'sidebarLogoActive', sidebarLogoActive,
      'sidebarLogoInactive', sidebarLogoInactive,
      'customReferences', customReferences,
      'loginLogoWidth', loginLogoWidth,
      'enforceWorkspaceViewAcls', enforceWorkspaceViewAcls,
      'enforceClusterViewAcls', enforceClusterViewAcls,
      'enableJobViewAcls', enableJobViewAcls,
      'enableHlsRuntime', enableHlsRuntime,
      'enableEnforceImdsV2', enableEnforceImdsV2,
      'enableJobsEmailsV2', enableJobsEmailsV2,
      'enableProjectTypeInWorkspace', enableProjectTypeInWorkspace,
      'mlflowModelRegistryEmailNotificationsEnabled', mlflowModelRegistryEmailNotificationsEnabled,
      'heapAnalyticsAdminConsent', heapAnalyticsAdminConsent,
      'jobsListBackendPaginationEnabled', jobsListBackendPaginationEnabled,
      'jobsListBackendPaginationOptOut', jobsListBackendPaginationOptOut
    ) AS settings_object,
    json_each.key,
    json_each.value
  FROM databricks_workspace.settings.workspace_config c,
      json_each(settings_object)
  WHERE keys='enableWebTerminal,enableTokensConfig,maxTokenLifetimeDays,enableWorkspaceFilesystem,enableExportNotebook,enableNotebookTableClipboard,enableResultsDownloading,enableDcs,enableGp3,mlflowRunArtifactDownloadEnabled,enableUploadDataUis,storeInteractiveNotebookResultsInCustomerAccount,enableDeprecatedGlobalInitScripts,rStudioUserDefaultHomeBase,enforceUserIsolation,enableProjectsAllowList,projectsAllowListPermissions,projectsAllowList,reposIpynbResultsExportPermissions,enableDbfsFileBrowser,enableDatabricksAutologgingAdminConf,mlflowModelServingEndpointCreationEnabled,enableVerboseAuditLogs,enableFileStoreEndpoint,loginLogo,productName,homePageLogo,homePageLogoWidth,homePageWelcomeMessage,sidebarLogoText,sidebarLogoActive,sidebarLogoInactive,customReferences,loginLogoWidth,enforceWorkspaceViewAcls,enforceClusterViewAcls,enableJobViewAcls,enableHlsRuntime,enableEnforceImdsV2,enableJobsEmailsV2,enableProjectTypeInWorkspace,mlflowModelRegistryEmailNotificationsEnabled,heapAnalyticsAdminConsent,jobsListBackendPaginationEnabled,jobsListBackendPaginationOptOut'
    AND deployment_name='{{ deployment_name }}'
) t WHERE value IS NOT NULL;
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT key, value
FROM (
  SELECT
    (jsonb_build_object(
      'enableWebTerminal', enableWebTerminal,
      'enableTokensConfig', enableTokensConfig,
      'maxTokenLifetimeDays', maxTokenLifetimeDays,
      'enableWorkspaceFilesystem', enableWorkspaceFilesystem,
      'enableExportNotebook', enableExportNotebook,
      'enableNotebookTableClipboard', enableNotebookTableClipboard,
      'enableResultsDownloading', enableResultsDownloading,
      'enableDcs', enableDcs,
      'enableGp3', enableGp3,
      'mlflowRunArtifactDownloadEnabled', mlflowRunArtifactDownloadEnabled,
      'enableUploadDataUis', enableUploadDataUis,
      'storeInteractiveNotebookResultsInCustomerAccount', storeInteractiveNotebookResultsInCustomerAccount,
      'enableDeprecatedGlobalInitScripts', enableDeprecatedGlobalInitScripts,
      'rStudioUserDefaultHomeBase', rStudioUserDefaultHomeBase,
      'enforceUserIsolation', enforceUserIsolation,
      'enableProjectsAllowList', enableProjectsAllowList,
      'projectsAllowListPermissions', projectsAllowListPermissions,
      'projectsAllowList', projectsAllowList,
      'reposIpynbResultsExportPermissions', reposIpynbResultsExportPermissions,
      'enableDbfsFileBrowser', enableDbfsFileBrowser,
      'enableDatabricksAutologgingAdminConf', enableDatabricksAutologgingAdminConf,
      'mlflowModelServingEndpointCreationEnabled', mlflowModelServingEndpointCreationEnabled,
      'enableVerboseAuditLogs', enableVerboseAuditLogs,
      'enableFileStoreEndpoint', enableFileStoreEndpoint,
      'loginLogo', loginLogo,
      'productName', productName,
      'homePageLogo', homePageLogo,
      'homePageLogoWidth', homePageLogoWidth,
      'homePageWelcomeMessage', homePageWelcomeMessage,
      'sidebarLogoText', sidebarLogoText,
      'sidebarLogoActive', sidebarLogoActive,
      'sidebarLogoInactive', sidebarLogoInactive,
      'customReferences', customReferences,
      'loginLogoWidth', loginLogoWidth,
      'enforceWorkspaceViewAcls', enforceWorkspaceViewAcls,
      'enforceClusterViewAcls', enforceClusterViewAcls,
      'enableJobViewAcls', enableJobViewAcls,
      'enableHlsRuntime', enableHlsRuntime,
      'enableEnforceImdsV2', enableEnforceImdsV2,
      'enableJobsEmailsV2', enableJobsEmailsV2,
      'enableProjectTypeInWorkspace', enableProjectTypeInWorkspace,
      'mlflowModelRegistryEmailNotificationsEnabled', mlflowModelRegistryEmailNotificationsEnabled,
      'heapAnalyticsAdminConsent', heapAnalyticsAdminConsent,
      'jobsListBackendPaginationEnabled', jobsListBackendPaginationEnabled,
      'jobsListBackendPaginationOptOut', jobsListBackendPaginationOptOut
    )) AS settings_object
  FROM databricks_workspace.settings.workspace_config c
  WHERE keys='enableWebTerminal,enableTokensConfig,maxTokenLifetimeDays,enableWorkspaceFilesystem,enableExportNotebook,enableNotebookTableClipboard,enableResultsDownloading,enableDcs,enableGp3,mlflowRunArtifactDownloadEnabled,enableUploadDataUis,storeInteractiveNotebookResultsInCustomerAccount,enableDeprecatedGlobalInitScripts,rStudioUserDefaultHomeBase,enforceUserIsolation,enableProjectsAllowList,projectsAllowListPermissions,projectsAllowList,reposIpynbResultsExportPermissions,enableDbfsFileBrowser,enableDatabricksAutologgingAdminConf,mlflowModelServingEndpointCreationEnabled,enableVerboseAuditLogs,enableFileStoreEndpoint,loginLogo,productName,homePageLogo,homePageLogoWidth,homePageWelcomeMessage,sidebarLogoText,sidebarLogoActive,sidebarLogoInactive,customReferences,loginLogoWidth,enforceWorkspaceViewAcls,enforceClusterViewAcls,enableJobViewAcls,enableHlsRuntime,enableEnforceImdsV2,enableJobsEmailsV2,enableProjectTypeInWorkspace,mlflowModelRegistryEmailNotificationsEnabled,heapAnalyticsAdminConsent,jobsListBackendPaginationEnabled,jobsListBackendPaginationOptOut'
    AND deployment_name='{{ deployment_name }}'
) t, LATERAL jsonb_each_text(t.settings_object)
WHERE value IS NOT NULL;
```

</TabItem>
</Tabs>

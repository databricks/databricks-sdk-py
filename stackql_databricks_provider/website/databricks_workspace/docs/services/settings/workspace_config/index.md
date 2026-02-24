---
title: workspace_config
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_config
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>workspace_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_config" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settings.workspace_config" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_workspace_config"
    values={[
        { label: 'get_workspace_config', value: 'get_workspace_config' }
    ]}
>
<TabItem value="get_workspace_config">

<SchemaTable fields={[
  {
    "name": "customReferences",
    "type": "string",
    "description": "Custom reference links displayed in the workspace help menu"
  },
  {
    "name": "enable-X-Frame-Options",
    "type": "string",
    "description": "Controls the X-Frame-Options HTTP header to prevent clickjacking by restricting iframe embedding"
  },
  {
    "name": "enableClusterAclsConfig",
    "type": "string",
    "description": "Enables cluster-level access control lists (ACLs) for managing cluster permissions"
  },
  {
    "name": "enableDatabricksAutologgingAdminConf",
    "type": "string",
    "description": "Enables or disables Databricks Autologging for MLflow experiments at the workspace level"
  },
  {
    "name": "enableDbfsFileBrowser",
    "type": "string",
    "description": "Enables the DBFS visual file browser in the workspace UI"
  },
  {
    "name": "enableDcs",
    "type": "string",
    "description": "Enables Delta Cache Service for accelerated data reads from cloud storage"
  },
  {
    "name": "enableDeprecatedGlobalInitScripts",
    "type": "string",
    "description": "Enables legacy global init scripts (deprecated in favor of the Global Init Scripts API)"
  },
  {
    "name": "enableEnforceImdsV2",
    "type": "string",
    "description": "Enforces IMDSv2 (Instance Metadata Service v2) on cluster nodes for improved security (AWS only)"
  },
  {
    "name": "enableExportNotebook",
    "type": "string",
    "description": "Controls whether users can export notebooks from the workspace"
  },
  {
    "name": "enableFileStoreEndpoint",
    "type": "string",
    "description": "Enables the /FileStore endpoint for accessing files uploaded to DBFS FileStore"
  },
  {
    "name": "enableGp3",
    "type": "string",
    "description": "Enables GP3 EBS volumes for cluster nodes instead of GP2 (AWS only)"
  },
  {
    "name": "enableHlsRuntime",
    "type": "string",
    "description": "Enables the Databricks Runtime for Health and Life Sciences (genomics and biomedical workloads)"
  },
  {
    "name": "enableIpAccessLists",
    "type": "string",
    "description": "Enables IP access list functionality to restrict workspace access by IP address (Premium tier required)"
  },
  {
    "name": "enableJobAclsConfig",
    "type": "string",
    "description": "Enables job-level access control lists (ACLs) for managing job permissions"
  },
  {
    "name": "enableJobsEmailsV2",
    "type": "string",
    "description": "Enables the updated email notification system for job run results"
  },
  {
    "name": "enableJobViewAcls",
    "type": "string",
    "description": "Enables view-level ACLs on jobs, restricting visibility of jobs to permitted users"
  },
  {
    "name": "enableNotebookTableClipboard",
    "type": "string",
    "description": "Controls whether users can copy table data from notebook output to the clipboard"
  },
  {
    "name": "enableProjectsAllowList",
    "type": "string",
    "description": "Enables the projects allow list to restrict which Git repositories can be used"
  },
  {
    "name": "enableProjectTypeInWorkspace",
    "type": "string",
    "description": "Enables project-type resources within the workspace"
  },
  {
    "name": "enableResultsDownloading",
    "type": "string",
    "description": "Controls whether users can download query and notebook results"
  },
  {
    "name": "enableTokensConfig",
    "type": "string",
    "description": "Enables or disables personal access token creation and management for the workspace"
  },
  {
    "name": "enableUploadDataUis",
    "type": "string",
    "description": "Enables the data upload UI for importing files into the workspace"
  },
  {
    "name": "enableVerboseAuditLogs",
    "type": "string",
    "description": "Enables verbose audit logging with additional event details including notebook command results"
  },
  {
    "name": "enableWebTerminal",
    "type": "string",
    "description": "Enables web-based terminal access to cluster driver nodes from the workspace UI"
  },
  {
    "name": "enableWorkspaceAclsConfig",
    "type": "string",
    "description": "Enables workspace-level access control lists (ACLs) for managing workspace object permissions"
  },
  {
    "name": "enableWorkspaceFilesystem",
    "type": "string",
    "description": "Enables the workspace filesystem for storing and accessing workspace files"
  },
  {
    "name": "enforceClusterViewAcls",
    "type": "string",
    "description": "Enforces view-level ACLs on clusters, restricting cluster visibility to permitted users"
  },
  {
    "name": "enforceUserIsolation",
    "type": "string",
    "description": "Enforces user isolation on clusters to prevent users from accessing each others data"
  },
  {
    "name": "enforceWorkspaceViewAcls",
    "type": "string",
    "description": "Enforces view-level ACLs on workspace objects, restricting visibility to permitted users"
  },
  {
    "name": "heapAnalyticsAdminConsent",
    "type": "string",
    "description": "Controls admin consent for Heap Analytics usage tracking in the workspace"
  },
  {
    "name": "homePageLogo",
    "type": "string",
    "description": "Custom logo image URL displayed on the workspace home page"
  },
  {
    "name": "homePageLogoWidth",
    "type": "string",
    "description": "Width in pixels of the custom home page logo"
  },
  {
    "name": "homePageWelcomeMessage",
    "type": "string",
    "description": "Custom welcome message displayed on the workspace home page"
  },
  {
    "name": "jobsListBackendPaginationEnabled",
    "type": "string",
    "description": "Enables backend pagination for the jobs list API for improved performance with large job counts"
  },
  {
    "name": "jobsListBackendPaginationOptOut",
    "type": "string",
    "description": "Opts out of backend pagination for the jobs list if enabled at the workspace level"
  },
  {
    "name": "loginLogo",
    "type": "string",
    "description": "Custom logo image URL displayed on the workspace login page"
  },
  {
    "name": "loginLogoWidth",
    "type": "string",
    "description": "Width in pixels of the custom login page logo"
  },
  {
    "name": "maxTokenLifetimeDays",
    "type": "string",
    "description": "Maximum lifetime in days for newly created personal access tokens (empty or 0 means no limit)"
  },
  {
    "name": "mlflowModelRegistryEmailNotificationsEnabled",
    "type": "string",
    "description": "Enables email notifications for MLflow Model Registry events such as model version transitions"
  },
  {
    "name": "mlflowModelServingEndpointCreationEnabled",
    "type": "string",
    "description": "Enables creation of MLflow model serving endpoints in the workspace"
  },
  {
    "name": "mlflowRunArtifactDownloadEnabled",
    "type": "string",
    "description": "Controls whether users can download artifacts from MLflow experiment runs"
  },
  {
    "name": "productName",
    "type": "string",
    "description": "Custom product name displayed in the workspace UI (white-labeling)"
  },
  {
    "name": "projectsAllowList",
    "type": "string",
    "description": "Comma-separated list of allowed Git repository URL prefixes for workspace projects"
  },
  {
    "name": "projectsAllowListPermissions",
    "type": "string",
    "description": "Permissions configuration for who can manage the projects allow list"
  },
  {
    "name": "reposIpynbResultsExportPermissions",
    "type": "string",
    "description": "Controls permissions for exporting ipynb notebook results from Git-backed repos"
  },
  {
    "name": "rStudioUserDefaultHomeBase",
    "type": "string",
    "description": "Default home directory base path for RStudio users in the workspace"
  },
  {
    "name": "sidebarLogoActive",
    "type": "string",
    "description": "Custom logo image URL for the active state of the workspace sidebar"
  },
  {
    "name": "sidebarLogoInactive",
    "type": "string",
    "description": "Custom logo image URL for the inactive state of the workspace sidebar"
  },
  {
    "name": "sidebarLogoText",
    "type": "string",
    "description": "Custom text displayed alongside the sidebar logo (white-labeling)"
  },
  {
    "name": "storeInteractiveNotebookResultsInCustomerAccount",
    "type": "string",
    "description": "Stores all interactive notebook results in the customer cloud account instead of the Databricks control plane"
  }
]} />
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#get_workspace_config"><CopyableCode code="get_workspace_config" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-keys"><code>keys</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets the configuration status for a workspace.</td>
</tr>
<tr>
    <td><a href="#set_workspace_config"><CopyableCode code="set_workspace_config" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-contents"><code>contents</code></a></td>
    <td></td>
    <td>Sets the configuration status for a workspace, including enabling or disabling it.</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-keys">
    <td><CopyableCode code="keys" /></td>
    <td><code>string</code></td>
    <td>:returns: Dict[str,str]</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_workspace_config"
    values={[
        { label: 'get_workspace_config', value: 'get_workspace_config' }
    ]}
>
<TabItem value="get_workspace_config">

Gets the configuration status for a workspace.

```sql
SELECT
customReferences,
enable-X-Frame-Options,
enableClusterAclsConfig,
enableDatabricksAutologgingAdminConf,
enableDbfsFileBrowser,
enableDcs,
enableDeprecatedGlobalInitScripts,
enableEnforceImdsV2,
enableExportNotebook,
enableFileStoreEndpoint,
enableGp3,
enableHlsRuntime,
enableIpAccessLists,
enableJobAclsConfig,
enableJobViewAcls,
enableJobsEmailsV2,
enableNotebookTableClipboard,
enableProjectTypeInWorkspace,
enableProjectsAllowList,
enableResultsDownloading,
enableTokensConfig,
enableUploadDataUis,
enableVerboseAuditLogs,
enableWebTerminal,
enableWorkspaceAclsConfig,
enableWorkspaceFilesystem,
enforceClusterViewAcls,
enforceUserIsolation,
enforceWorkspaceViewAcls,
heapAnalyticsAdminConsent,
homePageLogo,
homePageLogoWidth,
homePageWelcomeMessage,
jobsListBackendPaginationEnabled,
jobsListBackendPaginationOptOut,
loginLogo,
loginLogoWidth,
maxTokenLifetimeDays,
mlflowModelRegistryEmailNotificationsEnabled,
mlflowModelServingEndpointCreationEnabled,
mlflowRunArtifactDownloadEnabled,
productName,
projectsAllowList,
projectsAllowListPermissions,
rStudioUserDefaultHomeBase,
reposIpynbResultsExportPermissions,
sidebarLogoActive,
sidebarLogoInactive,
sidebarLogoText,
storeInteractiveNotebookResultsInCustomerAccount
FROM databricks_workspace.settings.workspace_config
WHERE keys = '{{ keys }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="set_workspace_config"
    values={[
        { label: 'set_workspace_config', value: 'set_workspace_config' }
    ]}
>
<TabItem value="set_workspace_config">

Sets the configuration status for a workspace, including enabling or disabling it.

```sql
UPDATE databricks_workspace.settings.workspace_config
SET 
contents = '{{ contents }}'
WHERE 
workspace = '{{ workspace }}' --required
AND contents = '{{ contents }}' --required;
```
</TabItem>
</Tabs>

---
title: vw_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_apps
  - apps
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

Creates, updates, deletes, gets or lists a <code>vw_apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_apps" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.apps.vw_apps" /></td></tr>
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
    <td><CopyableCode code="deployment_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Workspace deployment name used to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique name of the Databricks app within the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the app.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Optional description of the app.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><CopyableCode code="string" /></td>
    <td>URL at which the app is accessible.</td>
</tr>
<tr>
    <td><CopyableCode code="creator" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Username of the user who created the app.</td>
</tr>
<tr>
    <td><CopyableCode code="create_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the app was created (ISO 8601).</td>
</tr>
<tr>
    <td><CopyableCode code="updater" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Username of the user who last updated the app.</td>
</tr>
<tr>
    <td><CopyableCode code="update_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the app was last updated (ISO 8601).</td>
</tr>
<tr>
    <td><CopyableCode code="compute_size" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Compute size tier for the app (e.g. SMALL, MEDIUM, LARGE).</td>
</tr>
<tr>
    <td><CopyableCode code="budget_policy_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the budget policy explicitly assigned to this app.</td>
</tr>
<tr>
    <td><CopyableCode code="effective_budget_policy_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the budget policy in effect for this app (may be inherited).</td>
</tr>
<tr>
    <td><CopyableCode code="service_principal_id" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>ID of the service principal used by this app.</td>
</tr>
<tr>
    <td><CopyableCode code="service_principal_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Display name of the service principal used by this app.</td>
</tr>
<tr>
    <td><CopyableCode code="service_principal_client_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>OAuth client ID of the service principal used by this app.</td>
</tr>
<tr>
    <td><CopyableCode code="default_source_code_path" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Default workspace path to the app source code.</td>
</tr>
<tr>
    <td><CopyableCode code="app_state" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Current lifecycle state of the app (e.g. RUNNING, STOPPED, ERROR).</td>
</tr>
<tr>
    <td><CopyableCode code="app_status_message" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable message describing the current app state.</td>
</tr>
<tr>
    <td><CopyableCode code="compute_state" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Current state of the app compute resources (e.g. ACTIVE, STOPPING, ERROR).</td>
</tr>
<tr>
    <td><CopyableCode code="compute_status_message" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable message describing the current compute state.</td>
</tr>
<tr>
    <td><CopyableCode code="compute_active_instances" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Number of active compute instances currently running for the app.</td>
</tr>
<tr>
    <td><CopyableCode code="git_repo_url" /></td>
    <td><CopyableCode code="string" /></td>
    <td>URL of the linked Git repository (if configured).</td>
</tr>
<tr>
    <td><CopyableCode code="git_repo_provider" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Git provider for the linked repository (e.g. github, gitLab, azureDevOpsServices).</td>
</tr>
<tr>
    <td><CopyableCode code="active_deployment_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Deployment ID of the currently active deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="active_deployment_source_path" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Workspace source code path used by the active deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="active_deployment_mode" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Deployment mode of the active deployment (e.g. SNAPSHOT, AUTO_SYNC).</td>
</tr>
<tr>
    <td><CopyableCode code="active_deployment_state" /></td>
    <td><CopyableCode code="string" /></td>
    <td>State of the active deployment (e.g. SUCCEEDED, IN_PROGRESS, FAILED).</td>
</tr>
<tr>
    <td><CopyableCode code="active_deployment_message" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable status message for the active deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="active_deployment_creator" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Username of the user who created the active deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="active_deployment_create_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the active deployment was created (ISO 8601).</td>
</tr>
<tr>
    <td><CopyableCode code="pending_deployment_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Deployment ID of the pending deployment, if one is in progress.</td>
</tr>
<tr>
    <td><CopyableCode code="pending_deployment_state" /></td>
    <td><CopyableCode code="string" /></td>
    <td>State of the pending deployment (e.g. IN_PROGRESS, FAILED).</td>
</tr>
<tr>
    <td><CopyableCode code="pending_deployment_message" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable status message for the pending deployment.</td>
</tr>
</tbody>
</table>

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
SELECT
  a.deployment_name,
  a.name,
  a.id,
  a.description,
  a.url,
  a.creator,
  a.create_time,
  a.updater,
  a.update_time,
  a.compute_size,
  a.budget_policy_id,
  a.effective_budget_policy_id,
  a.service_principal_id,
  a.service_principal_name,
  a.service_principal_client_id,
  a.default_source_code_path,
  JSON_EXTRACT(a.app_status, '$.state') AS app_state,
  JSON_EXTRACT(a.app_status, '$.message') AS app_status_message,
  JSON_EXTRACT(a.compute_status, '$.state') AS compute_state,
  JSON_EXTRACT(a.compute_status, '$.message') AS compute_status_message,
  JSON_EXTRACT(a.compute_status, '$.active_instances') AS compute_active_instances,
  JSON_EXTRACT(a.git_repository, '$.url') AS git_repo_url,
  JSON_EXTRACT(a.git_repository, '$.provider') AS git_repo_provider,
  JSON_EXTRACT(a.active_deployment, '$.deployment_id') AS active_deployment_id,
  JSON_EXTRACT(a.active_deployment, '$.source_code_path') AS active_deployment_source_path,
  JSON_EXTRACT(a.active_deployment, '$.mode') AS active_deployment_mode,
  JSON_EXTRACT(a.active_deployment, '$.status.state') AS active_deployment_state,
  JSON_EXTRACT(a.active_deployment, '$.status.message') AS active_deployment_message,
  JSON_EXTRACT(a.active_deployment, '$.creator') AS active_deployment_creator,
  JSON_EXTRACT(a.active_deployment, '$.create_time') AS active_deployment_create_time,
  JSON_EXTRACT(a.pending_deployment, '$.deployment_id') AS pending_deployment_id,
  JSON_EXTRACT(a.pending_deployment, '$.status.state') AS pending_deployment_state,
  JSON_EXTRACT(a.pending_deployment, '$.status.message') AS pending_deployment_message
FROM databricks_workspace.apps.apps a
WHERE deployment_name = '{{ deployment_name }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  a.deployment_name,
  a.name,
  a.id,
  a.description,
  a.url,
  a.creator,
  a.create_time,
  a.updater,
  a.update_time,
  a.compute_size,
  a.budget_policy_id,
  a.effective_budget_policy_id,
  a.service_principal_id,
  a.service_principal_name,
  a.service_principal_client_id,
  a.default_source_code_path,
  a.app_status->>'state' AS app_state,
  a.app_status->>'message' AS app_status_message,
  a.compute_status->>'state' AS compute_state,
  a.compute_status->>'message' AS compute_status_message,
  (a.compute_status->>'active_instances')::integer AS compute_active_instances,
  a.git_repository->>'url' AS git_repo_url,
  a.git_repository->>'provider' AS git_repo_provider,
  a.active_deployment->>'deployment_id' AS active_deployment_id,
  a.active_deployment->>'source_code_path' AS active_deployment_source_path,
  a.active_deployment->>'mode' AS active_deployment_mode,
  a.active_deployment->'status'->>'state' AS active_deployment_state,
  a.active_deployment->'status'->>'message' AS active_deployment_message,
  a.active_deployment->>'creator' AS active_deployment_creator,
  a.active_deployment->>'create_time' AS active_deployment_create_time,
  a.pending_deployment->>'deployment_id' AS pending_deployment_id,
  a.pending_deployment->'status'->>'state' AS pending_deployment_state,
  a.pending_deployment->'status'->>'message' AS pending_deployment_message
FROM databricks_workspace.apps.apps a
WHERE deployment_name = '{{ deployment_name }}'
```

</TabItem>
</Tabs>

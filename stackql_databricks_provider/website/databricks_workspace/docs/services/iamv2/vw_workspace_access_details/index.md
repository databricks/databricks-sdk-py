---
title: vw_workspace_access_details
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_workspace_access_details
  - iamv2
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

Creates, updates, deletes, gets or lists a <code>vw_workspace_access_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_workspace_access_details" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iamv2.vw_workspace_access_details" /></td></tr>
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
    <td><CopyableCode code="principal_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier of the principal whose workspace access is being queried.</td>
</tr>
<tr>
    <td><CopyableCode code="principal_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Type of the principal (e.g. USER, GROUP, SERVICE_PRINCIPAL).</td>
</tr>
<tr>
    <td><CopyableCode code="access_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>How the principal was granted access to the workspace (e.g. DIRECT, ACCOUNT_ADMIN).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Current access status of the principal on the workspace (e.g. ACTIVE).</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Databricks account ID that owns the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="workspace_id" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Numeric identifier of the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="permission" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Permission level granted to the principal on the workspace (one row per permission, e.g. USER, ADMIN).</td>
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
<tr>
    <td><CopyableCode code="principal_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier of the principal whose workspace access is being queried.</td>
</tr>
</tbody>
</table>

## `SELECT` Examples

```sql
SELECT
  deployment_name,
  principal_id,
  principal_type,
  access_type,
  status,
  account_id,
  workspace_id,
  permission
FROM databricks_workspace.iamv2.vw_workspace_access_details
WHERE deployment_name = '{{ deployment_name }}'
  AND principal_id = '{{ principal_id }}';
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
SELECT
  wa.deployment_name,
  wa.principal_id,
  wa.principal_type,
  wa.access_type,
  wa.status,
  wa.account_id,
  wa.workspace_id,
  p.value AS permission
FROM databricks_workspace.iamv2.workspace_iam_v2 wa,
     JSON_EACH(wa.permissions) p
WHERE wa.deployment_name = '{{ deployment_name }}'
AND wa.principal_id = '{{ principal_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  wa.deployment_name,
  wa.principal_id,
  wa.principal_type,
  wa.access_type,
  wa.status,
  wa.account_id,
  wa.workspace_id,
  p.value AS permission
FROM databricks_workspace.iamv2.workspace_iam_v2 wa,
     jsonb_array_elements(wa.permissions::jsonb) AS p
WHERE wa.deployment_name = '{{ deployment_name }}'
AND wa.principal_id = '{{ principal_id }}'
```

</TabItem>
</Tabs>

---
title: object_permission_levels
hide_title: false
hide_table_of_contents: false
keywords:
  - object_permission_levels
  - workspace
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

Creates, updates, deletes, gets or lists an <code>object_permission_levels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>object_permission_levels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.object_permission_levels" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "permission_levels",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "description",
        "type": "string",
        "description": ""
      },
      {
        "name": "permission_level",
        "type": "string",
        "description": "Permission level"
      }
    ]
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace_object_type"><code>workspace_object_type</code></a>, <a href="#parameter-workspace_object_id"><code>workspace_object_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the permission levels that a user can have on an object.<br /><br />:param workspace_object_type: str<br />  The workspace object type for which to get or manage permissions. Could be one of the following:<br />  alerts, alertsv2, dashboards, dbsql-dashboards, directories, experiments, files, genie, notebooks,<br />  queries<br />:param workspace_object_id: str<br />  The workspace object for which to get or manage permissions.<br /><br />:returns: :class:`GetWorkspaceObjectPermissionLevelsResponse`</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-workspace_object_id">
    <td><CopyableCode code="workspace_object_id" /></td>
    <td><code>string</code></td>
    <td>The workspace object for which to get or manage permissions.</td>
</tr>
<tr id="parameter-workspace_object_type">
    <td><CopyableCode code="workspace_object_type" /></td>
    <td><code>string</code></td>
    <td>The workspace object type for which to get or manage permissions. Could be one of the following: alerts, alertsv2, dashboards, dbsql-dashboards, directories, experiments, files, genie, notebooks, queries</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the permission levels that a user can have on an object.<br /><br />:param workspace_object_type: str<br />  The workspace object type for which to get or manage permissions. Could be one of the following:<br />  alerts, alertsv2, dashboards, dbsql-dashboards, directories, experiments, files, genie, notebooks,<br />  queries<br />:param workspace_object_id: str<br />  The workspace object for which to get or manage permissions.<br /><br />:returns: :class:`GetWorkspaceObjectPermissionLevelsResponse`

```sql
SELECT
permission_levels
FROM databricks_workspace.workspace.object_permission_levels
WHERE workspace_object_type = '{{ workspace_object_type }}' -- required
AND workspace_object_id = '{{ workspace_object_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>

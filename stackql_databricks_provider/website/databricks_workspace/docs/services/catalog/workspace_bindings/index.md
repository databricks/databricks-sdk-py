---
title: workspace_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_bindings
  - catalog
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

Creates, updates, deletes, gets or lists a <code>workspace_bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_bindings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.workspace_bindings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_bindings"
    values={[
        { label: 'get_bindings', value: 'get_bindings' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_bindings">

<SchemaTable fields={[
  {
    "name": "workspace_id",
    "type": "integer",
    "description": ""
  },
  {
    "name": "binding_type",
    "type": "string",
    "description": "One of READ_WRITE/READ_ONLY. Default is READ_WRITE. (BINDING_TYPE_READ_ONLY, BINDING_TYPE_READ_WRITE)"
  }
]} />
</TabItem>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "workspaces",
    "type": "array",
    "description": ""
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
    <td><a href="#get_bindings"><CopyableCode code="get_bindings" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-securable_type"><code>securable_type</code></a>, <a href="#parameter-securable_name"><code>securable_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets workspace bindings of the securable. The caller must be a metastore admin or an owner of the</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets workspace bindings of the catalog. The caller must be a metastore admin or an owner of the</td>
</tr>
<tr>
    <td><a href="#update_bindings"><CopyableCode code="update_bindings" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-securable_type"><code>securable_type</code></a>, <a href="#parameter-securable_name"><code>securable_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates workspace bindings of the securable. The caller must be a metastore admin or an owner of the</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates workspace bindings of the catalog. The caller must be a metastore admin or an owner of the</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the catalog.</td>
</tr>
<tr id="parameter-securable_name">
    <td><CopyableCode code="securable_name" /></td>
    <td><code>string</code></td>
    <td>The name of the securable.</td>
</tr>
<tr id="parameter-securable_type">
    <td><CopyableCode code="securable_type" /></td>
    <td><code>string</code></td>
    <td>The type of the securable to bind to a workspace (catalog, storage_credential, credential, or external_location).</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of workspace bindings to return. - When set to 0, the page length is set to a server configured value (recommended); - When set to a value greater than 0, the page length is the minimum of this value and a server configured value; - When set to a value less than 0, an invalid parameter error is returned; - If not set, all the workspace bindings are returned (not recommended).</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on previous query.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_bindings"
    values={[
        { label: 'get_bindings', value: 'get_bindings' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_bindings">

Gets workspace bindings of the securable. The caller must be a metastore admin or an owner of the

```sql
SELECT
workspace_id,
binding_type
FROM databricks_workspace.catalog.workspace_bindings
WHERE securable_type = '{{ securable_type }}' -- required
AND securable_name = '{{ securable_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="get">

Gets workspace bindings of the catalog. The caller must be a metastore admin or an owner of the

```sql
SELECT
workspaces
FROM databricks_workspace.catalog.workspace_bindings
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_bindings"
    values={[
        { label: 'update_bindings', value: 'update_bindings' },
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update_bindings">

Updates workspace bindings of the securable. The caller must be a metastore admin or an owner of the

```sql
UPDATE databricks_workspace.catalog.workspace_bindings
SET 
add = '{{ add }}',
remove = '{{ remove }}'
WHERE 
securable_type = '{{ securable_type }}' --required
AND securable_name = '{{ securable_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
bindings;
```
</TabItem>
<TabItem value="update">

Updates workspace bindings of the catalog. The caller must be a metastore admin or an owner of the

```sql
UPDATE databricks_workspace.catalog.workspace_bindings
SET 
assign_workspaces = '{{ assign_workspaces }}',
unassign_workspaces = '{{ unassign_workspaces }}'
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
workspaces;
```
</TabItem>
</Tabs>

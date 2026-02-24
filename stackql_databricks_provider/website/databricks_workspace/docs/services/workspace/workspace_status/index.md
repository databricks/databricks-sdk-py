---
title: workspace_status
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_status
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

Creates, updates, deletes, gets or lists a <code>workspace_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.workspace_status" /></td></tr>
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
    "name": "object_id",
    "type": "integer",
    "description": "Unique identifier for the object."
  },
  {
    "name": "resource_id",
    "type": "string",
    "description": "A unique identifier for the object that is consistent across all Databricks APIs."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Only applicable to files. The creation UTC timestamp."
  },
  {
    "name": "language",
    "type": "string",
    "description": "The language of the object. This value is set only if the object type is ``NOTEBOOK``. (PYTHON, R, SCALA, SQL)"
  },
  {
    "name": "modified_at",
    "type": "integer",
    "description": "Only applicable to files, the last modified UTC timestamp."
  },
  {
    "name": "object_type",
    "type": "string",
    "description": "The type of the object in workspace. - `NOTEBOOK`: document that contains runnable code, visualizations, and explanatory text. - `DIRECTORY`: directory - `LIBRARY`: library - `FILE`: file - `REPO`: repository - `DASHBOARD`: Lakeview dashboard (DASHBOARD, DIRECTORY, FILE, LIBRARY, NOTEBOOK, REPO)"
  },
  {
    "name": "path",
    "type": "string",
    "description": "The absolute path of the object."
  },
  {
    "name": "size",
    "type": "integer",
    "description": "Only applicable to files. The file size in bytes can be returned."
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
    <td><a href="#parameter-path"><code>path</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets the status of an object or a directory. If `path` does not exist, this call returns an error</td>
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
<tr id="parameter-path">
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>The absolute path of the notebook or directory.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the status of an object or a directory. If `path` does not exist, this call returns an error

```sql
SELECT
object_id,
resource_id,
created_at,
language,
modified_at,
object_type,
path,
size
FROM databricks_workspace.workspace.workspace_status
WHERE path = '{{ path }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
</Tabs>

---
title: enable_export_notebook
hide_title: false
hide_table_of_contents: false
keywords:
  - enable_export_notebook
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

Creates, updates, deletes, gets or lists an <code>enable_export_notebook</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enable_export_notebook</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settings.enable_export_notebook" /></td></tr>
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
    "name": "setting_name",
    "type": "string",
    "description": "Name of the corresponding setting. This field is populated in the response, but it will not be respected even if it's set in the request body. The setting name in the path parameter will be respected instead. Setting name is required to be 'default' if the setting only has one instance per workspace."
  },
  {
    "name": "boolean_val",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "value",
        "type": "boolean",
        "description": ""
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
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the Notebook and File exporting setting.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__allow_missing"><code>data__allow_missing</code></a>, <a href="#parameter-data__setting"><code>data__setting</code></a>, <a href="#parameter-data__field_mask"><code>data__field_mask</code></a></td>
    <td></td>
    <td>Updates the Notebook and File exporting setting. The model follows eventual consistency, which means</td>
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

Gets the Notebook and File exporting setting.

```sql
SELECT
setting_name,
boolean_val
FROM databricks_workspace.settings.enable_export_notebook
WHERE deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates the Notebook and File exporting setting. The model follows eventual consistency, which means

```sql
UPDATE databricks_workspace.settings.enable_export_notebook
SET 
data__allow_missing = {{ allow_missing }},
data__setting = '{{ setting }}',
data__field_mask = '{{ field_mask }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
AND data__allow_missing = {{ allow_missing }} --required
AND data__setting = '{{ setting }}' --required
AND data__field_mask = '{{ field_mask }}' --required
RETURNING
setting_name,
boolean_val;
```
</TabItem>
</Tabs>

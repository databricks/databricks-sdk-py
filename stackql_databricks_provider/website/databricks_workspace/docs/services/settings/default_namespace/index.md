---
title: default_namespace
hide_title: false
hide_table_of_contents: false
keywords:
  - default_namespace
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

Creates, updates, deletes, gets or lists a <code>default_namespace</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="default_namespace" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settings.default_namespace" /></td></tr>
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
    "name": "etag",
    "type": "string",
    "description": "etag used for versioning. The response is at least as fresh as the eTag provided. This is used for optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting each other. It is strongly suggested that systems make use of the etag in the read -&gt; update pattern to perform setting updates in order to avoid race conditions. That is, get an etag from a GET request, and pass it with the PATCH request to identify the setting version you are updating."
  },
  {
    "name": "namespace",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "value",
        "type": "string",
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
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Gets the default namespace setting.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-allow_missing"><code>allow_missing</code></a>, <a href="#parameter-setting"><code>setting</code></a>, <a href="#parameter-field_mask"><code>field_mask</code></a></td>
    <td></td>
    <td>Updates the default namespace setting for the workspace. A fresh etag needs to be provided in `PATCH`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Deletes the default namespace setting for the workspace. A fresh etag needs to be provided in `DELETE`</td>
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
<tr id="parameter-etag">
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>etag used for versioning. The response is at least as fresh as the eTag provided. This is used for optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting each other. It is strongly suggested that systems make use of the etag in the read -&gt; delete pattern to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET request, and pass it with the DELETE request to identify the rule set version you are deleting.</td>
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

Gets the default namespace setting.

```sql
SELECT
setting_name,
etag,
namespace
FROM databricks_workspace.settings.default_namespace
WHERE deployment_name = '{{ deployment_name }}' -- required
AND etag = '{{ etag }}'
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

Updates the default namespace setting for the workspace. A fresh etag needs to be provided in `PATCH`

```sql
UPDATE databricks_workspace.settings.default_namespace
SET 
allow_missing = {{ allow_missing }},
setting = '{{ setting }}',
field_mask = '{{ field_mask }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
AND allow_missing = {{ allow_missing }} --required
AND setting = '{{ setting }}' --required
AND field_mask = '{{ field_mask }}' --required
RETURNING
setting_name,
etag,
namespace;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes the default namespace setting for the workspace. A fresh etag needs to be provided in `DELETE`

```sql
DELETE FROM databricks_workspace.settings.default_namespace
WHERE deployment_name = '{{ deployment_name }}' --required
AND etag = '{{ etag }}'
;
```
</TabItem>
</Tabs>

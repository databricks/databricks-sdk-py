---
title: artifact_allowlists
hide_title: false
hide_table_of_contents: false
keywords:
  - artifact_allowlists
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

Creates, updates, deletes, gets or lists an <code>artifact_allowlists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="artifact_allowlists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.artifact_allowlists" /></td></tr>
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
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of parent metastore."
  },
  {
    "name": "artifact_matchers",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "artifact",
        "type": "string",
        "description": ""
      },
      {
        "name": "match_type",
        "type": "string",
        "description": "The pattern matching type of the artifact (PREFIX_MATCH)"
      }
    ]
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this artifact allowlist was set, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of the user who set the artifact allowlist."
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
    <td><a href="#parameter-artifact_type.value"><code>artifact_type.value</code></a>, <a href="#parameter-artifact_type"><code>artifact_type</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Get the artifact allowlist of a certain artifact type. The caller must be a metastore admin or have</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-artifact_type.value"><code>artifact_type.value</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-artifact_type"><code>artifact_type</code></a>, <a href="#parameter-artifact_matchers"><code>artifact_matchers</code></a></td>
    <td></td>
    <td>Set the artifact allowlist of a certain artifact type. The whole artifact allowlist is replaced with</td>
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
<tr id="parameter-artifact_type">
    <td><CopyableCode code="artifact_type" /></td>
    <td><code>string</code></td>
    <td>The artifact type of the allowlist.</td>
</tr>
<tr id="parameter-artifact_type.value">
    <td><CopyableCode code="artifact_type.value" /></td>
    <td><code>string</code></td>
    <td></td>
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

Get the artifact allowlist of a certain artifact type. The caller must be a metastore admin or have

```sql
SELECT
metastore_id,
artifact_matchers,
created_at,
created_by
FROM databricks_workspace.catalog.artifact_allowlists
WHERE artifact_type.value = '{{ artifact_type.value }}' -- required
AND artifact_type = '{{ artifact_type }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="replace"
    values={[
        { label: 'replace', value: 'replace' }
    ]}
>
<TabItem value="replace">

Set the artifact allowlist of a certain artifact type. The whole artifact allowlist is replaced with

```sql
REPLACE databricks_workspace.catalog.artifact_allowlists
SET 
artifact_type = '{{ artifact_type }}',
artifact_matchers = '{{ artifact_matchers }}',
created_at = {{ created_at }},
created_by = '{{ created_by }}',
metastore_id = '{{ metastore_id }}'
WHERE 
artifact_type.value = '{{ artifact_type.value }}' --required
AND workspace = '{{ workspace }}' --required
AND artifact_type = '{{ artifact_type }}' --required
AND artifact_matchers = '{{ artifact_matchers }}' --required
RETURNING
metastore_id,
artifact_matchers,
created_at,
created_by;
```
</TabItem>
</Tabs>

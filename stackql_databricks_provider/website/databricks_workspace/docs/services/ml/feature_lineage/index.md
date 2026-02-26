---
title: feature_lineage
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_lineage
  - ml
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

Creates, updates, deletes, gets or lists a <code>feature_lineage</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="feature_lineage" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.feature_lineage" /></td></tr>
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
    "name": "feature_specs",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "models",
    "type": "array",
    "description": "List of Unity Catalog models that were trained on this feature.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "version",
        "type": "integer",
        "description": "The version of the model."
      }
    ]
  },
  {
    "name": "online_features",
    "type": "array",
    "description": "List of online features that use this feature as source.",
    "children": [
      {
        "name": "feature_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "table_name",
        "type": "string",
        "description": "The full name of the online table in Unity Catalog."
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
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get Feature Lineage.</td>
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
<tr id="parameter-feature_name">
    <td><CopyableCode code="feature_name" /></td>
    <td><code>string</code></td>
    <td>The name of the feature.</td>
</tr>
<tr id="parameter-table_name">
    <td><CopyableCode code="table_name" /></td>
    <td><code>string</code></td>
    <td>The full name of the feature table in Unity Catalog.</td>
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

Get Feature Lineage.

```sql
SELECT
feature_specs,
models,
online_features
FROM databricks_workspace.ml.feature_lineage
WHERE table_name = '{{ table_name }}' -- required
AND feature_name = '{{ feature_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>

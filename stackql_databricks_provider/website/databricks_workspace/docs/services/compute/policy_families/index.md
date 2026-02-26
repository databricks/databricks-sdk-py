---
title: policy_families
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_families
  - compute
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

Creates, updates, deletes, gets or lists a <code>policy_families</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_families" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.policy_families" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of the policy family."
  },
  {
    "name": "policy_family_id",
    "type": "string",
    "description": "Unique identifier for the policy family."
  },
  {
    "name": "definition",
    "type": "string",
    "description": ""
  },
  {
    "name": "description",
    "type": "string",
    "description": "Human-readable description of the purpose of the policy family."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of the policy family."
  },
  {
    "name": "policy_family_id",
    "type": "string",
    "description": "Unique identifier for the policy family."
  },
  {
    "name": "definition",
    "type": "string",
    "description": ""
  },
  {
    "name": "description",
    "type": "string",
    "description": "Human-readable description of the purpose of the policy family."
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
    <td><a href="#parameter-policy_family_id"><code>policy_family_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-version"><code>version</code></a></td>
    <td>Retrieve the information for an policy family based on its identifier and version</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns the list of policy definition types available to use at their latest version. This API is</td>
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
<tr id="parameter-policy_family_id">
    <td><CopyableCode code="policy_family_id" /></td>
    <td><code>string</code></td>
    <td>The family ID about which to retrieve information.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of policy families to return.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A token that can be used to get the next page of results.</td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>The version number for the family to fetch. Defaults to the latest version.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieve the information for an policy family based on its identifier and version

```sql
SELECT
name,
policy_family_id,
definition,
description
FROM databricks_workspace.compute.policy_families
WHERE policy_family_id = '{{ policy_family_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND version = '{{ version }}'
;
```
</TabItem>
<TabItem value="list">

Returns the list of policy definition types available to use at their latest version. This API is

```sql
SELECT
name,
policy_family_id,
definition,
description
FROM databricks_workspace.compute.policy_families
WHERE deployment_name = '{{ deployment_name }}' -- required
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>

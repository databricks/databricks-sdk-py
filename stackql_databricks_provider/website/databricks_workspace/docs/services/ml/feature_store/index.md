---
title: feature_store
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_store
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>feature_store</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="feature_store" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.feature_store" /></td></tr>
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
    "description": "The name of the online store. This is the unique identifier for the online store."
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": "The usage policy applied to the online store to track billing."
  },
  {
    "name": "capacity",
    "type": "string",
    "description": "The capacity of the online store. Valid values are \"CU_1\", \"CU_2\", \"CU_4\", \"CU_8\"."
  },
  {
    "name": "creation_time",
    "type": "string",
    "description": "The timestamp when the online store was created."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the creator of the online store."
  },
  {
    "name": "read_replica_count",
    "type": "integer",
    "description": "The number of read replicas for the online store. Defaults to 0."
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current state of the online store. (AVAILABLE, DELETING, FAILING_OVER, STARTING, STOPPED, UPDATING)"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the online store. This is the unique identifier for the online store."
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": "The usage policy applied to the online store to track billing."
  },
  {
    "name": "capacity",
    "type": "string",
    "description": "The capacity of the online store. Valid values are \"CU_1\", \"CU_2\", \"CU_4\", \"CU_8\"."
  },
  {
    "name": "creation_time",
    "type": "string",
    "description": "The timestamp when the online store was created."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the creator of the online store."
  },
  {
    "name": "read_replica_count",
    "type": "integer",
    "description": "The number of read replicas for the online store. Defaults to 0."
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current state of the online store. (AVAILABLE, DELETING, FAILING_OVER, STARTING, STOPPED, UPDATING)"
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get an Online Feature Store.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List Online Feature Stores.</td>
</tr>
<tr>
    <td><a href="#publish_table"><CopyableCode code="publish_table" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-source_table_name"><code>source_table_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-publish_spec"><code>publish_spec</code></a></td>
    <td></td>
    <td>Publish features.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-online_store"><code>online_store</code></a></td>
    <td></td>
    <td>Create an Online Feature Store.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-online_store"><code>online_store</code></a></td>
    <td></td>
    <td>Update an Online Feature Store.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete an Online Feature Store.</td>
</tr>
<tr>
    <td><a href="#delete_table"><CopyableCode code="delete_table" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-online_table_name"><code>online_table_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete online table.</td>
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
    <td>Name of the online store to delete.</td>
</tr>
<tr id="parameter-online_table_name">
    <td><CopyableCode code="online_table_name" /></td>
    <td><code>string</code></td>
    <td>The full three-part (catalog, schema, table) name of the online table.</td>
</tr>
<tr id="parameter-source_table_name">
    <td><CopyableCode code="source_table_name" /></td>
    <td><code>string</code></td>
    <td>The full three-part (catalog, schema, table) name of the source table.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>The list of fields to update.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>The maximum number of results to return. Defaults to 100 if not specified.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page based on a previous query.</td>
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

Get an Online Feature Store.

```sql
SELECT
name,
usage_policy_id,
capacity,
creation_time,
creator,
read_replica_count,
state
FROM databricks_workspace.ml.feature_store
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Online Feature Stores.

```sql
SELECT
name,
usage_policy_id,
capacity,
creation_time,
creator,
read_replica_count,
state
FROM databricks_workspace.ml.feature_store
WHERE deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="publish_table"
    values={[
        { label: 'publish_table', value: 'publish_table' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="publish_table">

Publish features.

```sql
INSERT INTO databricks_workspace.ml.feature_store (
publish_spec,
source_table_name,
deployment_name
)
SELECT 
'{{ publish_spec }}' /* required */,
'{{ source_table_name }}',
'{{ deployment_name }}'
RETURNING
pipeline_id,
online_table_name
;
```
</TabItem>
<TabItem value="create">

Create an Online Feature Store.

```sql
INSERT INTO databricks_workspace.ml.feature_store (
online_store,
deployment_name
)
SELECT 
'{{ online_store }}' /* required */,
'{{ deployment_name }}'
RETURNING
name,
usage_policy_id,
capacity,
creation_time,
creator,
read_replica_count,
state
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: feature_store
  props:
    - name: source_table_name
      value: string
      description: Required parameter for the feature_store resource.
    - name: deployment_name
      value: string
      description: Required parameter for the feature_store resource.
    - name: publish_spec
      value: string
      description: |
        The specification for publishing the online table from the source table.
    - name: online_store
      value: string
      description: |
        Online store to create.
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

Update an Online Feature Store.

```sql
UPDATE databricks_workspace.ml.feature_store
SET 
online_store = '{{ online_store }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND online_store = '{{ online_store }}' --required
RETURNING
name,
usage_policy_id,
capacity,
creation_time,
creator,
read_replica_count,
state;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'delete_table', value: 'delete_table' }
    ]}
>
<TabItem value="delete">

Delete an Online Feature Store.

```sql
DELETE FROM databricks_workspace.ml.feature_store
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="delete_table">

Delete online table.

```sql
DELETE FROM databricks_workspace.ml.feature_store
WHERE online_table_name = '{{ online_table_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

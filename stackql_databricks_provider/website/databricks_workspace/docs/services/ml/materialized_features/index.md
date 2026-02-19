---
title: materialized_features
hide_title: false
hide_table_of_contents: false
keywords:
  - materialized_features
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

Creates, updates, deletes, gets or lists a <code>materialized_features</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="materialized_features" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.materialized_features" /></td></tr>
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
    "name": "key",
    "type": "string",
    "description": ""
  },
  {
    "name": "value",
    "type": "string",
    "description": ""
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "key",
    "type": "string",
    "description": ""
  },
  {
    "name": "value",
    "type": "string",
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a FeatureTag.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists FeatureTags.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-feature_tag"><code>feature_tag</code></a></td>
    <td></td>
    <td>Creates a FeatureTag.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-feature_tag"><code>feature_tag</code></a></td>
    <td><a href="#parameter-update_mask"><code>update_mask</code></a></td>
    <td>Updates a FeatureTag.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a FeatureTag.</td>
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
    <td>The name of the feature within the feature table.</td>
</tr>
<tr id="parameter-key">
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>The key of the tag to delete.</td>
</tr>
<tr id="parameter-table_name">
    <td><CopyableCode code="table_name" /></td>
    <td><code>string</code></td>
    <td>The name of the feature table.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>The maximum number of results to return.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page based on a previous query.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>The list of fields to update.</td>
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

Gets a FeatureTag.

```sql
SELECT
key,
value
FROM databricks_workspace.ml.materialized_features
WHERE table_name = '{{ table_name }}' -- required
AND feature_name = '{{ feature_name }}' -- required
AND key = '{{ key }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists FeatureTags.

```sql
SELECT
key,
value
FROM databricks_workspace.ml.materialized_features
WHERE table_name = '{{ table_name }}' -- required
AND feature_name = '{{ feature_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a FeatureTag.

```sql
INSERT INTO databricks_workspace.ml.materialized_features (
feature_tag,
table_name,
feature_name,
deployment_name
)
SELECT 
'{{ feature_tag }}' /* required */,
'{{ table_name }}',
'{{ feature_name }}',
'{{ deployment_name }}'
RETURNING
key,
value
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: materialized_features
  props:
    - name: table_name
      value: string
      description: Required parameter for the materialized_features resource.
    - name: feature_name
      value: string
      description: Required parameter for the materialized_features resource.
    - name: deployment_name
      value: string
      description: Required parameter for the materialized_features resource.
    - name: feature_tag
      value: string
      description: |
        :returns: :class:`FeatureTag`
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

Updates a FeatureTag.

```sql
UPDATE databricks_workspace.ml.materialized_features
SET 
feature_tag = '{{ feature_tag }}'
WHERE 
table_name = '{{ table_name }}' --required
AND feature_name = '{{ feature_name }}' --required
AND key = '{{ key }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND feature_tag = '{{ feature_tag }}' --required
AND update_mask = '{{ update_mask}}'
RETURNING
key,
value;
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

Deletes a FeatureTag.

```sql
DELETE FROM databricks_workspace.ml.materialized_features
WHERE table_name = '{{ table_name }}' --required
AND feature_name = '{{ feature_name }}' --required
AND key = '{{ key }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

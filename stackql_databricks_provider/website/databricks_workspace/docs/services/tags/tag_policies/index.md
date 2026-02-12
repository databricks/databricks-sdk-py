---
title: tag_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_policies
  - tags
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

Creates, updates, deletes, gets or lists a <code>tag_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.tags.tag_policies" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": ""
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "Timestamp when the tag policy was created"
  },
  {
    "name": "description",
    "type": "string",
    "description": ""
  },
  {
    "name": "tag_key",
    "type": "string",
    "description": ""
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "Timestamp when the tag policy was last updated"
  },
  {
    "name": "values",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": ""
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "Timestamp when the tag policy was created"
  },
  {
    "name": "description",
    "type": "string",
    "description": ""
  },
  {
    "name": "tag_key",
    "type": "string",
    "description": ""
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "Timestamp when the tag policy was last updated"
  },
  {
    "name": "values",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "name",
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
    <td><a href="#parameter-tag_key"><code>tag_key</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a single tag policy by its associated governed tag's key. For Terraform usage, see the [Tag</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists the tag policies for all governed tags in the account. For Terraform usage, see the [Tag Policy</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__tag_policy"><code>data__tag_policy</code></a></td>
    <td></td>
    <td>Creates a new tag policy, making the associated tag key governed. For Terraform usage, see the [Tag</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-tag_key"><code>tag_key</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__tag_policy"><code>data__tag_policy</code></a></td>
    <td></td>
    <td>Updates an existing tag policy for a single governed tag. For Terraform usage, see the [Tag Policy</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-tag_key"><code>tag_key</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a tag policy by its associated governed tag's key, leaving that tag key ungoverned. For</td>
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
<tr id="parameter-tag_key">
    <td><CopyableCode code="tag_key" /></td>
    <td><code>string</code></td>
    <td>str</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>The field mask must be a single string, with multiple fields separated by commas (no spaces). The field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g., `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only the entire collection field can be specified. Field names must exactly match the resource field names. A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API changes in the future.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>The maximum number of results to return in this request. Fewer results may be returned than requested. If unspecified or set to 0, this defaults to 1000. The maximum value is 1000; values above 1000 will be coerced down to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>An optional page token received from a previous list tag policies call.</td>
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

Gets a single tag policy by its associated governed tag's key. For Terraform usage, see the [Tag

```sql
SELECT
id,
create_time,
description,
tag_key,
update_time,
values
FROM databricks_workspace.tags.tag_policies
WHERE tag_key = '{{ tag_key }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the tag policies for all governed tags in the account. For Terraform usage, see the [Tag Policy

```sql
SELECT
id,
create_time,
description,
tag_key,
update_time,
values
FROM databricks_workspace.tags.tag_policies
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Creates a new tag policy, making the associated tag key governed. For Terraform usage, see the [Tag

```sql
INSERT INTO databricks_workspace.tags.tag_policies (
data__tag_policy,
deployment_name
)
SELECT 
'{{ tag_policy }}' /* required */,
'{{ deployment_name }}'
RETURNING
id,
create_time,
description,
tag_key,
update_time,
values
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: tag_policies
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the tag_policies resource.
    - name: tag_policy
      value: string
      description: |
        :returns: :class:`TagPolicy`
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

Updates an existing tag policy for a single governed tag. For Terraform usage, see the [Tag Policy

```sql
UPDATE databricks_workspace.tags.tag_policies
SET 
data__tag_policy = '{{ tag_policy }}'
WHERE 
tag_key = '{{ tag_key }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__tag_policy = '{{ tag_policy }}' --required
RETURNING
id,
create_time,
description,
tag_key,
update_time,
values;
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

Deletes a tag policy by its associated governed tag's key, leaving that tag key ungoverned. For

```sql
DELETE FROM databricks_workspace.tags.tag_policies
WHERE tag_key = '{{ tag_key }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

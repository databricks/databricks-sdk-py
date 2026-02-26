---
title: workspace_entity_tag_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_entity_tag_assignments
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>workspace_entity_tag_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_entity_tag_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.tags.workspace_entity_tag_assignments" /></td></tr>
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
    "name": "entity_id",
    "type": "string",
    "description": "The identifier of the entity to which the tag is assigned"
  },
  {
    "name": "entity_type",
    "type": "string",
    "description": ""
  },
  {
    "name": "tag_key",
    "type": "string",
    "description": "The key of the tag. The characters , . : / - = and leading/trailing spaces are not allowed"
  },
  {
    "name": "tag_value",
    "type": "string",
    "description": "The value of the tag"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "entity_id",
    "type": "string",
    "description": "The identifier of the entity to which the tag is assigned"
  },
  {
    "name": "entity_type",
    "type": "string",
    "description": ""
  },
  {
    "name": "tag_key",
    "type": "string",
    "description": "The key of the tag. The characters , . : / - = and leading/trailing spaces are not allowed"
  },
  {
    "name": "tag_value",
    "type": "string",
    "description": "The value of the tag"
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
    <td><a href="#parameter-entity_type"><code>entity_type</code></a>, <a href="#parameter-entity_id"><code>entity_id</code></a>, <a href="#parameter-tag_key"><code>tag_key</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a tag assignment</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-entity_type"><code>entity_type</code></a>, <a href="#parameter-entity_id"><code>entity_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List the tag assignments for an entity</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-tag_assignment"><code>tag_assignment</code></a></td>
    <td></td>
    <td>Create a tag assignment</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-entity_type"><code>entity_type</code></a>, <a href="#parameter-entity_id"><code>entity_id</code></a>, <a href="#parameter-tag_key"><code>tag_key</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-tag_assignment"><code>tag_assignment</code></a></td>
    <td></td>
    <td>Update a tag assignment</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-entity_type"><code>entity_type</code></a>, <a href="#parameter-entity_id"><code>entity_id</code></a>, <a href="#parameter-tag_key"><code>tag_key</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a tag assignment</td>
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
<tr id="parameter-entity_id">
    <td><CopyableCode code="entity_id" /></td>
    <td><code>string</code></td>
    <td>The identifier of the entity to which the tag is assigned</td>
</tr>
<tr id="parameter-entity_type">
    <td><CopyableCode code="entity_type" /></td>
    <td><code>string</code></td>
    <td>The type of entity to which the tag is assigned. Allowed values are apps, dashboards, geniespaces</td>
</tr>
<tr id="parameter-tag_key">
    <td><CopyableCode code="tag_key" /></td>
    <td><code>string</code></td>
    <td>The key of the tag. The characters , . : / - = and leading/trailing spaces are not allowed</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Optional. Maximum number of tag assignments to return in a single page</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page of tag assignments. Requests first page if absent.</td>
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

Get a tag assignment

```sql
SELECT
entity_id,
entity_type,
tag_key,
tag_value
FROM databricks_workspace.tags.workspace_entity_tag_assignments
WHERE entity_type = '{{ entity_type }}' -- required
AND entity_id = '{{ entity_id }}' -- required
AND tag_key = '{{ tag_key }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the tag assignments for an entity

```sql
SELECT
entity_id,
entity_type,
tag_key,
tag_value
FROM databricks_workspace.tags.workspace_entity_tag_assignments
WHERE entity_type = '{{ entity_type }}' -- required
AND entity_id = '{{ entity_id }}' -- required
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

Create a tag assignment

```sql
INSERT INTO databricks_workspace.tags.workspace_entity_tag_assignments (
tag_assignment,
deployment_name
)
SELECT 
'{{ tag_assignment }}' /* required */,
'{{ deployment_name }}'
RETURNING
entity_id,
entity_type,
tag_key,
tag_value
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: workspace_entity_tag_assignments
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the workspace_entity_tag_assignments resource.
    - name: tag_assignment
      description: |
        :returns: :class:\`TagAssignment\`
      value:
        entity_type: "{{ entity_type }}"
        entity_id: "{{ entity_id }}"
        tag_key: "{{ tag_key }}"
        tag_value: "{{ tag_value }}"
`}</CodeBlock>

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

Update a tag assignment

```sql
UPDATE databricks_workspace.tags.workspace_entity_tag_assignments
SET 
tag_assignment = '{{ tag_assignment }}'
WHERE 
entity_type = '{{ entity_type }}' --required
AND entity_id = '{{ entity_id }}' --required
AND tag_key = '{{ tag_key }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND tag_assignment = '{{ tag_assignment }}' --required
RETURNING
entity_id,
entity_type,
tag_key,
tag_value;
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

Delete a tag assignment

```sql
DELETE FROM databricks_workspace.tags.workspace_entity_tag_assignments
WHERE entity_type = '{{ entity_type }}' --required
AND entity_id = '{{ entity_id }}' --required
AND tag_key = '{{ tag_key }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

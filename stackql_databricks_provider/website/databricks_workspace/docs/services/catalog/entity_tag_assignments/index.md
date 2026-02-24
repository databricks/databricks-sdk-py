---
title: entity_tag_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - entity_tag_assignments
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

Creates, updates, deletes, gets or lists an <code>entity_tag_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entity_tag_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.entity_tag_assignments" /></td></tr>
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
    "name": "entity_name",
    "type": "string",
    "description": "The fully qualified name of the entity to which the tag is assigned"
  },
  {
    "name": "entity_type",
    "type": "string",
    "description": "The type of the entity to which the tag is assigned. Allowed values are: catalogs, schemas, tables, columns, volumes."
  },
  {
    "name": "tag_key",
    "type": "string",
    "description": "The key of the tag"
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
    "name": "entity_name",
    "type": "string",
    "description": "The fully qualified name of the entity to which the tag is assigned"
  },
  {
    "name": "entity_type",
    "type": "string",
    "description": "The type of the entity to which the tag is assigned. Allowed values are: catalogs, schemas, tables, columns, volumes."
  },
  {
    "name": "tag_key",
    "type": "string",
    "description": "The key of the tag"
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
    <td><a href="#parameter-entity_type"><code>entity_type</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-tag_key"><code>tag_key</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets a tag assignment for an Unity Catalog entity by tag key.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-entity_type"><code>entity_type</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List tag assignments for an Unity Catalog entity</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-tag_assignment"><code>tag_assignment</code></a></td>
    <td></td>
    <td>Creates a tag assignment for an Unity Catalog entity.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-entity_type"><code>entity_type</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-tag_key"><code>tag_key</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-tag_assignment"><code>tag_assignment</code></a></td>
    <td></td>
    <td>Updates an existing tag assignment for an Unity Catalog entity.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-entity_type"><code>entity_type</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-tag_key"><code>tag_key</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Deletes a tag assignment for an Unity Catalog entity by its key.</td>
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
<tr id="parameter-entity_name">
    <td><CopyableCode code="entity_name" /></td>
    <td><code>string</code></td>
    <td>The fully qualified name of the entity to which the tag is assigned</td>
</tr>
<tr id="parameter-entity_type">
    <td><CopyableCode code="entity_type" /></td>
    <td><code>string</code></td>
    <td>The type of the entity to which the tag is assigned. Allowed values are: catalogs, schemas, tables, columns, volumes.</td>
</tr>
<tr id="parameter-tag_key">
    <td><CopyableCode code="tag_key" /></td>
    <td><code>string</code></td>
    <td>Required. The key of the tag to delete</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
    <td>Optional. Maximum number of tag assignments to return in a single page</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Optional. Pagination token to retrieve the next page of results</td>
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

Gets a tag assignment for an Unity Catalog entity by tag key.

```sql
SELECT
entity_name,
entity_type,
tag_key,
tag_value
FROM databricks_workspace.catalog.entity_tag_assignments
WHERE entity_type = '{{ entity_type }}' -- required
AND entity_name = '{{ entity_name }}' -- required
AND tag_key = '{{ tag_key }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

List tag assignments for an Unity Catalog entity

```sql
SELECT
entity_name,
entity_type,
tag_key,
tag_value
FROM databricks_workspace.catalog.entity_tag_assignments
WHERE entity_type = '{{ entity_type }}' -- required
AND entity_name = '{{ entity_name }}' -- required
AND workspace = '{{ workspace }}' -- required
AND max_results = '{{ max_results }}'
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

Creates a tag assignment for an Unity Catalog entity.

```sql
INSERT INTO databricks_workspace.catalog.entity_tag_assignments (
tag_assignment,
workspace
)
SELECT 
'{{ tag_assignment }}' /* required */,
'{{ workspace }}'
RETURNING
entity_name,
entity_type,
tag_key,
tag_value
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: entity_tag_assignments
  props:
    - name: workspace
      value: string
      description: Required parameter for the entity_tag_assignments resource.
    - name: tag_assignment
      value: object
      description: |
        :returns: :class:`EntityTagAssignment`
      props:
      - name: entity_name
        value: string
        description: |
          The fully qualified name of the entity to which the tag is assigned
      - name: tag_key
        value: string
        description: |
          The key of the tag
      - name: entity_type
        value: string
        description: |
          The type of the entity to which the tag is assigned. Allowed values are: catalogs, schemas, tables, columns, volumes.
      - name: tag_value
        value: string
        description: |
          The value of the tag
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

Updates an existing tag assignment for an Unity Catalog entity.

```sql
UPDATE databricks_workspace.catalog.entity_tag_assignments
SET 
tag_assignment = '{{ tag_assignment }}'
WHERE 
entity_type = '{{ entity_type }}' --required
AND entity_name = '{{ entity_name }}' --required
AND tag_key = '{{ tag_key }}' --required
AND update_mask = '{{ update_mask }}' --required
AND workspace = '{{ workspace }}' --required
AND tag_assignment = '{{ tag_assignment }}' --required
RETURNING
entity_name,
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

Deletes a tag assignment for an Unity Catalog entity by its key.

```sql
DELETE FROM databricks_workspace.catalog.entity_tag_assignments
WHERE entity_type = '{{ entity_type }}' --required
AND entity_name = '{{ entity_name }}' --required
AND tag_key = '{{ tag_key }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

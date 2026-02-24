---
title: default_warehouse_overrides
hide_title: false
hide_table_of_contents: false
keywords:
  - default_warehouse_overrides
  - sql
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

Creates, updates, deletes, gets or lists a <code>default_warehouse_overrides</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="default_warehouse_overrides" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.default_warehouse_overrides" /></td></tr>
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
    "description": "The resource name of the default warehouse override. Format: default-warehouse-overrides/&#123;default_warehouse_override_id&#125;"
  },
  {
    "name": "default_warehouse_override_id",
    "type": "string",
    "description": "The ID component of the resource name (user ID)."
  },
  {
    "name": "warehouse_id",
    "type": "string",
    "description": "The specific warehouse ID when type is CUSTOM. Not set for LAST_SELECTED type."
  },
  {
    "name": "type",
    "type": "string",
    "description": "The type of override behavior. (CUSTOM, LAST_SELECTED)"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The resource name of the default warehouse override. Format: default-warehouse-overrides/&#123;default_warehouse_override_id&#125;"
  },
  {
    "name": "default_warehouse_override_id",
    "type": "string",
    "description": "The ID component of the resource name (user ID)."
  },
  {
    "name": "warehouse_id",
    "type": "string",
    "description": "The specific warehouse ID when type is CUSTOM. Not set for LAST_SELECTED type."
  },
  {
    "name": "type",
    "type": "string",
    "description": "The type of override behavior. (CUSTOM, LAST_SELECTED)"
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Returns the default warehouse override for a user. Users can fetch their own override. Admins can</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists all default warehouse overrides in the workspace. Only workspace administrators can list all</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-default_warehouse_override_id"><code>default_warehouse_override_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-default_warehouse_override"><code>default_warehouse_override</code></a></td>
    <td></td>
    <td>Creates a new default warehouse override for a user. Users can create their own override. Admins can</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-default_warehouse_override"><code>default_warehouse_override</code></a></td>
    <td><a href="#parameter-allow_missing"><code>allow_missing</code></a></td>
    <td>Updates an existing default warehouse override for a user. Users can update their own override. Admins</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Deletes the default warehouse override for a user. Users can delete their own override. Admins can</td>
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
<tr id="parameter-default_warehouse_override_id">
    <td><CopyableCode code="default_warehouse_override_id" /></td>
    <td><code>string</code></td>
    <td>Required. The ID to use for the override, which will become the final component of the override's resource name. Can be a numeric user ID or the literal string "me" for the current user.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Required. The resource name of the default warehouse override to delete. Format: default-warehouse-overrides/&#123;default_warehouse_override_id&#125; The default_warehouse_override_id can be a numeric user ID or the literal string "me" for the current user.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Required. Field mask specifying which fields to update. Only the fields specified in the mask will be updated. Use "*" to update all fields. When allow_missing is true, this field is ignored and all fields are applied.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-allow_missing">
    <td><CopyableCode code="allow_missing" /></td>
    <td><code>boolean</code></td>
    <td>If set to true, and the override is not found, a new override will be created. In this situation, `update_mask` is ignored and all fields are applied. Defaults to false.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of overrides to return. The service may return fewer than this value. If unspecified, at most 100 overrides will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous `ListDefaultWarehouseOverrides` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDefaultWarehouseOverrides` must match the call that provided the page token.</td>
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

Returns the default warehouse override for a user. Users can fetch their own override. Admins can

```sql
SELECT
name,
default_warehouse_override_id,
warehouse_id,
type
FROM databricks_workspace.sql.default_warehouse_overrides
WHERE name = '{{ name }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all default warehouse overrides in the workspace. Only workspace administrators can list all

```sql
SELECT
name,
default_warehouse_override_id,
warehouse_id,
type
FROM databricks_workspace.sql.default_warehouse_overrides
WHERE workspace = '{{ workspace }}' -- required
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

Creates a new default warehouse override for a user. Users can create their own override. Admins can

```sql
INSERT INTO databricks_workspace.sql.default_warehouse_overrides (
default_warehouse_override,
default_warehouse_override_id,
workspace
)
SELECT 
'{{ default_warehouse_override }}' /* required */,
'{{ default_warehouse_override_id }}',
'{{ workspace }}'
RETURNING
name,
default_warehouse_override_id,
warehouse_id,
type
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: default_warehouse_overrides
  props:
    - name: default_warehouse_override_id
      value: string
      description: Required parameter for the default_warehouse_overrides resource.
    - name: workspace
      value: string
      description: Required parameter for the default_warehouse_overrides resource.
    - name: default_warehouse_override
      value: object
      description: |
        Required. The default warehouse override to create.
      props:
      - name: type
        value: string
        description: |
          The type of override behavior.
      - name: default_warehouse_override_id
        value: string
        description: |
          The ID component of the resource name (user ID).
      - name: name
        value: string
        description: |
          The resource name of the default warehouse override. Format: default-warehouse-overrides/{default_warehouse_override_id}
      - name: warehouse_id
        value: string
        description: |
          The specific warehouse ID when type is CUSTOM. Not set for LAST_SELECTED type.
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

Updates an existing default warehouse override for a user. Users can update their own override. Admins

```sql
UPDATE databricks_workspace.sql.default_warehouse_overrides
SET 
default_warehouse_override = '{{ default_warehouse_override }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND workspace = '{{ workspace }}' --required
AND default_warehouse_override = '{{ default_warehouse_override }}' --required
AND allow_missing = {{ allow_missing}}
RETURNING
name,
default_warehouse_override_id,
warehouse_id,
type;
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

Deletes the default warehouse override for a user. Users can delete their own override. Admins can

```sql
DELETE FROM databricks_workspace.sql.default_warehouse_overrides
WHERE name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - cleanrooms
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

Creates, updates, deletes, gets or lists an <code>assets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="assets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.cleanrooms.assets" /></td></tr>
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
    "description": "A fully qualified name that uniquely identifies the asset within the clean room. This is also the name displayed in the clean room UI. For UC securable assets (tables, volumes, etc.), the format is *shared_catalog*.*shared_schema*.*asset_name* For notebooks, the name is the notebook file name. For jar analyses, the name is the jar analysis name."
  },
  {
    "name": "clean_room_name",
    "type": "string",
    "description": "The name of the clean room this asset belongs to. This field is required for create operations and populated by the server for responses."
  },
  {
    "name": "added_at",
    "type": "integer",
    "description": "When the asset is added to the clean room, in epoch milliseconds."
  },
  {
    "name": "asset_type",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FOREIGN_TABLE, NOTEBOOK_FILE, TABLE, VIEW, VOLUME)"
  },
  {
    "name": "foreign_table",
    "type": "object",
    "description": "Foreign table details available to all collaborators of the clean room. Present if and only if **asset_type** is **FOREIGN_TABLE**",
    "children": [
      {
        "name": "columns",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "foreign_table_local_details",
    "type": "object",
    "description": "Local details for a foreign that are only available to its owner. Present if and only if **asset_type** is **FOREIGN_TABLE**",
    "children": [
      {
        "name": "local_name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "notebook",
    "type": "object",
    "description": "Notebook details available to all collaborators of the clean room. Present if and only if **asset_type** is **NOTEBOOK_FILE**",
    "children": [
      {
        "name": "notebook_content",
        "type": "string",
        "description": ""
      },
      {
        "name": "etag",
        "type": "string",
        "description": "Server generated etag that represents the notebook version."
      },
      {
        "name": "review_state",
        "type": "string",
        "description": "Top-level status derived from all reviews (APPROVED, PENDING, REJECTED)"
      },
      {
        "name": "reviews",
        "type": "array",
        "description": "All existing approvals or rejections",
        "children": [
          {
            "name": "comment",
            "type": "string",
            "description": ""
          },
          {
            "name": "created_at_millis",
            "type": "integer",
            "description": "When the review was submitted, in epoch milliseconds"
          },
          {
            "name": "review_state",
            "type": "string",
            "description": "Review outcome (APPROVED, PENDING, REJECTED)"
          },
          {
            "name": "review_sub_reason",
            "type": "string",
            "description": "Specified when the review was not explicitly made by a user (AUTO_APPROVED, BACKFILLED)"
          },
          {
            "name": "reviewer_collaborator_alias",
            "type": "string",
            "description": "Collaborator alias of the reviewer"
          }
        ]
      },
      {
        "name": "runner_collaborator_aliases",
        "type": "array",
        "description": "Aliases of collaborators that can run the notebook."
      }
    ]
  },
  {
    "name": "owner_collaborator_alias",
    "type": "string",
    "description": "The alias of the collaborator who owns this asset"
  },
  {
    "name": "status",
    "type": "string",
    "description": "Status of the asset (ACTIVE, PENDING, PERMISSION_DENIED)"
  },
  {
    "name": "table",
    "type": "object",
    "description": "Table details available to all collaborators of the clean room. Present if and only if **asset_type** is **TABLE**",
    "children": [
      {
        "name": "columns",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "table_local_details",
    "type": "object",
    "description": "Local details for a table that are only available to its owner. Present if and only if **asset_type** is **TABLE**",
    "children": [
      {
        "name": "local_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "partitions",
        "type": "string",
        "description": "Partition filtering specification for a shared table."
      }
    ]
  },
  {
    "name": "view",
    "type": "object",
    "description": "View details available to all collaborators of the clean room. Present if and only if **asset_type** is **VIEW**",
    "children": [
      {
        "name": "columns",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "view_local_details",
    "type": "object",
    "description": "Local details for a view that are only available to its owner. Present if and only if **asset_type** is **VIEW**",
    "children": [
      {
        "name": "local_name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "volume_local_details",
    "type": "object",
    "description": "Local details for a volume that are only available to its owner. Present if and only if **asset_type** is **VOLUME**",
    "children": [
      {
        "name": "local_name",
        "type": "string",
        "description": ""
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[]} />
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
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-asset_type.value"><code>asset_type.value</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-asset_type"><code>asset_type</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Get the details of a clean room asset by its type and full name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List assets.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-asset"><code>asset</code></a></td>
    <td></td>
    <td>Create a clean room asset —share an asset like a notebook or table into the clean room. For each UC</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-asset_type.value"><code>asset_type.value</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-asset_type"><code>asset_type</code></a>, <a href="#parameter-asset"><code>asset</code></a></td>
    <td></td>
    <td>Update a clean room asset. For example, updating the content of a notebook; changing the shared</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-asset_type.value"><code>asset_type.value</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-asset_type"><code>asset_type</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Delete a clean room asset - unshare/remove the asset from the clean room</td>
</tr>
<tr>
    <td><a href="#review"><CopyableCode code="review" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-asset_type.value"><code>asset_type.value</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-asset_type"><code>asset_type</code></a></td>
    <td></td>
    <td>Submit an asset review</td>
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
<tr id="parameter-asset_type">
    <td><CopyableCode code="asset_type" /></td>
    <td><code>string</code></td>
    <td>The type of the asset.</td>
</tr>
<tr id="parameter-asset_type.value">
    <td><CopyableCode code="asset_type.value" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-clean_room_name">
    <td><CopyableCode code="clean_room_name" /></td>
    <td><code>string</code></td>
    <td>Name of the clean room</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the asset</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on previous query.</td>
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

Get the details of a clean room asset by its type and full name.

```sql
SELECT
name,
clean_room_name,
added_at,
asset_type,
foreign_table,
foreign_table_local_details,
notebook,
owner_collaborator_alias,
status,
table,
table_local_details,
view,
view_local_details,
volume_local_details
FROM databricks_workspace.cleanrooms.assets
WHERE clean_room_name = '{{ clean_room_name }}' -- required
AND asset_type.value = '{{ asset_type.value }}' -- required
AND name = '{{ name }}' -- required
AND asset_type = '{{ asset_type }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

List assets.

```sql
SELECT
*
FROM databricks_workspace.cleanrooms.assets
WHERE clean_room_name = '{{ clean_room_name }}' -- required
AND workspace = '{{ workspace }}' -- required
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

Create a clean room asset —share an asset like a notebook or table into the clean room. For each UC

```sql
INSERT INTO databricks_workspace.cleanrooms.assets (
asset,
clean_room_name,
workspace
)
SELECT 
'{{ asset }}' /* required */,
'{{ clean_room_name }}',
'{{ workspace }}'
RETURNING
name,
clean_room_name,
added_at,
asset_type,
foreign_table,
foreign_table_local_details,
notebook,
owner_collaborator_alias,
status,
table,
table_local_details,
view,
view_local_details,
volume_local_details
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: assets
  props:
    - name: clean_room_name
      value: "{{ clean_room_name }}"
      description: Required parameter for the assets resource.
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the assets resource.
    - name: asset
      description: |
        :returns: :class:\`CleanRoomAsset\`
      value:
        name: "{{ name }}"
        asset_type: "{{ asset_type }}"
        added_at: {{ added_at }}
        clean_room_name: "{{ clean_room_name }}"
        foreign_table:
          columns: "{{ columns }}"
        foreign_table_local_details:
          local_name: "{{ local_name }}"
        notebook:
          notebook_content: "{{ notebook_content }}"
          etag: "{{ etag }}"
          review_state: "{{ review_state }}"
          reviews:
            - comment: "{{ comment }}"
              created_at_millis: {{ created_at_millis }}
              review_state: "{{ review_state }}"
              review_sub_reason: "{{ review_sub_reason }}"
              reviewer_collaborator_alias: "{{ reviewer_collaborator_alias }}"
          runner_collaborator_aliases:
            - "{{ runner_collaborator_aliases }}"
        owner_collaborator_alias: "{{ owner_collaborator_alias }}"
        status: "{{ status }}"
        table:
          columns: "{{ columns }}"
        table_local_details:
          local_name: "{{ local_name }}"
          partitions: "{{ partitions }}"
        view:
          columns: "{{ columns }}"
        view_local_details:
          local_name: "{{ local_name }}"
        volume_local_details:
          local_name: "{{ local_name }}"
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

Update a clean room asset. For example, updating the content of a notebook; changing the shared

```sql
UPDATE databricks_workspace.cleanrooms.assets
SET 
asset_type = '{{ asset_type }}',
asset = '{{ asset }}'
WHERE 
clean_room_name = '{{ clean_room_name }}' --required
AND asset_type.value = '{{ asset_type.value }}' --required
AND name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
AND asset_type = '{{ asset_type }}' --required
AND asset = '{{ asset }}' --required
RETURNING
name,
clean_room_name,
added_at,
asset_type,
foreign_table,
foreign_table_local_details,
notebook,
owner_collaborator_alias,
status,
table,
table_local_details,
view,
view_local_details,
volume_local_details;
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

Delete a clean room asset - unshare/remove the asset from the clean room

```sql
DELETE FROM databricks_workspace.cleanrooms.assets
WHERE clean_room_name = '{{ clean_room_name }}' --required
AND asset_type.value = '{{ asset_type.value }}' --required
AND name = '{{ name }}' --required
AND asset_type = '{{ asset_type }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="review"
    values={[
        { label: 'review', value: 'review' }
    ]}
>
<TabItem value="review">

Submit an asset review

```sql
EXEC databricks_workspace.cleanrooms.assets.review 
@clean_room_name='{{ clean_room_name }}' --required, 
@asset_type.value='{{ asset_type.value }}' --required, 
@name='{{ name }}' --required, 
@workspace='{{ workspace }}' --required 
@@json=
'{
"asset_type": "{{ asset_type }}", 
"notebook_review": "{{ notebook_review }}"
}'
;
```
</TabItem>
</Tabs>

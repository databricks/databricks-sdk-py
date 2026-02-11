---
title: asset_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - asset_revisions
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists an <code>asset_revisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asset_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.cleanrooms.asset_revisions" /></td></tr>
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
    "description": "The type of the asset."
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
        "description": "Top-level status derived from all reviews"
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
            "description": "Review outcome"
          },
          {
            "name": "review_sub_reason",
            "type": "string",
            "description": "Specified when the review was not explicitly made by a user"
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
    "description": "Status of the asset"
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
    "description": "The type of the asset."
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
        "description": "Top-level status derived from all reviews"
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
            "description": "Review outcome"
          },
          {
            "name": "review_sub_reason",
            "type": "string",
            "description": "Specified when the review was not explicitly made by a user"
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
    "description": "Status of the asset"
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
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-asset_type.value"><code>asset_type.value</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-etag"><code>etag</code></a>, <a href="#parameter-asset_type"><code>asset_type</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a specific revision of an asset<br /><br />:param clean_room_name: str<br />  Name of the clean room.<br />:param asset_type: :class:`CleanRoomAssetAssetType`<br />  Asset type. Only NOTEBOOK_FILE is supported.<br />:param name: str<br />  Name of the asset.<br />:param etag: str<br />  Revision etag to fetch. If not provided, the latest revision will be returned.<br /><br />:returns: :class:`CleanRoomAsset`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-asset_type.value"><code>asset_type.value</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-asset_type"><code>asset_type</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List revisions for an asset<br /><br />:param clean_room_name: str<br />  Name of the clean room.<br />:param asset_type: :class:`CleanRoomAssetAssetType`<br />  Asset type. Only NOTEBOOK_FILE is supported.<br />:param name: str<br />  Name of the asset.<br />:param page_size: int (optional)<br />  Maximum number of asset revisions to return. Defaults to 10.<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on the previous query.<br /><br />:returns: Iterator over :class:`CleanRoomAsset`</td>
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
    <td>Asset type. Only NOTEBOOK_FILE is supported.</td>
</tr>
<tr id="parameter-asset_type.value">
    <td><CopyableCode code="asset_type.value" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-clean_room_name">
    <td><CopyableCode code="clean_room_name" /></td>
    <td><code>string</code></td>
    <td>Name of the clean room.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-etag">
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Revision etag to fetch. If not provided, the latest revision will be returned.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the asset.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>Maximum number of asset revisions to return. Defaults to 10.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on the previous query.</td>
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

Get a specific revision of an asset<br /><br />:param clean_room_name: str<br />  Name of the clean room.<br />:param asset_type: :class:`CleanRoomAssetAssetType`<br />  Asset type. Only NOTEBOOK_FILE is supported.<br />:param name: str<br />  Name of the asset.<br />:param etag: str<br />  Revision etag to fetch. If not provided, the latest revision will be returned.<br /><br />:returns: :class:`CleanRoomAsset`

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
FROM databricks_workspace.cleanrooms.asset_revisions
WHERE clean_room_name = '{{ clean_room_name }}' -- required
AND asset_type.value = '{{ asset_type.value }}' -- required
AND name = '{{ name }}' -- required
AND etag = '{{ etag }}' -- required
AND asset_type = '{{ asset_type }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List revisions for an asset<br /><br />:param clean_room_name: str<br />  Name of the clean room.<br />:param asset_type: :class:`CleanRoomAssetAssetType`<br />  Asset type. Only NOTEBOOK_FILE is supported.<br />:param name: str<br />  Name of the asset.<br />:param page_size: int (optional)<br />  Maximum number of asset revisions to return. Defaults to 10.<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on the previous query.<br /><br />:returns: Iterator over :class:`CleanRoomAsset`

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
FROM databricks_workspace.cleanrooms.asset_revisions
WHERE clean_room_name = '{{ clean_room_name }}' -- required
AND asset_type.value = '{{ asset_type.value }}' -- required
AND name = '{{ name }}' -- required
AND asset_type = '{{ asset_type }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>

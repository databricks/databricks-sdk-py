---
title: genie
hide_title: false
hide_table_of_contents: false
keywords:
  - genie
  - dashboards
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

Creates, updates, deletes, gets or lists a <code>genie</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="genie" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dashboards.genie" /></td></tr>
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
    "name": "space_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "warehouse_id",
    "type": "string",
    "description": "Warehouse associated with the Genie Space"
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of the Genie Space"
  },
  {
    "name": "serialized_space",
    "type": "string",
    "description": "The contents of the Genie Space in serialized string form. This field is excluded in List Genie spaces responses. Use the [Get Genie Space](:method:genie/getspace) API to retrieve an example response, which includes the `serialized_space` field. This field provides the structure of the JSON string that represents the space's layout and components."
  },
  {
    "name": "title",
    "type": "string",
    "description": "Title of the Genie Space"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "next_page_token",
    "type": "string",
    "description": ""
  },
  {
    "name": "spaces",
    "type": "array",
    "description": "List of Genie spaces",
    "children": [
      {
        "name": "space_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "title",
        "type": "string",
        "description": "Title of the Genie Space"
      },
      {
        "name": "description",
        "type": "string",
        "description": "Description of the Genie Space"
      },
      {
        "name": "serialized_space",
        "type": "string",
        "description": "The contents of the Genie Space in serialized string form. This field is excluded in List Genie spaces responses. Use the [Get Genie Space](:method:genie/getspace) API to retrieve an example response, which includes the `serialized_space` field. This field provides the structure of the JSON string that represents the space's layout and components."
      },
      {
        "name": "warehouse_id",
        "type": "string",
        "description": "Warehouse associated with the Genie Space"
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
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-include_serialized_space"><code>include_serialized_space</code></a></td>
    <td>Get details of a Genie Space.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Get list of Genie Spaces.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-warehouse_id"><code>warehouse_id</code></a>, <a href="#parameter-serialized_space"><code>serialized_space</code></a></td>
    <td></td>
    <td>Creates a Genie space from a serialized payload.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Updates a Genie space with a serialized payload.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Move a Genie Space to the trash.</td>
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
<tr id="parameter-space_id">
    <td><CopyableCode code="space_id" /></td>
    <td><code>string</code></td>
    <td>The ID associated with the Genie space to be sent to the trash.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-include_serialized_space">
    <td><CopyableCode code="include_serialized_space" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include the serialized space export in the response. Requires at least CAN EDIT permission on the space.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of spaces to return per page</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token for getting the next page of results</td>
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

Get details of a Genie Space.

```sql
SELECT
space_id,
warehouse_id,
description,
serialized_space,
title
FROM databricks_workspace.dashboards.genie
WHERE space_id = '{{ space_id }}' -- required
AND workspace = '{{ workspace }}' -- required
AND include_serialized_space = '{{ include_serialized_space }}'
;
```
</TabItem>
<TabItem value="list">

Get list of Genie Spaces.

```sql
SELECT
next_page_token,
spaces
FROM databricks_workspace.dashboards.genie
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

Creates a Genie space from a serialized payload.

```sql
INSERT INTO databricks_workspace.dashboards.genie (
warehouse_id,
serialized_space,
description,
parent_path,
title,
workspace
)
SELECT 
'{{ warehouse_id }}' /* required */,
'{{ serialized_space }}' /* required */,
'{{ description }}',
'{{ parent_path }}',
'{{ title }}',
'{{ workspace }}'
RETURNING
space_id,
warehouse_id,
description,
serialized_space,
title
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: genie
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the genie resource.
    - name: warehouse_id
      value: "{{ warehouse_id }}"
      description: |
        Warehouse to associate with the new space
    - name: serialized_space
      value: "{{ serialized_space }}"
      description: |
        The contents of the Genie Space in serialized string form. Use the [Get Genie Space](:method:genie/getspace) API to retrieve an example response, which includes the \`serialized_space\` field. This field provides the structure of the JSON string that represents the space's layout and components.
    - name: description
      value: "{{ description }}"
      description: |
        Optional description
    - name: parent_path
      value: "{{ parent_path }}"
      description: |
        Parent folder path where the space will be registered
    - name: title
      value: "{{ title }}"
      description: |
        Optional title override
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

Updates a Genie space with a serialized payload.

```sql
UPDATE databricks_workspace.dashboards.genie
SET 
description = '{{ description }}',
serialized_space = '{{ serialized_space }}',
title = '{{ title }}',
warehouse_id = '{{ warehouse_id }}'
WHERE 
space_id = '{{ space_id }}' --required
AND workspace = '{{ workspace }}' --required
RETURNING
space_id,
warehouse_id,
description,
serialized_space,
title;
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

Move a Genie Space to the trash.

```sql
DELETE FROM databricks_workspace.dashboards.genie
WHERE space_id = '{{ space_id }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

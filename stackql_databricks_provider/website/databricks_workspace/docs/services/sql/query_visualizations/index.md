---
title: query_visualizations
hide_title: false
hide_table_of_contents: false
keywords:
  - query_visualizations
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

Creates, updates, deletes, gets or lists a <code>query_visualizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>query_visualizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.query_visualizations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "UUID identifying the visualization."
  },
  {
    "name": "query_id",
    "type": "string",
    "description": "UUID of the query that the visualization is attached to."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "The display name of the visualization."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": ""
  },
  {
    "name": "serialized_options",
    "type": "string",
    "description": "The visualization options varies widely from one visualization type to the next and is unsupported. Databricks does not recommend modifying visualization options directly."
  },
  {
    "name": "serialized_query_plan",
    "type": "string",
    "description": "The visualization query plan varies widely from one visualization type to the next and is unsupported. Databricks does not recommend modifying the visualization query plan directly."
  },
  {
    "name": "type",
    "type": "string",
    "description": "The type of visualization: counter, table, funnel, and so on."
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "The timestamp indicating when the visualization was updated."
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets a list of visualizations on a query.<br /><br />:param id: str<br />:param page_size: int (optional)<br />:param page_token: str (optional)<br /><br />:returns: Iterator over :class:`Visualization`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Adds a visualization to a query.<br /><br />:param visualization: :class:`CreateVisualizationRequestVisualization` (optional)<br /><br />:returns: :class:`Visualization`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__update_mask"><code>data__update_mask</code></a></td>
    <td></td>
    <td>Updates a visualization.<br /><br />:param id: str<br />:param update_mask: str<br />  The field mask must be a single string, with multiple fields separated by commas (no spaces). The<br />  field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,<br />  `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only<br />  the entire collection field can be specified. Field names must exactly match the resource field<br />  names.<br /><br />  A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the<br />  fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API<br />  changes in the future.<br />:param visualization: :class:`UpdateVisualizationRequestVisualization` (optional)<br /><br />:returns: :class:`Visualization`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Removes a visualization.<br /><br />:param id: str</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>str</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>:returns: Iterator over :class:`Visualization`</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Gets a list of visualizations on a query.<br /><br />:param id: str<br />:param page_size: int (optional)<br />:param page_token: str (optional)<br /><br />:returns: Iterator over :class:`Visualization`

```sql
SELECT
id,
query_id,
display_name,
create_time,
serialized_options,
serialized_query_plan,
type,
update_time
FROM databricks_workspace.sql.query_visualizations
WHERE id = '{{ id }}' -- required
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

Adds a visualization to a query.<br /><br />:param visualization: :class:`CreateVisualizationRequestVisualization` (optional)<br /><br />:returns: :class:`Visualization`

```sql
INSERT INTO databricks_workspace.sql.query_visualizations (
data__visualization,
deployment_name
)
SELECT 
'{{ visualization }}',
'{{ deployment_name }}'
RETURNING
id,
query_id,
display_name,
create_time,
serialized_options,
serialized_query_plan,
type,
update_time
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: query_visualizations
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the query_visualizations resource.
    - name: visualization
      value: string
      description: |
        :returns: :class:`Visualization`
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

Updates a visualization.<br /><br />:param id: str<br />:param update_mask: str<br />  The field mask must be a single string, with multiple fields separated by commas (no spaces). The<br />  field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,<br />  `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only<br />  the entire collection field can be specified. Field names must exactly match the resource field<br />  names.<br /><br />  A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the<br />  fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API<br />  changes in the future.<br />:param visualization: :class:`UpdateVisualizationRequestVisualization` (optional)<br /><br />:returns: :class:`Visualization`

```sql
UPDATE databricks_workspace.sql.query_visualizations
SET 
data__update_mask = '{{ update_mask }}',
data__visualization = '{{ visualization }}'
WHERE 
id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__update_mask = '{{ update_mask }}' --required
RETURNING
id,
query_id,
display_name,
create_time,
serialized_options,
serialized_query_plan,
type,
update_time;
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

Removes a visualization.<br /><br />:param id: str

```sql
DELETE FROM databricks_workspace.sql.query_visualizations
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

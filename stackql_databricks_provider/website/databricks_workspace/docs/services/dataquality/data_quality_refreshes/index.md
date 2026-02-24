---
title: data_quality_refreshes
hide_title: false
hide_table_of_contents: false
keywords:
  - data_quality_refreshes
  - dataquality
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

Creates, updates, deletes, gets or lists a <code>data_quality_refreshes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_quality_refreshes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dataquality.data_quality_refreshes" /></td></tr>
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
    "name": "object_id",
    "type": "string",
    "description": "The UUID of the request object. It is `schema_id` for `schema`, and `table_id` for `table`. Find the `schema_id` from either: 1. The [schema_id] of the `Schemas` resource. 2. In [Catalog Explorer] &gt; select the `schema` &gt; go to the `Details` tab &gt; the `Schema ID` field. Find the `table_id` from either: 1. The [table_id] of the `Tables` resource. 2. In [Catalog Explorer] &gt; select the `table` &gt; go to the `Details` tab &gt; the `Table ID` field. [Catalog Explorer]: https://docs.databricks.com/aws/en/catalog-explorer/ [schema_id]: https://docs.databricks.com/api/workspace/schemas/get#schema_id [table_id]: https://docs.databricks.com/api/workspace/tables/get#table_id"
  },
  {
    "name": "refresh_id",
    "type": "integer",
    "description": "Unique id of the refresh operation."
  },
  {
    "name": "end_time_ms",
    "type": "integer",
    "description": "Time when the refresh ended (milliseconds since 1/1/1970 UTC)."
  },
  {
    "name": "message",
    "type": "string",
    "description": "An optional message to give insight into the current state of the refresh (e.g. FAILURE messages)."
  },
  {
    "name": "object_type",
    "type": "string",
    "description": "The type of the monitored object. Can be one of the following: `schema`or `table`."
  },
  {
    "name": "start_time_ms",
    "type": "integer",
    "description": "Time when the refresh started (milliseconds since 1/1/1970 UTC)."
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current state of the refresh. (MONITOR_REFRESH_STATE_CANCELED, MONITOR_REFRESH_STATE_FAILED, MONITOR_REFRESH_STATE_PENDING, MONITOR_REFRESH_STATE_RUNNING, MONITOR_REFRESH_STATE_SUCCESS, MONITOR_REFRESH_STATE_UNKNOWN)"
  },
  {
    "name": "trigger",
    "type": "string",
    "description": "What triggered the refresh. (MONITOR_REFRESH_TRIGGER_DATA_CHANGE, MONITOR_REFRESH_TRIGGER_MANUAL, MONITOR_REFRESH_TRIGGER_SCHEDULE, MONITOR_REFRESH_TRIGGER_UNKNOWN)"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "object_id",
    "type": "string",
    "description": "The UUID of the request object. It is `schema_id` for `schema`, and `table_id` for `table`. Find the `schema_id` from either: 1. The [schema_id] of the `Schemas` resource. 2. In [Catalog Explorer] &gt; select the `schema` &gt; go to the `Details` tab &gt; the `Schema ID` field. Find the `table_id` from either: 1. The [table_id] of the `Tables` resource. 2. In [Catalog Explorer] &gt; select the `table` &gt; go to the `Details` tab &gt; the `Table ID` field. [Catalog Explorer]: https://docs.databricks.com/aws/en/catalog-explorer/ [schema_id]: https://docs.databricks.com/api/workspace/schemas/get#schema_id [table_id]: https://docs.databricks.com/api/workspace/tables/get#table_id"
  },
  {
    "name": "refresh_id",
    "type": "integer",
    "description": "Unique id of the refresh operation."
  },
  {
    "name": "end_time_ms",
    "type": "integer",
    "description": "Time when the refresh ended (milliseconds since 1/1/1970 UTC)."
  },
  {
    "name": "message",
    "type": "string",
    "description": "An optional message to give insight into the current state of the refresh (e.g. FAILURE messages)."
  },
  {
    "name": "object_type",
    "type": "string",
    "description": "The type of the monitored object. Can be one of the following: `schema`or `table`."
  },
  {
    "name": "start_time_ms",
    "type": "integer",
    "description": "Time when the refresh started (milliseconds since 1/1/1970 UTC)."
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current state of the refresh. (MONITOR_REFRESH_STATE_CANCELED, MONITOR_REFRESH_STATE_FAILED, MONITOR_REFRESH_STATE_PENDING, MONITOR_REFRESH_STATE_RUNNING, MONITOR_REFRESH_STATE_SUCCESS, MONITOR_REFRESH_STATE_UNKNOWN)"
  },
  {
    "name": "trigger",
    "type": "string",
    "description": "What triggered the refresh. (MONITOR_REFRESH_TRIGGER_DATA_CHANGE, MONITOR_REFRESH_TRIGGER_MANUAL, MONITOR_REFRESH_TRIGGER_SCHEDULE, MONITOR_REFRESH_TRIGGER_UNKNOWN)"
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
    <td><a href="#parameter-object_type"><code>object_type</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-refresh_id"><code>refresh_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Get data quality monitor refresh. The call must be made in the same workspace as where the monitor was</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-object_type"><code>object_type</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List data quality monitor refreshes. The call must be made in the same workspace as where the monitor</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-object_type"><code>object_type</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-refresh"><code>refresh</code></a></td>
    <td></td>
    <td>Creates a refresh. Currently only supported for the `table` `object_type`. The call must be made in</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-object_type"><code>object_type</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-refresh_id"><code>refresh_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-refresh"><code>refresh</code></a></td>
    <td></td>
    <td>(Unimplemented) Update a refresh</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-object_type"><code>object_type</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-refresh_id"><code>refresh_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>(Unimplemented) Delete a refresh</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-object_type"><code>object_type</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-refresh_id"><code>refresh_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Cancels a data quality monitor refresh. Currently only supported for the `table` `object_type`. The</td>
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
<tr id="parameter-object_id">
    <td><CopyableCode code="object_id" /></td>
    <td><code>string</code></td>
    <td>The UUID of the request object. It is `schema_id` for `schema`, and `table_id` for `table`. Find the `schema_id` from either: 1. The [schema_id] of the `Schemas` resource. 2. In [Catalog Explorer] &gt; select the `schema` &gt; go to the `Details` tab &gt; the `Schema ID` field. Find the `table_id` from either: 1. The [table_id] of the `Tables` resource. 2. In [Catalog Explorer] &gt; select the `table` &gt; go to the `Details` tab &gt; the `Table ID` field. [Catalog Explorer]: https://docs.databricks.com/aws/en/catalog-explorer/ [schema_id]: https://docs.databricks.com/api/workspace/schemas/get#schema_id [table_id]: https://docs.databricks.com/api/workspace/tables/get#table_id</td>
</tr>
<tr id="parameter-object_type">
    <td><CopyableCode code="object_type" /></td>
    <td><code>string</code></td>
    <td>The type of the monitored object. Can be one of the following: `schema` or `table`.</td>
</tr>
<tr id="parameter-refresh_id">
    <td><CopyableCode code="refresh_id" /></td>
    <td><code>integer</code></td>
    <td>Unique id of the refresh operation.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>The field mask to specify which fields to update.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>:param page_token: str (optional)</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td></td>
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

Get data quality monitor refresh. The call must be made in the same workspace as where the monitor was

```sql
SELECT
object_id,
refresh_id,
end_time_ms,
message,
object_type,
start_time_ms,
state,
trigger
FROM databricks_workspace.dataquality.data_quality_refreshes
WHERE object_type = '{{ object_type }}' -- required
AND object_id = '{{ object_id }}' -- required
AND refresh_id = '{{ refresh_id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

List data quality monitor refreshes. The call must be made in the same workspace as where the monitor

```sql
SELECT
object_id,
refresh_id,
end_time_ms,
message,
object_type,
start_time_ms,
state,
trigger
FROM databricks_workspace.dataquality.data_quality_refreshes
WHERE object_type = '{{ object_type }}' -- required
AND object_id = '{{ object_id }}' -- required
AND workspace = '{{ workspace }}' -- required
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

Creates a refresh. Currently only supported for the `table` `object_type`. The call must be made in

```sql
INSERT INTO databricks_workspace.dataquality.data_quality_refreshes (
refresh,
object_type,
object_id,
workspace
)
SELECT 
'{{ refresh }}' /* required */,
'{{ object_type }}',
'{{ object_id }}',
'{{ workspace }}'
RETURNING
object_id,
refresh_id,
end_time_ms,
message,
object_type,
start_time_ms,
state,
trigger
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: data_quality_refreshes
  props:
    - name: object_type
      value: string
      description: Required parameter for the data_quality_refreshes resource.
    - name: object_id
      value: string
      description: Required parameter for the data_quality_refreshes resource.
    - name: workspace
      value: string
      description: Required parameter for the data_quality_refreshes resource.
    - name: refresh
      value: object
      description: |
        The refresh to create
      props:
      - name: object_type
        value: string
        description: |
          The type of the monitored object. Can be one of the following: `schema`or `table`.
      - name: object_id
        value: string
        description: |
          The UUID of the request object. It is `schema_id` for `schema`, and `table_id` for `table`. Find the `schema_id` from either: 1. The [schema_id] of the `Schemas` resource. 2. In [Catalog Explorer] > select the `schema` > go to the `Details` tab > the `Schema ID` field. Find the `table_id` from either: 1. The [table_id] of the `Tables` resource. 2. In [Catalog Explorer] > select the `table` > go to the `Details` tab > the `Table ID` field. [Catalog Explorer]: https://docs.databricks.com/aws/en/catalog-explorer/ [schema_id]: https://docs.databricks.com/api/workspace/schemas/get#schema_id [table_id]: https://docs.databricks.com/api/workspace/tables/get#table_id
      - name: end_time_ms
        value: integer
        description: |
          Time when the refresh ended (milliseconds since 1/1/1970 UTC).
      - name: message
        value: string
        description: |
          An optional message to give insight into the current state of the refresh (e.g. FAILURE messages).
      - name: refresh_id
        value: integer
        description: |
          Unique id of the refresh operation.
      - name: start_time_ms
        value: integer
        description: |
          Time when the refresh started (milliseconds since 1/1/1970 UTC).
      - name: state
        value: string
        description: |
          The current state of the refresh.
      - name: trigger
        value: string
        description: |
          What triggered the refresh.
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

(Unimplemented) Update a refresh

```sql
UPDATE databricks_workspace.dataquality.data_quality_refreshes
SET 
refresh = '{{ refresh }}'
WHERE 
object_type = '{{ object_type }}' --required
AND object_id = '{{ object_id }}' --required
AND refresh_id = '{{ refresh_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND workspace = '{{ workspace }}' --required
AND refresh = '{{ refresh }}' --required
RETURNING
object_id,
refresh_id,
end_time_ms,
message,
object_type,
start_time_ms,
state,
trigger;
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

(Unimplemented) Delete a refresh

```sql
DELETE FROM databricks_workspace.dataquality.data_quality_refreshes
WHERE object_type = '{{ object_type }}' --required
AND object_id = '{{ object_id }}' --required
AND refresh_id = '{{ refresh_id }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="cancel">

Cancels a data quality monitor refresh. Currently only supported for the `table` `object_type`. The

```sql
EXEC databricks_workspace.dataquality.data_quality_refreshes.cancel 
@object_type='{{ object_type }}' --required, 
@object_id='{{ object_id }}' --required, 
@refresh_id='{{ refresh_id }}' --required, 
@workspace='{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

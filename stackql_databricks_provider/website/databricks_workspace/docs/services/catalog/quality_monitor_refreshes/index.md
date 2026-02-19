---
title: quality_monitor_refreshes
hide_title: false
hide_table_of_contents: false
keywords:
  - quality_monitor_refreshes
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

Creates, updates, deletes, gets or lists a <code>quality_monitor_refreshes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="quality_monitor_refreshes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.quality_monitor_refreshes" /></td></tr>
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
    "name": "refresh_id",
    "type": "integer",
    "description": ""
  },
  {
    "name": "end_time_ms",
    "type": "integer",
    "description": "Time at which refresh operation completed (milliseconds since 1/1/1970 UTC)."
  },
  {
    "name": "message",
    "type": "string",
    "description": "An optional message to give insight into the current state of the job (e.g. FAILURE messages)."
  },
  {
    "name": "start_time_ms",
    "type": "integer",
    "description": "Time at which refresh operation was initiated (milliseconds since 1/1/1970 UTC)."
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current state of the refresh. (CANCELED, FAILED, PENDING, RUNNING, SUCCESS, UNKNOWN)"
  },
  {
    "name": "trigger",
    "type": "string",
    "description": "The method by which the refresh was triggered. (MANUAL, SCHEDULE, UNKNOWN_TRIGGER)"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "refreshes",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "refresh_id",
        "type": "integer",
        "description": ""
      },
      {
        "name": "state",
        "type": "string",
        "description": "The current state of the refresh. (CANCELED, FAILED, PENDING, RUNNING, SUCCESS, UNKNOWN)"
      },
      {
        "name": "start_time_ms",
        "type": "integer",
        "description": "Time at which refresh operation was initiated (milliseconds since 1/1/1970 UTC)."
      },
      {
        "name": "end_time_ms",
        "type": "integer",
        "description": "Time at which refresh operation completed (milliseconds since 1/1/1970 UTC)."
      },
      {
        "name": "message",
        "type": "string",
        "description": "An optional message to give insight into the current state of the job (e.g. FAILURE messages)."
      },
      {
        "name": "trigger",
        "type": "string",
        "description": "The method by which the refresh was triggered. (MANUAL, SCHEDULE, UNKNOWN_TRIGGER)"
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
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-refresh_id"><code>refresh_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>[DEPRECATED] Gets info about a specific monitor refresh using the given refresh ID. Use Data Quality</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>[DEPRECATED] Gets an array containing the history of the most recent refreshes (up to 25) for this</td>
</tr>
<tr>
    <td><a href="#run"><CopyableCode code="run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>[DEPRECATED] Queues a metric refresh on the monitor for the specified table. Use Data Quality Monitors</td>
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
<tr id="parameter-refresh_id">
    <td><CopyableCode code="refresh_id" /></td>
    <td><code>integer</code></td>
    <td>ID of the refresh.</td>
</tr>
<tr id="parameter-table_name">
    <td><CopyableCode code="table_name" /></td>
    <td><code>string</code></td>
    <td>UC table name in format `catalog.schema.table_name`. table_name is case insensitive and spaces are disallowed.</td>
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

[DEPRECATED] Gets info about a specific monitor refresh using the given refresh ID. Use Data Quality

```sql
SELECT
refresh_id,
end_time_ms,
message,
start_time_ms,
state,
trigger
FROM databricks_workspace.catalog.quality_monitor_refreshes
WHERE table_name = '{{ table_name }}' -- required
AND refresh_id = '{{ refresh_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

[DEPRECATED] Gets an array containing the history of the most recent refreshes (up to 25) for this

```sql
SELECT
refreshes
FROM databricks_workspace.catalog.quality_monitor_refreshes
WHERE table_name = '{{ table_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="run"
    values={[
        { label: 'run', value: 'run' }
    ]}
>
<TabItem value="run">

[DEPRECATED] Queues a metric refresh on the monitor for the specified table. Use Data Quality Monitors

```sql
EXEC databricks_workspace.catalog.quality_monitor_refreshes.run 
@table_name='{{ table_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

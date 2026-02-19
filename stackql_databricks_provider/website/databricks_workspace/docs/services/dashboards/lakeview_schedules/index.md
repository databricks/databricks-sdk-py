---
title: lakeview_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - lakeview_schedules
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>lakeview_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lakeview_schedules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dashboards.lakeview_schedules" /></td></tr>
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
    "name": "dashboard_id",
    "type": "string",
    "description": "UUID identifying the dashboard to which the schedule belongs."
  },
  {
    "name": "schedule_id",
    "type": "string",
    "description": "UUID identifying the schedule."
  },
  {
    "name": "warehouse_id",
    "type": "string",
    "description": "The warehouse id to run the dashboard with for the schedule."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "The display name for schedule."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "A timestamp indicating when the schedule was created."
  },
  {
    "name": "cron_schedule",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "quartz_cron_expression",
        "type": "string",
        "description": ""
      },
      {
        "name": "timezone_id",
        "type": "string",
        "description": "A Java timezone id. The schedule will be resolved with respect to this timezone. See [Java TimeZone] for details. [Java TimeZone]: https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html"
      }
    ]
  },
  {
    "name": "etag",
    "type": "string",
    "description": "The etag for the schedule. Must be left empty on create, must be provided on updates to ensure that the schedule has not been modified since the last read, and can be optionally provided on delete."
  },
  {
    "name": "pause_status",
    "type": "string",
    "description": "The status indicates whether this schedule is paused or not. (PAUSED, UNPAUSED)"
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "A timestamp indicating when the schedule was last updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "dashboard_id",
    "type": "string",
    "description": "UUID identifying the dashboard to which the schedule belongs."
  },
  {
    "name": "schedule_id",
    "type": "string",
    "description": "UUID identifying the schedule."
  },
  {
    "name": "warehouse_id",
    "type": "string",
    "description": "The warehouse id to run the dashboard with for the schedule."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "The display name for schedule."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "A timestamp indicating when the schedule was created."
  },
  {
    "name": "cron_schedule",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "quartz_cron_expression",
        "type": "string",
        "description": ""
      },
      {
        "name": "timezone_id",
        "type": "string",
        "description": "A Java timezone id. The schedule will be resolved with respect to this timezone. See [Java TimeZone] for details. [Java TimeZone]: https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html"
      }
    ]
  },
  {
    "name": "etag",
    "type": "string",
    "description": "The etag for the schedule. Must be left empty on create, must be provided on updates to ensure that the schedule has not been modified since the last read, and can be optionally provided on delete."
  },
  {
    "name": "pause_status",
    "type": "string",
    "description": "The status indicates whether this schedule is paused or not. (PAUSED, UNPAUSED)"
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "A timestamp indicating when the schedule was last updated."
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
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-schedule_id"><code>schedule_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get dashboard schedule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List dashboard schedules.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-schedule"><code>schedule</code></a></td>
    <td></td>
    <td>Create dashboard schedule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-schedule_id"><code>schedule_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Delete dashboard schedule.</td>
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
<tr id="parameter-dashboard_id">
    <td><CopyableCode code="dashboard_id" /></td>
    <td><code>string</code></td>
    <td>UUID identifying the dashboard to which the schedule belongs.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-schedule_id">
    <td><CopyableCode code="schedule_id" /></td>
    <td><code>string</code></td>
    <td>UUID identifying the schedule.</td>
</tr>
<tr id="parameter-etag">
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the schedule. Optionally, it can be provided to verify that the schedule has not been modified from its last retrieval.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>The number of schedules to return per page.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous `ListSchedules` call. Use this to retrieve the subsequent page.</td>
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

Get dashboard schedule.

```sql
SELECT
dashboard_id,
schedule_id,
warehouse_id,
display_name,
create_time,
cron_schedule,
etag,
pause_status,
update_time
FROM databricks_workspace.dashboards.lakeview_schedules
WHERE dashboard_id = '{{ dashboard_id }}' -- required
AND schedule_id = '{{ schedule_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List dashboard schedules.

```sql
SELECT
dashboard_id,
schedule_id,
warehouse_id,
display_name,
create_time,
cron_schedule,
etag,
pause_status,
update_time
FROM databricks_workspace.dashboards.lakeview_schedules
WHERE dashboard_id = '{{ dashboard_id }}' -- required
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

Create dashboard schedule.

```sql
INSERT INTO databricks_workspace.dashboards.lakeview_schedules (
schedule,
dashboard_id,
deployment_name
)
SELECT 
'{{ schedule }}' /* required */,
'{{ dashboard_id }}',
'{{ deployment_name }}'
RETURNING
dashboard_id,
schedule_id,
warehouse_id,
display_name,
create_time,
cron_schedule,
etag,
pause_status,
update_time
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: lakeview_schedules
  props:
    - name: dashboard_id
      value: string
      description: Required parameter for the lakeview_schedules resource.
    - name: deployment_name
      value: string
      description: Required parameter for the lakeview_schedules resource.
    - name: schedule
      value: string
      description: |
        The schedule to create. A dashboard is limited to 10 schedules.
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

Delete dashboard schedule.

```sql
DELETE FROM databricks_workspace.dashboards.lakeview_schedules
WHERE dashboard_id = '{{ dashboard_id }}' --required
AND schedule_id = '{{ schedule_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND etag = '{{ etag }}'
;
```
</TabItem>
</Tabs>

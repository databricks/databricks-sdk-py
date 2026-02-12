---
title: task_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - task_runs
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

Creates, updates, deletes, gets or lists a <code>task_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.cleanrooms.task_runs" /></td></tr>
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
    "name": "notebook_name",
    "type": "string",
    "description": "Asset name of the notebook executed in this task run."
  },
  {
    "name": "output_schema_name",
    "type": "string",
    "description": "Name of the output schema associated with the clean rooms notebook task run."
  },
  {
    "name": "collaborator_job_run_info",
    "type": "object",
    "description": "Job run info of the task in the runner's local workspace. This field is only included in the LIST API. if the task was run within the same workspace the API is being called. If the task run was in a different workspace under the same metastore, only the workspace_id is included.",
    "children": [
      {
        "name": "collaborator_alias",
        "type": "string",
        "description": ""
      },
      {
        "name": "collaborator_job_id",
        "type": "integer",
        "description": "Job ID of the task run in the collaborator's workspace."
      },
      {
        "name": "collaborator_job_run_id",
        "type": "integer",
        "description": "Job run ID of the task run in the collaborator's workspace."
      },
      {
        "name": "collaborator_task_run_id",
        "type": "integer",
        "description": "Task run ID of the task run in the collaborator's workspace."
      },
      {
        "name": "collaborator_workspace_id",
        "type": "integer",
        "description": "ID of the collaborator's workspace that triggered the task run."
      }
    ]
  },
  {
    "name": "notebook_etag",
    "type": "string",
    "description": "Etag of the notebook executed in this task run, used to identify the notebook version."
  },
  {
    "name": "notebook_job_run_state",
    "type": "string",
    "description": "State of the task run."
  },
  {
    "name": "notebook_updated_at",
    "type": "integer",
    "description": "The timestamp of when the notebook was last updated."
  },
  {
    "name": "output_schema_expiration_time",
    "type": "integer",
    "description": "Expiration time of the output schema of the task run (if any), in epoch milliseconds."
  },
  {
    "name": "run_duration",
    "type": "integer",
    "description": "Duration of the task run, in milliseconds."
  },
  {
    "name": "start_time",
    "type": "integer",
    "description": "When the task run started, in epoch milliseconds."
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
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-notebook_name"><code>notebook_name</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List all the historical notebook task runs in a clean room.</td>
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
<tr id="parameter-notebook_name">
    <td><CopyableCode code="notebook_name" /></td>
    <td><code>string</code></td>
    <td>Notebook name</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>The maximum number of task runs to return. Currently ignored - all runs will be returned.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List all the historical notebook task runs in a clean room.

```sql
SELECT
notebook_name,
output_schema_name,
collaborator_job_run_info,
notebook_etag,
notebook_job_run_state,
notebook_updated_at,
output_schema_expiration_time,
run_duration,
start_time
FROM databricks_workspace.cleanrooms.task_runs
WHERE clean_room_name = '{{ clean_room_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND notebook_name = '{{ notebook_name }}'
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>

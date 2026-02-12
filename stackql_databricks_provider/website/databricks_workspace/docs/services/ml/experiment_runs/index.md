---
title: experiment_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - experiment_runs
  - ml
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

Creates, updates, deletes, gets or lists an <code>experiment_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiment_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.experiment_runs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "run",
    "type": "object",
    "description": "A single run.",
    "children": [
      {
        "name": "data",
        "type": "object",
        "description": "Run data.",
        "children": [
          {
            "name": "metrics",
            "type": "array",
            "description": "Run metrics.",
            "children": [
              {
                "name": "dataset_digest",
                "type": "string",
                "description": "The dataset digest of the dataset associated with the metric, e.g. an md5 hash of the dataset that uniquely identifies it within datasets of the same name."
              },
              {
                "name": "dataset_name",
                "type": "string",
                "description": "The name of the dataset associated with the metric. E.g. “my.uc.table@2” “nyc-taxi-dataset”, “fantastic-elk-3”"
              },
              {
                "name": "key",
                "type": "string",
                "description": "The key identifying the metric."
              },
              {
                "name": "model_id",
                "type": "string",
                "description": "The ID of the logged model or registered model version associated with the metric, if applicable."
              },
              {
                "name": "run_id",
                "type": "string",
                "description": "The ID of the run containing the metric."
              },
              {
                "name": "step",
                "type": "integer",
                "description": "The step at which the metric was logged."
              },
              {
                "name": "timestamp",
                "type": "integer",
                "description": "The timestamp at which the metric was recorded."
              },
              {
                "name": "value",
                "type": "number",
                "description": "The value of the metric."
              }
            ]
          },
          {
            "name": "params",
            "type": "array",
            "description": "Run parameters.",
            "children": [
              {
                "name": "key",
                "type": "string",
                "description": "Key identifying this param."
              },
              {
                "name": "value",
                "type": "string",
                "description": "Value associated with this param."
              }
            ]
          },
          {
            "name": "tags",
            "type": "array",
            "description": "Additional metadata key-value pairs.",
            "children": [
              {
                "name": "key",
                "type": "string",
                "description": "The tag key."
              },
              {
                "name": "value",
                "type": "string",
                "description": "The tag value."
              }
            ]
          }
        ]
      },
      {
        "name": "info",
        "type": "object",
        "description": "Run metadata.",
        "children": [
          {
            "name": "artifact_uri",
            "type": "string",
            "description": "URI of the directory where artifacts should be uploaded. This can be a local path (starting with \"/\"), or a distributed file system (DFS) path, like ``s3://bucket/directory`` or ``dbfs:/my/directory``. If not set, the local ``./mlruns`` directory is chosen."
          },
          {
            "name": "end_time",
            "type": "integer",
            "description": "Unix timestamp of when the run ended in milliseconds."
          },
          {
            "name": "experiment_id",
            "type": "string",
            "description": "The experiment ID."
          },
          {
            "name": "lifecycle_stage",
            "type": "string",
            "description": "Current life cycle stage of the experiment : OneOf(\"active\", \"deleted\")"
          },
          {
            "name": "run_id",
            "type": "string",
            "description": "Unique identifier for the run."
          },
          {
            "name": "run_name",
            "type": "string",
            "description": "The name of the run."
          },
          {
            "name": "run_uuid",
            "type": "string",
            "description": "[Deprecated, use run_id instead] Unique identifier for the run. This field will be removed in a future MLflow version."
          },
          {
            "name": "start_time",
            "type": "integer",
            "description": "Unix timestamp of when the run started in milliseconds."
          },
          {
            "name": "status",
            "type": "string",
            "description": "Current status of the run."
          },
          {
            "name": "user_id",
            "type": "string",
            "description": "User who initiated the run. This field is deprecated as of MLflow 1.0, and will be removed in a future MLflow release. Use 'mlflow.user' tag instead."
          }
        ]
      },
      {
        "name": "inputs",
        "type": "object",
        "description": "Run inputs.",
        "children": [
          {
            "name": "dataset_inputs",
            "type": "array",
            "description": "Run metrics.",
            "children": [
              {
                "name": "dataset",
                "type": "object",
                "description": "The dataset being used as a Run input."
              },
              {
                "name": "tags",
                "type": "array",
                "description": "A list of tags for the dataset input, e.g. a “context” tag with value “training”"
              }
            ]
          },
          {
            "name": "model_inputs",
            "type": "array",
            "description": "Model inputs to the Run.",
            "children": [
              {
                "name": "model_id",
                "type": "string",
                "description": "The unique identifier of the model."
              }
            ]
          }
        ]
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
    <td><a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-run_uuid"><code>run_uuid</code></a></td>
    <td>Gets the metadata, metrics, params, and tags for a run. In the case where multiple metrics with the</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new run within an experiment. A run is usually a single execution of a machine learning or</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a></td>
    <td></td>
    <td>Marks a run for deletion.</td>
</tr>
<tr>
    <td><a href="#delete_bulk"><CopyableCode code="delete_bulk" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-experiment_id"><code>experiment_id</code></a>, <a href="#parameter-max_timestamp_millis"><code>max_timestamp_millis</code></a></td>
    <td></td>
    <td>Bulk delete runs in an experiment that were created prior to or at the specified timestamp. Deletes at</td>
</tr>
<tr>
    <td><a href="#delete_tag"><CopyableCode code="delete_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-key"><code>key</code></a></td>
    <td></td>
    <td>Deletes a tag on a run. Tags are run metadata that can be updated during a run and after a run</td>
</tr>
<tr>
    <td><a href="#log_batch"><CopyableCode code="log_batch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Logs a batch of metrics, params, and tags for a run. If any data failed to be persisted, the server</td>
</tr>
<tr>
    <td><a href="#log_inputs"><CopyableCode code="log_inputs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a></td>
    <td></td>
    <td>Logs inputs, such as datasets and models, to an MLflow Run.</td>
</tr>
<tr>
    <td><a href="#log_metric"><CopyableCode code="log_metric" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-value"><code>value</code></a>, <a href="#parameter-timestamp"><code>timestamp</code></a></td>
    <td></td>
    <td>Log a metric for a run. A metric is a key-value pair (string key, float value) with an associated</td>
</tr>
<tr>
    <td><a href="#log_model"><CopyableCode code="log_model" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>**Note:** the [Create a logged model](/api/workspace/experiments/createloggedmodel) API replaces this</td>
</tr>
<tr>
    <td><a href="#log_outputs"><CopyableCode code="log_outputs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a></td>
    <td></td>
    <td>Logs outputs, such as models, from an MLflow Run.</td>
</tr>
<tr>
    <td><a href="#log_param"><CopyableCode code="log_param" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Logs a param used for a run. A param is a key-value pair (string key, string value). Examples include</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a></td>
    <td></td>
    <td>Restores a deleted run. This also restores associated metadata, runs, metrics, params, and tags.</td>
</tr>
<tr>
    <td><a href="#restore_bulk"><CopyableCode code="restore_bulk" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-experiment_id"><code>experiment_id</code></a>, <a href="#parameter-min_timestamp_millis"><code>min_timestamp_millis</code></a></td>
    <td></td>
    <td>Bulk restore runs in an experiment that were deleted no earlier than the specified timestamp. Restores</td>
</tr>
<tr>
    <td><a href="#search"><CopyableCode code="search" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Searches for runs that satisfy expressions.</td>
</tr>
<tr>
    <td><a href="#set_tag"><CopyableCode code="set_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Sets a tag on a run. Tags are run metadata that can be updated during a run and after a run completes.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates run metadata.</td>
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
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>ID of the run to fetch. Must be provided.</td>
</tr>
<tr id="parameter-run_uuid">
    <td><CopyableCode code="run_uuid" /></td>
    <td><code>string</code></td>
    <td>[Deprecated, use `run_id` instead] ID of the run to fetch. This field will be removed in a future MLflow version.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the metadata, metrics, params, and tags for a run. In the case where multiple metrics with the

```sql
SELECT
run
FROM databricks_workspace.ml.experiment_runs
WHERE run_id = '{{ run_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND run_uuid = '{{ run_uuid }}'
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

Creates a new run within an experiment. A run is usually a single execution of a machine learning or

```sql
INSERT INTO databricks_workspace.ml.experiment_runs (
data__experiment_id,
data__run_name,
data__start_time,
data__tags,
data__user_id,
deployment_name
)
SELECT 
'{{ experiment_id }}',
'{{ run_name }}',
'{{ start_time }}',
'{{ tags }}',
'{{ user_id }}',
'{{ deployment_name }}'
RETURNING
run
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: experiment_runs
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the experiment_runs resource.
    - name: experiment_id
      value: string
      description: |
        ID of the associated experiment.
    - name: run_name
      value: string
      description: |
        The name of the run.
    - name: start_time
      value: string
      description: |
        Unix timestamp in milliseconds of when the run started.
    - name: tags
      value: string
      description: |
        Additional metadata for run.
    - name: user_id
      value: string
      description: |
        ID of the user executing the run. This field is deprecated as of MLflow 1.0, and will be removed in a future MLflow release. Use 'mlflow.user' tag instead.
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'delete_bulk', value: 'delete_bulk' },
        { label: 'delete_tag', value: 'delete_tag' },
        { label: 'log_batch', value: 'log_batch' },
        { label: 'log_inputs', value: 'log_inputs' },
        { label: 'log_metric', value: 'log_metric' },
        { label: 'log_model', value: 'log_model' },
        { label: 'log_outputs', value: 'log_outputs' },
        { label: 'log_param', value: 'log_param' },
        { label: 'restore', value: 'restore' },
        { label: 'restore_bulk', value: 'restore_bulk' },
        { label: 'search', value: 'search' },
        { label: 'set_tag', value: 'set_tag' },
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="delete">

Marks a run for deletion.

```sql
EXEC databricks_workspace.ml.experiment_runs.delete 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": "{{ run_id }}"
}'
;
```
</TabItem>
<TabItem value="delete_bulk">

Bulk delete runs in an experiment that were created prior to or at the specified timestamp. Deletes at

```sql
EXEC databricks_workspace.ml.experiment_runs.delete_bulk 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"experiment_id": "{{ experiment_id }}", 
"max_timestamp_millis": {{ max_timestamp_millis }}, 
"max_runs": "{{ max_runs }}"
}'
;
```
</TabItem>
<TabItem value="delete_tag">

Deletes a tag on a run. Tags are run metadata that can be updated during a run and after a run

```sql
EXEC databricks_workspace.ml.experiment_runs.delete_tag 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": "{{ run_id }}", 
"key": "{{ key }}"
}'
;
```
</TabItem>
<TabItem value="log_batch">

Logs a batch of metrics, params, and tags for a run. If any data failed to be persisted, the server

```sql
EXEC databricks_workspace.ml.experiment_runs.log_batch 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"metrics": "{{ metrics }}", 
"params": "{{ params }}", 
"run_id": "{{ run_id }}", 
"tags": "{{ tags }}"
}'
;
```
</TabItem>
<TabItem value="log_inputs">

Logs inputs, such as datasets and models, to an MLflow Run.

```sql
EXEC databricks_workspace.ml.experiment_runs.log_inputs 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": "{{ run_id }}", 
"datasets": "{{ datasets }}", 
"models": "{{ models }}"
}'
;
```
</TabItem>
<TabItem value="log_metric">

Log a metric for a run. A metric is a key-value pair (string key, float value) with an associated

```sql
EXEC databricks_workspace.ml.experiment_runs.log_metric 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"key": "{{ key }}", 
"value": {{ value }}, 
"timestamp": {{ timestamp }}, 
"dataset_digest": "{{ dataset_digest }}", 
"dataset_name": "{{ dataset_name }}", 
"model_id": "{{ model_id }}", 
"run_id": "{{ run_id }}", 
"run_uuid": "{{ run_uuid }}", 
"step": "{{ step }}"
}'
;
```
</TabItem>
<TabItem value="log_model">

**Note:** the [Create a logged model](/api/workspace/experiments/createloggedmodel) API replaces this

```sql
EXEC databricks_workspace.ml.experiment_runs.log_model 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"model_json": "{{ model_json }}", 
"run_id": "{{ run_id }}"
}'
;
```
</TabItem>
<TabItem value="log_outputs">

Logs outputs, such as models, from an MLflow Run.

```sql
EXEC databricks_workspace.ml.experiment_runs.log_outputs 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": "{{ run_id }}", 
"models": "{{ models }}"
}'
;
```
</TabItem>
<TabItem value="log_param">

Logs a param used for a run. A param is a key-value pair (string key, string value). Examples include

```sql
EXEC databricks_workspace.ml.experiment_runs.log_param 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"key": "{{ key }}", 
"value": "{{ value }}", 
"run_id": "{{ run_id }}", 
"run_uuid": "{{ run_uuid }}"
}'
;
```
</TabItem>
<TabItem value="restore">

Restores a deleted run. This also restores associated metadata, runs, metrics, params, and tags.

```sql
EXEC databricks_workspace.ml.experiment_runs.restore 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": "{{ run_id }}"
}'
;
```
</TabItem>
<TabItem value="restore_bulk">

Bulk restore runs in an experiment that were deleted no earlier than the specified timestamp. Restores

```sql
EXEC databricks_workspace.ml.experiment_runs.restore_bulk 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"experiment_id": "{{ experiment_id }}", 
"min_timestamp_millis": {{ min_timestamp_millis }}, 
"max_runs": "{{ max_runs }}"
}'
;
```
</TabItem>
<TabItem value="search">

Searches for runs that satisfy expressions.

```sql
EXEC databricks_workspace.ml.experiment_runs.search 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"experiment_ids": "{{ experiment_ids }}", 
"filter": "{{ filter }}", 
"max_results": "{{ max_results }}", 
"order_by": "{{ order_by }}", 
"page_token": "{{ page_token }}", 
"run_view_type": "{{ run_view_type }}"
}'
;
```
</TabItem>
<TabItem value="set_tag">

Sets a tag on a run. Tags are run metadata that can be updated during a run and after a run completes.

```sql
EXEC databricks_workspace.ml.experiment_runs.set_tag 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"key": "{{ key }}", 
"value": "{{ value }}", 
"run_id": "{{ run_id }}", 
"run_uuid": "{{ run_uuid }}"
}'
;
```
</TabItem>
<TabItem value="update">

Updates run metadata.

```sql
EXEC databricks_workspace.ml.experiment_runs.update 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"end_time": "{{ end_time }}", 
"run_id": "{{ run_id }}", 
"run_name": "{{ run_name }}", 
"run_uuid": "{{ run_uuid }}", 
"status": "{{ status }}"
}'
;
```
</TabItem>
</Tabs>

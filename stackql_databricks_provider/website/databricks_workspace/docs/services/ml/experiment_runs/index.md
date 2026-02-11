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
    <td>Gets the metadata, metrics, params, and tags for a run. In the case where multiple metrics with the<br />same key are logged for a run, return only the value with the latest timestamp.<br /><br />If there are multiple values with the latest timestamp, return the maximum of these values.<br /><br />:param run_id: str<br />  ID of the run to fetch. Must be provided.<br />:param run_uuid: str (optional)<br />  [Deprecated, use `run_id` instead] ID of the run to fetch. This field will be removed in a future<br />  MLflow version.<br /><br />:returns: :class:`GetRunResponse`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new run within an experiment. A run is usually a single execution of a machine learning or<br />data ETL pipeline. MLflow uses runs to track the `mlflowParam`, `mlflowMetric`, and `mlflowRunTag`<br />associated with a single execution.<br /><br />:param experiment_id: str (optional)<br />  ID of the associated experiment.<br />:param run_name: str (optional)<br />  The name of the run.<br />:param start_time: int (optional)<br />  Unix timestamp in milliseconds of when the run started.<br />:param tags: List[:class:`RunTag`] (optional)<br />  Additional metadata for run.<br />:param user_id: str (optional)<br />  ID of the user executing the run. This field is deprecated as of MLflow 1.0, and will be removed in<br />  a future MLflow release. Use 'mlflow.user' tag instead.<br /><br />:returns: :class:`CreateRunResponse`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a></td>
    <td></td>
    <td>Marks a run for deletion.<br /><br />:param run_id: str<br />  ID of the run to delete.</td>
</tr>
<tr>
    <td><a href="#delete_bulk"><CopyableCode code="delete_bulk" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-experiment_id"><code>experiment_id</code></a>, <a href="#parameter-max_timestamp_millis"><code>max_timestamp_millis</code></a></td>
    <td></td>
    <td>Bulk delete runs in an experiment that were created prior to or at the specified timestamp. Deletes at<br />most max_runs per request. To call this API from a Databricks Notebook in Python, you can use the<br />client code snippet on<br /><br />:param experiment_id: str<br />  The ID of the experiment containing the runs to delete.<br />:param max_timestamp_millis: int<br />  The maximum creation timestamp in milliseconds since the UNIX epoch for deleting runs. Only runs<br />  created prior to or at this timestamp are deleted.<br />:param max_runs: int (optional)<br />  An optional positive integer indicating the maximum number of runs to delete. The maximum allowed<br />  value for max_runs is 10000.<br /><br />:returns: :class:`DeleteRunsResponse`</td>
</tr>
<tr>
    <td><a href="#delete_tag"><CopyableCode code="delete_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-key"><code>key</code></a></td>
    <td></td>
    <td>Deletes a tag on a run. Tags are run metadata that can be updated during a run and after a run<br />completes.<br /><br />:param run_id: str<br />  ID of the run that the tag was logged under. Must be provided.<br />:param key: str<br />  Name of the tag. Maximum size is 255 bytes. Must be provided.</td>
</tr>
<tr>
    <td><a href="#log_batch"><CopyableCode code="log_batch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Logs a batch of metrics, params, and tags for a run. If any data failed to be persisted, the server<br />will respond with an error (non-200 status code).<br /><br />In case of error (due to internal server error or an invalid request), partial data may be written.<br /><br />You can write metrics, params, and tags in interleaving fashion, but within a given entity type are<br />guaranteed to follow the order specified in the request body.<br /><br />The overwrite behavior for metrics, params, and tags is as follows:<br /><br />* Metrics: metric values are never overwritten. Logging a metric (key, value, timestamp) appends to<br />the set of values for the metric with the provided key.<br /><br />* Tags: tag values can be overwritten by successive writes to the same tag key. That is, if multiple<br />tag values with the same key are provided in the same API request, the last-provided tag value is<br />written. Logging the same tag (key, value) is permitted. Specifically, logging a tag is idempotent.<br /><br />* Parameters: once written, param values cannot be changed (attempting to overwrite a param value will<br />result in an error). However, logging the same param (key, value) is permitted. Specifically, logging<br />a param is idempotent.<br /><br />Request Limits ------------------------------- A single JSON-serialized API request may be up to 1 MB<br />in size and contain:<br /><br />* No more than 1000 metrics, params, and tags in total<br /><br />* Up to 1000 metrics<br /><br />* Up to 100 params<br /><br />* Up to 100 tags<br /><br />For example, a valid request might contain 900 metrics, 50 params, and 50 tags, but logging 900<br />metrics, 50 params, and 51 tags is invalid.<br /><br />The following limits also apply to metric, param, and tag keys and values:<br /><br />* Metric keys, param keys, and tag keys can be up to 250 characters in length<br /><br />* Parameter and tag values can be up to 250 characters in length<br /><br />:param metrics: List[:class:`Metric`] (optional)<br />  Metrics to log. A single request can contain up to 1000 metrics, and up to 1000 metrics, params, and<br />  tags in total.<br />:param params: List[:class:`Param`] (optional)<br />  Params to log. A single request can contain up to 100 params, and up to 1000 metrics, params, and<br />  tags in total.<br />:param run_id: str (optional)<br />  ID of the run to log under<br />:param tags: List[:class:`RunTag`] (optional)<br />  Tags to log. A single request can contain up to 100 tags, and up to 1000 metrics, params, and tags<br />  in total.</td>
</tr>
<tr>
    <td><a href="#log_inputs"><CopyableCode code="log_inputs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a></td>
    <td></td>
    <td>Logs inputs, such as datasets and models, to an MLflow Run.<br /><br />:param run_id: str<br />  ID of the run to log under<br />:param datasets: List[:class:`DatasetInput`] (optional)<br />  Dataset inputs<br />:param models: List[:class:`ModelInput`] (optional)<br />  Model inputs</td>
</tr>
<tr>
    <td><a href="#log_metric"><CopyableCode code="log_metric" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-value"><code>value</code></a>, <a href="#parameter-timestamp"><code>timestamp</code></a></td>
    <td></td>
    <td>Log a metric for a run. A metric is a key-value pair (string key, float value) with an associated<br />timestamp. Examples include the various metrics that represent ML model accuracy. A metric can be<br />logged multiple times.<br /><br />:param key: str<br />  Name of the metric.<br />:param value: float<br />  Double value of the metric being logged.<br />:param timestamp: int<br />  Unix timestamp in milliseconds at the time metric was logged.<br />:param dataset_digest: str (optional)<br />  Dataset digest of the dataset associated with the metric, e.g. an md5 hash of the dataset that<br />  uniquely identifies it within datasets of the same name.<br />:param dataset_name: str (optional)<br />  The name of the dataset associated with the metric. E.g. “my.uc.table@2” “nyc-taxi-dataset”,<br />  “fantastic-elk-3”<br />:param model_id: str (optional)<br />  ID of the logged model associated with the metric, if applicable<br />:param run_id: str (optional)<br />  ID of the run under which to log the metric. Must be provided.<br />:param run_uuid: str (optional)<br />  [Deprecated, use `run_id` instead] ID of the run under which to log the metric. This field will be<br />  removed in a future MLflow version.<br />:param step: int (optional)<br />  Step at which to log the metric</td>
</tr>
<tr>
    <td><a href="#log_model"><CopyableCode code="log_model" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>**Note:** the [Create a logged model](/api/workspace/experiments/createloggedmodel) API replaces this<br />endpoint.<br /><br />Log a model to an MLflow Run.<br /><br />:param model_json: str (optional)<br />  MLmodel file in json format.<br />:param run_id: str (optional)<br />  ID of the run to log under</td>
</tr>
<tr>
    <td><a href="#log_outputs"><CopyableCode code="log_outputs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a></td>
    <td></td>
    <td>Logs outputs, such as models, from an MLflow Run.<br /><br />:param run_id: str<br />  The ID of the Run from which to log outputs.<br />:param models: List[:class:`ModelOutput`] (optional)<br />  The model outputs from the Run.</td>
</tr>
<tr>
    <td><a href="#log_param"><CopyableCode code="log_param" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Logs a param used for a run. A param is a key-value pair (string key, string value). Examples include<br />hyperparameters used for ML model training and constant dates and values used in an ETL pipeline. A<br />param can be logged only once for a run.<br /><br />:param key: str<br />  Name of the param. Maximum size is 255 bytes.<br />:param value: str<br />  String value of the param being logged. Maximum size is 500 bytes.<br />:param run_id: str (optional)<br />  ID of the run under which to log the param. Must be provided.<br />:param run_uuid: str (optional)<br />  [Deprecated, use `run_id` instead] ID of the run under which to log the param. This field will be<br />  removed in a future MLflow version.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a></td>
    <td></td>
    <td>Restores a deleted run. This also restores associated metadata, runs, metrics, params, and tags.<br /><br />Throws `RESOURCE_DOES_NOT_EXIST` if the run was never created or was permanently deleted.<br /><br />:param run_id: str<br />  ID of the run to restore.</td>
</tr>
<tr>
    <td><a href="#restore_bulk"><CopyableCode code="restore_bulk" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-experiment_id"><code>experiment_id</code></a>, <a href="#parameter-min_timestamp_millis"><code>min_timestamp_millis</code></a></td>
    <td></td>
    <td>Bulk restore runs in an experiment that were deleted no earlier than the specified timestamp. Restores<br />at most max_runs per request. To call this API from a Databricks Notebook in Python, you can use the<br />client code snippet on<br /><br />:param experiment_id: str<br />  The ID of the experiment containing the runs to restore.<br />:param min_timestamp_millis: int<br />  The minimum deletion timestamp in milliseconds since the UNIX epoch for restoring runs. Only runs<br />  deleted no earlier than this timestamp are restored.<br />:param max_runs: int (optional)<br />  An optional positive integer indicating the maximum number of runs to restore. The maximum allowed<br />  value for max_runs is 10000.<br /><br />:returns: :class:`RestoreRunsResponse`</td>
</tr>
<tr>
    <td><a href="#search"><CopyableCode code="search" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Searches for runs that satisfy expressions.<br /><br />Search expressions can use `mlflowMetric` and `mlflowParam` keys.<br /><br />:param experiment_ids: List[str] (optional)<br />  List of experiment IDs to search over.<br />:param filter: str (optional)<br />  A filter expression over params, metrics, and tags, that allows returning a subset of runs. The<br />  syntax is a subset of SQL that supports ANDing together binary operations between a param, metric,<br />  or tag and a constant.<br /><br />  Example: `metrics.rmse < 1 and params.model_class = 'LogisticRegression'`<br /><br />  You can select columns with special characters (hyphen, space, period, etc.) by using double quotes:<br />  `metrics."model class" = 'LinearRegression' and tags."user-name" = 'Tomas'`<br /><br />  Supported operators are `=`, `!=`, `>`, `>=`, `<`, and `<=`.<br />:param max_results: int (optional)<br />  Maximum number of runs desired. Max threshold is 50000<br />:param order_by: List[str] (optional)<br />  List of columns to be ordered by, including attributes, params, metrics, and tags with an optional<br />  `"DESC"` or `"ASC"` annotation, where `"ASC"` is the default. Example: `["params.input DESC",<br />  "metrics.alpha ASC", "metrics.rmse"]`. Tiebreaks are done by start_time `DESC` followed by `run_id`<br />  for runs with the same start time (and this is the default ordering criterion if order_by is not<br />  provided).<br />:param page_token: str (optional)<br />  Token for the current page of runs.<br />:param run_view_type: :class:`ViewType` (optional)<br />  Whether to display only active, only deleted, or all runs. Defaults to only active runs.<br /><br />:returns: Iterator over :class:`Run`</td>
</tr>
<tr>
    <td><a href="#set_tag"><CopyableCode code="set_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Sets a tag on a run. Tags are run metadata that can be updated during a run and after a run completes.<br /><br />:param key: str<br />  Name of the tag. Keys up to 250 bytes in size are supported.<br />:param value: str<br />  String value of the tag being logged. Values up to 64KB in size are supported.<br />:param run_id: str (optional)<br />  ID of the run under which to log the tag. Must be provided.<br />:param run_uuid: str (optional)<br />  [Deprecated, use `run_id` instead] ID of the run under which to log the tag. This field will be<br />  removed in a future MLflow version.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates run metadata.<br /><br />:param end_time: int (optional)<br />  Unix timestamp in milliseconds of when the run ended.<br />:param run_id: str (optional)<br />  ID of the run to update. Must be provided.<br />:param run_name: str (optional)<br />  Updated name of the run.<br />:param run_uuid: str (optional)<br />  [Deprecated, use `run_id` instead] ID of the run to update. This field will be removed in a future<br />  MLflow version.<br />:param status: :class:`UpdateRunStatus` (optional)<br />  Updated status of the run.<br /><br />:returns: :class:`UpdateRunResponse`</td>
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

Gets the metadata, metrics, params, and tags for a run. In the case where multiple metrics with the<br />same key are logged for a run, return only the value with the latest timestamp.<br /><br />If there are multiple values with the latest timestamp, return the maximum of these values.<br /><br />:param run_id: str<br />  ID of the run to fetch. Must be provided.<br />:param run_uuid: str (optional)<br />  [Deprecated, use `run_id` instead] ID of the run to fetch. This field will be removed in a future<br />  MLflow version.<br /><br />:returns: :class:`GetRunResponse`

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

Creates a new run within an experiment. A run is usually a single execution of a machine learning or<br />data ETL pipeline. MLflow uses runs to track the `mlflowParam`, `mlflowMetric`, and `mlflowRunTag`<br />associated with a single execution.<br /><br />:param experiment_id: str (optional)<br />  ID of the associated experiment.<br />:param run_name: str (optional)<br />  The name of the run.<br />:param start_time: int (optional)<br />  Unix timestamp in milliseconds of when the run started.<br />:param tags: List[:class:`RunTag`] (optional)<br />  Additional metadata for run.<br />:param user_id: str (optional)<br />  ID of the user executing the run. This field is deprecated as of MLflow 1.0, and will be removed in<br />  a future MLflow release. Use 'mlflow.user' tag instead.<br /><br />:returns: :class:`CreateRunResponse`

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

Marks a run for deletion.<br /><br />:param run_id: str<br />  ID of the run to delete.

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

Bulk delete runs in an experiment that were created prior to or at the specified timestamp. Deletes at<br />most max_runs per request. To call this API from a Databricks Notebook in Python, you can use the<br />client code snippet on<br /><br />:param experiment_id: str<br />  The ID of the experiment containing the runs to delete.<br />:param max_timestamp_millis: int<br />  The maximum creation timestamp in milliseconds since the UNIX epoch for deleting runs. Only runs<br />  created prior to or at this timestamp are deleted.<br />:param max_runs: int (optional)<br />  An optional positive integer indicating the maximum number of runs to delete. The maximum allowed<br />  value for max_runs is 10000.<br /><br />:returns: :class:`DeleteRunsResponse`

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

Deletes a tag on a run. Tags are run metadata that can be updated during a run and after a run<br />completes.<br /><br />:param run_id: str<br />  ID of the run that the tag was logged under. Must be provided.<br />:param key: str<br />  Name of the tag. Maximum size is 255 bytes. Must be provided.

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

Logs a batch of metrics, params, and tags for a run. If any data failed to be persisted, the server<br />will respond with an error (non-200 status code).<br /><br />In case of error (due to internal server error or an invalid request), partial data may be written.<br /><br />You can write metrics, params, and tags in interleaving fashion, but within a given entity type are<br />guaranteed to follow the order specified in the request body.<br /><br />The overwrite behavior for metrics, params, and tags is as follows:<br /><br />* Metrics: metric values are never overwritten. Logging a metric (key, value, timestamp) appends to<br />the set of values for the metric with the provided key.<br /><br />* Tags: tag values can be overwritten by successive writes to the same tag key. That is, if multiple<br />tag values with the same key are provided in the same API request, the last-provided tag value is<br />written. Logging the same tag (key, value) is permitted. Specifically, logging a tag is idempotent.<br /><br />* Parameters: once written, param values cannot be changed (attempting to overwrite a param value will<br />result in an error). However, logging the same param (key, value) is permitted. Specifically, logging<br />a param is idempotent.<br /><br />Request Limits ------------------------------- A single JSON-serialized API request may be up to 1 MB<br />in size and contain:<br /><br />* No more than 1000 metrics, params, and tags in total<br /><br />* Up to 1000 metrics<br /><br />* Up to 100 params<br /><br />* Up to 100 tags<br /><br />For example, a valid request might contain 900 metrics, 50 params, and 50 tags, but logging 900<br />metrics, 50 params, and 51 tags is invalid.<br /><br />The following limits also apply to metric, param, and tag keys and values:<br /><br />* Metric keys, param keys, and tag keys can be up to 250 characters in length<br /><br />* Parameter and tag values can be up to 250 characters in length<br /><br />:param metrics: List[:class:`Metric`] (optional)<br />  Metrics to log. A single request can contain up to 1000 metrics, and up to 1000 metrics, params, and<br />  tags in total.<br />:param params: List[:class:`Param`] (optional)<br />  Params to log. A single request can contain up to 100 params, and up to 1000 metrics, params, and<br />  tags in total.<br />:param run_id: str (optional)<br />  ID of the run to log under<br />:param tags: List[:class:`RunTag`] (optional)<br />  Tags to log. A single request can contain up to 100 tags, and up to 1000 metrics, params, and tags<br />  in total.

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

Logs inputs, such as datasets and models, to an MLflow Run.<br /><br />:param run_id: str<br />  ID of the run to log under<br />:param datasets: List[:class:`DatasetInput`] (optional)<br />  Dataset inputs<br />:param models: List[:class:`ModelInput`] (optional)<br />  Model inputs

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

Log a metric for a run. A metric is a key-value pair (string key, float value) with an associated<br />timestamp. Examples include the various metrics that represent ML model accuracy. A metric can be<br />logged multiple times.<br /><br />:param key: str<br />  Name of the metric.<br />:param value: float<br />  Double value of the metric being logged.<br />:param timestamp: int<br />  Unix timestamp in milliseconds at the time metric was logged.<br />:param dataset_digest: str (optional)<br />  Dataset digest of the dataset associated with the metric, e.g. an md5 hash of the dataset that<br />  uniquely identifies it within datasets of the same name.<br />:param dataset_name: str (optional)<br />  The name of the dataset associated with the metric. E.g. “my.uc.table@2” “nyc-taxi-dataset”,<br />  “fantastic-elk-3”<br />:param model_id: str (optional)<br />  ID of the logged model associated with the metric, if applicable<br />:param run_id: str (optional)<br />  ID of the run under which to log the metric. Must be provided.<br />:param run_uuid: str (optional)<br />  [Deprecated, use `run_id` instead] ID of the run under which to log the metric. This field will be<br />  removed in a future MLflow version.<br />:param step: int (optional)<br />  Step at which to log the metric

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

**Note:** the [Create a logged model](/api/workspace/experiments/createloggedmodel) API replaces this<br />endpoint.<br /><br />Log a model to an MLflow Run.<br /><br />:param model_json: str (optional)<br />  MLmodel file in json format.<br />:param run_id: str (optional)<br />  ID of the run to log under

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

Logs outputs, such as models, from an MLflow Run.<br /><br />:param run_id: str<br />  The ID of the Run from which to log outputs.<br />:param models: List[:class:`ModelOutput`] (optional)<br />  The model outputs from the Run.

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

Logs a param used for a run. A param is a key-value pair (string key, string value). Examples include<br />hyperparameters used for ML model training and constant dates and values used in an ETL pipeline. A<br />param can be logged only once for a run.<br /><br />:param key: str<br />  Name of the param. Maximum size is 255 bytes.<br />:param value: str<br />  String value of the param being logged. Maximum size is 500 bytes.<br />:param run_id: str (optional)<br />  ID of the run under which to log the param. Must be provided.<br />:param run_uuid: str (optional)<br />  [Deprecated, use `run_id` instead] ID of the run under which to log the param. This field will be<br />  removed in a future MLflow version.

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

Restores a deleted run. This also restores associated metadata, runs, metrics, params, and tags.<br /><br />Throws `RESOURCE_DOES_NOT_EXIST` if the run was never created or was permanently deleted.<br /><br />:param run_id: str<br />  ID of the run to restore.

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

Bulk restore runs in an experiment that were deleted no earlier than the specified timestamp. Restores<br />at most max_runs per request. To call this API from a Databricks Notebook in Python, you can use the<br />client code snippet on<br /><br />:param experiment_id: str<br />  The ID of the experiment containing the runs to restore.<br />:param min_timestamp_millis: int<br />  The minimum deletion timestamp in milliseconds since the UNIX epoch for restoring runs. Only runs<br />  deleted no earlier than this timestamp are restored.<br />:param max_runs: int (optional)<br />  An optional positive integer indicating the maximum number of runs to restore. The maximum allowed<br />  value for max_runs is 10000.<br /><br />:returns: :class:`RestoreRunsResponse`

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

Searches for runs that satisfy expressions.<br /><br />Search expressions can use `mlflowMetric` and `mlflowParam` keys.<br /><br />:param experiment_ids: List[str] (optional)<br />  List of experiment IDs to search over.<br />:param filter: str (optional)<br />  A filter expression over params, metrics, and tags, that allows returning a subset of runs. The<br />  syntax is a subset of SQL that supports ANDing together binary operations between a param, metric,<br />  or tag and a constant.<br /><br />  Example: `metrics.rmse < 1 and params.model_class = 'LogisticRegression'`<br /><br />  You can select columns with special characters (hyphen, space, period, etc.) by using double quotes:<br />  `metrics."model class" = 'LinearRegression' and tags."user-name" = 'Tomas'`<br /><br />  Supported operators are `=`, `!=`, `>`, `>=`, `<`, and `<=`.<br />:param max_results: int (optional)<br />  Maximum number of runs desired. Max threshold is 50000<br />:param order_by: List[str] (optional)<br />  List of columns to be ordered by, including attributes, params, metrics, and tags with an optional<br />  `"DESC"` or `"ASC"` annotation, where `"ASC"` is the default. Example: `["params.input DESC",<br />  "metrics.alpha ASC", "metrics.rmse"]`. Tiebreaks are done by start_time `DESC` followed by `run_id`<br />  for runs with the same start time (and this is the default ordering criterion if order_by is not<br />  provided).<br />:param page_token: str (optional)<br />  Token for the current page of runs.<br />:param run_view_type: :class:`ViewType` (optional)<br />  Whether to display only active, only deleted, or all runs. Defaults to only active runs.<br /><br />:returns: Iterator over :class:`Run`

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

Sets a tag on a run. Tags are run metadata that can be updated during a run and after a run completes.<br /><br />:param key: str<br />  Name of the tag. Keys up to 250 bytes in size are supported.<br />:param value: str<br />  String value of the tag being logged. Values up to 64KB in size are supported.<br />:param run_id: str (optional)<br />  ID of the run under which to log the tag. Must be provided.<br />:param run_uuid: str (optional)<br />  [Deprecated, use `run_id` instead] ID of the run under which to log the tag. This field will be<br />  removed in a future MLflow version.

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

Updates run metadata.<br /><br />:param end_time: int (optional)<br />  Unix timestamp in milliseconds of when the run ended.<br />:param run_id: str (optional)<br />  ID of the run to update. Must be provided.<br />:param run_name: str (optional)<br />  Updated name of the run.<br />:param run_uuid: str (optional)<br />  [Deprecated, use `run_id` instead] ID of the run to update. This field will be removed in a future<br />  MLflow version.<br />:param status: :class:`UpdateRunStatus` (optional)<br />  Updated status of the run.<br /><br />:returns: :class:`UpdateRunResponse`

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

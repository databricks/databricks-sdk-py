---
title: forecasting
hide_title: false
hide_table_of_contents: false
keywords:
  - forecasting
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

Creates, updates, deletes, gets or lists a <code>forecasting</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="forecasting" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.forecasting" /></td></tr>
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
    "name": "experiment_id",
    "type": "string",
    "description": "The unique ID for the forecasting experiment."
  },
  {
    "name": "experiment_page_url",
    "type": "string",
    "description": "The URL to the forecasting experiment page."
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current state of the forecasting experiment. (CANCELLED, FAILED, PENDING, RUNNING, SUCCEEDED)"
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
    <td><a href="#parameter-experiment_id"><code>experiment_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Public RPC to get forecasting experiment</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-train_data_path"><code>train_data_path</code></a>, <a href="#parameter-target_column"><code>target_column</code></a>, <a href="#parameter-time_column"><code>time_column</code></a>, <a href="#parameter-forecast_granularity"><code>forecast_granularity</code></a>, <a href="#parameter-forecast_horizon"><code>forecast_horizon</code></a></td>
    <td></td>
    <td>Creates a serverless forecasting experiment. Returns the experiment ID.</td>
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
<tr id="parameter-experiment_id">
    <td><CopyableCode code="experiment_id" /></td>
    <td><code>string</code></td>
    <td>The unique ID of a forecasting experiment</td>
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

Public RPC to get forecasting experiment

```sql
SELECT
experiment_id,
experiment_page_url,
state
FROM databricks_workspace.ml.forecasting
WHERE experiment_id = '{{ experiment_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
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

Creates a serverless forecasting experiment. Returns the experiment ID.

```sql
INSERT INTO databricks_workspace.ml.forecasting (
train_data_path,
target_column,
time_column,
forecast_granularity,
forecast_horizon,
custom_weights_column,
experiment_path,
future_feature_data_path,
holiday_regions,
include_features,
max_runtime,
prediction_data_path,
primary_metric,
register_to,
split_column,
timeseries_identifier_columns,
training_frameworks,
deployment_name
)
SELECT 
'{{ train_data_path }}' /* required */,
'{{ target_column }}' /* required */,
'{{ time_column }}' /* required */,
'{{ forecast_granularity }}' /* required */,
{{ forecast_horizon }} /* required */,
'{{ custom_weights_column }}',
'{{ experiment_path }}',
'{{ future_feature_data_path }}',
'{{ holiday_regions }}',
'{{ include_features }}',
'{{ max_runtime }}',
'{{ prediction_data_path }}',
'{{ primary_metric }}',
'{{ register_to }}',
'{{ split_column }}',
'{{ timeseries_identifier_columns }}',
'{{ training_frameworks }}',
'{{ deployment_name }}'
RETURNING
experiment_id,
experiment_page_url,
state
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: forecasting
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the forecasting resource.
    - name: train_data_path
      value: string
      description: |
        The fully qualified path of a Unity Catalog table, formatted as catalog_name.schema_name.table_name, used as training data for the forecasting model.
    - name: target_column
      value: string
      description: |
        The column in the input training table used as the prediction target for model training. The values in this column are used as the ground truth for model training.
    - name: time_column
      value: string
      description: |
        The column in the input training table that represents each row's timestamp.
    - name: forecast_granularity
      value: string
      description: |
        The time interval between consecutive rows in the time series data. Possible values include: '1 second', '1 minute', '5 minutes', '10 minutes', '15 minutes', '30 minutes', 'Hourly', 'Daily', 'Weekly', 'Monthly', 'Quarterly', 'Yearly'.
    - name: forecast_horizon
      value: integer
      description: |
        The number of time steps into the future to make predictions, calculated as a multiple of forecast_granularity. This value represents how far ahead the model should forecast.
    - name: custom_weights_column
      value: string
      description: |
        The column in the training table used to customize weights for each time series.
    - name: experiment_path
      value: string
      description: |
        The path in the workspace to store the created experiment.
    - name: future_feature_data_path
      value: string
      description: |
        The fully qualified path of a Unity Catalog table, formatted as catalog_name.schema_name.table_name, used to store future feature data for predictions.
    - name: holiday_regions
      value: string
      description: |
        The region code(s) to automatically add holiday features. Currently supports only one region.
    - name: include_features
      value: string
      description: |
        Specifies the list of feature columns to include in model training. These columns must exist in the training data and be of type string, numerical, or boolean. If not specified, no additional features will be included. Note: Certain columns are automatically handled: - Automatically excluded: split_column, target_column, custom_weights_column. - Automatically included: time_column.
    - name: max_runtime
      value: string
      description: |
        The maximum duration for the experiment in minutes. The experiment stops automatically if it exceeds this limit.
    - name: prediction_data_path
      value: string
      description: |
        The fully qualified path of a Unity Catalog table, formatted as catalog_name.schema_name.table_name, used to store predictions.
    - name: primary_metric
      value: string
      description: |
        The evaluation metric used to optimize the forecasting model.
    - name: register_to
      value: string
      description: |
        The fully qualified path of a Unity Catalog model, formatted as catalog_name.schema_name.model_name, used to store the best model.
    - name: split_column
      value: string
      description: |
        // The column in the training table used for custom data splits. Values must be 'train', 'validate', or 'test'.
    - name: timeseries_identifier_columns
      value: string
      description: |
        The column in the training table used to group the dataset for predicting individual time series.
    - name: training_frameworks
      value: string
      description: |
        List of frameworks to include for model tuning. Possible values are 'Prophet', 'ARIMA', 'DeepAR'. An empty list includes all supported frameworks.
```
</TabItem>
</Tabs>

---
title: logged_models
hide_title: false
hide_table_of_contents: false
keywords:
  - logged_models
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

Creates, updates, deletes, gets or lists a <code>logged_models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logged_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.logged_models" /></td></tr>
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
    "name": "model",
    "type": "object",
    "description": "A logged model message includes logged model attributes, tags, registration info, params, and<br />    linked run metrics.",
    "children": [
      {
        "name": "data",
        "type": "object",
        "description": "The params and metrics attached to the logged model.",
        "children": [
          {
            "name": "metrics",
            "type": "array",
            "description": "Performance metrics linked to the model.",
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
            "description": "Immutable string key-value pairs of the model.",
            "children": [
              {
                "name": "key",
                "type": "string",
                "description": "The key identifying this param."
              },
              {
                "name": "value",
                "type": "string",
                "description": "The value of this param."
              }
            ]
          }
        ]
      },
      {
        "name": "info",
        "type": "object",
        "description": "The logged model attributes such as model ID, status, tags, etc.",
        "children": [
          {
            "name": "artifact_uri",
            "type": "string",
            "description": "The URI of the directory where model artifacts are stored."
          },
          {
            "name": "creation_timestamp_ms",
            "type": "integer",
            "description": "The timestamp when the model was created in milliseconds since the UNIX epoch."
          },
          {
            "name": "creator_id",
            "type": "integer",
            "description": "The ID of the user or principal that created the model."
          },
          {
            "name": "experiment_id",
            "type": "string",
            "description": "The ID of the experiment that owns the model."
          },
          {
            "name": "last_updated_timestamp_ms",
            "type": "integer",
            "description": "The timestamp when the model was last updated in milliseconds since the UNIX epoch."
          },
          {
            "name": "model_id",
            "type": "string",
            "description": "The unique identifier for the logged model."
          },
          {
            "name": "model_type",
            "type": "string",
            "description": "The type of model, such as ``\"Agent\"``, ``\"Classifier\"``, ``\"LLM\"``."
          },
          {
            "name": "name",
            "type": "string",
            "description": "The name of the model."
          },
          {
            "name": "source_run_id",
            "type": "string",
            "description": "The ID of the run that created the model."
          },
          {
            "name": "status",
            "type": "string",
            "description": "The status of whether or not the model is ready for use."
          },
          {
            "name": "status_message",
            "type": "string",
            "description": "Details on the current model status."
          },
          {
            "name": "tags",
            "type": "array",
            "description": "Mutable string key-value pairs set on the model.",
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
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a logged model.<br /><br />:param model_id: str<br />  The ID of the logged model to retrieve.<br /><br />:returns: :class:`GetLoggedModelResponse`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__experiment_id"><code>data__experiment_id</code></a></td>
    <td></td>
    <td>Create a logged model.<br /><br />:param experiment_id: str<br />  The ID of the experiment that owns the model.<br />:param model_type: str (optional)<br />  The type of the model, such as ``"Agent"``, ``"Classifier"``, ``"LLM"``.<br />:param name: str (optional)<br />  The name of the model (optional). If not specified one will be generated.<br />:param params: List[:class:`LoggedModelParameter`] (optional)<br />  Parameters attached to the model.<br />:param source_run_id: str (optional)<br />  The ID of the run that created the model.<br />:param tags: List[:class:`LoggedModelTag`] (optional)<br />  Tags attached to the model.<br /><br />:returns: :class:`CreateLoggedModelResponse`</td>
</tr>
<tr>
    <td><a href="#delete_tag"><CopyableCode code="delete_tag" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-tag_key"><code>tag_key</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a tag on a logged model.<br /><br />:param model_id: str<br />  The ID of the logged model to delete the tag from.<br />:param tag_key: str<br />  The tag key.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a logged model.<br /><br />:param model_id: str<br />  The ID of the logged model to delete.</td>
</tr>
<tr>
    <td><a href="#finalize"><CopyableCode code="finalize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-status"><code>status</code></a></td>
    <td></td>
    <td>Finalize a logged model.<br /><br />:param model_id: str<br />  The ID of the logged model to finalize.<br />:param status: :class:`LoggedModelStatus`<br />  Whether or not the model is ready for use. ``"LOGGED_MODEL_UPLOAD_FAILED"`` indicates that something<br />  went wrong when logging the model weights / agent code.<br /><br />:returns: :class:`FinalizeLoggedModelResponse`</td>
</tr>
<tr>
    <td><a href="#log_params"><CopyableCode code="log_params" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Logs params for a logged model. A param is a key-value pair (string key, string value). Examples<br />include hyperparameters used for ML model training. A param can be logged only once for a logged<br />model, and attempting to overwrite an existing param with a different value will result in an error<br /><br />:param model_id: str<br />  The ID of the logged model to log params for.<br />:param params: List[:class:`LoggedModelParameter`] (optional)<br />  Parameters to attach to the model.</td>
</tr>
<tr>
    <td><a href="#search"><CopyableCode code="search" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Search for Logged Models that satisfy specified search criteria.<br /><br />:param datasets: List[:class:`SearchLoggedModelsDataset`] (optional)<br />  List of datasets on which to apply the metrics filter clauses. For example, a filter with<br />  `metrics.accuracy > 0.9` and dataset info with name "test_dataset" means we will return all logged<br />  models with accuracy &gt; 0.9 on the test_dataset. Metric values from ANY dataset matching the criteria<br />  are considered. If no datasets are specified, then metrics across all datasets are considered in the<br />  filter.<br />:param experiment_ids: List[str] (optional)<br />  The IDs of the experiments in which to search for logged models.<br />:param filter: str (optional)<br />  A filter expression over logged model info and data that allows returning a subset of logged models.<br />  The syntax is a subset of SQL that supports AND'ing together binary operations.<br /><br />  Example: ``params.alpha &lt; 0.3 AND metrics.accuracy &gt; 0.9``.<br />:param max_results: int (optional)<br />  The maximum number of Logged Models to return. The maximum limit is 50.<br />:param order_by: List[:class:`SearchLoggedModelsOrderBy`] (optional)<br />  The list of columns for ordering the results, with additional fields for sorting criteria.<br />:param page_token: str (optional)<br />  The token indicating the page of logged models to fetch.<br /><br />:returns: :class:`SearchLoggedModelsResponse`</td>
</tr>
<tr>
    <td><a href="#set_tags"><CopyableCode code="set_tags" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Set tags for a logged model.<br /><br />:param model_id: str<br />  The ID of the logged model to set the tags on.<br />:param tags: List[:class:`LoggedModelTag`] (optional)<br />  The tags to set on the logged model.</td>
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
<tr id="parameter-model_id">
    <td><CopyableCode code="model_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the logged model to set the tags on.</td>
</tr>
<tr id="parameter-tag_key">
    <td><CopyableCode code="tag_key" /></td>
    <td><code>string</code></td>
    <td>The tag key.</td>
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

Get a logged model.<br /><br />:param model_id: str<br />  The ID of the logged model to retrieve.<br /><br />:returns: :class:`GetLoggedModelResponse`

```sql
SELECT
model
FROM databricks_workspace.ml.logged_models
WHERE model_id = '{{ model_id }}' -- required
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

Create a logged model.<br /><br />:param experiment_id: str<br />  The ID of the experiment that owns the model.<br />:param model_type: str (optional)<br />  The type of the model, such as ``"Agent"``, ``"Classifier"``, ``"LLM"``.<br />:param name: str (optional)<br />  The name of the model (optional). If not specified one will be generated.<br />:param params: List[:class:`LoggedModelParameter`] (optional)<br />  Parameters attached to the model.<br />:param source_run_id: str (optional)<br />  The ID of the run that created the model.<br />:param tags: List[:class:`LoggedModelTag`] (optional)<br />  Tags attached to the model.<br /><br />:returns: :class:`CreateLoggedModelResponse`

```sql
INSERT INTO databricks_workspace.ml.logged_models (
data__experiment_id,
data__model_type,
data__name,
data__params,
data__source_run_id,
data__tags,
deployment_name
)
SELECT 
'{{ experiment_id }}' /* required */,
'{{ model_type }}',
'{{ name }}',
'{{ params }}',
'{{ source_run_id }}',
'{{ tags }}',
'{{ deployment_name }}'
RETURNING
model
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: logged_models
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the logged_models resource.
    - name: experiment_id
      value: string
      description: |
        The ID of the experiment that owns the model.
    - name: model_type
      value: string
      description: |
        The type of the model, such as ``"Agent"``, ``"Classifier"``, ``"LLM"``.
    - name: name
      value: string
      description: |
        The name of the model (optional). If not specified one will be generated.
    - name: params
      value: string
      description: |
        Parameters attached to the model.
    - name: source_run_id
      value: string
      description: |
        The ID of the run that created the model.
    - name: tags
      value: string
      description: |
        Tags attached to the model.
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_tag"
    values={[
        { label: 'delete_tag', value: 'delete_tag' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_tag">

Delete a tag on a logged model.<br /><br />:param model_id: str<br />  The ID of the logged model to delete the tag from.<br />:param tag_key: str<br />  The tag key.

```sql
DELETE FROM databricks_workspace.ml.logged_models
WHERE model_id = '{{ model_id }}' --required
AND tag_key = '{{ tag_key }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="delete">

Delete a logged model.<br /><br />:param model_id: str<br />  The ID of the logged model to delete.

```sql
DELETE FROM databricks_workspace.ml.logged_models
WHERE model_id = '{{ model_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="finalize"
    values={[
        { label: 'finalize', value: 'finalize' },
        { label: 'log_params', value: 'log_params' },
        { label: 'search', value: 'search' },
        { label: 'set_tags', value: 'set_tags' }
    ]}
>
<TabItem value="finalize">

Finalize a logged model.<br /><br />:param model_id: str<br />  The ID of the logged model to finalize.<br />:param status: :class:`LoggedModelStatus`<br />  Whether or not the model is ready for use. ``"LOGGED_MODEL_UPLOAD_FAILED"`` indicates that something<br />  went wrong when logging the model weights / agent code.<br /><br />:returns: :class:`FinalizeLoggedModelResponse`

```sql
EXEC databricks_workspace.ml.logged_models.finalize 
@model_id='{{ model_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"status": "{{ status }}"
}'
;
```
</TabItem>
<TabItem value="log_params">

Logs params for a logged model. A param is a key-value pair (string key, string value). Examples<br />include hyperparameters used for ML model training. A param can be logged only once for a logged<br />model, and attempting to overwrite an existing param with a different value will result in an error<br /><br />:param model_id: str<br />  The ID of the logged model to log params for.<br />:param params: List[:class:`LoggedModelParameter`] (optional)<br />  Parameters to attach to the model.

```sql
EXEC databricks_workspace.ml.logged_models.log_params 
@model_id='{{ model_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"params": "{{ params }}"
}'
;
```
</TabItem>
<TabItem value="search">

Search for Logged Models that satisfy specified search criteria.<br /><br />:param datasets: List[:class:`SearchLoggedModelsDataset`] (optional)<br />  List of datasets on which to apply the metrics filter clauses. For example, a filter with<br />  `metrics.accuracy > 0.9` and dataset info with name "test_dataset" means we will return all logged<br />  models with accuracy &gt; 0.9 on the test_dataset. Metric values from ANY dataset matching the criteria<br />  are considered. If no datasets are specified, then metrics across all datasets are considered in the<br />  filter.<br />:param experiment_ids: List[str] (optional)<br />  The IDs of the experiments in which to search for logged models.<br />:param filter: str (optional)<br />  A filter expression over logged model info and data that allows returning a subset of logged models.<br />  The syntax is a subset of SQL that supports AND'ing together binary operations.<br /><br />  Example: ``params.alpha &lt; 0.3 AND metrics.accuracy &gt; 0.9``.<br />:param max_results: int (optional)<br />  The maximum number of Logged Models to return. The maximum limit is 50.<br />:param order_by: List[:class:`SearchLoggedModelsOrderBy`] (optional)<br />  The list of columns for ordering the results, with additional fields for sorting criteria.<br />:param page_token: str (optional)<br />  The token indicating the page of logged models to fetch.<br /><br />:returns: :class:`SearchLoggedModelsResponse`

```sql
EXEC databricks_workspace.ml.logged_models.search 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"datasets": "{{ datasets }}", 
"experiment_ids": "{{ experiment_ids }}", 
"filter": "{{ filter }}", 
"max_results": "{{ max_results }}", 
"order_by": "{{ order_by }}", 
"page_token": "{{ page_token }}"
}'
;
```
</TabItem>
<TabItem value="set_tags">

Set tags for a logged model.<br /><br />:param model_id: str<br />  The ID of the logged model to set the tags on.<br />:param tags: List[:class:`LoggedModelTag`] (optional)<br />  The tags to set on the logged model.

```sql
EXEC databricks_workspace.ml.logged_models.set_tags 
@model_id='{{ model_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"tags": "{{ tags }}"
}'
;
```
</TabItem>
</Tabs>

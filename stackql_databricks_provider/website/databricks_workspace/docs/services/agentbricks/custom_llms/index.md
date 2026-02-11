---
title: custom_llms
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_llms
  - agentbricks
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

Creates, updates, deletes, gets or lists a <code>custom_llms</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_llms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.agentbricks.custom_llms" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": ""
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "endpoint_name",
    "type": "string",
    "description": "Name of the endpoint that will be used to serve the custom LLM"
  },
  {
    "name": "agent_artifact_path",
    "type": "string",
    "description": ""
  },
  {
    "name": "creation_time",
    "type": "string",
    "description": "Creation timestamp of the custom LLM"
  },
  {
    "name": "creator",
    "type": "string",
    "description": "Creator of the custom LLM"
  },
  {
    "name": "datasets",
    "type": "array",
    "description": "Datasets used for training and evaluating the model, not for inference",
    "children": [
      {
        "name": "table",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "table_path",
            "type": "string",
            "description": ""
          },
          {
            "name": "request_col",
            "type": "string",
            "description": "Name of the request column"
          },
          {
            "name": "response_col",
            "type": "string",
            "description": "Optional: Name of the response column if the data is labeled"
          }
        ]
      }
    ]
  },
  {
    "name": "guidelines",
    "type": "array",
    "description": "Guidelines for the custom LLM to adhere to"
  },
  {
    "name": "instructions",
    "type": "string",
    "description": "Instructions for the custom LLM to follow"
  },
  {
    "name": "optimization_state",
    "type": "string",
    "description": "If optimization is kicked off, tracks the state of the custom LLM"
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a Custom LLM.<br /><br />:param id: str<br />  The id of the custom llm<br /><br />:returns: :class:`CustomLlm`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__name"><code>data__name</code></a>, <a href="#parameter-data__instructions"><code>data__instructions</code></a></td>
    <td></td>
    <td>Create a Custom LLM.<br /><br />:param name: str<br />  Name of the custom LLM. Only alphanumeric characters and dashes allowed.<br />:param instructions: str<br />  Instructions for the custom LLM to follow<br />:param agent_artifact_path: str (optional)<br />  This will soon be deprecated!! Optional: UC path for agent artifacts. If you are using a dataset<br />  that you only have read permissions, please provide a destination path where you have write<br />  permissions. Please provide this in catalog.schema format.<br />:param datasets: List[:class:`Dataset`] (optional)<br />  Datasets used for training and evaluating the model, not for inference. Currently, only 1 dataset is<br />  accepted.<br />:param guidelines: List[str] (optional)<br />  Guidelines for the custom LLM to adhere to<br /><br />:returns: :class:`CustomLlm`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__custom_llm"><code>data__custom_llm</code></a>, <a href="#parameter-data__update_mask"><code>data__update_mask</code></a></td>
    <td></td>
    <td>Update a Custom LLM.<br /><br />:param id: str<br />  The id of the custom llm<br />:param custom_llm: :class:`CustomLlm`<br />  The CustomLlm containing the fields which should be updated.<br />:param update_mask: str<br />  The list of the CustomLlm fields to update. These should correspond to the values (or lack thereof)<br />  present in `custom_llm`.<br /><br />  The field mask must be a single string, with multiple fields separated by commas (no spaces). The<br />  field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,<br />  `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only<br />  the entire collection field can be specified. Field names must exactly match the resource field<br />  names.<br /><br />  A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the<br />  fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API<br />  changes in the future.<br /><br />:returns: :class:`CustomLlm`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a Custom LLM.<br /><br />:param id: str<br />  The id of the custom llm</td>
</tr>
<tr>
    <td><a href="#cancel_optimize"><CopyableCode code="cancel_optimize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Cancel a Custom LLM Optimization Run.<br /><br />:param id: str</td>
</tr>
<tr>
    <td><a href="#start_optimize"><CopyableCode code="start_optimize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Start a Custom LLM Optimization Run.<br /><br />:param id: str<br />  The Id of the tile.<br /><br />:returns: :class:`CustomLlm`</td>
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
    <td>The Id of the tile.</td>
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

Get a Custom LLM.<br /><br />:param id: str<br />  The id of the custom llm<br /><br />:returns: :class:`CustomLlm`

```sql
SELECT
id,
name,
endpoint_name,
agent_artifact_path,
creation_time,
creator,
datasets,
guidelines,
instructions,
optimization_state
FROM databricks_workspace.agentbricks.custom_llms
WHERE id = '{{ id }}' -- required
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

Create a Custom LLM.<br /><br />:param name: str<br />  Name of the custom LLM. Only alphanumeric characters and dashes allowed.<br />:param instructions: str<br />  Instructions for the custom LLM to follow<br />:param agent_artifact_path: str (optional)<br />  This will soon be deprecated!! Optional: UC path for agent artifacts. If you are using a dataset<br />  that you only have read permissions, please provide a destination path where you have write<br />  permissions. Please provide this in catalog.schema format.<br />:param datasets: List[:class:`Dataset`] (optional)<br />  Datasets used for training and evaluating the model, not for inference. Currently, only 1 dataset is<br />  accepted.<br />:param guidelines: List[str] (optional)<br />  Guidelines for the custom LLM to adhere to<br /><br />:returns: :class:`CustomLlm`

```sql
INSERT INTO databricks_workspace.agentbricks.custom_llms (
data__name,
data__instructions,
data__agent_artifact_path,
data__datasets,
data__guidelines,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ instructions }}' /* required */,
'{{ agent_artifact_path }}',
'{{ datasets }}',
'{{ guidelines }}',
'{{ deployment_name }}'
RETURNING
id,
name,
endpoint_name,
agent_artifact_path,
creation_time,
creator,
datasets,
guidelines,
instructions,
optimization_state
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: custom_llms
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the custom_llms resource.
    - name: name
      value: string
      description: |
        Name of the custom LLM. Only alphanumeric characters and dashes allowed.
    - name: instructions
      value: string
      description: |
        Instructions for the custom LLM to follow
    - name: agent_artifact_path
      value: string
      description: |
        This will soon be deprecated!! Optional: UC path for agent artifacts. If you are using a dataset that you only have read permissions, please provide a destination path where you have write permissions. Please provide this in catalog.schema format.
    - name: datasets
      value: string
      description: |
        Datasets used for training and evaluating the model, not for inference. Currently, only 1 dataset is accepted.
    - name: guidelines
      value: string
      description: |
        Guidelines for the custom LLM to adhere to
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

Update a Custom LLM.<br /><br />:param id: str<br />  The id of the custom llm<br />:param custom_llm: :class:`CustomLlm`<br />  The CustomLlm containing the fields which should be updated.<br />:param update_mask: str<br />  The list of the CustomLlm fields to update. These should correspond to the values (or lack thereof)<br />  present in `custom_llm`.<br /><br />  The field mask must be a single string, with multiple fields separated by commas (no spaces). The<br />  field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,<br />  `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only<br />  the entire collection field can be specified. Field names must exactly match the resource field<br />  names.<br /><br />  A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the<br />  fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API<br />  changes in the future.<br /><br />:returns: :class:`CustomLlm`

```sql
UPDATE databricks_workspace.agentbricks.custom_llms
SET 
data__custom_llm = '{{ custom_llm }}',
data__update_mask = '{{ update_mask }}'
WHERE 
id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__custom_llm = '{{ custom_llm }}' --required
AND data__update_mask = '{{ update_mask }}' --required
RETURNING
id,
name,
endpoint_name,
agent_artifact_path,
creation_time,
creator,
datasets,
guidelines,
instructions,
optimization_state;
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

Delete a Custom LLM.<br /><br />:param id: str<br />  The id of the custom llm

```sql
DELETE FROM databricks_workspace.agentbricks.custom_llms
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel_optimize"
    values={[
        { label: 'cancel_optimize', value: 'cancel_optimize' },
        { label: 'start_optimize', value: 'start_optimize' }
    ]}
>
<TabItem value="cancel_optimize">

Cancel a Custom LLM Optimization Run.<br /><br />:param id: str

```sql
EXEC databricks_workspace.agentbricks.custom_llms.cancel_optimize 
@id='{{ id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="start_optimize">

Start a Custom LLM Optimization Run.<br /><br />:param id: str<br />  The Id of the tile.<br /><br />:returns: :class:`CustomLlm`

```sql
EXEC databricks_workspace.agentbricks.custom_llms.start_optimize 
@id='{{ id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

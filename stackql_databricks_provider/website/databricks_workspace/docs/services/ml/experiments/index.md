---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists an <code>experiments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="experiments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.experiments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_name"
    values={[
        { label: 'get_by_name', value: 'get_by_name' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_name">

<SchemaTable fields={[
  {
    "name": "experiment",
    "type": "object",
    "description": "An experiment and its metadata.",
    "children": [
      {
        "name": "artifact_location",
        "type": "string",
        "description": "Location where artifacts for the experiment are stored."
      },
      {
        "name": "creation_time",
        "type": "integer",
        "description": "Creation time"
      },
      {
        "name": "experiment_id",
        "type": "string",
        "description": "Unique identifier for the experiment."
      },
      {
        "name": "last_update_time",
        "type": "integer",
        "description": "Last update time"
      },
      {
        "name": "lifecycle_stage",
        "type": "string",
        "description": "Current life cycle stage of the experiment: \"active\" or \"deleted\". Deleted experiments are not returned by APIs."
      },
      {
        "name": "name",
        "type": "string",
        "description": "Human readable name that identifies the experiment."
      },
      {
        "name": "tags",
        "type": "array",
        "description": "Tags: Additional metadata key-value pairs.",
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
]} />
</TabItem>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "experiment",
    "type": "object",
    "description": "An experiment and its metadata.",
    "children": [
      {
        "name": "artifact_location",
        "type": "string",
        "description": "Location where artifacts for the experiment are stored."
      },
      {
        "name": "creation_time",
        "type": "integer",
        "description": "Creation time"
      },
      {
        "name": "experiment_id",
        "type": "string",
        "description": "Unique identifier for the experiment."
      },
      {
        "name": "last_update_time",
        "type": "integer",
        "description": "Last update time"
      },
      {
        "name": "lifecycle_stage",
        "type": "string",
        "description": "Current life cycle stage of the experiment: \"active\" or \"deleted\". Deleted experiments are not returned by APIs."
      },
      {
        "name": "name",
        "type": "string",
        "description": "Human readable name that identifies the experiment."
      },
      {
        "name": "tags",
        "type": "array",
        "description": "Tags: Additional metadata key-value pairs.",
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
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Human readable name that identifies the experiment."
  },
  {
    "name": "experiment_id",
    "type": "string",
    "description": "Unique identifier for the experiment."
  },
  {
    "name": "artifact_location",
    "type": "string",
    "description": "Location where artifacts for the experiment are stored."
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Creation time"
  },
  {
    "name": "last_update_time",
    "type": "integer",
    "description": "Last update time"
  },
  {
    "name": "lifecycle_stage",
    "type": "string",
    "description": "Current life cycle stage of the experiment: \"active\" or \"deleted\". Deleted experiments are not returned by APIs."
  },
  {
    "name": "tags",
    "type": "array",
    "description": "Tags: Additional metadata key-value pairs.",
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
    <td><a href="#get_by_name"><CopyableCode code="get_by_name" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-experiment_name"><code>experiment_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets metadata for an experiment.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-experiment_id"><code>experiment_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets metadata for an experiment. This method works on deleted experiments.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-view_type"><code>view_type</code></a></td>
    <td>Gets a list of all experiments.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates an experiment with a name. Returns the ID of the newly created experiment. Validates that</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-experiment_id"><code>experiment_id</code></a></td>
    <td></td>
    <td>Marks an experiment and associated metadata, runs, metrics, params, and tags for deletion. If the</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-experiment_id"><code>experiment_id</code></a></td>
    <td></td>
    <td>Restore an experiment marked for deletion. This also restores associated metadata, runs, metrics,</td>
</tr>
<tr>
    <td><a href="#search"><CopyableCode code="search" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Searches for experiments that satisfy specified search criteria.</td>
</tr>
<tr>
    <td><a href="#set_tag"><CopyableCode code="set_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-experiment_id"><code>experiment_id</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Sets a tag on an experiment. Experiment tags are metadata that can be updated.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-experiment_id"><code>experiment_id</code></a></td>
    <td></td>
    <td>Updates experiment metadata.</td>
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
<tr id="parameter-experiment_id">
    <td><CopyableCode code="experiment_id" /></td>
    <td><code>string</code></td>
    <td>ID of the associated experiment.</td>
</tr>
<tr id="parameter-experiment_name">
    <td><CopyableCode code="experiment_name" /></td>
    <td><code>string</code></td>
    <td>Name of the associated experiment.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of experiments desired. If `max_results` is unspecified, return all experiments. If `max_results` is too large, it'll be automatically capped at 1000. Callers of this endpoint are encouraged to pass max_results explicitly and leverage page_token to iterate through experiments.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Token indicating the page of experiments to fetch</td>
</tr>
<tr id="parameter-view_type">
    <td><CopyableCode code="view_type" /></td>
    <td><code>string</code></td>
    <td>Qualifier for type of experiments to be returned. If unspecified, return only active experiments.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_name"
    values={[
        { label: 'get_by_name', value: 'get_by_name' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_name">

Gets metadata for an experiment.

```sql
SELECT
experiment
FROM databricks_workspace.ml.experiments
WHERE experiment_name = '{{ experiment_name }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets metadata for an experiment. This method works on deleted experiments.

```sql
SELECT
experiment
FROM databricks_workspace.ml.experiments
WHERE experiment_id = '{{ experiment_id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of all experiments.

```sql
SELECT
name,
experiment_id,
artifact_location,
creation_time,
last_update_time,
lifecycle_stage,
tags
FROM databricks_workspace.ml.experiments
WHERE workspace = '{{ workspace }}' -- required
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
AND view_type = '{{ view_type }}'
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

Creates an experiment with a name. Returns the ID of the newly created experiment. Validates that

```sql
INSERT INTO databricks_workspace.ml.experiments (
name,
artifact_location,
tags,
workspace
)
SELECT 
'{{ name }}' /* required */,
'{{ artifact_location }}',
'{{ tags }}',
'{{ workspace }}'
RETURNING
experiment_id
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: experiments
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the experiments resource.
    - name: name
      value: "{{ name }}"
      description: |
        Experiment name.
    - name: artifact_location
      value: "{{ artifact_location }}"
      description: |
        Location where all artifacts for the experiment are stored. If not provided, the remote server will select an appropriate default.
    - name: tags
      description: |
        A collection of tags to set on the experiment. Maximum tag size and number of tags per request depends on the storage backend. All storage backends are guaranteed to support tag keys up to 250 bytes in size and tag values up to 5000 bytes in size. All storage backends are also guaranteed to support up to 20 tags per request.
      value:
        - key: "{{ key }}"
          value: "{{ value }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'restore', value: 'restore' },
        { label: 'search', value: 'search' },
        { label: 'set_tag', value: 'set_tag' },
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="delete">

Marks an experiment and associated metadata, runs, metrics, params, and tags for deletion. If the

```sql
EXEC databricks_workspace.ml.experiments.delete 
@workspace='{{ workspace }}' --required 
@@json=
'{
"experiment_id": "{{ experiment_id }}"
}'
;
```
</TabItem>
<TabItem value="restore">

Restore an experiment marked for deletion. This also restores associated metadata, runs, metrics,

```sql
EXEC databricks_workspace.ml.experiments.restore 
@workspace='{{ workspace }}' --required 
@@json=
'{
"experiment_id": "{{ experiment_id }}"
}'
;
```
</TabItem>
<TabItem value="search">

Searches for experiments that satisfy specified search criteria.

```sql
EXEC databricks_workspace.ml.experiments.search 
@workspace='{{ workspace }}' --required 
@@json=
'{
"filter": "{{ filter }}", 
"max_results": {{ max_results }}, 
"order_by": "{{ order_by }}", 
"page_token": "{{ page_token }}", 
"view_type": "{{ view_type }}"
}'
;
```
</TabItem>
<TabItem value="set_tag">

Sets a tag on an experiment. Experiment tags are metadata that can be updated.

```sql
EXEC databricks_workspace.ml.experiments.set_tag 
@workspace='{{ workspace }}' --required 
@@json=
'{
"experiment_id": "{{ experiment_id }}", 
"key": "{{ key }}", 
"value": "{{ value }}"
}'
;
```
</TabItem>
<TabItem value="update">

Updates experiment metadata.

```sql
EXEC databricks_workspace.ml.experiments.update 
@workspace='{{ workspace }}' --required 
@@json=
'{
"experiment_id": "{{ experiment_id }}", 
"new_name": "{{ new_name }}"
}'
;
```
</TabItem>
</Tabs>

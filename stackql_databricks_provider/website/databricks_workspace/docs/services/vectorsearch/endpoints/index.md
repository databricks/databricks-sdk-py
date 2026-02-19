---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - vectorsearch
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

Creates, updates, deletes, gets or lists an <code>endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.vectorsearch.endpoints" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": "Unique identifier of the endpoint"
  },
  {
    "name": "name",
    "type": "string",
    "description": "Name of the vector search endpoint"
  },
  {
    "name": "effective_budget_policy_id",
    "type": "string",
    "description": "The budget policy id applied to the endpoint"
  },
  {
    "name": "creation_timestamp",
    "type": "integer",
    "description": ""
  },
  {
    "name": "creator",
    "type": "string",
    "description": "Creator of the endpoint"
  },
  {
    "name": "custom_tags",
    "type": "array",
    "description": "The custom tags assigned to the endpoint",
    "children": [
      {
        "name": "key",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": "[Optional] Value field for a vector search endpoint tag."
      }
    ]
  },
  {
    "name": "endpoint_status",
    "type": "object",
    "description": "Current status of the endpoint",
    "children": [
      {
        "name": "message",
        "type": "string",
        "description": "Additional status message"
      },
      {
        "name": "state",
        "type": "string",
        "description": "Current state of the endpoint (DELETED, OFFLINE, ONLINE, PROVISIONING, RED_STATE, YELLOW_STATE)"
      }
    ]
  },
  {
    "name": "endpoint_type",
    "type": "string",
    "description": "Type of endpoint (STANDARD)"
  },
  {
    "name": "last_updated_timestamp",
    "type": "integer",
    "description": "Timestamp of last update to the endpoint"
  },
  {
    "name": "last_updated_user",
    "type": "string",
    "description": "User who last updated the endpoint"
  },
  {
    "name": "num_indexes",
    "type": "integer",
    "description": "Number of indexes on the endpoint"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Unique identifier of the endpoint"
  },
  {
    "name": "name",
    "type": "string",
    "description": "Name of the vector search endpoint"
  },
  {
    "name": "effective_budget_policy_id",
    "type": "string",
    "description": "The budget policy id applied to the endpoint"
  },
  {
    "name": "creation_timestamp",
    "type": "integer",
    "description": ""
  },
  {
    "name": "creator",
    "type": "string",
    "description": "Creator of the endpoint"
  },
  {
    "name": "custom_tags",
    "type": "array",
    "description": "The custom tags assigned to the endpoint",
    "children": [
      {
        "name": "key",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": "[Optional] Value field for a vector search endpoint tag."
      }
    ]
  },
  {
    "name": "endpoint_status",
    "type": "object",
    "description": "Current status of the endpoint",
    "children": [
      {
        "name": "message",
        "type": "string",
        "description": "Additional status message"
      },
      {
        "name": "state",
        "type": "string",
        "description": "Current state of the endpoint (DELETED, OFFLINE, ONLINE, PROVISIONING, RED_STATE, YELLOW_STATE)"
      }
    ]
  },
  {
    "name": "endpoint_type",
    "type": "string",
    "description": "Type of endpoint (STANDARD)"
  },
  {
    "name": "last_updated_timestamp",
    "type": "integer",
    "description": "Timestamp of last update to the endpoint"
  },
  {
    "name": "last_updated_user",
    "type": "string",
    "description": "User who last updated the endpoint"
  },
  {
    "name": "num_indexes",
    "type": "integer",
    "description": "Number of indexes on the endpoint"
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
    <td><a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get details for a single vector search endpoint.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List all vector search endpoints in the workspace.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint_type"><code>endpoint_type</code></a></td>
    <td></td>
    <td>Create a new endpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a vector search endpoint.</td>
</tr>
<tr>
    <td><a href="#retrieve_user_visible_metrics"><CopyableCode code="retrieve_user_visible_metrics" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieve user-visible metrics for an endpoint</td>
</tr>
<tr>
    <td><a href="#update_endpoint_budget_policy"><CopyableCode code="update_endpoint_budget_policy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-budget_policy_id"><code>budget_policy_id</code></a></td>
    <td></td>
    <td>Update the budget policy of an endpoint</td>
</tr>
<tr>
    <td><a href="#update_endpoint_custom_tags"><CopyableCode code="update_endpoint_custom_tags" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-custom_tags"><code>custom_tags</code></a></td>
    <td></td>
    <td>Update the custom tags of an endpoint.</td>
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
<tr id="parameter-endpoint_name">
    <td><CopyableCode code="endpoint_name" /></td>
    <td><code>string</code></td>
    <td>Name of the vector search endpoint</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Vector search endpoint name</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Token for pagination</td>
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

Get details for a single vector search endpoint.

```sql
SELECT
id,
name,
effective_budget_policy_id,
creation_timestamp,
creator,
custom_tags,
endpoint_status,
endpoint_type,
last_updated_timestamp,
last_updated_user,
num_indexes
FROM databricks_workspace.vectorsearch.endpoints
WHERE endpoint_name = '{{ endpoint_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all vector search endpoints in the workspace.

```sql
SELECT
id,
name,
effective_budget_policy_id,
creation_timestamp,
creator,
custom_tags,
endpoint_status,
endpoint_type,
last_updated_timestamp,
last_updated_user,
num_indexes
FROM databricks_workspace.vectorsearch.endpoints
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Create a new endpoint.

```sql
INSERT INTO databricks_workspace.vectorsearch.endpoints (
name,
endpoint_type,
budget_policy_id,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ endpoint_type }}' /* required */,
'{{ budget_policy_id }}',
'{{ deployment_name }}'
RETURNING
id,
name,
effective_budget_policy_id,
creation_timestamp,
creator,
custom_tags,
endpoint_status,
endpoint_type,
last_updated_timestamp,
last_updated_user,
num_indexes
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: endpoints
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the endpoints resource.
    - name: name
      value: string
      description: |
        Name of the vector search endpoint
    - name: endpoint_type
      value: string
      description: |
        Type of endpoint
    - name: budget_policy_id
      value: string
      description: |
        The budget policy id to be applied
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

Delete a vector search endpoint.

```sql
DELETE FROM databricks_workspace.vectorsearch.endpoints
WHERE endpoint_name = '{{ endpoint_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="retrieve_user_visible_metrics"
    values={[
        { label: 'retrieve_user_visible_metrics', value: 'retrieve_user_visible_metrics' },
        { label: 'update_endpoint_budget_policy', value: 'update_endpoint_budget_policy' },
        { label: 'update_endpoint_custom_tags', value: 'update_endpoint_custom_tags' }
    ]}
>
<TabItem value="retrieve_user_visible_metrics">

Retrieve user-visible metrics for an endpoint

```sql
EXEC databricks_workspace.vectorsearch.endpoints.retrieve_user_visible_metrics 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"end_time": "{{ end_time }}", 
"granularity_in_seconds": "{{ granularity_in_seconds }}", 
"metrics": "{{ metrics }}", 
"page_token": "{{ page_token }}", 
"start_time": "{{ start_time }}"
}'
;
```
</TabItem>
<TabItem value="update_endpoint_budget_policy">

Update the budget policy of an endpoint

```sql
EXEC databricks_workspace.vectorsearch.endpoints.update_endpoint_budget_policy 
@endpoint_name='{{ endpoint_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"budget_policy_id": "{{ budget_policy_id }}"
}'
;
```
</TabItem>
<TabItem value="update_endpoint_custom_tags">

Update the custom tags of an endpoint.

```sql
EXEC databricks_workspace.vectorsearch.endpoints.update_endpoint_custom_tags 
@endpoint_name='{{ endpoint_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"custom_tags": "{{ custom_tags }}"
}'
;
```
</TabItem>
</Tabs>

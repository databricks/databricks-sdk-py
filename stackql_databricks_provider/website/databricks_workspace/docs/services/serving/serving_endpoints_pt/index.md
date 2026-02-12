---
title: serving_endpoints_pt
hide_title: false
hide_table_of_contents: false
keywords:
  - serving_endpoints_pt
  - serving
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

Creates, updates, deletes, gets or lists a <code>serving_endpoints_pt</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serving_endpoints_pt</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.serving.serving_endpoints_pt" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__name"><code>data__name</code></a>, <a href="#parameter-data__config"><code>data__config</code></a></td>
    <td></td>
    <td>Create a new PT serving endpoint.</td>
</tr>
<tr>
    <td><a href="#update_config"><CopyableCode code="update_config" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__config"><code>data__config</code></a></td>
    <td></td>
    <td>Updates any combination of the pt endpoint's served entities, the compute configuration of those</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the pt endpoint to update. This field is required.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a new PT serving endpoint.

```sql
INSERT INTO databricks_workspace.serving.serving_endpoints_pt (
data__name,
data__config,
data__ai_gateway,
data__budget_policy_id,
data__email_notifications,
data__tags,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ config }}' /* required */,
'{{ ai_gateway }}',
'{{ budget_policy_id }}',
'{{ email_notifications }}',
'{{ tags }}',
'{{ deployment_name }}'
RETURNING
id,
name,
budget_policy_id,
ai_gateway,
config,
creation_timestamp,
creator,
data_plane_info,
description,
email_notifications,
endpoint_url,
last_updated_timestamp,
pending_config,
permission_level,
route_optimized,
state,
tags,
task
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: serving_endpoints_pt
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the serving_endpoints_pt resource.
    - name: name
      value: string
      description: |
        The name of the serving endpoint. This field is required and must be unique across a Databricks workspace. An endpoint name can consist of alphanumeric characters, dashes, and underscores.
    - name: config
      value: string
      description: |
        The core config of the serving endpoint.
    - name: ai_gateway
      value: string
      description: |
        The AI Gateway configuration for the serving endpoint.
    - name: budget_policy_id
      value: string
      description: |
        The budget policy associated with the endpoint.
    - name: email_notifications
      value: string
      description: |
        Email notification settings.
    - name: tags
      value: string
      description: |
        Tags to be attached to the serving endpoint and automatically propagated to billing logs.
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_config"
    values={[
        { label: 'update_config', value: 'update_config' }
    ]}
>
<TabItem value="update_config">

Updates any combination of the pt endpoint's served entities, the compute configuration of those

```sql
REPLACE databricks_workspace.serving.serving_endpoints_pt
SET 
data__config = '{{ config }}'
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__config = '{{ config }}' --required
RETURNING
id,
name,
budget_policy_id,
ai_gateway,
config,
creation_timestamp,
creator,
data_plane_info,
description,
email_notifications,
endpoint_url,
last_updated_timestamp,
pending_config,
permission_level,
route_optimized,
state,
tags,
task;
```
</TabItem>
</Tabs>

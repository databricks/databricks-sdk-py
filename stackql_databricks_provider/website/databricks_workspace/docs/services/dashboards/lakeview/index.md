---
title: lakeview
hide_title: false
hide_table_of_contents: false
keywords:
  - lakeview
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>lakeview</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lakeview" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dashboards.lakeview" /></td></tr>
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
    "description": "UUID identifying the dashboard."
  },
  {
    "name": "warehouse_id",
    "type": "string",
    "description": "The warehouse ID used to run the dashboard."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "The display name of the dashboard."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": ""
  },
  {
    "name": "etag",
    "type": "string",
    "description": "The etag for the dashboard. Can be optionally provided on updates to ensure that the dashboard has not been modified since the last read. This field is excluded in List Dashboards responses."
  },
  {
    "name": "lifecycle_state",
    "type": "string",
    "description": "The state of the dashboard resource. Used for tracking trashed status. (ACTIVE, TRASHED)"
  },
  {
    "name": "parent_path",
    "type": "string",
    "description": "The workspace path of the folder containing the dashboard. Includes leading slash and no trailing slash. This field is excluded in List Dashboards responses."
  },
  {
    "name": "path",
    "type": "string",
    "description": "The workspace path of the dashboard asset, including the file name. Exported dashboards always have the file extension `.lvdash.json`. This field is excluded in List Dashboards responses."
  },
  {
    "name": "serialized_dashboard",
    "type": "string",
    "description": "The contents of the dashboard in serialized string form. This field is excluded in List Dashboards responses. Use the [get dashboard API] to retrieve an example response, which includes the `serialized_dashboard` field. This field provides the structure of the JSON string that represents the dashboard's layout and components. [get dashboard API]: https://docs.databricks.com/api/workspace/lakeview/get"
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "The timestamp of when the dashboard was last updated by the user. This field is excluded in List Dashboards responses."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "dashboard_id",
    "type": "string",
    "description": "UUID identifying the dashboard."
  },
  {
    "name": "warehouse_id",
    "type": "string",
    "description": "The warehouse ID used to run the dashboard."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "The display name of the dashboard."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": ""
  },
  {
    "name": "etag",
    "type": "string",
    "description": "The etag for the dashboard. Can be optionally provided on updates to ensure that the dashboard has not been modified since the last read. This field is excluded in List Dashboards responses."
  },
  {
    "name": "lifecycle_state",
    "type": "string",
    "description": "The state of the dashboard resource. Used for tracking trashed status. (ACTIVE, TRASHED)"
  },
  {
    "name": "parent_path",
    "type": "string",
    "description": "The workspace path of the folder containing the dashboard. Includes leading slash and no trailing slash. This field is excluded in List Dashboards responses."
  },
  {
    "name": "path",
    "type": "string",
    "description": "The workspace path of the dashboard asset, including the file name. Exported dashboards always have the file extension `.lvdash.json`. This field is excluded in List Dashboards responses."
  },
  {
    "name": "serialized_dashboard",
    "type": "string",
    "description": "The contents of the dashboard in serialized string form. This field is excluded in List Dashboards responses. Use the [get dashboard API] to retrieve an example response, which includes the `serialized_dashboard` field. This field provides the structure of the JSON string that represents the dashboard's layout and components. [get dashboard API]: https://docs.databricks.com/api/workspace/lakeview/get"
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "The timestamp of when the dashboard was last updated by the user. This field is excluded in List Dashboards responses."
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
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a draft dashboard.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-show_trashed"><code>show_trashed</code></a>, <a href="#parameter-view"><code>view</code></a></td>
    <td>List dashboards.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-dashboard"><code>dashboard</code></a></td>
    <td><a href="#parameter-dataset_catalog"><code>dataset_catalog</code></a>, <a href="#parameter-dataset_schema"><code>dataset_schema</code></a></td>
    <td>Create a draft dashboard.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-dashboard"><code>dashboard</code></a></td>
    <td><a href="#parameter-dataset_catalog"><code>dataset_catalog</code></a>, <a href="#parameter-dataset_schema"><code>dataset_schema</code></a></td>
    <td>Update a draft dashboard.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-dashboard"><code>dashboard</code></a></td>
    <td><a href="#parameter-dataset_catalog"><code>dataset_catalog</code></a>, <a href="#parameter-dataset_schema"><code>dataset_schema</code></a></td>
    <td>Update a draft dashboard.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Trash a dashboard.</td>
</tr>
<tr>
    <td><a href="#migrate"><CopyableCode code="migrate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-source_dashboard_id"><code>source_dashboard_id</code></a></td>
    <td></td>
    <td>Migrates a classic SQL dashboard to Lakeview.</td>
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
    <td>UUID identifying the dashboard.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-dataset_catalog">
    <td><CopyableCode code="dataset_catalog" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-dataset_schema">
    <td><CopyableCode code="dataset_schema" /></td>
    <td><code>string</code></td>
    <td>Sets the default schema for all datasets in this dashboard. Does not impact table references that use fully qualified schema names (ex: nyctaxi.trips). Leave blank to keep each dataset’s existing configuration.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The number of dashboards to return per page.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous `ListDashboards` call. This token can be used to retrieve the subsequent page.</td>
</tr>
<tr id="parameter-show_trashed">
    <td><CopyableCode code="show_trashed" /></td>
    <td><code>boolean</code></td>
    <td>The flag to include dashboards located in the trash. If unspecified, only active dashboards will be returned.</td>
</tr>
<tr id="parameter-view">
    <td><CopyableCode code="view" /></td>
    <td><code>string</code></td>
    <td>`DASHBOARD_VIEW_BASIC`only includes summary metadata from the dashboard.</td>
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

Get a draft dashboard.

```sql
SELECT
dashboard_id,
warehouse_id,
display_name,
create_time,
etag,
lifecycle_state,
parent_path,
path,
serialized_dashboard,
update_time
FROM databricks_workspace.dashboards.lakeview
WHERE dashboard_id = '{{ dashboard_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List dashboards.

```sql
SELECT
dashboard_id,
warehouse_id,
display_name,
create_time,
etag,
lifecycle_state,
parent_path,
path,
serialized_dashboard,
update_time
FROM databricks_workspace.dashboards.lakeview
WHERE deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND show_trashed = '{{ show_trashed }}'
AND view = '{{ view }}'
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

Create a draft dashboard.

```sql
INSERT INTO databricks_workspace.dashboards.lakeview (
dashboard,
deployment_name,
dataset_catalog,
dataset_schema
)
SELECT 
'{{ dashboard }}' /* required */,
'{{ deployment_name }}',
'{{ dataset_catalog }}',
'{{ dataset_schema }}'
RETURNING
dashboard_id,
warehouse_id,
display_name,
create_time,
etag,
lifecycle_state,
parent_path,
path,
serialized_dashboard,
update_time
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: lakeview
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the lakeview resource.
    - name: dashboard
      description: |
        :param dataset_catalog: str (optional) Sets the default catalog for all datasets in this dashboard. Does not impact table references that use fully qualified catalog names (ex: samples.nyctaxi.trips). Leave blank to keep each dataset’s existing configuration.
      value:
        create_time: "{{ create_time }}"
        dashboard_id: "{{ dashboard_id }}"
        display_name: "{{ display_name }}"
        etag: "{{ etag }}"
        lifecycle_state: "{{ lifecycle_state }}"
        parent_path: "{{ parent_path }}"
        path: "{{ path }}"
        serialized_dashboard: "{{ serialized_dashboard }}"
        update_time: "{{ update_time }}"
        warehouse_id: "{{ warehouse_id }}"
    - name: dataset_catalog
      value: "{{ dataset_catalog }}"
    - name: dataset_schema
      value: "{{ dataset_schema }}"
      description: Sets the default schema for all datasets in this dashboard. Does not impact table references that use fully qualified schema names (ex: nyctaxi.trips). Leave blank to keep each dataset’s existing configuration.
`}</CodeBlock>

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

Update a draft dashboard.

```sql
UPDATE databricks_workspace.dashboards.lakeview
SET 
dashboard = '{{ dashboard }}'
WHERE 
dashboard_id = '{{ dashboard_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND dashboard = '{{ dashboard }}' --required
AND dataset_catalog = '{{ dataset_catalog}}'
AND dataset_schema = '{{ dataset_schema}}'
RETURNING
dashboard_id,
warehouse_id,
display_name,
create_time,
etag,
lifecycle_state,
parent_path,
path,
serialized_dashboard,
update_time;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update a draft dashboard.

```sql
REPLACE databricks_workspace.dashboards.lakeview
SET 
dashboard = '{{ dashboard }}'
WHERE 
dashboard_id = '{{ dashboard_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND dashboard = '{{ dashboard }}' --required
AND dataset_catalog = '{{ dataset_catalog}}'
AND dataset_schema = '{{ dataset_schema}}'
RETURNING
dashboard_id,
warehouse_id,
display_name,
create_time,
etag,
lifecycle_state,
parent_path,
path,
serialized_dashboard,
update_time;
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

Trash a dashboard.

```sql
DELETE FROM databricks_workspace.dashboards.lakeview
WHERE dashboard_id = '{{ dashboard_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="migrate"
    values={[
        { label: 'migrate', value: 'migrate' }
    ]}
>
<TabItem value="migrate">

Migrates a classic SQL dashboard to Lakeview.

```sql
EXEC databricks_workspace.dashboards.lakeview.migrate 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"source_dashboard_id": "{{ source_dashboard_id }}", 
"display_name": "{{ display_name }}", 
"parent_path": "{{ parent_path }}", 
"update_parameter_syntax": {{ update_parameter_syntax }}
}'
;
```
</TabItem>
</Tabs>

---
title: dashboard_widgets
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboard_widgets
  - sql
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

Creates, updates, deletes, gets or lists a <code>dashboard_widgets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dashboard_widgets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.dashboard_widgets" /></td></tr>
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
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-options"><code>options</code></a>, <a href="#parameter-width"><code>width</code></a></td>
    <td></td>
    <td>Updates an existing widget</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-options"><code>options</code></a>, <a href="#parameter-width"><code>width</code></a></td>
    <td></td>
    <td>Adds a widget to a dashboard</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Removes a widget from a dashboard</td>
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
    <td>Widget ID returned by :method:dashboardwidgets/create</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="update">

Updates an existing widget

```sql
INSERT INTO databricks_workspace.sql.dashboard_widgets (
dashboard_id,
options,
width,
text,
visualization_id,
id,
deployment_name
)
SELECT 
'{{ dashboard_id }}' /* required */,
'{{ options }}' /* required */,
{{ width }} /* required */,
'{{ text }}',
'{{ visualization_id }}',
'{{ id }}',
'{{ deployment_name }}'
RETURNING
id,
options,
visualization,
width
;
```
</TabItem>
<TabItem value="create">

Adds a widget to a dashboard

```sql
INSERT INTO databricks_workspace.sql.dashboard_widgets (
dashboard_id,
options,
width,
text,
visualization_id,
deployment_name
)
SELECT 
'{{ dashboard_id }}' /* required */,
'{{ options }}' /* required */,
{{ width }} /* required */,
'{{ text }}',
'{{ visualization_id }}',
'{{ deployment_name }}'
RETURNING
id,
options,
visualization,
width
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: dashboard_widgets
  props:
    - name: id
      value: "{{ id }}"
      description: Required parameter for the dashboard_widgets resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the dashboard_widgets resource.
    - name: dashboard_id
      value: "{{ dashboard_id }}"
      description: |
        Dashboard ID returned by :method:dashboards/create.
    - name: options
      description: |
        :param width: int Width of a widget
      value:
        created_at: "{{ created_at }}"
        description: "{{ description }}"
        isHidden: {{ isHidden }}
        parameterMappings: "{{ parameterMappings }}"
        position:
          autoHeight: {{ autoHeight }}
          col: {{ col }}
          row: {{ row }}
          sizeX: {{ sizeX }}
          sizeY: {{ sizeY }}
        title: "{{ title }}"
        updated_at: "{{ updated_at }}"
    - name: width
      value: {{ width }}
    - name: text
      value: "{{ text }}"
      description: |
        If this is a textbox widget, the application displays this text. This field is ignored if the widget contains a visualization in the \`visualization\` field.
    - name: visualization_id
      value: "{{ visualization_id }}"
      description: |
        Query Vizualization ID returned by :method:queryvisualizations/create.
`}</CodeBlock>

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

Removes a widget from a dashboard

```sql
DELETE FROM databricks_workspace.sql.dashboard_widgets
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

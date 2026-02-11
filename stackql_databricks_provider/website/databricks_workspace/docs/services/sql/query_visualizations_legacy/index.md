---
title: query_visualizations_legacy
hide_title: false
hide_table_of_contents: false
keywords:
  - query_visualizations_legacy
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>query_visualizations_legacy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>query_visualizations_legacy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.query_visualizations_legacy" /></td></tr>
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates visualization in the query.<br /><br />**Warning**: This API is deprecated. Please use :method:queryvisualizations/update instead. [Learn<br />more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br />:param created_at: str (optional)<br />:param description: str (optional)<br />  A short description of this visualization. This is not displayed in the UI.<br />:param id: str (optional)<br />  The UUID for this visualization.<br />:param name: str (optional)<br />  The name of the visualization that appears on dashboards and the query screen.<br />:param options: Any (optional)<br />  The options object varies widely from one visualization type to the next and is unsupported.<br />  Databricks does not recommend modifying visualization settings in JSON.<br />:param query: :class:`LegacyQuery` (optional)<br />:param type: str (optional)<br />  The type of visualization: chart, table, pivot table, and so on.<br />:param updated_at: str (optional)<br /><br />:returns: :class:`LegacyVisualization`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__options"><code>data__options</code></a>, <a href="#parameter-data__query_id"><code>data__query_id</code></a>, <a href="#parameter-data__type"><code>data__type</code></a></td>
    <td></td>
    <td>Creates visualization in the query.<br /><br />**Warning**: This API is deprecated. Please use :method:queryvisualizations/create instead. [Learn<br />more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br />:param options: Any<br />  The options object varies widely from one visualization type to the next and is unsupported.<br />  Databricks does not recommend modifying visualization settings in JSON.<br />:param query_id: str<br />  The identifier returned by :method:queries/create<br />:param type: str<br />  The type of visualization: chart, table, pivot table, and so on.<br />:param description: str (optional)<br />  A short description of this visualization. This is not displayed in the UI.<br />:param name: str (optional)<br />  The name of the visualization that appears on dashboards and the query screen.<br /><br />:returns: :class:`LegacyVisualization`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Removes a visualization from the query.<br /><br />**Warning**: This API is deprecated. Please use :method:queryvisualizations/delete instead. [Learn<br />more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br />:param id: str<br />  Widget ID returned by :method:queryvisualizations/create</td>
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
    <td>Widget ID returned by :method:queryvisualizations/create</td>
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

Updates visualization in the query.<br /><br />**Warning**: This API is deprecated. Please use :method:queryvisualizations/update instead. [Learn<br />more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br />:param created_at: str (optional)<br />:param description: str (optional)<br />  A short description of this visualization. This is not displayed in the UI.<br />:param id: str (optional)<br />  The UUID for this visualization.<br />:param name: str (optional)<br />  The name of the visualization that appears on dashboards and the query screen.<br />:param options: Any (optional)<br />  The options object varies widely from one visualization type to the next and is unsupported.<br />  Databricks does not recommend modifying visualization settings in JSON.<br />:param query: :class:`LegacyQuery` (optional)<br />:param type: str (optional)<br />  The type of visualization: chart, table, pivot table, and so on.<br />:param updated_at: str (optional)<br /><br />:returns: :class:`LegacyVisualization`

```sql
INSERT INTO databricks_workspace.sql.query_visualizations_legacy (
data__created_at,
data__description,
data__name,
data__options,
data__query,
data__type,
data__updated_at,
id,
deployment_name
)
SELECT 
'{{ created_at }}',
'{{ description }}',
'{{ name }}',
'{{ options }}',
'{{ query }}',
'{{ type }}',
'{{ updated_at }}',
'{{ id }}',
'{{ deployment_name }}'
RETURNING
id,
name,
created_at,
description,
options,
query,
type,
updated_at
;
```
</TabItem>
<TabItem value="create">

Creates visualization in the query.<br /><br />**Warning**: This API is deprecated. Please use :method:queryvisualizations/create instead. [Learn<br />more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br />:param options: Any<br />  The options object varies widely from one visualization type to the next and is unsupported.<br />  Databricks does not recommend modifying visualization settings in JSON.<br />:param query_id: str<br />  The identifier returned by :method:queries/create<br />:param type: str<br />  The type of visualization: chart, table, pivot table, and so on.<br />:param description: str (optional)<br />  A short description of this visualization. This is not displayed in the UI.<br />:param name: str (optional)<br />  The name of the visualization that appears on dashboards and the query screen.<br /><br />:returns: :class:`LegacyVisualization`

```sql
INSERT INTO databricks_workspace.sql.query_visualizations_legacy (
data__options,
data__query_id,
data__type,
data__description,
data__name,
deployment_name
)
SELECT 
'{{ options }}' /* required */,
'{{ query_id }}' /* required */,
'{{ type }}' /* required */,
'{{ description }}',
'{{ name }}',
'{{ deployment_name }}'
RETURNING
id,
name,
created_at,
description,
options,
query,
type,
updated_at
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: query_visualizations_legacy
  props:
    - name: id
      value: string
      description: Required parameter for the query_visualizations_legacy resource.
    - name: deployment_name
      value: string
      description: Required parameter for the query_visualizations_legacy resource.
    - name: created_at
      value: string
      description: |
        :param description: str (optional) A short description of this visualization. This is not displayed in the UI.
    - name: description
      value: string
      description: |
        A short description of this visualization. This is not displayed in the UI.
    - name: name
      value: string
      description: |
        The name of the visualization that appears on dashboards and the query screen.
    - name: options
      value: string
      description: |
        The options object varies widely from one visualization type to the next and is unsupported. Databricks does not recommend modifying visualization settings in JSON.
    - name: query
      value: string
      description: |
        :param type: str (optional) The type of visualization: chart, table, pivot table, and so on.
    - name: type
      value: string
      description: |
        The type of visualization: chart, table, pivot table, and so on.
    - name: updated_at
      value: string
      description: |
        :returns: :class:`LegacyVisualization`
    - name: query_id
      value: string
      description: |
        The identifier returned by :method:queries/create
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

Removes a visualization from the query.<br /><br />**Warning**: This API is deprecated. Please use :method:queryvisualizations/delete instead. [Learn<br />more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br />:param id: str<br />  Widget ID returned by :method:queryvisualizations/create

```sql
DELETE FROM databricks_workspace.sql.query_visualizations_legacy
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

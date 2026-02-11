---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
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

Creates, updates, deletes, gets or lists a <code>data_sources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.data_sources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Data source ID maps to the ID of the data source used by the resource and is distinct from the warehouse ID. [Learn more] [Learn more]: https://docs.databricks.com/api/workspace/datasources/list"
  },
  {
    "name": "name",
    "type": "string",
    "description": "The string name of this data source / SQL warehouse as it appears in the Databricks SQL web application."
  },
  {
    "name": "warehouse_id",
    "type": "string",
    "description": "The ID of the associated SQL warehouse, if this data source is backed by a SQL warehouse."
  },
  {
    "name": "pause_reason",
    "type": "string",
    "description": "Reserved for internal use."
  },
  {
    "name": "paused",
    "type": "integer",
    "description": "Reserved for internal use."
  },
  {
    "name": "supports_auto_limit",
    "type": "boolean",
    "description": "Reserved for internal use."
  },
  {
    "name": "syntax",
    "type": "string",
    "description": "Reserved for internal use."
  },
  {
    "name": "type",
    "type": "string",
    "description": "The type of data source. For SQL warehouses, this will be `databricks_internal`."
  },
  {
    "name": "view_only",
    "type": "boolean",
    "description": "Reserved for internal use."
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieves a full list of SQL warehouses available in this workspace. All fields that appear in this<br />API response are enumerated for clarity. However, you need only a SQL warehouse's `id` to create new<br />queries against it.<br /><br />**Warning**: This API is deprecated. Please use :method:warehouses/list instead. [Learn more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br /><br />:returns: Iterator over :class:`DataSource`</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Retrieves a full list of SQL warehouses available in this workspace. All fields that appear in this<br />API response are enumerated for clarity. However, you need only a SQL warehouse's `id` to create new<br />queries against it.<br /><br />**Warning**: This API is deprecated. Please use :method:warehouses/list instead. [Learn more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br /><br />:returns: Iterator over :class:`DataSource`

```sql
SELECT
id,
name,
warehouse_id,
pause_reason,
paused,
supports_auto_limit,
syntax,
type,
view_only
FROM databricks_workspace.sql.data_sources
WHERE deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>

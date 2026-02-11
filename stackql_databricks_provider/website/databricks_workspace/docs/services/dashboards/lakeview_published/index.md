---
title: lakeview_published
hide_title: false
hide_table_of_contents: false
keywords:
  - lakeview_published
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>lakeview_published</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lakeview_published</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dashboards.lakeview_published" /></td></tr>
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
    "name": "warehouse_id",
    "type": "string",
    "description": "The warehouse ID used to run the published dashboard."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "embed_credentials",
    "type": "boolean",
    "description": "Indicates whether credentials are embedded in the published dashboard."
  },
  {
    "name": "revision_create_time",
    "type": "string",
    "description": "The timestamp of when the published dashboard was last revised."
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
    <td>Get the current published dashboard.<br /><br />:param dashboard_id: str<br />  UUID identifying the published dashboard.<br /><br />:returns: :class:`PublishedDashboard`</td>
</tr>
<tr>
    <td><a href="#publish"><CopyableCode code="publish" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Publish the current draft dashboard.<br /><br />:param dashboard_id: str<br />  UUID identifying the dashboard to be published.<br />:param embed_credentials: bool (optional)<br />  Flag to indicate if the publisher's credentials should be embedded in the published dashboard. These<br />  embedded credentials will be used to execute the published dashboard's queries.<br />:param warehouse_id: str (optional)<br />  The ID of the warehouse that can be used to override the warehouse which was set in the draft.<br /><br />:returns: :class:`PublishedDashboard`</td>
</tr>
<tr>
    <td><a href="#unpublish"><CopyableCode code="unpublish" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Unpublish the dashboard.<br /><br />:param dashboard_id: str<br />  UUID identifying the published dashboard.</td>
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
    <td>UUID identifying the published dashboard.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
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

Get the current published dashboard.<br /><br />:param dashboard_id: str<br />  UUID identifying the published dashboard.<br /><br />:returns: :class:`PublishedDashboard`

```sql
SELECT
warehouse_id,
display_name,
embed_credentials,
revision_create_time
FROM databricks_workspace.dashboards.lakeview_published
WHERE dashboard_id = '{{ dashboard_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="publish"
    values={[
        { label: 'publish', value: 'publish' },
        { label: 'unpublish', value: 'unpublish' }
    ]}
>
<TabItem value="publish">

Publish the current draft dashboard.<br /><br />:param dashboard_id: str<br />  UUID identifying the dashboard to be published.<br />:param embed_credentials: bool (optional)<br />  Flag to indicate if the publisher's credentials should be embedded in the published dashboard. These<br />  embedded credentials will be used to execute the published dashboard's queries.<br />:param warehouse_id: str (optional)<br />  The ID of the warehouse that can be used to override the warehouse which was set in the draft.<br /><br />:returns: :class:`PublishedDashboard`

```sql
EXEC databricks_workspace.dashboards.lakeview_published.publish 
@dashboard_id='{{ dashboard_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"embed_credentials": "{{ embed_credentials }}", 
"warehouse_id": "{{ warehouse_id }}"
}'
;
```
</TabItem>
<TabItem value="unpublish">

Unpublish the dashboard.<br /><br />:param dashboard_id: str<br />  UUID identifying the published dashboard.

```sql
EXEC databricks_workspace.dashboards.lakeview_published.unpublish 
@dashboard_id='{{ dashboard_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

---
title: provider_provider_analytics_dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_provider_analytics_dashboards
  - marketplace
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

Creates, updates, deletes, gets or lists a <code>provider_provider_analytics_dashboards</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="provider_provider_analytics_dashboards" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_provider_analytics_dashboards" /></td></tr>
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
    "name": "dashboard_id",
    "type": "string",
    "description": "dashboard_id will be used to open Lakeview dashboard."
  },
  {
    "name": "version",
    "type": "integer",
    "description": ""
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
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Get provider analytics dashboard.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Create provider analytics dashboard. Returns Marketplace specific `id`. Not to be confused with the</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Update provider analytics dashboard.</td>
</tr>
<tr>
    <td><a href="#get_latest_version"><CopyableCode code="get_latest_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Get latest version of provider analytics dashboard.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>id is immutable property and can't be updated.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
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

Get provider analytics dashboard.

```sql
SELECT
id,
dashboard_id,
version
FROM databricks_workspace.marketplace.provider_provider_analytics_dashboards
WHERE workspace = '{{ workspace }}' -- required
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

Create provider analytics dashboard. Returns Marketplace specific `id`. Not to be confused with the

```sql
INSERT INTO databricks_workspace.marketplace.provider_provider_analytics_dashboards (
workspace
)
SELECT 
'{{ workspace }}'
RETURNING
id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: provider_provider_analytics_dashboards
  props:
    - name: workspace
      value: string
      description: Required parameter for the provider_provider_analytics_dashboards resource.
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

Update provider analytics dashboard.

```sql
REPLACE databricks_workspace.marketplace.provider_provider_analytics_dashboards
SET 
version = {{ version }}
WHERE 
id = '{{ id }}' --required
AND workspace = '{{ workspace }}' --required
RETURNING
id,
dashboard_id,
version;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_latest_version"
    values={[
        { label: 'get_latest_version', value: 'get_latest_version' }
    ]}
>
<TabItem value="get_latest_version">

Get latest version of provider analytics dashboard.

```sql
EXEC databricks_workspace.marketplace.provider_provider_analytics_dashboards.get_latest_version 
@workspace='{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

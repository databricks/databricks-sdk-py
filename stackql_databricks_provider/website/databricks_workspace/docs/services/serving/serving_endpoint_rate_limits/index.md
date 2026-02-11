---
title: serving_endpoint_rate_limits
hide_title: false
hide_table_of_contents: false
keywords:
  - serving_endpoint_rate_limits
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

Creates, updates, deletes, gets or lists a <code>serving_endpoint_rate_limits</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serving_endpoint_rate_limits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.serving.serving_endpoint_rate_limits" /></td></tr>
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
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deprecated: Please use AI Gateway to manage rate limits instead.<br /><br />:param name: str<br />  The name of the serving endpoint whose rate limits are being updated. This field is required.<br />:param rate_limits: List[:class:`RateLimit`] (optional)<br />  The list of endpoint rate limits.<br /><br />:returns: :class:`PutResponse`</td>
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
    <td>The name of the serving endpoint whose rate limits are being updated. This field is required.</td>
</tr>
</tbody>
</table>

## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Deprecated: Please use AI Gateway to manage rate limits instead.<br /><br />:param name: str<br />  The name of the serving endpoint whose rate limits are being updated. This field is required.<br />:param rate_limits: List[:class:`RateLimit`] (optional)<br />  The list of endpoint rate limits.<br /><br />:returns: :class:`PutResponse`

```sql
REPLACE databricks_workspace.serving.serving_endpoint_rate_limits
SET 
data__rate_limits = '{{ rate_limits }}'
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
rate_limits;
```
</TabItem>
</Tabs>

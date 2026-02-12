---
title: serving_endpoints_http_request
hide_title: false
hide_table_of_contents: false
keywords:
  - serving_endpoints_http_request
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

Creates, updates, deletes, gets or lists a <code>serving_endpoints_http_request</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serving_endpoints_http_request</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.serving.serving_endpoints_http_request" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="serving_endpoints_http_request"
    values={[
        { label: 'serving_endpoints_http_request', value: 'serving_endpoints_http_request' }
    ]}
>
<TabItem value="serving_endpoints_http_request">

<SchemaTable fields={[
  {
    "name": "contents",
    "type": "string",
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
    <td><a href="#serving_endpoints_http_request"><CopyableCode code="serving_endpoints_http_request" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Make external services call using the credentials stored in UC Connection.</td>
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
    defaultValue="serving_endpoints_http_request"
    values={[
        { label: 'serving_endpoints_http_request', value: 'serving_endpoints_http_request' }
    ]}
>
<TabItem value="serving_endpoints_http_request">

Make external services call using the credentials stored in UC Connection.

```sql
SELECT
contents
FROM databricks_workspace.serving.serving_endpoints_http_request
WHERE deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>

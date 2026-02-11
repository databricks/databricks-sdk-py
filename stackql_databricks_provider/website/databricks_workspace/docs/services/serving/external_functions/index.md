---
title: external_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - external_functions
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

Creates, updates, deletes, gets or lists an <code>external_functions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>external_functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.serving.external_functions" /></td></tr>
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
    <td><a href="#http_request"><CopyableCode code="http_request" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-method"><code>method</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Make external services call using the credentials stored in UC Connection.<br /><br />:param connection_name: str<br />  The connection name to use. This is required to identify the external connection.<br />:param method: :class:`ExternalFunctionRequestHttpMethod`<br />  The HTTP method to use (e.g., 'GET', 'POST').<br />:param path: str<br />  The relative path for the API endpoint. This is required.<br />:param headers: str (optional)<br />  Additional headers for the request. If not provided, only auth headers from connections would be<br />  passed.<br />:param json: str (optional)<br />  The JSON payload to send in the request body.<br />:param params: str (optional)<br />  Query parameters for the request.<br /><br />:returns: :class:`HttpRequestResponse`</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="http_request"
    values={[
        { label: 'http_request', value: 'http_request' }
    ]}
>
<TabItem value="http_request">

Make external services call using the credentials stored in UC Connection.<br /><br />:param connection_name: str<br />  The connection name to use. This is required to identify the external connection.<br />:param method: :class:`ExternalFunctionRequestHttpMethod`<br />  The HTTP method to use (e.g., 'GET', 'POST').<br />:param path: str<br />  The relative path for the API endpoint. This is required.<br />:param headers: str (optional)<br />  Additional headers for the request. If not provided, only auth headers from connections would be<br />  passed.<br />:param json: str (optional)<br />  The JSON payload to send in the request body.<br />:param params: str (optional)<br />  Query parameters for the request.<br /><br />:returns: :class:`HttpRequestResponse`

```sql
EXEC databricks_workspace.serving.external_functions.http_request 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"connection_name": "{{ connection_name }}", 
"method": "{{ method }}", 
"path": "{{ path }}", 
"json": "{{ json }}", 
"params": "{{ params }}"
}'
;
```
</TabItem>
</Tabs>

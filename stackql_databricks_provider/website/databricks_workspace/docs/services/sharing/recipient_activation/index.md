---
title: recipient_activation
hide_title: false
hide_table_of_contents: false
keywords:
  - recipient_activation
  - sharing
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

Creates, updates, deletes, gets or lists a <code>recipient_activation</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recipient_activation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sharing.recipient_activation" /></td></tr>
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
    <td><a href="#get_url"><CopyableCode code="get_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-activation_url"><code>activation_url</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets an activation URL for a share.</td>
</tr>
<tr>
    <td><a href="#retrieve_token"><CopyableCode code="retrieve_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-activation_url"><code>activation_url</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieve access token with an activation url. This is a public API without any authentication.</td>
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
<tr id="parameter-activation_url">
    <td><CopyableCode code="activation_url" /></td>
    <td><code>string</code></td>
    <td>The one time activation url. It also accepts activation token.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_url"
    values={[
        { label: 'get_url', value: 'get_url' },
        { label: 'retrieve_token', value: 'retrieve_token' }
    ]}
>
<TabItem value="get_url">

Gets an activation URL for a share.

```sql
EXEC databricks_workspace.sharing.recipient_activation.get_url 
@activation_url='{{ activation_url }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="retrieve_token">

Retrieve access token with an activation url. This is a public API without any authentication.

```sql
EXEC databricks_workspace.sharing.recipient_activation.retrieve_token 
@activation_url='{{ activation_url }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

---
title: workspace_network_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_network_configuration
  - settings
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>workspace_network_configuration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_network_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.workspace_network_configuration" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_workspace_network_option_rpc"
    values={[
        { label: 'get_workspace_network_option_rpc', value: 'get_workspace_network_option_rpc' }
    ]}
>
<TabItem value="get_workspace_network_option_rpc">

<SchemaTable fields={[
  {
    "name": "network_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "The workspace ID."
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
    <td><a href="#get_workspace_network_option_rpc"><CopyableCode code="get_workspace_network_option_rpc" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a></td>
    <td></td>
    <td>Gets the network option for a workspace. Every workspace has exactly one network policy binding, with</td>
</tr>
<tr>
    <td><a href="#update_workspace_network_option_rpc"><CopyableCode code="update_workspace_network_option_rpc" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-data__workspace_network_option"><code>data__workspace_network_option</code></a></td>
    <td></td>
    <td>Updates the network option for a workspace. This operation associates the workspace with the specified</td>
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
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_id">
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>integer</code></td>
    <td>The workspace ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_workspace_network_option_rpc"
    values={[
        { label: 'get_workspace_network_option_rpc', value: 'get_workspace_network_option_rpc' }
    ]}
>
<TabItem value="get_workspace_network_option_rpc">

Gets the network option for a workspace. Every workspace has exactly one network policy binding, with

```sql
SELECT
network_policy_id,
workspace_id
FROM databricks_account.settings.workspace_network_configuration
WHERE account_id = '{{ account_id }}' -- required
AND workspace_id = '{{ workspace_id }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_workspace_network_option_rpc"
    values={[
        { label: 'update_workspace_network_option_rpc', value: 'update_workspace_network_option_rpc' }
    ]}
>
<TabItem value="update_workspace_network_option_rpc">

Updates the network option for a workspace. This operation associates the workspace with the specified

```sql
REPLACE databricks_account.settings.workspace_network_configuration
SET 
data__workspace_network_option = '{{ workspace_network_option }}'
WHERE 
account_id = '{{ account_id }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND data__workspace_network_option = '{{ workspace_network_option }}' --required
RETURNING
network_policy_id,
workspace_id;
```
</TabItem>
</Tabs>

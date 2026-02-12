---
title: workspace_config
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_config
  - settings
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

Creates, updates, deletes, gets or lists a <code>workspace_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settings.workspace_config" /></td></tr>
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
    <td><a href="#get_workspace_config"><CopyableCode code="get_workspace_config" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-keys"><code>keys</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the configuration status for a workspace.</td>
</tr>
<tr>
    <td><a href="#set_workspace_config"><CopyableCode code="set_workspace_config" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-contents"><code>contents</code></a></td>
    <td></td>
    <td>Sets the configuration status for a workspace, including enabling or disabling it.</td>
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
<tr id="parameter-keys">
    <td><CopyableCode code="keys" /></td>
    <td><code>string</code></td>
    <td>:returns: Dict[str,str]</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_workspace_config"
    values={[
        { label: 'get_workspace_config', value: 'get_workspace_config' },
        { label: 'set_workspace_config', value: 'set_workspace_config' }
    ]}
>
<TabItem value="get_workspace_config">

Gets the configuration status for a workspace.

```sql
EXEC databricks_workspace.settings.workspace_config.get_workspace_config 
@keys='{{ keys }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="set_workspace_config">

Sets the configuration status for a workspace, including enabling or disabling it.

```sql
EXEC databricks_workspace.settings.workspace_config.set_workspace_config 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"contents": "{{ contents }}"
}'
;
```
</TabItem>
</Tabs>

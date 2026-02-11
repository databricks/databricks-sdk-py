---
title: global_init_scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - global_init_scripts
  - compute
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

Creates, updates, deletes, gets or lists a <code>global_init_scripts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_init_scripts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.global_init_scripts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the script"
  },
  {
    "name": "script_id",
    "type": "string",
    "description": "The global init script ID."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": ""
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The username of the user who created the script."
  },
  {
    "name": "enabled",
    "type": "boolean",
    "description": "Specifies whether the script is enabled. The script runs only if enabled."
  },
  {
    "name": "position",
    "type": "integer",
    "description": "The position of a script, where 0 represents the first script to run, 1 is the second script to run, in ascending order."
  },
  {
    "name": "script",
    "type": "string",
    "description": "The Base64-encoded content of the script."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time when the script was updated, represented as a Unix timestamp in milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "The username of the user who last updated the script"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the script"
  },
  {
    "name": "script_id",
    "type": "string",
    "description": "The global init script ID."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": ""
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The username of the user who created the script."
  },
  {
    "name": "enabled",
    "type": "boolean",
    "description": "Specifies whether the script is enabled. The script runs only if enabled."
  },
  {
    "name": "position",
    "type": "integer",
    "description": "The position of a script, where 0 represents the first script to run, 1 is the second script to run, in ascending order."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time when the script was updated, represented as a Unix timestamp in milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "The username of the user who last updated the script"
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
    <td><a href="#parameter-script_id"><code>script_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets all the details of a script, including its Base64-encoded contents.<br /><br />:param script_id: str<br />  The ID of the global init script.<br /><br />:returns: :class:`GlobalInitScriptDetailsWithContent`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a list of all global init scripts for this workspace. This returns all properties for each script<br />but **not** the script contents. To retrieve the contents of a script, use the [get a global init<br />script](:method:globalinitscripts/get) operation.<br /><br /><br />:returns: Iterator over :class:`GlobalInitScriptDetails`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__name"><code>data__name</code></a>, <a href="#parameter-data__script"><code>data__script</code></a></td>
    <td></td>
    <td>Creates a new global init script in this workspace.<br /><br />:param name: str<br />  The name of the script<br />:param script: str<br />  The Base64-encoded content of the script.<br />:param enabled: bool (optional)<br />  Specifies whether the script is enabled. The script runs only if enabled.<br />:param position: int (optional)<br />  The position of a global init script, where 0 represents the first script to run, 1 is the second<br />  script to run, in ascending order.<br /><br />  If you omit the numeric position for a new global init script, it defaults to last position. It will<br />  run after all current scripts. Setting any value greater than the position of the last script is<br />  equivalent to the last position. Example: Take three existing scripts with positions 0, 1, and 2.<br />  Any position of (3) or greater puts the script in the last position. If an explicit position value<br />  conflicts with an existing script value, your request succeeds, but the original script at that<br />  position and all later scripts have their positions incremented by 1.<br /><br />:returns: :class:`CreateResponse`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-script_id"><code>script_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__name"><code>data__name</code></a>, <a href="#parameter-data__script"><code>data__script</code></a></td>
    <td></td>
    <td>Updates a global init script, specifying only the fields to change. All fields are optional.<br />Unspecified fields retain their current value.<br /><br />:param script_id: str<br />  The ID of the global init script.<br />:param name: str<br />  The name of the script<br />:param script: str<br />  The Base64-encoded content of the script.<br />:param enabled: bool (optional)<br />  Specifies whether the script is enabled. The script runs only if enabled.<br />:param position: int (optional)<br />  The position of a script, where 0 represents the first script to run, 1 is the second script to run,<br />  in ascending order. To move the script to run first, set its position to 0.<br /><br />  To move the script to the end, set its position to any value greater or equal to the position of the<br />  last script. Example, three existing scripts with positions 0, 1, and 2. Any position value of 2 or<br />  greater puts the script in the last position (2).<br /><br />  If an explicit position value conflicts with an existing script, your request succeeds, but the<br />  original script at that position and all later scripts have their positions incremented by 1.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-script_id"><code>script_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a global init script.<br /><br />:param script_id: str<br />  The ID of the global init script.</td>
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
<tr id="parameter-script_id">
    <td><CopyableCode code="script_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the global init script.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets all the details of a script, including its Base64-encoded contents.<br /><br />:param script_id: str<br />  The ID of the global init script.<br /><br />:returns: :class:`GlobalInitScriptDetailsWithContent`

```sql
SELECT
name,
script_id,
created_at,
created_by,
enabled,
position,
script,
updated_at,
updated_by
FROM databricks_workspace.compute.global_init_scripts
WHERE script_id = '{{ script_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of all global init scripts for this workspace. This returns all properties for each script<br />but **not** the script contents. To retrieve the contents of a script, use the [get a global init<br />script](:method:globalinitscripts/get) operation.<br /><br /><br />:returns: Iterator over :class:`GlobalInitScriptDetails`

```sql
SELECT
name,
script_id,
created_at,
created_by,
enabled,
position,
updated_at,
updated_by
FROM databricks_workspace.compute.global_init_scripts
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Creates a new global init script in this workspace.<br /><br />:param name: str<br />  The name of the script<br />:param script: str<br />  The Base64-encoded content of the script.<br />:param enabled: bool (optional)<br />  Specifies whether the script is enabled. The script runs only if enabled.<br />:param position: int (optional)<br />  The position of a global init script, where 0 represents the first script to run, 1 is the second<br />  script to run, in ascending order.<br /><br />  If you omit the numeric position for a new global init script, it defaults to last position. It will<br />  run after all current scripts. Setting any value greater than the position of the last script is<br />  equivalent to the last position. Example: Take three existing scripts with positions 0, 1, and 2.<br />  Any position of (3) or greater puts the script in the last position. If an explicit position value<br />  conflicts with an existing script value, your request succeeds, but the original script at that<br />  position and all later scripts have their positions incremented by 1.<br /><br />:returns: :class:`CreateResponse`

```sql
INSERT INTO databricks_workspace.compute.global_init_scripts (
data__name,
data__script,
data__enabled,
data__position,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ script }}' /* required */,
'{{ enabled }}',
'{{ position }}',
'{{ deployment_name }}'
RETURNING
script_id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: global_init_scripts
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the global_init_scripts resource.
    - name: name
      value: string
      description: |
        The name of the script
    - name: script
      value: string
      description: |
        The Base64-encoded content of the script.
    - name: enabled
      value: string
      description: |
        Specifies whether the script is enabled. The script runs only if enabled.
    - name: position
      value: string
      description: |
        The position of a global init script, where 0 represents the first script to run, 1 is the second script to run, in ascending order. If you omit the numeric position for a new global init script, it defaults to last position. It will run after all current scripts. Setting any value greater than the position of the last script is equivalent to the last position. Example: Take three existing scripts with positions 0, 1, and 2. Any position of (3) or greater puts the script in the last position. If an explicit position value conflicts with an existing script value, your request succeeds, but the original script at that position and all later scripts have their positions incremented by 1.
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates a global init script, specifying only the fields to change. All fields are optional.<br />Unspecified fields retain their current value.<br /><br />:param script_id: str<br />  The ID of the global init script.<br />:param name: str<br />  The name of the script<br />:param script: str<br />  The Base64-encoded content of the script.<br />:param enabled: bool (optional)<br />  Specifies whether the script is enabled. The script runs only if enabled.<br />:param position: int (optional)<br />  The position of a script, where 0 represents the first script to run, 1 is the second script to run,<br />  in ascending order. To move the script to run first, set its position to 0.<br /><br />  To move the script to the end, set its position to any value greater or equal to the position of the<br />  last script. Example, three existing scripts with positions 0, 1, and 2. Any position value of 2 or<br />  greater puts the script in the last position (2).<br /><br />  If an explicit position value conflicts with an existing script, your request succeeds, but the<br />  original script at that position and all later scripts have their positions incremented by 1.

```sql
UPDATE databricks_workspace.compute.global_init_scripts
SET 
data__name = '{{ name }}',
data__script = '{{ script }}',
data__enabled = '{{ enabled }}',
data__position = '{{ position }}'
WHERE 
script_id = '{{ script_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__name = '{{ name }}' --required
AND data__script = '{{ script }}' --required;
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

Deletes a global init script.<br /><br />:param script_id: str<br />  The ID of the global init script.

```sql
DELETE FROM databricks_workspace.compute.global_init_scripts
WHERE script_id = '{{ script_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

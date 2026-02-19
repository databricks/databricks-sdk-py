---
title: account_user_preferences
hide_title: false
hide_table_of_contents: false
keywords:
  - account_user_preferences
  - settingsv2
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

Creates, updates, deletes, gets or lists an <code>account_user_preferences</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="account_user_preferences" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settingsv2.account_user_preferences" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_public_account_user_preference"
    values={[
        { label: 'get_public_account_user_preference', value: 'get_public_account_user_preference' }
    ]}
>
<TabItem value="get_public_account_user_preference">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of the setting."
  },
  {
    "name": "user_id",
    "type": "string",
    "description": "User ID of the user."
  },
  {
    "name": "boolean_val",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "value",
        "type": "boolean",
        "description": ""
      }
    ]
  },
  {
    "name": "effective_boolean_val",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "value",
        "type": "boolean",
        "description": ""
      }
    ]
  },
  {
    "name": "effective_string_val",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "value",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "string_val",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "value",
        "type": "string",
        "description": ""
      }
    ]
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
    <td><a href="#get_public_account_user_preference"><CopyableCode code="get_public_account_user_preference" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Get a user preference for a specific user. User preferences are personal settings that allow</td>
</tr>
<tr>
    <td><a href="#patch_public_account_user_preference"><CopyableCode code="patch_public_account_user_preference" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-setting"><code>setting</code></a></td>
    <td></td>
    <td>Update a user preference for a specific user. User preferences are personal settings that allow</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>:param setting: :class:`UserPreference`</td>
</tr>
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>User ID of the user whose setting is being updated.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_public_account_user_preference"
    values={[
        { label: 'get_public_account_user_preference', value: 'get_public_account_user_preference' }
    ]}
>
<TabItem value="get_public_account_user_preference">

Get a user preference for a specific user. User preferences are personal settings that allow

```sql
SELECT
name,
user_id,
boolean_val,
effective_boolean_val,
effective_string_val,
string_val
FROM databricks_account.settingsv2.account_user_preferences
WHERE account_id = '{{ account_id }}' -- required
AND user_id = '{{ user_id }}' -- required
AND name = '{{ name }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="patch_public_account_user_preference"
    values={[
        { label: 'patch_public_account_user_preference', value: 'patch_public_account_user_preference' }
    ]}
>
<TabItem value="patch_public_account_user_preference">

Update a user preference for a specific user. User preferences are personal settings that allow

```sql
UPDATE databricks_account.settingsv2.account_user_preferences
SET 
setting = '{{ setting }}'
WHERE 
account_id = '{{ account_id }}' --required
AND user_id = '{{ user_id }}' --required
AND name = '{{ name }}' --required
AND setting = '{{ setting }}' --required
RETURNING
name,
user_id,
boolean_val,
effective_boolean_val,
effective_string_val,
string_val;
```
</TabItem>
</Tabs>

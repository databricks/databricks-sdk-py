---
title: token_management
hide_title: false
hide_table_of_contents: false
keywords:
  - token_management
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

Creates, updates, deletes, gets or lists a <code>token_management</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>token_management</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settings.token_management" /></td></tr>
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
    "name": "token_info",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "comment",
        "type": "string",
        "description": ""
      },
      {
        "name": "created_by_id",
        "type": "integer",
        "description": "User ID of the user that created the token."
      },
      {
        "name": "created_by_username",
        "type": "string",
        "description": "Username of the user that created the token."
      },
      {
        "name": "creation_time",
        "type": "integer",
        "description": "Timestamp when the token was created."
      },
      {
        "name": "expiry_time",
        "type": "integer",
        "description": "Timestamp when the token expires."
      },
      {
        "name": "last_used_day",
        "type": "integer",
        "description": "Approximate timestamp for the day the token was last used. Accurate up to 1 day."
      },
      {
        "name": "owner_id",
        "type": "integer",
        "description": "User ID of the user that owns the token."
      },
      {
        "name": "token_id",
        "type": "string",
        "description": "ID of the token."
      },
      {
        "name": "workspace_id",
        "type": "integer",
        "description": "If applicable, the ID of the workspace that the token was created in."
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "created_by_id",
    "type": "integer",
    "description": "User ID of the user that created the token."
  },
  {
    "name": "owner_id",
    "type": "integer",
    "description": "User ID of the user that owns the token."
  },
  {
    "name": "token_id",
    "type": "string",
    "description": "ID of the token."
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "If applicable, the ID of the workspace that the token was created in."
  },
  {
    "name": "comment",
    "type": "string",
    "description": ""
  },
  {
    "name": "created_by_username",
    "type": "string",
    "description": "Username of the user that created the token."
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Timestamp when the token was created."
  },
  {
    "name": "expiry_time",
    "type": "integer",
    "description": "Timestamp when the token expires."
  },
  {
    "name": "last_used_day",
    "type": "integer",
    "description": "Approximate timestamp for the day the token was last used. Accurate up to 1 day."
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
    <td><a href="#parameter-token_id"><code>token_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets information about a token, specified by its ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-created_by_id"><code>created_by_id</code></a>, <a href="#parameter-created_by_username"><code>created_by_username</code></a></td>
    <td>Lists all tokens associated with the specified workspace or user.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__application_id"><code>data__application_id</code></a></td>
    <td></td>
    <td>Creates a token on behalf of a service principal.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-token_id"><code>token_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a token, specified by its ID.</td>
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
<tr id="parameter-token_id">
    <td><CopyableCode code="token_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the token to revoke.</td>
</tr>
<tr id="parameter-created_by_id">
    <td><CopyableCode code="created_by_id" /></td>
    <td><code>string</code></td>
    <td>User ID of the user that created the token.</td>
</tr>
<tr id="parameter-created_by_username">
    <td><CopyableCode code="created_by_username" /></td>
    <td><code>string</code></td>
    <td>Username of the user that created the token.</td>
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

Gets information about a token, specified by its ID.

```sql
SELECT
token_info
FROM databricks_workspace.settings.token_management
WHERE token_id = '{{ token_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all tokens associated with the specified workspace or user.

```sql
SELECT
created_by_id,
owner_id,
token_id,
workspace_id,
comment,
created_by_username,
creation_time,
expiry_time,
last_used_day
FROM databricks_workspace.settings.token_management
WHERE deployment_name = '{{ deployment_name }}' -- required
AND created_by_id = '{{ created_by_id }}'
AND created_by_username = '{{ created_by_username }}'
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

Creates a token on behalf of a service principal.

```sql
INSERT INTO databricks_workspace.settings.token_management (
data__application_id,
data__comment,
data__lifetime_seconds,
deployment_name
)
SELECT 
'{{ application_id }}' /* required */,
'{{ comment }}',
'{{ lifetime_seconds }}',
'{{ deployment_name }}'
RETURNING
token_info,
token_value
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: token_management
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the token_management resource.
    - name: application_id
      value: string
      description: |
        Application ID of the service principal.
    - name: comment
      value: string
      description: |
        Comment that describes the purpose of the token.
    - name: lifetime_seconds
      value: string
      description: |
        The number of seconds before the token expires.
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

Deletes a token, specified by its ID.

```sql
DELETE FROM databricks_workspace.settings.token_management
WHERE token_id = '{{ token_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

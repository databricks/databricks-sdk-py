---
title: workspace_assignment
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_assignment
  - iam
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

Creates, updates, deletes, gets or lists a <code>workspace_assignment</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_assignment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.workspace_assignment" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "error",
    "type": "string",
    "description": "Error response associated with a workspace permission assignment, if any."
  },
  {
    "name": "permissions",
    "type": "array",
    "description": "The permissions level of the principal."
  },
  {
    "name": "principal",
    "type": "object",
    "description": "Information about the principal assigned to the workspace.",
    "children": [
      {
        "name": "display_name",
        "type": "string",
        "description": "The display name of the principal."
      },
      {
        "name": "group_name",
        "type": "string",
        "description": "The group name of the group. Present only if the principal is a group."
      },
      {
        "name": "principal_id",
        "type": "integer",
        "description": "The unique, opaque id of the principal."
      },
      {
        "name": "service_principal_name",
        "type": "string",
        "description": "The name of the service principal. Present only if the principal is a service principal."
      },
      {
        "name": "user_name",
        "type": "string",
        "description": "The username of the user. Present only if the principal is a user."
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a></td>
    <td></td>
    <td>Get the permission assignments for the specified Databricks account and Databricks workspace.<br /><br />:param workspace_id: int<br />  The workspace ID for the account.<br /><br />:returns: Iterator over :class:`PermissionAssignment`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td></td>
    <td>Creates or updates the workspace permissions assignment in a given account and workspace for the<br />specified principal.<br /><br />:param workspace_id: int<br />  The workspace ID.<br />:param principal_id: int<br />  The ID of the user, service principal, or group.<br />:param permissions: List[:class:`WorkspacePermission`] (optional)<br />  Array of permissions assignments to update on the workspace. Valid values are "USER" and "ADMIN"<br />  (case-sensitive). If both "USER" and "ADMIN" are provided, "ADMIN" takes precedence. Other values<br />  will be ignored. Note that excluding this field, or providing unsupported values, will have the same<br />  effect as providing an empty list, which will result in the deletion of all permissions for the<br />  principal.<br /><br />:returns: :class:`PermissionAssignment`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td></td>
    <td>Deletes the workspace permissions assignment in a given account and workspace for the specified<br />principal.<br /><br />:param workspace_id: int<br />  The workspace ID for the account.<br />:param principal_id: int<br />  The ID of the user, service principal, or group.</td>
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
<tr id="parameter-principal_id">
    <td><CopyableCode code="principal_id" /></td>
    <td><code>integer</code></td>
    <td>The ID of the user, service principal, or group.</td>
</tr>
<tr id="parameter-workspace_id">
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>integer</code></td>
    <td>The workspace ID for the account.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Get the permission assignments for the specified Databricks account and Databricks workspace.<br /><br />:param workspace_id: int<br />  The workspace ID for the account.<br /><br />:returns: Iterator over :class:`PermissionAssignment`

```sql
SELECT
error,
permissions,
principal
FROM databricks_account.iam.workspace_assignment
WHERE account_id = '{{ account_id }}' -- required
AND workspace_id = '{{ workspace_id }}' -- required
;
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

Creates or updates the workspace permissions assignment in a given account and workspace for the<br />specified principal.<br /><br />:param workspace_id: int<br />  The workspace ID.<br />:param principal_id: int<br />  The ID of the user, service principal, or group.<br />:param permissions: List[:class:`WorkspacePermission`] (optional)<br />  Array of permissions assignments to update on the workspace. Valid values are "USER" and "ADMIN"<br />  (case-sensitive). If both "USER" and "ADMIN" are provided, "ADMIN" takes precedence. Other values<br />  will be ignored. Note that excluding this field, or providing unsupported values, will have the same<br />  effect as providing an empty list, which will result in the deletion of all permissions for the<br />  principal.<br /><br />:returns: :class:`PermissionAssignment`

```sql
REPLACE databricks_account.iam.workspace_assignment
SET 
data__permissions = '{{ permissions }}'
WHERE 
account_id = '{{ account_id }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND principal_id = '{{ principal_id }}' --required
RETURNING
error,
permissions,
principal;
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

Deletes the workspace permissions assignment in a given account and workspace for the specified<br />principal.<br /><br />:param workspace_id: int<br />  The workspace ID for the account.<br />:param principal_id: int<br />  The ID of the user, service principal, or group.

```sql
DELETE FROM databricks_account.iam.workspace_assignment
WHERE account_id = '{{ account_id }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND principal_id = '{{ principal_id }}' --required
;
```
</TabItem>
</Tabs>

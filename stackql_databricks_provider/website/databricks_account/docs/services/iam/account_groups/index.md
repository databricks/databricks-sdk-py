---
title: account_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - account_groups
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

Creates, updates, deletes, gets or lists an <code>account_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="account_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.account_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="account_groups_v2_get"
    values={[
        { label: 'account_groups_v2_get', value: 'account_groups_v2_get' },
        { label: 'account_groups_v2_list', value: 'account_groups_v2_list' }
    ]}
>
<TabItem value="account_groups_v2_get">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Databricks group ID"
  },
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "displayName",
    "type": "string",
    "description": "String that represents a human-readable group name"
  },
  {
    "name": "externalId",
    "type": "string",
    "description": "external_id should be unique for identifying groups"
  },
  {
    "name": "members",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "display",
        "type": "string",
        "description": ""
      },
      {
        "name": "primary",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "$ref",
        "type": "string",
        "description": ""
      },
      {
        "name": "type",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "meta",
    "type": "object",
    "description": "Container for the group identifier. Workspace local versus account.",
    "children": [
      {
        "name": "resourceType",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "roles",
    "type": "array",
    "description": "Indicates if the group has the admin role.",
    "children": [
      {
        "name": "display",
        "type": "string",
        "description": ""
      },
      {
        "name": "primary",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "$ref",
        "type": "string",
        "description": ""
      },
      {
        "name": "type",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": ""
      }
    ]
  }
]} />
</TabItem>
<TabItem value="account_groups_v2_list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Databricks group ID"
  },
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "displayName",
    "type": "string",
    "description": "String that represents a human-readable group name"
  },
  {
    "name": "externalId",
    "type": "string",
    "description": "external_id should be unique for identifying groups"
  },
  {
    "name": "members",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "display",
        "type": "string",
        "description": ""
      },
      {
        "name": "primary",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "$ref",
        "type": "string",
        "description": ""
      },
      {
        "name": "type",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "meta",
    "type": "object",
    "description": "Container for the group identifier. Workspace local versus account.",
    "children": [
      {
        "name": "resourceType",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "roles",
    "type": "array",
    "description": "Indicates if the group has the admin role.",
    "children": [
      {
        "name": "display",
        "type": "string",
        "description": ""
      },
      {
        "name": "primary",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "$ref",
        "type": "string",
        "description": ""
      },
      {
        "name": "type",
        "type": "string",
        "description": ""
      },
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
    <td><a href="#account_groups_v2_get"><CopyableCode code="account_groups_v2_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Gets the information for a specific group in the Databricks account.</td>
</tr>
<tr>
    <td><a href="#account_groups_v2_list"><CopyableCode code="account_groups_v2_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-attributes"><code>attributes</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-excluded_attributes"><code>excluded_attributes</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-sort_by"><code>sort_by</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a>, <a href="#parameter-start_index"><code>start_index</code></a></td>
    <td>Gets all details of the groups associated with the Databricks account. As of 08/22/2025, this endpoint</td>
</tr>
<tr>
    <td><a href="#account_groups_v2_create"><CopyableCode code="account_groups_v2_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a group in the Databricks account with a unique name, using the supplied group details.</td>
</tr>
<tr>
    <td><a href="#account_groups_v2_patch"><CopyableCode code="account_groups_v2_patch" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Partially updates the details of a group.</td>
</tr>
<tr>
    <td><a href="#account_groups_v2_update"><CopyableCode code="account_groups_v2_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Updates the details of a group by replacing the entire group entity.</td>
</tr>
<tr>
    <td><a href="#account_groups_v2_delete"><CopyableCode code="account_groups_v2_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Deletes a group from the Databricks account.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Unique ID for a group in the Databricks account.</td>
</tr>
<tr id="parameter-attributes">
    <td><CopyableCode code="attributes" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of attributes to return in response.</td>
</tr>
<tr id="parameter-count">
    <td><CopyableCode code="count" /></td>
    <td><code>string</code></td>
    <td>Desired number of results per page. Default is 10000.</td>
</tr>
<tr id="parameter-excluded_attributes">
    <td><CopyableCode code="excluded_attributes" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of attributes to exclude in response.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Query by which the results have to be filtered. Supported operators are equals(`eq`), contains(`co`), starts with(`sw`) and not equals(`ne`). Additionally, simple expressions can be formed using logical operators - `and` and `or`. The [SCIM RFC] has more details but we currently only support simple expressions. [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2</td>
</tr>
<tr id="parameter-sort_by">
    <td><CopyableCode code="sort_by" /></td>
    <td><code>string</code></td>
    <td>Attribute to sort the results.</td>
</tr>
<tr id="parameter-sort_order">
    <td><CopyableCode code="sort_order" /></td>
    <td><code>string</code></td>
    <td>The order to sort the results.</td>
</tr>
<tr id="parameter-start_index">
    <td><CopyableCode code="start_index" /></td>
    <td><code>string</code></td>
    <td>Specifies the index of the first result. First item is number 1.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="account_groups_v2_get"
    values={[
        { label: 'account_groups_v2_get', value: 'account_groups_v2_get' },
        { label: 'account_groups_v2_list', value: 'account_groups_v2_list' }
    ]}
>
<TabItem value="account_groups_v2_get">

Gets the information for a specific group in the Databricks account.

```sql
SELECT
id,
account_id,
displayName,
externalId,
members,
meta,
roles
FROM databricks_account.iam.account_groups
WHERE account_id = '{{ account_id }}' -- required
AND id = '{{ id }}' -- required
;
```
</TabItem>
<TabItem value="account_groups_v2_list">

Gets all details of the groups associated with the Databricks account. As of 08/22/2025, this endpoint

```sql
SELECT
id,
account_id,
displayName,
externalId,
members,
meta,
roles
FROM databricks_account.iam.account_groups
WHERE account_id = '{{ account_id }}' -- required
AND attributes = '{{ attributes }}'
AND count = '{{ count }}'
AND excluded_attributes = '{{ excluded_attributes }}'
AND filter = '{{ filter }}'
AND sort_by = '{{ sort_by }}'
AND sort_order = '{{ sort_order }}'
AND start_index = '{{ start_index }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="account_groups_v2_create"
    values={[
        { label: 'account_groups_v2_create', value: 'account_groups_v2_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="account_groups_v2_create">

Creates a group in the Databricks account with a unique name, using the supplied group details.

```sql
INSERT INTO databricks_account.iam.account_groups (
display_name,
external_id,
id,
members,
meta,
roles,
account_id
)
SELECT 
'{{ display_name }}',
'{{ external_id }}',
'{{ id }}',
'{{ members }}',
'{{ meta }}',
'{{ roles }}',
'{{ account_id }}'
RETURNING
id,
account_id,
displayName,
externalId,
members,
meta,
roles
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: account_groups
  props:
    - name: account_id
      value: string
      description: Required parameter for the account_groups resource.
    - name: display_name
      value: string
      description: |
        String that represents a human-readable group name
    - name: external_id
      value: string
      description: |
        :param id: str (optional) Databricks group ID
    - name: id
      value: string
    - name: members
      value: string
      description: |
        :param meta: :class:`ResourceMeta` (optional) Container for the group identifier. Workspace local versus account.
    - name: meta
      value: string
    - name: roles
      value: string
      description: |
        Indicates if the group has the admin role.
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="account_groups_v2_patch"
    values={[
        { label: 'account_groups_v2_patch', value: 'account_groups_v2_patch' }
    ]}
>
<TabItem value="account_groups_v2_patch">

Partially updates the details of a group.

```sql
UPDATE databricks_account.iam.account_groups
SET 
operations = '{{ operations }}',
schemas = '{{ schemas }}'
WHERE 
account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="account_groups_v2_update"
    values={[
        { label: 'account_groups_v2_update', value: 'account_groups_v2_update' }
    ]}
>
<TabItem value="account_groups_v2_update">

Updates the details of a group by replacing the entire group entity.

```sql
REPLACE databricks_account.iam.account_groups
SET 
display_name = '{{ display_name }}',
external_id = '{{ external_id }}',
members = '{{ members }}',
meta = '{{ meta }}',
roles = '{{ roles }}'
WHERE 
account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="account_groups_v2_delete"
    values={[
        { label: 'account_groups_v2_delete', value: 'account_groups_v2_delete' }
    ]}
>
<TabItem value="account_groups_v2_delete">

Deletes a group from the Databricks account.

```sql
DELETE FROM databricks_account.iam.account_groups
WHERE account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required
;
```
</TabItem>
</Tabs>

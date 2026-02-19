---
title: account_ip_access_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - account_ip_access_lists
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

Creates, updates, deletes, gets or lists an <code>account_ip_access_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="account_ip_access_lists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.account_ip_access_lists" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="account_ip_access_lists_get"
    values={[
        { label: 'account_ip_access_lists_get', value: 'account_ip_access_lists_get' },
        { label: 'account_ip_access_lists_list', value: 'account_ip_access_lists_list' }
    ]}
>
<TabItem value="account_ip_access_lists_get">

<SchemaTable fields={[
  {
    "name": "list_id",
    "type": "string",
    "description": "Universally unique identifier (UUID) of the IP access list."
  },
  {
    "name": "address_count",
    "type": "integer",
    "description": "Total number of IP or CIDR values."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Creation timestamp in milliseconds."
  },
  {
    "name": "created_by",
    "type": "integer",
    "description": "User ID of the user who created this list."
  },
  {
    "name": "enabled",
    "type": "boolean",
    "description": "Specifies whether this IP access list is enabled."
  },
  {
    "name": "ip_addresses",
    "type": "array",
    "description": ""
  },
  {
    "name": "label",
    "type": "string",
    "description": "Label for the IP access list. This **cannot** be empty."
  },
  {
    "name": "list_type",
    "type": "string",
    "description": "Type of IP access list. Valid values are as follows and are case-sensitive:<br /><br />* `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or<br />range. IP addresses in the block list are excluded even if they are included in an allow list. (ALLOW, BLOCK)"
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Update timestamp in milliseconds."
  },
  {
    "name": "updated_by",
    "type": "integer",
    "description": "User ID of the user who updated this list."
  }
]} />
</TabItem>
<TabItem value="account_ip_access_lists_list">

<SchemaTable fields={[
  {
    "name": "list_id",
    "type": "string",
    "description": "Universally unique identifier (UUID) of the IP access list."
  },
  {
    "name": "address_count",
    "type": "integer",
    "description": "Total number of IP or CIDR values."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Creation timestamp in milliseconds."
  },
  {
    "name": "created_by",
    "type": "integer",
    "description": "User ID of the user who created this list."
  },
  {
    "name": "enabled",
    "type": "boolean",
    "description": "Specifies whether this IP access list is enabled."
  },
  {
    "name": "ip_addresses",
    "type": "array",
    "description": ""
  },
  {
    "name": "label",
    "type": "string",
    "description": "Label for the IP access list. This **cannot** be empty."
  },
  {
    "name": "list_type",
    "type": "string",
    "description": "Type of IP access list. Valid values are as follows and are case-sensitive:<br /><br />* `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or<br />range. IP addresses in the block list are excluded even if they are included in an allow list. (ALLOW, BLOCK)"
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Update timestamp in milliseconds."
  },
  {
    "name": "updated_by",
    "type": "integer",
    "description": "User ID of the user who updated this list."
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
    <td><a href="#account_ip_access_lists_get"><CopyableCode code="account_ip_access_lists_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ip_access_list_id"><code>ip_access_list_id</code></a></td>
    <td></td>
    <td>Gets an IP access list, specified by its list ID.</td>
</tr>
<tr>
    <td><a href="#account_ip_access_lists_list"><CopyableCode code="account_ip_access_lists_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Gets all IP access lists for the specified account.</td>
</tr>
<tr>
    <td><a href="#account_ip_access_lists_create"><CopyableCode code="account_ip_access_lists_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-label"><code>label</code></a>, <a href="#parameter-list_type"><code>list_type</code></a></td>
    <td></td>
    <td>Creates an IP access list for the account.</td>
</tr>
<tr>
    <td><a href="#account_ip_access_lists_update"><CopyableCode code="account_ip_access_lists_update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ip_access_list_id"><code>ip_access_list_id</code></a></td>
    <td></td>
    <td>Updates an existing IP access list, specified by its ID.</td>
</tr>
<tr>
    <td><a href="#account_ip_access_lists_replace"><CopyableCode code="account_ip_access_lists_replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ip_access_list_id"><code>ip_access_list_id</code></a>, <a href="#parameter-label"><code>label</code></a>, <a href="#parameter-list_type"><code>list_type</code></a>, <a href="#parameter-enabled"><code>enabled</code></a></td>
    <td></td>
    <td>Replaces an IP access list, specified by its ID.</td>
</tr>
<tr>
    <td><a href="#account_ip_access_lists_delete"><CopyableCode code="account_ip_access_lists_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ip_access_list_id"><code>ip_access_list_id</code></a></td>
    <td></td>
    <td>Deletes an IP access list, specified by its list ID.</td>
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
<tr id="parameter-ip_access_list_id">
    <td><CopyableCode code="ip_access_list_id" /></td>
    <td><code>string</code></td>
    <td>The ID for the corresponding IP access list</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="account_ip_access_lists_get"
    values={[
        { label: 'account_ip_access_lists_get', value: 'account_ip_access_lists_get' },
        { label: 'account_ip_access_lists_list', value: 'account_ip_access_lists_list' }
    ]}
>
<TabItem value="account_ip_access_lists_get">

Gets an IP access list, specified by its list ID.

```sql
SELECT
list_id,
address_count,
created_at,
created_by,
enabled,
ip_addresses,
label,
list_type,
updated_at,
updated_by
FROM databricks_account.settings.account_ip_access_lists
WHERE account_id = '{{ account_id }}' -- required
AND ip_access_list_id = '{{ ip_access_list_id }}' -- required
;
```
</TabItem>
<TabItem value="account_ip_access_lists_list">

Gets all IP access lists for the specified account.

```sql
SELECT
list_id,
address_count,
created_at,
created_by,
enabled,
ip_addresses,
label,
list_type,
updated_at,
updated_by
FROM databricks_account.settings.account_ip_access_lists
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="account_ip_access_lists_create"
    values={[
        { label: 'account_ip_access_lists_create', value: 'account_ip_access_lists_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="account_ip_access_lists_create">

Creates an IP access list for the account.

```sql
INSERT INTO databricks_account.settings.account_ip_access_lists (
label,
list_type,
ip_addresses,
account_id
)
SELECT 
'{{ label }}' /* required */,
'{{ list_type }}' /* required */,
'{{ ip_addresses }}',
'{{ account_id }}'
RETURNING
ip_access_list
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: account_ip_access_lists
  props:
    - name: account_id
      value: string
      description: Required parameter for the account_ip_access_lists resource.
    - name: label
      value: string
      description: |
        Label for the IP access list. This **cannot** be empty.
    - name: list_type
      value: string
      description: |
        :param ip_addresses: List[str] (optional)
    - name: ip_addresses
      value: string
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="account_ip_access_lists_update"
    values={[
        { label: 'account_ip_access_lists_update', value: 'account_ip_access_lists_update' }
    ]}
>
<TabItem value="account_ip_access_lists_update">

Updates an existing IP access list, specified by its ID.

```sql
UPDATE databricks_account.settings.account_ip_access_lists
SET 
enabled = '{{ enabled }}',
ip_addresses = '{{ ip_addresses }}',
label = '{{ label }}',
list_type = '{{ list_type }}'
WHERE 
account_id = '{{ account_id }}' --required
AND ip_access_list_id = '{{ ip_access_list_id }}' --required;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="account_ip_access_lists_replace"
    values={[
        { label: 'account_ip_access_lists_replace', value: 'account_ip_access_lists_replace' }
    ]}
>
<TabItem value="account_ip_access_lists_replace">

Replaces an IP access list, specified by its ID.

```sql
REPLACE databricks_account.settings.account_ip_access_lists
SET 
label = '{{ label }}',
list_type = '{{ list_type }}',
enabled = {{ enabled }},
ip_addresses = '{{ ip_addresses }}'
WHERE 
account_id = '{{ account_id }}' --required
AND ip_access_list_id = '{{ ip_access_list_id }}' --required
AND label = '{{ label }}' --required
AND list_type = '{{ list_type }}' --required
AND enabled = {{ enabled }} --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="account_ip_access_lists_delete"
    values={[
        { label: 'account_ip_access_lists_delete', value: 'account_ip_access_lists_delete' }
    ]}
>
<TabItem value="account_ip_access_lists_delete">

Deletes an IP access list, specified by its list ID.

```sql
DELETE FROM databricks_account.settings.account_ip_access_lists
WHERE account_id = '{{ account_id }}' --required
AND ip_access_list_id = '{{ ip_access_list_id }}' --required
;
```
</TabItem>
</Tabs>

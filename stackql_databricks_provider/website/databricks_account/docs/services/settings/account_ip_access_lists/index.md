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
<tr><td><b>Name</b></td><td><code>account_ip_access_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.account_ip_access_lists" /></td></tr>
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
    "name": "ip_access_list",
    "type": "object",
    "description": "Definition of an IP Access list",
    "children": [
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
        "name": "list_id",
        "type": "string",
        "description": "Universally unique identifier (UUID) of the IP access list."
      },
      {
        "name": "list_type",
        "type": "string",
        "description": "Type of IP access list. Valid values are as follows and are case-sensitive:<br /><br />* `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or<br />range. IP addresses in the block list are excluded even if they are included in an allow list."
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
    ]
  }
]} />
</TabItem>
<TabItem value="list">

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
    "description": "Type of IP access list. Valid values are as follows and are case-sensitive:<br /><br />* `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or<br />range. IP addresses in the block list are excluded even if they are included in an allow list."
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ip_access_list_id"><code>ip_access_list_id</code></a></td>
    <td></td>
    <td>Gets an IP access list, specified by its list ID.<br /><br />:param ip_access_list_id: str<br />  The ID for the corresponding IP access list<br /><br />:returns: :class:`GetIpAccessListResponse`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Gets all IP access lists for the specified account.<br /><br /><br />:returns: Iterator over :class:`IpAccessListInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-data__label"><code>data__label</code></a>, <a href="#parameter-data__list_type"><code>data__list_type</code></a></td>
    <td></td>
    <td>Creates an IP access list for the account.<br /><br />A list can be an allow list or a block list. See the top of this file for a description of how the<br />server treats allow lists and block lists at runtime.<br /><br />When creating or updating an IP access list:<br /><br />* For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,<br />where one CIDR counts as a single value. Attempts to exceed that number return error 400 with<br />`error_code` value `QUOTA_EXCEEDED`. * If the new list would block the calling user's current IP,<br />error 400 is returned with `error_code` value `INVALID_STATE`.<br /><br />It can take a few minutes for the changes to take effect.<br /><br />:param label: str<br />  Label for the IP access list. This **cannot** be empty.<br />:param list_type: :class:`ListType`<br />:param ip_addresses: List[str] (optional)<br /><br />:returns: :class:`CreateIpAccessListResponse`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ip_access_list_id"><code>ip_access_list_id</code></a></td>
    <td></td>
    <td>Updates an existing IP access list, specified by its ID.<br /><br />A list can include allow lists and block lists. See the top of this file for a description of how the<br />server treats allow lists and block lists at run time.<br /><br />When updating an IP access list:<br /><br />* For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,<br />where one CIDR counts as a single value. Attempts to exceed that number return error 400 with<br />`error_code` value `QUOTA_EXCEEDED`. * If the updated list would block the calling user's current IP,<br />error 400 is returned with `error_code` value `INVALID_STATE`.<br /><br />It can take a few minutes for the changes to take effect.<br /><br />:param ip_access_list_id: str<br />  The ID for the corresponding IP access list<br />:param enabled: bool (optional)<br />  Specifies whether this IP access list is enabled.<br />:param ip_addresses: List[str] (optional)<br />:param label: str (optional)<br />  Label for the IP access list. This **cannot** be empty.<br />:param list_type: :class:`ListType` (optional)</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ip_access_list_id"><code>ip_access_list_id</code></a>, <a href="#parameter-data__label"><code>data__label</code></a>, <a href="#parameter-data__list_type"><code>data__list_type</code></a>, <a href="#parameter-data__enabled"><code>data__enabled</code></a></td>
    <td></td>
    <td>Replaces an IP access list, specified by its ID.<br /><br />A list can include allow lists and block lists. See the top of this file for a description of how the<br />server treats allow lists and block lists at run time. When replacing an IP access list: * For all<br />allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values, where one<br />CIDR counts as a single value. Attempts to exceed that number return error 400 with `error_code` value<br />`QUOTA_EXCEEDED`. * If the resulting list would block the calling user's current IP, error 400 is<br />returned with `error_code` value `INVALID_STATE`. It can take a few minutes for the changes to take<br />effect.<br /><br />:param ip_access_list_id: str<br />  The ID for the corresponding IP access list<br />:param label: str<br />  Label for the IP access list. This **cannot** be empty.<br />:param list_type: :class:`ListType`<br />:param enabled: bool<br />  Specifies whether this IP access list is enabled.<br />:param ip_addresses: List[str] (optional)</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ip_access_list_id"><code>ip_access_list_id</code></a></td>
    <td></td>
    <td>Deletes an IP access list, specified by its list ID.<br /><br />:param ip_access_list_id: str<br />  The ID for the corresponding IP access list</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets an IP access list, specified by its list ID.<br /><br />:param ip_access_list_id: str<br />  The ID for the corresponding IP access list<br /><br />:returns: :class:`GetIpAccessListResponse`

```sql
SELECT
ip_access_list
FROM databricks_account.settings.account_ip_access_lists
WHERE account_id = '{{ account_id }}' -- required
AND ip_access_list_id = '{{ ip_access_list_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all IP access lists for the specified account.<br /><br /><br />:returns: Iterator over :class:`IpAccessListInfo`

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
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates an IP access list for the account.<br /><br />A list can be an allow list or a block list. See the top of this file for a description of how the<br />server treats allow lists and block lists at runtime.<br /><br />When creating or updating an IP access list:<br /><br />* For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,<br />where one CIDR counts as a single value. Attempts to exceed that number return error 400 with<br />`error_code` value `QUOTA_EXCEEDED`. * If the new list would block the calling user's current IP,<br />error 400 is returned with `error_code` value `INVALID_STATE`.<br /><br />It can take a few minutes for the changes to take effect.<br /><br />:param label: str<br />  Label for the IP access list. This **cannot** be empty.<br />:param list_type: :class:`ListType`<br />:param ip_addresses: List[str] (optional)<br /><br />:returns: :class:`CreateIpAccessListResponse`

```sql
INSERT INTO databricks_account.settings.account_ip_access_lists (
data__label,
data__list_type,
data__ip_addresses,
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
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates an existing IP access list, specified by its ID.<br /><br />A list can include allow lists and block lists. See the top of this file for a description of how the<br />server treats allow lists and block lists at run time.<br /><br />When updating an IP access list:<br /><br />* For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,<br />where one CIDR counts as a single value. Attempts to exceed that number return error 400 with<br />`error_code` value `QUOTA_EXCEEDED`. * If the updated list would block the calling user's current IP,<br />error 400 is returned with `error_code` value `INVALID_STATE`.<br /><br />It can take a few minutes for the changes to take effect.<br /><br />:param ip_access_list_id: str<br />  The ID for the corresponding IP access list<br />:param enabled: bool (optional)<br />  Specifies whether this IP access list is enabled.<br />:param ip_addresses: List[str] (optional)<br />:param label: str (optional)<br />  Label for the IP access list. This **cannot** be empty.<br />:param list_type: :class:`ListType` (optional)

```sql
UPDATE databricks_account.settings.account_ip_access_lists
SET 
data__enabled = '{{ enabled }}',
data__ip_addresses = '{{ ip_addresses }}',
data__label = '{{ label }}',
data__list_type = '{{ list_type }}'
WHERE 
account_id = '{{ account_id }}' --required
AND ip_access_list_id = '{{ ip_access_list_id }}' --required;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="replace"
    values={[
        { label: 'replace', value: 'replace' }
    ]}
>
<TabItem value="replace">

Replaces an IP access list, specified by its ID.<br /><br />A list can include allow lists and block lists. See the top of this file for a description of how the<br />server treats allow lists and block lists at run time. When replacing an IP access list: * For all<br />allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values, where one<br />CIDR counts as a single value. Attempts to exceed that number return error 400 with `error_code` value<br />`QUOTA_EXCEEDED`. * If the resulting list would block the calling user's current IP, error 400 is<br />returned with `error_code` value `INVALID_STATE`. It can take a few minutes for the changes to take<br />effect.<br /><br />:param ip_access_list_id: str<br />  The ID for the corresponding IP access list<br />:param label: str<br />  Label for the IP access list. This **cannot** be empty.<br />:param list_type: :class:`ListType`<br />:param enabled: bool<br />  Specifies whether this IP access list is enabled.<br />:param ip_addresses: List[str] (optional)

```sql
REPLACE databricks_account.settings.account_ip_access_lists
SET 
data__label = '{{ label }}',
data__list_type = '{{ list_type }}',
data__enabled = {{ enabled }},
data__ip_addresses = '{{ ip_addresses }}'
WHERE 
account_id = '{{ account_id }}' --required
AND ip_access_list_id = '{{ ip_access_list_id }}' --required
AND data__label = '{{ label }}' --required
AND data__list_type = '{{ list_type }}' --required
AND data__enabled = {{ enabled }} --required;
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

Deletes an IP access list, specified by its list ID.<br /><br />:param ip_access_list_id: str<br />  The ID for the corresponding IP access list

```sql
DELETE FROM databricks_account.settings.account_ip_access_lists
WHERE account_id = '{{ account_id }}' --required
AND ip_access_list_id = '{{ ip_access_list_id }}' --required
;
```
</TabItem>
</Tabs>

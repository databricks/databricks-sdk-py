---
title: account_service_principals_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - account_service_principals_v2
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

Creates, updates, deletes, gets or lists an <code>account_service_principals_v2</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_service_principals_v2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.account_service_principals_v2" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": "Databricks service principal ID."
  },
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "application_id",
    "type": "string",
    "description": "UUID relating to the service principal"
  },
  {
    "name": "external_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "String that represents a concatenation of given and family names."
  },
  {
    "name": "active",
    "type": "boolean",
    "description": "If this user is active"
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
        "name": "ref",
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
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Databricks service principal ID."
  },
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "application_id",
    "type": "string",
    "description": "UUID relating to the service principal"
  },
  {
    "name": "external_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "String that represents a concatenation of given and family names."
  },
  {
    "name": "active",
    "type": "boolean",
    "description": "If this user is active"
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
        "name": "ref",
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Gets the details for a single service principal define in the Databricks account.<br /><br />:param id: str<br />  Unique ID for a service principal in the Databricks account.<br /><br />:returns: :class:`AccountServicePrincipal`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-attributes"><code>attributes</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-excluded_attributes"><code>excluded_attributes</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-sort_by"><code>sort_by</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a>, <a href="#parameter-start_index"><code>start_index</code></a></td>
    <td>Gets the set of service principals associated with a Databricks account.<br /><br />:param attributes: str (optional)<br />  Comma-separated list of attributes to return in response.<br />:param count: int (optional)<br />  Desired number of results per page. Default is 10000.<br />:param excluded_attributes: str (optional)<br />  Comma-separated list of attributes to exclude in response.<br />:param filter: str (optional)<br />  Query by which the results have to be filtered. Supported operators are equals(`eq`),<br />  contains(`co`), starts with(`sw`) and not equals(`ne`). Additionally, simple expressions can be<br />  formed using logical operators - `and` and `or`. The [SCIM RFC] has more details but we currently<br />  only support simple expressions.<br /><br />  [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2<br />:param sort_by: str (optional)<br />  Attribute to sort the results.<br />:param sort_order: :class:`ListSortOrder` (optional)<br />  The order to sort the results.<br />:param start_index: int (optional)<br />  Specifies the index of the first result. First item is number 1.<br /><br />:returns: Iterator over :class:`AccountServicePrincipal`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a new service principal in the Databricks account.<br /><br />:param active: bool (optional)<br />  If this user is active<br />:param application_id: str (optional)<br />  UUID relating to the service principal<br />:param display_name: str (optional)<br />  String that represents a concatenation of given and family names.<br />:param external_id: str (optional)<br />:param id: str (optional)<br />  Databricks service principal ID.<br />:param roles: List[:class:`ComplexValue`] (optional)<br />  Indicates if the group has the admin role.<br /><br />:returns: :class:`AccountServicePrincipal`</td>
</tr>
<tr>
    <td><a href="#patch"><CopyableCode code="patch" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Partially updates the details of a single service principal in the Databricks account.<br /><br />:param id: str<br />  Unique ID in the Databricks workspace.<br />:param operations: List[:class:`Patch`] (optional)<br />:param schemas: List[:class:`PatchSchema`] (optional)<br />  The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Updates the details of a single service principal.<br /><br />This action replaces the existing service principal with the same name.<br /><br />:param id: str<br />  Databricks service principal ID.<br />:param active: bool (optional)<br />  If this user is active<br />:param application_id: str (optional)<br />  UUID relating to the service principal<br />:param display_name: str (optional)<br />  String that represents a concatenation of given and family names.<br />:param external_id: str (optional)<br />:param roles: List[:class:`ComplexValue`] (optional)<br />  Indicates if the group has the admin role.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Delete a single service principal in the Databricks account.<br /><br />:param id: str<br />  Unique ID for a service principal in the Databricks account.</td>
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
    <td>Unique ID for a service principal in the Databricks account.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the details for a single service principal define in the Databricks account.<br /><br />:param id: str<br />  Unique ID for a service principal in the Databricks account.<br /><br />:returns: :class:`AccountServicePrincipal`

```sql
SELECT
id,
account_id,
application_id,
external_id,
display_name,
active,
roles
FROM databricks_account.iam.account_service_principals_v2
WHERE account_id = '{{ account_id }}' -- required
AND id = '{{ id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the set of service principals associated with a Databricks account.<br /><br />:param attributes: str (optional)<br />  Comma-separated list of attributes to return in response.<br />:param count: int (optional)<br />  Desired number of results per page. Default is 10000.<br />:param excluded_attributes: str (optional)<br />  Comma-separated list of attributes to exclude in response.<br />:param filter: str (optional)<br />  Query by which the results have to be filtered. Supported operators are equals(`eq`),<br />  contains(`co`), starts with(`sw`) and not equals(`ne`). Additionally, simple expressions can be<br />  formed using logical operators - `and` and `or`. The [SCIM RFC] has more details but we currently<br />  only support simple expressions.<br /><br />  [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2<br />:param sort_by: str (optional)<br />  Attribute to sort the results.<br />:param sort_order: :class:`ListSortOrder` (optional)<br />  The order to sort the results.<br />:param start_index: int (optional)<br />  Specifies the index of the first result. First item is number 1.<br /><br />:returns: Iterator over :class:`AccountServicePrincipal`

```sql
SELECT
id,
account_id,
application_id,
external_id,
display_name,
active,
roles
FROM databricks_account.iam.account_service_principals_v2
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
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a new service principal in the Databricks account.<br /><br />:param active: bool (optional)<br />  If this user is active<br />:param application_id: str (optional)<br />  UUID relating to the service principal<br />:param display_name: str (optional)<br />  String that represents a concatenation of given and family names.<br />:param external_id: str (optional)<br />:param id: str (optional)<br />  Databricks service principal ID.<br />:param roles: List[:class:`ComplexValue`] (optional)<br />  Indicates if the group has the admin role.<br /><br />:returns: :class:`AccountServicePrincipal`

```sql
INSERT INTO databricks_account.iam.account_service_principals_v2 (
data__active,
data__application_id,
data__display_name,
data__external_id,
data__id,
data__roles,
account_id
)
SELECT 
'{{ active }}',
'{{ application_id }}',
'{{ display_name }}',
'{{ external_id }}',
'{{ id }}',
'{{ roles }}',
'{{ account_id }}'
RETURNING
id,
account_id,
application_id,
external_id,
display_name,
active,
roles
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: account_service_principals_v2
  props:
    - name: account_id
      value: string
      description: Required parameter for the account_service_principals_v2 resource.
    - name: active
      value: string
      description: |
        If this user is active
    - name: application_id
      value: string
      description: |
        UUID relating to the service principal
    - name: display_name
      value: string
      description: |
        String that represents a concatenation of given and family names.
    - name: external_id
      value: string
      description: |
        :param id: str (optional) Databricks service principal ID.
    - name: id
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
    defaultValue="patch"
    values={[
        { label: 'patch', value: 'patch' }
    ]}
>
<TabItem value="patch">

Partially updates the details of a single service principal in the Databricks account.<br /><br />:param id: str<br />  Unique ID in the Databricks workspace.<br />:param operations: List[:class:`Patch`] (optional)<br />:param schemas: List[:class:`PatchSchema`] (optional)<br />  The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].

```sql
UPDATE databricks_account.iam.account_service_principals_v2
SET 
data__operations = '{{ operations }}',
data__schemas = '{{ schemas }}'
WHERE 
account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required;
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

Updates the details of a single service principal.<br /><br />This action replaces the existing service principal with the same name.<br /><br />:param id: str<br />  Databricks service principal ID.<br />:param active: bool (optional)<br />  If this user is active<br />:param application_id: str (optional)<br />  UUID relating to the service principal<br />:param display_name: str (optional)<br />  String that represents a concatenation of given and family names.<br />:param external_id: str (optional)<br />:param roles: List[:class:`ComplexValue`] (optional)<br />  Indicates if the group has the admin role.

```sql
REPLACE databricks_account.iam.account_service_principals_v2
SET 
data__active = '{{ active }}',
data__application_id = '{{ application_id }}',
data__display_name = '{{ display_name }}',
data__external_id = '{{ external_id }}',
data__roles = '{{ roles }}'
WHERE 
account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required;
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

Delete a single service principal in the Databricks account.<br /><br />:param id: str<br />  Unique ID for a service principal in the Databricks account.

```sql
DELETE FROM databricks_account.iam.account_service_principals_v2
WHERE account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required
;
```
</TabItem>
</Tabs>

---
title: service_principals_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - service_principals_v2
  - iam
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

Creates, updates, deletes, gets or lists a <code>service_principals_v2</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_principals_v2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.service_principals_v2" /></td></tr>
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
    "description": ""
  },
  {
    "name": "entitlements",
    "type": "array",
    "description": "Entitlements assigned to the service principal. See [assigning entitlements] for a full list of supported values. [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements",
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
  },
  {
    "name": "groups",
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
  },
  {
    "name": "roles",
    "type": "array",
    "description": "Corresponds to AWS instance profile/arn role.",
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
  },
  {
    "name": "schemas",
    "type": "array",
    "description": "The schema of the List response."
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
    "description": ""
  },
  {
    "name": "entitlements",
    "type": "array",
    "description": "Entitlements assigned to the service principal. See [assigning entitlements] for a full list of supported values. [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements",
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
  },
  {
    "name": "groups",
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
  },
  {
    "name": "roles",
    "type": "array",
    "description": "Corresponds to AWS instance profile/arn role.",
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
  },
  {
    "name": "schemas",
    "type": "array",
    "description": "The schema of the List response."
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the details for a single service principal define in the Databricks workspace.<br /><br />:param id: str<br />  Unique ID for a service principal in the Databricks workspace.<br /><br />:returns: :class:`ServicePrincipal`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-attributes"><code>attributes</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-excluded_attributes"><code>excluded_attributes</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-sort_by"><code>sort_by</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a>, <a href="#parameter-start_index"><code>start_index</code></a></td>
    <td>Gets the set of service principals associated with a Databricks workspace.<br /><br />:param attributes: str (optional)<br />  Comma-separated list of attributes to return in response.<br />:param count: int (optional)<br />  Desired number of results per page.<br />:param excluded_attributes: str (optional)<br />  Comma-separated list of attributes to exclude in response.<br />:param filter: str (optional)<br />  Query by which the results have to be filtered. Supported operators are equals(`eq`),<br />  contains(`co`), starts with(`sw`) and not equals(`ne`). Additionally, simple expressions can be<br />  formed using logical operators - `and` and `or`. The [SCIM RFC] has more details but we currently<br />  only support simple expressions.<br /><br />  [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2<br />:param sort_by: str (optional)<br />  Attribute to sort the results.<br />:param sort_order: :class:`ListSortOrder` (optional)<br />  The order to sort the results.<br />:param start_index: int (optional)<br />  Specifies the index of the first result. First item is number 1.<br /><br />:returns: Iterator over :class:`ServicePrincipal`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new service principal in the Databricks workspace.<br /><br />:param active: bool (optional)<br />  If this user is active<br />:param application_id: str (optional)<br />  UUID relating to the service principal<br />:param display_name: str (optional)<br />  String that represents a concatenation of given and family names.<br />:param entitlements: List[:class:`ComplexValue`] (optional)<br />  Entitlements assigned to the service principal. See [assigning entitlements] for a full list of<br />  supported values.<br /><br />  [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements<br />:param external_id: str (optional)<br />:param groups: List[:class:`ComplexValue`] (optional)<br />:param id: str (optional)<br />  Databricks service principal ID.<br />:param roles: List[:class:`ComplexValue`] (optional)<br />  Corresponds to AWS instance profile/arn role.<br />:param schemas: List[:class:`ServicePrincipalSchema`] (optional)<br />  The schema of the List response.<br /><br />:returns: :class:`ServicePrincipal`</td>
</tr>
<tr>
    <td><a href="#patch"><CopyableCode code="patch" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Partially updates the details of a single service principal in the Databricks workspace.<br /><br />:param id: str<br />  Unique ID in the Databricks workspace.<br />:param operations: List[:class:`Patch`] (optional)<br />:param schemas: List[:class:`PatchSchema`] (optional)<br />  The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the details of a single service principal.<br /><br />This action replaces the existing service principal with the same name.<br /><br />:param id: str<br />  Databricks service principal ID.<br />:param active: bool (optional)<br />  If this user is active<br />:param application_id: str (optional)<br />  UUID relating to the service principal<br />:param display_name: str (optional)<br />  String that represents a concatenation of given and family names.<br />:param entitlements: List[:class:`ComplexValue`] (optional)<br />  Entitlements assigned to the service principal. See [assigning entitlements] for a full list of<br />  supported values.<br /><br />  [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements<br />:param external_id: str (optional)<br />:param groups: List[:class:`ComplexValue`] (optional)<br />:param roles: List[:class:`ComplexValue`] (optional)<br />  Corresponds to AWS instance profile/arn role.<br />:param schemas: List[:class:`ServicePrincipalSchema`] (optional)<br />  The schema of the List response.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a single service principal in the Databricks workspace.<br /><br />:param id: str<br />  Unique ID for a service principal in the Databricks workspace.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Unique ID for a service principal in the Databricks workspace.</td>
</tr>
<tr id="parameter-attributes">
    <td><CopyableCode code="attributes" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of attributes to return in response.</td>
</tr>
<tr id="parameter-count">
    <td><CopyableCode code="count" /></td>
    <td><code>string</code></td>
    <td>Desired number of results per page.</td>
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

Gets the details for a single service principal define in the Databricks workspace.<br /><br />:param id: str<br />  Unique ID for a service principal in the Databricks workspace.<br /><br />:returns: :class:`ServicePrincipal`

```sql
SELECT
id,
application_id,
external_id,
display_name,
active,
entitlements,
groups,
roles,
schemas
FROM databricks_workspace.iam.service_principals_v2
WHERE id = '{{ id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the set of service principals associated with a Databricks workspace.<br /><br />:param attributes: str (optional)<br />  Comma-separated list of attributes to return in response.<br />:param count: int (optional)<br />  Desired number of results per page.<br />:param excluded_attributes: str (optional)<br />  Comma-separated list of attributes to exclude in response.<br />:param filter: str (optional)<br />  Query by which the results have to be filtered. Supported operators are equals(`eq`),<br />  contains(`co`), starts with(`sw`) and not equals(`ne`). Additionally, simple expressions can be<br />  formed using logical operators - `and` and `or`. The [SCIM RFC] has more details but we currently<br />  only support simple expressions.<br /><br />  [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2<br />:param sort_by: str (optional)<br />  Attribute to sort the results.<br />:param sort_order: :class:`ListSortOrder` (optional)<br />  The order to sort the results.<br />:param start_index: int (optional)<br />  Specifies the index of the first result. First item is number 1.<br /><br />:returns: Iterator over :class:`ServicePrincipal`

```sql
SELECT
id,
application_id,
external_id,
display_name,
active,
entitlements,
groups,
roles,
schemas
FROM databricks_workspace.iam.service_principals_v2
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Creates a new service principal in the Databricks workspace.<br /><br />:param active: bool (optional)<br />  If this user is active<br />:param application_id: str (optional)<br />  UUID relating to the service principal<br />:param display_name: str (optional)<br />  String that represents a concatenation of given and family names.<br />:param entitlements: List[:class:`ComplexValue`] (optional)<br />  Entitlements assigned to the service principal. See [assigning entitlements] for a full list of<br />  supported values.<br /><br />  [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements<br />:param external_id: str (optional)<br />:param groups: List[:class:`ComplexValue`] (optional)<br />:param id: str (optional)<br />  Databricks service principal ID.<br />:param roles: List[:class:`ComplexValue`] (optional)<br />  Corresponds to AWS instance profile/arn role.<br />:param schemas: List[:class:`ServicePrincipalSchema`] (optional)<br />  The schema of the List response.<br /><br />:returns: :class:`ServicePrincipal`

```sql
INSERT INTO databricks_workspace.iam.service_principals_v2 (
data__active,
data__application_id,
data__display_name,
data__entitlements,
data__external_id,
data__groups,
data__id,
data__roles,
data__schemas,
deployment_name
)
SELECT 
'{{ active }}',
'{{ application_id }}',
'{{ display_name }}',
'{{ entitlements }}',
'{{ external_id }}',
'{{ groups }}',
'{{ id }}',
'{{ roles }}',
'{{ schemas }}',
'{{ deployment_name }}'
RETURNING
id,
application_id,
external_id,
display_name,
active,
entitlements,
groups,
roles,
schemas
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: service_principals_v2
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the service_principals_v2 resource.
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
    - name: entitlements
      value: string
      description: |
        Entitlements assigned to the service principal. See [assigning entitlements] for a full list of supported values. [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
    - name: external_id
      value: string
      description: |
        :param groups: List[:class:`ComplexValue`] (optional)
    - name: groups
      value: string
    - name: id
      value: string
      description: |
        Databricks service principal ID.
    - name: roles
      value: string
      description: |
        Corresponds to AWS instance profile/arn role.
    - name: schemas
      value: string
      description: |
        The schema of the List response.
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

Partially updates the details of a single service principal in the Databricks workspace.<br /><br />:param id: str<br />  Unique ID in the Databricks workspace.<br />:param operations: List[:class:`Patch`] (optional)<br />:param schemas: List[:class:`PatchSchema`] (optional)<br />  The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].

```sql
UPDATE databricks_workspace.iam.service_principals_v2
SET 
data__operations = '{{ operations }}',
data__schemas = '{{ schemas }}'
WHERE 
id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required;
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

Updates the details of a single service principal.<br /><br />This action replaces the existing service principal with the same name.<br /><br />:param id: str<br />  Databricks service principal ID.<br />:param active: bool (optional)<br />  If this user is active<br />:param application_id: str (optional)<br />  UUID relating to the service principal<br />:param display_name: str (optional)<br />  String that represents a concatenation of given and family names.<br />:param entitlements: List[:class:`ComplexValue`] (optional)<br />  Entitlements assigned to the service principal. See [assigning entitlements] for a full list of<br />  supported values.<br /><br />  [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements<br />:param external_id: str (optional)<br />:param groups: List[:class:`ComplexValue`] (optional)<br />:param roles: List[:class:`ComplexValue`] (optional)<br />  Corresponds to AWS instance profile/arn role.<br />:param schemas: List[:class:`ServicePrincipalSchema`] (optional)<br />  The schema of the List response.

```sql
REPLACE databricks_workspace.iam.service_principals_v2
SET 
data__active = '{{ active }}',
data__application_id = '{{ application_id }}',
data__display_name = '{{ display_name }}',
data__entitlements = '{{ entitlements }}',
data__external_id = '{{ external_id }}',
data__groups = '{{ groups }}',
data__roles = '{{ roles }}',
data__schemas = '{{ schemas }}'
WHERE 
id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required;
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

Delete a single service principal in the Databricks workspace.<br /><br />:param id: str<br />  Unique ID for a service principal in the Databricks workspace.

```sql
DELETE FROM databricks_workspace.iam.service_principals_v2
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

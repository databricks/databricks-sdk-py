---
title: users_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - users_v2
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

Creates, updates, deletes, gets or lists a <code>users_v2</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="users_v2" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.users_v2" /></td></tr>
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
    "description": "Databricks user ID."
  },
  {
    "name": "name",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "familyName",
        "type": "string",
        "description": ""
      },
      {
        "name": "givenName",
        "type": "string",
        "description": "Given name of the Databricks user."
      }
    ]
  },
  {
    "name": "active",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "displayName",
    "type": "string",
    "description": "String that represents a concatenation of given and family names. For example `John Smith`. This field cannot be updated through the Workspace SCIM APIs when [identity federation is enabled]. Use Account SCIM APIs to update `displayName`. [identity federation is enabled]: https://docs.databricks.com/administration-guide/users-groups/best-practices.html#enable-identity-federation"
  },
  {
    "name": "emails",
    "type": "array",
    "description": "All the emails associated with the Databricks user.",
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
    "name": "entitlements",
    "type": "array",
    "description": "Entitlements assigned to the user. See [assigning entitlements] for a full list of supported values. [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements",
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
    "name": "externalId",
    "type": "string",
    "description": "External ID is not currently supported. It is reserved for future use."
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
    "name": "schemas",
    "type": "array",
    "description": "The schema of the user."
  },
  {
    "name": "userName",
    "type": "string",
    "description": "Email address of the Databricks user."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Databricks user ID."
  },
  {
    "name": "name",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "familyName",
        "type": "string",
        "description": ""
      },
      {
        "name": "givenName",
        "type": "string",
        "description": "Given name of the Databricks user."
      }
    ]
  },
  {
    "name": "active",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "displayName",
    "type": "string",
    "description": "String that represents a concatenation of given and family names. For example `John Smith`. This field cannot be updated through the Workspace SCIM APIs when [identity federation is enabled]. Use Account SCIM APIs to update `displayName`. [identity federation is enabled]: https://docs.databricks.com/administration-guide/users-groups/best-practices.html#enable-identity-federation"
  },
  {
    "name": "emails",
    "type": "array",
    "description": "All the emails associated with the Databricks user.",
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
    "name": "entitlements",
    "type": "array",
    "description": "Entitlements assigned to the user. See [assigning entitlements] for a full list of supported values. [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements",
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
    "name": "externalId",
    "type": "string",
    "description": "External ID is not currently supported. It is reserved for future use."
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
    "name": "schemas",
    "type": "array",
    "description": "The schema of the user."
  },
  {
    "name": "userName",
    "type": "string",
    "description": "Email address of the Databricks user."
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-attributes"><code>attributes</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-excluded_attributes"><code>excluded_attributes</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-sort_by"><code>sort_by</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a>, <a href="#parameter-start_index"><code>start_index</code></a></td>
    <td>Gets information for a specific user in Databricks workspace.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-attributes"><code>attributes</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-excluded_attributes"><code>excluded_attributes</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-sort_by"><code>sort_by</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a>, <a href="#parameter-start_index"><code>start_index</code></a></td>
    <td>Gets details for all the users associated with a Databricks workspace.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Creates a new user in the Databricks workspace. This new user will also be added to the Databricks</td>
</tr>
<tr>
    <td><a href="#patch"><CopyableCode code="patch" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Partially updates a user resource by applying the supplied operations on specific user attributes.</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Replaces a user's information with the data supplied in request.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Deletes a user. Deleting a user from a Databricks workspace also removes objects associated with the</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Unique ID for a user in the Databricks workspace.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-attributes">
    <td><CopyableCode code="attributes" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of attributes to return in response.</td>
</tr>
<tr id="parameter-count">
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
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
    <td>Attribute to sort the results. Multi-part paths are supported. For example, `userName`, `name.givenName`, and `emails`.</td>
</tr>
<tr id="parameter-sort_order">
    <td><CopyableCode code="sort_order" /></td>
    <td><code>string</code></td>
    <td>The order to sort the results.</td>
</tr>
<tr id="parameter-start_index">
    <td><CopyableCode code="start_index" /></td>
    <td><code>integer</code></td>
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

Gets information for a specific user in Databricks workspace.

```sql
SELECT
id,
name,
active,
displayName,
emails,
entitlements,
externalId,
groups,
roles,
schemas,
userName
FROM databricks_workspace.iam.users_v2
WHERE id = '{{ id }}' -- required
AND workspace = '{{ workspace }}' -- required
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
<TabItem value="list">

Gets details for all the users associated with a Databricks workspace.

```sql
SELECT
id,
name,
active,
displayName,
emails,
entitlements,
externalId,
groups,
roles,
schemas,
userName
FROM databricks_workspace.iam.users_v2
WHERE workspace = '{{ workspace }}' -- required
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

Creates a new user in the Databricks workspace. This new user will also be added to the Databricks

```sql
INSERT INTO databricks_workspace.iam.users_v2 (
active,
display_name,
emails,
entitlements,
external_id,
groups,
id,
name,
roles,
schemas,
user_name,
workspace
)
SELECT 
{{ active }},
'{{ display_name }}',
'{{ emails }}',
'{{ entitlements }}',
'{{ external_id }}',
'{{ groups }}',
'{{ id }}',
'{{ name }}',
'{{ roles }}',
'{{ schemas }}',
'{{ user_name }}',
'{{ workspace }}'
RETURNING
id,
name,
active,
displayName,
emails,
entitlements,
externalId,
groups,
roles,
schemas,
userName
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: users_v2
  props:
    - name: workspace
      value: string
      description: Required parameter for the users_v2 resource.
    - name: active
      value: boolean
      description: |
        If this user is active
    - name: display_name
      value: string
      description: |
        String that represents a concatenation of given and family names. For example `John Smith`. This field cannot be updated through the Workspace SCIM APIs when [identity federation is enabled]. Use Account SCIM APIs to update `displayName`. [identity federation is enabled]: https://docs.databricks.com/administration-guide/users-groups/best-practices.html#enable-identity-federation
    - name: emails
      value: array
      description: |
        All the emails associated with the Databricks user.
      props:
      - name: display
        value: string
      - name: primary
        value: boolean
      - name: $ref
        value: string
      - name: type
        value: string
      - name: value
        value: string
    - name: entitlements
      value: array
      description: |
        Entitlements assigned to the user. See [assigning entitlements] for a full list of supported values. [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
      props:
      - name: display
        value: string
      - name: primary
        value: boolean
      - name: $ref
        value: string
      - name: type
        value: string
      - name: value
        value: string
    - name: external_id
      value: string
      description: |
        External ID is not currently supported. It is reserved for future use.
    - name: groups
      value: array
      description: |
        :param id: str (optional) Databricks user ID.
      props:
      - name: display
        value: string
      - name: primary
        value: boolean
      - name: $ref
        value: string
      - name: type
        value: string
      - name: value
        value: string
    - name: id
      value: string
    - name: name
      value: object
      description: |
        :param roles: List[:class:`ComplexValue`] (optional) Corresponds to AWS instance profile/arn role.
      props:
      - name: familyName
        value: string
      - name: givenName
        value: string
        description: |
          Given name of the Databricks user.
    - name: roles
      value: array
      props:
      - name: display
        value: string
      - name: primary
        value: boolean
      - name: $ref
        value: string
      - name: type
        value: string
      - name: value
        value: string
    - name: schemas
      value: array
      description: |
        The schema of the user.
      items:
        type: string
    - name: user_name
      value: string
      description: |
        Email address of the Databricks user.
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

Partially updates a user resource by applying the supplied operations on specific user attributes.

```sql
UPDATE databricks_workspace.iam.users_v2
SET 
operations = '{{ operations }}',
schemas = '{{ schemas }}'
WHERE 
id = '{{ id }}' --required
AND workspace = '{{ workspace }}' --required;
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

Replaces a user's information with the data supplied in request.

```sql
REPLACE databricks_workspace.iam.users_v2
SET 
active = {{ active }},
display_name = '{{ display_name }}',
emails = '{{ emails }}',
entitlements = '{{ entitlements }}',
external_id = '{{ external_id }}',
groups = '{{ groups }}',
name = '{{ name }}',
roles = '{{ roles }}',
schemas = '{{ schemas }}',
user_name = '{{ user_name }}'
WHERE 
id = '{{ id }}' --required
AND workspace = '{{ workspace }}' --required;
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

Deletes a user. Deleting a user from a Databricks workspace also removes objects associated with the

```sql
DELETE FROM databricks_workspace.iam.users_v2
WHERE id = '{{ id }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

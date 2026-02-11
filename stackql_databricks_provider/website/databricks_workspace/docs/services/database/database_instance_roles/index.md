---
title: database_instance_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - database_instance_roles
  - database
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

Creates, updates, deletes, gets or lists a <code>database_instance_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_instance_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.database.database_instance_roles" /></td></tr>
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
    "description": "The name of the role. This is the unique identifier for the role in an instance."
  },
  {
    "name": "instance_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "attributes",
    "type": "object",
    "description": "The desired API-exposed Postgres role attribute to associate with the role. Optional.",
    "children": [
      {
        "name": "bypassrls",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "createdb",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "createrole",
        "type": "boolean",
        "description": ""
      }
    ]
  },
  {
    "name": "effective_attributes",
    "type": "object",
    "description": "The attributes that are applied to the role. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.",
    "children": [
      {
        "name": "bypassrls",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "createdb",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "createrole",
        "type": "boolean",
        "description": ""
      }
    ]
  },
  {
    "name": "identity_type",
    "type": "string",
    "description": "The type of the role."
  },
  {
    "name": "membership_role",
    "type": "string",
    "description": "An enum value for a standard role that this role is a member of."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the role. This is the unique identifier for the role in an instance."
  },
  {
    "name": "instance_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "attributes",
    "type": "object",
    "description": "The desired API-exposed Postgres role attribute to associate with the role. Optional.",
    "children": [
      {
        "name": "bypassrls",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "createdb",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "createrole",
        "type": "boolean",
        "description": ""
      }
    ]
  },
  {
    "name": "effective_attributes",
    "type": "object",
    "description": "The attributes that are applied to the role. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.",
    "children": [
      {
        "name": "bypassrls",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "createdb",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "createrole",
        "type": "boolean",
        "description": ""
      }
    ]
  },
  {
    "name": "identity_type",
    "type": "string",
    "description": "The type of the role."
  },
  {
    "name": "membership_role",
    "type": "string",
    "description": "An enum value for a standard role that this role is a member of."
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
    <td><a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a role for a Database Instance.<br /><br />:param instance_name: str<br />:param name: str<br /><br />:returns: :class:`DatabaseInstanceRole`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>START OF PG ROLE APIs Section These APIs are marked a PUBLIC with stage &lt; PUBLIC_PREVIEW. With more<br />recent Lakebase V2 plans, we don't plan to ever advance these to PUBLIC_PREVIEW. These APIs will<br />remain effectively undocumented/UI-only and we'll aim for a new public roles API as part of V2 PuPr.<br /><br />:param instance_name: str<br />:param page_size: int (optional)<br />  Upper bound for items returned.<br />:param page_token: str (optional)<br />  Pagination token to go to the next page of Database Instances. Requests first page if absent.<br /><br />:returns: Iterator over :class:`DatabaseInstanceRole`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__database_instance_role"><code>data__database_instance_role</code></a></td>
    <td><a href="#parameter-database_instance_name"><code>database_instance_name</code></a></td>
    <td>Create a role for a Database Instance.<br /><br />:param instance_name: str<br />:param database_instance_role: :class:`DatabaseInstanceRole`<br />:param database_instance_name: str (optional)<br /><br />:returns: :class:`DatabaseInstanceRole`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-allow_missing"><code>allow_missing</code></a>, <a href="#parameter-reassign_owned_to"><code>reassign_owned_to</code></a></td>
    <td>Deletes a role for a Database Instance.<br /><br />:param instance_name: str<br />:param name: str<br />:param allow_missing: bool (optional)<br />  This is the AIP standard name for the equivalent of Postgres' `IF EXISTS` option<br />:param reassign_owned_to: str (optional)</td>
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
<tr id="parameter-instance_name">
    <td><CopyableCode code="instance_name" /></td>
    <td><code>string</code></td>
    <td>:param name: str</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-allow_missing">
    <td><CopyableCode code="allow_missing" /></td>
    <td><code>string</code></td>
    <td>This is the AIP standard name for the equivalent of Postgres' `IF EXISTS` option</td>
</tr>
<tr id="parameter-database_instance_name">
    <td><CopyableCode code="database_instance_name" /></td>
    <td><code>string</code></td>
    <td>:returns: :class:`DatabaseInstanceRole`</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page of Database Instances. Requests first page if absent.</td>
</tr>
<tr id="parameter-reassign_owned_to">
    <td><CopyableCode code="reassign_owned_to" /></td>
    <td><code>string</code></td>
    <td>str (optional)</td>
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

Gets a role for a Database Instance.<br /><br />:param instance_name: str<br />:param name: str<br /><br />:returns: :class:`DatabaseInstanceRole`

```sql
SELECT
name,
instance_name,
attributes,
effective_attributes,
identity_type,
membership_role
FROM databricks_workspace.database.database_instance_roles
WHERE instance_name = '{{ instance_name }}' -- required
AND name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

START OF PG ROLE APIs Section These APIs are marked a PUBLIC with stage &lt; PUBLIC_PREVIEW. With more<br />recent Lakebase V2 plans, we don't plan to ever advance these to PUBLIC_PREVIEW. These APIs will<br />remain effectively undocumented/UI-only and we'll aim for a new public roles API as part of V2 PuPr.<br /><br />:param instance_name: str<br />:param page_size: int (optional)<br />  Upper bound for items returned.<br />:param page_token: str (optional)<br />  Pagination token to go to the next page of Database Instances. Requests first page if absent.<br /><br />:returns: Iterator over :class:`DatabaseInstanceRole`

```sql
SELECT
name,
instance_name,
attributes,
effective_attributes,
identity_type,
membership_role
FROM databricks_workspace.database.database_instance_roles
WHERE instance_name = '{{ instance_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
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

Create a role for a Database Instance.<br /><br />:param instance_name: str<br />:param database_instance_role: :class:`DatabaseInstanceRole`<br />:param database_instance_name: str (optional)<br /><br />:returns: :class:`DatabaseInstanceRole`

```sql
INSERT INTO databricks_workspace.database.database_instance_roles (
data__database_instance_role,
instance_name,
deployment_name,
database_instance_name
)
SELECT 
'{{ database_instance_role }}' /* required */,
'{{ instance_name }}',
'{{ deployment_name }}',
'{{ database_instance_name }}'
RETURNING
name,
instance_name,
attributes,
effective_attributes,
identity_type,
membership_role
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: database_instance_roles
  props:
    - name: instance_name
      value: string
      description: Required parameter for the database_instance_roles resource.
    - name: deployment_name
      value: string
      description: Required parameter for the database_instance_roles resource.
    - name: database_instance_role
      value: string
    - name: database_instance_name
      value: string
      description: :returns: :class:`DatabaseInstanceRole`
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

Deletes a role for a Database Instance.<br /><br />:param instance_name: str<br />:param name: str<br />:param allow_missing: bool (optional)<br />  This is the AIP standard name for the equivalent of Postgres' `IF EXISTS` option<br />:param reassign_owned_to: str (optional)

```sql
DELETE FROM databricks_workspace.database.database_instance_roles
WHERE instance_name = '{{ instance_name }}' --required
AND name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND allow_missing = '{{ allow_missing }}'
AND reassign_owned_to = '{{ reassign_owned_to }}'
;
```
</TabItem>
</Tabs>

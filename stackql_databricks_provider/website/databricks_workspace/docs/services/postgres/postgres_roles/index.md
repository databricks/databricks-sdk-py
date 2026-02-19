---
title: postgres_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_roles
  - postgres
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

Creates, updates, deletes, gets or lists a <code>postgres_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_roles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_roles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Output only. The full resource path of the role. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125;"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The Branch where this Role exists. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the role configuration, including identity type, authentication method, and role attributes.",
    "children": [
      {
        "name": "auth_method",
        "type": "string",
        "description": "How the role is authenticated when connecting to Postgres. (LAKEBASE_OAUTH_V1, NO_LOGIN, PG_PASSWORD_SCRAM_SHA_256)"
      },
      {
        "name": "identity_type",
        "type": "string",
        "description": "The type of role. When specifying a managed-identity, the chosen role_id must be a valid: * application ID for SERVICE_PRINCIPAL * user email for USER * group name for GROUP (GROUP, SERVICE_PRINCIPAL, USER)"
      },
      {
        "name": "postgres_role",
        "type": "string",
        "description": "The name of the Postgres role. This expects a valid Postgres identifier as specified in the link below. https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS Required when creating the Role. If you wish to create a Postgres Role backed by a managed Databricks identity, then postgres_role must be one of the following: 1. user email for IdentityType.USER 2. app ID for IdentityType.SERVICE_PRINCIPAL 2. group name for IdentityType.GROUP"
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Current status of the role, including its identity type, authentication method, and role attributes.",
    "children": [
      {
        "name": "auth_method",
        "type": "string",
        "description": "How the role is authenticated when connecting to Postgres. (LAKEBASE_OAUTH_V1, NO_LOGIN, PG_PASSWORD_SCRAM_SHA_256)"
      },
      {
        "name": "identity_type",
        "type": "string",
        "description": "The type of the role. (GROUP, SERVICE_PRINCIPAL, USER)"
      },
      {
        "name": "postgres_role",
        "type": "string",
        "description": "The name of the Postgres role."
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": ""
  }
]} />
</TabItem>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Output only. The full resource path of the role. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125;"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The Branch where this Role exists. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the role configuration, including identity type, authentication method, and role attributes.",
    "children": [
      {
        "name": "auth_method",
        "type": "string",
        "description": "How the role is authenticated when connecting to Postgres. (LAKEBASE_OAUTH_V1, NO_LOGIN, PG_PASSWORD_SCRAM_SHA_256)"
      },
      {
        "name": "identity_type",
        "type": "string",
        "description": "The type of role. When specifying a managed-identity, the chosen role_id must be a valid: * application ID for SERVICE_PRINCIPAL * user email for USER * group name for GROUP (GROUP, SERVICE_PRINCIPAL, USER)"
      },
      {
        "name": "postgres_role",
        "type": "string",
        "description": "The name of the Postgres role. This expects a valid Postgres identifier as specified in the link below. https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS Required when creating the Role. If you wish to create a Postgres Role backed by a managed Databricks identity, then postgres_role must be one of the following: 1. user email for IdentityType.USER 2. app ID for IdentityType.SERVICE_PRINCIPAL 2. group name for IdentityType.GROUP"
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Current status of the role, including its identity type, authentication method, and role attributes.",
    "children": [
      {
        "name": "auth_method",
        "type": "string",
        "description": "How the role is authenticated when connecting to Postgres. (LAKEBASE_OAUTH_V1, NO_LOGIN, PG_PASSWORD_SCRAM_SHA_256)"
      },
      {
        "name": "identity_type",
        "type": "string",
        "description": "The type of the role. (GROUP, SERVICE_PRINCIPAL, USER)"
      },
      {
        "name": "postgres_role",
        "type": "string",
        "description": "The name of the Postgres role."
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": ""
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
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns a paginated list of Postgres roles in the branch.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieves information about the specified Postgres role, including its authentication method and</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-role"><code>role</code></a></td>
    <td><a href="#parameter-role_id"><code>role_id</code></a></td>
    <td>Creates a new Postgres role in the branch.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-reassign_owned_to"><code>reassign_owned_to</code></a></td>
    <td>Deletes the specified Postgres role.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The full resource path of the role to delete. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125;</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>The Branch where this Role is created. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>Upper bound for items returned. Cannot be negative.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token from a previous response. If not provided, returns the first page.</td>
</tr>
<tr id="parameter-reassign_owned_to">
    <td><CopyableCode code="reassign_owned_to" /></td>
    <td><code>string</code></td>
    <td>Reassign objects. If this is set, all objects owned by the role are reassigned to the role specified in this parameter. NOTE: setting this requires spinning up a compute to succeed, since it involves running SQL queries. TODO: #LKB-7187 implement reassign_owned_to on LBM side. This might end-up being a synchronous query when this parameter is used.</td>
</tr>
<tr id="parameter-role_id">
    <td><CopyableCode code="role_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the Role, which will become the final component of the role's resource name. This ID becomes the role in Postgres. This value should be 4-63 characters, and valid characters are lowercase letters, numbers, and hyphens, as defined by RFC 1123. If role_id is not specified in the request, it is generated automatically.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="list">

Returns a paginated list of Postgres roles in the branch.

```sql
SELECT
name,
create_time,
parent,
spec,
status,
update_time
FROM databricks_workspace.postgres.postgres_roles
WHERE parent = '{{ parent }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="get">

Retrieves information about the specified Postgres role, including its authentication method and

```sql
SELECT
name,
create_time,
parent,
spec,
status,
update_time
FROM databricks_workspace.postgres.postgres_roles
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
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

Creates a new Postgres role in the branch.

```sql
INSERT INTO databricks_workspace.postgres.postgres_roles (
role,
parent,
deployment_name,
role_id
)
SELECT 
'{{ role }}' /* required */,
'{{ parent }}',
'{{ deployment_name }}',
'{{ role_id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: postgres_roles
  props:
    - name: parent
      value: string
      description: Required parameter for the postgres_roles resource.
    - name: deployment_name
      value: string
      description: Required parameter for the postgres_roles resource.
    - name: role
      value: string
      description: |
        The desired specification of a Role.
    - name: role_id
      value: string
      description: The ID to use for the Role, which will become the final component of the role's resource name. This ID becomes the role in Postgres. This value should be 4-63 characters, and valid characters are lowercase letters, numbers, and hyphens, as defined by RFC 1123. If role_id is not specified in the request, it is generated automatically.
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

Deletes the specified Postgres role.

```sql
DELETE FROM databricks_workspace.postgres.postgres_roles
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND reassign_owned_to = '{{ reassign_owned_to }}'
;
```
</TabItem>
</Tabs>

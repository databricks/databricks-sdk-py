---
title: vw_account_user_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_account_user_roles
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>vw_account_user_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_account_user_roles" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.vw_account_user_roles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Databricks account ID used to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the account user.</td>
</tr>
<tr>
    <td><CopyableCode code="userName" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Username (typically email address) of the account user.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable display name of the account user.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Role assigned to the user (one row per role assignment).</td>
</tr>
</tbody>
</table>

## Required Parameters

The following parameters are required by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Databricks account ID used to scope the query.</td>
</tr>
</tbody>
</table>

## `SELECT` Examples

```sql
SELECT
  account_id,
  id,
  userName,
  displayName,
  role
FROM databricks_account.iam.vw_account_user_roles
WHERE account_id = '{{ account_id }}';
```

## SQL Definition

<Tabs
defaultValue="Sqlite3"
values={[
{ label: 'Sqlite3', value: 'Sqlite3' },
{ label: 'Postgres', value: 'Postgres' }
]}
>
<TabItem value="Sqlite3">

```sql
SELECT
  u.account_id,
  u.id,
  u.userName,
  u.displayName,
  JSON_EXTRACT(r.value, '$.value') AS role
FROM databricks_account.iam.account_users u,
     JSON_EACH(u.roles) r
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  u.account_id,
  u.id,
  u.userName,
  u.displayName,
  r.value->>'value' AS role
FROM databricks_account.iam.account_users u,
     jsonb_array_elements(u.roles::jsonb) AS r
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

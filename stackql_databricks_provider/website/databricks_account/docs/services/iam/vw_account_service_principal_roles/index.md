---
title: vw_account_service_principal_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_account_service_principal_roles
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

Creates, updates, deletes, gets or lists a <code>vw_account_service_principal_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_account_service_principal_roles" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.vw_account_service_principal_roles" /></td></tr>
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
    <td>Unique identifier for the service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable display name of the service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationId" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Application ID of the service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="active" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether the service principal is active.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Role assigned to the service principal (one row per role assignment).</td>
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
  displayName,
  applicationId,
  active,
  role
FROM databricks_account.iam.vw_account_service_principal_roles
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
  sp.account_id,
  sp.id,
  sp.displayName,
  sp.applicationId,
  sp.active,
  JSON_EXTRACT(r.value, '$.value') AS role
FROM databricks_account.iam.account_service_principals sp,
     JSON_EACH(sp.roles) r
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  sp.account_id,
  sp.id,
  sp.displayName,
  sp.applicationId,
  sp.active,
  r.value->>'value' AS role
FROM databricks_account.iam.account_service_principals sp,
     jsonb_array_elements(sp.roles::jsonb) AS r
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

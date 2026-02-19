---
title: vw_account_group_members
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_account_group_members
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

Creates, updates, deletes, gets or lists a <code>vw_account_group_members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_account_group_members" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.vw_account_group_members" /></td></tr>
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
    <td>Unique identifier for the account group.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable display name of the account group.</td>
</tr>
<tr>
    <td><CopyableCode code="member_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier of the group member (one row per member).</td>
</tr>
<tr>
    <td><CopyableCode code="member_display" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Display name of the group member.</td>
</tr>
<tr>
    <td><CopyableCode code="member_ref" /></td>
    <td><CopyableCode code="string" /></td>
    <td>SCIM $ref URI for the group member resource.</td>
</tr>
<tr>
    <td><CopyableCode code="member_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Type of the member resource (e.g. User, Group, ServicePrincipal).</td>
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
  member_id,
  member_display,
  member_ref,
  member_type
FROM databricks_account.iam.vw_account_group_members
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
  g.account_id,
  g.id,
  g.displayName,
  JSON_EXTRACT(m.value, '$.value') AS member_id,
  JSON_EXTRACT(m.value, '$.display') AS member_display,
  JSON_EXTRACT(m.value, '$.$ref') AS member_ref,
  JSON_EXTRACT(m.value, '$.type') AS member_type
FROM databricks_account.iam.account_groups g,
     JSON_EACH(g.members) m
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  g.account_id,
  g.id,
  g.displayName,
  m.value->>'value' AS member_id,
  m.value->>'display' AS member_display,
  m.value->>'$ref' AS member_ref,
  m.value->>'type' AS member_type
FROM databricks_account.iam.account_groups g,
     jsonb_array_elements(g.members::jsonb) AS m
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

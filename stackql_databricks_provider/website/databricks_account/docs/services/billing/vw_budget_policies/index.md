---
title: vw_budget_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_budget_policies
  - billing
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

Creates, updates, deletes, gets or lists a <code>vw_budget_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_budget_policies" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.vw_budget_policies" /></td></tr>
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
    <td><CopyableCode code="policy_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the budget policy.</td>
</tr>
<tr>
    <td><CopyableCode code="policy_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Display name of the budget policy.</td>
</tr>
<tr>
    <td><CopyableCode code="custom_tags" /></td>
    <td><CopyableCode code="object" /></td>
    <td>Key-value custom tags associated with the budget policy.</td>
</tr>
<tr>
    <td><CopyableCode code="binding_workspace_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of a workspace bound to this budget policy (one row per workspace).</td>
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
  policy_id,
  policy_name,
  custom_tags,
  binding_workspace_id
FROM databricks_account.billing.vw_budget_policies
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
  p.account_id,
  p.policy_id,
  p.policy_name,
  p.custom_tags,
  w.value AS binding_workspace_id
FROM databricks_account.billing.budget_policy p,
     JSON_EACH(p.binding_workspace_ids) w
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  p.account_id,
  p.policy_id,
  p.policy_name,
  p.custom_tags,
  w.value AS binding_workspace_id
FROM databricks_account.billing.budget_policy p,
     jsonb_array_elements(p.binding_workspace_ids::jsonb) AS w
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

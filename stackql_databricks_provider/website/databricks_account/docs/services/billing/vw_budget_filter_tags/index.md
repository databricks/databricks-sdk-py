---
title: vw_budget_filter_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_budget_filter_tags
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>vw_budget_filter_tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_budget_filter_tags" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.vw_budget_filter_tags" /></td></tr>
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
    <td><CopyableCode code="budget_configuration_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the budget configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="display_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable name of the budget.</td>
</tr>
<tr>
    <td><CopyableCode code="tag_key" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Tag key used in the budget filter (one row per tag entry).</td>
</tr>
<tr>
    <td><CopyableCode code="tag_operator" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Comparison operator applied to the tag value filter (e.g. IN, NOT_IN).</td>
</tr>
<tr>
    <td><CopyableCode code="tag_values" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of tag values matched by the operator for this tag key.</td>
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
  budget_configuration_id,
  display_name,
  tag_key,
  tag_operator,
  tag_values
FROM databricks_account.billing.vw_budget_filter_tags
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
  b.account_id,
  b.budget_configuration_id,
  b.display_name,
  JSON_EXTRACT(t.value, '$.key') AS tag_key,
  JSON_EXTRACT(t.value, '$.value.operator') AS tag_operator,
  JSON_EXTRACT(t.value, '$.value.values') AS tag_values
FROM databricks_account.billing.budgets b,
     JSON_EACH(JSON_EXTRACT(b.filter, '$.tags')) t
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  b.account_id,
  b.budget_configuration_id,
  b.display_name,
  t.value->>'key' AS tag_key,
  t.value->'value'->>'operator' AS tag_operator,
  t.value->'value'->'values' AS tag_values
FROM databricks_account.billing.budgets b,
     jsonb_array_elements((b.filter->'tags')::jsonb) AS t
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

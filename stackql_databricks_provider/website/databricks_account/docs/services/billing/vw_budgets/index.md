---
title: vw_budgets
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_budgets
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

Creates, updates, deletes, gets or lists a <code>vw_budgets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_budgets" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.vw_budgets" /></td></tr>
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
    <td><CopyableCode code="create_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the budget was created (ISO 8601).</td>
</tr>
<tr>
    <td><CopyableCode code="update_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the budget was last updated (ISO 8601).</td>
</tr>
<tr>
    <td><CopyableCode code="filter_workspace_operator" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Comparison operator applied to the workspace ID filter (e.g. IN, NOT_IN).</td>
</tr>
<tr>
    <td><CopyableCode code="filter_workspace_ids" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of workspace IDs used in the budget filter.</td>
</tr>
<tr>
    <td><CopyableCode code="filter_tags" /></td>
    <td><CopyableCode code="array" /></td>
    <td>Tag-based filter criteria applied to this budget.</td>
</tr>
<tr>
    <td><CopyableCode code="alert_configuration_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the alert configuration (one row per alert).</td>
</tr>
<tr>
    <td><CopyableCode code="quantity_threshold" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Threshold value that triggers the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unit of the threshold quantity (e.g. LIST_PRICE_DOLLARS).</td>
</tr>
<tr>
    <td><CopyableCode code="time_period" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Time window evaluated for budget alerting (e.g. MONTH).</td>
</tr>
<tr>
    <td><CopyableCode code="trigger_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Condition that triggers the alert (e.g. CUMULATIVE_SPENDING_EXCEEDED).</td>
</tr>
<tr>
    <td><CopyableCode code="action_configurations" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of actions to execute when the alert fires.</td>
</tr>
</tbody>
</table>

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
  b.create_time,
  b.update_time,
  JSON_EXTRACT(b.filter, '$.workspace_id.operator') AS filter_workspace_operator,
  JSON_EXTRACT(b.filter, '$.workspace_id.values') AS filter_workspace_ids,
  JSON_EXTRACT(b.filter, '$.tags') AS filter_tags,
  JSON_EXTRACT(ac.value, '$.alert_configuration_id') AS alert_configuration_id,
  JSON_EXTRACT(ac.value, '$.quantity_threshold') AS quantity_threshold,
  JSON_EXTRACT(ac.value, '$.quantity_type') AS quantity_type,
  JSON_EXTRACT(ac.value, '$.time_period') AS time_period,
  JSON_EXTRACT(ac.value, '$.trigger_type') AS trigger_type,
  JSON_EXTRACT(ac.value, '$.action_configurations') AS action_configurations
FROM databricks_account.billing.budgets b,
     JSON_EACH(b.alert_configurations) ac
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  b.account_id,
  b.budget_configuration_id,
  b.display_name,
  b.create_time,
  b.update_time,
  b.filter->'workspace_id'->>'operator' AS filter_workspace_operator,
  b.filter->'workspace_id'->'values' AS filter_workspace_ids,
  b.filter->'tags' AS filter_tags,
  ac.value->>'alert_configuration_id' AS alert_configuration_id,
  ac.value->>'quantity_threshold' AS quantity_threshold,
  ac.value->>'quantity_type' AS quantity_type,
  ac.value->>'time_period' AS time_period,
  ac.value->>'trigger_type' AS trigger_type,
  ac.value->'action_configurations' AS action_configurations
FROM databricks_account.billing.budgets b,
     jsonb_array_elements(b.alert_configurations::jsonb) AS ac
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

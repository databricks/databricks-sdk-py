---
title: vw_budget_alert_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_budget_alert_actions
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

Creates, updates, deletes, gets or lists a <code>vw_budget_alert_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_budget_alert_actions" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.vw_budget_alert_actions" /></td></tr>
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
    <td><CopyableCode code="alert_configuration_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the alert configuration this action belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity_threshold" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Threshold value that triggers the parent alert.</td>
</tr>
<tr>
    <td><CopyableCode code="action_configuration_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for this action configuration (one row per action).</td>
</tr>
<tr>
    <td><CopyableCode code="action_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Type of action to perform when the alert fires (e.g. EMAIL_NOTIFICATION).</td>
</tr>
<tr>
    <td><CopyableCode code="action_target" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Target for the action, such as an email address or webhook URL.</td>
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
  alert_configuration_id,
  quantity_threshold,
  action_configuration_id,
  action_type,
  action_target
FROM databricks_account.billing.vw_budget_alert_actions
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
  JSON_EXTRACT(ac.value, '$.alert_configuration_id') AS alert_configuration_id,
  JSON_EXTRACT(ac.value, '$.quantity_threshold') AS quantity_threshold,
  JSON_EXTRACT(act.value, '$.action_configuration_id') AS action_configuration_id,
  JSON_EXTRACT(act.value, '$.action_type') AS action_type,
  JSON_EXTRACT(act.value, '$.target') AS action_target
FROM databricks_account.billing.budgets b,
     JSON_EACH(b.alert_configurations) ac,
     JSON_EACH(JSON_EXTRACT(ac.value, '$.action_configurations')) act
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  b.account_id,
  b.budget_configuration_id,
  b.display_name,
  ac.value->>'alert_configuration_id' AS alert_configuration_id,
  ac.value->>'quantity_threshold' AS quantity_threshold,
  act.value->>'action_configuration_id' AS action_configuration_id,
  act.value->>'action_type' AS action_type,
  act.value->>'target' AS action_target
FROM databricks_account.billing.budgets b,
     jsonb_array_elements(b.alert_configurations::jsonb) AS ac,
     jsonb_array_elements((ac.value->'action_configurations')::jsonb) AS act
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

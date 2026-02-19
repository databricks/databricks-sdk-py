---
title: vw_log_delivery_workspace_filter
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_log_delivery_workspace_filter
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

Creates, updates, deletes, gets or lists a <code>vw_log_delivery_workspace_filter</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_log_delivery_workspace_filter" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.vw_log_delivery_workspace_filter" /></td></tr>
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
    <td><CopyableCode code="config_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the log delivery configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="config_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable name of the log delivery configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="log_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Type of logs being delivered (e.g. BILLABLE_USAGE, AUDIT_LOGS).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Enabled/disabled status of the log delivery configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="delivery_status" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Status of the most recent log delivery attempt.</td>
</tr>
<tr>
    <td><CopyableCode code="workspace_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of a workspace included in the delivery filter (one row per workspace).</td>
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
  config_id,
  config_name,
  log_type,
  status,
  delivery_status,
  workspace_id
FROM databricks_account.billing.vw_log_delivery_workspace_filter
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
  ld.account_id,
  ld.config_id,
  ld.config_name,
  ld.log_type,
  ld.status,
  JSON_EXTRACT(ld.log_delivery_status, '$.status') AS delivery_status,
  w.value AS workspace_id
FROM databricks_account.billing.log_delivery ld,
     JSON_EACH(ld.workspace_ids_filter) w
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  ld.account_id,
  ld.config_id,
  ld.config_name,
  ld.log_type,
  ld.status,
  ld.log_delivery_status->>'status' AS delivery_status,
  w.value AS workspace_id
FROM databricks_account.billing.log_delivery ld,
     jsonb_array_elements(ld.workspace_ids_filter::jsonb) AS w
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

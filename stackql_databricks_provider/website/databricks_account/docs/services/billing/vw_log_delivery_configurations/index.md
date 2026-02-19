---
title: vw_log_delivery_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_log_delivery_configurations
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

Creates, updates, deletes, gets or lists a <code>vw_log_delivery_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_log_delivery_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.vw_log_delivery_configurations" /></td></tr>
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
    <td><CopyableCode code="output_format" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Format of the delivered log files (e.g. CSV, JSON).</td>
</tr>
<tr>
    <td><CopyableCode code="credentials_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the credentials used to write logs to the storage destination.</td>
</tr>
<tr>
    <td><CopyableCode code="storage_configuration_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the storage configuration that defines the delivery destination.</td>
</tr>
<tr>
    <td><CopyableCode code="delivery_path_prefix" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Optional path prefix prepended to log file paths in the storage destination.</td>
</tr>
<tr>
    <td><CopyableCode code="delivery_start_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Optional earliest date from which logs are delivered (YYYY-MM-DD).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Enabled/disabled status of the log delivery configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the configuration was created.</td>
</tr>
<tr>
    <td><CopyableCode code="update_time" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the configuration was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="delivery_status" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Status of the most recent log delivery attempt.</td>
</tr>
<tr>
    <td><CopyableCode code="delivery_status_message" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable message describing the most recent delivery attempt result.</td>
</tr>
<tr>
    <td><CopyableCode code="last_attempt_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp of the most recent delivery attempt (ISO 8601).</td>
</tr>
<tr>
    <td><CopyableCode code="last_successful_attempt_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp of the most recent successful delivery attempt (ISO 8601).</td>
</tr>
<tr>
    <td><CopyableCode code="workspace_ids_filter" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of workspace IDs to include in log delivery; empty means all workspaces.</td>
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
  output_format,
  credentials_id,
  storage_configuration_id,
  delivery_path_prefix,
  delivery_start_time,
  status,
  creation_time,
  update_time,
  delivery_status,
  delivery_status_message,
  last_attempt_time,
  last_successful_attempt_time,
  workspace_ids_filter
FROM databricks_account.billing.vw_log_delivery_configurations
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
  ld.output_format,
  ld.credentials_id,
  ld.storage_configuration_id,
  ld.delivery_path_prefix,
  ld.delivery_start_time,
  ld.status,
  ld.creation_time,
  ld.update_time,
  JSON_EXTRACT(ld.log_delivery_status, '$.status') AS delivery_status,
  JSON_EXTRACT(ld.log_delivery_status, '$.message') AS delivery_status_message,
  JSON_EXTRACT(ld.log_delivery_status, '$.last_attempt_time') AS last_attempt_time,
  JSON_EXTRACT(ld.log_delivery_status, '$.last_successful_attempt_time') AS last_successful_attempt_time,
  ld.workspace_ids_filter
FROM databricks_account.billing.log_delivery ld
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
  ld.output_format,
  ld.credentials_id,
  ld.storage_configuration_id,
  ld.delivery_path_prefix,
  ld.delivery_start_time,
  ld.status,
  ld.creation_time,
  ld.update_time,
  ld.log_delivery_status->>'status' AS delivery_status,
  ld.log_delivery_status->>'message' AS delivery_status_message,
  ld.log_delivery_status->>'last_attempt_time' AS last_attempt_time,
  ld.log_delivery_status->>'last_successful_attempt_time' AS last_successful_attempt_time,
  ld.workspace_ids_filter
FROM databricks_account.billing.log_delivery ld
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

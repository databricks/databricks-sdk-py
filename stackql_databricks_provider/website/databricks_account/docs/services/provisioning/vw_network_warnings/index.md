---
title: vw_network_warnings
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_network_warnings
  - provisioning
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

Creates, updates, deletes, gets or lists a <code>vw_network_warnings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_network_warnings" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.vw_network_warnings" /></td></tr>
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
    <td><CopyableCode code="network_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the network configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="network_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable name of the network configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpc_status" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Validation status of the VPC at the time of the warning.</td>
</tr>
<tr>
    <td><CopyableCode code="warning_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Category of the network validation warning (one row per warning).</td>
</tr>
<tr>
    <td><CopyableCode code="warning_message" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable description of the network validation warning.</td>
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
  network_id,
  network_name,
  vpc_status,
  warning_type,
  warning_message
FROM databricks_account.provisioning.vw_network_warnings
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
  n.account_id,
  n.network_id,
  n.network_name,
  n.vpc_status,
  JSON_EXTRACT(w.value, '$.warning_type') AS warning_type,
  JSON_EXTRACT(w.value, '$.warning_message') AS warning_message
FROM databricks_account.provisioning.networks n,
     JSON_EACH(n.warning_messages) w
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  n.account_id,
  n.network_id,
  n.network_name,
  n.vpc_status,
  w.value->>'warning_type' AS warning_type,
  w.value->>'warning_message' AS warning_message
FROM databricks_account.provisioning.networks n,
     jsonb_array_elements(n.warning_messages::jsonb) AS w
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

---
title: vw_network_errors
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_network_errors
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

Creates, updates, deletes, gets or lists a <code>vw_network_errors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_network_errors" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.vw_network_errors" /></td></tr>
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
    <td>Validation status of the VPC at the time of the error.</td>
</tr>
<tr>
    <td><CopyableCode code="error_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Category of the network validation error (one row per error).</td>
</tr>
<tr>
    <td><CopyableCode code="error_message" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable description of the network validation error.</td>
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
  n.account_id,
  n.network_id,
  n.network_name,
  n.vpc_status,
  JSON_EXTRACT(e.value, '$.error_type') AS error_type,
  JSON_EXTRACT(e.value, '$.error_message') AS error_message
FROM databricks_account.provisioning.networks n,
     JSON_EACH(n.error_messages) e
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
  e.value->>'error_type' AS error_type,
  e.value->>'error_message' AS error_message
FROM databricks_account.provisioning.networks n,
     jsonb_array_elements(n.error_messages::jsonb) AS e
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

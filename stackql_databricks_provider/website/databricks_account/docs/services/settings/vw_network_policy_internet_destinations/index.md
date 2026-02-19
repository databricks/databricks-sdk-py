---
title: vw_network_policy_internet_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_network_policy_internet_destinations
  - settings
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

Creates, updates, deletes, gets or lists a <code>vw_network_policy_internet_destinations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_network_policy_internet_destinations" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.vw_network_policy_internet_destinations" /></td></tr>
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
    <td><CopyableCode code="network_policy_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the network policy.</td>
</tr>
<tr>
    <td><CopyableCode code="restriction_mode" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Overall egress restriction mode for the policy (e.g. FULL_RESTRICTION, NO_RESTRICTION).</td>
</tr>
<tr>
    <td><CopyableCode code="enforcement_mode" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Enforcement mode for the egress policy (e.g. ENFORCED, AUDIT).</td>
</tr>
<tr>
    <td><CopyableCode code="destination" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Allowed internet destination hostname or CIDR (one row per destination).</td>
</tr>
<tr>
    <td><CopyableCode code="destination_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Classification of the allowed internet destination (e.g. PUBLIC).</td>
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
  network_policy_id,
  restriction_mode,
  enforcement_mode,
  destination,
  destination_type
FROM databricks_account.settings.vw_network_policy_internet_destinations
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
  np.account_id,
  np.network_policy_id,
  JSON_EXTRACT(np.egress, '$.network_access.restriction_mode') AS restriction_mode,
  JSON_EXTRACT(np.egress, '$.network_access.policy_enforcement.enforcement_mode') AS enforcement_mode,
  JSON_EXTRACT(d.value, '$.destination') AS destination,
  JSON_EXTRACT(d.value, '$.internet_destination_type') AS destination_type
FROM databricks_account.settings.network_policies np,
     JSON_EACH(JSON_EXTRACT(np.egress, '$.network_access.allowed_internet_destinations')) d
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  np.account_id,
  np.network_policy_id,
  np.egress->'network_access'->>'restriction_mode' AS restriction_mode,
  np.egress->'network_access'->'policy_enforcement'->>'enforcement_mode' AS enforcement_mode,
  d.value->>'destination' AS destination,
  d.value->>'internet_destination_type' AS destination_type
FROM databricks_account.settings.network_policies np,
     jsonb_array_elements((np.egress->'network_access'->'allowed_internet_destinations')::jsonb) AS d
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

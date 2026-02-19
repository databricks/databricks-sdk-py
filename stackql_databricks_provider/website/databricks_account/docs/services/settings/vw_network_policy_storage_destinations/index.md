---
title: vw_network_policy_storage_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_network_policy_storage_destinations
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

Creates, updates, deletes, gets or lists a <code>vw_network_policy_storage_destinations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_network_policy_storage_destinations" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.vw_network_policy_storage_destinations" /></td></tr>
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
    <td><CopyableCode code="storage_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Cloud storage type for this allowed destination (one row per destination, e.g. AWS_S3, AZURE_STORAGE).</td>
</tr>
<tr>
    <td><CopyableCode code="bucket_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the allowed S3 bucket (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Cloud region of the allowed storage destination (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_storage_account" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the allowed Azure storage account (Azure only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_storage_service" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Azure storage service type for this destination (e.g. blob, dfs) (Azure only).</td>
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
  np.account_id,
  np.network_policy_id,
  JSON_EXTRACT(np.egress, '$.network_access.restriction_mode') AS restriction_mode,
  JSON_EXTRACT(np.egress, '$.network_access.policy_enforcement.enforcement_mode') AS enforcement_mode,
  JSON_EXTRACT(d.value, '$.storage_destination_type') AS storage_type,
  JSON_EXTRACT(d.value, '$.bucket_name') AS bucket_name,
  JSON_EXTRACT(d.value, '$.region') AS region,
  JSON_EXTRACT(d.value, '$.azure_storage_account') AS azure_storage_account,
  JSON_EXTRACT(d.value, '$.azure_storage_service') AS azure_storage_service
FROM databricks_account.settings.network_policies np,
     JSON_EACH(JSON_EXTRACT(np.egress, '$.network_access.allowed_storage_destinations')) d
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
  d.value->>'storage_destination_type' AS storage_type,
  d.value->>'bucket_name' AS bucket_name,
  d.value->>'region' AS region,
  d.value->>'azure_storage_account' AS azure_storage_account,
  d.value->>'azure_storage_service' AS azure_storage_service
FROM databricks_account.settings.network_policies np,
     jsonb_array_elements((np.egress->'network_access'->'allowed_storage_destinations')::jsonb) AS d
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

---
title: vw_ip_access_list_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_ip_access_list_addresses
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

Creates, updates, deletes, gets or lists a <code>vw_ip_access_list_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_ip_access_list_addresses" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.vw_ip_access_list_addresses" /></td></tr>
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
    <td><CopyableCode code="list_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the IP access list.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable label for the IP access list.</td>
</tr>
<tr>
    <td><CopyableCode code="list_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Type of the IP access list - either ALLOW or BLOCK.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether the IP access list is currently active.</td>
</tr>
<tr>
    <td><CopyableCode code="address_count" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Total number of IP addresses or CIDR ranges in this list.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the IP access list was created.</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>ID of the user who created the IP access list.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the IP access list was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_by" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>ID of the user who last updated the IP access list.</td>
</tr>
<tr>
    <td><CopyableCode code="ip_address" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Individual IP address or CIDR range entry from the list (one row per entry).</td>
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
  l.account_id,
  l.list_id,
  l.label,
  l.list_type,
  l.enabled,
  l.address_count,
  l.created_at,
  l.created_by,
  l.updated_at,
  l.updated_by,
  a.value AS ip_address
FROM databricks_account.settings.account_ip_access_lists l,
     JSON_EACH(l.ip_addresses) a
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  l.account_id,
  l.list_id,
  l.label,
  l.list_type,
  l.enabled,
  l.address_count,
  l.created_at,
  l.created_by,
  l.updated_at,
  l.updated_by,
  a.value AS ip_address
FROM databricks_account.settings.account_ip_access_lists l,
     jsonb_array_elements(l.ip_addresses::jsonb) AS a
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

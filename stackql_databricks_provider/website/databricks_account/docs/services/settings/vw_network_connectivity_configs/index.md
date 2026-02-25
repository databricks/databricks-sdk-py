---
title: vw_network_connectivity_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_network_connectivity_configs
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>vw_network_connectivity_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_network_connectivity_configs" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.vw_network_connectivity_configs" /></td></tr>
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
    <td><CopyableCode code="network_connectivity_config_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the network connectivity configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable name of the network connectivity configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Cloud region where this network connectivity configuration applies.</td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the configuration was created.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_time" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the configuration was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="aws_stable_ip_cidr_blocks" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of stable CIDR blocks used for outbound traffic from Databricks (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_svc_endpoint_region" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Azure region targeted by the default service endpoint rule (Azure only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_svc_endpoint_subnets" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of subnets covered by the default Azure service endpoint rule (Azure only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_svc_endpoint_services" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of Azure services targeted by the default service endpoint rule (Azure only).</td>
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
  network_connectivity_config_id,
  name,
  region,
  creation_time,
  updated_time,
  aws_stable_ip_cidr_blocks,
  azure_svc_endpoint_region,
  azure_svc_endpoint_subnets,
  azure_svc_endpoint_services
FROM databricks_account.settings.vw_network_connectivity_configs
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
  ncc.account_id,
  ncc.network_connectivity_config_id,
  ncc.name,
  ncc.region,
  ncc.creation_time,
  ncc.updated_time,
  JSON_EXTRACT(ncc.egress_config, '$.default_rules.aws_stable_ip_rule.cidr_blocks') AS aws_stable_ip_cidr_blocks,
  JSON_EXTRACT(ncc.egress_config, '$.default_rules.azure_service_endpoint_rule.target_region') AS azure_svc_endpoint_region,
  JSON_EXTRACT(ncc.egress_config, '$.default_rules.azure_service_endpoint_rule.subnets') AS azure_svc_endpoint_subnets,
  JSON_EXTRACT(ncc.egress_config, '$.default_rules.azure_service_endpoint_rule.target_services') AS azure_svc_endpoint_services
FROM databricks_account.settings.network_connectivity ncc
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  ncc.account_id,
  ncc.network_connectivity_config_id,
  ncc.name,
  ncc.region,
  ncc.creation_time,
  ncc.updated_time,
  ncc.egress_config->'default_rules'->'aws_stable_ip_rule'->'cidr_blocks' AS aws_stable_ip_cidr_blocks,
  ncc.egress_config->'default_rules'->'azure_service_endpoint_rule'->>'target_region' AS azure_svc_endpoint_region,
  ncc.egress_config->'default_rules'->'azure_service_endpoint_rule'->'subnets' AS azure_svc_endpoint_subnets,
  ncc.egress_config->'default_rules'->'azure_service_endpoint_rule'->'target_services' AS azure_svc_endpoint_services
FROM databricks_account.settings.network_connectivity ncc
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

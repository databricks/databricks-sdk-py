---
title: vw_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_networks
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

Creates, updates, deletes, gets or lists a <code>vw_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_networks" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.vw_networks" /></td></tr>
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
    <td><CopyableCode code="vpc_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the VPC used by this network configuration (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="vpc_status" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Validation status of the VPC (e.g. VALID, BROKEN, UNATTACHED).</td>
</tr>
<tr>
    <td><CopyableCode code="workspace_id" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>ID of the workspace this network configuration is attached to.</td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the network configuration was created.</td>
</tr>
<tr>
    <td><CopyableCode code="security_group_ids" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of security group IDs associated with this network configuration (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="subnet_ids" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of subnet IDs associated with this network configuration (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_network_project_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>GCP project ID that hosts the shared VPC network (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_vpc_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the GCP VPC network (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_subnet_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the GCP subnet used by the workspace (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_subnet_region" /></td>
    <td><CopyableCode code="string" /></td>
    <td>GCP region where the subnet is located (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_pod_ip_range_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the secondary IP range used for GKE pods (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_service_ip_range_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the secondary IP range used for GKE services (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="vpc_endpoint_rest_api_ids" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of VPC endpoint IDs used for REST API private connectivity (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="vpc_endpoint_dataplane_relay_ids" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of VPC endpoint IDs used for dataplane relay private connectivity (AWS only).</td>
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
  vpc_id,
  vpc_status,
  workspace_id,
  creation_time,
  security_group_ids,
  subnet_ids,
  gcp_network_project_id,
  gcp_vpc_id,
  gcp_subnet_id,
  gcp_subnet_region,
  gcp_pod_ip_range_name,
  gcp_service_ip_range_name,
  vpc_endpoint_rest_api_ids,
  vpc_endpoint_dataplane_relay_ids
FROM databricks_account.provisioning.vw_networks
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
  n.vpc_id,
  n.vpc_status,
  n.workspace_id,
  n.creation_time,
  n.security_group_ids,
  n.subnet_ids,
  JSON_EXTRACT(n.gcp_network_info, '$.network_project_id') AS gcp_network_project_id,
  JSON_EXTRACT(n.gcp_network_info, '$.vpc_id') AS gcp_vpc_id,
  JSON_EXTRACT(n.gcp_network_info, '$.subnet_id') AS gcp_subnet_id,
  JSON_EXTRACT(n.gcp_network_info, '$.subnet_region') AS gcp_subnet_region,
  JSON_EXTRACT(n.gcp_network_info, '$.pod_ip_range_name') AS gcp_pod_ip_range_name,
  JSON_EXTRACT(n.gcp_network_info, '$.service_ip_range_name') AS gcp_service_ip_range_name,
  JSON_EXTRACT(n.vpc_endpoints, '$.rest_api') AS vpc_endpoint_rest_api_ids,
  JSON_EXTRACT(n.vpc_endpoints, '$.dataplane_relay') AS vpc_endpoint_dataplane_relay_ids
FROM databricks_account.provisioning.networks n
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  n.account_id,
  n.network_id,
  n.network_name,
  n.vpc_id,
  n.vpc_status,
  n.workspace_id,
  n.creation_time,
  n.security_group_ids,
  n.subnet_ids,
  n.gcp_network_info->>'network_project_id' AS gcp_network_project_id,
  n.gcp_network_info->>'vpc_id' AS gcp_vpc_id,
  n.gcp_network_info->>'subnet_id' AS gcp_subnet_id,
  n.gcp_network_info->>'subnet_region' AS gcp_subnet_region,
  n.gcp_network_info->>'pod_ip_range_name' AS gcp_pod_ip_range_name,
  n.gcp_network_info->>'service_ip_range_name' AS gcp_service_ip_range_name,
  n.vpc_endpoints->'rest_api' AS vpc_endpoint_rest_api_ids,
  n.vpc_endpoints->'dataplane_relay' AS vpc_endpoint_dataplane_relay_ids
FROM databricks_account.provisioning.networks n
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

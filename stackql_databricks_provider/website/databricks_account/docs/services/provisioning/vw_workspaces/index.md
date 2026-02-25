---
title: vw_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_workspaces
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>vw_workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_workspaces" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.vw_workspaces" /></td></tr>
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
    <td><CopyableCode code="workspace_id" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unique numeric identifier for the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="workspace_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable name of the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="workspace_status" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Current provisioning status of the workspace (e.g. RUNNING, PROVISIONING, FAILED).</td>
</tr>
<tr>
    <td><CopyableCode code="workspace_status_message" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable message describing the current workspace status.</td>
</tr>
<tr>
    <td><CopyableCode code="cloud" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Cloud provider hosting the workspace (e.g. aws, azure, gcp).</td>
</tr>
<tr>
    <td><CopyableCode code="aws_region" /></td>
    <td><CopyableCode code="string" /></td>
    <td>AWS region where the workspace is deployed (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Cloud region or location where the workspace is deployed (Azure/GCP).</td>
</tr>
<tr>
    <td><CopyableCode code="deployment_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Subdomain component of the workspace URL (e.g. mycompany in mycompany.azuredatabricks.net).</td>
</tr>
<tr>
    <td><CopyableCode code="pricing_tier" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Pricing tier of the workspace (e.g. PREMIUM, ENTERPRISE, STANDARD).</td>
</tr>
<tr>
    <td><CopyableCode code="compute_mode" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Compute isolation mode for the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="storage_mode" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Storage isolation mode for the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="credentials_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the cross-account credential configuration used by this workspace (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="storage_configuration_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the root storage configuration for this workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="network_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the customer-managed network configuration for this workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="network_connectivity_config_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the network connectivity configuration for private access.</td>
</tr>
<tr>
    <td><CopyableCode code="managed_services_customer_managed_key_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the customer-managed key used to encrypt managed services data.</td>
</tr>
<tr>
    <td><CopyableCode code="storage_customer_managed_key_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the customer-managed key used to encrypt workspace storage.</td>
</tr>
<tr>
    <td><CopyableCode code="private_access_settings_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the private access settings configuration for this workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the workspace was created.</td>
</tr>
<tr>
    <td><CopyableCode code="custom_tags" /></td>
    <td><CopyableCode code="object" /></td>
    <td>Key-value custom tags applied to cloud resources provisioned for this workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="azure_subscription_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Azure subscription ID where the workspace is deployed (Azure only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_resource_group" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Azure resource group containing the workspace resources (Azure only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_project_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>GCP project ID that contains the workspace resources (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_subnet_cidr" /></td>
    <td><CopyableCode code="string" /></td>
    <td>CIDR range for the GCP managed network subnet (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_pod_ip_range" /></td>
    <td><CopyableCode code="string" /></td>
    <td>IP range used for GKE cluster pods (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_service_ip_range" /></td>
    <td><CopyableCode code="string" /></td>
    <td>IP range used for GKE cluster services (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gke_connectivity_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>GKE cluster connectivity type (e.g. PRIVATE_NODE_PUBLIC_MASTER, PUBLIC_NODE_PUBLIC_MASTER) (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gke_master_ip_range" /></td>
    <td><CopyableCode code="string" /></td>
    <td>CIDR range for the GKE control plane (GCP only).</td>
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
  workspace_id,
  workspace_name,
  workspace_status,
  workspace_status_message,
  cloud,
  aws_region,
  location,
  deployment_name,
  pricing_tier,
  compute_mode,
  storage_mode,
  credentials_id,
  storage_configuration_id,
  network_id,
  network_connectivity_config_id,
  managed_services_customer_managed_key_id,
  storage_customer_managed_key_id,
  private_access_settings_id,
  creation_time,
  custom_tags,
  azure_subscription_id,
  azure_resource_group,
  gcp_project_id,
  gcp_subnet_cidr,
  gcp_pod_ip_range,
  gcp_service_ip_range,
  gke_connectivity_type,
  gke_master_ip_range
FROM databricks_account.provisioning.vw_workspaces
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
  w.account_id,
  w.workspace_id,
  w.workspace_name,
  w.workspace_status,
  w.workspace_status_message,
  w.cloud,
  w.aws_region,
  w.location,
  w.deployment_name,
  w.pricing_tier,
  w.compute_mode,
  w.storage_mode,
  w.credentials_id,
  w.storage_configuration_id,
  w.network_id,
  w.network_connectivity_config_id,
  w.managed_services_customer_managed_key_id,
  w.storage_customer_managed_key_id,
  w.private_access_settings_id,
  w.creation_time,
  w.custom_tags,
  JSON_EXTRACT(w.azure_workspace_info, '$.subscription_id') AS azure_subscription_id,
  JSON_EXTRACT(w.azure_workspace_info, '$.resource_group') AS azure_resource_group,
  JSON_EXTRACT(w.cloud_resource_container, '$.gcp.project_id') AS gcp_project_id,
  JSON_EXTRACT(w.gcp_managed_network_config, '$.subnet_cidr') AS gcp_subnet_cidr,
  JSON_EXTRACT(w.gcp_managed_network_config, '$.gke_cluster_pod_ip_range') AS gcp_pod_ip_range,
  JSON_EXTRACT(w.gcp_managed_network_config, '$.gke_cluster_service_ip_range') AS gcp_service_ip_range,
  JSON_EXTRACT(w.gke_config, '$.connectivity_type') AS gke_connectivity_type,
  JSON_EXTRACT(w.gke_config, '$.master_ip_range') AS gke_master_ip_range
FROM databricks_account.provisioning.workspaces w
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  w.account_id,
  w.workspace_id,
  w.workspace_name,
  w.workspace_status,
  w.workspace_status_message,
  w.cloud,
  w.aws_region,
  w.location,
  w.deployment_name,
  w.pricing_tier,
  w.compute_mode,
  w.storage_mode,
  w.credentials_id,
  w.storage_configuration_id,
  w.network_id,
  w.network_connectivity_config_id,
  w.managed_services_customer_managed_key_id,
  w.storage_customer_managed_key_id,
  w.private_access_settings_id,
  w.creation_time,
  w.custom_tags,
  w.azure_workspace_info->>'subscription_id' AS azure_subscription_id,
  w.azure_workspace_info->>'resource_group' AS azure_resource_group,
  w.cloud_resource_container->'gcp'->>'project_id' AS gcp_project_id,
  w.gcp_managed_network_config->>'subnet_cidr' AS gcp_subnet_cidr,
  w.gcp_managed_network_config->>'gke_cluster_pod_ip_range' AS gcp_pod_ip_range,
  w.gcp_managed_network_config->>'gke_cluster_service_ip_range' AS gcp_service_ip_range,
  w.gke_config->>'connectivity_type' AS gke_connectivity_type,
  w.gke_config->>'master_ip_range' AS gke_master_ip_range
FROM databricks_account.provisioning.workspaces w
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

---
title: vw_encryption_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_encryption_keys
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

Creates, updates, deletes, gets or lists a <code>vw_encryption_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_encryption_keys" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.vw_encryption_keys" /></td></tr>
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
    <td><CopyableCode code="customer_managed_key_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the customer-managed key configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the key configuration was created.</td>
</tr>
<tr>
    <td><CopyableCode code="use_case" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Encryption use case this key is assigned to (one row per use case, e.g. MANAGED_SERVICES, STORAGE).</td>
</tr>
<tr>
    <td><CopyableCode code="aws_key_arn" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ARN of the AWS KMS key (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="aws_key_region" /></td>
    <td><CopyableCode code="string" /></td>
    <td>AWS region where the KMS key resides (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="aws_key_alias" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Alias of the AWS KMS key (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="aws_reuse_key_for_volumes" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether to reuse the same KMS key for cluster EBS volumes (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_key_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the Azure Key Vault key (Azure only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_key_vault_uri" /></td>
    <td><CopyableCode code="string" /></td>
    <td>URI of the Azure Key Vault containing the key (Azure only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_tenant_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Azure Active Directory tenant ID for the key vault (Azure only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_key_version" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Version of the Azure Key Vault key (Azure only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_disk_encryption_set_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Resource ID of the Azure Disk Encryption Set using this key (Azure only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_kms_key_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Resource ID of the GCP Cloud KMS key (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="cloud_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Derived cloud provider for this key configuration - one of AWS, AZURE, GCP, or UNKNOWN.</td>
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
  customer_managed_key_id,
  creation_time,
  use_case,
  aws_key_arn,
  aws_key_region,
  aws_key_alias,
  aws_reuse_key_for_volumes,
  azure_key_name,
  azure_key_vault_uri,
  azure_tenant_id,
  azure_key_version,
  azure_disk_encryption_set_id,
  gcp_kms_key_id,
  cloud_type
FROM databricks_account.provisioning.vw_encryption_keys
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
  k.account_id,
  k.customer_managed_key_id,
  k.creation_time,
  uc.value AS use_case,
  JSON_EXTRACT(k.aws_key_info, '$.key_arn') AS aws_key_arn,
  JSON_EXTRACT(k.aws_key_info, '$.key_region') AS aws_key_region,
  JSON_EXTRACT(k.aws_key_info, '$.key_alias') AS aws_key_alias,
  JSON_EXTRACT(k.aws_key_info, '$.reuse_key_for_cluster_volumes') AS aws_reuse_key_for_volumes,
  JSON_EXTRACT(k.azure_key_info, '$.key_name') AS azure_key_name,
  JSON_EXTRACT(k.azure_key_info, '$.key_vault_uri') AS azure_key_vault_uri,
  JSON_EXTRACT(k.azure_key_info, '$.tenant_id') AS azure_tenant_id,
  JSON_EXTRACT(k.azure_key_info, '$.version') AS azure_key_version,
  JSON_EXTRACT(k.azure_key_info, '$.disk_encryption_set_id') AS azure_disk_encryption_set_id,
  JSON_EXTRACT(k.gcp_key_info, '$.kms_key_id') AS gcp_kms_key_id,
  CASE
    WHEN k.aws_key_info IS NOT NULL THEN 'AWS'
    WHEN k.azure_key_info IS NOT NULL THEN 'AZURE'
    WHEN k.gcp_key_info IS NOT NULL THEN 'GCP'
    ELSE 'UNKNOWN'
  END AS cloud_type
FROM databricks_account.provisioning.encryption_keys k,
     JSON_EACH(k.use_cases) uc
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  k.account_id,
  k.customer_managed_key_id,
  k.creation_time,
  uc.value AS use_case,
  k.aws_key_info->>'key_arn' AS aws_key_arn,
  k.aws_key_info->>'key_region' AS aws_key_region,
  k.aws_key_info->>'key_alias' AS aws_key_alias,
  (k.aws_key_info->>'reuse_key_for_cluster_volumes')::boolean AS aws_reuse_key_for_volumes,
  k.azure_key_info->>'key_name' AS azure_key_name,
  k.azure_key_info->>'key_vault_uri' AS azure_key_vault_uri,
  k.azure_key_info->>'tenant_id' AS azure_tenant_id,
  k.azure_key_info->>'version' AS azure_key_version,
  k.azure_key_info->>'disk_encryption_set_id' AS azure_disk_encryption_set_id,
  k.gcp_key_info->>'kms_key_id' AS gcp_kms_key_id,
  CASE
    WHEN k.aws_key_info IS NOT NULL THEN 'AWS'
    WHEN k.azure_key_info IS NOT NULL THEN 'AZURE'
    WHEN k.gcp_key_info IS NOT NULL THEN 'GCP'
    ELSE 'UNKNOWN'
  END AS cloud_type
FROM databricks_account.provisioning.encryption_keys k,
     jsonb_array_elements(k.use_cases::jsonb) AS uc
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

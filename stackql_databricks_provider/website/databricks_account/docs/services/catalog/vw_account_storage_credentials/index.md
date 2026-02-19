---
title: vw_account_storage_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_account_storage_credentials
  - catalog
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

Creates, updates, deletes, gets or lists a <code>vw_account_storage_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_account_storage_credentials" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.catalog.vw_account_storage_credentials" /></td></tr>
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
    <td><CopyableCode code="metastore_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Metastore ID used to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the storage credential.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the storage credential.</td>
</tr>
<tr>
    <td><CopyableCode code="full_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Fully qualified name of the storage credential.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Username or group that owns the storage credential.</td>
</tr>
<tr>
    <td><CopyableCode code="read_only" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether the storage credential is restricted to read-only access.</td>
</tr>
<tr>
    <td><CopyableCode code="used_for_managed_storage" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether this credential is used for managed storage in the metastore.</td>
</tr>
<tr>
    <td><CopyableCode code="isolation_mode" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Isolation mode controlling which workspaces can use this credential.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the credential was created.</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Identity that created the storage credential.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the credential was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_by" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Identity that last updated the storage credential.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Optional free-text comment describing the storage credential.</td>
</tr>
<tr>
    <td><CopyableCode code="aws_role_arn" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ARN of the AWS IAM role used for credential (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="aws_external_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>External ID used when assuming the AWS IAM role (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="aws_unity_catalog_iam_arn" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ARN of the Unity Catalog IAM role for the AWS credential (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_access_connector_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Resource ID of the Azure Databricks Access Connector (Azure managed identity only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_credential_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Credential ID for the Azure managed identity (Azure managed identity only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_managed_identity_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the Azure managed identity (Azure managed identity only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_directory_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Azure Active Directory tenant ID for the service principal (Azure service principal only).</td>
</tr>
<tr>
    <td><CopyableCode code="azure_application_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Application (client) ID of the Azure service principal (Azure service principal only).</td>
</tr>
<tr>
    <td><CopyableCode code="cloudflare_access_key_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Access key ID for the Cloudflare API token credential (Cloudflare only).</td>
</tr>
<tr>
    <td><CopyableCode code="cloudflare_account_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Cloudflare account ID associated with the API token credential (Cloudflare only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_credential_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Credential ID for the Databricks GCP service account (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_service_account_email" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Email address of the Databricks-managed GCP service account (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="cloud_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Derived cloud provider type - one of AWS, AZURE_MANAGED_IDENTITY, AZURE_SERVICE_PRINCIPAL, CLOUDFLARE, GCP, or UNKNOWN.</td>
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
  sc.account_id,
  sc.metastore_id,
  sc.id,
  sc.name,
  sc.full_name,
  sc.owner,
  sc.read_only,
  sc.used_for_managed_storage,
  sc.isolation_mode,
  sc.created_at,
  sc.created_by,
  sc.updated_at,
  sc.updated_by,
  sc.comment,
  JSON_EXTRACT(sc.aws_iam_role, '$.role_arn') AS aws_role_arn,
  JSON_EXTRACT(sc.aws_iam_role, '$.external_id') AS aws_external_id,
  JSON_EXTRACT(sc.aws_iam_role, '$.unity_catalog_iam_arn') AS aws_unity_catalog_iam_arn,
  JSON_EXTRACT(sc.azure_managed_identity, '$.access_connector_id') AS azure_access_connector_id,
  JSON_EXTRACT(sc.azure_managed_identity, '$.credential_id') AS azure_credential_id,
  JSON_EXTRACT(sc.azure_managed_identity, '$.managed_identity_id') AS azure_managed_identity_id,
  JSON_EXTRACT(sc.azure_service_principal, '$.directory_id') AS azure_directory_id,
  JSON_EXTRACT(sc.azure_service_principal, '$.application_id') AS azure_application_id,
  JSON_EXTRACT(sc.cloudflare_api_token, '$.access_key_id') AS cloudflare_access_key_id,
  JSON_EXTRACT(sc.cloudflare_api_token, '$.account_id') AS cloudflare_account_id,
  JSON_EXTRACT(sc.databricks_gcp_service_account, '$.credential_id') AS gcp_credential_id,
  JSON_EXTRACT(sc.databricks_gcp_service_account, '$.email') AS gcp_service_account_email,
  CASE
    WHEN sc.aws_iam_role IS NOT NULL THEN 'AWS'
    WHEN sc.azure_managed_identity IS NOT NULL THEN 'AZURE_MANAGED_IDENTITY'
    WHEN sc.azure_service_principal IS NOT NULL THEN 'AZURE_SERVICE_PRINCIPAL'
    WHEN sc.cloudflare_api_token IS NOT NULL THEN 'CLOUDFLARE'
    WHEN sc.databricks_gcp_service_account IS NOT NULL THEN 'GCP'
    ELSE 'UNKNOWN'
  END AS cloud_type
FROM databricks_account.catalog.account_storage_credentials sc
WHERE account_id = '{{ account_id }}'
AND metastore_id = '{{ metastore_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  sc.account_id,
  sc.metastore_id,
  sc.id,
  sc.name,
  sc.full_name,
  sc.owner,
  sc.read_only,
  sc.used_for_managed_storage,
  sc.isolation_mode,
  sc.created_at,
  sc.created_by,
  sc.updated_at,
  sc.updated_by,
  sc.comment,
  sc.aws_iam_role->>'role_arn' AS aws_role_arn,
  sc.aws_iam_role->>'external_id' AS aws_external_id,
  sc.aws_iam_role->>'unity_catalog_iam_arn' AS aws_unity_catalog_iam_arn,
  sc.azure_managed_identity->>'access_connector_id' AS azure_access_connector_id,
  sc.azure_managed_identity->>'credential_id' AS azure_credential_id,
  sc.azure_managed_identity->>'managed_identity_id' AS azure_managed_identity_id,
  sc.azure_service_principal->>'directory_id' AS azure_directory_id,
  sc.azure_service_principal->>'application_id' AS azure_application_id,
  sc.cloudflare_api_token->>'access_key_id' AS cloudflare_access_key_id,
  sc.cloudflare_api_token->>'account_id' AS cloudflare_account_id,
  sc.databricks_gcp_service_account->>'credential_id' AS gcp_credential_id,
  sc.databricks_gcp_service_account->>'email' AS gcp_service_account_email,
  CASE
    WHEN sc.aws_iam_role IS NOT NULL THEN 'AWS'
    WHEN sc.azure_managed_identity IS NOT NULL THEN 'AZURE_MANAGED_IDENTITY'
    WHEN sc.azure_service_principal IS NOT NULL THEN 'AZURE_SERVICE_PRINCIPAL'
    WHEN sc.cloudflare_api_token IS NOT NULL THEN 'CLOUDFLARE'
    WHEN sc.databricks_gcp_service_account IS NOT NULL THEN 'GCP'
    ELSE 'UNKNOWN'
  END AS cloud_type
FROM databricks_account.catalog.account_storage_credentials sc
WHERE account_id = '{{ account_id }}'
AND metastore_id = '{{ metastore_id }}'
```

</TabItem>
</Tabs>

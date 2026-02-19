---
title: account_storage_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - account_storage_credentials
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

Creates, updates, deletes, gets or lists an <code>account_storage_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="account_storage_credentials" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.catalog.account_storage_credentials" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="account_storage_credentials_get"
    values={[
        { label: 'account_storage_credentials_get', value: 'account_storage_credentials_get' },
        { label: 'account_storage_credentials_list', value: 'account_storage_credentials_list' }
    ]}
>
<TabItem value="account_storage_credentials_get">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "The unique identifier of the credential."
  },
  {
    "name": "name",
    "type": "string",
    "description": "The credential name. The name must be unique among storage and service credentials within the metastore."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of the parent metastore."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "The full name of the credential."
  },
  {
    "name": "aws_iam_role",
    "type": "object",
    "description": "The AWS IAM role configuration",
    "children": [
      {
        "name": "role_arn",
        "type": "string",
        "description": "The Amazon Resource Name (ARN) of the AWS IAM role used to vend temporary credentials."
      },
      {
        "name": "external_id",
        "type": "string",
        "description": "The external ID used in role assumption to prevent the confused deputy problem."
      },
      {
        "name": "unity_catalog_iam_arn",
        "type": "string",
        "description": "The Amazon Resource Name (ARN) of the AWS IAM user managed by Databricks. This is the identity that is going to assume the AWS IAM role."
      }
    ]
  },
  {
    "name": "azure_managed_identity",
    "type": "object",
    "description": "The Azure managed identity configuration.",
    "children": [
      {
        "name": "access_connector_id",
        "type": "string",
        "description": "The Azure resource ID of the Azure Databricks Access Connector. Use the format `/subscriptions/&#123;guid&#125;/resourceGroups/&#123;rg-name&#125;/providers/Microsoft.Databricks/accessConnectors/&#123;connector-name&#125;`."
      },
      {
        "name": "credential_id",
        "type": "string",
        "description": "The Databricks internal ID that represents this managed identity."
      },
      {
        "name": "managed_identity_id",
        "type": "string",
        "description": "The Azure resource ID of the managed identity. Use the format, `/subscriptions/&#123;guid&#125;/resourceGroups/&#123;rg-name&#125;/providers/Microsoft.ManagedIdentity/userAssignedIdentities/&#123;identity-name&#125;` This is only available for user-assgined identities. For system-assigned identities, the access_connector_id is used to identify the identity. If this field is not provided, then we assume the AzureManagedIdentity is using the system-assigned identity."
      }
    ]
  },
  {
    "name": "azure_service_principal",
    "type": "object",
    "description": "The Azure service principal configuration.",
    "children": [
      {
        "name": "directory_id",
        "type": "string",
        "description": "The directory ID corresponding to the Azure Active Directory (AAD) tenant of the application."
      },
      {
        "name": "application_id",
        "type": "string",
        "description": "The application ID of the application registration within the referenced AAD tenant."
      },
      {
        "name": "client_secret",
        "type": "string",
        "description": "The client secret generated for the above app ID in AAD."
      }
    ]
  },
  {
    "name": "cloudflare_api_token",
    "type": "object",
    "description": "The Cloudflare API token configuration.",
    "children": [
      {
        "name": "access_key_id",
        "type": "string",
        "description": "The access key ID associated with the API token."
      },
      {
        "name": "secret_access_key",
        "type": "string",
        "description": "The secret access token generated for the above access key ID."
      },
      {
        "name": "account_id",
        "type": "string",
        "description": "The ID of the account associated with the API token."
      }
    ]
  },
  {
    "name": "comment",
    "type": "string",
    "description": "Comment associated with the credential."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this credential was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of credential creator."
  },
  {
    "name": "databricks_gcp_service_account",
    "type": "object",
    "description": "The Databricks managed GCP service account configuration.",
    "children": [
      {
        "name": "credential_id",
        "type": "string",
        "description": "The Databricks internal ID that represents this managed identity."
      },
      {
        "name": "email",
        "type": "string",
        "description": "The email of the service account."
      }
    ]
  },
  {
    "name": "isolation_mode",
    "type": "string",
    "description": "Whether the current securable is accessible from all workspaces or a specific set of workspaces. (ISOLATION_MODE_ISOLATED, ISOLATION_MODE_OPEN)"
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of credential."
  },
  {
    "name": "read_only",
    "type": "boolean",
    "description": "Whether the credential is usable only for read operations. Only applicable when purpose is **STORAGE**."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this credential was last modified, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified the credential."
  },
  {
    "name": "used_for_managed_storage",
    "type": "boolean",
    "description": "Whether this credential is the current metastore's root storage credential. Only applicable when purpose is **STORAGE**."
  }
]} />
</TabItem>
<TabItem value="account_storage_credentials_list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "The unique identifier of the credential."
  },
  {
    "name": "name",
    "type": "string",
    "description": "The credential name. The name must be unique among storage and service credentials within the metastore."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of the parent metastore."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "The full name of the credential."
  },
  {
    "name": "aws_iam_role",
    "type": "object",
    "description": "The AWS IAM role configuration",
    "children": [
      {
        "name": "role_arn",
        "type": "string",
        "description": "The Amazon Resource Name (ARN) of the AWS IAM role used to vend temporary credentials."
      },
      {
        "name": "external_id",
        "type": "string",
        "description": "The external ID used in role assumption to prevent the confused deputy problem."
      },
      {
        "name": "unity_catalog_iam_arn",
        "type": "string",
        "description": "The Amazon Resource Name (ARN) of the AWS IAM user managed by Databricks. This is the identity that is going to assume the AWS IAM role."
      }
    ]
  },
  {
    "name": "azure_managed_identity",
    "type": "object",
    "description": "The Azure managed identity configuration.",
    "children": [
      {
        "name": "access_connector_id",
        "type": "string",
        "description": "The Azure resource ID of the Azure Databricks Access Connector. Use the format `/subscriptions/&#123;guid&#125;/resourceGroups/&#123;rg-name&#125;/providers/Microsoft.Databricks/accessConnectors/&#123;connector-name&#125;`."
      },
      {
        "name": "credential_id",
        "type": "string",
        "description": "The Databricks internal ID that represents this managed identity."
      },
      {
        "name": "managed_identity_id",
        "type": "string",
        "description": "The Azure resource ID of the managed identity. Use the format, `/subscriptions/&#123;guid&#125;/resourceGroups/&#123;rg-name&#125;/providers/Microsoft.ManagedIdentity/userAssignedIdentities/&#123;identity-name&#125;` This is only available for user-assgined identities. For system-assigned identities, the access_connector_id is used to identify the identity. If this field is not provided, then we assume the AzureManagedIdentity is using the system-assigned identity."
      }
    ]
  },
  {
    "name": "azure_service_principal",
    "type": "object",
    "description": "The Azure service principal configuration.",
    "children": [
      {
        "name": "directory_id",
        "type": "string",
        "description": "The directory ID corresponding to the Azure Active Directory (AAD) tenant of the application."
      },
      {
        "name": "application_id",
        "type": "string",
        "description": "The application ID of the application registration within the referenced AAD tenant."
      },
      {
        "name": "client_secret",
        "type": "string",
        "description": "The client secret generated for the above app ID in AAD."
      }
    ]
  },
  {
    "name": "cloudflare_api_token",
    "type": "object",
    "description": "The Cloudflare API token configuration.",
    "children": [
      {
        "name": "access_key_id",
        "type": "string",
        "description": "The access key ID associated with the API token."
      },
      {
        "name": "secret_access_key",
        "type": "string",
        "description": "The secret access token generated for the above access key ID."
      },
      {
        "name": "account_id",
        "type": "string",
        "description": "The ID of the account associated with the API token."
      }
    ]
  },
  {
    "name": "comment",
    "type": "string",
    "description": "Comment associated with the credential."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this credential was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of credential creator."
  },
  {
    "name": "databricks_gcp_service_account",
    "type": "object",
    "description": "The Databricks managed GCP service account configuration.",
    "children": [
      {
        "name": "credential_id",
        "type": "string",
        "description": "The Databricks internal ID that represents this managed identity."
      },
      {
        "name": "email",
        "type": "string",
        "description": "The email of the service account."
      }
    ]
  },
  {
    "name": "isolation_mode",
    "type": "string",
    "description": "Whether the current securable is accessible from all workspaces or a specific set of workspaces. (ISOLATION_MODE_ISOLATED, ISOLATION_MODE_OPEN)"
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of credential."
  },
  {
    "name": "read_only",
    "type": "boolean",
    "description": "Whether the credential is usable only for read operations. Only applicable when purpose is **STORAGE**."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this credential was last modified, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified the credential."
  },
  {
    "name": "used_for_managed_storage",
    "type": "boolean",
    "description": "Whether this credential is the current metastore's root storage credential. Only applicable when purpose is **STORAGE**."
  }
]} />
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#account_storage_credentials_get"><CopyableCode code="account_storage_credentials_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a>, <a href="#parameter-storage_credential_name"><code>storage_credential_name</code></a></td>
    <td></td>
    <td>Gets a storage credential from the metastore. The caller must be a metastore admin, the owner of the</td>
</tr>
<tr>
    <td><a href="#account_storage_credentials_list"><CopyableCode code="account_storage_credentials_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a></td>
    <td></td>
    <td>Gets a list of all storage credentials that have been assigned to given metastore.</td>
</tr>
<tr>
    <td><a href="#account_storage_credentials_create"><CopyableCode code="account_storage_credentials_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a></td>
    <td></td>
    <td>Creates a new storage credential. The request object is specific to the cloud: - **AwsIamRole** for</td>
</tr>
<tr>
    <td><a href="#account_storage_credentials_update"><CopyableCode code="account_storage_credentials_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a>, <a href="#parameter-storage_credential_name"><code>storage_credential_name</code></a></td>
    <td></td>
    <td>Updates a storage credential on the metastore. The caller must be the owner of the storage credential.</td>
</tr>
<tr>
    <td><a href="#account_storage_credentials_delete"><CopyableCode code="account_storage_credentials_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a>, <a href="#parameter-storage_credential_name"><code>storage_credential_name</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes a storage credential from the metastore. The caller must be an owner of the storage</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-metastore_id">
    <td><CopyableCode code="metastore_id" /></td>
    <td><code>string</code></td>
    <td>Unity Catalog metastore ID</td>
</tr>
<tr id="parameter-storage_credential_name">
    <td><CopyableCode code="storage_credential_name" /></td>
    <td><code>string</code></td>
    <td>Name of the storage credential.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>string</code></td>
    <td>Force deletion even if the Storage Credential is not empty. Default is false.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="account_storage_credentials_get"
    values={[
        { label: 'account_storage_credentials_get', value: 'account_storage_credentials_get' },
        { label: 'account_storage_credentials_list', value: 'account_storage_credentials_list' }
    ]}
>
<TabItem value="account_storage_credentials_get">

Gets a storage credential from the metastore. The caller must be a metastore admin, the owner of the

```sql
SELECT
id,
name,
metastore_id,
full_name,
aws_iam_role,
azure_managed_identity,
azure_service_principal,
cloudflare_api_token,
comment,
created_at,
created_by,
databricks_gcp_service_account,
isolation_mode,
owner,
read_only,
updated_at,
updated_by,
used_for_managed_storage
FROM databricks_account.catalog.account_storage_credentials
WHERE account_id = '{{ account_id }}' -- required
AND metastore_id = '{{ metastore_id }}' -- required
AND storage_credential_name = '{{ storage_credential_name }}' -- required
;
```
</TabItem>
<TabItem value="account_storage_credentials_list">

Gets a list of all storage credentials that have been assigned to given metastore.

```sql
SELECT
id,
name,
metastore_id,
full_name,
aws_iam_role,
azure_managed_identity,
azure_service_principal,
cloudflare_api_token,
comment,
created_at,
created_by,
databricks_gcp_service_account,
isolation_mode,
owner,
read_only,
updated_at,
updated_by,
used_for_managed_storage
FROM databricks_account.catalog.account_storage_credentials
WHERE account_id = '{{ account_id }}' -- required
AND metastore_id = '{{ metastore_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="account_storage_credentials_create"
    values={[
        { label: 'account_storage_credentials_create', value: 'account_storage_credentials_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="account_storage_credentials_create">

Creates a new storage credential. The request object is specific to the cloud: - **AwsIamRole** for

```sql
INSERT INTO databricks_account.catalog.account_storage_credentials (
credential_info,
skip_validation,
account_id,
metastore_id
)
SELECT 
'{{ credential_info }}',
'{{ skip_validation }}',
'{{ account_id }}',
'{{ metastore_id }}'
RETURNING
credential_info
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: account_storage_credentials
  props:
    - name: account_id
      value: string
      description: Required parameter for the account_storage_credentials resource.
    - name: metastore_id
      value: string
      description: Required parameter for the account_storage_credentials resource.
    - name: credential_info
      value: string
      description: |
        :param skip_validation: bool (optional) Optional, default false. Supplying true to this argument skips validation of the created set of credentials.
    - name: skip_validation
      value: string
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="account_storage_credentials_update"
    values={[
        { label: 'account_storage_credentials_update', value: 'account_storage_credentials_update' }
    ]}
>
<TabItem value="account_storage_credentials_update">

Updates a storage credential on the metastore. The caller must be the owner of the storage credential.

```sql
REPLACE databricks_account.catalog.account_storage_credentials
SET 
credential_info = '{{ credential_info }}',
skip_validation = '{{ skip_validation }}'
WHERE 
account_id = '{{ account_id }}' --required
AND metastore_id = '{{ metastore_id }}' --required
AND storage_credential_name = '{{ storage_credential_name }}' --required
RETURNING
credential_info;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="account_storage_credentials_delete"
    values={[
        { label: 'account_storage_credentials_delete', value: 'account_storage_credentials_delete' }
    ]}
>
<TabItem value="account_storage_credentials_delete">

Deletes a storage credential from the metastore. The caller must be an owner of the storage

```sql
DELETE FROM databricks_account.catalog.account_storage_credentials
WHERE account_id = '{{ account_id }}' --required
AND metastore_id = '{{ metastore_id }}' --required
AND storage_credential_name = '{{ storage_credential_name }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>

---
title: credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - credentials
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

Creates, updates, deletes, gets or lists a <code>credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="credentials" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.catalog.credentials" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_credential"
    values={[
        { label: 'get_credential', value: 'get_credential' },
        { label: 'list_credentials', value: 'list_credentials' }
    ]}
>
<TabItem value="get_credential">

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
        "name": "external_id",
        "type": "string",
        "description": "The external ID used in role assumption to prevent the confused deputy problem."
      },
      {
        "name": "role_arn",
        "type": "string",
        "description": "The Amazon Resource Name (ARN) of the AWS IAM role used to vend temporary credentials."
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
      },
      {
        "name": "private_key_id",
        "type": "string",
        "description": "The ID that represents the private key for this Service Account"
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
    "name": "purpose",
    "type": "string",
    "description": "Indicates the purpose of the credential. (SERVICE, STORAGE)"
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
<TabItem value="list_credentials">

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
        "name": "external_id",
        "type": "string",
        "description": "The external ID used in role assumption to prevent the confused deputy problem."
      },
      {
        "name": "role_arn",
        "type": "string",
        "description": "The Amazon Resource Name (ARN) of the AWS IAM role used to vend temporary credentials."
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
      },
      {
        "name": "private_key_id",
        "type": "string",
        "description": "The ID that represents the private key for this Service Account"
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
    "name": "purpose",
    "type": "string",
    "description": "Indicates the purpose of the credential. (SERVICE, STORAGE)"
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
    <td><a href="#get_credential"><CopyableCode code="get_credential" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name_arg"><code>name_arg</code></a></td>
    <td></td>
    <td>Gets a service or storage credential from the metastore. The caller must be a metastore admin, the</td>
</tr>
<tr>
    <td><a href="#list_credentials"><CopyableCode code="list_credentials" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-include_unbound"><code>include_unbound</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-purpose"><code>purpose</code></a></td>
    <td>Gets an array of credentials (as __CredentialInfo__ objects).</td>
</tr>
<tr>
    <td><a href="#create_credential"><CopyableCode code="create_credential" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates a new credential. The type of credential to be created is determined by the **purpose** field,</td>
</tr>
<tr>
    <td><a href="#credentials_generate_temporary_service_credential"><CopyableCode code="credentials_generate_temporary_service_credential" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-credential_name"><code>credential_name</code></a></td>
    <td></td>
    <td>Returns a set of temporary credentials generated using the specified service credential. The caller</td>
</tr>
<tr>
    <td><a href="#credentials_validate_credential"><CopyableCode code="credentials_validate_credential" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Validates a credential.</td>
</tr>
<tr>
    <td><a href="#update_credential"><CopyableCode code="update_credential" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name_arg"><code>name_arg</code></a></td>
    <td></td>
    <td>Updates a service or storage credential on the metastore.</td>
</tr>
<tr>
    <td><a href="#delete_credential"><CopyableCode code="delete_credential" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name_arg"><code>name_arg</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes a service or storage credential from the metastore. The caller must be an owner of the</td>
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
<tr id="parameter-name_arg">
    <td><CopyableCode code="name_arg" /></td>
    <td><code>string</code></td>
    <td>Name of the credential.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>string</code></td>
    <td>Force an update even if there are dependent services (when purpose is **SERVICE**) or dependent external locations and external tables (when purpose is **STORAGE**).</td>
</tr>
<tr id="parameter-include_unbound">
    <td><CopyableCode code="include_unbound" /></td>
    <td><code>string</code></td>
    <td>Whether to include credentials not bound to the workspace. Effective only if the user has permission to update the credential–workspace binding.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of credentials to return. - If not set, the default max page size is used. - When set to a value greater than 0, the page length is the minimum of this value and a server-configured value. - When set to 0, the page length is set to a server-configured value (recommended). - When set to a value less than 0, an invalid parameter error is returned.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque token to retrieve the next page of results.</td>
</tr>
<tr id="parameter-purpose">
    <td><CopyableCode code="purpose" /></td>
    <td><code>string</code></td>
    <td>Return only credentials for the specified purpose.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_credential"
    values={[
        { label: 'get_credential', value: 'get_credential' },
        { label: 'list_credentials', value: 'list_credentials' }
    ]}
>
<TabItem value="get_credential">

Gets a service or storage credential from the metastore. The caller must be a metastore admin, the

```sql
SELECT
id,
name,
metastore_id,
full_name,
aws_iam_role,
azure_managed_identity,
azure_service_principal,
comment,
created_at,
created_by,
databricks_gcp_service_account,
isolation_mode,
owner,
purpose,
read_only,
updated_at,
updated_by,
used_for_managed_storage
FROM databricks_account.catalog.credentials
WHERE name_arg = '{{ name_arg }}' -- required
;
```
</TabItem>
<TabItem value="list_credentials">

Gets an array of credentials (as __CredentialInfo__ objects).

```sql
SELECT
id,
name,
metastore_id,
full_name,
aws_iam_role,
azure_managed_identity,
azure_service_principal,
comment,
created_at,
created_by,
databricks_gcp_service_account,
isolation_mode,
owner,
purpose,
read_only,
updated_at,
updated_by,
used_for_managed_storage
FROM databricks_account.catalog.credentials
WHERE include_unbound = '{{ include_unbound }}'
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
AND purpose = '{{ purpose }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_credential"
    values={[
        { label: 'create_credential', value: 'create_credential' },
        { label: 'credentials_generate_temporary_service_credential', value: 'credentials_generate_temporary_service_credential' },
        { label: 'credentials_validate_credential', value: 'credentials_validate_credential' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_credential">

Creates a new credential. The type of credential to be created is determined by the **purpose** field,

```sql
INSERT INTO databricks_account.catalog.credentials (
name,
aws_iam_role,
azure_managed_identity,
azure_service_principal,
comment,
databricks_gcp_service_account,
purpose,
read_only,
skip_validation
)
SELECT 
'{{ name }}' /* required */,
'{{ aws_iam_role }}',
'{{ azure_managed_identity }}',
'{{ azure_service_principal }}',
'{{ comment }}',
'{{ databricks_gcp_service_account }}',
'{{ purpose }}',
'{{ read_only }}',
'{{ skip_validation }}'
RETURNING
id,
name,
metastore_id,
full_name,
aws_iam_role,
azure_managed_identity,
azure_service_principal,
comment,
created_at,
created_by,
databricks_gcp_service_account,
isolation_mode,
owner,
purpose,
read_only,
updated_at,
updated_by,
used_for_managed_storage
;
```
</TabItem>
<TabItem value="credentials_generate_temporary_service_credential">

Returns a set of temporary credentials generated using the specified service credential. The caller

```sql
INSERT INTO databricks_account.catalog.credentials (
credential_name,
azure_options,
gcp_options
)
SELECT 
'{{ credential_name }}' /* required */,
'{{ azure_options }}',
'{{ gcp_options }}'
RETURNING
aws_temp_credentials,
azure_aad,
expiration_time,
gcp_oauth_token
;
```
</TabItem>
<TabItem value="credentials_validate_credential">

Validates a credential.

```sql
INSERT INTO databricks_account.catalog.credentials (
aws_iam_role,
azure_managed_identity,
credential_name,
databricks_gcp_service_account,
external_location_name,
purpose,
read_only,
url
)
SELECT 
'{{ aws_iam_role }}',
'{{ azure_managed_identity }}',
'{{ credential_name }}',
'{{ databricks_gcp_service_account }}',
'{{ external_location_name }}',
'{{ purpose }}',
'{{ read_only }}',
'{{ url }}'
RETURNING
isDir,
results
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: credentials
  props:
    - name: name
      value: string
      description: |
        The credential name. The name must be unique among storage and service credentials within the metastore.
    - name: aws_iam_role
      value: string
      description: |
        :param azure_managed_identity: :class:`AzureManagedIdentity` (optional)
    - name: azure_managed_identity
      value: string
    - name: azure_service_principal
      value: string
      description: |
        The Azure service principal configuration.
    - name: comment
      value: string
      description: |
        Comment associated with the credential.
    - name: databricks_gcp_service_account
      value: string
      description: |
        :param external_location_name: str (optional) The name of an existing external location to validate. Only applicable for storage credentials (purpose is **STORAGE**.)
    - name: purpose
      value: string
      description: |
        The purpose of the credential. This should only be used when the credential is specified.
    - name: read_only
      value: string
      description: |
        Whether the credential is only usable for read operations. Only applicable for storage credentials (purpose is **STORAGE**.)
    - name: skip_validation
      value: string
      description: |
        Optional. Supplying true to this argument skips validation of the created set of credentials.
    - name: credential_name
      value: string
      description: |
        Required. The name of an existing credential or long-lived cloud credential to validate.
    - name: azure_options
      value: string
      description: |
        :param gcp_options: :class:`GenerateTemporaryServiceCredentialGcpOptions` (optional)
    - name: gcp_options
      value: string
    - name: external_location_name
      value: string
    - name: url
      value: string
      description: |
        The external location url to validate. Only applicable when purpose is **STORAGE**.
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_credential"
    values={[
        { label: 'update_credential', value: 'update_credential' }
    ]}
>
<TabItem value="update_credential">

Updates a service or storage credential on the metastore.

```sql
UPDATE databricks_account.catalog.credentials
SET 
aws_iam_role = '{{ aws_iam_role }}',
azure_managed_identity = '{{ azure_managed_identity }}',
azure_service_principal = '{{ azure_service_principal }}',
comment = '{{ comment }}',
databricks_gcp_service_account = '{{ databricks_gcp_service_account }}',
force = '{{ force }}',
isolation_mode = '{{ isolation_mode }}',
new_name = '{{ new_name }}',
owner = '{{ owner }}',
read_only = '{{ read_only }}',
skip_validation = '{{ skip_validation }}'
WHERE 
name_arg = '{{ name_arg }}' --required
RETURNING
id,
name,
metastore_id,
full_name,
aws_iam_role,
azure_managed_identity,
azure_service_principal,
comment,
created_at,
created_by,
databricks_gcp_service_account,
isolation_mode,
owner,
purpose,
read_only,
updated_at,
updated_by,
used_for_managed_storage;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_credential"
    values={[
        { label: 'delete_credential', value: 'delete_credential' }
    ]}
>
<TabItem value="delete_credential">

Deletes a service or storage credential from the metastore. The caller must be an owner of the

```sql
DELETE FROM databricks_account.catalog.credentials
WHERE name_arg = '{{ name_arg }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>

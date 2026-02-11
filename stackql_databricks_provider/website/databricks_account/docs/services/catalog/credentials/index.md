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
<tr><td><b>Name</b></td><td><code>credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.catalog.credentials" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

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
    "description": "Whether the current securable is accessible from all workspaces or a specific set of workspaces."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of credential."
  },
  {
    "name": "purpose",
    "type": "string",
    "description": "Indicates the purpose of the credential."
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
<TabItem value="list">

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
    "description": "Whether the current securable is accessible from all workspaces or a specific set of workspaces."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of credential."
  },
  {
    "name": "purpose",
    "type": "string",
    "description": "Indicates the purpose of the credential."
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name_arg"><code>name_arg</code></a></td>
    <td></td>
    <td>Gets a service or storage credential from the metastore. The caller must be a metastore admin, the<br />owner of the credential, or have any permission on the credential.<br /><br />:param name_arg: str<br />  Name of the credential.<br /><br />:returns: :class:`CredentialInfo`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-include_unbound"><code>include_unbound</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-purpose"><code>purpose</code></a></td>
    <td>Gets an array of credentials (as __CredentialInfo__ objects).<br /><br />The array is limited to only the credentials that the caller has permission to access. If the caller<br />is a metastore admin, retrieval of credentials is unrestricted. There is no guarantee of a specific<br />ordering of the elements in the array.<br /><br />PAGINATION BEHAVIOR: The API is by default paginated, a page may contain zero results while still<br />providing a next_page_token. Clients must continue reading pages until next_page_token is absent,<br />which is the only indication that the end of results has been reached.<br /><br />:param include_unbound: bool (optional)<br />  Whether to include credentials not bound to the workspace. Effective only if the user has permission<br />  to update the credential–workspace binding.<br />:param max_results: int (optional)<br />  Maximum number of credentials to return. - If not set, the default max page size is used. - When set<br />  to a value greater than 0, the page length is the minimum of this value and a server-configured<br />  value. - When set to 0, the page length is set to a server-configured value (recommended). - When<br />  set to a value less than 0, an invalid parameter error is returned.<br />:param page_token: str (optional)<br />  Opaque token to retrieve the next page of results.<br />:param purpose: :class:`CredentialPurpose` (optional)<br />  Return only credentials for the specified purpose.<br /><br />:returns: Iterator over :class:`CredentialInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__name"><code>data__name</code></a></td>
    <td></td>
    <td>Creates a new credential. The type of credential to be created is determined by the **purpose** field,<br />which should be either **SERVICE** or **STORAGE**.<br /><br />The caller must be a metastore admin or have the metastore privilege **CREATE_STORAGE_CREDENTIAL** for<br />storage credentials, or **CREATE_SERVICE_CREDENTIAL** for service credentials.<br /><br />:param name: str<br />  The credential name. The name must be unique among storage and service credentials within the<br />  metastore.<br />:param aws_iam_role: :class:`AwsIamRole` (optional)<br />  The AWS IAM role configuration.<br />:param azure_managed_identity: :class:`AzureManagedIdentity` (optional)<br />  The Azure managed identity configuration.<br />:param azure_service_principal: :class:`AzureServicePrincipal` (optional)<br />  The Azure service principal configuration.<br />:param comment: str (optional)<br />  Comment associated with the credential.<br />:param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccount` (optional)<br />  The Databricks managed GCP service account configuration.<br />:param purpose: :class:`CredentialPurpose` (optional)<br />  Indicates the purpose of the credential.<br />:param read_only: bool (optional)<br />  Whether the credential is usable only for read operations. Only applicable when purpose is<br />  **STORAGE**.<br />:param skip_validation: bool (optional)<br />  Optional. Supplying true to this argument skips validation of the created set of credentials.<br /><br />:returns: :class:`CredentialInfo`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name_arg"><code>name_arg</code></a></td>
    <td></td>
    <td>Updates a service or storage credential on the metastore.<br /><br />The caller must be the owner of the credential or a metastore admin or have the `MANAGE` permission.<br />If the caller is a metastore admin, only the __owner__ field can be changed.<br /><br />:param name_arg: str<br />  Name of the credential.<br />:param aws_iam_role: :class:`AwsIamRole` (optional)<br />  The AWS IAM role configuration.<br />:param azure_managed_identity: :class:`AzureManagedIdentity` (optional)<br />  The Azure managed identity configuration.<br />:param azure_service_principal: :class:`AzureServicePrincipal` (optional)<br />  The Azure service principal configuration.<br />:param comment: str (optional)<br />  Comment associated with the credential.<br />:param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccount` (optional)<br />  The Databricks managed GCP service account configuration.<br />:param force: bool (optional)<br />  Force an update even if there are dependent services (when purpose is **SERVICE**) or dependent<br />  external locations and external tables (when purpose is **STORAGE**).<br />:param isolation_mode: :class:`IsolationMode` (optional)<br />  Whether the current securable is accessible from all workspaces or a specific set of workspaces.<br />:param new_name: str (optional)<br />  New name of credential.<br />:param owner: str (optional)<br />  Username of current owner of credential.<br />:param read_only: bool (optional)<br />  Whether the credential is usable only for read operations. Only applicable when purpose is<br />  **STORAGE**.<br />:param skip_validation: bool (optional)<br />  Supply true to this argument to skip validation of the updated credential.<br /><br />:returns: :class:`CredentialInfo`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name_arg"><code>name_arg</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes a service or storage credential from the metastore. The caller must be an owner of the<br />credential.<br /><br />:param name_arg: str<br />  Name of the credential.<br />:param force: bool (optional)<br />  Force an update even if there are dependent services (when purpose is **SERVICE**) or dependent<br />  external locations and external tables (when purpose is **STORAGE**).</td>
</tr>
<tr>
    <td><a href="#generate_temporary_service_credential"><CopyableCode code="generate_temporary_service_credential" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-credential_name"><code>credential_name</code></a></td>
    <td></td>
    <td>Returns a set of temporary credentials generated using the specified service credential. The caller<br />must be a metastore admin or have the metastore privilege **ACCESS** on the service credential.<br /><br />:param credential_name: str<br />  The name of the service credential used to generate a temporary credential<br />:param azure_options: :class:`GenerateTemporaryServiceCredentialAzureOptions` (optional)<br />:param gcp_options: :class:`GenerateTemporaryServiceCredentialGcpOptions` (optional)<br /><br />:returns: :class:`TemporaryCredentials`</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Validates a credential.<br /><br />For service credentials (purpose is **SERVICE**), either the __credential_name__ or the cloud-specific<br />credential must be provided.<br /><br />For storage credentials (purpose is **STORAGE**), at least one of __external_location_name__ and<br />__url__ need to be provided. If only one of them is provided, it will be used for validation. And if<br />both are provided, the __url__ will be used for validation, and __external_location_name__ will be<br />ignored when checking overlapping urls. Either the __credential_name__ or the cloud-specific<br />credential must be provided.<br /><br />The caller must be a metastore admin or the credential owner or have the required permission on the<br />metastore and the credential (e.g., **CREATE_EXTERNAL_LOCATION** when purpose is **STORAGE**).<br /><br />:param aws_iam_role: :class:`AwsIamRole` (optional)<br />:param azure_managed_identity: :class:`AzureManagedIdentity` (optional)<br />:param credential_name: str (optional)<br />  Required. The name of an existing credential or long-lived cloud credential to validate.<br />:param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccount` (optional)<br />:param external_location_name: str (optional)<br />  The name of an existing external location to validate. Only applicable for storage credentials<br />  (purpose is **STORAGE**.)<br />:param purpose: :class:`CredentialPurpose` (optional)<br />  The purpose of the credential. This should only be used when the credential is specified.<br />:param read_only: bool (optional)<br />  Whether the credential is only usable for read operations. Only applicable for storage credentials<br />  (purpose is **STORAGE**.)<br />:param url: str (optional)<br />  The external location url to validate. Only applicable when purpose is **STORAGE**.<br /><br />:returns: :class:`ValidateCredentialResponse`</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a service or storage credential from the metastore. The caller must be a metastore admin, the<br />owner of the credential, or have any permission on the credential.<br /><br />:param name_arg: str<br />  Name of the credential.<br /><br />:returns: :class:`CredentialInfo`

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
<TabItem value="list">

Gets an array of credentials (as __CredentialInfo__ objects).<br /><br />The array is limited to only the credentials that the caller has permission to access. If the caller<br />is a metastore admin, retrieval of credentials is unrestricted. There is no guarantee of a specific<br />ordering of the elements in the array.<br /><br />PAGINATION BEHAVIOR: The API is by default paginated, a page may contain zero results while still<br />providing a next_page_token. Clients must continue reading pages until next_page_token is absent,<br />which is the only indication that the end of results has been reached.<br /><br />:param include_unbound: bool (optional)<br />  Whether to include credentials not bound to the workspace. Effective only if the user has permission<br />  to update the credential–workspace binding.<br />:param max_results: int (optional)<br />  Maximum number of credentials to return. - If not set, the default max page size is used. - When set<br />  to a value greater than 0, the page length is the minimum of this value and a server-configured<br />  value. - When set to 0, the page length is set to a server-configured value (recommended). - When<br />  set to a value less than 0, an invalid parameter error is returned.<br />:param page_token: str (optional)<br />  Opaque token to retrieve the next page of results.<br />:param purpose: :class:`CredentialPurpose` (optional)<br />  Return only credentials for the specified purpose.<br /><br />:returns: Iterator over :class:`CredentialInfo`

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
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a new credential. The type of credential to be created is determined by the **purpose** field,<br />which should be either **SERVICE** or **STORAGE**.<br /><br />The caller must be a metastore admin or have the metastore privilege **CREATE_STORAGE_CREDENTIAL** for<br />storage credentials, or **CREATE_SERVICE_CREDENTIAL** for service credentials.<br /><br />:param name: str<br />  The credential name. The name must be unique among storage and service credentials within the<br />  metastore.<br />:param aws_iam_role: :class:`AwsIamRole` (optional)<br />  The AWS IAM role configuration.<br />:param azure_managed_identity: :class:`AzureManagedIdentity` (optional)<br />  The Azure managed identity configuration.<br />:param azure_service_principal: :class:`AzureServicePrincipal` (optional)<br />  The Azure service principal configuration.<br />:param comment: str (optional)<br />  Comment associated with the credential.<br />:param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccount` (optional)<br />  The Databricks managed GCP service account configuration.<br />:param purpose: :class:`CredentialPurpose` (optional)<br />  Indicates the purpose of the credential.<br />:param read_only: bool (optional)<br />  Whether the credential is usable only for read operations. Only applicable when purpose is<br />  **STORAGE**.<br />:param skip_validation: bool (optional)<br />  Optional. Supplying true to this argument skips validation of the created set of credentials.<br /><br />:returns: :class:`CredentialInfo`

```sql
INSERT INTO databricks_account.catalog.credentials (
data__name,
data__aws_iam_role,
data__azure_managed_identity,
data__azure_service_principal,
data__comment,
data__databricks_gcp_service_account,
data__purpose,
data__read_only,
data__skip_validation
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
        The AWS IAM role configuration.
    - name: azure_managed_identity
      value: string
      description: |
        The Azure managed identity configuration.
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
        The Databricks managed GCP service account configuration.
    - name: purpose
      value: string
      description: |
        Indicates the purpose of the credential.
    - name: read_only
      value: string
      description: |
        Whether the credential is usable only for read operations. Only applicable when purpose is **STORAGE**.
    - name: skip_validation
      value: string
      description: |
        Optional. Supplying true to this argument skips validation of the created set of credentials.
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates a service or storage credential on the metastore.<br /><br />The caller must be the owner of the credential or a metastore admin or have the `MANAGE` permission.<br />If the caller is a metastore admin, only the __owner__ field can be changed.<br /><br />:param name_arg: str<br />  Name of the credential.<br />:param aws_iam_role: :class:`AwsIamRole` (optional)<br />  The AWS IAM role configuration.<br />:param azure_managed_identity: :class:`AzureManagedIdentity` (optional)<br />  The Azure managed identity configuration.<br />:param azure_service_principal: :class:`AzureServicePrincipal` (optional)<br />  The Azure service principal configuration.<br />:param comment: str (optional)<br />  Comment associated with the credential.<br />:param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccount` (optional)<br />  The Databricks managed GCP service account configuration.<br />:param force: bool (optional)<br />  Force an update even if there are dependent services (when purpose is **SERVICE**) or dependent<br />  external locations and external tables (when purpose is **STORAGE**).<br />:param isolation_mode: :class:`IsolationMode` (optional)<br />  Whether the current securable is accessible from all workspaces or a specific set of workspaces.<br />:param new_name: str (optional)<br />  New name of credential.<br />:param owner: str (optional)<br />  Username of current owner of credential.<br />:param read_only: bool (optional)<br />  Whether the credential is usable only for read operations. Only applicable when purpose is<br />  **STORAGE**.<br />:param skip_validation: bool (optional)<br />  Supply true to this argument to skip validation of the updated credential.<br /><br />:returns: :class:`CredentialInfo`

```sql
UPDATE databricks_account.catalog.credentials
SET 
data__aws_iam_role = '{{ aws_iam_role }}',
data__azure_managed_identity = '{{ azure_managed_identity }}',
data__azure_service_principal = '{{ azure_service_principal }}',
data__comment = '{{ comment }}',
data__databricks_gcp_service_account = '{{ databricks_gcp_service_account }}',
data__force = '{{ force }}',
data__isolation_mode = '{{ isolation_mode }}',
data__new_name = '{{ new_name }}',
data__owner = '{{ owner }}',
data__read_only = '{{ read_only }}',
data__skip_validation = '{{ skip_validation }}'
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a service or storage credential from the metastore. The caller must be an owner of the<br />credential.<br /><br />:param name_arg: str<br />  Name of the credential.<br />:param force: bool (optional)<br />  Force an update even if there are dependent services (when purpose is **SERVICE**) or dependent<br />  external locations and external tables (when purpose is **STORAGE**).

```sql
DELETE FROM databricks_account.catalog.credentials
WHERE name_arg = '{{ name_arg }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="generate_temporary_service_credential"
    values={[
        { label: 'generate_temporary_service_credential', value: 'generate_temporary_service_credential' },
        { label: 'validate', value: 'validate' }
    ]}
>
<TabItem value="generate_temporary_service_credential">

Returns a set of temporary credentials generated using the specified service credential. The caller<br />must be a metastore admin or have the metastore privilege **ACCESS** on the service credential.<br /><br />:param credential_name: str<br />  The name of the service credential used to generate a temporary credential<br />:param azure_options: :class:`GenerateTemporaryServiceCredentialAzureOptions` (optional)<br />:param gcp_options: :class:`GenerateTemporaryServiceCredentialGcpOptions` (optional)<br /><br />:returns: :class:`TemporaryCredentials`

```sql
EXEC databricks_account.catalog.credentials.generate_temporary_service_credential 
@@json=
'{
"credential_name": "{{ credential_name }}", 
"azure_options": "{{ azure_options }}", 
"gcp_options": "{{ gcp_options }}"
}'
;
```
</TabItem>
<TabItem value="validate">

Validates a credential.<br /><br />For service credentials (purpose is **SERVICE**), either the __credential_name__ or the cloud-specific<br />credential must be provided.<br /><br />For storage credentials (purpose is **STORAGE**), at least one of __external_location_name__ and<br />__url__ need to be provided. If only one of them is provided, it will be used for validation. And if<br />both are provided, the __url__ will be used for validation, and __external_location_name__ will be<br />ignored when checking overlapping urls. Either the __credential_name__ or the cloud-specific<br />credential must be provided.<br /><br />The caller must be a metastore admin or the credential owner or have the required permission on the<br />metastore and the credential (e.g., **CREATE_EXTERNAL_LOCATION** when purpose is **STORAGE**).<br /><br />:param aws_iam_role: :class:`AwsIamRole` (optional)<br />:param azure_managed_identity: :class:`AzureManagedIdentity` (optional)<br />:param credential_name: str (optional)<br />  Required. The name of an existing credential or long-lived cloud credential to validate.<br />:param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccount` (optional)<br />:param external_location_name: str (optional)<br />  The name of an existing external location to validate. Only applicable for storage credentials<br />  (purpose is **STORAGE**.)<br />:param purpose: :class:`CredentialPurpose` (optional)<br />  The purpose of the credential. This should only be used when the credential is specified.<br />:param read_only: bool (optional)<br />  Whether the credential is only usable for read operations. Only applicable for storage credentials<br />  (purpose is **STORAGE**.)<br />:param url: str (optional)<br />  The external location url to validate. Only applicable when purpose is **STORAGE**.<br /><br />:returns: :class:`ValidateCredentialResponse`

```sql
EXEC databricks_account.catalog.credentials.validate 
@@json=
'{
"aws_iam_role": "{{ aws_iam_role }}", 
"azure_managed_identity": "{{ azure_managed_identity }}", 
"credential_name": "{{ credential_name }}", 
"databricks_gcp_service_account": "{{ databricks_gcp_service_account }}", 
"external_location_name": "{{ external_location_name }}", 
"purpose": "{{ purpose }}", 
"read_only": "{{ read_only }}", 
"url": "{{ url }}"
}'
;
```
</TabItem>
</Tabs>

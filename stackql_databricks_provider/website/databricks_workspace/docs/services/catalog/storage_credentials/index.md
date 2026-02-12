---
title: storage_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_credentials
  - catalog
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>storage_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.storage_credentials" /></td></tr>
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
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
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
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a storage credential from the metastore. The caller must be a metastore admin, the owner of the</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_unbound"><code>include_unbound</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of storage credentials (as __StorageCredentialInfo__ objects). The array is limited to</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__name"><code>data__name</code></a></td>
    <td></td>
    <td>Creates a new storage credential.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates a storage credential on the metastore.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes a storage credential from the metastore. The caller must be an owner of the storage</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Validates a storage credential. At least one of __external_location_name__ and __url__ need to be</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the storage credential.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>string</code></td>
    <td>Force an update even if there are dependent external locations or external tables (when purpose is **STORAGE**) or dependent services (when purpose is **SERVICE**).</td>
</tr>
<tr id="parameter-include_unbound">
    <td><CopyableCode code="include_unbound" /></td>
    <td><code>string</code></td>
    <td>Whether to include credentials not bound to the workspace. Effective only if the user has permission to update the credential–workspace binding.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of storage credentials to return. If not set, all the storage credentials are returned (not recommended). - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to 0, the page length is set to a server configured value (recommended); - when set to a value less than 0, an invalid parameter error is returned;</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on previous query.</td>
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
FROM databricks_workspace.catalog.storage_credentials
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets an array of storage credentials (as __StorageCredentialInfo__ objects). The array is limited to

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
FROM databricks_workspace.catalog.storage_credentials
WHERE deployment_name = '{{ deployment_name }}' -- required
AND include_unbound = '{{ include_unbound }}'
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
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

Creates a new storage credential.

```sql
INSERT INTO databricks_workspace.catalog.storage_credentials (
data__name,
data__aws_iam_role,
data__azure_managed_identity,
data__azure_service_principal,
data__cloudflare_api_token,
data__comment,
data__databricks_gcp_service_account,
data__read_only,
data__skip_validation,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ aws_iam_role }}',
'{{ azure_managed_identity }}',
'{{ azure_service_principal }}',
'{{ cloudflare_api_token }}',
'{{ comment }}',
'{{ databricks_gcp_service_account }}',
'{{ read_only }}',
'{{ skip_validation }}',
'{{ deployment_name }}'
RETURNING
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
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: storage_credentials
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the storage_credentials resource.
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
    - name: cloudflare_api_token
      value: string
      description: |
        The Cloudflare API token configuration.
    - name: comment
      value: string
      description: |
        Comment associated with the credential.
    - name: databricks_gcp_service_account
      value: string
      description: |
        The Databricks managed GCP service account configuration.
    - name: read_only
      value: string
      description: |
        Whether the credential is usable only for read operations. Only applicable when purpose is **STORAGE**.
    - name: skip_validation
      value: string
      description: |
        Supplying true to this argument skips validation of the created credential.
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

Updates a storage credential on the metastore.

```sql
UPDATE databricks_workspace.catalog.storage_credentials
SET 
data__aws_iam_role = '{{ aws_iam_role }}',
data__azure_managed_identity = '{{ azure_managed_identity }}',
data__azure_service_principal = '{{ azure_service_principal }}',
data__cloudflare_api_token = '{{ cloudflare_api_token }}',
data__comment = '{{ comment }}',
data__databricks_gcp_service_account = '{{ databricks_gcp_service_account }}',
data__force = '{{ force }}',
data__isolation_mode = '{{ isolation_mode }}',
data__new_name = '{{ new_name }}',
data__owner = '{{ owner }}',
data__read_only = '{{ read_only }}',
data__skip_validation = '{{ skip_validation }}'
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
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

Deletes a storage credential from the metastore. The caller must be an owner of the storage

```sql
DELETE FROM databricks_workspace.catalog.storage_credentials
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate"
    values={[
        { label: 'validate', value: 'validate' }
    ]}
>
<TabItem value="validate">

Validates a storage credential. At least one of __external_location_name__ and __url__ need to be

```sql
EXEC databricks_workspace.catalog.storage_credentials.validate 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"aws_iam_role": "{{ aws_iam_role }}", 
"azure_managed_identity": "{{ azure_managed_identity }}", 
"azure_service_principal": "{{ azure_service_principal }}", 
"cloudflare_api_token": "{{ cloudflare_api_token }}", 
"databricks_gcp_service_account": "{{ databricks_gcp_service_account }}", 
"external_location_name": "{{ external_location_name }}", 
"read_only": "{{ read_only }}", 
"storage_credential_name": "{{ storage_credential_name }}", 
"url": "{{ url }}"
}'
;
```
</TabItem>
</Tabs>

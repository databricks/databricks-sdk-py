---
title: secret_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - secret_scopes
  - workspace
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

Creates, updates, deletes, gets or lists a <code>secret_scopes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secret_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.secret_scopes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "A unique name to identify the secret scope."
  },
  {
    "name": "backend_type",
    "type": "string",
    "description": "The type of secret scope backend."
  },
  {
    "name": "keyvault_metadata",
    "type": "object",
    "description": "The metadata for the secret scope if the type is ``AZURE_KEYVAULT``",
    "children": [
      {
        "name": "resource_id",
        "type": "string",
        "description": "The resource id of the azure KeyVault that user wants to associate the scope with."
      },
      {
        "name": "dns_name",
        "type": "string",
        "description": "The DNS of the KeyVault"
      }
    ]
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Lists all secret scopes available in the workspace.<br /><br />Example response:<br /><br />.. code::<br /><br />&#123; "scopes": [&#123; "name": "my-databricks-scope", "backend_type": "DATABRICKS" &#125;,&#123; "name": "mount-points",<br />"backend_type": "DATABRICKS" &#125;] &#125;<br /><br />Throws ``PERMISSION_DENIED`` if the user does not have permission to make this API call.<br /><br /><br />:returns: Iterator over :class:`SecretScope`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__scope"><code>data__scope</code></a></td>
    <td></td>
    <td>Creates a new secret scope.<br /><br />The scope name must consist of alphanumeric characters, dashes, underscores, and periods, and may not<br />exceed 128 characters.<br /><br />Example request:<br /><br />.. code::<br /><br />&#123; "scope": "my-simple-databricks-scope", "initial_manage_principal": "users" "scope_backend_type":<br />"databricks|azure_keyvault", # below is only required if scope type is azure_keyvault<br />"backend_azure_keyvault": &#123; "resource_id":<br />"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/xxxx/providers/Microsoft.KeyVault/vaults/xxxx",<br />"tenant_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "dns_name": "https://xxxx.vault.azure.net/", &#125; &#125;<br /><br />If ``initial_manage_principal`` is specified, the initial ACL applied to the scope is applied to the<br />supplied principal (user or group) with ``MANAGE`` permissions. The only supported principal for this<br />option is the group ``users``, which contains all users in the workspace. If<br />``initial_manage_principal`` is not specified, the initial ACL with ``MANAGE`` permission applied to<br />the scope is assigned to the API request issuer's user identity.<br /><br />If ``scope_backend_type`` is ``azure_keyvault``, a secret scope is created with secrets from a given<br />Azure KeyVault. The caller must provide the keyvault_resource_id and the tenant_id for the key vault.<br />If ``scope_backend_type`` is ``databricks`` or is unspecified, an empty secret scope is created and<br />stored in Databricks's own storage.<br /><br />Throws ``RESOURCE_ALREADY_EXISTS`` if a scope with the given name already exists. Throws<br />``RESOURCE_LIMIT_EXCEEDED`` if maximum number of scopes in the workspace is exceeded. Throws<br />``INVALID_PARAMETER_VALUE`` if the scope name is invalid. Throws ``BAD_REQUEST`` if request violated<br />constraints. Throws ``CUSTOMER_UNAUTHORIZED`` if normal user attempts to create a scope with name<br />reserved for databricks internal usage. Throws ``UNAUTHENTICATED`` if unable to verify user access<br />permission on Azure KeyVault<br /><br />:param scope: str<br />  Scope name requested by the user. Scope names are unique.<br />:param backend_azure_keyvault: :class:`AzureKeyVaultSecretScopeMetadata` (optional)<br />  The metadata for the secret scope if the type is ``AZURE_KEYVAULT``<br />:param initial_manage_principal: str (optional)<br />  The principal that is initially granted ``MANAGE`` permission to the created scope.<br />:param scope_backend_type: :class:`ScopeBackendType` (optional)<br />  The backend type the scope will be created with. If not specified, will default to ``DATABRICKS``</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Deletes a secret scope.<br /><br />Example request:<br /><br />.. code::<br /><br />&#123; "scope": "my-secret-scope" &#125;<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if the scope does not exist. Throws ``PERMISSION_DENIED`` if the<br />user does not have permission to make this API call. Throws ``BAD_REQUEST`` if system user attempts to<br />delete internal secret scope.<br /><br />:param scope: str<br />  Name of the scope to delete.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Lists all secret scopes available in the workspace.<br /><br />Example response:<br /><br />.. code::<br /><br />&#123; "scopes": [&#123; "name": "my-databricks-scope", "backend_type": "DATABRICKS" &#125;,&#123; "name": "mount-points",<br />"backend_type": "DATABRICKS" &#125;] &#125;<br /><br />Throws ``PERMISSION_DENIED`` if the user does not have permission to make this API call.<br /><br /><br />:returns: Iterator over :class:`SecretScope`

```sql
SELECT
name,
backend_type,
keyvault_metadata
FROM databricks_workspace.workspace.secret_scopes
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Creates a new secret scope.<br /><br />The scope name must consist of alphanumeric characters, dashes, underscores, and periods, and may not<br />exceed 128 characters.<br /><br />Example request:<br /><br />.. code::<br /><br />&#123; "scope": "my-simple-databricks-scope", "initial_manage_principal": "users" "scope_backend_type":<br />"databricks|azure_keyvault", # below is only required if scope type is azure_keyvault<br />"backend_azure_keyvault": &#123; "resource_id":<br />"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/xxxx/providers/Microsoft.KeyVault/vaults/xxxx",<br />"tenant_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "dns_name": "https://xxxx.vault.azure.net/", &#125; &#125;<br /><br />If ``initial_manage_principal`` is specified, the initial ACL applied to the scope is applied to the<br />supplied principal (user or group) with ``MANAGE`` permissions. The only supported principal for this<br />option is the group ``users``, which contains all users in the workspace. If<br />``initial_manage_principal`` is not specified, the initial ACL with ``MANAGE`` permission applied to<br />the scope is assigned to the API request issuer's user identity.<br /><br />If ``scope_backend_type`` is ``azure_keyvault``, a secret scope is created with secrets from a given<br />Azure KeyVault. The caller must provide the keyvault_resource_id and the tenant_id for the key vault.<br />If ``scope_backend_type`` is ``databricks`` or is unspecified, an empty secret scope is created and<br />stored in Databricks's own storage.<br /><br />Throws ``RESOURCE_ALREADY_EXISTS`` if a scope with the given name already exists. Throws<br />``RESOURCE_LIMIT_EXCEEDED`` if maximum number of scopes in the workspace is exceeded. Throws<br />``INVALID_PARAMETER_VALUE`` if the scope name is invalid. Throws ``BAD_REQUEST`` if request violated<br />constraints. Throws ``CUSTOMER_UNAUTHORIZED`` if normal user attempts to create a scope with name<br />reserved for databricks internal usage. Throws ``UNAUTHENTICATED`` if unable to verify user access<br />permission on Azure KeyVault<br /><br />:param scope: str<br />  Scope name requested by the user. Scope names are unique.<br />:param backend_azure_keyvault: :class:`AzureKeyVaultSecretScopeMetadata` (optional)<br />  The metadata for the secret scope if the type is ``AZURE_KEYVAULT``<br />:param initial_manage_principal: str (optional)<br />  The principal that is initially granted ``MANAGE`` permission to the created scope.<br />:param scope_backend_type: :class:`ScopeBackendType` (optional)<br />  The backend type the scope will be created with. If not specified, will default to ``DATABRICKS``

```sql
INSERT INTO databricks_workspace.workspace.secret_scopes (
data__scope,
data__backend_azure_keyvault,
data__initial_manage_principal,
data__scope_backend_type,
deployment_name
)
SELECT 
'{{ scope }}' /* required */,
'{{ backend_azure_keyvault }}',
'{{ initial_manage_principal }}',
'{{ scope_backend_type }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: secret_scopes
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the secret_scopes resource.
    - name: scope
      value: string
      description: |
        Scope name requested by the user. Scope names are unique.
    - name: backend_azure_keyvault
      value: string
      description: |
        The metadata for the secret scope if the type is ``AZURE_KEYVAULT``
    - name: initial_manage_principal
      value: string
      description: |
        The principal that is initially granted ``MANAGE`` permission to the created scope.
    - name: scope_backend_type
      value: string
      description: |
        The backend type the scope will be created with. If not specified, will default to ``DATABRICKS``
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a secret scope.<br /><br />Example request:<br /><br />.. code::<br /><br />&#123; "scope": "my-secret-scope" &#125;<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if the scope does not exist. Throws ``PERMISSION_DENIED`` if the<br />user does not have permission to make this API call. Throws ``BAD_REQUEST`` if system user attempts to<br />delete internal secret scope.<br /><br />:param scope: str<br />  Name of the scope to delete.

```sql
EXEC databricks_workspace.workspace.secret_scopes.delete 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"scope": "{{ scope }}"
}'
;
```
</TabItem>
</Tabs>

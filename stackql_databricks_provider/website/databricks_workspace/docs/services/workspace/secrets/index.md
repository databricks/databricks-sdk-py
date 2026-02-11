---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
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

Creates, updates, deletes, gets or lists a <code>secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.secrets" /></td></tr>
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
    "name": "key",
    "type": "string",
    "description": ""
  },
  {
    "name": "value",
    "type": "string",
    "description": "The value of the secret in its byte representation."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "key",
    "type": "string",
    "description": "A unique name to identify the secret."
  },
  {
    "name": "last_updated_timestamp",
    "type": "integer",
    "description": "The last updated timestamp (in milliseconds) for the secret."
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a secret for a given key and scope. This API can only be called from the DBUtils interface. Users<br />need the READ permission to make this call.<br /><br />Example response:<br /><br />.. code::<br /><br />&#123; "key": "my-string-key", "value": &lt;bytes of the secret value&gt; &#125;<br /><br />Note that the secret value returned is in bytes. The interpretation of the bytes is determined by the<br />caller in DBUtils and the type the data is decoded into.<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret or secret scope exists. Throws<br />``PERMISSION_DENIED`` if the user does not have permission to make this API call.<br /><br />Note: This is explicitly an undocumented API. It also doesn't need to be supported for the /preview<br />prefix, because it's not a customer-facing API (i.e. only used for DBUtils SecretUtils to fetch<br />secrets).<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope or secret exists. Throws ``BAD_REQUEST`` if<br />normal user calls get secret outside of a notebook. AKV specific errors: Throws<br />``INVALID_PARAMETER_VALUE`` if secret name is not alphanumeric or too long. Throws<br />``PERMISSION_DENIED`` if secret manager cannot access AKV with 403 error Throws ``MALFORMED_REQUEST``<br />if secret manager cannot access AKV with any other 4xx error<br /><br />:param scope: str<br />  The name of the scope that contains the secret.<br />:param key: str<br />  Name of the secret to fetch value information.<br /><br />:returns: :class:`GetSecretResponse`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Lists the secret keys that are stored at this scope. This is a metadata-only operation; secret data<br />cannot be retrieved using this API. Users need the READ permission to make this call.<br /><br />Example response:<br /><br />.. code::<br /><br />&#123; "secrets": [ &#123; "key": "my-string-key"", "last_updated_timestamp": "1520467595000" &#125;, &#123; "key":<br />"my-byte-key", "last_updated_timestamp": "1520467595000" &#125;, ] &#125;<br /><br />The lastUpdatedTimestamp returned is in milliseconds since epoch.<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``PERMISSION_DENIED`` if the<br />user does not have permission to make this API call.<br /><br />:param scope: str<br />  The name of the scope to list secrets within.<br /><br />:returns: Iterator over :class:`SecretMetadata`</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__scope"><code>data__scope</code></a>, <a href="#parameter-data__key"><code>data__key</code></a></td>
    <td></td>
    <td>Inserts a secret under the provided scope with the given name. If a secret already exists with the<br />same name, this command overwrites the existing secret's value. The server encrypts the secret using<br />the secret scope's encryption settings before storing it. You must have ``WRITE`` or ``MANAGE``<br />permission on the secret scope.<br /><br />The secret key must consist of alphanumeric characters, dashes, underscores, and periods, and cannot<br />exceed 128 characters. The maximum allowed secret value size is 128 KB. The maximum number of secrets<br />in a given scope is 1000.<br /><br />Example request:<br /><br />.. code::<br /><br />&#123; "scope": "my-databricks-scope", "key": "my-string-key", "string_value": "foobar" &#125;<br /><br />The input fields "string_value" or "bytes_value" specify the type of the secret, which will determine<br />the value returned when the secret value is requested. Exactly one must be specified.<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``RESOURCE_LIMIT_EXCEEDED``<br />if maximum number of secrets in scope is exceeded. Throws ``INVALID_PARAMETER_VALUE`` if the request<br />parameters are invalid. Throws ``PERMISSION_DENIED`` if the user does not have permission to make this<br />API call. Throws ``MALFORMED_REQUEST`` if request is incorrectly formatted or conflicting. Throws<br />``BAD_REQUEST`` if request is made against Azure KeyVault backed scope.<br /><br />:param scope: str<br />  The name of the scope to which the secret will be associated with.<br />:param key: str<br />  A unique name to identify the secret.<br />:param bytes_value: str (optional)<br />  If specified, value will be stored as bytes.<br />:param string_value: str (optional)<br />  If specified, note that the value will be stored in UTF-8 (MB4) form.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-key"><code>key</code></a></td>
    <td></td>
    <td>Deletes the secret stored in this secret scope. You must have ``WRITE`` or ``MANAGE`` permission on<br />the Secret Scope.<br /><br />Example request:<br /><br />.. code::<br /><br />&#123; "scope": "my-secret-scope", "key": "my-secret-key" &#125;<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope or secret exists. Throws<br />``PERMISSION_DENIED`` if the user does not have permission to make this API call. Throws<br />``BAD_REQUEST`` if system user attempts to delete an internal secret, or request is made against Azure<br />KeyVault backed scope.<br /><br />:param scope: str<br />  The name of the scope that contains the secret to delete.<br />:param key: str<br />  Name of the secret to delete.</td>
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
<tr id="parameter-key">
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>Name of the secret to fetch value information.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The name of the scope to list secrets within.</td>
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

Gets a secret for a given key and scope. This API can only be called from the DBUtils interface. Users<br />need the READ permission to make this call.<br /><br />Example response:<br /><br />.. code::<br /><br />&#123; "key": "my-string-key", "value": &lt;bytes of the secret value&gt; &#125;<br /><br />Note that the secret value returned is in bytes. The interpretation of the bytes is determined by the<br />caller in DBUtils and the type the data is decoded into.<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret or secret scope exists. Throws<br />``PERMISSION_DENIED`` if the user does not have permission to make this API call.<br /><br />Note: This is explicitly an undocumented API. It also doesn't need to be supported for the /preview<br />prefix, because it's not a customer-facing API (i.e. only used for DBUtils SecretUtils to fetch<br />secrets).<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope or secret exists. Throws ``BAD_REQUEST`` if<br />normal user calls get secret outside of a notebook. AKV specific errors: Throws<br />``INVALID_PARAMETER_VALUE`` if secret name is not alphanumeric or too long. Throws<br />``PERMISSION_DENIED`` if secret manager cannot access AKV with 403 error Throws ``MALFORMED_REQUEST``<br />if secret manager cannot access AKV with any other 4xx error<br /><br />:param scope: str<br />  The name of the scope that contains the secret.<br />:param key: str<br />  Name of the secret to fetch value information.<br /><br />:returns: :class:`GetSecretResponse`

```sql
SELECT
key,
value
FROM databricks_workspace.workspace.secrets
WHERE scope = '{{ scope }}' -- required
AND key = '{{ key }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the secret keys that are stored at this scope. This is a metadata-only operation; secret data<br />cannot be retrieved using this API. Users need the READ permission to make this call.<br /><br />Example response:<br /><br />.. code::<br /><br />&#123; "secrets": [ &#123; "key": "my-string-key"", "last_updated_timestamp": "1520467595000" &#125;, &#123; "key":<br />"my-byte-key", "last_updated_timestamp": "1520467595000" &#125;, ] &#125;<br /><br />The lastUpdatedTimestamp returned is in milliseconds since epoch.<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``PERMISSION_DENIED`` if the<br />user does not have permission to make this API call.<br /><br />:param scope: str<br />  The name of the scope to list secrets within.<br /><br />:returns: Iterator over :class:`SecretMetadata`

```sql
SELECT
key,
last_updated_timestamp
FROM databricks_workspace.workspace.secrets
WHERE scope = '{{ scope }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="put"
    values={[
        { label: 'put', value: 'put' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="put">

Inserts a secret under the provided scope with the given name. If a secret already exists with the<br />same name, this command overwrites the existing secret's value. The server encrypts the secret using<br />the secret scope's encryption settings before storing it. You must have ``WRITE`` or ``MANAGE``<br />permission on the secret scope.<br /><br />The secret key must consist of alphanumeric characters, dashes, underscores, and periods, and cannot<br />exceed 128 characters. The maximum allowed secret value size is 128 KB. The maximum number of secrets<br />in a given scope is 1000.<br /><br />Example request:<br /><br />.. code::<br /><br />&#123; "scope": "my-databricks-scope", "key": "my-string-key", "string_value": "foobar" &#125;<br /><br />The input fields "string_value" or "bytes_value" specify the type of the secret, which will determine<br />the value returned when the secret value is requested. Exactly one must be specified.<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``RESOURCE_LIMIT_EXCEEDED``<br />if maximum number of secrets in scope is exceeded. Throws ``INVALID_PARAMETER_VALUE`` if the request<br />parameters are invalid. Throws ``PERMISSION_DENIED`` if the user does not have permission to make this<br />API call. Throws ``MALFORMED_REQUEST`` if request is incorrectly formatted or conflicting. Throws<br />``BAD_REQUEST`` if request is made against Azure KeyVault backed scope.<br /><br />:param scope: str<br />  The name of the scope to which the secret will be associated with.<br />:param key: str<br />  A unique name to identify the secret.<br />:param bytes_value: str (optional)<br />  If specified, value will be stored as bytes.<br />:param string_value: str (optional)<br />  If specified, note that the value will be stored in UTF-8 (MB4) form.

```sql
INSERT INTO databricks_workspace.workspace.secrets (
data__scope,
data__key,
data__bytes_value,
data__string_value,
deployment_name
)
SELECT 
'{{ scope }}' /* required */,
'{{ key }}' /* required */,
'{{ bytes_value }}',
'{{ string_value }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: secrets
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the secrets resource.
    - name: scope
      value: string
      description: |
        The name of the scope to which the secret will be associated with.
    - name: key
      value: string
      description: |
        A unique name to identify the secret.
    - name: bytes_value
      value: string
      description: |
        If specified, value will be stored as bytes.
    - name: string_value
      value: string
      description: |
        If specified, note that the value will be stored in UTF-8 (MB4) form.
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

Deletes the secret stored in this secret scope. You must have ``WRITE`` or ``MANAGE`` permission on<br />the Secret Scope.<br /><br />Example request:<br /><br />.. code::<br /><br />&#123; "scope": "my-secret-scope", "key": "my-secret-key" &#125;<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope or secret exists. Throws<br />``PERMISSION_DENIED`` if the user does not have permission to make this API call. Throws<br />``BAD_REQUEST`` if system user attempts to delete an internal secret, or request is made against Azure<br />KeyVault backed scope.<br /><br />:param scope: str<br />  The name of the scope that contains the secret to delete.<br />:param key: str<br />  Name of the secret to delete.

```sql
EXEC databricks_workspace.workspace.secrets.delete 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"scope": "{{ scope }}", 
"key": "{{ key }}"
}'
;
```
</TabItem>
</Tabs>

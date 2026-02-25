---
title: providers
hide_title: false
hide_table_of_contents: false
keywords:
  - providers
  - sharing
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="providers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sharing.providers" /></td></tr>
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
    "name": "name",
    "type": "string",
    "description": "The name of the Provider."
  },
  {
    "name": "data_provider_global_metastore_id",
    "type": "string",
    "description": "The global UC metastore id of the data provider. This field is only present when the __authentication_type__ is **DATABRICKS**. The identifier is of format __cloud__:__region__:__metastore-uuid__."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "UUID of the provider's UC metastore. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "authentication_type",
    "type": "string",
    "description": "The delta sharing authentication type. (DATABRICKS, OAUTH_CLIENT_CREDENTIALS, OIDC_FEDERATION, TOKEN)"
  },
  {
    "name": "cloud",
    "type": "string",
    "description": "Cloud vendor of the provider's UC metastore. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "Description about the provider."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this Provider was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of Provider creator."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of Provider owner."
  },
  {
    "name": "recipient_profile",
    "type": "object",
    "description": "The recipient profile. This field is only present when the authentication_type is `TOKEN` or `OAUTH_CLIENT_CREDENTIALS`.",
    "children": [
      {
        "name": "bearer_token",
        "type": "string",
        "description": ""
      },
      {
        "name": "endpoint",
        "type": "string",
        "description": "The endpoint for the share to be used by the recipient."
      },
      {
        "name": "share_credentials_version",
        "type": "integer",
        "description": "The version number of the recipient's credentials on a share."
      }
    ]
  },
  {
    "name": "recipient_profile_str",
    "type": "string",
    "description": "This field is required when the __authentication_type__ is **TOKEN**, **OAUTH_CLIENT_CREDENTIALS** or not provided."
  },
  {
    "name": "region",
    "type": "string",
    "description": "Cloud region of the provider's UC metastore. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this Provider was created, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified Provider."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the Provider."
  },
  {
    "name": "data_provider_global_metastore_id",
    "type": "string",
    "description": "The global UC metastore id of the data provider. This field is only present when the __authentication_type__ is **DATABRICKS**. The identifier is of format __cloud__:__region__:__metastore-uuid__."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "UUID of the provider's UC metastore. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "authentication_type",
    "type": "string",
    "description": "The delta sharing authentication type. (DATABRICKS, OAUTH_CLIENT_CREDENTIALS, OIDC_FEDERATION, TOKEN)"
  },
  {
    "name": "cloud",
    "type": "string",
    "description": "Cloud vendor of the provider's UC metastore. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "Description about the provider."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this Provider was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of Provider creator."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of Provider owner."
  },
  {
    "name": "recipient_profile",
    "type": "object",
    "description": "The recipient profile. This field is only present when the authentication_type is `TOKEN` or `OAUTH_CLIENT_CREDENTIALS`.",
    "children": [
      {
        "name": "bearer_token",
        "type": "string",
        "description": ""
      },
      {
        "name": "endpoint",
        "type": "string",
        "description": "The endpoint for the share to be used by the recipient."
      },
      {
        "name": "share_credentials_version",
        "type": "integer",
        "description": "The version number of the recipient's credentials on a share."
      }
    ]
  },
  {
    "name": "recipient_profile_str",
    "type": "string",
    "description": "This field is required when the __authentication_type__ is **TOKEN**, **OAUTH_CLIENT_CREDENTIALS** or not provided."
  },
  {
    "name": "region",
    "type": "string",
    "description": "Cloud region of the provider's UC metastore. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this Provider was created, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified Provider."
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets a specific authentication provider. The caller must supply the name of the provider, and must</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-data_provider_global_metastore_id"><code>data_provider_global_metastore_id</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of available authentication providers. The caller must either be a metastore admin, have</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-authentication_type"><code>authentication_type</code></a></td>
    <td></td>
    <td>Creates a new authentication provider minimally based on a name and authentication type. The caller</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Updates the information for an authentication provider, if the caller is a metastore admin or is the</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Deletes an authentication provider, if the caller is a metastore admin or is the owner of the</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the provider.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-data_provider_global_metastore_id">
    <td><CopyableCode code="data_provider_global_metastore_id" /></td>
    <td><code>string</code></td>
    <td>If not provided, all providers will be returned. If no providers exist with this ID, no results will be returned.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of providers to return. - when set to 0, the page length is set to a server configured value (recommended); - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to a value less than 0, an invalid parameter error is returned; - If not set, all valid providers are returned (not recommended). - Note: The number of returned providers might be less than the specified max_results size, even zero. The only definitive indication that no further providers can be fetched is when the next_page_token is unset from the response.</td>
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

Gets a specific authentication provider. The caller must supply the name of the provider, and must

```sql
SELECT
name,
data_provider_global_metastore_id,
metastore_id,
authentication_type,
cloud,
comment,
created_at,
created_by,
owner,
recipient_profile,
recipient_profile_str,
region,
updated_at,
updated_by
FROM databricks_workspace.sharing.providers
WHERE name = '{{ name }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets an array of available authentication providers. The caller must either be a metastore admin, have

```sql
SELECT
name,
data_provider_global_metastore_id,
metastore_id,
authentication_type,
cloud,
comment,
created_at,
created_by,
owner,
recipient_profile,
recipient_profile_str,
region,
updated_at,
updated_by
FROM databricks_workspace.sharing.providers
WHERE workspace = '{{ workspace }}' -- required
AND data_provider_global_metastore_id = '{{ data_provider_global_metastore_id }}'
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

Creates a new authentication provider minimally based on a name and authentication type. The caller

```sql
INSERT INTO databricks_workspace.sharing.providers (
name,
authentication_type,
comment,
recipient_profile_str,
workspace
)
SELECT 
'{{ name }}' /* required */,
'{{ authentication_type }}' /* required */,
'{{ comment }}',
'{{ recipient_profile_str }}',
'{{ workspace }}'
RETURNING
name,
data_provider_global_metastore_id,
metastore_id,
authentication_type,
cloud,
comment,
created_at,
created_by,
owner,
recipient_profile,
recipient_profile_str,
region,
updated_at,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: providers
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the providers resource.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the Provider.
    - name: authentication_type
      value: "{{ authentication_type }}"
      description: |
        :param comment: str (optional) Description about the provider.
    - name: comment
      value: "{{ comment }}"
    - name: recipient_profile_str
      value: "{{ recipient_profile_str }}"
      description: |
        This field is required when the __authentication_type__ is **TOKEN**, **OAUTH_CLIENT_CREDENTIALS** or not provided.
`}</CodeBlock>

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

Updates the information for an authentication provider, if the caller is a metastore admin or is the

```sql
UPDATE databricks_workspace.sharing.providers
SET 
comment = '{{ comment }}',
new_name = '{{ new_name }}',
owner = '{{ owner }}',
recipient_profile_str = '{{ recipient_profile_str }}'
WHERE 
name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
RETURNING
name,
data_provider_global_metastore_id,
metastore_id,
authentication_type,
cloud,
comment,
created_at,
created_by,
owner,
recipient_profile,
recipient_profile_str,
region,
updated_at,
updated_by;
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

Deletes an authentication provider, if the caller is a metastore admin or is the owner of the

```sql
DELETE FROM databricks_workspace.sharing.providers
WHERE name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

---
title: account_metastores
hide_title: false
hide_table_of_contents: false
keywords:
  - account_metastores
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

Creates, updates, deletes, gets or lists an <code>account_metastores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_metastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.catalog.account_metastores" /></td></tr>
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
    "name": "metastore_info",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "cloud",
        "type": "string",
        "description": ""
      },
      {
        "name": "created_at",
        "type": "integer",
        "description": "Time at which this metastore was created, in epoch milliseconds."
      },
      {
        "name": "created_by",
        "type": "string",
        "description": "Username of metastore creator."
      },
      {
        "name": "default_data_access_config_id",
        "type": "string",
        "description": "Unique identifier of the metastore's (Default) Data Access Configuration."
      },
      {
        "name": "delta_sharing_organization_name",
        "type": "string",
        "description": "The organization name of a Delta Sharing entity, to be used in Databricks-to-Databricks Delta Sharing as the official name."
      },
      {
        "name": "delta_sharing_recipient_token_lifetime_in_seconds",
        "type": "integer",
        "description": "The lifetime of delta sharing recipient token in seconds."
      },
      {
        "name": "delta_sharing_scope",
        "type": "string",
        "description": "The scope of Delta Sharing enabled for the metastore."
      },
      {
        "name": "external_access_enabled",
        "type": "boolean",
        "description": "Whether to allow non-DBR clients to directly access entities under the metastore."
      },
      {
        "name": "global_metastore_id",
        "type": "string",
        "description": "Globally unique metastore ID across clouds and regions, of the form `cloud:region:metastore_id`."
      },
      {
        "name": "metastore_id",
        "type": "string",
        "description": "Unique identifier of metastore."
      },
      {
        "name": "name",
        "type": "string",
        "description": "The user-specified name of the metastore."
      },
      {
        "name": "owner",
        "type": "string",
        "description": "The owner of the metastore."
      },
      {
        "name": "privilege_model_version",
        "type": "string",
        "description": "Privilege model version of the metastore, of the form `major.minor` (e.g., `1.0`)."
      },
      {
        "name": "region",
        "type": "string",
        "description": "Cloud region which the metastore serves (e.g., `us-west-2`, `westus`)."
      },
      {
        "name": "storage_root",
        "type": "string",
        "description": "The storage root URL for metastore"
      },
      {
        "name": "storage_root_credential_id",
        "type": "string",
        "description": "UUID of storage credential to access the metastore storage_root."
      },
      {
        "name": "storage_root_credential_name",
        "type": "string",
        "description": "Name of the storage credential to access the metastore storage_root."
      },
      {
        "name": "updated_at",
        "type": "integer",
        "description": "Time at which the metastore was last modified, in epoch milliseconds."
      },
      {
        "name": "updated_by",
        "type": "string",
        "description": "Username of user who last modified the metastore."
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The user-specified name of the metastore."
  },
  {
    "name": "default_data_access_config_id",
    "type": "string",
    "description": "Unique identifier of the metastore's (Default) Data Access Configuration."
  },
  {
    "name": "global_metastore_id",
    "type": "string",
    "description": "Globally unique metastore ID across clouds and regions, of the form `cloud:region:metastore_id`."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of metastore."
  },
  {
    "name": "storage_root_credential_id",
    "type": "string",
    "description": "UUID of storage credential to access the metastore storage_root."
  },
  {
    "name": "delta_sharing_organization_name",
    "type": "string",
    "description": "The organization name of a Delta Sharing entity, to be used in Databricks-to-Databricks Delta Sharing as the official name."
  },
  {
    "name": "storage_root_credential_name",
    "type": "string",
    "description": "Name of the storage credential to access the metastore storage_root."
  },
  {
    "name": "cloud",
    "type": "string",
    "description": ""
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this metastore was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of metastore creator."
  },
  {
    "name": "delta_sharing_recipient_token_lifetime_in_seconds",
    "type": "integer",
    "description": "The lifetime of delta sharing recipient token in seconds."
  },
  {
    "name": "delta_sharing_scope",
    "type": "string",
    "description": "The scope of Delta Sharing enabled for the metastore."
  },
  {
    "name": "external_access_enabled",
    "type": "boolean",
    "description": "Whether to allow non-DBR clients to directly access entities under the metastore."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The owner of the metastore."
  },
  {
    "name": "privilege_model_version",
    "type": "string",
    "description": "Privilege model version of the metastore, of the form `major.minor` (e.g., `1.0`)."
  },
  {
    "name": "region",
    "type": "string",
    "description": "Cloud region which the metastore serves (e.g., `us-west-2`, `westus`)."
  },
  {
    "name": "storage_root",
    "type": "string",
    "description": "The storage root URL for metastore"
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which the metastore was last modified, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified the metastore."
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a></td>
    <td></td>
    <td>Gets a Unity Catalog metastore from an account, both specified by ID.<br /><br />:param metastore_id: str<br />  Unity Catalog metastore ID<br /><br />:returns: :class:`AccountsGetMetastoreResponse`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Gets all Unity Catalog metastores associated with an account specified by ID.<br /><br /><br />:returns: Iterator over :class:`MetastoreInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a Unity Catalog metastore.<br /><br />:param metastore_info: :class:`CreateAccountsMetastore` (optional)<br /><br />:returns: :class:`AccountsCreateMetastoreResponse`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a></td>
    <td></td>
    <td>Updates an existing Unity Catalog metastore.<br /><br />:param metastore_id: str<br />  Unity Catalog metastore ID<br />:param metastore_info: :class:`UpdateAccountsMetastore` (optional)<br />  Properties of the metastore to change.<br /><br />:returns: :class:`AccountsUpdateMetastoreResponse`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes a Unity Catalog metastore for an account, both specified by ID.<br /><br />:param metastore_id: str<br />  Unity Catalog metastore ID<br />:param force: bool (optional)<br />  Force deletion even if the metastore is not empty. Default is false.<br /><br />:returns: :class:`AccountsDeleteMetastoreResponse`</td>
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
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>string</code></td>
    <td>Force deletion even if the metastore is not empty. Default is false.</td>
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

Gets a Unity Catalog metastore from an account, both specified by ID.<br /><br />:param metastore_id: str<br />  Unity Catalog metastore ID<br /><br />:returns: :class:`AccountsGetMetastoreResponse`

```sql
SELECT
metastore_info
FROM databricks_account.catalog.account_metastores
WHERE account_id = '{{ account_id }}' -- required
AND metastore_id = '{{ metastore_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all Unity Catalog metastores associated with an account specified by ID.<br /><br /><br />:returns: Iterator over :class:`MetastoreInfo`

```sql
SELECT
name,
default_data_access_config_id,
global_metastore_id,
metastore_id,
storage_root_credential_id,
delta_sharing_organization_name,
storage_root_credential_name,
cloud,
created_at,
created_by,
delta_sharing_recipient_token_lifetime_in_seconds,
delta_sharing_scope,
external_access_enabled,
owner,
privilege_model_version,
region,
storage_root,
updated_at,
updated_by
FROM databricks_account.catalog.account_metastores
WHERE account_id = '{{ account_id }}' -- required
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

Creates a Unity Catalog metastore.<br /><br />:param metastore_info: :class:`CreateAccountsMetastore` (optional)<br /><br />:returns: :class:`AccountsCreateMetastoreResponse`

```sql
INSERT INTO databricks_account.catalog.account_metastores (
data__metastore_info,
account_id
)
SELECT 
'{{ metastore_info }}',
'{{ account_id }}'
RETURNING
metastore_info
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: account_metastores
  props:
    - name: account_id
      value: string
      description: Required parameter for the account_metastores resource.
    - name: metastore_info
      value: string
      description: |
        :returns: :class:`AccountsCreateMetastoreResponse`
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates an existing Unity Catalog metastore.<br /><br />:param metastore_id: str<br />  Unity Catalog metastore ID<br />:param metastore_info: :class:`UpdateAccountsMetastore` (optional)<br />  Properties of the metastore to change.<br /><br />:returns: :class:`AccountsUpdateMetastoreResponse`

```sql
REPLACE databricks_account.catalog.account_metastores
SET 
data__metastore_info = '{{ metastore_info }}'
WHERE 
account_id = '{{ account_id }}' --required
AND metastore_id = '{{ metastore_id }}' --required
RETURNING
metastore_info;
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

Deletes a Unity Catalog metastore for an account, both specified by ID.<br /><br />:param metastore_id: str<br />  Unity Catalog metastore ID<br />:param force: bool (optional)<br />  Force deletion even if the metastore is not empty. Default is false.<br /><br />:returns: :class:`AccountsDeleteMetastoreResponse`

```sql
DELETE FROM databricks_account.catalog.account_metastores
WHERE account_id = '{{ account_id }}' --required
AND metastore_id = '{{ metastore_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>

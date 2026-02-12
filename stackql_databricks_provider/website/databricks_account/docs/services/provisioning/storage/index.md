---
title: storage
hide_title: false
hide_table_of_contents: false
keywords:
  - storage
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>storage</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.storage" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="storage_get"
    values={[
        { label: 'storage_get', value: 'storage_get' },
        { label: 'storage_list', value: 'storage_list' }
    ]}
>
<TabItem value="storage_get">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "storage_configuration_id",
    "type": "string",
    "description": "Databricks storage configuration ID."
  },
  {
    "name": "storage_configuration_name",
    "type": "string",
    "description": "The human-readable name of the storage configuration."
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the storage configuration was created."
  },
  {
    "name": "role_arn",
    "type": "string",
    "description": "Optional IAM role that is used to access the workspace catalog which is created during workspace creation for UC by Default. If a storage configuration with this field populated is used to create a workspace, then a workspace catalog is created together with the workspace. The workspace catalog shares the root bucket with internal workspace storage (including DBFS root) but uses a dedicated bucket path prefix."
  },
  {
    "name": "root_bucket_info",
    "type": "object",
    "description": "The root bucket information for the storage configuration.",
    "children": [
      {
        "name": "bucket_name",
        "type": "string",
        "description": ""
      }
    ]
  }
]} />
</TabItem>
<TabItem value="storage_list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "storage_configuration_id",
    "type": "string",
    "description": "Databricks storage configuration ID."
  },
  {
    "name": "storage_configuration_name",
    "type": "string",
    "description": "The human-readable name of the storage configuration."
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the storage configuration was created."
  },
  {
    "name": "role_arn",
    "type": "string",
    "description": "Optional IAM role that is used to access the workspace catalog which is created during workspace creation for UC by Default. If a storage configuration with this field populated is used to create a workspace, then a workspace catalog is created together with the workspace. The workspace catalog shares the root bucket with internal workspace storage (including DBFS root) but uses a dedicated bucket path prefix."
  },
  {
    "name": "root_bucket_info",
    "type": "object",
    "description": "The root bucket information for the storage configuration.",
    "children": [
      {
        "name": "bucket_name",
        "type": "string",
        "description": ""
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
    <td><a href="#storage_get"><CopyableCode code="storage_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-storage_configuration_id"><code>storage_configuration_id</code></a></td>
    <td></td>
    <td>Gets a Databricks storage configuration for an account, both specified by ID.</td>
</tr>
<tr>
    <td><a href="#storage_list"><CopyableCode code="storage_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists Databricks storage configurations for an account, specified by ID.</td>
</tr>
<tr>
    <td><a href="#storage_create"><CopyableCode code="storage_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-data__storage_configuration_name"><code>data__storage_configuration_name</code></a>, <a href="#parameter-data__root_bucket_info"><code>data__root_bucket_info</code></a></td>
    <td></td>
    <td>Creates a Databricks storage configuration for an account.</td>
</tr>
<tr>
    <td><a href="#storage_delete"><CopyableCode code="storage_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-storage_configuration_id"><code>storage_configuration_id</code></a></td>
    <td></td>
    <td>Deletes a Databricks storage configuration. You cannot delete a storage configuration that is</td>
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
<tr id="parameter-storage_configuration_id">
    <td><CopyableCode code="storage_configuration_id" /></td>
    <td><code>string</code></td>
    <td>:returns: :class:`StorageConfiguration`</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="storage_get"
    values={[
        { label: 'storage_get', value: 'storage_get' },
        { label: 'storage_list', value: 'storage_list' }
    ]}
>
<TabItem value="storage_get">

Gets a Databricks storage configuration for an account, both specified by ID.

```sql
SELECT
account_id,
storage_configuration_id,
storage_configuration_name,
creation_time,
role_arn,
root_bucket_info
FROM databricks_account.provisioning.storage
WHERE account_id = '{{ account_id }}' -- required
AND storage_configuration_id = '{{ storage_configuration_id }}' -- required
;
```
</TabItem>
<TabItem value="storage_list">

Lists Databricks storage configurations for an account, specified by ID.

```sql
SELECT
account_id,
storage_configuration_id,
storage_configuration_name,
creation_time,
role_arn,
root_bucket_info
FROM databricks_account.provisioning.storage
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="storage_create"
    values={[
        { label: 'storage_create', value: 'storage_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="storage_create">

Creates a Databricks storage configuration for an account.

```sql
INSERT INTO databricks_account.provisioning.storage (
data__storage_configuration_name,
data__root_bucket_info,
data__role_arn,
account_id
)
SELECT 
'{{ storage_configuration_name }}' /* required */,
'{{ root_bucket_info }}' /* required */,
'{{ role_arn }}',
'{{ account_id }}'
RETURNING
account_id,
storage_configuration_id,
storage_configuration_name,
creation_time,
role_arn,
root_bucket_info
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: storage
  props:
    - name: account_id
      value: string
      description: Required parameter for the storage resource.
    - name: storage_configuration_name
      value: string
      description: |
        The human-readable name of the storage configuration.
    - name: root_bucket_info
      value: string
      description: |
        Root S3 bucket information.
    - name: role_arn
      value: string
      description: |
        Optional IAM role that is used to access the workspace catalog which is created during workspace creation for UC by Default. If a storage configuration with this field populated is used to create a workspace, then a workspace catalog is created together with the workspace. The workspace catalog shares the root bucket with internal workspace storage (including DBFS root) but uses a dedicated bucket path prefix.
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="storage_delete"
    values={[
        { label: 'storage_delete', value: 'storage_delete' }
    ]}
>
<TabItem value="storage_delete">

Deletes a Databricks storage configuration. You cannot delete a storage configuration that is

```sql
DELETE FROM databricks_account.provisioning.storage
WHERE account_id = '{{ account_id }}' --required
AND storage_configuration_id = '{{ storage_configuration_id }}' --required
;
```
</TabItem>
</Tabs>

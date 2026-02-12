---
title: private_access
hide_title: false
hide_table_of_contents: false
keywords:
  - private_access
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

Creates, updates, deletes, gets or lists a <code>private_access</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.private_access" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="private_access_get"
    values={[
        { label: 'private_access_get', value: 'private_access_get' },
        { label: 'private_access_list', value: 'private_access_list' }
    ]}
>
<TabItem value="private_access_get">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "The Databricks account ID that hosts the private access settings."
  },
  {
    "name": "private_access_settings_id",
    "type": "string",
    "description": "Databricks private access settings ID."
  },
  {
    "name": "private_access_settings_name",
    "type": "string",
    "description": "The human-readable name of the private access settings object."
  },
  {
    "name": "allowed_vpc_endpoint_ids",
    "type": "array",
    "description": "An array of Databricks VPC endpoint IDs. This is the Databricks ID that is returned when registering the VPC endpoint configuration in your Databricks account. This is not the ID of the VPC endpoint in AWS. Only used when private_access_level is set to ENDPOINT. This is an allow list of VPC endpoints that in your account that can connect to your workspace over AWS PrivateLink. If hybrid access to your workspace is enabled by setting public_access_enabled to true, this control only works for PrivateLink connections. To control how your workspace is accessed via public internet, see IP access lists."
  },
  {
    "name": "private_access_level",
    "type": "string",
    "description": "The private access level controls which VPC endpoints can connect to the UI or API of any workspace that attaches this private access settings object. `ACCOUNT` level access (the default) allows only VPC endpoints that are registered in your Databricks account connect to your workspace. `ENDPOINT` level access allows only specified VPC endpoints connect to your workspace. For details, see allowed_vpc_endpoint_ids."
  },
  {
    "name": "public_access_enabled",
    "type": "boolean",
    "description": "Determines if the workspace can be accessed over public internet. For fully private workspaces, you can optionally specify false, but only if you implement both the front-end and the back-end PrivateLink connections. Otherwise, specify true, which means that public access is enabled."
  },
  {
    "name": "region",
    "type": "string",
    "description": "The AWS region for workspaces attached to this private access settings object."
  }
]} />
</TabItem>
<TabItem value="private_access_list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "The Databricks account ID that hosts the private access settings."
  },
  {
    "name": "private_access_settings_id",
    "type": "string",
    "description": "Databricks private access settings ID."
  },
  {
    "name": "private_access_settings_name",
    "type": "string",
    "description": "The human-readable name of the private access settings object."
  },
  {
    "name": "allowed_vpc_endpoint_ids",
    "type": "array",
    "description": "An array of Databricks VPC endpoint IDs. This is the Databricks ID that is returned when registering the VPC endpoint configuration in your Databricks account. This is not the ID of the VPC endpoint in AWS. Only used when private_access_level is set to ENDPOINT. This is an allow list of VPC endpoints that in your account that can connect to your workspace over AWS PrivateLink. If hybrid access to your workspace is enabled by setting public_access_enabled to true, this control only works for PrivateLink connections. To control how your workspace is accessed via public internet, see IP access lists."
  },
  {
    "name": "private_access_level",
    "type": "string",
    "description": "The private access level controls which VPC endpoints can connect to the UI or API of any workspace that attaches this private access settings object. `ACCOUNT` level access (the default) allows only VPC endpoints that are registered in your Databricks account connect to your workspace. `ENDPOINT` level access allows only specified VPC endpoints connect to your workspace. For details, see allowed_vpc_endpoint_ids."
  },
  {
    "name": "public_access_enabled",
    "type": "boolean",
    "description": "Determines if the workspace can be accessed over public internet. For fully private workspaces, you can optionally specify false, but only if you implement both the front-end and the back-end PrivateLink connections. Otherwise, specify true, which means that public access is enabled."
  },
  {
    "name": "region",
    "type": "string",
    "description": "The AWS region for workspaces attached to this private access settings object."
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
    <td><a href="#private_access_get"><CopyableCode code="private_access_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-private_access_settings_id"><code>private_access_settings_id</code></a></td>
    <td></td>
    <td>Gets a Databricks private access settings configuration, both specified by ID.</td>
</tr>
<tr>
    <td><a href="#private_access_list"><CopyableCode code="private_access_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists Databricks private access settings for an account.</td>
</tr>
<tr>
    <td><a href="#private_access_create"><CopyableCode code="private_access_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a private access settings configuration, which represents network access restrictions for</td>
</tr>
<tr>
    <td><a href="#private_access_replace"><CopyableCode code="private_access_replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-private_access_settings_id"><code>private_access_settings_id</code></a>, <a href="#parameter-data__customer_facing_private_access_settings"><code>data__customer_facing_private_access_settings</code></a></td>
    <td></td>
    <td>Updates an existing private access settings object, which specifies how your workspace is accessed</td>
</tr>
<tr>
    <td><a href="#private_access_delete"><CopyableCode code="private_access_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-private_access_settings_id"><code>private_access_settings_id</code></a></td>
    <td></td>
    <td>Deletes a Databricks private access settings configuration, both specified by ID.</td>
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
<tr id="parameter-private_access_settings_id">
    <td><CopyableCode code="private_access_settings_id" /></td>
    <td><code>string</code></td>
    <td>:returns: :class:`PrivateAccessSettings`</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="private_access_get"
    values={[
        { label: 'private_access_get', value: 'private_access_get' },
        { label: 'private_access_list', value: 'private_access_list' }
    ]}
>
<TabItem value="private_access_get">

Gets a Databricks private access settings configuration, both specified by ID.

```sql
SELECT
account_id,
private_access_settings_id,
private_access_settings_name,
allowed_vpc_endpoint_ids,
private_access_level,
public_access_enabled,
region
FROM databricks_account.provisioning.private_access
WHERE account_id = '{{ account_id }}' -- required
AND private_access_settings_id = '{{ private_access_settings_id }}' -- required
;
```
</TabItem>
<TabItem value="private_access_list">

Lists Databricks private access settings for an account.

```sql
SELECT
account_id,
private_access_settings_id,
private_access_settings_name,
allowed_vpc_endpoint_ids,
private_access_level,
public_access_enabled,
region
FROM databricks_account.provisioning.private_access
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="private_access_create"
    values={[
        { label: 'private_access_create', value: 'private_access_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="private_access_create">

Creates a private access settings configuration, which represents network access restrictions for

```sql
INSERT INTO databricks_account.provisioning.private_access (
data__allowed_vpc_endpoint_ids,
data__private_access_level,
data__private_access_settings_name,
data__public_access_enabled,
data__region,
account_id
)
SELECT 
'{{ allowed_vpc_endpoint_ids }}',
'{{ private_access_level }}',
'{{ private_access_settings_name }}',
'{{ public_access_enabled }}',
'{{ region }}',
'{{ account_id }}'
RETURNING
account_id,
private_access_settings_id,
private_access_settings_name,
allowed_vpc_endpoint_ids,
private_access_level,
public_access_enabled,
region
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: private_access
  props:
    - name: account_id
      value: string
      description: Required parameter for the private_access resource.
    - name: allowed_vpc_endpoint_ids
      value: string
      description: |
        An array of Databricks VPC endpoint IDs. This is the Databricks ID returned when registering the VPC endpoint configuration in your Databricks account. This is not the ID of the VPC endpoint in AWS. Only used when private_access_level is set to ENDPOINT. This is an allow list of VPC endpoints registered in your Databricks account that can connect to your workspace over AWS PrivateLink. Note: If hybrid access to your workspace is enabled by setting public_access_enabled to true, this control only works for PrivateLink connections. To control how your workspace is accessed via public internet, see IP access lists.
    - name: private_access_level
      value: string
      description: |
        The private access level controls which VPC endpoints can connect to the UI or API of any workspace that attaches this private access settings object. `ACCOUNT` level access (the default) allows only VPC endpoints that are registered in your Databricks account connect to your workspace. `ENDPOINT` level access allows only specified VPC endpoints connect to your workspace. For details, see allowed_vpc_endpoint_ids.
    - name: private_access_settings_name
      value: string
      description: |
        The human-readable name of the private access settings object.
    - name: public_access_enabled
      value: string
      description: |
        Determines if the workspace can be accessed over public internet. For fully private workspaces, you can optionally specify false, but only if you implement both the front-end and the back-end PrivateLink connections. Otherwise, specify true, which means that public access is enabled.
    - name: region
      value: string
      description: |
        The AWS region for workspaces attached to this private access settings object.
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="private_access_replace"
    values={[
        { label: 'private_access_replace', value: 'private_access_replace' }
    ]}
>
<TabItem value="private_access_replace">

Updates an existing private access settings object, which specifies how your workspace is accessed

```sql
REPLACE databricks_account.provisioning.private_access
SET 
data__customer_facing_private_access_settings = '{{ customer_facing_private_access_settings }}'
WHERE 
account_id = '{{ account_id }}' --required
AND private_access_settings_id = '{{ private_access_settings_id }}' --required
AND data__customer_facing_private_access_settings = '{{ customer_facing_private_access_settings }}' --required
RETURNING
account_id,
private_access_settings_id,
private_access_settings_name,
allowed_vpc_endpoint_ids,
private_access_level,
public_access_enabled,
region;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="private_access_delete"
    values={[
        { label: 'private_access_delete', value: 'private_access_delete' }
    ]}
>
<TabItem value="private_access_delete">

Deletes a Databricks private access settings configuration, both specified by ID.

```sql
DELETE FROM databricks_account.provisioning.private_access
WHERE account_id = '{{ account_id }}' --required
AND private_access_settings_id = '{{ private_access_settings_id }}' --required
;
```
</TabItem>
</Tabs>

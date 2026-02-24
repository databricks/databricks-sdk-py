---
title: published_app_integration
hide_title: false
hide_table_of_contents: false
keywords:
  - published_app_integration
  - oauth2
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

Creates, updates, deletes, gets or lists a <code>published_app_integration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="published_app_integration" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.oauth2.published_app_integration" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="published_app_integration_get"
    values={[
        { label: 'published_app_integration_get', value: 'published_app_integration_get' },
        { label: 'published_app_integration_list', value: 'published_app_integration_list' }
    ]}
>
<TabItem value="published_app_integration_get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Display name of the published OAuth app"
  },
  {
    "name": "app_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "integration_id",
    "type": "string",
    "description": "Unique integration id for the published OAuth app"
  },
  {
    "name": "create_time",
    "type": "string",
    "description": ""
  },
  {
    "name": "created_by",
    "type": "integer",
    "description": ""
  },
  {
    "name": "token_access_policy",
    "type": "object",
    "description": "Token access policy",
    "children": [
      {
        "name": "absolute_session_lifetime_in_minutes",
        "type": "integer",
        "description": ""
      },
      {
        "name": "access_token_ttl_in_minutes",
        "type": "integer",
        "description": "access token time to live in minutes"
      },
      {
        "name": "enable_single_use_refresh_tokens",
        "type": "boolean",
        "description": "Whether to enable single-use refresh tokens (refresh token rotation). If this feature is enabled, upon successfully getting a new access token using a refresh token, Databricks will issue a new refresh token along with the access token in the response and invalidate the old refresh token. The client should use the new refresh token to get access tokens in future requests."
      },
      {
        "name": "refresh_token_ttl_in_minutes",
        "type": "integer",
        "description": "Refresh token time to live in minutes. When single-use refresh tokens are enabled, this represents the TTL of an individual refresh token. If the refresh token is used before it expires, a new one is issued with a renewed individual TTL."
      }
    ]
  }
]} />
</TabItem>
<TabItem value="published_app_integration_list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Display name of the published OAuth app"
  },
  {
    "name": "app_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "integration_id",
    "type": "string",
    "description": "Unique integration id for the published OAuth app"
  },
  {
    "name": "create_time",
    "type": "string",
    "description": ""
  },
  {
    "name": "created_by",
    "type": "integer",
    "description": ""
  },
  {
    "name": "token_access_policy",
    "type": "object",
    "description": "Token access policy",
    "children": [
      {
        "name": "absolute_session_lifetime_in_minutes",
        "type": "integer",
        "description": ""
      },
      {
        "name": "access_token_ttl_in_minutes",
        "type": "integer",
        "description": "access token time to live in minutes"
      },
      {
        "name": "enable_single_use_refresh_tokens",
        "type": "boolean",
        "description": "Whether to enable single-use refresh tokens (refresh token rotation). If this feature is enabled, upon successfully getting a new access token using a refresh token, Databricks will issue a new refresh token along with the access token in the response and invalidate the old refresh token. The client should use the new refresh token to get access tokens in future requests."
      },
      {
        "name": "refresh_token_ttl_in_minutes",
        "type": "integer",
        "description": "Refresh token time to live in minutes. When single-use refresh tokens are enabled, this represents the TTL of an individual refresh token. If the refresh token is used before it expires, a new one is issued with a renewed individual TTL."
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
    <td><a href="#published_app_integration_get"><CopyableCode code="published_app_integration_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a></td>
    <td></td>
    <td>Gets the Published OAuth App Integration for the given integration id.</td>
</tr>
<tr>
    <td><a href="#published_app_integration_list"><CopyableCode code="published_app_integration_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Get the list of published OAuth app integrations for the specified Databricks account</td>
</tr>
<tr>
    <td><a href="#published_app_integration_create"><CopyableCode code="published_app_integration_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Create Published OAuth App Integration.</td>
</tr>
<tr>
    <td><a href="#published_app_integration_update"><CopyableCode code="published_app_integration_update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a></td>
    <td></td>
    <td>Updates an existing published OAuth App Integration. You can retrieve the published OAuth app</td>
</tr>
<tr>
    <td><a href="#published_app_integration_delete"><CopyableCode code="published_app_integration_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a></td>
    <td></td>
    <td>Delete an existing Published OAuth App Integration. You can retrieve the published OAuth app</td>
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
<tr id="parameter-integration_id">
    <td><CopyableCode code="integration_id" /></td>
    <td><code>string</code></td>
    <td>str</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>:param page_token: str (optional)</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="published_app_integration_get"
    values={[
        { label: 'published_app_integration_get', value: 'published_app_integration_get' },
        { label: 'published_app_integration_list', value: 'published_app_integration_list' }
    ]}
>
<TabItem value="published_app_integration_get">

Gets the Published OAuth App Integration for the given integration id.

```sql
SELECT
name,
app_id,
integration_id,
create_time,
created_by,
token_access_policy
FROM databricks_account.oauth2.published_app_integration
WHERE account_id = '{{ account_id }}' -- required
AND integration_id = '{{ integration_id }}' -- required
;
```
</TabItem>
<TabItem value="published_app_integration_list">

Get the list of published OAuth app integrations for the specified Databricks account

```sql
SELECT
name,
app_id,
integration_id,
create_time,
created_by,
token_access_policy
FROM databricks_account.oauth2.published_app_integration
WHERE account_id = '{{ account_id }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="published_app_integration_create"
    values={[
        { label: 'published_app_integration_create', value: 'published_app_integration_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="published_app_integration_create">

Create Published OAuth App Integration.

```sql
INSERT INTO databricks_account.oauth2.published_app_integration (
app_id,
token_access_policy,
account_id
)
SELECT 
'{{ app_id }}',
'{{ token_access_policy }}',
'{{ account_id }}'
RETURNING
integration_id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: published_app_integration
  props:
    - name: account_id
      value: string
      description: Required parameter for the published_app_integration resource.
    - name: app_id
      value: string
      description: |
        App id of the OAuth published app integration. For example power-bi, tableau-deskop
    - name: token_access_policy
      value: object
      description: |
        Token access policy
      props:
      - name: absolute_session_lifetime_in_minutes
        value: integer
      - name: access_token_ttl_in_minutes
        value: integer
        description: |
          access token time to live in minutes
      - name: enable_single_use_refresh_tokens
        value: boolean
        description: |
          Whether to enable single-use refresh tokens (refresh token rotation). If this feature is enabled, upon successfully getting a new access token using a refresh token, Databricks will issue a new refresh token along with the access token in the response and invalidate the old refresh token. The client should use the new refresh token to get access tokens in future requests.
      - name: refresh_token_ttl_in_minutes
        value: integer
        description: |
          Refresh token time to live in minutes. When single-use refresh tokens are enabled, this represents the TTL of an individual refresh token. If the refresh token is used before it expires, a new one is issued with a renewed individual TTL.
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="published_app_integration_update"
    values={[
        { label: 'published_app_integration_update', value: 'published_app_integration_update' }
    ]}
>
<TabItem value="published_app_integration_update">

Updates an existing published OAuth App Integration. You can retrieve the published OAuth app

```sql
UPDATE databricks_account.oauth2.published_app_integration
SET 
token_access_policy = '{{ token_access_policy }}'
WHERE 
account_id = '{{ account_id }}' --required
AND integration_id = '{{ integration_id }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="published_app_integration_delete"
    values={[
        { label: 'published_app_integration_delete', value: 'published_app_integration_delete' }
    ]}
>
<TabItem value="published_app_integration_delete">

Delete an existing Published OAuth App Integration. You can retrieve the published OAuth app

```sql
DELETE FROM databricks_account.oauth2.published_app_integration
WHERE account_id = '{{ account_id }}' --required
AND integration_id = '{{ integration_id }}' --required
;
```
</TabItem>
</Tabs>

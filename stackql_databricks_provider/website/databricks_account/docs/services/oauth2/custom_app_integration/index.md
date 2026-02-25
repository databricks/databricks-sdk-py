---
title: custom_app_integration
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_app_integration
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>custom_app_integration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_app_integration" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.oauth2.custom_app_integration" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="custom_app_integration_get"
    values={[
        { label: 'custom_app_integration_get', value: 'custom_app_integration_get' },
        { label: 'custom_app_integration_list', value: 'custom_app_integration_list' }
    ]}
>
<TabItem value="custom_app_integration_get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The display name of the custom OAuth app"
  },
  {
    "name": "client_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "integration_id",
    "type": "string",
    "description": "ID of this custom app"
  },
  {
    "name": "confidential",
    "type": "boolean",
    "description": "This field indicates whether an OAuth client secret is required to authenticate this client."
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
    "name": "creator_username",
    "type": "string",
    "description": ""
  },
  {
    "name": "redirect_urls",
    "type": "array",
    "description": "List of OAuth redirect urls"
  },
  {
    "name": "scopes",
    "type": "array",
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
  },
  {
    "name": "user_authorized_scopes",
    "type": "array",
    "description": "Scopes that will need to be consented by end user to mint the access token. If the user does not authorize the access token will not be minted. Must be a subset of scopes."
  }
]} />
</TabItem>
<TabItem value="custom_app_integration_list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The display name of the custom OAuth app"
  },
  {
    "name": "client_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "integration_id",
    "type": "string",
    "description": "ID of this custom app"
  },
  {
    "name": "confidential",
    "type": "boolean",
    "description": "This field indicates whether an OAuth client secret is required to authenticate this client."
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
    "name": "creator_username",
    "type": "string",
    "description": ""
  },
  {
    "name": "redirect_urls",
    "type": "array",
    "description": "List of OAuth redirect urls"
  },
  {
    "name": "scopes",
    "type": "array",
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
  },
  {
    "name": "user_authorized_scopes",
    "type": "array",
    "description": "Scopes that will need to be consented by end user to mint the access token. If the user does not authorize the access token will not be minted. Must be a subset of scopes."
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
    <td><a href="#custom_app_integration_get"><CopyableCode code="custom_app_integration_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a></td>
    <td></td>
    <td>Gets the Custom OAuth App Integration for the given integration id.</td>
</tr>
<tr>
    <td><a href="#custom_app_integration_list"><CopyableCode code="custom_app_integration_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-include_creator_username"><code>include_creator_username</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Get the list of custom OAuth app integrations for the specified Databricks account</td>
</tr>
<tr>
    <td><a href="#custom_app_integration_create"><CopyableCode code="custom_app_integration_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Create Custom OAuth App Integration.</td>
</tr>
<tr>
    <td><a href="#custom_app_integration_update"><CopyableCode code="custom_app_integration_update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a></td>
    <td></td>
    <td>Updates an existing custom OAuth App Integration. You can retrieve the custom OAuth app integration</td>
</tr>
<tr>
    <td><a href="#custom_app_integration_delete"><CopyableCode code="custom_app_integration_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a></td>
    <td></td>
    <td>Delete an existing Custom OAuth App Integration. You can retrieve the custom OAuth app integration via</td>
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
<tr id="parameter-include_creator_username">
    <td><CopyableCode code="include_creator_username" /></td>
    <td><code>boolean</code></td>
    <td>:param page_size: int (optional)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>:returns: Iterator over :class:`GetCustomAppIntegrationOutput`</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="custom_app_integration_get"
    values={[
        { label: 'custom_app_integration_get', value: 'custom_app_integration_get' },
        { label: 'custom_app_integration_list', value: 'custom_app_integration_list' }
    ]}
>
<TabItem value="custom_app_integration_get">

Gets the Custom OAuth App Integration for the given integration id.

```sql
SELECT
name,
client_id,
integration_id,
confidential,
create_time,
created_by,
creator_username,
redirect_urls,
scopes,
token_access_policy,
user_authorized_scopes
FROM databricks_account.oauth2.custom_app_integration
WHERE account_id = '{{ account_id }}' -- required
AND integration_id = '{{ integration_id }}' -- required
;
```
</TabItem>
<TabItem value="custom_app_integration_list">

Get the list of custom OAuth app integrations for the specified Databricks account

```sql
SELECT
name,
client_id,
integration_id,
confidential,
create_time,
created_by,
creator_username,
redirect_urls,
scopes,
token_access_policy,
user_authorized_scopes
FROM databricks_account.oauth2.custom_app_integration
WHERE account_id = '{{ account_id }}' -- required
AND include_creator_username = '{{ include_creator_username }}'
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="custom_app_integration_create"
    values={[
        { label: 'custom_app_integration_create', value: 'custom_app_integration_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="custom_app_integration_create">

Create Custom OAuth App Integration.

```sql
INSERT INTO databricks_account.oauth2.custom_app_integration (
confidential,
name,
redirect_urls,
scopes,
token_access_policy,
user_authorized_scopes,
account_id
)
SELECT 
{{ confidential }},
'{{ name }}',
'{{ redirect_urls }}',
'{{ scopes }}',
'{{ token_access_policy }}',
'{{ user_authorized_scopes }}',
'{{ account_id }}'
RETURNING
client_id,
integration_id,
client_secret
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: custom_app_integration
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the custom_app_integration resource.
    - name: confidential
      value: {{ confidential }}
      description: |
        This field indicates whether an OAuth client secret is required to authenticate this client.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the custom OAuth app
    - name: redirect_urls
      value:
        - "{{ redirect_urls }}"
      description: |
        List of OAuth redirect urls
    - name: scopes
      value:
        - "{{ scopes }}"
      description: |
        OAuth scopes granted to the application. Supported scopes: all-apis, sql, offline_access, openid, profile, email.
    - name: token_access_policy
      description: |
        Token access policy
      value:
        absolute_session_lifetime_in_minutes: {{ absolute_session_lifetime_in_minutes }}
        access_token_ttl_in_minutes: {{ access_token_ttl_in_minutes }}
        enable_single_use_refresh_tokens: {{ enable_single_use_refresh_tokens }}
        refresh_token_ttl_in_minutes: {{ refresh_token_ttl_in_minutes }}
    - name: user_authorized_scopes
      value:
        - "{{ user_authorized_scopes }}"
      description: |
        Scopes that will need to be consented by end user to mint the access token. If the user does not authorize the access token will not be minted. Must be a subset of scopes.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="custom_app_integration_update"
    values={[
        { label: 'custom_app_integration_update', value: 'custom_app_integration_update' }
    ]}
>
<TabItem value="custom_app_integration_update">

Updates an existing custom OAuth App Integration. You can retrieve the custom OAuth app integration

```sql
UPDATE databricks_account.oauth2.custom_app_integration
SET 
redirect_urls = '{{ redirect_urls }}',
scopes = '{{ scopes }}',
token_access_policy = '{{ token_access_policy }}',
user_authorized_scopes = '{{ user_authorized_scopes }}'
WHERE 
account_id = '{{ account_id }}' --required
AND integration_id = '{{ integration_id }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="custom_app_integration_delete"
    values={[
        { label: 'custom_app_integration_delete', value: 'custom_app_integration_delete' }
    ]}
>
<TabItem value="custom_app_integration_delete">

Delete an existing Custom OAuth App Integration. You can retrieve the custom OAuth app integration via

```sql
DELETE FROM databricks_account.oauth2.custom_app_integration
WHERE account_id = '{{ account_id }}' --required
AND integration_id = '{{ integration_id }}' --required
;
```
</TabItem>
</Tabs>

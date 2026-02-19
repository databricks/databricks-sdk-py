---
title: vw_custom_app_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_custom_app_integrations
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

Creates, updates, deletes, gets or lists a <code>vw_custom_app_integrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_custom_app_integrations" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.oauth2.vw_custom_app_integrations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Databricks account ID used to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="integration_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the custom app integration.</td>
</tr>
<tr>
    <td><CopyableCode code="client_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>OAuth2 client ID issued for the custom app integration.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable name of the custom app integration.</td>
</tr>
<tr>
    <td><CopyableCode code="confidential" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether the app is a confidential client (can securely store a client secret).</td>
</tr>
<tr>
    <td><CopyableCode code="creator_username" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Username of the user who created the custom app integration.</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>ID of the user who created the custom app integration.</td>
</tr>
<tr>
    <td><CopyableCode code="create_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the integration was created (ISO 8601).</td>
</tr>
<tr>
    <td><CopyableCode code="redirect_urls" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of allowed OAuth2 redirect URLs for the app integration.</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of OAuth2 scopes the app integration is permitted to request.</td>
</tr>
<tr>
    <td><CopyableCode code="user_authorized_scopes" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of scopes that users have individually authorized for this app.</td>
</tr>
<tr>
    <td><CopyableCode code="access_token_ttl_minutes" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Time-to-live for access tokens issued to this app, in minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="refresh_token_ttl_minutes" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Time-to-live for refresh tokens issued to this app, in minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="session_lifetime_minutes" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Maximum absolute session lifetime for this app, in minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="single_use_refresh_tokens" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether refresh tokens are single-use (rotated on each use).</td>
</tr>
</tbody>
</table>

## Required Parameters

The following parameters are required by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Databricks account ID used to scope the query.</td>
</tr>
</tbody>
</table>

## `SELECT` Examples

```sql
SELECT
  account_id,
  integration_id,
  client_id,
  name,
  confidential,
  creator_username,
  created_by,
  create_time,
  redirect_urls,
  scopes,
  user_authorized_scopes,
  access_token_ttl_minutes,
  refresh_token_ttl_minutes,
  session_lifetime_minutes,
  single_use_refresh_tokens
FROM databricks_account.oauth2.vw_custom_app_integrations
WHERE account_id = '{{ account_id }}';
```

## SQL Definition

<Tabs
defaultValue="Sqlite3"
values={[
{ label: 'Sqlite3', value: 'Sqlite3' },
{ label: 'Postgres', value: 'Postgres' }
]}
>
<TabItem value="Sqlite3">

```sql
SELECT
  c.account_id,
  c.integration_id,
  c.client_id,
  c.name,
  c.confidential,
  c.creator_username,
  c.created_by,
  c.create_time,
  c.redirect_urls,
  c.scopes,
  c.user_authorized_scopes,
  JSON_EXTRACT(c.token_access_policy, '$.access_token_ttl_in_minutes') AS access_token_ttl_minutes,
  JSON_EXTRACT(c.token_access_policy, '$.refresh_token_ttl_in_minutes') AS refresh_token_ttl_minutes,
  JSON_EXTRACT(c.token_access_policy, '$.absolute_session_lifetime_in_minutes') AS session_lifetime_minutes,
  JSON_EXTRACT(c.token_access_policy, '$.enable_single_use_refresh_tokens') AS single_use_refresh_tokens
FROM databricks_account.oauth2.custom_app_integration c
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  c.account_id,
  c.integration_id,
  c.client_id,
  c.name,
  c.confidential,
  c.creator_username,
  c.created_by,
  c.create_time,
  c.redirect_urls,
  c.scopes,
  c.user_authorized_scopes,
  (c.token_access_policy->>'access_token_ttl_in_minutes')::integer AS access_token_ttl_minutes,
  (c.token_access_policy->>'refresh_token_ttl_in_minutes')::integer AS refresh_token_ttl_minutes,
  (c.token_access_policy->>'absolute_session_lifetime_in_minutes')::integer AS session_lifetime_minutes,
  (c.token_access_policy->>'enable_single_use_refresh_tokens')::boolean AS single_use_refresh_tokens
FROM databricks_account.oauth2.custom_app_integration c
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

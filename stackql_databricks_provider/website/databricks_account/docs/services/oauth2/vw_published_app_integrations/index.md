---
title: vw_published_app_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_published_app_integrations
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

Creates, updates, deletes, gets or lists a <code>vw_published_app_integrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_published_app_integrations" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.oauth2.vw_published_app_integrations" /></td></tr>
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
    <td>Unique identifier for the published app integration.</td>
</tr>
<tr>
    <td><CopyableCode code="app_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the published app (matches integration_id for published apps).</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable name of the published app (e.g. Tableau, Power BI, Databricks CLI).</td>
</tr>
<tr>
    <td><CopyableCode code="create_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the integration was enabled on this account (ISO 8601).</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>ID of the user who enabled this published app integration (0 for system-created).</td>
</tr>
<tr>
    <td><CopyableCode code="access_token_ttl_minutes" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Time-to-live for access tokens issued to this app, in minutes (typically 60).</td>
</tr>
<tr>
    <td><CopyableCode code="refresh_token_ttl_minutes" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Time-to-live for refresh tokens issued to this app, in minutes (typically 10080 - 7 days).</td>
</tr>
<tr>
    <td><CopyableCode code="session_lifetime_minutes" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Maximum absolute session lifetime for this app, in minutes (e.g. 129600 = 90 days, 525600 = 1 year).</td>
</tr>
<tr>
    <td><CopyableCode code="single_use_refresh_tokens" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether refresh tokens are single-use and rotated on each use (1 = true, 0 = false).</td>
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
  app_id,
  name,
  create_time,
  created_by,
  access_token_ttl_minutes,
  refresh_token_ttl_minutes,
  session_lifetime_minutes,
  single_use_refresh_tokens
FROM databricks_account.oauth2.vw_published_app_integrations
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
  p.account_id,
  p.integration_id,
  p.app_id,
  p.name,
  p.create_time,
  p.created_by,
  JSON_EXTRACT(p.token_access_policy, '$.access_token_ttl_in_minutes') AS access_token_ttl_minutes,
  JSON_EXTRACT(p.token_access_policy, '$.refresh_token_ttl_in_minutes') AS refresh_token_ttl_minutes,
  JSON_EXTRACT(p.token_access_policy, '$.absolute_session_lifetime_in_minutes') AS session_lifetime_minutes,
  JSON_EXTRACT(p.token_access_policy, '$.enable_single_use_refresh_tokens') AS single_use_refresh_tokens
FROM databricks_account.oauth2.published_app_integration p
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  p.account_id,
  p.integration_id,
  p.app_id,
  p.name,
  p.create_time,
  p.created_by,
  (p.token_access_policy->>'access_token_ttl_in_minutes')::integer AS access_token_ttl_minutes,
  (p.token_access_policy->>'refresh_token_ttl_in_minutes')::integer AS refresh_token_ttl_minutes,
  (p.token_access_policy->>'absolute_session_lifetime_in_minutes')::integer AS session_lifetime_minutes,
  (p.token_access_policy->>'enable_single_use_refresh_tokens')::boolean AS single_use_refresh_tokens
FROM databricks_account.oauth2.published_app_integration p
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

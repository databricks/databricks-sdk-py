---
title: oauth_published_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - oauth_published_apps
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

Creates, updates, deletes, gets or lists an <code>oauth_published_apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="oauth_published_apps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.oauth2.oauth_published_apps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="oauth_published_apps_list"
    values={[
        { label: 'oauth_published_apps_list', value: 'oauth_published_apps_list' }
    ]}
>
<TabItem value="oauth_published_apps_list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The display name of the published OAuth app."
  },
  {
    "name": "app_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "client_id",
    "type": "string",
    "description": "Client ID of the published OAuth app. It is the client_id in the OAuth flow"
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of the published OAuth app."
  },
  {
    "name": "is_confidential_client",
    "type": "boolean",
    "description": "Whether the published OAuth app is a confidential client. It is always false for published OAuth apps."
  },
  {
    "name": "redirect_urls",
    "type": "array",
    "description": "Redirect URLs of the published OAuth app."
  },
  {
    "name": "scopes",
    "type": "array",
    "description": "Required scopes for the published OAuth app."
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
    <td><a href="#oauth_published_apps_list"><CopyableCode code="oauth_published_apps_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Get all the available published OAuth apps in Databricks.</td>
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
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The max number of OAuth published apps to return in one page.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A token that can be used to get the next page of results.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="oauth_published_apps_list"
    values={[
        { label: 'oauth_published_apps_list', value: 'oauth_published_apps_list' }
    ]}
>
<TabItem value="oauth_published_apps_list">

Get all the available published OAuth apps in Databricks.

```sql
SELECT
name,
app_id,
client_id,
description,
is_confidential_client,
redirect_urls,
scopes
FROM databricks_account.oauth2.oauth_published_apps
WHERE account_id = '{{ account_id }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>

---
title: account_user_preferences_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - account_user_preferences_metadata
  - settingsv2
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

Creates, updates, deletes, gets or lists an <code>account_user_preferences_metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="account_user_preferences_metadata" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settingsv2.account_user_preferences_metadata" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_account_user_preferences_metadata"
    values={[
        { label: 'list_account_user_preferences_metadata', value: 'list_account_user_preferences_metadata' }
    ]}
>
<TabItem value="list_account_user_preferences_metadata">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of the setting."
  },
  {
    "name": "description",
    "type": "string",
    "description": ""
  },
  {
    "name": "docs_link",
    "type": "string",
    "description": "Link to databricks documentation for the setting"
  },
  {
    "name": "type",
    "type": "string",
    "description": "Sample message depicting the type of the setting. To set this setting, the value sent must match this type."
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
    <td><a href="#list_account_user_preferences_metadata"><CopyableCode code="list_account_user_preferences_metadata" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-user_id"><code>user_id</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List valid user preferences and their metadata for a specific user. User preferences are personal</td>
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
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>User ID of the user whose settings metadata is being retrieved.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of settings to return. The service may return fewer than this value. If unspecified, at most 200 settings will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous `ListAccountUserPreferencesMetadataRequest` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAccountUserPreferencesMetadataRequest` must match the call that provided the page token.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_account_user_preferences_metadata"
    values={[
        { label: 'list_account_user_preferences_metadata', value: 'list_account_user_preferences_metadata' }
    ]}
>
<TabItem value="list_account_user_preferences_metadata">

List valid user preferences and their metadata for a specific user. User preferences are personal

```sql
SELECT
name,
description,
docs_link,
type
FROM databricks_account.settingsv2.account_user_preferences_metadata
WHERE account_id = '{{ account_id }}' -- required
AND user_id = '{{ user_id }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>

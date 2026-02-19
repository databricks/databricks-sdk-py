---
title: notification_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_destinations
  - settings
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>notification_destinations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="notification_destinations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settings.notification_destinations" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": "UUID identifying notification destination."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "The display name for the notification destination."
  },
  {
    "name": "config",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "email",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "addresses",
            "type": "array",
            "description": ""
          }
        ]
      },
      {
        "name": "generic_webhook",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "password",
            "type": "string",
            "description": ""
          },
          {
            "name": "password_set",
            "type": "boolean",
            "description": "[Output-Only] Whether password is set."
          },
          {
            "name": "url",
            "type": "string",
            "description": "[Input-Only] URL for webhook."
          },
          {
            "name": "url_set",
            "type": "boolean",
            "description": "[Output-Only] Whether URL is set."
          },
          {
            "name": "username",
            "type": "string",
            "description": "[Input-Only][Optional] Username for webhook."
          },
          {
            "name": "username_set",
            "type": "boolean",
            "description": "[Output-Only] Whether username is set."
          }
        ]
      },
      {
        "name": "microsoft_teams",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "app_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "app_id_set",
            "type": "boolean",
            "description": "[Output-Only] Whether App ID is set."
          },
          {
            "name": "auth_secret",
            "type": "string",
            "description": "[Input-Only] Secret for Microsoft Teams App authentication."
          },
          {
            "name": "auth_secret_set",
            "type": "boolean",
            "description": "[Output-Only] Whether secret is set."
          },
          {
            "name": "channel_url",
            "type": "string",
            "description": "[Input-Only] Channel URL for Microsoft Teams App."
          },
          {
            "name": "channel_url_set",
            "type": "boolean",
            "description": "[Output-Only] Whether Channel URL is set."
          },
          {
            "name": "tenant_id",
            "type": "string",
            "description": "[Input-Only] Tenant ID for Microsoft Teams App."
          },
          {
            "name": "tenant_id_set",
            "type": "boolean",
            "description": "[Output-Only] Whether Tenant ID is set."
          },
          {
            "name": "url",
            "type": "string",
            "description": "[Input-Only] URL for Microsoft Teams webhook."
          },
          {
            "name": "url_set",
            "type": "boolean",
            "description": "[Output-Only] Whether URL is set."
          }
        ]
      },
      {
        "name": "pagerduty",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "integration_key",
            "type": "string",
            "description": ""
          },
          {
            "name": "integration_key_set",
            "type": "boolean",
            "description": "[Output-Only] Whether integration key is set."
          }
        ]
      },
      {
        "name": "slack",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "channel_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "channel_id_set",
            "type": "boolean",
            "description": "[Output-Only] Whether channel ID is set."
          },
          {
            "name": "oauth_token",
            "type": "string",
            "description": "[Input-Only] OAuth token for Slack authentication."
          },
          {
            "name": "oauth_token_set",
            "type": "boolean",
            "description": "[Output-Only] Whether OAuth token is set."
          },
          {
            "name": "url",
            "type": "string",
            "description": "[Input-Only] URL for Slack destination."
          },
          {
            "name": "url_set",
            "type": "boolean",
            "description": "[Output-Only] Whether URL is set."
          }
        ]
      }
    ]
  },
  {
    "name": "destination_type",
    "type": "string",
    "description": "[Output-only] The type of the notification destination. The type can not be changed once set. (EMAIL, MICROSOFT_TEAMS, PAGERDUTY, SLACK, WEBHOOK)"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "UUID identifying notification destination."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "The display name for the notification destination."
  },
  {
    "name": "destination_type",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EMAIL, MICROSOFT_TEAMS, PAGERDUTY, SLACK, WEBHOOK)"
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a notification destination.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists notification destinations.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a notification destination. Requires workspace admin permissions.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates a notification destination. Requires workspace admin permissions. At least one field is</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a notification destination. Requires workspace admin permissions.</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>str</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a notification destination.

```sql
SELECT
id,
display_name,
config,
destination_type
FROM databricks_workspace.settings.notification_destinations
WHERE id = '{{ id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists notification destinations.

```sql
SELECT
id,
display_name,
destination_type
FROM databricks_workspace.settings.notification_destinations
WHERE deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
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

Creates a notification destination. Requires workspace admin permissions.

```sql
INSERT INTO databricks_workspace.settings.notification_destinations (
config,
display_name,
deployment_name
)
SELECT 
'{{ config }}',
'{{ display_name }}',
'{{ deployment_name }}'
RETURNING
id,
display_name,
config,
destination_type
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: notification_destinations
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the notification_destinations resource.
    - name: config
      value: string
      description: |
        The configuration for the notification destination. Must wrap EXACTLY one of the nested configs.
    - name: display_name
      value: string
      description: |
        The display name for the notification destination.
```
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

Updates a notification destination. Requires workspace admin permissions. At least one field is

```sql
UPDATE databricks_workspace.settings.notification_destinations
SET 
config = '{{ config }}',
display_name = '{{ display_name }}'
WHERE 
id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
id,
display_name,
config,
destination_type;
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

Deletes a notification destination. Requires workspace admin permissions.

```sql
DELETE FROM databricks_workspace.settings.notification_destinations
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

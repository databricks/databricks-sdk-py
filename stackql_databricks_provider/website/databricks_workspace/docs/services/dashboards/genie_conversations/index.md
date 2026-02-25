---
title: genie_conversations
hide_title: false
hide_table_of_contents: false
keywords:
  - genie_conversations
  - dashboards
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>genie_conversations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="genie_conversations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dashboards.genie_conversations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "conversations",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "conversation_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "title",
        "type": "string",
        "description": ""
      },
      {
        "name": "created_timestamp",
        "type": "integer",
        "description": ""
      }
    ]
  },
  {
    "name": "next_page_token",
    "type": "string",
    "description": "Token to get the next page of results"
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-include_all"><code>include_all</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Get a list of conversations in a Genie Space.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Delete a conversation.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-content"><code>content</code></a></td>
    <td></td>
    <td>Start a new conversation.</td>
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
<tr id="parameter-conversation_id">
    <td><CopyableCode code="conversation_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the conversation to delete.</td>
</tr>
<tr id="parameter-space_id">
    <td><CopyableCode code="space_id" /></td>
    <td><code>string</code></td>
    <td>The ID associated with the Genie space where you want to start a conversation.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-include_all">
    <td><CopyableCode code="include_all" /></td>
    <td><code>boolean</code></td>
    <td>Include all conversations in the space across all users. Requires at least CAN MANAGE permission on the space.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of conversations to return per page</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Token to get the next page of results</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Get a list of conversations in a Genie Space.

```sql
SELECT
conversations,
next_page_token
FROM databricks_workspace.dashboards.genie_conversations
WHERE space_id = '{{ space_id }}' -- required
AND workspace = '{{ workspace }}' -- required
AND include_all = '{{ include_all }}'
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
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

Delete a conversation.

```sql
DELETE FROM databricks_workspace.dashboards.genie_conversations
WHERE space_id = '{{ space_id }}' --required
AND conversation_id = '{{ conversation_id }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' }
    ]}
>
<TabItem value="start">

Start a new conversation.

```sql
EXEC databricks_workspace.dashboards.genie_conversations.start 
@space_id='{{ space_id }}' --required, 
@workspace='{{ workspace }}' --required 
@@json=
'{
"content": "{{ content }}"
}'
;
```
</TabItem>
</Tabs>

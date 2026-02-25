---
title: genie_message_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - genie_message_attachments
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

Creates, updates, deletes, gets or lists a <code>genie_message_attachments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="genie_message_attachments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dashboards.genie_message_attachments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_query_result"
    values={[
        { label: 'get_query_result', value: 'get_query_result' }
    ]}
>
<TabItem value="get_query_result">

<SchemaTable fields={[
  {
    "name": "statement_response",
    "type": "string",
    "description": ""
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
    <td><a href="#get_query_result"><CopyableCode code="get_query_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-attachment_id"><code>attachment_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Get the result of SQL query if the message has a query attachment. This is only available if a message</td>
</tr>
<tr>
    <td><a href="#execute_attachment_query"><CopyableCode code="execute_attachment_query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-attachment_id"><code>attachment_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Execute the SQL for a message query attachment. Use this API when the query attachment has expired and</td>
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
<tr id="parameter-attachment_id">
    <td><CopyableCode code="attachment_id" /></td>
    <td><code>string</code></td>
    <td>Attachment ID</td>
</tr>
<tr id="parameter-conversation_id">
    <td><CopyableCode code="conversation_id" /></td>
    <td><code>string</code></td>
    <td>Conversation ID</td>
</tr>
<tr id="parameter-message_id">
    <td><CopyableCode code="message_id" /></td>
    <td><code>string</code></td>
    <td>Message ID</td>
</tr>
<tr id="parameter-space_id">
    <td><CopyableCode code="space_id" /></td>
    <td><code>string</code></td>
    <td>Genie space ID</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_query_result"
    values={[
        { label: 'get_query_result', value: 'get_query_result' }
    ]}
>
<TabItem value="get_query_result">

Get the result of SQL query if the message has a query attachment. This is only available if a message

```sql
SELECT
statement_response
FROM databricks_workspace.dashboards.genie_message_attachments
WHERE space_id = '{{ space_id }}' -- required
AND conversation_id = '{{ conversation_id }}' -- required
AND message_id = '{{ message_id }}' -- required
AND attachment_id = '{{ attachment_id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="execute_attachment_query"
    values={[
        { label: 'execute_attachment_query', value: 'execute_attachment_query' }
    ]}
>
<TabItem value="execute_attachment_query">

Execute the SQL for a message query attachment. Use this API when the query attachment has expired and

```sql
EXEC databricks_workspace.dashboards.genie_message_attachments.execute_attachment_query 
@space_id='{{ space_id }}' --required, 
@conversation_id='{{ conversation_id }}' --required, 
@message_id='{{ message_id }}' --required, 
@attachment_id='{{ attachment_id }}' --required, 
@workspace='{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

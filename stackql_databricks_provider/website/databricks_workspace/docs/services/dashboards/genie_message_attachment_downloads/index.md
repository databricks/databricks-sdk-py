---
title: genie_message_attachment_downloads
hide_title: false
hide_table_of_contents: false
keywords:
  - genie_message_attachment_downloads
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>genie_message_attachment_downloads</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="genie_message_attachment_downloads" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dashboards.genie_message_attachment_downloads" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_download"
    values={[
        { label: 'get_download', value: 'get_download' }
    ]}
>
<TabItem value="get_download">

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
    <td><a href="#get_download"><CopyableCode code="get_download" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-attachment_id"><code>attachment_id</code></a>, <a href="#parameter-download_id"><code>download_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-download_id_signature"><code>download_id_signature</code></a></td>
    <td>After [Generating a Full Query Result Download](:method:genie/generatedownloadfullqueryresult) and</td>
</tr>
<tr>
    <td><a href="#generate_download"><CopyableCode code="generate_download" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-attachment_id"><code>attachment_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Initiates a new SQL execution and returns a `download_id` and `download_id_signature` that you can use</td>
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
<tr id="parameter-download_id">
    <td><CopyableCode code="download_id" /></td>
    <td><code>string</code></td>
    <td>Download ID. This ID is provided by the [Generate Download endpoint](:method:genie/generateDownloadFullQueryResult)</td>
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
<tr id="parameter-download_id_signature">
    <td><CopyableCode code="download_id_signature" /></td>
    <td><code>string</code></td>
    <td>JWT signature for the download_id to ensure secure access to query results</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_download"
    values={[
        { label: 'get_download', value: 'get_download' }
    ]}
>
<TabItem value="get_download">

After [Generating a Full Query Result Download](:method:genie/generatedownloadfullqueryresult) and

```sql
SELECT
statement_response
FROM databricks_workspace.dashboards.genie_message_attachment_downloads
WHERE space_id = '{{ space_id }}' -- required
AND conversation_id = '{{ conversation_id }}' -- required
AND message_id = '{{ message_id }}' -- required
AND attachment_id = '{{ attachment_id }}' -- required
AND download_id = '{{ download_id }}' -- required
AND workspace = '{{ workspace }}' -- required
AND download_id_signature = '{{ download_id_signature }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="generate_download"
    values={[
        { label: 'generate_download', value: 'generate_download' }
    ]}
>
<TabItem value="generate_download">

Initiates a new SQL execution and returns a `download_id` and `download_id_signature` that you can use

```sql
EXEC databricks_workspace.dashboards.genie_message_attachment_downloads.generate_download 
@space_id='{{ space_id }}' --required, 
@conversation_id='{{ conversation_id }}' --required, 
@message_id='{{ message_id }}' --required, 
@attachment_id='{{ attachment_id }}' --required, 
@workspace='{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

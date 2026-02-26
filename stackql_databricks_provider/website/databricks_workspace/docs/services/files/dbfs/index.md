---
title: dbfs
hide_title: false
hide_table_of_contents: false
keywords:
  - dbfs
  - files
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

Creates, updates, deletes, gets or lists a <code>dbfs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dbfs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.files.dbfs" /></td></tr>
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
    "name": "file_size",
    "type": "integer",
    "description": ""
  },
  {
    "name": "is_dir",
    "type": "boolean",
    "description": "True if the path is a directory."
  },
  {
    "name": "modification_time",
    "type": "integer",
    "description": "Last modification time of given file in milliseconds since epoch."
  },
  {
    "name": "path",
    "type": "string",
    "description": "The absolute path of the file or directory."
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
    <td><a href="#parameter-path"><code>path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>List the contents of a directory, or details of the file. If the file or directory does not exist,</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Opens a stream to write to a file and returns a handle to this stream. There is a 10 minute idle</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete the file or directory (optionally recursively delete all files in the directory). This call</td>
</tr>
<tr>
    <td><a href="#add_block"><CopyableCode code="add_block" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-handle"><code>handle</code></a>, <a href="#parameter-data"><code>data</code></a></td>
    <td></td>
    <td>Appends a block of data to the stream specified by the input handle. If the handle does not exist,</td>
</tr>
<tr>
    <td><a href="#close"><CopyableCode code="close" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-handle"><code>handle</code></a></td>
    <td></td>
    <td>Closes the stream specified by the input handle. If the handle does not exist, this call throws an</td>
</tr>
<tr>
    <td><a href="#get_status"><CopyableCode code="get_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-path"><code>path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the file information for a file or directory. If the file or directory does not exist, this call</td>
</tr>
<tr>
    <td><a href="#mkdirs"><CopyableCode code="mkdirs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Creates the given directory and necessary parent directories if they do not exist. If a file (not a</td>
</tr>
<tr>
    <td><a href="#move"><CopyableCode code="move" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-source_path"><code>source_path</code></a>, <a href="#parameter-destination_path"><code>destination_path</code></a></td>
    <td></td>
    <td>Moves a file from one location to another location within DBFS. If the source file does not exist,</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Uploads a file through the use of multipart form post. It is mainly used for streaming uploads, but</td>
</tr>
<tr>
    <td><a href="#read"><CopyableCode code="read" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-path"><code>path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-length"><code>length</code></a>, <a href="#parameter-offset"><code>offset</code></a></td>
    <td>Returns the contents of a file. If the file does not exist, this call throws an exception with</td>
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
<tr id="parameter-path">
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>The path of the file to read. The path should be the absolute DBFS path.</td>
</tr>
<tr id="parameter-length">
    <td><CopyableCode code="length" /></td>
    <td><code>integer</code></td>
    <td>The number of bytes to read starting from the offset. This has a limit of 1 MB, and a default value of 0.5 MB.</td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>integer</code></td>
    <td>The offset to read from in bytes.</td>
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

List the contents of a directory, or details of the file. If the file or directory does not exist,

```sql
SELECT
file_size,
is_dir,
modification_time,
path
FROM databricks_workspace.files.dbfs
WHERE path = '{{ path }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
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

Opens a stream to write to a file and returns a handle to this stream. There is a 10 minute idle

```sql
INSERT INTO databricks_workspace.files.dbfs (
path,
overwrite,
deployment_name
)
SELECT 
'{{ path }}' /* required */,
{{ overwrite }},
'{{ deployment_name }}'
RETURNING
handle
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: dbfs
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the dbfs resource.
    - name: path
      value: "{{ path }}"
      description: |
        The path of the new file. The path should be the absolute DBFS path.
    - name: overwrite
      value: {{ overwrite }}
      description: |
        The flag that specifies whether to overwrite existing file/files.
`}</CodeBlock>

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

Delete the file or directory (optionally recursively delete all files in the directory). This call

```sql
DELETE FROM databricks_workspace.files.dbfs
WHERE deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="add_block"
    values={[
        { label: 'add_block', value: 'add_block' },
        { label: 'close', value: 'close' },
        { label: 'get_status', value: 'get_status' },
        { label: 'mkdirs', value: 'mkdirs' },
        { label: 'move', value: 'move' },
        { label: 'put', value: 'put' },
        { label: 'read', value: 'read' }
    ]}
>
<TabItem value="add_block">

Appends a block of data to the stream specified by the input handle. If the handle does not exist,

```sql
EXEC databricks_workspace.files.dbfs.add_block 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"handle": {{ handle }}, 
"data": "{{ data }}"
}'
;
```
</TabItem>
<TabItem value="close">

Closes the stream specified by the input handle. If the handle does not exist, this call throws an

```sql
EXEC databricks_workspace.files.dbfs.close 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"handle": {{ handle }}
}'
;
```
</TabItem>
<TabItem value="get_status">

Gets the file information for a file or directory. If the file or directory does not exist, this call

```sql
EXEC databricks_workspace.files.dbfs.get_status 
@path='{{ path }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="mkdirs">

Creates the given directory and necessary parent directories if they do not exist. If a file (not a

```sql
EXEC databricks_workspace.files.dbfs.mkdirs 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"path": "{{ path }}"
}'
;
```
</TabItem>
<TabItem value="move">

Moves a file from one location to another location within DBFS. If the source file does not exist,

```sql
EXEC databricks_workspace.files.dbfs.move 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"source_path": "{{ source_path }}", 
"destination_path": "{{ destination_path }}"
}'
;
```
</TabItem>
<TabItem value="put">

Uploads a file through the use of multipart form post. It is mainly used for streaming uploads, but

```sql
EXEC databricks_workspace.files.dbfs.put 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"path": "{{ path }}", 
"contents": "{{ contents }}", 
"overwrite": {{ overwrite }}
}'
;
```
</TabItem>
<TabItem value="read">

Returns the contents of a file. If the file does not exist, this call throws an exception with

```sql
EXEC databricks_workspace.files.dbfs.read 
@path='{{ path }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@length='{{ length }}', 
@offset='{{ offset }}'
;
```
</TabItem>
</Tabs>

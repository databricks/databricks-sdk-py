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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>dbfs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dbfs</code></td></tr>
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
    <td>List the contents of a directory, or details of the file. If the file or directory does not exist,<br />this call throws an exception with `RESOURCE_DOES_NOT_EXIST`.<br /><br />When calling list on a large directory, the list operation will time out after approximately 60<br />seconds. We strongly recommend using list only on directories containing less than 10K files and<br />discourage using the DBFS REST API for operations that list more than 10K files. Instead, we recommend<br />that you perform such operations in the context of a cluster, using the [File system utility<br />(dbutils.fs)](/dev-tools/databricks-utils.html#dbutils-fs), which provides the same functionality<br />without timing out.<br /><br />:param path: str<br />  The path of the file or directory. The path should be the absolute DBFS path.<br /><br />:returns: Iterator over :class:`FileInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__path"><code>data__path</code></a></td>
    <td></td>
    <td>Opens a stream to write to a file and returns a handle to this stream. There is a 10 minute idle<br />timeout on this handle. If a file or directory already exists on the given path and __overwrite__ is<br />set to false, this call will throw an exception with ``RESOURCE_ALREADY_EXISTS``.<br /><br />A typical workflow for file upload would be:<br /><br />1. Issue a ``create`` call and get a handle. 2. Issue one or more ``add-block`` calls with the handle<br />you have. 3. Issue a ``close`` call with the handle you have.<br /><br />:param path: str<br />  The path of the new file. The path should be the absolute DBFS path.<br />:param overwrite: bool (optional)<br />  The flag that specifies whether to overwrite existing file/files.<br /><br />:returns: :class:`CreateResponse`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete the file or directory (optionally recursively delete all files in the directory). This call<br />throws an exception with `IO_ERROR` if the path is a non-empty directory and `recursive` is set to<br />`false` or on other similar errors.<br /><br />When you delete a large number of files, the delete operation is done in increments. The call returns<br />a response after approximately 45 seconds with an error message (503 Service Unavailable) asking you<br />to re-invoke the delete operation until the directory structure is fully deleted.<br /><br />For operations that delete more than 10K files, we discourage using the DBFS REST API, but advise you<br />to perform such operations in the context of a cluster, using the [File system utility<br />(dbutils.fs)](/dev-tools/databricks-utils.html#dbutils-fs). `dbutils.fs` covers the functional scope<br />of the DBFS REST API, but from notebooks. Running such operations using notebooks provides better<br />control and manageability, such as selective deletes, and the possibility to automate periodic delete<br />jobs.<br /><br />:param path: str<br />  The path of the file or directory to delete. The path should be the absolute DBFS path.<br />:param recursive: bool (optional)<br />  Whether or not to recursively delete the directory's contents. Deleting empty directories can be<br />  done without providing the recursive flag.</td>
</tr>
<tr>
    <td><a href="#add_block"><CopyableCode code="add_block" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-handle"><code>handle</code></a>, <a href="#parameter-data"><code>data</code></a></td>
    <td></td>
    <td>Appends a block of data to the stream specified by the input handle. If the handle does not exist,<br />this call will throw an exception with ``RESOURCE_DOES_NOT_EXIST``.<br /><br />If the block of data exceeds 1 MB, this call will throw an exception with ``MAX_BLOCK_SIZE_EXCEEDED``.<br /><br />:param handle: int<br />  The handle on an open stream.<br />:param data: str<br />  The base64-encoded data to append to the stream. This has a limit of 1 MB.</td>
</tr>
<tr>
    <td><a href="#close"><CopyableCode code="close" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-handle"><code>handle</code></a></td>
    <td></td>
    <td>Closes the stream specified by the input handle. If the handle does not exist, this call throws an<br />exception with ``RESOURCE_DOES_NOT_EXIST``.<br /><br />:param handle: int<br />  The handle on an open stream.</td>
</tr>
<tr>
    <td><a href="#get_status"><CopyableCode code="get_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-path"><code>path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the file information for a file or directory. If the file or directory does not exist, this call<br />throws an exception with `RESOURCE_DOES_NOT_EXIST`.<br /><br />:param path: str<br />  The path of the file or directory. The path should be the absolute DBFS path.<br /><br />:returns: :class:`FileInfo`</td>
</tr>
<tr>
    <td><a href="#mkdirs"><CopyableCode code="mkdirs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Creates the given directory and necessary parent directories if they do not exist. If a file (not a<br />directory) exists at any prefix of the input path, this call throws an exception with<br />`RESOURCE_ALREADY_EXISTS`. **Note**: If this operation fails, it might have succeeded in creating some<br />of the necessary parent directories.<br /><br />:param path: str<br />  The path of the new directory. The path should be the absolute DBFS path.</td>
</tr>
<tr>
    <td><a href="#move"><CopyableCode code="move" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-source_path"><code>source_path</code></a>, <a href="#parameter-destination_path"><code>destination_path</code></a></td>
    <td></td>
    <td>Moves a file from one location to another location within DBFS. If the source file does not exist,<br />this call throws an exception with `RESOURCE_DOES_NOT_EXIST`. If a file already exists in the<br />destination path, this call throws an exception with `RESOURCE_ALREADY_EXISTS`. If the given source<br />path is a directory, this call always recursively moves all files.<br /><br />:param source_path: str<br />  The source path of the file or directory. The path should be the absolute DBFS path.<br />:param destination_path: str<br />  The destination path of the file or directory. The path should be the absolute DBFS path.</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Uploads a file through the use of multipart form post. It is mainly used for streaming uploads, but<br />can also be used as a convenient single call for data upload.<br /><br />Alternatively you can pass contents as base64 string.<br /><br />The amount of data that can be passed (when not streaming) using the __contents__ parameter is limited<br />to 1 MB. `MAX_BLOCK_SIZE_EXCEEDED` will be thrown if this limit is exceeded.<br /><br />If you want to upload large files, use the streaming upload. For details, see :method:dbfs/create,<br />:method:dbfs/addBlock, :method:dbfs/close.<br /><br />:param path: str<br />  The path of the new file. The path should be the absolute DBFS path.<br />:param contents: str (optional)<br />  This parameter might be absent, and instead a posted file will be used.<br />:param overwrite: bool (optional)<br />  The flag that specifies whether to overwrite existing file/files.</td>
</tr>
<tr>
    <td><a href="#read"><CopyableCode code="read" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-path"><code>path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-length"><code>length</code></a>, <a href="#parameter-offset"><code>offset</code></a></td>
    <td>Returns the contents of a file. If the file does not exist, this call throws an exception with<br />`RESOURCE_DOES_NOT_EXIST`. If the path is a directory, the read length is negative, or if the offset<br />is negative, this call throws an exception with `INVALID_PARAMETER_VALUE`. If the read length exceeds<br />1 MB, this call throws an exception with `MAX_READ_SIZE_EXCEEDED`.<br /><br />If `offset + length` exceeds the number of bytes in a file, it reads the contents until the end of<br />file.<br /><br />:param path: str<br />  The path of the file to read. The path should be the absolute DBFS path.<br />:param length: int (optional)<br />  The number of bytes to read starting from the offset. This has a limit of 1 MB, and a default value<br />  of 0.5 MB.<br />:param offset: int (optional)<br />  The offset to read from in bytes.<br /><br />:returns: :class:`ReadResponse`</td>
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
    <td><code>string</code></td>
    <td>The number of bytes to read starting from the offset. This has a limit of 1 MB, and a default value of 0.5 MB.</td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>string</code></td>
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

List the contents of a directory, or details of the file. If the file or directory does not exist,<br />this call throws an exception with `RESOURCE_DOES_NOT_EXIST`.<br /><br />When calling list on a large directory, the list operation will time out after approximately 60<br />seconds. We strongly recommend using list only on directories containing less than 10K files and<br />discourage using the DBFS REST API for operations that list more than 10K files. Instead, we recommend<br />that you perform such operations in the context of a cluster, using the [File system utility<br />(dbutils.fs)](/dev-tools/databricks-utils.html#dbutils-fs), which provides the same functionality<br />without timing out.<br /><br />:param path: str<br />  The path of the file or directory. The path should be the absolute DBFS path.<br /><br />:returns: Iterator over :class:`FileInfo`

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

Opens a stream to write to a file and returns a handle to this stream. There is a 10 minute idle<br />timeout on this handle. If a file or directory already exists on the given path and __overwrite__ is<br />set to false, this call will throw an exception with ``RESOURCE_ALREADY_EXISTS``.<br /><br />A typical workflow for file upload would be:<br /><br />1. Issue a ``create`` call and get a handle. 2. Issue one or more ``add-block`` calls with the handle<br />you have. 3. Issue a ``close`` call with the handle you have.<br /><br />:param path: str<br />  The path of the new file. The path should be the absolute DBFS path.<br />:param overwrite: bool (optional)<br />  The flag that specifies whether to overwrite existing file/files.<br /><br />:returns: :class:`CreateResponse`

```sql
INSERT INTO databricks_workspace.files.dbfs (
data__path,
data__overwrite,
deployment_name
)
SELECT 
'{{ path }}' /* required */,
'{{ overwrite }}',
'{{ deployment_name }}'
RETURNING
handle
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: dbfs
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the dbfs resource.
    - name: path
      value: string
      description: |
        The path of the new file. The path should be the absolute DBFS path.
    - name: overwrite
      value: string
      description: |
        The flag that specifies whether to overwrite existing file/files.
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

Delete the file or directory (optionally recursively delete all files in the directory). This call<br />throws an exception with `IO_ERROR` if the path is a non-empty directory and `recursive` is set to<br />`false` or on other similar errors.<br /><br />When you delete a large number of files, the delete operation is done in increments. The call returns<br />a response after approximately 45 seconds with an error message (503 Service Unavailable) asking you<br />to re-invoke the delete operation until the directory structure is fully deleted.<br /><br />For operations that delete more than 10K files, we discourage using the DBFS REST API, but advise you<br />to perform such operations in the context of a cluster, using the [File system utility<br />(dbutils.fs)](/dev-tools/databricks-utils.html#dbutils-fs). `dbutils.fs` covers the functional scope<br />of the DBFS REST API, but from notebooks. Running such operations using notebooks provides better<br />control and manageability, such as selective deletes, and the possibility to automate periodic delete<br />jobs.<br /><br />:param path: str<br />  The path of the file or directory to delete. The path should be the absolute DBFS path.<br />:param recursive: bool (optional)<br />  Whether or not to recursively delete the directory's contents. Deleting empty directories can be<br />  done without providing the recursive flag.

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

Appends a block of data to the stream specified by the input handle. If the handle does not exist,<br />this call will throw an exception with ``RESOURCE_DOES_NOT_EXIST``.<br /><br />If the block of data exceeds 1 MB, this call will throw an exception with ``MAX_BLOCK_SIZE_EXCEEDED``.<br /><br />:param handle: int<br />  The handle on an open stream.<br />:param data: str<br />  The base64-encoded data to append to the stream. This has a limit of 1 MB.

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

Closes the stream specified by the input handle. If the handle does not exist, this call throws an<br />exception with ``RESOURCE_DOES_NOT_EXIST``.<br /><br />:param handle: int<br />  The handle on an open stream.

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

Gets the file information for a file or directory. If the file or directory does not exist, this call<br />throws an exception with `RESOURCE_DOES_NOT_EXIST`.<br /><br />:param path: str<br />  The path of the file or directory. The path should be the absolute DBFS path.<br /><br />:returns: :class:`FileInfo`

```sql
EXEC databricks_workspace.files.dbfs.get_status 
@path='{{ path }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="mkdirs">

Creates the given directory and necessary parent directories if they do not exist. If a file (not a<br />directory) exists at any prefix of the input path, this call throws an exception with<br />`RESOURCE_ALREADY_EXISTS`. **Note**: If this operation fails, it might have succeeded in creating some<br />of the necessary parent directories.<br /><br />:param path: str<br />  The path of the new directory. The path should be the absolute DBFS path.

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

Moves a file from one location to another location within DBFS. If the source file does not exist,<br />this call throws an exception with `RESOURCE_DOES_NOT_EXIST`. If a file already exists in the<br />destination path, this call throws an exception with `RESOURCE_ALREADY_EXISTS`. If the given source<br />path is a directory, this call always recursively moves all files.<br /><br />:param source_path: str<br />  The source path of the file or directory. The path should be the absolute DBFS path.<br />:param destination_path: str<br />  The destination path of the file or directory. The path should be the absolute DBFS path.

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

Uploads a file through the use of multipart form post. It is mainly used for streaming uploads, but<br />can also be used as a convenient single call for data upload.<br /><br />Alternatively you can pass contents as base64 string.<br /><br />The amount of data that can be passed (when not streaming) using the __contents__ parameter is limited<br />to 1 MB. `MAX_BLOCK_SIZE_EXCEEDED` will be thrown if this limit is exceeded.<br /><br />If you want to upload large files, use the streaming upload. For details, see :method:dbfs/create,<br />:method:dbfs/addBlock, :method:dbfs/close.<br /><br />:param path: str<br />  The path of the new file. The path should be the absolute DBFS path.<br />:param contents: str (optional)<br />  This parameter might be absent, and instead a posted file will be used.<br />:param overwrite: bool (optional)<br />  The flag that specifies whether to overwrite existing file/files.

```sql
EXEC databricks_workspace.files.dbfs.put 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"path": "{{ path }}", 
"contents": "{{ contents }}", 
"overwrite": "{{ overwrite }}"
}'
;
```
</TabItem>
<TabItem value="read">

Returns the contents of a file. If the file does not exist, this call throws an exception with<br />`RESOURCE_DOES_NOT_EXIST`. If the path is a directory, the read length is negative, or if the offset<br />is negative, this call throws an exception with `INVALID_PARAMETER_VALUE`. If the read length exceeds<br />1 MB, this call throws an exception with `MAX_READ_SIZE_EXCEEDED`.<br /><br />If `offset + length` exceeds the number of bytes in a file, it reads the contents until the end of<br />file.<br /><br />:param path: str<br />  The path of the file to read. The path should be the absolute DBFS path.<br />:param length: int (optional)<br />  The number of bytes to read starting from the offset. This has a limit of 1 MB, and a default value<br />  of 0.5 MB.<br />:param offset: int (optional)<br />  The offset to read from in bytes.<br /><br />:returns: :class:`ReadResponse`

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

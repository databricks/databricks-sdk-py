---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
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

Creates, updates, deletes, gets or lists a <code>files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.files.files" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_directory_contents"
    values={[
        { label: 'list_directory_contents', value: 'list_directory_contents' },
        { label: 'download', value: 'download' }
    ]}
>
<TabItem value="list_directory_contents">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the file or directory. This is the last component of the path."
  },
  {
    "name": "file_size",
    "type": "integer",
    "description": ""
  },
  {
    "name": "is_directory",
    "type": "boolean",
    "description": "True if the path is a directory."
  },
  {
    "name": "last_modified",
    "type": "integer",
    "description": "Last modification time of given file in milliseconds since unix epoch."
  },
  {
    "name": "path",
    "type": "string",
    "description": "The absolute path of the file or directory."
  }
]} />
</TabItem>
<TabItem value="download">

<SchemaTable fields={[
  {
    "name": "content_length",
    "type": "integer",
    "description": ""
  },
  {
    "name": "content_type",
    "type": "string",
    "description": ""
  },
  {
    "name": "contents",
    "type": "string (binary)",
    "description": ""
  },
  {
    "name": "last_modified",
    "type": "string",
    "description": "The last modified time of the file in HTTP-date (RFC 7231) format."
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
    <td><a href="#list_directory_contents"><CopyableCode code="list_directory_contents" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-directory_path"><code>directory_path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns the contents of a directory. If there is no directory at the specified path, the API returns a<br />HTTP 404 error.<br /><br />:param directory_path: str<br />  The absolute path of a directory.<br />:param page_size: int (optional)<br />  The maximum number of directory entries to return. The response may contain fewer entries. If the<br />  response contains a `next_page_token`, there may be more entries, even if fewer than `page_size`<br />  entries are in the response.<br /><br />  We recommend not to set this value unless you are intentionally listing less than the complete<br />  directory contents.<br /><br />  If unspecified, at most 1000 directory entries will be returned. The maximum value is 1000. Values<br />  above 1000 will be coerced to 1000.<br />:param page_token: str (optional)<br />  An opaque page token which was the `next_page_token` in the response of the previous request to list<br />  the contents of this directory. Provide this token to retrieve the next page of directory entries.<br />  When providing a `page_token`, all other parameters provided to the request must match the previous<br />  request. To list all of the entries in a directory, it is necessary to continue requesting pages of<br />  entries until the response contains no `next_page_token`. Note that the number of entries returned<br />  must not be used to determine when the listing is complete.<br /><br />:returns: Iterator over :class:`DirectoryEntry`</td>
</tr>
<tr>
    <td><a href="#download"><CopyableCode code="download" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-file_path"><code>file_path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Downloads a file. The file contents are the response body. This is a standard HTTP file download, not<br />a JSON RPC. It supports the Range and If-Unmodified-Since HTTP headers.<br /><br />:param file_path: str<br />  The absolute path of the file.<br /><br />:returns: :class:`DownloadResponse`</td>
</tr>
<tr>
    <td><a href="#create_directory"><CopyableCode code="create_directory" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-directory_path"><code>directory_path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates an empty directory. If necessary, also creates any parent directories of the new, empty<br />directory (like the shell command `mkdir -p`). If called on an existing directory, returns a success<br />response; this method is idempotent (it will succeed if the directory already exists).<br /><br />:param directory_path: str<br />  The absolute path of a directory.</td>
</tr>
<tr>
    <td><a href="#upload"><CopyableCode code="upload" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-file_path"><code>file_path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__contents"><code>data__contents</code></a></td>
    <td><a href="#parameter-overwrite"><code>overwrite</code></a></td>
    <td>Uploads a file of up to 5 GiB. The file contents should be sent as the request body as raw bytes (an<br />octet stream); do not encode or otherwise modify the bytes before sending. The contents of the<br />resulting file will be exactly the bytes sent in the request body. If the request is successful, there<br />is no response body.<br /><br />:param file_path: str<br />  The absolute path of the file.<br />:param contents: BinaryIO<br />:param overwrite: bool (optional)<br />  If true or unspecified, an existing file will be overwritten. If false, an error will be returned if<br />  the path points to an existing file.</td>
</tr>
<tr>
    <td><a href="#delete_directory"><CopyableCode code="delete_directory" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-directory_path"><code>directory_path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes an empty directory.<br /><br />To delete a non-empty directory, first delete all of its contents. This can be done by listing the<br />directory contents and deleting each file and subdirectory recursively.<br /><br />:param directory_path: str<br />  The absolute path of a directory.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-file_path"><code>file_path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a file. If the request is successful, there is no response body.<br /><br />:param file_path: str<br />  The absolute path of the file.</td>
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
<tr id="parameter-directory_path">
    <td><CopyableCode code="directory_path" /></td>
    <td><code>string</code></td>
    <td>The absolute path of a directory.</td>
</tr>
<tr id="parameter-file_path">
    <td><CopyableCode code="file_path" /></td>
    <td><code>string</code></td>
    <td>The absolute path of the file.</td>
</tr>
<tr id="parameter-overwrite">
    <td><CopyableCode code="overwrite" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>The maximum number of directory entries to return. The response may contain fewer entries. If the response contains a `next_page_token`, there may be more entries, even if fewer than `page_size` entries are in the response. We recommend not to set this value unless you are intentionally listing less than the complete directory contents. If unspecified, at most 1000 directory entries will be returned. The maximum value is 1000. Values above 1000 will be coerced to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>An opaque page token which was the `next_page_token` in the response of the previous request to list the contents of this directory. Provide this token to retrieve the next page of directory entries. When providing a `page_token`, all other parameters provided to the request must match the previous request. To list all of the entries in a directory, it is necessary to continue requesting pages of entries until the response contains no `next_page_token`. Note that the number of entries returned must not be used to determine when the listing is complete.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_directory_contents"
    values={[
        { label: 'list_directory_contents', value: 'list_directory_contents' },
        { label: 'download', value: 'download' }
    ]}
>
<TabItem value="list_directory_contents">

Returns the contents of a directory. If there is no directory at the specified path, the API returns a<br />HTTP 404 error.<br /><br />:param directory_path: str<br />  The absolute path of a directory.<br />:param page_size: int (optional)<br />  The maximum number of directory entries to return. The response may contain fewer entries. If the<br />  response contains a `next_page_token`, there may be more entries, even if fewer than `page_size`<br />  entries are in the response.<br /><br />  We recommend not to set this value unless you are intentionally listing less than the complete<br />  directory contents.<br /><br />  If unspecified, at most 1000 directory entries will be returned. The maximum value is 1000. Values<br />  above 1000 will be coerced to 1000.<br />:param page_token: str (optional)<br />  An opaque page token which was the `next_page_token` in the response of the previous request to list<br />  the contents of this directory. Provide this token to retrieve the next page of directory entries.<br />  When providing a `page_token`, all other parameters provided to the request must match the previous<br />  request. To list all of the entries in a directory, it is necessary to continue requesting pages of<br />  entries until the response contains no `next_page_token`. Note that the number of entries returned<br />  must not be used to determine when the listing is complete.<br /><br />:returns: Iterator over :class:`DirectoryEntry`

```sql
SELECT
name,
file_size,
is_directory,
last_modified,
path
FROM databricks_workspace.files.files
WHERE directory_path = '{{ directory_path }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="download">

Downloads a file. The file contents are the response body. This is a standard HTTP file download, not<br />a JSON RPC. It supports the Range and If-Unmodified-Since HTTP headers.<br /><br />:param file_path: str<br />  The absolute path of the file.<br /><br />:returns: :class:`DownloadResponse`

```sql
SELECT
content_length,
content_type,
contents,
last_modified
FROM databricks_workspace.files.files
WHERE file_path = '{{ file_path }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_directory"
    values={[
        { label: 'create_directory', value: 'create_directory' },
        { label: 'upload', value: 'upload' }
    ]}
>
<TabItem value="create_directory">

Creates an empty directory. If necessary, also creates any parent directories of the new, empty<br />directory (like the shell command `mkdir -p`). If called on an existing directory, returns a success<br />response; this method is idempotent (it will succeed if the directory already exists).<br /><br />:param directory_path: str<br />  The absolute path of a directory.

```sql
REPLACE databricks_workspace.files.files
SET 
-- No updatable properties
WHERE 
directory_path = '{{ directory_path }}' --required
AND deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
<TabItem value="upload">

Uploads a file of up to 5 GiB. The file contents should be sent as the request body as raw bytes (an<br />octet stream); do not encode or otherwise modify the bytes before sending. The contents of the<br />resulting file will be exactly the bytes sent in the request body. If the request is successful, there<br />is no response body.<br /><br />:param file_path: str<br />  The absolute path of the file.<br />:param contents: BinaryIO<br />:param overwrite: bool (optional)<br />  If true or unspecified, an existing file will be overwritten. If false, an error will be returned if<br />  the path points to an existing file.

```sql
REPLACE databricks_workspace.files.files
SET 
data__contents = '{{ contents }}'
WHERE 
file_path = '{{ file_path }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__contents = '{{ contents }}' --required
AND overwrite = '{{ overwrite}}';
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_directory"
    values={[
        { label: 'delete_directory', value: 'delete_directory' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_directory">

Deletes an empty directory.<br /><br />To delete a non-empty directory, first delete all of its contents. This can be done by listing the<br />directory contents and deleting each file and subdirectory recursively.<br /><br />:param directory_path: str<br />  The absolute path of a directory.

```sql
DELETE FROM databricks_workspace.files.files
WHERE directory_path = '{{ directory_path }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes a file. If the request is successful, there is no response body.<br /><br />:param file_path: str<br />  The absolute path of the file.

```sql
DELETE FROM databricks_workspace.files.files
WHERE file_path = '{{ file_path }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

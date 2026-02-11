---
title: workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace
  - workspace
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

Creates, updates, deletes, gets or lists a <code>workspace</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.workspace" /></td></tr>
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
    "name": "object_id",
    "type": "integer",
    "description": "Unique identifier for the object."
  },
  {
    "name": "resource_id",
    "type": "string",
    "description": "A unique identifier for the object that is consistent across all Databricks APIs."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Only applicable to files. The creation UTC timestamp."
  },
  {
    "name": "language",
    "type": "string",
    "description": "The language of the object. This value is set only if the object type is ``NOTEBOOK``."
  },
  {
    "name": "modified_at",
    "type": "integer",
    "description": "Only applicable to files, the last modified UTC timestamp."
  },
  {
    "name": "object_type",
    "type": "string",
    "description": "The type of the object in workspace. - `NOTEBOOK`: document that contains runnable code, visualizations, and explanatory text. - `DIRECTORY`: directory - `LIBRARY`: library - `FILE`: file - `REPO`: repository - `DASHBOARD`: Lakeview dashboard"
  },
  {
    "name": "path",
    "type": "string",
    "description": "The absolute path of the object."
  },
  {
    "name": "size",
    "type": "integer",
    "description": "Only applicable to files. The file size in bytes can be returned."
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
    <td><a href="#parameter-notebooks_modified_after"><code>notebooks_modified_after</code></a></td>
    <td>Lists the contents of a directory, or the object if it is not a directory. If the input path does not<br />exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`.<br /><br />:param path: str<br />  The absolute path of the notebook or directory.<br />:param notebooks_modified_after: int (optional)<br />  UTC timestamp in milliseconds<br /><br />:returns: Iterator over :class:`ObjectInfo`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Deletes an object or a directory (and optionally recursively deletes all objects in the directory). *<br />If `path` does not exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`. * If `path` is a<br />non-empty directory and `recursive` is set to `false`, this call returns an error<br />`DIRECTORY_NOT_EMPTY`.<br /><br />Object deletion cannot be undone and deleting a directory recursively is not atomic.<br /><br />:param path: str<br />  The absolute path of the notebook or directory.<br />:param recursive: bool (optional)<br />  The flag that specifies whether to delete the object recursively. It is `false` by default. Please<br />  note this deleting directory is not atomic. If it fails in the middle, some of objects under this<br />  directory may be deleted and cannot be undone.</td>
</tr>
<tr>
    <td><a href="#export"><CopyableCode code="export" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-path"><code>path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-format"><code>format</code></a></td>
    <td>Exports an object or the contents of an entire directory.<br /><br />If `path` does not exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`.<br /><br />If the exported data would exceed size limit, this call returns `MAX_NOTEBOOK_SIZE_EXCEEDED`.<br />Currently, this API does not support exporting a library.<br /><br />:param path: str<br />  The absolute path of the object or directory. Exporting a directory is only supported for the `DBC`,<br />  `SOURCE`, and `AUTO` format.<br />:param format: :class:`ExportFormat` (optional)<br />  This specifies the format of the exported file. By default, this is `SOURCE`.<br /><br />  The value is case sensitive.<br /><br />  - `SOURCE`: The notebook is exported as source code. Directory exports will not include non-notebook<br />  entries. - `HTML`: The notebook is exported as an HTML file. - `JUPYTER`: The notebook is exported<br />  as a Jupyter/IPython Notebook file. - `DBC`: The notebook is exported in Databricks archive format.<br />  Directory exports will not include non-notebook entries. - `R_MARKDOWN`: The notebook is exported to<br />  R Markdown format. - `AUTO`: The object or directory is exported depending on the objects type.<br />  Directory exports will include notebooks and workspace files.<br /><br />:returns: :class:`ExportResponse`</td>
</tr>
<tr>
    <td><a href="#import"><CopyableCode code="import" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Imports a workspace object (for example, a notebook or file) or the contents of an entire directory.<br />If `path` already exists and `overwrite` is set to `false`, this call returns an error<br />`RESOURCE_ALREADY_EXISTS`. To import a directory, you can use either the `DBC` format or the `SOURCE`<br />format with the `language` field unset. To import a single file as `SOURCE`, you must set the<br />`language` field. Zip files within directories are not supported.<br /><br />:param path: str<br />  The absolute path of the object or directory. Importing a directory is only supported for the `DBC`<br />  and `SOURCE` formats.<br />:param content: str (optional)<br />  The base64-encoded content. This has a limit of 10 MB.<br /><br />  If the limit (10MB) is exceeded, exception with error code **MAX_NOTEBOOK_SIZE_EXCEEDED** is thrown.<br />  This parameter might be absent, and instead a posted file is used.<br />:param format: :class:`ImportFormat` (optional)<br />  This specifies the format of the file to be imported.<br /><br />  The value is case sensitive.<br /><br />  - `AUTO`: The item is imported depending on an analysis of the item's extension and the header<br />  content provided in the request. If the item is imported as a notebook, then the item's extension is<br />  automatically removed. - `SOURCE`: The notebook or directory is imported as source code. - `HTML`:<br />  The notebook is imported as an HTML file. - `JUPYTER`: The notebook is imported as a Jupyter/IPython<br />  Notebook file. - `DBC`: The notebook is imported in Databricks archive format. Required for<br />  directories. - `R_MARKDOWN`: The notebook is imported from R Markdown format.<br />:param language: :class:`Language` (optional)<br />  The language of the object. This value is set only if the object type is `NOTEBOOK`.<br />:param overwrite: bool (optional)<br />  The flag that specifies whether to overwrite existing object. It is `false` by default. For `DBC`<br />  format, `overwrite` is not supported since it may contain a directory.</td>
</tr>
<tr>
    <td><a href="#mkdirs"><CopyableCode code="mkdirs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Creates the specified directory (and necessary parent directories if they do not exist). If there is<br />an object (not a directory) at any prefix of the input path, this call returns an error<br />`RESOURCE_ALREADY_EXISTS`.<br /><br />Note that if this operation fails it may have succeeded in creating some of the necessary parent<br />directories.<br /><br />:param path: str<br />  The absolute path of the directory. If the parent directories do not exist, it will also create<br />  them. If the directory already exists, this command will do nothing and succeed.</td>
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
    <td>The absolute path of the object or directory. Exporting a directory is only supported for the `DBC`, `SOURCE`, and `AUTO` format.</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>This specifies the format of the exported file. By default, this is `SOURCE`. The value is case sensitive. - `SOURCE`: The notebook is exported as source code. Directory exports will not include non-notebook entries. - `HTML`: The notebook is exported as an HTML file. - `JUPYTER`: The notebook is exported as a Jupyter/IPython Notebook file. - `DBC`: The notebook is exported in Databricks archive format. Directory exports will not include non-notebook entries. - `R_MARKDOWN`: The notebook is exported to R Markdown format. - `AUTO`: The object or directory is exported depending on the objects type. Directory exports will include notebooks and workspace files.</td>
</tr>
<tr id="parameter-notebooks_modified_after">
    <td><CopyableCode code="notebooks_modified_after" /></td>
    <td><code>string</code></td>
    <td>UTC timestamp in milliseconds</td>
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

Lists the contents of a directory, or the object if it is not a directory. If the input path does not<br />exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`.<br /><br />:param path: str<br />  The absolute path of the notebook or directory.<br />:param notebooks_modified_after: int (optional)<br />  UTC timestamp in milliseconds<br /><br />:returns: Iterator over :class:`ObjectInfo`

```sql
SELECT
object_id,
resource_id,
created_at,
language,
modified_at,
object_type,
path,
size
FROM databricks_workspace.workspace.workspace
WHERE path = '{{ path }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND notebooks_modified_after = '{{ notebooks_modified_after }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'export', value: 'export' },
        { label: 'import', value: 'import' },
        { label: 'mkdirs', value: 'mkdirs' }
    ]}
>
<TabItem value="delete">

Deletes an object or a directory (and optionally recursively deletes all objects in the directory). *<br />If `path` does not exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`. * If `path` is a<br />non-empty directory and `recursive` is set to `false`, this call returns an error<br />`DIRECTORY_NOT_EMPTY`.<br /><br />Object deletion cannot be undone and deleting a directory recursively is not atomic.<br /><br />:param path: str<br />  The absolute path of the notebook or directory.<br />:param recursive: bool (optional)<br />  The flag that specifies whether to delete the object recursively. It is `false` by default. Please<br />  note this deleting directory is not atomic. If it fails in the middle, some of objects under this<br />  directory may be deleted and cannot be undone.

```sql
EXEC databricks_workspace.workspace.workspace.delete 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"path": "{{ path }}", 
"recursive": "{{ recursive }}"
}'
;
```
</TabItem>
<TabItem value="export">

Exports an object or the contents of an entire directory.<br /><br />If `path` does not exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`.<br /><br />If the exported data would exceed size limit, this call returns `MAX_NOTEBOOK_SIZE_EXCEEDED`.<br />Currently, this API does not support exporting a library.<br /><br />:param path: str<br />  The absolute path of the object or directory. Exporting a directory is only supported for the `DBC`,<br />  `SOURCE`, and `AUTO` format.<br />:param format: :class:`ExportFormat` (optional)<br />  This specifies the format of the exported file. By default, this is `SOURCE`.<br /><br />  The value is case sensitive.<br /><br />  - `SOURCE`: The notebook is exported as source code. Directory exports will not include non-notebook<br />  entries. - `HTML`: The notebook is exported as an HTML file. - `JUPYTER`: The notebook is exported<br />  as a Jupyter/IPython Notebook file. - `DBC`: The notebook is exported in Databricks archive format.<br />  Directory exports will not include non-notebook entries. - `R_MARKDOWN`: The notebook is exported to<br />  R Markdown format. - `AUTO`: The object or directory is exported depending on the objects type.<br />  Directory exports will include notebooks and workspace files.<br /><br />:returns: :class:`ExportResponse`

```sql
EXEC databricks_workspace.workspace.workspace.export 
@path='{{ path }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@format='{{ format }}'
;
```
</TabItem>
<TabItem value="import">

Imports a workspace object (for example, a notebook or file) or the contents of an entire directory.<br />If `path` already exists and `overwrite` is set to `false`, this call returns an error<br />`RESOURCE_ALREADY_EXISTS`. To import a directory, you can use either the `DBC` format or the `SOURCE`<br />format with the `language` field unset. To import a single file as `SOURCE`, you must set the<br />`language` field. Zip files within directories are not supported.<br /><br />:param path: str<br />  The absolute path of the object or directory. Importing a directory is only supported for the `DBC`<br />  and `SOURCE` formats.<br />:param content: str (optional)<br />  The base64-encoded content. This has a limit of 10 MB.<br /><br />  If the limit (10MB) is exceeded, exception with error code **MAX_NOTEBOOK_SIZE_EXCEEDED** is thrown.<br />  This parameter might be absent, and instead a posted file is used.<br />:param format: :class:`ImportFormat` (optional)<br />  This specifies the format of the file to be imported.<br /><br />  The value is case sensitive.<br /><br />  - `AUTO`: The item is imported depending on an analysis of the item's extension and the header<br />  content provided in the request. If the item is imported as a notebook, then the item's extension is<br />  automatically removed. - `SOURCE`: The notebook or directory is imported as source code. - `HTML`:<br />  The notebook is imported as an HTML file. - `JUPYTER`: The notebook is imported as a Jupyter/IPython<br />  Notebook file. - `DBC`: The notebook is imported in Databricks archive format. Required for<br />  directories. - `R_MARKDOWN`: The notebook is imported from R Markdown format.<br />:param language: :class:`Language` (optional)<br />  The language of the object. This value is set only if the object type is `NOTEBOOK`.<br />:param overwrite: bool (optional)<br />  The flag that specifies whether to overwrite existing object. It is `false` by default. For `DBC`<br />  format, `overwrite` is not supported since it may contain a directory.

```sql
EXEC databricks_workspace.workspace.workspace.import 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"path": "{{ path }}", 
"content": "{{ content }}", 
"format": "{{ format }}", 
"language": "{{ language }}", 
"overwrite": "{{ overwrite }}"
}'
;
```
</TabItem>
<TabItem value="mkdirs">

Creates the specified directory (and necessary parent directories if they do not exist). If there is<br />an object (not a directory) at any prefix of the input path, this call returns an error<br />`RESOURCE_ALREADY_EXISTS`.<br /><br />Note that if this operation fails it may have succeeded in creating some of the necessary parent<br />directories.<br /><br />:param path: str<br />  The absolute path of the directory. If the parent directories do not exist, it will also create<br />  them. If the directory already exists, this command will do nothing and succeed.

```sql
EXEC databricks_workspace.workspace.workspace.mkdirs 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"path": "{{ path }}"
}'
;
```
</TabItem>
</Tabs>

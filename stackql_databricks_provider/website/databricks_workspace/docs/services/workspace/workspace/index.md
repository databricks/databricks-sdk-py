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
<tr><td><b>Name</b></td><td><CopyableCode code="workspace" /></td></tr>
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
    "description": "The language of the object. This value is set only if the object type is ``NOTEBOOK``. (PYTHON, R, SCALA, SQL)"
  },
  {
    "name": "modified_at",
    "type": "integer",
    "description": "Only applicable to files, the last modified UTC timestamp."
  },
  {
    "name": "object_type",
    "type": "string",
    "description": "The type of the object in workspace. - `NOTEBOOK`: document that contains runnable code, visualizations, and explanatory text. - `DIRECTORY`: directory - `LIBRARY`: library - `FILE`: file - `REPO`: repository - `DASHBOARD`: Lakeview dashboard (DASHBOARD, DIRECTORY, FILE, LIBRARY, NOTEBOOK, REPO)"
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
    <td>Lists the contents of a directory, or the object if it is not a directory. If the input path does not</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Deletes an object or a directory (and optionally recursively deletes all objects in the directory). *</td>
</tr>
<tr>
    <td><a href="#export"><CopyableCode code="export" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-path"><code>path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-format"><code>format</code></a></td>
    <td>Exports an object or the contents of an entire directory.</td>
</tr>
<tr>
    <td><a href="#import"><CopyableCode code="import" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Imports a workspace object (for example, a notebook or file) or the contents of an entire directory.</td>
</tr>
<tr>
    <td><a href="#mkdirs"><CopyableCode code="mkdirs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Creates the specified directory (and necessary parent directories if they do not exist). If there is</td>
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

Lists the contents of a directory, or the object if it is not a directory. If the input path does not

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

Deletes an object or a directory (and optionally recursively deletes all objects in the directory). *

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

Exports an object or the contents of an entire directory.

```sql
EXEC databricks_workspace.workspace.workspace.export 
@path='{{ path }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@format='{{ format }}'
;
```
</TabItem>
<TabItem value="import">

Imports a workspace object (for example, a notebook or file) or the contents of an entire directory.

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

Creates the specified directory (and necessary parent directories if they do not exist). If there is

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

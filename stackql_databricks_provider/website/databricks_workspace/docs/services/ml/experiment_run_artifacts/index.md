---
title: experiment_run_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - experiment_run_artifacts
  - ml
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

Creates, updates, deletes, gets or lists an <code>experiment_run_artifacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="experiment_run_artifacts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.experiment_run_artifacts" /></td></tr>
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
    "description": "The size in bytes of the file. Unset for directories."
  },
  {
    "name": "is_dir",
    "type": "boolean",
    "description": "Whether the path is a directory."
  },
  {
    "name": "path",
    "type": "string",
    "description": "The path relative to the root artifact directory run."
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
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-path"><code>path</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-run_uuid"><code>run_uuid</code></a></td>
    <td>List artifacts for a run. Takes an optional `artifact_path` prefix which if specified, the response</td>
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
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>The token indicating the page of artifact results to fetch. `page_token` is not supported when listing artifacts in UC Volumes. A maximum of 1000 artifacts will be retrieved for UC Volumes. Please call `/api/2.0/fs/directories&#123;directory_path&#125;` for listing artifacts in UC Volumes, which supports pagination. See [List directory contents | Files API](/api/workspace/files/listdirectorycontents).</td>
</tr>
<tr id="parameter-path">
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Filter artifacts matching this path (a relative path from the root artifact directory).</td>
</tr>
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>ID of the run whose artifacts to list. Must be provided.</td>
</tr>
<tr id="parameter-run_uuid">
    <td><CopyableCode code="run_uuid" /></td>
    <td><code>string</code></td>
    <td>[Deprecated, use `run_id` instead] ID of the run whose artifacts to list. This field will be removed in a future MLflow version.</td>
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

List artifacts for a run. Takes an optional `artifact_path` prefix which if specified, the response

```sql
SELECT
file_size,
is_dir,
path
FROM databricks_workspace.ml.experiment_run_artifacts
WHERE deployment_name = '{{ deployment_name }}' -- required
AND page_token = '{{ page_token }}'
AND path = '{{ path }}'
AND run_id = '{{ run_id }}'
AND run_uuid = '{{ run_uuid }}'
;
```
</TabItem>
</Tabs>

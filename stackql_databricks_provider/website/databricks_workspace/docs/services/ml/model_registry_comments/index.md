---
title: model_registry_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - model_registry_comments
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

Creates, updates, deletes, gets or lists a <code>model_registry_comments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="model_registry_comments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.model_registry_comments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-comment"><code>comment</code></a></td>
    <td></td>
    <td>Posts a comment on a model version. A comment can be submitted either by a user or programmatically to</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-comment"><code>comment</code></a></td>
    <td></td>
    <td>Post an edit to a comment on a model version.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Deletes a comment on a model version.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of an activity</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Posts a comment on a model version. A comment can be submitted either by a user or programmatically to

```sql
INSERT INTO databricks_workspace.ml.model_registry_comments (
name,
version,
comment,
workspace
)
SELECT 
'{{ name }}' /* required */,
'{{ version }}' /* required */,
'{{ comment }}' /* required */,
'{{ workspace }}'
RETURNING
comment
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: model_registry_comments
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the model_registry_comments resource.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the model.
    - name: version
      value: "{{ version }}"
      description: |
        Version of the model.
    - name: comment
      value: "{{ comment }}"
      description: |
        User-provided comment on the action.
`}</CodeBlock>

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

Post an edit to a comment on a model version.

```sql
UPDATE databricks_workspace.ml.model_registry_comments
SET 
id = '{{ id }}',
comment = '{{ comment }}'
WHERE 
workspace = '{{ workspace }}' --required
AND id = '{{ id }}' --required
AND comment = '{{ comment }}' --required
RETURNING
comment;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a comment on a model version.

```sql
EXEC databricks_workspace.ml.model_registry_comments.delete 
@id='{{ id }}' --required, 
@workspace='{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

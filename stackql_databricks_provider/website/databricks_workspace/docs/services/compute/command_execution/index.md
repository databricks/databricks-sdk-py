---
title: command_execution
hide_title: false
hide_table_of_contents: false
keywords:
  - command_execution
  - compute
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

Creates, updates, deletes, gets or lists a <code>command_execution</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>command_execution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.command_execution" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="command_status"
    values={[
        { label: 'command_status', value: 'command_status' }
    ]}
>
<TabItem value="command_status">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": ""
  },
  {
    "name": "results",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "cause",
        "type": "string",
        "description": ""
      },
      {
        "name": "data",
        "type": "object",
        "description": ""
      },
      {
        "name": "fileName",
        "type": "string",
        "description": "The image data in one of the following formats: 1. A Data URL with base64-encoded image data: `data:image/&#123;type&#125;;base64,&#123;base64-data&#125;`. Example: `data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...` 2. A FileStore file path for large images: `/plots/&#123;filename&#125;.png`. Example: `/plots/b6a7ad70-fb2c-4353-8aed-3f1e015174a4.png`"
      },
      {
        "name": "fileNames",
        "type": "array",
        "description": "List of image data for multiple images. Each element follows the same format as file_name."
      },
      {
        "name": "isJsonSchema",
        "type": "boolean",
        "description": "true if a JSON schema is returned instead of a string representation of the Hive type."
      },
      {
        "name": "pos",
        "type": "integer",
        "description": "internal field used by SDK"
      },
      {
        "name": "resultType",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      },
      {
        "name": "schema",
        "type": "array",
        "description": "The table schema"
      },
      {
        "name": "summary",
        "type": "string",
        "description": "The summary of the error"
      },
      {
        "name": "truncated",
        "type": "boolean",
        "description": "true if partial results are returned."
      }
    ]
  },
  {
    "name": "status",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
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
    <td><a href="#command_status"><CopyableCode code="command_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-context_id"><code>context_id</code></a>, <a href="#parameter-command_id"><code>command_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the status of and, if available, the results from a currently executing command.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates an execution context for running cluster commands.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Cancels a currently running command within an execution context.</td>
</tr>
<tr>
    <td><a href="#destroy"><CopyableCode code="destroy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-context_id"><code>context_id</code></a></td>
    <td></td>
    <td>Deletes an execution context.</td>
</tr>
<tr>
    <td><a href="#execute"><CopyableCode code="execute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Runs a cluster command in the given execution context, using the provided language.</td>
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
<tr id="parameter-cluster_id">
    <td><CopyableCode code="cluster_id" /></td>
    <td><code>string</code></td>
    <td>:param context_id: str</td>
</tr>
<tr id="parameter-command_id">
    <td><CopyableCode code="command_id" /></td>
    <td><code>string</code></td>
    <td>:returns: :class:`CommandStatusResponse`</td>
</tr>
<tr id="parameter-context_id">
    <td><CopyableCode code="context_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="command_status"
    values={[
        { label: 'command_status', value: 'command_status' }
    ]}
>
<TabItem value="command_status">

Gets the status of and, if available, the results from a currently executing command.

```sql
SELECT
id,
results,
status
FROM databricks_workspace.compute.command_execution
WHERE cluster_id = '{{ cluster_id }}' -- required
AND context_id = '{{ context_id }}' -- required
AND command_id = '{{ command_id }}' -- required
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

Creates an execution context for running cluster commands.

```sql
INSERT INTO databricks_workspace.compute.command_execution (
data__cluster_id,
data__language,
deployment_name
)
SELECT 
'{{ cluster_id }}',
'{{ language }}',
'{{ deployment_name }}'
RETURNING
id,
status
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: command_execution
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the command_execution resource.
    - name: cluster_id
      value: string
      description: |
        Running cluster id
    - name: language
      value: string
      description: |
        :returns: Long-running operation waiter for :class:`ContextStatusResponse`. See :method:wait_context_status_command_execution_running for more details.
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' },
        { label: 'destroy', value: 'destroy' },
        { label: 'execute', value: 'execute' }
    ]}
>
<TabItem value="cancel">

Cancels a currently running command within an execution context.

```sql
EXEC databricks_workspace.compute.command_execution.cancel 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}", 
"command_id": "{{ command_id }}", 
"context_id": "{{ context_id }}"
}'
;
```
</TabItem>
<TabItem value="destroy">

Deletes an execution context.

```sql
EXEC databricks_workspace.compute.command_execution.destroy 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}", 
"context_id": "{{ context_id }}"
}'
;
```
</TabItem>
<TabItem value="execute">

Runs a cluster command in the given execution context, using the provided language.

```sql
EXEC databricks_workspace.compute.command_execution.execute 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}", 
"command": "{{ command }}", 
"context_id": "{{ context_id }}", 
"language": "{{ language }}"
}'
;
```
</TabItem>
</Tabs>

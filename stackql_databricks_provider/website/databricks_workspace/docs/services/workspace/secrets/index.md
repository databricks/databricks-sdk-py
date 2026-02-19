---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
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

Creates, updates, deletes, gets or lists a <code>secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="secrets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.secrets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "key",
    "type": "string",
    "description": ""
  },
  {
    "name": "value",
    "type": "string",
    "description": "The value of the secret in its byte representation."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "key",
    "type": "string",
    "description": "A unique name to identify the secret."
  },
  {
    "name": "last_updated_timestamp",
    "type": "integer",
    "description": "The last updated timestamp (in milliseconds) for the secret."
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a secret for a given key and scope. This API can only be called from the DBUtils interface. Users</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Lists the secret keys that are stored at this scope. This is a metadata-only operation; secret data</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-key"><code>key</code></a></td>
    <td></td>
    <td>Inserts a secret under the provided scope with the given name. If a secret already exists with the</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-key"><code>key</code></a></td>
    <td></td>
    <td>Deletes the secret stored in this secret scope. You must have ``WRITE`` or ``MANAGE`` permission on</td>
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
<tr id="parameter-key">
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>Name of the secret to fetch value information.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The name of the scope to list secrets within.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a secret for a given key and scope. This API can only be called from the DBUtils interface. Users

```sql
SELECT
key,
value
FROM databricks_workspace.workspace.secrets
WHERE scope = '{{ scope }}' -- required
AND key = '{{ key }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the secret keys that are stored at this scope. This is a metadata-only operation; secret data

```sql
SELECT
key,
last_updated_timestamp
FROM databricks_workspace.workspace.secrets
WHERE scope = '{{ scope }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="put"
    values={[
        { label: 'put', value: 'put' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="put">

Inserts a secret under the provided scope with the given name. If a secret already exists with the

```sql
INSERT INTO databricks_workspace.workspace.secrets (
scope,
key,
bytes_value,
string_value,
deployment_name
)
SELECT 
'{{ scope }}' /* required */,
'{{ key }}' /* required */,
'{{ bytes_value }}',
'{{ string_value }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: secrets
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the secrets resource.
    - name: scope
      value: string
      description: |
        The name of the scope to which the secret will be associated with.
    - name: key
      value: string
      description: |
        A unique name to identify the secret.
    - name: bytes_value
      value: string
      description: |
        If specified, value will be stored as bytes.
    - name: string_value
      value: string
      description: |
        If specified, note that the value will be stored in UTF-8 (MB4) form.
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

Deletes the secret stored in this secret scope. You must have ``WRITE`` or ``MANAGE`` permission on

```sql
EXEC databricks_workspace.workspace.secrets.delete 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"scope": "{{ scope }}", 
"key": "{{ key }}"
}'
;
```
</TabItem>
</Tabs>

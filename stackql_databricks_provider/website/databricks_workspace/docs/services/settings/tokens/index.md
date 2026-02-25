---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - settings
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

Creates, updates, deletes, gets or lists a <code>tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tokens" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settings.tokens" /></td></tr>
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
    "name": "token_id",
    "type": "string",
    "description": "The ID of this token."
  },
  {
    "name": "comment",
    "type": "string",
    "description": ""
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Server time (in epoch milliseconds) when the token was created."
  },
  {
    "name": "expiry_time",
    "type": "integer",
    "description": "Server time (in epoch milliseconds) when the token will expire, or -1 if not applicable."
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
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Lists all the valid tokens for a user-workspace pair.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Creates and returns a token for a user. If this call is made through token authentication, it creates</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-token_id"><code>token_id</code></a></td>
    <td></td>
    <td>Revokes an access token.</td>
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
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
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

Lists all the valid tokens for a user-workspace pair.

```sql
SELECT
token_id,
comment,
creation_time,
expiry_time
FROM databricks_workspace.settings.tokens
WHERE workspace = '{{ workspace }}' -- required
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

Creates and returns a token for a user. If this call is made through token authentication, it creates

```sql
INSERT INTO databricks_workspace.settings.tokens (
comment,
lifetime_seconds,
workspace
)
SELECT 
'{{ comment }}',
{{ lifetime_seconds }},
'{{ workspace }}'
RETURNING
token_info,
token_value
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: tokens
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the tokens resource.
    - name: comment
      value: "{{ comment }}"
      description: |
        Optional description to attach to the token.
    - name: lifetime_seconds
      value: {{ lifetime_seconds }}
      description: |
        The lifetime of the token, in seconds. If the lifetime is not specified, this token remains valid for 2 years.
`}</CodeBlock>

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

Revokes an access token.

```sql
EXEC databricks_workspace.settings.tokens.delete 
@workspace='{{ workspace }}' --required 
@@json=
'{
"token_id": "{{ token_id }}"
}'
;
```
</TabItem>
</Tabs>

---
title: credentials_manager
hide_title: false
hide_table_of_contents: false
keywords:
  - credentials_manager
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>credentials_manager</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>credentials_manager</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settings.credentials_manager" /></td></tr>
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
    <td><a href="#exchange_token"><CopyableCode code="exchange_token" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__partition_id"><code>data__partition_id</code></a>, <a href="#parameter-data__token_type"><code>data__token_type</code></a>, <a href="#parameter-data__scopes"><code>data__scopes</code></a></td>
    <td></td>
    <td>Exchange tokens with an Identity Provider to get a new access token. It allows specifying scopes to</td>
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
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="exchange_token"
    values={[
        { label: 'exchange_token', value: 'exchange_token' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="exchange_token">

Exchange tokens with an Identity Provider to get a new access token. It allows specifying scopes to

```sql
INSERT INTO databricks_workspace.settings.credentials_manager (
data__partition_id,
data__token_type,
data__scopes,
deployment_name
)
SELECT 
'{{ partition_id }}' /* required */,
'{{ token_type }}' /* required */,
'{{ scopes }}' /* required */,
'{{ deployment_name }}'
RETURNING
values
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: credentials_manager
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the credentials_manager resource.
    - name: partition_id
      value: string
      description: |
        The partition of Credentials store
    - name: token_type
      value: string
      description: |
        A list of token types being requested
    - name: scopes
      value: string
      description: |
        Array of scopes for the token request.
```
</TabItem>
</Tabs>

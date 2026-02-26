---
title: secret_acls
hide_title: false
hide_table_of_contents: false
keywords:
  - secret_acls
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>secret_acls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="secret_acls" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.secret_acls" /></td></tr>
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
    "name": "permission",
    "type": "string",
    "description": "The permission level applied to the principal. (MANAGE, READ, WRITE)"
  },
  {
    "name": "principal",
    "type": "string",
    "description": "The principal in which the permission is applied."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "permission",
    "type": "string",
    "description": "The permission level applied to the principal. (MANAGE, READ, WRITE)"
  },
  {
    "name": "principal",
    "type": "string",
    "description": "The principal in which the permission is applied."
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-principal"><code>principal</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Describes the details about the given ACL, such as the group and permission.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Lists the ACLs set on the given scope.</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-principal"><code>principal</code></a>, <a href="#parameter-permission"><code>permission</code></a></td>
    <td></td>
    <td>Creates or overwrites the ACL associated with the given principal (user or group) on the specified</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-principal"><code>principal</code></a></td>
    <td></td>
    <td>Deletes the given ACL on the given scope.</td>
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
<tr id="parameter-principal">
    <td><CopyableCode code="principal" /></td>
    <td><code>string</code></td>
    <td>The principal to fetch ACL information for.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The name of the scope to fetch ACL information from.</td>
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

Describes the details about the given ACL, such as the group and permission.

```sql
SELECT
permission,
principal
FROM databricks_workspace.workspace.secret_acls
WHERE scope = '{{ scope }}' -- required
AND principal = '{{ principal }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the ACLs set on the given scope.

```sql
SELECT
permission,
principal
FROM databricks_workspace.workspace.secret_acls
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

Creates or overwrites the ACL associated with the given principal (user or group) on the specified

```sql
INSERT INTO databricks_workspace.workspace.secret_acls (
scope,
principal,
permission,
deployment_name
)
SELECT 
'{{ scope }}' /* required */,
'{{ principal }}' /* required */,
'{{ permission }}' /* required */,
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: secret_acls
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the secret_acls resource.
    - name: scope
      value: "{{ scope }}"
      description: |
        The name of the scope to apply permissions to.
    - name: principal
      value: "{{ principal }}"
      description: |
        The principal in which the permission is applied.
    - name: permission
      value: "{{ permission }}"
      description: |
        The permission level applied to the principal.
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

Deletes the given ACL on the given scope.

```sql
EXEC databricks_workspace.workspace.secret_acls.delete 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"scope": "{{ scope }}", 
"principal": "{{ principal }}"
}'
;
```
</TabItem>
</Tabs>

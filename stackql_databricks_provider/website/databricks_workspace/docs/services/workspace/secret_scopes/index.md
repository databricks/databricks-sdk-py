---
title: secret_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - secret_scopes
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

Creates, updates, deletes, gets or lists a <code>secret_scopes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="secret_scopes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.secret_scopes" /></td></tr>
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
    "name": "name",
    "type": "string",
    "description": "A unique name to identify the secret scope."
  },
  {
    "name": "backend_type",
    "type": "string",
    "description": "The type of secret scope backend. (AZURE_KEYVAULT, DATABRICKS)"
  },
  {
    "name": "keyvault_metadata",
    "type": "object",
    "description": "The metadata for the secret scope if the type is ``AZURE_KEYVAULT``",
    "children": [
      {
        "name": "resource_id",
        "type": "string",
        "description": "The resource id of the azure KeyVault that user wants to associate the scope with."
      },
      {
        "name": "dns_name",
        "type": "string",
        "description": "The DNS of the KeyVault"
      }
    ]
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
    <td></td>
    <td>Lists all secret scopes available in the workspace.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Creates a new secret scope.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Deletes a secret scope.</td>
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

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Lists all secret scopes available in the workspace.

```sql
SELECT
name,
backend_type,
keyvault_metadata
FROM databricks_workspace.workspace.secret_scopes
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Creates a new secret scope.

```sql
INSERT INTO databricks_workspace.workspace.secret_scopes (
scope,
backend_azure_keyvault,
initial_manage_principal,
scope_backend_type,
deployment_name
)
SELECT 
'{{ scope }}' /* required */,
'{{ backend_azure_keyvault }}',
'{{ initial_manage_principal }}',
'{{ scope_backend_type }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: secret_scopes
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the secret_scopes resource.
    - name: scope
      value: "{{ scope }}"
      description: |
        Scope name requested by the user. Scope names are unique.
    - name: backend_azure_keyvault
      description: |
        The metadata for the secret scope if the type is \`\`AZURE_KEYVAULT\`\`
      value:
        resource_id: "{{ resource_id }}"
        dns_name: "{{ dns_name }}"
    - name: initial_manage_principal
      value: "{{ initial_manage_principal }}"
      description: |
        The principal that is initially granted \`\`MANAGE\`\` permission to the created scope.
    - name: scope_backend_type
      value: "{{ scope_backend_type }}"
      description: |
        The backend type the scope will be created with. If not specified, will default to \`\`DATABRICKS\`\`
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

Deletes a secret scope.

```sql
EXEC databricks_workspace.workspace.secret_scopes.delete 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"scope": "{{ scope }}"
}'
;
```
</TabItem>
</Tabs>

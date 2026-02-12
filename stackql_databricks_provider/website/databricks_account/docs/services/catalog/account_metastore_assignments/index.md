---
title: account_metastore_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - account_metastore_assignments
  - catalog
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists an <code>account_metastore_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_metastore_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.catalog.account_metastore_assignments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="account_metastore_assignments_get"
    values={[
        { label: 'account_metastore_assignments_get', value: 'account_metastore_assignments_get' },
        { label: 'account_metastore_assignments_list', value: 'account_metastore_assignments_list' }
    ]}
>
<TabItem value="account_metastore_assignments_get">

<SchemaTable fields={[
  {
    "name": "metastore_assignment",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "workspace_id",
        "type": "integer",
        "description": ""
      },
      {
        "name": "metastore_id",
        "type": "string",
        "description": "The unique ID of the metastore."
      },
      {
        "name": "default_catalog_name",
        "type": "string",
        "description": "The name of the default catalog in the metastore. This field is deprecated. Please use \"Default Namespace API\" to configure the default catalog for a Databricks workspace."
      }
    ]
  }
]} />
</TabItem>
<TabItem value="account_metastore_assignments_list">

<SchemaTable fields={[
  {
    "name": "workspaces",
    "type": "array",
    "description": ""
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
    <td><a href="#account_metastore_assignments_get"><CopyableCode code="account_metastore_assignments_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a></td>
    <td></td>
    <td>Gets the metastore assignment, if any, for the workspace specified by ID. If the workspace is assigned</td>
</tr>
<tr>
    <td><a href="#account_metastore_assignments_list"><CopyableCode code="account_metastore_assignments_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a></td>
    <td></td>
    <td>Gets a list of all Databricks workspace IDs that have been assigned to given metastore.</td>
</tr>
<tr>
    <td><a href="#account_metastore_assignments_create"><CopyableCode code="account_metastore_assignments_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a></td>
    <td></td>
    <td>Creates an assignment to a metastore for a workspace</td>
</tr>
<tr>
    <td><a href="#account_metastore_assignments_update"><CopyableCode code="account_metastore_assignments_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a></td>
    <td></td>
    <td>Updates an assignment to a metastore for a workspace. Currently, only the default catalog may be</td>
</tr>
<tr>
    <td><a href="#account_metastore_assignments_delete"><CopyableCode code="account_metastore_assignments_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a></td>
    <td></td>
    <td>Deletes a metastore assignment to a workspace, leaving the workspace with no metastore.</td>
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
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-metastore_id">
    <td><CopyableCode code="metastore_id" /></td>
    <td><code>string</code></td>
    <td>Unity Catalog metastore ID</td>
</tr>
<tr id="parameter-workspace_id">
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>integer</code></td>
    <td>Workspace ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="account_metastore_assignments_get"
    values={[
        { label: 'account_metastore_assignments_get', value: 'account_metastore_assignments_get' },
        { label: 'account_metastore_assignments_list', value: 'account_metastore_assignments_list' }
    ]}
>
<TabItem value="account_metastore_assignments_get">

Gets the metastore assignment, if any, for the workspace specified by ID. If the workspace is assigned

```sql
SELECT
metastore_assignment
FROM databricks_account.catalog.account_metastore_assignments
WHERE account_id = '{{ account_id }}' -- required
AND workspace_id = '{{ workspace_id }}' -- required
;
```
</TabItem>
<TabItem value="account_metastore_assignments_list">

Gets a list of all Databricks workspace IDs that have been assigned to given metastore.

```sql
SELECT
workspaces
FROM databricks_account.catalog.account_metastore_assignments
WHERE account_id = '{{ account_id }}' -- required
AND metastore_id = '{{ metastore_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="account_metastore_assignments_create"
    values={[
        { label: 'account_metastore_assignments_create', value: 'account_metastore_assignments_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="account_metastore_assignments_create">

Creates an assignment to a metastore for a workspace

```sql
INSERT INTO databricks_account.catalog.account_metastore_assignments (
data__metastore_assignment,
account_id,
workspace_id,
metastore_id
)
SELECT 
'{{ metastore_assignment }}',
'{{ account_id }}',
'{{ workspace_id }}',
'{{ metastore_id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: account_metastore_assignments
  props:
    - name: account_id
      value: string
      description: Required parameter for the account_metastore_assignments resource.
    - name: workspace_id
      value: integer
      description: Required parameter for the account_metastore_assignments resource.
    - name: metastore_id
      value: string
      description: Required parameter for the account_metastore_assignments resource.
    - name: metastore_assignment
      value: string
      description: |
        :returns: :class:`AccountsCreateMetastoreAssignmentResponse`
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="account_metastore_assignments_update"
    values={[
        { label: 'account_metastore_assignments_update', value: 'account_metastore_assignments_update' }
    ]}
>
<TabItem value="account_metastore_assignments_update">

Updates an assignment to a metastore for a workspace. Currently, only the default catalog may be

```sql
REPLACE databricks_account.catalog.account_metastore_assignments
SET 
data__metastore_assignment = '{{ metastore_assignment }}'
WHERE 
account_id = '{{ account_id }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND metastore_id = '{{ metastore_id }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="account_metastore_assignments_delete"
    values={[
        { label: 'account_metastore_assignments_delete', value: 'account_metastore_assignments_delete' }
    ]}
>
<TabItem value="account_metastore_assignments_delete">

Deletes a metastore assignment to a workspace, leaving the workspace with no metastore.

```sql
DELETE FROM databricks_account.catalog.account_metastore_assignments
WHERE account_id = '{{ account_id }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND metastore_id = '{{ metastore_id }}' --required
;
```
</TabItem>
</Tabs>

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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

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
<TabItem value="list">

<SchemaTable fields={[]} />
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a></td>
    <td></td>
    <td>Gets the metastore assignment, if any, for the workspace specified by ID. If the workspace is assigned<br />a metastore, the mapping will be returned. If no metastore is assigned to the workspace, the<br />assignment will not be found and a 404 returned.<br /><br />:param workspace_id: int<br />  Workspace ID.<br /><br />:returns: :class:`AccountsMetastoreAssignment`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a></td>
    <td></td>
    <td>Gets a list of all Databricks workspace IDs that have been assigned to given metastore.<br /><br />:param metastore_id: str<br />  Unity Catalog metastore ID<br /><br />:returns: Iterator over int</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a></td>
    <td></td>
    <td>Creates an assignment to a metastore for a workspace<br /><br />:param workspace_id: int<br />  Workspace ID.<br />:param metastore_id: str<br />  Unity Catalog metastore ID<br />:param metastore_assignment: :class:`CreateMetastoreAssignment` (optional)<br /><br />:returns: :class:`AccountsCreateMetastoreAssignmentResponse`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a></td>
    <td></td>
    <td>Updates an assignment to a metastore for a workspace. Currently, only the default catalog may be<br />updated.<br /><br />:param workspace_id: int<br />  Workspace ID.<br />:param metastore_id: str<br />  Unity Catalog metastore ID<br />:param metastore_assignment: :class:`UpdateMetastoreAssignment` (optional)<br /><br />:returns: :class:`AccountsUpdateMetastoreAssignmentResponse`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a></td>
    <td></td>
    <td>Deletes a metastore assignment to a workspace, leaving the workspace with no metastore.<br /><br />:param workspace_id: int<br />  Workspace ID.<br />:param metastore_id: str<br />  Unity Catalog metastore ID<br /><br />:returns: :class:`AccountsDeleteMetastoreAssignmentResponse`</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the metastore assignment, if any, for the workspace specified by ID. If the workspace is assigned<br />a metastore, the mapping will be returned. If no metastore is assigned to the workspace, the<br />assignment will not be found and a 404 returned.<br /><br />:param workspace_id: int<br />  Workspace ID.<br /><br />:returns: :class:`AccountsMetastoreAssignment`

```sql
SELECT
metastore_assignment
FROM databricks_account.catalog.account_metastore_assignments
WHERE account_id = '{{ account_id }}' -- required
AND workspace_id = '{{ workspace_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of all Databricks workspace IDs that have been assigned to given metastore.<br /><br />:param metastore_id: str<br />  Unity Catalog metastore ID<br /><br />:returns: Iterator over int

```sql
SELECT
*
FROM databricks_account.catalog.account_metastore_assignments
WHERE account_id = '{{ account_id }}' -- required
AND metastore_id = '{{ metastore_id }}' -- required
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

Creates an assignment to a metastore for a workspace<br /><br />:param workspace_id: int<br />  Workspace ID.<br />:param metastore_id: str<br />  Unity Catalog metastore ID<br />:param metastore_assignment: :class:`CreateMetastoreAssignment` (optional)<br /><br />:returns: :class:`AccountsCreateMetastoreAssignmentResponse`

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
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates an assignment to a metastore for a workspace. Currently, only the default catalog may be<br />updated.<br /><br />:param workspace_id: int<br />  Workspace ID.<br />:param metastore_id: str<br />  Unity Catalog metastore ID<br />:param metastore_assignment: :class:`UpdateMetastoreAssignment` (optional)<br /><br />:returns: :class:`AccountsUpdateMetastoreAssignmentResponse`

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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a metastore assignment to a workspace, leaving the workspace with no metastore.<br /><br />:param workspace_id: int<br />  Workspace ID.<br />:param metastore_id: str<br />  Unity Catalog metastore ID<br /><br />:returns: :class:`AccountsDeleteMetastoreAssignmentResponse`

```sql
DELETE FROM databricks_account.catalog.account_metastore_assignments
WHERE account_id = '{{ account_id }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND metastore_id = '{{ metastore_id }}' --required
;
```
</TabItem>
</Tabs>

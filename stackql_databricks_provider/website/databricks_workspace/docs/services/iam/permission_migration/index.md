---
title: permission_migration
hide_title: false
hide_table_of_contents: false
keywords:
  - permission_migration
  - iam
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

Creates, updates, deletes, gets or lists a <code>permission_migration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission_migration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.permission_migration" /></td></tr>
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
    <td><a href="#migrate"><CopyableCode code="migrate" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__workspace_id"><code>data__workspace_id</code></a>, <a href="#parameter-data__from_workspace_group_name"><code>data__from_workspace_group_name</code></a>, <a href="#parameter-data__to_account_group_name"><code>data__to_account_group_name</code></a></td>
    <td></td>
    <td>Migrate Permissions.</td>
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
    defaultValue="migrate"
    values={[
        { label: 'migrate', value: 'migrate' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="migrate">

Migrate Permissions.

```sql
INSERT INTO databricks_workspace.iam.permission_migration (
data__workspace_id,
data__from_workspace_group_name,
data__to_account_group_name,
data__size,
deployment_name
)
SELECT 
{{ workspace_id }} /* required */,
'{{ from_workspace_group_name }}' /* required */,
'{{ to_account_group_name }}' /* required */,
'{{ size }}',
'{{ deployment_name }}'
RETURNING
permissions_migrated
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: permission_migration
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the permission_migration resource.
    - name: workspace_id
      value: integer
      description: |
        WorkspaceId of the associated workspace where the permission migration will occur.
    - name: from_workspace_group_name
      value: string
      description: |
        The name of the workspace group that permissions will be migrated from.
    - name: to_account_group_name
      value: string
      description: |
        The name of the account group that permissions will be migrated to.
    - name: size
      value: string
      description: |
        The maximum number of permissions that will be migrated.
```
</TabItem>
</Tabs>

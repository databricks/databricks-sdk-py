---
title: table_constraints
hide_title: false
hide_table_of_contents: false
keywords:
  - table_constraints
  - catalog
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

Creates, updates, deletes, gets or lists a <code>table_constraints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table_constraints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.table_constraints" /></td></tr>
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
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__full_name_arg"><code>data__full_name_arg</code></a>, <a href="#parameter-data__constraint"><code>data__constraint</code></a></td>
    <td></td>
    <td>Creates a new table constraint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-constraint_name"><code>constraint_name</code></a>, <a href="#parameter-cascade"><code>cascade</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a table constraint.</td>
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
<tr id="parameter-cascade">
    <td><CopyableCode code="cascade" /></td>
    <td><code>boolean</code></td>
    <td>If true, try deleting all child constraints of the current constraint. If false, reject this operation if the current constraint has any child constraints.</td>
</tr>
<tr id="parameter-constraint_name">
    <td><CopyableCode code="constraint_name" /></td>
    <td><code>string</code></td>
    <td>The name of the constraint to delete.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>Full name of the table referenced by the constraint.</td>
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

Creates a new table constraint.

```sql
INSERT INTO databricks_workspace.catalog.table_constraints (
data__full_name_arg,
data__constraint,
deployment_name
)
SELECT 
'{{ full_name_arg }}' /* required */,
'{{ constraint }}' /* required */,
'{{ deployment_name }}'
RETURNING
foreign_key_constraint,
named_table_constraint,
primary_key_constraint
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: table_constraints
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the table_constraints resource.
    - name: full_name_arg
      value: string
      description: |
        The full name of the table referenced by the constraint.
    - name: constraint
      value: string
      description: |
        :returns: :class:`TableConstraint`
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

Deletes a table constraint.

```sql
DELETE FROM databricks_workspace.catalog.table_constraints
WHERE full_name = '{{ full_name }}' --required
AND constraint_name = '{{ constraint_name }}' --required
AND cascade = '{{ cascade }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

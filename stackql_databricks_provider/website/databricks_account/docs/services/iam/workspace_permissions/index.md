---
title: workspace_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_permissions
  - iam
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

Creates, updates, deletes, gets or lists a <code>workspace_permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_permissions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.workspace_permissions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="workspace_assignment_get"
    values={[
        { label: 'workspace_assignment_get', value: 'workspace_assignment_get' }
    ]}
>
<TabItem value="workspace_assignment_get">

<SchemaTable fields={[
  {
    "name": "permissions",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "description",
        "type": "string",
        "description": ""
      },
      {
        "name": "permission_level",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (ADMIN, UNKNOWN, USER)"
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
    <td><a href="#workspace_assignment_get"><CopyableCode code="workspace_assignment_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a></td>
    <td></td>
    <td>Get an array of workspace permissions for the specified account and workspace.</td>
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
<tr id="parameter-workspace_id">
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>integer</code></td>
    <td>The workspace ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="workspace_assignment_get"
    values={[
        { label: 'workspace_assignment_get', value: 'workspace_assignment_get' }
    ]}
>
<TabItem value="workspace_assignment_get">

Get an array of workspace permissions for the specified account and workspace.

```sql
SELECT
permissions
FROM databricks_account.iam.workspace_permissions
WHERE account_id = '{{ account_id }}' -- required
AND workspace_id = '{{ workspace_id }}' -- required
;
```
</TabItem>
</Tabs>

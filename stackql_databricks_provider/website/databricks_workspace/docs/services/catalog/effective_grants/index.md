---
title: effective_grants
hide_title: false
hide_table_of_contents: false
keywords:
  - effective_grants
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

Creates, updates, deletes, gets or lists an <code>effective_grants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>effective_grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.effective_grants" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "next_page_token",
    "type": "string",
    "description": ""
  },
  {
    "name": "privilege_assignments",
    "type": "array",
    "description": "The privileges conveyed to each principal (either directly or via inheritance)",
    "children": [
      {
        "name": "principal",
        "type": "string",
        "description": ""
      },
      {
        "name": "privileges",
        "type": "array",
        "description": "The privileges conveyed to the principal (either directly or via inheritance).",
        "children": [
          {
            "name": "inherited_from_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "inherited_from_type",
            "type": "string",
            "description": "The type of Unity Catalog securable."
          },
          {
            "name": "privilege",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
          }
        ]
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-securable_type"><code>securable_type</code></a>, <a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-principal"><code>principal</code></a></td>
    <td>Gets the effective permissions for a securable. Includes inherited permissions from any parent<br />securables.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param securable_type: str<br />  Type of securable.<br />:param full_name: str<br />  Full name of securable.<br />:param max_results: int (optional)<br />  Specifies the maximum number of privileges to return (page length). Every<br />  EffectivePrivilegeAssignment present in a single page response is guaranteed to contain all the<br />  effective privileges granted on (or inherited by) the requested Securable for the respective<br />  principal.<br /><br />  If not set, all the effective permissions are returned. If set to - lesser than 0: invalid parameter<br />  error - 0: page length is set to a server configured value - lesser than 150 but greater than 0:<br />  invalid parameter error (this is to ensure that server is able to return at least one complete<br />  EffectivePrivilegeAssignment in a single page response) - greater than (or equal to) 150: page<br />  length is the minimum of this value and a server configured value<br />:param page_token: str (optional)<br />  Opaque token for the next page of results (pagination).<br />:param principal: str (optional)<br />  If provided, only the effective permissions for the specified principal (user or group) are<br />  returned.<br /><br />:returns: :class:`EffectivePermissionsList`</td>
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
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>Full name of securable.</td>
</tr>
<tr id="parameter-securable_type">
    <td><CopyableCode code="securable_type" /></td>
    <td><code>string</code></td>
    <td>Type of securable.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Specifies the maximum number of privileges to return (page length). Every EffectivePrivilegeAssignment present in a single page response is guaranteed to contain all the effective privileges granted on (or inherited by) the requested Securable for the respective principal. If not set, all the effective permissions are returned. If set to - lesser than 0: invalid parameter error - 0: page length is set to a server configured value - lesser than 150 but greater than 0: invalid parameter error (this is to ensure that server is able to return at least one complete EffectivePrivilegeAssignment in a single page response) - greater than (or equal to) 150: page length is the minimum of this value and a server configured value</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque token for the next page of results (pagination).</td>
</tr>
<tr id="parameter-principal">
    <td><CopyableCode code="principal" /></td>
    <td><code>string</code></td>
    <td>If provided, only the effective permissions for the specified principal (user or group) are returned.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the effective permissions for a securable. Includes inherited permissions from any parent<br />securables.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param securable_type: str<br />  Type of securable.<br />:param full_name: str<br />  Full name of securable.<br />:param max_results: int (optional)<br />  Specifies the maximum number of privileges to return (page length). Every<br />  EffectivePrivilegeAssignment present in a single page response is guaranteed to contain all the<br />  effective privileges granted on (or inherited by) the requested Securable for the respective<br />  principal.<br /><br />  If not set, all the effective permissions are returned. If set to - lesser than 0: invalid parameter<br />  error - 0: page length is set to a server configured value - lesser than 150 but greater than 0:<br />  invalid parameter error (this is to ensure that server is able to return at least one complete<br />  EffectivePrivilegeAssignment in a single page response) - greater than (or equal to) 150: page<br />  length is the minimum of this value and a server configured value<br />:param page_token: str (optional)<br />  Opaque token for the next page of results (pagination).<br />:param principal: str (optional)<br />  If provided, only the effective permissions for the specified principal (user or group) are<br />  returned.<br /><br />:returns: :class:`EffectivePermissionsList`

```sql
SELECT
next_page_token,
privilege_assignments
FROM databricks_workspace.catalog.effective_grants
WHERE securable_type = '{{ securable_type }}' -- required
AND full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
AND principal = '{{ principal }}'
;
```
</TabItem>
</Tabs>

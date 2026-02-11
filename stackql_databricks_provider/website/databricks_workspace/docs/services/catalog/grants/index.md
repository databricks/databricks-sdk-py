---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
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

Creates, updates, deletes, gets or lists a <code>grants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.grants" /></td></tr>
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
    "description": "The privileges assigned to each principal",
    "children": [
      {
        "name": "principal",
        "type": "string",
        "description": ""
      },
      {
        "name": "privileges",
        "type": "array",
        "description": "The privileges assigned to the principal."
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
    <td>Gets the permissions for a securable. Does not include inherited permissions.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param securable_type: str<br />  Type of securable.<br />:param full_name: str<br />  Full name of securable.<br />:param max_results: int (optional)<br />  Specifies the maximum number of privileges to return (page length). Every PrivilegeAssignment<br />  present in a single page response is guaranteed to contain all the privileges granted on the<br />  requested Securable for the respective principal.<br /><br />  If not set, all the permissions are returned. If set to - lesser than 0: invalid parameter error -<br />  0: page length is set to a server configured value - lesser than 150 but greater than 0: invalid<br />  parameter error (this is to ensure that server is able to return at least one complete<br />  PrivilegeAssignment in a single page response) - greater than (or equal to) 150: page length is the<br />  minimum of this value and a server configured value<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br />:param principal: str (optional)<br />  If provided, only the permissions for the specified principal (user or group) are returned.<br /><br />:returns: :class:`GetPermissionsResponse`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-securable_type"><code>securable_type</code></a>, <a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the permissions for a securable.<br /><br />:param securable_type: str<br />  Type of securable.<br />:param full_name: str<br />  Full name of securable.<br />:param changes: List[:class:`PermissionsChange`] (optional)<br />  Array of permissions change objects.<br /><br />:returns: :class:`UpdatePermissionsResponse`</td>
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
    <td>Specifies the maximum number of privileges to return (page length). Every PrivilegeAssignment present in a single page response is guaranteed to contain all the privileges granted on the requested Securable for the respective principal. If not set, all the permissions are returned. If set to - lesser than 0: invalid parameter error - 0: page length is set to a server configured value - lesser than 150 but greater than 0: invalid parameter error (this is to ensure that server is able to return at least one complete PrivilegeAssignment in a single page response) - greater than (or equal to) 150: page length is the minimum of this value and a server configured value</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on previous query.</td>
</tr>
<tr id="parameter-principal">
    <td><CopyableCode code="principal" /></td>
    <td><code>string</code></td>
    <td>If provided, only the permissions for the specified principal (user or group) are returned.</td>
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

Gets the permissions for a securable. Does not include inherited permissions.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param securable_type: str<br />  Type of securable.<br />:param full_name: str<br />  Full name of securable.<br />:param max_results: int (optional)<br />  Specifies the maximum number of privileges to return (page length). Every PrivilegeAssignment<br />  present in a single page response is guaranteed to contain all the privileges granted on the<br />  requested Securable for the respective principal.<br /><br />  If not set, all the permissions are returned. If set to - lesser than 0: invalid parameter error -<br />  0: page length is set to a server configured value - lesser than 150 but greater than 0: invalid<br />  parameter error (this is to ensure that server is able to return at least one complete<br />  PrivilegeAssignment in a single page response) - greater than (or equal to) 150: page length is the<br />  minimum of this value and a server configured value<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br />:param principal: str (optional)<br />  If provided, only the permissions for the specified principal (user or group) are returned.<br /><br />:returns: :class:`GetPermissionsResponse`

```sql
SELECT
next_page_token,
privilege_assignments
FROM databricks_workspace.catalog.grants
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


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates the permissions for a securable.<br /><br />:param securable_type: str<br />  Type of securable.<br />:param full_name: str<br />  Full name of securable.<br />:param changes: List[:class:`PermissionsChange`] (optional)<br />  Array of permissions change objects.<br /><br />:returns: :class:`UpdatePermissionsResponse`

```sql
UPDATE databricks_workspace.catalog.grants
SET 
data__changes = '{{ changes }}'
WHERE 
securable_type = '{{ securable_type }}' --required
AND full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
privilege_assignments;
```
</TabItem>
</Tabs>

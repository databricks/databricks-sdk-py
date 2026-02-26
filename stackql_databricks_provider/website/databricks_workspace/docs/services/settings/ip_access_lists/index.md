---
title: ip_access_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_access_lists
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists an <code>ip_access_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ip_access_lists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settings.ip_access_lists" /></td></tr>
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
    "name": "ip_access_list",
    "type": "object",
    "description": "Definition of an IP Access list",
    "children": [
      {
        "name": "address_count",
        "type": "integer",
        "description": "Total number of IP or CIDR values."
      },
      {
        "name": "created_at",
        "type": "integer",
        "description": "Creation timestamp in milliseconds."
      },
      {
        "name": "created_by",
        "type": "integer",
        "description": "User ID of the user who created this list."
      },
      {
        "name": "enabled",
        "type": "boolean",
        "description": "Specifies whether this IP access list is enabled."
      },
      {
        "name": "ip_addresses",
        "type": "array",
        "description": ""
      },
      {
        "name": "label",
        "type": "string",
        "description": "Label for the IP access list. This **cannot** be empty."
      },
      {
        "name": "list_id",
        "type": "string",
        "description": "Universally unique identifier (UUID) of the IP access list."
      },
      {
        "name": "list_type",
        "type": "string",
        "description": "Type of IP access list. Valid values are as follows and are case-sensitive:<br /><br />* `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or<br />range. IP addresses in the block list are excluded even if they are included in an allow list. (ALLOW, BLOCK)"
      },
      {
        "name": "updated_at",
        "type": "integer",
        "description": "Update timestamp in milliseconds."
      },
      {
        "name": "updated_by",
        "type": "integer",
        "description": "User ID of the user who updated this list."
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "list_id",
    "type": "string",
    "description": "Universally unique identifier (UUID) of the IP access list."
  },
  {
    "name": "address_count",
    "type": "integer",
    "description": "Total number of IP or CIDR values."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Creation timestamp in milliseconds."
  },
  {
    "name": "created_by",
    "type": "integer",
    "description": "User ID of the user who created this list."
  },
  {
    "name": "enabled",
    "type": "boolean",
    "description": "Specifies whether this IP access list is enabled."
  },
  {
    "name": "ip_addresses",
    "type": "array",
    "description": ""
  },
  {
    "name": "label",
    "type": "string",
    "description": "Label for the IP access list. This **cannot** be empty."
  },
  {
    "name": "list_type",
    "type": "string",
    "description": "Type of IP access list. Valid values are as follows and are case-sensitive:<br /><br />* `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or<br />range. IP addresses in the block list are excluded even if they are included in an allow list. (ALLOW, BLOCK)"
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Update timestamp in milliseconds."
  },
  {
    "name": "updated_by",
    "type": "integer",
    "description": "User ID of the user who updated this list."
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
    <td><a href="#parameter-ip_access_list_id"><code>ip_access_list_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets an IP access list, specified by its list ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets all IP access lists for the specified workspace.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-label"><code>label</code></a>, <a href="#parameter-list_type"><code>list_type</code></a></td>
    <td></td>
    <td>Creates an IP access list for this workspace.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-ip_access_list_id"><code>ip_access_list_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates an existing IP access list, specified by its ID.</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-ip_access_list_id"><code>ip_access_list_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-label"><code>label</code></a>, <a href="#parameter-list_type"><code>list_type</code></a>, <a href="#parameter-enabled"><code>enabled</code></a></td>
    <td></td>
    <td>Replaces an IP access list, specified by its ID.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-ip_access_list_id"><code>ip_access_list_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes an IP access list, specified by its list ID.</td>
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
<tr id="parameter-ip_access_list_id">
    <td><CopyableCode code="ip_access_list_id" /></td>
    <td><code>string</code></td>
    <td>The ID for the corresponding IP access list</td>
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

Gets an IP access list, specified by its list ID.

```sql
SELECT
ip_access_list
FROM databricks_workspace.settings.ip_access_lists
WHERE ip_access_list_id = '{{ ip_access_list_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all IP access lists for the specified workspace.

```sql
SELECT
list_id,
address_count,
created_at,
created_by,
enabled,
ip_addresses,
label,
list_type,
updated_at,
updated_by
FROM databricks_workspace.settings.ip_access_lists
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

Creates an IP access list for this workspace.

```sql
INSERT INTO databricks_workspace.settings.ip_access_lists (
label,
list_type,
ip_addresses,
deployment_name
)
SELECT 
'{{ label }}' /* required */,
'{{ list_type }}' /* required */,
'{{ ip_addresses }}',
'{{ deployment_name }}'
RETURNING
ip_access_list
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ip_access_lists
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the ip_access_lists resource.
    - name: label
      value: "{{ label }}"
      description: |
        Label for the IP access list. This **cannot** be empty.
    - name: list_type
      value: "{{ list_type }}"
      description: |
        :param ip_addresses: List[str] (optional)
    - name: ip_addresses
      value:
        - "{{ ip_addresses }}"
`}</CodeBlock>

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

Updates an existing IP access list, specified by its ID.

```sql
UPDATE databricks_workspace.settings.ip_access_lists
SET 
enabled = {{ enabled }},
ip_addresses = '{{ ip_addresses }}',
label = '{{ label }}',
list_type = '{{ list_type }}'
WHERE 
ip_access_list_id = '{{ ip_access_list_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="replace"
    values={[
        { label: 'replace', value: 'replace' }
    ]}
>
<TabItem value="replace">

Replaces an IP access list, specified by its ID.

```sql
REPLACE databricks_workspace.settings.ip_access_lists
SET 
label = '{{ label }}',
list_type = '{{ list_type }}',
enabled = {{ enabled }},
ip_addresses = '{{ ip_addresses }}'
WHERE 
ip_access_list_id = '{{ ip_access_list_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND label = '{{ label }}' --required
AND list_type = '{{ list_type }}' --required
AND enabled = {{ enabled }} --required;
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

Deletes an IP access list, specified by its list ID.

```sql
DELETE FROM databricks_workspace.settings.ip_access_lists
WHERE ip_access_list_id = '{{ ip_access_list_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

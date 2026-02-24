---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
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

Creates, updates, deletes, gets or lists a <code>permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="permissions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.permissions" /></td></tr>
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
    "name": "object_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "access_control_list",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "all_permissions",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "inherited",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "inherited_from_object",
            "type": "array",
            "description": ""
          },
          {
            "name": "permission_level",
            "type": "string",
            "description": "Permission level (CAN_ATTACH_TO, CAN_BIND, CAN_CREATE, CAN_EDIT, CAN_EDIT_METADATA, CAN_MANAGE, CAN_MANAGE_PRODUCTION_VERSIONS, CAN_MANAGE_RUN, CAN_MANAGE_STAGING_VERSIONS, CAN_MONITOR, CAN_MONITOR_ONLY, CAN_QUERY, CAN_READ, CAN_RESTART, CAN_RUN, CAN_USE, CAN_VIEW, CAN_VIEW_METADATA, IS_OWNER)"
          }
        ]
      },
      {
        "name": "display_name",
        "type": "string",
        "description": "Display name of the user or service principal."
      },
      {
        "name": "group_name",
        "type": "string",
        "description": "name of the group"
      },
      {
        "name": "service_principal_name",
        "type": "string",
        "description": "Name of the service principal."
      },
      {
        "name": "user_name",
        "type": "string",
        "description": "name of the user"
      }
    ]
  },
  {
    "name": "object_type",
    "type": "string",
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-request_object_type"><code>request_object_type</code></a>, <a href="#parameter-request_object_id"><code>request_object_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets the permissions of an object. Objects can inherit permissions from their parent objects or root</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-request_object_type"><code>request_object_type</code></a>, <a href="#parameter-request_object_id"><code>request_object_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Updates the permissions on an object. Objects can inherit permissions from their parent objects or</td>
</tr>
<tr>
    <td><a href="#set"><CopyableCode code="set" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-request_object_type"><code>request_object_type</code></a>, <a href="#parameter-request_object_id"><code>request_object_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct</td>
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
<tr id="parameter-request_object_id">
    <td><CopyableCode code="request_object_id" /></td>
    <td><code>string</code></td>
    <td>The id of the request object.</td>
</tr>
<tr id="parameter-request_object_type">
    <td><CopyableCode code="request_object_type" /></td>
    <td><code>string</code></td>
    <td>The type of the request object. Can be one of the following: alerts, alertsv2, authorization, clusters, cluster-policies, dashboards, dbsql-dashboards, directories, experiments, files, genie, instance-pools, jobs, notebooks, pipelines, queries, registered-models, repos, serving-endpoints, or warehouses.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
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

Gets the permissions of an object. Objects can inherit permissions from their parent objects or root

```sql
SELECT
object_id,
access_control_list,
object_type
FROM databricks_workspace.iam.permissions
WHERE request_object_type = '{{ request_object_type }}' -- required
AND request_object_id = '{{ request_object_id }}' -- required
AND workspace = '{{ workspace }}' -- required
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

Updates the permissions on an object. Objects can inherit permissions from their parent objects or

```sql
UPDATE databricks_workspace.iam.permissions
SET 
access_control_list = '{{ access_control_list }}'
WHERE 
request_object_type = '{{ request_object_type }}' --required
AND request_object_id = '{{ request_object_id }}' --required
AND workspace = '{{ workspace }}' --required
RETURNING
object_id,
access_control_list,
object_type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="set"
    values={[
        { label: 'set', value: 'set' }
    ]}
>
<TabItem value="set">

Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct

```sql
REPLACE databricks_workspace.iam.permissions
SET 
access_control_list = '{{ access_control_list }}'
WHERE 
request_object_type = '{{ request_object_type }}' --required
AND request_object_id = '{{ request_object_id }}' --required
AND workspace = '{{ workspace }}' --required
RETURNING
object_id,
access_control_list,
object_type;
```
</TabItem>
</Tabs>

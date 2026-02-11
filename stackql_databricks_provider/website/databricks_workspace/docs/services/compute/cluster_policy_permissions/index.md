---
title: cluster_policy_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_policy_permissions
  - compute
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

Creates, updates, deletes, gets or lists a <code>cluster_policy_permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_policy_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.cluster_policy_permissions" /></td></tr>
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
            "description": "Permission level"
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
    <td><a href="#parameter-cluster_policy_id"><code>cluster_policy_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the permissions of a cluster policy. Cluster policies can inherit permissions from their root<br />object.<br /><br />:param cluster_policy_id: str<br />  The cluster policy for which to get or manage permissions.<br /><br />:returns: :class:`ClusterPolicyPermissions`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-cluster_policy_id"><code>cluster_policy_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the permissions on a cluster policy. Cluster policies can inherit permissions from their root<br />object.<br /><br />:param cluster_policy_id: str<br />  The cluster policy for which to get or manage permissions.<br />:param access_control_list: List[:class:`ClusterPolicyAccessControlRequest`] (optional)<br /><br />:returns: :class:`ClusterPolicyPermissions`</td>
</tr>
<tr>
    <td><a href="#set"><CopyableCode code="set" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-cluster_policy_id"><code>cluster_policy_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct<br />permissions if none are specified. Objects can inherit permissions from their root object.<br /><br />:param cluster_policy_id: str<br />  The cluster policy for which to get or manage permissions.<br />:param access_control_list: List[:class:`ClusterPolicyAccessControlRequest`] (optional)<br /><br />:returns: :class:`ClusterPolicyPermissions`</td>
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
<tr id="parameter-cluster_policy_id">
    <td><CopyableCode code="cluster_policy_id" /></td>
    <td><code>string</code></td>
    <td>The cluster policy for which to get or manage permissions.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
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

Gets the permissions of a cluster policy. Cluster policies can inherit permissions from their root<br />object.<br /><br />:param cluster_policy_id: str<br />  The cluster policy for which to get or manage permissions.<br /><br />:returns: :class:`ClusterPolicyPermissions`

```sql
SELECT
object_id,
access_control_list,
object_type
FROM databricks_workspace.compute.cluster_policy_permissions
WHERE cluster_policy_id = '{{ cluster_policy_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
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

Updates the permissions on a cluster policy. Cluster policies can inherit permissions from their root<br />object.<br /><br />:param cluster_policy_id: str<br />  The cluster policy for which to get or manage permissions.<br />:param access_control_list: List[:class:`ClusterPolicyAccessControlRequest`] (optional)<br /><br />:returns: :class:`ClusterPolicyPermissions`

```sql
UPDATE databricks_workspace.compute.cluster_policy_permissions
SET 
data__access_control_list = '{{ access_control_list }}'
WHERE 
cluster_policy_id = '{{ cluster_policy_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
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

Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct<br />permissions if none are specified. Objects can inherit permissions from their root object.<br /><br />:param cluster_policy_id: str<br />  The cluster policy for which to get or manage permissions.<br />:param access_control_list: List[:class:`ClusterPolicyAccessControlRequest`] (optional)<br /><br />:returns: :class:`ClusterPolicyPermissions`

```sql
REPLACE databricks_workspace.compute.cluster_policy_permissions
SET 
data__access_control_list = '{{ access_control_list }}'
WHERE 
cluster_policy_id = '{{ cluster_policy_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
object_id,
access_control_list,
object_type;
```
</TabItem>
</Tabs>

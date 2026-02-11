---
title: permission_levels
hide_title: false
hide_table_of_contents: false
keywords:
  - permission_levels
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

Creates, updates, deletes, gets or lists a <code>permission_levels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission_levels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.permission_levels" /></td></tr>
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
    "name": "permission_levels",
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
        "description": "Permission level"
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
    <td><a href="#parameter-request_object_type"><code>request_object_type</code></a>, <a href="#parameter-request_object_id"><code>request_object_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the permission levels that a user can have on an object.<br /><br />:param request_object_type: str<br />  The type of the request object. Can be one of the following: alerts, alertsv2, authorization,<br />  clusters, cluster-policies, dashboards, dbsql-dashboards, directories, experiments, files, genie,<br />  instance-pools, jobs, notebooks, pipelines, queries, registered-models, repos, serving-endpoints, or<br />  warehouses.<br />:param request_object_id: str<br /><br />:returns: :class:`GetPermissionLevelsResponse`</td>
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
<tr id="parameter-request_object_id">
    <td><CopyableCode code="request_object_id" /></td>
    <td><code>string</code></td>
    <td>:returns: :class:`GetPermissionLevelsResponse`</td>
</tr>
<tr id="parameter-request_object_type">
    <td><CopyableCode code="request_object_type" /></td>
    <td><code>string</code></td>
    <td>The type of the request object. Can be one of the following: alerts, alertsv2, authorization, clusters, cluster-policies, dashboards, dbsql-dashboards, directories, experiments, files, genie, instance-pools, jobs, notebooks, pipelines, queries, registered-models, repos, serving-endpoints, or warehouses.</td>
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

Gets the permission levels that a user can have on an object.<br /><br />:param request_object_type: str<br />  The type of the request object. Can be one of the following: alerts, alertsv2, authorization,<br />  clusters, cluster-policies, dashboards, dbsql-dashboards, directories, experiments, files, genie,<br />  instance-pools, jobs, notebooks, pipelines, queries, registered-models, repos, serving-endpoints, or<br />  warehouses.<br />:param request_object_id: str<br /><br />:returns: :class:`GetPermissionLevelsResponse`

```sql
SELECT
permission_levels
FROM databricks_workspace.iam.permission_levels
WHERE request_object_type = '{{ request_object_type }}' -- required
AND request_object_id = '{{ request_object_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>

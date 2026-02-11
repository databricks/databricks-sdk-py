---
title: postgres_branches
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_branches
  - postgres
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

Creates, updates, deletes, gets or lists a <code>postgres_branches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>postgres_branches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_branches" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Output only. The full resource path of the branch. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The project containing this branch (API resource hierarchy). Format: projects/&#123;project_id&#125; Note: This field indicates where the branch exists in the resource hierarchy. For point-in-time branching from another branch, see `status.source_branch`."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the branch configuration.",
    "children": [
      {
        "name": "expire_time",
        "type": "string (date-time)",
        "description": ""
      },
      {
        "name": "is_protected",
        "type": "boolean",
        "description": "When set to true, protects the branch from deletion and reset. Associated compute endpoints and the project cannot be deleted while the branch is protected."
      },
      {
        "name": "no_expiry",
        "type": "boolean",
        "description": "Explicitly disable expiration. When set to true, the branch will not expire. If set to false, the request is invalid; provide either ttl or expire_time instead."
      },
      {
        "name": "source_branch",
        "type": "string",
        "description": "The name of the source branch from which this branch was created (data lineage for point-in-time recovery). If not specified, defaults to the project's default branch. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      },
      {
        "name": "source_branch_lsn",
        "type": "string",
        "description": "The Log Sequence Number (LSN) on the source branch from which this branch was created."
      },
      {
        "name": "source_branch_time",
        "type": "string (date-time)",
        "description": "The point in time on the source branch from which this branch was created."
      },
      {
        "name": "ttl",
        "type": "string",
        "description": "Relative time-to-live duration. When set, the branch will expire at creation_time + ttl."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The current status of a Branch.",
    "children": [
      {
        "name": "current_state",
        "type": "string",
        "description": "The state of the branch."
      },
      {
        "name": "default",
        "type": "boolean",
        "description": "Whether the branch is the project's default branch."
      },
      {
        "name": "expire_time",
        "type": "string (date-time)",
        "description": "Absolute expiration time for the branch. Empty if expiration is disabled."
      },
      {
        "name": "is_protected",
        "type": "boolean",
        "description": "Whether the branch is protected."
      },
      {
        "name": "logical_size_bytes",
        "type": "integer",
        "description": "The logical size of the branch."
      },
      {
        "name": "pending_state",
        "type": "string",
        "description": "The state of the branch."
      },
      {
        "name": "source_branch",
        "type": "string",
        "description": "The name of the source branch from which this branch was created. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      },
      {
        "name": "source_branch_lsn",
        "type": "string",
        "description": "The Log Sequence Number (LSN) on the source branch from which this branch was created."
      },
      {
        "name": "source_branch_time",
        "type": "string (date-time)",
        "description": "The point in time on the source branch from which this branch was created."
      },
      {
        "name": "state_change_time",
        "type": "string (date-time)",
        "description": "A timestamp indicating when the `current_state` began."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "System-generated unique ID for the branch."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the branch was last updated."
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns a paginated list of database branches in the project.<br /><br />:param parent: str<br />  The Project that owns this collection of branches. Format: projects/&#123;project_id&#125;<br />:param page_size: int (optional)<br />  Upper bound for items returned. Cannot be negative.<br />:param page_token: str (optional)<br />  Page token from a previous response. If not provided, returns the first page.<br /><br />:returns: Iterator over :class:`Branch`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__branch"><code>data__branch</code></a></td>
    <td></td>
    <td>Creates a new database branch in the project.<br /><br />:param parent: str<br />  The Project where this Branch will be created. Format: projects/&#123;project_id&#125;<br />:param branch: :class:`Branch`<br />  The Branch to create.<br />:param branch_id: str<br />  The ID to use for the Branch. This becomes the final component of the branch's resource name. The ID<br />  is required and must be 1-63 characters long, start with a lowercase letter, and contain only<br />  lowercase letters, numbers, and hyphens. For example, `development` becomes<br />  `projects/my-app/branches/development`.<br /><br />:returns: :class:`Operation`</td>
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
<tr id="parameter-branch_id">
    <td><CopyableCode code="branch_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the Branch. This becomes the final component of the branch's resource name. The ID is required and must be 1-63 characters long, start with a lowercase letter, and contain only lowercase letters, numbers, and hyphens. For example, `development` becomes `projects/my-app/branches/development`.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>The Project where this Branch will be created. Format: projects/&#123;project_id&#125;</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>Upper bound for items returned. Cannot be negative.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token from a previous response. If not provided, returns the first page.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Returns a paginated list of database branches in the project.<br /><br />:param parent: str<br />  The Project that owns this collection of branches. Format: projects/&#123;project_id&#125;<br />:param page_size: int (optional)<br />  Upper bound for items returned. Cannot be negative.<br />:param page_token: str (optional)<br />  Page token from a previous response. If not provided, returns the first page.<br /><br />:returns: Iterator over :class:`Branch`

```sql
SELECT
name,
create_time,
parent,
spec,
status,
uid,
update_time
FROM databricks_workspace.postgres.postgres_branches
WHERE parent = '{{ parent }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
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

Creates a new database branch in the project.<br /><br />:param parent: str<br />  The Project where this Branch will be created. Format: projects/&#123;project_id&#125;<br />:param branch: :class:`Branch`<br />  The Branch to create.<br />:param branch_id: str<br />  The ID to use for the Branch. This becomes the final component of the branch's resource name. The ID<br />  is required and must be 1-63 characters long, start with a lowercase letter, and contain only<br />  lowercase letters, numbers, and hyphens. For example, `development` becomes<br />  `projects/my-app/branches/development`.<br /><br />:returns: :class:`Operation`

```sql
INSERT INTO databricks_workspace.postgres.postgres_branches (
data__branch,
parent,
branch_id,
deployment_name
)
SELECT 
'{{ branch }}' /* required */,
'{{ parent }}',
'{{ branch_id }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: postgres_branches
  props:
    - name: parent
      value: string
      description: Required parameter for the postgres_branches resource.
    - name: branch_id
      value: string
      description: Required parameter for the postgres_branches resource.
    - name: deployment_name
      value: string
      description: Required parameter for the postgres_branches resource.
    - name: branch
      value: string
      description: |
        The Branch to create.
```
</TabItem>
</Tabs>

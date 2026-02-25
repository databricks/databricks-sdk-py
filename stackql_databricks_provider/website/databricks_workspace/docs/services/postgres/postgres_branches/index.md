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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>postgres_branches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_branches" /></td></tr>
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
        "description": "The state of the branch. (ARCHIVED, IMPORTING, INIT, READY, RESETTING)"
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
        "description": "The state of the branch. (ARCHIVED, IMPORTING, INIT, READY, RESETTING)"
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
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns a paginated list of database branches in the project.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-branch"><code>branch</code></a></td>
    <td></td>
    <td>Creates a new database branch in the project.</td>
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
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>The Project where this Branch will be created. Format: projects/&#123;project_id&#125;</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
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

Returns a paginated list of database branches in the project.

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
AND workspace = '{{ workspace }}' -- required
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

Creates a new database branch in the project.

```sql
INSERT INTO databricks_workspace.postgres.postgres_branches (
branch,
parent,
branch_id,
workspace
)
SELECT 
'{{ branch }}' /* required */,
'{{ parent }}',
'{{ branch_id }}',
'{{ workspace }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_branches
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the postgres_branches resource.
    - name: branch_id
      value: "{{ branch_id }}"
      description: Required parameter for the postgres_branches resource.
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the postgres_branches resource.
    - name: branch
      description: |
        The Branch to create.
      value:
        create_time: "{{ create_time }}"
        name: "{{ name }}"
        parent: "{{ parent }}"
        spec:
          expire_time: "{{ expire_time }}"
          is_protected: {{ is_protected }}
          no_expiry: {{ no_expiry }}
          source_branch: "{{ source_branch }}"
          source_branch_lsn: "{{ source_branch_lsn }}"
          source_branch_time: "{{ source_branch_time }}"
          ttl: "{{ ttl }}"
        status:
          current_state: "{{ current_state }}"
          default: {{ default }}
          expire_time: "{{ expire_time }}"
          is_protected: {{ is_protected }}
          logical_size_bytes: {{ logical_size_bytes }}
          pending_state: "{{ pending_state }}"
          source_branch: "{{ source_branch }}"
          source_branch_lsn: "{{ source_branch_lsn }}"
          source_branch_time: "{{ source_branch_time }}"
          state_change_time: "{{ state_change_time }}"
        uid: "{{ uid }}"
        update_time: "{{ update_time }}"
`}</CodeBlock>

</TabItem>
</Tabs>

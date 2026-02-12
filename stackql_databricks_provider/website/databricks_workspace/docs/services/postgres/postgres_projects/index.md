---
title: postgres_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_projects
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

Creates, updates, deletes, gets or lists a <code>postgres_projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>postgres_projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_projects" /></td></tr>
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
    "description": "Output only. The full resource path of the project. Format: projects/&#123;project_id&#125;"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the project configuration, including display_name, pg_version (Postgres version), history_retention_duration, and default_endpoint_settings.",
    "children": [
      {
        "name": "default_endpoint_settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "autoscaling_limit_max_cu",
            "type": "number",
            "description": "The maximum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "autoscaling_limit_min_cu",
            "type": "number",
            "description": "The minimum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "no_suspension",
            "type": "boolean",
            "description": "When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided."
          },
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          },
          {
            "name": "suspend_timeout_duration",
            "type": "string",
            "description": "Duration of inactivity after which the compute endpoint is automatically suspended. If specified should be between 60s and 604800s (1 minute to 1 week)."
          }
        ]
      },
      {
        "name": "display_name",
        "type": "string",
        "description": "Human-readable project name. Length should be between 1 and 256 characters."
      },
      {
        "name": "history_retention_duration",
        "type": "string",
        "description": "The number of seconds to retain the shared history for point in time recovery for all branches in this project. Value should be between 0s and 2592000s (up to 30 days)."
      },
      {
        "name": "pg_version",
        "type": "integer",
        "description": "The major Postgres version number. Supported versions are 16 and 17."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The current status of a Project.",
    "children": [
      {
        "name": "branch_logical_size_limit_bytes",
        "type": "integer",
        "description": ""
      },
      {
        "name": "default_endpoint_settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "autoscaling_limit_max_cu",
            "type": "number",
            "description": "The maximum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "autoscaling_limit_min_cu",
            "type": "number",
            "description": "The minimum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "no_suspension",
            "type": "boolean",
            "description": "When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided."
          },
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          },
          {
            "name": "suspend_timeout_duration",
            "type": "string",
            "description": "Duration of inactivity after which the compute endpoint is automatically suspended. If specified should be between 60s and 604800s (1 minute to 1 week)."
          }
        ]
      },
      {
        "name": "display_name",
        "type": "string",
        "description": "The effective human-readable project name."
      },
      {
        "name": "history_retention_duration",
        "type": "string",
        "description": "The effective number of seconds to retain the shared history for point in time recovery."
      },
      {
        "name": "owner",
        "type": "string",
        "description": "The email of the project owner."
      },
      {
        "name": "pg_version",
        "type": "integer",
        "description": "The effective major Postgres version number."
      },
      {
        "name": "synthetic_storage_size_bytes",
        "type": "integer",
        "description": "The current space occupied by the project in storage."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "System-generated unique ID for the project."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the project was last updated."
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
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns a paginated list of database projects in the workspace that the user has permission to access.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__project"><code>data__project</code></a></td>
    <td></td>
    <td>Creates a new Lakebase Autoscaling Postgres database project, which contains branches and compute</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__project"><code>data__project</code></a></td>
    <td></td>
    <td>Updates the specified database project.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Output only. The full resource path of the project. Format: projects/&#123;project_id&#125;</td>
</tr>
<tr id="parameter-project_id">
    <td><CopyableCode code="project_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the Project. This becomes the final component of the project's resource name. The ID is required and must be 1-63 characters long, start with a lowercase letter, and contain only lowercase letters, numbers, and hyphens. For example, `my-app` becomes `projects/my-app`.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>The list of fields to update. If unspecified, all fields will be updated when possible.</td>
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

Returns a paginated list of database projects in the workspace that the user has permission to access.

```sql
SELECT
name,
create_time,
spec,
status,
uid,
update_time
FROM databricks_workspace.postgres.postgres_projects
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Creates a new Lakebase Autoscaling Postgres database project, which contains branches and compute

```sql
INSERT INTO databricks_workspace.postgres.postgres_projects (
data__project,
project_id,
deployment_name
)
SELECT 
'{{ project }}' /* required */,
'{{ project_id }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: postgres_projects
  props:
    - name: project_id
      value: string
      description: Required parameter for the postgres_projects resource.
    - name: deployment_name
      value: string
      description: Required parameter for the postgres_projects resource.
    - name: project
      value: string
      description: |
        The Project to create.
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

Updates the specified database project.

```sql
UPDATE databricks_workspace.postgres.postgres_projects
SET 
data__project = '{{ project }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__project = '{{ project }}' --required;
```
</TabItem>
</Tabs>

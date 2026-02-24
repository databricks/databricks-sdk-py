---
title: postgres_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_endpoints
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

Creates, updates, deletes, gets or lists a <code>postgres_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_endpoints" /></td></tr>
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
    "description": "Output only. The full resource path of the endpoint. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/endpoints/&#123;endpoint_id&#125;"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The branch containing this endpoint (API resource hierarchy). Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the compute endpoint configuration, including autoscaling limits, suspend timeout, and disabled state.",
    "children": [
      {
        "name": "endpoint_type",
        "type": "string",
        "description": "The compute endpoint type. Either `read_write` or `read_only`. (ENDPOINT_TYPE_READ_ONLY, ENDPOINT_TYPE_READ_WRITE)"
      },
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
        "name": "disabled",
        "type": "boolean",
        "description": "Whether to restrict connections to the compute endpoint. Enabling this option schedules a suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or console action."
      },
      {
        "name": "no_suspension",
        "type": "boolean",
        "description": "When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided."
      },
      {
        "name": "settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          }
        ]
      },
      {
        "name": "suspend_timeout_duration",
        "type": "string",
        "description": "Duration of inactivity after which the compute endpoint is automatically suspended. If specified should be between 60s and 604800s (1 minute to 1 week)."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Current operational status of the compute endpoint.",
    "children": [
      {
        "name": "autoscaling_limit_max_cu",
        "type": "number",
        "description": ""
      },
      {
        "name": "autoscaling_limit_min_cu",
        "type": "number",
        "description": "The minimum number of Compute Units."
      },
      {
        "name": "current_state",
        "type": "string",
        "description": "The state of the compute endpoint. (ACTIVE, IDLE, INIT)"
      },
      {
        "name": "disabled",
        "type": "boolean",
        "description": "Whether to restrict connections to the compute endpoint. Enabling this option schedules a suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or console action."
      },
      {
        "name": "endpoint_type",
        "type": "string",
        "description": "The compute endpoint type. Either `read_write` or `read_only`. (ENDPOINT_TYPE_READ_ONLY, ENDPOINT_TYPE_READ_WRITE)"
      },
      {
        "name": "hosts",
        "type": "object",
        "description": "Contains host information for connecting to the endpoint.",
        "children": [
          {
            "name": "host",
            "type": "string",
            "description": "The hostname to connect to this endpoint. For read-write endpoints, this is a read-write hostname which connects to the primary compute. For read-only endpoints, this is a read-only hostname which allows read-only operations."
          }
        ]
      },
      {
        "name": "pending_state",
        "type": "string",
        "description": "The state of the compute endpoint. (ACTIVE, IDLE, INIT)"
      },
      {
        "name": "settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          }
        ]
      },
      {
        "name": "suspend_timeout_duration",
        "type": "string",
        "description": "Duration of inactivity after which the compute endpoint is automatically suspended."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "System-generated unique ID for the endpoint."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the compute endpoint was last updated."
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
    <td>Returns a paginated list of compute endpoints in the branch.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-endpoint_id"><code>endpoint_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates a new compute endpoint in the branch.</td>
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
<tr id="parameter-endpoint_id">
    <td><CopyableCode code="endpoint_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the Endpoint. This becomes the final component of the endpoint's resource name. The ID is required and must be 1-63 characters long, start with a lowercase letter, and contain only lowercase letters, numbers, and hyphens. For example, `primary` becomes `projects/my-app/branches/development/endpoints/primary`.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>The Branch where this Endpoint will be created. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;</td>
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

Returns a paginated list of compute endpoints in the branch.

```sql
SELECT
name,
create_time,
parent,
spec,
status,
uid,
update_time
FROM databricks_workspace.postgres.postgres_endpoints
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

Creates a new compute endpoint in the branch.

```sql
INSERT INTO databricks_workspace.postgres.postgres_endpoints (
endpoint,
parent,
endpoint_id,
workspace
)
SELECT 
'{{ endpoint }}' /* required */,
'{{ parent }}',
'{{ endpoint_id }}',
'{{ workspace }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: postgres_endpoints
  props:
    - name: parent
      value: string
      description: Required parameter for the postgres_endpoints resource.
    - name: endpoint_id
      value: string
      description: Required parameter for the postgres_endpoints resource.
    - name: workspace
      value: string
      description: Required parameter for the postgres_endpoints resource.
    - name: endpoint
      value: object
      description: |
        The Endpoint to create.
      props:
      - name: create_time
        value: string
      - name: name
        value: string
        description: |
          Output only. The full resource path of the endpoint. Format: projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
      - name: parent
        value: string
        description: |
          The branch containing this endpoint (API resource hierarchy). Format: projects/{project_id}/branches/{branch_id}
      - name: spec
        value: object
        description: |
          The spec contains the compute endpoint configuration, including autoscaling limits, suspend timeout, and disabled state.
        props:
        - name: endpoint_type
          value: string
          description: |
            The compute endpoint type. Either `read_write` or `read_only`.
        - name: autoscaling_limit_max_cu
          value: number
          description: |
            The maximum number of Compute Units. Minimum value is 0.5.
        - name: autoscaling_limit_min_cu
          value: number
          description: |
            The minimum number of Compute Units. Minimum value is 0.5.
        - name: disabled
          value: boolean
          description: |
            Whether to restrict connections to the compute endpoint. Enabling this option schedules a suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or console action.
        - name: no_suspension
          value: boolean
          description: |
            When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided.
        - name: settings
          value: object
          description: |
            A collection of settings for a compute endpoint.
          props:
          - name: pg_settings
            value: object
            description: |
              A raw representation of Postgres settings.
        - name: suspend_timeout_duration
          value: string
          description: |
            Duration of inactivity after which the compute endpoint is automatically suspended. If specified should be between 60s and 604800s (1 minute to 1 week).
      - name: status
        value: object
        description: |
          Current operational status of the compute endpoint.
        props:
        - name: autoscaling_limit_max_cu
          value: number
        - name: autoscaling_limit_min_cu
          value: number
          description: |
            The minimum number of Compute Units.
        - name: current_state
          value: string
          description: |
            The state of the compute endpoint.
        - name: disabled
          value: boolean
          description: |
            Whether to restrict connections to the compute endpoint. Enabling this option schedules a suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or console action.
        - name: endpoint_type
          value: string
          description: |
            The endpoint type. A branch can only have one READ_WRITE endpoint.
        - name: hosts
          value: object
          description: |
            Contains host information for connecting to the endpoint.
          props:
          - name: host
            value: string
            description: |
              The hostname to connect to this endpoint. For read-write endpoints, this is a read-write hostname which connects to the primary compute. For read-only endpoints, this is a read-only hostname which allows read-only operations.
        - name: pending_state
          value: string
          description: |
            The state of the compute endpoint.
        - name: settings
          value: object
          description: |
            A collection of settings for a compute endpoint.
          props:
          - name: pg_settings
            value: object
            description: |
              A raw representation of Postgres settings.
        - name: suspend_timeout_duration
          value: string
          description: |
            Duration of inactivity after which the compute endpoint is automatically suspended.
      - name: uid
        value: string
        description: |
          System-generated unique ID for the endpoint.
      - name: update_time
        value: string
        description: |
          A timestamp indicating when the compute endpoint was last updated.
```
</TabItem>
</Tabs>

---
title: quality_monitor_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - quality_monitor_v2
  - qualitymonitorv2
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

Creates, updates, deletes, gets or lists a <code>quality_monitor_v2</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quality_monitor_v2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.qualitymonitorv2.quality_monitor_v2" /></td></tr>
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
    "name": "object_id",
    "type": "string",
    "description": "The uuid of the request object. For example, schema id."
  },
  {
    "name": "anomaly_detection_config",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "excluded_table_full_names",
        "type": "array",
        "description": ""
      },
      {
        "name": "last_run_id",
        "type": "string",
        "description": "Run id of the last run of the workflow"
      },
      {
        "name": "latest_run_status",
        "type": "string",
        "description": "The status of the last run of the workflow."
      }
    ]
  },
  {
    "name": "object_type",
    "type": "string",
    "description": ""
  },
  {
    "name": "validity_check_configurations",
    "type": "array",
    "description": "Validity check configurations for anomaly detection.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "percent_null_validity_check",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "column_names",
            "type": "array",
            "description": ""
          },
          {
            "name": "upper_bound",
            "type": "number",
            "description": "Optional upper bound; we should use auto determined bounds for now"
          }
        ]
      },
      {
        "name": "range_validity_check",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "column_names",
            "type": "array",
            "description": ""
          },
          {
            "name": "lower_bound",
            "type": "number",
            "description": "Lower bound for the range"
          },
          {
            "name": "upper_bound",
            "type": "number",
            "description": "Upper bound for the range"
          }
        ]
      },
      {
        "name": "uniqueness_validity_check",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "column_names",
            "type": "array",
            "description": ""
          }
        ]
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "object_id",
    "type": "string",
    "description": "The uuid of the request object. For example, schema id."
  },
  {
    "name": "anomaly_detection_config",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "excluded_table_full_names",
        "type": "array",
        "description": ""
      },
      {
        "name": "last_run_id",
        "type": "string",
        "description": "Run id of the last run of the workflow"
      },
      {
        "name": "latest_run_status",
        "type": "string",
        "description": "The status of the last run of the workflow."
      }
    ]
  },
  {
    "name": "object_type",
    "type": "string",
    "description": ""
  },
  {
    "name": "validity_check_configurations",
    "type": "array",
    "description": "Validity check configurations for anomaly detection.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "percent_null_validity_check",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "column_names",
            "type": "array",
            "description": ""
          },
          {
            "name": "upper_bound",
            "type": "number",
            "description": "Optional upper bound; we should use auto determined bounds for now"
          }
        ]
      },
      {
        "name": "range_validity_check",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "column_names",
            "type": "array",
            "description": ""
          },
          {
            "name": "lower_bound",
            "type": "number",
            "description": "Lower bound for the range"
          },
          {
            "name": "upper_bound",
            "type": "number",
            "description": "Upper bound for the range"
          }
        ]
      },
      {
        "name": "uniqueness_validity_check",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "column_names",
            "type": "array",
            "description": ""
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
    <td><a href="#parameter-object_type"><code>object_type</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>[DEPRECATED] Read a quality monitor on UC object. Use Data Quality Monitoring API instead.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>[DEPRECATED] (Unimplemented) List quality monitors. Use Data Quality Monitoring API instead.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__quality_monitor"><code>data__quality_monitor</code></a></td>
    <td></td>
    <td>[DEPRECATED] Create a quality monitor on UC object. Use Data Quality Monitoring API instead.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-object_type"><code>object_type</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__quality_monitor"><code>data__quality_monitor</code></a></td>
    <td></td>
    <td>[DEPRECATED] (Unimplemented) Update a quality monitor on UC object. Use Data Quality Monitoring API</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-object_type"><code>object_type</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>[DEPRECATED] Delete a quality monitor on UC object. Use Data Quality Monitoring API instead.</td>
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
<tr id="parameter-object_id">
    <td><CopyableCode code="object_id" /></td>
    <td><code>string</code></td>
    <td>The uuid of the request object. For example, schema id.</td>
</tr>
<tr id="parameter-object_type">
    <td><CopyableCode code="object_type" /></td>
    <td><code>string</code></td>
    <td>The type of the monitored object. Can be one of the following: schema.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>:param page_token: str (optional)</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td></td>
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

[DEPRECATED] Read a quality monitor on UC object. Use Data Quality Monitoring API instead.

```sql
SELECT
object_id,
anomaly_detection_config,
object_type,
validity_check_configurations
FROM databricks_workspace.qualitymonitorv2.quality_monitor_v2
WHERE object_type = '{{ object_type }}' -- required
AND object_id = '{{ object_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

[DEPRECATED] (Unimplemented) List quality monitors. Use Data Quality Monitoring API instead.

```sql
SELECT
object_id,
anomaly_detection_config,
object_type,
validity_check_configurations
FROM databricks_workspace.qualitymonitorv2.quality_monitor_v2
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

[DEPRECATED] Create a quality monitor on UC object. Use Data Quality Monitoring API instead.

```sql
INSERT INTO databricks_workspace.qualitymonitorv2.quality_monitor_v2 (
data__quality_monitor,
deployment_name
)
SELECT 
'{{ quality_monitor }}' /* required */,
'{{ deployment_name }}'
RETURNING
object_id,
anomaly_detection_config,
object_type,
validity_check_configurations
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: quality_monitor_v2
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the quality_monitor_v2 resource.
    - name: quality_monitor
      value: string
      description: |
        :returns: :class:`QualityMonitor`
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

[DEPRECATED] (Unimplemented) Update a quality monitor on UC object. Use Data Quality Monitoring API

```sql
REPLACE databricks_workspace.qualitymonitorv2.quality_monitor_v2
SET 
data__quality_monitor = '{{ quality_monitor }}'
WHERE 
object_type = '{{ object_type }}' --required
AND object_id = '{{ object_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__quality_monitor = '{{ quality_monitor }}' --required
RETURNING
object_id,
anomaly_detection_config,
object_type,
validity_check_configurations;
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

[DEPRECATED] Delete a quality monitor on UC object. Use Data Quality Monitoring API instead.

```sql
DELETE FROM databricks_workspace.qualitymonitorv2.quality_monitor_v2
WHERE object_type = '{{ object_type }}' --required
AND object_id = '{{ object_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

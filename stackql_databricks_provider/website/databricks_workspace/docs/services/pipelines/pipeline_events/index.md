---
title: pipeline_events
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_events
  - pipelines
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

Creates, updates, deletes, gets or lists a <code>pipeline_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pipeline_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.pipelines.pipeline_events" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": "A time-based, globally unique id."
  },
  {
    "name": "error",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "exceptions",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "class_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "message",
            "type": "string",
            "description": "Exception message"
          },
          {
            "name": "stack",
            "type": "array",
            "description": "Stack trace consisting of a list of stack frames",
            "children": [
              {
                "name": "declaring_class",
                "type": "string",
                "description": ""
              },
              {
                "name": "file_name",
                "type": "string",
                "description": "File where the method is defined"
              },
              {
                "name": "line_number",
                "type": "integer",
                "description": "Line from which the method was called"
              },
              {
                "name": "method_name",
                "type": "string",
                "description": "Name of the method which was called"
              }
            ]
          }
        ]
      },
      {
        "name": "fatal",
        "type": "boolean",
        "description": "Whether this error is considered fatal, that is, unrecoverable."
      }
    ]
  },
  {
    "name": "event_type",
    "type": "string",
    "description": "The event type. Should always correspond to the details"
  },
  {
    "name": "level",
    "type": "string",
    "description": "The severity level of the event. (ERROR, INFO, METRICS, WARN)"
  },
  {
    "name": "maturity_level",
    "type": "string",
    "description": "Maturity level for event_type. (DEPRECATED, EVOLVING, STABLE)"
  },
  {
    "name": "message",
    "type": "string",
    "description": "The display message associated with the event."
  },
  {
    "name": "origin",
    "type": "object",
    "description": "Describes where the event originates from.",
    "children": [
      {
        "name": "batch_id",
        "type": "integer",
        "description": ""
      },
      {
        "name": "cloud",
        "type": "string",
        "description": "The cloud provider, e.g., AWS or Azure."
      },
      {
        "name": "cluster_id",
        "type": "string",
        "description": "The id of the cluster where an execution happens. Unique within a region."
      },
      {
        "name": "dataset_name",
        "type": "string",
        "description": "The name of a dataset. Unique within a pipeline."
      },
      {
        "name": "flow_id",
        "type": "string",
        "description": "The id of the flow. Globally unique. Incremental queries will generally reuse the same id while complete queries will have a new id per update."
      },
      {
        "name": "flow_name",
        "type": "string",
        "description": "The name of the flow. Not unique."
      },
      {
        "name": "host",
        "type": "string",
        "description": "The optional host name where the event was triggered"
      },
      {
        "name": "maintenance_id",
        "type": "string",
        "description": "The id of a maintenance run. Globally unique."
      },
      {
        "name": "materialization_name",
        "type": "string",
        "description": "Materialization name."
      },
      {
        "name": "org_id",
        "type": "integer",
        "description": "The org id of the user. Unique within a cloud."
      },
      {
        "name": "pipeline_id",
        "type": "string",
        "description": "The id of the pipeline. Globally unique."
      },
      {
        "name": "pipeline_name",
        "type": "string",
        "description": "The name of the pipeline. Not unique."
      },
      {
        "name": "region",
        "type": "string",
        "description": "The cloud region."
      },
      {
        "name": "request_id",
        "type": "string",
        "description": "The id of the request that caused an update."
      },
      {
        "name": "table_id",
        "type": "string",
        "description": "The id of a (delta) table. Globally unique."
      },
      {
        "name": "uc_resource_id",
        "type": "string",
        "description": "The Unity Catalog id of the MV or ST being updated."
      },
      {
        "name": "update_id",
        "type": "string",
        "description": "The id of an execution. Globally unique."
      }
    ]
  },
  {
    "name": "sequence",
    "type": "object",
    "description": "A sequencing object to identify and order events.",
    "children": [
      {
        "name": "control_plane_seq_no",
        "type": "integer",
        "description": ""
      },
      {
        "name": "data_plane_id",
        "type": "object",
        "description": "the ID assigned by the data plane.",
        "children": [
          {
            "name": "instance",
            "type": "string",
            "description": ""
          },
          {
            "name": "seq_no",
            "type": "integer",
            "description": "A sequence number, unique and increasing within the data plane instance."
          }
        ]
      }
    ]
  },
  {
    "name": "timestamp",
    "type": "string",
    "description": "The time of the event."
  },
  {
    "name": "truncation",
    "type": "object",
    "description": "Information about which fields were truncated from this event due to size constraints. If empty or absent, no truncation occurred. See https://docs.databricks.com/en/ldp/monitor-event-logs for information on retrieving complete event data.",
    "children": [
      {
        "name": "truncated_fields",
        "type": "array",
        "description": "List of fields that were truncated from this event. If empty or absent, no truncation occurred.",
        "children": [
          {
            "name": "field_name",
            "type": "string",
            "description": "The name of the truncated field (e.g., \"error\"). Corresponds to field names in PipelineEvent."
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pipeline_id"><code>pipeline_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Retrieves events for a pipeline.</td>
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
<tr id="parameter-pipeline_id">
    <td><CopyableCode code="pipeline_id" /></td>
    <td><code>string</code></td>
    <td>The pipeline to return events for.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Criteria to select a subset of results, expressed using a SQL-like syntax. The supported filters are: 1. level='INFO' (or WARN or ERROR) 2. level in ('INFO', 'WARN') 3. id='[event-id]' 4. timestamp &gt; 'TIMESTAMP' (or &gt;=,&lt;,&lt;=,=) Composite expressions are supported, for example: level in ('ERROR', 'WARN') AND timestamp&gt; '2021-07-22T06:37:33.083Z'</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
    <td>Max number of entries to return in a single page. The system may return fewer than max_results events in a response, even if there are more events available.</td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>array</code></td>
    <td>A string indicating a sort order by timestamp for the results, for example, ["timestamp asc"]. The sort order can be ascending or descending. By default, events are returned in descending order by timestamp.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token returned by previous call. This field is mutually exclusive with all fields in this request except max_results. An error is returned if any fields other than max_results are set when this field is set.</td>
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

Retrieves events for a pipeline.

```sql
SELECT
id,
error,
event_type,
level,
maturity_level,
message,
origin,
sequence,
timestamp,
truncation
FROM databricks_workspace.pipelines.pipeline_events
WHERE pipeline_id = '{{ pipeline_id }}' -- required
AND workspace = '{{ workspace }}' -- required
AND filter = '{{ filter }}'
AND max_results = '{{ max_results }}'
AND order_by = '{{ order_by }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>

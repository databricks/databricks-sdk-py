---
title: query_history
hide_title: false
hide_table_of_contents: false
keywords:
  - query_history
  - sql
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

Creates, updates, deletes, gets or lists a <code>query_history</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>query_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.query_history" /></td></tr>
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
    "name": "has_next_page",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "next_page_token",
    "type": "string",
    "description": "A token that can be used to get the next page of results."
  },
  {
    "name": "res",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "cache_query_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "channel_used",
        "type": "object",
        "description": "SQL Warehouse channel information at the time of query execution",
        "children": [
          {
            "name": "dbsql_version",
            "type": "string",
            "description": "DB SQL Version the Channel is mapped to."
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the channel"
          }
        ]
      },
      {
        "name": "client_application",
        "type": "string",
        "description": "Client application that ran the statement. For example: Databricks SQL Editor, Tableau, and Power BI. This field is derived from information provided by client applications. While values are expected to remain static over time, this cannot be guaranteed."
      },
      {
        "name": "duration",
        "type": "integer",
        "description": "Total time of the statement execution. This value does not include the time taken to retrieve the results, which can result in a discrepancy between this value and the start-to-finish wall-clock time."
      },
      {
        "name": "endpoint_id",
        "type": "string",
        "description": "Alias for `warehouse_id`."
      },
      {
        "name": "error_message",
        "type": "string",
        "description": "Message describing why the query could not complete."
      },
      {
        "name": "executed_as_user_id",
        "type": "integer",
        "description": "The ID of the user whose credentials were used to run the query."
      },
      {
        "name": "executed_as_user_name",
        "type": "string",
        "description": "The email address or username of the user whose credentials were used to run the query."
      },
      {
        "name": "execution_end_time_ms",
        "type": "integer",
        "description": "The time execution of the query ended."
      },
      {
        "name": "is_final",
        "type": "boolean",
        "description": "Whether more updates for the query are expected."
      },
      {
        "name": "lookup_key",
        "type": "string",
        "description": "A key that can be used to look up query details."
      },
      {
        "name": "metrics",
        "type": "object",
        "description": "Metrics about query execution.",
        "children": [
          {
            "name": "compilation_time_ms",
            "type": "integer",
            "description": "Time spent loading metadata and optimizing the query, in milliseconds."
          },
          {
            "name": "execution_time_ms",
            "type": "integer",
            "description": "Time spent executing the query, in milliseconds."
          },
          {
            "name": "network_sent_bytes",
            "type": "integer",
            "description": "Total amount of data sent over the network between executor nodes during shuffle, in bytes."
          },
          {
            "name": "overloading_queue_start_timestamp",
            "type": "integer",
            "description": "Timestamp of when the query was enqueued waiting while the warehouse was at max load. This field is optional and will not appear if the query skipped the overloading queue."
          },
          {
            "name": "photon_total_time_ms",
            "type": "integer",
            "description": "Total execution time for all individual Photon query engine tasks in the query, in milliseconds."
          },
          {
            "name": "projected_remaining_task_total_time_ms",
            "type": "integer",
            "description": "projected remaining work to be done aggregated across all stages in the query, in milliseconds"
          },
          {
            "name": "projected_remaining_wallclock_time_ms",
            "type": "integer",
            "description": "projected lower bound on remaining total task time based on projected_remaining_task_total_time_ms / maximum concurrency"
          },
          {
            "name": "provisioning_queue_start_timestamp",
            "type": "integer",
            "description": "Timestamp of when the query was enqueued waiting for a cluster to be provisioned for the warehouse. This field is optional and will not appear if the query skipped the provisioning queue."
          },
          {
            "name": "pruned_bytes",
            "type": "integer",
            "description": "Total number of file bytes in all tables not read due to pruning"
          },
          {
            "name": "pruned_files_count",
            "type": "integer",
            "description": "Total number of files from all tables not read due to pruning"
          },
          {
            "name": "query_compilation_start_timestamp",
            "type": "integer",
            "description": "Timestamp of when the underlying compute started compilation of the query."
          },
          {
            "name": "read_bytes",
            "type": "integer",
            "description": "Total size of data read by the query, in bytes."
          },
          {
            "name": "read_cache_bytes",
            "type": "integer",
            "description": "Size of persistent data read from the cache, in bytes."
          },
          {
            "name": "read_files_bytes",
            "type": "integer",
            "description": "Total number of file bytes in all tables read"
          },
          {
            "name": "read_files_count",
            "type": "integer",
            "description": "Number of files read after pruning"
          },
          {
            "name": "read_partitions_count",
            "type": "integer",
            "description": "Number of partitions read after pruning."
          },
          {
            "name": "read_remote_bytes",
            "type": "integer",
            "description": "Size of persistent data read from cloud object storage on your cloud tenant, in bytes."
          },
          {
            "name": "remaining_task_count",
            "type": "integer",
            "description": "number of remaining tasks to complete this is based on the current status and could be bigger or smaller in the future based on future updates"
          },
          {
            "name": "result_fetch_time_ms",
            "type": "integer",
            "description": "Time spent fetching the query results after the execution finished, in milliseconds."
          },
          {
            "name": "result_from_cache",
            "type": "boolean",
            "description": "`true` if the query result was fetched from cache, `false` otherwise."
          },
          {
            "name": "rows_produced_count",
            "type": "integer",
            "description": "Total number of rows returned by the query."
          },
          {
            "name": "rows_read_count",
            "type": "integer",
            "description": "Total number of rows read by the query."
          },
          {
            "name": "runnable_tasks",
            "type": "integer",
            "description": "number of remaining tasks to complete, calculated by autoscaler StatementAnalysis.scala deprecated: use remaining_task_count instead"
          },
          {
            "name": "spill_to_disk_bytes",
            "type": "integer",
            "description": "Size of data temporarily written to disk while executing the query, in bytes."
          },
          {
            "name": "task_time_over_time_range",
            "type": "object",
            "description": "sum of task times completed in a range of wall clock time, approximated to a configurable number of points aggregated over all stages and jobs in the query (based on task_total_time_ms)",
            "children": [
              {
                "name": "entries",
                "type": "array",
                "description": ""
              },
              {
                "name": "interval",
                "type": "integer",
                "description": "interval length for all entries (difference in start time and end time of an entry range) the same for all entries start time of first interval is query_start_time_ms"
              }
            ]
          },
          {
            "name": "task_total_time_ms",
            "type": "integer",
            "description": "Sum of execution time for all of the query’s tasks, in milliseconds."
          },
          {
            "name": "total_time_ms",
            "type": "integer",
            "description": "Total execution time of the query from the client’s point of view, in milliseconds."
          },
          {
            "name": "work_to_be_done",
            "type": "integer",
            "description": "remaining work to be done across all stages in the query, calculated by autoscaler StatementAnalysis.scala, in milliseconds deprecated: using projected_remaining_task_total_time_ms instead"
          },
          {
            "name": "write_remote_bytes",
            "type": "integer",
            "description": "Size pf persistent data written to cloud object storage in your cloud tenant, in bytes."
          }
        ]
      },
      {
        "name": "plans_state",
        "type": "string",
        "description": "Whether plans exist for the execution, or the reason why they are missing"
      },
      {
        "name": "query_end_time_ms",
        "type": "integer",
        "description": "The time the query ended."
      },
      {
        "name": "query_id",
        "type": "string",
        "description": "The query ID."
      },
      {
        "name": "query_source",
        "type": "object",
        "description": "A struct that contains key-value pairs representing Databricks entities that were involved in the execution of this statement, such as jobs, notebooks, or dashboards. This field only records Databricks entities.",
        "children": [
          {
            "name": "alert_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "dashboard_id",
            "type": "string",
            "description": "The canonical identifier for this Lakeview dashboard"
          },
          {
            "name": "genie_space_id",
            "type": "string",
            "description": "The canonical identifier for this Genie space"
          },
          {
            "name": "job_info",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "job_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "job_run_id",
                "type": "string",
                "description": "The canonical identifier of the run. This ID is unique across all runs of all jobs."
              },
              {
                "name": "job_task_run_id",
                "type": "string",
                "description": "The canonical identifier of the task run."
              }
            ]
          },
          {
            "name": "legacy_dashboard_id",
            "type": "string",
            "description": "The canonical identifier for this legacy dashboard"
          },
          {
            "name": "notebook_id",
            "type": "string",
            "description": "The canonical identifier for this notebook"
          },
          {
            "name": "sql_query_id",
            "type": "string",
            "description": "The canonical identifier for this SQL query"
          }
        ]
      },
      {
        "name": "query_start_time_ms",
        "type": "integer",
        "description": "The time the query started."
      },
      {
        "name": "query_tags",
        "type": "array",
        "description": "A query execution can be optionally annotated with query tags",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "query_text",
        "type": "string",
        "description": "The text of the query."
      },
      {
        "name": "rows_produced",
        "type": "integer",
        "description": "The number of results returned by the query."
      },
      {
        "name": "session_id",
        "type": "string",
        "description": "The spark session UUID that query ran on. This is either the Spark Connect, DBSQL, or SDP session ID."
      },
      {
        "name": "spark_ui_url",
        "type": "string",
        "description": "URL to the Spark UI query plan."
      },
      {
        "name": "statement_type",
        "type": "string",
        "description": "Type of statement for this query"
      },
      {
        "name": "status",
        "type": "string",
        "description": "Query status with one the following values: - `QUEUED`: Query has been received and queued. - `RUNNING`: Query has started. - `CANCELED`: Query has been cancelled by the user. - `FAILED`: Query has failed. - `FINISHED`: Query has completed."
      },
      {
        "name": "user_id",
        "type": "integer",
        "description": "The ID of the user who ran the query."
      },
      {
        "name": "user_name",
        "type": "string",
        "description": "The email address or username of the user who ran the query."
      },
      {
        "name": "warehouse_id",
        "type": "string",
        "description": "Warehouse ID."
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
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-filter_by"><code>filter_by</code></a>, <a href="#parameter-include_metrics"><code>include_metrics</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List the history of queries through SQL warehouses, and serverless compute.<br /><br />You can filter by user ID, warehouse ID, status, and time range. Most recently started queries are<br />returned first (up to max_results in request). The pagination token returned in response can be used<br />to list subsequent query statuses.<br /><br />:param filter_by: :class:`QueryFilter` (optional)<br />  An optional filter object to limit query history results. Accepts parameters such as user IDs,<br />  endpoint IDs, and statuses to narrow the returned data. In a URL, the parameters of this filter are<br />  specified with dot notation. For example: `filter_by.statement_ids`.<br />:param include_metrics: bool (optional)<br />  Whether to include the query metrics with each query. Only use this for a small subset of queries<br />  (max_results). Defaults to false.<br />:param max_results: int (optional)<br />  Limit the number of results returned in one page. Must be less than 1000 and the default is 100.<br />:param page_token: str (optional)<br />  A token that can be used to get the next page of results. The token can contains characters that<br />  need to be encoded before using it in a URL. For example, the character '+' needs to be replaced by<br />  %2B. This field is optional.<br /><br />:returns: :class:`ListQueriesResponse`</td>
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
<tr id="parameter-filter_by">
    <td><CopyableCode code="filter_by" /></td>
    <td><code>string</code></td>
    <td>An optional filter object to limit query history results. Accepts parameters such as user IDs, endpoint IDs, and statuses to narrow the returned data. In a URL, the parameters of this filter are specified with dot notation. For example: `filter_by.statement_ids`.</td>
</tr>
<tr id="parameter-include_metrics">
    <td><CopyableCode code="include_metrics" /></td>
    <td><code>string</code></td>
    <td>Whether to include the query metrics with each query. Only use this for a small subset of queries (max_results). Defaults to false.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Limit the number of results returned in one page. Must be less than 1000 and the default is 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A token that can be used to get the next page of results. The token can contains characters that need to be encoded before using it in a URL. For example, the character '+' needs to be replaced by %2B. This field is optional.</td>
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

List the history of queries through SQL warehouses, and serverless compute.<br /><br />You can filter by user ID, warehouse ID, status, and time range. Most recently started queries are<br />returned first (up to max_results in request). The pagination token returned in response can be used<br />to list subsequent query statuses.<br /><br />:param filter_by: :class:`QueryFilter` (optional)<br />  An optional filter object to limit query history results. Accepts parameters such as user IDs,<br />  endpoint IDs, and statuses to narrow the returned data. In a URL, the parameters of this filter are<br />  specified with dot notation. For example: `filter_by.statement_ids`.<br />:param include_metrics: bool (optional)<br />  Whether to include the query metrics with each query. Only use this for a small subset of queries<br />  (max_results). Defaults to false.<br />:param max_results: int (optional)<br />  Limit the number of results returned in one page. Must be less than 1000 and the default is 100.<br />:param page_token: str (optional)<br />  A token that can be used to get the next page of results. The token can contains characters that<br />  need to be encoded before using it in a URL. For example, the character '+' needs to be replaced by<br />  %2B. This field is optional.<br /><br />:returns: :class:`ListQueriesResponse`

```sql
SELECT
has_next_page,
next_page_token,
res
FROM databricks_workspace.sql.query_history
WHERE deployment_name = '{{ deployment_name }}' -- required
AND filter_by = '{{ filter_by }}'
AND include_metrics = '{{ include_metrics }}'
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>

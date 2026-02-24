---
title: quality_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - quality_monitors
  - catalog
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

Creates, updates, deletes, gets or lists a <code>quality_monitors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="quality_monitors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.quality_monitors" /></td></tr>
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
    "name": "dashboard_id",
    "type": "string",
    "description": "[Create:ERR Update:OPT] Id of dashboard that visualizes the computed metrics. This can be empty if the monitor is in PENDING state."
  },
  {
    "name": "baseline_table_name",
    "type": "string",
    "description": "[Create:OPT Update:OPT] Baseline table name. Baseline data is used to compute drift from the data in the monitored `table_name`. The baseline table and the monitored table shall have the same schema."
  },
  {
    "name": "drift_metrics_table_name",
    "type": "string",
    "description": "[Create:ERR Update:IGN] Table that stores drift metrics data. Format: `catalog.schema.table_name`."
  },
  {
    "name": "output_schema_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "profile_metrics_table_name",
    "type": "string",
    "description": "[Create:ERR Update:IGN] Table that stores profile metrics data. Format: `catalog.schema.table_name`."
  },
  {
    "name": "table_name",
    "type": "string",
    "description": "[Create:ERR Update:IGN] UC table to monitor. Format: `catalog.schema.table_name`"
  },
  {
    "name": "assets_dir",
    "type": "string",
    "description": "[Create:REQ Update:IGN] Field for specifying the absolute path to a custom directory to store data-monitoring assets. Normally prepopulated to a default user location via UI and Python APIs."
  },
  {
    "name": "custom_metrics",
    "type": "array",
    "description": "[Create:OPT Update:OPT] Custom metrics.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Name of the metric in the output tables."
      },
      {
        "name": "definition",
        "type": "string",
        "description": "Jinja template for a SQL expression that specifies how to compute the metric. See [create metric definition]. [create metric definition]: https://docs.databricks.com/en/lakehouse-monitoring/custom-metrics.html#create-definition"
      },
      {
        "name": "input_columns",
        "type": "array",
        "description": "A list of column names in the input table the metric should be computed for. Can use ``\":table\"`` to indicate that the metric needs information from multiple columns."
      },
      {
        "name": "output_data_type",
        "type": "string",
        "description": "The output type of the custom metric."
      },
      {
        "name": "type",
        "type": "string",
        "description": "Can only be one of ``\"CUSTOM_METRIC_TYPE_AGGREGATE\"``, ``\"CUSTOM_METRIC_TYPE_DERIVED\"``, or ``\"CUSTOM_METRIC_TYPE_DRIFT\"``. The ``\"CUSTOM_METRIC_TYPE_AGGREGATE\"`` and ``\"CUSTOM_METRIC_TYPE_DERIVED\"`` metrics are computed on a single table, whereas the ``\"CUSTOM_METRIC_TYPE_DRIFT\"`` compare metrics across baseline and input table, or across the two consecutive time windows. - CUSTOM_METRIC_TYPE_AGGREGATE: only depend on the existing columns in your table - CUSTOM_METRIC_TYPE_DERIVED: depend on previously computed aggregate metrics - CUSTOM_METRIC_TYPE_DRIFT: depend on previously computed aggregate or derived metrics (CUSTOM_METRIC_TYPE_AGGREGATE, CUSTOM_METRIC_TYPE_DERIVED, CUSTOM_METRIC_TYPE_DRIFT)"
      }
    ]
  },
  {
    "name": "data_classification_config",
    "type": "object",
    "description": "[Create:OPT Update:OPT] Data classification related config.",
    "children": [
      {
        "name": "enabled",
        "type": "boolean",
        "description": "Whether to enable data classification."
      }
    ]
  },
  {
    "name": "inference_log",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "problem_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (PROBLEM_TYPE_CLASSIFICATION, PROBLEM_TYPE_REGRESSION)"
      },
      {
        "name": "timestamp_col",
        "type": "string",
        "description": "Column for the timestamp."
      },
      {
        "name": "granularities",
        "type": "array",
        "description": "List of granularities to use when aggregating data into time windows based on their timestamp."
      },
      {
        "name": "prediction_col",
        "type": "string",
        "description": "Column for the prediction."
      },
      {
        "name": "model_id_col",
        "type": "string",
        "description": "Column for the model identifier."
      },
      {
        "name": "label_col",
        "type": "string",
        "description": "Column for the label."
      },
      {
        "name": "prediction_proba_col",
        "type": "string",
        "description": "Column for prediction probabilities"
      }
    ]
  },
  {
    "name": "latest_monitor_failure_msg",
    "type": "string",
    "description": "[Create:ERR Update:IGN] The latest error message for a monitor failure."
  },
  {
    "name": "monitor_version",
    "type": "integer",
    "description": "[Create:ERR Update:IGN] Represents the current monitor configuration version in use. The version will be represented in a numeric fashion (1,2,3...). The field has flexibility to take on negative values, which can indicate corrupted monitor_version numbers."
  },
  {
    "name": "notifications",
    "type": "object",
    "description": "[Create:OPT Update:OPT] Field for specifying notification settings.",
    "children": [
      {
        "name": "on_failure",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "email_addresses",
            "type": "array",
            "description": ""
          }
        ]
      },
      {
        "name": "on_new_classification_tag_detected",
        "type": "object",
        "description": "Destinations to send notifications on new classification tag detected.",
        "children": [
          {
            "name": "email_addresses",
            "type": "array",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "schedule",
    "type": "object",
    "description": "[Create:OPT Update:OPT] The monitor schedule.",
    "children": [
      {
        "name": "quartz_cron_expression",
        "type": "string",
        "description": ""
      },
      {
        "name": "timezone_id",
        "type": "string",
        "description": "The timezone id (e.g., ``PST``) in which to evaluate the quartz expression."
      },
      {
        "name": "pause_status",
        "type": "string",
        "description": "Read only field that indicates whether a schedule is paused or not. (PAUSED, UNPAUSED, UNSPECIFIED)"
      }
    ]
  },
  {
    "name": "slicing_exprs",
    "type": "array",
    "description": "[Create:OPT Update:OPT] List of column expressions to slice data with for targeted analysis. The data is grouped by each expression independently, resulting in a separate slice for each predicate and its complements. For example `slicing_exprs=[“col_1”, “col_2 > 10”]` will generate the following slices: two slices for `col_2 > 10` (True and False), and one slice per unique value in `col1`. For high-cardinality columns, only the top 100 unique values by frequency will generate slices."
  },
  {
    "name": "snapshot",
    "type": "object",
    "description": "Configuration for monitoring snapshot tables."
  },
  {
    "name": "status",
    "type": "string",
    "description": "[Create:ERR Update:IGN] The monitor status. (MONITOR_STATUS_ACTIVE, MONITOR_STATUS_DELETE_PENDING, MONITOR_STATUS_ERROR, MONITOR_STATUS_FAILED, MONITOR_STATUS_PENDING)"
  },
  {
    "name": "time_series",
    "type": "object",
    "description": "Configuration for monitoring time series tables.",
    "children": [
      {
        "name": "timestamp_col",
        "type": "string",
        "description": "Column for the timestamp."
      },
      {
        "name": "granularities",
        "type": "array",
        "description": "Granularities for aggregating data into time windows based on their timestamp. Currently the following static granularities are supported: &#123;``\\\"5 minutes\\\"``, ``\\\"30 minutes\\\"``, ``\\\"1 hour\\\"``, ``\\\"1 day\\\"``, ``\\\"\\u003cn\\u003e week(s)\\\"``, ``\\\"1 month\\\"``, ``\\\"1 year\\\"``&#125;."
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
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>[DEPRECATED] Gets a monitor for the specified table. Use Data Quality Monitors API instead</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-output_schema_name"><code>output_schema_name</code></a>, <a href="#parameter-assets_dir"><code>assets_dir</code></a></td>
    <td></td>
    <td>[DEPRECATED] Creates a new monitor for the specified table. Use Data Quality Monitors API instead</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-output_schema_name"><code>output_schema_name</code></a></td>
    <td></td>
    <td>[DEPRECATED] Updates a monitor for the specified table. Use Data Quality Monitors API instead</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>[DEPRECATED] Deletes a monitor for the specified table. Use Data Quality Monitors API instead</td>
</tr>
<tr>
    <td><a href="#cancel_refresh"><CopyableCode code="cancel_refresh" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-refresh_id"><code>refresh_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>[DEPRECATED] Cancels an already-initiated refresh job. Use Data Quality Monitors API instead</td>
</tr>
<tr>
    <td><a href="#regenerate_dashboard"><CopyableCode code="regenerate_dashboard" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>[DEPRECATED] Regenerates the monitoring dashboard for the specified table. Use Data Quality Monitors</td>
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
<tr id="parameter-refresh_id">
    <td><CopyableCode code="refresh_id" /></td>
    <td><code>integer</code></td>
    <td>int</td>
</tr>
<tr id="parameter-table_name">
    <td><CopyableCode code="table_name" /></td>
    <td><code>string</code></td>
    <td>UC table name in format `catalog.schema.table_name`. This field corresponds to the &#123;full_table_name_arg&#125; arg in the endpoint path.</td>
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

[DEPRECATED] Gets a monitor for the specified table. Use Data Quality Monitors API instead

```sql
SELECT
dashboard_id,
baseline_table_name,
drift_metrics_table_name,
output_schema_name,
profile_metrics_table_name,
table_name,
assets_dir,
custom_metrics,
data_classification_config,
inference_log,
latest_monitor_failure_msg,
monitor_version,
notifications,
schedule,
slicing_exprs,
snapshot,
status,
time_series
FROM databricks_workspace.catalog.quality_monitors
WHERE table_name = '{{ table_name }}' -- required
AND workspace = '{{ workspace }}' -- required
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

[DEPRECATED] Creates a new monitor for the specified table. Use Data Quality Monitors API instead

```sql
INSERT INTO databricks_workspace.catalog.quality_monitors (
output_schema_name,
assets_dir,
baseline_table_name,
custom_metrics,
data_classification_config,
inference_log,
latest_monitor_failure_msg,
notifications,
schedule,
skip_builtin_dashboard,
slicing_exprs,
snapshot,
time_series,
warehouse_id,
table_name,
workspace
)
SELECT 
'{{ output_schema_name }}' /* required */,
'{{ assets_dir }}' /* required */,
'{{ baseline_table_name }}',
'{{ custom_metrics }}',
'{{ data_classification_config }}',
'{{ inference_log }}',
'{{ latest_monitor_failure_msg }}',
'{{ notifications }}',
'{{ schedule }}',
{{ skip_builtin_dashboard }},
'{{ slicing_exprs }}',
'{{ snapshot }}',
'{{ time_series }}',
'{{ warehouse_id }}',
'{{ table_name }}',
'{{ workspace }}'
RETURNING
dashboard_id,
baseline_table_name,
drift_metrics_table_name,
output_schema_name,
profile_metrics_table_name,
table_name,
assets_dir,
custom_metrics,
data_classification_config,
inference_log,
latest_monitor_failure_msg,
monitor_version,
notifications,
schedule,
slicing_exprs,
snapshot,
status,
time_series
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: quality_monitors
  props:
    - name: table_name
      value: string
      description: Required parameter for the quality_monitors resource.
    - name: workspace
      value: string
      description: Required parameter for the quality_monitors resource.
    - name: output_schema_name
      value: string
      description: |
        [Create:REQ Update:REQ] Schema where output tables are created. Needs to be in 2-level format {catalog}.{schema}
    - name: assets_dir
      value: string
      description: |
        [Create:REQ Update:IGN] Field for specifying the absolute path to a custom directory to store data-monitoring assets. Normally prepopulated to a default user location via UI and Python APIs.
    - name: baseline_table_name
      value: string
      description: |
        [Create:OPT Update:OPT] Baseline table name. Baseline data is used to compute drift from the data in the monitored `table_name`. The baseline table and the monitored table shall have the same schema.
    - name: custom_metrics
      value: array
      description: |
        [Create:OPT Update:OPT] Custom metrics.
      props:
      - name: name
        value: string
        description: |
          Name of the metric in the output tables.
      - name: definition
        value: string
        description: |
          Jinja template for a SQL expression that specifies how to compute the metric. See [create metric definition]. [create metric definition]: https://docs.databricks.com/en/lakehouse-monitoring/custom-metrics.html#create-definition
      - name: input_columns
        value: array
        description: |
          A list of column names in the input table the metric should be computed for. Can use ``":table"`` to indicate that the metric needs information from multiple columns.
        items:
          type: string
      - name: output_data_type
        value: string
        description: |
          The output type of the custom metric.
      - name: type
        value: string
        description: |
          Can only be one of ``"CUSTOM_METRIC_TYPE_AGGREGATE"``, ``"CUSTOM_METRIC_TYPE_DERIVED"``, or ``"CUSTOM_METRIC_TYPE_DRIFT"``. The ``"CUSTOM_METRIC_TYPE_AGGREGATE"`` and ``"CUSTOM_METRIC_TYPE_DERIVED"`` metrics are computed on a single table, whereas the ``"CUSTOM_METRIC_TYPE_DRIFT"`` compare metrics across baseline and input table, or across the two consecutive time windows. - CUSTOM_METRIC_TYPE_AGGREGATE: only depend on the existing columns in your table - CUSTOM_METRIC_TYPE_DERIVED: depend on previously computed aggregate metrics - CUSTOM_METRIC_TYPE_DRIFT: depend on previously computed aggregate or derived metrics
    - name: data_classification_config
      value: object
      description: |
        [Create:OPT Update:OPT] Data classification related config.
      props:
      - name: enabled
        value: boolean
        description: |
          Whether to enable data classification.
    - name: inference_log
      value: object
      description: |
        :param latest_monitor_failure_msg: str (optional) [Create:ERR Update:IGN] The latest error message for a monitor failure.
      props:
      - name: problem_type
        value: string
        description: |
          Create a collection of name/value pairs.
          Example enumeration:
          >>> class Color(Enum):
          ...     RED = 1
          ...     BLUE = 2
          ...     GREEN = 3
          Access them by:
          - attribute access::
          >>> Color.RED
          <Color.RED: 1>
          - value lookup:
          >>> Color(1)
          <Color.RED: 1>
          - name lookup:
          >>> Color['RED']
          <Color.RED: 1>
          Enumerations can be iterated over, and know how many members they have:
          >>> len(Color)
          3
          >>> list(Color)
          [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
          Methods can be added to enumerations, and members can have their own
          attributes -- see the documentation for details.
      - name: timestamp_col
        value: string
        description: |
          Column for the timestamp.
      - name: granularities
        value: array
        description: |
          List of granularities to use when aggregating data into time windows based on their timestamp.
        items:
          type: string
      - name: prediction_col
        value: string
        description: |
          Column for the prediction.
      - name: model_id_col
        value: string
        description: |
          Column for the model identifier.
      - name: label_col
        value: string
        description: |
          Column for the label.
      - name: prediction_proba_col
        value: string
        description: |
          Column for prediction probabilities
    - name: latest_monitor_failure_msg
      value: string
    - name: notifications
      value: object
      description: |
        [Create:OPT Update:OPT] Field for specifying notification settings.
      props:
      - name: on_failure
        value: object
        props:
        - name: email_addresses
          value: array
          items:
            type: string
      - name: on_new_classification_tag_detected
        value: object
        description: |
          Destinations to send notifications on new classification tag detected.
        props:
        - name: email_addresses
          value: array
          items:
            type: string
    - name: schedule
      value: object
      description: |
        [Create:OPT Update:OPT] The monitor schedule.
      props:
      - name: quartz_cron_expression
        value: string
      - name: timezone_id
        value: string
        description: |
          The timezone id (e.g., ``PST``) in which to evaluate the quartz expression.
      - name: pause_status
        value: string
        description: |
          Read only field that indicates whether a schedule is paused or not.
    - name: skip_builtin_dashboard
      value: boolean
      description: |
        Whether to skip creating a default dashboard summarizing data quality metrics.
    - name: slicing_exprs
      value: array
      description: |
        [Create:OPT Update:OPT] List of column expressions to slice data with for targeted analysis. The data is grouped by each expression independently, resulting in a separate slice for each predicate and its complements. For example `slicing_exprs=[“col_1”, “col_2 > 10”]` will generate the following slices: two slices for `col_2 > 10` (True and False), and one slice per unique value in `col1`. For high-cardinality columns, only the top 100 unique values by frequency will generate slices.
      items:
        type: string
    - name: snapshot
      value: object
      description: |
        Configuration for monitoring snapshot tables.
    - name: time_series
      value: object
      description: |
        Configuration for monitoring time series tables.
      props:
      - name: timestamp_col
        value: string
        description: |
          Column for the timestamp.
      - name: granularities
        value: array
        description: |
          Granularities for aggregating data into time windows based on their timestamp. Currently the following static granularities are supported: {``\"5 minutes\"``, ``\"30 minutes\"``, ``\"1 hour\"``, ``\"1 day\"``, ``\"\u003cn\u003e week(s)\"``, ``\"1 month\"``, ``\"1 year\"``}.
        items:
          type: string
    - name: warehouse_id
      value: string
      description: |
        Optional argument to specify the warehouse for dashboard creation. If not specified, the first running warehouse will be used.
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

[DEPRECATED] Updates a monitor for the specified table. Use Data Quality Monitors API instead

```sql
REPLACE databricks_workspace.catalog.quality_monitors
SET 
output_schema_name = '{{ output_schema_name }}',
baseline_table_name = '{{ baseline_table_name }}',
custom_metrics = '{{ custom_metrics }}',
dashboard_id = '{{ dashboard_id }}',
data_classification_config = '{{ data_classification_config }}',
inference_log = '{{ inference_log }}',
latest_monitor_failure_msg = '{{ latest_monitor_failure_msg }}',
notifications = '{{ notifications }}',
schedule = '{{ schedule }}',
slicing_exprs = '{{ slicing_exprs }}',
snapshot = '{{ snapshot }}',
time_series = '{{ time_series }}'
WHERE 
table_name = '{{ table_name }}' --required
AND workspace = '{{ workspace }}' --required
AND output_schema_name = '{{ output_schema_name }}' --required
RETURNING
dashboard_id,
baseline_table_name,
drift_metrics_table_name,
output_schema_name,
profile_metrics_table_name,
table_name,
assets_dir,
custom_metrics,
data_classification_config,
inference_log,
latest_monitor_failure_msg,
monitor_version,
notifications,
schedule,
slicing_exprs,
snapshot,
status,
time_series;
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

[DEPRECATED] Deletes a monitor for the specified table. Use Data Quality Monitors API instead

```sql
DELETE FROM databricks_workspace.catalog.quality_monitors
WHERE table_name = '{{ table_name }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel_refresh"
    values={[
        { label: 'cancel_refresh', value: 'cancel_refresh' },
        { label: 'regenerate_dashboard', value: 'regenerate_dashboard' }
    ]}
>
<TabItem value="cancel_refresh">

[DEPRECATED] Cancels an already-initiated refresh job. Use Data Quality Monitors API instead

```sql
EXEC databricks_workspace.catalog.quality_monitors.cancel_refresh 
@table_name='{{ table_name }}' --required, 
@refresh_id='{{ refresh_id }}' --required, 
@workspace='{{ workspace }}' --required
;
```
</TabItem>
<TabItem value="regenerate_dashboard">

[DEPRECATED] Regenerates the monitoring dashboard for the specified table. Use Data Quality Monitors

```sql
EXEC databricks_workspace.catalog.quality_monitors.regenerate_dashboard 
@table_name='{{ table_name }}' --required, 
@workspace='{{ workspace }}' --required 
@@json=
'{
"warehouse_id": "{{ warehouse_id }}"
}'
;
```
</TabItem>
</Tabs>

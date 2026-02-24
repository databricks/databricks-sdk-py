---
title: feature_engineering
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_engineering
  - ml
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

Creates, updates, deletes, gets or lists a <code>feature_engineering</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="feature_engineering" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.feature_engineering" /></td></tr>
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
    "name": "full_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "description",
    "type": "string",
    "description": "The description of the feature."
  },
  {
    "name": "filter_condition",
    "type": "string",
    "description": "The filter condition applied to the source data before aggregation."
  },
  {
    "name": "function",
    "type": "object",
    "description": "The function by which the feature is computed.",
    "children": [
      {
        "name": "function_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (APPROX_COUNT_DISTINCT, APPROX_PERCENTILE, AVG, COUNT, FIRST, LAST, MAX, MIN, STDDEV_POP, STDDEV_SAMP, SUM, VAR_POP, VAR_SAMP)"
      },
      {
        "name": "extra_parameters",
        "type": "array",
        "description": "Extra parameters for parameterized functions.",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value of the parameter."
          }
        ]
      }
    ]
  },
  {
    "name": "inputs",
    "type": "array",
    "description": "The input columns from which the feature is computed."
  },
  {
    "name": "lineage_context",
    "type": "object",
    "description": "WARNING: This field is primarily intended for internal use by Databricks systems and is automatically populated when features are created through Databricks notebooks or jobs. Users should not manually set this field as incorrect values may lead to inaccurate lineage tracking or unexpected behavior. This field will be set by feature-engineering client and should be left unset by SDK and terraform users.",
    "children": [
      {
        "name": "job_context",
        "type": "object",
        "description": "Job context information including job ID and run ID.",
        "children": [
          {
            "name": "job_id",
            "type": "integer",
            "description": ""
          },
          {
            "name": "job_run_id",
            "type": "integer",
            "description": "The job run ID where this API was invoked."
          }
        ]
      },
      {
        "name": "notebook_id",
        "type": "integer",
        "description": "The notebook ID where this API was invoked."
      }
    ]
  },
  {
    "name": "source",
    "type": "object",
    "description": "The data source of the feature.",
    "children": [
      {
        "name": "delta_table_source",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "full_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "entity_columns",
            "type": "array",
            "description": "The entity columns of the Delta table."
          },
          {
            "name": "timeseries_column",
            "type": "string",
            "description": "The timeseries column of the Delta table."
          }
        ]
      },
      {
        "name": "kafka_source",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "entity_column_identifiers",
            "type": "array",
            "description": "The entity column identifiers of the Kafka source.",
            "children": [
              {
                "name": "variant_expr_path",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "timeseries_column_identifier",
            "type": "object",
            "description": "The timeseries column identifier of the Kafka source.",
            "children": [
              {
                "name": "variant_expr_path",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "time_window",
    "type": "object",
    "description": "The time window in which the feature is computed.",
    "children": [
      {
        "name": "continuous",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "window_duration",
            "type": "string",
            "description": ""
          },
          {
            "name": "offset",
            "type": "string",
            "description": "The offset of the continuous window (must be non-positive)."
          }
        ]
      },
      {
        "name": "sliding",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "window_duration",
            "type": "string",
            "description": ""
          },
          {
            "name": "slide_duration",
            "type": "string",
            "description": "The slide duration (interval by which windows advance, must be positive and less than duration)."
          }
        ]
      },
      {
        "name": "tumbling",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "window_duration",
            "type": "string",
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
    "name": "full_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "description",
    "type": "string",
    "description": "The description of the feature."
  },
  {
    "name": "filter_condition",
    "type": "string",
    "description": "The filter condition applied to the source data before aggregation."
  },
  {
    "name": "function",
    "type": "object",
    "description": "The function by which the feature is computed.",
    "children": [
      {
        "name": "function_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (APPROX_COUNT_DISTINCT, APPROX_PERCENTILE, AVG, COUNT, FIRST, LAST, MAX, MIN, STDDEV_POP, STDDEV_SAMP, SUM, VAR_POP, VAR_SAMP)"
      },
      {
        "name": "extra_parameters",
        "type": "array",
        "description": "Extra parameters for parameterized functions.",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value of the parameter."
          }
        ]
      }
    ]
  },
  {
    "name": "inputs",
    "type": "array",
    "description": "The input columns from which the feature is computed."
  },
  {
    "name": "lineage_context",
    "type": "object",
    "description": "WARNING: This field is primarily intended for internal use by Databricks systems and is automatically populated when features are created through Databricks notebooks or jobs. Users should not manually set this field as incorrect values may lead to inaccurate lineage tracking or unexpected behavior. This field will be set by feature-engineering client and should be left unset by SDK and terraform users.",
    "children": [
      {
        "name": "job_context",
        "type": "object",
        "description": "Job context information including job ID and run ID.",
        "children": [
          {
            "name": "job_id",
            "type": "integer",
            "description": ""
          },
          {
            "name": "job_run_id",
            "type": "integer",
            "description": "The job run ID where this API was invoked."
          }
        ]
      },
      {
        "name": "notebook_id",
        "type": "integer",
        "description": "The notebook ID where this API was invoked."
      }
    ]
  },
  {
    "name": "source",
    "type": "object",
    "description": "The data source of the feature.",
    "children": [
      {
        "name": "delta_table_source",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "full_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "entity_columns",
            "type": "array",
            "description": "The entity columns of the Delta table."
          },
          {
            "name": "timeseries_column",
            "type": "string",
            "description": "The timeseries column of the Delta table."
          }
        ]
      },
      {
        "name": "kafka_source",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "entity_column_identifiers",
            "type": "array",
            "description": "The entity column identifiers of the Kafka source.",
            "children": [
              {
                "name": "variant_expr_path",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "timeseries_column_identifier",
            "type": "object",
            "description": "The timeseries column identifier of the Kafka source.",
            "children": [
              {
                "name": "variant_expr_path",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "time_window",
    "type": "object",
    "description": "The time window in which the feature is computed.",
    "children": [
      {
        "name": "continuous",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "window_duration",
            "type": "string",
            "description": ""
          },
          {
            "name": "offset",
            "type": "string",
            "description": "The offset of the continuous window (must be non-positive)."
          }
        ]
      },
      {
        "name": "sliding",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "window_duration",
            "type": "string",
            "description": ""
          },
          {
            "name": "slide_duration",
            "type": "string",
            "description": "The slide duration (interval by which windows advance, must be positive and less than duration)."
          }
        ]
      },
      {
        "name": "tumbling",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "window_duration",
            "type": "string",
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
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Get a Feature.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List Features.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-feature"><code>feature</code></a></td>
    <td></td>
    <td>Create a Feature.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-feature"><code>feature</code></a></td>
    <td></td>
    <td>Update a Feature.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Delete a Feature.</td>
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
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>Name of the feature to delete.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>The list of fields to update.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of results to return.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page based on a previous query.</td>
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

Get a Feature.

```sql
SELECT
full_name,
description,
filter_condition,
function,
inputs,
lineage_context,
source,
time_window
FROM databricks_workspace.ml.feature_engineering
WHERE full_name = '{{ full_name }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Features.

```sql
SELECT
full_name,
description,
filter_condition,
function,
inputs,
lineage_context,
source,
time_window
FROM databricks_workspace.ml.feature_engineering
WHERE workspace = '{{ workspace }}' -- required
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

Create a Feature.

```sql
INSERT INTO databricks_workspace.ml.feature_engineering (
feature,
workspace
)
SELECT 
'{{ feature }}' /* required */,
'{{ workspace }}'
RETURNING
full_name,
description,
filter_condition,
function,
inputs,
lineage_context,
source,
time_window
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: feature_engineering
  props:
    - name: workspace
      value: string
      description: Required parameter for the feature_engineering resource.
    - name: feature
      value: object
      description: |
        Feature to create.
      props:
      - name: full_name
        value: string
      - name: source
        value: object
        description: |
          The data source of the feature.
        props:
        - name: delta_table_source
          value: object
          props:
          - name: full_name
            value: string
          - name: entity_columns
            value: array
            description: |
              The entity columns of the Delta table.
            items:
              type: string
          - name: timeseries_column
            value: string
            description: |
              The timeseries column of the Delta table.
        - name: kafka_source
          value: object
          props:
          - name: name
            value: string
          - name: entity_column_identifiers
            value: array
            description: |
              The entity column identifiers of the Kafka source.
            props:
            - name: variant_expr_path
              value: string
          - name: timeseries_column_identifier
            value: object
            description: |
              The timeseries column identifier of the Kafka source.
            props:
            - name: variant_expr_path
              value: string
      - name: inputs
        value: array
        description: |
          The input columns from which the feature is computed.
        items:
          type: string
      - name: function
        value: object
        description: |
          The function by which the feature is computed.
        props:
        - name: function_type
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
        - name: extra_parameters
          value: array
          description: |
            Extra parameters for parameterized functions.
          props:
          - name: key
            value: string
          - name: value
            value: string
            description: |
              The value of the parameter.
      - name: description
        value: string
        description: |
          The description of the feature.
      - name: filter_condition
        value: string
        description: |
          The filter condition applied to the source data before aggregation.
      - name: lineage_context
        value: object
        description: |
          WARNING: This field is primarily intended for internal use by Databricks systems and is automatically populated when features are created through Databricks notebooks or jobs. Users should not manually set this field as incorrect values may lead to inaccurate lineage tracking or unexpected behavior. This field will be set by feature-engineering client and should be left unset by SDK and terraform users.
        props:
        - name: job_context
          value: object
          description: |
            Job context information including job ID and run ID.
          props:
          - name: job_id
            value: integer
          - name: job_run_id
            value: integer
            description: |
              The job run ID where this API was invoked.
        - name: notebook_id
          value: integer
          description: |
            The notebook ID where this API was invoked.
      - name: time_window
        value: object
        description: |
          The time window in which the feature is computed.
        props:
        - name: continuous
          value: object
          props:
          - name: window_duration
            value: string
          - name: offset
            value: string
            description: |
              The offset of the continuous window (must be non-positive).
        - name: sliding
          value: object
          props:
          - name: window_duration
            value: string
          - name: slide_duration
            value: string
            description: |
              The slide duration (interval by which windows advance, must be positive and less than duration).
        - name: tumbling
          value: object
          props:
          - name: window_duration
            value: string
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

Update a Feature.

```sql
UPDATE databricks_workspace.ml.feature_engineering
SET 
feature = '{{ feature }}'
WHERE 
full_name = '{{ full_name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND workspace = '{{ workspace }}' --required
AND feature = '{{ feature }}' --required
RETURNING
full_name,
description,
filter_condition,
function,
inputs,
lineage_context,
source,
time_window;
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

Delete a Feature.

```sql
DELETE FROM databricks_workspace.ml.feature_engineering
WHERE full_name = '{{ full_name }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

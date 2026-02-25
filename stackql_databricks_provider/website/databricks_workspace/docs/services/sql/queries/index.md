---
title: queries
hide_title: false
hide_table_of_contents: false
keywords:
  - queries
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>queries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="queries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.queries" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": "UUID identifying the query."
  },
  {
    "name": "warehouse_id",
    "type": "string",
    "description": "ID of the SQL warehouse attached to the query."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name of the query that appears in list views, widget headings, and on the query page."
  },
  {
    "name": "last_modifier_user_name",
    "type": "string",
    "description": "Username of the user who last saved changes to this query."
  },
  {
    "name": "owner_user_name",
    "type": "string",
    "description": "Username of the user that owns the query."
  },
  {
    "name": "apply_auto_limit",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "catalog",
    "type": "string",
    "description": "Name of the catalog where this query will be executed."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "Timestamp when this query was created."
  },
  {
    "name": "description",
    "type": "string",
    "description": "General description that conveys additional information about this query such as usage notes."
  },
  {
    "name": "lifecycle_state",
    "type": "string",
    "description": "Indicates whether the query is trashed. (ACTIVE, TRASHED)"
  },
  {
    "name": "parameters",
    "type": "array",
    "description": "List of query parameter definitions.",
    "children": [
      {
        "name": "date_range_value",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "date_range_value",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "start",
                "type": "string",
                "description": ""
              },
              {
                "name": "end",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "dynamic_date_range_value",
            "type": "string",
            "description": "Dynamic date-time range value based on current date-time. (LAST_12_MONTHS, LAST_14_DAYS, LAST_24_HOURS, LAST_30_DAYS, LAST_60_DAYS, LAST_7_DAYS, LAST_8_HOURS, LAST_90_DAYS, LAST_HOUR, LAST_MONTH, LAST_WEEK, LAST_YEAR, THIS_MONTH, THIS_WEEK, THIS_YEAR, TODAY, YESTERDAY)"
          },
          {
            "name": "precision",
            "type": "string",
            "description": "Date-time precision to format the value into when the query is run. Defaults to DAY_PRECISION (YYYY-MM-DD). (DAY_PRECISION, MINUTE_PRECISION, SECOND_PRECISION)"
          },
          {
            "name": "start_day_of_week",
            "type": "integer",
            "description": ""
          }
        ]
      },
      {
        "name": "date_value",
        "type": "object",
        "description": "Date query parameter value. Can only specify one of `dynamic_date_value` or `date_value`.",
        "children": [
          {
            "name": "date_value",
            "type": "string",
            "description": ""
          },
          {
            "name": "dynamic_date_value",
            "type": "string",
            "description": "Dynamic date-time value based on current date-time. (NOW, YESTERDAY)"
          },
          {
            "name": "precision",
            "type": "string",
            "description": "Date-time precision to format the value into when the query is run. Defaults to DAY_PRECISION (YYYY-MM-DD). (DAY_PRECISION, MINUTE_PRECISION, SECOND_PRECISION)"
          }
        ]
      },
      {
        "name": "enum_value",
        "type": "object",
        "description": "Dropdown query parameter value.",
        "children": [
          {
            "name": "enum_options",
            "type": "string",
            "description": ""
          },
          {
            "name": "multi_values_options",
            "type": "object",
            "description": "If specified, allows multiple values to be selected for this parameter.",
            "children": [
              {
                "name": "prefix",
                "type": "string",
                "description": ""
              },
              {
                "name": "separator",
                "type": "string",
                "description": "Character that separates each selected parameter value. Defaults to a comma."
              },
              {
                "name": "suffix",
                "type": "string",
                "description": "Character that suffixes each selected parameter value."
              }
            ]
          },
          {
            "name": "values",
            "type": "array",
            "description": "List of selected query parameter values."
          }
        ]
      },
      {
        "name": "name",
        "type": "string",
        "description": "Literal parameter marker that appears between double curly braces in the query text."
      },
      {
        "name": "numeric_value",
        "type": "object",
        "description": "Numeric query parameter value.",
        "children": [
          {
            "name": "value",
            "type": "number",
            "description": ""
          }
        ]
      },
      {
        "name": "query_backed_value",
        "type": "object",
        "description": "Query-based dropdown query parameter value.",
        "children": [
          {
            "name": "multi_values_options",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "prefix",
                "type": "string",
                "description": ""
              },
              {
                "name": "separator",
                "type": "string",
                "description": "Character that separates each selected parameter value. Defaults to a comma."
              },
              {
                "name": "suffix",
                "type": "string",
                "description": "Character that suffixes each selected parameter value."
              }
            ]
          },
          {
            "name": "query_id",
            "type": "string",
            "description": "UUID of the query that provides the parameter values."
          },
          {
            "name": "values",
            "type": "array",
            "description": "List of selected query parameter values."
          }
        ]
      },
      {
        "name": "text_value",
        "type": "object",
        "description": "Text query parameter value.",
        "children": [
          {
            "name": "value",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "title",
        "type": "string",
        "description": "Text displayed in the user-facing parameter widget in the UI."
      }
    ]
  },
  {
    "name": "parent_path",
    "type": "string",
    "description": "Workspace path of the workspace folder containing the object."
  },
  {
    "name": "query_text",
    "type": "string",
    "description": "Text of the query to be run."
  },
  {
    "name": "run_as_mode",
    "type": "string",
    "description": "Sets the \"Run as\" role for the object. (OWNER, VIEWER)"
  },
  {
    "name": "schema",
    "type": "string",
    "description": "Name of the schema where this query will be executed."
  },
  {
    "name": "tags",
    "type": "array",
    "description": ""
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "Timestamp when this query was last updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "UUID identifying the query."
  },
  {
    "name": "warehouse_id",
    "type": "string",
    "description": "ID of the SQL warehouse attached to the query."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name of the query that appears in list views, widget headings, and on the query page."
  },
  {
    "name": "last_modifier_user_name",
    "type": "string",
    "description": "Username of the user who last saved changes to this query."
  },
  {
    "name": "owner_user_name",
    "type": "string",
    "description": "Username of the user that owns the query."
  },
  {
    "name": "apply_auto_limit",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "catalog",
    "type": "string",
    "description": "Name of the catalog where this query will be executed."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "Timestamp when this query was created."
  },
  {
    "name": "description",
    "type": "string",
    "description": "General description that conveys additional information about this query such as usage notes."
  },
  {
    "name": "lifecycle_state",
    "type": "string",
    "description": "Indicates whether the query is trashed. (ACTIVE, TRASHED)"
  },
  {
    "name": "parameters",
    "type": "array",
    "description": "List of query parameter definitions.",
    "children": [
      {
        "name": "date_range_value",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "date_range_value",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "start",
                "type": "string",
                "description": ""
              },
              {
                "name": "end",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "dynamic_date_range_value",
            "type": "string",
            "description": "Dynamic date-time range value based on current date-time. (LAST_12_MONTHS, LAST_14_DAYS, LAST_24_HOURS, LAST_30_DAYS, LAST_60_DAYS, LAST_7_DAYS, LAST_8_HOURS, LAST_90_DAYS, LAST_HOUR, LAST_MONTH, LAST_WEEK, LAST_YEAR, THIS_MONTH, THIS_WEEK, THIS_YEAR, TODAY, YESTERDAY)"
          },
          {
            "name": "precision",
            "type": "string",
            "description": "Date-time precision to format the value into when the query is run. Defaults to DAY_PRECISION (YYYY-MM-DD). (DAY_PRECISION, MINUTE_PRECISION, SECOND_PRECISION)"
          },
          {
            "name": "start_day_of_week",
            "type": "integer",
            "description": ""
          }
        ]
      },
      {
        "name": "date_value",
        "type": "object",
        "description": "Date query parameter value. Can only specify one of `dynamic_date_value` or `date_value`.",
        "children": [
          {
            "name": "date_value",
            "type": "string",
            "description": ""
          },
          {
            "name": "dynamic_date_value",
            "type": "string",
            "description": "Dynamic date-time value based on current date-time. (NOW, YESTERDAY)"
          },
          {
            "name": "precision",
            "type": "string",
            "description": "Date-time precision to format the value into when the query is run. Defaults to DAY_PRECISION (YYYY-MM-DD). (DAY_PRECISION, MINUTE_PRECISION, SECOND_PRECISION)"
          }
        ]
      },
      {
        "name": "enum_value",
        "type": "object",
        "description": "Dropdown query parameter value.",
        "children": [
          {
            "name": "enum_options",
            "type": "string",
            "description": ""
          },
          {
            "name": "multi_values_options",
            "type": "object",
            "description": "If specified, allows multiple values to be selected for this parameter.",
            "children": [
              {
                "name": "prefix",
                "type": "string",
                "description": ""
              },
              {
                "name": "separator",
                "type": "string",
                "description": "Character that separates each selected parameter value. Defaults to a comma."
              },
              {
                "name": "suffix",
                "type": "string",
                "description": "Character that suffixes each selected parameter value."
              }
            ]
          },
          {
            "name": "values",
            "type": "array",
            "description": "List of selected query parameter values."
          }
        ]
      },
      {
        "name": "name",
        "type": "string",
        "description": "Literal parameter marker that appears between double curly braces in the query text."
      },
      {
        "name": "numeric_value",
        "type": "object",
        "description": "Numeric query parameter value.",
        "children": [
          {
            "name": "value",
            "type": "number",
            "description": ""
          }
        ]
      },
      {
        "name": "query_backed_value",
        "type": "object",
        "description": "Query-based dropdown query parameter value.",
        "children": [
          {
            "name": "multi_values_options",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "prefix",
                "type": "string",
                "description": ""
              },
              {
                "name": "separator",
                "type": "string",
                "description": "Character that separates each selected parameter value. Defaults to a comma."
              },
              {
                "name": "suffix",
                "type": "string",
                "description": "Character that suffixes each selected parameter value."
              }
            ]
          },
          {
            "name": "query_id",
            "type": "string",
            "description": "UUID of the query that provides the parameter values."
          },
          {
            "name": "values",
            "type": "array",
            "description": "List of selected query parameter values."
          }
        ]
      },
      {
        "name": "text_value",
        "type": "object",
        "description": "Text query parameter value.",
        "children": [
          {
            "name": "value",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "title",
        "type": "string",
        "description": "Text displayed in the user-facing parameter widget in the UI."
      }
    ]
  },
  {
    "name": "query_text",
    "type": "string",
    "description": "Text of the query to be run."
  },
  {
    "name": "run_as_mode",
    "type": "string",
    "description": "Sets the \"Run as\" role for the object. (OWNER, VIEWER)"
  },
  {
    "name": "schema",
    "type": "string",
    "description": "Name of the schema where this query will be executed."
  },
  {
    "name": "tags",
    "type": "array",
    "description": ""
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "Timestamp when this query was last updated."
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets a query.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets a list of queries accessible to the user, ordered by creation time. **Warning:** Calling this API</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Creates a query.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a></td>
    <td></td>
    <td>Updates a query.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Moves a query to the trash. Trashed queries immediately disappear from searches and list views, and</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>str</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
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

Gets a query.

```sql
SELECT
id,
warehouse_id,
display_name,
last_modifier_user_name,
owner_user_name,
apply_auto_limit,
catalog,
create_time,
description,
lifecycle_state,
parameters,
parent_path,
query_text,
run_as_mode,
schema,
tags,
update_time
FROM databricks_workspace.sql.queries
WHERE id = '{{ id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of queries accessible to the user, ordered by creation time. **Warning:** Calling this API

```sql
SELECT
id,
warehouse_id,
display_name,
last_modifier_user_name,
owner_user_name,
apply_auto_limit,
catalog,
create_time,
description,
lifecycle_state,
parameters,
query_text,
run_as_mode,
schema,
tags,
update_time
FROM databricks_workspace.sql.queries
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

Creates a query.

```sql
INSERT INTO databricks_workspace.sql.queries (
auto_resolve_display_name,
query,
workspace
)
SELECT 
{{ auto_resolve_display_name }},
'{{ query }}',
'{{ workspace }}'
RETURNING
id,
warehouse_id,
display_name,
last_modifier_user_name,
owner_user_name,
apply_auto_limit,
catalog,
create_time,
description,
lifecycle_state,
parameters,
parent_path,
query_text,
run_as_mode,
schema,
tags,
update_time
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: queries
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the queries resource.
    - name: auto_resolve_display_name
      value: {{ auto_resolve_display_name }}
      description: |
        If true, automatically resolve query display name conflicts. Otherwise, fail the request if the query's display name conflicts with an existing query's display name.
    - name: query
      description: |
        :returns: :class:\`Query\`
      value:
        apply_auto_limit: {{ apply_auto_limit }}
        catalog: "{{ catalog }}"
        description: "{{ description }}"
        display_name: "{{ display_name }}"
        parameters:
          - date_range_value:
              date_range_value:
                start: "{{ start }}"
                end: "{{ end }}"
              dynamic_date_range_value: "{{ dynamic_date_range_value }}"
              precision: "{{ precision }}"
              start_day_of_week: {{ start_day_of_week }}
            date_value:
              date_value: "{{ date_value }}"
              dynamic_date_value: "{{ dynamic_date_value }}"
              precision: "{{ precision }}"
            enum_value:
              enum_options: "{{ enum_options }}"
              multi_values_options:
                prefix: "{{ prefix }}"
                separator: "{{ separator }}"
                suffix: "{{ suffix }}"
              values:
                - "{{ values }}"
            name: "{{ name }}"
            numeric_value:
              value: {{ value }}
            query_backed_value:
              multi_values_options:
                prefix: "{{ prefix }}"
                separator: "{{ separator }}"
                suffix: "{{ suffix }}"
              query_id: "{{ query_id }}"
              values:
                - "{{ values }}"
            text_value:
              value: "{{ value }}"
            title: "{{ title }}"
        parent_path: "{{ parent_path }}"
        query_text: "{{ query_text }}"
        run_as_mode: "{{ run_as_mode }}"
        schema: "{{ schema }}"
        tags:
          - "{{ tags }}"
        warehouse_id: "{{ warehouse_id }}"
`}</CodeBlock>

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

Updates a query.

```sql
UPDATE databricks_workspace.sql.queries
SET 
update_mask = '{{ update_mask }}',
auto_resolve_display_name = {{ auto_resolve_display_name }},
query = '{{ query }}'
WHERE 
id = '{{ id }}' --required
AND workspace = '{{ workspace }}' --required
AND update_mask = '{{ update_mask }}' --required
RETURNING
id,
warehouse_id,
display_name,
last_modifier_user_name,
owner_user_name,
apply_auto_limit,
catalog,
create_time,
description,
lifecycle_state,
parameters,
parent_path,
query_text,
run_as_mode,
schema,
tags,
update_time;
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

Moves a query to the trash. Trashed queries immediately disappear from searches and list views, and

```sql
DELETE FROM databricks_workspace.sql.queries
WHERE id = '{{ id }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

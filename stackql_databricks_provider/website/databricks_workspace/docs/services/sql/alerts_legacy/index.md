---
title: alerts_legacy
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_legacy
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

Creates, updates, deletes, gets or lists an <code>alerts_legacy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="alerts_legacy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.alerts_legacy" /></td></tr>
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
    "description": "Alert ID."
  },
  {
    "name": "name",
    "type": "string",
    "description": "Name of the alert."
  },
  {
    "name": "created_at",
    "type": "string",
    "description": ""
  },
  {
    "name": "last_triggered_at",
    "type": "string",
    "description": "Timestamp when the alert was last triggered."
  },
  {
    "name": "options",
    "type": "object",
    "description": "Alert configuration options.",
    "children": [
      {
        "name": "column",
        "type": "string",
        "description": "Name of column in the query result to compare in alert evaluation."
      },
      {
        "name": "op",
        "type": "string",
        "description": "Operator used to compare in alert evaluation: `>`, `>=`, `<`, `<=`, `==`, `!=`"
      },
      {
        "name": "value",
        "type": "object",
        "description": "Value used to compare in alert evaluation. Supported types include strings (eg. 'foobar'), floats (eg. 123.4), and booleans (true)."
      },
      {
        "name": "custom_body",
        "type": "string",
        "description": "Custom body of alert notification, if it exists. See [here] for custom templating instructions. [here]: https://docs.databricks.com/sql/user/alerts/index.html"
      },
      {
        "name": "custom_subject",
        "type": "string",
        "description": "Custom subject of alert notification, if it exists. This includes email subject, Slack notification header, etc. See [here] for custom templating instructions. [here]: https://docs.databricks.com/sql/user/alerts/index.html"
      },
      {
        "name": "empty_result_state",
        "type": "string",
        "description": "State that alert evaluates to when query result is empty. (ok, triggered, unknown)"
      },
      {
        "name": "muted",
        "type": "boolean",
        "description": "Whether or not the alert is muted. If an alert is muted, it will not notify users and notification destinations when triggered."
      }
    ]
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The identifier of the workspace folder containing the object."
  },
  {
    "name": "query",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "created_at",
        "type": "string",
        "description": ""
      },
      {
        "name": "data_source_id",
        "type": "string",
        "description": "Data source ID maps to the ID of the data source used by the resource and is distinct from the warehouse ID. [Learn more] [Learn more]: https://docs.databricks.com/api/workspace/datasources/list"
      },
      {
        "name": "description",
        "type": "string",
        "description": "General description that conveys additional information about this query such as usage notes."
      },
      {
        "name": "id",
        "type": "string",
        "description": "Query ID."
      },
      {
        "name": "is_archived",
        "type": "boolean",
        "description": "Indicates whether the query is trashed. Trashed queries can't be used in dashboards, or appear in search results. If this boolean is `true`, the `options` property for this query includes a `moved_to_trash_at` timestamp. Trashed queries are permanently deleted after 30 days."
      },
      {
        "name": "is_draft",
        "type": "boolean",
        "description": "Whether the query is a draft. Draft queries only appear in list views for their owners. Visualizations from draft queries cannot appear on dashboards."
      },
      {
        "name": "is_safe",
        "type": "boolean",
        "description": "Text parameter types are not safe from SQL injection for all types of data source. Set this Boolean parameter to `true` if a query either does not use any text type parameters or uses a data source type where text type parameters are handled safely."
      },
      {
        "name": "name",
        "type": "string",
        "description": "The title of this query that appears in list views, widget headings, and on the query page."
      },
      {
        "name": "options",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "catalog",
            "type": "string",
            "description": ""
          },
          {
            "name": "moved_to_trash_at",
            "type": "string",
            "description": "The timestamp when this query was moved to trash. Only present when the `is_archived` property is `true`. Trashed items are deleted after thirty days."
          },
          {
            "name": "parameters",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "enumOptions",
                "type": "string",
                "description": ""
              },
              {
                "name": "multiValuesOptions",
                "type": "object",
                "description": "If specified, allows multiple values to be selected for this parameter. Only applies to dropdown list and query-based dropdown list parameters."
              },
              {
                "name": "name",
                "type": "string",
                "description": "The literal parameter marker that appears between double curly braces in the query text."
              },
              {
                "name": "queryId",
                "type": "string",
                "description": "The UUID of the query that provides the parameter values. Only applies for query-based dropdown list parameters."
              },
              {
                "name": "title",
                "type": "string",
                "description": "The text displayed in a parameter picking widget."
              },
              {
                "name": "type",
                "type": "string",
                "description": "Parameters can have several different types. (datetime, enum, number, query, text)"
              },
              {
                "name": "value",
                "type": "object",
                "description": "The default value for this parameter."
              }
            ]
          },
          {
            "name": "schema",
            "type": "string",
            "description": "The name of the schema to execute this query in."
          }
        ]
      },
      {
        "name": "query",
        "type": "string",
        "description": "The text of the query to be run."
      },
      {
        "name": "tags",
        "type": "array",
        "description": ""
      },
      {
        "name": "updated_at",
        "type": "string",
        "description": "The timestamp at which this query was last updated."
      },
      {
        "name": "user_id",
        "type": "integer",
        "description": "The ID of the user who owns the query."
      }
    ]
  },
  {
    "name": "rearm",
    "type": "integer",
    "description": "Number of seconds after being triggered before the alert rearms itself and can be triggered again. If `null`, alert will never be triggered again."
  },
  {
    "name": "state",
    "type": "string",
    "description": "State of the alert. Possible values are: `unknown` (yet to be evaluated), `triggered` (evaluated and fulfilled trigger conditions), or `ok` (evaluated and did not fulfill trigger conditions). (ok, triggered, unknown)"
  },
  {
    "name": "updated_at",
    "type": "string",
    "description": "Timestamp when the alert was last updated."
  },
  {
    "name": "user",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "email",
        "type": "string",
        "description": ""
      },
      {
        "name": "id",
        "type": "integer",
        "description": ""
      },
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Alert ID."
  },
  {
    "name": "name",
    "type": "string",
    "description": "Name of the alert."
  },
  {
    "name": "created_at",
    "type": "string",
    "description": ""
  },
  {
    "name": "last_triggered_at",
    "type": "string",
    "description": "Timestamp when the alert was last triggered."
  },
  {
    "name": "options",
    "type": "object",
    "description": "Alert configuration options.",
    "children": [
      {
        "name": "column",
        "type": "string",
        "description": "Name of column in the query result to compare in alert evaluation."
      },
      {
        "name": "op",
        "type": "string",
        "description": "Operator used to compare in alert evaluation: `>`, `>=`, `<`, `<=`, `==`, `!=`"
      },
      {
        "name": "value",
        "type": "object",
        "description": "Value used to compare in alert evaluation. Supported types include strings (eg. 'foobar'), floats (eg. 123.4), and booleans (true)."
      },
      {
        "name": "custom_body",
        "type": "string",
        "description": "Custom body of alert notification, if it exists. See [here] for custom templating instructions. [here]: https://docs.databricks.com/sql/user/alerts/index.html"
      },
      {
        "name": "custom_subject",
        "type": "string",
        "description": "Custom subject of alert notification, if it exists. This includes email subject, Slack notification header, etc. See [here] for custom templating instructions. [here]: https://docs.databricks.com/sql/user/alerts/index.html"
      },
      {
        "name": "empty_result_state",
        "type": "string",
        "description": "State that alert evaluates to when query result is empty. (ok, triggered, unknown)"
      },
      {
        "name": "muted",
        "type": "boolean",
        "description": "Whether or not the alert is muted. If an alert is muted, it will not notify users and notification destinations when triggered."
      }
    ]
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The identifier of the workspace folder containing the object."
  },
  {
    "name": "query",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "created_at",
        "type": "string",
        "description": ""
      },
      {
        "name": "data_source_id",
        "type": "string",
        "description": "Data source ID maps to the ID of the data source used by the resource and is distinct from the warehouse ID. [Learn more] [Learn more]: https://docs.databricks.com/api/workspace/datasources/list"
      },
      {
        "name": "description",
        "type": "string",
        "description": "General description that conveys additional information about this query such as usage notes."
      },
      {
        "name": "id",
        "type": "string",
        "description": "Query ID."
      },
      {
        "name": "is_archived",
        "type": "boolean",
        "description": "Indicates whether the query is trashed. Trashed queries can't be used in dashboards, or appear in search results. If this boolean is `true`, the `options` property for this query includes a `moved_to_trash_at` timestamp. Trashed queries are permanently deleted after 30 days."
      },
      {
        "name": "is_draft",
        "type": "boolean",
        "description": "Whether the query is a draft. Draft queries only appear in list views for their owners. Visualizations from draft queries cannot appear on dashboards."
      },
      {
        "name": "is_safe",
        "type": "boolean",
        "description": "Text parameter types are not safe from SQL injection for all types of data source. Set this Boolean parameter to `true` if a query either does not use any text type parameters or uses a data source type where text type parameters are handled safely."
      },
      {
        "name": "name",
        "type": "string",
        "description": "The title of this query that appears in list views, widget headings, and on the query page."
      },
      {
        "name": "options",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "catalog",
            "type": "string",
            "description": ""
          },
          {
            "name": "moved_to_trash_at",
            "type": "string",
            "description": "The timestamp when this query was moved to trash. Only present when the `is_archived` property is `true`. Trashed items are deleted after thirty days."
          },
          {
            "name": "parameters",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "enumOptions",
                "type": "string",
                "description": ""
              },
              {
                "name": "multiValuesOptions",
                "type": "object",
                "description": "If specified, allows multiple values to be selected for this parameter. Only applies to dropdown list and query-based dropdown list parameters."
              },
              {
                "name": "name",
                "type": "string",
                "description": "The literal parameter marker that appears between double curly braces in the query text."
              },
              {
                "name": "queryId",
                "type": "string",
                "description": "The UUID of the query that provides the parameter values. Only applies for query-based dropdown list parameters."
              },
              {
                "name": "title",
                "type": "string",
                "description": "The text displayed in a parameter picking widget."
              },
              {
                "name": "type",
                "type": "string",
                "description": "Parameters can have several different types. (datetime, enum, number, query, text)"
              },
              {
                "name": "value",
                "type": "object",
                "description": "The default value for this parameter."
              }
            ]
          },
          {
            "name": "schema",
            "type": "string",
            "description": "The name of the schema to execute this query in."
          }
        ]
      },
      {
        "name": "query",
        "type": "string",
        "description": "The text of the query to be run."
      },
      {
        "name": "tags",
        "type": "array",
        "description": ""
      },
      {
        "name": "updated_at",
        "type": "string",
        "description": "The timestamp at which this query was last updated."
      },
      {
        "name": "user_id",
        "type": "integer",
        "description": "The ID of the user who owns the query."
      }
    ]
  },
  {
    "name": "rearm",
    "type": "integer",
    "description": "Number of seconds after being triggered before the alert rearms itself and can be triggered again. If `null`, alert will never be triggered again."
  },
  {
    "name": "state",
    "type": "string",
    "description": "State of the alert. Possible values are: `unknown` (yet to be evaluated), `triggered` (evaluated and fulfilled trigger conditions), or `ok` (evaluated and did not fulfill trigger conditions). (ok, triggered, unknown)"
  },
  {
    "name": "updated_at",
    "type": "string",
    "description": "Timestamp when the alert was last updated."
  },
  {
    "name": "user",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "email",
        "type": "string",
        "description": ""
      },
      {
        "name": "id",
        "type": "integer",
        "description": ""
      },
      {
        "name": "name",
        "type": "string",
        "description": ""
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
    <td><a href="#parameter-alert_id"><code>alert_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets an alert.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets a list of alerts.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-options"><code>options</code></a>, <a href="#parameter-query_id"><code>query_id</code></a></td>
    <td></td>
    <td>Creates an alert. An alert is a Databricks SQL object that periodically runs a query, evaluates a</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-alert_id"><code>alert_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-options"><code>options</code></a>, <a href="#parameter-query_id"><code>query_id</code></a></td>
    <td></td>
    <td>Updates an alert.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-alert_id"><code>alert_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Deletes an alert. Deleted alerts are no longer accessible and cannot be restored. **Note**: Unlike</td>
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
<tr id="parameter-alert_id">
    <td><CopyableCode code="alert_id" /></td>
    <td><code>string</code></td>
    <td>str</td>
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
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets an alert.

```sql
SELECT
id,
name,
created_at,
last_triggered_at,
options,
parent,
query,
rearm,
state,
updated_at,
user
FROM databricks_workspace.sql.alerts_legacy
WHERE alert_id = '{{ alert_id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of alerts.

```sql
SELECT
id,
name,
created_at,
last_triggered_at,
options,
parent,
query,
rearm,
state,
updated_at,
user
FROM databricks_workspace.sql.alerts_legacy
WHERE workspace = '{{ workspace }}' -- required
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

Creates an alert. An alert is a Databricks SQL object that periodically runs a query, evaluates a

```sql
INSERT INTO databricks_workspace.sql.alerts_legacy (
name,
options,
query_id,
parent,
rearm,
workspace
)
SELECT 
'{{ name }}' /* required */,
'{{ options }}' /* required */,
'{{ query_id }}' /* required */,
'{{ parent }}',
{{ rearm }},
'{{ workspace }}'
RETURNING
id,
name,
created_at,
last_triggered_at,
options,
parent,
query,
rearm,
state,
updated_at,
user
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: alerts_legacy
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the alerts_legacy resource.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the alert.
    - name: options
      description: |
        Alert configuration options.
      value:
        column: "{{ column }}"
        op: "{{ op }}"
        value: "{{ value }}"
        custom_body: "{{ custom_body }}"
        custom_subject: "{{ custom_subject }}"
        empty_result_state: "{{ empty_result_state }}"
        muted: {{ muted }}
    - name: query_id
      value: "{{ query_id }}"
      description: |
        Query ID.
    - name: parent
      value: "{{ parent }}"
      description: |
        The identifier of the workspace folder containing the object.
    - name: rearm
      value: {{ rearm }}
      description: |
        Number of seconds after being triggered before the alert rearms itself and can be triggered again. If \`null\`, alert will never be triggered again.
`}</CodeBlock>

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

Updates an alert.

```sql
REPLACE databricks_workspace.sql.alerts_legacy
SET 
name = '{{ name }}',
options = '{{ options }}',
query_id = '{{ query_id }}',
rearm = {{ rearm }}
WHERE 
alert_id = '{{ alert_id }}' --required
AND workspace = '{{ workspace }}' --required
AND name = '{{ name }}' --required
AND options = '{{ options }}' --required
AND query_id = '{{ query_id }}' --required;
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

Deletes an alert. Deleted alerts are no longer accessible and cannot be restored. **Note**: Unlike

```sql
DELETE FROM databricks_workspace.sql.alerts_legacy
WHERE alert_id = '{{ alert_id }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

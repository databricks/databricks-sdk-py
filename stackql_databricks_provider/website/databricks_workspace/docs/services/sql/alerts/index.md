---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
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

Creates, updates, deletes, gets or lists an <code>alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="alerts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.alerts" /></td></tr>
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
    "description": "UUID identifying the alert."
  },
  {
    "name": "query_id",
    "type": "string",
    "description": "UUID of the query attached to the alert."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "The display name of the alert."
  },
  {
    "name": "owner_user_name",
    "type": "string",
    "description": "The owner's username. This field is set to \"Unavailable\" if the user has been deleted."
  },
  {
    "name": "condition",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "empty_result_state",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (OK, TRIGGERED, UNKNOWN)"
      },
      {
        "name": "op",
        "type": "string",
        "description": "Operator used for comparison in alert evaluation. (EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, IS_NULL, LESS_THAN, LESS_THAN_OR_EQUAL, NOT_EQUAL)"
      },
      {
        "name": "operand",
        "type": "object",
        "description": "Name of the column from the query result to use for comparison in alert evaluation.",
        "children": [
          {
            "name": "column",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "threshold",
        "type": "object",
        "description": "Threshold value used for comparison in alert evaluation.",
        "children": [
          {
            "name": "value",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "bool_value",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "double_value",
                "type": "number",
                "description": ""
              },
              {
                "name": "string_value",
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
    "name": "create_time",
    "type": "string",
    "description": "The timestamp indicating when the alert was created."
  },
  {
    "name": "custom_body",
    "type": "string",
    "description": "Custom body of alert notification, if it exists. See [here] for custom templating instructions. [here]: https://docs.databricks.com/sql/user/alerts/index.html"
  },
  {
    "name": "custom_subject",
    "type": "string",
    "description": "Custom subject of alert notification, if it exists. This can include email subject entries and Slack notification headers, for example. See [here] for custom templating instructions. [here]: https://docs.databricks.com/sql/user/alerts/index.html"
  },
  {
    "name": "lifecycle_state",
    "type": "string",
    "description": "The workspace state of the alert. Used for tracking trashed status. (ACTIVE, TRASHED)"
  },
  {
    "name": "notify_on_ok",
    "type": "boolean",
    "description": "Whether to notify alert subscribers when alert returns back to normal."
  },
  {
    "name": "parent_path",
    "type": "string",
    "description": "The workspace path of the folder containing the alert."
  },
  {
    "name": "seconds_to_retrigger",
    "type": "integer",
    "description": "Number of seconds an alert must wait after being triggered to rearm itself. After rearming, it can be triggered again. If 0 or not specified, the alert will not be triggered again."
  },
  {
    "name": "state",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (OK, TRIGGERED, UNKNOWN)"
  },
  {
    "name": "trigger_time",
    "type": "string",
    "description": "Timestamp when the alert was last triggered, if the alert has been triggered before."
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "The timestamp indicating when the alert was updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "UUID identifying the alert."
  },
  {
    "name": "query_id",
    "type": "string",
    "description": "UUID of the query attached to the alert."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "The display name of the alert."
  },
  {
    "name": "owner_user_name",
    "type": "string",
    "description": "The owner's username. This field is set to \"Unavailable\" if the user has been deleted."
  },
  {
    "name": "condition",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "empty_result_state",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (OK, TRIGGERED, UNKNOWN)"
      },
      {
        "name": "op",
        "type": "string",
        "description": "Operator used for comparison in alert evaluation. (EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, IS_NULL, LESS_THAN, LESS_THAN_OR_EQUAL, NOT_EQUAL)"
      },
      {
        "name": "operand",
        "type": "object",
        "description": "Name of the column from the query result to use for comparison in alert evaluation.",
        "children": [
          {
            "name": "column",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "threshold",
        "type": "object",
        "description": "Threshold value used for comparison in alert evaluation.",
        "children": [
          {
            "name": "value",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "bool_value",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "double_value",
                "type": "number",
                "description": ""
              },
              {
                "name": "string_value",
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
    "name": "create_time",
    "type": "string",
    "description": "The timestamp indicating when the alert was created."
  },
  {
    "name": "custom_body",
    "type": "string",
    "description": "Custom body of alert notification, if it exists. See [here] for custom templating instructions. [here]: https://docs.databricks.com/sql/user/alerts/index.html"
  },
  {
    "name": "custom_subject",
    "type": "string",
    "description": "Custom subject of alert notification, if it exists. This can include email subject entries and Slack notification headers, for example. See [here] for custom templating instructions. [here]: https://docs.databricks.com/sql/user/alerts/index.html"
  },
  {
    "name": "lifecycle_state",
    "type": "string",
    "description": "The workspace state of the alert. Used for tracking trashed status. (ACTIVE, TRASHED)"
  },
  {
    "name": "notify_on_ok",
    "type": "boolean",
    "description": "Whether to notify alert subscribers when alert returns back to normal."
  },
  {
    "name": "seconds_to_retrigger",
    "type": "integer",
    "description": "Number of seconds an alert must wait after being triggered to rearm itself. After rearming, it can be triggered again. If 0 or not specified, the alert will not be triggered again."
  },
  {
    "name": "state",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (OK, TRIGGERED, UNKNOWN)"
  },
  {
    "name": "trigger_time",
    "type": "string",
    "description": "Timestamp when the alert was last triggered, if the alert has been triggered before."
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "The timestamp indicating when the alert was updated."
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets an alert.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets a list of alerts accessible to the user, ordered by creation time. **Warning:** Calling this API</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates an alert.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a></td>
    <td></td>
    <td>Updates an alert.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Moves an alert to the trash. Trashed alerts immediately disappear from searches and list views, and</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>str</td>
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

Gets an alert.

```sql
SELECT
id,
query_id,
display_name,
owner_user_name,
condition,
create_time,
custom_body,
custom_subject,
lifecycle_state,
notify_on_ok,
parent_path,
seconds_to_retrigger,
state,
trigger_time,
update_time
FROM databricks_workspace.sql.alerts
WHERE id = '{{ id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of alerts accessible to the user, ordered by creation time. **Warning:** Calling this API

```sql
SELECT
id,
query_id,
display_name,
owner_user_name,
condition,
create_time,
custom_body,
custom_subject,
lifecycle_state,
notify_on_ok,
seconds_to_retrigger,
state,
trigger_time,
update_time
FROM databricks_workspace.sql.alerts
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

Creates an alert.

```sql
INSERT INTO databricks_workspace.sql.alerts (
alert,
auto_resolve_display_name,
deployment_name
)
SELECT 
'{{ alert }}',
{{ auto_resolve_display_name }},
'{{ deployment_name }}'
RETURNING
id,
query_id,
display_name,
owner_user_name,
condition,
create_time,
custom_body,
custom_subject,
lifecycle_state,
notify_on_ok,
parent_path,
seconds_to_retrigger,
state,
trigger_time,
update_time
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: alerts
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the alerts resource.
    - name: alert
      description: |
        :param auto_resolve_display_name: bool (optional) If true, automatically resolve alert display name conflicts. Otherwise, fail the request if the alert's display name conflicts with an existing alert's display name.
      value:
        condition:
          empty_result_state: "{{ empty_result_state }}"
          op: "{{ op }}"
          operand:
            column:
              name: "{{ name }}"
          threshold:
            value:
              bool_value: {{ bool_value }}
              double_value: {{ double_value }}
              string_value: "{{ string_value }}"
        custom_body: "{{ custom_body }}"
        custom_subject: "{{ custom_subject }}"
        display_name: "{{ display_name }}"
        notify_on_ok: {{ notify_on_ok }}
        parent_path: "{{ parent_path }}"
        query_id: "{{ query_id }}"
        seconds_to_retrigger: {{ seconds_to_retrigger }}
    - name: auto_resolve_display_name
      value: {{ auto_resolve_display_name }}
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

Updates an alert.

```sql
UPDATE databricks_workspace.sql.alerts
SET 
update_mask = '{{ update_mask }}',
alert = '{{ alert }}',
auto_resolve_display_name = {{ auto_resolve_display_name }}
WHERE 
id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND update_mask = '{{ update_mask }}' --required
RETURNING
id,
query_id,
display_name,
owner_user_name,
condition,
create_time,
custom_body,
custom_subject,
lifecycle_state,
notify_on_ok,
parent_path,
seconds_to_retrigger,
state,
trigger_time,
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

Moves an alert to the trash. Trashed alerts immediately disappear from searches and list views, and

```sql
DELETE FROM databricks_workspace.sql.alerts
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

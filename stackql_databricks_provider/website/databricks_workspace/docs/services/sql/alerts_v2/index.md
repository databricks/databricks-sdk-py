---
title: alerts_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_v2
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

Creates, updates, deletes, gets or lists an <code>alerts_v2</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="alerts_v2" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.alerts_v2" /></td></tr>
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
    "name": "warehouse_id",
    "type": "string",
    "description": "ID of the SQL warehouse attached to the alert."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "owner_user_name",
    "type": "string",
    "description": "The owner's username. This field is set to \"Unavailable\" if the user has been deleted."
  },
  {
    "name": "run_as_user_name",
    "type": "string",
    "description": "The run as username or application ID of service principal. On Create and Update, this field can be set to application ID of an active service principal. Setting this field requires the servicePrincipal/user role. Deprecated: Use `run_as` field instead. This field will be removed in a future release."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "The timestamp indicating when the alert was created."
  },
  {
    "name": "custom_description",
    "type": "string",
    "description": "Custom description for the alert. support mustache template."
  },
  {
    "name": "custom_summary",
    "type": "string",
    "description": "Custom summary for the alert. support mustache template."
  },
  {
    "name": "effective_run_as",
    "type": "object",
    "description": "The actual identity that will be used to execute the alert. This is an output-only field that shows the resolved run-as identity after applying permissions and defaults.",
    "children": [
      {
        "name": "service_principal_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "user_name",
        "type": "string",
        "description": "The email of an active workspace user. Can only set this field to their own email."
      }
    ]
  },
  {
    "name": "evaluation",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "source",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "aggregation",
            "type": "string",
            "description": "If not set, the behavior is equivalent to using `First row` in the UI. (AVG, COUNT, COUNT_DISTINCT, MAX, MEDIAN, MIN, STDDEV, SUM)"
          },
          {
            "name": "display",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "comparison_operator",
        "type": "string",
        "description": "Operator used for comparison in alert evaluation. (EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, IS_NOT_NULL, IS_NULL, LESS_THAN, LESS_THAN_OR_EQUAL, NOT_EQUAL)"
      },
      {
        "name": "empty_result_state",
        "type": "string",
        "description": "Alert state if result is empty. Please avoid setting this field to be `UNKNOWN` because `UNKNOWN` state is planned to be deprecated. (ERROR, OK, TRIGGERED, UNKNOWN)"
      },
      {
        "name": "last_evaluated_at",
        "type": "string",
        "description": "Timestamp of the last evaluation."
      },
      {
        "name": "notification",
        "type": "object",
        "description": "User or Notification Destination to notify when alert is triggered.",
        "children": [
          {
            "name": "notify_on_ok",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "retrigger_seconds",
            "type": "integer",
            "description": "Number of seconds an alert waits after being triggered before it is allowed to send another notification. If set to 0 or omitted, the alert will not send any further notifications after the first trigger Setting this value to 1 allows the alert to send a notification on every evaluation where the condition is met, effectively making it always retrigger for notification purposes."
          },
          {
            "name": "subscriptions",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "destination_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "user_email",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "state",
        "type": "string",
        "description": "Latest state of alert evaluation. (ERROR, OK, TRIGGERED, UNKNOWN)"
      },
      {
        "name": "threshold",
        "type": "object",
        "description": "Threshold to user for alert evaluation, can be a column or a value.",
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
              },
              {
                "name": "aggregation",
                "type": "string",
                "description": "If not set, the behavior is equivalent to using `First row` in the UI. (AVG, COUNT, COUNT_DISTINCT, MAX, MEDIAN, MIN, STDDEV, SUM)"
              },
              {
                "name": "display",
                "type": "string",
                "description": ""
              }
            ]
          },
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
    "name": "lifecycle_state",
    "type": "string",
    "description": "Indicates whether the query is trashed. (ACTIVE, DELETED)"
  },
  {
    "name": "parent_path",
    "type": "string",
    "description": "The workspace path of the folder containing the alert. Can only be set on create, and cannot be updated."
  },
  {
    "name": "query_text",
    "type": "string",
    "description": "Text of the query to be run."
  },
  {
    "name": "run_as",
    "type": "object",
    "description": "Specifies the identity that will be used to run the alert. This field allows you to configure alerts to run as a specific user or service principal. - For user identity: Set `user_name` to the email of an active workspace user. Users can only set this to their own email. - For service principal: Set `service_principal_name` to the application ID. Requires the `servicePrincipal/user` role. If not specified, the alert will run as the request user.",
    "children": [
      {
        "name": "service_principal_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "user_name",
        "type": "string",
        "description": "The email of an active workspace user. Can only set this field to their own email."
      }
    ]
  },
  {
    "name": "schedule",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "quartz_cron_schedule",
        "type": "string",
        "description": ""
      },
      {
        "name": "timezone_id",
        "type": "string",
        "description": "A Java timezone id. The schedule will be resolved using this timezone. This will be combined with the quartz_cron_schedule to determine the schedule. See https://docs.databricks.com/sql/language-manual/sql-ref-syntax-aux-conf-mgmt-set-timezone.html for details."
      },
      {
        "name": "pause_status",
        "type": "string",
        "description": "Indicate whether this schedule is paused or not. (PAUSED, UNPAUSED)"
      }
    ]
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
    "name": "warehouse_id",
    "type": "string",
    "description": "ID of the SQL warehouse attached to the alert."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "owner_user_name",
    "type": "string",
    "description": "The owner's username. This field is set to \"Unavailable\" if the user has been deleted."
  },
  {
    "name": "run_as_user_name",
    "type": "string",
    "description": "The run as username or application ID of service principal. On Create and Update, this field can be set to application ID of an active service principal. Setting this field requires the servicePrincipal/user role. Deprecated: Use `run_as` field instead. This field will be removed in a future release."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "The timestamp indicating when the alert was created."
  },
  {
    "name": "custom_description",
    "type": "string",
    "description": "Custom description for the alert. support mustache template."
  },
  {
    "name": "custom_summary",
    "type": "string",
    "description": "Custom summary for the alert. support mustache template."
  },
  {
    "name": "effective_run_as",
    "type": "object",
    "description": "The actual identity that will be used to execute the alert. This is an output-only field that shows the resolved run-as identity after applying permissions and defaults.",
    "children": [
      {
        "name": "service_principal_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "user_name",
        "type": "string",
        "description": "The email of an active workspace user. Can only set this field to their own email."
      }
    ]
  },
  {
    "name": "evaluation",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "source",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "aggregation",
            "type": "string",
            "description": "If not set, the behavior is equivalent to using `First row` in the UI. (AVG, COUNT, COUNT_DISTINCT, MAX, MEDIAN, MIN, STDDEV, SUM)"
          },
          {
            "name": "display",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "comparison_operator",
        "type": "string",
        "description": "Operator used for comparison in alert evaluation. (EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, IS_NOT_NULL, IS_NULL, LESS_THAN, LESS_THAN_OR_EQUAL, NOT_EQUAL)"
      },
      {
        "name": "empty_result_state",
        "type": "string",
        "description": "Alert state if result is empty. Please avoid setting this field to be `UNKNOWN` because `UNKNOWN` state is planned to be deprecated. (ERROR, OK, TRIGGERED, UNKNOWN)"
      },
      {
        "name": "last_evaluated_at",
        "type": "string",
        "description": "Timestamp of the last evaluation."
      },
      {
        "name": "notification",
        "type": "object",
        "description": "User or Notification Destination to notify when alert is triggered.",
        "children": [
          {
            "name": "notify_on_ok",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "retrigger_seconds",
            "type": "integer",
            "description": "Number of seconds an alert waits after being triggered before it is allowed to send another notification. If set to 0 or omitted, the alert will not send any further notifications after the first trigger Setting this value to 1 allows the alert to send a notification on every evaluation where the condition is met, effectively making it always retrigger for notification purposes."
          },
          {
            "name": "subscriptions",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "destination_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "user_email",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "state",
        "type": "string",
        "description": "Latest state of alert evaluation. (ERROR, OK, TRIGGERED, UNKNOWN)"
      },
      {
        "name": "threshold",
        "type": "object",
        "description": "Threshold to user for alert evaluation, can be a column or a value.",
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
              },
              {
                "name": "aggregation",
                "type": "string",
                "description": "If not set, the behavior is equivalent to using `First row` in the UI. (AVG, COUNT, COUNT_DISTINCT, MAX, MEDIAN, MIN, STDDEV, SUM)"
              },
              {
                "name": "display",
                "type": "string",
                "description": ""
              }
            ]
          },
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
    "name": "lifecycle_state",
    "type": "string",
    "description": "Indicates whether the query is trashed. (ACTIVE, DELETED)"
  },
  {
    "name": "parent_path",
    "type": "string",
    "description": "The workspace path of the folder containing the alert. Can only be set on create, and cannot be updated."
  },
  {
    "name": "query_text",
    "type": "string",
    "description": "Text of the query to be run."
  },
  {
    "name": "run_as",
    "type": "object",
    "description": "Specifies the identity that will be used to run the alert. This field allows you to configure alerts to run as a specific user or service principal. - For user identity: Set `user_name` to the email of an active workspace user. Users can only set this to their own email. - For service principal: Set `service_principal_name` to the application ID. Requires the `servicePrincipal/user` role. If not specified, the alert will run as the request user.",
    "children": [
      {
        "name": "service_principal_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "user_name",
        "type": "string",
        "description": "The email of an active workspace user. Can only set this field to their own email."
      }
    ]
  },
  {
    "name": "schedule",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "quartz_cron_schedule",
        "type": "string",
        "description": ""
      },
      {
        "name": "timezone_id",
        "type": "string",
        "description": "A Java timezone id. The schedule will be resolved using this timezone. This will be combined with the quartz_cron_schedule to determine the schedule. See https://docs.databricks.com/sql/language-manual/sql-ref-syntax-aux-conf-mgmt-set-timezone.html for details."
      },
      {
        "name": "pause_status",
        "type": "string",
        "description": "Indicate whether this schedule is paused or not. (PAUSED, UNPAUSED)"
      }
    ]
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
    <td>Gets a list of alerts accessible to the user, ordered by creation time.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-alert"><code>alert</code></a></td>
    <td></td>
    <td>Create Alert</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-alert"><code>alert</code></a></td>
    <td></td>
    <td>Update alert</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-purge"><code>purge</code></a></td>
    <td>Moves an alert to the trash. Trashed alerts immediately disappear from list views, and can no longer</td>
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
    <td>:param purge: bool (optional) Whether to permanently delete the alert. If not set, the alert will only be soft deleted.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td></td>
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
<tr id="parameter-purge">
    <td><CopyableCode code="purge" /></td>
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
warehouse_id,
display_name,
owner_user_name,
run_as_user_name,
create_time,
custom_description,
custom_summary,
effective_run_as,
evaluation,
lifecycle_state,
parent_path,
query_text,
run_as,
schedule,
update_time
FROM databricks_workspace.sql.alerts_v2
WHERE id = '{{ id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of alerts accessible to the user, ordered by creation time.

```sql
SELECT
id,
warehouse_id,
display_name,
owner_user_name,
run_as_user_name,
create_time,
custom_description,
custom_summary,
effective_run_as,
evaluation,
lifecycle_state,
parent_path,
query_text,
run_as,
schedule,
update_time
FROM databricks_workspace.sql.alerts_v2
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

Create Alert

```sql
INSERT INTO databricks_workspace.sql.alerts_v2 (
alert,
deployment_name
)
SELECT 
'{{ alert }}' /* required */,
'{{ deployment_name }}'
RETURNING
id,
warehouse_id,
display_name,
owner_user_name,
run_as_user_name,
create_time,
custom_description,
custom_summary,
effective_run_as,
evaluation,
lifecycle_state,
parent_path,
query_text,
run_as,
schedule,
update_time
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: alerts_v2
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the alerts_v2 resource.
    - name: alert
      value: string
      description: |
        :returns: :class:`AlertV2`
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

Update alert

```sql
UPDATE databricks_workspace.sql.alerts_v2
SET 
alert = '{{ alert }}'
WHERE 
id = '{{ id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND alert = '{{ alert }}' --required
RETURNING
id,
warehouse_id,
display_name,
owner_user_name,
run_as_user_name,
create_time,
custom_description,
custom_summary,
effective_run_as,
evaluation,
lifecycle_state,
parent_path,
query_text,
run_as,
schedule,
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

Moves an alert to the trash. Trashed alerts immediately disappear from list views, and can no longer

```sql
DELETE FROM databricks_workspace.sql.alerts_v2
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND purge = '{{ purge }}'
;
```
</TabItem>
</Tabs>

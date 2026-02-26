---
title: lakeview_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - lakeview_subscriptions
  - dashboards
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

Creates, updates, deletes, gets or lists a <code>lakeview_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lakeview_subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dashboards.lakeview_subscriptions" /></td></tr>
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
    "name": "created_by_user_id",
    "type": "integer",
    "description": "UserId of the user who adds subscribers (users or notification destinations) to the dashboard's schedule."
  },
  {
    "name": "dashboard_id",
    "type": "string",
    "description": "UUID identifying the dashboard to which the subscription belongs."
  },
  {
    "name": "schedule_id",
    "type": "string",
    "description": "UUID identifying the schedule to which the subscription belongs."
  },
  {
    "name": "subscription_id",
    "type": "string",
    "description": "UUID identifying the subscription."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "A timestamp indicating when the subscription was created."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "The etag for the subscription. Must be left empty on create, can be optionally provided on delete to ensure that the subscription has not been deleted since the last read."
  },
  {
    "name": "subscriber",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "destination_subscriber",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "destination_id",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "user_subscriber",
        "type": "object",
        "description": "The user to receive the subscription email. This parameter is mutually exclusive with `destination_subscriber`.",
        "children": [
          {
            "name": "user_id",
            "type": "integer",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "A timestamp indicating when the subscription was last updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "created_by_user_id",
    "type": "integer",
    "description": "UserId of the user who adds subscribers (users or notification destinations) to the dashboard's schedule."
  },
  {
    "name": "dashboard_id",
    "type": "string",
    "description": "UUID identifying the dashboard to which the subscription belongs."
  },
  {
    "name": "schedule_id",
    "type": "string",
    "description": "UUID identifying the schedule to which the subscription belongs."
  },
  {
    "name": "subscription_id",
    "type": "string",
    "description": "UUID identifying the subscription."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "A timestamp indicating when the subscription was created."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "The etag for the subscription. Must be left empty on create, can be optionally provided on delete to ensure that the subscription has not been deleted since the last read."
  },
  {
    "name": "subscriber",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "destination_subscriber",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "destination_id",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "user_subscriber",
        "type": "object",
        "description": "The user to receive the subscription email. This parameter is mutually exclusive with `destination_subscriber`.",
        "children": [
          {
            "name": "user_id",
            "type": "integer",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "A timestamp indicating when the subscription was last updated."
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
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-schedule_id"><code>schedule_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get schedule subscription.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-schedule_id"><code>schedule_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List schedule subscriptions.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-schedule_id"><code>schedule_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription"><code>subscription</code></a></td>
    <td></td>
    <td>Create schedule subscription.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-schedule_id"><code>schedule_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Delete schedule subscription.</td>
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
<tr id="parameter-dashboard_id">
    <td><CopyableCode code="dashboard_id" /></td>
    <td><code>string</code></td>
    <td>UUID identifying the dashboard which the subscription belongs.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-schedule_id">
    <td><CopyableCode code="schedule_id" /></td>
    <td><code>string</code></td>
    <td>UUID identifying the schedule which the subscription belongs.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td>UUID identifying the subscription.</td>
</tr>
<tr id="parameter-etag">
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the subscription. Can be optionally provided to ensure that the subscription has not been modified since the last read.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The number of subscriptions to return per page.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous `ListSubscriptions` call. Use this to retrieve the subsequent page.</td>
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

Get schedule subscription.

```sql
SELECT
created_by_user_id,
dashboard_id,
schedule_id,
subscription_id,
create_time,
etag,
subscriber,
update_time
FROM databricks_workspace.dashboards.lakeview_subscriptions
WHERE dashboard_id = '{{ dashboard_id }}' -- required
AND schedule_id = '{{ schedule_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List schedule subscriptions.

```sql
SELECT
created_by_user_id,
dashboard_id,
schedule_id,
subscription_id,
create_time,
etag,
subscriber,
update_time
FROM databricks_workspace.dashboards.lakeview_subscriptions
WHERE dashboard_id = '{{ dashboard_id }}' -- required
AND schedule_id = '{{ schedule_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
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

Create schedule subscription.

```sql
INSERT INTO databricks_workspace.dashboards.lakeview_subscriptions (
subscription,
dashboard_id,
schedule_id,
deployment_name
)
SELECT 
'{{ subscription }}' /* required */,
'{{ dashboard_id }}',
'{{ schedule_id }}',
'{{ deployment_name }}'
RETURNING
created_by_user_id,
dashboard_id,
schedule_id,
subscription_id,
create_time,
etag,
subscriber,
update_time
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: lakeview_subscriptions
  props:
    - name: dashboard_id
      value: "{{ dashboard_id }}"
      description: Required parameter for the lakeview_subscriptions resource.
    - name: schedule_id
      value: "{{ schedule_id }}"
      description: Required parameter for the lakeview_subscriptions resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the lakeview_subscriptions resource.
    - name: subscription
      description: |
        The subscription to create. A schedule is limited to 100 subscriptions.
      value:
        subscriber:
          destination_subscriber:
            destination_id: "{{ destination_id }}"
          user_subscriber:
            user_id: {{ user_id }}
        create_time: "{{ create_time }}"
        created_by_user_id: {{ created_by_user_id }}
        dashboard_id: "{{ dashboard_id }}"
        etag: "{{ etag }}"
        schedule_id: "{{ schedule_id }}"
        subscription_id: "{{ subscription_id }}"
        update_time: "{{ update_time }}"
`}</CodeBlock>

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

Delete schedule subscription.

```sql
DELETE FROM databricks_workspace.dashboards.lakeview_subscriptions
WHERE dashboard_id = '{{ dashboard_id }}' --required
AND schedule_id = '{{ schedule_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND etag = '{{ etag }}'
;
```
</TabItem>
</Tabs>

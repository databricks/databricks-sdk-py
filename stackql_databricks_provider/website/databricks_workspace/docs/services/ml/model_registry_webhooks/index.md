---
title: model_registry_webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - model_registry_webhooks
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>model_registry_webhooks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="model_registry_webhooks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.model_registry_webhooks" /></td></tr>
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
    "description": "Webhook ID"
  },
  {
    "name": "model_name",
    "type": "string",
    "description": "Name of the model whose events would trigger this webhook."
  },
  {
    "name": "creation_timestamp",
    "type": "integer",
    "description": ""
  },
  {
    "name": "description",
    "type": "string",
    "description": "User-specified description for the webhook."
  },
  {
    "name": "events",
    "type": "array",
    "description": "Events that can trigger a registry webhook: * `MODEL_VERSION_CREATED`: A new model version was created for the associated model. * `MODEL_VERSION_TRANSITIONED_STAGE`: A model version’s stage was changed. * `TRANSITION_REQUEST_CREATED`: A user requested a model version’s stage be transitioned. * `COMMENT_CREATED`: A user wrote a comment on a registered model. * `REGISTERED_MODEL_CREATED`: A new registered model was created. This event type can only be specified for a registry-wide webhook, which can be created by not specifying a model name in the create request. * `MODEL_VERSION_TAG_SET`: A user set a tag on the model version. * `MODEL_VERSION_TRANSITIONED_TO_STAGING`: A model version was transitioned to staging. * `MODEL_VERSION_TRANSITIONED_TO_PRODUCTION`: A model version was transitioned to production. * `MODEL_VERSION_TRANSITIONED_TO_ARCHIVED`: A model version was archived. * `TRANSITION_REQUEST_TO_STAGING_CREATED`: A user requested a model version be transitioned to staging. * `TRANSITION_REQUEST_TO_PRODUCTION_CREATED`: A user requested a model version be transitioned to production. * `TRANSITION_REQUEST_TO_ARCHIVED_CREATED`: A user requested a model version be archived."
  },
  {
    "name": "http_url_spec",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "enable_ssl_verification",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "url",
        "type": "string",
        "description": "External HTTPS URL called on event trigger (by using a POST request)."
      }
    ]
  },
  {
    "name": "job_spec",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "job_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "workspace_url",
        "type": "string",
        "description": "URL of the workspace containing the job that this webhook runs. If not specified, the job’s workspace URL is assumed to be the same as the workspace where the webhook is created."
      }
    ]
  },
  {
    "name": "last_updated_timestamp",
    "type": "integer",
    "description": "Time of the object at last update, as a Unix timestamp in milliseconds."
  },
  {
    "name": "status",
    "type": "string",
    "description": "Enable or disable triggering the webhook, or put the webhook into test mode. The default is<br />`ACTIVE`: * `ACTIVE`: Webhook is triggered when an associated event happens.<br /><br />* `DISABLED`: Webhook is not triggered.<br /><br />* `TEST_MODE`: Webhook can be triggered through the test endpoint, but is not triggered on a<br />real event. (ACTIVE, DISABLED, TEST_MODE)"
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
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-events"><code>events</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-model_name"><code>model_name</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>**NOTE:** This endpoint is in Public Preview. Lists all registry webhooks.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-events"><code>events</code></a></td>
    <td></td>
    <td>**NOTE:** This endpoint is in Public Preview. Creates a registry webhook.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>**NOTE:** This endpoint is in Public Preview. Updates a registry webhook.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>**NOTE:** This endpoint is in Public Preview. Deletes a registry webhook.</td>
</tr>
<tr>
    <td><a href="#test"><CopyableCode code="test" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>**NOTE:** This endpoint is in Public Preview. Tests a registry webhook.</td>
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
    <td>Webhook ID required to delete a registry webhook.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-events">
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td>Events that trigger the webhook. * `MODEL_VERSION_CREATED`: A new model version was created for the associated model. * `MODEL_VERSION_TRANSITIONED_STAGE`: A model version’s stage was changed. * `TRANSITION_REQUEST_CREATED`: A user requested a model version’s stage be transitioned. * `COMMENT_CREATED`: A user wrote a comment on a registered model. * `REGISTERED_MODEL_CREATED`: A new registered model was created. This event type can only be specified for a registry-wide webhook, which can be created by not specifying a model name in the create request. * `MODEL_VERSION_TAG_SET`: A user set a tag on the model version. * `MODEL_VERSION_TRANSITIONED_TO_STAGING`: A model version was transitioned to staging. * `MODEL_VERSION_TRANSITIONED_TO_PRODUCTION`: A model version was transitioned to production. * `MODEL_VERSION_TRANSITIONED_TO_ARCHIVED`: A model version was archived. * `TRANSITION_REQUEST_TO_STAGING_CREATED`: A user requested a model version be transitioned to staging. * `TRANSITION_REQUEST_TO_PRODUCTION_CREATED`: A user requested a model version be transitioned to production. * `TRANSITION_REQUEST_TO_ARCHIVED_CREATED`: A user requested a model version be archived. If `events` is specified, any webhook with one or more of the specified trigger events is included in the output. If `events` is not specified, webhooks of all event types are included in the output.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
    <td>:param model_name: str (optional) Registered model name If not specified, all webhooks associated with the specified events are listed, regardless of their associated model.</td>
</tr>
<tr id="parameter-model_name">
    <td><CopyableCode code="model_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Token indicating the page of artifact results to fetch</td>
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

**NOTE:** This endpoint is in Public Preview. Lists all registry webhooks.

```sql
SELECT
id,
model_name,
creation_timestamp,
description,
events,
http_url_spec,
job_spec,
last_updated_timestamp,
status
FROM databricks_workspace.ml.model_registry_webhooks
WHERE workspace = '{{ workspace }}' -- required
AND events = '{{ events }}'
AND max_results = '{{ max_results }}'
AND model_name = '{{ model_name }}'
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

**NOTE:** This endpoint is in Public Preview. Creates a registry webhook.

```sql
INSERT INTO databricks_workspace.ml.model_registry_webhooks (
events,
description,
http_url_spec,
job_spec,
model_name,
status,
workspace
)
SELECT 
'{{ events }}' /* required */,
'{{ description }}',
'{{ http_url_spec }}',
'{{ job_spec }}',
'{{ model_name }}',
'{{ status }}',
'{{ workspace }}'
RETURNING
webhook
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: model_registry_webhooks
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the model_registry_webhooks resource.
    - name: events
      value:
        - "{{ events }}"
      description: |
        Events that can trigger a registry webhook: * \`MODEL_VERSION_CREATED\`: A new model version was created for the associated model. * \`MODEL_VERSION_TRANSITIONED_STAGE\`: A model version’s stage was changed. * \`TRANSITION_REQUEST_CREATED\`: A user requested a model version’s stage be transitioned. * \`COMMENT_CREATED\`: A user wrote a comment on a registered model. * \`REGISTERED_MODEL_CREATED\`: A new registered model was created. This event type can only be specified for a registry-wide webhook, which can be created by not specifying a model name in the create request. * \`MODEL_VERSION_TAG_SET\`: A user set a tag on the model version. * \`MODEL_VERSION_TRANSITIONED_TO_STAGING\`: A model version was transitioned to staging. * \`MODEL_VERSION_TRANSITIONED_TO_PRODUCTION\`: A model version was transitioned to production. * \`MODEL_VERSION_TRANSITIONED_TO_ARCHIVED\`: A model version was archived. * \`TRANSITION_REQUEST_TO_STAGING_CREATED\`: A user requested a model version be transitioned to staging. * \`TRANSITION_REQUEST_TO_PRODUCTION_CREATED\`: A user requested a model version be transitioned to production. * \`TRANSITION_REQUEST_TO_ARCHIVED_CREATED\`: A user requested a model version be archived.
    - name: description
      value: "{{ description }}"
      description: |
        User-specified description for the webhook.
    - name: http_url_spec
      description: |
        External HTTPS URL called on event trigger (by using a POST request).
      value:
        url: "{{ url }}"
        authorization: "{{ authorization }}"
        enable_ssl_verification: {{ enable_ssl_verification }}
        secret: "{{ secret }}"
    - name: job_spec
      description: |
        ID of the job that the webhook runs.
      value:
        job_id: "{{ job_id }}"
        access_token: "{{ access_token }}"
        workspace_url: "{{ workspace_url }}"
    - name: model_name
      value: "{{ model_name }}"
      description: |
        If model name is not specified, a registry-wide webhook is created that listens for the specified events across all versions of all registered models.
    - name: status
      value: "{{ status }}"
      description: |
        Enable or disable triggering the webhook, or put the webhook into test mode. The default is \`ACTIVE\`: * \`ACTIVE\`: Webhook is triggered when an associated event happens. * \`DISABLED\`: Webhook is not triggered. * \`TEST_MODE\`: Webhook can be triggered through the test endpoint, but is not triggered on a real event.
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

**NOTE:** This endpoint is in Public Preview. Updates a registry webhook.

```sql
UPDATE databricks_workspace.ml.model_registry_webhooks
SET 
id = '{{ id }}',
description = '{{ description }}',
events = '{{ events }}',
http_url_spec = '{{ http_url_spec }}',
job_spec = '{{ job_spec }}',
status = '{{ status }}'
WHERE 
workspace = '{{ workspace }}' --required
AND id = '{{ id }}' --required
RETURNING
webhook;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'test', value: 'test' }
    ]}
>
<TabItem value="delete">

**NOTE:** This endpoint is in Public Preview. Deletes a registry webhook.

```sql
EXEC databricks_workspace.ml.model_registry_webhooks.delete 
@id='{{ id }}' --required, 
@workspace='{{ workspace }}' --required
;
```
</TabItem>
<TabItem value="test">

**NOTE:** This endpoint is in Public Preview. Tests a registry webhook.

```sql
EXEC databricks_workspace.ml.model_registry_webhooks.test 
@workspace='{{ workspace }}' --required 
@@json=
'{
"id": "{{ id }}", 
"event": "{{ event }}"
}'
;
```
</TabItem>
</Tabs>

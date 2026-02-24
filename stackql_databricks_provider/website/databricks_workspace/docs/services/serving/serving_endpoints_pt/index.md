---
title: serving_endpoints_pt
hide_title: false
hide_table_of_contents: false
keywords:
  - serving_endpoints_pt
  - serving
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

Creates, updates, deletes, gets or lists a <code>serving_endpoints_pt</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="serving_endpoints_pt" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.serving.serving_endpoints_pt" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-config"><code>config</code></a></td>
    <td></td>
    <td>Create a new PT serving endpoint.</td>
</tr>
<tr>
    <td><a href="#update_config"><CopyableCode code="update_config" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-config"><code>config</code></a></td>
    <td></td>
    <td>Updates any combination of the pt endpoint's served entities, the compute configuration of those</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the pt endpoint to update. This field is required.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a new PT serving endpoint.

```sql
INSERT INTO databricks_workspace.serving.serving_endpoints_pt (
name,
config,
ai_gateway,
budget_policy_id,
email_notifications,
tags,
workspace
)
SELECT 
'{{ name }}' /* required */,
'{{ config }}' /* required */,
'{{ ai_gateway }}',
'{{ budget_policy_id }}',
'{{ email_notifications }}',
'{{ tags }}',
'{{ workspace }}'
RETURNING
id,
name,
budget_policy_id,
ai_gateway,
config,
creation_timestamp,
creator,
data_plane_info,
description,
email_notifications,
endpoint_url,
last_updated_timestamp,
pending_config,
permission_level,
route_optimized,
state,
tags,
task
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: serving_endpoints_pt
  props:
    - name: workspace
      value: string
      description: Required parameter for the serving_endpoints_pt resource.
    - name: name
      value: string
      description: |
        The name of the serving endpoint. This field is required and must be unique across a Databricks workspace. An endpoint name can consist of alphanumeric characters, dashes, and underscores.
    - name: config
      value: object
      description: |
        The core config of the serving endpoint.
      props:
      - name: served_entities
        value: array
        props:
        - name: entity_name
          value: string
        - name: provisioned_model_units
          value: integer
          description: |
            The number of model units to be provisioned.
        - name: burst_scaling_enabled
          value: boolean
          description: |
            Whether burst scaling is enabled. When enabled (default), the endpoint can automatically scale up beyond provisioned capacity to handle traffic spikes. When disabled, the endpoint maintains fixed capacity at provisioned_model_units.
        - name: entity_version
          value: string
        - name: name
          value: string
          description: |
            The name of a served entity. It must be unique across an endpoint. A served entity name can consist of alphanumeric characters, dashes, and underscores. If not specified for an external model, this field defaults to external_model.name, with '.' and ':' replaced with '-', and if not specified for other entities, it defaults to entity_name-entity_version.
      - name: traffic_config
        value: object
        props:
        - name: routes
          value: array
          props:
          - name: traffic_percentage
            value: integer
          - name: served_entity_name
            value: string
          - name: served_model_name
            value: string
            description: |
              The name of the served model this route configures traffic for.
    - name: ai_gateway
      value: object
      description: |
        The AI Gateway configuration for the serving endpoint.
      props:
      - name: fallback_config
        value: object
        props:
        - name: enabled
          value: boolean
      - name: guardrails
        value: object
        description: |
          Configuration for AI Guardrails to prevent unwanted data and unsafe data in requests and responses.
        props:
        - name: input
          value: object
          props:
          - name: invalid_keywords
            value: array
            items:
              type: string
          - name: pii
            value: object
            description: |
              Configuration for guardrail PII filter.
            props:
            - name: behavior
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
          - name: safety
            value: boolean
            description: |
              Indicates whether the safety filter is enabled.
          - name: valid_topics
            value: array
            description: |
              The list of allowed topics. Given a chat request, this guardrail flags the request if its topic is not in the allowed topics.
            items:
              type: string
        - name: output
          value: object
          description: |
            Configuration for output guardrail filters.
          props:
          - name: invalid_keywords
            value: array
            items:
              type: string
          - name: pii
            value: object
            description: |
              Configuration for guardrail PII filter.
            props:
            - name: behavior
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
          - name: safety
            value: boolean
            description: |
              Indicates whether the safety filter is enabled.
          - name: valid_topics
            value: array
            description: |
              The list of allowed topics. Given a chat request, this guardrail flags the request if its topic is not in the allowed topics.
            items:
              type: string
      - name: inference_table_config
        value: object
        description: |
          Configuration for payload logging using inference tables. Use these tables to monitor and audit data being sent to and received from model APIs and to improve model quality.
        props:
        - name: catalog_name
          value: string
        - name: enabled
          value: boolean
          description: |
            Indicates whether the inference table is enabled.
        - name: schema_name
          value: string
          description: |
            The name of the schema in Unity Catalog. Required when enabling inference tables. NOTE: On update, you have to disable inference table first in order to change the schema name.
        - name: table_name_prefix
          value: string
          description: |
            The prefix of the table in Unity Catalog. NOTE: On update, you have to disable inference table first in order to change the prefix name.
      - name: rate_limits
        value: array
        description: |
          Configuration for rate limits which can be set to limit endpoint traffic.
        props:
        - name: renewal_period
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
        - name: calls
          value: integer
          description: |
            Used to specify how many calls are allowed for a key within the renewal_period.
        - name: key
          value: string
          description: |
            Key field for a rate limit. Currently, 'user', 'user_group, 'service_principal', and 'endpoint' are supported, with 'endpoint' being the default if not specified.
        - name: principal
          value: string
          description: |
            Principal field for a user, user group, or service principal to apply rate limiting to. Accepts a user email, group name, or service principal application ID.
        - name: tokens
          value: integer
          description: |
            Used to specify how many tokens are allowed for a key within the renewal_period.
      - name: usage_tracking_config
        value: object
        description: |
          Configuration to enable usage tracking using system tables. These tables allow you to monitor operational usage on endpoints and their associated costs.
        props:
        - name: enabled
          value: boolean
    - name: budget_policy_id
      value: string
      description: |
        The budget policy associated with the endpoint.
    - name: email_notifications
      value: object
      description: |
        Email notification settings.
      props:
      - name: on_update_failure
        value: array
        items:
          type: string
      - name: on_update_success
        value: array
        description: |
          A list of email addresses to be notified when an endpoint successfully updates its configuration or state.
        items:
          type: string
    - name: tags
      value: array
      description: |
        Tags to be attached to the serving endpoint and automatically propagated to billing logs.
      props:
      - name: key
        value: string
      - name: value
        value: string
        description: |
          Optional value field for a serving endpoint tag.
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_config"
    values={[
        { label: 'update_config', value: 'update_config' }
    ]}
>
<TabItem value="update_config">

Updates any combination of the pt endpoint's served entities, the compute configuration of those

```sql
REPLACE databricks_workspace.serving.serving_endpoints_pt
SET 
config = '{{ config }}'
WHERE 
name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
AND config = '{{ config }}' --required
RETURNING
id,
name,
budget_policy_id,
ai_gateway,
config,
creation_timestamp,
creator,
data_plane_info,
description,
email_notifications,
endpoint_url,
last_updated_timestamp,
pending_config,
permission_level,
route_optimized,
state,
tags,
task;
```
</TabItem>
</Tabs>

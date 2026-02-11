---
title: serving_endpoint_ai_gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - serving_endpoint_ai_gateway
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

Creates, updates, deletes, gets or lists a <code>serving_endpoint_ai_gateway</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serving_endpoint_ai_gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.serving.serving_endpoint_ai_gateway" /></td></tr>
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
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Used to update the AI Gateway of a serving endpoint. NOTE: External model, provisioned throughput, and<br />pay-per-token endpoints are fully supported; agent endpoints currently only support inference tables.<br /><br />:param name: str<br />  The name of the serving endpoint whose AI Gateway is being updated. This field is required.<br />:param fallback_config: :class:`FallbackConfig` (optional)<br />  Configuration for traffic fallback which auto fallbacks to other served entities if the request to a<br />  served entity fails with certain error codes, to increase availability.<br />:param guardrails: :class:`AiGatewayGuardrails` (optional)<br />  Configuration for AI Guardrails to prevent unwanted data and unsafe data in requests and responses.<br />:param inference_table_config: :class:`AiGatewayInferenceTableConfig` (optional)<br />  Configuration for payload logging using inference tables. Use these tables to monitor and audit data<br />  being sent to and received from model APIs and to improve model quality.<br />:param rate_limits: List[:class:`AiGatewayRateLimit`] (optional)<br />  Configuration for rate limits which can be set to limit endpoint traffic.<br />:param usage_tracking_config: :class:`AiGatewayUsageTrackingConfig` (optional)<br />  Configuration to enable usage tracking using system tables. These tables allow you to monitor<br />  operational usage on endpoints and their associated costs.<br /><br />:returns: :class:`PutAiGatewayResponse`</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the serving endpoint whose AI Gateway is being updated. This field is required.</td>
</tr>
</tbody>
</table>

## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Used to update the AI Gateway of a serving endpoint. NOTE: External model, provisioned throughput, and<br />pay-per-token endpoints are fully supported; agent endpoints currently only support inference tables.<br /><br />:param name: str<br />  The name of the serving endpoint whose AI Gateway is being updated. This field is required.<br />:param fallback_config: :class:`FallbackConfig` (optional)<br />  Configuration for traffic fallback which auto fallbacks to other served entities if the request to a<br />  served entity fails with certain error codes, to increase availability.<br />:param guardrails: :class:`AiGatewayGuardrails` (optional)<br />  Configuration for AI Guardrails to prevent unwanted data and unsafe data in requests and responses.<br />:param inference_table_config: :class:`AiGatewayInferenceTableConfig` (optional)<br />  Configuration for payload logging using inference tables. Use these tables to monitor and audit data<br />  being sent to and received from model APIs and to improve model quality.<br />:param rate_limits: List[:class:`AiGatewayRateLimit`] (optional)<br />  Configuration for rate limits which can be set to limit endpoint traffic.<br />:param usage_tracking_config: :class:`AiGatewayUsageTrackingConfig` (optional)<br />  Configuration to enable usage tracking using system tables. These tables allow you to monitor<br />  operational usage on endpoints and their associated costs.<br /><br />:returns: :class:`PutAiGatewayResponse`

```sql
REPLACE databricks_workspace.serving.serving_endpoint_ai_gateway
SET 
data__fallback_config = '{{ fallback_config }}',
data__guardrails = '{{ guardrails }}',
data__inference_table_config = '{{ inference_table_config }}',
data__rate_limits = '{{ rate_limits }}',
data__usage_tracking_config = '{{ usage_tracking_config }}'
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
fallback_config,
guardrails,
inference_table_config,
rate_limits,
usage_tracking_config;
```
</TabItem>
</Tabs>

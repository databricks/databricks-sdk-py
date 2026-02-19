---
title: feature_kafka_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_kafka_configs
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

Creates, updates, deletes, gets or lists a <code>feature_kafka_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="feature_kafka_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.feature_kafka_configs" /></td></tr>
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
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "auth_config",
    "type": "object",
    "description": "Authentication configuration for connection to topics.",
    "children": [
      {
        "name": "uc_service_credential_name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "backfill_source",
    "type": "object",
    "description": "A user-provided and managed source for backfilling data. Historical data is used when creating a training set from streaming features linked to this Kafka config. In the future, a separate table will be maintained by Databricks for forward filling data. The schema for this source must match exactly that of the key and value schemas specified for this Kafka config.",
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
      }
    ]
  },
  {
    "name": "bootstrap_servers",
    "type": "string",
    "description": "A comma-separated list of host/port pairs pointing to Kafka cluster."
  },
  {
    "name": "extra_options",
    "type": "object",
    "description": "Catch-all for miscellaneous options. Keys should be source options or Kafka consumer options (kafka.*)"
  },
  {
    "name": "key_schema",
    "type": "object",
    "description": "Schema configuration for extracting message keys from topics. At least one of key_schema and value_schema must be provided.",
    "children": [
      {
        "name": "json_schema",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "subscription_mode",
    "type": "object",
    "description": "Options to configure which Kafka topics to pull data from.",
    "children": [
      {
        "name": "assign",
        "type": "string",
        "description": ""
      },
      {
        "name": "subscribe",
        "type": "string",
        "description": "A comma-separated list of Kafka topics to read from. For example, 'topicA,topicB,topicC'."
      },
      {
        "name": "subscribe_pattern",
        "type": "string",
        "description": "A regular expression matching topics to subscribe to. For example, 'topic.*' will subscribe to all topics starting with 'topic'."
      }
    ]
  },
  {
    "name": "value_schema",
    "type": "object",
    "description": "Schema configuration for extracting message values from topics. At least one of key_schema and value_schema must be provided.",
    "children": [
      {
        "name": "json_schema",
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
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "auth_config",
    "type": "object",
    "description": "Authentication configuration for connection to topics.",
    "children": [
      {
        "name": "uc_service_credential_name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "backfill_source",
    "type": "object",
    "description": "A user-provided and managed source for backfilling data. Historical data is used when creating a training set from streaming features linked to this Kafka config. In the future, a separate table will be maintained by Databricks for forward filling data. The schema for this source must match exactly that of the key and value schemas specified for this Kafka config.",
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
      }
    ]
  },
  {
    "name": "bootstrap_servers",
    "type": "string",
    "description": "A comma-separated list of host/port pairs pointing to Kafka cluster."
  },
  {
    "name": "extra_options",
    "type": "object",
    "description": "Catch-all for miscellaneous options. Keys should be source options or Kafka consumer options (kafka.*)"
  },
  {
    "name": "key_schema",
    "type": "object",
    "description": "Schema configuration for extracting message keys from topics. At least one of key_schema and value_schema must be provided.",
    "children": [
      {
        "name": "json_schema",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "subscription_mode",
    "type": "object",
    "description": "Options to configure which Kafka topics to pull data from.",
    "children": [
      {
        "name": "assign",
        "type": "string",
        "description": ""
      },
      {
        "name": "subscribe",
        "type": "string",
        "description": "A comma-separated list of Kafka topics to read from. For example, 'topicA,topicB,topicC'."
      },
      {
        "name": "subscribe_pattern",
        "type": "string",
        "description": "A regular expression matching topics to subscribe to. For example, 'topic.*' will subscribe to all topics starting with 'topic'."
      }
    ]
  },
  {
    "name": "value_schema",
    "type": "object",
    "description": "Schema configuration for extracting message values from topics. At least one of key_schema and value_schema must be provided.",
    "children": [
      {
        "name": "json_schema",
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a Kafka config. During PrPr, Kafka configs can be read and used when creating features under the</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List Kafka configs. During PrPr, Kafka configs can be read and used when creating features under the</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-kafka_config"><code>kafka_config</code></a></td>
    <td></td>
    <td>Create a Kafka config. During PrPr, Kafka configs can be read and used when creating features under</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-kafka_config"><code>kafka_config</code></a></td>
    <td></td>
    <td>Update a Kafka config. During PrPr, Kafka configs can be read and used when creating features under</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a Kafka config. During PrPr, Kafka configs can be read and used when creating features under</td>
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
    <td>Name of the Kafka config to delete.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>The list of fields to update.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
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

Get a Kafka config. During PrPr, Kafka configs can be read and used when creating features under the

```sql
SELECT
name,
auth_config,
backfill_source,
bootstrap_servers,
extra_options,
key_schema,
subscription_mode,
value_schema
FROM databricks_workspace.ml.feature_kafka_configs
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Kafka configs. During PrPr, Kafka configs can be read and used when creating features under the

```sql
SELECT
name,
auth_config,
backfill_source,
bootstrap_servers,
extra_options,
key_schema,
subscription_mode,
value_schema
FROM databricks_workspace.ml.feature_kafka_configs
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

Create a Kafka config. During PrPr, Kafka configs can be read and used when creating features under

```sql
INSERT INTO databricks_workspace.ml.feature_kafka_configs (
kafka_config,
deployment_name
)
SELECT 
'{{ kafka_config }}' /* required */,
'{{ deployment_name }}'
RETURNING
name,
auth_config,
backfill_source,
bootstrap_servers,
extra_options,
key_schema,
subscription_mode,
value_schema
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: feature_kafka_configs
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the feature_kafka_configs resource.
    - name: kafka_config
      value: string
      description: |
        :returns: :class:`KafkaConfig`
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

Update a Kafka config. During PrPr, Kafka configs can be read and used when creating features under

```sql
UPDATE databricks_workspace.ml.feature_kafka_configs
SET 
kafka_config = '{{ kafka_config }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND kafka_config = '{{ kafka_config }}' --required
RETURNING
name,
auth_config,
backfill_source,
bootstrap_servers,
extra_options,
key_schema,
subscription_mode,
value_schema;
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

Delete a Kafka config. During PrPr, Kafka configs can be read and used when creating features under

```sql
DELETE FROM databricks_workspace.ml.feature_kafka_configs
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

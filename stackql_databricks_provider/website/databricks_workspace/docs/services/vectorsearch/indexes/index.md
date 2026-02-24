---
title: indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes
  - vectorsearch
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

Creates, updates, deletes, gets or lists an <code>indexes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="indexes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.vectorsearch.indexes" /></td></tr>
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
    "description": "Name of the index"
  },
  {
    "name": "endpoint_name",
    "type": "string",
    "description": "Name of the endpoint associated with the index"
  },
  {
    "name": "creator",
    "type": "string",
    "description": ""
  },
  {
    "name": "delta_sync_index_spec",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "embedding_source_columns",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "embedding_model_endpoint_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "model_endpoint_name_for_query",
            "type": "string",
            "description": "Name of the embedding model endpoint which, if specified, is used for querying (not ingestion)."
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the column"
          }
        ]
      },
      {
        "name": "embedding_vector_columns",
        "type": "array",
        "description": "The columns that contain the embedding vectors.",
        "children": [
          {
            "name": "embedding_dimension",
            "type": "integer",
            "description": ""
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the column"
          }
        ]
      },
      {
        "name": "embedding_writeback_table",
        "type": "string",
        "description": "[Optional] Name of the Delta table to sync the vector index contents and computed embeddings to."
      },
      {
        "name": "pipeline_id",
        "type": "string",
        "description": "The ID of the pipeline that is used to sync the index."
      },
      {
        "name": "pipeline_type",
        "type": "string",
        "description": "Pipeline execution mode. - `TRIGGERED`: If the pipeline uses the triggered execution mode, the system stops processing after successfully refreshing the source table in the pipeline once, ensuring the table is updated based on the data available when the update started. - `CONTINUOUS`: If the pipeline uses continuous execution, the pipeline processes new data as it arrives in the source table to keep vector index fresh. (CONTINUOUS, TRIGGERED)"
      },
      {
        "name": "source_table",
        "type": "string",
        "description": "The name of the source table."
      }
    ]
  },
  {
    "name": "direct_access_index_spec",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "embedding_source_columns",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "embedding_model_endpoint_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "model_endpoint_name_for_query",
            "type": "string",
            "description": "Name of the embedding model endpoint which, if specified, is used for querying (not ingestion)."
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the column"
          }
        ]
      },
      {
        "name": "embedding_vector_columns",
        "type": "array",
        "description": "The columns that contain the embedding vectors. The format should be array[double].",
        "children": [
          {
            "name": "embedding_dimension",
            "type": "integer",
            "description": ""
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the column"
          }
        ]
      },
      {
        "name": "schema_json",
        "type": "string",
        "description": "The schema of the index in JSON format. Supported types are `integer`, `long`, `float`, `double`, `boolean`, `string`, `date`, `timestamp`. Supported types for vector column: `array<float>`, `array<double>`,`."
      }
    ]
  },
  {
    "name": "index_type",
    "type": "string",
    "description": "There are 2 types of Vector Search indexes: - `DELTA_SYNC`: An index that automatically syncs<br />with a source Delta Table, automatically and incrementally updating the index as the underlying<br />data in the Delta Table changes. - `DIRECT_ACCESS`: An index that supports direct read and write<br />of vectors and metadata through our REST and SDK APIs. With this model, the user manages index<br />updates. (DELTA_SYNC, DIRECT_ACCESS)"
  },
  {
    "name": "primary_key",
    "type": "string",
    "description": "Primary key of the index"
  },
  {
    "name": "status",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "index_url",
        "type": "string",
        "description": ""
      },
      {
        "name": "indexed_row_count",
        "type": "integer",
        "description": "Number of rows indexed"
      },
      {
        "name": "message",
        "type": "string",
        "description": "Message associated with the index status"
      },
      {
        "name": "ready",
        "type": "boolean",
        "description": "Whether the index is ready for search"
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
    "description": "Name of the index"
  },
  {
    "name": "endpoint_name",
    "type": "string",
    "description": "Name of the endpoint associated with the index"
  },
  {
    "name": "creator",
    "type": "string",
    "description": ""
  },
  {
    "name": "index_type",
    "type": "string",
    "description": "There are 2 types of Vector Search indexes: - `DELTA_SYNC`: An index that automatically syncs<br />with a source Delta Table, automatically and incrementally updating the index as the underlying<br />data in the Delta Table changes. - `DIRECT_ACCESS`: An index that supports direct read and write<br />of vectors and metadata through our REST and SDK APIs. With this model, the user manages index<br />updates. (DELTA_SYNC, DIRECT_ACCESS)"
  },
  {
    "name": "primary_key",
    "type": "string",
    "description": "Primary key of the index"
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
    <td><a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-ensure_reranker_compatible"><code>ensure_reranker_compatible</code></a></td>
    <td>Get an index.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List all indexes in the given endpoint.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-primary_key"><code>primary_key</code></a>, <a href="#parameter-index_type"><code>index_type</code></a></td>
    <td></td>
    <td>Create a new index.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Delete an index.</td>
</tr>
<tr>
    <td><a href="#delete_data_vector_index"><CopyableCode code="delete_data_vector_index" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-primary_keys"><code>primary_keys</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Handles the deletion of data from a specified vector index.</td>
</tr>
<tr>
    <td><a href="#query_index"><CopyableCode code="query_index" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-columns"><code>columns</code></a></td>
    <td></td>
    <td>Query the specified vector index.</td>
</tr>
<tr>
    <td><a href="#query_next_page"><CopyableCode code="query_next_page" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Use `next_page_token` returned from previous `QueryVectorIndex` or `QueryVectorIndexNextPage` request</td>
</tr>
<tr>
    <td><a href="#scan_index"><CopyableCode code="scan_index" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Scan the specified vector index and return the first `num_results` entries after the exclusive</td>
</tr>
<tr>
    <td><a href="#sync_index"><CopyableCode code="sync_index" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Triggers a synchronization process for a specified vector index.</td>
</tr>
<tr>
    <td><a href="#upsert_data_vector_index"><CopyableCode code="upsert_data_vector_index" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-inputs_json"><code>inputs_json</code></a></td>
    <td></td>
    <td>Handles the upserting of data into a specified vector index.</td>
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
<tr id="parameter-endpoint_name">
    <td><CopyableCode code="endpoint_name" /></td>
    <td><code>string</code></td>
    <td>Name of the endpoint</td>
</tr>
<tr id="parameter-index_name">
    <td><CopyableCode code="index_name" /></td>
    <td><code>string</code></td>
    <td>Name of the vector index where data is to be upserted. Must be a Direct Vector Access Index.</td>
</tr>
<tr id="parameter-primary_keys">
    <td><CopyableCode code="primary_keys" /></td>
    <td><code>array</code></td>
    <td>List of primary keys for the data to be deleted.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-ensure_reranker_compatible">
    <td><CopyableCode code="ensure_reranker_compatible" /></td>
    <td><code>boolean</code></td>
    <td>If true, the URL returned for the index is guaranteed to be compatible with the reranker. Currently this means we return the CP URL regardless of how the index is being accessed. If not set or set to false, the URL may still be compatible with the reranker depending on what URL we return.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Token for pagination</td>
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

Get an index.

```sql
SELECT
name,
endpoint_name,
creator,
delta_sync_index_spec,
direct_access_index_spec,
index_type,
primary_key,
status
FROM databricks_workspace.vectorsearch.indexes
WHERE index_name = '{{ index_name }}' -- required
AND workspace = '{{ workspace }}' -- required
AND ensure_reranker_compatible = '{{ ensure_reranker_compatible }}'
;
```
</TabItem>
<TabItem value="list">

List all indexes in the given endpoint.

```sql
SELECT
name,
endpoint_name,
creator,
index_type,
primary_key
FROM databricks_workspace.vectorsearch.indexes
WHERE endpoint_name = '{{ endpoint_name }}' -- required
AND workspace = '{{ workspace }}' -- required
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

Create a new index.

```sql
INSERT INTO databricks_workspace.vectorsearch.indexes (
name,
endpoint_name,
primary_key,
index_type,
delta_sync_index_spec,
direct_access_index_spec,
workspace
)
SELECT 
'{{ name }}' /* required */,
'{{ endpoint_name }}' /* required */,
'{{ primary_key }}' /* required */,
'{{ index_type }}' /* required */,
'{{ delta_sync_index_spec }}',
'{{ direct_access_index_spec }}',
'{{ workspace }}'
RETURNING
name,
endpoint_name,
creator,
delta_sync_index_spec,
direct_access_index_spec,
index_type,
primary_key,
status
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: indexes
  props:
    - name: workspace
      value: string
      description: Required parameter for the indexes resource.
    - name: name
      value: string
      description: |
        Name of the index
    - name: endpoint_name
      value: string
      description: |
        Name of the endpoint to be used for serving the index
    - name: primary_key
      value: string
      description: |
        Primary key of the index
    - name: index_type
      value: string
      description: |
        :param delta_sync_index_spec: :class:`DeltaSyncVectorIndexSpecRequest` (optional) Specification for Delta Sync Index. Required if `index_type` is `DELTA_SYNC`.
    - name: delta_sync_index_spec
      value: object
      props:
      - name: columns_to_sync
        value: array
        items:
          type: string
      - name: embedding_source_columns
        value: array
        description: |
          The columns that contain the embedding source.
        props:
        - name: embedding_model_endpoint_name
          value: string
        - name: model_endpoint_name_for_query
          value: string
          description: |
            Name of the embedding model endpoint which, if specified, is used for querying (not ingestion).
        - name: name
          value: string
          description: |
            Name of the column
      - name: embedding_vector_columns
        value: array
        description: |
          The columns that contain the embedding vectors.
        props:
        - name: embedding_dimension
          value: integer
        - name: name
          value: string
          description: |
            Name of the column
      - name: embedding_writeback_table
        value: string
        description: |
          [Optional] Name of the Delta table to sync the vector index contents and computed embeddings to.
      - name: pipeline_type
        value: string
        description: |
          Pipeline execution mode. - `TRIGGERED`: If the pipeline uses the triggered execution mode, the system stops processing after successfully refreshing the source table in the pipeline once, ensuring the table is updated based on the data available when the update started. - `CONTINUOUS`: If the pipeline uses continuous execution, the pipeline processes new data as it arrives in the source table to keep vector index fresh.
      - name: source_table
        value: string
        description: |
          The name of the source table.
    - name: direct_access_index_spec
      value: object
      description: |
        Specification for Direct Vector Access Index. Required if `index_type` is `DIRECT_ACCESS`.
      props:
      - name: embedding_source_columns
        value: array
        props:
        - name: embedding_model_endpoint_name
          value: string
        - name: model_endpoint_name_for_query
          value: string
          description: |
            Name of the embedding model endpoint which, if specified, is used for querying (not ingestion).
        - name: name
          value: string
          description: |
            Name of the column
      - name: embedding_vector_columns
        value: array
        description: |
          The columns that contain the embedding vectors. The format should be array[double].
        props:
        - name: embedding_dimension
          value: integer
        - name: name
          value: string
          description: |
            Name of the column
      - name: schema_json
        value: string
        description: |
          The schema of the index in JSON format. Supported types are `integer`, `long`, `float`, `double`, `boolean`, `string`, `date`, `timestamp`. Supported types for vector column: `array<float>`, `array<double>`,`.
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

Delete an index.

```sql
DELETE FROM databricks_workspace.vectorsearch.indexes
WHERE index_name = '{{ index_name }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="delete_data_vector_index"
    values={[
        { label: 'delete_data_vector_index', value: 'delete_data_vector_index' },
        { label: 'query_index', value: 'query_index' },
        { label: 'query_next_page', value: 'query_next_page' },
        { label: 'scan_index', value: 'scan_index' },
        { label: 'sync_index', value: 'sync_index' },
        { label: 'upsert_data_vector_index', value: 'upsert_data_vector_index' }
    ]}
>
<TabItem value="delete_data_vector_index">

Handles the deletion of data from a specified vector index.

```sql
EXEC databricks_workspace.vectorsearch.indexes.delete_data_vector_index 
@index_name='{{ index_name }}' --required, 
@primary_keys='{{ primary_keys }}' --required, 
@workspace='{{ workspace }}' --required
;
```
</TabItem>
<TabItem value="query_index">

Query the specified vector index.

```sql
EXEC databricks_workspace.vectorsearch.indexes.query_index 
@index_name='{{ index_name }}' --required, 
@workspace='{{ workspace }}' --required 
@@json=
'{
"columns": "{{ columns }}", 
"columns_to_rerank": "{{ columns_to_rerank }}", 
"filters_json": "{{ filters_json }}", 
"num_results": {{ num_results }}, 
"query_text": "{{ query_text }}", 
"query_type": "{{ query_type }}", 
"query_vector": "{{ query_vector }}", 
"reranker": "{{ reranker }}", 
"score_threshold": {{ score_threshold }}
}'
;
```
</TabItem>
<TabItem value="query_next_page">

Use `next_page_token` returned from previous `QueryVectorIndex` or `QueryVectorIndexNextPage` request

```sql
EXEC databricks_workspace.vectorsearch.indexes.query_next_page 
@index_name='{{ index_name }}' --required, 
@workspace='{{ workspace }}' --required 
@@json=
'{
"endpoint_name": "{{ endpoint_name }}", 
"page_token": "{{ page_token }}"
}'
;
```
</TabItem>
<TabItem value="scan_index">

Scan the specified vector index and return the first `num_results` entries after the exclusive

```sql
EXEC databricks_workspace.vectorsearch.indexes.scan_index 
@index_name='{{ index_name }}' --required, 
@workspace='{{ workspace }}' --required 
@@json=
'{
"last_primary_key": "{{ last_primary_key }}", 
"num_results": {{ num_results }}
}'
;
```
</TabItem>
<TabItem value="sync_index">

Triggers a synchronization process for a specified vector index.

```sql
EXEC databricks_workspace.vectorsearch.indexes.sync_index 
@index_name='{{ index_name }}' --required, 
@workspace='{{ workspace }}' --required
;
```
</TabItem>
<TabItem value="upsert_data_vector_index">

Handles the upserting of data into a specified vector index.

```sql
EXEC databricks_workspace.vectorsearch.indexes.upsert_data_vector_index 
@index_name='{{ index_name }}' --required, 
@workspace='{{ workspace }}' --required 
@@json=
'{
"inputs_json": "{{ inputs_json }}"
}'
;
```
</TabItem>
</Tabs>

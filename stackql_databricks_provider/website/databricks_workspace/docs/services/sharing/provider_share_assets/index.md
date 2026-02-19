---
title: provider_share_assets
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_share_assets
  - sharing
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

Creates, updates, deletes, gets or lists a <code>provider_share_assets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="provider_share_assets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sharing.provider_share_assets" /></td></tr>
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
    "name": "functions",
    "type": "array",
    "description": "The list of functions in the share.",
    "children": [
      {
        "name": "aliases",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "alias_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "version_num",
            "type": "integer",
            "description": "Numeric model version that alias will reference."
          }
        ]
      },
      {
        "name": "comment",
        "type": "string",
        "description": "The comment of the function."
      },
      {
        "name": "data_type",
        "type": "string",
        "description": "The data type of the function. (ARRAY, BINARY, BOOLEAN, BYTE, CHAR, DATE, DECIMAL, DOUBLE, FLOAT, INT, INTERVAL, LONG, MAP, NULL, SHORT, STRING, STRUCT, TABLE_TYPE, TIMESTAMP, TIMESTAMP_NTZ, USER_DEFINED_TYPE, VARIANT)"
      },
      {
        "name": "dependency_list",
        "type": "object",
        "description": "The dependency list of the function.",
        "children": [
          {
            "name": "dependencies",
            "type": "array",
            "description": "An array of Dependency.",
            "children": [
              {
                "name": "function",
                "type": "object",
                "description": "A Function in UC as a dependency."
              },
              {
                "name": "table",
                "type": "object",
                "description": "A Table in UC as a dependency."
              }
            ]
          }
        ]
      },
      {
        "name": "full_data_type",
        "type": "string",
        "description": "The full data type of the function."
      },
      {
        "name": "id",
        "type": "string",
        "description": "The id of the function."
      },
      {
        "name": "input_params",
        "type": "object",
        "description": "The function parameter information.",
        "children": [
          {
            "name": "parameters",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "comment",
                "type": "string",
                "description": "The comment of the parameter."
              },
              {
                "name": "name",
                "type": "string",
                "description": "The name of the parameter."
              },
              {
                "name": "parameter_default",
                "type": "string",
                "description": "The default value of the parameter."
              },
              {
                "name": "parameter_mode",
                "type": "string",
                "description": "The mode of the function parameter. (IN, INOUT, OUT)"
              },
              {
                "name": "parameter_type",
                "type": "string",
                "description": "The type of the function parameter. (COLUMN, PARAM)"
              },
              {
                "name": "position",
                "type": "integer",
                "description": "The position of the parameter."
              },
              {
                "name": "type_interval_type",
                "type": "string",
                "description": "The interval type of the parameter type."
              },
              {
                "name": "type_json",
                "type": "string",
                "description": "The type of the parameter in JSON format."
              },
              {
                "name": "type_name",
                "type": "string",
                "description": "The type of the parameter in Enum format. (ARRAY, BINARY, BOOLEAN, BYTE, CHAR, DATE, DECIMAL, DOUBLE, FLOAT, INT, INTERVAL, LONG, MAP, NULL, SHORT, STRING, STRUCT, TABLE_TYPE, TIMESTAMP, TIMESTAMP_NTZ, USER_DEFINED_TYPE, VARIANT)"
              },
              {
                "name": "type_precision",
                "type": "integer",
                "description": "The precision of the parameter type."
              },
              {
                "name": "type_scale",
                "type": "integer",
                "description": "The scale of the parameter type."
              },
              {
                "name": "type_text",
                "type": "string",
                "description": "The type of the parameter in text format."
              }
            ]
          }
        ]
      },
      {
        "name": "name",
        "type": "string",
        "description": "The name of the function."
      },
      {
        "name": "properties",
        "type": "string",
        "description": "The properties of the function."
      },
      {
        "name": "routine_definition",
        "type": "string",
        "description": "The routine definition of the function."
      },
      {
        "name": "schema",
        "type": "string",
        "description": "The name of the schema that the function belongs to."
      },
      {
        "name": "securable_kind",
        "type": "string",
        "description": "The securable kind of the function. (FUNCTION_FEATURE_SPEC, FUNCTION_REGISTERED_MODEL, FUNCTION_STANDARD)"
      },
      {
        "name": "share",
        "type": "string",
        "description": "The name of the share that the function belongs to."
      },
      {
        "name": "share_id",
        "type": "string",
        "description": "The id of the share that the function belongs to."
      },
      {
        "name": "storage_location",
        "type": "string",
        "description": "The storage location of the function."
      },
      {
        "name": "tags",
        "type": "string",
        "description": "The tags of the function."
      }
    ]
  },
  {
    "name": "notebooks",
    "type": "array",
    "description": "The list of notebooks in the share.",
    "children": [
      {
        "name": "comment",
        "type": "string",
        "description": ""
      },
      {
        "name": "id",
        "type": "string",
        "description": "The id of the notebook file."
      },
      {
        "name": "name",
        "type": "string",
        "description": "Name of the notebook file."
      },
      {
        "name": "share",
        "type": "string",
        "description": "The name of the share that the notebook file belongs to."
      },
      {
        "name": "share_id",
        "type": "string",
        "description": "The id of the share that the notebook file belongs to."
      },
      {
        "name": "tags",
        "type": "string",
        "description": "The tags of the notebook file."
      }
    ]
  },
  {
    "name": "share",
    "type": "object",
    "description": "The metadata of the share.",
    "children": [
      {
        "name": "id",
        "type": "string",
        "description": ""
      },
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "tables",
    "type": "array",
    "description": "The list of tables in the share.",
    "children": [
      {
        "name": "comment",
        "type": "string",
        "description": ""
      },
      {
        "name": "id",
        "type": "string",
        "description": "The id of the table."
      },
      {
        "name": "internal_attributes",
        "type": "object",
        "description": "Internal information for D2D sharing that should not be disclosed to external users.",
        "children": [
          {
            "name": "auxiliary_managed_location",
            "type": "string",
            "description": "Managed Delta Metadata location for foreign iceberg tables."
          },
          {
            "name": "dependency_storage_locations",
            "type": "array",
            "description": "Storage locations of all table dependencies for shared views. Used on the recipient side for SEG (Secure Egress Gateway) whitelisting."
          },
          {
            "name": "has_delta_uniform_iceberg",
            "type": "boolean",
            "description": "Whether the table has uniform enabled."
          },
          {
            "name": "parent_storage_location",
            "type": "string",
            "description": "Will be populated in the reconciliation response for VIEW and FOREIGN_TABLE, with the value of the parent UC entity's storage_location, following the same logic as getManagedEntityPath in CreateStagingTableHandler, which is used to store the materialized table for a shared VIEW/FOREIGN_TABLE for D2O queries. The value will be used on the recipient side to be whitelisted when SEG is enabled on the workspace of the recipient, to allow the recipient users to query this shared VIEW/FOREIGN_TABLE."
          },
          {
            "name": "storage_location",
            "type": "string",
            "description": "The cloud storage location of a shard table with DIRECTORY_BASED_TABLE type."
          },
          {
            "name": "type",
            "type": "string",
            "description": "The type of the shared table. (DELTA_ICEBERG_TABLE, DIRECTORY_BASED_TABLE, FILE_BASED_TABLE, FOREIGN_ICEBERG_TABLE, FOREIGN_TABLE, MATERIALIZED_VIEW, METRIC_VIEW, STREAMING_TABLE, VIEW)"
          },
          {
            "name": "view_definition",
            "type": "string",
            "description": "The view definition of a shared view. DEPRECATED."
          }
        ]
      },
      {
        "name": "materialization_namespace",
        "type": "string",
        "description": "The catalog and schema of the materialized table"
      },
      {
        "name": "materialized_table_name",
        "type": "string",
        "description": "The name of a materialized table."
      },
      {
        "name": "name",
        "type": "string",
        "description": "The name of the table."
      },
      {
        "name": "schema",
        "type": "string",
        "description": "The name of the schema that the table belongs to."
      },
      {
        "name": "share",
        "type": "string",
        "description": "The name of the share that the table belongs to."
      },
      {
        "name": "share_id",
        "type": "string",
        "description": "The id of the share that the table belongs to."
      },
      {
        "name": "tags",
        "type": "string",
        "description": "The Tags of the table."
      }
    ]
  },
  {
    "name": "volumes",
    "type": "array",
    "description": "The list of volumes in the share.",
    "children": [
      {
        "name": "comment",
        "type": "string",
        "description": ""
      },
      {
        "name": "id",
        "type": "string",
        "description": "This id maps to the shared_volume_id in database Recipient needs shared_volume_id for recon to check if this volume is already in recipient's DB or not."
      },
      {
        "name": "internal_attributes",
        "type": "object",
        "description": "Internal attributes for D2D sharing that should not be disclosed to external users.",
        "children": [
          {
            "name": "storage_location",
            "type": "string",
            "description": "The cloud storage location of the volume"
          },
          {
            "name": "type",
            "type": "string",
            "description": "The type of the shared volume."
          }
        ]
      },
      {
        "name": "name",
        "type": "string",
        "description": "The name of the volume."
      },
      {
        "name": "schema",
        "type": "string",
        "description": "The name of the schema that the volume belongs to."
      },
      {
        "name": "share",
        "type": "string",
        "description": "The name of the share that the volume belongs to."
      },
      {
        "name": "share_id",
        "type": "string",
        "description": "/ The id of the share that the volume belongs to."
      },
      {
        "name": "tags",
        "type": "string",
        "description": "The tags of the volume."
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-function_max_results"><code>function_max_results</code></a>, <a href="#parameter-notebook_max_results"><code>notebook_max_results</code></a>, <a href="#parameter-table_max_results"><code>table_max_results</code></a>, <a href="#parameter-volume_max_results"><code>volume_max_results</code></a></td>
    <td>Get arrays of assets associated with a specified provider's share. The caller is the recipient of the</td>
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
<tr id="parameter-provider_name">
    <td><CopyableCode code="provider_name" /></td>
    <td><code>string</code></td>
    <td>The name of the provider who owns the share.</td>
</tr>
<tr id="parameter-share_name">
    <td><CopyableCode code="share_name" /></td>
    <td><code>string</code></td>
    <td>The name of the share.</td>
</tr>
<tr id="parameter-function_max_results">
    <td><CopyableCode code="function_max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of functions to return.</td>
</tr>
<tr id="parameter-notebook_max_results">
    <td><CopyableCode code="notebook_max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of notebooks to return.</td>
</tr>
<tr id="parameter-table_max_results">
    <td><CopyableCode code="table_max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of tables to return.</td>
</tr>
<tr id="parameter-volume_max_results">
    <td><CopyableCode code="volume_max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of volumes to return.</td>
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

Get arrays of assets associated with a specified provider's share. The caller is the recipient of the

```sql
SELECT
functions,
notebooks,
share,
tables,
volumes
FROM databricks_workspace.sharing.provider_share_assets
WHERE provider_name = '{{ provider_name }}' -- required
AND share_name = '{{ share_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND function_max_results = '{{ function_max_results }}'
AND notebook_max_results = '{{ notebook_max_results }}'
AND table_max_results = '{{ table_max_results }}'
AND volume_max_results = '{{ volume_max_results }}'
;
```
</TabItem>
</Tabs>

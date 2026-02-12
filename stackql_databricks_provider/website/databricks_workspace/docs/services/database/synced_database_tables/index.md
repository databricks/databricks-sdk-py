---
title: synced_database_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - synced_database_tables
  - database
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

Creates, updates, deletes, gets or lists a <code>synced_database_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>synced_database_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.database.synced_database_tables" /></td></tr>
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
    "description": "Full three-part (catalog, schema, table) name of the table."
  },
  {
    "name": "database_instance_name",
    "type": "string",
    "description": "Name of the target database instance. This is required when creating synced database tables in standard catalogs. This is optional when creating synced database tables in registered catalogs. If this field is specified when creating synced database tables in registered catalogs, the database instance name MUST match that of the registered catalog (or the request will be rejected)."
  },
  {
    "name": "effective_database_instance_name",
    "type": "string",
    "description": "The name of the database instance that this table is registered to. This field is always returned, and for tables inside database catalogs is inferred database instance associated with the catalog. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_logical_database_name",
    "type": "string",
    "description": "The name of the logical database that this table is registered to. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "logical_database_name",
    "type": "string",
    "description": "Target Postgres database object (logical database) name for this table. When creating a synced table in a registered Postgres catalog, the target Postgres database name is inferred to be that of the registered catalog. If this field is specified in this scenario, the Postgres database name MUST match that of the registered catalog (or the request will be rejected). When creating a synced table in a standard catalog, this field is required. In this scenario, specifying this field will allow targeting an arbitrary postgres database. Note that this has implications for the `create_database_objects_is_missing` field in `spec`."
  },
  {
    "name": "data_synchronization_status",
    "type": "object",
    "description": "Synced Table data synchronization status",
    "children": [
      {
        "name": "continuous_update_status",
        "type": "object",
        "description": "Detailed status of a synced table. Shown if the synced table is in the SYNCED_CONTINUOUS_UPDATE<br />    or the SYNCED_UPDATING_PIPELINE_RESOURCES state.",
        "children": [
          {
            "name": "initial_pipeline_sync_progress",
            "type": "object",
            "description": "Progress of the initial data synchronization.",
            "children": [
              {
                "name": "estimated_completion_time_seconds",
                "type": "number",
                "description": "The estimated time remaining to complete this update in seconds."
              },
              {
                "name": "latest_version_currently_processing",
                "type": "integer",
                "description": "The source table Delta version that was last processed by the pipeline. The pipeline may not have completely processed this version yet."
              },
              {
                "name": "provisioning_phase",
                "type": "string",
                "description": "The current phase of the data synchronization pipeline."
              },
              {
                "name": "sync_progress_completion",
                "type": "number",
                "description": "The completion ratio of this update. This is a number between 0 and 1."
              },
              {
                "name": "synced_row_count",
                "type": "integer",
                "description": "The number of rows that have been synced in this update."
              },
              {
                "name": "total_row_count",
                "type": "integer",
                "description": "The total number of rows that need to be synced in this update. This number may be an estimate."
              }
            ]
          },
          {
            "name": "last_processed_commit_version",
            "type": "integer",
            "description": "The last source table Delta version that was successfully synced to the synced table."
          },
          {
            "name": "timestamp",
            "type": "string",
            "description": "The end timestamp of the last time any data was synchronized from the source table to the synced table. This is when the data is available in the synced table."
          }
        ]
      },
      {
        "name": "detailed_state",
        "type": "string",
        "description": "The state of the synced table."
      },
      {
        "name": "failed_status",
        "type": "object",
        "description": "Detailed status of a synced table. Shown if the synced table is in the OFFLINE_FAILED or the<br />    SYNCED_PIPELINE_FAILED state.",
        "children": [
          {
            "name": "last_processed_commit_version",
            "type": "integer",
            "description": "The last source table Delta version that was successfully synced to the synced table. The last source table Delta version that was synced to the synced table. Only populated if the table is still synced and available for serving."
          },
          {
            "name": "timestamp",
            "type": "string",
            "description": "The end timestamp of the last time any data was synchronized from the source table to the synced table. Only populated if the table is still synced and available for serving."
          }
        ]
      },
      {
        "name": "last_sync",
        "type": "object",
        "description": "Summary of the last successful synchronization from source to destination. Will always be present if there has been a successful sync. Even if the most recent syncs have failed. Limitation: The only exception is if the synced table is doing a FULL REFRESH, then the last sync information will not be available until the full refresh is complete. This limitation will be addressed in a future version. This top-level field is a convenience for consumers who want easy access to last sync information without having to traverse detailed_status.",
        "children": [
          {
            "name": "delta_table_sync_info",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "delta_commit_timestamp",
                "type": "string",
                "description": ""
              },
              {
                "name": "delta_commit_version",
                "type": "integer",
                "description": "The Delta Lake commit version that was last successfully synced."
              }
            ]
          },
          {
            "name": "sync_end_timestamp",
            "type": "string",
            "description": "The end timestamp of the most recent successful synchronization. This is the time when the data is available in the synced table."
          },
          {
            "name": "sync_start_timestamp",
            "type": "string",
            "description": "The starting timestamp of the most recent successful synchronization from the source table to the destination (synced) table. Note this is the starting timestamp of the sync operation, not the end time. E.g., for a batch, this is the time when the sync operation started."
          }
        ]
      },
      {
        "name": "message",
        "type": "string",
        "description": "A text description of the current state of the synced table."
      },
      {
        "name": "pipeline_id",
        "type": "string",
        "description": "ID of the associated pipeline. The pipeline ID may have been provided by the client (in the case of bin packing), or generated by the server (when creating a new pipeline)."
      },
      {
        "name": "provisioning_status",
        "type": "object",
        "description": "Detailed status of a synced table. Shown if the synced table is in the<br />    PROVISIONING_PIPELINE_RESOURCES or the PROVISIONING_INITIAL_SNAPSHOT state.",
        "children": [
          {
            "name": "initial_pipeline_sync_progress",
            "type": "object",
            "description": "Details about initial data synchronization. Only populated when in the PROVISIONING_INITIAL_SNAPSHOT state.",
            "children": [
              {
                "name": "estimated_completion_time_seconds",
                "type": "number",
                "description": "The estimated time remaining to complete this update in seconds."
              },
              {
                "name": "latest_version_currently_processing",
                "type": "integer",
                "description": "The source table Delta version that was last processed by the pipeline. The pipeline may not have completely processed this version yet."
              },
              {
                "name": "provisioning_phase",
                "type": "string",
                "description": "The current phase of the data synchronization pipeline."
              },
              {
                "name": "sync_progress_completion",
                "type": "number",
                "description": "The completion ratio of this update. This is a number between 0 and 1."
              },
              {
                "name": "synced_row_count",
                "type": "integer",
                "description": "The number of rows that have been synced in this update."
              },
              {
                "name": "total_row_count",
                "type": "integer",
                "description": "The total number of rows that need to be synced in this update. This number may be an estimate."
              }
            ]
          }
        ]
      },
      {
        "name": "triggered_update_status",
        "type": "object",
        "description": "Detailed status of a synced table. Shown if the synced table is in the SYNCED_TRIGGERED_UPDATE<br />    or the SYNCED_NO_PENDING_UPDATE state.",
        "children": [
          {
            "name": "last_processed_commit_version",
            "type": "integer",
            "description": "The last source table Delta version that was successfully synced to the synced table."
          },
          {
            "name": "timestamp",
            "type": "string",
            "description": "The end timestamp of the last time any data was synchronized from the source table to the synced table. This is when the data is available in the synced table."
          },
          {
            "name": "triggered_update_progress",
            "type": "object",
            "description": "Progress of the active data synchronization pipeline.",
            "children": [
              {
                "name": "estimated_completion_time_seconds",
                "type": "number",
                "description": "The estimated time remaining to complete this update in seconds."
              },
              {
                "name": "latest_version_currently_processing",
                "type": "integer",
                "description": "The source table Delta version that was last processed by the pipeline. The pipeline may not have completely processed this version yet."
              },
              {
                "name": "provisioning_phase",
                "type": "string",
                "description": "The current phase of the data synchronization pipeline."
              },
              {
                "name": "sync_progress_completion",
                "type": "number",
                "description": "The completion ratio of this update. This is a number between 0 and 1."
              },
              {
                "name": "synced_row_count",
                "type": "integer",
                "description": "The number of rows that have been synced in this update."
              },
              {
                "name": "total_row_count",
                "type": "integer",
                "description": "The total number of rows that need to be synced in this update. This number may be an estimate."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "spec",
    "type": "object",
    "description": "Specification of a synced database table.",
    "children": [
      {
        "name": "create_database_objects_if_missing",
        "type": "boolean",
        "description": "If true, the synced table's logical database and schema resources in PG will be created if they do not already exist."
      },
      {
        "name": "existing_pipeline_id",
        "type": "string",
        "description": "At most one of existing_pipeline_id and new_pipeline_spec should be defined. If existing_pipeline_id is defined, the synced table will be bin packed into the existing pipeline referenced. This avoids creating a new pipeline and allows sharing existing compute. In this case, the scheduling_policy of this synced table must match the scheduling policy of the existing pipeline."
      },
      {
        "name": "new_pipeline_spec",
        "type": "object",
        "description": "At most one of existing_pipeline_id and new_pipeline_spec should be defined. If new_pipeline_spec is defined, a new pipeline is created for this synced table. The location pointed to is used to store intermediate files (checkpoints, event logs etc). The caller must have write permissions to create Delta tables in the specified catalog and schema. Again, note this requires write permissions, whereas the source table only requires read permissions.",
        "children": [
          {
            "name": "budget_policy_id",
            "type": "string",
            "description": "Budget policy to set on the newly created pipeline."
          },
          {
            "name": "storage_catalog",
            "type": "string",
            "description": "This field needs to be specified if the destination catalog is a managed postgres catalog. UC catalog for the pipeline to store intermediate files (checkpoints, event logs etc). This needs to be a standard catalog where the user has permissions to create Delta tables."
          },
          {
            "name": "storage_schema",
            "type": "string",
            "description": "This field needs to be specified if the destination catalog is a managed postgres catalog. UC schema for the pipeline to store intermediate files (checkpoints, event logs etc). This needs to be in the standard catalog where the user has permissions to create Delta tables."
          }
        ]
      },
      {
        "name": "primary_key_columns",
        "type": "array",
        "description": "Primary Key columns to be used for data insert/update in the destination."
      },
      {
        "name": "scheduling_policy",
        "type": "string",
        "description": "Scheduling policy of the underlying pipeline."
      },
      {
        "name": "source_table_full_name",
        "type": "string",
        "description": "Three-part (catalog, schema, table) name of the source Delta table."
      },
      {
        "name": "timeseries_key",
        "type": "string",
        "description": "Time series key to deduplicate (tie-break) rows with the same primary key."
      }
    ]
  },
  {
    "name": "unity_catalog_provisioning_state",
    "type": "string",
    "description": "The provisioning state of the synced table entity in Unity Catalog. This is distinct from the state of the data synchronization pipeline (i.e. the table may be in \"ACTIVE\" but the pipeline may be in \"PROVISIONING\" as it runs asynchronously)."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Full three-part (catalog, schema, table) name of the table."
  },
  {
    "name": "database_instance_name",
    "type": "string",
    "description": "Name of the target database instance. This is required when creating synced database tables in standard catalogs. This is optional when creating synced database tables in registered catalogs. If this field is specified when creating synced database tables in registered catalogs, the database instance name MUST match that of the registered catalog (or the request will be rejected)."
  },
  {
    "name": "effective_database_instance_name",
    "type": "string",
    "description": "The name of the database instance that this table is registered to. This field is always returned, and for tables inside database catalogs is inferred database instance associated with the catalog. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_logical_database_name",
    "type": "string",
    "description": "The name of the logical database that this table is registered to. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "logical_database_name",
    "type": "string",
    "description": "Target Postgres database object (logical database) name for this table. When creating a synced table in a registered Postgres catalog, the target Postgres database name is inferred to be that of the registered catalog. If this field is specified in this scenario, the Postgres database name MUST match that of the registered catalog (or the request will be rejected). When creating a synced table in a standard catalog, this field is required. In this scenario, specifying this field will allow targeting an arbitrary postgres database. Note that this has implications for the `create_database_objects_is_missing` field in `spec`."
  },
  {
    "name": "data_synchronization_status",
    "type": "object",
    "description": "Synced Table data synchronization status",
    "children": [
      {
        "name": "continuous_update_status",
        "type": "object",
        "description": "Detailed status of a synced table. Shown if the synced table is in the SYNCED_CONTINUOUS_UPDATE<br />    or the SYNCED_UPDATING_PIPELINE_RESOURCES state.",
        "children": [
          {
            "name": "initial_pipeline_sync_progress",
            "type": "object",
            "description": "Progress of the initial data synchronization.",
            "children": [
              {
                "name": "estimated_completion_time_seconds",
                "type": "number",
                "description": "The estimated time remaining to complete this update in seconds."
              },
              {
                "name": "latest_version_currently_processing",
                "type": "integer",
                "description": "The source table Delta version that was last processed by the pipeline. The pipeline may not have completely processed this version yet."
              },
              {
                "name": "provisioning_phase",
                "type": "string",
                "description": "The current phase of the data synchronization pipeline."
              },
              {
                "name": "sync_progress_completion",
                "type": "number",
                "description": "The completion ratio of this update. This is a number between 0 and 1."
              },
              {
                "name": "synced_row_count",
                "type": "integer",
                "description": "The number of rows that have been synced in this update."
              },
              {
                "name": "total_row_count",
                "type": "integer",
                "description": "The total number of rows that need to be synced in this update. This number may be an estimate."
              }
            ]
          },
          {
            "name": "last_processed_commit_version",
            "type": "integer",
            "description": "The last source table Delta version that was successfully synced to the synced table."
          },
          {
            "name": "timestamp",
            "type": "string",
            "description": "The end timestamp of the last time any data was synchronized from the source table to the synced table. This is when the data is available in the synced table."
          }
        ]
      },
      {
        "name": "detailed_state",
        "type": "string",
        "description": "The state of the synced table."
      },
      {
        "name": "failed_status",
        "type": "object",
        "description": "Detailed status of a synced table. Shown if the synced table is in the OFFLINE_FAILED or the<br />    SYNCED_PIPELINE_FAILED state.",
        "children": [
          {
            "name": "last_processed_commit_version",
            "type": "integer",
            "description": "The last source table Delta version that was successfully synced to the synced table. The last source table Delta version that was synced to the synced table. Only populated if the table is still synced and available for serving."
          },
          {
            "name": "timestamp",
            "type": "string",
            "description": "The end timestamp of the last time any data was synchronized from the source table to the synced table. Only populated if the table is still synced and available for serving."
          }
        ]
      },
      {
        "name": "last_sync",
        "type": "object",
        "description": "Summary of the last successful synchronization from source to destination. Will always be present if there has been a successful sync. Even if the most recent syncs have failed. Limitation: The only exception is if the synced table is doing a FULL REFRESH, then the last sync information will not be available until the full refresh is complete. This limitation will be addressed in a future version. This top-level field is a convenience for consumers who want easy access to last sync information without having to traverse detailed_status.",
        "children": [
          {
            "name": "delta_table_sync_info",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "delta_commit_timestamp",
                "type": "string",
                "description": ""
              },
              {
                "name": "delta_commit_version",
                "type": "integer",
                "description": "The Delta Lake commit version that was last successfully synced."
              }
            ]
          },
          {
            "name": "sync_end_timestamp",
            "type": "string",
            "description": "The end timestamp of the most recent successful synchronization. This is the time when the data is available in the synced table."
          },
          {
            "name": "sync_start_timestamp",
            "type": "string",
            "description": "The starting timestamp of the most recent successful synchronization from the source table to the destination (synced) table. Note this is the starting timestamp of the sync operation, not the end time. E.g., for a batch, this is the time when the sync operation started."
          }
        ]
      },
      {
        "name": "message",
        "type": "string",
        "description": "A text description of the current state of the synced table."
      },
      {
        "name": "pipeline_id",
        "type": "string",
        "description": "ID of the associated pipeline. The pipeline ID may have been provided by the client (in the case of bin packing), or generated by the server (when creating a new pipeline)."
      },
      {
        "name": "provisioning_status",
        "type": "object",
        "description": "Detailed status of a synced table. Shown if the synced table is in the<br />    PROVISIONING_PIPELINE_RESOURCES or the PROVISIONING_INITIAL_SNAPSHOT state.",
        "children": [
          {
            "name": "initial_pipeline_sync_progress",
            "type": "object",
            "description": "Details about initial data synchronization. Only populated when in the PROVISIONING_INITIAL_SNAPSHOT state.",
            "children": [
              {
                "name": "estimated_completion_time_seconds",
                "type": "number",
                "description": "The estimated time remaining to complete this update in seconds."
              },
              {
                "name": "latest_version_currently_processing",
                "type": "integer",
                "description": "The source table Delta version that was last processed by the pipeline. The pipeline may not have completely processed this version yet."
              },
              {
                "name": "provisioning_phase",
                "type": "string",
                "description": "The current phase of the data synchronization pipeline."
              },
              {
                "name": "sync_progress_completion",
                "type": "number",
                "description": "The completion ratio of this update. This is a number between 0 and 1."
              },
              {
                "name": "synced_row_count",
                "type": "integer",
                "description": "The number of rows that have been synced in this update."
              },
              {
                "name": "total_row_count",
                "type": "integer",
                "description": "The total number of rows that need to be synced in this update. This number may be an estimate."
              }
            ]
          }
        ]
      },
      {
        "name": "triggered_update_status",
        "type": "object",
        "description": "Detailed status of a synced table. Shown if the synced table is in the SYNCED_TRIGGERED_UPDATE<br />    or the SYNCED_NO_PENDING_UPDATE state.",
        "children": [
          {
            "name": "last_processed_commit_version",
            "type": "integer",
            "description": "The last source table Delta version that was successfully synced to the synced table."
          },
          {
            "name": "timestamp",
            "type": "string",
            "description": "The end timestamp of the last time any data was synchronized from the source table to the synced table. This is when the data is available in the synced table."
          },
          {
            "name": "triggered_update_progress",
            "type": "object",
            "description": "Progress of the active data synchronization pipeline.",
            "children": [
              {
                "name": "estimated_completion_time_seconds",
                "type": "number",
                "description": "The estimated time remaining to complete this update in seconds."
              },
              {
                "name": "latest_version_currently_processing",
                "type": "integer",
                "description": "The source table Delta version that was last processed by the pipeline. The pipeline may not have completely processed this version yet."
              },
              {
                "name": "provisioning_phase",
                "type": "string",
                "description": "The current phase of the data synchronization pipeline."
              },
              {
                "name": "sync_progress_completion",
                "type": "number",
                "description": "The completion ratio of this update. This is a number between 0 and 1."
              },
              {
                "name": "synced_row_count",
                "type": "integer",
                "description": "The number of rows that have been synced in this update."
              },
              {
                "name": "total_row_count",
                "type": "integer",
                "description": "The total number of rows that need to be synced in this update. This number may be an estimate."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "spec",
    "type": "object",
    "description": "Specification of a synced database table.",
    "children": [
      {
        "name": "create_database_objects_if_missing",
        "type": "boolean",
        "description": "If true, the synced table's logical database and schema resources in PG will be created if they do not already exist."
      },
      {
        "name": "existing_pipeline_id",
        "type": "string",
        "description": "At most one of existing_pipeline_id and new_pipeline_spec should be defined. If existing_pipeline_id is defined, the synced table will be bin packed into the existing pipeline referenced. This avoids creating a new pipeline and allows sharing existing compute. In this case, the scheduling_policy of this synced table must match the scheduling policy of the existing pipeline."
      },
      {
        "name": "new_pipeline_spec",
        "type": "object",
        "description": "At most one of existing_pipeline_id and new_pipeline_spec should be defined. If new_pipeline_spec is defined, a new pipeline is created for this synced table. The location pointed to is used to store intermediate files (checkpoints, event logs etc). The caller must have write permissions to create Delta tables in the specified catalog and schema. Again, note this requires write permissions, whereas the source table only requires read permissions.",
        "children": [
          {
            "name": "budget_policy_id",
            "type": "string",
            "description": "Budget policy to set on the newly created pipeline."
          },
          {
            "name": "storage_catalog",
            "type": "string",
            "description": "This field needs to be specified if the destination catalog is a managed postgres catalog. UC catalog for the pipeline to store intermediate files (checkpoints, event logs etc). This needs to be a standard catalog where the user has permissions to create Delta tables."
          },
          {
            "name": "storage_schema",
            "type": "string",
            "description": "This field needs to be specified if the destination catalog is a managed postgres catalog. UC schema for the pipeline to store intermediate files (checkpoints, event logs etc). This needs to be in the standard catalog where the user has permissions to create Delta tables."
          }
        ]
      },
      {
        "name": "primary_key_columns",
        "type": "array",
        "description": "Primary Key columns to be used for data insert/update in the destination."
      },
      {
        "name": "scheduling_policy",
        "type": "string",
        "description": "Scheduling policy of the underlying pipeline."
      },
      {
        "name": "source_table_full_name",
        "type": "string",
        "description": "Three-part (catalog, schema, table) name of the source Delta table."
      },
      {
        "name": "timeseries_key",
        "type": "string",
        "description": "Time series key to deduplicate (tie-break) rows with the same primary key."
      }
    ]
  },
  {
    "name": "unity_catalog_provisioning_state",
    "type": "string",
    "description": "The provisioning state of the synced table entity in Unity Catalog. This is distinct from the state of the data synchronization pipeline (i.e. the table may be in \"ACTIVE\" but the pipeline may be in \"PROVISIONING\" as it runs asynchronously)."
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
    <td>Get a Synced Database Table.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>This API is currently unimplemented, but exposed for Terraform support.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__synced_table"><code>data__synced_table</code></a></td>
    <td></td>
    <td>Create a Synced Database Table.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__synced_table"><code>data__synced_table</code></a></td>
    <td></td>
    <td>This API is currently unimplemented, but exposed for Terraform support.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-purge_data"><code>purge_data</code></a></td>
    <td>Delete a Synced Database Table.</td>
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
<tr id="parameter-instance_name">
    <td><CopyableCode code="instance_name" /></td>
    <td><code>string</code></td>
    <td>Name of the instance to get synced tables for.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>:param purge_data: bool (optional) Optional. When set to true, the actual PostgreSQL table will be dropped from the database.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>The list of fields to update. Setting this field is not yet supported.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>Upper bound for items returned.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page of synced database tables. Requests first page if absent.</td>
</tr>
<tr id="parameter-purge_data">
    <td><CopyableCode code="purge_data" /></td>
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

Get a Synced Database Table.

```sql
SELECT
name,
database_instance_name,
effective_database_instance_name,
effective_logical_database_name,
logical_database_name,
data_synchronization_status,
spec,
unity_catalog_provisioning_state
FROM databricks_workspace.database.synced_database_tables
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

This API is currently unimplemented, but exposed for Terraform support.

```sql
SELECT
name,
database_instance_name,
effective_database_instance_name,
effective_logical_database_name,
logical_database_name,
data_synchronization_status,
spec,
unity_catalog_provisioning_state
FROM databricks_workspace.database.synced_database_tables
WHERE instance_name = '{{ instance_name }}' -- required
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

Create a Synced Database Table.

```sql
INSERT INTO databricks_workspace.database.synced_database_tables (
data__synced_table,
deployment_name
)
SELECT 
'{{ synced_table }}' /* required */,
'{{ deployment_name }}'
RETURNING
name,
database_instance_name,
effective_database_instance_name,
effective_logical_database_name,
logical_database_name,
data_synchronization_status,
spec,
unity_catalog_provisioning_state
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: synced_database_tables
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the synced_database_tables resource.
    - name: synced_table
      value: string
      description: |
        :returns: :class:`SyncedDatabaseTable`
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

This API is currently unimplemented, but exposed for Terraform support.

```sql
UPDATE databricks_workspace.database.synced_database_tables
SET 
data__synced_table = '{{ synced_table }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__synced_table = '{{ synced_table }}' --required
RETURNING
name,
database_instance_name,
effective_database_instance_name,
effective_logical_database_name,
logical_database_name,
data_synchronization_status,
spec,
unity_catalog_provisioning_state;
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

Delete a Synced Database Table.

```sql
DELETE FROM databricks_workspace.database.synced_database_tables
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND purge_data = '{{ purge_data }}'
;
```
</TabItem>
</Tabs>

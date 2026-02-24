---
title: database_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - database_instances
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

Creates, updates, deletes, gets or lists a <code>database_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="database_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.database.database_instances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'find_by_uid', value: 'find_by_uid' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the instance. This is the unique identifier for the instance."
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": "The policy that is applied to the instance. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": "The desired usage policy to associate with the instance."
  },
  {
    "name": "capacity",
    "type": "string",
    "description": "The sku of the instance. Valid values are \"CU_1\", \"CU_2\", \"CU_4\", \"CU_8\"."
  },
  {
    "name": "child_instance_refs",
    "type": "array",
    "description": "The refs of the child instances. This is only available if the instance is parent instance.",
    "children": [
      {
        "name": "branch_time",
        "type": "string",
        "description": "Branch time of the ref database instance. For a parent ref instance, this is the point in time on the parent instance from which the instance was created. For a child ref instance, this is the point in time on the instance from which the child instance was created. Input: For specifying the point in time to create a child instance. Optional. Output: Only populated if provided as input to create a child instance."
      },
      {
        "name": "effective_lsn",
        "type": "string",
        "description": "For a parent ref instance, this is the LSN on the parent instance from which the instance was created. For a child ref instance, this is the LSN on the instance from which the child instance was created. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
      },
      {
        "name": "lsn",
        "type": "string",
        "description": "User-specified WAL LSN of the ref database instance. Input: For specifying the WAL LSN to create a child instance. Optional. Output: Only populated if provided as input to create a child instance."
      },
      {
        "name": "name",
        "type": "string",
        "description": "Name of the ref database instance."
      },
      {
        "name": "uid",
        "type": "string",
        "description": "Id of the ref database instance."
      }
    ]
  },
  {
    "name": "creation_time",
    "type": "string",
    "description": "The timestamp when the instance was created."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the creator of the instance."
  },
  {
    "name": "custom_tags",
    "type": "array",
    "description": "Custom tags associated with the instance. This field is only included on create and update responses.",
    "children": [
      {
        "name": "key",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": "The value of the custom tag."
      }
    ]
  },
  {
    "name": "effective_capacity",
    "type": "string",
    "description": "Deprecated. The sku of the instance; this field will always match the value of capacity. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_custom_tags",
    "type": "array",
    "description": "The recorded custom tags associated with the instance. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.",
    "children": [
      {
        "name": "key",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": "The value of the custom tag."
      }
    ]
  },
  {
    "name": "effective_enable_pg_native_login",
    "type": "boolean",
    "description": "Whether the instance has PG native password login enabled. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_enable_readable_secondaries",
    "type": "boolean",
    "description": "Whether secondaries serving read-only traffic are enabled. Defaults to false. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_node_count",
    "type": "integer",
    "description": "The number of nodes in the instance, composed of 1 primary and 0 or more secondaries. Defaults to 1 primary and 0 secondaries. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_retention_window_in_days",
    "type": "integer",
    "description": "The retention window for the instance. This is the time window in days for which the historical data is retained. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_stopped",
    "type": "boolean",
    "description": "Whether the instance is stopped. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "enable_pg_native_login",
    "type": "boolean",
    "description": "Whether to enable PG native password login on the instance. Defaults to false."
  },
  {
    "name": "enable_readable_secondaries",
    "type": "boolean",
    "description": "Whether to enable secondaries to serve read-only traffic. Defaults to false."
  },
  {
    "name": "node_count",
    "type": "integer",
    "description": "The number of nodes in the instance, composed of 1 primary and 0 or more secondaries. Defaults to 1 primary and 0 secondaries. This field is input only, see effective_node_count for the output."
  },
  {
    "name": "parent_instance_ref",
    "type": "object",
    "description": "DatabaseInstanceRef is a reference to a database instance. It is used in the DatabaseInstance<br />    object to refer to the parent instance of an instance and to refer the child instances of an<br />    instance. To specify as a parent instance during creation of an instance, the lsn and<br />    branch_time fields are optional. If not specified, the child instance will be created from the<br />    latest lsn of the parent. If both lsn and branch_time are specified, the lsn will be used to<br />    create the child instance.",
    "children": [
      {
        "name": "branch_time",
        "type": "string",
        "description": "Branch time of the ref database instance. For a parent ref instance, this is the point in time on the parent instance from which the instance was created. For a child ref instance, this is the point in time on the instance from which the child instance was created. Input: For specifying the point in time to create a child instance. Optional. Output: Only populated if provided as input to create a child instance."
      },
      {
        "name": "effective_lsn",
        "type": "string",
        "description": "For a parent ref instance, this is the LSN on the parent instance from which the instance was created. For a child ref instance, this is the LSN on the instance from which the child instance was created. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
      },
      {
        "name": "lsn",
        "type": "string",
        "description": "User-specified WAL LSN of the ref database instance. Input: For specifying the WAL LSN to create a child instance. Optional. Output: Only populated if provided as input to create a child instance."
      },
      {
        "name": "name",
        "type": "string",
        "description": "Name of the ref database instance."
      },
      {
        "name": "uid",
        "type": "string",
        "description": "Id of the ref database instance."
      }
    ]
  },
  {
    "name": "pg_version",
    "type": "string",
    "description": "The version of Postgres running on the instance."
  },
  {
    "name": "read_only_dns",
    "type": "string",
    "description": "The DNS endpoint to connect to the instance for read only access. This is only available if enable_readable_secondaries is true."
  },
  {
    "name": "read_write_dns",
    "type": "string",
    "description": "The DNS endpoint to connect to the instance for read+write access."
  },
  {
    "name": "retention_window_in_days",
    "type": "integer",
    "description": "The retention window for the instance. This is the time window in days for which the historical data is retained. The default value is 7 days. Valid values are 2 to 35 days."
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current state of the instance. (AVAILABLE, DELETING, FAILING_OVER, STARTING, STOPPED, UPDATING)"
  },
  {
    "name": "stopped",
    "type": "boolean",
    "description": "Whether to stop the instance. An input only param, see effective_stopped for the output."
  },
  {
    "name": "uid",
    "type": "string",
    "description": "An immutable UUID identifier for the instance."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the instance. This is the unique identifier for the instance."
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": "The policy that is applied to the instance. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": "The desired usage policy to associate with the instance."
  },
  {
    "name": "capacity",
    "type": "string",
    "description": "The sku of the instance. Valid values are \"CU_1\", \"CU_2\", \"CU_4\", \"CU_8\"."
  },
  {
    "name": "child_instance_refs",
    "type": "array",
    "description": "The refs of the child instances. This is only available if the instance is parent instance.",
    "children": [
      {
        "name": "branch_time",
        "type": "string",
        "description": "Branch time of the ref database instance. For a parent ref instance, this is the point in time on the parent instance from which the instance was created. For a child ref instance, this is the point in time on the instance from which the child instance was created. Input: For specifying the point in time to create a child instance. Optional. Output: Only populated if provided as input to create a child instance."
      },
      {
        "name": "effective_lsn",
        "type": "string",
        "description": "For a parent ref instance, this is the LSN on the parent instance from which the instance was created. For a child ref instance, this is the LSN on the instance from which the child instance was created. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
      },
      {
        "name": "lsn",
        "type": "string",
        "description": "User-specified WAL LSN of the ref database instance. Input: For specifying the WAL LSN to create a child instance. Optional. Output: Only populated if provided as input to create a child instance."
      },
      {
        "name": "name",
        "type": "string",
        "description": "Name of the ref database instance."
      },
      {
        "name": "uid",
        "type": "string",
        "description": "Id of the ref database instance."
      }
    ]
  },
  {
    "name": "creation_time",
    "type": "string",
    "description": "The timestamp when the instance was created."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the creator of the instance."
  },
  {
    "name": "custom_tags",
    "type": "array",
    "description": "Custom tags associated with the instance. This field is only included on create and update responses.",
    "children": [
      {
        "name": "key",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": "The value of the custom tag."
      }
    ]
  },
  {
    "name": "effective_capacity",
    "type": "string",
    "description": "Deprecated. The sku of the instance; this field will always match the value of capacity. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_custom_tags",
    "type": "array",
    "description": "The recorded custom tags associated with the instance. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.",
    "children": [
      {
        "name": "key",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": "The value of the custom tag."
      }
    ]
  },
  {
    "name": "effective_enable_pg_native_login",
    "type": "boolean",
    "description": "Whether the instance has PG native password login enabled. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_enable_readable_secondaries",
    "type": "boolean",
    "description": "Whether secondaries serving read-only traffic are enabled. Defaults to false. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_node_count",
    "type": "integer",
    "description": "The number of nodes in the instance, composed of 1 primary and 0 or more secondaries. Defaults to 1 primary and 0 secondaries. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_retention_window_in_days",
    "type": "integer",
    "description": "The retention window for the instance. This is the time window in days for which the historical data is retained. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_stopped",
    "type": "boolean",
    "description": "Whether the instance is stopped. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "enable_pg_native_login",
    "type": "boolean",
    "description": "Whether to enable PG native password login on the instance. Defaults to false."
  },
  {
    "name": "enable_readable_secondaries",
    "type": "boolean",
    "description": "Whether to enable secondaries to serve read-only traffic. Defaults to false."
  },
  {
    "name": "node_count",
    "type": "integer",
    "description": "The number of nodes in the instance, composed of 1 primary and 0 or more secondaries. Defaults to 1 primary and 0 secondaries. This field is input only, see effective_node_count for the output."
  },
  {
    "name": "parent_instance_ref",
    "type": "object",
    "description": "DatabaseInstanceRef is a reference to a database instance. It is used in the DatabaseInstance<br />    object to refer to the parent instance of an instance and to refer the child instances of an<br />    instance. To specify as a parent instance during creation of an instance, the lsn and<br />    branch_time fields are optional. If not specified, the child instance will be created from the<br />    latest lsn of the parent. If both lsn and branch_time are specified, the lsn will be used to<br />    create the child instance.",
    "children": [
      {
        "name": "branch_time",
        "type": "string",
        "description": "Branch time of the ref database instance. For a parent ref instance, this is the point in time on the parent instance from which the instance was created. For a child ref instance, this is the point in time on the instance from which the child instance was created. Input: For specifying the point in time to create a child instance. Optional. Output: Only populated if provided as input to create a child instance."
      },
      {
        "name": "effective_lsn",
        "type": "string",
        "description": "For a parent ref instance, this is the LSN on the parent instance from which the instance was created. For a child ref instance, this is the LSN on the instance from which the child instance was created. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
      },
      {
        "name": "lsn",
        "type": "string",
        "description": "User-specified WAL LSN of the ref database instance. Input: For specifying the WAL LSN to create a child instance. Optional. Output: Only populated if provided as input to create a child instance."
      },
      {
        "name": "name",
        "type": "string",
        "description": "Name of the ref database instance."
      },
      {
        "name": "uid",
        "type": "string",
        "description": "Id of the ref database instance."
      }
    ]
  },
  {
    "name": "pg_version",
    "type": "string",
    "description": "The version of Postgres running on the instance."
  },
  {
    "name": "read_only_dns",
    "type": "string",
    "description": "The DNS endpoint to connect to the instance for read only access. This is only available if enable_readable_secondaries is true."
  },
  {
    "name": "read_write_dns",
    "type": "string",
    "description": "The DNS endpoint to connect to the instance for read+write access."
  },
  {
    "name": "retention_window_in_days",
    "type": "integer",
    "description": "The retention window for the instance. This is the time window in days for which the historical data is retained. The default value is 7 days. Valid values are 2 to 35 days."
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current state of the instance. (AVAILABLE, DELETING, FAILING_OVER, STARTING, STOPPED, UPDATING)"
  },
  {
    "name": "stopped",
    "type": "boolean",
    "description": "Whether to stop the instance. An input only param, see effective_stopped for the output."
  },
  {
    "name": "uid",
    "type": "string",
    "description": "An immutable UUID identifier for the instance."
  }
]} />
</TabItem>
<TabItem value="find_by_uid">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the instance. This is the unique identifier for the instance."
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": "The policy that is applied to the instance. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": "The desired usage policy to associate with the instance."
  },
  {
    "name": "capacity",
    "type": "string",
    "description": "The sku of the instance. Valid values are \"CU_1\", \"CU_2\", \"CU_4\", \"CU_8\"."
  },
  {
    "name": "child_instance_refs",
    "type": "array",
    "description": "The refs of the child instances. This is only available if the instance is parent instance.",
    "children": [
      {
        "name": "branch_time",
        "type": "string",
        "description": "Branch time of the ref database instance. For a parent ref instance, this is the point in time on the parent instance from which the instance was created. For a child ref instance, this is the point in time on the instance from which the child instance was created. Input: For specifying the point in time to create a child instance. Optional. Output: Only populated if provided as input to create a child instance."
      },
      {
        "name": "effective_lsn",
        "type": "string",
        "description": "For a parent ref instance, this is the LSN on the parent instance from which the instance was created. For a child ref instance, this is the LSN on the instance from which the child instance was created. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
      },
      {
        "name": "lsn",
        "type": "string",
        "description": "User-specified WAL LSN of the ref database instance. Input: For specifying the WAL LSN to create a child instance. Optional. Output: Only populated if provided as input to create a child instance."
      },
      {
        "name": "name",
        "type": "string",
        "description": "Name of the ref database instance."
      },
      {
        "name": "uid",
        "type": "string",
        "description": "Id of the ref database instance."
      }
    ]
  },
  {
    "name": "creation_time",
    "type": "string",
    "description": "The timestamp when the instance was created."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the creator of the instance."
  },
  {
    "name": "custom_tags",
    "type": "array",
    "description": "Custom tags associated with the instance. This field is only included on create and update responses.",
    "children": [
      {
        "name": "key",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": "The value of the custom tag."
      }
    ]
  },
  {
    "name": "effective_capacity",
    "type": "string",
    "description": "Deprecated. The sku of the instance; this field will always match the value of capacity. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_custom_tags",
    "type": "array",
    "description": "The recorded custom tags associated with the instance. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.",
    "children": [
      {
        "name": "key",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": "The value of the custom tag."
      }
    ]
  },
  {
    "name": "effective_enable_pg_native_login",
    "type": "boolean",
    "description": "Whether the instance has PG native password login enabled. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_enable_readable_secondaries",
    "type": "boolean",
    "description": "Whether secondaries serving read-only traffic are enabled. Defaults to false. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_node_count",
    "type": "integer",
    "description": "The number of nodes in the instance, composed of 1 primary and 0 or more secondaries. Defaults to 1 primary and 0 secondaries. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_retention_window_in_days",
    "type": "integer",
    "description": "The retention window for the instance. This is the time window in days for which the historical data is retained. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "effective_stopped",
    "type": "boolean",
    "description": "Whether the instance is stopped. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
  },
  {
    "name": "enable_pg_native_login",
    "type": "boolean",
    "description": "Whether to enable PG native password login on the instance. Defaults to false."
  },
  {
    "name": "enable_readable_secondaries",
    "type": "boolean",
    "description": "Whether to enable secondaries to serve read-only traffic. Defaults to false."
  },
  {
    "name": "node_count",
    "type": "integer",
    "description": "The number of nodes in the instance, composed of 1 primary and 0 or more secondaries. Defaults to 1 primary and 0 secondaries. This field is input only, see effective_node_count for the output."
  },
  {
    "name": "parent_instance_ref",
    "type": "object",
    "description": "DatabaseInstanceRef is a reference to a database instance. It is used in the DatabaseInstance<br />    object to refer to the parent instance of an instance and to refer the child instances of an<br />    instance. To specify as a parent instance during creation of an instance, the lsn and<br />    branch_time fields are optional. If not specified, the child instance will be created from the<br />    latest lsn of the parent. If both lsn and branch_time are specified, the lsn will be used to<br />    create the child instance.",
    "children": [
      {
        "name": "branch_time",
        "type": "string",
        "description": "Branch time of the ref database instance. For a parent ref instance, this is the point in time on the parent instance from which the instance was created. For a child ref instance, this is the point in time on the instance from which the child instance was created. Input: For specifying the point in time to create a child instance. Optional. Output: Only populated if provided as input to create a child instance."
      },
      {
        "name": "effective_lsn",
        "type": "string",
        "description": "For a parent ref instance, this is the LSN on the parent instance from which the instance was created. For a child ref instance, this is the LSN on the instance from which the child instance was created. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value."
      },
      {
        "name": "lsn",
        "type": "string",
        "description": "User-specified WAL LSN of the ref database instance. Input: For specifying the WAL LSN to create a child instance. Optional. Output: Only populated if provided as input to create a child instance."
      },
      {
        "name": "name",
        "type": "string",
        "description": "Name of the ref database instance."
      },
      {
        "name": "uid",
        "type": "string",
        "description": "Id of the ref database instance."
      }
    ]
  },
  {
    "name": "pg_version",
    "type": "string",
    "description": "The version of Postgres running on the instance."
  },
  {
    "name": "read_only_dns",
    "type": "string",
    "description": "The DNS endpoint to connect to the instance for read only access. This is only available if enable_readable_secondaries is true."
  },
  {
    "name": "read_write_dns",
    "type": "string",
    "description": "The DNS endpoint to connect to the instance for read+write access."
  },
  {
    "name": "retention_window_in_days",
    "type": "integer",
    "description": "The retention window for the instance. This is the time window in days for which the historical data is retained. The default value is 7 days. Valid values are 2 to 35 days."
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current state of the instance. (AVAILABLE, DELETING, FAILING_OVER, STARTING, STOPPED, UPDATING)"
  },
  {
    "name": "stopped",
    "type": "boolean",
    "description": "Whether to stop the instance. An input only param, see effective_stopped for the output."
  },
  {
    "name": "uid",
    "type": "string",
    "description": "An immutable UUID identifier for the instance."
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Get a Database Instance.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List Database Instances.</td>
</tr>
<tr>
    <td><a href="#find_by_uid"><CopyableCode code="find_by_uid" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-uid"><code>uid</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Find a Database Instance by uid.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-database_instance"><code>database_instance</code></a></td>
    <td></td>
    <td>Create a Database Instance.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-database_instance"><code>database_instance</code></a></td>
    <td></td>
    <td>Update a Database Instance.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a>, <a href="#parameter-purge"><code>purge</code></a></td>
    <td>Delete a Database Instance.</td>
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
    <td>Name of the instance to delete.</td>
</tr>
<tr id="parameter-uid">
    <td><CopyableCode code="uid" /></td>
    <td><code>string</code></td>
    <td>UID of the cluster to get.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>By default, a instance cannot be deleted if it has descendant instances created via PITR. If this flag is specified as true, all descendent instances will be deleted as well.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Upper bound for items returned.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page of Database Instances. Requests first page if absent.</td>
</tr>
<tr id="parameter-purge">
    <td><CopyableCode code="purge" /></td>
    <td><code>boolean</code></td>
    <td>Deprecated. Omitting the field or setting it to true will result in the field being hard deleted. Setting a value of false will throw a bad request.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'find_by_uid', value: 'find_by_uid' }
    ]}
>
<TabItem value="get">

Get a Database Instance.

```sql
SELECT
name,
effective_usage_policy_id,
usage_policy_id,
capacity,
child_instance_refs,
creation_time,
creator,
custom_tags,
effective_capacity,
effective_custom_tags,
effective_enable_pg_native_login,
effective_enable_readable_secondaries,
effective_node_count,
effective_retention_window_in_days,
effective_stopped,
enable_pg_native_login,
enable_readable_secondaries,
node_count,
parent_instance_ref,
pg_version,
read_only_dns,
read_write_dns,
retention_window_in_days,
state,
stopped,
uid
FROM databricks_workspace.database.database_instances
WHERE name = '{{ name }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Database Instances.

```sql
SELECT
name,
effective_usage_policy_id,
usage_policy_id,
capacity,
child_instance_refs,
creation_time,
creator,
custom_tags,
effective_capacity,
effective_custom_tags,
effective_enable_pg_native_login,
effective_enable_readable_secondaries,
effective_node_count,
effective_retention_window_in_days,
effective_stopped,
enable_pg_native_login,
enable_readable_secondaries,
node_count,
parent_instance_ref,
pg_version,
read_only_dns,
read_write_dns,
retention_window_in_days,
state,
stopped,
uid
FROM databricks_workspace.database.database_instances
WHERE workspace = '{{ workspace }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="find_by_uid">

Find a Database Instance by uid.

```sql
SELECT
name,
effective_usage_policy_id,
usage_policy_id,
capacity,
child_instance_refs,
creation_time,
creator,
custom_tags,
effective_capacity,
effective_custom_tags,
effective_enable_pg_native_login,
effective_enable_readable_secondaries,
effective_node_count,
effective_retention_window_in_days,
effective_stopped,
enable_pg_native_login,
enable_readable_secondaries,
node_count,
parent_instance_ref,
pg_version,
read_only_dns,
read_write_dns,
retention_window_in_days,
state,
stopped,
uid
FROM databricks_workspace.database.database_instances
WHERE uid = '{{ uid }}' -- required
AND workspace = '{{ workspace }}' -- required
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

Create a Database Instance.

```sql
INSERT INTO databricks_workspace.database.database_instances (
database_instance,
workspace
)
SELECT 
'{{ database_instance }}' /* required */,
'{{ workspace }}'
RETURNING
name,
effective_usage_policy_id,
usage_policy_id,
capacity,
child_instance_refs,
creation_time,
creator,
custom_tags,
effective_capacity,
effective_custom_tags,
effective_enable_pg_native_login,
effective_enable_readable_secondaries,
effective_node_count,
effective_retention_window_in_days,
effective_stopped,
enable_pg_native_login,
enable_readable_secondaries,
node_count,
parent_instance_ref,
pg_version,
read_only_dns,
read_write_dns,
retention_window_in_days,
state,
stopped,
uid
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: database_instances
  props:
    - name: workspace
      value: string
      description: Required parameter for the database_instances resource.
    - name: database_instance
      value: object
      description: |
        Instance to create.
      props:
      - name: name
        value: string
        description: |
          The name of the instance. This is the unique identifier for the instance.
      - name: capacity
        value: string
        description: |
          The sku of the instance. Valid values are "CU_1", "CU_2", "CU_4", "CU_8".
      - name: child_instance_refs
        value: array
        description: |
          The refs of the child instances. This is only available if the instance is parent instance.
        props:
        - name: branch_time
          value: string
          description: |
            Branch time of the ref database instance. For a parent ref instance, this is the point in time on the parent instance from which the instance was created. For a child ref instance, this is the point in time on the instance from which the child instance was created. Input: For specifying the point in time to create a child instance. Optional. Output: Only populated if provided as input to create a child instance.
        - name: effective_lsn
          value: string
          description: |
            For a parent ref instance, this is the LSN on the parent instance from which the instance was created. For a child ref instance, this is the LSN on the instance from which the child instance was created. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.
        - name: lsn
          value: string
          description: |
            User-specified WAL LSN of the ref database instance. Input: For specifying the WAL LSN to create a child instance. Optional. Output: Only populated if provided as input to create a child instance.
        - name: name
          value: string
          description: |
            Name of the ref database instance.
        - name: uid
          value: string
          description: |
            Id of the ref database instance.
      - name: creation_time
        value: string
        description: |
          The timestamp when the instance was created.
      - name: creator
        value: string
        description: |
          The email of the creator of the instance.
      - name: custom_tags
        value: array
        description: |
          Custom tags associated with the instance. This field is only included on create and update responses.
        props:
        - name: key
          value: string
        - name: value
          value: string
          description: |
            The value of the custom tag.
      - name: effective_capacity
        value: string
        description: |
          Deprecated. The sku of the instance; this field will always match the value of capacity. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.
      - name: effective_custom_tags
        value: array
        description: |
          The recorded custom tags associated with the instance. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.
        props:
        - name: key
          value: string
        - name: value
          value: string
          description: |
            The value of the custom tag.
      - name: effective_enable_pg_native_login
        value: boolean
        description: |
          Whether the instance has PG native password login enabled. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.
      - name: effective_enable_readable_secondaries
        value: boolean
        description: |
          Whether secondaries serving read-only traffic are enabled. Defaults to false. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.
      - name: effective_node_count
        value: integer
        description: |
          The number of nodes in the instance, composed of 1 primary and 0 or more secondaries. Defaults to 1 primary and 0 secondaries. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.
      - name: effective_retention_window_in_days
        value: integer
        description: |
          The retention window for the instance. This is the time window in days for which the historical data is retained. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.
      - name: effective_stopped
        value: boolean
        description: |
          Whether the instance is stopped. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.
      - name: effective_usage_policy_id
        value: string
        description: |
          The policy that is applied to the instance. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.
      - name: enable_pg_native_login
        value: boolean
        description: |
          Whether to enable PG native password login on the instance. Defaults to false.
      - name: enable_readable_secondaries
        value: boolean
        description: |
          Whether to enable secondaries to serve read-only traffic. Defaults to false.
      - name: node_count
        value: integer
        description: |
          The number of nodes in the instance, composed of 1 primary and 0 or more secondaries. Defaults to 1 primary and 0 secondaries. This field is input only, see effective_node_count for the output.
      - name: parent_instance_ref
        value: object
        description: |
          The ref of the parent instance. This is only available if the instance is child instance. Input: For specifying the parent instance to create a child instance. Optional. Output: Only populated if provided as input to create a child instance.
        props:
        - name: branch_time
          value: string
          description: |
            Branch time of the ref database instance. For a parent ref instance, this is the point in time on the parent instance from which the instance was created. For a child ref instance, this is the point in time on the instance from which the child instance was created. Input: For specifying the point in time to create a child instance. Optional. Output: Only populated if provided as input to create a child instance.
        - name: effective_lsn
          value: string
          description: |
            For a parent ref instance, this is the LSN on the parent instance from which the instance was created. For a child ref instance, this is the LSN on the instance from which the child instance was created. This is an output only field that contains the value computed from the input field combined with server side defaults. Use the field without the effective_ prefix to set the value.
        - name: lsn
          value: string
          description: |
            User-specified WAL LSN of the ref database instance. Input: For specifying the WAL LSN to create a child instance. Optional. Output: Only populated if provided as input to create a child instance.
        - name: name
          value: string
          description: |
            Name of the ref database instance.
        - name: uid
          value: string
          description: |
            Id of the ref database instance.
      - name: pg_version
        value: string
        description: |
          The version of Postgres running on the instance.
      - name: read_only_dns
        value: string
        description: |
          The DNS endpoint to connect to the instance for read only access. This is only available if enable_readable_secondaries is true.
      - name: read_write_dns
        value: string
        description: |
          The DNS endpoint to connect to the instance for read+write access.
      - name: retention_window_in_days
        value: integer
        description: |
          The retention window for the instance. This is the time window in days for which the historical data is retained. The default value is 7 days. Valid values are 2 to 35 days.
      - name: state
        value: string
        description: |
          The current state of the instance.
      - name: stopped
        value: boolean
        description: |
          Whether to stop the instance. An input only param, see effective_stopped for the output.
      - name: uid
        value: string
        description: |
          An immutable UUID identifier for the instance.
      - name: usage_policy_id
        value: string
        description: |
          The desired usage policy to associate with the instance.
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

Update a Database Instance.

```sql
UPDATE databricks_workspace.database.database_instances
SET 
database_instance = '{{ database_instance }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND workspace = '{{ workspace }}' --required
AND database_instance = '{{ database_instance }}' --required
RETURNING
name,
effective_usage_policy_id,
usage_policy_id,
capacity,
child_instance_refs,
creation_time,
creator,
custom_tags,
effective_capacity,
effective_custom_tags,
effective_enable_pg_native_login,
effective_enable_readable_secondaries,
effective_node_count,
effective_retention_window_in_days,
effective_stopped,
enable_pg_native_login,
enable_readable_secondaries,
node_count,
parent_instance_ref,
pg_version,
read_only_dns,
read_write_dns,
retention_window_in_days,
state,
stopped,
uid;
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

Delete a Database Instance.

```sql
DELETE FROM databricks_workspace.database.database_instances
WHERE name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
AND force = '{{ force }}'
AND purge = '{{ purge }}'
;
```
</TabItem>
</Tabs>

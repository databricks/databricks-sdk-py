---
title: workspace_warehouse_config
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_warehouse_config
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

Creates, updates, deletes, gets or lists a <code>workspace_warehouse_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_warehouse_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.workspace_warehouse_config" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "channel",
    "type": "object",
    "description": "Configures the channel name and DBSQL version of the warehouse. CHANNEL_NAME_CUSTOM should be<br />    chosen only when `dbsql_version` is specified.",
    "children": [
      {
        "name": "dbsql_version",
        "type": "string",
        "description": ""
      },
      {
        "name": "name",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      }
    ]
  },
  {
    "name": "config_param",
    "type": "object",
    "description": "Deprecated: Use sql_configuration_parameters",
    "children": [
      {
        "name": "config_pair",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "configuration_pairs",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "data_access_config",
    "type": "array",
    "description": "Spark confs for external hive metastore configuration JSON serialized size must be less than &lt;= 512K",
    "children": [
      {
        "name": "key",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "enable_serverless_compute",
    "type": "boolean",
    "description": "Enable Serverless compute for SQL warehouses"
  },
  {
    "name": "enabled_warehouse_types",
    "type": "array",
    "description": "List of Warehouse Types allowed in this workspace (limits allowed value of the type field in CreateWarehouse and EditWarehouse). Note: Some types cannot be disabled, they don't need to be specified in SetWorkspaceWarehouseConfig. Note: Disabling a type may cause existing warehouses to be converted to another type. Used by frontend to save specific type availability in the warehouse create and edit form UI.",
    "children": [
      {
        "name": "enabled",
        "type": "boolean",
        "description": "If set to false the specific warehouse type will not be be allowed as a value for warehouse_type in CreateWarehouse and EditWarehouse"
      },
      {
        "name": "warehouse_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      }
    ]
  },
  {
    "name": "global_param",
    "type": "object",
    "description": "Deprecated: Use sql_configuration_parameters",
    "children": [
      {
        "name": "config_pair",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "configuration_pairs",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "google_service_account",
    "type": "string",
    "description": "GCP only: Google Service Account used to pass to cluster to access Google Cloud Storage"
  },
  {
    "name": "instance_profile_arn",
    "type": "string",
    "description": "AWS Only: The instance profile used to pass an IAM role to the SQL warehouses. This configuration is also applied to the workspace's serverless compute for notebooks and jobs."
  },
  {
    "name": "security_policy",
    "type": "string",
    "description": "Security policy for warehouses"
  },
  {
    "name": "sql_configuration_parameters",
    "type": "object",
    "description": "SQL configuration parameters",
    "children": [
      {
        "name": "config_pair",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "configuration_pairs",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": ""
          }
        ]
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
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the workspace level configuration that is shared by all SQL warehouses in a workspace.<br /><br /><br />:returns: :class:`GetWorkspaceWarehouseConfigResponse`</td>
</tr>
<tr>
    <td><a href="#set"><CopyableCode code="set" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Sets the workspace level configuration that is shared by all SQL warehouses in a workspace.<br /><br />:param channel: :class:`Channel` (optional)<br />  Optional: Channel selection details<br />:param config_param: :class:`RepeatedEndpointConfPairs` (optional)<br />  Deprecated: Use sql_configuration_parameters<br />:param data_access_config: List[:class:`EndpointConfPair`] (optional)<br />  Spark confs for external hive metastore configuration JSON serialized size must be less than &lt;= 512K<br />:param enable_serverless_compute: bool (optional)<br />  Enable Serverless compute for SQL warehouses<br />:param enabled_warehouse_types: List[:class:`WarehouseTypePair`] (optional)<br />  List of Warehouse Types allowed in this workspace (limits allowed value of the type field in<br />  CreateWarehouse and EditWarehouse). Note: Some types cannot be disabled, they don't need to be<br />  specified in SetWorkspaceWarehouseConfig. Note: Disabling a type may cause existing warehouses to be<br />  converted to another type. Used by frontend to save specific type availability in the warehouse<br />  create and edit form UI.<br />:param global_param: :class:`RepeatedEndpointConfPairs` (optional)<br />  Deprecated: Use sql_configuration_parameters<br />:param google_service_account: str (optional)<br />  GCP only: Google Service Account used to pass to cluster to access Google Cloud Storage<br />:param instance_profile_arn: str (optional)<br />  AWS Only: The instance profile used to pass an IAM role to the SQL warehouses. This configuration is<br />  also applied to the workspace's serverless compute for notebooks and jobs.<br />:param security_policy: :class:`SetWorkspaceWarehouseConfigRequestSecurityPolicy` (optional)<br />  Security policy for warehouses<br />:param sql_configuration_parameters: :class:`RepeatedEndpointConfPairs` (optional)<br />  SQL configuration parameters</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the workspace level configuration that is shared by all SQL warehouses in a workspace.<br /><br /><br />:returns: :class:`GetWorkspaceWarehouseConfigResponse`

```sql
SELECT
channel,
config_param,
data_access_config,
enable_serverless_compute,
enabled_warehouse_types,
global_param,
google_service_account,
instance_profile_arn,
security_policy,
sql_configuration_parameters
FROM databricks_workspace.sql.workspace_warehouse_config
WHERE deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="set"
    values={[
        { label: 'set', value: 'set' }
    ]}
>
<TabItem value="set">

Sets the workspace level configuration that is shared by all SQL warehouses in a workspace.<br /><br />:param channel: :class:`Channel` (optional)<br />  Optional: Channel selection details<br />:param config_param: :class:`RepeatedEndpointConfPairs` (optional)<br />  Deprecated: Use sql_configuration_parameters<br />:param data_access_config: List[:class:`EndpointConfPair`] (optional)<br />  Spark confs for external hive metastore configuration JSON serialized size must be less than &lt;= 512K<br />:param enable_serverless_compute: bool (optional)<br />  Enable Serverless compute for SQL warehouses<br />:param enabled_warehouse_types: List[:class:`WarehouseTypePair`] (optional)<br />  List of Warehouse Types allowed in this workspace (limits allowed value of the type field in<br />  CreateWarehouse and EditWarehouse). Note: Some types cannot be disabled, they don't need to be<br />  specified in SetWorkspaceWarehouseConfig. Note: Disabling a type may cause existing warehouses to be<br />  converted to another type. Used by frontend to save specific type availability in the warehouse<br />  create and edit form UI.<br />:param global_param: :class:`RepeatedEndpointConfPairs` (optional)<br />  Deprecated: Use sql_configuration_parameters<br />:param google_service_account: str (optional)<br />  GCP only: Google Service Account used to pass to cluster to access Google Cloud Storage<br />:param instance_profile_arn: str (optional)<br />  AWS Only: The instance profile used to pass an IAM role to the SQL warehouses. This configuration is<br />  also applied to the workspace's serverless compute for notebooks and jobs.<br />:param security_policy: :class:`SetWorkspaceWarehouseConfigRequestSecurityPolicy` (optional)<br />  Security policy for warehouses<br />:param sql_configuration_parameters: :class:`RepeatedEndpointConfPairs` (optional)<br />  SQL configuration parameters

```sql
REPLACE databricks_workspace.sql.workspace_warehouse_config
SET 
data__channel = '{{ channel }}',
data__config_param = '{{ config_param }}',
data__data_access_config = '{{ data_access_config }}',
data__enable_serverless_compute = '{{ enable_serverless_compute }}',
data__enabled_warehouse_types = '{{ enabled_warehouse_types }}',
data__global_param = '{{ global_param }}',
data__google_service_account = '{{ google_service_account }}',
data__instance_profile_arn = '{{ instance_profile_arn }}',
data__security_policy = '{{ security_policy }}',
data__sql_configuration_parameters = '{{ sql_configuration_parameters }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>

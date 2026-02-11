---
title: warehouses
hide_title: false
hide_table_of_contents: false
keywords:
  - warehouses
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

Creates, updates, deletes, gets or lists a <code>warehouses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>warehouses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.warehouses" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": "unique identifier for warehouse"
  },
  {
    "name": "name",
    "type": "string",
    "description": "Logical name for the cluster. Supported values: - Must be unique within an org. - Must be less than 100 characters."
  },
  {
    "name": "creator_name",
    "type": "string",
    "description": "warehouse creator name"
  },
  {
    "name": "auto_stop_mins",
    "type": "integer",
    "description": ""
  },
  {
    "name": "channel",
    "type": "object",
    "description": "Channel Details",
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
    "name": "cluster_size",
    "type": "string",
    "description": "Size of the clusters allocated for this warehouse. Increasing the size of a spark cluster allows you to run larger queries on it. If you want to increase the number of concurrent queries, please tune max_num_clusters. Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large - 4X-Large"
  },
  {
    "name": "enable_photon",
    "type": "boolean",
    "description": "Configures whether the warehouse should use Photon optimized clusters. Defaults to false."
  },
  {
    "name": "enable_serverless_compute",
    "type": "boolean",
    "description": "Configures whether the warehouse should use serverless compute"
  },
  {
    "name": "health",
    "type": "object",
    "description": "Optional health status. Assume the warehouse is healthy if this field is not set.",
    "children": [
      {
        "name": "details",
        "type": "string",
        "description": ""
      },
      {
        "name": "failure_reason",
        "type": "object",
        "description": "The reason for failure to bring up clusters for this warehouse. This is available when status is 'FAILED' and sometimes when it is DEGRADED.",
        "children": [
          {
            "name": "code",
            "type": "string",
            "description": "The status code indicating why the cluster was terminated"
          },
          {
            "name": "parameters",
            "type": "object",
            "description": "list of parameters that provide additional information about why the cluster was terminated"
          },
          {
            "name": "type",
            "type": "string",
            "description": "type of the termination"
          }
        ]
      },
      {
        "name": "message",
        "type": "string",
        "description": "Deprecated. split into summary and details for security"
      },
      {
        "name": "status",
        "type": "string",
        "description": "Health status of the endpoint."
      },
      {
        "name": "summary",
        "type": "string",
        "description": "A short summary of the health status in case of degraded/failed warehouses."
      }
    ]
  },
  {
    "name": "instance_profile_arn",
    "type": "string",
    "description": "Deprecated. Instance profile used to pass IAM role to the cluster"
  },
  {
    "name": "jdbc_url",
    "type": "string",
    "description": "the jdbc connection string for this warehouse"
  },
  {
    "name": "max_num_clusters",
    "type": "integer",
    "description": "Maximum number of clusters that the autoscaler will create to handle concurrent queries. Supported values: - Must be &gt;= min_num_clusters - Must be &lt;= 40. Defaults to min_clusters if unset."
  },
  {
    "name": "min_num_clusters",
    "type": "integer",
    "description": "Minimum number of available clusters that will be maintained for this SQL warehouse. Increasing this will ensure that a larger number of clusters are always running and therefore may reduce the cold start time for new queries. This is similar to reserved vs. revocable cores in a resource manager. Supported values: - Must be &gt; 0 - Must be &lt;= min(max_num_clusters, 30) Defaults to 1"
  },
  {
    "name": "num_active_sessions",
    "type": "integer",
    "description": "Deprecated. current number of active sessions for the warehouse"
  },
  {
    "name": "num_clusters",
    "type": "integer",
    "description": "current number of clusters running for the service"
  },
  {
    "name": "odbc_params",
    "type": "object",
    "description": "ODBC parameters for the SQL warehouse",
    "children": [
      {
        "name": "hostname",
        "type": "string",
        "description": ""
      },
      {
        "name": "path",
        "type": "string",
        "description": ""
      },
      {
        "name": "port",
        "type": "integer",
        "description": ""
      },
      {
        "name": "protocol",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "spot_instance_policy",
    "type": "string",
    "description": "Configurations whether the endpoint should use spot instances."
  },
  {
    "name": "state",
    "type": "string",
    "description": "state of the endpoint"
  },
  {
    "name": "tags",
    "type": "object",
    "description": "A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes) associated with this SQL warehouse. Supported values: - Number of tags &lt; 45.",
    "children": [
      {
        "name": "custom_tags",
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
    "name": "warehouse_type",
    "type": "string",
    "description": "Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and also set the field `enable_serverless_compute` to `true`."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "unique identifier for warehouse"
  },
  {
    "name": "name",
    "type": "string",
    "description": "Logical name for the cluster. Supported values: - Must be unique within an org. - Must be less than 100 characters."
  },
  {
    "name": "creator_name",
    "type": "string",
    "description": "warehouse creator name"
  },
  {
    "name": "auto_stop_mins",
    "type": "integer",
    "description": ""
  },
  {
    "name": "channel",
    "type": "object",
    "description": "Channel Details",
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
    "name": "cluster_size",
    "type": "string",
    "description": "Size of the clusters allocated for this warehouse. Increasing the size of a spark cluster allows you to run larger queries on it. If you want to increase the number of concurrent queries, please tune max_num_clusters. Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large - 4X-Large"
  },
  {
    "name": "enable_photon",
    "type": "boolean",
    "description": "Configures whether the warehouse should use Photon optimized clusters. Defaults to false."
  },
  {
    "name": "enable_serverless_compute",
    "type": "boolean",
    "description": "Configures whether the warehouse should use serverless compute"
  },
  {
    "name": "health",
    "type": "object",
    "description": "Optional health status. Assume the warehouse is healthy if this field is not set.",
    "children": [
      {
        "name": "details",
        "type": "string",
        "description": ""
      },
      {
        "name": "failure_reason",
        "type": "object",
        "description": "The reason for failure to bring up clusters for this warehouse. This is available when status is 'FAILED' and sometimes when it is DEGRADED.",
        "children": [
          {
            "name": "code",
            "type": "string",
            "description": "The status code indicating why the cluster was terminated"
          },
          {
            "name": "parameters",
            "type": "object",
            "description": "list of parameters that provide additional information about why the cluster was terminated"
          },
          {
            "name": "type",
            "type": "string",
            "description": "type of the termination"
          }
        ]
      },
      {
        "name": "message",
        "type": "string",
        "description": "Deprecated. split into summary and details for security"
      },
      {
        "name": "status",
        "type": "string",
        "description": "Health status of the endpoint."
      },
      {
        "name": "summary",
        "type": "string",
        "description": "A short summary of the health status in case of degraded/failed warehouses."
      }
    ]
  },
  {
    "name": "instance_profile_arn",
    "type": "string",
    "description": "Deprecated. Instance profile used to pass IAM role to the cluster"
  },
  {
    "name": "jdbc_url",
    "type": "string",
    "description": "the jdbc connection string for this warehouse"
  },
  {
    "name": "max_num_clusters",
    "type": "integer",
    "description": "Maximum number of clusters that the autoscaler will create to handle concurrent queries. Supported values: - Must be &gt;= min_num_clusters - Must be &lt;= 40. Defaults to min_clusters if unset."
  },
  {
    "name": "min_num_clusters",
    "type": "integer",
    "description": "Minimum number of available clusters that will be maintained for this SQL warehouse. Increasing this will ensure that a larger number of clusters are always running and therefore may reduce the cold start time for new queries. This is similar to reserved vs. revocable cores in a resource manager. Supported values: - Must be &gt; 0 - Must be &lt;= min(max_num_clusters, 30) Defaults to 1"
  },
  {
    "name": "num_active_sessions",
    "type": "integer",
    "description": "Deprecated. current number of active sessions for the warehouse"
  },
  {
    "name": "num_clusters",
    "type": "integer",
    "description": "current number of clusters running for the service"
  },
  {
    "name": "odbc_params",
    "type": "object",
    "description": "ODBC parameters for the SQL warehouse",
    "children": [
      {
        "name": "hostname",
        "type": "string",
        "description": ""
      },
      {
        "name": "path",
        "type": "string",
        "description": ""
      },
      {
        "name": "port",
        "type": "integer",
        "description": ""
      },
      {
        "name": "protocol",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "spot_instance_policy",
    "type": "string",
    "description": "Configurations whether the endpoint should use spot instances."
  },
  {
    "name": "state",
    "type": "string",
    "description": "state of the endpoint"
  },
  {
    "name": "tags",
    "type": "object",
    "description": "A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes) associated with this SQL warehouse. Supported values: - Number of tags &lt; 45.",
    "children": [
      {
        "name": "custom_tags",
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
    "name": "warehouse_type",
    "type": "string",
    "description": "Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and also set the field `enable_serverless_compute` to `true`."
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the information for a single SQL warehouse.<br /><br />:param id: str<br />  Required. Id of the SQL warehouse.<br /><br />:returns: :class:`GetWarehouseResponse`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-run_as_user_id"><code>run_as_user_id</code></a></td>
    <td>Lists all SQL warehouses that a user has access to.<br /><br />:param page_size: int (optional)<br />  The max number of warehouses to return.<br />:param page_token: str (optional)<br />  A page token, received from a previous `ListWarehouses` call. Provide this to retrieve the<br />  subsequent page; otherwise the first will be retrieved.<br /><br />  When paginating, all other parameters provided to `ListWarehouses` must match the call that provided<br />  the page token.<br />:param run_as_user_id: int (optional)<br />  Service Principal which will be used to fetch the list of endpoints. If not specified, SQL Gateway<br />  will use the user from the session header.<br /><br />:returns: Iterator over :class:`EndpointInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new SQL warehouse.<br /><br />:param auto_stop_mins: int (optional)<br />  The amount of time in minutes that a SQL warehouse must be idle (i.e., no RUNNING queries) before it<br />  is automatically stopped.<br /><br />  Supported values: - Must be == 0 or &gt;= 10 mins - 0 indicates no autostop.<br /><br />  Defaults to 120 mins<br />:param channel: :class:`Channel` (optional)<br />  Channel Details<br />:param cluster_size: str (optional)<br />  Size of the clusters allocated for this warehouse. Increasing the size of a spark cluster allows you<br />  to run larger queries on it. If you want to increase the number of concurrent queries, please tune<br />  max_num_clusters.<br /><br />  Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large -<br />  4X-Large<br />:param creator_name: str (optional)<br />  warehouse creator name<br />:param enable_photon: bool (optional)<br />  Configures whether the warehouse should use Photon optimized clusters.<br /><br />  Defaults to false.<br />:param enable_serverless_compute: bool (optional)<br />  Configures whether the warehouse should use serverless compute<br />:param instance_profile_arn: str (optional)<br />  Deprecated. Instance profile used to pass IAM role to the cluster<br />:param max_num_clusters: int (optional)<br />  Maximum number of clusters that the autoscaler will create to handle concurrent queries.<br /><br />  Supported values: - Must be &gt;= min_num_clusters - Must be &lt;= 40.<br /><br />  Defaults to min_clusters if unset.<br />:param min_num_clusters: int (optional)<br />  Minimum number of available clusters that will be maintained for this SQL warehouse. Increasing this<br />  will ensure that a larger number of clusters are always running and therefore may reduce the cold<br />  start time for new queries. This is similar to reserved vs. revocable cores in a resource manager.<br /><br />  Supported values: - Must be &gt; 0 - Must be &lt;= min(max_num_clusters, 30)<br /><br />  Defaults to 1<br />:param name: str (optional)<br />  Logical name for the cluster.<br /><br />  Supported values: - Must be unique within an org. - Must be less than 100 characters.<br />:param spot_instance_policy: :class:`SpotInstancePolicy` (optional)<br />  Configurations whether the endpoint should use spot instances.<br />:param tags: :class:`EndpointTags` (optional)<br />  A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes)<br />  associated with this SQL warehouse.<br /><br />  Supported values: - Number of tags &lt; 45.<br />:param warehouse_type: :class:`CreateWarehouseRequestWarehouseType` (optional)<br />  Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and<br />  also set the field `enable_serverless_compute` to `true`.<br /><br />:returns:<br />  Long-running operation waiter for :class:`GetWarehouseResponse`.<br />  See :method:wait_get_warehouse_running for more details.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the configuration for a SQL warehouse.<br /><br />:param id: str<br />  Required. Id of the warehouse to configure.<br />:param auto_stop_mins: int (optional)<br />  The amount of time in minutes that a SQL warehouse must be idle (i.e., no RUNNING queries) before it<br />  is automatically stopped.<br /><br />  Supported values: - Must be == 0 or &gt;= 10 mins - 0 indicates no autostop.<br /><br />  Defaults to 120 mins<br />:param channel: :class:`Channel` (optional)<br />  Channel Details<br />:param cluster_size: str (optional)<br />  Size of the clusters allocated for this warehouse. Increasing the size of a spark cluster allows you<br />  to run larger queries on it. If you want to increase the number of concurrent queries, please tune<br />  max_num_clusters.<br /><br />  Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large -<br />  4X-Large<br />:param creator_name: str (optional)<br />  warehouse creator name<br />:param enable_photon: bool (optional)<br />  Configures whether the warehouse should use Photon optimized clusters.<br /><br />  Defaults to false.<br />:param enable_serverless_compute: bool (optional)<br />  Configures whether the warehouse should use serverless compute<br />:param instance_profile_arn: str (optional)<br />  Deprecated. Instance profile used to pass IAM role to the cluster<br />:param max_num_clusters: int (optional)<br />  Maximum number of clusters that the autoscaler will create to handle concurrent queries.<br /><br />  Supported values: - Must be &gt;= min_num_clusters - Must be &lt;= 40.<br /><br />  Defaults to min_clusters if unset.<br />:param min_num_clusters: int (optional)<br />  Minimum number of available clusters that will be maintained for this SQL warehouse. Increasing this<br />  will ensure that a larger number of clusters are always running and therefore may reduce the cold<br />  start time for new queries. This is similar to reserved vs. revocable cores in a resource manager.<br /><br />  Supported values: - Must be &gt; 0 - Must be &lt;= min(max_num_clusters, 30)<br /><br />  Defaults to 1<br />:param name: str (optional)<br />  Logical name for the cluster.<br /><br />  Supported values: - Must be unique within an org. - Must be less than 100 characters.<br />:param spot_instance_policy: :class:`SpotInstancePolicy` (optional)<br />  Configurations whether the endpoint should use spot instances.<br />:param tags: :class:`EndpointTags` (optional)<br />  A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes)<br />  associated with this SQL warehouse.<br /><br />  Supported values: - Number of tags &lt; 45.<br />:param warehouse_type: :class:`EditWarehouseRequestWarehouseType` (optional)<br />  Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and<br />  also set the field `enable_serverless_compute` to `true`.<br /><br />:returns:<br />  Long-running operation waiter for :class:`GetWarehouseResponse`.<br />  See :method:wait_get_warehouse_running for more details.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a SQL warehouse.<br /><br />:param id: str<br />  Required. Id of the SQL warehouse.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Starts a SQL warehouse.<br /><br />:param id: str<br />  Required. Id of the SQL warehouse.<br /><br />:returns:<br />  Long-running operation waiter for :class:`GetWarehouseResponse`.<br />  See :method:wait_get_warehouse_running for more details.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Stops a SQL warehouse.<br /><br />:param id: str<br />  Required. Id of the SQL warehouse.<br /><br />:returns:<br />  Long-running operation waiter for :class:`GetWarehouseResponse`.<br />  See :method:wait_get_warehouse_stopped for more details.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Required. Id of the SQL warehouse.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>The max number of warehouses to return.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous `ListWarehouses` call. Provide this to retrieve the subsequent page; otherwise the first will be retrieved. When paginating, all other parameters provided to `ListWarehouses` must match the call that provided the page token.</td>
</tr>
<tr id="parameter-run_as_user_id">
    <td><CopyableCode code="run_as_user_id" /></td>
    <td><code>string</code></td>
    <td>Service Principal which will be used to fetch the list of endpoints. If not specified, SQL Gateway will use the user from the session header.</td>
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

Gets the information for a single SQL warehouse.<br /><br />:param id: str<br />  Required. Id of the SQL warehouse.<br /><br />:returns: :class:`GetWarehouseResponse`

```sql
SELECT
id,
name,
creator_name,
auto_stop_mins,
channel,
cluster_size,
enable_photon,
enable_serverless_compute,
health,
instance_profile_arn,
jdbc_url,
max_num_clusters,
min_num_clusters,
num_active_sessions,
num_clusters,
odbc_params,
spot_instance_policy,
state,
tags,
warehouse_type
FROM databricks_workspace.sql.warehouses
WHERE id = '{{ id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all SQL warehouses that a user has access to.<br /><br />:param page_size: int (optional)<br />  The max number of warehouses to return.<br />:param page_token: str (optional)<br />  A page token, received from a previous `ListWarehouses` call. Provide this to retrieve the<br />  subsequent page; otherwise the first will be retrieved.<br /><br />  When paginating, all other parameters provided to `ListWarehouses` must match the call that provided<br />  the page token.<br />:param run_as_user_id: int (optional)<br />  Service Principal which will be used to fetch the list of endpoints. If not specified, SQL Gateway<br />  will use the user from the session header.<br /><br />:returns: Iterator over :class:`EndpointInfo`

```sql
SELECT
id,
name,
creator_name,
auto_stop_mins,
channel,
cluster_size,
enable_photon,
enable_serverless_compute,
health,
instance_profile_arn,
jdbc_url,
max_num_clusters,
min_num_clusters,
num_active_sessions,
num_clusters,
odbc_params,
spot_instance_policy,
state,
tags,
warehouse_type
FROM databricks_workspace.sql.warehouses
WHERE deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND run_as_user_id = '{{ run_as_user_id }}'
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

Creates a new SQL warehouse.<br /><br />:param auto_stop_mins: int (optional)<br />  The amount of time in minutes that a SQL warehouse must be idle (i.e., no RUNNING queries) before it<br />  is automatically stopped.<br /><br />  Supported values: - Must be == 0 or &gt;= 10 mins - 0 indicates no autostop.<br /><br />  Defaults to 120 mins<br />:param channel: :class:`Channel` (optional)<br />  Channel Details<br />:param cluster_size: str (optional)<br />  Size of the clusters allocated for this warehouse. Increasing the size of a spark cluster allows you<br />  to run larger queries on it. If you want to increase the number of concurrent queries, please tune<br />  max_num_clusters.<br /><br />  Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large -<br />  4X-Large<br />:param creator_name: str (optional)<br />  warehouse creator name<br />:param enable_photon: bool (optional)<br />  Configures whether the warehouse should use Photon optimized clusters.<br /><br />  Defaults to false.<br />:param enable_serverless_compute: bool (optional)<br />  Configures whether the warehouse should use serverless compute<br />:param instance_profile_arn: str (optional)<br />  Deprecated. Instance profile used to pass IAM role to the cluster<br />:param max_num_clusters: int (optional)<br />  Maximum number of clusters that the autoscaler will create to handle concurrent queries.<br /><br />  Supported values: - Must be &gt;= min_num_clusters - Must be &lt;= 40.<br /><br />  Defaults to min_clusters if unset.<br />:param min_num_clusters: int (optional)<br />  Minimum number of available clusters that will be maintained for this SQL warehouse. Increasing this<br />  will ensure that a larger number of clusters are always running and therefore may reduce the cold<br />  start time for new queries. This is similar to reserved vs. revocable cores in a resource manager.<br /><br />  Supported values: - Must be &gt; 0 - Must be &lt;= min(max_num_clusters, 30)<br /><br />  Defaults to 1<br />:param name: str (optional)<br />  Logical name for the cluster.<br /><br />  Supported values: - Must be unique within an org. - Must be less than 100 characters.<br />:param spot_instance_policy: :class:`SpotInstancePolicy` (optional)<br />  Configurations whether the endpoint should use spot instances.<br />:param tags: :class:`EndpointTags` (optional)<br />  A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes)<br />  associated with this SQL warehouse.<br /><br />  Supported values: - Number of tags &lt; 45.<br />:param warehouse_type: :class:`CreateWarehouseRequestWarehouseType` (optional)<br />  Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and<br />  also set the field `enable_serverless_compute` to `true`.<br /><br />:returns:<br />  Long-running operation waiter for :class:`GetWarehouseResponse`.<br />  See :method:wait_get_warehouse_running for more details.

```sql
INSERT INTO databricks_workspace.sql.warehouses (
data__auto_stop_mins,
data__channel,
data__cluster_size,
data__creator_name,
data__enable_photon,
data__enable_serverless_compute,
data__instance_profile_arn,
data__max_num_clusters,
data__min_num_clusters,
data__name,
data__spot_instance_policy,
data__tags,
data__warehouse_type,
deployment_name
)
SELECT 
'{{ auto_stop_mins }}',
'{{ channel }}',
'{{ cluster_size }}',
'{{ creator_name }}',
'{{ enable_photon }}',
'{{ enable_serverless_compute }}',
'{{ instance_profile_arn }}',
'{{ max_num_clusters }}',
'{{ min_num_clusters }}',
'{{ name }}',
'{{ spot_instance_policy }}',
'{{ tags }}',
'{{ warehouse_type }}',
'{{ deployment_name }}'
RETURNING
id,
name,
creator_name,
auto_stop_mins,
channel,
cluster_size,
enable_photon,
enable_serverless_compute,
health,
instance_profile_arn,
jdbc_url,
max_num_clusters,
min_num_clusters,
num_active_sessions,
num_clusters,
odbc_params,
spot_instance_policy,
state,
tags,
warehouse_type
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: warehouses
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the warehouses resource.
    - name: auto_stop_mins
      value: string
      description: |
        The amount of time in minutes that a SQL warehouse must be idle (i.e., no RUNNING queries) before it is automatically stopped. Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop. Defaults to 120 mins
    - name: channel
      value: string
      description: |
        Channel Details
    - name: cluster_size
      value: string
      description: |
        Size of the clusters allocated for this warehouse. Increasing the size of a spark cluster allows you to run larger queries on it. If you want to increase the number of concurrent queries, please tune max_num_clusters. Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large - 4X-Large
    - name: creator_name
      value: string
      description: |
        warehouse creator name
    - name: enable_photon
      value: string
      description: |
        Configures whether the warehouse should use Photon optimized clusters. Defaults to false.
    - name: enable_serverless_compute
      value: string
      description: |
        Configures whether the warehouse should use serverless compute
    - name: instance_profile_arn
      value: string
      description: |
        Deprecated. Instance profile used to pass IAM role to the cluster
    - name: max_num_clusters
      value: string
      description: |
        Maximum number of clusters that the autoscaler will create to handle concurrent queries. Supported values: - Must be >= min_num_clusters - Must be <= 40. Defaults to min_clusters if unset.
    - name: min_num_clusters
      value: string
      description: |
        Minimum number of available clusters that will be maintained for this SQL warehouse. Increasing this will ensure that a larger number of clusters are always running and therefore may reduce the cold start time for new queries. This is similar to reserved vs. revocable cores in a resource manager. Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30) Defaults to 1
    - name: name
      value: string
      description: |
        Logical name for the cluster. Supported values: - Must be unique within an org. - Must be less than 100 characters.
    - name: spot_instance_policy
      value: string
      description: |
        Configurations whether the endpoint should use spot instances.
    - name: tags
      value: string
      description: |
        A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes) associated with this SQL warehouse. Supported values: - Number of tags < 45.
    - name: warehouse_type
      value: string
      description: |
        Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and also set the field `enable_serverless_compute` to `true`.
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="edit">

Updates the configuration for a SQL warehouse.<br /><br />:param id: str<br />  Required. Id of the warehouse to configure.<br />:param auto_stop_mins: int (optional)<br />  The amount of time in minutes that a SQL warehouse must be idle (i.e., no RUNNING queries) before it<br />  is automatically stopped.<br /><br />  Supported values: - Must be == 0 or &gt;= 10 mins - 0 indicates no autostop.<br /><br />  Defaults to 120 mins<br />:param channel: :class:`Channel` (optional)<br />  Channel Details<br />:param cluster_size: str (optional)<br />  Size of the clusters allocated for this warehouse. Increasing the size of a spark cluster allows you<br />  to run larger queries on it. If you want to increase the number of concurrent queries, please tune<br />  max_num_clusters.<br /><br />  Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large -<br />  4X-Large<br />:param creator_name: str (optional)<br />  warehouse creator name<br />:param enable_photon: bool (optional)<br />  Configures whether the warehouse should use Photon optimized clusters.<br /><br />  Defaults to false.<br />:param enable_serverless_compute: bool (optional)<br />  Configures whether the warehouse should use serverless compute<br />:param instance_profile_arn: str (optional)<br />  Deprecated. Instance profile used to pass IAM role to the cluster<br />:param max_num_clusters: int (optional)<br />  Maximum number of clusters that the autoscaler will create to handle concurrent queries.<br /><br />  Supported values: - Must be &gt;= min_num_clusters - Must be &lt;= 40.<br /><br />  Defaults to min_clusters if unset.<br />:param min_num_clusters: int (optional)<br />  Minimum number of available clusters that will be maintained for this SQL warehouse. Increasing this<br />  will ensure that a larger number of clusters are always running and therefore may reduce the cold<br />  start time for new queries. This is similar to reserved vs. revocable cores in a resource manager.<br /><br />  Supported values: - Must be &gt; 0 - Must be &lt;= min(max_num_clusters, 30)<br /><br />  Defaults to 1<br />:param name: str (optional)<br />  Logical name for the cluster.<br /><br />  Supported values: - Must be unique within an org. - Must be less than 100 characters.<br />:param spot_instance_policy: :class:`SpotInstancePolicy` (optional)<br />  Configurations whether the endpoint should use spot instances.<br />:param tags: :class:`EndpointTags` (optional)<br />  A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes)<br />  associated with this SQL warehouse.<br /><br />  Supported values: - Number of tags &lt; 45.<br />:param warehouse_type: :class:`EditWarehouseRequestWarehouseType` (optional)<br />  Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and<br />  also set the field `enable_serverless_compute` to `true`.<br /><br />:returns:<br />  Long-running operation waiter for :class:`GetWarehouseResponse`.<br />  See :method:wait_get_warehouse_running for more details.

```sql
REPLACE databricks_workspace.sql.warehouses
SET 
data__auto_stop_mins = '{{ auto_stop_mins }}',
data__channel = '{{ channel }}',
data__cluster_size = '{{ cluster_size }}',
data__creator_name = '{{ creator_name }}',
data__enable_photon = '{{ enable_photon }}',
data__enable_serverless_compute = '{{ enable_serverless_compute }}',
data__instance_profile_arn = '{{ instance_profile_arn }}',
data__max_num_clusters = '{{ max_num_clusters }}',
data__min_num_clusters = '{{ min_num_clusters }}',
data__name = '{{ name }}',
data__spot_instance_policy = '{{ spot_instance_policy }}',
data__tags = '{{ tags }}',
data__warehouse_type = '{{ warehouse_type }}'
WHERE 
id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
id,
name,
creator_name,
auto_stop_mins,
channel,
cluster_size,
enable_photon,
enable_serverless_compute,
health,
instance_profile_arn,
jdbc_url,
max_num_clusters,
min_num_clusters,
num_active_sessions,
num_clusters,
odbc_params,
spot_instance_policy,
state,
tags,
warehouse_type;
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

Deletes a SQL warehouse.<br /><br />:param id: str<br />  Required. Id of the SQL warehouse.

```sql
DELETE FROM databricks_workspace.sql.warehouses
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="start">

Starts a SQL warehouse.<br /><br />:param id: str<br />  Required. Id of the SQL warehouse.<br /><br />:returns:<br />  Long-running operation waiter for :class:`GetWarehouseResponse`.<br />  See :method:wait_get_warehouse_running for more details.

```sql
EXEC databricks_workspace.sql.warehouses.start 
@id='{{ id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops a SQL warehouse.<br /><br />:param id: str<br />  Required. Id of the SQL warehouse.<br /><br />:returns:<br />  Long-running operation waiter for :class:`GetWarehouseResponse`.<br />  See :method:wait_get_warehouse_stopped for more details.

```sql
EXEC databricks_workspace.sql.warehouses.stop 
@id='{{ id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

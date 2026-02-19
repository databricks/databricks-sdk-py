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
<tr><td><b>Name</b></td><td><CopyableCode code="warehouses" /></td></tr>
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
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CHANNEL_NAME_CURRENT, CHANNEL_NAME_CUSTOM, CHANNEL_NAME_PREVIEW, CHANNEL_NAME_PREVIOUS)"
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
            "description": "The status code indicating why the cluster was terminated (ABUSE_DETECTED, ACCESS_TOKEN_FAILURE, ALLOCATION_TIMEOUT, ALLOCATION_TIMEOUT_NODE_DAEMON_NOT_READY, ALLOCATION_TIMEOUT_NO_HEALTHY_AND_WARMED_UP_CLUSTERS, ALLOCATION_TIMEOUT_NO_HEALTHY_CLUSTERS, ALLOCATION_TIMEOUT_NO_MATCHED_CLUSTERS, ALLOCATION_TIMEOUT_NO_READY_CLUSTERS, ALLOCATION_TIMEOUT_NO_UNALLOCATED_CLUSTERS, ALLOCATION_TIMEOUT_NO_WARMED_UP_CLUSTERS, ATTACH_PROJECT_FAILURE, AWS_AUTHORIZATION_FAILURE, AWS_INACCESSIBLE_KMS_KEY_FAILURE, AWS_INSTANCE_PROFILE_UPDATE_FAILURE, AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE, AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE, AWS_INVALID_KEY_PAIR, AWS_INVALID_KMS_KEY_STATE, AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE, AWS_REQUEST_LIMIT_EXCEEDED, AWS_RESOURCE_QUOTA_EXCEEDED, AWS_UNSUPPORTED_FAILURE, AZURE_BYOK_KEY_PERMISSION_FAILURE, AZURE_EPHEMERAL_DISK_FAILURE, AZURE_INVALID_DEPLOYMENT_TEMPLATE, AZURE_OPERATION_NOT_ALLOWED_EXCEPTION, AZURE_PACKED_DEPLOYMENT_PARTIAL_FAILURE, AZURE_QUOTA_EXCEEDED_EXCEPTION, AZURE_RESOURCE_MANAGER_THROTTLING, AZURE_RESOURCE_PROVIDER_THROTTLING, AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE, AZURE_VM_EXTENSION_FAILURE, AZURE_VNET_CONFIGURATION_FAILURE, BOOTSTRAP_TIMEOUT, BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION, BOOTSTRAP_TIMEOUT_DUE_TO_MISCONFIG, BUDGET_POLICY_LIMIT_ENFORCEMENT_ACTIVATED, BUDGET_POLICY_RESOLUTION_FAILURE, CLOUD_ACCOUNT_POD_QUOTA_EXCEEDED, CLOUD_ACCOUNT_SETUP_FAILURE, CLOUD_OPERATION_CANCELLED, CLOUD_PROVIDER_DISK_SETUP_FAILURE, CLOUD_PROVIDER_INSTANCE_NOT_LAUNCHED, CLOUD_PROVIDER_LAUNCH_FAILURE, CLOUD_PROVIDER_LAUNCH_FAILURE_DUE_TO_MISCONFIG, CLOUD_PROVIDER_RESOURCE_STOCKOUT, CLOUD_PROVIDER_RESOURCE_STOCKOUT_DUE_TO_MISCONFIG, CLOUD_PROVIDER_SHUTDOWN, CLUSTER_OPERATION_THROTTLED, CLUSTER_OPERATION_TIMEOUT, COMMUNICATION_LOST, CONTAINER_LAUNCH_FAILURE, CONTROL_PLANE_CONNECTION_FAILURE, CONTROL_PLANE_CONNECTION_FAILURE_DUE_TO_MISCONFIG, CONTROL_PLANE_REQUEST_FAILURE, CONTROL_PLANE_REQUEST_FAILURE_DUE_TO_MISCONFIG, DATABASE_CONNECTION_FAILURE, DATA_ACCESS_CONFIG_CHANGED, DBFS_COMPONENT_UNHEALTHY, DBR_IMAGE_RESOLUTION_FAILURE, DISASTER_RECOVERY_REPLICATION, DNS_RESOLUTION_ERROR, DOCKER_CONTAINER_CREATION_EXCEPTION, DOCKER_IMAGE_PULL_FAILURE, DOCKER_IMAGE_TOO_LARGE_FOR_INSTANCE_EXCEPTION, DOCKER_INVALID_OS_EXCEPTION, DRIVER_EVICTION, DRIVER_LAUNCH_TIMEOUT, DRIVER_NODE_UNREACHABLE, DRIVER_OUT_OF_DISK, DRIVER_OUT_OF_MEMORY, DRIVER_POD_CREATION_FAILURE, DRIVER_UNEXPECTED_FAILURE, DRIVER_UNHEALTHY, DRIVER_UNREACHABLE, DRIVER_UNRESPONSIVE, DYNAMIC_SPARK_CONF_SIZE_EXCEEDED, EOS_SPARK_IMAGE, EXECUTION_COMPONENT_UNHEALTHY, EXECUTOR_POD_UNSCHEDULED, GCP_API_RATE_QUOTA_EXCEEDED, GCP_DENIED_BY_ORG_POLICY, GCP_FORBIDDEN, GCP_IAM_TIMEOUT, GCP_INACCESSIBLE_KMS_KEY_FAILURE, GCP_INSUFFICIENT_CAPACITY, GCP_IP_SPACE_EXHAUSTED, GCP_KMS_KEY_PERMISSION_DENIED, GCP_NOT_FOUND, GCP_QUOTA_EXCEEDED, GCP_RESOURCE_QUOTA_EXCEEDED, GCP_SERVICE_ACCOUNT_ACCESS_DENIED, GCP_SERVICE_ACCOUNT_DELETED, GCP_SERVICE_ACCOUNT_NOT_FOUND, GCP_SUBNET_NOT_READY, GCP_TRUSTED_IMAGE_PROJECTS_VIOLATED, GKE_BASED_CLUSTER_TERMINATION, GLOBAL_INIT_SCRIPT_FAILURE, HIVE_METASTORE_PROVISIONING_FAILURE, IMAGE_PULL_PERMISSION_DENIED, INACTIVITY, INIT_CONTAINER_NOT_FINISHED, INIT_SCRIPT_FAILURE, INSTANCE_POOL_CLUSTER_FAILURE, INSTANCE_POOL_MAX_CAPACITY_REACHED, INSTANCE_POOL_NOT_FOUND, INSTANCE_UNREACHABLE, INSTANCE_UNREACHABLE_DUE_TO_MISCONFIG, INTERNAL_CAPACITY_FAILURE, INTERNAL_ERROR, INVALID_ARGUMENT, INVALID_AWS_PARAMETER, INVALID_INSTANCE_PLACEMENT_PROTOCOL, INVALID_SPARK_IMAGE, INVALID_WORKER_IMAGE_FAILURE, IN_PENALTY_BOX, IP_EXHAUSTION_FAILURE, JOB_FINISHED, K8S_ACTIVE_POD_QUOTA_EXCEEDED, K8S_AUTOSCALING_FAILURE, K8S_DBR_CLUSTER_LAUNCH_TIMEOUT, LAZY_ALLOCATION_TIMEOUT, MAINTENANCE_MODE, METASTORE_COMPONENT_UNHEALTHY, MTLS_PORT_CONNECTIVITY_FAILURE, NEPHOS_RESOURCE_MANAGEMENT, NETVISOR_SETUP_TIMEOUT, NETWORK_CHECK_CONTROL_PLANE_FAILURE, NETWORK_CHECK_CONTROL_PLANE_FAILURE_DUE_TO_MISCONFIG, NETWORK_CHECK_DNS_SERVER_FAILURE, NETWORK_CHECK_DNS_SERVER_FAILURE_DUE_TO_MISCONFIG, NETWORK_CHECK_METADATA_ENDPOINT_FAILURE, NETWORK_CHECK_METADATA_ENDPOINT_FAILURE_DUE_TO_MISCONFIG, NETWORK_CHECK_MULTIPLE_COMPONENTS_FAILURE, NETWORK_CHECK_MULTIPLE_COMPONENTS_FAILURE_DUE_TO_MISCONFIG, NETWORK_CHECK_NIC_FAILURE, NETWORK_CHECK_NIC_FAILURE_DUE_TO_MISCONFIG, NETWORK_CHECK_STORAGE_FAILURE, NETWORK_CHECK_STORAGE_FAILURE_DUE_TO_MISCONFIG, NETWORK_CONFIGURATION_FAILURE, NFS_MOUNT_FAILURE, NO_MATCHED_K8S, NO_MATCHED_K8S_TESTING_TAG, NPIP_TUNNEL_SETUP_FAILURE, NPIP_TUNNEL_TOKEN_FAILURE, POD_ASSIGNMENT_FAILURE, POD_SCHEDULING_FAILURE, RATE_LIMITED, REQUEST_REJECTED, REQUEST_THROTTLED, RESOURCE_USAGE_BLOCKED, SECRET_CREATION_FAILURE, SECRET_PERMISSION_DENIED, SECRET_RESOLUTION_ERROR, SECURITY_DAEMON_REGISTRATION_EXCEPTION, SELF_BOOTSTRAP_FAILURE, SERVERLESS_LONG_RUNNING_TERMINATED, SKIPPED_SLOW_NODES, SLOW_IMAGE_DOWNLOAD, SPARK_ERROR, SPARK_IMAGE_DOWNLOAD_FAILURE, SPARK_IMAGE_DOWNLOAD_THROTTLED, SPARK_IMAGE_NOT_FOUND, SPARK_STARTUP_FAILURE, SPOT_INSTANCE_TERMINATION, SSH_BOOTSTRAP_FAILURE, STORAGE_DOWNLOAD_FAILURE, STORAGE_DOWNLOAD_FAILURE_DUE_TO_MISCONFIG, STORAGE_DOWNLOAD_FAILURE_SLOW, STORAGE_DOWNLOAD_FAILURE_THROTTLED, STS_CLIENT_SETUP_FAILURE, SUBNET_EXHAUSTED_FAILURE, TEMPORARILY_UNAVAILABLE, TRIAL_EXPIRED, UNEXPECTED_LAUNCH_FAILURE, UNEXPECTED_POD_RECREATION, UNKNOWN, UNSUPPORTED_INSTANCE_TYPE, UPDATE_INSTANCE_PROFILE_FAILURE, USAGE_POLICY_ENTITLEMENT_DENIED, USER_INITIATED_VM_TERMINATION, USER_REQUEST, WORKER_SETUP_FAILURE, WORKSPACE_CANCELLED_ERROR, WORKSPACE_CONFIGURATION_ERROR, WORKSPACE_UPDATE)"
          },
          {
            "name": "parameters",
            "type": "object",
            "description": "list of parameters that provide additional information about why the cluster was terminated"
          },
          {
            "name": "type",
            "type": "string",
            "description": "type of the termination (CLIENT_ERROR, CLOUD_FAILURE, SERVICE_FAULT, SUCCESS)"
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
        "description": "Health status of the endpoint. (DEGRADED, FAILED, HEALTHY)"
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
    "description": "Configurations whether the endpoint should use spot instances. (COST_OPTIMIZED, POLICY_UNSPECIFIED, RELIABILITY_OPTIMIZED)"
  },
  {
    "name": "state",
    "type": "string",
    "description": "state of the endpoint (DELETED, DELETING, RUNNING, STARTING, STOPPED, STOPPING)"
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
    "description": "Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and also set the field `enable_serverless_compute` to `true`. (CLASSIC, PRO, TYPE_UNSPECIFIED)"
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
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CHANNEL_NAME_CURRENT, CHANNEL_NAME_CUSTOM, CHANNEL_NAME_PREVIEW, CHANNEL_NAME_PREVIOUS)"
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
            "description": "The status code indicating why the cluster was terminated (ABUSE_DETECTED, ACCESS_TOKEN_FAILURE, ALLOCATION_TIMEOUT, ALLOCATION_TIMEOUT_NODE_DAEMON_NOT_READY, ALLOCATION_TIMEOUT_NO_HEALTHY_AND_WARMED_UP_CLUSTERS, ALLOCATION_TIMEOUT_NO_HEALTHY_CLUSTERS, ALLOCATION_TIMEOUT_NO_MATCHED_CLUSTERS, ALLOCATION_TIMEOUT_NO_READY_CLUSTERS, ALLOCATION_TIMEOUT_NO_UNALLOCATED_CLUSTERS, ALLOCATION_TIMEOUT_NO_WARMED_UP_CLUSTERS, ATTACH_PROJECT_FAILURE, AWS_AUTHORIZATION_FAILURE, AWS_INACCESSIBLE_KMS_KEY_FAILURE, AWS_INSTANCE_PROFILE_UPDATE_FAILURE, AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE, AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE, AWS_INVALID_KEY_PAIR, AWS_INVALID_KMS_KEY_STATE, AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE, AWS_REQUEST_LIMIT_EXCEEDED, AWS_RESOURCE_QUOTA_EXCEEDED, AWS_UNSUPPORTED_FAILURE, AZURE_BYOK_KEY_PERMISSION_FAILURE, AZURE_EPHEMERAL_DISK_FAILURE, AZURE_INVALID_DEPLOYMENT_TEMPLATE, AZURE_OPERATION_NOT_ALLOWED_EXCEPTION, AZURE_PACKED_DEPLOYMENT_PARTIAL_FAILURE, AZURE_QUOTA_EXCEEDED_EXCEPTION, AZURE_RESOURCE_MANAGER_THROTTLING, AZURE_RESOURCE_PROVIDER_THROTTLING, AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE, AZURE_VM_EXTENSION_FAILURE, AZURE_VNET_CONFIGURATION_FAILURE, BOOTSTRAP_TIMEOUT, BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION, BOOTSTRAP_TIMEOUT_DUE_TO_MISCONFIG, BUDGET_POLICY_LIMIT_ENFORCEMENT_ACTIVATED, BUDGET_POLICY_RESOLUTION_FAILURE, CLOUD_ACCOUNT_POD_QUOTA_EXCEEDED, CLOUD_ACCOUNT_SETUP_FAILURE, CLOUD_OPERATION_CANCELLED, CLOUD_PROVIDER_DISK_SETUP_FAILURE, CLOUD_PROVIDER_INSTANCE_NOT_LAUNCHED, CLOUD_PROVIDER_LAUNCH_FAILURE, CLOUD_PROVIDER_LAUNCH_FAILURE_DUE_TO_MISCONFIG, CLOUD_PROVIDER_RESOURCE_STOCKOUT, CLOUD_PROVIDER_RESOURCE_STOCKOUT_DUE_TO_MISCONFIG, CLOUD_PROVIDER_SHUTDOWN, CLUSTER_OPERATION_THROTTLED, CLUSTER_OPERATION_TIMEOUT, COMMUNICATION_LOST, CONTAINER_LAUNCH_FAILURE, CONTROL_PLANE_CONNECTION_FAILURE, CONTROL_PLANE_CONNECTION_FAILURE_DUE_TO_MISCONFIG, CONTROL_PLANE_REQUEST_FAILURE, CONTROL_PLANE_REQUEST_FAILURE_DUE_TO_MISCONFIG, DATABASE_CONNECTION_FAILURE, DATA_ACCESS_CONFIG_CHANGED, DBFS_COMPONENT_UNHEALTHY, DBR_IMAGE_RESOLUTION_FAILURE, DISASTER_RECOVERY_REPLICATION, DNS_RESOLUTION_ERROR, DOCKER_CONTAINER_CREATION_EXCEPTION, DOCKER_IMAGE_PULL_FAILURE, DOCKER_IMAGE_TOO_LARGE_FOR_INSTANCE_EXCEPTION, DOCKER_INVALID_OS_EXCEPTION, DRIVER_EVICTION, DRIVER_LAUNCH_TIMEOUT, DRIVER_NODE_UNREACHABLE, DRIVER_OUT_OF_DISK, DRIVER_OUT_OF_MEMORY, DRIVER_POD_CREATION_FAILURE, DRIVER_UNEXPECTED_FAILURE, DRIVER_UNHEALTHY, DRIVER_UNREACHABLE, DRIVER_UNRESPONSIVE, DYNAMIC_SPARK_CONF_SIZE_EXCEEDED, EOS_SPARK_IMAGE, EXECUTION_COMPONENT_UNHEALTHY, EXECUTOR_POD_UNSCHEDULED, GCP_API_RATE_QUOTA_EXCEEDED, GCP_DENIED_BY_ORG_POLICY, GCP_FORBIDDEN, GCP_IAM_TIMEOUT, GCP_INACCESSIBLE_KMS_KEY_FAILURE, GCP_INSUFFICIENT_CAPACITY, GCP_IP_SPACE_EXHAUSTED, GCP_KMS_KEY_PERMISSION_DENIED, GCP_NOT_FOUND, GCP_QUOTA_EXCEEDED, GCP_RESOURCE_QUOTA_EXCEEDED, GCP_SERVICE_ACCOUNT_ACCESS_DENIED, GCP_SERVICE_ACCOUNT_DELETED, GCP_SERVICE_ACCOUNT_NOT_FOUND, GCP_SUBNET_NOT_READY, GCP_TRUSTED_IMAGE_PROJECTS_VIOLATED, GKE_BASED_CLUSTER_TERMINATION, GLOBAL_INIT_SCRIPT_FAILURE, HIVE_METASTORE_PROVISIONING_FAILURE, IMAGE_PULL_PERMISSION_DENIED, INACTIVITY, INIT_CONTAINER_NOT_FINISHED, INIT_SCRIPT_FAILURE, INSTANCE_POOL_CLUSTER_FAILURE, INSTANCE_POOL_MAX_CAPACITY_REACHED, INSTANCE_POOL_NOT_FOUND, INSTANCE_UNREACHABLE, INSTANCE_UNREACHABLE_DUE_TO_MISCONFIG, INTERNAL_CAPACITY_FAILURE, INTERNAL_ERROR, INVALID_ARGUMENT, INVALID_AWS_PARAMETER, INVALID_INSTANCE_PLACEMENT_PROTOCOL, INVALID_SPARK_IMAGE, INVALID_WORKER_IMAGE_FAILURE, IN_PENALTY_BOX, IP_EXHAUSTION_FAILURE, JOB_FINISHED, K8S_ACTIVE_POD_QUOTA_EXCEEDED, K8S_AUTOSCALING_FAILURE, K8S_DBR_CLUSTER_LAUNCH_TIMEOUT, LAZY_ALLOCATION_TIMEOUT, MAINTENANCE_MODE, METASTORE_COMPONENT_UNHEALTHY, MTLS_PORT_CONNECTIVITY_FAILURE, NEPHOS_RESOURCE_MANAGEMENT, NETVISOR_SETUP_TIMEOUT, NETWORK_CHECK_CONTROL_PLANE_FAILURE, NETWORK_CHECK_CONTROL_PLANE_FAILURE_DUE_TO_MISCONFIG, NETWORK_CHECK_DNS_SERVER_FAILURE, NETWORK_CHECK_DNS_SERVER_FAILURE_DUE_TO_MISCONFIG, NETWORK_CHECK_METADATA_ENDPOINT_FAILURE, NETWORK_CHECK_METADATA_ENDPOINT_FAILURE_DUE_TO_MISCONFIG, NETWORK_CHECK_MULTIPLE_COMPONENTS_FAILURE, NETWORK_CHECK_MULTIPLE_COMPONENTS_FAILURE_DUE_TO_MISCONFIG, NETWORK_CHECK_NIC_FAILURE, NETWORK_CHECK_NIC_FAILURE_DUE_TO_MISCONFIG, NETWORK_CHECK_STORAGE_FAILURE, NETWORK_CHECK_STORAGE_FAILURE_DUE_TO_MISCONFIG, NETWORK_CONFIGURATION_FAILURE, NFS_MOUNT_FAILURE, NO_MATCHED_K8S, NO_MATCHED_K8S_TESTING_TAG, NPIP_TUNNEL_SETUP_FAILURE, NPIP_TUNNEL_TOKEN_FAILURE, POD_ASSIGNMENT_FAILURE, POD_SCHEDULING_FAILURE, RATE_LIMITED, REQUEST_REJECTED, REQUEST_THROTTLED, RESOURCE_USAGE_BLOCKED, SECRET_CREATION_FAILURE, SECRET_PERMISSION_DENIED, SECRET_RESOLUTION_ERROR, SECURITY_DAEMON_REGISTRATION_EXCEPTION, SELF_BOOTSTRAP_FAILURE, SERVERLESS_LONG_RUNNING_TERMINATED, SKIPPED_SLOW_NODES, SLOW_IMAGE_DOWNLOAD, SPARK_ERROR, SPARK_IMAGE_DOWNLOAD_FAILURE, SPARK_IMAGE_DOWNLOAD_THROTTLED, SPARK_IMAGE_NOT_FOUND, SPARK_STARTUP_FAILURE, SPOT_INSTANCE_TERMINATION, SSH_BOOTSTRAP_FAILURE, STORAGE_DOWNLOAD_FAILURE, STORAGE_DOWNLOAD_FAILURE_DUE_TO_MISCONFIG, STORAGE_DOWNLOAD_FAILURE_SLOW, STORAGE_DOWNLOAD_FAILURE_THROTTLED, STS_CLIENT_SETUP_FAILURE, SUBNET_EXHAUSTED_FAILURE, TEMPORARILY_UNAVAILABLE, TRIAL_EXPIRED, UNEXPECTED_LAUNCH_FAILURE, UNEXPECTED_POD_RECREATION, UNKNOWN, UNSUPPORTED_INSTANCE_TYPE, UPDATE_INSTANCE_PROFILE_FAILURE, USAGE_POLICY_ENTITLEMENT_DENIED, USER_INITIATED_VM_TERMINATION, USER_REQUEST, WORKER_SETUP_FAILURE, WORKSPACE_CANCELLED_ERROR, WORKSPACE_CONFIGURATION_ERROR, WORKSPACE_UPDATE)"
          },
          {
            "name": "parameters",
            "type": "object",
            "description": "list of parameters that provide additional information about why the cluster was terminated"
          },
          {
            "name": "type",
            "type": "string",
            "description": "type of the termination (CLIENT_ERROR, CLOUD_FAILURE, SERVICE_FAULT, SUCCESS)"
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
        "description": "Health status of the endpoint. (DEGRADED, FAILED, HEALTHY)"
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
    "description": "Configurations whether the endpoint should use spot instances. (COST_OPTIMIZED, POLICY_UNSPECIFIED, RELIABILITY_OPTIMIZED)"
  },
  {
    "name": "state",
    "type": "string",
    "description": "state of the endpoint (DELETED, DELETING, RUNNING, STARTING, STOPPED, STOPPING)"
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
    "description": "Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and also set the field `enable_serverless_compute` to `true`. (CLASSIC, PRO, TYPE_UNSPECIFIED)"
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
    <td>Gets the information for a single SQL warehouse.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-run_as_user_id"><code>run_as_user_id</code></a></td>
    <td>Lists all SQL warehouses that a user has access to.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new SQL warehouse.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the configuration for a SQL warehouse.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a SQL warehouse.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Starts a SQL warehouse.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Stops a SQL warehouse.</td>
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

Gets the information for a single SQL warehouse.

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

Lists all SQL warehouses that a user has access to.

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

Creates a new SQL warehouse.

```sql
INSERT INTO databricks_workspace.sql.warehouses (
auto_stop_mins,
channel,
cluster_size,
creator_name,
enable_photon,
enable_serverless_compute,
instance_profile_arn,
max_num_clusters,
min_num_clusters,
name,
spot_instance_policy,
tags,
warehouse_type,
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

Updates the configuration for a SQL warehouse.

```sql
REPLACE databricks_workspace.sql.warehouses
SET 
auto_stop_mins = '{{ auto_stop_mins }}',
channel = '{{ channel }}',
cluster_size = '{{ cluster_size }}',
creator_name = '{{ creator_name }}',
enable_photon = '{{ enable_photon }}',
enable_serverless_compute = '{{ enable_serverless_compute }}',
instance_profile_arn = '{{ instance_profile_arn }}',
max_num_clusters = '{{ max_num_clusters }}',
min_num_clusters = '{{ min_num_clusters }}',
name = '{{ name }}',
spot_instance_policy = '{{ spot_instance_policy }}',
tags = '{{ tags }}',
warehouse_type = '{{ warehouse_type }}'
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

Deletes a SQL warehouse.

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

Starts a SQL warehouse.

```sql
EXEC databricks_workspace.sql.warehouses.start 
@id='{{ id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops a SQL warehouse.

```sql
EXEC databricks_workspace.sql.warehouses.stop 
@id='{{ id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

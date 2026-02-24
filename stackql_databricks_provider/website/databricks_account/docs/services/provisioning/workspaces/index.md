---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - provisioning
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.workspaces" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="workspaces_get"
    values={[
        { label: 'workspaces_get', value: 'workspaces_get' },
        { label: 'workspaces_list', value: 'workspaces_list' }
    ]}
>
<TabItem value="workspaces_get">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "credentials_id",
    "type": "string",
    "description": "ID of the workspace's credential configuration object."
  },
  {
    "name": "managed_services_customer_managed_key_id",
    "type": "string",
    "description": "ID of the key configuration for encrypting managed services."
  },
  {
    "name": "network_connectivity_config_id",
    "type": "string",
    "description": "The object ID of network connectivity config."
  },
  {
    "name": "network_id",
    "type": "string",
    "description": "If this workspace is BYO VPC, then the network_id will be populated. If this workspace is not BYO VPC, then the network_id will be empty."
  },
  {
    "name": "private_access_settings_id",
    "type": "string",
    "description": "ID of the workspace's private access settings object. Only used for PrivateLink. You must specify this ID if you are using [AWS PrivateLink] for either front-end (user-to-workspace connection), back-end (data plane to control plane connection), or both connection types. Before configuring PrivateLink, read the [Databricks article about PrivateLink].\", [AWS PrivateLink]: https://aws.amazon.com/privatelink/ [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"
  },
  {
    "name": "storage_configuration_id",
    "type": "string",
    "description": "ID of the workspace's storage configuration object."
  },
  {
    "name": "storage_customer_managed_key_id",
    "type": "string",
    "description": "ID of the key configuration for encrypting workspace storage."
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "A unique integer ID for the workspace"
  },
  {
    "name": "deployment_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "workspace_name",
    "type": "string",
    "description": "The human-readable name of the workspace."
  },
  {
    "name": "aws_region",
    "type": "string",
    "description": ""
  },
  {
    "name": "azure_workspace_info",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "resource_group",
        "type": "string",
        "description": ""
      },
      {
        "name": "subscription_id",
        "type": "string",
        "description": "Azure Subscription ID"
      }
    ]
  },
  {
    "name": "cloud",
    "type": "string",
    "description": "The cloud name. This field can have values like `azure`, `gcp`."
  },
  {
    "name": "cloud_resource_container",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "gcp",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "project_id",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "compute_mode",
    "type": "string",
    "description": "The compute mode of the workspace. (HYBRID, SERVERLESS)"
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the workspace was created."
  },
  {
    "name": "custom_tags",
    "type": "object",
    "description": "The custom tags key-value pairing that is attached to this workspace. The key-value pair is a string of utf-8 characters. The value can be an empty string, with maximum length of 255 characters. The key can be of maximum length of 127 characters, and cannot be empty."
  },
  {
    "name": "expected_workspace_status",
    "type": "string",
    "description": "A client owned field used to indicate the workspace status that the client expects to be in. For now this is only used to unblock Temporal workflow for GCP least privileged workspace. (BANNED, CANCELLING, FAILED, NOT_PROVISIONED, PROVISIONING, RUNNING)"
  },
  {
    "name": "gcp_managed_network_config",
    "type": "object",
    "description": "The network configuration for the workspace.",
    "children": [
      {
        "name": "gke_cluster_pod_ip_range",
        "type": "string",
        "description": "The IP range that will be used to allocate GKE cluster Pods from."
      },
      {
        "name": "gke_cluster_service_ip_range",
        "type": "string",
        "description": "The IP range that will be used to allocate GKE cluster Services from."
      },
      {
        "name": "subnet_cidr",
        "type": "string",
        "description": "The IP range which will be used to allocate GKE cluster nodes from. Note: Pods, services and master IP range must be mutually exclusive."
      }
    ]
  },
  {
    "name": "gke_config",
    "type": "object",
    "description": "The configurations of the GKE cluster used by the GCP workspace.",
    "children": [
      {
        "name": "connectivity_type",
        "type": "string",
        "description": "The type of network connectivity of the GKE cluster. (PRIVATE_NODE_PUBLIC_MASTER, PUBLIC_NODE_PUBLIC_MASTER)"
      },
      {
        "name": "master_ip_range",
        "type": "string",
        "description": "The IP range that will be used to allocate GKE cluster master resources from. This field must not be set if gke_cluster_type=PUBLIC_NODE_PUBLIC_MASTER."
      }
    ]
  },
  {
    "name": "location",
    "type": "string",
    "description": "The Google Cloud region of the workspace data plane in your Google account (for example, `us-east4`)."
  },
  {
    "name": "network",
    "type": "object",
    "description": "The network configuration for the workspace. DEPRECATED. Use `network_id` instead.",
    "children": [
      {
        "name": "gcp_common_network_config",
        "type": "object",
        "description": "The shared network config for GCP workspace. This object has common network configurations that are network attributions of a workspace. This object is input-only.",
        "children": [
          {
            "name": "gke_cluster_master_ip_range",
            "type": "string",
            "description": "The IP range that will be used to allocate GKE cluster master resources from. This field must not be set if gke_cluster_type=PUBLIC_NODE_PUBLIC_MASTER."
          },
          {
            "name": "gke_connectivity_type",
            "type": "string",
            "description": "The type of network connectivity of the GKE cluster. (PRIVATE_NODE_PUBLIC_MASTER, PUBLIC_NODE_PUBLIC_MASTER)"
          }
        ]
      },
      {
        "name": "gcp_managed_network_config",
        "type": "object",
        "description": "The network configuration for the workspace.",
        "children": [
          {
            "name": "gke_cluster_pod_ip_range",
            "type": "string",
            "description": "The IP range that will be used to allocate GKE cluster Pods from."
          },
          {
            "name": "gke_cluster_service_ip_range",
            "type": "string",
            "description": "The IP range that will be used to allocate GKE cluster Services from."
          },
          {
            "name": "subnet_cidr",
            "type": "string",
            "description": "The IP range which will be used to allocate GKE cluster nodes from. Note: Pods, services and master IP range must be mutually exclusive."
          }
        ]
      },
      {
        "name": "network_id",
        "type": "string",
        "description": "The ID of the network object, if the workspace is a BYOVPC workspace. This should apply to workspaces on all clouds in internal services. In accounts-rest-api, user will use workspace.network_id for input and output instead. Currently (2021-06-19) the network ID is only used by GCP."
      }
    ]
  },
  {
    "name": "pricing_tier",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (COMMUNITY_EDITION, DEDICATED, ENTERPRISE, PREMIUM, STANDARD, UNKNOWN)"
  },
  {
    "name": "storage_mode",
    "type": "string",
    "description": "The storage mode of the workspace. (CUSTOMER_HOSTED, DEFAULT_STORAGE)"
  },
  {
    "name": "workspace_status",
    "type": "string",
    "description": "The status of a workspace (BANNED, CANCELLING, FAILED, NOT_PROVISIONED, PROVISIONING, RUNNING)"
  },
  {
    "name": "workspace_status_message",
    "type": "string",
    "description": "Message describing the current workspace status."
  }
]} />
</TabItem>
<TabItem value="workspaces_list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "credentials_id",
    "type": "string",
    "description": "ID of the workspace's credential configuration object."
  },
  {
    "name": "managed_services_customer_managed_key_id",
    "type": "string",
    "description": "ID of the key configuration for encrypting managed services."
  },
  {
    "name": "network_connectivity_config_id",
    "type": "string",
    "description": "The object ID of network connectivity config."
  },
  {
    "name": "network_id",
    "type": "string",
    "description": "If this workspace is BYO VPC, then the network_id will be populated. If this workspace is not BYO VPC, then the network_id will be empty."
  },
  {
    "name": "private_access_settings_id",
    "type": "string",
    "description": "ID of the workspace's private access settings object. Only used for PrivateLink. You must specify this ID if you are using [AWS PrivateLink] for either front-end (user-to-workspace connection), back-end (data plane to control plane connection), or both connection types. Before configuring PrivateLink, read the [Databricks article about PrivateLink].\", [AWS PrivateLink]: https://aws.amazon.com/privatelink/ [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html"
  },
  {
    "name": "storage_configuration_id",
    "type": "string",
    "description": "ID of the workspace's storage configuration object."
  },
  {
    "name": "storage_customer_managed_key_id",
    "type": "string",
    "description": "ID of the key configuration for encrypting workspace storage."
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "A unique integer ID for the workspace"
  },
  {
    "name": "deployment_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "workspace_name",
    "type": "string",
    "description": "The human-readable name of the workspace."
  },
  {
    "name": "aws_region",
    "type": "string",
    "description": ""
  },
  {
    "name": "azure_workspace_info",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "resource_group",
        "type": "string",
        "description": ""
      },
      {
        "name": "subscription_id",
        "type": "string",
        "description": "Azure Subscription ID"
      }
    ]
  },
  {
    "name": "cloud",
    "type": "string",
    "description": "The cloud name. This field can have values like `azure`, `gcp`."
  },
  {
    "name": "cloud_resource_container",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "gcp",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "project_id",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "compute_mode",
    "type": "string",
    "description": "The compute mode of the workspace. (HYBRID, SERVERLESS)"
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the workspace was created."
  },
  {
    "name": "custom_tags",
    "type": "object",
    "description": "The custom tags key-value pairing that is attached to this workspace. The key-value pair is a string of utf-8 characters. The value can be an empty string, with maximum length of 255 characters. The key can be of maximum length of 127 characters, and cannot be empty."
  },
  {
    "name": "expected_workspace_status",
    "type": "string",
    "description": "A client owned field used to indicate the workspace status that the client expects to be in. For now this is only used to unblock Temporal workflow for GCP least privileged workspace. (BANNED, CANCELLING, FAILED, NOT_PROVISIONED, PROVISIONING, RUNNING)"
  },
  {
    "name": "gcp_managed_network_config",
    "type": "object",
    "description": "The network configuration for the workspace.",
    "children": [
      {
        "name": "gke_cluster_pod_ip_range",
        "type": "string",
        "description": "The IP range that will be used to allocate GKE cluster Pods from."
      },
      {
        "name": "gke_cluster_service_ip_range",
        "type": "string",
        "description": "The IP range that will be used to allocate GKE cluster Services from."
      },
      {
        "name": "subnet_cidr",
        "type": "string",
        "description": "The IP range which will be used to allocate GKE cluster nodes from. Note: Pods, services and master IP range must be mutually exclusive."
      }
    ]
  },
  {
    "name": "gke_config",
    "type": "object",
    "description": "The configurations of the GKE cluster used by the GCP workspace.",
    "children": [
      {
        "name": "connectivity_type",
        "type": "string",
        "description": "The type of network connectivity of the GKE cluster. (PRIVATE_NODE_PUBLIC_MASTER, PUBLIC_NODE_PUBLIC_MASTER)"
      },
      {
        "name": "master_ip_range",
        "type": "string",
        "description": "The IP range that will be used to allocate GKE cluster master resources from. This field must not be set if gke_cluster_type=PUBLIC_NODE_PUBLIC_MASTER."
      }
    ]
  },
  {
    "name": "location",
    "type": "string",
    "description": "The Google Cloud region of the workspace data plane in your Google account (for example, `us-east4`)."
  },
  {
    "name": "network",
    "type": "object",
    "description": "The network configuration for the workspace. DEPRECATED. Use `network_id` instead.",
    "children": [
      {
        "name": "gcp_common_network_config",
        "type": "object",
        "description": "The shared network config for GCP workspace. This object has common network configurations that are network attributions of a workspace. This object is input-only.",
        "children": [
          {
            "name": "gke_cluster_master_ip_range",
            "type": "string",
            "description": "The IP range that will be used to allocate GKE cluster master resources from. This field must not be set if gke_cluster_type=PUBLIC_NODE_PUBLIC_MASTER."
          },
          {
            "name": "gke_connectivity_type",
            "type": "string",
            "description": "The type of network connectivity of the GKE cluster. (PRIVATE_NODE_PUBLIC_MASTER, PUBLIC_NODE_PUBLIC_MASTER)"
          }
        ]
      },
      {
        "name": "gcp_managed_network_config",
        "type": "object",
        "description": "The network configuration for the workspace.",
        "children": [
          {
            "name": "gke_cluster_pod_ip_range",
            "type": "string",
            "description": "The IP range that will be used to allocate GKE cluster Pods from."
          },
          {
            "name": "gke_cluster_service_ip_range",
            "type": "string",
            "description": "The IP range that will be used to allocate GKE cluster Services from."
          },
          {
            "name": "subnet_cidr",
            "type": "string",
            "description": "The IP range which will be used to allocate GKE cluster nodes from. Note: Pods, services and master IP range must be mutually exclusive."
          }
        ]
      },
      {
        "name": "network_id",
        "type": "string",
        "description": "The ID of the network object, if the workspace is a BYOVPC workspace. This should apply to workspaces on all clouds in internal services. In accounts-rest-api, user will use workspace.network_id for input and output instead. Currently (2021-06-19) the network ID is only used by GCP."
      }
    ]
  },
  {
    "name": "pricing_tier",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (COMMUNITY_EDITION, DEDICATED, ENTERPRISE, PREMIUM, STANDARD, UNKNOWN)"
  },
  {
    "name": "storage_mode",
    "type": "string",
    "description": "The storage mode of the workspace. (CUSTOMER_HOSTED, DEFAULT_STORAGE)"
  },
  {
    "name": "workspace_status",
    "type": "string",
    "description": "The status of a workspace (BANNED, CANCELLING, FAILED, NOT_PROVISIONED, PROVISIONING, RUNNING)"
  },
  {
    "name": "workspace_status_message",
    "type": "string",
    "description": "Message describing the current workspace status."
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
    <td><a href="#workspaces_get"><CopyableCode code="workspaces_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a></td>
    <td></td>
    <td>Gets information including status for a Databricks workspace, specified by ID. In the response, the</td>
</tr>
<tr>
    <td><a href="#workspaces_list"><CopyableCode code="workspaces_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists Databricks workspaces for an account.</td>
</tr>
<tr>
    <td><a href="#workspaces_create"><CopyableCode code="workspaces_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a new workspace using a credential configuration and a storage configuration, an optional</td>
</tr>
<tr>
    <td><a href="#workspaces_update"><CopyableCode code="workspaces_update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-customer_facing_workspace"><code>customer_facing_workspace</code></a></td>
    <td><a href="#parameter-update_mask"><code>update_mask</code></a></td>
    <td>Updates a workspace.</td>
</tr>
<tr>
    <td><a href="#workspaces_delete"><CopyableCode code="workspaces_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a></td>
    <td></td>
    <td>Deletes a Databricks workspace, both specified by ID.</td>
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
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_id">
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>integer</code></td>
    <td>:returns: :class:`Workspace`</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="workspaces_get"
    values={[
        { label: 'workspaces_get', value: 'workspaces_get' },
        { label: 'workspaces_list', value: 'workspaces_list' }
    ]}
>
<TabItem value="workspaces_get">

Gets information including status for a Databricks workspace, specified by ID. In the response, the

```sql
SELECT
account_id,
credentials_id,
managed_services_customer_managed_key_id,
network_connectivity_config_id,
network_id,
private_access_settings_id,
storage_configuration_id,
storage_customer_managed_key_id,
workspace_id,
deployment_name,
workspace_name,
aws_region,
azure_workspace_info,
cloud,
cloud_resource_container,
compute_mode,
creation_time,
custom_tags,
expected_workspace_status,
gcp_managed_network_config,
gke_config,
location,
network,
pricing_tier,
storage_mode,
workspace_status,
workspace_status_message
FROM databricks_account.provisioning.workspaces
WHERE account_id = '{{ account_id }}' -- required
AND workspace_id = '{{ workspace_id }}' -- required
;
```
</TabItem>
<TabItem value="workspaces_list">

Lists Databricks workspaces for an account.

```sql
SELECT
account_id,
credentials_id,
managed_services_customer_managed_key_id,
network_connectivity_config_id,
network_id,
private_access_settings_id,
storage_configuration_id,
storage_customer_managed_key_id,
workspace_id,
deployment_name,
workspace_name,
aws_region,
azure_workspace_info,
cloud,
cloud_resource_container,
compute_mode,
creation_time,
custom_tags,
expected_workspace_status,
gcp_managed_network_config,
gke_config,
location,
network,
pricing_tier,
storage_mode,
workspace_status,
workspace_status_message
FROM databricks_account.provisioning.workspaces
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="workspaces_create"
    values={[
        { label: 'workspaces_create', value: 'workspaces_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workspaces_create">

Creates a new workspace using a credential configuration and a storage configuration, an optional

```sql
INSERT INTO databricks_account.provisioning.workspaces (
aws_region,
cloud,
cloud_resource_container,
compute_mode,
credentials_id,
custom_tags,
deployment_name,
gcp_managed_network_config,
gke_config,
location,
managed_services_customer_managed_key_id,
network_connectivity_config_id,
network_id,
pricing_tier,
private_access_settings_id,
storage_configuration_id,
storage_customer_managed_key_id,
workspace_name,
account_id
)
SELECT 
'{{ aws_region }}',
'{{ cloud }}',
'{{ cloud_resource_container }}',
'{{ compute_mode }}',
'{{ credentials_id }}',
'{{ custom_tags }}',
'{{ deployment_name }}',
'{{ gcp_managed_network_config }}',
'{{ gke_config }}',
'{{ location }}',
'{{ managed_services_customer_managed_key_id }}',
'{{ network_connectivity_config_id }}',
'{{ network_id }}',
'{{ pricing_tier }}',
'{{ private_access_settings_id }}',
'{{ storage_configuration_id }}',
'{{ storage_customer_managed_key_id }}',
'{{ workspace_name }}',
'{{ account_id }}'
RETURNING
account_id,
credentials_id,
managed_services_customer_managed_key_id,
network_connectivity_config_id,
network_id,
private_access_settings_id,
storage_configuration_id,
storage_customer_managed_key_id,
workspace_id,
deployment_name,
workspace_name,
aws_region,
azure_workspace_info,
cloud,
cloud_resource_container,
compute_mode,
creation_time,
custom_tags,
expected_workspace_status,
gcp_managed_network_config,
gke_config,
location,
network,
pricing_tier,
storage_mode,
workspace_status,
workspace_status_message
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: workspaces
  props:
    - name: account_id
      value: string
      description: Required parameter for the workspaces resource.
    - name: aws_region
      value: string
      description: |
        :param cloud: str (optional) The cloud name. This field always has the value `gcp`.
    - name: cloud
      value: string
    - name: cloud_resource_container
      value: object
      description: |
        :param compute_mode: :class:`CustomerFacingComputeMode` (optional) If the compute mode is `SERVERLESS`, a serverless workspace is created that comes pre-configured with serverless compute and default storage, providing a fully-managed, enterprise-ready SaaS experience. This means you don't need to provide any resources managed by you, such as credentials, storage, or network. If the compute mode is `HYBRID` (which is the default option), a classic workspace is created that uses customer-managed resources.
      props:
      - name: gcp
        value: object
        props:
        - name: project_id
          value: string
    - name: compute_mode
      value: string
      description: |
        Corresponds to compute mode defined here:
        https://src.dev.databricks.com/databricks/universe@9076536b18479afd639d1c1f9dd5a59f72215e69/-/blob/central/api/common.proto?L872
    - name: credentials_id
      value: string
      description: |
        ID of the workspace's credential configuration object.
    - name: custom_tags
      value: object
      description: |
        The custom tags key-value pairing that is attached to this workspace. The key-value pair is a string of utf-8 characters. The value can be an empty string, with maximum length of 255 characters. The key can be of maximum length of 127 characters, and cannot be empty.
    - name: deployment_name
      value: string
      description: |
        The deployment name defines part of the subdomain for the workspace. The workspace URL for the web application and REST APIs is <workspace-deployment-name>.cloud.databricks.com. For example, if the deployment name is abcsales, your workspace URL will be https://abcsales.cloud.databricks.com. Hyphens are allowed. This property supports only the set of characters that are allowed in a subdomain. To set this value, you must have a deployment name prefix. Contact your Databricks account team to add an account deployment name prefix to your account. Workspace deployment names follow the account prefix and a hyphen. For example, if your account's deployment prefix is acme and the workspace deployment name is workspace-1, the JSON response for the deployment_name field becomes acme-workspace-1. The workspace URL would be acme-workspace-1.cloud.databricks.com. You can also set the deployment_name to the reserved keyword EMPTY if you want the deployment name to only include the deployment prefix. For example, if your account's deployment prefix is acme and the workspace deployment name is EMPTY, the deployment_name becomes acme only and the workspace URL is acme.cloud.databricks.com. This value must be unique across all non-deleted deployments across all AWS regions. If a new workspace omits this property, the server generates a unique deployment name for you with the pattern dbc-xxxxxxxx-xxxx.
    - name: gcp_managed_network_config
      value: object
      description: |
        :param gke_config: :class:`GkeConfig` (optional)
      props:
      - name: gke_cluster_pod_ip_range
        value: string
        description: |
          The IP range that will be used to allocate GKE cluster Pods from.
      - name: gke_cluster_service_ip_range
        value: string
        description: |
          The IP range that will be used to allocate GKE cluster Services from.
      - name: subnet_cidr
        value: string
        description: |
          The IP range which will be used to allocate GKE cluster nodes from. Note: Pods, services and master IP range must be mutually exclusive.
    - name: gke_config
      value: object
      description: |
        The configurations of the GKE cluster used by the GCP workspace.
      props:
      - name: connectivity_type
        value: string
        description: |
          The type of network connectivity of the GKE cluster.
      - name: master_ip_range
        value: string
        description: |
          The IP range that will be used to allocate GKE cluster master resources from. This field must not be set if gke_cluster_type=PUBLIC_NODE_PUBLIC_MASTER.
    - name: location
      value: string
      description: |
        The Google Cloud region of the workspace data plane in your Google account (for example, `us-east4`).
    - name: managed_services_customer_managed_key_id
      value: string
      description: |
        The ID of the workspace's managed services encryption key configuration object. This is used to help protect and control access to the workspace's notebooks, secrets, Databricks SQL queries, and query history. The provided key configuration object property use_cases must contain MANAGED_SERVICES.
    - name: network_connectivity_config_id
      value: string
      description: |
        The object ID of network connectivity config. Once assigned, the workspace serverless compute resources use the same set of stable IP CIDR blocks and optional private link to access your resources.
    - name: network_id
      value: string
      description: |
        The ID of the workspace's network configuration object. To use AWS PrivateLink, this field is required.
    - name: pricing_tier
      value: string
      description: |
        :param private_access_settings_id: str (optional) ID of the workspace's private access settings object. Only used for PrivateLink. You must specify this ID if you are using [AWS PrivateLink] for either front-end (user-to-workspace connection), back-end (data plane to control plane connection), or both connection types. Before configuring PrivateLink, read the [Databricks article about PrivateLink].", [AWS PrivateLink]: https://aws.amazon.com/privatelink/ [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
    - name: private_access_settings_id
      value: string
    - name: storage_configuration_id
      value: string
      description: |
        ID of the workspace's storage configuration object.
    - name: storage_customer_managed_key_id
      value: string
      description: |
        The ID of the workspace's storage encryption key configuration object. This is used to encrypt the workspace's root S3 bucket (root DBFS and system data) and, optionally, cluster EBS volumes. The provided key configuration object property use_cases must contain STORAGE.
    - name: workspace_name
      value: string
      description: |
        The human-readable name of the workspace.
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="workspaces_update"
    values={[
        { label: 'workspaces_update', value: 'workspaces_update' }
    ]}
>
<TabItem value="workspaces_update">

Updates a workspace.

```sql
UPDATE databricks_account.provisioning.workspaces
SET 
customer_facing_workspace = '{{ customer_facing_workspace }}'
WHERE 
account_id = '{{ account_id }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND customer_facing_workspace = '{{ customer_facing_workspace }}' --required
AND update_mask = '{{ update_mask}}'
RETURNING
account_id,
credentials_id,
managed_services_customer_managed_key_id,
network_connectivity_config_id,
network_id,
private_access_settings_id,
storage_configuration_id,
storage_customer_managed_key_id,
workspace_id,
deployment_name,
workspace_name,
aws_region,
azure_workspace_info,
cloud,
cloud_resource_container,
compute_mode,
creation_time,
custom_tags,
expected_workspace_status,
gcp_managed_network_config,
gke_config,
location,
network,
pricing_tier,
storage_mode,
workspace_status,
workspace_status_message;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="workspaces_delete"
    values={[
        { label: 'workspaces_delete', value: 'workspaces_delete' }
    ]}
>
<TabItem value="workspaces_delete">

Deletes a Databricks workspace, both specified by ID.

```sql
DELETE FROM databricks_account.provisioning.workspaces
WHERE account_id = '{{ account_id }}' --required
AND workspace_id = '{{ workspace_id }}' --required
;
```
</TabItem>
</Tabs>

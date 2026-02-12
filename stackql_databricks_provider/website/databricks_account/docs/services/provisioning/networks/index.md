---
title: networks
hide_title: false
hide_table_of_contents: false
keywords:
  - networks
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

Creates, updates, deletes, gets or lists a <code>networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.networks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="networks_get"
    values={[
        { label: 'networks_get', value: 'networks_get' },
        { label: 'networks_list', value: 'networks_list' }
    ]}
>
<TabItem value="networks_get">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "network_id",
    "type": "string",
    "description": "The Databricks network configuration ID."
  },
  {
    "name": "vpc_id",
    "type": "string",
    "description": "The ID of the VPC associated with this network configuration. VPC IDs can be used in multiple networks."
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "Workspace ID associated with this network configuration."
  },
  {
    "name": "network_name",
    "type": "string",
    "description": "The human-readable name of the network configuration."
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the network was created."
  },
  {
    "name": "error_messages",
    "type": "array",
    "description": "Array of error messages about the network configuration.",
    "children": [
      {
        "name": "error_message",
        "type": "string",
        "description": ""
      },
      {
        "name": "error_type",
        "type": "string",
        "description": "ErrorType and WarningType are used to represent the type of error or warning by NetworkHealth<br />and NetworkWarning defined in central/api/accounts/accounts.proto"
      }
    ]
  },
  {
    "name": "gcp_network_info",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "network_project_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "vpc_id",
        "type": "string",
        "description": "The customer-provided VPC ID."
      },
      {
        "name": "subnet_id",
        "type": "string",
        "description": "The customer-provided Subnet ID that will be available to Clusters in Workspaces using this Network."
      },
      {
        "name": "subnet_region",
        "type": "string",
        "description": ""
      },
      {
        "name": "pod_ip_range_name",
        "type": "string",
        "description": "Name of the secondary range within the subnet that will be used by GKE as Pod IP range. This is BYO VPC specific. DB VPC uses network.getGcpManagedNetworkConfig.getGkeClusterPodIpRange"
      },
      {
        "name": "service_ip_range_name",
        "type": "string",
        "description": "Name of the secondary range within the subnet that will be used by GKE as Service IP range."
      }
    ]
  },
  {
    "name": "security_group_ids",
    "type": "array",
    "description": "IDs of one to five security groups associated with this network. Security group IDs **cannot** be used in multiple network configurations."
  },
  {
    "name": "subnet_ids",
    "type": "array",
    "description": "IDs of at least two subnets associated with this network. Subnet IDs **cannot** be used in multiple network configurations."
  },
  {
    "name": "vpc_endpoints",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "dataplane_relay",
        "type": "array",
        "description": ""
      },
      {
        "name": "rest_api",
        "type": "array",
        "description": "The VPC endpoint ID used by this network to access the Databricks REST API."
      }
    ]
  },
  {
    "name": "vpc_status",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
  },
  {
    "name": "warning_messages",
    "type": "array",
    "description": "Array of warning messages about the network configuration.",
    "children": [
      {
        "name": "warning_message",
        "type": "string",
        "description": ""
      },
      {
        "name": "warning_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      }
    ]
  }
]} />
</TabItem>
<TabItem value="networks_list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "network_id",
    "type": "string",
    "description": "The Databricks network configuration ID."
  },
  {
    "name": "vpc_id",
    "type": "string",
    "description": "The ID of the VPC associated with this network configuration. VPC IDs can be used in multiple networks."
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "Workspace ID associated with this network configuration."
  },
  {
    "name": "network_name",
    "type": "string",
    "description": "The human-readable name of the network configuration."
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the network was created."
  },
  {
    "name": "error_messages",
    "type": "array",
    "description": "Array of error messages about the network configuration.",
    "children": [
      {
        "name": "error_message",
        "type": "string",
        "description": ""
      },
      {
        "name": "error_type",
        "type": "string",
        "description": "ErrorType and WarningType are used to represent the type of error or warning by NetworkHealth<br />and NetworkWarning defined in central/api/accounts/accounts.proto"
      }
    ]
  },
  {
    "name": "gcp_network_info",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "network_project_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "vpc_id",
        "type": "string",
        "description": "The customer-provided VPC ID."
      },
      {
        "name": "subnet_id",
        "type": "string",
        "description": "The customer-provided Subnet ID that will be available to Clusters in Workspaces using this Network."
      },
      {
        "name": "subnet_region",
        "type": "string",
        "description": ""
      },
      {
        "name": "pod_ip_range_name",
        "type": "string",
        "description": "Name of the secondary range within the subnet that will be used by GKE as Pod IP range. This is BYO VPC specific. DB VPC uses network.getGcpManagedNetworkConfig.getGkeClusterPodIpRange"
      },
      {
        "name": "service_ip_range_name",
        "type": "string",
        "description": "Name of the secondary range within the subnet that will be used by GKE as Service IP range."
      }
    ]
  },
  {
    "name": "security_group_ids",
    "type": "array",
    "description": "IDs of one to five security groups associated with this network. Security group IDs **cannot** be used in multiple network configurations."
  },
  {
    "name": "subnet_ids",
    "type": "array",
    "description": "IDs of at least two subnets associated with this network. Subnet IDs **cannot** be used in multiple network configurations."
  },
  {
    "name": "vpc_endpoints",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "dataplane_relay",
        "type": "array",
        "description": ""
      },
      {
        "name": "rest_api",
        "type": "array",
        "description": "The VPC endpoint ID used by this network to access the Databricks REST API."
      }
    ]
  },
  {
    "name": "vpc_status",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
  },
  {
    "name": "warning_messages",
    "type": "array",
    "description": "Array of warning messages about the network configuration.",
    "children": [
      {
        "name": "warning_message",
        "type": "string",
        "description": ""
      },
      {
        "name": "warning_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
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
    <td><a href="#networks_get"><CopyableCode code="networks_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_id"><code>network_id</code></a></td>
    <td></td>
    <td>Gets a Databricks network configuration, which represents a cloud VPC and its resources.</td>
</tr>
<tr>
    <td><a href="#networks_list"><CopyableCode code="networks_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists Databricks network configurations for an account.</td>
</tr>
<tr>
    <td><a href="#networks_create"><CopyableCode code="networks_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a Databricks network configuration that represents an VPC and its resources. The VPC will be</td>
</tr>
<tr>
    <td><a href="#networks_delete"><CopyableCode code="networks_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_id"><code>network_id</code></a></td>
    <td></td>
    <td>Deletes a Databricks network configuration, which represents a cloud VPC and its resources. You cannot</td>
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
<tr id="parameter-network_id">
    <td><CopyableCode code="network_id" /></td>
    <td><code>string</code></td>
    <td>Databricks Account API network configuration ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="networks_get"
    values={[
        { label: 'networks_get', value: 'networks_get' },
        { label: 'networks_list', value: 'networks_list' }
    ]}
>
<TabItem value="networks_get">

Gets a Databricks network configuration, which represents a cloud VPC and its resources.

```sql
SELECT
account_id,
network_id,
vpc_id,
workspace_id,
network_name,
creation_time,
error_messages,
gcp_network_info,
security_group_ids,
subnet_ids,
vpc_endpoints,
vpc_status,
warning_messages
FROM databricks_account.provisioning.networks
WHERE account_id = '{{ account_id }}' -- required
AND network_id = '{{ network_id }}' -- required
;
```
</TabItem>
<TabItem value="networks_list">

Lists Databricks network configurations for an account.

```sql
SELECT
account_id,
network_id,
vpc_id,
workspace_id,
network_name,
creation_time,
error_messages,
gcp_network_info,
security_group_ids,
subnet_ids,
vpc_endpoints,
vpc_status,
warning_messages
FROM databricks_account.provisioning.networks
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="networks_create"
    values={[
        { label: 'networks_create', value: 'networks_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="networks_create">

Creates a Databricks network configuration that represents an VPC and its resources. The VPC will be

```sql
INSERT INTO databricks_account.provisioning.networks (
data__gcp_network_info,
data__network_name,
data__security_group_ids,
data__subnet_ids,
data__vpc_endpoints,
data__vpc_id,
account_id
)
SELECT 
'{{ gcp_network_info }}',
'{{ network_name }}',
'{{ security_group_ids }}',
'{{ subnet_ids }}',
'{{ vpc_endpoints }}',
'{{ vpc_id }}',
'{{ account_id }}'
RETURNING
account_id,
network_id,
vpc_id,
workspace_id,
network_name,
creation_time,
error_messages,
gcp_network_info,
security_group_ids,
subnet_ids,
vpc_endpoints,
vpc_status,
warning_messages
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: networks
  props:
    - name: account_id
      value: string
      description: Required parameter for the networks resource.
    - name: gcp_network_info
      value: string
      description: |
        :param network_name: str (optional) The human-readable name of the network configuration.
    - name: network_name
      value: string
    - name: security_group_ids
      value: string
      description: |
        IDs of one to five security groups associated with this network. Security group IDs **cannot** be used in multiple network configurations.
    - name: subnet_ids
      value: string
      description: |
        IDs of at least two subnets associated with this network. Subnet IDs **cannot** be used in multiple network configurations.
    - name: vpc_endpoints
      value: string
      description: |
        :param vpc_id: str (optional) The ID of the VPC associated with this network configuration. VPC IDs can be used in multiple networks.
    - name: vpc_id
      value: string
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="networks_delete"
    values={[
        { label: 'networks_delete', value: 'networks_delete' }
    ]}
>
<TabItem value="networks_delete">

Deletes a Databricks network configuration, which represents a cloud VPC and its resources. You cannot

```sql
DELETE FROM databricks_account.provisioning.networks
WHERE account_id = '{{ account_id }}' --required
AND network_id = '{{ network_id }}' --required
;
```
</TabItem>
</Tabs>

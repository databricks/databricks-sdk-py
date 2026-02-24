---
title: network_connectivity
hide_title: false
hide_table_of_contents: false
keywords:
  - network_connectivity
  - settings
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

Creates, updates, deletes, gets or lists a <code>network_connectivity</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_connectivity" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.network_connectivity" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_network_connectivity_configuration"
    values={[
        { label: 'get_network_connectivity_configuration', value: 'get_network_connectivity_configuration' },
        { label: 'list_network_connectivity_configurations', value: 'list_network_connectivity_configurations' }
    ]}
>
<TabItem value="get_network_connectivity_configuration">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the network connectivity configuration. The name can contain alphanumeric characters, hyphens, and underscores. The length must be between 3 and 30 characters. The name must match the regular expression ^[0-9a-zA-Z-_]&#123;3,30&#125;$"
  },
  {
    "name": "account_id",
    "type": "string",
    "description": "Your Databricks account ID. You can find your account ID in your Databricks accounts console."
  },
  {
    "name": "network_connectivity_config_id",
    "type": "string",
    "description": "Databricks network connectivity configuration ID."
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when this object was created."
  },
  {
    "name": "egress_config",
    "type": "object",
    "description": "The network connectivity rules that apply to network traffic from your serverless compute resources.",
    "children": [
      {
        "name": "default_rules",
        "type": "object",
        "description": "Default rules don't have specific targets.",
        "children": [
          {
            "name": "aws_stable_ip_rule",
            "type": "object",
            "description": "The stable AWS IP CIDR blocks. You can use these to configure the firewall of your resources to<br />    allow traffic from your Databricks workspace.",
            "children": [
              {
                "name": "cidr_blocks",
                "type": "array",
                "description": "The list of stable IP CIDR blocks from which Databricks network traffic originates when accessing your resources."
              }
            ]
          },
          {
            "name": "azure_service_endpoint_rule",
            "type": "object",
            "description": "The stable Azure service endpoints. You can configure the firewall of your Azure resources to<br />    allow traffic from your Databricks serverless compute resources.",
            "children": [
              {
                "name": "subnets",
                "type": "array",
                "description": "The list of subnets from which Databricks network traffic originates when accessing your Azure resources."
              },
              {
                "name": "target_region",
                "type": "string",
                "description": "The Azure region in which this service endpoint rule applies.."
              },
              {
                "name": "target_services",
                "type": "array",
                "description": "The Azure services to which this service endpoint rule applies to."
              }
            ]
          }
        ]
      },
      {
        "name": "target_rules",
        "type": "object",
        "description": "The network connectivity rules that configured for each destinations. These rules override default rules.",
        "children": [
          {
            "name": "aws_private_endpoint_rules",
            "type": "array",
            "description": "AWS private endpoint rule controls the AWS private endpoint based egress rules.",
            "children": [
              {
                "name": "account_id",
                "type": "string",
                "description": "Databricks account ID. You can find your account ID from the Accounts Console."
              },
              {
                "name": "connection_state",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CREATE_FAILED, CREATING, DISCONNECTED, ESTABLISHED, EXPIRED, PENDING, REJECTED)"
              },
              {
                "name": "creation_time",
                "type": "integer",
                "description": "Time in epoch milliseconds when this object was created."
              },
              {
                "name": "deactivated",
                "type": "boolean",
                "description": "Whether this private endpoint is deactivated."
              },
              {
                "name": "deactivated_at",
                "type": "integer",
                "description": "Time in epoch milliseconds when this object was deactivated."
              },
              {
                "name": "domain_names",
                "type": "array",
                "description": "Only used by private endpoints towards a VPC endpoint service for customer-managed VPC endpoint service. The target AWS resource FQDNs accessible via the VPC endpoint service. When updating this field, we perform full update on this field. Please ensure a full list of desired domain_names is provided."
              },
              {
                "name": "enabled",
                "type": "boolean",
                "description": "Only used by private endpoints towards an AWS S3 service. Update this field to activate/deactivate this private endpoint to allow egress access from serverless compute resources."
              },
              {
                "name": "endpoint_service",
                "type": "string",
                "description": "The full target AWS endpoint service name that connects to the destination resources of the private endpoint."
              },
              {
                "name": "error_message",
                "type": "string",
                "description": ""
              },
              {
                "name": "network_connectivity_config_id",
                "type": "string",
                "description": "The ID of a network connectivity configuration, which is the parent resource of this private endpoint rule object."
              },
              {
                "name": "resource_names",
                "type": "array",
                "description": "Only used by private endpoints towards AWS S3 service. The globally unique S3 bucket names that will be accessed via the VPC endpoint. The bucket names must be in the same region as the NCC/endpoint service. When updating this field, we perform full update on this field. Please ensure a full list of desired resource_names is provided."
              },
              {
                "name": "rule_id",
                "type": "string",
                "description": "The ID of a private endpoint rule."
              },
              {
                "name": "updated_time",
                "type": "integer",
                "description": "Time in epoch milliseconds when this object was updated."
              },
              {
                "name": "vpc_endpoint_id",
                "type": "string",
                "description": "The AWS VPC endpoint ID. You can use this ID to identify VPC endpoint created by Databricks."
              }
            ]
          },
          {
            "name": "azure_private_endpoint_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "connection_state",
                "type": "string",
                "description": "The current status of this private endpoint. The private endpoint rules are effective only if the connection state is ESTABLISHED. Remember that you must approve new endpoints on your resources in the Azure portal before they take effect. The possible values are: - INIT: (deprecated) The endpoint has been created and pending approval. - PENDING: The endpoint has been created and pending approval. - ESTABLISHED: The endpoint has been approved and is ready to use in your serverless compute resources. - REJECTED: Connection was rejected by the private link resource owner. - DISCONNECTED: Connection was removed by the private link resource owner, the private endpoint becomes informative and should be deleted for clean-up. - EXPIRED: If the endpoint was created but not approved in 14 days, it will be EXPIRED. (CREATE_FAILED, CREATING, DISCONNECTED, ESTABLISHED, EXPIRED, INIT, PENDING, REJECTED)"
              },
              {
                "name": "creation_time",
                "type": "integer",
                "description": "Time in epoch milliseconds when this object was created."
              },
              {
                "name": "deactivated",
                "type": "boolean",
                "description": "Whether this private endpoint is deactivated."
              },
              {
                "name": "deactivated_at",
                "type": "integer",
                "description": "Time in epoch milliseconds when this object was deactivated."
              },
              {
                "name": "domain_names",
                "type": "array",
                "description": "Not used by customer-managed private endpoint services. Domain names of target private link service. When updating this field, the full list of target domain_names must be specified."
              },
              {
                "name": "endpoint_name",
                "type": "string",
                "description": "The name of the Azure private endpoint resource."
              },
              {
                "name": "error_message",
                "type": "string",
                "description": ""
              },
              {
                "name": "group_id",
                "type": "string",
                "description": "Only used by private endpoints to Azure first-party services. The sub-resource type (group ID) of the target resource. Note that to connect to workspace root storage (root DBFS), you need two endpoints, one for blob and one for dfs."
              },
              {
                "name": "network_connectivity_config_id",
                "type": "string",
                "description": "The ID of a network connectivity configuration, which is the parent resource of this private endpoint rule object."
              },
              {
                "name": "resource_id",
                "type": "string",
                "description": "The Azure resource ID of the target resource."
              },
              {
                "name": "rule_id",
                "type": "string",
                "description": "The ID of a private endpoint rule."
              },
              {
                "name": "updated_time",
                "type": "integer",
                "description": "Time in epoch milliseconds when this object was updated."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "region",
    "type": "string",
    "description": "The region for the network connectivity configuration. Only workspaces in the same region can be attached to the network connectivity configuration."
  },
  {
    "name": "updated_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when this object was updated."
  }
]} />
</TabItem>
<TabItem value="list_network_connectivity_configurations">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the network connectivity configuration. The name can contain alphanumeric characters, hyphens, and underscores. The length must be between 3 and 30 characters. The name must match the regular expression ^[0-9a-zA-Z-_]&#123;3,30&#125;$"
  },
  {
    "name": "account_id",
    "type": "string",
    "description": "Your Databricks account ID. You can find your account ID in your Databricks accounts console."
  },
  {
    "name": "network_connectivity_config_id",
    "type": "string",
    "description": "Databricks network connectivity configuration ID."
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when this object was created."
  },
  {
    "name": "egress_config",
    "type": "object",
    "description": "The network connectivity rules that apply to network traffic from your serverless compute resources.",
    "children": [
      {
        "name": "default_rules",
        "type": "object",
        "description": "Default rules don't have specific targets.",
        "children": [
          {
            "name": "aws_stable_ip_rule",
            "type": "object",
            "description": "The stable AWS IP CIDR blocks. You can use these to configure the firewall of your resources to<br />    allow traffic from your Databricks workspace.",
            "children": [
              {
                "name": "cidr_blocks",
                "type": "array",
                "description": "The list of stable IP CIDR blocks from which Databricks network traffic originates when accessing your resources."
              }
            ]
          },
          {
            "name": "azure_service_endpoint_rule",
            "type": "object",
            "description": "The stable Azure service endpoints. You can configure the firewall of your Azure resources to<br />    allow traffic from your Databricks serverless compute resources.",
            "children": [
              {
                "name": "subnets",
                "type": "array",
                "description": "The list of subnets from which Databricks network traffic originates when accessing your Azure resources."
              },
              {
                "name": "target_region",
                "type": "string",
                "description": "The Azure region in which this service endpoint rule applies.."
              },
              {
                "name": "target_services",
                "type": "array",
                "description": "The Azure services to which this service endpoint rule applies to."
              }
            ]
          }
        ]
      },
      {
        "name": "target_rules",
        "type": "object",
        "description": "The network connectivity rules that configured for each destinations. These rules override default rules.",
        "children": [
          {
            "name": "aws_private_endpoint_rules",
            "type": "array",
            "description": "AWS private endpoint rule controls the AWS private endpoint based egress rules.",
            "children": [
              {
                "name": "account_id",
                "type": "string",
                "description": "Databricks account ID. You can find your account ID from the Accounts Console."
              },
              {
                "name": "connection_state",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CREATE_FAILED, CREATING, DISCONNECTED, ESTABLISHED, EXPIRED, PENDING, REJECTED)"
              },
              {
                "name": "creation_time",
                "type": "integer",
                "description": "Time in epoch milliseconds when this object was created."
              },
              {
                "name": "deactivated",
                "type": "boolean",
                "description": "Whether this private endpoint is deactivated."
              },
              {
                "name": "deactivated_at",
                "type": "integer",
                "description": "Time in epoch milliseconds when this object was deactivated."
              },
              {
                "name": "domain_names",
                "type": "array",
                "description": "Only used by private endpoints towards a VPC endpoint service for customer-managed VPC endpoint service. The target AWS resource FQDNs accessible via the VPC endpoint service. When updating this field, we perform full update on this field. Please ensure a full list of desired domain_names is provided."
              },
              {
                "name": "enabled",
                "type": "boolean",
                "description": "Only used by private endpoints towards an AWS S3 service. Update this field to activate/deactivate this private endpoint to allow egress access from serverless compute resources."
              },
              {
                "name": "endpoint_service",
                "type": "string",
                "description": "The full target AWS endpoint service name that connects to the destination resources of the private endpoint."
              },
              {
                "name": "error_message",
                "type": "string",
                "description": ""
              },
              {
                "name": "network_connectivity_config_id",
                "type": "string",
                "description": "The ID of a network connectivity configuration, which is the parent resource of this private endpoint rule object."
              },
              {
                "name": "resource_names",
                "type": "array",
                "description": "Only used by private endpoints towards AWS S3 service. The globally unique S3 bucket names that will be accessed via the VPC endpoint. The bucket names must be in the same region as the NCC/endpoint service. When updating this field, we perform full update on this field. Please ensure a full list of desired resource_names is provided."
              },
              {
                "name": "rule_id",
                "type": "string",
                "description": "The ID of a private endpoint rule."
              },
              {
                "name": "updated_time",
                "type": "integer",
                "description": "Time in epoch milliseconds when this object was updated."
              },
              {
                "name": "vpc_endpoint_id",
                "type": "string",
                "description": "The AWS VPC endpoint ID. You can use this ID to identify VPC endpoint created by Databricks."
              }
            ]
          },
          {
            "name": "azure_private_endpoint_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "connection_state",
                "type": "string",
                "description": "The current status of this private endpoint. The private endpoint rules are effective only if the connection state is ESTABLISHED. Remember that you must approve new endpoints on your resources in the Azure portal before they take effect. The possible values are: - INIT: (deprecated) The endpoint has been created and pending approval. - PENDING: The endpoint has been created and pending approval. - ESTABLISHED: The endpoint has been approved and is ready to use in your serverless compute resources. - REJECTED: Connection was rejected by the private link resource owner. - DISCONNECTED: Connection was removed by the private link resource owner, the private endpoint becomes informative and should be deleted for clean-up. - EXPIRED: If the endpoint was created but not approved in 14 days, it will be EXPIRED. (CREATE_FAILED, CREATING, DISCONNECTED, ESTABLISHED, EXPIRED, INIT, PENDING, REJECTED)"
              },
              {
                "name": "creation_time",
                "type": "integer",
                "description": "Time in epoch milliseconds when this object was created."
              },
              {
                "name": "deactivated",
                "type": "boolean",
                "description": "Whether this private endpoint is deactivated."
              },
              {
                "name": "deactivated_at",
                "type": "integer",
                "description": "Time in epoch milliseconds when this object was deactivated."
              },
              {
                "name": "domain_names",
                "type": "array",
                "description": "Not used by customer-managed private endpoint services. Domain names of target private link service. When updating this field, the full list of target domain_names must be specified."
              },
              {
                "name": "endpoint_name",
                "type": "string",
                "description": "The name of the Azure private endpoint resource."
              },
              {
                "name": "error_message",
                "type": "string",
                "description": ""
              },
              {
                "name": "group_id",
                "type": "string",
                "description": "Only used by private endpoints to Azure first-party services. The sub-resource type (group ID) of the target resource. Note that to connect to workspace root storage (root DBFS), you need two endpoints, one for blob and one for dfs."
              },
              {
                "name": "network_connectivity_config_id",
                "type": "string",
                "description": "The ID of a network connectivity configuration, which is the parent resource of this private endpoint rule object."
              },
              {
                "name": "resource_id",
                "type": "string",
                "description": "The Azure resource ID of the target resource."
              },
              {
                "name": "rule_id",
                "type": "string",
                "description": "The ID of a private endpoint rule."
              },
              {
                "name": "updated_time",
                "type": "integer",
                "description": "Time in epoch milliseconds when this object was updated."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "region",
    "type": "string",
    "description": "The region for the network connectivity configuration. Only workspaces in the same region can be attached to the network connectivity configuration."
  },
  {
    "name": "updated_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when this object was updated."
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
    <td><a href="#get_network_connectivity_configuration"><CopyableCode code="get_network_connectivity_configuration" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_connectivity_config_id"><code>network_connectivity_config_id</code></a></td>
    <td></td>
    <td>Gets a network connectivity configuration.</td>
</tr>
<tr>
    <td><a href="#list_network_connectivity_configurations"><CopyableCode code="list_network_connectivity_configurations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of network connectivity configurations.</td>
</tr>
<tr>
    <td><a href="#create_network_connectivity_configuration"><CopyableCode code="create_network_connectivity_configuration" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_connectivity_config"><code>network_connectivity_config</code></a></td>
    <td></td>
    <td>Creates a network connectivity configuration (NCC), which provides stable Azure service subnets when</td>
</tr>
<tr>
    <td><a href="#delete_network_connectivity_configuration"><CopyableCode code="delete_network_connectivity_configuration" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_connectivity_config_id"><code>network_connectivity_config_id</code></a></td>
    <td></td>
    <td>Deletes a network connectivity configuration.</td>
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
<tr id="parameter-network_connectivity_config_id">
    <td><CopyableCode code="network_connectivity_config_id" /></td>
    <td><code>string</code></td>
    <td>Your Network Connectivity Configuration ID.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to next page based on previous query.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_network_connectivity_configuration"
    values={[
        { label: 'get_network_connectivity_configuration', value: 'get_network_connectivity_configuration' },
        { label: 'list_network_connectivity_configurations', value: 'list_network_connectivity_configurations' }
    ]}
>
<TabItem value="get_network_connectivity_configuration">

Gets a network connectivity configuration.

```sql
SELECT
name,
account_id,
network_connectivity_config_id,
creation_time,
egress_config,
region,
updated_time
FROM databricks_account.settings.network_connectivity
WHERE account_id = '{{ account_id }}' -- required
AND network_connectivity_config_id = '{{ network_connectivity_config_id }}' -- required
;
```
</TabItem>
<TabItem value="list_network_connectivity_configurations">

Gets an array of network connectivity configurations.

```sql
SELECT
name,
account_id,
network_connectivity_config_id,
creation_time,
egress_config,
region,
updated_time
FROM databricks_account.settings.network_connectivity
WHERE account_id = '{{ account_id }}' -- required
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_network_connectivity_configuration"
    values={[
        { label: 'create_network_connectivity_configuration', value: 'create_network_connectivity_configuration' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_network_connectivity_configuration">

Creates a network connectivity configuration (NCC), which provides stable Azure service subnets when

```sql
INSERT INTO databricks_account.settings.network_connectivity (
network_connectivity_config,
account_id
)
SELECT 
'{{ network_connectivity_config }}' /* required */,
'{{ account_id }}'
RETURNING
name,
account_id,
network_connectivity_config_id,
creation_time,
egress_config,
region,
updated_time
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: network_connectivity
  props:
    - name: account_id
      value: string
      description: Required parameter for the network_connectivity resource.
    - name: network_connectivity_config
      value: object
      description: |
        :returns: :class:`NetworkConnectivityConfiguration`
      props:
      - name: name
        value: string
        description: |
          The name of the network connectivity configuration. The name can contain alphanumeric characters, hyphens, and underscores. The length must be between 3 and 30 characters. The name must match the regular expression ^[0-9a-zA-Z-_]{3,30}$
      - name: region
        value: string
        description: |
          The region for the network connectivity configuration. Only workspaces in the same region can be attached to the network connectivity configuration.
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_network_connectivity_configuration"
    values={[
        { label: 'delete_network_connectivity_configuration', value: 'delete_network_connectivity_configuration' }
    ]}
>
<TabItem value="delete_network_connectivity_configuration">

Deletes a network connectivity configuration.

```sql
DELETE FROM databricks_account.settings.network_connectivity
WHERE account_id = '{{ account_id }}' --required
AND network_connectivity_config_id = '{{ network_connectivity_config_id }}' --required
;
```
</TabItem>
</Tabs>

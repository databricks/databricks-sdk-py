---
title: private_endpoint_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_rules
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

Creates, updates, deletes, gets or lists a <code>private_endpoint_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_endpoint_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.private_endpoint_rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_private_endpoint_rule"
    values={[
        { label: 'get_private_endpoint_rule', value: 'get_private_endpoint_rule' },
        { label: 'list_private_endpoint_rules', value: 'list_private_endpoint_rules' }
    ]}
>
<TabItem value="get_private_endpoint_rule">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "Databricks account ID. You can find your account ID from the Accounts Console."
  },
  {
    "name": "group_id",
    "type": "string",
    "description": "Not used by customer-managed private endpoint services. The sub-resource type (group ID) of the target resource. Note that to connect to workspace root storage (root DBFS), you need two endpoints, one for blob and one for dfs."
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
    "name": "vpc_endpoint_id",
    "type": "string",
    "description": "The AWS VPC endpoint ID. You can use this ID to identify the VPC endpoint created by Databricks."
  },
  {
    "name": "endpoint_name",
    "type": "string",
    "description": "The name of the Azure private endpoint resource."
  },
  {
    "name": "connection_state",
    "type": "string",
    "description": "The current status of this private endpoint. The private endpoint rules are effective only if the connection state is ESTABLISHED. Remember that you must approve new endpoints on your resources in the Cloud console before they take effect. The possible values are: - PENDING: The endpoint has been created and pending approval. - ESTABLISHED: The endpoint has been approved and is ready to use in your serverless compute resources. - REJECTED: Connection was rejected by the private link resource owner. - DISCONNECTED: Connection was removed by the private link resource owner, the private endpoint becomes informative and should be deleted for clean-up. - EXPIRED: If the endpoint was created but not approved in 14 days, it will be EXPIRED. - CREATING: The endpoint creation is in progress. Once successfully created, the state will transition to PENDING. - CREATE_FAILED: The endpoint creation failed. You can check the error_message field for more details."
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
    "description": "Only used by private endpoints to customer-managed private endpoint services. Domain names of target private link service. When updating this field, the full list of target domain_names must be specified."
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
    "name": "resource_names",
    "type": "array",
    "description": "Only used by private endpoints towards AWS S3 service. The globally unique S3 bucket names that will be accessed via the VPC endpoint. The bucket names must be in the same region as the NCC/endpoint service. When updating this field, we perform full update on this field. Please ensure a full list of desired resource_names is provided."
  },
  {
    "name": "updated_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when this object was updated."
  }
]} />
</TabItem>
<TabItem value="list_private_endpoint_rules">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "Databricks account ID. You can find your account ID from the Accounts Console."
  },
  {
    "name": "group_id",
    "type": "string",
    "description": "Not used by customer-managed private endpoint services. The sub-resource type (group ID) of the target resource. Note that to connect to workspace root storage (root DBFS), you need two endpoints, one for blob and one for dfs."
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
    "name": "vpc_endpoint_id",
    "type": "string",
    "description": "The AWS VPC endpoint ID. You can use this ID to identify the VPC endpoint created by Databricks."
  },
  {
    "name": "endpoint_name",
    "type": "string",
    "description": "The name of the Azure private endpoint resource."
  },
  {
    "name": "connection_state",
    "type": "string",
    "description": "The current status of this private endpoint. The private endpoint rules are effective only if the connection state is ESTABLISHED. Remember that you must approve new endpoints on your resources in the Cloud console before they take effect. The possible values are: - PENDING: The endpoint has been created and pending approval. - ESTABLISHED: The endpoint has been approved and is ready to use in your serverless compute resources. - REJECTED: Connection was rejected by the private link resource owner. - DISCONNECTED: Connection was removed by the private link resource owner, the private endpoint becomes informative and should be deleted for clean-up. - EXPIRED: If the endpoint was created but not approved in 14 days, it will be EXPIRED. - CREATING: The endpoint creation is in progress. Once successfully created, the state will transition to PENDING. - CREATE_FAILED: The endpoint creation failed. You can check the error_message field for more details."
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
    "description": "Only used by private endpoints to customer-managed private endpoint services. Domain names of target private link service. When updating this field, the full list of target domain_names must be specified."
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
    "name": "resource_names",
    "type": "array",
    "description": "Only used by private endpoints towards AWS S3 service. The globally unique S3 bucket names that will be accessed via the VPC endpoint. The bucket names must be in the same region as the NCC/endpoint service. When updating this field, we perform full update on this field. Please ensure a full list of desired resource_names is provided."
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
    <td><a href="#get_private_endpoint_rule"><CopyableCode code="get_private_endpoint_rule" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_connectivity_config_id"><code>network_connectivity_config_id</code></a>, <a href="#parameter-private_endpoint_rule_id"><code>private_endpoint_rule_id</code></a></td>
    <td></td>
    <td>Gets the private endpoint rule.</td>
</tr>
<tr>
    <td><a href="#list_private_endpoint_rules"><CopyableCode code="list_private_endpoint_rules" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_connectivity_config_id"><code>network_connectivity_config_id</code></a></td>
    <td><a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of private endpoint rules.</td>
</tr>
<tr>
    <td><a href="#create_private_endpoint_rule"><CopyableCode code="create_private_endpoint_rule" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_connectivity_config_id"><code>network_connectivity_config_id</code></a>, <a href="#parameter-data__private_endpoint_rule"><code>data__private_endpoint_rule</code></a></td>
    <td></td>
    <td>Create a private endpoint rule for the specified network connectivity config object. Once the object</td>
</tr>
<tr>
    <td><a href="#update_private_endpoint_rule"><CopyableCode code="update_private_endpoint_rule" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_connectivity_config_id"><code>network_connectivity_config_id</code></a>, <a href="#parameter-private_endpoint_rule_id"><code>private_endpoint_rule_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-data__private_endpoint_rule"><code>data__private_endpoint_rule</code></a></td>
    <td></td>
    <td>Updates a private endpoint rule. Currently only a private endpoint rule to customer-managed resources</td>
</tr>
<tr>
    <td><a href="#delete_private_endpoint_rule"><CopyableCode code="delete_private_endpoint_rule" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_connectivity_config_id"><code>network_connectivity_config_id</code></a>, <a href="#parameter-private_endpoint_rule_id"><code>private_endpoint_rule_id</code></a></td>
    <td></td>
    <td>Initiates deleting a private endpoint rule. If the connection state is PENDING or EXPIRED, the private</td>
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
    <td>Your Network Connectvity Configuration ID.</td>
</tr>
<tr id="parameter-private_endpoint_rule_id">
    <td><CopyableCode code="private_endpoint_rule_id" /></td>
    <td><code>string</code></td>
    <td>Your private endpoint rule ID.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td></td>
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
    defaultValue="get_private_endpoint_rule"
    values={[
        { label: 'get_private_endpoint_rule', value: 'get_private_endpoint_rule' },
        { label: 'list_private_endpoint_rules', value: 'list_private_endpoint_rules' }
    ]}
>
<TabItem value="get_private_endpoint_rule">

Gets the private endpoint rule.

```sql
SELECT
account_id,
group_id,
network_connectivity_config_id,
resource_id,
rule_id,
vpc_endpoint_id,
endpoint_name,
connection_state,
creation_time,
deactivated,
deactivated_at,
domain_names,
enabled,
endpoint_service,
error_message,
resource_names,
updated_time
FROM databricks_account.settings.private_endpoint_rules
WHERE account_id = '{{ account_id }}' -- required
AND network_connectivity_config_id = '{{ network_connectivity_config_id }}' -- required
AND private_endpoint_rule_id = '{{ private_endpoint_rule_id }}' -- required
;
```
</TabItem>
<TabItem value="list_private_endpoint_rules">

Gets an array of private endpoint rules.

```sql
SELECT
account_id,
group_id,
network_connectivity_config_id,
resource_id,
rule_id,
vpc_endpoint_id,
endpoint_name,
connection_state,
creation_time,
deactivated,
deactivated_at,
domain_names,
enabled,
endpoint_service,
error_message,
resource_names,
updated_time
FROM databricks_account.settings.private_endpoint_rules
WHERE account_id = '{{ account_id }}' -- required
AND network_connectivity_config_id = '{{ network_connectivity_config_id }}' -- required
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_private_endpoint_rule"
    values={[
        { label: 'create_private_endpoint_rule', value: 'create_private_endpoint_rule' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_private_endpoint_rule">

Create a private endpoint rule for the specified network connectivity config object. Once the object

```sql
INSERT INTO databricks_account.settings.private_endpoint_rules (
data__private_endpoint_rule,
account_id,
network_connectivity_config_id
)
SELECT 
'{{ private_endpoint_rule }}' /* required */,
'{{ account_id }}',
'{{ network_connectivity_config_id }}'
RETURNING
account_id,
group_id,
network_connectivity_config_id,
resource_id,
rule_id,
vpc_endpoint_id,
endpoint_name,
connection_state,
creation_time,
deactivated,
deactivated_at,
domain_names,
enabled,
endpoint_service,
error_message,
resource_names,
updated_time
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: private_endpoint_rules
  props:
    - name: account_id
      value: string
      description: Required parameter for the private_endpoint_rules resource.
    - name: network_connectivity_config_id
      value: string
      description: Required parameter for the private_endpoint_rules resource.
    - name: private_endpoint_rule
      value: string
      description: |
        :returns: :class:`NccPrivateEndpointRule`
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_private_endpoint_rule"
    values={[
        { label: 'update_private_endpoint_rule', value: 'update_private_endpoint_rule' }
    ]}
>
<TabItem value="update_private_endpoint_rule">

Updates a private endpoint rule. Currently only a private endpoint rule to customer-managed resources

```sql
UPDATE databricks_account.settings.private_endpoint_rules
SET 
data__private_endpoint_rule = '{{ private_endpoint_rule }}'
WHERE 
account_id = '{{ account_id }}' --required
AND network_connectivity_config_id = '{{ network_connectivity_config_id }}' --required
AND private_endpoint_rule_id = '{{ private_endpoint_rule_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND data__private_endpoint_rule = '{{ private_endpoint_rule }}' --required
RETURNING
account_id,
group_id,
network_connectivity_config_id,
resource_id,
rule_id,
vpc_endpoint_id,
endpoint_name,
connection_state,
creation_time,
deactivated,
deactivated_at,
domain_names,
enabled,
endpoint_service,
error_message,
resource_names,
updated_time;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_private_endpoint_rule"
    values={[
        { label: 'delete_private_endpoint_rule', value: 'delete_private_endpoint_rule' }
    ]}
>
<TabItem value="delete_private_endpoint_rule">

Initiates deleting a private endpoint rule. If the connection state is PENDING or EXPIRED, the private

```sql
DELETE FROM databricks_account.settings.private_endpoint_rules
WHERE account_id = '{{ account_id }}' --required
AND network_connectivity_config_id = '{{ network_connectivity_config_id }}' --required
AND private_endpoint_rule_id = '{{ private_endpoint_rule_id }}' --required
;
```
</TabItem>
</Tabs>

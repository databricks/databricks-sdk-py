---
title: network_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - network_policies
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

Creates, updates, deletes, gets or lists a <code>network_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.network_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_network_policy_rpc"
    values={[
        { label: 'get_network_policy_rpc', value: 'get_network_policy_rpc' },
        { label: 'list_network_policies_rpc', value: 'list_network_policies_rpc' }
    ]}
>
<TabItem value="get_network_policy_rpc">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "network_policy_id",
    "type": "string",
    "description": "The unique identifier for the network policy."
  },
  {
    "name": "egress",
    "type": "object",
    "description": "The network policies applying for egress traffic.",
    "children": [
      {
        "name": "network_access",
        "type": "object",
        "description": "The access policy enforced for egress traffic to the internet.",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "At which level can Databricks and Databricks managed compute access Internet. FULL_ACCESS:<br />Databricks can access Internet. No blocking rules will apply. RESTRICTED_ACCESS: Databricks can<br />only access explicitly allowed internet and storage destinations, as well as UC connections and<br />external locations."
          },
          {
            "name": "allowed_internet_destinations",
            "type": "array",
            "description": "List of internet destinations that serverless workloads are allowed to access when in RESTRICTED_ACCESS mode.",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "The internet destination to which access will be allowed. Format dependent on the destination type."
              },
              {
                "name": "internet_destination_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              }
            ]
          },
          {
            "name": "allowed_storage_destinations",
            "type": "array",
            "description": "List of storage destinations that serverless workloads are allowed to access when in RESTRICTED_ACCESS mode.",
            "children": [
              {
                "name": "azure_storage_account",
                "type": "string",
                "description": "The Azure storage account name."
              },
              {
                "name": "azure_storage_service",
                "type": "string",
                "description": "The Azure storage service type (blob, dfs, etc.)."
              },
              {
                "name": "bucket_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "region",
                "type": "string",
                "description": ""
              },
              {
                "name": "storage_destination_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              }
            ]
          },
          {
            "name": "policy_enforcement",
            "type": "object",
            "description": "Optional. When policy_enforcement is not provided, we default to ENFORCE_MODE_ALL_SERVICES",
            "children": [
              {
                "name": "dry_run_mode_product_filter",
                "type": "array",
                "description": ""
              },
              {
                "name": "enforcement_mode",
                "type": "string",
                "description": "The mode of policy enforcement. ENFORCED blocks traffic that violates policy, while DRY_RUN only logs violations without blocking. When not specified, defaults to ENFORCED."
              }
            ]
          }
        ]
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list_network_policies_rpc">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "network_policy_id",
    "type": "string",
    "description": "The unique identifier for the network policy."
  },
  {
    "name": "egress",
    "type": "object",
    "description": "The network policies applying for egress traffic.",
    "children": [
      {
        "name": "network_access",
        "type": "object",
        "description": "The access policy enforced for egress traffic to the internet.",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "At which level can Databricks and Databricks managed compute access Internet. FULL_ACCESS:<br />Databricks can access Internet. No blocking rules will apply. RESTRICTED_ACCESS: Databricks can<br />only access explicitly allowed internet and storage destinations, as well as UC connections and<br />external locations."
          },
          {
            "name": "allowed_internet_destinations",
            "type": "array",
            "description": "List of internet destinations that serverless workloads are allowed to access when in RESTRICTED_ACCESS mode.",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "The internet destination to which access will be allowed. Format dependent on the destination type."
              },
              {
                "name": "internet_destination_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              }
            ]
          },
          {
            "name": "allowed_storage_destinations",
            "type": "array",
            "description": "List of storage destinations that serverless workloads are allowed to access when in RESTRICTED_ACCESS mode.",
            "children": [
              {
                "name": "azure_storage_account",
                "type": "string",
                "description": "The Azure storage account name."
              },
              {
                "name": "azure_storage_service",
                "type": "string",
                "description": "The Azure storage service type (blob, dfs, etc.)."
              },
              {
                "name": "bucket_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "region",
                "type": "string",
                "description": ""
              },
              {
                "name": "storage_destination_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              }
            ]
          },
          {
            "name": "policy_enforcement",
            "type": "object",
            "description": "Optional. When policy_enforcement is not provided, we default to ENFORCE_MODE_ALL_SERVICES",
            "children": [
              {
                "name": "dry_run_mode_product_filter",
                "type": "array",
                "description": ""
              },
              {
                "name": "enforcement_mode",
                "type": "string",
                "description": "The mode of policy enforcement. ENFORCED blocks traffic that violates policy, while DRY_RUN only logs violations without blocking. When not specified, defaults to ENFORCED."
              }
            ]
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
    <td><a href="#get_network_policy_rpc"><CopyableCode code="get_network_policy_rpc" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_policy_id"><code>network_policy_id</code></a></td>
    <td></td>
    <td>Gets a network policy.</td>
</tr>
<tr>
    <td><a href="#list_network_policies_rpc"><CopyableCode code="list_network_policies_rpc" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of network policies.</td>
</tr>
<tr>
    <td><a href="#create_network_policy_rpc"><CopyableCode code="create_network_policy_rpc" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-data__network_policy"><code>data__network_policy</code></a></td>
    <td></td>
    <td>Creates a new network policy to manage which network destinations can be accessed from the Databricks</td>
</tr>
<tr>
    <td><a href="#update_network_policy_rpc"><CopyableCode code="update_network_policy_rpc" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_policy_id"><code>network_policy_id</code></a>, <a href="#parameter-data__network_policy"><code>data__network_policy</code></a></td>
    <td></td>
    <td>Updates a network policy. This allows you to modify the configuration of a network policy.</td>
</tr>
<tr>
    <td><a href="#delete_network_policy_rpc"><CopyableCode code="delete_network_policy_rpc" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_policy_id"><code>network_policy_id</code></a></td>
    <td></td>
    <td>Deletes a network policy. Cannot be called on 'default-policy'.</td>
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
<tr id="parameter-network_policy_id">
    <td><CopyableCode code="network_policy_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the network policy to delete.</td>
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
    defaultValue="get_network_policy_rpc"
    values={[
        { label: 'get_network_policy_rpc', value: 'get_network_policy_rpc' },
        { label: 'list_network_policies_rpc', value: 'list_network_policies_rpc' }
    ]}
>
<TabItem value="get_network_policy_rpc">

Gets a network policy.

```sql
SELECT
account_id,
network_policy_id,
egress
FROM databricks_account.settings.network_policies
WHERE account_id = '{{ account_id }}' -- required
AND network_policy_id = '{{ network_policy_id }}' -- required
;
```
</TabItem>
<TabItem value="list_network_policies_rpc">

Gets an array of network policies.

```sql
SELECT
account_id,
network_policy_id,
egress
FROM databricks_account.settings.network_policies
WHERE account_id = '{{ account_id }}' -- required
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_network_policy_rpc"
    values={[
        { label: 'create_network_policy_rpc', value: 'create_network_policy_rpc' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_network_policy_rpc">

Creates a new network policy to manage which network destinations can be accessed from the Databricks

```sql
INSERT INTO databricks_account.settings.network_policies (
data__network_policy,
account_id
)
SELECT 
'{{ network_policy }}' /* required */,
'{{ account_id }}'
RETURNING
account_id,
network_policy_id,
egress
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: network_policies
  props:
    - name: account_id
      value: string
      description: Required parameter for the network_policies resource.
    - name: network_policy
      value: string
      description: |
        Network policy configuration details.
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_network_policy_rpc"
    values={[
        { label: 'update_network_policy_rpc', value: 'update_network_policy_rpc' }
    ]}
>
<TabItem value="update_network_policy_rpc">

Updates a network policy. This allows you to modify the configuration of a network policy.

```sql
REPLACE databricks_account.settings.network_policies
SET 
data__network_policy = '{{ network_policy }}'
WHERE 
account_id = '{{ account_id }}' --required
AND network_policy_id = '{{ network_policy_id }}' --required
AND data__network_policy = '{{ network_policy }}' --required
RETURNING
account_id,
network_policy_id,
egress;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_network_policy_rpc"
    values={[
        { label: 'delete_network_policy_rpc', value: 'delete_network_policy_rpc' }
    ]}
>
<TabItem value="delete_network_policy_rpc">

Deletes a network policy. Cannot be called on 'default-policy'.

```sql
DELETE FROM databricks_account.settings.network_policies
WHERE account_id = '{{ account_id }}' --required
AND network_policy_id = '{{ network_policy_id }}' --required
;
```
</TabItem>
</Tabs>

---
title: policy_compliance_for_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_compliance_for_clusters
  - compute
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

Creates, updates, deletes, gets or lists a <code>policy_compliance_for_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_compliance_for_clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.policy_compliance_for_clusters" /></td></tr>
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
    "name": "is_compliant",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "violations",
    "type": "object",
    "description": "An object containing key-value mappings representing the first 200 policy validation errors. The keys indicate the path where the policy validation error is occurring. The values indicate an error message describing the policy validation error."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "cluster_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "is_compliant",
    "type": "boolean",
    "description": "Whether this cluster is in compliance with the latest version of its policy."
  },
  {
    "name": "violations",
    "type": "object",
    "description": "An object containing key-value mappings representing the first 200 policy validation errors. The keys indicate the path where the policy validation error is occurring. The values indicate an error message describing the policy validation error."
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
    <td><a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Returns the policy compliance status of a cluster. Clusters could be out of compliance if their policy</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns the policy compliance status of all clusters that use a given policy. Clusters could be out of</td>
</tr>
<tr>
    <td><a href="#enforce"><CopyableCode code="enforce" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a></td>
    <td></td>
    <td>Updates a cluster to be compliant with the current version of its policy. A cluster can be updated if</td>
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
<tr id="parameter-cluster_id">
    <td><CopyableCode code="cluster_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the cluster to get the compliance status</td>
</tr>
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>Canonical unique identifier for the cluster policy.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Use this field to specify the maximum number of results to be returned by the server. The server may further constrain the maximum number of results returned in a single page.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token that can be used to navigate to the next page or previous page as returned by `next_page_token` or `prev_page_token`.</td>
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

Returns the policy compliance status of a cluster. Clusters could be out of compliance if their policy

```sql
SELECT
is_compliant,
violations
FROM databricks_workspace.compute.policy_compliance_for_clusters
WHERE cluster_id = '{{ cluster_id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns the policy compliance status of all clusters that use a given policy. Clusters could be out of

```sql
SELECT
cluster_id,
is_compliant,
violations
FROM databricks_workspace.compute.policy_compliance_for_clusters
WHERE policy_id = '{{ policy_id }}' -- required
AND workspace = '{{ workspace }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="enforce"
    values={[
        { label: 'enforce', value: 'enforce' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="enforce">

Updates a cluster to be compliant with the current version of its policy. A cluster can be updated if

```sql
INSERT INTO databricks_workspace.compute.policy_compliance_for_clusters (
cluster_id,
validate_only,
workspace
)
SELECT 
'{{ cluster_id }}' /* required */,
{{ validate_only }},
'{{ workspace }}'
RETURNING
changes,
has_changes
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: policy_compliance_for_clusters
  props:
    - name: workspace
      value: string
      description: Required parameter for the policy_compliance_for_clusters resource.
    - name: cluster_id
      value: string
      description: |
        The ID of the cluster you want to enforce policy compliance on.
    - name: validate_only
      value: boolean
      description: |
        If set, previews the changes that would be made to a cluster to enforce compliance but does not update the cluster.
```
</TabItem>
</Tabs>

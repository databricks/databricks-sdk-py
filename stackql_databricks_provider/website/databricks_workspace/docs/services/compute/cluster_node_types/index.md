---
title: cluster_node_types
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_node_types
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

Creates, updates, deletes, gets or lists a <code>cluster_node_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cluster_node_types" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.cluster_node_types" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "node_types",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "node_type_id",
        "type": "string",
        "description": "Unique identifier for this node type."
      },
      {
        "name": "memory_mb",
        "type": "integer",
        "description": "Memory (in MB) available for this node type."
      },
      {
        "name": "num_cores",
        "type": "number",
        "description": "Number of CPU cores available for this node type. Note that this can be fractional, e.g., 2.5 cores, if the the number of cores on a machine instance is not divisible by the number of Spark nodes on that machine."
      },
      {
        "name": "description",
        "type": "string",
        "description": "A string description associated with this node type, e.g., \"r3.xlarge\"."
      },
      {
        "name": "instance_type_id",
        "type": "string",
        "description": "An identifier for the type of hardware that this node runs on, e.g., \"r3.2xlarge\" in AWS."
      },
      {
        "name": "category",
        "type": "string",
        "description": "A descriptive category for this node type. Examples include \"Memory Optimized\" and \"Compute Optimized\"."
      },
      {
        "name": "display_order",
        "type": "integer",
        "description": "An optional hint at the display order of node types in the UI. Within a node type category, lowest numbers come first."
      },
      {
        "name": "is_deprecated",
        "type": "boolean",
        "description": "Whether the node type is deprecated. Non-deprecated node types offer greater performance."
      },
      {
        "name": "is_encrypted_in_transit",
        "type": "boolean",
        "description": "AWS specific, whether this instance supports encryption in transit, used for hipaa and pci workloads."
      },
      {
        "name": "is_graviton",
        "type": "boolean",
        "description": "Whether this is an Arm-based instance."
      },
      {
        "name": "is_hidden",
        "type": "boolean",
        "description": "Whether this node is hidden from presentation in the UI."
      },
      {
        "name": "is_io_cache_enabled",
        "type": "boolean",
        "description": "Whether this node comes with IO cache enabled by default."
      },
      {
        "name": "node_info",
        "type": "object",
        "description": "A collection of node type info reported by the cloud provider",
        "children": [
          {
            "name": "status",
            "type": "array",
            "description": ""
          }
        ]
      },
      {
        "name": "node_instance_type",
        "type": "object",
        "description": "The NodeInstanceType object corresponding to instance_type_id",
        "children": [
          {
            "name": "instance_type_id",
            "type": "string",
            "description": "Unique identifier across instance types"
          },
          {
            "name": "local_disk_size_gb",
            "type": "integer",
            "description": "Size of the individual local disks attached to this instance (i.e. per local disk)."
          },
          {
            "name": "local_disks",
            "type": "integer",
            "description": "Number of local disks that are present on this instance."
          },
          {
            "name": "local_nvme_disk_size_gb",
            "type": "integer",
            "description": "Size of the individual local nvme disks attached to this instance (i.e. per local disk)."
          },
          {
            "name": "local_nvme_disks",
            "type": "integer",
            "description": "Number of local nvme disks that are present on this instance."
          }
        ]
      },
      {
        "name": "num_gpus",
        "type": "integer",
        "description": "Number of GPUs available for this node type."
      },
      {
        "name": "photon_driver_capable",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "photon_worker_capable",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "support_cluster_tags",
        "type": "boolean",
        "description": "Whether this node type support cluster tags."
      },
      {
        "name": "support_ebs_volumes",
        "type": "boolean",
        "description": "Whether this node type support EBS volumes. EBS volumes is disabled for node types that we could place multiple corresponding containers on the same hosting instance."
      },
      {
        "name": "support_port_forwarding",
        "type": "boolean",
        "description": "Whether this node type supports port forwarding."
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Returns a list of supported Spark node types. These node types can be used to launch a cluster.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Returns a list of supported Spark node types. These node types can be used to launch a cluster.

```sql
SELECT
node_types
FROM databricks_workspace.compute.cluster_node_types
WHERE deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>

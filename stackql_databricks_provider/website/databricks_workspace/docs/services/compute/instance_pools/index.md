---
title: instance_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_pools
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists an <code>instance_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="instance_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.instance_pools" /></td></tr>
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
    "name": "instance_pool_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "node_type_id",
    "type": "string",
    "description": "This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads. A list of available node types can be retrieved by using the :method:clusters/listNodeTypes API call."
  },
  {
    "name": "instance_pool_name",
    "type": "string",
    "description": "Pool name requested by the user. Pool name must be unique. Length must be between 1 and 100 characters."
  },
  {
    "name": "aws_attributes",
    "type": "object",
    "description": "Attributes related to instance pools running on Amazon Web Services. If not specified at pool creation, a set of default values will be used.",
    "children": [
      {
        "name": "availability",
        "type": "string",
        "description": "Availability type used for the spot nodes. (ON_DEMAND, SPOT)"
      },
      {
        "name": "instance_profile_arn",
        "type": "string",
        "description": "All AWS instances belonging to the instance pool will have this instance profile. If omitted, instances will initially be launched with the workspace's default instance profile. If defined, clusters that use the pool will inherit the instance profile, and must not specify their own instance profile on cluster creation or update. If the pool does not specify an instance profile, clusters using the pool may specify any instance profile. The instance profile must have previously been added to the Databricks environment by an account administrator. This feature may only be available to certain customer plans."
      },
      {
        "name": "spot_bid_price_percent",
        "type": "integer",
        "description": "Calculates the bid price for AWS spot instances, as a percentage of the corresponding instance type's on-demand price. For example, if this field is set to 50, and the cluster needs a new `r3.xlarge` spot instance, then the bid price is half of the price of on-demand `r3.xlarge` instances. Similarly, if this field is set to 200, the bid price is twice the price of on-demand `r3.xlarge` instances. If not specified, the default value is 100. When spot instances are requested for this cluster, only spot instances whose bid price percentage matches this field will be considered. Note that, for safety, we enforce this field to be no more than 10000."
      },
      {
        "name": "zone_id",
        "type": "string",
        "description": "Identifier for the availability zone/datacenter in which the cluster resides. This string will be of a form like \"us-west-2a\". The provided availability zone must be in the same region as the Databricks deployment. For example, \"us-west-2a\" is not a valid zone id if the Databricks deployment resides in the \"us-east-1\" region. This is an optional field at cluster creation, and if not specified, a default zone will be used. The list of available zones as well as the default value can be found by using the `List Zones` method."
      }
    ]
  },
  {
    "name": "azure_attributes",
    "type": "object",
    "description": "Attributes related to instance pools running on Azure. If not specified at pool creation, a set of default values will be used.",
    "children": [
      {
        "name": "availability",
        "type": "string",
        "description": "Availability type used for the spot nodes. (ON_DEMAND_AZURE, SPOT_AZURE)"
      },
      {
        "name": "spot_bid_max_price",
        "type": "number",
        "description": "With variable pricing, you have option to set a max price, in US dollars (USD) For example, the value 2 would be a max price of $2.00 USD per hour. If you set the max price to be -1, the VM won't be evicted based on price. The price for the VM will be the current price for spot or the price for a standard VM, which ever is less, as long as there is capacity and quota available."
      }
    ]
  },
  {
    "name": "custom_tags",
    "type": "object",
    "description": "Additional tags for pool resources. Databricks will tag all pool resources (e.g., AWS instances and EBS volumes) with these tags in addition to `default_tags`. Notes: - Currently, Databricks allows at most 45 custom tags"
  },
  {
    "name": "default_tags",
    "type": "object",
    "description": "Tags that are added by Databricks regardless of any ``custom_tags``, including: - Vendor: Databricks - InstancePoolCreator: &lt;user_id_of_creator&gt; - InstancePoolName: &lt;name_of_pool&gt; - InstancePoolId: &lt;id_of_pool&gt;"
  },
  {
    "name": "disk_spec",
    "type": "object",
    "description": "Defines the specification of the disks that will be attached to all spark containers.",
    "children": [
      {
        "name": "disk_count",
        "type": "integer",
        "description": "The number of disks launched for each instance: - This feature is only enabled for supported node types. - Users can choose up to the limit of the disks supported by the node type. - For node types with no OS disk, at least one disk must be specified; otherwise, cluster creation will fail. If disks are attached, Databricks will configure Spark to use only the disks for scratch storage, because heterogenously sized scratch devices can lead to inefficient disk utilization. If no disks are attached, Databricks will configure Spark to use instance store disks. Note: If disks are specified, then the Spark configuration `spark.local.dir` will be overridden. Disks will be mounted at: - For AWS: `/ebs0`, `/ebs1`, and etc. - For Azure: `/remote_volume0`, `/remote_volume1`, and etc."
      },
      {
        "name": "disk_iops",
        "type": "integer",
        "description": ""
      },
      {
        "name": "disk_size",
        "type": "integer",
        "description": "The size of each disk (in GiB) launched for each instance. Values must fall into the supported range for a particular instance type. For AWS: - General Purpose SSD: 100 - 4096 GiB - Throughput Optimized HDD: 500 - 4096 GiB For Azure: - Premium LRS (SSD): 1 - 1023 GiB - Standard LRS (HDD): 1- 1023 GiB"
      },
      {
        "name": "disk_throughput",
        "type": "integer",
        "description": ""
      },
      {
        "name": "disk_type",
        "type": "object",
        "description": "The type of disks that will be launched with this cluster.",
        "children": [
          {
            "name": "azure_disk_volume_type",
            "type": "string",
            "description": "All Azure Disk types that Databricks supports. See<br />https://docs.microsoft.com/en-us/azure/storage/storage-about-disks-and-vhds-linux#types-of-disks (PREMIUM_LRS, STANDARD_LRS)"
          },
          {
            "name": "ebs_volume_type",
            "type": "string",
            "description": "All EBS volume types that Databricks supports. See https://aws.amazon.com/ebs/details/ for<br />details. (GENERAL_PURPOSE_SSD, THROUGHPUT_OPTIMIZED_HDD)"
          }
        ]
      }
    ]
  },
  {
    "name": "enable_elastic_disk",
    "type": "boolean",
    "description": "Autoscaling Local Storage: when enabled, this instances in this pool will dynamically acquire additional disk space when its Spark workers are running low on disk space. In AWS, this feature requires specific AWS permissions to function correctly - refer to the User Guide for more details."
  },
  {
    "name": "gcp_attributes",
    "type": "object",
    "description": "Attributes related to instance pools running on Google Cloud Platform. If not specified at pool creation, a set of default values will be used.",
    "children": [
      {
        "name": "gcp_availability",
        "type": "string",
        "description": "This field determines whether the instance pool will contain preemptible VMs, on-demand VMs, or<br />preemptible VMs with a fallback to on-demand VMs if the former is unavailable. (ON_DEMAND_GCP, PREEMPTIBLE_GCP, PREEMPTIBLE_WITH_FALLBACK_GCP)"
      },
      {
        "name": "local_ssd_count",
        "type": "integer",
        "description": "If provided, each node in the instance pool will have this number of local SSDs attached. Each local SSD is 375GB in size. Refer to [GCP documentation] for the supported number of local SSDs for each instance type. [GCP documentation]: https://cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds"
      },
      {
        "name": "zone_id",
        "type": "string",
        "description": "Identifier for the availability zone/datacenter in which the cluster resides. This string will be of a form like \"us-west1-a\". The provided availability zone must be in the same region as the Databricks workspace. For example, \"us-west1-a\" is not a valid zone id if the Databricks workspace resides in the \"us-east1\" region. This is an optional field at instance pool creation, and if not specified, a default zone will be used. This field can be one of the following: - \"HA\" =&gt; High availability, spread nodes across availability zones for a Databricks deployment region - A GCP availability zone =&gt; Pick One of the available zones for (machine type + region) from https://cloud.google.com/compute/docs/regions-zones (e.g. \"us-west1-a\"). If empty, Databricks picks an availability zone to schedule the cluster on."
      }
    ]
  },
  {
    "name": "idle_instance_autotermination_minutes",
    "type": "integer",
    "description": "Automatically terminates the extra instances in the pool cache after they are inactive for this time in minutes if min_idle_instances requirement is already met. If not set, the extra pool instances will be automatically terminated after a default timeout. If specified, the threshold must be between 0 and 10000 minutes. Users can also set this value to 0 to instantly remove idle instances from the cache if min cache size could still hold."
  },
  {
    "name": "max_capacity",
    "type": "integer",
    "description": "Maximum number of outstanding instances to keep in the pool, including both instances used by clusters and idle instances. Clusters that require further instance provisioning will fail during upsize requests."
  },
  {
    "name": "min_idle_instances",
    "type": "integer",
    "description": "Minimum number of idle instances to keep in the instance pool"
  },
  {
    "name": "node_type_flexibility",
    "type": "object",
    "description": "Flexible node type configuration for the pool.",
    "children": [
      {
        "name": "alternate_node_type_ids",
        "type": "array",
        "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
      }
    ]
  },
  {
    "name": "preloaded_docker_images",
    "type": "array",
    "description": "Custom Docker Image BYOC",
    "children": [
      {
        "name": "basic_auth",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "password",
            "type": "string",
            "description": ""
          },
          {
            "name": "username",
            "type": "string",
            "description": "Name of the user"
          }
        ]
      },
      {
        "name": "url",
        "type": "string",
        "description": "URL of the docker image."
      }
    ]
  },
  {
    "name": "preloaded_spark_versions",
    "type": "array",
    "description": "A list containing at most one preloaded Spark image version for the pool. Pool-backed clusters started with the preloaded Spark version will start faster. A list of available Spark versions can be retrieved by using the :method:clusters/sparkVersions API call."
  },
  {
    "name": "remote_disk_throughput",
    "type": "integer",
    "description": "If set, what the configurable throughput (in Mb/s) for the remote disk is. Currently only supported for GCP HYPERDISK_BALANCED types."
  },
  {
    "name": "state",
    "type": "string",
    "description": "Current state of the instance pool. (ACTIVE, DELETED, STOPPED)"
  },
  {
    "name": "stats",
    "type": "object",
    "description": "Usage statistics about the instance pool.",
    "children": [
      {
        "name": "idle_count",
        "type": "integer",
        "description": ""
      },
      {
        "name": "pending_idle_count",
        "type": "integer",
        "description": "Number of pending instances in the pool that are NOT part of a cluster."
      },
      {
        "name": "pending_used_count",
        "type": "integer",
        "description": "Number of pending instances in the pool that are part of a cluster."
      },
      {
        "name": "used_count",
        "type": "integer",
        "description": "Number of active instances in the pool that are part of a cluster."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Status of failed pending instances in the pool.",
    "children": [
      {
        "name": "pending_instance_errors",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "instance_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "message",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "total_initial_remote_disk_size",
    "type": "integer",
    "description": "If set, what the total initial volume size (in GB) of the remote disks should be. Currently only supported for GCP HYPERDISK_BALANCED types."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "instance_pool_id",
    "type": "string",
    "description": "Canonical unique identifier for the pool."
  },
  {
    "name": "node_type_id",
    "type": "string",
    "description": "This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads. A list of available node types can be retrieved by using the :method:clusters/listNodeTypes API call."
  },
  {
    "name": "instance_pool_name",
    "type": "string",
    "description": "Pool name requested by the user. Pool name must be unique. Length must be between 1 and 100 characters."
  },
  {
    "name": "aws_attributes",
    "type": "object",
    "description": "Attributes set during instance pool creation which are related to Amazon Web Services.",
    "children": [
      {
        "name": "availability",
        "type": "string",
        "description": "Availability type used for the spot nodes. (ON_DEMAND, SPOT)"
      },
      {
        "name": "instance_profile_arn",
        "type": "string",
        "description": "All AWS instances belonging to the instance pool will have this instance profile. If omitted, instances will initially be launched with the workspace's default instance profile. If defined, clusters that use the pool will inherit the instance profile, and must not specify their own instance profile on cluster creation or update. If the pool does not specify an instance profile, clusters using the pool may specify any instance profile. The instance profile must have previously been added to the Databricks environment by an account administrator. This feature may only be available to certain customer plans."
      },
      {
        "name": "spot_bid_price_percent",
        "type": "integer",
        "description": "Calculates the bid price for AWS spot instances, as a percentage of the corresponding instance type's on-demand price. For example, if this field is set to 50, and the cluster needs a new `r3.xlarge` spot instance, then the bid price is half of the price of on-demand `r3.xlarge` instances. Similarly, if this field is set to 200, the bid price is twice the price of on-demand `r3.xlarge` instances. If not specified, the default value is 100. When spot instances are requested for this cluster, only spot instances whose bid price percentage matches this field will be considered. Note that, for safety, we enforce this field to be no more than 10000."
      },
      {
        "name": "zone_id",
        "type": "string",
        "description": "Identifier for the availability zone/datacenter in which the cluster resides. This string will be of a form like \"us-west-2a\". The provided availability zone must be in the same region as the Databricks deployment. For example, \"us-west-2a\" is not a valid zone id if the Databricks deployment resides in the \"us-east-1\" region. This is an optional field at cluster creation, and if not specified, a default zone will be used. The list of available zones as well as the default value can be found by using the `List Zones` method."
      }
    ]
  },
  {
    "name": "azure_attributes",
    "type": "object",
    "description": "Attributes related to instance pools running on Azure. If not specified at pool creation, a set of default values will be used.",
    "children": [
      {
        "name": "availability",
        "type": "string",
        "description": "Availability type used for the spot nodes. (ON_DEMAND_AZURE, SPOT_AZURE)"
      },
      {
        "name": "spot_bid_max_price",
        "type": "number",
        "description": "With variable pricing, you have option to set a max price, in US dollars (USD) For example, the value 2 would be a max price of $2.00 USD per hour. If you set the max price to be -1, the VM won't be evicted based on price. The price for the VM will be the current price for spot or the price for a standard VM, which ever is less, as long as there is capacity and quota available."
      }
    ]
  },
  {
    "name": "custom_tags",
    "type": "object",
    "description": "Additional tags for pool resources. Databricks will tag all pool resources (e.g., AWS instances and EBS volumes) with these tags in addition to `default_tags`. Notes: - Currently, Databricks allows at most 45 custom tags"
  },
  {
    "name": "default_tags",
    "type": "object",
    "description": "Tags that are added by Databricks regardless of any ``custom_tags``, including: - Vendor: Databricks - InstancePoolCreator: &lt;user_id_of_creator&gt; - InstancePoolName: &lt;name_of_pool&gt; - InstancePoolId: &lt;id_of_pool&gt;"
  },
  {
    "name": "disk_spec",
    "type": "object",
    "description": "Defines the specification of the disks that will be attached to all spark containers.",
    "children": [
      {
        "name": "disk_count",
        "type": "integer",
        "description": "The number of disks launched for each instance: - This feature is only enabled for supported node types. - Users can choose up to the limit of the disks supported by the node type. - For node types with no OS disk, at least one disk must be specified; otherwise, cluster creation will fail. If disks are attached, Databricks will configure Spark to use only the disks for scratch storage, because heterogenously sized scratch devices can lead to inefficient disk utilization. If no disks are attached, Databricks will configure Spark to use instance store disks. Note: If disks are specified, then the Spark configuration `spark.local.dir` will be overridden. Disks will be mounted at: - For AWS: `/ebs0`, `/ebs1`, and etc. - For Azure: `/remote_volume0`, `/remote_volume1`, and etc."
      },
      {
        "name": "disk_iops",
        "type": "integer",
        "description": ""
      },
      {
        "name": "disk_size",
        "type": "integer",
        "description": "The size of each disk (in GiB) launched for each instance. Values must fall into the supported range for a particular instance type. For AWS: - General Purpose SSD: 100 - 4096 GiB - Throughput Optimized HDD: 500 - 4096 GiB For Azure: - Premium LRS (SSD): 1 - 1023 GiB - Standard LRS (HDD): 1- 1023 GiB"
      },
      {
        "name": "disk_throughput",
        "type": "integer",
        "description": ""
      },
      {
        "name": "disk_type",
        "type": "object",
        "description": "The type of disks that will be launched with this cluster.",
        "children": [
          {
            "name": "azure_disk_volume_type",
            "type": "string",
            "description": "All Azure Disk types that Databricks supports. See<br />https://docs.microsoft.com/en-us/azure/storage/storage-about-disks-and-vhds-linux#types-of-disks (PREMIUM_LRS, STANDARD_LRS)"
          },
          {
            "name": "ebs_volume_type",
            "type": "string",
            "description": "All EBS volume types that Databricks supports. See https://aws.amazon.com/ebs/details/ for<br />details. (GENERAL_PURPOSE_SSD, THROUGHPUT_OPTIMIZED_HDD)"
          }
        ]
      }
    ]
  },
  {
    "name": "enable_elastic_disk",
    "type": "boolean",
    "description": "Autoscaling Local Storage: when enabled, this instances in this pool will dynamically acquire additional disk space when its Spark workers are running low on disk space. In AWS, this feature requires specific AWS permissions to function correctly - refer to the User Guide for more details."
  },
  {
    "name": "gcp_attributes",
    "type": "object",
    "description": "Attributes related to instance pools running on Google Cloud Platform. If not specified at pool creation, a set of default values will be used.",
    "children": [
      {
        "name": "gcp_availability",
        "type": "string",
        "description": "This field determines whether the instance pool will contain preemptible VMs, on-demand VMs, or<br />preemptible VMs with a fallback to on-demand VMs if the former is unavailable. (ON_DEMAND_GCP, PREEMPTIBLE_GCP, PREEMPTIBLE_WITH_FALLBACK_GCP)"
      },
      {
        "name": "local_ssd_count",
        "type": "integer",
        "description": "If provided, each node in the instance pool will have this number of local SSDs attached. Each local SSD is 375GB in size. Refer to [GCP documentation] for the supported number of local SSDs for each instance type. [GCP documentation]: https://cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds"
      },
      {
        "name": "zone_id",
        "type": "string",
        "description": "Identifier for the availability zone/datacenter in which the cluster resides. This string will be of a form like \"us-west1-a\". The provided availability zone must be in the same region as the Databricks workspace. For example, \"us-west1-a\" is not a valid zone id if the Databricks workspace resides in the \"us-east1\" region. This is an optional field at instance pool creation, and if not specified, a default zone will be used. This field can be one of the following: - \"HA\" =&gt; High availability, spread nodes across availability zones for a Databricks deployment region - A GCP availability zone =&gt; Pick One of the available zones for (machine type + region) from https://cloud.google.com/compute/docs/regions-zones (e.g. \"us-west1-a\"). If empty, Databricks picks an availability zone to schedule the cluster on."
      }
    ]
  },
  {
    "name": "idle_instance_autotermination_minutes",
    "type": "integer",
    "description": "Automatically terminates the extra instances in the pool cache after they are inactive for this time in minutes if min_idle_instances requirement is already met. If not set, the extra pool instances will be automatically terminated after a default timeout. If specified, the threshold must be between 0 and 10000 minutes. Users can also set this value to 0 to instantly remove idle instances from the cache if min cache size could still hold."
  },
  {
    "name": "max_capacity",
    "type": "integer",
    "description": "Maximum number of outstanding instances to keep in the pool, including both instances used by clusters and idle instances. Clusters that require further instance provisioning will fail during upsize requests."
  },
  {
    "name": "min_idle_instances",
    "type": "integer",
    "description": "Minimum number of idle instances to keep in the instance pool"
  },
  {
    "name": "node_type_flexibility",
    "type": "object",
    "description": "Flexible node type configuration for the pool.",
    "children": [
      {
        "name": "alternate_node_type_ids",
        "type": "array",
        "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
      }
    ]
  },
  {
    "name": "preloaded_docker_images",
    "type": "array",
    "description": "Custom Docker Image BYOC",
    "children": [
      {
        "name": "basic_auth",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "password",
            "type": "string",
            "description": ""
          },
          {
            "name": "username",
            "type": "string",
            "description": "Name of the user"
          }
        ]
      },
      {
        "name": "url",
        "type": "string",
        "description": "URL of the docker image."
      }
    ]
  },
  {
    "name": "preloaded_spark_versions",
    "type": "array",
    "description": "A list containing at most one preloaded Spark image version for the pool. Pool-backed clusters started with the preloaded Spark version will start faster. A list of available Spark versions can be retrieved by using the :method:clusters/sparkVersions API call."
  },
  {
    "name": "remote_disk_throughput",
    "type": "integer",
    "description": "If set, what the configurable throughput (in Mb/s) for the remote disk is. Currently only supported for GCP HYPERDISK_BALANCED types."
  },
  {
    "name": "state",
    "type": "string",
    "description": "Current state of the instance pool. (ACTIVE, DELETED, STOPPED)"
  },
  {
    "name": "stats",
    "type": "object",
    "description": "Usage statistics about the instance pool.",
    "children": [
      {
        "name": "idle_count",
        "type": "integer",
        "description": ""
      },
      {
        "name": "pending_idle_count",
        "type": "integer",
        "description": "Number of pending instances in the pool that are NOT part of a cluster."
      },
      {
        "name": "pending_used_count",
        "type": "integer",
        "description": "Number of pending instances in the pool that are part of a cluster."
      },
      {
        "name": "used_count",
        "type": "integer",
        "description": "Number of active instances in the pool that are part of a cluster."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Status of failed pending instances in the pool.",
    "children": [
      {
        "name": "pending_instance_errors",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "instance_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "message",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "total_initial_remote_disk_size",
    "type": "integer",
    "description": "If set, what the total initial volume size (in GB) of the remote disks should be. Currently only supported for GCP HYPERDISK_BALANCED types."
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
    <td><a href="#parameter-instance_pool_id"><code>instance_pool_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Retrieve the information for an instance pool based on its identifier.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets a list of instance pools with their statistics.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-instance_pool_name"><code>instance_pool_name</code></a>, <a href="#parameter-node_type_id"><code>node_type_id</code></a></td>
    <td></td>
    <td>Creates a new instance pool using idle and ready-to-use cloud instances.</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-instance_pool_id"><code>instance_pool_id</code></a>, <a href="#parameter-instance_pool_name"><code>instance_pool_name</code></a>, <a href="#parameter-node_type_id"><code>node_type_id</code></a></td>
    <td></td>
    <td>Modifies the configuration of an existing instance pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Deletes the instance pool permanently. The idle instances in the pool are terminated asynchronously.</td>
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
<tr id="parameter-instance_pool_id">
    <td><CopyableCode code="instance_pool_id" /></td>
    <td><code>string</code></td>
    <td>The canonical unique identifier for the instance pool.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
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

Retrieve the information for an instance pool based on its identifier.

```sql
SELECT
instance_pool_id,
node_type_id,
instance_pool_name,
aws_attributes,
azure_attributes,
custom_tags,
default_tags,
disk_spec,
enable_elastic_disk,
gcp_attributes,
idle_instance_autotermination_minutes,
max_capacity,
min_idle_instances,
node_type_flexibility,
preloaded_docker_images,
preloaded_spark_versions,
remote_disk_throughput,
state,
stats,
status,
total_initial_remote_disk_size
FROM databricks_workspace.compute.instance_pools
WHERE instance_pool_id = '{{ instance_pool_id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of instance pools with their statistics.

```sql
SELECT
instance_pool_id,
node_type_id,
instance_pool_name,
aws_attributes,
azure_attributes,
custom_tags,
default_tags,
disk_spec,
enable_elastic_disk,
gcp_attributes,
idle_instance_autotermination_minutes,
max_capacity,
min_idle_instances,
node_type_flexibility,
preloaded_docker_images,
preloaded_spark_versions,
remote_disk_throughput,
state,
stats,
status,
total_initial_remote_disk_size
FROM databricks_workspace.compute.instance_pools
WHERE workspace = '{{ workspace }}' -- required
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

Creates a new instance pool using idle and ready-to-use cloud instances.

```sql
INSERT INTO databricks_workspace.compute.instance_pools (
instance_pool_name,
node_type_id,
aws_attributes,
azure_attributes,
custom_tags,
disk_spec,
enable_elastic_disk,
gcp_attributes,
idle_instance_autotermination_minutes,
max_capacity,
min_idle_instances,
node_type_flexibility,
preloaded_docker_images,
preloaded_spark_versions,
remote_disk_throughput,
total_initial_remote_disk_size,
workspace
)
SELECT 
'{{ instance_pool_name }}' /* required */,
'{{ node_type_id }}' /* required */,
'{{ aws_attributes }}',
'{{ azure_attributes }}',
'{{ custom_tags }}',
'{{ disk_spec }}',
{{ enable_elastic_disk }},
'{{ gcp_attributes }}',
{{ idle_instance_autotermination_minutes }},
{{ max_capacity }},
{{ min_idle_instances }},
'{{ node_type_flexibility }}',
'{{ preloaded_docker_images }}',
'{{ preloaded_spark_versions }}',
{{ remote_disk_throughput }},
{{ total_initial_remote_disk_size }},
'{{ workspace }}'
RETURNING
instance_pool_id
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: instance_pools
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the instance_pools resource.
    - name: instance_pool_name
      value: "{{ instance_pool_name }}"
      description: |
        Pool name requested by the user. Pool name must be unique. Length must be between 1 and 100 characters.
    - name: node_type_id
      value: "{{ node_type_id }}"
      description: |
        This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads. A list of available node types can be retrieved by using the :method:clusters/listNodeTypes API call.
    - name: aws_attributes
      description: |
        Attributes related to instance pools running on Amazon Web Services. If not specified at pool creation, a set of default values will be used.
      value:
        availability: "{{ availability }}"
        instance_profile_arn: "{{ instance_profile_arn }}"
        spot_bid_price_percent: {{ spot_bid_price_percent }}
        zone_id: "{{ zone_id }}"
    - name: azure_attributes
      description: |
        Attributes related to instance pools running on Azure. If not specified at pool creation, a set of default values will be used.
      value:
        availability: "{{ availability }}"
        spot_bid_max_price: {{ spot_bid_max_price }}
    - name: custom_tags
      value: "{{ custom_tags }}"
      description: |
        Additional tags for pool resources. Databricks will tag all pool resources (e.g., AWS instances and EBS volumes) with these tags in addition to \`default_tags\`. Notes: - Currently, Databricks allows at most 45 custom tags
    - name: disk_spec
      description: |
        Defines the specification of the disks that will be attached to all spark containers.
      value:
        disk_count: {{ disk_count }}
        disk_iops: {{ disk_iops }}
        disk_size: {{ disk_size }}
        disk_throughput: {{ disk_throughput }}
        disk_type:
          azure_disk_volume_type: "{{ azure_disk_volume_type }}"
          ebs_volume_type: "{{ ebs_volume_type }}"
    - name: enable_elastic_disk
      value: {{ enable_elastic_disk }}
      description: |
        Autoscaling Local Storage: when enabled, this instances in this pool will dynamically acquire additional disk space when its Spark workers are running low on disk space. In AWS, this feature requires specific AWS permissions to function correctly - refer to the User Guide for more details.
    - name: gcp_attributes
      description: |
        Attributes related to instance pools running on Google Cloud Platform. If not specified at pool creation, a set of default values will be used.
      value:
        gcp_availability: "{{ gcp_availability }}"
        local_ssd_count: {{ local_ssd_count }}
        zone_id: "{{ zone_id }}"
    - name: idle_instance_autotermination_minutes
      value: {{ idle_instance_autotermination_minutes }}
      description: |
        Automatically terminates the extra instances in the pool cache after they are inactive for this time in minutes if min_idle_instances requirement is already met. If not set, the extra pool instances will be automatically terminated after a default timeout. If specified, the threshold must be between 0 and 10000 minutes. Users can also set this value to 0 to instantly remove idle instances from the cache if min cache size could still hold.
    - name: max_capacity
      value: {{ max_capacity }}
      description: |
        Maximum number of outstanding instances to keep in the pool, including both instances used by clusters and idle instances. Clusters that require further instance provisioning will fail during upsize requests.
    - name: min_idle_instances
      value: {{ min_idle_instances }}
      description: |
        Minimum number of idle instances to keep in the instance pool
    - name: node_type_flexibility
      description: |
        Flexible node type configuration for the pool.
      value:
        alternate_node_type_ids:
          - "{{ alternate_node_type_ids }}"
    - name: preloaded_docker_images
      description: |
        Custom Docker Image BYOC
      value:
        - basic_auth:
            password: "{{ password }}"
            username: "{{ username }}"
          url: "{{ url }}"
    - name: preloaded_spark_versions
      value:
        - "{{ preloaded_spark_versions }}"
      description: |
        A list containing at most one preloaded Spark image version for the pool. Pool-backed clusters started with the preloaded Spark version will start faster. A list of available Spark versions can be retrieved by using the :method:clusters/sparkVersions API call.
    - name: remote_disk_throughput
      value: {{ remote_disk_throughput }}
      description: |
        If set, what the configurable throughput (in Mb/s) for the remote disk is. Currently only supported for GCP HYPERDISK_BALANCED types.
    - name: total_initial_remote_disk_size
      value: {{ total_initial_remote_disk_size }}
      description: |
        If set, what the total initial volume size (in GB) of the remote disks should be. Currently only supported for GCP HYPERDISK_BALANCED types.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="replace"
    values={[
        { label: 'replace', value: 'replace' }
    ]}
>
<TabItem value="replace">

Modifies the configuration of an existing instance pool.

```sql
REPLACE databricks_workspace.compute.instance_pools
SET 
instance_pool_id = '{{ instance_pool_id }}',
instance_pool_name = '{{ instance_pool_name }}',
node_type_id = '{{ node_type_id }}',
custom_tags = '{{ custom_tags }}',
idle_instance_autotermination_minutes = {{ idle_instance_autotermination_minutes }},
max_capacity = {{ max_capacity }},
min_idle_instances = {{ min_idle_instances }},
node_type_flexibility = '{{ node_type_flexibility }}',
remote_disk_throughput = {{ remote_disk_throughput }},
total_initial_remote_disk_size = {{ total_initial_remote_disk_size }}
WHERE 
workspace = '{{ workspace }}' --required
AND instance_pool_id = '{{ instance_pool_id }}' --required
AND instance_pool_name = '{{ instance_pool_name }}' --required
AND node_type_id = '{{ node_type_id }}' --required;
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

Deletes the instance pool permanently. The idle instances in the pool are terminated asynchronously.

```sql
DELETE FROM databricks_workspace.compute.instance_pools
WHERE workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

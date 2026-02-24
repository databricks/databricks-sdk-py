---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.clusters" /></td></tr>
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
    "name": "cluster_id",
    "type": "string",
    "description": "Canonical identifier for the cluster. This id is retained during cluster restarts and resizes, while each new cluster has a globally unique id."
  },
  {
    "name": "driver_instance_pool_id",
    "type": "string",
    "description": "The optional ID of the instance pool for the driver of the cluster belongs. The pool cluster uses the instance pool with id (instance_pool_id) if the driver pool is not assigned."
  },
  {
    "name": "driver_node_type_id",
    "type": "string",
    "description": "The node type of the Spark driver. Note that this field is optional; if unset, the driver node type will be set as the same value as `node_type_id` defined above. This field, along with node_type_id, should not be set if virtual_cluster_size is set. If both driver_node_type_id, node_type_id, and virtual_cluster_size are specified, driver_node_type_id and node_type_id take precedence."
  },
  {
    "name": "instance_pool_id",
    "type": "string",
    "description": "The optional ID of the instance pool to which the cluster belongs."
  },
  {
    "name": "node_type_id",
    "type": "string",
    "description": "This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads. A list of available node types can be retrieved by using the :method:clusters/listNodeTypes API call."
  },
  {
    "name": "policy_id",
    "type": "string",
    "description": "The ID of the cluster policy used to create the cluster if applicable."
  },
  {
    "name": "spark_context_id",
    "type": "integer",
    "description": "A canonical SparkContext identifier. This value *does* change when the Spark driver restarts. The pair `(cluster_id, spark_context_id)` is a globally unique identifier over all Spark contexts."
  },
  {
    "name": "cluster_name",
    "type": "string",
    "description": "Cluster name requested by the user. This doesn't have to be unique. If not specified at creation, the cluster name will be an empty string. For job clusters, the cluster name is automatically set based on the job and job run IDs."
  },
  {
    "name": "creator_user_name",
    "type": "string",
    "description": "Creator user name. The field won't be included in the response if the user has already been deleted."
  },
  {
    "name": "single_user_name",
    "type": "string",
    "description": "Single user name if data_security_mode is `SINGLE_USER`"
  },
  {
    "name": "autoscale",
    "type": "object",
    "description": "Parameters needed in order to automatically scale clusters up and down based on load. Note: autoscaling works best with DB runtime versions 3.0 or later.",
    "children": [
      {
        "name": "max_workers",
        "type": "integer",
        "description": ""
      },
      {
        "name": "min_workers",
        "type": "integer",
        "description": "The minimum number of workers to which the cluster can scale down when underutilized. It is also the initial number of workers the cluster will have after creation."
      }
    ]
  },
  {
    "name": "autotermination_minutes",
    "type": "integer",
    "description": "Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this cluster will not be automatically terminated. If specified, the threshold must be between 10 and 10000 minutes. Users can also set this value to 0 to explicitly disable automatic termination."
  },
  {
    "name": "aws_attributes",
    "type": "object",
    "description": "Attributes related to clusters running on Amazon Web Services. If not specified at cluster creation, a set of default values will be used.",
    "children": [
      {
        "name": "availability",
        "type": "string",
        "description": "Availability type used for all subsequent nodes past the `first_on_demand` ones.<br /><br />Note: If `first_on_demand` is zero, this availability type will be used for the entire cluster. (ON_DEMAND, SPOT, SPOT_WITH_FALLBACK)"
      },
      {
        "name": "ebs_volume_count",
        "type": "integer",
        "description": "The number of volumes launched for each instance. Users can choose up to 10 volumes. This feature is only enabled for supported node types. Legacy node types cannot specify custom EBS volumes. For node types with no instance store, at least one EBS volume needs to be specified; otherwise, cluster creation will fail. These EBS volumes will be mounted at `/ebs0`, `/ebs1`, and etc. Instance store volumes will be mounted at `/local_disk0`, `/local_disk1`, and etc. If EBS volumes are attached, Databricks will configure Spark to use only the EBS volumes for scratch storage because heterogenously sized scratch devices can lead to inefficient disk utilization. If no EBS volumes are attached, Databricks will configure Spark to use instance store volumes. Please note that if EBS volumes are specified, then the Spark configuration `spark.local.dir` will be overridden."
      },
      {
        "name": "ebs_volume_iops",
        "type": "integer",
        "description": "If using gp3 volumes, what IOPS to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used."
      },
      {
        "name": "ebs_volume_size",
        "type": "integer",
        "description": "The size of each EBS volume (in GiB) launched for each instance. For general purpose SSD, this value must be within the range 100 - 4096. For throughput optimized HDD, this value must be within the range 500 - 4096."
      },
      {
        "name": "ebs_volume_throughput",
        "type": "integer",
        "description": "If using gp3 volumes, what throughput to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used."
      },
      {
        "name": "ebs_volume_type",
        "type": "string",
        "description": "The type of EBS volumes that will be launched with this cluster. (GENERAL_PURPOSE_SSD, THROUGHPUT_OPTIMIZED_HDD)"
      },
      {
        "name": "first_on_demand",
        "type": "integer",
        "description": "The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. If this value is greater than 0, the cluster driver node in particular will be placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
      },
      {
        "name": "instance_profile_arn",
        "type": "string",
        "description": "Nodes for this cluster will only be placed on AWS instances with this instance profile. If ommitted, nodes will be placed on instances without an IAM instance profile. The instance profile must have previously been added to the Databricks environment by an account administrator. This feature may only be available to certain customer plans."
      },
      {
        "name": "spot_bid_price_percent",
        "type": "integer",
        "description": "The bid price for AWS spot instances, as a percentage of the corresponding instance type's on-demand price. For example, if this field is set to 50, and the cluster needs a new `r3.xlarge` spot instance, then the bid price is half of the price of on-demand `r3.xlarge` instances. Similarly, if this field is set to 200, the bid price is twice the price of on-demand `r3.xlarge` instances. If not specified, the default value is 100. When spot instances are requested for this cluster, only spot instances whose bid price percentage matches this field will be considered. Note that, for safety, we enforce this field to be no more than 10000."
      },
      {
        "name": "zone_id",
        "type": "string",
        "description": "Identifier for the availability zone/datacenter in which the cluster resides. This string will be of a form like \"us-west-2a\". The provided availability zone must be in the same region as the Databricks deployment. For example, \"us-west-2a\" is not a valid zone id if the Databricks deployment resides in the \"us-east-1\" region. This is an optional field at cluster creation, and if not specified, the zone \"auto\" will be used. If the zone specified is \"auto\", will try to place cluster in a zone with high availability, and will retry placement in a different AZ if there is not enough capacity. The list of available zones as well as the default value can be found by using the `List Zones` method."
      }
    ]
  },
  {
    "name": "azure_attributes",
    "type": "object",
    "description": "Attributes related to clusters running on Microsoft Azure. If not specified at cluster creation, a set of default values will be used.",
    "children": [
      {
        "name": "availability",
        "type": "string",
        "description": "Availability type used for all subsequent nodes past the `first_on_demand` ones. Note: If `first_on_demand` is zero, this availability type will be used for the entire cluster. (ON_DEMAND_AZURE, SPOT_AZURE, SPOT_WITH_FALLBACK_AZURE)"
      },
      {
        "name": "first_on_demand",
        "type": "integer",
        "description": "The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
      },
      {
        "name": "log_analytics_info",
        "type": "object",
        "description": "Defines values necessary to configure and run Azure Log Analytics agent",
        "children": [
          {
            "name": "log_analytics_primary_key",
            "type": "string",
            "description": ""
          },
          {
            "name": "log_analytics_workspace_id",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "spot_bid_max_price",
        "type": "number",
        "description": "The max bid price to be used for Azure spot instances. The Max price for the bid cannot be higher than the on-demand price of the instance. If not specified, the default value is -1, which specifies that the instance cannot be evicted on the basis of price, and only on the basis of availability. Further, the value should &gt; 0 or -1."
      }
    ]
  },
  {
    "name": "cluster_cores",
    "type": "number",
    "description": "Number of CPU cores available for this cluster. Note that this can be fractional, e.g. 7.5 cores, since certain node types are configured to share cores between Spark nodes on the same instance."
  },
  {
    "name": "cluster_log_conf",
    "type": "object",
    "description": "The configuration for delivering spark logs to a long-term storage destination. Three kinds of destinations (DBFS, S3 and Unity Catalog volumes) are supported. Only one destination can be specified for one cluster. If the conf is given, the logs will be delivered to the destination every `5 mins`. The destination of driver logs is `$destination/$clusterId/driver`, while the destination of executor logs is `$destination/$clusterId/executor`.",
    "children": [
      {
        "name": "dbfs",
        "type": "object",
        "description": "destination needs to be provided. e.g. `&#123; \"dbfs\" : &#123; \"destination\" : \"dbfs:/home/cluster_log\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "dbfs destination, e.g. `dbfs:/my/path`"
          }
        ]
      },
      {
        "name": "s3",
        "type": "object",
        "description": "destination and either the region or endpoint need to be provided. e.g. `&#123; \"s3\": &#123; \"destination\" : \"s3://cluster_log_bucket/prefix\", \"region\" : \"us-west-2\" &#125; &#125;` Cluster iam role is used to access s3, please make sure the cluster iam role in `instance_profile_arn` has permission to write data to the s3 destination.",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "S3 destination, e.g. `s3://my-bucket/some-prefix` Note that logs will be delivered using cluster iam role, please make sure you set cluster iam role and the role has write access to the destination. Please also note that you cannot use AWS keys to deliver logs."
          },
          {
            "name": "canned_acl",
            "type": "string",
            "description": "(Optional) Set canned access control list for the logs, e.g. `bucket-owner-full-control`. If `canned_cal` is set, please make sure the cluster iam role has `s3:PutObjectAcl` permission on the destination bucket and prefix. The full list of possible canned acl can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl. Please also note that by default only the object owner gets full controls. If you are using cross account role for writing data, you may want to set `bucket-owner-full-control` to make bucket owner able to read the logs."
          },
          {
            "name": "enable_encryption",
            "type": "boolean",
            "description": "(Optional) Flag to enable server side encryption, `false` by default."
          },
          {
            "name": "encryption_type",
            "type": "string",
            "description": "(Optional) The encryption type, it could be `sse-s3` or `sse-kms`. It will be used only when encryption is enabled and the default type is `sse-s3`."
          },
          {
            "name": "endpoint",
            "type": "string",
            "description": "S3 endpoint, e.g. `https://s3-us-west-2.amazonaws.com`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
          },
          {
            "name": "kms_key",
            "type": "string",
            "description": "(Optional) Kms key which will be used if encryption is enabled and encryption type is set to `sse-kms`."
          },
          {
            "name": "region",
            "type": "string",
            "description": "S3 region, e.g. `us-west-2`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
          }
        ]
      },
      {
        "name": "volumes",
        "type": "object",
        "description": "destination needs to be provided, e.g. `&#123; \"volumes\": &#123; \"destination\": \"/Volumes/catalog/schema/volume/cluster_log\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "UC Volumes destination, e.g. `/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh` or `dbfs:/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh`"
          }
        ]
      }
    ]
  },
  {
    "name": "cluster_log_status",
    "type": "object",
    "description": "Cluster log delivery status.",
    "children": [
      {
        "name": "last_attempted",
        "type": "integer",
        "description": "The timestamp of last attempt. If the last attempt fails, `last_exception` will contain the exception in the last attempt."
      },
      {
        "name": "last_exception",
        "type": "string",
        "description": "The exception thrown in the last attempt, it would be null (omitted in the response) if there is no exception in last attempted."
      }
    ]
  },
  {
    "name": "cluster_memory_mb",
    "type": "integer",
    "description": "Total amount of cluster memory, in megabytes"
  },
  {
    "name": "cluster_source",
    "type": "string",
    "description": "Determines whether the cluster was created by a user through the UI, created by the Databricks Jobs Scheduler, or through an API request. (API, JOB, MODELS, PIPELINE, PIPELINE_MAINTENANCE, SQL, UI)"
  },
  {
    "name": "custom_tags",
    "type": "object",
    "description": "Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS instances and EBS volumes) with these tags in addition to `default_tags`. Notes: - Currently, Databricks allows at most 45 custom tags - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags"
  },
  {
    "name": "data_security_mode",
    "type": "string",
    "description": "Data security mode decides what data governance model to use when accessing data from a cluster.<br /><br />The following modes can only be used when `kind = CLASSIC_PREVIEW`. * `DATA_SECURITY_MODE_AUTO`:<br />Databricks will choose the most appropriate access mode depending on your compute configuration.<br />* `DATA_SECURITY_MODE_STANDARD`: Alias for `USER_ISOLATION`. * `DATA_SECURITY_MODE_DEDICATED`:<br />Alias for `SINGLE_USER`.<br /><br />The following modes can be used regardless of `kind`. * `NONE`: No security isolation for<br />multiple users sharing the cluster. Data governance features are not available in this mode. *<br />`SINGLE_USER`: A secure cluster that can only be exclusively used by a single user specified in<br />`single_user_name`. Most programming languages, cluster features and data governance features<br />are available in this mode. * `USER_ISOLATION`: A secure cluster that can be shared by multiple<br />users. Cluster users are fully isolated so that they cannot see each other's data and<br />credentials. Most data governance features are supported in this mode. But programming languages<br />and cluster features might be limited.<br /><br />The following modes are deprecated starting with Databricks Runtime 15.0 and will be removed for<br />future Databricks Runtime versions:<br /><br />* `LEGACY_TABLE_ACL`: This mode is for users migrating from legacy Table ACL clusters. *<br />`LEGACY_PASSTHROUGH`: This mode is for users migrating from legacy Passthrough on high<br />concurrency clusters. * `LEGACY_SINGLE_USER`: This mode is for users migrating from legacy<br />Passthrough on standard clusters. * `LEGACY_SINGLE_USER_STANDARD`: This mode provides a way that<br />doesn’t have UC nor passthrough enabled. (DATA_SECURITY_MODE_AUTO, DATA_SECURITY_MODE_DEDICATED, DATA_SECURITY_MODE_STANDARD, LEGACY_PASSTHROUGH, LEGACY_SINGLE_USER, LEGACY_SINGLE_USER_STANDARD, LEGACY_TABLE_ACL, NONE, SINGLE_USER, USER_ISOLATION)"
  },
  {
    "name": "default_tags",
    "type": "object",
    "description": "Tags that are added by Databricks regardless of any `custom_tags`, including: - Vendor: Databricks - Creator: &lt;username_of_creator&gt; - ClusterName: &lt;name_of_cluster&gt; - ClusterId: &lt;id_of_cluster&gt; - Name: &lt;Databricks internal use&gt;"
  },
  {
    "name": "docker_image",
    "type": "object",
    "description": "Custom docker image BYOC",
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
    "name": "driver",
    "type": "object",
    "description": "Node on which the Spark driver resides. The driver node contains the Spark master and the Databricks application that manages the per-notebook Spark REPLs.",
    "children": [
      {
        "name": "host_private_ip",
        "type": "string",
        "description": "The private IP address of the host instance."
      },
      {
        "name": "instance_id",
        "type": "string",
        "description": "Globally unique identifier for the host instance from the cloud provider."
      },
      {
        "name": "node_aws_attributes",
        "type": "object",
        "description": "Attributes specific to AWS for a Spark node.",
        "children": [
          {
            "name": "is_spot",
            "type": "boolean",
            "description": "Whether this node is on an Amazon spot instance."
          }
        ]
      },
      {
        "name": "node_id",
        "type": "string",
        "description": "Globally unique identifier for this node."
      },
      {
        "name": "private_ip",
        "type": "string",
        "description": "Private IP address (typically a 10.x.x.x address) of the Spark node. Note that this is different from the private IP address of the host instance."
      },
      {
        "name": "public_dns",
        "type": "string",
        "description": "Public DNS address of this node. This address can be used to access the Spark JDBC server on the driver node. To communicate with the JDBC server, traffic must be manually authorized by adding security group rules to the \"worker-unmanaged\" security group via the AWS console."
      },
      {
        "name": "start_timestamp",
        "type": "integer",
        "description": "The timestamp (in millisecond) when the Spark node is launched."
      }
    ]
  },
  {
    "name": "driver_node_type_flexibility",
    "type": "object",
    "description": "Flexible node type configuration for the driver node.",
    "children": [
      {
        "name": "alternate_node_type_ids",
        "type": "array",
        "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
      }
    ]
  },
  {
    "name": "enable_elastic_disk",
    "type": "boolean",
    "description": "Autoscaling Local Storage: when enabled, this cluster will dynamically acquire additional disk space when its Spark workers are running low on disk space."
  },
  {
    "name": "enable_local_disk_encryption",
    "type": "boolean",
    "description": "Whether to enable LUKS on cluster VMs' local disks"
  },
  {
    "name": "executors",
    "type": "array",
    "description": "Nodes on which the Spark executors reside.",
    "children": [
      {
        "name": "host_private_ip",
        "type": "string",
        "description": "The private IP address of the host instance."
      },
      {
        "name": "instance_id",
        "type": "string",
        "description": "Globally unique identifier for the host instance from the cloud provider."
      },
      {
        "name": "node_aws_attributes",
        "type": "object",
        "description": "Attributes specific to AWS for a Spark node.",
        "children": [
          {
            "name": "is_spot",
            "type": "boolean",
            "description": "Whether this node is on an Amazon spot instance."
          }
        ]
      },
      {
        "name": "node_id",
        "type": "string",
        "description": "Globally unique identifier for this node."
      },
      {
        "name": "private_ip",
        "type": "string",
        "description": "Private IP address (typically a 10.x.x.x address) of the Spark node. Note that this is different from the private IP address of the host instance."
      },
      {
        "name": "public_dns",
        "type": "string",
        "description": "Public DNS address of this node. This address can be used to access the Spark JDBC server on the driver node. To communicate with the JDBC server, traffic must be manually authorized by adding security group rules to the \"worker-unmanaged\" security group via the AWS console."
      },
      {
        "name": "start_timestamp",
        "type": "integer",
        "description": "The timestamp (in millisecond) when the Spark node is launched."
      }
    ]
  },
  {
    "name": "gcp_attributes",
    "type": "object",
    "description": "Attributes related to clusters running on Google Cloud Platform. If not specified at cluster creation, a set of default values will be used.",
    "children": [
      {
        "name": "availability",
        "type": "string",
        "description": "This field determines whether the spark executors will be scheduled to run on preemptible VMs, on-demand VMs, or preemptible VMs with a fallback to on-demand VMs if the former is unavailable. (ON_DEMAND_GCP, PREEMPTIBLE_GCP, PREEMPTIBLE_WITH_FALLBACK_GCP)"
      },
      {
        "name": "boot_disk_size",
        "type": "integer",
        "description": "Boot disk size in GB"
      },
      {
        "name": "first_on_demand",
        "type": "integer",
        "description": "The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
      },
      {
        "name": "google_service_account",
        "type": "string",
        "description": "If provided, the cluster will impersonate the google service account when accessing gcloud services (like GCS). The google service account must have previously been added to the Databricks environment by an account administrator."
      },
      {
        "name": "local_ssd_count",
        "type": "integer",
        "description": "If provided, each node (workers and driver) in the cluster will have this number of local SSDs attached. Each local SSD is 375GB in size. Refer to [GCP documentation] for the supported number of local SSDs for each instance type. [GCP documentation]: https://cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds"
      },
      {
        "name": "use_preemptible_executors",
        "type": "boolean",
        "description": "This field determines whether the spark executors will be scheduled to run on preemptible VMs (when set to true) versus standard compute engine VMs (when set to false; default). Note: Soon to be deprecated, use the 'availability' field instead."
      },
      {
        "name": "zone_id",
        "type": "string",
        "description": "Identifier for the availability zone in which the cluster resides. This can be one of the following: - \"HA\" =&gt; High availability, spread nodes across availability zones for a Databricks deployment region [default]. - \"AUTO\" =&gt; Databricks picks an availability zone to schedule the cluster on. - A GCP availability zone =&gt; Pick One of the available zones for (machine type + region) from https://cloud.google.com/compute/docs/regions-zones."
      }
    ]
  },
  {
    "name": "init_scripts",
    "type": "array",
    "description": "The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If `cluster_log_conf` is specified, init script logs are sent to `<destination>/<cluster-ID>/init_scripts`.",
    "children": [
      {
        "name": "abfss",
        "type": "object",
        "description": "destination needs to be provided, e.g. `abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<directory-name>`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "abfss destination, e.g. `abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<directory-name>`."
          }
        ]
      },
      {
        "name": "dbfs",
        "type": "object",
        "description": "destination needs to be provided. e.g. `&#123; \"dbfs\": &#123; \"destination\" : \"dbfs:/home/cluster_log\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "dbfs destination, e.g. `dbfs:/my/path`"
          }
        ]
      },
      {
        "name": "file",
        "type": "object",
        "description": "destination needs to be provided, e.g. `&#123; \"file\": &#123; \"destination\": \"file:/my/local/file.sh\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "gcs",
        "type": "object",
        "description": "destination needs to be provided, e.g. `&#123; \"gcs\": &#123; \"destination\": \"gs://my-bucket/file.sh\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "GCS destination/URI, e.g. `gs://my-bucket/some-prefix`"
          }
        ]
      },
      {
        "name": "s3",
        "type": "object",
        "description": "destination and either the region or endpoint need to be provided. e.g. `&#123; \\\"s3\\\": &#123; \\\"destination\\\": \\\"s3://cluster_log_bucket/prefix\\\", \\\"region\\\": \\\"us-west-2\\\" &#125; &#125;` Cluster iam role is used to access s3, please make sure the cluster iam role in `instance_profile_arn` has permission to write data to the s3 destination.",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "S3 destination, e.g. `s3://my-bucket/some-prefix` Note that logs will be delivered using cluster iam role, please make sure you set cluster iam role and the role has write access to the destination. Please also note that you cannot use AWS keys to deliver logs."
          },
          {
            "name": "canned_acl",
            "type": "string",
            "description": "(Optional) Set canned access control list for the logs, e.g. `bucket-owner-full-control`. If `canned_cal` is set, please make sure the cluster iam role has `s3:PutObjectAcl` permission on the destination bucket and prefix. The full list of possible canned acl can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl. Please also note that by default only the object owner gets full controls. If you are using cross account role for writing data, you may want to set `bucket-owner-full-control` to make bucket owner able to read the logs."
          },
          {
            "name": "enable_encryption",
            "type": "boolean",
            "description": "(Optional) Flag to enable server side encryption, `false` by default."
          },
          {
            "name": "encryption_type",
            "type": "string",
            "description": "(Optional) The encryption type, it could be `sse-s3` or `sse-kms`. It will be used only when encryption is enabled and the default type is `sse-s3`."
          },
          {
            "name": "endpoint",
            "type": "string",
            "description": "S3 endpoint, e.g. `https://s3-us-west-2.amazonaws.com`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
          },
          {
            "name": "kms_key",
            "type": "string",
            "description": "(Optional) Kms key which will be used if encryption is enabled and encryption type is set to `sse-kms`."
          },
          {
            "name": "region",
            "type": "string",
            "description": "S3 region, e.g. `us-west-2`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
          }
        ]
      },
      {
        "name": "volumes",
        "type": "object",
        "description": "destination needs to be provided. e.g. `&#123; \\\"volumes\\\" : &#123; \\\"destination\\\" : \\\"/Volumes/my-init.sh\\\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "UC Volumes destination, e.g. `/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh` or `dbfs:/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh`"
          }
        ]
      },
      {
        "name": "workspace",
        "type": "object",
        "description": "destination needs to be provided, e.g. `&#123; \"workspace\": &#123; \"destination\": \"/cluster-init-scripts/setup-datadog.sh\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "wsfs destination, e.g. `workspace:/cluster-init-scripts/setup-datadog.sh`"
          }
        ]
      }
    ]
  },
  {
    "name": "is_single_node",
    "type": "boolean",
    "description": "This field can only be used when `kind = CLASSIC_PREVIEW`. When set to true, Databricks will automatically set single node related `custom_tags`, `spark_conf`, and `num_workers`"
  },
  {
    "name": "jdbc_port",
    "type": "integer",
    "description": "Port on which Spark JDBC server is listening, in the driver nod. No service will be listeningon on this port in executor nodes."
  },
  {
    "name": "kind",
    "type": "string",
    "description": "The kind of compute described by this compute specification.<br /><br />Depending on `kind`, different validations and default values will be applied.<br /><br />Clusters with `kind = CLASSIC_PREVIEW` support the following fields, whereas clusters with no<br />specified `kind` do not. * [is_single_node](/api/workspace/clusters/create#is_single_node) *<br />[use_ml_runtime](/api/workspace/clusters/create#use_ml_runtime) *<br />[data_security_mode](/api/workspace/clusters/create#data_security_mode) set to<br />`DATA_SECURITY_MODE_AUTO`, `DATA_SECURITY_MODE_DEDICATED`, or `DATA_SECURITY_MODE_STANDARD`<br /><br />By using the [simple form], your clusters are automatically using `kind = CLASSIC_PREVIEW`.<br /><br />[simple form]: https://docs.databricks.com/compute/simple-form.html (CLASSIC_PREVIEW)"
  },
  {
    "name": "last_restarted_time",
    "type": "integer",
    "description": "the timestamp that the cluster was started/restarted"
  },
  {
    "name": "last_state_loss_time",
    "type": "integer",
    "description": "Time when the cluster driver last lost its state (due to a restart or driver failure)."
  },
  {
    "name": "num_workers",
    "type": "integer",
    "description": "Number of worker nodes that this cluster should have. A cluster has one Spark Driver and `num_workers` Executors for a total of `num_workers` + 1 Spark nodes. Note: When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual current number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field will immediately be updated to reflect the target size of 10 workers, whereas the workers listed in `spark_info` will gradually increase from 5 to 10 as the new nodes are provisioned."
  },
  {
    "name": "remote_disk_throughput",
    "type": "integer",
    "description": "If set, what the configurable throughput (in Mb/s) for the remote disk is. Currently only supported for GCP HYPERDISK_BALANCED disks."
  },
  {
    "name": "runtime_engine",
    "type": "string",
    "description": "Determines the cluster's runtime engine, either standard or Photon. This field is not compatible with legacy `spark_version` values that contain `-photon-`. Remove `-photon-` from the `spark_version` and set `runtime_engine` to `PHOTON`. If left unspecified, the runtime engine defaults to standard unless the spark_version contains -photon-, in which case Photon will be used. (NULL, PHOTON, STANDARD)"
  },
  {
    "name": "spark_conf",
    "type": "object",
    "description": "An object containing a set of optional, user-specified Spark configuration key-value pairs. Users can also pass in a string of extra JVM options to the driver and the executors via `spark.driver.extraJavaOptions` and `spark.executor.extraJavaOptions` respectively."
  },
  {
    "name": "spark_env_vars",
    "type": "object",
    "description": "An object containing a set of optional, user-specified environment variable key-value pairs. Please note that key-value pair of the form (X,Y) will be exported as is (i.e., `export X='Y'`) while launching the driver and workers. In order to specify an additional set of `SPARK_DAEMON_JAVA_OPTS`, we recommend appending them to `$SPARK_DAEMON_JAVA_OPTS` as shown in the example below. This ensures that all default databricks managed environmental variables are included as well. Example Spark environment variables: `&#123;\"SPARK_WORKER_MEMORY\": \"28000m\", \"SPARK_LOCAL_DIRS\": \"/local_disk0\"&#125;` or `&#123;\"SPARK_DAEMON_JAVA_OPTS\": \"$SPARK_DAEMON_JAVA_OPTS -Dspark.shuffle.service.enabled=true\"&#125;`"
  },
  {
    "name": "spark_version",
    "type": "string",
    "description": "The Spark version of the cluster, e.g. `3.3.x-scala2.11`. A list of available Spark versions can be retrieved by using the :method:clusters/sparkVersions API call."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains a snapshot of the latest user specified settings that were used to create/edit the cluster. Note: not included in the response of the ListClusters API.",
    "children": [
      {
        "name": "apply_policy_default_values",
        "type": "boolean",
        "description": "When set to true, fixed and default values from the policy will be used for fields that are omitted. When set to false, only fixed values from the policy will be applied."
      },
      {
        "name": "autoscale",
        "type": "object",
        "description": "Parameters needed in order to automatically scale clusters up and down based on load. Note: autoscaling works best with DB runtime versions 3.0 or later.",
        "children": [
          {
            "name": "max_workers",
            "type": "integer",
            "description": ""
          },
          {
            "name": "min_workers",
            "type": "integer",
            "description": "The minimum number of workers to which the cluster can scale down when underutilized. It is also the initial number of workers the cluster will have after creation."
          }
        ]
      },
      {
        "name": "autotermination_minutes",
        "type": "integer",
        "description": "Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this cluster will not be automatically terminated. If specified, the threshold must be between 10 and 10000 minutes. Users can also set this value to 0 to explicitly disable automatic termination."
      },
      {
        "name": "aws_attributes",
        "type": "object",
        "description": "Attributes related to clusters running on Amazon Web Services. If not specified at cluster creation, a set of default values will be used.",
        "children": [
          {
            "name": "availability",
            "type": "string",
            "description": "Availability type used for all subsequent nodes past the `first_on_demand` ones.<br /><br />Note: If `first_on_demand` is zero, this availability type will be used for the entire cluster. (ON_DEMAND, SPOT, SPOT_WITH_FALLBACK)"
          },
          {
            "name": "ebs_volume_count",
            "type": "integer",
            "description": "The number of volumes launched for each instance. Users can choose up to 10 volumes. This feature is only enabled for supported node types. Legacy node types cannot specify custom EBS volumes. For node types with no instance store, at least one EBS volume needs to be specified; otherwise, cluster creation will fail. These EBS volumes will be mounted at `/ebs0`, `/ebs1`, and etc. Instance store volumes will be mounted at `/local_disk0`, `/local_disk1`, and etc. If EBS volumes are attached, Databricks will configure Spark to use only the EBS volumes for scratch storage because heterogenously sized scratch devices can lead to inefficient disk utilization. If no EBS volumes are attached, Databricks will configure Spark to use instance store volumes. Please note that if EBS volumes are specified, then the Spark configuration `spark.local.dir` will be overridden."
          },
          {
            "name": "ebs_volume_iops",
            "type": "integer",
            "description": "If using gp3 volumes, what IOPS to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used."
          },
          {
            "name": "ebs_volume_size",
            "type": "integer",
            "description": "The size of each EBS volume (in GiB) launched for each instance. For general purpose SSD, this value must be within the range 100 - 4096. For throughput optimized HDD, this value must be within the range 500 - 4096."
          },
          {
            "name": "ebs_volume_throughput",
            "type": "integer",
            "description": "If using gp3 volumes, what throughput to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used."
          },
          {
            "name": "ebs_volume_type",
            "type": "string",
            "description": "The type of EBS volumes that will be launched with this cluster. (GENERAL_PURPOSE_SSD, THROUGHPUT_OPTIMIZED_HDD)"
          },
          {
            "name": "first_on_demand",
            "type": "integer",
            "description": "The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. If this value is greater than 0, the cluster driver node in particular will be placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
          },
          {
            "name": "instance_profile_arn",
            "type": "string",
            "description": "Nodes for this cluster will only be placed on AWS instances with this instance profile. If ommitted, nodes will be placed on instances without an IAM instance profile. The instance profile must have previously been added to the Databricks environment by an account administrator. This feature may only be available to certain customer plans."
          },
          {
            "name": "spot_bid_price_percent",
            "type": "integer",
            "description": "The bid price for AWS spot instances, as a percentage of the corresponding instance type's on-demand price. For example, if this field is set to 50, and the cluster needs a new `r3.xlarge` spot instance, then the bid price is half of the price of on-demand `r3.xlarge` instances. Similarly, if this field is set to 200, the bid price is twice the price of on-demand `r3.xlarge` instances. If not specified, the default value is 100. When spot instances are requested for this cluster, only spot instances whose bid price percentage matches this field will be considered. Note that, for safety, we enforce this field to be no more than 10000."
          },
          {
            "name": "zone_id",
            "type": "string",
            "description": "Identifier for the availability zone/datacenter in which the cluster resides. This string will be of a form like \"us-west-2a\". The provided availability zone must be in the same region as the Databricks deployment. For example, \"us-west-2a\" is not a valid zone id if the Databricks deployment resides in the \"us-east-1\" region. This is an optional field at cluster creation, and if not specified, the zone \"auto\" will be used. If the zone specified is \"auto\", will try to place cluster in a zone with high availability, and will retry placement in a different AZ if there is not enough capacity. The list of available zones as well as the default value can be found by using the `List Zones` method."
          }
        ]
      },
      {
        "name": "azure_attributes",
        "type": "object",
        "description": "Attributes related to clusters running on Microsoft Azure. If not specified at cluster creation, a set of default values will be used.",
        "children": [
          {
            "name": "availability",
            "type": "string",
            "description": "Availability type used for all subsequent nodes past the `first_on_demand` ones. Note: If `first_on_demand` is zero, this availability type will be used for the entire cluster. (ON_DEMAND_AZURE, SPOT_AZURE, SPOT_WITH_FALLBACK_AZURE)"
          },
          {
            "name": "first_on_demand",
            "type": "integer",
            "description": "The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
          },
          {
            "name": "log_analytics_info",
            "type": "object",
            "description": "Defines values necessary to configure and run Azure Log Analytics agent",
            "children": [
              {
                "name": "log_analytics_primary_key",
                "type": "string",
                "description": ""
              },
              {
                "name": "log_analytics_workspace_id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "spot_bid_max_price",
            "type": "number",
            "description": "The max bid price to be used for Azure spot instances. The Max price for the bid cannot be higher than the on-demand price of the instance. If not specified, the default value is -1, which specifies that the instance cannot be evicted on the basis of price, and only on the basis of availability. Further, the value should &gt; 0 or -1."
          }
        ]
      },
      {
        "name": "cluster_log_conf",
        "type": "object",
        "description": "The configuration for delivering spark logs to a long-term storage destination. Three kinds of destinations (DBFS, S3 and Unity Catalog volumes) are supported. Only one destination can be specified for one cluster. If the conf is given, the logs will be delivered to the destination every `5 mins`. The destination of driver logs is `$destination/$clusterId/driver`, while the destination of executor logs is `$destination/$clusterId/executor`.",
        "children": [
          {
            "name": "dbfs",
            "type": "object",
            "description": "destination needs to be provided. e.g. `&#123; \"dbfs\" : &#123; \"destination\" : \"dbfs:/home/cluster_log\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "dbfs destination, e.g. `dbfs:/my/path`"
              }
            ]
          },
          {
            "name": "s3",
            "type": "object",
            "description": "destination and either the region or endpoint need to be provided. e.g. `&#123; \"s3\": &#123; \"destination\" : \"s3://cluster_log_bucket/prefix\", \"region\" : \"us-west-2\" &#125; &#125;` Cluster iam role is used to access s3, please make sure the cluster iam role in `instance_profile_arn` has permission to write data to the s3 destination.",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "S3 destination, e.g. `s3://my-bucket/some-prefix` Note that logs will be delivered using cluster iam role, please make sure you set cluster iam role and the role has write access to the destination. Please also note that you cannot use AWS keys to deliver logs."
              },
              {
                "name": "canned_acl",
                "type": "string",
                "description": "(Optional) Set canned access control list for the logs, e.g. `bucket-owner-full-control`. If `canned_cal` is set, please make sure the cluster iam role has `s3:PutObjectAcl` permission on the destination bucket and prefix. The full list of possible canned acl can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl. Please also note that by default only the object owner gets full controls. If you are using cross account role for writing data, you may want to set `bucket-owner-full-control` to make bucket owner able to read the logs."
              },
              {
                "name": "enable_encryption",
                "type": "boolean",
                "description": "(Optional) Flag to enable server side encryption, `false` by default."
              },
              {
                "name": "encryption_type",
                "type": "string",
                "description": "(Optional) The encryption type, it could be `sse-s3` or `sse-kms`. It will be used only when encryption is enabled and the default type is `sse-s3`."
              },
              {
                "name": "endpoint",
                "type": "string",
                "description": "S3 endpoint, e.g. `https://s3-us-west-2.amazonaws.com`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
              },
              {
                "name": "kms_key",
                "type": "string",
                "description": "(Optional) Kms key which will be used if encryption is enabled and encryption type is set to `sse-kms`."
              },
              {
                "name": "region",
                "type": "string",
                "description": "S3 region, e.g. `us-west-2`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
              }
            ]
          },
          {
            "name": "volumes",
            "type": "object",
            "description": "destination needs to be provided, e.g. `&#123; \"volumes\": &#123; \"destination\": \"/Volumes/catalog/schema/volume/cluster_log\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "UC Volumes destination, e.g. `/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh` or `dbfs:/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh`"
              }
            ]
          }
        ]
      },
      {
        "name": "cluster_name",
        "type": "string",
        "description": "Cluster name requested by the user. This doesn't have to be unique. If not specified at creation, the cluster name will be an empty string. For job clusters, the cluster name is automatically set based on the job and job run IDs."
      },
      {
        "name": "custom_tags",
        "type": "object",
        "description": "Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS instances and EBS volumes) with these tags in addition to `default_tags`. Notes: - Currently, Databricks allows at most 45 custom tags - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags"
      },
      {
        "name": "data_security_mode",
        "type": "string",
        "description": "Data security mode decides what data governance model to use when accessing data from a cluster.<br /><br />The following modes can only be used when `kind = CLASSIC_PREVIEW`. * `DATA_SECURITY_MODE_AUTO`:<br />Databricks will choose the most appropriate access mode depending on your compute configuration.<br />* `DATA_SECURITY_MODE_STANDARD`: Alias for `USER_ISOLATION`. * `DATA_SECURITY_MODE_DEDICATED`:<br />Alias for `SINGLE_USER`.<br /><br />The following modes can be used regardless of `kind`. * `NONE`: No security isolation for<br />multiple users sharing the cluster. Data governance features are not available in this mode. *<br />`SINGLE_USER`: A secure cluster that can only be exclusively used by a single user specified in<br />`single_user_name`. Most programming languages, cluster features and data governance features<br />are available in this mode. * `USER_ISOLATION`: A secure cluster that can be shared by multiple<br />users. Cluster users are fully isolated so that they cannot see each other's data and<br />credentials. Most data governance features are supported in this mode. But programming languages<br />and cluster features might be limited.<br /><br />The following modes are deprecated starting with Databricks Runtime 15.0 and will be removed for<br />future Databricks Runtime versions:<br /><br />* `LEGACY_TABLE_ACL`: This mode is for users migrating from legacy Table ACL clusters. *<br />`LEGACY_PASSTHROUGH`: This mode is for users migrating from legacy Passthrough on high<br />concurrency clusters. * `LEGACY_SINGLE_USER`: This mode is for users migrating from legacy<br />Passthrough on standard clusters. * `LEGACY_SINGLE_USER_STANDARD`: This mode provides a way that<br />doesn’t have UC nor passthrough enabled. (DATA_SECURITY_MODE_AUTO, DATA_SECURITY_MODE_DEDICATED, DATA_SECURITY_MODE_STANDARD, LEGACY_PASSTHROUGH, LEGACY_SINGLE_USER, LEGACY_SINGLE_USER_STANDARD, LEGACY_TABLE_ACL, NONE, SINGLE_USER, USER_ISOLATION)"
      },
      {
        "name": "docker_image",
        "type": "object",
        "description": "Custom docker image BYOC",
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
        "name": "driver_instance_pool_id",
        "type": "string",
        "description": "The optional ID of the instance pool for the driver of the cluster belongs. The pool cluster uses the instance pool with id (instance_pool_id) if the driver pool is not assigned."
      },
      {
        "name": "driver_node_type_flexibility",
        "type": "object",
        "description": "Flexible node type configuration for the driver node.",
        "children": [
          {
            "name": "alternate_node_type_ids",
            "type": "array",
            "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
          }
        ]
      },
      {
        "name": "driver_node_type_id",
        "type": "string",
        "description": "The node type of the Spark driver. Note that this field is optional; if unset, the driver node type will be set as the same value as `node_type_id` defined above. This field, along with node_type_id, should not be set if virtual_cluster_size is set. If both driver_node_type_id, node_type_id, and virtual_cluster_size are specified, driver_node_type_id and node_type_id take precedence."
      },
      {
        "name": "enable_elastic_disk",
        "type": "boolean",
        "description": "Autoscaling Local Storage: when enabled, this cluster will dynamically acquire additional disk space when its Spark workers are running low on disk space."
      },
      {
        "name": "enable_local_disk_encryption",
        "type": "boolean",
        "description": "Whether to enable LUKS on cluster VMs' local disks"
      },
      {
        "name": "gcp_attributes",
        "type": "object",
        "description": "Attributes related to clusters running on Google Cloud Platform. If not specified at cluster creation, a set of default values will be used.",
        "children": [
          {
            "name": "availability",
            "type": "string",
            "description": "This field determines whether the spark executors will be scheduled to run on preemptible VMs, on-demand VMs, or preemptible VMs with a fallback to on-demand VMs if the former is unavailable. (ON_DEMAND_GCP, PREEMPTIBLE_GCP, PREEMPTIBLE_WITH_FALLBACK_GCP)"
          },
          {
            "name": "boot_disk_size",
            "type": "integer",
            "description": "Boot disk size in GB"
          },
          {
            "name": "first_on_demand",
            "type": "integer",
            "description": "The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
          },
          {
            "name": "google_service_account",
            "type": "string",
            "description": "If provided, the cluster will impersonate the google service account when accessing gcloud services (like GCS). The google service account must have previously been added to the Databricks environment by an account administrator."
          },
          {
            "name": "local_ssd_count",
            "type": "integer",
            "description": "If provided, each node (workers and driver) in the cluster will have this number of local SSDs attached. Each local SSD is 375GB in size. Refer to [GCP documentation] for the supported number of local SSDs for each instance type. [GCP documentation]: https://cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds"
          },
          {
            "name": "use_preemptible_executors",
            "type": "boolean",
            "description": "This field determines whether the spark executors will be scheduled to run on preemptible VMs (when set to true) versus standard compute engine VMs (when set to false; default). Note: Soon to be deprecated, use the 'availability' field instead."
          },
          {
            "name": "zone_id",
            "type": "string",
            "description": "Identifier for the availability zone in which the cluster resides. This can be one of the following: - \"HA\" =&gt; High availability, spread nodes across availability zones for a Databricks deployment region [default]. - \"AUTO\" =&gt; Databricks picks an availability zone to schedule the cluster on. - A GCP availability zone =&gt; Pick One of the available zones for (machine type + region) from https://cloud.google.com/compute/docs/regions-zones."
          }
        ]
      },
      {
        "name": "init_scripts",
        "type": "array",
        "description": "The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If `cluster_log_conf` is specified, init script logs are sent to `<destination>/<cluster-ID>/init_scripts`.",
        "children": [
          {
            "name": "abfss",
            "type": "object",
            "description": "destination needs to be provided, e.g. `abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<directory-name>`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "abfss destination, e.g. `abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<directory-name>`."
              }
            ]
          },
          {
            "name": "dbfs",
            "type": "object",
            "description": "destination needs to be provided. e.g. `&#123; \"dbfs\": &#123; \"destination\" : \"dbfs:/home/cluster_log\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "dbfs destination, e.g. `dbfs:/my/path`"
              }
            ]
          },
          {
            "name": "file",
            "type": "object",
            "description": "destination needs to be provided, e.g. `&#123; \"file\": &#123; \"destination\": \"file:/my/local/file.sh\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "gcs",
            "type": "object",
            "description": "destination needs to be provided, e.g. `&#123; \"gcs\": &#123; \"destination\": \"gs://my-bucket/file.sh\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "GCS destination/URI, e.g. `gs://my-bucket/some-prefix`"
              }
            ]
          },
          {
            "name": "s3",
            "type": "object",
            "description": "destination and either the region or endpoint need to be provided. e.g. `&#123; \\\"s3\\\": &#123; \\\"destination\\\": \\\"s3://cluster_log_bucket/prefix\\\", \\\"region\\\": \\\"us-west-2\\\" &#125; &#125;` Cluster iam role is used to access s3, please make sure the cluster iam role in `instance_profile_arn` has permission to write data to the s3 destination.",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "S3 destination, e.g. `s3://my-bucket/some-prefix` Note that logs will be delivered using cluster iam role, please make sure you set cluster iam role and the role has write access to the destination. Please also note that you cannot use AWS keys to deliver logs."
              },
              {
                "name": "canned_acl",
                "type": "string",
                "description": "(Optional) Set canned access control list for the logs, e.g. `bucket-owner-full-control`. If `canned_cal` is set, please make sure the cluster iam role has `s3:PutObjectAcl` permission on the destination bucket and prefix. The full list of possible canned acl can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl. Please also note that by default only the object owner gets full controls. If you are using cross account role for writing data, you may want to set `bucket-owner-full-control` to make bucket owner able to read the logs."
              },
              {
                "name": "enable_encryption",
                "type": "boolean",
                "description": "(Optional) Flag to enable server side encryption, `false` by default."
              },
              {
                "name": "encryption_type",
                "type": "string",
                "description": "(Optional) The encryption type, it could be `sse-s3` or `sse-kms`. It will be used only when encryption is enabled and the default type is `sse-s3`."
              },
              {
                "name": "endpoint",
                "type": "string",
                "description": "S3 endpoint, e.g. `https://s3-us-west-2.amazonaws.com`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
              },
              {
                "name": "kms_key",
                "type": "string",
                "description": "(Optional) Kms key which will be used if encryption is enabled and encryption type is set to `sse-kms`."
              },
              {
                "name": "region",
                "type": "string",
                "description": "S3 region, e.g. `us-west-2`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
              }
            ]
          },
          {
            "name": "volumes",
            "type": "object",
            "description": "destination needs to be provided. e.g. `&#123; \\\"volumes\\\" : &#123; \\\"destination\\\" : \\\"/Volumes/my-init.sh\\\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "UC Volumes destination, e.g. `/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh` or `dbfs:/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh`"
              }
            ]
          },
          {
            "name": "workspace",
            "type": "object",
            "description": "destination needs to be provided, e.g. `&#123; \"workspace\": &#123; \"destination\": \"/cluster-init-scripts/setup-datadog.sh\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "wsfs destination, e.g. `workspace:/cluster-init-scripts/setup-datadog.sh`"
              }
            ]
          }
        ]
      },
      {
        "name": "instance_pool_id",
        "type": "string",
        "description": "The optional ID of the instance pool to which the cluster belongs."
      },
      {
        "name": "is_single_node",
        "type": "boolean",
        "description": "This field can only be used when `kind = CLASSIC_PREVIEW`. When set to true, Databricks will automatically set single node related `custom_tags`, `spark_conf`, and `num_workers`"
      },
      {
        "name": "kind",
        "type": "string",
        "description": "The kind of compute described by this compute specification.<br /><br />Depending on `kind`, different validations and default values will be applied.<br /><br />Clusters with `kind = CLASSIC_PREVIEW` support the following fields, whereas clusters with no<br />specified `kind` do not. * [is_single_node](/api/workspace/clusters/create#is_single_node) *<br />[use_ml_runtime](/api/workspace/clusters/create#use_ml_runtime) *<br />[data_security_mode](/api/workspace/clusters/create#data_security_mode) set to<br />`DATA_SECURITY_MODE_AUTO`, `DATA_SECURITY_MODE_DEDICATED`, or `DATA_SECURITY_MODE_STANDARD`<br /><br />By using the [simple form], your clusters are automatically using `kind = CLASSIC_PREVIEW`.<br /><br />[simple form]: https://docs.databricks.com/compute/simple-form.html (CLASSIC_PREVIEW)"
      },
      {
        "name": "node_type_id",
        "type": "string",
        "description": "This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads. A list of available node types can be retrieved by using the :method:clusters/listNodeTypes API call."
      },
      {
        "name": "num_workers",
        "type": "integer",
        "description": "Number of worker nodes that this cluster should have. A cluster has one Spark Driver and `num_workers` Executors for a total of `num_workers` + 1 Spark nodes. Note: When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual current number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field will immediately be updated to reflect the target size of 10 workers, whereas the workers listed in `spark_info` will gradually increase from 5 to 10 as the new nodes are provisioned."
      },
      {
        "name": "policy_id",
        "type": "string",
        "description": "The ID of the cluster policy used to create the cluster if applicable."
      },
      {
        "name": "remote_disk_throughput",
        "type": "integer",
        "description": "If set, what the configurable throughput (in Mb/s) for the remote disk is. Currently only supported for GCP HYPERDISK_BALANCED disks."
      },
      {
        "name": "runtime_engine",
        "type": "string",
        "description": "Determines the cluster's runtime engine, either standard or Photon. This field is not compatible with legacy `spark_version` values that contain `-photon-`. Remove `-photon-` from the `spark_version` and set `runtime_engine` to `PHOTON`. If left unspecified, the runtime engine defaults to standard unless the spark_version contains -photon-, in which case Photon will be used. (NULL, PHOTON, STANDARD)"
      },
      {
        "name": "single_user_name",
        "type": "string",
        "description": "Single user name if data_security_mode is `SINGLE_USER`"
      },
      {
        "name": "spark_conf",
        "type": "object",
        "description": "An object containing a set of optional, user-specified Spark configuration key-value pairs. Users can also pass in a string of extra JVM options to the driver and the executors via `spark.driver.extraJavaOptions` and `spark.executor.extraJavaOptions` respectively."
      },
      {
        "name": "spark_env_vars",
        "type": "object",
        "description": "An object containing a set of optional, user-specified environment variable key-value pairs. Please note that key-value pair of the form (X,Y) will be exported as is (i.e., `export X='Y'`) while launching the driver and workers. In order to specify an additional set of `SPARK_DAEMON_JAVA_OPTS`, we recommend appending them to `$SPARK_DAEMON_JAVA_OPTS` as shown in the example below. This ensures that all default databricks managed environmental variables are included as well. Example Spark environment variables: `&#123;\"SPARK_WORKER_MEMORY\": \"28000m\", \"SPARK_LOCAL_DIRS\": \"/local_disk0\"&#125;` or `&#123;\"SPARK_DAEMON_JAVA_OPTS\": \"$SPARK_DAEMON_JAVA_OPTS -Dspark.shuffle.service.enabled=true\"&#125;`"
      },
      {
        "name": "spark_version",
        "type": "string",
        "description": "The Spark version of the cluster, e.g. `3.3.x-scala2.11`. A list of available Spark versions can be retrieved by using the :method:clusters/sparkVersions API call."
      },
      {
        "name": "ssh_public_keys",
        "type": "array",
        "description": "SSH public key contents that will be added to each Spark node in this cluster. The corresponding private keys can be used to login with the user name `ubuntu` on port `2200`. Up to 10 keys can be specified."
      },
      {
        "name": "total_initial_remote_disk_size",
        "type": "integer",
        "description": "If set, what the total initial volume size (in GB) of the remote disks should be. Currently only supported for GCP HYPERDISK_BALANCED disks."
      },
      {
        "name": "use_ml_runtime",
        "type": "boolean",
        "description": "This field can only be used when `kind = CLASSIC_PREVIEW`. `effective_spark_version` is determined by `spark_version` (DBR release), this field `use_ml_runtime`, and whether `node_type_id` is gpu node or not."
      },
      {
        "name": "worker_node_type_flexibility",
        "type": "object",
        "description": "Flexible node type configuration for worker nodes.",
        "children": [
          {
            "name": "alternate_node_type_ids",
            "type": "array",
            "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
          }
        ]
      },
      {
        "name": "workload_type",
        "type": "object",
        "description": "Cluster Attributes showing for clusters workload types.",
        "children": [
          {
            "name": "clients",
            "type": "object",
            "description": "defined what type of clients can use the cluster. E.g. Notebooks, Jobs",
            "children": [
              {
                "name": "jobs",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "notebooks",
                "type": "boolean",
                "description": "With notebooks set, this cluster can be used for notebooks"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "ssh_public_keys",
    "type": "array",
    "description": "SSH public key contents that will be added to each Spark node in this cluster. The corresponding private keys can be used to login with the user name `ubuntu` on port `2200`. Up to 10 keys can be specified."
  },
  {
    "name": "start_time",
    "type": "integer",
    "description": "Time (in epoch milliseconds) when the cluster creation request was received (when the cluster entered a `PENDING` state)."
  },
  {
    "name": "state",
    "type": "string",
    "description": "Current state of the cluster. (ERROR, PENDING, RESIZING, RESTARTING, RUNNING, TERMINATED, TERMINATING, UNKNOWN)"
  },
  {
    "name": "state_message",
    "type": "string",
    "description": "A message associated with the most recent state transition (e.g., the reason why the cluster entered a `TERMINATED` state)."
  },
  {
    "name": "terminated_time",
    "type": "integer",
    "description": "Time (in epoch milliseconds) when the cluster was terminated, if applicable."
  },
  {
    "name": "termination_reason",
    "type": "object",
    "description": "Information about why the cluster was terminated. This field only appears when the cluster is in a `TERMINATING` or `TERMINATED` state.",
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
    "name": "total_initial_remote_disk_size",
    "type": "integer",
    "description": "If set, what the total initial volume size (in GB) of the remote disks should be. Currently only supported for GCP HYPERDISK_BALANCED disks."
  },
  {
    "name": "use_ml_runtime",
    "type": "boolean",
    "description": "This field can only be used when `kind = CLASSIC_PREVIEW`. `effective_spark_version` is determined by `spark_version` (DBR release), this field `use_ml_runtime`, and whether `node_type_id` is gpu node or not."
  },
  {
    "name": "worker_node_type_flexibility",
    "type": "object",
    "description": "Flexible node type configuration for worker nodes.",
    "children": [
      {
        "name": "alternate_node_type_ids",
        "type": "array",
        "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
      }
    ]
  },
  {
    "name": "workload_type",
    "type": "object",
    "description": "Cluster Attributes showing for clusters workload types.",
    "children": [
      {
        "name": "clients",
        "type": "object",
        "description": "defined what type of clients can use the cluster. E.g. Notebooks, Jobs",
        "children": [
          {
            "name": "jobs",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "notebooks",
            "type": "boolean",
            "description": "With notebooks set, this cluster can be used for notebooks"
          }
        ]
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "cluster_id",
    "type": "string",
    "description": "Canonical identifier for the cluster. This id is retained during cluster restarts and resizes, while each new cluster has a globally unique id."
  },
  {
    "name": "driver_instance_pool_id",
    "type": "string",
    "description": "The optional ID of the instance pool for the driver of the cluster belongs. The pool cluster uses the instance pool with id (instance_pool_id) if the driver pool is not assigned."
  },
  {
    "name": "driver_node_type_id",
    "type": "string",
    "description": "The node type of the Spark driver. Note that this field is optional; if unset, the driver node type will be set as the same value as `node_type_id` defined above. This field, along with node_type_id, should not be set if virtual_cluster_size is set. If both driver_node_type_id, node_type_id, and virtual_cluster_size are specified, driver_node_type_id and node_type_id take precedence."
  },
  {
    "name": "instance_pool_id",
    "type": "string",
    "description": "The optional ID of the instance pool to which the cluster belongs."
  },
  {
    "name": "node_type_id",
    "type": "string",
    "description": "This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads. A list of available node types can be retrieved by using the :method:clusters/listNodeTypes API call."
  },
  {
    "name": "policy_id",
    "type": "string",
    "description": "The ID of the cluster policy used to create the cluster if applicable."
  },
  {
    "name": "spark_context_id",
    "type": "integer",
    "description": "A canonical SparkContext identifier. This value *does* change when the Spark driver restarts. The pair `(cluster_id, spark_context_id)` is a globally unique identifier over all Spark contexts."
  },
  {
    "name": "cluster_name",
    "type": "string",
    "description": "Cluster name requested by the user. This doesn't have to be unique. If not specified at creation, the cluster name will be an empty string. For job clusters, the cluster name is automatically set based on the job and job run IDs."
  },
  {
    "name": "creator_user_name",
    "type": "string",
    "description": "Creator user name. The field won't be included in the response if the user has already been deleted."
  },
  {
    "name": "single_user_name",
    "type": "string",
    "description": "Single user name if data_security_mode is `SINGLE_USER`"
  },
  {
    "name": "autoscale",
    "type": "object",
    "description": "Parameters needed in order to automatically scale clusters up and down based on load. Note: autoscaling works best with DB runtime versions 3.0 or later.",
    "children": [
      {
        "name": "max_workers",
        "type": "integer",
        "description": ""
      },
      {
        "name": "min_workers",
        "type": "integer",
        "description": "The minimum number of workers to which the cluster can scale down when underutilized. It is also the initial number of workers the cluster will have after creation."
      }
    ]
  },
  {
    "name": "autotermination_minutes",
    "type": "integer",
    "description": "Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this cluster will not be automatically terminated. If specified, the threshold must be between 10 and 10000 minutes. Users can also set this value to 0 to explicitly disable automatic termination."
  },
  {
    "name": "aws_attributes",
    "type": "object",
    "description": "Attributes related to clusters running on Amazon Web Services. If not specified at cluster creation, a set of default values will be used.",
    "children": [
      {
        "name": "availability",
        "type": "string",
        "description": "Availability type used for all subsequent nodes past the `first_on_demand` ones.<br /><br />Note: If `first_on_demand` is zero, this availability type will be used for the entire cluster. (ON_DEMAND, SPOT, SPOT_WITH_FALLBACK)"
      },
      {
        "name": "ebs_volume_count",
        "type": "integer",
        "description": "The number of volumes launched for each instance. Users can choose up to 10 volumes. This feature is only enabled for supported node types. Legacy node types cannot specify custom EBS volumes. For node types with no instance store, at least one EBS volume needs to be specified; otherwise, cluster creation will fail. These EBS volumes will be mounted at `/ebs0`, `/ebs1`, and etc. Instance store volumes will be mounted at `/local_disk0`, `/local_disk1`, and etc. If EBS volumes are attached, Databricks will configure Spark to use only the EBS volumes for scratch storage because heterogenously sized scratch devices can lead to inefficient disk utilization. If no EBS volumes are attached, Databricks will configure Spark to use instance store volumes. Please note that if EBS volumes are specified, then the Spark configuration `spark.local.dir` will be overridden."
      },
      {
        "name": "ebs_volume_iops",
        "type": "integer",
        "description": "If using gp3 volumes, what IOPS to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used."
      },
      {
        "name": "ebs_volume_size",
        "type": "integer",
        "description": "The size of each EBS volume (in GiB) launched for each instance. For general purpose SSD, this value must be within the range 100 - 4096. For throughput optimized HDD, this value must be within the range 500 - 4096."
      },
      {
        "name": "ebs_volume_throughput",
        "type": "integer",
        "description": "If using gp3 volumes, what throughput to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used."
      },
      {
        "name": "ebs_volume_type",
        "type": "string",
        "description": "The type of EBS volumes that will be launched with this cluster. (GENERAL_PURPOSE_SSD, THROUGHPUT_OPTIMIZED_HDD)"
      },
      {
        "name": "first_on_demand",
        "type": "integer",
        "description": "The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. If this value is greater than 0, the cluster driver node in particular will be placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
      },
      {
        "name": "instance_profile_arn",
        "type": "string",
        "description": "Nodes for this cluster will only be placed on AWS instances with this instance profile. If ommitted, nodes will be placed on instances without an IAM instance profile. The instance profile must have previously been added to the Databricks environment by an account administrator. This feature may only be available to certain customer plans."
      },
      {
        "name": "spot_bid_price_percent",
        "type": "integer",
        "description": "The bid price for AWS spot instances, as a percentage of the corresponding instance type's on-demand price. For example, if this field is set to 50, and the cluster needs a new `r3.xlarge` spot instance, then the bid price is half of the price of on-demand `r3.xlarge` instances. Similarly, if this field is set to 200, the bid price is twice the price of on-demand `r3.xlarge` instances. If not specified, the default value is 100. When spot instances are requested for this cluster, only spot instances whose bid price percentage matches this field will be considered. Note that, for safety, we enforce this field to be no more than 10000."
      },
      {
        "name": "zone_id",
        "type": "string",
        "description": "Identifier for the availability zone/datacenter in which the cluster resides. This string will be of a form like \"us-west-2a\". The provided availability zone must be in the same region as the Databricks deployment. For example, \"us-west-2a\" is not a valid zone id if the Databricks deployment resides in the \"us-east-1\" region. This is an optional field at cluster creation, and if not specified, the zone \"auto\" will be used. If the zone specified is \"auto\", will try to place cluster in a zone with high availability, and will retry placement in a different AZ if there is not enough capacity. The list of available zones as well as the default value can be found by using the `List Zones` method."
      }
    ]
  },
  {
    "name": "azure_attributes",
    "type": "object",
    "description": "Attributes related to clusters running on Microsoft Azure. If not specified at cluster creation, a set of default values will be used.",
    "children": [
      {
        "name": "availability",
        "type": "string",
        "description": "Availability type used for all subsequent nodes past the `first_on_demand` ones. Note: If `first_on_demand` is zero, this availability type will be used for the entire cluster. (ON_DEMAND_AZURE, SPOT_AZURE, SPOT_WITH_FALLBACK_AZURE)"
      },
      {
        "name": "first_on_demand",
        "type": "integer",
        "description": "The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
      },
      {
        "name": "log_analytics_info",
        "type": "object",
        "description": "Defines values necessary to configure and run Azure Log Analytics agent",
        "children": [
          {
            "name": "log_analytics_primary_key",
            "type": "string",
            "description": ""
          },
          {
            "name": "log_analytics_workspace_id",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "spot_bid_max_price",
        "type": "number",
        "description": "The max bid price to be used for Azure spot instances. The Max price for the bid cannot be higher than the on-demand price of the instance. If not specified, the default value is -1, which specifies that the instance cannot be evicted on the basis of price, and only on the basis of availability. Further, the value should &gt; 0 or -1."
      }
    ]
  },
  {
    "name": "cluster_cores",
    "type": "number",
    "description": "Number of CPU cores available for this cluster. Note that this can be fractional, e.g. 7.5 cores, since certain node types are configured to share cores between Spark nodes on the same instance."
  },
  {
    "name": "cluster_log_conf",
    "type": "object",
    "description": "The configuration for delivering spark logs to a long-term storage destination. Three kinds of destinations (DBFS, S3 and Unity Catalog volumes) are supported. Only one destination can be specified for one cluster. If the conf is given, the logs will be delivered to the destination every `5 mins`. The destination of driver logs is `$destination/$clusterId/driver`, while the destination of executor logs is `$destination/$clusterId/executor`.",
    "children": [
      {
        "name": "dbfs",
        "type": "object",
        "description": "destination needs to be provided. e.g. `&#123; \"dbfs\" : &#123; \"destination\" : \"dbfs:/home/cluster_log\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "dbfs destination, e.g. `dbfs:/my/path`"
          }
        ]
      },
      {
        "name": "s3",
        "type": "object",
        "description": "destination and either the region or endpoint need to be provided. e.g. `&#123; \"s3\": &#123; \"destination\" : \"s3://cluster_log_bucket/prefix\", \"region\" : \"us-west-2\" &#125; &#125;` Cluster iam role is used to access s3, please make sure the cluster iam role in `instance_profile_arn` has permission to write data to the s3 destination.",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "S3 destination, e.g. `s3://my-bucket/some-prefix` Note that logs will be delivered using cluster iam role, please make sure you set cluster iam role and the role has write access to the destination. Please also note that you cannot use AWS keys to deliver logs."
          },
          {
            "name": "canned_acl",
            "type": "string",
            "description": "(Optional) Set canned access control list for the logs, e.g. `bucket-owner-full-control`. If `canned_cal` is set, please make sure the cluster iam role has `s3:PutObjectAcl` permission on the destination bucket and prefix. The full list of possible canned acl can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl. Please also note that by default only the object owner gets full controls. If you are using cross account role for writing data, you may want to set `bucket-owner-full-control` to make bucket owner able to read the logs."
          },
          {
            "name": "enable_encryption",
            "type": "boolean",
            "description": "(Optional) Flag to enable server side encryption, `false` by default."
          },
          {
            "name": "encryption_type",
            "type": "string",
            "description": "(Optional) The encryption type, it could be `sse-s3` or `sse-kms`. It will be used only when encryption is enabled and the default type is `sse-s3`."
          },
          {
            "name": "endpoint",
            "type": "string",
            "description": "S3 endpoint, e.g. `https://s3-us-west-2.amazonaws.com`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
          },
          {
            "name": "kms_key",
            "type": "string",
            "description": "(Optional) Kms key which will be used if encryption is enabled and encryption type is set to `sse-kms`."
          },
          {
            "name": "region",
            "type": "string",
            "description": "S3 region, e.g. `us-west-2`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
          }
        ]
      },
      {
        "name": "volumes",
        "type": "object",
        "description": "destination needs to be provided, e.g. `&#123; \"volumes\": &#123; \"destination\": \"/Volumes/catalog/schema/volume/cluster_log\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "UC Volumes destination, e.g. `/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh` or `dbfs:/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh`"
          }
        ]
      }
    ]
  },
  {
    "name": "cluster_log_status",
    "type": "object",
    "description": "Cluster log delivery status.",
    "children": [
      {
        "name": "last_attempted",
        "type": "integer",
        "description": "The timestamp of last attempt. If the last attempt fails, `last_exception` will contain the exception in the last attempt."
      },
      {
        "name": "last_exception",
        "type": "string",
        "description": "The exception thrown in the last attempt, it would be null (omitted in the response) if there is no exception in last attempted."
      }
    ]
  },
  {
    "name": "cluster_memory_mb",
    "type": "integer",
    "description": "Total amount of cluster memory, in megabytes"
  },
  {
    "name": "cluster_source",
    "type": "string",
    "description": "Determines whether the cluster was created by a user through the UI, created by the Databricks Jobs Scheduler, or through an API request. (API, JOB, MODELS, PIPELINE, PIPELINE_MAINTENANCE, SQL, UI)"
  },
  {
    "name": "custom_tags",
    "type": "object",
    "description": "Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS instances and EBS volumes) with these tags in addition to `default_tags`. Notes: - Currently, Databricks allows at most 45 custom tags - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags"
  },
  {
    "name": "data_security_mode",
    "type": "string",
    "description": "Data security mode decides what data governance model to use when accessing data from a cluster.<br /><br />The following modes can only be used when `kind = CLASSIC_PREVIEW`. * `DATA_SECURITY_MODE_AUTO`:<br />Databricks will choose the most appropriate access mode depending on your compute configuration.<br />* `DATA_SECURITY_MODE_STANDARD`: Alias for `USER_ISOLATION`. * `DATA_SECURITY_MODE_DEDICATED`:<br />Alias for `SINGLE_USER`.<br /><br />The following modes can be used regardless of `kind`. * `NONE`: No security isolation for<br />multiple users sharing the cluster. Data governance features are not available in this mode. *<br />`SINGLE_USER`: A secure cluster that can only be exclusively used by a single user specified in<br />`single_user_name`. Most programming languages, cluster features and data governance features<br />are available in this mode. * `USER_ISOLATION`: A secure cluster that can be shared by multiple<br />users. Cluster users are fully isolated so that they cannot see each other's data and<br />credentials. Most data governance features are supported in this mode. But programming languages<br />and cluster features might be limited.<br /><br />The following modes are deprecated starting with Databricks Runtime 15.0 and will be removed for<br />future Databricks Runtime versions:<br /><br />* `LEGACY_TABLE_ACL`: This mode is for users migrating from legacy Table ACL clusters. *<br />`LEGACY_PASSTHROUGH`: This mode is for users migrating from legacy Passthrough on high<br />concurrency clusters. * `LEGACY_SINGLE_USER`: This mode is for users migrating from legacy<br />Passthrough on standard clusters. * `LEGACY_SINGLE_USER_STANDARD`: This mode provides a way that<br />doesn’t have UC nor passthrough enabled. (DATA_SECURITY_MODE_AUTO, DATA_SECURITY_MODE_DEDICATED, DATA_SECURITY_MODE_STANDARD, LEGACY_PASSTHROUGH, LEGACY_SINGLE_USER, LEGACY_SINGLE_USER_STANDARD, LEGACY_TABLE_ACL, NONE, SINGLE_USER, USER_ISOLATION)"
  },
  {
    "name": "default_tags",
    "type": "object",
    "description": "Tags that are added by Databricks regardless of any `custom_tags`, including: - Vendor: Databricks - Creator: &lt;username_of_creator&gt; - ClusterName: &lt;name_of_cluster&gt; - ClusterId: &lt;id_of_cluster&gt; - Name: &lt;Databricks internal use&gt;"
  },
  {
    "name": "docker_image",
    "type": "object",
    "description": "Custom docker image BYOC",
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
    "name": "driver",
    "type": "object",
    "description": "Node on which the Spark driver resides. The driver node contains the Spark master and the Databricks application that manages the per-notebook Spark REPLs.",
    "children": [
      {
        "name": "host_private_ip",
        "type": "string",
        "description": "The private IP address of the host instance."
      },
      {
        "name": "instance_id",
        "type": "string",
        "description": "Globally unique identifier for the host instance from the cloud provider."
      },
      {
        "name": "node_aws_attributes",
        "type": "object",
        "description": "Attributes specific to AWS for a Spark node.",
        "children": [
          {
            "name": "is_spot",
            "type": "boolean",
            "description": "Whether this node is on an Amazon spot instance."
          }
        ]
      },
      {
        "name": "node_id",
        "type": "string",
        "description": "Globally unique identifier for this node."
      },
      {
        "name": "private_ip",
        "type": "string",
        "description": "Private IP address (typically a 10.x.x.x address) of the Spark node. Note that this is different from the private IP address of the host instance."
      },
      {
        "name": "public_dns",
        "type": "string",
        "description": "Public DNS address of this node. This address can be used to access the Spark JDBC server on the driver node. To communicate with the JDBC server, traffic must be manually authorized by adding security group rules to the \"worker-unmanaged\" security group via the AWS console."
      },
      {
        "name": "start_timestamp",
        "type": "integer",
        "description": "The timestamp (in millisecond) when the Spark node is launched."
      }
    ]
  },
  {
    "name": "driver_node_type_flexibility",
    "type": "object",
    "description": "Flexible node type configuration for the driver node.",
    "children": [
      {
        "name": "alternate_node_type_ids",
        "type": "array",
        "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
      }
    ]
  },
  {
    "name": "enable_elastic_disk",
    "type": "boolean",
    "description": "Autoscaling Local Storage: when enabled, this cluster will dynamically acquire additional disk space when its Spark workers are running low on disk space."
  },
  {
    "name": "enable_local_disk_encryption",
    "type": "boolean",
    "description": "Whether to enable LUKS on cluster VMs' local disks"
  },
  {
    "name": "executors",
    "type": "array",
    "description": "Nodes on which the Spark executors reside.",
    "children": [
      {
        "name": "host_private_ip",
        "type": "string",
        "description": "The private IP address of the host instance."
      },
      {
        "name": "instance_id",
        "type": "string",
        "description": "Globally unique identifier for the host instance from the cloud provider."
      },
      {
        "name": "node_aws_attributes",
        "type": "object",
        "description": "Attributes specific to AWS for a Spark node.",
        "children": [
          {
            "name": "is_spot",
            "type": "boolean",
            "description": "Whether this node is on an Amazon spot instance."
          }
        ]
      },
      {
        "name": "node_id",
        "type": "string",
        "description": "Globally unique identifier for this node."
      },
      {
        "name": "private_ip",
        "type": "string",
        "description": "Private IP address (typically a 10.x.x.x address) of the Spark node. Note that this is different from the private IP address of the host instance."
      },
      {
        "name": "public_dns",
        "type": "string",
        "description": "Public DNS address of this node. This address can be used to access the Spark JDBC server on the driver node. To communicate with the JDBC server, traffic must be manually authorized by adding security group rules to the \"worker-unmanaged\" security group via the AWS console."
      },
      {
        "name": "start_timestamp",
        "type": "integer",
        "description": "The timestamp (in millisecond) when the Spark node is launched."
      }
    ]
  },
  {
    "name": "gcp_attributes",
    "type": "object",
    "description": "Attributes related to clusters running on Google Cloud Platform. If not specified at cluster creation, a set of default values will be used.",
    "children": [
      {
        "name": "availability",
        "type": "string",
        "description": "This field determines whether the spark executors will be scheduled to run on preemptible VMs, on-demand VMs, or preemptible VMs with a fallback to on-demand VMs if the former is unavailable. (ON_DEMAND_GCP, PREEMPTIBLE_GCP, PREEMPTIBLE_WITH_FALLBACK_GCP)"
      },
      {
        "name": "boot_disk_size",
        "type": "integer",
        "description": "Boot disk size in GB"
      },
      {
        "name": "first_on_demand",
        "type": "integer",
        "description": "The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
      },
      {
        "name": "google_service_account",
        "type": "string",
        "description": "If provided, the cluster will impersonate the google service account when accessing gcloud services (like GCS). The google service account must have previously been added to the Databricks environment by an account administrator."
      },
      {
        "name": "local_ssd_count",
        "type": "integer",
        "description": "If provided, each node (workers and driver) in the cluster will have this number of local SSDs attached. Each local SSD is 375GB in size. Refer to [GCP documentation] for the supported number of local SSDs for each instance type. [GCP documentation]: https://cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds"
      },
      {
        "name": "use_preemptible_executors",
        "type": "boolean",
        "description": "This field determines whether the spark executors will be scheduled to run on preemptible VMs (when set to true) versus standard compute engine VMs (when set to false; default). Note: Soon to be deprecated, use the 'availability' field instead."
      },
      {
        "name": "zone_id",
        "type": "string",
        "description": "Identifier for the availability zone in which the cluster resides. This can be one of the following: - \"HA\" =&gt; High availability, spread nodes across availability zones for a Databricks deployment region [default]. - \"AUTO\" =&gt; Databricks picks an availability zone to schedule the cluster on. - A GCP availability zone =&gt; Pick One of the available zones for (machine type + region) from https://cloud.google.com/compute/docs/regions-zones."
      }
    ]
  },
  {
    "name": "init_scripts",
    "type": "array",
    "description": "The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If `cluster_log_conf` is specified, init script logs are sent to `<destination>/<cluster-ID>/init_scripts`.",
    "children": [
      {
        "name": "abfss",
        "type": "object",
        "description": "destination needs to be provided, e.g. `abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<directory-name>`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "abfss destination, e.g. `abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<directory-name>`."
          }
        ]
      },
      {
        "name": "dbfs",
        "type": "object",
        "description": "destination needs to be provided. e.g. `&#123; \"dbfs\": &#123; \"destination\" : \"dbfs:/home/cluster_log\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "dbfs destination, e.g. `dbfs:/my/path`"
          }
        ]
      },
      {
        "name": "file",
        "type": "object",
        "description": "destination needs to be provided, e.g. `&#123; \"file\": &#123; \"destination\": \"file:/my/local/file.sh\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "gcs",
        "type": "object",
        "description": "destination needs to be provided, e.g. `&#123; \"gcs\": &#123; \"destination\": \"gs://my-bucket/file.sh\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "GCS destination/URI, e.g. `gs://my-bucket/some-prefix`"
          }
        ]
      },
      {
        "name": "s3",
        "type": "object",
        "description": "destination and either the region or endpoint need to be provided. e.g. `&#123; \\\"s3\\\": &#123; \\\"destination\\\": \\\"s3://cluster_log_bucket/prefix\\\", \\\"region\\\": \\\"us-west-2\\\" &#125; &#125;` Cluster iam role is used to access s3, please make sure the cluster iam role in `instance_profile_arn` has permission to write data to the s3 destination.",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "S3 destination, e.g. `s3://my-bucket/some-prefix` Note that logs will be delivered using cluster iam role, please make sure you set cluster iam role and the role has write access to the destination. Please also note that you cannot use AWS keys to deliver logs."
          },
          {
            "name": "canned_acl",
            "type": "string",
            "description": "(Optional) Set canned access control list for the logs, e.g. `bucket-owner-full-control`. If `canned_cal` is set, please make sure the cluster iam role has `s3:PutObjectAcl` permission on the destination bucket and prefix. The full list of possible canned acl can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl. Please also note that by default only the object owner gets full controls. If you are using cross account role for writing data, you may want to set `bucket-owner-full-control` to make bucket owner able to read the logs."
          },
          {
            "name": "enable_encryption",
            "type": "boolean",
            "description": "(Optional) Flag to enable server side encryption, `false` by default."
          },
          {
            "name": "encryption_type",
            "type": "string",
            "description": "(Optional) The encryption type, it could be `sse-s3` or `sse-kms`. It will be used only when encryption is enabled and the default type is `sse-s3`."
          },
          {
            "name": "endpoint",
            "type": "string",
            "description": "S3 endpoint, e.g. `https://s3-us-west-2.amazonaws.com`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
          },
          {
            "name": "kms_key",
            "type": "string",
            "description": "(Optional) Kms key which will be used if encryption is enabled and encryption type is set to `sse-kms`."
          },
          {
            "name": "region",
            "type": "string",
            "description": "S3 region, e.g. `us-west-2`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
          }
        ]
      },
      {
        "name": "volumes",
        "type": "object",
        "description": "destination needs to be provided. e.g. `&#123; \\\"volumes\\\" : &#123; \\\"destination\\\" : \\\"/Volumes/my-init.sh\\\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "UC Volumes destination, e.g. `/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh` or `dbfs:/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh`"
          }
        ]
      },
      {
        "name": "workspace",
        "type": "object",
        "description": "destination needs to be provided, e.g. `&#123; \"workspace\": &#123; \"destination\": \"/cluster-init-scripts/setup-datadog.sh\" &#125; &#125;`",
        "children": [
          {
            "name": "destination",
            "type": "string",
            "description": "wsfs destination, e.g. `workspace:/cluster-init-scripts/setup-datadog.sh`"
          }
        ]
      }
    ]
  },
  {
    "name": "is_single_node",
    "type": "boolean",
    "description": "This field can only be used when `kind = CLASSIC_PREVIEW`. When set to true, Databricks will automatically set single node related `custom_tags`, `spark_conf`, and `num_workers`"
  },
  {
    "name": "jdbc_port",
    "type": "integer",
    "description": "Port on which Spark JDBC server is listening, in the driver nod. No service will be listeningon on this port in executor nodes."
  },
  {
    "name": "kind",
    "type": "string",
    "description": "The kind of compute described by this compute specification.<br /><br />Depending on `kind`, different validations and default values will be applied.<br /><br />Clusters with `kind = CLASSIC_PREVIEW` support the following fields, whereas clusters with no<br />specified `kind` do not. * [is_single_node](/api/workspace/clusters/create#is_single_node) *<br />[use_ml_runtime](/api/workspace/clusters/create#use_ml_runtime) *<br />[data_security_mode](/api/workspace/clusters/create#data_security_mode) set to<br />`DATA_SECURITY_MODE_AUTO`, `DATA_SECURITY_MODE_DEDICATED`, or `DATA_SECURITY_MODE_STANDARD`<br /><br />By using the [simple form], your clusters are automatically using `kind = CLASSIC_PREVIEW`.<br /><br />[simple form]: https://docs.databricks.com/compute/simple-form.html (CLASSIC_PREVIEW)"
  },
  {
    "name": "last_restarted_time",
    "type": "integer",
    "description": "the timestamp that the cluster was started/restarted"
  },
  {
    "name": "last_state_loss_time",
    "type": "integer",
    "description": "Time when the cluster driver last lost its state (due to a restart or driver failure)."
  },
  {
    "name": "num_workers",
    "type": "integer",
    "description": "Number of worker nodes that this cluster should have. A cluster has one Spark Driver and `num_workers` Executors for a total of `num_workers` + 1 Spark nodes. Note: When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual current number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field will immediately be updated to reflect the target size of 10 workers, whereas the workers listed in `spark_info` will gradually increase from 5 to 10 as the new nodes are provisioned."
  },
  {
    "name": "remote_disk_throughput",
    "type": "integer",
    "description": "If set, what the configurable throughput (in Mb/s) for the remote disk is. Currently only supported for GCP HYPERDISK_BALANCED disks."
  },
  {
    "name": "runtime_engine",
    "type": "string",
    "description": "Determines the cluster's runtime engine, either standard or Photon. This field is not compatible with legacy `spark_version` values that contain `-photon-`. Remove `-photon-` from the `spark_version` and set `runtime_engine` to `PHOTON`. If left unspecified, the runtime engine defaults to standard unless the spark_version contains -photon-, in which case Photon will be used. (NULL, PHOTON, STANDARD)"
  },
  {
    "name": "spark_conf",
    "type": "object",
    "description": "An object containing a set of optional, user-specified Spark configuration key-value pairs. Users can also pass in a string of extra JVM options to the driver and the executors via `spark.driver.extraJavaOptions` and `spark.executor.extraJavaOptions` respectively."
  },
  {
    "name": "spark_env_vars",
    "type": "object",
    "description": "An object containing a set of optional, user-specified environment variable key-value pairs. Please note that key-value pair of the form (X,Y) will be exported as is (i.e., `export X='Y'`) while launching the driver and workers. In order to specify an additional set of `SPARK_DAEMON_JAVA_OPTS`, we recommend appending them to `$SPARK_DAEMON_JAVA_OPTS` as shown in the example below. This ensures that all default databricks managed environmental variables are included as well. Example Spark environment variables: `&#123;\"SPARK_WORKER_MEMORY\": \"28000m\", \"SPARK_LOCAL_DIRS\": \"/local_disk0\"&#125;` or `&#123;\"SPARK_DAEMON_JAVA_OPTS\": \"$SPARK_DAEMON_JAVA_OPTS -Dspark.shuffle.service.enabled=true\"&#125;`"
  },
  {
    "name": "spark_version",
    "type": "string",
    "description": "The Spark version of the cluster, e.g. `3.3.x-scala2.11`. A list of available Spark versions can be retrieved by using the :method:clusters/sparkVersions API call."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains a snapshot of the latest user specified settings that were used to create/edit the cluster. Note: not included in the response of the ListClusters API.",
    "children": [
      {
        "name": "apply_policy_default_values",
        "type": "boolean",
        "description": "When set to true, fixed and default values from the policy will be used for fields that are omitted. When set to false, only fixed values from the policy will be applied."
      },
      {
        "name": "autoscale",
        "type": "object",
        "description": "Parameters needed in order to automatically scale clusters up and down based on load. Note: autoscaling works best with DB runtime versions 3.0 or later.",
        "children": [
          {
            "name": "max_workers",
            "type": "integer",
            "description": ""
          },
          {
            "name": "min_workers",
            "type": "integer",
            "description": "The minimum number of workers to which the cluster can scale down when underutilized. It is also the initial number of workers the cluster will have after creation."
          }
        ]
      },
      {
        "name": "autotermination_minutes",
        "type": "integer",
        "description": "Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this cluster will not be automatically terminated. If specified, the threshold must be between 10 and 10000 minutes. Users can also set this value to 0 to explicitly disable automatic termination."
      },
      {
        "name": "aws_attributes",
        "type": "object",
        "description": "Attributes related to clusters running on Amazon Web Services. If not specified at cluster creation, a set of default values will be used.",
        "children": [
          {
            "name": "availability",
            "type": "string",
            "description": "Availability type used for all subsequent nodes past the `first_on_demand` ones.<br /><br />Note: If `first_on_demand` is zero, this availability type will be used for the entire cluster. (ON_DEMAND, SPOT, SPOT_WITH_FALLBACK)"
          },
          {
            "name": "ebs_volume_count",
            "type": "integer",
            "description": "The number of volumes launched for each instance. Users can choose up to 10 volumes. This feature is only enabled for supported node types. Legacy node types cannot specify custom EBS volumes. For node types with no instance store, at least one EBS volume needs to be specified; otherwise, cluster creation will fail. These EBS volumes will be mounted at `/ebs0`, `/ebs1`, and etc. Instance store volumes will be mounted at `/local_disk0`, `/local_disk1`, and etc. If EBS volumes are attached, Databricks will configure Spark to use only the EBS volumes for scratch storage because heterogenously sized scratch devices can lead to inefficient disk utilization. If no EBS volumes are attached, Databricks will configure Spark to use instance store volumes. Please note that if EBS volumes are specified, then the Spark configuration `spark.local.dir` will be overridden."
          },
          {
            "name": "ebs_volume_iops",
            "type": "integer",
            "description": "If using gp3 volumes, what IOPS to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used."
          },
          {
            "name": "ebs_volume_size",
            "type": "integer",
            "description": "The size of each EBS volume (in GiB) launched for each instance. For general purpose SSD, this value must be within the range 100 - 4096. For throughput optimized HDD, this value must be within the range 500 - 4096."
          },
          {
            "name": "ebs_volume_throughput",
            "type": "integer",
            "description": "If using gp3 volumes, what throughput to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used."
          },
          {
            "name": "ebs_volume_type",
            "type": "string",
            "description": "The type of EBS volumes that will be launched with this cluster. (GENERAL_PURPOSE_SSD, THROUGHPUT_OPTIMIZED_HDD)"
          },
          {
            "name": "first_on_demand",
            "type": "integer",
            "description": "The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. If this value is greater than 0, the cluster driver node in particular will be placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
          },
          {
            "name": "instance_profile_arn",
            "type": "string",
            "description": "Nodes for this cluster will only be placed on AWS instances with this instance profile. If ommitted, nodes will be placed on instances without an IAM instance profile. The instance profile must have previously been added to the Databricks environment by an account administrator. This feature may only be available to certain customer plans."
          },
          {
            "name": "spot_bid_price_percent",
            "type": "integer",
            "description": "The bid price for AWS spot instances, as a percentage of the corresponding instance type's on-demand price. For example, if this field is set to 50, and the cluster needs a new `r3.xlarge` spot instance, then the bid price is half of the price of on-demand `r3.xlarge` instances. Similarly, if this field is set to 200, the bid price is twice the price of on-demand `r3.xlarge` instances. If not specified, the default value is 100. When spot instances are requested for this cluster, only spot instances whose bid price percentage matches this field will be considered. Note that, for safety, we enforce this field to be no more than 10000."
          },
          {
            "name": "zone_id",
            "type": "string",
            "description": "Identifier for the availability zone/datacenter in which the cluster resides. This string will be of a form like \"us-west-2a\". The provided availability zone must be in the same region as the Databricks deployment. For example, \"us-west-2a\" is not a valid zone id if the Databricks deployment resides in the \"us-east-1\" region. This is an optional field at cluster creation, and if not specified, the zone \"auto\" will be used. If the zone specified is \"auto\", will try to place cluster in a zone with high availability, and will retry placement in a different AZ if there is not enough capacity. The list of available zones as well as the default value can be found by using the `List Zones` method."
          }
        ]
      },
      {
        "name": "azure_attributes",
        "type": "object",
        "description": "Attributes related to clusters running on Microsoft Azure. If not specified at cluster creation, a set of default values will be used.",
        "children": [
          {
            "name": "availability",
            "type": "string",
            "description": "Availability type used for all subsequent nodes past the `first_on_demand` ones. Note: If `first_on_demand` is zero, this availability type will be used for the entire cluster. (ON_DEMAND_AZURE, SPOT_AZURE, SPOT_WITH_FALLBACK_AZURE)"
          },
          {
            "name": "first_on_demand",
            "type": "integer",
            "description": "The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
          },
          {
            "name": "log_analytics_info",
            "type": "object",
            "description": "Defines values necessary to configure and run Azure Log Analytics agent",
            "children": [
              {
                "name": "log_analytics_primary_key",
                "type": "string",
                "description": ""
              },
              {
                "name": "log_analytics_workspace_id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "spot_bid_max_price",
            "type": "number",
            "description": "The max bid price to be used for Azure spot instances. The Max price for the bid cannot be higher than the on-demand price of the instance. If not specified, the default value is -1, which specifies that the instance cannot be evicted on the basis of price, and only on the basis of availability. Further, the value should &gt; 0 or -1."
          }
        ]
      },
      {
        "name": "cluster_log_conf",
        "type": "object",
        "description": "The configuration for delivering spark logs to a long-term storage destination. Three kinds of destinations (DBFS, S3 and Unity Catalog volumes) are supported. Only one destination can be specified for one cluster. If the conf is given, the logs will be delivered to the destination every `5 mins`. The destination of driver logs is `$destination/$clusterId/driver`, while the destination of executor logs is `$destination/$clusterId/executor`.",
        "children": [
          {
            "name": "dbfs",
            "type": "object",
            "description": "destination needs to be provided. e.g. `&#123; \"dbfs\" : &#123; \"destination\" : \"dbfs:/home/cluster_log\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "dbfs destination, e.g. `dbfs:/my/path`"
              }
            ]
          },
          {
            "name": "s3",
            "type": "object",
            "description": "destination and either the region or endpoint need to be provided. e.g. `&#123; \"s3\": &#123; \"destination\" : \"s3://cluster_log_bucket/prefix\", \"region\" : \"us-west-2\" &#125; &#125;` Cluster iam role is used to access s3, please make sure the cluster iam role in `instance_profile_arn` has permission to write data to the s3 destination.",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "S3 destination, e.g. `s3://my-bucket/some-prefix` Note that logs will be delivered using cluster iam role, please make sure you set cluster iam role and the role has write access to the destination. Please also note that you cannot use AWS keys to deliver logs."
              },
              {
                "name": "canned_acl",
                "type": "string",
                "description": "(Optional) Set canned access control list for the logs, e.g. `bucket-owner-full-control`. If `canned_cal` is set, please make sure the cluster iam role has `s3:PutObjectAcl` permission on the destination bucket and prefix. The full list of possible canned acl can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl. Please also note that by default only the object owner gets full controls. If you are using cross account role for writing data, you may want to set `bucket-owner-full-control` to make bucket owner able to read the logs."
              },
              {
                "name": "enable_encryption",
                "type": "boolean",
                "description": "(Optional) Flag to enable server side encryption, `false` by default."
              },
              {
                "name": "encryption_type",
                "type": "string",
                "description": "(Optional) The encryption type, it could be `sse-s3` or `sse-kms`. It will be used only when encryption is enabled and the default type is `sse-s3`."
              },
              {
                "name": "endpoint",
                "type": "string",
                "description": "S3 endpoint, e.g. `https://s3-us-west-2.amazonaws.com`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
              },
              {
                "name": "kms_key",
                "type": "string",
                "description": "(Optional) Kms key which will be used if encryption is enabled and encryption type is set to `sse-kms`."
              },
              {
                "name": "region",
                "type": "string",
                "description": "S3 region, e.g. `us-west-2`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
              }
            ]
          },
          {
            "name": "volumes",
            "type": "object",
            "description": "destination needs to be provided, e.g. `&#123; \"volumes\": &#123; \"destination\": \"/Volumes/catalog/schema/volume/cluster_log\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "UC Volumes destination, e.g. `/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh` or `dbfs:/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh`"
              }
            ]
          }
        ]
      },
      {
        "name": "cluster_name",
        "type": "string",
        "description": "Cluster name requested by the user. This doesn't have to be unique. If not specified at creation, the cluster name will be an empty string. For job clusters, the cluster name is automatically set based on the job and job run IDs."
      },
      {
        "name": "custom_tags",
        "type": "object",
        "description": "Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS instances and EBS volumes) with these tags in addition to `default_tags`. Notes: - Currently, Databricks allows at most 45 custom tags - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags"
      },
      {
        "name": "data_security_mode",
        "type": "string",
        "description": "Data security mode decides what data governance model to use when accessing data from a cluster.<br /><br />The following modes can only be used when `kind = CLASSIC_PREVIEW`. * `DATA_SECURITY_MODE_AUTO`:<br />Databricks will choose the most appropriate access mode depending on your compute configuration.<br />* `DATA_SECURITY_MODE_STANDARD`: Alias for `USER_ISOLATION`. * `DATA_SECURITY_MODE_DEDICATED`:<br />Alias for `SINGLE_USER`.<br /><br />The following modes can be used regardless of `kind`. * `NONE`: No security isolation for<br />multiple users sharing the cluster. Data governance features are not available in this mode. *<br />`SINGLE_USER`: A secure cluster that can only be exclusively used by a single user specified in<br />`single_user_name`. Most programming languages, cluster features and data governance features<br />are available in this mode. * `USER_ISOLATION`: A secure cluster that can be shared by multiple<br />users. Cluster users are fully isolated so that they cannot see each other's data and<br />credentials. Most data governance features are supported in this mode. But programming languages<br />and cluster features might be limited.<br /><br />The following modes are deprecated starting with Databricks Runtime 15.0 and will be removed for<br />future Databricks Runtime versions:<br /><br />* `LEGACY_TABLE_ACL`: This mode is for users migrating from legacy Table ACL clusters. *<br />`LEGACY_PASSTHROUGH`: This mode is for users migrating from legacy Passthrough on high<br />concurrency clusters. * `LEGACY_SINGLE_USER`: This mode is for users migrating from legacy<br />Passthrough on standard clusters. * `LEGACY_SINGLE_USER_STANDARD`: This mode provides a way that<br />doesn’t have UC nor passthrough enabled. (DATA_SECURITY_MODE_AUTO, DATA_SECURITY_MODE_DEDICATED, DATA_SECURITY_MODE_STANDARD, LEGACY_PASSTHROUGH, LEGACY_SINGLE_USER, LEGACY_SINGLE_USER_STANDARD, LEGACY_TABLE_ACL, NONE, SINGLE_USER, USER_ISOLATION)"
      },
      {
        "name": "docker_image",
        "type": "object",
        "description": "Custom docker image BYOC",
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
        "name": "driver_instance_pool_id",
        "type": "string",
        "description": "The optional ID of the instance pool for the driver of the cluster belongs. The pool cluster uses the instance pool with id (instance_pool_id) if the driver pool is not assigned."
      },
      {
        "name": "driver_node_type_flexibility",
        "type": "object",
        "description": "Flexible node type configuration for the driver node.",
        "children": [
          {
            "name": "alternate_node_type_ids",
            "type": "array",
            "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
          }
        ]
      },
      {
        "name": "driver_node_type_id",
        "type": "string",
        "description": "The node type of the Spark driver. Note that this field is optional; if unset, the driver node type will be set as the same value as `node_type_id` defined above. This field, along with node_type_id, should not be set if virtual_cluster_size is set. If both driver_node_type_id, node_type_id, and virtual_cluster_size are specified, driver_node_type_id and node_type_id take precedence."
      },
      {
        "name": "enable_elastic_disk",
        "type": "boolean",
        "description": "Autoscaling Local Storage: when enabled, this cluster will dynamically acquire additional disk space when its Spark workers are running low on disk space."
      },
      {
        "name": "enable_local_disk_encryption",
        "type": "boolean",
        "description": "Whether to enable LUKS on cluster VMs' local disks"
      },
      {
        "name": "gcp_attributes",
        "type": "object",
        "description": "Attributes related to clusters running on Google Cloud Platform. If not specified at cluster creation, a set of default values will be used.",
        "children": [
          {
            "name": "availability",
            "type": "string",
            "description": "This field determines whether the spark executors will be scheduled to run on preemptible VMs, on-demand VMs, or preemptible VMs with a fallback to on-demand VMs if the former is unavailable. (ON_DEMAND_GCP, PREEMPTIBLE_GCP, PREEMPTIBLE_WITH_FALLBACK_GCP)"
          },
          {
            "name": "boot_disk_size",
            "type": "integer",
            "description": "Boot disk size in GB"
          },
          {
            "name": "first_on_demand",
            "type": "integer",
            "description": "The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
          },
          {
            "name": "google_service_account",
            "type": "string",
            "description": "If provided, the cluster will impersonate the google service account when accessing gcloud services (like GCS). The google service account must have previously been added to the Databricks environment by an account administrator."
          },
          {
            "name": "local_ssd_count",
            "type": "integer",
            "description": "If provided, each node (workers and driver) in the cluster will have this number of local SSDs attached. Each local SSD is 375GB in size. Refer to [GCP documentation] for the supported number of local SSDs for each instance type. [GCP documentation]: https://cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds"
          },
          {
            "name": "use_preemptible_executors",
            "type": "boolean",
            "description": "This field determines whether the spark executors will be scheduled to run on preemptible VMs (when set to true) versus standard compute engine VMs (when set to false; default). Note: Soon to be deprecated, use the 'availability' field instead."
          },
          {
            "name": "zone_id",
            "type": "string",
            "description": "Identifier for the availability zone in which the cluster resides. This can be one of the following: - \"HA\" =&gt; High availability, spread nodes across availability zones for a Databricks deployment region [default]. - \"AUTO\" =&gt; Databricks picks an availability zone to schedule the cluster on. - A GCP availability zone =&gt; Pick One of the available zones for (machine type + region) from https://cloud.google.com/compute/docs/regions-zones."
          }
        ]
      },
      {
        "name": "init_scripts",
        "type": "array",
        "description": "The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If `cluster_log_conf` is specified, init script logs are sent to `<destination>/<cluster-ID>/init_scripts`.",
        "children": [
          {
            "name": "abfss",
            "type": "object",
            "description": "destination needs to be provided, e.g. `abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<directory-name>`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "abfss destination, e.g. `abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<directory-name>`."
              }
            ]
          },
          {
            "name": "dbfs",
            "type": "object",
            "description": "destination needs to be provided. e.g. `&#123; \"dbfs\": &#123; \"destination\" : \"dbfs:/home/cluster_log\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "dbfs destination, e.g. `dbfs:/my/path`"
              }
            ]
          },
          {
            "name": "file",
            "type": "object",
            "description": "destination needs to be provided, e.g. `&#123; \"file\": &#123; \"destination\": \"file:/my/local/file.sh\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "gcs",
            "type": "object",
            "description": "destination needs to be provided, e.g. `&#123; \"gcs\": &#123; \"destination\": \"gs://my-bucket/file.sh\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "GCS destination/URI, e.g. `gs://my-bucket/some-prefix`"
              }
            ]
          },
          {
            "name": "s3",
            "type": "object",
            "description": "destination and either the region or endpoint need to be provided. e.g. `&#123; \\\"s3\\\": &#123; \\\"destination\\\": \\\"s3://cluster_log_bucket/prefix\\\", \\\"region\\\": \\\"us-west-2\\\" &#125; &#125;` Cluster iam role is used to access s3, please make sure the cluster iam role in `instance_profile_arn` has permission to write data to the s3 destination.",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "S3 destination, e.g. `s3://my-bucket/some-prefix` Note that logs will be delivered using cluster iam role, please make sure you set cluster iam role and the role has write access to the destination. Please also note that you cannot use AWS keys to deliver logs."
              },
              {
                "name": "canned_acl",
                "type": "string",
                "description": "(Optional) Set canned access control list for the logs, e.g. `bucket-owner-full-control`. If `canned_cal` is set, please make sure the cluster iam role has `s3:PutObjectAcl` permission on the destination bucket and prefix. The full list of possible canned acl can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl. Please also note that by default only the object owner gets full controls. If you are using cross account role for writing data, you may want to set `bucket-owner-full-control` to make bucket owner able to read the logs."
              },
              {
                "name": "enable_encryption",
                "type": "boolean",
                "description": "(Optional) Flag to enable server side encryption, `false` by default."
              },
              {
                "name": "encryption_type",
                "type": "string",
                "description": "(Optional) The encryption type, it could be `sse-s3` or `sse-kms`. It will be used only when encryption is enabled and the default type is `sse-s3`."
              },
              {
                "name": "endpoint",
                "type": "string",
                "description": "S3 endpoint, e.g. `https://s3-us-west-2.amazonaws.com`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
              },
              {
                "name": "kms_key",
                "type": "string",
                "description": "(Optional) Kms key which will be used if encryption is enabled and encryption type is set to `sse-kms`."
              },
              {
                "name": "region",
                "type": "string",
                "description": "S3 region, e.g. `us-west-2`. Either region or endpoint needs to be set. If both are set, endpoint will be used."
              }
            ]
          },
          {
            "name": "volumes",
            "type": "object",
            "description": "destination needs to be provided. e.g. `&#123; \\\"volumes\\\" : &#123; \\\"destination\\\" : \\\"/Volumes/my-init.sh\\\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "UC Volumes destination, e.g. `/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh` or `dbfs:/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh`"
              }
            ]
          },
          {
            "name": "workspace",
            "type": "object",
            "description": "destination needs to be provided, e.g. `&#123; \"workspace\": &#123; \"destination\": \"/cluster-init-scripts/setup-datadog.sh\" &#125; &#125;`",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "wsfs destination, e.g. `workspace:/cluster-init-scripts/setup-datadog.sh`"
              }
            ]
          }
        ]
      },
      {
        "name": "instance_pool_id",
        "type": "string",
        "description": "The optional ID of the instance pool to which the cluster belongs."
      },
      {
        "name": "is_single_node",
        "type": "boolean",
        "description": "This field can only be used when `kind = CLASSIC_PREVIEW`. When set to true, Databricks will automatically set single node related `custom_tags`, `spark_conf`, and `num_workers`"
      },
      {
        "name": "kind",
        "type": "string",
        "description": "The kind of compute described by this compute specification.<br /><br />Depending on `kind`, different validations and default values will be applied.<br /><br />Clusters with `kind = CLASSIC_PREVIEW` support the following fields, whereas clusters with no<br />specified `kind` do not. * [is_single_node](/api/workspace/clusters/create#is_single_node) *<br />[use_ml_runtime](/api/workspace/clusters/create#use_ml_runtime) *<br />[data_security_mode](/api/workspace/clusters/create#data_security_mode) set to<br />`DATA_SECURITY_MODE_AUTO`, `DATA_SECURITY_MODE_DEDICATED`, or `DATA_SECURITY_MODE_STANDARD`<br /><br />By using the [simple form], your clusters are automatically using `kind = CLASSIC_PREVIEW`.<br /><br />[simple form]: https://docs.databricks.com/compute/simple-form.html (CLASSIC_PREVIEW)"
      },
      {
        "name": "node_type_id",
        "type": "string",
        "description": "This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads. A list of available node types can be retrieved by using the :method:clusters/listNodeTypes API call."
      },
      {
        "name": "num_workers",
        "type": "integer",
        "description": "Number of worker nodes that this cluster should have. A cluster has one Spark Driver and `num_workers` Executors for a total of `num_workers` + 1 Spark nodes. Note: When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual current number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field will immediately be updated to reflect the target size of 10 workers, whereas the workers listed in `spark_info` will gradually increase from 5 to 10 as the new nodes are provisioned."
      },
      {
        "name": "policy_id",
        "type": "string",
        "description": "The ID of the cluster policy used to create the cluster if applicable."
      },
      {
        "name": "remote_disk_throughput",
        "type": "integer",
        "description": "If set, what the configurable throughput (in Mb/s) for the remote disk is. Currently only supported for GCP HYPERDISK_BALANCED disks."
      },
      {
        "name": "runtime_engine",
        "type": "string",
        "description": "Determines the cluster's runtime engine, either standard or Photon. This field is not compatible with legacy `spark_version` values that contain `-photon-`. Remove `-photon-` from the `spark_version` and set `runtime_engine` to `PHOTON`. If left unspecified, the runtime engine defaults to standard unless the spark_version contains -photon-, in which case Photon will be used. (NULL, PHOTON, STANDARD)"
      },
      {
        "name": "single_user_name",
        "type": "string",
        "description": "Single user name if data_security_mode is `SINGLE_USER`"
      },
      {
        "name": "spark_conf",
        "type": "object",
        "description": "An object containing a set of optional, user-specified Spark configuration key-value pairs. Users can also pass in a string of extra JVM options to the driver and the executors via `spark.driver.extraJavaOptions` and `spark.executor.extraJavaOptions` respectively."
      },
      {
        "name": "spark_env_vars",
        "type": "object",
        "description": "An object containing a set of optional, user-specified environment variable key-value pairs. Please note that key-value pair of the form (X,Y) will be exported as is (i.e., `export X='Y'`) while launching the driver and workers. In order to specify an additional set of `SPARK_DAEMON_JAVA_OPTS`, we recommend appending them to `$SPARK_DAEMON_JAVA_OPTS` as shown in the example below. This ensures that all default databricks managed environmental variables are included as well. Example Spark environment variables: `&#123;\"SPARK_WORKER_MEMORY\": \"28000m\", \"SPARK_LOCAL_DIRS\": \"/local_disk0\"&#125;` or `&#123;\"SPARK_DAEMON_JAVA_OPTS\": \"$SPARK_DAEMON_JAVA_OPTS -Dspark.shuffle.service.enabled=true\"&#125;`"
      },
      {
        "name": "spark_version",
        "type": "string",
        "description": "The Spark version of the cluster, e.g. `3.3.x-scala2.11`. A list of available Spark versions can be retrieved by using the :method:clusters/sparkVersions API call."
      },
      {
        "name": "ssh_public_keys",
        "type": "array",
        "description": "SSH public key contents that will be added to each Spark node in this cluster. The corresponding private keys can be used to login with the user name `ubuntu` on port `2200`. Up to 10 keys can be specified."
      },
      {
        "name": "total_initial_remote_disk_size",
        "type": "integer",
        "description": "If set, what the total initial volume size (in GB) of the remote disks should be. Currently only supported for GCP HYPERDISK_BALANCED disks."
      },
      {
        "name": "use_ml_runtime",
        "type": "boolean",
        "description": "This field can only be used when `kind = CLASSIC_PREVIEW`. `effective_spark_version` is determined by `spark_version` (DBR release), this field `use_ml_runtime`, and whether `node_type_id` is gpu node or not."
      },
      {
        "name": "worker_node_type_flexibility",
        "type": "object",
        "description": "Flexible node type configuration for worker nodes.",
        "children": [
          {
            "name": "alternate_node_type_ids",
            "type": "array",
            "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
          }
        ]
      },
      {
        "name": "workload_type",
        "type": "object",
        "description": "Cluster Attributes showing for clusters workload types.",
        "children": [
          {
            "name": "clients",
            "type": "object",
            "description": "defined what type of clients can use the cluster. E.g. Notebooks, Jobs",
            "children": [
              {
                "name": "jobs",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "notebooks",
                "type": "boolean",
                "description": "With notebooks set, this cluster can be used for notebooks"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "ssh_public_keys",
    "type": "array",
    "description": "SSH public key contents that will be added to each Spark node in this cluster. The corresponding private keys can be used to login with the user name `ubuntu` on port `2200`. Up to 10 keys can be specified."
  },
  {
    "name": "start_time",
    "type": "integer",
    "description": "Time (in epoch milliseconds) when the cluster creation request was received (when the cluster entered a `PENDING` state)."
  },
  {
    "name": "state",
    "type": "string",
    "description": "Current state of the cluster. (ERROR, PENDING, RESIZING, RESTARTING, RUNNING, TERMINATED, TERMINATING, UNKNOWN)"
  },
  {
    "name": "state_message",
    "type": "string",
    "description": "A message associated with the most recent state transition (e.g., the reason why the cluster entered a `TERMINATED` state)."
  },
  {
    "name": "terminated_time",
    "type": "integer",
    "description": "Time (in epoch milliseconds) when the cluster was terminated, if applicable."
  },
  {
    "name": "termination_reason",
    "type": "object",
    "description": "Information about why the cluster was terminated. This field only appears when the cluster is in a `TERMINATING` or `TERMINATED` state.",
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
    "name": "total_initial_remote_disk_size",
    "type": "integer",
    "description": "If set, what the total initial volume size (in GB) of the remote disks should be. Currently only supported for GCP HYPERDISK_BALANCED disks."
  },
  {
    "name": "use_ml_runtime",
    "type": "boolean",
    "description": "This field can only be used when `kind = CLASSIC_PREVIEW`. `effective_spark_version` is determined by `spark_version` (DBR release), this field `use_ml_runtime`, and whether `node_type_id` is gpu node or not."
  },
  {
    "name": "worker_node_type_flexibility",
    "type": "object",
    "description": "Flexible node type configuration for worker nodes.",
    "children": [
      {
        "name": "alternate_node_type_ids",
        "type": "array",
        "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
      }
    ]
  },
  {
    "name": "workload_type",
    "type": "object",
    "description": "Cluster Attributes showing for clusters workload types.",
    "children": [
      {
        "name": "clients",
        "type": "object",
        "description": "defined what type of clients can use the cluster. E.g. Notebooks, Jobs",
        "children": [
          {
            "name": "jobs",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "notebooks",
            "type": "boolean",
            "description": "With notebooks set, this cluster can be used for notebooks"
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Retrieves the information for a cluster given its identifier. Clusters can be described while they are</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-filter_by"><code>filter_by</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-sort_by"><code>sort_by</code></a></td>
    <td>Return information about all pinned and active clusters, and all clusters terminated within the last</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-spark_version"><code>spark_version</code></a></td>
    <td></td>
    <td>Creates a new Spark cluster. This method will acquire new instances from the cloud provider if</td>
</tr>
<tr>
    <td><a href="#change_owner"><CopyableCode code="change_owner" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-owner_username"><code>owner_username</code></a></td>
    <td></td>
    <td>Change the owner of the cluster. You must be an admin and the cluster must be terminated to perform</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a></td>
    <td></td>
    <td>Terminates the Spark cluster with the specified ID. The cluster is removed asynchronously. Once the</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-spark_version"><code>spark_version</code></a></td>
    <td></td>
    <td>Updates the configuration of a cluster to match the provided attributes and size. A cluster can be</td>
</tr>
<tr>
    <td><a href="#events"><CopyableCode code="events" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a></td>
    <td></td>
    <td>Retrieves a list of events about the activity of a cluster. This API is paginated. If there are more</td>
</tr>
<tr>
    <td><a href="#permanent_delete"><CopyableCode code="permanent_delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a></td>
    <td></td>
    <td>Permanently deletes a Spark cluster. This cluster is terminated and resources are asynchronously</td>
</tr>
<tr>
    <td><a href="#pin"><CopyableCode code="pin" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a></td>
    <td></td>
    <td>Pinning a cluster ensures that the cluster will always be returned by the ListClusters API. Pinning a</td>
</tr>
<tr>
    <td><a href="#resize"><CopyableCode code="resize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a></td>
    <td></td>
    <td>Resizes a cluster to have a desired number of workers. This will fail unless the cluster is in a</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a></td>
    <td></td>
    <td>Restarts a Spark cluster with the supplied ID. If the cluster is not currently in a `RUNNING` state,</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a></td>
    <td></td>
    <td>Starts a terminated Spark cluster with the supplied ID. This works similar to `createCluster` except:</td>
</tr>
<tr>
    <td><a href="#unpin"><CopyableCode code="unpin" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a></td>
    <td></td>
    <td>Unpinning a cluster will allow the cluster to eventually be removed from the ListClusters API.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a></td>
    <td></td>
    <td>Updates the configuration of a cluster to match the partial set of attributes and size. Denote which</td>
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
    <td>The cluster about which to retrieve information.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-filter_by">
    <td><CopyableCode code="filter_by" /></td>
    <td><code>object</code></td>
    <td>Filters to apply to the list of clusters.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Use this field to specify the maximum number of results to be returned by the server. The server may further constrain the maximum number of results returned in a single page.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Use next_page_token or prev_page_token returned from the previous request to list the next or previous page of clusters respectively.</td>
</tr>
<tr id="parameter-sort_by">
    <td><CopyableCode code="sort_by" /></td>
    <td><code>object</code></td>
    <td>Sort the list of clusters by a specific criteria.</td>
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

Retrieves the information for a cluster given its identifier. Clusters can be described while they are

```sql
SELECT
cluster_id,
driver_instance_pool_id,
driver_node_type_id,
instance_pool_id,
node_type_id,
policy_id,
spark_context_id,
cluster_name,
creator_user_name,
single_user_name,
autoscale,
autotermination_minutes,
aws_attributes,
azure_attributes,
cluster_cores,
cluster_log_conf,
cluster_log_status,
cluster_memory_mb,
cluster_source,
custom_tags,
data_security_mode,
default_tags,
docker_image,
driver,
driver_node_type_flexibility,
enable_elastic_disk,
enable_local_disk_encryption,
executors,
gcp_attributes,
init_scripts,
is_single_node,
jdbc_port,
kind,
last_restarted_time,
last_state_loss_time,
num_workers,
remote_disk_throughput,
runtime_engine,
spark_conf,
spark_env_vars,
spark_version,
spec,
ssh_public_keys,
start_time,
state,
state_message,
terminated_time,
termination_reason,
total_initial_remote_disk_size,
use_ml_runtime,
worker_node_type_flexibility,
workload_type
FROM databricks_workspace.compute.clusters
WHERE cluster_id = '{{ cluster_id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Return information about all pinned and active clusters, and all clusters terminated within the last

```sql
SELECT
cluster_id,
driver_instance_pool_id,
driver_node_type_id,
instance_pool_id,
node_type_id,
policy_id,
spark_context_id,
cluster_name,
creator_user_name,
single_user_name,
autoscale,
autotermination_minutes,
aws_attributes,
azure_attributes,
cluster_cores,
cluster_log_conf,
cluster_log_status,
cluster_memory_mb,
cluster_source,
custom_tags,
data_security_mode,
default_tags,
docker_image,
driver,
driver_node_type_flexibility,
enable_elastic_disk,
enable_local_disk_encryption,
executors,
gcp_attributes,
init_scripts,
is_single_node,
jdbc_port,
kind,
last_restarted_time,
last_state_loss_time,
num_workers,
remote_disk_throughput,
runtime_engine,
spark_conf,
spark_env_vars,
spark_version,
spec,
ssh_public_keys,
start_time,
state,
state_message,
terminated_time,
termination_reason,
total_initial_remote_disk_size,
use_ml_runtime,
worker_node_type_flexibility,
workload_type
FROM databricks_workspace.compute.clusters
WHERE workspace = '{{ workspace }}' -- required
AND filter_by = '{{ filter_by }}'
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND sort_by = '{{ sort_by }}'
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

Creates a new Spark cluster. This method will acquire new instances from the cloud provider if

```sql
INSERT INTO databricks_workspace.compute.clusters (
spark_version,
apply_policy_default_values,
autoscale,
autotermination_minutes,
aws_attributes,
azure_attributes,
clone_from,
cluster_log_conf,
cluster_name,
custom_tags,
data_security_mode,
docker_image,
driver_instance_pool_id,
driver_node_type_flexibility,
driver_node_type_id,
enable_elastic_disk,
enable_local_disk_encryption,
gcp_attributes,
init_scripts,
instance_pool_id,
is_single_node,
kind,
node_type_id,
num_workers,
policy_id,
remote_disk_throughput,
runtime_engine,
single_user_name,
spark_conf,
spark_env_vars,
ssh_public_keys,
total_initial_remote_disk_size,
use_ml_runtime,
worker_node_type_flexibility,
workload_type,
workspace
)
SELECT 
'{{ spark_version }}' /* required */,
{{ apply_policy_default_values }},
'{{ autoscale }}',
{{ autotermination_minutes }},
'{{ aws_attributes }}',
'{{ azure_attributes }}',
'{{ clone_from }}',
'{{ cluster_log_conf }}',
'{{ cluster_name }}',
'{{ custom_tags }}',
'{{ data_security_mode }}',
'{{ docker_image }}',
'{{ driver_instance_pool_id }}',
'{{ driver_node_type_flexibility }}',
'{{ driver_node_type_id }}',
{{ enable_elastic_disk }},
{{ enable_local_disk_encryption }},
'{{ gcp_attributes }}',
'{{ init_scripts }}',
'{{ instance_pool_id }}',
{{ is_single_node }},
'{{ kind }}',
'{{ node_type_id }}',
{{ num_workers }},
'{{ policy_id }}',
{{ remote_disk_throughput }},
'{{ runtime_engine }}',
'{{ single_user_name }}',
'{{ spark_conf }}',
'{{ spark_env_vars }}',
'{{ ssh_public_keys }}',
{{ total_initial_remote_disk_size }},
{{ use_ml_runtime }},
'{{ worker_node_type_flexibility }}',
'{{ workload_type }}',
'{{ workspace }}'
RETURNING
cluster_id,
driver_instance_pool_id,
driver_node_type_id,
instance_pool_id,
node_type_id,
policy_id,
spark_context_id,
cluster_name,
creator_user_name,
single_user_name,
autoscale,
autotermination_minutes,
aws_attributes,
azure_attributes,
cluster_cores,
cluster_log_conf,
cluster_log_status,
cluster_memory_mb,
cluster_source,
custom_tags,
data_security_mode,
default_tags,
docker_image,
driver,
driver_node_type_flexibility,
enable_elastic_disk,
enable_local_disk_encryption,
executors,
gcp_attributes,
init_scripts,
is_single_node,
jdbc_port,
kind,
last_restarted_time,
last_state_loss_time,
num_workers,
remote_disk_throughput,
runtime_engine,
spark_conf,
spark_env_vars,
spark_version,
spec,
ssh_public_keys,
start_time,
state,
state_message,
terminated_time,
termination_reason,
total_initial_remote_disk_size,
use_ml_runtime,
worker_node_type_flexibility,
workload_type
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: clusters
  props:
    - name: workspace
      value: string
      description: Required parameter for the clusters resource.
    - name: spark_version
      value: string
      description: |
        The Spark version of the cluster, e.g. `3.3.x-scala2.11`. A list of available Spark versions can be retrieved by using the :method:clusters/sparkVersions API call.
    - name: apply_policy_default_values
      value: boolean
      description: |
        When set to true, fixed and default values from the policy will be used for fields that are omitted. When set to false, only fixed values from the policy will be applied.
    - name: autoscale
      value: object
      description: |
        Parameters needed in order to automatically scale clusters up and down based on load. Note: autoscaling works best with DB runtime versions 3.0 or later.
      props:
      - name: max_workers
        value: integer
      - name: min_workers
        value: integer
        description: |
          The minimum number of workers to which the cluster can scale down when underutilized. It is also the initial number of workers the cluster will have after creation.
    - name: autotermination_minutes
      value: integer
      description: |
        Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this cluster will not be automatically terminated. If specified, the threshold must be between 10 and 10000 minutes. Users can also set this value to 0 to explicitly disable automatic termination.
    - name: aws_attributes
      value: object
      description: |
        Attributes related to clusters running on Amazon Web Services. If not specified at cluster creation, a set of default values will be used.
      props:
      - name: availability
        value: string
        description: |
          Availability type used for all subsequent nodes past the `first_on_demand` ones.
          Note: If `first_on_demand` is zero, this availability type will be used for the entire cluster.
      - name: ebs_volume_count
        value: integer
        description: |
          The number of volumes launched for each instance. Users can choose up to 10 volumes. This feature is only enabled for supported node types. Legacy node types cannot specify custom EBS volumes. For node types with no instance store, at least one EBS volume needs to be specified; otherwise, cluster creation will fail. These EBS volumes will be mounted at `/ebs0`, `/ebs1`, and etc. Instance store volumes will be mounted at `/local_disk0`, `/local_disk1`, and etc. If EBS volumes are attached, Databricks will configure Spark to use only the EBS volumes for scratch storage because heterogenously sized scratch devices can lead to inefficient disk utilization. If no EBS volumes are attached, Databricks will configure Spark to use instance store volumes. Please note that if EBS volumes are specified, then the Spark configuration `spark.local.dir` will be overridden.
      - name: ebs_volume_iops
        value: integer
        description: |
          If using gp3 volumes, what IOPS to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used.
      - name: ebs_volume_size
        value: integer
        description: |
          The size of each EBS volume (in GiB) launched for each instance. For general purpose SSD, this value must be within the range 100 - 4096. For throughput optimized HDD, this value must be within the range 500 - 4096.
      - name: ebs_volume_throughput
        value: integer
        description: |
          If using gp3 volumes, what throughput to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used.
      - name: ebs_volume_type
        value: string
        description: |
          The type of EBS volumes that will be launched with this cluster.
      - name: first_on_demand
        value: integer
        description: |
          The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. If this value is greater than 0, the cluster driver node in particular will be placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster.
      - name: instance_profile_arn
        value: string
        description: |
          Nodes for this cluster will only be placed on AWS instances with this instance profile. If ommitted, nodes will be placed on instances without an IAM instance profile. The instance profile must have previously been added to the Databricks environment by an account administrator. This feature may only be available to certain customer plans.
      - name: spot_bid_price_percent
        value: integer
        description: |
          The bid price for AWS spot instances, as a percentage of the corresponding instance type's on-demand price. For example, if this field is set to 50, and the cluster needs a new `r3.xlarge` spot instance, then the bid price is half of the price of on-demand `r3.xlarge` instances. Similarly, if this field is set to 200, the bid price is twice the price of on-demand `r3.xlarge` instances. If not specified, the default value is 100. When spot instances are requested for this cluster, only spot instances whose bid price percentage matches this field will be considered. Note that, for safety, we enforce this field to be no more than 10000.
      - name: zone_id
        value: string
        description: |
          Identifier for the availability zone/datacenter in which the cluster resides. This string will be of a form like "us-west-2a". The provided availability zone must be in the same region as the Databricks deployment. For example, "us-west-2a" is not a valid zone id if the Databricks deployment resides in the "us-east-1" region. This is an optional field at cluster creation, and if not specified, the zone "auto" will be used. If the zone specified is "auto", will try to place cluster in a zone with high availability, and will retry placement in a different AZ if there is not enough capacity. The list of available zones as well as the default value can be found by using the `List Zones` method.
    - name: azure_attributes
      value: object
      description: |
        Attributes related to clusters running on Microsoft Azure. If not specified at cluster creation, a set of default values will be used.
      props:
      - name: availability
        value: string
        description: |
          Availability type used for all subsequent nodes past the `first_on_demand` ones. Note: If `first_on_demand` is zero, this availability type will be used for the entire cluster.
      - name: first_on_demand
        value: integer
        description: |
          The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster.
      - name: log_analytics_info
        value: object
        description: |
          Defines values necessary to configure and run Azure Log Analytics agent
        props:
        - name: log_analytics_primary_key
          value: string
        - name: log_analytics_workspace_id
          value: string
      - name: spot_bid_max_price
        value: number
        description: |
          The max bid price to be used for Azure spot instances. The Max price for the bid cannot be higher than the on-demand price of the instance. If not specified, the default value is -1, which specifies that the instance cannot be evicted on the basis of price, and only on the basis of availability. Further, the value should > 0 or -1.
    - name: clone_from
      value: object
      description: |
        When specified, this clones libraries from a source cluster during the creation of a new cluster.
      props:
      - name: source_cluster_id
        value: string
    - name: cluster_log_conf
      value: object
      description: |
        The configuration for delivering spark logs to a long-term storage destination. Three kinds of destinations (DBFS, S3 and Unity Catalog volumes) are supported. Only one destination can be specified for one cluster. If the conf is given, the logs will be delivered to the destination every `5 mins`. The destination of driver logs is `$destination/$clusterId/driver`, while the destination of executor logs is `$destination/$clusterId/executor`.
      props:
      - name: dbfs
        value: object
        description: |
          destination needs to be provided. e.g. `{ "dbfs" : { "destination" : "dbfs:/home/cluster_log" } }`
        props:
        - name: destination
          value: string
          description: |
            dbfs destination, e.g. `dbfs:/my/path`
      - name: s3
        value: object
        description: |
          destination and either the region or endpoint need to be provided. e.g. `{ "s3": { "destination" : "s3://cluster_log_bucket/prefix", "region" : "us-west-2" } }` Cluster iam role is used to access s3, please make sure the cluster iam role in `instance_profile_arn` has permission to write data to the s3 destination.
        props:
        - name: destination
          value: string
          description: |
            S3 destination, e.g. `s3://my-bucket/some-prefix` Note that logs will be delivered using cluster iam role, please make sure you set cluster iam role and the role has write access to the destination. Please also note that you cannot use AWS keys to deliver logs.
        - name: canned_acl
          value: string
          description: |
            (Optional) Set canned access control list for the logs, e.g. `bucket-owner-full-control`. If `canned_cal` is set, please make sure the cluster iam role has `s3:PutObjectAcl` permission on the destination bucket and prefix. The full list of possible canned acl can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl. Please also note that by default only the object owner gets full controls. If you are using cross account role for writing data, you may want to set `bucket-owner-full-control` to make bucket owner able to read the logs.
        - name: enable_encryption
          value: boolean
          description: |
            (Optional) Flag to enable server side encryption, `false` by default.
        - name: encryption_type
          value: string
          description: |
            (Optional) The encryption type, it could be `sse-s3` or `sse-kms`. It will be used only when encryption is enabled and the default type is `sse-s3`.
        - name: endpoint
          value: string
          description: |
            S3 endpoint, e.g. `https://s3-us-west-2.amazonaws.com`. Either region or endpoint needs to be set. If both are set, endpoint will be used.
        - name: kms_key
          value: string
          description: |
            (Optional) Kms key which will be used if encryption is enabled and encryption type is set to `sse-kms`.
        - name: region
          value: string
          description: |
            S3 region, e.g. `us-west-2`. Either region or endpoint needs to be set. If both are set, endpoint will be used.
      - name: volumes
        value: object
        description: |
          destination needs to be provided, e.g. `{ "volumes": { "destination": "/Volumes/catalog/schema/volume/cluster_log" } }`
        props:
        - name: destination
          value: string
          description: |
            UC Volumes destination, e.g. `/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh` or `dbfs:/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh`
    - name: cluster_name
      value: string
      description: |
        Cluster name requested by the user. This doesn't have to be unique. If not specified at creation, the cluster name will be an empty string. For job clusters, the cluster name is automatically set based on the job and job run IDs.
    - name: custom_tags
      value: object
      description: |
        Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS instances and EBS volumes) with these tags in addition to `default_tags`. Notes: - Currently, Databricks allows at most 45 custom tags - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags
    - name: data_security_mode
      value: string
      description: |
        :param docker_image: :class:`DockerImage` (optional) Custom docker image BYOC
    - name: docker_image
      value: object
      props:
      - name: basic_auth
        value: object
        props:
        - name: password
          value: string
        - name: username
          value: string
          description: |
            Name of the user
      - name: url
        value: string
        description: |
          URL of the docker image.
    - name: driver_instance_pool_id
      value: string
      description: |
        The optional ID of the instance pool for the driver of the cluster belongs. The pool cluster uses the instance pool with id (instance_pool_id) if the driver pool is not assigned.
    - name: driver_node_type_flexibility
      value: object
      description: |
        Flexible node type configuration for the driver node.
      props:
      - name: alternate_node_type_ids
        value: array
        description: |
          A list of node type IDs to use as fallbacks when the primary node type is unavailable.
        items:
          type: string
    - name: driver_node_type_id
      value: string
      description: |
        The node type of the Spark driver. Note that this field is optional; if unset, the driver node type will be set as the same value as `node_type_id` defined above. This field, along with node_type_id, should not be set if virtual_cluster_size is set. If both driver_node_type_id, node_type_id, and virtual_cluster_size are specified, driver_node_type_id and node_type_id take precedence.
    - name: enable_elastic_disk
      value: boolean
      description: |
        Autoscaling Local Storage: when enabled, this cluster will dynamically acquire additional disk space when its Spark workers are running low on disk space.
    - name: enable_local_disk_encryption
      value: boolean
      description: |
        Whether to enable LUKS on cluster VMs' local disks
    - name: gcp_attributes
      value: object
      description: |
        Attributes related to clusters running on Google Cloud Platform. If not specified at cluster creation, a set of default values will be used.
      props:
      - name: availability
        value: string
        description: |
          This field determines whether the spark executors will be scheduled to run on preemptible VMs, on-demand VMs, or preemptible VMs with a fallback to on-demand VMs if the former is unavailable.
      - name: boot_disk_size
        value: integer
        description: |
          Boot disk size in GB
      - name: first_on_demand
        value: integer
        description: |
          The first `first_on_demand` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, `first_on_demand` nodes will be placed on on-demand instances and the remainder will be placed on `availability` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster.
      - name: google_service_account
        value: string
        description: |
          If provided, the cluster will impersonate the google service account when accessing gcloud services (like GCS). The google service account must have previously been added to the Databricks environment by an account administrator.
      - name: local_ssd_count
        value: integer
        description: |
          If provided, each node (workers and driver) in the cluster will have this number of local SSDs attached. Each local SSD is 375GB in size. Refer to [GCP documentation] for the supported number of local SSDs for each instance type. [GCP documentation]: https://cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds
      - name: use_preemptible_executors
        value: boolean
        description: |
          This field determines whether the spark executors will be scheduled to run on preemptible VMs (when set to true) versus standard compute engine VMs (when set to false; default). Note: Soon to be deprecated, use the 'availability' field instead.
      - name: zone_id
        value: string
        description: |
          Identifier for the availability zone in which the cluster resides. This can be one of the following: - "HA" => High availability, spread nodes across availability zones for a Databricks deployment region [default]. - "AUTO" => Databricks picks an availability zone to schedule the cluster on. - A GCP availability zone => Pick One of the available zones for (machine type + region) from https://cloud.google.com/compute/docs/regions-zones.
    - name: init_scripts
      value: array
      description: |
        The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If `cluster_log_conf` is specified, init script logs are sent to `<destination>/<cluster-ID>/init_scripts`.
      props:
      - name: abfss
        value: object
        description: |
          destination needs to be provided, e.g. `abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<directory-name>`
        props:
        - name: destination
          value: string
          description: |
            abfss destination, e.g. `abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<directory-name>`.
      - name: dbfs
        value: object
        description: |
          destination needs to be provided. e.g. `{ "dbfs": { "destination" : "dbfs:/home/cluster_log" } }`
        props:
        - name: destination
          value: string
          description: |
            dbfs destination, e.g. `dbfs:/my/path`
      - name: file
        value: object
        description: |
          destination needs to be provided, e.g. `{ "file": { "destination": "file:/my/local/file.sh" } }`
        props:
        - name: destination
          value: string
      - name: gcs
        value: object
        description: |
          destination needs to be provided, e.g. `{ "gcs": { "destination": "gs://my-bucket/file.sh" } }`
        props:
        - name: destination
          value: string
          description: |
            GCS destination/URI, e.g. `gs://my-bucket/some-prefix`
      - name: s3
        value: object
        description: |
          destination and either the region or endpoint need to be provided. e.g. `{ \"s3\": { \"destination\": \"s3://cluster_log_bucket/prefix\", \"region\": \"us-west-2\" } }` Cluster iam role is used to access s3, please make sure the cluster iam role in `instance_profile_arn` has permission to write data to the s3 destination.
        props:
        - name: destination
          value: string
          description: |
            S3 destination, e.g. `s3://my-bucket/some-prefix` Note that logs will be delivered using cluster iam role, please make sure you set cluster iam role and the role has write access to the destination. Please also note that you cannot use AWS keys to deliver logs.
        - name: canned_acl
          value: string
          description: |
            (Optional) Set canned access control list for the logs, e.g. `bucket-owner-full-control`. If `canned_cal` is set, please make sure the cluster iam role has `s3:PutObjectAcl` permission on the destination bucket and prefix. The full list of possible canned acl can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl. Please also note that by default only the object owner gets full controls. If you are using cross account role for writing data, you may want to set `bucket-owner-full-control` to make bucket owner able to read the logs.
        - name: enable_encryption
          value: boolean
          description: |
            (Optional) Flag to enable server side encryption, `false` by default.
        - name: encryption_type
          value: string
          description: |
            (Optional) The encryption type, it could be `sse-s3` or `sse-kms`. It will be used only when encryption is enabled and the default type is `sse-s3`.
        - name: endpoint
          value: string
          description: |
            S3 endpoint, e.g. `https://s3-us-west-2.amazonaws.com`. Either region or endpoint needs to be set. If both are set, endpoint will be used.
        - name: kms_key
          value: string
          description: |
            (Optional) Kms key which will be used if encryption is enabled and encryption type is set to `sse-kms`.
        - name: region
          value: string
          description: |
            S3 region, e.g. `us-west-2`. Either region or endpoint needs to be set. If both are set, endpoint will be used.
      - name: volumes
        value: object
        description: |
          destination needs to be provided. e.g. `{ \"volumes\" : { \"destination\" : \"/Volumes/my-init.sh\" } }`
        props:
        - name: destination
          value: string
          description: |
            UC Volumes destination, e.g. `/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh` or `dbfs:/Volumes/catalog/schema/vol1/init-scripts/setup-datadog.sh`
      - name: workspace
        value: object
        description: |
          destination needs to be provided, e.g. `{ "workspace": { "destination": "/cluster-init-scripts/setup-datadog.sh" } }`
        props:
        - name: destination
          value: string
          description: |
            wsfs destination, e.g. `workspace:/cluster-init-scripts/setup-datadog.sh`
    - name: instance_pool_id
      value: string
      description: |
        The optional ID of the instance pool to which the cluster belongs.
    - name: is_single_node
      value: boolean
      description: |
        This field can only be used when `kind = CLASSIC_PREVIEW`. When set to true, Databricks will automatically set single node related `custom_tags`, `spark_conf`, and `num_workers`
    - name: kind
      value: string
      description: |
        :param node_type_id: str (optional) This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads. A list of available node types can be retrieved by using the :method:clusters/listNodeTypes API call.
    - name: node_type_id
      value: string
    - name: num_workers
      value: integer
      description: |
        Number of worker nodes that this cluster should have. A cluster has one Spark Driver and `num_workers` Executors for a total of `num_workers` + 1 Spark nodes. Note: When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual current number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field will immediately be updated to reflect the target size of 10 workers, whereas the workers listed in `spark_info` will gradually increase from 5 to 10 as the new nodes are provisioned.
    - name: policy_id
      value: string
      description: |
        The ID of the cluster policy used to create the cluster if applicable.
    - name: remote_disk_throughput
      value: integer
      description: |
        If set, what the configurable throughput (in Mb/s) for the remote disk is. Currently only supported for GCP HYPERDISK_BALANCED disks.
    - name: runtime_engine
      value: string
      description: |
        Determines the cluster's runtime engine, either standard or Photon. This field is not compatible with legacy `spark_version` values that contain `-photon-`. Remove `-photon-` from the `spark_version` and set `runtime_engine` to `PHOTON`. If left unspecified, the runtime engine defaults to standard unless the spark_version contains -photon-, in which case Photon will be used.
    - name: single_user_name
      value: string
      description: |
        Single user name if data_security_mode is `SINGLE_USER`
    - name: spark_conf
      value: object
      description: |
        An object containing a set of optional, user-specified Spark configuration key-value pairs. Users can also pass in a string of extra JVM options to the driver and the executors via `spark.driver.extraJavaOptions` and `spark.executor.extraJavaOptions` respectively.
    - name: spark_env_vars
      value: object
      description: |
        An object containing a set of optional, user-specified environment variable key-value pairs. Please note that key-value pair of the form (X,Y) will be exported as is (i.e., `export X='Y'`) while launching the driver and workers. In order to specify an additional set of `SPARK_DAEMON_JAVA_OPTS`, we recommend appending them to `$SPARK_DAEMON_JAVA_OPTS` as shown in the example below. This ensures that all default databricks managed environmental variables are included as well. Example Spark environment variables: `{"SPARK_WORKER_MEMORY": "28000m", "SPARK_LOCAL_DIRS": "/local_disk0"}` or `{"SPARK_DAEMON_JAVA_OPTS": "$SPARK_DAEMON_JAVA_OPTS -Dspark.shuffle.service.enabled=true"}`
    - name: ssh_public_keys
      value: array
      description: |
        SSH public key contents that will be added to each Spark node in this cluster. The corresponding private keys can be used to login with the user name `ubuntu` on port `2200`. Up to 10 keys can be specified.
      items:
        type: string
    - name: total_initial_remote_disk_size
      value: integer
      description: |
        If set, what the total initial volume size (in GB) of the remote disks should be. Currently only supported for GCP HYPERDISK_BALANCED disks.
    - name: use_ml_runtime
      value: boolean
      description: |
        This field can only be used when `kind = CLASSIC_PREVIEW`. `effective_spark_version` is determined by `spark_version` (DBR release), this field `use_ml_runtime`, and whether `node_type_id` is gpu node or not.
    - name: worker_node_type_flexibility
      value: object
      description: |
        Flexible node type configuration for worker nodes.
      props:
      - name: alternate_node_type_ids
        value: array
        description: |
          A list of node type IDs to use as fallbacks when the primary node type is unavailable.
        items:
          type: string
    - name: workload_type
      value: object
      description: |
        :returns: Long-running operation waiter for :class:`ClusterDetails`. See :method:wait_get_cluster_running for more details.
      props:
      - name: clients
        value: object
        description: |
          defined what type of clients can use the cluster. E.g. Notebooks, Jobs
        props:
        - name: jobs
          value: boolean
        - name: notebooks
          value: boolean
          description: |
            With notebooks set, this cluster can be used for notebooks
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="change_owner"
    values={[
        { label: 'change_owner', value: 'change_owner' },
        { label: 'delete', value: 'delete' },
        { label: 'edit', value: 'edit' },
        { label: 'events', value: 'events' },
        { label: 'permanent_delete', value: 'permanent_delete' },
        { label: 'pin', value: 'pin' },
        { label: 'resize', value: 'resize' },
        { label: 'restart', value: 'restart' },
        { label: 'start', value: 'start' },
        { label: 'unpin', value: 'unpin' },
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="change_owner">

Change the owner of the cluster. You must be an admin and the cluster must be terminated to perform

```sql
EXEC databricks_workspace.compute.clusters.change_owner 
@workspace='{{ workspace }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}", 
"owner_username": "{{ owner_username }}"
}'
;
```
</TabItem>
<TabItem value="delete">

Terminates the Spark cluster with the specified ID. The cluster is removed asynchronously. Once the

```sql
EXEC databricks_workspace.compute.clusters.delete 
@workspace='{{ workspace }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}"
}'
;
```
</TabItem>
<TabItem value="edit">

Updates the configuration of a cluster to match the provided attributes and size. A cluster can be

```sql
EXEC databricks_workspace.compute.clusters.edit 
@workspace='{{ workspace }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}", 
"spark_version": "{{ spark_version }}", 
"apply_policy_default_values": {{ apply_policy_default_values }}, 
"autoscale": "{{ autoscale }}", 
"autotermination_minutes": {{ autotermination_minutes }}, 
"aws_attributes": "{{ aws_attributes }}", 
"azure_attributes": "{{ azure_attributes }}", 
"cluster_log_conf": "{{ cluster_log_conf }}", 
"cluster_name": "{{ cluster_name }}", 
"custom_tags": "{{ custom_tags }}", 
"data_security_mode": "{{ data_security_mode }}", 
"docker_image": "{{ docker_image }}", 
"driver_instance_pool_id": "{{ driver_instance_pool_id }}", 
"driver_node_type_flexibility": "{{ driver_node_type_flexibility }}", 
"driver_node_type_id": "{{ driver_node_type_id }}", 
"enable_elastic_disk": {{ enable_elastic_disk }}, 
"enable_local_disk_encryption": {{ enable_local_disk_encryption }}, 
"gcp_attributes": "{{ gcp_attributes }}", 
"init_scripts": "{{ init_scripts }}", 
"instance_pool_id": "{{ instance_pool_id }}", 
"is_single_node": {{ is_single_node }}, 
"kind": "{{ kind }}", 
"node_type_id": "{{ node_type_id }}", 
"num_workers": {{ num_workers }}, 
"policy_id": "{{ policy_id }}", 
"remote_disk_throughput": {{ remote_disk_throughput }}, 
"runtime_engine": "{{ runtime_engine }}", 
"single_user_name": "{{ single_user_name }}", 
"spark_conf": "{{ spark_conf }}", 
"spark_env_vars": "{{ spark_env_vars }}", 
"ssh_public_keys": "{{ ssh_public_keys }}", 
"total_initial_remote_disk_size": {{ total_initial_remote_disk_size }}, 
"use_ml_runtime": {{ use_ml_runtime }}, 
"worker_node_type_flexibility": "{{ worker_node_type_flexibility }}", 
"workload_type": "{{ workload_type }}"
}'
;
```
</TabItem>
<TabItem value="events">

Retrieves a list of events about the activity of a cluster. This API is paginated. If there are more

```sql
EXEC databricks_workspace.compute.clusters.events 
@workspace='{{ workspace }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}", 
"end_time": {{ end_time }}, 
"event_types": "{{ event_types }}", 
"limit": {{ limit }}, 
"offset": {{ offset }}, 
"order": "{{ order }}", 
"page_size": {{ page_size }}, 
"page_token": "{{ page_token }}", 
"start_time": {{ start_time }}
}'
;
```
</TabItem>
<TabItem value="permanent_delete">

Permanently deletes a Spark cluster. This cluster is terminated and resources are asynchronously

```sql
EXEC databricks_workspace.compute.clusters.permanent_delete 
@workspace='{{ workspace }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}"
}'
;
```
</TabItem>
<TabItem value="pin">

Pinning a cluster ensures that the cluster will always be returned by the ListClusters API. Pinning a

```sql
EXEC databricks_workspace.compute.clusters.pin 
@workspace='{{ workspace }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}"
}'
;
```
</TabItem>
<TabItem value="resize">

Resizes a cluster to have a desired number of workers. This will fail unless the cluster is in a

```sql
EXEC databricks_workspace.compute.clusters.resize 
@workspace='{{ workspace }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}", 
"autoscale": "{{ autoscale }}", 
"num_workers": {{ num_workers }}
}'
;
```
</TabItem>
<TabItem value="restart">

Restarts a Spark cluster with the supplied ID. If the cluster is not currently in a `RUNNING` state,

```sql
EXEC databricks_workspace.compute.clusters.restart 
@workspace='{{ workspace }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}", 
"restart_user": "{{ restart_user }}"
}'
;
```
</TabItem>
<TabItem value="start">

Starts a terminated Spark cluster with the supplied ID. This works similar to `createCluster` except:

```sql
EXEC databricks_workspace.compute.clusters.start 
@workspace='{{ workspace }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}"
}'
;
```
</TabItem>
<TabItem value="unpin">

Unpinning a cluster will allow the cluster to eventually be removed from the ListClusters API.

```sql
EXEC databricks_workspace.compute.clusters.unpin 
@workspace='{{ workspace }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}"
}'
;
```
</TabItem>
<TabItem value="update">

Updates the configuration of a cluster to match the partial set of attributes and size. Denote which

```sql
EXEC databricks_workspace.compute.clusters.update 
@workspace='{{ workspace }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}", 
"update_mask": "{{ update_mask }}", 
"cluster": "{{ cluster }}"
}'
;
```
</TabItem>
</Tabs>

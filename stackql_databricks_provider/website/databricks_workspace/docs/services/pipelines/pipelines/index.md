---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - pipelines
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

Creates, updates, deletes, gets or lists a <code>pipelines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.pipelines.pipelines" /></td></tr>
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
    "name": "name",
    "type": "string",
    "description": "A human friendly identifier for the pipeline, taken from the `spec`."
  },
  {
    "name": "cluster_id",
    "type": "string",
    "description": "The ID of the cluster that the pipeline is running on."
  },
  {
    "name": "effective_budget_policy_id",
    "type": "string",
    "description": "Serverless budget policy ID of this pipeline."
  },
  {
    "name": "pipeline_id",
    "type": "string",
    "description": "The ID of the pipeline."
  },
  {
    "name": "creator_user_name",
    "type": "string",
    "description": "The username of the pipeline creator."
  },
  {
    "name": "run_as_user_name",
    "type": "string",
    "description": "Username of the user that the pipeline will run on behalf of."
  },
  {
    "name": "cause",
    "type": "string",
    "description": ""
  },
  {
    "name": "health",
    "type": "string",
    "description": "The health of a pipeline."
  },
  {
    "name": "last_modified",
    "type": "integer",
    "description": "The last time the pipeline settings were modified or created."
  },
  {
    "name": "latest_updates",
    "type": "array",
    "description": "Status of the latest updates for the pipeline. Ordered with the newest update first.",
    "children": [
      {
        "name": "creation_time",
        "type": "string",
        "description": ""
      },
      {
        "name": "state",
        "type": "string",
        "description": "The update state."
      },
      {
        "name": "update_id",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "run_as",
    "type": "object",
    "description": "The user or service principal that the pipeline runs as, if specified in the request. This field indicates the explicit configuration of `run_as` for the pipeline. To find the value in all cases, explicit or implicit, use `run_as_user_name`.",
    "children": [
      {
        "name": "service_principal_name",
        "type": "string",
        "description": "Application ID of an active service principal. Setting this field requires the `servicePrincipal/user` role."
      },
      {
        "name": "user_name",
        "type": "string",
        "description": "The email of an active workspace user. Users can only set this field to their own email."
      }
    ]
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The pipeline specification. This field is not returned when called by `ListPipelines`.",
    "children": [
      {
        "name": "budget_policy_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "catalog",
        "type": "string",
        "description": "A catalog in Unity Catalog to publish data from this pipeline to. If `target` is specified, tables in this pipeline are published to a `target` schema inside `catalog` (for example, `catalog`.`target`.`table`). If `target` is not specified, no data is published to Unity Catalog."
      },
      {
        "name": "channel",
        "type": "string",
        "description": "DLT Release Channel that specifies which version to use."
      },
      {
        "name": "clusters",
        "type": "array",
        "description": "Cluster settings for this pipeline deployment.",
        "children": [
          {
            "name": "apply_policy_default_values",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "autoscale",
            "type": "object",
            "description": "Parameters needed in order to automatically scale clusters up and down based on load. Note: autoscaling works best with DB runtime versions 3.0 or later.",
            "children": [
              {
                "name": "min_workers",
                "type": "integer",
                "description": ""
              },
              {
                "name": "max_workers",
                "type": "integer",
                "description": "The maximum number of workers to which the cluster can scale up when overloaded. `max_workers` must be strictly greater than `min_workers`."
              },
              {
                "name": "mode",
                "type": "string",
                "description": "Databricks Enhanced Autoscaling optimizes cluster utilization by automatically allocating cluster resources based on workload volume, with minimal impact to the data processing latency of your pipelines. Enhanced Autoscaling is available for `updates` clusters only. The legacy autoscaling feature is used for `maintenance` clusters."
              }
            ]
          },
          {
            "name": "aws_attributes",
            "type": "string",
            "description": "Attributes related to clusters running on Amazon Web Services. If not specified at cluster creation, a set of default values will be used."
          },
          {
            "name": "azure_attributes",
            "type": "string",
            "description": "Attributes related to clusters running on Microsoft Azure. If not specified at cluster creation, a set of default values will be used."
          },
          {
            "name": "cluster_log_conf",
            "type": "string",
            "description": "The configuration for delivering spark logs to a long-term storage destination. Only dbfs destinations are supported. Only one destination can be specified for one cluster. If the conf is given, the logs will be delivered to the destination every `5 mins`. The destination of driver logs is `$destination/$clusterId/driver`, while the destination of executor logs is `$destination/$clusterId/executor`."
          },
          {
            "name": "custom_tags",
            "type": "object",
            "description": "Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS instances and EBS volumes) with these tags in addition to `default_tags`. Notes: - Currently, Databricks allows at most 45 custom tags - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags"
          },
          {
            "name": "driver_instance_pool_id",
            "type": "string",
            "description": "The optional ID of the instance pool for the driver of the cluster belongs. The pool cluster uses the instance pool with id (instance_pool_id) if the driver pool is not assigned."
          },
          {
            "name": "driver_node_type_id",
            "type": "string",
            "description": "The node type of the Spark driver. Note that this field is optional; if unset, the driver node type will be set as the same value as `node_type_id` defined above."
          },
          {
            "name": "enable_local_disk_encryption",
            "type": "boolean",
            "description": "Whether to enable local disk encryption for the cluster."
          },
          {
            "name": "gcp_attributes",
            "type": "string",
            "description": "Attributes related to clusters running on Google Cloud Platform. If not specified at cluster creation, a set of default values will be used."
          },
          {
            "name": "init_scripts",
            "type": "string",
            "description": "The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If `cluster_log_conf` is specified, init script logs are sent to `<destination>/<cluster-ID>/init_scripts`."
          },
          {
            "name": "instance_pool_id",
            "type": "string",
            "description": "The optional ID of the instance pool to which the cluster belongs."
          },
          {
            "name": "label",
            "type": "string",
            "description": "A label for the cluster specification, either `default` to configure the default cluster, or `maintenance` to configure the maintenance cluster. This field is optional. The default value is `default`."
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
            "name": "spark_conf",
            "type": "object",
            "description": "An object containing a set of optional, user-specified Spark configuration key-value pairs. See :method:clusters/create for more details."
          },
          {
            "name": "spark_env_vars",
            "type": "object",
            "description": "An object containing a set of optional, user-specified environment variable key-value pairs. Please note that key-value pair of the form (X,Y) will be exported as is (i.e., `export X='Y'`) while launching the driver and workers. In order to specify an additional set of `SPARK_DAEMON_JAVA_OPTS`, we recommend appending them to `$SPARK_DAEMON_JAVA_OPTS` as shown in the example below. This ensures that all default databricks managed environmental variables are included as well. Example Spark environment variables: `&#123;\"SPARK_WORKER_MEMORY\": \"28000m\", \"SPARK_LOCAL_DIRS\": \"/local_disk0\"&#125;` or `&#123;\"SPARK_DAEMON_JAVA_OPTS\": \"$SPARK_DAEMON_JAVA_OPTS -Dspark.shuffle.service.enabled=true\"&#125;`"
          },
          {
            "name": "ssh_public_keys",
            "type": "array",
            "description": "SSH public key contents that will be added to each Spark node in this cluster. The corresponding private keys can be used to login with the user name `ubuntu` on port `2200`. Up to 10 keys can be specified."
          }
        ]
      },
      {
        "name": "configuration",
        "type": "object",
        "description": "String-String configuration for this pipeline execution."
      },
      {
        "name": "continuous",
        "type": "boolean",
        "description": "Whether the pipeline is continuous or triggered. This replaces `trigger`."
      },
      {
        "name": "deployment",
        "type": "object",
        "description": "Deployment type of this pipeline.",
        "children": [
          {
            "name": "kind",
            "type": "string",
            "description": "The deployment method that manages the pipeline: - BUNDLE: The pipeline is managed by a<br />Databricks Asset Bundle."
          },
          {
            "name": "metadata_file_path",
            "type": "string",
            "description": "The path to the file containing metadata about the deployment."
          }
        ]
      },
      {
        "name": "development",
        "type": "boolean",
        "description": "Whether the pipeline is in Development mode. Defaults to false."
      },
      {
        "name": "edition",
        "type": "string",
        "description": "Pipeline product edition."
      },
      {
        "name": "environment",
        "type": "object",
        "description": "Environment specification for this pipeline used to install dependencies.",
        "children": [
          {
            "name": "dependencies",
            "type": "array",
            "description": "List of pip dependencies, as supported by the version of pip in this environment. Each dependency is a pip requirement file line https://pip.pypa.io/en/stable/reference/requirements-file-format/ Allowed dependency could be &lt;requirement specifier&gt;, &lt;archive url/path&gt;, &lt;local project path&gt;(WSFS or Volumes in Databricks), &lt;vcs project url&gt;"
          }
        ]
      },
      {
        "name": "event_log",
        "type": "object",
        "description": "Event log configuration for this pipeline",
        "children": [
          {
            "name": "catalog",
            "type": "string",
            "description": "The UC catalog the event log is published under."
          },
          {
            "name": "name",
            "type": "string",
            "description": "The name the event log is published to in UC."
          },
          {
            "name": "schema",
            "type": "string",
            "description": "The UC schema the event log is published under."
          }
        ]
      },
      {
        "name": "filters",
        "type": "object",
        "description": "Filters on which Pipeline packages to include in the deployed graph.",
        "children": [
          {
            "name": "exclude",
            "type": "array",
            "description": ""
          },
          {
            "name": "include",
            "type": "array",
            "description": "Paths to include."
          }
        ]
      },
      {
        "name": "gateway_definition",
        "type": "object",
        "description": "The definition of a gateway pipeline to support change data capture.",
        "children": [
          {
            "name": "connection_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "gateway_storage_catalog",
            "type": "string",
            "description": "Required, Immutable. The name of the catalog for the gateway pipeline's storage location."
          },
          {
            "name": "gateway_storage_schema",
            "type": "string",
            "description": "Required, Immutable. The name of the schema for the gateway pipelines's storage location."
          },
          {
            "name": "connection_id",
            "type": "string",
            "description": "[Deprecated, use connection_name instead] Immutable. The Unity Catalog connection that this gateway pipeline uses to communicate with the source."
          },
          {
            "name": "connection_parameters",
            "type": "object",
            "description": "Optional, Internal. Parameters required to establish an initial connection with the source.",
            "children": [
              {
                "name": "source_catalog",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "gateway_storage_name",
            "type": "string",
            "description": "Optional. The Unity Catalog-compatible name for the gateway storage location. This is the destination to use for the data that is extracted by the gateway. Spark Declarative Pipelines system will automatically create the storage location under the catalog and schema."
          }
        ]
      },
      {
        "name": "id",
        "type": "string",
        "description": "Unique identifier for this pipeline."
      },
      {
        "name": "ingestion_definition",
        "type": "object",
        "description": "The configuration for a managed ingestion pipeline. These settings cannot be used with the 'libraries', 'schema', 'target', or 'catalog' settings.",
        "children": [
          {
            "name": "connection_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "full_refresh_window",
            "type": "object",
            "description": "(Optional) A window that specifies a set of time ranges for snapshot queries in CDC.",
            "children": [
              {
                "name": "start_hour",
                "type": "integer",
                "description": "An integer between 0 and 23 denoting the start hour for the window in the 24-hour day."
              },
              {
                "name": "days_of_week",
                "type": "array",
                "description": "Days of week in which the window is allowed to happen If not specified all days of the week will be used."
              },
              {
                "name": "time_zone_id",
                "type": "string",
                "description": "Time zone id of window. See https://docs.databricks.com/sql/language-manual/sql-ref-syntax-aux-conf-mgmt-set-timezone.html for details. If not specified, UTC will be used."
              }
            ]
          },
          {
            "name": "ingest_from_uc_foreign_catalog",
            "type": "boolean",
            "description": "Immutable. If set to true, the pipeline will ingest tables from the UC foreign catalogs directly without the need to specify a UC connection or ingestion gateway. The `source_catalog` fields in objects of IngestionConfig are interpreted as the UC foreign catalogs to ingest from."
          },
          {
            "name": "ingestion_gateway_id",
            "type": "string",
            "description": "Identifier for the gateway that is used by this ingestion pipeline to communicate with the source database. This is used with CDC connectors to databases like SQL Server using a gateway pipeline (connector_type = CDC). Under certain conditions, this can be replaced with connection_name to change the connector to Combined Cdc Managed Ingestion Pipeline."
          },
          {
            "name": "netsuite_jar_path",
            "type": "string",
            "description": "Netsuite only configuration. When the field is set for a netsuite connector, the jar stored in the field will be validated and added to the classpath of pipeline's cluster."
          },
          {
            "name": "objects",
            "type": "array",
            "description": "Required. Settings specifying tables to replicate and the destination for the replicated tables.",
            "children": [
              {
                "name": "report",
                "type": "object",
                "description": ""
              },
              {
                "name": "schema",
                "type": "object",
                "description": "Select all tables from a specific source schema."
              },
              {
                "name": "table",
                "type": "object",
                "description": "Select a specific source table."
              }
            ]
          },
          {
            "name": "source_configurations",
            "type": "array",
            "description": "Top-level source configurations",
            "children": [
              {
                "name": "catalog",
                "type": "object",
                "description": "SourceCatalogConfig contains catalog-level custom configuration parameters for each source"
              }
            ]
          },
          {
            "name": "source_type",
            "type": "string",
            "description": "The type of the foreign source. The source type will be inferred from the source connection or ingestion gateway. This field is output only and will be ignored if provided."
          },
          {
            "name": "table_configuration",
            "type": "object",
            "description": "Configuration settings to control the ingestion of tables. These settings are applied to all tables in the pipeline.",
            "children": [
              {
                "name": "auto_full_refresh_policy",
                "type": "object",
                "description": "Policy for auto full refresh."
              },
              {
                "name": "exclude_columns",
                "type": "array",
                "description": "A list of column names to be excluded for the ingestion. When not specified, include_columns fully controls what columns to be ingested. When specified, all other columns including future ones will be automatically included for ingestion. This field in mutually exclusive with `include_columns`."
              },
              {
                "name": "include_columns",
                "type": "array",
                "description": "A list of column names to be included for the ingestion. When not specified, all columns except ones in exclude_columns will be included. Future columns will be automatically included. When specified, all other future columns will be automatically excluded from ingestion. This field in mutually exclusive with `exclude_columns`."
              },
              {
                "name": "primary_keys",
                "type": "array",
                "description": "The primary key of the table used to apply changes."
              },
              {
                "name": "query_based_connector_config",
                "type": "object",
                "description": "Configurations that are only applicable for query-based ingestion connectors."
              },
              {
                "name": "row_filter",
                "type": "string",
                "description": "(Optional, Immutable) The row filter condition to be applied to the table. It must not contain the WHERE keyword, only the actual filter condition. It must be in DBSQL format."
              },
              {
                "name": "salesforce_include_formula_fields",
                "type": "boolean",
                "description": "If true, formula fields defined in the table are included in the ingestion. This setting is only valid for the Salesforce connector"
              },
              {
                "name": "scd_type",
                "type": "string",
                "description": "The SCD type to use to ingest the table."
              },
              {
                "name": "sequence_by",
                "type": "array",
                "description": "The column names specifying the logical order of events in the source data. Spark Declarative Pipelines uses this sequencing to handle change events that arrive out of order."
              },
              {
                "name": "workday_report_parameters",
                "type": "object",
                "description": "(Optional) Additional custom parameters for Workday Report"
              }
            ]
          }
        ]
      },
      {
        "name": "libraries",
        "type": "array",
        "description": "Libraries or code needed by this deployment.",
        "children": [
          {
            "name": "file",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "path",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "glob",
            "type": "object",
            "description": "The unified field to include source codes. Each entry can be a notebook path, a file path, or a folder path that ends `/**`. This field cannot be used together with `notebook` or `file`.",
            "children": [
              {
                "name": "include",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "jar",
            "type": "string",
            "description": "URI of the jar to be installed. Currently only DBFS is supported."
          },
          {
            "name": "maven",
            "type": "string",
            "description": "Specification of a maven library to be installed."
          },
          {
            "name": "notebook",
            "type": "object",
            "description": "The path to a notebook that defines a pipeline and is stored in the Databricks workspace.",
            "children": [
              {
                "name": "path",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "whl",
            "type": "string",
            "description": "URI of the whl to be installed."
          }
        ]
      },
      {
        "name": "name",
        "type": "string",
        "description": "Friendly identifier for this pipeline."
      },
      {
        "name": "notifications",
        "type": "array",
        "description": "List of notification settings for this pipeline.",
        "children": [
          {
            "name": "alerts",
            "type": "array",
            "description": ""
          },
          {
            "name": "email_recipients",
            "type": "array",
            "description": "A list of email addresses notified when a configured alert is triggered."
          }
        ]
      },
      {
        "name": "photon",
        "type": "boolean",
        "description": "Whether Photon is enabled for this pipeline."
      },
      {
        "name": "restart_window",
        "type": "object",
        "description": "Restart window of this pipeline.",
        "children": [
          {
            "name": "start_hour",
            "type": "integer",
            "description": ""
          },
          {
            "name": "days_of_week",
            "type": "array",
            "description": "Days of week in which the restart is allowed to happen (within a five-hour window starting at start_hour). If not specified all days of the week will be used."
          },
          {
            "name": "time_zone_id",
            "type": "string",
            "description": "Time zone id of restart window. See https://docs.databricks.com/sql/language-manual/sql-ref-syntax-aux-conf-mgmt-set-timezone.html for details. If not specified, UTC will be used."
          }
        ]
      },
      {
        "name": "root_path",
        "type": "string",
        "description": "Root path for this pipeline. This is used as the root directory when editing the pipeline in the Databricks user interface and it is added to sys.path when executing Python sources during pipeline execution."
      },
      {
        "name": "schema",
        "type": "string",
        "description": "The default schema (database) where tables are read from or published to."
      },
      {
        "name": "serverless",
        "type": "boolean",
        "description": "Whether serverless compute is enabled for this pipeline."
      },
      {
        "name": "storage",
        "type": "string",
        "description": "DBFS root directory for storing checkpoints and tables."
      },
      {
        "name": "tags",
        "type": "object",
        "description": "A map of tags associated with the pipeline. These are forwarded to the cluster as cluster tags, and are therefore subject to the same limitations. A maximum of 25 tags can be added to the pipeline."
      },
      {
        "name": "target",
        "type": "string",
        "description": "Target schema (database) to add tables in this pipeline to. Exactly one of `schema` or `target` must be specified. To publish to Unity Catalog, also specify `catalog`. This legacy field is deprecated for pipeline creation in favor of the `schema` field."
      },
      {
        "name": "trigger",
        "type": "object",
        "description": "Which pipeline trigger to use. Deprecated: Use `continuous` instead.",
        "children": [
          {
            "name": "cron",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "quartz_cron_schedule",
                "type": "string",
                "description": ""
              },
              {
                "name": "timezone_id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "manual",
            "type": "object",
            "description": ""
          }
        ]
      },
      {
        "name": "usage_policy_id",
        "type": "string",
        "description": "Usage policy of this pipeline."
      }
    ]
  },
  {
    "name": "state",
    "type": "string",
    "description": "The pipeline state."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The user-friendly name of the pipeline."
  },
  {
    "name": "cluster_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "pipeline_id",
    "type": "string",
    "description": "The unique identifier of the pipeline."
  },
  {
    "name": "creator_user_name",
    "type": "string",
    "description": "The username of the pipeline creator."
  },
  {
    "name": "run_as_user_name",
    "type": "string",
    "description": "The username that the pipeline runs as. This is a read only value derived from the pipeline owner."
  },
  {
    "name": "health",
    "type": "string",
    "description": "The health of a pipeline."
  },
  {
    "name": "latest_updates",
    "type": "array",
    "description": "Status of the latest updates for the pipeline. Ordered with the newest update first.",
    "children": [
      {
        "name": "creation_time",
        "type": "string",
        "description": ""
      },
      {
        "name": "state",
        "type": "string",
        "description": "The update state."
      },
      {
        "name": "update_id",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "state",
    "type": "string",
    "description": "The pipeline state."
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
    <td><a href="#parameter-pipeline_id"><code>pipeline_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a pipeline.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists pipelines defined in the Spark Declarative Pipelines system.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new data processing pipeline based on the requested configuration. If successful, this</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-pipeline_id"><code>pipeline_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates a pipeline with the supplied configuration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-pipeline_id"><code>pipeline_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes a pipeline. If the pipeline publishes to Unity Catalog, pipeline deletion will cascade to all</td>
</tr>
<tr>
    <td><a href="#clone"><CopyableCode code="clone" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-pipeline_id"><code>pipeline_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new pipeline using Unity Catalog from a pipeline using Hive Metastore. This method returns</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-pipeline_id"><code>pipeline_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Stops the pipeline by canceling the active update. If there is no active update for the pipeline, this</td>
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
<tr id="parameter-pipeline_id">
    <td><CopyableCode code="pipeline_id" /></td>
    <td><code>string</code></td>
    <td>:returns: Long-running operation waiter for :class:`GetPipelineResponse`. See :method:wait_get_pipeline_idle for more details.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Select a subset of results based on the specified criteria. The supported filters are: * `notebook='<path>'` to select pipelines that reference the provided notebook path. * `name LIKE '[pattern]'` to select pipelines with a name that matches pattern. Wildcards are supported, for example: `name LIKE '%shopping%'` Composite filters are not supported. This field is optional.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>The maximum number of entries to return in a single page. The system may return fewer than max_results events in a response, even if there are more events available. This field is optional. The default value is 25. The maximum value is 100. An error is returned if the value of max_results is greater than 100.</td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>string</code></td>
    <td>A list of strings specifying the order of results. Supported order_by fields are id and name. The default is id asc. This field is optional.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token returned by previous call</td>
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

Get a pipeline.

```sql
SELECT
name,
cluster_id,
effective_budget_policy_id,
pipeline_id,
creator_user_name,
run_as_user_name,
cause,
health,
last_modified,
latest_updates,
run_as,
spec,
state
FROM databricks_workspace.pipelines.pipelines
WHERE pipeline_id = '{{ pipeline_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists pipelines defined in the Spark Declarative Pipelines system.

```sql
SELECT
name,
cluster_id,
pipeline_id,
creator_user_name,
run_as_user_name,
health,
latest_updates,
state
FROM databricks_workspace.pipelines.pipelines
WHERE deployment_name = '{{ deployment_name }}' -- required
AND filter = '{{ filter }}'
AND max_results = '{{ max_results }}'
AND order_by = '{{ order_by }}'
AND page_token = '{{ page_token }}'
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

Creates a new data processing pipeline based on the requested configuration. If successful, this

```sql
INSERT INTO databricks_workspace.pipelines.pipelines (
data__allow_duplicate_names,
data__budget_policy_id,
data__catalog,
data__channel,
data__clusters,
data__configuration,
data__continuous,
data__deployment,
data__development,
data__dry_run,
data__edition,
data__environment,
data__event_log,
data__filters,
data__gateway_definition,
data__id,
data__ingestion_definition,
data__libraries,
data__name,
data__notifications,
data__photon,
data__restart_window,
data__root_path,
data__run_as,
data__schema,
data__serverless,
data__storage,
data__tags,
data__target,
data__trigger,
data__usage_policy_id,
deployment_name
)
SELECT 
'{{ allow_duplicate_names }}',
'{{ budget_policy_id }}',
'{{ catalog }}',
'{{ channel }}',
'{{ clusters }}',
'{{ configuration }}',
'{{ continuous }}',
'{{ deployment }}',
'{{ development }}',
'{{ dry_run }}',
'{{ edition }}',
'{{ environment }}',
'{{ event_log }}',
'{{ filters }}',
'{{ gateway_definition }}',
'{{ id }}',
'{{ ingestion_definition }}',
'{{ libraries }}',
'{{ name }}',
'{{ notifications }}',
'{{ photon }}',
'{{ restart_window }}',
'{{ root_path }}',
'{{ run_as }}',
'{{ schema }}',
'{{ serverless }}',
'{{ storage }}',
'{{ tags }}',
'{{ target }}',
'{{ trigger }}',
'{{ usage_policy_id }}',
'{{ deployment_name }}'
RETURNING
pipeline_id,
effective_settings
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: pipelines
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the pipelines resource.
    - name: allow_duplicate_names
      value: string
      description: |
        If false, deployment will fail if name conflicts with that of another pipeline.
    - name: budget_policy_id
      value: string
      description: |
        Budget policy of this pipeline.
    - name: catalog
      value: string
      description: |
        A catalog in Unity Catalog to publish data from this pipeline to. If `target` is specified, tables in this pipeline are published to a `target` schema inside `catalog` (for example, `catalog`.`target`.`table`). If `target` is not specified, no data is published to Unity Catalog.
    - name: channel
      value: string
      description: |
        DLT Release Channel that specifies which version to use.
    - name: clusters
      value: string
      description: |
        Cluster settings for this pipeline deployment.
    - name: configuration
      value: string
      description: |
        String-String configuration for this pipeline execution.
    - name: continuous
      value: string
      description: |
        Whether the pipeline is continuous or triggered. This replaces `trigger`.
    - name: deployment
      value: string
      description: |
        Deployment type of this pipeline.
    - name: development
      value: string
      description: |
        Whether the pipeline is in Development mode. Defaults to false.
    - name: dry_run
      value: string
      description: |
        :param edition: str (optional) Pipeline product edition.
    - name: edition
      value: string
    - name: environment
      value: string
      description: |
        Environment specification for this pipeline used to install dependencies.
    - name: event_log
      value: string
      description: |
        Event log configuration for this pipeline
    - name: filters
      value: string
      description: |
        Filters on which Pipeline packages to include in the deployed graph.
    - name: gateway_definition
      value: string
      description: |
        The definition of a gateway pipeline to support change data capture.
    - name: id
      value: string
      description: |
        Unique identifier for this pipeline.
    - name: ingestion_definition
      value: string
      description: |
        The configuration for a managed ingestion pipeline. These settings cannot be used with the 'libraries', 'schema', 'target', or 'catalog' settings.
    - name: libraries
      value: string
      description: |
        Libraries or code needed by this deployment.
    - name: name
      value: string
      description: |
        Friendly identifier for this pipeline.
    - name: notifications
      value: string
      description: |
        List of notification settings for this pipeline.
    - name: photon
      value: string
      description: |
        Whether Photon is enabled for this pipeline.
    - name: restart_window
      value: string
      description: |
        Restart window of this pipeline.
    - name: root_path
      value: string
      description: |
        Root path for this pipeline. This is used as the root directory when editing the pipeline in the Databricks user interface and it is added to sys.path when executing Python sources during pipeline execution.
    - name: run_as
      value: string
      description: |
        :param schema: str (optional) The default schema (database) where tables are read from or published to.
    - name: schema
      value: string
    - name: serverless
      value: string
      description: |
        Whether serverless compute is enabled for this pipeline.
    - name: storage
      value: string
      description: |
        DBFS root directory for storing checkpoints and tables.
    - name: tags
      value: string
      description: |
        A map of tags associated with the pipeline. These are forwarded to the cluster as cluster tags, and are therefore subject to the same limitations. A maximum of 25 tags can be added to the pipeline.
    - name: target
      value: string
      description: |
        Target schema (database) to add tables in this pipeline to. Exactly one of `schema` or `target` must be specified. To publish to Unity Catalog, also specify `catalog`. This legacy field is deprecated for pipeline creation in favor of the `schema` field.
    - name: trigger
      value: string
      description: |
        Which pipeline trigger to use. Deprecated: Use `continuous` instead.
    - name: usage_policy_id
      value: string
      description: |
        Usage policy of this pipeline.
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates a pipeline with the supplied configuration.

```sql
REPLACE databricks_workspace.pipelines.pipelines
SET 
data__allow_duplicate_names = '{{ allow_duplicate_names }}',
data__budget_policy_id = '{{ budget_policy_id }}',
data__catalog = '{{ catalog }}',
data__channel = '{{ channel }}',
data__clusters = '{{ clusters }}',
data__configuration = '{{ configuration }}',
data__continuous = '{{ continuous }}',
data__deployment = '{{ deployment }}',
data__development = '{{ development }}',
data__edition = '{{ edition }}',
data__environment = '{{ environment }}',
data__event_log = '{{ event_log }}',
data__expected_last_modified = '{{ expected_last_modified }}',
data__filters = '{{ filters }}',
data__gateway_definition = '{{ gateway_definition }}',
data__id = '{{ id }}',
data__ingestion_definition = '{{ ingestion_definition }}',
data__libraries = '{{ libraries }}',
data__name = '{{ name }}',
data__notifications = '{{ notifications }}',
data__photon = '{{ photon }}',
data__restart_window = '{{ restart_window }}',
data__root_path = '{{ root_path }}',
data__run_as = '{{ run_as }}',
data__schema = '{{ schema }}',
data__serverless = '{{ serverless }}',
data__storage = '{{ storage }}',
data__tags = '{{ tags }}',
data__target = '{{ target }}',
data__trigger = '{{ trigger }}',
data__usage_policy_id = '{{ usage_policy_id }}'
WHERE 
pipeline_id = '{{ pipeline_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required;
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

Deletes a pipeline. If the pipeline publishes to Unity Catalog, pipeline deletion will cascade to all

```sql
DELETE FROM databricks_workspace.pipelines.pipelines
WHERE pipeline_id = '{{ pipeline_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="clone"
    values={[
        { label: 'clone', value: 'clone' },
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="clone">

Creates a new pipeline using Unity Catalog from a pipeline using Hive Metastore. This method returns

```sql
EXEC databricks_workspace.pipelines.pipelines.clone 
@pipeline_id='{{ pipeline_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"allow_duplicate_names": "{{ allow_duplicate_names }}", 
"budget_policy_id": "{{ budget_policy_id }}", 
"catalog": "{{ catalog }}", 
"channel": "{{ channel }}", 
"clone_mode": "{{ clone_mode }}", 
"clusters": "{{ clusters }}", 
"configuration": "{{ configuration }}", 
"continuous": "{{ continuous }}", 
"deployment": "{{ deployment }}", 
"development": "{{ development }}", 
"edition": "{{ edition }}", 
"environment": "{{ environment }}", 
"event_log": "{{ event_log }}", 
"expected_last_modified": "{{ expected_last_modified }}", 
"filters": "{{ filters }}", 
"gateway_definition": "{{ gateway_definition }}", 
"id": "{{ id }}", 
"ingestion_definition": "{{ ingestion_definition }}", 
"libraries": "{{ libraries }}", 
"name": "{{ name }}", 
"notifications": "{{ notifications }}", 
"photon": "{{ photon }}", 
"restart_window": "{{ restart_window }}", 
"root_path": "{{ root_path }}", 
"schema": "{{ schema }}", 
"serverless": "{{ serverless }}", 
"storage": "{{ storage }}", 
"tags": "{{ tags }}", 
"target": "{{ target }}", 
"trigger": "{{ trigger }}", 
"usage_policy_id": "{{ usage_policy_id }}"
}'
;
```
</TabItem>
<TabItem value="stop">

Stops the pipeline by canceling the active update. If there is no active update for the pipeline, this

```sql
EXEC databricks_workspace.pipelines.pipelines.stop 
@pipeline_id='{{ pipeline_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

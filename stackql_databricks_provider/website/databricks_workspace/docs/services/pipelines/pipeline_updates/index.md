---
title: pipeline_updates
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_updates
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

Creates, updates, deletes, gets or lists a <code>pipeline_updates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pipeline_updates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.pipelines.pipeline_updates" /></td></tr>
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
    "name": "update",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "cause",
        "type": "string",
        "description": "What triggered this update. (API_CALL, INFRASTRUCTURE_MAINTENANCE, JOB_TASK, RETRY_ON_FAILURE, SCHEMA_CHANGE, SERVICE_UPGRADE, USER_ACTION)"
      },
      {
        "name": "cluster_id",
        "type": "string",
        "description": "The ID of the cluster that the update is running on."
      },
      {
        "name": "config",
        "type": "object",
        "description": "The pipeline configuration with system defaults applied where unspecified by the user. Not returned by ListUpdates.",
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
                "description": "Parameters needed in order to automatically scale clusters up and down based on load. Note: autoscaling works best with DB runtime versions 3.0 or later."
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
                "description": "The deployment method that manages the pipeline: - BUNDLE: The pipeline is managed by a<br />Databricks Asset Bundle. (BUNDLE)"
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
                "description": "Optional, Internal. Parameters required to establish an initial connection with the source."
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
                "description": "(Optional) A window that specifies a set of time ranges for snapshot queries in CDC."
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
                "description": "Required. Settings specifying tables to replicate and the destination for the replicated tables."
              },
              {
                "name": "source_configurations",
                "type": "array",
                "description": "Top-level source configurations"
              },
              {
                "name": "source_type",
                "type": "string",
                "description": "The type of the foreign source. The source type will be inferred from the source connection or ingestion gateway. This field is output only and will be ignored if provided. (BIGQUERY, DYNAMICS365, FOREIGN_CATALOG, GA4_RAW_DATA, MANAGED_POSTGRESQL, MYSQL, NETSUITE, ORACLE, POSTGRESQL, SALESFORCE, SERVICENOW, SHAREPOINT, SQLSERVER, TERADATA, WORKDAY_RAAS)"
              },
              {
                "name": "table_configuration",
                "type": "object",
                "description": "Configuration settings to control the ingestion of tables. These settings are applied to all tables in the pipeline."
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
                "description": ""
              },
              {
                "name": "glob",
                "type": "object",
                "description": "The unified field to include source codes. Each entry can be a notebook path, a file path, or a folder path that ends `/**`. This field cannot be used together with `notebook` or `file`."
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
                "description": "The path to a notebook that defines a pipeline and is stored in the Databricks workspace."
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
                "description": ""
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
        "name": "creation_time",
        "type": "integer",
        "description": "The time when this update was created."
      },
      {
        "name": "full_refresh",
        "type": "boolean",
        "description": "If true, this update will reset all tables before running."
      },
      {
        "name": "full_refresh_selection",
        "type": "array",
        "description": "A list of tables to update with fullRefresh. If both refresh_selection and full_refresh_selection are empty, this is a full graph update. Full Refresh on a table means that the states of the table will be reset before the refresh."
      },
      {
        "name": "pipeline_id",
        "type": "string",
        "description": "The ID of the pipeline."
      },
      {
        "name": "refresh_selection",
        "type": "array",
        "description": "A list of tables to update without fullRefresh. If both refresh_selection and full_refresh_selection are empty, this is a full graph update. Full Refresh on a table means that the states of the table will be reset before the refresh."
      },
      {
        "name": "state",
        "type": "string",
        "description": "The update state. (CANCELED, COMPLETED, CREATED, FAILED, INITIALIZING, QUEUED, RESETTING, RUNNING, SETTING_UP_TABLES, STOPPING, WAITING_FOR_RESOURCES)"
      },
      {
        "name": "update_id",
        "type": "string",
        "description": "The ID of this update."
      },
      {
        "name": "validate_only",
        "type": "boolean",
        "description": "If true, this update only validates the correctness of pipeline source code but does not materialize or publish any datasets."
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "next_page_token",
    "type": "string",
    "description": ""
  },
  {
    "name": "prev_page_token",
    "type": "string",
    "description": "If present, then this token can be used in a subsequent request to fetch the previous page."
  },
  {
    "name": "updates",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "cause",
        "type": "string",
        "description": "What triggered this update. (API_CALL, INFRASTRUCTURE_MAINTENANCE, JOB_TASK, RETRY_ON_FAILURE, SCHEMA_CHANGE, SERVICE_UPGRADE, USER_ACTION)"
      },
      {
        "name": "cluster_id",
        "type": "string",
        "description": "The ID of the cluster that the update is running on."
      },
      {
        "name": "config",
        "type": "object",
        "description": "The pipeline configuration with system defaults applied where unspecified by the user. Not returned by ListUpdates.",
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
                "description": "Parameters needed in order to automatically scale clusters up and down based on load. Note: autoscaling works best with DB runtime versions 3.0 or later."
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
                "description": "The deployment method that manages the pipeline: - BUNDLE: The pipeline is managed by a<br />Databricks Asset Bundle. (BUNDLE)"
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
                "description": "Optional, Internal. Parameters required to establish an initial connection with the source."
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
                "description": "(Optional) A window that specifies a set of time ranges for snapshot queries in CDC."
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
                "description": "Required. Settings specifying tables to replicate and the destination for the replicated tables."
              },
              {
                "name": "source_configurations",
                "type": "array",
                "description": "Top-level source configurations"
              },
              {
                "name": "source_type",
                "type": "string",
                "description": "The type of the foreign source. The source type will be inferred from the source connection or ingestion gateway. This field is output only and will be ignored if provided. (BIGQUERY, DYNAMICS365, FOREIGN_CATALOG, GA4_RAW_DATA, MANAGED_POSTGRESQL, MYSQL, NETSUITE, ORACLE, POSTGRESQL, SALESFORCE, SERVICENOW, SHAREPOINT, SQLSERVER, TERADATA, WORKDAY_RAAS)"
              },
              {
                "name": "table_configuration",
                "type": "object",
                "description": "Configuration settings to control the ingestion of tables. These settings are applied to all tables in the pipeline."
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
                "description": ""
              },
              {
                "name": "glob",
                "type": "object",
                "description": "The unified field to include source codes. Each entry can be a notebook path, a file path, or a folder path that ends `/**`. This field cannot be used together with `notebook` or `file`."
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
                "description": "The path to a notebook that defines a pipeline and is stored in the Databricks workspace."
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
                "description": ""
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
        "name": "creation_time",
        "type": "integer",
        "description": "The time when this update was created."
      },
      {
        "name": "full_refresh",
        "type": "boolean",
        "description": "If true, this update will reset all tables before running."
      },
      {
        "name": "full_refresh_selection",
        "type": "array",
        "description": "A list of tables to update with fullRefresh. If both refresh_selection and full_refresh_selection are empty, this is a full graph update. Full Refresh on a table means that the states of the table will be reset before the refresh."
      },
      {
        "name": "pipeline_id",
        "type": "string",
        "description": "The ID of the pipeline."
      },
      {
        "name": "refresh_selection",
        "type": "array",
        "description": "A list of tables to update without fullRefresh. If both refresh_selection and full_refresh_selection are empty, this is a full graph update. Full Refresh on a table means that the states of the table will be reset before the refresh."
      },
      {
        "name": "state",
        "type": "string",
        "description": "The update state. (CANCELED, COMPLETED, CREATED, FAILED, INITIALIZING, QUEUED, RESETTING, RUNNING, SETTING_UP_TABLES, STOPPING, WAITING_FOR_RESOURCES)"
      },
      {
        "name": "update_id",
        "type": "string",
        "description": "The ID of this update."
      },
      {
        "name": "validate_only",
        "type": "boolean",
        "description": "If true, this update only validates the correctness of pipeline source code but does not materialize or publish any datasets."
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
    <td><a href="#parameter-pipeline_id"><code>pipeline_id</code></a>, <a href="#parameter-update_id"><code>update_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets an update from an active pipeline.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pipeline_id"><code>pipeline_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-until_update_id"><code>until_update_id</code></a></td>
    <td>List updates for an active pipeline.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-pipeline_id"><code>pipeline_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Starts a new update for the pipeline. If there is already an active update for the pipeline, the</td>
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
<tr id="parameter-pipeline_id">
    <td><CopyableCode code="pipeline_id" /></td>
    <td><code>string</code></td>
    <td>:param cause: :class:`StartUpdateCause` (optional)</td>
</tr>
<tr id="parameter-update_id">
    <td><CopyableCode code="update_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the update.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
    <td>Max number of entries to return in a single page.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token returned by previous call</td>
</tr>
<tr id="parameter-until_update_id">
    <td><CopyableCode code="until_update_id" /></td>
    <td><code>string</code></td>
    <td>If present, returns updates until and including this update_id.</td>
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

Gets an update from an active pipeline.

```sql
SELECT
update
FROM databricks_workspace.pipelines.pipeline_updates
WHERE pipeline_id = '{{ pipeline_id }}' -- required
AND update_id = '{{ update_id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

List updates for an active pipeline.

```sql
SELECT
next_page_token,
prev_page_token,
updates
FROM databricks_workspace.pipelines.pipeline_updates
WHERE pipeline_id = '{{ pipeline_id }}' -- required
AND workspace = '{{ workspace }}' -- required
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
AND until_update_id = '{{ until_update_id }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' }
    ]}
>
<TabItem value="start">

Starts a new update for the pipeline. If there is already an active update for the pipeline, the

```sql
EXEC databricks_workspace.pipelines.pipeline_updates.start 
@pipeline_id='{{ pipeline_id }}' --required, 
@workspace='{{ workspace }}' --required 
@@json=
'{
"cause": "{{ cause }}", 
"full_refresh": {{ full_refresh }}, 
"full_refresh_selection": "{{ full_refresh_selection }}", 
"refresh_selection": "{{ refresh_selection }}", 
"rewind_spec": "{{ rewind_spec }}", 
"validate_only": {{ validate_only }}
}'
;
```
</TabItem>
</Tabs>

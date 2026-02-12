---
title: job_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - job_runs
  - jobs
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

Creates, updates, deletes, gets or lists a <code>job_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.jobs.job_runs" /></td></tr>
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
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": "The id of the usage policy used by this run for cost attribution purposes."
  },
  {
    "name": "job_id",
    "type": "integer",
    "description": "The canonical identifier of the job that contains this run."
  },
  {
    "name": "job_run_id",
    "type": "integer",
    "description": "ID of the job run that this run belongs to. For legacy and single-task job runs the field is populated with the job run ID. For task runs, the field is populated with the ID of the job run that the task run belongs to."
  },
  {
    "name": "original_attempt_run_id",
    "type": "integer",
    "description": "If this run is a retry of a prior run attempt, this field contains the run_id of the original attempt; otherwise, it is the same as the run_id."
  },
  {
    "name": "run_id",
    "type": "integer",
    "description": "The canonical identifier of the run. This ID is unique across all runs of all jobs."
  },
  {
    "name": "creator_user_name",
    "type": "string",
    "description": "The creator user name. This field won’t be included in the response if the user has already been deleted."
  },
  {
    "name": "run_name",
    "type": "string",
    "description": "An optional name for the run. The maximum length is 4096 bytes in UTF-8 encoding."
  },
  {
    "name": "attempt_number",
    "type": "integer",
    "description": "The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt_number of 0. If the initial run attempt fails, and the job has a retry policy (`max_retries` &gt; 0), subsequent runs are created with an `original_attempt_run_id` of the original attempt’s ID and an incrementing `attempt_number`. Runs are retried only until they succeed, and the maximum `attempt_number` is the same as the `max_retries` value for the job."
  },
  {
    "name": "cleanup_duration",
    "type": "integer",
    "description": "The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `cleanup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
  },
  {
    "name": "cluster_instance",
    "type": "object",
    "description": "The cluster used for this run. If the run is specified to use a new cluster, this field is set once the Jobs service has requested a cluster for the run.",
    "children": [
      {
        "name": "cluster_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "spark_context_id",
        "type": "string",
        "description": "The canonical identifier for the Spark context used by a run. This field is filled in once the run begins execution. This value can be used to view the Spark UI by browsing to `/#setting/sparkui/$cluster_id/$spark_context_id`. The Spark UI continues to be available after the run has completed. The response won’t include this field if the identifier is not available yet."
      }
    ]
  },
  {
    "name": "cluster_spec",
    "type": "object",
    "description": "A snapshot of the job’s cluster specification when this run was created.",
    "children": [
      {
        "name": "existing_cluster_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "job_cluster_key",
        "type": "string",
        "description": "If job_cluster_key, this task is executed reusing the cluster specified in `job.settings.job_clusters`."
      },
      {
        "name": "libraries",
        "type": "string",
        "description": "An optional list of libraries to be installed on the cluster. The default value is an empty list."
      },
      {
        "name": "new_cluster",
        "type": "string",
        "description": "If new_cluster, a description of a new cluster that is created for each run."
      }
    ]
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of the run"
  },
  {
    "name": "effective_performance_target",
    "type": "string",
    "description": "The actual performance target used by the serverless run during execution. This can differ from the client-set performance target on the request depending on whether the performance mode is supported by the job type. * `STANDARD`: Enables cost-efficient execution of serverless workloads. * `PERFORMANCE_OPTIMIZED`: Prioritizes fast startup and execution times through rapid scaling and optimized cluster performance."
  },
  {
    "name": "end_time",
    "type": "integer",
    "description": "The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running."
  },
  {
    "name": "execution_duration",
    "type": "integer",
    "description": "The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `execution_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
  },
  {
    "name": "git_source",
    "type": "object",
    "description": "An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks. If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task. Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.",
    "children": [
      {
        "name": "git_url",
        "type": "string",
        "description": "URL of the repository to be cloned by this job."
      },
      {
        "name": "git_provider",
        "type": "string",
        "description": "Unique identifier of the service used to host the Git repository. The value is case insensitive."
      },
      {
        "name": "git_branch",
        "type": "string",
        "description": "Name of the branch to be checked out and used by this job. This field cannot be specified in conjunction with git_tag or git_commit."
      },
      {
        "name": "git_commit",
        "type": "string",
        "description": "Commit to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_tag."
      },
      {
        "name": "git_snapshot",
        "type": "object",
        "description": "Read-only state of the remote repository at the time the job was run. This field is only<br />    included on job runs.",
        "children": [
          {
            "name": "used_commit",
            "type": "string",
            "description": "Commit that was used to execute the run. If git_branch was specified, this points to the HEAD of the branch at the time of the run; if git_tag was specified, this points to the commit the tag points to."
          }
        ]
      },
      {
        "name": "git_tag",
        "type": "string",
        "description": "Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_commit."
      },
      {
        "name": "job_source",
        "type": "object",
        "description": "The source of the job specification in the remote repository when the job is source controlled.",
        "children": [
          {
            "name": "job_config_path",
            "type": "string",
            "description": "Path of the job YAML file that contains the job specification."
          },
          {
            "name": "import_from_git_branch",
            "type": "string",
            "description": "Name of the branch which the job is imported from."
          },
          {
            "name": "dirty_state",
            "type": "string",
            "description": "Dirty state indicates the job is not fully synced with the job specification in the remote repository. Possible values are: * `NOT_SYNCED`: The job is not yet synced with the remote job specification. Import the remote job specification from UI to make the job fully synced. * `DISCONNECTED`: The job is temporary disconnected from the remote job specification and is allowed for live edit. Import the remote job specification again from UI to make the job fully synced."
          }
        ]
      }
    ]
  },
  {
    "name": "has_more",
    "type": "boolean",
    "description": "Indicates if the run has more array properties (`tasks`, `job_clusters`) that are not shown. They can be accessed via :method:jobs/getrun endpoint. It is only relevant for API 2.2 :method:jobs/listruns requests with `expand_tasks=true`."
  },
  {
    "name": "iterations",
    "type": "array",
    "description": "Only populated by for-each iterations. The parent for-each task is located in tasks array.",
    "children": [
      {
        "name": "task_key",
        "type": "string",
        "description": "A unique name for the task. This field is used to refer to this task from other tasks. This field is required and must be unique within its parent job. On Update or Reset, this field is used to reference the tasks to be updated or reset."
      },
      {
        "name": "attempt_number",
        "type": "integer",
        "description": "The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt_number of 0. If the initial run attempt fails, and the job has a retry policy (`max_retries` &gt; 0), subsequent runs are created with an `original_attempt_run_id` of the original attempt’s ID and an incrementing `attempt_number`. Runs are retried only until they succeed, and the maximum `attempt_number` is the same as the `max_retries` value for the job."
      },
      {
        "name": "clean_rooms_notebook_task",
        "type": "object",
        "description": "The task runs a [clean rooms] notebook when the `clean_rooms_notebook_task` field is present. [clean rooms]: https://docs.databricks.com/clean-rooms/index.html",
        "children": [
          {
            "name": "clean_room_name",
            "type": "string",
            "description": "The clean room that the notebook belongs to."
          },
          {
            "name": "notebook_name",
            "type": "string",
            "description": "Name of the notebook being run."
          },
          {
            "name": "etag",
            "type": "string",
            "description": "Checksum to validate the freshness of the notebook resource (i.e. the notebook being run is the latest version). It can be fetched by calling the :method:cleanroomassets/get API."
          },
          {
            "name": "notebook_base_parameters",
            "type": "object",
            "description": "Base parameters to be used for the clean room notebook job."
          }
        ]
      },
      {
        "name": "cleanup_duration",
        "type": "integer",
        "description": "The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `cleanup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
      },
      {
        "name": "cluster_instance",
        "type": "object",
        "description": "The cluster used for this run. If the run is specified to use a new cluster, this field is set once the Jobs service has requested a cluster for the run.",
        "children": [
          {
            "name": "cluster_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "spark_context_id",
            "type": "string",
            "description": "The canonical identifier for the Spark context used by a run. This field is filled in once the run begins execution. This value can be used to view the Spark UI by browsing to `/#setting/sparkui/$cluster_id/$spark_context_id`. The Spark UI continues to be available after the run has completed. The response won’t include this field if the identifier is not available yet."
          }
        ]
      },
      {
        "name": "compute",
        "type": "object",
        "description": "Task level compute configuration.",
        "children": [
          {
            "name": "hardware_accelerator",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "condition_task",
        "type": "object",
        "description": "The task evaluates a condition that can be used to control the execution of other tasks when the `condition_task` field is present. The condition task does not require a cluster to execute and does not support retries or notifications.",
        "children": [
          {
            "name": "op",
            "type": "string",
            "description": "* `EQUAL_TO`, `NOT_EQUAL` operators perform string comparison of their operands. This means that<br />`“12.0” == “12”` will evaluate to `false`. * `GREATER_THAN`, `GREATER_THAN_OR_EQUAL`,<br />`LESS_THAN`, `LESS_THAN_OR_EQUAL` operators perform numeric comparison of their operands.<br />`“12.0” >= “12”` will evaluate to `true`, `“10.0” >= “12”` will evaluate to<br />`false`.<br /><br />The boolean comparison to task values can be implemented with operators `EQUAL_TO`, `NOT_EQUAL`.<br />If a task value was set to a boolean value, it will be serialized to `“true”` or<br />`“false”` for the comparison."
          },
          {
            "name": "left",
            "type": "string",
            "description": "The left operand of the condition task. Can be either a string value or a job state or parameter reference."
          },
          {
            "name": "right",
            "type": "string",
            "description": "The right operand of the condition task. Can be either a string value or a job state or parameter reference."
          },
          {
            "name": "outcome",
            "type": "string",
            "description": "The condition expression evaluation result. Filled in if the task was successfully completed. Can be `\"true\"` or `\"false\"`"
          }
        ]
      },
      {
        "name": "dashboard_task",
        "type": "object",
        "description": "The task refreshes a dashboard and sends a snapshot to subscribers.",
        "children": [
          {
            "name": "dashboard_id",
            "type": "string",
            "description": "The identifier of the dashboard to refresh."
          },
          {
            "name": "filters",
            "type": "object",
            "description": "Dashboard task parameters. Used to apply dashboard filter values during dashboard task execution. Parameter values get applied to any dashboard filters that have a matching URL identifier as the parameter key. The parameter value format is dependent on the filter type: - For text and single-select filters, provide a single value (e.g. `\"value\"`) - For date and datetime filters, provide the value in ISO 8601 format (e.g. `\"2000-01-01T00:00:00\"`) - For multi-select filters, provide a JSON array of values (e.g. `\"[\\\"value1\\\",\\\"value2\\\"]\"`) - For range and date range filters, provide a JSON object with `start` and `end` (e.g. `\"&#123;\\\"start\\\":\\\"1\\\",\\\"end\\\":\\\"10\\\"&#125;\"`)"
          },
          {
            "name": "subscription",
            "type": "object",
            "description": "Optional: subscription configuration for sending the dashboard snapshot.",
            "children": [
              {
                "name": "custom_subject",
                "type": "string",
                "description": ""
              },
              {
                "name": "paused",
                "type": "boolean",
                "description": "When true, the subscription will not send emails."
              },
              {
                "name": "subscribers",
                "type": "array",
                "description": "The list of subscribers to send the snapshot of the dashboard to."
              }
            ]
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "Optional: The warehouse id to execute the dashboard with for the schedule. If not specified, the default warehouse of the dashboard will be used."
          }
        ]
      },
      {
        "name": "dbt_cloud_task",
        "type": "object",
        "description": "Task type for dbt cloud, deprecated in favor of the new name dbt_platform_task",
        "children": [
          {
            "name": "connection_resource_name",
            "type": "string",
            "description": "The resource name of the UC connection that authenticates the dbt Cloud for this task"
          },
          {
            "name": "dbt_cloud_job_id",
            "type": "integer",
            "description": "Id of the dbt Cloud job to be triggered"
          }
        ]
      },
      {
        "name": "dbt_platform_task",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "connection_resource_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "dbt_platform_job_id",
            "type": "string",
            "description": "Id of the dbt platform job to be triggered. Specified as a string for maximum compatibility with clients."
          }
        ]
      },
      {
        "name": "dbt_task",
        "type": "object",
        "description": "The task runs one or more dbt commands when the `dbt_task` field is present. The dbt task requires both Databricks SQL and the ability to use a serverless or a pro SQL warehouse.",
        "children": [
          {
            "name": "commands",
            "type": "array",
            "description": ""
          },
          {
            "name": "catalog",
            "type": "string",
            "description": "Optional name of the catalog to use. The value is the top level in the 3-level namespace of Unity Catalog (catalog / schema / relation). The catalog value can only be specified if a warehouse_id is specified. Requires dbt-databricks &gt;= 1.1.1."
          },
          {
            "name": "profiles_directory",
            "type": "string",
            "description": "Optional (relative) path to the profiles directory. Can only be specified if no warehouse_id is specified. If no warehouse_id is specified and this folder is unset, the root directory is used."
          },
          {
            "name": "project_directory",
            "type": "string",
            "description": "Path to the project directory. Optional for Git sourced tasks, in which case if no value is provided, the root of the Git repository is used."
          },
          {
            "name": "schema",
            "type": "string",
            "description": "Optional schema to write to. This parameter is only used when a warehouse_id is also provided. If not provided, the `default` schema is used."
          },
          {
            "name": "source",
            "type": "string",
            "description": "Optional location type of the project directory. When set to `WORKSPACE`, the project will be retrieved from the local Databricks workspace. When set to `GIT`, the project will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Project is located in Databricks workspace. * `GIT`: Project is located in cloud Git provider."
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "ID of the SQL warehouse to connect to. If provided, we automatically generate and provide the profile and connection details to dbt. It can be overridden on a per-command basis by using the `--profiles-dir` command line argument."
          }
        ]
      },
      {
        "name": "depends_on",
        "type": "array",
        "description": "An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete successfully before executing this task. The key is `task_key`, and the value is the name assigned to the dependent task.",
        "children": [
          {
            "name": "task_key",
            "type": "string",
            "description": ""
          },
          {
            "name": "outcome",
            "type": "string",
            "description": "Can only be specified on condition task dependencies. The outcome of the dependent task that must be met for this task to run."
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "An optional description for this task."
      },
      {
        "name": "effective_performance_target",
        "type": "string",
        "description": "The actual performance target used by the serverless run during execution. This can differ from the client-set performance target on the request depending on whether the performance mode is supported by the job type. * `STANDARD`: Enables cost-efficient execution of serverless workloads. * `PERFORMANCE_OPTIMIZED`: Prioritizes fast startup and execution times through rapid scaling and optimized cluster performance."
      },
      {
        "name": "email_notifications",
        "type": "object",
        "description": "An optional set of email addresses notified when the task run begins or completes. The default behavior is to not send any emails.",
        "children": [
          {
            "name": "no_alert_for_skipped_runs",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "on_duration_warning_threshold_exceeded",
            "type": "array",
            "description": "A list of email addresses to be notified when the duration of a run exceeds the threshold specified for the `RUN_DURATION_SECONDS` metric in the `health` field. If no rule for the `RUN_DURATION_SECONDS` metric is specified in the `health` field for the job, notifications are not sent."
          },
          {
            "name": "on_failure",
            "type": "array",
            "description": "A list of email addresses to be notified when a run unsuccessfully completes. A run is considered to have completed unsuccessfully if it ends with an `INTERNAL_ERROR` `life_cycle_state` or a `FAILED`, or `TIMED_OUT` result_state. If this is not specified on job creation, reset, or update the list is empty, and notifications are not sent."
          },
          {
            "name": "on_start",
            "type": "array",
            "description": "A list of email addresses to be notified when a run begins. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent."
          },
          {
            "name": "on_streaming_backlog_exceeded",
            "type": "array",
            "description": "A list of email addresses to notify when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the `health` field using the following metrics: `STREAMING_BACKLOG_BYTES`, `STREAMING_BACKLOG_RECORDS`, `STREAMING_BACKLOG_SECONDS`, or `STREAMING_BACKLOG_FILES`. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes."
          },
          {
            "name": "on_success",
            "type": "array",
            "description": "A list of email addresses to be notified when a run successfully completes. A run is considered to have completed successfully if it ends with a `TERMINATED` `life_cycle_state` and a `SUCCESS` result_state. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent."
          }
        ]
      },
      {
        "name": "end_time",
        "type": "integer",
        "description": "The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running."
      },
      {
        "name": "environment_key",
        "type": "string",
        "description": "The key that references an environment spec in a job. This field is required for Python script, Python wheel and dbt tasks when using serverless compute."
      },
      {
        "name": "execution_duration",
        "type": "integer",
        "description": "The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `execution_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
      },
      {
        "name": "existing_cluster_id",
        "type": "string",
        "description": "If existing_cluster_id, the ID of an existing cluster that is used for all runs. When running jobs or tasks on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs and tasks on new clusters for greater reliability"
      },
      {
        "name": "for_each_task",
        "type": "object",
        "description": "The task executes a nested task for every input provided when the `for_each_task` field is present.",
        "children": [
          {
            "name": "inputs",
            "type": "string",
            "description": ""
          },
          {
            "name": "task",
            "type": "object",
            "description": "Configuration for the task that will be run for each element in the array",
            "children": [
              {
                "name": "task_key",
                "type": "string",
                "description": ""
              },
              {
                "name": "clean_rooms_notebook_task",
                "type": "object",
                "description": "The task runs a [clean rooms] notebook when the `clean_rooms_notebook_task` field is present. [clean rooms]: https://docs.databricks.com/clean-rooms/index.html"
              },
              {
                "name": "compute",
                "type": "object",
                "description": "Task level compute configuration."
              },
              {
                "name": "condition_task",
                "type": "object",
                "description": "The task evaluates a condition that can be used to control the execution of other tasks when the `condition_task` field is present. The condition task does not require a cluster to execute and does not support retries or notifications."
              },
              {
                "name": "dashboard_task",
                "type": "object",
                "description": "The task refreshes a dashboard and sends a snapshot to subscribers."
              },
              {
                "name": "dbt_cloud_task",
                "type": "object",
                "description": "Task type for dbt cloud, deprecated in favor of the new name dbt_platform_task"
              },
              {
                "name": "dbt_platform_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "dbt_task",
                "type": "object",
                "description": "The task runs one or more dbt commands when the `dbt_task` field is present. The dbt task requires both Databricks SQL and the ability to use a serverless or a pro SQL warehouse."
              },
              {
                "name": "depends_on",
                "type": "array",
                "description": "An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete before executing this task. The task will run only if the `run_if` condition is true. The key is `task_key`, and the value is the name assigned to the dependent task."
              },
              {
                "name": "description",
                "type": "string",
                "description": "An optional description for this task."
              },
              {
                "name": "disable_auto_optimization",
                "type": "boolean",
                "description": "An option to disable auto optimization in serverless"
              },
              {
                "name": "disabled",
                "type": "boolean",
                "description": "An optional flag to disable the task. If set to true, the task will not run even if it is part of a job."
              },
              {
                "name": "email_notifications",
                "type": "object",
                "description": "An optional set of email addresses that is notified when runs of this task begin or complete as well as when this task is deleted. The default behavior is to not send any emails."
              },
              {
                "name": "environment_key",
                "type": "string",
                "description": "The key that references an environment spec in a job. This field is required for Python script, Python wheel and dbt tasks when using serverless compute."
              },
              {
                "name": "existing_cluster_id",
                "type": "string",
                "description": "If existing_cluster_id, the ID of an existing cluster that is used for all runs. When running jobs or tasks on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs and tasks on new clusters for greater reliability"
              },
              {
                "name": "for_each_task",
                "type": "object",
                "description": "The task executes a nested task for every input provided when the `for_each_task` field is present."
              },
              {
                "name": "gen_ai_compute_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "health",
                "type": "object",
                "description": "An optional set of health rules that can be defined for this job."
              },
              {
                "name": "job_cluster_key",
                "type": "string",
                "description": "If job_cluster_key, this task is executed reusing the cluster specified in `job.settings.job_clusters`."
              },
              {
                "name": "libraries",
                "type": "string",
                "description": "An optional list of libraries to be installed on the cluster. The default value is an empty list."
              },
              {
                "name": "max_retries",
                "type": "integer",
                "description": "An optional maximum number of times to retry an unsuccessful run. A run is considered to be unsuccessful if it completes with the `FAILED` result_state or `INTERNAL_ERROR` `life_cycle_state`. The value `-1` means to retry indefinitely and the value `0` means to never retry."
              },
              {
                "name": "min_retry_interval_millis",
                "type": "integer",
                "description": "An optional minimal interval in milliseconds between the start of the failed run and the subsequent retry run. The default behavior is that unsuccessful runs are immediately retried."
              },
              {
                "name": "new_cluster",
                "type": "string",
                "description": "If new_cluster, a description of a new cluster that is created for each run."
              },
              {
                "name": "notebook_task",
                "type": "object",
                "description": "The task runs a notebook when the `notebook_task` field is present."
              },
              {
                "name": "notification_settings",
                "type": "object",
                "description": "Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this task."
              },
              {
                "name": "pipeline_task",
                "type": "object",
                "description": "The task triggers a pipeline update when the `pipeline_task` field is present. Only pipelines configured to use triggered more are supported."
              },
              {
                "name": "power_bi_task",
                "type": "object",
                "description": "The task triggers a Power BI semantic model update when the `power_bi_task` field is present."
              },
              {
                "name": "python_wheel_task",
                "type": "object",
                "description": "The task runs a Python wheel when the `python_wheel_task` field is present."
              },
              {
                "name": "retry_on_timeout",
                "type": "boolean",
                "description": "An optional policy to specify whether to retry a job when it times out. The default behavior is to not retry on timeout."
              },
              {
                "name": "run_if",
                "type": "string",
                "description": "An optional value specifying the condition determining whether the task is run once its dependencies have been completed. * `ALL_SUCCESS`: All dependencies have executed and succeeded * `AT_LEAST_ONE_SUCCESS`: At least one dependency has succeeded * `NONE_FAILED`: None of the dependencies have failed and at least one was executed * `ALL_DONE`: All dependencies have been completed * `AT_LEAST_ONE_FAILED`: At least one dependency failed * `ALL_FAILED`: ALl dependencies have failed"
              },
              {
                "name": "run_job_task",
                "type": "object",
                "description": "The task triggers another job when the `run_job_task` field is present."
              },
              {
                "name": "spark_jar_task",
                "type": "object",
                "description": "The task runs a JAR when the `spark_jar_task` field is present."
              },
              {
                "name": "spark_python_task",
                "type": "object",
                "description": "The task runs a Python file when the `spark_python_task` field is present."
              },
              {
                "name": "spark_submit_task",
                "type": "object",
                "description": "(Legacy) The task runs the spark-submit script when the spark_submit_task field is present. Databricks recommends using the spark_jar_task instead; see [Spark Submit task for jobs](/jobs/spark-submit)."
              },
              {
                "name": "sql_task",
                "type": "object",
                "description": "The task runs a SQL query or file, or it refreshes a SQL alert or a legacy SQL dashboard when the `sql_task` field is present."
              },
              {
                "name": "timeout_seconds",
                "type": "integer",
                "description": "An optional timeout applied to each run of this job task. A value of `0` means no timeout."
              },
              {
                "name": "webhook_notifications",
                "type": "object",
                "description": "A collection of system notification IDs to notify when runs of this task begin or complete. The default behavior is to not send any system notifications."
              }
            ]
          },
          {
            "name": "concurrency",
            "type": "integer",
            "description": "An optional maximum allowed number of concurrent runs of the task. Set this value if you want to be able to execute multiple runs of the task concurrently."
          },
          {
            "name": "stats",
            "type": "object",
            "description": "Read only field. Populated for GetRun and ListRuns RPC calls and stores the execution stats of an For each task",
            "children": [
              {
                "name": "error_message_stats",
                "type": "array",
                "description": ""
              },
              {
                "name": "task_run_stats",
                "type": "object",
                "description": "Describes stats of the iteration. Only latest retries are considered."
              }
            ]
          }
        ]
      },
      {
        "name": "gen_ai_compute_task",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "dl_runtime_image",
            "type": "string",
            "description": ""
          },
          {
            "name": "command",
            "type": "string",
            "description": "Command launcher to run the actual script, e.g. bash, python etc."
          },
          {
            "name": "compute",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "num_gpus",
                "type": "integer",
                "description": ""
              },
              {
                "name": "gpu_node_pool_id",
                "type": "string",
                "description": "IDof the GPU pool to use."
              },
              {
                "name": "gpu_type",
                "type": "string",
                "description": "GPU type."
              }
            ]
          },
          {
            "name": "mlflow_experiment_name",
            "type": "string",
            "description": "Optional string containing the name of the MLflow experiment to log the run to. If name is not found, backend will create the mlflow experiment using the name."
          },
          {
            "name": "source",
            "type": "string",
            "description": "Optional location type of the training script. When set to `WORKSPACE`, the script will be retrieved from the local Databricks workspace. When set to `GIT`, the script will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Script is located in Databricks workspace. * `GIT`: Script is located in cloud Git provider."
          },
          {
            "name": "training_script_path",
            "type": "string",
            "description": "The training script file path to be executed. Cloud file URIs (such as dbfs:/, s3:/, adls:/, gcs:/) and workspace paths are supported. For python files stored in the Databricks workspace, the path must be absolute and begin with `/`. For files stored in a remote repository, the path must be relative. This field is required."
          },
          {
            "name": "yaml_parameters",
            "type": "string",
            "description": "Optional string containing model parameters passed to the training script in yaml format. If present, then the content in yaml_parameters_file_path will be ignored."
          },
          {
            "name": "yaml_parameters_file_path",
            "type": "string",
            "description": "Optional path to a YAML file containing model parameters passed to the training script."
          }
        ]
      },
      {
        "name": "git_source",
        "type": "object",
        "description": "An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks. If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task. Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.",
        "children": [
          {
            "name": "git_url",
            "type": "string",
            "description": "URL of the repository to be cloned by this job."
          },
          {
            "name": "git_provider",
            "type": "string",
            "description": "Unique identifier of the service used to host the Git repository. The value is case insensitive."
          },
          {
            "name": "git_branch",
            "type": "string",
            "description": "Name of the branch to be checked out and used by this job. This field cannot be specified in conjunction with git_tag or git_commit."
          },
          {
            "name": "git_commit",
            "type": "string",
            "description": "Commit to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_tag."
          },
          {
            "name": "git_snapshot",
            "type": "object",
            "description": "Read-only state of the remote repository at the time the job was run. This field is only<br />    included on job runs.",
            "children": [
              {
                "name": "used_commit",
                "type": "string",
                "description": "Commit that was used to execute the run. If git_branch was specified, this points to the HEAD of the branch at the time of the run; if git_tag was specified, this points to the commit the tag points to."
              }
            ]
          },
          {
            "name": "git_tag",
            "type": "string",
            "description": "Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_commit."
          },
          {
            "name": "job_source",
            "type": "object",
            "description": "The source of the job specification in the remote repository when the job is source controlled.",
            "children": [
              {
                "name": "job_config_path",
                "type": "string",
                "description": "Path of the job YAML file that contains the job specification."
              },
              {
                "name": "import_from_git_branch",
                "type": "string",
                "description": "Name of the branch which the job is imported from."
              },
              {
                "name": "dirty_state",
                "type": "string",
                "description": "Dirty state indicates the job is not fully synced with the job specification in the remote repository. Possible values are: * `NOT_SYNCED`: The job is not yet synced with the remote job specification. Import the remote job specification from UI to make the job fully synced. * `DISCONNECTED`: The job is temporary disconnected from the remote job specification and is allowed for live edit. Import the remote job specification again from UI to make the job fully synced."
              }
            ]
          }
        ]
      },
      {
        "name": "job_cluster_key",
        "type": "string",
        "description": "If job_cluster_key, this task is executed reusing the cluster specified in `job.settings.job_clusters`."
      },
      {
        "name": "libraries",
        "type": "string",
        "description": "An optional list of libraries to be installed on the cluster. The default value is an empty list."
      },
      {
        "name": "new_cluster",
        "type": "string",
        "description": "If new_cluster, a description of a new cluster that is created for each run."
      },
      {
        "name": "notebook_task",
        "type": "object",
        "description": "The task runs a notebook when the `notebook_task` field is present.",
        "children": [
          {
            "name": "notebook_path",
            "type": "string",
            "description": ""
          },
          {
            "name": "base_parameters",
            "type": "object",
            "description": "Base parameters to be used for each run of this job. If the run is initiated by a call to :method:jobs/run Now with parameters specified, the two parameters maps are merged. If the same key is specified in `base_parameters` and in `run-now`, the value from `run-now` is used. Use [Task parameter variables] to set parameters containing information about job runs. If the notebook takes a parameter that is not specified in the job’s `base_parameters` or the `run-now` override parameters, the default value from the notebook is used. Retrieve these parameters in a notebook using [dbutils.widgets.get]. The JSON representation of this field cannot exceed 1MB. [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-widgets"
          },
          {
            "name": "source",
            "type": "string",
            "description": "Optional location type of the notebook. When set to `WORKSPACE`, the notebook will be retrieved from the local Databricks workspace. When set to `GIT`, the notebook will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Notebook is located in Databricks workspace. * `GIT`: Notebook is located in cloud Git provider."
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "Optional `warehouse_id` to run the notebook on a SQL warehouse. Classic SQL warehouses are NOT supported, please use serverless or pro SQL warehouses. Note that SQL warehouses only support SQL cells; if the notebook contains non-SQL cells, the run will fail."
          }
        ]
      },
      {
        "name": "notification_settings",
        "type": "object",
        "description": "Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this task run.",
        "children": [
          {
            "name": "alert_on_last_attempt",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "no_alert_for_canceled_runs",
            "type": "boolean",
            "description": "If true, do not send notifications to recipients specified in `on_failure` if the run is canceled."
          },
          {
            "name": "no_alert_for_skipped_runs",
            "type": "boolean",
            "description": "If true, do not send notifications to recipients specified in `on_failure` if the run is skipped."
          }
        ]
      },
      {
        "name": "pipeline_task",
        "type": "object",
        "description": "The task triggers a pipeline update when the `pipeline_task` field is present. Only pipelines configured to use triggered more are supported.",
        "children": [
          {
            "name": "pipeline_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "full_refresh",
            "type": "boolean",
            "description": "If true, triggers a full refresh on the delta live table."
          }
        ]
      },
      {
        "name": "power_bi_task",
        "type": "object",
        "description": "The task triggers a Power BI semantic model update when the `power_bi_task` field is present.",
        "children": [
          {
            "name": "connection_resource_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "power_bi_model",
            "type": "object",
            "description": "The semantic model to update",
            "children": [
              {
                "name": "authentication_method",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              },
              {
                "name": "model_name",
                "type": "string",
                "description": "The name of the Power BI model"
              },
              {
                "name": "overwrite_existing",
                "type": "boolean",
                "description": "Whether to overwrite existing Power BI models"
              },
              {
                "name": "storage_mode",
                "type": "string",
                "description": "The default storage mode of the Power BI model"
              },
              {
                "name": "workspace_name",
                "type": "string",
                "description": "The name of the Power BI workspace of the model"
              }
            ]
          },
          {
            "name": "refresh_after_update",
            "type": "boolean",
            "description": "Whether the model should be refreshed after the update"
          },
          {
            "name": "tables",
            "type": "array",
            "description": "The tables to be exported to Power BI",
            "children": [
              {
                "name": "catalog",
                "type": "string",
                "description": ""
              },
              {
                "name": "name",
                "type": "string",
                "description": "The table name in Databricks"
              },
              {
                "name": "schema",
                "type": "string",
                "description": "The schema name in Databricks"
              },
              {
                "name": "storage_mode",
                "type": "string",
                "description": "The Power BI storage mode of the table"
              }
            ]
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "The SQL warehouse ID to use as the Power BI data source"
          }
        ]
      },
      {
        "name": "python_wheel_task",
        "type": "object",
        "description": "The task runs a Python wheel when the `python_wheel_task` field is present.",
        "children": [
          {
            "name": "package_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "entry_point",
            "type": "string",
            "description": "Named entry point to use, if it does not exist in the metadata of the package it executes the function from the package directly using `$packageName.$entryPoint()`"
          },
          {
            "name": "named_parameters",
            "type": "object",
            "description": "Command-line parameters passed to Python wheel task in the form of `[\"--name=task\", \"--data=dbfs:/path/to/data.json\"]`. Leave it empty if `parameters` is not null."
          },
          {
            "name": "parameters",
            "type": "array",
            "description": "Command-line parameters passed to Python wheel task. Leave it empty if `named_parameters` is not null."
          }
        ]
      },
      {
        "name": "queue_duration",
        "type": "integer",
        "description": "The time in milliseconds that the run has spent in the queue."
      },
      {
        "name": "resolved_values",
        "type": "object",
        "description": "Parameter values including resolved references",
        "children": [
          {
            "name": "condition_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "left",
                "type": "string",
                "description": ""
              },
              {
                "name": "right",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "dbt_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "commands",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "notebook_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "base_parameters",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "python_wheel_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "named_parameters",
                "type": "object",
                "description": ""
              },
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "run_job_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "job_parameters",
                "type": "object",
                "description": ""
              },
              {
                "name": "parameters",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "simulation_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "spark_jar_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "spark_python_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "spark_submit_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "sql_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "object",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "run_duration",
        "type": "integer",
        "description": "The time in milliseconds it took the job run and all of its repairs to finish."
      },
      {
        "name": "run_id",
        "type": "integer",
        "description": "The ID of the task run."
      },
      {
        "name": "run_if",
        "type": "string",
        "description": "An optional value indicating the condition that determines whether the task should be run once its dependencies have been completed. When omitted, defaults to `ALL_SUCCESS`. See :method:jobs/create for a list of possible values."
      },
      {
        "name": "run_job_task",
        "type": "object",
        "description": "The task triggers another job when the `run_job_task` field is present.",
        "children": [
          {
            "name": "job_id",
            "type": "integer",
            "description": ""
          },
          {
            "name": "dbt_commands",
            "type": "array",
            "description": "An array of commands to execute for jobs with the dbt task, for example `\"dbt_commands\": [\"dbt deps\", \"dbt seed\", \"dbt deps\", \"dbt seed\", \"dbt run\"]` ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "jar_params",
            "type": "array",
            "description": "A list of parameters for jobs with Spark JAR tasks, for example `\"jar_params\": [\"john doe\", \"35\"]`. The parameters are used to invoke the main function of the main class specified in the Spark JAR task. If not specified upon `run-now`, it defaults to an empty list. jar_params cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example `&#123;\"jar_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "job_parameters",
            "type": "object",
            "description": "Job-level parameters used to trigger the job."
          },
          {
            "name": "notebook_params",
            "type": "object",
            "description": "A map from keys to values for jobs with notebook task, for example `\"notebook_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;`. The map is passed to the notebook and is accessible through the [dbutils.widgets.get] function. If not specified upon `run-now`, the triggered run uses the job’s base parameters. notebook_params cannot be specified in conjunction with jar_params. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. The JSON representation of this field (for example `&#123;\"notebook_params\":&#123;\"name\":\"john doe\",\"age\":\"35\"&#125;&#125;`) cannot exceed 10,000 bytes. [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "pipeline_params",
            "type": "object",
            "description": "Controls whether the pipeline should perform a full refresh",
            "children": [
              {
                "name": "full_refresh",
                "type": "boolean",
                "description": ""
              }
            ]
          },
          {
            "name": "python_named_params",
            "type": "object",
            "description": ""
          },
          {
            "name": "python_params",
            "type": "array",
            "description": "A list of parameters for jobs with Python tasks, for example `\"python_params\": [\"john doe\", \"35\"]`. The parameters are passed to Python file as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `&#123;\"python_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "spark_submit_params",
            "type": "array",
            "description": "A list of parameters for jobs with spark submit task, for example `\"spark_submit_params\": [\"--class\", \"org.apache.spark.examples.SparkPi\"]`. The parameters are passed to spark-submit script as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `&#123;\"python_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "sql_params",
            "type": "object",
            "description": "A map from keys to values for jobs with SQL task, for example `\"sql_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;`. The SQL alert task does not support custom parameters. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          }
        ]
      },
      {
        "name": "run_page_url",
        "type": "string",
        "description": ""
      },
      {
        "name": "setup_duration",
        "type": "integer",
        "description": "The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `setup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
      },
      {
        "name": "spark_jar_task",
        "type": "object",
        "description": "The task runs a JAR when the `spark_jar_task` field is present.",
        "children": [
          {
            "name": "jar_uri",
            "type": "string",
            "description": ""
          },
          {
            "name": "main_class_name",
            "type": "string",
            "description": "The full name of the class containing the main method to be executed. This class must be contained in a JAR provided as a library. The code must use `SparkContext.getOrCreate` to obtain a Spark context; otherwise, runs of the job fail."
          },
          {
            "name": "parameters",
            "type": "array",
            "description": "Parameters passed to the main method. Use [Task parameter variables] to set parameters containing information about job runs. [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables"
          },
          {
            "name": "run_as_repl",
            "type": "boolean",
            "description": "Deprecated. A value of `false` is no longer supported."
          }
        ]
      },
      {
        "name": "spark_python_task",
        "type": "object",
        "description": "The task runs a Python file when the `spark_python_task` field is present.",
        "children": [
          {
            "name": "python_file",
            "type": "string",
            "description": ""
          },
          {
            "name": "parameters",
            "type": "array",
            "description": "Command line parameters passed to the Python file. Use [Task parameter variables] to set parameters containing information about job runs. [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables"
          },
          {
            "name": "source",
            "type": "string",
            "description": "Optional location type of the Python file. When set to `WORKSPACE` or not specified, the file will be retrieved from the local Databricks workspace or cloud location (if the `python_file` has a URI format). When set to `GIT`, the Python file will be retrieved from a Git repository defined in `git_source`. * `WORKSPACE`: The Python file is located in a Databricks workspace or at a cloud filesystem URI. * `GIT`: The Python file is located in a remote Git repository."
          }
        ]
      },
      {
        "name": "spark_submit_task",
        "type": "object",
        "description": "(Legacy) The task runs the spark-submit script when the spark_submit_task field is present. Databricks recommends using the spark_jar_task instead; see [Spark Submit task for jobs](/jobs/spark-submit).",
        "children": [
          {
            "name": "parameters",
            "type": "array",
            "description": ""
          }
        ]
      },
      {
        "name": "sql_task",
        "type": "object",
        "description": "The task runs a SQL query or file, or it refreshes a SQL alert or a legacy SQL dashboard when the `sql_task` field is present.",
        "children": [
          {
            "name": "warehouse_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "alert",
            "type": "object",
            "description": "If alert, indicates that this job must refresh a SQL alert.",
            "children": [
              {
                "name": "alert_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "pause_subscriptions",
                "type": "boolean",
                "description": "If true, the alert notifications are not sent to subscribers."
              },
              {
                "name": "subscriptions",
                "type": "array",
                "description": "If specified, alert notifications are sent to subscribers."
              }
            ]
          },
          {
            "name": "dashboard",
            "type": "object",
            "description": "If dashboard, indicates that this job must refresh a SQL dashboard.",
            "children": [
              {
                "name": "dashboard_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "custom_subject",
                "type": "string",
                "description": "Subject of the email sent to subscribers of this task."
              },
              {
                "name": "pause_subscriptions",
                "type": "boolean",
                "description": "If true, the dashboard snapshot is not taken, and emails are not sent to subscribers."
              },
              {
                "name": "subscriptions",
                "type": "array",
                "description": "If specified, dashboard snapshots are sent to subscriptions."
              }
            ]
          },
          {
            "name": "file",
            "type": "object",
            "description": "If file, indicates that this job runs a SQL file in a remote Git repository.",
            "children": [
              {
                "name": "path",
                "type": "string",
                "description": ""
              },
              {
                "name": "source",
                "type": "string",
                "description": "Optional location type of the SQL file. When set to `WORKSPACE`, the SQL file will be retrieved from the local Databricks workspace. When set to `GIT`, the SQL file will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: SQL file is located in Databricks workspace. * `GIT`: SQL file is located in cloud Git provider."
              }
            ]
          },
          {
            "name": "parameters",
            "type": "object",
            "description": "Parameters to be used for each run of this job. The SQL alert task does not support custom parameters."
          },
          {
            "name": "query",
            "type": "object",
            "description": "If query, indicates that this job must execute a SQL query.",
            "children": [
              {
                "name": "query_id",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "start_time",
        "type": "integer",
        "description": "The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued."
      },
      {
        "name": "state",
        "type": "object",
        "description": "Deprecated. Please use the `status` field instead.",
        "children": [
          {
            "name": "life_cycle_state",
            "type": "string",
            "description": "A value indicating the run's current lifecycle state. This field is always available in the response. Note: Additional states might be introduced in future releases."
          },
          {
            "name": "queue_reason",
            "type": "string",
            "description": "The reason indicating why the run was queued."
          },
          {
            "name": "result_state",
            "type": "string",
            "description": "A value indicating the run's result. This field is only available for terminal lifecycle states. Note: Additional states might be introduced in future releases."
          },
          {
            "name": "state_message",
            "type": "string",
            "description": "A descriptive message for the current state. This field is unstructured, and its exact format is subject to change."
          },
          {
            "name": "user_cancelled_or_timedout",
            "type": "boolean",
            "description": "A value indicating whether a run was canceled manually by a user or by the scheduler because the run timed out."
          }
        ]
      },
      {
        "name": "status",
        "type": "object",
        "description": "The current status of the run",
        "children": [
          {
            "name": "queue_details",
            "type": "object",
            "description": "If the run was queued, details about the reason for queuing the run.",
            "children": [
              {
                "name": "code",
                "type": "string",
                "description": "The reason for queuing the run. * `ACTIVE_RUNS_LIMIT_REACHED`: The run was queued due to<br />reaching the workspace limit of active task runs. * `MAX_CONCURRENT_RUNS_REACHED`: The run was<br />queued due to reaching the per-job limit of concurrent job runs. *<br />`ACTIVE_RUN_JOB_TASKS_LIMIT_REACHED`: The run was queued due to reaching the workspace limit of<br />active run job tasks."
              },
              {
                "name": "message",
                "type": "string",
                "description": "A descriptive message with the queuing details. This field is unstructured, and its exact format is subject to change."
              }
            ]
          },
          {
            "name": "state",
            "type": "string",
            "description": "The current state of the run."
          },
          {
            "name": "termination_details",
            "type": "object",
            "description": "If the run is in a TERMINATING or TERMINATED state, details about the reason for terminating the run.",
            "children": [
              {
                "name": "code",
                "type": "string",
                "description": "The code indicates why the run was terminated. Additional codes might be introduced in future<br />releases. * `SUCCESS`: The run was completed successfully. * `SUCCESS_WITH_FAILURES`: The run<br />was completed successfully but some child runs failed. * `USER_CANCELED`: The run was<br />successfully canceled during execution by a user. * `CANCELED`: The run was canceled during<br />execution by the Databricks platform; for example, if the maximum run duration was exceeded. *<br />`SKIPPED`: Run was never executed, for example, if the upstream task run failed, the dependency<br />type condition was not met, or there were no material tasks to execute. * `INTERNAL_ERROR`: The<br />run encountered an unexpected error. Refer to the state message for further details. *<br />`DRIVER_ERROR`: The run encountered an error while communicating with the Spark Driver. *<br />`CLUSTER_ERROR`: The run failed due to a cluster error. Refer to the state message for further<br />details. * `REPOSITORY_CHECKOUT_FAILED`: Failed to complete the checkout due to an error when<br />communicating with the third party service. * `INVALID_CLUSTER_REQUEST`: The run failed because<br />it issued an invalid request to start the cluster. * `WORKSPACE_RUN_LIMIT_EXCEEDED`: The<br />workspace has reached the quota for the maximum number of concurrent active runs. Consider<br />scheduling the runs over a larger time frame. * `FEATURE_DISABLED`: The run failed because it<br />tried to access a feature unavailable for the workspace. * `CLUSTER_REQUEST_LIMIT_EXCEEDED`: The<br />number of cluster creation, start, and upsize requests have exceeded the allotted rate limit.<br />Consider spreading the run execution over a larger time frame. * `STORAGE_ACCESS_ERROR`: The run<br />failed due to an error when accessing the customer blob storage. Refer to the state message for<br />further details. * `RUN_EXECUTION_ERROR`: The run was completed with task failures. For more<br />details, refer to the state message or run output. * `UNAUTHORIZED_ERROR`: The run failed due to<br />a permission issue while accessing a resource. Refer to the state message for further details. *<br />`LIBRARY_INSTALLATION_ERROR`: The run failed while installing the user-requested library. Refer<br />to the state message for further details. The causes might include, but are not limited to: The<br />provided library is invalid, there are insufficient permissions to install the library, and so<br />forth. * `MAX_CONCURRENT_RUNS_EXCEEDED`: The scheduled run exceeds the limit of maximum<br />concurrent runs set for the job. * `MAX_SPARK_CONTEXTS_EXCEEDED`: The run is scheduled on a<br />cluster that has already reached the maximum number of contexts it is configured to create. See:<br />[Link]. * `RESOURCE_NOT_FOUND`: A resource necessary for run execution does not exist. Refer to<br />the state message for further details. * `INVALID_RUN_CONFIGURATION`: The run failed due to an<br />invalid configuration. Refer to the state message for further details. * `CLOUD_FAILURE`: The<br />run failed due to a cloud provider issue. Refer to the state message for further details. *<br />`MAX_JOB_QUEUE_SIZE_EXCEEDED`: The run was skipped due to reaching the job level queue size<br />limit. * `DISABLED`: The run was never executed because it was disabled explicitly by the user.<br />* `BREAKING_CHANGE`: Run failed because of an intentional breaking change in Spark, but it will<br />be retried with a mitigation config.<br /><br />[Link]: https://kb.databricks.com/en_US/notebooks/too-many-execution-contexts-are-open-right-now"
              },
              {
                "name": "message",
                "type": "string",
                "description": "A descriptive message with the termination details. This field is unstructured and the format might change."
              },
              {
                "name": "type",
                "type": "string",
                "description": "* `SUCCESS`: The run terminated without any issues * `INTERNAL_ERROR`: An error occurred in the<br />Databricks platform. Please look at the [status page] or contact support if the issue persists.<br />* `CLIENT_ERROR`: The run was terminated because of an error caused by user input or the job<br />configuration. * `CLOUD_FAILURE`: The run was terminated because of an issue with your cloud<br />provider.<br /><br />[status page]: https://status.databricks.com/"
              }
            ]
          }
        ]
      },
      {
        "name": "timeout_seconds",
        "type": "integer",
        "description": "An optional timeout applied to each run of this job task. A value of `0` means no timeout."
      },
      {
        "name": "webhook_notifications",
        "type": "object",
        "description": "A collection of system notification IDs to notify when the run begins or completes. The default behavior is to not send any system notifications. Task webhooks respect the task notification settings.",
        "children": [
          {
            "name": "on_duration_warning_threshold_exceeded",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_failure",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the `on_failure` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_start",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the `on_start` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_streaming_backlog_exceeded",
            "type": "array",
            "description": "An optional list of system notification IDs to call when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the `health` field using the following metrics: `STREAMING_BACKLOG_BYTES`, `STREAMING_BACKLOG_RECORDS`, `STREAMING_BACKLOG_SECONDS`, or `STREAMING_BACKLOG_FILES`. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes. A maximum of 3 destinations can be specified for the `on_streaming_backlog_exceeded` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_success",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the `on_success` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "job_clusters",
    "type": "array",
    "description": "A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings. If more than 100 job clusters are available, you can paginate through them using :method:jobs/getrun.",
    "children": [
      {
        "name": "job_cluster_key",
        "type": "string",
        "description": ""
      },
      {
        "name": "new_cluster",
        "type": "string",
        "description": "If new_cluster, a description of a cluster that is created for each task."
      }
    ]
  },
  {
    "name": "job_parameters",
    "type": "array",
    "description": "Job-level parameters used in the run",
    "children": [
      {
        "name": "default",
        "type": "string",
        "description": ""
      },
      {
        "name": "name",
        "type": "string",
        "description": "The name of the parameter"
      },
      {
        "name": "value",
        "type": "string",
        "description": "The value used in the run"
      }
    ]
  },
  {
    "name": "next_page_token",
    "type": "string",
    "description": "A token that can be used to list the next page of array properties."
  },
  {
    "name": "number_in_job",
    "type": "integer",
    "description": "A unique identifier for this job run. This is set to the same value as `run_id`."
  },
  {
    "name": "overriding_parameters",
    "type": "object",
    "description": "The parameters used for this run.",
    "children": [
      {
        "name": "dbt_commands",
        "type": "array",
        "description": ""
      },
      {
        "name": "jar_params",
        "type": "array",
        "description": "A list of parameters for jobs with Spark JAR tasks, for example `\"jar_params\": [\"john doe\", \"35\"]`. The parameters are used to invoke the main function of the main class specified in the Spark JAR task. If not specified upon `run-now`, it defaults to an empty list. jar_params cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example `&#123;\"jar_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
      },
      {
        "name": "notebook_params",
        "type": "object",
        "description": "A map from keys to values for jobs with notebook task, for example `\"notebook_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;`. The map is passed to the notebook and is accessible through the [dbutils.widgets.get] function. If not specified upon `run-now`, the triggered run uses the job’s base parameters. notebook_params cannot be specified in conjunction with jar_params. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. The JSON representation of this field (for example `&#123;\"notebook_params\":&#123;\"name\":\"john doe\",\"age\":\"35\"&#125;&#125;`) cannot exceed 10,000 bytes. [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
      },
      {
        "name": "pipeline_params",
        "type": "object",
        "description": "Controls whether the pipeline should perform a full refresh",
        "children": [
          {
            "name": "full_refresh",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "python_named_params",
        "type": "object",
        "description": ""
      },
      {
        "name": "python_params",
        "type": "array",
        "description": "A list of parameters for jobs with Python tasks, for example `\"python_params\": [\"john doe\", \"35\"]`. The parameters are passed to Python file as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `&#123;\"python_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
      },
      {
        "name": "spark_submit_params",
        "type": "array",
        "description": "A list of parameters for jobs with spark submit task, for example `\"spark_submit_params\": [\"--class\", \"org.apache.spark.examples.SparkPi\"]`. The parameters are passed to spark-submit script as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `&#123;\"python_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
      },
      {
        "name": "sql_params",
        "type": "object",
        "description": "A map from keys to values for jobs with SQL task, for example `\"sql_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;`. The SQL alert task does not support custom parameters. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
      }
    ]
  },
  {
    "name": "queue_duration",
    "type": "integer",
    "description": "The time in milliseconds that the run has spent in the queue."
  },
  {
    "name": "repair_history",
    "type": "array",
    "description": "The repair history of the run.",
    "children": [
      {
        "name": "effective_performance_target",
        "type": "string",
        "description": "PerformanceTarget defines how performant (lower latency) or cost efficient the execution of run<br />on serverless compute should be. The performance mode on the job or pipeline should map to a<br />performance setting that is passed to Cluster Manager (see cluster-common PerformanceTarget)."
      },
      {
        "name": "end_time",
        "type": "integer",
        "description": "The end time of the (repaired) run."
      },
      {
        "name": "id",
        "type": "integer",
        "description": "The ID of the repair. Only returned for the items that represent a repair in `repair_history`."
      },
      {
        "name": "start_time",
        "type": "integer",
        "description": "The start time of the (repaired) run."
      },
      {
        "name": "state",
        "type": "object",
        "description": "Deprecated. Please use the `status` field instead.",
        "children": [
          {
            "name": "life_cycle_state",
            "type": "string",
            "description": "A value indicating the run's current lifecycle state. This field is always available in the response. Note: Additional states might be introduced in future releases."
          },
          {
            "name": "queue_reason",
            "type": "string",
            "description": "The reason indicating why the run was queued."
          },
          {
            "name": "result_state",
            "type": "string",
            "description": "A value indicating the run's result. This field is only available for terminal lifecycle states. Note: Additional states might be introduced in future releases."
          },
          {
            "name": "state_message",
            "type": "string",
            "description": "A descriptive message for the current state. This field is unstructured, and its exact format is subject to change."
          },
          {
            "name": "user_cancelled_or_timedout",
            "type": "boolean",
            "description": "A value indicating whether a run was canceled manually by a user or by the scheduler because the run timed out."
          }
        ]
      },
      {
        "name": "status",
        "type": "object",
        "description": "The current status of the run",
        "children": [
          {
            "name": "queue_details",
            "type": "object",
            "description": "If the run was queued, details about the reason for queuing the run.",
            "children": [
              {
                "name": "code",
                "type": "string",
                "description": "The reason for queuing the run. * `ACTIVE_RUNS_LIMIT_REACHED`: The run was queued due to<br />reaching the workspace limit of active task runs. * `MAX_CONCURRENT_RUNS_REACHED`: The run was<br />queued due to reaching the per-job limit of concurrent job runs. *<br />`ACTIVE_RUN_JOB_TASKS_LIMIT_REACHED`: The run was queued due to reaching the workspace limit of<br />active run job tasks."
              },
              {
                "name": "message",
                "type": "string",
                "description": "A descriptive message with the queuing details. This field is unstructured, and its exact format is subject to change."
              }
            ]
          },
          {
            "name": "state",
            "type": "string",
            "description": "The current state of the run."
          },
          {
            "name": "termination_details",
            "type": "object",
            "description": "If the run is in a TERMINATING or TERMINATED state, details about the reason for terminating the run.",
            "children": [
              {
                "name": "code",
                "type": "string",
                "description": "The code indicates why the run was terminated. Additional codes might be introduced in future<br />releases. * `SUCCESS`: The run was completed successfully. * `SUCCESS_WITH_FAILURES`: The run<br />was completed successfully but some child runs failed. * `USER_CANCELED`: The run was<br />successfully canceled during execution by a user. * `CANCELED`: The run was canceled during<br />execution by the Databricks platform; for example, if the maximum run duration was exceeded. *<br />`SKIPPED`: Run was never executed, for example, if the upstream task run failed, the dependency<br />type condition was not met, or there were no material tasks to execute. * `INTERNAL_ERROR`: The<br />run encountered an unexpected error. Refer to the state message for further details. *<br />`DRIVER_ERROR`: The run encountered an error while communicating with the Spark Driver. *<br />`CLUSTER_ERROR`: The run failed due to a cluster error. Refer to the state message for further<br />details. * `REPOSITORY_CHECKOUT_FAILED`: Failed to complete the checkout due to an error when<br />communicating with the third party service. * `INVALID_CLUSTER_REQUEST`: The run failed because<br />it issued an invalid request to start the cluster. * `WORKSPACE_RUN_LIMIT_EXCEEDED`: The<br />workspace has reached the quota for the maximum number of concurrent active runs. Consider<br />scheduling the runs over a larger time frame. * `FEATURE_DISABLED`: The run failed because it<br />tried to access a feature unavailable for the workspace. * `CLUSTER_REQUEST_LIMIT_EXCEEDED`: The<br />number of cluster creation, start, and upsize requests have exceeded the allotted rate limit.<br />Consider spreading the run execution over a larger time frame. * `STORAGE_ACCESS_ERROR`: The run<br />failed due to an error when accessing the customer blob storage. Refer to the state message for<br />further details. * `RUN_EXECUTION_ERROR`: The run was completed with task failures. For more<br />details, refer to the state message or run output. * `UNAUTHORIZED_ERROR`: The run failed due to<br />a permission issue while accessing a resource. Refer to the state message for further details. *<br />`LIBRARY_INSTALLATION_ERROR`: The run failed while installing the user-requested library. Refer<br />to the state message for further details. The causes might include, but are not limited to: The<br />provided library is invalid, there are insufficient permissions to install the library, and so<br />forth. * `MAX_CONCURRENT_RUNS_EXCEEDED`: The scheduled run exceeds the limit of maximum<br />concurrent runs set for the job. * `MAX_SPARK_CONTEXTS_EXCEEDED`: The run is scheduled on a<br />cluster that has already reached the maximum number of contexts it is configured to create. See:<br />[Link]. * `RESOURCE_NOT_FOUND`: A resource necessary for run execution does not exist. Refer to<br />the state message for further details. * `INVALID_RUN_CONFIGURATION`: The run failed due to an<br />invalid configuration. Refer to the state message for further details. * `CLOUD_FAILURE`: The<br />run failed due to a cloud provider issue. Refer to the state message for further details. *<br />`MAX_JOB_QUEUE_SIZE_EXCEEDED`: The run was skipped due to reaching the job level queue size<br />limit. * `DISABLED`: The run was never executed because it was disabled explicitly by the user.<br />* `BREAKING_CHANGE`: Run failed because of an intentional breaking change in Spark, but it will<br />be retried with a mitigation config.<br /><br />[Link]: https://kb.databricks.com/en_US/notebooks/too-many-execution-contexts-are-open-right-now"
              },
              {
                "name": "message",
                "type": "string",
                "description": "A descriptive message with the termination details. This field is unstructured and the format might change."
              },
              {
                "name": "type",
                "type": "string",
                "description": "* `SUCCESS`: The run terminated without any issues * `INTERNAL_ERROR`: An error occurred in the<br />Databricks platform. Please look at the [status page] or contact support if the issue persists.<br />* `CLIENT_ERROR`: The run was terminated because of an error caused by user input or the job<br />configuration. * `CLOUD_FAILURE`: The run was terminated because of an issue with your cloud<br />provider.<br /><br />[status page]: https://status.databricks.com/"
              }
            ]
          }
        ]
      },
      {
        "name": "task_run_ids",
        "type": "array",
        "description": "The run IDs of the task runs that ran as part of this repair history item."
      },
      {
        "name": "type",
        "type": "string",
        "description": "The repair history item type. Indicates whether a run is the original run or a repair run."
      }
    ]
  },
  {
    "name": "run_duration",
    "type": "integer",
    "description": "The time in milliseconds it took the job run and all of its repairs to finish."
  },
  {
    "name": "run_page_url",
    "type": "string",
    "description": "The URL to the detail page of the run."
  },
  {
    "name": "run_type",
    "type": "string",
    "description": "The type of a run. * `JOB_RUN`: Normal job run. A run created with :method:jobs/runNow. *<br />`WORKFLOW_RUN`: Workflow run. A run created with [dbutils.notebook.run]. * `SUBMIT_RUN`: Submit<br />run. A run created with :method:jobs/submit.<br /><br />[dbutils.notebook.run]: https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-workflow"
  },
  {
    "name": "schedule",
    "type": "object",
    "description": "The cron schedule that triggered this run if it was triggered by the periodic scheduler.",
    "children": [
      {
        "name": "quartz_cron_expression",
        "type": "string",
        "description": ""
      },
      {
        "name": "timezone_id",
        "type": "string",
        "description": "A Java timezone ID. The schedule for a job is resolved with respect to this timezone. See [Java TimeZone] for details. This field is required. [Java TimeZone]: https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html"
      },
      {
        "name": "pause_status",
        "type": "string",
        "description": "Indicate whether this schedule is paused or not."
      }
    ]
  },
  {
    "name": "setup_duration",
    "type": "integer",
    "description": "The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `setup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
  },
  {
    "name": "start_time",
    "type": "integer",
    "description": "The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued."
  },
  {
    "name": "state",
    "type": "object",
    "description": "Deprecated. Please use the `status` field instead.",
    "children": [
      {
        "name": "life_cycle_state",
        "type": "string",
        "description": "A value indicating the run's current lifecycle state. This field is always available in the response. Note: Additional states might be introduced in future releases."
      },
      {
        "name": "queue_reason",
        "type": "string",
        "description": "The reason indicating why the run was queued."
      },
      {
        "name": "result_state",
        "type": "string",
        "description": "A value indicating the run's result. This field is only available for terminal lifecycle states. Note: Additional states might be introduced in future releases."
      },
      {
        "name": "state_message",
        "type": "string",
        "description": "A descriptive message for the current state. This field is unstructured, and its exact format is subject to change."
      },
      {
        "name": "user_cancelled_or_timedout",
        "type": "boolean",
        "description": "A value indicating whether a run was canceled manually by a user or by the scheduler because the run timed out."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The current status of the run",
    "children": [
      {
        "name": "queue_details",
        "type": "object",
        "description": "If the run was queued, details about the reason for queuing the run.",
        "children": [
          {
            "name": "code",
            "type": "string",
            "description": "The reason for queuing the run. * `ACTIVE_RUNS_LIMIT_REACHED`: The run was queued due to<br />reaching the workspace limit of active task runs. * `MAX_CONCURRENT_RUNS_REACHED`: The run was<br />queued due to reaching the per-job limit of concurrent job runs. *<br />`ACTIVE_RUN_JOB_TASKS_LIMIT_REACHED`: The run was queued due to reaching the workspace limit of<br />active run job tasks."
          },
          {
            "name": "message",
            "type": "string",
            "description": "A descriptive message with the queuing details. This field is unstructured, and its exact format is subject to change."
          }
        ]
      },
      {
        "name": "state",
        "type": "string",
        "description": "The current state of the run."
      },
      {
        "name": "termination_details",
        "type": "object",
        "description": "If the run is in a TERMINATING or TERMINATED state, details about the reason for terminating the run.",
        "children": [
          {
            "name": "code",
            "type": "string",
            "description": "The code indicates why the run was terminated. Additional codes might be introduced in future<br />releases. * `SUCCESS`: The run was completed successfully. * `SUCCESS_WITH_FAILURES`: The run<br />was completed successfully but some child runs failed. * `USER_CANCELED`: The run was<br />successfully canceled during execution by a user. * `CANCELED`: The run was canceled during<br />execution by the Databricks platform; for example, if the maximum run duration was exceeded. *<br />`SKIPPED`: Run was never executed, for example, if the upstream task run failed, the dependency<br />type condition was not met, or there were no material tasks to execute. * `INTERNAL_ERROR`: The<br />run encountered an unexpected error. Refer to the state message for further details. *<br />`DRIVER_ERROR`: The run encountered an error while communicating with the Spark Driver. *<br />`CLUSTER_ERROR`: The run failed due to a cluster error. Refer to the state message for further<br />details. * `REPOSITORY_CHECKOUT_FAILED`: Failed to complete the checkout due to an error when<br />communicating with the third party service. * `INVALID_CLUSTER_REQUEST`: The run failed because<br />it issued an invalid request to start the cluster. * `WORKSPACE_RUN_LIMIT_EXCEEDED`: The<br />workspace has reached the quota for the maximum number of concurrent active runs. Consider<br />scheduling the runs over a larger time frame. * `FEATURE_DISABLED`: The run failed because it<br />tried to access a feature unavailable for the workspace. * `CLUSTER_REQUEST_LIMIT_EXCEEDED`: The<br />number of cluster creation, start, and upsize requests have exceeded the allotted rate limit.<br />Consider spreading the run execution over a larger time frame. * `STORAGE_ACCESS_ERROR`: The run<br />failed due to an error when accessing the customer blob storage. Refer to the state message for<br />further details. * `RUN_EXECUTION_ERROR`: The run was completed with task failures. For more<br />details, refer to the state message or run output. * `UNAUTHORIZED_ERROR`: The run failed due to<br />a permission issue while accessing a resource. Refer to the state message for further details. *<br />`LIBRARY_INSTALLATION_ERROR`: The run failed while installing the user-requested library. Refer<br />to the state message for further details. The causes might include, but are not limited to: The<br />provided library is invalid, there are insufficient permissions to install the library, and so<br />forth. * `MAX_CONCURRENT_RUNS_EXCEEDED`: The scheduled run exceeds the limit of maximum<br />concurrent runs set for the job. * `MAX_SPARK_CONTEXTS_EXCEEDED`: The run is scheduled on a<br />cluster that has already reached the maximum number of contexts it is configured to create. See:<br />[Link]. * `RESOURCE_NOT_FOUND`: A resource necessary for run execution does not exist. Refer to<br />the state message for further details. * `INVALID_RUN_CONFIGURATION`: The run failed due to an<br />invalid configuration. Refer to the state message for further details. * `CLOUD_FAILURE`: The<br />run failed due to a cloud provider issue. Refer to the state message for further details. *<br />`MAX_JOB_QUEUE_SIZE_EXCEEDED`: The run was skipped due to reaching the job level queue size<br />limit. * `DISABLED`: The run was never executed because it was disabled explicitly by the user.<br />* `BREAKING_CHANGE`: Run failed because of an intentional breaking change in Spark, but it will<br />be retried with a mitigation config.<br /><br />[Link]: https://kb.databricks.com/en_US/notebooks/too-many-execution-contexts-are-open-right-now"
          },
          {
            "name": "message",
            "type": "string",
            "description": "A descriptive message with the termination details. This field is unstructured and the format might change."
          },
          {
            "name": "type",
            "type": "string",
            "description": "* `SUCCESS`: The run terminated without any issues * `INTERNAL_ERROR`: An error occurred in the<br />Databricks platform. Please look at the [status page] or contact support if the issue persists.<br />* `CLIENT_ERROR`: The run was terminated because of an error caused by user input or the job<br />configuration. * `CLOUD_FAILURE`: The run was terminated because of an issue with your cloud<br />provider.<br /><br />[status page]: https://status.databricks.com/"
          }
        ]
      }
    ]
  },
  {
    "name": "tasks",
    "type": "array",
    "description": "The list of tasks performed by the run. Each task has its own `run_id` which you can use to call `JobsGetOutput` to retrieve the run resutls. If more than 100 tasks are available, you can paginate through them using :method:jobs/getrun. Use the `next_page_token` field at the object root to determine if more results are available.",
    "children": [
      {
        "name": "task_key",
        "type": "string",
        "description": "A unique name for the task. This field is used to refer to this task from other tasks. This field is required and must be unique within its parent job. On Update or Reset, this field is used to reference the tasks to be updated or reset."
      },
      {
        "name": "attempt_number",
        "type": "integer",
        "description": "The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt_number of 0. If the initial run attempt fails, and the job has a retry policy (`max_retries` &gt; 0), subsequent runs are created with an `original_attempt_run_id` of the original attempt’s ID and an incrementing `attempt_number`. Runs are retried only until they succeed, and the maximum `attempt_number` is the same as the `max_retries` value for the job."
      },
      {
        "name": "clean_rooms_notebook_task",
        "type": "object",
        "description": "The task runs a [clean rooms] notebook when the `clean_rooms_notebook_task` field is present. [clean rooms]: https://docs.databricks.com/clean-rooms/index.html",
        "children": [
          {
            "name": "clean_room_name",
            "type": "string",
            "description": "The clean room that the notebook belongs to."
          },
          {
            "name": "notebook_name",
            "type": "string",
            "description": "Name of the notebook being run."
          },
          {
            "name": "etag",
            "type": "string",
            "description": "Checksum to validate the freshness of the notebook resource (i.e. the notebook being run is the latest version). It can be fetched by calling the :method:cleanroomassets/get API."
          },
          {
            "name": "notebook_base_parameters",
            "type": "object",
            "description": "Base parameters to be used for the clean room notebook job."
          }
        ]
      },
      {
        "name": "cleanup_duration",
        "type": "integer",
        "description": "The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `cleanup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
      },
      {
        "name": "cluster_instance",
        "type": "object",
        "description": "The cluster used for this run. If the run is specified to use a new cluster, this field is set once the Jobs service has requested a cluster for the run.",
        "children": [
          {
            "name": "cluster_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "spark_context_id",
            "type": "string",
            "description": "The canonical identifier for the Spark context used by a run. This field is filled in once the run begins execution. This value can be used to view the Spark UI by browsing to `/#setting/sparkui/$cluster_id/$spark_context_id`. The Spark UI continues to be available after the run has completed. The response won’t include this field if the identifier is not available yet."
          }
        ]
      },
      {
        "name": "compute",
        "type": "object",
        "description": "Task level compute configuration.",
        "children": [
          {
            "name": "hardware_accelerator",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "condition_task",
        "type": "object",
        "description": "The task evaluates a condition that can be used to control the execution of other tasks when the `condition_task` field is present. The condition task does not require a cluster to execute and does not support retries or notifications.",
        "children": [
          {
            "name": "op",
            "type": "string",
            "description": "* `EQUAL_TO`, `NOT_EQUAL` operators perform string comparison of their operands. This means that<br />`“12.0” == “12”` will evaluate to `false`. * `GREATER_THAN`, `GREATER_THAN_OR_EQUAL`,<br />`LESS_THAN`, `LESS_THAN_OR_EQUAL` operators perform numeric comparison of their operands.<br />`“12.0” >= “12”` will evaluate to `true`, `“10.0” >= “12”` will evaluate to<br />`false`.<br /><br />The boolean comparison to task values can be implemented with operators `EQUAL_TO`, `NOT_EQUAL`.<br />If a task value was set to a boolean value, it will be serialized to `“true”` or<br />`“false”` for the comparison."
          },
          {
            "name": "left",
            "type": "string",
            "description": "The left operand of the condition task. Can be either a string value or a job state or parameter reference."
          },
          {
            "name": "right",
            "type": "string",
            "description": "The right operand of the condition task. Can be either a string value or a job state or parameter reference."
          },
          {
            "name": "outcome",
            "type": "string",
            "description": "The condition expression evaluation result. Filled in if the task was successfully completed. Can be `\"true\"` or `\"false\"`"
          }
        ]
      },
      {
        "name": "dashboard_task",
        "type": "object",
        "description": "The task refreshes a dashboard and sends a snapshot to subscribers.",
        "children": [
          {
            "name": "dashboard_id",
            "type": "string",
            "description": "The identifier of the dashboard to refresh."
          },
          {
            "name": "filters",
            "type": "object",
            "description": "Dashboard task parameters. Used to apply dashboard filter values during dashboard task execution. Parameter values get applied to any dashboard filters that have a matching URL identifier as the parameter key. The parameter value format is dependent on the filter type: - For text and single-select filters, provide a single value (e.g. `\"value\"`) - For date and datetime filters, provide the value in ISO 8601 format (e.g. `\"2000-01-01T00:00:00\"`) - For multi-select filters, provide a JSON array of values (e.g. `\"[\\\"value1\\\",\\\"value2\\\"]\"`) - For range and date range filters, provide a JSON object with `start` and `end` (e.g. `\"&#123;\\\"start\\\":\\\"1\\\",\\\"end\\\":\\\"10\\\"&#125;\"`)"
          },
          {
            "name": "subscription",
            "type": "object",
            "description": "Optional: subscription configuration for sending the dashboard snapshot.",
            "children": [
              {
                "name": "custom_subject",
                "type": "string",
                "description": ""
              },
              {
                "name": "paused",
                "type": "boolean",
                "description": "When true, the subscription will not send emails."
              },
              {
                "name": "subscribers",
                "type": "array",
                "description": "The list of subscribers to send the snapshot of the dashboard to."
              }
            ]
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "Optional: The warehouse id to execute the dashboard with for the schedule. If not specified, the default warehouse of the dashboard will be used."
          }
        ]
      },
      {
        "name": "dbt_cloud_task",
        "type": "object",
        "description": "Task type for dbt cloud, deprecated in favor of the new name dbt_platform_task",
        "children": [
          {
            "name": "connection_resource_name",
            "type": "string",
            "description": "The resource name of the UC connection that authenticates the dbt Cloud for this task"
          },
          {
            "name": "dbt_cloud_job_id",
            "type": "integer",
            "description": "Id of the dbt Cloud job to be triggered"
          }
        ]
      },
      {
        "name": "dbt_platform_task",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "connection_resource_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "dbt_platform_job_id",
            "type": "string",
            "description": "Id of the dbt platform job to be triggered. Specified as a string for maximum compatibility with clients."
          }
        ]
      },
      {
        "name": "dbt_task",
        "type": "object",
        "description": "The task runs one or more dbt commands when the `dbt_task` field is present. The dbt task requires both Databricks SQL and the ability to use a serverless or a pro SQL warehouse.",
        "children": [
          {
            "name": "commands",
            "type": "array",
            "description": ""
          },
          {
            "name": "catalog",
            "type": "string",
            "description": "Optional name of the catalog to use. The value is the top level in the 3-level namespace of Unity Catalog (catalog / schema / relation). The catalog value can only be specified if a warehouse_id is specified. Requires dbt-databricks &gt;= 1.1.1."
          },
          {
            "name": "profiles_directory",
            "type": "string",
            "description": "Optional (relative) path to the profiles directory. Can only be specified if no warehouse_id is specified. If no warehouse_id is specified and this folder is unset, the root directory is used."
          },
          {
            "name": "project_directory",
            "type": "string",
            "description": "Path to the project directory. Optional for Git sourced tasks, in which case if no value is provided, the root of the Git repository is used."
          },
          {
            "name": "schema",
            "type": "string",
            "description": "Optional schema to write to. This parameter is only used when a warehouse_id is also provided. If not provided, the `default` schema is used."
          },
          {
            "name": "source",
            "type": "string",
            "description": "Optional location type of the project directory. When set to `WORKSPACE`, the project will be retrieved from the local Databricks workspace. When set to `GIT`, the project will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Project is located in Databricks workspace. * `GIT`: Project is located in cloud Git provider."
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "ID of the SQL warehouse to connect to. If provided, we automatically generate and provide the profile and connection details to dbt. It can be overridden on a per-command basis by using the `--profiles-dir` command line argument."
          }
        ]
      },
      {
        "name": "depends_on",
        "type": "array",
        "description": "An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete successfully before executing this task. The key is `task_key`, and the value is the name assigned to the dependent task.",
        "children": [
          {
            "name": "task_key",
            "type": "string",
            "description": ""
          },
          {
            "name": "outcome",
            "type": "string",
            "description": "Can only be specified on condition task dependencies. The outcome of the dependent task that must be met for this task to run."
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "An optional description for this task."
      },
      {
        "name": "effective_performance_target",
        "type": "string",
        "description": "The actual performance target used by the serverless run during execution. This can differ from the client-set performance target on the request depending on whether the performance mode is supported by the job type. * `STANDARD`: Enables cost-efficient execution of serverless workloads. * `PERFORMANCE_OPTIMIZED`: Prioritizes fast startup and execution times through rapid scaling and optimized cluster performance."
      },
      {
        "name": "email_notifications",
        "type": "object",
        "description": "An optional set of email addresses notified when the task run begins or completes. The default behavior is to not send any emails.",
        "children": [
          {
            "name": "no_alert_for_skipped_runs",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "on_duration_warning_threshold_exceeded",
            "type": "array",
            "description": "A list of email addresses to be notified when the duration of a run exceeds the threshold specified for the `RUN_DURATION_SECONDS` metric in the `health` field. If no rule for the `RUN_DURATION_SECONDS` metric is specified in the `health` field for the job, notifications are not sent."
          },
          {
            "name": "on_failure",
            "type": "array",
            "description": "A list of email addresses to be notified when a run unsuccessfully completes. A run is considered to have completed unsuccessfully if it ends with an `INTERNAL_ERROR` `life_cycle_state` or a `FAILED`, or `TIMED_OUT` result_state. If this is not specified on job creation, reset, or update the list is empty, and notifications are not sent."
          },
          {
            "name": "on_start",
            "type": "array",
            "description": "A list of email addresses to be notified when a run begins. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent."
          },
          {
            "name": "on_streaming_backlog_exceeded",
            "type": "array",
            "description": "A list of email addresses to notify when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the `health` field using the following metrics: `STREAMING_BACKLOG_BYTES`, `STREAMING_BACKLOG_RECORDS`, `STREAMING_BACKLOG_SECONDS`, or `STREAMING_BACKLOG_FILES`. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes."
          },
          {
            "name": "on_success",
            "type": "array",
            "description": "A list of email addresses to be notified when a run successfully completes. A run is considered to have completed successfully if it ends with a `TERMINATED` `life_cycle_state` and a `SUCCESS` result_state. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent."
          }
        ]
      },
      {
        "name": "end_time",
        "type": "integer",
        "description": "The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running."
      },
      {
        "name": "environment_key",
        "type": "string",
        "description": "The key that references an environment spec in a job. This field is required for Python script, Python wheel and dbt tasks when using serverless compute."
      },
      {
        "name": "execution_duration",
        "type": "integer",
        "description": "The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `execution_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
      },
      {
        "name": "existing_cluster_id",
        "type": "string",
        "description": "If existing_cluster_id, the ID of an existing cluster that is used for all runs. When running jobs or tasks on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs and tasks on new clusters for greater reliability"
      },
      {
        "name": "for_each_task",
        "type": "object",
        "description": "The task executes a nested task for every input provided when the `for_each_task` field is present.",
        "children": [
          {
            "name": "inputs",
            "type": "string",
            "description": ""
          },
          {
            "name": "task",
            "type": "object",
            "description": "Configuration for the task that will be run for each element in the array",
            "children": [
              {
                "name": "task_key",
                "type": "string",
                "description": ""
              },
              {
                "name": "clean_rooms_notebook_task",
                "type": "object",
                "description": "The task runs a [clean rooms] notebook when the `clean_rooms_notebook_task` field is present. [clean rooms]: https://docs.databricks.com/clean-rooms/index.html"
              },
              {
                "name": "compute",
                "type": "object",
                "description": "Task level compute configuration."
              },
              {
                "name": "condition_task",
                "type": "object",
                "description": "The task evaluates a condition that can be used to control the execution of other tasks when the `condition_task` field is present. The condition task does not require a cluster to execute and does not support retries or notifications."
              },
              {
                "name": "dashboard_task",
                "type": "object",
                "description": "The task refreshes a dashboard and sends a snapshot to subscribers."
              },
              {
                "name": "dbt_cloud_task",
                "type": "object",
                "description": "Task type for dbt cloud, deprecated in favor of the new name dbt_platform_task"
              },
              {
                "name": "dbt_platform_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "dbt_task",
                "type": "object",
                "description": "The task runs one or more dbt commands when the `dbt_task` field is present. The dbt task requires both Databricks SQL and the ability to use a serverless or a pro SQL warehouse."
              },
              {
                "name": "depends_on",
                "type": "array",
                "description": "An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete before executing this task. The task will run only if the `run_if` condition is true. The key is `task_key`, and the value is the name assigned to the dependent task."
              },
              {
                "name": "description",
                "type": "string",
                "description": "An optional description for this task."
              },
              {
                "name": "disable_auto_optimization",
                "type": "boolean",
                "description": "An option to disable auto optimization in serverless"
              },
              {
                "name": "disabled",
                "type": "boolean",
                "description": "An optional flag to disable the task. If set to true, the task will not run even if it is part of a job."
              },
              {
                "name": "email_notifications",
                "type": "object",
                "description": "An optional set of email addresses that is notified when runs of this task begin or complete as well as when this task is deleted. The default behavior is to not send any emails."
              },
              {
                "name": "environment_key",
                "type": "string",
                "description": "The key that references an environment spec in a job. This field is required for Python script, Python wheel and dbt tasks when using serverless compute."
              },
              {
                "name": "existing_cluster_id",
                "type": "string",
                "description": "If existing_cluster_id, the ID of an existing cluster that is used for all runs. When running jobs or tasks on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs and tasks on new clusters for greater reliability"
              },
              {
                "name": "for_each_task",
                "type": "object",
                "description": "The task executes a nested task for every input provided when the `for_each_task` field is present."
              },
              {
                "name": "gen_ai_compute_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "health",
                "type": "object",
                "description": "An optional set of health rules that can be defined for this job."
              },
              {
                "name": "job_cluster_key",
                "type": "string",
                "description": "If job_cluster_key, this task is executed reusing the cluster specified in `job.settings.job_clusters`."
              },
              {
                "name": "libraries",
                "type": "string",
                "description": "An optional list of libraries to be installed on the cluster. The default value is an empty list."
              },
              {
                "name": "max_retries",
                "type": "integer",
                "description": "An optional maximum number of times to retry an unsuccessful run. A run is considered to be unsuccessful if it completes with the `FAILED` result_state or `INTERNAL_ERROR` `life_cycle_state`. The value `-1` means to retry indefinitely and the value `0` means to never retry."
              },
              {
                "name": "min_retry_interval_millis",
                "type": "integer",
                "description": "An optional minimal interval in milliseconds between the start of the failed run and the subsequent retry run. The default behavior is that unsuccessful runs are immediately retried."
              },
              {
                "name": "new_cluster",
                "type": "string",
                "description": "If new_cluster, a description of a new cluster that is created for each run."
              },
              {
                "name": "notebook_task",
                "type": "object",
                "description": "The task runs a notebook when the `notebook_task` field is present."
              },
              {
                "name": "notification_settings",
                "type": "object",
                "description": "Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this task."
              },
              {
                "name": "pipeline_task",
                "type": "object",
                "description": "The task triggers a pipeline update when the `pipeline_task` field is present. Only pipelines configured to use triggered more are supported."
              },
              {
                "name": "power_bi_task",
                "type": "object",
                "description": "The task triggers a Power BI semantic model update when the `power_bi_task` field is present."
              },
              {
                "name": "python_wheel_task",
                "type": "object",
                "description": "The task runs a Python wheel when the `python_wheel_task` field is present."
              },
              {
                "name": "retry_on_timeout",
                "type": "boolean",
                "description": "An optional policy to specify whether to retry a job when it times out. The default behavior is to not retry on timeout."
              },
              {
                "name": "run_if",
                "type": "string",
                "description": "An optional value specifying the condition determining whether the task is run once its dependencies have been completed. * `ALL_SUCCESS`: All dependencies have executed and succeeded * `AT_LEAST_ONE_SUCCESS`: At least one dependency has succeeded * `NONE_FAILED`: None of the dependencies have failed and at least one was executed * `ALL_DONE`: All dependencies have been completed * `AT_LEAST_ONE_FAILED`: At least one dependency failed * `ALL_FAILED`: ALl dependencies have failed"
              },
              {
                "name": "run_job_task",
                "type": "object",
                "description": "The task triggers another job when the `run_job_task` field is present."
              },
              {
                "name": "spark_jar_task",
                "type": "object",
                "description": "The task runs a JAR when the `spark_jar_task` field is present."
              },
              {
                "name": "spark_python_task",
                "type": "object",
                "description": "The task runs a Python file when the `spark_python_task` field is present."
              },
              {
                "name": "spark_submit_task",
                "type": "object",
                "description": "(Legacy) The task runs the spark-submit script when the spark_submit_task field is present. Databricks recommends using the spark_jar_task instead; see [Spark Submit task for jobs](/jobs/spark-submit)."
              },
              {
                "name": "sql_task",
                "type": "object",
                "description": "The task runs a SQL query or file, or it refreshes a SQL alert or a legacy SQL dashboard when the `sql_task` field is present."
              },
              {
                "name": "timeout_seconds",
                "type": "integer",
                "description": "An optional timeout applied to each run of this job task. A value of `0` means no timeout."
              },
              {
                "name": "webhook_notifications",
                "type": "object",
                "description": "A collection of system notification IDs to notify when runs of this task begin or complete. The default behavior is to not send any system notifications."
              }
            ]
          },
          {
            "name": "concurrency",
            "type": "integer",
            "description": "An optional maximum allowed number of concurrent runs of the task. Set this value if you want to be able to execute multiple runs of the task concurrently."
          },
          {
            "name": "stats",
            "type": "object",
            "description": "Read only field. Populated for GetRun and ListRuns RPC calls and stores the execution stats of an For each task",
            "children": [
              {
                "name": "error_message_stats",
                "type": "array",
                "description": ""
              },
              {
                "name": "task_run_stats",
                "type": "object",
                "description": "Describes stats of the iteration. Only latest retries are considered."
              }
            ]
          }
        ]
      },
      {
        "name": "gen_ai_compute_task",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "dl_runtime_image",
            "type": "string",
            "description": ""
          },
          {
            "name": "command",
            "type": "string",
            "description": "Command launcher to run the actual script, e.g. bash, python etc."
          },
          {
            "name": "compute",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "num_gpus",
                "type": "integer",
                "description": ""
              },
              {
                "name": "gpu_node_pool_id",
                "type": "string",
                "description": "IDof the GPU pool to use."
              },
              {
                "name": "gpu_type",
                "type": "string",
                "description": "GPU type."
              }
            ]
          },
          {
            "name": "mlflow_experiment_name",
            "type": "string",
            "description": "Optional string containing the name of the MLflow experiment to log the run to. If name is not found, backend will create the mlflow experiment using the name."
          },
          {
            "name": "source",
            "type": "string",
            "description": "Optional location type of the training script. When set to `WORKSPACE`, the script will be retrieved from the local Databricks workspace. When set to `GIT`, the script will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Script is located in Databricks workspace. * `GIT`: Script is located in cloud Git provider."
          },
          {
            "name": "training_script_path",
            "type": "string",
            "description": "The training script file path to be executed. Cloud file URIs (such as dbfs:/, s3:/, adls:/, gcs:/) and workspace paths are supported. For python files stored in the Databricks workspace, the path must be absolute and begin with `/`. For files stored in a remote repository, the path must be relative. This field is required."
          },
          {
            "name": "yaml_parameters",
            "type": "string",
            "description": "Optional string containing model parameters passed to the training script in yaml format. If present, then the content in yaml_parameters_file_path will be ignored."
          },
          {
            "name": "yaml_parameters_file_path",
            "type": "string",
            "description": "Optional path to a YAML file containing model parameters passed to the training script."
          }
        ]
      },
      {
        "name": "git_source",
        "type": "object",
        "description": "An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks. If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task. Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.",
        "children": [
          {
            "name": "git_url",
            "type": "string",
            "description": "URL of the repository to be cloned by this job."
          },
          {
            "name": "git_provider",
            "type": "string",
            "description": "Unique identifier of the service used to host the Git repository. The value is case insensitive."
          },
          {
            "name": "git_branch",
            "type": "string",
            "description": "Name of the branch to be checked out and used by this job. This field cannot be specified in conjunction with git_tag or git_commit."
          },
          {
            "name": "git_commit",
            "type": "string",
            "description": "Commit to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_tag."
          },
          {
            "name": "git_snapshot",
            "type": "object",
            "description": "Read-only state of the remote repository at the time the job was run. This field is only<br />    included on job runs.",
            "children": [
              {
                "name": "used_commit",
                "type": "string",
                "description": "Commit that was used to execute the run. If git_branch was specified, this points to the HEAD of the branch at the time of the run; if git_tag was specified, this points to the commit the tag points to."
              }
            ]
          },
          {
            "name": "git_tag",
            "type": "string",
            "description": "Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_commit."
          },
          {
            "name": "job_source",
            "type": "object",
            "description": "The source of the job specification in the remote repository when the job is source controlled.",
            "children": [
              {
                "name": "job_config_path",
                "type": "string",
                "description": "Path of the job YAML file that contains the job specification."
              },
              {
                "name": "import_from_git_branch",
                "type": "string",
                "description": "Name of the branch which the job is imported from."
              },
              {
                "name": "dirty_state",
                "type": "string",
                "description": "Dirty state indicates the job is not fully synced with the job specification in the remote repository. Possible values are: * `NOT_SYNCED`: The job is not yet synced with the remote job specification. Import the remote job specification from UI to make the job fully synced. * `DISCONNECTED`: The job is temporary disconnected from the remote job specification and is allowed for live edit. Import the remote job specification again from UI to make the job fully synced."
              }
            ]
          }
        ]
      },
      {
        "name": "job_cluster_key",
        "type": "string",
        "description": "If job_cluster_key, this task is executed reusing the cluster specified in `job.settings.job_clusters`."
      },
      {
        "name": "libraries",
        "type": "string",
        "description": "An optional list of libraries to be installed on the cluster. The default value is an empty list."
      },
      {
        "name": "new_cluster",
        "type": "string",
        "description": "If new_cluster, a description of a new cluster that is created for each run."
      },
      {
        "name": "notebook_task",
        "type": "object",
        "description": "The task runs a notebook when the `notebook_task` field is present.",
        "children": [
          {
            "name": "notebook_path",
            "type": "string",
            "description": ""
          },
          {
            "name": "base_parameters",
            "type": "object",
            "description": "Base parameters to be used for each run of this job. If the run is initiated by a call to :method:jobs/run Now with parameters specified, the two parameters maps are merged. If the same key is specified in `base_parameters` and in `run-now`, the value from `run-now` is used. Use [Task parameter variables] to set parameters containing information about job runs. If the notebook takes a parameter that is not specified in the job’s `base_parameters` or the `run-now` override parameters, the default value from the notebook is used. Retrieve these parameters in a notebook using [dbutils.widgets.get]. The JSON representation of this field cannot exceed 1MB. [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-widgets"
          },
          {
            "name": "source",
            "type": "string",
            "description": "Optional location type of the notebook. When set to `WORKSPACE`, the notebook will be retrieved from the local Databricks workspace. When set to `GIT`, the notebook will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Notebook is located in Databricks workspace. * `GIT`: Notebook is located in cloud Git provider."
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "Optional `warehouse_id` to run the notebook on a SQL warehouse. Classic SQL warehouses are NOT supported, please use serverless or pro SQL warehouses. Note that SQL warehouses only support SQL cells; if the notebook contains non-SQL cells, the run will fail."
          }
        ]
      },
      {
        "name": "notification_settings",
        "type": "object",
        "description": "Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this task run.",
        "children": [
          {
            "name": "alert_on_last_attempt",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "no_alert_for_canceled_runs",
            "type": "boolean",
            "description": "If true, do not send notifications to recipients specified in `on_failure` if the run is canceled."
          },
          {
            "name": "no_alert_for_skipped_runs",
            "type": "boolean",
            "description": "If true, do not send notifications to recipients specified in `on_failure` if the run is skipped."
          }
        ]
      },
      {
        "name": "pipeline_task",
        "type": "object",
        "description": "The task triggers a pipeline update when the `pipeline_task` field is present. Only pipelines configured to use triggered more are supported.",
        "children": [
          {
            "name": "pipeline_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "full_refresh",
            "type": "boolean",
            "description": "If true, triggers a full refresh on the delta live table."
          }
        ]
      },
      {
        "name": "power_bi_task",
        "type": "object",
        "description": "The task triggers a Power BI semantic model update when the `power_bi_task` field is present.",
        "children": [
          {
            "name": "connection_resource_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "power_bi_model",
            "type": "object",
            "description": "The semantic model to update",
            "children": [
              {
                "name": "authentication_method",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              },
              {
                "name": "model_name",
                "type": "string",
                "description": "The name of the Power BI model"
              },
              {
                "name": "overwrite_existing",
                "type": "boolean",
                "description": "Whether to overwrite existing Power BI models"
              },
              {
                "name": "storage_mode",
                "type": "string",
                "description": "The default storage mode of the Power BI model"
              },
              {
                "name": "workspace_name",
                "type": "string",
                "description": "The name of the Power BI workspace of the model"
              }
            ]
          },
          {
            "name": "refresh_after_update",
            "type": "boolean",
            "description": "Whether the model should be refreshed after the update"
          },
          {
            "name": "tables",
            "type": "array",
            "description": "The tables to be exported to Power BI",
            "children": [
              {
                "name": "catalog",
                "type": "string",
                "description": ""
              },
              {
                "name": "name",
                "type": "string",
                "description": "The table name in Databricks"
              },
              {
                "name": "schema",
                "type": "string",
                "description": "The schema name in Databricks"
              },
              {
                "name": "storage_mode",
                "type": "string",
                "description": "The Power BI storage mode of the table"
              }
            ]
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "The SQL warehouse ID to use as the Power BI data source"
          }
        ]
      },
      {
        "name": "python_wheel_task",
        "type": "object",
        "description": "The task runs a Python wheel when the `python_wheel_task` field is present.",
        "children": [
          {
            "name": "package_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "entry_point",
            "type": "string",
            "description": "Named entry point to use, if it does not exist in the metadata of the package it executes the function from the package directly using `$packageName.$entryPoint()`"
          },
          {
            "name": "named_parameters",
            "type": "object",
            "description": "Command-line parameters passed to Python wheel task in the form of `[\"--name=task\", \"--data=dbfs:/path/to/data.json\"]`. Leave it empty if `parameters` is not null."
          },
          {
            "name": "parameters",
            "type": "array",
            "description": "Command-line parameters passed to Python wheel task. Leave it empty if `named_parameters` is not null."
          }
        ]
      },
      {
        "name": "queue_duration",
        "type": "integer",
        "description": "The time in milliseconds that the run has spent in the queue."
      },
      {
        "name": "resolved_values",
        "type": "object",
        "description": "Parameter values including resolved references",
        "children": [
          {
            "name": "condition_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "left",
                "type": "string",
                "description": ""
              },
              {
                "name": "right",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "dbt_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "commands",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "notebook_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "base_parameters",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "python_wheel_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "named_parameters",
                "type": "object",
                "description": ""
              },
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "run_job_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "job_parameters",
                "type": "object",
                "description": ""
              },
              {
                "name": "parameters",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "simulation_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "spark_jar_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "spark_python_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "spark_submit_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "sql_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "object",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "run_duration",
        "type": "integer",
        "description": "The time in milliseconds it took the job run and all of its repairs to finish."
      },
      {
        "name": "run_id",
        "type": "integer",
        "description": "The ID of the task run."
      },
      {
        "name": "run_if",
        "type": "string",
        "description": "An optional value indicating the condition that determines whether the task should be run once its dependencies have been completed. When omitted, defaults to `ALL_SUCCESS`. See :method:jobs/create for a list of possible values."
      },
      {
        "name": "run_job_task",
        "type": "object",
        "description": "The task triggers another job when the `run_job_task` field is present.",
        "children": [
          {
            "name": "job_id",
            "type": "integer",
            "description": ""
          },
          {
            "name": "dbt_commands",
            "type": "array",
            "description": "An array of commands to execute for jobs with the dbt task, for example `\"dbt_commands\": [\"dbt deps\", \"dbt seed\", \"dbt deps\", \"dbt seed\", \"dbt run\"]` ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "jar_params",
            "type": "array",
            "description": "A list of parameters for jobs with Spark JAR tasks, for example `\"jar_params\": [\"john doe\", \"35\"]`. The parameters are used to invoke the main function of the main class specified in the Spark JAR task. If not specified upon `run-now`, it defaults to an empty list. jar_params cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example `&#123;\"jar_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "job_parameters",
            "type": "object",
            "description": "Job-level parameters used to trigger the job."
          },
          {
            "name": "notebook_params",
            "type": "object",
            "description": "A map from keys to values for jobs with notebook task, for example `\"notebook_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;`. The map is passed to the notebook and is accessible through the [dbutils.widgets.get] function. If not specified upon `run-now`, the triggered run uses the job’s base parameters. notebook_params cannot be specified in conjunction with jar_params. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. The JSON representation of this field (for example `&#123;\"notebook_params\":&#123;\"name\":\"john doe\",\"age\":\"35\"&#125;&#125;`) cannot exceed 10,000 bytes. [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "pipeline_params",
            "type": "object",
            "description": "Controls whether the pipeline should perform a full refresh",
            "children": [
              {
                "name": "full_refresh",
                "type": "boolean",
                "description": ""
              }
            ]
          },
          {
            "name": "python_named_params",
            "type": "object",
            "description": ""
          },
          {
            "name": "python_params",
            "type": "array",
            "description": "A list of parameters for jobs with Python tasks, for example `\"python_params\": [\"john doe\", \"35\"]`. The parameters are passed to Python file as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `&#123;\"python_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "spark_submit_params",
            "type": "array",
            "description": "A list of parameters for jobs with spark submit task, for example `\"spark_submit_params\": [\"--class\", \"org.apache.spark.examples.SparkPi\"]`. The parameters are passed to spark-submit script as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `&#123;\"python_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "sql_params",
            "type": "object",
            "description": "A map from keys to values for jobs with SQL task, for example `\"sql_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;`. The SQL alert task does not support custom parameters. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          }
        ]
      },
      {
        "name": "run_page_url",
        "type": "string",
        "description": ""
      },
      {
        "name": "setup_duration",
        "type": "integer",
        "description": "The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `setup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
      },
      {
        "name": "spark_jar_task",
        "type": "object",
        "description": "The task runs a JAR when the `spark_jar_task` field is present.",
        "children": [
          {
            "name": "jar_uri",
            "type": "string",
            "description": ""
          },
          {
            "name": "main_class_name",
            "type": "string",
            "description": "The full name of the class containing the main method to be executed. This class must be contained in a JAR provided as a library. The code must use `SparkContext.getOrCreate` to obtain a Spark context; otherwise, runs of the job fail."
          },
          {
            "name": "parameters",
            "type": "array",
            "description": "Parameters passed to the main method. Use [Task parameter variables] to set parameters containing information about job runs. [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables"
          },
          {
            "name": "run_as_repl",
            "type": "boolean",
            "description": "Deprecated. A value of `false` is no longer supported."
          }
        ]
      },
      {
        "name": "spark_python_task",
        "type": "object",
        "description": "The task runs a Python file when the `spark_python_task` field is present.",
        "children": [
          {
            "name": "python_file",
            "type": "string",
            "description": ""
          },
          {
            "name": "parameters",
            "type": "array",
            "description": "Command line parameters passed to the Python file. Use [Task parameter variables] to set parameters containing information about job runs. [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables"
          },
          {
            "name": "source",
            "type": "string",
            "description": "Optional location type of the Python file. When set to `WORKSPACE` or not specified, the file will be retrieved from the local Databricks workspace or cloud location (if the `python_file` has a URI format). When set to `GIT`, the Python file will be retrieved from a Git repository defined in `git_source`. * `WORKSPACE`: The Python file is located in a Databricks workspace or at a cloud filesystem URI. * `GIT`: The Python file is located in a remote Git repository."
          }
        ]
      },
      {
        "name": "spark_submit_task",
        "type": "object",
        "description": "(Legacy) The task runs the spark-submit script when the spark_submit_task field is present. Databricks recommends using the spark_jar_task instead; see [Spark Submit task for jobs](/jobs/spark-submit).",
        "children": [
          {
            "name": "parameters",
            "type": "array",
            "description": ""
          }
        ]
      },
      {
        "name": "sql_task",
        "type": "object",
        "description": "The task runs a SQL query or file, or it refreshes a SQL alert or a legacy SQL dashboard when the `sql_task` field is present.",
        "children": [
          {
            "name": "warehouse_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "alert",
            "type": "object",
            "description": "If alert, indicates that this job must refresh a SQL alert.",
            "children": [
              {
                "name": "alert_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "pause_subscriptions",
                "type": "boolean",
                "description": "If true, the alert notifications are not sent to subscribers."
              },
              {
                "name": "subscriptions",
                "type": "array",
                "description": "If specified, alert notifications are sent to subscribers."
              }
            ]
          },
          {
            "name": "dashboard",
            "type": "object",
            "description": "If dashboard, indicates that this job must refresh a SQL dashboard.",
            "children": [
              {
                "name": "dashboard_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "custom_subject",
                "type": "string",
                "description": "Subject of the email sent to subscribers of this task."
              },
              {
                "name": "pause_subscriptions",
                "type": "boolean",
                "description": "If true, the dashboard snapshot is not taken, and emails are not sent to subscribers."
              },
              {
                "name": "subscriptions",
                "type": "array",
                "description": "If specified, dashboard snapshots are sent to subscriptions."
              }
            ]
          },
          {
            "name": "file",
            "type": "object",
            "description": "If file, indicates that this job runs a SQL file in a remote Git repository.",
            "children": [
              {
                "name": "path",
                "type": "string",
                "description": ""
              },
              {
                "name": "source",
                "type": "string",
                "description": "Optional location type of the SQL file. When set to `WORKSPACE`, the SQL file will be retrieved from the local Databricks workspace. When set to `GIT`, the SQL file will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: SQL file is located in Databricks workspace. * `GIT`: SQL file is located in cloud Git provider."
              }
            ]
          },
          {
            "name": "parameters",
            "type": "object",
            "description": "Parameters to be used for each run of this job. The SQL alert task does not support custom parameters."
          },
          {
            "name": "query",
            "type": "object",
            "description": "If query, indicates that this job must execute a SQL query.",
            "children": [
              {
                "name": "query_id",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "start_time",
        "type": "integer",
        "description": "The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued."
      },
      {
        "name": "state",
        "type": "object",
        "description": "Deprecated. Please use the `status` field instead.",
        "children": [
          {
            "name": "life_cycle_state",
            "type": "string",
            "description": "A value indicating the run's current lifecycle state. This field is always available in the response. Note: Additional states might be introduced in future releases."
          },
          {
            "name": "queue_reason",
            "type": "string",
            "description": "The reason indicating why the run was queued."
          },
          {
            "name": "result_state",
            "type": "string",
            "description": "A value indicating the run's result. This field is only available for terminal lifecycle states. Note: Additional states might be introduced in future releases."
          },
          {
            "name": "state_message",
            "type": "string",
            "description": "A descriptive message for the current state. This field is unstructured, and its exact format is subject to change."
          },
          {
            "name": "user_cancelled_or_timedout",
            "type": "boolean",
            "description": "A value indicating whether a run was canceled manually by a user or by the scheduler because the run timed out."
          }
        ]
      },
      {
        "name": "status",
        "type": "object",
        "description": "The current status of the run",
        "children": [
          {
            "name": "queue_details",
            "type": "object",
            "description": "If the run was queued, details about the reason for queuing the run.",
            "children": [
              {
                "name": "code",
                "type": "string",
                "description": "The reason for queuing the run. * `ACTIVE_RUNS_LIMIT_REACHED`: The run was queued due to<br />reaching the workspace limit of active task runs. * `MAX_CONCURRENT_RUNS_REACHED`: The run was<br />queued due to reaching the per-job limit of concurrent job runs. *<br />`ACTIVE_RUN_JOB_TASKS_LIMIT_REACHED`: The run was queued due to reaching the workspace limit of<br />active run job tasks."
              },
              {
                "name": "message",
                "type": "string",
                "description": "A descriptive message with the queuing details. This field is unstructured, and its exact format is subject to change."
              }
            ]
          },
          {
            "name": "state",
            "type": "string",
            "description": "The current state of the run."
          },
          {
            "name": "termination_details",
            "type": "object",
            "description": "If the run is in a TERMINATING or TERMINATED state, details about the reason for terminating the run.",
            "children": [
              {
                "name": "code",
                "type": "string",
                "description": "The code indicates why the run was terminated. Additional codes might be introduced in future<br />releases. * `SUCCESS`: The run was completed successfully. * `SUCCESS_WITH_FAILURES`: The run<br />was completed successfully but some child runs failed. * `USER_CANCELED`: The run was<br />successfully canceled during execution by a user. * `CANCELED`: The run was canceled during<br />execution by the Databricks platform; for example, if the maximum run duration was exceeded. *<br />`SKIPPED`: Run was never executed, for example, if the upstream task run failed, the dependency<br />type condition was not met, or there were no material tasks to execute. * `INTERNAL_ERROR`: The<br />run encountered an unexpected error. Refer to the state message for further details. *<br />`DRIVER_ERROR`: The run encountered an error while communicating with the Spark Driver. *<br />`CLUSTER_ERROR`: The run failed due to a cluster error. Refer to the state message for further<br />details. * `REPOSITORY_CHECKOUT_FAILED`: Failed to complete the checkout due to an error when<br />communicating with the third party service. * `INVALID_CLUSTER_REQUEST`: The run failed because<br />it issued an invalid request to start the cluster. * `WORKSPACE_RUN_LIMIT_EXCEEDED`: The<br />workspace has reached the quota for the maximum number of concurrent active runs. Consider<br />scheduling the runs over a larger time frame. * `FEATURE_DISABLED`: The run failed because it<br />tried to access a feature unavailable for the workspace. * `CLUSTER_REQUEST_LIMIT_EXCEEDED`: The<br />number of cluster creation, start, and upsize requests have exceeded the allotted rate limit.<br />Consider spreading the run execution over a larger time frame. * `STORAGE_ACCESS_ERROR`: The run<br />failed due to an error when accessing the customer blob storage. Refer to the state message for<br />further details. * `RUN_EXECUTION_ERROR`: The run was completed with task failures. For more<br />details, refer to the state message or run output. * `UNAUTHORIZED_ERROR`: The run failed due to<br />a permission issue while accessing a resource. Refer to the state message for further details. *<br />`LIBRARY_INSTALLATION_ERROR`: The run failed while installing the user-requested library. Refer<br />to the state message for further details. The causes might include, but are not limited to: The<br />provided library is invalid, there are insufficient permissions to install the library, and so<br />forth. * `MAX_CONCURRENT_RUNS_EXCEEDED`: The scheduled run exceeds the limit of maximum<br />concurrent runs set for the job. * `MAX_SPARK_CONTEXTS_EXCEEDED`: The run is scheduled on a<br />cluster that has already reached the maximum number of contexts it is configured to create. See:<br />[Link]. * `RESOURCE_NOT_FOUND`: A resource necessary for run execution does not exist. Refer to<br />the state message for further details. * `INVALID_RUN_CONFIGURATION`: The run failed due to an<br />invalid configuration. Refer to the state message for further details. * `CLOUD_FAILURE`: The<br />run failed due to a cloud provider issue. Refer to the state message for further details. *<br />`MAX_JOB_QUEUE_SIZE_EXCEEDED`: The run was skipped due to reaching the job level queue size<br />limit. * `DISABLED`: The run was never executed because it was disabled explicitly by the user.<br />* `BREAKING_CHANGE`: Run failed because of an intentional breaking change in Spark, but it will<br />be retried with a mitigation config.<br /><br />[Link]: https://kb.databricks.com/en_US/notebooks/too-many-execution-contexts-are-open-right-now"
              },
              {
                "name": "message",
                "type": "string",
                "description": "A descriptive message with the termination details. This field is unstructured and the format might change."
              },
              {
                "name": "type",
                "type": "string",
                "description": "* `SUCCESS`: The run terminated without any issues * `INTERNAL_ERROR`: An error occurred in the<br />Databricks platform. Please look at the [status page] or contact support if the issue persists.<br />* `CLIENT_ERROR`: The run was terminated because of an error caused by user input or the job<br />configuration. * `CLOUD_FAILURE`: The run was terminated because of an issue with your cloud<br />provider.<br /><br />[status page]: https://status.databricks.com/"
              }
            ]
          }
        ]
      },
      {
        "name": "timeout_seconds",
        "type": "integer",
        "description": "An optional timeout applied to each run of this job task. A value of `0` means no timeout."
      },
      {
        "name": "webhook_notifications",
        "type": "object",
        "description": "A collection of system notification IDs to notify when the run begins or completes. The default behavior is to not send any system notifications. Task webhooks respect the task notification settings.",
        "children": [
          {
            "name": "on_duration_warning_threshold_exceeded",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_failure",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the `on_failure` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_start",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the `on_start` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_streaming_backlog_exceeded",
            "type": "array",
            "description": "An optional list of system notification IDs to call when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the `health` field using the following metrics: `STREAMING_BACKLOG_BYTES`, `STREAMING_BACKLOG_RECORDS`, `STREAMING_BACKLOG_SECONDS`, or `STREAMING_BACKLOG_FILES`. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes. A maximum of 3 destinations can be specified for the `on_streaming_backlog_exceeded` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_success",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the `on_success` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "trigger",
    "type": "string",
    "description": "The type of trigger that fired this run.<br /><br />* `PERIODIC`: Schedules that periodically trigger runs, such as a cron scheduler. * `ONE_TIME`:<br />One time triggers that fire a single run. This occurs you triggered a single run on demand<br />through the UI or the API. * `RETRY`: Indicates a run that is triggered as a retry of a<br />previously failed run. This occurs when you request to re-run the job in case of failures. *<br />`RUN_JOB_TASK`: Indicates a run that is triggered using a Run Job task. * `FILE_ARRIVAL`:<br />Indicates a run that is triggered by a file arrival. * `CONTINUOUS`: Indicates a run that is<br />triggered by a continuous job. * `TABLE`: Indicates a run that is triggered by a table update. *<br />`CONTINUOUS_RESTART`: Indicates a run created by user to manually restart a continuous job run.<br />* `MODEL`: Indicates a run that is triggered by a model update."
  },
  {
    "name": "trigger_info",
    "type": "object",
    "description": "Additional details about what triggered the run",
    "children": [
      {
        "name": "run_id",
        "type": "integer",
        "description": "The run id of the Run Job task run"
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": "The id of the usage policy used by this run for cost attribution purposes."
  },
  {
    "name": "job_id",
    "type": "integer",
    "description": "The canonical identifier of the job that contains this run."
  },
  {
    "name": "job_run_id",
    "type": "integer",
    "description": "ID of the job run that this run belongs to. For legacy and single-task job runs the field is populated with the job run ID. For task runs, the field is populated with the ID of the job run that the task run belongs to."
  },
  {
    "name": "original_attempt_run_id",
    "type": "integer",
    "description": "If this run is a retry of a prior run attempt, this field contains the run_id of the original attempt; otherwise, it is the same as the run_id."
  },
  {
    "name": "run_id",
    "type": "integer",
    "description": "The canonical identifier of the run. This ID is unique across all runs of all jobs."
  },
  {
    "name": "creator_user_name",
    "type": "string",
    "description": "The creator user name. This field won’t be included in the response if the user has already been deleted."
  },
  {
    "name": "run_name",
    "type": "string",
    "description": "An optional name for the run. The maximum length is 4096 bytes in UTF-8 encoding."
  },
  {
    "name": "attempt_number",
    "type": "integer",
    "description": ""
  },
  {
    "name": "cleanup_duration",
    "type": "integer",
    "description": "The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `cleanup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
  },
  {
    "name": "cluster_instance",
    "type": "object",
    "description": "The cluster used for this run. If the run is specified to use a new cluster, this field is set once the Jobs service has requested a cluster for the run.",
    "children": [
      {
        "name": "cluster_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "spark_context_id",
        "type": "string",
        "description": "The canonical identifier for the Spark context used by a run. This field is filled in once the run begins execution. This value can be used to view the Spark UI by browsing to `/#setting/sparkui/$cluster_id/$spark_context_id`. The Spark UI continues to be available after the run has completed. The response won’t include this field if the identifier is not available yet."
      }
    ]
  },
  {
    "name": "cluster_spec",
    "type": "object",
    "description": "A snapshot of the job’s cluster specification when this run was created.",
    "children": [
      {
        "name": "existing_cluster_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "job_cluster_key",
        "type": "string",
        "description": "If job_cluster_key, this task is executed reusing the cluster specified in `job.settings.job_clusters`."
      },
      {
        "name": "libraries",
        "type": "string",
        "description": "An optional list of libraries to be installed on the cluster. The default value is an empty list."
      },
      {
        "name": "new_cluster",
        "type": "string",
        "description": "If new_cluster, a description of a new cluster that is created for each run."
      }
    ]
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of the run"
  },
  {
    "name": "effective_performance_target",
    "type": "string",
    "description": "PerformanceTarget defines how performant (lower latency) or cost efficient the execution of run<br />on serverless compute should be. The performance mode on the job or pipeline should map to a<br />performance setting that is passed to Cluster Manager (see cluster-common PerformanceTarget)."
  },
  {
    "name": "end_time",
    "type": "integer",
    "description": "The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running."
  },
  {
    "name": "execution_duration",
    "type": "integer",
    "description": "The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `execution_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
  },
  {
    "name": "git_source",
    "type": "object",
    "description": "An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks. If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task. Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.",
    "children": [
      {
        "name": "git_url",
        "type": "string",
        "description": "URL of the repository to be cloned by this job."
      },
      {
        "name": "git_provider",
        "type": "string",
        "description": "Unique identifier of the service used to host the Git repository. The value is case insensitive."
      },
      {
        "name": "git_branch",
        "type": "string",
        "description": "Name of the branch to be checked out and used by this job. This field cannot be specified in conjunction with git_tag or git_commit."
      },
      {
        "name": "git_commit",
        "type": "string",
        "description": "Commit to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_tag."
      },
      {
        "name": "git_snapshot",
        "type": "object",
        "description": "Read-only state of the remote repository at the time the job was run. This field is only<br />    included on job runs.",
        "children": [
          {
            "name": "used_commit",
            "type": "string",
            "description": "Commit that was used to execute the run. If git_branch was specified, this points to the HEAD of the branch at the time of the run; if git_tag was specified, this points to the commit the tag points to."
          }
        ]
      },
      {
        "name": "git_tag",
        "type": "string",
        "description": "Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_commit."
      },
      {
        "name": "job_source",
        "type": "object",
        "description": "The source of the job specification in the remote repository when the job is source controlled.",
        "children": [
          {
            "name": "job_config_path",
            "type": "string",
            "description": "Path of the job YAML file that contains the job specification."
          },
          {
            "name": "import_from_git_branch",
            "type": "string",
            "description": "Name of the branch which the job is imported from."
          },
          {
            "name": "dirty_state",
            "type": "string",
            "description": "Dirty state indicates the job is not fully synced with the job specification in the remote repository. Possible values are: * `NOT_SYNCED`: The job is not yet synced with the remote job specification. Import the remote job specification from UI to make the job fully synced. * `DISCONNECTED`: The job is temporary disconnected from the remote job specification and is allowed for live edit. Import the remote job specification again from UI to make the job fully synced."
          }
        ]
      }
    ]
  },
  {
    "name": "has_more",
    "type": "boolean",
    "description": "Indicates if the run has more array properties (`tasks`, `job_clusters`) that are not shown. They can be accessed via :method:jobs/getrun endpoint. It is only relevant for API 2.2 :method:jobs/listruns requests with `expand_tasks=true`."
  },
  {
    "name": "job_clusters",
    "type": "array",
    "description": "A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings. If more than 100 job clusters are available, you can paginate through them using :method:jobs/getrun.",
    "children": [
      {
        "name": "job_cluster_key",
        "type": "string",
        "description": ""
      },
      {
        "name": "new_cluster",
        "type": "string",
        "description": "If new_cluster, a description of a cluster that is created for each task."
      }
    ]
  },
  {
    "name": "job_parameters",
    "type": "array",
    "description": "Job-level parameters used in the run",
    "children": [
      {
        "name": "default",
        "type": "string",
        "description": ""
      },
      {
        "name": "name",
        "type": "string",
        "description": "The name of the parameter"
      },
      {
        "name": "value",
        "type": "string",
        "description": "The value used in the run"
      }
    ]
  },
  {
    "name": "number_in_job",
    "type": "integer",
    "description": "A unique identifier for this job run. This is set to the same value as `run_id`."
  },
  {
    "name": "overriding_parameters",
    "type": "object",
    "description": "The parameters used for this run.",
    "children": [
      {
        "name": "dbt_commands",
        "type": "array",
        "description": ""
      },
      {
        "name": "jar_params",
        "type": "array",
        "description": "A list of parameters for jobs with Spark JAR tasks, for example `\"jar_params\": [\"john doe\", \"35\"]`. The parameters are used to invoke the main function of the main class specified in the Spark JAR task. If not specified upon `run-now`, it defaults to an empty list. jar_params cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example `&#123;\"jar_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
      },
      {
        "name": "notebook_params",
        "type": "object",
        "description": "A map from keys to values for jobs with notebook task, for example `\"notebook_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;`. The map is passed to the notebook and is accessible through the [dbutils.widgets.get] function. If not specified upon `run-now`, the triggered run uses the job’s base parameters. notebook_params cannot be specified in conjunction with jar_params. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. The JSON representation of this field (for example `&#123;\"notebook_params\":&#123;\"name\":\"john doe\",\"age\":\"35\"&#125;&#125;`) cannot exceed 10,000 bytes. [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
      },
      {
        "name": "pipeline_params",
        "type": "object",
        "description": "Controls whether the pipeline should perform a full refresh",
        "children": [
          {
            "name": "full_refresh",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "python_named_params",
        "type": "object",
        "description": ""
      },
      {
        "name": "python_params",
        "type": "array",
        "description": "A list of parameters for jobs with Python tasks, for example `\"python_params\": [\"john doe\", \"35\"]`. The parameters are passed to Python file as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `&#123;\"python_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
      },
      {
        "name": "spark_submit_params",
        "type": "array",
        "description": "A list of parameters for jobs with spark submit task, for example `\"spark_submit_params\": [\"--class\", \"org.apache.spark.examples.SparkPi\"]`. The parameters are passed to spark-submit script as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `&#123;\"python_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
      },
      {
        "name": "sql_params",
        "type": "object",
        "description": "A map from keys to values for jobs with SQL task, for example `\"sql_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;`. The SQL alert task does not support custom parameters. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
      }
    ]
  },
  {
    "name": "queue_duration",
    "type": "integer",
    "description": "The time in milliseconds that the run has spent in the queue."
  },
  {
    "name": "repair_history",
    "type": "array",
    "description": "The repair history of the run.",
    "children": [
      {
        "name": "effective_performance_target",
        "type": "string",
        "description": "PerformanceTarget defines how performant (lower latency) or cost efficient the execution of run<br />on serverless compute should be. The performance mode on the job or pipeline should map to a<br />performance setting that is passed to Cluster Manager (see cluster-common PerformanceTarget)."
      },
      {
        "name": "end_time",
        "type": "integer",
        "description": "The end time of the (repaired) run."
      },
      {
        "name": "id",
        "type": "integer",
        "description": "The ID of the repair. Only returned for the items that represent a repair in `repair_history`."
      },
      {
        "name": "start_time",
        "type": "integer",
        "description": "The start time of the (repaired) run."
      },
      {
        "name": "state",
        "type": "object",
        "description": "Deprecated. Please use the `status` field instead.",
        "children": [
          {
            "name": "life_cycle_state",
            "type": "string",
            "description": "A value indicating the run's current lifecycle state. This field is always available in the response. Note: Additional states might be introduced in future releases."
          },
          {
            "name": "queue_reason",
            "type": "string",
            "description": "The reason indicating why the run was queued."
          },
          {
            "name": "result_state",
            "type": "string",
            "description": "A value indicating the run's result. This field is only available for terminal lifecycle states. Note: Additional states might be introduced in future releases."
          },
          {
            "name": "state_message",
            "type": "string",
            "description": "A descriptive message for the current state. This field is unstructured, and its exact format is subject to change."
          },
          {
            "name": "user_cancelled_or_timedout",
            "type": "boolean",
            "description": "A value indicating whether a run was canceled manually by a user or by the scheduler because the run timed out."
          }
        ]
      },
      {
        "name": "status",
        "type": "object",
        "description": "The current status of the run",
        "children": [
          {
            "name": "queue_details",
            "type": "object",
            "description": "If the run was queued, details about the reason for queuing the run.",
            "children": [
              {
                "name": "code",
                "type": "string",
                "description": "The reason for queuing the run. * `ACTIVE_RUNS_LIMIT_REACHED`: The run was queued due to<br />reaching the workspace limit of active task runs. * `MAX_CONCURRENT_RUNS_REACHED`: The run was<br />queued due to reaching the per-job limit of concurrent job runs. *<br />`ACTIVE_RUN_JOB_TASKS_LIMIT_REACHED`: The run was queued due to reaching the workspace limit of<br />active run job tasks."
              },
              {
                "name": "message",
                "type": "string",
                "description": "A descriptive message with the queuing details. This field is unstructured, and its exact format is subject to change."
              }
            ]
          },
          {
            "name": "state",
            "type": "string",
            "description": "The current state of the run."
          },
          {
            "name": "termination_details",
            "type": "object",
            "description": "If the run is in a TERMINATING or TERMINATED state, details about the reason for terminating the run.",
            "children": [
              {
                "name": "code",
                "type": "string",
                "description": "The code indicates why the run was terminated. Additional codes might be introduced in future<br />releases. * `SUCCESS`: The run was completed successfully. * `SUCCESS_WITH_FAILURES`: The run<br />was completed successfully but some child runs failed. * `USER_CANCELED`: The run was<br />successfully canceled during execution by a user. * `CANCELED`: The run was canceled during<br />execution by the Databricks platform; for example, if the maximum run duration was exceeded. *<br />`SKIPPED`: Run was never executed, for example, if the upstream task run failed, the dependency<br />type condition was not met, or there were no material tasks to execute. * `INTERNAL_ERROR`: The<br />run encountered an unexpected error. Refer to the state message for further details. *<br />`DRIVER_ERROR`: The run encountered an error while communicating with the Spark Driver. *<br />`CLUSTER_ERROR`: The run failed due to a cluster error. Refer to the state message for further<br />details. * `REPOSITORY_CHECKOUT_FAILED`: Failed to complete the checkout due to an error when<br />communicating with the third party service. * `INVALID_CLUSTER_REQUEST`: The run failed because<br />it issued an invalid request to start the cluster. * `WORKSPACE_RUN_LIMIT_EXCEEDED`: The<br />workspace has reached the quota for the maximum number of concurrent active runs. Consider<br />scheduling the runs over a larger time frame. * `FEATURE_DISABLED`: The run failed because it<br />tried to access a feature unavailable for the workspace. * `CLUSTER_REQUEST_LIMIT_EXCEEDED`: The<br />number of cluster creation, start, and upsize requests have exceeded the allotted rate limit.<br />Consider spreading the run execution over a larger time frame. * `STORAGE_ACCESS_ERROR`: The run<br />failed due to an error when accessing the customer blob storage. Refer to the state message for<br />further details. * `RUN_EXECUTION_ERROR`: The run was completed with task failures. For more<br />details, refer to the state message or run output. * `UNAUTHORIZED_ERROR`: The run failed due to<br />a permission issue while accessing a resource. Refer to the state message for further details. *<br />`LIBRARY_INSTALLATION_ERROR`: The run failed while installing the user-requested library. Refer<br />to the state message for further details. The causes might include, but are not limited to: The<br />provided library is invalid, there are insufficient permissions to install the library, and so<br />forth. * `MAX_CONCURRENT_RUNS_EXCEEDED`: The scheduled run exceeds the limit of maximum<br />concurrent runs set for the job. * `MAX_SPARK_CONTEXTS_EXCEEDED`: The run is scheduled on a<br />cluster that has already reached the maximum number of contexts it is configured to create. See:<br />[Link]. * `RESOURCE_NOT_FOUND`: A resource necessary for run execution does not exist. Refer to<br />the state message for further details. * `INVALID_RUN_CONFIGURATION`: The run failed due to an<br />invalid configuration. Refer to the state message for further details. * `CLOUD_FAILURE`: The<br />run failed due to a cloud provider issue. Refer to the state message for further details. *<br />`MAX_JOB_QUEUE_SIZE_EXCEEDED`: The run was skipped due to reaching the job level queue size<br />limit. * `DISABLED`: The run was never executed because it was disabled explicitly by the user.<br />* `BREAKING_CHANGE`: Run failed because of an intentional breaking change in Spark, but it will<br />be retried with a mitigation config.<br /><br />[Link]: https://kb.databricks.com/en_US/notebooks/too-many-execution-contexts-are-open-right-now"
              },
              {
                "name": "message",
                "type": "string",
                "description": "A descriptive message with the termination details. This field is unstructured and the format might change."
              },
              {
                "name": "type",
                "type": "string",
                "description": "* `SUCCESS`: The run terminated without any issues * `INTERNAL_ERROR`: An error occurred in the<br />Databricks platform. Please look at the [status page] or contact support if the issue persists.<br />* `CLIENT_ERROR`: The run was terminated because of an error caused by user input or the job<br />configuration. * `CLOUD_FAILURE`: The run was terminated because of an issue with your cloud<br />provider.<br /><br />[status page]: https://status.databricks.com/"
              }
            ]
          }
        ]
      },
      {
        "name": "task_run_ids",
        "type": "array",
        "description": "The run IDs of the task runs that ran as part of this repair history item."
      },
      {
        "name": "type",
        "type": "string",
        "description": "The repair history item type. Indicates whether a run is the original run or a repair run."
      }
    ]
  },
  {
    "name": "run_duration",
    "type": "integer",
    "description": "The time in milliseconds it took the job run and all of its repairs to finish."
  },
  {
    "name": "run_page_url",
    "type": "string",
    "description": "The URL to the detail page of the run."
  },
  {
    "name": "run_type",
    "type": "string",
    "description": "The type of a run. * `JOB_RUN`: Normal job run. A run created with :method:jobs/runNow. *<br />`WORKFLOW_RUN`: Workflow run. A run created with [dbutils.notebook.run]. * `SUBMIT_RUN`: Submit<br />run. A run created with :method:jobs/submit.<br /><br />[dbutils.notebook.run]: https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-workflow"
  },
  {
    "name": "schedule",
    "type": "object",
    "description": "The cron schedule that triggered this run if it was triggered by the periodic scheduler.",
    "children": [
      {
        "name": "quartz_cron_expression",
        "type": "string",
        "description": ""
      },
      {
        "name": "timezone_id",
        "type": "string",
        "description": "A Java timezone ID. The schedule for a job is resolved with respect to this timezone. See [Java TimeZone] for details. This field is required. [Java TimeZone]: https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html"
      },
      {
        "name": "pause_status",
        "type": "string",
        "description": "Indicate whether this schedule is paused or not."
      }
    ]
  },
  {
    "name": "setup_duration",
    "type": "integer",
    "description": "The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `setup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
  },
  {
    "name": "start_time",
    "type": "integer",
    "description": "The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued."
  },
  {
    "name": "state",
    "type": "object",
    "description": "Deprecated. Please use the `status` field instead.",
    "children": [
      {
        "name": "life_cycle_state",
        "type": "string",
        "description": "A value indicating the run's current lifecycle state. This field is always available in the response. Note: Additional states might be introduced in future releases."
      },
      {
        "name": "queue_reason",
        "type": "string",
        "description": "The reason indicating why the run was queued."
      },
      {
        "name": "result_state",
        "type": "string",
        "description": "A value indicating the run's result. This field is only available for terminal lifecycle states. Note: Additional states might be introduced in future releases."
      },
      {
        "name": "state_message",
        "type": "string",
        "description": "A descriptive message for the current state. This field is unstructured, and its exact format is subject to change."
      },
      {
        "name": "user_cancelled_or_timedout",
        "type": "boolean",
        "description": "A value indicating whether a run was canceled manually by a user or by the scheduler because the run timed out."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The current status of the run",
    "children": [
      {
        "name": "queue_details",
        "type": "object",
        "description": "If the run was queued, details about the reason for queuing the run.",
        "children": [
          {
            "name": "code",
            "type": "string",
            "description": "The reason for queuing the run. * `ACTIVE_RUNS_LIMIT_REACHED`: The run was queued due to<br />reaching the workspace limit of active task runs. * `MAX_CONCURRENT_RUNS_REACHED`: The run was<br />queued due to reaching the per-job limit of concurrent job runs. *<br />`ACTIVE_RUN_JOB_TASKS_LIMIT_REACHED`: The run was queued due to reaching the workspace limit of<br />active run job tasks."
          },
          {
            "name": "message",
            "type": "string",
            "description": "A descriptive message with the queuing details. This field is unstructured, and its exact format is subject to change."
          }
        ]
      },
      {
        "name": "state",
        "type": "string",
        "description": "The current state of the run."
      },
      {
        "name": "termination_details",
        "type": "object",
        "description": "If the run is in a TERMINATING or TERMINATED state, details about the reason for terminating the run.",
        "children": [
          {
            "name": "code",
            "type": "string",
            "description": "The code indicates why the run was terminated. Additional codes might be introduced in future<br />releases. * `SUCCESS`: The run was completed successfully. * `SUCCESS_WITH_FAILURES`: The run<br />was completed successfully but some child runs failed. * `USER_CANCELED`: The run was<br />successfully canceled during execution by a user. * `CANCELED`: The run was canceled during<br />execution by the Databricks platform; for example, if the maximum run duration was exceeded. *<br />`SKIPPED`: Run was never executed, for example, if the upstream task run failed, the dependency<br />type condition was not met, or there were no material tasks to execute. * `INTERNAL_ERROR`: The<br />run encountered an unexpected error. Refer to the state message for further details. *<br />`DRIVER_ERROR`: The run encountered an error while communicating with the Spark Driver. *<br />`CLUSTER_ERROR`: The run failed due to a cluster error. Refer to the state message for further<br />details. * `REPOSITORY_CHECKOUT_FAILED`: Failed to complete the checkout due to an error when<br />communicating with the third party service. * `INVALID_CLUSTER_REQUEST`: The run failed because<br />it issued an invalid request to start the cluster. * `WORKSPACE_RUN_LIMIT_EXCEEDED`: The<br />workspace has reached the quota for the maximum number of concurrent active runs. Consider<br />scheduling the runs over a larger time frame. * `FEATURE_DISABLED`: The run failed because it<br />tried to access a feature unavailable for the workspace. * `CLUSTER_REQUEST_LIMIT_EXCEEDED`: The<br />number of cluster creation, start, and upsize requests have exceeded the allotted rate limit.<br />Consider spreading the run execution over a larger time frame. * `STORAGE_ACCESS_ERROR`: The run<br />failed due to an error when accessing the customer blob storage. Refer to the state message for<br />further details. * `RUN_EXECUTION_ERROR`: The run was completed with task failures. For more<br />details, refer to the state message or run output. * `UNAUTHORIZED_ERROR`: The run failed due to<br />a permission issue while accessing a resource. Refer to the state message for further details. *<br />`LIBRARY_INSTALLATION_ERROR`: The run failed while installing the user-requested library. Refer<br />to the state message for further details. The causes might include, but are not limited to: The<br />provided library is invalid, there are insufficient permissions to install the library, and so<br />forth. * `MAX_CONCURRENT_RUNS_EXCEEDED`: The scheduled run exceeds the limit of maximum<br />concurrent runs set for the job. * `MAX_SPARK_CONTEXTS_EXCEEDED`: The run is scheduled on a<br />cluster that has already reached the maximum number of contexts it is configured to create. See:<br />[Link]. * `RESOURCE_NOT_FOUND`: A resource necessary for run execution does not exist. Refer to<br />the state message for further details. * `INVALID_RUN_CONFIGURATION`: The run failed due to an<br />invalid configuration. Refer to the state message for further details. * `CLOUD_FAILURE`: The<br />run failed due to a cloud provider issue. Refer to the state message for further details. *<br />`MAX_JOB_QUEUE_SIZE_EXCEEDED`: The run was skipped due to reaching the job level queue size<br />limit. * `DISABLED`: The run was never executed because it was disabled explicitly by the user.<br />* `BREAKING_CHANGE`: Run failed because of an intentional breaking change in Spark, but it will<br />be retried with a mitigation config.<br /><br />[Link]: https://kb.databricks.com/en_US/notebooks/too-many-execution-contexts-are-open-right-now"
          },
          {
            "name": "message",
            "type": "string",
            "description": "A descriptive message with the termination details. This field is unstructured and the format might change."
          },
          {
            "name": "type",
            "type": "string",
            "description": "* `SUCCESS`: The run terminated without any issues * `INTERNAL_ERROR`: An error occurred in the<br />Databricks platform. Please look at the [status page] or contact support if the issue persists.<br />* `CLIENT_ERROR`: The run was terminated because of an error caused by user input or the job<br />configuration. * `CLOUD_FAILURE`: The run was terminated because of an issue with your cloud<br />provider.<br /><br />[status page]: https://status.databricks.com/"
          }
        ]
      }
    ]
  },
  {
    "name": "tasks",
    "type": "array",
    "description": "The list of tasks performed by the run. Each task has its own `run_id` which you can use to call `JobsGetOutput` to retrieve the run resutls. If more than 100 tasks are available, you can paginate through them using :method:jobs/getrun. Use the `next_page_token` field at the object root to determine if more results are available.",
    "children": [
      {
        "name": "task_key",
        "type": "string",
        "description": "A unique name for the task. This field is used to refer to this task from other tasks. This field is required and must be unique within its parent job. On Update or Reset, this field is used to reference the tasks to be updated or reset."
      },
      {
        "name": "attempt_number",
        "type": "integer",
        "description": "The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt_number of 0. If the initial run attempt fails, and the job has a retry policy (`max_retries` &gt; 0), subsequent runs are created with an `original_attempt_run_id` of the original attempt’s ID and an incrementing `attempt_number`. Runs are retried only until they succeed, and the maximum `attempt_number` is the same as the `max_retries` value for the job."
      },
      {
        "name": "clean_rooms_notebook_task",
        "type": "object",
        "description": "The task runs a [clean rooms] notebook when the `clean_rooms_notebook_task` field is present. [clean rooms]: https://docs.databricks.com/clean-rooms/index.html",
        "children": [
          {
            "name": "clean_room_name",
            "type": "string",
            "description": "The clean room that the notebook belongs to."
          },
          {
            "name": "notebook_name",
            "type": "string",
            "description": "Name of the notebook being run."
          },
          {
            "name": "etag",
            "type": "string",
            "description": "Checksum to validate the freshness of the notebook resource (i.e. the notebook being run is the latest version). It can be fetched by calling the :method:cleanroomassets/get API."
          },
          {
            "name": "notebook_base_parameters",
            "type": "object",
            "description": "Base parameters to be used for the clean room notebook job."
          }
        ]
      },
      {
        "name": "cleanup_duration",
        "type": "integer",
        "description": "The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `cleanup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
      },
      {
        "name": "cluster_instance",
        "type": "object",
        "description": "The cluster used for this run. If the run is specified to use a new cluster, this field is set once the Jobs service has requested a cluster for the run.",
        "children": [
          {
            "name": "cluster_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "spark_context_id",
            "type": "string",
            "description": "The canonical identifier for the Spark context used by a run. This field is filled in once the run begins execution. This value can be used to view the Spark UI by browsing to `/#setting/sparkui/$cluster_id/$spark_context_id`. The Spark UI continues to be available after the run has completed. The response won’t include this field if the identifier is not available yet."
          }
        ]
      },
      {
        "name": "compute",
        "type": "object",
        "description": "Task level compute configuration.",
        "children": [
          {
            "name": "hardware_accelerator",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "condition_task",
        "type": "object",
        "description": "The task evaluates a condition that can be used to control the execution of other tasks when the `condition_task` field is present. The condition task does not require a cluster to execute and does not support retries or notifications.",
        "children": [
          {
            "name": "op",
            "type": "string",
            "description": "* `EQUAL_TO`, `NOT_EQUAL` operators perform string comparison of their operands. This means that<br />`“12.0” == “12”` will evaluate to `false`. * `GREATER_THAN`, `GREATER_THAN_OR_EQUAL`,<br />`LESS_THAN`, `LESS_THAN_OR_EQUAL` operators perform numeric comparison of their operands.<br />`“12.0” >= “12”` will evaluate to `true`, `“10.0” >= “12”` will evaluate to<br />`false`.<br /><br />The boolean comparison to task values can be implemented with operators `EQUAL_TO`, `NOT_EQUAL`.<br />If a task value was set to a boolean value, it will be serialized to `“true”` or<br />`“false”` for the comparison."
          },
          {
            "name": "left",
            "type": "string",
            "description": "The left operand of the condition task. Can be either a string value or a job state or parameter reference."
          },
          {
            "name": "right",
            "type": "string",
            "description": "The right operand of the condition task. Can be either a string value or a job state or parameter reference."
          },
          {
            "name": "outcome",
            "type": "string",
            "description": "The condition expression evaluation result. Filled in if the task was successfully completed. Can be `\"true\"` or `\"false\"`"
          }
        ]
      },
      {
        "name": "dashboard_task",
        "type": "object",
        "description": "The task refreshes a dashboard and sends a snapshot to subscribers.",
        "children": [
          {
            "name": "dashboard_id",
            "type": "string",
            "description": "The identifier of the dashboard to refresh."
          },
          {
            "name": "filters",
            "type": "object",
            "description": "Dashboard task parameters. Used to apply dashboard filter values during dashboard task execution. Parameter values get applied to any dashboard filters that have a matching URL identifier as the parameter key. The parameter value format is dependent on the filter type: - For text and single-select filters, provide a single value (e.g. `\"value\"`) - For date and datetime filters, provide the value in ISO 8601 format (e.g. `\"2000-01-01T00:00:00\"`) - For multi-select filters, provide a JSON array of values (e.g. `\"[\\\"value1\\\",\\\"value2\\\"]\"`) - For range and date range filters, provide a JSON object with `start` and `end` (e.g. `\"&#123;\\\"start\\\":\\\"1\\\",\\\"end\\\":\\\"10\\\"&#125;\"`)"
          },
          {
            "name": "subscription",
            "type": "object",
            "description": "Optional: subscription configuration for sending the dashboard snapshot.",
            "children": [
              {
                "name": "custom_subject",
                "type": "string",
                "description": ""
              },
              {
                "name": "paused",
                "type": "boolean",
                "description": "When true, the subscription will not send emails."
              },
              {
                "name": "subscribers",
                "type": "array",
                "description": "The list of subscribers to send the snapshot of the dashboard to."
              }
            ]
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "Optional: The warehouse id to execute the dashboard with for the schedule. If not specified, the default warehouse of the dashboard will be used."
          }
        ]
      },
      {
        "name": "dbt_cloud_task",
        "type": "object",
        "description": "Task type for dbt cloud, deprecated in favor of the new name dbt_platform_task",
        "children": [
          {
            "name": "connection_resource_name",
            "type": "string",
            "description": "The resource name of the UC connection that authenticates the dbt Cloud for this task"
          },
          {
            "name": "dbt_cloud_job_id",
            "type": "integer",
            "description": "Id of the dbt Cloud job to be triggered"
          }
        ]
      },
      {
        "name": "dbt_platform_task",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "connection_resource_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "dbt_platform_job_id",
            "type": "string",
            "description": "Id of the dbt platform job to be triggered. Specified as a string for maximum compatibility with clients."
          }
        ]
      },
      {
        "name": "dbt_task",
        "type": "object",
        "description": "The task runs one or more dbt commands when the `dbt_task` field is present. The dbt task requires both Databricks SQL and the ability to use a serverless or a pro SQL warehouse.",
        "children": [
          {
            "name": "commands",
            "type": "array",
            "description": ""
          },
          {
            "name": "catalog",
            "type": "string",
            "description": "Optional name of the catalog to use. The value is the top level in the 3-level namespace of Unity Catalog (catalog / schema / relation). The catalog value can only be specified if a warehouse_id is specified. Requires dbt-databricks &gt;= 1.1.1."
          },
          {
            "name": "profiles_directory",
            "type": "string",
            "description": "Optional (relative) path to the profiles directory. Can only be specified if no warehouse_id is specified. If no warehouse_id is specified and this folder is unset, the root directory is used."
          },
          {
            "name": "project_directory",
            "type": "string",
            "description": "Path to the project directory. Optional for Git sourced tasks, in which case if no value is provided, the root of the Git repository is used."
          },
          {
            "name": "schema",
            "type": "string",
            "description": "Optional schema to write to. This parameter is only used when a warehouse_id is also provided. If not provided, the `default` schema is used."
          },
          {
            "name": "source",
            "type": "string",
            "description": "Optional location type of the project directory. When set to `WORKSPACE`, the project will be retrieved from the local Databricks workspace. When set to `GIT`, the project will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Project is located in Databricks workspace. * `GIT`: Project is located in cloud Git provider."
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "ID of the SQL warehouse to connect to. If provided, we automatically generate and provide the profile and connection details to dbt. It can be overridden on a per-command basis by using the `--profiles-dir` command line argument."
          }
        ]
      },
      {
        "name": "depends_on",
        "type": "array",
        "description": "An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete successfully before executing this task. The key is `task_key`, and the value is the name assigned to the dependent task.",
        "children": [
          {
            "name": "task_key",
            "type": "string",
            "description": ""
          },
          {
            "name": "outcome",
            "type": "string",
            "description": "Can only be specified on condition task dependencies. The outcome of the dependent task that must be met for this task to run."
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "An optional description for this task."
      },
      {
        "name": "effective_performance_target",
        "type": "string",
        "description": "The actual performance target used by the serverless run during execution. This can differ from the client-set performance target on the request depending on whether the performance mode is supported by the job type. * `STANDARD`: Enables cost-efficient execution of serverless workloads. * `PERFORMANCE_OPTIMIZED`: Prioritizes fast startup and execution times through rapid scaling and optimized cluster performance."
      },
      {
        "name": "email_notifications",
        "type": "object",
        "description": "An optional set of email addresses notified when the task run begins or completes. The default behavior is to not send any emails.",
        "children": [
          {
            "name": "no_alert_for_skipped_runs",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "on_duration_warning_threshold_exceeded",
            "type": "array",
            "description": "A list of email addresses to be notified when the duration of a run exceeds the threshold specified for the `RUN_DURATION_SECONDS` metric in the `health` field. If no rule for the `RUN_DURATION_SECONDS` metric is specified in the `health` field for the job, notifications are not sent."
          },
          {
            "name": "on_failure",
            "type": "array",
            "description": "A list of email addresses to be notified when a run unsuccessfully completes. A run is considered to have completed unsuccessfully if it ends with an `INTERNAL_ERROR` `life_cycle_state` or a `FAILED`, or `TIMED_OUT` result_state. If this is not specified on job creation, reset, or update the list is empty, and notifications are not sent."
          },
          {
            "name": "on_start",
            "type": "array",
            "description": "A list of email addresses to be notified when a run begins. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent."
          },
          {
            "name": "on_streaming_backlog_exceeded",
            "type": "array",
            "description": "A list of email addresses to notify when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the `health` field using the following metrics: `STREAMING_BACKLOG_BYTES`, `STREAMING_BACKLOG_RECORDS`, `STREAMING_BACKLOG_SECONDS`, or `STREAMING_BACKLOG_FILES`. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes."
          },
          {
            "name": "on_success",
            "type": "array",
            "description": "A list of email addresses to be notified when a run successfully completes. A run is considered to have completed successfully if it ends with a `TERMINATED` `life_cycle_state` and a `SUCCESS` result_state. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent."
          }
        ]
      },
      {
        "name": "end_time",
        "type": "integer",
        "description": "The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running."
      },
      {
        "name": "environment_key",
        "type": "string",
        "description": "The key that references an environment spec in a job. This field is required for Python script, Python wheel and dbt tasks when using serverless compute."
      },
      {
        "name": "execution_duration",
        "type": "integer",
        "description": "The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `execution_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
      },
      {
        "name": "existing_cluster_id",
        "type": "string",
        "description": "If existing_cluster_id, the ID of an existing cluster that is used for all runs. When running jobs or tasks on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs and tasks on new clusters for greater reliability"
      },
      {
        "name": "for_each_task",
        "type": "object",
        "description": "The task executes a nested task for every input provided when the `for_each_task` field is present.",
        "children": [
          {
            "name": "inputs",
            "type": "string",
            "description": ""
          },
          {
            "name": "task",
            "type": "object",
            "description": "Configuration for the task that will be run for each element in the array",
            "children": [
              {
                "name": "task_key",
                "type": "string",
                "description": ""
              },
              {
                "name": "clean_rooms_notebook_task",
                "type": "object",
                "description": "The task runs a [clean rooms] notebook when the `clean_rooms_notebook_task` field is present. [clean rooms]: https://docs.databricks.com/clean-rooms/index.html"
              },
              {
                "name": "compute",
                "type": "object",
                "description": "Task level compute configuration."
              },
              {
                "name": "condition_task",
                "type": "object",
                "description": "The task evaluates a condition that can be used to control the execution of other tasks when the `condition_task` field is present. The condition task does not require a cluster to execute and does not support retries or notifications."
              },
              {
                "name": "dashboard_task",
                "type": "object",
                "description": "The task refreshes a dashboard and sends a snapshot to subscribers."
              },
              {
                "name": "dbt_cloud_task",
                "type": "object",
                "description": "Task type for dbt cloud, deprecated in favor of the new name dbt_platform_task"
              },
              {
                "name": "dbt_platform_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "dbt_task",
                "type": "object",
                "description": "The task runs one or more dbt commands when the `dbt_task` field is present. The dbt task requires both Databricks SQL and the ability to use a serverless or a pro SQL warehouse."
              },
              {
                "name": "depends_on",
                "type": "array",
                "description": "An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete before executing this task. The task will run only if the `run_if` condition is true. The key is `task_key`, and the value is the name assigned to the dependent task."
              },
              {
                "name": "description",
                "type": "string",
                "description": "An optional description for this task."
              },
              {
                "name": "disable_auto_optimization",
                "type": "boolean",
                "description": "An option to disable auto optimization in serverless"
              },
              {
                "name": "disabled",
                "type": "boolean",
                "description": "An optional flag to disable the task. If set to true, the task will not run even if it is part of a job."
              },
              {
                "name": "email_notifications",
                "type": "object",
                "description": "An optional set of email addresses that is notified when runs of this task begin or complete as well as when this task is deleted. The default behavior is to not send any emails."
              },
              {
                "name": "environment_key",
                "type": "string",
                "description": "The key that references an environment spec in a job. This field is required for Python script, Python wheel and dbt tasks when using serverless compute."
              },
              {
                "name": "existing_cluster_id",
                "type": "string",
                "description": "If existing_cluster_id, the ID of an existing cluster that is used for all runs. When running jobs or tasks on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs and tasks on new clusters for greater reliability"
              },
              {
                "name": "for_each_task",
                "type": "object",
                "description": "The task executes a nested task for every input provided when the `for_each_task` field is present."
              },
              {
                "name": "gen_ai_compute_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "health",
                "type": "object",
                "description": "An optional set of health rules that can be defined for this job."
              },
              {
                "name": "job_cluster_key",
                "type": "string",
                "description": "If job_cluster_key, this task is executed reusing the cluster specified in `job.settings.job_clusters`."
              },
              {
                "name": "libraries",
                "type": "string",
                "description": "An optional list of libraries to be installed on the cluster. The default value is an empty list."
              },
              {
                "name": "max_retries",
                "type": "integer",
                "description": "An optional maximum number of times to retry an unsuccessful run. A run is considered to be unsuccessful if it completes with the `FAILED` result_state or `INTERNAL_ERROR` `life_cycle_state`. The value `-1` means to retry indefinitely and the value `0` means to never retry."
              },
              {
                "name": "min_retry_interval_millis",
                "type": "integer",
                "description": "An optional minimal interval in milliseconds between the start of the failed run and the subsequent retry run. The default behavior is that unsuccessful runs are immediately retried."
              },
              {
                "name": "new_cluster",
                "type": "string",
                "description": "If new_cluster, a description of a new cluster that is created for each run."
              },
              {
                "name": "notebook_task",
                "type": "object",
                "description": "The task runs a notebook when the `notebook_task` field is present."
              },
              {
                "name": "notification_settings",
                "type": "object",
                "description": "Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this task."
              },
              {
                "name": "pipeline_task",
                "type": "object",
                "description": "The task triggers a pipeline update when the `pipeline_task` field is present. Only pipelines configured to use triggered more are supported."
              },
              {
                "name": "power_bi_task",
                "type": "object",
                "description": "The task triggers a Power BI semantic model update when the `power_bi_task` field is present."
              },
              {
                "name": "python_wheel_task",
                "type": "object",
                "description": "The task runs a Python wheel when the `python_wheel_task` field is present."
              },
              {
                "name": "retry_on_timeout",
                "type": "boolean",
                "description": "An optional policy to specify whether to retry a job when it times out. The default behavior is to not retry on timeout."
              },
              {
                "name": "run_if",
                "type": "string",
                "description": "An optional value specifying the condition determining whether the task is run once its dependencies have been completed. * `ALL_SUCCESS`: All dependencies have executed and succeeded * `AT_LEAST_ONE_SUCCESS`: At least one dependency has succeeded * `NONE_FAILED`: None of the dependencies have failed and at least one was executed * `ALL_DONE`: All dependencies have been completed * `AT_LEAST_ONE_FAILED`: At least one dependency failed * `ALL_FAILED`: ALl dependencies have failed"
              },
              {
                "name": "run_job_task",
                "type": "object",
                "description": "The task triggers another job when the `run_job_task` field is present."
              },
              {
                "name": "spark_jar_task",
                "type": "object",
                "description": "The task runs a JAR when the `spark_jar_task` field is present."
              },
              {
                "name": "spark_python_task",
                "type": "object",
                "description": "The task runs a Python file when the `spark_python_task` field is present."
              },
              {
                "name": "spark_submit_task",
                "type": "object",
                "description": "(Legacy) The task runs the spark-submit script when the spark_submit_task field is present. Databricks recommends using the spark_jar_task instead; see [Spark Submit task for jobs](/jobs/spark-submit)."
              },
              {
                "name": "sql_task",
                "type": "object",
                "description": "The task runs a SQL query or file, or it refreshes a SQL alert or a legacy SQL dashboard when the `sql_task` field is present."
              },
              {
                "name": "timeout_seconds",
                "type": "integer",
                "description": "An optional timeout applied to each run of this job task. A value of `0` means no timeout."
              },
              {
                "name": "webhook_notifications",
                "type": "object",
                "description": "A collection of system notification IDs to notify when runs of this task begin or complete. The default behavior is to not send any system notifications."
              }
            ]
          },
          {
            "name": "concurrency",
            "type": "integer",
            "description": "An optional maximum allowed number of concurrent runs of the task. Set this value if you want to be able to execute multiple runs of the task concurrently."
          },
          {
            "name": "stats",
            "type": "object",
            "description": "Read only field. Populated for GetRun and ListRuns RPC calls and stores the execution stats of an For each task",
            "children": [
              {
                "name": "error_message_stats",
                "type": "array",
                "description": ""
              },
              {
                "name": "task_run_stats",
                "type": "object",
                "description": "Describes stats of the iteration. Only latest retries are considered."
              }
            ]
          }
        ]
      },
      {
        "name": "gen_ai_compute_task",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "dl_runtime_image",
            "type": "string",
            "description": ""
          },
          {
            "name": "command",
            "type": "string",
            "description": "Command launcher to run the actual script, e.g. bash, python etc."
          },
          {
            "name": "compute",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "num_gpus",
                "type": "integer",
                "description": ""
              },
              {
                "name": "gpu_node_pool_id",
                "type": "string",
                "description": "IDof the GPU pool to use."
              },
              {
                "name": "gpu_type",
                "type": "string",
                "description": "GPU type."
              }
            ]
          },
          {
            "name": "mlflow_experiment_name",
            "type": "string",
            "description": "Optional string containing the name of the MLflow experiment to log the run to. If name is not found, backend will create the mlflow experiment using the name."
          },
          {
            "name": "source",
            "type": "string",
            "description": "Optional location type of the training script. When set to `WORKSPACE`, the script will be retrieved from the local Databricks workspace. When set to `GIT`, the script will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Script is located in Databricks workspace. * `GIT`: Script is located in cloud Git provider."
          },
          {
            "name": "training_script_path",
            "type": "string",
            "description": "The training script file path to be executed. Cloud file URIs (such as dbfs:/, s3:/, adls:/, gcs:/) and workspace paths are supported. For python files stored in the Databricks workspace, the path must be absolute and begin with `/`. For files stored in a remote repository, the path must be relative. This field is required."
          },
          {
            "name": "yaml_parameters",
            "type": "string",
            "description": "Optional string containing model parameters passed to the training script in yaml format. If present, then the content in yaml_parameters_file_path will be ignored."
          },
          {
            "name": "yaml_parameters_file_path",
            "type": "string",
            "description": "Optional path to a YAML file containing model parameters passed to the training script."
          }
        ]
      },
      {
        "name": "git_source",
        "type": "object",
        "description": "An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks. If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task. Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.",
        "children": [
          {
            "name": "git_url",
            "type": "string",
            "description": "URL of the repository to be cloned by this job."
          },
          {
            "name": "git_provider",
            "type": "string",
            "description": "Unique identifier of the service used to host the Git repository. The value is case insensitive."
          },
          {
            "name": "git_branch",
            "type": "string",
            "description": "Name of the branch to be checked out and used by this job. This field cannot be specified in conjunction with git_tag or git_commit."
          },
          {
            "name": "git_commit",
            "type": "string",
            "description": "Commit to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_tag."
          },
          {
            "name": "git_snapshot",
            "type": "object",
            "description": "Read-only state of the remote repository at the time the job was run. This field is only<br />    included on job runs.",
            "children": [
              {
                "name": "used_commit",
                "type": "string",
                "description": "Commit that was used to execute the run. If git_branch was specified, this points to the HEAD of the branch at the time of the run; if git_tag was specified, this points to the commit the tag points to."
              }
            ]
          },
          {
            "name": "git_tag",
            "type": "string",
            "description": "Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_commit."
          },
          {
            "name": "job_source",
            "type": "object",
            "description": "The source of the job specification in the remote repository when the job is source controlled.",
            "children": [
              {
                "name": "job_config_path",
                "type": "string",
                "description": "Path of the job YAML file that contains the job specification."
              },
              {
                "name": "import_from_git_branch",
                "type": "string",
                "description": "Name of the branch which the job is imported from."
              },
              {
                "name": "dirty_state",
                "type": "string",
                "description": "Dirty state indicates the job is not fully synced with the job specification in the remote repository. Possible values are: * `NOT_SYNCED`: The job is not yet synced with the remote job specification. Import the remote job specification from UI to make the job fully synced. * `DISCONNECTED`: The job is temporary disconnected from the remote job specification and is allowed for live edit. Import the remote job specification again from UI to make the job fully synced."
              }
            ]
          }
        ]
      },
      {
        "name": "job_cluster_key",
        "type": "string",
        "description": "If job_cluster_key, this task is executed reusing the cluster specified in `job.settings.job_clusters`."
      },
      {
        "name": "libraries",
        "type": "string",
        "description": "An optional list of libraries to be installed on the cluster. The default value is an empty list."
      },
      {
        "name": "new_cluster",
        "type": "string",
        "description": "If new_cluster, a description of a new cluster that is created for each run."
      },
      {
        "name": "notebook_task",
        "type": "object",
        "description": "The task runs a notebook when the `notebook_task` field is present.",
        "children": [
          {
            "name": "notebook_path",
            "type": "string",
            "description": ""
          },
          {
            "name": "base_parameters",
            "type": "object",
            "description": "Base parameters to be used for each run of this job. If the run is initiated by a call to :method:jobs/run Now with parameters specified, the two parameters maps are merged. If the same key is specified in `base_parameters` and in `run-now`, the value from `run-now` is used. Use [Task parameter variables] to set parameters containing information about job runs. If the notebook takes a parameter that is not specified in the job’s `base_parameters` or the `run-now` override parameters, the default value from the notebook is used. Retrieve these parameters in a notebook using [dbutils.widgets.get]. The JSON representation of this field cannot exceed 1MB. [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-widgets"
          },
          {
            "name": "source",
            "type": "string",
            "description": "Optional location type of the notebook. When set to `WORKSPACE`, the notebook will be retrieved from the local Databricks workspace. When set to `GIT`, the notebook will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Notebook is located in Databricks workspace. * `GIT`: Notebook is located in cloud Git provider."
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "Optional `warehouse_id` to run the notebook on a SQL warehouse. Classic SQL warehouses are NOT supported, please use serverless or pro SQL warehouses. Note that SQL warehouses only support SQL cells; if the notebook contains non-SQL cells, the run will fail."
          }
        ]
      },
      {
        "name": "notification_settings",
        "type": "object",
        "description": "Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this task run.",
        "children": [
          {
            "name": "alert_on_last_attempt",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "no_alert_for_canceled_runs",
            "type": "boolean",
            "description": "If true, do not send notifications to recipients specified in `on_failure` if the run is canceled."
          },
          {
            "name": "no_alert_for_skipped_runs",
            "type": "boolean",
            "description": "If true, do not send notifications to recipients specified in `on_failure` if the run is skipped."
          }
        ]
      },
      {
        "name": "pipeline_task",
        "type": "object",
        "description": "The task triggers a pipeline update when the `pipeline_task` field is present. Only pipelines configured to use triggered more are supported.",
        "children": [
          {
            "name": "pipeline_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "full_refresh",
            "type": "boolean",
            "description": "If true, triggers a full refresh on the delta live table."
          }
        ]
      },
      {
        "name": "power_bi_task",
        "type": "object",
        "description": "The task triggers a Power BI semantic model update when the `power_bi_task` field is present.",
        "children": [
          {
            "name": "connection_resource_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "power_bi_model",
            "type": "object",
            "description": "The semantic model to update",
            "children": [
              {
                "name": "authentication_method",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              },
              {
                "name": "model_name",
                "type": "string",
                "description": "The name of the Power BI model"
              },
              {
                "name": "overwrite_existing",
                "type": "boolean",
                "description": "Whether to overwrite existing Power BI models"
              },
              {
                "name": "storage_mode",
                "type": "string",
                "description": "The default storage mode of the Power BI model"
              },
              {
                "name": "workspace_name",
                "type": "string",
                "description": "The name of the Power BI workspace of the model"
              }
            ]
          },
          {
            "name": "refresh_after_update",
            "type": "boolean",
            "description": "Whether the model should be refreshed after the update"
          },
          {
            "name": "tables",
            "type": "array",
            "description": "The tables to be exported to Power BI",
            "children": [
              {
                "name": "catalog",
                "type": "string",
                "description": ""
              },
              {
                "name": "name",
                "type": "string",
                "description": "The table name in Databricks"
              },
              {
                "name": "schema",
                "type": "string",
                "description": "The schema name in Databricks"
              },
              {
                "name": "storage_mode",
                "type": "string",
                "description": "The Power BI storage mode of the table"
              }
            ]
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "The SQL warehouse ID to use as the Power BI data source"
          }
        ]
      },
      {
        "name": "python_wheel_task",
        "type": "object",
        "description": "The task runs a Python wheel when the `python_wheel_task` field is present.",
        "children": [
          {
            "name": "package_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "entry_point",
            "type": "string",
            "description": "Named entry point to use, if it does not exist in the metadata of the package it executes the function from the package directly using `$packageName.$entryPoint()`"
          },
          {
            "name": "named_parameters",
            "type": "object",
            "description": "Command-line parameters passed to Python wheel task in the form of `[\"--name=task\", \"--data=dbfs:/path/to/data.json\"]`. Leave it empty if `parameters` is not null."
          },
          {
            "name": "parameters",
            "type": "array",
            "description": "Command-line parameters passed to Python wheel task. Leave it empty if `named_parameters` is not null."
          }
        ]
      },
      {
        "name": "queue_duration",
        "type": "integer",
        "description": "The time in milliseconds that the run has spent in the queue."
      },
      {
        "name": "resolved_values",
        "type": "object",
        "description": "Parameter values including resolved references",
        "children": [
          {
            "name": "condition_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "left",
                "type": "string",
                "description": ""
              },
              {
                "name": "right",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "dbt_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "commands",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "notebook_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "base_parameters",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "python_wheel_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "named_parameters",
                "type": "object",
                "description": ""
              },
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "run_job_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "job_parameters",
                "type": "object",
                "description": ""
              },
              {
                "name": "parameters",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "simulation_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "spark_jar_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "spark_python_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "spark_submit_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "sql_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "parameters",
                "type": "object",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "run_duration",
        "type": "integer",
        "description": "The time in milliseconds it took the job run and all of its repairs to finish."
      },
      {
        "name": "run_id",
        "type": "integer",
        "description": "The ID of the task run."
      },
      {
        "name": "run_if",
        "type": "string",
        "description": "An optional value indicating the condition that determines whether the task should be run once its dependencies have been completed. When omitted, defaults to `ALL_SUCCESS`. See :method:jobs/create for a list of possible values."
      },
      {
        "name": "run_job_task",
        "type": "object",
        "description": "The task triggers another job when the `run_job_task` field is present.",
        "children": [
          {
            "name": "job_id",
            "type": "integer",
            "description": ""
          },
          {
            "name": "dbt_commands",
            "type": "array",
            "description": "An array of commands to execute for jobs with the dbt task, for example `\"dbt_commands\": [\"dbt deps\", \"dbt seed\", \"dbt deps\", \"dbt seed\", \"dbt run\"]` ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "jar_params",
            "type": "array",
            "description": "A list of parameters for jobs with Spark JAR tasks, for example `\"jar_params\": [\"john doe\", \"35\"]`. The parameters are used to invoke the main function of the main class specified in the Spark JAR task. If not specified upon `run-now`, it defaults to an empty list. jar_params cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example `&#123;\"jar_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "job_parameters",
            "type": "object",
            "description": "Job-level parameters used to trigger the job."
          },
          {
            "name": "notebook_params",
            "type": "object",
            "description": "A map from keys to values for jobs with notebook task, for example `\"notebook_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;`. The map is passed to the notebook and is accessible through the [dbutils.widgets.get] function. If not specified upon `run-now`, the triggered run uses the job’s base parameters. notebook_params cannot be specified in conjunction with jar_params. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. The JSON representation of this field (for example `&#123;\"notebook_params\":&#123;\"name\":\"john doe\",\"age\":\"35\"&#125;&#125;`) cannot exceed 10,000 bytes. [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "pipeline_params",
            "type": "object",
            "description": "Controls whether the pipeline should perform a full refresh",
            "children": [
              {
                "name": "full_refresh",
                "type": "boolean",
                "description": ""
              }
            ]
          },
          {
            "name": "python_named_params",
            "type": "object",
            "description": ""
          },
          {
            "name": "python_params",
            "type": "array",
            "description": "A list of parameters for jobs with Python tasks, for example `\"python_params\": [\"john doe\", \"35\"]`. The parameters are passed to Python file as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `&#123;\"python_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "spark_submit_params",
            "type": "array",
            "description": "A list of parameters for jobs with spark submit task, for example `\"spark_submit_params\": [\"--class\", \"org.apache.spark.examples.SparkPi\"]`. The parameters are passed to spark-submit script as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example `&#123;\"python_params\":[\"john doe\",\"35\"]&#125;`) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          },
          {
            "name": "sql_params",
            "type": "object",
            "description": "A map from keys to values for jobs with SQL task, for example `\"sql_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;`. The SQL alert task does not support custom parameters. ⚠ **Deprecation note** Use [job parameters] to pass information down to tasks. [job parameters]: https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown"
          }
        ]
      },
      {
        "name": "run_page_url",
        "type": "string",
        "description": ""
      },
      {
        "name": "setup_duration",
        "type": "integer",
        "description": "The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `setup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field."
      },
      {
        "name": "spark_jar_task",
        "type": "object",
        "description": "The task runs a JAR when the `spark_jar_task` field is present.",
        "children": [
          {
            "name": "jar_uri",
            "type": "string",
            "description": ""
          },
          {
            "name": "main_class_name",
            "type": "string",
            "description": "The full name of the class containing the main method to be executed. This class must be contained in a JAR provided as a library. The code must use `SparkContext.getOrCreate` to obtain a Spark context; otherwise, runs of the job fail."
          },
          {
            "name": "parameters",
            "type": "array",
            "description": "Parameters passed to the main method. Use [Task parameter variables] to set parameters containing information about job runs. [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables"
          },
          {
            "name": "run_as_repl",
            "type": "boolean",
            "description": "Deprecated. A value of `false` is no longer supported."
          }
        ]
      },
      {
        "name": "spark_python_task",
        "type": "object",
        "description": "The task runs a Python file when the `spark_python_task` field is present.",
        "children": [
          {
            "name": "python_file",
            "type": "string",
            "description": ""
          },
          {
            "name": "parameters",
            "type": "array",
            "description": "Command line parameters passed to the Python file. Use [Task parameter variables] to set parameters containing information about job runs. [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables"
          },
          {
            "name": "source",
            "type": "string",
            "description": "Optional location type of the Python file. When set to `WORKSPACE` or not specified, the file will be retrieved from the local Databricks workspace or cloud location (if the `python_file` has a URI format). When set to `GIT`, the Python file will be retrieved from a Git repository defined in `git_source`. * `WORKSPACE`: The Python file is located in a Databricks workspace or at a cloud filesystem URI. * `GIT`: The Python file is located in a remote Git repository."
          }
        ]
      },
      {
        "name": "spark_submit_task",
        "type": "object",
        "description": "(Legacy) The task runs the spark-submit script when the spark_submit_task field is present. Databricks recommends using the spark_jar_task instead; see [Spark Submit task for jobs](/jobs/spark-submit).",
        "children": [
          {
            "name": "parameters",
            "type": "array",
            "description": ""
          }
        ]
      },
      {
        "name": "sql_task",
        "type": "object",
        "description": "The task runs a SQL query or file, or it refreshes a SQL alert or a legacy SQL dashboard when the `sql_task` field is present.",
        "children": [
          {
            "name": "warehouse_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "alert",
            "type": "object",
            "description": "If alert, indicates that this job must refresh a SQL alert.",
            "children": [
              {
                "name": "alert_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "pause_subscriptions",
                "type": "boolean",
                "description": "If true, the alert notifications are not sent to subscribers."
              },
              {
                "name": "subscriptions",
                "type": "array",
                "description": "If specified, alert notifications are sent to subscribers."
              }
            ]
          },
          {
            "name": "dashboard",
            "type": "object",
            "description": "If dashboard, indicates that this job must refresh a SQL dashboard.",
            "children": [
              {
                "name": "dashboard_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "custom_subject",
                "type": "string",
                "description": "Subject of the email sent to subscribers of this task."
              },
              {
                "name": "pause_subscriptions",
                "type": "boolean",
                "description": "If true, the dashboard snapshot is not taken, and emails are not sent to subscribers."
              },
              {
                "name": "subscriptions",
                "type": "array",
                "description": "If specified, dashboard snapshots are sent to subscriptions."
              }
            ]
          },
          {
            "name": "file",
            "type": "object",
            "description": "If file, indicates that this job runs a SQL file in a remote Git repository.",
            "children": [
              {
                "name": "path",
                "type": "string",
                "description": ""
              },
              {
                "name": "source",
                "type": "string",
                "description": "Optional location type of the SQL file. When set to `WORKSPACE`, the SQL file will be retrieved from the local Databricks workspace. When set to `GIT`, the SQL file will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: SQL file is located in Databricks workspace. * `GIT`: SQL file is located in cloud Git provider."
              }
            ]
          },
          {
            "name": "parameters",
            "type": "object",
            "description": "Parameters to be used for each run of this job. The SQL alert task does not support custom parameters."
          },
          {
            "name": "query",
            "type": "object",
            "description": "If query, indicates that this job must execute a SQL query.",
            "children": [
              {
                "name": "query_id",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "start_time",
        "type": "integer",
        "description": "The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued."
      },
      {
        "name": "state",
        "type": "object",
        "description": "Deprecated. Please use the `status` field instead.",
        "children": [
          {
            "name": "life_cycle_state",
            "type": "string",
            "description": "A value indicating the run's current lifecycle state. This field is always available in the response. Note: Additional states might be introduced in future releases."
          },
          {
            "name": "queue_reason",
            "type": "string",
            "description": "The reason indicating why the run was queued."
          },
          {
            "name": "result_state",
            "type": "string",
            "description": "A value indicating the run's result. This field is only available for terminal lifecycle states. Note: Additional states might be introduced in future releases."
          },
          {
            "name": "state_message",
            "type": "string",
            "description": "A descriptive message for the current state. This field is unstructured, and its exact format is subject to change."
          },
          {
            "name": "user_cancelled_or_timedout",
            "type": "boolean",
            "description": "A value indicating whether a run was canceled manually by a user or by the scheduler because the run timed out."
          }
        ]
      },
      {
        "name": "status",
        "type": "object",
        "description": "The current status of the run",
        "children": [
          {
            "name": "queue_details",
            "type": "object",
            "description": "If the run was queued, details about the reason for queuing the run.",
            "children": [
              {
                "name": "code",
                "type": "string",
                "description": "The reason for queuing the run. * `ACTIVE_RUNS_LIMIT_REACHED`: The run was queued due to<br />reaching the workspace limit of active task runs. * `MAX_CONCURRENT_RUNS_REACHED`: The run was<br />queued due to reaching the per-job limit of concurrent job runs. *<br />`ACTIVE_RUN_JOB_TASKS_LIMIT_REACHED`: The run was queued due to reaching the workspace limit of<br />active run job tasks."
              },
              {
                "name": "message",
                "type": "string",
                "description": "A descriptive message with the queuing details. This field is unstructured, and its exact format is subject to change."
              }
            ]
          },
          {
            "name": "state",
            "type": "string",
            "description": "The current state of the run."
          },
          {
            "name": "termination_details",
            "type": "object",
            "description": "If the run is in a TERMINATING or TERMINATED state, details about the reason for terminating the run.",
            "children": [
              {
                "name": "code",
                "type": "string",
                "description": "The code indicates why the run was terminated. Additional codes might be introduced in future<br />releases. * `SUCCESS`: The run was completed successfully. * `SUCCESS_WITH_FAILURES`: The run<br />was completed successfully but some child runs failed. * `USER_CANCELED`: The run was<br />successfully canceled during execution by a user. * `CANCELED`: The run was canceled during<br />execution by the Databricks platform; for example, if the maximum run duration was exceeded. *<br />`SKIPPED`: Run was never executed, for example, if the upstream task run failed, the dependency<br />type condition was not met, or there were no material tasks to execute. * `INTERNAL_ERROR`: The<br />run encountered an unexpected error. Refer to the state message for further details. *<br />`DRIVER_ERROR`: The run encountered an error while communicating with the Spark Driver. *<br />`CLUSTER_ERROR`: The run failed due to a cluster error. Refer to the state message for further<br />details. * `REPOSITORY_CHECKOUT_FAILED`: Failed to complete the checkout due to an error when<br />communicating with the third party service. * `INVALID_CLUSTER_REQUEST`: The run failed because<br />it issued an invalid request to start the cluster. * `WORKSPACE_RUN_LIMIT_EXCEEDED`: The<br />workspace has reached the quota for the maximum number of concurrent active runs. Consider<br />scheduling the runs over a larger time frame. * `FEATURE_DISABLED`: The run failed because it<br />tried to access a feature unavailable for the workspace. * `CLUSTER_REQUEST_LIMIT_EXCEEDED`: The<br />number of cluster creation, start, and upsize requests have exceeded the allotted rate limit.<br />Consider spreading the run execution over a larger time frame. * `STORAGE_ACCESS_ERROR`: The run<br />failed due to an error when accessing the customer blob storage. Refer to the state message for<br />further details. * `RUN_EXECUTION_ERROR`: The run was completed with task failures. For more<br />details, refer to the state message or run output. * `UNAUTHORIZED_ERROR`: The run failed due to<br />a permission issue while accessing a resource. Refer to the state message for further details. *<br />`LIBRARY_INSTALLATION_ERROR`: The run failed while installing the user-requested library. Refer<br />to the state message for further details. The causes might include, but are not limited to: The<br />provided library is invalid, there are insufficient permissions to install the library, and so<br />forth. * `MAX_CONCURRENT_RUNS_EXCEEDED`: The scheduled run exceeds the limit of maximum<br />concurrent runs set for the job. * `MAX_SPARK_CONTEXTS_EXCEEDED`: The run is scheduled on a<br />cluster that has already reached the maximum number of contexts it is configured to create. See:<br />[Link]. * `RESOURCE_NOT_FOUND`: A resource necessary for run execution does not exist. Refer to<br />the state message for further details. * `INVALID_RUN_CONFIGURATION`: The run failed due to an<br />invalid configuration. Refer to the state message for further details. * `CLOUD_FAILURE`: The<br />run failed due to a cloud provider issue. Refer to the state message for further details. *<br />`MAX_JOB_QUEUE_SIZE_EXCEEDED`: The run was skipped due to reaching the job level queue size<br />limit. * `DISABLED`: The run was never executed because it was disabled explicitly by the user.<br />* `BREAKING_CHANGE`: Run failed because of an intentional breaking change in Spark, but it will<br />be retried with a mitigation config.<br /><br />[Link]: https://kb.databricks.com/en_US/notebooks/too-many-execution-contexts-are-open-right-now"
              },
              {
                "name": "message",
                "type": "string",
                "description": "A descriptive message with the termination details. This field is unstructured and the format might change."
              },
              {
                "name": "type",
                "type": "string",
                "description": "* `SUCCESS`: The run terminated without any issues * `INTERNAL_ERROR`: An error occurred in the<br />Databricks platform. Please look at the [status page] or contact support if the issue persists.<br />* `CLIENT_ERROR`: The run was terminated because of an error caused by user input or the job<br />configuration. * `CLOUD_FAILURE`: The run was terminated because of an issue with your cloud<br />provider.<br /><br />[status page]: https://status.databricks.com/"
              }
            ]
          }
        ]
      },
      {
        "name": "timeout_seconds",
        "type": "integer",
        "description": "An optional timeout applied to each run of this job task. A value of `0` means no timeout."
      },
      {
        "name": "webhook_notifications",
        "type": "object",
        "description": "A collection of system notification IDs to notify when the run begins or completes. The default behavior is to not send any system notifications. Task webhooks respect the task notification settings.",
        "children": [
          {
            "name": "on_duration_warning_threshold_exceeded",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_failure",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the `on_failure` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_start",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the `on_start` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_streaming_backlog_exceeded",
            "type": "array",
            "description": "An optional list of system notification IDs to call when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the `health` field using the following metrics: `STREAMING_BACKLOG_BYTES`, `STREAMING_BACKLOG_RECORDS`, `STREAMING_BACKLOG_SECONDS`, or `STREAMING_BACKLOG_FILES`. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes. A maximum of 3 destinations can be specified for the `on_streaming_backlog_exceeded` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_success",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the `on_success` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "trigger",
    "type": "string",
    "description": "The type of trigger that fired this run.<br /><br />* `PERIODIC`: Schedules that periodically trigger runs, such as a cron scheduler. * `ONE_TIME`:<br />One time triggers that fire a single run. This occurs you triggered a single run on demand<br />through the UI or the API. * `RETRY`: Indicates a run that is triggered as a retry of a<br />previously failed run. This occurs when you request to re-run the job in case of failures. *<br />`RUN_JOB_TASK`: Indicates a run that is triggered using a Run Job task. * `FILE_ARRIVAL`:<br />Indicates a run that is triggered by a file arrival. * `CONTINUOUS`: Indicates a run that is<br />triggered by a continuous job. * `TABLE`: Indicates a run that is triggered by a table update. *<br />`CONTINUOUS_RESTART`: Indicates a run created by user to manually restart a continuous job run.<br />* `MODEL`: Indicates a run that is triggered by a model update."
  },
  {
    "name": "trigger_info",
    "type": "object",
    "description": "Additional details about what triggered the run",
    "children": [
      {
        "name": "run_id",
        "type": "integer",
        "description": "The run id of the Run Job task run"
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
    <td><a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_history"><code>include_history</code></a>, <a href="#parameter-include_resolved_values"><code>include_resolved_values</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Retrieves the metadata of a run.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-active_only"><code>active_only</code></a>, <a href="#parameter-completed_only"><code>completed_only</code></a>, <a href="#parameter-expand_tasks"><code>expand_tasks</code></a>, <a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-run_type"><code>run_type</code></a>, <a href="#parameter-start_time_from"><code>start_time_from</code></a>, <a href="#parameter-start_time_to"><code>start_time_to</code></a></td>
    <td>List runs in descending order by start time.</td>
</tr>
<tr>
    <td><a href="#submit"><CopyableCode code="submit" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Submit a one-time run. This endpoint allows you to submit a workload directly without creating a job.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a non-active run. Returns an error if the run is active.</td>
</tr>
<tr>
    <td><a href="#cancel_all"><CopyableCode code="cancel_all" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new runs</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a></td>
    <td></td>
    <td>Cancels a job run or a task run. The run is canceled asynchronously, so it may still be running when</td>
</tr>
<tr>
    <td><a href="#export"><CopyableCode code="export" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-views_to_export"><code>views_to_export</code></a></td>
    <td>Export and retrieve the job run task.</td>
</tr>
<tr>
    <td><a href="#repair"><CopyableCode code="repair" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a></td>
    <td></td>
    <td>Re-run one or more tasks. Tasks are re-run as part of the original job run. They use the current job</td>
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
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>integer</code></td>
    <td>The canonical identifier for the run. This field is required.</td>
</tr>
<tr id="parameter-active_only">
    <td><CopyableCode code="active_only" /></td>
    <td><code>string</code></td>
    <td>If active_only is `true`, only active runs are included in the results; otherwise, lists both active and completed runs. An active run is a run in the `QUEUED`, `PENDING`, `RUNNING`, or `TERMINATING`. This field cannot be `true` when completed_only is `true`.</td>
</tr>
<tr id="parameter-completed_only">
    <td><CopyableCode code="completed_only" /></td>
    <td><code>string</code></td>
    <td>If completed_only is `true`, only completed runs are included in the results; otherwise, lists both active and completed runs. This field cannot be `true` when active_only is `true`.</td>
</tr>
<tr id="parameter-expand_tasks">
    <td><CopyableCode code="expand_tasks" /></td>
    <td><code>string</code></td>
    <td>Whether to include task and cluster details in the response. Note that only the first 100 elements will be shown. Use :method:jobs/getrun to paginate through all tasks and clusters.</td>
</tr>
<tr id="parameter-include_history">
    <td><CopyableCode code="include_history" /></td>
    <td><code>string</code></td>
    <td>Whether to include the repair history in the response.</td>
</tr>
<tr id="parameter-include_resolved_values">
    <td><CopyableCode code="include_resolved_values" /></td>
    <td><code>string</code></td>
    <td>Whether to include resolved parameter values in the response.</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>The job for which to list runs. If omitted, the Jobs service lists runs from all jobs.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>string</code></td>
    <td>The number of runs to return. This value must be greater than 0 and less than 25. The default value is 20. If a request specifies a limit of 0, the service instead uses the maximum limit.</td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>string</code></td>
    <td>The offset of the first run to return, relative to the most recent run. Deprecated since June 2023. Use `page_token` to iterate through the pages instead.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Use `next_page_token` or `prev_page_token` returned from the previous request to list the next or previous page of runs respectively.</td>
</tr>
<tr id="parameter-run_type">
    <td><CopyableCode code="run_type" /></td>
    <td><code>string</code></td>
    <td>The type of runs to return. For a description of run types, see :method:jobs/getRun.</td>
</tr>
<tr id="parameter-start_time_from">
    <td><CopyableCode code="start_time_from" /></td>
    <td><code>string</code></td>
    <td>Show runs that started _at or after_ this value. The value must be a UTC timestamp in milliseconds. Can be combined with _start_time_to_ to filter by a time range.</td>
</tr>
<tr id="parameter-start_time_to">
    <td><CopyableCode code="start_time_to" /></td>
    <td><code>string</code></td>
    <td>Show runs that started _at or before_ this value. The value must be a UTC timestamp in milliseconds. Can be combined with _start_time_from_ to filter by a time range.</td>
</tr>
<tr id="parameter-views_to_export">
    <td><CopyableCode code="views_to_export" /></td>
    <td><code>string</code></td>
    <td>Which views to export (CODE, DASHBOARDS, or ALL). Defaults to CODE.</td>
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

Retrieves the metadata of a run.

```sql
SELECT
effective_usage_policy_id,
job_id,
job_run_id,
original_attempt_run_id,
run_id,
creator_user_name,
run_name,
attempt_number,
cleanup_duration,
cluster_instance,
cluster_spec,
description,
effective_performance_target,
end_time,
execution_duration,
git_source,
has_more,
iterations,
job_clusters,
job_parameters,
next_page_token,
number_in_job,
overriding_parameters,
queue_duration,
repair_history,
run_duration,
run_page_url,
run_type,
schedule,
setup_duration,
start_time,
state,
status,
tasks,
trigger,
trigger_info
FROM databricks_workspace.jobs.job_runs
WHERE run_id = '{{ run_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_history = '{{ include_history }}'
AND include_resolved_values = '{{ include_resolved_values }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="list">

List runs in descending order by start time.

```sql
SELECT
effective_usage_policy_id,
job_id,
job_run_id,
original_attempt_run_id,
run_id,
creator_user_name,
run_name,
attempt_number,
cleanup_duration,
cluster_instance,
cluster_spec,
description,
effective_performance_target,
end_time,
execution_duration,
git_source,
has_more,
job_clusters,
job_parameters,
number_in_job,
overriding_parameters,
queue_duration,
repair_history,
run_duration,
run_page_url,
run_type,
schedule,
setup_duration,
start_time,
state,
status,
tasks,
trigger,
trigger_info
FROM databricks_workspace.jobs.job_runs
WHERE deployment_name = '{{ deployment_name }}' -- required
AND active_only = '{{ active_only }}'
AND completed_only = '{{ completed_only }}'
AND expand_tasks = '{{ expand_tasks }}'
AND job_id = '{{ job_id }}'
AND limit = '{{ limit }}'
AND offset = '{{ offset }}'
AND page_token = '{{ page_token }}'
AND run_type = '{{ run_type }}'
AND start_time_from = '{{ start_time_from }}'
AND start_time_to = '{{ start_time_to }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="submit"
    values={[
        { label: 'submit', value: 'submit' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="submit">

Submit a one-time run. This endpoint allows you to submit a workload directly without creating a job.

```sql
INSERT INTO databricks_workspace.jobs.job_runs (
data__access_control_list,
data__budget_policy_id,
data__email_notifications,
data__environments,
data__git_source,
data__health,
data__idempotency_token,
data__notification_settings,
data__queue,
data__run_as,
data__run_name,
data__tasks,
data__timeout_seconds,
data__usage_policy_id,
data__webhook_notifications,
deployment_name
)
SELECT 
'{{ access_control_list }}',
'{{ budget_policy_id }}',
'{{ email_notifications }}',
'{{ environments }}',
'{{ git_source }}',
'{{ health }}',
'{{ idempotency_token }}',
'{{ notification_settings }}',
'{{ queue }}',
'{{ run_as }}',
'{{ run_name }}',
'{{ tasks }}',
'{{ timeout_seconds }}',
'{{ usage_policy_id }}',
'{{ webhook_notifications }}',
'{{ deployment_name }}'
RETURNING
effective_usage_policy_id,
job_id,
job_run_id,
original_attempt_run_id,
run_id,
creator_user_name,
run_name,
attempt_number,
cleanup_duration,
cluster_instance,
cluster_spec,
description,
effective_performance_target,
end_time,
execution_duration,
git_source,
has_more,
iterations,
job_clusters,
job_parameters,
next_page_token,
number_in_job,
overriding_parameters,
queue_duration,
repair_history,
run_duration,
run_page_url,
run_type,
schedule,
setup_duration,
start_time,
state,
status,
tasks,
trigger,
trigger_info
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: job_runs
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the job_runs resource.
    - name: access_control_list
      value: string
      description: |
        List of permissions to set on the job.
    - name: budget_policy_id
      value: string
      description: |
        The user specified id of the budget policy to use for this one-time run. If not specified, the run will be not be attributed to any budget policy.
    - name: email_notifications
      value: string
      description: |
        An optional set of email addresses notified when the run begins or completes.
    - name: environments
      value: string
      description: |
        A list of task execution environment specifications that can be referenced by tasks of this run.
    - name: git_source
      value: string
      description: |
        An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks. If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task. Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.
    - name: health
      value: string
      description: |
        :param idempotency_token: str (optional) An optional token that can be used to guarantee the idempotency of job run requests. If a run with the provided token already exists, the request does not create a new run but returns the ID of the existing run instead. If a run with the provided token is deleted, an error is returned. If you specify the idempotency token, upon failure you can retry until the request succeeds. Databricks guarantees that exactly one run is launched with that idempotency token. This token must have at most 64 characters. For more information, see [How to ensure idempotency for jobs]. [How to ensure idempotency for jobs]: https://kb.databricks.com/jobs/jobs-idempotency.html
    - name: idempotency_token
      value: string
    - name: notification_settings
      value: string
      description: |
        Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this run.
    - name: queue
      value: string
      description: |
        The queue settings of the one-time run.
    - name: run_as
      value: string
      description: |
        Specifies the user or service principal that the job runs as. If not specified, the job runs as the user who submits the request.
    - name: run_name
      value: string
      description: |
        An optional name for the run. The default value is `Untitled`.
    - name: tasks
      value: string
      description: |
        :param timeout_seconds: int (optional) An optional timeout applied to each run of this job. A value of `0` means no timeout.
    - name: timeout_seconds
      value: string
    - name: usage_policy_id
      value: string
      description: |
        The user specified id of the usage policy to use for this one-time run. If not specified, a default usage policy may be applied when creating or modifying the job.
    - name: webhook_notifications
      value: string
      description: |
        A collection of system notification IDs to notify when the run begins or completes.
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

Deletes a non-active run. Returns an error if the run is active.

```sql
DELETE FROM databricks_workspace.jobs.job_runs
WHERE deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel_all"
    values={[
        { label: 'cancel_all', value: 'cancel_all' },
        { label: 'cancel', value: 'cancel' },
        { label: 'export', value: 'export' },
        { label: 'repair', value: 'repair' }
    ]}
>
<TabItem value="cancel_all">

Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new runs

```sql
EXEC databricks_workspace.jobs.job_runs.cancel_all 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"all_queued_runs": "{{ all_queued_runs }}", 
"job_id": "{{ job_id }}"
}'
;
```
</TabItem>
<TabItem value="cancel">

Cancels a job run or a task run. The run is canceled asynchronously, so it may still be running when

```sql
EXEC databricks_workspace.jobs.job_runs.cancel 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": {{ run_id }}
}'
;
```
</TabItem>
<TabItem value="export">

Export and retrieve the job run task.

```sql
EXEC databricks_workspace.jobs.job_runs.export 
@run_id='{{ run_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@views_to_export='{{ views_to_export }}'
;
```
</TabItem>
<TabItem value="repair">

Re-run one or more tasks. Tasks are re-run as part of the original job run. They use the current job

```sql
EXEC databricks_workspace.jobs.job_runs.repair 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": {{ run_id }}, 
"dbt_commands": "{{ dbt_commands }}", 
"jar_params": "{{ jar_params }}", 
"job_parameters": "{{ job_parameters }}", 
"latest_repair_id": "{{ latest_repair_id }}", 
"notebook_params": "{{ notebook_params }}", 
"performance_target": "{{ performance_target }}", 
"pipeline_params": "{{ pipeline_params }}", 
"python_named_params": "{{ python_named_params }}", 
"python_params": "{{ python_params }}", 
"rerun_all_failed_tasks": "{{ rerun_all_failed_tasks }}", 
"rerun_dependent_tasks": "{{ rerun_dependent_tasks }}", 
"rerun_tasks": "{{ rerun_tasks }}", 
"spark_submit_params": "{{ spark_submit_params }}", 
"sql_params": "{{ sql_params }}"
}'
;
```
</TabItem>
</Tabs>

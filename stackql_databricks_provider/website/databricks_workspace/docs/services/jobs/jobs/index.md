---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.jobs.jobs" /></td></tr>
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
    "name": "effective_budget_policy_id",
    "type": "string",
    "description": "The id of the budget policy used by this job for cost attribution purposes. This may be set through (in order of precedence): 1. Budget admins through the account or workspace console 2. Jobs UI in the job details page and Jobs API using `budget_policy_id` 3. Inferred default based on accessible budget policies of the run_as identity on job creation or modification."
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": "The id of the usage policy used by this job for cost attribution purposes."
  },
  {
    "name": "job_id",
    "type": "integer",
    "description": "The canonical identifier for this job."
  },
  {
    "name": "creator_user_name",
    "type": "string",
    "description": "The creator user name. This field won’t be included in the response if the user has already been deleted."
  },
  {
    "name": "run_as_user_name",
    "type": "string",
    "description": "The email of an active workspace user or the application ID of a service principal that the job runs as. This value can be changed by setting the `run_as` field when creating or updating a job. By default, `run_as_user_name` is based on the current job settings and is set to the creator of the job if job access control is disabled or to the user with the `is_owner` permission if job access control is enabled."
  },
  {
    "name": "created_time",
    "type": "integer",
    "description": "The time at which this job was created in epoch milliseconds (milliseconds since 1/1/1970 UTC)."
  },
  {
    "name": "has_more",
    "type": "boolean",
    "description": "Indicates if the job has more array properties (`tasks`, `job_clusters`) that are not shown. They can be accessed via :method:jobs/get endpoint. It is only relevant for API 2.2 :method:jobs/list requests with `expand_tasks=true`."
  },
  {
    "name": "next_page_token",
    "type": "string",
    "description": "A token that can be used to list the next page of array properties."
  },
  {
    "name": "settings",
    "type": "object",
    "description": "Settings for this job and all of its runs. These settings can be updated using the `resetJob` method.",
    "children": [
      {
        "name": "budget_policy_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "continuous",
        "type": "object",
        "description": "An optional continuous property for this job. The continuous property will ensure that there is always one run executing. Only one of `schedule` and `continuous` can be used.",
        "children": [
          {
            "name": "pause_status",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (PAUSED, UNPAUSED)"
          },
          {
            "name": "task_retry_mode",
            "type": "string",
            "description": "Indicate whether the continuous job is applying task level retries or not. Defaults to NEVER. (NEVER, ON_FAILURE)"
          }
        ]
      },
      {
        "name": "deployment",
        "type": "object",
        "description": "Deployment information for jobs managed by external sources.",
        "children": [
          {
            "name": "kind",
            "type": "string",
            "description": "* `BUNDLE`: The job is managed by Databricks Asset Bundle. * `SYSTEM_MANAGED`: The job is<br />managed by Databricks and is read-only. (BUNDLE, SYSTEM_MANAGED)"
          },
          {
            "name": "metadata_file_path",
            "type": "string",
            "description": "Path of the file that contains deployment metadata."
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "An optional description for the job. The maximum length is 27700 characters in UTF-8 encoding."
      },
      {
        "name": "edit_mode",
        "type": "string",
        "description": "Edit mode of the job. * `UI_LOCKED`: The job is in a locked UI state and cannot be modified. * `EDITABLE`: The job is in an editable state and can be modified. (EDITABLE, UI_LOCKED)"
      },
      {
        "name": "email_notifications",
        "type": "object",
        "description": "An optional set of email addresses that is notified when runs of this job begin or complete as well as when this job is deleted.",
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
        "name": "environments",
        "type": "array",
        "description": "A list of task execution environment specifications that can be referenced by serverless tasks of this job. For serverless notebook tasks, if the environment_key is not specified, the notebook environment will be used if present. If a jobs environment is specified, it will override the notebook environment. For other serverless tasks, the task environment is required to be specified using environment_key in the task settings.",
        "children": [
          {
            "name": "environment_key",
            "type": "string",
            "description": ""
          },
          {
            "name": "spec",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "format",
        "type": "string",
        "description": "Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to `\"MULTI_TASK\"`. (MULTI_TASK, SINGLE_TASK)"
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
            "description": "Unique identifier of the service used to host the Git repository. The value is case insensitive. (awsCodeCommit, azureDevOpsServices, bitbucketCloud, bitbucketServer, gitHub, gitHubEnterprise, gitLab, gitLabEnterpriseEdition)"
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
                "description": "Dirty state indicates the job is not fully synced with the job specification in the remote repository. Possible values are: * `NOT_SYNCED`: The job is not yet synced with the remote job specification. Import the remote job specification from UI to make the job fully synced. * `DISCONNECTED`: The job is temporary disconnected from the remote job specification and is allowed for live edit. Import the remote job specification again from UI to make the job fully synced. (DISCONNECTED, NOT_SYNCED)"
              }
            ]
          }
        ]
      },
      {
        "name": "health",
        "type": "object",
        "description": "An optional set of health rules that can be defined for this job.",
        "children": [
          {
            "name": "rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "metric",
                "type": "string",
                "description": "Specifies the health metric that is being evaluated for a particular health rule.<br /><br />* `RUN_DURATION_SECONDS`: Expected total time for a run in seconds. * `STREAMING_BACKLOG_BYTES`:<br />An estimate of the maximum bytes of data waiting to be consumed across all streams. This metric<br />is in Public Preview. * `STREAMING_BACKLOG_RECORDS`: An estimate of the maximum offset lag<br />across all streams. This metric is in Public Preview. * `STREAMING_BACKLOG_SECONDS`: An estimate<br />of the maximum consumer delay across all streams. This metric is in Public Preview. *<br />`STREAMING_BACKLOG_FILES`: An estimate of the maximum number of outstanding files across all<br />streams. This metric is in Public Preview. (RUN_DURATION_SECONDS, STREAMING_BACKLOG_BYTES, STREAMING_BACKLOG_FILES, STREAMING_BACKLOG_RECORDS, STREAMING_BACKLOG_SECONDS)"
              },
              {
                "name": "op",
                "type": "string",
                "description": "Specifies the operator used to compare the health metric value with the specified threshold. (GREATER_THAN)"
              },
              {
                "name": "value",
                "type": "integer",
                "description": "Specifies the threshold value that the health metric should obey to satisfy the health rule."
              }
            ]
          }
        ]
      },
      {
        "name": "job_clusters",
        "type": "array",
        "description": "A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.",
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
        "name": "max_concurrent_runs",
        "type": "integer",
        "description": "An optional maximum allowed number of concurrent runs of the job. Set this value if you want to be able to execute multiple runs of the same job concurrently. This is useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each other, or if you want to trigger multiple runs which differ by their input parameters. This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs. However, from then on, new runs are skipped unless there are fewer than 3 active runs. This value cannot exceed 1000. Setting this value to `0` causes all new runs to be skipped."
      },
      {
        "name": "name",
        "type": "string",
        "description": "An optional name for the job. The maximum length is 4096 bytes in UTF-8 encoding."
      },
      {
        "name": "notification_settings",
        "type": "object",
        "description": "Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this job.",
        "children": [
          {
            "name": "no_alert_for_canceled_runs",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "no_alert_for_skipped_runs",
            "type": "boolean",
            "description": "If true, do not send notifications to recipients specified in `on_failure` if the run is skipped."
          }
        ]
      },
      {
        "name": "parameters",
        "type": "array",
        "description": "Job-level parameter definitions",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "default",
            "type": "string",
            "description": "Default value of the parameter."
          }
        ]
      },
      {
        "name": "performance_target",
        "type": "string",
        "description": "PerformanceTarget defines how performant (lower latency) or cost efficient the execution of run<br />on serverless compute should be. The performance mode on the job or pipeline should map to a<br />performance setting that is passed to Cluster Manager (see cluster-common PerformanceTarget). (PERFORMANCE_OPTIMIZED, STANDARD)"
      },
      {
        "name": "queue",
        "type": "object",
        "description": "The queue settings of the job.",
        "children": [
          {
            "name": "enabled",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "run_as",
        "type": "object",
        "description": "The user or service principal that the job runs as, if specified in the request. This field indicates the explicit configuration of `run_as` for the job. To find the value in all cases, explicit or implicit, use `run_as_user_name`.",
        "children": [
          {
            "name": "group_name",
            "type": "string",
            "description": "Group name of an account group assigned to the workspace. Setting this field requires being a member of the group."
          },
          {
            "name": "service_principal_name",
            "type": "string",
            "description": "Application ID of an active service principal. Setting this field requires the `servicePrincipal/user` role."
          },
          {
            "name": "user_name",
            "type": "string",
            "description": "The email of an active workspace user. Non-admin users can only set this field to their own email."
          }
        ]
      },
      {
        "name": "schedule",
        "type": "object",
        "description": "An optional periodic schedule for this job. The default behavior is that the job only runs when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.",
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
            "description": "Indicate whether this schedule is paused or not. (PAUSED, UNPAUSED)"
          }
        ]
      },
      {
        "name": "tags",
        "type": "object",
        "description": "A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job."
      },
      {
        "name": "tasks",
        "type": "array",
        "description": "A list of task specifications to be executed by this job. It supports up to 1000 elements in write endpoints (:method:jobs/create, :method:jobs/reset, :method:jobs/update, :method:jobs/submit). Read endpoints return only 100 tasks. If more than 100 tasks are available, you can paginate through them using :method:jobs/get. Use the `next_page_token` field at the object root to determine if more results are available.",
        "children": [
          {
            "name": "task_key",
            "type": "string",
            "description": ""
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
                "description": "* `EQUAL_TO`, `NOT_EQUAL` operators perform string comparison of their operands. This means that<br />`“12.0” == “12”` will evaluate to `false`. * `GREATER_THAN`, `GREATER_THAN_OR_EQUAL`,<br />`LESS_THAN`, `LESS_THAN_OR_EQUAL` operators perform numeric comparison of their operands.<br />`“12.0” >= “12”` will evaluate to `true`, `“10.0” >= “12”` will evaluate to<br />`false`.<br /><br />The boolean comparison to task values can be implemented with operators `EQUAL_TO`, `NOT_EQUAL`.<br />If a task value was set to a boolean value, it will be serialized to `“true”` or<br />`“false”` for the comparison. (EQUAL_TO, GREATER_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN, LESS_THAN_OR_EQUAL, NOT_EQUAL)"
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
                "description": "Optional: subscription configuration for sending the dashboard snapshot."
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
                "description": "Optional location type of the project directory. When set to `WORKSPACE`, the project will be retrieved from the local Databricks workspace. When set to `GIT`, the project will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Project is located in Databricks workspace. * `GIT`: Project is located in cloud Git provider. (GIT, WORKSPACE)"
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
            "description": "An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete before executing this task. The task will run only if the `run_if` condition is true. The key is `task_key`, and the value is the name assigned to the dependent task.",
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
            "description": "An optional set of email addresses that is notified when runs of this task begin or complete as well as when this task is deleted. The default behavior is to not send any emails.",
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
                "description": "Configuration for the task that will be run for each element in the array"
              },
              {
                "name": "concurrency",
                "type": "integer",
                "description": "An optional maximum allowed number of concurrent runs of the task. Set this value if you want to be able to execute multiple runs of the task concurrently."
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
                "description": ""
              },
              {
                "name": "mlflow_experiment_name",
                "type": "string",
                "description": "Optional string containing the name of the MLflow experiment to log the run to. If name is not found, backend will create the mlflow experiment using the name."
              },
              {
                "name": "source",
                "type": "string",
                "description": "Optional location type of the training script. When set to `WORKSPACE`, the script will be retrieved from the local Databricks workspace. When set to `GIT`, the script will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Script is located in Databricks workspace. * `GIT`: Script is located in cloud Git provider. (GIT, WORKSPACE)"
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
            "name": "health",
            "type": "object",
            "description": "An optional set of health rules that can be defined for this job.",
            "children": [
              {
                "name": "rules",
                "type": "array",
                "description": ""
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
                "description": "Optional location type of the notebook. When set to `WORKSPACE`, the notebook will be retrieved from the local Databricks workspace. When set to `GIT`, the notebook will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Notebook is located in Databricks workspace. * `GIT`: Notebook is located in cloud Git provider. (GIT, WORKSPACE)"
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
            "description": "Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this task.",
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
                "description": "The semantic model to update"
              },
              {
                "name": "refresh_after_update",
                "type": "boolean",
                "description": "Whether the model should be refreshed after the update"
              },
              {
                "name": "tables",
                "type": "array",
                "description": "The tables to be exported to Power BI"
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
            "name": "retry_on_timeout",
            "type": "boolean",
            "description": "An optional policy to specify whether to retry a job when it times out. The default behavior is to not retry on timeout."
          },
          {
            "name": "run_if",
            "type": "string",
            "description": "An optional value specifying the condition determining whether the task is run once its dependencies have been completed. * `ALL_SUCCESS`: All dependencies have executed and succeeded * `AT_LEAST_ONE_SUCCESS`: At least one dependency has succeeded * `NONE_FAILED`: None of the dependencies have failed and at least one was executed * `ALL_DONE`: All dependencies have been completed * `AT_LEAST_ONE_FAILED`: At least one dependency failed * `ALL_FAILED`: ALl dependencies have failed (ALL_DONE, ALL_FAILED, ALL_SUCCESS, AT_LEAST_ONE_FAILED, AT_LEAST_ONE_SUCCESS, NONE_FAILED)"
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
                "description": "Controls whether the pipeline should perform a full refresh"
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
                "description": "Optional location type of the Python file. When set to `WORKSPACE` or not specified, the file will be retrieved from the local Databricks workspace or cloud location (if the `python_file` has a URI format). When set to `GIT`, the Python file will be retrieved from a Git repository defined in `git_source`. * `WORKSPACE`: The Python file is located in a Databricks workspace or at a cloud filesystem URI. * `GIT`: The Python file is located in a remote Git repository. (GIT, WORKSPACE)"
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
                "description": "If alert, indicates that this job must refresh a SQL alert."
              },
              {
                "name": "dashboard",
                "type": "object",
                "description": "If dashboard, indicates that this job must refresh a SQL dashboard."
              },
              {
                "name": "file",
                "type": "object",
                "description": "If file, indicates that this job runs a SQL file in a remote Git repository."
              },
              {
                "name": "parameters",
                "type": "object",
                "description": "Parameters to be used for each run of this job. The SQL alert task does not support custom parameters."
              },
              {
                "name": "query",
                "type": "object",
                "description": "If query, indicates that this job must execute a SQL query."
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
            "description": "A collection of system notification IDs to notify when runs of this task begin or complete. The default behavior is to not send any system notifications.",
            "children": [
              {
                "name": "on_duration_warning_threshold_exceeded",
                "type": "array",
                "description": ""
              },
              {
                "name": "on_failure",
                "type": "array",
                "description": "An optional list of system notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the `on_failure` property."
              },
              {
                "name": "on_start",
                "type": "array",
                "description": "An optional list of system notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the `on_start` property."
              },
              {
                "name": "on_streaming_backlog_exceeded",
                "type": "array",
                "description": "An optional list of system notification IDs to call when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the `health` field using the following metrics: `STREAMING_BACKLOG_BYTES`, `STREAMING_BACKLOG_RECORDS`, `STREAMING_BACKLOG_SECONDS`, or `STREAMING_BACKLOG_FILES`. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes. A maximum of 3 destinations can be specified for the `on_streaming_backlog_exceeded` property."
              },
              {
                "name": "on_success",
                "type": "array",
                "description": "An optional list of system notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the `on_success` property."
              }
            ]
          }
        ]
      },
      {
        "name": "timeout_seconds",
        "type": "integer",
        "description": "An optional timeout applied to each run of this job. A value of `0` means no timeout."
      },
      {
        "name": "trigger",
        "type": "object",
        "description": "A configuration to trigger a run when certain conditions are met. The default behavior is that the job runs only when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.",
        "children": [
          {
            "name": "file_arrival",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "url",
                "type": "string",
                "description": ""
              },
              {
                "name": "min_time_between_triggers_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after the specified amount of time passed since the last time the trigger fired. The minimum allowed value is 60 seconds"
              },
              {
                "name": "wait_after_last_change_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after no file activity has occurred for the specified amount of time. This makes it possible to wait for a batch of incoming files to arrive before triggering a run. The minimum allowed value is 60 seconds."
              }
            ]
          },
          {
            "name": "model",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "condition",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (MODEL_ALIAS_SET, MODEL_CREATED, MODEL_VERSION_READY)"
              },
              {
                "name": "aliases",
                "type": "array",
                "description": "Aliases of the model versions to monitor. Can only be used in conjunction with condition MODEL_ALIAS_SET."
              },
              {
                "name": "min_time_between_triggers_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after the specified amount of time has passed since the last time the trigger fired. The minimum allowed value is 60 seconds."
              },
              {
                "name": "securable_name",
                "type": "string",
                "description": "Name of the securable to monitor (\"mycatalog.myschema.mymodel\" in the case of model-level triggers, \"mycatalog.myschema\" in the case of schema-level triggers) or empty in the case of metastore-level triggers."
              },
              {
                "name": "wait_after_last_change_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after no model updates have occurred for the specified time and can be used to wait for a series of model updates before triggering a run. The minimum allowed value is 60 seconds."
              }
            ]
          },
          {
            "name": "pause_status",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (PAUSED, UNPAUSED)"
          },
          {
            "name": "periodic",
            "type": "object",
            "description": "Periodic trigger settings.",
            "children": [
              {
                "name": "interval",
                "type": "integer",
                "description": ""
              },
              {
                "name": "unit",
                "type": "string",
                "description": "The unit of time for the interval. (DAYS, HOURS, WEEKS)"
              }
            ]
          },
          {
            "name": "table_update",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "table_names",
                "type": "array",
                "description": ""
              },
              {
                "name": "condition",
                "type": "string",
                "description": "The table(s) condition based on which to trigger a job run. (ALL_UPDATED, ANY_UPDATED)"
              },
              {
                "name": "min_time_between_triggers_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after the specified amount of time has passed since the last time the trigger fired. The minimum allowed value is 60 seconds."
              },
              {
                "name": "wait_after_last_change_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after no table updates have occurred for the specified time and can be used to wait for a series of table updates before triggering a run. The minimum allowed value is 60 seconds."
              }
            ]
          }
        ]
      },
      {
        "name": "usage_policy_id",
        "type": "string",
        "description": "The id of the user specified usage policy to use for this job. If not specified, a default usage policy may be applied when creating or modifying the job. See `effective_usage_policy_id` for the usage policy used by this workload."
      },
      {
        "name": "webhook_notifications",
        "type": "object",
        "description": "A collection of system notification IDs to notify when runs of this job begin or complete.",
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
    "name": "trigger_state",
    "type": "object",
    "description": "State of the trigger associated with the job.",
    "children": [
      {
        "name": "file_arrival",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "using_file_events",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "table",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "last_seen_table_states",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "has_seen_updates",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "table_name",
                "type": "string",
                "description": "Full table name of the table to monitor, e.g. `mycatalog.myschema.mytable`"
              }
            ]
          },
          {
            "name": "using_scalable_monitoring",
            "type": "boolean",
            "description": "Indicates whether the trigger is using scalable monitoring."
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
    "name": "effective_budget_policy_id",
    "type": "string",
    "description": "The id of the budget policy used by this job for cost attribution purposes. This may be set through (in order of precedence): 1. Budget admins through the account or workspace console 2. Jobs UI in the job details page and Jobs API using `budget_policy_id` 3. Inferred default based on accessible budget policies of the run_as identity on job creation or modification."
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": "The id of the usage policy used by this job for cost attribution purposes."
  },
  {
    "name": "job_id",
    "type": "integer",
    "description": "The canonical identifier for this job."
  },
  {
    "name": "creator_user_name",
    "type": "string",
    "description": "The creator user name. This field won’t be included in the response if the user has already been deleted."
  },
  {
    "name": "created_time",
    "type": "integer",
    "description": ""
  },
  {
    "name": "has_more",
    "type": "boolean",
    "description": "Indicates if the job has more array properties (`tasks`, `job_clusters`) that are not shown. They can be accessed via :method:jobs/get endpoint. It is only relevant for API 2.2 :method:jobs/list requests with `expand_tasks=true`."
  },
  {
    "name": "settings",
    "type": "object",
    "description": "Settings for this job and all of its runs. These settings can be updated using the `resetJob` method.",
    "children": [
      {
        "name": "budget_policy_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "continuous",
        "type": "object",
        "description": "An optional continuous property for this job. The continuous property will ensure that there is always one run executing. Only one of `schedule` and `continuous` can be used.",
        "children": [
          {
            "name": "pause_status",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (PAUSED, UNPAUSED)"
          },
          {
            "name": "task_retry_mode",
            "type": "string",
            "description": "Indicate whether the continuous job is applying task level retries or not. Defaults to NEVER. (NEVER, ON_FAILURE)"
          }
        ]
      },
      {
        "name": "deployment",
        "type": "object",
        "description": "Deployment information for jobs managed by external sources.",
        "children": [
          {
            "name": "kind",
            "type": "string",
            "description": "* `BUNDLE`: The job is managed by Databricks Asset Bundle. * `SYSTEM_MANAGED`: The job is<br />managed by Databricks and is read-only. (BUNDLE, SYSTEM_MANAGED)"
          },
          {
            "name": "metadata_file_path",
            "type": "string",
            "description": "Path of the file that contains deployment metadata."
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "An optional description for the job. The maximum length is 27700 characters in UTF-8 encoding."
      },
      {
        "name": "edit_mode",
        "type": "string",
        "description": "Edit mode of the job. * `UI_LOCKED`: The job is in a locked UI state and cannot be modified. * `EDITABLE`: The job is in an editable state and can be modified. (EDITABLE, UI_LOCKED)"
      },
      {
        "name": "email_notifications",
        "type": "object",
        "description": "An optional set of email addresses that is notified when runs of this job begin or complete as well as when this job is deleted.",
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
        "name": "environments",
        "type": "array",
        "description": "A list of task execution environment specifications that can be referenced by serverless tasks of this job. For serverless notebook tasks, if the environment_key is not specified, the notebook environment will be used if present. If a jobs environment is specified, it will override the notebook environment. For other serverless tasks, the task environment is required to be specified using environment_key in the task settings.",
        "children": [
          {
            "name": "environment_key",
            "type": "string",
            "description": ""
          },
          {
            "name": "spec",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "format",
        "type": "string",
        "description": "Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to `\"MULTI_TASK\"`. (MULTI_TASK, SINGLE_TASK)"
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
            "description": "Unique identifier of the service used to host the Git repository. The value is case insensitive. (awsCodeCommit, azureDevOpsServices, bitbucketCloud, bitbucketServer, gitHub, gitHubEnterprise, gitLab, gitLabEnterpriseEdition)"
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
                "description": "Dirty state indicates the job is not fully synced with the job specification in the remote repository. Possible values are: * `NOT_SYNCED`: The job is not yet synced with the remote job specification. Import the remote job specification from UI to make the job fully synced. * `DISCONNECTED`: The job is temporary disconnected from the remote job specification and is allowed for live edit. Import the remote job specification again from UI to make the job fully synced. (DISCONNECTED, NOT_SYNCED)"
              }
            ]
          }
        ]
      },
      {
        "name": "health",
        "type": "object",
        "description": "An optional set of health rules that can be defined for this job.",
        "children": [
          {
            "name": "rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "metric",
                "type": "string",
                "description": "Specifies the health metric that is being evaluated for a particular health rule.<br /><br />* `RUN_DURATION_SECONDS`: Expected total time for a run in seconds. * `STREAMING_BACKLOG_BYTES`:<br />An estimate of the maximum bytes of data waiting to be consumed across all streams. This metric<br />is in Public Preview. * `STREAMING_BACKLOG_RECORDS`: An estimate of the maximum offset lag<br />across all streams. This metric is in Public Preview. * `STREAMING_BACKLOG_SECONDS`: An estimate<br />of the maximum consumer delay across all streams. This metric is in Public Preview. *<br />`STREAMING_BACKLOG_FILES`: An estimate of the maximum number of outstanding files across all<br />streams. This metric is in Public Preview. (RUN_DURATION_SECONDS, STREAMING_BACKLOG_BYTES, STREAMING_BACKLOG_FILES, STREAMING_BACKLOG_RECORDS, STREAMING_BACKLOG_SECONDS)"
              },
              {
                "name": "op",
                "type": "string",
                "description": "Specifies the operator used to compare the health metric value with the specified threshold. (GREATER_THAN)"
              },
              {
                "name": "value",
                "type": "integer",
                "description": "Specifies the threshold value that the health metric should obey to satisfy the health rule."
              }
            ]
          }
        ]
      },
      {
        "name": "job_clusters",
        "type": "array",
        "description": "A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.",
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
        "name": "max_concurrent_runs",
        "type": "integer",
        "description": "An optional maximum allowed number of concurrent runs of the job. Set this value if you want to be able to execute multiple runs of the same job concurrently. This is useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each other, or if you want to trigger multiple runs which differ by their input parameters. This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs. However, from then on, new runs are skipped unless there are fewer than 3 active runs. This value cannot exceed 1000. Setting this value to `0` causes all new runs to be skipped."
      },
      {
        "name": "name",
        "type": "string",
        "description": "An optional name for the job. The maximum length is 4096 bytes in UTF-8 encoding."
      },
      {
        "name": "notification_settings",
        "type": "object",
        "description": "Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this job.",
        "children": [
          {
            "name": "no_alert_for_canceled_runs",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "no_alert_for_skipped_runs",
            "type": "boolean",
            "description": "If true, do not send notifications to recipients specified in `on_failure` if the run is skipped."
          }
        ]
      },
      {
        "name": "parameters",
        "type": "array",
        "description": "Job-level parameter definitions",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "default",
            "type": "string",
            "description": "Default value of the parameter."
          }
        ]
      },
      {
        "name": "performance_target",
        "type": "string",
        "description": "PerformanceTarget defines how performant (lower latency) or cost efficient the execution of run<br />on serverless compute should be. The performance mode on the job or pipeline should map to a<br />performance setting that is passed to Cluster Manager (see cluster-common PerformanceTarget). (PERFORMANCE_OPTIMIZED, STANDARD)"
      },
      {
        "name": "queue",
        "type": "object",
        "description": "The queue settings of the job.",
        "children": [
          {
            "name": "enabled",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "run_as",
        "type": "object",
        "description": "The user or service principal that the job runs as, if specified in the request. This field indicates the explicit configuration of `run_as` for the job. To find the value in all cases, explicit or implicit, use `run_as_user_name`.",
        "children": [
          {
            "name": "group_name",
            "type": "string",
            "description": "Group name of an account group assigned to the workspace. Setting this field requires being a member of the group."
          },
          {
            "name": "service_principal_name",
            "type": "string",
            "description": "Application ID of an active service principal. Setting this field requires the `servicePrincipal/user` role."
          },
          {
            "name": "user_name",
            "type": "string",
            "description": "The email of an active workspace user. Non-admin users can only set this field to their own email."
          }
        ]
      },
      {
        "name": "schedule",
        "type": "object",
        "description": "An optional periodic schedule for this job. The default behavior is that the job only runs when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.",
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
            "description": "Indicate whether this schedule is paused or not. (PAUSED, UNPAUSED)"
          }
        ]
      },
      {
        "name": "tags",
        "type": "object",
        "description": "A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job."
      },
      {
        "name": "tasks",
        "type": "array",
        "description": "A list of task specifications to be executed by this job. It supports up to 1000 elements in write endpoints (:method:jobs/create, :method:jobs/reset, :method:jobs/update, :method:jobs/submit). Read endpoints return only 100 tasks. If more than 100 tasks are available, you can paginate through them using :method:jobs/get. Use the `next_page_token` field at the object root to determine if more results are available.",
        "children": [
          {
            "name": "task_key",
            "type": "string",
            "description": ""
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
                "description": "* `EQUAL_TO`, `NOT_EQUAL` operators perform string comparison of their operands. This means that<br />`“12.0” == “12”` will evaluate to `false`. * `GREATER_THAN`, `GREATER_THAN_OR_EQUAL`,<br />`LESS_THAN`, `LESS_THAN_OR_EQUAL` operators perform numeric comparison of their operands.<br />`“12.0” >= “12”` will evaluate to `true`, `“10.0” >= “12”` will evaluate to<br />`false`.<br /><br />The boolean comparison to task values can be implemented with operators `EQUAL_TO`, `NOT_EQUAL`.<br />If a task value was set to a boolean value, it will be serialized to `“true”` or<br />`“false”` for the comparison. (EQUAL_TO, GREATER_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN, LESS_THAN_OR_EQUAL, NOT_EQUAL)"
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
                "description": "Optional: subscription configuration for sending the dashboard snapshot."
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
                "description": "Optional location type of the project directory. When set to `WORKSPACE`, the project will be retrieved from the local Databricks workspace. When set to `GIT`, the project will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Project is located in Databricks workspace. * `GIT`: Project is located in cloud Git provider. (GIT, WORKSPACE)"
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
            "description": "An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete before executing this task. The task will run only if the `run_if` condition is true. The key is `task_key`, and the value is the name assigned to the dependent task.",
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
            "description": "An optional set of email addresses that is notified when runs of this task begin or complete as well as when this task is deleted. The default behavior is to not send any emails.",
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
                "description": "Configuration for the task that will be run for each element in the array"
              },
              {
                "name": "concurrency",
                "type": "integer",
                "description": "An optional maximum allowed number of concurrent runs of the task. Set this value if you want to be able to execute multiple runs of the task concurrently."
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
                "description": ""
              },
              {
                "name": "mlflow_experiment_name",
                "type": "string",
                "description": "Optional string containing the name of the MLflow experiment to log the run to. If name is not found, backend will create the mlflow experiment using the name."
              },
              {
                "name": "source",
                "type": "string",
                "description": "Optional location type of the training script. When set to `WORKSPACE`, the script will be retrieved from the local Databricks workspace. When set to `GIT`, the script will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Script is located in Databricks workspace. * `GIT`: Script is located in cloud Git provider. (GIT, WORKSPACE)"
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
            "name": "health",
            "type": "object",
            "description": "An optional set of health rules that can be defined for this job.",
            "children": [
              {
                "name": "rules",
                "type": "array",
                "description": ""
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
                "description": "Optional location type of the notebook. When set to `WORKSPACE`, the notebook will be retrieved from the local Databricks workspace. When set to `GIT`, the notebook will be retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if `git_source` is defined and `WORKSPACE` otherwise. * `WORKSPACE`: Notebook is located in Databricks workspace. * `GIT`: Notebook is located in cloud Git provider. (GIT, WORKSPACE)"
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
            "description": "Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this task.",
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
                "description": "The semantic model to update"
              },
              {
                "name": "refresh_after_update",
                "type": "boolean",
                "description": "Whether the model should be refreshed after the update"
              },
              {
                "name": "tables",
                "type": "array",
                "description": "The tables to be exported to Power BI"
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
            "name": "retry_on_timeout",
            "type": "boolean",
            "description": "An optional policy to specify whether to retry a job when it times out. The default behavior is to not retry on timeout."
          },
          {
            "name": "run_if",
            "type": "string",
            "description": "An optional value specifying the condition determining whether the task is run once its dependencies have been completed. * `ALL_SUCCESS`: All dependencies have executed and succeeded * `AT_LEAST_ONE_SUCCESS`: At least one dependency has succeeded * `NONE_FAILED`: None of the dependencies have failed and at least one was executed * `ALL_DONE`: All dependencies have been completed * `AT_LEAST_ONE_FAILED`: At least one dependency failed * `ALL_FAILED`: ALl dependencies have failed (ALL_DONE, ALL_FAILED, ALL_SUCCESS, AT_LEAST_ONE_FAILED, AT_LEAST_ONE_SUCCESS, NONE_FAILED)"
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
                "description": "Controls whether the pipeline should perform a full refresh"
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
                "description": "Optional location type of the Python file. When set to `WORKSPACE` or not specified, the file will be retrieved from the local Databricks workspace or cloud location (if the `python_file` has a URI format). When set to `GIT`, the Python file will be retrieved from a Git repository defined in `git_source`. * `WORKSPACE`: The Python file is located in a Databricks workspace or at a cloud filesystem URI. * `GIT`: The Python file is located in a remote Git repository. (GIT, WORKSPACE)"
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
                "description": "If alert, indicates that this job must refresh a SQL alert."
              },
              {
                "name": "dashboard",
                "type": "object",
                "description": "If dashboard, indicates that this job must refresh a SQL dashboard."
              },
              {
                "name": "file",
                "type": "object",
                "description": "If file, indicates that this job runs a SQL file in a remote Git repository."
              },
              {
                "name": "parameters",
                "type": "object",
                "description": "Parameters to be used for each run of this job. The SQL alert task does not support custom parameters."
              },
              {
                "name": "query",
                "type": "object",
                "description": "If query, indicates that this job must execute a SQL query."
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
            "description": "A collection of system notification IDs to notify when runs of this task begin or complete. The default behavior is to not send any system notifications.",
            "children": [
              {
                "name": "on_duration_warning_threshold_exceeded",
                "type": "array",
                "description": ""
              },
              {
                "name": "on_failure",
                "type": "array",
                "description": "An optional list of system notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the `on_failure` property."
              },
              {
                "name": "on_start",
                "type": "array",
                "description": "An optional list of system notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the `on_start` property."
              },
              {
                "name": "on_streaming_backlog_exceeded",
                "type": "array",
                "description": "An optional list of system notification IDs to call when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the `health` field using the following metrics: `STREAMING_BACKLOG_BYTES`, `STREAMING_BACKLOG_RECORDS`, `STREAMING_BACKLOG_SECONDS`, or `STREAMING_BACKLOG_FILES`. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes. A maximum of 3 destinations can be specified for the `on_streaming_backlog_exceeded` property."
              },
              {
                "name": "on_success",
                "type": "array",
                "description": "An optional list of system notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the `on_success` property."
              }
            ]
          }
        ]
      },
      {
        "name": "timeout_seconds",
        "type": "integer",
        "description": "An optional timeout applied to each run of this job. A value of `0` means no timeout."
      },
      {
        "name": "trigger",
        "type": "object",
        "description": "A configuration to trigger a run when certain conditions are met. The default behavior is that the job runs only when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.",
        "children": [
          {
            "name": "file_arrival",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "url",
                "type": "string",
                "description": ""
              },
              {
                "name": "min_time_between_triggers_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after the specified amount of time passed since the last time the trigger fired. The minimum allowed value is 60 seconds"
              },
              {
                "name": "wait_after_last_change_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after no file activity has occurred for the specified amount of time. This makes it possible to wait for a batch of incoming files to arrive before triggering a run. The minimum allowed value is 60 seconds."
              }
            ]
          },
          {
            "name": "model",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "condition",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (MODEL_ALIAS_SET, MODEL_CREATED, MODEL_VERSION_READY)"
              },
              {
                "name": "aliases",
                "type": "array",
                "description": "Aliases of the model versions to monitor. Can only be used in conjunction with condition MODEL_ALIAS_SET."
              },
              {
                "name": "min_time_between_triggers_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after the specified amount of time has passed since the last time the trigger fired. The minimum allowed value is 60 seconds."
              },
              {
                "name": "securable_name",
                "type": "string",
                "description": "Name of the securable to monitor (\"mycatalog.myschema.mymodel\" in the case of model-level triggers, \"mycatalog.myschema\" in the case of schema-level triggers) or empty in the case of metastore-level triggers."
              },
              {
                "name": "wait_after_last_change_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after no model updates have occurred for the specified time and can be used to wait for a series of model updates before triggering a run. The minimum allowed value is 60 seconds."
              }
            ]
          },
          {
            "name": "pause_status",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (PAUSED, UNPAUSED)"
          },
          {
            "name": "periodic",
            "type": "object",
            "description": "Periodic trigger settings.",
            "children": [
              {
                "name": "interval",
                "type": "integer",
                "description": ""
              },
              {
                "name": "unit",
                "type": "string",
                "description": "The unit of time for the interval. (DAYS, HOURS, WEEKS)"
              }
            ]
          },
          {
            "name": "table_update",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "table_names",
                "type": "array",
                "description": ""
              },
              {
                "name": "condition",
                "type": "string",
                "description": "The table(s) condition based on which to trigger a job run. (ALL_UPDATED, ANY_UPDATED)"
              },
              {
                "name": "min_time_between_triggers_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after the specified amount of time has passed since the last time the trigger fired. The minimum allowed value is 60 seconds."
              },
              {
                "name": "wait_after_last_change_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after no table updates have occurred for the specified time and can be used to wait for a series of table updates before triggering a run. The minimum allowed value is 60 seconds."
              }
            ]
          }
        ]
      },
      {
        "name": "usage_policy_id",
        "type": "string",
        "description": "The id of the user specified usage policy to use for this job. If not specified, a default usage policy may be applied when creating or modifying the job. See `effective_usage_policy_id` for the usage policy used by this workload."
      },
      {
        "name": "webhook_notifications",
        "type": "object",
        "description": "A collection of system notification IDs to notify when runs of this job begin or complete.",
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
    "name": "trigger_state",
    "type": "object",
    "description": "State of the trigger associated with the job.",
    "children": [
      {
        "name": "file_arrival",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "using_file_events",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "table",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "last_seen_table_states",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "has_seen_updates",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "table_name",
                "type": "string",
                "description": "Full table name of the table to monitor, e.g. `mycatalog.myschema.mytable`"
              }
            ]
          },
          {
            "name": "using_scalable_monitoring",
            "type": "boolean",
            "description": "Indicates whether the trigger is using scalable monitoring."
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
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Retrieves the details for a single job.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-expand_tasks"><code>expand_tasks</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Retrieves a list of jobs.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Create a new job.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-job_id"><code>job_id</code></a></td>
    <td></td>
    <td>Add, update, or remove specific settings of an existing job. Use the [_Reset_</td>
</tr>
<tr>
    <td><a href="#reset"><CopyableCode code="reset" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-new_settings"><code>new_settings</code></a></td>
    <td></td>
    <td>Overwrite all settings for the given job. Use the [_Update_ endpoint](:method:jobs/update) to update</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a job.</td>
</tr>
<tr>
    <td><a href="#run_now"><CopyableCode code="run_now" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-job_id"><code>job_id</code></a></td>
    <td></td>
    <td>Run a job and return the `run_id` of the triggered run.</td>
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
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>integer</code></td>
    <td>The canonical identifier of the job to retrieve information about. This field is required.</td>
</tr>
<tr id="parameter-expand_tasks">
    <td><CopyableCode code="expand_tasks" /></td>
    <td><code>string</code></td>
    <td>Whether to include task and cluster details in the response. Note that only the first 100 elements will be shown. Use :method:jobs/get to paginate through all tasks and clusters.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>string</code></td>
    <td>The number of jobs to return. This value must be greater than 0 and less or equal to 100. The default value is 20.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A filter on the list based on the exact (case insensitive) job name.</td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>string</code></td>
    <td>The offset of the first job to return, relative to the most recently created job. Deprecated since June 2023. Use `page_token` to iterate through the pages instead.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Use `next_page_token` or `prev_page_token` returned from the previous request to list the next or previous page of jobs respectively.</td>
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

Retrieves the details for a single job.

```sql
SELECT
effective_budget_policy_id,
effective_usage_policy_id,
job_id,
creator_user_name,
run_as_user_name,
created_time,
has_more,
next_page_token,
settings,
trigger_state
FROM databricks_workspace.jobs.jobs
WHERE job_id = '{{ job_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves a list of jobs.

```sql
SELECT
effective_budget_policy_id,
effective_usage_policy_id,
job_id,
creator_user_name,
created_time,
has_more,
settings,
trigger_state
FROM databricks_workspace.jobs.jobs
WHERE deployment_name = '{{ deployment_name }}' -- required
AND expand_tasks = '{{ expand_tasks }}'
AND limit = '{{ limit }}'
AND name = '{{ name }}'
AND offset = '{{ offset }}'
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

Create a new job.

```sql
INSERT INTO databricks_workspace.jobs.jobs (
access_control_list,
budget_policy_id,
continuous,
deployment,
description,
edit_mode,
email_notifications,
environments,
format,
git_source,
health,
job_clusters,
max_concurrent_runs,
name,
notification_settings,
parameters,
performance_target,
queue,
run_as,
schedule,
tags,
tasks,
timeout_seconds,
trigger,
usage_policy_id,
webhook_notifications,
deployment_name
)
SELECT 
'{{ access_control_list }}',
'{{ budget_policy_id }}',
'{{ continuous }}',
'{{ deployment }}',
'{{ description }}',
'{{ edit_mode }}',
'{{ email_notifications }}',
'{{ environments }}',
'{{ format }}',
'{{ git_source }}',
'{{ health }}',
'{{ job_clusters }}',
'{{ max_concurrent_runs }}',
'{{ name }}',
'{{ notification_settings }}',
'{{ parameters }}',
'{{ performance_target }}',
'{{ queue }}',
'{{ run_as }}',
'{{ schedule }}',
'{{ tags }}',
'{{ tasks }}',
'{{ timeout_seconds }}',
'{{ trigger }}',
'{{ usage_policy_id }}',
'{{ webhook_notifications }}',
'{{ deployment_name }}'
RETURNING
job_id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: jobs
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the jobs resource.
    - name: access_control_list
      value: string
      description: |
        List of permissions to set on the job.
    - name: budget_policy_id
      value: string
      description: |
        The id of the user specified budget policy to use for this job. If not specified, a default budget policy may be applied when creating or modifying the job. See `effective_budget_policy_id` for the budget policy used by this workload.
    - name: continuous
      value: string
      description: |
        An optional continuous property for this job. The continuous property will ensure that there is always one run executing. Only one of `schedule` and `continuous` can be used.
    - name: deployment
      value: string
      description: |
        Deployment information for jobs managed by external sources.
    - name: description
      value: string
      description: |
        An optional description for the job. The maximum length is 27700 characters in UTF-8 encoding.
    - name: edit_mode
      value: string
      description: |
        Edit mode of the job. * `UI_LOCKED`: The job is in a locked UI state and cannot be modified. * `EDITABLE`: The job is in an editable state and can be modified.
    - name: email_notifications
      value: string
      description: |
        An optional set of email addresses that is notified when runs of this job begin or complete as well as when this job is deleted.
    - name: environments
      value: string
      description: |
        A list of task execution environment specifications that can be referenced by serverless tasks of this job. For serverless notebook tasks, if the environment_key is not specified, the notebook environment will be used if present. If a jobs environment is specified, it will override the notebook environment. For other serverless tasks, the task environment is required to be specified using environment_key in the task settings.
    - name: format
      value: string
      description: |
        Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to `"MULTI_TASK"`.
    - name: git_source
      value: string
      description: |
        An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks. If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task. Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.
    - name: health
      value: string
      description: |
        :param job_clusters: List[:class:`JobCluster`] (optional) A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.
    - name: job_clusters
      value: string
    - name: max_concurrent_runs
      value: string
      description: |
        An optional maximum allowed number of concurrent runs of the job. Set this value if you want to be able to execute multiple runs of the same job concurrently. This is useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each other, or if you want to trigger multiple runs which differ by their input parameters. This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs. However, from then on, new runs are skipped unless there are fewer than 3 active runs. This value cannot exceed 1000. Setting this value to `0` causes all new runs to be skipped.
    - name: name
      value: string
      description: |
        An optional name for the job. The maximum length is 4096 bytes in UTF-8 encoding.
    - name: notification_settings
      value: string
      description: |
        Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this job.
    - name: parameters
      value: string
      description: |
        Job-level parameter definitions
    - name: performance_target
      value: string
      description: |
        The performance mode on a serverless job. This field determines the level of compute performance or cost-efficiency for the run. The performance target does not apply to tasks that run on Serverless GPU compute. * `STANDARD`: Enables cost-efficient execution of serverless workloads. * `PERFORMANCE_OPTIMIZED`: Prioritizes fast startup and execution times through rapid scaling and optimized cluster performance.
    - name: queue
      value: string
      description: |
        The queue settings of the job.
    - name: run_as
      value: string
      description: |
        The user or service principal that the job runs as, if specified in the request. This field indicates the explicit configuration of `run_as` for the job. To find the value in all cases, explicit or implicit, use `run_as_user_name`.
    - name: schedule
      value: string
      description: |
        An optional periodic schedule for this job. The default behavior is that the job only runs when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.
    - name: tags
      value: string
      description: |
        A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job.
    - name: tasks
      value: string
      description: |
        A list of task specifications to be executed by this job. It supports up to 1000 elements in write endpoints (:method:jobs/create, :method:jobs/reset, :method:jobs/update, :method:jobs/submit). Read endpoints return only 100 tasks. If more than 100 tasks are available, you can paginate through them using :method:jobs/get. Use the `next_page_token` field at the object root to determine if more results are available.
    - name: timeout_seconds
      value: string
      description: |
        An optional timeout applied to each run of this job. A value of `0` means no timeout.
    - name: trigger
      value: string
      description: |
        A configuration to trigger a run when certain conditions are met. The default behavior is that the job runs only when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.
    - name: usage_policy_id
      value: string
      description: |
        The id of the user specified usage policy to use for this job. If not specified, a default usage policy may be applied when creating or modifying the job. See `effective_usage_policy_id` for the usage policy used by this workload.
    - name: webhook_notifications
      value: string
      description: |
        A collection of system notification IDs to notify when runs of this job begin or complete.
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Add, update, or remove specific settings of an existing job. Use the [_Reset_

```sql
UPDATE databricks_workspace.jobs.jobs
SET 
job_id = {{ job_id }},
fields_to_remove = '{{ fields_to_remove }}',
new_settings = '{{ new_settings }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
AND job_id = '{{ job_id }}' --required;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="reset"
    values={[
        { label: 'reset', value: 'reset' }
    ]}
>
<TabItem value="reset">

Overwrite all settings for the given job. Use the [_Update_ endpoint](:method:jobs/update) to update

```sql
REPLACE databricks_workspace.jobs.jobs
SET 
job_id = {{ job_id }},
new_settings = '{{ new_settings }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
AND job_id = '{{ job_id }}' --required
AND new_settings = '{{ new_settings }}' --required;
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

Deletes a job.

```sql
DELETE FROM databricks_workspace.jobs.jobs
WHERE deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="run_now"
    values={[
        { label: 'run_now', value: 'run_now' }
    ]}
>
<TabItem value="run_now">

Run a job and return the `run_id` of the triggered run.

```sql
EXEC databricks_workspace.jobs.jobs.run_now 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"job_id": {{ job_id }}, 
"dbt_commands": "{{ dbt_commands }}", 
"idempotency_token": "{{ idempotency_token }}", 
"jar_params": "{{ jar_params }}", 
"job_parameters": "{{ job_parameters }}", 
"notebook_params": "{{ notebook_params }}", 
"only": "{{ only }}", 
"performance_target": "{{ performance_target }}", 
"pipeline_params": "{{ pipeline_params }}", 
"python_named_params": "{{ python_named_params }}", 
"python_params": "{{ python_params }}", 
"queue": "{{ queue }}", 
"spark_submit_params": "{{ spark_submit_params }}", 
"sql_params": "{{ sql_params }}"
}'
;
```
</TabItem>
</Tabs>

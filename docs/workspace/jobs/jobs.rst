``w.jobs``: Jobs
================
.. currentmodule:: databricks.sdk.service.jobs

.. py:class:: JobsAPI

    The Jobs API allows you to create, edit, and delete jobs.
    
    You can use a Databricks job to run a data processing or data analysis task in a Databricks cluster with
    scalable resources. Your job can consist of a single task or can be a large, multi-task workflow with
    complex dependencies. Databricks manages the task orchestration, cluster management, monitoring, and error
    reporting for all of your jobs. You can run your jobs immediately or periodically through an easy-to-use
    scheduling system. You can implement job tasks using notebooks, JARS, Delta Live Tables pipelines, or
    Python, Scala, Spark submit, and Java applications.
    
    You should never hard code secrets or store them in plain text. Use the [Secrets CLI] to manage secrets in
    the [Databricks CLI]. Use the [Secrets utility] to reference secrets in notebooks and jobs.
    
    [Databricks CLI]: https://docs.databricks.com/dev-tools/cli/index.html
    [Secrets CLI]: https://docs.databricks.com/dev-tools/cli/secrets-cli.html
    [Secrets utility]: https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-secrets

    .. py:method:: cancel_all_runs( [, all_queued_runs: Optional[bool], job_id: Optional[int]])


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            created_job = w.jobs.create(name=f'sdk-{time.time_ns()}',
                                        tasks=[
                                            jobs.Task(description="test",
                                                      existing_cluster_id=cluster_id,
                                                      notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                      task_key="test",
                                                      timeout_seconds=0)
                                        ])
            
            w.jobs.cancel_all_runs(job_id=created_job.job_id)
            
            # cleanup
            w.jobs.delete(job_id=created_job.job_id)

        Cancel all runs of a job.
        
        Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new runs
        from being started.
        
        :param all_queued_runs: bool (optional)
          Optional boolean parameter to cancel all queued runs. If no job_id is provided, all queued runs in
          the workspace are canceled.
        :param job_id: int (optional)
          The canonical identifier of the job to cancel all runs of.
        
        
        

    .. py:method:: cancel_run(run_id: int) -> Wait[Run]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            created_job = w.jobs.create(name=f'sdk-{time.time_ns()}',
                                        tasks=[
                                            jobs.Task(description="test",
                                                      existing_cluster_id=cluster_id,
                                                      notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                      task_key="test",
                                                      timeout_seconds=0)
                                        ])
            
            run_now_response = w.jobs.run_now(job_id=created_job.job_id)
            
            cancelled_run = w.jobs.cancel_run(run_id=run_now_response.response.run_id).result()
            
            # cleanup
            w.jobs.delete(job_id=created_job.job_id)

        Cancel a run.
        
        Cancels a job run or a task run. The run is canceled asynchronously, so it may still be running when
        this request completes.
        
        :param run_id: int
          This field is required.
        
        :returns:
          Long-running operation waiter for :class:`Run`.
          See :method:wait_get_run_job_terminated_or_skipped for more details.
        

    .. py:method:: cancel_run_and_wait(run_id: int, timeout: datetime.timedelta = 0:20:00) -> Run


    .. py:method:: create( [, access_control_list: Optional[List[JobAccessControlRequest]], budget_policy_id: Optional[str], continuous: Optional[Continuous], deployment: Optional[JobDeployment], description: Optional[str], edit_mode: Optional[JobEditMode], email_notifications: Optional[JobEmailNotifications], environments: Optional[List[JobEnvironment]], format: Optional[Format], git_source: Optional[GitSource], health: Optional[JobsHealthRules], job_clusters: Optional[List[JobCluster]], max_concurrent_runs: Optional[int], name: Optional[str], notification_settings: Optional[JobNotificationSettings], parameters: Optional[List[JobParameterDefinition]], queue: Optional[QueueSettings], run_as: Optional[JobRunAs], schedule: Optional[CronSchedule], tags: Optional[Dict[str, str]], tasks: Optional[List[Task]], timeout_seconds: Optional[int], trigger: Optional[TriggerSettings], webhook_notifications: Optional[WebhookNotifications]]) -> CreateResponse


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            created_job = w.jobs.create(name=f'sdk-{time.time_ns()}',
                                        tasks=[
                                            jobs.Task(description="test",
                                                      existing_cluster_id=cluster_id,
                                                      notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                      task_key="test",
                                                      timeout_seconds=0)
                                        ])
            
            # cleanup
            w.jobs.delete(job_id=created_job.job_id)

        Create a new job.
        
        Create a new job.
        
        :param access_control_list: List[:class:`JobAccessControlRequest`] (optional)
          List of permissions to set on the job.
        :param budget_policy_id: str (optional)
          The id of the user specified budget policy to use for this job. If not specified, a default budget
          policy may be applied when creating or modifying the job. See `effective_budget_policy_id` for the
          budget policy used by this workload.
        :param continuous: :class:`Continuous` (optional)
          An optional continuous property for this job. The continuous property will ensure that there is
          always one run executing. Only one of `schedule` and `continuous` can be used.
        :param deployment: :class:`JobDeployment` (optional)
          Deployment information for jobs managed by external sources.
        :param description: str (optional)
          An optional description for the job. The maximum length is 27700 characters in UTF-8 encoding.
        :param edit_mode: :class:`JobEditMode` (optional)
          Edit mode of the job.
          
          * `UI_LOCKED`: The job is in a locked UI state and cannot be modified. * `EDITABLE`: The job is in
          an editable state and can be modified.
        :param email_notifications: :class:`JobEmailNotifications` (optional)
          An optional set of email addresses that is notified when runs of this job begin or complete as well
          as when this job is deleted.
        :param environments: List[:class:`JobEnvironment`] (optional)
          A list of task execution environment specifications that can be referenced by serverless tasks of
          this job. An environment is required to be present for serverless tasks. For serverless notebook
          tasks, the environment is accessible in the notebook environment panel. For other serverless tasks,
          the task environment is required to be specified using environment_key in the task settings.
        :param format: :class:`Format` (optional)
          Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When
          using the Jobs API 2.1 this value is always set to `"MULTI_TASK"`.
        :param git_source: :class:`GitSource` (optional)
          An optional specification for a remote Git repository containing the source code used by tasks.
          Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks.
          
          If `git_source` is set, these tasks retrieve the file from the remote repository by default.
          However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task.
          
          Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are
          used, `git_source` must be defined on the job.
        :param health: :class:`JobsHealthRules` (optional)
          An optional set of health rules that can be defined for this job.
        :param job_clusters: List[:class:`JobCluster`] (optional)
          A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries
          cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.
        :param max_concurrent_runs: int (optional)
          An optional maximum allowed number of concurrent runs of the job. Set this value if you want to be
          able to execute multiple runs of the same job concurrently. This is useful for example if you
          trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each
          other, or if you want to trigger multiple runs which differ by their input parameters. This setting
          affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent
          active runs. Then setting the concurrency to 3 won’t kill any of the active runs. However, from
          then on, new runs are skipped unless there are fewer than 3 active runs. This value cannot exceed
          1000. Setting this value to `0` causes all new runs to be skipped.
        :param name: str (optional)
          An optional name for the job. The maximum length is 4096 bytes in UTF-8 encoding.
        :param notification_settings: :class:`JobNotificationSettings` (optional)
          Optional notification settings that are used when sending notifications to each of the
          `email_notifications` and `webhook_notifications` for this job.
        :param parameters: List[:class:`JobParameterDefinition`] (optional)
          Job-level parameter definitions
        :param queue: :class:`QueueSettings` (optional)
          The queue settings of the job.
        :param run_as: :class:`JobRunAs` (optional)
          Write-only setting. Specifies the user, service principal or group that the job/pipeline runs as. If
          not specified, the job/pipeline runs as the user who created the job/pipeline.
          
          Exactly one of `user_name`, `service_principal_name`, `group_name` should be specified. If not, an
          error is thrown.
        :param schedule: :class:`CronSchedule` (optional)
          An optional periodic schedule for this job. The default behavior is that the job only runs when
          triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.
        :param tags: Dict[str,str] (optional)
          A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs
          clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added
          to the job.
        :param tasks: List[:class:`Task`] (optional)
          A list of task specifications to be executed by this job.
        :param timeout_seconds: int (optional)
          An optional timeout applied to each run of this job. A value of `0` means no timeout.
        :param trigger: :class:`TriggerSettings` (optional)
          A configuration to trigger a run when certain conditions are met. The default behavior is that the
          job runs only when triggered by clicking “Run Now” in the Jobs UI or sending an API request to
          `runNow`.
        :param webhook_notifications: :class:`WebhookNotifications` (optional)
          A collection of system notification IDs to notify when runs of this job begin or complete.
        
        :returns: :class:`CreateResponse`
        

    .. py:method:: delete(job_id: int)

        Delete a job.
        
        Deletes a job.
        
        :param job_id: int
          The canonical identifier of the job to delete. This field is required.
        
        
        

    .. py:method:: delete_run(run_id: int)

        Delete a job run.
        
        Deletes a non-active run. Returns an error if the run is active.
        
        :param run_id: int
          ID of the run to delete.
        
        
        

    .. py:method:: export_run(run_id: int [, views_to_export: Optional[ViewsToExport]]) -> ExportRunOutput


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            created_job = w.jobs.create(name=f'sdk-{time.time_ns()}',
                                        tasks=[
                                            jobs.Task(description="test",
                                                      existing_cluster_id=cluster_id,
                                                      notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                      task_key="test",
                                                      timeout_seconds=0)
                                        ])
            
            run_by_id = w.jobs.run_now(job_id=created_job.job_id).result()
            
            exported_view = w.jobs.export_run(run_id=run_by_id.tasks[0].run_id, views_to_export="CODE")
            
            # cleanup
            w.jobs.delete(job_id=created_job.job_id)

        Export and retrieve a job run.
        
        Export and retrieve the job run task.
        
        :param run_id: int
          The canonical identifier for the run. This field is required.
        :param views_to_export: :class:`ViewsToExport` (optional)
          Which views to export (CODE, DASHBOARDS, or ALL). Defaults to CODE.
        
        :returns: :class:`ExportRunOutput`
        

    .. py:method:: get(job_id: int) -> Job


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            run = w.jobs.submit(run_name=f'sdk-{time.time_ns()}',
                                tasks=[
                                    jobs.SubmitTask(existing_cluster_id=cluster_id,
                                                    notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                    task_key=f'sdk-{time.time_ns()}')
                                ]).result()
            
            output = w.jobs.get_run_output(run_id=run.tasks[0].run_id)
            
            # cleanup
            w.jobs.delete_run(run_id=run.run_id)

        Get a single job.
        
        Retrieves the details for a single job.
        
        :param job_id: int
          The canonical identifier of the job to retrieve information about. This field is required.
        
        :returns: :class:`Job`
        

    .. py:method:: get_permission_levels(job_id: str) -> GetJobPermissionLevelsResponse

        Get job permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param job_id: str
          The job for which to get or manage permissions.
        
        :returns: :class:`GetJobPermissionLevelsResponse`
        

    .. py:method:: get_permissions(job_id: str) -> JobPermissions

        Get job permissions.
        
        Gets the permissions of a job. Jobs can inherit permissions from their root object.
        
        :param job_id: str
          The job for which to get or manage permissions.
        
        :returns: :class:`JobPermissions`
        

    .. py:method:: get_run(run_id: int [, include_history: Optional[bool], include_resolved_values: Optional[bool], page_token: Optional[str]]) -> Run


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            run = w.jobs.submit(run_name=f'sdk-{time.time_ns()}',
                                tasks=[
                                    jobs.SubmitTask(existing_cluster_id=cluster_id,
                                                    notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                    task_key=f'sdk-{time.time_ns()}')
                                ]).result()
            
            output = w.jobs.get_run_output(run_id=run.tasks[0].run_id)
            
            # cleanup
            w.jobs.delete_run(run_id=run.run_id)

        Get a single job run.
        
        Retrieve the metadata of a run.
        
        :param run_id: int
          The canonical identifier of the run for which to retrieve the metadata. This field is required.
        :param include_history: bool (optional)
          Whether to include the repair history in the response.
        :param include_resolved_values: bool (optional)
          Whether to include resolved parameter values in the response.
        :param page_token: str (optional)
          To list the next page or the previous page of job tasks, set this field to the value of the
          `next_page_token` or `prev_page_token` returned in the GetJob response.
        
        :returns: :class:`Run`
        

    .. py:method:: get_run_output(run_id: int) -> RunOutput


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            run = w.jobs.submit(run_name=f'sdk-{time.time_ns()}',
                                tasks=[
                                    jobs.SubmitTask(existing_cluster_id=cluster_id,
                                                    notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                    task_key=f'sdk-{time.time_ns()}')
                                ]).result()
            
            output = w.jobs.get_run_output(run_id=run.tasks[0].run_id)
            
            # cleanup
            w.jobs.delete_run(run_id=run.run_id)

        Get the output for a single run.
        
        Retrieve the output and metadata of a single task run. When a notebook task returns a value through
        the `dbutils.notebook.exit()` call, you can use this endpoint to retrieve that value. Databricks
        restricts this API to returning the first 5 MB of the output. To return a larger result, you can store
        job results in a cloud storage service.
        
        This endpoint validates that the __run_id__ parameter is valid and returns an HTTP status code 400 if
        the __run_id__ parameter is invalid. Runs are automatically removed after 60 days. If you to want to
        reference them beyond 60 days, you must save old run results before they expire.
        
        :param run_id: int
          The canonical identifier for the run.
        
        :returns: :class:`RunOutput`
        

    .. py:method:: list( [, expand_tasks: Optional[bool], limit: Optional[int], name: Optional[str], offset: Optional[int], page_token: Optional[str]]) -> Iterator[BaseJob]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            created_job = w.jobs.create(name=f'sdk-{time.time_ns()}',
                                        tasks=[
                                            jobs.Task(description="test",
                                                      existing_cluster_id=cluster_id,
                                                      notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                      task_key="test",
                                                      timeout_seconds=0)
                                        ])
            
            run_list = w.jobs.list_runs(job_id=created_job.job_id)
            
            # cleanup
            w.jobs.delete(job_id=created_job.job_id)

        List jobs.
        
        Retrieves a list of jobs.
        
        :param expand_tasks: bool (optional)
          Whether to include task and cluster details in the response.
        :param limit: int (optional)
          The number of jobs to return. This value must be greater than 0 and less or equal to 100. The
          default value is 20.
        :param name: str (optional)
          A filter on the list based on the exact (case insensitive) job name.
        :param offset: int (optional)
          The offset of the first job to return, relative to the most recently created job. Deprecated since
          June 2023. Use `page_token` to iterate through the pages instead.
        :param page_token: str (optional)
          Use `next_page_token` or `prev_page_token` returned from the previous request to list the next or
          previous page of jobs respectively.
        
        :returns: Iterator over :class:`BaseJob`
        

    .. py:method:: list_runs( [, active_only: Optional[bool], completed_only: Optional[bool], expand_tasks: Optional[bool], job_id: Optional[int], limit: Optional[int], offset: Optional[int], page_token: Optional[str], run_type: Optional[RunType], start_time_from: Optional[int], start_time_to: Optional[int]]) -> Iterator[BaseRun]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            created_job = w.jobs.create(name=f'sdk-{time.time_ns()}',
                                        tasks=[
                                            jobs.Task(description="test",
                                                      existing_cluster_id=cluster_id,
                                                      notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                      task_key="test",
                                                      timeout_seconds=0)
                                        ])
            
            run_list = w.jobs.list_runs(job_id=created_job.job_id)
            
            # cleanup
            w.jobs.delete(job_id=created_job.job_id)

        List job runs.
        
        List runs in descending order by start time.
        
        :param active_only: bool (optional)
          If active_only is `true`, only active runs are included in the results; otherwise, lists both active
          and completed runs. An active run is a run in the `QUEUED`, `PENDING`, `RUNNING`, or `TERMINATING`.
          This field cannot be `true` when completed_only is `true`.
        :param completed_only: bool (optional)
          If completed_only is `true`, only completed runs are included in the results; otherwise, lists both
          active and completed runs. This field cannot be `true` when active_only is `true`.
        :param expand_tasks: bool (optional)
          Whether to include task and cluster details in the response.
        :param job_id: int (optional)
          The job for which to list runs. If omitted, the Jobs service lists runs from all jobs.
        :param limit: int (optional)
          The number of runs to return. This value must be greater than 0 and less than 25. The default value
          is 20. If a request specifies a limit of 0, the service instead uses the maximum limit.
        :param offset: int (optional)
          The offset of the first run to return, relative to the most recent run. Deprecated since June 2023.
          Use `page_token` to iterate through the pages instead.
        :param page_token: str (optional)
          Use `next_page_token` or `prev_page_token` returned from the previous request to list the next or
          previous page of runs respectively.
        :param run_type: :class:`RunType` (optional)
          The type of runs to return. For a description of run types, see :method:jobs/getRun.
        :param start_time_from: int (optional)
          Show runs that started _at or after_ this value. The value must be a UTC timestamp in milliseconds.
          Can be combined with _start_time_to_ to filter by a time range.
        :param start_time_to: int (optional)
          Show runs that started _at or before_ this value. The value must be a UTC timestamp in milliseconds.
          Can be combined with _start_time_from_ to filter by a time range.
        
        :returns: Iterator over :class:`BaseRun`
        

    .. py:method:: repair_run(run_id: int [, dbt_commands: Optional[List[str]], jar_params: Optional[List[str]], job_parameters: Optional[Dict[str, str]], latest_repair_id: Optional[int], notebook_params: Optional[Dict[str, str]], pipeline_params: Optional[PipelineParams], python_named_params: Optional[Dict[str, str]], python_params: Optional[List[str]], rerun_all_failed_tasks: Optional[bool], rerun_dependent_tasks: Optional[bool], rerun_tasks: Optional[List[str]], spark_submit_params: Optional[List[str]], sql_params: Optional[Dict[str, str]]]) -> Wait[Run]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            created_job = w.jobs.create(name=f'sdk-{time.time_ns()}',
                                        tasks=[
                                            jobs.Task(description="test",
                                                      existing_cluster_id=cluster_id,
                                                      notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                      task_key="test",
                                                      timeout_seconds=0)
                                        ])
            
            run_now_response = w.jobs.run_now(job_id=created_job.job_id)
            
            cancelled_run = w.jobs.cancel_run(run_id=run_now_response.response.run_id).result()
            
            repaired_run = w.jobs.repair_run(rerun_tasks=[cancelled_run.tasks[0].task_key],
                                             run_id=run_now_response.response.run_id).result()
            
            # cleanup
            w.jobs.delete(job_id=created_job.job_id)

        Repair a job run.
        
        Re-run one or more tasks. Tasks are re-run as part of the original job run. They use the current job
        and task settings, and can be viewed in the history for the original job run.
        
        :param run_id: int
          The job run ID of the run to repair. The run must not be in progress.
        :param dbt_commands: List[str] (optional)
          An array of commands to execute for jobs with the dbt task, for example `"dbt_commands": ["dbt
          deps", "dbt seed", "dbt deps", "dbt seed", "dbt run"]`
        :param jar_params: List[str] (optional)
          A list of parameters for jobs with Spark JAR tasks, for example `"jar_params": ["john doe", "35"]`.
          The parameters are used to invoke the main function of the main class specified in the Spark JAR
          task. If not specified upon `run-now`, it defaults to an empty list. jar_params cannot be specified
          in conjunction with notebook_params. The JSON representation of this field (for example
          `{"jar_params":["john doe","35"]}`) cannot exceed 10,000 bytes.
          
          Use [Task parameter variables](/jobs.html"#parameter-variables") to set parameters containing
          information about job runs.
        :param job_parameters: Dict[str,str] (optional)
          Job-level parameters used in the run. for example `"param": "overriding_val"`
        :param latest_repair_id: int (optional)
          The ID of the latest repair. This parameter is not required when repairing a run for the first time,
          but must be provided on subsequent requests to repair the same run.
        :param notebook_params: Dict[str,str] (optional)
          A map from keys to values for jobs with notebook task, for example `"notebook_params": {"name":
          "john doe", "age": "35"}`. The map is passed to the notebook and is accessible through the
          [dbutils.widgets.get] function.
          
          If not specified upon `run-now`, the triggered run uses the job’s base parameters.
          
          notebook_params cannot be specified in conjunction with jar_params.
          
          Use [Task parameter variables] to set parameters containing information about job runs.
          
          The JSON representation of this field (for example `{"notebook_params":{"name":"john
          doe","age":"35"}}`) cannot exceed 10,000 bytes.
          
          [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
          [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html
        :param pipeline_params: :class:`PipelineParams` (optional)
          Controls whether the pipeline should perform a full refresh
        :param python_named_params: Dict[str,str] (optional)
        :param python_params: List[str] (optional)
          A list of parameters for jobs with Python tasks, for example `"python_params": ["john doe", "35"]`.
          The parameters are passed to Python file as command-line parameters. If specified upon `run-now`, it
          would overwrite the parameters specified in job setting. The JSON representation of this field (for
          example `{"python_params":["john doe","35"]}`) cannot exceed 10,000 bytes.
          
          Use [Task parameter variables] to set parameters containing information about job runs.
          
          Important
          
          These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters
          returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and
          emojis.
          
          [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
        :param rerun_all_failed_tasks: bool (optional)
          If true, repair all failed tasks. Only one of `rerun_tasks` or `rerun_all_failed_tasks` can be used.
        :param rerun_dependent_tasks: bool (optional)
          If true, repair all tasks that depend on the tasks in `rerun_tasks`, even if they were previously
          successful. Can be also used in combination with `rerun_all_failed_tasks`.
        :param rerun_tasks: List[str] (optional)
          The task keys of the task runs to repair.
        :param spark_submit_params: List[str] (optional)
          A list of parameters for jobs with spark submit task, for example `"spark_submit_params":
          ["--class", "org.apache.spark.examples.SparkPi"]`. The parameters are passed to spark-submit script
          as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified
          in job setting. The JSON representation of this field (for example `{"python_params":["john
          doe","35"]}`) cannot exceed 10,000 bytes.
          
          Use [Task parameter variables] to set parameters containing information about job runs
          
          Important
          
          These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters
          returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and
          emojis.
          
          [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
        :param sql_params: Dict[str,str] (optional)
          A map from keys to values for jobs with SQL task, for example `"sql_params": {"name": "john doe",
          "age": "35"}`. The SQL alert task does not support custom parameters.
        
        :returns:
          Long-running operation waiter for :class:`Run`.
          See :method:wait_get_run_job_terminated_or_skipped for more details.
        

    .. py:method:: repair_run_and_wait(run_id: int [, dbt_commands: Optional[List[str]], jar_params: Optional[List[str]], job_parameters: Optional[Dict[str, str]], latest_repair_id: Optional[int], notebook_params: Optional[Dict[str, str]], pipeline_params: Optional[PipelineParams], python_named_params: Optional[Dict[str, str]], python_params: Optional[List[str]], rerun_all_failed_tasks: Optional[bool], rerun_dependent_tasks: Optional[bool], rerun_tasks: Optional[List[str]], spark_submit_params: Optional[List[str]], sql_params: Optional[Dict[str, str]], timeout: datetime.timedelta = 0:20:00]) -> Run


    .. py:method:: reset(job_id: int, new_settings: JobSettings)


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            created_job = w.jobs.create(name=f'sdk-{time.time_ns()}',
                                        tasks=[
                                            jobs.Task(description="test",
                                                      existing_cluster_id=cluster_id,
                                                      notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                      task_key="test",
                                                      timeout_seconds=0)
                                        ])
            
            new_name = f'sdk-{time.time_ns()}'
            
            by_id = w.jobs.get(job_id=created_job.job_id)
            
            w.jobs.reset(job_id=by_id.job_id, new_settings=jobs.JobSettings(name=new_name, tasks=by_id.settings.tasks))
            
            # cleanup
            w.jobs.delete(job_id=created_job.job_id)

        Update all job settings (reset).
        
        Overwrite all settings for the given job. Use the [_Update_ endpoint](:method:jobs/update) to update
        job settings partially.
        
        :param job_id: int
          The canonical identifier of the job to reset. This field is required.
        :param new_settings: :class:`JobSettings`
          The new settings of the job. These settings completely replace the old settings.
          
          Changes to the field `JobBaseSettings.timeout_seconds` are applied to active runs. Changes to other
          fields are applied to future runs only.
        
        
        

    .. py:method:: run_now(job_id: int [, dbt_commands: Optional[List[str]], idempotency_token: Optional[str], jar_params: Optional[List[str]], job_parameters: Optional[Dict[str, str]], notebook_params: Optional[Dict[str, str]], pipeline_params: Optional[PipelineParams], python_named_params: Optional[Dict[str, str]], python_params: Optional[List[str]], queue: Optional[QueueSettings], spark_submit_params: Optional[List[str]], sql_params: Optional[Dict[str, str]]]) -> Wait[Run]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            created_job = w.jobs.create(name=f'sdk-{time.time_ns()}',
                                        tasks=[
                                            jobs.Task(description="test",
                                                      existing_cluster_id=cluster_id,
                                                      notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                      task_key="test",
                                                      timeout_seconds=0)
                                        ])
            
            run_by_id = w.jobs.run_now(job_id=created_job.job_id).result()
            
            # cleanup
            w.jobs.delete(job_id=created_job.job_id)

        Trigger a new job run.
        
        Run a job and return the `run_id` of the triggered run.
        
        :param job_id: int
          The ID of the job to be executed
        :param dbt_commands: List[str] (optional)
          An array of commands to execute for jobs with the dbt task, for example `"dbt_commands": ["dbt
          deps", "dbt seed", "dbt deps", "dbt seed", "dbt run"]`
        :param idempotency_token: str (optional)
          An optional token to guarantee the idempotency of job run requests. If a run with the provided token
          already exists, the request does not create a new run but returns the ID of the existing run
          instead. If a run with the provided token is deleted, an error is returned.
          
          If you specify the idempotency token, upon failure you can retry until the request succeeds.
          Databricks guarantees that exactly one run is launched with that idempotency token.
          
          This token must have at most 64 characters.
          
          For more information, see [How to ensure idempotency for jobs].
          
          [How to ensure idempotency for jobs]: https://kb.databricks.com/jobs/jobs-idempotency.html
        :param jar_params: List[str] (optional)
          A list of parameters for jobs with Spark JAR tasks, for example `"jar_params": ["john doe", "35"]`.
          The parameters are used to invoke the main function of the main class specified in the Spark JAR
          task. If not specified upon `run-now`, it defaults to an empty list. jar_params cannot be specified
          in conjunction with notebook_params. The JSON representation of this field (for example
          `{"jar_params":["john doe","35"]}`) cannot exceed 10,000 bytes.
          
          Use [Task parameter variables](/jobs.html"#parameter-variables") to set parameters containing
          information about job runs.
        :param job_parameters: Dict[str,str] (optional)
          Job-level parameters used in the run. for example `"param": "overriding_val"`
        :param notebook_params: Dict[str,str] (optional)
          A map from keys to values for jobs with notebook task, for example `"notebook_params": {"name":
          "john doe", "age": "35"}`. The map is passed to the notebook and is accessible through the
          [dbutils.widgets.get] function.
          
          If not specified upon `run-now`, the triggered run uses the job’s base parameters.
          
          notebook_params cannot be specified in conjunction with jar_params.
          
          Use [Task parameter variables] to set parameters containing information about job runs.
          
          The JSON representation of this field (for example `{"notebook_params":{"name":"john
          doe","age":"35"}}`) cannot exceed 10,000 bytes.
          
          [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
          [dbutils.widgets.get]: https://docs.databricks.com/dev-tools/databricks-utils.html
        :param pipeline_params: :class:`PipelineParams` (optional)
          Controls whether the pipeline should perform a full refresh
        :param python_named_params: Dict[str,str] (optional)
        :param python_params: List[str] (optional)
          A list of parameters for jobs with Python tasks, for example `"python_params": ["john doe", "35"]`.
          The parameters are passed to Python file as command-line parameters. If specified upon `run-now`, it
          would overwrite the parameters specified in job setting. The JSON representation of this field (for
          example `{"python_params":["john doe","35"]}`) cannot exceed 10,000 bytes.
          
          Use [Task parameter variables] to set parameters containing information about job runs.
          
          Important
          
          These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters
          returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and
          emojis.
          
          [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
        :param queue: :class:`QueueSettings` (optional)
          The queue settings of the run.
        :param spark_submit_params: List[str] (optional)
          A list of parameters for jobs with spark submit task, for example `"spark_submit_params":
          ["--class", "org.apache.spark.examples.SparkPi"]`. The parameters are passed to spark-submit script
          as command-line parameters. If specified upon `run-now`, it would overwrite the parameters specified
          in job setting. The JSON representation of this field (for example `{"python_params":["john
          doe","35"]}`) cannot exceed 10,000 bytes.
          
          Use [Task parameter variables] to set parameters containing information about job runs
          
          Important
          
          These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters
          returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and
          emojis.
          
          [Task parameter variables]: https://docs.databricks.com/jobs.html#parameter-variables
        :param sql_params: Dict[str,str] (optional)
          A map from keys to values for jobs with SQL task, for example `"sql_params": {"name": "john doe",
          "age": "35"}`. The SQL alert task does not support custom parameters.
        
        :returns:
          Long-running operation waiter for :class:`Run`.
          See :method:wait_get_run_job_terminated_or_skipped for more details.
        

    .. py:method:: run_now_and_wait(job_id: int [, dbt_commands: Optional[List[str]], idempotency_token: Optional[str], jar_params: Optional[List[str]], job_parameters: Optional[Dict[str, str]], notebook_params: Optional[Dict[str, str]], pipeline_params: Optional[PipelineParams], python_named_params: Optional[Dict[str, str]], python_params: Optional[List[str]], queue: Optional[QueueSettings], spark_submit_params: Optional[List[str]], sql_params: Optional[Dict[str, str]], timeout: datetime.timedelta = 0:20:00]) -> Run


    .. py:method:: set_permissions(job_id: str [, access_control_list: Optional[List[JobAccessControlRequest]]]) -> JobPermissions

        Set job permissions.
        
        Sets permissions on a job. Jobs can inherit permissions from their root object.
        
        :param job_id: str
          The job for which to get or manage permissions.
        :param access_control_list: List[:class:`JobAccessControlRequest`] (optional)
        
        :returns: :class:`JobPermissions`
        

    .. py:method:: submit( [, access_control_list: Optional[List[JobAccessControlRequest]], budget_policy_id: Optional[str], email_notifications: Optional[JobEmailNotifications], environments: Optional[List[JobEnvironment]], git_source: Optional[GitSource], health: Optional[JobsHealthRules], idempotency_token: Optional[str], notification_settings: Optional[JobNotificationSettings], queue: Optional[QueueSettings], run_as: Optional[JobRunAs], run_name: Optional[str], tasks: Optional[List[SubmitTask]], timeout_seconds: Optional[int], webhook_notifications: Optional[WebhookNotifications]]) -> Wait[Run]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            run = w.jobs.submit(run_name=f'sdk-{time.time_ns()}',
                                tasks=[
                                    jobs.SubmitTask(existing_cluster_id=cluster_id,
                                                    notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                    task_key=f'sdk-{time.time_ns()}')
                                ]).result()
            
            # cleanup
            w.jobs.delete_run(run_id=run.run_id)

        Create and trigger a one-time run.
        
        Submit a one-time run. This endpoint allows you to submit a workload directly without creating a job.
        Runs submitted using this endpoint don’t display in the UI. Use the `jobs/runs/get` API to check the
        run state after the job is submitted.
        
        :param access_control_list: List[:class:`JobAccessControlRequest`] (optional)
          List of permissions to set on the job.
        :param budget_policy_id: str (optional)
          The user specified id of the budget policy to use for this one-time run. If not specified, the run
          will be not be attributed to any budget policy.
        :param email_notifications: :class:`JobEmailNotifications` (optional)
          An optional set of email addresses notified when the run begins or completes.
        :param environments: List[:class:`JobEnvironment`] (optional)
          A list of task execution environment specifications that can be referenced by tasks of this run.
        :param git_source: :class:`GitSource` (optional)
          An optional specification for a remote Git repository containing the source code used by tasks.
          Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks.
          
          If `git_source` is set, these tasks retrieve the file from the remote repository by default.
          However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task.
          
          Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are
          used, `git_source` must be defined on the job.
        :param health: :class:`JobsHealthRules` (optional)
          An optional set of health rules that can be defined for this job.
        :param idempotency_token: str (optional)
          An optional token that can be used to guarantee the idempotency of job run requests. If a run with
          the provided token already exists, the request does not create a new run but returns the ID of the
          existing run instead. If a run with the provided token is deleted, an error is returned.
          
          If you specify the idempotency token, upon failure you can retry until the request succeeds.
          Databricks guarantees that exactly one run is launched with that idempotency token.
          
          This token must have at most 64 characters.
          
          For more information, see [How to ensure idempotency for jobs].
          
          [How to ensure idempotency for jobs]: https://kb.databricks.com/jobs/jobs-idempotency.html
        :param notification_settings: :class:`JobNotificationSettings` (optional)
          Optional notification settings that are used when sending notifications to each of the
          `email_notifications` and `webhook_notifications` for this run.
        :param queue: :class:`QueueSettings` (optional)
          The queue settings of the one-time run.
        :param run_as: :class:`JobRunAs` (optional)
          Specifies the user or service principal that the job runs as. If not specified, the job runs as the
          user who submits the request.
        :param run_name: str (optional)
          An optional name for the run. The default value is `Untitled`.
        :param tasks: List[:class:`SubmitTask`] (optional)
        :param timeout_seconds: int (optional)
          An optional timeout applied to each run of this job. A value of `0` means no timeout.
        :param webhook_notifications: :class:`WebhookNotifications` (optional)
          A collection of system notification IDs to notify when the run begins or completes.
        
        :returns:
          Long-running operation waiter for :class:`Run`.
          See :method:wait_get_run_job_terminated_or_skipped for more details.
        

    .. py:method:: submit_and_wait( [, access_control_list: Optional[List[JobAccessControlRequest]], budget_policy_id: Optional[str], email_notifications: Optional[JobEmailNotifications], environments: Optional[List[JobEnvironment]], git_source: Optional[GitSource], health: Optional[JobsHealthRules], idempotency_token: Optional[str], notification_settings: Optional[JobNotificationSettings], queue: Optional[QueueSettings], run_as: Optional[JobRunAs], run_name: Optional[str], tasks: Optional[List[SubmitTask]], timeout_seconds: Optional[int], webhook_notifications: Optional[WebhookNotifications], timeout: datetime.timedelta = 0:20:00]) -> Run


    .. py:method:: update(job_id: int [, fields_to_remove: Optional[List[str]], new_settings: Optional[JobSettings]])


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import jobs
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            cluster_id = w.clusters.ensure_cluster_is_running(
                os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
            
            new_name = f'sdk-{time.time_ns()}'
            
            created_job = w.jobs.create(name=f'sdk-{time.time_ns()}',
                                        tasks=[
                                            jobs.Task(description="test",
                                                      existing_cluster_id=cluster_id,
                                                      notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
                                                      task_key="test",
                                                      timeout_seconds=0)
                                        ])
            
            w.jobs.update(job_id=created_job.job_id, new_settings=jobs.JobSettings(name=new_name, max_concurrent_runs=5))
            
            # cleanup
            w.jobs.delete(job_id=created_job.job_id)

        Update job settings partially.
        
        Add, update, or remove specific settings of an existing job. Use the [_Reset_
        endpoint](:method:jobs/reset) to overwrite all job settings.
        
        :param job_id: int
          The canonical identifier of the job to update. This field is required.
        :param fields_to_remove: List[str] (optional)
          Remove top-level fields in the job settings. Removing nested fields is not supported, except for
          tasks and job clusters (`tasks/task_1`). This field is optional.
        :param new_settings: :class:`JobSettings` (optional)
          The new settings for the job.
          
          Top-level fields specified in `new_settings` are completely replaced, except for arrays which are
          merged. That is, new and existing entries are completely replaced based on the respective key
          fields, i.e. `task_key` or `job_cluster_key`, while previous entries are kept.
          
          Partially updating nested fields is not supported.
          
          Changes to the field `JobSettings.timeout_seconds` are applied to active runs. Changes to other
          fields are applied to future runs only.
        
        
        

    .. py:method:: update_permissions(job_id: str [, access_control_list: Optional[List[JobAccessControlRequest]]]) -> JobPermissions

        Update job permissions.
        
        Updates the permissions on a job. Jobs can inherit permissions from their root object.
        
        :param job_id: str
          The job for which to get or manage permissions.
        :param access_control_list: List[:class:`JobAccessControlRequest`] (optional)
        
        :returns: :class:`JobPermissions`
        

    .. py:method:: wait_get_run_job_terminated_or_skipped(run_id: int, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[Run], None]]) -> Run

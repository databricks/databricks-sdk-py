``w.pipelines``: Pipelines
==========================
.. currentmodule:: databricks.sdk.service.pipelines

.. py:class:: PipelinesAPI

    The Delta Live Tables API allows you to create, edit, delete, start, and view details about pipelines.
    
    Delta Live Tables is a framework for building reliable, maintainable, and testable data processing
    pipelines. You define the transformations to perform on your data, and Delta Live Tables manages task
    orchestration, cluster management, monitoring, data quality, and error handling.
    
    Instead of defining your data pipelines using a series of separate Apache Spark tasks, Delta Live Tables
    manages how your data is transformed based on a target schema you define for each processing step. You can
    also enforce data quality with Delta Live Tables expectations. Expectations allow you to define expected
    data quality and specify how to handle records that fail those expectations.

    .. py:method:: create( [, allow_duplicate_names: Optional[bool], budget_policy_id: Optional[str], catalog: Optional[str], channel: Optional[str], clusters: Optional[List[PipelineCluster]], configuration: Optional[Dict[str, str]], continuous: Optional[bool], deployment: Optional[PipelineDeployment], development: Optional[bool], dry_run: Optional[bool], edition: Optional[str], filters: Optional[Filters], gateway_definition: Optional[IngestionGatewayPipelineDefinition], id: Optional[str], ingestion_definition: Optional[IngestionPipelineDefinition], libraries: Optional[List[PipelineLibrary]], name: Optional[str], notifications: Optional[List[Notifications]], photon: Optional[bool], schema: Optional[str], serverless: Optional[bool], storage: Optional[str], target: Optional[str], trigger: Optional[PipelineTrigger]]) -> CreatePipelineResponse


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import pipelines
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            created = w.pipelines.create(
                continuous=False,
                name=f'sdk-{time.time_ns()}',
                libraries=[pipelines.PipelineLibrary(notebook=pipelines.NotebookLibrary(path=notebook_path))],
                clusters=[
                    pipelines.PipelineCluster(instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                              label="default",
                                              num_workers=1,
                                              custom_tags={
                                                  "cluster_type": "default",
                                              })
                ])
            
            # cleanup
            w.pipelines.delete(pipeline_id=created.pipeline_id)

        Create a pipeline.
        
        Creates a new data processing pipeline based on the requested configuration. If successful, this
        method returns the ID of the new pipeline.
        
        :param allow_duplicate_names: bool (optional)
          If false, deployment will fail if name conflicts with that of another pipeline.
        :param budget_policy_id: str (optional)
          Budget policy of this pipeline.
        :param catalog: str (optional)
          A catalog in Unity Catalog to publish data from this pipeline to. If `target` is specified, tables
          in this pipeline are published to a `target` schema inside `catalog` (for example,
          `catalog`.`target`.`table`). If `target` is not specified, no data is published to Unity Catalog.
        :param channel: str (optional)
          DLT Release Channel that specifies which version to use.
        :param clusters: List[:class:`PipelineCluster`] (optional)
          Cluster settings for this pipeline deployment.
        :param configuration: Dict[str,str] (optional)
          String-String configuration for this pipeline execution.
        :param continuous: bool (optional)
          Whether the pipeline is continuous or triggered. This replaces `trigger`.
        :param deployment: :class:`PipelineDeployment` (optional)
          Deployment type of this pipeline.
        :param development: bool (optional)
          Whether the pipeline is in Development mode. Defaults to false.
        :param dry_run: bool (optional)
        :param edition: str (optional)
          Pipeline product edition.
        :param filters: :class:`Filters` (optional)
          Filters on which Pipeline packages to include in the deployed graph.
        :param gateway_definition: :class:`IngestionGatewayPipelineDefinition` (optional)
          The definition of a gateway pipeline to support CDC.
        :param id: str (optional)
          Unique identifier for this pipeline.
        :param ingestion_definition: :class:`IngestionPipelineDefinition` (optional)
          The configuration for a managed ingestion pipeline. These settings cannot be used with the
          'libraries', 'target' or 'catalog' settings.
        :param libraries: List[:class:`PipelineLibrary`] (optional)
          Libraries or code needed by this deployment.
        :param name: str (optional)
          Friendly identifier for this pipeline.
        :param notifications: List[:class:`Notifications`] (optional)
          List of notification settings for this pipeline.
        :param photon: bool (optional)
          Whether Photon is enabled for this pipeline.
        :param schema: str (optional)
          The default schema (database) where tables are read from or published to. The presence of this field
          implies that the pipeline is in direct publishing mode.
        :param serverless: bool (optional)
          Whether serverless compute is enabled for this pipeline.
        :param storage: str (optional)
          DBFS root directory for storing checkpoints and tables.
        :param target: str (optional)
          Target schema (database) to add tables in this pipeline to. If not specified, no data is published
          to the Hive metastore or Unity Catalog. To publish to Unity Catalog, also specify `catalog`.
        :param trigger: :class:`PipelineTrigger` (optional)
          Which pipeline trigger to use. Deprecated: Use `continuous` instead.
        
        :returns: :class:`CreatePipelineResponse`
        

    .. py:method:: delete(pipeline_id: str)

        Delete a pipeline.
        
        Deletes a pipeline.
        
        :param pipeline_id: str
        
        
        

    .. py:method:: get(pipeline_id: str) -> GetPipelineResponse


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import pipelines
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            created = w.pipelines.create(
                continuous=False,
                name=f'sdk-{time.time_ns()}',
                libraries=[pipelines.PipelineLibrary(notebook=pipelines.NotebookLibrary(path=notebook_path))],
                clusters=[
                    pipelines.PipelineCluster(instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                              label="default",
                                              num_workers=1,
                                              custom_tags={
                                                  "cluster_type": "default",
                                              })
                ])
            
            by_id = w.pipelines.get(pipeline_id=created.pipeline_id)
            
            # cleanup
            w.pipelines.delete(pipeline_id=created.pipeline_id)

        Get a pipeline.
        
        :param pipeline_id: str
        
        :returns: :class:`GetPipelineResponse`
        

    .. py:method:: get_permission_levels(pipeline_id: str) -> GetPipelinePermissionLevelsResponse

        Get pipeline permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param pipeline_id: str
          The pipeline for which to get or manage permissions.
        
        :returns: :class:`GetPipelinePermissionLevelsResponse`
        

    .. py:method:: get_permissions(pipeline_id: str) -> PipelinePermissions

        Get pipeline permissions.
        
        Gets the permissions of a pipeline. Pipelines can inherit permissions from their root object.
        
        :param pipeline_id: str
          The pipeline for which to get or manage permissions.
        
        :returns: :class:`PipelinePermissions`
        

    .. py:method:: get_update(pipeline_id: str, update_id: str) -> GetUpdateResponse

        Get a pipeline update.
        
        Gets an update from an active pipeline.
        
        :param pipeline_id: str
          The ID of the pipeline.
        :param update_id: str
          The ID of the update.
        
        :returns: :class:`GetUpdateResponse`
        

    .. py:method:: list_pipeline_events(pipeline_id: str [, filter: Optional[str], max_results: Optional[int], order_by: Optional[List[str]], page_token: Optional[str]]) -> Iterator[PipelineEvent]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import pipelines
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            created = w.pipelines.create(
                continuous=False,
                name=f'sdk-{time.time_ns()}',
                libraries=[pipelines.PipelineLibrary(notebook=pipelines.NotebookLibrary(path=notebook_path))],
                clusters=[
                    pipelines.PipelineCluster(instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                              label="default",
                                              num_workers=1,
                                              custom_tags={
                                                  "cluster_type": "default",
                                              })
                ])
            
            events = w.pipelines.list_pipeline_events(pipeline_id=created.pipeline_id)
            
            # cleanup
            w.pipelines.delete(pipeline_id=created.pipeline_id)

        List pipeline events.
        
        Retrieves events for a pipeline.
        
        :param pipeline_id: str
        :param filter: str (optional)
          Criteria to select a subset of results, expressed using a SQL-like syntax. The supported filters
          are: 1. level='INFO' (or WARN or ERROR) 2. level in ('INFO', 'WARN') 3. id='[event-id]' 4. timestamp
          > 'TIMESTAMP' (or >=,<,<=,=)
          
          Composite expressions are supported, for example: level in ('ERROR', 'WARN') AND timestamp>
          '2021-07-22T06:37:33.083Z'
        :param max_results: int (optional)
          Max number of entries to return in a single page. The system may return fewer than max_results
          events in a response, even if there are more events available.
        :param order_by: List[str] (optional)
          A string indicating a sort order by timestamp for the results, for example, ["timestamp asc"]. The
          sort order can be ascending or descending. By default, events are returned in descending order by
          timestamp.
        :param page_token: str (optional)
          Page token returned by previous call. This field is mutually exclusive with all fields in this
          request except max_results. An error is returned if any fields other than max_results are set when
          this field is set.
        
        :returns: Iterator over :class:`PipelineEvent`
        

    .. py:method:: list_pipelines( [, filter: Optional[str], max_results: Optional[int], order_by: Optional[List[str]], page_token: Optional[str]]) -> Iterator[PipelineStateInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import pipelines
            
            w = WorkspaceClient()
            
            all = w.pipelines.list_pipelines(pipelines.ListPipelinesRequest())

        List pipelines.
        
        Lists pipelines defined in the Delta Live Tables system.
        
        :param filter: str (optional)
          Select a subset of results based on the specified criteria. The supported filters are:
          
          * `notebook='<path>'` to select pipelines that reference the provided notebook path. * `name LIKE
          '[pattern]'` to select pipelines with a name that matches pattern. Wildcards are supported, for
          example: `name LIKE '%shopping%'`
          
          Composite filters are not supported. This field is optional.
        :param max_results: int (optional)
          The maximum number of entries to return in a single page. The system may return fewer than
          max_results events in a response, even if there are more events available. This field is optional.
          The default value is 25. The maximum value is 100. An error is returned if the value of max_results
          is greater than 100.
        :param order_by: List[str] (optional)
          A list of strings specifying the order of results. Supported order_by fields are id and name. The
          default is id asc. This field is optional.
        :param page_token: str (optional)
          Page token returned by previous call
        
        :returns: Iterator over :class:`PipelineStateInfo`
        

    .. py:method:: list_updates(pipeline_id: str [, max_results: Optional[int], page_token: Optional[str], until_update_id: Optional[str]]) -> ListUpdatesResponse

        List pipeline updates.
        
        List updates for an active pipeline.
        
        :param pipeline_id: str
          The pipeline to return updates for.
        :param max_results: int (optional)
          Max number of entries to return in a single page.
        :param page_token: str (optional)
          Page token returned by previous call
        :param until_update_id: str (optional)
          If present, returns updates until and including this update_id.
        
        :returns: :class:`ListUpdatesResponse`
        

    .. py:method:: set_permissions(pipeline_id: str [, access_control_list: Optional[List[PipelineAccessControlRequest]]]) -> PipelinePermissions

        Set pipeline permissions.
        
        Sets permissions on a pipeline. Pipelines can inherit permissions from their root object.
        
        :param pipeline_id: str
          The pipeline for which to get or manage permissions.
        :param access_control_list: List[:class:`PipelineAccessControlRequest`] (optional)
        
        :returns: :class:`PipelinePermissions`
        

    .. py:method:: start_update(pipeline_id: str [, cause: Optional[StartUpdateCause], full_refresh: Optional[bool], full_refresh_selection: Optional[List[str]], refresh_selection: Optional[List[str]], validate_only: Optional[bool]]) -> StartUpdateResponse

        Start a pipeline.
        
        Starts a new update for the pipeline. If there is already an active update for the pipeline, the
        request will fail and the active update will remain running.
        
        :param pipeline_id: str
        :param cause: :class:`StartUpdateCause` (optional)
        :param full_refresh: bool (optional)
          If true, this update will reset all tables before running.
        :param full_refresh_selection: List[str] (optional)
          A list of tables to update with fullRefresh. If both refresh_selection and full_refresh_selection
          are empty, this is a full graph update. Full Refresh on a table means that the states of the table
          will be reset before the refresh.
        :param refresh_selection: List[str] (optional)
          A list of tables to update without fullRefresh. If both refresh_selection and full_refresh_selection
          are empty, this is a full graph update. Full Refresh on a table means that the states of the table
          will be reset before the refresh.
        :param validate_only: bool (optional)
          If true, this update only validates the correctness of pipeline source code but does not materialize
          or publish any datasets.
        
        :returns: :class:`StartUpdateResponse`
        

    .. py:method:: stop(pipeline_id: str) -> Wait[GetPipelineResponse]

        Stop a pipeline.
        
        Stops the pipeline by canceling the active update. If there is no active update for the pipeline, this
        request is a no-op.
        
        :param pipeline_id: str
        
        :returns:
          Long-running operation waiter for :class:`GetPipelineResponse`.
          See :method:wait_get_pipeline_idle for more details.
        

    .. py:method:: stop_and_wait(pipeline_id: str, timeout: datetime.timedelta = 0:20:00) -> GetPipelineResponse


    .. py:method:: update(pipeline_id: str [, allow_duplicate_names: Optional[bool], budget_policy_id: Optional[str], catalog: Optional[str], channel: Optional[str], clusters: Optional[List[PipelineCluster]], configuration: Optional[Dict[str, str]], continuous: Optional[bool], deployment: Optional[PipelineDeployment], development: Optional[bool], edition: Optional[str], expected_last_modified: Optional[int], filters: Optional[Filters], gateway_definition: Optional[IngestionGatewayPipelineDefinition], id: Optional[str], ingestion_definition: Optional[IngestionPipelineDefinition], libraries: Optional[List[PipelineLibrary]], name: Optional[str], notifications: Optional[List[Notifications]], photon: Optional[bool], schema: Optional[str], serverless: Optional[bool], storage: Optional[str], target: Optional[str], trigger: Optional[PipelineTrigger]])


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import pipelines
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            created = w.pipelines.create(
                continuous=False,
                name=f'sdk-{time.time_ns()}',
                libraries=[pipelines.PipelineLibrary(notebook=pipelines.NotebookLibrary(path=notebook_path))],
                clusters=[
                    pipelines.PipelineCluster(instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                              label="default",
                                              num_workers=1,
                                              custom_tags={
                                                  "cluster_type": "default",
                                              })
                ])
            
            w.pipelines.update(
                pipeline_id=created.pipeline_id,
                name=f'sdk-{time.time_ns()}',
                libraries=[pipelines.PipelineLibrary(notebook=pipelines.NotebookLibrary(path=notebook_path))],
                clusters=[
                    pipelines.PipelineCluster(instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                              label="default",
                                              num_workers=1,
                                              custom_tags={
                                                  "cluster_type": "default",
                                              })
                ])
            
            # cleanup
            w.pipelines.delete(pipeline_id=created.pipeline_id)

        Edit a pipeline.
        
        Updates a pipeline with the supplied configuration.
        
        :param pipeline_id: str
          Unique identifier for this pipeline.
        :param allow_duplicate_names: bool (optional)
          If false, deployment will fail if name has changed and conflicts the name of another pipeline.
        :param budget_policy_id: str (optional)
          Budget policy of this pipeline.
        :param catalog: str (optional)
          A catalog in Unity Catalog to publish data from this pipeline to. If `target` is specified, tables
          in this pipeline are published to a `target` schema inside `catalog` (for example,
          `catalog`.`target`.`table`). If `target` is not specified, no data is published to Unity Catalog.
        :param channel: str (optional)
          DLT Release Channel that specifies which version to use.
        :param clusters: List[:class:`PipelineCluster`] (optional)
          Cluster settings for this pipeline deployment.
        :param configuration: Dict[str,str] (optional)
          String-String configuration for this pipeline execution.
        :param continuous: bool (optional)
          Whether the pipeline is continuous or triggered. This replaces `trigger`.
        :param deployment: :class:`PipelineDeployment` (optional)
          Deployment type of this pipeline.
        :param development: bool (optional)
          Whether the pipeline is in Development mode. Defaults to false.
        :param edition: str (optional)
          Pipeline product edition.
        :param expected_last_modified: int (optional)
          If present, the last-modified time of the pipeline settings before the edit. If the settings were
          modified after that time, then the request will fail with a conflict.
        :param filters: :class:`Filters` (optional)
          Filters on which Pipeline packages to include in the deployed graph.
        :param gateway_definition: :class:`IngestionGatewayPipelineDefinition` (optional)
          The definition of a gateway pipeline to support CDC.
        :param id: str (optional)
          Unique identifier for this pipeline.
        :param ingestion_definition: :class:`IngestionPipelineDefinition` (optional)
          The configuration for a managed ingestion pipeline. These settings cannot be used with the
          'libraries', 'target' or 'catalog' settings.
        :param libraries: List[:class:`PipelineLibrary`] (optional)
          Libraries or code needed by this deployment.
        :param name: str (optional)
          Friendly identifier for this pipeline.
        :param notifications: List[:class:`Notifications`] (optional)
          List of notification settings for this pipeline.
        :param photon: bool (optional)
          Whether Photon is enabled for this pipeline.
        :param schema: str (optional)
          The default schema (database) where tables are read from or published to. The presence of this field
          implies that the pipeline is in direct publishing mode.
        :param serverless: bool (optional)
          Whether serverless compute is enabled for this pipeline.
        :param storage: str (optional)
          DBFS root directory for storing checkpoints and tables.
        :param target: str (optional)
          Target schema (database) to add tables in this pipeline to. If not specified, no data is published
          to the Hive metastore or Unity Catalog. To publish to Unity Catalog, also specify `catalog`.
        :param trigger: :class:`PipelineTrigger` (optional)
          Which pipeline trigger to use. Deprecated: Use `continuous` instead.
        
        
        

    .. py:method:: update_permissions(pipeline_id: str [, access_control_list: Optional[List[PipelineAccessControlRequest]]]) -> PipelinePermissions

        Update pipeline permissions.
        
        Updates the permissions on a pipeline. Pipelines can inherit permissions from their root object.
        
        :param pipeline_id: str
          The pipeline for which to get or manage permissions.
        :param access_control_list: List[:class:`PipelineAccessControlRequest`] (optional)
        
        :returns: :class:`PipelinePermissions`
        

    .. py:method:: wait_get_pipeline_idle(pipeline_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[GetPipelineResponse], None]]) -> GetPipelineResponse


    .. py:method:: wait_get_pipeline_running(pipeline_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[GetPipelineResponse], None]]) -> GetPipelineResponse

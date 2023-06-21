Pipelines
=========
.. py:class:: PipelinesAPI

    The Delta Live Tables API allows you to create, edit, delete, start, and view details about pipelines.
    
    Delta Live Tables is a framework for building reliable, maintainable, and testable data processing
    pipelines. You define the transformations to perform on your data, and Delta Live Tables manages task
    orchestration, cluster management, monitoring, data quality, and error handling.
    
    Instead of defining your data pipelines using a series of separate Apache Spark tasks, Delta Live Tables
    manages how your data is transformed based on a target schema you define for each processing step. You can
    also enforce data quality with Delta Live Tables expectations. Expectations allow you to define expected
    data quality and specify how to handle records that fail those expectations.

    .. py:method:: create( [, allow_duplicate_names, catalog, channel, clusters, configuration, continuous, development, dry_run, edition, filters, id, libraries, name, photon, serverless, storage, target, trigger])

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
            w.pipelines.delete(delete=created.pipeline_id)

        Create a pipeline.
        
        Creates a new data processing pipeline based on the requested configuration. If successful, this
        method returns the ID of the new pipeline.
        
        :param allow_duplicate_names: bool (optional)
          If false, deployment will fail if name conflicts with that of another pipeline.
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
        :param development: bool (optional)
          Whether the pipeline is in Development mode. Defaults to false.
        :param dry_run: bool (optional)
        :param edition: str (optional)
          Pipeline product edition.
        :param filters: :class:`Filters` (optional)
          Filters on which Pipeline packages to include in the deployed graph.
        :param id: str (optional)
          Unique identifier for this pipeline.
        :param libraries: List[:class:`PipelineLibrary`] (optional)
          Libraries or code needed by this deployment.
        :param name: str (optional)
          Friendly identifier for this pipeline.
        :param photon: bool (optional)
          Whether Photon is enabled for this pipeline.
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
        

    .. py:method:: delete(pipeline_id)

        Delete a pipeline.
        
        Deletes a pipeline.
        
        :param pipeline_id: str
        
        
        

    .. py:method:: get(pipeline_id)

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
            
            by_id = w.pipelines.get(get=created.pipeline_id)
            
            # cleanup
            w.pipelines.delete(delete=created.pipeline_id)

        Get a pipeline.
        
        :param pipeline_id: str
        
        :returns: :class:`GetPipelineResponse`
        

    .. py:method:: get_update(pipeline_id, update_id)

        Get a pipeline update.
        
        Gets an update from an active pipeline.
        
        :param pipeline_id: str
          The ID of the pipeline.
        :param update_id: str
          The ID of the update.
        
        :returns: :class:`GetUpdateResponse`
        

    .. py:method:: list_pipeline_events(pipeline_id [, filter, max_results, order_by, page_token])

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
            w.pipelines.delete(delete=created.pipeline_id)

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
        

    .. py:method:: list_pipelines( [, filter, max_results, order_by, page_token])

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
        

    .. py:method:: list_updates(pipeline_id [, max_results, page_token, until_update_id])

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
        

    .. py:method:: reset(pipeline_id)

        Reset a pipeline.
        
        Resets a pipeline.
        
        :param pipeline_id: str
        
        :returns:
          long-running operation waiter for :class:`GetPipelineResponse`.
          See :method:wait_get_pipeline_running for more details.
        

    .. py:method:: start_update(pipeline_id [, cause, full_refresh, full_refresh_selection, refresh_selection])

        Queue a pipeline update.
        
        Starts or queues a pipeline update.
        
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
        
        :returns: :class:`StartUpdateResponse`
        

    .. py:method:: stop(pipeline_id)

        Stop a pipeline.
        
        Stops a pipeline.
        
        :param pipeline_id: str
        
        :returns:
          long-running operation waiter for :class:`GetPipelineResponse`.
          See :method:wait_get_pipeline_idle for more details.
        

    .. py:method:: update(pipeline_id [, allow_duplicate_names, catalog, channel, clusters, configuration, continuous, development, edition, expected_last_modified, filters, id, libraries, name, photon, serverless, storage, target, trigger])

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
            w.pipelines.delete(delete=created.pipeline_id)

        Edit a pipeline.
        
        Updates a pipeline with the supplied configuration.
        
        :param pipeline_id: str
          Unique identifier for this pipeline.
        :param allow_duplicate_names: bool (optional)
          If false, deployment will fail if name has changed and conflicts the name of another pipeline.
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
        :param development: bool (optional)
          Whether the pipeline is in Development mode. Defaults to false.
        :param edition: str (optional)
          Pipeline product edition.
        :param expected_last_modified: int (optional)
          If present, the last-modified time of the pipeline settings before the edit. If the settings were
          modified after that time, then the request will fail with a conflict.
        :param filters: :class:`Filters` (optional)
          Filters on which Pipeline packages to include in the deployed graph.
        :param id: str (optional)
          Unique identifier for this pipeline.
        :param libraries: List[:class:`PipelineLibrary`] (optional)
          Libraries or code needed by this deployment.
        :param name: str (optional)
          Friendly identifier for this pipeline.
        :param photon: bool (optional)
          Whether Photon is enabled for this pipeline.
        :param serverless: bool (optional)
          Whether serverless compute is enabled for this pipeline.
        :param storage: str (optional)
          DBFS root directory for storing checkpoints and tables.
        :param target: str (optional)
          Target schema (database) to add tables in this pipeline to. If not specified, no data is published
          to the Hive metastore or Unity Catalog. To publish to Unity Catalog, also specify `catalog`.
        :param trigger: :class:`PipelineTrigger` (optional)
          Which pipeline trigger to use. Deprecated: Use `continuous` instead.
        
        
        
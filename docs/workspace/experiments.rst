Experiments
===========
.. py:class:: ExperimentsAPI

    Experiments are the primary unit of organization in MLflow; all MLflow runs belong to an experiment. Each
    experiment lets you visualize, search, and compare runs, as well as download run artifacts or metadata for
    analysis in other tools. Experiments are maintained in a Databricks hosted MLflow tracking server.
    
    Experiments are located in the workspace file tree. You manage experiments using the same tools you use to
    manage other workspace objects such as folders, notebooks, and libraries.

    .. py:method:: create_experiment(name [, artifact_location, tags])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            experiment = w.experiments.create_experiment(name=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.experiments.delete_experiment(experiment_id=experiment.experiment_id)

        Create experiment.
        
        Creates an experiment with a name. Returns the ID of the newly created experiment. Validates that
        another experiment with the same name does not already exist and fails if another experiment with the
        same name already exists.
        
        Throws `RESOURCE_ALREADY_EXISTS` if a experiment with the given name exists.
        
        :param name: str
          Experiment name.
        :param artifact_location: str (optional)
          Location where all artifacts for the experiment are stored. If not provided, the remote server will
          select an appropriate default.
        :param tags: List[:class:`ExperimentTag`] (optional)
          A collection of tags to set on the experiment. Maximum tag size and number of tags per request
          depends on the storage backend. All storage backends are guaranteed to support tag keys up to 250
          bytes in size and tag values up to 5000 bytes in size. All storage backends are also guaranteed to
          support up to 20 tags per request.
        
        :returns: :class:`CreateExperimentResponse`
        

    .. py:method:: create_run( [, experiment_id, start_time, tags, user_id])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import ml
            
            w = WorkspaceClient()
            
            experiment = w.experiments.create_experiment(name=f'sdk-{time.time_ns()}')
            
            created = w.experiments.create_run(experiment_id=experiment.experiment_id,
                                               tags=[ml.RunTag(key="foo", value="bar")])
            
            # cleanup
            w.experiments.delete_experiment(experiment_id=experiment.experiment_id)
            w.experiments.delete_run(run_id=created.run.info.run_id)

        Create a run.
        
        Creates a new run within an experiment. A run is usually a single execution of a machine learning or
        data ETL pipeline. MLflow uses runs to track the `mlflowParam`, `mlflowMetric` and `mlflowRunTag`
        associated with a single execution.
        
        :param experiment_id: str (optional)
          ID of the associated experiment.
        :param start_time: int (optional)
          Unix timestamp in milliseconds of when the run started.
        :param tags: List[:class:`RunTag`] (optional)
          Additional metadata for run.
        :param user_id: str (optional)
          ID of the user executing the run. This field is deprecated as of MLflow 1.0, and will be removed in
          a future MLflow release. Use 'mlflow.user' tag instead.
        
        :returns: :class:`CreateRunResponse`
        

    .. py:method:: delete_experiment(experiment_id)

        Delete an experiment.
        
        Marks an experiment and associated metadata, runs, metrics, params, and tags for deletion. If the
        experiment uses FileStore, artifacts associated with experiment are also deleted.
        
        :param experiment_id: str
          ID of the associated experiment.
        
        
        

    .. py:method:: delete_run(run_id)

        Delete a run.
        
        Marks a run for deletion.
        
        :param run_id: str
          ID of the run to delete.
        
        
        

    .. py:method:: delete_tag(run_id, key)

        Delete a tag.
        
        Deletes a tag on a run. Tags are run metadata that can be updated during a run and after a run
        completes.
        
        :param run_id: str
          ID of the run that the tag was logged under. Must be provided.
        :param key: str
          Name of the tag. Maximum size is 255 bytes. Must be provided.
        
        
        

    .. py:method:: get_by_name(experiment_name)

        Get metadata.
        
        Gets metadata for an experiment.
        
        This endpoint will return deleted experiments, but prefers the active experiment if an active and
        deleted experiment share the same name. If multiple deleted experiments share the same name, the API
        will return one of them.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no experiment with the specified name exists.
        
        :param experiment_name: str
          Name of the associated experiment.
        
        :returns: :class:`GetExperimentByNameResponse`
        

    .. py:method:: get_experiment(experiment_id)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            experiment = w.experiments.create_experiment(name=f'sdk-{time.time_ns()}')
            
            _ = w.experiments.get_experiment(experiment_id=experiment.experiment_id)
            
            # cleanup
            w.experiments.delete_experiment(experiment_id=experiment.experiment_id)

        Get an experiment.
        
        Gets metadata for an experiment. This method works on deleted experiments.
        
        :param experiment_id: str
          ID of the associated experiment.
        
        :returns: :class:`Experiment`
        

    .. py:method:: get_history(metric_key [, max_results, page_token, run_id, run_uuid])

        Get history of a given metric within a run.
        
        Gets a list of all values for the specified metric for a given run.
        
        :param metric_key: str
          Name of the metric.
        :param max_results: int (optional)
          Maximum number of Metric records to return per paginated request. Default is set to 25,000. If set
          higher than 25,000, a request Exception will be raised.
        :param page_token: str (optional)
          Token indicating the page of metric histories to fetch.
        :param run_id: str (optional)
          ID of the run from which to fetch metric values. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run from which to fetch metric values. This field will be
          removed in a future MLflow version.
        
        :returns: :class:`GetMetricHistoryResponse`
        

    .. py:method:: get_run(run_id [, run_uuid])

        Get a run.
        
        Gets the metadata, metrics, params, and tags for a run. In the case where multiple metrics with the
        same key are logged for a run, return only the value with the latest timestamp.
        
        If there are multiple values with the latest timestamp, return the maximum of these values.
        
        :param run_id: str
          ID of the run to fetch. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run to fetch. This field will be removed in a future
          MLflow version.
        
        :returns: :class:`GetRunResponse`
        

    .. py:method:: list_artifacts( [, page_token, path, run_id, run_uuid])

        Get all artifacts.
        
        List artifacts for a run. Takes an optional `artifact_path` prefix. If it is specified, the response
        contains only artifacts with the specified prefix.",
        
        :param page_token: str (optional)
          Token indicating the page of artifact results to fetch
        :param path: str (optional)
          Filter artifacts matching this path (a relative path from the root artifact directory).
        :param run_id: str (optional)
          ID of the run whose artifacts to list. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run whose artifacts to list. This field will be removed
          in a future MLflow version.
        
        :returns: Iterator over :class:`FileInfo`
        

    .. py:method:: list_experiments( [, max_results, page_token, view_type])

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import ml
            
            w = WorkspaceClient()
            
            all = w.experiments.list_experiments(ml.ListExperimentsRequest())

        List experiments.
        
        Gets a list of all experiments.
        
        :param max_results: int (optional)
          Maximum number of experiments desired. If `max_results` is unspecified, return all experiments. If
          `max_results` is too large, it'll be automatically capped at 1000. Callers of this endpoint are
          encouraged to pass max_results explicitly and leverage page_token to iterate through experiments.
        :param page_token: str (optional)
          Token indicating the page of experiments to fetch
        :param view_type: str (optional)
          Qualifier for type of experiments to be returned. If unspecified, return only active experiments.
        
        :returns: Iterator over :class:`Experiment`
        

    .. py:method:: log_batch( [, metrics, params, run_id, tags])

        Log a batch.
        
        Logs a batch of metrics, params, and tags for a run. If any data failed to be persisted, the server
        will respond with an error (non-200 status code).
        
        In case of error (due to internal server error or an invalid request), partial data may be written.
        
        You can write metrics, params, and tags in interleaving fashion, but within a given entity type are
        guaranteed to follow the order specified in the request body.
        
        The overwrite behavior for metrics, params, and tags is as follows:
        
        * Metrics: metric values are never overwritten. Logging a metric (key, value, timestamp) appends to
        the set of values for the metric with the provided key.
        
        * Tags: tag values can be overwritten by successive writes to the same tag key. That is, if multiple
        tag values with the same key are provided in the same API request, the last-provided tag value is
        written. Logging the same tag (key, value) is permitted. Specifically, logging a tag is idempotent.
        
        * Parameters: once written, param values cannot be changed (attempting to overwrite a param value will
        result in an error). However, logging the same param (key, value) is permitted. Specifically, logging
        a param is idempotent.
        
        Request Limits ------------------------------- A single JSON-serialized API request may be up to 1 MB
        in size and contain:
        
        * No more than 1000 metrics, params, and tags in total * Up to 1000 metrics * Up to 100 params * Up to
        100 tags
        
        For example, a valid request might contain 900 metrics, 50 params, and 50 tags, but logging 900
        metrics, 50 params, and 51 tags is invalid.
        
        The following limits also apply to metric, param, and tag keys and values:
        
        * Metric keyes, param keys, and tag keys can be up to 250 characters in length * Parameter and tag
        values can be up to 250 characters in length
        
        :param metrics: List[:class:`Metric`] (optional)
          Metrics to log. A single request can contain up to 1000 metrics, and up to 1000 metrics, params, and
          tags in total.
        :param params: List[:class:`Param`] (optional)
          Params to log. A single request can contain up to 100 params, and up to 1000 metrics, params, and
          tags in total.
        :param run_id: str (optional)
          ID of the run to log under
        :param tags: List[:class:`RunTag`] (optional)
          Tags to log. A single request can contain up to 100 tags, and up to 1000 metrics, params, and tags
          in total.
        
        
        

    .. py:method:: log_inputs( [, datasets, run_id])

        Log inputs to a run.
        
        **NOTE:** Experimental: This API may change or be removed in a future release without warning.
        
        :param datasets: List[:class:`DatasetInput`] (optional)
          Dataset inputs
        :param run_id: str (optional)
          ID of the run to log under
        
        
        

    .. py:method:: log_metric(key, value, timestamp [, run_id, run_uuid, step])

        Log a metric.
        
        Logs a metric for a run. A metric is a key-value pair (string key, float value) with an associated
        timestamp. Examples include the various metrics that represent ML model accuracy. A metric can be
        logged multiple times.
        
        :param key: str
          Name of the metric.
        :param value: float
          Double value of the metric being logged.
        :param timestamp: int
          Unix timestamp in milliseconds at the time metric was logged.
        :param run_id: str (optional)
          ID of the run under which to log the metric. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run under which to log the metric. This field will be
          removed in a future MLflow version.
        :param step: int (optional)
          Step at which to log the metric
        
        
        

    .. py:method:: log_model( [, model_json, run_id])

        Log a model.
        
        **NOTE:** Experimental: This API may change or be removed in a future release without warning.
        
        :param model_json: str (optional)
          MLmodel file in json format.
        :param run_id: str (optional)
          ID of the run to log under
        
        
        

    .. py:method:: log_param(key, value [, run_id, run_uuid])

        Log a param.
        
        Logs a param used for a run. A param is a key-value pair (string key, string value). Examples include
        hyperparameters used for ML model training and constant dates and values used in an ETL pipeline. A
        param can be logged only once for a run.
        
        :param key: str
          Name of the param. Maximum size is 255 bytes.
        :param value: str
          String value of the param being logged. Maximum size is 500 bytes.
        :param run_id: str (optional)
          ID of the run under which to log the param. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run under which to log the param. This field will be
          removed in a future MLflow version.
        
        
        

    .. py:method:: restore_experiment(experiment_id)

        Restores an experiment.
        
        Restore an experiment marked for deletion. This also restores associated metadata, runs, metrics,
        params, and tags. If experiment uses FileStore, underlying artifacts associated with experiment are
        also restored.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if experiment was never created or was permanently deleted.
        
        :param experiment_id: str
          ID of the associated experiment.
        
        
        

    .. py:method:: restore_run(run_id)

        Restore a run.
        
        Restores a deleted run.
        
        :param run_id: str
          ID of the run to restore.
        
        
        

    .. py:method:: search_experiments( [, filter, max_results, order_by, page_token, view_type])

        Search experiments.
        
        Searches for experiments that satisfy specified search criteria.
        
        :param filter: str (optional)
          String representing a SQL filter condition (e.g. "name ILIKE 'my-experiment%'")
        :param max_results: int (optional)
          Maximum number of experiments desired. Max threshold is 3000.
        :param order_by: List[str] (optional)
          List of columns for ordering search results, which can include experiment name and last updated
          timestamp with an optional "DESC" or "ASC" annotation, where "ASC" is the default. Tiebreaks are
          done by experiment id DESC.
        :param page_token: str (optional)
          Token indicating the page of experiments to fetch
        :param view_type: :class:`SearchExperimentsViewType` (optional)
          Qualifier for type of experiments to be returned. If unspecified, return only active experiments.
        
        :returns: Iterator over :class:`Experiment`
        

    .. py:method:: search_runs( [, experiment_ids, filter, max_results, order_by, page_token, run_view_type])

        Search for runs.
        
        Searches for runs that satisfy expressions.
        
        Search expressions can use `mlflowMetric` and `mlflowParam` keys.",
        
        :param experiment_ids: List[str] (optional)
          List of experiment IDs to search over.
        :param filter: str (optional)
          A filter expression over params, metrics, and tags, that allows returning a subset of runs. The
          syntax is a subset of SQL that supports ANDing together binary operations between a param, metric,
          or tag and a constant.
          
          Example: `metrics.rmse < 1 and params.model_class = 'LogisticRegression'`
          
          You can select columns with special characters (hyphen, space, period, etc.) by using double quotes:
          `metrics."model class" = 'LinearRegression' and tags."user-name" = 'Tomas'`
          
          Supported operators are `=`, `!=`, `>`, `>=`, `<`, and `<=`.
        :param max_results: int (optional)
          Maximum number of runs desired. Max threshold is 50000
        :param order_by: List[str] (optional)
          List of columns to be ordered by, including attributes, params, metrics, and tags with an optional
          "DESC" or "ASC" annotation, where "ASC" is the default. Example: ["params.input DESC",
          "metrics.alpha ASC", "metrics.rmse"] Tiebreaks are done by start_time DESC followed by run_id for
          runs with the same start time (and this is the default ordering criterion if order_by is not
          provided).
        :param page_token: str (optional)
          Token for the current page of runs.
        :param run_view_type: :class:`SearchRunsRunViewType` (optional)
          Whether to display only active, only deleted, or all runs. Defaults to only active runs.
        
        :returns: Iterator over :class:`Run`
        

    .. py:method:: set_experiment_tag(experiment_id, key, value)

        Set a tag.
        
        Sets a tag on an experiment. Experiment tags are metadata that can be updated.
        
        :param experiment_id: str
          ID of the experiment under which to log the tag. Must be provided.
        :param key: str
          Name of the tag. Maximum size depends on storage backend. All storage backends are guaranteed to
          support key values up to 250 bytes in size.
        :param value: str
          String value of the tag being logged. Maximum size depends on storage backend. All storage backends
          are guaranteed to support key values up to 5000 bytes in size.
        
        
        

    .. py:method:: set_tag(key, value [, run_id, run_uuid])

        Set a tag.
        
        Sets a tag on a run. Tags are run metadata that can be updated during a run and after a run completes.
        
        :param key: str
          Name of the tag. Maximum size depends on storage backend. All storage backends are guaranteed to
          support key values up to 250 bytes in size.
        :param value: str
          String value of the tag being logged. Maximum size depends on storage backend. All storage backends
          are guaranteed to support key values up to 5000 bytes in size.
        :param run_id: str (optional)
          ID of the run under which to log the tag. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run under which to log the tag. This field will be
          removed in a future MLflow version.
        
        
        

    .. py:method:: update_experiment(experiment_id [, new_name])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            experiment = w.experiments.create_experiment(name=f'sdk-{time.time_ns()}')
            
            w.experiments.update_experiment(new_name=f'sdk-{time.time_ns()}', experiment_id=experiment.experiment_id)
            
            # cleanup
            w.experiments.delete_experiment(experiment_id=experiment.experiment_id)

        Update an experiment.
        
        Updates experiment metadata.
        
        :param experiment_id: str
          ID of the associated experiment.
        :param new_name: str (optional)
          If provided, the experiment's name is changed to the new name. The new name must be unique.
        
        
        

    .. py:method:: update_run( [, end_time, run_id, run_uuid, status])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import ml
            
            w = WorkspaceClient()
            
            experiment = w.experiments.create_experiment(name=f'sdk-{time.time_ns()}')
            
            created = w.experiments.create_run(experiment_id=experiment.experiment_id,
                                               tags=[ml.RunTag(key="foo", value="bar")])
            
            _ = w.experiments.update_run(run_id=created.run.info.run_id, status=ml.UpdateRunStatus.KILLED)
            
            # cleanup
            w.experiments.delete_experiment(experiment_id=experiment.experiment_id)
            w.experiments.delete_run(run_id=created.run.info.run_id)

        Update a run.
        
        Updates run metadata.
        
        :param end_time: int (optional)
          Unix timestamp in milliseconds of when the run ended.
        :param run_id: str (optional)
          ID of the run to update. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run to update.. This field will be removed in a future
          MLflow version.
        :param status: :class:`UpdateRunStatus` (optional)
          Updated status of the run.
        
        :returns: :class:`UpdateRunResponse`
        
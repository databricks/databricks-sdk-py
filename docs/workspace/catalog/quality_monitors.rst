``w.quality_monitors``: Quality Monitors
========================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: QualityMonitorsAPI

    A monitor computes and monitors data or model quality metrics for a table over time. It generates metrics
    tables and a dashboard that you can use to monitor table health and set alerts.
    
    Most write operations require the user to be the owner of the table (or its parent schema or parent
    catalog). Viewing the dashboard, computed metrics, or monitor configuration only requires the user to have
    **SELECT** privileges on the table (along with **USE_SCHEMA** and **USE_CATALOG**).

    .. py:method:: cancel_refresh(table_name: str, refresh_id: str)

        Cancel refresh.
        
        Cancel an active monitor refresh for the given refresh ID.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema - be an
        owner of the table
        
        Additionally, the call must be made from the workspace where the monitor was created.
        
        :param table_name: str
          Full name of the table.
        :param refresh_id: str
          ID of the refresh.
        
        
        

    .. py:method:: create(table_name: str, assets_dir: str, output_schema_name: str [, baseline_table_name: Optional[str], custom_metrics: Optional[List[MonitorMetric]], data_classification_config: Optional[MonitorDataClassificationConfig], inference_log: Optional[MonitorInferenceLog], notifications: Optional[MonitorNotifications], schedule: Optional[MonitorCronSchedule], skip_builtin_dashboard: Optional[bool], slicing_exprs: Optional[List[str]], snapshot: Optional[MonitorSnapshot], time_series: Optional[MonitorTimeSeries], warehouse_id: Optional[str]]) -> MonitorInfo

        Create a table monitor.
        
        Creates a new monitor for the specified table.
        
        The caller must either: 1. be an owner of the table's parent catalog, have **USE_SCHEMA** on the
        table's parent schema, and have **SELECT** access on the table 2. have **USE_CATALOG** on the table's
        parent catalog, be an owner of the table's parent schema, and have **SELECT** access on the table. 3.
        have the following permissions: - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on
        the table's parent schema - be an owner of the table.
        
        Workspace assets, such as the dashboard, will be created in the workspace where this call was made.
        
        :param table_name: str
          Full name of the table.
        :param assets_dir: str
          The directory to store monitoring assets (e.g. dashboard, metric tables).
        :param output_schema_name: str
          Schema where output metric tables are created.
        :param baseline_table_name: str (optional)
          Name of the baseline table from which drift metrics are computed from. Columns in the monitored
          table should also be present in the baseline table.
        :param custom_metrics: List[:class:`MonitorMetric`] (optional)
          Custom metrics to compute on the monitored table. These can be aggregate metrics, derived metrics
          (from already computed aggregate metrics), or drift metrics (comparing metrics across time windows).
        :param data_classification_config: :class:`MonitorDataClassificationConfig` (optional)
          The data classification config for the monitor.
        :param inference_log: :class:`MonitorInferenceLog` (optional)
          Configuration for monitoring inference logs.
        :param notifications: :class:`MonitorNotifications` (optional)
          The notification settings for the monitor.
        :param schedule: :class:`MonitorCronSchedule` (optional)
          The schedule for automatically updating and refreshing metric tables.
        :param skip_builtin_dashboard: bool (optional)
          Whether to skip creating a default dashboard summarizing data quality metrics.
        :param slicing_exprs: List[str] (optional)
          List of column expressions to slice data with for targeted analysis. The data is grouped by each
          expression independently, resulting in a separate slice for each predicate and its complements. For
          high-cardinality columns, only the top 100 unique values by frequency will generate slices.
        :param snapshot: :class:`MonitorSnapshot` (optional)
          Configuration for monitoring snapshot tables.
        :param time_series: :class:`MonitorTimeSeries` (optional)
          Configuration for monitoring time series tables.
        :param warehouse_id: str (optional)
          Optional argument to specify the warehouse for dashboard creation. If not specified, the first
          running warehouse will be used.
        
        :returns: :class:`MonitorInfo`
        

    .. py:method:: delete(table_name: str)

        Delete a table monitor.
        
        Deletes a monitor for the specified table.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema - be an
        owner of the table.
        
        Additionally, the call must be made from the workspace where the monitor was created.
        
        Note that the metric tables and dashboard will not be deleted as part of this call; those assets must
        be manually cleaned up (if desired).
        
        :param table_name: str
          Full name of the table.
        
        
        

    .. py:method:: get(table_name: str) -> MonitorInfo

        Get a table monitor.
        
        Gets a monitor for the specified table.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema. 3. have the following
        permissions: - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent
        schema - **SELECT** privilege on the table.
        
        The returned information includes configuration values, as well as information on assets created by
        the monitor. Some information (e.g., dashboard) may be filtered out if the caller is in a different
        workspace than where the monitor was created.
        
        :param table_name: str
          Full name of the table.
        
        :returns: :class:`MonitorInfo`
        

    .. py:method:: get_refresh(table_name: str, refresh_id: str) -> MonitorRefreshInfo

        Get refresh.
        
        Gets info about a specific monitor refresh using the given refresh ID.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema -
        **SELECT** privilege on the table.
        
        Additionally, the call must be made from the workspace where the monitor was created.
        
        :param table_name: str
          Full name of the table.
        :param refresh_id: str
          ID of the refresh.
        
        :returns: :class:`MonitorRefreshInfo`
        

    .. py:method:: list_refreshes(table_name: str) -> MonitorRefreshListResponse

        List refreshes.
        
        Gets an array containing the history of the most recent refreshes (up to 25) for this table.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema -
        **SELECT** privilege on the table.
        
        Additionally, the call must be made from the workspace where the monitor was created.
        
        :param table_name: str
          Full name of the table.
        
        :returns: :class:`MonitorRefreshListResponse`
        

    .. py:method:: regenerate_dashboard(table_name: str [, warehouse_id: Optional[str]]) -> RegenerateDashboardResponse

        Regenerate a monitoring dashboard.
        
        Regenerates the monitoring dashboard for the specified table.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema - be an
        owner of the table
        
        The call must be made from the workspace where the monitor was created. The dashboard will be
        regenerated in the assets directory that was specified when the monitor was created.
        
        :param table_name: str
          Full name of the table.
        :param warehouse_id: str (optional)
          Optional argument to specify the warehouse for dashboard regeneration. If not specified, the first
          running warehouse will be used.
        
        :returns: :class:`RegenerateDashboardResponse`
        

    .. py:method:: run_refresh(table_name: str) -> MonitorRefreshInfo

        Queue a metric refresh for a monitor.
        
        Queues a metric refresh on the monitor for the specified table. The refresh will execute in the
        background.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema - be an
        owner of the table
        
        Additionally, the call must be made from the workspace where the monitor was created.
        
        :param table_name: str
          Full name of the table.
        
        :returns: :class:`MonitorRefreshInfo`
        

    .. py:method:: update(table_name: str, output_schema_name: str [, baseline_table_name: Optional[str], custom_metrics: Optional[List[MonitorMetric]], dashboard_id: Optional[str], data_classification_config: Optional[MonitorDataClassificationConfig], inference_log: Optional[MonitorInferenceLog], notifications: Optional[MonitorNotifications], schedule: Optional[MonitorCronSchedule], slicing_exprs: Optional[List[str]], snapshot: Optional[MonitorSnapshot], time_series: Optional[MonitorTimeSeries]]) -> MonitorInfo

        Update a table monitor.
        
        Updates a monitor for the specified table.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema - be an
        owner of the table.
        
        Additionally, the call must be made from the workspace where the monitor was created, and the caller
        must be the original creator of the monitor.
        
        Certain configuration fields, such as output asset identifiers, cannot be updated.
        
        :param table_name: str
          Full name of the table.
        :param output_schema_name: str
          Schema where output metric tables are created.
        :param baseline_table_name: str (optional)
          Name of the baseline table from which drift metrics are computed from. Columns in the monitored
          table should also be present in the baseline table.
        :param custom_metrics: List[:class:`MonitorMetric`] (optional)
          Custom metrics to compute on the monitored table. These can be aggregate metrics, derived metrics
          (from already computed aggregate metrics), or drift metrics (comparing metrics across time windows).
        :param dashboard_id: str (optional)
          Id of dashboard that visualizes the computed metrics. This can be empty if the monitor is in PENDING
          state.
        :param data_classification_config: :class:`MonitorDataClassificationConfig` (optional)
          The data classification config for the monitor.
        :param inference_log: :class:`MonitorInferenceLog` (optional)
          Configuration for monitoring inference logs.
        :param notifications: :class:`MonitorNotifications` (optional)
          The notification settings for the monitor.
        :param schedule: :class:`MonitorCronSchedule` (optional)
          The schedule for automatically updating and refreshing metric tables.
        :param slicing_exprs: List[str] (optional)
          List of column expressions to slice data with for targeted analysis. The data is grouped by each
          expression independently, resulting in a separate slice for each predicate and its complements. For
          high-cardinality columns, only the top 100 unique values by frequency will generate slices.
        :param snapshot: :class:`MonitorSnapshot` (optional)
          Configuration for monitoring snapshot tables.
        :param time_series: :class:`MonitorTimeSeries` (optional)
          Configuration for monitoring time series tables.
        
        :returns: :class:`MonitorInfo`
        
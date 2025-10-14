``w.data_quality``: DataQuality.v1
==================================
.. currentmodule:: databricks.sdk.service.dataquality

.. py:class:: DataQualityAPI

    Manage the data quality of Unity Catalog objects (currently support `schema` and `table`)

    .. py:method:: cancel_refresh(object_type: str, object_id: str, refresh_id: int) -> CancelRefreshResponse

        Cancels a data quality monitor refresh. Currently only supported for the `table` `object_type`.

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. For example, schema id.
        :param refresh_id: int
          Unique id of the refresh operation.

        :returns: :class:`CancelRefreshResponse`
        

    .. py:method:: create_monitor(monitor: Monitor) -> Monitor

        Create a data quality monitor on a Unity Catalog object. The caller must provide either
        `anomaly_detection_config` for a schema monitor or `data_profiling_config` for a table monitor.

        For the `table` `object_type`, the caller must either: 1. be an owner of the table's parent catalog,
        have **USE_SCHEMA** on the table's parent schema, and have **SELECT** access on the table 2. have
        **USE_CATALOG** on the table's parent catalog, be an owner of the table's parent schema, and have
        **SELECT** access on the table. 3. have the following permissions: - **USE_CATALOG** on the table's
        parent catalog - **USE_SCHEMA** on the table's parent schema - be an owner of the table.

        Workspace assets, such as the dashboard, will be created in the workspace where this call was made.

        :param monitor: :class:`Monitor`
          The monitor to create.

        :returns: :class:`Monitor`
        

    .. py:method:: create_refresh(object_type: str, object_id: str, refresh: Refresh) -> Refresh

        Creates a refresh. Currently only supported for the `table` `object_type`.

        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema - be an
        owner of the table

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema`or `table`.
        :param object_id: str
          The UUID of the request object. For example, table id.
        :param refresh: :class:`Refresh`
          The refresh to create

        :returns: :class:`Refresh`
        

    .. py:method:: delete_monitor(object_type: str, object_id: str)

        Delete a data quality monitor on Unity Catalog object.

        For the `table` `object_type`, the caller must either: 1. be an owner of the table's parent catalog 2.
        have **USE_CATALOG** on the table's parent catalog and be an owner of the table's parent schema 3.
        have the following permissions: - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on
        the table's parent schema - be an owner of the table.

        Note that the metric tables and dashboard will not be deleted as part of this call; those assets must
        be manually cleaned up (if desired).

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. For example, schema id.


        

    .. py:method:: delete_refresh(object_type: str, object_id: str, refresh_id: int)

        (Unimplemented) Delete a refresh

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. For example, schema id.
        :param refresh_id: int
          Unique id of the refresh operation.


        

    .. py:method:: get_monitor(object_type: str, object_id: str) -> Monitor

        Read a data quality monitor on Unity Catalog object.

        For the `table` `object_type`, the caller must either: 1. be an owner of the table's parent catalog 2.
        have **USE_CATALOG** on the table's parent catalog and be an owner of the table's parent schema. 3.
        have the following permissions: - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on
        the table's parent schema - **SELECT** privilege on the table.

        The returned information includes configuration values, as well as information on assets created by
        the monitor. Some information (e.g., dashboard) may be filtered out if the caller is in a different
        workspace than where the monitor was created.

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. For example, schema id.

        :returns: :class:`Monitor`
        

    .. py:method:: get_refresh(object_type: str, object_id: str, refresh_id: int) -> Refresh

        Get data quality monitor refresh.

        For the `table` `object_type`, the caller must either: 1. be an owner of the table's parent catalog 2.
        have **USE_CATALOG** on the table's parent catalog and be an owner of the table's parent schema 3.
        have the following permissions: - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on
        the table's parent schema - **SELECT** privilege on the table.

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. For example, schema id.
        :param refresh_id: int
          Unique id of the refresh operation.

        :returns: :class:`Refresh`
        

    .. py:method:: list_monitor( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Monitor]

        (Unimplemented) List data quality monitors.

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Monitor`
        

    .. py:method:: list_refresh(object_type: str, object_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Refresh]

        List data quality monitor refreshes.

        For the `table` `object_type`, the caller must either: 1. be an owner of the table's parent catalog 2.
        have **USE_CATALOG** on the table's parent catalog and be an owner of the table's parent schema 3.
        have the following permissions: - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on
        the table's parent schema - **SELECT** privilege on the table.

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. For example, schema id.
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Refresh`
        

    .. py:method:: update_monitor(object_type: str, object_id: str, monitor: Monitor, update_mask: str) -> Monitor

        Update a data quality monitor on Unity Catalog object.

        For the `table` `object_type`, The caller must either: 1. be an owner of the table's parent catalog 2.
        have **USE_CATALOG** on the table's parent catalog and be an owner of the table's parent schema 3.
        have the following permissions: - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on
        the table's parent schema - be an owner of the table.

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. For example, schema id.
        :param monitor: :class:`Monitor`
          The monitor to update.
        :param update_mask: str
          The field mask to specify which fields to update as a comma-separated list. Example value:
          `data_profiling_config.custom_metrics,data_profiling_config.schedule.quartz_cron_expression`

        :returns: :class:`Monitor`
        

    .. py:method:: update_refresh(object_type: str, object_id: str, refresh_id: int, refresh: Refresh, update_mask: str) -> Refresh

        (Unimplemented) Update a refresh

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. For example, schema id.
        :param refresh_id: int
          Unique id of the refresh operation.
        :param refresh: :class:`Refresh`
          The refresh to update.
        :param update_mask: str
          The field mask to specify which fields to update.

        :returns: :class:`Refresh`
        
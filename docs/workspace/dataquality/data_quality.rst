``w.data_quality``: DataQuality.v1
==================================
.. currentmodule:: databricks.sdk.service.dataquality

.. py:class:: DataQualityAPI

    Manage the data quality of Unity Catalog objects (currently support `schema` and `table`)

    .. py:method:: cancel_refresh(object_type: str, object_id: str, refresh_id: int) -> CancelRefreshResponse

        Cancels a data quality monitor refresh. Currently only supported for the `table` `object_type`. The
        call must be made in the same workspace as where the monitor was created.

        The caller must have either of the following sets of permissions: 1. **MANAGE** and **USE_CATALOG** on
        the table's parent catalog. 2. **USE_CATALOG** on the table's parent catalog, and **MANAGE** and
        **USE_SCHEMA** on the table's parent schema. 3. **USE_CATALOG** on the table's parent catalog,
        **USE_SCHEMA** on the table's parent schema, and **MANAGE** on the table.

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. It is `schema_id` for `schema`, and `table_id` for `table`.

          Find the `schema_id` from either: 1. The [schema_id] of the `Schemas` resource. 2. In [Catalog
          Explorer] > select the `schema` > go to the `Details` tab > the `Schema ID` field.

          Find the `table_id` from either: 1. The [table_id] of the `Tables` resource. 2. In [Catalog
          Explorer] > select the `table` > go to the `Details` tab > the `Table ID` field.

          [Catalog Explorer]: https://docs.databricks.com/aws/en/catalog-explorer/
          [schema_id]: https://docs.databricks.com/api/workspace/schemas/get#schema_id
          [table_id]: https://docs.databricks.com/api/workspace/tables/get#table_id
        :param refresh_id: int
          Unique id of the refresh operation.

        :returns: :class:`CancelRefreshResponse`
        

    .. py:method:: create_monitor(monitor: Monitor) -> Monitor

        Create a data quality monitor on a Unity Catalog object. The caller must provide either
        `anomaly_detection_config` for a schema monitor or `data_profiling_config` for a table monitor.

        For the `table` `object_type`, the caller must have either of the following sets of permissions: 1.
        **MANAGE** and **USE_CATALOG** on the table's parent catalog, **USE_SCHEMA** on the table's parent
        schema, and **SELECT** on the table 2. **USE_CATALOG** on the table's parent catalog, **MANAGE** and
        **USE_SCHEMA** on the table's parent schema, and **SELECT** on the table. 3. **USE_CATALOG** on the
        table's parent catalog, **USE_SCHEMA** on the table's parent schema, and **MANAGE** and **SELECT** on
        the table.

        Workspace assets, such as the dashboard, will be created in the workspace where this call was made.

        For the `schema` `object_type`, the caller must have either of the following sets of permissions: 1.
        **MANAGE** and **USE_CATALOG** on the schema's parent catalog. 2. **USE_CATALOG** on the schema's
        parent catalog, and **MANAGE** and **USE_SCHEMA** on the schema.

        :param monitor: :class:`Monitor`
          The monitor to create.

        :returns: :class:`Monitor`
        

    .. py:method:: create_refresh(object_type: str, object_id: str, refresh: Refresh) -> Refresh

        Creates a refresh. Currently only supported for the `table` `object_type`. The call must be made in
        the same workspace as where the monitor was created.

        The caller must have either of the following sets of permissions: 1. **MANAGE** and **USE_CATALOG** on
        the table's parent catalog. 2. **USE_CATALOG** on the table's parent catalog, and **MANAGE** and
        **USE_SCHEMA** on the table's parent schema. 3. **USE_CATALOG** on the table's parent catalog,
        **USE_SCHEMA** on the table's parent schema, and **MANAGE** on the table.

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema`or `table`.
        :param object_id: str
          The UUID of the request object. It is `schema_id` for `schema`, and `table_id` for `table`.

          Find the `schema_id` from either: 1. The [schema_id] of the `Schemas` resource. 2. In [Catalog
          Explorer] > select the `schema` > go to the `Details` tab > the `Schema ID` field.

          Find the `table_id` from either: 1. The [table_id] of the `Tables` resource. 2. In [Catalog
          Explorer] > select the `table` > go to the `Details` tab > the `Table ID` field.

          [Catalog Explorer]: https://docs.databricks.com/aws/en/catalog-explorer/
          [schema_id]: https://docs.databricks.com/api/workspace/schemas/get#schema_id
          [table_id]: https://docs.databricks.com/api/workspace/tables/get#table_id
        :param refresh: :class:`Refresh`
          The refresh to create

        :returns: :class:`Refresh`
        

    .. py:method:: delete_monitor(object_type: str, object_id: str)

        Delete a data quality monitor on Unity Catalog object.

        For the `table` `object_type`, the caller must have either of the following sets of permissions:
        **MANAGE** and **USE_CATALOG** on the table's parent catalog. **USE_CATALOG** on the table's parent
        catalog, and **MANAGE** and **USE_SCHEMA** on the table's parent schema. **USE_CATALOG** on the
        table's parent catalog, **USE_SCHEMA** on the table's parent schema, and **MANAGE** on the table.

        Note that the metric tables and dashboard will not be deleted as part of this call; those assets must
        be manually cleaned up (if desired).

        For the `schema` `object_type`, the caller must have either of the following sets of permissions: 1.
        **MANAGE** and **USE_CATALOG** on the schema's parent catalog. 2. **USE_CATALOG** on the schema's
        parent catalog, and **MANAGE** and **USE_SCHEMA** on the schema.

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. It is `schema_id` for `schema`, and `table_id` for `table`.

          Find the `schema_id` from either: 1. The [schema_id] of the `Schemas` resource. 2. In [Catalog
          Explorer] > select the `schema` > go to the `Details` tab > the `Schema ID` field.

          Find the `table_id` from either: 1. The [table_id] of the `Tables` resource. 2. In [Catalog
          Explorer] > select the `table` > go to the `Details` tab > the `Table ID` field.

          [Catalog Explorer]: https://docs.databricks.com/aws/en/catalog-explorer/
          [schema_id]: https://docs.databricks.com/api/workspace/schemas/get#schema_id
          [table_id]: https://docs.databricks.com/api/workspace/tables/get#table_id


        

    .. py:method:: delete_refresh(object_type: str, object_id: str, refresh_id: int)

        (Unimplemented) Delete a refresh

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. It is `schema_id` for `schema`, and `table_id` for `table`.

          Find the `schema_id` from either: 1. The [schema_id] of the `Schemas` resource. 2. In [Catalog
          Explorer] > select the `schema` > go to the `Details` tab > the `Schema ID` field.

          Find the `table_id` from either: 1. The [table_id] of the `Tables` resource. 2. In [Catalog
          Explorer] > select the `table` > go to the `Details` tab > the `Table ID` field.

          [Catalog Explorer]: https://docs.databricks.com/aws/en/catalog-explorer/
          [schema_id]: https://docs.databricks.com/api/workspace/schemas/get#schema_id
          [table_id]: https://docs.databricks.com/api/workspace/tables/get#table_id
        :param refresh_id: int
          Unique id of the refresh operation.


        

    .. py:method:: get_monitor(object_type: str, object_id: str) -> Monitor

        Read a data quality monitor on a Unity Catalog object.

        For the `table` `object_type`, the caller must have either of the following sets of permissions: 1.
        **MANAGE** and **USE_CATALOG** on the table's parent catalog. 2. **USE_CATALOG** on the table's parent
        catalog, and **MANAGE** and **USE_SCHEMA** on the table's parent schema. 3. **USE_CATALOG** on the
        table's parent catalog, **USE_SCHEMA** on the table's parent schema, and **SELECT** on the table.

        For the `schema` `object_type`, the caller must have either of the following sets of permissions: 1.
        **MANAGE** and **USE_CATALOG** on the schema's parent catalog. 2. **USE_CATALOG** on the schema's
        parent catalog, and **USE_SCHEMA** on the schema.

        The returned information includes configuration values on the entity and parent entity as well as
        information on assets created by the monitor. Some information (e.g. dashboard) may be filtered out if
        the caller is in a different workspace than where the monitor was created.

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. It is `schema_id` for `schema`, and `table_id` for `table`.

          Find the `schema_id` from either: 1. The [schema_id] of the `Schemas` resource. 2. In [Catalog
          Explorer] > select the `schema` > go to the `Details` tab > the `Schema ID` field.

          Find the `table_id` from either: 1. The [table_id] of the `Tables` resource. 2. In [Catalog
          Explorer] > select the `table` > go to the `Details` tab > the `Table ID` field.

          [Catalog Explorer]: https://docs.databricks.com/aws/en/catalog-explorer/
          [schema_id]: https://docs.databricks.com/api/workspace/schemas/get#schema_id
          [table_id]: https://docs.databricks.com/api/workspace/tables/get#table_id

        :returns: :class:`Monitor`
        

    .. py:method:: get_refresh(object_type: str, object_id: str, refresh_id: int) -> Refresh

        Get data quality monitor refresh. The call must be made in the same workspace as where the monitor was
        created.

        For the `table` `object_type`, the caller must have either of the following sets of permissions: 1.
        **MANAGE** and **USE_CATALOG** on the table's parent catalog. 2. **USE_CATALOG** on the table's parent
        catalog, and **MANAGE** and **USE_SCHEMA** on the table's parent schema. 3. **USE_CATALOG** on the
        table's parent catalog, **USE_SCHEMA** on the table's parent schema, and **SELECT** on the table.

        For the `schema` `object_type`, the caller must have either of the following sets of permissions: 1.
        **MANAGE** and **USE_CATALOG** on the schema's parent catalog. 2. **USE_CATALOG** on the schema's
        parent catalog, and **USE_SCHEMA** on the schema.

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. It is `schema_id` for `schema`, and `table_id` for `table`.

          Find the `schema_id` from either: 1. The [schema_id] of the `Schemas` resource. 2. In [Catalog
          Explorer] > select the `schema` > go to the `Details` tab > the `Schema ID` field.

          Find the `table_id` from either: 1. The [table_id] of the `Tables` resource. 2. In [Catalog
          Explorer] > select the `table` > go to the `Details` tab > the `Table ID` field.

          [Catalog Explorer]: https://docs.databricks.com/aws/en/catalog-explorer/
          [schema_id]: https://docs.databricks.com/api/workspace/schemas/get#schema_id
          [table_id]: https://docs.databricks.com/api/workspace/tables/get#table_id
        :param refresh_id: int
          Unique id of the refresh operation.

        :returns: :class:`Refresh`
        

    .. py:method:: list_monitor( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Monitor]

        (Unimplemented) List data quality monitors.

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Monitor`
        

    .. py:method:: list_refresh(object_type: str, object_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Refresh]

        List data quality monitor refreshes. The call must be made in the same workspace as where the monitor
        was created.

        For the `table` `object_type`, the caller must have either of the following sets of permissions: 1.
        **MANAGE** and **USE_CATALOG** on the table's parent catalog. 2. **USE_CATALOG** on the table's parent
        catalog, and **MANAGE** and **USE_SCHEMA** on the table's parent schema. 3. **USE_CATALOG** on the
        table's parent catalog, **USE_SCHEMA** on the table's parent schema, and **SELECT** on the table.

        For the `schema` `object_type`, the caller must have either of the following sets of permissions: 1.
        **MANAGE** and **USE_CATALOG** on the schema's parent catalog. 2. **USE_CATALOG** on the schema's
        parent catalog, and **USE_SCHEMA** on the schema.

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. It is `schema_id` for `schema`, and `table_id` for `table`.

          Find the `schema_id` from either: 1. The [schema_id] of the `Schemas` resource. 2. In [Catalog
          Explorer] > select the `schema` > go to the `Details` tab > the `Schema ID` field.

          Find the `table_id` from either: 1. The [table_id] of the `Tables` resource. 2. In [Catalog
          Explorer] > select the `table` > go to the `Details` tab > the `Table ID` field.

          [Catalog Explorer]: https://docs.databricks.com/aws/en/catalog-explorer/
          [schema_id]: https://docs.databricks.com/api/workspace/schemas/get#schema_id
          [table_id]: https://docs.databricks.com/api/workspace/tables/get#table_id
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Refresh`
        

    .. py:method:: update_monitor(object_type: str, object_id: str, monitor: Monitor, update_mask: str) -> Monitor

        Update a data quality monitor on Unity Catalog object.

        For the `table` `object_type`, the caller must have either of the following sets of permissions: 1.
        **MANAGE** and **USE_CATALOG** on the table's parent catalog. 2. **USE_CATALOG** on the table's parent
        catalog, and **MANAGE** and **USE_SCHEMA** on the table's parent schema. 3. **USE_CATALOG** on the
        table's parent catalog, **USE_SCHEMA** on the table's parent schema, and **MANAGE** on the table.

        For the `schema` `object_type`, the caller must have either of the following sets of permissions: 1.
        **MANAGE** and **USE_CATALOG** on the schema's parent catalog. 2. **USE_CATALOG** on the schema's
        parent catalog, and **MANAGE** and **USE_SCHEMA** on the schema.

        :param object_type: str
          The type of the monitored object. Can be one of the following: `schema` or `table`.
        :param object_id: str
          The UUID of the request object. It is `schema_id` for `schema`, and `table_id` for `table`.

          Find the `schema_id` from either: 1. The [schema_id] of the `Schemas` resource. 2. In [Catalog
          Explorer] > select the `schema` > go to the `Details` tab > the `Schema ID` field.

          Find the `table_id` from either: 1. The [table_id] of the `Tables` resource. 2. In [Catalog
          Explorer] > select the `table` > go to the `Details` tab > the `Table ID` field.

          [Catalog Explorer]: https://docs.databricks.com/aws/en/catalog-explorer/
          [schema_id]: https://docs.databricks.com/api/workspace/schemas/get#schema_id
          [table_id]: https://docs.databricks.com/api/workspace/tables/get#table_id
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
          The UUID of the request object. It is `schema_id` for `schema`, and `table_id` for `table`.

          Find the `schema_id` from either: 1. The [schema_id] of the `Schemas` resource. 2. In [Catalog
          Explorer] > select the `schema` > go to the `Details` tab > the `Schema ID` field.

          Find the `table_id` from either: 1. The [table_id] of the `Tables` resource. 2. In [Catalog
          Explorer] > select the `table` > go to the `Details` tab > the `Table ID` field.

          [Catalog Explorer]: https://docs.databricks.com/aws/en/catalog-explorer/
          [schema_id]: https://docs.databricks.com/api/workspace/schemas/get#schema_id
          [table_id]: https://docs.databricks.com/api/workspace/tables/get#table_id
        :param refresh_id: int
          Unique id of the refresh operation.
        :param refresh: :class:`Refresh`
          The refresh to update.
        :param update_mask: str
          The field mask to specify which fields to update.

        :returns: :class:`Refresh`
        
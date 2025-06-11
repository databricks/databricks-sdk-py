``w.quality_monitor_v2``: QualityMonitor.v2
===========================================
.. currentmodule:: databricks.sdk.service.qualitymonitorv2

.. py:class:: QualityMonitorV2API

    Manage data quality of UC objects (currently support `schema`)

    .. py:method:: create_quality_monitor(quality_monitor: QualityMonitor) -> QualityMonitor

        Create a quality monitor.

        Create a quality monitor on UC object

        :param quality_monitor: :class:`QualityMonitor`

        :returns: :class:`QualityMonitor`
        

    .. py:method:: delete_quality_monitor(object_type: str, object_id: str)

        Delete a quality monitor.

        Delete a quality monitor on UC object

        :param object_type: str
          The type of the monitored object. Can be one of the following: schema.
        :param object_id: str
          The uuid of the request object. For example, schema id.


        

    .. py:method:: get_quality_monitor(object_type: str, object_id: str) -> QualityMonitor

        Read a quality monitor.

        Read a quality monitor on UC object

        :param object_type: str
          The type of the monitored object. Can be one of the following: schema.
        :param object_id: str
          The uuid of the request object. For example, schema id.

        :returns: :class:`QualityMonitor`
        

    .. py:method:: list_quality_monitor( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[QualityMonitor]

        List quality monitors.

        (Unimplemented) List quality monitors

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`QualityMonitor`
        

    .. py:method:: update_quality_monitor(object_type: str, object_id: str, quality_monitor: QualityMonitor) -> QualityMonitor

        Update a quality monitor.

        (Unimplemented) Update a quality monitor on UC object

        :param object_type: str
          The type of the monitored object. Can be one of the following: schema.
        :param object_id: str
          The uuid of the request object. For example, schema id.
        :param quality_monitor: :class:`QualityMonitor`

        :returns: :class:`QualityMonitor`
        
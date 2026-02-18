``w.quality_monitor_v2``: QualityMonitor.v2
===========================================
.. currentmodule:: databricks.sdk.service.qualitymonitorv2

.. py:class:: QualityMonitorV2API

    Deprecated: Please use the Data Quality Monitoring API instead (REST: /api/data-quality/v1/monitors).
    Manage data quality of UC objects (currently support `schema`).

    .. py:method:: create_quality_monitor(quality_monitor: QualityMonitor) -> QualityMonitor

        Deprecated: Use Data Quality Monitoring API instead (/api/data-quality/v1/monitors). Create a quality
        monitor on UC object.

        :param quality_monitor: :class:`QualityMonitor`

        :returns: :class:`QualityMonitor`
        

    .. py:method:: delete_quality_monitor(object_type: str, object_id: str)

        Deprecated: Use Data Quality Monitoring API instead (/api/data-quality/v1/monitors). Delete a quality
        monitor on UC object.

        :param object_type: str
          The type of the monitored object. Can be one of the following: schema.
        :param object_id: str
          The uuid of the request object. For example, schema id.


        

    .. py:method:: get_quality_monitor(object_type: str, object_id: str) -> QualityMonitor

        Deprecated: Use Data Quality Monitoring API instead (/api/data-quality/v1/monitors). Read a quality
        monitor on UC object.

        :param object_type: str
          The type of the monitored object. Can be one of the following: schema.
        :param object_id: str
          The uuid of the request object. For example, schema id.

        :returns: :class:`QualityMonitor`
        

    .. py:method:: list_quality_monitor( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[QualityMonitor]

        Deprecated: Use Data Quality Monitoring API instead (/api/data-quality/v1/monitors). (Unimplemented)
        List quality monitors.

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`QualityMonitor`
        

    .. py:method:: update_quality_monitor(object_type: str, object_id: str, quality_monitor: QualityMonitor) -> QualityMonitor

        Deprecated: Use Data Quality Monitoring API instead (/api/data-quality/v1/monitors). (Unimplemented)
        Update a quality monitor on UC object.

        :param object_type: str
          The type of the monitored object. Can be one of the following: schema.
        :param object_id: str
          The uuid of the request object. For example, schema id.
        :param quality_monitor: :class:`QualityMonitor`

        :returns: :class:`QualityMonitor`
        
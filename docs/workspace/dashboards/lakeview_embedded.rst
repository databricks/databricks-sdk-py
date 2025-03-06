``w.lakeview_embedded``: Lakeview Embedded
==========================================
.. currentmodule:: databricks.sdk.service.dashboards

.. py:class:: LakeviewEmbeddedAPI

    Token-based Lakeview APIs for embedding dashboards in external applications.

    .. py:method:: get_published_dashboard_embedded(dashboard_id: str)

        Read a published dashboard in an embedded ui.

        Get the current published dashboard within an embedded context.

        :param dashboard_id: str
          UUID identifying the published dashboard.


        
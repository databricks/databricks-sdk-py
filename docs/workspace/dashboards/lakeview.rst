``w.lakeview``: Lakeview
========================
.. currentmodule:: databricks.sdk.service.dashboards

.. py:class:: LakeviewAPI

    These APIs provide specific management operations for Lakeview dashboards. Generic resource management can
    be done with Workspace API (import, export, get-status, list, delete).

    .. py:method:: publish(dashboard_id: str [, embed_credentials: Optional[bool], warehouse_id: Optional[str]])

        Publish dashboard.
        
        Publish the current draft dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard to be published.
        :param embed_credentials: bool (optional)
          Flag to indicate if the publisher's credentials should be embedded in the published dashboard. These
          embedded credentials will be used to execute the published dashboard's queries.
        :param warehouse_id: str (optional)
          The ID of the warehouse that can be used to override the warehouse which was set in the draft.
        
        
        
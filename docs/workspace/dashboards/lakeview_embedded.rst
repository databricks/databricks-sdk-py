``w.lakeview_embedded``: Lakeview Embedded
==========================================
.. currentmodule:: databricks.sdk.service.dashboards

.. py:class:: LakeviewEmbeddedAPI

    Token-based Lakeview APIs for embedding dashboards in external applications.

    .. py:method:: get_published_dashboard_token_info(dashboard_id: str [, external_value: Optional[str], external_viewer_id: Optional[str]]) -> GetPublishedDashboardTokenInfoResponse

        Get a required authorization details and scopes of a published dashboard to mint an OAuth token. The
        `authorization_details` can be enriched to apply additional restriction.

        Example: Adding the following `authorization_details` object to downscope the viewer permission to
        specific table ``` { type: "unity_catalog_privileges", privileges: ["SELECT"], object_type: "TABLE",
        object_full_path: "main.default.testdata" } ```

        :param dashboard_id: str
          UUID identifying the published dashboard.
        :param external_value: str (optional)
          Provided external value to be included in the custom claim.
        :param external_viewer_id: str (optional)
          Provided external viewer id to be included in the custom claim.

        :returns: :class:`GetPublishedDashboardTokenInfoResponse`
        
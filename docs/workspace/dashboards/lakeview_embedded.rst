``w.lakeview_embedded``: Lakeview Embedded
==========================================
.. currentmodule:: databricks.sdk.service.dashboards

.. py:class:: LakeviewEmbeddedAPI

    Token-based Lakeview APIs for embedding dashboards in external applications.

    .. py:method:: get_published_dashboard_token_info(dashboard_id: str [, external_value: Optional[str], external_viewer_id: Optional[str]]) -> GetPublishedDashboardTokenInfoResponse

        Get the OAuth scope and authorization details needed to mint a token that is scoped to viewing the
        published dashboard, for example to embed it in an external application. Pass the response fields,
        with ``authorization_details`` serialized as a JSON string, to the workspace OAuth token endpoint with
        the ``client_credentials`` grant to mint the token. See `Embedding for external users
        <https://docs.databricks.com/dashboards/share/embedding/external-embed>`__.

        The caller must be a workspace user with one of the following entitlements: Workspace access,
        Databricks SQL access, or Consumer access.

        Account-level users who are not members of the workspace cannot call this endpoint, even if the
        dashboard has been shared with them.

        :param dashboard_id: str
          UUID identifying the published dashboard.
        :param external_value: str (optional)
          Value to carry in the token for this viewer, such as a tenant or region key. Dashboard dataset
          queries can reference it as ``__aibi_external_value`` to filter data per viewer. The combined size
          of ``external_value`` and ``external_viewer_id`` must be less than 1 KB.
        :param external_viewer_id: str (optional)
          Identifier of the viewer in the external application. It is recorded in dashboard audit logs, so it
          should be unique per viewer and must not contain personally identifiable information.

        :returns: :class:`GetPublishedDashboardTokenInfoResponse`
        
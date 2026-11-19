``w.provider_provider_analytics_dashboards``: Provider Providers Analytics Dashboards
=====================================================================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ProviderProviderAnalyticsDashboardsAPI

    Manage templated analytics solution for providers.

    .. py:method:: create() -> ProviderAnalyticsDashboard

        Creates the Provider Analytics Dashboard in the caller's workspace from the latest template. Fails if
        the dashboard already exists. Returns the Marketplace-specific ``id`` of the dashboard record, which
        is distinct from the AI/BI dashboard ID.


        :returns: :class:`ProviderAnalyticsDashboard`
        

    .. py:method:: get() -> ListProviderAnalyticsDashboardResponse

        Gets the Provider Analytics Dashboard that was created for the caller's account. Returns an empty
        response if the dashboard has not been created yet.


        :returns: :class:`ListProviderAnalyticsDashboardResponse`
        

    .. py:method:: get_latest_version() -> GetLatestVersionProviderAnalyticsDashboardResponse

        Gets the latest available version of the Provider Analytics Dashboard template.


        :returns: :class:`GetLatestVersionProviderAnalyticsDashboardResponse`
        

    .. py:method:: update(id: str [, version: Optional[int]]) -> UpdateProviderAnalyticsDashboardResponse

        Updates the Provider Analytics Dashboard to a newer version of the template. The requested version
        must be newer than the version that the dashboard currently uses.

        :param id: str
          Marketplace-specific ID of the dashboard record, as returned when the dashboard was created or
          retrieved.
        :param version: int (optional)
          Version of the dashboard template to update to. Must be newer than the version that the dashboard
          currently uses; use the version returned by getLatestVersionProviderAnalyticsDashboard.

        :returns: :class:`UpdateProviderAnalyticsDashboardResponse`
        
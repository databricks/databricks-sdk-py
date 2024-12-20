``w.provider_provider_analytics_dashboards``: Provider Providers Analytics Dashboards
=====================================================================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ProviderProviderAnalyticsDashboardsAPI

    Manage templated analytics solution for providers.

    .. py:method:: create() -> ProviderAnalyticsDashboard

        Create provider analytics dashboard.
        
        Create provider analytics dashboard. Returns Marketplace specific `id`. Not to be confused with the
        Lakeview dashboard id.
        
        :returns: :class:`ProviderAnalyticsDashboard`


    .. py:method:: get() -> ListProviderAnalyticsDashboardResponse

        Get provider analytics dashboard.
        
        Get provider analytics dashboard.
        
        :returns: :class:`ListProviderAnalyticsDashboardResponse`


    .. py:method:: get_latest_version() -> GetLatestVersionProviderAnalyticsDashboardResponse

        Get latest version of provider analytics dashboard.
        
        Get latest version of provider analytics dashboard.
        
        :returns: :class:`GetLatestVersionProviderAnalyticsDashboardResponse`


    .. py:method:: update(id: str [, version: Optional[int]]) -> UpdateProviderAnalyticsDashboardResponse

        Update provider analytics dashboard.
        
        Update provider analytics dashboard.
        
        :param id: str
          id is immutable property and can't be updated.
        :param version: int (optional)
          this is the version of the dashboard template we want to update our user to current expectation is
          that it should be equal to latest version of the dashboard template
        
        :returns: :class:`UpdateProviderAnalyticsDashboardResponse`

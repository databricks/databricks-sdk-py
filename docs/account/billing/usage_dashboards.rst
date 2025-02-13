``a.usage_dashboards``: Usage Dashboards
========================================
.. currentmodule:: databricks.sdk.service.billing

.. py:class:: UsageDashboardsAPI

    These APIs manage usage dashboards for this account. Usage dashboards enable you to gain insights into
    your usage with pre-built dashboards: visualize breakdowns, analyze tag attributions, and identify cost
    drivers.

    .. py:method:: create( [, dashboard_type: Optional[UsageDashboardType], workspace_id: Optional[int]]) -> CreateBillingUsageDashboardResponse

        Create new usage dashboard.
        
        Create a usage dashboard specified by workspaceId, accountId, and dashboard type.
        
        :param dashboard_type: :class:`UsageDashboardType` (optional)
          Workspace level usage dashboard shows usage data for the specified workspace ID. Global level usage
          dashboard shows usage data for all workspaces in the account.
        :param workspace_id: int (optional)
          The workspace ID of the workspace in which the usage dashboard is created.
        
        :returns: :class:`CreateBillingUsageDashboardResponse`
        

    .. py:method:: get( [, dashboard_type: Optional[UsageDashboardType], workspace_id: Optional[int]]) -> GetBillingUsageDashboardResponse

        Get usage dashboard.
        
        Get a usage dashboard specified by workspaceId, accountId, and dashboard type.
        
        :param dashboard_type: :class:`UsageDashboardType` (optional)
          Workspace level usage dashboard shows usage data for the specified workspace ID. Global level usage
          dashboard shows usage data for all workspaces in the account.
        :param workspace_id: int (optional)
          The workspace ID of the workspace in which the usage dashboard is created.
        
        :returns: :class:`GetBillingUsageDashboardResponse`
        
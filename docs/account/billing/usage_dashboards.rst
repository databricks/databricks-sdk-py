``a.usage_dashboards``: Usage Dashboards
========================================
.. currentmodule:: databricks.sdk.service.billing

.. py:class:: UsageDashboardsAPI

    These APIs manage usage dashboards for this account. Usage dashboards enable you to gain insights into
    your usage with pre-built dashboards: visualize breakdowns, analyze tag attributions, and identify cost
    drivers.

    .. py:method:: create( [, dashboard_type: Optional[UsageDashboardType], major_version: Optional[UsageDashboardMajorVersion], workspace_id: Optional[int]]) -> CreateBillingUsageDashboardResponse

        Imports a pre-built usage dashboard of the given type into a workspace. Each call imports a new
        dashboard, even if the caller already created one of the same type in that workspace. The caller must
        be an account admin and a user of the target workspace. See
        https://docs.databricks.com/admin/account-settings/usage.html.

        :param dashboard_type: :class:`UsageDashboardType` (optional)
          Workspace level usage dashboard shows usage data for the specified workspace ID. Global level usage
          dashboard shows usage data for all workspaces in the account. The request fails if the type is not
          set.
        :param major_version: :class:`UsageDashboardMajorVersion` (optional)
          The major version of the usage dashboard template to import. Version 2 adds cost forecasting and
          object-level cost drill-down.
        :param workspace_id: int (optional)
          The ID of the workspace to import the usage dashboard into. The workspace must be running, belong to
          the account, and not be a disaster recovery secondary.

        :returns: :class:`CreateBillingUsageDashboardResponse`
        

    .. py:method:: get( [, dashboard_type: Optional[UsageDashboardType], workspace_id: Optional[int]]) -> GetBillingUsageDashboardResponse

        Gets the most recent usage dashboard of the given type that the caller created. The response is empty
        if no such dashboard exists, if it has been deleted, or if the caller can no longer access its
        workspace.

        :param dashboard_type: :class:`UsageDashboardType` (optional)
          Workspace level usage dashboard shows usage data for the specified workspace ID. Global level usage
          dashboard shows usage data for all workspaces in the account. The request fails if the type is not
          set.
        :param workspace_id: int (optional)
          The ID of the workspace that contains the usage dashboard. If omitted, the most recently created
          dashboard of the given type across all workspaces in the account is returned.

        :returns: :class:`GetBillingUsageDashboardResponse`
        
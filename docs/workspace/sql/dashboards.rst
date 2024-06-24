``w.dashboards``: Dashboards
============================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: DashboardsAPI

    In general, there is little need to modify dashboards using the API. However, it can be useful to use
    dashboard objects to look-up a collection of related query IDs. The API can also be used to duplicate
    multiple dashboards at once since you can get a dashboard definition with a GET request and then POST it
    to create a new one. Dashboards can be scheduled using the `sql_task` type of the Jobs API, e.g.
    :method:jobs/create.

    .. py:method:: create(name: str [, dashboard_filters_enabled: Optional[bool], is_favorite: Optional[bool], parent: Optional[str], run_as_role: Optional[RunAsRole], tags: Optional[List[str]]]) -> Dashboard


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.dashboards.create(name=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.dashboards.delete(dashboard_id=created.id)

        Create a dashboard object.
        
        :param name: str
          The title of this dashboard that appears in list views and at the top of the dashboard page.
        :param dashboard_filters_enabled: bool (optional)
          Indicates whether the dashboard filters are enabled
        :param is_favorite: bool (optional)
          Indicates whether this dashboard object should appear in the current user's favorites list.
        :param parent: str (optional)
          The identifier of the workspace folder containing the object.
        :param run_as_role: :class:`RunAsRole` (optional)
          Sets the **Run as** role for the object. Must be set to one of `"viewer"` (signifying "run as
          viewer" behavior) or `"owner"` (signifying "run as owner" behavior)
        :param tags: List[str] (optional)
        
        :returns: :class:`Dashboard`
        

    .. py:method:: delete(dashboard_id: str)


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.dashboards.create(name=f'sdk-{time.time_ns()}')
            
            w.dashboards.delete(dashboard_id=created.id)
            
            # cleanup
            w.dashboards.delete(dashboard_id=created.id)

        Remove a dashboard.
        
        Moves a dashboard to the trash. Trashed dashboards do not appear in list views or searches, and cannot
        be shared.
        
        :param dashboard_id: str
        
        
        

    .. py:method:: get(dashboard_id: str) -> Dashboard


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.dashboards.create(name=f'sdk-{time.time_ns()}')
            
            by_id = w.dashboards.get(dashboard_id=created.id)
            
            # cleanup
            w.dashboards.delete(dashboard_id=created.id)

        Retrieve a definition.
        
        Returns a JSON representation of a dashboard object, including its visualization and query objects.
        
        :param dashboard_id: str
        
        :returns: :class:`Dashboard`
        

    .. py:method:: list( [, order: Optional[ListOrder], page: Optional[int], page_size: Optional[int], q: Optional[str]]) -> Iterator[Dashboard]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            all = w.dashboards.list(sql.ListDashboardsRequest())

        Get dashboard objects.
        
        Fetch a paginated list of dashboard objects.
        
        **Warning**: Calling this API concurrently 10 or more times could result in throttling, service
        degradation, or a temporary ban.
        
        :param order: :class:`ListOrder` (optional)
          Name of dashboard attribute to order by.
        :param page: int (optional)
          Page number to retrieve.
        :param page_size: int (optional)
          Number of dashboards to return per page.
        :param q: str (optional)
          Full text search term.
        
        :returns: Iterator over :class:`Dashboard`
        

    .. py:method:: restore(dashboard_id: str)


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.dashboards.create(name=f'sdk-{time.time_ns()}')
            
            w.dashboards.restore(dashboard_id=created.id)
            
            # cleanup
            w.dashboards.delete(dashboard_id=created.id)

        Restore a dashboard.
        
        A restored dashboard appears in list views and searches and can be shared.
        
        :param dashboard_id: str
        
        
        

    .. py:method:: update(dashboard_id: str [, name: Optional[str], run_as_role: Optional[RunAsRole], tags: Optional[List[str]]]) -> Dashboard

        Change a dashboard definition.
        
        Modify this dashboard definition. This operation only affects attributes of the dashboard object. It
        does not add, modify, or remove widgets.
        
        **Note**: You cannot undo this operation.
        
        :param dashboard_id: str
        :param name: str (optional)
          The title of this dashboard that appears in list views and at the top of the dashboard page.
        :param run_as_role: :class:`RunAsRole` (optional)
          Sets the **Run as** role for the object. Must be set to one of `"viewer"` (signifying "run as
          viewer" behavior) or `"owner"` (signifying "run as owner" behavior)
        :param tags: List[str] (optional)
        
        :returns: :class:`Dashboard`
        
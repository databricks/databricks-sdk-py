Dashboards
==========
.. py:class:: DashboardsAPI

    In general, there is little need to modify dashboards using the API. However, it can be useful to use
    dashboard objects to look-up a collection of related query IDs. The API can also be used to duplicate
    multiple dashboards at once since you can get a dashboard definition with a GET request and then POST it
    to create a new one. Dashboards can be scheduled using the `sql_task` type of the Jobs API, e.g.
    :method:jobs/create.

    .. py:method:: create( [, is_favorite, name, parent, tags])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.dashboards.create(name=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.dashboards.delete(delete=created.id)

        Create a dashboard object.
        
        :param is_favorite: bool (optional)
          Indicates whether this query object should appear in the current user's favorites list. The
          application uses this flag to determine whether or not the "favorite star " should selected.
        :param name: str (optional)
          The title of this dashboard that appears in list views and at the top of the dashboard page.
        :param parent: str (optional)
          The identifier of the workspace folder containing the dashboard. The default is the user's home
          folder.
        :param tags: List[str] (optional)
        
        :returns: :class:`Dashboard`
        

    .. py:method:: delete(dashboard_id)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.dashboards.create(name=f'sdk-{time.time_ns()}')
            
            w.dashboards.delete(delete=created.id)
            
            # cleanup
            w.dashboards.delete(delete=created.id)

        Remove a dashboard.
        
        Moves a dashboard to the trash. Trashed dashboards do not appear in list views or searches, and cannot
        be shared.
        
        :param dashboard_id: str
        
        
        

    .. py:method:: get(dashboard_id)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.dashboards.create(name=f'sdk-{time.time_ns()}')
            
            by_id = w.dashboards.get(get=created.id)
            
            # cleanup
            w.dashboards.delete(delete=created.id)

        Retrieve a definition.
        
        Returns a JSON representation of a dashboard object, including its visualization and query objects.
        
        :param dashboard_id: str
        
        :returns: :class:`Dashboard`
        

    .. py:method:: list( [, order, page, page_size, q])

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            all = w.dashboards.list(sql.ListDashboardsRequest())

        Get dashboard objects.
        
        Fetch a paginated list of dashboard objects.
        
        :param order: :class:`ListOrder` (optional)
          Name of dashboard attribute to order by.
        :param page: int (optional)
          Page number to retrieve.
        :param page_size: int (optional)
          Number of dashboards to return per page.
        :param q: str (optional)
          Full text search term.
        
        :returns: Iterator over :class:`Dashboard`
        

    .. py:method:: restore(dashboard_id)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.dashboards.create(name=f'sdk-{time.time_ns()}')
            
            w.dashboards.restore(dashboard_id=created.id)
            
            # cleanup
            w.dashboards.delete(delete=created.id)

        Restore a dashboard.
        
        A restored dashboard appears in list views and searches and can be shared.
        
        :param dashboard_id: str
        
        
        
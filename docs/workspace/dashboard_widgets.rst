Dashboard Widgets
=================
.. py:class:: DashboardWidgetsAPI

    This is an evolving API that facilitates the addition and removal of widgets from existing dashboards
    within the Databricks Workspace. Data structures may change over time.

    .. py:method:: create(dashboard_id, options, width [, text, visualization_id])

        Add widget to a dashboard.
        
        :param dashboard_id: str
          Dashboard ID returned by :method:dashboards/create.
        :param options: :class:`WidgetOptions`
        :param width: int
          Width of a widget
        :param text: str (optional)
          If this is a textbox widget, the application displays this text. This field is ignored if the widget
          contains a visualization in the `visualization` field.
        :param visualization_id: str (optional)
          Query Vizualization ID returned by :method:queryvisualizations/create.
        
        :returns: :class:`Widget`
        

    .. py:method:: delete(id)

        Remove widget.
        
        :param id: str
        
        
        

    .. py:method:: update(id, dashboard_id, options, width [, text, visualization_id])

        Update existing widget.
        
        :param id: str
        :param dashboard_id: str
          Dashboard ID returned by :method:dashboards/create.
        :param options: :class:`WidgetOptions`
        :param width: int
          Width of a widget
        :param text: str (optional)
          If this is a textbox widget, the application displays this text. This field is ignored if the widget
          contains a visualization in the `visualization` field.
        :param visualization_id: str (optional)
          Query Vizualization ID returned by :method:queryvisualizations/create.
        
        :returns: :class:`Widget`
        
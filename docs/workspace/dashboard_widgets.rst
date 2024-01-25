Dashboard Widgets
=================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: DashboardWidgetsAPI

    This is an evolving API that facilitates the addition and removal of widgets from existing dashboards
    within the Databricks Workspace. Data structures may change over time.

    .. py:method:: create(dashboard_id: str, options: WidgetOptions, width: int [, text: Optional[str], visualization_id: Optional[str]]) -> Widget

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
        

    .. py:method:: delete(id: str)

        Remove widget.
        
        :param id: str
          Widget ID returned by :method:dashboardwidgets/create
        
        
        

    .. py:method:: update(id: str, dashboard_id: str, options: WidgetOptions, width: int [, text: Optional[str], visualization_id: Optional[str]]) -> Widget

        Update existing widget.
        
        :param id: str
          Widget ID returned by :method:dashboardwidgets/create
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
        
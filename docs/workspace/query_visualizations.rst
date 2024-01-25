Query Visualizations
====================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: QueryVisualizationsAPI

    This is an evolving API that facilitates the addition and removal of vizualisations from existing queries
    within the Databricks Workspace. Data structures may change over time.

    .. py:method:: create(query_id: str, type: str, options: Any [, description: Optional[str], name: Optional[str]]) -> Visualization

        Add visualization to a query.
        
        :param query_id: str
          The identifier returned by :method:queries/create
        :param type: str
          The type of visualization: chart, table, pivot table, and so on.
        :param options: Any
          The options object varies widely from one visualization type to the next and is unsupported.
          Databricks does not recommend modifying visualization settings in JSON.
        :param description: str (optional)
          A short description of this visualization. This is not displayed in the UI.
        :param name: str (optional)
          The name of the visualization that appears on dashboards and the query screen.
        
        :returns: :class:`Visualization`
        

    .. py:method:: delete(id: str)

        Remove visualization.
        
        :param id: str
          Widget ID returned by :method:queryvizualisations/create
        
        
        

    .. py:method:: update(id: str [, created_at: Optional[str], description: Optional[str], name: Optional[str], options: Optional[Any], type: Optional[str], updated_at: Optional[str]]) -> Visualization

        Edit existing visualization.
        
        :param id: str
          The UUID for this visualization.
        :param created_at: str (optional)
        :param description: str (optional)
          A short description of this visualization. This is not displayed in the UI.
        :param name: str (optional)
          The name of the visualization that appears on dashboards and the query screen.
        :param options: Any (optional)
          The options object varies widely from one visualization type to the next and is unsupported.
          Databricks does not recommend modifying visualization settings in JSON.
        :param type: str (optional)
          The type of visualization: chart, table, pivot table, and so on.
        :param updated_at: str (optional)
        
        :returns: :class:`Visualization`
        
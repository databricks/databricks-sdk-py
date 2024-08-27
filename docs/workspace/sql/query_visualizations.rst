``w.query_visualizations``: Query Visualizations
================================================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: QueryVisualizationsAPI

    This is an evolving API that facilitates the addition and removal of visualizations from existing queries
    in the Databricks Workspace. Data structures can change over time.

    .. py:method:: create( [, visualization: Optional[CreateVisualizationRequestVisualization]]) -> Visualization

        Add a visualization to a query.
        
        Adds a visualization to a query.
        
        :param visualization: :class:`CreateVisualizationRequestVisualization` (optional)
        
        :returns: :class:`Visualization`
        

    .. py:method:: delete(id: str)

        Remove a visualization.
        
        Removes a visualization.
        
        :param id: str
        
        
        

    .. py:method:: update(id: str, update_mask: str [, visualization: Optional[UpdateVisualizationRequestVisualization]]) -> Visualization

        Update a visualization.
        
        Updates a visualization.
        
        :param id: str
        :param update_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        :param visualization: :class:`UpdateVisualizationRequestVisualization` (optional)
        
        :returns: :class:`Visualization`
        
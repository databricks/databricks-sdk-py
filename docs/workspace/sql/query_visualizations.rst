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
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.
          
          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.
        :param visualization: :class:`UpdateVisualizationRequestVisualization` (optional)
        
        :returns: :class:`Visualization`
        
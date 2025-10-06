``w.feature_engineering``: Feature Engineering
==============================================
.. currentmodule:: databricks.sdk.service.ml

.. py:class:: FeatureEngineeringAPI

    [description]

    .. py:method:: create_feature(feature: Feature) -> Feature

        Create a Feature.

        :param feature: :class:`Feature`
          Feature to create.

        :returns: :class:`Feature`
        

    .. py:method:: delete_feature(full_name: str)

        Delete a Feature.

        :param full_name: str
          Name of the feature to delete.


        

    .. py:method:: get_feature(full_name: str) -> Feature

        Get a Feature.

        :param full_name: str
          Name of the feature to get.

        :returns: :class:`Feature`
        

    .. py:method:: list_features( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Feature]

        List Features.

        :param page_size: int (optional)
          The maximum number of results to return.
        :param page_token: str (optional)
          Pagination token to go to the next page based on a previous query.

        :returns: Iterator over :class:`Feature`
        

    .. py:method:: update_feature(full_name: str, feature: Feature, update_mask: str) -> Feature

        Update a Feature.

        :param full_name: str
          The full three-part name (catalog, schema, name) of the feature.
        :param feature: :class:`Feature`
          Feature to update.
        :param update_mask: str
          The list of fields to update.

        :returns: :class:`Feature`
        
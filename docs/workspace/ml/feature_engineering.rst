``w.feature_engineering``: Feature Engineering
==============================================
.. currentmodule:: databricks.sdk.service.ml

.. py:class:: FeatureEngineeringAPI

    [description]

    .. py:method:: batch_create_materialized_features(requests: List[CreateMaterializedFeatureRequest]) -> BatchCreateMaterializedFeaturesResponse

        Batch create materialized features.

        :param requests: List[:class:`CreateMaterializedFeatureRequest`]
          The requests to create materialized features.

        :returns: :class:`BatchCreateMaterializedFeaturesResponse`
        

    .. py:method:: create_feature(feature: Feature) -> Feature

        Create a Feature.

        :param feature: :class:`Feature`
          Feature to create.

        :returns: :class:`Feature`
        

    .. py:method:: create_materialized_feature(materialized_feature: MaterializedFeature) -> MaterializedFeature

        Create a materialized feature.

        :param materialized_feature: :class:`MaterializedFeature`
          The materialized feature to create.

        :returns: :class:`MaterializedFeature`
        

    .. py:method:: delete_feature(full_name: str)

        Delete a Feature.

        :param full_name: str
          Name of the feature to delete.


        

    .. py:method:: delete_materialized_feature(materialized_feature_id: str)

        Delete a materialized feature.

        :param materialized_feature_id: str
          The ID of the materialized feature to delete.


        

    .. py:method:: get_feature(full_name: str) -> Feature

        Get a Feature.

        :param full_name: str
          Name of the feature to get.

        :returns: :class:`Feature`
        

    .. py:method:: get_materialized_feature(materialized_feature_id: str) -> MaterializedFeature

        Get a materialized feature.

        :param materialized_feature_id: str
          The ID of the materialized feature.

        :returns: :class:`MaterializedFeature`
        

    .. py:method:: list_features( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Feature]

        List Features.

        :param page_size: int (optional)
          The maximum number of results to return.
        :param page_token: str (optional)
          Pagination token to go to the next page based on a previous query.

        :returns: Iterator over :class:`Feature`
        

    .. py:method:: list_materialized_features( [, feature_name: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[MaterializedFeature]

        List materialized features.

        :param feature_name: str (optional)
          Filter by feature name. If specified, only materialized features materialized from this feature will
          be returned.
        :param page_size: int (optional)
          The maximum number of results to return. Defaults to 100 if not specified. Cannot be greater than
          1000.
        :param page_token: str (optional)
          Pagination token to go to the next page based on a previous query.

        :returns: Iterator over :class:`MaterializedFeature`
        

    .. py:method:: update_feature(full_name: str, feature: Feature, update_mask: str) -> Feature

        Update a Feature.

        :param full_name: str
          The full three-part name (catalog, schema, name) of the feature.
        :param feature: :class:`Feature`
          Feature to update.
        :param update_mask: str
          The list of fields to update.

        :returns: :class:`Feature`
        

    .. py:method:: update_materialized_feature(materialized_feature_id: str, materialized_feature: MaterializedFeature, update_mask: str) -> MaterializedFeature

        Update a materialized feature (pause/resume).

        :param materialized_feature_id: str
          Unique identifier for the materialized feature.
        :param materialized_feature: :class:`MaterializedFeature`
          The materialized feature to update.
        :param update_mask: str
          Provide the materialization feature fields which should be updated. Currently, only the
          pipeline_state field can be updated.

        :returns: :class:`MaterializedFeature`
        
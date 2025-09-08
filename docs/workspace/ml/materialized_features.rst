``w.materialized_features``: Materialized Features
==================================================
.. currentmodule:: databricks.sdk.service.ml

.. py:class:: MaterializedFeaturesAPI

    Materialized Features are columns in tables and views that can be directly used as features to train and
    serve ML models.

    .. py:method:: create_feature_tag(table_name: str, feature_name: str, feature_tag: FeatureTag) -> FeatureTag

        Creates a FeatureTag.
        
        :param table_name: str
        :param feature_name: str
        :param feature_tag: :class:`FeatureTag`
        
        :returns: :class:`FeatureTag`
        

    .. py:method:: delete_feature_tag(table_name: str, feature_name: str, key: str)

        Deletes a FeatureTag.
        
        :param table_name: str
          The name of the feature table.
        :param feature_name: str
          The name of the feature within the feature table.
        :param key: str
          The key of the tag to delete.
        
        
        

    .. py:method:: get_feature_lineage(table_name: str, feature_name: str) -> FeatureLineage

        Get Feature Lineage.
        
        :param table_name: str
          The full name of the feature table in Unity Catalog.
        :param feature_name: str
          The name of the feature.
        
        :returns: :class:`FeatureLineage`
        

    .. py:method:: get_feature_tag(table_name: str, feature_name: str, key: str) -> FeatureTag

        Gets a FeatureTag.
        
        :param table_name: str
        :param feature_name: str
        :param key: str
        
        :returns: :class:`FeatureTag`
        

    .. py:method:: list_feature_tags(table_name: str, feature_name: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[FeatureTag]

        Lists FeatureTags.
        
        :param table_name: str
        :param feature_name: str
        :param page_size: int (optional)
          The maximum number of results to return.
        :param page_token: str (optional)
          Pagination token to go to the next page based on a previous query.
        
        :returns: Iterator over :class:`FeatureTag`
        

    .. py:method:: update_feature_tag(table_name: str, feature_name: str, key: str, feature_tag: FeatureTag [, update_mask: Optional[str]]) -> FeatureTag

        Updates a FeatureTag.
        
        :param table_name: str
        :param feature_name: str
        :param key: str
        :param feature_tag: :class:`FeatureTag`
        :param update_mask: str (optional)
          The list of fields to update.
        
        :returns: :class:`FeatureTag`
        
``w.feature_store``: Feature Store
==================================
.. currentmodule:: databricks.sdk.service.ml

.. py:class:: FeatureStoreAPI

    A feature store is a centralized repository that enables data scientists to find and share features. Using
    a feature store also ensures that the code used to compute feature values is the same during model
    training and when the model is used for inference.

    An online store is a low-latency database used for feature lookup during real-time model inference or
    serve feature for real-time applications.

    .. py:method:: create_online_store(online_store: OnlineStore) -> OnlineStore

        Create an Online Feature Store.

        Create an Online Feature Store.

        :param online_store: :class:`OnlineStore`
          An OnlineStore is a logical database instance that stores and serves features online.

        :returns: :class:`OnlineStore`
        

    .. py:method:: delete_online_store(name: str)

        Delete an Online Feature Store.

        Delete an Online Feature Store.

        :param name: str
          Name of the online store to delete.


        

    .. py:method:: get_online_store(name: str) -> OnlineStore

        Get an Online Feature Store.

        Get an Online Feature Store.

        :param name: str
          Name of the online store to get.

        :returns: :class:`OnlineStore`
        

    .. py:method:: list_online_stores( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[OnlineStore]

        List Online Feature Stores.

        List Online Feature Stores.

        :param page_size: int (optional)
          The maximum number of results to return. Defaults to 100 if not specified.
        :param page_token: str (optional)
          Pagination token to go to the next page based on a previous query.

        :returns: Iterator over :class:`OnlineStore`
        

    .. py:method:: publish_table(source_table_name: str, publish_spec: PublishSpec) -> PublishTableResponse

        Publish features.

        Publish features.

        :param source_table_name: str
          The full three-part (catalog, schema, table) name of the source table.
        :param publish_spec: :class:`PublishSpec`
          The specification for publishing the online table from the source table.

        :returns: :class:`PublishTableResponse`
        

    .. py:method:: update_online_store(name: str, online_store: OnlineStore, update_mask: str) -> OnlineStore

        Update an Online Feature Store.

        Update an Online Feature Store.

        :param name: str
          The name of the online store. This is the unique identifier for the online store.
        :param online_store: :class:`OnlineStore`
          An OnlineStore is a logical database instance that stores and serves features online.
        :param update_mask: str
          The list of fields to update.

        :returns: :class:`OnlineStore`
        
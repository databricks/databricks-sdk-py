``w.consumer_providers``: Consumer Providers
============================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ConsumerProvidersAPI

    Providers are the entities that publish listings to the Marketplace.

    .. py:method:: batch_get( [, ids: Optional[List[str]]]) -> BatchGetProvidersResponse

        Get one batch of providers. One may specify up to 50 IDs per request.
        
        Batch get a provider in the Databricks Marketplace with at least one visible listing.
        
        :param ids: List[str] (optional)
        
        :returns: :class:`BatchGetProvidersResponse`
        

    .. py:method:: get(id: str) -> GetProviderResponse

        Get a provider.
        
        Get a provider in the Databricks Marketplace with at least one visible listing.
        
        :param id: str
        
        :returns: :class:`GetProviderResponse`
        

    .. py:method:: list( [, is_featured: Optional[bool], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ProviderInfo]

        List providers.
        
        List all providers in the Databricks Marketplace with at least one visible listing.
        
        :param is_featured: bool (optional)
        :param page_size: int (optional)
        :param page_token: str (optional)
        
        :returns: Iterator over :class:`ProviderInfo`
        
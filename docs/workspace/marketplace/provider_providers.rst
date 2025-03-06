``w.provider_providers``: Provider Providers
============================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ProviderProvidersAPI

    Providers are entities that manage assets in Marketplace.

    .. py:method:: create(provider: ProviderInfo) -> CreateProviderResponse

        Create a provider.

        Create a provider

        :param provider: :class:`ProviderInfo`

        :returns: :class:`CreateProviderResponse`
        

    .. py:method:: delete(id: str)

        Delete provider.

        Delete provider

        :param id: str


        

    .. py:method:: get(id: str) -> GetProviderResponse

        Get provider.

        Get provider profile

        :param id: str

        :returns: :class:`GetProviderResponse`
        

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ProviderInfo]

        List providers.

        List provider profiles for account.

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`ProviderInfo`
        

    .. py:method:: update(id: str, provider: ProviderInfo) -> UpdateProviderResponse

        Update provider.

        Update provider profile

        :param id: str
        :param provider: :class:`ProviderInfo`

        :returns: :class:`UpdateProviderResponse`
        
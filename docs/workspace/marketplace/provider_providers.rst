``w.provider_providers``: Provider Providers
============================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ProviderProvidersAPI

    Providers are entities that manage assets in Marketplace.

    .. py:method:: create(provider: ProviderInfo) -> CreateProviderResponse

        Creates a provider profile in the caller's account. Returns the ID of the new profile.

        :param provider: :class:`ProviderInfo`
          Provider profile to create.

        :returns: :class:`CreateProviderResponse`
        

    .. py:method:: delete(id: str)

        Deletes a provider profile and all of the listings that it owns.

        :param id: str
          ID of the provider profile to delete.


        

    .. py:method:: get(id: str) -> GetProviderResponse

        Gets a provider profile by ID.

        :param id: str

        :returns: :class:`GetProviderResponse`
        

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ProviderInfo]

        Lists the provider profiles in the caller's account.

        :param page_size: int (optional)
          Maximum number of results to return per page.
        :param page_token: str (optional)
          Token from the next_page_token field of a previous response. Omit to get the first page.

        :returns: Iterator over :class:`ProviderInfo`
        

    .. py:method:: update(id: str, provider: ProviderInfo) -> UpdateProviderResponse

        Updates a provider profile. Send the full profile definition.

        :param id: str
          ID of the provider profile to update.
        :param provider: :class:`ProviderInfo`
          Full definition of the provider profile, including the fields that are not changing.

        :returns: :class:`UpdateProviderResponse`
        
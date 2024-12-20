``w.provider_exchange_filters``: Provider Exchange Filters
==========================================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ProviderExchangeFiltersAPI

    Marketplace exchanges filters curate which groups can access an exchange.

    .. py:method:: create(filter: ExchangeFilter) -> CreateExchangeFilterResponse

        Create a new exchange filter.
        
        Add an exchange filter.
        
        :param filter: :class:`ExchangeFilter`
        
        :returns: :class:`CreateExchangeFilterResponse`


    .. py:method:: delete(id: str)

        Delete an exchange filter.
        
        Delete an exchange filter
        
        :param id: str
        



    .. py:method:: list(exchange_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ExchangeFilter]

        List exchange filters.
        
        List exchange filter
        
        :param exchange_id: str
        :param page_size: int (optional)
        :param page_token: str (optional)
        
        :returns: Iterator over :class:`ExchangeFilter`


    .. py:method:: update(id: str, filter: ExchangeFilter) -> UpdateExchangeFilterResponse

        Update exchange filter.
        
        Update an exchange filter.
        
        :param id: str
        :param filter: :class:`ExchangeFilter`
        
        :returns: :class:`UpdateExchangeFilterResponse`

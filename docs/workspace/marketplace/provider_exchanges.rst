``w.provider_exchanges``: Provider Exchanges
============================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ProviderExchangesAPI

    Marketplace exchanges allow providers to share their listings with a curated set of customers.

    .. py:method:: add_listing_to_exchange(listing_id: str, exchange_id: str) -> AddExchangeForListingResponse

        Add an exchange for listing.

        Associate an exchange with a listing

        :param listing_id: str
        :param exchange_id: str

        :returns: :class:`AddExchangeForListingResponse`
        

    .. py:method:: create(exchange: Exchange) -> CreateExchangeResponse

        Create an exchange.

        Create an exchange

        :param exchange: :class:`Exchange`

        :returns: :class:`CreateExchangeResponse`
        

    .. py:method:: delete(id: str)

        Delete an exchange.

        This removes a listing from marketplace.

        :param id: str


        

    .. py:method:: delete_listing_from_exchange(id: str)

        Remove an exchange for listing.

        Disassociate an exchange with a listing

        :param id: str


        

    .. py:method:: get(id: str) -> GetExchangeResponse

        Get an exchange.

        Get an exchange.

        :param id: str

        :returns: :class:`GetExchangeResponse`
        

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Exchange]

        List exchanges.

        List exchanges visible to provider

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Exchange`
        

    .. py:method:: list_exchanges_for_listing(listing_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ExchangeListing]

        List exchanges for listing.

        List exchanges associated with a listing

        :param listing_id: str
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`ExchangeListing`
        

    .. py:method:: list_listings_for_exchange(exchange_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ExchangeListing]

        List listings for exchange.

        List listings associated with an exchange

        :param exchange_id: str
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`ExchangeListing`
        

    .. py:method:: update(id: str, exchange: Exchange) -> UpdateExchangeResponse

        Update exchange.

        Update an exchange

        :param id: str
        :param exchange: :class:`Exchange`

        :returns: :class:`UpdateExchangeResponse`
        
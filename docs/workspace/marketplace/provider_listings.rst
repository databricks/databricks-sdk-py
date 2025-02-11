``w.provider_listings``: Provider Listings
==========================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ProviderListingsAPI

    Listings are the core entities in the Marketplace. They represent the products that are available for
consumption.

    .. py:method:: create(listing: Listing) -> CreateListingResponse

        Create a listing.

Create a new listing

:param listing: :class:`Listing`

:returns: :class:`CreateListingResponse`


    .. py:method:: delete(id: str)

        Delete a listing.

Delete a listing

:param id: str




    .. py:method:: get(id: str) -> GetListingResponse

        Get a listing.

Get a listing

:param id: str

:returns: :class:`GetListingResponse`


    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Listing]

        List listings.

List listings owned by this provider

:param page_size: int (optional)
:param page_token: str (optional)

:returns: Iterator over :class:`Listing`


    .. py:method:: update(id: str, listing: Listing) -> UpdateListingResponse

        Update listing.

Update a listing

:param id: str
:param listing: :class:`Listing`

:returns: :class:`UpdateListingResponse`

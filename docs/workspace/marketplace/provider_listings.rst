``w.provider_listings``: Provider Listings
==========================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ProviderListingsAPI

    Listings are the core entities in the Marketplace. They represent the products that are available for
    consumption.

    .. py:method:: create(listing: Listing) -> CreateListingResponse

        Creates a listing under one of the caller's provider profiles. The listing name, provider ID and
        visibility are required, and the caller must have access to any share that the listing references.
        Returns the ID of the new listing.

        :param listing: :class:`Listing`
          Listing to create.

        :returns: :class:`CreateListingResponse`
        

    .. py:method:: delete(id: str)

        Deletes a listing permanently. The underlying share is not deleted, and consumers who already have
        access to the share keep that access until it is revoked in Delta Sharing.

        :param id: str
          ID of the listing to delete.


        

    .. py:method:: get(id: str) -> GetListingResponse

        Gets a listing owned by one of the caller's provider profiles.

        :param id: str

        :returns: :class:`GetListingResponse`
        

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Listing]

        Lists the listings owned by the provider profiles in the caller's account.

        :param page_size: int (optional)
          Maximum number of results to return per page.
        :param page_token: str (optional)
          Token from the next_page_token field of a previous response. Omit to get the first page.

        :returns: Iterator over :class:`Listing`
        

    .. py:method:: update(id: str, listing: Listing) -> UpdateListingResponse

        Updates a listing. Send the full listing definition; the listing type cannot be changed after the
        listing is created, and changing the share re-links the listing to the new share.

        :param id: str
          ID of the listing to update.
        :param listing: :class:`Listing`
          Full definition of the listing, including the fields that are not changing.

        :returns: :class:`UpdateListingResponse`
        
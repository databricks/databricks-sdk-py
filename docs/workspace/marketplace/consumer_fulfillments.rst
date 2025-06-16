``w.consumer_fulfillments``: Consumer Fulfillments
==================================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ConsumerFulfillmentsAPI

    Fulfillments are entities that allow consumers to preview installations.

    .. py:method:: get(listing_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SharedDataObject]

        Get a high level preview of the metadata of listing installable content.

        :param listing_id: str
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`SharedDataObject`
        

    .. py:method:: list(listing_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ListingFulfillment]

        Get all listings fulfillments associated with a listing. A _fulfillment_ is a potential installation.
        Standard installations contain metadata about the attached share or git repo. Only one of these fields
        will be present. Personalized installations contain metadata about the attached share or git repo, as
        well as the Delta Sharing recipient type.

        :param listing_id: str
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`ListingFulfillment`
        
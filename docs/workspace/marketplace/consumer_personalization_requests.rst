``w.consumer_personalization_requests``: Consumer Personalization Requests
==========================================================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ConsumerPersonalizationRequestsAPI

    Personalization Requests allow customers to interact with the individualized Marketplace listing flow.

    .. py:method:: create(listing_id: str, intended_use: str, accepted_consumer_terms: ConsumerTerms [, comment: Optional[str], company: Optional[str], first_name: Optional[str], is_from_lighthouse: Optional[bool], last_name: Optional[str], recipient_type: Optional[DeltaSharingRecipientType]]) -> CreatePersonalizationRequestResponse

        Create a personalization request for a listing.

        :param listing_id: str
        :param intended_use: str
        :param accepted_consumer_terms: :class:`ConsumerTerms`
        :param comment: str (optional)
        :param company: str (optional)
        :param first_name: str (optional)
        :param is_from_lighthouse: bool (optional)
        :param last_name: str (optional)
        :param recipient_type: :class:`DeltaSharingRecipientType` (optional)

        :returns: :class:`CreatePersonalizationRequestResponse`
        

    .. py:method:: get(listing_id: str) -> GetPersonalizationRequestResponse

        Get the personalization request for a listing. Each consumer can make at *most* one personalization
        request for a listing.

        :param listing_id: str

        :returns: :class:`GetPersonalizationRequestResponse`
        

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[PersonalizationRequest]

        List personalization requests for a consumer across all listings.

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`PersonalizationRequest`
        
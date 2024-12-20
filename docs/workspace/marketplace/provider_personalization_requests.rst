``w.provider_personalization_requests``: Provider Personalization Requests
==========================================================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ProviderPersonalizationRequestsAPI

    Personalization requests are an alternate to instantly available listings. Control the lifecycle of
    personalized solutions.

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[PersonalizationRequest]

        All personalization requests across all listings.
        
        List personalization requests to this provider. This will return all personalization requests,
        regardless of which listing they are for.
        
        :param page_size: int (optional)
        :param page_token: str (optional)
        
        :returns: Iterator over :class:`PersonalizationRequest`


    .. py:method:: update(listing_id: str, request_id: str, status: PersonalizationRequestStatus [, reason: Optional[str], share: Optional[ShareInfo]]) -> UpdatePersonalizationRequestResponse

        Update personalization request status.
        
        Update personalization request. This method only permits updating the status of the request.
        
        :param listing_id: str
        :param request_id: str
        :param status: :class:`PersonalizationRequestStatus`
        :param reason: str (optional)
        :param share: :class:`ShareInfo` (optional)
        
        :returns: :class:`UpdatePersonalizationRequestResponse`

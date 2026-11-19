``w.provider_personalization_requests``: Provider Personalization Requests
==========================================================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ProviderPersonalizationRequestsAPI

    Personalization requests are an alternate to instantly available listings. Control the lifecycle of
    personalized solutions.

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[PersonalizationRequest]

        List personalization requests to this provider. This will return all personalization requests,
        regardless of which listing they are for.

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`PersonalizationRequest`
        

    .. py:method:: update(listing_id: str, request_id: str, status: PersonalizationRequestStatus [, reason: Optional[str], share: Optional[ShareInfo]]) -> UpdatePersonalizationRequestResponse

        Updates the status of a personalization request; other properties of the request cannot be changed.
        Fulfilling a request grants the consumer access to the share, and denying a fulfilled request revokes
        that access. The listing must be published.

        :param listing_id: str
          ID of the listing that the request was made for.
        :param request_id: str
          ID of the personalization request.
        :param status: :class:`PersonalizationRequestStatus`
          New status of the request. Allowed transitions: NEW or REQUEST_PENDING to REQUEST_PENDING, FULFILLED
          or DENIED; FULFILLED to DENIED; DENIED to REQUEST_PENDING.
        :param reason: str (optional)
          Message for the consumer that explains the status change, at most 255 characters.
        :param share: :class:`ShareInfo` (optional)
          Share to grant the consumer access to. Required when fulfilling a request for a listing with data
          assets and not allowed with other statuses. Ignored for app and MCP server listings.

        :returns: :class:`UpdatePersonalizationRequestResponse`
        
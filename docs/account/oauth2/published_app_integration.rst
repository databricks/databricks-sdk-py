``a.published_app_integration``: OAuth Published App Integration
================================================================
.. currentmodule:: databricks.sdk.service.oauth2

.. py:class:: PublishedAppIntegrationAPI

    These APIs enable administrators to manage published OAuth app integrations, which is required for
    adding/using Published OAuth App Integration like Tableau Desktop for Databricks in AWS cloud.

    .. py:method:: create( [, app_id: Optional[str], token_access_policy: Optional[TokenAccessPolicy]]) -> CreatePublishedAppIntegrationOutput

        Create Published OAuth App Integration.

        You can retrieve the published OAuth app integration via `PublishedAppIntegration/get
        <https://docs.databricks.com/api/account/publishedappintegration/get>`__.

        :param app_id: str (optional)
          ID of the published OAuth app to enable, as returned in app_id by the list of published OAuth apps.
          The short legacy IDs of the original published apps, such as power-bi and tableau-desktop, are also
          accepted. The request fails if the app is already enabled for the account.
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Lifetimes of the tokens issued to the app. If omitted, the app's default token lifetimes apply. If
          set, both TTL fields are required.

        :returns: :class:`CreatePublishedAppIntegrationOutput`
        

    .. py:method:: delete(integration_id: str)

        Delete an existing Published OAuth App Integration. The app can no longer be used to sign in to the
        account until it is enabled again with `PublishedAppIntegration/create
        <https://docs.databricks.com/api/account/publishedappintegration/create>`__.

        :param integration_id: str
          ID of the published OAuth app integration to delete.


        

    .. py:method:: get(integration_id: str) -> GetPublishedAppIntegrationOutput

        Gets the Published OAuth App Integration for the given integration id.

        :param integration_id: str
          ID of the published OAuth app integration.

        :returns: :class:`GetPublishedAppIntegrationOutput`
        

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[GetPublishedAppIntegrationOutput]

        Get the list of published OAuth app integrations for the specified Databricks account.

        :param page_size: int (optional)
          Maximum number of integrations to return in one page, at most 1000.
        :param page_token: str (optional)
          Token from the next_page_token field of a previous response. Omit it to request the first page.

        :returns: Iterator over :class:`GetPublishedAppIntegrationOutput`
        

    .. py:method:: update(integration_id: str [, token_access_policy: Optional[TokenAccessPolicy]])

        Updates an existing published OAuth App Integration. You can retrieve the published OAuth app
        integration via `PublishedAppIntegration/get
        <https://docs.databricks.com/api/account/publishedappintegration/get>`__.

        :param integration_id: str
          ID of the published OAuth app integration to update.
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          New token lifetimes for the app. Both TTL fields are required when the policy is set; the single-use
          refresh token settings keep their current values when omitted. If the policy is omitted, the
          integration is left unchanged.


        
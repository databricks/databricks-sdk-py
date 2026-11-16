``a.custom_app_integration``: OAuth Custom App Integration
==========================================================
.. currentmodule:: databricks.sdk.service.oauth2

.. py:class:: CustomAppIntegrationAPI

    These APIs enable administrators to manage custom OAuth app integrations, which is required for
    adding/using Custom OAuth App Integration like Tableau Cloud for Databricks in AWS cloud.

    .. py:method:: create( [, confidential: Optional[bool], name: Optional[str], redirect_urls: Optional[List[str]], scopes: Optional[List[str]], token_access_policy: Optional[TokenAccessPolicy], user_authorized_scopes: Optional[List[str]]]) -> CreateCustomAppIntegrationOutput

        Create Custom OAuth App Integration.

        You can retrieve the custom OAuth app integration via `CustomAppIntegration/get
        <https://docs.databricks.com/api/account/customappintegration/get>`__.

        :param confidential: bool (optional)
          Whether to create a confidential client that authenticates with a client secret. Public clients
          receive no client secret.
        :param name: str (optional)
          Name of the custom OAuth app
        :param redirect_urls: List[str] (optional)
          OAuth redirect URLs for the application. Each URL must use https, except loopback URLs (localhost,
          127.0.0.1 or ::1), which may use http. At most 100 URLs of at most 256 characters each.
        :param scopes: List[str] (optional)
          OAuth scopes granted to the application. At least one scope is required. Supported scopes: all-apis,
          sql, offline_access, openid, profile, email, and the fine-grained API scopes listed at
          https://docs.databricks.com/api/account/scopes.
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Lifetimes of the tokens issued to the application. If omitted, access tokens are valid for 60
          minutes and refresh tokens for 7 days (10080 minutes). If set, both TTL fields are required.
        :param user_authorized_scopes: List[str] (optional)
          Scopes that will need to be consented by end user to mint the access token. If the user does not
          authorize the access token will not be minted. Must be a subset of scopes.

        :returns: :class:`CreateCustomAppIntegrationOutput`
        

    .. py:method:: delete(integration_id: str)

        Delete an existing Custom OAuth App Integration. You can retrieve the custom OAuth app integration via
        `CustomAppIntegration/get <https://docs.databricks.com/api/account/customappintegration/get>`__.

        :param integration_id: str
          ID of the custom OAuth app integration to delete.


        

    .. py:method:: get(integration_id: str) -> GetCustomAppIntegrationOutput

        Gets the Custom OAuth App Integration for the given integration id.

        :param integration_id: str
          The OAuth app integration ID.

        :returns: :class:`GetCustomAppIntegrationOutput`
        

    .. py:method:: list( [, include_creator_username: Optional[bool], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[GetCustomAppIntegrationOutput]

        Get the list of custom OAuth app integrations for the specified Databricks account.

        :param include_creator_username: bool (optional)
          When true, each returned integration includes creator_username.
        :param page_size: int (optional)
          Maximum number of integrations to return in one page, at most 1000.
        :param page_token: str (optional)
          Token from the next_page_token field of a previous response. Omit it to request the first page.

        :returns: Iterator over :class:`GetCustomAppIntegrationOutput`
        

    .. py:method:: update(integration_id: str [, redirect_urls: Optional[List[str]], scopes: Optional[List[str]], token_access_policy: Optional[TokenAccessPolicy], user_authorized_scopes: Optional[List[str]]])

        Updates an existing custom OAuth App Integration. You can retrieve the custom OAuth app integration
        via `CustomAppIntegration/get <https://docs.databricks.com/api/account/customappintegration/get>`__.

        :param integration_id: str
          ID of the custom OAuth app integration to update.
        :param redirect_urls: List[str] (optional)
          New OAuth redirect URLs for the application. Replaces the existing list; same constraints as on
          create.
        :param scopes: List[str] (optional)
          List of OAuth scopes to be updated in the custom OAuth app integration, similar to redirect URIs
          this will fully replace the existing values instead of appending
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          New token lifetimes for the application. Both TTL fields are required when the policy is set; the
          single-use refresh token settings keep their current values when omitted.
        :param user_authorized_scopes: List[str] (optional)
          Scopes that will need to be consented by end user to mint the access token. If the user does not
          authorize the access token will not be minted. Must be a subset of scopes.


        
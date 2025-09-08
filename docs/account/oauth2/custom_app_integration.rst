``a.custom_app_integration``: OAuth Custom App Integration
==========================================================
.. currentmodule:: databricks.sdk.service.oauth2

.. py:class:: CustomAppIntegrationAPI

    These APIs enable administrators to manage custom OAuth app integrations, which is required for
    adding/using Custom OAuth App Integration like Tableau Cloud for Databricks in AWS cloud.

    .. py:method:: create( [, confidential: Optional[bool], name: Optional[str], redirect_urls: Optional[List[str]], scopes: Optional[List[str]], token_access_policy: Optional[TokenAccessPolicy], user_authorized_scopes: Optional[List[str]]]) -> CreateCustomAppIntegrationOutput

        Create Custom OAuth App Integration.
        
        You can retrieve the custom OAuth app integration via :method:CustomAppIntegration/get.
        
        :param confidential: bool (optional)
          This field indicates whether an OAuth client secret is required to authenticate this client.
        :param name: str (optional)
          Name of the custom OAuth app
        :param redirect_urls: List[str] (optional)
          List of OAuth redirect urls
        :param scopes: List[str] (optional)
          OAuth scopes granted to the application. Supported scopes: all-apis, sql, offline_access, openid,
          profile, email.
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy
        :param user_authorized_scopes: List[str] (optional)
          Scopes that will need to be consented by end user to mint the access token. If the user does not
          authorize the access token will not be minted. Must be a subset of scopes.
        
        :returns: :class:`CreateCustomAppIntegrationOutput`
        

    .. py:method:: delete(integration_id: str)

        Delete an existing Custom OAuth App Integration. You can retrieve the custom OAuth app integration via
        :method:CustomAppIntegration/get.
        
        :param integration_id: str
        
        
        

    .. py:method:: get(integration_id: str) -> GetCustomAppIntegrationOutput

        Gets the Custom OAuth App Integration for the given integration id.
        
        :param integration_id: str
          The OAuth app integration ID.
        
        :returns: :class:`GetCustomAppIntegrationOutput`
        

    .. py:method:: list( [, include_creator_username: Optional[bool], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[GetCustomAppIntegrationOutput]

        Get the list of custom OAuth app integrations for the specified Databricks account
        
        :param include_creator_username: bool (optional)
        :param page_size: int (optional)
        :param page_token: str (optional)
        
        :returns: Iterator over :class:`GetCustomAppIntegrationOutput`
        

    .. py:method:: update(integration_id: str [, redirect_urls: Optional[List[str]], scopes: Optional[List[str]], token_access_policy: Optional[TokenAccessPolicy], user_authorized_scopes: Optional[List[str]]])

        Updates an existing custom OAuth App Integration. You can retrieve the custom OAuth app integration
        via :method:CustomAppIntegration/get.
        
        :param integration_id: str
        :param redirect_urls: List[str] (optional)
          List of OAuth redirect urls to be updated in the custom OAuth app integration
        :param scopes: List[str] (optional)
          List of OAuth scopes to be updated in the custom OAuth app integration, similar to redirect URIs
          this will fully replace the existing values instead of appending
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy to be updated in the custom OAuth app integration
        :param user_authorized_scopes: List[str] (optional)
          Scopes that will need to be consented by end user to mint the access token. If the user does not
          authorize the access token will not be minted. Must be a subset of scopes.
        
        
        
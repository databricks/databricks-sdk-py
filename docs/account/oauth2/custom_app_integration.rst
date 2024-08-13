``a.custom_app_integration``: OAuth Custom App Integration
==========================================================
.. currentmodule:: databricks.sdk.service.oauth2

.. py:class:: CustomAppIntegrationAPI

    These APIs enable administrators to manage custom OAuth app integrations, which is required for
    adding/using Custom OAuth App Integration like Tableau Cloud for Databricks in AWS cloud.

    .. py:method:: create( [, confidential: Optional[bool], name: Optional[str], redirect_urls: Optional[List[str]], scopes: Optional[List[str]], token_access_policy: Optional[TokenAccessPolicy]]) -> CreateCustomAppIntegrationOutput

        Create Custom OAuth App Integration.
        
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
        
        :returns: :class:`CreateCustomAppIntegrationOutput`
        

    .. py:method:: delete(integration_id: str)

        Delete Custom OAuth App Integration.
        
        Delete an existing Custom OAuth App Integration. You can retrieve the custom OAuth app integration via
        :method:CustomAppIntegration/get.
        
        :param integration_id: str
        
        
        

    .. py:method:: get(integration_id: str) -> GetCustomAppIntegrationOutput

        Get OAuth Custom App Integration.
        
        Gets the Custom OAuth App Integration for the given integration id.
        
        :param integration_id: str
        
        :returns: :class:`GetCustomAppIntegrationOutput`
        

    .. py:method:: list( [, include_creator_username: Optional[bool], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[GetCustomAppIntegrationOutput]

        Get custom oauth app integrations.
        
        Get the list of custom OAuth app integrations for the specified Databricks account
        
        :param include_creator_username: bool (optional)
        :param page_size: int (optional)
        :param page_token: str (optional)
        
        :returns: Iterator over :class:`GetCustomAppIntegrationOutput`
        

    .. py:method:: update(integration_id: str [, redirect_urls: Optional[List[str]], token_access_policy: Optional[TokenAccessPolicy]])

        Updates Custom OAuth App Integration.
        
        Updates an existing custom OAuth App Integration. You can retrieve the custom OAuth app integration
        via :method:CustomAppIntegration/get.
        
        :param integration_id: str
        :param redirect_urls: List[str] (optional)
          List of OAuth redirect urls to be updated in the custom OAuth app integration
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy to be updated in the custom OAuth app integration
        
        
        
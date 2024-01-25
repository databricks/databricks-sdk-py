OAuth Custom App Integration
============================
.. currentmodule:: databricks.sdk.service.oauth2

.. py:class:: CustomAppIntegrationAPI

    These APIs enable administrators to manage custom oauth app integrations, which is required for
    adding/using Custom OAuth App Integration like Tableau Cloud for Databricks in AWS cloud.

    .. py:method:: create(name: str, redirect_urls: List[str] [, confidential: Optional[bool], scopes: Optional[List[str]], token_access_policy: Optional[TokenAccessPolicy]]) -> CreateCustomAppIntegrationOutput

        Create Custom OAuth App Integration.
        
        Create Custom OAuth App Integration.
        
        You can retrieve the custom oauth app integration via :method:CustomAppIntegration/get.
        
        :param name: str
          name of the custom oauth app
        :param redirect_urls: List[str]
          List of oauth redirect urls
        :param confidential: bool (optional)
          indicates if an oauth client-secret should be generated
        :param scopes: List[str] (optional)
          OAuth scopes granted to the application. Supported scopes: all-apis, sql, offline_access, openid,
          profile, email.
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy
        
        :returns: :class:`CreateCustomAppIntegrationOutput`
        

    .. py:method:: delete(integration_id: str)

        Delete Custom OAuth App Integration.
        
        Delete an existing Custom OAuth App Integration. You can retrieve the custom oauth app integration via
        :method:CustomAppIntegration/get.
        
        :param integration_id: str
          The oauth app integration ID.
        
        
        

    .. py:method:: get(integration_id: str) -> GetCustomAppIntegrationOutput

        Get OAuth Custom App Integration.
        
        Gets the Custom OAuth App Integration for the given integration id.
        
        :param integration_id: str
          The oauth app integration ID.
        
        :returns: :class:`GetCustomAppIntegrationOutput`
        

    .. py:method:: list() -> Iterator[GetCustomAppIntegrationOutput]

        Get custom oauth app integrations.
        
        Get the list of custom oauth app integrations for the specified Databricks account
        
        :returns: Iterator over :class:`GetCustomAppIntegrationOutput`
        

    .. py:method:: update(integration_id: str [, redirect_urls: Optional[List[str]], token_access_policy: Optional[TokenAccessPolicy]])

        Updates Custom OAuth App Integration.
        
        Updates an existing custom OAuth App Integration. You can retrieve the custom oauth app integration
        via :method:CustomAppIntegration/get.
        
        :param integration_id: str
          The oauth app integration ID.
        :param redirect_urls: List[str] (optional)
          List of oauth redirect urls to be updated in the custom oauth app integration
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy to be updated in the custom oauth app integration
        
        
        
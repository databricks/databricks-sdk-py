OAuth Custom App Integration
============================
.. py:class:: CustomAppIntegrationAPI

    These APIs enable administrators to manage custom oauth app integrations, which is required for
    adding/using Custom OAuth App Integration like Tableau Cloud for Databricks in AWS cloud.

    .. py:method:: create(name, redirect_urls [, confidential, scopes, token_access_policy])

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
        

    .. py:method:: delete(integration_id)

        Delete Custom OAuth App Integration.
        
        Delete an existing Custom OAuth App Integration. You can retrieve the custom oauth app integration via
        :method:CustomAppIntegration/get.
        
        :param integration_id: str
          The oauth app integration ID.
        
        
        

    .. py:method:: get(integration_id)

        Get OAuth Custom App Integration.
        
        Gets the Custom OAuth App Integration for the given integration id.
        
        :param integration_id: str
          The oauth app integration ID.
        
        :returns: :class:`GetCustomAppIntegrationOutput`
        

    .. py:method:: list()

        Get custom oauth app integrations.
        
        Get the list of custom oauth app integrations for the specified Databricks account
        
        :returns: Iterator over :class:`GetCustomAppIntegrationOutput`
        

    .. py:method:: update(integration_id [, redirect_urls, token_access_policy])

        Updates Custom OAuth App Integration.
        
        Updates an existing custom OAuth App Integration. You can retrieve the custom oauth app integration
        via :method:CustomAppIntegration/get.
        
        :param integration_id: str
          The oauth app integration ID.
        :param redirect_urls: List[str] (optional)
          List of oauth redirect urls to be updated in the custom oauth app integration
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy to be updated in the custom oauth app integration
        
        
        
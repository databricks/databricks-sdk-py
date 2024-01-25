OAuth Published App Integration
===============================
.. currentmodule:: databricks.sdk.service.oauth2

.. py:class:: PublishedAppIntegrationAPI

    These APIs enable administrators to manage published oauth app integrations, which is required for
    adding/using Published OAuth App Integration like Tableau Desktop for Databricks in AWS cloud.

    .. py:method:: create( [, app_id: Optional[str], token_access_policy: Optional[TokenAccessPolicy]]) -> CreatePublishedAppIntegrationOutput

        Create Published OAuth App Integration.
        
        Create Published OAuth App Integration.
        
        You can retrieve the published oauth app integration via :method:PublishedAppIntegration/get.
        
        :param app_id: str (optional)
          app_id of the oauth published app integration. For example power-bi, tableau-deskop
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy
        
        :returns: :class:`CreatePublishedAppIntegrationOutput`
        

    .. py:method:: delete(integration_id: str)

        Delete Published OAuth App Integration.
        
        Delete an existing Published OAuth App Integration. You can retrieve the published oauth app
        integration via :method:PublishedAppIntegration/get.
        
        :param integration_id: str
          The oauth app integration ID.
        
        
        

    .. py:method:: get(integration_id: str) -> GetPublishedAppIntegrationOutput

        Get OAuth Published App Integration.
        
        Gets the Published OAuth App Integration for the given integration id.
        
        :param integration_id: str
          The oauth app integration ID.
        
        :returns: :class:`GetPublishedAppIntegrationOutput`
        

    .. py:method:: list() -> Iterator[GetPublishedAppIntegrationOutput]

        Get published oauth app integrations.
        
        Get the list of published oauth app integrations for the specified Databricks account
        
        :returns: Iterator over :class:`GetPublishedAppIntegrationOutput`
        

    .. py:method:: update(integration_id: str [, token_access_policy: Optional[TokenAccessPolicy]])

        Updates Published OAuth App Integration.
        
        Updates an existing published OAuth App Integration. You can retrieve the published oauth app
        integration via :method:PublishedAppIntegration/get.
        
        :param integration_id: str
          The oauth app integration ID.
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy to be updated in the published oauth app integration
        
        
        
``w.service_principal_secrets_proxy``: Service Principal Secrets Proxy
======================================================================
.. currentmodule:: databricks.sdk.service.oauth2

.. py:class:: ServicePrincipalSecretsProxyAPI

    These APIs enable administrators to manage service principal secrets at the workspace level. To use these
    APIs, the service principal must be first added to the current workspace.
    
    You can use the generated secrets to obtain OAuth access tokens for a service principal, which can then be
    used to access Databricks Accounts and Workspace APIs. For more information, see [Authentication using
    OAuth tokens for service principals].
    
    In addition, the generated secrets can be used to configure the Databricks Terraform Providerto
    authenticate with the service principal. For more information, see [Databricks Terraform Provider].
    
    [Authentication using OAuth tokens for service principals]: https://docs.databricks.com/dev-tools/authentication-oauth.html
    [Databricks Terraform Provider]: https://github.com/databricks/terraform-provider-databricks/blob/master/docs/index.md#authenticating-with-service-principal

    .. py:method:: create(service_principal_id: str [, lifetime: Optional[str]]) -> CreateServicePrincipalSecretResponse

        Create a secret for the given service principal.
        
        :param service_principal_id: str
          The service principal ID.
        :param lifetime: str (optional)
          The lifetime of the secret in seconds. If this parameter is not provided, the secret will have a
          default lifetime of 730 days (63072000s).
        
        :returns: :class:`CreateServicePrincipalSecretResponse`
        

    .. py:method:: delete(service_principal_id: str, secret_id: str)

        Delete a secret from the given service principal.
        
        :param service_principal_id: str
          The service principal ID.
        :param secret_id: str
          The secret ID.
        
        
        

    .. py:method:: list(service_principal_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SecretInfo]

        List all secrets associated with the given service principal. This operation only returns information
        about the secrets themselves and does not include the secret values.
        
        :param service_principal_id: str
          The service principal ID.
        :param page_size: int (optional)
        :param page_token: str (optional)
          An opaque page token which was the `next_page_token` in the response of the previous request to list
          the secrets for this service principal. Provide this token to retrieve the next page of secret
          entries. When providing a `page_token`, all other parameters provided to the request must match the
          previous request. To list all of the secrets for a service principal, it is necessary to continue
          requesting pages of entries until the response contains no `next_page_token`. Note that the number
          of entries returned must not be used to determine when the listing is complete.
        
        :returns: Iterator over :class:`SecretInfo`
        
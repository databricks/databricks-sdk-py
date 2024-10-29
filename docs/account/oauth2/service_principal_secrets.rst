``a.service_principal_secrets``: Service Principal Secrets
==========================================================
.. currentmodule:: databricks.sdk.service.oauth2

.. py:class:: ServicePrincipalSecretsAPI

    These APIs enable administrators to manage service principal secrets.

You can use the generated secrets to obtain OAuth access tokens for a service principal, which can then be
used to access Databricks Accounts and Workspace APIs. For more information, see [Authentication using
OAuth tokens for service principals],

In addition, the generated secrets can be used to configure the Databricks Terraform Provider to
authenticate with the service principal. For more information, see [Databricks Terraform Provider].

[Authentication using OAuth tokens for service principals]: https://docs.databricks.com/dev-tools/authentication-oauth.html
[Databricks Terraform Provider]: https://github.com/databricks/terraform-provider-databricks/blob/master/docs/index.md#authenticating-with-service-principal

    .. py:method:: create(service_principal_id: int) -> CreateServicePrincipalSecretResponse

        Create service principal secret.

Create a secret for the given service principal.

:param service_principal_id: int
  The service principal ID.

:returns: :class:`CreateServicePrincipalSecretResponse`


    .. py:method:: delete(service_principal_id: int, secret_id: str)

        Delete service principal secret.

Delete a secret from the given service principal.

:param service_principal_id: int
  The service principal ID.
:param secret_id: str
  The secret ID.




    .. py:method:: list(service_principal_id: int) -> Iterator[SecretInfo]

        List service principal secrets.

List all secrets associated with the given service principal. This operation only returns information
about the secrets themselves and does not include the secret values.

:param service_principal_id: int
  The service principal ID.

:returns: Iterator over :class:`SecretInfo`

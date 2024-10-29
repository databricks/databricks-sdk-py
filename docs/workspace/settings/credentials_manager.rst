``w.credentials_manager``: Credentials Manager
==============================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: CredentialsManagerAPI

    Credentials manager interacts with with Identity Providers to to perform token exchanges using stored
credentials and refresh tokens.

    .. py:method:: exchange_token(partition_id: PartitionId, token_type: List[TokenType], scopes: List[str]) -> ExchangeTokenResponse

        Exchange token.

Exchange tokens with an Identity Provider to get a new access token. It allows specifying scopes to
determine token permissions.

:param partition_id: :class:`PartitionId`
  The partition of Credentials store
:param token_type: List[:class:`TokenType`]
  A list of token types being requested
:param scopes: List[str]
  Array of scopes for the token request.

:returns: :class:`ExchangeTokenResponse`

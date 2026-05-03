``w.credentials_manager``: Credentials Manager
==============================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: CredentialsManagerAPI

    Credentials manager interacts with with Identity Providers to to perform token exchanges using stored
    credentials and refresh tokens.

    .. py:method:: exchange_token(partition_id: PartitionId, token_type: List[TokenType], scopes: List[str]) -> ExchangeTokenResponse

        Exchange tokens with an Identity Provider to get a new access token. It allows specifying scopes to
        determine token permissions.

        POST /exchange-tokens/token is the documented public form, expressed via `google.api.http` below. GET
        /exchange-tokens/$exchange is a legacy alias used by the Spark driver's OAuth refresh path
        (DBHttpClient#get sends a body via HttpGetWithEntity) and stays on the legacy `option (rpc).endpoints`
        annotation: its path contains a literal `$`, which `google.api.http`'s LITERAL grammar does not allow,
        and `HttpPathParser` does not percent-decode template segments (so encoding as `%24exchange` would not
        match the literal `$exchange` path the Spark driver sends). Per-endpoint `visibility:
        PUBLIC_UNDOCUMENTED` preserves the DECO-7732 intent of suppressing the GET alias from the public API
        spec.

        :param partition_id: :class:`PartitionId`
          The partition of Credentials store
        :param token_type: List[:class:`TokenType`]
          A list of token types being requested
        :param scopes: List[str]
          Array of scopes for the token request.

        :returns: :class:`ExchangeTokenResponse`
        
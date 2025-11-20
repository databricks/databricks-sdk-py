``w.tokens``: Token
===================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: TokensAPI

    The Token API allows you to create, list, and revoke tokens that can be used to authenticate and access
    Databricks REST APIs.

    .. py:method:: create( [, comment: Optional[str], lifetime_seconds: Optional[int], scopes: Optional[List[str]]]) -> CreateTokenResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            token = w.tokens.create(comment=f"sdk-{time.time_ns()}", lifetime_seconds=300)
            
            # cleanup
            w.tokens.delete(token_id=token.token_info.token_id)

        Creates and returns a token for a user. If this call is made through token authentication, it creates
        a token with the same client ID as the authenticated token. If the user's token quota is exceeded,
        this call returns an error **QUOTA_EXCEEDED**.

        :param comment: str (optional)
          Optional description to attach to the token.
        :param lifetime_seconds: int (optional)
          The lifetime of the token, in seconds.

          If the lifetime is not specified, this token remains valid indefinitely.
        :param scopes: List[str] (optional)
          Optional scopes of the token.

        :returns: :class:`CreateTokenResponse`
        

    .. py:method:: delete(token_id: str)

        Revokes an access token.

        If a token with the specified ID is not valid, this call returns an error **RESOURCE_DOES_NOT_EXIST**.

        :param token_id: str
          The ID of the token to be revoked.


        

    .. py:method:: list() -> Iterator[PublicTokenInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.tokens.list()

        Lists all the valid tokens for a user-workspace pair.


        :returns: Iterator over :class:`PublicTokenInfo`
        
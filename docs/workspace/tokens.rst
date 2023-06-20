Token
=====
.. py:class:: TokensAPI

    The Token API allows you to create, list, and revoke tokens that can be used to authenticate and access
    Databricks REST APIs.

    .. py:method:: create( [, comment, lifetime_seconds])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            token = w.tokens.create(comment=f'sdk-{time.time_ns()}', lifetime_seconds=300)
            
            # cleanup
            w.tokens.delete(delete=token.token_info.token_id)

        Create a user token.
        
        Creates and returns a token for a user. If this call is made through token authentication, it creates
        a token with the same client ID as the authenticated token. If the user's token quota is exceeded,
        this call returns an error **QUOTA_EXCEEDED**.
        
        :param comment: str (optional)
          Optional description to attach to the token.
        :param lifetime_seconds: int (optional)
          The lifetime of the token, in seconds.
          
          If the ifetime is not specified, this token remains valid indefinitely.
        
        :returns: :class:`CreateTokenResponse`
        

    .. py:method:: delete(token_id)

        Revoke token.
        
        Revokes an access token.
        
        If a token with the specified ID is not valid, this call returns an error **RESOURCE_DOES_NOT_EXIST**.
        
        :param token_id: str
          The ID of the token to be revoked.
        
        
        

    .. py:method:: list()

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.tokens.list()

        List tokens.
        
        Lists all the valid tokens for a user-workspace pair.
        
        :returns: Iterator over :class:`TokenInfo`
        
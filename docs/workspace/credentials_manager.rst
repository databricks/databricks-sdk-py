Credentials Manager
===================
.. py:class:: CredentialsManagerAPI

    Credentials manager interacts with with Identity Providers to to perform token exchanges using stored
    credentials and refresh tokens.

    .. py:method:: exchange_token(partition_id, token_type, scopes)

        Exchange token.
        
        Exchange tokens with an Identity Provider to get a new access token. It allowes specifying scopes to
        determine token permissions.
        
        :param partition_id: :class:`PartitionId`
        :param token_type: List[:class:`TokenType`]
        :param scopes: List[str]
          Array of scopes for the token request.
        
        :returns: :class:`ExchangeTokenResponse`
        
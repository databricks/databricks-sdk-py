Recipient Activation
====================
.. py:class:: RecipientActivationAPI

    Databricks Recipient Activation REST API

    .. py:method:: get_activation_url_info(activation_url)

        Get a share activation URL.
        
        Gets an activation URL for a share.
        
        :param activation_url: str
          The one time activation url. It also accepts activation token.
        
        
        

    .. py:method:: retrieve_token(activation_url)

        Get an access token.
        
        Retrieve access token with an activation url. This is a public API without any authentication.
        
        :param activation_url: str
          The one time activation url. It also accepts activation token.
        
        :returns: :class:`RetrieveTokenResponse`
        
``w.recipient_activation``: Recipient Activation
================================================
.. currentmodule:: databricks.sdk.service.sharing

.. py:class:: RecipientActivationAPI

    The Recipient Activation API is only applicable in the open sharing model where the recipient object has
    the authentication type of `TOKEN`. The data recipient follows the activation link shared by the data
    provider to download the credential file that includes the access token. The recipient will then use the
    credential file to establish a secure connection with the provider to receive the shared data.
    
    Note that you can download the credential file only once. Recipients should treat the downloaded
    credential as a secret and must not share it outside of their organization.

    .. py:method:: get_activation_url_info(activation_url: str)

        Get a share activation URL.
        
        Gets an activation URL for a share.
        
        :param activation_url: str
          The one time activation url. It also accepts activation token.
        
        
        

    .. py:method:: retrieve_token(activation_url: str) -> RetrieveTokenResponse

        Get an access token.
        
        Retrieve access token with an activation url. This is a public API without any authentication.
        
        :param activation_url: str
          The one time activation url. It also accepts activation token.
        
        :returns: :class:`RetrieveTokenResponse`
        
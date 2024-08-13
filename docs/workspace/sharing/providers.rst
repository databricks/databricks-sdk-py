``w.providers``: Providers
==========================
.. currentmodule:: databricks.sdk.service.sharing

.. py:class:: ProvidersAPI

    A data provider is an object representing the organization in the real world who shares the data. A
    provider contains shares which further contain the shared data.

    .. py:method:: create(name: str, authentication_type: AuthenticationType [, comment: Optional[str], recipient_profile_str: Optional[str]]) -> ProviderInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            public_share_recipient = """{
                    "shareCredentialsVersion":1,
                    "bearerToken":"dapiabcdefghijklmonpqrstuvwxyz",
                    "endpoint":"https://sharing.delta.io/delta-sharing/"
                }
            """
            
            created = w.providers.create(name=f'sdk-{time.time_ns()}', recipient_profile_str=public_share_recipient)
            
            # cleanup
            w.providers.delete(name=created.name)

        Create an auth provider.
        
        Creates a new authentication provider minimally based on a name and authentication type. The caller
        must be an admin on the metastore.
        
        :param name: str
          The name of the Provider.
        :param authentication_type: :class:`AuthenticationType`
          The delta sharing authentication type.
        :param comment: str (optional)
          Description about the provider.
        :param recipient_profile_str: str (optional)
          This field is required when the __authentication_type__ is **TOKEN** or not provided.
        
        :returns: :class:`ProviderInfo`
        

    .. py:method:: delete(name: str)

        Delete a provider.
        
        Deletes an authentication provider, if the caller is a metastore admin or is the owner of the
        provider.
        
        :param name: str
          Name of the provider.
        
        
        

    .. py:method:: get(name: str) -> ProviderInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            public_share_recipient = """{
                    "shareCredentialsVersion":1,
                    "bearerToken":"dapiabcdefghijklmonpqrstuvwxyz",
                    "endpoint":"https://sharing.delta.io/delta-sharing/"
                }
            """
            
            created = w.providers.create(name=f'sdk-{time.time_ns()}', recipient_profile_str=public_share_recipient)
            
            _ = w.providers.get(name=created.name)
            
            # cleanup
            w.providers.delete(name=created.name)

        Get a provider.
        
        Gets a specific authentication provider. The caller must supply the name of the provider, and must
        either be a metastore admin or the owner of the provider.
        
        :param name: str
          Name of the provider.
        
        :returns: :class:`ProviderInfo`
        

    .. py:method:: list( [, data_provider_global_metastore_id: Optional[str], max_results: Optional[int], page_token: Optional[str]]) -> Iterator[ProviderInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sharing
            
            w = WorkspaceClient()
            
            all = w.providers.list(sharing.ListProvidersRequest())

        List providers.
        
        Gets an array of available authentication providers. The caller must either be a metastore admin or
        the owner of the providers. Providers not owned by the caller are not included in the response. There
        is no guarantee of a specific ordering of the elements in the array.
        
        :param data_provider_global_metastore_id: str (optional)
          If not provided, all providers will be returned. If no providers exist with this ID, no results will
          be returned.
        :param max_results: int (optional)
          Maximum number of providers to return. - when set to 0, the page length is set to a server
          configured value (recommended); - when set to a value greater than 0, the page length is the minimum
          of this value and a server configured value; - when set to a value less than 0, an invalid parameter
          error is returned; - If not set, all valid providers are returned (not recommended). - Note: The
          number of returned providers might be less than the specified max_results size, even zero. The only
          definitive indication that no further providers can be fetched is when the next_page_token is unset
          from the response.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`ProviderInfo`
        

    .. py:method:: list_shares(name: str [, max_results: Optional[int], page_token: Optional[str]]) -> Iterator[ProviderShare]


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            public_share_recipient = """{
                    "shareCredentialsVersion":1,
                    "bearerToken":"dapiabcdefghijklmonpqrstuvwxyz",
                    "endpoint":"https://sharing.delta.io/delta-sharing/"
                }
            """
            
            created = w.providers.create(name=f'sdk-{time.time_ns()}', recipient_profile_str=public_share_recipient)
            
            shares = w.providers.list_shares(name=created.name)
            
            # cleanup
            w.providers.delete(name=created.name)

        List shares by Provider.
        
        Gets an array of a specified provider's shares within the metastore where:
        
        * the caller is a metastore admin, or * the caller is the owner.
        
        :param name: str
          Name of the provider in which to list shares.
        :param max_results: int (optional)
          Maximum number of shares to return. - when set to 0, the page length is set to a server configured
          value (recommended); - when set to a value greater than 0, the page length is the minimum of this
          value and a server configured value; - when set to a value less than 0, an invalid parameter error
          is returned; - If not set, all valid shares are returned (not recommended). - Note: The number of
          returned shares might be less than the specified max_results size, even zero. The only definitive
          indication that no further shares can be fetched is when the next_page_token is unset from the
          response.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`ProviderShare`
        

    .. py:method:: update(name: str [, comment: Optional[str], new_name: Optional[str], owner: Optional[str], recipient_profile_str: Optional[str]]) -> ProviderInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            public_share_recipient = """{
                    "shareCredentialsVersion":1,
                    "bearerToken":"dapiabcdefghijklmonpqrstuvwxyz",
                    "endpoint":"https://sharing.delta.io/delta-sharing/"
                }
            """
            
            created = w.providers.create(name=f'sdk-{time.time_ns()}', recipient_profile_str=public_share_recipient)
            
            _ = w.providers.update(name=created.name, comment="Comment for update")
            
            # cleanup
            w.providers.delete(name=created.name)

        Update a provider.
        
        Updates the information for an authentication provider, if the caller is a metastore admin or is the
        owner of the provider. If the update changes the provider name, the caller must be both a metastore
        admin and the owner of the provider.
        
        :param name: str
          Name of the provider.
        :param comment: str (optional)
          Description about the provider.
        :param new_name: str (optional)
          New name for the provider.
        :param owner: str (optional)
          Username of Provider owner.
        :param recipient_profile_str: str (optional)
          This field is required when the __authentication_type__ is **TOKEN** or not provided.
        
        :returns: :class:`ProviderInfo`
        
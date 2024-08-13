``w.recipients``: Recipients
============================
.. currentmodule:: databricks.sdk.service.sharing

.. py:class:: RecipientsAPI

    A recipient is an object you create using :method:recipients/create to represent an organization which you
    want to allow access shares. The way how sharing works differs depending on whether or not your recipient
    has access to a Databricks workspace that is enabled for Unity Catalog:
    
    - For recipients with access to a Databricks workspace that is enabled for Unity Catalog, you can create a
    recipient object along with a unique sharing identifier you get from the recipient. The sharing identifier
    is the key identifier that enables the secure connection. This sharing mode is called
    **Databricks-to-Databricks sharing**.
    
    - For recipients without access to a Databricks workspace that is enabled for Unity Catalog, when you
    create a recipient object, Databricks generates an activation link you can send to the recipient. The
    recipient follows the activation link to download the credential file, and then uses the credential file
    to establish a secure connection to receive the shared data. This sharing mode is called **open sharing**.

    .. py:method:: create(name: str, authentication_type: AuthenticationType [, comment: Optional[str], data_recipient_global_metastore_id: Optional[str], expiration_time: Optional[int], ip_access_list: Optional[IpAccessList], owner: Optional[str], properties_kvpairs: Optional[SecurablePropertiesKvPairs], sharing_code: Optional[str]]) -> RecipientInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.recipients.create(name=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.recipients.delete(name=created.name)

        Create a share recipient.
        
        Creates a new recipient with the delta sharing authentication type in the metastore. The caller must
        be a metastore admin or has the **CREATE_RECIPIENT** privilege on the metastore.
        
        :param name: str
          Name of Recipient.
        :param authentication_type: :class:`AuthenticationType`
          The delta sharing authentication type.
        :param comment: str (optional)
          Description about the recipient.
        :param data_recipient_global_metastore_id: str (optional)
          The global Unity Catalog metastore id provided by the data recipient. This field is required when
          the __authentication_type__ is **DATABRICKS**. The identifier is of format
          __cloud__:__region__:__metastore-uuid__.
        :param expiration_time: int (optional)
          Expiration timestamp of the token, in epoch milliseconds.
        :param ip_access_list: :class:`IpAccessList` (optional)
          IP Access List
        :param owner: str (optional)
          Username of the recipient owner.
        :param properties_kvpairs: :class:`SecurablePropertiesKvPairs` (optional)
          Recipient properties as map of string key-value pairs.
        :param sharing_code: str (optional)
          The one-time sharing code provided by the data recipient. This field is required when the
          __authentication_type__ is **DATABRICKS**.
        
        :returns: :class:`RecipientInfo`
        

    .. py:method:: delete(name: str)

        Delete a share recipient.
        
        Deletes the specified recipient from the metastore. The caller must be the owner of the recipient.
        
        :param name: str
          Name of the recipient.
        
        
        

    .. py:method:: get(name: str) -> RecipientInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.recipients.create(name=f'sdk-{time.time_ns()}')
            
            _ = w.recipients.get(name=created.name)
            
            # cleanup
            w.recipients.delete(name=created.name)

        Get a share recipient.
        
        Gets a share recipient from the metastore if:
        
        * the caller is the owner of the share recipient, or: * is a metastore admin
        
        :param name: str
          Name of the recipient.
        
        :returns: :class:`RecipientInfo`
        

    .. py:method:: list( [, data_recipient_global_metastore_id: Optional[str], max_results: Optional[int], page_token: Optional[str]]) -> Iterator[RecipientInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sharing
            
            w = WorkspaceClient()
            
            all = w.recipients.list(sharing.ListRecipientsRequest())

        List share recipients.
        
        Gets an array of all share recipients within the current metastore where:
        
        * the caller is a metastore admin, or * the caller is the owner. There is no guarantee of a specific
        ordering of the elements in the array.
        
        :param data_recipient_global_metastore_id: str (optional)
          If not provided, all recipients will be returned. If no recipients exist with this ID, no results
          will be returned.
        :param max_results: int (optional)
          Maximum number of recipients to return. - when set to 0, the page length is set to a server
          configured value (recommended); - when set to a value greater than 0, the page length is the minimum
          of this value and a server configured value; - when set to a value less than 0, an invalid parameter
          error is returned; - If not set, all valid recipients are returned (not recommended). - Note: The
          number of returned recipients might be less than the specified max_results size, even zero. The only
          definitive indication that no further recipients can be fetched is when the next_page_token is unset
          from the response.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`RecipientInfo`
        

    .. py:method:: rotate_token(name: str, existing_token_expire_in_seconds: int) -> RecipientInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.recipients.create(name=f'sdk-{time.time_ns()}')
            
            recipient_info = w.recipients.rotate_token(name=created.name, existing_token_expire_in_seconds=0)
            
            # cleanup
            w.recipients.delete(name=created.name)

        Rotate a token.
        
        Refreshes the specified recipient's delta sharing authentication token with the provided token info.
        The caller must be the owner of the recipient.
        
        :param name: str
          The name of the recipient.
        :param existing_token_expire_in_seconds: int
          The expiration time of the bearer token in ISO 8601 format. This will set the expiration_time of
          existing token only to a smaller timestamp, it cannot extend the expiration_time. Use 0 to expire
          the existing token immediately, negative number will return an error.
        
        :returns: :class:`RecipientInfo`
        

    .. py:method:: share_permissions(name: str [, max_results: Optional[int], page_token: Optional[str]]) -> GetRecipientSharePermissionsResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.recipients.create(name=f'sdk-{time.time_ns()}')
            
            share_permissions = w.recipients.share_permissions(name=created.name)
            
            # cleanup
            w.recipients.delete(name=created.name)

        Get recipient share permissions.
        
        Gets the share permissions for the specified Recipient. The caller must be a metastore admin or the
        owner of the Recipient.
        
        :param name: str
          The name of the Recipient.
        :param max_results: int (optional)
          Maximum number of permissions to return. - when set to 0, the page length is set to a server
          configured value (recommended); - when set to a value greater than 0, the page length is the minimum
          of this value and a server configured value; - when set to a value less than 0, an invalid parameter
          error is returned; - If not set, all valid permissions are returned (not recommended). - Note: The
          number of returned permissions might be less than the specified max_results size, even zero. The
          only definitive indication that no further permissions can be fetched is when the next_page_token is
          unset from the response.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: :class:`GetRecipientSharePermissionsResponse`
        

    .. py:method:: update(name: str [, comment: Optional[str], expiration_time: Optional[int], ip_access_list: Optional[IpAccessList], new_name: Optional[str], owner: Optional[str], properties_kvpairs: Optional[SecurablePropertiesKvPairs]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.recipients.create(name=f'sdk-{time.time_ns()}')
            
            w.recipients.update(name=created.name, comment=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.recipients.delete(name=created.name)

        Update a share recipient.
        
        Updates an existing recipient in the metastore. The caller must be a metastore admin or the owner of
        the recipient. If the recipient name will be updated, the user must be both a metastore admin and the
        owner of the recipient.
        
        :param name: str
          Name of the recipient.
        :param comment: str (optional)
          Description about the recipient.
        :param expiration_time: int (optional)
          Expiration timestamp of the token, in epoch milliseconds.
        :param ip_access_list: :class:`IpAccessList` (optional)
          IP Access List
        :param new_name: str (optional)
          New name for the recipient.
        :param owner: str (optional)
          Username of the recipient owner.
        :param properties_kvpairs: :class:`SecurablePropertiesKvPairs` (optional)
          Recipient properties as map of string key-value pairs. When provided in update request, the
          specified properties will override the existing properties. To add and remove properties, one would
          need to perform a read-modify-write.
        
        
        
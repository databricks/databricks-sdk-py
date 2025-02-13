``a.storage_credentials``: Account Storage Credentials
======================================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: AccountStorageCredentialsAPI

    These APIs manage storage credentials for a particular metastore.

    .. py:method:: create(metastore_id: str [, credential_info: Optional[CreateStorageCredential]]) -> AccountsStorageCredentialInfo

        Create a storage credential.
        
        Creates a new storage credential. The request object is specific to the cloud:
        
        * **AwsIamRole** for AWS credentials * **AzureServicePrincipal** for Azure credentials *
        **GcpServiceAcountKey** for GCP credentials.
        
        The caller must be a metastore admin and have the **CREATE_STORAGE_CREDENTIAL** privilege on the
        metastore.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param credential_info: :class:`CreateStorageCredential` (optional)
        
        :returns: :class:`AccountsStorageCredentialInfo`
        

    .. py:method:: delete(metastore_id: str, storage_credential_name: str [, force: Optional[bool]])

        Delete a storage credential.
        
        Deletes a storage credential from the metastore. The caller must be an owner of the storage
        credential.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param storage_credential_name: str
          Name of the storage credential.
        :param force: bool (optional)
          Force deletion even if the Storage Credential is not empty. Default is false.
        
        
        

    .. py:method:: get(metastore_id: str, storage_credential_name: str) -> AccountsStorageCredentialInfo

        Gets the named storage credential.
        
        Gets a storage credential from the metastore. The caller must be a metastore admin, the owner of the
        storage credential, or have a level of privilege on the storage credential.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param storage_credential_name: str
          Name of the storage credential.
        
        :returns: :class:`AccountsStorageCredentialInfo`
        

    .. py:method:: list(metastore_id: str) -> Iterator[StorageCredentialInfo]

        Get all storage credentials assigned to a metastore.
        
        Gets a list of all storage credentials that have been assigned to given metastore.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        
        :returns: Iterator over :class:`StorageCredentialInfo`
        

    .. py:method:: update(metastore_id: str, storage_credential_name: str [, credential_info: Optional[UpdateStorageCredential]]) -> AccountsStorageCredentialInfo

        Updates a storage credential.
        
        Updates a storage credential on the metastore. The caller must be the owner of the storage credential.
        If the caller is a metastore admin, only the __owner__ credential can be changed.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param storage_credential_name: str
          Name of the storage credential.
        :param credential_info: :class:`UpdateStorageCredential` (optional)
        
        :returns: :class:`AccountsStorageCredentialInfo`
        
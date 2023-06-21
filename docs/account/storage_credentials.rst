Account Storage Credentials
===========================
.. py:class:: AccountStorageCredentialsAPI

    These APIs manage storage credentials for a particular metastore.

    .. py:method:: create(metastore_id [, credential_info])

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            created = w.storage_credentials.create(
                name=f'sdk-{time.time_ns()}',
                aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]))
            
            # cleanup
            w.storage_credentials.delete(delete=created.name)

        Create a storage credential.
        
        Creates a new storage credential. The request object is specific to the cloud:
        
        * **AwsIamRole** for AWS credentials * **AzureServicePrincipal** for Azure credentials *
        **GcpServiceAcountKey** for GCP credentials.
        
        The caller must be a metastore admin and have the **CREATE_STORAGE_CREDENTIAL** privilege on the
        metastore.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param credential_info: :class:`CreateStorageCredential` (optional)
        
        :returns: :class:`StorageCredentialInfo`
        

    .. py:method:: delete(metastore_id, name)

        Delete a storage credential.
        
        Deletes a storage credential from the metastore. The caller must be an owner of the storage
        credential.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param name: str
          Name of the storage credential.
        
        
        

    .. py:method:: get(metastore_id, name)

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            created = w.storage_credentials.create(
                name=f'sdk-{time.time_ns()}',
                aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]))
            
            by_name = w.storage_credentials.get(get=created.name)
            
            # cleanup
            w.storage_credentials.delete(delete=created.name)

        Gets the named storage credential.
        
        Gets a storage credential from the metastore. The caller must be a metastore admin, the owner of the
        storage credential, or have a level of privilege on the storage credential.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param name: str
          Name of the storage credential.
        
        :returns: :class:`StorageCredentialInfo`
        

    .. py:method:: list(metastore_id)

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.storage_credentials.list()

        Get all storage credentials assigned to a metastore.
        
        Gets a list of all storage credentials that have been assigned to given metastore.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        
        :returns: :class:`ListStorageCredentialsResponse`
        

    .. py:method:: update(metastore_id, name [, credential_info])

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            created = w.storage_credentials.create(
                name=f'sdk-{time.time_ns()}',
                aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]))
            
            _ = w.storage_credentials.update(
                name=created.name,
                comment=f'sdk-{time.time_ns()}',
                aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]))
            
            # cleanup
            w.storage_credentials.delete(delete=created.name)

        Updates a storage credential.
        
        Updates a storage credential on the metastore. The caller must be the owner of the storage credential.
        If the caller is a metastore admin, only the __owner__ credential can be changed.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param name: str
          Name of the storage credential.
        :param credential_info: :class:`UpdateStorageCredential` (optional)
        
        :returns: :class:`StorageCredentialInfo`
        
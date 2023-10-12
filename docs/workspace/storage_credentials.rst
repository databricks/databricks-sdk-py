Storage Credentials
===================
.. py:class:: StorageCredentialsAPI

    A storage credential represents an authentication and authorization mechanism for accessing data stored on
    your cloud tenant. Each storage credential is subject to Unity Catalog access-control policies that
    control which users and groups can access the credential. If a user does not have access to a storage
    credential in Unity Catalog, the request fails and Unity Catalog does not attempt to authenticate to your
    cloud tenant on the user’s behalf.
    
    Databricks recommends using external locations rather than using storage credentials directly.
    
    To create storage credentials, you must be a Databricks account admin. The account admin who creates the
    storage credential can delegate ownership to another user or group to manage permissions on it.

    .. py:method:: create(name [, aws_iam_role, azure_managed_identity, azure_service_principal, comment, databricks_gcp_service_account, read_only, skip_validation])

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
        
        Creates a new storage credential.
        
        :param name: str
          The credential name. The name must be unique within the metastore.
        :param aws_iam_role: :class:`AwsIamRole` (optional)
          The AWS IAM role configuration.
        :param azure_managed_identity: :class:`AzureManagedIdentity` (optional)
          The Azure managed identity configuration.
        :param azure_service_principal: :class:`AzureServicePrincipal` (optional)
          The Azure service principal configuration.
        :param comment: str (optional)
          Comment associated with the credential.
        :param databricks_gcp_service_account: Any (optional)
          The <Databricks> managed GCP service account configuration.
        :param read_only: bool (optional)
          Whether the storage credential is only usable for read operations.
        :param skip_validation: bool (optional)
          Supplying true to this argument skips validation of the created credential.
        
        :returns: :class:`StorageCredentialInfo`
        

    .. py:method:: delete(name [, force])

        Delete a credential.
        
        Deletes a storage credential from the metastore. The caller must be an owner of the storage
        credential.
        
        :param name: str
          Name of the storage credential.
        :param force: bool (optional)
          Force deletion even if there are dependent external locations or external tables.
        
        
        

    .. py:method:: get(name)

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
            
            by_name = w.storage_credentials.get(name=created.name)
            
            # cleanup
            w.storage_credentials.delete(name=created.name)

        Get a credential.
        
        Gets a storage credential from the metastore. The caller must be a metastore admin, the owner of the
        storage credential, or have some permission on the storage credential.
        
        :param name: str
          Name of the storage credential.
        
        :returns: :class:`StorageCredentialInfo`
        

    .. py:method:: list()

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.storage_credentials.list()

        List credentials.
        
        Gets an array of storage credentials (as __StorageCredentialInfo__ objects). The array is limited to
        only those storage credentials the caller has permission to access. If the caller is a metastore
        admin, all storage credentials will be retrieved. There is no guarantee of a specific ordering of the
        elements in the array.
        
        :returns: Iterator over :class:`StorageCredentialInfo`
        

    .. py:method:: update(name [, aws_iam_role, azure_managed_identity, azure_service_principal, comment, databricks_gcp_service_account, force, owner, read_only, skip_validation])

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

        Update a credential.
        
        Updates a storage credential on the metastore.
        
        :param name: str
          The credential name. The name must be unique within the metastore.
        :param aws_iam_role: :class:`AwsIamRole` (optional)
          The AWS IAM role configuration.
        :param azure_managed_identity: :class:`AzureManagedIdentity` (optional)
          The Azure managed identity configuration.
        :param azure_service_principal: :class:`AzureServicePrincipal` (optional)
          The Azure service principal configuration.
        :param comment: str (optional)
          Comment associated with the credential.
        :param databricks_gcp_service_account: Any (optional)
          The <Databricks> managed GCP service account configuration.
        :param force: bool (optional)
          Force update even if there are dependent external locations or external tables.
        :param owner: str (optional)
          Username of current owner of credential.
        :param read_only: bool (optional)
          Whether the storage credential is only usable for read operations.
        :param skip_validation: bool (optional)
          Supplying true to this argument skips validation of the updated credential.
        
        :returns: :class:`StorageCredentialInfo`
        

    .. py:method:: validate( [, aws_iam_role, azure_managed_identity, azure_service_principal, databricks_gcp_service_account, external_location_name, read_only, storage_credential_name, url])

        Validate a storage credential.
        
        Validates a storage credential. At least one of __external_location_name__ and __url__ need to be
        provided. If only one of them is provided, it will be used for validation. And if both are provided,
        the __url__ will be used for validation, and __external_location_name__ will be ignored when checking
        overlapping urls.
        
        Either the __storage_credential_name__ or the cloud-specific credential must be provided.
        
        The caller must be a metastore admin or the storage credential owner or have the
        **CREATE_EXTERNAL_LOCATION** privilege on the metastore and the storage credential.
        
        :param aws_iam_role: :class:`AwsIamRole` (optional)
          The AWS IAM role configuration.
        :param azure_managed_identity: :class:`AzureManagedIdentity` (optional)
          The Azure managed identity configuration.
        :param azure_service_principal: :class:`AzureServicePrincipal` (optional)
          The Azure service principal configuration.
        :param databricks_gcp_service_account: Any (optional)
          The Databricks created GCP service account configuration.
        :param external_location_name: str (optional)
          The name of an existing external location to validate.
        :param read_only: bool (optional)
          Whether the storage credential is only usable for read operations.
        :param storage_credential_name: Any (optional)
          The name of the storage credential to validate.
        :param url: str (optional)
          The external location url to validate.
        
        :returns: :class:`ValidateStorageCredentialResponse`
        
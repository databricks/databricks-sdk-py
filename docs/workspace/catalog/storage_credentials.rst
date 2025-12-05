``w.storage_credentials``: Storage Credentials
==============================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: StorageCredentialsAPI

    A storage credential represents an authentication and authorization mechanism for accessing data stored on
    your cloud tenant. Each storage credential is subject to Unity Catalog access-control policies that
    control which users and groups can access the credential. If a user does not have access to a storage
    credential in Unity Catalog, the request fails and Unity Catalog does not attempt to authenticate to your
    cloud tenant on the user’s behalf.

    Databricks recommends using external locations rather than using storage credentials directly.

    To create storage credentials, you must be a Databricks account admin. The account admin who creates the
    storage credential can delegate ownership to another user or group to manage permissions on it.

    .. py:method:: create(name: str [, aws_iam_role: Optional[AwsIamRoleRequest], azure_managed_identity: Optional[AzureManagedIdentityRequest], azure_service_principal: Optional[AzureServicePrincipal], cloudflare_api_token: Optional[CloudflareApiToken], comment: Optional[str], databricks_gcp_service_account: Optional[DatabricksGcpServiceAccountRequest], read_only: Optional[bool], skip_validation: Optional[bool]]) -> StorageCredentialInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            created = w.storage_credentials.create(
                name=f"sdk-{time.time_ns()}",
                aws_iam_role=catalog.AwsIamRoleRequest(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
            )
            
            # cleanup
            w.storage_credentials.delete(name=created.name)

        Creates a new storage credential.

        The caller must be a metastore admin or have the **CREATE_STORAGE_CREDENTIAL** privilege on the
        metastore.

        :param name: str
          The credential name. The name must be unique among storage and service credentials within the
          metastore.
        :param aws_iam_role: :class:`AwsIamRoleRequest` (optional)
          The AWS IAM role configuration.
        :param azure_managed_identity: :class:`AzureManagedIdentityRequest` (optional)
          The Azure managed identity configuration.
        :param azure_service_principal: :class:`AzureServicePrincipal` (optional)
          The Azure service principal configuration.
        :param cloudflare_api_token: :class:`CloudflareApiToken` (optional)
          The Cloudflare API token configuration.
        :param comment: str (optional)
          Comment associated with the credential.
        :param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccountRequest` (optional)
          The Databricks managed GCP service account configuration.
        :param read_only: bool (optional)
          Whether the credential is usable only for read operations. Only applicable when purpose is
          **STORAGE**.
        :param skip_validation: bool (optional)
          Supplying true to this argument skips validation of the created credential.

        :returns: :class:`StorageCredentialInfo`
        

    .. py:method:: delete(name: str [, force: Optional[bool]])

        Deletes a storage credential from the metastore. The caller must be an owner of the storage
        credential.

        :param name: str
          Name of the storage credential.
        :param force: bool (optional)
          Force an update even if there are dependent external locations or external tables (when purpose is
          **STORAGE**) or dependent services (when purpose is **SERVICE**).


        

    .. py:method:: get(name: str) -> StorageCredentialInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            created = w.storage_credentials.create(
                name=f"sdk-{time.time_ns()}",
                aws_iam_role=catalog.AwsIamRoleRequest(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
            )
            
            by_name = w.storage_credentials.get(name=created.name)
            
            # cleanup
            w.storage_credentials.delete(name=created.name)

        Gets a storage credential from the metastore. The caller must be a metastore admin, the owner of the
        storage credential, or have some permission on the storage credential.

        :param name: str
          Name of the storage credential.

        :returns: :class:`StorageCredentialInfo`
        

    .. py:method:: list( [, include_unbound: Optional[bool], max_results: Optional[int], page_token: Optional[str]]) -> Iterator[StorageCredentialInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.storage_credentials.list()

        Gets an array of storage credentials (as __StorageCredentialInfo__ objects). The array is limited to
        only those storage credentials the caller has permission to access. If the caller is a metastore
        admin, retrieval of credentials is unrestricted. There is no guarantee of a specific ordering of the
        elements in the array.

        NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls
        will be deprecated soon.

        PAGINATION BEHAVIOR: When using pagination (max_results >= 0), a page may contain zero results while
        still providing a next_page_token. Clients must continue reading pages until next_page_token is
        absent, which is the only indication that the end of results has been reached.

        :param include_unbound: bool (optional)
          Whether to include credentials not bound to the workspace. Effective only if the user has permission
          to update the credential–workspace binding.
        :param max_results: int (optional)
          Maximum number of storage credentials to return. If not set, all the storage credentials are
          returned (not recommended). - when set to a value greater than 0, the page length is the minimum of
          this value and a server configured value; - when set to 0, the page length is set to a server
          configured value (recommended); - when set to a value less than 0, an invalid parameter error is
          returned;
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.

        :returns: Iterator over :class:`StorageCredentialInfo`
        

    .. py:method:: update(name: str [, aws_iam_role: Optional[AwsIamRoleRequest], azure_managed_identity: Optional[AzureManagedIdentityResponse], azure_service_principal: Optional[AzureServicePrincipal], cloudflare_api_token: Optional[CloudflareApiToken], comment: Optional[str], databricks_gcp_service_account: Optional[DatabricksGcpServiceAccountRequest], force: Optional[bool], isolation_mode: Optional[IsolationMode], new_name: Optional[str], owner: Optional[str], read_only: Optional[bool], skip_validation: Optional[bool]]) -> StorageCredentialInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            created = w.storage_credentials.create(
                name=f"sdk-{time.time_ns()}",
                aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
            )
            
            _ = w.storage_credentials.update(
                name=created.name,
                comment=f"sdk-{time.time_ns()}",
                aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
            )
            
            # cleanup
            w.storage_credentials.delete(delete=created.name)

        Updates a storage credential on the metastore.

        The caller must be the owner of the storage credential or a metastore admin. If the caller is a
        metastore admin, only the **owner** field can be changed.

        :param name: str
          Name of the storage credential.
        :param aws_iam_role: :class:`AwsIamRoleRequest` (optional)
          The AWS IAM role configuration.
        :param azure_managed_identity: :class:`AzureManagedIdentityResponse` (optional)
          The Azure managed identity configuration.
        :param azure_service_principal: :class:`AzureServicePrincipal` (optional)
          The Azure service principal configuration.
        :param cloudflare_api_token: :class:`CloudflareApiToken` (optional)
          The Cloudflare API token configuration.
        :param comment: str (optional)
          Comment associated with the credential.
        :param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccountRequest` (optional)
          The Databricks managed GCP service account configuration.
        :param force: bool (optional)
          Force update even if there are dependent external locations or external tables.
        :param isolation_mode: :class:`IsolationMode` (optional)
          Whether the current securable is accessible from all workspaces or a specific set of workspaces.
        :param new_name: str (optional)
          New name for the storage credential.
        :param owner: str (optional)
          Username of current owner of credential.
        :param read_only: bool (optional)
          Whether the credential is usable only for read operations. Only applicable when purpose is
          **STORAGE**.
        :param skip_validation: bool (optional)
          Supplying true to this argument skips validation of the updated credential.

        :returns: :class:`StorageCredentialInfo`
        

    .. py:method:: validate( [, aws_iam_role: Optional[AwsIamRoleRequest], azure_managed_identity: Optional[AzureManagedIdentityRequest], azure_service_principal: Optional[AzureServicePrincipal], cloudflare_api_token: Optional[CloudflareApiToken], databricks_gcp_service_account: Optional[DatabricksGcpServiceAccountRequest], external_location_name: Optional[str], read_only: Optional[bool], storage_credential_name: Optional[str], url: Optional[str]]) -> ValidateStorageCredentialResponse

        Validates a storage credential. At least one of __external_location_name__ and __url__ need to be
        provided. If only one of them is provided, it will be used for validation. And if both are provided,
        the __url__ will be used for validation, and __external_location_name__ will be ignored when checking
        overlapping urls.

        Either the __storage_credential_name__ or the cloud-specific credential must be provided.

        The caller must be a metastore admin or the storage credential owner or have the
        **CREATE_EXTERNAL_LOCATION** privilege on the metastore and the storage credential.

        :param aws_iam_role: :class:`AwsIamRoleRequest` (optional)
          The AWS IAM role configuration.
        :param azure_managed_identity: :class:`AzureManagedIdentityRequest` (optional)
          The Azure managed identity configuration.
        :param azure_service_principal: :class:`AzureServicePrincipal` (optional)
          The Azure service principal configuration.
        :param cloudflare_api_token: :class:`CloudflareApiToken` (optional)
          The Cloudflare API token configuration.
        :param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccountRequest` (optional)
          The Databricks created GCP service account configuration.
        :param external_location_name: str (optional)
          The name of an existing external location to validate.
        :param read_only: bool (optional)
          Whether the storage credential is only usable for read operations.
        :param storage_credential_name: str (optional)
          Required. The name of an existing credential or long-lived cloud credential to validate.
        :param url: str (optional)
          The external location url to validate.

        :returns: :class:`ValidateStorageCredentialResponse`
        
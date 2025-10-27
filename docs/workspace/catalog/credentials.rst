``w.credentials``: Credentials
==============================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: CredentialsAPI

    A credential represents an authentication and authorization mechanism for accessing services on your cloud
    tenant. Each credential is subject to Unity Catalog access-control policies that control which users and
    groups can access the credential.

    To create credentials, you must be a Databricks account admin or have the `CREATE SERVICE CREDENTIAL`
    privilege. The user who creates the credential can delegate ownership to another user or group to manage
    permissions on it.

    .. py:method:: create_credential(name: str [, aws_iam_role: Optional[AwsIamRole], azure_managed_identity: Optional[AzureManagedIdentity], azure_service_principal: Optional[AzureServicePrincipal], comment: Optional[str], databricks_gcp_service_account: Optional[DatabricksGcpServiceAccount], purpose: Optional[CredentialPurpose], read_only: Optional[bool], skip_validation: Optional[bool]]) -> CredentialInfo

        Creates a new credential. The type of credential to be created is determined by the **purpose** field,
        which should be either **SERVICE** or **STORAGE**.

        The caller must be a metastore admin or have the metastore privilege **CREATE_STORAGE_CREDENTIAL** for
        storage credentials, or **CREATE_SERVICE_CREDENTIAL** for service credentials.

        :param name: str
          The credential name. The name must be unique among storage and service credentials within the
          metastore.
        :param aws_iam_role: :class:`AwsIamRole` (optional)
          The AWS IAM role configuration.
        :param azure_managed_identity: :class:`AzureManagedIdentity` (optional)
          The Azure managed identity configuration.
        :param azure_service_principal: :class:`AzureServicePrincipal` (optional)
          The Azure service principal configuration.
        :param comment: str (optional)
          Comment associated with the credential.
        :param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccount` (optional)
          The Databricks managed GCP service account configuration.
        :param purpose: :class:`CredentialPurpose` (optional)
          Indicates the purpose of the credential.
        :param read_only: bool (optional)
          Whether the credential is usable only for read operations. Only applicable when purpose is
          **STORAGE**.
        :param skip_validation: bool (optional)
          Optional. Supplying true to this argument skips validation of the created set of credentials.

        :returns: :class:`CredentialInfo`
        

    .. py:method:: delete_credential(name_arg: str [, force: Optional[bool]])

        Deletes a service or storage credential from the metastore. The caller must be an owner of the
        credential.

        :param name_arg: str
          Name of the credential.
        :param force: bool (optional)
          Force an update even if there are dependent services (when purpose is **SERVICE**) or dependent
          external locations and external tables (when purpose is **STORAGE**).


        

    .. py:method:: generate_temporary_service_credential(credential_name: str [, azure_options: Optional[GenerateTemporaryServiceCredentialAzureOptions], gcp_options: Optional[GenerateTemporaryServiceCredentialGcpOptions]]) -> TemporaryCredentials

        Returns a set of temporary credentials generated using the specified service credential. The caller
        must be a metastore admin or have the metastore privilege **ACCESS** on the service credential.

        :param credential_name: str
          The name of the service credential used to generate a temporary credential
        :param azure_options: :class:`GenerateTemporaryServiceCredentialAzureOptions` (optional)
        :param gcp_options: :class:`GenerateTemporaryServiceCredentialGcpOptions` (optional)

        :returns: :class:`TemporaryCredentials`
        

    .. py:method:: get_credential(name_arg: str) -> CredentialInfo

        Gets a service or storage credential from the metastore. The caller must be a metastore admin, the
        owner of the credential, or have any permission on the credential.

        :param name_arg: str
          Name of the credential.

        :returns: :class:`CredentialInfo`
        

    .. py:method:: list_credentials( [, include_unbound: Optional[bool], max_results: Optional[int], page_token: Optional[str], purpose: Optional[CredentialPurpose]]) -> Iterator[CredentialInfo]

        Gets an array of credentials (as __CredentialInfo__ objects).

        The array is limited to only the credentials that the caller has permission to access. If the caller
        is a metastore admin, retrieval of credentials is unrestricted. There is no guarantee of a specific
        ordering of the elements in the array.

        :param include_unbound: bool (optional)
          Whether to include credentials not bound to the workspace. Effective only if the user has permission
          to update the credential–workspace binding.
        :param max_results: int (optional)
          Maximum number of credentials to return. - If not set, the default max page size is used. - When set
          to a value greater than 0, the page length is the minimum of this value and a server-configured
          value. - When set to 0, the page length is set to a server-configured value (recommended). - When
          set to a value less than 0, an invalid parameter error is returned.
        :param page_token: str (optional)
          Opaque token to retrieve the next page of results.
        :param purpose: :class:`CredentialPurpose` (optional)
          Return only credentials for the specified purpose.

        :returns: Iterator over :class:`CredentialInfo`
        

    .. py:method:: update_credential(name_arg: str [, aws_iam_role: Optional[AwsIamRole], azure_managed_identity: Optional[AzureManagedIdentity], azure_service_principal: Optional[AzureServicePrincipal], comment: Optional[str], databricks_gcp_service_account: Optional[DatabricksGcpServiceAccount], force: Optional[bool], isolation_mode: Optional[IsolationMode], new_name: Optional[str], owner: Optional[str], read_only: Optional[bool], skip_validation: Optional[bool]]) -> CredentialInfo

        Updates a service or storage credential on the metastore.

        The caller must be the owner of the credential or a metastore admin or have the `MANAGE` permission.
        If the caller is a metastore admin, only the __owner__ field can be changed.

        :param name_arg: str
          Name of the credential.
        :param aws_iam_role: :class:`AwsIamRole` (optional)
          The AWS IAM role configuration.
        :param azure_managed_identity: :class:`AzureManagedIdentity` (optional)
          The Azure managed identity configuration.
        :param azure_service_principal: :class:`AzureServicePrincipal` (optional)
          The Azure service principal configuration.
        :param comment: str (optional)
          Comment associated with the credential.
        :param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccount` (optional)
          The Databricks managed GCP service account configuration.
        :param force: bool (optional)
          Force an update even if there are dependent services (when purpose is **SERVICE**) or dependent
          external locations and external tables (when purpose is **STORAGE**).
        :param isolation_mode: :class:`IsolationMode` (optional)
          Whether the current securable is accessible from all workspaces or a specific set of workspaces.
        :param new_name: str (optional)
          New name of credential.
        :param owner: str (optional)
          Username of current owner of credential.
        :param read_only: bool (optional)
          Whether the credential is usable only for read operations. Only applicable when purpose is
          **STORAGE**.
        :param skip_validation: bool (optional)
          Supply true to this argument to skip validation of the updated credential.

        :returns: :class:`CredentialInfo`
        

    .. py:method:: validate_credential( [, aws_iam_role: Optional[AwsIamRole], azure_managed_identity: Optional[AzureManagedIdentity], credential_name: Optional[str], databricks_gcp_service_account: Optional[DatabricksGcpServiceAccount], external_location_name: Optional[str], purpose: Optional[CredentialPurpose], read_only: Optional[bool], url: Optional[str]]) -> ValidateCredentialResponse

        Validates a credential.

        For service credentials (purpose is **SERVICE**), either the __credential_name__ or the cloud-specific
        credential must be provided.

        For storage credentials (purpose is **STORAGE**), at least one of __external_location_name__ and
        __url__ need to be provided. If only one of them is provided, it will be used for validation. And if
        both are provided, the __url__ will be used for validation, and __external_location_name__ will be
        ignored when checking overlapping urls. Either the __credential_name__ or the cloud-specific
        credential must be provided.

        The caller must be a metastore admin or the credential owner or have the required permission on the
        metastore and the credential (e.g., **CREATE_EXTERNAL_LOCATION** when purpose is **STORAGE**).

        :param aws_iam_role: :class:`AwsIamRole` (optional)
        :param azure_managed_identity: :class:`AzureManagedIdentity` (optional)
        :param credential_name: str (optional)
          Required. The name of an existing credential or long-lived cloud credential to validate.
        :param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccount` (optional)
        :param external_location_name: str (optional)
          The name of an existing external location to validate. Only applicable for storage credentials
          (purpose is **STORAGE**.)
        :param purpose: :class:`CredentialPurpose` (optional)
          The purpose of the credential. This should only be used when the credential is specified.
        :param read_only: bool (optional)
          Whether the credential is only usable for read operations. Only applicable for storage credentials
          (purpose is **STORAGE**.)
        :param url: str (optional)
          The external location url to validate. Only applicable when purpose is **STORAGE**.

        :returns: :class:`ValidateCredentialResponse`
        
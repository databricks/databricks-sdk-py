``a.encryption_keys``: Key configurations
=========================================
.. currentmodule:: databricks.sdk.service.provisioning

.. py:class:: EncryptionKeysAPI

    These APIs manage encryption key configurations for this workspace (optional). A key configuration
    encapsulates the AWS KMS key information and some information about how the key configuration can be used.
    There are two possible uses for key configurations:

    * Managed services: A key configuration can be used to encrypt a workspace's notebook and secret data in
    the control plane, as well as Databricks SQL queries and query history. * Storage: A key configuration can
    be used to encrypt a workspace's DBFS and EBS data in the data plane.

    In both of these cases, the key configuration's ID is used when creating a new workspace. This Preview
    feature is available if your account is on the E2 version of the platform. Updating a running workspace
    with workspace storage encryption requires that the workspace is on the E2 version of the platform. If you
    have an older workspace, it might not be on the E2 version of the platform. If you are not sure, contact
    your Databricks representative.

    .. py:method:: create(use_cases: List[KeyUseCase] [, aws_key_info: Optional[CreateAwsKeyInfo], gcp_key_info: Optional[CreateGcpKeyInfo]]) -> CustomerManagedKey


        Usage:

        .. code-block::

            import os
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import provisioning
            
            a = AccountClient()
            
            created = a.encryption_keys.create(
                aws_key_info=provisioning.CreateAwsKeyInfo(
                    key_arn=os.environ["TEST_MANAGED_KMS_KEY_ARN"],
                    key_alias=os.environ["TEST_STORAGE_KMS_KEY_ALIAS"],
                ),
                use_cases=[provisioning.KeyUseCase.MANAGED_SERVICES],
            )
            
            # cleanup
            a.encryption_keys.delete(customer_managed_key_id=created.customer_managed_key_id)

        Creates a customer-managed key configuration object for an account, specified by ID. This operation
        uploads a reference to a customer-managed key to Databricks. If the key is assigned as a workspace's
        customer-managed key for managed services, Databricks uses the key to encrypt the workspaces notebooks
        and secrets in the control plane, in addition to Databricks SQL queries and query history. If it is
        specified as a workspace's customer-managed key for workspace storage, the key encrypts the
        workspace's root S3 bucket (which contains the workspace's root DBFS and system data) and, optionally,
        cluster EBS volume data.

        **Important**: Customer-managed keys are supported only for some deployment types, subscription types,
        and AWS regions that currently support creation of Databricks workspaces.

        This operation is available only if your account is on the E2 version of the platform or on a select
        custom plan that allows multiple workspaces per account.

        :param use_cases: List[:class:`KeyUseCase`]
          The cases that the key can be used for.
        :param aws_key_info: :class:`CreateAwsKeyInfo` (optional)
        :param gcp_key_info: :class:`CreateGcpKeyInfo` (optional)

        :returns: :class:`CustomerManagedKey`
        

    .. py:method:: delete(customer_managed_key_id: str)

        Deletes a customer-managed key configuration object for an account. You cannot delete a configuration
        that is associated with a running workspace.

        :param customer_managed_key_id: str
          Databricks encryption key configuration ID.


        

    .. py:method:: get(customer_managed_key_id: str) -> CustomerManagedKey


        Usage:

        .. code-block::

            import os
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import provisioning
            
            a = AccountClient()
            
            created = a.encryption_keys.create(
                aws_key_info=provisioning.CreateAwsKeyInfo(
                    key_arn=os.environ["TEST_MANAGED_KMS_KEY_ARN"],
                    key_alias=os.environ["TEST_STORAGE_KMS_KEY_ALIAS"],
                ),
                use_cases=[provisioning.KeyUseCase.MANAGED_SERVICES],
            )
            
            by_id = a.encryption_keys.get(customer_managed_key_id=created.customer_managed_key_id)
            
            # cleanup
            a.encryption_keys.delete(customer_managed_key_id=created.customer_managed_key_id)

        Gets a customer-managed key configuration object for an account, specified by ID. This operation
        uploads a reference to a customer-managed key to Databricks. If assigned as a workspace's
        customer-managed key for managed services, Databricks uses the key to encrypt the workspaces notebooks
        and secrets in the control plane, in addition to Databricks SQL queries and query history. If it is
        specified as a workspace's customer-managed key for storage, the key encrypts the workspace's root S3
        bucket (which contains the workspace's root DBFS and system data) and, optionally, cluster EBS volume
        data.

        **Important**: Customer-managed keys are supported only for some deployment types, subscription types,
        and AWS regions.

        This operation is available only if your account is on the E2 version of the platform.",

        :param customer_managed_key_id: str
          Databricks encryption key configuration ID.

        :returns: :class:`CustomerManagedKey`
        

    .. py:method:: list() -> Iterator[CustomerManagedKey]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            all = a.encryption_keys.list()

        Gets all customer-managed key configuration objects for an account. If the key is specified as a
        workspace's managed services customer-managed key, Databricks uses the key to encrypt the workspace's
        notebooks and secrets in the control plane, in addition to Databricks SQL queries and query history.
        If the key is specified as a workspace's storage customer-managed key, the key is used to encrypt the
        workspace's root S3 bucket and optionally can encrypt cluster EBS volumes data in the data plane.

        **Important**: Customer-managed keys are supported only for some deployment types, subscription types,
        and AWS regions.

        This operation is available only if your account is on the E2 version of the platform.


        :returns: Iterator over :class:`CustomerManagedKey`
        
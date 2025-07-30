``a.credentials``: Credential configurations
============================================
.. currentmodule:: databricks.sdk.service.provisioning

.. py:class:: CredentialsAPI

    These APIs manage credential configurations for this workspace. Databricks needs access to a cross-account
    service IAM role in your AWS account so that Databricks can deploy clusters in the appropriate VPC for the
    new workspace. A credential configuration encapsulates this role information, and its ID is used when
    creating a new workspace.

    .. py:method:: create(credentials_name: str, aws_credentials: CreateCredentialAwsCredentials) -> Credential


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import provisioning
            
            a = AccountClient()
            
            role = a.credentials.create(
                credentials_name=f"sdk-{time.time_ns()}",
                aws_credentials=provisioning.CreateCredentialAwsCredentials(
                    sts_role=provisioning.CreateCredentialStsRole(role_arn=os.environ["TEST_CROSSACCOUNT_ARN"])
                ),
            )
            
            # cleanup
            a.credentials.delete(credentials_id=role.credentials_id)

        Creates a Databricks credential configuration that represents cloud cross-account credentials for a
        specified account. Databricks uses this to set up network infrastructure properly to host Databricks
        clusters. For your AWS IAM role, you need to trust the External ID (the Databricks Account API account
        ID) in the returned credential object, and configure the required access policy.

        Save the response's `credentials_id` field, which is the ID for your new credential configuration
        object.

        For information about how to create a new workspace with this API, see [Create a new workspace using
        the Account API]

        [Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html

        :param credentials_name: str
          The human-readable name of the credential configuration object.
        :param aws_credentials: :class:`CreateCredentialAwsCredentials`

        :returns: :class:`Credential`
        

    .. py:method:: delete(credentials_id: str)

        Deletes a Databricks credential configuration object for an account, both specified by ID. You cannot
        delete a credential that is associated with any workspace.

        :param credentials_id: str
          Databricks Account API credential configuration ID


        

    .. py:method:: get(credentials_id: str) -> Credential


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import provisioning
            
            a = AccountClient()
            
            role = a.credentials.create(
                credentials_name=f"sdk-{time.time_ns()}",
                aws_credentials=provisioning.CreateCredentialAwsCredentials(
                    sts_role=provisioning.CreateCredentialStsRole(role_arn=os.environ["TEST_CROSSACCOUNT_ARN"])
                ),
            )
            
            by_id = a.credentials.get(credentials_id=role.credentials_id)
            
            # cleanup
            a.credentials.delete(credentials_id=role.credentials_id)

        Gets a Databricks credential configuration object for an account, both specified by ID.

        :param credentials_id: str
          Databricks Account API credential configuration ID

        :returns: :class:`Credential`
        

    .. py:method:: list() -> Iterator[Credential]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            configs = a.credentials.list()

        Gets all Databricks credential configurations associated with an account specified by ID.


        :returns: Iterator over :class:`Credential`
        
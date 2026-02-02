``w.git_credentials``: Git Credentials
======================================
.. currentmodule:: databricks.sdk.service.workspace

.. py:class:: GitCredentialsAPI

    Registers personal access token for Databricks to do operations on behalf of the user.

    See [more info].

    [more info]: https://docs.databricks.com/repos/get-access-tokens-from-git-provider.html

    .. py:method:: create(git_provider: str [, git_email: Optional[str], git_username: Optional[str], is_default_for_provider: Optional[bool], name: Optional[str], personal_access_token: Optional[str], principal_id: Optional[int]]) -> CreateCredentialsResponse


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            cr = w.git_credentials.create(git_provider="gitHub", git_username="test", personal_access_token="test")
            
            # cleanup
            w.git_credentials.delete(credential_id=cr.credential_id)

        Creates a Git credential entry for the user. Only one Git credential per user is supported, so any
        attempts to create credentials if an entry already exists will fail. Use the PATCH endpoint to update
        existing credentials, or the DELETE endpoint to delete existing credentials.

        :param git_provider: str
          Git provider. This field is case-insensitive. The available Git providers are `gitHub`,
          `bitbucketCloud`, `gitLab`, `azureDevOpsServices`, `gitHubEnterprise`, `bitbucketServer`,
          `gitLabEnterpriseEdition` and `awsCodeCommit`.
        :param git_email: str (optional)
          The authenticating email associated with your Git provider user account. Used for authentication
          with the remote repository and also sets the author & committer identity for commits. Required for
          most Git providers except AWS CodeCommit. Learn more at
          https://docs.databricks.com/aws/en/repos/get-access-tokens-from-git-provider
        :param git_username: str (optional)
          The username provided with your Git provider account and associated with the credential. For most
          Git providers it is only used to set the Git committer & author names for commits, however it may be
          required for authentication depending on your Git provider / token requirements. Required for AWS
          CodeCommit.
        :param is_default_for_provider: bool (optional)
          if the credential is the default for the given provider
        :param name: str (optional)
          the name of the git credential, used for identification and ease of lookup
        :param personal_access_token: str (optional)
          The personal access token used to authenticate to the corresponding Git provider. For certain
          providers, support may exist for other types of scoped access tokens. [Learn more].

          [Learn more]: https://docs.databricks.com/repos/get-access-tokens-from-git-provider.html
        :param principal_id: int (optional)
          The ID of the service principal whose credentials will be modified. Only service principal managers
          can perform this action.

        :returns: :class:`CreateCredentialsResponse`
        

    .. py:method:: delete(credential_id: int [, principal_id: Optional[int]])

        Deletes the specified Git credential.

        :param credential_id: int
          The ID for the corresponding credential to access.
        :param principal_id: int (optional)
          The ID of the service principal whose credentials will be modified. Only service principal managers
          can perform this action.


        

    .. py:method:: get(credential_id: int [, principal_id: Optional[int]]) -> GetCredentialsResponse


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            cr = w.git_credentials.create(git_provider="gitHub", git_username="test", personal_access_token="test")
            
            by_id = w.git_credentials.get(credential_id=cr.credential_id)
            
            # cleanup
            w.git_credentials.delete(credential_id=cr.credential_id)

        Gets the Git credential with the specified credential ID.

        :param credential_id: int
          The ID for the corresponding credential to access.
        :param principal_id: int (optional)
          The ID of the service principal whose credentials will be modified. Only service principal managers
          can perform this action.

        :returns: :class:`GetCredentialsResponse`
        

    .. py:method:: list( [, principal_id: Optional[int]]) -> Iterator[CredentialInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            list = w.git_credentials.list()

        Lists the calling user's Git credentials.

        :param principal_id: int (optional)
          The ID of the service principal whose credentials will be listed. Only service principal managers
          can perform this action.

        :returns: Iterator over :class:`CredentialInfo`
        

    .. py:method:: update(credential_id: int, git_provider: str [, git_email: Optional[str], git_username: Optional[str], is_default_for_provider: Optional[bool], name: Optional[str], personal_access_token: Optional[str], principal_id: Optional[int]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            cr = w.git_credentials.create(git_provider="gitHub", git_username="test", personal_access_token="test")
            
            w.git_credentials.update(
                credential_id=cr.credential_id,
                git_provider="gitHub",
                git_username=f"sdk-{time.time_ns()}@example.com",
                personal_access_token=f"sdk-{time.time_ns()}",
            )
            
            # cleanup
            w.git_credentials.delete(credential_id=cr.credential_id)

        Updates the specified Git credential.

        :param credential_id: int
          The ID for the corresponding credential to access.
        :param git_provider: str
          Git provider. This field is case-insensitive. The available Git providers are `gitHub`,
          `bitbucketCloud`, `gitLab`, `azureDevOpsServices`, `gitHubEnterprise`, `bitbucketServer`,
          `gitLabEnterpriseEdition` and `awsCodeCommit`.
        :param git_email: str (optional)
          The authenticating email associated with your Git provider user account. Used for authentication
          with the remote repository and also sets the author & committer identity for commits. Required for
          most Git providers except AWS CodeCommit. Learn more at
          https://docs.databricks.com/aws/en/repos/get-access-tokens-from-git-provider
        :param git_username: str (optional)
          The username provided with your Git provider account and associated with the credential. For most
          Git providers it is only used to set the Git committer & author names for commits, however it may be
          required for authentication depending on your Git provider / token requirements. Required for AWS
          CodeCommit.
        :param is_default_for_provider: bool (optional)
          if the credential is the default for the given provider
        :param name: str (optional)
          the name of the git credential, used for identification and ease of lookup
        :param personal_access_token: str (optional)
          The personal access token used to authenticate to the corresponding Git provider. For certain
          providers, support may exist for other types of scoped access tokens. [Learn more].

          [Learn more]: https://docs.databricks.com/repos/get-access-tokens-from-git-provider.html
        :param principal_id: int (optional)
          The ID of the service principal whose credentials will be modified. Only service principal managers
          can perform this action.


        
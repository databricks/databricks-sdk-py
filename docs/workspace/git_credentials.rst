Git Credentials
===============
.. py:class:: GitCredentialsAPI

    Registers personal access token for Databricks to do operations on behalf of the user.
    
    See [more info].
    
    [more info]: https://docs.databricks.com/repos/get-access-tokens-from-git-provider.html

    .. py:method:: create(git_provider [, git_username, personal_access_token])

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            cr = w.git_credentials.create(git_provider="gitHub", git_username="test", personal_access_token="test")
            
            # cleanup
            w.git_credentials.delete(credential_id=cr.credential_id)

        Create a credential entry.
        
        Creates a Git credential entry for the user. Only one Git credential per user is supported, so any
        attempts to create credentials if an entry already exists will fail. Use the PATCH endpoint to update
        existing credentials, or the DELETE endpoint to delete existing credentials.
        
        :param git_provider: str
          Git provider. This field is case-insensitive. The available Git providers are gitHub,
          bitbucketCloud, gitLab, azureDevOpsServices, gitHubEnterprise, bitbucketServer,
          gitLabEnterpriseEdition and awsCodeCommit.
        :param git_username: str (optional)
          Git username.
        :param personal_access_token: str (optional)
          The personal access token used to authenticate to the corresponding Git provider.
        
        :returns: :class:`CreateCredentialsResponse`
        

    .. py:method:: delete(credential_id)

        Delete a credential.
        
        Deletes the specified Git credential.
        
        :param credential_id: int
          The ID for the corresponding credential to access.
        
        
        

    .. py:method:: get(credential_id)

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            cr = w.git_credentials.create(git_provider="gitHub", git_username="test", personal_access_token="test")
            
            by_id = w.git_credentials.get(credential_id=cr.credential_id)
            
            # cleanup
            w.git_credentials.delete(credential_id=cr.credential_id)

        Get a credential entry.
        
        Gets the Git credential with the specified credential ID.
        
        :param credential_id: int
          The ID for the corresponding credential to access.
        
        :returns: :class:`CredentialInfo`
        

    .. py:method:: list()

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            list = w.git_credentials.list()

        Get Git credentials.
        
        Lists the calling user's Git credentials. One credential per user is supported.
        
        :returns: Iterator over :class:`CredentialInfo`
        

    .. py:method:: update(credential_id [, git_provider, git_username, personal_access_token])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            cr = w.git_credentials.create(git_provider="gitHub", git_username="test", personal_access_token="test")
            
            w.git_credentials.update(credential_id=cr.credential_id,
                                     git_provider="gitHub",
                                     git_username=f'sdk-{time.time_ns()}@example.com',
                                     personal_access_token=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.git_credentials.delete(credential_id=cr.credential_id)

        Update a credential.
        
        Updates the specified Git credential.
        
        :param credential_id: int
          The ID for the corresponding credential to access.
        :param git_provider: str (optional)
          Git provider. This field is case-insensitive. The available Git providers are gitHub,
          bitbucketCloud, gitLab, azureDevOpsServices, gitHubEnterprise, bitbucketServer,
          gitLabEnterpriseEdition and awsCodeCommit.
        :param git_username: str (optional)
          Git username.
        :param personal_access_token: str (optional)
          The personal access token used to authenticate to the corresponding Git provider.
        
        
        
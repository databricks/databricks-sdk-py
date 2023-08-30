Repos
=====
.. py:class:: ReposAPI

    The Repos API allows users to manage their git repos. Users can use the API to access all repos that they
    have manage permissions on.
    
    Databricks Repos is a visual Git client in Databricks. It supports common Git operations such a cloning a
    repository, committing and pushing, pulling, branch management, and visual comparison of diffs when
    committing.
    
    Within Repos you can develop code in notebooks or other files and follow data science and engineering code
    development best practices using Git for version control, collaboration, and CI/CD.

    .. py:method:: create(url, provider [, path, sparse_checkout])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            root = f'sdk-{time.time_ns()}'
            
            ri = w.repos.create(path=root, url="https://github.com/shreyas-goenka/empty-repo.git", provider="github")
            
            # cleanup
            w.repos.delete(repo_id=ri.id)

        Create a repo.
        
        Creates a repo in the workspace and links it to the remote Git repo specified. Note that repos created
        programmatically must be linked to a remote Git repo, unlike repos created in the browser.
        
        :param url: str
          URL of the Git repository to be linked.
        :param provider: str
          Git provider. This field is case-insensitive. The available Git providers are gitHub,
          bitbucketCloud, gitLab, azureDevOpsServices, gitHubEnterprise, bitbucketServer,
          gitLabEnterpriseEdition and awsCodeCommit.
        :param path: str (optional)
          Desired path for the repo in the workspace. Must be in the format /Repos/{folder}/{repo-name}.
        :param sparse_checkout: :class:`SparseCheckout` (optional)
          If specified, the repo will be created with sparse checkout enabled. You cannot enable/disable
          sparse checkout after the repo is created.
        
        :returns: :class:`RepoInfo`
        

    .. py:method:: delete(repo_id)

        Delete a repo.
        
        Deletes the specified repo.
        
        :param repo_id: int
          The ID for the corresponding repo to access.
        
        
        

    .. py:method:: get(repo_id)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            root = f'sdk-{time.time_ns()}'
            
            ri = w.repos.create(path=root, url="https://github.com/shreyas-goenka/empty-repo.git", provider="github")
            
            by_id = w.repos.get(repo_id=ri.id)
            
            # cleanup
            w.repos.delete(repo_id=ri.id)

        Get a repo.
        
        Returns the repo with the given repo ID.
        
        :param repo_id: int
          The ID for the corresponding repo to access.
        
        :returns: :class:`RepoInfo`
        

    .. py:method:: get_repo_permission_levels(repo_id)

        Get repo permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param repo_id: str
          The repo for which to get or manage permissions.
        
        :returns: :class:`GetRepoPermissionLevelsResponse`
        

    .. py:method:: get_repo_permissions(repo_id)

        Get repo permissions.
        
        Gets the permissions of a repo. Repos can inherit permissions from their root object.
        
        :param repo_id: str
          The repo for which to get or manage permissions.
        
        :returns: :class:`RepoPermissions`
        

    .. py:method:: list( [, next_page_token, path_prefix])

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import workspace
            
            w = WorkspaceClient()
            
            all = w.repos.list()

        Get repos.
        
        Returns repos that the calling user has Manage permissions on. Results are paginated with each page
        containing twenty repos.
        
        :param next_page_token: str (optional)
          Token used to get the next page of results. If not specified, returns the first page of results as
          well as a next page token if there are more results.
        :param path_prefix: str (optional)
          Filters repos that have paths starting with the given path prefix.
        
        :returns: Iterator over :class:`RepoInfo`
        

    .. py:method:: set_repo_permissions(repo_id [, access_control_list])

        Set repo permissions.
        
        Sets permissions on a repo. Repos can inherit permissions from their root object.
        
        :param repo_id: str
          The repo for which to get or manage permissions.
        :param access_control_list: List[:class:`RepoAccessControlRequest`] (optional)
        
        :returns: :class:`RepoPermissions`
        

    .. py:method:: update(repo_id [, branch, sparse_checkout, tag])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            root = f'sdk-{time.time_ns()}'
            
            ri = w.repos.create(path=root, url="https://github.com/shreyas-goenka/empty-repo.git", provider="github")
            
            w.repos.update(repo_id=ri.id, branch="foo")
            
            # cleanup
            w.repos.delete(repo_id=ri.id)

        Update a repo.
        
        Updates the repo to a different branch or tag, or updates the repo to the latest commit on the same
        branch.
        
        :param repo_id: int
          The ID for the corresponding repo to access.
        :param branch: str (optional)
          Branch that the local version of the repo is checked out to.
        :param sparse_checkout: :class:`SparseCheckoutUpdate` (optional)
          If specified, update the sparse checkout settings. The update will fail if sparse checkout is not
          enabled for the repo.
        :param tag: str (optional)
          Tag that the local version of the repo is checked out to. Updating the repo to a tag puts the repo
          in a detached HEAD state. Before committing new changes, you must update the repo to a branch
          instead of the detached HEAD.
        
        
        

    .. py:method:: update_repo_permissions(repo_id [, access_control_list])

        Update repo permissions.
        
        Updates the permissions on a repo. Repos can inherit permissions from their root object.
        
        :param repo_id: str
          The repo for which to get or manage permissions.
        :param access_control_list: List[:class:`RepoAccessControlRequest`] (optional)
        
        :returns: :class:`RepoPermissions`
        

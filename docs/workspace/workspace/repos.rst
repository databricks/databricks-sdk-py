``w.repos``: Repos
==================
.. currentmodule:: databricks.sdk.service.workspace

.. py:class:: ReposAPI

    The Repos API allows users to manage their git repos. Users can use the API to access all repos that they
    have manage permissions on.
    
    Databricks Repos is a visual Git client in Databricks. It supports common Git operations such a cloning a
    repository, committing and pushing, pulling, branch management, and visual comparison of diffs when
    committing.
    
    Within Repos you can develop code in notebooks or other files and follow data science and engineering code
    development best practices using Git for version control, collaboration, and CI/CD.

    .. py:method:: create(url: str, provider: str [, path: Optional[str], sparse_checkout: Optional[SparseCheckout]]) -> CreateRepoResponse


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
          Git provider. This field is case-insensitive. The available Git providers are `gitHub`,
          `bitbucketCloud`, `gitLab`, `azureDevOpsServices`, `gitHubEnterprise`, `bitbucketServer`,
          `gitLabEnterpriseEdition` and `awsCodeCommit`.
        :param path: str (optional)
          Desired path for the repo in the workspace. Almost any path in the workspace can be chosen. If repo
          is created in `/Repos`, path must be in the format `/Repos/{folder}/{repo-name}`.
        :param sparse_checkout: :class:`SparseCheckout` (optional)
          If specified, the repo will be created with sparse checkout enabled. You cannot enable/disable
          sparse checkout after the repo is created.
        
        :returns: :class:`CreateRepoResponse`
        

    .. py:method:: delete(repo_id: int)

        Delete a repo.
        
        Deletes the specified repo.
        
        :param repo_id: int
          ID of the Git folder (repo) object in the workspace.
        
        
        

    .. py:method:: get(repo_id: int) -> GetRepoResponse


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
          ID of the Git folder (repo) object in the workspace.
        
        :returns: :class:`GetRepoResponse`
        

    .. py:method:: get_permission_levels(repo_id: str) -> GetRepoPermissionLevelsResponse

        Get repo permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param repo_id: str
          The repo for which to get or manage permissions.
        
        :returns: :class:`GetRepoPermissionLevelsResponse`
        

    .. py:method:: get_permissions(repo_id: str) -> RepoPermissions

        Get repo permissions.
        
        Gets the permissions of a repo. Repos can inherit permissions from their root object.
        
        :param repo_id: str
          The repo for which to get or manage permissions.
        
        :returns: :class:`RepoPermissions`
        

    .. py:method:: list( [, next_page_token: Optional[str], path_prefix: Optional[str]]) -> Iterator[RepoInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import workspace
            
            w = WorkspaceClient()
            
            all = w.repos.list(workspace.ListReposRequest())

        Get repos.
        
        Returns repos that the calling user has Manage permissions on. Use `next_page_token` to iterate
        through additional pages.
        
        :param next_page_token: str (optional)
          Token used to get the next page of results. If not specified, returns the first page of results as
          well as a next page token if there are more results.
        :param path_prefix: str (optional)
          Filters repos that have paths starting with the given path prefix. If not provided or when provided
          an effectively empty prefix (`/` or `/Workspace`) Git folders (repos) from `/Workspace/Repos` will
          be served.
        
        :returns: Iterator over :class:`RepoInfo`
        

    .. py:method:: set_permissions(repo_id: str [, access_control_list: Optional[List[RepoAccessControlRequest]]]) -> RepoPermissions

        Set repo permissions.
        
        Sets permissions on a repo. Repos can inherit permissions from their root object.
        
        :param repo_id: str
          The repo for which to get or manage permissions.
        :param access_control_list: List[:class:`RepoAccessControlRequest`] (optional)
        
        :returns: :class:`RepoPermissions`
        

    .. py:method:: update(repo_id: int [, branch: Optional[str], sparse_checkout: Optional[SparseCheckoutUpdate], tag: Optional[str]])


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
          ID of the Git folder (repo) object in the workspace.
        :param branch: str (optional)
          Branch that the local version of the repo is checked out to.
        :param sparse_checkout: :class:`SparseCheckoutUpdate` (optional)
          If specified, update the sparse checkout settings. The update will fail if sparse checkout is not
          enabled for the repo.
        :param tag: str (optional)
          Tag that the local version of the repo is checked out to. Updating the repo to a tag puts the repo
          in a detached HEAD state. Before committing new changes, you must update the repo to a branch
          instead of the detached HEAD.
        
        
        

    .. py:method:: update_permissions(repo_id: str [, access_control_list: Optional[List[RepoAccessControlRequest]]]) -> RepoPermissions

        Update repo permissions.
        
        Updates the permissions on a repo. Repos can inherit permissions from their root object.
        
        :param repo_id: str
          The repo for which to get or manage permissions.
        :param access_control_list: List[:class:`RepoAccessControlRequest`] (optional)
        
        :returns: :class:`RepoPermissions`
        
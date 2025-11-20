``w.libraries``: Managed Libraries
==================================
.. currentmodule:: databricks.sdk.service.compute

.. py:class:: LibrariesAPI

    The Libraries API allows you to install and uninstall libraries and get the status of libraries on a
    cluster.

    To make third-party or custom code available to notebooks and jobs running on your clusters, you can
    install a library. Libraries can be written in Python, Java, Scala, and R. You can upload Python, Java,
    Scala and R libraries and point to external packages in PyPI, Maven, and CRAN repositories.

    Cluster libraries can be used by all notebooks running on a cluster. You can install a cluster library
    directly from a public repository such as PyPI or Maven, using a previously installed workspace library,
    or using an init script.

    When you uninstall a library from a cluster, the library is removed only when you restart the cluster.
    Until you restart the cluster, the status of the uninstalled library appears as Uninstall pending restart.

    .. py:method:: all_cluster_statuses() -> Iterator[ClusterLibraryStatuses]

        Get the status of all libraries on all clusters. A status is returned for all libraries installed on
        this cluster via the API or the libraries UI.


        :returns: Iterator over :class:`ClusterLibraryStatuses`
        

    .. py:method:: cluster_status(cluster_id: str) -> Iterator[LibraryFullStatus]

        Get the status of libraries on a cluster. A status is returned for all libraries installed on this
        cluster via the API or the libraries UI. The order of returned libraries is as follows: 1. Libraries
        set to be installed on this cluster, in the order that the libraries were added to the cluster, are
        returned first. 2. Libraries that were previously requested to be installed on this cluster or, but
        are now marked for removal, in no particular order, are returned last.

        :param cluster_id: str
          Unique identifier of the cluster whose status should be retrieved.

        :returns: Iterator over :class:`LibraryFullStatus`
        

    .. py:method:: create_default_base_environment(default_base_environment: DefaultBaseEnvironment [, request_id: Optional[str]]) -> DefaultBaseEnvironment

        Create a default base environment within workspaces to define the environment version and a list of
        dependencies to be used in serverless notebooks and jobs. This process will asynchronously generate a
        cache to optimize dependency resolution.

        :param default_base_environment: :class:`DefaultBaseEnvironment`
        :param request_id: str (optional)
          A unique identifier for this request. A random UUID is recommended. This request is only idempotent
          if a `request_id` is provided.

        :returns: :class:`DefaultBaseEnvironment`
        

    .. py:method:: delete_default_base_environment(id: str)

        Delete the default base environment given an ID. The default base environment may be used by
        downstream workloads. Please ensure that the deletion is intentional.

        :param id: str


        

    .. py:method:: get_default_base_environment(id: str [, trace_id: Optional[str]]) -> DefaultBaseEnvironment

        Return the default base environment details for a given ID.

        :param id: str
        :param trace_id: str (optional)
          Deprecated: use ctx.requestId instead

        :returns: :class:`DefaultBaseEnvironment`
        

    .. py:method:: install(cluster_id: str, libraries: List[Library])

        Add libraries to install on a cluster. The installation is asynchronous; it happens in the background
        after the completion of this request.

        :param cluster_id: str
          Unique identifier for the cluster on which to install these libraries.
        :param libraries: List[:class:`Library`]
          The libraries to install.


        

    .. py:method:: list_default_base_environments( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DefaultBaseEnvironment]

        List default base environments defined in the workspaces for the requested user.

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`DefaultBaseEnvironment`
        

    .. py:method:: refresh_default_base_environments(ids: List[str])

        Refresh the cached default base environments for the given IDs. This process will asynchronously
        regenerate the caches. The existing caches remains available until it expires.

        :param ids: List[str]


        

    .. py:method:: uninstall(cluster_id: str, libraries: List[Library])

        Set libraries to uninstall from a cluster. The libraries won't be uninstalled until the cluster is
        restarted. A request to uninstall a library that is not currently installed is ignored.

        :param cluster_id: str
          Unique identifier for the cluster on which to uninstall these libraries.
        :param libraries: List[:class:`Library`]
          The libraries to uninstall.


        

    .. py:method:: update_default_base_environment(id: str, default_base_environment: DefaultBaseEnvironment) -> DefaultBaseEnvironment

        Update the default base environment for the given ID. This process will asynchronously regenerate the
        cache. The existing cache remains available until it expires.

        :param id: str
        :param default_base_environment: :class:`DefaultBaseEnvironment`

        :returns: :class:`DefaultBaseEnvironment`
        

    .. py:method:: update_default_default_base_environment( [, base_environment_type: Optional[BaseEnvironmentType], id: Optional[str]]) -> DefaultBaseEnvironment

        Set the default base environment for the workspace. This marks the specified DBE as the workspace
        default.

        :param base_environment_type: :class:`BaseEnvironmentType` (optional)
        :param id: str (optional)

        :returns: :class:`DefaultBaseEnvironment`
        
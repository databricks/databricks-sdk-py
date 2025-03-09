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

        Get all statuses.

        Get the status of all libraries on all clusters. A status is returned for all libraries installed on
        this cluster via the API or the libraries UI.

        :returns: Iterator over :class:`ClusterLibraryStatuses`
        

    .. py:method:: cluster_status(cluster_id: str) -> Iterator[LibraryFullStatus]

        Get status.

        Get the status of libraries on a cluster. A status is returned for all libraries installed on this
        cluster via the API or the libraries UI. The order of returned libraries is as follows: 1. Libraries
        set to be installed on this cluster, in the order that the libraries were added to the cluster, are
        returned first. 2. Libraries that were previously requested to be installed on this cluster or, but
        are now marked for removal, in no particular order, are returned last.

        :param cluster_id: str
          Unique identifier of the cluster whose status should be retrieved.

        :returns: Iterator over :class:`LibraryFullStatus`
        

    .. py:method:: install(cluster_id: str, libraries: List[Library])

        Add a library.

        Add libraries to install on a cluster. The installation is asynchronous; it happens in the background
        after the completion of this request.

        :param cluster_id: str
          Unique identifier for the cluster on which to install these libraries.
        :param libraries: List[:class:`Library`]
          The libraries to install.


        

    .. py:method:: uninstall(cluster_id: str, libraries: List[Library])

        Uninstall libraries.

        Set libraries to uninstall from a cluster. The libraries won't be uninstalled until the cluster is
        restarted. A request to uninstall a library that is not currently installed is ignored.

        :param cluster_id: str
          Unique identifier for the cluster on which to uninstall these libraries.
        :param libraries: List[:class:`Library`]
          The libraries to uninstall.


        
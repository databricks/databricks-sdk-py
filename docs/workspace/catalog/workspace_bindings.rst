``w.workspace_bindings``: Workspace Bindings
============================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: WorkspaceBindingsAPI

    A securable in Databricks can be configured as __OPEN__ or __ISOLATED__. An __OPEN__ securable can be
    accessed from any workspace, while an __ISOLATED__ securable can only be accessed from a configured list
    of workspaces. This API allows you to configure (bind) securables to workspaces.

    NOTE: The __isolation_mode__ is configured for the securable itself (using its Update method) and the
    workspace bindings are only consulted when the securable's __isolation_mode__ is set to __ISOLATED__.

    A securable's workspace bindings can be configured by a metastore admin or the owner of the securable.

    The original path (/api/2.1/unity-catalog/workspace-bindings/catalogs/{name}) is deprecated. Please use
    the new path (/api/2.1/unity-catalog/bindings/{securable_type}/{securable_name}) which introduces the
    ability to bind a securable in READ_ONLY mode (catalogs only).

    Securable types that support binding: - catalog - storage_credential - credential - external_location

    .. py:method:: get(name: str) -> GetCatalogWorkspaceBindingsResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.catalogs.create(name=f"sdk-{time.time_ns()}")
            
            bindings = w.workspace_bindings.get(name=created.name)
            
            # cleanup
            w.catalogs.delete(name=created.name, force=True)

        Gets workspace bindings of the catalog. The caller must be a metastore admin or an owner of the
        catalog.

        :param name: str
          The name of the catalog.

        :returns: :class:`GetCatalogWorkspaceBindingsResponse`
        

    .. py:method:: get_bindings(securable_type: str, securable_name: str [, max_results: Optional[int], page_token: Optional[str]]) -> Iterator[WorkspaceBinding]

        Gets workspace bindings of the securable. The caller must be a metastore admin or an owner of the
        securable.

        NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls
        will be deprecated soon.

        PAGINATION BEHAVIOR: When using pagination (max_results >= 0), a page may contain zero results while
        still providing a next_page_token. Clients must continue reading pages until next_page_token is
        absent, which is the only indication that the end of results has been reached.

        :param securable_type: str
          The type of the securable to bind to a workspace (catalog, storage_credential, credential, or
          external_location).
        :param securable_name: str
          The name of the securable.
        :param max_results: int (optional)
          Maximum number of workspace bindings to return. - When set to 0, the page length is set to a server
          configured value (recommended); - When set to a value greater than 0, the page length is the minimum
          of this value and a server configured value; - When set to a value less than 0, an invalid parameter
          error is returned; - If not set, all the workspace bindings are returned (not recommended).
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.

        :returns: Iterator over :class:`WorkspaceBinding`
        

    .. py:method:: update(name: str [, assign_workspaces: Optional[List[int]], unassign_workspaces: Optional[List[int]]]) -> UpdateCatalogWorkspaceBindingsResponse


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            this_workspace_id = os.environ["THIS_WORKSPACE_ID"]
            
            created = w.catalogs.create(name=f"sdk-{time.time_ns()}")
            
            _ = w.workspace_bindings.update(name=created.name, assign_workspaces=[this_workspace_id])
            
            # cleanup
            w.catalogs.delete(name=created.name, force=True)

        Updates workspace bindings of the catalog. The caller must be a metastore admin or an owner of the
        catalog.

        :param name: str
          The name of the catalog.
        :param assign_workspaces: List[int] (optional)
          A list of workspace IDs.
        :param unassign_workspaces: List[int] (optional)
          A list of workspace IDs.

        :returns: :class:`UpdateCatalogWorkspaceBindingsResponse`
        

    .. py:method:: update_bindings(securable_type: str, securable_name: str [, add: Optional[List[WorkspaceBinding]], remove: Optional[List[WorkspaceBinding]]]) -> UpdateWorkspaceBindingsResponse

        Updates workspace bindings of the securable. The caller must be a metastore admin or an owner of the
        securable.

        :param securable_type: str
          The type of the securable to bind to a workspace (catalog, storage_credential, credential, or
          external_location).
        :param securable_name: str
          The name of the securable.
        :param add: List[:class:`WorkspaceBinding`] (optional)
          List of workspace bindings to add. If a binding for the workspace already exists with a different
          binding_type, adding it again with a new binding_type will update the existing binding (e.g., from
          READ_WRITE to READ_ONLY).
        :param remove: List[:class:`WorkspaceBinding`] (optional)
          List of workspace bindings to remove.

        :returns: :class:`UpdateWorkspaceBindingsResponse`
        
Workspace Bindings
==================
.. py:class:: WorkspaceBindingsAPI

    A catalog in Databricks can be configured as __OPEN__ or __ISOLATED__. An __OPEN__ catalog can be accessed
    from any workspace, while an __ISOLATED__ catalog can only be access from a configured list of workspaces.
    
    A catalog's workspace bindings can be configured by a metastore admin or the owner of the catalog.

    .. py:method:: get(name)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            bindings = w.workspace_bindings.get(name=created.name)
            
            # cleanup
            w.catalogs.delete(name=created.name, force=True)

        Get catalog workspace bindings.
        
        Gets workspace bindings of the catalog. The caller must be a metastore admin or an owner of the
        catalog.
        
        :param name: str
          The name of the catalog.
        
        :returns: :class:`CurrentWorkspaceBindings`
        

    .. py:method:: update(name [, assign_workspaces, unassign_workspaces])

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            this_workspace_id = os.environ["THIS_WORKSPACE_ID"]
            
            created = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            _ = w.workspace_bindings.update(name=created.name, assign_workspaces=[this_workspace_id])
            
            # cleanup
            w.catalogs.delete(name=created.name, force=True)

        Update catalog workspace bindings.
        
        Updates workspace bindings of the catalog. The caller must be a metastore admin or an owner of the
        catalog.
        
        :param name: str
          The name of the catalog.
        :param assign_workspaces: List[int] (optional)
          A list of workspace IDs.
        :param unassign_workspaces: List[int] (optional)
          A list of workspace IDs.
        
        :returns: :class:`CurrentWorkspaceBindings`
        
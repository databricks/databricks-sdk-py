Catalogs
========
.. py:class:: CatalogsAPI

    A catalog is the first layer of Unity Catalog’s three-level namespace. It’s used to organize your data
    assets. Users can see all catalogs on which they have been assigned the USE_CATALOG data permission.
    
    In Unity Catalog, admins and data stewards manage users and their access to data centrally across all of
    the workspaces in a Databricks account. Users in different workspaces can share access to the same data,
    depending on privileges granted centrally in Unity Catalog.

    .. py:method:: create(name [, comment, properties, provider_name, share_name, storage_root])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.catalogs.delete(name=created.name, force=True)

        Create a catalog.
        
        Creates a new catalog instance in the parent metastore if the caller is a metastore admin or has the
        **CREATE_CATALOG** privilege.
        
        :param name: str
          Name of catalog.
        :param comment: str (optional)
          User-provided free-form text description.
        :param properties: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        :param provider_name: str (optional)
          The name of delta sharing provider.
          
          A Delta Sharing catalog is a catalog that is based on a Delta share on a remote sharing server.
        :param share_name: str (optional)
          The name of the share under the share provider.
        :param storage_root: str (optional)
          Storage root URL for managed tables within catalog.
        
        :returns: :class:`CatalogInfo`
        

    .. py:method:: delete(name [, force])

        Delete a catalog.
        
        Deletes the catalog that matches the supplied name. The caller must be a metastore admin or the owner
        of the catalog.
        
        :param name: str
          The name of the catalog.
        :param force: bool (optional)
          Force deletion even if the catalog is not empty.
        
        
        

    .. py:method:: get(name)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            _ = w.catalogs.get(get=created.name)
            
            # cleanup
            w.catalogs.delete(name=created.name, force=True)

        Get a catalog.
        
        Gets the specified catalog in a metastore. The caller must be a metastore admin, the owner of the
        catalog, or a user that has the **USE_CATALOG** privilege set for their account.
        
        :param name: str
          The name of the catalog.
        
        :returns: :class:`CatalogInfo`
        

    .. py:method:: list()

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.catalogs.list()

        List catalogs.
        
        Gets an array of catalogs in the metastore. If the caller is the metastore admin, all catalogs will be
        retrieved. Otherwise, only catalogs owned by the caller (or for which the caller has the
        **USE_CATALOG** privilege) will be retrieved. There is no guarantee of a specific ordering of the
        elements in the array.
        
        :returns: Iterator over :class:`CatalogInfo`
        

    .. py:method:: update(name [, comment, isolation_mode, owner, properties])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            _ = w.catalogs.update(name=created.name, comment="updated")
            
            # cleanup
            w.catalogs.delete(name=created.name, force=True)

        Update a catalog.
        
        Updates the catalog that matches the supplied name. The caller must be either the owner of the
        catalog, or a metastore admin (when changing the owner field of the catalog).
        
        :param name: str
          Name of catalog.
        :param comment: str (optional)
          User-provided free-form text description.
        :param isolation_mode: :class:`IsolationMode` (optional)
          Whether the current securable is accessible from all workspaces or a specific set of workspaces.
        :param owner: str (optional)
          Username of current owner of catalog.
        :param properties: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        
        :returns: :class:`CatalogInfo`
        
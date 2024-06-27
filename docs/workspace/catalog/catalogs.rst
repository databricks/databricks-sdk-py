``w.catalogs``: Catalogs
========================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: CatalogsAPI

    A catalog is the first layer of Unity Catalog’s three-level namespace. It’s used to organize your data
    assets. Users can see all catalogs on which they have been assigned the USE_CATALOG data permission.
    
    In Unity Catalog, admins and data stewards manage users and their access to data centrally across all of
    the workspaces in a Databricks account. Users in different workspaces can share access to the same data,
    depending on privileges granted centrally in Unity Catalog.

    .. py:method:: create(name: str [, comment: Optional[str], connection_name: Optional[str], options: Optional[Dict[str, str]], properties: Optional[Dict[str, str]], provider_name: Optional[str], share_name: Optional[str], storage_root: Optional[str]]) -> CatalogInfo


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
        :param connection_name: str (optional)
          The name of the connection to an external data source.
        :param options: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
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
        

    .. py:method:: delete(name: str [, force: Optional[bool]])

        Delete a catalog.
        
        Deletes the catalog that matches the supplied name. The caller must be a metastore admin or the owner
        of the catalog.
        
        :param name: str
          The name of the catalog.
        :param force: bool (optional)
          Force deletion even if the catalog is not empty.
        
        
        

    .. py:method:: get(name: str [, include_browse: Optional[bool]]) -> CatalogInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            _ = w.catalogs.get(name=created.name)
            
            # cleanup
            w.catalogs.delete(name=created.name, force=True)

        Get a catalog.
        
        Gets the specified catalog in a metastore. The caller must be a metastore admin, the owner of the
        catalog, or a user that has the **USE_CATALOG** privilege set for their account.
        
        :param name: str
          The name of the catalog.
        :param include_browse: bool (optional)
          Whether to include catalogs in the response for which the principal can only access selective
          metadata for
        
        :returns: :class:`CatalogInfo`
        

    .. py:method:: list( [, include_browse: Optional[bool], max_results: Optional[int], page_token: Optional[str]]) -> Iterator[CatalogInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            all = w.catalogs.list(catalog.ListCatalogsRequest())

        List catalogs.
        
        Gets an array of catalogs in the metastore. If the caller is the metastore admin, all catalogs will be
        retrieved. Otherwise, only catalogs owned by the caller (or for which the caller has the
        **USE_CATALOG** privilege) will be retrieved. There is no guarantee of a specific ordering of the
        elements in the array.
        
        :param include_browse: bool (optional)
          Whether to include catalogs in the response for which the principal can only access selective
          metadata for
        :param max_results: int (optional)
          Maximum number of catalogs to return. - when set to 0, the page length is set to a server configured
          value (recommended); - when set to a value greater than 0, the page length is the minimum of this
          value and a server configured value; - when set to a value less than 0, an invalid parameter error
          is returned; - If not set, all valid catalogs are returned (not recommended). - Note: The number of
          returned catalogs might be less than the specified max_results size, even zero. The only definitive
          indication that no further catalogs can be fetched is when the next_page_token is unset from the
          response.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`CatalogInfo`
        

    .. py:method:: update(name: str [, comment: Optional[str], enable_predictive_optimization: Optional[EnablePredictiveOptimization], isolation_mode: Optional[CatalogIsolationMode], new_name: Optional[str], owner: Optional[str], properties: Optional[Dict[str, str]]]) -> CatalogInfo


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
          The name of the catalog.
        :param comment: str (optional)
          User-provided free-form text description.
        :param enable_predictive_optimization: :class:`EnablePredictiveOptimization` (optional)
          Whether predictive optimization should be enabled for this object and objects under it.
        :param isolation_mode: :class:`CatalogIsolationMode` (optional)
          Whether the current securable is accessible from all workspaces or a specific set of workspaces.
        :param new_name: str (optional)
          New name for the catalog.
        :param owner: str (optional)
          Username of current owner of catalog.
        :param properties: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        
        :returns: :class:`CatalogInfo`
        
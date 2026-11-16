``w.catalogs``: Catalogs
========================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: CatalogsAPI

    A catalog is the first layer of Unity Catalog’s three-level namespace. It’s used to organize your data
    assets. Users can see all catalogs on which they have been assigned the USE_CATALOG data permission.

    In Unity Catalog, admins and data stewards manage users and their access to data centrally across all of
    the workspaces in a Databricks account. Users in different workspaces can share access to the same data,
    depending on privileges granted centrally in Unity Catalog.

    .. py:method:: create(name: str [, comment: Optional[str], connection_name: Optional[str], custom_max_retention_hours: Optional[int], managed_encryption_settings: Optional[EncryptionSettings], options: Optional[Dict[str, str]], properties: Optional[Dict[str, str]], provider_name: Optional[str], share_name: Optional[str], storage_root: Optional[str]]) -> CatalogInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.catalogs.create(name=f"sdk-{time.time_ns()}")
            
            # cleanup
            w.catalogs.delete(name=created.name, force=True)

        Creates a new catalog instance in the parent metastore if the caller is a metastore admin or has the
        **CREATE_CATALOG** privilege.

        :param name: str
          The name of the catalog is stored in lowercase, can be at most 255 characters long, and cannot
          contain periods, spaces, forward slashes, or control characters.
        :param comment: str (optional)
          User-provided free-form text description.
        :param connection_name: str (optional)
          Naming a connection to an external data source creates a foreign catalog that mirrors a database in
          that source, which requires ownership of or the CREATE FOREIGN CATALOG privilege on the connection.
          Connection-specific settings, such as the database to mirror, go in options. The connection cannot
          be changed after creation.
        :param custom_max_retention_hours: int (optional)
          Dropped objects in the catalog remain recoverable for this number of hours before they are
          permanently purged. The value applies to standard catalogs only, must be 0 or within the range
          allowed for the metastore, and is inherited by schemas and tables that do not set their own value.
        :param managed_encryption_settings: :class:`EncryptionSettings` (optional)
          Customer-managed key (CMK) settings control the encryption at rest of the catalog's managed data.
        :param options: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        :param properties: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        :param provider_name: str (optional)
          The Delta Sharing provider that owns the share must be named here, together with share_name, to
          create a Delta Sharing catalog that exposes the data of the share on a remote sharing server. The
          provider cannot be changed after creation.
        :param share_name: str (optional)
          The share under the Delta Sharing provider must be named here, together with provider_name, to
          create a Delta Sharing catalog. The share cannot be changed after creation.
        :param storage_root: str (optional)
          Managed tables and volumes in the catalog are stored under this storage root URL. The path must be
          inside an external location on which the caller has the CREATE MANAGED STORAGE privilege. If
          omitted, managed data is stored under the metastore's root storage location, which must then be
          configured. Delta Sharing catalogs cannot have a storage root.

        :returns: :class:`CatalogInfo`
        

    .. py:method:: delete(name: str [, force: Optional[bool]])

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
            
            created = w.catalogs.create(name=f"sdk-{time.time_ns()}")
            
            _ = w.catalogs.get(name=created.name)
            
            # cleanup
            w.catalogs.delete(name=created.name, force=True)

        Gets the specified catalog in a metastore. The caller must be a metastore admin, the owner of the
        catalog, or a user that has the **USE_CATALOG** privilege set for their account.

        :param name: str
          The name of the catalog.
        :param include_browse: bool (optional)
          Whether to return the catalog when the principal can only access selective metadata for it through
          the BROWSE privilege. The response then has browse_only set to true.

        :returns: :class:`CatalogInfo`
        

    .. py:method:: list( [, include_browse: Optional[bool], include_unbound: Optional[bool], max_results: Optional[int], page_token: Optional[str]]) -> Iterator[CatalogInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            all = w.catalogs.list(catalog.ListCatalogsRequest())

        Gets an array of catalogs in the metastore. If the caller is the metastore admin, all catalogs will be
        retrieved. Otherwise, only catalogs owned by the caller (or for which the caller has the
        **USE_CATALOG** privilege) will be retrieved. There is no guarantee of a specific ordering of the
        elements in the array.

        NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls
        will be deprecated soon.

        PAGINATION BEHAVIOR: When using pagination (max_results >= 0), a page may contain zero results while
        still providing a next_page_token. Clients must continue reading pages until next_page_token is
        absent, which is the only indication that the end of results has been reached.

        :param include_browse: bool (optional)
          Whether to include catalogs for which the principal can only access selective metadata through the
          BROWSE privilege. Such catalogs are returned with browse_only set to true.
        :param include_unbound: bool (optional)
          Whether to include catalogs not bound to the workspace. Effective only if the user has permission to
          update the catalog–workspace binding.
        :param max_results: int (optional)
          Maximum number of catalogs to return.

          - when set to 0, the page length is set to a server configured value (recommended);
          - when set to a value greater than 0, the page length is the minimum of this value and a server
            configured value;
          - when set to a value less than 0, an invalid parameter error is returned;
          - If not set, all valid catalogs are returned (not recommended).
          - Note: The number of returned catalogs might be less than the specified max_results size, even
            zero. The only definitive indication that no further catalogs can be fetched is when the
            next_page_token is unset from the response.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.

        :returns: Iterator over :class:`CatalogInfo`
        

    .. py:method:: update(name: str [, comment: Optional[str], custom_max_retention_hours: Optional[int], enable_predictive_optimization: Optional[EnablePredictiveOptimization], isolation_mode: Optional[CatalogIsolationMode], managed_encryption_settings: Optional[EncryptionSettings], new_name: Optional[str], options: Optional[Dict[str, str]], owner: Optional[str], properties: Optional[Dict[str, str]]]) -> CatalogInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            created = w.catalogs.create(name=f"sdk-{time.time_ns()}")
            
            _ = w.catalogs.update(name=created.name, isolation_mode=catalog.CatalogIsolationMode.ISOLATED)
            
            # cleanup
            w.catalogs.delete(name=created.name, force=True)

        Updates the catalog that matches the supplied name. The caller must be either the owner of the
        catalog, or a metastore admin (when changing the owner field of the catalog).

        :param name: str
          The name of the catalog.
        :param comment: str (optional)
          User-provided free-form text description.
        :param custom_max_retention_hours: int (optional)
          Dropped objects in the catalog remain recoverable for this number of hours before they are
          permanently purged. The value applies to standard catalogs only, must be 0 or within the range
          allowed for the metastore, and is inherited by schemas and tables that do not set their own value.
        :param enable_predictive_optimization: :class:`EnablePredictiveOptimization` (optional)
          Whether predictive optimization is enabled for this catalog and the objects under it. Valid values
          are ENABLE, DISABLE, and INHERIT, where INHERIT applies the account-level setting. Standard catalogs
          start as INHERIT and other catalog types as DISABLE. It cannot be set when creating a catalog; use
          the update method instead.
        :param isolation_mode: :class:`CatalogIsolationMode` (optional)
          Whether the catalog is accessible from all workspaces attached to the metastore (OPEN) or only from
          the workspaces bound to it (ISOLATED). It cannot be set when creating a catalog; change it with the
          update method and manage the bound workspaces with the workspace bindings API. See
          `Workspace-catalog binding <https://docs.databricks.com/aws/en/catalogs/binding>`__.
        :param managed_encryption_settings: :class:`EncryptionSettings` (optional)
          Customer-managed key (CMK) settings control the encryption at rest of the catalog's managed data.
        :param new_name: str (optional)
          New name for the catalog.
        :param options: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        :param owner: str (optional)
          Username of current owner of catalog.
        :param properties: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.

        :returns: :class:`CatalogInfo`
        
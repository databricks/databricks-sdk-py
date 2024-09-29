``w.schemas``: Schemas
======================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: SchemasAPI

    A schema (also called a database) is the second layer of Unity Catalog’s three-level namespace. A schema
    organizes tables, views and functions. To access (or list) a table or view in a schema, users must have
    the USE_SCHEMA data permission on the schema and its parent catalog, and they must have the SELECT
    permission on the table or view.

    .. py:method:: create(name: str, catalog_name: str [, comment: Optional[str], properties: Optional[Dict[str, str]], storage_root: Optional[str]]) -> SchemaInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)
            
            # cleanup
            w.catalogs.delete(name=created_catalog.name, force=True)
            w.schemas.delete(full_name=created_schema.full_name)

        Create a schema.
        
        Creates a new schema for catalog in the Metatastore. The caller must be a metastore admin, or have the
        **CREATE_SCHEMA** privilege in the parent catalog.
        
        :param name: str
          Name of schema, relative to parent catalog.
        :param catalog_name: str
          Name of parent catalog.
        :param comment: str (optional)
          User-provided free-form text description.
        :param properties: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        :param storage_root: str (optional)
          Storage root URL for managed tables within schema.
        
        :returns: :class:`SchemaInfo`
        

    .. py:method:: delete(full_name: str [, force: Optional[bool]])

        Delete a schema.
        
        Deletes the specified schema from the parent catalog. The caller must be the owner of the schema or an
        owner of the parent catalog.
        
        :param full_name: str
          Full name of the schema.
        :param force: bool (optional)
          Force deletion even if the schema is not empty.
        
        
        

    .. py:method:: get(full_name: str [, include_browse: Optional[bool]]) -> SchemaInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            new_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            created = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=new_catalog.name)
            
            _ = w.schemas.get(full_name=created.full_name)
            
            # cleanup
            w.catalogs.delete(name=new_catalog.name, force=True)
            w.schemas.delete(full_name=created.full_name)

        Get a schema.
        
        Gets the specified schema within the metastore. The caller must be a metastore admin, the owner of the
        schema, or a user that has the **USE_SCHEMA** privilege on the schema.
        
        :param full_name: str
          Full name of the schema.
        :param include_browse: bool (optional)
          Whether to include schemas in the response for which the principal can only access selective
          metadata for
        
        :returns: :class:`SchemaInfo`
        

    .. py:method:: list(catalog_name: str [, include_browse: Optional[bool], max_results: Optional[int], page_token: Optional[str]]) -> Iterator[SchemaInfo]


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            new_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            all = w.schemas.list(catalog_name=new_catalog.name)
            
            # cleanup
            w.catalogs.delete(name=new_catalog.name, force=True)

        List schemas.
        
        Gets an array of schemas for a catalog in the metastore. If the caller is the metastore admin or the
        owner of the parent catalog, all schemas for the catalog will be retrieved. Otherwise, only schemas
        owned by the caller (or for which the caller has the **USE_SCHEMA** privilege) will be retrieved.
        There is no guarantee of a specific ordering of the elements in the array.
        
        :param catalog_name: str
          Parent catalog for schemas of interest.
        :param include_browse: bool (optional)
          Whether to include schemas in the response for which the principal can only access selective
          metadata for
        :param max_results: int (optional)
          Maximum number of schemas to return. If not set, all the schemas are returned (not recommended). -
          when set to a value greater than 0, the page length is the minimum of this value and a server
          configured value; - when set to 0, the page length is set to a server configured value
          (recommended); - when set to a value less than 0, an invalid parameter error is returned;
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`SchemaInfo`
        

    .. py:method:: update(full_name: str [, comment: Optional[str], enable_predictive_optimization: Optional[EnablePredictiveOptimization], new_name: Optional[str], owner: Optional[str], properties: Optional[Dict[str, str]]]) -> SchemaInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            new_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            created = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=new_catalog.name)
            
            _ = w.schemas.update(full_name=created.full_name, comment=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.catalogs.delete(name=new_catalog.name, force=True)
            w.schemas.delete(full_name=created.full_name)

        Update a schema.
        
        Updates a schema for a catalog. The caller must be the owner of the schema or a metastore admin. If
        the caller is a metastore admin, only the __owner__ field can be changed in the update. If the
        __name__ field must be updated, the caller must be a metastore admin or have the **CREATE_SCHEMA**
        privilege on the parent catalog.
        
        :param full_name: str
          Full name of the schema.
        :param comment: str (optional)
          User-provided free-form text description.
        :param enable_predictive_optimization: :class:`EnablePredictiveOptimization` (optional)
          Whether predictive optimization should be enabled for this object and objects under it.
        :param new_name: str (optional)
          New name for the schema.
        :param owner: str (optional)
          Username of current owner of schema.
        :param properties: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        
        :returns: :class:`SchemaInfo`
        
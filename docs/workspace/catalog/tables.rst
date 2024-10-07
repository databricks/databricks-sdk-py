``w.tables``: Tables
====================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: TablesAPI

    A table resides in the third layer of Unity Catalog’s three-level namespace. It contains rows of data.
    To create a table, users must have CREATE_TABLE and USE_SCHEMA permissions on the schema, and they must
    have the USE_CATALOG permission on its parent catalog. To query a table, users must have the SELECT
    permission on the table, and they must have the USE_CATALOG permission on its parent catalog and the
    USE_SCHEMA permission on its parent schema.
    
    A table can be managed or external. From an API perspective, a __VIEW__ is a particular kind of table
    (rather than a managed or external table).

    .. py:method:: delete(full_name: str)

        Delete a table.
        
        Deletes a table from the specified parent catalog and schema. The caller must be the owner of the
        parent catalog, have the **USE_CATALOG** privilege on the parent catalog and be the owner of the
        parent schema, or be the owner of the table and have the **USE_CATALOG** privilege on the parent
        catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          Full name of the table.
        
        
        

    .. py:method:: exists(full_name: str) -> TableExistsResponse

        Get boolean reflecting if table exists.
        
        Gets if a table exists in the metastore for a specific catalog and schema. The caller must satisfy one
        of the following requirements: * Be a metastore admin * Be the owner of the parent catalog * Be the
        owner of the parent schema and have the USE_CATALOG privilege on the parent catalog * Have the
        **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema,
        and either be the table owner or have the SELECT privilege on the table. * Have BROWSE privilege on
        the parent catalog * Have BROWSE privilege on the parent schema.
        
        :param full_name: str
          Full name of the table.
        
        :returns: :class:`TableExistsResponse`
        

    .. py:method:: get(full_name: str [, include_browse: Optional[bool], include_delta_metadata: Optional[bool], include_manifest_capabilities: Optional[bool]]) -> TableInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            table_name = f'sdk-{time.time_ns()}'
            
            created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)
            
            _ = w.statement_execution.execute(warehouse_id=os.environ["TEST_DEFAULT_WAREHOUSE_ID"],
                                              catalog=created_catalog.name,
                                              schema=created_schema.name,
                                              statement="CREATE TABLE %s AS SELECT 2+2 as four" % (table_name)).result()
            
            table_full_name = "%s.%s.%s" % (created_catalog.name, created_schema.name, table_name)
            
            created_table = w.tables.get(full_name=table_full_name)
            
            # cleanup
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)
            w.tables.delete(full_name=table_full_name)

        Get a table.
        
        Gets a table from the metastore for a specific catalog and schema. The caller must satisfy one of the
        following requirements: * Be a metastore admin * Be the owner of the parent catalog * Be the owner of
        the parent schema and have the USE_CATALOG privilege on the parent catalog * Have the **USE_CATALOG**
        privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema, and either be
        the table owner or have the SELECT privilege on the table.
        
        :param full_name: str
          Full name of the table.
        :param include_browse: bool (optional)
          Whether to include tables in the response for which the principal can only access selective metadata
          for
        :param include_delta_metadata: bool (optional)
          Whether delta metadata should be included in the response.
        :param include_manifest_capabilities: bool (optional)
          Whether to include a manifest containing capabilities the table has.
        
        :returns: :class:`TableInfo`
        

    .. py:method:: list(catalog_name: str, schema_name: str [, include_browse: Optional[bool], include_delta_metadata: Optional[bool], include_manifest_capabilities: Optional[bool], max_results: Optional[int], omit_columns: Optional[bool], omit_properties: Optional[bool], page_token: Optional[str]]) -> Iterator[TableInfo]


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)
            
            all_tables = w.tables.list(catalog_name=created_catalog.name, schema_name=created_schema.name)
            
            # cleanup
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)

        List tables.
        
        Gets an array of all tables for the current metastore under the parent catalog and schema. The caller
        must be a metastore admin or an owner of (or have the **SELECT** privilege on) the table. For the
        latter case, the caller must also be the owner or have the **USE_CATALOG** privilege on the parent
        catalog and the **USE_SCHEMA** privilege on the parent schema. There is no guarantee of a specific
        ordering of the elements in the array.
        
        :param catalog_name: str
          Name of parent catalog for tables of interest.
        :param schema_name: str
          Parent schema of tables.
        :param include_browse: bool (optional)
          Whether to include tables in the response for which the principal can only access selective metadata
          for
        :param include_delta_metadata: bool (optional)
          Whether delta metadata should be included in the response.
        :param include_manifest_capabilities: bool (optional)
          Whether to include a manifest containing capabilities the table has.
        :param max_results: int (optional)
          Maximum number of tables to return. If not set, all the tables are returned (not recommended). -
          when set to a value greater than 0, the page length is the minimum of this value and a server
          configured value; - when set to 0, the page length is set to a server configured value
          (recommended); - when set to a value less than 0, an invalid parameter error is returned;
        :param omit_columns: bool (optional)
          Whether to omit the columns of the table from the response or not.
        :param omit_properties: bool (optional)
          Whether to omit the properties of the table from the response or not.
        :param page_token: str (optional)
          Opaque token to send for the next page of results (pagination).
        
        :returns: Iterator over :class:`TableInfo`
        

    .. py:method:: list_summaries(catalog_name: str [, include_manifest_capabilities: Optional[bool], max_results: Optional[int], page_token: Optional[str], schema_name_pattern: Optional[str], table_name_pattern: Optional[str]]) -> Iterator[TableSummary]


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)
            
            summaries = w.tables.list_summaries(catalog_name=created_catalog.name,
                                                schema_name_pattern=created_schema.name)
            
            # cleanup
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)

        List table summaries.
        
        Gets an array of summaries for tables for a schema and catalog within the metastore. The table
        summaries returned are either:
        
        * summaries for tables (within the current metastore and parent catalog and schema), when the user is
        a metastore admin, or: * summaries for tables and schemas (within the current metastore and parent
        catalog) for which the user has ownership or the **SELECT** privilege on the table and ownership or
        **USE_SCHEMA** privilege on the schema, provided that the user also has ownership or the
        **USE_CATALOG** privilege on the parent catalog.
        
        There is no guarantee of a specific ordering of the elements in the array.
        
        :param catalog_name: str
          Name of parent catalog for tables of interest.
        :param include_manifest_capabilities: bool (optional)
          Whether to include a manifest containing capabilities the table has.
        :param max_results: int (optional)
          Maximum number of summaries for tables to return. If not set, the page length is set to a server
          configured value (10000, as of 1/5/2024). - when set to a value greater than 0, the page length is
          the minimum of this value and a server configured value (10000, as of 1/5/2024); - when set to 0,
          the page length is set to a server configured value (10000, as of 1/5/2024) (recommended); - when
          set to a value less than 0, an invalid parameter error is returned;
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        :param schema_name_pattern: str (optional)
          A sql LIKE pattern (% and _) for schema names. All schemas will be returned if not set or empty.
        :param table_name_pattern: str (optional)
          A sql LIKE pattern (% and _) for table names. All tables will be returned if not set or empty.
        
        :returns: Iterator over :class:`TableSummary`
        

    .. py:method:: update(full_name: str [, owner: Optional[str]])

        Update a table owner.
        
        Change the owner of the table. The caller must be the owner of the parent catalog, have the
        **USE_CATALOG** privilege on the parent catalog and be the owner of the parent schema, or be the owner
        of the table and have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**
        privilege on the parent schema.
        
        :param full_name: str
          Full name of the table.
        :param owner: str (optional)
        
        
        
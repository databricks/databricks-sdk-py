Tables
======
.. py:class:: TablesAPI

    A table resides in the third layer of Unity Catalog’s three-level namespace. It contains rows of data.
    To create a table, users must have CREATE_TABLE and USE_SCHEMA permissions on the schema, and they must
    have the USE_CATALOG permission on its parent catalog. To query a table, users must have the SELECT
    permission on the table, and they must have the USE_CATALOG permission on its parent catalog and the
    USE_SCHEMA permission on its parent schema.
    
    A table can be managed or external. From an API perspective, a __VIEW__ is a particular kind of table
    (rather than a managed or external table).

    .. py:method:: delete(full_name)

        Delete a table.
        
        Deletes a table from the specified parent catalog and schema. The caller must be the owner of the
        parent catalog, have the **USE_CATALOG** privilege on the parent catalog and be the owner of the
        parent schema, or be the owner of the table and have the **USE_CATALOG** privilege on the parent
        catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          Full name of the table.
        
        
        

    .. py:method:: get(full_name [, include_delta_metadata])

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
            
            created_table = w.tables.get(get=table_full_name)
            
            # cleanup
            w.schemas.delete(delete=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)
            w.tables.delete(delete=table_full_name)

        Get a table.
        
        Gets a table from the metastore for a specific catalog and schema. The caller must be a metastore
        admin, be the owner of the table and have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema, or be the owner of the table and have the **SELECT**
        privilege on it as well.
        
        :param full_name: str
          Full name of the table.
        :param include_delta_metadata: bool (optional)
          Whether delta metadata should be included in the response.
        
        :returns: :class:`TableInfo`
        

    .. py:method:: list(catalog_name, schema_name [, include_delta_metadata, max_results, page_token])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)
            
            all_tables = w.tables.list(catalog_name=created_catalog.name, schema_name=created_schema.name)
            
            # cleanup
            w.schemas.delete(delete=created_schema.full_name)
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
        :param include_delta_metadata: bool (optional)
          Whether delta metadata should be included in the response.
        :param max_results: int (optional)
          Maximum number of tables to return (page length). If not set, all accessible tables in the schema
          are returned. If set to:
          
          * greater than 0, page length is the minimum of this value and a server configured value. * equal to
          0, page length is set to a server configured value. * lesser than 0, invalid parameter error.
        :param page_token: str (optional)
          Opaque token to send for the next page of results (pagination).
        
        :returns: Iterator over :class:`TableInfo`
        

    .. py:method:: list_summaries(catalog_name [, max_results, page_token, schema_name_pattern, table_name_pattern])

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
            w.schemas.delete(delete=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)

        List table summaries.
        
        Gets an array of summaries for tables for a schema and catalog within the metastore. The table
        summaries returned are either:
        
        * summaries for all tables (within the current metastore and parent catalog and schema), when the user
        is a metastore admin, or: * summaries for all tables and schemas (within the current metastore and
        parent catalog) for which the user has ownership or the **SELECT** privilege on the table and
        ownership or **USE_SCHEMA** privilege on the schema, provided that the user also has ownership or the
        **USE_CATALOG** privilege on the parent catalog.
        
        There is no guarantee of a specific ordering of the elements in the array.
        
        :param catalog_name: str
          Name of parent catalog for tables of interest.
        :param max_results: int (optional)
          Maximum number of tables to return (page length). Defaults to 10000.
        :param page_token: str (optional)
          Opaque token to send for the next page of results (pagination).
        :param schema_name_pattern: str (optional)
          A sql LIKE pattern (% and _) for schema names. All schemas will be returned if not set or empty.
        :param table_name_pattern: str (optional)
          A sql LIKE pattern (% and _) for table names. All tables will be returned if not set or empty.
        
        :returns: Iterator over :class:`TableSummary`
        
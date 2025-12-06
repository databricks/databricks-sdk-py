``w.database``: Database Instances
==================================
.. currentmodule:: databricks.sdk.service.database

.. py:class:: DatabaseAPI

    Database Instances provide access to a database via REST API or direct SQL.

    .. py:method:: create_database_catalog(catalog: DatabaseCatalog) -> DatabaseCatalog

        Create a Database Catalog.

        :param catalog: :class:`DatabaseCatalog`

        :returns: :class:`DatabaseCatalog`
        

    .. py:method:: create_database_instance(database_instance: DatabaseInstance) -> Wait[DatabaseInstance]

        Create a Database Instance.

        :param database_instance: :class:`DatabaseInstance`
          Instance to create.

        :returns:
          Long-running operation waiter for :class:`DatabaseInstance`.
          See :method:wait_get_database_instance_database_available for more details.
        

    .. py:method:: create_database_instance_and_wait(database_instance: DatabaseInstance, timeout: datetime.timedelta = 0:20:00) -> DatabaseInstance


    .. py:method:: create_database_instance_role(instance_name: str, database_instance_role: DatabaseInstanceRole [, database_instance_name: Optional[str]]) -> DatabaseInstanceRole

        Create a role for a Database Instance.

        :param instance_name: str
        :param database_instance_role: :class:`DatabaseInstanceRole`
        :param database_instance_name: str (optional)

        :returns: :class:`DatabaseInstanceRole`
        

    .. py:method:: create_database_table(table: DatabaseTable) -> DatabaseTable

        Create a Database Table. Useful for registering pre-existing PG tables in UC. See
        CreateSyncedDatabaseTable for creating synced tables in PG from a source table in UC.

        :param table: :class:`DatabaseTable`

        :returns: :class:`DatabaseTable`
        

    .. py:method:: create_synced_database_table(synced_table: SyncedDatabaseTable) -> SyncedDatabaseTable

        Create a Synced Database Table.

        :param synced_table: :class:`SyncedDatabaseTable`

        :returns: :class:`SyncedDatabaseTable`
        

    .. py:method:: delete_database_catalog(name: str)

        Delete a Database Catalog.

        :param name: str


        

    .. py:method:: delete_database_instance(name: str [, force: Optional[bool], purge: Optional[bool]])

        Delete a Database Instance.

        :param name: str
          Name of the instance to delete.
        :param force: bool (optional)
          By default, a instance cannot be deleted if it has descendant instances created via PITR. If this
          flag is specified as true, all descendent instances will be deleted as well.
        :param purge: bool (optional)
          Deprecated. Omitting the field or setting it to true will result in the field being hard deleted.
          Setting a value of false will throw a bad request.


        

    .. py:method:: delete_database_instance_role(instance_name: str, name: str [, allow_missing: Optional[bool], reassign_owned_to: Optional[str]])

        Deletes a role for a Database Instance.

        :param instance_name: str
        :param name: str
        :param allow_missing: bool (optional)
          This is the AIP standard name for the equivalent of Postgres' `IF EXISTS` option
        :param reassign_owned_to: str (optional)


        

    .. py:method:: delete_database_table(name: str)

        Delete a Database Table.

        :param name: str


        

    .. py:method:: delete_synced_database_table(name: str [, purge_data: Optional[bool]])

        Delete a Synced Database Table.

        :param name: str
        :param purge_data: bool (optional)
          Optional. When set to true, the actual PostgreSQL table will be dropped from the database.


        

    .. py:method:: find_database_instance_by_uid( [, uid: Optional[str]]) -> DatabaseInstance

        Find a Database Instance by uid.

        :param uid: str (optional)
          UID of the cluster to get.

        :returns: :class:`DatabaseInstance`
        

    .. py:method:: generate_database_credential( [, claims: Optional[List[RequestedClaims]], instance_names: Optional[List[str]], request_id: Optional[str]]) -> DatabaseCredential

        Generates a credential that can be used to access database instances.

        :param claims: List[:class:`RequestedClaims`] (optional)
          The returned token will be scoped to the union of instance_names and instances containing the
          specified UC tables, so instance_names is allowed to be empty.
        :param instance_names: List[str] (optional)
          Instances to which the token will be scoped.
        :param request_id: str (optional)

        :returns: :class:`DatabaseCredential`
        

    .. py:method:: get_database_catalog(name: str) -> DatabaseCatalog

        Get a Database Catalog.

        :param name: str

        :returns: :class:`DatabaseCatalog`
        

    .. py:method:: get_database_instance(name: str) -> DatabaseInstance

        Get a Database Instance.

        :param name: str
          Name of the cluster to get.

        :returns: :class:`DatabaseInstance`
        

    .. py:method:: get_database_instance_role(instance_name: str, name: str) -> DatabaseInstanceRole

        Gets a role for a Database Instance.

        :param instance_name: str
        :param name: str

        :returns: :class:`DatabaseInstanceRole`
        

    .. py:method:: get_database_table(name: str) -> DatabaseTable

        Get a Database Table.

        :param name: str

        :returns: :class:`DatabaseTable`
        

    .. py:method:: get_synced_database_table(name: str) -> SyncedDatabaseTable

        Get a Synced Database Table.

        :param name: str

        :returns: :class:`SyncedDatabaseTable`
        

    .. py:method:: list_database_catalogs(instance_name: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DatabaseCatalog]

        This API is currently unimplemented, but exposed for Terraform support.

        :param instance_name: str
          Name of the instance to get database catalogs for.
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of synced database tables. Requests first page if absent.

        :returns: Iterator over :class:`DatabaseCatalog`
        

    .. py:method:: list_database_instance_roles(instance_name: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DatabaseInstanceRole]

        START OF PG ROLE APIs Section These APIs are marked a PUBLIC with stage < PUBLIC_PREVIEW. With more
        recent Lakebase V2 plans, we don't plan to ever advance these to PUBLIC_PREVIEW. These APIs will
        remain effectively undocumented/UI-only and we'll aim for a new public roles API as part of V2 PuPr.

        :param instance_name: str
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Database Instances. Requests first page if absent.

        :returns: Iterator over :class:`DatabaseInstanceRole`
        

    .. py:method:: list_database_instances( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DatabaseInstance]

        List Database Instances.

        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Database Instances. Requests first page if absent.

        :returns: Iterator over :class:`DatabaseInstance`
        

    .. py:method:: list_synced_database_tables(instance_name: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SyncedDatabaseTable]

        This API is currently unimplemented, but exposed for Terraform support.

        :param instance_name: str
          Name of the instance to get synced tables for.
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of synced database tables. Requests first page if absent.

        :returns: Iterator over :class:`SyncedDatabaseTable`
        

    .. py:method:: update_database_catalog(name: str, database_catalog: DatabaseCatalog, update_mask: str) -> DatabaseCatalog

        This API is currently unimplemented, but exposed for Terraform support.

        :param name: str
          The name of the catalog in UC.
        :param database_catalog: :class:`DatabaseCatalog`
          Note that updating a database catalog is not yet supported.
        :param update_mask: str
          The list of fields to update. Setting this field is not yet supported.

        :returns: :class:`DatabaseCatalog`
        

    .. py:method:: update_database_instance(name: str, database_instance: DatabaseInstance, update_mask: str) -> DatabaseInstance

        Update a Database Instance.

        :param name: str
          The name of the instance. This is the unique identifier for the instance.
        :param database_instance: :class:`DatabaseInstance`
        :param update_mask: str
          The list of fields to update. If unspecified, all fields will be updated when possible. To wipe out
          custom_tags, specify custom_tags in the update_mask with an empty custom_tags map.

        :returns: :class:`DatabaseInstance`
        

    .. py:method:: update_synced_database_table(name: str, synced_table: SyncedDatabaseTable, update_mask: str) -> SyncedDatabaseTable

        This API is currently unimplemented, but exposed for Terraform support.

        :param name: str
          Full three-part (catalog, schema, table) name of the table.
        :param synced_table: :class:`SyncedDatabaseTable`
          Note that updating a synced database table is not yet supported.
        :param update_mask: str
          The list of fields to update. Setting this field is not yet supported.

        :returns: :class:`SyncedDatabaseTable`
        

    .. py:method:: wait_get_database_instance_database_available(name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[DatabaseInstance], None]]) -> DatabaseInstance

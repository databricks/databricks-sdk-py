``w.database``: Database Instances
==================================
.. currentmodule:: databricks.sdk.service.database

.. py:class:: DatabaseAPI

    Database Instances provide access to a database via REST API or direct SQL.

    For new workloads, Databricks recommends the `Postgres API
    <https://docs.databricks.com/api/postgres/v1/postgres>`__, which supports the latest Lakebase features.

    .. py:method:: create_database_catalog(catalog: DatabaseCatalog) -> DatabaseCatalog

        Create a Database Catalog.

        For new workloads, Databricks recommends the Postgres API equivalent: `Create a catalog
        <https://docs.databricks.com/api/postgres/v1/create-catalog>`__.

        :param catalog: :class:`DatabaseCatalog`

        :returns: :class:`DatabaseCatalog`
        

    .. py:method:: create_database_instance(database_instance: DatabaseInstance) -> Wait[DatabaseInstance]

        Create a Database Instance.

        For new workloads, Databricks recommends the Postgres API equivalent: `Create a project
        <https://docs.databricks.com/api/postgres/v1/create-project>`__.

        :param database_instance: :class:`DatabaseInstance`
          Instance to create.

        :returns:
          Long-running operation waiter for :class:`DatabaseInstance`.
          See :method:wait_get_database_instance_database_available for more details.
        

    .. py:method:: create_database_instance_and_wait(database_instance: DatabaseInstance, timeout: datetime.timedelta = 0:20:00) -> DatabaseInstance


    .. py:method:: create_database_instance_role(instance_name: str, database_instance_role: DatabaseInstanceRole [, database_instance_name: Optional[str]]) -> DatabaseInstanceRole

        Create a role for a Database Instance.

        For new workloads, Databricks recommends the Postgres API equivalent: `Create a role
        <https://docs.databricks.com/api/postgres/v1/create-role>`__.

        :param instance_name: str
        :param database_instance_role: :class:`DatabaseInstanceRole`
        :param database_instance_name: str (optional)

        :returns: :class:`DatabaseInstanceRole`
        

    .. py:method:: create_database_table(table: DatabaseTable) -> DatabaseTable

        Create a Database Table. This registers a table that already exists in a Postgres database of a
        database instance as a table in Unity Catalog. The Postgres database, schema and table must already
        exist; the request does not create them. Repeating the request for the same table succeeds, and a
        request for a name that is already registered from a different database or instance fails. To create a
        Postgres table from a Unity Catalog source table instead, use `Create a Synced Database Table
        <https://docs.databricks.com/api/workspace/database/createsynceddatabasetable>`__.

        :param table: :class:`DatabaseTable`

        :returns: :class:`DatabaseTable`
        

    .. py:method:: create_synced_database_table(synced_table: SyncedDatabaseTable) -> SyncedDatabaseTable

        Create a Synced Database Table.

        The table and its data synchronization pipeline are provisioned asynchronously. The response reflects
        the initial state; use Get a Synced Database Table to follow the data synchronization status until the
        table is online.

        For new workloads, Databricks recommends the Postgres API equivalent: `Create a synced table
        <https://docs.databricks.com/api/postgres/v1/create-synced-table>`__.

        :param synced_table: :class:`SyncedDatabaseTable`

        :returns: :class:`SyncedDatabaseTable`
        

    .. py:method:: delete_database_catalog(name: str)

        Delete a Database Catalog. This removes the catalog from Unity Catalog, while the Postgres database
        and its tables remain in the instance.

        For new workloads, Databricks recommends the Postgres API equivalent: `Delete a catalog
        <https://docs.databricks.com/api/postgres/v1/delete-catalog>`__.

        :param name: str
          The Unity Catalog name of the catalog to delete.


        

    .. py:method:: delete_database_instance(name: str [, force: Optional[bool], purge: Optional[bool]])

        Delete a Database Instance.

        For new workloads, Databricks recommends the Postgres API equivalent: `Delete a project
        <https://docs.databricks.com/api/postgres/v1/delete-project>`__.

        :param name: str
          Name of the instance to delete.
        :param force: bool (optional)
          By default, an instance cannot be deleted if it has descendant instances created via PITR. Setting
          this flag to true is not supported and the request is rejected; delete the child instances first.
        :param purge: bool (optional)
          Deprecated: omitting the field or setting it to true hard deletes the instance. Setting it to false
          returns a bad request.


        

    .. py:method:: delete_database_instance_role(instance_name: str, name: str [, allow_missing: Optional[bool], reassign_owned_to: Optional[str]])

        Deletes a role for a Database Instance.

        For new workloads, Databricks recommends the Postgres API equivalent: `Delete a role
        <https://docs.databricks.com/api/postgres/v1/delete-role>`__.

        :param instance_name: str
        :param name: str
        :param allow_missing: bool (optional)
          This is the AIP standard name for the equivalent of Postgres' ``IF EXISTS`` option
        :param reassign_owned_to: str (optional)


        

    .. py:method:: delete_database_table(name: str)

        Delete a Database Table. This removes the table from Unity Catalog only; the Postgres table and its
        data are kept. Tables in a database catalog cannot be deleted with this method, and synced tables must
        be deleted with `Delete a Synced Database Table
        <https://docs.databricks.com/api/workspace/database/deletesynceddatabasetable>`__.

        :param name: str
          Specifies the database table by its full three-part (catalog, schema, table) name.


        

    .. py:method:: delete_synced_database_table(name: str [, purge_data: Optional[bool]])

        Delete a Synced Database Table.

        For new workloads, Databricks recommends the Postgres API equivalent: `Delete a synced table
        <https://docs.databricks.com/api/postgres/v1/delete-synced-table>`__.

        :param name: str
          Specifies the synced table by its full three-part (catalog, schema, table) name.
        :param purge_data: bool (optional)
          When true, the Postgres table is also dropped from the database. When false, the synced table is
          unregistered from Unity Catalog and its pipeline stops syncing it, but the Postgres table and its
          data are kept.


        

    .. py:method:: find_database_instance_by_uid( [, uid: Optional[str]]) -> DatabaseInstance

        Find a Database Instance by its uid rather than by name.

        :param uid: str (optional)
          UID of the instance to get, as returned in the uid field of the instance.

        :returns: :class:`DatabaseInstance`
        

    .. py:method:: generate_database_credential( [, claims: Optional[List[RequestedClaims]], instance_names: Optional[List[str]], request_id: Optional[str]]) -> DatabaseCredential

        Generates a short-lived OAuth token for connecting to database instances. Connect with the caller's
        Databricks identity as the Postgres user and the returned token as the password. For details about
        OAuth token authentication, see `About authentication
        <https://docs.databricks.com/aws/en/oltp/projects/authentication>`__.

        For new workloads, Databricks recommends the Postgres API equivalent: `Generate a database credential
        <https://docs.databricks.com/api/postgres/v1/generate-database-credential>`__.

        :param claims: List[:class:`RequestedClaims`] (optional)
          Unity Catalog permissions to embed in the credential. Databricks verifies that the caller holds each
          permission in Unity Catalog and records a reference to it in the token. When the user connects,
          Postgres grants them the matching privileges on the Postgres objects that back those Unity Catalog
          resources. Each resource must have a Postgres counterpart, such as a synced table or a table in a
          database catalog.
        :param instance_names: List[str] (optional)
          Names of the database instances to connect to with the credential. Every named instance must exist
          in the workspace, or the request fails. At least one of instance_names or claims must be specified.
        :param request_id: str (optional)
          A client-generated identifier for this request, such as a UUID. The request fails when it is
          omitted.

        :returns: :class:`DatabaseCredential`
        

    .. py:method:: get_database_catalog(name: str) -> DatabaseCatalog

        Get a Database Catalog.

        For new workloads, Databricks recommends the Postgres API equivalent: `Get a catalog
        <https://docs.databricks.com/api/postgres/v1/get-catalog>`__.

        :param name: str
          The Unity Catalog name of the catalog to retrieve.

        :returns: :class:`DatabaseCatalog`
        

    .. py:method:: get_database_instance(name: str) -> DatabaseInstance

        Get a Database Instance.

        For new workloads, Databricks recommends the Postgres API equivalent: `Get a project
        <https://docs.databricks.com/api/postgres/v1/get-project>`__.

        :param name: str
          Name of the instance to get.

        :returns: :class:`DatabaseInstance`
        

    .. py:method:: get_database_instance_role(instance_name: str, name: str) -> DatabaseInstanceRole

        Gets a role for a Database Instance.

        For new workloads, Databricks recommends the Postgres API equivalent: `Get a role
        <https://docs.databricks.com/api/postgres/v1/get-role>`__.

        :param instance_name: str
        :param name: str

        :returns: :class:`DatabaseInstanceRole`
        

    .. py:method:: get_database_table(name: str) -> DatabaseTable

        Get a Database Table. The request fails if the name refers to a synced table or to a table that is not
        a database table; for synced tables, use `Get a Synced Database Table
        <https://docs.databricks.com/api/workspace/database/getsynceddatabasetable>`__.

        :param name: str
          Specifies the database table by its full three-part (catalog, schema, table) name.

        :returns: :class:`DatabaseTable`
        

    .. py:method:: get_synced_database_table(name: str) -> SyncedDatabaseTable

        Get a Synced Database Table.

        For new workloads, Databricks recommends the Postgres API equivalent: `Get a synced table
        <https://docs.databricks.com/api/postgres/v1/get-synced-table>`__.

        :param name: str
          Specifies the synced table by its full three-part (catalog, schema, table) name.

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

        List roles for a Database Instance.

        For new workloads, Databricks recommends the Postgres API equivalent: `List roles
        <https://docs.databricks.com/api/postgres/v1/list-roles>`__.

        :param instance_name: str
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Database Instances. Requests first page if absent.

        :returns: Iterator over :class:`DatabaseInstanceRole`
        

    .. py:method:: list_database_instances( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DatabaseInstance]

        List Database Instances.

        For new workloads, Databricks recommends the Postgres API equivalent: `List projects
        <https://docs.databricks.com/api/postgres/v1/list-projects>`__.

        :param page_size: int (optional)
          Upper bound for items returned. Defaults to 100, which is also the maximum value.
        :param page_token: str (optional)
          Pagination token to go to the next page of Database Instances. Requests first page if absent.

        :returns: Iterator over :class:`DatabaseInstance`
        

    .. py:method:: list_synced_database_tables(instance_name: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SyncedDatabaseTable]

        List synced database tables in a Database Instance.

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
          The name of the catalog in Unity Catalog.
        :param database_catalog: :class:`DatabaseCatalog`
          Note that updating a database catalog is not yet supported.
        :param update_mask: str
          The list of fields to update. Setting this field is not yet supported.

        :returns: :class:`DatabaseCatalog`
        

    .. py:method:: update_database_instance(name: str, database_instance: DatabaseInstance, update_mask: str) -> DatabaseInstance

        Update a Database Instance.

        For new workloads, Databricks recommends the Postgres API equivalents: `Update a project
        <https://docs.databricks.com/api/postgres/v1/update-project>`__ and `Update an endpoint
        <https://docs.databricks.com/api/postgres/v1/update-endpoint>`__.

        :param name: str
          The name of the instance. This is the unique identifier for the instance. Must be 1 to 63 characters
          long, contain only letters, digits and hyphens, start with a letter, and not contain consecutive
          hyphens.
        :param database_instance: :class:`DatabaseInstance`
          Specifies the instance to update, identified by its name.
        :param update_mask: str
          The list of fields to update. If unspecified, all fields will be updated when possible. Use "*" to
          update every field. To wipe out custom_tags, specify custom_tags in the update_mask with an empty
          custom_tags list.

        :returns: :class:`DatabaseInstance`
        

    .. py:method:: update_synced_database_table(name: str, synced_table: SyncedDatabaseTable, update_mask: str) -> SyncedDatabaseTable

        This API is currently unimplemented, but exposed for Terraform support.

        :param name: str
          Full three-part (catalog, schema, table) name of the table.
        :param synced_table: :class:`SyncedDatabaseTable`
          The synced database table and requested spec values.
        :param update_mask: str
          The list of fields to update. Updatable paths include spec.accelerated_sync and *.

        :returns: :class:`SyncedDatabaseTable`
        

    .. py:method:: wait_get_database_instance_database_available(name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[DatabaseInstance], None]]) -> DatabaseInstance

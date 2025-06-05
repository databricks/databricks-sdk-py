``w.database``: Database Instances
==================================
.. currentmodule:: databricks.sdk.service.database

.. py:class:: DatabaseAPI

    Database Instances provide access to a database via REST API or direct SQL.

    .. py:method:: create_database_catalog(catalog: DatabaseCatalog) -> DatabaseCatalog

        Create a Database Catalog.
        
        :param catalog: :class:`DatabaseCatalog`
        
        :returns: :class:`DatabaseCatalog`
        

    .. py:method:: create_database_instance(database_instance: DatabaseInstance) -> DatabaseInstance

        Create a Database Instance.
        
        :param database_instance: :class:`DatabaseInstance`
          A DatabaseInstance represents a logical Postgres instance, comprised of both compute and storage.
        
        :returns: :class:`DatabaseInstance`
        

    .. py:method:: create_database_table(table: DatabaseTable) -> DatabaseTable

        Create a Database Table.
        
        :param table: :class:`DatabaseTable`
          Next field marker: 13
        
        :returns: :class:`DatabaseTable`
        

    .. py:method:: create_synced_database_table(synced_table: SyncedDatabaseTable) -> SyncedDatabaseTable

        Create a Synced Database Table.
        
        :param synced_table: :class:`SyncedDatabaseTable`
          Next field marker: 12
        
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
          If false, the database instance is soft deleted. Soft deleted instances behave as if they are
          deleted, and cannot be used for CRUD operations nor connected to. However they can be undeleted by
          calling the undelete API for a limited time. If true, the database instance is hard deleted and
          cannot be undeleted.
        
        
        

    .. py:method:: delete_database_table(name: str)

        Delete a Database Table.
        
        :param name: str
        
        
        

    .. py:method:: delete_synced_database_table(name: str)

        Delete a Synced Database Table.
        
        :param name: str
        
        
        

    .. py:method:: find_database_instance_by_uid( [, uid: Optional[str]]) -> DatabaseInstance

        Find a Database Instance by uid.
        
        :param uid: str (optional)
          UID of the cluster to get.
        
        :returns: :class:`DatabaseInstance`
        

    .. py:method:: generate_database_credential( [, instance_names: Optional[List[str]], request_id: Optional[str]]) -> DatabaseCredential

        Generates a credential that can be used to access database instances.
        
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
        

    .. py:method:: get_database_table(name: str) -> DatabaseTable

        Get a Database Table.
        
        :param name: str
        
        :returns: :class:`DatabaseTable`
        

    .. py:method:: get_synced_database_table(name: str) -> SyncedDatabaseTable

        Get a Synced Database Table.
        
        :param name: str
        
        :returns: :class:`SyncedDatabaseTable`
        

    .. py:method:: list_database_instances( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DatabaseInstance]

        List Database Instances.
        
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Database Instances. Requests first page if absent.
        
        :returns: Iterator over :class:`DatabaseInstance`
        

    .. py:method:: update_database_instance(name: str, database_instance: DatabaseInstance, update_mask: str) -> DatabaseInstance

        Update a Database Instance.
        
        :param name: str
          The name of the instance. This is the unique identifier for the instance.
        :param database_instance: :class:`DatabaseInstance`
          A DatabaseInstance represents a logical Postgres instance, comprised of both compute and storage.
        :param update_mask: str
          The list of fields to update.
        
        :returns: :class:`DatabaseInstance`
        
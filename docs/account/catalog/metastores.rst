``a.metastores``: Account Metastores
====================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: AccountMetastoresAPI

    These APIs manage Unity Catalog metastores for an account. A metastore contains catalogs that can be
    associated with workspaces

    .. py:method:: create( [, metastore_info: Optional[CreateMetastore]]) -> AccountsMetastoreInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.metastores.create(name=f'sdk-{time.time_ns()}',
                                          storage_root="s3://%s/%s" %
                                          (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))
            
            # cleanup
            w.metastores.delete(id=created.metastore_id, force=True)

        Create metastore.
        
        Creates a Unity Catalog metastore.
        
        :param metastore_info: :class:`CreateMetastore` (optional)
        
        :returns: :class:`AccountsMetastoreInfo`
        

    .. py:method:: delete(metastore_id: str [, force: Optional[bool]])

        Delete a metastore.
        
        Deletes a Unity Catalog metastore for an account, both specified by ID.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param force: bool (optional)
          Force deletion even if the metastore is not empty. Default is false.
        
        
        

    .. py:method:: get(metastore_id: str) -> AccountsMetastoreInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.metastores.create(name=f'sdk-{time.time_ns()}',
                                          storage_root="s3://%s/%s" %
                                          (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))
            
            _ = w.metastores.get(id=created.metastore_id)
            
            # cleanup
            w.metastores.delete(id=created.metastore_id, force=True)

        Get a metastore.
        
        Gets a Unity Catalog metastore from an account, both specified by ID.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        
        :returns: :class:`AccountsMetastoreInfo`
        

    .. py:method:: list() -> Iterator[MetastoreInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.metastores.list()

        Get all metastores associated with an account.
        
        Gets all Unity Catalog metastores associated with an account specified by ID.
        
        :returns: Iterator over :class:`MetastoreInfo`
        

    .. py:method:: update(metastore_id: str [, metastore_info: Optional[UpdateMetastore]]) -> AccountsMetastoreInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.metastores.create(name=f'sdk-{time.time_ns()}',
                                          storage_root="s3://%s/%s" %
                                          (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))
            
            _ = w.metastores.update(id=created.metastore_id, new_name=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.metastores.delete(id=created.metastore_id, force=True)

        Update a metastore.
        
        Updates an existing Unity Catalog metastore.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param metastore_info: :class:`UpdateMetastore` (optional)
        
        :returns: :class:`AccountsMetastoreInfo`
        
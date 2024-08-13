``w.shares``: Shares
====================
.. currentmodule:: databricks.sdk.service.sharing

.. py:class:: SharesAPI

    A share is a container instantiated with :method:shares/create. Once created you can iteratively register
    a collection of existing data assets defined within the metastore using :method:shares/update. You can
    register data assets under their original name, qualified by their original schema, or provide alternate
    exposed names.

    .. py:method:: create(name: str [, comment: Optional[str], storage_root: Optional[str]]) -> ShareInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created_share = w.shares.create(name=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.shares.delete(name=created_share.name)

        Create a share.
        
        Creates a new share for data objects. Data objects can be added after creation with **update**. The
        caller must be a metastore admin or have the **CREATE_SHARE** privilege on the metastore.
        
        :param name: str
          Name of the share.
        :param comment: str (optional)
          User-provided free-form text description.
        :param storage_root: str (optional)
          Storage root URL for the share.
        
        :returns: :class:`ShareInfo`
        

    .. py:method:: delete(name: str)

        Delete a share.
        
        Deletes a data object share from the metastore. The caller must be an owner of the share.
        
        :param name: str
          The name of the share.
        
        
        

    .. py:method:: get(name: str [, include_shared_data: Optional[bool]]) -> ShareInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created_share = w.shares.create(name=f'sdk-{time.time_ns()}')
            
            _ = w.shares.get(name=created_share.name)
            
            # cleanup
            w.shares.delete(name=created_share.name)

        Get a share.
        
        Gets a data object share from the metastore. The caller must be a metastore admin or the owner of the
        share.
        
        :param name: str
          The name of the share.
        :param include_shared_data: bool (optional)
          Query for data to include in the share.
        
        :returns: :class:`ShareInfo`
        

    .. py:method:: list( [, max_results: Optional[int], page_token: Optional[str]]) -> Iterator[ShareInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sharing
            
            w = WorkspaceClient()
            
            all = w.shares.list(sharing.ListSharesRequest())

        List shares.
        
        Gets an array of data object shares from the metastore. The caller must be a metastore admin or the
        owner of the share. There is no guarantee of a specific ordering of the elements in the array.
        
        :param max_results: int (optional)
          Maximum number of shares to return. - when set to 0, the page length is set to a server configured
          value (recommended); - when set to a value greater than 0, the page length is the minimum of this
          value and a server configured value; - when set to a value less than 0, an invalid parameter error
          is returned; - If not set, all valid shares are returned (not recommended). - Note: The number of
          returned shares might be less than the specified max_results size, even zero. The only definitive
          indication that no further shares can be fetched is when the next_page_token is unset from the
          response.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`ShareInfo`
        

    .. py:method:: share_permissions(name: str [, max_results: Optional[int], page_token: Optional[str]]) -> catalog.PermissionsList

        Get permissions.
        
        Gets the permissions for a data share from the metastore. The caller must be a metastore admin or the
        owner of the share.
        
        :param name: str
          The name of the share.
        :param max_results: int (optional)
          Maximum number of permissions to return. - when set to 0, the page length is set to a server
          configured value (recommended); - when set to a value greater than 0, the page length is the minimum
          of this value and a server configured value; - when set to a value less than 0, an invalid parameter
          error is returned; - If not set, all valid permissions are returned (not recommended). - Note: The
          number of returned permissions might be less than the specified max_results size, even zero. The
          only definitive indication that no further permissions can be fetched is when the next_page_token is
          unset from the response.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: :class:`PermissionsList`
        

    .. py:method:: update(name: str [, comment: Optional[str], new_name: Optional[str], owner: Optional[str], storage_root: Optional[str], updates: Optional[List[SharedDataObjectUpdate]]]) -> ShareInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sharing
            
            w = WorkspaceClient()
            
            table_name = f'sdk-{time.time_ns()}'
            
            created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)
            
            _ = w.statement_execution.execute(
                warehouse_id=os.environ["TEST_DEFAULT_WAREHOUSE_ID"],
                catalog=created_catalog.name,
                schema=created_schema.name,
                statement="CREATE TABLE %s TBLPROPERTIES (delta.enableDeletionVectors=false) AS SELECT 2+2 as four" %
                (table_name)).result()
            
            table_full_name = "%s.%s.%s" % (created_catalog.name, created_schema.name, table_name)
            
            created_share = w.shares.create(name=f'sdk-{time.time_ns()}')
            
            _ = w.shares.update(name=created_share.name,
                                updates=[
                                    sharing.SharedDataObjectUpdate(action=sharing.SharedDataObjectUpdateAction.ADD,
                                                                   data_object=sharing.SharedDataObject(
                                                                       name=table_full_name, data_object_type="TABLE"))
                                ])
            
            # cleanup
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)
            w.tables.delete(full_name=table_full_name)
            w.shares.delete(name=created_share.name)

        Update a share.
        
        Updates the share with the changes and data objects in the request. The caller must be the owner of
        the share or a metastore admin.
        
        When the caller is a metastore admin, only the __owner__ field can be updated.
        
        In the case that the share name is changed, **updateShare** requires that the caller is both the share
        owner and a metastore admin.
        
        If there are notebook files in the share, the __storage_root__ field cannot be updated.
        
        For each table that is added through this method, the share owner must also have **SELECT** privilege
        on the table. This privilege must be maintained indefinitely for recipients to be able to access the
        table. Typically, you should use a group as the share owner.
        
        Table removals through **update** do not require additional privileges.
        
        :param name: str
          The name of the share.
        :param comment: str (optional)
          User-provided free-form text description.
        :param new_name: str (optional)
          New name for the share.
        :param owner: str (optional)
          Username of current owner of share.
        :param storage_root: str (optional)
          Storage root URL for the share.
        :param updates: List[:class:`SharedDataObjectUpdate`] (optional)
          Array of shared data object updates.
        
        :returns: :class:`ShareInfo`
        

    .. py:method:: update_permissions(name: str [, changes: Optional[List[catalog.PermissionsChange]], max_results: Optional[int], page_token: Optional[str]])

        Update permissions.
        
        Updates the permissions for a data share in the metastore. The caller must be a metastore admin or an
        owner of the share.
        
        For new recipient grants, the user must also be the owner of the recipients. recipient revocations do
        not require additional privileges.
        
        :param name: str
          The name of the share.
        :param changes: List[:class:`PermissionsChange`] (optional)
          Array of permission changes.
        :param max_results: int (optional)
          Maximum number of permissions to return. - when set to 0, the page length is set to a server
          configured value (recommended); - when set to a value greater than 0, the page length is the minimum
          of this value and a server configured value; - when set to a value less than 0, an invalid parameter
          error is returned; - If not set, all valid permissions are returned (not recommended). - Note: The
          number of returned permissions might be less than the specified max_results size, even zero. The
          only definitive indication that no further permissions can be fetched is when the next_page_token is
          unset from the response.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        
        
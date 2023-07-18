Metastores
==========
.. py:class:: MetastoresAPI

    A metastore is the top-level container of objects in Unity Catalog. It stores data assets (tables and
    views) and the permissions that govern access to them. Databricks account admins can create metastores and
    assign them to Databricks workspaces to control which workloads use each metastore. For a workspace to use
    Unity Catalog, it must have a Unity Catalog metastore attached.
    
    Each metastore is configured with a root storage location in a cloud storage account. This storage
    location is used for metadata and managed tables data.
    
    NOTE: This metastore is distinct from the metastore included in Databricks workspaces created before Unity
    Catalog was released. If your workspace includes a legacy Hive metastore, the data in that metastore is
    available in a catalog named hive_metastore.

    .. py:method:: assign(metastore_id, default_catalog_name, workspace_id)

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            workspace_id = os.environ["TEST_WORKSPACE_ID"]
            
            created = w.metastores.create(name=f'sdk-{time.time_ns()}',
                                          storage_root="s3://%s/%s" %
                                          (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))
            
            w.metastores.assign(metastore_id=created.metastore_id, workspace_id=workspace_id)
            
            # cleanup
            w.metastores.delete(id=created.metastore_id, force=True)

        Create an assignment.
        
        Creates a new metastore assignment. If an assignment for the same __workspace_id__ exists, it will be
        overwritten by the new __metastore_id__ and __default_catalog_name__. The caller must be an account
        admin.
        
        :param metastore_id: str
          The unique ID of the metastore.
        :param default_catalog_name: str
          The name of the default catalog in the metastore.
        :param workspace_id: int
          A workspace ID.
        
        
        

    .. py:method:: create(name, storage_root [, region])

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

        Create a metastore.
        
        Creates a new metastore based on a provided name and storage root path.
        
        :param name: str
          The user-specified name of the metastore.
        :param storage_root: str
          The storage root URL for metastore
        :param region: str (optional)
          Cloud region which the metastore serves (e.g., `us-west-2`, `westus`). If this field is omitted, the
          region of the workspace receiving the request will be used.
        
        :returns: :class:`MetastoreInfo`
        

    .. py:method:: current()

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            current_metastore = w.metastores.current()

        Get metastore assignment for workspace.
        
        Gets the metastore assignment for the workspace being accessed.
        
        :returns: :class:`MetastoreAssignment`
        

    .. py:method:: delete(id [, force])

        Delete a metastore.
        
        Deletes a metastore. The caller must be a metastore admin.
        
        :param id: str
          Unique ID of the metastore.
        :param force: bool (optional)
          Force deletion even if the metastore is not empty. Default is false.
        
        
        

    .. py:method:: enable_optimization(metastore_id, enable)

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.metastores.create(name=f'sdk-{time.time_ns()}',
                                          storage_root="s3://%s/%s" %
                                          (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))
            
            auto_maintenance = w.metastores.enable_optimization(enable=True, metastore_id=created.metastore_id)
            
            # cleanup
            w.metastores.delete(id=created.metastore_id, force=True)

        Toggle predictive optimization on the metastore.
        
        Enables or disables predictive optimization on the metastore.
        
        :param metastore_id: str
          Unique identifier of metastore.
        :param enable: bool
          Whether to enable predictive optimization on the metastore.
        
        :returns: :class:`UpdatePredictiveOptimizationResponse`
        

    .. py:method:: get(id)

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.metastores.create(name=f'sdk-{time.time_ns()}',
                                          storage_root="s3://%s/%s" %
                                          (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))
            
            _ = w.metastores.get(get=created.metastore_id)
            
            # cleanup
            w.metastores.delete(id=created.metastore_id, force=True)

        Get a metastore.
        
        Gets a metastore that matches the supplied ID. The caller must be a metastore admin to retrieve this
        info.
        
        :param id: str
          Unique ID of the metastore.
        
        :returns: :class:`MetastoreInfo`
        

    .. py:method:: list()

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.metastores.list()

        List metastores.
        
        Gets an array of the available metastores (as __MetastoreInfo__ objects). The caller must be an admin
        to retrieve this info. There is no guarantee of a specific ordering of the elements in the array.
        
        :returns: Iterator over :class:`MetastoreInfo`
        

    .. py:method:: summary()

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            summary = w.metastores.summary()

        Get a metastore summary.
        
        Gets information about a metastore. This summary includes the storage credential, the cloud vendor,
        the cloud region, and the global metastore ID.
        
        :returns: :class:`GetMetastoreSummaryResponse`
        

    .. py:method:: unassign(workspace_id, metastore_id)

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            workspace_id = os.environ["TEST_WORKSPACE_ID"]
            
            created = w.metastores.create(name=f'sdk-{time.time_ns()}',
                                          storage_root="s3://%s/%s" %
                                          (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))
            
            w.metastores.unassign(metastore_id=created.metastore_id, workspace_id=workspace_id)
            
            # cleanup
            w.metastores.delete(id=created.metastore_id, force=True)

        Delete an assignment.
        
        Deletes a metastore assignment. The caller must be an account administrator.
        
        :param workspace_id: int
          A workspace ID.
        :param metastore_id: str
          Query for the ID of the metastore to delete.
        
        
        

    .. py:method:: update(id [, delta_sharing_organization_name, delta_sharing_recipient_token_lifetime_in_seconds, delta_sharing_scope, name, owner, privilege_model_version, storage_root_credential_id])

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.metastores.create(name=f'sdk-{time.time_ns()}',
                                          storage_root="s3://%s/%s" %
                                          (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))
            
            _ = w.metastores.update(id=created.metastore_id, name=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.metastores.delete(id=created.metastore_id, force=True)

        Update a metastore.
        
        Updates information for a specific metastore. The caller must be a metastore admin.
        
        :param id: str
          Unique ID of the metastore.
        :param delta_sharing_organization_name: str (optional)
          The organization name of a Delta Sharing entity, to be used in Databricks-to-Databricks Delta
          Sharing as the official name.
        :param delta_sharing_recipient_token_lifetime_in_seconds: int (optional)
          The lifetime of delta sharing recipient token in seconds.
        :param delta_sharing_scope: :class:`UpdateMetastoreDeltaSharingScope` (optional)
          The scope of Delta Sharing enabled for the metastore.
        :param name: str (optional)
          The user-specified name of the metastore.
        :param owner: str (optional)
          The owner of the metastore.
        :param privilege_model_version: str (optional)
          Privilege model version of the metastore, of the form `major.minor` (e.g., `1.0`).
        :param storage_root_credential_id: str (optional)
          UUID of storage credential to access the metastore storage_root.
        
        :returns: :class:`MetastoreInfo`
        

    .. py:method:: update_assignment(workspace_id [, default_catalog_name, metastore_id])

        Update an assignment.
        
        Updates a metastore assignment. This operation can be used to update __metastore_id__ or
        __default_catalog_name__ for a specified Workspace, if the Workspace is already assigned a metastore.
        The caller must be an account admin to update __metastore_id__; otherwise, the caller can be a
        Workspace admin.
        
        :param workspace_id: int
          A workspace ID.
        :param default_catalog_name: str (optional)
          The name of the default catalog for the metastore.
        :param metastore_id: str (optional)
          The unique ID of the metastore.
        
        
        
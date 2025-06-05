``w.grants``: Grants
====================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: GrantsAPI

    In Unity Catalog, data is secure by default. Initially, users have no access to data in a metastore.
    Access can be granted by either a metastore admin, the owner of an object, or the owner of the catalog or
    schema that contains the object. Securable objects in Unity Catalog are hierarchical and privileges are
    inherited downward.
    
    Securable objects in Unity Catalog are hierarchical and privileges are inherited downward. This means that
    granting a privilege on the catalog automatically grants the privilege to all current and future objects
    within the catalog. Similarly, privileges granted on a schema are inherited by all current and future
    objects within that schema.

    .. py:method:: get(securable_type: str, full_name: str [, max_results: Optional[int], page_token: Optional[str], principal: Optional[str]]) -> GetPermissionsResponse


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            table_name = f"sdk-{time.time_ns()}"
            
            created_catalog = w.catalogs.create(name=f"sdk-{time.time_ns()}")
            
            created_schema = w.schemas.create(name=f"sdk-{time.time_ns()}", catalog_name=created_catalog.name)
            
            _ = w.statement_execution.execute(
                warehouse_id=os.environ["TEST_DEFAULT_WAREHOUSE_ID"],
                catalog=created_catalog.name,
                schema=created_schema.name,
                statement="CREATE TABLE %s AS SELECT 2+2 as four" % (table_name),
            ).result()
            
            table_full_name = "%s.%s.%s" % (
                created_catalog.name,
                created_schema.name,
                table_name,
            )
            
            created_table = w.tables.get(full_name=table_full_name)
            
            grants = w.grants.get_effective(
                securable_type=catalog.SecurableType.TABLE,
                full_name=created_table.full_name,
            )
            
            # cleanup
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)
            w.tables.delete(full_name=table_full_name)

        Get permissions.
        
        Gets the permissions for a securable. Does not include inherited permissions.
        
        :param securable_type: str
          Type of securable.
        :param full_name: str
          Full name of securable.
        :param max_results: int (optional)
          Specifies the maximum number of privileges to return (page length). Every PrivilegeAssignment
          present in a single page response is guaranteed to contain all the privileges granted on the
          requested Securable for the respective principal.
          
          If not set, all the permissions are returned. If set to - lesser than 0: invalid parameter error -
          0: page length is set to a server configured value - lesser than 150 but greater than 0: invalid
          parameter error (this is to ensure that server is able to return at least one complete
          PrivilegeAssignment in a single page response) - greater than (or equal to) 150: page length is the
          minimum of this value and a server configured value
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        :param principal: str (optional)
          If provided, only the permissions for the specified principal (user or group) are returned.
        
        :returns: :class:`GetPermissionsResponse`
        

    .. py:method:: get_effective(securable_type: str, full_name: str [, max_results: Optional[int], page_token: Optional[str], principal: Optional[str]]) -> EffectivePermissionsList


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            table_name = f"sdk-{time.time_ns()}"
            
            created_catalog = w.catalogs.create(name=f"sdk-{time.time_ns()}")
            
            created_schema = w.schemas.create(name=f"sdk-{time.time_ns()}", catalog_name=created_catalog.name)
            
            _ = w.statement_execution.execute(
                warehouse_id=os.environ["TEST_DEFAULT_WAREHOUSE_ID"],
                catalog=created_catalog.name,
                schema=created_schema.name,
                statement="CREATE TABLE %s AS SELECT 2+2 as four" % (table_name),
            ).result()
            
            table_full_name = "%s.%s.%s" % (
                created_catalog.name,
                created_schema.name,
                table_name,
            )
            
            created_table = w.tables.get(full_name=table_full_name)
            
            grants = w.grants.get_effective(
                securable_type=catalog.SecurableType.TABLE,
                full_name=created_table.full_name,
            )
            
            # cleanup
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)
            w.tables.delete(full_name=table_full_name)

        Get effective permissions.
        
        Gets the effective permissions for a securable. Includes inherited permissions from any parent
        securables.
        
        :param securable_type: str
          Type of securable.
        :param full_name: str
          Full name of securable.
        :param max_results: int (optional)
          Specifies the maximum number of privileges to return (page length). Every
          EffectivePrivilegeAssignment present in a single page response is guaranteed to contain all the
          effective privileges granted on (or inherited by) the requested Securable for the respective
          principal.
          
          If not set, all the effective permissions are returned. If set to - lesser than 0: invalid parameter
          error - 0: page length is set to a server configured value - lesser than 150 but greater than 0:
          invalid parameter error (this is to ensure that server is able to return at least one complete
          EffectivePrivilegeAssignment in a single page response) - greater than (or equal to) 150: page
          length is the minimum of this value and a server configured value
        :param page_token: str (optional)
          Opaque token for the next page of results (pagination).
        :param principal: str (optional)
          If provided, only the effective permissions for the specified principal (user or group) are
          returned.
        
        :returns: :class:`EffectivePermissionsList`
        

    .. py:method:: update(securable_type: str, full_name: str [, changes: Optional[List[PermissionsChange]]]) -> UpdatePermissionsResponse


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            table_name = f"sdk-{time.time_ns()}"
            
            created_catalog = w.catalogs.create(name=f"sdk-{time.time_ns()}")
            
            created_schema = w.schemas.create(name=f"sdk-{time.time_ns()}", catalog_name=created_catalog.name)
            
            _ = w.statement_execution.execute(
                warehouse_id=os.environ["TEST_DEFAULT_WAREHOUSE_ID"],
                catalog=created_catalog.name,
                schema=created_schema.name,
                statement="CREATE TABLE %s AS SELECT 2+2 as four" % (table_name),
            ).result()
            
            table_full_name = "%s.%s.%s" % (
                created_catalog.name,
                created_schema.name,
                table_name,
            )
            
            account_level_group_name = os.environ["TEST_DATA_ENG_GROUP"]
            
            created_table = w.tables.get(full_name=table_full_name)
            
            x = w.grants.update(
                full_name=created_table.full_name,
                securable_type=catalog.SecurableType.TABLE,
                changes=[
                    catalog.PermissionsChange(
                        add=[catalog.Privilege.MODIFY, catalog.Privilege.SELECT],
                        principal=account_level_group_name,
                    )
                ],
            )
            
            # cleanup
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)
            w.tables.delete(full_name=table_full_name)

        Update permissions.
        
        Updates the permissions for a securable.
        
        :param securable_type: str
          Type of securable.
        :param full_name: str
          Full name of securable.
        :param changes: List[:class:`PermissionsChange`] (optional)
          Array of permissions change objects.
        
        :returns: :class:`UpdatePermissionsResponse`
        
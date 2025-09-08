``w.permission_migration``: PermissionMigration
===============================================
.. currentmodule:: databricks.sdk.service.iam

.. py:class:: PermissionMigrationAPI

    APIs for migrating acl permissions, used only by the ucx tool: https://github.com/databrickslabs/ucx

    .. py:method:: migrate_permissions(workspace_id: int, from_workspace_group_name: str, to_account_group_name: str [, size: Optional[int]]) -> MigratePermissionsResponse

        Migrate Permissions.
        
        :param workspace_id: int
          WorkspaceId of the associated workspace where the permission migration will occur.
        :param from_workspace_group_name: str
          The name of the workspace group that permissions will be migrated from.
        :param to_account_group_name: str
          The name of the account group that permissions will be migrated to.
        :param size: int (optional)
          The maximum number of permissions that will be migrated.
        
        :returns: :class:`MigratePermissionsResponse`
        
``a.workspace_assignment``: Workspace Assignment
================================================
.. currentmodule:: databricks.sdk.service.iam

.. py:class:: WorkspaceAssignmentAPI

    The Workspace Permission Assignment API allows you to manage workspace permissions for principals in your
    account.

    .. py:method:: delete(workspace_id: int, principal_id: int)

        Delete permissions assignment.
        
        Deletes the workspace permissions assignment in a given account and workspace for the specified
        principal.
        
        :param workspace_id: int
          The workspace ID.
        :param principal_id: int
          The ID of the user, service principal, or group.
        
        
        

    .. py:method:: get(workspace_id: int) -> WorkspacePermissions

        List workspace permissions.
        
        Get an array of workspace permissions for the specified account and workspace.
        
        :param workspace_id: int
          The workspace ID.
        
        :returns: :class:`WorkspacePermissions`
        

    .. py:method:: list(workspace_id: int) -> Iterator[PermissionAssignment]


        Usage:

        .. code-block::

            import os
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            workspace_id = os.environ["TEST_WORKSPACE_ID"]
            
            all = a.workspace_assignment.list(list=workspace_id)

        Get permission assignments.
        
        Get the permission assignments for the specified Databricks account and Databricks workspace.
        
        :param workspace_id: int
          The workspace ID for the account.
        
        :returns: Iterator over :class:`PermissionAssignment`
        

    .. py:method:: update(workspace_id: int, principal_id: int, permissions: List[WorkspacePermission]) -> PermissionAssignment


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import iam
            
            a = AccountClient()
            
            spn = a.service_principals.create(display_name=f'sdk-{time.time_ns()}')
            
            spn_id = spn.id
            
            workspace_id = os.environ["DUMMY_WORKSPACE_ID"]
            
            a.workspace_assignment.update(workspace_id=workspace_id,
                                          principal_id=spn_id,
                                          permissions=[iam.WorkspacePermission.USER])

        Create or update permissions assignment.
        
        Creates or updates the workspace permissions assignment in a given account and workspace for the
        specified principal.
        
        :param workspace_id: int
          The workspace ID.
        :param principal_id: int
          The ID of the user, service principal, or group.
        :param permissions: List[:class:`WorkspacePermission`]
          Array of permissions assignments to update on the workspace. Note that excluding this field will
          have the same effect as providing an empty list which will result in the deletion of all permissions
          for the principal.
        
        :returns: :class:`PermissionAssignment`
        
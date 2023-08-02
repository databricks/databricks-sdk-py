Permissions
===========
.. py:class:: PermissionsAPI

    Permissions API are used to create read, write, edit, update and manage access for various users on
    different objects and endpoints.

    .. py:method:: get(request_object_type, request_object_id)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            obj = w.workspace.get_status(path=notebook_path)
            
            levels = w.permissions.get_permission_levels(request_object_type="notebooks",
                                                         request_object_id="%d" % (obj.object_id))

        Get object permissions.
        
        Gets the permission of an object. Objects can inherit permissions from their parent objects or root
        objects.
        
        :param request_object_type: str
          <needs content>
        :param request_object_id: str
        
        :returns: :class:`ObjectPermissions`
        

    .. py:method:: get_permission_levels(request_object_type, request_object_id)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            obj = w.workspace.get_status(path=notebook_path)
            
            levels = w.permissions.get_permission_levels(request_object_type="notebooks",
                                                         request_object_id="%d" % (obj.object_id))

        Get permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param request_object_type: str
          <needs content>
        :param request_object_id: str
          <needs content>
        
        :returns: :class:`GetPermissionLevelsResponse`
        

    .. py:method:: set(request_object_type, request_object_id [, access_control_list])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import iam
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            group = w.groups.create(display_name=f'sdk-{time.time_ns()}')
            
            obj = w.workspace.get_status(path=notebook_path)
            
            _ = w.permissions.set(request_object_type="notebooks",
                                  request_object_id="%d" % (obj.object_id),
                                  access_control_list=[
                                      iam.AccessControlRequest(group_name=group.display_name,
                                                               permission_level=iam.PermissionLevel.CAN_RUN)
                                  ])
            
            # cleanup
            w.groups.delete(id=group.id)

        Set permissions.
        
        Sets permissions on object. Objects can inherit permissions from their parent objects and root
        objects.
        
        :param request_object_type: str
          <needs content>
        :param request_object_id: str
        :param access_control_list: List[:class:`AccessControlRequest`] (optional)
        
        
        

    .. py:method:: update(request_object_type, request_object_id [, access_control_list])

        Update permission.
        
        Updates the permissions on an object.
        
        :param request_object_type: str
          <needs content>
        :param request_object_id: str
        :param access_control_list: List[:class:`AccessControlRequest`] (optional)
        
        
        
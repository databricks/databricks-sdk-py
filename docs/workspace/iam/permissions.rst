``w.permissions``: Permissions
==============================
.. currentmodule:: databricks.sdk.service.iam

.. py:class:: PermissionsAPI

    Permissions API are used to create read, write, edit, update and manage access for various users on
    different objects and endpoints.
    
    * **[Apps permissions](:service:apps)** — Manage which users can manage or use apps.
    
    * **[Cluster permissions](:service:clusters)** — Manage which users can manage, restart, or attach to
    clusters.
    
    * **[Cluster policy permissions](:service:clusterpolicies)** — Manage which users can use cluster
    policies.
    
    * **[Delta Live Tables pipeline permissions](:service:pipelines)** — Manage which users can view,
    manage, run, cancel, or own a Delta Live Tables pipeline.
    
    * **[Job permissions](:service:jobs)** — Manage which users can view, manage, trigger, cancel, or own a
    job.
    
    * **[MLflow experiment permissions](:service:experiments)** — Manage which users can read, edit, or
    manage MLflow experiments.
    
    * **[MLflow registered model permissions](:service:modelregistry)** — Manage which users can read, edit,
    or manage MLflow registered models.
    
    * **[Password permissions](:service:users)** — Manage which users can use password login when SSO is
    enabled.
    
    * **[Instance Pool permissions](:service:instancepools)** — Manage which users can manage or attach to
    pools.
    
    * **[Repo permissions](repos)** — Manage which users can read, run, edit, or manage a repo.
    
    * **[Serving endpoint permissions](:service:servingendpoints)** — Manage which users can view, query, or
    manage a serving endpoint.
    
    * **[SQL warehouse permissions](:service:warehouses)** — Manage which users can use or manage SQL
    warehouses.
    
    * **[Token permissions](:service:tokenmanagement)** — Manage which users can create or use tokens.
    
    * **[Workspace object permissions](:service:workspace)** — Manage which users can read, run, edit, or
    manage alerts, dbsql-dashboards, directories, files, notebooks and queries.
    
    For the mapping of the required permissions for specific actions or abilities and other important
    information, see [Access Control].
    
    Note that to manage access control on service principals, use **[Account Access Control
    Proxy](:service:accountaccesscontrolproxy)**.
    
    [Access Control]: https://docs.databricks.com/security/auth-authz/access-control/index.html

    .. py:method:: get(request_object_type: str, request_object_id: str) -> ObjectPermissions


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
        
        Gets the permissions of an object. Objects can inherit permissions from their parent objects or root
        object.
        
        :param request_object_type: str
          The type of the request object. Can be one of the following: alerts, authorization, clusters,
          cluster-policies, dashboards, dbsql-dashboards, directories, experiments, files, instance-pools,
          jobs, notebooks, pipelines, queries, registered-models, repos, serving-endpoints, or warehouses.
        :param request_object_id: str
          The id of the request object.
        
        :returns: :class:`ObjectPermissions`
        

    .. py:method:: get_permission_levels(request_object_type: str, request_object_id: str) -> GetPermissionLevelsResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            obj = w.workspace.get_status(path=notebook_path)
            
            levels = w.permissions.get_permission_levels(request_object_type="notebooks",
                                                         request_object_id="%d" % (obj.object_id))

        Get object permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param request_object_type: str
          <needs content>
        :param request_object_id: str
          <needs content>
        
        :returns: :class:`GetPermissionLevelsResponse`
        

    .. py:method:: set(request_object_type: str, request_object_id: str [, access_control_list: Optional[List[AccessControlRequest]]]) -> ObjectPermissions


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

        Set object permissions.
        
        Sets permissions on an object. Objects can inherit permissions from their parent objects or root
        object.
        
        :param request_object_type: str
          The type of the request object. Can be one of the following: alerts, authorization, clusters,
          cluster-policies, dashboards, dbsql-dashboards, directories, experiments, files, instance-pools,
          jobs, notebooks, pipelines, queries, registered-models, repos, serving-endpoints, or warehouses.
        :param request_object_id: str
          The id of the request object.
        :param access_control_list: List[:class:`AccessControlRequest`] (optional)
        
        :returns: :class:`ObjectPermissions`
        

    .. py:method:: update(request_object_type: str, request_object_id: str [, access_control_list: Optional[List[AccessControlRequest]]]) -> ObjectPermissions

        Update object permissions.
        
        Updates the permissions on an object. Objects can inherit permissions from their parent objects or
        root object.
        
        :param request_object_type: str
          The type of the request object. Can be one of the following: alerts, authorization, clusters,
          cluster-policies, dashboards, dbsql-dashboards, directories, experiments, files, instance-pools,
          jobs, notebooks, pipelines, queries, registered-models, repos, serving-endpoints, or warehouses.
        :param request_object_id: str
          The id of the request object.
        :param access_control_list: List[:class:`AccessControlRequest`] (optional)
        
        :returns: :class:`ObjectPermissions`
        
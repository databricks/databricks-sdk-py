``w.apps``: Apps
================
.. currentmodule:: databricks.sdk.service.apps

.. py:class:: AppsAPI

    Apps run directly on a customer’s Databricks instance, integrate with their data, use and extend
    Databricks services, and enable users to interact through single sign-on.

    .. py:method:: create( [, app: Optional[App], no_compute: Optional[bool]]) -> Wait[App]

        Create an app.
        
        Creates a new app.
        
        :param app: :class:`App` (optional)
        :param no_compute: bool (optional)
          If true, the app will not be started after creation.
        
        :returns:
          Long-running operation waiter for :class:`App`.
          See :method:wait_get_app_active for more details.
        

    .. py:method:: create_and_wait( [, app: Optional[App], no_compute: Optional[bool], timeout: datetime.timedelta = 0:20:00]) -> App


    .. py:method:: delete(name: str) -> App

        Delete an app.
        
        Deletes an app.
        
        :param name: str
          The name of the app.
        
        :returns: :class:`App`
        

    .. py:method:: deploy(app_name: str [, app_deployment: Optional[AppDeployment]]) -> Wait[AppDeployment]

        Create an app deployment.
        
        Creates an app deployment for the app with the supplied name.
        
        :param app_name: str
          The name of the app.
        :param app_deployment: :class:`AppDeployment` (optional)
        
        :returns:
          Long-running operation waiter for :class:`AppDeployment`.
          See :method:wait_get_deployment_app_succeeded for more details.
        

    .. py:method:: deploy_and_wait(app_name: str [, app_deployment: Optional[AppDeployment], timeout: datetime.timedelta = 0:20:00]) -> AppDeployment


    .. py:method:: get(name: str) -> App

        Get an app.
        
        Retrieves information for the app with the supplied name.
        
        :param name: str
          The name of the app.
        
        :returns: :class:`App`
        

    .. py:method:: get_deployment(app_name: str, deployment_id: str) -> AppDeployment

        Get an app deployment.
        
        Retrieves information for the app deployment with the supplied name and deployment id.
        
        :param app_name: str
          The name of the app.
        :param deployment_id: str
          The unique id of the deployment.
        
        :returns: :class:`AppDeployment`
        

    .. py:method:: get_permission_levels(app_name: str) -> GetAppPermissionLevelsResponse

        Get app permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param app_name: str
          The app for which to get or manage permissions.
        
        :returns: :class:`GetAppPermissionLevelsResponse`
        

    .. py:method:: get_permissions(app_name: str) -> AppPermissions

        Get app permissions.
        
        Gets the permissions of an app. Apps can inherit permissions from their root object.
        
        :param app_name: str
          The app for which to get or manage permissions.
        
        :returns: :class:`AppPermissions`
        

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[App]

        List apps.
        
        Lists all apps in the workspace.
        
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of apps. Requests first page if absent.
        
        :returns: Iterator over :class:`App`
        

    .. py:method:: list_deployments(app_name: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[AppDeployment]

        List app deployments.
        
        Lists all app deployments for the app with the supplied name.
        
        :param app_name: str
          The name of the app.
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of apps. Requests first page if absent.
        
        :returns: Iterator over :class:`AppDeployment`
        

    .. py:method:: set_permissions(app_name: str [, access_control_list: Optional[List[AppAccessControlRequest]]]) -> AppPermissions

        Set app permissions.
        
        Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct
        permissions if none are specified. Objects can inherit permissions from their root object.
        
        :param app_name: str
          The app for which to get or manage permissions.
        :param access_control_list: List[:class:`AppAccessControlRequest`] (optional)
        
        :returns: :class:`AppPermissions`
        

    .. py:method:: start(name: str) -> Wait[App]

        Start an app.
        
        Start the last active deployment of the app in the workspace.
        
        :param name: str
          The name of the app.
        
        :returns:
          Long-running operation waiter for :class:`App`.
          See :method:wait_get_app_active for more details.
        

    .. py:method:: start_and_wait(name: str, timeout: datetime.timedelta = 0:20:00) -> App


    .. py:method:: stop(name: str) -> Wait[App]

        Stop an app.
        
        Stops the active deployment of the app in the workspace.
        
        :param name: str
          The name of the app.
        
        :returns:
          Long-running operation waiter for :class:`App`.
          See :method:wait_get_app_stopped for more details.
        

    .. py:method:: stop_and_wait(name: str, timeout: datetime.timedelta = 0:20:00) -> App


    .. py:method:: update(name: str [, app: Optional[App]]) -> App

        Update an app.
        
        Updates the app with the supplied name.
        
        :param name: str
          The name of the app. The name must contain only lowercase alphanumeric characters and hyphens. It
          must be unique within the workspace.
        :param app: :class:`App` (optional)
        
        :returns: :class:`App`
        

    .. py:method:: update_permissions(app_name: str [, access_control_list: Optional[List[AppAccessControlRequest]]]) -> AppPermissions

        Update app permissions.
        
        Updates the permissions on an app. Apps can inherit permissions from their root object.
        
        :param app_name: str
          The app for which to get or manage permissions.
        :param access_control_list: List[:class:`AppAccessControlRequest`] (optional)
        
        :returns: :class:`AppPermissions`
        

    .. py:method:: wait_get_app_active(name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[App], None]]) -> App


    .. py:method:: wait_get_app_stopped(name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[App], None]]) -> App


    .. py:method:: wait_get_deployment_app_succeeded(app_name: str, deployment_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[AppDeployment], None]]) -> AppDeployment

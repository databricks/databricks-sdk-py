``w.apps``: Apps
================
.. currentmodule:: databricks.sdk.service.apps

.. py:class:: AppsAPI

    Apps run directly on a customer's Databricks instance, integrate with their data, use and extend
    Databricks services, and enable users to interact through single sign-on.

    .. py:method:: create(app: App [, no_compute: Optional[bool]]) -> Wait[App]

        Creates a new app.

        :param app: :class:`App`
        :param no_compute: bool (optional)
          If true, the app will not be started after creation.

        :returns:
          Long-running operation waiter for :class:`App`.
          See :method:wait_get_app_active for more details.
        

    .. py:method:: create_and_wait(app: App [, no_compute: Optional[bool], timeout: datetime.timedelta = 0:20:00]) -> App


    .. py:method:: create_space(space: Space) -> CreateSpaceOperation

        Creates a new app space.

        :param space: :class:`Space`

        :returns: :class:`Operation`
        

    .. py:method:: create_update(app_name: str, update_mask: str [, app: Optional[App]]) -> Wait[AppUpdate]

        Creates an app update and starts the update process. The update process is asynchronous and the status
        of the update can be checked with the GetAppUpdate method.

        :param app_name: str
        :param update_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.
        :param app: :class:`App` (optional)

        :returns:
          Long-running operation waiter for :class:`AppUpdate`.
          See :method:wait_get_update_app_succeeded for more details.
        

    .. py:method:: create_update_and_wait(app_name: str, update_mask: str [, app: Optional[App], timeout: datetime.timedelta = 0:20:00]) -> AppUpdate


    .. py:method:: delete(name: str) -> App

        Deletes an app.

        :param name: str
          The name of the app.

        :returns: :class:`App`
        

    .. py:method:: delete_space(name: str) -> DeleteSpaceOperation

        Deletes an app space.

        :param name: str
          The name of the app space.

        :returns: :class:`Operation`
        

    .. py:method:: deploy(app_name: str, app_deployment: AppDeployment) -> Wait[AppDeployment]

        Creates an app deployment for the app with the supplied name.

        :param app_name: str
          The name of the app.
        :param app_deployment: :class:`AppDeployment`
          The app deployment configuration.

        :returns:
          Long-running operation waiter for :class:`AppDeployment`.
          See :method:wait_get_deployment_app_succeeded for more details.
        

    .. py:method:: deploy_and_wait(app_name: str, app_deployment: AppDeployment, timeout: datetime.timedelta = 0:20:00) -> AppDeployment


    .. py:method:: get(name: str) -> App

        Retrieves information for the app with the supplied name.

        :param name: str
          The name of the app.

        :returns: :class:`App`
        

    .. py:method:: get_deployment(app_name: str, deployment_id: str) -> AppDeployment

        Retrieves information for the app deployment with the supplied name and deployment id.

        :param app_name: str
          The name of the app.
        :param deployment_id: str
          The unique id of the deployment.

        :returns: :class:`AppDeployment`
        

    .. py:method:: get_permission_levels(app_name: str) -> GetAppPermissionLevelsResponse

        Gets the permission levels that a user can have on an object.

        :param app_name: str
          The app for which to get or manage permissions.

        :returns: :class:`GetAppPermissionLevelsResponse`
        

    .. py:method:: get_permissions(app_name: str) -> AppPermissions

        Gets the permissions of an app. Apps can inherit permissions from their root object.

        :param app_name: str
          The app for which to get or manage permissions.

        :returns: :class:`AppPermissions`
        

    .. py:method:: get_space(name: str) -> Space

        Retrieves information for the app space with the supplied name.

        :param name: str
          The name of the app space.

        :returns: :class:`Space`
        

    .. py:method:: get_space_operation(name: str) -> Operation

        Gets the status of an app space update operation.

        :param name: str
          The name of the operation resource.

        :returns: :class:`Operation`
        

    .. py:method:: get_update(app_name: str) -> AppUpdate

        Gets the status of an app update.

        :param app_name: str
          The name of the app.

        :returns: :class:`AppUpdate`
        

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str], space: Optional[str]]) -> Iterator[App]

        Lists all apps in the workspace.

        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of apps. Requests first page if absent.
        :param space: str (optional)
          Filter apps by app space name. When specified, only apps belonging to this space are returned.

        :returns: Iterator over :class:`App`
        

    .. py:method:: list_deployments(app_name: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[AppDeployment]

        Lists all app deployments for the app with the supplied name.

        :param app_name: str
          The name of the app.
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of apps. Requests first page if absent.

        :returns: Iterator over :class:`AppDeployment`
        

    .. py:method:: list_spaces( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Space]

        Lists all app spaces in the workspace.

        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of app spaces. Requests first page if absent.

        :returns: Iterator over :class:`Space`
        

    .. py:method:: set_permissions(app_name: str [, access_control_list: Optional[List[AppAccessControlRequest]]]) -> AppPermissions

        Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct
        permissions if none are specified. Objects can inherit permissions from their root object.

        :param app_name: str
          The app for which to get or manage permissions.
        :param access_control_list: List[:class:`AppAccessControlRequest`] (optional)

        :returns: :class:`AppPermissions`
        

    .. py:method:: start(name: str) -> Wait[App]

        Start the last active deployment of the app in the workspace.

        :param name: str
          The name of the app.

        :returns:
          Long-running operation waiter for :class:`App`.
          See :method:wait_get_app_active for more details.
        

    .. py:method:: start_and_wait(name: str, timeout: datetime.timedelta = 0:20:00) -> App


    .. py:method:: stop(name: str) -> Wait[App]

        Stops the active deployment of the app in the workspace.

        :param name: str
          The name of the app.

        :returns:
          Long-running operation waiter for :class:`App`.
          See :method:wait_get_app_stopped for more details.
        

    .. py:method:: stop_and_wait(name: str, timeout: datetime.timedelta = 0:20:00) -> App


    .. py:method:: update(name: str, app: App) -> App

        Updates the app with the supplied name.

        :param name: str
          The name of the app. The name must contain only lowercase alphanumeric characters and hyphens. It
          must be unique within the workspace.
        :param app: :class:`App`

        :returns: :class:`App`
        

    .. py:method:: update_permissions(app_name: str [, access_control_list: Optional[List[AppAccessControlRequest]]]) -> AppPermissions

        Updates the permissions on an app. Apps can inherit permissions from their root object.

        :param app_name: str
          The app for which to get or manage permissions.
        :param access_control_list: List[:class:`AppAccessControlRequest`] (optional)

        :returns: :class:`AppPermissions`
        

    .. py:method:: update_space(name: str, space: Space, update_mask: FieldMask) -> UpdateSpaceOperation

        Updates an app space. The update process is asynchronous and the status of the update can be checked
        with the GetSpaceOperation method.

        :param name: str
          The name of the app space. The name must contain only lowercase alphanumeric characters and hyphens.
          It must be unique within the workspace.
        :param space: :class:`Space`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`Operation`
        

    .. py:method:: wait_get_app_active(name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[App], None]]) -> App


    .. py:method:: wait_get_app_stopped(name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[App], None]]) -> App


    .. py:method:: wait_get_deployment_app_succeeded(app_name: str, deployment_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[AppDeployment], None]]) -> AppDeployment


    .. py:method:: wait_get_update_app_succeeded(app_name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[AppUpdate], None]]) -> AppUpdate

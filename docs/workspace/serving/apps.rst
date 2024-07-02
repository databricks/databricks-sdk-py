``w.apps``: Apps
================
.. currentmodule:: databricks.sdk.service.serving

.. py:class:: AppsAPI

    Apps run directly on a customer’s Databricks instance, integrate with their data, use and extend
    Databricks services, and enable users to interact through single sign-on.

    .. py:method:: create(name: str [, description: Optional[str]]) -> Wait[App]

        Create an app.
        
        Creates a new app.
        
        :param name: str
          The name of the app. The name must contain only lowercase alphanumeric characters and hyphens. It
          must be unique within the workspace.
        :param description: str (optional)
          The description of the app.
        
        :returns:
          Long-running operation waiter for :class:`App`.
          See :method:wait_get_app_idle for more details.
        

    .. py:method:: create_and_wait(name: str [, description: Optional[str], timeout: datetime.timedelta = 0:20:00]) -> App


    .. py:method:: delete(name: str)

        Delete an app.
        
        Deletes an app.
        
        :param name: str
          The name of the app.
        
        
        

    .. py:method:: deploy(app_name: str, source_code_path: str, mode: AppDeploymentMode) -> Wait[AppDeployment]

        Create an app deployment.
        
        Creates an app deployment for the app with the supplied name.
        
        :param app_name: str
          The name of the app.
        :param source_code_path: str
          The workspace file system path of the source code used to create the app deployment. This is
          different from `deployment_artifacts.source_code_path`, which is the path used by the deployed app.
          The former refers to the original source code location of the app in the workspace during deployment
          creation, whereas the latter provides a system generated stable snapshotted source code path used by
          the deployment.
        :param mode: :class:`AppDeploymentMode`
          The mode of which the deployment will manage the source code.
        
        :returns:
          Long-running operation waiter for :class:`AppDeployment`.
          See :method:wait_get_deployment_app_succeeded for more details.
        

    .. py:method:: deploy_and_wait(app_name: str, source_code_path: str, mode: AppDeploymentMode, timeout: datetime.timedelta = 0:20:00) -> AppDeployment


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
        

    .. py:method:: get_environment(name: str) -> AppEnvironment

        Get app environment.
        
        Retrieves app environment.
        
        :param name: str
          The name of the app.
        
        :returns: :class:`AppEnvironment`
        

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
        

    .. py:method:: stop(name: str)

        Stop an app.
        
        Stops the active deployment of the app in the workspace.
        
        :param name: str
          The name of the app.
        
        
        

    .. py:method:: update(name: str [, description: Optional[str]]) -> App

        Update an app.
        
        Updates the app with the supplied name.
        
        :param name: str
          The name of the app. The name must contain only lowercase alphanumeric characters and hyphens. It
          must be unique within the workspace.
        :param description: str (optional)
          The description of the app.
        
        :returns: :class:`App`
        

    .. py:method:: wait_get_app_idle(name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[App], None]]) -> App


    .. py:method:: wait_get_deployment_app_succeeded(app_name: str, deployment_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[AppDeployment], None]]) -> AppDeployment

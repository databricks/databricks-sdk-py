Databricks Apps
===============
.. py:class:: AppsAPI

    Lakehouse Apps run directly on a customer’s Databricks instance, integrate with their data, use and
    extend Databricks services, and enable users to interact through single sign-on.

    .. py:method:: create(manifest [, resources])

        Create and deploy an application.
        
        Creates and deploys an application.
        
        :param manifest: :class:`AppManifest`
          Manifest that specifies the application requirements
        :param resources: Any (optional)
          Information passed at app deployment time to fulfill app dependencies
        
        :returns: :class:`DeploymentStatus`
        

    .. py:method:: delete_app(name)

        Delete an application.
        
        Delete an application definition
        
        :param name: str
          The name of an application. This field is required.
        
        :returns: :class:`DeleteAppResponse`
        

    .. py:method:: get_app(name)

        Get definition for an application.
        
        Get an application definition
        
        :param name: str
          The name of an application. This field is required.
        
        :returns: :class:`GetAppResponse`
        

    .. py:method:: get_app_deployment_status(deployment_id [, include_app_log])

        Get deployment status for an application.
        
        Get deployment status for an application
        
        :param deployment_id: str
          The deployment id for an application. This field is required.
        :param include_app_log: str (optional)
          Boolean flag to include application logs
        
        :returns: :class:`DeploymentStatus`
        

    .. py:method:: get_apps()

        List all applications.
        
        List all available applications
        
        :returns: :class:`ListAppsResponse`
        

    .. py:method:: get_events(name)

        Get deployment events for an application.
        
        Get deployment events for an application
        
        :param name: str
          The name of an application. This field is required.
        
        :returns: :class:`ListAppEventsResponse`
        
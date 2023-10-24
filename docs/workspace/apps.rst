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
        

    .. py:method:: delete(name)

        Delete an application.
        
        Delete an application definition
        
        :param name: str
          The name of an application. This field is required.
        
        
        

    .. py:method:: get(name)

        Get definition for an application.
        
        Get an application definition
        
        :param name: str
          The name of an application. This field is required.
        
        
        
``w.settings``: Settings
========================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: SettingsAPI

    Wrapper for Workspace Settings services

    .. py:property:: default_namespace
        :type: DefaultNamespaceAPI

        The default namespace setting API allows users to configure the default namespace for a Databricks
        workspace.
        
        Through this API, users can retrieve, set, or modify the default namespace used when queries do not
        reference a fully qualified three-level name. For example, if you use the API to set 'retail_prod' as the
        default catalog, then a query 'SELECT * FROM myTable' would reference the object
        'retail_prod.default.myTable' (the schema 'default' is always assumed).
        
        This setting requires a restart of clusters and SQL warehouses to take effect. Additionally, the default
        namespace only applies when using Unity Catalog-enabled compute.

    .. py:property:: restrict_workspace_admins
        :type: RestrictWorkspaceAdminsAPI

        The Restrict Workspace Admins setting lets you control the capabilities of workspace admins. With the
        setting status set to ALLOW_ALL, workspace admins can create service principal personal access tokens on
        behalf of any service principal in their workspace. Workspace admins can also change a job owner or the
        job run_as setting to any user in their workspace or a service principal on which they have the Service
        Principal User role. With the setting status set to RESTRICT_TOKENS_AND_JOB_RUN_AS, workspace admins can
        only create personal access tokens on behalf of service principals they have the Service Principal User
        role on. They can also only change a job owner or the job run_as setting to themselves or a service
        principal on which they have the Service Principal User role.
``w.settings``: Settings
========================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: SettingsAPI

    Workspace Settings API allows users to manage settings at the workspace level.

    .. py:property:: automatic_cluster_update
        :type: AutomaticClusterUpdateAPI

        Controls whether automatic cluster update is enabled for the current workspace. By default, it is turned
        off.

    .. py:property:: compliance_security_profile
        :type: ComplianceSecurityProfileAPI

        Controls whether to enable the compliance security profile for the current workspace. Enabling it on a
        workspace is permanent. By default, it is turned off.
        
        This settings can NOT be disabled once it is enabled.

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

    .. py:property:: disable_legacy_access
        :type: DisableLegacyAccessAPI

        'Disabling legacy access' has the following impacts:
        
        1. Disables direct access to the Hive Metastore. However, you can still access Hive Metastore through HMS
        Federation. 2. Disables Fallback Mode (docs link) on any External Location access from the workspace. 3.
        Alters DBFS path access to use External Location permissions in place of legacy credentials. 4. Enforces
        Unity Catalog access on all path based access.

    .. py:property:: disable_legacy_dbfs
        :type: DisableLegacyDbfsAPI

        When this setting is on, access to DBFS root and DBFS mounts is disallowed (as well as creation of new
        mounts). When the setting is off, all DBFS functionality is enabled

    .. py:property:: enhanced_security_monitoring
        :type: EnhancedSecurityMonitoringAPI

        Controls whether enhanced security monitoring is enabled for the current workspace. If the compliance
        security profile is enabled, this is automatically enabled. By default, it is disabled. However, if the
        compliance security profile is enabled, this is automatically enabled.
        
        If the compliance security profile is disabled, you can enable or disable this setting and it is not
        permanent.

    .. py:property:: restrict_workspace_admins
        :type: RestrictWorkspaceAdminsAPI

        The Restrict Workspace Admins setting lets you control the capabilities of workspace admins. With the
        setting status set to ALLOW_ALL, workspace admins can create service principal personal access tokens on
        behalf of any service principal in their workspace. Workspace admins can also change a job owner to any
        user in their workspace. And they can change the job run_as setting to any user in their workspace or to a
        service principal on which they have the Service Principal User role. With the setting status set to
        RESTRICT_TOKENS_AND_JOB_RUN_AS, workspace admins can only create personal access tokens on behalf of
        service principals they have the Service Principal User role on. They can also only change a job owner to
        themselves. And they can change the job run_as setting to themselves or to a service principal on which
        they have the Service Principal User role.
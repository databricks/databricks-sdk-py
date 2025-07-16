``w.settings``: Settings
========================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: SettingsAPI

    Workspace Settings API allows users to manage settings at the workspace level.

    .. py:property:: aibi_dashboard_embedding_access_policy
        :type: AibiDashboardEmbeddingAccessPolicyAPI

        Controls whether AI/BI published dashboard embedding is enabled, conditionally enabled, or disabled at the
        workspace level. By default, this setting is conditionally enabled (ALLOW_APPROVED_DOMAINS).

    .. py:property:: aibi_dashboard_embedding_approved_domains
        :type: AibiDashboardEmbeddingApprovedDomainsAPI

        Controls the list of domains approved to host the embedded AI/BI dashboards. The approved domains list
        can't be mutated when the current access policy is not set to ALLOW_APPROVED_DOMAINS.

    .. py:property:: automatic_cluster_update
        :type: AutomaticClusterUpdateAPI

        Controls whether automatic cluster update is enabled for the current workspace. By default, it is turned
        off.

    .. py:property:: compliance_security_profile
        :type: ComplianceSecurityProfileAPI

        Controls whether to enable the compliance security profile for the current workspace. Enabling it on a
        workspace is permanent. By default, it is turned off.
    
        This settings can NOT be disabled once it is enabled.

    .. py:property:: dashboard_email_subscriptions
        :type: DashboardEmailSubscriptionsAPI

        Controls whether schedules or workload tasks for refreshing AI/BI Dashboards in the workspace can send
        subscription emails containing PDFs and/or images of the dashboard. By default, this setting is enabled
        (set to `true`)

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

    .. py:property:: default_warehouse_id
        :type: DefaultWarehouseIdAPI

        Warehouse to be selected by default for users in this workspace. Covers SQL workloads only and can be
        overridden by users.

    .. py:property:: disable_legacy_access
        :type: DisableLegacyAccessAPI

        'Disabling legacy access' has the following impacts:
    
        1. Disables direct access to Hive Metastores from the workspace. However, you can still access a Hive
        Metastore through Hive Metastore federation. 2. Disables fallback mode on external location access from
        the workspace. 3. Disables Databricks Runtime versions prior to 13.3LTS.

    .. py:property:: disable_legacy_dbfs
        :type: DisableLegacyDbfsAPI

        Disabling legacy DBFS has the following implications:
    
        1. Access to DBFS root and DBFS mounts is disallowed (as well as the creation of new mounts). 2. Disables
        Databricks Runtime versions prior to 13.3LTS.
    
        When the setting is off, all DBFS functionality is enabled and no restrictions are imposed on Databricks
        Runtime versions. This setting can take up to 20 minutes to take effect and requires a manual restart of
        all-purpose compute clusters and SQL warehouses.

    .. py:property:: enable_export_notebook
        :type: EnableExportNotebookAPI

        Controls whether users can export notebooks and files from the Workspace UI. By default, this setting is
        enabled.

    .. py:property:: enable_notebook_table_clipboard
        :type: EnableNotebookTableClipboardAPI

        Controls whether users can copy tabular data to the clipboard via the UI. By default, this setting is
        enabled.

    .. py:property:: enable_results_downloading
        :type: EnableResultsDownloadingAPI

        Controls whether users can download notebook results. By default, this setting is enabled.

    .. py:property:: enhanced_security_monitoring
        :type: EnhancedSecurityMonitoringAPI

        Controls whether enhanced security monitoring is enabled for the current workspace. If the compliance
        security profile is enabled, this is automatically enabled. By default, it is disabled. However, if the
        compliance security profile is enabled, this is automatically enabled.
    
        If the compliance security profile is disabled, you can enable or disable this setting and it is not
        permanent.

    .. py:property:: llm_proxy_partner_powered_workspace
        :type: LlmProxyPartnerPoweredWorkspaceAPI

        Determines if partner powered models are enabled or not for a specific workspace

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

    .. py:property:: sql_results_download
        :type: SqlResultsDownloadAPI

        Controls whether users within the workspace are allowed to download results from the SQL Editor and AI/BI
        Dashboards UIs. By default, this setting is enabled (set to `true`)
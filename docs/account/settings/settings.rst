``a.settings``: Account Settings
================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: AccountSettingsAPI

    Accounts Settings API allows users to manage settings at the account level.

    .. py:property:: csp_enablement_account
        :type: CspEnablementAccountAPI

        The compliance security profile settings at the account level control whether to enable it for new
        workspaces. By default, this account-level setting is disabled for new workspaces. After workspace
        creation, account admins can enable the compliance security profile individually for each workspace.
        
        This settings can be disabled so that new workspaces do not have compliance security profile enabled by
        default.

    .. py:property:: disable_legacy_features
        :type: DisableLegacyFeaturesAPI

        Disable legacy features for new Databricks workspaces.
        
        For newly created workspaces: 1. Disables the use of DBFS root and mounts. 2. Hive Metastore will not be
        provisioned. 3. Disables the use of ‘No-isolation clusters’. 4. Disables Databricks Runtime versions
        prior to 13.3LTS.

    .. py:property:: esm_enablement_account
        :type: EsmEnablementAccountAPI

        The enhanced security monitoring setting at the account level controls whether to enable the feature on
        new workspaces. By default, this account-level setting is disabled for new workspaces. After workspace
        creation, account admins can enable enhanced security monitoring individually for each workspace.

    .. py:property:: personal_compute
        :type: PersonalComputeAPI

        The Personal Compute enablement setting lets you control which users can use the Personal Compute default
        policy to create compute resources. By default all users in all workspaces have access (ON), but you can
        change the setting to instead let individual workspaces configure access control (DELEGATE).
        
        There is only one instance of this setting per account. Since this setting has a default value, this
        setting is present on all accounts even though it's never set on a given account. Deletion reverts the
        value of the setting back to the default value.
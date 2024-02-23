``a.settings``: Account Settings
================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: AccountSettingsAPI

    Wrapper for Account Settings services

    .. py:property:: personal_compute_enablement
        :type: PersonalComputeEnablementAPI

        The Personal Compute enablement setting lets you control which users can use the Personal Compute default
        policy to create compute resources. By default all users in all workspaces have access (ON), but you can
        change the setting to instead let individual workspaces configure access control (DELEGATE).
        
        There is only one instance of this setting per account. Since this setting has a default value, this
        setting is present on all accounts even though it's never set on a given account. Deletion reverts the
        value of the setting back to the default value.
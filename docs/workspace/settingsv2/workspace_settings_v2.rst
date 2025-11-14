``w.workspace_settings_v2``: WorkspaceSettings.v2
=================================================
.. currentmodule:: databricks.sdk.service.settingsv2

.. py:class:: WorkspaceSettingsV2API

    APIs to manage workspace level settings

    .. py:method:: get_public_workspace_setting(name: str) -> Setting

        Get a setting value at workspace level. See :method:settingsv2/listworkspacesettingsmetadata for list
        of setting available via public APIs.

        :param name: str
          Name of the setting

        :returns: :class:`Setting`
        

    .. py:method:: list_workspace_settings_metadata( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SettingsMetadata]

        List valid setting keys and metadata. These settings are available to be referenced via GET
        :method:settingsv2/getpublicworkspacesetting and PATCH :method:settingsv2/patchpublicworkspacesetting
        APIs

        :param page_size: int (optional)
          The maximum number of settings to return. The service may return fewer than this value. If
          unspecified, at most 200 settings will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListWorkspaceSettingsMetadataRequest` call. Provide this to
          retrieve the subsequent page.

          When paginating, all other parameters provided to `ListWorkspaceSettingsMetadataRequest` must match
          the call that provided the page token.

        :returns: Iterator over :class:`SettingsMetadata`
        

    .. py:method:: patch_public_workspace_setting(name: str, setting: Setting) -> Setting

        Patch a setting value at workspace level. See :method:settingsv2/listworkspacesettingsmetadata for
        list of setting available via public APIs at workspace level. To determine the correct field to
        include in a patch request, refer to the type field of the setting returned in the
        :method:settingsv2/listworkspacesettingsmetadata response.

        :param name: str
          Name of the setting
        :param setting: :class:`Setting`

        :returns: :class:`Setting`
        
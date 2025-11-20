``a.settings_v2``: AccountSettings.v2
=====================================
.. currentmodule:: databricks.sdk.service.settingsv2

.. py:class:: AccountSettingsV2API

    APIs to manage account level settings

    .. py:method:: get_public_account_setting(name: str) -> Setting

        Get a setting value at account level. See :method:settingsv2/listaccountsettingsmetadata for list of
        setting available via public APIs at account level.

        :param name: str

        :returns: :class:`Setting`
        

    .. py:method:: get_public_account_user_preference(user_id: str, name: str) -> UserPreference

        Get a setting value for a specific user at account level. See
        :method:settingsv2/listaccountuserpreferencesmetadata for list of setting available via public APIs.

        :param user_id: str
          User ID of the user whose setting is being retrieved.
        :param name: str
          User Setting name.

        :returns: :class:`UserPreference`
        

    .. py:method:: list_account_settings_metadata( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SettingsMetadata]

        List valid setting keys and metadata. These settings are available to be referenced via GET
        :method:settingsv2/getpublicaccountsetting and PATCH :method:settingsv2/patchpublicaccountsetting APIs

        :param page_size: int (optional)
          The maximum number of settings to return. The service may return fewer than this value. If
          unspecified, at most 200 settings will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListAccountSettingsMetadataRequest` call. Provide this to
          retrieve the subsequent page.

          When paginating, all other parameters provided to `ListAccountSettingsMetadataRequest` must match
          the call that provided the page token.

        :returns: Iterator over :class:`SettingsMetadata`
        

    .. py:method:: list_account_user_preferences_metadata(user_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SettingsMetadata]

        List valid setting keys and metadata for a specific user. These settings are available to be
        referenced via GET :method:settingsv2/getpublicaccountuserpreference and PATCH
        :method:settingsv2/patchpublicaccountuserpreference APIs

        :param user_id: str
          User ID of the user whose settings metadata is being retrieved.
        :param page_size: int (optional)
          The maximum number of settings to return. The service may return fewer than this value. If
          unspecified, at most 200 settings will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListAccountUserPreferencesMetadataRequest` call. Provide
          this to retrieve the subsequent page.

          When paginating, all other parameters provided to `ListAccountUserPreferencesMetadataRequest` must
          match the call that provided the page token.

        :returns: Iterator over :class:`SettingsMetadata`
        

    .. py:method:: patch_public_account_setting(name: str, setting: Setting) -> Setting

        Patch a setting value at account level. See :method:settingsv2/listaccountsettingsmetadata for list of
        setting available via public APIs at account level. To determine the correct field to include in a
        patch request, refer to the type field of the setting returned in the
        :method:settingsv2/listaccountsettingsmetadata response.

        :param name: str
        :param setting: :class:`Setting`

        :returns: :class:`Setting`
        

    .. py:method:: patch_public_account_user_preference(user_id: str, name: str, setting: UserPreference) -> UserPreference

        Patch a setting value for a specific user at account level. See
        :method:settingsv2/listaccountuserpreferencesmetadata for list of setting available via public APIs at
        account-user level.

        :param user_id: str
          User ID of the user whose setting is being updated.
        :param name: str
        :param setting: :class:`UserPreference`

        :returns: :class:`UserPreference`
        
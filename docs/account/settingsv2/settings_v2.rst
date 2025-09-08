``a.settings_v2``: AccountSettings.v2
=====================================
.. currentmodule:: databricks.sdk.service.settingsv2

.. py:class:: AccountSettingsV2API

    APIs to manage account level settings

    .. py:method:: get_public_account_setting(name: str) -> Setting

        Get a setting value at account level

        :param name: str

        :returns: :class:`Setting`
        

    .. py:method:: list_account_settings_metadata( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SettingsMetadata]

        List valid setting keys and metadata. These settings are available to referenced via [GET
        /api/2.1/settings/{name}](#~1api~1account~1settingsv2~1getpublicaccountsetting) and [PATCH
        /api/2.1/settings/{name}](#~1api~1account~1settingsv2~patchpublicaccountsetting) APIs

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
        

    .. py:method:: patch_public_account_setting(name: str, setting: Setting) -> Setting

        Patch a setting value at account level

        :param name: str
        :param setting: :class:`Setting`

        :returns: :class:`Setting`
        
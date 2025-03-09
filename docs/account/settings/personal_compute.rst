``a.settings.personal_compute``: Personal Compute Enablement
============================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: PersonalComputeAPI

    The Personal Compute enablement setting lets you control which users can use the Personal Compute default
    policy to create compute resources. By default all users in all workspaces have access (ON), but you can
    change the setting to instead let individual workspaces configure access control (DELEGATE).

    There is only one instance of this setting per account. Since this setting has a default value, this
    setting is present on all accounts even though it's never set on a given account. Deletion reverts the
    value of the setting back to the default value.

    .. py:method:: delete( [, etag: Optional[str]]) -> DeletePersonalComputeSettingResponse

        Delete Personal Compute setting.

        Reverts back the Personal Compute setting value to default (ON)

        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.

        :returns: :class:`DeletePersonalComputeSettingResponse`
        

    .. py:method:: get( [, etag: Optional[str]]) -> PersonalComputeSetting

        Get Personal Compute setting.

        Gets the value of the Personal Compute setting.

        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.

        :returns: :class:`PersonalComputeSetting`
        

    .. py:method:: update(allow_missing: bool, setting: PersonalComputeSetting, field_mask: str) -> PersonalComputeSetting

        Update Personal Compute setting.

        Updates the value of the Personal Compute setting.

        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`PersonalComputeSetting`
        :param field_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`PersonalComputeSetting`
        
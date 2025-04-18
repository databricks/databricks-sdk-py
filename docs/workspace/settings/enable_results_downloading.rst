``w.settings.enable_results_downloading``: Enable Results Downloading
=====================================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: EnableResultsDownloadingAPI

    Controls whether users can download notebook results. By default, this setting is enabled.

    .. py:method:: get_enable_results_downloading() -> EnableResultsDownloading

        Get the Enable Results Downloading setting.

        Gets the Enable Results Downloading setting.

        :returns: :class:`EnableResultsDownloading`
        

    .. py:method:: patch_enable_results_downloading(allow_missing: bool, setting: EnableResultsDownloading, field_mask: str) -> EnableResultsDownloading

        Update the Enable Results Downloading setting.

        Updates the Enable Results Downloading setting. The model follows eventual consistency, which means
        the get after the update operation might receive stale values for some time.

        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`EnableResultsDownloading`
        :param field_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`EnableResultsDownloading`
        
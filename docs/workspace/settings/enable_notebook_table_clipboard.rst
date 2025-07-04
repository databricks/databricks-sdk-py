``w.settings.enable_notebook_table_clipboard``: Results Table Clipboard features
================================================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: EnableNotebookTableClipboardAPI

    Controls whether users can copy tabular data to the clipboard via the UI. By default, this setting is
    enabled.

    .. py:method:: get_enable_notebook_table_clipboard() -> EnableNotebookTableClipboard

        Gets the Results Table Clipboard features setting.


        :returns: :class:`EnableNotebookTableClipboard`
        

    .. py:method:: patch_enable_notebook_table_clipboard(allow_missing: bool, setting: EnableNotebookTableClipboard, field_mask: str) -> EnableNotebookTableClipboard

        Updates the Results Table Clipboard features setting. The model follows eventual consistency, which
        means the get after the update operation might receive stale values for some time.

        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`EnableNotebookTableClipboard`
        :param field_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`EnableNotebookTableClipboard`
        
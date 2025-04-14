``w.settings.enable_export_notebook``: Enable Export Notebook
=============================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: EnableExportNotebookAPI

    Controls whether users can export notebooks and files from the Workspace. By default, this setting is
    enabled.

    .. py:method:: get_enable_export_notebook() -> EnableExportNotebook

        Get the Enable Export Notebook setting.

        Gets the Enable Export Notebook setting.

        :returns: :class:`EnableExportNotebook`
        

    .. py:method:: patch_enable_export_notebook(allow_missing: bool, setting: EnableExportNotebook, field_mask: str) -> EnableExportNotebook

        Update the Enable Export Notebook setting.

        Updates the Enable Export Notebook setting. The model follows eventual consistency, which means the
        get after the update operation might receive stale values for some time.

        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`EnableExportNotebook`
        :param field_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`EnableExportNotebook`
        
``w.settings.disable_legacy_dbfs``: Disable Legacy DBFS
=======================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: DisableLegacyDbfsAPI

    Disabling legacy DBFS has the following implications:

    1. Access to DBFS root and DBFS mounts is disallowed (as well as the creation of new mounts). 2. Disables
    Databricks Runtime versions prior to 13.3LTS.

    When the setting is off, all DBFS functionality is enabled and no restrictions are imposed on Databricks
    Runtime versions. This setting can take up to 20 minutes to take effect and requires a manual restart of
    all-purpose compute clusters and SQL warehouses.

    .. py:method:: delete( [, etag: Optional[str]]) -> DeleteDisableLegacyDbfsResponse

        Delete the disable legacy DBFS setting.

        Deletes the disable legacy DBFS setting for a workspace, reverting back to the default.

        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.

        :returns: :class:`DeleteDisableLegacyDbfsResponse`
        

    .. py:method:: get( [, etag: Optional[str]]) -> DisableLegacyDbfs

        Get the disable legacy DBFS setting.

        Gets the disable legacy DBFS setting.

        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.

        :returns: :class:`DisableLegacyDbfs`
        

    .. py:method:: update(allow_missing: bool, setting: DisableLegacyDbfs, field_mask: str) -> DisableLegacyDbfs

        Update the disable legacy DBFS setting.

        Updates the disable legacy DBFS setting for the workspace.

        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`DisableLegacyDbfs`
        :param field_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`DisableLegacyDbfs`
        
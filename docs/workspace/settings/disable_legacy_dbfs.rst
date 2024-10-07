``w.settings.disable_legacy_dbfs``: Disable Legacy DBFS
=======================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: DisableLegacyDbfsAPI

    When this setting is on, access to DBFS root and DBFS mounts is disallowed (as well as creation of new
    mounts). When the setting is off, all DBFS functionality is enabled

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
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`DisableLegacyDbfs`
        
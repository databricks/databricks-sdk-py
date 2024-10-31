``a.settings.disable_legacy_features``: Disable Legacy Features
===============================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: DisableLegacyFeaturesAPI

    Disable legacy features for new Databricks workspaces.
    
    For newly created workspaces: 1. Disables the use of DBFS root and mounts. 2. Hive Metastore will not be
    provisioned. 3. Disables the use of ‘No-isolation clusters’. 4. Disables Databricks Runtime versions
    prior to 13.3LTS.

    .. py:method:: delete( [, etag: Optional[str]]) -> DeleteDisableLegacyFeaturesResponse

        Delete the disable legacy features setting.
        
        Deletes the disable legacy features setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteDisableLegacyFeaturesResponse`
        

    .. py:method:: get( [, etag: Optional[str]]) -> DisableLegacyFeatures

        Get the disable legacy features setting.
        
        Gets the value of the disable legacy features setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DisableLegacyFeatures`
        

    .. py:method:: update(allow_missing: bool, setting: DisableLegacyFeatures, field_mask: str) -> DisableLegacyFeatures

        Update the disable legacy features setting.
        
        Updates the value of the disable legacy features setting.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`DisableLegacyFeatures`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`DisableLegacyFeatures`
        
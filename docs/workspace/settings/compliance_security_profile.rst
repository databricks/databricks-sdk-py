``w.settings.compliance_security_profile``: Compliance Security Profile
=======================================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: ComplianceSecurityProfileAPI

    Controls whether to enable the compliance security profile for the current workspace. Enabling it on a
    workspace is permanent. By default, it is turned off.
    
    This settings can NOT be disabled once it is enabled.

    .. py:method:: get( [, etag: Optional[str]]) -> ComplianceSecurityProfileSetting

        Get the compliance security profile setting.
        
        Gets the compliance security profile setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`ComplianceSecurityProfileSetting`
        

    .. py:method:: update(allow_missing: bool, setting: ComplianceSecurityProfileSetting, field_mask: str) -> ComplianceSecurityProfileSetting

        Update the compliance security profile setting.
        
        Updates the compliance security profile setting for the workspace. A fresh etag needs to be provided
        in `PATCH` requests (as part of the setting field). The etag can be retrieved by making a `GET`
        request before the `PATCH` request. If the setting is updated concurrently, `PATCH` fails with 409 and
        the request must be retried by using the fresh etag in the 409 response.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`ComplianceSecurityProfileSetting`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`ComplianceSecurityProfileSetting`
        
``a.settings.csp_enablement_account``: Compliance Security Profile For New Workspaces
=====================================================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: CspEnablementAccountAPI

    The compliance security profile settings at the account level control whether to enable it for new
    workspaces. By default, this account-level setting is disabled for new workspaces. After workspace
    creation, account admins can enable the compliance security profile individually for each workspace.
    
    This settings can be disabled so that new workspaces do not have compliance security profile enabled by
    default.

    .. py:method:: get( [, etag: Optional[str]]) -> CspEnablementAccountSetting

        Get the compliance security profile setting for new workspaces.
        
        Gets the compliance security profile setting for new workspaces.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`CspEnablementAccountSetting`


    .. py:method:: update(allow_missing: bool, setting: CspEnablementAccountSetting, field_mask: str) -> CspEnablementAccountSetting

        Update the compliance security profile setting for new workspaces.
        
        Updates the value of the compliance security profile setting for new workspaces.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`CspEnablementAccountSetting`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`CspEnablementAccountSetting`

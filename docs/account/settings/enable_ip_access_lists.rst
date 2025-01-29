``a.settings.enable_ip_access_lists``: Enable Account IP Access Lists
=====================================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: EnableIpAccessListsAPI

    Controls the enforcement of IP access lists for accessing the account console. Allowing you to enable or
    disable restricted access based on IP addresses.

    .. py:method:: delete( [, etag: Optional[str]]) -> DeleteAccountIpAccessEnableResponse

        Delete the account IP access toggle setting.
        
        Reverts the value of the account IP access toggle setting to default (ON)
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteAccountIpAccessEnableResponse`
        

    .. py:method:: get( [, etag: Optional[str]]) -> AccountIpAccessEnable

        Get the account IP access toggle setting.
        
        Gets the value of the account IP access toggle setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`AccountIpAccessEnable`
        

    .. py:method:: update(allow_missing: bool, setting: AccountIpAccessEnable, field_mask: str) -> AccountIpAccessEnable

        Update the account IP access toggle setting.
        
        Updates the value of the account IP access toggle setting.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`AccountIpAccessEnable`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`AccountIpAccessEnable`
        
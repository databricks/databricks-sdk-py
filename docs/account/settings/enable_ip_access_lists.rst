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
  The field mask must be a single string, with multiple fields separated by commas (no spaces). The
  field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
  `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
  the entire collection field can be specified. Field names must exactly match the resource field
  names.
  
  A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
  fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
  changes in the future.

:returns: :class:`AccountIpAccessEnable`

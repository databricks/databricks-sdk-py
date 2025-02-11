``a.settings.esm_enablement_account``: Enhanced Security Monitoring For New Workspaces
======================================================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: EsmEnablementAccountAPI

    The enhanced security monitoring setting at the account level controls whether to enable the feature on
new workspaces. By default, this account-level setting is disabled for new workspaces. After workspace
creation, account admins can enable enhanced security monitoring individually for each workspace.

    .. py:method:: get( [, etag: Optional[str]]) -> EsmEnablementAccountSetting

        Get the enhanced security monitoring setting for new workspaces.

Gets the enhanced security monitoring setting for new workspaces.

:param etag: str (optional)
  etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
  optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
  each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
  to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
  request, and pass it with the DELETE request to identify the rule set version you are deleting.

:returns: :class:`EsmEnablementAccountSetting`


    .. py:method:: update(allow_missing: bool, setting: EsmEnablementAccountSetting, field_mask: str) -> EsmEnablementAccountSetting

        Update the enhanced security monitoring setting for new workspaces.

Updates the value of the enhanced security monitoring setting for new workspaces.

:param allow_missing: bool
  This should always be set to true for Settings API. Added for AIP compliance.
:param setting: :class:`EsmEnablementAccountSetting`
:param field_mask: str
  The field mask must be a single string, with multiple fields separated by commas (no spaces). The
  field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
  `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
  the entire collection field can be specified. Field names must exactly match the resource field
  names.
  
  A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
  fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
  changes in the future.

:returns: :class:`EsmEnablementAccountSetting`

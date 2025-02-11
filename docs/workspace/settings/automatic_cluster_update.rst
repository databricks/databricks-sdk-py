``w.settings.automatic_cluster_update``: Automatic Cluster Update
=================================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: AutomaticClusterUpdateAPI

    Controls whether automatic cluster update is enabled for the current workspace. By default, it is turned
off.

    .. py:method:: get( [, etag: Optional[str]]) -> AutomaticClusterUpdateSetting

        Get the automatic cluster update setting.

Gets the automatic cluster update setting.

:param etag: str (optional)
  etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
  optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
  each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
  to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
  request, and pass it with the DELETE request to identify the rule set version you are deleting.

:returns: :class:`AutomaticClusterUpdateSetting`


    .. py:method:: update(allow_missing: bool, setting: AutomaticClusterUpdateSetting, field_mask: str) -> AutomaticClusterUpdateSetting

        Update the automatic cluster update setting.

Updates the automatic cluster update setting for the workspace. A fresh etag needs to be provided in
`PATCH` requests (as part of the setting field). The etag can be retrieved by making a `GET` request
before the `PATCH` request. If the setting is updated concurrently, `PATCH` fails with 409 and the
request must be retried by using the fresh etag in the 409 response.

:param allow_missing: bool
  This should always be set to true for Settings API. Added for AIP compliance.
:param setting: :class:`AutomaticClusterUpdateSetting`
:param field_mask: str
  The field mask must be a single string, with multiple fields separated by commas (no spaces). The
  field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
  `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
  the entire collection field can be specified. Field names must exactly match the resource field
  names.
  
  A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
  fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
  changes in the future.

:returns: :class:`AutomaticClusterUpdateSetting`

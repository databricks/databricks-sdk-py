``w.settings.disable_legacy_access``: Disable Legacy Access
===========================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: DisableLegacyAccessAPI

    'Disabling legacy access' has the following impacts:

1. Disables direct access to the Hive Metastore. However, you can still access Hive Metastore through HMS
Federation. 2. Disables Fallback Mode (docs link) on any External Location access from the workspace. 3.
Alters DBFS path access to use External Location permissions in place of legacy credentials. 4. Enforces
Unity Catalog access on all path based access.

    .. py:method:: delete( [, etag: Optional[str]]) -> DeleteDisableLegacyAccessResponse

        Delete Legacy Access Disablement Status.

Deletes legacy access disablement status.

:param etag: str (optional)
  etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
  optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
  each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
  to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
  request, and pass it with the DELETE request to identify the rule set version you are deleting.

:returns: :class:`DeleteDisableLegacyAccessResponse`


    .. py:method:: get( [, etag: Optional[str]]) -> DisableLegacyAccess

        Retrieve Legacy Access Disablement Status.

Retrieves legacy access disablement Status.

:param etag: str (optional)
  etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
  optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
  each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
  to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
  request, and pass it with the DELETE request to identify the rule set version you are deleting.

:returns: :class:`DisableLegacyAccess`


    .. py:method:: update(allow_missing: bool, setting: DisableLegacyAccess, field_mask: str) -> DisableLegacyAccess

        Update Legacy Access Disablement Status.

Updates legacy access disablement status.

:param allow_missing: bool
  This should always be set to true for Settings API. Added for AIP compliance.
:param setting: :class:`DisableLegacyAccess`
:param field_mask: str
  The field mask must be a single string, with multiple fields separated by commas (no spaces). The
  field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
  `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
  the entire collection field can be specified. Field names must exactly match the resource field
  names.
  
  A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
  fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
  changes in the future.

:returns: :class:`DisableLegacyAccess`

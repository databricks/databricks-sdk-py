``w.settings.aibi_dashboard_embedding_approved_domains``: AI/BI Dashboard Embedding Approved Domains
====================================================================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: AibiDashboardEmbeddingApprovedDomainsAPI

    Controls the list of domains approved to host the embedded AI/BI dashboards. The approved domains list
can't be mutated when the current access policy is not set to ALLOW_APPROVED_DOMAINS.

    .. py:method:: delete( [, etag: Optional[str]]) -> DeleteAibiDashboardEmbeddingApprovedDomainsSettingResponse

        Delete AI/BI dashboard embedding approved domains.

Delete the list of domains approved to host embedded AI/BI dashboards, reverting back to the default
empty list.

:param etag: str (optional)
  etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
  optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
  each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
  to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
  request, and pass it with the DELETE request to identify the rule set version you are deleting.

:returns: :class:`DeleteAibiDashboardEmbeddingApprovedDomainsSettingResponse`


    .. py:method:: get( [, etag: Optional[str]]) -> AibiDashboardEmbeddingApprovedDomainsSetting

        Retrieve the list of domains approved to host embedded AI/BI dashboards.

Retrieves the list of domains approved to host embedded AI/BI dashboards.

:param etag: str (optional)
  etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
  optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
  each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
  to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
  request, and pass it with the DELETE request to identify the rule set version you are deleting.

:returns: :class:`AibiDashboardEmbeddingApprovedDomainsSetting`


    .. py:method:: update(allow_missing: bool, setting: AibiDashboardEmbeddingApprovedDomainsSetting, field_mask: str) -> AibiDashboardEmbeddingApprovedDomainsSetting

        Update the list of domains approved to host embedded AI/BI dashboards.

Updates the list of domains approved to host embedded AI/BI dashboards. This update will fail if the
current workspace access policy is not ALLOW_APPROVED_DOMAINS.

:param allow_missing: bool
  This should always be set to true for Settings API. Added for AIP compliance.
:param setting: :class:`AibiDashboardEmbeddingApprovedDomainsSetting`
:param field_mask: str
  The field mask must be a single string, with multiple fields separated by commas (no spaces). The
  field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
  `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
  the entire collection field can be specified. Field names must exactly match the resource field
  names.
  
  A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
  fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
  changes in the future.

:returns: :class:`AibiDashboardEmbeddingApprovedDomainsSetting`

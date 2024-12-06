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
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`AibiDashboardEmbeddingApprovedDomainsSetting`
        
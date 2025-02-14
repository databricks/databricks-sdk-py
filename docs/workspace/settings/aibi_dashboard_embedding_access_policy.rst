``w.settings.aibi_dashboard_embedding_access_policy``: AI/BI Dashboard Embedding Access Policy
==============================================================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: AibiDashboardEmbeddingAccessPolicyAPI

    Controls whether AI/BI published dashboard embedding is enabled, conditionally enabled, or disabled at the
    workspace level. By default, this setting is conditionally enabled (ALLOW_APPROVED_DOMAINS).

    .. py:method:: delete( [, etag: Optional[str]]) -> DeleteAibiDashboardEmbeddingAccessPolicySettingResponse

        Delete the AI/BI dashboard embedding access policy.
        
        Delete the AI/BI dashboard embedding access policy, reverting back to the default.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteAibiDashboardEmbeddingAccessPolicySettingResponse`
        

    .. py:method:: get( [, etag: Optional[str]]) -> AibiDashboardEmbeddingAccessPolicySetting

        Retrieve the AI/BI dashboard embedding access policy.
        
        Retrieves the AI/BI dashboard embedding access policy. The default setting is ALLOW_APPROVED_DOMAINS,
        permitting AI/BI dashboards to be embedded on approved domains.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`AibiDashboardEmbeddingAccessPolicySetting`
        

    .. py:method:: update(allow_missing: bool, setting: AibiDashboardEmbeddingAccessPolicySetting, field_mask: str) -> AibiDashboardEmbeddingAccessPolicySetting

        Update the AI/BI dashboard embedding access policy.
        
        Updates the AI/BI dashboard embedding access policy at the workspace level.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`AibiDashboardEmbeddingAccessPolicySetting`
        :param field_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.
          
          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.
        
        :returns: :class:`AibiDashboardEmbeddingAccessPolicySetting`
        
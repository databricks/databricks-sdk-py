``w.resource_quotas``: Resource Quotas
======================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: ResourceQuotasAPI

    Unity Catalog enforces resource quotas on all securable objects, which limits the number of resources that
    can be created. Quotas are expressed in terms of a resource type and a parent (for example, tables per
    metastore or schemas per catalog). The resource quota APIs enable you to monitor your current usage and
    limits. For more information on resource quotas see the [Unity Catalog documentation].
    
    [Unity Catalog documentation]: https://docs.databricks.com/en/data-governance/unity-catalog/index.html#resource-quotas

    .. py:method:: get_quota(parent_securable_type: str, parent_full_name: str, quota_name: str) -> GetQuotaResponse

        Get information for a single resource quota.
        
        The GetQuota API returns usage information for a single resource quota, defined as a child-parent
        pair. This API also refreshes the quota count if it is out of date. Refreshes are triggered
        asynchronously. The updated count might not be returned in the first call.
        
        :param parent_securable_type: str
          Securable type of the quota parent.
        :param parent_full_name: str
          Full name of the parent resource. Provide the metastore ID if the parent is a metastore.
        :param quota_name: str
          Name of the quota. Follows the pattern of the quota type, with "-quota" added as a suffix.
        
        :returns: :class:`GetQuotaResponse`
        

    .. py:method:: list_quotas( [, max_results: Optional[int], page_token: Optional[str]]) -> Iterator[QuotaInfo]

        List all resource quotas under a metastore.
        
        ListQuotas returns all quota values under the metastore. There are no SLAs on the freshness of the
        counts returned. This API does not trigger a refresh of quota counts.
        
        :param max_results: int (optional)
          The number of quotas to return.
        :param page_token: str (optional)
          Opaque token for the next page of results.
        
        :returns: Iterator over :class:`QuotaInfo`
        
``w.policy_compliance_for_clusters``: Policy compliance for clusters
====================================================================
.. currentmodule:: databricks.sdk.service.compute

.. py:class:: PolicyComplianceForClustersAPI

    The policy compliance APIs allow you to view and manage the policy compliance status of clusters in your
    workspace.
    
    A cluster is compliant with its policy if its configuration satisfies all its policy rules. Clusters could
    be out of compliance if their policy was updated after the cluster was last edited.
    
    The get and list compliance APIs allow you to view the policy compliance status of a cluster. The enforce
    compliance API allows you to update a cluster to be compliant with the current version of its policy.

    .. py:method:: enforce_compliance(cluster_id: str [, validate_only: Optional[bool]]) -> EnforceClusterComplianceResponse

        Enforce cluster policy compliance.
        
        Updates a cluster to be compliant with the current version of its policy. A cluster can be updated if
        it is in a `RUNNING` or `TERMINATED` state.
        
        If a cluster is updated while in a `RUNNING` state, it will be restarted so that the new attributes
        can take effect.
        
        If a cluster is updated while in a `TERMINATED` state, it will remain `TERMINATED`. The next time the
        cluster is started, the new attributes will take effect.
        
        Clusters created by the Databricks Jobs, DLT, or Models services cannot be enforced by this API.
        Instead, use the "Enforce job policy compliance" API to enforce policy compliance on jobs.
        
        :param cluster_id: str
          The ID of the cluster you want to enforce policy compliance on.
        :param validate_only: bool (optional)
          If set, previews the changes that would be made to a cluster to enforce compliance but does not
          update the cluster.
        
        :returns: :class:`EnforceClusterComplianceResponse`
        

    .. py:method:: get_compliance(cluster_id: str) -> GetClusterComplianceResponse

        Get cluster policy compliance.
        
        Returns the policy compliance status of a cluster. Clusters could be out of compliance if their policy
        was updated after the cluster was last edited.
        
        :param cluster_id: str
          The ID of the cluster to get the compliance status
        
        :returns: :class:`GetClusterComplianceResponse`
        

    .. py:method:: list_compliance(policy_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ClusterCompliance]

        List cluster policy compliance.
        
        Returns the policy compliance status of all clusters that use a given policy. Clusters could be out of
        compliance if their policy was updated after the cluster was last edited.
        
        :param policy_id: str
          Canonical unique identifier for the cluster policy.
        :param page_size: int (optional)
          Use this field to specify the maximum number of results to be returned by the server. The server may
          further constrain the maximum number of results returned in a single page.
        :param page_token: str (optional)
          A page token that can be used to navigate to the next page or previous page as returned by
          `next_page_token` or `prev_page_token`.
        
        :returns: Iterator over :class:`ClusterCompliance`
        
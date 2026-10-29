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

    .. py:method:: cancel_pending_cluster_enforcement(cluster_id: str [, allow_missing: Optional[bool]]) -> CancelPendingClusterEnforcementResponse

        Cancels a pending enforcement on a cluster. After canceling the pending enforcement, the cluster will
        no longer update on the next termination or restart. Pending enforcements cannot be canceled when a
        cluster is in ``TERMINATING`` state. Only workspace admins can cancel pending enforcements.

        :param cluster_id: str
          The ID of the cluster to cancel the pending enforcement for.
        :param allow_missing: bool (optional)
          If true and no pending enforcement exists, the request will succeed but no action will be taken.

        :returns: :class:`CancelPendingClusterEnforcementResponse`
        

    .. py:method:: enforce_compliance(cluster_id: str [, enforce_mode: Optional[EnforcePolicyComplianceForClusterEnforceMode], validate_only: Optional[bool]]) -> EnforceClusterComplianceResponse

        Updates a cluster to be compliant with the current version of its policy.

        If a cluster is updated while in a ``TERMINATED`` state, it will remain ``TERMINATED``. The next time
        the cluster is started, the new attributes will take effect.

        For clusters in other states, the behavior depends on the ``enforce_mode`` used.

        Clusters created by the Databricks Jobs, SDP, or Models services cannot be enforced by this API.
        Instead, use the "Enforce job policy compliance" API to enforce policy compliance on jobs.

        :param cluster_id: str
          The ID of the cluster you want to enforce policy compliance on.
        :param enforce_mode: :class:`EnforcePolicyComplianceForClusterEnforceMode` (optional)
          Determines how changes should be made to clusters that are not in ``TERMINATED`` state.

          - ``ENFORCE_IMMEDIATELY``: If the cluster is in a ``RUNNING`` state, it will be restarted so that
            the new attributes can take effect. For other states aside from ``TERMINATED`` state, the request
            will be rejected.
          - ``WAIT_FOR_TERMINATION``: The cluster is not immediately edited. Instead, a pending enforcement is
            scheduled to update the cluster when it terminates or restarts. When this occurs,
            ``enforce_result`` will contain ``DEFERRED``. Only workspace admins can use this mode.

          Regardless of the enforce mode, clusters in ``TERMINATED`` state are immediately edited.
        :param validate_only: bool (optional)
          If set, previews the changes that would be made to a cluster to enforce compliance but does not
          update the cluster.

        :returns: :class:`EnforceClusterComplianceResponse`
        

    .. py:method:: get_compliance(cluster_id: str) -> GetClusterComplianceResponse

        Returns the policy compliance status of a cluster. Clusters could be out of compliance if their policy
        was updated after the cluster was last edited.

        :param cluster_id: str
          The ID of the cluster to get the compliance status

        :returns: :class:`GetClusterComplianceResponse`
        

    .. py:method:: list_compliance(policy_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ClusterCompliance]

        Returns the policy compliance status of all clusters that use a given policy. Clusters could be out of
        compliance if their policy was updated after the cluster was last edited.

        :param policy_id: str
          Canonical unique identifier for the cluster policy.
        :param page_size: int (optional)
          Use this field to specify the maximum number of results to be returned by the server. The server may
          further constrain the maximum number of results returned in a single page.
        :param page_token: str (optional)
          A page token that can be used to navigate to the next page or previous page as returned by
          ``next_page_token`` or ``prev_page_token``.

        :returns: Iterator over :class:`ClusterCompliance`
        
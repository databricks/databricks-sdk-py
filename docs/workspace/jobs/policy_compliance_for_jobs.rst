``w.policy_compliance_for_jobs``: Policy compliance for jobs
============================================================
.. currentmodule:: databricks.sdk.service.jobs

.. py:class:: PolicyComplianceForJobsAPI

    The compliance APIs allow you to view and manage the policy compliance status of jobs in your workspace.
    This API currently only supports compliance controls for cluster policies.
    
    A job is in compliance if its cluster configurations satisfy the rules of all their respective cluster
    policies. A job could be out of compliance if a cluster policy it uses was updated after the job was last
    edited. The job is considered out of compliance if any of its clusters no longer comply with their updated
    policies.
    
    The get and list compliance APIs allow you to view the policy compliance status of a job. The enforce
    compliance API allows you to update a job so that it becomes compliant with all of its policies.

    .. py:method:: enforce_compliance(job_id: int [, validate_only: Optional[bool]]) -> EnforcePolicyComplianceResponse

        Enforce job policy compliance.
        
        Updates a job so the job clusters that are created when running the job (specified in `new_cluster`)
        are compliant with the current versions of their respective cluster policies. All-purpose clusters
        used in the job will not be updated.
        
        :param job_id: int
          The ID of the job you want to enforce policy compliance on.
        :param validate_only: bool (optional)
          If set, previews changes made to the job to comply with its policy, but does not update the job.
        
        :returns: :class:`EnforcePolicyComplianceResponse`
        

    .. py:method:: get_compliance(job_id: int) -> GetPolicyComplianceResponse

        Get job policy compliance.
        
        Returns the policy compliance status of a job. Jobs could be out of compliance if a cluster policy
        they use was updated after the job was last edited and some of its job clusters no longer comply with
        their updated policies.
        
        :param job_id: int
          The ID of the job whose compliance status you are requesting.
        
        :returns: :class:`GetPolicyComplianceResponse`
        

    .. py:method:: list_compliance(policy_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[JobCompliance]

        List job policy compliance.
        
        Returns the policy compliance status of all jobs that use a given policy. Jobs could be out of
        compliance if a cluster policy they use was updated after the job was last edited and its job clusters
        no longer comply with the updated policy.
        
        :param policy_id: str
          Canonical unique identifier for the cluster policy.
        :param page_size: int (optional)
          Use this field to specify the maximum number of results to be returned by the server. The server may
          further constrain the maximum number of results returned in a single page.
        :param page_token: str (optional)
          A page token that can be used to navigate to the next page or previous page as returned by
          `next_page_token` or `prev_page_token`.
        
        :returns: Iterator over :class:`JobCompliance`
        
``w.policy_families``: Policy Families
======================================
.. currentmodule:: databricks.sdk.service.compute

.. py:class:: PolicyFamiliesAPI

    View available policy families. A policy family contains a policy definition providing best practices for
    configuring clusters for a particular use case.
    
    Databricks manages and provides policy families for several common cluster use cases. You cannot create,
    edit, or delete policy families.
    
    Policy families cannot be used directly to create clusters. Instead, you create cluster policies using a
    policy family. Cluster policies created using a policy family inherit the policy family's policy
    definition.

    .. py:method:: get(policy_family_id: str) -> PolicyFamily


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import compute
            
            w = WorkspaceClient()
            
            all = w.policy_families.list(compute.ListPolicyFamiliesRequest())
            
            first_family = w.policy_families.get(policy_family_id=all[0].policy_family_id)

        Get policy family information.
        
        Retrieve the information for an policy family based on its identifier.
        
        :param policy_family_id: str
        
        :returns: :class:`PolicyFamily`
        

    .. py:method:: list( [, max_results: Optional[int], page_token: Optional[str]]) -> Iterator[PolicyFamily]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import compute
            
            w = WorkspaceClient()
            
            all = w.policy_families.list(compute.ListPolicyFamiliesRequest())

        List policy families.
        
        Retrieve a list of policy families. This API is paginated.
        
        :param max_results: int (optional)
          The max number of policy families to return.
        :param page_token: str (optional)
          A token that can be used to get the next page of results.
        
        :returns: Iterator over :class:`PolicyFamily`
        
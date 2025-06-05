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

    .. py:method:: get(policy_family_id: str [, version: Optional[int]]) -> PolicyFamily


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import compute
            
            w = WorkspaceClient()
            
            all = w.policy_families.list(compute.ListPolicyFamiliesRequest())
            
            first_family = w.policy_families.get(policy_family_id=all[0].policy_family_id)

        Get policy family information.
        
        Retrieve the information for an policy family based on its identifier and version
        
        :param policy_family_id: str
          The family ID about which to retrieve information.
        :param version: int (optional)
          The version number for the family to fetch. Defaults to the latest version.
        
        :returns: :class:`PolicyFamily`
        

    .. py:method:: list( [, max_results: Optional[int], page_token: Optional[str]]) -> Iterator[PolicyFamily]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import compute
            
            w = WorkspaceClient()
            
            all = w.policy_families.list(compute.ListPolicyFamiliesRequest())

        List policy families.
        
        Returns the list of policy definition types available to use at their latest version. This API is
        paginated.
        
        :param max_results: int (optional)
          Maximum number of policy families to return.
        :param page_token: str (optional)
          A token that can be used to get the next page of results.
        
        :returns: Iterator over :class:`PolicyFamily`
        
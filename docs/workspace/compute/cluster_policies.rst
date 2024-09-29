``w.cluster_policies``: Cluster Policies
========================================
.. currentmodule:: databricks.sdk.service.compute

.. py:class:: ClusterPoliciesAPI

    You can use cluster policies to control users' ability to configure clusters based on a set of rules.
    These rules specify which attributes or attribute values can be used during cluster creation. Cluster
    policies have ACLs that limit their use to specific users and groups.
    
    With cluster policies, you can: - Auto-install cluster libraries on the next restart by listing them in
    the policy's "libraries" field (Public Preview). - Limit users to creating clusters with the prescribed
    settings. - Simplify the user interface, enabling more users to create clusters, by fixing and hiding some
    fields. - Manage costs by setting limits on attributes that impact the hourly rate.
    
    Cluster policy permissions limit which policies a user can select in the Policy drop-down when the user
    creates a cluster: - A user who has unrestricted cluster create permission can select the Unrestricted
    policy and create fully-configurable clusters. - A user who has both unrestricted cluster create
    permission and access to cluster policies can select the Unrestricted policy and policies they have access
    to. - A user that has access to only cluster policies, can select the policies they have access to.
    
    If no policies exist in the workspace, the Policy drop-down doesn't appear. Only admin users can create,
    edit, and delete policies. Admin users also have access to all policies.

    .. py:method:: create( [, definition: Optional[str], description: Optional[str], libraries: Optional[List[Library]], max_clusters_per_user: Optional[int], name: Optional[str], policy_family_definition_overrides: Optional[str], policy_family_id: Optional[str]]) -> CreatePolicyResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.cluster_policies.create(name=f'sdk-{time.time_ns()}',
                                                definition="""{
                        "spark_conf.spark.databricks.delta.preview.enabled": {
                            "type": "fixed",
                            "value": true
                        }
                    }
            """)
            
            # cleanup
            w.cluster_policies.delete(policy_id=created.policy_id)

        Create a new policy.
        
        Creates a new policy with prescribed settings.
        
        :param definition: str (optional)
          Policy definition document expressed in [Databricks Cluster Policy Definition Language].
          
          [Databricks Cluster Policy Definition Language]: https://docs.databricks.com/administration-guide/clusters/policy-definition.html
        :param description: str (optional)
          Additional human-readable description of the cluster policy.
        :param libraries: List[:class:`Library`] (optional)
          A list of libraries to be installed on the next cluster restart that uses this policy. The maximum
          number of libraries is 500.
        :param max_clusters_per_user: int (optional)
          Max number of clusters per user that can be active using this policy. If not present, there is no
          max limit.
        :param name: str (optional)
          Cluster Policy name requested by the user. This has to be unique. Length must be between 1 and 100
          characters.
        :param policy_family_definition_overrides: str (optional)
          Policy definition JSON document expressed in [Databricks Policy Definition Language]. The JSON
          document must be passed as a string and cannot be embedded in the requests.
          
          You can use this to customize the policy definition inherited from the policy family. Policy rules
          specified here are merged into the inherited policy definition.
          
          [Databricks Policy Definition Language]: https://docs.databricks.com/administration-guide/clusters/policy-definition.html
        :param policy_family_id: str (optional)
          ID of the policy family. The cluster policy's policy definition inherits the policy family's policy
          definition.
          
          Cannot be used with `definition`. Use `policy_family_definition_overrides` instead to customize the
          policy definition.
        
        :returns: :class:`CreatePolicyResponse`
        

    .. py:method:: delete(policy_id: str)

        Delete a cluster policy.
        
        Delete a policy for a cluster. Clusters governed by this policy can still run, but cannot be edited.
        
        :param policy_id: str
          The ID of the policy to delete.
        
        
        

    .. py:method:: edit(policy_id: str [, definition: Optional[str], description: Optional[str], libraries: Optional[List[Library]], max_clusters_per_user: Optional[int], name: Optional[str], policy_family_definition_overrides: Optional[str], policy_family_id: Optional[str]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.cluster_policies.create(name=f'sdk-{time.time_ns()}',
                                                definition="""{
                        "spark_conf.spark.databricks.delta.preview.enabled": {
                            "type": "fixed",
                            "value": true
                        }
                    }
            """)
            
            policy = w.cluster_policies.get(policy_id=created.policy_id)
            
            w.cluster_policies.edit(policy_id=policy.policy_id,
                                    name=policy.name,
                                    definition="""{
                        "spark_conf.spark.databricks.delta.preview.enabled": {
                            "type": "fixed",
                            "value": false
                        }
                    }
            """)
            
            # cleanup
            w.cluster_policies.delete(policy_id=created.policy_id)

        Update a cluster policy.
        
        Update an existing policy for cluster. This operation may make some clusters governed by the previous
        policy invalid.
        
        :param policy_id: str
          The ID of the policy to update.
        :param definition: str (optional)
          Policy definition document expressed in [Databricks Cluster Policy Definition Language].
          
          [Databricks Cluster Policy Definition Language]: https://docs.databricks.com/administration-guide/clusters/policy-definition.html
        :param description: str (optional)
          Additional human-readable description of the cluster policy.
        :param libraries: List[:class:`Library`] (optional)
          A list of libraries to be installed on the next cluster restart that uses this policy. The maximum
          number of libraries is 500.
        :param max_clusters_per_user: int (optional)
          Max number of clusters per user that can be active using this policy. If not present, there is no
          max limit.
        :param name: str (optional)
          Cluster Policy name requested by the user. This has to be unique. Length must be between 1 and 100
          characters.
        :param policy_family_definition_overrides: str (optional)
          Policy definition JSON document expressed in [Databricks Policy Definition Language]. The JSON
          document must be passed as a string and cannot be embedded in the requests.
          
          You can use this to customize the policy definition inherited from the policy family. Policy rules
          specified here are merged into the inherited policy definition.
          
          [Databricks Policy Definition Language]: https://docs.databricks.com/administration-guide/clusters/policy-definition.html
        :param policy_family_id: str (optional)
          ID of the policy family. The cluster policy's policy definition inherits the policy family's policy
          definition.
          
          Cannot be used with `definition`. Use `policy_family_definition_overrides` instead to customize the
          policy definition.
        
        
        

    .. py:method:: get(policy_id: str) -> Policy


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.cluster_policies.create(name=f'sdk-{time.time_ns()}',
                                                definition="""{
                        "spark_conf.spark.databricks.delta.preview.enabled": {
                            "type": "fixed",
                            "value": true
                        }
                    }
            """)
            
            policy = w.cluster_policies.get(policy_id=created.policy_id)
            
            # cleanup
            w.cluster_policies.delete(policy_id=created.policy_id)

        Get a cluster policy.
        
        Get a cluster policy entity. Creation and editing is available to admins only.
        
        :param policy_id: str
          Canonical unique identifier for the Cluster Policy.
        
        :returns: :class:`Policy`
        

    .. py:method:: get_permission_levels(cluster_policy_id: str) -> GetClusterPolicyPermissionLevelsResponse

        Get cluster policy permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param cluster_policy_id: str
          The cluster policy for which to get or manage permissions.
        
        :returns: :class:`GetClusterPolicyPermissionLevelsResponse`
        

    .. py:method:: get_permissions(cluster_policy_id: str) -> ClusterPolicyPermissions

        Get cluster policy permissions.
        
        Gets the permissions of a cluster policy. Cluster policies can inherit permissions from their root
        object.
        
        :param cluster_policy_id: str
          The cluster policy for which to get or manage permissions.
        
        :returns: :class:`ClusterPolicyPermissions`
        

    .. py:method:: list( [, sort_column: Optional[ListSortColumn], sort_order: Optional[ListSortOrder]]) -> Iterator[Policy]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import compute
            
            w = WorkspaceClient()
            
            all = w.cluster_policies.list(compute.ListClusterPoliciesRequest())

        List cluster policies.
        
        Returns a list of policies accessible by the requesting user.
        
        :param sort_column: :class:`ListSortColumn` (optional)
          The cluster policy attribute to sort by. * `POLICY_CREATION_TIME` - Sort result list by policy
          creation time. * `POLICY_NAME` - Sort result list by policy name.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order in which the policies get listed. * `DESC` - Sort result list in descending order. * `ASC`
          - Sort result list in ascending order.
        
        :returns: Iterator over :class:`Policy`
        

    .. py:method:: set_permissions(cluster_policy_id: str [, access_control_list: Optional[List[ClusterPolicyAccessControlRequest]]]) -> ClusterPolicyPermissions

        Set cluster policy permissions.
        
        Sets permissions on a cluster policy. Cluster policies can inherit permissions from their root object.
        
        :param cluster_policy_id: str
          The cluster policy for which to get or manage permissions.
        :param access_control_list: List[:class:`ClusterPolicyAccessControlRequest`] (optional)
        
        :returns: :class:`ClusterPolicyPermissions`
        

    .. py:method:: update_permissions(cluster_policy_id: str [, access_control_list: Optional[List[ClusterPolicyAccessControlRequest]]]) -> ClusterPolicyPermissions

        Update cluster policy permissions.
        
        Updates the permissions on a cluster policy. Cluster policies can inherit permissions from their root
        object.
        
        :param cluster_policy_id: str
          The cluster policy for which to get or manage permissions.
        :param access_control_list: List[:class:`ClusterPolicyAccessControlRequest`] (optional)
        
        :returns: :class:`ClusterPolicyPermissions`
        
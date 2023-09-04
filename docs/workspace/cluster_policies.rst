Cluster Policies
================
.. py:class:: ClusterPoliciesAPI

    Cluster policy limits the ability to configure clusters based on a set of rules. The policy rules limit
    the attributes or attribute values available for cluster creation. Cluster policies have ACLs that limit
    their use to specific users and groups.
    
    Cluster policies let you limit users to create clusters with prescribed settings, simplify the user
    interface and enable more users to create their own clusters (by fixing and hiding some values), control
    cost by limiting per cluster maximum cost (by setting limits on attributes whose values contribute to
    hourly price).
    
    Cluster policy permissions limit which policies a user can select in the Policy drop-down when the user
    creates a cluster: - A user who has cluster create permission can select the Unrestricted policy and
    create fully-configurable clusters. - A user who has both cluster create permission and access to cluster
    policies can select the Unrestricted policy and policies they have access to. - A user that has access to
    only cluster policies, can select the policies they have access to.
    
    If no policies have been created in the workspace, the Policy drop-down does not display.
    
    Only admin users can create, edit, and delete policies. Admin users also have access to all policies.

    .. py:method:: create(name [, definition, description, max_clusters_per_user, policy_family_definition_overrides, policy_family_id])

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
        
        :param name: str
          Cluster Policy name requested by the user. This has to be unique. Length must be between 1 and 100
          characters.
        :param definition: str (optional)
          Policy definition document expressed in Databricks Cluster Policy Definition Language.
        :param description: str (optional)
          Additional human-readable description of the cluster policy.
        :param max_clusters_per_user: int (optional)
          Max number of clusters per user that can be active using this policy. If not present, there is no
          max limit.
        :param policy_family_definition_overrides: str (optional)
          Policy definition JSON document expressed in Databricks Policy Definition Language. The JSON
          document must be passed as a string and cannot be embedded in the requests.
          
          You can use this to customize the policy definition inherited from the policy family. Policy rules
          specified here are merged into the inherited policy definition.
        :param policy_family_id: str (optional)
          ID of the policy family. The cluster policy's policy definition inherits the policy family's policy
          definition.
          
          Cannot be used with `definition`. Use `policy_family_definition_overrides` instead to customize the
          policy definition.
        
        :returns: :class:`CreatePolicyResponse`
        

    .. py:method:: delete(policy_id)

        Delete a cluster policy.
        
        Delete a policy for a cluster. Clusters governed by this policy can still run, but cannot be edited.
        
        :param policy_id: str
          The ID of the policy to delete.
        
        
        

    .. py:method:: edit(policy_id, name [, definition, description, max_clusters_per_user, policy_family_definition_overrides, policy_family_id])

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
        :param name: str
          Cluster Policy name requested by the user. This has to be unique. Length must be between 1 and 100
          characters.
        :param definition: str (optional)
          Policy definition document expressed in Databricks Cluster Policy Definition Language.
        :param description: str (optional)
          Additional human-readable description of the cluster policy.
        :param max_clusters_per_user: int (optional)
          Max number of clusters per user that can be active using this policy. If not present, there is no
          max limit.
        :param policy_family_definition_overrides: str (optional)
          Policy definition JSON document expressed in Databricks Policy Definition Language. The JSON
          document must be passed as a string and cannot be embedded in the requests.
          
          You can use this to customize the policy definition inherited from the policy family. Policy rules
          specified here are merged into the inherited policy definition.
        :param policy_family_id: str (optional)
          ID of the policy family. The cluster policy's policy definition inherits the policy family's policy
          definition.
          
          Cannot be used with `definition`. Use `policy_family_definition_overrides` instead to customize the
          policy definition.
        
        
        

    .. py:method:: get(policy_id)

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
          Canonical unique identifier for the cluster policy.
        
        :returns: :class:`Policy`
        

    .. py:method:: get_permission_levels(cluster_policy_id)

        Get cluster policy permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param cluster_policy_id: str
          The cluster policy for which to get or manage permissions.
        
        :returns: :class:`GetClusterPolicyPermissionLevelsResponse`
        

    .. py:method:: get_permissions(cluster_policy_id)

        Get cluster policy permissions.
        
        Gets the permissions of a cluster policy. Cluster policies can inherit permissions from their root
        object.
        
        :param cluster_policy_id: str
          The cluster policy for which to get or manage permissions.
        
        :returns: :class:`ClusterPolicyPermissions`
        

    .. py:method:: list( [, sort_column, sort_order])

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
        

    .. py:method:: set_permissions(cluster_policy_id [, access_control_list])

        Set cluster policy permissions.
        
        Sets permissions on a cluster policy. Cluster policies can inherit permissions from their root object.
        
        :param cluster_policy_id: str
          The cluster policy for which to get or manage permissions.
        :param access_control_list: List[:class:`ClusterPolicyAccessControlRequest`] (optional)
        
        :returns: :class:`ClusterPolicyPermissions`
        

    .. py:method:: update_permissions(cluster_policy_id [, access_control_list])

        Update cluster policy permissions.
        
        Updates the permissions on a cluster policy. Cluster policies can inherit permissions from their root
        object.
        
        :param cluster_policy_id: str
          The cluster policy for which to get or manage permissions.
        :param access_control_list: List[:class:`ClusterPolicyAccessControlRequest`] (optional)
        
        :returns: :class:`ClusterPolicyPermissions`
        
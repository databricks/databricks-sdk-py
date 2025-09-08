``a.workspace_network_configuration``: Workspace Network Option
===============================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: WorkspaceNetworkConfigurationAPI

    These APIs allow configuration of network settings for Databricks workspaces by selecting which network
    policy to associate with the workspace. Each workspace is always associated with exactly one network
    policy that controls which network destinations can be accessed from the Databricks environment. By
    default, workspaces are associated with the 'default-policy' network policy. You cannot create or delete a
    workspace's network option, only update it to associate the workspace with a different policy

    .. py:method:: get_workspace_network_option_rpc(workspace_id: int) -> WorkspaceNetworkOption

        Gets the network option for a workspace. Every workspace has exactly one network policy binding, with
        'default-policy' used if no explicit assignment exists.
        
        :param workspace_id: int
          The workspace ID.
        
        :returns: :class:`WorkspaceNetworkOption`
        

    .. py:method:: update_workspace_network_option_rpc(workspace_id: int, workspace_network_option: WorkspaceNetworkOption) -> WorkspaceNetworkOption

        Updates the network option for a workspace. This operation associates the workspace with the specified
        network policy. To revert to the default policy, specify 'default-policy' as the network_policy_id.
        
        :param workspace_id: int
          The workspace ID.
        :param workspace_network_option: :class:`WorkspaceNetworkOption`
          The network option details for the workspace.
        
        :returns: :class:`WorkspaceNetworkOption`
        
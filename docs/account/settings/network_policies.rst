``a.network_policies``: Network Policies
========================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: NetworkPoliciesAPI

    These APIs manage network policies for this account. Network policies control which network destinations
    can be accessed from the Databricks environment. Each Databricks account includes a default policy named
    'default-policy'. 'default-policy' is associated with any workspace lacking an explicit network policy
    assignment, and is automatically associated with each newly created workspace. 'default-policy' is
    reserved and cannot be deleted, but it can be updated to customize the default network access rules for
    your account.

    .. py:method:: create_network_policy_rpc(network_policy: AccountNetworkPolicy) -> AccountNetworkPolicy

        Creates a new network policy to manage which network destinations can be accessed from the Databricks
        environment.

        :param network_policy: :class:`AccountNetworkPolicy`
          Network policy configuration details.

        :returns: :class:`AccountNetworkPolicy`
        

    .. py:method:: delete_network_policy_rpc(network_policy_id: str)

        Deletes a network policy. Cannot be called on 'default-policy'.

        :param network_policy_id: str
          The unique identifier of the network policy to delete.


        

    .. py:method:: get_network_policy_rpc(network_policy_id: str) -> AccountNetworkPolicy

        Gets a network policy.

        :param network_policy_id: str
          The unique identifier of the network policy to retrieve.

        :returns: :class:`AccountNetworkPolicy`
        

    .. py:method:: list_network_policies_rpc( [, page_token: Optional[str]]) -> Iterator[AccountNetworkPolicy]

        Gets an array of network policies.

        :param page_token: str (optional)
          Pagination token to go to next page based on previous query.

        :returns: Iterator over :class:`AccountNetworkPolicy`
        

    .. py:method:: update_network_policy_rpc(network_policy_id: str, network_policy: AccountNetworkPolicy) -> AccountNetworkPolicy

        Updates a network policy. This allows you to modify the configuration of a network policy.

        :param network_policy_id: str
          The unique identifier for the network policy.
        :param network_policy: :class:`AccountNetworkPolicy`
          Updated network policy configuration details.

        :returns: :class:`AccountNetworkPolicy`
        
``a.networks``: Network configurations
======================================
.. currentmodule:: databricks.sdk.service.provisioning

.. py:class:: NetworksAPI

    These APIs manage network configurations for customer-managed VPCs (optional). Its ID is used when
    creating a new workspace if you use customer-managed VPCs.

    .. py:method:: create(network_name: str [, gcp_network_info: Optional[GcpNetworkInfo], security_group_ids: Optional[List[str]], subnet_ids: Optional[List[str]], vpc_endpoints: Optional[NetworkVpcEndpoints], vpc_id: Optional[str]]) -> Network


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            netw = a.networks.create(network_name=f'sdk-{time.time_ns()}',
                                     vpc_id=hex(time.time_ns())[2:],
                                     subnet_ids=[hex(time.time_ns())[2:],
                                                 hex(time.time_ns())[2:]],
                                     security_group_ids=[hex(time.time_ns())[2:]])

        Create network configuration.
        
        Creates a Databricks network configuration that represents an VPC and its resources. The VPC will be
        used for new Databricks clusters. This requires a pre-existing VPC and subnets.
        
        :param network_name: str
          The human-readable name of the network configuration.
        :param gcp_network_info: :class:`GcpNetworkInfo` (optional)
          The Google Cloud specific information for this network (for example, the VPC ID, subnet ID, and
          secondary IP ranges).
        :param security_group_ids: List[str] (optional)
          IDs of one to five security groups associated with this network. Security group IDs **cannot** be
          used in multiple network configurations.
        :param subnet_ids: List[str] (optional)
          IDs of at least two subnets associated with this network. Subnet IDs **cannot** be used in multiple
          network configurations.
        :param vpc_endpoints: :class:`NetworkVpcEndpoints` (optional)
          If specified, contains the VPC endpoints used to allow cluster communication from this VPC over [AWS
          PrivateLink].
          
          [AWS PrivateLink]: https://aws.amazon.com/privatelink/
        :param vpc_id: str (optional)
          The ID of the VPC associated with this network. VPC IDs can be used in multiple network
          configurations.
        
        :returns: :class:`Network`
        

    .. py:method:: delete(network_id: str)

        Delete a network configuration.
        
        Deletes a Databricks network configuration, which represents a cloud VPC and its resources. You cannot
        delete a network that is associated with a workspace.
        
        This operation is available only if your account is on the E2 version of the platform.
        
        :param network_id: str
          Databricks Account API network configuration ID.
        
        
        

    .. py:method:: get(network_id: str) -> Network


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            netw = a.networks.create(network_name=f'sdk-{time.time_ns()}',
                                     vpc_id=hex(time.time_ns())[2:],
                                     subnet_ids=[hex(time.time_ns())[2:],
                                                 hex(time.time_ns())[2:]],
                                     security_group_ids=[hex(time.time_ns())[2:]])
            
            by_id = a.networks.get(network_id=netw.network_id)

        Get a network configuration.
        
        Gets a Databricks network configuration, which represents a cloud VPC and its resources.
        
        :param network_id: str
          Databricks Account API network configuration ID.
        
        :returns: :class:`Network`
        

    .. py:method:: list() -> Iterator[Network]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            configs = a.networks.list()

        Get all network configurations.
        
        Gets a list of all Databricks network configurations for an account, specified by ID.
        
        This operation is available only if your account is on the E2 version of the platform.
        
        :returns: Iterator over :class:`Network`
        
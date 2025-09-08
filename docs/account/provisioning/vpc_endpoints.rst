``a.vpc_endpoints``: VPC Endpoint Configurations
================================================
.. currentmodule:: databricks.sdk.service.provisioning

.. py:class:: VpcEndpointsAPI

    These APIs manage VPC endpoint configurations for this account.

    .. py:method:: create(vpc_endpoint_name: str [, aws_vpc_endpoint_id: Optional[str], gcp_vpc_endpoint_info: Optional[GcpVpcEndpointInfo], region: Optional[str]]) -> VpcEndpoint


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            created = a.vpc_endpoints.create(
                aws_vpc_endpoint_id=os.environ["TEST_RELAY_VPC_ENDPOINT"],
                region=os.environ["AWS_REGION"],
                vpc_endpoint_name=f"sdk-{time.time_ns()}",
            )
            
            # cleanup
            a.vpc_endpoints.delete(vpc_endpoint_id=created.vpc_endpoint_id)

        Creates a VPC endpoint configuration, which represents a [VPC endpoint] object in AWS used to
        communicate privately with Databricks over [AWS PrivateLink].
        
        After you create the VPC endpoint configuration, the Databricks [endpoint service] automatically
        accepts the VPC endpoint.
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        [VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html
        [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html
        
        :param vpc_endpoint_name: str
          The human-readable name of the storage configuration.
        :param aws_vpc_endpoint_id: str (optional)
          The ID of the VPC endpoint object in AWS.
        :param gcp_vpc_endpoint_info: :class:`GcpVpcEndpointInfo` (optional)
        :param region: str (optional)
          The AWS region in which this VPC endpoint object exists.
        
        :returns: :class:`VpcEndpoint`
        

    .. py:method:: delete(vpc_endpoint_id: str)

        Deletes a VPC endpoint configuration, which represents an [AWS VPC endpoint] that can communicate
        privately with Databricks over [AWS PrivateLink].
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [AWS VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        
        :param vpc_endpoint_id: str
          Databricks VPC endpoint ID.
        
        
        

    .. py:method:: get(vpc_endpoint_id: str) -> VpcEndpoint


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            created = a.vpc_endpoints.create(
                aws_vpc_endpoint_id=os.environ["TEST_RELAY_VPC_ENDPOINT"],
                region=os.environ["AWS_REGION"],
                vpc_endpoint_name=f"sdk-{time.time_ns()}",
            )
            
            by_id = a.vpc_endpoints.get(vpc_endpoint_id=created.vpc_endpoint_id)
            
            # cleanup
            a.vpc_endpoints.delete(vpc_endpoint_id=created.vpc_endpoint_id)

        Gets a VPC endpoint configuration, which represents a [VPC endpoint] object in AWS used to communicate
        privately with Databricks over [AWS PrivateLink].
        
        [AWS PrivateLink]: https://aws.amazon.com/privatelink
        [VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html
        
        :param vpc_endpoint_id: str
          Databricks VPC endpoint ID.
        
        :returns: :class:`VpcEndpoint`
        

    .. py:method:: list() -> Iterator[VpcEndpoint]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            all = a.vpc_endpoints.list()

        Gets a list of all VPC endpoints for an account, specified by ID.
        
        Before configuring PrivateLink, read the [Databricks article about PrivateLink].
        
        [Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html
        
        
        :returns: Iterator over :class:`VpcEndpoint`
        
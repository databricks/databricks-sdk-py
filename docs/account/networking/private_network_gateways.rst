``a.private_network_gateways``: Private Network Gateways
========================================================
.. currentmodule:: databricks.sdk.service.networking

.. py:class:: PrivateNetworkGatewaysAPI

    These APIs manage private network gateways under network connectivity configurations.

    .. py:method:: create_private_network_gateway(parent: str, private_network_gateway: PrivateNetworkGateway [, request_id: Optional[str]]) -> CreatePrivateNetworkGatewayOperation

        Creates a private network gateway.

        :param parent: str
          The network connectivity configuration that will contain the gateway.
        :param private_network_gateway: :class:`PrivateNetworkGateway`
          The gateway to create.
        :param request_id: str (optional)
          A unique identifier for this request. The request is idempotent when this is provided.

        :returns: :class:`Operation`
        

    .. py:method:: delete_private_network_gateway(name: str)

        Permanently deletes a private network gateway.

        :param name: str
          The canonical resource name of the gateway.


        

    .. py:method:: get_private_network_gateway(name: str) -> PrivateNetworkGateway

        Gets a private network gateway.

        :param name: str
          The canonical resource name of the gateway.

        :returns: :class:`PrivateNetworkGateway`
        

    .. py:method:: get_private_network_gateway_operation(name: str) -> Operation

        Gets the status of a private network gateway create operation.

        :param name: str
          The name of the operation resource.

        :returns: :class:`Operation`
        

    .. py:method:: list_private_network_gateways(parent: str [, page_token: Optional[str]]) -> Iterator[PrivateNetworkGateway]

        Lists private network gateways under a network connectivity configuration.

        :param parent: str
          The network connectivity configuration containing the gateways.
        :param page_token: str (optional)
          An opaque token returned by a previous list request.

        :returns: Iterator over :class:`PrivateNetworkGateway`
        

    .. py:method:: update_private_network_gateway(name: str, private_network_gateway: PrivateNetworkGateway, update_mask: FieldMask) -> PrivateNetworkGateway

        Updates a private network gateway.

        :param name: str
          The canonical resource name of the gateway, in the form
          ``accounts/{account_id}/network-connectivity-configs/{ncc_id}/private-network-gateways/{gateway_id}``.
        :param private_network_gateway: :class:`PrivateNetworkGateway`
          The gateway containing the desired mutable field values.
        :param update_mask: FieldMask
          The fields to update.

        :returns: :class:`PrivateNetworkGateway`
        
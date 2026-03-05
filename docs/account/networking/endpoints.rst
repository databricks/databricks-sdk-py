``a.endpoints``: Networking Endpoints
=====================================
.. currentmodule:: databricks.sdk.service.networking

.. py:class:: EndpointsAPI

    These APIs manage endpoint configurations for this account.

    .. py:method:: create_endpoint(parent: str, endpoint: Endpoint) -> Endpoint

        Creates a new network connectivity endpoint that enables private connectivity between your network
        resources and Databricks services.

        After creation, the endpoint is initially in the PENDING state. The Databricks endpoint service
        automatically reviews and approves the endpoint within a few minutes. Use the GET method to retrieve
        the latest endpoint state.

        An endpoint can be used only after it reaches the APPROVED state.

        :param parent: str
          The parent resource name of the account under which the endpoint is created. Format:
          `accounts/{account_id}`.
        :param endpoint: :class:`Endpoint`

        :returns: :class:`Endpoint`
        

    .. py:method:: delete_endpoint(name: str)

        Deletes a network endpoint. This will remove the endpoint configuration from Databricks. Depending on
        the endpoint type and use case, you may also need to delete corresponding network resources in your
        cloud provider account.

        :param name: str


        

    .. py:method:: get_endpoint(name: str) -> Endpoint

        Gets details of a specific network endpoint.

        :param name: str

        :returns: :class:`Endpoint`
        

    .. py:method:: list_endpoints(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Endpoint]

        Lists all network connectivity endpoints for the account.

        :param parent: str
          The parent resource name of the account to list endpoints for. Format: `accounts/{account_id}`.
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Endpoint`
        
``w.vector_search_endpoints``: Endpoints
========================================
.. currentmodule:: databricks.sdk.service.vectorsearch

.. py:class:: VectorSearchEndpointsAPI

    **Endpoint**: Represents the compute resources to host vector search indexes.

    .. py:method:: create_endpoint(name: str, endpoint_type: EndpointType) -> Wait[EndpointInfo]

        Create an endpoint.

Create a new endpoint.

:param name: str
  Name of endpoint
:param endpoint_type: :class:`EndpointType`
  Type of endpoint.

:returns:
  Long-running operation waiter for :class:`EndpointInfo`.
  See :method:wait_get_endpoint_vector_search_endpoint_online for more details.


    .. py:method:: create_endpoint_and_wait(name: str, endpoint_type: EndpointType, timeout: datetime.timedelta = 0:20:00) -> EndpointInfo


    .. py:method:: delete_endpoint(endpoint_name: str)

        Delete an endpoint.

:param endpoint_name: str
  Name of the endpoint




    .. py:method:: get_endpoint(endpoint_name: str) -> EndpointInfo

        Get an endpoint.

:param endpoint_name: str
  Name of the endpoint

:returns: :class:`EndpointInfo`


    .. py:method:: list_endpoints( [, page_token: Optional[str]]) -> Iterator[EndpointInfo]

        List all endpoints.

:param page_token: str (optional)
  Token for pagination

:returns: Iterator over :class:`EndpointInfo`


    .. py:method:: wait_get_endpoint_vector_search_endpoint_online(endpoint_name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[EndpointInfo], None]]) -> EndpointInfo

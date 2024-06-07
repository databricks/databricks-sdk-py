``w.endpoints``: Online Endpoints
=================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: EndpointsAPI

    Endpoints are used to connect to PG clusters.

    .. py:method:: create( [, endpoint: Optional[Endpoint]]) -> Endpoint

        Create an Endpoint.
        
        :param endpoint: :class:`Endpoint` (optional)
          Endpoint
        
        :returns: :class:`Endpoint`
        

    .. py:method:: delete(name: str)

        Delete an Endpoint.
        
        :param name: str
        
        
        

    .. py:method:: get(name: str) -> Endpoint

        Get an Endpoint.
        
        :param name: str
        
        :returns: :class:`Endpoint`
        
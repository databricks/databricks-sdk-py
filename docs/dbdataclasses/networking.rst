Networking
==========

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.networking`` module.

.. py:currentmodule:: databricks.sdk.service.networking
.. autoclass:: AwsVpcEndpointInfo
   :members:
   :undoc-members:

.. autoclass:: AzurePrivateEndpointInfo
   :members:
   :undoc-members:

.. autoclass:: Endpoint
   :members:
   :undoc-members:

.. py:class:: EndpointState

   .. py:attribute:: APPROVED
      :value: "APPROVED"

   .. py:attribute:: DISCONNECTED
      :value: "DISCONNECTED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: PENDING
      :value: "PENDING"

.. py:class:: EndpointUseCase

   .. py:attribute:: SERVICE_DIRECT
      :value: "SERVICE_DIRECT"

.. autoclass:: GcpPscEndpointInfo
   :members:
   :undoc-members:

.. autoclass:: ListEndpointsResponse
   :members:
   :undoc-members:

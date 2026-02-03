Agent Bricks
============

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.agentbricks`` module.

.. py:currentmodule:: databricks.sdk.service.agentbricks
.. autoclass:: CustomLlm
   :members:
   :undoc-members:

.. autoclass:: Dataset
   :members:
   :undoc-members:

.. py:class:: HostType

   Enum representing the type of Databricks host.

   .. py:attribute:: ACCOUNTS
      :value: "ACCOUNTS"

   .. py:attribute:: WORKSPACE
      :value: "WORKSPACE"

   .. py:attribute:: UNIFIED
      :value: "UNIFIED"

.. py:class:: State

   States of Custom LLM optimization lifecycle.

   .. py:attribute:: CANCELLED
      :value: "CANCELLED"

   .. py:attribute:: COMPLETED
      :value: "COMPLETED"

   .. py:attribute:: CREATED
      :value: "CREATED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

.. autoclass:: Table
   :members:
   :undoc-members:

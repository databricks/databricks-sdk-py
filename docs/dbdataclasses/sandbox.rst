Sandbox
=======

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.sandbox`` module.

.. py:currentmodule:: databricks.sdk.service.sandbox
.. autoclass:: ComputeSpec
   :members:
   :undoc-members:

.. autoclass:: ListSandboxesResponse
   :members:
   :undoc-members:

.. autoclass:: Sandbox
   :members:
   :undoc-members:

.. autoclass:: SandboxSpec
   :members:
   :undoc-members:

.. py:class:: SandboxState

   Lifecycle state of a Sandbox resource. STOPPING is the transient state surfaced while a teardown (Stop, DeleteSandbox, auto-terminate, provisioning failure) is in flight but the sandbox row still exists; the row settles to STOPPED once the workflow finishes.

   .. py:attribute:: SANDBOX_STATE_PENDING
      :value: "SANDBOX_STATE_PENDING"

   .. py:attribute:: SANDBOX_STATE_RUNNING
      :value: "SANDBOX_STATE_RUNNING"

   .. py:attribute:: SANDBOX_STATE_STOPPED
      :value: "SANDBOX_STATE_STOPPED"

   .. py:attribute:: SANDBOX_STATE_STOPPING
      :value: "SANDBOX_STATE_STOPPING"

.. autoclass:: SandboxStatus
   :members:
   :undoc-members:

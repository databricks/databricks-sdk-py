Sandbox
=======

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.sandbox`` module.

.. py:currentmodule:: databricks.sdk.service.sandbox
.. autoclass:: ComputeSpec
   :members:
   :undoc-members:

.. py:class:: ExecuteCommandStatus

   Terminal status of a unary command execution.

   .. py:attribute:: EXECUTE_COMMAND_STATUS_COMPLETED
      :value: "EXECUTE_COMMAND_STATUS_COMPLETED"

   .. py:attribute:: EXECUTE_COMMAND_STATUS_FAILED
      :value: "EXECUTE_COMMAND_STATUS_FAILED"

   .. py:attribute:: EXECUTE_COMMAND_STATUS_TIMED_OUT
      :value: "EXECUTE_COMMAND_STATUS_TIMED_OUT"

.. autoclass:: ExecuteCommandSyncResponse
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

   Lifecycle state of a Sandbox resource. STOPPING is the transient state while the sandbox is being stopped -- by a Stop request or inactivity auto-termination -- and settles to STOPPED once the operation completes.

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

Sandbox
=======

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.sandbox`` module.

.. py:currentmodule:: databricks.sdk.service.sandbox
.. autoclass:: Command
   :members:
   :undoc-members:

.. autoclass:: ComputeSpec
   :members:
   :undoc-members:

.. autoclass:: CreateDirectoryResponse
   :members:
   :undoc-members:

.. autoclass:: DeletePathResponse
   :members:
   :undoc-members:

.. autoclass:: EnvironmentSpec
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

.. autoclass:: GetMetadataResponse
   :members:
   :undoc-members:

.. autoclass:: ListCommandsResponse
   :members:
   :undoc-members:

.. autoclass:: ListDirectoryContentsResponse
   :members:
   :undoc-members:

.. autoclass:: ListSandboxesResponse
   :members:
   :undoc-members:

.. autoclass:: RenamePathResponse
   :members:
   :undoc-members:

.. autoclass:: Sandbox
   :members:
   :undoc-members:

.. autoclass:: SandboxFileInfo
   :members:
   :undoc-members:

.. py:class:: SandboxFileType

   Type of a sandbox filesystem entry without following its final symlink.

   .. py:attribute:: SANDBOX_FILE_TYPE_DIRECTORY
      :value: "SANDBOX_FILE_TYPE_DIRECTORY"

   .. py:attribute:: SANDBOX_FILE_TYPE_FILE
      :value: "SANDBOX_FILE_TYPE_FILE"

   .. py:attribute:: SANDBOX_FILE_TYPE_OTHER
      :value: "SANDBOX_FILE_TYPE_OTHER"

   .. py:attribute:: SANDBOX_FILE_TYPE_SYMLINK
      :value: "SANDBOX_FILE_TYPE_SYMLINK"

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

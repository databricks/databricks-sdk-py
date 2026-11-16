Statement Execution (Lakehouse//RT) V2
======================================

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.statementexecutionv2`` module.

.. py:currentmodule:: databricks.sdk.service.statementexecutionv2
.. autoclass:: BaseChunkInfo
   :members:
   :undoc-members:

.. autoclass:: CancelStatementResponse
   :members:
   :undoc-members:

.. autoclass:: ColumnInfo
   :members:
   :undoc-members:

.. py:class:: ColumnTypeName

   The name of the base data type. This doesn't include details for complex types such as STRUCT, MAP or ARRAY.

   .. py:attribute:: ARRAY
      :value: "ARRAY"

   .. py:attribute:: BINARY
      :value: "BINARY"

   .. py:attribute:: BOOLEAN
      :value: "BOOLEAN"

   .. py:attribute:: BYTE
      :value: "BYTE"

   .. py:attribute:: CHAR
      :value: "CHAR"

   .. py:attribute:: DATE
      :value: "DATE"

   .. py:attribute:: DECIMAL
      :value: "DECIMAL"

   .. py:attribute:: DOUBLE
      :value: "DOUBLE"

   .. py:attribute:: FLOAT
      :value: "FLOAT"

   .. py:attribute:: INT
      :value: "INT"

   .. py:attribute:: INTERVAL
      :value: "INTERVAL"

   .. py:attribute:: LONG
      :value: "LONG"

   .. py:attribute:: MAP
      :value: "MAP"

   .. py:attribute:: NULL
      :value: "NULL"

   .. py:attribute:: SHORT
      :value: "SHORT"

   .. py:attribute:: STRING
      :value: "STRING"

   .. py:attribute:: STRUCT
      :value: "STRUCT"

   .. py:attribute:: TIMESTAMP
      :value: "TIMESTAMP"

   .. py:attribute:: USER_DEFINED_TYPE
      :value: "USER_DEFINED_TYPE"

.. autoclass:: ExternalLink
   :members:
   :undoc-members:

.. py:class:: FetchDisposition

   .. py:attribute:: EXTERNAL_LINKS
      :value: "EXTERNAL_LINKS"

   .. py:attribute:: INLINE
      :value: "INLINE"

.. py:class:: Format

   The format of the result data.

   .. py:attribute:: ARROW_STREAM
      :value: "ARROW_STREAM"

   .. py:attribute:: CSV
      :value: "CSV"

   .. py:attribute:: JSON_ARRAY
      :value: "JSON_ARRAY"

.. autoclass:: QueryTag
   :members:
   :undoc-members:

.. autoclass:: ResultData
   :members:
   :undoc-members:

.. autoclass:: ResultManifest
   :members:
   :undoc-members:

.. autoclass:: Schema
   :members:
   :undoc-members:

.. autoclass:: ServiceError
   :members:
   :undoc-members:

.. py:class:: ServiceErrorCode

   Error codes that classify a failed statement execution.

   .. py:attribute:: ABORTED
      :value: "ABORTED"

   .. py:attribute:: ALREADY_EXISTS
      :value: "ALREADY_EXISTS"

   .. py:attribute:: BAD_REQUEST
      :value: "BAD_REQUEST"

   .. py:attribute:: CANCELLED
      :value: "CANCELLED"

   .. py:attribute:: DEADLINE_EXCEEDED
      :value: "DEADLINE_EXCEEDED"

   .. py:attribute:: INTERNAL_ERROR
      :value: "INTERNAL_ERROR"

   .. py:attribute:: IO_ERROR
      :value: "IO_ERROR"

   .. py:attribute:: NOT_FOUND
      :value: "NOT_FOUND"

   .. py:attribute:: RESOURCE_EXHAUSTED
      :value: "RESOURCE_EXHAUSTED"

   .. py:attribute:: SERVICE_UNDER_MAINTENANCE
      :value: "SERVICE_UNDER_MAINTENANCE"

   .. py:attribute:: TEMPORARILY_UNAVAILABLE
      :value: "TEMPORARILY_UNAVAILABLE"

   .. py:attribute:: UNAUTHENTICATED
      :value: "UNAUTHENTICATED"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

   .. py:attribute:: WORKSPACE_TEMPORARILY_UNAVAILABLE
      :value: "WORKSPACE_TEMPORARILY_UNAVAILABLE"

.. autoclass:: StatementParameter
   :members:
   :undoc-members:

.. autoclass:: StatementResponse
   :members:
   :undoc-members:

.. autoclass:: StatementStatus
   :members:
   :undoc-members:

.. py:class:: StatementStatusState

   Statement execution state.

   .. py:attribute:: CANCELED
      :value: "CANCELED"

   .. py:attribute:: CLOSED
      :value: "CLOSED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SUCCEEDED
      :value: "SUCCEEDED"

.. py:class:: TimeoutAction

   What happens when the statement execution outlives ``wait_timeout``.

   .. py:attribute:: CANCEL
      :value: "CANCEL"

   .. py:attribute:: CONTINUE
      :value: "CONTINUE"

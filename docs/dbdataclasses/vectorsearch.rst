Vector Search
=============

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.vectorsearch`` module.

.. py:currentmodule:: databricks.sdk.service.vectorsearch
.. autoclass:: ColumnInfo
   :members:
   :undoc-members:

.. autoclass:: CreateEndpoint
   :members:
   :undoc-members:

.. autoclass:: CreateVectorIndexRequest
   :members:
   :undoc-members:

.. autoclass:: CreateVectorIndexResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteDataResult
   :members:
   :undoc-members:

.. py:class:: DeleteDataStatus

   Status of the delete operation.

   .. py:attribute:: FAILURE
      :value: "FAILURE"

   .. py:attribute:: PARTIAL_SUCCESS
      :value: "PARTIAL_SUCCESS"

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

.. autoclass:: DeleteDataVectorIndexRequest
   :members:
   :undoc-members:

.. autoclass:: DeleteDataVectorIndexResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteEndpointResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteIndexResponse
   :members:
   :undoc-members:

.. autoclass:: DeltaSyncVectorIndexSpecRequest
   :members:
   :undoc-members:

.. autoclass:: DeltaSyncVectorIndexSpecResponse
   :members:
   :undoc-members:

.. autoclass:: DirectAccessVectorIndexSpec
   :members:
   :undoc-members:

.. autoclass:: EmbeddingSourceColumn
   :members:
   :undoc-members:

.. autoclass:: EmbeddingVectorColumn
   :members:
   :undoc-members:

.. autoclass:: EndpointInfo
   :members:
   :undoc-members:

.. autoclass:: EndpointStatus
   :members:
   :undoc-members:

.. py:class:: EndpointStatusState

   Current state of the endpoint

   .. py:attribute:: OFFLINE
      :value: "OFFLINE"

   .. py:attribute:: ONLINE
      :value: "ONLINE"

   .. py:attribute:: PROVISIONING
      :value: "PROVISIONING"

.. py:class:: EndpointType

   Type of endpoint.

   .. py:attribute:: STANDARD
      :value: "STANDARD"

.. autoclass:: ListEndpointResponse
   :members:
   :undoc-members:

.. autoclass:: ListValue
   :members:
   :undoc-members:

.. autoclass:: ListVectorIndexesResponse
   :members:
   :undoc-members:

.. autoclass:: MapStringValueEntry
   :members:
   :undoc-members:

.. autoclass:: MiniVectorIndex
   :members:
   :undoc-members:

.. py:class:: PipelineType

   Pipeline execution mode.
   - `TRIGGERED`: If the pipeline uses the triggered execution mode, the system stops processing after successfully refreshing the source table in the pipeline once, ensuring the table is updated based on the data available when the update started. - `CONTINUOUS`: If the pipeline uses continuous execution, the pipeline processes new data as it arrives in the source table to keep vector index fresh.

   .. py:attribute:: CONTINUOUS
      :value: "CONTINUOUS"

   .. py:attribute:: TRIGGERED
      :value: "TRIGGERED"

.. autoclass:: QueryVectorIndexNextPageRequest
   :members:
   :undoc-members:

.. autoclass:: QueryVectorIndexRequest
   :members:
   :undoc-members:

.. autoclass:: QueryVectorIndexResponse
   :members:
   :undoc-members:

.. autoclass:: ResultData
   :members:
   :undoc-members:

.. autoclass:: ResultManifest
   :members:
   :undoc-members:

.. autoclass:: ScanVectorIndexRequest
   :members:
   :undoc-members:

.. autoclass:: ScanVectorIndexResponse
   :members:
   :undoc-members:

.. autoclass:: Struct
   :members:
   :undoc-members:

.. autoclass:: SyncIndexResponse
   :members:
   :undoc-members:

.. autoclass:: UpsertDataResult
   :members:
   :undoc-members:

.. py:class:: UpsertDataStatus

   Status of the upsert operation.

   .. py:attribute:: FAILURE
      :value: "FAILURE"

   .. py:attribute:: PARTIAL_SUCCESS
      :value: "PARTIAL_SUCCESS"

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

.. autoclass:: UpsertDataVectorIndexRequest
   :members:
   :undoc-members:

.. autoclass:: UpsertDataVectorIndexResponse
   :members:
   :undoc-members:

.. autoclass:: Value
   :members:
   :undoc-members:

.. autoclass:: VectorIndex
   :members:
   :undoc-members:

.. autoclass:: VectorIndexStatus
   :members:
   :undoc-members:

.. py:class:: VectorIndexType

   There are 2 types of Vector Search indexes:
   - `DELTA_SYNC`: An index that automatically syncs with a source Delta Table, automatically and incrementally updating the index as the underlying data in the Delta Table changes. - `DIRECT_ACCESS`: An index that supports direct read and write of vectors and metadata through our REST and SDK APIs. With this model, the user manages index updates.

   .. py:attribute:: DELTA_SYNC
      :value: "DELTA_SYNC"

   .. py:attribute:: DIRECT_ACCESS
      :value: "DIRECT_ACCESS"

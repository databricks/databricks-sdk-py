AISearch
========

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.aisearch`` module.

.. py:currentmodule:: databricks.sdk.service.aisearch
.. autoclass:: ColumnInfo
   :members:
   :undoc-members:

.. autoclass:: CustomTag
   :members:
   :undoc-members:

.. autoclass:: DataModificationResult
   :members:
   :undoc-members:

.. py:class:: DataModificationStatus

   Overall outcome of a data-plane upsert or delete. Mirrors the legacy ``databricks.brickindexscheduler.UpsertDeleteDataStatus`` value-for-value.

   .. py:attribute:: FAILURE
      :value: "FAILURE"

   .. py:attribute:: PARTIAL_SUCCESS
      :value: "PARTIAL_SUCCESS"

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

.. autoclass:: DeltaSyncIndexSpec
   :members:
   :undoc-members:

.. autoclass:: DirectAccessIndexSpec
   :members:
   :undoc-members:

.. autoclass:: EmbeddingSourceColumn
   :members:
   :undoc-members:

.. autoclass:: EmbeddingVectorColumn
   :members:
   :undoc-members:

.. autoclass:: Endpoint
   :members:
   :undoc-members:

.. autoclass:: EndpointScalingInfo
   :members:
   :undoc-members:

.. autoclass:: EndpointStatus
   :members:
   :undoc-members:

.. py:class:: EndpointStatusState

   Lifecycle state of an AI Search endpoint, used by both Standard and Storage Optimized SKUs.

   .. py:attribute:: DELETED
      :value: "DELETED"

   .. py:attribute:: OFFLINE
      :value: "OFFLINE"

   .. py:attribute:: ONLINE
      :value: "ONLINE"

   .. py:attribute:: PROVISIONING
      :value: "PROVISIONING"

   .. py:attribute:: RED_STATE
      :value: "RED_STATE"

   .. py:attribute:: YELLOW_STATE
      :value: "YELLOW_STATE"

.. autoclass:: EndpointThroughputInfo
   :members:
   :undoc-members:

.. py:class:: EndpointType

   Type of endpoint.

   .. py:attribute:: STANDARD
      :value: "STANDARD"

   .. py:attribute:: STORAGE_OPTIMIZED
      :value: "STORAGE_OPTIMIZED"

.. autoclass:: FacetResultData
   :members:
   :undoc-members:

.. autoclass:: Index
   :members:
   :undoc-members:

.. autoclass:: IndexStatus
   :members:
   :undoc-members:

.. py:class:: IndexSubtype

   The subtype of the AI Search index, determining the indexing and retrieval strategy.
   - ``VECTOR``: Not a supported create value — do not select it. Use ``HYBRID`` (vector + hybrid search) or ``FULL_TEXT`` (full-text only). It is the proto2 default (``= 0``) solely to mirror the legacy ``index_v2.proto`` enum value-for-value; it is not an offered index subtype. - ``FULL_TEXT``: An index that uses full-text search without vector embeddings. - ``HYBRID``: An index that uses vector embeddings for similarity search and hybrid search.

   .. py:attribute:: FULL_TEXT
      :value: "FULL_TEXT"

   .. py:attribute:: HYBRID
      :value: "HYBRID"

   .. py:attribute:: VECTOR
      :value: "VECTOR"

.. py:class:: IndexType

   There are 2 types of AI Search indexes:
   - ``DELTA_SYNC``: An index that automatically syncs with a source Delta Table, automatically and incrementally updating the index as the underlying data in the Delta Table changes. - ``DIRECT_ACCESS``: An index that supports direct read and write of vectors and metadata through our REST and SDK APIs. With this model, the user manages index updates.

   .. py:attribute:: DELTA_SYNC
      :value: "DELTA_SYNC"

   .. py:attribute:: DIRECT_ACCESS
      :value: "DIRECT_ACCESS"

.. autoclass:: ListEndpointsResponse
   :members:
   :undoc-members:

.. autoclass:: ListIndexesResponse
   :members:
   :undoc-members:

.. py:class:: PipelineType

   Pipeline execution mode for a Delta Sync index. Required on create for Delta Sync indexes; the legacy backend rejects an unset value with INVALID_PARAMETER_VALUE.
   - ``TRIGGERED``: the pipeline stops after refreshing the source table once, using the data available when the update started. - ``CONTINUOUS``: the pipeline processes new data as it arrives in the source table to keep the index fresh.

   .. py:attribute:: CONTINUOUS
      :value: "CONTINUOUS"

   .. py:attribute:: TRIGGERED
      :value: "TRIGGERED"

.. autoclass:: QueryIndexResponse
   :members:
   :undoc-members:

.. autoclass:: RemoveDataResponse
   :members:
   :undoc-members:

.. autoclass:: RerankerConfig
   :members:
   :undoc-members:

.. py:class:: RerankerConfigModelType

   How the ``model`` field is interpreted.

   .. py:attribute:: MODEL_TYPE_BASE
      :value: "MODEL_TYPE_BASE"

   .. py:attribute:: MODEL_TYPE_FINETUNED
      :value: "MODEL_TYPE_FINETUNED"

.. autoclass:: RerankerConfigRerankerParameters
   :members:
   :undoc-members:

.. autoclass:: ResultData
   :members:
   :undoc-members:

.. autoclass:: ResultManifest
   :members:
   :undoc-members:

.. py:class:: ScalingChangeState

   State of the most recent scaling change request for a Storage Optimized endpoint.

   .. py:attribute:: SCALING_CHANGE_APPLIED
      :value: "SCALING_CHANGE_APPLIED"

   .. py:attribute:: SCALING_CHANGE_IN_PROGRESS
      :value: "SCALING_CHANGE_IN_PROGRESS"

   .. py:attribute:: SCALING_CHANGE_UNSPECIFIED
      :value: "SCALING_CHANGE_UNSPECIFIED"

.. autoclass:: ScanIndexResponse
   :members:
   :undoc-members:

.. autoclass:: SyncIndexResponse
   :members:
   :undoc-members:

.. py:class:: ThroughputChangeRequestState

   State of the most recent throughput change request issued against a Storage Optimized endpoint. Surfaced on ``EndpointThroughputInfo.change_request_state``.

   .. py:attribute:: CHANGE_ADJUSTED
      :value: "CHANGE_ADJUSTED"

   .. py:attribute:: CHANGE_FAILED
      :value: "CHANGE_FAILED"

   .. py:attribute:: CHANGE_IN_PROGRESS
      :value: "CHANGE_IN_PROGRESS"

   .. py:attribute:: CHANGE_REACHED_MAXIMUM
      :value: "CHANGE_REACHED_MAXIMUM"

   .. py:attribute:: CHANGE_REACHED_MINIMUM
      :value: "CHANGE_REACHED_MINIMUM"

   .. py:attribute:: CHANGE_SUCCESS
      :value: "CHANGE_SUCCESS"

.. autoclass:: UpsertDataResponse
   :members:
   :undoc-members:

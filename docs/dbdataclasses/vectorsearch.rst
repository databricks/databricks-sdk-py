Vector Search
=============

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.vectorsearch`` module.

.. py:currentmodule:: databricks.sdk.service.vectorsearch
.. autoclass:: AdjustedThroughputRequest
   :members:
   :undoc-members:

.. py:class:: AutoEvalDisplayStatus

   .. py:attribute:: AUTO_EVAL_DISPLAY_STATUS_FAILED
      :value: "AUTO_EVAL_DISPLAY_STATUS_FAILED"

   .. py:attribute:: AUTO_EVAL_DISPLAY_STATUS_PENDING
      :value: "AUTO_EVAL_DISPLAY_STATUS_PENDING"

   .. py:attribute:: AUTO_EVAL_DISPLAY_STATUS_RUNNING
      :value: "AUTO_EVAL_DISPLAY_STATUS_RUNNING"

   .. py:attribute:: AUTO_EVAL_DISPLAY_STATUS_SUCCEEDED
      :value: "AUTO_EVAL_DISPLAY_STATUS_SUCCEEDED"

.. autoclass:: AutoEvalJob
   :members:
   :undoc-members:

.. py:class:: AutoEvalStage

   Pipeline stages within a single autoeval run, in execution order. Used together with AutoEvalJob to drive a staged progress bar in the UI.

   .. py:attribute:: AUTO_EVAL_STAGE_FEW_SHOT_QUERIES
      :value: "AUTO_EVAL_STAGE_FEW_SHOT_QUERIES"

   .. py:attribute:: AUTO_EVAL_STAGE_GENERATE_QUERIES
      :value: "AUTO_EVAL_STAGE_GENERATE_QUERIES"

   .. py:attribute:: AUTO_EVAL_STAGE_GENERATE_RESULTS
      :value: "AUTO_EVAL_STAGE_GENERATE_RESULTS"

   .. py:attribute:: AUTO_EVAL_STAGE_METRICS_COMPUTATION
      :value: "AUTO_EVAL_STAGE_METRICS_COMPUTATION"

.. autoclass:: ColumnInfo
   :members:
   :undoc-members:

.. autoclass:: CustomTag
   :members:
   :undoc-members:

.. autoclass:: DeleteDataResult
   :members:
   :undoc-members:

.. py:class:: DeleteDataStatus

   .. py:attribute:: FAILURE
      :value: "FAILURE"

   .. py:attribute:: PARTIAL_SUCCESS
      :value: "PARTIAL_SUCCESS"

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

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

.. autoclass:: EndpointScalingInfo
   :members:
   :undoc-members:

.. autoclass:: EndpointStatus
   :members:
   :undoc-members:

.. py:class:: EndpointStatusState

   Current state of the endpoint

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

.. autoclass:: GetAutoEvalStatusResponse
   :members:
   :undoc-members:

.. autoclass:: GetVectorSearchEndpointPermissionLevelsResponse
   :members:
   :undoc-members:

.. py:class:: IndexSubtype

   The subtype of the AI Search index, determining the indexing and retrieval strategy.
   - ``VECTOR``: Not supported. Use ``HYBRID`` instead. - ``FULL_TEXT``: An index that uses full-text search without vector embeddings. - ``HYBRID``: An index that uses vector embeddings for similarity search and hybrid search.

   .. py:attribute:: FULL_TEXT
      :value: "FULL_TEXT"

   .. py:attribute:: HYBRID
      :value: "HYBRID"

   .. py:attribute:: VECTOR
      :value: "VECTOR"

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

.. autoclass:: Metric
   :members:
   :undoc-members:

.. autoclass:: MetricLabel
   :members:
   :undoc-members:

.. autoclass:: MetricValue
   :members:
   :undoc-members:

.. autoclass:: MetricValues
   :members:
   :undoc-members:

.. autoclass:: MiniVectorIndex
   :members:
   :undoc-members:

.. autoclass:: PatchEndpointBudgetPolicyResponse
   :members:
   :undoc-members:

.. autoclass:: PatchEndpointThroughputResponse
   :members:
   :undoc-members:

.. py:class:: PipelineType

   Pipeline execution mode.
   - ``TRIGGERED``: If the pipeline uses the triggered execution mode, the system stops processing after successfully refreshing the source table in the pipeline once, ensuring the table is updated based on the data available when the update started. - ``CONTINUOUS``: If the pipeline uses continuous execution, the pipeline processes new data as it arrives in the source table to keep vector index fresh.

   .. py:attribute:: CONTINUOUS
      :value: "CONTINUOUS"

   .. py:attribute:: TRIGGERED
      :value: "TRIGGERED"

.. autoclass:: QueryVectorIndexResponse
   :members:
   :undoc-members:

.. autoclass:: RerankerConfig
   :members:
   :undoc-members:

.. py:class:: RerankerConfigModelType

   EXPERIMENTAL. Selects how ``model`` is interpreted.

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

.. autoclass:: RetrieveUserVisibleMetricsResponse
   :members:
   :undoc-members:

.. autoclass:: RunAutoEvalResponse
   :members:
   :undoc-members:

.. autoclass:: RunRerankerFinetuningResponse
   :members:
   :undoc-members:

.. py:class:: ScalingChangeState

   .. py:attribute:: SCALING_CHANGE_APPLIED
      :value: "SCALING_CHANGE_APPLIED"

   .. py:attribute:: SCALING_CHANGE_IN_PROGRESS
      :value: "SCALING_CHANGE_IN_PROGRESS"

   .. py:attribute:: SCALING_CHANGE_UNSPECIFIED
      :value: "SCALING_CHANGE_UNSPECIFIED"

.. autoclass:: ScanVectorIndexResponse
   :members:
   :undoc-members:

.. autoclass:: Struct
   :members:
   :undoc-members:

.. autoclass:: SyncIndexResponse
   :members:
   :undoc-members:

.. py:class:: ThroughputChangeRequestState

   Throughput change request state

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

.. py:class:: ThroughputPatchStatus

   Response status for throughput change requests

   .. py:attribute:: PATCH_ACCEPTED
      :value: "PATCH_ACCEPTED"

   .. py:attribute:: PATCH_FAILED
      :value: "PATCH_FAILED"

   .. py:attribute:: PATCH_REJECTED
      :value: "PATCH_REJECTED"

.. autoclass:: UpdateEndpointCustomTagsResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateVectorIndexUsagePolicyResponse
   :members:
   :undoc-members:

.. autoclass:: UpsertDataResult
   :members:
   :undoc-members:

.. py:class:: UpsertDataStatus

   .. py:attribute:: FAILURE
      :value: "FAILURE"

   .. py:attribute:: PARTIAL_SUCCESS
      :value: "PARTIAL_SUCCESS"

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

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

   There are 2 types of AI Search indexes:
   - ``DELTA_SYNC``: An index that automatically syncs with a source Delta Table, automatically and incrementally updating the index as the underlying data in the Delta Table changes. - ``DIRECT_ACCESS``: An index that supports direct read and write of vectors and metadata through our REST and SDK APIs. With this model, the user manages index updates.

   .. py:attribute:: DELTA_SYNC
      :value: "DELTA_SYNC"

   .. py:attribute:: DIRECT_ACCESS
      :value: "DIRECT_ACCESS"

.. autoclass:: VectorSearchEndpointAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: VectorSearchEndpointAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: VectorSearchEndpointPermission
   :members:
   :undoc-members:

.. py:class:: VectorSearchEndpointPermissionLevel

   Permission level

   .. py:attribute:: CAN_CREATE
      :value: "CAN_CREATE"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_USE
      :value: "CAN_USE"

.. autoclass:: VectorSearchEndpointPermissions
   :members:
   :undoc-members:

.. autoclass:: VectorSearchEndpointPermissionsDescription
   :members:
   :undoc-members:

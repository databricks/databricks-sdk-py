Real-time Serving
=================

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.serving`` module.

.. py:currentmodule:: databricks.sdk.service.serving
.. autoclass:: Ai21LabsConfig
   :members:
   :undoc-members:

.. autoclass:: AiGatewayConfig
   :members:
   :undoc-members:

.. autoclass:: AiGatewayGuardrailParameters
   :members:
   :undoc-members:

.. autoclass:: AiGatewayGuardrailPiiBehavior
   :members:
   :undoc-members:

.. py:class:: AiGatewayGuardrailPiiBehaviorBehavior

   .. py:attribute:: BLOCK
      :value: "BLOCK"

   .. py:attribute:: NONE
      :value: "NONE"

.. autoclass:: AiGatewayGuardrails
   :members:
   :undoc-members:

.. autoclass:: AiGatewayInferenceTableConfig
   :members:
   :undoc-members:

.. autoclass:: AiGatewayRateLimit
   :members:
   :undoc-members:

.. py:class:: AiGatewayRateLimitKey

   .. py:attribute:: ENDPOINT
      :value: "ENDPOINT"

   .. py:attribute:: USER
      :value: "USER"

.. py:class:: AiGatewayRateLimitRenewalPeriod

   .. py:attribute:: MINUTE
      :value: "MINUTE"

.. autoclass:: AiGatewayUsageTrackingConfig
   :members:
   :undoc-members:

.. autoclass:: AmazonBedrockConfig
   :members:
   :undoc-members:

.. py:class:: AmazonBedrockConfigBedrockProvider

   .. py:attribute:: AI21LABS
      :value: "AI21LABS"

   .. py:attribute:: AMAZON
      :value: "AMAZON"

   .. py:attribute:: ANTHROPIC
      :value: "ANTHROPIC"

   .. py:attribute:: COHERE
      :value: "COHERE"

.. autoclass:: AnthropicConfig
   :members:
   :undoc-members:

.. autoclass:: ApiKeyAuth
   :members:
   :undoc-members:

.. autoclass:: AutoCaptureConfigInput
   :members:
   :undoc-members:

.. autoclass:: AutoCaptureConfigOutput
   :members:
   :undoc-members:

.. autoclass:: AutoCaptureState
   :members:
   :undoc-members:

.. autoclass:: BearerTokenAuth
   :members:
   :undoc-members:

.. autoclass:: BuildLogsResponse
   :members:
   :undoc-members:

.. autoclass:: ChatMessage
   :members:
   :undoc-members:

.. py:class:: ChatMessageRole

   The role of the message. One of [system, user, assistant].

   .. py:attribute:: ASSISTANT
      :value: "ASSISTANT"

   .. py:attribute:: SYSTEM
      :value: "SYSTEM"

   .. py:attribute:: USER
      :value: "USER"

.. autoclass:: CohereConfig
   :members:
   :undoc-members:

.. autoclass:: CustomProviderConfig
   :members:
   :undoc-members:

.. autoclass:: DataPlaneInfo
   :members:
   :undoc-members:

.. autoclass:: DatabricksModelServingConfig
   :members:
   :undoc-members:

.. autoclass:: DataframeSplitInput
   :members:
   :undoc-members:

.. autoclass:: DeleteResponse
   :members:
   :undoc-members:

.. autoclass:: EmbeddingsV1ResponseEmbeddingElement
   :members:
   :undoc-members:

.. py:class:: EmbeddingsV1ResponseEmbeddingElementObject

   This will always be 'embedding'.

   .. py:attribute:: EMBEDDING
      :value: "EMBEDDING"

.. autoclass:: EndpointCoreConfigInput
   :members:
   :undoc-members:

.. autoclass:: EndpointCoreConfigOutput
   :members:
   :undoc-members:

.. autoclass:: EndpointCoreConfigSummary
   :members:
   :undoc-members:

.. autoclass:: EndpointPendingConfig
   :members:
   :undoc-members:

.. autoclass:: EndpointState
   :members:
   :undoc-members:

.. py:class:: EndpointStateConfigUpdate

   .. py:attribute:: IN_PROGRESS
      :value: "IN_PROGRESS"

   .. py:attribute:: NOT_UPDATING
      :value: "NOT_UPDATING"

   .. py:attribute:: UPDATE_CANCELED
      :value: "UPDATE_CANCELED"

   .. py:attribute:: UPDATE_FAILED
      :value: "UPDATE_FAILED"

.. py:class:: EndpointStateReady

   .. py:attribute:: NOT_READY
      :value: "NOT_READY"

   .. py:attribute:: READY
      :value: "READY"

.. autoclass:: EndpointTag
   :members:
   :undoc-members:

.. autoclass:: EndpointTags
   :members:
   :undoc-members:

.. autoclass:: ExportMetricsResponse
   :members:
   :undoc-members:

.. py:class:: ExternalFunctionRequestHttpMethod

   .. py:attribute:: DELETE
      :value: "DELETE"

   .. py:attribute:: GET
      :value: "GET"

   .. py:attribute:: PATCH
      :value: "PATCH"

   .. py:attribute:: POST
      :value: "POST"

   .. py:attribute:: PUT
      :value: "PUT"

.. autoclass:: ExternalModel
   :members:
   :undoc-members:

.. py:class:: ExternalModelProvider

   .. py:attribute:: AI21LABS
      :value: "AI21LABS"

   .. py:attribute:: AMAZON_BEDROCK
      :value: "AMAZON_BEDROCK"

   .. py:attribute:: ANTHROPIC
      :value: "ANTHROPIC"

   .. py:attribute:: COHERE
      :value: "COHERE"

   .. py:attribute:: CUSTOM
      :value: "CUSTOM"

   .. py:attribute:: DATABRICKS_MODEL_SERVING
      :value: "DATABRICKS_MODEL_SERVING"

   .. py:attribute:: GOOGLE_CLOUD_VERTEX_AI
      :value: "GOOGLE_CLOUD_VERTEX_AI"

   .. py:attribute:: OPENAI
      :value: "OPENAI"

   .. py:attribute:: PALM
      :value: "PALM"

.. autoclass:: ExternalModelUsageElement
   :members:
   :undoc-members:

.. autoclass:: FallbackConfig
   :members:
   :undoc-members:

.. autoclass:: FoundationModel
   :members:
   :undoc-members:

.. autoclass:: GetOpenApiResponse
   :members:
   :undoc-members:

.. autoclass:: GetServingEndpointPermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GoogleCloudVertexAiConfig
   :members:
   :undoc-members:

.. autoclass:: HttpRequestResponse
   :members:
   :undoc-members:

.. autoclass:: ListEndpointsResponse
   :members:
   :undoc-members:

.. autoclass:: ModelDataPlaneInfo
   :members:
   :undoc-members:

.. autoclass:: OpenAiConfig
   :members:
   :undoc-members:

.. autoclass:: PaLmConfig
   :members:
   :undoc-members:

.. autoclass:: PayloadTable
   :members:
   :undoc-members:

.. autoclass:: PtEndpointCoreConfig
   :members:
   :undoc-members:

.. autoclass:: PtServedModel
   :members:
   :undoc-members:

.. autoclass:: PutAiGatewayResponse
   :members:
   :undoc-members:

.. autoclass:: PutResponse
   :members:
   :undoc-members:

.. autoclass:: QueryEndpointResponse
   :members:
   :undoc-members:

.. py:class:: QueryEndpointResponseObject

   The type of object returned by the __external/foundation model__ serving endpoint, one of [text_completion, chat.completion, list (of embeddings)].

   .. py:attribute:: CHAT_COMPLETION
      :value: "CHAT_COMPLETION"

   .. py:attribute:: LIST
      :value: "LIST"

   .. py:attribute:: TEXT_COMPLETION
      :value: "TEXT_COMPLETION"

.. autoclass:: RateLimit
   :members:
   :undoc-members:

.. py:class:: RateLimitKey

   .. py:attribute:: ENDPOINT
      :value: "ENDPOINT"

   .. py:attribute:: USER
      :value: "USER"

.. py:class:: RateLimitRenewalPeriod

   .. py:attribute:: MINUTE
      :value: "MINUTE"

.. autoclass:: Route
   :members:
   :undoc-members:

.. autoclass:: ServedEntityInput
   :members:
   :undoc-members:

.. autoclass:: ServedEntityOutput
   :members:
   :undoc-members:

.. autoclass:: ServedEntitySpec
   :members:
   :undoc-members:

.. autoclass:: ServedModelInput
   :members:
   :undoc-members:

.. py:class:: ServedModelInputWorkloadType

   Please keep this in sync with with workload types in InferenceEndpointEntities.scala

   .. py:attribute:: CPU
      :value: "CPU"

   .. py:attribute:: GPU_LARGE
      :value: "GPU_LARGE"

   .. py:attribute:: GPU_MEDIUM
      :value: "GPU_MEDIUM"

   .. py:attribute:: GPU_SMALL
      :value: "GPU_SMALL"

   .. py:attribute:: MULTIGPU_MEDIUM
      :value: "MULTIGPU_MEDIUM"

.. autoclass:: ServedModelOutput
   :members:
   :undoc-members:

.. autoclass:: ServedModelSpec
   :members:
   :undoc-members:

.. autoclass:: ServedModelState
   :members:
   :undoc-members:

.. py:class:: ServedModelStateDeployment

   .. py:attribute:: ABORTED
      :value: "ABORTED"

   .. py:attribute:: CREATING
      :value: "CREATING"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: READY
      :value: "READY"

   .. py:attribute:: RECOVERING
      :value: "RECOVERING"

.. autoclass:: ServerLogsResponse
   :members:
   :undoc-members:

.. autoclass:: ServingEndpoint
   :members:
   :undoc-members:

.. autoclass:: ServingEndpointAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: ServingEndpointAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: ServingEndpointDetailed
   :members:
   :undoc-members:

.. py:class:: ServingEndpointDetailedPermissionLevel

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_QUERY
      :value: "CAN_QUERY"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

.. autoclass:: ServingEndpointPermission
   :members:
   :undoc-members:

.. py:class:: ServingEndpointPermissionLevel

   Permission level

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_QUERY
      :value: "CAN_QUERY"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

.. autoclass:: ServingEndpointPermissions
   :members:
   :undoc-members:

.. autoclass:: ServingEndpointPermissionsDescription
   :members:
   :undoc-members:

.. py:class:: ServingModelWorkloadType

   Please keep this in sync with with workload types in InferenceEndpointEntities.scala

   .. py:attribute:: CPU
      :value: "CPU"

   .. py:attribute:: GPU_LARGE
      :value: "GPU_LARGE"

   .. py:attribute:: GPU_MEDIUM
      :value: "GPU_MEDIUM"

   .. py:attribute:: GPU_SMALL
      :value: "GPU_SMALL"

   .. py:attribute:: MULTIGPU_MEDIUM
      :value: "MULTIGPU_MEDIUM"

.. autoclass:: TrafficConfig
   :members:
   :undoc-members:

.. autoclass:: V1ResponseChoiceElement
   :members:
   :undoc-members:

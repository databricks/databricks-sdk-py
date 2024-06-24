Real-time Serving
=================

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.serving`` module.

.. py:currentmodule:: databricks.sdk.service.serving
.. autoclass:: Ai21LabsConfig
   :members:
   :undoc-members:

.. autoclass:: AmazonBedrockConfig
   :members:
   :undoc-members:

.. py:class:: AmazonBedrockConfigBedrockProvider

   The underlying provider in Amazon Bedrock. Supported values (case insensitive) include: Anthropic, Cohere, AI21Labs, Amazon.

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

.. autoclass:: App
   :members:
   :undoc-members:

.. autoclass:: AppDeployment
   :members:
   :undoc-members:

.. autoclass:: AppDeploymentArtifacts
   :members:
   :undoc-members:

.. py:class:: AppDeploymentMode

   .. py:attribute:: AUTO_SYNC
      :value: "AUTO_SYNC"

   .. py:attribute:: MODE_UNSPECIFIED
      :value: "MODE_UNSPECIFIED"

   .. py:attribute:: SNAPSHOT
      :value: "SNAPSHOT"

.. py:class:: AppDeploymentState

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: IN_PROGRESS
      :value: "IN_PROGRESS"

   .. py:attribute:: STATE_UNSPECIFIED
      :value: "STATE_UNSPECIFIED"

   .. py:attribute:: STOPPED
      :value: "STOPPED"

   .. py:attribute:: SUCCEEDED
      :value: "SUCCEEDED"

.. autoclass:: AppDeploymentStatus
   :members:
   :undoc-members:

.. autoclass:: AppEnvironment
   :members:
   :undoc-members:

.. py:class:: AppState

   .. py:attribute:: CREATING
      :value: "CREATING"

   .. py:attribute:: DELETED
      :value: "DELETED"

   .. py:attribute:: DELETING
      :value: "DELETING"

   .. py:attribute:: ERROR
      :value: "ERROR"

   .. py:attribute:: IDLE
      :value: "IDLE"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: STARTING
      :value: "STARTING"

   .. py:attribute:: STATE_UNSPECIFIED
      :value: "STATE_UNSPECIFIED"

.. autoclass:: AppStatus
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

.. autoclass:: CreateAppDeploymentRequest
   :members:
   :undoc-members:

.. autoclass:: CreateAppRequest
   :members:
   :undoc-members:

.. autoclass:: CreateServingEndpoint
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

   The state of an endpoint's config update. This informs the user if the pending_config is in progress, if the update failed, or if there is no update in progress. Note that if the endpoint's config_update state value is IN_PROGRESS, another update can not be made until the update completes or fails.

   .. py:attribute:: IN_PROGRESS
      :value: "IN_PROGRESS"

   .. py:attribute:: NOT_UPDATING
      :value: "NOT_UPDATING"

   .. py:attribute:: UPDATE_FAILED
      :value: "UPDATE_FAILED"

.. py:class:: EndpointStateReady

   The state of an endpoint, indicating whether or not the endpoint is queryable. An endpoint is READY if all of the served entities in its active configuration are ready. If any of the actively served entities are in a non-ready state, the endpoint state will be NOT_READY.

   .. py:attribute:: NOT_READY
      :value: "NOT_READY"

   .. py:attribute:: READY
      :value: "READY"

.. autoclass:: EndpointTag
   :members:
   :undoc-members:

.. autoclass:: EnvVariable
   :members:
   :undoc-members:

.. autoclass:: ExportMetricsResponse
   :members:
   :undoc-members:

.. autoclass:: ExternalModel
   :members:
   :undoc-members:

.. py:class:: ExternalModelProvider

   The name of the provider for the external model. Currently, the supported providers are 'ai21labs', 'anthropic', 'amazon-bedrock', 'cohere', 'databricks-model-serving', 'openai', and 'palm'.",

   .. py:attribute:: AI21LABS
      :value: "AI21LABS"

   .. py:attribute:: AMAZON_BEDROCK
      :value: "AMAZON_BEDROCK"

   .. py:attribute:: ANTHROPIC
      :value: "ANTHROPIC"

   .. py:attribute:: COHERE
      :value: "COHERE"

   .. py:attribute:: DATABRICKS_MODEL_SERVING
      :value: "DATABRICKS_MODEL_SERVING"

   .. py:attribute:: OPENAI
      :value: "OPENAI"

   .. py:attribute:: PALM
      :value: "PALM"

.. autoclass:: ExternalModelUsageElement
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

.. autoclass:: ListAppDeploymentsResponse
   :members:
   :undoc-members:

.. autoclass:: ListAppsResponse
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

.. autoclass:: PatchServingEndpointTags
   :members:
   :undoc-members:

.. autoclass:: PayloadTable
   :members:
   :undoc-members:

.. autoclass:: PutResponse
   :members:
   :undoc-members:

.. autoclass:: QueryEndpointInput
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

   Key field for a serving endpoint rate limit. Currently, only 'user' and 'endpoint' are supported, with 'endpoint' being the default if not specified.

   .. py:attribute:: ENDPOINT
      :value: "ENDPOINT"

   .. py:attribute:: USER
      :value: "USER"

.. py:class:: RateLimitRenewalPeriod

   Renewal period field for a serving endpoint rate limit. Currently, only 'minute' is supported.

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

.. py:class:: ServedModelInputWorkloadSize

   The workload size of the served model. The workload size corresponds to a range of provisioned concurrency that the compute will autoscale between. A single unit of provisioned concurrency can process one request at a time. Valid workload sizes are "Small" (4 - 4 provisioned concurrency), "Medium" (8 - 16 provisioned concurrency), and "Large" (16 - 64 provisioned concurrency). If scale-to-zero is enabled, the lower bound of the provisioned concurrency for each workload size will be 0.

   .. py:attribute:: LARGE
      :value: "LARGE"

   .. py:attribute:: MEDIUM
      :value: "MEDIUM"

   .. py:attribute:: SMALL
      :value: "SMALL"

.. py:class:: ServedModelInputWorkloadType

   The workload type of the served model. The workload type selects which type of compute to use in the endpoint. The default value for this parameter is "CPU". For deep learning workloads, GPU acceleration is available by selecting workload types like GPU_SMALL and others. See the available [GPU types].
   [GPU types]: https://docs.databricks.com/machine-learning/model-serving/create-manage-serving-endpoints.html#gpu-workload-types

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

   The state of the served entity deployment. DEPLOYMENT_CREATING indicates that the served entity is not ready yet because the deployment is still being created (i.e container image is building, model server is deploying for the first time, etc.). DEPLOYMENT_RECOVERING indicates that the served entity was previously in a ready state but no longer is and is attempting to recover. DEPLOYMENT_READY indicates that the served entity is ready to receive traffic. DEPLOYMENT_FAILED indicates that there was an error trying to bring up the served entity (e.g container image build failed, the model server failed to start due to a model loading error, etc.) DEPLOYMENT_ABORTED indicates that the deployment was terminated likely due to a failure in bringing up another served entity under the same endpoint and config version.

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

   The permission level of the principal making the request.

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

.. autoclass:: ServingEndpointPermissionsRequest
   :members:
   :undoc-members:

.. autoclass:: StartAppRequest
   :members:
   :undoc-members:

.. autoclass:: StopAppRequest
   :members:
   :undoc-members:

.. autoclass:: StopAppResponse
   :members:
   :undoc-members:

.. autoclass:: TrafficConfig
   :members:
   :undoc-members:

.. autoclass:: UpdateAppRequest
   :members:
   :undoc-members:

.. autoclass:: V1ResponseChoiceElement
   :members:
   :undoc-members:

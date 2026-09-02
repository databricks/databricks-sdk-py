Machine Learning
================

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.ml`` module.

.. py:currentmodule:: databricks.sdk.service.ml
.. autoclass:: Activity
   :members:
   :undoc-members:

.. py:class:: ActivityAction

   An action that a user (with sufficient permissions) could take on an activity or comment.
   For activities, valid values are:
   - ``APPROVE_TRANSITION_REQUEST``: Approve a transition request - ``REJECT_TRANSITION_REQUEST``: Reject a transition request - ``CANCEL_TRANSITION_REQUEST``: Cancel (delete) a transition request
   For comments, valid values are:
   - ``EDIT_COMMENT``: Edit the comment - ``DELETE_COMMENT``: Delete the comment

   .. py:attribute:: APPROVE_TRANSITION_REQUEST
      :value: "APPROVE_TRANSITION_REQUEST"

   .. py:attribute:: CANCEL_TRANSITION_REQUEST
      :value: "CANCEL_TRANSITION_REQUEST"

   .. py:attribute:: DELETE_COMMENT
      :value: "DELETE_COMMENT"

   .. py:attribute:: EDIT_COMMENT
      :value: "EDIT_COMMENT"

   .. py:attribute:: REJECT_TRANSITION_REQUEST
      :value: "REJECT_TRANSITION_REQUEST"

.. py:class:: ActivityType

   Type of activity. Valid values are:
   - ``APPLIED_TRANSITION``: User applied the corresponding stage transition. - ``REQUESTED_TRANSITION``: User requested the corresponding stage transition. - ``CANCELLED_REQUEST``: User cancelled an existing transition request. - ``APPROVED_REQUEST``: User approved the corresponding stage transition. - ``REJECTED_REQUEST``: User rejected the coressponding stage transition. - ``SYSTEM_TRANSITION``: For events performed as a side effect, such as archiving existing model versions in a stage.

   .. py:attribute:: APPLIED_TRANSITION
      :value: "APPLIED_TRANSITION"

   .. py:attribute:: APPROVED_REQUEST
      :value: "APPROVED_REQUEST"

   .. py:attribute:: CANCELLED_REQUEST
      :value: "CANCELLED_REQUEST"

   .. py:attribute:: NEW_COMMENT
      :value: "NEW_COMMENT"

   .. py:attribute:: REJECTED_REQUEST
      :value: "REJECTED_REQUEST"

   .. py:attribute:: REQUESTED_TRANSITION
      :value: "REQUESTED_TRANSITION"

   .. py:attribute:: SYSTEM_TRANSITION
      :value: "SYSTEM_TRANSITION"

.. autoclass:: AggregationFunction
   :members:
   :undoc-members:

.. autoclass:: ApproveTransitionRequestResponse
   :members:
   :undoc-members:

.. autoclass:: ApproxCountDistinctFunction
   :members:
   :undoc-members:

.. autoclass:: ApproxPercentileFunction
   :members:
   :undoc-members:

.. autoclass:: AuthConfig
   :members:
   :undoc-members:

.. autoclass:: AvgFunction
   :members:
   :undoc-members:

.. autoclass:: BackfillFeaturesResponse
   :members:
   :undoc-members:

.. autoclass:: BackfillOperationMetadata
   :members:
   :undoc-members:

.. py:class:: BackfillOperationMetadataState

   Lifecycle state of a backfill.

   .. py:attribute:: CANCELLED
      :value: "CANCELLED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SUCCEEDED
      :value: "SUCCEEDED"

.. autoclass:: BackfillRange
   :members:
   :undoc-members:

.. autoclass:: BackfillSource
   :members:
   :undoc-members:

.. autoclass:: BatchCreateMaterializedFeaturesResponse
   :members:
   :undoc-members:

.. autoclass:: ColumnSelection
   :members:
   :undoc-members:

.. py:class:: CommentActivityAction

   An action that a user (with sufficient permissions) could take on an activity or comment.
   For activities, valid values are:
   - ``APPROVE_TRANSITION_REQUEST``: Approve a transition request - ``REJECT_TRANSITION_REQUEST``: Reject a transition request - ``CANCEL_TRANSITION_REQUEST``: Cancel (delete) a transition request
   For comments, valid values are:
   - ``EDIT_COMMENT``: Edit the comment - ``DELETE_COMMENT``: Delete the comment

   .. py:attribute:: APPROVE_TRANSITION_REQUEST
      :value: "APPROVE_TRANSITION_REQUEST"

   .. py:attribute:: CANCEL_TRANSITION_REQUEST
      :value: "CANCEL_TRANSITION_REQUEST"

   .. py:attribute:: DELETE_COMMENT
      :value: "DELETE_COMMENT"

   .. py:attribute:: EDIT_COMMENT
      :value: "EDIT_COMMENT"

   .. py:attribute:: REJECT_TRANSITION_REQUEST
      :value: "REJECT_TRANSITION_REQUEST"

.. autoclass:: CommentObject
   :members:
   :undoc-members:

.. autoclass:: CountFunction
   :members:
   :undoc-members:

.. autoclass:: CreateCommentResponse
   :members:
   :undoc-members:

.. autoclass:: CreateExperimentResponse
   :members:
   :undoc-members:

.. autoclass:: CreateForecastingExperimentResponse
   :members:
   :undoc-members:

.. autoclass:: CreateLoggedModelResponse
   :members:
   :undoc-members:

.. autoclass:: CreateMaterializedFeatureRequest
   :members:
   :undoc-members:

.. autoclass:: CreateModelResponse
   :members:
   :undoc-members:

.. autoclass:: CreateModelVersionResponse
   :members:
   :undoc-members:

.. autoclass:: CreateRunResponse
   :members:
   :undoc-members:

.. autoclass:: CreateTransitionRequestResponse
   :members:
   :undoc-members:

.. autoclass:: CreateWebhookResponse
   :members:
   :undoc-members:

.. autoclass:: CronSchedule
   :members:
   :undoc-members:

.. autoclass:: CustomUdf
   :members:
   :undoc-members:

.. autoclass:: DataSource
   :members:
   :undoc-members:

.. autoclass:: DatabricksServiceExceptionWithDetailsProto
   :members:
   :undoc-members:

.. autoclass:: Dataset
   :members:
   :undoc-members:

.. autoclass:: DatasetInput
   :members:
   :undoc-members:

.. autoclass:: DeleteCommentResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteExperimentResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteLoggedModelResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteLoggedModelTagResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteModelResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteModelTagResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteModelVersionResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteModelVersionTagResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteRunResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteRunsResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteTagResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteTransitionRequestResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteWebhookResponse
   :members:
   :undoc-members:

.. autoclass:: DeltaTableSource
   :members:
   :undoc-members:

.. autoclass:: DirectMtlsConfig
   :members:
   :undoc-members:

.. autoclass:: DirectSchemas
   :members:
   :undoc-members:

.. autoclass:: EntityColumn
   :members:
   :undoc-members:

.. py:class:: ErrorCode

   Error codes returned by Databricks APIs to indicate specific failure conditions.

   .. py:attribute:: ABORTED
      :value: "ABORTED"

   .. py:attribute:: ALREADY_EXISTS
      :value: "ALREADY_EXISTS"

   .. py:attribute:: BAD_REQUEST
      :value: "BAD_REQUEST"

   .. py:attribute:: CANCELLED
      :value: "CANCELLED"

   .. py:attribute:: CATALOG_ALREADY_EXISTS
      :value: "CATALOG_ALREADY_EXISTS"

   .. py:attribute:: CATALOG_DOES_NOT_EXIST
      :value: "CATALOG_DOES_NOT_EXIST"

   .. py:attribute:: CATALOG_NOT_EMPTY
      :value: "CATALOG_NOT_EMPTY"

   .. py:attribute:: COULD_NOT_ACQUIRE_LOCK
      :value: "COULD_NOT_ACQUIRE_LOCK"

   .. py:attribute:: CUSTOMER_UNAUTHORIZED
      :value: "CUSTOMER_UNAUTHORIZED"

   .. py:attribute:: DAC_ALREADY_EXISTS
      :value: "DAC_ALREADY_EXISTS"

   .. py:attribute:: DAC_DOES_NOT_EXIST
      :value: "DAC_DOES_NOT_EXIST"

   .. py:attribute:: DATA_LOSS
      :value: "DATA_LOSS"

   .. py:attribute:: DEADLINE_EXCEEDED
      :value: "DEADLINE_EXCEEDED"

   .. py:attribute:: DEPLOYMENT_TIMEOUT
      :value: "DEPLOYMENT_TIMEOUT"

   .. py:attribute:: DIRECTORY_NOT_EMPTY
      :value: "DIRECTORY_NOT_EMPTY"

   .. py:attribute:: DIRECTORY_PROTECTED
      :value: "DIRECTORY_PROTECTED"

   .. py:attribute:: DRY_RUN_FAILED
      :value: "DRY_RUN_FAILED"

   .. py:attribute:: ENDPOINT_NOT_FOUND
      :value: "ENDPOINT_NOT_FOUND"

   .. py:attribute:: EXTERNAL_LOCATION_ALREADY_EXISTS
      :value: "EXTERNAL_LOCATION_ALREADY_EXISTS"

   .. py:attribute:: EXTERNAL_LOCATION_DOES_NOT_EXIST
      :value: "EXTERNAL_LOCATION_DOES_NOT_EXIST"

   .. py:attribute:: FEATURE_DISABLED
      :value: "FEATURE_DISABLED"

   .. py:attribute:: GIT_CONFLICT
      :value: "GIT_CONFLICT"

   .. py:attribute:: GIT_REMOTE_ERROR
      :value: "GIT_REMOTE_ERROR"

   .. py:attribute:: GIT_SENSITIVE_TOKEN_DETECTED
      :value: "GIT_SENSITIVE_TOKEN_DETECTED"

   .. py:attribute:: GIT_UNKNOWN_REF
      :value: "GIT_UNKNOWN_REF"

   .. py:attribute:: GIT_URL_NOT_ON_ALLOW_LIST
      :value: "GIT_URL_NOT_ON_ALLOW_LIST"

   .. py:attribute:: INSECURE_PARTNER_RESPONSE
      :value: "INSECURE_PARTNER_RESPONSE"

   .. py:attribute:: INTERNAL_ERROR
      :value: "INTERNAL_ERROR"

   .. py:attribute:: INVALID_PARAMETER_VALUE
      :value: "INVALID_PARAMETER_VALUE"

   .. py:attribute:: INVALID_STATE
      :value: "INVALID_STATE"

   .. py:attribute:: INVALID_STATE_TRANSITION
      :value: "INVALID_STATE_TRANSITION"

   .. py:attribute:: IO_ERROR
      :value: "IO_ERROR"

   .. py:attribute:: IPYNB_FILE_IN_REPO
      :value: "IPYNB_FILE_IN_REPO"

   .. py:attribute:: MALFORMED_PARTNER_RESPONSE
      :value: "MALFORMED_PARTNER_RESPONSE"

   .. py:attribute:: MALFORMED_REQUEST
      :value: "MALFORMED_REQUEST"

   .. py:attribute:: MANAGED_RESOURCE_GROUP_DOES_NOT_EXIST
      :value: "MANAGED_RESOURCE_GROUP_DOES_NOT_EXIST"

   .. py:attribute:: MAX_BLOCK_SIZE_EXCEEDED
      :value: "MAX_BLOCK_SIZE_EXCEEDED"

   .. py:attribute:: MAX_CHILD_NODE_SIZE_EXCEEDED
      :value: "MAX_CHILD_NODE_SIZE_EXCEEDED"

   .. py:attribute:: MAX_LIST_SIZE_EXCEEDED
      :value: "MAX_LIST_SIZE_EXCEEDED"

   .. py:attribute:: MAX_NOTEBOOK_SIZE_EXCEEDED
      :value: "MAX_NOTEBOOK_SIZE_EXCEEDED"

   .. py:attribute:: MAX_READ_SIZE_EXCEEDED
      :value: "MAX_READ_SIZE_EXCEEDED"

   .. py:attribute:: METASTORE_ALREADY_EXISTS
      :value: "METASTORE_ALREADY_EXISTS"

   .. py:attribute:: METASTORE_DOES_NOT_EXIST
      :value: "METASTORE_DOES_NOT_EXIST"

   .. py:attribute:: METASTORE_NOT_EMPTY
      :value: "METASTORE_NOT_EMPTY"

   .. py:attribute:: NOT_FOUND
      :value: "NOT_FOUND"

   .. py:attribute:: NOT_IMPLEMENTED
      :value: "NOT_IMPLEMENTED"

   .. py:attribute:: PARTIAL_DELETE
      :value: "PARTIAL_DELETE"

   .. py:attribute:: PERMISSION_DENIED
      :value: "PERMISSION_DENIED"

   .. py:attribute:: PERMISSION_NOT_PROPAGATED
      :value: "PERMISSION_NOT_PROPAGATED"

   .. py:attribute:: PRINCIPAL_DOES_NOT_EXIST
      :value: "PRINCIPAL_DOES_NOT_EXIST"

   .. py:attribute:: PROJECTS_OPERATION_TIMEOUT
      :value: "PROJECTS_OPERATION_TIMEOUT"

   .. py:attribute:: PROVIDER_ALREADY_EXISTS
      :value: "PROVIDER_ALREADY_EXISTS"

   .. py:attribute:: PROVIDER_DOES_NOT_EXIST
      :value: "PROVIDER_DOES_NOT_EXIST"

   .. py:attribute:: PROVIDER_SHARE_NOT_ACCESSIBLE
      :value: "PROVIDER_SHARE_NOT_ACCESSIBLE"

   .. py:attribute:: QUOTA_EXCEEDED
      :value: "QUOTA_EXCEEDED"

   .. py:attribute:: RECIPIENT_ALREADY_EXISTS
      :value: "RECIPIENT_ALREADY_EXISTS"

   .. py:attribute:: RECIPIENT_DOES_NOT_EXIST
      :value: "RECIPIENT_DOES_NOT_EXIST"

   .. py:attribute:: REQUEST_LIMIT_EXCEEDED
      :value: "REQUEST_LIMIT_EXCEEDED"

   .. py:attribute:: RESOURCE_ALREADY_EXISTS
      :value: "RESOURCE_ALREADY_EXISTS"

   .. py:attribute:: RESOURCE_CONFLICT
      :value: "RESOURCE_CONFLICT"

   .. py:attribute:: RESOURCE_DOES_NOT_EXIST
      :value: "RESOURCE_DOES_NOT_EXIST"

   .. py:attribute:: RESOURCE_EXHAUSTED
      :value: "RESOURCE_EXHAUSTED"

   .. py:attribute:: RESOURCE_LIMIT_EXCEEDED
      :value: "RESOURCE_LIMIT_EXCEEDED"

   .. py:attribute:: SCHEMA_ALREADY_EXISTS
      :value: "SCHEMA_ALREADY_EXISTS"

   .. py:attribute:: SCHEMA_DOES_NOT_EXIST
      :value: "SCHEMA_DOES_NOT_EXIST"

   .. py:attribute:: SCHEMA_NOT_EMPTY
      :value: "SCHEMA_NOT_EMPTY"

   .. py:attribute:: SEARCH_QUERY_TOO_LONG
      :value: "SEARCH_QUERY_TOO_LONG"

   .. py:attribute:: SEARCH_QUERY_TOO_SHORT
      :value: "SEARCH_QUERY_TOO_SHORT"

   .. py:attribute:: SERVICE_UNDER_MAINTENANCE
      :value: "SERVICE_UNDER_MAINTENANCE"

   .. py:attribute:: SHARE_ALREADY_EXISTS
      :value: "SHARE_ALREADY_EXISTS"

   .. py:attribute:: SHARE_DOES_NOT_EXIST
      :value: "SHARE_DOES_NOT_EXIST"

   .. py:attribute:: STORAGE_CREDENTIAL_ALREADY_EXISTS
      :value: "STORAGE_CREDENTIAL_ALREADY_EXISTS"

   .. py:attribute:: STORAGE_CREDENTIAL_DOES_NOT_EXIST
      :value: "STORAGE_CREDENTIAL_DOES_NOT_EXIST"

   .. py:attribute:: TABLE_ALREADY_EXISTS
      :value: "TABLE_ALREADY_EXISTS"

   .. py:attribute:: TABLE_DOES_NOT_EXIST
      :value: "TABLE_DOES_NOT_EXIST"

   .. py:attribute:: TEMPORARILY_UNAVAILABLE
      :value: "TEMPORARILY_UNAVAILABLE"

   .. py:attribute:: UNAUTHENTICATED
      :value: "UNAUTHENTICATED"

   .. py:attribute:: UNAVAILABLE
      :value: "UNAVAILABLE"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

   .. py:attribute:: UNPARSEABLE_HTTP_ERROR
      :value: "UNPARSEABLE_HTTP_ERROR"

   .. py:attribute:: WORKSPACE_TEMPORARILY_UNAVAILABLE
      :value: "WORKSPACE_TEMPORARILY_UNAVAILABLE"

.. autoclass:: Experiment
   :members:
   :undoc-members:

.. autoclass:: ExperimentAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: ExperimentAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: ExperimentPermission
   :members:
   :undoc-members:

.. py:class:: ExperimentPermissionLevel

   Permission level

   .. py:attribute:: CAN_EDIT
      :value: "CAN_EDIT"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_READ
      :value: "CAN_READ"

.. autoclass:: ExperimentPermissions
   :members:
   :undoc-members:

.. autoclass:: ExperimentPermissionsDescription
   :members:
   :undoc-members:

.. autoclass:: ExperimentTag
   :members:
   :undoc-members:

.. autoclass:: ExperimentTraceLocation
   :members:
   :undoc-members:

.. autoclass:: Feature
   :members:
   :undoc-members:

.. autoclass:: FeatureLineage
   :members:
   :undoc-members:

.. autoclass:: FeatureLineageFeatureSpec
   :members:
   :undoc-members:

.. autoclass:: FeatureLineageModel
   :members:
   :undoc-members:

.. autoclass:: FeatureLineageOnlineFeature
   :members:
   :undoc-members:

.. autoclass:: FeatureList
   :members:
   :undoc-members:

.. autoclass:: FeatureTag
   :members:
   :undoc-members:

.. autoclass:: FieldDefinition
   :members:
   :undoc-members:

.. autoclass:: FileInfo
   :members:
   :undoc-members:

.. autoclass:: FinalizeLoggedModelResponse
   :members:
   :undoc-members:

.. autoclass:: FirstDistinctFunction
   :members:
   :undoc-members:

.. autoclass:: FirstFunction
   :members:
   :undoc-members:

.. autoclass:: FirstNFunction
   :members:
   :undoc-members:

.. autoclass:: FlatSchema
   :members:
   :undoc-members:

.. autoclass:: ForecastingExperiment
   :members:
   :undoc-members:

.. py:class:: ForecastingExperimentState

   .. py:attribute:: CANCELLED
      :value: "CANCELLED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SUCCEEDED
      :value: "SUCCEEDED"

.. autoclass:: Function
   :members:
   :undoc-members:

.. autoclass:: GetExperimentByNameResponse
   :members:
   :undoc-members:

.. autoclass:: GetExperimentPermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GetExperimentResponse
   :members:
   :undoc-members:

.. autoclass:: GetLatestVersionsResponse
   :members:
   :undoc-members:

.. autoclass:: GetLoggedModelResponse
   :members:
   :undoc-members:

.. autoclass:: GetMetricHistoryResponse
   :members:
   :undoc-members:

.. autoclass:: GetModelResponse
   :members:
   :undoc-members:

.. autoclass:: GetModelVersionDownloadUriResponse
   :members:
   :undoc-members:

.. autoclass:: GetModelVersionResponse
   :members:
   :undoc-members:

.. autoclass:: GetRegisteredModelPermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GetRunResponse
   :members:
   :undoc-members:

.. autoclass:: HttpUrlSpec
   :members:
   :undoc-members:

.. autoclass:: HttpUrlSpecWithoutSecret
   :members:
   :undoc-members:

.. autoclass:: IngestionConfig
   :members:
   :undoc-members:

.. autoclass:: IngestionDestination
   :members:
   :undoc-members:

.. autoclass:: InputBinding
   :members:
   :undoc-members:

.. autoclass:: InputTag
   :members:
   :undoc-members:

.. autoclass:: JobContext
   :members:
   :undoc-members:

.. autoclass:: JobSpec
   :members:
   :undoc-members:

.. autoclass:: JobSpecWithoutSecret
   :members:
   :undoc-members:

.. autoclass:: KafkaConfig
   :members:
   :undoc-members:

.. autoclass:: KafkaSource
   :members:
   :undoc-members:

.. autoclass:: KafkaStreamConfig
   :members:
   :undoc-members:

.. autoclass:: KafkaSubscriptionMode
   :members:
   :undoc-members:

.. autoclass:: KinesisStreamConfig
   :members:
   :undoc-members:

.. autoclass:: LastDistinctFunction
   :members:
   :undoc-members:

.. autoclass:: LastFunction
   :members:
   :undoc-members:

.. autoclass:: LastNFunction
   :members:
   :undoc-members:

.. autoclass:: LineageContext
   :members:
   :undoc-members:

.. autoclass:: LinkedFeature
   :members:
   :undoc-members:

.. autoclass:: ListArtifactsResponse
   :members:
   :undoc-members:

.. autoclass:: ListExperimentsResponse
   :members:
   :undoc-members:

.. autoclass:: ListFeatureTagsResponse
   :members:
   :undoc-members:

.. autoclass:: ListFeaturesResponse
   :members:
   :undoc-members:

.. autoclass:: ListKafkaConfigsResponse
   :members:
   :undoc-members:

.. autoclass:: ListMaterializedFeaturesResponse
   :members:
   :undoc-members:

.. autoclass:: ListModelsResponse
   :members:
   :undoc-members:

.. autoclass:: ListOnlineStoresResponse
   :members:
   :undoc-members:

.. autoclass:: ListRegistryWebhooks
   :members:
   :undoc-members:

.. autoclass:: ListStreamsResponse
   :members:
   :undoc-members:

.. autoclass:: ListTransitionRequestsResponse
   :members:
   :undoc-members:

.. autoclass:: LogBatchResponse
   :members:
   :undoc-members:

.. autoclass:: LogInputsResponse
   :members:
   :undoc-members:

.. autoclass:: LogLoggedModelParamsRequestResponse
   :members:
   :undoc-members:

.. autoclass:: LogMetricResponse
   :members:
   :undoc-members:

.. autoclass:: LogModelResponse
   :members:
   :undoc-members:

.. autoclass:: LogOutputsResponse
   :members:
   :undoc-members:

.. autoclass:: LogParamResponse
   :members:
   :undoc-members:

.. autoclass:: LoggedModel
   :members:
   :undoc-members:

.. autoclass:: LoggedModelData
   :members:
   :undoc-members:

.. autoclass:: LoggedModelInfo
   :members:
   :undoc-members:

.. autoclass:: LoggedModelParameter
   :members:
   :undoc-members:

.. py:class:: LoggedModelStatus

   A LoggedModelStatus enum value represents the status of a logged model.

   .. py:attribute:: LOGGED_MODEL_PENDING
      :value: "LOGGED_MODEL_PENDING"

   .. py:attribute:: LOGGED_MODEL_READY
      :value: "LOGGED_MODEL_READY"

   .. py:attribute:: LOGGED_MODEL_UPLOAD_FAILED
      :value: "LOGGED_MODEL_UPLOAD_FAILED"

.. autoclass:: LoggedModelTag
   :members:
   :undoc-members:

.. autoclass:: MaterializedFeature
   :members:
   :undoc-members:

.. py:class:: MaterializedFeaturePipelineScheduleState

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: PAUSED
      :value: "PAUSED"

   .. py:attribute:: SNAPSHOT
      :value: "SNAPSHOT"

.. autoclass:: MaxFunction
   :members:
   :undoc-members:

.. autoclass:: Metric
   :members:
   :undoc-members:

.. autoclass:: MinFunction
   :members:
   :undoc-members:

.. autoclass:: Model
   :members:
   :undoc-members:

.. autoclass:: ModelDatabricks
   :members:
   :undoc-members:

.. autoclass:: ModelInput
   :members:
   :undoc-members:

.. autoclass:: ModelOutput
   :members:
   :undoc-members:

.. autoclass:: ModelTag
   :members:
   :undoc-members:

.. autoclass:: ModelVersion
   :members:
   :undoc-members:

.. autoclass:: ModelVersionDatabricks
   :members:
   :undoc-members:

.. py:class:: ModelVersionStatus

   The status of the model version. Valid values are:
   - ``PENDING_REGISTRATION``: Request to register a new model version is pending as server performs background tasks. - ``FAILED_REGISTRATION``: Request to register a new model version has failed. - ``READY``: Model version is ready for use.

   .. py:attribute:: FAILED_REGISTRATION
      :value: "FAILED_REGISTRATION"

   .. py:attribute:: PENDING_REGISTRATION
      :value: "PENDING_REGISTRATION"

   .. py:attribute:: READY
      :value: "READY"

.. autoclass:: ModelVersionTag
   :members:
   :undoc-members:

.. autoclass:: MtlsConfig
   :members:
   :undoc-members:

.. autoclass:: OfflineStoreConfig
   :members:
   :undoc-members:

.. autoclass:: OnlineStore
   :members:
   :undoc-members:

.. autoclass:: OnlineStoreConfig
   :members:
   :undoc-members:

.. py:class:: OnlineStoreState

   .. py:attribute:: AVAILABLE
      :value: "AVAILABLE"

   .. py:attribute:: DELETING
      :value: "DELETING"

   .. py:attribute:: FAILING_OVER
      :value: "FAILING_OVER"

   .. py:attribute:: STARTING
      :value: "STARTING"

   .. py:attribute:: STOPPED
      :value: "STOPPED"

   .. py:attribute:: UPDATING
      :value: "UPDATING"

.. autoclass:: Operation
   :members:
   :undoc-members:

.. autoclass:: Param
   :members:
   :undoc-members:

.. py:class:: PermissionLevel

   Permission level of the requesting user on the object. For what is allowed at each level, see [MLflow Model permissions](..).

   .. py:attribute:: CAN_CREATE_REGISTERED_MODEL
      :value: "CAN_CREATE_REGISTERED_MODEL"

   .. py:attribute:: CAN_EDIT
      :value: "CAN_EDIT"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_MANAGE_PRODUCTION_VERSIONS
      :value: "CAN_MANAGE_PRODUCTION_VERSIONS"

   .. py:attribute:: CAN_MANAGE_STAGING_VERSIONS
      :value: "CAN_MANAGE_STAGING_VERSIONS"

   .. py:attribute:: CAN_READ
      :value: "CAN_READ"

.. autoclass:: ProtoSchemaSpec
   :members:
   :undoc-members:

.. autoclass:: PublishSpec
   :members:
   :undoc-members:

.. py:class:: PublishSpecPublishMode

   .. py:attribute:: CONTINUOUS
      :value: "CONTINUOUS"

   .. py:attribute:: SNAPSHOT
      :value: "SNAPSHOT"

   .. py:attribute:: TRIGGERED
      :value: "TRIGGERED"

.. autoclass:: PublishTableResponse
   :members:
   :undoc-members:

.. autoclass:: RegisteredModelAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: RegisteredModelAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: RegisteredModelPermission
   :members:
   :undoc-members:

.. py:class:: RegisteredModelPermissionLevel

   Permission level

   .. py:attribute:: CAN_EDIT
      :value: "CAN_EDIT"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_MANAGE_PRODUCTION_VERSIONS
      :value: "CAN_MANAGE_PRODUCTION_VERSIONS"

   .. py:attribute:: CAN_MANAGE_STAGING_VERSIONS
      :value: "CAN_MANAGE_STAGING_VERSIONS"

   .. py:attribute:: CAN_READ
      :value: "CAN_READ"

.. autoclass:: RegisteredModelPermissions
   :members:
   :undoc-members:

.. autoclass:: RegisteredModelPermissionsDescription
   :members:
   :undoc-members:

.. py:class:: RegistryEmailSubscriptionType

   .. note:: Experimental: This entity may change or be removed in a future release without warning. Email subscription types for registry notifications:
   - ``ALL_EVENTS``: Subscribed to all events. - ``DEFAULT``: Default subscription type. - ``SUBSCRIBED``: Subscribed to notifications. - ``UNSUBSCRIBED``: Not subscribed to notifications.

   .. py:attribute:: ALL_EVENTS
      :value: "ALL_EVENTS"

   .. py:attribute:: DEFAULT
      :value: "DEFAULT"

   .. py:attribute:: SUBSCRIBED
      :value: "SUBSCRIBED"

   .. py:attribute:: UNSUBSCRIBED
      :value: "UNSUBSCRIBED"

.. autoclass:: RegistryWebhook
   :members:
   :undoc-members:

.. py:class:: RegistryWebhookEvent

   .. py:attribute:: COMMENT_CREATED
      :value: "COMMENT_CREATED"

   .. py:attribute:: MODEL_VERSION_CREATED
      :value: "MODEL_VERSION_CREATED"

   .. py:attribute:: MODEL_VERSION_TAG_SET
      :value: "MODEL_VERSION_TAG_SET"

   .. py:attribute:: MODEL_VERSION_TRANSITIONED_STAGE
      :value: "MODEL_VERSION_TRANSITIONED_STAGE"

   .. py:attribute:: MODEL_VERSION_TRANSITIONED_TO_ARCHIVED
      :value: "MODEL_VERSION_TRANSITIONED_TO_ARCHIVED"

   .. py:attribute:: MODEL_VERSION_TRANSITIONED_TO_PRODUCTION
      :value: "MODEL_VERSION_TRANSITIONED_TO_PRODUCTION"

   .. py:attribute:: MODEL_VERSION_TRANSITIONED_TO_STAGING
      :value: "MODEL_VERSION_TRANSITIONED_TO_STAGING"

   .. py:attribute:: REGISTERED_MODEL_CREATED
      :value: "REGISTERED_MODEL_CREATED"

   .. py:attribute:: TRANSITION_REQUEST_CREATED
      :value: "TRANSITION_REQUEST_CREATED"

   .. py:attribute:: TRANSITION_REQUEST_TO_ARCHIVED_CREATED
      :value: "TRANSITION_REQUEST_TO_ARCHIVED_CREATED"

   .. py:attribute:: TRANSITION_REQUEST_TO_PRODUCTION_CREATED
      :value: "TRANSITION_REQUEST_TO_PRODUCTION_CREATED"

   .. py:attribute:: TRANSITION_REQUEST_TO_STAGING_CREATED
      :value: "TRANSITION_REQUEST_TO_STAGING_CREATED"

.. py:class:: RegistryWebhookStatus

   Enable or disable triggering the webhook, or put the webhook into test mode. The default is ``ACTIVE``:
   - ``ACTIVE``: Webhook is triggered when an associated event happens. - ``DISABLED``: Webhook is not triggered. - ``TEST_MODE``: Webhook can be triggered through the test endpoint, but is not triggered on a real event.

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: DISABLED
      :value: "DISABLED"

   .. py:attribute:: TEST_MODE
      :value: "TEST_MODE"

.. autoclass:: RejectTransitionRequestResponse
   :members:
   :undoc-members:

.. autoclass:: RenameModelResponse
   :members:
   :undoc-members:

.. autoclass:: RequestSource
   :members:
   :undoc-members:

.. autoclass:: RestoreExperimentResponse
   :members:
   :undoc-members:

.. autoclass:: RestoreRunResponse
   :members:
   :undoc-members:

.. autoclass:: RestoreRunsResponse
   :members:
   :undoc-members:

.. autoclass:: RollingWindow
   :members:
   :undoc-members:

.. autoclass:: Run
   :members:
   :undoc-members:

.. autoclass:: RunData
   :members:
   :undoc-members:

.. autoclass:: RunInfo
   :members:
   :undoc-members:

.. py:class:: RunInfoStatus

   Status of a run.

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: FINISHED
      :value: "FINISHED"

   .. py:attribute:: KILLED
      :value: "KILLED"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SCHEDULED
      :value: "SCHEDULED"

.. autoclass:: RunInputs
   :members:
   :undoc-members:

.. autoclass:: RunTag
   :members:
   :undoc-members:

.. autoclass:: SawtoothWindow
   :members:
   :undoc-members:

.. py:class:: ScalarDataType

   Scalar data types for request-time field definitions. Only flat (non-nested) types are supported.

   .. py:attribute:: BINARY
      :value: "BINARY"

   .. py:attribute:: BOOLEAN
      :value: "BOOLEAN"

   .. py:attribute:: DATE
      :value: "DATE"

   .. py:attribute:: DECIMAL
      :value: "DECIMAL"

   .. py:attribute:: DOUBLE
      :value: "DOUBLE"

   .. py:attribute:: FLOAT
      :value: "FLOAT"

   .. py:attribute:: INTEGER
      :value: "INTEGER"

   .. py:attribute:: LONG
      :value: "LONG"

   .. py:attribute:: SHORT
      :value: "SHORT"

   .. py:attribute:: STRING
      :value: "STRING"

   .. py:attribute:: TIMESTAMP
      :value: "TIMESTAMP"

.. autoclass:: SchemaConfig
   :members:
   :undoc-members:

.. autoclass:: SchemaLocator
   :members:
   :undoc-members:

.. autoclass:: SchemaLocatorConfluentSchema
   :members:
   :undoc-members:

.. py:class:: SchemaLocatorFormat

   Supported serialization formats for a schema registry schema.

   .. py:attribute:: FORMAT_AVRO
      :value: "FORMAT_AVRO"

   .. py:attribute:: FORMAT_JSON
      :value: "FORMAT_JSON"

   .. py:attribute:: FORMAT_PROTOBUF
      :value: "FORMAT_PROTOBUF"

.. autoclass:: SchemaRegistryConfig
   :members:
   :undoc-members:

.. autoclass:: SearchExperimentsResponse
   :members:
   :undoc-members:

.. autoclass:: SearchLoggedModelsDataset
   :members:
   :undoc-members:

.. autoclass:: SearchLoggedModelsOrderBy
   :members:
   :undoc-members:

.. autoclass:: SearchLoggedModelsResponse
   :members:
   :undoc-members:

.. autoclass:: SearchModelVersionsResponse
   :members:
   :undoc-members:

.. autoclass:: SearchModelsResponse
   :members:
   :undoc-members:

.. autoclass:: SearchRunsResponse
   :members:
   :undoc-members:

.. autoclass:: SecretScopeReference
   :members:
   :undoc-members:

.. autoclass:: SetExperimentTagResponse
   :members:
   :undoc-members:

.. autoclass:: SetLoggedModelTagsResponse
   :members:
   :undoc-members:

.. autoclass:: SetModelTagResponse
   :members:
   :undoc-members:

.. autoclass:: SetModelVersionTagResponse
   :members:
   :undoc-members:

.. autoclass:: SetTagResponse
   :members:
   :undoc-members:

.. autoclass:: SlidingWindow
   :members:
   :undoc-members:

.. autoclass:: SourceLateness
   :members:
   :undoc-members:

.. py:class:: Status

   The status of the model version. Valid values are:
   - ``PENDING_REGISTRATION``: Request to register a new model version is pending as server performs background tasks. - ``FAILED_REGISTRATION``: Request to register a new model version has failed. - ``READY``: Model version is ready for use.

   .. py:attribute:: FAILED_REGISTRATION
      :value: "FAILED_REGISTRATION"

   .. py:attribute:: PENDING_REGISTRATION
      :value: "PENDING_REGISTRATION"

   .. py:attribute:: READY
      :value: "READY"

.. autoclass:: StddevPopFunction
   :members:
   :undoc-members:

.. autoclass:: StddevSampFunction
   :members:
   :undoc-members:

.. autoclass:: Stream
   :members:
   :undoc-members:

.. autoclass:: StreamArnList
   :members:
   :undoc-members:

.. autoclass:: StreamConnectionConfig
   :members:
   :undoc-members:

.. autoclass:: StreamNameList
   :members:
   :undoc-members:

.. autoclass:: StreamSchemaConfig
   :members:
   :undoc-members:

.. autoclass:: StreamSource
   :members:
   :undoc-members:

.. autoclass:: StreamSourceConfig
   :members:
   :undoc-members:

.. autoclass:: StreamingMode
   :members:
   :undoc-members:

.. py:class:: StreamingModeStreamingModeType

   .. py:attribute:: STREAMING_MODE_TYPE_MBM
      :value: "STREAMING_MODE_TYPE_MBM"

   .. py:attribute:: STREAMING_MODE_TYPE_RTM
      :value: "STREAMING_MODE_TYPE_RTM"

.. autoclass:: SubscriptionMode
   :members:
   :undoc-members:

.. autoclass:: SumFunction
   :members:
   :undoc-members:

.. autoclass:: TableTrigger
   :members:
   :undoc-members:

.. autoclass:: TestRegistryWebhookResponse
   :members:
   :undoc-members:

.. autoclass:: TimeWindow
   :members:
   :undoc-members:

.. autoclass:: TimeseriesColumn
   :members:
   :undoc-members:

.. autoclass:: TransitionRequest
   :members:
   :undoc-members:

.. autoclass:: TransitionStageResponse
   :members:
   :undoc-members:

.. autoclass:: TumblingWindow
   :members:
   :undoc-members:

.. autoclass:: UcTraceLocation
   :members:
   :undoc-members:

.. autoclass:: UpdateCommentResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateExperimentResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateModelResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateModelVersionResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateRunResponse
   :members:
   :undoc-members:

.. py:class:: UpdateRunStatus

   Status of a run.

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: FINISHED
      :value: "FINISHED"

   .. py:attribute:: KILLED
      :value: "KILLED"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SCHEDULED
      :value: "SCHEDULED"

.. autoclass:: UpdateWebhookResponse
   :members:
   :undoc-members:

.. autoclass:: VarPopFunction
   :members:
   :undoc-members:

.. autoclass:: VarSampFunction
   :members:
   :undoc-members:

.. py:class:: ViewType

   Qualifier for the view type.

   .. py:attribute:: ACTIVE_ONLY
      :value: "ACTIVE_ONLY"

   .. py:attribute:: ALL
      :value: "ALL"

   .. py:attribute:: DELETED_ONLY
      :value: "DELETED_ONLY"

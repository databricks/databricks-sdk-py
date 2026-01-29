Machine Learning
================

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.ml`` module.

.. py:currentmodule:: databricks.sdk.service.ml
.. autoclass:: Activity
   :members:
   :undoc-members:

.. py:class:: ActivityAction

   An action that a user (with sufficient permissions) could take on an activity or comment.
   For activities, valid values are: * `APPROVE_TRANSITION_REQUEST`: Approve a transition request
   * `REJECT_TRANSITION_REQUEST`: Reject a transition request
   * `CANCEL_TRANSITION_REQUEST`: Cancel (delete) a transition request
   For comments, valid values are: * `EDIT_COMMENT`: Edit the comment
   * `DELETE_COMMENT`: Delete the comment

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

   Type of activity. Valid values are: * `APPLIED_TRANSITION`: User applied the corresponding stage transition.
   * `REQUESTED_TRANSITION`: User requested the corresponding stage transition.
   * `CANCELLED_REQUEST`: User cancelled an existing transition request.
   * `APPROVED_REQUEST`: User approved the corresponding stage transition.
   * `REJECTED_REQUEST`: User rejected the coressponding stage transition.
   * `SYSTEM_TRANSITION`: For events performed as a side effect, such as archiving existing model versions in a stage.

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

.. autoclass:: ApproveTransitionRequestResponse
   :members:
   :undoc-members:

.. autoclass:: AuthConfig
   :members:
   :undoc-members:

.. autoclass:: BackfillSource
   :members:
   :undoc-members:

.. autoclass:: BatchCreateMaterializedFeaturesResponse
   :members:
   :undoc-members:

.. autoclass:: ColumnIdentifier
   :members:
   :undoc-members:

.. py:class:: CommentActivityAction

   An action that a user (with sufficient permissions) could take on an activity or comment.
   For activities, valid values are: * `APPROVE_TRANSITION_REQUEST`: Approve a transition request
   * `REJECT_TRANSITION_REQUEST`: Reject a transition request
   * `CANCEL_TRANSITION_REQUEST`: Cancel (delete) a transition request
   For comments, valid values are: * `EDIT_COMMENT`: Edit the comment
   * `DELETE_COMMENT`: Delete the comment

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

.. autoclass:: ContinuousWindow
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

.. autoclass:: DataSource
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

.. autoclass:: FileInfo
   :members:
   :undoc-members:

.. autoclass:: FinalizeLoggedModelResponse
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

.. autoclass:: FunctionExtraParameter
   :members:
   :undoc-members:

.. py:class:: FunctionFunctionType

   .. py:attribute:: APPROX_COUNT_DISTINCT
      :value: "APPROX_COUNT_DISTINCT"

   .. py:attribute:: APPROX_PERCENTILE
      :value: "APPROX_PERCENTILE"

   .. py:attribute:: AVG
      :value: "AVG"

   .. py:attribute:: COUNT
      :value: "COUNT"

   .. py:attribute:: FIRST
      :value: "FIRST"

   .. py:attribute:: LAST
      :value: "LAST"

   .. py:attribute:: MAX
      :value: "MAX"

   .. py:attribute:: MIN
      :value: "MIN"

   .. py:attribute:: STDDEV_POP
      :value: "STDDEV_POP"

   .. py:attribute:: STDDEV_SAMP
      :value: "STDDEV_SAMP"

   .. py:attribute:: SUM
      :value: "SUM"

   .. py:attribute:: VAR_POP
      :value: "VAR_POP"

   .. py:attribute:: VAR_SAMP
      :value: "VAR_SAMP"

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

.. autoclass:: Metric
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

   The status of the model version. Valid values are: * `PENDING_REGISTRATION`: Request to register a new model version is pending as server performs background tasks.
   * `FAILED_REGISTRATION`: Request to register a new model version has failed.
   * `READY`: Model version is ready for use.

   .. py:attribute:: FAILED_REGISTRATION
      :value: "FAILED_REGISTRATION"

   .. py:attribute:: PENDING_REGISTRATION
      :value: "PENDING_REGISTRATION"

   .. py:attribute:: READY
      :value: "READY"

.. autoclass:: ModelVersionTag
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

   .. note:: Experimental: This entity may change or be removed in a future release without warning. Email subscription types for registry notifications: - `ALL_EVENTS`: Subscribed to all events. - `DEFAULT`: Default subscription type. - `SUBSCRIBED`: Subscribed to notifications. - `UNSUBSCRIBED`: Not subscribed to notifications.

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

   Enable or disable triggering the webhook, or put the webhook into test mode. The default is `ACTIVE`: * `ACTIVE`: Webhook is triggered when an associated event happens.
   * `DISABLED`: Webhook is not triggered.
   * `TEST_MODE`: Webhook can be triggered through the test endpoint, but is not triggered on a real event.

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

.. autoclass:: RestoreExperimentResponse
   :members:
   :undoc-members:

.. autoclass:: RestoreRunResponse
   :members:
   :undoc-members:

.. autoclass:: RestoreRunsResponse
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

.. autoclass:: SchemaConfig
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

.. py:class:: Status

   The status of the model version. Valid values are: * `PENDING_REGISTRATION`: Request to register a new model version is pending as server performs background tasks.
   * `FAILED_REGISTRATION`: Request to register a new model version has failed.
   * `READY`: Model version is ready for use.

   .. py:attribute:: FAILED_REGISTRATION
      :value: "FAILED_REGISTRATION"

   .. py:attribute:: PENDING_REGISTRATION
      :value: "PENDING_REGISTRATION"

   .. py:attribute:: READY
      :value: "READY"

.. autoclass:: SubscriptionMode
   :members:
   :undoc-members:

.. autoclass:: TestRegistryWebhookResponse
   :members:
   :undoc-members:

.. autoclass:: TimeWindow
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

.. py:class:: ViewType

   Qualifier for the view type.

   .. py:attribute:: ACTIVE_ONLY
      :value: "ACTIVE_ONLY"

   .. py:attribute:: ALL
      :value: "ALL"

   .. py:attribute:: DELETED_ONLY
      :value: "DELETED_ONLY"

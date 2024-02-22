Machine Learning
================

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.ml`` module.

.. py:currentmodule:: databricks.sdk.service.ml
.. autoclass:: Activity
   :members:
   :undoc-members:

.. py:class:: ActivityAction

   An action that a user (with sufficient permissions) could take on an activity. Valid values are: * `APPROVE_TRANSITION_REQUEST`: Approve a transition request
   * `REJECT_TRANSITION_REQUEST`: Reject a transition request
   * `CANCEL_TRANSITION_REQUEST`: Cancel (delete) a transition request

   .. py:attribute:: APPROVE_TRANSITION_REQUEST
      :value: "APPROVE_TRANSITION_REQUEST"

   .. py:attribute:: CANCEL_TRANSITION_REQUEST
      :value: "CANCEL_TRANSITION_REQUEST"

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

.. autoclass:: ApproveTransitionRequest
   :members:
   :undoc-members:

.. autoclass:: ApproveTransitionRequestResponse
   :members:
   :undoc-members:

.. py:class:: CommentActivityAction

   An action that a user (with sufficient permissions) could take on a comment. Valid values are: * `EDIT_COMMENT`: Edit the comment
   * `DELETE_COMMENT`: Delete the comment

   .. py:attribute:: DELETE_COMMENT
      :value: "DELETE_COMMENT"

   .. py:attribute:: EDIT_COMMENT
      :value: "EDIT_COMMENT"

.. autoclass:: CommentObject
   :members:
   :undoc-members:

.. autoclass:: CreateComment
   :members:
   :undoc-members:

.. autoclass:: CreateCommentResponse
   :members:
   :undoc-members:

.. autoclass:: CreateExperiment
   :members:
   :undoc-members:

.. autoclass:: CreateExperimentResponse
   :members:
   :undoc-members:

.. autoclass:: CreateModelRequest
   :members:
   :undoc-members:

.. autoclass:: CreateModelResponse
   :members:
   :undoc-members:

.. autoclass:: CreateModelVersionRequest
   :members:
   :undoc-members:

.. autoclass:: CreateModelVersionResponse
   :members:
   :undoc-members:

.. autoclass:: CreateRegistryWebhook
   :members:
   :undoc-members:

.. autoclass:: CreateRun
   :members:
   :undoc-members:

.. autoclass:: CreateRunResponse
   :members:
   :undoc-members:

.. autoclass:: CreateTransitionRequest
   :members:
   :undoc-members:

.. autoclass:: CreateTransitionRequestResponse
   :members:
   :undoc-members:

.. autoclass:: CreateWebhookResponse
   :members:
   :undoc-members:

.. autoclass:: Dataset
   :members:
   :undoc-members:

.. autoclass:: DatasetInput
   :members:
   :undoc-members:

.. autoclass:: DeleteExperiment
   :members:
   :undoc-members:

.. autoclass:: DeleteRun
   :members:
   :undoc-members:

.. autoclass:: DeleteRuns
   :members:
   :undoc-members:

.. autoclass:: DeleteRunsResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteTag
   :members:
   :undoc-members:

.. py:class:: DeleteTransitionRequestStage

   .. py:attribute:: ARCHIVED
      :value: "ARCHIVED"

   .. py:attribute:: NONE
      :value: "NONE"

   .. py:attribute:: PRODUCTION
      :value: "PRODUCTION"

   .. py:attribute:: STAGING
      :value: "STAGING"

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

.. autoclass:: ExperimentPermissionsRequest
   :members:
   :undoc-members:

.. autoclass:: ExperimentTag
   :members:
   :undoc-members:

.. autoclass:: FileInfo
   :members:
   :undoc-members:

.. autoclass:: GetExperimentPermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GetExperimentResponse
   :members:
   :undoc-members:

.. autoclass:: GetLatestVersionsRequest
   :members:
   :undoc-members:

.. autoclass:: GetLatestVersionsResponse
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

.. autoclass:: JobSpec
   :members:
   :undoc-members:

.. autoclass:: JobSpecWithoutSecret
   :members:
   :undoc-members:

.. autoclass:: ListArtifactsResponse
   :members:
   :undoc-members:

.. autoclass:: ListExperimentsResponse
   :members:
   :undoc-members:

.. autoclass:: ListModelsResponse
   :members:
   :undoc-members:

.. autoclass:: ListRegistryWebhooks
   :members:
   :undoc-members:

.. autoclass:: ListTransitionRequestsResponse
   :members:
   :undoc-members:

.. autoclass:: LogBatch
   :members:
   :undoc-members:

.. autoclass:: LogInputs
   :members:
   :undoc-members:

.. autoclass:: LogMetric
   :members:
   :undoc-members:

.. autoclass:: LogModel
   :members:
   :undoc-members:

.. autoclass:: LogParam
   :members:
   :undoc-members:

.. autoclass:: Metric
   :members:
   :undoc-members:

.. autoclass:: Model
   :members:
   :undoc-members:

.. autoclass:: ModelDatabricks
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

   Current status of `model_version`

   .. py:attribute:: FAILED_REGISTRATION
      :value: "FAILED_REGISTRATION"

   .. py:attribute:: PENDING_REGISTRATION
      :value: "PENDING_REGISTRATION"

   .. py:attribute:: READY
      :value: "READY"

.. autoclass:: ModelVersionTag
   :members:
   :undoc-members:

.. autoclass:: Param
   :members:
   :undoc-members:

.. py:class:: PermissionLevel

   Permission level of the requesting user on the object. For what is allowed at each level, see [MLflow Model permissions](..).

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

.. autoclass:: RegisteredModelPermissionsRequest
   :members:
   :undoc-members:

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

.. autoclass:: RejectTransitionRequest
   :members:
   :undoc-members:

.. autoclass:: RejectTransitionRequestResponse
   :members:
   :undoc-members:

.. autoclass:: RenameModelRequest
   :members:
   :undoc-members:

.. autoclass:: RenameModelResponse
   :members:
   :undoc-members:

.. autoclass:: RestoreExperiment
   :members:
   :undoc-members:

.. autoclass:: RestoreRun
   :members:
   :undoc-members:

.. autoclass:: RestoreRuns
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

   Current status of the run.

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

.. autoclass:: SearchExperiments
   :members:
   :undoc-members:

.. autoclass:: SearchExperimentsResponse
   :members:
   :undoc-members:

.. py:class:: SearchExperimentsViewType

   Qualifier for type of experiments to be returned. If unspecified, return only active experiments.

   .. py:attribute:: ACTIVE_ONLY
      :value: "ACTIVE_ONLY"

   .. py:attribute:: ALL
      :value: "ALL"

   .. py:attribute:: DELETED_ONLY
      :value: "DELETED_ONLY"

.. autoclass:: SearchModelVersionsResponse
   :members:
   :undoc-members:

.. autoclass:: SearchModelsResponse
   :members:
   :undoc-members:

.. autoclass:: SearchRuns
   :members:
   :undoc-members:

.. autoclass:: SearchRunsResponse
   :members:
   :undoc-members:

.. py:class:: SearchRunsRunViewType

   Whether to display only active, only deleted, or all runs. Defaults to only active runs.

   .. py:attribute:: ACTIVE_ONLY
      :value: "ACTIVE_ONLY"

   .. py:attribute:: ALL
      :value: "ALL"

   .. py:attribute:: DELETED_ONLY
      :value: "DELETED_ONLY"

.. autoclass:: SetExperimentTag
   :members:
   :undoc-members:

.. autoclass:: SetModelTagRequest
   :members:
   :undoc-members:

.. autoclass:: SetModelVersionTagRequest
   :members:
   :undoc-members:

.. autoclass:: SetTag
   :members:
   :undoc-members:

.. py:class:: Stage

   Stage of the model version. Valid values are:
   * `None`: The initial stage of a model version.
   * `Staging`: Staging or pre-production stage.
   * `Production`: Production stage.
   * `Archived`: Archived stage.

   .. py:attribute:: ARCHIVED
      :value: "ARCHIVED"

   .. py:attribute:: NONE
      :value: "NONE"

   .. py:attribute:: PRODUCTION
      :value: "PRODUCTION"

   .. py:attribute:: STAGING
      :value: "STAGING"

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

.. autoclass:: TestRegistryWebhook
   :members:
   :undoc-members:

.. autoclass:: TestRegistryWebhookRequest
   :members:
   :undoc-members:

.. autoclass:: TestRegistryWebhookResponse
   :members:
   :undoc-members:

.. autoclass:: TransitionModelVersionStageDatabricks
   :members:
   :undoc-members:

.. autoclass:: TransitionRequest
   :members:
   :undoc-members:

.. autoclass:: TransitionStageResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateComment
   :members:
   :undoc-members:

.. autoclass:: UpdateCommentResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateExperiment
   :members:
   :undoc-members:

.. autoclass:: UpdateModelRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateModelVersionRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateRegistryWebhook
   :members:
   :undoc-members:

.. autoclass:: UpdateRun
   :members:
   :undoc-members:

.. autoclass:: UpdateRunResponse
   :members:
   :undoc-members:

.. py:class:: UpdateRunStatus

   Updated status of the run.

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

# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class Activity:
    """Activity recorded for the action."""

    # This describes an enum
    activity_type: "ActivityType"
    # User-provided comment associated with the activity.
    comment: str
    # Creation time of the object, as a Unix timestamp in milliseconds.
    creation_timestamp: int
    # Source stage of the transition (if the activity is stage transition
    # related). Valid values are:
    #
    # * `None`: The initial stage of a model version.
    #
    # * `Staging`: Staging or pre-production stage.
    #
    # * `Production`: Production stage.
    #
    # * `Archived`: Archived stage.
    from_stage: "Stage"
    # Unique identifier for the object.
    id: str
    # Time of the object at last update, as a Unix timestamp in milliseconds.
    last_updated_timestamp: int
    # Comment made by system, for example explaining an activity of type
    # `SYSTEM_TRANSITION`. It usually describes a side effect, such as a version
    # being archived as part of another version's stage transition, and may not
    # be returned for some activity types.
    system_comment: str
    # Target stage of the transition (if the activity is stage transition
    # related). Valid values are:
    #
    # * `None`: The initial stage of a model version.
    #
    # * `Staging`: Staging or pre-production stage.
    #
    # * `Production`: Production stage.
    #
    # * `Archived`: Archived stage.
    to_stage: "Stage"
    # The username of the user that created the object.
    user_id: str

    def as_request(self) -> (dict, dict):
        activity_query, activity_body = {}, {}
        if self.activity_type:
            activity_body["activity_type"] = self.activity_type.value
        if self.comment:
            activity_body["comment"] = self.comment
        if self.creation_timestamp:
            activity_body["creation_timestamp"] = self.creation_timestamp
        if self.from_stage:
            activity_body["from_stage"] = self.from_stage.value
        if self.id:
            activity_body["id"] = self.id
        if self.last_updated_timestamp:
            activity_body["last_updated_timestamp"] = self.last_updated_timestamp
        if self.system_comment:
            activity_body["system_comment"] = self.system_comment
        if self.to_stage:
            activity_body["to_stage"] = self.to_stage.value
        if self.user_id:
            activity_body["user_id"] = self.user_id

        return activity_query, activity_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Activity":
        return cls(
            activity_type=ActivityType(d["activity_type"])
            if "activity_type" in d
            else None,
            comment=d.get("comment", None),
            creation_timestamp=d.get("creation_timestamp", None),
            from_stage=Stage(d["from_stage"]) if "from_stage" in d else None,
            id=d.get("id", None),
            last_updated_timestamp=d.get("last_updated_timestamp", None),
            system_comment=d.get("system_comment", None),
            to_stage=Stage(d["to_stage"]) if "to_stage" in d else None,
            user_id=d.get("user_id", None),
        )


class ActivityAction(Enum):
    """This describes an enum"""

    APPROVE_TRANSITION_REQUEST = "APPROVE_TRANSITION_REQUEST"
    CANCEL_TRANSITION_REQUEST = "CANCEL_TRANSITION_REQUEST"
    REJECT_TRANSITION_REQUEST = "REJECT_TRANSITION_REQUEST"


class ActivityType(Enum):
    """This describes an enum"""

    APPLIED_TRANSITION = "APPLIED_TRANSITION"
    APPROVED_REQUEST = "APPROVED_REQUEST"
    CANCELLED_REQUEST = "CANCELLED_REQUEST"
    NEW_COMMENT = "NEW_COMMENT"
    REJECTED_REQUEST = "REJECTED_REQUEST"
    REQUESTED_TRANSITION = "REQUESTED_TRANSITION"
    SYSTEM_TRANSITION = "SYSTEM_TRANSITION"


@dataclass
class ApproveResponse:

    # Activity recorded for the action.
    activity: "Activity"

    def as_request(self) -> (dict, dict):
        approveResponse_query, approveResponse_body = {}, {}
        if self.activity:
            approveResponse_body["activity"] = self.activity.as_request()[1]

        return approveResponse_query, approveResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ApproveResponse":
        return cls(
            activity=Activity.from_dict(d["activity"]) if "activity" in d else None,
        )


@dataclass
class ApproveTransitionRequest:

    # Specifies whether to archive all current model versions in the target
    # stage.
    archive_existing_versions: bool
    # User-provided comment on the action.
    comment: str
    # Name of the model.
    name: str
    # Target stage of the transition. Valid values are:
    #
    # * `None`: The initial stage of a model version.
    #
    # * `Staging`: Staging or pre-production stage.
    #
    # * `Production`: Production stage.
    #
    # * `Archived`: Archived stage.
    stage: "Stage"
    # Version of the model.
    version: str

    def as_request(self) -> (dict, dict):
        approveTransitionRequest_query, approveTransitionRequest_body = {}, {}
        if self.archive_existing_versions:
            approveTransitionRequest_body[
                "archive_existing_versions"
            ] = self.archive_existing_versions
        if self.comment:
            approveTransitionRequest_body["comment"] = self.comment
        if self.name:
            approveTransitionRequest_body["name"] = self.name
        if self.stage:
            approveTransitionRequest_body["stage"] = self.stage.value
        if self.version:
            approveTransitionRequest_body["version"] = self.version

        return approveTransitionRequest_query, approveTransitionRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ApproveTransitionRequest":
        return cls(
            archive_existing_versions=d.get("archive_existing_versions", None),
            comment=d.get("comment", None),
            name=d.get("name", None),
            stage=Stage(d["stage"]) if "stage" in d else None,
            version=d.get("version", None),
        )


class CommentActivityAction(Enum):
    """This describes an enum"""

    DELETE_COMMENT = "DELETE_COMMENT"
    EDIT_COMMENT = "EDIT_COMMENT"


@dataclass
class CommentObject:
    """Comment details."""

    # Array of actions on the activity allowed for the current viewer.
    available_actions: "List[CommentActivityAction]"
    # User-provided comment on the action.
    comment: str
    # Creation time of the object, as a Unix timestamp in milliseconds.
    creation_timestamp: int
    # Time of the object at last update, as a Unix timestamp in milliseconds.
    last_updated_timestamp: int
    # The username of the user that created the object.
    user_id: str

    def as_request(self) -> (dict, dict):
        commentObject_query, commentObject_body = {}, {}
        if self.available_actions:
            commentObject_body["available_actions"] = [
                v for v in self.available_actions
            ]
        if self.comment:
            commentObject_body["comment"] = self.comment
        if self.creation_timestamp:
            commentObject_body["creation_timestamp"] = self.creation_timestamp
        if self.last_updated_timestamp:
            commentObject_body["last_updated_timestamp"] = self.last_updated_timestamp
        if self.user_id:
            commentObject_body["user_id"] = self.user_id

        return commentObject_query, commentObject_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CommentObject":
        return cls(
            available_actions=d.get("available_actions", None),
            comment=d.get("comment", None),
            creation_timestamp=d.get("creation_timestamp", None),
            last_updated_timestamp=d.get("last_updated_timestamp", None),
            user_id=d.get("user_id", None),
        )


@dataclass
class CreateComment:

    # User-provided comment on the action.
    comment: str
    # Name of the model.
    name: str
    # Version of the model.
    version: str

    def as_request(self) -> (dict, dict):
        createComment_query, createComment_body = {}, {}
        if self.comment:
            createComment_body["comment"] = self.comment
        if self.name:
            createComment_body["name"] = self.name
        if self.version:
            createComment_body["version"] = self.version

        return createComment_query, createComment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateComment":
        return cls(
            comment=d.get("comment", None),
            name=d.get("name", None),
            version=d.get("version", None),
        )


@dataclass
class CreateExperiment:

    # Location where all artifacts for the experiment are stored. If not
    # provided, the remote server will select an appropriate default.
    artifact_location: str
    # Experiment name.
    name: str
    # A collection of tags to set on the experiment. Maximum tag size and number
    # of tags per request depends on the storage backend. All storage backends
    # are guaranteed to support tag keys up to 250 bytes in size and tag values
    # up to 5000 bytes in size. All storage backends are also guaranteed to
    # support up to 20 tags per request.
    tags: "List[ExperimentTag]"

    def as_request(self) -> (dict, dict):
        createExperiment_query, createExperiment_body = {}, {}
        if self.artifact_location:
            createExperiment_body["artifact_location"] = self.artifact_location
        if self.name:
            createExperiment_body["name"] = self.name
        if self.tags:
            createExperiment_body["tags"] = [v.as_request()[1] for v in self.tags]

        return createExperiment_query, createExperiment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateExperiment":
        return cls(
            artifact_location=d.get("artifact_location", None),
            name=d.get("name", None),
            tags=[ExperimentTag.from_dict(v) for v in d["tags"]]
            if "tags" in d
            else None,
        )


@dataclass
class CreateExperimentResponse:

    # Unique identifier for the experiment.
    experiment_id: str

    def as_request(self) -> (dict, dict):
        createExperimentResponse_query, createExperimentResponse_body = {}, {}
        if self.experiment_id:
            createExperimentResponse_body["experiment_id"] = self.experiment_id

        return createExperimentResponse_query, createExperimentResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateExperimentResponse":
        return cls(
            experiment_id=d.get("experiment_id", None),
        )


@dataclass
class CreateModelVersionRequest:

    # Optional description for model version.
    description: str
    # Register model under this name
    name: str
    # MLflow run ID for correlation, if `source` was generated by an experiment
    # run in MLflow tracking server
    run_id: str
    # MLflow run link - this is the exact link of the run that generated this
    # model version, potentially hosted at another instance of MLflow.
    run_link: str
    # URI indicating the location of the model artifacts.
    source: str
    # Additional metadata for model version.
    tags: "List[ModelVersionTag]"

    def as_request(self) -> (dict, dict):
        createModelVersionRequest_query, createModelVersionRequest_body = {}, {}
        if self.description:
            createModelVersionRequest_body["description"] = self.description
        if self.name:
            createModelVersionRequest_body["name"] = self.name
        if self.run_id:
            createModelVersionRequest_body["run_id"] = self.run_id
        if self.run_link:
            createModelVersionRequest_body["run_link"] = self.run_link
        if self.source:
            createModelVersionRequest_body["source"] = self.source
        if self.tags:
            createModelVersionRequest_body["tags"] = [
                v.as_request()[1] for v in self.tags
            ]

        return createModelVersionRequest_query, createModelVersionRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateModelVersionRequest":
        return cls(
            description=d.get("description", None),
            name=d.get("name", None),
            run_id=d.get("run_id", None),
            run_link=d.get("run_link", None),
            source=d.get("source", None),
            tags=[ModelVersionTag.from_dict(v) for v in d["tags"]]
            if "tags" in d
            else None,
        )


@dataclass
class CreateModelVersionResponse:

    # Return new version number generated for this model in registry.
    model_version: "ModelVersion"

    def as_request(self) -> (dict, dict):
        createModelVersionResponse_query, createModelVersionResponse_body = {}, {}
        if self.model_version:
            createModelVersionResponse_body[
                "model_version"
            ] = self.model_version.as_request()[1]

        return createModelVersionResponse_query, createModelVersionResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateModelVersionResponse":
        return cls(
            model_version=ModelVersion.from_dict(d["model_version"])
            if "model_version" in d
            else None,
        )


@dataclass
class CreateRegisteredModelRequest:

    # Optional description for registered model.
    description: str
    # Register models under this name
    name: str
    # Additional metadata for registered model.
    tags: "List[RegisteredModelTag]"

    def as_request(self) -> (dict, dict):
        createRegisteredModelRequest_query, createRegisteredModelRequest_body = {}, {}
        if self.description:
            createRegisteredModelRequest_body["description"] = self.description
        if self.name:
            createRegisteredModelRequest_body["name"] = self.name
        if self.tags:
            createRegisteredModelRequest_body["tags"] = [
                v.as_request()[1] for v in self.tags
            ]

        return createRegisteredModelRequest_query, createRegisteredModelRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateRegisteredModelRequest":
        return cls(
            description=d.get("description", None),
            name=d.get("name", None),
            tags=[RegisteredModelTag.from_dict(v) for v in d["tags"]]
            if "tags" in d
            else None,
        )


@dataclass
class CreateRegisteredModelResponse:

    registered_model: "RegisteredModel"

    def as_request(self) -> (dict, dict):
        createRegisteredModelResponse_query, createRegisteredModelResponse_body = {}, {}
        if self.registered_model:
            createRegisteredModelResponse_body[
                "registered_model"
            ] = self.registered_model.as_request()[1]

        return createRegisteredModelResponse_query, createRegisteredModelResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateRegisteredModelResponse":
        return cls(
            registered_model=RegisteredModel.from_dict(d["registered_model"])
            if "registered_model" in d
            else None,
        )


@dataclass
class CreateRegistryWebhook:

    # User-specified description for the webhook.
    description: str
    # Events that can trigger a registry webhook: * `MODEL_VERSION_CREATED`: A
    # new model version was created for the associated model.
    #
    # * `MODEL_VERSION_TRANSITIONED_STAGE`: A model version’s stage was
    # changed.
    #
    # * `TRANSITION_REQUEST_CREATED`: A user requested a model version’s stage
    # be transitioned.
    #
    # * `COMMENT_CREATED`: A user wrote a comment on a registered model.
    #
    # * `REGISTERED_MODEL_CREATED`: A new registered model was created. This
    # event type can only be specified for a registry-wide webhook, which can be
    # created by not specifying a model name in the create request.
    #
    # * `MODEL_VERSION_TAG_SET`: A user set a tag on the model version.
    #
    # * `MODEL_VERSION_TRANSITIONED_TO_STAGING`: A model version was
    # transitioned to staging.
    #
    # * `MODEL_VERSION_TRANSITIONED_TO_PRODUCTION`: A model version was
    # transitioned to production.
    #
    # * `MODEL_VERSION_TRANSITIONED_TO_ARCHIVED`: A model version was archived.
    #
    # * `TRANSITION_REQUEST_TO_STAGING_CREATED`: A user requested a model
    # version be transitioned to staging.
    #
    # * `TRANSITION_REQUEST_TO_PRODUCTION_CREATED`: A user requested a model
    # version be transitioned to production.
    #
    # * `TRANSITION_REQUEST_TO_ARCHIVED_CREATED`: A user requested a model
    # version be archived.
    events: "List[RegistryWebhookEvent]"

    http_url_spec: "HttpUrlSpec"

    job_spec: "JobSpec"
    # Name of the model whose events would trigger this webhook.
    model_name: str
    # This describes an enum
    status: "RegistryWebhookStatus"

    def as_request(self) -> (dict, dict):
        createRegistryWebhook_query, createRegistryWebhook_body = {}, {}
        if self.description:
            createRegistryWebhook_body["description"] = self.description
        if self.events:
            createRegistryWebhook_body["events"] = [v for v in self.events]
        if self.http_url_spec:
            createRegistryWebhook_body[
                "http_url_spec"
            ] = self.http_url_spec.as_request()[1]
        if self.job_spec:
            createRegistryWebhook_body["job_spec"] = self.job_spec.as_request()[1]
        if self.model_name:
            createRegistryWebhook_body["model_name"] = self.model_name
        if self.status:
            createRegistryWebhook_body["status"] = self.status.value

        return createRegistryWebhook_query, createRegistryWebhook_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateRegistryWebhook":
        return cls(
            description=d.get("description", None),
            events=d.get("events", None),
            http_url_spec=HttpUrlSpec.from_dict(d["http_url_spec"])
            if "http_url_spec" in d
            else None,
            job_spec=JobSpec.from_dict(d["job_spec"]) if "job_spec" in d else None,
            model_name=d.get("model_name", None),
            status=RegistryWebhookStatus(d["status"]) if "status" in d else None,
        )


@dataclass
class CreateResponse:

    # Comment details.
    comment: "CommentObject"

    def as_request(self) -> (dict, dict):
        createResponse_query, createResponse_body = {}, {}
        if self.comment:
            createResponse_body["comment"] = self.comment.as_request()[1]

        return createResponse_query, createResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateResponse":
        return cls(
            comment=CommentObject.from_dict(d["comment"]) if "comment" in d else None,
        )


@dataclass
class CreateRun:

    # ID of the associated experiment.
    experiment_id: str
    # Unix timestamp in milliseconds of when the run started.
    start_time: int
    # Additional metadata for run.
    tags: "List[RunTag]"
    # ID of the user executing the run. This field is deprecated as of MLflow
    # 1.0, and will be removed in a future MLflow release. Use 'mlflow.user' tag
    # instead.
    user_id: str

    def as_request(self) -> (dict, dict):
        createRun_query, createRun_body = {}, {}
        if self.experiment_id:
            createRun_body["experiment_id"] = self.experiment_id
        if self.start_time:
            createRun_body["start_time"] = self.start_time
        if self.tags:
            createRun_body["tags"] = [v.as_request()[1] for v in self.tags]
        if self.user_id:
            createRun_body["user_id"] = self.user_id

        return createRun_query, createRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateRun":
        return cls(
            experiment_id=d.get("experiment_id", None),
            start_time=d.get("start_time", None),
            tags=[RunTag.from_dict(v) for v in d["tags"]] if "tags" in d else None,
            user_id=d.get("user_id", None),
        )


@dataclass
class CreateRunResponse:

    # The newly created run.
    run: "Run"

    def as_request(self) -> (dict, dict):
        createRunResponse_query, createRunResponse_body = {}, {}
        if self.run:
            createRunResponse_body["run"] = self.run.as_request()[1]

        return createRunResponse_query, createRunResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateRunResponse":
        return cls(
            run=Run.from_dict(d["run"]) if "run" in d else None,
        )


@dataclass
class CreateTransitionRequest:

    # User-provided comment on the action.
    comment: str
    # Name of the model.
    name: str
    # Target stage of the transition. Valid values are:
    #
    # * `None`: The initial stage of a model version.
    #
    # * `Staging`: Staging or pre-production stage.
    #
    # * `Production`: Production stage.
    #
    # * `Archived`: Archived stage.
    stage: "Stage"
    # Version of the model.
    version: str

    def as_request(self) -> (dict, dict):
        createTransitionRequest_query, createTransitionRequest_body = {}, {}
        if self.comment:
            createTransitionRequest_body["comment"] = self.comment
        if self.name:
            createTransitionRequest_body["name"] = self.name
        if self.stage:
            createTransitionRequest_body["stage"] = self.stage.value
        if self.version:
            createTransitionRequest_body["version"] = self.version

        return createTransitionRequest_query, createTransitionRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateTransitionRequest":
        return cls(
            comment=d.get("comment", None),
            name=d.get("name", None),
            stage=Stage(d["stage"]) if "stage" in d else None,
            version=d.get("version", None),
        )


@dataclass
class DeleteExperiment:

    # ID of the associated experiment.
    experiment_id: str

    def as_request(self) -> (dict, dict):
        deleteExperiment_query, deleteExperiment_body = {}, {}
        if self.experiment_id:
            deleteExperiment_body["experiment_id"] = self.experiment_id

        return deleteExperiment_query, deleteExperiment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteExperiment":
        return cls(
            experiment_id=d.get("experiment_id", None),
        )


@dataclass
class DeleteModelVersionCommentRequest:
    """Delete a comment"""

    id: str  # query

    def as_request(self) -> (dict, dict):
        (
            deleteModelVersionCommentRequest_query,
            deleteModelVersionCommentRequest_body,
        ) = ({}, {})
        if self.id:
            deleteModelVersionCommentRequest_query["id"] = self.id

        return (
            deleteModelVersionCommentRequest_query,
            deleteModelVersionCommentRequest_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteModelVersionCommentRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class DeleteModelVersionRequest:
    """Delete a model version."""

    # Name of the registered model
    name: str  # query
    # Model version number
    version: str  # query

    def as_request(self) -> (dict, dict):
        deleteModelVersionRequest_query, deleteModelVersionRequest_body = {}, {}
        if self.name:
            deleteModelVersionRequest_query["name"] = self.name
        if self.version:
            deleteModelVersionRequest_query["version"] = self.version

        return deleteModelVersionRequest_query, deleteModelVersionRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteModelVersionRequest":
        return cls(
            name=d.get("name", None),
            version=d.get("version", None),
        )


@dataclass
class DeleteModelVersionTagRequest:
    """Delete a model version tag"""

    # Name of the tag. The name must be an exact match; wild-card deletion is
    # not supported. Maximum size is 250 bytes.
    key: str  # query
    # Name of the registered model that the tag was logged under.
    name: str  # query
    # Model version number that the tag was logged under.
    version: str  # query

    def as_request(self) -> (dict, dict):
        deleteModelVersionTagRequest_query, deleteModelVersionTagRequest_body = {}, {}
        if self.key:
            deleteModelVersionTagRequest_query["key"] = self.key
        if self.name:
            deleteModelVersionTagRequest_query["name"] = self.name
        if self.version:
            deleteModelVersionTagRequest_query["version"] = self.version

        return deleteModelVersionTagRequest_query, deleteModelVersionTagRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteModelVersionTagRequest":
        return cls(
            key=d.get("key", None),
            name=d.get("name", None),
            version=d.get("version", None),
        )


@dataclass
class DeleteRegisteredModelRequest:
    """Delete a model"""

    # Registered model unique name identifier.
    name: str  # query

    def as_request(self) -> (dict, dict):
        deleteRegisteredModelRequest_query, deleteRegisteredModelRequest_body = {}, {}
        if self.name:
            deleteRegisteredModelRequest_query["name"] = self.name

        return deleteRegisteredModelRequest_query, deleteRegisteredModelRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteRegisteredModelRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class DeleteRegisteredModelTagRequest:
    """Delete a model tag"""

    # Name of the tag. The name must be an exact match; wild-card deletion is
    # not supported. Maximum size is 250 bytes.
    key: str  # query
    # Name of the registered model that the tag was logged under.
    name: str  # query

    def as_request(self) -> (dict, dict):
        deleteRegisteredModelTagRequest_query, deleteRegisteredModelTagRequest_body = (
            {},
            {},
        )
        if self.key:
            deleteRegisteredModelTagRequest_query["key"] = self.key
        if self.name:
            deleteRegisteredModelTagRequest_query["name"] = self.name

        return (
            deleteRegisteredModelTagRequest_query,
            deleteRegisteredModelTagRequest_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteRegisteredModelTagRequest":
        return cls(
            key=d.get("key", None),
            name=d.get("name", None),
        )


@dataclass
class DeleteRegistryWebhookRequest:
    """Delete a webhook"""

    # Webhook ID required to delete a registry webhook.
    id: str  # query

    def as_request(self) -> (dict, dict):
        deleteRegistryWebhookRequest_query, deleteRegistryWebhookRequest_body = {}, {}
        if self.id:
            deleteRegistryWebhookRequest_query["id"] = self.id

        return deleteRegistryWebhookRequest_query, deleteRegistryWebhookRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteRegistryWebhookRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class DeleteRun:

    # ID of the run to delete.
    run_id: str

    def as_request(self) -> (dict, dict):
        deleteRun_query, deleteRun_body = {}, {}
        if self.run_id:
            deleteRun_body["run_id"] = self.run_id

        return deleteRun_query, deleteRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteRun":
        return cls(
            run_id=d.get("run_id", None),
        )


@dataclass
class DeleteTag:

    # Name of the tag. Maximum size is 255 bytes. Must be provided.
    key: str
    # ID of the run that the tag was logged under. Must be provided.
    run_id: str

    def as_request(self) -> (dict, dict):
        deleteTag_query, deleteTag_body = {}, {}
        if self.key:
            deleteTag_body["key"] = self.key
        if self.run_id:
            deleteTag_body["run_id"] = self.run_id

        return deleteTag_query, deleteTag_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteTag":
        return cls(
            key=d.get("key", None),
            run_id=d.get("run_id", None),
        )


@dataclass
class DeleteTransitionRequestRequest:
    """Delete a ransition request"""

    # User-provided comment on the action.
    comment: str  # query
    # Username of the user who created this request. Of the transition requests
    # matching the specified details, only the one transition created by this
    # user will be deleted.
    creator: str  # query
    # Name of the model.
    name: str  # query
    # Target stage of the transition request. Valid values are:
    #
    # * `None`: The initial stage of a model version.
    #
    # * `Staging`: Staging or pre-production stage.
    #
    # * `Production`: Production stage.
    #
    # * `Archived`: Archived stage.
    stage: str  # query
    # Version of the model.
    version: str  # query

    def as_request(self) -> (dict, dict):
        deleteTransitionRequestRequest_query, deleteTransitionRequestRequest_body = (
            {},
            {},
        )
        if self.comment:
            deleteTransitionRequestRequest_query["comment"] = self.comment
        if self.creator:
            deleteTransitionRequestRequest_query["creator"] = self.creator
        if self.name:
            deleteTransitionRequestRequest_query["name"] = self.name
        if self.stage:
            deleteTransitionRequestRequest_query["stage"] = self.stage
        if self.version:
            deleteTransitionRequestRequest_query["version"] = self.version

        return deleteTransitionRequestRequest_query, deleteTransitionRequestRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteTransitionRequestRequest":
        return cls(
            comment=d.get("comment", None),
            creator=d.get("creator", None),
            name=d.get("name", None),
            stage=d.get("stage", None),
            version=d.get("version", None),
        )


@dataclass
class Experiment:

    # Location where artifacts for the experiment are stored.
    artifact_location: str
    # Creation time
    creation_time: int
    # Unique identifier for the experiment.
    experiment_id: str
    # Last update time
    last_update_time: int
    # Current life cycle stage of the experiment: "active" or "deleted". Deleted
    # experiments are not returned by APIs.
    lifecycle_stage: str
    # Human readable name that identifies the experiment.
    name: str
    # Tags: Additional metadata key-value pairs.
    tags: "List[ExperimentTag]"

    def as_request(self) -> (dict, dict):
        experiment_query, experiment_body = {}, {}
        if self.artifact_location:
            experiment_body["artifact_location"] = self.artifact_location
        if self.creation_time:
            experiment_body["creation_time"] = self.creation_time
        if self.experiment_id:
            experiment_body["experiment_id"] = self.experiment_id
        if self.last_update_time:
            experiment_body["last_update_time"] = self.last_update_time
        if self.lifecycle_stage:
            experiment_body["lifecycle_stage"] = self.lifecycle_stage
        if self.name:
            experiment_body["name"] = self.name
        if self.tags:
            experiment_body["tags"] = [v.as_request()[1] for v in self.tags]

        return experiment_query, experiment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Experiment":
        return cls(
            artifact_location=d.get("artifact_location", None),
            creation_time=d.get("creation_time", None),
            experiment_id=d.get("experiment_id", None),
            last_update_time=d.get("last_update_time", None),
            lifecycle_stage=d.get("lifecycle_stage", None),
            name=d.get("name", None),
            tags=[ExperimentTag.from_dict(v) for v in d["tags"]]
            if "tags" in d
            else None,
        )


@dataclass
class ExperimentTag:

    # The tag key.
    key: str
    # The tag value.
    value: str

    def as_request(self) -> (dict, dict):
        experimentTag_query, experimentTag_body = {}, {}
        if self.key:
            experimentTag_body["key"] = self.key
        if self.value:
            experimentTag_body["value"] = self.value

        return experimentTag_query, experimentTag_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ExperimentTag":
        return cls(
            key=d.get("key", None),
            value=d.get("value", None),
        )


@dataclass
class FileInfo:

    # Size in bytes. Unset for directories.
    file_size: int
    # Whether the path is a directory.
    is_dir: bool
    # Path relative to the root artifact directory run.
    path: str

    def as_request(self) -> (dict, dict):
        fileInfo_query, fileInfo_body = {}, {}
        if self.file_size:
            fileInfo_body["file_size"] = self.file_size
        if self.is_dir:
            fileInfo_body["is_dir"] = self.is_dir
        if self.path:
            fileInfo_body["path"] = self.path

        return fileInfo_query, fileInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "FileInfo":
        return cls(
            file_size=d.get("file_size", None),
            is_dir=d.get("is_dir", None),
            path=d.get("path", None),
        )


@dataclass
class GetByNameRequest:
    """Get metadata"""

    # Name of the associated experiment.
    experiment_name: str  # query

    def as_request(self) -> (dict, dict):
        getByNameRequest_query, getByNameRequest_body = {}, {}
        if self.experiment_name:
            getByNameRequest_query["experiment_name"] = self.experiment_name

        return getByNameRequest_query, getByNameRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetByNameRequest":
        return cls(
            experiment_name=d.get("experiment_name", None),
        )


@dataclass
class GetExperimentByNameResponse:

    # Experiment details.
    experiment: "Experiment"

    def as_request(self) -> (dict, dict):
        getExperimentByNameResponse_query, getExperimentByNameResponse_body = {}, {}
        if self.experiment:
            getExperimentByNameResponse_body[
                "experiment"
            ] = self.experiment.as_request()[1]

        return getExperimentByNameResponse_query, getExperimentByNameResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetExperimentByNameResponse":
        return cls(
            experiment=Experiment.from_dict(d["experiment"])
            if "experiment" in d
            else None,
        )


@dataclass
class GetExperimentRequest:
    """Get an experiment"""

    # ID of the associated experiment.
    experiment_id: str  # query

    def as_request(self) -> (dict, dict):
        getExperimentRequest_query, getExperimentRequest_body = {}, {}
        if self.experiment_id:
            getExperimentRequest_query["experiment_id"] = self.experiment_id

        return getExperimentRequest_query, getExperimentRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetExperimentRequest":
        return cls(
            experiment_id=d.get("experiment_id", None),
        )


@dataclass
class GetHistoryRequest:
    """Get all history"""

    # Name of the metric.
    metric_key: str  # query
    # ID of the run from which to fetch metric values. Must be provided.
    run_id: str  # query
    # [Deprecated, use run_id instead] ID of the run from which to fetch metric
    # values. This field will be removed in a future MLflow version.
    run_uuid: str  # query

    def as_request(self) -> (dict, dict):
        getHistoryRequest_query, getHistoryRequest_body = {}, {}
        if self.metric_key:
            getHistoryRequest_query["metric_key"] = self.metric_key
        if self.run_id:
            getHistoryRequest_query["run_id"] = self.run_id
        if self.run_uuid:
            getHistoryRequest_query["run_uuid"] = self.run_uuid

        return getHistoryRequest_query, getHistoryRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetHistoryRequest":
        return cls(
            metric_key=d.get("metric_key", None),
            run_id=d.get("run_id", None),
            run_uuid=d.get("run_uuid", None),
        )


@dataclass
class GetLatestVersionsRequest:

    # Registered model unique name identifier.
    name: str
    # List of stages.
    stages: "List[str]"

    def as_request(self) -> (dict, dict):
        getLatestVersionsRequest_query, getLatestVersionsRequest_body = {}, {}
        if self.name:
            getLatestVersionsRequest_body["name"] = self.name
        if self.stages:
            getLatestVersionsRequest_body["stages"] = [v for v in self.stages]

        return getLatestVersionsRequest_query, getLatestVersionsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetLatestVersionsRequest":
        return cls(
            name=d.get("name", None),
            stages=d.get("stages", None),
        )


@dataclass
class GetLatestVersionsResponse:

    # Latest version models for each requests stage. Only return models with
    # current `READY` status. If no `stages` provided, returns the latest
    # version for each stage, including `"None"`.
    model_versions: "List[ModelVersion]"

    def as_request(self) -> (dict, dict):
        getLatestVersionsResponse_query, getLatestVersionsResponse_body = {}, {}
        if self.model_versions:
            getLatestVersionsResponse_body["model_versions"] = [
                v.as_request()[1] for v in self.model_versions
            ]

        return getLatestVersionsResponse_query, getLatestVersionsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetLatestVersionsResponse":
        return cls(
            model_versions=[ModelVersion.from_dict(v) for v in d["model_versions"]]
            if "model_versions" in d
            else None,
        )


@dataclass
class GetMLflowDatabrickRequest:
    """Get model"""

    # Name of the model.
    name: str  # query

    def as_request(self) -> (dict, dict):
        getMLflowDatabrickRequest_query, getMLflowDatabrickRequest_body = {}, {}
        if self.name:
            getMLflowDatabrickRequest_query["name"] = self.name

        return getMLflowDatabrickRequest_query, getMLflowDatabrickRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetMLflowDatabrickRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class GetMetricHistoryResponse:

    # All logged values for this metric.
    metrics: "List[Metric]"

    def as_request(self) -> (dict, dict):
        getMetricHistoryResponse_query, getMetricHistoryResponse_body = {}, {}
        if self.metrics:
            getMetricHistoryResponse_body["metrics"] = [
                v.as_request()[1] for v in self.metrics
            ]

        return getMetricHistoryResponse_query, getMetricHistoryResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetMetricHistoryResponse":
        return cls(
            metrics=[Metric.from_dict(v) for v in d["metrics"]]
            if "metrics" in d
            else None,
        )


@dataclass
class GetModelVersionDownloadUriRequest:
    """Get a model version URI"""

    # Name of the registered model
    name: str  # query
    # Model version number
    version: str  # query

    def as_request(self) -> (dict, dict):
        (
            getModelVersionDownloadUriRequest_query,
            getModelVersionDownloadUriRequest_body,
        ) = ({}, {})
        if self.name:
            getModelVersionDownloadUriRequest_query["name"] = self.name
        if self.version:
            getModelVersionDownloadUriRequest_query["version"] = self.version

        return (
            getModelVersionDownloadUriRequest_query,
            getModelVersionDownloadUriRequest_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetModelVersionDownloadUriRequest":
        return cls(
            name=d.get("name", None),
            version=d.get("version", None),
        )


@dataclass
class GetModelVersionDownloadUriResponse:

    # URI corresponding to where artifacts for this model version are stored.
    artifact_uri: str

    def as_request(self) -> (dict, dict):
        (
            getModelVersionDownloadUriResponse_query,
            getModelVersionDownloadUriResponse_body,
        ) = ({}, {})
        if self.artifact_uri:
            getModelVersionDownloadUriResponse_body["artifact_uri"] = self.artifact_uri

        return (
            getModelVersionDownloadUriResponse_query,
            getModelVersionDownloadUriResponse_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetModelVersionDownloadUriResponse":
        return cls(
            artifact_uri=d.get("artifact_uri", None),
        )


@dataclass
class GetModelVersionRequest:
    """Get a model version"""

    # Name of the registered model
    name: str  # query
    # Model version number
    version: str  # query

    def as_request(self) -> (dict, dict):
        getModelVersionRequest_query, getModelVersionRequest_body = {}, {}
        if self.name:
            getModelVersionRequest_query["name"] = self.name
        if self.version:
            getModelVersionRequest_query["version"] = self.version

        return getModelVersionRequest_query, getModelVersionRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetModelVersionRequest":
        return cls(
            name=d.get("name", None),
            version=d.get("version", None),
        )


@dataclass
class GetModelVersionResponse:

    model_version: "ModelVersion"

    def as_request(self) -> (dict, dict):
        getModelVersionResponse_query, getModelVersionResponse_body = {}, {}
        if self.model_version:
            getModelVersionResponse_body[
                "model_version"
            ] = self.model_version.as_request()[1]

        return getModelVersionResponse_query, getModelVersionResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetModelVersionResponse":
        return cls(
            model_version=ModelVersion.from_dict(d["model_version"])
            if "model_version" in d
            else None,
        )


@dataclass
class GetRegisteredModelRequest:
    """Get a model"""

    # Registered model unique name identifier.
    name: str  # query

    def as_request(self) -> (dict, dict):
        getRegisteredModelRequest_query, getRegisteredModelRequest_body = {}, {}
        if self.name:
            getRegisteredModelRequest_query["name"] = self.name

        return getRegisteredModelRequest_query, getRegisteredModelRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetRegisteredModelRequest":
        return cls(
            name=d.get("name", None),
        )


@dataclass
class GetRegisteredModelResponse:

    registered_model: "RegisteredModel"

    def as_request(self) -> (dict, dict):
        getRegisteredModelResponse_query, getRegisteredModelResponse_body = {}, {}
        if self.registered_model:
            getRegisteredModelResponse_body[
                "registered_model"
            ] = self.registered_model.as_request()[1]

        return getRegisteredModelResponse_query, getRegisteredModelResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetRegisteredModelResponse":
        return cls(
            registered_model=RegisteredModel.from_dict(d["registered_model"])
            if "registered_model" in d
            else None,
        )


@dataclass
class GetResponse:

    registered_model: "RegisteredModelDatabricks"

    def as_request(self) -> (dict, dict):
        getResponse_query, getResponse_body = {}, {}
        if self.registered_model:
            getResponse_body["registered_model"] = self.registered_model.as_request()[1]

        return getResponse_query, getResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetResponse":
        return cls(
            registered_model=RegisteredModelDatabricks.from_dict(d["registered_model"])
            if "registered_model" in d
            else None,
        )


@dataclass
class GetRunRequest:
    """Get a run"""

    # ID of the run to fetch. Must be provided.
    run_id: str  # query
    # [Deprecated, use run_id instead] ID of the run to fetch. This field will
    # be removed in a future MLflow version.
    run_uuid: str  # query

    def as_request(self) -> (dict, dict):
        getRunRequest_query, getRunRequest_body = {}, {}
        if self.run_id:
            getRunRequest_query["run_id"] = self.run_id
        if self.run_uuid:
            getRunRequest_query["run_uuid"] = self.run_uuid

        return getRunRequest_query, getRunRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetRunRequest":
        return cls(
            run_id=d.get("run_id", None),
            run_uuid=d.get("run_uuid", None),
        )


@dataclass
class GetRunResponse:

    # Run metadata (name, start time, etc) and data (metrics, params, and tags).
    run: "Run"

    def as_request(self) -> (dict, dict):
        getRunResponse_query, getRunResponse_body = {}, {}
        if self.run:
            getRunResponse_body["run"] = self.run.as_request()[1]

        return getRunResponse_query, getRunResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetRunResponse":
        return cls(
            run=Run.from_dict(d["run"]) if "run" in d else None,
        )


@dataclass
class HttpUrlSpec:

    # Value of the authorization header that should be sent in the request sent
    # by the wehbook. It should be of the form `"<auth type> <credentials>"`. If
    # set to an empty string, no authorization header will be included in the
    # request.
    authorization: str
    # Enable/disable SSL certificate validation. Default is true. For
    # self-signed certificates, this field must be false AND the destination
    # server must disable certificate validation as well. For security purposes,
    # it is encouraged to perform secret validation with the HMAC-encoded
    # portion of the payload and acknowledge the risk associated with disabling
    # hostname validation whereby it becomes more likely that requests can be
    # maliciously routed to an unintended host.
    enable_ssl_verification: bool
    # Shared secret required for HMAC encoding payload. The HMAC-encoded payload
    # will be sent in the header as: { "X-Databricks-Signature":
    # $encoded_payload }.
    secret: str
    # External HTTPS URL called on event trigger (by using a POST request).
    url: str

    def as_request(self) -> (dict, dict):
        httpUrlSpec_query, httpUrlSpec_body = {}, {}
        if self.authorization:
            httpUrlSpec_body["authorization"] = self.authorization
        if self.enable_ssl_verification:
            httpUrlSpec_body["enable_ssl_verification"] = self.enable_ssl_verification
        if self.secret:
            httpUrlSpec_body["secret"] = self.secret
        if self.url:
            httpUrlSpec_body["url"] = self.url

        return httpUrlSpec_query, httpUrlSpec_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "HttpUrlSpec":
        return cls(
            authorization=d.get("authorization", None),
            enable_ssl_verification=d.get("enable_ssl_verification", None),
            secret=d.get("secret", None),
            url=d.get("url", None),
        )


@dataclass
class HttpUrlSpecWithoutSecret:

    # Enable/disable SSL certificate validation. Default is true. For
    # self-signed certificates, this field must be false AND the destination
    # server must disable certificate validation as well. For security purposes,
    # it is encouraged to perform secret validation with the HMAC-encoded
    # portion of the payload and acknowledge the risk associated with disabling
    # hostname validation whereby it becomes more likely that requests can be
    # maliciously routed to an unintended host.
    enable_ssl_verification: bool
    # External HTTPS URL called on event trigger (by using a POST request).
    url: str

    def as_request(self) -> (dict, dict):
        httpUrlSpecWithoutSecret_query, httpUrlSpecWithoutSecret_body = {}, {}
        if self.enable_ssl_verification:
            httpUrlSpecWithoutSecret_body[
                "enable_ssl_verification"
            ] = self.enable_ssl_verification
        if self.url:
            httpUrlSpecWithoutSecret_body["url"] = self.url

        return httpUrlSpecWithoutSecret_query, httpUrlSpecWithoutSecret_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "HttpUrlSpecWithoutSecret":
        return cls(
            enable_ssl_verification=d.get("enable_ssl_verification", None),
            url=d.get("url", None),
        )


@dataclass
class JobSpec:

    # The personal access token used to authorize webhook's job runs.
    access_token: str
    # ID of the job that the webhook runs.
    job_id: str
    # URL of the workspace containing the job that this webhook runs. If not
    # specified, the job’s workspace URL is assumed to be the same as the
    # workspace where the webhook is created.
    workspace_url: str

    def as_request(self) -> (dict, dict):
        jobSpec_query, jobSpec_body = {}, {}
        if self.access_token:
            jobSpec_body["access_token"] = self.access_token
        if self.job_id:
            jobSpec_body["job_id"] = self.job_id
        if self.workspace_url:
            jobSpec_body["workspace_url"] = self.workspace_url

        return jobSpec_query, jobSpec_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "JobSpec":
        return cls(
            access_token=d.get("access_token", None),
            job_id=d.get("job_id", None),
            workspace_url=d.get("workspace_url", None),
        )


@dataclass
class JobSpecWithoutSecret:

    # ID of the job that the webhook runs.
    job_id: str
    # URL of the workspace containing the job that this webhook runs. Defaults
    # to the workspace URL in which the webhook is created. If not specified,
    # the job’s workspace is assumed to be the same as the webhook’s.
    workspace_url: str

    def as_request(self) -> (dict, dict):
        jobSpecWithoutSecret_query, jobSpecWithoutSecret_body = {}, {}
        if self.job_id:
            jobSpecWithoutSecret_body["job_id"] = self.job_id
        if self.workspace_url:
            jobSpecWithoutSecret_body["workspace_url"] = self.workspace_url

        return jobSpecWithoutSecret_query, jobSpecWithoutSecret_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "JobSpecWithoutSecret":
        return cls(
            job_id=d.get("job_id", None),
            workspace_url=d.get("workspace_url", None),
        )


@dataclass
class ListArtifactsRequest:
    """Get all artifacts"""

    # Token indicating the page of artifact results to fetch
    page_token: str  # query
    # Filter artifacts matching this path (a relative path from the root
    # artifact directory).
    path: str  # query
    # ID of the run whose artifacts to list. Must be provided.
    run_id: str  # query
    # [Deprecated, use run_id instead] ID of the run whose artifacts to list.
    # This field will be removed in a future MLflow version.
    run_uuid: str  # query

    def as_request(self) -> (dict, dict):
        listArtifactsRequest_query, listArtifactsRequest_body = {}, {}
        if self.page_token:
            listArtifactsRequest_query["page_token"] = self.page_token
        if self.path:
            listArtifactsRequest_query["path"] = self.path
        if self.run_id:
            listArtifactsRequest_query["run_id"] = self.run_id
        if self.run_uuid:
            listArtifactsRequest_query["run_uuid"] = self.run_uuid

        return listArtifactsRequest_query, listArtifactsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListArtifactsRequest":
        return cls(
            page_token=d.get("page_token", None),
            path=d.get("path", None),
            run_id=d.get("run_id", None),
            run_uuid=d.get("run_uuid", None),
        )


@dataclass
class ListArtifactsResponse:

    # File location and metadata for artifacts.
    files: "List[FileInfo]"
    # Token that can be used to retrieve the next page of artifact results
    next_page_token: str
    # Root artifact directory for the run.
    root_uri: str

    def as_request(self) -> (dict, dict):
        listArtifactsResponse_query, listArtifactsResponse_body = {}, {}
        if self.files:
            listArtifactsResponse_body["files"] = [
                v.as_request()[1] for v in self.files
            ]
        if self.next_page_token:
            listArtifactsResponse_body["next_page_token"] = self.next_page_token
        if self.root_uri:
            listArtifactsResponse_body["root_uri"] = self.root_uri

        return listArtifactsResponse_query, listArtifactsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListArtifactsResponse":
        return cls(
            files=[FileInfo.from_dict(v) for v in d["files"]] if "files" in d else None,
            next_page_token=d.get("next_page_token", None),
            root_uri=d.get("root_uri", None),
        )


@dataclass
class ListExperimentsRequest:
    """List experiments"""

    # Maximum number of experiments desired. If `max_results` is unspecified,
    # return all experiments. If `max_results` is too large, it'll be
    # automatically capped at 1000. Callers of this endpoint are encouraged to
    # pass max_results explicitly and leverage page_token to iterate through
    # experiments.
    max_results: int  # query
    # Token indicating the page of experiments to fetch
    page_token: str  # query
    # Qualifier for type of experiments to be returned. If unspecified, return
    # only active experiments.
    view_type: str  # query

    def as_request(self) -> (dict, dict):
        listExperimentsRequest_query, listExperimentsRequest_body = {}, {}
        if self.max_results:
            listExperimentsRequest_query["max_results"] = self.max_results
        if self.page_token:
            listExperimentsRequest_query["page_token"] = self.page_token
        if self.view_type:
            listExperimentsRequest_query["view_type"] = self.view_type

        return listExperimentsRequest_query, listExperimentsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListExperimentsRequest":
        return cls(
            max_results=d.get("max_results", None),
            page_token=d.get("page_token", None),
            view_type=d.get("view_type", None),
        )


@dataclass
class ListExperimentsResponse:

    # Paginated Experiments beginning with the first item on the requested page.
    experiments: "List[Experiment]"
    # Token that can be used to retrieve the next page of experiments. Empty
    # token means no more experiment is available for retrieval.
    next_page_token: str

    def as_request(self) -> (dict, dict):
        listExperimentsResponse_query, listExperimentsResponse_body = {}, {}
        if self.experiments:
            listExperimentsResponse_body["experiments"] = [
                v.as_request()[1] for v in self.experiments
            ]
        if self.next_page_token:
            listExperimentsResponse_body["next_page_token"] = self.next_page_token

        return listExperimentsResponse_query, listExperimentsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListExperimentsResponse":
        return cls(
            experiments=[Experiment.from_dict(v) for v in d["experiments"]]
            if "experiments" in d
            else None,
            next_page_token=d.get("next_page_token", None),
        )


@dataclass
class ListRegisteredModelsRequest:
    """List models"""

    # Maximum number of registered models desired. Max threshold is 1000.
    max_results: int  # query
    # Pagination token to go to the next page based on a previous query.
    page_token: str  # query

    def as_request(self) -> (dict, dict):
        listRegisteredModelsRequest_query, listRegisteredModelsRequest_body = {}, {}
        if self.max_results:
            listRegisteredModelsRequest_query["max_results"] = self.max_results
        if self.page_token:
            listRegisteredModelsRequest_query["page_token"] = self.page_token

        return listRegisteredModelsRequest_query, listRegisteredModelsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListRegisteredModelsRequest":
        return cls(
            max_results=d.get("max_results", None),
            page_token=d.get("page_token", None),
        )


@dataclass
class ListRegisteredModelsResponse:

    # Pagination token to request next page of models for the same query.
    next_page_token: str

    registered_models: "List[RegisteredModel]"

    def as_request(self) -> (dict, dict):
        listRegisteredModelsResponse_query, listRegisteredModelsResponse_body = {}, {}
        if self.next_page_token:
            listRegisteredModelsResponse_body["next_page_token"] = self.next_page_token
        if self.registered_models:
            listRegisteredModelsResponse_body["registered_models"] = [
                v.as_request()[1] for v in self.registered_models
            ]

        return listRegisteredModelsResponse_query, listRegisteredModelsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListRegisteredModelsResponse":
        return cls(
            next_page_token=d.get("next_page_token", None),
            registered_models=[
                RegisteredModel.from_dict(v) for v in d["registered_models"]
            ]
            if "registered_models" in d
            else None,
        )


@dataclass
class ListRegistryWebhooks:

    # Token that can be used to retrieve the next page of artifact results
    next_page_token: str
    # Array of registry webhooks.
    webhooks: "List[RegistryWebhook]"

    def as_request(self) -> (dict, dict):
        listRegistryWebhooks_query, listRegistryWebhooks_body = {}, {}
        if self.next_page_token:
            listRegistryWebhooks_body["next_page_token"] = self.next_page_token
        if self.webhooks:
            listRegistryWebhooks_body["webhooks"] = [
                v.as_request()[1] for v in self.webhooks
            ]

        return listRegistryWebhooks_query, listRegistryWebhooks_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListRegistryWebhooks":
        return cls(
            next_page_token=d.get("next_page_token", None),
            webhooks=[RegistryWebhook.from_dict(v) for v in d["webhooks"]]
            if "webhooks" in d
            else None,
        )


@dataclass
class ListRegistryWebhooksRequest:
    """List registry webhooks"""

    # If `events` is specified, any webhook with one or more of the specified
    # trigger events is included in the output. If `events` is not specified,
    # webhooks of all event types are included in the output.
    events: "List[RegistryWebhookEvent]"  # query
    # If not specified, all webhooks associated with the specified events are
    # listed, regardless of their associated model.
    model_name: str  # query
    # Token indicating the page of artifact results to fetch
    page_token: str  # query

    def as_request(self) -> (dict, dict):
        listRegistryWebhooksRequest_query, listRegistryWebhooksRequest_body = {}, {}
        if self.events:
            listRegistryWebhooksRequest_query["events"] = [v for v in self.events]
        if self.model_name:
            listRegistryWebhooksRequest_query["model_name"] = self.model_name
        if self.page_token:
            listRegistryWebhooksRequest_query["page_token"] = self.page_token

        return listRegistryWebhooksRequest_query, listRegistryWebhooksRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListRegistryWebhooksRequest":
        return cls(
            events=d.get("events", None),
            model_name=d.get("model_name", None),
            page_token=d.get("page_token", None),
        )


@dataclass
class ListResponse:

    # Array of open transition requests.
    requests: "List[Activity]"

    def as_request(self) -> (dict, dict):
        listResponse_query, listResponse_body = {}, {}
        if self.requests:
            listResponse_body["requests"] = [v.as_request()[1] for v in self.requests]

        return listResponse_query, listResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListResponse":
        return cls(
            requests=[Activity.from_dict(v) for v in d["requests"]]
            if "requests" in d
            else None,
        )


@dataclass
class ListTransitionRequestsRequest:
    """List transition requests"""

    # Name of the model.
    name: str  # query
    # Version of the model.
    version: str  # query

    def as_request(self) -> (dict, dict):
        listTransitionRequestsRequest_query, listTransitionRequestsRequest_body = {}, {}
        if self.name:
            listTransitionRequestsRequest_query["name"] = self.name
        if self.version:
            listTransitionRequestsRequest_query["version"] = self.version

        return listTransitionRequestsRequest_query, listTransitionRequestsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListTransitionRequestsRequest":
        return cls(
            name=d.get("name", None),
            version=d.get("version", None),
        )


@dataclass
class LogBatch:

    # Metrics to log. A single request can contain up to 1000 metrics, and up to
    # 1000 metrics, params, and tags in total.
    metrics: "List[Metric]"
    # Params to log. A single request can contain up to 100 params, and up to
    # 1000 metrics, params, and tags in total.
    params: "List[Param]"
    # ID of the run to log under
    run_id: str
    # Tags to log. A single request can contain up to 100 tags, and up to 1000
    # metrics, params, and tags in total.
    tags: "List[RunTag]"

    def as_request(self) -> (dict, dict):
        logBatch_query, logBatch_body = {}, {}
        if self.metrics:
            logBatch_body["metrics"] = [v.as_request()[1] for v in self.metrics]
        if self.params:
            logBatch_body["params"] = [v.as_request()[1] for v in self.params]
        if self.run_id:
            logBatch_body["run_id"] = self.run_id
        if self.tags:
            logBatch_body["tags"] = [v.as_request()[1] for v in self.tags]

        return logBatch_query, logBatch_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "LogBatch":
        return cls(
            metrics=[Metric.from_dict(v) for v in d["metrics"]]
            if "metrics" in d
            else None,
            params=[Param.from_dict(v) for v in d["params"]] if "params" in d else None,
            run_id=d.get("run_id", None),
            tags=[RunTag.from_dict(v) for v in d["tags"]] if "tags" in d else None,
        )


@dataclass
class LogMetric:

    # Name of the metric.
    key: str
    # ID of the run under which to log the metric. Must be provided.
    run_id: str
    # [Deprecated, use run_id instead] ID of the run under which to log the
    # metric. This field will be removed in a future MLflow version.
    run_uuid: str
    # Step at which to log the metric
    step: int
    # Unix timestamp in milliseconds at the time metric was logged.
    timestamp: int
    # Double value of the metric being logged.
    value: float

    def as_request(self) -> (dict, dict):
        logMetric_query, logMetric_body = {}, {}
        if self.key:
            logMetric_body["key"] = self.key
        if self.run_id:
            logMetric_body["run_id"] = self.run_id
        if self.run_uuid:
            logMetric_body["run_uuid"] = self.run_uuid
        if self.step:
            logMetric_body["step"] = self.step
        if self.timestamp:
            logMetric_body["timestamp"] = self.timestamp
        if self.value:
            logMetric_body["value"] = self.value

        return logMetric_query, logMetric_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "LogMetric":
        return cls(
            key=d.get("key", None),
            run_id=d.get("run_id", None),
            run_uuid=d.get("run_uuid", None),
            step=d.get("step", None),
            timestamp=d.get("timestamp", None),
            value=d.get("value", None),
        )


@dataclass
class LogModel:

    # MLmodel file in json format.
    model_json: str
    # ID of the run to log under
    run_id: str

    def as_request(self) -> (dict, dict):
        logModel_query, logModel_body = {}, {}
        if self.model_json:
            logModel_body["model_json"] = self.model_json
        if self.run_id:
            logModel_body["run_id"] = self.run_id

        return logModel_query, logModel_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "LogModel":
        return cls(
            model_json=d.get("model_json", None),
            run_id=d.get("run_id", None),
        )


@dataclass
class LogParam:

    # Name of the param. Maximum size is 255 bytes.
    key: str
    # ID of the run under which to log the param. Must be provided.
    run_id: str
    # [Deprecated, use run_id instead] ID of the run under which to log the
    # param. This field will be removed in a future MLflow version.
    run_uuid: str
    # String value of the param being logged. Maximum size is 500 bytes.
    value: str

    def as_request(self) -> (dict, dict):
        logParam_query, logParam_body = {}, {}
        if self.key:
            logParam_body["key"] = self.key
        if self.run_id:
            logParam_body["run_id"] = self.run_id
        if self.run_uuid:
            logParam_body["run_uuid"] = self.run_uuid
        if self.value:
            logParam_body["value"] = self.value

        return logParam_query, logParam_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "LogParam":
        return cls(
            key=d.get("key", None),
            run_id=d.get("run_id", None),
            run_uuid=d.get("run_uuid", None),
            value=d.get("value", None),
        )


@dataclass
class Metric:

    # Key identifying this metric.
    key: str
    # Step at which to log the metric.
    step: int
    # The timestamp at which this metric was recorded.
    timestamp: int
    # Value associated with this metric.
    value: float

    def as_request(self) -> (dict, dict):
        metric_query, metric_body = {}, {}
        if self.key:
            metric_body["key"] = self.key
        if self.step:
            metric_body["step"] = self.step
        if self.timestamp:
            metric_body["timestamp"] = self.timestamp
        if self.value:
            metric_body["value"] = self.value

        return metric_query, metric_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Metric":
        return cls(
            key=d.get("key", None),
            step=d.get("step", None),
            timestamp=d.get("timestamp", None),
            value=d.get("value", None),
        )


@dataclass
class ModelVersion:

    # Timestamp recorded when this `model_version` was created.
    creation_timestamp: int
    # Current stage for this `model_version`.
    current_stage: str
    # Description of this `model_version`.
    description: str
    # Timestamp recorded when metadata for this `model_version` was last
    # updated.
    last_updated_timestamp: int
    # Unique name of the model
    name: str
    # MLflow run ID used when creating `model_version`, if `source` was
    # generated by an experiment run stored in MLflow tracking server.
    run_id: str
    # Run Link: Direct link to the run that generated this version
    run_link: str
    # URI indicating the location of the source model artifacts, used when
    # creating `model_version`
    source: str
    # Current status of `model_version`
    status: "ModelVersionStatus"
    # Details on current `status`, if it is pending or failed.
    status_message: str
    # Tags: Additional metadata key-value pairs for this `model_version`.
    tags: "List[ModelVersionTag]"
    # User that created this `model_version`.
    user_id: str
    # Model's version number.
    version: str

    def as_request(self) -> (dict, dict):
        modelVersion_query, modelVersion_body = {}, {}
        if self.creation_timestamp:
            modelVersion_body["creation_timestamp"] = self.creation_timestamp
        if self.current_stage:
            modelVersion_body["current_stage"] = self.current_stage
        if self.description:
            modelVersion_body["description"] = self.description
        if self.last_updated_timestamp:
            modelVersion_body["last_updated_timestamp"] = self.last_updated_timestamp
        if self.name:
            modelVersion_body["name"] = self.name
        if self.run_id:
            modelVersion_body["run_id"] = self.run_id
        if self.run_link:
            modelVersion_body["run_link"] = self.run_link
        if self.source:
            modelVersion_body["source"] = self.source
        if self.status:
            modelVersion_body["status"] = self.status.value
        if self.status_message:
            modelVersion_body["status_message"] = self.status_message
        if self.tags:
            modelVersion_body["tags"] = [v.as_request()[1] for v in self.tags]
        if self.user_id:
            modelVersion_body["user_id"] = self.user_id
        if self.version:
            modelVersion_body["version"] = self.version

        return modelVersion_query, modelVersion_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ModelVersion":
        return cls(
            creation_timestamp=d.get("creation_timestamp", None),
            current_stage=d.get("current_stage", None),
            description=d.get("description", None),
            last_updated_timestamp=d.get("last_updated_timestamp", None),
            name=d.get("name", None),
            run_id=d.get("run_id", None),
            run_link=d.get("run_link", None),
            source=d.get("source", None),
            status=ModelVersionStatus(d["status"]) if "status" in d else None,
            status_message=d.get("status_message", None),
            tags=[ModelVersionTag.from_dict(v) for v in d["tags"]]
            if "tags" in d
            else None,
            user_id=d.get("user_id", None),
            version=d.get("version", None),
        )


@dataclass
class ModelVersionDatabricks:

    # Creation time of the object, as a Unix timestamp in milliseconds.
    creation_timestamp: int
    # This describes an enum
    current_stage: "Stage"
    # User-specified description for the object.
    description: str
    # Time of the object at last update, as a Unix timestamp in milliseconds.
    last_updated_timestamp: int
    # Name of the model.
    name: str
    # Permission level of the requesting user on the object. For what is allowed
    # at each level, see [MLflow Model permissions](..).
    permission_level: "PermissionLevel"
    # Unique identifier for the MLflow tracking run associated with the source
    # model artifacts.
    run_id: str
    # URL of the run associated with the model artifacts. This field is set at
    # model version creation time only for model versions whose source run is
    # from a tracking server that is different from the registry server.
    run_link: str
    # URI that indicates the location of the source model artifacts. This is
    # used when creating the model version.
    source: str
    # This describes an enum
    status: "Status"
    # Details on the current status, for example why registration failed.
    status_message: str
    # Array of tags that are associated with the model version.
    tags: "List[ModelVersionTag]"
    # The username of the user that created the object.
    user_id: str
    # Version of the model.
    version: str

    def as_request(self) -> (dict, dict):
        modelVersionDatabricks_query, modelVersionDatabricks_body = {}, {}
        if self.creation_timestamp:
            modelVersionDatabricks_body["creation_timestamp"] = self.creation_timestamp
        if self.current_stage:
            modelVersionDatabricks_body["current_stage"] = self.current_stage.value
        if self.description:
            modelVersionDatabricks_body["description"] = self.description
        if self.last_updated_timestamp:
            modelVersionDatabricks_body[
                "last_updated_timestamp"
            ] = self.last_updated_timestamp
        if self.name:
            modelVersionDatabricks_body["name"] = self.name
        if self.permission_level:
            modelVersionDatabricks_body[
                "permission_level"
            ] = self.permission_level.value
        if self.run_id:
            modelVersionDatabricks_body["run_id"] = self.run_id
        if self.run_link:
            modelVersionDatabricks_body["run_link"] = self.run_link
        if self.source:
            modelVersionDatabricks_body["source"] = self.source
        if self.status:
            modelVersionDatabricks_body["status"] = self.status.value
        if self.status_message:
            modelVersionDatabricks_body["status_message"] = self.status_message
        if self.tags:
            modelVersionDatabricks_body["tags"] = [v.as_request()[1] for v in self.tags]
        if self.user_id:
            modelVersionDatabricks_body["user_id"] = self.user_id
        if self.version:
            modelVersionDatabricks_body["version"] = self.version

        return modelVersionDatabricks_query, modelVersionDatabricks_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ModelVersionDatabricks":
        return cls(
            creation_timestamp=d.get("creation_timestamp", None),
            current_stage=Stage(d["current_stage"]) if "current_stage" in d else None,
            description=d.get("description", None),
            last_updated_timestamp=d.get("last_updated_timestamp", None),
            name=d.get("name", None),
            permission_level=PermissionLevel(d["permission_level"])
            if "permission_level" in d
            else None,
            run_id=d.get("run_id", None),
            run_link=d.get("run_link", None),
            source=d.get("source", None),
            status=Status(d["status"]) if "status" in d else None,
            status_message=d.get("status_message", None),
            tags=[ModelVersionTag.from_dict(v) for v in d["tags"]]
            if "tags" in d
            else None,
            user_id=d.get("user_id", None),
            version=d.get("version", None),
        )


class ModelVersionStatus(Enum):
    """Current status of `model_version`"""

    FAILED_REGISTRATION = "FAILED_REGISTRATION"
    PENDING_REGISTRATION = "PENDING_REGISTRATION"
    READY = "READY"


@dataclass
class ModelVersionTag:

    # The tag key.
    key: str
    # The tag value.
    value: str

    def as_request(self) -> (dict, dict):
        modelVersionTag_query, modelVersionTag_body = {}, {}
        if self.key:
            modelVersionTag_body["key"] = self.key
        if self.value:
            modelVersionTag_body["value"] = self.value

        return modelVersionTag_query, modelVersionTag_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ModelVersionTag":
        return cls(
            key=d.get("key", None),
            value=d.get("value", None),
        )


@dataclass
class Param:

    # Key identifying this param.
    key: str
    # Value associated with this param.
    value: str

    def as_request(self) -> (dict, dict):
        param_query, param_body = {}, {}
        if self.key:
            param_body["key"] = self.key
        if self.value:
            param_body["value"] = self.value

        return param_query, param_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Param":
        return cls(
            key=d.get("key", None),
            value=d.get("value", None),
        )


class PermissionLevel(Enum):
    """Permission level of the requesting user on the object. For what is allowed
    at each level, see [MLflow Model permissions](..)."""

    CAN_EDIT = "CAN_EDIT"
    CAN_MANAGE = "CAN_MANAGE"
    CAN_MANAGE_PRODUCTION_VERSIONS = "CAN_MANAGE_PRODUCTION_VERSIONS"
    CAN_MANAGE_STAGING_VERSIONS = "CAN_MANAGE_STAGING_VERSIONS"
    CAN_READ = "CAN_READ"


@dataclass
class RegisteredModel:

    # Timestamp recorded when this `registered_model` was created.
    creation_timestamp: int
    # Description of this `registered_model`.
    description: str
    # Timestamp recorded when metadata for this `registered_model` was last
    # updated.
    last_updated_timestamp: int
    # Collection of latest model versions for each stage. Only contains models
    # with current `READY` status.
    latest_versions: "List[ModelVersion]"
    # Unique name for the model.
    name: str
    # Tags: Additional metadata key-value pairs for this `registered_model`.
    tags: "List[RegisteredModelTag]"
    # User that created this `registered_model`
    user_id: str

    def as_request(self) -> (dict, dict):
        registeredModel_query, registeredModel_body = {}, {}
        if self.creation_timestamp:
            registeredModel_body["creation_timestamp"] = self.creation_timestamp
        if self.description:
            registeredModel_body["description"] = self.description
        if self.last_updated_timestamp:
            registeredModel_body["last_updated_timestamp"] = self.last_updated_timestamp
        if self.latest_versions:
            registeredModel_body["latest_versions"] = [
                v.as_request()[1] for v in self.latest_versions
            ]
        if self.name:
            registeredModel_body["name"] = self.name
        if self.tags:
            registeredModel_body["tags"] = [v.as_request()[1] for v in self.tags]
        if self.user_id:
            registeredModel_body["user_id"] = self.user_id

        return registeredModel_query, registeredModel_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RegisteredModel":
        return cls(
            creation_timestamp=d.get("creation_timestamp", None),
            description=d.get("description", None),
            last_updated_timestamp=d.get("last_updated_timestamp", None),
            latest_versions=[ModelVersion.from_dict(v) for v in d["latest_versions"]]
            if "latest_versions" in d
            else None,
            name=d.get("name", None),
            tags=[RegisteredModelTag.from_dict(v) for v in d["tags"]]
            if "tags" in d
            else None,
            user_id=d.get("user_id", None),
        )


@dataclass
class RegisteredModelDatabricks:

    # Creation time of the object, as a Unix timestamp in milliseconds.
    creation_timestamp: int
    # User-specified description for the object.
    description: str
    # Unique identifier for the object.
    id: str
    # Time of the object at last update, as a Unix timestamp in milliseconds.
    last_updated_timestamp: int
    # Array of model versions, each the latest version for its stage.
    latest_versions: "List[ModelVersion]"
    # Name of the model.
    name: str
    # Permission level of the requesting user on the object. For what is allowed
    # at each level, see [MLflow Model permissions](..).
    permission_level: "PermissionLevel"
    # Array of tags associated with the model.
    tags: "List[RegisteredModelTag]"
    # The username of the user that created the object.
    user_id: str

    def as_request(self) -> (dict, dict):
        registeredModelDatabricks_query, registeredModelDatabricks_body = {}, {}
        if self.creation_timestamp:
            registeredModelDatabricks_body[
                "creation_timestamp"
            ] = self.creation_timestamp
        if self.description:
            registeredModelDatabricks_body["description"] = self.description
        if self.id:
            registeredModelDatabricks_body["id"] = self.id
        if self.last_updated_timestamp:
            registeredModelDatabricks_body[
                "last_updated_timestamp"
            ] = self.last_updated_timestamp
        if self.latest_versions:
            registeredModelDatabricks_body["latest_versions"] = [
                v.as_request()[1] for v in self.latest_versions
            ]
        if self.name:
            registeredModelDatabricks_body["name"] = self.name
        if self.permission_level:
            registeredModelDatabricks_body[
                "permission_level"
            ] = self.permission_level.value
        if self.tags:
            registeredModelDatabricks_body["tags"] = [
                v.as_request()[1] for v in self.tags
            ]
        if self.user_id:
            registeredModelDatabricks_body["user_id"] = self.user_id

        return registeredModelDatabricks_query, registeredModelDatabricks_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RegisteredModelDatabricks":
        return cls(
            creation_timestamp=d.get("creation_timestamp", None),
            description=d.get("description", None),
            id=d.get("id", None),
            last_updated_timestamp=d.get("last_updated_timestamp", None),
            latest_versions=[ModelVersion.from_dict(v) for v in d["latest_versions"]]
            if "latest_versions" in d
            else None,
            name=d.get("name", None),
            permission_level=PermissionLevel(d["permission_level"])
            if "permission_level" in d
            else None,
            tags=[RegisteredModelTag.from_dict(v) for v in d["tags"]]
            if "tags" in d
            else None,
            user_id=d.get("user_id", None),
        )


@dataclass
class RegisteredModelTag:

    # The tag key.
    key: str
    # The tag value.
    value: str

    def as_request(self) -> (dict, dict):
        registeredModelTag_query, registeredModelTag_body = {}, {}
        if self.key:
            registeredModelTag_body["key"] = self.key
        if self.value:
            registeredModelTag_body["value"] = self.value

        return registeredModelTag_query, registeredModelTag_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RegisteredModelTag":
        return cls(
            key=d.get("key", None),
            value=d.get("value", None),
        )


@dataclass
class RegistryWebhook:

    # Creation time of the object, as a Unix timestamp in milliseconds.
    creation_timestamp: int
    # User-specified description for the webhook.
    description: str
    # Events that can trigger a registry webhook: * `MODEL_VERSION_CREATED`: A
    # new model version was created for the associated model.
    #
    # * `MODEL_VERSION_TRANSITIONED_STAGE`: A model version’s stage was
    # changed.
    #
    # * `TRANSITION_REQUEST_CREATED`: A user requested a model version’s stage
    # be transitioned.
    #
    # * `COMMENT_CREATED`: A user wrote a comment on a registered model.
    #
    # * `REGISTERED_MODEL_CREATED`: A new registered model was created. This
    # event type can only be specified for a registry-wide webhook, which can be
    # created by not specifying a model name in the create request.
    #
    # * `MODEL_VERSION_TAG_SET`: A user set a tag on the model version.
    #
    # * `MODEL_VERSION_TRANSITIONED_TO_STAGING`: A model version was
    # transitioned to staging.
    #
    # * `MODEL_VERSION_TRANSITIONED_TO_PRODUCTION`: A model version was
    # transitioned to production.
    #
    # * `MODEL_VERSION_TRANSITIONED_TO_ARCHIVED`: A model version was archived.
    #
    # * `TRANSITION_REQUEST_TO_STAGING_CREATED`: A user requested a model
    # version be transitioned to staging.
    #
    # * `TRANSITION_REQUEST_TO_PRODUCTION_CREATED`: A user requested a model
    # version be transitioned to production.
    #
    # * `TRANSITION_REQUEST_TO_ARCHIVED_CREATED`: A user requested a model
    # version be archived.
    events: "List[RegistryWebhookEvent]"

    http_url_spec: "HttpUrlSpecWithoutSecret"
    # Webhook ID
    id: str

    job_spec: "JobSpecWithoutSecret"
    # Time of the object at last update, as a Unix timestamp in milliseconds.
    last_updated_timestamp: int
    # Name of the model whose events would trigger this webhook.
    model_name: str
    # This describes an enum
    status: "RegistryWebhookStatus"

    def as_request(self) -> (dict, dict):
        registryWebhook_query, registryWebhook_body = {}, {}
        if self.creation_timestamp:
            registryWebhook_body["creation_timestamp"] = self.creation_timestamp
        if self.description:
            registryWebhook_body["description"] = self.description
        if self.events:
            registryWebhook_body["events"] = [v for v in self.events]
        if self.http_url_spec:
            registryWebhook_body["http_url_spec"] = self.http_url_spec.as_request()[1]
        if self.id:
            registryWebhook_body["id"] = self.id
        if self.job_spec:
            registryWebhook_body["job_spec"] = self.job_spec.as_request()[1]
        if self.last_updated_timestamp:
            registryWebhook_body["last_updated_timestamp"] = self.last_updated_timestamp
        if self.model_name:
            registryWebhook_body["model_name"] = self.model_name
        if self.status:
            registryWebhook_body["status"] = self.status.value

        return registryWebhook_query, registryWebhook_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RegistryWebhook":
        return cls(
            creation_timestamp=d.get("creation_timestamp", None),
            description=d.get("description", None),
            events=d.get("events", None),
            http_url_spec=HttpUrlSpecWithoutSecret.from_dict(d["http_url_spec"])
            if "http_url_spec" in d
            else None,
            id=d.get("id", None),
            job_spec=JobSpecWithoutSecret.from_dict(d["job_spec"])
            if "job_spec" in d
            else None,
            last_updated_timestamp=d.get("last_updated_timestamp", None),
            model_name=d.get("model_name", None),
            status=RegistryWebhookStatus(d["status"]) if "status" in d else None,
        )


class RegistryWebhookEvent(Enum):

    COMMENT_CREATED = "COMMENT_CREATED"
    MODEL_VERSION_CREATED = "MODEL_VERSION_CREATED"
    MODEL_VERSION_TAG_SET = "MODEL_VERSION_TAG_SET"
    MODEL_VERSION_TRANSITIONED_STAGE = "MODEL_VERSION_TRANSITIONED_STAGE"
    MODEL_VERSION_TRANSITIONED_TO_ARCHIVED = "MODEL_VERSION_TRANSITIONED_TO_ARCHIVED"
    MODEL_VERSION_TRANSITIONED_TO_PRODUCTION = (
        "MODEL_VERSION_TRANSITIONED_TO_PRODUCTION"
    )
    MODEL_VERSION_TRANSITIONED_TO_STAGING = "MODEL_VERSION_TRANSITIONED_TO_STAGING"
    REGISTERED_MODEL_CREATED = "REGISTERED_MODEL_CREATED"
    TRANSITION_REQUEST_CREATED = "TRANSITION_REQUEST_CREATED"
    TRANSITION_REQUEST_TO_ARCHIVED_CREATED = "TRANSITION_REQUEST_TO_ARCHIVED_CREATED"
    TRANSITION_REQUEST_TO_PRODUCTION_CREATED = (
        "TRANSITION_REQUEST_TO_PRODUCTION_CREATED"
    )
    TRANSITION_REQUEST_TO_STAGING_CREATED = "TRANSITION_REQUEST_TO_STAGING_CREATED"


class RegistryWebhookStatus(Enum):
    """This describes an enum"""

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    TEST_MODE = "TEST_MODE"


@dataclass
class RejectResponse:

    # Activity recorded for the action.
    activity: "Activity"

    def as_request(self) -> (dict, dict):
        rejectResponse_query, rejectResponse_body = {}, {}
        if self.activity:
            rejectResponse_body["activity"] = self.activity.as_request()[1]

        return rejectResponse_query, rejectResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RejectResponse":
        return cls(
            activity=Activity.from_dict(d["activity"]) if "activity" in d else None,
        )


@dataclass
class RejectTransitionRequest:

    # User-provided comment on the action.
    comment: str
    # Name of the model.
    name: str
    # Target stage of the transition. Valid values are:
    #
    # * `None`: The initial stage of a model version.
    #
    # * `Staging`: Staging or pre-production stage.
    #
    # * `Production`: Production stage.
    #
    # * `Archived`: Archived stage.
    stage: "Stage"
    # Version of the model.
    version: str

    def as_request(self) -> (dict, dict):
        rejectTransitionRequest_query, rejectTransitionRequest_body = {}, {}
        if self.comment:
            rejectTransitionRequest_body["comment"] = self.comment
        if self.name:
            rejectTransitionRequest_body["name"] = self.name
        if self.stage:
            rejectTransitionRequest_body["stage"] = self.stage.value
        if self.version:
            rejectTransitionRequest_body["version"] = self.version

        return rejectTransitionRequest_query, rejectTransitionRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RejectTransitionRequest":
        return cls(
            comment=d.get("comment", None),
            name=d.get("name", None),
            stage=Stage(d["stage"]) if "stage" in d else None,
            version=d.get("version", None),
        )


@dataclass
class RenameRegisteredModelRequest:

    # Registered model unique name identifier.
    name: str
    # If provided, updates the name for this `registered_model`.
    new_name: str

    def as_request(self) -> (dict, dict):
        renameRegisteredModelRequest_query, renameRegisteredModelRequest_body = {}, {}
        if self.name:
            renameRegisteredModelRequest_body["name"] = self.name
        if self.new_name:
            renameRegisteredModelRequest_body["new_name"] = self.new_name

        return renameRegisteredModelRequest_query, renameRegisteredModelRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RenameRegisteredModelRequest":
        return cls(
            name=d.get("name", None),
            new_name=d.get("new_name", None),
        )


@dataclass
class RenameRegisteredModelResponse:

    registered_model: "RegisteredModel"

    def as_request(self) -> (dict, dict):
        renameRegisteredModelResponse_query, renameRegisteredModelResponse_body = {}, {}
        if self.registered_model:
            renameRegisteredModelResponse_body[
                "registered_model"
            ] = self.registered_model.as_request()[1]

        return renameRegisteredModelResponse_query, renameRegisteredModelResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RenameRegisteredModelResponse":
        return cls(
            registered_model=RegisteredModel.from_dict(d["registered_model"])
            if "registered_model" in d
            else None,
        )


@dataclass
class RestoreExperiment:

    # ID of the associated experiment.
    experiment_id: str

    def as_request(self) -> (dict, dict):
        restoreExperiment_query, restoreExperiment_body = {}, {}
        if self.experiment_id:
            restoreExperiment_body["experiment_id"] = self.experiment_id

        return restoreExperiment_query, restoreExperiment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RestoreExperiment":
        return cls(
            experiment_id=d.get("experiment_id", None),
        )


@dataclass
class RestoreRun:

    # ID of the run to restore.
    run_id: str

    def as_request(self) -> (dict, dict):
        restoreRun_query, restoreRun_body = {}, {}
        if self.run_id:
            restoreRun_body["run_id"] = self.run_id

        return restoreRun_query, restoreRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RestoreRun":
        return cls(
            run_id=d.get("run_id", None),
        )


@dataclass
class Run:

    # Run data.
    data: "RunData"
    # Run metadata.
    info: "RunInfo"

    def as_request(self) -> (dict, dict):
        run_query, run_body = {}, {}
        if self.data:
            run_body["data"] = self.data.as_request()[1]
        if self.info:
            run_body["info"] = self.info.as_request()[1]

        return run_query, run_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Run":
        return cls(
            data=RunData.from_dict(d["data"]) if "data" in d else None,
            info=RunInfo.from_dict(d["info"]) if "info" in d else None,
        )


@dataclass
class RunData:

    # Run metrics.
    metrics: "List[Metric]"
    # Run parameters.
    params: "List[Param]"
    # Additional metadata key-value pairs.
    tags: "List[RunTag]"

    def as_request(self) -> (dict, dict):
        runData_query, runData_body = {}, {}
        if self.metrics:
            runData_body["metrics"] = [v.as_request()[1] for v in self.metrics]
        if self.params:
            runData_body["params"] = [v.as_request()[1] for v in self.params]
        if self.tags:
            runData_body["tags"] = [v.as_request()[1] for v in self.tags]

        return runData_query, runData_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RunData":
        return cls(
            metrics=[Metric.from_dict(v) for v in d["metrics"]]
            if "metrics" in d
            else None,
            params=[Param.from_dict(v) for v in d["params"]] if "params" in d else None,
            tags=[RunTag.from_dict(v) for v in d["tags"]] if "tags" in d else None,
        )


@dataclass
class RunInfo:

    # URI of the directory where artifacts should be uploaded. This can be a
    # local path (starting with "/"), or a distributed file system (DFS) path,
    # like `s3://bucket/directory` or `dbfs:/my/directory`. If not set, the
    # local `./mlruns` directory is chosen.
    artifact_uri: str
    # Unix timestamp of when the run ended in milliseconds.
    end_time: int
    # The experiment ID.
    experiment_id: str
    # Current life cycle stage of the experiment : OneOf("active", "deleted")
    lifecycle_stage: str
    # Unique identifier for the run.
    run_id: str
    # [Deprecated, use run_id instead] Unique identifier for the run. This field
    # will be removed in a future MLflow version.
    run_uuid: str
    # Unix timestamp of when the run started in milliseconds.
    start_time: int
    # Current status of the run.
    status: "RunInfoStatus"
    # User who initiated the run. This field is deprecated as of MLflow 1.0, and
    # will be removed in a future MLflow release. Use 'mlflow.user' tag instead.
    user_id: str

    def as_request(self) -> (dict, dict):
        runInfo_query, runInfo_body = {}, {}
        if self.artifact_uri:
            runInfo_body["artifact_uri"] = self.artifact_uri
        if self.end_time:
            runInfo_body["end_time"] = self.end_time
        if self.experiment_id:
            runInfo_body["experiment_id"] = self.experiment_id
        if self.lifecycle_stage:
            runInfo_body["lifecycle_stage"] = self.lifecycle_stage
        if self.run_id:
            runInfo_body["run_id"] = self.run_id
        if self.run_uuid:
            runInfo_body["run_uuid"] = self.run_uuid
        if self.start_time:
            runInfo_body["start_time"] = self.start_time
        if self.status:
            runInfo_body["status"] = self.status.value
        if self.user_id:
            runInfo_body["user_id"] = self.user_id

        return runInfo_query, runInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RunInfo":
        return cls(
            artifact_uri=d.get("artifact_uri", None),
            end_time=d.get("end_time", None),
            experiment_id=d.get("experiment_id", None),
            lifecycle_stage=d.get("lifecycle_stage", None),
            run_id=d.get("run_id", None),
            run_uuid=d.get("run_uuid", None),
            start_time=d.get("start_time", None),
            status=RunInfoStatus(d["status"]) if "status" in d else None,
            user_id=d.get("user_id", None),
        )


class RunInfoStatus(Enum):
    """Current status of the run."""

    FAILED = "FAILED"
    FINISHED = "FINISHED"
    KILLED = "KILLED"
    RUNNING = "RUNNING"
    SCHEDULED = "SCHEDULED"


@dataclass
class RunTag:

    # The tag key.
    key: str
    # The tag value.
    value: str

    def as_request(self) -> (dict, dict):
        runTag_query, runTag_body = {}, {}
        if self.key:
            runTag_body["key"] = self.key
        if self.value:
            runTag_body["value"] = self.value

        return runTag_query, runTag_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RunTag":
        return cls(
            key=d.get("key", None),
            value=d.get("value", None),
        )


@dataclass
class SearchExperiments:

    # String representing a SQL filter condition (e.g. "name ILIKE
    # 'my-experiment%'")
    filter: str
    # Maximum number of experiments desired. Max threshold is 3000.
    max_results: int
    # List of columns for ordering search results, which can include experiment
    # name and last updated timestamp with an optional "DESC" or "ASC"
    # annotation, where "ASC" is the default. Tiebreaks are done by experiment
    # id DESC.
    order_by: "List[str]"
    # Token indicating the page of experiments to fetch
    page_token: str
    # Qualifier for type of experiments to be returned. If unspecified, return
    # only active experiments.
    view_type: "SearchExperimentsViewType"

    def as_request(self) -> (dict, dict):
        searchExperiments_query, searchExperiments_body = {}, {}
        if self.filter:
            searchExperiments_body["filter"] = self.filter
        if self.max_results:
            searchExperiments_body["max_results"] = self.max_results
        if self.order_by:
            searchExperiments_body["order_by"] = [v for v in self.order_by]
        if self.page_token:
            searchExperiments_body["page_token"] = self.page_token
        if self.view_type:
            searchExperiments_body["view_type"] = self.view_type.value

        return searchExperiments_query, searchExperiments_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SearchExperiments":
        return cls(
            filter=d.get("filter", None),
            max_results=d.get("max_results", None),
            order_by=d.get("order_by", None),
            page_token=d.get("page_token", None),
            view_type=SearchExperimentsViewType(d["view_type"])
            if "view_type" in d
            else None,
        )


@dataclass
class SearchExperimentsResponse:

    # Experiments that match the search criteria
    experiments: "List[Experiment]"
    # Token that can be used to retrieve the next page of experiments. An empty
    # token means that no more experiments are available for retrieval.
    next_page_token: str

    def as_request(self) -> (dict, dict):
        searchExperimentsResponse_query, searchExperimentsResponse_body = {}, {}
        if self.experiments:
            searchExperimentsResponse_body["experiments"] = [
                v.as_request()[1] for v in self.experiments
            ]
        if self.next_page_token:
            searchExperimentsResponse_body["next_page_token"] = self.next_page_token

        return searchExperimentsResponse_query, searchExperimentsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SearchExperimentsResponse":
        return cls(
            experiments=[Experiment.from_dict(v) for v in d["experiments"]]
            if "experiments" in d
            else None,
            next_page_token=d.get("next_page_token", None),
        )


class SearchExperimentsViewType(Enum):
    """Qualifier for type of experiments to be returned. If unspecified, return
    only active experiments."""

    ACTIVE_ONLY = "ACTIVE_ONLY"
    ALL = "ALL"
    DELETED_ONLY = "DELETED_ONLY"


@dataclass
class SearchModelVersionsRequest:
    """Searches model versions"""

    # String filter condition, like "name='my-model-name'". Must be a single
    # boolean condition, with string values wrapped in single quotes.
    filter: str  # query
    # Maximum number of models desired. Max threshold is 10K.
    max_results: int  # query
    # List of columns to be ordered by including model name, version, stage with
    # an optional "DESC" or "ASC" annotation, where "ASC" is the default.
    # Tiebreaks are done by latest stage transition timestamp, followed by name
    # ASC, followed by version DESC.
    order_by: "List[str]"  # query
    # Pagination token to go to next page based on previous search query.
    page_token: str  # query

    def as_request(self) -> (dict, dict):
        searchModelVersionsRequest_query, searchModelVersionsRequest_body = {}, {}
        if self.filter:
            searchModelVersionsRequest_query["filter"] = self.filter
        if self.max_results:
            searchModelVersionsRequest_query["max_results"] = self.max_results
        if self.order_by:
            searchModelVersionsRequest_query["order_by"] = [v for v in self.order_by]
        if self.page_token:
            searchModelVersionsRequest_query["page_token"] = self.page_token

        return searchModelVersionsRequest_query, searchModelVersionsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SearchModelVersionsRequest":
        return cls(
            filter=d.get("filter", None),
            max_results=d.get("max_results", None),
            order_by=d.get("order_by", None),
            page_token=d.get("page_token", None),
        )


@dataclass
class SearchModelVersionsResponse:

    # Models that match the search criteria
    model_versions: "List[ModelVersion]"
    # Pagination token to request next page of models for the same search query.
    next_page_token: str

    def as_request(self) -> (dict, dict):
        searchModelVersionsResponse_query, searchModelVersionsResponse_body = {}, {}
        if self.model_versions:
            searchModelVersionsResponse_body["model_versions"] = [
                v.as_request()[1] for v in self.model_versions
            ]
        if self.next_page_token:
            searchModelVersionsResponse_body["next_page_token"] = self.next_page_token

        return searchModelVersionsResponse_query, searchModelVersionsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SearchModelVersionsResponse":
        return cls(
            model_versions=[ModelVersion.from_dict(v) for v in d["model_versions"]]
            if "model_versions" in d
            else None,
            next_page_token=d.get("next_page_token", None),
        )


@dataclass
class SearchRegisteredModelsRequest:
    """Search models"""

    # String filter condition, like "name LIKE 'my-model-name'". Interpreted in
    # the backend automatically as "name LIKE '%my-model-name%'". Single boolean
    # condition, with string values wrapped in single quotes.
    filter: str  # query
    # Maximum number of models desired. Default is 100. Max threshold is 1000.
    max_results: int  # query
    # List of columns for ordering search results, which can include model name
    # and last updated timestamp with an optional "DESC" or "ASC" annotation,
    # where "ASC" is the default. Tiebreaks are done by model name ASC.
    order_by: "List[str]"  # query
    # Pagination token to go to the next page based on a previous search query.
    page_token: str  # query

    def as_request(self) -> (dict, dict):
        searchRegisteredModelsRequest_query, searchRegisteredModelsRequest_body = {}, {}
        if self.filter:
            searchRegisteredModelsRequest_query["filter"] = self.filter
        if self.max_results:
            searchRegisteredModelsRequest_query["max_results"] = self.max_results
        if self.order_by:
            searchRegisteredModelsRequest_query["order_by"] = [v for v in self.order_by]
        if self.page_token:
            searchRegisteredModelsRequest_query["page_token"] = self.page_token

        return searchRegisteredModelsRequest_query, searchRegisteredModelsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SearchRegisteredModelsRequest":
        return cls(
            filter=d.get("filter", None),
            max_results=d.get("max_results", None),
            order_by=d.get("order_by", None),
            page_token=d.get("page_token", None),
        )


@dataclass
class SearchRegisteredModelsResponse:

    # Pagination token to request the next page of models.
    next_page_token: str
    # Registered Models that match the search criteria.
    registered_models: "List[RegisteredModel]"

    def as_request(self) -> (dict, dict):
        searchRegisteredModelsResponse_query, searchRegisteredModelsResponse_body = (
            {},
            {},
        )
        if self.next_page_token:
            searchRegisteredModelsResponse_body[
                "next_page_token"
            ] = self.next_page_token
        if self.registered_models:
            searchRegisteredModelsResponse_body["registered_models"] = [
                v.as_request()[1] for v in self.registered_models
            ]

        return searchRegisteredModelsResponse_query, searchRegisteredModelsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SearchRegisteredModelsResponse":
        return cls(
            next_page_token=d.get("next_page_token", None),
            registered_models=[
                RegisteredModel.from_dict(v) for v in d["registered_models"]
            ]
            if "registered_models" in d
            else None,
        )


@dataclass
class SearchRuns:

    # List of experiment IDs to search over.
    experiment_ids: "List[str]"
    # A filter expression over params, metrics, and tags, that allows returning
    # a subset of runs. The syntax is a subset of SQL that supports ANDing
    # together binary operations between a param, metric, or tag and a constant.
    #
    # Example: `metrics.rmse < 1 and params.model_class = 'LogisticRegression'`
    #
    # You can select columns with special characters (hyphen, space, period,
    # etc.) by using double quotes: `metrics."model class" = 'LinearRegression'
    # and tags."user-name" = 'Tomas'`
    #
    # Supported operators are `=`, `!=`, `>`, `>=`, `<`, and `<=`.
    filter: str
    # Maximum number of runs desired. Max threshold is 50000
    max_results: int
    # List of columns to be ordered by, including attributes, params, metrics,
    # and tags with an optional "DESC" or "ASC" annotation, where "ASC" is the
    # default. Example: ["params.input DESC", "metrics.alpha ASC",
    # "metrics.rmse"] Tiebreaks are done by start_time DESC followed by run_id
    # for runs with the same start time (and this is the default ordering
    # criterion if order_by is not provided).
    order_by: "List[str]"
    # Token for the current page of runs.
    page_token: str
    # Whether to display only active, only deleted, or all runs. Defaults to
    # only active runs.
    run_view_type: "SearchRunsRunViewType"

    def as_request(self) -> (dict, dict):
        searchRuns_query, searchRuns_body = {}, {}
        if self.experiment_ids:
            searchRuns_body["experiment_ids"] = [v for v in self.experiment_ids]
        if self.filter:
            searchRuns_body["filter"] = self.filter
        if self.max_results:
            searchRuns_body["max_results"] = self.max_results
        if self.order_by:
            searchRuns_body["order_by"] = [v for v in self.order_by]
        if self.page_token:
            searchRuns_body["page_token"] = self.page_token
        if self.run_view_type:
            searchRuns_body["run_view_type"] = self.run_view_type.value

        return searchRuns_query, searchRuns_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SearchRuns":
        return cls(
            experiment_ids=d.get("experiment_ids", None),
            filter=d.get("filter", None),
            max_results=d.get("max_results", None),
            order_by=d.get("order_by", None),
            page_token=d.get("page_token", None),
            run_view_type=SearchRunsRunViewType(d["run_view_type"])
            if "run_view_type" in d
            else None,
        )


@dataclass
class SearchRunsResponse:

    # Token for the next page of runs.
    next_page_token: str
    # Runs that match the search criteria.
    runs: "List[Run]"

    def as_request(self) -> (dict, dict):
        searchRunsResponse_query, searchRunsResponse_body = {}, {}
        if self.next_page_token:
            searchRunsResponse_body["next_page_token"] = self.next_page_token
        if self.runs:
            searchRunsResponse_body["runs"] = [v.as_request()[1] for v in self.runs]

        return searchRunsResponse_query, searchRunsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SearchRunsResponse":
        return cls(
            next_page_token=d.get("next_page_token", None),
            runs=[Run.from_dict(v) for v in d["runs"]] if "runs" in d else None,
        )


class SearchRunsRunViewType(Enum):
    """Whether to display only active, only deleted, or all runs. Defaults to only
    active runs."""

    ACTIVE_ONLY = "ACTIVE_ONLY"
    ALL = "ALL"
    DELETED_ONLY = "DELETED_ONLY"


@dataclass
class SetExperimentTag:

    # ID of the experiment under which to log the tag. Must be provided.
    experiment_id: str
    # Name of the tag. Maximum size depends on storage backend. All storage
    # backends are guaranteed to support key values up to 250 bytes in size.
    key: str
    # String value of the tag being logged. Maximum size depends on storage
    # backend. All storage backends are guaranteed to support key values up to
    # 5000 bytes in size.
    value: str

    def as_request(self) -> (dict, dict):
        setExperimentTag_query, setExperimentTag_body = {}, {}
        if self.experiment_id:
            setExperimentTag_body["experiment_id"] = self.experiment_id
        if self.key:
            setExperimentTag_body["key"] = self.key
        if self.value:
            setExperimentTag_body["value"] = self.value

        return setExperimentTag_query, setExperimentTag_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SetExperimentTag":
        return cls(
            experiment_id=d.get("experiment_id", None),
            key=d.get("key", None),
            value=d.get("value", None),
        )


@dataclass
class SetModelVersionTagRequest:

    # Name of the tag. Maximum size depends on storage backend. If a tag with
    # this name already exists, its preexisting value will be replaced by the
    # specified `value`. All storage backends are guaranteed to support key
    # values up to 250 bytes in size.
    key: str
    # Unique name of the model.
    name: str
    # String value of the tag being logged. Maximum size depends on storage
    # backend. All storage backends are guaranteed to support key values up to
    # 5000 bytes in size.
    value: str
    # Model version number.
    version: str

    def as_request(self) -> (dict, dict):
        setModelVersionTagRequest_query, setModelVersionTagRequest_body = {}, {}
        if self.key:
            setModelVersionTagRequest_body["key"] = self.key
        if self.name:
            setModelVersionTagRequest_body["name"] = self.name
        if self.value:
            setModelVersionTagRequest_body["value"] = self.value
        if self.version:
            setModelVersionTagRequest_body["version"] = self.version

        return setModelVersionTagRequest_query, setModelVersionTagRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SetModelVersionTagRequest":
        return cls(
            key=d.get("key", None),
            name=d.get("name", None),
            value=d.get("value", None),
            version=d.get("version", None),
        )


@dataclass
class SetRegisteredModelTagRequest:

    # Name of the tag. Maximum size depends on storage backend. If a tag with
    # this name already exists, its preexisting value will be replaced by the
    # specified `value`. All storage backends are guaranteed to support key
    # values up to 250 bytes in size.
    key: str
    # Unique name of the model.
    name: str
    # String value of the tag being logged. Maximum size depends on storage
    # backend. All storage backends are guaranteed to support key values up to
    # 5000 bytes in size.
    value: str

    def as_request(self) -> (dict, dict):
        setRegisteredModelTagRequest_query, setRegisteredModelTagRequest_body = {}, {}
        if self.key:
            setRegisteredModelTagRequest_body["key"] = self.key
        if self.name:
            setRegisteredModelTagRequest_body["name"] = self.name
        if self.value:
            setRegisteredModelTagRequest_body["value"] = self.value

        return setRegisteredModelTagRequest_query, setRegisteredModelTagRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SetRegisteredModelTagRequest":
        return cls(
            key=d.get("key", None),
            name=d.get("name", None),
            value=d.get("value", None),
        )


@dataclass
class SetTag:

    # Name of the tag. Maximum size depends on storage backend. All storage
    # backends are guaranteed to support key values up to 250 bytes in size.
    key: str
    # ID of the run under which to log the tag. Must be provided.
    run_id: str
    # [Deprecated, use run_id instead] ID of the run under which to log the tag.
    # This field will be removed in a future MLflow version.
    run_uuid: str
    # String value of the tag being logged. Maximum size depends on storage
    # backend. All storage backends are guaranteed to support key values up to
    # 5000 bytes in size.
    value: str

    def as_request(self) -> (dict, dict):
        setTag_query, setTag_body = {}, {}
        if self.key:
            setTag_body["key"] = self.key
        if self.run_id:
            setTag_body["run_id"] = self.run_id
        if self.run_uuid:
            setTag_body["run_uuid"] = self.run_uuid
        if self.value:
            setTag_body["value"] = self.value

        return setTag_query, setTag_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SetTag":
        return cls(
            key=d.get("key", None),
            run_id=d.get("run_id", None),
            run_uuid=d.get("run_uuid", None),
            value=d.get("value", None),
        )


class Stage(Enum):
    """This describes an enum"""

    Archived = "Archived"
    None_ = "None"
    Production = "Production"
    Staging = "Staging"


class Status(Enum):
    """This describes an enum"""

    FAILED_REGISTRATION = "FAILED_REGISTRATION"
    PENDING_REGISTRATION = "PENDING_REGISTRATION"
    READY = "READY"


@dataclass
class TestRegistryWebhook:
    """Test webhook response object."""

    # Body of the response from the webhook URL
    body: str
    # Status code returned by the webhook URL
    status_code: int

    def as_request(self) -> (dict, dict):
        testRegistryWebhook_query, testRegistryWebhook_body = {}, {}
        if self.body:
            testRegistryWebhook_body["body"] = self.body
        if self.status_code:
            testRegistryWebhook_body["status_code"] = self.status_code

        return testRegistryWebhook_query, testRegistryWebhook_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TestRegistryWebhook":
        return cls(
            body=d.get("body", None),
            status_code=d.get("status_code", None),
        )


@dataclass
class TestRegistryWebhookRequest:

    # If `event` is specified, the test trigger uses the specified event. If
    # `event` is not specified, the test trigger uses a randomly chosen event
    # associated with the webhook.
    event: "RegistryWebhookEvent"
    # Webhook ID
    id: str

    def as_request(self) -> (dict, dict):
        testRegistryWebhookRequest_query, testRegistryWebhookRequest_body = {}, {}
        if self.event:
            testRegistryWebhookRequest_body["event"] = self.event.value
        if self.id:
            testRegistryWebhookRequest_body["id"] = self.id

        return testRegistryWebhookRequest_query, testRegistryWebhookRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TestRegistryWebhookRequest":
        return cls(
            event=RegistryWebhookEvent(d["event"]) if "event" in d else None,
            id=d.get("id", None),
        )


@dataclass
class TestRegistryWebhookResponse:

    # Test webhook response object.
    webhook: "TestRegistryWebhook"

    def as_request(self) -> (dict, dict):
        testRegistryWebhookResponse_query, testRegistryWebhookResponse_body = {}, {}
        if self.webhook:
            testRegistryWebhookResponse_body["webhook"] = self.webhook.as_request()[1]

        return testRegistryWebhookResponse_query, testRegistryWebhookResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TestRegistryWebhookResponse":
        return cls(
            webhook=TestRegistryWebhook.from_dict(d["webhook"])
            if "webhook" in d
            else None,
        )


@dataclass
class TransitionModelVersionStage:

    # When transitioning a model version to a particular stage, this flag
    # dictates whether all existing model versions in that stage should be
    # atomically moved to the "archived" stage. This ensures that at-most-one
    # model version exists in the target stage. This field is *required* when
    # transitioning a model versions's stage
    archive_existing_versions: bool
    # Name of the registered model
    name: str
    # Transition `model_version` to new stage.
    stage: str
    # Model version number
    version: str

    def as_request(self) -> (dict, dict):
        transitionModelVersionStage_query, transitionModelVersionStage_body = {}, {}
        if self.archive_existing_versions:
            transitionModelVersionStage_body[
                "archive_existing_versions"
            ] = self.archive_existing_versions
        if self.name:
            transitionModelVersionStage_body["name"] = self.name
        if self.stage:
            transitionModelVersionStage_body["stage"] = self.stage
        if self.version:
            transitionModelVersionStage_body["version"] = self.version

        return transitionModelVersionStage_query, transitionModelVersionStage_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TransitionModelVersionStage":
        return cls(
            archive_existing_versions=d.get("archive_existing_versions", None),
            name=d.get("name", None),
            stage=d.get("stage", None),
            version=d.get("version", None),
        )


@dataclass
class TransitionModelVersionStageDatabricks:

    # Specifies whether to archive all current model versions in the target
    # stage.
    archive_existing_versions: bool
    # User-provided comment on the action.
    comment: str
    # Name of the model.
    name: str
    # Target stage of the transition. Valid values are:
    #
    # * `None`: The initial stage of a model version.
    #
    # * `Staging`: Staging or pre-production stage.
    #
    # * `Production`: Production stage.
    #
    # * `Archived`: Archived stage.
    stage: "Stage"
    # Version of the model.
    version: str

    def as_request(self) -> (dict, dict):
        (
            transitionModelVersionStageDatabricks_query,
            transitionModelVersionStageDatabricks_body,
        ) = ({}, {})
        if self.archive_existing_versions:
            transitionModelVersionStageDatabricks_body[
                "archive_existing_versions"
            ] = self.archive_existing_versions
        if self.comment:
            transitionModelVersionStageDatabricks_body["comment"] = self.comment
        if self.name:
            transitionModelVersionStageDatabricks_body["name"] = self.name
        if self.stage:
            transitionModelVersionStageDatabricks_body["stage"] = self.stage.value
        if self.version:
            transitionModelVersionStageDatabricks_body["version"] = self.version

        return (
            transitionModelVersionStageDatabricks_query,
            transitionModelVersionStageDatabricks_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TransitionModelVersionStageDatabricks":
        return cls(
            archive_existing_versions=d.get("archive_existing_versions", None),
            comment=d.get("comment", None),
            name=d.get("name", None),
            stage=Stage(d["stage"]) if "stage" in d else None,
            version=d.get("version", None),
        )


@dataclass
class TransitionModelVersionStageResponse:

    # Updated model version
    model_version: "ModelVersion"

    def as_request(self) -> (dict, dict):
        (
            transitionModelVersionStageResponse_query,
            transitionModelVersionStageResponse_body,
        ) = ({}, {})
        if self.model_version:
            transitionModelVersionStageResponse_body[
                "model_version"
            ] = self.model_version.as_request()[1]

        return (
            transitionModelVersionStageResponse_query,
            transitionModelVersionStageResponse_body,
        )

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TransitionModelVersionStageResponse":
        return cls(
            model_version=ModelVersion.from_dict(d["model_version"])
            if "model_version" in d
            else None,
        )


@dataclass
class TransitionRequest:
    """Transition request details."""

    # Array of actions on the activity allowed for the current viewer.
    available_actions: "List[ActivityAction]"
    # User-provided comment associated with the transition request.
    comment: str
    # Creation time of the object, as a Unix timestamp in milliseconds.
    creation_timestamp: int
    # Target stage of the transition (if the activity is stage transition
    # related). Valid values are:
    #
    # * `None`: The initial stage of a model version.
    #
    # * `Staging`: Staging or pre-production stage.
    #
    # * `Production`: Production stage.
    #
    # * `Archived`: Archived stage.
    to_stage: "Stage"
    # The username of the user that created the object.
    user_id: str

    def as_request(self) -> (dict, dict):
        transitionRequest_query, transitionRequest_body = {}, {}
        if self.available_actions:
            transitionRequest_body["available_actions"] = [
                v for v in self.available_actions
            ]
        if self.comment:
            transitionRequest_body["comment"] = self.comment
        if self.creation_timestamp:
            transitionRequest_body["creation_timestamp"] = self.creation_timestamp
        if self.to_stage:
            transitionRequest_body["to_stage"] = self.to_stage.value
        if self.user_id:
            transitionRequest_body["user_id"] = self.user_id

        return transitionRequest_query, transitionRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TransitionRequest":
        return cls(
            available_actions=d.get("available_actions", None),
            comment=d.get("comment", None),
            creation_timestamp=d.get("creation_timestamp", None),
            to_stage=Stage(d["to_stage"]) if "to_stage" in d else None,
            user_id=d.get("user_id", None),
        )


@dataclass
class TransitionStageResponse:

    model_version: "ModelVersionDatabricks"

    def as_request(self) -> (dict, dict):
        transitionStageResponse_query, transitionStageResponse_body = {}, {}
        if self.model_version:
            transitionStageResponse_body[
                "model_version"
            ] = self.model_version.as_request()[1]

        return transitionStageResponse_query, transitionStageResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TransitionStageResponse":
        return cls(
            model_version=ModelVersionDatabricks.from_dict(d["model_version"])
            if "model_version" in d
            else None,
        )


@dataclass
class UpdateComment:

    # User-provided comment on the action.
    comment: str
    # Unique identifier of an activity
    id: str

    def as_request(self) -> (dict, dict):
        updateComment_query, updateComment_body = {}, {}
        if self.comment:
            updateComment_body["comment"] = self.comment
        if self.id:
            updateComment_body["id"] = self.id

        return updateComment_query, updateComment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateComment":
        return cls(
            comment=d.get("comment", None),
            id=d.get("id", None),
        )


@dataclass
class UpdateExperiment:

    # ID of the associated experiment.
    experiment_id: str
    # If provided, the experiment's name is changed to the new name. The new
    # name must be unique.
    new_name: str

    def as_request(self) -> (dict, dict):
        updateExperiment_query, updateExperiment_body = {}, {}
        if self.experiment_id:
            updateExperiment_body["experiment_id"] = self.experiment_id
        if self.new_name:
            updateExperiment_body["new_name"] = self.new_name

        return updateExperiment_query, updateExperiment_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateExperiment":
        return cls(
            experiment_id=d.get("experiment_id", None),
            new_name=d.get("new_name", None),
        )


@dataclass
class UpdateModelVersionRequest:

    # If provided, updates the description for this `registered_model`.
    description: str
    # Name of the registered model
    name: str
    # Model version number
    version: str

    def as_request(self) -> (dict, dict):
        updateModelVersionRequest_query, updateModelVersionRequest_body = {}, {}
        if self.description:
            updateModelVersionRequest_body["description"] = self.description
        if self.name:
            updateModelVersionRequest_body["name"] = self.name
        if self.version:
            updateModelVersionRequest_body["version"] = self.version

        return updateModelVersionRequest_query, updateModelVersionRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateModelVersionRequest":
        return cls(
            description=d.get("description", None),
            name=d.get("name", None),
            version=d.get("version", None),
        )


@dataclass
class UpdateRegisteredModelRequest:

    # If provided, updates the description for this `registered_model`.
    description: str
    # Registered model unique name identifier.
    name: str

    def as_request(self) -> (dict, dict):
        updateRegisteredModelRequest_query, updateRegisteredModelRequest_body = {}, {}
        if self.description:
            updateRegisteredModelRequest_body["description"] = self.description
        if self.name:
            updateRegisteredModelRequest_body["name"] = self.name

        return updateRegisteredModelRequest_query, updateRegisteredModelRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateRegisteredModelRequest":
        return cls(
            description=d.get("description", None),
            name=d.get("name", None),
        )


@dataclass
class UpdateRegistryWebhook:

    # User-specified description for the webhook.
    description: str
    # Events that can trigger a registry webhook: * `MODEL_VERSION_CREATED`: A
    # new model version was created for the associated model.
    #
    # * `MODEL_VERSION_TRANSITIONED_STAGE`: A model version’s stage was
    # changed.
    #
    # * `TRANSITION_REQUEST_CREATED`: A user requested a model version’s stage
    # be transitioned.
    #
    # * `COMMENT_CREATED`: A user wrote a comment on a registered model.
    #
    # * `REGISTERED_MODEL_CREATED`: A new registered model was created. This
    # event type can only be specified for a registry-wide webhook, which can be
    # created by not specifying a model name in the create request.
    #
    # * `MODEL_VERSION_TAG_SET`: A user set a tag on the model version.
    #
    # * `MODEL_VERSION_TRANSITIONED_TO_STAGING`: A model version was
    # transitioned to staging.
    #
    # * `MODEL_VERSION_TRANSITIONED_TO_PRODUCTION`: A model version was
    # transitioned to production.
    #
    # * `MODEL_VERSION_TRANSITIONED_TO_ARCHIVED`: A model version was archived.
    #
    # * `TRANSITION_REQUEST_TO_STAGING_CREATED`: A user requested a model
    # version be transitioned to staging.
    #
    # * `TRANSITION_REQUEST_TO_PRODUCTION_CREATED`: A user requested a model
    # version be transitioned to production.
    #
    # * `TRANSITION_REQUEST_TO_ARCHIVED_CREATED`: A user requested a model
    # version be archived.
    events: "List[RegistryWebhookEvent]"

    http_url_spec: "HttpUrlSpec"
    # Webhook ID
    id: str

    job_spec: "JobSpec"
    # This describes an enum
    status: "RegistryWebhookStatus"

    def as_request(self) -> (dict, dict):
        updateRegistryWebhook_query, updateRegistryWebhook_body = {}, {}
        if self.description:
            updateRegistryWebhook_body["description"] = self.description
        if self.events:
            updateRegistryWebhook_body["events"] = [v for v in self.events]
        if self.http_url_spec:
            updateRegistryWebhook_body[
                "http_url_spec"
            ] = self.http_url_spec.as_request()[1]
        if self.id:
            updateRegistryWebhook_body["id"] = self.id
        if self.job_spec:
            updateRegistryWebhook_body["job_spec"] = self.job_spec.as_request()[1]
        if self.status:
            updateRegistryWebhook_body["status"] = self.status.value

        return updateRegistryWebhook_query, updateRegistryWebhook_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateRegistryWebhook":
        return cls(
            description=d.get("description", None),
            events=d.get("events", None),
            http_url_spec=HttpUrlSpec.from_dict(d["http_url_spec"])
            if "http_url_spec" in d
            else None,
            id=d.get("id", None),
            job_spec=JobSpec.from_dict(d["job_spec"]) if "job_spec" in d else None,
            status=RegistryWebhookStatus(d["status"]) if "status" in d else None,
        )


@dataclass
class UpdateResponse:

    # Comment details.
    comment: "CommentObject"

    def as_request(self) -> (dict, dict):
        updateResponse_query, updateResponse_body = {}, {}
        if self.comment:
            updateResponse_body["comment"] = self.comment.as_request()[1]

        return updateResponse_query, updateResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateResponse":
        return cls(
            comment=CommentObject.from_dict(d["comment"]) if "comment" in d else None,
        )


@dataclass
class UpdateRun:

    # Unix timestamp in milliseconds of when the run ended.
    end_time: int
    # ID of the run to update. Must be provided.
    run_id: str
    # [Deprecated, use run_id instead] ID of the run to update.. This field will
    # be removed in a future MLflow version.
    run_uuid: str
    # Updated status of the run.
    status: "UpdateRunStatus"

    def as_request(self) -> (dict, dict):
        updateRun_query, updateRun_body = {}, {}
        if self.end_time:
            updateRun_body["end_time"] = self.end_time
        if self.run_id:
            updateRun_body["run_id"] = self.run_id
        if self.run_uuid:
            updateRun_body["run_uuid"] = self.run_uuid
        if self.status:
            updateRun_body["status"] = self.status.value

        return updateRun_query, updateRun_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateRun":
        return cls(
            end_time=d.get("end_time", None),
            run_id=d.get("run_id", None),
            run_uuid=d.get("run_uuid", None),
            status=UpdateRunStatus(d["status"]) if "status" in d else None,
        )


@dataclass
class UpdateRunResponse:

    # Updated metadata of the run.
    run_info: "RunInfo"

    def as_request(self) -> (dict, dict):
        updateRunResponse_query, updateRunResponse_body = {}, {}
        if self.run_info:
            updateRunResponse_body["run_info"] = self.run_info.as_request()[1]

        return updateRunResponse_query, updateRunResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateRunResponse":
        return cls(
            run_info=RunInfo.from_dict(d["run_info"]) if "run_info" in d else None,
        )


class UpdateRunStatus(Enum):
    """Updated status of the run."""

    FAILED = "FAILED"
    FINISHED = "FINISHED"
    KILLED = "KILLED"
    RUNNING = "RUNNING"
    SCHEDULED = "SCHEDULED"


class ExperimentsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateExperiment) -> CreateExperimentResponse:
        """Create experiment.

        Creates an experiment with a name. Returns the ID of the newly created
        experiment. Validates that another experiment with the same name does
        not already exist and fails if another experiment with the same name
        already exists.

        Throws `RESOURCE_ALREADY_EXISTS` if a experiment with the given name
        exists."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/experiments/create", query=query, body=body
        )
        return CreateExperimentResponse.from_dict(json)

    def delete(self, request: DeleteExperiment):
        """Delete an experiment.

        Marks an experiment and associated metadata, runs, metrics, params, and
        tags for deletion. If the experiment uses FileStore, artifacts
        associated with experiment are also deleted."""
        query, body = request.as_request()
        self._api.do(
            "POST", "/api/2.0/mlflow/experiments/delete", query=query, body=body
        )

    def get(self, request: GetExperimentRequest) -> Experiment:
        """Get an experiment.

        Gets metadata for an experiment. This method works on deleted
        experiments."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/mlflow/experiments/get", query=query, body=body
        )
        return Experiment.from_dict(json)

    def get_by_name(self, request: GetByNameRequest) -> GetExperimentByNameResponse:
        """Get metadata.

        "Gets metadata for an experiment.

        This endpoint will return deleted experiments, but prefers the active
        experiment if an active and deleted experiment share the same name. If
        multiple deleted\nexperiments share the same name, the API will return
        one of them.

        Throws `RESOURCE_DOES_NOT_EXIST` if no experiment with the specified
        name exists.S"""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/mlflow/experiments/get-by-name", query=query, body=body
        )
        return GetExperimentByNameResponse.from_dict(json)

    def list(self, request: ListExperimentsRequest) -> ListExperimentsResponse:
        """List experiments.

        Gets a list of all experiments."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/mlflow/experiments/list", query=query, body=body
        )
        return ListExperimentsResponse.from_dict(json)

    def restore(self, request: RestoreExperiment):
        """Restores an experiment.

        "Restore an experiment marked for deletion. This also
        restores\nassociated metadata, runs, metrics, params, and tags. If
        experiment uses FileStore, underlying\nartifacts associated with
        experiment are also restored.\n\nThrows `RESOURCE_DOES_NOT_EXIST` if
        experiment was never created or was permanently deleted.","""
        query, body = request.as_request()
        self._api.do(
            "POST", "/api/2.0/mlflow/experiments/restore", query=query, body=body
        )

    def search(self, request: SearchExperiments) -> SearchExperimentsResponse:
        """Search experiments.

        Searches for experiments that satisfy specified search criteria."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/experiments/search", query=query, body=body
        )
        return SearchExperimentsResponse.from_dict(json)

    def set_experiment_tag(self, request: SetExperimentTag):
        """Set a tag.

        Sets a tag on an experiment. Experiment tags are metadata that can be
        updated."""
        query, body = request.as_request()
        self._api.do(
            "POST",
            "/api/2.0/mlflow/experiments/set-experiment-tag",
            query=query,
            body=body,
        )

    def update(self, request: UpdateExperiment):
        """Update an experiment.

        Updates experiment metadata."""
        query, body = request.as_request()
        self._api.do(
            "POST", "/api/2.0/mlflow/experiments/update", query=query, body=body
        )


class MLflowArtifactsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def list(self, request: ListArtifactsRequest) -> ListArtifactsResponse:
        """Get all artifacts.

        List artifacts for a run. Takes an optional `artifact_path` prefix. If
        it is specified, the response contains only artifacts with the specified
        prefix.","""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/mlflow/artifacts/list", query=query, body=body
        )
        return ListArtifactsResponse.from_dict(json)


class MLflowDatabricksAPI:
    def __init__(self, api_client):
        self._api = api_client

    def get(self, request: GetMLflowDatabrickRequest) -> GetResponse:
        """Get model.

        Get the details of a model. This is a Databricks Workspace version of
        the [MLflow endpoint] that also returns the model's Databricks Workspace
        ID and the permission level of the requesting user on the model.

        [MLflow endpoint]: https://www.mlflow.org/docs/latest/rest-api.html#get-registeredmodel"""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            "/api/2.0/mlflow/databricks/registered-models/get",
            query=query,
            body=body,
        )
        return GetResponse.from_dict(json)

    def transition_stage(
        self, request: TransitionModelVersionStageDatabricks
    ) -> TransitionStageResponse:
        """Transition a stage.

        Transition a model version's stage. This is a Databricks Workspace
        version of the [MLflow endpoint] that also accepts a comment associated
        with the transition to be recorded.",

        [MLflow endpoint]: https://www.mlflow.org/docs/latest/rest-api.html#transition-modelversion-stage"""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            "/api/2.0/mlflow/databricks/model-versions/transition-stage",
            query=query,
            body=body,
        )
        return TransitionStageResponse.from_dict(json)


class MLflowMetricsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def get_history(self, request: GetHistoryRequest) -> GetMetricHistoryResponse:
        """Get all history.

        Gets a list of all values for the specified metric for a given run."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/mlflow/metrics/get-history", query=query, body=body
        )
        return GetMetricHistoryResponse.from_dict(json)


class MLflowRunsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateRun) -> CreateRunResponse:
        """Create a run.

        Creates a new run within an experiment. A run is usually a single
        execution of a machine learning or data ETL pipeline. MLflow uses runs
        to track the `mlflowParam`, `mlflowMetric` and `mlflowRunTag` associated
        with a single execution."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/runs/create", query=query, body=body
        )
        return CreateRunResponse.from_dict(json)

    def delete(self, request: DeleteRun):
        """Delete a run.

        Marks a run for deletion."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.0/mlflow/runs/delete", query=query, body=body)

    def delete_tag(self, request: DeleteTag):
        """Delete a tag.

        Deletes a tag on a run. Tags are run metadata that can be updated during
        a run and after a run completes."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.0/mlflow/runs/delete-tag", query=query, body=body)

    def get(self, request: GetRunRequest) -> GetRunResponse:
        """Get a run.

        "Gets the metadata, metrics, params, and tags for a run. In the case
        where multiple metrics with the same key are logged for a run, return
        only the value with the latest timestamp.

        If there are multiple values with the latest timestamp, return the
        maximum of these values."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/2.0/mlflow/runs/get", query=query, body=body)
        return GetRunResponse.from_dict(json)

    def log_batch(self, request: LogBatch):
        """Log a batch.

        Logs a batch of metrics, params, and tags for a run. If any data failed
        to be persisted, the server will respond with an error (non-200 status
        code).

        In case of error (due to internal server error or an invalid request),
        partial data may be written.

        You can write metrics, params, and tags in interleaving fashion, but
        within a given entity type are guaranteed to follow the order specified
        in the request body.

        The overwrite behavior for metrics, params, and tags is as follows:

        * Metrics: metric values are never overwritten. Logging a metric (key,
        value, timestamp) appends to the set of values for the metric with the
        provided key.

        * Tags: tag values can be overwritten by successive writes to the same
        tag key. That is, if multiple tag values with the same key are provided
        in the same API request, the last-provided tag value is written. Logging
        the same tag (key, value) is permitted. Specifically, logging a tag is
        idempotent.

        * Parameters: once written, param values cannot be changed (attempting
        to overwrite a param value will result in an error). However, logging
        the same param (key, value) is permitted. Specifically, logging a param
        is idempotent.

        Request Limits ------------------------------- A single JSON-serialized
        API request may be up to 1 MB in size and contain:

        * No more than 1000 metrics, params, and tags in total * Up to 1000
        metrics\n- Up to 100 params * Up to 100 tags

        For example, a valid request might contain 900 metrics, 50 params, and
        50 tags, but logging 900 metrics, 50 params, and 51 tags is invalid.

        The following limits also apply to metric, param, and tag keys and
        values:

        * Metric keyes, param keys, and tag keys can be up to 250 characters in
        length * Parameter and tag values can be up to 250 characters in length"""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.0/mlflow/runs/log-batch", query=query, body=body)

    def log_metric(self, request: LogMetric):
        """Log a metric.

        Logs a metric for a run. A metric is a key-value pair (string key, float
        value) with an associated timestamp. Examples include the various
        metrics that represent ML model accuracy. A metric can be logged
        multiple times."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.0/mlflow/runs/log-metric", query=query, body=body)

    def log_model(self, request: LogModel):
        """Log a model.

        **NOTE:** Experimental: This API may change or be removed in a future
        release without warning."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.0/mlflow/runs/log-model", query=query, body=body)

    def log_parameter(self, request: LogParam):
        """Log a param.

        Logs a param used for a run. A param is a key-value pair (string key,
        string value). Examples include hyperparameters used for ML model
        training and constant dates and values used in an ETL pipeline. A param
        can be logged only once for a run."""
        query, body = request.as_request()
        self._api.do(
            "POST", "/api/2.0/mlflow/runs/log-parameter", query=query, body=body
        )

    def restore(self, request: RestoreRun):
        """Restore a run.

        Restores a deleted run."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.0/mlflow/runs/restore", query=query, body=body)

    def search(self, request: SearchRuns) -> SearchRunsResponse:
        """Search for runs.

        Searches for runs that satisfy expressions.

        Search expressions can use `mlflowMetric` and `mlflowParam` keys.","""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/runs/search", query=query, body=body
        )
        return SearchRunsResponse.from_dict(json)

    def set_tag(self, request: SetTag):
        """Set a tag.

        Sets a tag on a run. Tags are run metadata that can be updated during a
        run and after a run completes."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.0/mlflow/runs/set-tag", query=query, body=body)

    def update(self, request: UpdateRun) -> UpdateRunResponse:
        """Update a run.

        Updates run metadata."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/runs/update", query=query, body=body
        )
        return UpdateRunResponse.from_dict(json)


class ModelVersionCommentsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateComment) -> CreateResponse:
        """Post a comment.

        Posts a comment on a model version. A comment can be submitted either by
        a user or programmatically to display relevant information about the
        model. For example, test results or deployment errors."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/comments/create", query=query, body=body
        )
        return CreateResponse.from_dict(json)

    def delete(self, request: DeleteModelVersionCommentRequest):
        """Delete a comment.

        Deletes a comment on a model version."""
        query, body = request.as_request()
        self._api.do(
            "DELETE", "/api/2.0/mlflow/comments/delete", query=query, body=body
        )

    def update(self, request: UpdateComment) -> UpdateResponse:
        """Update a comment.

        Post an edit to a comment on a model version."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/comments/update", query=query, body=body
        )
        return UpdateResponse.from_dict(json)


class ModelVersionsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateModelVersionRequest) -> CreateModelVersionResponse:
        """Create a model version.

        Creates a model version."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/model-versions/create", query=query, body=body
        )
        return CreateModelVersionResponse.from_dict(json)

    def delete(self, request: DeleteModelVersionRequest):
        """Delete a model version.

        Deletes a model version."""
        query, body = request.as_request()
        self._api.do(
            "DELETE", "/api/2.0/mlflow/model-versions/delete", query=query, body=body
        )

    def delete_tag(self, request: DeleteModelVersionTagRequest):
        """Delete a model version tag.

        Deletes a model version tag."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            "/api/2.0/mlflow/model-versions/delete-tag",
            query=query,
            body=body,
        )

    def get(self, request: GetModelVersionRequest) -> GetModelVersionResponse:
        """Get a model version.

        Get a model version."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/mlflow/model-versions/get", query=query, body=body
        )
        return GetModelVersionResponse.from_dict(json)

    def get_download_uri(
        self, request: GetModelVersionDownloadUriRequest
    ) -> GetModelVersionDownloadUriResponse:
        """Get a model version URI.

        Gets a URI to download the model version."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            "/api/2.0/mlflow/model-versions/get-download-uri",
            query=query,
            body=body,
        )
        return GetModelVersionDownloadUriResponse.from_dict(json)

    def search(
        self, request: SearchModelVersionsRequest
    ) -> SearchModelVersionsResponse:
        """Searches model versions.

        Searches for specific model versions based on the supplied __filter__."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/mlflow/model-versions/search", query=query, body=body
        )
        return SearchModelVersionsResponse.from_dict(json)

    def set_tag(self, request: SetModelVersionTagRequest):
        """Set a version tag.

        Sets a model version tag."""
        query, body = request.as_request()
        self._api.do(
            "POST", "/api/2.0/mlflow/model-versions/set-tag", query=query, body=body
        )

    def transition_stage(
        self, request: TransitionModelVersionStage
    ) -> TransitionModelVersionStageResponse:
        """Transition a stage.

        Transition to the next model stage."""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            "/api/2.0/mlflow/model-versions/transition-stage",
            query=query,
            body=body,
        )
        return TransitionModelVersionStageResponse.from_dict(json)

    def update(self, request: UpdateModelVersionRequest):
        """Update model version.

        Updates the model version."""
        query, body = request.as_request()
        self._api.do(
            "PATCH", "/api/2.0/mlflow/model-versions/update", query=query, body=body
        )


class RegisteredModelsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self, request: CreateRegisteredModelRequest
    ) -> CreateRegisteredModelResponse:
        """Create a model.

        Creates a new registered model with the name specified in the request
        body.

        Throws `RESOURCE_ALREADY_EXISTS` if a registered model with the given
        name exists."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/registered-models/create", query=query, body=body
        )
        return CreateRegisteredModelResponse.from_dict(json)

    def delete(self, request: DeleteRegisteredModelRequest):
        """Delete a model.

        Deletes a registered model."""
        query, body = request.as_request()
        self._api.do(
            "DELETE", "/api/2.0/mlflow/registered-models/delete", query=query, body=body
        )

    def delete_tag(self, request: DeleteRegisteredModelTagRequest):
        """Delete a model tag.

        Deletes the tag for a registered model."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            "/api/2.0/mlflow/registered-models/delete-tag",
            query=query,
            body=body,
        )

    def get(self, request: GetRegisteredModelRequest) -> GetRegisteredModelResponse:
        """Get a model.

        Gets the registered model that matches the specified ID."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/mlflow/registered-models/get", query=query, body=body
        )
        return GetRegisteredModelResponse.from_dict(json)

    def get_latest_versions(
        self, request: GetLatestVersionsRequest
    ) -> GetLatestVersionsResponse:
        """Get the latest version.

        Gets the latest version of a registered model."""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            "/api/2.0/mlflow/registered-models/get-latest-versions",
            query=query,
            body=body,
        )
        return GetLatestVersionsResponse.from_dict(json)

    def list(
        self, request: ListRegisteredModelsRequest
    ) -> ListRegisteredModelsResponse:
        """List models.

        Lists all available registered models, up to the limit specified in
        __max_results__."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/mlflow/registered-models/list", query=query, body=body
        )
        return ListRegisteredModelsResponse.from_dict(json)

    def rename(
        self, request: RenameRegisteredModelRequest
    ) -> RenameRegisteredModelResponse:
        """Rename a model.

        Renames a registered model."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/registered-models/rename", query=query, body=body
        )
        return RenameRegisteredModelResponse.from_dict(json)

    def search(
        self, request: SearchRegisteredModelsRequest
    ) -> SearchRegisteredModelsResponse:
        """Search models.

        Search for registered models based on the specified __filter__."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/mlflow/registered-models/search", query=query, body=body
        )
        return SearchRegisteredModelsResponse.from_dict(json)

    def set_tag(self, request: SetRegisteredModelTagRequest):
        """Set a tag.

        Sets a tag on a registered model."""
        query, body = request.as_request()
        self._api.do(
            "POST", "/api/2.0/mlflow/registered-models/set-tag", query=query, body=body
        )

    def update(self, request: UpdateRegisteredModelRequest):
        """Update model.

        Updates a registered model."""
        query, body = request.as_request()
        self._api.do(
            "PATCH", "/api/2.0/mlflow/registered-models/update", query=query, body=body
        )


class RegistryWebhooksAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateRegistryWebhook) -> CreateResponse:
        """Create a webhook.

        **NOTE**: This endpoint is in Public Preview.

        Creates a registry webhook."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/registry-webhooks/create", query=query, body=body
        )
        return CreateResponse.from_dict(json)

    def delete(self, request: DeleteRegistryWebhookRequest):
        """Delete a webhook.

        **NOTE:** This endpoint is in Public Preview.

        Deletes a registry webhook."""
        query, body = request.as_request()
        self._api.do(
            "DELETE", "/api/2.0/mlflow/registry-webhooks/delete", query=query, body=body
        )

    def list(self, request: ListRegistryWebhooksRequest) -> ListRegistryWebhooks:
        """List registry webhooks.

        **NOTE:** This endpoint is in Public Preview.

        Lists all registry webhooks."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/mlflow/registry-webhooks/list", query=query, body=body
        )
        return ListRegistryWebhooks.from_dict(json)

    def test(self, request: TestRegistryWebhookRequest) -> TestRegistryWebhookResponse:
        """Test a webhook.

        **NOTE:** This endpoint is in Public Preview.

        Tests a registry webhook."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/registry-webhooks/test", query=query, body=body
        )
        return TestRegistryWebhookResponse.from_dict(json)

    def update(self, request: UpdateRegistryWebhook):
        """Update a webhook.

        **NOTE:** This endpoint is in Public Preview.

        Updates a registry webhook."""
        query, body = request.as_request()
        self._api.do(
            "PATCH", "/api/2.0/mlflow/registry-webhooks/update", query=query, body=body
        )


class TransitionRequestsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def approve(self, request: ApproveTransitionRequest) -> ApproveResponse:
        """Approve transition requests.

        Approves a model version stage transition request."""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            "/api/2.0/mlflow/transition-requests/approve",
            query=query,
            body=body,
        )
        return ApproveResponse.from_dict(json)

    def create(self, request: CreateTransitionRequest) -> CreateResponse:
        """Make a transition request.

        Creates a model version stage transition request."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/transition-requests/create", query=query, body=body
        )
        return CreateResponse.from_dict(json)

    def delete(self, request: DeleteTransitionRequestRequest):
        """Delete a ransition request.

        Cancels a model version stage transition request."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            "/api/2.0/mlflow/transition-requests/delete",
            query=query,
            body=body,
        )

    def list(self, request: ListTransitionRequestsRequest) -> ListResponse:
        """List transition requests.

        Gets a list of all open stage transition requests for the model version."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/mlflow/transition-requests/list", query=query, body=body
        )
        return ListResponse.from_dict(json)

    def reject(self, request: RejectTransitionRequest) -> RejectResponse:
        """Reject a transition request.

        Rejects a model version stage transition request."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/mlflow/transition-requests/reject", query=query, body=body
        )
        return RejectResponse.from_dict(json)

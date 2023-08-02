# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class Activity:
    """Activity recorded for the action."""

    activity_type: Optional['ActivityType'] = None
    comment: Optional[str] = None
    creation_timestamp: Optional[int] = None
    from_stage: Optional['Stage'] = None
    id: Optional[str] = None
    last_updated_timestamp: Optional[int] = None
    system_comment: Optional[str] = None
    to_stage: Optional['Stage'] = None
    user_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.activity_type is not None: body['activity_type'] = self.activity_type.value
        if self.comment is not None: body['comment'] = self.comment
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.from_stage is not None: body['from_stage'] = self.from_stage.value
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.system_comment is not None: body['system_comment'] = self.system_comment
        if self.to_stage is not None: body['to_stage'] = self.to_stage.value
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Activity':
        return cls(activity_type=_enum(d, 'activity_type', ActivityType),
                   comment=d.get('comment', None),
                   creation_timestamp=d.get('creation_timestamp', None),
                   from_stage=_enum(d, 'from_stage', Stage),
                   id=d.get('id', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   system_comment=d.get('system_comment', None),
                   to_stage=_enum(d, 'to_stage', Stage),
                   user_id=d.get('user_id', None))


class ActivityAction(Enum):
    """This describes an enum"""

    APPROVE_TRANSITION_REQUEST = 'APPROVE_TRANSITION_REQUEST'
    CANCEL_TRANSITION_REQUEST = 'CANCEL_TRANSITION_REQUEST'
    REJECT_TRANSITION_REQUEST = 'REJECT_TRANSITION_REQUEST'


class ActivityType(Enum):
    """This describes an enum"""

    APPLIED_TRANSITION = 'APPLIED_TRANSITION'
    APPROVED_REQUEST = 'APPROVED_REQUEST'
    CANCELLED_REQUEST = 'CANCELLED_REQUEST'
    NEW_COMMENT = 'NEW_COMMENT'
    REJECTED_REQUEST = 'REJECTED_REQUEST'
    REQUESTED_TRANSITION = 'REQUESTED_TRANSITION'
    SYSTEM_TRANSITION = 'SYSTEM_TRANSITION'


@dataclass
class ApproveTransitionRequest:
    name: str
    version: str
    stage: 'Stage'
    archive_existing_versions: bool
    comment: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.archive_existing_versions is not None:
            body['archive_existing_versions'] = self.archive_existing_versions
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        if self.stage is not None: body['stage'] = self.stage.value
        if self.version is not None: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ApproveTransitionRequest':
        return cls(archive_existing_versions=d.get('archive_existing_versions', None),
                   comment=d.get('comment', None),
                   name=d.get('name', None),
                   stage=_enum(d, 'stage', Stage),
                   version=d.get('version', None))


@dataclass
class ApproveTransitionRequestResponse:
    activity: Optional['Activity'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.activity: body['activity'] = self.activity.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ApproveTransitionRequestResponse':
        return cls(activity=_from_dict(d, 'activity', Activity))


class CommentActivityAction(Enum):
    """This describes an enum"""

    DELETE_COMMENT = 'DELETE_COMMENT'
    EDIT_COMMENT = 'EDIT_COMMENT'


@dataclass
class CommentObject:
    """Comment details."""

    available_actions: Optional['List[CommentActivityAction]'] = None
    comment: Optional[str] = None
    creation_timestamp: Optional[int] = None
    id: Optional[str] = None
    last_updated_timestamp: Optional[int] = None
    user_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.available_actions: body['available_actions'] = [v.value for v in self.available_actions]
        if self.comment is not None: body['comment'] = self.comment
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CommentObject':
        return cls(available_actions=d.get('available_actions', None),
                   comment=d.get('comment', None),
                   creation_timestamp=d.get('creation_timestamp', None),
                   id=d.get('id', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   user_id=d.get('user_id', None))


@dataclass
class CreateComment:
    name: str
    version: str
    comment: str

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        if self.version is not None: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateComment':
        return cls(comment=d.get('comment', None), name=d.get('name', None), version=d.get('version', None))


@dataclass
class CreateCommentResponse:
    comment: Optional['CommentObject'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCommentResponse':
        return cls(comment=_from_dict(d, 'comment', CommentObject))


@dataclass
class CreateExperiment:
    name: str
    artifact_location: Optional[str] = None
    tags: Optional['List[ExperimentTag]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.artifact_location is not None: body['artifact_location'] = self.artifact_location
        if self.name is not None: body['name'] = self.name
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateExperiment':
        return cls(artifact_location=d.get('artifact_location', None),
                   name=d.get('name', None),
                   tags=_repeated(d, 'tags', ExperimentTag))


@dataclass
class CreateExperimentResponse:
    experiment_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.experiment_id is not None: body['experiment_id'] = self.experiment_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateExperimentResponse':
        return cls(experiment_id=d.get('experiment_id', None))


@dataclass
class CreateModelRequest:
    name: str
    description: Optional[str] = None
    tags: Optional['List[ModelTag]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.name is not None: body['name'] = self.name
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateModelRequest':
        return cls(description=d.get('description', None),
                   name=d.get('name', None),
                   tags=_repeated(d, 'tags', ModelTag))


@dataclass
class CreateModelResponse:
    registered_model: Optional['Model'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.registered_model: body['registered_model'] = self.registered_model.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateModelResponse':
        return cls(registered_model=_from_dict(d, 'registered_model', Model))


@dataclass
class CreateModelVersionRequest:
    name: str
    source: str
    description: Optional[str] = None
    run_id: Optional[str] = None
    run_link: Optional[str] = None
    tags: Optional['List[ModelVersionTag]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.name is not None: body['name'] = self.name
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.run_link is not None: body['run_link'] = self.run_link
        if self.source is not None: body['source'] = self.source
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateModelVersionRequest':
        return cls(description=d.get('description', None),
                   name=d.get('name', None),
                   run_id=d.get('run_id', None),
                   run_link=d.get('run_link', None),
                   source=d.get('source', None),
                   tags=_repeated(d, 'tags', ModelVersionTag))


@dataclass
class CreateModelVersionResponse:
    model_version: Optional['ModelVersion'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.model_version: body['model_version'] = self.model_version.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateModelVersionResponse':
        return cls(model_version=_from_dict(d, 'model_version', ModelVersion))


@dataclass
class CreateRegistryWebhook:
    events: 'List[RegistryWebhookEvent]'
    description: Optional[str] = None
    http_url_spec: Optional['HttpUrlSpec'] = None
    job_spec: Optional['JobSpec'] = None
    model_name: Optional[str] = None
    status: Optional['RegistryWebhookStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.events: body['events'] = [v.value for v in self.events]
        if self.http_url_spec: body['http_url_spec'] = self.http_url_spec.as_dict()
        if self.job_spec: body['job_spec'] = self.job_spec.as_dict()
        if self.model_name is not None: body['model_name'] = self.model_name
        if self.status is not None: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRegistryWebhook':
        return cls(description=d.get('description', None),
                   events=d.get('events', None),
                   http_url_spec=_from_dict(d, 'http_url_spec', HttpUrlSpec),
                   job_spec=_from_dict(d, 'job_spec', JobSpec),
                   model_name=d.get('model_name', None),
                   status=_enum(d, 'status', RegistryWebhookStatus))


@dataclass
class CreateRun:
    experiment_id: Optional[str] = None
    start_time: Optional[int] = None
    tags: Optional['List[RunTag]'] = None
    user_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.experiment_id is not None: body['experiment_id'] = self.experiment_id
        if self.start_time is not None: body['start_time'] = self.start_time
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRun':
        return cls(experiment_id=d.get('experiment_id', None),
                   start_time=d.get('start_time', None),
                   tags=_repeated(d, 'tags', RunTag),
                   user_id=d.get('user_id', None))


@dataclass
class CreateRunResponse:
    run: Optional['Run'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.run: body['run'] = self.run.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRunResponse':
        return cls(run=_from_dict(d, 'run', Run))


@dataclass
class CreateTransitionRequest:
    name: str
    version: str
    stage: 'Stage'
    comment: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        if self.stage is not None: body['stage'] = self.stage.value
        if self.version is not None: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateTransitionRequest':
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   stage=_enum(d, 'stage', Stage),
                   version=d.get('version', None))


@dataclass
class CreateTransitionRequestResponse:
    request: Optional['TransitionRequest'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.request: body['request'] = self.request.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateTransitionRequestResponse':
        return cls(request=_from_dict(d, 'request', TransitionRequest))


@dataclass
class CreateWebhookResponse:
    webhook: Optional['RegistryWebhook'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.webhook: body['webhook'] = self.webhook.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateWebhookResponse':
        return cls(webhook=_from_dict(d, 'webhook', RegistryWebhook))


@dataclass
class Dataset:
    digest: Optional[str] = None
    name: Optional[str] = None
    profile: Optional[str] = None
    schema: Optional[str] = None
    source: Optional[str] = None
    source_type: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.digest is not None: body['digest'] = self.digest
        if self.name is not None: body['name'] = self.name
        if self.profile is not None: body['profile'] = self.profile
        if self.schema is not None: body['schema'] = self.schema
        if self.source is not None: body['source'] = self.source
        if self.source_type is not None: body['source_type'] = self.source_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Dataset':
        return cls(digest=d.get('digest', None),
                   name=d.get('name', None),
                   profile=d.get('profile', None),
                   schema=d.get('schema', None),
                   source=d.get('source', None),
                   source_type=d.get('source_type', None))


@dataclass
class DatasetInput:
    dataset: Optional['Dataset'] = None
    tags: Optional['List[InputTag]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.dataset: body['dataset'] = self.dataset.as_dict()
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DatasetInput':
        return cls(dataset=_from_dict(d, 'dataset', Dataset), tags=_repeated(d, 'tags', InputTag))


@dataclass
class DeleteCommentRequest:
    """Delete a comment"""

    id: str


@dataclass
class DeleteExperiment:
    experiment_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.experiment_id is not None: body['experiment_id'] = self.experiment_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteExperiment':
        return cls(experiment_id=d.get('experiment_id', None))


@dataclass
class DeleteModelRequest:
    """Delete a model"""

    name: str


@dataclass
class DeleteModelTagRequest:
    """Delete a model tag"""

    name: str
    key: str


@dataclass
class DeleteModelVersionRequest:
    """Delete a model version."""

    name: str
    version: str


@dataclass
class DeleteModelVersionTagRequest:
    """Delete a model version tag"""

    name: str
    version: str
    key: str


@dataclass
class DeleteRun:
    run_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.run_id is not None: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteRun':
        return cls(run_id=d.get('run_id', None))


@dataclass
class DeleteTag:
    run_id: str
    key: str

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.run_id is not None: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteTag':
        return cls(key=d.get('key', None), run_id=d.get('run_id', None))


@dataclass
class DeleteTransitionRequestRequest:
    """Delete a transition request"""

    name: str
    version: str
    stage: 'DeleteTransitionRequestStage'
    creator: str
    comment: Optional[str] = None


class DeleteTransitionRequestStage(Enum):

    ARCHIVED = 'Archived'
    NONE = 'None'
    PRODUCTION = 'Production'
    STAGING = 'Staging'


@dataclass
class DeleteWebhookRequest:
    """Delete a webhook"""

    id: Optional[str] = None


@dataclass
class Experiment:
    artifact_location: Optional[str] = None
    creation_time: Optional[int] = None
    experiment_id: Optional[str] = None
    last_update_time: Optional[int] = None
    lifecycle_stage: Optional[str] = None
    name: Optional[str] = None
    tags: Optional['List[ExperimentTag]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.artifact_location is not None: body['artifact_location'] = self.artifact_location
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.experiment_id is not None: body['experiment_id'] = self.experiment_id
        if self.last_update_time is not None: body['last_update_time'] = self.last_update_time
        if self.lifecycle_stage is not None: body['lifecycle_stage'] = self.lifecycle_stage
        if self.name is not None: body['name'] = self.name
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Experiment':
        return cls(artifact_location=d.get('artifact_location', None),
                   creation_time=d.get('creation_time', None),
                   experiment_id=d.get('experiment_id', None),
                   last_update_time=d.get('last_update_time', None),
                   lifecycle_stage=d.get('lifecycle_stage', None),
                   name=d.get('name', None),
                   tags=_repeated(d, 'tags', ExperimentTag))


@dataclass
class ExperimentTag:
    key: Optional[str] = None
    value: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExperimentTag':
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class FileInfo:
    file_size: Optional[int] = None
    is_dir: Optional[bool] = None
    path: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.file_size is not None: body['file_size'] = self.file_size
        if self.is_dir is not None: body['is_dir'] = self.is_dir
        if self.path is not None: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FileInfo':
        return cls(file_size=d.get('file_size', None), is_dir=d.get('is_dir', None), path=d.get('path', None))


@dataclass
class GetByNameRequest:
    """Get metadata"""

    experiment_name: str


@dataclass
class GetExperimentByNameResponse:
    experiment: Optional['Experiment'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.experiment: body['experiment'] = self.experiment.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetExperimentByNameResponse':
        return cls(experiment=_from_dict(d, 'experiment', Experiment))


@dataclass
class GetExperimentRequest:
    """Get an experiment"""

    experiment_id: str


@dataclass
class GetHistoryRequest:
    """Get history of a given metric within a run"""

    metric_key: str
    max_results: Optional[int] = None
    page_token: Optional[str] = None
    run_id: Optional[str] = None
    run_uuid: Optional[str] = None


@dataclass
class GetLatestVersionsRequest:
    name: str
    stages: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.stages: body['stages'] = [v for v in self.stages]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetLatestVersionsRequest':
        return cls(name=d.get('name', None), stages=d.get('stages', None))


@dataclass
class GetLatestVersionsResponse:
    model_versions: Optional['List[ModelVersion]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.model_versions: body['model_versions'] = [v.as_dict() for v in self.model_versions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetLatestVersionsResponse':
        return cls(model_versions=_repeated(d, 'model_versions', ModelVersion))


@dataclass
class GetMetricHistoryResponse:
    metrics: Optional['List[Metric]'] = None
    next_page_token: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.metrics: body['metrics'] = [v.as_dict() for v in self.metrics]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetMetricHistoryResponse':
        return cls(metrics=_repeated(d, 'metrics', Metric), next_page_token=d.get('next_page_token', None))


@dataclass
class GetModelRequest:
    """Get model"""

    name: str


@dataclass
class GetModelResponse:
    registered_model_databricks: Optional['ModelDatabricks'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.registered_model_databricks:
            body['registered_model_databricks'] = self.registered_model_databricks.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetModelResponse':
        return cls(registered_model_databricks=_from_dict(d, 'registered_model_databricks', ModelDatabricks))


@dataclass
class GetModelVersionDownloadUriRequest:
    """Get a model version URI"""

    name: str
    version: str


@dataclass
class GetModelVersionDownloadUriResponse:
    artifact_uri: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.artifact_uri is not None: body['artifact_uri'] = self.artifact_uri
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetModelVersionDownloadUriResponse':
        return cls(artifact_uri=d.get('artifact_uri', None))


@dataclass
class GetModelVersionRequest:
    """Get a model version"""

    name: str
    version: str


@dataclass
class GetModelVersionResponse:
    model_version: Optional['ModelVersion'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.model_version: body['model_version'] = self.model_version.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetModelVersionResponse':
        return cls(model_version=_from_dict(d, 'model_version', ModelVersion))


@dataclass
class GetRunRequest:
    """Get a run"""

    run_id: str
    run_uuid: Optional[str] = None


@dataclass
class GetRunResponse:
    run: Optional['Run'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.run: body['run'] = self.run.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRunResponse':
        return cls(run=_from_dict(d, 'run', Run))


@dataclass
class HttpUrlSpec:
    url: str
    authorization: Optional[str] = None
    enable_ssl_verification: Optional[bool] = None
    secret: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.authorization is not None: body['authorization'] = self.authorization
        if self.enable_ssl_verification is not None:
            body['enable_ssl_verification'] = self.enable_ssl_verification
        if self.secret is not None: body['secret'] = self.secret
        if self.url is not None: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'HttpUrlSpec':
        return cls(authorization=d.get('authorization', None),
                   enable_ssl_verification=d.get('enable_ssl_verification', None),
                   secret=d.get('secret', None),
                   url=d.get('url', None))


@dataclass
class HttpUrlSpecWithoutSecret:
    enable_ssl_verification: Optional[bool] = None
    url: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.enable_ssl_verification is not None:
            body['enable_ssl_verification'] = self.enable_ssl_verification
        if self.url is not None: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'HttpUrlSpecWithoutSecret':
        return cls(enable_ssl_verification=d.get('enable_ssl_verification', None), url=d.get('url', None))


@dataclass
class InputTag:
    key: Optional[str] = None
    value: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InputTag':
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class JobSpec:
    job_id: str
    access_token: str
    workspace_url: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_token is not None: body['access_token'] = self.access_token
        if self.job_id is not None: body['job_id'] = self.job_id
        if self.workspace_url is not None: body['workspace_url'] = self.workspace_url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobSpec':
        return cls(access_token=d.get('access_token', None),
                   job_id=d.get('job_id', None),
                   workspace_url=d.get('workspace_url', None))


@dataclass
class JobSpecWithoutSecret:
    job_id: Optional[str] = None
    workspace_url: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.job_id is not None: body['job_id'] = self.job_id
        if self.workspace_url is not None: body['workspace_url'] = self.workspace_url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobSpecWithoutSecret':
        return cls(job_id=d.get('job_id', None), workspace_url=d.get('workspace_url', None))


@dataclass
class ListArtifactsRequest:
    """Get all artifacts"""

    page_token: Optional[str] = None
    path: Optional[str] = None
    run_id: Optional[str] = None
    run_uuid: Optional[str] = None


@dataclass
class ListArtifactsResponse:
    files: Optional['List[FileInfo]'] = None
    next_page_token: Optional[str] = None
    root_uri: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.files: body['files'] = [v.as_dict() for v in self.files]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.root_uri is not None: body['root_uri'] = self.root_uri
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListArtifactsResponse':
        return cls(files=_repeated(d, 'files', FileInfo),
                   next_page_token=d.get('next_page_token', None),
                   root_uri=d.get('root_uri', None))


@dataclass
class ListExperimentsRequest:
    """List experiments"""

    max_results: Optional[int] = None
    page_token: Optional[str] = None
    view_type: Optional[str] = None


@dataclass
class ListExperimentsResponse:
    experiments: Optional['List[Experiment]'] = None
    next_page_token: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.experiments: body['experiments'] = [v.as_dict() for v in self.experiments]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListExperimentsResponse':
        return cls(experiments=_repeated(d, 'experiments', Experiment),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListModelsRequest:
    """List models"""

    max_results: Optional[int] = None
    page_token: Optional[str] = None


@dataclass
class ListModelsResponse:
    next_page_token: Optional[str] = None
    registered_models: Optional['List[Model]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.registered_models: body['registered_models'] = [v.as_dict() for v in self.registered_models]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListModelsResponse':
        return cls(next_page_token=d.get('next_page_token', None),
                   registered_models=_repeated(d, 'registered_models', Model))


@dataclass
class ListRegistryWebhooks:
    next_page_token: Optional[str] = None
    webhooks: Optional['List[RegistryWebhook]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.webhooks: body['webhooks'] = [v.as_dict() for v in self.webhooks]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRegistryWebhooks':
        return cls(next_page_token=d.get('next_page_token', None),
                   webhooks=_repeated(d, 'webhooks', RegistryWebhook))


@dataclass
class ListTransitionRequestsRequest:
    """List transition requests"""

    name: str
    version: str


@dataclass
class ListTransitionRequestsResponse:
    requests: Optional['List[Activity]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.requests: body['requests'] = [v.as_dict() for v in self.requests]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListTransitionRequestsResponse':
        return cls(requests=_repeated(d, 'requests', Activity))


@dataclass
class ListWebhooksRequest:
    """List registry webhooks"""

    events: Optional['List[RegistryWebhookEvent]'] = None
    model_name: Optional[str] = None
    page_token: Optional[str] = None


@dataclass
class LogBatch:
    metrics: Optional['List[Metric]'] = None
    params: Optional['List[Param]'] = None
    run_id: Optional[str] = None
    tags: Optional['List[RunTag]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.metrics: body['metrics'] = [v.as_dict() for v in self.metrics]
        if self.params: body['params'] = [v.as_dict() for v in self.params]
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogBatch':
        return cls(metrics=_repeated(d, 'metrics', Metric),
                   params=_repeated(d, 'params', Param),
                   run_id=d.get('run_id', None),
                   tags=_repeated(d, 'tags', RunTag))


@dataclass
class LogInputs:
    datasets: Optional['List[DatasetInput]'] = None
    run_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.datasets: body['datasets'] = [v.as_dict() for v in self.datasets]
        if self.run_id is not None: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogInputs':
        return cls(datasets=_repeated(d, 'datasets', DatasetInput), run_id=d.get('run_id', None))


@dataclass
class LogMetric:
    key: str
    value: float
    timestamp: int
    run_id: Optional[str] = None
    run_uuid: Optional[str] = None
    step: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.run_uuid is not None: body['run_uuid'] = self.run_uuid
        if self.step is not None: body['step'] = self.step
        if self.timestamp is not None: body['timestamp'] = self.timestamp
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogMetric':
        return cls(key=d.get('key', None),
                   run_id=d.get('run_id', None),
                   run_uuid=d.get('run_uuid', None),
                   step=d.get('step', None),
                   timestamp=d.get('timestamp', None),
                   value=d.get('value', None))


@dataclass
class LogModel:
    model_json: Optional[str] = None
    run_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.model_json is not None: body['model_json'] = self.model_json
        if self.run_id is not None: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogModel':
        return cls(model_json=d.get('model_json', None), run_id=d.get('run_id', None))


@dataclass
class LogParam:
    key: str
    value: str
    run_id: Optional[str] = None
    run_uuid: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.run_uuid is not None: body['run_uuid'] = self.run_uuid
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogParam':
        return cls(key=d.get('key', None),
                   run_id=d.get('run_id', None),
                   run_uuid=d.get('run_uuid', None),
                   value=d.get('value', None))


@dataclass
class Metric:
    key: Optional[str] = None
    step: Optional[int] = None
    timestamp: Optional[int] = None
    value: Optional[float] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.step is not None: body['step'] = self.step
        if self.timestamp is not None: body['timestamp'] = self.timestamp
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Metric':
        return cls(key=d.get('key', None),
                   step=d.get('step', None),
                   timestamp=d.get('timestamp', None),
                   value=d.get('value', None))


@dataclass
class Model:
    creation_timestamp: Optional[int] = None
    description: Optional[str] = None
    last_updated_timestamp: Optional[int] = None
    latest_versions: Optional['List[ModelVersion]'] = None
    name: Optional[str] = None
    tags: Optional['List[ModelTag]'] = None
    user_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.description is not None: body['description'] = self.description
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.latest_versions: body['latest_versions'] = [v.as_dict() for v in self.latest_versions]
        if self.name is not None: body['name'] = self.name
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Model':
        return cls(creation_timestamp=d.get('creation_timestamp', None),
                   description=d.get('description', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   latest_versions=_repeated(d, 'latest_versions', ModelVersion),
                   name=d.get('name', None),
                   tags=_repeated(d, 'tags', ModelTag),
                   user_id=d.get('user_id', None))


@dataclass
class ModelDatabricks:
    creation_timestamp: Optional[int] = None
    description: Optional[str] = None
    id: Optional[str] = None
    last_updated_timestamp: Optional[int] = None
    latest_versions: Optional['List[ModelVersion]'] = None
    name: Optional[str] = None
    permission_level: Optional['PermissionLevel'] = None
    tags: Optional['List[ModelTag]'] = None
    user_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.description is not None: body['description'] = self.description
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.latest_versions: body['latest_versions'] = [v.as_dict() for v in self.latest_versions]
        if self.name is not None: body['name'] = self.name
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ModelDatabricks':
        return cls(creation_timestamp=d.get('creation_timestamp', None),
                   description=d.get('description', None),
                   id=d.get('id', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   latest_versions=_repeated(d, 'latest_versions', ModelVersion),
                   name=d.get('name', None),
                   permission_level=_enum(d, 'permission_level', PermissionLevel),
                   tags=_repeated(d, 'tags', ModelTag),
                   user_id=d.get('user_id', None))


@dataclass
class ModelTag:
    key: Optional[str] = None
    value: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ModelTag':
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class ModelVersion:
    creation_timestamp: Optional[int] = None
    current_stage: Optional[str] = None
    description: Optional[str] = None
    last_updated_timestamp: Optional[int] = None
    name: Optional[str] = None
    run_id: Optional[str] = None
    run_link: Optional[str] = None
    source: Optional[str] = None
    status: Optional['ModelVersionStatus'] = None
    status_message: Optional[str] = None
    tags: Optional['List[ModelVersionTag]'] = None
    user_id: Optional[str] = None
    version: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.current_stage is not None: body['current_stage'] = self.current_stage
        if self.description is not None: body['description'] = self.description
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.name is not None: body['name'] = self.name
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.run_link is not None: body['run_link'] = self.run_link
        if self.source is not None: body['source'] = self.source
        if self.status is not None: body['status'] = self.status.value
        if self.status_message is not None: body['status_message'] = self.status_message
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        if self.user_id is not None: body['user_id'] = self.user_id
        if self.version is not None: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ModelVersion':
        return cls(creation_timestamp=d.get('creation_timestamp', None),
                   current_stage=d.get('current_stage', None),
                   description=d.get('description', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   name=d.get('name', None),
                   run_id=d.get('run_id', None),
                   run_link=d.get('run_link', None),
                   source=d.get('source', None),
                   status=_enum(d, 'status', ModelVersionStatus),
                   status_message=d.get('status_message', None),
                   tags=_repeated(d, 'tags', ModelVersionTag),
                   user_id=d.get('user_id', None),
                   version=d.get('version', None))


@dataclass
class ModelVersionDatabricks:
    creation_timestamp: Optional[int] = None
    current_stage: Optional['Stage'] = None
    description: Optional[str] = None
    last_updated_timestamp: Optional[int] = None
    name: Optional[str] = None
    permission_level: Optional['PermissionLevel'] = None
    run_id: Optional[str] = None
    run_link: Optional[str] = None
    source: Optional[str] = None
    status: Optional['Status'] = None
    status_message: Optional[str] = None
    tags: Optional['List[ModelVersionTag]'] = None
    user_id: Optional[str] = None
    version: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.current_stage is not None: body['current_stage'] = self.current_stage.value
        if self.description is not None: body['description'] = self.description
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.name is not None: body['name'] = self.name
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.run_link is not None: body['run_link'] = self.run_link
        if self.source is not None: body['source'] = self.source
        if self.status is not None: body['status'] = self.status.value
        if self.status_message is not None: body['status_message'] = self.status_message
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        if self.user_id is not None: body['user_id'] = self.user_id
        if self.version is not None: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ModelVersionDatabricks':
        return cls(creation_timestamp=d.get('creation_timestamp', None),
                   current_stage=_enum(d, 'current_stage', Stage),
                   description=d.get('description', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   name=d.get('name', None),
                   permission_level=_enum(d, 'permission_level', PermissionLevel),
                   run_id=d.get('run_id', None),
                   run_link=d.get('run_link', None),
                   source=d.get('source', None),
                   status=_enum(d, 'status', Status),
                   status_message=d.get('status_message', None),
                   tags=_repeated(d, 'tags', ModelVersionTag),
                   user_id=d.get('user_id', None),
                   version=d.get('version', None))


class ModelVersionStatus(Enum):
    """Current status of `model_version`"""

    FAILED_REGISTRATION = 'FAILED_REGISTRATION'
    PENDING_REGISTRATION = 'PENDING_REGISTRATION'
    READY = 'READY'


@dataclass
class ModelVersionTag:
    key: Optional[str] = None
    value: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ModelVersionTag':
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class Param:
    key: Optional[str] = None
    value: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Param':
        return cls(key=d.get('key', None), value=d.get('value', None))


class PermissionLevel(Enum):
    """Permission level of the requesting user on the object. For what is allowed at each level, see
    [MLflow Model permissions](..)."""

    CAN_EDIT = 'CAN_EDIT'
    CAN_MANAGE = 'CAN_MANAGE'
    CAN_MANAGE_PRODUCTION_VERSIONS = 'CAN_MANAGE_PRODUCTION_VERSIONS'
    CAN_MANAGE_STAGING_VERSIONS = 'CAN_MANAGE_STAGING_VERSIONS'
    CAN_READ = 'CAN_READ'


@dataclass
class RegistryWebhook:
    creation_timestamp: Optional[int] = None
    description: Optional[str] = None
    events: Optional['List[RegistryWebhookEvent]'] = None
    http_url_spec: Optional['HttpUrlSpecWithoutSecret'] = None
    id: Optional[str] = None
    job_spec: Optional['JobSpecWithoutSecret'] = None
    last_updated_timestamp: Optional[int] = None
    model_name: Optional[str] = None
    status: Optional['RegistryWebhookStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.description is not None: body['description'] = self.description
        if self.events: body['events'] = [v.value for v in self.events]
        if self.http_url_spec: body['http_url_spec'] = self.http_url_spec.as_dict()
        if self.id is not None: body['id'] = self.id
        if self.job_spec: body['job_spec'] = self.job_spec.as_dict()
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.model_name is not None: body['model_name'] = self.model_name
        if self.status is not None: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RegistryWebhook':
        return cls(creation_timestamp=d.get('creation_timestamp', None),
                   description=d.get('description', None),
                   events=d.get('events', None),
                   http_url_spec=_from_dict(d, 'http_url_spec', HttpUrlSpecWithoutSecret),
                   id=d.get('id', None),
                   job_spec=_from_dict(d, 'job_spec', JobSpecWithoutSecret),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   model_name=d.get('model_name', None),
                   status=_enum(d, 'status', RegistryWebhookStatus))


class RegistryWebhookEvent(Enum):

    COMMENT_CREATED = 'COMMENT_CREATED'
    MODEL_VERSION_CREATED = 'MODEL_VERSION_CREATED'
    MODEL_VERSION_TAG_SET = 'MODEL_VERSION_TAG_SET'
    MODEL_VERSION_TRANSITIONED_STAGE = 'MODEL_VERSION_TRANSITIONED_STAGE'
    MODEL_VERSION_TRANSITIONED_TO_ARCHIVED = 'MODEL_VERSION_TRANSITIONED_TO_ARCHIVED'
    MODEL_VERSION_TRANSITIONED_TO_PRODUCTION = 'MODEL_VERSION_TRANSITIONED_TO_PRODUCTION'
    MODEL_VERSION_TRANSITIONED_TO_STAGING = 'MODEL_VERSION_TRANSITIONED_TO_STAGING'
    REGISTERED_MODEL_CREATED = 'REGISTERED_MODEL_CREATED'
    TRANSITION_REQUEST_CREATED = 'TRANSITION_REQUEST_CREATED'
    TRANSITION_REQUEST_TO_ARCHIVED_CREATED = 'TRANSITION_REQUEST_TO_ARCHIVED_CREATED'
    TRANSITION_REQUEST_TO_PRODUCTION_CREATED = 'TRANSITION_REQUEST_TO_PRODUCTION_CREATED'
    TRANSITION_REQUEST_TO_STAGING_CREATED = 'TRANSITION_REQUEST_TO_STAGING_CREATED'


class RegistryWebhookStatus(Enum):
    """This describes an enum"""

    ACTIVE = 'ACTIVE'
    DISABLED = 'DISABLED'
    TEST_MODE = 'TEST_MODE'


@dataclass
class RejectTransitionRequest:
    name: str
    version: str
    stage: 'Stage'
    comment: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        if self.stage is not None: body['stage'] = self.stage.value
        if self.version is not None: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RejectTransitionRequest':
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   stage=_enum(d, 'stage', Stage),
                   version=d.get('version', None))


@dataclass
class RejectTransitionRequestResponse:
    activity: Optional['Activity'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.activity: body['activity'] = self.activity.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RejectTransitionRequestResponse':
        return cls(activity=_from_dict(d, 'activity', Activity))


@dataclass
class RenameModelRequest:
    name: str
    new_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.new_name is not None: body['new_name'] = self.new_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RenameModelRequest':
        return cls(name=d.get('name', None), new_name=d.get('new_name', None))


@dataclass
class RenameModelResponse:
    registered_model: Optional['Model'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.registered_model: body['registered_model'] = self.registered_model.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RenameModelResponse':
        return cls(registered_model=_from_dict(d, 'registered_model', Model))


@dataclass
class RestoreExperiment:
    experiment_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.experiment_id is not None: body['experiment_id'] = self.experiment_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RestoreExperiment':
        return cls(experiment_id=d.get('experiment_id', None))


@dataclass
class RestoreRun:
    run_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.run_id is not None: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RestoreRun':
        return cls(run_id=d.get('run_id', None))


@dataclass
class Run:
    data: Optional['RunData'] = None
    info: Optional['RunInfo'] = None
    inputs: Optional['RunInputs'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.data: body['data'] = self.data.as_dict()
        if self.info: body['info'] = self.info.as_dict()
        if self.inputs: body['inputs'] = self.inputs.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Run':
        return cls(data=_from_dict(d, 'data', RunData),
                   info=_from_dict(d, 'info', RunInfo),
                   inputs=_from_dict(d, 'inputs', RunInputs))


@dataclass
class RunData:
    metrics: Optional['List[Metric]'] = None
    params: Optional['List[Param]'] = None
    tags: Optional['List[RunTag]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.metrics: body['metrics'] = [v.as_dict() for v in self.metrics]
        if self.params: body['params'] = [v.as_dict() for v in self.params]
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunData':
        return cls(metrics=_repeated(d, 'metrics', Metric),
                   params=_repeated(d, 'params', Param),
                   tags=_repeated(d, 'tags', RunTag))


@dataclass
class RunInfo:
    artifact_uri: Optional[str] = None
    end_time: Optional[int] = None
    experiment_id: Optional[str] = None
    lifecycle_stage: Optional[str] = None
    run_id: Optional[str] = None
    run_uuid: Optional[str] = None
    start_time: Optional[int] = None
    status: Optional['RunInfoStatus'] = None
    user_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.artifact_uri is not None: body['artifact_uri'] = self.artifact_uri
        if self.end_time is not None: body['end_time'] = self.end_time
        if self.experiment_id is not None: body['experiment_id'] = self.experiment_id
        if self.lifecycle_stage is not None: body['lifecycle_stage'] = self.lifecycle_stage
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.run_uuid is not None: body['run_uuid'] = self.run_uuid
        if self.start_time is not None: body['start_time'] = self.start_time
        if self.status is not None: body['status'] = self.status.value
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunInfo':
        return cls(artifact_uri=d.get('artifact_uri', None),
                   end_time=d.get('end_time', None),
                   experiment_id=d.get('experiment_id', None),
                   lifecycle_stage=d.get('lifecycle_stage', None),
                   run_id=d.get('run_id', None),
                   run_uuid=d.get('run_uuid', None),
                   start_time=d.get('start_time', None),
                   status=_enum(d, 'status', RunInfoStatus),
                   user_id=d.get('user_id', None))


class RunInfoStatus(Enum):
    """Current status of the run."""

    FAILED = 'FAILED'
    FINISHED = 'FINISHED'
    KILLED = 'KILLED'
    RUNNING = 'RUNNING'
    SCHEDULED = 'SCHEDULED'


@dataclass
class RunInputs:
    dataset_inputs: Optional['List[DatasetInput]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.dataset_inputs: body['dataset_inputs'] = [v.as_dict() for v in self.dataset_inputs]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunInputs':
        return cls(dataset_inputs=_repeated(d, 'dataset_inputs', DatasetInput))


@dataclass
class RunTag:
    key: Optional[str] = None
    value: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunTag':
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class SearchExperiments:
    filter: Optional[str] = None
    max_results: Optional[int] = None
    order_by: Optional['List[str]'] = None
    page_token: Optional[str] = None
    view_type: Optional['SearchExperimentsViewType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.filter is not None: body['filter'] = self.filter
        if self.max_results is not None: body['max_results'] = self.max_results
        if self.order_by: body['order_by'] = [v for v in self.order_by]
        if self.page_token is not None: body['page_token'] = self.page_token
        if self.view_type is not None: body['view_type'] = self.view_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SearchExperiments':
        return cls(filter=d.get('filter', None),
                   max_results=d.get('max_results', None),
                   order_by=d.get('order_by', None),
                   page_token=d.get('page_token', None),
                   view_type=_enum(d, 'view_type', SearchExperimentsViewType))


@dataclass
class SearchExperimentsResponse:
    experiments: Optional['List[Experiment]'] = None
    next_page_token: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.experiments: body['experiments'] = [v.as_dict() for v in self.experiments]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SearchExperimentsResponse':
        return cls(experiments=_repeated(d, 'experiments', Experiment),
                   next_page_token=d.get('next_page_token', None))


class SearchExperimentsViewType(Enum):
    """Qualifier for type of experiments to be returned. If unspecified, return only active
    experiments."""

    ACTIVE_ONLY = 'ACTIVE_ONLY'
    ALL = 'ALL'
    DELETED_ONLY = 'DELETED_ONLY'


@dataclass
class SearchModelVersionsRequest:
    """Searches model versions"""

    filter: Optional[str] = None
    max_results: Optional[int] = None
    order_by: Optional['List[str]'] = None
    page_token: Optional[str] = None


@dataclass
class SearchModelVersionsResponse:
    model_versions: Optional['List[ModelVersion]'] = None
    next_page_token: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.model_versions: body['model_versions'] = [v.as_dict() for v in self.model_versions]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SearchModelVersionsResponse':
        return cls(model_versions=_repeated(d, 'model_versions', ModelVersion),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class SearchModelsRequest:
    """Search models"""

    filter: Optional[str] = None
    max_results: Optional[int] = None
    order_by: Optional['List[str]'] = None
    page_token: Optional[str] = None


@dataclass
class SearchModelsResponse:
    next_page_token: Optional[str] = None
    registered_models: Optional['List[Model]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.registered_models: body['registered_models'] = [v.as_dict() for v in self.registered_models]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SearchModelsResponse':
        return cls(next_page_token=d.get('next_page_token', None),
                   registered_models=_repeated(d, 'registered_models', Model))


@dataclass
class SearchRuns:
    experiment_ids: Optional['List[str]'] = None
    filter: Optional[str] = None
    max_results: Optional[int] = None
    order_by: Optional['List[str]'] = None
    page_token: Optional[str] = None
    run_view_type: Optional['SearchRunsRunViewType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.experiment_ids: body['experiment_ids'] = [v for v in self.experiment_ids]
        if self.filter is not None: body['filter'] = self.filter
        if self.max_results is not None: body['max_results'] = self.max_results
        if self.order_by: body['order_by'] = [v for v in self.order_by]
        if self.page_token is not None: body['page_token'] = self.page_token
        if self.run_view_type is not None: body['run_view_type'] = self.run_view_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SearchRuns':
        return cls(experiment_ids=d.get('experiment_ids', None),
                   filter=d.get('filter', None),
                   max_results=d.get('max_results', None),
                   order_by=d.get('order_by', None),
                   page_token=d.get('page_token', None),
                   run_view_type=_enum(d, 'run_view_type', SearchRunsRunViewType))


@dataclass
class SearchRunsResponse:
    next_page_token: Optional[str] = None
    runs: Optional['List[Run]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.runs: body['runs'] = [v.as_dict() for v in self.runs]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SearchRunsResponse':
        return cls(next_page_token=d.get('next_page_token', None), runs=_repeated(d, 'runs', Run))


class SearchRunsRunViewType(Enum):
    """Whether to display only active, only deleted, or all runs. Defaults to only active runs."""

    ACTIVE_ONLY = 'ACTIVE_ONLY'
    ALL = 'ALL'
    DELETED_ONLY = 'DELETED_ONLY'


@dataclass
class SetExperimentTag:
    experiment_id: str
    key: str
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.experiment_id is not None: body['experiment_id'] = self.experiment_id
        if self.key is not None: body['key'] = self.key
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetExperimentTag':
        return cls(experiment_id=d.get('experiment_id', None),
                   key=d.get('key', None),
                   value=d.get('value', None))


@dataclass
class SetModelTagRequest:
    name: str
    key: str
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.name is not None: body['name'] = self.name
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetModelTagRequest':
        return cls(key=d.get('key', None), name=d.get('name', None), value=d.get('value', None))


@dataclass
class SetModelVersionTagRequest:
    name: str
    version: str
    key: str
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.name is not None: body['name'] = self.name
        if self.value is not None: body['value'] = self.value
        if self.version is not None: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetModelVersionTagRequest':
        return cls(key=d.get('key', None),
                   name=d.get('name', None),
                   value=d.get('value', None),
                   version=d.get('version', None))


@dataclass
class SetTag:
    key: str
    value: str
    run_id: Optional[str] = None
    run_uuid: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.run_uuid is not None: body['run_uuid'] = self.run_uuid
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetTag':
        return cls(key=d.get('key', None),
                   run_id=d.get('run_id', None),
                   run_uuid=d.get('run_uuid', None),
                   value=d.get('value', None))


class Stage(Enum):
    """This describes an enum"""

    ARCHIVED = 'Archived'
    NONE = 'None'
    PRODUCTION = 'Production'
    STAGING = 'Staging'


class Status(Enum):
    """This describes an enum"""

    FAILED_REGISTRATION = 'FAILED_REGISTRATION'
    PENDING_REGISTRATION = 'PENDING_REGISTRATION'
    READY = 'READY'


@dataclass
class TestRegistryWebhook:
    """Test webhook response object."""

    body: Optional[str] = None
    status_code: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.body is not None: body['body'] = self.body
        if self.status_code is not None: body['status_code'] = self.status_code
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TestRegistryWebhook':
        return cls(body=d.get('body', None), status_code=d.get('status_code', None))


@dataclass
class TestRegistryWebhookRequest:
    id: str
    event: Optional['RegistryWebhookEvent'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.event is not None: body['event'] = self.event.value
        if self.id is not None: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TestRegistryWebhookRequest':
        return cls(event=_enum(d, 'event', RegistryWebhookEvent), id=d.get('id', None))


@dataclass
class TestRegistryWebhookResponse:
    webhook: Optional['TestRegistryWebhook'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.webhook: body['webhook'] = self.webhook.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TestRegistryWebhookResponse':
        return cls(webhook=_from_dict(d, 'webhook', TestRegistryWebhook))


@dataclass
class TransitionModelVersionStageDatabricks:
    name: str
    version: str
    stage: 'Stage'
    archive_existing_versions: bool
    comment: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.archive_existing_versions is not None:
            body['archive_existing_versions'] = self.archive_existing_versions
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        if self.stage is not None: body['stage'] = self.stage.value
        if self.version is not None: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TransitionModelVersionStageDatabricks':
        return cls(archive_existing_versions=d.get('archive_existing_versions', None),
                   comment=d.get('comment', None),
                   name=d.get('name', None),
                   stage=_enum(d, 'stage', Stage),
                   version=d.get('version', None))


@dataclass
class TransitionRequest:
    """Transition request details."""

    available_actions: Optional['List[ActivityAction]'] = None
    comment: Optional[str] = None
    creation_timestamp: Optional[int] = None
    to_stage: Optional['Stage'] = None
    user_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.available_actions: body['available_actions'] = [v.value for v in self.available_actions]
        if self.comment is not None: body['comment'] = self.comment
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.to_stage is not None: body['to_stage'] = self.to_stage.value
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TransitionRequest':
        return cls(available_actions=d.get('available_actions', None),
                   comment=d.get('comment', None),
                   creation_timestamp=d.get('creation_timestamp', None),
                   to_stage=_enum(d, 'to_stage', Stage),
                   user_id=d.get('user_id', None))


@dataclass
class TransitionStageResponse:
    model_version: Optional['ModelVersionDatabricks'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.model_version: body['model_version'] = self.model_version.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TransitionStageResponse':
        return cls(model_version=_from_dict(d, 'model_version', ModelVersionDatabricks))


@dataclass
class UpdateComment:
    id: str
    comment: str

    def as_dict(self) -> dict:
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.id is not None: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateComment':
        return cls(comment=d.get('comment', None), id=d.get('id', None))


@dataclass
class UpdateCommentResponse:
    comment: Optional['CommentObject'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateCommentResponse':
        return cls(comment=_from_dict(d, 'comment', CommentObject))


@dataclass
class UpdateExperiment:
    experiment_id: str
    new_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.experiment_id is not None: body['experiment_id'] = self.experiment_id
        if self.new_name is not None: body['new_name'] = self.new_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateExperiment':
        return cls(experiment_id=d.get('experiment_id', None), new_name=d.get('new_name', None))


@dataclass
class UpdateModelRequest:
    name: str
    description: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateModelRequest':
        return cls(description=d.get('description', None), name=d.get('name', None))


@dataclass
class UpdateModelVersionRequest:
    name: str
    version: str
    description: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.name is not None: body['name'] = self.name
        if self.version is not None: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateModelVersionRequest':
        return cls(description=d.get('description', None),
                   name=d.get('name', None),
                   version=d.get('version', None))


@dataclass
class UpdateRegistryWebhook:
    id: str
    description: Optional[str] = None
    events: Optional['List[RegistryWebhookEvent]'] = None
    http_url_spec: Optional['HttpUrlSpec'] = None
    job_spec: Optional['JobSpec'] = None
    status: Optional['RegistryWebhookStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.events: body['events'] = [v.value for v in self.events]
        if self.http_url_spec: body['http_url_spec'] = self.http_url_spec.as_dict()
        if self.id is not None: body['id'] = self.id
        if self.job_spec: body['job_spec'] = self.job_spec.as_dict()
        if self.status is not None: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateRegistryWebhook':
        return cls(description=d.get('description', None),
                   events=d.get('events', None),
                   http_url_spec=_from_dict(d, 'http_url_spec', HttpUrlSpec),
                   id=d.get('id', None),
                   job_spec=_from_dict(d, 'job_spec', JobSpec),
                   status=_enum(d, 'status', RegistryWebhookStatus))


@dataclass
class UpdateRun:
    end_time: Optional[int] = None
    run_id: Optional[str] = None
    run_uuid: Optional[str] = None
    status: Optional['UpdateRunStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.end_time is not None: body['end_time'] = self.end_time
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.run_uuid is not None: body['run_uuid'] = self.run_uuid
        if self.status is not None: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateRun':
        return cls(end_time=d.get('end_time', None),
                   run_id=d.get('run_id', None),
                   run_uuid=d.get('run_uuid', None),
                   status=_enum(d, 'status', UpdateRunStatus))


@dataclass
class UpdateRunResponse:
    run_info: Optional['RunInfo'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.run_info: body['run_info'] = self.run_info.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateRunResponse':
        return cls(run_info=_from_dict(d, 'run_info', RunInfo))


class UpdateRunStatus(Enum):
    """Updated status of the run."""

    FAILED = 'FAILED'
    FINISHED = 'FINISHED'
    KILLED = 'KILLED'
    RUNNING = 'RUNNING'
    SCHEDULED = 'SCHEDULED'


class ExperimentsAPI:
    """Experiments are the primary unit of organization in MLflow; all MLflow runs belong to an experiment. Each
    experiment lets you visualize, search, and compare runs, as well as download run artifacts or metadata for
    analysis in other tools. Experiments are maintained in a Databricks hosted MLflow tracking server.
    
    Experiments are located in the workspace file tree. You manage experiments using the same tools you use to
    manage other workspace objects such as folders, notebooks, and libraries."""

    def __init__(self, api_client):
        self._api = api_client

    def create_experiment(self,
                          name: str,
                          *,
                          artifact_location: Optional[str] = None,
                          tags: Optional[List[ExperimentTag]] = None,
                          **kwargs) -> CreateExperimentResponse:
        """Create experiment.
        
        Creates an experiment with a name. Returns the ID of the newly created experiment. Validates that
        another experiment with the same name does not already exist and fails if another experiment with the
        same name already exists.
        
        Throws `RESOURCE_ALREADY_EXISTS` if a experiment with the given name exists.
        
        :param name: str
          Experiment name.
        :param artifact_location: str (optional)
          Location where all artifacts for the experiment are stored. If not provided, the remote server will
          select an appropriate default.
        :param tags: List[:class:`ExperimentTag`] (optional)
          A collection of tags to set on the experiment. Maximum tag size and number of tags per request
          depends on the storage backend. All storage backends are guaranteed to support tag keys up to 250
          bytes in size and tag values up to 5000 bytes in size. All storage backends are also guaranteed to
          support up to 20 tags per request.
        
        :returns: :class:`CreateExperimentResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateExperiment(artifact_location=artifact_location, name=name, tags=tags)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/experiments/create', body=body)
        return CreateExperimentResponse.from_dict(json)

    def create_run(self,
                   *,
                   experiment_id: Optional[str] = None,
                   start_time: Optional[int] = None,
                   tags: Optional[List[RunTag]] = None,
                   user_id: Optional[str] = None,
                   **kwargs) -> CreateRunResponse:
        """Create a run.
        
        Creates a new run within an experiment. A run is usually a single execution of a machine learning or
        data ETL pipeline. MLflow uses runs to track the `mlflowParam`, `mlflowMetric` and `mlflowRunTag`
        associated with a single execution.
        
        :param experiment_id: str (optional)
          ID of the associated experiment.
        :param start_time: int (optional)
          Unix timestamp in milliseconds of when the run started.
        :param tags: List[:class:`RunTag`] (optional)
          Additional metadata for run.
        :param user_id: str (optional)
          ID of the user executing the run. This field is deprecated as of MLflow 1.0, and will be removed in
          a future MLflow release. Use 'mlflow.user' tag instead.
        
        :returns: :class:`CreateRunResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateRun(experiment_id=experiment_id,
                                start_time=start_time,
                                tags=tags,
                                user_id=user_id)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/runs/create', body=body)
        return CreateRunResponse.from_dict(json)

    def delete_experiment(self, experiment_id: str, **kwargs):
        """Delete an experiment.
        
        Marks an experiment and associated metadata, runs, metrics, params, and tags for deletion. If the
        experiment uses FileStore, artifacts associated with experiment are also deleted.
        
        :param experiment_id: str
          ID of the associated experiment.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteExperiment(experiment_id=experiment_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/experiments/delete', body=body)

    def delete_run(self, run_id: str, **kwargs):
        """Delete a run.
        
        Marks a run for deletion.
        
        :param run_id: str
          ID of the run to delete.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteRun(run_id=run_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/delete', body=body)

    def delete_tag(self, run_id: str, key: str, **kwargs):
        """Delete a tag.
        
        Deletes a tag on a run. Tags are run metadata that can be updated during a run and after a run
        completes.
        
        :param run_id: str
          ID of the run that the tag was logged under. Must be provided.
        :param key: str
          Name of the tag. Maximum size is 255 bytes. Must be provided.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteTag(key=key, run_id=run_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/delete-tag', body=body)

    def get_by_name(self, experiment_name: str, **kwargs) -> GetExperimentByNameResponse:
        """Get metadata.
        
        Gets metadata for an experiment.
        
        This endpoint will return deleted experiments, but prefers the active experiment if an active and
        deleted experiment share the same name. If multiple deleted experiments share the same name, the API
        will return one of them.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no experiment with the specified name exists.
        
        :param experiment_name: str
          Name of the associated experiment.
        
        :returns: :class:`GetExperimentByNameResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetByNameRequest(experiment_name=experiment_name)

        query = {}
        if experiment_name: query['experiment_name'] = request.experiment_name

        json = self._api.do('GET', '/api/2.0/mlflow/experiments/get-by-name', query=query)
        return GetExperimentByNameResponse.from_dict(json)

    def get_experiment(self, experiment_id: str, **kwargs) -> Experiment:
        """Get an experiment.
        
        Gets metadata for an experiment. This method works on deleted experiments.
        
        :param experiment_id: str
          ID of the associated experiment.
        
        :returns: :class:`Experiment`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetExperimentRequest(experiment_id=experiment_id)

        query = {}
        if experiment_id: query['experiment_id'] = request.experiment_id

        json = self._api.do('GET', '/api/2.0/mlflow/experiments/get', query=query)
        return Experiment.from_dict(json)

    def get_history(self,
                    metric_key: str,
                    *,
                    max_results: Optional[int] = None,
                    page_token: Optional[str] = None,
                    run_id: Optional[str] = None,
                    run_uuid: Optional[str] = None,
                    **kwargs) -> GetMetricHistoryResponse:
        """Get history of a given metric within a run.
        
        Gets a list of all values for the specified metric for a given run.
        
        :param metric_key: str
          Name of the metric.
        :param max_results: int (optional)
          Maximum number of Metric records to return per paginated request. Default is set to 25,000. If set
          higher than 25,000, a request Exception will be raised.
        :param page_token: str (optional)
          Token indicating the page of metric histories to fetch.
        :param run_id: str (optional)
          ID of the run from which to fetch metric values. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run from which to fetch metric values. This field will be
          removed in a future MLflow version.
        
        :returns: :class:`GetMetricHistoryResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetHistoryRequest(max_results=max_results,
                                        metric_key=metric_key,
                                        page_token=page_token,
                                        run_id=run_id,
                                        run_uuid=run_uuid)

        query = {}
        if max_results: query['max_results'] = request.max_results
        if metric_key: query['metric_key'] = request.metric_key
        if page_token: query['page_token'] = request.page_token
        if run_id: query['run_id'] = request.run_id
        if run_uuid: query['run_uuid'] = request.run_uuid

        json = self._api.do('GET', '/api/2.0/mlflow/metrics/get-history', query=query)
        return GetMetricHistoryResponse.from_dict(json)

    def get_run(self, run_id: str, *, run_uuid: Optional[str] = None, **kwargs) -> GetRunResponse:
        """Get a run.
        
        Gets the metadata, metrics, params, and tags for a run. In the case where multiple metrics with the
        same key are logged for a run, return only the value with the latest timestamp.
        
        If there are multiple values with the latest timestamp, return the maximum of these values.
        
        :param run_id: str
          ID of the run to fetch. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run to fetch. This field will be removed in a future
          MLflow version.
        
        :returns: :class:`GetRunResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetRunRequest(run_id=run_id, run_uuid=run_uuid)

        query = {}
        if run_id: query['run_id'] = request.run_id
        if run_uuid: query['run_uuid'] = request.run_uuid

        json = self._api.do('GET', '/api/2.0/mlflow/runs/get', query=query)
        return GetRunResponse.from_dict(json)

    def list_artifacts(self,
                       *,
                       page_token: Optional[str] = None,
                       path: Optional[str] = None,
                       run_id: Optional[str] = None,
                       run_uuid: Optional[str] = None,
                       **kwargs) -> Iterator[FileInfo]:
        """Get all artifacts.
        
        List artifacts for a run. Takes an optional `artifact_path` prefix. If it is specified, the response
        contains only artifacts with the specified prefix.",
        
        :param page_token: str (optional)
          Token indicating the page of artifact results to fetch
        :param path: str (optional)
          Filter artifacts matching this path (a relative path from the root artifact directory).
        :param run_id: str (optional)
          ID of the run whose artifacts to list. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run whose artifacts to list. This field will be removed
          in a future MLflow version.
        
        :returns: Iterator over :class:`FileInfo`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListArtifactsRequest(page_token=page_token, path=path, run_id=run_id, run_uuid=run_uuid)

        query = {}
        if page_token: query['page_token'] = request.page_token
        if path: query['path'] = request.path
        if run_id: query['run_id'] = request.run_id
        if run_uuid: query['run_uuid'] = request.run_uuid

        while True:
            json = self._api.do('GET', '/api/2.0/mlflow/artifacts/list', query=query)
            if 'files' not in json or not json['files']:
                return
            for v in json['files']:
                yield FileInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def list_experiments(self,
                         *,
                         max_results: Optional[int] = None,
                         page_token: Optional[str] = None,
                         view_type: Optional[str] = None,
                         **kwargs) -> Iterator[Experiment]:
        """List experiments.
        
        Gets a list of all experiments.
        
        :param max_results: int (optional)
          Maximum number of experiments desired. If `max_results` is unspecified, return all experiments. If
          `max_results` is too large, it'll be automatically capped at 1000. Callers of this endpoint are
          encouraged to pass max_results explicitly and leverage page_token to iterate through experiments.
        :param page_token: str (optional)
          Token indicating the page of experiments to fetch
        :param view_type: str (optional)
          Qualifier for type of experiments to be returned. If unspecified, return only active experiments.
        
        :returns: Iterator over :class:`Experiment`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListExperimentsRequest(max_results=max_results,
                                             page_token=page_token,
                                             view_type=view_type)

        query = {}
        if max_results: query['max_results'] = request.max_results
        if page_token: query['page_token'] = request.page_token
        if view_type: query['view_type'] = request.view_type

        while True:
            json = self._api.do('GET', '/api/2.0/mlflow/experiments/list', query=query)
            if 'experiments' not in json or not json['experiments']:
                return
            for v in json['experiments']:
                yield Experiment.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def log_batch(self,
                  *,
                  metrics: Optional[List[Metric]] = None,
                  params: Optional[List[Param]] = None,
                  run_id: Optional[str] = None,
                  tags: Optional[List[RunTag]] = None,
                  **kwargs):
        """Log a batch.
        
        Logs a batch of metrics, params, and tags for a run. If any data failed to be persisted, the server
        will respond with an error (non-200 status code).
        
        In case of error (due to internal server error or an invalid request), partial data may be written.
        
        You can write metrics, params, and tags in interleaving fashion, but within a given entity type are
        guaranteed to follow the order specified in the request body.
        
        The overwrite behavior for metrics, params, and tags is as follows:
        
        * Metrics: metric values are never overwritten. Logging a metric (key, value, timestamp) appends to
        the set of values for the metric with the provided key.
        
        * Tags: tag values can be overwritten by successive writes to the same tag key. That is, if multiple
        tag values with the same key are provided in the same API request, the last-provided tag value is
        written. Logging the same tag (key, value) is permitted. Specifically, logging a tag is idempotent.
        
        * Parameters: once written, param values cannot be changed (attempting to overwrite a param value will
        result in an error). However, logging the same param (key, value) is permitted. Specifically, logging
        a param is idempotent.
        
        Request Limits ------------------------------- A single JSON-serialized API request may be up to 1 MB
        in size and contain:
        
        * No more than 1000 metrics, params, and tags in total * Up to 1000 metrics * Up to 100 params * Up to
        100 tags
        
        For example, a valid request might contain 900 metrics, 50 params, and 50 tags, but logging 900
        metrics, 50 params, and 51 tags is invalid.
        
        The following limits also apply to metric, param, and tag keys and values:
        
        * Metric keys, param keys, and tag keys can be up to 250 characters in length * Parameter and tag
        values can be up to 250 characters in length
        
        :param metrics: List[:class:`Metric`] (optional)
          Metrics to log. A single request can contain up to 1000 metrics, and up to 1000 metrics, params, and
          tags in total.
        :param params: List[:class:`Param`] (optional)
          Params to log. A single request can contain up to 100 params, and up to 1000 metrics, params, and
          tags in total.
        :param run_id: str (optional)
          ID of the run to log under
        :param tags: List[:class:`RunTag`] (optional)
          Tags to log. A single request can contain up to 100 tags, and up to 1000 metrics, params, and tags
          in total.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = LogBatch(metrics=metrics, params=params, run_id=run_id, tags=tags)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/log-batch', body=body)

    def log_inputs(self,
                   *,
                   datasets: Optional[List[DatasetInput]] = None,
                   run_id: Optional[str] = None,
                   **kwargs):
        """Log inputs to a run.
        
        **NOTE:** Experimental: This API may change or be removed in a future release without warning.
        
        :param datasets: List[:class:`DatasetInput`] (optional)
          Dataset inputs
        :param run_id: str (optional)
          ID of the run to log under
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = LogInputs(datasets=datasets, run_id=run_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/log-inputs', body=body)

    def log_metric(self,
                   key: str,
                   value: float,
                   timestamp: int,
                   *,
                   run_id: Optional[str] = None,
                   run_uuid: Optional[str] = None,
                   step: Optional[int] = None,
                   **kwargs):
        """Log a metric.
        
        Logs a metric for a run. A metric is a key-value pair (string key, float value) with an associated
        timestamp. Examples include the various metrics that represent ML model accuracy. A metric can be
        logged multiple times.
        
        :param key: str
          Name of the metric.
        :param value: float
          Double value of the metric being logged.
        :param timestamp: int
          Unix timestamp in milliseconds at the time metric was logged.
        :param run_id: str (optional)
          ID of the run under which to log the metric. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run under which to log the metric. This field will be
          removed in a future MLflow version.
        :param step: int (optional)
          Step at which to log the metric
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = LogMetric(key=key,
                                run_id=run_id,
                                run_uuid=run_uuid,
                                step=step,
                                timestamp=timestamp,
                                value=value)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/log-metric', body=body)

    def log_model(self, *, model_json: Optional[str] = None, run_id: Optional[str] = None, **kwargs):
        """Log a model.
        
        **NOTE:** Experimental: This API may change or be removed in a future release without warning.
        
        :param model_json: str (optional)
          MLmodel file in json format.
        :param run_id: str (optional)
          ID of the run to log under
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = LogModel(model_json=model_json, run_id=run_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/log-model', body=body)

    def log_param(self,
                  key: str,
                  value: str,
                  *,
                  run_id: Optional[str] = None,
                  run_uuid: Optional[str] = None,
                  **kwargs):
        """Log a param.
        
        Logs a param used for a run. A param is a key-value pair (string key, string value). Examples include
        hyperparameters used for ML model training and constant dates and values used in an ETL pipeline. A
        param can be logged only once for a run.
        
        :param key: str
          Name of the param. Maximum size is 255 bytes.
        :param value: str
          String value of the param being logged. Maximum size is 500 bytes.
        :param run_id: str (optional)
          ID of the run under which to log the param. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run under which to log the param. This field will be
          removed in a future MLflow version.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = LogParam(key=key, run_id=run_id, run_uuid=run_uuid, value=value)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/log-parameter', body=body)

    def restore_experiment(self, experiment_id: str, **kwargs):
        """Restores an experiment.
        
        Restore an experiment marked for deletion. This also restores associated metadata, runs, metrics,
        params, and tags. If experiment uses FileStore, underlying artifacts associated with experiment are
        also restored.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if experiment was never created or was permanently deleted.
        
        :param experiment_id: str
          ID of the associated experiment.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RestoreExperiment(experiment_id=experiment_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/experiments/restore', body=body)

    def restore_run(self, run_id: str, **kwargs):
        """Restore a run.
        
        Restores a deleted run.
        
        :param run_id: str
          ID of the run to restore.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RestoreRun(run_id=run_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/restore', body=body)

    def search_experiments(self,
                           *,
                           filter: Optional[str] = None,
                           max_results: Optional[int] = None,
                           order_by: Optional[List[str]] = None,
                           page_token: Optional[str] = None,
                           view_type: Optional[SearchExperimentsViewType] = None,
                           **kwargs) -> Iterator[Experiment]:
        """Search experiments.
        
        Searches for experiments that satisfy specified search criteria.
        
        :param filter: str (optional)
          String representing a SQL filter condition (e.g. "name ILIKE 'my-experiment%'")
        :param max_results: int (optional)
          Maximum number of experiments desired. Max threshold is 3000.
        :param order_by: List[str] (optional)
          List of columns for ordering search results, which can include experiment name and last updated
          timestamp with an optional "DESC" or "ASC" annotation, where "ASC" is the default. Tiebreaks are
          done by experiment id DESC.
        :param page_token: str (optional)
          Token indicating the page of experiments to fetch
        :param view_type: :class:`SearchExperimentsViewType` (optional)
          Qualifier for type of experiments to be returned. If unspecified, return only active experiments.
        
        :returns: Iterator over :class:`Experiment`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SearchExperiments(filter=filter,
                                        max_results=max_results,
                                        order_by=order_by,
                                        page_token=page_token,
                                        view_type=view_type)
        body = request.as_dict()

        while True:
            json = self._api.do('POST', '/api/2.0/mlflow/experiments/search', body=body)
            if 'experiments' not in json or not json['experiments']:
                return
            for v in json['experiments']:
                yield Experiment.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            body['page_token'] = json['next_page_token']

    def search_runs(self,
                    *,
                    experiment_ids: Optional[List[str]] = None,
                    filter: Optional[str] = None,
                    max_results: Optional[int] = None,
                    order_by: Optional[List[str]] = None,
                    page_token: Optional[str] = None,
                    run_view_type: Optional[SearchRunsRunViewType] = None,
                    **kwargs) -> Iterator[Run]:
        """Search for runs.
        
        Searches for runs that satisfy expressions.
        
        Search expressions can use `mlflowMetric` and `mlflowParam` keys.",
        
        :param experiment_ids: List[str] (optional)
          List of experiment IDs to search over.
        :param filter: str (optional)
          A filter expression over params, metrics, and tags, that allows returning a subset of runs. The
          syntax is a subset of SQL that supports ANDing together binary operations between a param, metric,
          or tag and a constant.
          
          Example: `metrics.rmse < 1 and params.model_class = 'LogisticRegression'`
          
          You can select columns with special characters (hyphen, space, period, etc.) by using double quotes:
          `metrics."model class" = 'LinearRegression' and tags."user-name" = 'Tomas'`
          
          Supported operators are `=`, `!=`, `>`, `>=`, `<`, and `<=`.
        :param max_results: int (optional)
          Maximum number of runs desired. Max threshold is 50000
        :param order_by: List[str] (optional)
          List of columns to be ordered by, including attributes, params, metrics, and tags with an optional
          "DESC" or "ASC" annotation, where "ASC" is the default. Example: ["params.input DESC",
          "metrics.alpha ASC", "metrics.rmse"] Tiebreaks are done by start_time DESC followed by run_id for
          runs with the same start time (and this is the default ordering criterion if order_by is not
          provided).
        :param page_token: str (optional)
          Token for the current page of runs.
        :param run_view_type: :class:`SearchRunsRunViewType` (optional)
          Whether to display only active, only deleted, or all runs. Defaults to only active runs.
        
        :returns: Iterator over :class:`Run`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SearchRuns(experiment_ids=experiment_ids,
                                 filter=filter,
                                 max_results=max_results,
                                 order_by=order_by,
                                 page_token=page_token,
                                 run_view_type=run_view_type)
        body = request.as_dict()

        while True:
            json = self._api.do('POST', '/api/2.0/mlflow/runs/search', body=body)
            if 'runs' not in json or not json['runs']:
                return
            for v in json['runs']:
                yield Run.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            body['page_token'] = json['next_page_token']

    def set_experiment_tag(self, experiment_id: str, key: str, value: str, **kwargs):
        """Set a tag.
        
        Sets a tag on an experiment. Experiment tags are metadata that can be updated.
        
        :param experiment_id: str
          ID of the experiment under which to log the tag. Must be provided.
        :param key: str
          Name of the tag. Maximum size depends on storage backend. All storage backends are guaranteed to
          support key values up to 250 bytes in size.
        :param value: str
          String value of the tag being logged. Maximum size depends on storage backend. All storage backends
          are guaranteed to support key values up to 5000 bytes in size.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SetExperimentTag(experiment_id=experiment_id, key=key, value=value)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/experiments/set-experiment-tag', body=body)

    def set_tag(self,
                key: str,
                value: str,
                *,
                run_id: Optional[str] = None,
                run_uuid: Optional[str] = None,
                **kwargs):
        """Set a tag.
        
        Sets a tag on a run. Tags are run metadata that can be updated during a run and after a run completes.
        
        :param key: str
          Name of the tag. Maximum size depends on storage backend. All storage backends are guaranteed to
          support key values up to 250 bytes in size.
        :param value: str
          String value of the tag being logged. Maximum size depends on storage backend. All storage backends
          are guaranteed to support key values up to 5000 bytes in size.
        :param run_id: str (optional)
          ID of the run under which to log the tag. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run under which to log the tag. This field will be
          removed in a future MLflow version.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SetTag(key=key, run_id=run_id, run_uuid=run_uuid, value=value)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/set-tag', body=body)

    def update_experiment(self, experiment_id: str, *, new_name: Optional[str] = None, **kwargs):
        """Update an experiment.
        
        Updates experiment metadata.
        
        :param experiment_id: str
          ID of the associated experiment.
        :param new_name: str (optional)
          If provided, the experiment's name is changed to the new name. The new name must be unique.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateExperiment(experiment_id=experiment_id, new_name=new_name)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/experiments/update', body=body)

    def update_run(self,
                   *,
                   end_time: Optional[int] = None,
                   run_id: Optional[str] = None,
                   run_uuid: Optional[str] = None,
                   status: Optional[UpdateRunStatus] = None,
                   **kwargs) -> UpdateRunResponse:
        """Update a run.
        
        Updates run metadata.
        
        :param end_time: int (optional)
          Unix timestamp in milliseconds of when the run ended.
        :param run_id: str (optional)
          ID of the run to update. Must be provided.
        :param run_uuid: str (optional)
          [Deprecated, use run_id instead] ID of the run to update.. This field will be removed in a future
          MLflow version.
        :param status: :class:`UpdateRunStatus` (optional)
          Updated status of the run.
        
        :returns: :class:`UpdateRunResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateRun(end_time=end_time, run_id=run_id, run_uuid=run_uuid, status=status)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/runs/update', body=body)
        return UpdateRunResponse.from_dict(json)


class ModelRegistryAPI:
    """MLflow Model Registry is a centralized model repository and a UI and set of APIs that enable you to manage
    the full lifecycle of MLflow Models."""

    def __init__(self, api_client):
        self._api = api_client

    def approve_transition_request(self,
                                   name: str,
                                   version: str,
                                   stage: Stage,
                                   archive_existing_versions: bool,
                                   *,
                                   comment: Optional[str] = None,
                                   **kwargs) -> ApproveTransitionRequestResponse:
        """Approve transition request.
        
        Approves a model version stage transition request.
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        :param stage: :class:`Stage`
          Target stage of the transition. Valid values are:
          
          * `None`: The initial stage of a model version.
          
          * `Staging`: Staging or pre-production stage.
          
          * `Production`: Production stage.
          
          * `Archived`: Archived stage.
        :param archive_existing_versions: bool
          Specifies whether to archive all current model versions in the target stage.
        :param comment: str (optional)
          User-provided comment on the action.
        
        :returns: :class:`ApproveTransitionRequestResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ApproveTransitionRequest(archive_existing_versions=archive_existing_versions,
                                               comment=comment,
                                               name=name,
                                               stage=stage,
                                               version=version)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/transition-requests/approve', body=body)
        return ApproveTransitionRequestResponse.from_dict(json)

    def create_comment(self, name: str, version: str, comment: str, **kwargs) -> CreateCommentResponse:
        """Post a comment.
        
        Posts a comment on a model version. A comment can be submitted either by a user or programmatically to
        display relevant information about the model. For example, test results or deployment errors.
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        :param comment: str
          User-provided comment on the action.
        
        :returns: :class:`CreateCommentResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateComment(comment=comment, name=name, version=version)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/comments/create', body=body)
        return CreateCommentResponse.from_dict(json)

    def create_model(self,
                     name: str,
                     *,
                     description: Optional[str] = None,
                     tags: Optional[List[ModelTag]] = None,
                     **kwargs) -> CreateModelResponse:
        """Create a model.
        
        Creates a new registered model with the name specified in the request body.
        
        Throws `RESOURCE_ALREADY_EXISTS` if a registered model with the given name exists.
        
        :param name: str
          Register models under this name
        :param description: str (optional)
          Optional description for registered model.
        :param tags: List[:class:`ModelTag`] (optional)
          Additional metadata for registered model.
        
        :returns: :class:`CreateModelResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateModelRequest(description=description, name=name, tags=tags)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/registered-models/create', body=body)
        return CreateModelResponse.from_dict(json)

    def create_model_version(self,
                             name: str,
                             source: str,
                             *,
                             description: Optional[str] = None,
                             run_id: Optional[str] = None,
                             run_link: Optional[str] = None,
                             tags: Optional[List[ModelVersionTag]] = None,
                             **kwargs) -> CreateModelVersionResponse:
        """Create a model version.
        
        Creates a model version.
        
        :param name: str
          Register model under this name
        :param source: str
          URI indicating the location of the model artifacts.
        :param description: str (optional)
          Optional description for model version.
        :param run_id: str (optional)
          MLflow run ID for correlation, if `source` was generated by an experiment run in MLflow tracking
          server
        :param run_link: str (optional)
          MLflow run link - this is the exact link of the run that generated this model version, potentially
          hosted at another instance of MLflow.
        :param tags: List[:class:`ModelVersionTag`] (optional)
          Additional metadata for model version.
        
        :returns: :class:`CreateModelVersionResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateModelVersionRequest(description=description,
                                                name=name,
                                                run_id=run_id,
                                                run_link=run_link,
                                                source=source,
                                                tags=tags)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/model-versions/create', body=body)
        return CreateModelVersionResponse.from_dict(json)

    def create_transition_request(self,
                                  name: str,
                                  version: str,
                                  stage: Stage,
                                  *,
                                  comment: Optional[str] = None,
                                  **kwargs) -> CreateTransitionRequestResponse:
        """Make a transition request.
        
        Creates a model version stage transition request.
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        :param stage: :class:`Stage`
          Target stage of the transition. Valid values are:
          
          * `None`: The initial stage of a model version.
          
          * `Staging`: Staging or pre-production stage.
          
          * `Production`: Production stage.
          
          * `Archived`: Archived stage.
        :param comment: str (optional)
          User-provided comment on the action.
        
        :returns: :class:`CreateTransitionRequestResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateTransitionRequest(comment=comment, name=name, stage=stage, version=version)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/transition-requests/create', body=body)
        return CreateTransitionRequestResponse.from_dict(json)

    def create_webhook(self,
                       events: List[RegistryWebhookEvent],
                       *,
                       description: Optional[str] = None,
                       http_url_spec: Optional[HttpUrlSpec] = None,
                       job_spec: Optional[JobSpec] = None,
                       model_name: Optional[str] = None,
                       status: Optional[RegistryWebhookStatus] = None,
                       **kwargs) -> CreateWebhookResponse:
        """Create a webhook.
        
        **NOTE**: This endpoint is in Public Preview.
        
        Creates a registry webhook.
        
        :param events: List[:class:`RegistryWebhookEvent`]
          Events that can trigger a registry webhook: * `MODEL_VERSION_CREATED`: A new model version was
          created for the associated model.
          
          * `MODEL_VERSION_TRANSITIONED_STAGE`: A model version’s stage was changed.
          
          * `TRANSITION_REQUEST_CREATED`: A user requested a model version’s stage be transitioned.
          
          * `COMMENT_CREATED`: A user wrote a comment on a registered model.
          
          * `REGISTERED_MODEL_CREATED`: A new registered model was created. This event type can only be
          specified for a registry-wide webhook, which can be created by not specifying a model name in the
          create request.
          
          * `MODEL_VERSION_TAG_SET`: A user set a tag on the model version.
          
          * `MODEL_VERSION_TRANSITIONED_TO_STAGING`: A model version was transitioned to staging.
          
          * `MODEL_VERSION_TRANSITIONED_TO_PRODUCTION`: A model version was transitioned to production.
          
          * `MODEL_VERSION_TRANSITIONED_TO_ARCHIVED`: A model version was archived.
          
          * `TRANSITION_REQUEST_TO_STAGING_CREATED`: A user requested a model version be transitioned to
          staging.
          
          * `TRANSITION_REQUEST_TO_PRODUCTION_CREATED`: A user requested a model version be transitioned to
          production.
          
          * `TRANSITION_REQUEST_TO_ARCHIVED_CREATED`: A user requested a model version be archived.
        :param description: str (optional)
          User-specified description for the webhook.
        :param http_url_spec: :class:`HttpUrlSpec` (optional)
        :param job_spec: :class:`JobSpec` (optional)
        :param model_name: str (optional)
          Name of the model whose events would trigger this webhook.
        :param status: :class:`RegistryWebhookStatus` (optional)
          This describes an enum
        
        :returns: :class:`CreateWebhookResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateRegistryWebhook(description=description,
                                            events=events,
                                            http_url_spec=http_url_spec,
                                            job_spec=job_spec,
                                            model_name=model_name,
                                            status=status)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/registry-webhooks/create', body=body)
        return CreateWebhookResponse.from_dict(json)

    def delete_comment(self, id: str, **kwargs):
        """Delete a comment.
        
        Deletes a comment on a model version.
        
        :param id: str
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteCommentRequest(id=id)

        query = {}
        if id: query['id'] = request.id

        self._api.do('DELETE', '/api/2.0/mlflow/comments/delete', query=query)

    def delete_model(self, name: str, **kwargs):
        """Delete a model.
        
        Deletes a registered model.
        
        :param name: str
          Registered model unique name identifier.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteModelRequest(name=name)

        query = {}
        if name: query['name'] = request.name

        self._api.do('DELETE', '/api/2.0/mlflow/registered-models/delete', query=query)

    def delete_model_tag(self, name: str, key: str, **kwargs):
        """Delete a model tag.
        
        Deletes the tag for a registered model.
        
        :param name: str
          Name of the registered model that the tag was logged under.
        :param key: str
          Name of the tag. The name must be an exact match; wild-card deletion is not supported. Maximum size
          is 250 bytes.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteModelTagRequest(key=key, name=name)

        query = {}
        if key: query['key'] = request.key
        if name: query['name'] = request.name

        self._api.do('DELETE', '/api/2.0/mlflow/registered-models/delete-tag', query=query)

    def delete_model_version(self, name: str, version: str, **kwargs):
        """Delete a model version.
        
        Deletes a model version.
        
        :param name: str
          Name of the registered model
        :param version: str
          Model version number
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteModelVersionRequest(name=name, version=version)

        query = {}
        if name: query['name'] = request.name
        if version: query['version'] = request.version

        self._api.do('DELETE', '/api/2.0/mlflow/model-versions/delete', query=query)

    def delete_model_version_tag(self, name: str, version: str, key: str, **kwargs):
        """Delete a model version tag.
        
        Deletes a model version tag.
        
        :param name: str
          Name of the registered model that the tag was logged under.
        :param version: str
          Model version number that the tag was logged under.
        :param key: str
          Name of the tag. The name must be an exact match; wild-card deletion is not supported. Maximum size
          is 250 bytes.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteModelVersionTagRequest(key=key, name=name, version=version)

        query = {}
        if key: query['key'] = request.key
        if name: query['name'] = request.name
        if version: query['version'] = request.version

        self._api.do('DELETE', '/api/2.0/mlflow/model-versions/delete-tag', query=query)

    def delete_transition_request(self,
                                  name: str,
                                  version: str,
                                  stage: DeleteTransitionRequestStage,
                                  creator: str,
                                  *,
                                  comment: Optional[str] = None,
                                  **kwargs):
        """Delete a transition request.
        
        Cancels a model version stage transition request.
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        :param stage: :class:`DeleteTransitionRequestStage`
          Target stage of the transition request. Valid values are:
          
          * `None`: The initial stage of a model version.
          
          * `Staging`: Staging or pre-production stage.
          
          * `Production`: Production stage.
          
          * `Archived`: Archived stage.
        :param creator: str
          Username of the user who created this request. Of the transition requests matching the specified
          details, only the one transition created by this user will be deleted.
        :param comment: str (optional)
          User-provided comment on the action.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteTransitionRequestRequest(comment=comment,
                                                     creator=creator,
                                                     name=name,
                                                     stage=stage,
                                                     version=version)

        query = {}
        if comment: query['comment'] = request.comment
        if creator: query['creator'] = request.creator
        if name: query['name'] = request.name
        if stage: query['stage'] = request.stage.value
        if version: query['version'] = request.version

        self._api.do('DELETE', '/api/2.0/mlflow/transition-requests/delete', query=query)

    def delete_webhook(self, *, id: Optional[str] = None, **kwargs):
        """Delete a webhook.
        
        **NOTE:** This endpoint is in Public Preview.
        
        Deletes a registry webhook.
        
        :param id: str (optional)
          Webhook ID required to delete a registry webhook.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteWebhookRequest(id=id)

        query = {}
        if id: query['id'] = request.id

        self._api.do('DELETE', '/api/2.0/mlflow/registry-webhooks/delete', query=query)

    def get_latest_versions(self,
                            name: str,
                            *,
                            stages: Optional[List[str]] = None,
                            **kwargs) -> Iterator[ModelVersion]:
        """Get the latest version.
        
        Gets the latest version of a registered model.
        
        :param name: str
          Registered model unique name identifier.
        :param stages: List[str] (optional)
          List of stages.
        
        :returns: Iterator over :class:`ModelVersion`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetLatestVersionsRequest(name=name, stages=stages)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/registered-models/get-latest-versions', body=body)
        return [ModelVersion.from_dict(v) for v in json.get('model_versions', [])]

    def get_model(self, name: str, **kwargs) -> GetModelResponse:
        """Get model.
        
        Get the details of a model. This is a Databricks workspace version of the [MLflow endpoint] that also
        returns the model's Databricks workspace ID and the permission level of the requesting user on the
        model.
        
        [MLflow endpoint]: https://www.mlflow.org/docs/latest/rest-api.html#get-registeredmodel
        
        :param name: str
          Registered model unique name identifier.
        
        :returns: :class:`GetModelResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetModelRequest(name=name)

        query = {}
        if name: query['name'] = request.name

        json = self._api.do('GET', '/api/2.0/mlflow/databricks/registered-models/get', query=query)
        return GetModelResponse.from_dict(json)

    def get_model_version(self, name: str, version: str, **kwargs) -> GetModelVersionResponse:
        """Get a model version.
        
        Get a model version.
        
        :param name: str
          Name of the registered model
        :param version: str
          Model version number
        
        :returns: :class:`GetModelVersionResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetModelVersionRequest(name=name, version=version)

        query = {}
        if name: query['name'] = request.name
        if version: query['version'] = request.version

        json = self._api.do('GET', '/api/2.0/mlflow/model-versions/get', query=query)
        return GetModelVersionResponse.from_dict(json)

    def get_model_version_download_uri(self, name: str, version: str,
                                       **kwargs) -> GetModelVersionDownloadUriResponse:
        """Get a model version URI.
        
        Gets a URI to download the model version.
        
        :param name: str
          Name of the registered model
        :param version: str
          Model version number
        
        :returns: :class:`GetModelVersionDownloadUriResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetModelVersionDownloadUriRequest(name=name, version=version)

        query = {}
        if name: query['name'] = request.name
        if version: query['version'] = request.version

        json = self._api.do('GET', '/api/2.0/mlflow/model-versions/get-download-uri', query=query)
        return GetModelVersionDownloadUriResponse.from_dict(json)

    def list_models(self,
                    *,
                    max_results: Optional[int] = None,
                    page_token: Optional[str] = None,
                    **kwargs) -> Iterator[Model]:
        """List models.
        
        Lists all available registered models, up to the limit specified in __max_results__.
        
        :param max_results: int (optional)
          Maximum number of registered models desired. Max threshold is 1000.
        :param page_token: str (optional)
          Pagination token to go to the next page based on a previous query.
        
        :returns: Iterator over :class:`Model`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListModelsRequest(max_results=max_results, page_token=page_token)

        query = {}
        if max_results: query['max_results'] = request.max_results
        if page_token: query['page_token'] = request.page_token

        while True:
            json = self._api.do('GET', '/api/2.0/mlflow/registered-models/list', query=query)
            if 'registered_models' not in json or not json['registered_models']:
                return
            for v in json['registered_models']:
                yield Model.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def list_transition_requests(self, name: str, version: str, **kwargs) -> Iterator[Activity]:
        """List transition requests.
        
        Gets a list of all open stage transition requests for the model version.
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        
        :returns: Iterator over :class:`Activity`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListTransitionRequestsRequest(name=name, version=version)

        query = {}
        if name: query['name'] = request.name
        if version: query['version'] = request.version

        json = self._api.do('GET', '/api/2.0/mlflow/transition-requests/list', query=query)
        return [Activity.from_dict(v) for v in json.get('requests', [])]

    def list_webhooks(self,
                      *,
                      events: Optional[List[RegistryWebhookEvent]] = None,
                      model_name: Optional[str] = None,
                      page_token: Optional[str] = None,
                      **kwargs) -> Iterator[RegistryWebhook]:
        """List registry webhooks.
        
        **NOTE:** This endpoint is in Public Preview.
        
        Lists all registry webhooks.
        
        :param events: List[:class:`RegistryWebhookEvent`] (optional)
          If `events` is specified, any webhook with one or more of the specified trigger events is included
          in the output. If `events` is not specified, webhooks of all event types are included in the output.
        :param model_name: str (optional)
          If not specified, all webhooks associated with the specified events are listed, regardless of their
          associated model.
        :param page_token: str (optional)
          Token indicating the page of artifact results to fetch
        
        :returns: Iterator over :class:`RegistryWebhook`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListWebhooksRequest(events=events, model_name=model_name, page_token=page_token)

        query = {}
        if events: query['events'] = [v for v in request.events]
        if model_name: query['model_name'] = request.model_name
        if page_token: query['page_token'] = request.page_token

        while True:
            json = self._api.do('GET', '/api/2.0/mlflow/registry-webhooks/list', query=query)
            if 'webhooks' not in json or not json['webhooks']:
                return
            for v in json['webhooks']:
                yield RegistryWebhook.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def reject_transition_request(self,
                                  name: str,
                                  version: str,
                                  stage: Stage,
                                  *,
                                  comment: Optional[str] = None,
                                  **kwargs) -> RejectTransitionRequestResponse:
        """Reject a transition request.
        
        Rejects a model version stage transition request.
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        :param stage: :class:`Stage`
          Target stage of the transition. Valid values are:
          
          * `None`: The initial stage of a model version.
          
          * `Staging`: Staging or pre-production stage.
          
          * `Production`: Production stage.
          
          * `Archived`: Archived stage.
        :param comment: str (optional)
          User-provided comment on the action.
        
        :returns: :class:`RejectTransitionRequestResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RejectTransitionRequest(comment=comment, name=name, stage=stage, version=version)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/transition-requests/reject', body=body)
        return RejectTransitionRequestResponse.from_dict(json)

    def rename_model(self, name: str, *, new_name: Optional[str] = None, **kwargs) -> RenameModelResponse:
        """Rename a model.
        
        Renames a registered model.
        
        :param name: str
          Registered model unique name identifier.
        :param new_name: str (optional)
          If provided, updates the name for this `registered_model`.
        
        :returns: :class:`RenameModelResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RenameModelRequest(name=name, new_name=new_name)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/registered-models/rename', body=body)
        return RenameModelResponse.from_dict(json)

    def search_model_versions(self,
                              *,
                              filter: Optional[str] = None,
                              max_results: Optional[int] = None,
                              order_by: Optional[List[str]] = None,
                              page_token: Optional[str] = None,
                              **kwargs) -> Iterator[ModelVersion]:
        """Searches model versions.
        
        Searches for specific model versions based on the supplied __filter__.
        
        :param filter: str (optional)
          String filter condition, like "name='my-model-name'". Must be a single boolean condition, with
          string values wrapped in single quotes.
        :param max_results: int (optional)
          Maximum number of models desired. Max threshold is 10K.
        :param order_by: List[str] (optional)
          List of columns to be ordered by including model name, version, stage with an optional "DESC" or
          "ASC" annotation, where "ASC" is the default. Tiebreaks are done by latest stage transition
          timestamp, followed by name ASC, followed by version DESC.
        :param page_token: str (optional)
          Pagination token to go to next page based on previous search query.
        
        :returns: Iterator over :class:`ModelVersion`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SearchModelVersionsRequest(filter=filter,
                                                 max_results=max_results,
                                                 order_by=order_by,
                                                 page_token=page_token)

        query = {}
        if filter: query['filter'] = request.filter
        if max_results: query['max_results'] = request.max_results
        if order_by: query['order_by'] = [v for v in request.order_by]
        if page_token: query['page_token'] = request.page_token

        while True:
            json = self._api.do('GET', '/api/2.0/mlflow/model-versions/search', query=query)
            if 'model_versions' not in json or not json['model_versions']:
                return
            for v in json['model_versions']:
                yield ModelVersion.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def search_models(self,
                      *,
                      filter: Optional[str] = None,
                      max_results: Optional[int] = None,
                      order_by: Optional[List[str]] = None,
                      page_token: Optional[str] = None,
                      **kwargs) -> Iterator[Model]:
        """Search models.
        
        Search for registered models based on the specified __filter__.
        
        :param filter: str (optional)
          String filter condition, like "name LIKE 'my-model-name'". Interpreted in the backend automatically
          as "name LIKE '%my-model-name%'". Single boolean condition, with string values wrapped in single
          quotes.
        :param max_results: int (optional)
          Maximum number of models desired. Default is 100. Max threshold is 1000.
        :param order_by: List[str] (optional)
          List of columns for ordering search results, which can include model name and last updated timestamp
          with an optional "DESC" or "ASC" annotation, where "ASC" is the default. Tiebreaks are done by model
          name ASC.
        :param page_token: str (optional)
          Pagination token to go to the next page based on a previous search query.
        
        :returns: Iterator over :class:`Model`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SearchModelsRequest(filter=filter,
                                          max_results=max_results,
                                          order_by=order_by,
                                          page_token=page_token)

        query = {}
        if filter: query['filter'] = request.filter
        if max_results: query['max_results'] = request.max_results
        if order_by: query['order_by'] = [v for v in request.order_by]
        if page_token: query['page_token'] = request.page_token

        while True:
            json = self._api.do('GET', '/api/2.0/mlflow/registered-models/search', query=query)
            if 'registered_models' not in json or not json['registered_models']:
                return
            for v in json['registered_models']:
                yield Model.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def set_model_tag(self, name: str, key: str, value: str, **kwargs):
        """Set a tag.
        
        Sets a tag on a registered model.
        
        :param name: str
          Unique name of the model.
        :param key: str
          Name of the tag. Maximum size depends on storage backend. If a tag with this name already exists,
          its preexisting value will be replaced by the specified `value`. All storage backends are guaranteed
          to support key values up to 250 bytes in size.
        :param value: str
          String value of the tag being logged. Maximum size depends on storage backend. All storage backends
          are guaranteed to support key values up to 5000 bytes in size.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SetModelTagRequest(key=key, name=name, value=value)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/registered-models/set-tag', body=body)

    def set_model_version_tag(self, name: str, version: str, key: str, value: str, **kwargs):
        """Set a version tag.
        
        Sets a model version tag.
        
        :param name: str
          Unique name of the model.
        :param version: str
          Model version number.
        :param key: str
          Name of the tag. Maximum size depends on storage backend. If a tag with this name already exists,
          its preexisting value will be replaced by the specified `value`. All storage backends are guaranteed
          to support key values up to 250 bytes in size.
        :param value: str
          String value of the tag being logged. Maximum size depends on storage backend. All storage backends
          are guaranteed to support key values up to 5000 bytes in size.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SetModelVersionTagRequest(key=key, name=name, value=value, version=version)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/model-versions/set-tag', body=body)

    def test_registry_webhook(self,
                              id: str,
                              *,
                              event: Optional[RegistryWebhookEvent] = None,
                              **kwargs) -> TestRegistryWebhookResponse:
        """Test a webhook.
        
        **NOTE:** This endpoint is in Public Preview.
        
        Tests a registry webhook.
        
        :param id: str
          Webhook ID
        :param event: :class:`RegistryWebhookEvent` (optional)
          If `event` is specified, the test trigger uses the specified event. If `event` is not specified, the
          test trigger uses a randomly chosen event associated with the webhook.
        
        :returns: :class:`TestRegistryWebhookResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = TestRegistryWebhookRequest(event=event, id=id)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/registry-webhooks/test', body=body)
        return TestRegistryWebhookResponse.from_dict(json)

    def transition_stage(self,
                         name: str,
                         version: str,
                         stage: Stage,
                         archive_existing_versions: bool,
                         *,
                         comment: Optional[str] = None,
                         **kwargs) -> TransitionStageResponse:
        """Transition a stage.
        
        Transition a model version's stage. This is a Databricks workspace version of the [MLflow endpoint]
        that also accepts a comment associated with the transition to be recorded.",
        
        [MLflow endpoint]: https://www.mlflow.org/docs/latest/rest-api.html#transition-modelversion-stage
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        :param stage: :class:`Stage`
          Target stage of the transition. Valid values are:
          
          * `None`: The initial stage of a model version.
          
          * `Staging`: Staging or pre-production stage.
          
          * `Production`: Production stage.
          
          * `Archived`: Archived stage.
        :param archive_existing_versions: bool
          Specifies whether to archive all current model versions in the target stage.
        :param comment: str (optional)
          User-provided comment on the action.
        
        :returns: :class:`TransitionStageResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = TransitionModelVersionStageDatabricks(
                archive_existing_versions=archive_existing_versions,
                comment=comment,
                name=name,
                stage=stage,
                version=version)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/databricks/model-versions/transition-stage', body=body)
        return TransitionStageResponse.from_dict(json)

    def update_comment(self, id: str, comment: str, **kwargs) -> UpdateCommentResponse:
        """Update a comment.
        
        Post an edit to a comment on a model version.
        
        :param id: str
          Unique identifier of an activity
        :param comment: str
          User-provided comment on the action.
        
        :returns: :class:`UpdateCommentResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateComment(comment=comment, id=id)
        body = request.as_dict()

        json = self._api.do('PATCH', '/api/2.0/mlflow/comments/update', body=body)
        return UpdateCommentResponse.from_dict(json)

    def update_model(self, name: str, *, description: Optional[str] = None, **kwargs):
        """Update model.
        
        Updates a registered model.
        
        :param name: str
          Registered model unique name identifier.
        :param description: str (optional)
          If provided, updates the description for this `registered_model`.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateModelRequest(description=description, name=name)
        body = request.as_dict()
        self._api.do('PATCH', '/api/2.0/mlflow/registered-models/update', body=body)

    def update_model_version(self, name: str, version: str, *, description: Optional[str] = None, **kwargs):
        """Update model version.
        
        Updates the model version.
        
        :param name: str
          Name of the registered model
        :param version: str
          Model version number
        :param description: str (optional)
          If provided, updates the description for this `registered_model`.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateModelVersionRequest(description=description, name=name, version=version)
        body = request.as_dict()
        self._api.do('PATCH', '/api/2.0/mlflow/model-versions/update', body=body)

    def update_webhook(self,
                       id: str,
                       *,
                       description: Optional[str] = None,
                       events: Optional[List[RegistryWebhookEvent]] = None,
                       http_url_spec: Optional[HttpUrlSpec] = None,
                       job_spec: Optional[JobSpec] = None,
                       status: Optional[RegistryWebhookStatus] = None,
                       **kwargs):
        """Update a webhook.
        
        **NOTE:** This endpoint is in Public Preview.
        
        Updates a registry webhook.
        
        :param id: str
          Webhook ID
        :param description: str (optional)
          User-specified description for the webhook.
        :param events: List[:class:`RegistryWebhookEvent`] (optional)
          Events that can trigger a registry webhook: * `MODEL_VERSION_CREATED`: A new model version was
          created for the associated model.
          
          * `MODEL_VERSION_TRANSITIONED_STAGE`: A model version’s stage was changed.
          
          * `TRANSITION_REQUEST_CREATED`: A user requested a model version’s stage be transitioned.
          
          * `COMMENT_CREATED`: A user wrote a comment on a registered model.
          
          * `REGISTERED_MODEL_CREATED`: A new registered model was created. This event type can only be
          specified for a registry-wide webhook, which can be created by not specifying a model name in the
          create request.
          
          * `MODEL_VERSION_TAG_SET`: A user set a tag on the model version.
          
          * `MODEL_VERSION_TRANSITIONED_TO_STAGING`: A model version was transitioned to staging.
          
          * `MODEL_VERSION_TRANSITIONED_TO_PRODUCTION`: A model version was transitioned to production.
          
          * `MODEL_VERSION_TRANSITIONED_TO_ARCHIVED`: A model version was archived.
          
          * `TRANSITION_REQUEST_TO_STAGING_CREATED`: A user requested a model version be transitioned to
          staging.
          
          * `TRANSITION_REQUEST_TO_PRODUCTION_CREATED`: A user requested a model version be transitioned to
          production.
          
          * `TRANSITION_REQUEST_TO_ARCHIVED_CREATED`: A user requested a model version be archived.
        :param http_url_spec: :class:`HttpUrlSpec` (optional)
        :param job_spec: :class:`JobSpec` (optional)
        :param status: :class:`RegistryWebhookStatus` (optional)
          This describes an enum
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateRegistryWebhook(description=description,
                                            events=events,
                                            http_url_spec=http_url_spec,
                                            id=id,
                                            job_spec=job_spec,
                                            status=status)
        body = request.as_dict()
        self._api.do('PATCH', '/api/2.0/mlflow/registry-webhooks/update', body=body)

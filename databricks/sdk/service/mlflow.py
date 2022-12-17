# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any

# all definitions in this file are in alphabetical order


@dataclass
class Activity:
    """Activity recorded for the action."""

    activity_type: 'ActivityType'
    comment: str
    creation_timestamp: int
    from_stage: 'Stage'
    id: str
    last_updated_timestamp: int
    system_comment: str
    to_stage: 'Stage'
    user_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.activity_type: body['activity_type'] = self.activity_type.value
        if self.comment: body['comment'] = self.comment
        if self.creation_timestamp: body['creation_timestamp'] = self.creation_timestamp
        if self.from_stage: body['from_stage'] = self.from_stage.value
        if self.id: body['id'] = self.id
        if self.last_updated_timestamp: body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.system_comment: body['system_comment'] = self.system_comment
        if self.to_stage: body['to_stage'] = self.to_stage.value
        if self.user_id: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Activity':
        return cls(activity_type=ActivityType(d['activity_type']) if 'activity_type' in d else None,
                   comment=d.get('comment', None),
                   creation_timestamp=d.get('creation_timestamp', None),
                   from_stage=Stage(d['from_stage']) if 'from_stage' in d else None,
                   id=d.get('id', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   system_comment=d.get('system_comment', None),
                   to_stage=Stage(d['to_stage']) if 'to_stage' in d else None,
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
class ApproveResponse:
    activity: 'Activity'

    def as_dict(self) -> dict:
        body = {}
        if self.activity: body['activity'] = self.activity.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ApproveResponse':
        return cls(activity=Activity.from_dict(d['activity']) if 'activity' in d else None)


@dataclass
class ApproveTransitionRequest:
    archive_existing_versions: bool
    comment: str
    name: str
    stage: 'Stage'
    version: str

    def as_dict(self) -> dict:
        body = {}
        if self.archive_existing_versions: body['archive_existing_versions'] = self.archive_existing_versions
        if self.comment: body['comment'] = self.comment
        if self.name: body['name'] = self.name
        if self.stage: body['stage'] = self.stage.value
        if self.version: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ApproveTransitionRequest':
        return cls(archive_existing_versions=d.get('archive_existing_versions', None),
                   comment=d.get('comment', None),
                   name=d.get('name', None),
                   stage=Stage(d['stage']) if 'stage' in d else None,
                   version=d.get('version', None))


class CommentActivityAction(Enum):
    """This describes an enum"""

    DELETE_COMMENT = 'DELETE_COMMENT'
    EDIT_COMMENT = 'EDIT_COMMENT'


@dataclass
class CommentObject:
    """Comment details."""

    available_actions: 'List[CommentActivityAction]'
    comment: str
    creation_timestamp: int
    last_updated_timestamp: int
    user_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.available_actions: body['available_actions'] = [v for v in self.available_actions]
        if self.comment: body['comment'] = self.comment
        if self.creation_timestamp: body['creation_timestamp'] = self.creation_timestamp
        if self.last_updated_timestamp: body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.user_id: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CommentObject':
        return cls(available_actions=d.get('available_actions', None),
                   comment=d.get('comment', None),
                   creation_timestamp=d.get('creation_timestamp', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   user_id=d.get('user_id', None))


@dataclass
class CreateComment:
    comment: str
    name: str
    version: str

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.name: body['name'] = self.name
        if self.version: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateComment':
        return cls(comment=d.get('comment', None), name=d.get('name', None), version=d.get('version', None))


@dataclass
class CreateExperiment:
    artifact_location: str
    name: str
    tags: 'List[ExperimentTag]'

    def as_dict(self) -> dict:
        body = {}
        if self.artifact_location: body['artifact_location'] = self.artifact_location
        if self.name: body['name'] = self.name
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateExperiment':
        return cls(artifact_location=d.get('artifact_location', None),
                   name=d.get('name', None),
                   tags=[ExperimentTag.from_dict(v) for v in d['tags']] if 'tags' in d else None)


@dataclass
class CreateExperimentResponse:
    experiment_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.experiment_id: body['experiment_id'] = self.experiment_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateExperimentResponse':
        return cls(experiment_id=d.get('experiment_id', None))


@dataclass
class CreateModelVersionRequest:
    description: str
    name: str
    run_id: str
    run_link: str
    source: str
    tags: 'List[ModelVersionTag]'

    def as_dict(self) -> dict:
        body = {}
        if self.description: body['description'] = self.description
        if self.name: body['name'] = self.name
        if self.run_id: body['run_id'] = self.run_id
        if self.run_link: body['run_link'] = self.run_link
        if self.source: body['source'] = self.source
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateModelVersionRequest':
        return cls(description=d.get('description', None),
                   name=d.get('name', None),
                   run_id=d.get('run_id', None),
                   run_link=d.get('run_link', None),
                   source=d.get('source', None),
                   tags=[ModelVersionTag.from_dict(v) for v in d['tags']] if 'tags' in d else None)


@dataclass
class CreateModelVersionResponse:
    model_version: 'ModelVersion'

    def as_dict(self) -> dict:
        body = {}
        if self.model_version: body['model_version'] = self.model_version.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateModelVersionResponse':
        return cls(model_version=ModelVersion.from_dict(d['model_version']) if 'model_version' in d else None)


@dataclass
class CreateRegisteredModelRequest:
    description: str
    name: str
    tags: 'List[RegisteredModelTag]'

    def as_dict(self) -> dict:
        body = {}
        if self.description: body['description'] = self.description
        if self.name: body['name'] = self.name
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRegisteredModelRequest':
        return cls(description=d.get('description', None),
                   name=d.get('name', None),
                   tags=[RegisteredModelTag.from_dict(v) for v in d['tags']] if 'tags' in d else None)


@dataclass
class CreateRegisteredModelResponse:
    registered_model: 'RegisteredModel'

    def as_dict(self) -> dict:
        body = {}
        if self.registered_model: body['registered_model'] = self.registered_model.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRegisteredModelResponse':
        return cls(registered_model=RegisteredModel.from_dict(d['registered_model']) if 'registered_model' in
                   d else None)


@dataclass
class CreateRegistryWebhook:
    description: str
    events: 'List[RegistryWebhookEvent]'
    http_url_spec: 'HttpUrlSpec'
    job_spec: 'JobSpec'
    model_name: str
    status: 'RegistryWebhookStatus'

    def as_dict(self) -> dict:
        body = {}
        if self.description: body['description'] = self.description
        if self.events: body['events'] = [v for v in self.events]
        if self.http_url_spec: body['http_url_spec'] = self.http_url_spec.as_dict()
        if self.job_spec: body['job_spec'] = self.job_spec.as_dict()
        if self.model_name: body['model_name'] = self.model_name
        if self.status: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRegistryWebhook':
        return cls(description=d.get('description', None),
                   events=d.get('events', None),
                   http_url_spec=HttpUrlSpec.from_dict(d['http_url_spec']) if 'http_url_spec' in d else None,
                   job_spec=JobSpec.from_dict(d['job_spec']) if 'job_spec' in d else None,
                   model_name=d.get('model_name', None),
                   status=RegistryWebhookStatus(d['status']) if 'status' in d else None)


@dataclass
class CreateResponse:
    comment: 'CommentObject'

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateResponse':
        return cls(comment=CommentObject.from_dict(d['comment']) if 'comment' in d else None)


@dataclass
class CreateRun:
    experiment_id: str
    start_time: int
    tags: 'List[RunTag]'
    user_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.experiment_id: body['experiment_id'] = self.experiment_id
        if self.start_time: body['start_time'] = self.start_time
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        if self.user_id: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRun':
        return cls(experiment_id=d.get('experiment_id', None),
                   start_time=d.get('start_time', None),
                   tags=[RunTag.from_dict(v) for v in d['tags']] if 'tags' in d else None,
                   user_id=d.get('user_id', None))


@dataclass
class CreateRunResponse:
    run: 'Run'

    def as_dict(self) -> dict:
        body = {}
        if self.run: body['run'] = self.run.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRunResponse':
        return cls(run=Run.from_dict(d['run']) if 'run' in d else None)


@dataclass
class CreateTransitionRequest:
    comment: str
    name: str
    stage: 'Stage'
    version: str

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.name: body['name'] = self.name
        if self.stage: body['stage'] = self.stage.value
        if self.version: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateTransitionRequest':
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   stage=Stage(d['stage']) if 'stage' in d else None,
                   version=d.get('version', None))


@dataclass
class DeleteExperiment:
    experiment_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.experiment_id: body['experiment_id'] = self.experiment_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteExperiment':
        return cls(experiment_id=d.get('experiment_id', None))


@dataclass
class DeleteModelVersionCommentRequest:
    """Delete a comment"""

    id: str


@dataclass
class DeleteModelVersionRequest:
    """Delete a model version."""

    name: str
    version: str


@dataclass
class DeleteModelVersionTagRequest:
    """Delete a model version tag"""

    key: str
    name: str
    version: str


@dataclass
class DeleteRegisteredModelRequest:
    """Delete a model"""

    name: str


@dataclass
class DeleteRegisteredModelTagRequest:
    """Delete a model tag"""

    key: str
    name: str


@dataclass
class DeleteRegistryWebhookRequest:
    """Delete a webhook"""

    id: str


@dataclass
class DeleteRun:
    run_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.run_id: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteRun':
        return cls(run_id=d.get('run_id', None))


@dataclass
class DeleteTag:
    key: str
    run_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.run_id: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteTag':
        return cls(key=d.get('key', None), run_id=d.get('run_id', None))


@dataclass
class DeleteTransitionRequestRequest:
    """Delete a ransition request"""

    comment: str
    creator: str
    name: str
    stage: str
    version: str


@dataclass
class Experiment:
    artifact_location: str
    creation_time: int
    experiment_id: str
    last_update_time: int
    lifecycle_stage: str
    name: str
    tags: 'List[ExperimentTag]'

    def as_dict(self) -> dict:
        body = {}
        if self.artifact_location: body['artifact_location'] = self.artifact_location
        if self.creation_time: body['creation_time'] = self.creation_time
        if self.experiment_id: body['experiment_id'] = self.experiment_id
        if self.last_update_time: body['last_update_time'] = self.last_update_time
        if self.lifecycle_stage: body['lifecycle_stage'] = self.lifecycle_stage
        if self.name: body['name'] = self.name
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
                   tags=[ExperimentTag.from_dict(v) for v in d['tags']] if 'tags' in d else None)


@dataclass
class ExperimentTag:
    key: str
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExperimentTag':
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class FileInfo:
    file_size: int
    is_dir: bool
    path: str

    def as_dict(self) -> dict:
        body = {}
        if self.file_size: body['file_size'] = self.file_size
        if self.is_dir: body['is_dir'] = self.is_dir
        if self.path: body['path'] = self.path
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
    experiment: 'Experiment'

    def as_dict(self) -> dict:
        body = {}
        if self.experiment: body['experiment'] = self.experiment.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetExperimentByNameResponse':
        return cls(experiment=Experiment.from_dict(d['experiment']) if 'experiment' in d else None)


@dataclass
class GetExperimentRequest:
    """Get an experiment"""

    experiment_id: str


@dataclass
class GetHistoryRequest:
    """Get all history"""

    metric_key: str
    run_id: str
    run_uuid: str


@dataclass
class GetLatestVersionsRequest:
    name: str
    stages: 'List[str]'

    def as_dict(self) -> dict:
        body = {}
        if self.name: body['name'] = self.name
        if self.stages: body['stages'] = [v for v in self.stages]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetLatestVersionsRequest':
        return cls(name=d.get('name', None), stages=d.get('stages', None))


@dataclass
class GetLatestVersionsResponse:
    model_versions: 'List[ModelVersion]'

    def as_dict(self) -> dict:
        body = {}
        if self.model_versions: body['model_versions'] = [v.as_dict() for v in self.model_versions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetLatestVersionsResponse':
        return cls(model_versions=[ModelVersion.from_dict(v)
                                   for v in d['model_versions']] if 'model_versions' in d else None)


@dataclass
class GetMLflowDatabrickRequest:
    """Get model"""

    name: str


@dataclass
class GetMetricHistoryResponse:
    metrics: 'List[Metric]'

    def as_dict(self) -> dict:
        body = {}
        if self.metrics: body['metrics'] = [v.as_dict() for v in self.metrics]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetMetricHistoryResponse':
        return cls(metrics=[Metric.from_dict(v) for v in d['metrics']] if 'metrics' in d else None)


@dataclass
class GetModelVersionDownloadUriRequest:
    """Get a model version URI"""

    name: str
    version: str


@dataclass
class GetModelVersionDownloadUriResponse:
    artifact_uri: str

    def as_dict(self) -> dict:
        body = {}
        if self.artifact_uri: body['artifact_uri'] = self.artifact_uri
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
    model_version: 'ModelVersion'

    def as_dict(self) -> dict:
        body = {}
        if self.model_version: body['model_version'] = self.model_version.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetModelVersionResponse':
        return cls(model_version=ModelVersion.from_dict(d['model_version']) if 'model_version' in d else None)


@dataclass
class GetRegisteredModelRequest:
    """Get a model"""

    name: str


@dataclass
class GetRegisteredModelResponse:
    registered_model: 'RegisteredModel'

    def as_dict(self) -> dict:
        body = {}
        if self.registered_model: body['registered_model'] = self.registered_model.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRegisteredModelResponse':
        return cls(registered_model=RegisteredModel.from_dict(d['registered_model']) if 'registered_model' in
                   d else None)


@dataclass
class GetResponse:
    registered_model: 'RegisteredModelDatabricks'

    def as_dict(self) -> dict:
        body = {}
        if self.registered_model: body['registered_model'] = self.registered_model.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetResponse':
        return cls(registered_model=RegisteredModelDatabricks.
                   from_dict(d['registered_model']) if 'registered_model' in d else None)


@dataclass
class GetRunRequest:
    """Get a run"""

    run_id: str
    run_uuid: str


@dataclass
class GetRunResponse:
    run: 'Run'

    def as_dict(self) -> dict:
        body = {}
        if self.run: body['run'] = self.run.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRunResponse':
        return cls(run=Run.from_dict(d['run']) if 'run' in d else None)


@dataclass
class HttpUrlSpec:
    authorization: str
    enable_ssl_verification: bool
    secret: str
    url: str

    def as_dict(self) -> dict:
        body = {}
        if self.authorization: body['authorization'] = self.authorization
        if self.enable_ssl_verification: body['enable_ssl_verification'] = self.enable_ssl_verification
        if self.secret: body['secret'] = self.secret
        if self.url: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'HttpUrlSpec':
        return cls(authorization=d.get('authorization', None),
                   enable_ssl_verification=d.get('enable_ssl_verification', None),
                   secret=d.get('secret', None),
                   url=d.get('url', None))


@dataclass
class HttpUrlSpecWithoutSecret:
    enable_ssl_verification: bool
    url: str

    def as_dict(self) -> dict:
        body = {}
        if self.enable_ssl_verification: body['enable_ssl_verification'] = self.enable_ssl_verification
        if self.url: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'HttpUrlSpecWithoutSecret':
        return cls(enable_ssl_verification=d.get('enable_ssl_verification', None), url=d.get('url', None))


@dataclass
class JobSpec:
    access_token: str
    job_id: str
    workspace_url: str

    def as_dict(self) -> dict:
        body = {}
        if self.access_token: body['access_token'] = self.access_token
        if self.job_id: body['job_id'] = self.job_id
        if self.workspace_url: body['workspace_url'] = self.workspace_url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobSpec':
        return cls(access_token=d.get('access_token', None),
                   job_id=d.get('job_id', None),
                   workspace_url=d.get('workspace_url', None))


@dataclass
class JobSpecWithoutSecret:
    job_id: str
    workspace_url: str

    def as_dict(self) -> dict:
        body = {}
        if self.job_id: body['job_id'] = self.job_id
        if self.workspace_url: body['workspace_url'] = self.workspace_url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'JobSpecWithoutSecret':
        return cls(job_id=d.get('job_id', None), workspace_url=d.get('workspace_url', None))


@dataclass
class ListArtifactsRequest:
    """Get all artifacts"""

    page_token: str
    path: str
    run_id: str
    run_uuid: str


@dataclass
class ListArtifactsResponse:
    files: 'List[FileInfo]'
    next_page_token: str
    root_uri: str

    def as_dict(self) -> dict:
        body = {}
        if self.files: body['files'] = [v.as_dict() for v in self.files]
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.root_uri: body['root_uri'] = self.root_uri
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListArtifactsResponse':
        return cls(files=[FileInfo.from_dict(v) for v in d['files']] if 'files' in d else None,
                   next_page_token=d.get('next_page_token', None),
                   root_uri=d.get('root_uri', None))


@dataclass
class ListExperimentsRequest:
    """List experiments"""

    max_results: int
    page_token: str
    view_type: str


@dataclass
class ListExperimentsResponse:
    experiments: 'List[Experiment]'
    next_page_token: str

    def as_dict(self) -> dict:
        body = {}
        if self.experiments: body['experiments'] = [v.as_dict() for v in self.experiments]
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListExperimentsResponse':
        return cls(experiments=[Experiment.from_dict(v)
                                for v in d['experiments']] if 'experiments' in d else None,
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListRegisteredModelsRequest:
    """List models"""

    max_results: int
    page_token: str


@dataclass
class ListRegisteredModelsResponse:
    next_page_token: str
    registered_models: 'List[RegisteredModel]'

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.registered_models: body['registered_models'] = [v.as_dict() for v in self.registered_models]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRegisteredModelsResponse':
        return cls(next_page_token=d.get('next_page_token', None),
                   registered_models=[RegisteredModel.from_dict(v)
                                      for v in d['registered_models']] if 'registered_models' in d else None)


@dataclass
class ListRegistryWebhooks:
    next_page_token: str
    webhooks: 'List[RegistryWebhook]'

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.webhooks: body['webhooks'] = [v.as_dict() for v in self.webhooks]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRegistryWebhooks':
        return cls(next_page_token=d.get('next_page_token', None),
                   webhooks=[RegistryWebhook.from_dict(v)
                             for v in d['webhooks']] if 'webhooks' in d else None)


@dataclass
class ListRegistryWebhooksRequest:
    """List registry webhooks"""

    events: 'List[RegistryWebhookEvent]'
    model_name: str
    page_token: str


@dataclass
class ListResponse:
    requests: 'List[Activity]'

    def as_dict(self) -> dict:
        body = {}
        if self.requests: body['requests'] = [v.as_dict() for v in self.requests]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListResponse':
        return cls(requests=[Activity.from_dict(v) for v in d['requests']] if 'requests' in d else None)


@dataclass
class ListTransitionRequestsRequest:
    """List transition requests"""

    name: str
    version: str


@dataclass
class LogBatch:
    metrics: 'List[Metric]'
    params: 'List[Param]'
    run_id: str
    tags: 'List[RunTag]'

    def as_dict(self) -> dict:
        body = {}
        if self.metrics: body['metrics'] = [v.as_dict() for v in self.metrics]
        if self.params: body['params'] = [v.as_dict() for v in self.params]
        if self.run_id: body['run_id'] = self.run_id
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogBatch':
        return cls(metrics=[Metric.from_dict(v) for v in d['metrics']] if 'metrics' in d else None,
                   params=[Param.from_dict(v) for v in d['params']] if 'params' in d else None,
                   run_id=d.get('run_id', None),
                   tags=[RunTag.from_dict(v) for v in d['tags']] if 'tags' in d else None)


@dataclass
class LogMetric:
    key: str
    run_id: str
    run_uuid: str
    step: int
    timestamp: int
    value: float

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.run_id: body['run_id'] = self.run_id
        if self.run_uuid: body['run_uuid'] = self.run_uuid
        if self.step: body['step'] = self.step
        if self.timestamp: body['timestamp'] = self.timestamp
        if self.value: body['value'] = self.value
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
    model_json: str
    run_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.model_json: body['model_json'] = self.model_json
        if self.run_id: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogModel':
        return cls(model_json=d.get('model_json', None), run_id=d.get('run_id', None))


@dataclass
class LogParam:
    key: str
    run_id: str
    run_uuid: str
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.run_id: body['run_id'] = self.run_id
        if self.run_uuid: body['run_uuid'] = self.run_uuid
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogParam':
        return cls(key=d.get('key', None),
                   run_id=d.get('run_id', None),
                   run_uuid=d.get('run_uuid', None),
                   value=d.get('value', None))


@dataclass
class Metric:
    key: str
    step: int
    timestamp: int
    value: float

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.step: body['step'] = self.step
        if self.timestamp: body['timestamp'] = self.timestamp
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Metric':
        return cls(key=d.get('key', None),
                   step=d.get('step', None),
                   timestamp=d.get('timestamp', None),
                   value=d.get('value', None))


@dataclass
class ModelVersion:
    creation_timestamp: int
    current_stage: str
    description: str
    last_updated_timestamp: int
    name: str
    run_id: str
    run_link: str
    source: str
    status: 'ModelVersionStatus'
    status_message: str
    tags: 'List[ModelVersionTag]'
    user_id: str
    version: str

    def as_dict(self) -> dict:
        body = {}
        if self.creation_timestamp: body['creation_timestamp'] = self.creation_timestamp
        if self.current_stage: body['current_stage'] = self.current_stage
        if self.description: body['description'] = self.description
        if self.last_updated_timestamp: body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.name: body['name'] = self.name
        if self.run_id: body['run_id'] = self.run_id
        if self.run_link: body['run_link'] = self.run_link
        if self.source: body['source'] = self.source
        if self.status: body['status'] = self.status.value
        if self.status_message: body['status_message'] = self.status_message
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        if self.user_id: body['user_id'] = self.user_id
        if self.version: body['version'] = self.version
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
                   status=ModelVersionStatus(d['status']) if 'status' in d else None,
                   status_message=d.get('status_message', None),
                   tags=[ModelVersionTag.from_dict(v) for v in d['tags']] if 'tags' in d else None,
                   user_id=d.get('user_id', None),
                   version=d.get('version', None))


@dataclass
class ModelVersionDatabricks:
    creation_timestamp: int
    current_stage: 'Stage'
    description: str
    last_updated_timestamp: int
    name: str
    permission_level: 'PermissionLevel'
    run_id: str
    run_link: str
    source: str
    status: 'Status'
    status_message: str
    tags: 'List[ModelVersionTag]'
    user_id: str
    version: str

    def as_dict(self) -> dict:
        body = {}
        if self.creation_timestamp: body['creation_timestamp'] = self.creation_timestamp
        if self.current_stage: body['current_stage'] = self.current_stage.value
        if self.description: body['description'] = self.description
        if self.last_updated_timestamp: body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.name: body['name'] = self.name
        if self.permission_level: body['permission_level'] = self.permission_level.value
        if self.run_id: body['run_id'] = self.run_id
        if self.run_link: body['run_link'] = self.run_link
        if self.source: body['source'] = self.source
        if self.status: body['status'] = self.status.value
        if self.status_message: body['status_message'] = self.status_message
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        if self.user_id: body['user_id'] = self.user_id
        if self.version: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ModelVersionDatabricks':
        return cls(
            creation_timestamp=d.get('creation_timestamp', None),
            current_stage=Stage(d['current_stage']) if 'current_stage' in d else None,
            description=d.get('description', None),
            last_updated_timestamp=d.get('last_updated_timestamp', None),
            name=d.get('name', None),
            permission_level=PermissionLevel(d['permission_level']) if 'permission_level' in d else None,
            run_id=d.get('run_id', None),
            run_link=d.get('run_link', None),
            source=d.get('source', None),
            status=Status(d['status']) if 'status' in d else None,
            status_message=d.get('status_message', None),
            tags=[ModelVersionTag.from_dict(v) for v in d['tags']] if 'tags' in d else None,
            user_id=d.get('user_id', None),
            version=d.get('version', None))


class ModelVersionStatus(Enum):
    """Current status of `model_version`"""

    FAILED_REGISTRATION = 'FAILED_REGISTRATION'
    PENDING_REGISTRATION = 'PENDING_REGISTRATION'
    READY = 'READY'


@dataclass
class ModelVersionTag:
    key: str
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ModelVersionTag':
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class Param:
    key: str
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.value: body['value'] = self.value
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
class RegisteredModel:
    creation_timestamp: int
    description: str
    last_updated_timestamp: int
    latest_versions: 'List[ModelVersion]'
    name: str
    tags: 'List[RegisteredModelTag]'
    user_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.creation_timestamp: body['creation_timestamp'] = self.creation_timestamp
        if self.description: body['description'] = self.description
        if self.last_updated_timestamp: body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.latest_versions: body['latest_versions'] = [v.as_dict() for v in self.latest_versions]
        if self.name: body['name'] = self.name
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        if self.user_id: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RegisteredModel':
        return cls(creation_timestamp=d.get('creation_timestamp', None),
                   description=d.get('description', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   latest_versions=[ModelVersion.from_dict(v)
                                    for v in d['latest_versions']] if 'latest_versions' in d else None,
                   name=d.get('name', None),
                   tags=[RegisteredModelTag.from_dict(v) for v in d['tags']] if 'tags' in d else None,
                   user_id=d.get('user_id', None))


@dataclass
class RegisteredModelDatabricks:
    creation_timestamp: int
    description: str
    id: str
    last_updated_timestamp: int
    latest_versions: 'List[ModelVersion]'
    name: str
    permission_level: 'PermissionLevel'
    tags: 'List[RegisteredModelTag]'
    user_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.creation_timestamp: body['creation_timestamp'] = self.creation_timestamp
        if self.description: body['description'] = self.description
        if self.id: body['id'] = self.id
        if self.last_updated_timestamp: body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.latest_versions: body['latest_versions'] = [v.as_dict() for v in self.latest_versions]
        if self.name: body['name'] = self.name
        if self.permission_level: body['permission_level'] = self.permission_level.value
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        if self.user_id: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RegisteredModelDatabricks':
        return cls(
            creation_timestamp=d.get('creation_timestamp', None),
            description=d.get('description', None),
            id=d.get('id', None),
            last_updated_timestamp=d.get('last_updated_timestamp', None),
            latest_versions=[ModelVersion.from_dict(v)
                             for v in d['latest_versions']] if 'latest_versions' in d else None,
            name=d.get('name', None),
            permission_level=PermissionLevel(d['permission_level']) if 'permission_level' in d else None,
            tags=[RegisteredModelTag.from_dict(v) for v in d['tags']] if 'tags' in d else None,
            user_id=d.get('user_id', None))


@dataclass
class RegisteredModelTag:
    key: str
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RegisteredModelTag':
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class RegistryWebhook:
    creation_timestamp: int
    description: str
    events: 'List[RegistryWebhookEvent]'
    http_url_spec: 'HttpUrlSpecWithoutSecret'
    id: str
    job_spec: 'JobSpecWithoutSecret'
    last_updated_timestamp: int
    model_name: str
    status: 'RegistryWebhookStatus'

    def as_dict(self) -> dict:
        body = {}
        if self.creation_timestamp: body['creation_timestamp'] = self.creation_timestamp
        if self.description: body['description'] = self.description
        if self.events: body['events'] = [v for v in self.events]
        if self.http_url_spec: body['http_url_spec'] = self.http_url_spec.as_dict()
        if self.id: body['id'] = self.id
        if self.job_spec: body['job_spec'] = self.job_spec.as_dict()
        if self.last_updated_timestamp: body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.model_name: body['model_name'] = self.model_name
        if self.status: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RegistryWebhook':
        return cls(creation_timestamp=d.get('creation_timestamp', None),
                   description=d.get('description', None),
                   events=d.get('events', None),
                   http_url_spec=HttpUrlSpecWithoutSecret.from_dict(d['http_url_spec'])
                   if 'http_url_spec' in d else None,
                   id=d.get('id', None),
                   job_spec=JobSpecWithoutSecret.from_dict(d['job_spec']) if 'job_spec' in d else None,
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   model_name=d.get('model_name', None),
                   status=RegistryWebhookStatus(d['status']) if 'status' in d else None)


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
class RejectResponse:
    activity: 'Activity'

    def as_dict(self) -> dict:
        body = {}
        if self.activity: body['activity'] = self.activity.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RejectResponse':
        return cls(activity=Activity.from_dict(d['activity']) if 'activity' in d else None)


@dataclass
class RejectTransitionRequest:
    comment: str
    name: str
    stage: 'Stage'
    version: str

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.name: body['name'] = self.name
        if self.stage: body['stage'] = self.stage.value
        if self.version: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RejectTransitionRequest':
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   stage=Stage(d['stage']) if 'stage' in d else None,
                   version=d.get('version', None))


@dataclass
class RenameRegisteredModelRequest:
    name: str
    new_name: str

    def as_dict(self) -> dict:
        body = {}
        if self.name: body['name'] = self.name
        if self.new_name: body['new_name'] = self.new_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RenameRegisteredModelRequest':
        return cls(name=d.get('name', None), new_name=d.get('new_name', None))


@dataclass
class RenameRegisteredModelResponse:
    registered_model: 'RegisteredModel'

    def as_dict(self) -> dict:
        body = {}
        if self.registered_model: body['registered_model'] = self.registered_model.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RenameRegisteredModelResponse':
        return cls(registered_model=RegisteredModel.from_dict(d['registered_model']) if 'registered_model' in
                   d else None)


@dataclass
class RestoreExperiment:
    experiment_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.experiment_id: body['experiment_id'] = self.experiment_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RestoreExperiment':
        return cls(experiment_id=d.get('experiment_id', None))


@dataclass
class RestoreRun:
    run_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.run_id: body['run_id'] = self.run_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RestoreRun':
        return cls(run_id=d.get('run_id', None))


@dataclass
class Run:
    data: 'RunData'
    info: 'RunInfo'

    def as_dict(self) -> dict:
        body = {}
        if self.data: body['data'] = self.data.as_dict()
        if self.info: body['info'] = self.info.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Run':
        return cls(data=RunData.from_dict(d['data']) if 'data' in d else None,
                   info=RunInfo.from_dict(d['info']) if 'info' in d else None)


@dataclass
class RunData:
    metrics: 'List[Metric]'
    params: 'List[Param]'
    tags: 'List[RunTag]'

    def as_dict(self) -> dict:
        body = {}
        if self.metrics: body['metrics'] = [v.as_dict() for v in self.metrics]
        if self.params: body['params'] = [v.as_dict() for v in self.params]
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunData':
        return cls(metrics=[Metric.from_dict(v) for v in d['metrics']] if 'metrics' in d else None,
                   params=[Param.from_dict(v) for v in d['params']] if 'params' in d else None,
                   tags=[RunTag.from_dict(v) for v in d['tags']] if 'tags' in d else None)


@dataclass
class RunInfo:
    artifact_uri: str
    end_time: int
    experiment_id: str
    lifecycle_stage: str
    run_id: str
    run_uuid: str
    start_time: int
    status: 'RunInfoStatus'
    user_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.artifact_uri: body['artifact_uri'] = self.artifact_uri
        if self.end_time: body['end_time'] = self.end_time
        if self.experiment_id: body['experiment_id'] = self.experiment_id
        if self.lifecycle_stage: body['lifecycle_stage'] = self.lifecycle_stage
        if self.run_id: body['run_id'] = self.run_id
        if self.run_uuid: body['run_uuid'] = self.run_uuid
        if self.start_time: body['start_time'] = self.start_time
        if self.status: body['status'] = self.status.value
        if self.user_id: body['user_id'] = self.user_id
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
                   status=RunInfoStatus(d['status']) if 'status' in d else None,
                   user_id=d.get('user_id', None))


class RunInfoStatus(Enum):
    """Current status of the run."""

    FAILED = 'FAILED'
    FINISHED = 'FINISHED'
    KILLED = 'KILLED'
    RUNNING = 'RUNNING'
    SCHEDULED = 'SCHEDULED'


@dataclass
class RunTag:
    key: str
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RunTag':
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class SearchExperiments:
    filter: str
    max_results: int
    order_by: 'List[str]'
    page_token: str
    view_type: 'SearchExperimentsViewType'

    def as_dict(self) -> dict:
        body = {}
        if self.filter: body['filter'] = self.filter
        if self.max_results: body['max_results'] = self.max_results
        if self.order_by: body['order_by'] = [v for v in self.order_by]
        if self.page_token: body['page_token'] = self.page_token
        if self.view_type: body['view_type'] = self.view_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SearchExperiments':
        return cls(filter=d.get('filter', None),
                   max_results=d.get('max_results', None),
                   order_by=d.get('order_by', None),
                   page_token=d.get('page_token', None),
                   view_type=SearchExperimentsViewType(d['view_type']) if 'view_type' in d else None)


@dataclass
class SearchExperimentsResponse:
    experiments: 'List[Experiment]'
    next_page_token: str

    def as_dict(self) -> dict:
        body = {}
        if self.experiments: body['experiments'] = [v.as_dict() for v in self.experiments]
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SearchExperimentsResponse':
        return cls(experiments=[Experiment.from_dict(v)
                                for v in d['experiments']] if 'experiments' in d else None,
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

    filter: str
    max_results: int
    order_by: 'List[str]'
    page_token: str


@dataclass
class SearchModelVersionsResponse:
    model_versions: 'List[ModelVersion]'
    next_page_token: str

    def as_dict(self) -> dict:
        body = {}
        if self.model_versions: body['model_versions'] = [v.as_dict() for v in self.model_versions]
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SearchModelVersionsResponse':
        return cls(model_versions=[ModelVersion.from_dict(v)
                                   for v in d['model_versions']] if 'model_versions' in d else None,
                   next_page_token=d.get('next_page_token', None))


@dataclass
class SearchRegisteredModelsRequest:
    """Search models"""

    filter: str
    max_results: int
    order_by: 'List[str]'
    page_token: str


@dataclass
class SearchRegisteredModelsResponse:
    next_page_token: str
    registered_models: 'List[RegisteredModel]'

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.registered_models: body['registered_models'] = [v.as_dict() for v in self.registered_models]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SearchRegisteredModelsResponse':
        return cls(next_page_token=d.get('next_page_token', None),
                   registered_models=[RegisteredModel.from_dict(v)
                                      for v in d['registered_models']] if 'registered_models' in d else None)


@dataclass
class SearchRuns:
    experiment_ids: 'List[str]'
    filter: str
    max_results: int
    order_by: 'List[str]'
    page_token: str
    run_view_type: 'SearchRunsRunViewType'

    def as_dict(self) -> dict:
        body = {}
        if self.experiment_ids: body['experiment_ids'] = [v for v in self.experiment_ids]
        if self.filter: body['filter'] = self.filter
        if self.max_results: body['max_results'] = self.max_results
        if self.order_by: body['order_by'] = [v for v in self.order_by]
        if self.page_token: body['page_token'] = self.page_token
        if self.run_view_type: body['run_view_type'] = self.run_view_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SearchRuns':
        return cls(experiment_ids=d.get('experiment_ids', None),
                   filter=d.get('filter', None),
                   max_results=d.get('max_results', None),
                   order_by=d.get('order_by', None),
                   page_token=d.get('page_token', None),
                   run_view_type=SearchRunsRunViewType(d['run_view_type']) if 'run_view_type' in d else None)


@dataclass
class SearchRunsResponse:
    next_page_token: str
    runs: 'List[Run]'

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.runs: body['runs'] = [v.as_dict() for v in self.runs]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SearchRunsResponse':
        return cls(next_page_token=d.get('next_page_token', None),
                   runs=[Run.from_dict(v) for v in d['runs']] if 'runs' in d else None)


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
        if self.experiment_id: body['experiment_id'] = self.experiment_id
        if self.key: body['key'] = self.key
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetExperimentTag':
        return cls(experiment_id=d.get('experiment_id', None),
                   key=d.get('key', None),
                   value=d.get('value', None))


@dataclass
class SetModelVersionTagRequest:
    key: str
    name: str
    value: str
    version: str

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.name: body['name'] = self.name
        if self.value: body['value'] = self.value
        if self.version: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetModelVersionTagRequest':
        return cls(key=d.get('key', None),
                   name=d.get('name', None),
                   value=d.get('value', None),
                   version=d.get('version', None))


@dataclass
class SetRegisteredModelTagRequest:
    key: str
    name: str
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.name: body['name'] = self.name
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetRegisteredModelTagRequest':
        return cls(key=d.get('key', None), name=d.get('name', None), value=d.get('value', None))


@dataclass
class SetTag:
    key: str
    run_id: str
    run_uuid: str
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.run_id: body['run_id'] = self.run_id
        if self.run_uuid: body['run_uuid'] = self.run_uuid
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetTag':
        return cls(key=d.get('key', None),
                   run_id=d.get('run_id', None),
                   run_uuid=d.get('run_uuid', None),
                   value=d.get('value', None))


class Stage(Enum):
    """This describes an enum"""

    Archived = 'Archived'
    None_ = 'None'
    Production = 'Production'
    Staging = 'Staging'


class Status(Enum):
    """This describes an enum"""

    FAILED_REGISTRATION = 'FAILED_REGISTRATION'
    PENDING_REGISTRATION = 'PENDING_REGISTRATION'
    READY = 'READY'


@dataclass
class TestRegistryWebhook:
    """Test webhook response object."""

    body: str
    status_code: int

    def as_dict(self) -> dict:
        body = {}
        if self.body: body['body'] = self.body
        if self.status_code: body['status_code'] = self.status_code
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TestRegistryWebhook':
        return cls(body=d.get('body', None), status_code=d.get('status_code', None))


@dataclass
class TestRegistryWebhookRequest:
    event: 'RegistryWebhookEvent'
    id: str

    def as_dict(self) -> dict:
        body = {}
        if self.event: body['event'] = self.event.value
        if self.id: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TestRegistryWebhookRequest':
        return cls(event=RegistryWebhookEvent(d['event']) if 'event' in d else None, id=d.get('id', None))


@dataclass
class TestRegistryWebhookResponse:
    webhook: 'TestRegistryWebhook'

    def as_dict(self) -> dict:
        body = {}
        if self.webhook: body['webhook'] = self.webhook.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TestRegistryWebhookResponse':
        return cls(webhook=TestRegistryWebhook.from_dict(d['webhook']) if 'webhook' in d else None)


@dataclass
class TransitionModelVersionStage:
    archive_existing_versions: bool
    name: str
    stage: str
    version: str

    def as_dict(self) -> dict:
        body = {}
        if self.archive_existing_versions: body['archive_existing_versions'] = self.archive_existing_versions
        if self.name: body['name'] = self.name
        if self.stage: body['stage'] = self.stage
        if self.version: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TransitionModelVersionStage':
        return cls(archive_existing_versions=d.get('archive_existing_versions', None),
                   name=d.get('name', None),
                   stage=d.get('stage', None),
                   version=d.get('version', None))


@dataclass
class TransitionModelVersionStageDatabricks:
    archive_existing_versions: bool
    comment: str
    name: str
    stage: 'Stage'
    version: str

    def as_dict(self) -> dict:
        body = {}
        if self.archive_existing_versions: body['archive_existing_versions'] = self.archive_existing_versions
        if self.comment: body['comment'] = self.comment
        if self.name: body['name'] = self.name
        if self.stage: body['stage'] = self.stage.value
        if self.version: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TransitionModelVersionStageDatabricks':
        return cls(archive_existing_versions=d.get('archive_existing_versions', None),
                   comment=d.get('comment', None),
                   name=d.get('name', None),
                   stage=Stage(d['stage']) if 'stage' in d else None,
                   version=d.get('version', None))


@dataclass
class TransitionModelVersionStageResponse:
    model_version: 'ModelVersion'

    def as_dict(self) -> dict:
        body = {}
        if self.model_version: body['model_version'] = self.model_version.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TransitionModelVersionStageResponse':
        return cls(model_version=ModelVersion.from_dict(d['model_version']) if 'model_version' in d else None)


@dataclass
class TransitionRequest:
    """Transition request details."""

    available_actions: 'List[ActivityAction]'
    comment: str
    creation_timestamp: int
    to_stage: 'Stage'
    user_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.available_actions: body['available_actions'] = [v for v in self.available_actions]
        if self.comment: body['comment'] = self.comment
        if self.creation_timestamp: body['creation_timestamp'] = self.creation_timestamp
        if self.to_stage: body['to_stage'] = self.to_stage.value
        if self.user_id: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TransitionRequest':
        return cls(available_actions=d.get('available_actions', None),
                   comment=d.get('comment', None),
                   creation_timestamp=d.get('creation_timestamp', None),
                   to_stage=Stage(d['to_stage']) if 'to_stage' in d else None,
                   user_id=d.get('user_id', None))


@dataclass
class TransitionStageResponse:
    model_version: 'ModelVersionDatabricks'

    def as_dict(self) -> dict:
        body = {}
        if self.model_version: body['model_version'] = self.model_version.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TransitionStageResponse':
        return cls(model_version=ModelVersionDatabricks.from_dict(d['model_version']) if 'model_version' in
                   d else None)


@dataclass
class UpdateComment:
    comment: str
    id: str

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.id: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateComment':
        return cls(comment=d.get('comment', None), id=d.get('id', None))


@dataclass
class UpdateExperiment:
    experiment_id: str
    new_name: str

    def as_dict(self) -> dict:
        body = {}
        if self.experiment_id: body['experiment_id'] = self.experiment_id
        if self.new_name: body['new_name'] = self.new_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateExperiment':
        return cls(experiment_id=d.get('experiment_id', None), new_name=d.get('new_name', None))


@dataclass
class UpdateModelVersionRequest:
    description: str
    name: str
    version: str

    def as_dict(self) -> dict:
        body = {}
        if self.description: body['description'] = self.description
        if self.name: body['name'] = self.name
        if self.version: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateModelVersionRequest':
        return cls(description=d.get('description', None),
                   name=d.get('name', None),
                   version=d.get('version', None))


@dataclass
class UpdateRegisteredModelRequest:
    description: str
    name: str

    def as_dict(self) -> dict:
        body = {}
        if self.description: body['description'] = self.description
        if self.name: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateRegisteredModelRequest':
        return cls(description=d.get('description', None), name=d.get('name', None))


@dataclass
class UpdateRegistryWebhook:
    description: str
    events: 'List[RegistryWebhookEvent]'
    http_url_spec: 'HttpUrlSpec'
    id: str
    job_spec: 'JobSpec'
    status: 'RegistryWebhookStatus'

    def as_dict(self) -> dict:
        body = {}
        if self.description: body['description'] = self.description
        if self.events: body['events'] = [v for v in self.events]
        if self.http_url_spec: body['http_url_spec'] = self.http_url_spec.as_dict()
        if self.id: body['id'] = self.id
        if self.job_spec: body['job_spec'] = self.job_spec.as_dict()
        if self.status: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateRegistryWebhook':
        return cls(description=d.get('description', None),
                   events=d.get('events', None),
                   http_url_spec=HttpUrlSpec.from_dict(d['http_url_spec']) if 'http_url_spec' in d else None,
                   id=d.get('id', None),
                   job_spec=JobSpec.from_dict(d['job_spec']) if 'job_spec' in d else None,
                   status=RegistryWebhookStatus(d['status']) if 'status' in d else None)


@dataclass
class UpdateResponse:
    comment: 'CommentObject'

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateResponse':
        return cls(comment=CommentObject.from_dict(d['comment']) if 'comment' in d else None)


@dataclass
class UpdateRun:
    end_time: int
    run_id: str
    run_uuid: str
    status: 'UpdateRunStatus'

    def as_dict(self) -> dict:
        body = {}
        if self.end_time: body['end_time'] = self.end_time
        if self.run_id: body['run_id'] = self.run_id
        if self.run_uuid: body['run_uuid'] = self.run_uuid
        if self.status: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateRun':
        return cls(end_time=d.get('end_time', None),
                   run_id=d.get('run_id', None),
                   run_uuid=d.get('run_uuid', None),
                   status=UpdateRunStatus(d['status']) if 'status' in d else None)


@dataclass
class UpdateRunResponse:
    run_info: 'RunInfo'

    def as_dict(self) -> dict:
        body = {}
        if self.run_info: body['run_info'] = self.run_info.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateRunResponse':
        return cls(run_info=RunInfo.from_dict(d['run_info']) if 'run_info' in d else None)


class UpdateRunStatus(Enum):
    """Updated status of the run."""

    FAILED = 'FAILED'
    FINISHED = 'FINISHED'
    KILLED = 'KILLED'
    RUNNING = 'RUNNING'
    SCHEDULED = 'SCHEDULED'


class ExperimentsAPI:

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               *,
               artifact_location: str = None,
               tags: List[ExperimentTag] = None,
               **kwargs) -> CreateExperimentResponse:
        """Create experiment.
        
        Creates an experiment with a name. Returns the ID of the newly created experiment. Validates that
        another experiment with the same name does not already exist and fails if another experiment with the
        same name already exists.
        
        Throws `RESOURCE_ALREADY_EXISTS` if a experiment with the given name exists."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateExperiment(artifact_location=artifact_location, name=name, tags=tags)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/experiments/create', body=body)
        return CreateExperimentResponse.from_dict(json)

    def delete(self, experiment_id: str, **kwargs):
        """Delete an experiment.
        
        Marks an experiment and associated metadata, runs, metrics, params, and tags for deletion. If the
        experiment uses FileStore, artifacts associated with experiment are also deleted."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteExperiment(experiment_id=experiment_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/experiments/delete', body=body)

    def get(self, experiment_id: str, **kwargs) -> Experiment:
        """Get an experiment.
        
        Gets metadata for an experiment. This method works on deleted experiments."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetExperimentRequest(experiment_id=experiment_id)

        query = {}
        if experiment_id: query['experiment_id'] = request.experiment_id

        json = self._api.do('GET', '/api/2.0/mlflow/experiments/get', query=query)
        return Experiment.from_dict(json)

    def get_by_name(self, experiment_name: str, **kwargs) -> GetExperimentByNameResponse:
        """Get metadata.
        
        "Gets metadata for an experiment.
        
        This endpoint will return deleted experiments, but prefers the active experiment if an active and
        deleted experiment share the same name. If multiple deleted\nexperiments share the same name, the API
        will return one of them.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no experiment with the specified name exists.S"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetByNameRequest(experiment_name=experiment_name)

        query = {}
        if experiment_name: query['experiment_name'] = request.experiment_name

        json = self._api.do('GET', '/api/2.0/mlflow/experiments/get-by-name', query=query)
        return GetExperimentByNameResponse.from_dict(json)

    def list(self,
             *,
             max_results: int = None,
             page_token: str = None,
             view_type: str = None,
             **kwargs) -> ListExperimentsResponse:
        """List experiments.
        
        Gets a list of all experiments."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListExperimentsRequest(max_results=max_results,
                                             page_token=page_token,
                                             view_type=view_type)

        query = {}
        if max_results: query['max_results'] = request.max_results
        if page_token: query['page_token'] = request.page_token
        if view_type: query['view_type'] = request.view_type

        json = self._api.do('GET', '/api/2.0/mlflow/experiments/list', query=query)
        return ListExperimentsResponse.from_dict(json)

    def restore(self, experiment_id: str, **kwargs):
        """Restores an experiment.
        
        "Restore an experiment marked for deletion. This also restores\nassociated metadata, runs, metrics,
        params, and tags. If experiment uses FileStore, underlying\nartifacts associated with experiment are
        also restored.\n\nThrows `RESOURCE_DOES_NOT_EXIST` if experiment was never created or was permanently
        deleted.","""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RestoreExperiment(experiment_id=experiment_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/experiments/restore', body=body)

    def search(self,
               *,
               filter: str = None,
               max_results: int = None,
               order_by: List[str] = None,
               page_token: str = None,
               view_type: SearchExperimentsViewType = None,
               **kwargs) -> SearchExperimentsResponse:
        """Search experiments.
        
        Searches for experiments that satisfy specified search criteria."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SearchExperiments(filter=filter,
                                        max_results=max_results,
                                        order_by=order_by,
                                        page_token=page_token,
                                        view_type=view_type)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/experiments/search', body=body)
        return SearchExperimentsResponse.from_dict(json)

    def set_experiment_tag(self, experiment_id: str, key: str, value: str, **kwargs):
        """Set a tag.
        
        Sets a tag on an experiment. Experiment tags are metadata that can be updated."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SetExperimentTag(experiment_id=experiment_id, key=key, value=value)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/experiments/set-experiment-tag', body=body)

    def update(self, experiment_id: str, *, new_name: str = None, **kwargs):
        """Update an experiment.
        
        Updates experiment metadata."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateExperiment(experiment_id=experiment_id, new_name=new_name)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/experiments/update', body=body)


class MLflowArtifactsAPI:

    def __init__(self, api_client):
        self._api = api_client

    def list(self,
             *,
             page_token: str = None,
             path: str = None,
             run_id: str = None,
             run_uuid: str = None,
             **kwargs) -> ListArtifactsResponse:
        """Get all artifacts.
        
        List artifacts for a run. Takes an optional `artifact_path` prefix. If it is specified, the response
        contains only artifacts with the specified prefix.","""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListArtifactsRequest(page_token=page_token, path=path, run_id=run_id, run_uuid=run_uuid)

        query = {}
        if page_token: query['page_token'] = request.page_token
        if path: query['path'] = request.path
        if run_id: query['run_id'] = request.run_id
        if run_uuid: query['run_uuid'] = request.run_uuid

        json = self._api.do('GET', '/api/2.0/mlflow/artifacts/list', query=query)
        return ListArtifactsResponse.from_dict(json)


class MLflowDatabricksAPI:
    """These endpoints are modified versions of the MLflow API that accept additional input parameters or return
    additional information."""

    def __init__(self, api_client):
        self._api = api_client

    def get(self, name: str, **kwargs) -> GetResponse:
        """Get model.
        
        Get the details of a model. This is a Databricks Workspace version of the [MLflow endpoint] that also
        returns the model's Databricks Workspace ID and the permission level of the requesting user on the
        model.
        
        [MLflow endpoint]: https://www.mlflow.org/docs/latest/rest-api.html#get-registeredmodel"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetMLflowDatabrickRequest(name=name)

        query = {}
        if name: query['name'] = request.name

        json = self._api.do('GET', '/api/2.0/mlflow/databricks/registered-models/get', query=query)
        return GetResponse.from_dict(json)

    def transition_stage(self,
                         name: str,
                         version: str,
                         stage: Stage,
                         archive_existing_versions: bool,
                         *,
                         comment: str = None,
                         **kwargs) -> TransitionStageResponse:
        """Transition a stage.
        
        Transition a model version's stage. This is a Databricks Workspace version of the [MLflow endpoint]
        that also accepts a comment associated with the transition to be recorded.",
        
        [MLflow endpoint]: https://www.mlflow.org/docs/latest/rest-api.html#transition-modelversion-stage"""
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


class MLflowMetricsAPI:

    def __init__(self, api_client):
        self._api = api_client

    def get_history(self,
                    metric_key: str,
                    *,
                    run_id: str = None,
                    run_uuid: str = None,
                    **kwargs) -> GetMetricHistoryResponse:
        """Get all history.
        
        Gets a list of all values for the specified metric for a given run."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetHistoryRequest(metric_key=metric_key, run_id=run_id, run_uuid=run_uuid)

        query = {}
        if metric_key: query['metric_key'] = request.metric_key
        if run_id: query['run_id'] = request.run_id
        if run_uuid: query['run_uuid'] = request.run_uuid

        json = self._api.do('GET', '/api/2.0/mlflow/metrics/get-history', query=query)
        return GetMetricHistoryResponse.from_dict(json)


class MLflowRunsAPI:

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               experiment_id: str = None,
               start_time: int = None,
               tags: List[RunTag] = None,
               user_id: str = None,
               **kwargs) -> CreateRunResponse:
        """Create a run.
        
        Creates a new run within an experiment. A run is usually a single execution of a machine learning or
        data ETL pipeline. MLflow uses runs to track the `mlflowParam`, `mlflowMetric` and `mlflowRunTag`
        associated with a single execution."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateRun(experiment_id=experiment_id,
                                start_time=start_time,
                                tags=tags,
                                user_id=user_id)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/runs/create', body=body)
        return CreateRunResponse.from_dict(json)

    def delete(self, run_id: str, **kwargs):
        """Delete a run.
        
        Marks a run for deletion."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteRun(run_id=run_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/delete', body=body)

    def delete_tag(self, run_id: str, key: str, **kwargs):
        """Delete a tag.
        
        Deletes a tag on a run. Tags are run metadata that can be updated during a run and after a run
        completes."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteTag(key=key, run_id=run_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/delete-tag', body=body)

    def get(self, run_id: str, *, run_uuid: str = None, **kwargs) -> GetRunResponse:
        """Get a run.
        
        "Gets the metadata, metrics, params, and tags for a run. In the case where multiple metrics with the
        same key are logged for a run, return only the value with the latest timestamp.
        
        If there are multiple values with the latest timestamp, return the maximum of these values."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetRunRequest(run_id=run_id, run_uuid=run_uuid)

        query = {}
        if run_id: query['run_id'] = request.run_id
        if run_uuid: query['run_uuid'] = request.run_uuid

        json = self._api.do('GET', '/api/2.0/mlflow/runs/get', query=query)
        return GetRunResponse.from_dict(json)

    def log_batch(self,
                  *,
                  metrics: List[Metric] = None,
                  params: List[Param] = None,
                  run_id: str = None,
                  tags: List[RunTag] = None,
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
        
        * No more than 1000 metrics, params, and tags in total * Up to 1000 metrics\n- Up to 100 params * Up
        to 100 tags
        
        For example, a valid request might contain 900 metrics, 50 params, and 50 tags, but logging 900
        metrics, 50 params, and 51 tags is invalid.
        
        The following limits also apply to metric, param, and tag keys and values:
        
        * Metric keyes, param keys, and tag keys can be up to 250 characters in length * Parameter and tag
        values can be up to 250 characters in length"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = LogBatch(metrics=metrics, params=params, run_id=run_id, tags=tags)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/log-batch', body=body)

    def log_metric(self,
                   key: str,
                   value: float,
                   timestamp: int,
                   *,
                   run_id: str = None,
                   run_uuid: str = None,
                   step: int = None,
                   **kwargs):
        """Log a metric.
        
        Logs a metric for a run. A metric is a key-value pair (string key, float value) with an associated
        timestamp. Examples include the various metrics that represent ML model accuracy. A metric can be
        logged multiple times."""
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

    def log_model(self, *, model_json: str = None, run_id: str = None, **kwargs):
        """Log a model.
        
        **NOTE:** Experimental: This API may change or be removed in a future release without warning."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = LogModel(model_json=model_json, run_id=run_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/log-model', body=body)

    def log_parameter(self, key: str, value: str, *, run_id: str = None, run_uuid: str = None, **kwargs):
        """Log a param.
        
        Logs a param used for a run. A param is a key-value pair (string key, string value). Examples include
        hyperparameters used for ML model training and constant dates and values used in an ETL pipeline. A
        param can be logged only once for a run."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = LogParam(key=key, run_id=run_id, run_uuid=run_uuid, value=value)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/log-parameter', body=body)

    def restore(self, run_id: str, **kwargs):
        """Restore a run.
        
        Restores a deleted run."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RestoreRun(run_id=run_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/restore', body=body)

    def search(self,
               *,
               experiment_ids: List[str] = None,
               filter: str = None,
               max_results: int = None,
               order_by: List[str] = None,
               page_token: str = None,
               run_view_type: SearchRunsRunViewType = None,
               **kwargs) -> SearchRunsResponse:
        """Search for runs.
        
        Searches for runs that satisfy expressions.
        
        Search expressions can use `mlflowMetric` and `mlflowParam` keys.","""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SearchRuns(experiment_ids=experiment_ids,
                                 filter=filter,
                                 max_results=max_results,
                                 order_by=order_by,
                                 page_token=page_token,
                                 run_view_type=run_view_type)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/runs/search', body=body)
        return SearchRunsResponse.from_dict(json)

    def set_tag(self, key: str, value: str, *, run_id: str = None, run_uuid: str = None, **kwargs):
        """Set a tag.
        
        Sets a tag on a run. Tags are run metadata that can be updated during a run and after a run completes."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SetTag(key=key, run_id=run_id, run_uuid=run_uuid, value=value)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/runs/set-tag', body=body)

    def update(self,
               *,
               end_time: int = None,
               run_id: str = None,
               run_uuid: str = None,
               status: UpdateRunStatus = None,
               **kwargs) -> UpdateRunResponse:
        """Update a run.
        
        Updates run metadata."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateRun(end_time=end_time, run_id=run_id, run_uuid=run_uuid, status=status)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/runs/update', body=body)
        return UpdateRunResponse.from_dict(json)


class ModelVersionCommentsAPI:

    def __init__(self, api_client):
        self._api = api_client

    def create(self, name: str, version: str, comment: str, **kwargs) -> CreateResponse:
        """Post a comment.
        
        Posts a comment on a model version. A comment can be submitted either by a user or programmatically to
        display relevant information about the model. For example, test results or deployment errors."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateComment(comment=comment, name=name, version=version)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/comments/create', body=body)
        return CreateResponse.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a comment.
        
        Deletes a comment on a model version."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteModelVersionCommentRequest(id=id)

        query = {}
        if id: query['id'] = request.id

        self._api.do('DELETE', '/api/2.0/mlflow/comments/delete', query=query)

    def update(self, id: str, comment: str, **kwargs) -> UpdateResponse:
        """Update a comment.
        
        Post an edit to a comment on a model version."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateComment(comment=comment, id=id)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/comments/update', body=body)
        return UpdateResponse.from_dict(json)


class ModelVersionsAPI:

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               source: str,
               *,
               description: str = None,
               run_id: str = None,
               run_link: str = None,
               tags: List[ModelVersionTag] = None,
               **kwargs) -> CreateModelVersionResponse:
        """Create a model version.
        
        Creates a model version."""
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

    def delete(self, name: str, version: str, **kwargs):
        """Delete a model version.
        
        Deletes a model version."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteModelVersionRequest(name=name, version=version)

        query = {}
        if name: query['name'] = request.name
        if version: query['version'] = request.version

        self._api.do('DELETE', '/api/2.0/mlflow/model-versions/delete', query=query)

    def delete_tag(self, name: str, version: str, key: str, **kwargs):
        """Delete a model version tag.
        
        Deletes a model version tag."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteModelVersionTagRequest(key=key, name=name, version=version)

        query = {}
        if key: query['key'] = request.key
        if name: query['name'] = request.name
        if version: query['version'] = request.version

        self._api.do('DELETE', '/api/2.0/mlflow/model-versions/delete-tag', query=query)

    def get(self, name: str, version: str, **kwargs) -> GetModelVersionResponse:
        """Get a model version.
        
        Get a model version."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetModelVersionRequest(name=name, version=version)

        query = {}
        if name: query['name'] = request.name
        if version: query['version'] = request.version

        json = self._api.do('GET', '/api/2.0/mlflow/model-versions/get', query=query)
        return GetModelVersionResponse.from_dict(json)

    def get_download_uri(self, name: str, version: str, **kwargs) -> GetModelVersionDownloadUriResponse:
        """Get a model version URI.
        
        Gets a URI to download the model version."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetModelVersionDownloadUriRequest(name=name, version=version)

        query = {}
        if name: query['name'] = request.name
        if version: query['version'] = request.version

        json = self._api.do('GET', '/api/2.0/mlflow/model-versions/get-download-uri', query=query)
        return GetModelVersionDownloadUriResponse.from_dict(json)

    def search(self,
               *,
               filter: str = None,
               max_results: int = None,
               order_by: List[str] = None,
               page_token: str = None,
               **kwargs) -> SearchModelVersionsResponse:
        """Searches model versions.
        
        Searches for specific model versions based on the supplied __filter__."""
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

        json = self._api.do('GET', '/api/2.0/mlflow/model-versions/search', query=query)
        return SearchModelVersionsResponse.from_dict(json)

    def set_tag(self, name: str, version: str, key: str, value: str, **kwargs):
        """Set a version tag.
        
        Sets a model version tag."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SetModelVersionTagRequest(key=key, name=name, value=value, version=version)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/model-versions/set-tag', body=body)

    def transition_stage(self, name: str, version: str, stage: str, archive_existing_versions: bool,
                         **kwargs) -> TransitionModelVersionStageResponse:
        """Transition a stage.
        
        Transition to the next model stage."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = TransitionModelVersionStage(archive_existing_versions=archive_existing_versions,
                                                  name=name,
                                                  stage=stage,
                                                  version=version)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/model-versions/transition-stage', body=body)
        return TransitionModelVersionStageResponse.from_dict(json)

    def update(self, name: str, version: str, *, description: str = None, **kwargs):
        """Update model version.
        
        Updates the model version."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateModelVersionRequest(description=description, name=name, version=version)
        body = request.as_dict()
        self._api.do('PATCH', '/api/2.0/mlflow/model-versions/update', body=body)


class RegisteredModelsAPI:

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               *,
               description: str = None,
               tags: List[RegisteredModelTag] = None,
               **kwargs) -> CreateRegisteredModelResponse:
        """Create a model.
        
        Creates a new registered model with the name specified in the request body.
        
        Throws `RESOURCE_ALREADY_EXISTS` if a registered model with the given name exists."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateRegisteredModelRequest(description=description, name=name, tags=tags)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/registered-models/create', body=body)
        return CreateRegisteredModelResponse.from_dict(json)

    def delete(self, name: str, **kwargs):
        """Delete a model.
        
        Deletes a registered model."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteRegisteredModelRequest(name=name)

        query = {}
        if name: query['name'] = request.name

        self._api.do('DELETE', '/api/2.0/mlflow/registered-models/delete', query=query)

    def delete_tag(self, name: str, key: str, **kwargs):
        """Delete a model tag.
        
        Deletes the tag for a registered model."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteRegisteredModelTagRequest(key=key, name=name)

        query = {}
        if key: query['key'] = request.key
        if name: query['name'] = request.name

        self._api.do('DELETE', '/api/2.0/mlflow/registered-models/delete-tag', query=query)

    def get(self, name: str, **kwargs) -> GetRegisteredModelResponse:
        """Get a model.
        
        Gets the registered model that matches the specified ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetRegisteredModelRequest(name=name)

        query = {}
        if name: query['name'] = request.name

        json = self._api.do('GET', '/api/2.0/mlflow/registered-models/get', query=query)
        return GetRegisteredModelResponse.from_dict(json)

    def get_latest_versions(self,
                            name: str,
                            *,
                            stages: List[str] = None,
                            **kwargs) -> GetLatestVersionsResponse:
        """Get the latest version.
        
        Gets the latest version of a registered model."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetLatestVersionsRequest(name=name, stages=stages)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/registered-models/get-latest-versions', body=body)
        return GetLatestVersionsResponse.from_dict(json)

    def list(self,
             *,
             max_results: int = None,
             page_token: str = None,
             **kwargs) -> ListRegisteredModelsResponse:
        """List models.
        
        Lists all available registered models, up to the limit specified in __max_results__."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListRegisteredModelsRequest(max_results=max_results, page_token=page_token)

        query = {}
        if max_results: query['max_results'] = request.max_results
        if page_token: query['page_token'] = request.page_token

        json = self._api.do('GET', '/api/2.0/mlflow/registered-models/list', query=query)
        return ListRegisteredModelsResponse.from_dict(json)

    def rename(self, name: str, *, new_name: str = None, **kwargs) -> RenameRegisteredModelResponse:
        """Rename a model.
        
        Renames a registered model."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RenameRegisteredModelRequest(name=name, new_name=new_name)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/registered-models/rename', body=body)
        return RenameRegisteredModelResponse.from_dict(json)

    def search(self,
               *,
               filter: str = None,
               max_results: int = None,
               order_by: List[str] = None,
               page_token: str = None,
               **kwargs) -> SearchRegisteredModelsResponse:
        """Search models.
        
        Search for registered models based on the specified __filter__."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SearchRegisteredModelsRequest(filter=filter,
                                                    max_results=max_results,
                                                    order_by=order_by,
                                                    page_token=page_token)

        query = {}
        if filter: query['filter'] = request.filter
        if max_results: query['max_results'] = request.max_results
        if order_by: query['order_by'] = [v for v in request.order_by]
        if page_token: query['page_token'] = request.page_token

        json = self._api.do('GET', '/api/2.0/mlflow/registered-models/search', query=query)
        return SearchRegisteredModelsResponse.from_dict(json)

    def set_tag(self, name: str, key: str, value: str, **kwargs):
        """Set a tag.
        
        Sets a tag on a registered model."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SetRegisteredModelTagRequest(key=key, name=name, value=value)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/mlflow/registered-models/set-tag', body=body)

    def update(self, name: str, *, description: str = None, **kwargs):
        """Update model.
        
        Updates a registered model."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateRegisteredModelRequest(description=description, name=name)
        body = request.as_dict()
        self._api.do('PATCH', '/api/2.0/mlflow/registered-models/update', body=body)


class RegistryWebhooksAPI:

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               events: List[RegistryWebhookEvent],
               *,
               description: str = None,
               http_url_spec: HttpUrlSpec = None,
               job_spec: JobSpec = None,
               model_name: str = None,
               status: RegistryWebhookStatus = None,
               **kwargs) -> CreateResponse:
        """Create a webhook.
        
        **NOTE**: This endpoint is in Public Preview.
        
        Creates a registry webhook."""
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
        return CreateResponse.from_dict(json)

    def delete(self, *, id: str = None, **kwargs):
        """Delete a webhook.
        
        **NOTE:** This endpoint is in Public Preview.
        
        Deletes a registry webhook."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteRegistryWebhookRequest(id=id)

        query = {}
        if id: query['id'] = request.id

        self._api.do('DELETE', '/api/2.0/mlflow/registry-webhooks/delete', query=query)

    def list(self,
             *,
             events: List[RegistryWebhookEvent] = None,
             model_name: str = None,
             page_token: str = None,
             **kwargs) -> ListRegistryWebhooks:
        """List registry webhooks.
        
        **NOTE:** This endpoint is in Public Preview.
        
        Lists all registry webhooks."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListRegistryWebhooksRequest(events=events, model_name=model_name, page_token=page_token)

        query = {}
        if events: query['events'] = [v for v in request.events]
        if model_name: query['model_name'] = request.model_name
        if page_token: query['page_token'] = request.page_token

        json = self._api.do('GET', '/api/2.0/mlflow/registry-webhooks/list', query=query)
        return ListRegistryWebhooks.from_dict(json)

    def test(self, id: str, *, event: RegistryWebhookEvent = None, **kwargs) -> TestRegistryWebhookResponse:
        """Test a webhook.
        
        **NOTE:** This endpoint is in Public Preview.
        
        Tests a registry webhook."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = TestRegistryWebhookRequest(event=event, id=id)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/registry-webhooks/test', body=body)
        return TestRegistryWebhookResponse.from_dict(json)

    def update(self,
               id: str,
               *,
               description: str = None,
               events: List[RegistryWebhookEvent] = None,
               http_url_spec: HttpUrlSpec = None,
               job_spec: JobSpec = None,
               status: RegistryWebhookStatus = None,
               **kwargs):
        """Update a webhook.
        
        **NOTE:** This endpoint is in Public Preview.
        
        Updates a registry webhook."""
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


class TransitionRequestsAPI:

    def __init__(self, api_client):
        self._api = api_client

    def approve(self,
                name: str,
                version: str,
                stage: Stage,
                archive_existing_versions: bool,
                *,
                comment: str = None,
                **kwargs) -> ApproveResponse:
        """Approve transition requests.
        
        Approves a model version stage transition request."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ApproveTransitionRequest(archive_existing_versions=archive_existing_versions,
                                               comment=comment,
                                               name=name,
                                               stage=stage,
                                               version=version)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/transition-requests/approve', body=body)
        return ApproveResponse.from_dict(json)

    def create(self,
               name: str,
               version: str,
               stage: Stage,
               *,
               comment: str = None,
               **kwargs) -> CreateResponse:
        """Make a transition request.
        
        Creates a model version stage transition request."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateTransitionRequest(comment=comment, name=name, stage=stage, version=version)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/transition-requests/create', body=body)
        return CreateResponse.from_dict(json)

    def delete(self, name: str, version: str, stage: str, creator: str, *, comment: str = None, **kwargs):
        """Delete a ransition request.
        
        Cancels a model version stage transition request."""
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
        if stage: query['stage'] = request.stage
        if version: query['version'] = request.version

        self._api.do('DELETE', '/api/2.0/mlflow/transition-requests/delete', query=query)

    def list(self, name: str, version: str, **kwargs) -> ListResponse:
        """List transition requests.
        
        Gets a list of all open stage transition requests for the model version."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListTransitionRequestsRequest(name=name, version=version)

        query = {}
        if name: query['name'] = request.name
        if version: query['version'] = request.version

        json = self._api.do('GET', '/api/2.0/mlflow/transition-requests/list', query=query)
        return ListResponse.from_dict(json)

    def reject(self,
               name: str,
               version: str,
               stage: Stage,
               *,
               comment: str = None,
               **kwargs) -> RejectResponse:
        """Reject a transition request.
        
        Rejects a model version stage transition request."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RejectTransitionRequest(comment=comment, name=name, stage=stage, version=version)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/mlflow/transition-requests/reject', body=body)
        return RejectResponse.from_dict(json)

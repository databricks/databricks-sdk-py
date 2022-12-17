# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List

from .clusters import (AutoScale, AwsAttributes, AzureAttributes,
                       ClusterLogConf, GcpAttributes)
from .libraries import MavenLibrary

# all definitions in this file are in alphabetical order


@dataclass
class CreatePipeline:
    allow_duplicate_names: bool
    catalog: str
    channel: str
    clusters: 'List[PipelineCluster]'
    configuration: 'Dict[str,str]'
    continuous: bool
    development: bool
    dry_run: bool
    edition: str
    filters: 'Filters'
    id: str
    libraries: 'List[PipelineLibrary]'
    name: str
    photon: bool
    storage: str
    target: str
    trigger: 'PipelineTrigger'

    def as_dict(self) -> dict:
        body = {}
        if self.allow_duplicate_names: body['allow_duplicate_names'] = self.allow_duplicate_names
        if self.catalog: body['catalog'] = self.catalog
        if self.channel: body['channel'] = self.channel
        if self.clusters: body['clusters'] = [v.as_dict() for v in self.clusters]
        if self.configuration: body['configuration'] = self.configuration
        if self.continuous: body['continuous'] = self.continuous
        if self.development: body['development'] = self.development
        if self.dry_run: body['dry_run'] = self.dry_run
        if self.edition: body['edition'] = self.edition
        if self.filters: body['filters'] = self.filters.as_dict()
        if self.id: body['id'] = self.id
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        if self.name: body['name'] = self.name
        if self.photon: body['photon'] = self.photon
        if self.storage: body['storage'] = self.storage
        if self.target: body['target'] = self.target
        if self.trigger: body['trigger'] = self.trigger.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePipeline':
        return cls(allow_duplicate_names=d.get('allow_duplicate_names', None),
                   catalog=d.get('catalog', None),
                   channel=d.get('channel', None),
                   clusters=[PipelineCluster.from_dict(v)
                             for v in d['clusters']] if 'clusters' in d else None,
                   configuration=d.get('configuration', None),
                   continuous=d.get('continuous', None),
                   development=d.get('development', None),
                   dry_run=d.get('dry_run', None),
                   edition=d.get('edition', None),
                   filters=Filters.from_dict(d['filters']) if 'filters' in d else None,
                   id=d.get('id', None),
                   libraries=[PipelineLibrary.from_dict(v)
                              for v in d['libraries']] if 'libraries' in d else None,
                   name=d.get('name', None),
                   photon=d.get('photon', None),
                   storage=d.get('storage', None),
                   target=d.get('target', None),
                   trigger=PipelineTrigger.from_dict(d['trigger']) if 'trigger' in d else None)


@dataclass
class CreatePipelineResponse:
    effective_settings: 'PipelineSpec'
    pipeline_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.effective_settings: body['effective_settings'] = self.effective_settings.as_dict()
        if self.pipeline_id: body['pipeline_id'] = self.pipeline_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePipelineResponse':
        return cls(effective_settings=PipelineSpec.from_dict(d['effective_settings'])
                   if 'effective_settings' in d else None,
                   pipeline_id=d.get('pipeline_id', None))


@dataclass
class CronTrigger:
    quartz_cron_schedule: str
    timezone_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.quartz_cron_schedule: body['quartz_cron_schedule'] = self.quartz_cron_schedule
        if self.timezone_id: body['timezone_id'] = self.timezone_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CronTrigger':
        return cls(quartz_cron_schedule=d.get('quartz_cron_schedule', None),
                   timezone_id=d.get('timezone_id', None))


@dataclass
class Delete:
    """Delete a pipeline"""

    pipeline_id: str


@dataclass
class EditPipeline:
    allow_duplicate_names: bool
    catalog: str
    channel: str
    clusters: 'List[PipelineCluster]'
    configuration: 'Dict[str,str]'
    continuous: bool
    development: bool
    edition: str
    expected_last_modified: int
    filters: 'Filters'
    id: str
    libraries: 'List[PipelineLibrary]'
    name: str
    photon: bool
    pipeline_id: str
    storage: str
    target: str
    trigger: 'PipelineTrigger'

    def as_dict(self) -> dict:
        body = {}
        if self.allow_duplicate_names: body['allow_duplicate_names'] = self.allow_duplicate_names
        if self.catalog: body['catalog'] = self.catalog
        if self.channel: body['channel'] = self.channel
        if self.clusters: body['clusters'] = [v.as_dict() for v in self.clusters]
        if self.configuration: body['configuration'] = self.configuration
        if self.continuous: body['continuous'] = self.continuous
        if self.development: body['development'] = self.development
        if self.edition: body['edition'] = self.edition
        if self.expected_last_modified: body['expected_last_modified'] = self.expected_last_modified
        if self.filters: body['filters'] = self.filters.as_dict()
        if self.id: body['id'] = self.id
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        if self.name: body['name'] = self.name
        if self.photon: body['photon'] = self.photon
        if self.pipeline_id: body['pipeline_id'] = self.pipeline_id
        if self.storage: body['storage'] = self.storage
        if self.target: body['target'] = self.target
        if self.trigger: body['trigger'] = self.trigger.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditPipeline':
        return cls(allow_duplicate_names=d.get('allow_duplicate_names', None),
                   catalog=d.get('catalog', None),
                   channel=d.get('channel', None),
                   clusters=[PipelineCluster.from_dict(v)
                             for v in d['clusters']] if 'clusters' in d else None,
                   configuration=d.get('configuration', None),
                   continuous=d.get('continuous', None),
                   development=d.get('development', None),
                   edition=d.get('edition', None),
                   expected_last_modified=d.get('expected_last_modified', None),
                   filters=Filters.from_dict(d['filters']) if 'filters' in d else None,
                   id=d.get('id', None),
                   libraries=[PipelineLibrary.from_dict(v)
                              for v in d['libraries']] if 'libraries' in d else None,
                   name=d.get('name', None),
                   photon=d.get('photon', None),
                   pipeline_id=d.get('pipeline_id', None),
                   storage=d.get('storage', None),
                   target=d.get('target', None),
                   trigger=PipelineTrigger.from_dict(d['trigger']) if 'trigger' in d else None)


@dataclass
class Filters:
    exclude: 'List[str]'
    include: 'List[str]'

    def as_dict(self) -> dict:
        body = {}
        if self.exclude: body['exclude'] = [v for v in self.exclude]
        if self.include: body['include'] = [v for v in self.include]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Filters':
        return cls(exclude=d.get('exclude', None), include=d.get('include', None))


@dataclass
class Get:
    """Get a pipeline"""

    pipeline_id: str


@dataclass
class GetPipelineResponse:
    cause: str
    cluster_id: str
    creator_user_name: str
    health: 'GetPipelineResponseHealth'
    last_modified: int
    latest_updates: 'List[UpdateStateInfo]'
    name: str
    pipeline_id: str
    run_as_user_name: str
    spec: 'PipelineSpec'
    state: 'PipelineState'

    def as_dict(self) -> dict:
        body = {}
        if self.cause: body['cause'] = self.cause
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.creator_user_name: body['creator_user_name'] = self.creator_user_name
        if self.health: body['health'] = self.health.value
        if self.last_modified: body['last_modified'] = self.last_modified
        if self.latest_updates: body['latest_updates'] = [v.as_dict() for v in self.latest_updates]
        if self.name: body['name'] = self.name
        if self.pipeline_id: body['pipeline_id'] = self.pipeline_id
        if self.run_as_user_name: body['run_as_user_name'] = self.run_as_user_name
        if self.spec: body['spec'] = self.spec.as_dict()
        if self.state: body['state'] = self.state.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPipelineResponse':
        return cls(cause=d.get('cause', None),
                   cluster_id=d.get('cluster_id', None),
                   creator_user_name=d.get('creator_user_name', None),
                   health=GetPipelineResponseHealth(d['health']) if 'health' in d else None,
                   last_modified=d.get('last_modified', None),
                   latest_updates=[UpdateStateInfo.from_dict(v)
                                   for v in d['latest_updates']] if 'latest_updates' in d else None,
                   name=d.get('name', None),
                   pipeline_id=d.get('pipeline_id', None),
                   run_as_user_name=d.get('run_as_user_name', None),
                   spec=PipelineSpec.from_dict(d['spec']) if 'spec' in d else None,
                   state=PipelineState(d['state']) if 'state' in d else None)


class GetPipelineResponseHealth(Enum):
    """The health of a pipeline."""

    HEALTHY = 'HEALTHY'
    UNHEALTHY = 'UNHEALTHY'


@dataclass
class GetUpdate:
    """Get a pipeline update"""

    pipeline_id: str
    update_id: str


@dataclass
class GetUpdateResponse:
    update: 'UpdateInfo'

    def as_dict(self) -> dict:
        body = {}
        if self.update: body['update'] = self.update.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetUpdateResponse':
        return cls(update=UpdateInfo.from_dict(d['update']) if 'update' in d else None)


@dataclass
class ListPipelines:
    """List pipelines"""

    filter: str
    max_results: int
    order_by: 'List[str]'
    page_token: str


@dataclass
class ListPipelinesResponse:
    next_page_token: str
    statuses: 'List[PipelineStateInfo]'

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.statuses: body['statuses'] = [v.as_dict() for v in self.statuses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListPipelinesResponse':
        return cls(next_page_token=d.get('next_page_token', None),
                   statuses=[PipelineStateInfo.from_dict(v)
                             for v in d['statuses']] if 'statuses' in d else None)


@dataclass
class ListUpdates:
    """List pipeline updates"""

    max_results: int
    page_token: str
    pipeline_id: str
    until_update_id: str


@dataclass
class ListUpdatesResponse:
    next_page_token: str
    prev_page_token: str
    updates: 'List[UpdateInfo]'

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.prev_page_token: body['prev_page_token'] = self.prev_page_token
        if self.updates: body['updates'] = [v.as_dict() for v in self.updates]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListUpdatesResponse':
        return cls(next_page_token=d.get('next_page_token', None),
                   prev_page_token=d.get('prev_page_token', None),
                   updates=[UpdateInfo.from_dict(v) for v in d['updates']] if 'updates' in d else None)


@dataclass
class NotebookLibrary:
    path: str

    def as_dict(self) -> dict:
        body = {}
        if self.path: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NotebookLibrary':
        return cls(path=d.get('path', None))


@dataclass
class PipelineCluster:
    apply_policy_default_values: bool
    autoscale: 'AutoScale'
    aws_attributes: 'AwsAttributes'
    azure_attributes: 'AzureAttributes'
    cluster_log_conf: 'ClusterLogConf'
    custom_tags: 'Dict[str,str]'
    driver_instance_pool_id: str
    driver_node_type_id: str
    gcp_attributes: 'GcpAttributes'
    instance_pool_id: str
    label: str
    node_type_id: str
    num_workers: int
    policy_id: str
    spark_conf: 'Dict[str,str]'
    spark_env_vars: 'Dict[str,str]'
    ssh_public_keys: 'List[str]'

    def as_dict(self) -> dict:
        body = {}
        if self.apply_policy_default_values:
            body['apply_policy_default_values'] = self.apply_policy_default_values
        if self.autoscale: body['autoscale'] = self.autoscale
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes
        if self.cluster_log_conf: body['cluster_log_conf'] = self.cluster_log_conf
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.driver_instance_pool_id: body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id: body['driver_node_type_id'] = self.driver_node_type_id
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes
        if self.instance_pool_id: body['instance_pool_id'] = self.instance_pool_id
        if self.label: body['label'] = self.label
        if self.node_type_id: body['node_type_id'] = self.node_type_id
        if self.num_workers: body['num_workers'] = self.num_workers
        if self.policy_id: body['policy_id'] = self.policy_id
        if self.spark_conf: body['spark_conf'] = self.spark_conf
        if self.spark_env_vars: body['spark_env_vars'] = self.spark_env_vars
        if self.ssh_public_keys: body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineCluster':
        return cls(
            apply_policy_default_values=d.get('apply_policy_default_values', None),
            autoscale=AutoScale.from_dict(d['autoscale']) if 'autoscale' in d else None,
            aws_attributes=AwsAttributes.from_dict(d['aws_attributes']) if 'aws_attributes' in d else None,
            azure_attributes=AzureAttributes.from_dict(d['azure_attributes'])
            if 'azure_attributes' in d else None,
            cluster_log_conf=ClusterLogConf.from_dict(d['cluster_log_conf'])
            if 'cluster_log_conf' in d else None,
            custom_tags=d.get('custom_tags', None),
            driver_instance_pool_id=d.get('driver_instance_pool_id', None),
            driver_node_type_id=d.get('driver_node_type_id', None),
            gcp_attributes=GcpAttributes.from_dict(d['gcp_attributes']) if 'gcp_attributes' in d else None,
            instance_pool_id=d.get('instance_pool_id', None),
            label=d.get('label', None),
            node_type_id=d.get('node_type_id', None),
            num_workers=d.get('num_workers', None),
            policy_id=d.get('policy_id', None),
            spark_conf=d.get('spark_conf', None),
            spark_env_vars=d.get('spark_env_vars', None),
            ssh_public_keys=d.get('ssh_public_keys', None))


@dataclass
class PipelineLibrary:
    jar: str
    maven: 'MavenLibrary'
    notebook: 'NotebookLibrary'
    whl: str

    def as_dict(self) -> dict:
        body = {}
        if self.jar: body['jar'] = self.jar
        if self.maven: body['maven'] = self.maven
        if self.notebook: body['notebook'] = self.notebook.as_dict()
        if self.whl: body['whl'] = self.whl
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineLibrary':
        return cls(jar=d.get('jar', None),
                   maven=MavenLibrary.from_dict(d['maven']) if 'maven' in d else None,
                   notebook=NotebookLibrary.from_dict(d['notebook']) if 'notebook' in d else None,
                   whl=d.get('whl', None))


@dataclass
class PipelineSpec:
    catalog: str
    channel: str
    clusters: 'List[PipelineCluster]'
    configuration: 'Dict[str,str]'
    continuous: bool
    development: bool
    edition: str
    filters: 'Filters'
    id: str
    libraries: 'List[PipelineLibrary]'
    name: str
    photon: bool
    storage: str
    target: str
    trigger: 'PipelineTrigger'

    def as_dict(self) -> dict:
        body = {}
        if self.catalog: body['catalog'] = self.catalog
        if self.channel: body['channel'] = self.channel
        if self.clusters: body['clusters'] = [v.as_dict() for v in self.clusters]
        if self.configuration: body['configuration'] = self.configuration
        if self.continuous: body['continuous'] = self.continuous
        if self.development: body['development'] = self.development
        if self.edition: body['edition'] = self.edition
        if self.filters: body['filters'] = self.filters.as_dict()
        if self.id: body['id'] = self.id
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        if self.name: body['name'] = self.name
        if self.photon: body['photon'] = self.photon
        if self.storage: body['storage'] = self.storage
        if self.target: body['target'] = self.target
        if self.trigger: body['trigger'] = self.trigger.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineSpec':
        return cls(catalog=d.get('catalog', None),
                   channel=d.get('channel', None),
                   clusters=[PipelineCluster.from_dict(v)
                             for v in d['clusters']] if 'clusters' in d else None,
                   configuration=d.get('configuration', None),
                   continuous=d.get('continuous', None),
                   development=d.get('development', None),
                   edition=d.get('edition', None),
                   filters=Filters.from_dict(d['filters']) if 'filters' in d else None,
                   id=d.get('id', None),
                   libraries=[PipelineLibrary.from_dict(v)
                              for v in d['libraries']] if 'libraries' in d else None,
                   name=d.get('name', None),
                   photon=d.get('photon', None),
                   storage=d.get('storage', None),
                   target=d.get('target', None),
                   trigger=PipelineTrigger.from_dict(d['trigger']) if 'trigger' in d else None)


class PipelineState(Enum):
    """The pipeline state."""

    DELETED = 'DELETED'
    DEPLOYING = 'DEPLOYING'
    FAILED = 'FAILED'
    IDLE = 'IDLE'
    RECOVERING = 'RECOVERING'
    RESETTING = 'RESETTING'
    RUNNING = 'RUNNING'
    STARTING = 'STARTING'
    STOPPING = 'STOPPING'


@dataclass
class PipelineStateInfo:
    cluster_id: str
    creator_user_name: str
    latest_updates: 'List[UpdateStateInfo]'
    name: str
    pipeline_id: str
    run_as_user_name: str
    state: 'PipelineState'

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.creator_user_name: body['creator_user_name'] = self.creator_user_name
        if self.latest_updates: body['latest_updates'] = [v.as_dict() for v in self.latest_updates]
        if self.name: body['name'] = self.name
        if self.pipeline_id: body['pipeline_id'] = self.pipeline_id
        if self.run_as_user_name: body['run_as_user_name'] = self.run_as_user_name
        if self.state: body['state'] = self.state.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineStateInfo':
        return cls(cluster_id=d.get('cluster_id', None),
                   creator_user_name=d.get('creator_user_name', None),
                   latest_updates=[UpdateStateInfo.from_dict(v)
                                   for v in d['latest_updates']] if 'latest_updates' in d else None,
                   name=d.get('name', None),
                   pipeline_id=d.get('pipeline_id', None),
                   run_as_user_name=d.get('run_as_user_name', None),
                   state=PipelineState(d['state']) if 'state' in d else None)


@dataclass
class PipelineTrigger:
    cron: 'CronTrigger'
    manual: Any

    def as_dict(self) -> dict:
        body = {}
        if self.cron: body['cron'] = self.cron.as_dict()
        if self.manual: body['manual'] = self.manual
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineTrigger':
        return cls(cron=CronTrigger.from_dict(d['cron']) if 'cron' in d else None,
                   manual=d.get('manual', None))


@dataclass
class Reset:
    """Reset a pipeline"""

    pipeline_id: str


@dataclass
class StartUpdate:
    cause: 'StartUpdateCause'
    full_refresh: bool
    full_refresh_selection: 'List[str]'
    pipeline_id: str
    refresh_selection: 'List[str]'

    def as_dict(self) -> dict:
        body = {}
        if self.cause: body['cause'] = self.cause.value
        if self.full_refresh: body['full_refresh'] = self.full_refresh
        if self.full_refresh_selection:
            body['full_refresh_selection'] = [v for v in self.full_refresh_selection]
        if self.pipeline_id: body['pipeline_id'] = self.pipeline_id
        if self.refresh_selection: body['refresh_selection'] = [v for v in self.refresh_selection]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StartUpdate':
        return cls(cause=StartUpdateCause(d['cause']) if 'cause' in d else None,
                   full_refresh=d.get('full_refresh', None),
                   full_refresh_selection=d.get('full_refresh_selection', None),
                   pipeline_id=d.get('pipeline_id', None),
                   refresh_selection=d.get('refresh_selection', None))


class StartUpdateCause(Enum):

    API_CALL = 'API_CALL'
    JOB_TASK = 'JOB_TASK'
    RETRY_ON_FAILURE = 'RETRY_ON_FAILURE'
    SCHEMA_CHANGE = 'SCHEMA_CHANGE'
    SERVICE_UPGRADE = 'SERVICE_UPGRADE'
    USER_ACTION = 'USER_ACTION'


@dataclass
class StartUpdateResponse:
    update_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.update_id: body['update_id'] = self.update_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StartUpdateResponse':
        return cls(update_id=d.get('update_id', None))


@dataclass
class Stop:
    """Stop a pipeline"""

    pipeline_id: str


@dataclass
class UpdateInfo:
    cause: 'UpdateInfoCause'
    cluster_id: str
    config: 'PipelineSpec'
    creation_time: int
    full_refresh: bool
    full_refresh_selection: 'List[str]'
    pipeline_id: str
    refresh_selection: 'List[str]'
    state: 'UpdateInfoState'
    update_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cause: body['cause'] = self.cause.value
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.config: body['config'] = self.config.as_dict()
        if self.creation_time: body['creation_time'] = self.creation_time
        if self.full_refresh: body['full_refresh'] = self.full_refresh
        if self.full_refresh_selection:
            body['full_refresh_selection'] = [v for v in self.full_refresh_selection]
        if self.pipeline_id: body['pipeline_id'] = self.pipeline_id
        if self.refresh_selection: body['refresh_selection'] = [v for v in self.refresh_selection]
        if self.state: body['state'] = self.state.value
        if self.update_id: body['update_id'] = self.update_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateInfo':
        return cls(cause=UpdateInfoCause(d['cause']) if 'cause' in d else None,
                   cluster_id=d.get('cluster_id', None),
                   config=PipelineSpec.from_dict(d['config']) if 'config' in d else None,
                   creation_time=d.get('creation_time', None),
                   full_refresh=d.get('full_refresh', None),
                   full_refresh_selection=d.get('full_refresh_selection', None),
                   pipeline_id=d.get('pipeline_id', None),
                   refresh_selection=d.get('refresh_selection', None),
                   state=UpdateInfoState(d['state']) if 'state' in d else None,
                   update_id=d.get('update_id', None))


class UpdateInfoCause(Enum):
    """What triggered this update."""

    API_CALL = 'API_CALL'
    JOB_TASK = 'JOB_TASK'
    RETRY_ON_FAILURE = 'RETRY_ON_FAILURE'
    SCHEMA_CHANGE = 'SCHEMA_CHANGE'
    SERVICE_UPGRADE = 'SERVICE_UPGRADE'
    USER_ACTION = 'USER_ACTION'


class UpdateInfoState(Enum):
    """The update state."""

    CANCELED = 'CANCELED'
    COMPLETED = 'COMPLETED'
    CREATED = 'CREATED'
    FAILED = 'FAILED'
    INITIALIZING = 'INITIALIZING'
    QUEUED = 'QUEUED'
    RESETTING = 'RESETTING'
    RUNNING = 'RUNNING'
    SETTING_UP_TABLES = 'SETTING_UP_TABLES'
    STOPPING = 'STOPPING'
    WAITING_FOR_RESOURCES = 'WAITING_FOR_RESOURCES'


@dataclass
class UpdateStateInfo:
    creation_time: str
    state: 'UpdateStateInfoState'
    update_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.creation_time: body['creation_time'] = self.creation_time
        if self.state: body['state'] = self.state.value
        if self.update_id: body['update_id'] = self.update_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateStateInfo':
        return cls(creation_time=d.get('creation_time', None),
                   state=UpdateStateInfoState(d['state']) if 'state' in d else None,
                   update_id=d.get('update_id', None))


class UpdateStateInfoState(Enum):

    CANCELED = 'CANCELED'
    COMPLETED = 'COMPLETED'
    CREATED = 'CREATED'
    FAILED = 'FAILED'
    INITIALIZING = 'INITIALIZING'
    QUEUED = 'QUEUED'
    RESETTING = 'RESETTING'
    RUNNING = 'RUNNING'
    SETTING_UP_TABLES = 'SETTING_UP_TABLES'
    STOPPING = 'STOPPING'
    WAITING_FOR_RESOURCES = 'WAITING_FOR_RESOURCES'


class PipelinesAPI:
    """The Delta Live Tables API allows you to create, edit, delete, start, and view details about pipelines.
    
    Delta Live Tables is a framework for building reliable, maintainable, and testable data processing
    pipelines. You define the transformations to perform on your data, and Delta Live Tables manages task
    orchestration, cluster management, monitoring, data quality, and error handling.
    
    Instead of defining your data pipelines using a series of separate Apache Spark tasks, Delta Live Tables
    manages how your data is transformed based on a target schema you define for each processing step. You can
    also enforce data quality with Delta Live Tables expectations. Expectations allow you to define expected
    data quality and specify how to handle records that fail those expectations."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               allow_duplicate_names: bool = None,
               catalog: str = None,
               channel: str = None,
               clusters: List[PipelineCluster] = None,
               configuration: Dict[str, str] = None,
               continuous: bool = None,
               development: bool = None,
               dry_run: bool = None,
               edition: str = None,
               filters: Filters = None,
               id: str = None,
               libraries: List[PipelineLibrary] = None,
               name: str = None,
               photon: bool = None,
               storage: str = None,
               target: str = None,
               trigger: PipelineTrigger = None,
               **kwargs) -> CreatePipelineResponse:
        """Create a pipeline.
        
        Creates a new data processing pipeline based on the requested configuration. If successful, this
        method returns the ID of the new pipeline."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreatePipeline(allow_duplicate_names=allow_duplicate_names,
                                     catalog=catalog,
                                     channel=channel,
                                     clusters=clusters,
                                     configuration=configuration,
                                     continuous=continuous,
                                     development=development,
                                     dry_run=dry_run,
                                     edition=edition,
                                     filters=filters,
                                     id=id,
                                     libraries=libraries,
                                     name=name,
                                     photon=photon,
                                     storage=storage,
                                     target=target,
                                     trigger=trigger)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/pipelines', body=body)
        return CreatePipelineResponse.from_dict(json)

    def delete(self, pipeline_id: str, **kwargs):
        """Delete a pipeline.
        
        Deletes a pipeline."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Delete(pipeline_id=pipeline_id)

        self._api.do('DELETE', f'/api/2.0/pipelines/{request.pipeline_id}')

    def get(self, pipeline_id: str, **kwargs) -> GetPipelineResponse:
        """Get a pipeline."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Get(pipeline_id=pipeline_id)

        json = self._api.do('GET', f'/api/2.0/pipelines/{request.pipeline_id}')
        return GetPipelineResponse.from_dict(json)

    def get_update(self, pipeline_id: str, update_id: str, **kwargs) -> GetUpdateResponse:
        """Get a pipeline update.
        
        Gets an update from an active pipeline."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetUpdate(pipeline_id=pipeline_id, update_id=update_id)

        json = self._api.do('GET', f'/api/2.0/pipelines/{request.pipeline_id}/updates/{request.update_id}')
        return GetUpdateResponse.from_dict(json)

    def list_pipelines(self,
                       *,
                       filter: str = None,
                       max_results: int = None,
                       order_by: List[str] = None,
                       page_token: str = None,
                       **kwargs) -> Iterator[PipelineStateInfo]:
        """List pipelines.
        
        Lists pipelines defined in the Delta Live Tables system."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListPipelines(filter=filter,
                                    max_results=max_results,
                                    order_by=order_by,
                                    page_token=page_token)

        query = {}
        if filter: query['filter'] = request.filter
        if max_results: query['max_results'] = request.max_results
        if order_by: query['order_by'] = [v for v in request.order_by]
        if page_token: query['page_token'] = request.page_token

        while True:
            json = self._api.do('GET', '/api/2.0/pipelines', query=query)
            if not json['statuses']:
                return
            for v in json['statuses']:
                yield PipelineStateInfo.from_dict(v)
            query['page_token'] = json['next_page_token']
            if not json['next_page_token']:
                return

    def list_updates(self,
                     pipeline_id: str,
                     *,
                     max_results: int = None,
                     page_token: str = None,
                     until_update_id: str = None,
                     **kwargs) -> ListUpdatesResponse:
        """List pipeline updates.
        
        List updates for an active pipeline."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListUpdates(max_results=max_results,
                                  page_token=page_token,
                                  pipeline_id=pipeline_id,
                                  until_update_id=until_update_id)

        query = {}
        if max_results: query['max_results'] = request.max_results
        if page_token: query['page_token'] = request.page_token
        if until_update_id: query['until_update_id'] = request.until_update_id

        json = self._api.do('GET', f'/api/2.0/pipelines/{request.pipeline_id}/updates', query=query)
        return ListUpdatesResponse.from_dict(json)

    def reset(self, pipeline_id: str, **kwargs):
        """Reset a pipeline.
        
        Resets a pipeline."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Reset(pipeline_id=pipeline_id)

        self._api.do('POST', f'/api/2.0/pipelines/{request.pipeline_id}/reset')

    def start_update(self,
                     pipeline_id: str,
                     *,
                     cause: StartUpdateCause = None,
                     full_refresh: bool = None,
                     full_refresh_selection: List[str] = None,
                     refresh_selection: List[str] = None,
                     **kwargs) -> StartUpdateResponse:
        """Queue a pipeline update.
        
        Starts or queues a pipeline update."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = StartUpdate(cause=cause,
                                  full_refresh=full_refresh,
                                  full_refresh_selection=full_refresh_selection,
                                  pipeline_id=pipeline_id,
                                  refresh_selection=refresh_selection)
        body = request.as_dict()

        json = self._api.do('POST', f'/api/2.0/pipelines/{request.pipeline_id}/updates', body=body)
        return StartUpdateResponse.from_dict(json)

    def stop(self, pipeline_id: str, **kwargs):
        """Stop a pipeline.
        
        Stops a pipeline."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Stop(pipeline_id=pipeline_id)

        self._api.do('POST', f'/api/2.0/pipelines/{request.pipeline_id}/stop')

    def update(self,
               pipeline_id: str,
               *,
               allow_duplicate_names: bool = None,
               catalog: str = None,
               channel: str = None,
               clusters: List[PipelineCluster] = None,
               configuration: Dict[str, str] = None,
               continuous: bool = None,
               development: bool = None,
               edition: str = None,
               expected_last_modified: int = None,
               filters: Filters = None,
               id: str = None,
               libraries: List[PipelineLibrary] = None,
               name: str = None,
               photon: bool = None,
               storage: str = None,
               target: str = None,
               trigger: PipelineTrigger = None,
               **kwargs):
        """Edit a pipeline.
        
        Updates a pipeline with the supplied configuration."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = EditPipeline(allow_duplicate_names=allow_duplicate_names,
                                   catalog=catalog,
                                   channel=channel,
                                   clusters=clusters,
                                   configuration=configuration,
                                   continuous=continuous,
                                   development=development,
                                   edition=edition,
                                   expected_last_modified=expected_last_modified,
                                   filters=filters,
                                   id=id,
                                   libraries=libraries,
                                   name=name,
                                   photon=photon,
                                   pipeline_id=pipeline_id,
                                   storage=storage,
                                   target=target,
                                   trigger=trigger)
        body = request.as_dict()
        self._api.do('PUT', f'/api/2.0/pipelines/{request.pipeline_id}', body=body)

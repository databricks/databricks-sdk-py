# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
import random
import time
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Any, Dict, Iterator, List

from ..errors import OperationFailed
from ._internal import Wait, _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

from .clusters import (AutoScale, AwsAttributes, AzureAttributes,
                       ClusterLogConf, GcpAttributes)
from .libraries import MavenLibrary

# all definitions in this file are in alphabetical order


@dataclass
class CreatePipeline:
    allow_duplicate_names: bool = None
    catalog: str = None
    channel: str = None
    clusters: 'List[PipelineCluster]' = None
    configuration: 'Dict[str,str]' = None
    continuous: bool = None
    development: bool = None
    dry_run: bool = None
    edition: str = None
    filters: 'Filters' = None
    id: str = None
    libraries: 'List[PipelineLibrary]' = None
    name: str = None
    photon: bool = None
    storage: str = None
    target: str = None
    trigger: 'PipelineTrigger' = None

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
                   clusters=_repeated(d, 'clusters', PipelineCluster),
                   configuration=d.get('configuration', None),
                   continuous=d.get('continuous', None),
                   development=d.get('development', None),
                   dry_run=d.get('dry_run', None),
                   edition=d.get('edition', None),
                   filters=_from_dict(d, 'filters', Filters),
                   id=d.get('id', None),
                   libraries=_repeated(d, 'libraries', PipelineLibrary),
                   name=d.get('name', None),
                   photon=d.get('photon', None),
                   storage=d.get('storage', None),
                   target=d.get('target', None),
                   trigger=_from_dict(d, 'trigger', PipelineTrigger))


@dataclass
class CreatePipelineResponse:
    effective_settings: 'PipelineSpec' = None
    pipeline_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.effective_settings: body['effective_settings'] = self.effective_settings.as_dict()
        if self.pipeline_id: body['pipeline_id'] = self.pipeline_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePipelineResponse':
        return cls(effective_settings=_from_dict(d, 'effective_settings', PipelineSpec),
                   pipeline_id=d.get('pipeline_id', None))


@dataclass
class CronTrigger:
    quartz_cron_schedule: str = None
    timezone_id: str = None

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
class DataPlaneId:
    instance: str = None
    seq_no: Any = None

    def as_dict(self) -> dict:
        body = {}
        if self.instance: body['instance'] = self.instance
        if self.seq_no: body['seq_no'] = self.seq_no
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DataPlaneId':
        return cls(instance=d.get('instance', None), seq_no=d.get('seq_no', None))


@dataclass
class Delete:
    """Delete a pipeline"""

    pipeline_id: str


@dataclass
class EditPipeline:
    pipeline_id: str
    allow_duplicate_names: bool = None
    catalog: str = None
    channel: str = None
    clusters: 'List[PipelineCluster]' = None
    configuration: 'Dict[str,str]' = None
    continuous: bool = None
    development: bool = None
    edition: str = None
    expected_last_modified: int = None
    filters: 'Filters' = None
    id: str = None
    libraries: 'List[PipelineLibrary]' = None
    name: str = None
    photon: bool = None
    storage: str = None
    target: str = None
    trigger: 'PipelineTrigger' = None

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
                   clusters=_repeated(d, 'clusters', PipelineCluster),
                   configuration=d.get('configuration', None),
                   continuous=d.get('continuous', None),
                   development=d.get('development', None),
                   edition=d.get('edition', None),
                   expected_last_modified=d.get('expected_last_modified', None),
                   filters=_from_dict(d, 'filters', Filters),
                   id=d.get('id', None),
                   libraries=_repeated(d, 'libraries', PipelineLibrary),
                   name=d.get('name', None),
                   photon=d.get('photon', None),
                   pipeline_id=d.get('pipeline_id', None),
                   storage=d.get('storage', None),
                   target=d.get('target', None),
                   trigger=_from_dict(d, 'trigger', PipelineTrigger))


@dataclass
class ErrorDetail:
    exceptions: 'List[SerializedException]' = None
    fatal: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.exceptions: body['exceptions'] = [v.as_dict() for v in self.exceptions]
        if self.fatal: body['fatal'] = self.fatal
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ErrorDetail':
        return cls(exceptions=_repeated(d, 'exceptions', SerializedException), fatal=d.get('fatal', None))


class EventLevel(Enum):
    """The severity level of the event."""

    ERROR = 'ERROR'
    INFO = 'INFO'
    METRICS = 'METRICS'
    WARN = 'WARN'


@dataclass
class Filters:
    exclude: 'List[str]' = None
    include: 'List[str]' = None

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
    cause: str = None
    cluster_id: str = None
    creator_user_name: str = None
    health: 'GetPipelineResponseHealth' = None
    last_modified: int = None
    latest_updates: 'List[UpdateStateInfo]' = None
    name: str = None
    pipeline_id: str = None
    run_as_user_name: str = None
    spec: 'PipelineSpec' = None
    state: 'PipelineState' = None

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
                   health=_enum(d, 'health', GetPipelineResponseHealth),
                   last_modified=d.get('last_modified', None),
                   latest_updates=_repeated(d, 'latest_updates', UpdateStateInfo),
                   name=d.get('name', None),
                   pipeline_id=d.get('pipeline_id', None),
                   run_as_user_name=d.get('run_as_user_name', None),
                   spec=_from_dict(d, 'spec', PipelineSpec),
                   state=_enum(d, 'state', PipelineState))


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
    update: 'UpdateInfo' = None

    def as_dict(self) -> dict:
        body = {}
        if self.update: body['update'] = self.update.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetUpdateResponse':
        return cls(update=_from_dict(d, 'update', UpdateInfo))


@dataclass
class ListPipelineEvents:
    """List pipeline events"""

    pipeline_id: str
    filter: str = None
    max_results: int = None
    order_by: 'List[str]' = None
    page_token: str = None


@dataclass
class ListPipelineEventsResponse:
    events: 'List[PipelineEvent]' = None
    next_page_token: str = None
    prev_page_token: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.events: body['events'] = [v.as_dict() for v in self.events]
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.prev_page_token: body['prev_page_token'] = self.prev_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListPipelineEventsResponse':
        return cls(events=_repeated(d, 'events', PipelineEvent),
                   next_page_token=d.get('next_page_token', None),
                   prev_page_token=d.get('prev_page_token', None))


@dataclass
class ListPipelines:
    """List pipelines"""

    filter: str = None
    max_results: int = None
    order_by: 'List[str]' = None
    page_token: str = None


@dataclass
class ListPipelinesResponse:
    next_page_token: str = None
    statuses: 'List[PipelineStateInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.statuses: body['statuses'] = [v.as_dict() for v in self.statuses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListPipelinesResponse':
        return cls(next_page_token=d.get('next_page_token', None),
                   statuses=_repeated(d, 'statuses', PipelineStateInfo))


@dataclass
class ListUpdates:
    """List pipeline updates"""

    pipeline_id: str
    max_results: int = None
    page_token: str = None
    until_update_id: str = None


@dataclass
class ListUpdatesResponse:
    next_page_token: str = None
    prev_page_token: str = None
    updates: 'List[UpdateInfo]' = None

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
                   updates=_repeated(d, 'updates', UpdateInfo))


class MaturityLevel(Enum):
    """Maturity level for EventDetails."""

    DEPRECATED = 'DEPRECATED'
    EVOLVING = 'EVOLVING'
    STABLE = 'STABLE'


@dataclass
class NotebookLibrary:
    path: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.path: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NotebookLibrary':
        return cls(path=d.get('path', None))


@dataclass
class Origin:
    batch_id: int = None
    cloud: str = None
    cluster_id: str = None
    dataset_name: str = None
    flow_id: str = None
    flow_name: str = None
    host: str = None
    maintenance_id: str = None
    materialization_name: str = None
    org_id: int = None
    pipeline_id: str = None
    pipeline_name: str = None
    region: str = None
    request_id: str = None
    table_id: str = None
    uc_resource_id: str = None
    update_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.batch_id: body['batch_id'] = self.batch_id
        if self.cloud: body['cloud'] = self.cloud
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.dataset_name: body['dataset_name'] = self.dataset_name
        if self.flow_id: body['flow_id'] = self.flow_id
        if self.flow_name: body['flow_name'] = self.flow_name
        if self.host: body['host'] = self.host
        if self.maintenance_id: body['maintenance_id'] = self.maintenance_id
        if self.materialization_name: body['materialization_name'] = self.materialization_name
        if self.org_id: body['org_id'] = self.org_id
        if self.pipeline_id: body['pipeline_id'] = self.pipeline_id
        if self.pipeline_name: body['pipeline_name'] = self.pipeline_name
        if self.region: body['region'] = self.region
        if self.request_id: body['request_id'] = self.request_id
        if self.table_id: body['table_id'] = self.table_id
        if self.uc_resource_id: body['uc_resource_id'] = self.uc_resource_id
        if self.update_id: body['update_id'] = self.update_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Origin':
        return cls(batch_id=d.get('batch_id', None),
                   cloud=d.get('cloud', None),
                   cluster_id=d.get('cluster_id', None),
                   dataset_name=d.get('dataset_name', None),
                   flow_id=d.get('flow_id', None),
                   flow_name=d.get('flow_name', None),
                   host=d.get('host', None),
                   maintenance_id=d.get('maintenance_id', None),
                   materialization_name=d.get('materialization_name', None),
                   org_id=d.get('org_id', None),
                   pipeline_id=d.get('pipeline_id', None),
                   pipeline_name=d.get('pipeline_name', None),
                   region=d.get('region', None),
                   request_id=d.get('request_id', None),
                   table_id=d.get('table_id', None),
                   uc_resource_id=d.get('uc_resource_id', None),
                   update_id=d.get('update_id', None))


@dataclass
class PipelineCluster:
    apply_policy_default_values: bool = None
    autoscale: 'AutoScale' = None
    aws_attributes: 'AwsAttributes' = None
    azure_attributes: 'AzureAttributes' = None
    cluster_log_conf: 'ClusterLogConf' = None
    custom_tags: 'Dict[str,str]' = None
    driver_instance_pool_id: str = None
    driver_node_type_id: str = None
    gcp_attributes: 'GcpAttributes' = None
    instance_pool_id: str = None
    label: str = None
    node_type_id: str = None
    num_workers: int = None
    policy_id: str = None
    spark_conf: 'Dict[str,str]' = None
    spark_env_vars: 'Dict[str,str]' = None
    ssh_public_keys: 'List[str]' = None

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
        return cls(apply_policy_default_values=d.get('apply_policy_default_values', None),
                   autoscale=_from_dict(d, 'autoscale', AutoScale),
                   aws_attributes=_from_dict(d, 'aws_attributes', AwsAttributes),
                   azure_attributes=_from_dict(d, 'azure_attributes', AzureAttributes),
                   cluster_log_conf=_from_dict(d, 'cluster_log_conf', ClusterLogConf),
                   custom_tags=d.get('custom_tags', None),
                   driver_instance_pool_id=d.get('driver_instance_pool_id', None),
                   driver_node_type_id=d.get('driver_node_type_id', None),
                   gcp_attributes=_from_dict(d, 'gcp_attributes', GcpAttributes),
                   instance_pool_id=d.get('instance_pool_id', None),
                   label=d.get('label', None),
                   node_type_id=d.get('node_type_id', None),
                   num_workers=d.get('num_workers', None),
                   policy_id=d.get('policy_id', None),
                   spark_conf=d.get('spark_conf', None),
                   spark_env_vars=d.get('spark_env_vars', None),
                   ssh_public_keys=d.get('ssh_public_keys', None))


@dataclass
class PipelineEvent:
    error: 'ErrorDetail' = None
    event_type: str = None
    id: str = None
    level: 'EventLevel' = None
    maturity_level: 'MaturityLevel' = None
    message: str = None
    origin: 'Origin' = None
    sequence: 'Sequencing' = None
    timestamp: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.error: body['error'] = self.error.as_dict()
        if self.event_type: body['event_type'] = self.event_type
        if self.id: body['id'] = self.id
        if self.level: body['level'] = self.level.value
        if self.maturity_level: body['maturity_level'] = self.maturity_level.value
        if self.message: body['message'] = self.message
        if self.origin: body['origin'] = self.origin.as_dict()
        if self.sequence: body['sequence'] = self.sequence.as_dict()
        if self.timestamp: body['timestamp'] = self.timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineEvent':
        return cls(error=_from_dict(d, 'error', ErrorDetail),
                   event_type=d.get('event_type', None),
                   id=d.get('id', None),
                   level=_enum(d, 'level', EventLevel),
                   maturity_level=_enum(d, 'maturity_level', MaturityLevel),
                   message=d.get('message', None),
                   origin=_from_dict(d, 'origin', Origin),
                   sequence=_from_dict(d, 'sequence', Sequencing),
                   timestamp=d.get('timestamp', None))


@dataclass
class PipelineLibrary:
    jar: str = None
    maven: 'MavenLibrary' = None
    notebook: 'NotebookLibrary' = None
    whl: str = None

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
                   maven=_from_dict(d, 'maven', MavenLibrary),
                   notebook=_from_dict(d, 'notebook', NotebookLibrary),
                   whl=d.get('whl', None))


@dataclass
class PipelineSpec:
    catalog: str = None
    channel: str = None
    clusters: 'List[PipelineCluster]' = None
    configuration: 'Dict[str,str]' = None
    continuous: bool = None
    development: bool = None
    edition: str = None
    filters: 'Filters' = None
    id: str = None
    libraries: 'List[PipelineLibrary]' = None
    name: str = None
    photon: bool = None
    storage: str = None
    target: str = None
    trigger: 'PipelineTrigger' = None

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
                   clusters=_repeated(d, 'clusters', PipelineCluster),
                   configuration=d.get('configuration', None),
                   continuous=d.get('continuous', None),
                   development=d.get('development', None),
                   edition=d.get('edition', None),
                   filters=_from_dict(d, 'filters', Filters),
                   id=d.get('id', None),
                   libraries=_repeated(d, 'libraries', PipelineLibrary),
                   name=d.get('name', None),
                   photon=d.get('photon', None),
                   storage=d.get('storage', None),
                   target=d.get('target', None),
                   trigger=_from_dict(d, 'trigger', PipelineTrigger))


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
    cluster_id: str = None
    creator_user_name: str = None
    latest_updates: 'List[UpdateStateInfo]' = None
    name: str = None
    pipeline_id: str = None
    run_as_user_name: str = None
    state: 'PipelineState' = None

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
                   latest_updates=_repeated(d, 'latest_updates', UpdateStateInfo),
                   name=d.get('name', None),
                   pipeline_id=d.get('pipeline_id', None),
                   run_as_user_name=d.get('run_as_user_name', None),
                   state=_enum(d, 'state', PipelineState))


@dataclass
class PipelineTrigger:
    cron: 'CronTrigger' = None
    manual: Any = None

    def as_dict(self) -> dict:
        body = {}
        if self.cron: body['cron'] = self.cron.as_dict()
        if self.manual: body['manual'] = self.manual
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineTrigger':
        return cls(cron=_from_dict(d, 'cron', CronTrigger), manual=d.get('manual', None))


@dataclass
class Reset:
    """Reset a pipeline"""

    pipeline_id: str


@dataclass
class Sequencing:
    control_plane_seq_no: int = None
    data_plane_id: 'DataPlaneId' = None

    def as_dict(self) -> dict:
        body = {}
        if self.control_plane_seq_no: body['control_plane_seq_no'] = self.control_plane_seq_no
        if self.data_plane_id: body['data_plane_id'] = self.data_plane_id.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Sequencing':
        return cls(control_plane_seq_no=d.get('control_plane_seq_no', None),
                   data_plane_id=_from_dict(d, 'data_plane_id', DataPlaneId))


@dataclass
class SerializedException:
    class_name: str = None
    message: str = None
    stack: 'List[StackFrame]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.class_name: body['class_name'] = self.class_name
        if self.message: body['message'] = self.message
        if self.stack: body['stack'] = [v.as_dict() for v in self.stack]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SerializedException':
        return cls(class_name=d.get('class_name', None),
                   message=d.get('message', None),
                   stack=_repeated(d, 'stack', StackFrame))


@dataclass
class StackFrame:
    declaring_class: str = None
    file_name: str = None
    line_number: int = None
    method_name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.declaring_class: body['declaring_class'] = self.declaring_class
        if self.file_name: body['file_name'] = self.file_name
        if self.line_number: body['line_number'] = self.line_number
        if self.method_name: body['method_name'] = self.method_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StackFrame':
        return cls(declaring_class=d.get('declaring_class', None),
                   file_name=d.get('file_name', None),
                   line_number=d.get('line_number', None),
                   method_name=d.get('method_name', None))


@dataclass
class StartUpdate:
    pipeline_id: str
    cause: 'StartUpdateCause' = None
    full_refresh: bool = None
    full_refresh_selection: 'List[str]' = None
    refresh_selection: 'List[str]' = None

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
        return cls(cause=_enum(d, 'cause', StartUpdateCause),
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
    update_id: str = None

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
    cause: 'UpdateInfoCause' = None
    cluster_id: str = None
    config: 'PipelineSpec' = None
    creation_time: int = None
    full_refresh: bool = None
    full_refresh_selection: 'List[str]' = None
    pipeline_id: str = None
    refresh_selection: 'List[str]' = None
    state: 'UpdateInfoState' = None
    update_id: str = None

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
        return cls(cause=_enum(d, 'cause', UpdateInfoCause),
                   cluster_id=d.get('cluster_id', None),
                   config=_from_dict(d, 'config', PipelineSpec),
                   creation_time=d.get('creation_time', None),
                   full_refresh=d.get('full_refresh', None),
                   full_refresh_selection=d.get('full_refresh_selection', None),
                   pipeline_id=d.get('pipeline_id', None),
                   refresh_selection=d.get('refresh_selection', None),
                   state=_enum(d, 'state', UpdateInfoState),
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
    creation_time: str = None
    state: 'UpdateStateInfoState' = None
    update_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.creation_time: body['creation_time'] = self.creation_time
        if self.state: body['state'] = self.state.value
        if self.update_id: body['update_id'] = self.update_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateStateInfo':
        return cls(creation_time=d.get('creation_time', None),
                   state=_enum(d, 'state', UpdateStateInfoState),
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

    def wait_get_pipeline_idle(self, pipeline_id: str, timeout=timedelta(minutes=20)) -> GetPipelineResponse:
        deadline = time.time() + timeout.total_seconds()
        target_states = (PipelineState.IDLE, )
        failure_states = (PipelineState.FAILED, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get(pipeline_id=pipeline_id)
            status = poll.state
            status_message = poll.cause
            if status in target_states:
                return poll
            if status in failure_states:
                msg = f'failed to reach IDLE, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"pipeline_id={pipeline_id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def wait_get_pipeline_running(self, pipeline_id: str,
                                  timeout=timedelta(minutes=20)) -> GetPipelineResponse:
        deadline = time.time() + timeout.total_seconds()
        target_states = (PipelineState.RUNNING, )
        failure_states = (PipelineState.FAILED, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get(pipeline_id=pipeline_id)
            status = poll.state
            status_message = poll.cause
            if status in target_states:
                return poll
            if status in failure_states:
                msg = f'failed to reach RUNNING, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"pipeline_id={pipeline_id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

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

    def list_pipeline_events(self,
                             pipeline_id: str,
                             *,
                             filter: str = None,
                             max_results: int = None,
                             order_by: List[str] = None,
                             page_token: str = None,
                             **kwargs) -> Iterator[PipelineEvent]:
        """List pipeline events.
        
        Retrieves events for a pipeline."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListPipelineEvents(filter=filter,
                                         max_results=max_results,
                                         order_by=order_by,
                                         page_token=page_token,
                                         pipeline_id=pipeline_id)

        query = {}
        if filter: query['filter'] = request.filter
        if max_results: query['max_results'] = request.max_results
        if order_by: query['order_by'] = [v for v in request.order_by]
        if page_token: query['page_token'] = request.page_token

        while True:
            json = self._api.do('GET', f'/api/2.0/pipelines/{request.pipeline_id}/events', query=query)
            if 'events' not in json or not json['events']:
                return
            for v in json['events']:
                yield PipelineEvent.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

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
            if 'statuses' not in json or not json['statuses']:
                return
            for v in json['statuses']:
                yield PipelineStateInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

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

    def reset(self, pipeline_id: str, **kwargs) -> Wait[GetPipelineResponse]:
        """Reset a pipeline.
        
        Resets a pipeline."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Reset(pipeline_id=pipeline_id)

        self._api.do('POST', f'/api/2.0/pipelines/{request.pipeline_id}/reset')
        return Wait(self.wait_get_pipeline_running, pipeline_id=request.pipeline_id)

    def reset_and_wait(self, pipeline_id: str, timeout=timedelta(minutes=20)) -> GetPipelineResponse:
        return self.reset(pipeline_id=pipeline_id).result(timeout=timeout)

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

    def stop(self, pipeline_id: str, **kwargs) -> Wait[GetPipelineResponse]:
        """Stop a pipeline.
        
        Stops a pipeline."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Stop(pipeline_id=pipeline_id)

        self._api.do('POST', f'/api/2.0/pipelines/{request.pipeline_id}/stop')
        return Wait(self.wait_get_pipeline_idle, pipeline_id=request.pipeline_id)

    def stop_and_wait(self, pipeline_id: str, timeout=timedelta(minutes=20)) -> GetPipelineResponse:
        return self.stop(pipeline_id=pipeline_id).result(timeout=timeout)

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

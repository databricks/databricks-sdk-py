# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
import random
import time
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Any, Callable, Dict, Iterator, List, Optional

from ..errors import OperationFailed
from ._internal import Wait, _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

from databricks.sdk.service import compute

# all definitions in this file are in alphabetical order


@dataclass
class CreatePipeline:
    allow_duplicate_names: Optional[bool] = None
    catalog: Optional[str] = None
    channel: Optional[str] = None
    clusters: Optional['List[PipelineCluster]'] = None
    configuration: Optional['Dict[str,str]'] = None
    continuous: Optional[bool] = None
    development: Optional[bool] = None
    dry_run: Optional[bool] = None
    edition: Optional[str] = None
    filters: Optional['Filters'] = None
    id: Optional[str] = None
    libraries: Optional['List[PipelineLibrary]'] = None
    name: Optional[str] = None
    notifications: Optional['List[Notifications]'] = None
    photon: Optional[bool] = None
    serverless: Optional[bool] = None
    storage: Optional[str] = None
    target: Optional[str] = None
    trigger: Optional['PipelineTrigger'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.allow_duplicate_names is not None: body['allow_duplicate_names'] = self.allow_duplicate_names
        if self.catalog is not None: body['catalog'] = self.catalog
        if self.channel is not None: body['channel'] = self.channel
        if self.clusters: body['clusters'] = [v.as_dict() for v in self.clusters]
        if self.configuration: body['configuration'] = self.configuration
        if self.continuous is not None: body['continuous'] = self.continuous
        if self.development is not None: body['development'] = self.development
        if self.dry_run is not None: body['dry_run'] = self.dry_run
        if self.edition is not None: body['edition'] = self.edition
        if self.filters: body['filters'] = self.filters.as_dict()
        if self.id is not None: body['id'] = self.id
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        if self.name is not None: body['name'] = self.name
        if self.notifications: body['notifications'] = [v.as_dict() for v in self.notifications]
        if self.photon is not None: body['photon'] = self.photon
        if self.serverless is not None: body['serverless'] = self.serverless
        if self.storage is not None: body['storage'] = self.storage
        if self.target is not None: body['target'] = self.target
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
                   notifications=_repeated(d, 'notifications', Notifications),
                   photon=d.get('photon', None),
                   serverless=d.get('serverless', None),
                   storage=d.get('storage', None),
                   target=d.get('target', None),
                   trigger=_from_dict(d, 'trigger', PipelineTrigger))


@dataclass
class CreatePipelineResponse:
    effective_settings: Optional['PipelineSpec'] = None
    pipeline_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.effective_settings: body['effective_settings'] = self.effective_settings.as_dict()
        if self.pipeline_id is not None: body['pipeline_id'] = self.pipeline_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePipelineResponse':
        return cls(effective_settings=_from_dict(d, 'effective_settings', PipelineSpec),
                   pipeline_id=d.get('pipeline_id', None))


@dataclass
class CronTrigger:
    quartz_cron_schedule: Optional[str] = None
    timezone_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.quartz_cron_schedule is not None: body['quartz_cron_schedule'] = self.quartz_cron_schedule
        if self.timezone_id is not None: body['timezone_id'] = self.timezone_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CronTrigger':
        return cls(quartz_cron_schedule=d.get('quartz_cron_schedule', None),
                   timezone_id=d.get('timezone_id', None))


@dataclass
class DataPlaneId:
    instance: Optional[str] = None
    seq_no: Optional[Any] = None

    def as_dict(self) -> dict:
        body = {}
        if self.instance is not None: body['instance'] = self.instance
        if self.seq_no: body['seq_no'] = self.seq_no
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DataPlaneId':
        return cls(instance=d.get('instance', None), seq_no=d.get('seq_no', None))


@dataclass
class EditPipeline:
    allow_duplicate_names: Optional[bool] = None
    catalog: Optional[str] = None
    channel: Optional[str] = None
    clusters: Optional['List[PipelineCluster]'] = None
    configuration: Optional['Dict[str,str]'] = None
    continuous: Optional[bool] = None
    development: Optional[bool] = None
    edition: Optional[str] = None
    expected_last_modified: Optional[int] = None
    filters: Optional['Filters'] = None
    id: Optional[str] = None
    libraries: Optional['List[PipelineLibrary]'] = None
    name: Optional[str] = None
    notifications: Optional['List[Notifications]'] = None
    photon: Optional[bool] = None
    pipeline_id: Optional[str] = None
    serverless: Optional[bool] = None
    storage: Optional[str] = None
    target: Optional[str] = None
    trigger: Optional['PipelineTrigger'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.allow_duplicate_names is not None: body['allow_duplicate_names'] = self.allow_duplicate_names
        if self.catalog is not None: body['catalog'] = self.catalog
        if self.channel is not None: body['channel'] = self.channel
        if self.clusters: body['clusters'] = [v.as_dict() for v in self.clusters]
        if self.configuration: body['configuration'] = self.configuration
        if self.continuous is not None: body['continuous'] = self.continuous
        if self.development is not None: body['development'] = self.development
        if self.edition is not None: body['edition'] = self.edition
        if self.expected_last_modified is not None:
            body['expected_last_modified'] = self.expected_last_modified
        if self.filters: body['filters'] = self.filters.as_dict()
        if self.id is not None: body['id'] = self.id
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        if self.name is not None: body['name'] = self.name
        if self.notifications: body['notifications'] = [v.as_dict() for v in self.notifications]
        if self.photon is not None: body['photon'] = self.photon
        if self.pipeline_id is not None: body['pipeline_id'] = self.pipeline_id
        if self.serverless is not None: body['serverless'] = self.serverless
        if self.storage is not None: body['storage'] = self.storage
        if self.target is not None: body['target'] = self.target
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
                   notifications=_repeated(d, 'notifications', Notifications),
                   photon=d.get('photon', None),
                   pipeline_id=d.get('pipeline_id', None),
                   serverless=d.get('serverless', None),
                   storage=d.get('storage', None),
                   target=d.get('target', None),
                   trigger=_from_dict(d, 'trigger', PipelineTrigger))


@dataclass
class ErrorDetail:
    exceptions: Optional['List[SerializedException]'] = None
    fatal: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.exceptions: body['exceptions'] = [v.as_dict() for v in self.exceptions]
        if self.fatal is not None: body['fatal'] = self.fatal
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
class FileLibrary:
    path: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.path is not None: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FileLibrary':
        return cls(path=d.get('path', None))


@dataclass
class Filters:
    exclude: Optional['List[str]'] = None
    include: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.exclude: body['exclude'] = [v for v in self.exclude]
        if self.include: body['include'] = [v for v in self.include]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Filters':
        return cls(exclude=d.get('exclude', None), include=d.get('include', None))


@dataclass
class GetPipelinePermissionLevelsResponse:
    permission_levels: Optional['List[PipelinePermissionsDescription]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPipelinePermissionLevelsResponse':
        return cls(permission_levels=_repeated(d, 'permission_levels', PipelinePermissionsDescription))


@dataclass
class GetPipelineResponse:
    cause: Optional[str] = None
    cluster_id: Optional[str] = None
    creator_user_name: Optional[str] = None
    health: Optional['GetPipelineResponseHealth'] = None
    last_modified: Optional[int] = None
    latest_updates: Optional['List[UpdateStateInfo]'] = None
    name: Optional[str] = None
    pipeline_id: Optional[str] = None
    run_as_user_name: Optional[str] = None
    spec: Optional['PipelineSpec'] = None
    state: Optional['PipelineState'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cause is not None: body['cause'] = self.cause
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.creator_user_name is not None: body['creator_user_name'] = self.creator_user_name
        if self.health is not None: body['health'] = self.health.value
        if self.last_modified is not None: body['last_modified'] = self.last_modified
        if self.latest_updates: body['latest_updates'] = [v.as_dict() for v in self.latest_updates]
        if self.name is not None: body['name'] = self.name
        if self.pipeline_id is not None: body['pipeline_id'] = self.pipeline_id
        if self.run_as_user_name is not None: body['run_as_user_name'] = self.run_as_user_name
        if self.spec: body['spec'] = self.spec.as_dict()
        if self.state is not None: body['state'] = self.state.value
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
class GetUpdateResponse:
    update: Optional['UpdateInfo'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.update: body['update'] = self.update.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetUpdateResponse':
        return cls(update=_from_dict(d, 'update', UpdateInfo))


@dataclass
class ListPipelineEventsResponse:
    events: Optional['List[PipelineEvent]'] = None
    next_page_token: Optional[str] = None
    prev_page_token: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.events: body['events'] = [v.as_dict() for v in self.events]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.prev_page_token is not None: body['prev_page_token'] = self.prev_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListPipelineEventsResponse':
        return cls(events=_repeated(d, 'events', PipelineEvent),
                   next_page_token=d.get('next_page_token', None),
                   prev_page_token=d.get('prev_page_token', None))


@dataclass
class ListPipelinesResponse:
    next_page_token: Optional[str] = None
    statuses: Optional['List[PipelineStateInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.statuses: body['statuses'] = [v.as_dict() for v in self.statuses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListPipelinesResponse':
        return cls(next_page_token=d.get('next_page_token', None),
                   statuses=_repeated(d, 'statuses', PipelineStateInfo))


@dataclass
class ListUpdatesResponse:
    next_page_token: Optional[str] = None
    prev_page_token: Optional[str] = None
    updates: Optional['List[UpdateInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.prev_page_token is not None: body['prev_page_token'] = self.prev_page_token
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
    path: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.path is not None: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NotebookLibrary':
        return cls(path=d.get('path', None))


@dataclass
class Notifications:
    alerts: Optional['List[str]'] = None
    email_recipients: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.alerts: body['alerts'] = [v for v in self.alerts]
        if self.email_recipients: body['email_recipients'] = [v for v in self.email_recipients]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Notifications':
        return cls(alerts=d.get('alerts', None), email_recipients=d.get('email_recipients', None))


@dataclass
class Origin:
    batch_id: Optional[int] = None
    cloud: Optional[str] = None
    cluster_id: Optional[str] = None
    dataset_name: Optional[str] = None
    flow_id: Optional[str] = None
    flow_name: Optional[str] = None
    host: Optional[str] = None
    maintenance_id: Optional[str] = None
    materialization_name: Optional[str] = None
    org_id: Optional[int] = None
    pipeline_id: Optional[str] = None
    pipeline_name: Optional[str] = None
    region: Optional[str] = None
    request_id: Optional[str] = None
    table_id: Optional[str] = None
    uc_resource_id: Optional[str] = None
    update_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.batch_id is not None: body['batch_id'] = self.batch_id
        if self.cloud is not None: body['cloud'] = self.cloud
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.dataset_name is not None: body['dataset_name'] = self.dataset_name
        if self.flow_id is not None: body['flow_id'] = self.flow_id
        if self.flow_name is not None: body['flow_name'] = self.flow_name
        if self.host is not None: body['host'] = self.host
        if self.maintenance_id is not None: body['maintenance_id'] = self.maintenance_id
        if self.materialization_name is not None: body['materialization_name'] = self.materialization_name
        if self.org_id is not None: body['org_id'] = self.org_id
        if self.pipeline_id is not None: body['pipeline_id'] = self.pipeline_id
        if self.pipeline_name is not None: body['pipeline_name'] = self.pipeline_name
        if self.region is not None: body['region'] = self.region
        if self.request_id is not None: body['request_id'] = self.request_id
        if self.table_id is not None: body['table_id'] = self.table_id
        if self.uc_resource_id is not None: body['uc_resource_id'] = self.uc_resource_id
        if self.update_id is not None: body['update_id'] = self.update_id
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
class PipelineAccessControlRequest:
    group_name: Optional[str] = None
    permission_level: Optional['PipelinePermissionLevel'] = None
    service_principal_name: Optional[str] = None
    user_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineAccessControlRequest':
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', PipelinePermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class PipelineAccessControlResponse:
    all_permissions: Optional['List[PipelinePermission]'] = None
    display_name: Optional[str] = None
    group_name: Optional[str] = None
    service_principal_name: Optional[str] = None
    user_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.all_permissions: body['all_permissions'] = [v.as_dict() for v in self.all_permissions]
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineAccessControlResponse':
        return cls(all_permissions=_repeated(d, 'all_permissions', PipelinePermission),
                   display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class PipelineCluster:
    apply_policy_default_values: Optional[bool] = None
    autoscale: Optional['compute.AutoScale'] = None
    aws_attributes: Optional['compute.AwsAttributes'] = None
    azure_attributes: Optional['compute.AzureAttributes'] = None
    cluster_log_conf: Optional['compute.ClusterLogConf'] = None
    custom_tags: Optional['Dict[str,str]'] = None
    driver_instance_pool_id: Optional[str] = None
    driver_node_type_id: Optional[str] = None
    gcp_attributes: Optional['compute.GcpAttributes'] = None
    instance_pool_id: Optional[str] = None
    label: Optional[str] = None
    node_type_id: Optional[str] = None
    num_workers: Optional[int] = None
    policy_id: Optional[str] = None
    spark_conf: Optional['Dict[str,str]'] = None
    spark_env_vars: Optional['Dict[str,str]'] = None
    ssh_public_keys: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.apply_policy_default_values is not None:
            body['apply_policy_default_values'] = self.apply_policy_default_values
        if self.autoscale: body['autoscale'] = self.autoscale.as_dict()
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.cluster_log_conf: body['cluster_log_conf'] = self.cluster_log_conf.as_dict()
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.driver_instance_pool_id is not None:
            body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id is not None: body['driver_node_type_id'] = self.driver_node_type_id
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.instance_pool_id is not None: body['instance_pool_id'] = self.instance_pool_id
        if self.label is not None: body['label'] = self.label
        if self.node_type_id is not None: body['node_type_id'] = self.node_type_id
        if self.num_workers is not None: body['num_workers'] = self.num_workers
        if self.policy_id is not None: body['policy_id'] = self.policy_id
        if self.spark_conf: body['spark_conf'] = self.spark_conf
        if self.spark_env_vars: body['spark_env_vars'] = self.spark_env_vars
        if self.ssh_public_keys: body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineCluster':
        return cls(apply_policy_default_values=d.get('apply_policy_default_values', None),
                   autoscale=_from_dict(d, 'autoscale', compute.AutoScale),
                   aws_attributes=_from_dict(d, 'aws_attributes', compute.AwsAttributes),
                   azure_attributes=_from_dict(d, 'azure_attributes', compute.AzureAttributes),
                   cluster_log_conf=_from_dict(d, 'cluster_log_conf', compute.ClusterLogConf),
                   custom_tags=d.get('custom_tags', None),
                   driver_instance_pool_id=d.get('driver_instance_pool_id', None),
                   driver_node_type_id=d.get('driver_node_type_id', None),
                   gcp_attributes=_from_dict(d, 'gcp_attributes', compute.GcpAttributes),
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
    error: Optional['ErrorDetail'] = None
    event_type: Optional[str] = None
    id: Optional[str] = None
    level: Optional['EventLevel'] = None
    maturity_level: Optional['MaturityLevel'] = None
    message: Optional[str] = None
    origin: Optional['Origin'] = None
    sequence: Optional['Sequencing'] = None
    timestamp: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.error: body['error'] = self.error.as_dict()
        if self.event_type is not None: body['event_type'] = self.event_type
        if self.id is not None: body['id'] = self.id
        if self.level is not None: body['level'] = self.level.value
        if self.maturity_level is not None: body['maturity_level'] = self.maturity_level.value
        if self.message is not None: body['message'] = self.message
        if self.origin: body['origin'] = self.origin.as_dict()
        if self.sequence: body['sequence'] = self.sequence.as_dict()
        if self.timestamp is not None: body['timestamp'] = self.timestamp
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
    file: Optional['FileLibrary'] = None
    jar: Optional[str] = None
    maven: Optional['compute.MavenLibrary'] = None
    notebook: Optional['NotebookLibrary'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.file: body['file'] = self.file.as_dict()
        if self.jar is not None: body['jar'] = self.jar
        if self.maven: body['maven'] = self.maven.as_dict()
        if self.notebook: body['notebook'] = self.notebook.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineLibrary':
        return cls(file=_from_dict(d, 'file', FileLibrary),
                   jar=d.get('jar', None),
                   maven=_from_dict(d, 'maven', compute.MavenLibrary),
                   notebook=_from_dict(d, 'notebook', NotebookLibrary))


@dataclass
class PipelinePermission:
    inherited: Optional[bool] = None
    inherited_from_object: Optional['List[str]'] = None
    permission_level: Optional['PipelinePermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelinePermission':
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', PipelinePermissionLevel))


class PipelinePermissionLevel(Enum):
    """Permission level"""

    CAN_MANAGE = 'CAN_MANAGE'
    CAN_RUN = 'CAN_RUN'
    CAN_VIEW = 'CAN_VIEW'
    IS_OWNER = 'IS_OWNER'


@dataclass
class PipelinePermissions:
    access_control_list: Optional['List[PipelineAccessControlResponse]'] = None
    object_id: Optional[str] = None
    object_type: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None: body['object_id'] = self.object_id
        if self.object_type is not None: body['object_type'] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelinePermissions':
        return cls(access_control_list=_repeated(d, 'access_control_list', PipelineAccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class PipelinePermissionsDescription:
    description: Optional[str] = None
    permission_level: Optional['PipelinePermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelinePermissionsDescription':
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', PipelinePermissionLevel))


@dataclass
class PipelinePermissionsRequest:
    access_control_list: Optional['List[PipelineAccessControlRequest]'] = None
    pipeline_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.pipeline_id is not None: body['pipeline_id'] = self.pipeline_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelinePermissionsRequest':
        return cls(access_control_list=_repeated(d, 'access_control_list', PipelineAccessControlRequest),
                   pipeline_id=d.get('pipeline_id', None))


@dataclass
class PipelineSpec:
    catalog: Optional[str] = None
    channel: Optional[str] = None
    clusters: Optional['List[PipelineCluster]'] = None
    configuration: Optional['Dict[str,str]'] = None
    continuous: Optional[bool] = None
    development: Optional[bool] = None
    edition: Optional[str] = None
    filters: Optional['Filters'] = None
    id: Optional[str] = None
    libraries: Optional['List[PipelineLibrary]'] = None
    name: Optional[str] = None
    notifications: Optional['List[Notifications]'] = None
    photon: Optional[bool] = None
    serverless: Optional[bool] = None
    storage: Optional[str] = None
    target: Optional[str] = None
    trigger: Optional['PipelineTrigger'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.catalog is not None: body['catalog'] = self.catalog
        if self.channel is not None: body['channel'] = self.channel
        if self.clusters: body['clusters'] = [v.as_dict() for v in self.clusters]
        if self.configuration: body['configuration'] = self.configuration
        if self.continuous is not None: body['continuous'] = self.continuous
        if self.development is not None: body['development'] = self.development
        if self.edition is not None: body['edition'] = self.edition
        if self.filters: body['filters'] = self.filters.as_dict()
        if self.id is not None: body['id'] = self.id
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        if self.name is not None: body['name'] = self.name
        if self.notifications: body['notifications'] = [v.as_dict() for v in self.notifications]
        if self.photon is not None: body['photon'] = self.photon
        if self.serverless is not None: body['serverless'] = self.serverless
        if self.storage is not None: body['storage'] = self.storage
        if self.target is not None: body['target'] = self.target
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
                   notifications=_repeated(d, 'notifications', Notifications),
                   photon=d.get('photon', None),
                   serverless=d.get('serverless', None),
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
    cluster_id: Optional[str] = None
    creator_user_name: Optional[str] = None
    latest_updates: Optional['List[UpdateStateInfo]'] = None
    name: Optional[str] = None
    pipeline_id: Optional[str] = None
    run_as_user_name: Optional[str] = None
    state: Optional['PipelineState'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.creator_user_name is not None: body['creator_user_name'] = self.creator_user_name
        if self.latest_updates: body['latest_updates'] = [v.as_dict() for v in self.latest_updates]
        if self.name is not None: body['name'] = self.name
        if self.pipeline_id is not None: body['pipeline_id'] = self.pipeline_id
        if self.run_as_user_name is not None: body['run_as_user_name'] = self.run_as_user_name
        if self.state is not None: body['state'] = self.state.value
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
    cron: Optional['CronTrigger'] = None
    manual: Optional[Any] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cron: body['cron'] = self.cron.as_dict()
        if self.manual: body['manual'] = self.manual
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PipelineTrigger':
        return cls(cron=_from_dict(d, 'cron', CronTrigger), manual=d.get('manual', None))


@dataclass
class Sequencing:
    control_plane_seq_no: Optional[int] = None
    data_plane_id: Optional['DataPlaneId'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.control_plane_seq_no is not None: body['control_plane_seq_no'] = self.control_plane_seq_no
        if self.data_plane_id: body['data_plane_id'] = self.data_plane_id.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Sequencing':
        return cls(control_plane_seq_no=d.get('control_plane_seq_no', None),
                   data_plane_id=_from_dict(d, 'data_plane_id', DataPlaneId))


@dataclass
class SerializedException:
    class_name: Optional[str] = None
    message: Optional[str] = None
    stack: Optional['List[StackFrame]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.class_name is not None: body['class_name'] = self.class_name
        if self.message is not None: body['message'] = self.message
        if self.stack: body['stack'] = [v.as_dict() for v in self.stack]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SerializedException':
        return cls(class_name=d.get('class_name', None),
                   message=d.get('message', None),
                   stack=_repeated(d, 'stack', StackFrame))


@dataclass
class StackFrame:
    declaring_class: Optional[str] = None
    file_name: Optional[str] = None
    line_number: Optional[int] = None
    method_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.declaring_class is not None: body['declaring_class'] = self.declaring_class
        if self.file_name is not None: body['file_name'] = self.file_name
        if self.line_number is not None: body['line_number'] = self.line_number
        if self.method_name is not None: body['method_name'] = self.method_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StackFrame':
        return cls(declaring_class=d.get('declaring_class', None),
                   file_name=d.get('file_name', None),
                   line_number=d.get('line_number', None),
                   method_name=d.get('method_name', None))


@dataclass
class StartUpdate:
    cause: Optional['StartUpdateCause'] = None
    full_refresh: Optional[bool] = None
    full_refresh_selection: Optional['List[str]'] = None
    pipeline_id: Optional[str] = None
    refresh_selection: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cause is not None: body['cause'] = self.cause.value
        if self.full_refresh is not None: body['full_refresh'] = self.full_refresh
        if self.full_refresh_selection:
            body['full_refresh_selection'] = [v for v in self.full_refresh_selection]
        if self.pipeline_id is not None: body['pipeline_id'] = self.pipeline_id
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
    update_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.update_id is not None: body['update_id'] = self.update_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StartUpdateResponse':
        return cls(update_id=d.get('update_id', None))


@dataclass
class UpdateInfo:
    cause: Optional['UpdateInfoCause'] = None
    cluster_id: Optional[str] = None
    config: Optional['PipelineSpec'] = None
    creation_time: Optional[int] = None
    full_refresh: Optional[bool] = None
    full_refresh_selection: Optional['List[str]'] = None
    pipeline_id: Optional[str] = None
    refresh_selection: Optional['List[str]'] = None
    state: Optional['UpdateInfoState'] = None
    update_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cause is not None: body['cause'] = self.cause.value
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.config: body['config'] = self.config.as_dict()
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.full_refresh is not None: body['full_refresh'] = self.full_refresh
        if self.full_refresh_selection:
            body['full_refresh_selection'] = [v for v in self.full_refresh_selection]
        if self.pipeline_id is not None: body['pipeline_id'] = self.pipeline_id
        if self.refresh_selection: body['refresh_selection'] = [v for v in self.refresh_selection]
        if self.state is not None: body['state'] = self.state.value
        if self.update_id is not None: body['update_id'] = self.update_id
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
    creation_time: Optional[str] = None
    state: Optional['UpdateStateInfoState'] = None
    update_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.state is not None: body['state'] = self.state.value
        if self.update_id is not None: body['update_id'] = self.update_id
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

    def wait_get_pipeline_idle(
            self,
            pipeline_id: str,
            timeout=timedelta(minutes=20),
            callback: Optional[Callable[[GetPipelineResponse], None]] = None) -> GetPipelineResponse:
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
            if callback:
                callback(poll)
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

    def wait_get_pipeline_running(
            self,
            pipeline_id: str,
            timeout=timedelta(minutes=20),
            callback: Optional[Callable[[GetPipelineResponse], None]] = None) -> GetPipelineResponse:
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
            if callback:
                callback(poll)
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
               allow_duplicate_names: Optional[bool] = None,
               catalog: Optional[str] = None,
               channel: Optional[str] = None,
               clusters: Optional[List[PipelineCluster]] = None,
               configuration: Optional[Dict[str, str]] = None,
               continuous: Optional[bool] = None,
               development: Optional[bool] = None,
               dry_run: Optional[bool] = None,
               edition: Optional[str] = None,
               filters: Optional[Filters] = None,
               id: Optional[str] = None,
               libraries: Optional[List[PipelineLibrary]] = None,
               name: Optional[str] = None,
               notifications: Optional[List[Notifications]] = None,
               photon: Optional[bool] = None,
               serverless: Optional[bool] = None,
               storage: Optional[str] = None,
               target: Optional[str] = None,
               trigger: Optional[PipelineTrigger] = None) -> CreatePipelineResponse:
        """Create a pipeline.
        
        Creates a new data processing pipeline based on the requested configuration. If successful, this
        method returns the ID of the new pipeline.
        
        :param allow_duplicate_names: bool (optional)
          If false, deployment will fail if name conflicts with that of another pipeline.
        :param catalog: str (optional)
          A catalog in Unity Catalog to publish data from this pipeline to. If `target` is specified, tables
          in this pipeline are published to a `target` schema inside `catalog` (for example,
          `catalog`.`target`.`table`). If `target` is not specified, no data is published to Unity Catalog.
        :param channel: str (optional)
          DLT Release Channel that specifies which version to use.
        :param clusters: List[:class:`PipelineCluster`] (optional)
          Cluster settings for this pipeline deployment.
        :param configuration: Dict[str,str] (optional)
          String-String configuration for this pipeline execution.
        :param continuous: bool (optional)
          Whether the pipeline is continuous or triggered. This replaces `trigger`.
        :param development: bool (optional)
          Whether the pipeline is in Development mode. Defaults to false.
        :param dry_run: bool (optional)
        :param edition: str (optional)
          Pipeline product edition.
        :param filters: :class:`Filters` (optional)
          Filters on which Pipeline packages to include in the deployed graph.
        :param id: str (optional)
          Unique identifier for this pipeline.
        :param libraries: List[:class:`PipelineLibrary`] (optional)
          Libraries or code needed by this deployment.
        :param name: str (optional)
          Friendly identifier for this pipeline.
        :param notifications: List[:class:`Notifications`] (optional)
          List of notification settings for this pipeline.
        :param photon: bool (optional)
          Whether Photon is enabled for this pipeline.
        :param serverless: bool (optional)
          Whether serverless compute is enabled for this pipeline.
        :param storage: str (optional)
          DBFS root directory for storing checkpoints and tables.
        :param target: str (optional)
          Target schema (database) to add tables in this pipeline to. If not specified, no data is published
          to the Hive metastore or Unity Catalog. To publish to Unity Catalog, also specify `catalog`.
        :param trigger: :class:`PipelineTrigger` (optional)
          Which pipeline trigger to use. Deprecated: Use `continuous` instead.
        
        :returns: :class:`CreatePipelineResponse`
        """
        body = {}
        if allow_duplicate_names is not None: body['allow_duplicate_names'] = allow_duplicate_names
        if catalog is not None: body['catalog'] = catalog
        if channel is not None: body['channel'] = channel
        if clusters is not None: body['clusters'] = [v.as_dict() for v in clusters]
        if configuration is not None: body['configuration'] = configuration
        if continuous is not None: body['continuous'] = continuous
        if development is not None: body['development'] = development
        if dry_run is not None: body['dry_run'] = dry_run
        if edition is not None: body['edition'] = edition
        if filters is not None: body['filters'] = filters.as_dict()
        if id is not None: body['id'] = id
        if libraries is not None: body['libraries'] = [v.as_dict() for v in libraries]
        if name is not None: body['name'] = name
        if notifications is not None: body['notifications'] = [v.as_dict() for v in notifications]
        if photon is not None: body['photon'] = photon
        if serverless is not None: body['serverless'] = serverless
        if storage is not None: body['storage'] = storage
        if target is not None: body['target'] = target
        if trigger is not None: body['trigger'] = trigger.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/pipelines', body=body, headers=headers)
        return CreatePipelineResponse.from_dict(res)

    def delete(self, pipeline_id: str):
        """Delete a pipeline.
        
        Deletes a pipeline.
        
        :param pipeline_id: str
        
        
        """

        headers = {'Accept': 'application/json', }
        self._api.do('DELETE', f'/api/2.0/pipelines/{pipeline_id}', headers=headers)

    def get(self, pipeline_id: str) -> GetPipelineResponse:
        """Get a pipeline.
        
        :param pipeline_id: str
        
        :returns: :class:`GetPipelineResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/pipelines/{pipeline_id}', headers=headers)
        return GetPipelineResponse.from_dict(res)

    def get_permission_levels(self, pipeline_id: str) -> GetPipelinePermissionLevelsResponse:
        """Get pipeline permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param pipeline_id: str
          The pipeline for which to get or manage permissions.
        
        :returns: :class:`GetPipelinePermissionLevelsResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/permissions/pipelines/{pipeline_id}/permissionLevels',
                           headers=headers)
        return GetPipelinePermissionLevelsResponse.from_dict(res)

    def get_permissions(self, pipeline_id: str) -> PipelinePermissions:
        """Get pipeline permissions.
        
        Gets the permissions of a pipeline. Pipelines can inherit permissions from their root object.
        
        :param pipeline_id: str
          The pipeline for which to get or manage permissions.
        
        :returns: :class:`PipelinePermissions`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/permissions/pipelines/{pipeline_id}', headers=headers)
        return PipelinePermissions.from_dict(res)

    def get_update(self, pipeline_id: str, update_id: str) -> GetUpdateResponse:
        """Get a pipeline update.
        
        Gets an update from an active pipeline.
        
        :param pipeline_id: str
          The ID of the pipeline.
        :param update_id: str
          The ID of the update.
        
        :returns: :class:`GetUpdateResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/pipelines/{pipeline_id}/updates/{update_id}', headers=headers)
        return GetUpdateResponse.from_dict(res)

    def list_pipeline_events(self,
                             pipeline_id: str,
                             *,
                             filter: Optional[str] = None,
                             max_results: Optional[int] = None,
                             order_by: Optional[List[str]] = None,
                             page_token: Optional[str] = None) -> Iterator['PipelineEvent']:
        """List pipeline events.
        
        Retrieves events for a pipeline.
        
        :param pipeline_id: str
        :param filter: str (optional)
          Criteria to select a subset of results, expressed using a SQL-like syntax. The supported filters
          are: 1. level='INFO' (or WARN or ERROR) 2. level in ('INFO', 'WARN') 3. id='[event-id]' 4. timestamp
          > 'TIMESTAMP' (or >=,<,<=,=)
          
          Composite expressions are supported, for example: level in ('ERROR', 'WARN') AND timestamp>
          '2021-07-22T06:37:33.083Z'
        :param max_results: int (optional)
          Max number of entries to return in a single page. The system may return fewer than max_results
          events in a response, even if there are more events available.
        :param order_by: List[str] (optional)
          A string indicating a sort order by timestamp for the results, for example, ["timestamp asc"]. The
          sort order can be ascending or descending. By default, events are returned in descending order by
          timestamp.
        :param page_token: str (optional)
          Page token returned by previous call. This field is mutually exclusive with all fields in this
          request except max_results. An error is returned if any fields other than max_results are set when
          this field is set.
        
        :returns: Iterator over :class:`PipelineEvent`
        """

        query = {}
        if filter is not None: query['filter'] = filter
        if max_results is not None: query['max_results'] = max_results
        if order_by is not None: query['order_by'] = [v for v in order_by]
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET',
                                f'/api/2.0/pipelines/{pipeline_id}/events',
                                query=query,
                                headers=headers)
            if 'events' not in json or not json['events']:
                return
            for v in json['events']:
                yield PipelineEvent.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def list_pipelines(self,
                       *,
                       filter: Optional[str] = None,
                       max_results: Optional[int] = None,
                       order_by: Optional[List[str]] = None,
                       page_token: Optional[str] = None) -> Iterator['PipelineStateInfo']:
        """List pipelines.
        
        Lists pipelines defined in the Delta Live Tables system.
        
        :param filter: str (optional)
          Select a subset of results based on the specified criteria. The supported filters are:
          
          * `notebook='<path>'` to select pipelines that reference the provided notebook path. * `name LIKE
          '[pattern]'` to select pipelines with a name that matches pattern. Wildcards are supported, for
          example: `name LIKE '%shopping%'`
          
          Composite filters are not supported. This field is optional.
        :param max_results: int (optional)
          The maximum number of entries to return in a single page. The system may return fewer than
          max_results events in a response, even if there are more events available. This field is optional.
          The default value is 25. The maximum value is 100. An error is returned if the value of max_results
          is greater than 100.
        :param order_by: List[str] (optional)
          A list of strings specifying the order of results. Supported order_by fields are id and name. The
          default is id asc. This field is optional.
        :param page_token: str (optional)
          Page token returned by previous call
        
        :returns: Iterator over :class:`PipelineStateInfo`
        """

        query = {}
        if filter is not None: query['filter'] = filter
        if max_results is not None: query['max_results'] = max_results
        if order_by is not None: query['order_by'] = [v for v in order_by]
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.0/pipelines', query=query, headers=headers)
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
                     max_results: Optional[int] = None,
                     page_token: Optional[str] = None,
                     until_update_id: Optional[str] = None) -> ListUpdatesResponse:
        """List pipeline updates.
        
        List updates for an active pipeline.
        
        :param pipeline_id: str
          The pipeline to return updates for.
        :param max_results: int (optional)
          Max number of entries to return in a single page.
        :param page_token: str (optional)
          Page token returned by previous call
        :param until_update_id: str (optional)
          If present, returns updates until and including this update_id.
        
        :returns: :class:`ListUpdatesResponse`
        """

        query = {}
        if max_results is not None: query['max_results'] = max_results
        if page_token is not None: query['page_token'] = page_token
        if until_update_id is not None: query['until_update_id'] = until_update_id
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/pipelines/{pipeline_id}/updates', query=query, headers=headers)
        return ListUpdatesResponse.from_dict(res)

    def reset(self, pipeline_id: str) -> Wait[GetPipelineResponse]:
        """Reset a pipeline.
        
        Resets a pipeline.
        
        :param pipeline_id: str
        
        :returns:
          Long-running operation waiter for :class:`GetPipelineResponse`.
          See :method:wait_get_pipeline_running for more details.
        """

        headers = {'Accept': 'application/json', }
        self._api.do('POST', f'/api/2.0/pipelines/{pipeline_id}/reset', headers=headers)
        return Wait(self.wait_get_pipeline_running, pipeline_id=pipeline_id)

    def reset_and_wait(self, pipeline_id: str, timeout=timedelta(minutes=20)) -> GetPipelineResponse:
        return self.reset(pipeline_id=pipeline_id).result(timeout=timeout)

    def set_permissions(
            self,
            pipeline_id: str,
            *,
            access_control_list: Optional[List[PipelineAccessControlRequest]] = None) -> PipelinePermissions:
        """Set pipeline permissions.
        
        Sets permissions on a pipeline. Pipelines can inherit permissions from their root object.
        
        :param pipeline_id: str
          The pipeline for which to get or manage permissions.
        :param access_control_list: List[:class:`PipelineAccessControlRequest`] (optional)
        
        :returns: :class:`PipelinePermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PUT', f'/api/2.0/permissions/pipelines/{pipeline_id}', body=body, headers=headers)
        return PipelinePermissions.from_dict(res)

    def start_update(self,
                     pipeline_id: str,
                     *,
                     cause: Optional[StartUpdateCause] = None,
                     full_refresh: Optional[bool] = None,
                     full_refresh_selection: Optional[List[str]] = None,
                     refresh_selection: Optional[List[str]] = None) -> StartUpdateResponse:
        """Start a pipeline.
        
        Starts a new update for the pipeline. If there is already an active update for the pipeline, the
        request will fail and the active update will remain running.
        
        :param pipeline_id: str
        :param cause: :class:`StartUpdateCause` (optional)
        :param full_refresh: bool (optional)
          If true, this update will reset all tables before running.
        :param full_refresh_selection: List[str] (optional)
          A list of tables to update with fullRefresh. If both refresh_selection and full_refresh_selection
          are empty, this is a full graph update. Full Refresh on a table means that the states of the table
          will be reset before the refresh.
        :param refresh_selection: List[str] (optional)
          A list of tables to update without fullRefresh. If both refresh_selection and full_refresh_selection
          are empty, this is a full graph update. Full Refresh on a table means that the states of the table
          will be reset before the refresh.
        
        :returns: :class:`StartUpdateResponse`
        """
        body = {}
        if cause is not None: body['cause'] = cause.value
        if full_refresh is not None: body['full_refresh'] = full_refresh
        if full_refresh_selection is not None:
            body['full_refresh_selection'] = [v for v in full_refresh_selection]
        if refresh_selection is not None: body['refresh_selection'] = [v for v in refresh_selection]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', f'/api/2.0/pipelines/{pipeline_id}/updates', body=body, headers=headers)
        return StartUpdateResponse.from_dict(res)

    def stop(self, pipeline_id: str) -> Wait[GetPipelineResponse]:
        """Stop a pipeline.
        
        Stops the pipeline by canceling the active update. If there is no active update for the pipeline, this
        request is a no-op.
        
        :param pipeline_id: str
        
        :returns:
          Long-running operation waiter for :class:`GetPipelineResponse`.
          See :method:wait_get_pipeline_idle for more details.
        """

        headers = {'Accept': 'application/json', }
        self._api.do('POST', f'/api/2.0/pipelines/{pipeline_id}/stop', headers=headers)
        return Wait(self.wait_get_pipeline_idle, pipeline_id=pipeline_id)

    def stop_and_wait(self, pipeline_id: str, timeout=timedelta(minutes=20)) -> GetPipelineResponse:
        return self.stop(pipeline_id=pipeline_id).result(timeout=timeout)

    def update(self,
               pipeline_id: str,
               *,
               allow_duplicate_names: Optional[bool] = None,
               catalog: Optional[str] = None,
               channel: Optional[str] = None,
               clusters: Optional[List[PipelineCluster]] = None,
               configuration: Optional[Dict[str, str]] = None,
               continuous: Optional[bool] = None,
               development: Optional[bool] = None,
               edition: Optional[str] = None,
               expected_last_modified: Optional[int] = None,
               filters: Optional[Filters] = None,
               id: Optional[str] = None,
               libraries: Optional[List[PipelineLibrary]] = None,
               name: Optional[str] = None,
               notifications: Optional[List[Notifications]] = None,
               photon: Optional[bool] = None,
               serverless: Optional[bool] = None,
               storage: Optional[str] = None,
               target: Optional[str] = None,
               trigger: Optional[PipelineTrigger] = None):
        """Edit a pipeline.
        
        Updates a pipeline with the supplied configuration.
        
        :param pipeline_id: str
          Unique identifier for this pipeline.
        :param allow_duplicate_names: bool (optional)
          If false, deployment will fail if name has changed and conflicts the name of another pipeline.
        :param catalog: str (optional)
          A catalog in Unity Catalog to publish data from this pipeline to. If `target` is specified, tables
          in this pipeline are published to a `target` schema inside `catalog` (for example,
          `catalog`.`target`.`table`). If `target` is not specified, no data is published to Unity Catalog.
        :param channel: str (optional)
          DLT Release Channel that specifies which version to use.
        :param clusters: List[:class:`PipelineCluster`] (optional)
          Cluster settings for this pipeline deployment.
        :param configuration: Dict[str,str] (optional)
          String-String configuration for this pipeline execution.
        :param continuous: bool (optional)
          Whether the pipeline is continuous or triggered. This replaces `trigger`.
        :param development: bool (optional)
          Whether the pipeline is in Development mode. Defaults to false.
        :param edition: str (optional)
          Pipeline product edition.
        :param expected_last_modified: int (optional)
          If present, the last-modified time of the pipeline settings before the edit. If the settings were
          modified after that time, then the request will fail with a conflict.
        :param filters: :class:`Filters` (optional)
          Filters on which Pipeline packages to include in the deployed graph.
        :param id: str (optional)
          Unique identifier for this pipeline.
        :param libraries: List[:class:`PipelineLibrary`] (optional)
          Libraries or code needed by this deployment.
        :param name: str (optional)
          Friendly identifier for this pipeline.
        :param notifications: List[:class:`Notifications`] (optional)
          List of notification settings for this pipeline.
        :param photon: bool (optional)
          Whether Photon is enabled for this pipeline.
        :param serverless: bool (optional)
          Whether serverless compute is enabled for this pipeline.
        :param storage: str (optional)
          DBFS root directory for storing checkpoints and tables.
        :param target: str (optional)
          Target schema (database) to add tables in this pipeline to. If not specified, no data is published
          to the Hive metastore or Unity Catalog. To publish to Unity Catalog, also specify `catalog`.
        :param trigger: :class:`PipelineTrigger` (optional)
          Which pipeline trigger to use. Deprecated: Use `continuous` instead.
        
        
        """
        body = {}
        if allow_duplicate_names is not None: body['allow_duplicate_names'] = allow_duplicate_names
        if catalog is not None: body['catalog'] = catalog
        if channel is not None: body['channel'] = channel
        if clusters is not None: body['clusters'] = [v.as_dict() for v in clusters]
        if configuration is not None: body['configuration'] = configuration
        if continuous is not None: body['continuous'] = continuous
        if development is not None: body['development'] = development
        if edition is not None: body['edition'] = edition
        if expected_last_modified is not None: body['expected_last_modified'] = expected_last_modified
        if filters is not None: body['filters'] = filters.as_dict()
        if id is not None: body['id'] = id
        if libraries is not None: body['libraries'] = [v.as_dict() for v in libraries]
        if name is not None: body['name'] = name
        if notifications is not None: body['notifications'] = [v.as_dict() for v in notifications]
        if photon is not None: body['photon'] = photon
        if serverless is not None: body['serverless'] = serverless
        if storage is not None: body['storage'] = storage
        if target is not None: body['target'] = target
        if trigger is not None: body['trigger'] = trigger.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PUT', f'/api/2.0/pipelines/{pipeline_id}', body=body, headers=headers)

    def update_permissions(
            self,
            pipeline_id: str,
            *,
            access_control_list: Optional[List[PipelineAccessControlRequest]] = None) -> PipelinePermissions:
        """Update pipeline permissions.
        
        Updates the permissions on a pipeline. Pipelines can inherit permissions from their root object.
        
        :param pipeline_id: str
          The pipeline for which to get or manage permissions.
        :param access_control_list: List[:class:`PipelineAccessControlRequest`] (optional)
        
        :returns: :class:`PipelinePermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PATCH',
                           f'/api/2.0/permissions/pipelines/{pipeline_id}',
                           body=body,
                           headers=headers)
        return PipelinePermissions.from_dict(res)

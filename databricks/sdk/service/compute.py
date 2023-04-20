# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
import random
import time
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Any, Callable, Dict, Iterator, List

from ..errors import OperationFailed
from ._internal import Wait, _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AddInstanceProfile:
    instance_profile_arn: str
    iam_role_arn: str = None
    is_meta_instance_profile: bool = None
    skip_validation: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.iam_role_arn: body['iam_role_arn'] = self.iam_role_arn
        if self.instance_profile_arn: body['instance_profile_arn'] = self.instance_profile_arn
        if self.is_meta_instance_profile: body['is_meta_instance_profile'] = self.is_meta_instance_profile
        if self.skip_validation: body['skip_validation'] = self.skip_validation
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AddInstanceProfile':
        return cls(iam_role_arn=d.get('iam_role_arn', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   is_meta_instance_profile=d.get('is_meta_instance_profile', None),
                   skip_validation=d.get('skip_validation', None))


@dataclass
class AutoScale:
    min_workers: int
    max_workers: int

    def as_dict(self) -> dict:
        body = {}
        if self.max_workers: body['max_workers'] = self.max_workers
        if self.min_workers: body['min_workers'] = self.min_workers
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AutoScale':
        return cls(max_workers=d.get('max_workers', None), min_workers=d.get('min_workers', None))


@dataclass
class AwsAttributes:
    availability: 'AwsAvailability' = None
    ebs_volume_count: int = None
    ebs_volume_iops: int = None
    ebs_volume_size: int = None
    ebs_volume_throughput: int = None
    ebs_volume_type: 'EbsVolumeType' = None
    first_on_demand: int = None
    instance_profile_arn: str = None
    spot_bid_price_percent: int = None
    zone_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.availability: body['availability'] = self.availability.value
        if self.ebs_volume_count: body['ebs_volume_count'] = self.ebs_volume_count
        if self.ebs_volume_iops: body['ebs_volume_iops'] = self.ebs_volume_iops
        if self.ebs_volume_size: body['ebs_volume_size'] = self.ebs_volume_size
        if self.ebs_volume_throughput: body['ebs_volume_throughput'] = self.ebs_volume_throughput
        if self.ebs_volume_type: body['ebs_volume_type'] = self.ebs_volume_type.value
        if self.first_on_demand: body['first_on_demand'] = self.first_on_demand
        if self.instance_profile_arn: body['instance_profile_arn'] = self.instance_profile_arn
        if self.spot_bid_price_percent: body['spot_bid_price_percent'] = self.spot_bid_price_percent
        if self.zone_id: body['zone_id'] = self.zone_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AwsAttributes':
        return cls(availability=_enum(d, 'availability', AwsAvailability),
                   ebs_volume_count=d.get('ebs_volume_count', None),
                   ebs_volume_iops=d.get('ebs_volume_iops', None),
                   ebs_volume_size=d.get('ebs_volume_size', None),
                   ebs_volume_throughput=d.get('ebs_volume_throughput', None),
                   ebs_volume_type=_enum(d, 'ebs_volume_type', EbsVolumeType),
                   first_on_demand=d.get('first_on_demand', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   spot_bid_price_percent=d.get('spot_bid_price_percent', None),
                   zone_id=d.get('zone_id', None))


class AwsAvailability(Enum):
    """Availability type used for all subsequent nodes past the `first_on_demand` ones.
    
    Note: If `first_on_demand` is zero, this availability type will be used for the entire cluster."""

    ON_DEMAND = 'ON_DEMAND'
    SPOT = 'SPOT'
    SPOT_WITH_FALLBACK = 'SPOT_WITH_FALLBACK'


@dataclass
class AzureAttributes:
    availability: 'AzureAvailability' = None
    first_on_demand: int = None
    log_analytics_info: 'LogAnalyticsInfo' = None
    spot_bid_max_price: float = None

    def as_dict(self) -> dict:
        body = {}
        if self.availability: body['availability'] = self.availability.value
        if self.first_on_demand: body['first_on_demand'] = self.first_on_demand
        if self.log_analytics_info: body['log_analytics_info'] = self.log_analytics_info.as_dict()
        if self.spot_bid_max_price: body['spot_bid_max_price'] = self.spot_bid_max_price
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AzureAttributes':
        return cls(availability=_enum(d, 'availability', AzureAvailability),
                   first_on_demand=d.get('first_on_demand', None),
                   log_analytics_info=_from_dict(d, 'log_analytics_info', LogAnalyticsInfo),
                   spot_bid_max_price=d.get('spot_bid_max_price', None))


class AzureAvailability(Enum):
    """Availability type used for all subsequent nodes past the `first_on_demand` ones. Note: If
    `first_on_demand` is zero (which only happens on pool clusters), this availability type will be
    used for the entire cluster."""

    ON_DEMAND_AZURE = 'ON_DEMAND_AZURE'
    SPOT_AZURE = 'SPOT_AZURE'
    SPOT_WITH_FALLBACK_AZURE = 'SPOT_WITH_FALLBACK_AZURE'


@dataclass
class BaseClusterInfo:
    autoscale: 'AutoScale' = None
    autotermination_minutes: int = None
    aws_attributes: 'AwsAttributes' = None
    azure_attributes: 'AzureAttributes' = None
    cluster_log_conf: 'ClusterLogConf' = None
    cluster_name: str = None
    cluster_source: 'ClusterSource' = None
    custom_tags: 'Dict[str,str]' = None
    driver_instance_pool_id: str = None
    driver_node_type_id: str = None
    enable_elastic_disk: bool = None
    enable_local_disk_encryption: bool = None
    gcp_attributes: 'GcpAttributes' = None
    instance_pool_id: str = None
    node_type_id: str = None
    num_workers: int = None
    policy_id: str = None
    runtime_engine: 'RuntimeEngine' = None
    spark_conf: 'Dict[str,str]' = None
    spark_env_vars: 'Dict[str,str]' = None
    spark_version: str = None
    ssh_public_keys: 'List[str]' = None
    workload_type: 'WorkloadType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.autoscale: body['autoscale'] = self.autoscale.as_dict()
        if self.autotermination_minutes: body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.cluster_log_conf: body['cluster_log_conf'] = self.cluster_log_conf.as_dict()
        if self.cluster_name: body['cluster_name'] = self.cluster_name
        if self.cluster_source: body['cluster_source'] = self.cluster_source.value
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.driver_instance_pool_id: body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id: body['driver_node_type_id'] = self.driver_node_type_id
        if self.enable_elastic_disk: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption:
            body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.instance_pool_id: body['instance_pool_id'] = self.instance_pool_id
        if self.node_type_id: body['node_type_id'] = self.node_type_id
        if self.num_workers: body['num_workers'] = self.num_workers
        if self.policy_id: body['policy_id'] = self.policy_id
        if self.runtime_engine: body['runtime_engine'] = self.runtime_engine.value
        if self.spark_conf: body['spark_conf'] = self.spark_conf
        if self.spark_env_vars: body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version: body['spark_version'] = self.spark_version
        if self.ssh_public_keys: body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        if self.workload_type: body['workload_type'] = self.workload_type.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'BaseClusterInfo':
        return cls(autoscale=_from_dict(d, 'autoscale', AutoScale),
                   autotermination_minutes=d.get('autotermination_minutes', None),
                   aws_attributes=_from_dict(d, 'aws_attributes', AwsAttributes),
                   azure_attributes=_from_dict(d, 'azure_attributes', AzureAttributes),
                   cluster_log_conf=_from_dict(d, 'cluster_log_conf', ClusterLogConf),
                   cluster_name=d.get('cluster_name', None),
                   cluster_source=_enum(d, 'cluster_source', ClusterSource),
                   custom_tags=d.get('custom_tags', None),
                   driver_instance_pool_id=d.get('driver_instance_pool_id', None),
                   driver_node_type_id=d.get('driver_node_type_id', None),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
                   gcp_attributes=_from_dict(d, 'gcp_attributes', GcpAttributes),
                   instance_pool_id=d.get('instance_pool_id', None),
                   node_type_id=d.get('node_type_id', None),
                   num_workers=d.get('num_workers', None),
                   policy_id=d.get('policy_id', None),
                   runtime_engine=_enum(d, 'runtime_engine', RuntimeEngine),
                   spark_conf=d.get('spark_conf', None),
                   spark_env_vars=d.get('spark_env_vars', None),
                   spark_version=d.get('spark_version', None),
                   ssh_public_keys=d.get('ssh_public_keys', None),
                   workload_type=_from_dict(d, 'workload_type', WorkloadType))


@dataclass
class CancelCommand:
    cluster_id: str = None
    command_id: str = None
    context_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['clusterId'] = self.cluster_id
        if self.command_id: body['commandId'] = self.command_id
        if self.context_id: body['contextId'] = self.context_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CancelCommand':
        return cls(cluster_id=d.get('clusterId', None),
                   command_id=d.get('commandId', None),
                   context_id=d.get('contextId', None))


@dataclass
class ChangeClusterOwner:
    cluster_id: str
    owner_username: str

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.owner_username: body['owner_username'] = self.owner_username
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ChangeClusterOwner':
        return cls(cluster_id=d.get('cluster_id', None), owner_username=d.get('owner_username', None))


@dataclass
class ClientsTypes:
    jobs: bool = None
    notebooks: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.jobs: body['jobs'] = self.jobs
        if self.notebooks: body['notebooks'] = self.notebooks
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClientsTypes':
        return cls(jobs=d.get('jobs', None), notebooks=d.get('notebooks', None))


@dataclass
class CloudProviderNodeInfo:
    status: 'List[CloudProviderNodeStatus]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.status: body['status'] = [v for v in self.status]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CloudProviderNodeInfo':
        return cls(status=d.get('status', None))


class CloudProviderNodeStatus(Enum):

    NotAvailableInRegion = 'NotAvailableInRegion'
    NotEnabledOnSubscription = 'NotEnabledOnSubscription'


@dataclass
class ClusterAttributes:
    spark_version: str
    autotermination_minutes: int = None
    aws_attributes: 'AwsAttributes' = None
    azure_attributes: 'AzureAttributes' = None
    cluster_log_conf: 'ClusterLogConf' = None
    cluster_name: str = None
    cluster_source: 'ClusterSource' = None
    custom_tags: 'Dict[str,str]' = None
    driver_instance_pool_id: str = None
    driver_node_type_id: str = None
    enable_elastic_disk: bool = None
    enable_local_disk_encryption: bool = None
    gcp_attributes: 'GcpAttributes' = None
    instance_pool_id: str = None
    node_type_id: str = None
    policy_id: str = None
    runtime_engine: 'RuntimeEngine' = None
    spark_conf: 'Dict[str,str]' = None
    spark_env_vars: 'Dict[str,str]' = None
    ssh_public_keys: 'List[str]' = None
    workload_type: 'WorkloadType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.autotermination_minutes: body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.cluster_log_conf: body['cluster_log_conf'] = self.cluster_log_conf.as_dict()
        if self.cluster_name: body['cluster_name'] = self.cluster_name
        if self.cluster_source: body['cluster_source'] = self.cluster_source.value
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.driver_instance_pool_id: body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id: body['driver_node_type_id'] = self.driver_node_type_id
        if self.enable_elastic_disk: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption:
            body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.instance_pool_id: body['instance_pool_id'] = self.instance_pool_id
        if self.node_type_id: body['node_type_id'] = self.node_type_id
        if self.policy_id: body['policy_id'] = self.policy_id
        if self.runtime_engine: body['runtime_engine'] = self.runtime_engine.value
        if self.spark_conf: body['spark_conf'] = self.spark_conf
        if self.spark_env_vars: body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version: body['spark_version'] = self.spark_version
        if self.ssh_public_keys: body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        if self.workload_type: body['workload_type'] = self.workload_type.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterAttributes':
        return cls(autotermination_minutes=d.get('autotermination_minutes', None),
                   aws_attributes=_from_dict(d, 'aws_attributes', AwsAttributes),
                   azure_attributes=_from_dict(d, 'azure_attributes', AzureAttributes),
                   cluster_log_conf=_from_dict(d, 'cluster_log_conf', ClusterLogConf),
                   cluster_name=d.get('cluster_name', None),
                   cluster_source=_enum(d, 'cluster_source', ClusterSource),
                   custom_tags=d.get('custom_tags', None),
                   driver_instance_pool_id=d.get('driver_instance_pool_id', None),
                   driver_node_type_id=d.get('driver_node_type_id', None),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
                   gcp_attributes=_from_dict(d, 'gcp_attributes', GcpAttributes),
                   instance_pool_id=d.get('instance_pool_id', None),
                   node_type_id=d.get('node_type_id', None),
                   policy_id=d.get('policy_id', None),
                   runtime_engine=_enum(d, 'runtime_engine', RuntimeEngine),
                   spark_conf=d.get('spark_conf', None),
                   spark_env_vars=d.get('spark_env_vars', None),
                   spark_version=d.get('spark_version', None),
                   ssh_public_keys=d.get('ssh_public_keys', None),
                   workload_type=_from_dict(d, 'workload_type', WorkloadType))


@dataclass
class ClusterEvent:
    cluster_id: str
    data_plane_event_details: 'DataPlaneEventDetails' = None
    details: 'EventDetails' = None
    timestamp: int = None
    type: 'EventType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.data_plane_event_details:
            body['data_plane_event_details'] = self.data_plane_event_details.as_dict()
        if self.details: body['details'] = self.details.as_dict()
        if self.timestamp: body['timestamp'] = self.timestamp
        if self.type: body['type'] = self.type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterEvent':
        return cls(cluster_id=d.get('cluster_id', None),
                   data_plane_event_details=_from_dict(d, 'data_plane_event_details', DataPlaneEventDetails),
                   details=_from_dict(d, 'details', EventDetails),
                   timestamp=d.get('timestamp', None),
                   type=_enum(d, 'type', EventType))


@dataclass
class ClusterInfo:
    autoscale: 'AutoScale' = None
    autotermination_minutes: int = None
    aws_attributes: 'AwsAttributes' = None
    azure_attributes: 'AzureAttributes' = None
    cluster_cores: float = None
    cluster_id: str = None
    cluster_log_conf: 'ClusterLogConf' = None
    cluster_log_status: 'LogSyncStatus' = None
    cluster_memory_mb: int = None
    cluster_name: str = None
    cluster_source: 'ClusterSource' = None
    creator_user_name: str = None
    custom_tags: 'Dict[str,str]' = None
    data_security_mode: 'DataSecurityMode' = None
    default_tags: 'Dict[str,str]' = None
    driver: 'SparkNode' = None
    driver_instance_pool_id: str = None
    driver_node_type_id: str = None
    enable_elastic_disk: bool = None
    enable_local_disk_encryption: bool = None
    executors: 'List[SparkNode]' = None
    gcp_attributes: 'GcpAttributes' = None
    instance_pool_id: str = None
    jdbc_port: int = None
    last_restarted_time: int = None
    last_state_loss_time: int = None
    node_type_id: str = None
    num_workers: int = None
    policy_id: str = None
    runtime_engine: 'RuntimeEngine' = None
    single_user_name: str = None
    spark_conf: 'Dict[str,str]' = None
    spark_context_id: int = None
    spark_env_vars: 'Dict[str,str]' = None
    spark_version: str = None
    ssh_public_keys: 'List[str]' = None
    start_time: int = None
    state: 'State' = None
    state_message: str = None
    terminated_time: int = None
    termination_reason: 'TerminationReason' = None
    workload_type: 'WorkloadType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.autoscale: body['autoscale'] = self.autoscale.as_dict()
        if self.autotermination_minutes: body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.cluster_cores: body['cluster_cores'] = self.cluster_cores
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.cluster_log_conf: body['cluster_log_conf'] = self.cluster_log_conf.as_dict()
        if self.cluster_log_status: body['cluster_log_status'] = self.cluster_log_status.as_dict()
        if self.cluster_memory_mb: body['cluster_memory_mb'] = self.cluster_memory_mb
        if self.cluster_name: body['cluster_name'] = self.cluster_name
        if self.cluster_source: body['cluster_source'] = self.cluster_source.value
        if self.creator_user_name: body['creator_user_name'] = self.creator_user_name
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.data_security_mode: body['data_security_mode'] = self.data_security_mode.value
        if self.default_tags: body['default_tags'] = self.default_tags
        if self.driver: body['driver'] = self.driver.as_dict()
        if self.driver_instance_pool_id: body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id: body['driver_node_type_id'] = self.driver_node_type_id
        if self.enable_elastic_disk: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption:
            body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.executors: body['executors'] = [v.as_dict() for v in self.executors]
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.instance_pool_id: body['instance_pool_id'] = self.instance_pool_id
        if self.jdbc_port: body['jdbc_port'] = self.jdbc_port
        if self.last_restarted_time: body['last_restarted_time'] = self.last_restarted_time
        if self.last_state_loss_time: body['last_state_loss_time'] = self.last_state_loss_time
        if self.node_type_id: body['node_type_id'] = self.node_type_id
        if self.num_workers: body['num_workers'] = self.num_workers
        if self.policy_id: body['policy_id'] = self.policy_id
        if self.runtime_engine: body['runtime_engine'] = self.runtime_engine.value
        if self.single_user_name: body['single_user_name'] = self.single_user_name
        if self.spark_conf: body['spark_conf'] = self.spark_conf
        if self.spark_context_id: body['spark_context_id'] = self.spark_context_id
        if self.spark_env_vars: body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version: body['spark_version'] = self.spark_version
        if self.ssh_public_keys: body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        if self.start_time: body['start_time'] = self.start_time
        if self.state: body['state'] = self.state.value
        if self.state_message: body['state_message'] = self.state_message
        if self.terminated_time: body['terminated_time'] = self.terminated_time
        if self.termination_reason: body['termination_reason'] = self.termination_reason.as_dict()
        if self.workload_type: body['workload_type'] = self.workload_type.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterInfo':
        return cls(autoscale=_from_dict(d, 'autoscale', AutoScale),
                   autotermination_minutes=d.get('autotermination_minutes', None),
                   aws_attributes=_from_dict(d, 'aws_attributes', AwsAttributes),
                   azure_attributes=_from_dict(d, 'azure_attributes', AzureAttributes),
                   cluster_cores=d.get('cluster_cores', None),
                   cluster_id=d.get('cluster_id', None),
                   cluster_log_conf=_from_dict(d, 'cluster_log_conf', ClusterLogConf),
                   cluster_log_status=_from_dict(d, 'cluster_log_status', LogSyncStatus),
                   cluster_memory_mb=d.get('cluster_memory_mb', None),
                   cluster_name=d.get('cluster_name', None),
                   cluster_source=_enum(d, 'cluster_source', ClusterSource),
                   creator_user_name=d.get('creator_user_name', None),
                   custom_tags=d.get('custom_tags', None),
                   data_security_mode=_enum(d, 'data_security_mode', DataSecurityMode),
                   default_tags=d.get('default_tags', None),
                   driver=_from_dict(d, 'driver', SparkNode),
                   driver_instance_pool_id=d.get('driver_instance_pool_id', None),
                   driver_node_type_id=d.get('driver_node_type_id', None),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
                   executors=_repeated(d, 'executors', SparkNode),
                   gcp_attributes=_from_dict(d, 'gcp_attributes', GcpAttributes),
                   instance_pool_id=d.get('instance_pool_id', None),
                   jdbc_port=d.get('jdbc_port', None),
                   last_restarted_time=d.get('last_restarted_time', None),
                   last_state_loss_time=d.get('last_state_loss_time', None),
                   node_type_id=d.get('node_type_id', None),
                   num_workers=d.get('num_workers', None),
                   policy_id=d.get('policy_id', None),
                   runtime_engine=_enum(d, 'runtime_engine', RuntimeEngine),
                   single_user_name=d.get('single_user_name', None),
                   spark_conf=d.get('spark_conf', None),
                   spark_context_id=d.get('spark_context_id', None),
                   spark_env_vars=d.get('spark_env_vars', None),
                   spark_version=d.get('spark_version', None),
                   ssh_public_keys=d.get('ssh_public_keys', None),
                   start_time=d.get('start_time', None),
                   state=_enum(d, 'state', State),
                   state_message=d.get('state_message', None),
                   terminated_time=d.get('terminated_time', None),
                   termination_reason=_from_dict(d, 'termination_reason', TerminationReason),
                   workload_type=_from_dict(d, 'workload_type', WorkloadType))


@dataclass
class ClusterLibraryStatuses:
    cluster_id: str = None
    library_statuses: 'List[LibraryFullStatus]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.library_statuses: body['library_statuses'] = [v.as_dict() for v in self.library_statuses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterLibraryStatuses':
        return cls(cluster_id=d.get('cluster_id', None),
                   library_statuses=_repeated(d, 'library_statuses', LibraryFullStatus))


@dataclass
class ClusterLogConf:
    dbfs: 'DbfsStorageInfo' = None
    s3: 'S3StorageInfo' = None

    def as_dict(self) -> dict:
        body = {}
        if self.dbfs: body['dbfs'] = self.dbfs.as_dict()
        if self.s3: body['s3'] = self.s3.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterLogConf':
        return cls(dbfs=_from_dict(d, 'dbfs', DbfsStorageInfo), s3=_from_dict(d, 's3', S3StorageInfo))


@dataclass
class ClusterSize:
    autoscale: 'AutoScale' = None
    num_workers: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.autoscale: body['autoscale'] = self.autoscale.as_dict()
        if self.num_workers: body['num_workers'] = self.num_workers
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterSize':
        return cls(autoscale=_from_dict(d, 'autoscale', AutoScale), num_workers=d.get('num_workers', None))


class ClusterSource(Enum):
    """Determines whether the cluster was created by a user through the UI, created by the Databricks
    Jobs Scheduler, or through an API request. This is the same as cluster_creator, but read only."""

    API = 'API'
    JOB = 'JOB'
    MODELS = 'MODELS'
    PIPELINE = 'PIPELINE'
    PIPELINE_MAINTENANCE = 'PIPELINE_MAINTENANCE'
    SQL = 'SQL'
    UI = 'UI'


@dataclass
class ClusterStatusRequest:
    """Get status"""

    cluster_id: str


@dataclass
class Command:
    cluster_id: str = None
    command: str = None
    context_id: str = None
    language: 'Language' = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['clusterId'] = self.cluster_id
        if self.command: body['command'] = self.command
        if self.context_id: body['contextId'] = self.context_id
        if self.language: body['language'] = self.language.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Command':
        return cls(cluster_id=d.get('clusterId', None),
                   command=d.get('command', None),
                   context_id=d.get('contextId', None),
                   language=_enum(d, 'language', Language))


class CommandStatus(Enum):

    Cancelled = 'Cancelled'
    Cancelling = 'Cancelling'
    Error = 'Error'
    Finished = 'Finished'
    Queued = 'Queued'
    Running = 'Running'


@dataclass
class CommandStatusRequest:
    """Get command info"""

    cluster_id: str
    context_id: str
    command_id: str


@dataclass
class CommandStatusResponse:
    id: str = None
    results: 'Results' = None
    status: 'CommandStatus' = None

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        if self.results: body['results'] = self.results.as_dict()
        if self.status: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CommandStatusResponse':
        return cls(id=d.get('id', None),
                   results=_from_dict(d, 'results', Results),
                   status=_enum(d, 'status', CommandStatus))


class ContextStatus(Enum):

    Error = 'Error'
    Pending = 'Pending'
    Running = 'Running'


@dataclass
class ContextStatusRequest:
    """Get status"""

    cluster_id: str
    context_id: str


@dataclass
class ContextStatusResponse:
    id: str = None
    status: 'ContextStatus' = None

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        if self.status: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ContextStatusResponse':
        return cls(id=d.get('id', None), status=_enum(d, 'status', ContextStatus))


@dataclass
class CreateCluster:
    spark_version: str
    apply_policy_default_values: bool = None
    autoscale: 'AutoScale' = None
    autotermination_minutes: int = None
    aws_attributes: 'AwsAttributes' = None
    azure_attributes: 'AzureAttributes' = None
    cluster_log_conf: 'ClusterLogConf' = None
    cluster_name: str = None
    cluster_source: 'ClusterSource' = None
    custom_tags: 'Dict[str,str]' = None
    driver_instance_pool_id: str = None
    driver_node_type_id: str = None
    enable_elastic_disk: bool = None
    enable_local_disk_encryption: bool = None
    gcp_attributes: 'GcpAttributes' = None
    instance_pool_id: str = None
    node_type_id: str = None
    num_workers: int = None
    policy_id: str = None
    runtime_engine: 'RuntimeEngine' = None
    spark_conf: 'Dict[str,str]' = None
    spark_env_vars: 'Dict[str,str]' = None
    ssh_public_keys: 'List[str]' = None
    workload_type: 'WorkloadType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.apply_policy_default_values:
            body['apply_policy_default_values'] = self.apply_policy_default_values
        if self.autoscale: body['autoscale'] = self.autoscale.as_dict()
        if self.autotermination_minutes: body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.cluster_log_conf: body['cluster_log_conf'] = self.cluster_log_conf.as_dict()
        if self.cluster_name: body['cluster_name'] = self.cluster_name
        if self.cluster_source: body['cluster_source'] = self.cluster_source.value
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.driver_instance_pool_id: body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id: body['driver_node_type_id'] = self.driver_node_type_id
        if self.enable_elastic_disk: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption:
            body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.instance_pool_id: body['instance_pool_id'] = self.instance_pool_id
        if self.node_type_id: body['node_type_id'] = self.node_type_id
        if self.num_workers: body['num_workers'] = self.num_workers
        if self.policy_id: body['policy_id'] = self.policy_id
        if self.runtime_engine: body['runtime_engine'] = self.runtime_engine.value
        if self.spark_conf: body['spark_conf'] = self.spark_conf
        if self.spark_env_vars: body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version: body['spark_version'] = self.spark_version
        if self.ssh_public_keys: body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        if self.workload_type: body['workload_type'] = self.workload_type.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCluster':
        return cls(apply_policy_default_values=d.get('apply_policy_default_values', None),
                   autoscale=_from_dict(d, 'autoscale', AutoScale),
                   autotermination_minutes=d.get('autotermination_minutes', None),
                   aws_attributes=_from_dict(d, 'aws_attributes', AwsAttributes),
                   azure_attributes=_from_dict(d, 'azure_attributes', AzureAttributes),
                   cluster_log_conf=_from_dict(d, 'cluster_log_conf', ClusterLogConf),
                   cluster_name=d.get('cluster_name', None),
                   cluster_source=_enum(d, 'cluster_source', ClusterSource),
                   custom_tags=d.get('custom_tags', None),
                   driver_instance_pool_id=d.get('driver_instance_pool_id', None),
                   driver_node_type_id=d.get('driver_node_type_id', None),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
                   gcp_attributes=_from_dict(d, 'gcp_attributes', GcpAttributes),
                   instance_pool_id=d.get('instance_pool_id', None),
                   node_type_id=d.get('node_type_id', None),
                   num_workers=d.get('num_workers', None),
                   policy_id=d.get('policy_id', None),
                   runtime_engine=_enum(d, 'runtime_engine', RuntimeEngine),
                   spark_conf=d.get('spark_conf', None),
                   spark_env_vars=d.get('spark_env_vars', None),
                   spark_version=d.get('spark_version', None),
                   ssh_public_keys=d.get('ssh_public_keys', None),
                   workload_type=_from_dict(d, 'workload_type', WorkloadType))


@dataclass
class CreateClusterResponse:
    cluster_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateClusterResponse':
        return cls(cluster_id=d.get('cluster_id', None))


@dataclass
class CreateContext:
    cluster_id: str = None
    language: 'Language' = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['clusterId'] = self.cluster_id
        if self.language: body['language'] = self.language.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateContext':
        return cls(cluster_id=d.get('clusterId', None), language=_enum(d, 'language', Language))


@dataclass
class CreateInstancePool:
    instance_pool_name: str
    node_type_id: str
    aws_attributes: 'InstancePoolAwsAttributes' = None
    azure_attributes: 'InstancePoolAzureAttributes' = None
    custom_tags: 'Dict[str,str]' = None
    disk_spec: 'DiskSpec' = None
    enable_elastic_disk: bool = None
    idle_instance_autotermination_minutes: int = None
    instance_pool_fleet_attributes: 'InstancePoolFleetAttributes' = None
    max_capacity: int = None
    min_idle_instances: int = None
    preloaded_docker_images: 'List[DockerImage]' = None
    preloaded_spark_versions: 'List[str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.disk_spec: body['disk_spec'] = self.disk_spec.as_dict()
        if self.enable_elastic_disk: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.idle_instance_autotermination_minutes:
            body['idle_instance_autotermination_minutes'] = self.idle_instance_autotermination_minutes
        if self.instance_pool_fleet_attributes:
            body['instance_pool_fleet_attributes'] = self.instance_pool_fleet_attributes.as_dict()
        if self.instance_pool_name: body['instance_pool_name'] = self.instance_pool_name
        if self.max_capacity: body['max_capacity'] = self.max_capacity
        if self.min_idle_instances: body['min_idle_instances'] = self.min_idle_instances
        if self.node_type_id: body['node_type_id'] = self.node_type_id
        if self.preloaded_docker_images:
            body['preloaded_docker_images'] = [v.as_dict() for v in self.preloaded_docker_images]
        if self.preloaded_spark_versions:
            body['preloaded_spark_versions'] = [v for v in self.preloaded_spark_versions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateInstancePool':
        return cls(aws_attributes=_from_dict(d, 'aws_attributes', InstancePoolAwsAttributes),
                   azure_attributes=_from_dict(d, 'azure_attributes', InstancePoolAzureAttributes),
                   custom_tags=d.get('custom_tags', None),
                   disk_spec=_from_dict(d, 'disk_spec', DiskSpec),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   idle_instance_autotermination_minutes=d.get('idle_instance_autotermination_minutes', None),
                   instance_pool_fleet_attributes=_from_dict(d, 'instance_pool_fleet_attributes',
                                                             InstancePoolFleetAttributes),
                   instance_pool_name=d.get('instance_pool_name', None),
                   max_capacity=d.get('max_capacity', None),
                   min_idle_instances=d.get('min_idle_instances', None),
                   node_type_id=d.get('node_type_id', None),
                   preloaded_docker_images=_repeated(d, 'preloaded_docker_images', DockerImage),
                   preloaded_spark_versions=d.get('preloaded_spark_versions', None))


@dataclass
class CreateInstancePoolResponse:
    instance_pool_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.instance_pool_id: body['instance_pool_id'] = self.instance_pool_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateInstancePoolResponse':
        return cls(instance_pool_id=d.get('instance_pool_id', None))


@dataclass
class CreatePolicy:
    name: str
    definition: str = None
    description: str = None
    max_clusters_per_user: int = None
    policy_family_definition_overrides: str = None
    policy_family_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.definition: body['definition'] = self.definition
        if self.description: body['description'] = self.description
        if self.max_clusters_per_user: body['max_clusters_per_user'] = self.max_clusters_per_user
        if self.name: body['name'] = self.name
        if self.policy_family_definition_overrides:
            body['policy_family_definition_overrides'] = self.policy_family_definition_overrides
        if self.policy_family_id: body['policy_family_id'] = self.policy_family_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePolicy':
        return cls(definition=d.get('definition', None),
                   description=d.get('description', None),
                   max_clusters_per_user=d.get('max_clusters_per_user', None),
                   name=d.get('name', None),
                   policy_family_definition_overrides=d.get('policy_family_definition_overrides', None),
                   policy_family_id=d.get('policy_family_id', None))


@dataclass
class CreatePolicyResponse:
    policy_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.policy_id: body['policy_id'] = self.policy_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePolicyResponse':
        return cls(policy_id=d.get('policy_id', None))


@dataclass
class CreateResponse:
    script_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.script_id: body['script_id'] = self.script_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateResponse':
        return cls(script_id=d.get('script_id', None))


@dataclass
class Created:
    id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Created':
        return cls(id=d.get('id', None))


@dataclass
class DataPlaneEventDetails:
    event_type: 'DataPlaneEventDetailsEventType' = None
    executor_failures: int = None
    host_id: str = None
    timestamp: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.event_type: body['event_type'] = self.event_type.value
        if self.executor_failures: body['executor_failures'] = self.executor_failures
        if self.host_id: body['host_id'] = self.host_id
        if self.timestamp: body['timestamp'] = self.timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DataPlaneEventDetails':
        return cls(event_type=_enum(d, 'event_type', DataPlaneEventDetailsEventType),
                   executor_failures=d.get('executor_failures', None),
                   host_id=d.get('host_id', None),
                   timestamp=d.get('timestamp', None))


class DataPlaneEventDetailsEventType(Enum):
    """<needs content added>"""

    NODE_BLACKLISTED = 'NODE_BLACKLISTED'
    NODE_EXCLUDED_DECOMMISSIONED = 'NODE_EXCLUDED_DECOMMISSIONED'


class DataSecurityMode(Enum):
    """This describes an enum"""

    LEGACY_PASSTHROUGH = 'LEGACY_PASSTHROUGH'
    LEGACY_SINGLE_USER = 'LEGACY_SINGLE_USER'
    LEGACY_TABLE_ACL = 'LEGACY_TABLE_ACL'
    NONE = 'NONE'
    SINGLE_USER = 'SINGLE_USER'
    USER_ISOLATION = 'USER_ISOLATION'


@dataclass
class DbfsStorageInfo:
    destination: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.destination: body['destination'] = self.destination
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DbfsStorageInfo':
        return cls(destination=d.get('destination', None))


@dataclass
class DeleteCluster:
    cluster_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteCluster':
        return cls(cluster_id=d.get('cluster_id', None))


@dataclass
class DeleteGlobalInitScriptRequest:
    """Delete init script"""

    script_id: str


@dataclass
class DeleteInstancePool:
    instance_pool_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.instance_pool_id: body['instance_pool_id'] = self.instance_pool_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteInstancePool':
        return cls(instance_pool_id=d.get('instance_pool_id', None))


@dataclass
class DeletePolicy:
    policy_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.policy_id: body['policy_id'] = self.policy_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeletePolicy':
        return cls(policy_id=d.get('policy_id', None))


@dataclass
class DestroyContext:
    cluster_id: str
    context_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['clusterId'] = self.cluster_id
        if self.context_id: body['contextId'] = self.context_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DestroyContext':
        return cls(cluster_id=d.get('clusterId', None), context_id=d.get('contextId', None))


@dataclass
class DiskSpec:
    disk_count: int = None
    disk_iops: int = None
    disk_size: int = None
    disk_throughput: int = None
    disk_type: 'DiskType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.disk_count: body['disk_count'] = self.disk_count
        if self.disk_iops: body['disk_iops'] = self.disk_iops
        if self.disk_size: body['disk_size'] = self.disk_size
        if self.disk_throughput: body['disk_throughput'] = self.disk_throughput
        if self.disk_type: body['disk_type'] = self.disk_type.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DiskSpec':
        return cls(disk_count=d.get('disk_count', None),
                   disk_iops=d.get('disk_iops', None),
                   disk_size=d.get('disk_size', None),
                   disk_throughput=d.get('disk_throughput', None),
                   disk_type=_from_dict(d, 'disk_type', DiskType))


@dataclass
class DiskType:
    azure_disk_volume_type: 'DiskTypeAzureDiskVolumeType' = None
    ebs_volume_type: 'DiskTypeEbsVolumeType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.azure_disk_volume_type: body['azure_disk_volume_type'] = self.azure_disk_volume_type.value
        if self.ebs_volume_type: body['ebs_volume_type'] = self.ebs_volume_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DiskType':
        return cls(azure_disk_volume_type=_enum(d, 'azure_disk_volume_type', DiskTypeAzureDiskVolumeType),
                   ebs_volume_type=_enum(d, 'ebs_volume_type', DiskTypeEbsVolumeType))


class DiskTypeAzureDiskVolumeType(Enum):

    PREMIUM_LRS = 'PREMIUM_LRS'
    STANDARD_LRS = 'STANDARD_LRS'


class DiskTypeEbsVolumeType(Enum):

    GENERAL_PURPOSE_SSD = 'GENERAL_PURPOSE_SSD'
    THROUGHPUT_OPTIMIZED_HDD = 'THROUGHPUT_OPTIMIZED_HDD'


@dataclass
class DockerBasicAuth:
    password: str = None
    username: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.password: body['password'] = self.password
        if self.username: body['username'] = self.username
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DockerBasicAuth':
        return cls(password=d.get('password', None), username=d.get('username', None))


@dataclass
class DockerImage:
    basic_auth: 'DockerBasicAuth' = None
    url: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.basic_auth: body['basic_auth'] = self.basic_auth.as_dict()
        if self.url: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DockerImage':
        return cls(basic_auth=_from_dict(d, 'basic_auth', DockerBasicAuth), url=d.get('url', None))


class EbsVolumeType(Enum):
    """The type of EBS volumes that will be launched with this cluster."""

    GENERAL_PURPOSE_SSD = 'GENERAL_PURPOSE_SSD'
    THROUGHPUT_OPTIMIZED_HDD = 'THROUGHPUT_OPTIMIZED_HDD'


@dataclass
class EditCluster:
    cluster_id: str
    spark_version: str
    apply_policy_default_values: bool = None
    autoscale: 'AutoScale' = None
    autotermination_minutes: int = None
    aws_attributes: 'AwsAttributes' = None
    azure_attributes: 'AzureAttributes' = None
    cluster_log_conf: 'ClusterLogConf' = None
    cluster_name: str = None
    cluster_source: 'ClusterSource' = None
    custom_tags: 'Dict[str,str]' = None
    driver_instance_pool_id: str = None
    driver_node_type_id: str = None
    enable_elastic_disk: bool = None
    enable_local_disk_encryption: bool = None
    gcp_attributes: 'GcpAttributes' = None
    instance_pool_id: str = None
    node_type_id: str = None
    num_workers: int = None
    policy_id: str = None
    runtime_engine: 'RuntimeEngine' = None
    spark_conf: 'Dict[str,str]' = None
    spark_env_vars: 'Dict[str,str]' = None
    ssh_public_keys: 'List[str]' = None
    workload_type: 'WorkloadType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.apply_policy_default_values:
            body['apply_policy_default_values'] = self.apply_policy_default_values
        if self.autoscale: body['autoscale'] = self.autoscale.as_dict()
        if self.autotermination_minutes: body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.cluster_log_conf: body['cluster_log_conf'] = self.cluster_log_conf.as_dict()
        if self.cluster_name: body['cluster_name'] = self.cluster_name
        if self.cluster_source: body['cluster_source'] = self.cluster_source.value
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.driver_instance_pool_id: body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id: body['driver_node_type_id'] = self.driver_node_type_id
        if self.enable_elastic_disk: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption:
            body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.instance_pool_id: body['instance_pool_id'] = self.instance_pool_id
        if self.node_type_id: body['node_type_id'] = self.node_type_id
        if self.num_workers: body['num_workers'] = self.num_workers
        if self.policy_id: body['policy_id'] = self.policy_id
        if self.runtime_engine: body['runtime_engine'] = self.runtime_engine.value
        if self.spark_conf: body['spark_conf'] = self.spark_conf
        if self.spark_env_vars: body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version: body['spark_version'] = self.spark_version
        if self.ssh_public_keys: body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        if self.workload_type: body['workload_type'] = self.workload_type.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditCluster':
        return cls(apply_policy_default_values=d.get('apply_policy_default_values', None),
                   autoscale=_from_dict(d, 'autoscale', AutoScale),
                   autotermination_minutes=d.get('autotermination_minutes', None),
                   aws_attributes=_from_dict(d, 'aws_attributes', AwsAttributes),
                   azure_attributes=_from_dict(d, 'azure_attributes', AzureAttributes),
                   cluster_id=d.get('cluster_id', None),
                   cluster_log_conf=_from_dict(d, 'cluster_log_conf', ClusterLogConf),
                   cluster_name=d.get('cluster_name', None),
                   cluster_source=_enum(d, 'cluster_source', ClusterSource),
                   custom_tags=d.get('custom_tags', None),
                   driver_instance_pool_id=d.get('driver_instance_pool_id', None),
                   driver_node_type_id=d.get('driver_node_type_id', None),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
                   gcp_attributes=_from_dict(d, 'gcp_attributes', GcpAttributes),
                   instance_pool_id=d.get('instance_pool_id', None),
                   node_type_id=d.get('node_type_id', None),
                   num_workers=d.get('num_workers', None),
                   policy_id=d.get('policy_id', None),
                   runtime_engine=_enum(d, 'runtime_engine', RuntimeEngine),
                   spark_conf=d.get('spark_conf', None),
                   spark_env_vars=d.get('spark_env_vars', None),
                   spark_version=d.get('spark_version', None),
                   ssh_public_keys=d.get('ssh_public_keys', None),
                   workload_type=_from_dict(d, 'workload_type', WorkloadType))


@dataclass
class EditInstancePool:
    instance_pool_id: str
    instance_pool_name: str
    node_type_id: str
    aws_attributes: 'InstancePoolAwsAttributes' = None
    azure_attributes: 'InstancePoolAzureAttributes' = None
    custom_tags: 'Dict[str,str]' = None
    disk_spec: 'DiskSpec' = None
    enable_elastic_disk: bool = None
    idle_instance_autotermination_minutes: int = None
    instance_pool_fleet_attributes: 'InstancePoolFleetAttributes' = None
    max_capacity: int = None
    min_idle_instances: int = None
    preloaded_docker_images: 'List[DockerImage]' = None
    preloaded_spark_versions: 'List[str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.disk_spec: body['disk_spec'] = self.disk_spec.as_dict()
        if self.enable_elastic_disk: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.idle_instance_autotermination_minutes:
            body['idle_instance_autotermination_minutes'] = self.idle_instance_autotermination_minutes
        if self.instance_pool_fleet_attributes:
            body['instance_pool_fleet_attributes'] = self.instance_pool_fleet_attributes.as_dict()
        if self.instance_pool_id: body['instance_pool_id'] = self.instance_pool_id
        if self.instance_pool_name: body['instance_pool_name'] = self.instance_pool_name
        if self.max_capacity: body['max_capacity'] = self.max_capacity
        if self.min_idle_instances: body['min_idle_instances'] = self.min_idle_instances
        if self.node_type_id: body['node_type_id'] = self.node_type_id
        if self.preloaded_docker_images:
            body['preloaded_docker_images'] = [v.as_dict() for v in self.preloaded_docker_images]
        if self.preloaded_spark_versions:
            body['preloaded_spark_versions'] = [v for v in self.preloaded_spark_versions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditInstancePool':
        return cls(aws_attributes=_from_dict(d, 'aws_attributes', InstancePoolAwsAttributes),
                   azure_attributes=_from_dict(d, 'azure_attributes', InstancePoolAzureAttributes),
                   custom_tags=d.get('custom_tags', None),
                   disk_spec=_from_dict(d, 'disk_spec', DiskSpec),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   idle_instance_autotermination_minutes=d.get('idle_instance_autotermination_minutes', None),
                   instance_pool_fleet_attributes=_from_dict(d, 'instance_pool_fleet_attributes',
                                                             InstancePoolFleetAttributes),
                   instance_pool_id=d.get('instance_pool_id', None),
                   instance_pool_name=d.get('instance_pool_name', None),
                   max_capacity=d.get('max_capacity', None),
                   min_idle_instances=d.get('min_idle_instances', None),
                   node_type_id=d.get('node_type_id', None),
                   preloaded_docker_images=_repeated(d, 'preloaded_docker_images', DockerImage),
                   preloaded_spark_versions=d.get('preloaded_spark_versions', None))


@dataclass
class EditPolicy:
    policy_id: str
    name: str
    definition: str = None
    description: str = None
    max_clusters_per_user: int = None
    policy_family_definition_overrides: str = None
    policy_family_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.definition: body['definition'] = self.definition
        if self.description: body['description'] = self.description
        if self.max_clusters_per_user: body['max_clusters_per_user'] = self.max_clusters_per_user
        if self.name: body['name'] = self.name
        if self.policy_family_definition_overrides:
            body['policy_family_definition_overrides'] = self.policy_family_definition_overrides
        if self.policy_family_id: body['policy_family_id'] = self.policy_family_id
        if self.policy_id: body['policy_id'] = self.policy_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditPolicy':
        return cls(definition=d.get('definition', None),
                   description=d.get('description', None),
                   max_clusters_per_user=d.get('max_clusters_per_user', None),
                   name=d.get('name', None),
                   policy_family_definition_overrides=d.get('policy_family_definition_overrides', None),
                   policy_family_id=d.get('policy_family_id', None),
                   policy_id=d.get('policy_id', None))


@dataclass
class EventDetails:
    attributes: 'ClusterAttributes' = None
    cause: 'EventDetailsCause' = None
    cluster_size: 'ClusterSize' = None
    current_num_vcpus: int = None
    current_num_workers: int = None
    did_not_expand_reason: str = None
    disk_size: int = None
    driver_state_message: str = None
    enable_termination_for_node_blocklisted: bool = None
    free_space: int = None
    instance_id: str = None
    job_run_name: str = None
    previous_attributes: 'ClusterAttributes' = None
    previous_cluster_size: 'ClusterSize' = None
    previous_disk_size: int = None
    reason: 'TerminationReason' = None
    target_num_vcpus: int = None
    target_num_workers: int = None
    user: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.attributes: body['attributes'] = self.attributes.as_dict()
        if self.cause: body['cause'] = self.cause.value
        if self.cluster_size: body['cluster_size'] = self.cluster_size.as_dict()
        if self.current_num_vcpus: body['current_num_vcpus'] = self.current_num_vcpus
        if self.current_num_workers: body['current_num_workers'] = self.current_num_workers
        if self.did_not_expand_reason: body['did_not_expand_reason'] = self.did_not_expand_reason
        if self.disk_size: body['disk_size'] = self.disk_size
        if self.driver_state_message: body['driver_state_message'] = self.driver_state_message
        if self.enable_termination_for_node_blocklisted:
            body['enable_termination_for_node_blocklisted'] = self.enable_termination_for_node_blocklisted
        if self.free_space: body['free_space'] = self.free_space
        if self.instance_id: body['instance_id'] = self.instance_id
        if self.job_run_name: body['job_run_name'] = self.job_run_name
        if self.previous_attributes: body['previous_attributes'] = self.previous_attributes.as_dict()
        if self.previous_cluster_size: body['previous_cluster_size'] = self.previous_cluster_size.as_dict()
        if self.previous_disk_size: body['previous_disk_size'] = self.previous_disk_size
        if self.reason: body['reason'] = self.reason.as_dict()
        if self.target_num_vcpus: body['target_num_vcpus'] = self.target_num_vcpus
        if self.target_num_workers: body['target_num_workers'] = self.target_num_workers
        if self.user: body['user'] = self.user
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EventDetails':
        return cls(attributes=_from_dict(d, 'attributes', ClusterAttributes),
                   cause=_enum(d, 'cause', EventDetailsCause),
                   cluster_size=_from_dict(d, 'cluster_size', ClusterSize),
                   current_num_vcpus=d.get('current_num_vcpus', None),
                   current_num_workers=d.get('current_num_workers', None),
                   did_not_expand_reason=d.get('did_not_expand_reason', None),
                   disk_size=d.get('disk_size', None),
                   driver_state_message=d.get('driver_state_message', None),
                   enable_termination_for_node_blocklisted=d.get('enable_termination_for_node_blocklisted',
                                                                 None),
                   free_space=d.get('free_space', None),
                   instance_id=d.get('instance_id', None),
                   job_run_name=d.get('job_run_name', None),
                   previous_attributes=_from_dict(d, 'previous_attributes', ClusterAttributes),
                   previous_cluster_size=_from_dict(d, 'previous_cluster_size', ClusterSize),
                   previous_disk_size=d.get('previous_disk_size', None),
                   reason=_from_dict(d, 'reason', TerminationReason),
                   target_num_vcpus=d.get('target_num_vcpus', None),
                   target_num_workers=d.get('target_num_workers', None),
                   user=d.get('user', None))


class EventDetailsCause(Enum):
    """The cause of a change in target size."""

    AUTORECOVERY = 'AUTORECOVERY'
    AUTOSCALE = 'AUTOSCALE'
    REPLACE_BAD_NODES = 'REPLACE_BAD_NODES'
    USER_REQUEST = 'USER_REQUEST'


class EventType(Enum):

    AUTOSCALING_STATS_REPORT = 'AUTOSCALING_STATS_REPORT'
    CREATING = 'CREATING'
    DBFS_DOWN = 'DBFS_DOWN'
    DID_NOT_EXPAND_DISK = 'DID_NOT_EXPAND_DISK'
    DRIVER_HEALTHY = 'DRIVER_HEALTHY'
    DRIVER_NOT_RESPONDING = 'DRIVER_NOT_RESPONDING'
    DRIVER_UNAVAILABLE = 'DRIVER_UNAVAILABLE'
    EDITED = 'EDITED'
    EXPANDED_DISK = 'EXPANDED_DISK'
    FAILED_TO_EXPAND_DISK = 'FAILED_TO_EXPAND_DISK'
    INIT_SCRIPTS_FINISHED = 'INIT_SCRIPTS_FINISHED'
    INIT_SCRIPTS_STARTED = 'INIT_SCRIPTS_STARTED'
    METASTORE_DOWN = 'METASTORE_DOWN'
    NODE_BLACKLISTED = 'NODE_BLACKLISTED'
    NODE_EXCLUDED_DECOMMISSIONED = 'NODE_EXCLUDED_DECOMMISSIONED'
    NODES_LOST = 'NODES_LOST'
    PINNED = 'PINNED'
    RESIZING = 'RESIZING'
    RESTARTING = 'RESTARTING'
    RUNNING = 'RUNNING'
    SPARK_EXCEPTION = 'SPARK_EXCEPTION'
    STARTING = 'STARTING'
    TERMINATING = 'TERMINATING'
    UNPINNED = 'UNPINNED'
    UPSIZE_COMPLETED = 'UPSIZE_COMPLETED'


@dataclass
class FleetLaunchTemplateOverride:
    availability_zone: str
    instance_type: str
    max_price: float = None
    priority: float = None

    def as_dict(self) -> dict:
        body = {}
        if self.availability_zone: body['availability_zone'] = self.availability_zone
        if self.instance_type: body['instance_type'] = self.instance_type
        if self.max_price: body['max_price'] = self.max_price
        if self.priority: body['priority'] = self.priority
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FleetLaunchTemplateOverride':
        return cls(availability_zone=d.get('availability_zone', None),
                   instance_type=d.get('instance_type', None),
                   max_price=d.get('max_price', None),
                   priority=d.get('priority', None))


@dataclass
class FleetOnDemandOption:
    allocation_strategy: 'FleetOnDemandOptionAllocationStrategy' = None
    max_total_price: float = None
    use_capacity_reservations_first: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.allocation_strategy: body['allocation_strategy'] = self.allocation_strategy.value
        if self.max_total_price: body['max_total_price'] = self.max_total_price
        if self.use_capacity_reservations_first:
            body['use_capacity_reservations_first'] = self.use_capacity_reservations_first
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FleetOnDemandOption':
        return cls(allocation_strategy=_enum(d, 'allocation_strategy', FleetOnDemandOptionAllocationStrategy),
                   max_total_price=d.get('max_total_price', None),
                   use_capacity_reservations_first=d.get('use_capacity_reservations_first', None))


class FleetOnDemandOptionAllocationStrategy(Enum):
    """Only lowest-price and prioritized are allowed"""

    CAPACITY_OPTIMIZED = 'CAPACITY_OPTIMIZED'
    DIVERSIFIED = 'DIVERSIFIED'
    LOWEST_PRICE = 'LOWEST_PRICE'
    PRIORITIZED = 'PRIORITIZED'


@dataclass
class FleetSpotOption:
    allocation_strategy: 'FleetSpotOptionAllocationStrategy' = None
    instance_pools_to_use_count: int = None
    max_total_price: float = None

    def as_dict(self) -> dict:
        body = {}
        if self.allocation_strategy: body['allocation_strategy'] = self.allocation_strategy.value
        if self.instance_pools_to_use_count:
            body['instance_pools_to_use_count'] = self.instance_pools_to_use_count
        if self.max_total_price: body['max_total_price'] = self.max_total_price
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FleetSpotOption':
        return cls(allocation_strategy=_enum(d, 'allocation_strategy', FleetSpotOptionAllocationStrategy),
                   instance_pools_to_use_count=d.get('instance_pools_to_use_count', None),
                   max_total_price=d.get('max_total_price', None))


class FleetSpotOptionAllocationStrategy(Enum):
    """lowest-price | diversified | capacity-optimized"""

    CAPACITY_OPTIMIZED = 'CAPACITY_OPTIMIZED'
    DIVERSIFIED = 'DIVERSIFIED'
    LOWEST_PRICE = 'LOWEST_PRICE'
    PRIORITIZED = 'PRIORITIZED'


@dataclass
class GcpAttributes:
    availability: 'GcpAvailability' = None
    boot_disk_size: int = None
    google_service_account: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.availability: body['availability'] = self.availability.value
        if self.boot_disk_size: body['boot_disk_size'] = self.boot_disk_size
        if self.google_service_account: body['google_service_account'] = self.google_service_account
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GcpAttributes':
        return cls(availability=_enum(d, 'availability', GcpAvailability),
                   boot_disk_size=d.get('boot_disk_size', None),
                   google_service_account=d.get('google_service_account', None))


class GcpAvailability(Enum):
    """This field determines whether the spark executors will be scheduled to run on preemptible VMs,
    on-demand VMs, or preemptible VMs with a fallback to on-demand VMs if the former is unavailable."""

    ON_DEMAND_GCP = 'ON_DEMAND_GCP'
    PREEMPTIBLE_GCP = 'PREEMPTIBLE_GCP'
    PREEMPTIBLE_WITH_FALLBACK_GCP = 'PREEMPTIBLE_WITH_FALLBACK_GCP'


@dataclass
class GetClusterPolicyRequest:
    """Get entity"""

    policy_id: str


@dataclass
class GetClusterRequest:
    """Get cluster info"""

    cluster_id: str


@dataclass
class GetEvents:
    cluster_id: str
    end_time: int = None
    event_types: 'List[EventType]' = None
    limit: int = None
    offset: int = None
    order: 'GetEventsOrder' = None
    start_time: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.end_time: body['end_time'] = self.end_time
        if self.event_types: body['event_types'] = [v for v in self.event_types]
        if self.limit: body['limit'] = self.limit
        if self.offset: body['offset'] = self.offset
        if self.order: body['order'] = self.order.value
        if self.start_time: body['start_time'] = self.start_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetEvents':
        return cls(cluster_id=d.get('cluster_id', None),
                   end_time=d.get('end_time', None),
                   event_types=d.get('event_types', None),
                   limit=d.get('limit', None),
                   offset=d.get('offset', None),
                   order=_enum(d, 'order', GetEventsOrder),
                   start_time=d.get('start_time', None))


class GetEventsOrder(Enum):
    """The order to list events in; either "ASC" or "DESC". Defaults to "DESC"."""

    ASC = 'ASC'
    DESC = 'DESC'


@dataclass
class GetEventsResponse:
    events: 'List[ClusterEvent]' = None
    next_page: 'GetEvents' = None
    total_count: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.events: body['events'] = [v.as_dict() for v in self.events]
        if self.next_page: body['next_page'] = self.next_page.as_dict()
        if self.total_count: body['total_count'] = self.total_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetEventsResponse':
        return cls(events=_repeated(d, 'events', ClusterEvent),
                   next_page=_from_dict(d, 'next_page', GetEvents),
                   total_count=d.get('total_count', None))


@dataclass
class GetGlobalInitScriptRequest:
    """Get an init script"""

    script_id: str


@dataclass
class GetInstancePool:
    instance_pool_id: str
    aws_attributes: 'InstancePoolAwsAttributes' = None
    azure_attributes: 'InstancePoolAzureAttributes' = None
    custom_tags: 'Dict[str,str]' = None
    default_tags: 'Dict[str,str]' = None
    disk_spec: 'DiskSpec' = None
    enable_elastic_disk: bool = None
    idle_instance_autotermination_minutes: int = None
    instance_pool_fleet_attributes: 'InstancePoolFleetAttributes' = None
    instance_pool_name: str = None
    max_capacity: int = None
    min_idle_instances: int = None
    node_type_id: str = None
    preloaded_docker_images: 'List[DockerImage]' = None
    preloaded_spark_versions: 'List[str]' = None
    state: 'InstancePoolState' = None
    stats: 'InstancePoolStats' = None
    status: 'InstancePoolStatus' = None

    def as_dict(self) -> dict:
        body = {}
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.default_tags: body['default_tags'] = self.default_tags
        if self.disk_spec: body['disk_spec'] = self.disk_spec.as_dict()
        if self.enable_elastic_disk: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.idle_instance_autotermination_minutes:
            body['idle_instance_autotermination_minutes'] = self.idle_instance_autotermination_minutes
        if self.instance_pool_fleet_attributes:
            body['instance_pool_fleet_attributes'] = self.instance_pool_fleet_attributes.as_dict()
        if self.instance_pool_id: body['instance_pool_id'] = self.instance_pool_id
        if self.instance_pool_name: body['instance_pool_name'] = self.instance_pool_name
        if self.max_capacity: body['max_capacity'] = self.max_capacity
        if self.min_idle_instances: body['min_idle_instances'] = self.min_idle_instances
        if self.node_type_id: body['node_type_id'] = self.node_type_id
        if self.preloaded_docker_images:
            body['preloaded_docker_images'] = [v.as_dict() for v in self.preloaded_docker_images]
        if self.preloaded_spark_versions:
            body['preloaded_spark_versions'] = [v for v in self.preloaded_spark_versions]
        if self.state: body['state'] = self.state.value
        if self.stats: body['stats'] = self.stats.as_dict()
        if self.status: body['status'] = self.status.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetInstancePool':
        return cls(aws_attributes=_from_dict(d, 'aws_attributes', InstancePoolAwsAttributes),
                   azure_attributes=_from_dict(d, 'azure_attributes', InstancePoolAzureAttributes),
                   custom_tags=d.get('custom_tags', None),
                   default_tags=d.get('default_tags', None),
                   disk_spec=_from_dict(d, 'disk_spec', DiskSpec),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   idle_instance_autotermination_minutes=d.get('idle_instance_autotermination_minutes', None),
                   instance_pool_fleet_attributes=_from_dict(d, 'instance_pool_fleet_attributes',
                                                             InstancePoolFleetAttributes),
                   instance_pool_id=d.get('instance_pool_id', None),
                   instance_pool_name=d.get('instance_pool_name', None),
                   max_capacity=d.get('max_capacity', None),
                   min_idle_instances=d.get('min_idle_instances', None),
                   node_type_id=d.get('node_type_id', None),
                   preloaded_docker_images=_repeated(d, 'preloaded_docker_images', DockerImage),
                   preloaded_spark_versions=d.get('preloaded_spark_versions', None),
                   state=_enum(d, 'state', InstancePoolState),
                   stats=_from_dict(d, 'stats', InstancePoolStats),
                   status=_from_dict(d, 'status', InstancePoolStatus))


@dataclass
class GetInstancePoolRequest:
    """Get instance pool information"""

    instance_pool_id: str


@dataclass
class GetPolicyFamilyRequest:
    policy_family_id: str


@dataclass
class GetSparkVersionsResponse:
    versions: 'List[SparkVersion]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.versions: body['versions'] = [v.as_dict() for v in self.versions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetSparkVersionsResponse':
        return cls(versions=_repeated(d, 'versions', SparkVersion))


@dataclass
class GlobalInitScriptCreateRequest:
    name: str
    script: str
    enabled: bool = None
    position: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.enabled: body['enabled'] = self.enabled
        if self.name: body['name'] = self.name
        if self.position: body['position'] = self.position
        if self.script: body['script'] = self.script
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptCreateRequest':
        return cls(enabled=d.get('enabled', None),
                   name=d.get('name', None),
                   position=d.get('position', None),
                   script=d.get('script', None))


@dataclass
class GlobalInitScriptDetails:
    created_at: int = None
    created_by: str = None
    enabled: bool = None
    name: str = None
    position: int = None
    script_id: str = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.enabled: body['enabled'] = self.enabled
        if self.name: body['name'] = self.name
        if self.position: body['position'] = self.position
        if self.script_id: body['script_id'] = self.script_id
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptDetails':
        return cls(created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   enabled=d.get('enabled', None),
                   name=d.get('name', None),
                   position=d.get('position', None),
                   script_id=d.get('script_id', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


@dataclass
class GlobalInitScriptDetailsWithContent:
    created_at: int = None
    created_by: str = None
    enabled: bool = None
    name: str = None
    position: int = None
    script: str = None
    script_id: str = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.enabled: body['enabled'] = self.enabled
        if self.name: body['name'] = self.name
        if self.position: body['position'] = self.position
        if self.script: body['script'] = self.script
        if self.script_id: body['script_id'] = self.script_id
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptDetailsWithContent':
        return cls(created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   enabled=d.get('enabled', None),
                   name=d.get('name', None),
                   position=d.get('position', None),
                   script=d.get('script', None),
                   script_id=d.get('script_id', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


@dataclass
class GlobalInitScriptUpdateRequest:
    name: str
    script: str
    script_id: str
    enabled: bool = None
    position: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.enabled: body['enabled'] = self.enabled
        if self.name: body['name'] = self.name
        if self.position: body['position'] = self.position
        if self.script: body['script'] = self.script
        if self.script_id: body['script_id'] = self.script_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptUpdateRequest':
        return cls(enabled=d.get('enabled', None),
                   name=d.get('name', None),
                   position=d.get('position', None),
                   script=d.get('script', None),
                   script_id=d.get('script_id', None))


@dataclass
class InstallLibraries:
    cluster_id: str
    libraries: 'List[Library]'

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstallLibraries':
        return cls(cluster_id=d.get('cluster_id', None), libraries=_repeated(d, 'libraries', Library))


@dataclass
class InstancePoolAndStats:
    aws_attributes: 'InstancePoolAwsAttributes' = None
    azure_attributes: 'InstancePoolAzureAttributes' = None
    custom_tags: 'Dict[str,str]' = None
    default_tags: 'Dict[str,str]' = None
    disk_spec: 'DiskSpec' = None
    enable_elastic_disk: bool = None
    idle_instance_autotermination_minutes: int = None
    instance_pool_fleet_attributes: 'InstancePoolFleetAttributes' = None
    instance_pool_id: str = None
    instance_pool_name: str = None
    max_capacity: int = None
    min_idle_instances: int = None
    node_type_id: str = None
    preloaded_docker_images: 'List[DockerImage]' = None
    preloaded_spark_versions: 'List[str]' = None
    state: 'InstancePoolState' = None
    stats: 'InstancePoolStats' = None
    status: 'InstancePoolStatus' = None

    def as_dict(self) -> dict:
        body = {}
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.default_tags: body['default_tags'] = self.default_tags
        if self.disk_spec: body['disk_spec'] = self.disk_spec.as_dict()
        if self.enable_elastic_disk: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.idle_instance_autotermination_minutes:
            body['idle_instance_autotermination_minutes'] = self.idle_instance_autotermination_minutes
        if self.instance_pool_fleet_attributes:
            body['instance_pool_fleet_attributes'] = self.instance_pool_fleet_attributes.as_dict()
        if self.instance_pool_id: body['instance_pool_id'] = self.instance_pool_id
        if self.instance_pool_name: body['instance_pool_name'] = self.instance_pool_name
        if self.max_capacity: body['max_capacity'] = self.max_capacity
        if self.min_idle_instances: body['min_idle_instances'] = self.min_idle_instances
        if self.node_type_id: body['node_type_id'] = self.node_type_id
        if self.preloaded_docker_images:
            body['preloaded_docker_images'] = [v.as_dict() for v in self.preloaded_docker_images]
        if self.preloaded_spark_versions:
            body['preloaded_spark_versions'] = [v for v in self.preloaded_spark_versions]
        if self.state: body['state'] = self.state.value
        if self.stats: body['stats'] = self.stats.as_dict()
        if self.status: body['status'] = self.status.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolAndStats':
        return cls(aws_attributes=_from_dict(d, 'aws_attributes', InstancePoolAwsAttributes),
                   azure_attributes=_from_dict(d, 'azure_attributes', InstancePoolAzureAttributes),
                   custom_tags=d.get('custom_tags', None),
                   default_tags=d.get('default_tags', None),
                   disk_spec=_from_dict(d, 'disk_spec', DiskSpec),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   idle_instance_autotermination_minutes=d.get('idle_instance_autotermination_minutes', None),
                   instance_pool_fleet_attributes=_from_dict(d, 'instance_pool_fleet_attributes',
                                                             InstancePoolFleetAttributes),
                   instance_pool_id=d.get('instance_pool_id', None),
                   instance_pool_name=d.get('instance_pool_name', None),
                   max_capacity=d.get('max_capacity', None),
                   min_idle_instances=d.get('min_idle_instances', None),
                   node_type_id=d.get('node_type_id', None),
                   preloaded_docker_images=_repeated(d, 'preloaded_docker_images', DockerImage),
                   preloaded_spark_versions=d.get('preloaded_spark_versions', None),
                   state=_enum(d, 'state', InstancePoolState),
                   stats=_from_dict(d, 'stats', InstancePoolStats),
                   status=_from_dict(d, 'status', InstancePoolStatus))


@dataclass
class InstancePoolAwsAttributes:
    availability: 'InstancePoolAwsAttributesAvailability' = None
    spot_bid_price_percent: int = None
    zone_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.availability: body['availability'] = self.availability.value
        if self.spot_bid_price_percent: body['spot_bid_price_percent'] = self.spot_bid_price_percent
        if self.zone_id: body['zone_id'] = self.zone_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolAwsAttributes':
        return cls(availability=_enum(d, 'availability', InstancePoolAwsAttributesAvailability),
                   spot_bid_price_percent=d.get('spot_bid_price_percent', None),
                   zone_id=d.get('zone_id', None))


class InstancePoolAwsAttributesAvailability(Enum):
    """Availability type used for the spot nodes.
    
    The default value is defined by InstancePoolConf.instancePoolDefaultAwsAvailability"""

    ON_DEMAND = 'ON_DEMAND'
    SPOT = 'SPOT'
    SPOT_WITH_FALLBACK = 'SPOT_WITH_FALLBACK'


@dataclass
class InstancePoolAzureAttributes:
    availability: 'InstancePoolAzureAttributesAvailability' = None
    spot_bid_max_price: float = None

    def as_dict(self) -> dict:
        body = {}
        if self.availability: body['availability'] = self.availability.value
        if self.spot_bid_max_price: body['spot_bid_max_price'] = self.spot_bid_max_price
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolAzureAttributes':
        return cls(availability=_enum(d, 'availability', InstancePoolAzureAttributesAvailability),
                   spot_bid_max_price=d.get('spot_bid_max_price', None))


class InstancePoolAzureAttributesAvailability(Enum):
    """Shows the Availability type used for the spot nodes.
    
    The default value is defined by InstancePoolConf.instancePoolDefaultAzureAvailability"""

    ON_DEMAND_AZURE = 'ON_DEMAND_AZURE'
    SPOT_AZURE = 'SPOT_AZURE'
    SPOT_WITH_FALLBACK_AZURE = 'SPOT_WITH_FALLBACK_AZURE'


@dataclass
class InstancePoolFleetAttributes:
    fleet_on_demand_option: 'FleetOnDemandOption' = None
    fleet_spot_option: 'FleetSpotOption' = None
    launch_template_overrides: 'List[FleetLaunchTemplateOverride]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.fleet_on_demand_option: body['fleet_on_demand_option'] = self.fleet_on_demand_option.as_dict()
        if self.fleet_spot_option: body['fleet_spot_option'] = self.fleet_spot_option.as_dict()
        if self.launch_template_overrides:
            body['launch_template_overrides'] = [v.as_dict() for v in self.launch_template_overrides]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolFleetAttributes':
        return cls(fleet_on_demand_option=_from_dict(d, 'fleet_on_demand_option', FleetOnDemandOption),
                   fleet_spot_option=_from_dict(d, 'fleet_spot_option', FleetSpotOption),
                   launch_template_overrides=_repeated(d, 'launch_template_overrides',
                                                       FleetLaunchTemplateOverride))


class InstancePoolState(Enum):
    """Current state of the instance pool."""

    ACTIVE = 'ACTIVE'
    DELETED = 'DELETED'
    STOPPED = 'STOPPED'


@dataclass
class InstancePoolStats:
    idle_count: int = None
    pending_idle_count: int = None
    pending_used_count: int = None
    used_count: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.idle_count: body['idle_count'] = self.idle_count
        if self.pending_idle_count: body['pending_idle_count'] = self.pending_idle_count
        if self.pending_used_count: body['pending_used_count'] = self.pending_used_count
        if self.used_count: body['used_count'] = self.used_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolStats':
        return cls(idle_count=d.get('idle_count', None),
                   pending_idle_count=d.get('pending_idle_count', None),
                   pending_used_count=d.get('pending_used_count', None),
                   used_count=d.get('used_count', None))


@dataclass
class InstancePoolStatus:
    pending_instance_errors: 'List[PendingInstanceError]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.pending_instance_errors:
            body['pending_instance_errors'] = [v.as_dict() for v in self.pending_instance_errors]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolStatus':
        return cls(pending_instance_errors=_repeated(d, 'pending_instance_errors', PendingInstanceError))


@dataclass
class InstanceProfile:
    instance_profile_arn: str
    iam_role_arn: str = None
    is_meta_instance_profile: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.iam_role_arn: body['iam_role_arn'] = self.iam_role_arn
        if self.instance_profile_arn: body['instance_profile_arn'] = self.instance_profile_arn
        if self.is_meta_instance_profile: body['is_meta_instance_profile'] = self.is_meta_instance_profile
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstanceProfile':
        return cls(iam_role_arn=d.get('iam_role_arn', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   is_meta_instance_profile=d.get('is_meta_instance_profile', None))


class Language(Enum):

    python = 'python'
    scala = 'scala'
    sql = 'sql'


@dataclass
class Library:
    cran: 'RCranLibrary' = None
    egg: str = None
    jar: str = None
    maven: 'MavenLibrary' = None
    pypi: 'PythonPyPiLibrary' = None
    whl: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.cran: body['cran'] = self.cran.as_dict()
        if self.egg: body['egg'] = self.egg
        if self.jar: body['jar'] = self.jar
        if self.maven: body['maven'] = self.maven.as_dict()
        if self.pypi: body['pypi'] = self.pypi.as_dict()
        if self.whl: body['whl'] = self.whl
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Library':
        return cls(cran=_from_dict(d, 'cran', RCranLibrary),
                   egg=d.get('egg', None),
                   jar=d.get('jar', None),
                   maven=_from_dict(d, 'maven', MavenLibrary),
                   pypi=_from_dict(d, 'pypi', PythonPyPiLibrary),
                   whl=d.get('whl', None))


@dataclass
class LibraryFullStatus:
    is_library_for_all_clusters: bool = None
    library: 'Library' = None
    messages: 'List[str]' = None
    status: 'LibraryFullStatusStatus' = None

    def as_dict(self) -> dict:
        body = {}
        if self.is_library_for_all_clusters:
            body['is_library_for_all_clusters'] = self.is_library_for_all_clusters
        if self.library: body['library'] = self.library.as_dict()
        if self.messages: body['messages'] = [v for v in self.messages]
        if self.status: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LibraryFullStatus':
        return cls(is_library_for_all_clusters=d.get('is_library_for_all_clusters', None),
                   library=_from_dict(d, 'library', Library),
                   messages=d.get('messages', None),
                   status=_enum(d, 'status', LibraryFullStatusStatus))


class LibraryFullStatusStatus(Enum):
    """Status of installing the library on the cluster."""

    FAILED = 'FAILED'
    INSTALLED = 'INSTALLED'
    INSTALLING = 'INSTALLING'
    PENDING = 'PENDING'
    RESOLVING = 'RESOLVING'
    SKIPPED = 'SKIPPED'
    UNINSTALL_ON_RESTART = 'UNINSTALL_ON_RESTART'


@dataclass
class ListAllClusterLibraryStatusesResponse:
    statuses: 'List[ClusterLibraryStatuses]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.statuses: body['statuses'] = [v.as_dict() for v in self.statuses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListAllClusterLibraryStatusesResponse':
        return cls(statuses=_repeated(d, 'statuses', ClusterLibraryStatuses))


@dataclass
class ListAvailableZonesResponse:
    default_zone: str = None
    zones: 'List[str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.default_zone: body['default_zone'] = self.default_zone
        if self.zones: body['zones'] = [v for v in self.zones]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListAvailableZonesResponse':
        return cls(default_zone=d.get('default_zone', None), zones=d.get('zones', None))


@dataclass
class ListClusterPoliciesRequest:
    """Get a cluster policy"""

    sort_column: 'ListSortColumn' = None
    sort_order: 'ListSortOrder' = None


@dataclass
class ListClustersRequest:
    """List all clusters"""

    can_use_client: str = None


@dataclass
class ListClustersResponse:
    clusters: 'List[ClusterInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.clusters: body['clusters'] = [v.as_dict() for v in self.clusters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListClustersResponse':
        return cls(clusters=_repeated(d, 'clusters', ClusterInfo))


@dataclass
class ListGlobalInitScriptsResponse:
    scripts: 'List[GlobalInitScriptDetails]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.scripts: body['scripts'] = [v.as_dict() for v in self.scripts]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListGlobalInitScriptsResponse':
        return cls(scripts=_repeated(d, 'scripts', GlobalInitScriptDetails))


@dataclass
class ListInstancePools:
    instance_pools: 'List[InstancePoolAndStats]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.instance_pools: body['instance_pools'] = [v.as_dict() for v in self.instance_pools]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListInstancePools':
        return cls(instance_pools=_repeated(d, 'instance_pools', InstancePoolAndStats))


@dataclass
class ListInstanceProfilesResponse:
    instance_profiles: 'List[InstanceProfile]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.instance_profiles: body['instance_profiles'] = [v.as_dict() for v in self.instance_profiles]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListInstanceProfilesResponse':
        return cls(instance_profiles=_repeated(d, 'instance_profiles', InstanceProfile))


@dataclass
class ListNodeTypesResponse:
    node_types: 'List[NodeType]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.node_types: body['node_types'] = [v.as_dict() for v in self.node_types]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListNodeTypesResponse':
        return cls(node_types=_repeated(d, 'node_types', NodeType))


@dataclass
class ListPoliciesResponse:
    policies: 'List[Policy]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.policies: body['policies'] = [v.as_dict() for v in self.policies]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListPoliciesResponse':
        return cls(policies=_repeated(d, 'policies', Policy))


@dataclass
class ListPolicyFamiliesRequest:
    max_results: int = None
    page_token: str = None


@dataclass
class ListPolicyFamiliesResponse:
    policy_families: 'List[PolicyFamily]'
    next_page_token: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.policy_families: body['policy_families'] = [v.as_dict() for v in self.policy_families]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListPolicyFamiliesResponse':
        return cls(next_page_token=d.get('next_page_token', None),
                   policy_families=_repeated(d, 'policy_families', PolicyFamily))


class ListSortColumn(Enum):

    POLICY_CREATION_TIME = 'POLICY_CREATION_TIME'
    POLICY_NAME = 'POLICY_NAME'


class ListSortOrder(Enum):

    ASC = 'ASC'
    DESC = 'DESC'


@dataclass
class LogAnalyticsInfo:
    log_analytics_primary_key: str = None
    log_analytics_workspace_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.log_analytics_primary_key: body['log_analytics_primary_key'] = self.log_analytics_primary_key
        if self.log_analytics_workspace_id:
            body['log_analytics_workspace_id'] = self.log_analytics_workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogAnalyticsInfo':
        return cls(log_analytics_primary_key=d.get('log_analytics_primary_key', None),
                   log_analytics_workspace_id=d.get('log_analytics_workspace_id', None))


@dataclass
class LogSyncStatus:
    last_attempted: int = None
    last_exception: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.last_attempted: body['last_attempted'] = self.last_attempted
        if self.last_exception: body['last_exception'] = self.last_exception
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogSyncStatus':
        return cls(last_attempted=d.get('last_attempted', None), last_exception=d.get('last_exception', None))


@dataclass
class MavenLibrary:
    coordinates: str
    exclusions: 'List[str]' = None
    repo: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.coordinates: body['coordinates'] = self.coordinates
        if self.exclusions: body['exclusions'] = [v for v in self.exclusions]
        if self.repo: body['repo'] = self.repo
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'MavenLibrary':
        return cls(coordinates=d.get('coordinates', None),
                   exclusions=d.get('exclusions', None),
                   repo=d.get('repo', None))


@dataclass
class NodeInstanceType:
    instance_type_id: str = None
    local_disk_size_gb: int = None
    local_disks: int = None
    local_nvme_disk_size_gb: int = None
    local_nvme_disks: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.instance_type_id: body['instance_type_id'] = self.instance_type_id
        if self.local_disk_size_gb: body['local_disk_size_gb'] = self.local_disk_size_gb
        if self.local_disks: body['local_disks'] = self.local_disks
        if self.local_nvme_disk_size_gb: body['local_nvme_disk_size_gb'] = self.local_nvme_disk_size_gb
        if self.local_nvme_disks: body['local_nvme_disks'] = self.local_nvme_disks
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NodeInstanceType':
        return cls(instance_type_id=d.get('instance_type_id', None),
                   local_disk_size_gb=d.get('local_disk_size_gb', None),
                   local_disks=d.get('local_disks', None),
                   local_nvme_disk_size_gb=d.get('local_nvme_disk_size_gb', None),
                   local_nvme_disks=d.get('local_nvme_disks', None))


@dataclass
class NodeType:
    node_type_id: str
    memory_mb: int
    num_cores: float
    description: str
    instance_type_id: str
    category: str = None
    display_order: int = None
    is_deprecated: bool = None
    is_encrypted_in_transit: bool = None
    is_graviton: bool = None
    is_hidden: bool = None
    is_io_cache_enabled: bool = None
    node_info: 'CloudProviderNodeInfo' = None
    node_instance_type: 'NodeInstanceType' = None
    num_gpus: int = None
    photon_driver_capable: bool = None
    photon_worker_capable: bool = None
    support_cluster_tags: bool = None
    support_ebs_volumes: bool = None
    support_port_forwarding: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.category: body['category'] = self.category
        if self.description: body['description'] = self.description
        if self.display_order: body['display_order'] = self.display_order
        if self.instance_type_id: body['instance_type_id'] = self.instance_type_id
        if self.is_deprecated: body['is_deprecated'] = self.is_deprecated
        if self.is_encrypted_in_transit: body['is_encrypted_in_transit'] = self.is_encrypted_in_transit
        if self.is_graviton: body['is_graviton'] = self.is_graviton
        if self.is_hidden: body['is_hidden'] = self.is_hidden
        if self.is_io_cache_enabled: body['is_io_cache_enabled'] = self.is_io_cache_enabled
        if self.memory_mb: body['memory_mb'] = self.memory_mb
        if self.node_info: body['node_info'] = self.node_info.as_dict()
        if self.node_instance_type: body['node_instance_type'] = self.node_instance_type.as_dict()
        if self.node_type_id: body['node_type_id'] = self.node_type_id
        if self.num_cores: body['num_cores'] = self.num_cores
        if self.num_gpus: body['num_gpus'] = self.num_gpus
        if self.photon_driver_capable: body['photon_driver_capable'] = self.photon_driver_capable
        if self.photon_worker_capable: body['photon_worker_capable'] = self.photon_worker_capable
        if self.support_cluster_tags: body['support_cluster_tags'] = self.support_cluster_tags
        if self.support_ebs_volumes: body['support_ebs_volumes'] = self.support_ebs_volumes
        if self.support_port_forwarding: body['support_port_forwarding'] = self.support_port_forwarding
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NodeType':
        return cls(category=d.get('category', None),
                   description=d.get('description', None),
                   display_order=d.get('display_order', None),
                   instance_type_id=d.get('instance_type_id', None),
                   is_deprecated=d.get('is_deprecated', None),
                   is_encrypted_in_transit=d.get('is_encrypted_in_transit', None),
                   is_graviton=d.get('is_graviton', None),
                   is_hidden=d.get('is_hidden', None),
                   is_io_cache_enabled=d.get('is_io_cache_enabled', None),
                   memory_mb=d.get('memory_mb', None),
                   node_info=_from_dict(d, 'node_info', CloudProviderNodeInfo),
                   node_instance_type=_from_dict(d, 'node_instance_type', NodeInstanceType),
                   node_type_id=d.get('node_type_id', None),
                   num_cores=d.get('num_cores', None),
                   num_gpus=d.get('num_gpus', None),
                   photon_driver_capable=d.get('photon_driver_capable', None),
                   photon_worker_capable=d.get('photon_worker_capable', None),
                   support_cluster_tags=d.get('support_cluster_tags', None),
                   support_ebs_volumes=d.get('support_ebs_volumes', None),
                   support_port_forwarding=d.get('support_port_forwarding', None))


@dataclass
class PendingInstanceError:
    instance_id: str = None
    message: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.instance_id: body['instance_id'] = self.instance_id
        if self.message: body['message'] = self.message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PendingInstanceError':
        return cls(instance_id=d.get('instance_id', None), message=d.get('message', None))


@dataclass
class PermanentDeleteCluster:
    cluster_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermanentDeleteCluster':
        return cls(cluster_id=d.get('cluster_id', None))


@dataclass
class PinCluster:
    cluster_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PinCluster':
        return cls(cluster_id=d.get('cluster_id', None))


@dataclass
class Policy:
    created_at_timestamp: int = None
    creator_user_name: str = None
    definition: str = None
    description: str = None
    is_default: bool = None
    max_clusters_per_user: int = None
    name: str = None
    policy_family_definition_overrides: str = None
    policy_family_id: str = None
    policy_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at_timestamp: body['created_at_timestamp'] = self.created_at_timestamp
        if self.creator_user_name: body['creator_user_name'] = self.creator_user_name
        if self.definition: body['definition'] = self.definition
        if self.description: body['description'] = self.description
        if self.is_default: body['is_default'] = self.is_default
        if self.max_clusters_per_user: body['max_clusters_per_user'] = self.max_clusters_per_user
        if self.name: body['name'] = self.name
        if self.policy_family_definition_overrides:
            body['policy_family_definition_overrides'] = self.policy_family_definition_overrides
        if self.policy_family_id: body['policy_family_id'] = self.policy_family_id
        if self.policy_id: body['policy_id'] = self.policy_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Policy':
        return cls(created_at_timestamp=d.get('created_at_timestamp', None),
                   creator_user_name=d.get('creator_user_name', None),
                   definition=d.get('definition', None),
                   description=d.get('description', None),
                   is_default=d.get('is_default', None),
                   max_clusters_per_user=d.get('max_clusters_per_user', None),
                   name=d.get('name', None),
                   policy_family_definition_overrides=d.get('policy_family_definition_overrides', None),
                   policy_family_id=d.get('policy_family_id', None),
                   policy_id=d.get('policy_id', None))


@dataclass
class PolicyFamily:
    policy_family_id: str
    name: str
    description: str
    definition: str

    def as_dict(self) -> dict:
        body = {}
        if self.definition: body['definition'] = self.definition
        if self.description: body['description'] = self.description
        if self.name: body['name'] = self.name
        if self.policy_family_id: body['policy_family_id'] = self.policy_family_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PolicyFamily':
        return cls(definition=d.get('definition', None),
                   description=d.get('description', None),
                   name=d.get('name', None),
                   policy_family_id=d.get('policy_family_id', None))


@dataclass
class PythonPyPiLibrary:
    package: str
    repo: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.package: body['package'] = self.package
        if self.repo: body['repo'] = self.repo
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PythonPyPiLibrary':
        return cls(package=d.get('package', None), repo=d.get('repo', None))


@dataclass
class RCranLibrary:
    package: str
    repo: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.package: body['package'] = self.package
        if self.repo: body['repo'] = self.repo
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RCranLibrary':
        return cls(package=d.get('package', None), repo=d.get('repo', None))


@dataclass
class RemoveInstanceProfile:
    instance_profile_arn: str

    def as_dict(self) -> dict:
        body = {}
        if self.instance_profile_arn: body['instance_profile_arn'] = self.instance_profile_arn
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RemoveInstanceProfile':
        return cls(instance_profile_arn=d.get('instance_profile_arn', None))


@dataclass
class ResizeCluster:
    cluster_id: str
    autoscale: 'AutoScale' = None
    num_workers: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.autoscale: body['autoscale'] = self.autoscale.as_dict()
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.num_workers: body['num_workers'] = self.num_workers
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResizeCluster':
        return cls(autoscale=_from_dict(d, 'autoscale', AutoScale),
                   cluster_id=d.get('cluster_id', None),
                   num_workers=d.get('num_workers', None))


@dataclass
class RestartCluster:
    cluster_id: str
    restart_user: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.restart_user: body['restart_user'] = self.restart_user
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RestartCluster':
        return cls(cluster_id=d.get('cluster_id', None), restart_user=d.get('restart_user', None))


class ResultType(Enum):

    error = 'error'
    image = 'image'
    images = 'images'
    table = 'table'
    text = 'text'


@dataclass
class Results:
    cause: str = None
    data: Any = None
    file_name: str = None
    file_names: 'List[str]' = None
    is_json_schema: bool = None
    pos: int = None
    result_type: 'ResultType' = None
    schema: 'List[Dict[str,Any]]' = None
    summary: str = None
    truncated: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.cause: body['cause'] = self.cause
        if self.data: body['data'] = self.data
        if self.file_name: body['fileName'] = self.file_name
        if self.file_names: body['fileNames'] = [v for v in self.file_names]
        if self.is_json_schema: body['isJsonSchema'] = self.is_json_schema
        if self.pos: body['pos'] = self.pos
        if self.result_type: body['resultType'] = self.result_type.value
        if self.schema: body['schema'] = [v for v in self.schema]
        if self.summary: body['summary'] = self.summary
        if self.truncated: body['truncated'] = self.truncated
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Results':
        return cls(cause=d.get('cause', None),
                   data=d.get('data', None),
                   file_name=d.get('fileName', None),
                   file_names=d.get('fileNames', None),
                   is_json_schema=d.get('isJsonSchema', None),
                   pos=d.get('pos', None),
                   result_type=_enum(d, 'resultType', ResultType),
                   schema=d.get('schema', None),
                   summary=d.get('summary', None),
                   truncated=d.get('truncated', None))


class RuntimeEngine(Enum):
    """Decides which runtime engine to be use, e.g. Standard vs. Photon. If unspecified, the runtime
    engine is inferred from spark_version."""

    NULL = 'NULL'
    PHOTON = 'PHOTON'
    STANDARD = 'STANDARD'


@dataclass
class S3StorageInfo:
    canned_acl: str = None
    destination: str = None
    enable_encryption: bool = None
    encryption_type: str = None
    endpoint: str = None
    kms_key: str = None
    region: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.canned_acl: body['canned_acl'] = self.canned_acl
        if self.destination: body['destination'] = self.destination
        if self.enable_encryption: body['enable_encryption'] = self.enable_encryption
        if self.encryption_type: body['encryption_type'] = self.encryption_type
        if self.endpoint: body['endpoint'] = self.endpoint
        if self.kms_key: body['kms_key'] = self.kms_key
        if self.region: body['region'] = self.region
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'S3StorageInfo':
        return cls(canned_acl=d.get('canned_acl', None),
                   destination=d.get('destination', None),
                   enable_encryption=d.get('enable_encryption', None),
                   encryption_type=d.get('encryption_type', None),
                   endpoint=d.get('endpoint', None),
                   kms_key=d.get('kms_key', None),
                   region=d.get('region', None))


@dataclass
class SparkNode:
    host_private_ip: str = None
    instance_id: str = None
    node_aws_attributes: 'SparkNodeAwsAttributes' = None
    node_id: str = None
    private_ip: str = None
    public_dns: str = None
    start_timestamp: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.host_private_ip: body['host_private_ip'] = self.host_private_ip
        if self.instance_id: body['instance_id'] = self.instance_id
        if self.node_aws_attributes: body['node_aws_attributes'] = self.node_aws_attributes.as_dict()
        if self.node_id: body['node_id'] = self.node_id
        if self.private_ip: body['private_ip'] = self.private_ip
        if self.public_dns: body['public_dns'] = self.public_dns
        if self.start_timestamp: body['start_timestamp'] = self.start_timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkNode':
        return cls(host_private_ip=d.get('host_private_ip', None),
                   instance_id=d.get('instance_id', None),
                   node_aws_attributes=_from_dict(d, 'node_aws_attributes', SparkNodeAwsAttributes),
                   node_id=d.get('node_id', None),
                   private_ip=d.get('private_ip', None),
                   public_dns=d.get('public_dns', None),
                   start_timestamp=d.get('start_timestamp', None))


@dataclass
class SparkNodeAwsAttributes:
    is_spot: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.is_spot: body['is_spot'] = self.is_spot
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkNodeAwsAttributes':
        return cls(is_spot=d.get('is_spot', None))


@dataclass
class SparkVersion:
    key: str = None
    name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.name: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkVersion':
        return cls(key=d.get('key', None), name=d.get('name', None))


@dataclass
class StartCluster:
    cluster_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StartCluster':
        return cls(cluster_id=d.get('cluster_id', None))


class State(Enum):
    """Current state of the cluster."""

    ERROR = 'ERROR'
    PENDING = 'PENDING'
    RESIZING = 'RESIZING'
    RESTARTING = 'RESTARTING'
    RUNNING = 'RUNNING'
    TERMINATED = 'TERMINATED'
    TERMINATING = 'TERMINATING'
    UNKNOWN = 'UNKNOWN'


@dataclass
class TerminationReason:
    code: 'TerminationReasonCode' = None
    parameters: 'Dict[str,str]' = None
    type: 'TerminationReasonType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.code: body['code'] = self.code.value
        if self.parameters: body['parameters'] = self.parameters
        if self.type: body['type'] = self.type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TerminationReason':
        return cls(code=_enum(d, 'code', TerminationReasonCode),
                   parameters=d.get('parameters', None),
                   type=_enum(d, 'type', TerminationReasonType))


class TerminationReasonCode(Enum):
    """status code indicating why the cluster was terminated"""

    ABUSE_DETECTED = 'ABUSE_DETECTED'
    ATTACH_PROJECT_FAILURE = 'ATTACH_PROJECT_FAILURE'
    AWS_AUTHORIZATION_FAILURE = 'AWS_AUTHORIZATION_FAILURE'
    AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE = 'AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE'
    AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE = 'AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE'
    AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE = 'AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE'
    AWS_REQUEST_LIMIT_EXCEEDED = 'AWS_REQUEST_LIMIT_EXCEEDED'
    AWS_UNSUPPORTED_FAILURE = 'AWS_UNSUPPORTED_FAILURE'
    AZURE_BYOK_KEY_PERMISSION_FAILURE = 'AZURE_BYOK_KEY_PERMISSION_FAILURE'
    AZURE_EPHEMERAL_DISK_FAILURE = 'AZURE_EPHEMERAL_DISK_FAILURE'
    AZURE_INVALID_DEPLOYMENT_TEMPLATE = 'AZURE_INVALID_DEPLOYMENT_TEMPLATE'
    AZURE_OPERATION_NOT_ALLOWED_EXCEPTION = 'AZURE_OPERATION_NOT_ALLOWED_EXCEPTION'
    AZURE_QUOTA_EXCEEDED_EXCEPTION = 'AZURE_QUOTA_EXCEEDED_EXCEPTION'
    AZURE_RESOURCE_MANAGER_THROTTLING = 'AZURE_RESOURCE_MANAGER_THROTTLING'
    AZURE_RESOURCE_PROVIDER_THROTTLING = 'AZURE_RESOURCE_PROVIDER_THROTTLING'
    AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE = 'AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE'
    AZURE_VM_EXTENSION_FAILURE = 'AZURE_VM_EXTENSION_FAILURE'
    AZURE_VNET_CONFIGURATION_FAILURE = 'AZURE_VNET_CONFIGURATION_FAILURE'
    BOOTSTRAP_TIMEOUT = 'BOOTSTRAP_TIMEOUT'
    BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION = 'BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION'
    CLOUD_PROVIDER_DISK_SETUP_FAILURE = 'CLOUD_PROVIDER_DISK_SETUP_FAILURE'
    CLOUD_PROVIDER_LAUNCH_FAILURE = 'CLOUD_PROVIDER_LAUNCH_FAILURE'
    CLOUD_PROVIDER_RESOURCE_STOCKOUT = 'CLOUD_PROVIDER_RESOURCE_STOCKOUT'
    CLOUD_PROVIDER_SHUTDOWN = 'CLOUD_PROVIDER_SHUTDOWN'
    COMMUNICATION_LOST = 'COMMUNICATION_LOST'
    CONTAINER_LAUNCH_FAILURE = 'CONTAINER_LAUNCH_FAILURE'
    CONTROL_PLANE_REQUEST_FAILURE = 'CONTROL_PLANE_REQUEST_FAILURE'
    DATABASE_CONNECTION_FAILURE = 'DATABASE_CONNECTION_FAILURE'
    DBFS_COMPONENT_UNHEALTHY = 'DBFS_COMPONENT_UNHEALTHY'
    DOCKER_IMAGE_PULL_FAILURE = 'DOCKER_IMAGE_PULL_FAILURE'
    DRIVER_UNREACHABLE = 'DRIVER_UNREACHABLE'
    DRIVER_UNRESPONSIVE = 'DRIVER_UNRESPONSIVE'
    EXECUTION_COMPONENT_UNHEALTHY = 'EXECUTION_COMPONENT_UNHEALTHY'
    GCP_QUOTA_EXCEEDED = 'GCP_QUOTA_EXCEEDED'
    GCP_SERVICE_ACCOUNT_DELETED = 'GCP_SERVICE_ACCOUNT_DELETED'
    GLOBAL_INIT_SCRIPT_FAILURE = 'GLOBAL_INIT_SCRIPT_FAILURE'
    HIVE_METASTORE_PROVISIONING_FAILURE = 'HIVE_METASTORE_PROVISIONING_FAILURE'
    IMAGE_PULL_PERMISSION_DENIED = 'IMAGE_PULL_PERMISSION_DENIED'
    INACTIVITY = 'INACTIVITY'
    INIT_SCRIPT_FAILURE = 'INIT_SCRIPT_FAILURE'
    INSTANCE_POOL_CLUSTER_FAILURE = 'INSTANCE_POOL_CLUSTER_FAILURE'
    INSTANCE_UNREACHABLE = 'INSTANCE_UNREACHABLE'
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    INVALID_ARGUMENT = 'INVALID_ARGUMENT'
    INVALID_SPARK_IMAGE = 'INVALID_SPARK_IMAGE'
    IP_EXHAUSTION_FAILURE = 'IP_EXHAUSTION_FAILURE'
    JOB_FINISHED = 'JOB_FINISHED'
    K8S_AUTOSCALING_FAILURE = 'K8S_AUTOSCALING_FAILURE'
    K8S_DBR_CLUSTER_LAUNCH_TIMEOUT = 'K8S_DBR_CLUSTER_LAUNCH_TIMEOUT'
    METASTORE_COMPONENT_UNHEALTHY = 'METASTORE_COMPONENT_UNHEALTHY'
    NEPHOS_RESOURCE_MANAGEMENT = 'NEPHOS_RESOURCE_MANAGEMENT'
    NETWORK_CONFIGURATION_FAILURE = 'NETWORK_CONFIGURATION_FAILURE'
    NFS_MOUNT_FAILURE = 'NFS_MOUNT_FAILURE'
    NPIP_TUNNEL_SETUP_FAILURE = 'NPIP_TUNNEL_SETUP_FAILURE'
    NPIP_TUNNEL_TOKEN_FAILURE = 'NPIP_TUNNEL_TOKEN_FAILURE'
    REQUEST_REJECTED = 'REQUEST_REJECTED'
    REQUEST_THROTTLED = 'REQUEST_THROTTLED'
    SECRET_RESOLUTION_ERROR = 'SECRET_RESOLUTION_ERROR'
    SECURITY_DAEMON_REGISTRATION_EXCEPTION = 'SECURITY_DAEMON_REGISTRATION_EXCEPTION'
    SELF_BOOTSTRAP_FAILURE = 'SELF_BOOTSTRAP_FAILURE'
    SKIPPED_SLOW_NODES = 'SKIPPED_SLOW_NODES'
    SLOW_IMAGE_DOWNLOAD = 'SLOW_IMAGE_DOWNLOAD'
    SPARK_ERROR = 'SPARK_ERROR'
    SPARK_IMAGE_DOWNLOAD_FAILURE = 'SPARK_IMAGE_DOWNLOAD_FAILURE'
    SPARK_STARTUP_FAILURE = 'SPARK_STARTUP_FAILURE'
    SPOT_INSTANCE_TERMINATION = 'SPOT_INSTANCE_TERMINATION'
    STORAGE_DOWNLOAD_FAILURE = 'STORAGE_DOWNLOAD_FAILURE'
    STS_CLIENT_SETUP_FAILURE = 'STS_CLIENT_SETUP_FAILURE'
    SUBNET_EXHAUSTED_FAILURE = 'SUBNET_EXHAUSTED_FAILURE'
    TEMPORARILY_UNAVAILABLE = 'TEMPORARILY_UNAVAILABLE'
    TRIAL_EXPIRED = 'TRIAL_EXPIRED'
    UNEXPECTED_LAUNCH_FAILURE = 'UNEXPECTED_LAUNCH_FAILURE'
    UNKNOWN = 'UNKNOWN'
    UNSUPPORTED_INSTANCE_TYPE = 'UNSUPPORTED_INSTANCE_TYPE'
    UPDATE_INSTANCE_PROFILE_FAILURE = 'UPDATE_INSTANCE_PROFILE_FAILURE'
    USER_REQUEST = 'USER_REQUEST'
    WORKER_SETUP_FAILURE = 'WORKER_SETUP_FAILURE'
    WORKSPACE_CANCELLED_ERROR = 'WORKSPACE_CANCELLED_ERROR'
    WORKSPACE_CONFIGURATION_ERROR = 'WORKSPACE_CONFIGURATION_ERROR'


class TerminationReasonType(Enum):
    """type of the termination"""

    CLIENT_ERROR = 'CLIENT_ERROR'
    CLOUD_FAILURE = 'CLOUD_FAILURE'
    SERVICE_FAULT = 'SERVICE_FAULT'
    SUCCESS = 'SUCCESS'


@dataclass
class UninstallLibraries:
    cluster_id: str
    libraries: 'List[Library]'

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UninstallLibraries':
        return cls(cluster_id=d.get('cluster_id', None), libraries=_repeated(d, 'libraries', Library))


@dataclass
class UnpinCluster:
    cluster_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UnpinCluster':
        return cls(cluster_id=d.get('cluster_id', None))


@dataclass
class WorkloadType:
    clients: 'ClientsTypes' = None

    def as_dict(self) -> dict:
        body = {}
        if self.clients: body['clients'] = self.clients.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WorkloadType':
        return cls(clients=_from_dict(d, 'clients', ClientsTypes))


class ClusterPoliciesAPI:
    """Cluster policy limits the ability to configure clusters based on a set of rules. The policy rules limit
    the attributes or attribute values available for cluster creation. Cluster policies have ACLs that limit
    their use to specific users and groups.
    
    Cluster policies let you limit users to create clusters with prescribed settings, simplify the user
    interface and enable more users to create their own clusters (by fixing and hiding some values), control
    cost by limiting per cluster maximum cost (by setting limits on attributes whose values contribute to
    hourly price).
    
    Cluster policy permissions limit which policies a user can select in the Policy drop-down when the user
    creates a cluster: - A user who has cluster create permission can select the Unrestricted policy and
    create fully-configurable clusters. - A user who has both cluster create permission and access to cluster
    policies can select the Unrestricted policy and policies they have access to. - A user that has access to
    only cluster policies, can select the policies they have access to.
    
    If no policies have been created in the workspace, the Policy drop-down does not display.
    
    Only admin users can create, edit, and delete policies. Admin users also have access to all policies."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               *,
               definition: str = None,
               description: str = None,
               max_clusters_per_user: int = None,
               policy_family_definition_overrides: str = None,
               policy_family_id: str = None,
               **kwargs) -> CreatePolicyResponse:
        """Create a new policy.
        
        Creates a new policy with prescribed settings."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreatePolicy(definition=definition,
                                   description=description,
                                   max_clusters_per_user=max_clusters_per_user,
                                   name=name,
                                   policy_family_definition_overrides=policy_family_definition_overrides,
                                   policy_family_id=policy_family_id)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/policies/clusters/create', body=body)
        return CreatePolicyResponse.from_dict(json)

    def delete(self, policy_id: str, **kwargs):
        """Delete a cluster policy.
        
        Delete a policy for a cluster. Clusters governed by this policy can still run, but cannot be edited."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeletePolicy(policy_id=policy_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/policies/clusters/delete', body=body)

    def edit(self,
             policy_id: str,
             name: str,
             *,
             definition: str = None,
             description: str = None,
             max_clusters_per_user: int = None,
             policy_family_definition_overrides: str = None,
             policy_family_id: str = None,
             **kwargs):
        """Update a cluster policy.
        
        Update an existing policy for cluster. This operation may make some clusters governed by the previous
        policy invalid."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = EditPolicy(definition=definition,
                                 description=description,
                                 max_clusters_per_user=max_clusters_per_user,
                                 name=name,
                                 policy_family_definition_overrides=policy_family_definition_overrides,
                                 policy_family_id=policy_family_id,
                                 policy_id=policy_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/policies/clusters/edit', body=body)

    def get(self, policy_id: str, **kwargs) -> Policy:
        """Get entity.
        
        Get a cluster policy entity. Creation and editing is available to admins only."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetClusterPolicyRequest(policy_id=policy_id)

        query = {}
        if policy_id: query['policy_id'] = request.policy_id

        json = self._api.do('GET', '/api/2.0/policies/clusters/get', query=query)
        return Policy.from_dict(json)

    def list(self,
             *,
             sort_column: ListSortColumn = None,
             sort_order: ListSortOrder = None,
             **kwargs) -> Iterator[Policy]:
        """Get a cluster policy.
        
        Returns a list of policies accessible by the requesting user."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListClusterPoliciesRequest(sort_column=sort_column, sort_order=sort_order)

        query = {}
        if sort_column: query['sort_column'] = request.sort_column.value
        if sort_order: query['sort_order'] = request.sort_order.value

        json = self._api.do('GET', '/api/2.0/policies/clusters/list', query=query)
        return [Policy.from_dict(v) for v in json.get('policies', [])]


class ClustersAPI:
    """The Clusters API allows you to create, start, edit, list, terminate, and delete clusters.
    
    Databricks maps cluster node instance types to compute units known as DBUs. See the instance type pricing
    page for a list of the supported instance types and their corresponding DBUs.
    
    A Databricks cluster is a set of computation resources and configurations on which you run data
    engineering, data science, and data analytics workloads, such as production ETL pipelines, streaming
    analytics, ad-hoc analytics, and machine learning.
    
    You run these workloads as a set of commands in a notebook or as an automated job. Databricks makes a
    distinction between all-purpose clusters and job clusters. You use all-purpose clusters to analyze data
    collaboratively using interactive notebooks. You use job clusters to run fast and robust automated jobs.
    
    You can create an all-purpose cluster using the UI, CLI, or REST API. You can manually terminate and
    restart an all-purpose cluster. Multiple users can share such clusters to do collaborative interactive
    analysis.
    
    IMPORTANT: Databricks retains cluster configuration information for up to 200 all-purpose clusters
    terminated in the last 30 days and up to 30 job clusters recently terminated by the job scheduler. To keep
    an all-purpose cluster configuration even after it has been terminated for more than 30 days, an
    administrator can pin a cluster to the cluster list."""

    def __init__(self, api_client):
        self._api = api_client

    def wait_get_cluster_running(self,
                                 cluster_id: str,
                                 timeout=timedelta(minutes=20),
                                 callback: Callable[[ClusterInfo], None] = None) -> ClusterInfo:
        deadline = time.time() + timeout.total_seconds()
        target_states = (State.RUNNING, )
        failure_states = (State.ERROR, State.TERMINATED, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get(cluster_id=cluster_id)
            status = poll.state
            status_message = poll.state_message
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach RUNNING, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"cluster_id={cluster_id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def wait_get_cluster_terminated(self,
                                    cluster_id: str,
                                    timeout=timedelta(minutes=20),
                                    callback: Callable[[ClusterInfo], None] = None) -> ClusterInfo:
        deadline = time.time() + timeout.total_seconds()
        target_states = (State.TERMINATED, )
        failure_states = (State.ERROR, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get(cluster_id=cluster_id)
            status = poll.state
            status_message = poll.state_message
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach TERMINATED, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"cluster_id={cluster_id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def change_owner(self, cluster_id: str, owner_username: str, **kwargs):
        """Change cluster owner.
        
        Change the owner of the cluster. You must be an admin to perform this operation."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ChangeClusterOwner(cluster_id=cluster_id, owner_username=owner_username)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/clusters/change-owner', body=body)

    def create(self,
               spark_version: str,
               *,
               apply_policy_default_values: bool = None,
               autoscale: AutoScale = None,
               autotermination_minutes: int = None,
               aws_attributes: AwsAttributes = None,
               azure_attributes: AzureAttributes = None,
               cluster_log_conf: ClusterLogConf = None,
               cluster_name: str = None,
               cluster_source: ClusterSource = None,
               custom_tags: Dict[str, str] = None,
               driver_instance_pool_id: str = None,
               driver_node_type_id: str = None,
               enable_elastic_disk: bool = None,
               enable_local_disk_encryption: bool = None,
               gcp_attributes: GcpAttributes = None,
               instance_pool_id: str = None,
               node_type_id: str = None,
               num_workers: int = None,
               policy_id: str = None,
               runtime_engine: RuntimeEngine = None,
               spark_conf: Dict[str, str] = None,
               spark_env_vars: Dict[str, str] = None,
               ssh_public_keys: List[str] = None,
               workload_type: WorkloadType = None,
               **kwargs) -> Wait[ClusterInfo]:
        """Create new cluster.
        
        Creates a new Spark cluster. This method will acquire new instances from the cloud provider if
        necessary. This method is asynchronous; the returned `cluster_id` can be used to poll the cluster
        status. When this method returns, the cluster will be in a `PENDING` state. The cluster will be usable
        once it enters a `RUNNING` state.
        
        Note: Databricks may not be able to acquire some of the requested nodes, due to cloud provider
        limitations (account limits, spot price, etc.) or transient network issues.
        
        If Databricks acquires at least 85% of the requested on-demand nodes, cluster creation will succeed.
        Otherwise the cluster will terminate with an informative error message."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateCluster(apply_policy_default_values=apply_policy_default_values,
                                    autoscale=autoscale,
                                    autotermination_minutes=autotermination_minutes,
                                    aws_attributes=aws_attributes,
                                    azure_attributes=azure_attributes,
                                    cluster_log_conf=cluster_log_conf,
                                    cluster_name=cluster_name,
                                    cluster_source=cluster_source,
                                    custom_tags=custom_tags,
                                    driver_instance_pool_id=driver_instance_pool_id,
                                    driver_node_type_id=driver_node_type_id,
                                    enable_elastic_disk=enable_elastic_disk,
                                    enable_local_disk_encryption=enable_local_disk_encryption,
                                    gcp_attributes=gcp_attributes,
                                    instance_pool_id=instance_pool_id,
                                    node_type_id=node_type_id,
                                    num_workers=num_workers,
                                    policy_id=policy_id,
                                    runtime_engine=runtime_engine,
                                    spark_conf=spark_conf,
                                    spark_env_vars=spark_env_vars,
                                    spark_version=spark_version,
                                    ssh_public_keys=ssh_public_keys,
                                    workload_type=workload_type)
        body = request.as_dict()
        op_response = self._api.do('POST', '/api/2.0/clusters/create', body=body)
        return Wait(self.wait_get_cluster_running,
                    response=CreateClusterResponse.from_dict(op_response),
                    cluster_id=op_response['cluster_id'])

    def create_and_wait(self,
                        spark_version: str,
                        *,
                        apply_policy_default_values: bool = None,
                        autoscale: AutoScale = None,
                        autotermination_minutes: int = None,
                        aws_attributes: AwsAttributes = None,
                        azure_attributes: AzureAttributes = None,
                        cluster_log_conf: ClusterLogConf = None,
                        cluster_name: str = None,
                        cluster_source: ClusterSource = None,
                        custom_tags: Dict[str, str] = None,
                        driver_instance_pool_id: str = None,
                        driver_node_type_id: str = None,
                        enable_elastic_disk: bool = None,
                        enable_local_disk_encryption: bool = None,
                        gcp_attributes: GcpAttributes = None,
                        instance_pool_id: str = None,
                        node_type_id: str = None,
                        num_workers: int = None,
                        policy_id: str = None,
                        runtime_engine: RuntimeEngine = None,
                        spark_conf: Dict[str, str] = None,
                        spark_env_vars: Dict[str, str] = None,
                        ssh_public_keys: List[str] = None,
                        workload_type: WorkloadType = None,
                        timeout=timedelta(minutes=20)) -> ClusterInfo:
        return self.create(apply_policy_default_values=apply_policy_default_values,
                           autoscale=autoscale,
                           autotermination_minutes=autotermination_minutes,
                           aws_attributes=aws_attributes,
                           azure_attributes=azure_attributes,
                           cluster_log_conf=cluster_log_conf,
                           cluster_name=cluster_name,
                           cluster_source=cluster_source,
                           custom_tags=custom_tags,
                           driver_instance_pool_id=driver_instance_pool_id,
                           driver_node_type_id=driver_node_type_id,
                           enable_elastic_disk=enable_elastic_disk,
                           enable_local_disk_encryption=enable_local_disk_encryption,
                           gcp_attributes=gcp_attributes,
                           instance_pool_id=instance_pool_id,
                           node_type_id=node_type_id,
                           num_workers=num_workers,
                           policy_id=policy_id,
                           runtime_engine=runtime_engine,
                           spark_conf=spark_conf,
                           spark_env_vars=spark_env_vars,
                           spark_version=spark_version,
                           ssh_public_keys=ssh_public_keys,
                           workload_type=workload_type).result(timeout=timeout)

    def delete(self, cluster_id: str, **kwargs) -> Wait[ClusterInfo]:
        """Terminate cluster.
        
        Terminates the Spark cluster with the specified ID. The cluster is removed asynchronously. Once the
        termination has completed, the cluster will be in a `TERMINATED` state. If the cluster is already in a
        `TERMINATING` or `TERMINATED` state, nothing will happen."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteCluster(cluster_id=cluster_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/clusters/delete', body=body)
        return Wait(self.wait_get_cluster_terminated, cluster_id=request.cluster_id)

    def delete_and_wait(self, cluster_id: str, timeout=timedelta(minutes=20)) -> ClusterInfo:
        return self.delete(cluster_id=cluster_id).result(timeout=timeout)

    def edit(self,
             cluster_id: str,
             spark_version: str,
             *,
             apply_policy_default_values: bool = None,
             autoscale: AutoScale = None,
             autotermination_minutes: int = None,
             aws_attributes: AwsAttributes = None,
             azure_attributes: AzureAttributes = None,
             cluster_log_conf: ClusterLogConf = None,
             cluster_name: str = None,
             cluster_source: ClusterSource = None,
             custom_tags: Dict[str, str] = None,
             driver_instance_pool_id: str = None,
             driver_node_type_id: str = None,
             enable_elastic_disk: bool = None,
             enable_local_disk_encryption: bool = None,
             gcp_attributes: GcpAttributes = None,
             instance_pool_id: str = None,
             node_type_id: str = None,
             num_workers: int = None,
             policy_id: str = None,
             runtime_engine: RuntimeEngine = None,
             spark_conf: Dict[str, str] = None,
             spark_env_vars: Dict[str, str] = None,
             ssh_public_keys: List[str] = None,
             workload_type: WorkloadType = None,
             **kwargs) -> Wait[ClusterInfo]:
        """Update cluster configuration.
        
        Updates the configuration of a cluster to match the provided attributes and size. A cluster can be
        updated if it is in a `RUNNING` or `TERMINATED` state.
        
        If a cluster is updated while in a `RUNNING` state, it will be restarted so that the new attributes
        can take effect.
        
        If a cluster is updated while in a `TERMINATED` state, it will remain `TERMINATED`. The next time it
        is started using the `clusters/start` API, the new attributes will take effect. Any attempt to update
        a cluster in any other state will be rejected with an `INVALID_STATE` error code.
        
        Clusters created by the Databricks Jobs service cannot be edited."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = EditCluster(apply_policy_default_values=apply_policy_default_values,
                                  autoscale=autoscale,
                                  autotermination_minutes=autotermination_minutes,
                                  aws_attributes=aws_attributes,
                                  azure_attributes=azure_attributes,
                                  cluster_id=cluster_id,
                                  cluster_log_conf=cluster_log_conf,
                                  cluster_name=cluster_name,
                                  cluster_source=cluster_source,
                                  custom_tags=custom_tags,
                                  driver_instance_pool_id=driver_instance_pool_id,
                                  driver_node_type_id=driver_node_type_id,
                                  enable_elastic_disk=enable_elastic_disk,
                                  enable_local_disk_encryption=enable_local_disk_encryption,
                                  gcp_attributes=gcp_attributes,
                                  instance_pool_id=instance_pool_id,
                                  node_type_id=node_type_id,
                                  num_workers=num_workers,
                                  policy_id=policy_id,
                                  runtime_engine=runtime_engine,
                                  spark_conf=spark_conf,
                                  spark_env_vars=spark_env_vars,
                                  spark_version=spark_version,
                                  ssh_public_keys=ssh_public_keys,
                                  workload_type=workload_type)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/clusters/edit', body=body)
        return Wait(self.wait_get_cluster_running, cluster_id=request.cluster_id)

    def edit_and_wait(self,
                      cluster_id: str,
                      spark_version: str,
                      *,
                      apply_policy_default_values: bool = None,
                      autoscale: AutoScale = None,
                      autotermination_minutes: int = None,
                      aws_attributes: AwsAttributes = None,
                      azure_attributes: AzureAttributes = None,
                      cluster_log_conf: ClusterLogConf = None,
                      cluster_name: str = None,
                      cluster_source: ClusterSource = None,
                      custom_tags: Dict[str, str] = None,
                      driver_instance_pool_id: str = None,
                      driver_node_type_id: str = None,
                      enable_elastic_disk: bool = None,
                      enable_local_disk_encryption: bool = None,
                      gcp_attributes: GcpAttributes = None,
                      instance_pool_id: str = None,
                      node_type_id: str = None,
                      num_workers: int = None,
                      policy_id: str = None,
                      runtime_engine: RuntimeEngine = None,
                      spark_conf: Dict[str, str] = None,
                      spark_env_vars: Dict[str, str] = None,
                      ssh_public_keys: List[str] = None,
                      workload_type: WorkloadType = None,
                      timeout=timedelta(minutes=20)) -> ClusterInfo:
        return self.edit(apply_policy_default_values=apply_policy_default_values,
                         autoscale=autoscale,
                         autotermination_minutes=autotermination_minutes,
                         aws_attributes=aws_attributes,
                         azure_attributes=azure_attributes,
                         cluster_id=cluster_id,
                         cluster_log_conf=cluster_log_conf,
                         cluster_name=cluster_name,
                         cluster_source=cluster_source,
                         custom_tags=custom_tags,
                         driver_instance_pool_id=driver_instance_pool_id,
                         driver_node_type_id=driver_node_type_id,
                         enable_elastic_disk=enable_elastic_disk,
                         enable_local_disk_encryption=enable_local_disk_encryption,
                         gcp_attributes=gcp_attributes,
                         instance_pool_id=instance_pool_id,
                         node_type_id=node_type_id,
                         num_workers=num_workers,
                         policy_id=policy_id,
                         runtime_engine=runtime_engine,
                         spark_conf=spark_conf,
                         spark_env_vars=spark_env_vars,
                         spark_version=spark_version,
                         ssh_public_keys=ssh_public_keys,
                         workload_type=workload_type).result(timeout=timeout)

    def events(self,
               cluster_id: str,
               *,
               end_time: int = None,
               event_types: List[EventType] = None,
               limit: int = None,
               offset: int = None,
               order: GetEventsOrder = None,
               start_time: int = None,
               **kwargs) -> Iterator[ClusterEvent]:
        """List cluster activity events.
        
        Retrieves a list of events about the activity of a cluster. This API is paginated. If there are more
        events to read, the response includes all the nparameters necessary to request the next page of
        events."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetEvents(cluster_id=cluster_id,
                                end_time=end_time,
                                event_types=event_types,
                                limit=limit,
                                offset=offset,
                                order=order,
                                start_time=start_time)
        body = request.as_dict()

        while True:
            json = self._api.do('POST', '/api/2.0/clusters/events', body=body)
            if 'events' not in json or not json['events']:
                return
            for v in json['events']:
                yield ClusterEvent.from_dict(v)
            if 'next_page' not in json or not json['next_page']:
                return
            body = json['next_page']

    def get(self, cluster_id: str, **kwargs) -> ClusterInfo:
        """Get cluster info.
        
        "Retrieves the information for a cluster given its identifier. Clusters can be described while they
        are running, or up to 60 days after they are terminated."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetClusterRequest(cluster_id=cluster_id)

        query = {}
        if cluster_id: query['cluster_id'] = request.cluster_id

        json = self._api.do('GET', '/api/2.0/clusters/get', query=query)
        return ClusterInfo.from_dict(json)

    def list(self, *, can_use_client: str = None, **kwargs) -> Iterator[ClusterInfo]:
        """List all clusters.
        
        Return information about all pinned clusters, active clusters, up to 200 of the most recently
        terminated all-purpose clusters in the past 30 days, and up to 30 of the most recently terminated job
        clusters in the past 30 days.
        
        For example, if there is 1 pinned cluster, 4 active clusters, 45 terminated all-purpose clusters in
        the past 30 days, and 50 terminated job clusters in the past 30 days, then this API returns the 1
        pinned cluster, 4 active clusters, all 45 terminated all-purpose clusters, and the 30 most recently
        terminated job clusters."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListClustersRequest(can_use_client=can_use_client)

        query = {}
        if can_use_client: query['can_use_client'] = request.can_use_client

        json = self._api.do('GET', '/api/2.0/clusters/list', query=query)
        return [ClusterInfo.from_dict(v) for v in json.get('clusters', [])]

    def list_node_types(self) -> ListNodeTypesResponse:
        """List node types.
        
        Returns a list of supported Spark node types. These node types can be used to launch a cluster."""

        json = self._api.do('GET', '/api/2.0/clusters/list-node-types')
        return ListNodeTypesResponse.from_dict(json)

    def list_zones(self) -> ListAvailableZonesResponse:
        """List availability zones.
        
        Returns a list of availability zones where clusters can be created in (For example, us-west-2a). These
        zones can be used to launch a cluster."""

        json = self._api.do('GET', '/api/2.0/clusters/list-zones')
        return ListAvailableZonesResponse.from_dict(json)

    def permanent_delete(self, cluster_id: str, **kwargs):
        """Permanently delete cluster.
        
        Permanently deletes a Spark cluster. This cluster is terminated and resources are asynchronously
        removed.
        
        In addition, users will no longer see permanently deleted clusters in the cluster list, and API users
        can no longer perform any action on permanently deleted clusters."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PermanentDeleteCluster(cluster_id=cluster_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/clusters/permanent-delete', body=body)

    def pin(self, cluster_id: str, **kwargs):
        """Pin cluster.
        
        Pinning a cluster ensures that the cluster will always be returned by the ListClusters API. Pinning a
        cluster that is already pinned will have no effect. This API can only be called by workspace admins."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PinCluster(cluster_id=cluster_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/clusters/pin', body=body)

    def resize(self,
               cluster_id: str,
               *,
               autoscale: AutoScale = None,
               num_workers: int = None,
               **kwargs) -> Wait[ClusterInfo]:
        """Resize cluster.
        
        Resizes a cluster to have a desired number of workers. This will fail unless the cluster is in a
        `RUNNING` state."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ResizeCluster(autoscale=autoscale, cluster_id=cluster_id, num_workers=num_workers)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/clusters/resize', body=body)
        return Wait(self.wait_get_cluster_running, cluster_id=request.cluster_id)

    def resize_and_wait(self,
                        cluster_id: str,
                        *,
                        autoscale: AutoScale = None,
                        num_workers: int = None,
                        timeout=timedelta(minutes=20)) -> ClusterInfo:
        return self.resize(autoscale=autoscale, cluster_id=cluster_id,
                           num_workers=num_workers).result(timeout=timeout)

    def restart(self, cluster_id: str, *, restart_user: str = None, **kwargs) -> Wait[ClusterInfo]:
        """Restart cluster.
        
        Restarts a Spark cluster with the supplied ID. If the cluster is not currently in a `RUNNING` state,
        nothing will happen."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RestartCluster(cluster_id=cluster_id, restart_user=restart_user)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/clusters/restart', body=body)
        return Wait(self.wait_get_cluster_running, cluster_id=request.cluster_id)

    def restart_and_wait(self,
                         cluster_id: str,
                         *,
                         restart_user: str = None,
                         timeout=timedelta(minutes=20)) -> ClusterInfo:
        return self.restart(cluster_id=cluster_id, restart_user=restart_user).result(timeout=timeout)

    def spark_versions(self) -> GetSparkVersionsResponse:
        """List available Spark versions.
        
        Returns the list of available Spark versions. These versions can be used to launch a cluster."""

        json = self._api.do('GET', '/api/2.0/clusters/spark-versions')
        return GetSparkVersionsResponse.from_dict(json)

    def start(self, cluster_id: str, **kwargs) -> Wait[ClusterInfo]:
        """Start terminated cluster.
        
        Starts a terminated Spark cluster with the supplied ID. This works similar to `createCluster` except:
        
        * The previous cluster id and attributes are preserved. * The cluster starts with the last specified
        cluster size. * If the previous cluster was an autoscaling cluster, the current cluster starts with
        the minimum number of nodes. * If the cluster is not currently in a `TERMINATED` state, nothing will
        happen. * Clusters launched to run a job cannot be started."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = StartCluster(cluster_id=cluster_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/clusters/start', body=body)
        return Wait(self.wait_get_cluster_running, cluster_id=request.cluster_id)

    def start_and_wait(self, cluster_id: str, timeout=timedelta(minutes=20)) -> ClusterInfo:
        return self.start(cluster_id=cluster_id).result(timeout=timeout)

    def unpin(self, cluster_id: str, **kwargs):
        """Unpin cluster.
        
        Unpinning a cluster will allow the cluster to eventually be removed from the ListClusters API.
        Unpinning a cluster that is not pinned will have no effect. This API can only be called by workspace
        admins."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UnpinCluster(cluster_id=cluster_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/clusters/unpin', body=body)


class CommandExecutionAPI:
    """This API allows execution of Python, Scala, SQL, or R commands on running Databricks Clusters."""

    def __init__(self, api_client):
        self._api = api_client

    def wait_command_status_command_execution_cancelled(
            self,
            cluster_id: str,
            command_id: str,
            context_id: str,
            timeout=timedelta(minutes=20),
            callback: Callable[[CommandStatusResponse], None] = None) -> CommandStatusResponse:
        deadline = time.time() + timeout.total_seconds()
        target_states = (CommandStatus.Cancelled, )
        failure_states = (CommandStatus.Error, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.command_status(cluster_id=cluster_id, command_id=command_id, context_id=context_id)
            status = poll.status
            status_message = f'current status: {status}'
            if poll.results:
                status_message = poll.results.cause
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach Cancelled, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"cluster_id={cluster_id}, command_id={command_id}, context_id={context_id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def wait_command_status_command_execution_finished_or_error(
            self,
            cluster_id: str,
            command_id: str,
            context_id: str,
            timeout=timedelta(minutes=20),
            callback: Callable[[CommandStatusResponse], None] = None) -> CommandStatusResponse:
        deadline = time.time() + timeout.total_seconds()
        target_states = (CommandStatus.Finished, CommandStatus.Error, )
        failure_states = (CommandStatus.Cancelled, CommandStatus.Cancelling, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.command_status(cluster_id=cluster_id, command_id=command_id, context_id=context_id)
            status = poll.status
            status_message = f'current status: {status}'
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach Finished or Error, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"cluster_id={cluster_id}, command_id={command_id}, context_id={context_id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def wait_context_status_command_execution_running(
            self,
            cluster_id: str,
            context_id: str,
            timeout=timedelta(minutes=20),
            callback: Callable[[ContextStatusResponse], None] = None) -> ContextStatusResponse:
        deadline = time.time() + timeout.total_seconds()
        target_states = (ContextStatus.Running, )
        failure_states = (ContextStatus.Error, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.context_status(cluster_id=cluster_id, context_id=context_id)
            status = poll.status
            status_message = f'current status: {status}'
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach Running, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"cluster_id={cluster_id}, context_id={context_id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def cancel(self,
               *,
               cluster_id: str = None,
               command_id: str = None,
               context_id: str = None,
               **kwargs) -> Wait[CommandStatusResponse]:
        """Cancel a command.
        
        Cancels a currently running command within an execution context.
        
        The command ID is obtained from a prior successful call to __execute__."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CancelCommand(cluster_id=cluster_id, command_id=command_id, context_id=context_id)
        body = request.as_dict()
        self._api.do('POST', '/api/1.2/commands/cancel', body=body)
        return Wait(self.wait_command_status_command_execution_cancelled,
                    cluster_id=request.cluster_id,
                    command_id=request.command_id,
                    context_id=request.context_id)

    def cancel_and_wait(self,
                        *,
                        cluster_id: str = None,
                        command_id: str = None,
                        context_id: str = None,
                        timeout=timedelta(minutes=20)) -> CommandStatusResponse:
        return self.cancel(cluster_id=cluster_id, command_id=command_id,
                           context_id=context_id).result(timeout=timeout)

    def command_status(self, cluster_id: str, context_id: str, command_id: str,
                       **kwargs) -> CommandStatusResponse:
        """Get command info.
        
        Gets the status of and, if available, the results from a currently executing command.
        
        The command ID is obtained from a prior successful call to __execute__."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CommandStatusRequest(cluster_id=cluster_id,
                                           command_id=command_id,
                                           context_id=context_id)

        query = {}
        if cluster_id: query['clusterId'] = request.cluster_id
        if command_id: query['commandId'] = request.command_id
        if context_id: query['contextId'] = request.context_id

        json = self._api.do('GET', '/api/1.2/commands/status', query=query)
        return CommandStatusResponse.from_dict(json)

    def context_status(self, cluster_id: str, context_id: str, **kwargs) -> ContextStatusResponse:
        """Get status.
        
        Gets the status for an execution context."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ContextStatusRequest(cluster_id=cluster_id, context_id=context_id)

        query = {}
        if cluster_id: query['clusterId'] = request.cluster_id
        if context_id: query['contextId'] = request.context_id

        json = self._api.do('GET', '/api/1.2/contexts/status', query=query)
        return ContextStatusResponse.from_dict(json)

    def create(self,
               *,
               cluster_id: str = None,
               language: Language = None,
               **kwargs) -> Wait[ContextStatusResponse]:
        """Create an execution context.
        
        Creates an execution context for running cluster commands.
        
        If successful, this method returns the ID of the new execution context."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateContext(cluster_id=cluster_id, language=language)
        body = request.as_dict()
        op_response = self._api.do('POST', '/api/1.2/contexts/create', body=body)
        return Wait(self.wait_context_status_command_execution_running,
                    response=Created.from_dict(op_response),
                    cluster_id=request.cluster_id,
                    context_id=op_response['id'])

    def create_and_wait(self,
                        *,
                        cluster_id: str = None,
                        language: Language = None,
                        timeout=timedelta(minutes=20)) -> ContextStatusResponse:
        return self.create(cluster_id=cluster_id, language=language).result(timeout=timeout)

    def destroy(self, cluster_id: str, context_id: str, **kwargs):
        """Delete an execution context.
        
        Deletes an execution context."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DestroyContext(cluster_id=cluster_id, context_id=context_id)
        body = request.as_dict()
        self._api.do('POST', '/api/1.2/contexts/destroy', body=body)

    def execute(self,
                *,
                cluster_id: str = None,
                command: str = None,
                context_id: str = None,
                language: Language = None,
                **kwargs) -> Wait[CommandStatusResponse]:
        """Run a command.
        
        Runs a cluster command in the given execution context, using the provided language.
        
        If successful, it returns an ID for tracking the status of the command's execution."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Command(cluster_id=cluster_id,
                              command=command,
                              context_id=context_id,
                              language=language)
        body = request.as_dict()
        op_response = self._api.do('POST', '/api/1.2/commands/execute', body=body)
        return Wait(self.wait_command_status_command_execution_finished_or_error,
                    response=Created.from_dict(op_response),
                    cluster_id=request.cluster_id,
                    command_id=op_response['id'],
                    context_id=request.context_id)

    def execute_and_wait(self,
                         *,
                         cluster_id: str = None,
                         command: str = None,
                         context_id: str = None,
                         language: Language = None,
                         timeout=timedelta(minutes=20)) -> CommandStatusResponse:
        return self.execute(cluster_id=cluster_id, command=command, context_id=context_id,
                            language=language).result(timeout=timeout)


class GlobalInitScriptsAPI:
    """The Global Init Scripts API enables Workspace administrators to configure global initialization scripts
    for their workspace. These scripts run on every node in every cluster in the workspace.
    
    **Important:** Existing clusters must be restarted to pick up any changes made to global init scripts.
    Global init scripts are run in order. If the init script returns with a bad exit code, the Apache Spark
    container fails to launch and init scripts with later position are skipped. If enough containers fail, the
    entire cluster fails with a `GLOBAL_INIT_SCRIPT_FAILURE` error code."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               script: str,
               *,
               enabled: bool = None,
               position: int = None,
               **kwargs) -> CreateResponse:
        """Create init script.
        
        Creates a new global init script in this workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GlobalInitScriptCreateRequest(enabled=enabled,
                                                    name=name,
                                                    position=position,
                                                    script=script)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/global-init-scripts', body=body)
        return CreateResponse.from_dict(json)

    def delete(self, script_id: str, **kwargs):
        """Delete init script.
        
        Deletes a global init script."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteGlobalInitScriptRequest(script_id=script_id)

        self._api.do('DELETE', f'/api/2.0/global-init-scripts/{request.script_id}')

    def get(self, script_id: str, **kwargs) -> GlobalInitScriptDetailsWithContent:
        """Get an init script.
        
        Gets all the details of a script, including its Base64-encoded contents."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetGlobalInitScriptRequest(script_id=script_id)

        json = self._api.do('GET', f'/api/2.0/global-init-scripts/{request.script_id}')
        return GlobalInitScriptDetailsWithContent.from_dict(json)

    def list(self) -> Iterator[GlobalInitScriptDetails]:
        """Get init scripts.
        
        "Get a list of all global init scripts for this workspace. This returns all properties for each script
        but **not** the script contents. To retrieve the contents of a script, use the [get a global init
        script](#operation/get-script) operation."""

        json = self._api.do('GET', '/api/2.0/global-init-scripts')
        return [GlobalInitScriptDetails.from_dict(v) for v in json.get('scripts', [])]

    def update(self,
               name: str,
               script: str,
               script_id: str,
               *,
               enabled: bool = None,
               position: int = None,
               **kwargs):
        """Update init script.
        
        Updates a global init script, specifying only the fields to change. All fields are optional.
        Unspecified fields retain their current value."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GlobalInitScriptUpdateRequest(enabled=enabled,
                                                    name=name,
                                                    position=position,
                                                    script=script,
                                                    script_id=script_id)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.0/global-init-scripts/{request.script_id}', body=body)


class InstancePoolsAPI:
    """Instance Pools API are used to create, edit, delete and list instance pools by using ready-to-use cloud
    instances which reduces a cluster start and auto-scaling times.
    
    Databricks pools reduce cluster start and auto-scaling times by maintaining a set of idle, ready-to-use
    instances. When a cluster is attached to a pool, cluster nodes are created using the pool’s idle
    instances. If the pool has no idle instances, the pool expands by allocating a new instance from the
    instance provider in order to accommodate the cluster’s request. When a cluster releases an instance, it
    returns to the pool and is free for another cluster to use. Only clusters attached to a pool can use that
    pool’s idle instances.
    
    You can specify a different pool for the driver node and worker nodes, or use the same pool for both.
    
    Databricks does not charge DBUs while instances are idle in the pool. Instance provider billing does
    apply. See pricing."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               instance_pool_name: str,
               node_type_id: str,
               *,
               aws_attributes: InstancePoolAwsAttributes = None,
               azure_attributes: InstancePoolAzureAttributes = None,
               custom_tags: Dict[str, str] = None,
               disk_spec: DiskSpec = None,
               enable_elastic_disk: bool = None,
               idle_instance_autotermination_minutes: int = None,
               instance_pool_fleet_attributes: InstancePoolFleetAttributes = None,
               max_capacity: int = None,
               min_idle_instances: int = None,
               preloaded_docker_images: List[DockerImage] = None,
               preloaded_spark_versions: List[str] = None,
               **kwargs) -> CreateInstancePoolResponse:
        """Create a new instance pool.
        
        Creates a new instance pool using idle and ready-to-use cloud instances."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateInstancePool(
                aws_attributes=aws_attributes,
                azure_attributes=azure_attributes,
                custom_tags=custom_tags,
                disk_spec=disk_spec,
                enable_elastic_disk=enable_elastic_disk,
                idle_instance_autotermination_minutes=idle_instance_autotermination_minutes,
                instance_pool_fleet_attributes=instance_pool_fleet_attributes,
                instance_pool_name=instance_pool_name,
                max_capacity=max_capacity,
                min_idle_instances=min_idle_instances,
                node_type_id=node_type_id,
                preloaded_docker_images=preloaded_docker_images,
                preloaded_spark_versions=preloaded_spark_versions)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/instance-pools/create', body=body)
        return CreateInstancePoolResponse.from_dict(json)

    def delete(self, instance_pool_id: str, **kwargs):
        """Delete an instance pool.
        
        Deletes the instance pool permanently. The idle instances in the pool are terminated asynchronously."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteInstancePool(instance_pool_id=instance_pool_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/instance-pools/delete', body=body)

    def edit(self,
             instance_pool_id: str,
             instance_pool_name: str,
             node_type_id: str,
             *,
             aws_attributes: InstancePoolAwsAttributes = None,
             azure_attributes: InstancePoolAzureAttributes = None,
             custom_tags: Dict[str, str] = None,
             disk_spec: DiskSpec = None,
             enable_elastic_disk: bool = None,
             idle_instance_autotermination_minutes: int = None,
             instance_pool_fleet_attributes: InstancePoolFleetAttributes = None,
             max_capacity: int = None,
             min_idle_instances: int = None,
             preloaded_docker_images: List[DockerImage] = None,
             preloaded_spark_versions: List[str] = None,
             **kwargs):
        """Edit an existing instance pool.
        
        Modifies the configuration of an existing instance pool."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = EditInstancePool(
                aws_attributes=aws_attributes,
                azure_attributes=azure_attributes,
                custom_tags=custom_tags,
                disk_spec=disk_spec,
                enable_elastic_disk=enable_elastic_disk,
                idle_instance_autotermination_minutes=idle_instance_autotermination_minutes,
                instance_pool_fleet_attributes=instance_pool_fleet_attributes,
                instance_pool_id=instance_pool_id,
                instance_pool_name=instance_pool_name,
                max_capacity=max_capacity,
                min_idle_instances=min_idle_instances,
                node_type_id=node_type_id,
                preloaded_docker_images=preloaded_docker_images,
                preloaded_spark_versions=preloaded_spark_versions)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/instance-pools/edit', body=body)

    def get(self, instance_pool_id: str, **kwargs) -> GetInstancePool:
        """Get instance pool information.
        
        Retrieve the information for an instance pool based on its identifier."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetInstancePoolRequest(instance_pool_id=instance_pool_id)

        query = {}
        if instance_pool_id: query['instance_pool_id'] = request.instance_pool_id

        json = self._api.do('GET', '/api/2.0/instance-pools/get', query=query)
        return GetInstancePool.from_dict(json)

    def list(self) -> Iterator[InstancePoolAndStats]:
        """List instance pool info.
        
        Gets a list of instance pools with their statistics."""

        json = self._api.do('GET', '/api/2.0/instance-pools/list')
        return [InstancePoolAndStats.from_dict(v) for v in json.get('instance_pools', [])]


class InstanceProfilesAPI:
    """The Instance Profiles API allows admins to add, list, and remove instance profiles that users can launch
    clusters with. Regular users can list the instance profiles available to them. See [Secure access to S3
    buckets] using instance profiles for more information.
    
    [Secure access to S3 buckets]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/instance-profiles.html"""

    def __init__(self, api_client):
        self._api = api_client

    def add(self,
            instance_profile_arn: str,
            *,
            iam_role_arn: str = None,
            is_meta_instance_profile: bool = None,
            skip_validation: bool = None,
            **kwargs):
        """Register an instance profile.
        
        In the UI, you can select the instance profile when launching clusters. This API is only available to
        admin users."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = AddInstanceProfile(iam_role_arn=iam_role_arn,
                                         instance_profile_arn=instance_profile_arn,
                                         is_meta_instance_profile=is_meta_instance_profile,
                                         skip_validation=skip_validation)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/instance-profiles/add', body=body)

    def edit(self,
             instance_profile_arn: str,
             *,
             iam_role_arn: str = None,
             is_meta_instance_profile: bool = None,
             **kwargs):
        """Edit an instance profile.
        
        The only supported field to change is the optional IAM role ARN associated with the instance profile.
        It is required to specify the IAM role ARN if both of the following are true:
        
        * Your role name and instance profile name do not match. The name is the part after the last slash in
        each ARN. * You want to use the instance profile with [Databricks SQL Serverless].
        
        To understand where these fields are in the AWS console, see [Enable serverless SQL warehouses].
        
        This API is only available to admin users.
        
        [Databricks SQL Serverless]: https://docs.databricks.com/sql/admin/serverless.html
        [Enable serverless SQL warehouses]: https://docs.databricks.com/sql/admin/serverless.html"""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = InstanceProfile(iam_role_arn=iam_role_arn,
                                      instance_profile_arn=instance_profile_arn,
                                      is_meta_instance_profile=is_meta_instance_profile)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/instance-profiles/edit', body=body)

    def list(self) -> Iterator[InstanceProfile]:
        """List available instance profiles.
        
        List the instance profiles that the calling user can use to launch a cluster.
        
        This API is available to all users."""

        json = self._api.do('GET', '/api/2.0/instance-profiles/list')
        return [InstanceProfile.from_dict(v) for v in json.get('instance_profiles', [])]

    def remove(self, instance_profile_arn: str, **kwargs):
        """Remove the instance profile.
        
        Remove the instance profile with the provided ARN. Existing clusters with this instance profile will
        continue to function.
        
        This API is only accessible to admin users."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RemoveInstanceProfile(instance_profile_arn=instance_profile_arn)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/instance-profiles/remove', body=body)


class LibrariesAPI:
    """The Libraries API allows you to install and uninstall libraries and get the status of libraries on a
    cluster.
    
    To make third-party or custom code available to notebooks and jobs running on your clusters, you can
    install a library. Libraries can be written in Python, Java, Scala, and R. You can upload Java, Scala, and
    Python libraries and point to external packages in PyPI, Maven, and CRAN repositories.
    
    Cluster libraries can be used by all notebooks running on a cluster. You can install a cluster library
    directly from a public repository such as PyPI or Maven, using a previously installed workspace library,
    or using an init script.
    
    When you install a library on a cluster, a notebook already attached to that cluster will not immediately
    see the new library. You must first detach and then reattach the notebook to the cluster.
    
    When you uninstall a library from a cluster, the library is removed only when you restart the cluster.
    Until you restart the cluster, the status of the uninstalled library appears as Uninstall pending restart."""

    def __init__(self, api_client):
        self._api = api_client

    def all_cluster_statuses(self) -> ListAllClusterLibraryStatusesResponse:
        """Get all statuses.
        
        Get the status of all libraries on all clusters. A status will be available for all libraries
        installed on this cluster via the API or the libraries UI as well as libraries set to be installed on
        all clusters via the libraries UI."""

        json = self._api.do('GET', '/api/2.0/libraries/all-cluster-statuses')
        return ListAllClusterLibraryStatusesResponse.from_dict(json)

    def cluster_status(self, cluster_id: str, **kwargs) -> ClusterLibraryStatuses:
        """Get status.
        
        Get the status of libraries on a cluster. A status will be available for all libraries installed on
        this cluster via the API or the libraries UI as well as libraries set to be installed on all clusters
        via the libraries UI. The order of returned libraries will be as follows.
        
        1. Libraries set to be installed on this cluster will be returned first. Within this group, the final
        order will be order in which the libraries were added to the cluster.
        
        2. Libraries set to be installed on all clusters are returned next. Within this group there is no
        order guarantee.
        
        3. Libraries that were previously requested on this cluster or on all clusters, but now marked for
        removal. Within this group there is no order guarantee."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ClusterStatusRequest(cluster_id=cluster_id)

        query = {}
        if cluster_id: query['cluster_id'] = request.cluster_id

        json = self._api.do('GET', '/api/2.0/libraries/cluster-status', query=query)
        return ClusterLibraryStatuses.from_dict(json)

    def install(self, cluster_id: str, libraries: List[Library], **kwargs):
        """Add a library.
        
        Add libraries to be installed on a cluster. The installation is asynchronous; it happens in the
        background after the completion of this request.
        
        **Note**: The actual set of libraries to be installed on a cluster is the union of the libraries
        specified via this method and the libraries set to be installed on all clusters via the libraries UI."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = InstallLibraries(cluster_id=cluster_id, libraries=libraries)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/libraries/install', body=body)

    def uninstall(self, cluster_id: str, libraries: List[Library], **kwargs):
        """Uninstall libraries.
        
        Set libraries to be uninstalled on a cluster. The libraries won't be uninstalled until the cluster is
        restarted. Uninstalling libraries that are not installed on the cluster will have no impact but is not
        an error."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UninstallLibraries(cluster_id=cluster_id, libraries=libraries)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/libraries/uninstall', body=body)


class PolicyFamiliesAPI:
    """View available policy families. A policy family contains a policy definition providing best practices for
    configuring clusters for a particular use case.
    
    Databricks manages and provides policy families for several common cluster use cases. You cannot create,
    edit, or delete policy families.
    
    Policy families cannot be used directly to create clusters. Instead, you create cluster policies using a
    policy family. Cluster policies created using a policy family inherit the policy family's policy
    definition."""

    def __init__(self, api_client):
        self._api = api_client

    def get(self, policy_family_id: str, **kwargs) -> PolicyFamily:

        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetPolicyFamilyRequest(policy_family_id=policy_family_id)

        json = self._api.do('GET', f'/api/2.0/policy-families/{request.policy_family_id}')
        return PolicyFamily.from_dict(json)

    def list(self, *, max_results: int = None, page_token: str = None, **kwargs) -> Iterator[PolicyFamily]:

        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListPolicyFamiliesRequest(max_results=max_results, page_token=page_token)

        query = {}
        if max_results: query['max_results'] = request.max_results
        if page_token: query['page_token'] = request.page_token

        while True:
            json = self._api.do('GET', '/api/2.0/policy-families', query=query)
            if 'policy_families' not in json or not json['policy_families']:
                return
            for v in json['policy_families']:
                yield PolicyFamily.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

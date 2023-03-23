# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
import random
import time
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Dict, Iterator, List

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
class Get:
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


@dataclass
class ListRequest:
    """List all clusters"""

    can_use_client: str = None


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

    def wait_get_cluster_running(self, cluster_id: str, timeout=timedelta(minutes=20)) -> ClusterInfo:
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

    def wait_get_cluster_terminated(self, cluster_id: str, timeout=timedelta(minutes=20)) -> ClusterInfo:
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
        return Wait(self.wait_get_cluster_running, cluster_id=op_response['cluster_id'])

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
            request = Get(cluster_id=cluster_id)

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
            request = ListRequest(can_use_client=can_use_client)

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

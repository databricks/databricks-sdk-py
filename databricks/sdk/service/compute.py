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

# all definitions in this file are in alphabetical order


@dataclass
class AddInstanceProfile:
    instance_profile_arn: str
    iam_role_arn: Optional[str] = None
    is_meta_instance_profile: Optional[bool] = None
    skip_validation: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.iam_role_arn is not None: body['iam_role_arn'] = self.iam_role_arn
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.is_meta_instance_profile is not None:
            body['is_meta_instance_profile'] = self.is_meta_instance_profile
        if self.skip_validation is not None: body['skip_validation'] = self.skip_validation
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
        if self.max_workers is not None: body['max_workers'] = self.max_workers
        if self.min_workers is not None: body['min_workers'] = self.min_workers
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AutoScale':
        return cls(max_workers=d.get('max_workers', None), min_workers=d.get('min_workers', None))


@dataclass
class AwsAttributes:
    availability: Optional['AwsAvailability'] = None
    ebs_volume_count: Optional[int] = None
    ebs_volume_iops: Optional[int] = None
    ebs_volume_size: Optional[int] = None
    ebs_volume_throughput: Optional[int] = None
    ebs_volume_type: Optional['EbsVolumeType'] = None
    first_on_demand: Optional[int] = None
    instance_profile_arn: Optional[str] = None
    spot_bid_price_percent: Optional[int] = None
    zone_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.availability is not None: body['availability'] = self.availability.value
        if self.ebs_volume_count is not None: body['ebs_volume_count'] = self.ebs_volume_count
        if self.ebs_volume_iops is not None: body['ebs_volume_iops'] = self.ebs_volume_iops
        if self.ebs_volume_size is not None: body['ebs_volume_size'] = self.ebs_volume_size
        if self.ebs_volume_throughput is not None: body['ebs_volume_throughput'] = self.ebs_volume_throughput
        if self.ebs_volume_type is not None: body['ebs_volume_type'] = self.ebs_volume_type.value
        if self.first_on_demand is not None: body['first_on_demand'] = self.first_on_demand
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.spot_bid_price_percent is not None:
            body['spot_bid_price_percent'] = self.spot_bid_price_percent
        if self.zone_id is not None: body['zone_id'] = self.zone_id
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
    availability: Optional['AzureAvailability'] = None
    first_on_demand: Optional[int] = None
    log_analytics_info: Optional['LogAnalyticsInfo'] = None
    spot_bid_max_price: Optional[float] = None

    def as_dict(self) -> dict:
        body = {}
        if self.availability is not None: body['availability'] = self.availability.value
        if self.first_on_demand is not None: body['first_on_demand'] = self.first_on_demand
        if self.log_analytics_info: body['log_analytics_info'] = self.log_analytics_info.as_dict()
        if self.spot_bid_max_price is not None: body['spot_bid_max_price'] = self.spot_bid_max_price
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
class CancelCommand:
    cluster_id: Optional[str] = None
    command_id: Optional[str] = None
    context_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['clusterId'] = self.cluster_id
        if self.command_id is not None: body['commandId'] = self.command_id
        if self.context_id is not None: body['contextId'] = self.context_id
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
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.owner_username is not None: body['owner_username'] = self.owner_username
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ChangeClusterOwner':
        return cls(cluster_id=d.get('cluster_id', None), owner_username=d.get('owner_username', None))


@dataclass
class ClientsTypes:
    jobs: Optional[bool] = None
    notebooks: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.jobs is not None: body['jobs'] = self.jobs
        if self.notebooks is not None: body['notebooks'] = self.notebooks
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClientsTypes':
        return cls(jobs=d.get('jobs', None), notebooks=d.get('notebooks', None))


@dataclass
class CloudProviderNodeInfo:
    status: Optional['List[CloudProviderNodeStatus]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.status: body['status'] = [v.value for v in self.status]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CloudProviderNodeInfo':
        return cls(status=d.get('status', None))


class CloudProviderNodeStatus(Enum):

    NOT_AVAILABLE_IN_REGION = 'NotAvailableInRegion'
    NOT_ENABLED_ON_SUBSCRIPTION = 'NotEnabledOnSubscription'


@dataclass
class ClusterAccessControlRequest:
    group_name: Optional[str] = None
    permission_level: Optional['ClusterPermissionLevel'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterAccessControlRequest':
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', ClusterPermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class ClusterAccessControlResponse:
    all_permissions: Optional['List[ClusterPermission]'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterAccessControlResponse':
        return cls(all_permissions=_repeated(d, 'all_permissions', ClusterPermission),
                   display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class ClusterAttributes:
    spark_version: str
    autotermination_minutes: Optional[int] = None
    aws_attributes: Optional['AwsAttributes'] = None
    azure_attributes: Optional['AzureAttributes'] = None
    cluster_log_conf: Optional['ClusterLogConf'] = None
    cluster_name: Optional[str] = None
    cluster_source: Optional['ClusterSource'] = None
    custom_tags: Optional['Dict[str,str]'] = None
    data_security_mode: Optional['DataSecurityMode'] = None
    docker_image: Optional['DockerImage'] = None
    driver_instance_pool_id: Optional[str] = None
    driver_node_type_id: Optional[str] = None
    enable_elastic_disk: Optional[bool] = None
    enable_local_disk_encryption: Optional[bool] = None
    gcp_attributes: Optional['GcpAttributes'] = None
    init_scripts: Optional['List[InitScriptInfo]'] = None
    instance_pool_id: Optional[str] = None
    node_type_id: Optional[str] = None
    policy_id: Optional[str] = None
    runtime_engine: Optional['RuntimeEngine'] = None
    single_user_name: Optional[str] = None
    spark_conf: Optional['Dict[str,str]'] = None
    spark_env_vars: Optional['Dict[str,str]'] = None
    ssh_public_keys: Optional['List[str]'] = None
    workload_type: Optional['WorkloadType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.autotermination_minutes is not None:
            body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.cluster_log_conf: body['cluster_log_conf'] = self.cluster_log_conf.as_dict()
        if self.cluster_name is not None: body['cluster_name'] = self.cluster_name
        if self.cluster_source is not None: body['cluster_source'] = self.cluster_source.value
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.data_security_mode is not None: body['data_security_mode'] = self.data_security_mode.value
        if self.docker_image: body['docker_image'] = self.docker_image.as_dict()
        if self.driver_instance_pool_id is not None:
            body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id is not None: body['driver_node_type_id'] = self.driver_node_type_id
        if self.enable_elastic_disk is not None: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption is not None:
            body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.init_scripts: body['init_scripts'] = [v.as_dict() for v in self.init_scripts]
        if self.instance_pool_id is not None: body['instance_pool_id'] = self.instance_pool_id
        if self.node_type_id is not None: body['node_type_id'] = self.node_type_id
        if self.policy_id is not None: body['policy_id'] = self.policy_id
        if self.runtime_engine is not None: body['runtime_engine'] = self.runtime_engine.value
        if self.single_user_name is not None: body['single_user_name'] = self.single_user_name
        if self.spark_conf: body['spark_conf'] = self.spark_conf
        if self.spark_env_vars: body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version is not None: body['spark_version'] = self.spark_version
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
                   data_security_mode=_enum(d, 'data_security_mode', DataSecurityMode),
                   docker_image=_from_dict(d, 'docker_image', DockerImage),
                   driver_instance_pool_id=d.get('driver_instance_pool_id', None),
                   driver_node_type_id=d.get('driver_node_type_id', None),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
                   gcp_attributes=_from_dict(d, 'gcp_attributes', GcpAttributes),
                   init_scripts=_repeated(d, 'init_scripts', InitScriptInfo),
                   instance_pool_id=d.get('instance_pool_id', None),
                   node_type_id=d.get('node_type_id', None),
                   policy_id=d.get('policy_id', None),
                   runtime_engine=_enum(d, 'runtime_engine', RuntimeEngine),
                   single_user_name=d.get('single_user_name', None),
                   spark_conf=d.get('spark_conf', None),
                   spark_env_vars=d.get('spark_env_vars', None),
                   spark_version=d.get('spark_version', None),
                   ssh_public_keys=d.get('ssh_public_keys', None),
                   workload_type=_from_dict(d, 'workload_type', WorkloadType))


@dataclass
class ClusterDetails:
    autoscale: Optional['AutoScale'] = None
    autotermination_minutes: Optional[int] = None
    aws_attributes: Optional['AwsAttributes'] = None
    azure_attributes: Optional['AzureAttributes'] = None
    cluster_cores: Optional[float] = None
    cluster_id: Optional[str] = None
    cluster_log_conf: Optional['ClusterLogConf'] = None
    cluster_log_status: Optional['LogSyncStatus'] = None
    cluster_memory_mb: Optional[int] = None
    cluster_name: Optional[str] = None
    cluster_source: Optional['ClusterSource'] = None
    creator_user_name: Optional[str] = None
    custom_tags: Optional['Dict[str,str]'] = None
    data_security_mode: Optional['DataSecurityMode'] = None
    default_tags: Optional['Dict[str,str]'] = None
    docker_image: Optional['DockerImage'] = None
    driver: Optional['SparkNode'] = None
    driver_instance_pool_id: Optional[str] = None
    driver_node_type_id: Optional[str] = None
    enable_elastic_disk: Optional[bool] = None
    enable_local_disk_encryption: Optional[bool] = None
    executors: Optional['List[SparkNode]'] = None
    gcp_attributes: Optional['GcpAttributes'] = None
    init_scripts: Optional['List[InitScriptInfo]'] = None
    instance_pool_id: Optional[str] = None
    jdbc_port: Optional[int] = None
    last_restarted_time: Optional[int] = None
    last_state_loss_time: Optional[int] = None
    node_type_id: Optional[str] = None
    num_workers: Optional[int] = None
    policy_id: Optional[str] = None
    runtime_engine: Optional['RuntimeEngine'] = None
    single_user_name: Optional[str] = None
    spark_conf: Optional['Dict[str,str]'] = None
    spark_context_id: Optional[int] = None
    spark_env_vars: Optional['Dict[str,str]'] = None
    spark_version: Optional[str] = None
    spec: Optional['CreateCluster'] = None
    ssh_public_keys: Optional['List[str]'] = None
    start_time: Optional[int] = None
    state: Optional['State'] = None
    state_message: Optional[str] = None
    terminated_time: Optional[int] = None
    termination_reason: Optional['TerminationReason'] = None
    workload_type: Optional['WorkloadType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.autoscale: body['autoscale'] = self.autoscale.as_dict()
        if self.autotermination_minutes is not None:
            body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.cluster_cores is not None: body['cluster_cores'] = self.cluster_cores
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.cluster_log_conf: body['cluster_log_conf'] = self.cluster_log_conf.as_dict()
        if self.cluster_log_status: body['cluster_log_status'] = self.cluster_log_status.as_dict()
        if self.cluster_memory_mb is not None: body['cluster_memory_mb'] = self.cluster_memory_mb
        if self.cluster_name is not None: body['cluster_name'] = self.cluster_name
        if self.cluster_source is not None: body['cluster_source'] = self.cluster_source.value
        if self.creator_user_name is not None: body['creator_user_name'] = self.creator_user_name
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.data_security_mode is not None: body['data_security_mode'] = self.data_security_mode.value
        if self.default_tags: body['default_tags'] = self.default_tags
        if self.docker_image: body['docker_image'] = self.docker_image.as_dict()
        if self.driver: body['driver'] = self.driver.as_dict()
        if self.driver_instance_pool_id is not None:
            body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id is not None: body['driver_node_type_id'] = self.driver_node_type_id
        if self.enable_elastic_disk is not None: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption is not None:
            body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.executors: body['executors'] = [v.as_dict() for v in self.executors]
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.init_scripts: body['init_scripts'] = [v.as_dict() for v in self.init_scripts]
        if self.instance_pool_id is not None: body['instance_pool_id'] = self.instance_pool_id
        if self.jdbc_port is not None: body['jdbc_port'] = self.jdbc_port
        if self.last_restarted_time is not None: body['last_restarted_time'] = self.last_restarted_time
        if self.last_state_loss_time is not None: body['last_state_loss_time'] = self.last_state_loss_time
        if self.node_type_id is not None: body['node_type_id'] = self.node_type_id
        if self.num_workers is not None: body['num_workers'] = self.num_workers
        if self.policy_id is not None: body['policy_id'] = self.policy_id
        if self.runtime_engine is not None: body['runtime_engine'] = self.runtime_engine.value
        if self.single_user_name is not None: body['single_user_name'] = self.single_user_name
        if self.spark_conf: body['spark_conf'] = self.spark_conf
        if self.spark_context_id is not None: body['spark_context_id'] = self.spark_context_id
        if self.spark_env_vars: body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version is not None: body['spark_version'] = self.spark_version
        if self.spec: body['spec'] = self.spec.as_dict()
        if self.ssh_public_keys: body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        if self.start_time is not None: body['start_time'] = self.start_time
        if self.state is not None: body['state'] = self.state.value
        if self.state_message is not None: body['state_message'] = self.state_message
        if self.terminated_time is not None: body['terminated_time'] = self.terminated_time
        if self.termination_reason: body['termination_reason'] = self.termination_reason.as_dict()
        if self.workload_type: body['workload_type'] = self.workload_type.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterDetails':
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
                   docker_image=_from_dict(d, 'docker_image', DockerImage),
                   driver=_from_dict(d, 'driver', SparkNode),
                   driver_instance_pool_id=d.get('driver_instance_pool_id', None),
                   driver_node_type_id=d.get('driver_node_type_id', None),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
                   executors=_repeated(d, 'executors', SparkNode),
                   gcp_attributes=_from_dict(d, 'gcp_attributes', GcpAttributes),
                   init_scripts=_repeated(d, 'init_scripts', InitScriptInfo),
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
                   spec=_from_dict(d, 'spec', CreateCluster),
                   ssh_public_keys=d.get('ssh_public_keys', None),
                   start_time=d.get('start_time', None),
                   state=_enum(d, 'state', State),
                   state_message=d.get('state_message', None),
                   terminated_time=d.get('terminated_time', None),
                   termination_reason=_from_dict(d, 'termination_reason', TerminationReason),
                   workload_type=_from_dict(d, 'workload_type', WorkloadType))


@dataclass
class ClusterEvent:
    cluster_id: str
    data_plane_event_details: Optional['DataPlaneEventDetails'] = None
    details: Optional['EventDetails'] = None
    timestamp: Optional[int] = None
    type: Optional['EventType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.data_plane_event_details:
            body['data_plane_event_details'] = self.data_plane_event_details.as_dict()
        if self.details: body['details'] = self.details.as_dict()
        if self.timestamp is not None: body['timestamp'] = self.timestamp
        if self.type is not None: body['type'] = self.type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterEvent':
        return cls(cluster_id=d.get('cluster_id', None),
                   data_plane_event_details=_from_dict(d, 'data_plane_event_details', DataPlaneEventDetails),
                   details=_from_dict(d, 'details', EventDetails),
                   timestamp=d.get('timestamp', None),
                   type=_enum(d, 'type', EventType))


@dataclass
class ClusterLibraryStatuses:
    cluster_id: Optional[str] = None
    library_statuses: Optional['List[LibraryFullStatus]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.library_statuses: body['library_statuses'] = [v.as_dict() for v in self.library_statuses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterLibraryStatuses':
        return cls(cluster_id=d.get('cluster_id', None),
                   library_statuses=_repeated(d, 'library_statuses', LibraryFullStatus))


@dataclass
class ClusterLogConf:
    dbfs: Optional['DbfsStorageInfo'] = None
    s3: Optional['S3StorageInfo'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.dbfs: body['dbfs'] = self.dbfs.as_dict()
        if self.s3: body['s3'] = self.s3.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterLogConf':
        return cls(dbfs=_from_dict(d, 'dbfs', DbfsStorageInfo), s3=_from_dict(d, 's3', S3StorageInfo))


@dataclass
class ClusterPermission:
    inherited: Optional[bool] = None
    inherited_from_object: Optional['List[str]'] = None
    permission_level: Optional['ClusterPermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterPermission':
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', ClusterPermissionLevel))


class ClusterPermissionLevel(Enum):
    """Permission level"""

    CAN_ATTACH_TO = 'CAN_ATTACH_TO'
    CAN_MANAGE = 'CAN_MANAGE'
    CAN_RESTART = 'CAN_RESTART'


@dataclass
class ClusterPermissions:
    access_control_list: Optional['List[ClusterAccessControlResponse]'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterPermissions':
        return cls(access_control_list=_repeated(d, 'access_control_list', ClusterAccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class ClusterPermissionsDescription:
    description: Optional[str] = None
    permission_level: Optional['ClusterPermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterPermissionsDescription':
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', ClusterPermissionLevel))


@dataclass
class ClusterPermissionsRequest:
    access_control_list: Optional['List[ClusterAccessControlRequest]'] = None
    cluster_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterPermissionsRequest':
        return cls(access_control_list=_repeated(d, 'access_control_list', ClusterAccessControlRequest),
                   cluster_id=d.get('cluster_id', None))


@dataclass
class ClusterPolicyAccessControlRequest:
    group_name: Optional[str] = None
    permission_level: Optional['ClusterPolicyPermissionLevel'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterPolicyAccessControlRequest':
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', ClusterPolicyPermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class ClusterPolicyAccessControlResponse:
    all_permissions: Optional['List[ClusterPolicyPermission]'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterPolicyAccessControlResponse':
        return cls(all_permissions=_repeated(d, 'all_permissions', ClusterPolicyPermission),
                   display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class ClusterPolicyPermission:
    inherited: Optional[bool] = None
    inherited_from_object: Optional['List[str]'] = None
    permission_level: Optional['ClusterPolicyPermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterPolicyPermission':
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', ClusterPolicyPermissionLevel))


class ClusterPolicyPermissionLevel(Enum):
    """Permission level"""

    CAN_USE = 'CAN_USE'


@dataclass
class ClusterPolicyPermissions:
    access_control_list: Optional['List[ClusterPolicyAccessControlResponse]'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterPolicyPermissions':
        return cls(access_control_list=_repeated(d, 'access_control_list',
                                                 ClusterPolicyAccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class ClusterPolicyPermissionsDescription:
    description: Optional[str] = None
    permission_level: Optional['ClusterPolicyPermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterPolicyPermissionsDescription':
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', ClusterPolicyPermissionLevel))


@dataclass
class ClusterPolicyPermissionsRequest:
    access_control_list: Optional['List[ClusterPolicyAccessControlRequest]'] = None
    cluster_policy_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.cluster_policy_id is not None: body['cluster_policy_id'] = self.cluster_policy_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterPolicyPermissionsRequest':
        return cls(access_control_list=_repeated(d, 'access_control_list', ClusterPolicyAccessControlRequest),
                   cluster_policy_id=d.get('cluster_policy_id', None))


@dataclass
class ClusterSize:
    autoscale: Optional['AutoScale'] = None
    num_workers: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.autoscale: body['autoscale'] = self.autoscale.as_dict()
        if self.num_workers is not None: body['num_workers'] = self.num_workers
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
class ClusterSpec:
    apply_policy_default_values: Optional[bool] = None
    autoscale: Optional['AutoScale'] = None
    autotermination_minutes: Optional[int] = None
    aws_attributes: Optional['AwsAttributes'] = None
    azure_attributes: Optional['AzureAttributes'] = None
    cluster_log_conf: Optional['ClusterLogConf'] = None
    cluster_name: Optional[str] = None
    cluster_source: Optional['ClusterSource'] = None
    custom_tags: Optional['Dict[str,str]'] = None
    data_security_mode: Optional['DataSecurityMode'] = None
    docker_image: Optional['DockerImage'] = None
    driver_instance_pool_id: Optional[str] = None
    driver_node_type_id: Optional[str] = None
    enable_elastic_disk: Optional[bool] = None
    enable_local_disk_encryption: Optional[bool] = None
    gcp_attributes: Optional['GcpAttributes'] = None
    init_scripts: Optional['List[InitScriptInfo]'] = None
    instance_pool_id: Optional[str] = None
    node_type_id: Optional[str] = None
    num_workers: Optional[int] = None
    policy_id: Optional[str] = None
    runtime_engine: Optional['RuntimeEngine'] = None
    single_user_name: Optional[str] = None
    spark_conf: Optional['Dict[str,str]'] = None
    spark_env_vars: Optional['Dict[str,str]'] = None
    spark_version: Optional[str] = None
    ssh_public_keys: Optional['List[str]'] = None
    workload_type: Optional['WorkloadType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.apply_policy_default_values is not None:
            body['apply_policy_default_values'] = self.apply_policy_default_values
        if self.autoscale: body['autoscale'] = self.autoscale.as_dict()
        if self.autotermination_minutes is not None:
            body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.cluster_log_conf: body['cluster_log_conf'] = self.cluster_log_conf.as_dict()
        if self.cluster_name is not None: body['cluster_name'] = self.cluster_name
        if self.cluster_source is not None: body['cluster_source'] = self.cluster_source.value
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.data_security_mode is not None: body['data_security_mode'] = self.data_security_mode.value
        if self.docker_image: body['docker_image'] = self.docker_image.as_dict()
        if self.driver_instance_pool_id is not None:
            body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id is not None: body['driver_node_type_id'] = self.driver_node_type_id
        if self.enable_elastic_disk is not None: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption is not None:
            body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.init_scripts: body['init_scripts'] = [v.as_dict() for v in self.init_scripts]
        if self.instance_pool_id is not None: body['instance_pool_id'] = self.instance_pool_id
        if self.node_type_id is not None: body['node_type_id'] = self.node_type_id
        if self.num_workers is not None: body['num_workers'] = self.num_workers
        if self.policy_id is not None: body['policy_id'] = self.policy_id
        if self.runtime_engine is not None: body['runtime_engine'] = self.runtime_engine.value
        if self.single_user_name is not None: body['single_user_name'] = self.single_user_name
        if self.spark_conf: body['spark_conf'] = self.spark_conf
        if self.spark_env_vars: body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version is not None: body['spark_version'] = self.spark_version
        if self.ssh_public_keys: body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        if self.workload_type: body['workload_type'] = self.workload_type.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterSpec':
        return cls(apply_policy_default_values=d.get('apply_policy_default_values', None),
                   autoscale=_from_dict(d, 'autoscale', AutoScale),
                   autotermination_minutes=d.get('autotermination_minutes', None),
                   aws_attributes=_from_dict(d, 'aws_attributes', AwsAttributes),
                   azure_attributes=_from_dict(d, 'azure_attributes', AzureAttributes),
                   cluster_log_conf=_from_dict(d, 'cluster_log_conf', ClusterLogConf),
                   cluster_name=d.get('cluster_name', None),
                   cluster_source=_enum(d, 'cluster_source', ClusterSource),
                   custom_tags=d.get('custom_tags', None),
                   data_security_mode=_enum(d, 'data_security_mode', DataSecurityMode),
                   docker_image=_from_dict(d, 'docker_image', DockerImage),
                   driver_instance_pool_id=d.get('driver_instance_pool_id', None),
                   driver_node_type_id=d.get('driver_node_type_id', None),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
                   gcp_attributes=_from_dict(d, 'gcp_attributes', GcpAttributes),
                   init_scripts=_repeated(d, 'init_scripts', InitScriptInfo),
                   instance_pool_id=d.get('instance_pool_id', None),
                   node_type_id=d.get('node_type_id', None),
                   num_workers=d.get('num_workers', None),
                   policy_id=d.get('policy_id', None),
                   runtime_engine=_enum(d, 'runtime_engine', RuntimeEngine),
                   single_user_name=d.get('single_user_name', None),
                   spark_conf=d.get('spark_conf', None),
                   spark_env_vars=d.get('spark_env_vars', None),
                   spark_version=d.get('spark_version', None),
                   ssh_public_keys=d.get('ssh_public_keys', None),
                   workload_type=_from_dict(d, 'workload_type', WorkloadType))


@dataclass
class Command:
    cluster_id: Optional[str] = None
    command: Optional[str] = None
    context_id: Optional[str] = None
    language: Optional['Language'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['clusterId'] = self.cluster_id
        if self.command is not None: body['command'] = self.command
        if self.context_id is not None: body['contextId'] = self.context_id
        if self.language is not None: body['language'] = self.language.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Command':
        return cls(cluster_id=d.get('clusterId', None),
                   command=d.get('command', None),
                   context_id=d.get('contextId', None),
                   language=_enum(d, 'language', Language))


class CommandStatus(Enum):

    CANCELLED = 'Cancelled'
    CANCELLING = 'Cancelling'
    ERROR = 'Error'
    FINISHED = 'Finished'
    QUEUED = 'Queued'
    RUNNING = 'Running'


@dataclass
class CommandStatusResponse:
    id: Optional[str] = None
    results: Optional['Results'] = None
    status: Optional['CommandStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.id is not None: body['id'] = self.id
        if self.results: body['results'] = self.results.as_dict()
        if self.status is not None: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CommandStatusResponse':
        return cls(id=d.get('id', None),
                   results=_from_dict(d, 'results', Results),
                   status=_enum(d, 'status', CommandStatus))


@dataclass
class ComputeSpec:
    kind: Optional['ComputeSpecKind'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.kind is not None: body['kind'] = self.kind.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ComputeSpec':
        return cls(kind=_enum(d, 'kind', ComputeSpecKind))


class ComputeSpecKind(Enum):
    """The kind of compute described by this compute specification."""

    SERVERLESS_PREVIEW = 'SERVERLESS_PREVIEW'


class ContextStatus(Enum):

    ERROR = 'Error'
    PENDING = 'Pending'
    RUNNING = 'Running'


@dataclass
class ContextStatusResponse:
    id: Optional[str] = None
    status: Optional['ContextStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.id is not None: body['id'] = self.id
        if self.status is not None: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ContextStatusResponse':
        return cls(id=d.get('id', None), status=_enum(d, 'status', ContextStatus))


@dataclass
class CreateCluster:
    spark_version: str
    apply_policy_default_values: Optional[bool] = None
    autoscale: Optional['AutoScale'] = None
    autotermination_minutes: Optional[int] = None
    aws_attributes: Optional['AwsAttributes'] = None
    azure_attributes: Optional['AzureAttributes'] = None
    cluster_log_conf: Optional['ClusterLogConf'] = None
    cluster_name: Optional[str] = None
    cluster_source: Optional['ClusterSource'] = None
    custom_tags: Optional['Dict[str,str]'] = None
    data_security_mode: Optional['DataSecurityMode'] = None
    docker_image: Optional['DockerImage'] = None
    driver_instance_pool_id: Optional[str] = None
    driver_node_type_id: Optional[str] = None
    enable_elastic_disk: Optional[bool] = None
    enable_local_disk_encryption: Optional[bool] = None
    gcp_attributes: Optional['GcpAttributes'] = None
    init_scripts: Optional['List[InitScriptInfo]'] = None
    instance_pool_id: Optional[str] = None
    node_type_id: Optional[str] = None
    num_workers: Optional[int] = None
    policy_id: Optional[str] = None
    runtime_engine: Optional['RuntimeEngine'] = None
    single_user_name: Optional[str] = None
    spark_conf: Optional['Dict[str,str]'] = None
    spark_env_vars: Optional['Dict[str,str]'] = None
    ssh_public_keys: Optional['List[str]'] = None
    workload_type: Optional['WorkloadType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.apply_policy_default_values is not None:
            body['apply_policy_default_values'] = self.apply_policy_default_values
        if self.autoscale: body['autoscale'] = self.autoscale.as_dict()
        if self.autotermination_minutes is not None:
            body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.cluster_log_conf: body['cluster_log_conf'] = self.cluster_log_conf.as_dict()
        if self.cluster_name is not None: body['cluster_name'] = self.cluster_name
        if self.cluster_source is not None: body['cluster_source'] = self.cluster_source.value
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.data_security_mode is not None: body['data_security_mode'] = self.data_security_mode.value
        if self.docker_image: body['docker_image'] = self.docker_image.as_dict()
        if self.driver_instance_pool_id is not None:
            body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id is not None: body['driver_node_type_id'] = self.driver_node_type_id
        if self.enable_elastic_disk is not None: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption is not None:
            body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.init_scripts: body['init_scripts'] = [v.as_dict() for v in self.init_scripts]
        if self.instance_pool_id is not None: body['instance_pool_id'] = self.instance_pool_id
        if self.node_type_id is not None: body['node_type_id'] = self.node_type_id
        if self.num_workers is not None: body['num_workers'] = self.num_workers
        if self.policy_id is not None: body['policy_id'] = self.policy_id
        if self.runtime_engine is not None: body['runtime_engine'] = self.runtime_engine.value
        if self.single_user_name is not None: body['single_user_name'] = self.single_user_name
        if self.spark_conf: body['spark_conf'] = self.spark_conf
        if self.spark_env_vars: body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version is not None: body['spark_version'] = self.spark_version
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
                   data_security_mode=_enum(d, 'data_security_mode', DataSecurityMode),
                   docker_image=_from_dict(d, 'docker_image', DockerImage),
                   driver_instance_pool_id=d.get('driver_instance_pool_id', None),
                   driver_node_type_id=d.get('driver_node_type_id', None),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
                   gcp_attributes=_from_dict(d, 'gcp_attributes', GcpAttributes),
                   init_scripts=_repeated(d, 'init_scripts', InitScriptInfo),
                   instance_pool_id=d.get('instance_pool_id', None),
                   node_type_id=d.get('node_type_id', None),
                   num_workers=d.get('num_workers', None),
                   policy_id=d.get('policy_id', None),
                   runtime_engine=_enum(d, 'runtime_engine', RuntimeEngine),
                   single_user_name=d.get('single_user_name', None),
                   spark_conf=d.get('spark_conf', None),
                   spark_env_vars=d.get('spark_env_vars', None),
                   spark_version=d.get('spark_version', None),
                   ssh_public_keys=d.get('ssh_public_keys', None),
                   workload_type=_from_dict(d, 'workload_type', WorkloadType))


@dataclass
class CreateClusterResponse:
    cluster_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateClusterResponse':
        return cls(cluster_id=d.get('cluster_id', None))


@dataclass
class CreateContext:
    cluster_id: Optional[str] = None
    language: Optional['Language'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['clusterId'] = self.cluster_id
        if self.language is not None: body['language'] = self.language.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateContext':
        return cls(cluster_id=d.get('clusterId', None), language=_enum(d, 'language', Language))


@dataclass
class CreateInstancePool:
    instance_pool_name: str
    node_type_id: str
    aws_attributes: Optional['InstancePoolAwsAttributes'] = None
    azure_attributes: Optional['InstancePoolAzureAttributes'] = None
    custom_tags: Optional['Dict[str,str]'] = None
    disk_spec: Optional['DiskSpec'] = None
    enable_elastic_disk: Optional[bool] = None
    gcp_attributes: Optional['InstancePoolGcpAttributes'] = None
    idle_instance_autotermination_minutes: Optional[int] = None
    max_capacity: Optional[int] = None
    min_idle_instances: Optional[int] = None
    preloaded_docker_images: Optional['List[DockerImage]'] = None
    preloaded_spark_versions: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.disk_spec: body['disk_spec'] = self.disk_spec.as_dict()
        if self.enable_elastic_disk is not None: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.idle_instance_autotermination_minutes is not None:
            body['idle_instance_autotermination_minutes'] = self.idle_instance_autotermination_minutes
        if self.instance_pool_name is not None: body['instance_pool_name'] = self.instance_pool_name
        if self.max_capacity is not None: body['max_capacity'] = self.max_capacity
        if self.min_idle_instances is not None: body['min_idle_instances'] = self.min_idle_instances
        if self.node_type_id is not None: body['node_type_id'] = self.node_type_id
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
                   gcp_attributes=_from_dict(d, 'gcp_attributes', InstancePoolGcpAttributes),
                   idle_instance_autotermination_minutes=d.get('idle_instance_autotermination_minutes', None),
                   instance_pool_name=d.get('instance_pool_name', None),
                   max_capacity=d.get('max_capacity', None),
                   min_idle_instances=d.get('min_idle_instances', None),
                   node_type_id=d.get('node_type_id', None),
                   preloaded_docker_images=_repeated(d, 'preloaded_docker_images', DockerImage),
                   preloaded_spark_versions=d.get('preloaded_spark_versions', None))


@dataclass
class CreateInstancePoolResponse:
    instance_pool_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.instance_pool_id is not None: body['instance_pool_id'] = self.instance_pool_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateInstancePoolResponse':
        return cls(instance_pool_id=d.get('instance_pool_id', None))


@dataclass
class CreatePolicy:
    name: str
    definition: Optional[str] = None
    description: Optional[str] = None
    max_clusters_per_user: Optional[int] = None
    policy_family_definition_overrides: Optional[str] = None
    policy_family_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.definition is not None: body['definition'] = self.definition
        if self.description is not None: body['description'] = self.description
        if self.max_clusters_per_user is not None: body['max_clusters_per_user'] = self.max_clusters_per_user
        if self.name is not None: body['name'] = self.name
        if self.policy_family_definition_overrides is not None:
            body['policy_family_definition_overrides'] = self.policy_family_definition_overrides
        if self.policy_family_id is not None: body['policy_family_id'] = self.policy_family_id
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
    policy_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.policy_id is not None: body['policy_id'] = self.policy_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePolicyResponse':
        return cls(policy_id=d.get('policy_id', None))


@dataclass
class CreateResponse:
    script_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.script_id is not None: body['script_id'] = self.script_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateResponse':
        return cls(script_id=d.get('script_id', None))


@dataclass
class Created:
    id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.id is not None: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Created':
        return cls(id=d.get('id', None))


@dataclass
class DataPlaneEventDetails:
    event_type: Optional['DataPlaneEventDetailsEventType'] = None
    executor_failures: Optional[int] = None
    host_id: Optional[str] = None
    timestamp: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.event_type is not None: body['event_type'] = self.event_type.value
        if self.executor_failures is not None: body['executor_failures'] = self.executor_failures
        if self.host_id is not None: body['host_id'] = self.host_id
        if self.timestamp is not None: body['timestamp'] = self.timestamp
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
    """Data security mode decides what data governance model to use when accessing data from a cluster.
    
    * `NONE`: No security isolation for multiple users sharing the cluster. Data governance features
    are not available in this mode. * `SINGLE_USER`: A secure cluster that can only be exclusively
    used by a single user specified in `single_user_name`. Most programming languages, cluster
    features and data governance features are available in this mode. * `USER_ISOLATION`: A secure
    cluster that can be shared by multiple users. Cluster users are fully isolated so that they
    cannot see each other's data and credentials. Most data governance features are supported in
    this mode. But programming languages and cluster features might be limited. *
    `LEGACY_TABLE_ACL`: This mode is for users migrating from legacy Table ACL clusters. *
    `LEGACY_PASSTHROUGH`: This mode is for users migrating from legacy Passthrough on high
    concurrency clusters. * `LEGACY_SINGLE_USER`: This mode is for users migrating from legacy
    Passthrough on standard clusters."""

    LEGACY_PASSTHROUGH = 'LEGACY_PASSTHROUGH'
    LEGACY_SINGLE_USER = 'LEGACY_SINGLE_USER'
    LEGACY_TABLE_ACL = 'LEGACY_TABLE_ACL'
    NONE = 'NONE'
    SINGLE_USER = 'SINGLE_USER'
    USER_ISOLATION = 'USER_ISOLATION'


@dataclass
class DbfsStorageInfo:
    destination: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.destination is not None: body['destination'] = self.destination
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DbfsStorageInfo':
        return cls(destination=d.get('destination', None))


@dataclass
class DeleteCluster:
    cluster_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteCluster':
        return cls(cluster_id=d.get('cluster_id', None))


@dataclass
class DeleteInstancePool:
    instance_pool_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.instance_pool_id is not None: body['instance_pool_id'] = self.instance_pool_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteInstancePool':
        return cls(instance_pool_id=d.get('instance_pool_id', None))


@dataclass
class DeletePolicy:
    policy_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.policy_id is not None: body['policy_id'] = self.policy_id
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
        if self.cluster_id is not None: body['clusterId'] = self.cluster_id
        if self.context_id is not None: body['contextId'] = self.context_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DestroyContext':
        return cls(cluster_id=d.get('clusterId', None), context_id=d.get('contextId', None))


@dataclass
class DiskSpec:
    disk_count: Optional[int] = None
    disk_iops: Optional[int] = None
    disk_size: Optional[int] = None
    disk_throughput: Optional[int] = None
    disk_type: Optional['DiskType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.disk_count is not None: body['disk_count'] = self.disk_count
        if self.disk_iops is not None: body['disk_iops'] = self.disk_iops
        if self.disk_size is not None: body['disk_size'] = self.disk_size
        if self.disk_throughput is not None: body['disk_throughput'] = self.disk_throughput
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
    azure_disk_volume_type: Optional['DiskTypeAzureDiskVolumeType'] = None
    ebs_volume_type: Optional['DiskTypeEbsVolumeType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.azure_disk_volume_type is not None:
            body['azure_disk_volume_type'] = self.azure_disk_volume_type.value
        if self.ebs_volume_type is not None: body['ebs_volume_type'] = self.ebs_volume_type.value
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
    password: Optional[str] = None
    username: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.password is not None: body['password'] = self.password
        if self.username is not None: body['username'] = self.username
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DockerBasicAuth':
        return cls(password=d.get('password', None), username=d.get('username', None))


@dataclass
class DockerImage:
    basic_auth: Optional['DockerBasicAuth'] = None
    url: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.basic_auth: body['basic_auth'] = self.basic_auth.as_dict()
        if self.url is not None: body['url'] = self.url
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
    apply_policy_default_values: Optional[bool] = None
    autoscale: Optional['AutoScale'] = None
    autotermination_minutes: Optional[int] = None
    aws_attributes: Optional['AwsAttributes'] = None
    azure_attributes: Optional['AzureAttributes'] = None
    cluster_log_conf: Optional['ClusterLogConf'] = None
    cluster_name: Optional[str] = None
    cluster_source: Optional['ClusterSource'] = None
    custom_tags: Optional['Dict[str,str]'] = None
    data_security_mode: Optional['DataSecurityMode'] = None
    docker_image: Optional['DockerImage'] = None
    driver_instance_pool_id: Optional[str] = None
    driver_node_type_id: Optional[str] = None
    enable_elastic_disk: Optional[bool] = None
    enable_local_disk_encryption: Optional[bool] = None
    gcp_attributes: Optional['GcpAttributes'] = None
    init_scripts: Optional['List[InitScriptInfo]'] = None
    instance_pool_id: Optional[str] = None
    node_type_id: Optional[str] = None
    num_workers: Optional[int] = None
    policy_id: Optional[str] = None
    runtime_engine: Optional['RuntimeEngine'] = None
    single_user_name: Optional[str] = None
    spark_conf: Optional['Dict[str,str]'] = None
    spark_env_vars: Optional['Dict[str,str]'] = None
    ssh_public_keys: Optional['List[str]'] = None
    workload_type: Optional['WorkloadType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.apply_policy_default_values is not None:
            body['apply_policy_default_values'] = self.apply_policy_default_values
        if self.autoscale: body['autoscale'] = self.autoscale.as_dict()
        if self.autotermination_minutes is not None:
            body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.cluster_log_conf: body['cluster_log_conf'] = self.cluster_log_conf.as_dict()
        if self.cluster_name is not None: body['cluster_name'] = self.cluster_name
        if self.cluster_source is not None: body['cluster_source'] = self.cluster_source.value
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.data_security_mode is not None: body['data_security_mode'] = self.data_security_mode.value
        if self.docker_image: body['docker_image'] = self.docker_image.as_dict()
        if self.driver_instance_pool_id is not None:
            body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id is not None: body['driver_node_type_id'] = self.driver_node_type_id
        if self.enable_elastic_disk is not None: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption is not None:
            body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.init_scripts: body['init_scripts'] = [v.as_dict() for v in self.init_scripts]
        if self.instance_pool_id is not None: body['instance_pool_id'] = self.instance_pool_id
        if self.node_type_id is not None: body['node_type_id'] = self.node_type_id
        if self.num_workers is not None: body['num_workers'] = self.num_workers
        if self.policy_id is not None: body['policy_id'] = self.policy_id
        if self.runtime_engine is not None: body['runtime_engine'] = self.runtime_engine.value
        if self.single_user_name is not None: body['single_user_name'] = self.single_user_name
        if self.spark_conf: body['spark_conf'] = self.spark_conf
        if self.spark_env_vars: body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version is not None: body['spark_version'] = self.spark_version
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
                   data_security_mode=_enum(d, 'data_security_mode', DataSecurityMode),
                   docker_image=_from_dict(d, 'docker_image', DockerImage),
                   driver_instance_pool_id=d.get('driver_instance_pool_id', None),
                   driver_node_type_id=d.get('driver_node_type_id', None),
                   enable_elastic_disk=d.get('enable_elastic_disk', None),
                   enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
                   gcp_attributes=_from_dict(d, 'gcp_attributes', GcpAttributes),
                   init_scripts=_repeated(d, 'init_scripts', InitScriptInfo),
                   instance_pool_id=d.get('instance_pool_id', None),
                   node_type_id=d.get('node_type_id', None),
                   num_workers=d.get('num_workers', None),
                   policy_id=d.get('policy_id', None),
                   runtime_engine=_enum(d, 'runtime_engine', RuntimeEngine),
                   single_user_name=d.get('single_user_name', None),
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
    custom_tags: Optional['Dict[str,str]'] = None
    idle_instance_autotermination_minutes: Optional[int] = None
    max_capacity: Optional[int] = None
    min_idle_instances: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.idle_instance_autotermination_minutes is not None:
            body['idle_instance_autotermination_minutes'] = self.idle_instance_autotermination_minutes
        if self.instance_pool_id is not None: body['instance_pool_id'] = self.instance_pool_id
        if self.instance_pool_name is not None: body['instance_pool_name'] = self.instance_pool_name
        if self.max_capacity is not None: body['max_capacity'] = self.max_capacity
        if self.min_idle_instances is not None: body['min_idle_instances'] = self.min_idle_instances
        if self.node_type_id is not None: body['node_type_id'] = self.node_type_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditInstancePool':
        return cls(custom_tags=d.get('custom_tags', None),
                   idle_instance_autotermination_minutes=d.get('idle_instance_autotermination_minutes', None),
                   instance_pool_id=d.get('instance_pool_id', None),
                   instance_pool_name=d.get('instance_pool_name', None),
                   max_capacity=d.get('max_capacity', None),
                   min_idle_instances=d.get('min_idle_instances', None),
                   node_type_id=d.get('node_type_id', None))


@dataclass
class EditPolicy:
    policy_id: str
    name: str
    definition: Optional[str] = None
    description: Optional[str] = None
    max_clusters_per_user: Optional[int] = None
    policy_family_definition_overrides: Optional[str] = None
    policy_family_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.definition is not None: body['definition'] = self.definition
        if self.description is not None: body['description'] = self.description
        if self.max_clusters_per_user is not None: body['max_clusters_per_user'] = self.max_clusters_per_user
        if self.name is not None: body['name'] = self.name
        if self.policy_family_definition_overrides is not None:
            body['policy_family_definition_overrides'] = self.policy_family_definition_overrides
        if self.policy_family_id is not None: body['policy_family_id'] = self.policy_family_id
        if self.policy_id is not None: body['policy_id'] = self.policy_id
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
    attributes: Optional['ClusterAttributes'] = None
    cause: Optional['EventDetailsCause'] = None
    cluster_size: Optional['ClusterSize'] = None
    current_num_vcpus: Optional[int] = None
    current_num_workers: Optional[int] = None
    did_not_expand_reason: Optional[str] = None
    disk_size: Optional[int] = None
    driver_state_message: Optional[str] = None
    enable_termination_for_node_blocklisted: Optional[bool] = None
    free_space: Optional[int] = None
    instance_id: Optional[str] = None
    job_run_name: Optional[str] = None
    previous_attributes: Optional['ClusterAttributes'] = None
    previous_cluster_size: Optional['ClusterSize'] = None
    previous_disk_size: Optional[int] = None
    reason: Optional['TerminationReason'] = None
    target_num_vcpus: Optional[int] = None
    target_num_workers: Optional[int] = None
    user: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.attributes: body['attributes'] = self.attributes.as_dict()
        if self.cause is not None: body['cause'] = self.cause.value
        if self.cluster_size: body['cluster_size'] = self.cluster_size.as_dict()
        if self.current_num_vcpus is not None: body['current_num_vcpus'] = self.current_num_vcpus
        if self.current_num_workers is not None: body['current_num_workers'] = self.current_num_workers
        if self.did_not_expand_reason is not None: body['did_not_expand_reason'] = self.did_not_expand_reason
        if self.disk_size is not None: body['disk_size'] = self.disk_size
        if self.driver_state_message is not None: body['driver_state_message'] = self.driver_state_message
        if self.enable_termination_for_node_blocklisted is not None:
            body['enable_termination_for_node_blocklisted'] = self.enable_termination_for_node_blocklisted
        if self.free_space is not None: body['free_space'] = self.free_space
        if self.instance_id is not None: body['instance_id'] = self.instance_id
        if self.job_run_name is not None: body['job_run_name'] = self.job_run_name
        if self.previous_attributes: body['previous_attributes'] = self.previous_attributes.as_dict()
        if self.previous_cluster_size: body['previous_cluster_size'] = self.previous_cluster_size.as_dict()
        if self.previous_disk_size is not None: body['previous_disk_size'] = self.previous_disk_size
        if self.reason: body['reason'] = self.reason.as_dict()
        if self.target_num_vcpus is not None: body['target_num_vcpus'] = self.target_num_vcpus
        if self.target_num_workers is not None: body['target_num_workers'] = self.target_num_workers
        if self.user is not None: body['user'] = self.user
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
    NODES_LOST = 'NODES_LOST'
    NODE_BLACKLISTED = 'NODE_BLACKLISTED'
    NODE_EXCLUDED_DECOMMISSIONED = 'NODE_EXCLUDED_DECOMMISSIONED'
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
    availability: Optional['GcpAvailability'] = None
    boot_disk_size: Optional[int] = None
    google_service_account: Optional[str] = None
    local_ssd_count: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.availability is not None: body['availability'] = self.availability.value
        if self.boot_disk_size is not None: body['boot_disk_size'] = self.boot_disk_size
        if self.google_service_account is not None:
            body['google_service_account'] = self.google_service_account
        if self.local_ssd_count is not None: body['local_ssd_count'] = self.local_ssd_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GcpAttributes':
        return cls(availability=_enum(d, 'availability', GcpAvailability),
                   boot_disk_size=d.get('boot_disk_size', None),
                   google_service_account=d.get('google_service_account', None),
                   local_ssd_count=d.get('local_ssd_count', None))


class GcpAvailability(Enum):
    """This field determines whether the instance pool will contain preemptible VMs, on-demand VMs, or
    preemptible VMs with a fallback to on-demand VMs if the former is unavailable."""

    ON_DEMAND_GCP = 'ON_DEMAND_GCP'
    PREEMPTIBLE_GCP = 'PREEMPTIBLE_GCP'
    PREEMPTIBLE_WITH_FALLBACK_GCP = 'PREEMPTIBLE_WITH_FALLBACK_GCP'


@dataclass
class GetClusterPermissionLevelsResponse:
    permission_levels: Optional['List[ClusterPermissionsDescription]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetClusterPermissionLevelsResponse':
        return cls(permission_levels=_repeated(d, 'permission_levels', ClusterPermissionsDescription))


@dataclass
class GetClusterPolicyPermissionLevelsResponse:
    permission_levels: Optional['List[ClusterPolicyPermissionsDescription]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetClusterPolicyPermissionLevelsResponse':
        return cls(permission_levels=_repeated(d, 'permission_levels', ClusterPolicyPermissionsDescription))


@dataclass
class GetEvents:
    cluster_id: str
    end_time: Optional[int] = None
    event_types: Optional['List[EventType]'] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    order: Optional['GetEventsOrder'] = None
    start_time: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.end_time is not None: body['end_time'] = self.end_time
        if self.event_types: body['event_types'] = [v.value for v in self.event_types]
        if self.limit is not None: body['limit'] = self.limit
        if self.offset is not None: body['offset'] = self.offset
        if self.order is not None: body['order'] = self.order.value
        if self.start_time is not None: body['start_time'] = self.start_time
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
    events: Optional['List[ClusterEvent]'] = None
    next_page: Optional['GetEvents'] = None
    total_count: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.events: body['events'] = [v.as_dict() for v in self.events]
        if self.next_page: body['next_page'] = self.next_page.as_dict()
        if self.total_count is not None: body['total_count'] = self.total_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetEventsResponse':
        return cls(events=_repeated(d, 'events', ClusterEvent),
                   next_page=_from_dict(d, 'next_page', GetEvents),
                   total_count=d.get('total_count', None))


@dataclass
class GetInstancePool:
    instance_pool_id: str
    aws_attributes: Optional['InstancePoolAwsAttributes'] = None
    azure_attributes: Optional['InstancePoolAzureAttributes'] = None
    custom_tags: Optional['Dict[str,str]'] = None
    default_tags: Optional['Dict[str,str]'] = None
    disk_spec: Optional['DiskSpec'] = None
    enable_elastic_disk: Optional[bool] = None
    gcp_attributes: Optional['InstancePoolGcpAttributes'] = None
    idle_instance_autotermination_minutes: Optional[int] = None
    instance_pool_name: Optional[str] = None
    max_capacity: Optional[int] = None
    min_idle_instances: Optional[int] = None
    node_type_id: Optional[str] = None
    preloaded_docker_images: Optional['List[DockerImage]'] = None
    preloaded_spark_versions: Optional['List[str]'] = None
    state: Optional['InstancePoolState'] = None
    stats: Optional['InstancePoolStats'] = None
    status: Optional['InstancePoolStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.default_tags: body['default_tags'] = self.default_tags
        if self.disk_spec: body['disk_spec'] = self.disk_spec.as_dict()
        if self.enable_elastic_disk is not None: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.idle_instance_autotermination_minutes is not None:
            body['idle_instance_autotermination_minutes'] = self.idle_instance_autotermination_minutes
        if self.instance_pool_id is not None: body['instance_pool_id'] = self.instance_pool_id
        if self.instance_pool_name is not None: body['instance_pool_name'] = self.instance_pool_name
        if self.max_capacity is not None: body['max_capacity'] = self.max_capacity
        if self.min_idle_instances is not None: body['min_idle_instances'] = self.min_idle_instances
        if self.node_type_id is not None: body['node_type_id'] = self.node_type_id
        if self.preloaded_docker_images:
            body['preloaded_docker_images'] = [v.as_dict() for v in self.preloaded_docker_images]
        if self.preloaded_spark_versions:
            body['preloaded_spark_versions'] = [v for v in self.preloaded_spark_versions]
        if self.state is not None: body['state'] = self.state.value
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
                   gcp_attributes=_from_dict(d, 'gcp_attributes', InstancePoolGcpAttributes),
                   idle_instance_autotermination_minutes=d.get('idle_instance_autotermination_minutes', None),
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
class GetInstancePoolPermissionLevelsResponse:
    permission_levels: Optional['List[InstancePoolPermissionsDescription]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetInstancePoolPermissionLevelsResponse':
        return cls(permission_levels=_repeated(d, 'permission_levels', InstancePoolPermissionsDescription))


@dataclass
class GetSparkVersionsResponse:
    versions: Optional['List[SparkVersion]'] = None

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
    enabled: Optional[bool] = None
    position: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.name is not None: body['name'] = self.name
        if self.position is not None: body['position'] = self.position
        if self.script is not None: body['script'] = self.script
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptCreateRequest':
        return cls(enabled=d.get('enabled', None),
                   name=d.get('name', None),
                   position=d.get('position', None),
                   script=d.get('script', None))


@dataclass
class GlobalInitScriptDetails:
    created_at: Optional[int] = None
    created_by: Optional[str] = None
    enabled: Optional[bool] = None
    name: Optional[str] = None
    position: Optional[int] = None
    script_id: Optional[str] = None
    updated_at: Optional[int] = None
    updated_by: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.name is not None: body['name'] = self.name
        if self.position is not None: body['position'] = self.position
        if self.script_id is not None: body['script_id'] = self.script_id
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
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
    created_at: Optional[int] = None
    created_by: Optional[str] = None
    enabled: Optional[bool] = None
    name: Optional[str] = None
    position: Optional[int] = None
    script: Optional[str] = None
    script_id: Optional[str] = None
    updated_at: Optional[int] = None
    updated_by: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.name is not None: body['name'] = self.name
        if self.position is not None: body['position'] = self.position
        if self.script is not None: body['script'] = self.script
        if self.script_id is not None: body['script_id'] = self.script_id
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
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
    enabled: Optional[bool] = None
    position: Optional[int] = None
    script_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.name is not None: body['name'] = self.name
        if self.position is not None: body['position'] = self.position
        if self.script is not None: body['script'] = self.script
        if self.script_id is not None: body['script_id'] = self.script_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptUpdateRequest':
        return cls(enabled=d.get('enabled', None),
                   name=d.get('name', None),
                   position=d.get('position', None),
                   script=d.get('script', None),
                   script_id=d.get('script_id', None))


@dataclass
class InitScriptInfo:
    dbfs: Optional['DbfsStorageInfo'] = None
    s3: Optional['S3StorageInfo'] = None
    volumes: Optional['VolumesStorageInfo'] = None
    workspace: Optional['WorkspaceStorageInfo'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.dbfs: body['dbfs'] = self.dbfs.as_dict()
        if self.s3: body['s3'] = self.s3.as_dict()
        if self.volumes: body['volumes'] = self.volumes.as_dict()
        if self.workspace: body['workspace'] = self.workspace.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InitScriptInfo':
        return cls(dbfs=_from_dict(d, 'dbfs', DbfsStorageInfo),
                   s3=_from_dict(d, 's3', S3StorageInfo),
                   volumes=_from_dict(d, 'volumes', VolumesStorageInfo),
                   workspace=_from_dict(d, 'workspace', WorkspaceStorageInfo))


@dataclass
class InstallLibraries:
    cluster_id: str
    libraries: 'List[Library]'

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstallLibraries':
        return cls(cluster_id=d.get('cluster_id', None), libraries=_repeated(d, 'libraries', Library))


@dataclass
class InstancePoolAccessControlRequest:
    group_name: Optional[str] = None
    permission_level: Optional['InstancePoolPermissionLevel'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolAccessControlRequest':
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', InstancePoolPermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class InstancePoolAccessControlResponse:
    all_permissions: Optional['List[InstancePoolPermission]'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolAccessControlResponse':
        return cls(all_permissions=_repeated(d, 'all_permissions', InstancePoolPermission),
                   display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class InstancePoolAndStats:
    aws_attributes: Optional['InstancePoolAwsAttributes'] = None
    azure_attributes: Optional['InstancePoolAzureAttributes'] = None
    custom_tags: Optional['Dict[str,str]'] = None
    default_tags: Optional['Dict[str,str]'] = None
    disk_spec: Optional['DiskSpec'] = None
    enable_elastic_disk: Optional[bool] = None
    gcp_attributes: Optional['InstancePoolGcpAttributes'] = None
    idle_instance_autotermination_minutes: Optional[int] = None
    instance_pool_id: Optional[str] = None
    instance_pool_name: Optional[str] = None
    max_capacity: Optional[int] = None
    min_idle_instances: Optional[int] = None
    node_type_id: Optional[str] = None
    preloaded_docker_images: Optional['List[DockerImage]'] = None
    preloaded_spark_versions: Optional['List[str]'] = None
    state: Optional['InstancePoolState'] = None
    stats: Optional['InstancePoolStats'] = None
    status: Optional['InstancePoolStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.aws_attributes: body['aws_attributes'] = self.aws_attributes.as_dict()
        if self.azure_attributes: body['azure_attributes'] = self.azure_attributes.as_dict()
        if self.custom_tags: body['custom_tags'] = self.custom_tags
        if self.default_tags: body['default_tags'] = self.default_tags
        if self.disk_spec: body['disk_spec'] = self.disk_spec.as_dict()
        if self.enable_elastic_disk is not None: body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.gcp_attributes: body['gcp_attributes'] = self.gcp_attributes.as_dict()
        if self.idle_instance_autotermination_minutes is not None:
            body['idle_instance_autotermination_minutes'] = self.idle_instance_autotermination_minutes
        if self.instance_pool_id is not None: body['instance_pool_id'] = self.instance_pool_id
        if self.instance_pool_name is not None: body['instance_pool_name'] = self.instance_pool_name
        if self.max_capacity is not None: body['max_capacity'] = self.max_capacity
        if self.min_idle_instances is not None: body['min_idle_instances'] = self.min_idle_instances
        if self.node_type_id is not None: body['node_type_id'] = self.node_type_id
        if self.preloaded_docker_images:
            body['preloaded_docker_images'] = [v.as_dict() for v in self.preloaded_docker_images]
        if self.preloaded_spark_versions:
            body['preloaded_spark_versions'] = [v for v in self.preloaded_spark_versions]
        if self.state is not None: body['state'] = self.state.value
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
                   gcp_attributes=_from_dict(d, 'gcp_attributes', InstancePoolGcpAttributes),
                   idle_instance_autotermination_minutes=d.get('idle_instance_autotermination_minutes', None),
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
    availability: Optional['InstancePoolAwsAttributesAvailability'] = None
    spot_bid_price_percent: Optional[int] = None
    zone_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.availability is not None: body['availability'] = self.availability.value
        if self.spot_bid_price_percent is not None:
            body['spot_bid_price_percent'] = self.spot_bid_price_percent
        if self.zone_id is not None: body['zone_id'] = self.zone_id
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


@dataclass
class InstancePoolAzureAttributes:
    availability: Optional['InstancePoolAzureAttributesAvailability'] = None
    spot_bid_max_price: Optional[float] = None

    def as_dict(self) -> dict:
        body = {}
        if self.availability is not None: body['availability'] = self.availability.value
        if self.spot_bid_max_price is not None: body['spot_bid_max_price'] = self.spot_bid_max_price
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


@dataclass
class InstancePoolGcpAttributes:
    gcp_availability: Optional['GcpAvailability'] = None
    local_ssd_count: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.gcp_availability is not None: body['gcp_availability'] = self.gcp_availability.value
        if self.local_ssd_count is not None: body['local_ssd_count'] = self.local_ssd_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolGcpAttributes':
        return cls(gcp_availability=_enum(d, 'gcp_availability', GcpAvailability),
                   local_ssd_count=d.get('local_ssd_count', None))


@dataclass
class InstancePoolPermission:
    inherited: Optional[bool] = None
    inherited_from_object: Optional['List[str]'] = None
    permission_level: Optional['InstancePoolPermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolPermission':
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', InstancePoolPermissionLevel))


class InstancePoolPermissionLevel(Enum):
    """Permission level"""

    CAN_ATTACH_TO = 'CAN_ATTACH_TO'
    CAN_MANAGE = 'CAN_MANAGE'


@dataclass
class InstancePoolPermissions:
    access_control_list: Optional['List[InstancePoolAccessControlResponse]'] = None
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
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolPermissions':
        return cls(access_control_list=_repeated(d, 'access_control_list', InstancePoolAccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class InstancePoolPermissionsDescription:
    description: Optional[str] = None
    permission_level: Optional['InstancePoolPermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolPermissionsDescription':
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', InstancePoolPermissionLevel))


@dataclass
class InstancePoolPermissionsRequest:
    access_control_list: Optional['List[InstancePoolAccessControlRequest]'] = None
    instance_pool_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.instance_pool_id is not None: body['instance_pool_id'] = self.instance_pool_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolPermissionsRequest':
        return cls(access_control_list=_repeated(d, 'access_control_list', InstancePoolAccessControlRequest),
                   instance_pool_id=d.get('instance_pool_id', None))


class InstancePoolState(Enum):
    """Current state of the instance pool."""

    ACTIVE = 'ACTIVE'
    DELETED = 'DELETED'
    STOPPED = 'STOPPED'


@dataclass
class InstancePoolStats:
    idle_count: Optional[int] = None
    pending_idle_count: Optional[int] = None
    pending_used_count: Optional[int] = None
    used_count: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.idle_count is not None: body['idle_count'] = self.idle_count
        if self.pending_idle_count is not None: body['pending_idle_count'] = self.pending_idle_count
        if self.pending_used_count is not None: body['pending_used_count'] = self.pending_used_count
        if self.used_count is not None: body['used_count'] = self.used_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolStats':
        return cls(idle_count=d.get('idle_count', None),
                   pending_idle_count=d.get('pending_idle_count', None),
                   pending_used_count=d.get('pending_used_count', None),
                   used_count=d.get('used_count', None))


@dataclass
class InstancePoolStatus:
    pending_instance_errors: Optional['List[PendingInstanceError]'] = None

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
    iam_role_arn: Optional[str] = None
    is_meta_instance_profile: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.iam_role_arn is not None: body['iam_role_arn'] = self.iam_role_arn
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.is_meta_instance_profile is not None:
            body['is_meta_instance_profile'] = self.is_meta_instance_profile
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstanceProfile':
        return cls(iam_role_arn=d.get('iam_role_arn', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   is_meta_instance_profile=d.get('is_meta_instance_profile', None))


class Language(Enum):

    PYTHON = 'python'
    SCALA = 'scala'
    SQL = 'sql'


@dataclass
class Library:
    cran: Optional['RCranLibrary'] = None
    egg: Optional[str] = None
    jar: Optional[str] = None
    maven: Optional['MavenLibrary'] = None
    pypi: Optional['PythonPyPiLibrary'] = None
    whl: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cran: body['cran'] = self.cran.as_dict()
        if self.egg is not None: body['egg'] = self.egg
        if self.jar is not None: body['jar'] = self.jar
        if self.maven: body['maven'] = self.maven.as_dict()
        if self.pypi: body['pypi'] = self.pypi.as_dict()
        if self.whl is not None: body['whl'] = self.whl
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
    is_library_for_all_clusters: Optional[bool] = None
    library: Optional['Library'] = None
    messages: Optional['List[str]'] = None
    status: Optional['LibraryFullStatusStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.is_library_for_all_clusters is not None:
            body['is_library_for_all_clusters'] = self.is_library_for_all_clusters
        if self.library: body['library'] = self.library.as_dict()
        if self.messages: body['messages'] = [v for v in self.messages]
        if self.status is not None: body['status'] = self.status.value
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
    statuses: Optional['List[ClusterLibraryStatuses]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.statuses: body['statuses'] = [v.as_dict() for v in self.statuses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListAllClusterLibraryStatusesResponse':
        return cls(statuses=_repeated(d, 'statuses', ClusterLibraryStatuses))


@dataclass
class ListAvailableZonesResponse:
    default_zone: Optional[str] = None
    zones: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.default_zone is not None: body['default_zone'] = self.default_zone
        if self.zones: body['zones'] = [v for v in self.zones]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListAvailableZonesResponse':
        return cls(default_zone=d.get('default_zone', None), zones=d.get('zones', None))


@dataclass
class ListClustersResponse:
    clusters: Optional['List[ClusterDetails]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.clusters: body['clusters'] = [v.as_dict() for v in self.clusters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListClustersResponse':
        return cls(clusters=_repeated(d, 'clusters', ClusterDetails))


@dataclass
class ListGlobalInitScriptsResponse:
    scripts: Optional['List[GlobalInitScriptDetails]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.scripts: body['scripts'] = [v.as_dict() for v in self.scripts]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListGlobalInitScriptsResponse':
        return cls(scripts=_repeated(d, 'scripts', GlobalInitScriptDetails))


@dataclass
class ListInstancePools:
    instance_pools: Optional['List[InstancePoolAndStats]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.instance_pools: body['instance_pools'] = [v.as_dict() for v in self.instance_pools]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListInstancePools':
        return cls(instance_pools=_repeated(d, 'instance_pools', InstancePoolAndStats))


@dataclass
class ListInstanceProfilesResponse:
    instance_profiles: Optional['List[InstanceProfile]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.instance_profiles: body['instance_profiles'] = [v.as_dict() for v in self.instance_profiles]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListInstanceProfilesResponse':
        return cls(instance_profiles=_repeated(d, 'instance_profiles', InstanceProfile))


@dataclass
class ListNodeTypesResponse:
    node_types: Optional['List[NodeType]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.node_types: body['node_types'] = [v.as_dict() for v in self.node_types]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListNodeTypesResponse':
        return cls(node_types=_repeated(d, 'node_types', NodeType))


@dataclass
class ListPoliciesResponse:
    policies: Optional['List[Policy]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.policies: body['policies'] = [v.as_dict() for v in self.policies]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListPoliciesResponse':
        return cls(policies=_repeated(d, 'policies', Policy))


@dataclass
class ListPolicyFamiliesResponse:
    policy_families: 'List[PolicyFamily]'
    next_page_token: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
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
    log_analytics_primary_key: Optional[str] = None
    log_analytics_workspace_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.log_analytics_primary_key is not None:
            body['log_analytics_primary_key'] = self.log_analytics_primary_key
        if self.log_analytics_workspace_id is not None:
            body['log_analytics_workspace_id'] = self.log_analytics_workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogAnalyticsInfo':
        return cls(log_analytics_primary_key=d.get('log_analytics_primary_key', None),
                   log_analytics_workspace_id=d.get('log_analytics_workspace_id', None))


@dataclass
class LogSyncStatus:
    last_attempted: Optional[int] = None
    last_exception: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.last_attempted is not None: body['last_attempted'] = self.last_attempted
        if self.last_exception is not None: body['last_exception'] = self.last_exception
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogSyncStatus':
        return cls(last_attempted=d.get('last_attempted', None), last_exception=d.get('last_exception', None))


@dataclass
class MavenLibrary:
    coordinates: str
    exclusions: Optional['List[str]'] = None
    repo: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.coordinates is not None: body['coordinates'] = self.coordinates
        if self.exclusions: body['exclusions'] = [v for v in self.exclusions]
        if self.repo is not None: body['repo'] = self.repo
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'MavenLibrary':
        return cls(coordinates=d.get('coordinates', None),
                   exclusions=d.get('exclusions', None),
                   repo=d.get('repo', None))


@dataclass
class NodeInstanceType:
    instance_type_id: Optional[str] = None
    local_disk_size_gb: Optional[int] = None
    local_disks: Optional[int] = None
    local_nvme_disk_size_gb: Optional[int] = None
    local_nvme_disks: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.instance_type_id is not None: body['instance_type_id'] = self.instance_type_id
        if self.local_disk_size_gb is not None: body['local_disk_size_gb'] = self.local_disk_size_gb
        if self.local_disks is not None: body['local_disks'] = self.local_disks
        if self.local_nvme_disk_size_gb is not None:
            body['local_nvme_disk_size_gb'] = self.local_nvme_disk_size_gb
        if self.local_nvme_disks is not None: body['local_nvme_disks'] = self.local_nvme_disks
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
    category: Optional[str] = None
    display_order: Optional[int] = None
    is_deprecated: Optional[bool] = None
    is_encrypted_in_transit: Optional[bool] = None
    is_graviton: Optional[bool] = None
    is_hidden: Optional[bool] = None
    is_io_cache_enabled: Optional[bool] = None
    node_info: Optional['CloudProviderNodeInfo'] = None
    node_instance_type: Optional['NodeInstanceType'] = None
    num_gpus: Optional[int] = None
    photon_driver_capable: Optional[bool] = None
    photon_worker_capable: Optional[bool] = None
    support_cluster_tags: Optional[bool] = None
    support_ebs_volumes: Optional[bool] = None
    support_port_forwarding: Optional[bool] = None
    supports_elastic_disk: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.category is not None: body['category'] = self.category
        if self.description is not None: body['description'] = self.description
        if self.display_order is not None: body['display_order'] = self.display_order
        if self.instance_type_id is not None: body['instance_type_id'] = self.instance_type_id
        if self.is_deprecated is not None: body['is_deprecated'] = self.is_deprecated
        if self.is_encrypted_in_transit is not None:
            body['is_encrypted_in_transit'] = self.is_encrypted_in_transit
        if self.is_graviton is not None: body['is_graviton'] = self.is_graviton
        if self.is_hidden is not None: body['is_hidden'] = self.is_hidden
        if self.is_io_cache_enabled is not None: body['is_io_cache_enabled'] = self.is_io_cache_enabled
        if self.memory_mb is not None: body['memory_mb'] = self.memory_mb
        if self.node_info: body['node_info'] = self.node_info.as_dict()
        if self.node_instance_type: body['node_instance_type'] = self.node_instance_type.as_dict()
        if self.node_type_id is not None: body['node_type_id'] = self.node_type_id
        if self.num_cores is not None: body['num_cores'] = self.num_cores
        if self.num_gpus is not None: body['num_gpus'] = self.num_gpus
        if self.photon_driver_capable is not None: body['photon_driver_capable'] = self.photon_driver_capable
        if self.photon_worker_capable is not None: body['photon_worker_capable'] = self.photon_worker_capable
        if self.support_cluster_tags is not None: body['support_cluster_tags'] = self.support_cluster_tags
        if self.support_ebs_volumes is not None: body['support_ebs_volumes'] = self.support_ebs_volumes
        if self.support_port_forwarding is not None:
            body['support_port_forwarding'] = self.support_port_forwarding
        if self.supports_elastic_disk is not None: body['supports_elastic_disk'] = self.supports_elastic_disk
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
                   support_port_forwarding=d.get('support_port_forwarding', None),
                   supports_elastic_disk=d.get('supports_elastic_disk', None))


@dataclass
class PendingInstanceError:
    instance_id: Optional[str] = None
    message: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.instance_id is not None: body['instance_id'] = self.instance_id
        if self.message is not None: body['message'] = self.message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PendingInstanceError':
        return cls(instance_id=d.get('instance_id', None), message=d.get('message', None))


@dataclass
class PermanentDeleteCluster:
    cluster_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermanentDeleteCluster':
        return cls(cluster_id=d.get('cluster_id', None))


@dataclass
class PinCluster:
    cluster_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PinCluster':
        return cls(cluster_id=d.get('cluster_id', None))


@dataclass
class Policy:
    created_at_timestamp: Optional[int] = None
    creator_user_name: Optional[str] = None
    definition: Optional[str] = None
    description: Optional[str] = None
    is_default: Optional[bool] = None
    max_clusters_per_user: Optional[int] = None
    name: Optional[str] = None
    policy_family_definition_overrides: Optional[str] = None
    policy_family_id: Optional[str] = None
    policy_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at_timestamp is not None: body['created_at_timestamp'] = self.created_at_timestamp
        if self.creator_user_name is not None: body['creator_user_name'] = self.creator_user_name
        if self.definition is not None: body['definition'] = self.definition
        if self.description is not None: body['description'] = self.description
        if self.is_default is not None: body['is_default'] = self.is_default
        if self.max_clusters_per_user is not None: body['max_clusters_per_user'] = self.max_clusters_per_user
        if self.name is not None: body['name'] = self.name
        if self.policy_family_definition_overrides is not None:
            body['policy_family_definition_overrides'] = self.policy_family_definition_overrides
        if self.policy_family_id is not None: body['policy_family_id'] = self.policy_family_id
        if self.policy_id is not None: body['policy_id'] = self.policy_id
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
        if self.definition is not None: body['definition'] = self.definition
        if self.description is not None: body['description'] = self.description
        if self.name is not None: body['name'] = self.name
        if self.policy_family_id is not None: body['policy_family_id'] = self.policy_family_id
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
    repo: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.package is not None: body['package'] = self.package
        if self.repo is not None: body['repo'] = self.repo
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PythonPyPiLibrary':
        return cls(package=d.get('package', None), repo=d.get('repo', None))


@dataclass
class RCranLibrary:
    package: str
    repo: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.package is not None: body['package'] = self.package
        if self.repo is not None: body['repo'] = self.repo
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RCranLibrary':
        return cls(package=d.get('package', None), repo=d.get('repo', None))


@dataclass
class RemoveInstanceProfile:
    instance_profile_arn: str

    def as_dict(self) -> dict:
        body = {}
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RemoveInstanceProfile':
        return cls(instance_profile_arn=d.get('instance_profile_arn', None))


@dataclass
class ResizeCluster:
    cluster_id: str
    autoscale: Optional['AutoScale'] = None
    num_workers: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.autoscale: body['autoscale'] = self.autoscale.as_dict()
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.num_workers is not None: body['num_workers'] = self.num_workers
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResizeCluster':
        return cls(autoscale=_from_dict(d, 'autoscale', AutoScale),
                   cluster_id=d.get('cluster_id', None),
                   num_workers=d.get('num_workers', None))


@dataclass
class RestartCluster:
    cluster_id: str
    restart_user: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        if self.restart_user is not None: body['restart_user'] = self.restart_user
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RestartCluster':
        return cls(cluster_id=d.get('cluster_id', None), restart_user=d.get('restart_user', None))


class ResultType(Enum):

    ERROR = 'error'
    IMAGE = 'image'
    IMAGES = 'images'
    TABLE = 'table'
    TEXT = 'text'


@dataclass
class Results:
    cause: Optional[str] = None
    data: Optional[Any] = None
    file_name: Optional[str] = None
    file_names: Optional['List[str]'] = None
    is_json_schema: Optional[bool] = None
    pos: Optional[int] = None
    result_type: Optional['ResultType'] = None
    schema: Optional['List[Dict[str,Any]]'] = None
    summary: Optional[str] = None
    truncated: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.cause is not None: body['cause'] = self.cause
        if self.data: body['data'] = self.data
        if self.file_name is not None: body['fileName'] = self.file_name
        if self.file_names: body['fileNames'] = [v for v in self.file_names]
        if self.is_json_schema is not None: body['isJsonSchema'] = self.is_json_schema
        if self.pos is not None: body['pos'] = self.pos
        if self.result_type is not None: body['resultType'] = self.result_type.value
        if self.schema: body['schema'] = [v for v in self.schema]
        if self.summary is not None: body['summary'] = self.summary
        if self.truncated is not None: body['truncated'] = self.truncated
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
    canned_acl: Optional[str] = None
    destination: Optional[str] = None
    enable_encryption: Optional[bool] = None
    encryption_type: Optional[str] = None
    endpoint: Optional[str] = None
    kms_key: Optional[str] = None
    region: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.canned_acl is not None: body['canned_acl'] = self.canned_acl
        if self.destination is not None: body['destination'] = self.destination
        if self.enable_encryption is not None: body['enable_encryption'] = self.enable_encryption
        if self.encryption_type is not None: body['encryption_type'] = self.encryption_type
        if self.endpoint is not None: body['endpoint'] = self.endpoint
        if self.kms_key is not None: body['kms_key'] = self.kms_key
        if self.region is not None: body['region'] = self.region
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
    host_private_ip: Optional[str] = None
    instance_id: Optional[str] = None
    node_aws_attributes: Optional['SparkNodeAwsAttributes'] = None
    node_id: Optional[str] = None
    private_ip: Optional[str] = None
    public_dns: Optional[str] = None
    start_timestamp: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.host_private_ip is not None: body['host_private_ip'] = self.host_private_ip
        if self.instance_id is not None: body['instance_id'] = self.instance_id
        if self.node_aws_attributes: body['node_aws_attributes'] = self.node_aws_attributes.as_dict()
        if self.node_id is not None: body['node_id'] = self.node_id
        if self.private_ip is not None: body['private_ip'] = self.private_ip
        if self.public_dns is not None: body['public_dns'] = self.public_dns
        if self.start_timestamp is not None: body['start_timestamp'] = self.start_timestamp
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
    is_spot: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.is_spot is not None: body['is_spot'] = self.is_spot
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkNodeAwsAttributes':
        return cls(is_spot=d.get('is_spot', None))


@dataclass
class SparkVersion:
    key: Optional[str] = None
    name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkVersion':
        return cls(key=d.get('key', None), name=d.get('name', None))


@dataclass
class StartCluster:
    cluster_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
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
    code: Optional['TerminationReasonCode'] = None
    parameters: Optional['Dict[str,str]'] = None
    type: Optional['TerminationReasonType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.code is not None: body['code'] = self.code.value
        if self.parameters: body['parameters'] = self.parameters
        if self.type is not None: body['type'] = self.type.value
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
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
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
        if self.cluster_id is not None: body['cluster_id'] = self.cluster_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UnpinCluster':
        return cls(cluster_id=d.get('cluster_id', None))


@dataclass
class VolumesStorageInfo:
    destination: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.destination is not None: body['destination'] = self.destination
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'VolumesStorageInfo':
        return cls(destination=d.get('destination', None))


@dataclass
class WorkloadType:
    clients: Optional['ClientsTypes'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.clients: body['clients'] = self.clients.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WorkloadType':
        return cls(clients=_from_dict(d, 'clients', ClientsTypes))


@dataclass
class WorkspaceStorageInfo:
    destination: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.destination is not None: body['destination'] = self.destination
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WorkspaceStorageInfo':
        return cls(destination=d.get('destination', None))


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
               definition: Optional[str] = None,
               description: Optional[str] = None,
               max_clusters_per_user: Optional[int] = None,
               policy_family_definition_overrides: Optional[str] = None,
               policy_family_id: Optional[str] = None) -> CreatePolicyResponse:
        """Create a new policy.
        
        Creates a new policy with prescribed settings.
        
        :param name: str
          Cluster Policy name requested by the user. This has to be unique. Length must be between 1 and 100
          characters.
        :param definition: str (optional)
          Policy definition document expressed in Databricks Cluster Policy Definition Language.
        :param description: str (optional)
          Additional human-readable description of the cluster policy.
        :param max_clusters_per_user: int (optional)
          Max number of clusters per user that can be active using this policy. If not present, there is no
          max limit.
        :param policy_family_definition_overrides: str (optional)
          Policy definition JSON document expressed in Databricks Policy Definition Language. The JSON
          document must be passed as a string and cannot be embedded in the requests.
          
          You can use this to customize the policy definition inherited from the policy family. Policy rules
          specified here are merged into the inherited policy definition.
        :param policy_family_id: str (optional)
          ID of the policy family. The cluster policy's policy definition inherits the policy family's policy
          definition.
          
          Cannot be used with `definition`. Use `policy_family_definition_overrides` instead to customize the
          policy definition.
        
        :returns: :class:`CreatePolicyResponse`
        """
        body = {}
        if definition is not None: body['definition'] = definition
        if description is not None: body['description'] = description
        if max_clusters_per_user is not None: body['max_clusters_per_user'] = max_clusters_per_user
        if name is not None: body['name'] = name
        if policy_family_definition_overrides is not None:
            body['policy_family_definition_overrides'] = policy_family_definition_overrides
        if policy_family_id is not None: body['policy_family_id'] = policy_family_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/policies/clusters/create', body=body, headers=headers)
        return CreatePolicyResponse.from_dict(res)

    def delete(self, policy_id: str):
        """Delete a cluster policy.
        
        Delete a policy for a cluster. Clusters governed by this policy can still run, but cannot be edited.
        
        :param policy_id: str
          The ID of the policy to delete.
        
        
        """
        body = {}
        if policy_id is not None: body['policy_id'] = policy_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/policies/clusters/delete', body=body, headers=headers)

    def edit(self,
             policy_id: str,
             name: str,
             *,
             definition: Optional[str] = None,
             description: Optional[str] = None,
             max_clusters_per_user: Optional[int] = None,
             policy_family_definition_overrides: Optional[str] = None,
             policy_family_id: Optional[str] = None):
        """Update a cluster policy.
        
        Update an existing policy for cluster. This operation may make some clusters governed by the previous
        policy invalid.
        
        :param policy_id: str
          The ID of the policy to update.
        :param name: str
          Cluster Policy name requested by the user. This has to be unique. Length must be between 1 and 100
          characters.
        :param definition: str (optional)
          Policy definition document expressed in Databricks Cluster Policy Definition Language.
        :param description: str (optional)
          Additional human-readable description of the cluster policy.
        :param max_clusters_per_user: int (optional)
          Max number of clusters per user that can be active using this policy. If not present, there is no
          max limit.
        :param policy_family_definition_overrides: str (optional)
          Policy definition JSON document expressed in Databricks Policy Definition Language. The JSON
          document must be passed as a string and cannot be embedded in the requests.
          
          You can use this to customize the policy definition inherited from the policy family. Policy rules
          specified here are merged into the inherited policy definition.
        :param policy_family_id: str (optional)
          ID of the policy family. The cluster policy's policy definition inherits the policy family's policy
          definition.
          
          Cannot be used with `definition`. Use `policy_family_definition_overrides` instead to customize the
          policy definition.
        
        
        """
        body = {}
        if definition is not None: body['definition'] = definition
        if description is not None: body['description'] = description
        if max_clusters_per_user is not None: body['max_clusters_per_user'] = max_clusters_per_user
        if name is not None: body['name'] = name
        if policy_family_definition_overrides is not None:
            body['policy_family_definition_overrides'] = policy_family_definition_overrides
        if policy_family_id is not None: body['policy_family_id'] = policy_family_id
        if policy_id is not None: body['policy_id'] = policy_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/policies/clusters/edit', body=body, headers=headers)

    def get(self, policy_id: str) -> Policy:
        """Get a cluster policy.
        
        Get a cluster policy entity. Creation and editing is available to admins only.
        
        :param policy_id: str
          Canonical unique identifier for the cluster policy.
        
        :returns: :class:`Policy`
        """

        query = {}
        if policy_id is not None: query['policy_id'] = policy_id
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/policies/clusters/get', query=query, headers=headers)
        return Policy.from_dict(res)

    def get_permission_levels(self, cluster_policy_id: str) -> GetClusterPolicyPermissionLevelsResponse:
        """Get cluster policy permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param cluster_policy_id: str
          The cluster policy for which to get or manage permissions.
        
        :returns: :class:`GetClusterPolicyPermissionLevelsResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/permissions/cluster-policies/{cluster_policy_id}/permissionLevels',
                           headers=headers)
        return GetClusterPolicyPermissionLevelsResponse.from_dict(res)

    def get_permissions(self, cluster_policy_id: str) -> ClusterPolicyPermissions:
        """Get cluster policy permissions.
        
        Gets the permissions of a cluster policy. Cluster policies can inherit permissions from their root
        object.
        
        :param cluster_policy_id: str
          The cluster policy for which to get or manage permissions.
        
        :returns: :class:`ClusterPolicyPermissions`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/permissions/cluster-policies/{cluster_policy_id}',
                           headers=headers)
        return ClusterPolicyPermissions.from_dict(res)

    def list(self,
             *,
             sort_column: Optional[ListSortColumn] = None,
             sort_order: Optional[ListSortOrder] = None) -> Iterator['Policy']:
        """List cluster policies.
        
        Returns a list of policies accessible by the requesting user.
        
        :param sort_column: :class:`ListSortColumn` (optional)
          The cluster policy attribute to sort by. * `POLICY_CREATION_TIME` - Sort result list by policy
          creation time. * `POLICY_NAME` - Sort result list by policy name.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order in which the policies get listed. * `DESC` - Sort result list in descending order. * `ASC`
          - Sort result list in ascending order.
        
        :returns: Iterator over :class:`Policy`
        """

        query = {}
        if sort_column is not None: query['sort_column'] = sort_column.value
        if sort_order is not None: query['sort_order'] = sort_order.value
        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/policies/clusters/list', query=query, headers=headers)
        parsed = ListPoliciesResponse.from_dict(json).policies
        return parsed if parsed is not None else []

    def set_permissions(
        self,
        cluster_policy_id: str,
        *,
        access_control_list: Optional[List[ClusterPolicyAccessControlRequest]] = None
    ) -> ClusterPolicyPermissions:
        """Set cluster policy permissions.
        
        Sets permissions on a cluster policy. Cluster policies can inherit permissions from their root object.
        
        :param cluster_policy_id: str
          The cluster policy for which to get or manage permissions.
        :param access_control_list: List[:class:`ClusterPolicyAccessControlRequest`] (optional)
        
        :returns: :class:`ClusterPolicyPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PUT',
                           f'/api/2.0/permissions/cluster-policies/{cluster_policy_id}',
                           body=body,
                           headers=headers)
        return ClusterPolicyPermissions.from_dict(res)

    def update_permissions(
        self,
        cluster_policy_id: str,
        *,
        access_control_list: Optional[List[ClusterPolicyAccessControlRequest]] = None
    ) -> ClusterPolicyPermissions:
        """Update cluster policy permissions.
        
        Updates the permissions on a cluster policy. Cluster policies can inherit permissions from their root
        object.
        
        :param cluster_policy_id: str
          The cluster policy for which to get or manage permissions.
        :param access_control_list: List[:class:`ClusterPolicyAccessControlRequest`] (optional)
        
        :returns: :class:`ClusterPolicyPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PATCH',
                           f'/api/2.0/permissions/cluster-policies/{cluster_policy_id}',
                           body=body,
                           headers=headers)
        return ClusterPolicyPermissions.from_dict(res)


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

    def wait_get_cluster_running(
            self,
            cluster_id: str,
            timeout=timedelta(minutes=20),
            callback: Optional[Callable[[ClusterDetails], None]] = None) -> ClusterDetails:
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

    def wait_get_cluster_terminated(
            self,
            cluster_id: str,
            timeout=timedelta(minutes=20),
            callback: Optional[Callable[[ClusterDetails], None]] = None) -> ClusterDetails:
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

    def change_owner(self, cluster_id: str, owner_username: str):
        """Change cluster owner.
        
        Change the owner of the cluster. You must be an admin to perform this operation.
        
        :param cluster_id: str
          <needs content added>
        :param owner_username: str
          New owner of the cluster_id after this RPC.
        
        
        """
        body = {}
        if cluster_id is not None: body['cluster_id'] = cluster_id
        if owner_username is not None: body['owner_username'] = owner_username
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/clusters/change-owner', body=body, headers=headers)

    def create(self,
               spark_version: str,
               *,
               apply_policy_default_values: Optional[bool] = None,
               autoscale: Optional[AutoScale] = None,
               autotermination_minutes: Optional[int] = None,
               aws_attributes: Optional[AwsAttributes] = None,
               azure_attributes: Optional[AzureAttributes] = None,
               cluster_log_conf: Optional[ClusterLogConf] = None,
               cluster_name: Optional[str] = None,
               cluster_source: Optional[ClusterSource] = None,
               custom_tags: Optional[Dict[str, str]] = None,
               data_security_mode: Optional[DataSecurityMode] = None,
               docker_image: Optional[DockerImage] = None,
               driver_instance_pool_id: Optional[str] = None,
               driver_node_type_id: Optional[str] = None,
               enable_elastic_disk: Optional[bool] = None,
               enable_local_disk_encryption: Optional[bool] = None,
               gcp_attributes: Optional[GcpAttributes] = None,
               init_scripts: Optional[List[InitScriptInfo]] = None,
               instance_pool_id: Optional[str] = None,
               node_type_id: Optional[str] = None,
               num_workers: Optional[int] = None,
               policy_id: Optional[str] = None,
               runtime_engine: Optional[RuntimeEngine] = None,
               single_user_name: Optional[str] = None,
               spark_conf: Optional[Dict[str, str]] = None,
               spark_env_vars: Optional[Dict[str, str]] = None,
               ssh_public_keys: Optional[List[str]] = None,
               workload_type: Optional[WorkloadType] = None) -> Wait[ClusterDetails]:
        """Create new cluster.
        
        Creates a new Spark cluster. This method will acquire new instances from the cloud provider if
        necessary. Note: Databricks may not be able to acquire some of the requested nodes, due to cloud
        provider limitations (account limits, spot price, etc.) or transient network issues.
        
        If Databricks acquires at least 85% of the requested on-demand nodes, cluster creation will succeed.
        Otherwise the cluster will terminate with an informative error message.
        
        :param spark_version: str
          The Spark version of the cluster, e.g. `3.3.x-scala2.11`. A list of available Spark versions can be
          retrieved by using the :method:clusters/sparkVersions API call.
        :param apply_policy_default_values: bool (optional)
        :param autoscale: :class:`AutoScale` (optional)
          Parameters needed in order to automatically scale clusters up and down based on load. Note:
          autoscaling works best with DB runtime versions 3.0 or later.
        :param autotermination_minutes: int (optional)
          Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this
          cluster will not be automatically terminated. If specified, the threshold must be between 10 and
          10000 minutes. Users can also set this value to 0 to explicitly disable automatic termination.
        :param aws_attributes: :class:`AwsAttributes` (optional)
          Attributes related to clusters running on Amazon Web Services. If not specified at cluster creation,
          a set of default values will be used.
        :param azure_attributes: :class:`AzureAttributes` (optional)
          Attributes related to clusters running on Microsoft Azure. If not specified at cluster creation, a
          set of default values will be used.
        :param cluster_log_conf: :class:`ClusterLogConf` (optional)
          The configuration for delivering spark logs to a long-term storage destination. Two kinds of
          destinations (dbfs and s3) are supported. Only one destination can be specified for one cluster. If
          the conf is given, the logs will be delivered to the destination every `5 mins`. The destination of
          driver logs is `$destination/$clusterId/driver`, while the destination of executor logs is
          `$destination/$clusterId/executor`.
        :param cluster_name: str (optional)
          Cluster name requested by the user. This doesn't have to be unique. If not specified at creation,
          the cluster name will be an empty string.
        :param cluster_source: :class:`ClusterSource` (optional)
          Determines whether the cluster was created by a user through the UI, created by the Databricks Jobs
          Scheduler, or through an API request. This is the same as cluster_creator, but read only.
        :param custom_tags: Dict[str,str] (optional)
          Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS
          instances and EBS volumes) with these tags in addition to `default_tags`. Notes:
          
          - Currently, Databricks allows at most 45 custom tags
          
          - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags
        :param data_security_mode: :class:`DataSecurityMode` (optional)
          Data security mode decides what data governance model to use when accessing data from a cluster.
          
          * `NONE`: No security isolation for multiple users sharing the cluster. Data governance features are
          not available in this mode. * `SINGLE_USER`: A secure cluster that can only be exclusively used by a
          single user specified in `single_user_name`. Most programming languages, cluster features and data
          governance features are available in this mode. * `USER_ISOLATION`: A secure cluster that can be
          shared by multiple users. Cluster users are fully isolated so that they cannot see each other's data
          and credentials. Most data governance features are supported in this mode. But programming languages
          and cluster features might be limited. * `LEGACY_TABLE_ACL`: This mode is for users migrating from
          legacy Table ACL clusters. * `LEGACY_PASSTHROUGH`: This mode is for users migrating from legacy
          Passthrough on high concurrency clusters. * `LEGACY_SINGLE_USER`: This mode is for users migrating
          from legacy Passthrough on standard clusters.
        :param docker_image: :class:`DockerImage` (optional)
        :param driver_instance_pool_id: str (optional)
          The optional ID of the instance pool for the driver of the cluster belongs. The pool cluster uses
          the instance pool with id (instance_pool_id) if the driver pool is not assigned.
        :param driver_node_type_id: str (optional)
          The node type of the Spark driver. Note that this field is optional; if unset, the driver node type
          will be set as the same value as `node_type_id` defined above.
        :param enable_elastic_disk: bool (optional)
          Autoscaling Local Storage: when enabled, this cluster will dynamically acquire additional disk space
          when its Spark workers are running low on disk space. This feature requires specific AWS permissions
          to function correctly - refer to the User Guide for more details.
        :param enable_local_disk_encryption: bool (optional)
          Whether to enable LUKS on cluster VMs' local disks
        :param gcp_attributes: :class:`GcpAttributes` (optional)
          Attributes related to clusters running on Google Cloud Platform. If not specified at cluster
          creation, a set of default values will be used.
        :param init_scripts: List[:class:`InitScriptInfo`] (optional)
          The configuration for storing init scripts. Any number of destinations can be specified. The scripts
          are executed sequentially in the order provided. If `cluster_log_conf` is specified, init script
          logs are sent to `<destination>/<cluster-ID>/init_scripts`.
        :param instance_pool_id: str (optional)
          The optional ID of the instance pool to which the cluster belongs.
        :param node_type_id: str (optional)
          This field encodes, through a single value, the resources available to each of the Spark nodes in
          this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute
          intensive workloads. A list of available node types can be retrieved by using the
          :method:clusters/listNodeTypes API call.
        :param num_workers: int (optional)
          Number of worker nodes that this cluster should have. A cluster has one Spark Driver and
          `num_workers` Executors for a total of `num_workers` + 1 Spark nodes.
          
          Note: When reading the properties of a cluster, this field reflects the desired number of workers
          rather than the actual current number of workers. For instance, if a cluster is resized from 5 to 10
          workers, this field will immediately be updated to reflect the target size of 10 workers, whereas
          the workers listed in `spark_info` will gradually increase from 5 to 10 as the new nodes are
          provisioned.
        :param policy_id: str (optional)
          The ID of the cluster policy used to create the cluster if applicable.
        :param runtime_engine: :class:`RuntimeEngine` (optional)
          Decides which runtime engine to be use, e.g. Standard vs. Photon. If unspecified, the runtime engine
          is inferred from spark_version.
        :param single_user_name: str (optional)
          Single user name if data_security_mode is `SINGLE_USER`
        :param spark_conf: Dict[str,str] (optional)
          An object containing a set of optional, user-specified Spark configuration key-value pairs. Users
          can also pass in a string of extra JVM options to the driver and the executors via
          `spark.driver.extraJavaOptions` and `spark.executor.extraJavaOptions` respectively.
        :param spark_env_vars: Dict[str,str] (optional)
          An object containing a set of optional, user-specified environment variable key-value pairs. Please
          note that key-value pair of the form (X,Y) will be exported as is (i.e., `export X='Y'`) while
          launching the driver and workers.
          
          In order to specify an additional set of `SPARK_DAEMON_JAVA_OPTS`, we recommend appending them to
          `$SPARK_DAEMON_JAVA_OPTS` as shown in the example below. This ensures that all default databricks
          managed environmental variables are included as well.
          
          Example Spark environment variables: `{"SPARK_WORKER_MEMORY": "28000m", "SPARK_LOCAL_DIRS":
          "/local_disk0"}` or `{"SPARK_DAEMON_JAVA_OPTS": "$SPARK_DAEMON_JAVA_OPTS
          -Dspark.shuffle.service.enabled=true"}`
        :param ssh_public_keys: List[str] (optional)
          SSH public key contents that will be added to each Spark node in this cluster. The corresponding
          private keys can be used to login with the user name `ubuntu` on port `2200`. Up to 10 keys can be
          specified.
        :param workload_type: :class:`WorkloadType` (optional)
        
        :returns:
          Long-running operation waiter for :class:`ClusterDetails`.
          See :method:wait_get_cluster_running for more details.
        """
        body = {}
        if apply_policy_default_values is not None:
            body['apply_policy_default_values'] = apply_policy_default_values
        if autoscale is not None: body['autoscale'] = autoscale.as_dict()
        if autotermination_minutes is not None: body['autotermination_minutes'] = autotermination_minutes
        if aws_attributes is not None: body['aws_attributes'] = aws_attributes.as_dict()
        if azure_attributes is not None: body['azure_attributes'] = azure_attributes.as_dict()
        if cluster_log_conf is not None: body['cluster_log_conf'] = cluster_log_conf.as_dict()
        if cluster_name is not None: body['cluster_name'] = cluster_name
        if cluster_source is not None: body['cluster_source'] = cluster_source.value
        if custom_tags is not None: body['custom_tags'] = custom_tags
        if data_security_mode is not None: body['data_security_mode'] = data_security_mode.value
        if docker_image is not None: body['docker_image'] = docker_image.as_dict()
        if driver_instance_pool_id is not None: body['driver_instance_pool_id'] = driver_instance_pool_id
        if driver_node_type_id is not None: body['driver_node_type_id'] = driver_node_type_id
        if enable_elastic_disk is not None: body['enable_elastic_disk'] = enable_elastic_disk
        if enable_local_disk_encryption is not None:
            body['enable_local_disk_encryption'] = enable_local_disk_encryption
        if gcp_attributes is not None: body['gcp_attributes'] = gcp_attributes.as_dict()
        if init_scripts is not None: body['init_scripts'] = [v.as_dict() for v in init_scripts]
        if instance_pool_id is not None: body['instance_pool_id'] = instance_pool_id
        if node_type_id is not None: body['node_type_id'] = node_type_id
        if num_workers is not None: body['num_workers'] = num_workers
        if policy_id is not None: body['policy_id'] = policy_id
        if runtime_engine is not None: body['runtime_engine'] = runtime_engine.value
        if single_user_name is not None: body['single_user_name'] = single_user_name
        if spark_conf is not None: body['spark_conf'] = spark_conf
        if spark_env_vars is not None: body['spark_env_vars'] = spark_env_vars
        if spark_version is not None: body['spark_version'] = spark_version
        if ssh_public_keys is not None: body['ssh_public_keys'] = [v for v in ssh_public_keys]
        if workload_type is not None: body['workload_type'] = workload_type.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        op_response = self._api.do('POST', '/api/2.0/clusters/create', body=body, headers=headers)
        return Wait(self.wait_get_cluster_running,
                    response=CreateClusterResponse.from_dict(op_response),
                    cluster_id=op_response['cluster_id'])

    def create_and_wait(
        self,
        spark_version: str,
        *,
        apply_policy_default_values: Optional[bool] = None,
        autoscale: Optional[AutoScale] = None,
        autotermination_minutes: Optional[int] = None,
        aws_attributes: Optional[AwsAttributes] = None,
        azure_attributes: Optional[AzureAttributes] = None,
        cluster_log_conf: Optional[ClusterLogConf] = None,
        cluster_name: Optional[str] = None,
        cluster_source: Optional[ClusterSource] = None,
        custom_tags: Optional[Dict[str, str]] = None,
        data_security_mode: Optional[DataSecurityMode] = None,
        docker_image: Optional[DockerImage] = None,
        driver_instance_pool_id: Optional[str] = None,
        driver_node_type_id: Optional[str] = None,
        enable_elastic_disk: Optional[bool] = None,
        enable_local_disk_encryption: Optional[bool] = None,
        gcp_attributes: Optional[GcpAttributes] = None,
        init_scripts: Optional[List[InitScriptInfo]] = None,
        instance_pool_id: Optional[str] = None,
        node_type_id: Optional[str] = None,
        num_workers: Optional[int] = None,
        policy_id: Optional[str] = None,
        runtime_engine: Optional[RuntimeEngine] = None,
        single_user_name: Optional[str] = None,
        spark_conf: Optional[Dict[str, str]] = None,
        spark_env_vars: Optional[Dict[str, str]] = None,
        ssh_public_keys: Optional[List[str]] = None,
        workload_type: Optional[WorkloadType] = None,
        timeout=timedelta(minutes=20)) -> ClusterDetails:
        return self.create(apply_policy_default_values=apply_policy_default_values,
                           autoscale=autoscale,
                           autotermination_minutes=autotermination_minutes,
                           aws_attributes=aws_attributes,
                           azure_attributes=azure_attributes,
                           cluster_log_conf=cluster_log_conf,
                           cluster_name=cluster_name,
                           cluster_source=cluster_source,
                           custom_tags=custom_tags,
                           data_security_mode=data_security_mode,
                           docker_image=docker_image,
                           driver_instance_pool_id=driver_instance_pool_id,
                           driver_node_type_id=driver_node_type_id,
                           enable_elastic_disk=enable_elastic_disk,
                           enable_local_disk_encryption=enable_local_disk_encryption,
                           gcp_attributes=gcp_attributes,
                           init_scripts=init_scripts,
                           instance_pool_id=instance_pool_id,
                           node_type_id=node_type_id,
                           num_workers=num_workers,
                           policy_id=policy_id,
                           runtime_engine=runtime_engine,
                           single_user_name=single_user_name,
                           spark_conf=spark_conf,
                           spark_env_vars=spark_env_vars,
                           spark_version=spark_version,
                           ssh_public_keys=ssh_public_keys,
                           workload_type=workload_type).result(timeout=timeout)

    def delete(self, cluster_id: str) -> Wait[ClusterDetails]:
        """Terminate cluster.
        
        Terminates the Spark cluster with the specified ID. The cluster is removed asynchronously. Once the
        termination has completed, the cluster will be in a `TERMINATED` state. If the cluster is already in a
        `TERMINATING` or `TERMINATED` state, nothing will happen.
        
        :param cluster_id: str
          The cluster to be terminated.
        
        :returns:
          Long-running operation waiter for :class:`ClusterDetails`.
          See :method:wait_get_cluster_terminated for more details.
        """
        body = {}
        if cluster_id is not None: body['cluster_id'] = cluster_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/clusters/delete', body=body, headers=headers)
        return Wait(self.wait_get_cluster_terminated, cluster_id=cluster_id)

    def delete_and_wait(self, cluster_id: str, timeout=timedelta(minutes=20)) -> ClusterDetails:
        return self.delete(cluster_id=cluster_id).result(timeout=timeout)

    def edit(self,
             cluster_id: str,
             spark_version: str,
             *,
             apply_policy_default_values: Optional[bool] = None,
             autoscale: Optional[AutoScale] = None,
             autotermination_minutes: Optional[int] = None,
             aws_attributes: Optional[AwsAttributes] = None,
             azure_attributes: Optional[AzureAttributes] = None,
             cluster_log_conf: Optional[ClusterLogConf] = None,
             cluster_name: Optional[str] = None,
             cluster_source: Optional[ClusterSource] = None,
             custom_tags: Optional[Dict[str, str]] = None,
             data_security_mode: Optional[DataSecurityMode] = None,
             docker_image: Optional[DockerImage] = None,
             driver_instance_pool_id: Optional[str] = None,
             driver_node_type_id: Optional[str] = None,
             enable_elastic_disk: Optional[bool] = None,
             enable_local_disk_encryption: Optional[bool] = None,
             gcp_attributes: Optional[GcpAttributes] = None,
             init_scripts: Optional[List[InitScriptInfo]] = None,
             instance_pool_id: Optional[str] = None,
             node_type_id: Optional[str] = None,
             num_workers: Optional[int] = None,
             policy_id: Optional[str] = None,
             runtime_engine: Optional[RuntimeEngine] = None,
             single_user_name: Optional[str] = None,
             spark_conf: Optional[Dict[str, str]] = None,
             spark_env_vars: Optional[Dict[str, str]] = None,
             ssh_public_keys: Optional[List[str]] = None,
             workload_type: Optional[WorkloadType] = None) -> Wait[ClusterDetails]:
        """Update cluster configuration.
        
        Updates the configuration of a cluster to match the provided attributes and size. A cluster can be
        updated if it is in a `RUNNING` or `TERMINATED` state.
        
        If a cluster is updated while in a `RUNNING` state, it will be restarted so that the new attributes
        can take effect.
        
        If a cluster is updated while in a `TERMINATED` state, it will remain `TERMINATED`. The next time it
        is started using the `clusters/start` API, the new attributes will take effect. Any attempt to update
        a cluster in any other state will be rejected with an `INVALID_STATE` error code.
        
        Clusters created by the Databricks Jobs service cannot be edited.
        
        :param cluster_id: str
          ID of the cluser
        :param spark_version: str
          The Spark version of the cluster, e.g. `3.3.x-scala2.11`. A list of available Spark versions can be
          retrieved by using the :method:clusters/sparkVersions API call.
        :param apply_policy_default_values: bool (optional)
        :param autoscale: :class:`AutoScale` (optional)
          Parameters needed in order to automatically scale clusters up and down based on load. Note:
          autoscaling works best with DB runtime versions 3.0 or later.
        :param autotermination_minutes: int (optional)
          Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this
          cluster will not be automatically terminated. If specified, the threshold must be between 10 and
          10000 minutes. Users can also set this value to 0 to explicitly disable automatic termination.
        :param aws_attributes: :class:`AwsAttributes` (optional)
          Attributes related to clusters running on Amazon Web Services. If not specified at cluster creation,
          a set of default values will be used.
        :param azure_attributes: :class:`AzureAttributes` (optional)
          Attributes related to clusters running on Microsoft Azure. If not specified at cluster creation, a
          set of default values will be used.
        :param cluster_log_conf: :class:`ClusterLogConf` (optional)
          The configuration for delivering spark logs to a long-term storage destination. Two kinds of
          destinations (dbfs and s3) are supported. Only one destination can be specified for one cluster. If
          the conf is given, the logs will be delivered to the destination every `5 mins`. The destination of
          driver logs is `$destination/$clusterId/driver`, while the destination of executor logs is
          `$destination/$clusterId/executor`.
        :param cluster_name: str (optional)
          Cluster name requested by the user. This doesn't have to be unique. If not specified at creation,
          the cluster name will be an empty string.
        :param cluster_source: :class:`ClusterSource` (optional)
          Determines whether the cluster was created by a user through the UI, created by the Databricks Jobs
          Scheduler, or through an API request. This is the same as cluster_creator, but read only.
        :param custom_tags: Dict[str,str] (optional)
          Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS
          instances and EBS volumes) with these tags in addition to `default_tags`. Notes:
          
          - Currently, Databricks allows at most 45 custom tags
          
          - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags
        :param data_security_mode: :class:`DataSecurityMode` (optional)
          Data security mode decides what data governance model to use when accessing data from a cluster.
          
          * `NONE`: No security isolation for multiple users sharing the cluster. Data governance features are
          not available in this mode. * `SINGLE_USER`: A secure cluster that can only be exclusively used by a
          single user specified in `single_user_name`. Most programming languages, cluster features and data
          governance features are available in this mode. * `USER_ISOLATION`: A secure cluster that can be
          shared by multiple users. Cluster users are fully isolated so that they cannot see each other's data
          and credentials. Most data governance features are supported in this mode. But programming languages
          and cluster features might be limited. * `LEGACY_TABLE_ACL`: This mode is for users migrating from
          legacy Table ACL clusters. * `LEGACY_PASSTHROUGH`: This mode is for users migrating from legacy
          Passthrough on high concurrency clusters. * `LEGACY_SINGLE_USER`: This mode is for users migrating
          from legacy Passthrough on standard clusters.
        :param docker_image: :class:`DockerImage` (optional)
        :param driver_instance_pool_id: str (optional)
          The optional ID of the instance pool for the driver of the cluster belongs. The pool cluster uses
          the instance pool with id (instance_pool_id) if the driver pool is not assigned.
        :param driver_node_type_id: str (optional)
          The node type of the Spark driver. Note that this field is optional; if unset, the driver node type
          will be set as the same value as `node_type_id` defined above.
        :param enable_elastic_disk: bool (optional)
          Autoscaling Local Storage: when enabled, this cluster will dynamically acquire additional disk space
          when its Spark workers are running low on disk space. This feature requires specific AWS permissions
          to function correctly - refer to the User Guide for more details.
        :param enable_local_disk_encryption: bool (optional)
          Whether to enable LUKS on cluster VMs' local disks
        :param gcp_attributes: :class:`GcpAttributes` (optional)
          Attributes related to clusters running on Google Cloud Platform. If not specified at cluster
          creation, a set of default values will be used.
        :param init_scripts: List[:class:`InitScriptInfo`] (optional)
          The configuration for storing init scripts. Any number of destinations can be specified. The scripts
          are executed sequentially in the order provided. If `cluster_log_conf` is specified, init script
          logs are sent to `<destination>/<cluster-ID>/init_scripts`.
        :param instance_pool_id: str (optional)
          The optional ID of the instance pool to which the cluster belongs.
        :param node_type_id: str (optional)
          This field encodes, through a single value, the resources available to each of the Spark nodes in
          this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute
          intensive workloads. A list of available node types can be retrieved by using the
          :method:clusters/listNodeTypes API call.
        :param num_workers: int (optional)
          Number of worker nodes that this cluster should have. A cluster has one Spark Driver and
          `num_workers` Executors for a total of `num_workers` + 1 Spark nodes.
          
          Note: When reading the properties of a cluster, this field reflects the desired number of workers
          rather than the actual current number of workers. For instance, if a cluster is resized from 5 to 10
          workers, this field will immediately be updated to reflect the target size of 10 workers, whereas
          the workers listed in `spark_info` will gradually increase from 5 to 10 as the new nodes are
          provisioned.
        :param policy_id: str (optional)
          The ID of the cluster policy used to create the cluster if applicable.
        :param runtime_engine: :class:`RuntimeEngine` (optional)
          Decides which runtime engine to be use, e.g. Standard vs. Photon. If unspecified, the runtime engine
          is inferred from spark_version.
        :param single_user_name: str (optional)
          Single user name if data_security_mode is `SINGLE_USER`
        :param spark_conf: Dict[str,str] (optional)
          An object containing a set of optional, user-specified Spark configuration key-value pairs. Users
          can also pass in a string of extra JVM options to the driver and the executors via
          `spark.driver.extraJavaOptions` and `spark.executor.extraJavaOptions` respectively.
        :param spark_env_vars: Dict[str,str] (optional)
          An object containing a set of optional, user-specified environment variable key-value pairs. Please
          note that key-value pair of the form (X,Y) will be exported as is (i.e., `export X='Y'`) while
          launching the driver and workers.
          
          In order to specify an additional set of `SPARK_DAEMON_JAVA_OPTS`, we recommend appending them to
          `$SPARK_DAEMON_JAVA_OPTS` as shown in the example below. This ensures that all default databricks
          managed environmental variables are included as well.
          
          Example Spark environment variables: `{"SPARK_WORKER_MEMORY": "28000m", "SPARK_LOCAL_DIRS":
          "/local_disk0"}` or `{"SPARK_DAEMON_JAVA_OPTS": "$SPARK_DAEMON_JAVA_OPTS
          -Dspark.shuffle.service.enabled=true"}`
        :param ssh_public_keys: List[str] (optional)
          SSH public key contents that will be added to each Spark node in this cluster. The corresponding
          private keys can be used to login with the user name `ubuntu` on port `2200`. Up to 10 keys can be
          specified.
        :param workload_type: :class:`WorkloadType` (optional)
        
        :returns:
          Long-running operation waiter for :class:`ClusterDetails`.
          See :method:wait_get_cluster_running for more details.
        """
        body = {}
        if apply_policy_default_values is not None:
            body['apply_policy_default_values'] = apply_policy_default_values
        if autoscale is not None: body['autoscale'] = autoscale.as_dict()
        if autotermination_minutes is not None: body['autotermination_minutes'] = autotermination_minutes
        if aws_attributes is not None: body['aws_attributes'] = aws_attributes.as_dict()
        if azure_attributes is not None: body['azure_attributes'] = azure_attributes.as_dict()
        if cluster_id is not None: body['cluster_id'] = cluster_id
        if cluster_log_conf is not None: body['cluster_log_conf'] = cluster_log_conf.as_dict()
        if cluster_name is not None: body['cluster_name'] = cluster_name
        if cluster_source is not None: body['cluster_source'] = cluster_source.value
        if custom_tags is not None: body['custom_tags'] = custom_tags
        if data_security_mode is not None: body['data_security_mode'] = data_security_mode.value
        if docker_image is not None: body['docker_image'] = docker_image.as_dict()
        if driver_instance_pool_id is not None: body['driver_instance_pool_id'] = driver_instance_pool_id
        if driver_node_type_id is not None: body['driver_node_type_id'] = driver_node_type_id
        if enable_elastic_disk is not None: body['enable_elastic_disk'] = enable_elastic_disk
        if enable_local_disk_encryption is not None:
            body['enable_local_disk_encryption'] = enable_local_disk_encryption
        if gcp_attributes is not None: body['gcp_attributes'] = gcp_attributes.as_dict()
        if init_scripts is not None: body['init_scripts'] = [v.as_dict() for v in init_scripts]
        if instance_pool_id is not None: body['instance_pool_id'] = instance_pool_id
        if node_type_id is not None: body['node_type_id'] = node_type_id
        if num_workers is not None: body['num_workers'] = num_workers
        if policy_id is not None: body['policy_id'] = policy_id
        if runtime_engine is not None: body['runtime_engine'] = runtime_engine.value
        if single_user_name is not None: body['single_user_name'] = single_user_name
        if spark_conf is not None: body['spark_conf'] = spark_conf
        if spark_env_vars is not None: body['spark_env_vars'] = spark_env_vars
        if spark_version is not None: body['spark_version'] = spark_version
        if ssh_public_keys is not None: body['ssh_public_keys'] = [v for v in ssh_public_keys]
        if workload_type is not None: body['workload_type'] = workload_type.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/clusters/edit', body=body, headers=headers)
        return Wait(self.wait_get_cluster_running, cluster_id=cluster_id)

    def edit_and_wait(
        self,
        cluster_id: str,
        spark_version: str,
        *,
        apply_policy_default_values: Optional[bool] = None,
        autoscale: Optional[AutoScale] = None,
        autotermination_minutes: Optional[int] = None,
        aws_attributes: Optional[AwsAttributes] = None,
        azure_attributes: Optional[AzureAttributes] = None,
        cluster_log_conf: Optional[ClusterLogConf] = None,
        cluster_name: Optional[str] = None,
        cluster_source: Optional[ClusterSource] = None,
        custom_tags: Optional[Dict[str, str]] = None,
        data_security_mode: Optional[DataSecurityMode] = None,
        docker_image: Optional[DockerImage] = None,
        driver_instance_pool_id: Optional[str] = None,
        driver_node_type_id: Optional[str] = None,
        enable_elastic_disk: Optional[bool] = None,
        enable_local_disk_encryption: Optional[bool] = None,
        gcp_attributes: Optional[GcpAttributes] = None,
        init_scripts: Optional[List[InitScriptInfo]] = None,
        instance_pool_id: Optional[str] = None,
        node_type_id: Optional[str] = None,
        num_workers: Optional[int] = None,
        policy_id: Optional[str] = None,
        runtime_engine: Optional[RuntimeEngine] = None,
        single_user_name: Optional[str] = None,
        spark_conf: Optional[Dict[str, str]] = None,
        spark_env_vars: Optional[Dict[str, str]] = None,
        ssh_public_keys: Optional[List[str]] = None,
        workload_type: Optional[WorkloadType] = None,
        timeout=timedelta(minutes=20)) -> ClusterDetails:
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
                         data_security_mode=data_security_mode,
                         docker_image=docker_image,
                         driver_instance_pool_id=driver_instance_pool_id,
                         driver_node_type_id=driver_node_type_id,
                         enable_elastic_disk=enable_elastic_disk,
                         enable_local_disk_encryption=enable_local_disk_encryption,
                         gcp_attributes=gcp_attributes,
                         init_scripts=init_scripts,
                         instance_pool_id=instance_pool_id,
                         node_type_id=node_type_id,
                         num_workers=num_workers,
                         policy_id=policy_id,
                         runtime_engine=runtime_engine,
                         single_user_name=single_user_name,
                         spark_conf=spark_conf,
                         spark_env_vars=spark_env_vars,
                         spark_version=spark_version,
                         ssh_public_keys=ssh_public_keys,
                         workload_type=workload_type).result(timeout=timeout)

    def events(self,
               cluster_id: str,
               *,
               end_time: Optional[int] = None,
               event_types: Optional[List[EventType]] = None,
               limit: Optional[int] = None,
               offset: Optional[int] = None,
               order: Optional[GetEventsOrder] = None,
               start_time: Optional[int] = None) -> Iterator['ClusterEvent']:
        """List cluster activity events.
        
        Retrieves a list of events about the activity of a cluster. This API is paginated. If there are more
        events to read, the response includes all the nparameters necessary to request the next page of
        events.
        
        :param cluster_id: str
          The ID of the cluster to retrieve events about.
        :param end_time: int (optional)
          The end time in epoch milliseconds. If empty, returns events up to the current time.
        :param event_types: List[:class:`EventType`] (optional)
          An optional set of event types to filter on. If empty, all event types are returned.
        :param limit: int (optional)
          The maximum number of events to include in a page of events. Defaults to 50, and maximum allowed
          value is 500.
        :param offset: int (optional)
          The offset in the result set. Defaults to 0 (no offset). When an offset is specified and the results
          are requested in descending order, the end_time field is required.
        :param order: :class:`GetEventsOrder` (optional)
          The order to list events in; either "ASC" or "DESC". Defaults to "DESC".
        :param start_time: int (optional)
          The start time in epoch milliseconds. If empty, returns events starting from the beginning of time.
        
        :returns: Iterator over :class:`ClusterEvent`
        """
        body = {}
        if cluster_id is not None: body['cluster_id'] = cluster_id
        if end_time is not None: body['end_time'] = end_time
        if event_types is not None: body['event_types'] = [v.value for v in event_types]
        if limit is not None: body['limit'] = limit
        if offset is not None: body['offset'] = offset
        if order is not None: body['order'] = order.value
        if start_time is not None: body['start_time'] = start_time
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        while True:
            json = self._api.do('POST', '/api/2.0/clusters/events', body=body, headers=headers)
            if 'events' not in json or not json['events']:
                return
            for v in json['events']:
                yield ClusterEvent.from_dict(v)
            if 'next_page' not in json or not json['next_page']:
                return
            body = json['next_page']

    def get(self, cluster_id: str) -> ClusterDetails:
        """Get cluster info.
        
        Retrieves the information for a cluster given its identifier. Clusters can be described while they are
        running, or up to 60 days after they are terminated.
        
        :param cluster_id: str
          The cluster about which to retrieve information.
        
        :returns: :class:`ClusterDetails`
        """

        query = {}
        if cluster_id is not None: query['cluster_id'] = cluster_id
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/clusters/get', query=query, headers=headers)
        return ClusterDetails.from_dict(res)

    def get_permission_levels(self, cluster_id: str) -> GetClusterPermissionLevelsResponse:
        """Get cluster permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param cluster_id: str
          The cluster for which to get or manage permissions.
        
        :returns: :class:`GetClusterPermissionLevelsResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/permissions/clusters/{cluster_id}/permissionLevels',
                           headers=headers)
        return GetClusterPermissionLevelsResponse.from_dict(res)

    def get_permissions(self, cluster_id: str) -> ClusterPermissions:
        """Get cluster permissions.
        
        Gets the permissions of a cluster. Clusters can inherit permissions from their root object.
        
        :param cluster_id: str
          The cluster for which to get or manage permissions.
        
        :returns: :class:`ClusterPermissions`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/permissions/clusters/{cluster_id}', headers=headers)
        return ClusterPermissions.from_dict(res)

    def list(self, *, can_use_client: Optional[str] = None) -> Iterator['ClusterDetails']:
        """List all clusters.
        
        Return information about all pinned clusters, active clusters, up to 200 of the most recently
        terminated all-purpose clusters in the past 30 days, and up to 30 of the most recently terminated job
        clusters in the past 30 days.
        
        For example, if there is 1 pinned cluster, 4 active clusters, 45 terminated all-purpose clusters in
        the past 30 days, and 50 terminated job clusters in the past 30 days, then this API returns the 1
        pinned cluster, 4 active clusters, all 45 terminated all-purpose clusters, and the 30 most recently
        terminated job clusters.
        
        :param can_use_client: str (optional)
          Filter clusters based on what type of client it can be used for. Could be either NOTEBOOKS or JOBS.
          No input for this field will get all clusters in the workspace without filtering on its supported
          client
        
        :returns: Iterator over :class:`ClusterDetails`
        """

        query = {}
        if can_use_client is not None: query['can_use_client'] = can_use_client
        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/clusters/list', query=query, headers=headers)
        parsed = ListClustersResponse.from_dict(json).clusters
        return parsed if parsed is not None else []

    def list_node_types(self) -> ListNodeTypesResponse:
        """List node types.
        
        Returns a list of supported Spark node types. These node types can be used to launch a cluster.
        
        :returns: :class:`ListNodeTypesResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/clusters/list-node-types', headers=headers)
        return ListNodeTypesResponse.from_dict(res)

    def list_zones(self) -> ListAvailableZonesResponse:
        """List availability zones.
        
        Returns a list of availability zones where clusters can be created in (For example, us-west-2a). These
        zones can be used to launch a cluster.
        
        :returns: :class:`ListAvailableZonesResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/clusters/list-zones', headers=headers)
        return ListAvailableZonesResponse.from_dict(res)

    def permanent_delete(self, cluster_id: str):
        """Permanently delete cluster.
        
        Permanently deletes a Spark cluster. This cluster is terminated and resources are asynchronously
        removed.
        
        In addition, users will no longer see permanently deleted clusters in the cluster list, and API users
        can no longer perform any action on permanently deleted clusters.
        
        :param cluster_id: str
          The cluster to be deleted.
        
        
        """
        body = {}
        if cluster_id is not None: body['cluster_id'] = cluster_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/clusters/permanent-delete', body=body, headers=headers)

    def pin(self, cluster_id: str):
        """Pin cluster.
        
        Pinning a cluster ensures that the cluster will always be returned by the ListClusters API. Pinning a
        cluster that is already pinned will have no effect. This API can only be called by workspace admins.
        
        :param cluster_id: str
          <needs content added>
        
        
        """
        body = {}
        if cluster_id is not None: body['cluster_id'] = cluster_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/clusters/pin', body=body, headers=headers)

    def resize(self,
               cluster_id: str,
               *,
               autoscale: Optional[AutoScale] = None,
               num_workers: Optional[int] = None) -> Wait[ClusterDetails]:
        """Resize cluster.
        
        Resizes a cluster to have a desired number of workers. This will fail unless the cluster is in a
        `RUNNING` state.
        
        :param cluster_id: str
          The cluster to be resized.
        :param autoscale: :class:`AutoScale` (optional)
          Parameters needed in order to automatically scale clusters up and down based on load. Note:
          autoscaling works best with DB runtime versions 3.0 or later.
        :param num_workers: int (optional)
          Number of worker nodes that this cluster should have. A cluster has one Spark Driver and
          `num_workers` Executors for a total of `num_workers` + 1 Spark nodes.
          
          Note: When reading the properties of a cluster, this field reflects the desired number of workers
          rather than the actual current number of workers. For instance, if a cluster is resized from 5 to 10
          workers, this field will immediately be updated to reflect the target size of 10 workers, whereas
          the workers listed in `spark_info` will gradually increase from 5 to 10 as the new nodes are
          provisioned.
        
        :returns:
          Long-running operation waiter for :class:`ClusterDetails`.
          See :method:wait_get_cluster_running for more details.
        """
        body = {}
        if autoscale is not None: body['autoscale'] = autoscale.as_dict()
        if cluster_id is not None: body['cluster_id'] = cluster_id
        if num_workers is not None: body['num_workers'] = num_workers
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/clusters/resize', body=body, headers=headers)
        return Wait(self.wait_get_cluster_running, cluster_id=cluster_id)

    def resize_and_wait(self,
                        cluster_id: str,
                        *,
                        autoscale: Optional[AutoScale] = None,
                        num_workers: Optional[int] = None,
                        timeout=timedelta(minutes=20)) -> ClusterDetails:
        return self.resize(autoscale=autoscale, cluster_id=cluster_id,
                           num_workers=num_workers).result(timeout=timeout)

    def restart(self, cluster_id: str, *, restart_user: Optional[str] = None) -> Wait[ClusterDetails]:
        """Restart cluster.
        
        Restarts a Spark cluster with the supplied ID. If the cluster is not currently in a `RUNNING` state,
        nothing will happen.
        
        :param cluster_id: str
          The cluster to be started.
        :param restart_user: str (optional)
          <needs content added>
        
        :returns:
          Long-running operation waiter for :class:`ClusterDetails`.
          See :method:wait_get_cluster_running for more details.
        """
        body = {}
        if cluster_id is not None: body['cluster_id'] = cluster_id
        if restart_user is not None: body['restart_user'] = restart_user
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/clusters/restart', body=body, headers=headers)
        return Wait(self.wait_get_cluster_running, cluster_id=cluster_id)

    def restart_and_wait(self,
                         cluster_id: str,
                         *,
                         restart_user: Optional[str] = None,
                         timeout=timedelta(minutes=20)) -> ClusterDetails:
        return self.restart(cluster_id=cluster_id, restart_user=restart_user).result(timeout=timeout)

    def set_permissions(
            self,
            cluster_id: str,
            *,
            access_control_list: Optional[List[ClusterAccessControlRequest]] = None) -> ClusterPermissions:
        """Set cluster permissions.
        
        Sets permissions on a cluster. Clusters can inherit permissions from their root object.
        
        :param cluster_id: str
          The cluster for which to get or manage permissions.
        :param access_control_list: List[:class:`ClusterAccessControlRequest`] (optional)
        
        :returns: :class:`ClusterPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PUT', f'/api/2.0/permissions/clusters/{cluster_id}', body=body, headers=headers)
        return ClusterPermissions.from_dict(res)

    def spark_versions(self) -> GetSparkVersionsResponse:
        """List available Spark versions.
        
        Returns the list of available Spark versions. These versions can be used to launch a cluster.
        
        :returns: :class:`GetSparkVersionsResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/clusters/spark-versions', headers=headers)
        return GetSparkVersionsResponse.from_dict(res)

    def start(self, cluster_id: str) -> Wait[ClusterDetails]:
        """Start terminated cluster.
        
        Starts a terminated Spark cluster with the supplied ID. This works similar to `createCluster` except:
        
        * The previous cluster id and attributes are preserved. * The cluster starts with the last specified
        cluster size. * If the previous cluster was an autoscaling cluster, the current cluster starts with
        the minimum number of nodes. * If the cluster is not currently in a `TERMINATED` state, nothing will
        happen. * Clusters launched to run a job cannot be started.
        
        :param cluster_id: str
          The cluster to be started.
        
        :returns:
          Long-running operation waiter for :class:`ClusterDetails`.
          See :method:wait_get_cluster_running for more details.
        """
        body = {}
        if cluster_id is not None: body['cluster_id'] = cluster_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/clusters/start', body=body, headers=headers)
        return Wait(self.wait_get_cluster_running, cluster_id=cluster_id)

    def start_and_wait(self, cluster_id: str, timeout=timedelta(minutes=20)) -> ClusterDetails:
        return self.start(cluster_id=cluster_id).result(timeout=timeout)

    def unpin(self, cluster_id: str):
        """Unpin cluster.
        
        Unpinning a cluster will allow the cluster to eventually be removed from the ListClusters API.
        Unpinning a cluster that is not pinned will have no effect. This API can only be called by workspace
        admins.
        
        :param cluster_id: str
          <needs content added>
        
        
        """
        body = {}
        if cluster_id is not None: body['cluster_id'] = cluster_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/clusters/unpin', body=body, headers=headers)

    def update_permissions(
            self,
            cluster_id: str,
            *,
            access_control_list: Optional[List[ClusterAccessControlRequest]] = None) -> ClusterPermissions:
        """Update cluster permissions.
        
        Updates the permissions on a cluster. Clusters can inherit permissions from their root object.
        
        :param cluster_id: str
          The cluster for which to get or manage permissions.
        :param access_control_list: List[:class:`ClusterAccessControlRequest`] (optional)
        
        :returns: :class:`ClusterPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PATCH', f'/api/2.0/permissions/clusters/{cluster_id}', body=body, headers=headers)
        return ClusterPermissions.from_dict(res)


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
            callback: Optional[Callable[[CommandStatusResponse], None]] = None) -> CommandStatusResponse:
        deadline = time.time() + timeout.total_seconds()
        target_states = (CommandStatus.CANCELLED, )
        failure_states = (CommandStatus.ERROR, )
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
            callback: Optional[Callable[[CommandStatusResponse], None]] = None) -> CommandStatusResponse:
        deadline = time.time() + timeout.total_seconds()
        target_states = (CommandStatus.FINISHED, CommandStatus.ERROR, )
        failure_states = (CommandStatus.CANCELLED, CommandStatus.CANCELLING, )
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
            callback: Optional[Callable[[ContextStatusResponse], None]] = None) -> ContextStatusResponse:
        deadline = time.time() + timeout.total_seconds()
        target_states = (ContextStatus.RUNNING, )
        failure_states = (ContextStatus.ERROR, )
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
               cluster_id: Optional[str] = None,
               command_id: Optional[str] = None,
               context_id: Optional[str] = None) -> Wait[CommandStatusResponse]:
        """Cancel a command.
        
        Cancels a currently running command within an execution context.
        
        The command ID is obtained from a prior successful call to __execute__.
        
        :param cluster_id: str (optional)
        :param command_id: str (optional)
        :param context_id: str (optional)
        
        :returns:
          Long-running operation waiter for :class:`CommandStatusResponse`.
          See :method:wait_command_status_command_execution_cancelled for more details.
        """
        body = {}
        if cluster_id is not None: body['clusterId'] = cluster_id
        if command_id is not None: body['commandId'] = command_id
        if context_id is not None: body['contextId'] = context_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/1.2/commands/cancel', body=body, headers=headers)
        return Wait(self.wait_command_status_command_execution_cancelled,
                    cluster_id=cluster_id,
                    command_id=command_id,
                    context_id=context_id)

    def cancel_and_wait(
        self,
        *,
        cluster_id: Optional[str] = None,
        command_id: Optional[str] = None,
        context_id: Optional[str] = None,
        timeout=timedelta(minutes=20)) -> CommandStatusResponse:
        return self.cancel(cluster_id=cluster_id, command_id=command_id,
                           context_id=context_id).result(timeout=timeout)

    def command_status(self, cluster_id: str, context_id: str, command_id: str) -> CommandStatusResponse:
        """Get command info.
        
        Gets the status of and, if available, the results from a currently executing command.
        
        The command ID is obtained from a prior successful call to __execute__.
        
        :param cluster_id: str
        :param context_id: str
        :param command_id: str
        
        :returns: :class:`CommandStatusResponse`
        """

        query = {}
        if cluster_id is not None: query['clusterId'] = cluster_id
        if command_id is not None: query['commandId'] = command_id
        if context_id is not None: query['contextId'] = context_id
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/1.2/commands/status', query=query, headers=headers)
        return CommandStatusResponse.from_dict(res)

    def context_status(self, cluster_id: str, context_id: str) -> ContextStatusResponse:
        """Get status.
        
        Gets the status for an execution context.
        
        :param cluster_id: str
        :param context_id: str
        
        :returns: :class:`ContextStatusResponse`
        """

        query = {}
        if cluster_id is not None: query['clusterId'] = cluster_id
        if context_id is not None: query['contextId'] = context_id
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/1.2/contexts/status', query=query, headers=headers)
        return ContextStatusResponse.from_dict(res)

    def create(self,
               *,
               cluster_id: Optional[str] = None,
               language: Optional[Language] = None) -> Wait[ContextStatusResponse]:
        """Create an execution context.
        
        Creates an execution context for running cluster commands.
        
        If successful, this method returns the ID of the new execution context.
        
        :param cluster_id: str (optional)
          Running cluster id
        :param language: :class:`Language` (optional)
        
        :returns:
          Long-running operation waiter for :class:`ContextStatusResponse`.
          See :method:wait_context_status_command_execution_running for more details.
        """
        body = {}
        if cluster_id is not None: body['clusterId'] = cluster_id
        if language is not None: body['language'] = language.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        op_response = self._api.do('POST', '/api/1.2/contexts/create', body=body, headers=headers)
        return Wait(self.wait_context_status_command_execution_running,
                    response=Created.from_dict(op_response),
                    cluster_id=cluster_id,
                    context_id=op_response['id'])

    def create_and_wait(
        self,
        *,
        cluster_id: Optional[str] = None,
        language: Optional[Language] = None,
        timeout=timedelta(minutes=20)) -> ContextStatusResponse:
        return self.create(cluster_id=cluster_id, language=language).result(timeout=timeout)

    def destroy(self, cluster_id: str, context_id: str):
        """Delete an execution context.
        
        Deletes an execution context.
        
        :param cluster_id: str
        :param context_id: str
        
        
        """
        body = {}
        if cluster_id is not None: body['clusterId'] = cluster_id
        if context_id is not None: body['contextId'] = context_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/1.2/contexts/destroy', body=body, headers=headers)

    def execute(self,
                *,
                cluster_id: Optional[str] = None,
                command: Optional[str] = None,
                context_id: Optional[str] = None,
                language: Optional[Language] = None) -> Wait[CommandStatusResponse]:
        """Run a command.
        
        Runs a cluster command in the given execution context, using the provided language.
        
        If successful, it returns an ID for tracking the status of the command's execution.
        
        :param cluster_id: str (optional)
          Running cluster id
        :param command: str (optional)
          Executable code
        :param context_id: str (optional)
          Running context id
        :param language: :class:`Language` (optional)
        
        :returns:
          Long-running operation waiter for :class:`CommandStatusResponse`.
          See :method:wait_command_status_command_execution_finished_or_error for more details.
        """
        body = {}
        if cluster_id is not None: body['clusterId'] = cluster_id
        if command is not None: body['command'] = command
        if context_id is not None: body['contextId'] = context_id
        if language is not None: body['language'] = language.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        op_response = self._api.do('POST', '/api/1.2/commands/execute', body=body, headers=headers)
        return Wait(self.wait_command_status_command_execution_finished_or_error,
                    response=Created.from_dict(op_response),
                    cluster_id=cluster_id,
                    command_id=op_response['id'],
                    context_id=context_id)

    def execute_and_wait(
        self,
        *,
        cluster_id: Optional[str] = None,
        command: Optional[str] = None,
        context_id: Optional[str] = None,
        language: Optional[Language] = None,
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
               enabled: Optional[bool] = None,
               position: Optional[int] = None) -> CreateResponse:
        """Create init script.
        
        Creates a new global init script in this workspace.
        
        :param name: str
          The name of the script
        :param script: str
          The Base64-encoded content of the script.
        :param enabled: bool (optional)
          Specifies whether the script is enabled. The script runs only if enabled.
        :param position: int (optional)
          The position of a global init script, where 0 represents the first script to run, 1 is the second
          script to run, in ascending order.
          
          If you omit the numeric position for a new global init script, it defaults to last position. It will
          run after all current scripts. Setting any value greater than the position of the last script is
          equivalent to the last position. Example: Take three existing scripts with positions 0, 1, and 2.
          Any position of (3) or greater puts the script in the last position. If an explicit position value
          conflicts with an existing script value, your request succeeds, but the original script at that
          position and all later scripts have their positions incremented by 1.
        
        :returns: :class:`CreateResponse`
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if name is not None: body['name'] = name
        if position is not None: body['position'] = position
        if script is not None: body['script'] = script
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/global-init-scripts', body=body, headers=headers)
        return CreateResponse.from_dict(res)

    def delete(self, script_id: str):
        """Delete init script.
        
        Deletes a global init script.
        
        :param script_id: str
          The ID of the global init script.
        
        
        """

        headers = {}
        self._api.do('DELETE', f'/api/2.0/global-init-scripts/{script_id}', headers=headers)

    def get(self, script_id: str) -> GlobalInitScriptDetailsWithContent:
        """Get an init script.
        
        Gets all the details of a script, including its Base64-encoded contents.
        
        :param script_id: str
          The ID of the global init script.
        
        :returns: :class:`GlobalInitScriptDetailsWithContent`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/global-init-scripts/{script_id}', headers=headers)
        return GlobalInitScriptDetailsWithContent.from_dict(res)

    def list(self) -> Iterator['GlobalInitScriptDetails']:
        """Get init scripts.
        
        Get a list of all global init scripts for this workspace. This returns all properties for each script
        but **not** the script contents. To retrieve the contents of a script, use the [get a global init
        script](#operation/get-script) operation.
        
        :returns: Iterator over :class:`GlobalInitScriptDetails`
        """

        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/global-init-scripts', headers=headers)
        parsed = ListGlobalInitScriptsResponse.from_dict(json).scripts
        return parsed if parsed is not None else []

    def update(self,
               name: str,
               script: str,
               script_id: str,
               *,
               enabled: Optional[bool] = None,
               position: Optional[int] = None):
        """Update init script.
        
        Updates a global init script, specifying only the fields to change. All fields are optional.
        Unspecified fields retain their current value.
        
        :param name: str
          The name of the script
        :param script: str
          The Base64-encoded content of the script.
        :param script_id: str
          The ID of the global init script.
        :param enabled: bool (optional)
          Specifies whether the script is enabled. The script runs only if enabled.
        :param position: int (optional)
          The position of a script, where 0 represents the first script to run, 1 is the second script to run,
          in ascending order. To move the script to run first, set its position to 0.
          
          To move the script to the end, set its position to any value greater or equal to the position of the
          last script. Example, three existing scripts with positions 0, 1, and 2. Any position value of 2 or
          greater puts the script in the last position (2).
          
          If an explicit position value conflicts with an existing script, your request succeeds, but the
          original script at that position and all later scripts have their positions incremented by 1.
        
        
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if name is not None: body['name'] = name
        if position is not None: body['position'] = position
        if script is not None: body['script'] = script
        headers = {'Content-Type': 'application/json', }
        self._api.do('PATCH', f'/api/2.0/global-init-scripts/{script_id}', body=body, headers=headers)


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
               aws_attributes: Optional[InstancePoolAwsAttributes] = None,
               azure_attributes: Optional[InstancePoolAzureAttributes] = None,
               custom_tags: Optional[Dict[str, str]] = None,
               disk_spec: Optional[DiskSpec] = None,
               enable_elastic_disk: Optional[bool] = None,
               gcp_attributes: Optional[InstancePoolGcpAttributes] = None,
               idle_instance_autotermination_minutes: Optional[int] = None,
               max_capacity: Optional[int] = None,
               min_idle_instances: Optional[int] = None,
               preloaded_docker_images: Optional[List[DockerImage]] = None,
               preloaded_spark_versions: Optional[List[str]] = None) -> CreateInstancePoolResponse:
        """Create a new instance pool.
        
        Creates a new instance pool using idle and ready-to-use cloud instances.
        
        :param instance_pool_name: str
          Pool name requested by the user. Pool name must be unique. Length must be between 1 and 100
          characters.
        :param node_type_id: str
          This field encodes, through a single value, the resources available to each of the Spark nodes in
          this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute
          intensive workloads. A list of available node types can be retrieved by using the
          :method:clusters/listNodeTypes API call.
        :param aws_attributes: :class:`InstancePoolAwsAttributes` (optional)
          Attributes related to instance pools running on Amazon Web Services. If not specified at pool
          creation, a set of default values will be used.
        :param azure_attributes: :class:`InstancePoolAzureAttributes` (optional)
          Attributes related to instance pools running on Azure. If not specified at pool creation, a set of
          default values will be used.
        :param custom_tags: Dict[str,str] (optional)
          Additional tags for pool resources. Databricks will tag all pool resources (e.g., AWS instances and
          EBS volumes) with these tags in addition to `default_tags`. Notes:
          
          - Currently, Databricks allows at most 45 custom tags
        :param disk_spec: :class:`DiskSpec` (optional)
          Defines the specification of the disks that will be attached to all spark containers.
        :param enable_elastic_disk: bool (optional)
          Autoscaling Local Storage: when enabled, this instances in this pool will dynamically acquire
          additional disk space when its Spark workers are running low on disk space. In AWS, this feature
          requires specific AWS permissions to function correctly - refer to the User Guide for more details.
        :param gcp_attributes: :class:`InstancePoolGcpAttributes` (optional)
          Attributes related to instance pools running on Google Cloud Platform. If not specified at pool
          creation, a set of default values will be used.
        :param idle_instance_autotermination_minutes: int (optional)
          Automatically terminates the extra instances in the pool cache after they are inactive for this time
          in minutes if min_idle_instances requirement is already met. If not set, the extra pool instances
          will be automatically terminated after a default timeout. If specified, the threshold must be
          between 0 and 10000 minutes. Users can also set this value to 0 to instantly remove idle instances
          from the cache if min cache size could still hold.
        :param max_capacity: int (optional)
          Maximum number of outstanding instances to keep in the pool, including both instances used by
          clusters and idle instances. Clusters that require further instance provisioning will fail during
          upsize requests.
        :param min_idle_instances: int (optional)
          Minimum number of idle instances to keep in the instance pool
        :param preloaded_docker_images: List[:class:`DockerImage`] (optional)
          Custom Docker Image BYOC
        :param preloaded_spark_versions: List[str] (optional)
          A list containing at most one preloaded Spark image version for the pool. Pool-backed clusters
          started with the preloaded Spark version will start faster. A list of available Spark versions can
          be retrieved by using the :method:clusters/sparkVersions API call.
        
        :returns: :class:`CreateInstancePoolResponse`
        """
        body = {}
        if aws_attributes is not None: body['aws_attributes'] = aws_attributes.as_dict()
        if azure_attributes is not None: body['azure_attributes'] = azure_attributes.as_dict()
        if custom_tags is not None: body['custom_tags'] = custom_tags
        if disk_spec is not None: body['disk_spec'] = disk_spec.as_dict()
        if enable_elastic_disk is not None: body['enable_elastic_disk'] = enable_elastic_disk
        if gcp_attributes is not None: body['gcp_attributes'] = gcp_attributes.as_dict()
        if idle_instance_autotermination_minutes is not None:
            body['idle_instance_autotermination_minutes'] = idle_instance_autotermination_minutes
        if instance_pool_name is not None: body['instance_pool_name'] = instance_pool_name
        if max_capacity is not None: body['max_capacity'] = max_capacity
        if min_idle_instances is not None: body['min_idle_instances'] = min_idle_instances
        if node_type_id is not None: body['node_type_id'] = node_type_id
        if preloaded_docker_images is not None:
            body['preloaded_docker_images'] = [v.as_dict() for v in preloaded_docker_images]
        if preloaded_spark_versions is not None:
            body['preloaded_spark_versions'] = [v for v in preloaded_spark_versions]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/instance-pools/create', body=body, headers=headers)
        return CreateInstancePoolResponse.from_dict(res)

    def delete(self, instance_pool_id: str):
        """Delete an instance pool.
        
        Deletes the instance pool permanently. The idle instances in the pool are terminated asynchronously.
        
        :param instance_pool_id: str
          The instance pool to be terminated.
        
        
        """
        body = {}
        if instance_pool_id is not None: body['instance_pool_id'] = instance_pool_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/instance-pools/delete', body=body, headers=headers)

    def edit(self,
             instance_pool_id: str,
             instance_pool_name: str,
             node_type_id: str,
             *,
             custom_tags: Optional[Dict[str, str]] = None,
             idle_instance_autotermination_minutes: Optional[int] = None,
             max_capacity: Optional[int] = None,
             min_idle_instances: Optional[int] = None):
        """Edit an existing instance pool.
        
        Modifies the configuration of an existing instance pool.
        
        :param instance_pool_id: str
          Instance pool ID
        :param instance_pool_name: str
          Pool name requested by the user. Pool name must be unique. Length must be between 1 and 100
          characters.
        :param node_type_id: str
          This field encodes, through a single value, the resources available to each of the Spark nodes in
          this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute
          intensive workloads. A list of available node types can be retrieved by using the
          :method:clusters/listNodeTypes API call.
        :param custom_tags: Dict[str,str] (optional)
          Additional tags for pool resources. Databricks will tag all pool resources (e.g., AWS instances and
          EBS volumes) with these tags in addition to `default_tags`. Notes:
          
          - Currently, Databricks allows at most 45 custom tags
        :param idle_instance_autotermination_minutes: int (optional)
          Automatically terminates the extra instances in the pool cache after they are inactive for this time
          in minutes if min_idle_instances requirement is already met. If not set, the extra pool instances
          will be automatically terminated after a default timeout. If specified, the threshold must be
          between 0 and 10000 minutes. Users can also set this value to 0 to instantly remove idle instances
          from the cache if min cache size could still hold.
        :param max_capacity: int (optional)
          Maximum number of outstanding instances to keep in the pool, including both instances used by
          clusters and idle instances. Clusters that require further instance provisioning will fail during
          upsize requests.
        :param min_idle_instances: int (optional)
          Minimum number of idle instances to keep in the instance pool
        
        
        """
        body = {}
        if custom_tags is not None: body['custom_tags'] = custom_tags
        if idle_instance_autotermination_minutes is not None:
            body['idle_instance_autotermination_minutes'] = idle_instance_autotermination_minutes
        if instance_pool_id is not None: body['instance_pool_id'] = instance_pool_id
        if instance_pool_name is not None: body['instance_pool_name'] = instance_pool_name
        if max_capacity is not None: body['max_capacity'] = max_capacity
        if min_idle_instances is not None: body['min_idle_instances'] = min_idle_instances
        if node_type_id is not None: body['node_type_id'] = node_type_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/instance-pools/edit', body=body, headers=headers)

    def get(self, instance_pool_id: str) -> GetInstancePool:
        """Get instance pool information.
        
        Retrieve the information for an instance pool based on its identifier.
        
        :param instance_pool_id: str
          The canonical unique identifier for the instance pool.
        
        :returns: :class:`GetInstancePool`
        """

        query = {}
        if instance_pool_id is not None: query['instance_pool_id'] = instance_pool_id
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/instance-pools/get', query=query, headers=headers)
        return GetInstancePool.from_dict(res)

    def get_permission_levels(self, instance_pool_id: str) -> GetInstancePoolPermissionLevelsResponse:
        """Get instance pool permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param instance_pool_id: str
          The instance pool for which to get or manage permissions.
        
        :returns: :class:`GetInstancePoolPermissionLevelsResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/permissions/instance-pools/{instance_pool_id}/permissionLevels',
                           headers=headers)
        return GetInstancePoolPermissionLevelsResponse.from_dict(res)

    def get_permissions(self, instance_pool_id: str) -> InstancePoolPermissions:
        """Get instance pool permissions.
        
        Gets the permissions of an instance pool. Instance pools can inherit permissions from their root
        object.
        
        :param instance_pool_id: str
          The instance pool for which to get or manage permissions.
        
        :returns: :class:`InstancePoolPermissions`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/permissions/instance-pools/{instance_pool_id}', headers=headers)
        return InstancePoolPermissions.from_dict(res)

    def list(self) -> Iterator['InstancePoolAndStats']:
        """List instance pool info.
        
        Gets a list of instance pools with their statistics.
        
        :returns: Iterator over :class:`InstancePoolAndStats`
        """

        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/instance-pools/list', headers=headers)
        parsed = ListInstancePools.from_dict(json).instance_pools
        return parsed if parsed is not None else []

    def set_permissions(
        self,
        instance_pool_id: str,
        *,
        access_control_list: Optional[List[InstancePoolAccessControlRequest]] = None
    ) -> InstancePoolPermissions:
        """Set instance pool permissions.
        
        Sets permissions on an instance pool. Instance pools can inherit permissions from their root object.
        
        :param instance_pool_id: str
          The instance pool for which to get or manage permissions.
        :param access_control_list: List[:class:`InstancePoolAccessControlRequest`] (optional)
        
        :returns: :class:`InstancePoolPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PUT',
                           f'/api/2.0/permissions/instance-pools/{instance_pool_id}',
                           body=body,
                           headers=headers)
        return InstancePoolPermissions.from_dict(res)

    def update_permissions(
        self,
        instance_pool_id: str,
        *,
        access_control_list: Optional[List[InstancePoolAccessControlRequest]] = None
    ) -> InstancePoolPermissions:
        """Update instance pool permissions.
        
        Updates the permissions on an instance pool. Instance pools can inherit permissions from their root
        object.
        
        :param instance_pool_id: str
          The instance pool for which to get or manage permissions.
        :param access_control_list: List[:class:`InstancePoolAccessControlRequest`] (optional)
        
        :returns: :class:`InstancePoolPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PATCH',
                           f'/api/2.0/permissions/instance-pools/{instance_pool_id}',
                           body=body,
                           headers=headers)
        return InstancePoolPermissions.from_dict(res)


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
            iam_role_arn: Optional[str] = None,
            is_meta_instance_profile: Optional[bool] = None,
            skip_validation: Optional[bool] = None):
        """Register an instance profile.
        
        In the UI, you can select the instance profile when launching clusters. This API is only available to
        admin users.
        
        :param instance_profile_arn: str
          The AWS ARN of the instance profile to register with Databricks. This field is required.
        :param iam_role_arn: str (optional)
          The AWS IAM role ARN of the role associated with the instance profile. This field is required if
          your role name and instance profile name do not match and you want to use the instance profile with
          [Databricks SQL Serverless].
          
          Otherwise, this field is optional.
          
          [Databricks SQL Serverless]: https://docs.databricks.com/sql/admin/serverless.html
        :param is_meta_instance_profile: bool (optional)
          Boolean flag indicating whether the instance profile should only be used in credential passthrough
          scenarios. If true, it means the instance profile contains an meta IAM role which could assume a
          wide range of roles. Therefore it should always be used with authorization. This field is optional,
          the default value is `false`.
        :param skip_validation: bool (optional)
          By default, Databricks validates that it has sufficient permissions to launch instances with the
          instance profile. This validation uses AWS dry-run mode for the RunInstances API. If validation
          fails with an error message that does not indicate an IAM related permission issue, (e.g. “Your
          requested instance type is not supported in your requested availability zone”), you can pass this
          flag to skip the validation and forcibly add the instance profile.
        
        
        """
        body = {}
        if iam_role_arn is not None: body['iam_role_arn'] = iam_role_arn
        if instance_profile_arn is not None: body['instance_profile_arn'] = instance_profile_arn
        if is_meta_instance_profile is not None: body['is_meta_instance_profile'] = is_meta_instance_profile
        if skip_validation is not None: body['skip_validation'] = skip_validation
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/instance-profiles/add', body=body, headers=headers)

    def edit(self,
             instance_profile_arn: str,
             *,
             iam_role_arn: Optional[str] = None,
             is_meta_instance_profile: Optional[bool] = None):
        """Edit an instance profile.
        
        The only supported field to change is the optional IAM role ARN associated with the instance profile.
        It is required to specify the IAM role ARN if both of the following are true:
        
        * Your role name and instance profile name do not match. The name is the part after the last slash in
        each ARN. * You want to use the instance profile with [Databricks SQL Serverless].
        
        To understand where these fields are in the AWS console, see [Enable serverless SQL warehouses].
        
        This API is only available to admin users.
        
        [Databricks SQL Serverless]: https://docs.databricks.com/sql/admin/serverless.html
        [Enable serverless SQL warehouses]: https://docs.databricks.com/sql/admin/serverless.html
        
        :param instance_profile_arn: str
          The AWS ARN of the instance profile to register with Databricks. This field is required.
        :param iam_role_arn: str (optional)
          The AWS IAM role ARN of the role associated with the instance profile. This field is required if
          your role name and instance profile name do not match and you want to use the instance profile with
          [Databricks SQL Serverless].
          
          Otherwise, this field is optional.
          
          [Databricks SQL Serverless]: https://docs.databricks.com/sql/admin/serverless.html
        :param is_meta_instance_profile: bool (optional)
          Boolean flag indicating whether the instance profile should only be used in credential passthrough
          scenarios. If true, it means the instance profile contains an meta IAM role which could assume a
          wide range of roles. Therefore it should always be used with authorization. This field is optional,
          the default value is `false`.
        
        
        """
        body = {}
        if iam_role_arn is not None: body['iam_role_arn'] = iam_role_arn
        if instance_profile_arn is not None: body['instance_profile_arn'] = instance_profile_arn
        if is_meta_instance_profile is not None: body['is_meta_instance_profile'] = is_meta_instance_profile
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/instance-profiles/edit', body=body, headers=headers)

    def list(self) -> Iterator['InstanceProfile']:
        """List available instance profiles.
        
        List the instance profiles that the calling user can use to launch a cluster.
        
        This API is available to all users.
        
        :returns: Iterator over :class:`InstanceProfile`
        """

        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/instance-profiles/list', headers=headers)
        parsed = ListInstanceProfilesResponse.from_dict(json).instance_profiles
        return parsed if parsed is not None else []

    def remove(self, instance_profile_arn: str):
        """Remove the instance profile.
        
        Remove the instance profile with the provided ARN. Existing clusters with this instance profile will
        continue to function.
        
        This API is only accessible to admin users.
        
        :param instance_profile_arn: str
          The ARN of the instance profile to remove. This field is required.
        
        
        """
        body = {}
        if instance_profile_arn is not None: body['instance_profile_arn'] = instance_profile_arn
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/instance-profiles/remove', body=body, headers=headers)


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
        all clusters via the libraries UI.
        
        :returns: :class:`ListAllClusterLibraryStatusesResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/libraries/all-cluster-statuses', headers=headers)
        return ListAllClusterLibraryStatusesResponse.from_dict(res)

    def cluster_status(self, cluster_id: str) -> Iterator['LibraryFullStatus']:
        """Get status.
        
        Get the status of libraries on a cluster. A status will be available for all libraries installed on
        this cluster via the API or the libraries UI as well as libraries set to be installed on all clusters
        via the libraries UI. The order of returned libraries will be as follows.
        
        1. Libraries set to be installed on this cluster will be returned first. Within this group, the final
        order will be order in which the libraries were added to the cluster.
        
        2. Libraries set to be installed on all clusters are returned next. Within this group there is no
        order guarantee.
        
        3. Libraries that were previously requested on this cluster or on all clusters, but now marked for
        removal. Within this group there is no order guarantee.
        
        :param cluster_id: str
          Unique identifier of the cluster whose status should be retrieved.
        
        :returns: Iterator over :class:`LibraryFullStatus`
        """

        query = {}
        if cluster_id is not None: query['cluster_id'] = cluster_id
        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/libraries/cluster-status', query=query, headers=headers)
        parsed = ClusterLibraryStatuses.from_dict(json).library_statuses
        return parsed if parsed is not None else []

    def install(self, cluster_id: str, libraries: List[Library]):
        """Add a library.
        
        Add libraries to be installed on a cluster. The installation is asynchronous; it happens in the
        background after the completion of this request.
        
        **Note**: The actual set of libraries to be installed on a cluster is the union of the libraries
        specified via this method and the libraries set to be installed on all clusters via the libraries UI.
        
        :param cluster_id: str
          Unique identifier for the cluster on which to install these libraries.
        :param libraries: List[:class:`Library`]
          The libraries to install.
        
        
        """
        body = {}
        if cluster_id is not None: body['cluster_id'] = cluster_id
        if libraries is not None: body['libraries'] = [v.as_dict() for v in libraries]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/libraries/install', body=body, headers=headers)

    def uninstall(self, cluster_id: str, libraries: List[Library]):
        """Uninstall libraries.
        
        Set libraries to be uninstalled on a cluster. The libraries won't be uninstalled until the cluster is
        restarted. Uninstalling libraries that are not installed on the cluster will have no impact but is not
        an error.
        
        :param cluster_id: str
          Unique identifier for the cluster on which to uninstall these libraries.
        :param libraries: List[:class:`Library`]
          The libraries to uninstall.
        
        
        """
        body = {}
        if cluster_id is not None: body['cluster_id'] = cluster_id
        if libraries is not None: body['libraries'] = [v.as_dict() for v in libraries]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/libraries/uninstall', body=body, headers=headers)


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

    def get(self, policy_family_id: str) -> PolicyFamily:
        """Get policy family information.
        
        Retrieve the information for an policy family based on its identifier.
        
        :param policy_family_id: str
        
        :returns: :class:`PolicyFamily`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/policy-families/{policy_family_id}', headers=headers)
        return PolicyFamily.from_dict(res)

    def list(self,
             *,
             max_results: Optional[int] = None,
             page_token: Optional[str] = None) -> Iterator['PolicyFamily']:
        """List policy families.
        
        Retrieve a list of policy families. This API is paginated.
        
        :param max_results: int (optional)
          The max number of policy families to return.
        :param page_token: str (optional)
          A token that can be used to get the next page of results.
        
        :returns: Iterator over :class:`PolicyFamily`
        """

        query = {}
        if max_results is not None: query['max_results'] = max_results
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.0/policy-families', query=query, headers=headers)
            if 'policy_families' not in json or not json['policy_families']:
                return
            for v in json['policy_families']:
                yield PolicyFamily.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

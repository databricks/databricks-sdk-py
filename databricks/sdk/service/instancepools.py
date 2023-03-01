# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List

_LOG = logging.getLogger('databricks.sdk.service.instancepools')

# all definitions in this file are in alphabetical order


@dataclass
class CreateInstancePool:
    aws_attributes: 'InstancePoolAwsAttributes'
    azure_attributes: 'InstancePoolAzureAttributes'
    custom_tags: 'Dict[str,str]'
    disk_spec: 'DiskSpec'
    enable_elastic_disk: bool
    idle_instance_autotermination_minutes: int
    instance_pool_fleet_attributes: 'InstancePoolFleetAttributes'
    instance_pool_name: str
    max_capacity: int
    min_idle_instances: int
    node_type_id: str
    preloaded_docker_images: 'List[DockerImage]'
    preloaded_spark_versions: 'List[str]'

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
        return cls(
            aws_attributes=InstancePoolAwsAttributes.from_dict(d['aws_attributes'])
            if 'aws_attributes' in d else None,
            azure_attributes=InstancePoolAzureAttributes.from_dict(d['azure_attributes'])
            if 'azure_attributes' in d else None,
            custom_tags=d.get('custom_tags', None),
            disk_spec=DiskSpec.from_dict(d['disk_spec']) if 'disk_spec' in d else None,
            enable_elastic_disk=d.get('enable_elastic_disk', None),
            idle_instance_autotermination_minutes=d.get('idle_instance_autotermination_minutes', None),
            instance_pool_fleet_attributes=InstancePoolFleetAttributes.from_dict(
                d['instance_pool_fleet_attributes']) if 'instance_pool_fleet_attributes' in d else None,
            instance_pool_name=d.get('instance_pool_name', None),
            max_capacity=d.get('max_capacity', None),
            min_idle_instances=d.get('min_idle_instances', None),
            node_type_id=d.get('node_type_id', None),
            preloaded_docker_images=[DockerImage.from_dict(v) for v in d['preloaded_docker_images']]
            if 'preloaded_docker_images' in d and d['preloaded_docker_images'] is not None else None,
            preloaded_spark_versions=d.get('preloaded_spark_versions', None))


@dataclass
class CreateInstancePoolResponse:
    instance_pool_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.instance_pool_id: body['instance_pool_id'] = self.instance_pool_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateInstancePoolResponse':
        return cls(instance_pool_id=d.get('instance_pool_id', None))


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
class DiskSpec:
    disk_count: int
    disk_iops: int
    disk_size: int
    disk_throughput: int
    disk_type: 'DiskType'

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
                   disk_type=DiskType.from_dict(d['disk_type']) if 'disk_type' in d else None)


@dataclass
class DiskType:
    azure_disk_volume_type: 'DiskTypeAzureDiskVolumeType'
    ebs_volume_type: 'DiskTypeEbsVolumeType'

    def as_dict(self) -> dict:
        body = {}
        if self.azure_disk_volume_type: body['azure_disk_volume_type'] = self.azure_disk_volume_type.value
        if self.ebs_volume_type: body['ebs_volume_type'] = self.ebs_volume_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DiskType':
        return cls(azure_disk_volume_type=DiskTypeAzureDiskVolumeType.__members__.get(
            d['azure_disk_volume_type'], None) if 'azure_disk_volume_type' in d else None,
                   ebs_volume_type=DiskTypeEbsVolumeType.__members__.get(d['ebs_volume_type'], None)
                   if 'ebs_volume_type' in d else None)


class DiskTypeAzureDiskVolumeType(Enum):

    PREMIUM_LRS = 'PREMIUM_LRS'
    STANDARD_LRS = 'STANDARD_LRS'


class DiskTypeEbsVolumeType(Enum):

    GENERAL_PURPOSE_SSD = 'GENERAL_PURPOSE_SSD'
    THROUGHPUT_OPTIMIZED_HDD = 'THROUGHPUT_OPTIMIZED_HDD'


@dataclass
class DockerBasicAuth:
    password: str
    username: str

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
    basic_auth: 'DockerBasicAuth'
    url: str

    def as_dict(self) -> dict:
        body = {}
        if self.basic_auth: body['basic_auth'] = self.basic_auth.as_dict()
        if self.url: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DockerImage':
        return cls(basic_auth=DockerBasicAuth.from_dict(d['basic_auth']) if 'basic_auth' in d else None,
                   url=d.get('url', None))


@dataclass
class EditInstancePool:
    aws_attributes: 'InstancePoolAwsAttributes'
    azure_attributes: 'InstancePoolAzureAttributes'
    custom_tags: 'Dict[str,str]'
    disk_spec: 'DiskSpec'
    enable_elastic_disk: bool
    idle_instance_autotermination_minutes: int
    instance_pool_fleet_attributes: 'InstancePoolFleetAttributes'
    instance_pool_id: str
    instance_pool_name: str
    max_capacity: int
    min_idle_instances: int
    node_type_id: str
    preloaded_docker_images: 'List[DockerImage]'
    preloaded_spark_versions: 'List[str]'

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
        return cls(
            aws_attributes=InstancePoolAwsAttributes.from_dict(d['aws_attributes'])
            if 'aws_attributes' in d else None,
            azure_attributes=InstancePoolAzureAttributes.from_dict(d['azure_attributes'])
            if 'azure_attributes' in d else None,
            custom_tags=d.get('custom_tags', None),
            disk_spec=DiskSpec.from_dict(d['disk_spec']) if 'disk_spec' in d else None,
            enable_elastic_disk=d.get('enable_elastic_disk', None),
            idle_instance_autotermination_minutes=d.get('idle_instance_autotermination_minutes', None),
            instance_pool_fleet_attributes=InstancePoolFleetAttributes.from_dict(
                d['instance_pool_fleet_attributes']) if 'instance_pool_fleet_attributes' in d else None,
            instance_pool_id=d.get('instance_pool_id', None),
            instance_pool_name=d.get('instance_pool_name', None),
            max_capacity=d.get('max_capacity', None),
            min_idle_instances=d.get('min_idle_instances', None),
            node_type_id=d.get('node_type_id', None),
            preloaded_docker_images=[DockerImage.from_dict(v) for v in d['preloaded_docker_images']]
            if 'preloaded_docker_images' in d and d['preloaded_docker_images'] is not None else None,
            preloaded_spark_versions=d.get('preloaded_spark_versions', None))


@dataclass
class FleetLaunchTemplateOverride:
    availability_zone: str
    instance_type: str
    max_price: float
    priority: float

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
    allocation_strategy: 'FleetOnDemandOptionAllocationStrategy'
    max_total_price: float
    use_capacity_reservations_first: bool

    def as_dict(self) -> dict:
        body = {}
        if self.allocation_strategy: body['allocation_strategy'] = self.allocation_strategy.value
        if self.max_total_price: body['max_total_price'] = self.max_total_price
        if self.use_capacity_reservations_first:
            body['use_capacity_reservations_first'] = self.use_capacity_reservations_first
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FleetOnDemandOption':
        return cls(allocation_strategy=FleetOnDemandOptionAllocationStrategy.__members__.get(
            d['allocation_strategy'], None) if 'allocation_strategy' in d else None,
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
    allocation_strategy: 'FleetSpotOptionAllocationStrategy'
    instance_pools_to_use_count: int
    max_total_price: float

    def as_dict(self) -> dict:
        body = {}
        if self.allocation_strategy: body['allocation_strategy'] = self.allocation_strategy.value
        if self.instance_pools_to_use_count:
            body['instance_pools_to_use_count'] = self.instance_pools_to_use_count
        if self.max_total_price: body['max_total_price'] = self.max_total_price
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FleetSpotOption':
        return cls(allocation_strategy=FleetSpotOptionAllocationStrategy.__members__.get(
            d['allocation_strategy'], None) if 'allocation_strategy' in d else None,
                   instance_pools_to_use_count=d.get('instance_pools_to_use_count', None),
                   max_total_price=d.get('max_total_price', None))


class FleetSpotOptionAllocationStrategy(Enum):
    """lowest-price | diversified | capacity-optimized"""

    CAPACITY_OPTIMIZED = 'CAPACITY_OPTIMIZED'
    DIVERSIFIED = 'DIVERSIFIED'
    LOWEST_PRICE = 'LOWEST_PRICE'
    PRIORITIZED = 'PRIORITIZED'


@dataclass
class Get:
    """Get instance pool information"""

    instance_pool_id: str


@dataclass
class GetInstancePool:
    aws_attributes: 'InstancePoolAwsAttributes'
    azure_attributes: 'InstancePoolAzureAttributes'
    custom_tags: 'Dict[str,str]'
    default_tags: 'Dict[str,str]'
    disk_spec: 'DiskSpec'
    enable_elastic_disk: bool
    idle_instance_autotermination_minutes: int
    instance_pool_fleet_attributes: 'InstancePoolFleetAttributes'
    instance_pool_id: str
    instance_pool_name: str
    max_capacity: int
    min_idle_instances: int
    node_type_id: str
    preloaded_docker_images: 'List[DockerImage]'
    preloaded_spark_versions: 'List[str]'
    state: 'InstancePoolState'
    stats: 'InstancePoolStats'
    status: 'InstancePoolStatus'

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
        return cls(
            aws_attributes=InstancePoolAwsAttributes.from_dict(d['aws_attributes'])
            if 'aws_attributes' in d else None,
            azure_attributes=InstancePoolAzureAttributes.from_dict(d['azure_attributes'])
            if 'azure_attributes' in d else None,
            custom_tags=d.get('custom_tags', None),
            default_tags=d.get('default_tags', None),
            disk_spec=DiskSpec.from_dict(d['disk_spec']) if 'disk_spec' in d else None,
            enable_elastic_disk=d.get('enable_elastic_disk', None),
            idle_instance_autotermination_minutes=d.get('idle_instance_autotermination_minutes', None),
            instance_pool_fleet_attributes=InstancePoolFleetAttributes.from_dict(
                d['instance_pool_fleet_attributes']) if 'instance_pool_fleet_attributes' in d else None,
            instance_pool_id=d.get('instance_pool_id', None),
            instance_pool_name=d.get('instance_pool_name', None),
            max_capacity=d.get('max_capacity', None),
            min_idle_instances=d.get('min_idle_instances', None),
            node_type_id=d.get('node_type_id', None),
            preloaded_docker_images=[DockerImage.from_dict(v) for v in d['preloaded_docker_images']]
            if 'preloaded_docker_images' in d and d['preloaded_docker_images'] is not None else None,
            preloaded_spark_versions=d.get('preloaded_spark_versions', None),
            state=InstancePoolState.__members__.get(d['state'], None) if 'state' in d else None,
            stats=InstancePoolStats.from_dict(d['stats']) if 'stats' in d else None,
            status=InstancePoolStatus.from_dict(d['status']) if 'status' in d else None)


@dataclass
class InstancePoolAndStats:
    aws_attributes: 'InstancePoolAwsAttributes'
    azure_attributes: 'InstancePoolAzureAttributes'
    custom_tags: 'Dict[str,str]'
    default_tags: 'Dict[str,str]'
    disk_spec: 'DiskSpec'
    enable_elastic_disk: bool
    idle_instance_autotermination_minutes: int
    instance_pool_fleet_attributes: 'InstancePoolFleetAttributes'
    instance_pool_id: str
    instance_pool_name: str
    max_capacity: int
    min_idle_instances: int
    node_type_id: str
    preloaded_docker_images: 'List[DockerImage]'
    preloaded_spark_versions: 'List[str]'
    state: 'InstancePoolState'
    stats: 'InstancePoolStats'
    status: 'InstancePoolStatus'

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
        return cls(
            aws_attributes=InstancePoolAwsAttributes.from_dict(d['aws_attributes'])
            if 'aws_attributes' in d else None,
            azure_attributes=InstancePoolAzureAttributes.from_dict(d['azure_attributes'])
            if 'azure_attributes' in d else None,
            custom_tags=d.get('custom_tags', None),
            default_tags=d.get('default_tags', None),
            disk_spec=DiskSpec.from_dict(d['disk_spec']) if 'disk_spec' in d else None,
            enable_elastic_disk=d.get('enable_elastic_disk', None),
            idle_instance_autotermination_minutes=d.get('idle_instance_autotermination_minutes', None),
            instance_pool_fleet_attributes=InstancePoolFleetAttributes.from_dict(
                d['instance_pool_fleet_attributes']) if 'instance_pool_fleet_attributes' in d else None,
            instance_pool_id=d.get('instance_pool_id', None),
            instance_pool_name=d.get('instance_pool_name', None),
            max_capacity=d.get('max_capacity', None),
            min_idle_instances=d.get('min_idle_instances', None),
            node_type_id=d.get('node_type_id', None),
            preloaded_docker_images=[DockerImage.from_dict(v) for v in d['preloaded_docker_images']]
            if 'preloaded_docker_images' in d and d['preloaded_docker_images'] is not None else None,
            preloaded_spark_versions=d.get('preloaded_spark_versions', None),
            state=InstancePoolState.__members__.get(d['state'], None) if 'state' in d else None,
            stats=InstancePoolStats.from_dict(d['stats']) if 'stats' in d else None,
            status=InstancePoolStatus.from_dict(d['status']) if 'status' in d else None)


@dataclass
class InstancePoolAwsAttributes:
    availability: 'InstancePoolAwsAttributesAvailability'
    spot_bid_price_percent: int
    zone_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.availability: body['availability'] = self.availability.value
        if self.spot_bid_price_percent: body['spot_bid_price_percent'] = self.spot_bid_price_percent
        if self.zone_id: body['zone_id'] = self.zone_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolAwsAttributes':
        return cls(availability=InstancePoolAwsAttributesAvailability.__members__.get(
            d['availability'], None) if 'availability' in d else None,
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
    availability: 'InstancePoolAzureAttributesAvailability'
    spot_bid_max_price: float

    def as_dict(self) -> dict:
        body = {}
        if self.availability: body['availability'] = self.availability.value
        if self.spot_bid_max_price: body['spot_bid_max_price'] = self.spot_bid_max_price
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolAzureAttributes':
        return cls(availability=InstancePoolAzureAttributesAvailability.__members__.get(
            d['availability'], None) if 'availability' in d else None,
                   spot_bid_max_price=d.get('spot_bid_max_price', None))


class InstancePoolAzureAttributesAvailability(Enum):
    """Shows the Availability type used for the spot nodes.
    
    The default value is defined by InstancePoolConf.instancePoolDefaultAzureAvailability"""

    ON_DEMAND_AZURE = 'ON_DEMAND_AZURE'
    SPOT_AZURE = 'SPOT_AZURE'
    SPOT_WITH_FALLBACK_AZURE = 'SPOT_WITH_FALLBACK_AZURE'


@dataclass
class InstancePoolFleetAttributes:
    fleet_on_demand_option: 'FleetOnDemandOption'
    fleet_spot_option: 'FleetSpotOption'
    launch_template_overrides: 'List[FleetLaunchTemplateOverride]'

    def as_dict(self) -> dict:
        body = {}
        if self.fleet_on_demand_option: body['fleet_on_demand_option'] = self.fleet_on_demand_option.as_dict()
        if self.fleet_spot_option: body['fleet_spot_option'] = self.fleet_spot_option.as_dict()
        if self.launch_template_overrides:
            body['launch_template_overrides'] = [v.as_dict() for v in self.launch_template_overrides]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolFleetAttributes':
        return cls(
            fleet_on_demand_option=FleetOnDemandOption.from_dict(d['fleet_on_demand_option'])
            if 'fleet_on_demand_option' in d else None,
            fleet_spot_option=FleetSpotOption.from_dict(d['fleet_spot_option'])
            if 'fleet_spot_option' in d else None,
            launch_template_overrides=[
                FleetLaunchTemplateOverride.from_dict(v) for v in d['launch_template_overrides']
            ] if 'launch_template_overrides' in d and d['launch_template_overrides'] is not None else None)


class InstancePoolState(Enum):
    """Current state of the instance pool."""

    ACTIVE = 'ACTIVE'
    DELETED = 'DELETED'
    STOPPED = 'STOPPED'


@dataclass
class InstancePoolStats:
    idle_count: int
    pending_idle_count: int
    pending_used_count: int
    used_count: int

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
    pending_instance_errors: 'List[PendingInstanceError]'

    def as_dict(self) -> dict:
        body = {}
        if self.pending_instance_errors:
            body['pending_instance_errors'] = [v.as_dict() for v in self.pending_instance_errors]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstancePoolStatus':
        return cls(
            pending_instance_errors=[PendingInstanceError.from_dict(v) for v in d['pending_instance_errors']]
            if 'pending_instance_errors' in d and d['pending_instance_errors'] is not None else None)


@dataclass
class ListInstancePools:
    instance_pools: 'List[InstancePoolAndStats]'

    def as_dict(self) -> dict:
        body = {}
        if self.instance_pools: body['instance_pools'] = [v.as_dict() for v in self.instance_pools]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListInstancePools':
        return cls(instance_pools=[InstancePoolAndStats.from_dict(v) for v in d['instance_pools']]
                   if 'instance_pools' in d and d['instance_pools'] is not None else None)


@dataclass
class PendingInstanceError:
    instance_id: str
    message: str

    def as_dict(self) -> dict:
        body = {}
        if self.instance_id: body['instance_id'] = self.instance_id
        if self.message: body['message'] = self.message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PendingInstanceError':
        return cls(instance_id=d.get('instance_id', None), message=d.get('message', None))


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
            request = Get(instance_pool_id=instance_pool_id)

        query = {}
        if instance_pool_id: query['instance_pool_id'] = request.instance_pool_id

        json = self._api.do('GET', '/api/2.0/instance-pools/get', query=query)
        return GetInstancePool.from_dict(json)

    def list(self) -> Iterator[InstancePoolAndStats]:
        """List instance pool info.
        
        Gets a list of instance pools with their statistics."""

        json = self._api.do('GET', '/api/2.0/instance-pools/list')
        return [InstancePoolAndStats.from_dict(v) for v in json['instance_pools']]

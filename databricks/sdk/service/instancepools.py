# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class CreateInstancePool:

    # Attributes related to pool running on Amazon Web Services. If not
    # specified at pool creation, a set of default values will be used.
    aws_attributes: "InstancePoolAwsAttributes"
    # Attributes related to pool running on Azure. If not specified at pool
    # creation, a set of default values will be used.
    azure_attributes: "InstancePoolAzureAttributes"
    # Additional tags for pool resources. Databricks will tag all pool resources
    # (e.g., AWS instances and EBS volumes) with these tags in addition to
    # `default_tags`. Notes:
    #
    # - Currently, Databricks allows at most 45 custom tags
    custom_tags: "Dict[str,str]"
    # Defines the specification of the disks that will be attached to all spark
    # containers.
    disk_spec: "DiskSpec"
    # Autoscaling Local Storage: when enabled, this instances in this pool will
    # dynamically acquire additional disk space when its Spark workers are
    # running low on disk space. In AWS, this feature requires specific AWS
    # permissions to function correctly - refer to the User Guide for more
    # details.
    enable_elastic_disk: bool
    # Automatically terminates the extra instances in the pool cache after they
    # are inactive for this time in minutes if min_idle_instances requirement is
    # already met. If not set, the extra pool instances will be automatically
    # terminated after a default timeout. If specified, the threshold must be
    # between 0 and 10000 minutes. Users can also set this value to 0 to
    # instantly remove idle instances from the cache if min cache size could
    # still hold.
    idle_instance_autotermination_minutes: int
    # The fleet related setting to power the instance pool.
    instance_pool_fleet_attributes: "InstancePoolFleetAttributes"
    # Pool name requested by the user. Pool name must be unique. Length must be
    # between 1 and 100 characters.
    instance_pool_name: str
    # Maximum number of outstanding instances to keep in the pool, including
    # both instances used by clusters and idle instances. Clusters that require
    # further instance provisioning will fail during upsize requests.
    max_capacity: int
    # Minimum number of idle instances to keep in the instance pool
    min_idle_instances: int
    # This field encodes, through a single value, the resources available to
    # each of the Spark nodes in this cluster. For example, the Spark nodes can
    # be provisioned and optimized for memory or compute intensive workloads. A
    # list of available node types can be retrieved by using the
    # :method:clusters/listNodeTypes API call.
    node_type_id: str
    # Custom Docker Image BYOC
    preloaded_docker_images: "List[DockerImage]"
    # A list of preloaded Spark image versions for the pool. Pool-backed
    # clusters started with the preloaded Spark version will start faster. A
    # list of available Spark versions can be retrieved by using the
    # :method:clusters/sparkVersions API call.
    preloaded_spark_versions: "List[str]"

    def as_dict(self) -> dict:
        body = {}
        if self.aws_attributes:
            body["aws_attributes"] = self.aws_attributes.as_dict()
        if self.azure_attributes:
            body["azure_attributes"] = self.azure_attributes.as_dict()
        if self.custom_tags:
            body["custom_tags"] = self.custom_tags
        if self.disk_spec:
            body["disk_spec"] = self.disk_spec.as_dict()
        if self.enable_elastic_disk:
            body["enable_elastic_disk"] = self.enable_elastic_disk
        if self.idle_instance_autotermination_minutes:
            body[
                "idle_instance_autotermination_minutes"
            ] = self.idle_instance_autotermination_minutes
        if self.instance_pool_fleet_attributes:
            body[
                "instance_pool_fleet_attributes"
            ] = self.instance_pool_fleet_attributes.as_dict()
        if self.instance_pool_name:
            body["instance_pool_name"] = self.instance_pool_name
        if self.max_capacity:
            body["max_capacity"] = self.max_capacity
        if self.min_idle_instances:
            body["min_idle_instances"] = self.min_idle_instances
        if self.node_type_id:
            body["node_type_id"] = self.node_type_id
        if self.preloaded_docker_images:
            body["preloaded_docker_images"] = [
                v.as_dict() for v in self.preloaded_docker_images
            ]
        if self.preloaded_spark_versions:
            body["preloaded_spark_versions"] = [
                v for v in self.preloaded_spark_versions
            ]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateInstancePool":
        return cls(
            aws_attributes=InstancePoolAwsAttributes.from_dict(d["aws_attributes"])
            if "aws_attributes" in d
            else None,
            azure_attributes=InstancePoolAzureAttributes.from_dict(
                d["azure_attributes"]
            )
            if "azure_attributes" in d
            else None,
            custom_tags=d.get("custom_tags", None),
            disk_spec=DiskSpec.from_dict(d["disk_spec"]) if "disk_spec" in d else None,
            enable_elastic_disk=d.get("enable_elastic_disk", None),
            idle_instance_autotermination_minutes=d.get(
                "idle_instance_autotermination_minutes", None
            ),
            instance_pool_fleet_attributes=InstancePoolFleetAttributes.from_dict(
                d["instance_pool_fleet_attributes"]
            )
            if "instance_pool_fleet_attributes" in d
            else None,
            instance_pool_name=d.get("instance_pool_name", None),
            max_capacity=d.get("max_capacity", None),
            min_idle_instances=d.get("min_idle_instances", None),
            node_type_id=d.get("node_type_id", None),
            preloaded_docker_images=[
                DockerImage.from_dict(v) for v in d["preloaded_docker_images"]
            ]
            if "preloaded_docker_images" in d
            else None,
            preloaded_spark_versions=d.get("preloaded_spark_versions", None),
        )


@dataclass
class CreateInstancePoolResponse:

    # The ID of the created instance pool.
    instance_pool_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.instance_pool_id:
            body["instance_pool_id"] = self.instance_pool_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateInstancePoolResponse":
        return cls(
            instance_pool_id=d.get("instance_pool_id", None),
        )


@dataclass
class DeleteInstancePool:

    # The instance pool to be terminated.
    instance_pool_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.instance_pool_id:
            body["instance_pool_id"] = self.instance_pool_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteInstancePool":
        return cls(
            instance_pool_id=d.get("instance_pool_id", None),
        )


@dataclass
class DiskSpec:

    # The number of disks launched for each instance: - This feature is only
    # enabled for supported node types. - Users can choose up to the limit of
    # the disks supported by the node type. - For node types with no OS disk, at
    # least one disk must be specified; otherwise, cluster creation will fail.
    #
    # If disks are attached, Databricks will configure Spark to use only the
    # disks for scratch storage, because heterogenously sized scratch devices
    # can lead to inefficient disk utilization. If no disks are attached,
    # Databricks will configure Spark to use instance store disks.
    #
    # Note: If disks are specified, then the Spark configuration
    # `spark.local.dir` will be overridden.
    #
    # Disks will be mounted at: - For AWS: `/ebs0`, `/ebs1`, and etc. - For
    # Azure: `/remote_volume0`, `/remote_volume1`, and etc.
    disk_count: int

    disk_iops: int
    # The size of each disk (in GiB) launched for each instance. Values must
    # fall into the supported range for a particular instance type.
    #
    # For AWS: - General Purpose SSD: 100 - 4096 GiB - Throughput Optimized HDD:
    # 500 - 4096 GiB
    #
    # For Azure: - Premium LRS (SSD): 1 - 1023 GiB - Standard LRS (HDD): 1- 1023
    # GiB
    disk_size: int

    disk_throughput: int
    # The type of disks that will be launched with this cluster.
    disk_type: "DiskType"

    def as_dict(self) -> dict:
        body = {}
        if self.disk_count:
            body["disk_count"] = self.disk_count
        if self.disk_iops:
            body["disk_iops"] = self.disk_iops
        if self.disk_size:
            body["disk_size"] = self.disk_size
        if self.disk_throughput:
            body["disk_throughput"] = self.disk_throughput
        if self.disk_type:
            body["disk_type"] = self.disk_type.as_dict()

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DiskSpec":
        return cls(
            disk_count=d.get("disk_count", None),
            disk_iops=d.get("disk_iops", None),
            disk_size=d.get("disk_size", None),
            disk_throughput=d.get("disk_throughput", None),
            disk_type=DiskType.from_dict(d["disk_type"]) if "disk_type" in d else None,
        )


@dataclass
class DiskType:

    azure_disk_volume_type: "DiskTypeAzureDiskVolumeType"

    ebs_volume_type: "DiskTypeEbsVolumeType"

    def as_dict(self) -> dict:
        body = {}
        if self.azure_disk_volume_type:
            body["azure_disk_volume_type"] = self.azure_disk_volume_type.value
        if self.ebs_volume_type:
            body["ebs_volume_type"] = self.ebs_volume_type.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DiskType":
        return cls(
            azure_disk_volume_type=DiskTypeAzureDiskVolumeType(
                d["azure_disk_volume_type"]
            )
            if "azure_disk_volume_type" in d
            else None,
            ebs_volume_type=DiskTypeEbsVolumeType(d["ebs_volume_type"])
            if "ebs_volume_type" in d
            else None,
        )


class DiskTypeAzureDiskVolumeType(Enum):

    PREMIUM_LRS = "PREMIUM_LRS"
    STANDARD_LRS = "STANDARD_LRS"


class DiskTypeEbsVolumeType(Enum):

    GENERAL_PURPOSE_SSD = "GENERAL_PURPOSE_SSD"
    THROUGHPUT_OPTIMIZED_HDD = "THROUGHPUT_OPTIMIZED_HDD"


@dataclass
class DockerBasicAuth:

    password: str

    username: str

    def as_dict(self) -> dict:
        body = {}
        if self.password:
            body["password"] = self.password
        if self.username:
            body["username"] = self.username

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DockerBasicAuth":
        return cls(
            password=d.get("password", None),
            username=d.get("username", None),
        )


@dataclass
class DockerImage:

    basic_auth: "DockerBasicAuth"
    # URL of the docker image.
    url: str

    def as_dict(self) -> dict:
        body = {}
        if self.basic_auth:
            body["basic_auth"] = self.basic_auth.as_dict()
        if self.url:
            body["url"] = self.url

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DockerImage":
        return cls(
            basic_auth=DockerBasicAuth.from_dict(d["basic_auth"])
            if "basic_auth" in d
            else None,
            url=d.get("url", None),
        )


@dataclass
class EditInstancePool:

    # Attributes related to pool running on Amazon Web Services. If not
    # specified at pool creation, a set of default values will be used.
    aws_attributes: "InstancePoolAwsAttributes"
    # Attributes related to pool running on Azure. If not specified at pool
    # creation, a set of default values will be used.
    azure_attributes: "InstancePoolAzureAttributes"
    # Additional tags for pool resources. Databricks will tag all pool resources
    # (e.g., AWS instances and EBS volumes) with these tags in addition to
    # `default_tags`. Notes:
    #
    # - Currently, Databricks allows at most 45 custom tags
    custom_tags: "Dict[str,str]"
    # Defines the specification of the disks that will be attached to all spark
    # containers.
    disk_spec: "DiskSpec"
    # Autoscaling Local Storage: when enabled, this instances in this pool will
    # dynamically acquire additional disk space when its Spark workers are
    # running low on disk space. In AWS, this feature requires specific AWS
    # permissions to function correctly - refer to the User Guide for more
    # details.
    enable_elastic_disk: bool
    # Automatically terminates the extra instances in the pool cache after they
    # are inactive for this time in minutes if min_idle_instances requirement is
    # already met. If not set, the extra pool instances will be automatically
    # terminated after a default timeout. If specified, the threshold must be
    # between 0 and 10000 minutes. Users can also set this value to 0 to
    # instantly remove idle instances from the cache if min cache size could
    # still hold.
    idle_instance_autotermination_minutes: int
    # The fleet related setting to power the instance pool.
    instance_pool_fleet_attributes: "InstancePoolFleetAttributes"
    # Instance pool ID
    instance_pool_id: str
    # Pool name requested by the user. Pool name must be unique. Length must be
    # between 1 and 100 characters.
    instance_pool_name: str
    # Maximum number of outstanding instances to keep in the pool, including
    # both instances used by clusters and idle instances. Clusters that require
    # further instance provisioning will fail during upsize requests.
    max_capacity: int
    # Minimum number of idle instances to keep in the instance pool
    min_idle_instances: int
    # This field encodes, through a single value, the resources available to
    # each of the Spark nodes in this cluster. For example, the Spark nodes can
    # be provisioned and optimized for memory or compute intensive workloads. A
    # list of available node types can be retrieved by using the
    # :method:clusters/listNodeTypes API call.
    node_type_id: str
    # Custom Docker Image BYOC
    preloaded_docker_images: "List[DockerImage]"
    # A list of preloaded Spark image versions for the pool. Pool-backed
    # clusters started with the preloaded Spark version will start faster. A
    # list of available Spark versions can be retrieved by using the
    # :method:clusters/sparkVersions API call.
    preloaded_spark_versions: "List[str]"

    def as_dict(self) -> dict:
        body = {}
        if self.aws_attributes:
            body["aws_attributes"] = self.aws_attributes.as_dict()
        if self.azure_attributes:
            body["azure_attributes"] = self.azure_attributes.as_dict()
        if self.custom_tags:
            body["custom_tags"] = self.custom_tags
        if self.disk_spec:
            body["disk_spec"] = self.disk_spec.as_dict()
        if self.enable_elastic_disk:
            body["enable_elastic_disk"] = self.enable_elastic_disk
        if self.idle_instance_autotermination_minutes:
            body[
                "idle_instance_autotermination_minutes"
            ] = self.idle_instance_autotermination_minutes
        if self.instance_pool_fleet_attributes:
            body[
                "instance_pool_fleet_attributes"
            ] = self.instance_pool_fleet_attributes.as_dict()
        if self.instance_pool_id:
            body["instance_pool_id"] = self.instance_pool_id
        if self.instance_pool_name:
            body["instance_pool_name"] = self.instance_pool_name
        if self.max_capacity:
            body["max_capacity"] = self.max_capacity
        if self.min_idle_instances:
            body["min_idle_instances"] = self.min_idle_instances
        if self.node_type_id:
            body["node_type_id"] = self.node_type_id
        if self.preloaded_docker_images:
            body["preloaded_docker_images"] = [
                v.as_dict() for v in self.preloaded_docker_images
            ]
        if self.preloaded_spark_versions:
            body["preloaded_spark_versions"] = [
                v for v in self.preloaded_spark_versions
            ]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "EditInstancePool":
        return cls(
            aws_attributes=InstancePoolAwsAttributes.from_dict(d["aws_attributes"])
            if "aws_attributes" in d
            else None,
            azure_attributes=InstancePoolAzureAttributes.from_dict(
                d["azure_attributes"]
            )
            if "azure_attributes" in d
            else None,
            custom_tags=d.get("custom_tags", None),
            disk_spec=DiskSpec.from_dict(d["disk_spec"]) if "disk_spec" in d else None,
            enable_elastic_disk=d.get("enable_elastic_disk", None),
            idle_instance_autotermination_minutes=d.get(
                "idle_instance_autotermination_minutes", None
            ),
            instance_pool_fleet_attributes=InstancePoolFleetAttributes.from_dict(
                d["instance_pool_fleet_attributes"]
            )
            if "instance_pool_fleet_attributes" in d
            else None,
            instance_pool_id=d.get("instance_pool_id", None),
            instance_pool_name=d.get("instance_pool_name", None),
            max_capacity=d.get("max_capacity", None),
            min_idle_instances=d.get("min_idle_instances", None),
            node_type_id=d.get("node_type_id", None),
            preloaded_docker_images=[
                DockerImage.from_dict(v) for v in d["preloaded_docker_images"]
            ]
            if "preloaded_docker_images" in d
            else None,
            preloaded_spark_versions=d.get("preloaded_spark_versions", None),
        )


@dataclass
class FleetLaunchTemplateOverride:

    # User-assigned preferred availability zone. It will adjust to the default
    # zone of the worker environment if the preferred zone does not exist in the
    # subnet.
    availability_zone: str

    instance_type: str
    # The maximum price per unit hour that you are willing to pay for a Spot
    # Instance.
    max_price: float
    # The priority for the launch template override. If AllocationStrategy is
    # set to prioritized, EC2 Fleet uses priority to determine which launch
    # template override or to use first in fulfilling On-Demand capacity. The
    # highest priority is launched first. Valid values are whole numbers
    # starting at 0. The lower the number, the higher the priority. If no number
    # is set, the launch template override has the lowest priority.
    priority: float

    def as_dict(self) -> dict:
        body = {}
        if self.availability_zone:
            body["availability_zone"] = self.availability_zone
        if self.instance_type:
            body["instance_type"] = self.instance_type
        if self.max_price:
            body["max_price"] = self.max_price
        if self.priority:
            body["priority"] = self.priority

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "FleetLaunchTemplateOverride":
        return cls(
            availability_zone=d.get("availability_zone", None),
            instance_type=d.get("instance_type", None),
            max_price=d.get("max_price", None),
            priority=d.get("priority", None),
        )


@dataclass
class FleetOnDemandOption:

    # Only lowest-price and prioritized are allowed
    allocation_strategy: "FleetOnDemandOptionAllocationStrategy"
    # The maximum amount per hour for On-Demand Instances that you're willing to
    # pay.
    max_total_price: float
    # If you specify use-capacity-reservations-first, the fleet uses unused
    # Capacity Reservations to fulfill On-Demand capacity up to the target
    # On-Demand capacity. If multiple instance pools have unused Capacity
    # Reservations, the On-Demand allocation strategy (lowest-price or
    # prioritized) is applied. If the number of unused Capacity Reservations is
    # less than the On-Demand target capacity, the remaining On-Demand target
    # capacity is launched according to the On-Demand allocation strategy
    # (lowest-price or prioritized).
    use_capacity_reservations_first: bool

    def as_dict(self) -> dict:
        body = {}
        if self.allocation_strategy:
            body["allocation_strategy"] = self.allocation_strategy.value
        if self.max_total_price:
            body["max_total_price"] = self.max_total_price
        if self.use_capacity_reservations_first:
            body[
                "use_capacity_reservations_first"
            ] = self.use_capacity_reservations_first

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "FleetOnDemandOption":
        return cls(
            allocation_strategy=FleetOnDemandOptionAllocationStrategy(
                d["allocation_strategy"]
            )
            if "allocation_strategy" in d
            else None,
            max_total_price=d.get("max_total_price", None),
            use_capacity_reservations_first=d.get(
                "use_capacity_reservations_first", None
            ),
        )


class FleetOnDemandOptionAllocationStrategy(Enum):
    """Only lowest-price and prioritized are allowed"""

    CAPACITY_OPTIMIZED = "CAPACITY_OPTIMIZED"
    DIVERSIFIED = "DIVERSIFIED"
    LOWEST_PRICE = "LOWEST_PRICE"
    PRIORITIZED = "PRIORITIZED"


@dataclass
class FleetSpotOption:

    # lowest-price | diversified | capacity-optimized
    allocation_strategy: "FleetSpotOptionAllocationStrategy"
    # The number of Spot pools across which to allocate your target Spot
    # capacity. Valid only when Spot Allocation Strategy is set to lowest-price.
    # EC2 Fleet selects the cheapest Spot pools and evenly allocates your target
    # Spot capacity across the number of Spot pools that you specify.
    instance_pools_to_use_count: int
    # The maximum amount per hour for Spot Instances that you're willing to pay.
    max_total_price: float

    def as_dict(self) -> dict:
        body = {}
        if self.allocation_strategy:
            body["allocation_strategy"] = self.allocation_strategy.value
        if self.instance_pools_to_use_count:
            body["instance_pools_to_use_count"] = self.instance_pools_to_use_count
        if self.max_total_price:
            body["max_total_price"] = self.max_total_price

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "FleetSpotOption":
        return cls(
            allocation_strategy=FleetSpotOptionAllocationStrategy(
                d["allocation_strategy"]
            )
            if "allocation_strategy" in d
            else None,
            instance_pools_to_use_count=d.get("instance_pools_to_use_count", None),
            max_total_price=d.get("max_total_price", None),
        )


class FleetSpotOptionAllocationStrategy(Enum):
    """lowest-price | diversified | capacity-optimized"""

    CAPACITY_OPTIMIZED = "CAPACITY_OPTIMIZED"
    DIVERSIFIED = "DIVERSIFIED"
    LOWEST_PRICE = "LOWEST_PRICE"
    PRIORITIZED = "PRIORITIZED"


@dataclass
class Get:
    """Get instance pool information"""

    # The canonical unique identifier for the instance pool.
    instance_pool_id: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.instance_pool_id:
            body["instance_pool_id"] = self.instance_pool_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Get":
        return cls(
            instance_pool_id=d.get("instance_pool_id", None),
        )


@dataclass
class GetInstancePool:

    # Attributes related to pool running on Amazon Web Services. If not
    # specified at pool creation, a set of default values will be used.
    aws_attributes: "InstancePoolAwsAttributes"
    # Attributes related to pool running on Azure. If not specified at pool
    # creation, a set of default values will be used.
    azure_attributes: "InstancePoolAzureAttributes"
    # Additional tags for pool resources. Databricks will tag all pool resources
    # (e.g., AWS instances and EBS volumes) with these tags in addition to
    # `default_tags`. Notes:
    #
    # - Currently, Databricks allows at most 45 custom tags
    custom_tags: "Dict[str,str]"
    # Tags that are added by Databricks regardless of any `custom_tags`,
    # including:
    #
    # - Vendor: Databricks
    #
    # - InstancePoolCreator: <user_id_of_creator>
    #
    # - InstancePoolName: <name_of_pool>
    #
    # - InstancePoolId: <id_of_pool>
    default_tags: "Dict[str,str]"
    # Defines the specification of the disks that will be attached to all spark
    # containers.
    disk_spec: "DiskSpec"
    # Autoscaling Local Storage: when enabled, this instances in this pool will
    # dynamically acquire additional disk space when its Spark workers are
    # running low on disk space. In AWS, this feature requires specific AWS
    # permissions to function correctly - refer to the User Guide for more
    # details.
    enable_elastic_disk: bool
    # Automatically terminates the extra instances in the pool cache after they
    # are inactive for this time in minutes if min_idle_instances requirement is
    # already met. If not set, the extra pool instances will be automatically
    # terminated after a default timeout. If specified, the threshold must be
    # between 0 and 10000 minutes. Users can also set this value to 0 to
    # instantly remove idle instances from the cache if min cache size could
    # still hold.
    idle_instance_autotermination_minutes: int
    # The fleet related setting to power the instance pool.
    instance_pool_fleet_attributes: "InstancePoolFleetAttributes"
    # Canonical unique identifier for the pool.
    instance_pool_id: str
    # Pool name requested by the user. Pool name must be unique. Length must be
    # between 1 and 100 characters.
    instance_pool_name: str
    # Maximum number of outstanding instances to keep in the pool, including
    # both instances used by clusters and idle instances. Clusters that require
    # further instance provisioning will fail during upsize requests.
    max_capacity: int
    # Minimum number of idle instances to keep in the instance pool
    min_idle_instances: int
    # This field encodes, through a single value, the resources available to
    # each of the Spark nodes in this cluster. For example, the Spark nodes can
    # be provisioned and optimized for memory or compute intensive workloads. A
    # list of available node types can be retrieved by using the
    # :method:clusters/listNodeTypes API call.
    node_type_id: str
    # Custom Docker Image BYOC
    preloaded_docker_images: "List[DockerImage]"
    # A list of preloaded Spark image versions for the pool. Pool-backed
    # clusters started with the preloaded Spark version will start faster. A
    # list of available Spark versions can be retrieved by using the
    # :method:clusters/sparkVersions API call.
    preloaded_spark_versions: "List[str]"
    # Current state of the instance pool.
    state: "InstancePoolState"
    # Usage statistics about the instance pool.
    stats: "InstancePoolStats"
    # Status of failed pending instances in the pool.
    status: "InstancePoolStatus"

    def as_dict(self) -> dict:
        body = {}
        if self.aws_attributes:
            body["aws_attributes"] = self.aws_attributes.as_dict()
        if self.azure_attributes:
            body["azure_attributes"] = self.azure_attributes.as_dict()
        if self.custom_tags:
            body["custom_tags"] = self.custom_tags
        if self.default_tags:
            body["default_tags"] = self.default_tags
        if self.disk_spec:
            body["disk_spec"] = self.disk_spec.as_dict()
        if self.enable_elastic_disk:
            body["enable_elastic_disk"] = self.enable_elastic_disk
        if self.idle_instance_autotermination_minutes:
            body[
                "idle_instance_autotermination_minutes"
            ] = self.idle_instance_autotermination_minutes
        if self.instance_pool_fleet_attributes:
            body[
                "instance_pool_fleet_attributes"
            ] = self.instance_pool_fleet_attributes.as_dict()
        if self.instance_pool_id:
            body["instance_pool_id"] = self.instance_pool_id
        if self.instance_pool_name:
            body["instance_pool_name"] = self.instance_pool_name
        if self.max_capacity:
            body["max_capacity"] = self.max_capacity
        if self.min_idle_instances:
            body["min_idle_instances"] = self.min_idle_instances
        if self.node_type_id:
            body["node_type_id"] = self.node_type_id
        if self.preloaded_docker_images:
            body["preloaded_docker_images"] = [
                v.as_dict() for v in self.preloaded_docker_images
            ]
        if self.preloaded_spark_versions:
            body["preloaded_spark_versions"] = [
                v for v in self.preloaded_spark_versions
            ]
        if self.state:
            body["state"] = self.state.value
        if self.stats:
            body["stats"] = self.stats.as_dict()
        if self.status:
            body["status"] = self.status.as_dict()

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetInstancePool":
        return cls(
            aws_attributes=InstancePoolAwsAttributes.from_dict(d["aws_attributes"])
            if "aws_attributes" in d
            else None,
            azure_attributes=InstancePoolAzureAttributes.from_dict(
                d["azure_attributes"]
            )
            if "azure_attributes" in d
            else None,
            custom_tags=d.get("custom_tags", None),
            default_tags=d.get("default_tags", None),
            disk_spec=DiskSpec.from_dict(d["disk_spec"]) if "disk_spec" in d else None,
            enable_elastic_disk=d.get("enable_elastic_disk", None),
            idle_instance_autotermination_minutes=d.get(
                "idle_instance_autotermination_minutes", None
            ),
            instance_pool_fleet_attributes=InstancePoolFleetAttributes.from_dict(
                d["instance_pool_fleet_attributes"]
            )
            if "instance_pool_fleet_attributes" in d
            else None,
            instance_pool_id=d.get("instance_pool_id", None),
            instance_pool_name=d.get("instance_pool_name", None),
            max_capacity=d.get("max_capacity", None),
            min_idle_instances=d.get("min_idle_instances", None),
            node_type_id=d.get("node_type_id", None),
            preloaded_docker_images=[
                DockerImage.from_dict(v) for v in d["preloaded_docker_images"]
            ]
            if "preloaded_docker_images" in d
            else None,
            preloaded_spark_versions=d.get("preloaded_spark_versions", None),
            state=InstancePoolState(d["state"]) if "state" in d else None,
            stats=InstancePoolStats.from_dict(d["stats"]) if "stats" in d else None,
            status=InstancePoolStatus.from_dict(d["status"]) if "status" in d else None,
        )


@dataclass
class InstancePoolAndStats:

    # Attributes related to pool running on Amazon Web Services. If not
    # specified at pool creation, a set of default values will be used.
    aws_attributes: "InstancePoolAwsAttributes"
    # Attributes related to pool running on Azure. If not specified at pool
    # creation, a set of default values will be used.
    azure_attributes: "InstancePoolAzureAttributes"
    # Additional tags for pool resources. Databricks will tag all pool resources
    # (e.g., AWS instances and EBS volumes) with these tags in addition to
    # `default_tags`. Notes:
    #
    # - Currently, Databricks allows at most 45 custom tags
    custom_tags: "Dict[str,str]"
    # Tags that are added by Databricks regardless of any `custom_tags`,
    # including:
    #
    # - Vendor: Databricks
    #
    # - InstancePoolCreator: <user_id_of_creator>
    #
    # - InstancePoolName: <name_of_pool>
    #
    # - InstancePoolId: <id_of_pool>
    default_tags: "Dict[str,str]"
    # Defines the specification of the disks that will be attached to all spark
    # containers.
    disk_spec: "DiskSpec"
    # Autoscaling Local Storage: when enabled, this instances in this pool will
    # dynamically acquire additional disk space when its Spark workers are
    # running low on disk space. In AWS, this feature requires specific AWS
    # permissions to function correctly - refer to the User Guide for more
    # details.
    enable_elastic_disk: bool
    # Automatically terminates the extra instances in the pool cache after they
    # are inactive for this time in minutes if min_idle_instances requirement is
    # already met. If not set, the extra pool instances will be automatically
    # terminated after a default timeout. If specified, the threshold must be
    # between 0 and 10000 minutes. Users can also set this value to 0 to
    # instantly remove idle instances from the cache if min cache size could
    # still hold.
    idle_instance_autotermination_minutes: int
    # The fleet related setting to power the instance pool.
    instance_pool_fleet_attributes: "InstancePoolFleetAttributes"
    # Canonical unique identifier for the pool.
    instance_pool_id: str
    # Pool name requested by the user. Pool name must be unique. Length must be
    # between 1 and 100 characters.
    instance_pool_name: str
    # Maximum number of outstanding instances to keep in the pool, including
    # both instances used by clusters and idle instances. Clusters that require
    # further instance provisioning will fail during upsize requests.
    max_capacity: int
    # Minimum number of idle instances to keep in the instance pool
    min_idle_instances: int
    # This field encodes, through a single value, the resources available to
    # each of the Spark nodes in this cluster. For example, the Spark nodes can
    # be provisioned and optimized for memory or compute intensive workloads. A
    # list of available node types can be retrieved by using the
    # :method:clusters/listNodeTypes API call.
    node_type_id: str
    # Custom Docker Image BYOC
    preloaded_docker_images: "List[DockerImage]"
    # A list of preloaded Spark image versions for the pool. Pool-backed
    # clusters started with the preloaded Spark version will start faster. A
    # list of available Spark versions can be retrieved by using the
    # :method:clusters/sparkVersions API call.
    preloaded_spark_versions: "List[str]"
    # Current state of the instance pool.
    state: "InstancePoolState"
    # Usage statistics about the instance pool.
    stats: "InstancePoolStats"
    # Status of failed pending instances in the pool.
    status: "InstancePoolStatus"

    def as_dict(self) -> dict:
        body = {}
        if self.aws_attributes:
            body["aws_attributes"] = self.aws_attributes.as_dict()
        if self.azure_attributes:
            body["azure_attributes"] = self.azure_attributes.as_dict()
        if self.custom_tags:
            body["custom_tags"] = self.custom_tags
        if self.default_tags:
            body["default_tags"] = self.default_tags
        if self.disk_spec:
            body["disk_spec"] = self.disk_spec.as_dict()
        if self.enable_elastic_disk:
            body["enable_elastic_disk"] = self.enable_elastic_disk
        if self.idle_instance_autotermination_minutes:
            body[
                "idle_instance_autotermination_minutes"
            ] = self.idle_instance_autotermination_minutes
        if self.instance_pool_fleet_attributes:
            body[
                "instance_pool_fleet_attributes"
            ] = self.instance_pool_fleet_attributes.as_dict()
        if self.instance_pool_id:
            body["instance_pool_id"] = self.instance_pool_id
        if self.instance_pool_name:
            body["instance_pool_name"] = self.instance_pool_name
        if self.max_capacity:
            body["max_capacity"] = self.max_capacity
        if self.min_idle_instances:
            body["min_idle_instances"] = self.min_idle_instances
        if self.node_type_id:
            body["node_type_id"] = self.node_type_id
        if self.preloaded_docker_images:
            body["preloaded_docker_images"] = [
                v.as_dict() for v in self.preloaded_docker_images
            ]
        if self.preloaded_spark_versions:
            body["preloaded_spark_versions"] = [
                v for v in self.preloaded_spark_versions
            ]
        if self.state:
            body["state"] = self.state.value
        if self.stats:
            body["stats"] = self.stats.as_dict()
        if self.status:
            body["status"] = self.status.as_dict()

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "InstancePoolAndStats":
        return cls(
            aws_attributes=InstancePoolAwsAttributes.from_dict(d["aws_attributes"])
            if "aws_attributes" in d
            else None,
            azure_attributes=InstancePoolAzureAttributes.from_dict(
                d["azure_attributes"]
            )
            if "azure_attributes" in d
            else None,
            custom_tags=d.get("custom_tags", None),
            default_tags=d.get("default_tags", None),
            disk_spec=DiskSpec.from_dict(d["disk_spec"]) if "disk_spec" in d else None,
            enable_elastic_disk=d.get("enable_elastic_disk", None),
            idle_instance_autotermination_minutes=d.get(
                "idle_instance_autotermination_minutes", None
            ),
            instance_pool_fleet_attributes=InstancePoolFleetAttributes.from_dict(
                d["instance_pool_fleet_attributes"]
            )
            if "instance_pool_fleet_attributes" in d
            else None,
            instance_pool_id=d.get("instance_pool_id", None),
            instance_pool_name=d.get("instance_pool_name", None),
            max_capacity=d.get("max_capacity", None),
            min_idle_instances=d.get("min_idle_instances", None),
            node_type_id=d.get("node_type_id", None),
            preloaded_docker_images=[
                DockerImage.from_dict(v) for v in d["preloaded_docker_images"]
            ]
            if "preloaded_docker_images" in d
            else None,
            preloaded_spark_versions=d.get("preloaded_spark_versions", None),
            state=InstancePoolState(d["state"]) if "state" in d else None,
            stats=InstancePoolStats.from_dict(d["stats"]) if "stats" in d else None,
            status=InstancePoolStatus.from_dict(d["status"]) if "status" in d else None,
        )


@dataclass
class InstancePoolAwsAttributes:

    # Availability type used for the spot nodes.
    #
    # The default value is defined by
    # InstancePoolConf.instancePoolDefaultAwsAvailability
    availability: "InstancePoolAwsAttributesAvailability"
    # Calculates the bid price for AWS spot instances, as a percentage of the
    # corresponding instance type's on-demand price. For example, if this field
    # is set to 50, and the cluster needs a new `r3.xlarge` spot instance, then
    # the bid price is half of the price of on-demand `r3.xlarge` instances.
    # Similarly, if this field is set to 200, the bid price is twice the price
    # of on-demand `r3.xlarge` instances. If not specified, the default value is
    # 100. When spot instances are requested for this cluster, only spot
    # instances whose bid price percentage matches this field will be
    # considered. Note that, for safety, we enforce this field to be no more
    # than 10000.
    #
    # The default value and documentation here should be kept consistent with
    # CommonConf.defaultSpotBidPricePercent and
    # CommonConf.maxSpotBidPricePercent.
    spot_bid_price_percent: int
    # Identifier for the availability zone/datacenter in which the cluster
    # resides. This string will be of a form like "us-west-2a". The provided
    # availability zone must be in the same region as the Databricks deployment.
    # For example, "us-west-2a" is not a valid zone id if the Databricks
    # deployment resides in the "us-east-1" region. This is an optional field at
    # cluster creation, and if not specified, a default zone will be used. The
    # list of available zones as well as the default value can be found by using
    # the `List Zones`_ method.
    zone_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.availability:
            body["availability"] = self.availability.value
        if self.spot_bid_price_percent:
            body["spot_bid_price_percent"] = self.spot_bid_price_percent
        if self.zone_id:
            body["zone_id"] = self.zone_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "InstancePoolAwsAttributes":
        return cls(
            availability=InstancePoolAwsAttributesAvailability(d["availability"])
            if "availability" in d
            else None,
            spot_bid_price_percent=d.get("spot_bid_price_percent", None),
            zone_id=d.get("zone_id", None),
        )


class InstancePoolAwsAttributesAvailability(Enum):
    """Availability type used for the spot nodes.

    The default value is defined by
    InstancePoolConf.instancePoolDefaultAwsAvailability"""

    ON_DEMAND = "ON_DEMAND"
    SPOT = "SPOT"
    SPOT_WITH_FALLBACK = "SPOT_WITH_FALLBACK"


@dataclass
class InstancePoolAzureAttributes:

    # Shows the Availability type used for the spot nodes.
    #
    # The default value is defined by
    # InstancePoolConf.instancePoolDefaultAzureAvailability
    availability: "InstancePoolAzureAttributesAvailability"
    # The default value and documentation here should be kept consistent with
    # CommonConf.defaultSpotBidMaxPrice.
    spot_bid_max_price: float

    def as_dict(self) -> dict:
        body = {}
        if self.availability:
            body["availability"] = self.availability.value
        if self.spot_bid_max_price:
            body["spot_bid_max_price"] = self.spot_bid_max_price

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "InstancePoolAzureAttributes":
        return cls(
            availability=InstancePoolAzureAttributesAvailability(d["availability"])
            if "availability" in d
            else None,
            spot_bid_max_price=d.get("spot_bid_max_price", None),
        )


class InstancePoolAzureAttributesAvailability(Enum):
    """Shows the Availability type used for the spot nodes.

    The default value is defined by
    InstancePoolConf.instancePoolDefaultAzureAvailability"""

    ON_DEMAND_AZURE = "ON_DEMAND_AZURE"
    SPOT_AZURE = "SPOT_AZURE"
    SPOT_WITH_FALLBACK_AZURE = "SPOT_WITH_FALLBACK_AZURE"


@dataclass
class InstancePoolFleetAttributes:

    fleet_on_demand_option: "FleetOnDemandOption"

    fleet_spot_option: "FleetSpotOption"

    launch_template_overrides: "List[FleetLaunchTemplateOverride]"

    def as_dict(self) -> dict:
        body = {}
        if self.fleet_on_demand_option:
            body["fleet_on_demand_option"] = self.fleet_on_demand_option.as_dict()
        if self.fleet_spot_option:
            body["fleet_spot_option"] = self.fleet_spot_option.as_dict()
        if self.launch_template_overrides:
            body["launch_template_overrides"] = [
                v.as_dict() for v in self.launch_template_overrides
            ]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "InstancePoolFleetAttributes":
        return cls(
            fleet_on_demand_option=FleetOnDemandOption.from_dict(
                d["fleet_on_demand_option"]
            )
            if "fleet_on_demand_option" in d
            else None,
            fleet_spot_option=FleetSpotOption.from_dict(d["fleet_spot_option"])
            if "fleet_spot_option" in d
            else None,
            launch_template_overrides=[
                FleetLaunchTemplateOverride.from_dict(v)
                for v in d["launch_template_overrides"]
            ]
            if "launch_template_overrides" in d
            else None,
        )


class InstancePoolState(Enum):
    """Current state of the instance pool."""

    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    STOPPED = "STOPPED"


@dataclass
class InstancePoolStats:

    # Number of active instances in the pool that are NOT part of a cluster.
    idle_count: int
    # Number of pending instances in the pool that are NOT part of a cluster.
    pending_idle_count: int
    # Number of pending instances in the pool that are part of a cluster.
    pending_used_count: int
    # Number of active instances in the pool that are part of a cluster.
    used_count: int

    def as_dict(self) -> dict:
        body = {}
        if self.idle_count:
            body["idle_count"] = self.idle_count
        if self.pending_idle_count:
            body["pending_idle_count"] = self.pending_idle_count
        if self.pending_used_count:
            body["pending_used_count"] = self.pending_used_count
        if self.used_count:
            body["used_count"] = self.used_count

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "InstancePoolStats":
        return cls(
            idle_count=d.get("idle_count", None),
            pending_idle_count=d.get("pending_idle_count", None),
            pending_used_count=d.get("pending_used_count", None),
            used_count=d.get("used_count", None),
        )


@dataclass
class InstancePoolStatus:

    # List of error messages for the failed pending instances. The
    # pending_instance_errors follows FIFO with maximum length of the min_idle
    # of the pool. The pending_instance_errors is emptied once the number of
    # exiting available instances reaches the min_idle of the pool.
    pending_instance_errors: "List[PendingInstanceError]"

    def as_dict(self) -> dict:
        body = {}
        if self.pending_instance_errors:
            body["pending_instance_errors"] = [
                v.as_dict() for v in self.pending_instance_errors
            ]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "InstancePoolStatus":
        return cls(
            pending_instance_errors=[
                PendingInstanceError.from_dict(v) for v in d["pending_instance_errors"]
            ]
            if "pending_instance_errors" in d
            else None,
        )


@dataclass
class ListInstancePools:

    instance_pools: "List[InstancePoolAndStats]"

    def as_dict(self) -> dict:
        body = {}
        if self.instance_pools:
            body["instance_pools"] = [v.as_dict() for v in self.instance_pools]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListInstancePools":
        return cls(
            instance_pools=[
                InstancePoolAndStats.from_dict(v) for v in d["instance_pools"]
            ]
            if "instance_pools" in d
            else None,
        )


@dataclass
class PendingInstanceError:

    instance_id: str

    message: str

    def as_dict(self) -> dict:
        body = {}
        if self.instance_id:
            body["instance_id"] = self.instance_id
        if self.message:
            body["message"] = self.message

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PendingInstanceError":
        return cls(
            instance_id=d.get("instance_id", None),
            message=d.get("message", None),
        )


class InstancePoolsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self,
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
        **kwargs
    ) -> CreateInstancePoolResponse:
        """Create a new instance pool.

        Creates a new instance pool using idle and ready-to-use cloud instances."""

        request = kwargs.get("request", None)
        if not request:
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
                preloaded_spark_versions=preloaded_spark_versions,
            )
        body = request.as_dict()
        query = {}

        json = self._api.do(
            "POST", "/api/2.0/instance-pools/create", query=query, body=body
        )
        return CreateInstancePoolResponse.from_dict(json)

    def delete(self, instance_pool_id: str, **kwargs):
        """Delete an instance pool.

        Deletes the instance pool permanently. The idle instances in the pool
        are terminated asynchronously."""

        request = kwargs.get("request", None)
        if not request:
            request = DeleteInstancePool(instance_pool_id=instance_pool_id)
        body = request.as_dict()
        query = {}

        self._api.do("POST", "/api/2.0/instance-pools/delete", query=query, body=body)

    def edit(
        self,
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
        **kwargs
    ):
        """Edit an existing instance pool.

        Modifies the configuration of an existing instance pool."""

        request = kwargs.get("request", None)
        if not request:
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
                preloaded_spark_versions=preloaded_spark_versions,
            )
        body = request.as_dict()
        query = {}

        self._api.do("POST", "/api/2.0/instance-pools/edit", query=query, body=body)

    def get(self, instance_pool_id: str, **kwargs) -> GetInstancePool:
        """Get instance pool information.

        Retrieve the information for an instance pool based on its identifier."""

        request = kwargs.get("request", None)
        if not request:
            request = Get(instance_pool_id=instance_pool_id)
        body = request.as_dict()
        query = {}
        if instance_pool_id:
            query["instance_pool_id"] = instance_pool_id

        json = self._api.do(
            "GET", "/api/2.0/instance-pools/get", query=query, body=body
        )
        return GetInstancePool.from_dict(json)

    def list(self) -> ListInstancePools:
        """List instance pool info.

        Gets a list of instance pools with their statistics."""

        json = self._api.do("GET", "/api/2.0/instance-pools/list")
        return ListInstancePools.from_dict(json)

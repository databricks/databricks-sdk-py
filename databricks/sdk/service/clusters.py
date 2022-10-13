# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'AutoScale',
    'AwsAttributes',
    'AwsAttributesAvailability',
    'AwsAttributesEbsVolumeType',
    'AzureAttributes',
    'AzureAttributesAvailability',
    'ChangeClusterOwner',
    'ClientsTypes',
    'CloudProviderNodeInfo',
    'CloudProviderNodeStatus',
    'ClusterAttributes',
    'ClusterAttributesClusterSource',
    'ClusterAttributesRuntimeEngine',
    'ClusterEvent',
    'ClusterEventType',
    'ClusterInfo',
    'ClusterInfoClusterSource',
    'ClusterInfoRuntimeEngine',
    'ClusterInfoState',
    'ClusterLogConf',
    'ClusterSize',
    'CreateCluster',
    'CreateClusterClusterSource',
    'CreateClusterResponse',
    'CreateClusterRuntimeEngine',
    'DataPlaneEventDetails',
    'DataPlaneEventDetailsEventType',
    'DbfsStorageInfo',
    'DeleteCluster',
    'EditCluster',
    'EditClusterClusterSource',
    'EditClusterRuntimeEngine',
    'EventDetails',
    'EventDetailsCause',
    'GcpAttributes',
    'GcpAttributesAvailability',
    'GetEvents',
    'GetEventsEventTypesItem',
    'GetEventsOrder',
    'GetEventsResponse',
    'GetSparkVersionsResponse',
    'ListAvailableZonesResponse',
    'ListClustersResponse',
    'ListNodeTypesResponse',
    'LogAnalyticsInfo',
    'LogSyncStatus',
    'NodeInstanceType',
    'NodeType',
    'PermanentDeleteCluster',
    'PinCluster',
    'ResizeCluster',
    'RestartCluster',
    'S3StorageInfo',
    'SparkNode',
    'SparkNodeAwsAttributes',
    'SparkVersion',
    'StartCluster',
    'TerminationReason',
    'TerminationReasonCode',
    'TerminationReasonType',
    'UnpinCluster',
    'WorkloadType',
    'GetRequest',
    'ListRequest',
    
    'Clusters',
]

# all definitions in this file are in alphabetical order

@dataclass
class AutoScale:
    
    # The maximum number of workers to which the cluster can scale up when
    # overloaded. Note that ``max_workers`` must be strictly greater than
    # ``min_workers``.
    max_workers: int = None
    # The minimum number of workers to which the cluster can scale down when
    # underutilized. It is also the initial number of workers the cluster will
    # have after creation.
    min_workers: int = None

    def as_request(self) -> (dict, dict):
        autoScale_query, autoScale_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.max_workers:
            autoScale_body['max_workers'] = self.max_workers
        if self.min_workers:
            autoScale_body['min_workers'] = self.min_workers
        
        return autoScale_query, autoScale_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AutoScale':
        return cls(
            max_workers=d.get('max_workers', None),
            min_workers=d.get('min_workers', None),
        )



@dataclass
class AwsAttributes:
    
    # Availability type used for all subsequent nodes past the
    # ``first_on_demand`` ones. Note: If ``first_on_demand`` is zero, this
    # availability type will be used for the entire cluster.
    availability: 'AwsAttributesAvailability' = None
    # The number of volumes launched for each instance. Users can choose up to
    # 10 volumes. This feature is only enabled for supported node types. Legacy
    # node types cannot specify custom EBS volumes. For node types with no
    # instance store, at least one EBS volume needs to be specified; otherwise,
    # cluster creation will fail.
    # 
    # These EBS volumes will be mounted at ``/ebs0``, ``/ebs1``, and etc.
    # Instance store volumes will be mounted at ``/local_disk0``,
    # ``/local_disk1``, and etc.
    # 
    # If EBS volumes are attached, Databricks will configure Spark to use only
    # the EBS volumes for scratch storage because heterogenously sized scratch
    # devices can lead to inefficient disk utilization. If no EBS volumes are
    # attached, Databricks will configure Spark to use instance store volumes.
    # 
    # Please note that if EBS volumes are specified, then the Spark
    # configuration ``spark.local.dir`` will be overridden.
    ebs_volume_count: int = None
    # <needs content added>
    ebs_volume_iops: int = None
    # The size of each EBS volume (in GiB) launched for each instance. For
    # general purpose SSD, this value must be within the range 100 - 4096. For
    # throughput optimized HDD, this value must be within the range 500 - 4096.
    ebs_volume_size: int = None
    # <needs content added>
    ebs_volume_throughput: int = None
    # The type of EBS volumes that will be launched with this cluster.
    ebs_volume_type: 'AwsAttributesEbsVolumeType' = None
    # The first ``first_on_demand`` nodes of the cluster will be placed on
    # on-demand instances. If this value is greater than 0, the cluster driver
    # node in particular will be placed on an on-demand instance. If this value
    # is greater than or equal to the current cluster size, all nodes will be
    # placed on on-demand instances. If this value is less than the current
    # cluster size, ``first_on_demand`` nodes will be placed on on-demand
    # instances and the remainder will be placed on ``availability`` instances.
    # Note that this value does not affect cluster size and cannot currently be
    # mutated over the lifetime of a cluster.
    first_on_demand: int = None
    # Nodes for this cluster will only be placed on AWS instances with this
    # instance profile. If ommitted, nodes will be placed on instances without
    # an IAM instance profile. The instance profile must have previously been
    # added to the Databricks environment by an account administrator.
    # 
    # This feature may only be available to certain customer plans.
    # 
    # If this field is ommitted, we will pull in the default from the conf if it
    # exists.
    instance_profile_arn: str = None
    # The bid price for AWS spot instances, as a percentage of the corresponding
    # instance type's on-demand price. For example, if this field is set to 50,
    # and the cluster needs a new ``r3.xlarge`` spot instance, then the bid
    # price is half of the price of on-demand ``r3.xlarge`` instances.
    # Similarly, if this field is set to 200, the bid price is twice the price
    # of on-demand ``r3.xlarge`` instances. If not specified, the default value
    # is 100. When spot instances are requested for this cluster, only spot
    # instances whose bid price percentage matches this field will be
    # considered. Note that, for safety, we enforce this field to be no more
    # than 10000.
    # 
    # The default value and documentation here should be kept consistent with
    # CommonConf.defaultSpotBidPricePercent and
    # CommonConf.maxSpotBidPricePercent.
    spot_bid_price_percent: int = None
    # Identifier for the availability zone/datacenter in which the cluster
    # resides. This string will be of a form like "us-west-2a". The provided
    # availability zone must be in the same region as the Databricks deployment.
    # For example, "us-west-2a" is not a valid zone id if the Databricks
    # deployment resides in the "us-east-1" region. This is an optional field at
    # cluster creation, and if not specified, a default zone will be used. If
    # the zone specified is "auto", will try to place cluster in a zone with
    # high availability, and will retry placement in a different AZ if there is
    # not enough capacity. See [[AutoAZHelper.scala]] for more details. The list
    # of available zones as well as the default value can be found by using the
    # `List Zones`_ method.
    zone_id: str = None

    def as_request(self) -> (dict, dict):
        awsAttributes_query, awsAttributes_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.availability:
            awsAttributes_body['availability'] = self.availability.value
        if self.ebs_volume_count:
            awsAttributes_body['ebs_volume_count'] = self.ebs_volume_count
        if self.ebs_volume_iops:
            awsAttributes_body['ebs_volume_iops'] = self.ebs_volume_iops
        if self.ebs_volume_size:
            awsAttributes_body['ebs_volume_size'] = self.ebs_volume_size
        if self.ebs_volume_throughput:
            awsAttributes_body['ebs_volume_throughput'] = self.ebs_volume_throughput
        if self.ebs_volume_type:
            awsAttributes_body['ebs_volume_type'] = self.ebs_volume_type.value
        if self.first_on_demand:
            awsAttributes_body['first_on_demand'] = self.first_on_demand
        if self.instance_profile_arn:
            awsAttributes_body['instance_profile_arn'] = self.instance_profile_arn
        if self.spot_bid_price_percent:
            awsAttributes_body['spot_bid_price_percent'] = self.spot_bid_price_percent
        if self.zone_id:
            awsAttributes_body['zone_id'] = self.zone_id
        
        return awsAttributes_query, awsAttributes_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AwsAttributes':
        return cls(
            availability=AwsAttributesAvailability(d['availability']) if 'availability' in d else None,
            ebs_volume_count=d.get('ebs_volume_count', None),
            ebs_volume_iops=d.get('ebs_volume_iops', None),
            ebs_volume_size=d.get('ebs_volume_size', None),
            ebs_volume_throughput=d.get('ebs_volume_throughput', None),
            ebs_volume_type=AwsAttributesEbsVolumeType(d['ebs_volume_type']) if 'ebs_volume_type' in d else None,
            first_on_demand=d.get('first_on_demand', None),
            instance_profile_arn=d.get('instance_profile_arn', None),
            spot_bid_price_percent=d.get('spot_bid_price_percent', None),
            zone_id=d.get('zone_id', None),
        )



class AwsAttributesAvailability(Enum):
    """Availability type used for all subsequent nodes past the ``first_on_demand``
    ones. Note: If ``first_on_demand`` is zero, this availability type will be
    used for the entire cluster."""
    
    ON_DEMAND = 'ON_DEMAND'
    SPOT = 'SPOT'
    SPOT_WITH_FALLBACK = 'SPOT_WITH_FALLBACK'

class AwsAttributesEbsVolumeType(Enum):
    """The type of EBS volumes that will be launched with this cluster."""
    
    GENERAL_PURPOSE_SSD = 'GENERAL_PURPOSE_SSD'
    THROUGHPUT_OPTIMIZED_HDD = 'THROUGHPUT_OPTIMIZED_HDD'

@dataclass
class AzureAttributes:
    
    # Availability type used for all subsequent nodes past the
    # ``first_on_demand`` ones. Note: If ``first_on_demand`` is zero (which only
    # happens on pool clusters), this availability type will be used for the
    # entire cluster.
    availability: 'AzureAttributesAvailability' = None
    # The first ``first_on_demand`` nodes of the cluster will be placed on
    # on-demand instances. This value should be greater than 0, to make sure the
    # cluster driver node is placed on an on-demand instance. If this value is
    # greater than or equal to the current cluster size, all nodes will be
    # placed on on-demand instances. If this value is less than the current
    # cluster size, ``first_on_demand`` nodes will be placed on on-demand
    # instances and the remainder will be placed on ``availability`` instances.
    # Note that this value does not affect cluster size and cannot currently be
    # mutated over the lifetime of a cluster.
    first_on_demand: int = None
    # Defines values necessary to configure and run Azure Log Analytics agent
    log_analytics_info: 'LogAnalyticsInfo' = None
    # The max bid price to be used for Azure spot instances. The Max price for
    # the bid cannot be higher than the on-demand price of the instance. If not
    # specified, the default value is -1, which specifies that the instance
    # cannot be evicted on the basis of price, and only on the basis of
    # availability. Further, the value should > 0 or -1.
    spot_bid_max_price: float = None

    def as_request(self) -> (dict, dict):
        azureAttributes_query, azureAttributes_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.availability:
            azureAttributes_body['availability'] = self.availability.value
        if self.first_on_demand:
            azureAttributes_body['first_on_demand'] = self.first_on_demand
        if self.log_analytics_info:
            azureAttributes_body['log_analytics_info'] = self.log_analytics_info.as_request()[1]
        if self.spot_bid_max_price:
            azureAttributes_body['spot_bid_max_price'] = self.spot_bid_max_price
        
        return azureAttributes_query, azureAttributes_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AzureAttributes':
        return cls(
            availability=AzureAttributesAvailability(d['availability']) if 'availability' in d else None,
            first_on_demand=d.get('first_on_demand', None),
            log_analytics_info=LogAnalyticsInfo.from_dict(d['log_analytics_info']) if 'log_analytics_info' in d else None,
            spot_bid_max_price=d.get('spot_bid_max_price', None),
        )



class AzureAttributesAvailability(Enum):
    """Availability type used for all subsequent nodes past the ``first_on_demand``
    ones. Note: If ``first_on_demand`` is zero (which only happens on pool
    clusters), this availability type will be used for the entire cluster."""
    
    ON_DEMAND_AZURE = 'ON_DEMAND_AZURE'
    SPOT_AZURE = 'SPOT_AZURE'
    SPOT_WITH_FALLBACK_AZURE = 'SPOT_WITH_FALLBACK_AZURE'

@dataclass
class ChangeClusterOwner:
    
    # <needs content added>
    cluster_id: str
    # New owner of the cluster_id after this RPC.
    owner_username: str = None

    def as_request(self) -> (dict, dict):
        changeClusterOwner_query, changeClusterOwner_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cluster_id:
            changeClusterOwner_body['cluster_id'] = self.cluster_id
        if self.owner_username:
            changeClusterOwner_body['owner_username'] = self.owner_username
        
        return changeClusterOwner_query, changeClusterOwner_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ChangeClusterOwner':
        return cls(
            cluster_id=d.get('cluster_id', None),
            owner_username=d.get('owner_username', None),
        )



@dataclass
class ClientsTypes:
    
    # With jobs set, the cluster can be used for jobs
    jobs: bool = None
    # With notebooks set, this cluster can be used for notebooks
    notebooks: bool = None

    def as_request(self) -> (dict, dict):
        clientsTypes_query, clientsTypes_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.jobs:
            clientsTypes_body['jobs'] = self.jobs
        if self.notebooks:
            clientsTypes_body['notebooks'] = self.notebooks
        
        return clientsTypes_query, clientsTypes_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClientsTypes':
        return cls(
            jobs=d.get('jobs', None),
            notebooks=d.get('notebooks', None),
        )



@dataclass
class CloudProviderNodeInfo:
    
    
    status: 'List[CloudProviderNodeStatus]' = None

    def as_request(self) -> (dict, dict):
        cloudProviderNodeInfo_query, cloudProviderNodeInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.status:
            cloudProviderNodeInfo_body['status'] = [v for v in self.status]
        
        return cloudProviderNodeInfo_query, cloudProviderNodeInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CloudProviderNodeInfo':
        return cls(
            status=d.get('status', None),
        )



class CloudProviderNodeStatus(Enum):
    
    
    NotAvailableInRegion = 'NotAvailableInRegion'
    NotEnabledOnSubscription = 'NotEnabledOnSubscription'

@dataclass
class ClusterAttributes:
    
    # Automatically terminates the cluster after it is inactive for this time in
    # minutes. If not set, this cluster will not be automatically terminated. If
    # specified, the threshold must be between 10 and 10000 minutes. Users can
    # also set this value to 0 to explicitly disable automatic termination.
    autotermination_minutes: int = None
    # Attributes related to clusters running on Amazon Web Services. If not
    # specified at cluster creation, a set of default values will be used.
    aws_attributes: 'AwsAttributes' = None
    # Attributes related to clusters running on Microsoft Azure. If not
    # specified at cluster creation, a set of default values will be used.
    azure_attributes: 'AzureAttributes' = None
    # The configuration for delivering spark logs to a long-term storage
    # destination. Two kinds of destinations (dbfs and s3) are supported. Only
    # one destination can be specified for one cluster. If the conf is given,
    # the logs will be delivered to the destination every ``5 mins``. The
    # destination of driver logs is ``$destination/$clusterId/driver``, while
    # the destination of executor logs is ``$destination/$clusterId/executor``.
    cluster_log_conf: 'ClusterLogConf' = None
    # Cluster name requested by the user. This doesn't have to be unique. If not
    # specified at creation, the cluster name will be an empty string.
    cluster_name: str = None
    # Determines whether the cluster was created by a user through the UI,
    # created by the Databricks Jobs Scheduler, or through an API request. This
    # is the same as cluster_creator, but read only.
    cluster_source: 'ClusterAttributesClusterSource' = None
    # Additional tags for cluster resources. Databricks will tag all cluster
    # resources (e.g., AWS instances and EBS volumes) with these tags in
    # addition to ``default_tags``. Notes:
    # 
    # - Currently, Databricks allows at most 45 custom tags
    # 
    # - Clusters can only reuse cloud resources if the resources' tags are a
    # subset of the cluster tags
    custom_tags: 'Dict[str,str]' = None
    # The optional ID of the instance pool for the driver of the cluster
    # belongs. The pool cluster uses the instance pool with id
    # (instance_pool_id) if the driver pool is not assigned.
    driver_instance_pool_id: str = None
    # The node type of the Spark driver. Note that this field is optional; if
    # unset, the driver node type will be set as the same value as
    # `node_type_id` defined above.
    # 
    # This field, along with node_type_id, should not be set if
    # virtual_cluster_size is set. If both driver_node_type_id, node_type_id,
    # and virtual_cluster_size are specified, driver_node_type_id and
    # node_type_id take precedence.
    driver_node_type_id: str = None
    # The key of the spark version running in the dataplane. This is possibly
    # different from the spark_version (index 2). The spark_version is the raw
    # string provided by the user through API or UI, which could map to a
    # different effective_spark_version running in the dataplane, depending on
    # the cluster's instance type or the runtimeEngine parameter.
    effective_spark_version: str = None
    # Autoscaling Local Storage: when enabled, this cluster will dynamically
    # acquire additional disk space when its Spark workers are running low on
    # disk space. This feature requires specific AWS permissions to function
    # correctly - refer to the User Guide for more details.
    enable_elastic_disk: bool = None
    # Whether to enable LUKS on cluster VMs' local disks
    enable_local_disk_encryption: bool = None
    # Attributes related to clusters running on Google Cloud Platform. If not
    # specified at cluster creation, a set of default values will be used.
    gcp_attributes: 'GcpAttributes' = None
    # The optional ID of the instance pool to which the cluster belongs.
    instance_pool_id: str = None
    # This field encodes, through a single value, the resources available to
    # each of the Spark nodes in this cluster. For example, the Spark nodes can
    # be provisioned and optimized for memory or compute intensive workloads A
    # list of available node types can be retrieved by using the
    # :ref:`clusterClusterServicelistNodeTypes` API call.
    # 
    # This field, along with driver_node_type_id, should not be set if
    # virtual_cluster_size is set. If both driver_node_type_id, node_type_id,
    # and virtual_cluster_size are specified, driver_node_type_id and
    # node_type_id take precedence.
    node_type_id: str = None
    # The ID of the cluster policy used to create the cluster if applicable.
    policy_id: str = None
    # Decides which runtime engine to be use, e.g. Standard vs. Photon. If
    # unspecified, the runtime engine is inferred from spark_version.
    runtime_engine: 'ClusterAttributesRuntimeEngine' = None
    # An object containing a set of optional, user-specified Spark configuration
    # key-value pairs. Users can also pass in a string of extra JVM options to
    # the driver and the executors via ``spark.driver.extraJavaOptions`` and
    # ``spark.executor.extraJavaOptions`` respectively.
    # 
    # Example Spark confs: ``{"spark.speculation": true,
    # "spark.streaming.ui.retainedBatches": 5}`` or
    # ``{"spark.driver.extraJavaOptions": "-verbose:gc -XX:+PrintGCDetails"}``
    spark_conf: 'Dict[str,str]' = None
    # An object containing a set of optional, user-specified environment
    # variable key-value pairs. Please note that key-value pair of the form
    # (X,Y) will be exported as is (i.e., ``export X='Y'``) while launching the
    # driver and workers.
    # 
    # In order to specify an additional set of ``SPARK_DAEMON_JAVA_OPTS``, we
    # recommend appending them to ``$SPARK_DAEMON_JAVA_OPTS`` as shown in the
    # example below. This ensures that all default databricks managed
    # environmental variables are included as well.
    # 
    # Example Spark environment variables: ``{"SPARK_WORKER_MEMORY": "28000m",
    # "SPARK_LOCAL_DIRS": "/local_disk0"}`` or ``{"SPARK_DAEMON_JAVA_OPTS":
    # "$SPARK_DAEMON_JAVA_OPTS -Dspark.shuffle.service.enabled=true"}``
    spark_env_vars: 'Dict[str,str]' = None
    # The Spark version of the cluster, e.g. "3.3.x-scala2.11". A list of
    # available Spark versions can be retrieved by using the
    # :ref:`clusterClusterServicelistSparkVersions` API call. This is the Spark
    # version provided from the user input (API/UI) and may be different from
    # the effective_spark_version, which is the spark version that is actually
    # run in the dataplane. See index 45 for more context.
    spark_version: str = None
    # SSH public key contents that will be added to each Spark node in this
    # cluster. The corresponding private keys can be used to login with the user
    # name ``ubuntu`` on port ``2200``. Up to 10 keys can be specified.
    ssh_public_keys: 'List[str]' = None
    
    workload_type: 'WorkloadType' = None

    def as_request(self) -> (dict, dict):
        clusterAttributes_query, clusterAttributes_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.autotermination_minutes:
            clusterAttributes_body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes:
            clusterAttributes_body['aws_attributes'] = self.aws_attributes.as_request()[1]
        if self.azure_attributes:
            clusterAttributes_body['azure_attributes'] = self.azure_attributes.as_request()[1]
        if self.cluster_log_conf:
            clusterAttributes_body['cluster_log_conf'] = self.cluster_log_conf.as_request()[1]
        if self.cluster_name:
            clusterAttributes_body['cluster_name'] = self.cluster_name
        if self.cluster_source:
            clusterAttributes_body['cluster_source'] = self.cluster_source.value
        if self.custom_tags:
            clusterAttributes_body['custom_tags'] = self.custom_tags
        if self.driver_instance_pool_id:
            clusterAttributes_body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id:
            clusterAttributes_body['driver_node_type_id'] = self.driver_node_type_id
        if self.effective_spark_version:
            clusterAttributes_body['effective_spark_version'] = self.effective_spark_version
        if self.enable_elastic_disk:
            clusterAttributes_body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption:
            clusterAttributes_body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.gcp_attributes:
            clusterAttributes_body['gcp_attributes'] = self.gcp_attributes.as_request()[1]
        if self.instance_pool_id:
            clusterAttributes_body['instance_pool_id'] = self.instance_pool_id
        if self.node_type_id:
            clusterAttributes_body['node_type_id'] = self.node_type_id
        if self.policy_id:
            clusterAttributes_body['policy_id'] = self.policy_id
        if self.runtime_engine:
            clusterAttributes_body['runtime_engine'] = self.runtime_engine.value
        if self.spark_conf:
            clusterAttributes_body['spark_conf'] = self.spark_conf
        if self.spark_env_vars:
            clusterAttributes_body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version:
            clusterAttributes_body['spark_version'] = self.spark_version
        if self.ssh_public_keys:
            clusterAttributes_body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        if self.workload_type:
            clusterAttributes_body['workload_type'] = self.workload_type.as_request()[1]
        
        return clusterAttributes_query, clusterAttributes_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterAttributes':
        return cls(
            autotermination_minutes=d.get('autotermination_minutes', None),
            aws_attributes=AwsAttributes.from_dict(d['aws_attributes']) if 'aws_attributes' in d else None,
            azure_attributes=AzureAttributes.from_dict(d['azure_attributes']) if 'azure_attributes' in d else None,
            cluster_log_conf=ClusterLogConf.from_dict(d['cluster_log_conf']) if 'cluster_log_conf' in d else None,
            cluster_name=d.get('cluster_name', None),
            cluster_source=ClusterAttributesClusterSource(d['cluster_source']) if 'cluster_source' in d else None,
            custom_tags=d.get('custom_tags', None),
            driver_instance_pool_id=d.get('driver_instance_pool_id', None),
            driver_node_type_id=d.get('driver_node_type_id', None),
            effective_spark_version=d.get('effective_spark_version', None),
            enable_elastic_disk=d.get('enable_elastic_disk', None),
            enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
            gcp_attributes=GcpAttributes.from_dict(d['gcp_attributes']) if 'gcp_attributes' in d else None,
            instance_pool_id=d.get('instance_pool_id', None),
            node_type_id=d.get('node_type_id', None),
            policy_id=d.get('policy_id', None),
            runtime_engine=ClusterAttributesRuntimeEngine(d['runtime_engine']) if 'runtime_engine' in d else None,
            spark_conf=d.get('spark_conf', None),
            spark_env_vars=d.get('spark_env_vars', None),
            spark_version=d.get('spark_version', None),
            ssh_public_keys=d.get('ssh_public_keys', None),
            workload_type=WorkloadType.from_dict(d['workload_type']) if 'workload_type' in d else None,
        )



class ClusterAttributesClusterSource(Enum):
    """Determines whether the cluster was created by a user through the UI, created
    by the Databricks Jobs Scheduler, or through an API request. This is the
    same as cluster_creator, but read only."""
    
    API = 'API'
    JOB = 'JOB'
    MODELS = 'MODELS'
    PIPELINE = 'PIPELINE'
    PIPELINE_MAINTENANCE = 'PIPELINE_MAINTENANCE'
    SQL = 'SQL'
    UI = 'UI'

class ClusterAttributesRuntimeEngine(Enum):
    """Decides which runtime engine to be use, e.g. Standard vs. Photon. If
    unspecified, the runtime engine is inferred from spark_version."""
    
    NULL = 'NULL'
    PHOTON = 'PHOTON'
    STANDARD = 'STANDARD'

@dataclass
class ClusterEvent:
    
    # <needs content added>
    cluster_id: str
    # <needs content added>
    data_plane_event_details: 'DataPlaneEventDetails' = None
    # <needs content added>
    details: 'EventDetails' = None
    # The timestamp when the event occurred, stored as the number of
    # milliseconds since the Unix epoch. If not provided, this will be assigned
    # by the Timeline service.
    timestamp: int = None
    # <needs content added>
    type: 'ClusterEventType' = None

    def as_request(self) -> (dict, dict):
        clusterEvent_query, clusterEvent_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cluster_id:
            clusterEvent_body['cluster_id'] = self.cluster_id
        if self.data_plane_event_details:
            clusterEvent_body['data_plane_event_details'] = self.data_plane_event_details.as_request()[1]
        if self.details:
            clusterEvent_body['details'] = self.details.as_request()[1]
        if self.timestamp:
            clusterEvent_body['timestamp'] = self.timestamp
        if self.type:
            clusterEvent_body['type'] = self.type.value
        
        return clusterEvent_query, clusterEvent_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterEvent':
        return cls(
            cluster_id=d.get('cluster_id', None),
            data_plane_event_details=DataPlaneEventDetails.from_dict(d['data_plane_event_details']) if 'data_plane_event_details' in d else None,
            details=EventDetails.from_dict(d['details']) if 'details' in d else None,
            timestamp=d.get('timestamp', None),
            type=ClusterEventType(d['type']) if 'type' in d else None,
        )



class ClusterEventType(Enum):
    """<needs content added>"""
    
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
class ClusterInfo:
    
    # Parameters needed in order to automatically scale clusters up and down
    # based on load. Note: autoscaling works best with DB runtime versions 3.0
    # or later.
    autoscale: 'AutoScale' = None
    # Automatically terminates the cluster after it is inactive for this time in
    # minutes. If not set, this cluster will not be automatically terminated. If
    # specified, the threshold must be between 10 and 10000 minutes. Users can
    # also set this value to 0 to explicitly disable automatic termination.
    autotermination_minutes: int = None
    # Attributes related to clusters running on Amazon Web Services. If not
    # specified at cluster creation, a set of default values will be used.
    aws_attributes: 'AwsAttributes' = None
    # Attributes related to clusters running on Microsoft Azure. If not
    # specified at cluster creation, a set of default values will be used.
    azure_attributes: 'AzureAttributes' = None
    # Number of CPU cores available for this cluster. Note that this can be
    # fractional, e.g. 7.5 cores, since certain node types are configured to
    # share cores between Spark nodes on the same instance.
    cluster_cores: float = None
    # Canonical identifier for the cluster. This id is retained during cluster
    # restarts and resizes, while each new cluster has a globally unique id.
    cluster_id: str = None
    # The configuration for delivering spark logs to a long-term storage
    # destination. Two kinds of destinations (dbfs and s3) are supported. Only
    # one destination can be specified for one cluster. If the conf is given,
    # the logs will be delivered to the destination every ``5 mins``. The
    # destination of driver logs is ``$destination/$clusterId/driver``, while
    # the destination of executor logs is ``$destination/$clusterId/executor``.
    cluster_log_conf: 'ClusterLogConf' = None
    # Cluster log delivery status.
    cluster_log_status: 'LogSyncStatus' = None
    # Total amount of cluster memory, in megabytes
    cluster_memory_mb: int = None
    # Cluster name requested by the user. This doesn't have to be unique. If not
    # specified at creation, the cluster name will be an empty string.
    cluster_name: str = None
    # Determines whether the cluster was created by a user through the UI,
    # created by the Databricks Jobs Scheduler, or through an API request. This
    # is the same as cluster_creator, but read only.
    cluster_source: 'ClusterInfoClusterSource' = None
    # Creator user name. The field won't be included in the response if the user
    # has already been deleted.
    creator_user_name: str = None
    # Additional tags for cluster resources. Databricks will tag all cluster
    # resources (e.g., AWS instances and EBS volumes) with these tags in
    # addition to ``default_tags``. Notes:
    # 
    # - Currently, Databricks allows at most 45 custom tags
    # 
    # - Clusters can only reuse cloud resources if the resources' tags are a
    # subset of the cluster tags
    custom_tags: 'Dict[str,str]' = None
    # Tags that are added by Databricks regardless of any ``custom_tags``,
    # including:
    # 
    # - Vendor: Databricks
    # 
    # - Creator: <username_of_creator>
    # 
    # - ClusterName: <name_of_cluster>
    # 
    # - ClusterId: <id_of_cluster>
    # 
    # - Name: <Databricks internal use>
    default_tags: 'Dict[str,str]' = None
    # Node on which the Spark driver resides. The driver node contains the Spark
    # master and the Databricks application that manages the per-notebook Spark
    # REPLs.
    driver: 'SparkNode' = None
    # The optional ID of the instance pool for the driver of the cluster
    # belongs. The pool cluster uses the instance pool with id
    # (instance_pool_id) if the driver pool is not assigned.
    driver_instance_pool_id: str = None
    # The node type of the Spark driver. Note that this field is optional; if
    # unset, the driver node type will be set as the same value as
    # `node_type_id` defined above.
    # 
    # This field, along with node_type_id, should not be set if
    # virtual_cluster_size is set. If both driver_node_type_id, node_type_id,
    # and virtual_cluster_size are specified, driver_node_type_id and
    # node_type_id take precedence.
    driver_node_type_id: str = None
    # The key of the spark version running in the dataplane. This is possibly
    # different from the spark_version (index 2). The spark_version is the raw
    # string provided by the user through API or UI, which could map to a
    # different effective_spark_version running in the dataplane, depending on
    # the cluster's instance type or the runtimeEngine parameter.
    effective_spark_version: str = None
    # Autoscaling Local Storage: when enabled, this cluster will dynamically
    # acquire additional disk space when its Spark workers are running low on
    # disk space. This feature requires specific AWS permissions to function
    # correctly - refer to the User Guide for more details.
    enable_elastic_disk: bool = None
    # Whether to enable LUKS on cluster VMs' local disks
    enable_local_disk_encryption: bool = None
    # Nodes on which the Spark executors reside.
    executors: 'List[SparkNode]' = None
    # Attributes related to clusters running on Google Cloud Platform. If not
    # specified at cluster creation, a set of default values will be used.
    gcp_attributes: 'GcpAttributes' = None
    # The optional ID of the instance pool to which the cluster belongs.
    instance_pool_id: str = None
    # Port on which Spark JDBC server is listening, in the driver nod. No
    # service will be listeningon on this port in executor nodes.
    jdbc_port: int = None
    # the timestamp that the cluster was started/restarted
    last_restarted_time: int = None
    # Time when the cluster driver last lost its state (due to a restart or
    # driver failure).
    last_state_loss_time: int = None
    # This field encodes, through a single value, the resources available to
    # each of the Spark nodes in this cluster. For example, the Spark nodes can
    # be provisioned and optimized for memory or compute intensive workloads. A
    # list of available node types can be retrieved by using the
    # :ref:`clusterClusterServicelistNodeTypes` API call.
    # 
    # This field, along with driver_node_type_id, should not be set if
    # virtual_cluster_size is set. If both driver_node_type_id, node_type_id,
    # and virtual_cluster_size are specified, driver_node_type_id and
    # node_type_id take precedence.
    node_type_id: str = None
    # Number of worker nodes that this cluster should have. A cluster has one
    # Spark Driver and ``num_workers`` Executors for a total of ``num_workers``
    # + 1 Spark nodes.
    # 
    # Note: When reading the properties of a cluster, this field reflects the
    # desired number of workers rather than the actual current number of
    # workers. For instance, if a cluster is resized from 5 to 10 workers, this
    # field will immediately be updated to reflect the target size of 10
    # workers, whereas the workers listed in ``spark_info`` will gradually
    # increase from 5 to 10 as the new nodes are provisioned.
    num_workers: int = None
    # The ID of the cluster policy used to create the cluster if applicable.
    policy_id: str = None
    # Decides which runtime engine to be use, e.g. Standard vs. Photon. If
    # unspecified, the runtime engine is inferred from spark_version.
    runtime_engine: 'ClusterInfoRuntimeEngine' = None
    # An object containing a set of optional, user-specified Spark configuration
    # key-value pairs. Users can also pass in a string of extra JVM options to
    # the driver and the executors via ``spark.driver.extraJavaOptions`` and
    # ``spark.executor.extraJavaOptions`` respectively.
    # 
    # Example Spark confs: ``{"spark.speculation": true,
    # "spark.streaming.ui.retainedBatches": 5}`` or
    # ``{"spark.driver.extraJavaOptions": "-verbose:gc -XX:+PrintGCDetails"}``
    spark_conf: 'Dict[str,str]' = None
    # A canonical SparkContext identifier. This value *does* change when the
    # Spark driver restarts. The pair `(cluster_id, spark_context_id)` is a
    # globally unique identifier over all Spark contexts.
    spark_context_id: int = None
    # An object containing a set of optional, user-specified environment
    # variable key-value pairs. Please note that key-value pair of the form
    # (X,Y) will be exported as is (i.e., `export X='Y'`) while launching the
    # driver and workers. In order to specify an additional set of
    # ``SPARK_DAEMON_JAVA_OPTS``, we recommend appending them to
    # ``$SPARK_DAEMON_JAVA_OPTS`` as shown in the example. This ensures that all
    # default databricks managed environmental variables are included as well.
    spark_env_vars: 'Dict[str,str]' = None
    # The Spark version of the cluster, e.g. "3.3.x-scala2.11". A list of
    # available Spark versions can be retrieved by using the
    # :ref:`clusterClusterServicelistSparkVersions` API call. This is the Spark
    # version provided from the user input (API/UI) and may be different from
    # the effective_spark_version, which is the spark version that is actually
    # run in the dataplane. See index 45 for more context.
    spark_version: str = None
    # SSH public key contents that will be added to each Spark node in this
    # cluster. The corresponding private keys can be used to login with the user
    # name ``ubuntu`` on port ``2200``. Up to 10 keys can be specified.
    ssh_public_keys: 'List[str]' = None
    # Time (in epoch milliseconds) when the cluster creation request was
    # received (when the cluster entered a ``PENDING`` state).
    start_time: int = None
    # Current state of the cluster.
    state: 'ClusterInfoState' = None
    # A message associated with the most recent state transition (e.g., the
    # reason why the cluster entered a ``TERMINATED`` state).
    state_message: str = None
    # Time (in epoch milliseconds) when the cluster was terminated, if
    # applicable.
    terminated_time: int = None
    # Information about why the cluster was terminated. This field only appears
    # when the cluster is in a ``TERMINATING`` or ``TERMINATED`` state.
    termination_reason: 'TerminationReason' = None
    
    workload_type: 'WorkloadType' = None

    def as_request(self) -> (dict, dict):
        clusterInfo_query, clusterInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.autoscale:
            clusterInfo_body['autoscale'] = self.autoscale.as_request()[1]
        if self.autotermination_minutes:
            clusterInfo_body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes:
            clusterInfo_body['aws_attributes'] = self.aws_attributes.as_request()[1]
        if self.azure_attributes:
            clusterInfo_body['azure_attributes'] = self.azure_attributes.as_request()[1]
        if self.cluster_cores:
            clusterInfo_body['cluster_cores'] = self.cluster_cores
        if self.cluster_id:
            clusterInfo_body['cluster_id'] = self.cluster_id
        if self.cluster_log_conf:
            clusterInfo_body['cluster_log_conf'] = self.cluster_log_conf.as_request()[1]
        if self.cluster_log_status:
            clusterInfo_body['cluster_log_status'] = self.cluster_log_status.as_request()[1]
        if self.cluster_memory_mb:
            clusterInfo_body['cluster_memory_mb'] = self.cluster_memory_mb
        if self.cluster_name:
            clusterInfo_body['cluster_name'] = self.cluster_name
        if self.cluster_source:
            clusterInfo_body['cluster_source'] = self.cluster_source.value
        if self.creator_user_name:
            clusterInfo_body['creator_user_name'] = self.creator_user_name
        if self.custom_tags:
            clusterInfo_body['custom_tags'] = self.custom_tags
        if self.default_tags:
            clusterInfo_body['default_tags'] = self.default_tags
        if self.driver:
            clusterInfo_body['driver'] = self.driver.as_request()[1]
        if self.driver_instance_pool_id:
            clusterInfo_body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id:
            clusterInfo_body['driver_node_type_id'] = self.driver_node_type_id
        if self.effective_spark_version:
            clusterInfo_body['effective_spark_version'] = self.effective_spark_version
        if self.enable_elastic_disk:
            clusterInfo_body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption:
            clusterInfo_body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.executors:
            clusterInfo_body['executors'] = [v.as_request()[1] for v in self.executors]
        if self.gcp_attributes:
            clusterInfo_body['gcp_attributes'] = self.gcp_attributes.as_request()[1]
        if self.instance_pool_id:
            clusterInfo_body['instance_pool_id'] = self.instance_pool_id
        if self.jdbc_port:
            clusterInfo_body['jdbc_port'] = self.jdbc_port
        if self.last_restarted_time:
            clusterInfo_body['last_restarted_time'] = self.last_restarted_time
        if self.last_state_loss_time:
            clusterInfo_body['last_state_loss_time'] = self.last_state_loss_time
        if self.node_type_id:
            clusterInfo_body['node_type_id'] = self.node_type_id
        if self.num_workers:
            clusterInfo_body['num_workers'] = self.num_workers
        if self.policy_id:
            clusterInfo_body['policy_id'] = self.policy_id
        if self.runtime_engine:
            clusterInfo_body['runtime_engine'] = self.runtime_engine.value
        if self.spark_conf:
            clusterInfo_body['spark_conf'] = self.spark_conf
        if self.spark_context_id:
            clusterInfo_body['spark_context_id'] = self.spark_context_id
        if self.spark_env_vars:
            clusterInfo_body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version:
            clusterInfo_body['spark_version'] = self.spark_version
        if self.ssh_public_keys:
            clusterInfo_body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        if self.start_time:
            clusterInfo_body['start_time'] = self.start_time
        if self.state:
            clusterInfo_body['state'] = self.state.value
        if self.state_message:
            clusterInfo_body['state_message'] = self.state_message
        if self.terminated_time:
            clusterInfo_body['terminated_time'] = self.terminated_time
        if self.termination_reason:
            clusterInfo_body['termination_reason'] = self.termination_reason.as_request()[1]
        if self.workload_type:
            clusterInfo_body['workload_type'] = self.workload_type.as_request()[1]
        
        return clusterInfo_query, clusterInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterInfo':
        return cls(
            autoscale=AutoScale.from_dict(d['autoscale']) if 'autoscale' in d else None,
            autotermination_minutes=d.get('autotermination_minutes', None),
            aws_attributes=AwsAttributes.from_dict(d['aws_attributes']) if 'aws_attributes' in d else None,
            azure_attributes=AzureAttributes.from_dict(d['azure_attributes']) if 'azure_attributes' in d else None,
            cluster_cores=d.get('cluster_cores', None),
            cluster_id=d.get('cluster_id', None),
            cluster_log_conf=ClusterLogConf.from_dict(d['cluster_log_conf']) if 'cluster_log_conf' in d else None,
            cluster_log_status=LogSyncStatus.from_dict(d['cluster_log_status']) if 'cluster_log_status' in d else None,
            cluster_memory_mb=d.get('cluster_memory_mb', None),
            cluster_name=d.get('cluster_name', None),
            cluster_source=ClusterInfoClusterSource(d['cluster_source']) if 'cluster_source' in d else None,
            creator_user_name=d.get('creator_user_name', None),
            custom_tags=d.get('custom_tags', None),
            default_tags=d.get('default_tags', None),
            driver=SparkNode.from_dict(d['driver']) if 'driver' in d else None,
            driver_instance_pool_id=d.get('driver_instance_pool_id', None),
            driver_node_type_id=d.get('driver_node_type_id', None),
            effective_spark_version=d.get('effective_spark_version', None),
            enable_elastic_disk=d.get('enable_elastic_disk', None),
            enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
            executors=[SparkNode.from_dict(v) for v in d['executors']] if 'executors' in d else None,
            gcp_attributes=GcpAttributes.from_dict(d['gcp_attributes']) if 'gcp_attributes' in d else None,
            instance_pool_id=d.get('instance_pool_id', None),
            jdbc_port=d.get('jdbc_port', None),
            last_restarted_time=d.get('last_restarted_time', None),
            last_state_loss_time=d.get('last_state_loss_time', None),
            node_type_id=d.get('node_type_id', None),
            num_workers=d.get('num_workers', None),
            policy_id=d.get('policy_id', None),
            runtime_engine=ClusterInfoRuntimeEngine(d['runtime_engine']) if 'runtime_engine' in d else None,
            spark_conf=d.get('spark_conf', None),
            spark_context_id=d.get('spark_context_id', None),
            spark_env_vars=d.get('spark_env_vars', None),
            spark_version=d.get('spark_version', None),
            ssh_public_keys=d.get('ssh_public_keys', None),
            start_time=d.get('start_time', None),
            state=ClusterInfoState(d['state']) if 'state' in d else None,
            state_message=d.get('state_message', None),
            terminated_time=d.get('terminated_time', None),
            termination_reason=TerminationReason.from_dict(d['termination_reason']) if 'termination_reason' in d else None,
            workload_type=WorkloadType.from_dict(d['workload_type']) if 'workload_type' in d else None,
        )



class ClusterInfoClusterSource(Enum):
    """Determines whether the cluster was created by a user through the UI, created
    by the Databricks Jobs Scheduler, or through an API request. This is the
    same as cluster_creator, but read only."""
    
    API = 'API'
    JOB = 'JOB'
    MODELS = 'MODELS'
    PIPELINE = 'PIPELINE'
    PIPELINE_MAINTENANCE = 'PIPELINE_MAINTENANCE'
    SQL = 'SQL'
    UI = 'UI'

class ClusterInfoRuntimeEngine(Enum):
    """Decides which runtime engine to be use, e.g. Standard vs. Photon. If
    unspecified, the runtime engine is inferred from spark_version."""
    
    NULL = 'NULL'
    PHOTON = 'PHOTON'
    STANDARD = 'STANDARD'

class ClusterInfoState(Enum):
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
class ClusterLogConf:
    
    # destination needs to be provided. e.g. ``{ "dbfs" : { "destination" :
    # "dbfs:/home/cluster_log" } }``
    dbfs: 'DbfsStorageInfo' = None
    # destination and either region or endpoint should also be provided. e.g.
    # ``{ "s3": { "destination" : "s3://cluster_log_bucket/prefix", "region" :
    # "us-west-2" } }`` Cluster iam role is used to access s3, please make sure
    # the cluster iam role in ``instance_profile_arn`` has permission to write
    # data to the s3 destination.
    s3: 'S3StorageInfo' = None

    def as_request(self) -> (dict, dict):
        clusterLogConf_query, clusterLogConf_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.dbfs:
            clusterLogConf_body['dbfs'] = self.dbfs.as_request()[1]
        if self.s3:
            clusterLogConf_body['s3'] = self.s3.as_request()[1]
        
        return clusterLogConf_query, clusterLogConf_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterLogConf':
        return cls(
            dbfs=DbfsStorageInfo.from_dict(d['dbfs']) if 'dbfs' in d else None,
            s3=S3StorageInfo.from_dict(d['s3']) if 's3' in d else None,
        )



@dataclass
class ClusterSize:
    
    # Parameters needed in order to automatically scale clusters up and down
    # based on load. Note: autoscaling works best with DB runtime versions 3.0
    # or later.
    autoscale: 'AutoScale' = None
    # Number of worker nodes that this cluster should have. A cluster has one
    # Spark Driver and ``num_workers`` Executors for a total of ``num_workers``
    # + 1 Spark nodes.
    # 
    # Note: When reading the properties of a cluster, this field reflects the
    # desired number of workers rather than the actual current number of
    # workers. For instance, if a cluster is resized from 5 to 10 workers, this
    # field will immediately be updated to reflect the target size of 10
    # workers, whereas the workers listed in ``spark_info`` will gradually
    # increase from 5 to 10 as the new nodes are provisioned.
    num_workers: int = None

    def as_request(self) -> (dict, dict):
        clusterSize_query, clusterSize_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.autoscale:
            clusterSize_body['autoscale'] = self.autoscale.as_request()[1]
        if self.num_workers:
            clusterSize_body['num_workers'] = self.num_workers
        
        return clusterSize_query, clusterSize_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterSize':
        return cls(
            autoscale=AutoScale.from_dict(d['autoscale']) if 'autoscale' in d else None,
            num_workers=d.get('num_workers', None),
        )



@dataclass
class CreateCluster:
    
    # Note: This field won't be true for webapp requests. Only API users will
    # check this field.
    apply_policy_default_values: bool = None
    # Parameters needed in order to automatically scale clusters up and down
    # based on load. Note: autoscaling works best with DB runtime versions 3.0
    # or later.
    autoscale: 'AutoScale' = None
    # Automatically terminates the cluster after it is inactive for this time in
    # minutes. If not set, this cluster will not be automatically terminated. If
    # specified, the threshold must be between 10 and 10000 minutes. Users can
    # also set this value to 0 to explicitly disable automatic termination.
    autotermination_minutes: int = None
    # Attributes related to clusters running on Amazon Web Services. If not
    # specified at cluster creation, a set of default values will be used.
    aws_attributes: 'AwsAttributes' = None
    # Attributes related to clusters running on Microsoft Azure. If not
    # specified at cluster creation, a set of default values will be used.
    azure_attributes: 'AzureAttributes' = None
    # The configuration for delivering spark logs to a long-term storage
    # destination. Two kinds of destinations (dbfs and s3) are supported. Only
    # one destination can be specified for one cluster. If the conf is given,
    # the logs will be delivered to the destination every ``5 mins``. The
    # destination of driver logs is ``$destination/$clusterId/driver``, while
    # the destination of executor logs is ``$destination/$clusterId/executor``.
    cluster_log_conf: 'ClusterLogConf' = None
    # Cluster name requested by the user. This doesn't have to be unique. If not
    # specified at creation, the cluster name will be an empty string.
    cluster_name: str = None
    # Determines whether the cluster was created by a user through the UI,
    # created by the Databricks Jobs Scheduler, or through an API request. This
    # is the same as cluster_creator, but read only.
    cluster_source: 'CreateClusterClusterSource' = None
    # Additional tags for cluster resources. Databricks will tag all cluster
    # resources (e.g., AWS instances and EBS volumes) with these tags in
    # addition to ``default_tags``. Notes:
    # 
    # - Currently, Databricks allows at most 45 custom tags
    # 
    # - Clusters can only reuse cloud resources if the resources' tags are a
    # subset of the cluster tags
    custom_tags: 'Dict[str,str]' = None
    # The optional ID of the instance pool for the driver of the cluster
    # belongs. The pool cluster uses the instance pool with id
    # (instance_pool_id) if the driver pool is not assigned.
    driver_instance_pool_id: str = None
    # The node type of the Spark driver. Note that this field is optional; if
    # unset, the driver node type will be set as the same value as
    # `node_type_id` defined above.
    # 
    # This field, along with node_type_id, should not be set if
    # virtual_cluster_size is set. If both driver_node_type_id, node_type_id,
    # and virtual_cluster_size are specified, driver_node_type_id and
    # node_type_id take precedence.
    driver_node_type_id: str = None
    # The key of the spark version running in the dataplane. This is possibly
    # different from the spark_version (index 2). The spark_version is the raw
    # string provided by the user through API or UI, which could map to a
    # different effective_spark_version running in the dataplane, depending on
    # the cluster's instance type or the runtimeEngine parameter.
    effective_spark_version: str = None
    # Autoscaling Local Storage: when enabled, this cluster will dynamically
    # acquire additional disk space when its Spark workers are running low on
    # disk space. This feature requires specific AWS permissions to function
    # correctly - refer to the User Guide for more details.
    enable_elastic_disk: bool = None
    # Whether to enable LUKS on cluster VMs' local disks
    enable_local_disk_encryption: bool = None
    # Attributes related to clusters running on Google Cloud Platform. If not
    # specified at cluster creation, a set of default values will be used.
    gcp_attributes: 'GcpAttributes' = None
    # The optional ID of the instance pool to which the cluster belongs.
    instance_pool_id: str = None
    # This field encodes, through a single value, the resources available to
    # each of the Spark nodes in this cluster. For example, the Spark nodes can
    # be provisioned and optimized for memory or compute intensive workloads A
    # list of available node types can be retrieved by using the
    # :ref:`clusterClusterServicelistNodeTypes` API call.
    # 
    # This field, along with driver_node_type_id, should not be set if
    # virtual_cluster_size is set. If both driver_node_type_id, node_type_id,
    # and virtual_cluster_size are specified, driver_node_type_id and
    # node_type_id take precedence.
    node_type_id: str = None
    # Number of worker nodes that this cluster should have. A cluster has one
    # Spark Driver and ``num_workers`` Executors for a total of ``num_workers``
    # + 1 Spark nodes.
    # 
    # Note: When reading the properties of a cluster, this field reflects the
    # desired number of workers rather than the actual current number of
    # workers. For instance, if a cluster is resized from 5 to 10 workers, this
    # field will immediately be updated to reflect the target size of 10
    # workers, whereas the workers listed in ``spark_info`` will gradually
    # increase from 5 to 10 as the new nodes are provisioned.
    num_workers: int = None
    # The ID of the cluster policy used to create the cluster if applicable.
    policy_id: str = None
    # Decides which runtime engine to be use, e.g. Standard vs. Photon. If
    # unspecified, the runtime engine is inferred from spark_version.
    runtime_engine: 'CreateClusterRuntimeEngine' = None
    # An object containing a set of optional, user-specified Spark configuration
    # key-value pairs. Users can also pass in a string of extra JVM options to
    # the driver and the executors via ``spark.driver.extraJavaOptions`` and
    # ``spark.executor.extraJavaOptions`` respectively.
    spark_conf: 'Dict[str,str]' = None
    # An object containing a set of optional, user-specified environment
    # variable key-value pairs. Please note that key-value pair of the form
    # (X,Y) will be exported as is (i.e., ``export X='Y'``) while launching the
    # driver and workers.
    # 
    # In order to specify an additional set of ``SPARK_DAEMON_JAVA_OPTS``, we
    # recommend appending them to ``$SPARK_DAEMON_JAVA_OPTS`` as shown in the
    # example below. This ensures that all default databricks managed
    # environmental variables are included as well.
    # 
    # Example Spark environment variables: ``{"SPARK_WORKER_MEMORY": "28000m",
    # "SPARK_LOCAL_DIRS": "/local_disk0"}`` or ``{"SPARK_DAEMON_JAVA_OPTS":
    # "$SPARK_DAEMON_JAVA_OPTS -Dspark.shuffle.service.enabled=true"}``
    spark_env_vars: 'Dict[str,str]' = None
    # The Spark version of the cluster, e.g. "3.3.x-scala2.11". A list of
    # available Spark versions can be retrieved by using the
    # :ref:`clusterClusterServicelistSparkVersions` API call. This is the Spark
    # version provided from the user input (API/UI) and may be different from
    # the effective_spark_version, which is the spark version that is actually
    # run in the dataplane. See index 45 for more context.
    spark_version: str = None
    # SSH public key contents that will be added to each Spark node in this
    # cluster. The corresponding private keys can be used to login with the user
    # name ``ubuntu`` on port ``2200``. Up to 10 keys can be specified.
    ssh_public_keys: 'List[str]' = None
    
    workload_type: 'WorkloadType' = None

    def as_request(self) -> (dict, dict):
        createCluster_query, createCluster_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.apply_policy_default_values:
            createCluster_body['apply_policy_default_values'] = self.apply_policy_default_values
        if self.autoscale:
            createCluster_body['autoscale'] = self.autoscale.as_request()[1]
        if self.autotermination_minutes:
            createCluster_body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes:
            createCluster_body['aws_attributes'] = self.aws_attributes.as_request()[1]
        if self.azure_attributes:
            createCluster_body['azure_attributes'] = self.azure_attributes.as_request()[1]
        if self.cluster_log_conf:
            createCluster_body['cluster_log_conf'] = self.cluster_log_conf.as_request()[1]
        if self.cluster_name:
            createCluster_body['cluster_name'] = self.cluster_name
        if self.cluster_source:
            createCluster_body['cluster_source'] = self.cluster_source.value
        if self.custom_tags:
            createCluster_body['custom_tags'] = self.custom_tags
        if self.driver_instance_pool_id:
            createCluster_body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id:
            createCluster_body['driver_node_type_id'] = self.driver_node_type_id
        if self.effective_spark_version:
            createCluster_body['effective_spark_version'] = self.effective_spark_version
        if self.enable_elastic_disk:
            createCluster_body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption:
            createCluster_body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.gcp_attributes:
            createCluster_body['gcp_attributes'] = self.gcp_attributes.as_request()[1]
        if self.instance_pool_id:
            createCluster_body['instance_pool_id'] = self.instance_pool_id
        if self.node_type_id:
            createCluster_body['node_type_id'] = self.node_type_id
        if self.num_workers:
            createCluster_body['num_workers'] = self.num_workers
        if self.policy_id:
            createCluster_body['policy_id'] = self.policy_id
        if self.runtime_engine:
            createCluster_body['runtime_engine'] = self.runtime_engine.value
        if self.spark_conf:
            createCluster_body['spark_conf'] = self.spark_conf
        if self.spark_env_vars:
            createCluster_body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version:
            createCluster_body['spark_version'] = self.spark_version
        if self.ssh_public_keys:
            createCluster_body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        if self.workload_type:
            createCluster_body['workload_type'] = self.workload_type.as_request()[1]
        
        return createCluster_query, createCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCluster':
        return cls(
            apply_policy_default_values=d.get('apply_policy_default_values', None),
            autoscale=AutoScale.from_dict(d['autoscale']) if 'autoscale' in d else None,
            autotermination_minutes=d.get('autotermination_minutes', None),
            aws_attributes=AwsAttributes.from_dict(d['aws_attributes']) if 'aws_attributes' in d else None,
            azure_attributes=AzureAttributes.from_dict(d['azure_attributes']) if 'azure_attributes' in d else None,
            cluster_log_conf=ClusterLogConf.from_dict(d['cluster_log_conf']) if 'cluster_log_conf' in d else None,
            cluster_name=d.get('cluster_name', None),
            cluster_source=CreateClusterClusterSource(d['cluster_source']) if 'cluster_source' in d else None,
            custom_tags=d.get('custom_tags', None),
            driver_instance_pool_id=d.get('driver_instance_pool_id', None),
            driver_node_type_id=d.get('driver_node_type_id', None),
            effective_spark_version=d.get('effective_spark_version', None),
            enable_elastic_disk=d.get('enable_elastic_disk', None),
            enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
            gcp_attributes=GcpAttributes.from_dict(d['gcp_attributes']) if 'gcp_attributes' in d else None,
            instance_pool_id=d.get('instance_pool_id', None),
            node_type_id=d.get('node_type_id', None),
            num_workers=d.get('num_workers', None),
            policy_id=d.get('policy_id', None),
            runtime_engine=CreateClusterRuntimeEngine(d['runtime_engine']) if 'runtime_engine' in d else None,
            spark_conf=d.get('spark_conf', None),
            spark_env_vars=d.get('spark_env_vars', None),
            spark_version=d.get('spark_version', None),
            ssh_public_keys=d.get('ssh_public_keys', None),
            workload_type=WorkloadType.from_dict(d['workload_type']) if 'workload_type' in d else None,
        )



class CreateClusterClusterSource(Enum):
    """Determines whether the cluster was created by a user through the UI, created
    by the Databricks Jobs Scheduler, or through an API request. This is the
    same as cluster_creator, but read only."""
    
    API = 'API'
    JOB = 'JOB'
    MODELS = 'MODELS'
    PIPELINE = 'PIPELINE'
    PIPELINE_MAINTENANCE = 'PIPELINE_MAINTENANCE'
    SQL = 'SQL'
    UI = 'UI'

@dataclass
class CreateClusterResponse:
    
    
    cluster_id: str = None

    def as_request(self) -> (dict, dict):
        createClusterResponse_query, createClusterResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cluster_id:
            createClusterResponse_body['cluster_id'] = self.cluster_id
        
        return createClusterResponse_query, createClusterResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateClusterResponse':
        return cls(
            cluster_id=d.get('cluster_id', None),
        )



class CreateClusterRuntimeEngine(Enum):
    """Decides which runtime engine to be use, e.g. Standard vs. Photon. If
    unspecified, the runtime engine is inferred from spark_version."""
    
    NULL = 'NULL'
    PHOTON = 'PHOTON'
    STANDARD = 'STANDARD'

@dataclass
class DataPlaneEventDetails:
    
    # <needs content added>
    event_type: 'DataPlaneEventDetailsEventType' = None
    # <needs content added>
    executor_failures: int = None
    # <needs content added>
    host_id: str = None
    # <needs content added>
    timestamp: int = None

    def as_request(self) -> (dict, dict):
        dataPlaneEventDetails_query, dataPlaneEventDetails_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.event_type:
            dataPlaneEventDetails_body['event_type'] = self.event_type.value
        if self.executor_failures:
            dataPlaneEventDetails_body['executor_failures'] = self.executor_failures
        if self.host_id:
            dataPlaneEventDetails_body['host_id'] = self.host_id
        if self.timestamp:
            dataPlaneEventDetails_body['timestamp'] = self.timestamp
        
        return dataPlaneEventDetails_query, dataPlaneEventDetails_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DataPlaneEventDetails':
        return cls(
            event_type=DataPlaneEventDetailsEventType(d['event_type']) if 'event_type' in d else None,
            executor_failures=d.get('executor_failures', None),
            host_id=d.get('host_id', None),
            timestamp=d.get('timestamp', None),
        )



class DataPlaneEventDetailsEventType(Enum):
    """<needs content added>"""
    
    NODE_BLACKLISTED = 'NODE_BLACKLISTED'
    NODE_EXCLUDED_DECOMMISSIONED = 'NODE_EXCLUDED_DECOMMISSIONED'

@dataclass
class DbfsStorageInfo:
    
    # dbfs destination, e.g. ``dbfs:/my/path``
    destination: str = None

    def as_request(self) -> (dict, dict):
        dbfsStorageInfo_query, dbfsStorageInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.destination:
            dbfsStorageInfo_body['destination'] = self.destination
        
        return dbfsStorageInfo_query, dbfsStorageInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DbfsStorageInfo':
        return cls(
            destination=d.get('destination', None),
        )



@dataclass
class DeleteCluster:
    
    # The cluster to be terminated.
    cluster_id: str

    def as_request(self) -> (dict, dict):
        deleteCluster_query, deleteCluster_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cluster_id:
            deleteCluster_body['cluster_id'] = self.cluster_id
        
        return deleteCluster_query, deleteCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteCluster':
        return cls(
            cluster_id=d.get('cluster_id', None),
        )



@dataclass
class EditCluster:
    
    # <needs content added>
    cluster_id: str
    # Note: This field won't be true for webapp requests. Only API users will
    # check this field.
    apply_policy_default_values: bool = None
    # Parameters needed in order to automatically scale clusters up and down
    # based on load. Note: autoscaling works best with DB runtime versions 3.0
    # or later.
    autoscale: 'AutoScale' = None
    # Automatically terminates the cluster after it is inactive for this time in
    # minutes. If not set, this cluster will not be automatically terminated. If
    # specified, the threshold must be between 10 and 10000 minutes. Users can
    # also set this value to 0 to explicitly disable automatic termination.
    autotermination_minutes: int = None
    # Attributes related to clusters running on Amazon Web Services. If not
    # specified at cluster creation, a set of default values will be used.
    aws_attributes: 'AwsAttributes' = None
    # Attributes related to clusters running on Microsoft Azure. If not
    # specified at cluster creation, a set of default values will be used.
    azure_attributes: 'AzureAttributes' = None
    # The configuration for delivering spark logs to a long-term storage
    # destination. Two kinds of destinations (dbfs and s3) are supported. Only
    # one destination can be specified for one cluster. If the conf is given,
    # the logs will be delivered to the destination every ``5 mins``. The
    # destination of driver logs is ``$destination/$clusterId/driver``, while
    # the destination of executor logs is ``$destination/$clusterId/executor``.
    cluster_log_conf: 'ClusterLogConf' = None
    # Cluster name requested by the user. This doesn't have to be unique. If not
    # specified at creation, the cluster name will be an empty string.
    cluster_name: str = None
    # Determines whether the cluster was created by a user through the UI,
    # created by the Databricks Jobs Scheduler, or through an API request. This
    # is the same as cluster_creator, but read only.
    cluster_source: 'EditClusterClusterSource' = None
    # Additional tags for cluster resources. Databricks will tag all cluster
    # resources (e.g., AWS instances and EBS volumes) with these tags in
    # addition to ``default_tags``. Notes:
    # 
    # - Currently, Databricks allows at most 45 custom tags
    # 
    # - Clusters can only reuse cloud resources if the resources' tags are a
    # subset of the cluster tags
    custom_tags: 'Dict[str,str]' = None
    # The optional ID of the instance pool for the driver of the cluster
    # belongs. The pool cluster uses the instance pool with id
    # (instance_pool_id) if the driver pool is not assigned.
    driver_instance_pool_id: str = None
    # The node type of the Spark driver. Note that this field is optional; if
    # unset, the driver node type will be set as the same value as
    # `node_type_id` defined above.
    # 
    # This field, along with node_type_id, should not be set if
    # virtual_cluster_size is set. If both driver_node_type_id, node_type_id,
    # and virtual_cluster_size are specified, driver_node_type_id and
    # node_type_id take precedence.
    driver_node_type_id: str = None
    # The key of the spark version running in the dataplane. This is possibly
    # different from the spark_version (index 2). The spark_version is the raw
    # string provided by the user through API or UI, which could map to a
    # different effective_spark_version running in the dataplane, depending on
    # the cluster's instance type or the runtimeEngine parameter.
    effective_spark_version: str = None
    # Autoscaling Local Storage: when enabled, this cluster will dynamically
    # acquire additional disk space when its Spark workers are running low on
    # disk space. This feature requires specific AWS permissions to function
    # correctly - refer to the User Guide for more details.
    enable_elastic_disk: bool = None
    # Whether to enable LUKS on cluster VMs' local disks
    enable_local_disk_encryption: bool = None
    # Attributes related to clusters running on Google Cloud Platform. If not
    # specified at cluster creation, a set of default values will be used.
    gcp_attributes: 'GcpAttributes' = None
    # The optional ID of the instance pool to which the cluster belongs.
    instance_pool_id: str = None
    # This field encodes, through a single value, the resources available to
    # each of the Spark nodes in this cluster. For example, the Spark nodes can
    # be provisioned and optimized for memory or compute intensive workloads A
    # list of available node types can be retrieved by using the
    # :ref:`clusterClusterServicelistNodeTypes` API call.
    # 
    # This field, along with driver_node_type_id, should not be set if
    # virtual_cluster_size is set. If both driver_node_type_id, node_type_id,
    # and virtual_cluster_size are specified, driver_node_type_id and
    # node_type_id take precedence.
    node_type_id: str = None
    # Number of worker nodes that this cluster should have. A cluster has one
    # Spark Driver and ``num_workers`` Executors for a total of ``num_workers``
    # + 1 Spark nodes.
    # 
    # Note: When reading the properties of a cluster, this field reflects the
    # desired number of workers rather than the actual current number of
    # workers. For instance, if a cluster is resized from 5 to 10 workers, this
    # field will immediately be updated to reflect the target size of 10
    # workers, whereas the workers listed in ``spark_info`` will gradually
    # increase from 5 to 10 as the new nodes are provisioned.
    num_workers: int = None
    # The ID of the cluster policy used to create the cluster if applicable.
    policy_id: str = None
    # Decides which runtime engine to be use, e.g. Standard vs. Photon. If
    # unspecified, the runtime engine is inferred from spark_version.
    runtime_engine: 'EditClusterRuntimeEngine' = None
    # An object containing a set of optional, user-specified Spark configuration
    # key-value pairs. Users can also pass in a string of extra JVM options to
    # the driver and the executors via ``spark.driver.extraJavaOptions`` and
    # ``spark.executor.extraJavaOptions`` respectively.
    # 
    # Example Spark confs: ``{"spark.speculation": true,
    # "spark.streaming.ui.retainedBatches": 5}`` or
    # ``{"spark.driver.extraJavaOptions": "-verbose:gc -XX:+PrintGCDetails"}``
    spark_conf: 'Dict[str,str]' = None
    # An object containing a set of optional, user-specified environment
    # variable key-value pairs. Please note that key-value pair of the form
    # (X,Y) will be exported as is (i.e., ``export X='Y'``) while launching the
    # driver and workers.
    # 
    # In order to specify an additional set of ``SPARK_DAEMON_JAVA_OPTS``, we
    # recommend appending them to ``$SPARK_DAEMON_JAVA_OPTS`` as shown in the
    # example below. This ensures that all default databricks managed
    # environmental variables are included as well.
    # 
    # Example Spark environment variables: ``{"SPARK_WORKER_MEMORY": "28000m",
    # "SPARK_LOCAL_DIRS": "/local_disk0"}`` or ``{"SPARK_DAEMON_JAVA_OPTS":
    # "$SPARK_DAEMON_JAVA_OPTS -Dspark.shuffle.service.enabled=true"}``
    spark_env_vars: 'Dict[str,str]' = None
    # The Spark version of the cluster, e.g. "3.3.x-scala2.11". A list of
    # available Spark versions can be retrieved by using the
    # :ref:`clusterClusterServicelistSparkVersions` API call. This is the Spark
    # version provided from the user input (API/UI) and may be different from
    # the effective_spark_version, which is the spark version that is actually
    # run in the dataplane. See index 45 for more context.
    spark_version: str = None
    # SSH public key contents that will be added to each Spark node in this
    # cluster. The corresponding private keys can be used to login with the user
    # name ``ubuntu`` on port ``2200``. Up to 10 keys can be specified.
    ssh_public_keys: 'List[str]' = None
    # <needs content added>
    workload_type: 'WorkloadType' = None

    def as_request(self) -> (dict, dict):
        editCluster_query, editCluster_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.apply_policy_default_values:
            editCluster_body['apply_policy_default_values'] = self.apply_policy_default_values
        if self.autoscale:
            editCluster_body['autoscale'] = self.autoscale.as_request()[1]
        if self.autotermination_minutes:
            editCluster_body['autotermination_minutes'] = self.autotermination_minutes
        if self.aws_attributes:
            editCluster_body['aws_attributes'] = self.aws_attributes.as_request()[1]
        if self.azure_attributes:
            editCluster_body['azure_attributes'] = self.azure_attributes.as_request()[1]
        if self.cluster_id:
            editCluster_body['cluster_id'] = self.cluster_id
        if self.cluster_log_conf:
            editCluster_body['cluster_log_conf'] = self.cluster_log_conf.as_request()[1]
        if self.cluster_name:
            editCluster_body['cluster_name'] = self.cluster_name
        if self.cluster_source:
            editCluster_body['cluster_source'] = self.cluster_source.value
        if self.custom_tags:
            editCluster_body['custom_tags'] = self.custom_tags
        if self.driver_instance_pool_id:
            editCluster_body['driver_instance_pool_id'] = self.driver_instance_pool_id
        if self.driver_node_type_id:
            editCluster_body['driver_node_type_id'] = self.driver_node_type_id
        if self.effective_spark_version:
            editCluster_body['effective_spark_version'] = self.effective_spark_version
        if self.enable_elastic_disk:
            editCluster_body['enable_elastic_disk'] = self.enable_elastic_disk
        if self.enable_local_disk_encryption:
            editCluster_body['enable_local_disk_encryption'] = self.enable_local_disk_encryption
        if self.gcp_attributes:
            editCluster_body['gcp_attributes'] = self.gcp_attributes.as_request()[1]
        if self.instance_pool_id:
            editCluster_body['instance_pool_id'] = self.instance_pool_id
        if self.node_type_id:
            editCluster_body['node_type_id'] = self.node_type_id
        if self.num_workers:
            editCluster_body['num_workers'] = self.num_workers
        if self.policy_id:
            editCluster_body['policy_id'] = self.policy_id
        if self.runtime_engine:
            editCluster_body['runtime_engine'] = self.runtime_engine.value
        if self.spark_conf:
            editCluster_body['spark_conf'] = self.spark_conf
        if self.spark_env_vars:
            editCluster_body['spark_env_vars'] = self.spark_env_vars
        if self.spark_version:
            editCluster_body['spark_version'] = self.spark_version
        if self.ssh_public_keys:
            editCluster_body['ssh_public_keys'] = [v for v in self.ssh_public_keys]
        if self.workload_type:
            editCluster_body['workload_type'] = self.workload_type.as_request()[1]
        
        return editCluster_query, editCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditCluster':
        return cls(
            apply_policy_default_values=d.get('apply_policy_default_values', None),
            autoscale=AutoScale.from_dict(d['autoscale']) if 'autoscale' in d else None,
            autotermination_minutes=d.get('autotermination_minutes', None),
            aws_attributes=AwsAttributes.from_dict(d['aws_attributes']) if 'aws_attributes' in d else None,
            azure_attributes=AzureAttributes.from_dict(d['azure_attributes']) if 'azure_attributes' in d else None,
            cluster_id=d.get('cluster_id', None),
            cluster_log_conf=ClusterLogConf.from_dict(d['cluster_log_conf']) if 'cluster_log_conf' in d else None,
            cluster_name=d.get('cluster_name', None),
            cluster_source=EditClusterClusterSource(d['cluster_source']) if 'cluster_source' in d else None,
            custom_tags=d.get('custom_tags', None),
            driver_instance_pool_id=d.get('driver_instance_pool_id', None),
            driver_node_type_id=d.get('driver_node_type_id', None),
            effective_spark_version=d.get('effective_spark_version', None),
            enable_elastic_disk=d.get('enable_elastic_disk', None),
            enable_local_disk_encryption=d.get('enable_local_disk_encryption', None),
            gcp_attributes=GcpAttributes.from_dict(d['gcp_attributes']) if 'gcp_attributes' in d else None,
            instance_pool_id=d.get('instance_pool_id', None),
            node_type_id=d.get('node_type_id', None),
            num_workers=d.get('num_workers', None),
            policy_id=d.get('policy_id', None),
            runtime_engine=EditClusterRuntimeEngine(d['runtime_engine']) if 'runtime_engine' in d else None,
            spark_conf=d.get('spark_conf', None),
            spark_env_vars=d.get('spark_env_vars', None),
            spark_version=d.get('spark_version', None),
            ssh_public_keys=d.get('ssh_public_keys', None),
            workload_type=WorkloadType.from_dict(d['workload_type']) if 'workload_type' in d else None,
        )



class EditClusterClusterSource(Enum):
    """Determines whether the cluster was created by a user through the UI, created
    by the Databricks Jobs Scheduler, or through an API request. This is the
    same as cluster_creator, but read only."""
    
    API = 'API'
    JOB = 'JOB'
    MODELS = 'MODELS'
    PIPELINE = 'PIPELINE'
    PIPELINE_MAINTENANCE = 'PIPELINE_MAINTENANCE'
    SQL = 'SQL'
    UI = 'UI'

class EditClusterRuntimeEngine(Enum):
    """Decides which runtime engine to be use, e.g. Standard vs. Photon. If
    unspecified, the runtime engine is inferred from spark_version."""
    
    NULL = 'NULL'
    PHOTON = 'PHOTON'
    STANDARD = 'STANDARD'

@dataclass
class EventDetails:
    
    # * For created clusters, the attributes of the cluster. * For edited
    # clusters, the new attributes of the cluster.
    attributes: 'ClusterAttributes' = None
    # The cause of a change in target size.
    cause: 'EventDetailsCause' = None
    # The actual cluster size that was set in the cluster creation or edit.
    cluster_size: 'ClusterSize' = None
    # The current number of vCPUs in the cluster.
    current_num_vcpus: int = None
    # The current number of nodes in the cluster.
    current_num_workers: int = None
    # <needs content added>
    did_not_expand_reason: str = None
    # Current disk size in bytes
    disk_size: int = None
    # More details about the change in driver's state
    driver_state_message: str = None
    # Whether or not a blocklisted node should be terminated. For
    # ClusterEventType NODE_BLACKLISTED.
    enable_termination_for_node_blocklisted: bool = None
    # <needs content added>
    free_space: int = None
    # Instance Id where the event originated from
    instance_id: str = None
    # Unique identifier of the specific job run associated with this cluster
    # event * For clusters created for jobs, this will be the same as the
    # cluster name
    job_run_name: str = None
    # The cluster attributes before a cluster was edited.
    previous_attributes: 'ClusterAttributes' = None
    # The size of the cluster before an edit or resize.
    previous_cluster_size: 'ClusterSize' = None
    # Previous disk size in bytes
    previous_disk_size: int = None
    # A termination reason: * On a TERMINATED event, this is the reason of the
    # termination. * On a RESIZE_COMPLETE event, this indicates the reason that
    # we failed to acquire some nodes.
    reason: 'TerminationReason' = None
    # The targeted number of vCPUs in the cluster.
    target_num_vcpus: int = None
    # The targeted number of nodes in the cluster.
    target_num_workers: int = None
    # The user that caused the event to occur. (Empty if it was done by the
    # control plane.)
    user: str = None

    def as_request(self) -> (dict, dict):
        eventDetails_query, eventDetails_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.attributes:
            eventDetails_body['attributes'] = self.attributes.as_request()[1]
        if self.cause:
            eventDetails_body['cause'] = self.cause.value
        if self.cluster_size:
            eventDetails_body['cluster_size'] = self.cluster_size.as_request()[1]
        if self.current_num_vcpus:
            eventDetails_body['current_num_vcpus'] = self.current_num_vcpus
        if self.current_num_workers:
            eventDetails_body['current_num_workers'] = self.current_num_workers
        if self.did_not_expand_reason:
            eventDetails_body['did_not_expand_reason'] = self.did_not_expand_reason
        if self.disk_size:
            eventDetails_body['disk_size'] = self.disk_size
        if self.driver_state_message:
            eventDetails_body['driver_state_message'] = self.driver_state_message
        if self.enable_termination_for_node_blocklisted:
            eventDetails_body['enable_termination_for_node_blocklisted'] = self.enable_termination_for_node_blocklisted
        if self.free_space:
            eventDetails_body['free_space'] = self.free_space
        if self.instance_id:
            eventDetails_body['instance_id'] = self.instance_id
        if self.job_run_name:
            eventDetails_body['job_run_name'] = self.job_run_name
        if self.previous_attributes:
            eventDetails_body['previous_attributes'] = self.previous_attributes.as_request()[1]
        if self.previous_cluster_size:
            eventDetails_body['previous_cluster_size'] = self.previous_cluster_size.as_request()[1]
        if self.previous_disk_size:
            eventDetails_body['previous_disk_size'] = self.previous_disk_size
        if self.reason:
            eventDetails_body['reason'] = self.reason.as_request()[1]
        if self.target_num_vcpus:
            eventDetails_body['target_num_vcpus'] = self.target_num_vcpus
        if self.target_num_workers:
            eventDetails_body['target_num_workers'] = self.target_num_workers
        if self.user:
            eventDetails_body['user'] = self.user
        
        return eventDetails_query, eventDetails_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EventDetails':
        return cls(
            attributes=ClusterAttributes.from_dict(d['attributes']) if 'attributes' in d else None,
            cause=EventDetailsCause(d['cause']) if 'cause' in d else None,
            cluster_size=ClusterSize.from_dict(d['cluster_size']) if 'cluster_size' in d else None,
            current_num_vcpus=d.get('current_num_vcpus', None),
            current_num_workers=d.get('current_num_workers', None),
            did_not_expand_reason=d.get('did_not_expand_reason', None),
            disk_size=d.get('disk_size', None),
            driver_state_message=d.get('driver_state_message', None),
            enable_termination_for_node_blocklisted=d.get('enable_termination_for_node_blocklisted', None),
            free_space=d.get('free_space', None),
            instance_id=d.get('instance_id', None),
            job_run_name=d.get('job_run_name', None),
            previous_attributes=ClusterAttributes.from_dict(d['previous_attributes']) if 'previous_attributes' in d else None,
            previous_cluster_size=ClusterSize.from_dict(d['previous_cluster_size']) if 'previous_cluster_size' in d else None,
            previous_disk_size=d.get('previous_disk_size', None),
            reason=TerminationReason.from_dict(d['reason']) if 'reason' in d else None,
            target_num_vcpus=d.get('target_num_vcpus', None),
            target_num_workers=d.get('target_num_workers', None),
            user=d.get('user', None),
        )



class EventDetailsCause(Enum):
    """The cause of a change in target size."""
    
    AUTORECOVERY = 'AUTORECOVERY'
    AUTOSCALE = 'AUTOSCALE'
    REPLACE_BAD_NODES = 'REPLACE_BAD_NODES'
    USER_REQUEST = 'USER_REQUEST'

@dataclass
class GcpAttributes:
    
    # This field determines whether the spark executors will be scheduled to run
    # on preemptible VMs, on-demand VMs, or preemptible VMs with a fallback to
    # on-demand VMs if the former is unavailable.
    availability: 'GcpAttributesAvailability' = None
    # boot disk size in GB
    boot_disk_size: int = None
    # If provided, the cluster will impersonate the google service account when
    # accessing gcloud services (like GCS). The google service account must have
    # previously been added to the Databricks environment by an account
    # administrator.
    google_service_account: str = None

    def as_request(self) -> (dict, dict):
        gcpAttributes_query, gcpAttributes_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.availability:
            gcpAttributes_body['availability'] = self.availability.value
        if self.boot_disk_size:
            gcpAttributes_body['boot_disk_size'] = self.boot_disk_size
        if self.google_service_account:
            gcpAttributes_body['google_service_account'] = self.google_service_account
        
        return gcpAttributes_query, gcpAttributes_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GcpAttributes':
        return cls(
            availability=GcpAttributesAvailability(d['availability']) if 'availability' in d else None,
            boot_disk_size=d.get('boot_disk_size', None),
            google_service_account=d.get('google_service_account', None),
        )



class GcpAttributesAvailability(Enum):
    """This field determines whether the spark executors will be scheduled to run
    on preemptible VMs, on-demand VMs, or preemptible VMs with a fallback to
    on-demand VMs if the former is unavailable."""
    
    ON_DEMAND_GCP = 'ON_DEMAND_GCP'
    PREEMPTIBLE_GCP = 'PREEMPTIBLE_GCP'
    PREEMPTIBLE_WITH_FALLBACK_GCP = 'PREEMPTIBLE_WITH_FALLBACK_GCP'

@dataclass
class GetEvents:
    
    # The ID of the cluster to retrieve events about.
    cluster_id: str
    # The end time in epoch milliseconds. If empty, returns events up to the
    # current time.
    end_time: int = None
    # An optional set of event types to filter on. If empty, all event types are
    # returned.
    event_types: 'List[GetEventsEventTypesItem]' = None
    # The maximum number of events to include in a page of events. Defaults to
    # 50, and maximum allowed value is 500.
    limit: int = None
    # The offset in the result set. Defaults to 0 (no offset). When an offset is
    # specified and the results are requested in descending order, the end_time
    # field is required.
    offset: int = None
    # The order to list events in; either "ASC" or "DESC". Defaults to "DESC".
    order: 'GetEventsOrder' = None
    # The start time in epoch milliseconds. If empty, returns events starting
    # from the beginning of time.
    start_time: int = None

    def as_request(self) -> (dict, dict):
        getEvents_query, getEvents_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cluster_id:
            getEvents_body['cluster_id'] = self.cluster_id
        if self.end_time:
            getEvents_body['end_time'] = self.end_time
        if self.event_types:
            getEvents_body['event_types'] = [v for v in self.event_types]
        if self.limit:
            getEvents_body['limit'] = self.limit
        if self.offset:
            getEvents_body['offset'] = self.offset
        if self.order:
            getEvents_body['order'] = self.order.value
        if self.start_time:
            getEvents_body['start_time'] = self.start_time
        
        return getEvents_query, getEvents_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetEvents':
        return cls(
            cluster_id=d.get('cluster_id', None),
            end_time=d.get('end_time', None),
            event_types=d.get('event_types', None),
            limit=d.get('limit', None),
            offset=d.get('offset', None),
            order=GetEventsOrder(d['order']) if 'order' in d else None,
            start_time=d.get('start_time', None),
        )



class GetEventsEventTypesItem(Enum):
    
    
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

class GetEventsOrder(Enum):
    """The order to list events in; either "ASC" or "DESC". Defaults to "DESC"."""
    
    ASC = 'ASC'
    DESC = 'DESC'

@dataclass
class GetEventsResponse:
    
    # <content needs to be added>
    events: 'List[ClusterEvent]' = None
    # The parameters required to retrieve the next page of events. Omitted if
    # there are no more events to read.
    next_page: 'GetEvents' = None
    # The total number of events filtered by the start_time, end_time, and
    # event_types.
    total_count: int = None

    def as_request(self) -> (dict, dict):
        getEventsResponse_query, getEventsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.events:
            getEventsResponse_body['events'] = [v.as_request()[1] for v in self.events]
        if self.next_page:
            getEventsResponse_body['next_page'] = self.next_page.as_request()[1]
        if self.total_count:
            getEventsResponse_body['total_count'] = self.total_count
        
        return getEventsResponse_query, getEventsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetEventsResponse':
        return cls(
            events=[ClusterEvent.from_dict(v) for v in d['events']] if 'events' in d else None,
            next_page=GetEvents.from_dict(d['next_page']) if 'next_page' in d else None,
            total_count=d.get('total_count', None),
        )



@dataclass
class GetSparkVersionsResponse:
    
    # All the available Spark versions.
    versions: 'List[SparkVersion]' = None

    def as_request(self) -> (dict, dict):
        getSparkVersionsResponse_query, getSparkVersionsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.versions:
            getSparkVersionsResponse_body['versions'] = [v.as_request()[1] for v in self.versions]
        
        return getSparkVersionsResponse_query, getSparkVersionsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetSparkVersionsResponse':
        return cls(
            versions=[SparkVersion.from_dict(v) for v in d['versions']] if 'versions' in d else None,
        )



@dataclass
class ListAvailableZonesResponse:
    
    # The availability zone if no ``zone_id`` is provided in the cluster
    # creation request.
    default_zone: str = None
    # The list of available zones (e.g., ['us-west-2c', 'us-east-2']).
    zones: 'List[str]' = None

    def as_request(self) -> (dict, dict):
        listAvailableZonesResponse_query, listAvailableZonesResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.default_zone:
            listAvailableZonesResponse_body['default_zone'] = self.default_zone
        if self.zones:
            listAvailableZonesResponse_body['zones'] = [v for v in self.zones]
        
        return listAvailableZonesResponse_query, listAvailableZonesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListAvailableZonesResponse':
        return cls(
            default_zone=d.get('default_zone', None),
            zones=d.get('zones', None),
        )



@dataclass
class ListClustersResponse:
    
    # <needs content added>
    clusters: 'List[ClusterInfo]' = None

    def as_request(self) -> (dict, dict):
        listClustersResponse_query, listClustersResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.clusters:
            listClustersResponse_body['clusters'] = [v.as_request()[1] for v in self.clusters]
        
        return listClustersResponse_query, listClustersResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListClustersResponse':
        return cls(
            clusters=[ClusterInfo.from_dict(v) for v in d['clusters']] if 'clusters' in d else None,
        )



@dataclass
class ListNodeTypesResponse:
    
    # The list of available Spark node types.
    node_types: 'List[NodeType]' = None

    def as_request(self) -> (dict, dict):
        listNodeTypesResponse_query, listNodeTypesResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.node_types:
            listNodeTypesResponse_body['node_types'] = [v.as_request()[1] for v in self.node_types]
        
        return listNodeTypesResponse_query, listNodeTypesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListNodeTypesResponse':
        return cls(
            node_types=[NodeType.from_dict(v) for v in d['node_types']] if 'node_types' in d else None,
        )



@dataclass
class LogAnalyticsInfo:
    
    # <needs content added>
    log_analytics_primary_key: str = None
    # <needs content added>
    log_analytics_workspace_id: str = None

    def as_request(self) -> (dict, dict):
        logAnalyticsInfo_query, logAnalyticsInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.log_analytics_primary_key:
            logAnalyticsInfo_body['log_analytics_primary_key'] = self.log_analytics_primary_key
        if self.log_analytics_workspace_id:
            logAnalyticsInfo_body['log_analytics_workspace_id'] = self.log_analytics_workspace_id
        
        return logAnalyticsInfo_query, logAnalyticsInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogAnalyticsInfo':
        return cls(
            log_analytics_primary_key=d.get('log_analytics_primary_key', None),
            log_analytics_workspace_id=d.get('log_analytics_workspace_id', None),
        )



@dataclass
class LogSyncStatus:
    
    # The timestamp of last attempt. If the last attempt fails,
    # ``last_exception`` will contain the exception in the last attempt.
    last_attempted: int = None
    # The exception thrown in the last attempt, it would be null (omitted in the
    # response) if there is no exception in last attempted.
    last_exception: str = None

    def as_request(self) -> (dict, dict):
        logSyncStatus_query, logSyncStatus_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.last_attempted:
            logSyncStatus_body['last_attempted'] = self.last_attempted
        if self.last_exception:
            logSyncStatus_body['last_exception'] = self.last_exception
        
        return logSyncStatus_query, logSyncStatus_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LogSyncStatus':
        return cls(
            last_attempted=d.get('last_attempted', None),
            last_exception=d.get('last_exception', None),
        )



@dataclass
class NodeInstanceType:
    
    
    instance_type_id: str = None
    
    local_disk_size_gb: int = None
    
    local_disks: int = None
    
    local_nvme_disk_size_gb: int = None
    
    local_nvme_disks: int = None

    def as_request(self) -> (dict, dict):
        nodeInstanceType_query, nodeInstanceType_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.instance_type_id:
            nodeInstanceType_body['instance_type_id'] = self.instance_type_id
        if self.local_disk_size_gb:
            nodeInstanceType_body['local_disk_size_gb'] = self.local_disk_size_gb
        if self.local_disks:
            nodeInstanceType_body['local_disks'] = self.local_disks
        if self.local_nvme_disk_size_gb:
            nodeInstanceType_body['local_nvme_disk_size_gb'] = self.local_nvme_disk_size_gb
        if self.local_nvme_disks:
            nodeInstanceType_body['local_nvme_disks'] = self.local_nvme_disks
        
        return nodeInstanceType_query, nodeInstanceType_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NodeInstanceType':
        return cls(
            instance_type_id=d.get('instance_type_id', None),
            local_disk_size_gb=d.get('local_disk_size_gb', None),
            local_disks=d.get('local_disks', None),
            local_nvme_disk_size_gb=d.get('local_nvme_disk_size_gb', None),
            local_nvme_disks=d.get('local_nvme_disks', None),
        )



@dataclass
class NodeType:
    
    # A string description associated with this node type, e.g., "r3.xlarge".
    description: str
    # An identifier for the type of hardware that this node runs on, e.g.,
    # "r3.2xlarge" in AWS.
    instance_type_id: str
    # Memory (in MB) available for this node type.
    memory_mb: int
    # Unique identifier for this node type.
    node_type_id: str
    # Number of CPU cores available for this node type. Note that this can be
    # fractional, e.g., 2.5 cores, if the the number of cores on a machine
    # instance is not divisible by the number of Spark nodes on that machine.
    num_cores: float
    
    category: str = None
    
    display_order: int = None
    # Whether the node type is deprecated. Non-deprecated node types offer
    # greater performance.
    is_deprecated: bool = None
    # AWS specific, whether this instance supports encryption in transit, used
    # for hipaa and pci workloads.
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

    def as_request(self) -> (dict, dict):
        nodeType_query, nodeType_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.category:
            nodeType_body['category'] = self.category
        if self.description:
            nodeType_body['description'] = self.description
        if self.display_order:
            nodeType_body['display_order'] = self.display_order
        if self.instance_type_id:
            nodeType_body['instance_type_id'] = self.instance_type_id
        if self.is_deprecated:
            nodeType_body['is_deprecated'] = self.is_deprecated
        if self.is_encrypted_in_transit:
            nodeType_body['is_encrypted_in_transit'] = self.is_encrypted_in_transit
        if self.is_graviton:
            nodeType_body['is_graviton'] = self.is_graviton
        if self.is_hidden:
            nodeType_body['is_hidden'] = self.is_hidden
        if self.is_io_cache_enabled:
            nodeType_body['is_io_cache_enabled'] = self.is_io_cache_enabled
        if self.memory_mb:
            nodeType_body['memory_mb'] = self.memory_mb
        if self.node_info:
            nodeType_body['node_info'] = self.node_info.as_request()[1]
        if self.node_instance_type:
            nodeType_body['node_instance_type'] = self.node_instance_type.as_request()[1]
        if self.node_type_id:
            nodeType_body['node_type_id'] = self.node_type_id
        if self.num_cores:
            nodeType_body['num_cores'] = self.num_cores
        if self.num_gpus:
            nodeType_body['num_gpus'] = self.num_gpus
        if self.photon_driver_capable:
            nodeType_body['photon_driver_capable'] = self.photon_driver_capable
        if self.photon_worker_capable:
            nodeType_body['photon_worker_capable'] = self.photon_worker_capable
        if self.support_cluster_tags:
            nodeType_body['support_cluster_tags'] = self.support_cluster_tags
        if self.support_ebs_volumes:
            nodeType_body['support_ebs_volumes'] = self.support_ebs_volumes
        if self.support_port_forwarding:
            nodeType_body['support_port_forwarding'] = self.support_port_forwarding
        
        return nodeType_query, nodeType_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'NodeType':
        return cls(
            category=d.get('category', None),
            description=d.get('description', None),
            display_order=d.get('display_order', None),
            instance_type_id=d.get('instance_type_id', None),
            is_deprecated=d.get('is_deprecated', None),
            is_encrypted_in_transit=d.get('is_encrypted_in_transit', None),
            is_graviton=d.get('is_graviton', None),
            is_hidden=d.get('is_hidden', None),
            is_io_cache_enabled=d.get('is_io_cache_enabled', None),
            memory_mb=d.get('memory_mb', None),
            node_info=CloudProviderNodeInfo.from_dict(d['node_info']) if 'node_info' in d else None,
            node_instance_type=NodeInstanceType.from_dict(d['node_instance_type']) if 'node_instance_type' in d else None,
            node_type_id=d.get('node_type_id', None),
            num_cores=d.get('num_cores', None),
            num_gpus=d.get('num_gpus', None),
            photon_driver_capable=d.get('photon_driver_capable', None),
            photon_worker_capable=d.get('photon_worker_capable', None),
            support_cluster_tags=d.get('support_cluster_tags', None),
            support_ebs_volumes=d.get('support_ebs_volumes', None),
            support_port_forwarding=d.get('support_port_forwarding', None),
        )



@dataclass
class PermanentDeleteCluster:
    
    # The cluster to be deleted.
    cluster_id: str

    def as_request(self) -> (dict, dict):
        permanentDeleteCluster_query, permanentDeleteCluster_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cluster_id:
            permanentDeleteCluster_body['cluster_id'] = self.cluster_id
        
        return permanentDeleteCluster_query, permanentDeleteCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PermanentDeleteCluster':
        return cls(
            cluster_id=d.get('cluster_id', None),
        )



@dataclass
class PinCluster:
    
    # <needs content added>
    cluster_id: str

    def as_request(self) -> (dict, dict):
        pinCluster_query, pinCluster_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cluster_id:
            pinCluster_body['cluster_id'] = self.cluster_id
        
        return pinCluster_query, pinCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PinCluster':
        return cls(
            cluster_id=d.get('cluster_id', None),
        )



@dataclass
class ResizeCluster:
    
    # The cluster to be resized.
    cluster_id: str
    # Parameters needed in order to automatically scale clusters up and down
    # based on load. Note: autoscaling works best with DB runtime versions 3.0
    # or later.
    autoscale: 'AutoScale' = None
    # Number of worker nodes that this cluster should have. A cluster has one
    # Spark Driver and ``num_workers`` Executors for a total of ``num_workers``
    # + 1 Spark nodes.
    # 
    # Note: When reading the properties of a cluster, this field reflects the
    # desired number of workers rather than the actual current number of
    # workers. For instance, if a cluster is resized from 5 to 10 workers, this
    # field will immediately be updated to reflect the target size of 10
    # workers, whereas the workers listed in ``spark_info`` will gradually
    # increase from 5 to 10 as the new nodes are provisioned.
    num_workers: int = None

    def as_request(self) -> (dict, dict):
        resizeCluster_query, resizeCluster_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.autoscale:
            resizeCluster_body['autoscale'] = self.autoscale.as_request()[1]
        if self.cluster_id:
            resizeCluster_body['cluster_id'] = self.cluster_id
        if self.num_workers:
            resizeCluster_body['num_workers'] = self.num_workers
        
        return resizeCluster_query, resizeCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResizeCluster':
        return cls(
            autoscale=AutoScale.from_dict(d['autoscale']) if 'autoscale' in d else None,
            cluster_id=d.get('cluster_id', None),
            num_workers=d.get('num_workers', None),
        )



@dataclass
class RestartCluster:
    
    # The cluster to be started.
    cluster_id: str
    # <needs content added>
    restart_user: str = None

    def as_request(self) -> (dict, dict):
        restartCluster_query, restartCluster_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cluster_id:
            restartCluster_body['cluster_id'] = self.cluster_id
        if self.restart_user:
            restartCluster_body['restart_user'] = self.restart_user
        
        return restartCluster_query, restartCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RestartCluster':
        return cls(
            cluster_id=d.get('cluster_id', None),
            restart_user=d.get('restart_user', None),
        )



@dataclass
class S3StorageInfo:
    
    # (Optional) Set canned access control list for the logs, e.g.
    # ``bucket-owner-full-control``. If ``canned_cal`` is set, please make sure
    # the cluster iam role has ``s3:PutObjectAcl`` permission on the destination
    # bucket and prefix. The full list of possible canned acl can be found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl.
    # Please also note that by default only the object owner gets full controls.
    # If you are using cross account role for writing data, you may want to set
    # ``bucket-owner-full-control`` to make bucket owner able to read the logs.
    canned_acl: str = None
    # S3 destination, e.g. ``s3://my-bucket/some-prefix`` Note that logs will be
    # delivered using cluster iam role, please make sure you set cluster iam
    # role and the role has write access to the destination. Please also note
    # that you cannot use AWS keys to deliver logs.
    destination: str = None
    # (Optional) Flag to enable server side encryption, ``false`` by default.
    enable_encryption: bool = None
    # (Optional) The encryption type, it could be ``sse-s3`` or ``sse-kms``. It
    # will be used only when encryption is enabled and the default type is
    # ``sse-s3``.
    encryption_type: str = None
    # S3 endpoint, e.g. ``https://s3-us-west-2.amazonaws.com``. Either region or
    # endpoint needs to be set. If both are set, endpoint will be used.
    endpoint: str = None
    # (Optional) Kms key which will be used if encryption is enabled and
    # encryption type is set to ``sse-kms``.
    kms_key: str = None
    # S3 region, e.g. ``us-west-2``. Either region or endpoint needs to be set.
    # If both are set, endpoint will be used.
    region: str = None

    def as_request(self) -> (dict, dict):
        s3StorageInfo_query, s3StorageInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.canned_acl:
            s3StorageInfo_body['canned_acl'] = self.canned_acl
        if self.destination:
            s3StorageInfo_body['destination'] = self.destination
        if self.enable_encryption:
            s3StorageInfo_body['enable_encryption'] = self.enable_encryption
        if self.encryption_type:
            s3StorageInfo_body['encryption_type'] = self.encryption_type
        if self.endpoint:
            s3StorageInfo_body['endpoint'] = self.endpoint
        if self.kms_key:
            s3StorageInfo_body['kms_key'] = self.kms_key
        if self.region:
            s3StorageInfo_body['region'] = self.region
        
        return s3StorageInfo_query, s3StorageInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'S3StorageInfo':
        return cls(
            canned_acl=d.get('canned_acl', None),
            destination=d.get('destination', None),
            enable_encryption=d.get('enable_encryption', None),
            encryption_type=d.get('encryption_type', None),
            endpoint=d.get('endpoint', None),
            kms_key=d.get('kms_key', None),
            region=d.get('region', None),
        )



@dataclass
class SparkNode:
    
    # The private IP address of the host instance.
    host_private_ip: str = None
    # Globally unique identifier for the host instance from the cloud provider.
    instance_id: str = None
    # Attributes specific to AWS for a Spark node.
    node_aws_attributes: 'SparkNodeAwsAttributes' = None
    # Globally unique identifier for this node.
    node_id: str = None
    # Private IP address (typically a 10.x.x.x address) of the Spark node. Note
    # that this is different from the private IP address of the host instance.
    private_ip: str = None
    # Public DNS address of this node. This address can be used to access the
    # Spark JDBC server on the driver node. To communicate with the JDBC server,
    # traffic must be manually authorized by adding security group rules to the
    # "worker-unmanaged" security group via the AWS console.
    # 
    # Actually it's the public DNS address of the host instance.
    public_dns: str = None
    # The timestamp (in millisecond) when the Spark node is launched.
    # 
    # The start_timestamp is set right before the container is being launched.
    # The timestamp when the container is placed on the ResourceManager, before
    # its launch and setup by the NodeDaemon. This timestamp is the same as the
    # creation timestamp in the database.
    start_timestamp: int = None

    def as_request(self) -> (dict, dict):
        sparkNode_query, sparkNode_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.host_private_ip:
            sparkNode_body['host_private_ip'] = self.host_private_ip
        if self.instance_id:
            sparkNode_body['instance_id'] = self.instance_id
        if self.node_aws_attributes:
            sparkNode_body['node_aws_attributes'] = self.node_aws_attributes.as_request()[1]
        if self.node_id:
            sparkNode_body['node_id'] = self.node_id
        if self.private_ip:
            sparkNode_body['private_ip'] = self.private_ip
        if self.public_dns:
            sparkNode_body['public_dns'] = self.public_dns
        if self.start_timestamp:
            sparkNode_body['start_timestamp'] = self.start_timestamp
        
        return sparkNode_query, sparkNode_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkNode':
        return cls(
            host_private_ip=d.get('host_private_ip', None),
            instance_id=d.get('instance_id', None),
            node_aws_attributes=SparkNodeAwsAttributes.from_dict(d['node_aws_attributes']) if 'node_aws_attributes' in d else None,
            node_id=d.get('node_id', None),
            private_ip=d.get('private_ip', None),
            public_dns=d.get('public_dns', None),
            start_timestamp=d.get('start_timestamp', None),
        )



@dataclass
class SparkNodeAwsAttributes:
    
    # Whether this node is on an Amazon spot instance.
    is_spot: bool = None

    def as_request(self) -> (dict, dict):
        sparkNodeAwsAttributes_query, sparkNodeAwsAttributes_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.is_spot:
            sparkNodeAwsAttributes_body['is_spot'] = self.is_spot
        
        return sparkNodeAwsAttributes_query, sparkNodeAwsAttributes_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkNodeAwsAttributes':
        return cls(
            is_spot=d.get('is_spot', None),
        )



@dataclass
class SparkVersion:
    
    # Spark version key, for example "2.1.x-scala2.11". This is the value which
    # should be provided as the "spark_version" when creating a new cluster.
    # Note that the exact Spark version may change over time for a "wildcard"
    # version (i.e., "2.1.x-scala2.11" is a "wildcard" version) with minor bug
    # fixes.
    key: str = None
    # A descriptive name for this Spark version, for example "Spark 2.1".
    name: str = None

    def as_request(self) -> (dict, dict):
        sparkVersion_query, sparkVersion_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.key:
            sparkVersion_body['key'] = self.key
        if self.name:
            sparkVersion_body['name'] = self.name
        
        return sparkVersion_query, sparkVersion_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparkVersion':
        return cls(
            key=d.get('key', None),
            name=d.get('name', None),
        )



@dataclass
class StartCluster:
    
    # The cluster to be started.
    cluster_id: str

    def as_request(self) -> (dict, dict):
        startCluster_query, startCluster_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cluster_id:
            startCluster_body['cluster_id'] = self.cluster_id
        
        return startCluster_query, startCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StartCluster':
        return cls(
            cluster_id=d.get('cluster_id', None),
        )



@dataclass
class TerminationReason:
    
    # status code indicating why the cluster was terminated
    code: 'TerminationReasonCode' = None
    # list of parameters that provide additional information about why the
    # cluster was terminated
    parameters: 'Dict[str,str]' = None
    # type of the termination
    type: 'TerminationReasonType' = None

    def as_request(self) -> (dict, dict):
        terminationReason_query, terminationReason_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.code:
            terminationReason_body['code'] = self.code.value
        if self.parameters:
            terminationReason_body['parameters'] = self.parameters
        if self.type:
            terminationReason_body['type'] = self.type.value
        
        return terminationReason_query, terminationReason_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TerminationReason':
        return cls(
            code=TerminationReasonCode(d['code']) if 'code' in d else None,
            parameters=d.get('parameters', None),
            type=TerminationReasonType(d['type']) if 'type' in d else None,
        )



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
    
    # <needs content added>
    cluster_id: str

    def as_request(self) -> (dict, dict):
        unpinCluster_query, unpinCluster_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cluster_id:
            unpinCluster_body['cluster_id'] = self.cluster_id
        
        return unpinCluster_query, unpinCluster_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UnpinCluster':
        return cls(
            cluster_id=d.get('cluster_id', None),
        )



@dataclass
class WorkloadType:
    
    # defined what type of clients can use the cluster. E.g. Notebooks, Jobs
    clients: 'ClientsTypes' = None

    def as_request(self) -> (dict, dict):
        workloadType_query, workloadType_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.clients:
            workloadType_body['clients'] = self.clients.as_request()[1]
        
        return workloadType_query, workloadType_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WorkloadType':
        return cls(
            clients=ClientsTypes.from_dict(d['clients']) if 'clients' in d else None,
        )



@dataclass
class GetRequest:
    
    # The cluster about which to retrieve information.
    cluster_id: str # query

    def as_request(self) -> (dict, dict):
        getRequest_query, getRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cluster_id:
            getRequest_query['cluster_id'] = self.cluster_id
        
        return getRequest_query, getRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRequest':
        return cls(
            cluster_id=d.get('cluster_id', None),
        )



@dataclass
class ListRequest:
    
    # Filter clusters based on what type of client it can be used for. Could be
    # either NOTEBOOKS or JOBS. No input for this field will get all clusters in
    # the workspace without filtering on its supported client
    can_use_client: str = None # query

    def as_request(self) -> (dict, dict):
        listRequest_query, listRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.can_use_client:
            listRequest_query['can_use_client'] = self.can_use_client
        
        return listRequest_query, listRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRequest':
        return cls(
            can_use_client=d.get('can_use_client', None),
        )



class ClustersAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def changeOwner(self, request: ChangeClusterOwner):
        """Change cluster owner
        
        Change the owner of the cluster. You must be an admin to perform this
        operation."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/clusters/change-owner', query=query, body=body)
        
    
    def create(self, request: CreateCluster) -> CreateClusterResponse:
        """Create new cluster
        
        Creates a new Spark cluster. This method will acquire new instances from
        the cloud provider if necessary. This method is asynchronous; the
        returned ``cluster_id`` can be used to poll the cluster status. When
        this method returns, the cluster will be in\na ``PENDING`` state. The
        cluster will be usable once it enters a ``RUNNING`` state.
        
        Note: Databricks may not be able to acquire some of the requested nodes,
        due to cloud provider limitations (account limits, spot price, etc.) or
        transient network issues.
        
        If Databricks acquires at least 85% of the requested on-demand nodes,
        cluster creation will succeed. Otherwise the cluster will terminate with
        an informative error message."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/clusters/create', query=query, body=body)
        return CreateClusterResponse.from_dict(json)
    
    def delete(self, request: DeleteCluster):
        """Terminate cluster
        
        Terminates the Spark cluster with the specified ID. The cluster is
        removed asynchronously. Once the termination has completed, the cluster
        will be in a ``TERMINATED`` state. If the cluster is already in a
        ``TERMINATING`` or ``TERMINATED`` state, nothing will happen."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/clusters/delete', query=query, body=body)
        
    
    def edit(self, request: EditCluster):
        """Update cluster configuration
        
        Updates the configuration of a cluster to match the provided attributes
        and size. A cluster can be updated if it is in a ``RUNNING`` or
        ``TERMINATED`` state.
        
        If a cluster is updated while in a ``RUNNING`` state, it will be
        restarted so that the new attributes can take effect.
        
        If a cluster is updated while in a ``TERMINATED`` state, it will remain
        ``TERMINATED``. The next time it is started using the ``clusters/start``
        API, the new attributes will take effect. Any attempt to update a
        cluster in any other state will be rejected with an ``INVALID_STATE``
        error code.
        
        Clusters created by the Databricks Jobs service cannot be edited."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/clusters/edit', query=query, body=body)
        
    
    def events(self, request: GetEvents) -> GetEventsResponse:
        """List cluster activity events
        
        Retrieves a list of events about the activity of a cluster. This API is
        paginated. If there are more events to read, the response includes all
        the nparameters necessary to request the next page of events."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/clusters/events', query=query, body=body)
        return GetEventsResponse.from_dict(json)
    
    def get(self, request: GetRequest) -> ClusterInfo:
        """Get cluster info
        
        "Retrieves the information for a cluster given its identifier. Clusters
        can be described while they are running, or up to 60 days after they are
        terminated."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/clusters/get', query=query, body=body)
        return ClusterInfo.from_dict(json)
    
    def list(self, request: ListRequest) -> ListClustersResponse:
        """List all clusters
        
        Returns information about all pinned clusters, currently active
        clusters, up to 70 of the most recently terminated interactive clusters
        in the past 7 days, and up to 30 of the most recently terminated job
        clusters in the past 7 days.
        
        For example, if there is 1 pinned cluster, 4 active clusters, 45
        terminated interactive clusters in the past 7 days, and 50 terminated
        job clusters\nin the past 7 days, then this API returns the 1 pinned
        cluster, 4 active clusters, all 45 terminated interactive clusters, and
        the 30 most recently terminated job clusters."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/clusters/list', query=query, body=body)
        return ListClustersResponse.from_dict(json)
    
    def listNodeTypes(self) -> ListNodeTypesResponse:
        """List node types
        
        Returns a list of supported Spark node types. These node types can be
        used to launch a cluster."""
        
        json = self._api.do('GET', '/api/2.0/clusters/list-node-types')
        return ListNodeTypesResponse.from_dict(json)
    
    def listZones(self) -> ListAvailableZonesResponse:
        """List availability zones
        
        Returns a list of availability zones where clusters can be created in
        (For example, us-west-2a). These zones can be used to launch a cluster."""
        
        json = self._api.do('GET', '/api/2.0/clusters/list-zones')
        return ListAvailableZonesResponse.from_dict(json)
    
    def permanentDelete(self, request: PermanentDeleteCluster):
        """Permanently delete cluster
        
        Permanently deletes a Spark cluster. This cluster is terminated and
        resources are asynchronously removed.
        
        In addition, users will no longer see permanently deleted clusters in
        the cluster list, and API users can no longer perform any action on
        permanently deleted clusters."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/clusters/permanent-delete', query=query, body=body)
        
    
    def pin(self, request: PinCluster):
        """Pin cluster
        
        Pinning a cluster ensures that the cluster will always be returned by
        the ListClusters API. Pinning a cluster that is already pinned will have
        no effect. This API can only be called by workspace admins."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/clusters/pin', query=query, body=body)
        
    
    def resize(self, request: ResizeCluster):
        """Resize cluster
        
        Resizes a cluster to have a desired number of workers. This will fail
        unless the cluster is in a `RUNNING` state."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/clusters/resize', query=query, body=body)
        
    
    def restart(self, request: RestartCluster):
        """Restart cluster
        
        Restarts a Spark cluster with the supplied ID. If the cluster is not
        currently in a `RUNNING` state, nothing will happen."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/clusters/restart', query=query, body=body)
        
    
    def sparkVersions(self) -> GetSparkVersionsResponse:
        """List available Spark versions
        
        Returns the list of available Spark versions. These versions can be used
        to launch a cluster."""
        
        json = self._api.do('GET', '/api/2.0/clusters/spark-versions')
        return GetSparkVersionsResponse.from_dict(json)
    
    def start(self, request: StartCluster):
        """Start terminated cluster
        
        Starts a terminated Spark cluster with the supplied ID. This works
        similar to `createCluster` except:
        
        * The previous cluster id and attributes are preserved. * The cluster
        starts with the last specified cluster size. * If the previous cluster
        was an autoscaling cluster, the current cluster starts with the minimum
        number of nodes. * If the cluster is not currently in a ``TERMINATED``
        state, nothing will happen. * Clusters launched to run a job cannot be
        started."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/clusters/start', query=query, body=body)
        
    
    def unpin(self, request: UnpinCluster):
        """Unpin cluster
        
        Unpinning a cluster will allow the cluster to eventually be removed from
        the ListClusters API. Unpinning a cluster that is not pinned will have
        no effect. This API can only be called by workspace admins."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/clusters/unpin', query=query, body=body)
        
    